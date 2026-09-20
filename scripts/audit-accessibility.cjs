#!/usr/bin/env node

const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');

const ROOT = process.cwd();
const SKIP_DIRS = new Set(['.git', 'node_modules']);
const SAMPLE_LIMIT = 12;

const totals = {
  files: 0,
  images: 0,
  imagesMissingAlt: 0,
  buttons: 0,
  buttonsUnnamed: 0,
  links: 0,
  linksUnnamed: 0,
  formControls: 0,
  controlsUnlabelled: 0,
  iframes: 0,
  iframesMissingTitle: 0,
};

const perFile = new Map();
const samples = {
  imagesMissingAlt: [],
  buttonsUnnamed: [],
  linksUnnamed: [],
  controlsUnlabelled: [],
  iframesMissingTitle: [],
};

function relativeFile(file) {
  return path.relative(ROOT, file).replaceAll(path.sep, '/');
}

function addFinding(kind, file, detail) {
  const key = relativeFile(file);
  const current = perFile.get(key) || {};
  current[kind] = (current[kind] || 0) + 1;
  perFile.set(key, current);
  if (samples[kind].length < SAMPLE_LIMIT) {
    samples[kind].push({ file: key, detail });
  }
}

function hasAccessibleName($, element) {
  const node = $(element);
  const labelledBy = node.attr('aria-labelledby');
  return Boolean(
    node.text().replace(/\s+/g, ' ').trim()
      || node.attr('aria-label')
      || (labelledBy && labelledBy.split(/\s+/).some((id) => $('#' + id).text().trim()))
      || node.attr('title')
      || node.find('img[alt]').attr('alt')
      || node.find('svg[aria-label], svg title').text().trim()
  );
}

function isHiddenControl($, element) {
  const node = $(element);
  return node.attr('type') === 'hidden'
    || node.attr('aria-hidden') === 'true'
    || node.is('[hidden]')
    || node.closest('[aria-hidden="true"], [hidden], template').length > 0;
}

function isLabelledControl($, element) {
  const node = $(element);
  const id = node.attr('id');
  const labelledBy = node.attr('aria-labelledby');
  return Boolean(
    node.attr('aria-label')
      || (labelledBy && labelledBy.split(/\s+/).some((labelId) => $('#' + labelId).text().trim()))
      || (id && $('label[for="' + id + '"]').length)
      || node.closest('label').length
      || node.attr('title')
      || (['button', 'submit', 'reset', 'image'].includes(node.attr('type')) && (node.attr('value') || node.text().trim()))
  );
}

function inspectFile(file) {
  const $ = cheerio.load(fs.readFileSync(file, 'utf8'));

  $('img').each((_, element) => {
    totals.images += 1;
    if ($(element).attr('alt') === undefined) {
      totals.imagesMissingAlt += 1;
      addFinding('imagesMissingAlt', file, $(element).attr('src') || '<missing src>');
    }
  });

  $('button').each((_, element) => {
    if (isHiddenControl($, element)) return;
    totals.buttons += 1;
    if (!hasAccessibleName($, element)) {
      totals.buttonsUnnamed += 1;
      addFinding('buttonsUnnamed', file, $.html(element).slice(0, 180));
    }
  });

  $('a').each((_, element) => {
    if (isHiddenControl($, element)) return;
    totals.links += 1;
    if (!hasAccessibleName($, element)) {
      totals.linksUnnamed += 1;
      addFinding('linksUnnamed', file, $(element).attr('href') || $.html(element).slice(0, 180));
    }
  });

  $('input, select, textarea').each((_, element) => {
    if (isHiddenControl($, element)) return;
    totals.formControls += 1;
    if (!isLabelledControl($, element)) {
      totals.controlsUnlabelled += 1;
      addFinding('controlsUnlabelled', file, $(element).attr('name') || element.tagName);
    }
  });

  $('iframe').each((_, element) => {
    totals.iframes += 1;
    if (!$(element).attr('title') && !$(element).attr('aria-label')) {
      totals.iframesMissingTitle += 1;
      addFinding('iframesMissingTitle', file, $(element).attr('src') || '<missing src>');
    }
  });
}

function walk(directory) {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (SKIP_DIRS.has(entry.name)) continue;
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      walk(file);
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.html')) {
      totals.files += 1;
      inspectFile(file);
    }
  }
}

walk(ROOT);

const filesWithFindings = [...perFile.entries()]
  .map(([file, findings]) => ({
    file,
    total: Object.values(findings).reduce((sum, count) => sum + count, 0),
    findings,
  }))
  .sort((a, b) => b.total - a.total || a.file.localeCompare(b.file))
  .slice(0, 25);

console.log(JSON.stringify({ totals, filesWithFindings, samples }, null, 2));
