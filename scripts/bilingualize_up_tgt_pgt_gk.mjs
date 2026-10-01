#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import * as cheerio from 'cheerio';
import { jsonrepair } from 'jsonrepair';
import { upTgtPgtGkLanguageRuntimeTag, upTgtPgtGkRuntimeSrc } from './lib/up-tgt-pgt-gk-runtime.mjs';

const ROOT = process.cwd();
const GK_ROOT = path.join(ROOT, 'up-tgt-pgt-gk');
const MODEL = process.env.GEMINI_MODEL || 'gemini-3.5-flash-lite';
const args = process.argv.slice(2);
const hasFlag = (flag) => args.includes(flag);
const argValue = (flag) => { const i = args.indexOf(flag); return i >= 0 ? args[i + 1] : null; };
const force = hasFlag('--force');
const limit = Math.max(0, Number.parseInt(argValue('--limit') || '0', 10) || 0);
const maxAttempts = Math.max(1, Number.parseInt(argValue('--attempts') || '3', 10) || 3);
const apiKey = process.env.GEMINI_API_KEY_2 || process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY || process.env.GOOGLE_API_KEY;
if (!apiKey) throw new Error('Set GEMINI_API_KEY, GEMINI_API_KEY_1 or GOOGLE_API_KEY before translation.');
const ai = new GoogleGenAI({ apiKey });
const requestGapMs = Math.max(0, Number.parseInt(process.env.GEMINI_REQUEST_GAP_MS || '4500', 10) || 4500);
let lastApiRequestAt = 0;

async function waitForApiSlot() {
  const waitMs = Math.max(0, requestGapMs - (Date.now() - lastApiRequestAt));
  if (waitMs) await new Promise((resolve) => setTimeout(resolve, waitMs));
  lastApiRequestAt = Date.now();
}

function parseJson(raw) {
  const clean = String(raw || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  try { return JSON.parse(clean); } catch (firstError) {
    try { return JSON.parse(jsonrepair(clean)); } catch { throw new Error(`Gemini JSON parse failed: ${firstError.message}`); }
  }
}

function safeJson(value) {
  return JSON.stringify(value).replace(/</g, '\\u003c').replace(/>/g, '\\u003e').replace(/&/g, '\\u0026');
}

function cleanText(value) { return String(value || '').replace(/\s+/g, ' ').trim(); }

function normalizeDocument(html) {
  const source = String(html || '');
  if (/<(?:!doctype|html\b)/i.test(source)) return source;
  const headerStart = source.search(/<header\b/i);
  if (headerStart < 0) throw new Error('Could not locate page header in an incomplete HTML document');
  return `<!doctype html><html lang="en"><head>${source.slice(0, headerStart)}</head><body>${source.slice(headerStart)}</body></html>`;
}

function readPage(file) {
  const html = normalizeDocument(fs.readFileSync(file, 'utf8'));
  const $ = cheerio.load(html, { decodeEntities: false });
  let quiz = [];
  let test = [];
  try { quiz = JSON.parse($('#quiz-data').text() || '[]'); } catch { quiz = []; }
  try { test = JSON.parse($('#test-data').text() || '[]'); } catch { test = []; }
  const entries = [];
  const elements = [];
  const add = (id, text) => { const value = cleanText(text); if (value) entries.push({ id, text: value }); };

  $('body *').each((_, element) => {
    const tag = String(element.tagName || '').toLowerCase();
    const node = $(element);
    if (['script', 'style', 'noscript', 'input', 'textarea'].includes(tag)) return;
    if (node.closest('.question-source-data').length || node.children().length) return;
    const text = cleanText(node.text());
    if (!text || /^\d+[Qq]$/.test(text)) return;
    const id = `element-${elements.length + 1}`;
    node.attr('data-bilingual-id', id);
    elements.push(id);
    add(id, text);
  });

  add('page-title', $('title').text());
  add('page-description', $('meta[name="description"]').attr('content'));

  const addQuestionEntries = (questions, prefix) => questions.forEach((question, index) => {
    for (const [key, value] of Object.entries(question || {})) {
      if (['id', 'concept_id', 'type', 'correct_index'].includes(key)) continue;
      if (['question', 'options'].includes(key)) continue;
      if (typeof value === 'string') add(`${prefix}-${index}-${key}`, value);
      else if (Array.isArray(value)) value.forEach((item, itemIndex) => {
        if (typeof item === 'string') add(`${prefix}-${index}-${key}-${itemIndex}`, item);
      });
    }
  });
  addQuestionEntries(quiz, 'quiz');
  addQuestionEntries(test, 'test');
  return { html, $, quiz, test, entries, elements };
}

function splitEntries(entries) {
  const chunks = [];
  const uniqueEntries = [...new Map(entries.map((entry) => [entry.text, entry])).values()];
  let current = [];
  let chars = 0;
  for (const entry of uniqueEntries) {
    if (current.length && (current.length >= 70 || chars + entry.text.length > 18000)) {
      chunks.push(current); current = []; chars = 0;
    }
    current.push(entry); chars += entry.text.length;
  }
  if (current.length) chunks.push(current);
  return chunks;
}

async function translateChunk(entries) {
  const prompt = `Translate the following educational webpage strings from English to natural, accurate Hindi for UP TGT/PGT exam preparation. Return JSON only in the exact shape {"translations":[{"id":"same id","hi":"Hindi translation"}]}. Preserve dates, numbers, formulas, names, Articles, abbreviations and technical terms; keep important English technical terms in parentheses when useful. Do not omit, merge or reorder any item.\n\n${JSON.stringify(entries)}`;
  let lastError;
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      await waitForApiSlot();
      const response = await ai.models.generateContent({ model: MODEL, contents: prompt, config: { temperature: 0.1, responseMimeType: 'application/json' } });
      const data = parseJson(response?.text);
      if (!Array.isArray(data?.translations)) throw new Error('translation response has no translations array');
      const map = new Map(data.translations.filter((item) => item && item.id && typeof item.hi === 'string').map((item) => [item.id, item.hi.trim()]));
      const missing = entries.filter((entry) => !map.get(entry.id));
      if (missing.length) {
        for (const entry of missing) {
          const singlePrompt = `Translate this one educational webpage string from English to natural, accurate Hindi for UP TGT/PGT exam preparation. Return JSON only in the exact shape {"id":"${entry.id}","hi":"Hindi translation"}. Preserve dates, numbers, formulas, names, Articles, abbreviations and technical terms; keep important English technical terms in parentheses when useful. String: ${JSON.stringify(entry.text)}`;
          await waitForApiSlot();
          const singleResponse = await ai.models.generateContent({ model: MODEL, contents: singlePrompt, config: { temperature: 0.1, responseMimeType: 'application/json' } });
          const single = parseJson(singleResponse?.text);
          if (single?.id !== entry.id || typeof single.hi !== 'string' || !single.hi.trim()) throw new Error(`single-string repair failed for ${entry.id}`);
          map.set(entry.id, single.hi.trim());
        }
      }
      return map;
    } catch (error) {
      lastError = error;
      if (attempt < maxAttempts) await new Promise((resolve) => setTimeout(resolve, attempt * 3000));
    }
  }
  throw lastError || new Error('translation failed');
}

function translateQuestions(questions, prefix, translations) {
  return questions.map((question, index) => {
    const translated = { ...question };
    for (const [key, value] of Object.entries(question || {})) {
      if (['id', 'concept_id', 'type', 'correct_index'].includes(key)) continue;
      if (typeof value === 'string') translated[key] = translations.get(`${prefix}-${index}-${key}`) || value;
      else if (Array.isArray(value)) translated[key] = value.map((item, itemIndex) => typeof item === 'string' ? (translations.get(`${prefix}-${index}-${key}-${itemIndex}`) || item) : item);
    }
    return translated;
  });
}

function patchPage(page, translations) {
  const { $, quiz, test, elements } = page;
  if ($(`script[src="${upTgtPgtGkRuntimeSrc}"][data-up-tgt-pgt-gk-runtime="topic"]`).length !== 1) {
    throw new Error('The shared GK topic runtime must be present before bilingualizing a page.');
  }
  const elementTranslations = Object.fromEntries(elements.map((id) => [id, translations.get(id)]).filter(([, value]) => value));
  const hiQuiz = translateQuestions(quiz, 'quiz', translations);
  const hiTest = translateQuestions(test, 'test', translations);
  const bilingualData = { elements: elementTranslations, meta: { title: translations.get('page-title') || $('title').text(), description: translations.get('page-description') || $('meta[name="description"]').attr('content') || '' }, quiz: hiQuiz, test: hiTest };

  if (!$('#btn-language-toggle').length) $('.header-actions').first().prepend('<button type="button" class="language-toggle-btn" id="btn-language-toggle">हिन्दी</button>');
  if (!$('#bilingual-style').length) $('head').append('<style id="bilingual-style">.language-toggle-btn{min-height:42px;padding:0 14px;border:1px solid var(--line,#d8dee8);border-radius:999px;background:var(--paper,#fff);color:var(--ink,#16324f);font:inherit;font-weight:800;cursor:pointer}.language-toggle-btn:hover{border-color:var(--accent,#b45309)}[data-bilingual-id]{transition:none}</style>');
  $('#bilingual-data').remove();
  const bilingualMarkup = `<script type="application/json" id="bilingual-data">${safeJson(bilingualData)}</script>${upTgtPgtGkLanguageRuntimeTag}`;

  let output = $.html();
  const bodyStart = output.search(/<body\b[^>]*>/i);
  if (bodyStart < 0) throw new Error('Could not locate body element while adding bilingual payload');
  const bodyEnd = output.indexOf('>', bodyStart) + 1;
  output = output.slice(0, bodyEnd) + bilingualMarkup + output.slice(bodyEnd);
  return output;
}

async function main() {
  const files = [];
  for (const entry of fs.readdirSync(GK_ROOT, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name === 'current-affairs') continue;
    const moduleDir = path.join(GK_ROOT, entry.name);
    const walk = (dir) => { for (const child of fs.readdirSync(dir, { withFileTypes: true })) { const full = path.join(dir, child.name); if (child.isDirectory()) walk(full); else if (child.name === 'index.html' && dir !== moduleDir) files.push(full); } };
    walk(moduleDir);
  }
  files.sort();
  const targets = limit ? files.slice(0, limit) : files;
  console.log(`Bilingualizing ${targets.length} GK page(s). Hindi is default. Model: ${MODEL}`);
  for (const file of targets) {
    const alreadyBilingual = fs.readFileSync(file, 'utf8').includes('id="bilingual-data"');
    const page = readPage(file);
    if (!force && alreadyBilingual) { console.log(`Skipped ${file} (already bilingual)`); continue; }
    const uniqueStringCount = new Set(page.entries.map((entry) => entry.text)).size;
    console.log(`Translating ${file} (${page.entries.length} strings; ${uniqueStringCount} unique)`);
    const translations = new Map();
    for (const chunk of splitEntries(page.entries)) {
      const translated = await translateChunk(chunk);
      for (const [id, value] of translated) translations.set(id, value);
    }
    const byText = new Map(page.entries.map((entry) => [entry.text, translations.get(entry.id)]).filter(([, value]) => value));
    const expandedTranslations = new Map(page.entries.map((entry) => [entry.id, translations.get(entry.id) || byText.get(entry.text)]));
    fs.writeFileSync(file, patchPage(page, expandedTranslations), 'utf8');
    console.log(`  saved ${file}`);
  }
}

main().catch((error) => { console.error(`Bilingual generation failed: ${error.message}`); process.exitCode = 1; });
