import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const API_KEYS = [
  process.env.GEMINI_API_KEY_1,
  process.env.GEMINI_API_KEY_2,
  process.env.GEMINI_API_KEY
].filter(Boolean);

let keyIdx = 0;
function getAI() {
  const key = API_KEYS[keyIdx % API_KEYS.length];
  const name = `KEY_${(keyIdx % API_KEYS.length) + 1}`;
  keyIdx++;
  return { client: new GoogleGenAI({ apiKey: key }), name };
}

function cleanOption(str) {
  return String(str || '')
    .replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '')
    .trim();
}

function extractTopicData(filePath) {
  const html = fs.readFileSync(filePath, 'utf8');

  // Breadcrumbs & Navigation
  const prevMatch = html.match(/<a href="([^"]+)" class="topic-nav-btn prev-btn">([\s\S]*?)<\/a>/);
  const nextMatch = html.match(/<a href="([^"]+)" class="topic-nav-btn next-btn">([\s\S]*?)<\/a>/);
  const prevNav = prevMatch ? { href: prevMatch[1], html: prevMatch[2].trim() } : null;
  const nextNav = nextMatch ? { href: nextMatch[1], html: nextMatch[2].trim() } : null;

  // Metadata pills
  const badgeMatch = html.match(/<span class="topic-badge-pill">([\s\S]*?)<\/span>/);
  const tagMatches = [...html.matchAll(/<span class="subject-tag-pill">([\s\S]*?)<\/span>/g)].map(m => m[1].trim());

  // Titles
  const h1Match = html.match(/<h1>([\s\S]*?)<\/h1>/);
  const h1Raw = h1Match ? h1Match[1].replace(/<[^>]+>/g, '').trim() : '';

  const subtitleMatch = html.match(/<div class="topic-hero-subtitle">([\s\S]*?)<\/div>/);
  const subtitleRaw = subtitleMatch ? subtitleMatch[1].replace(/<[^>]+>/g, '').trim() : '';

  const leadMatch = html.match(/<p class="lead-desc">([\s\S]*?)<\/p>/);
  const leadDesc = leadMatch ? leadMatch[1].replace(/<[^>]+>/g, '').trim() : '';

  const focusMatch = html.match(/<strong>Syllabus Focus &amp; High-Yield Strategy:<\/strong>([\s\S]*?)<\/p>/);
  const syllabusFocus = focusMatch ? focusMatch[1].replace(/<[^>]+>/g, '').trim() : '';

  // Concepts using accurate boundary extraction
  const concepts = [];
  const startMarker = '<div class="topic-content-body">';
  const cardStartRegex = /<div class="prep-card">\s*<h2>\s*<i class="fas fa-bookmark"[^>]*><\/i>\s*<span>([^<]+)<\/span>\s*<\/h2>/g;

  let match;
  const matches = [];
  while ((match = cardStartRegex.exec(html)) !== null) {
    matches.push({
      heading: match[1].trim(),
      startIdx: match.index + match[0].length
    });
  }

  for (let i = 0; i < matches.length; i++) {
    const current = matches[i];
    const bodyStart = html.indexOf(startMarker, current.startIdx);
    if (bodyStart === -1) continue;
    const contentStart = bodyStart + startMarker.length;

    let contentEnd;
    if (i < matches.length - 1) {
      const idxNextCard = html.lastIndexOf('<div class="prep-card">', matches[i + 1].startIdx);
      contentEnd = idxNextCard !== -1 ? idxNextCard : contentStart;
    } else {
      const idxTable = html.indexOf('<i class="fas fa-table-columns"', contentStart);
      if (idxTable !== -1) {
        contentEnd = html.lastIndexOf('<div class="prep-card">', idxTable);
      } else {
        contentEnd = html.indexOf('</div>\n    </div>\n\n    <!-- ===', contentStart);
      }
    }

    let rawBody = html.slice(contentStart, contentEnd).trim();
    rawBody = rawBody.replace(/<\/div>\s*<\/div>\s*$/, '').trim();

    concepts.push({
      heading: current.heading,
      html_content: rawBody
    });
  }

  // Comparative Table
  let comparativeTable = null;
  const tableTitleMatch = html.match(/<i class="fas fa-table-columns"[^>]*><\/i>\s*<span>([^<]+)<\/span>/);
  const tableMatch = html.match(/<table class="prep-table">([\s\S]*?)<\/table>/);
  if (tableTitleMatch && tableMatch) {
    const tableHtml = tableMatch[1];
    const ths = [...tableHtml.matchAll(/<th>([\s\S]*?)<\/th>/g)].map(m => m[1].replace(/<[^>]+>/g, '').trim());
    const rows = [];
    const trRegex = /<tr>([\s\S]*?)<\/tr>/g;
    let trMatch;
    while ((trMatch = trRegex.exec(tableHtml)) !== null) {
      if (trMatch[1].includes('<th')) continue;
      const tds = [...trMatch[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(m => m[1].trim());
      if (tds.length) rows.push(tds);
    }
    comparativeTable = {
      title: tableTitleMatch[1].trim(),
      headers: ths,
      rows: rows
    };
  }

  // MCQs
  let testData = [];
  const testDataMatch = html.match(/const testData\s*=\s*(\[[\s\S]*?\]);\s*<\/script>/);
  if (testDataMatch) {
    try {
      testData = JSON.parse(testDataMatch[1]);
    } catch (e) {
      console.warn('Failed to parse testData JSON:', e.message);
    }
  }

  // Storage keys
  const storageKeyMatch = html.match(/const TOPIC_STORAGE_KEY\s*=\s*'([^']+)';/);
  const chkIdMatch = html.match(/const TOPIC_CHECKBOX_ID\s*=\s*'([^']+)';/);
  const storageKey = storageKeyMatch ? storageKeyMatch[1] : 'up-upper-primary-teacher-checklist-v2';
  const chkId = chkIdMatch ? chkIdMatch[1] : '';

  // Revision facts
  const facts = [];
  const factRegex = /<div class="revision-fact-row">\s*<span class="fact-num-badge">[^<]+<\/span>\s*<div class="fact-text-col">([\s\S]*?)<\/div>\s*<\/div>/g;
  let fMatch;
  while ((fMatch = factRegex.exec(html)) !== null) {
    facts.push(fMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  // Mnemonics
  const mnemonics = [];
  const mnemRegex = /<div class="mnemonic-card">[\s\S]*?<h3[^>]*>[\s\S]*?<i class="fas fa-lightbulb"><\/i>\s*([\s\S]*?)<\/h3>[\s\S]*?<code>([\s\S]*?)<\/code>[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>/g;
  let mMatch;
  while ((mMatch = mnemRegex.exec(html)) !== null) {
    mnemonics.push({
      title: mMatch[1].replace(/<[^>]+>/g, '').trim(),
      acronym: mMatch[2].trim(),
      expansion: mMatch[3].trim()
    });
  }

  // Traps
  const traps = [];
  const trapRegex = /<div class="trap-card-item">[\s\S]*?<p[^>]*>([\s\S]*?)<\/p>\s*<\/div>\s*<\/div>/g;
  let tMatch;
  while ((tMatch = trapRegex.exec(html)) !== null) {
    traps.push(tMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  // Checklist
  const checklist = [];
  const chkRegex = /<label class="mastery-check-item">[\s\S]*?<span>([\s\S]*?)<\/span>\s*<\/label>/g;
  let chkMatch;
  while ((chkMatch = chkRegex.exec(html)) !== null) {
    checklist.push(chkMatch[1].replace(/<[^>]+>/g, '').trim());
  }

  return {
    badge: badgeMatch ? badgeMatch[1].trim() : '#1 Compulsory',
    tags: tagMatches,
    titleEn: h1Raw,
    titleHi: subtitleRaw,
    leadDesc,
    syllabusFocus,
    concepts,
    comparativeTable,
    testData,
    facts,
    mnemonics,
    traps,
    checklist,
    prevNav,
    nextNav,
    storageKey,
    chkId
  };
}

async function callGemini(prompt, taskName = 'translate') {
  for (let attempt = 1; attempt <= 4; attempt++) {
    const { client, name } = getAI();
    try {
      const response = await client.models.generateContent({
        model: 'gemini-3.1-flash-lite',
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.1,
        }
      });
      let raw = response.text?.trim() || '';
      if (raw.startsWith('```')) {
        raw = raw.replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
      }
      try {
        return JSON.parse(raw);
      } catch {
        return JSON.parse(jsonrepair(raw));
      }
    } catch (e) {
      console.warn(`  [${taskName} Attempt ${attempt}/4] Error on ${name}: ${e.message?.slice(0, 100)}`);
      await new Promise(r => setTimeout(r, attempt * 1500));
    }
  }
  throw new Error(`${taskName} failed after 4 attempts`);
}

async function translateTopic(dataEn, topicNameEn, topicNameHi) {
  const promptPart1 = `You are a Senior Bilingual Academic Translation Expert for SCERT Uttar Pradesh.
Translate the following theoretical study notes from English into standard academic Hindi (Devanagari, using authentic terminology from SCERT UP "Hamara Itihas" and NCERT Hindi books).
Preserve all HTML tags (<strong>, <code>, <div class="...">, <table>, <thead>, <tbody>, <tr>, <th>, <td>, <i>) exactly intact, translating only the human-readable text.

TOPIC: ${topicNameEn} (${topicNameHi})

INPUT JSON:
${JSON.stringify({
  lead_desc: dataEn.leadDesc,
  syllabus_focus: dataEn.syllabusFocus,
  concepts: dataEn.concepts,
  comparative_table: dataEn.comparativeTable
}, null, 2)}

OUTPUT FORMAT (RAW JSON ONLY):
{
  "lead_desc": "...",
  "syllabus_focus": "...",
  "concepts": [
    { "heading": "...", "html_content": "..." }
  ],
  "comparative_table": {
    "title": "...",
    "headers": ["...", "..."],
    "rows": [["...", "..."]]
  }
}`;

  const promptPart2 = `You are a Senior Bilingual Academic Translation Expert for SCERT Uttar Pradesh.
Translate the following 10 practice MCQs, rapid recall facts, mnemonics, exam traps, and mastery checklist into standard academic Hindi.
1. For MCQs, keep the exact same correct_index (0-based) and ensure options correspond accurately.
2. For mnemonics, translate the title, keep the acronym, and translate the expansion/explanation.
3. Preserve any HTML tags intact.

INPUT JSON:
${JSON.stringify({
  mcqs: dataEn.testData,
  facts: dataEn.facts,
  mnemonics: dataEn.mnemonics,
  traps: dataEn.traps,
  checklist: dataEn.checklist
}, null, 2)}

OUTPUT FORMAT (RAW JSON ONLY):
{
  "mcqs": [
    { "question": "...", "options": ["...", "...", "...", "..."], "correct_index": 0, "explanation": "..." }
  ],
  "facts": ["...", "..."],
  "mnemonics": [
    { "title": "...", "acronym": "...", "expansion": "..." }
  ],
  "traps": ["...", "..."],
  "checklist": ["...", "..."]
}`;

  const [res1, res2] = await Promise.all([
    callGemini(promptPart1, 'Part1-Theory'),
    callGemini(promptPart2, 'Part2-MCQs')
  ]);

  return {
    leadDesc: res1.lead_desc || dataEn.leadDesc,
    syllabusFocus: res1.syllabus_focus || dataEn.syllabusFocus,
    concepts: res1.concepts || dataEn.concepts,
    comparativeTable: res1.comparative_table || dataEn.comparativeTable,
    mcqs: res2.mcqs || dataEn.testData,
    facts: res2.facts || dataEn.facts,
    mnemonics: res2.mnemonics || dataEn.mnemonics,
    traps: res2.traps || dataEn.traps,
    checklist: res2.checklist || dataEn.checklist
  };
}

function renderBilingualPage(meta, dataEn, dataHi) {
  const mergedTestData = (dataEn.testData || []).map((qEn, idx) => {
    const qHi = dataHi.mcqs?.[idx] || {};
    return {
      question: qEn.question,
      question_hi: qHi.question || qEn.question,
      options: (qEn.options || []).map(cleanOption),
      options_hi: (qHi.options || qEn.options || []).map(cleanOption),
      correct_index: qEn.correct_index,
      explanation: qEn.explanation,
      explanation_hi: qHi.explanation || qEn.explanation
    };
  });

  return `<!DOCTYPE html>
<html lang="en">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${meta.topicNameEn} | ${meta.topicNameHi} | UP Teacher ${meta.hubName} | SJMaths</title>
<meta content="${meta.topicNameEn}, ${meta.topicNameHi}, ${meta.hubName} UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="Bilingual (English & Hindi) pointwise study notes, comparative analysis, 10 practice MCQs, timed mini test, and revision traps for ${meta.topicNameEn} (${meta.topicNameHi}) for UP Upper Primary Assistant Teacher Exam 2026." name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="https://sjmaths.com${meta.canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${meta.topicNameEn} | ${meta.topicNameHi} | UP Teacher ${meta.hubName} | SJMaths"/>
<meta content="Bilingual (English & Hindi) pointwise study notes, 10 MCQs, timed mini test, and revision traps for ${meta.topicNameEn} (${meta.topicNameHi}) for UP Upper Primary Assistant Teacher Exam 2026." property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="https://sjmaths.com${meta.canonicalUrl}" property="og:url"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="${meta.topicNameEn} | ${meta.topicNameHi} | UP Teacher ${meta.hubName} | SJMaths"/>
<meta content="Bilingual (English & Hindi) pointwise study notes, 10 MCQs, timed mini test, and revision traps for ${meta.topicNameEn} (${meta.topicNameHi}) for UP Upper Primary Assistant Teacher Exam 2026." name="twitter:description"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" name="twitter:image"/>

<!-- Fonts and Icons -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets -->
<link href="/assets/css/main.min.css?v=a3faaea0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=3fce8e36" rel="stylesheet"/>
<link href="/assets/css/improved-ui.min.css?v=dd2cffe9" rel="stylesheet"/>
<link href="/assets/css/pages.min.css?v=9e3bd560" rel="stylesheet"/>
<link href="/assets/css/up-upper-primary-topic.min.css" rel="stylesheet"/>

<!-- Breadcrumb Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://sjmaths.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "UP Upper Primary Teacher",
      "item": "https://sjmaths.com/up-upper-primary-teacher/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "${meta.hubName}",
      "item": "https://sjmaths.com${meta.hubHref}"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "${meta.topicNameEn}",
      "item": "https://sjmaths.com${meta.canonicalUrl}"
    }
  ]
}
</script>
</head>

<body>
<div id="header-container"></div>

<main class="topic-page-container">

    <!-- Top Action Bar with Persistent Language Toggle -->
    <div class="top-action-bar">
        <div class="breadcrumb-trail">
            <a href="/"><i class="fas fa-home"></i> Home</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/">UP Upper Primary</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="${meta.hubHref}">${meta.hubName}</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${meta.topicNumStr}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
            <button class="lang-toggle-btn" id="langToggleBtn" onclick="toggleLanguageMode()" title="Switch Language / भाषा बदलें">
                <i class="fas fa-language"></i>
                <span class="lang-en">हिंदी में देखें</span>
                <span class="lang-hi">Switch to English</span>
            </button>
            <a href="${meta.hubHref}" class="back-hub-btn">
                <i class="fas fa-arrow-left"></i>
                <span class="lang-en">Back to Hub</span>
                <span class="lang-hi">हब पर वापस जाएं</span>
            </a>
        </div>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row">
            <span class="topic-badge-pill">${meta.topicBadge}</span>
            ${(meta.tags || []).map(t => `<span class="subject-tag-pill">${t}</span>`).join('')}
        </div>
        <h1>
            <span class="lang-en">${meta.topicNameEn}</span>
            <span class="lang-hi">${meta.topicNameHi}</span>
        </h1>
        <div class="topic-hero-subtitle">
            <span class="lang-en">${meta.topicNameHi}</span>
            <span class="lang-hi">${meta.topicNameEn}</span>
        </div>
        <p class="lead-desc">
            <span class="lang-en">${dataEn.leadDesc}</span>
            <span class="lang-hi">${dataHi.leadDesc}</span>
        </p>
    </div>

    <!-- Live Completion Toggle -->
    <div class="completion-card">
        <div class="completion-card-left">
            <i class="fas fa-tasks" style="font-size: 1.5rem; color: var(--brand-emerald);"></i>
            <div>
                <strong style="font-size: 1rem; color: var(--text-headline);">
                    <span class="lang-en">Preparation Status</span>
                    <span class="lang-hi">तैयारी की स्थिति</span>
                </strong>
                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: var(--text-muted);" id="statusDesc">
                    <span class="lang-en">Mark complete once covered. Progress syncs automatically with the main syllabus hub.</span>
                    <span class="lang-hi">अध्ययन पूरा होने पर पूर्ण चिह्नित करें। प्रगति मुख्य पाठ्यक्रम हब के साथ स्वतः सिंक होती है।</span>
                </p>
            </div>
        </div>
        <button id="topicCompletionBtn" class="toggle-topic-btn" onclick="toggleTopicStatus()">
            <i class="fas fa-check-circle"></i>
            <span id="completionBtnText">
                <span class="lang-en">Mark as Completed</span>
                <span class="lang-hi">पूर्ण चिह्नित करें</span>
            </span>
        </button>
    </div>

    <!-- Study Tabs Strip -->
    <div class="study-tabs-strip" role="tablist">
        <button class="study-tab-btn active" data-tab="concepts">
            <i class="fas fa-book-open"></i>
            <span>
                <span class="lang-en">1. Concepts &amp; Theory</span>
                <span class="lang-hi">1. अवधारणाएं एवं सिद्धांत</span>
            </span>
        </button>
        <button class="study-tab-btn" data-tab="practice">
            <i class="fas fa-list-check"></i>
            <span>
                <span class="lang-en">2. Practice Questions (10 MCQs)</span>
                <span class="lang-hi">2. अभ्यास प्रश्न (10 MCQs)</span>
            </span>
        </button>
        <button class="study-tab-btn" data-tab="test">
            <i class="fas fa-stopwatch"></i>
            <span>
                <span class="lang-en">3. Mini Test</span>
                <span class="lang-hi">3. मिनी टेस्ट</span>
            </span>
        </button>
        <button class="study-tab-btn" data-tab="revision">
            <i class="fas fa-redo"></i>
            <span>
                <span class="lang-en">4. Quick Revision &amp; Traps</span>
                <span class="lang-hi">4. त्वरित पुनरीक्षण एवं जाल</span>
            </span>
        </button>
    </div>

    <!-- ==================== TAB 1: CONCEPTS & THEORY ==================== -->
    <div class="study-tab-pane active" id="tab-concepts">
        <div style="background: var(--brand-emerald-subtle); border-left: 4px solid var(--brand-emerald); padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1.5rem;">
            <p style="margin: 0; font-size: 0.95rem; color: var(--text-headline); line-height: 1.6;">
                <i class="fas fa-compass" style="color: var(--brand-emerald); margin-right: 0.4rem;"></i>
                <strong>
                    <span class="lang-en">Syllabus Focus &amp; High-Yield Strategy:</span>
                    <span class="lang-hi">पाठ्यक्रम फोकस एवं उच्च अंक रणनीति:</span>
                </strong>
                <span class="lang-en">${dataEn.syllabusFocus}</span>
                <span class="lang-hi">${dataHi.syllabusFocus}</span>
            </p>
        </div>
        
        ${(dataEn.concepts || []).map((cEn, idx) => {
          const cHi = dataHi.concepts?.[idx] || cEn;
          return `
        <div class="prep-card">
            <h2>
                <i class="fas fa-bookmark" style="color: var(--brand-emerald);"></i>
                <span class="lang-en">${cEn.heading}</span>
                <span class="lang-hi">${cHi.heading}</span>
            </h2>
            <div class="topic-content-body">
                <div class="lang-en">${cEn.html_content}</div>
                <div class="lang-hi">${cHi.html_content}</div>
            </div>
        </div>`;
        }).join('')}

        ${dataEn.comparativeTable ? `
        <div class="prep-card">
            <h2>
                <i class="fas fa-table-columns" style="color: var(--brand-emerald);"></i>
                <span class="lang-en">${dataEn.comparativeTable.title}</span>
                <span class="lang-hi">${dataHi.comparativeTable?.title || dataEn.comparativeTable.title}</span>
            </h2>
            <div class="table-scroll-wrapper lang-en">
                <table class="prep-table">
                    <thead>
                        <tr>${dataEn.comparativeTable.headers.map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                        ${dataEn.comparativeTable.rows.map(r => `<tr>${r.map(td => `<td>${td}</td>`).join('')}</tr>`).join('')}
                    </tbody>
                </table>
            </div>
            <div class="table-scroll-wrapper lang-hi">
                <table class="prep-table">
                    <thead>
                        <tr>${(dataHi.comparativeTable?.headers || dataEn.comparativeTable.headers).map(h => `<th>${h}</th>`).join('')}</tr>
                    </thead>
                    <tbody>
                        ${(dataHi.comparativeTable?.rows || dataEn.comparativeTable.rows).map(r => `<tr>${r.map(td => `<td>${td}</td>`).join('')}</tr>`).join('')}
                    </tbody>
                </table>
            </div>
        </div>` : ''}
    </div>

    <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
    <div class="study-tab-pane" id="tab-practice">
        <div class="practice-summary-bar">
            <div>
                <strong style="color: var(--text-headline);">
                    <span class="lang-en">Practice Progress:</span>
                    <span class="lang-hi">अभ्यास प्रगति:</span>
                </strong>
                <span id="practiceProgressText" style="color: var(--text-sub); margin-left: 0.5rem;">0 of 10 Answered</span>
            </div>
            <div class="practice-score-badge" id="practiceScoreBadge">Score: 0 / 10</div>
        </div>

        ${mergedTestData.map((q, idx) => `
        <div class="mcq-item-card" id="mcq-card-${idx}">
            <div class="mcq-header-meta">
                <span class="mcq-q-pill">Question ${idx + 1} of 10</span>
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior</span>
            </div>
            <div class="mcq-question-text">
                <p class="lang-en"><strong>${idx + 1}.</strong> ${q.question}</p>
                <p class="lang-hi"><strong>${idx + 1}.</strong> ${q.question_hi}</p>
            </div>
            <div class="mcq-options-group">
                ${[0, 1, 2, 3].map(optIdx => `
                <button type="button" class="mcq-option-btn" data-correct="${optIdx === q.correct_index}" onclick="handleMcqOptionClick(this, ${idx})">
                    <span class="opt-label">${['A', 'B', 'C', 'D'][optIdx]}</span>
                    <span class="lang-en">${q.options[optIdx]}</span>
                    <span class="lang-hi">${q.options_hi[optIdx]}</span>
                </button>
                `).join('')}
            </div>
            <div class="mcq-explanation-box" id="mcq-exp-${idx}">
                <div class="exp-badge"><i class="fas fa-circle-check"></i> Correct Answer: Option ${['A', 'B', 'C', 'D'][q.correct_index]}</div>
                <p class="lang-en" style="margin: 0; font-size: 0.93rem; line-height: 1.6;">${q.explanation}</p>
                <p class="lang-hi" style="margin: 0; font-size: 0.93rem; line-height: 1.6;">${q.explanation_hi}</p>
            </div>
        </div>`).join('')}
    </div>

    <!-- ==================== TAB 3: MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="prep-card">
            <!-- Screen 1: Intro Screen -->
            <div id="miniTestIntro" class="mini-test-intro">
                <i class="fas fa-stopwatch" style="font-size: 2.75rem; color: var(--brand-emerald); margin-bottom: 1rem;"></i>
                <h3 style="font-family: Outfit, sans-serif; font-size: 1.5rem; font-weight: 800; color: var(--text-headline); margin: 0 0 0.5rem;">
                    <span class="lang-en">5-Minute Exam Hall Mini Test</span>
                    <span class="lang-hi">5-मिनट परीक्षा हॉल मिनी टेस्ट</span>
                </h3>
                <p class="test-desc">
                    <span class="lang-en">Simulate real examination conditions under UP Super TET Junior rules. 10 Questions | 300 Seconds | -1 Negative Marking.</span>
                    <span class="lang-hi">यूपी सुपर टीईटी जूनियर नियमों के तहत वास्तविक परीक्षा माहौल का अनुभव करें। 10 प्रश्न | 300 सेकंड | -1 नकारात्मक अंकन।</span>
                </p>
                <div class="test-stats-row">
                    <span class="test-stat-chip"><i class="fas fa-circle-question"></i> 10 MCQs</span>
                    <span class="test-stat-chip"><i class="fas fa-clock"></i> 5 Minutes</span>
                    <span class="test-stat-chip"><i class="fas fa-award"></i> 30 Marks (+3, -1)</span>
                </div>
                <button type="button" class="start-test-btn" onclick="startMiniTest()">
                    <span class="lang-en">Start Timed Test Now</span>
                    <span class="lang-hi">समयबद्ध टेस्ट अभी शुरू करें</span>
                </button>
            </div>

            <!-- Screen 2: Active Test Screen -->
            <div id="miniTestActive" style="display: none;">
                <div class="test-timer-bar">
                    <div style="font-weight: 700; font-size: 0.95rem; color: var(--text-headline);">
                        <span class="lang-en">Question</span><span class="lang-hi">प्रश्न</span> <span id="testCurrentQ">1</span> of 10
                    </div>
                    <div class="test-countdown" id="timerDisplay">05:00</div>
                </div>
                <div id="testQuestionContainer"></div>
                <div class="test-nav-controls">
                    <button type="button" class="test-btn-nav" id="testPrevBtn" onclick="navTest(-1)" disabled>
                        <i class="fas fa-chevron-left"></i> <span class="lang-en">Previous</span><span class="lang-hi">पिछला</span>
                    </button>
                    <button type="button" class="test-btn-nav" id="testNextBtn" onclick="navTest(1)">
                        <span class="lang-en">Next</span><span class="lang-hi">अगला</span> <i class="fas fa-chevron-right"></i>
                    </button>
                    <button type="button" class="test-submit-btn" id="testSubmitBtn" onclick="submitMiniTest()" style="display: none;">
                        <span class="lang-en">Submit Test</span><span class="lang-hi">टेस्ट सबमिट करें</span>
                    </button>
                </div>
            </div>

            <!-- Screen 3: Test Result Screen -->
            <div id="miniTestResult" style="display: none; text-align: center; padding: 2rem 1rem;">
                <i class="fas fa-trophy" style="font-size: 3rem; color: #f59e0b; margin-bottom: 1rem;"></i>
                <h3 style="font-family: Outfit, sans-serif; font-size: 1.6rem; font-weight: 800; color: var(--text-headline); margin: 0 0 0.5rem;">
                    <span class="lang-en">Mini Test Summary</span>
                    <span class="lang-hi">मिनी टेस्ट परिणाम</span>
                </h3>
                <div id="testResultScore" style="font-size: 2.2rem; font-weight: 900; color: var(--brand-emerald); margin-bottom: 0.5rem;"></div>
                <p id="testResultFeedback" style="color: var(--text-sub); margin-bottom: 1.5rem;"></p>
                <button type="button" class="retry-test-btn" onclick="resetMiniTest()">
                    <span class="lang-en">Retake Mini Test</span>
                    <span class="lang-hi">पुनः टेस्ट दें</span>
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: QUICK REVISION & TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #f59e0b;"></i>
                <span class="lang-en">High-Yield Rapid Recall Facts</span>
                <span class="lang-hi">उच्च अंक त्वरित स्मरण तथ्य (Rapid Recall)</span>
            </h2>
            <div class="revision-facts-grid">
                ${(dataEn.facts || []).map((factEn, idx) => `
                <div class="revision-fact-row">
                    <span class="fact-num-badge">#${idx + 1}</span>
                    <div class="fact-text-col">
                        <span class="lang-en">${factEn}</span>
                        <span class="lang-hi">${dataHi.facts?.[idx] || factEn}</span>
                    </div>
                </div>`).join('')}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span class="lang-en">Memory Mnemonics &amp; Retention Anchors</span>
                <span class="lang-hi">स्मृति सूत्र एवं निमोनिक्स (Retention Anchors)</span>
            </h2>
            ${(dataEn.mnemonics || []).map((mEn, idx) => {
              const mHi = dataHi.mnemonics?.[idx] || mEn;
              return `
            <div class="mnemonic-card">
                <h3 style="font-size: 1.05rem; margin: 0 0 0.5rem 0; color: var(--brand-indigo);">
                    <i class="fas fa-lightbulb"></i>
                    <span class="lang-en">${mEn.title}</span>
                    <span class="lang-hi">${mHi.title}</span>
                </h3>
                <div class="mnemonic-quote-box">
                    <strong>Memory Key:</strong> <code>${mEn.acronym}</code>
                </div>
                <p style="margin: 0; font-size: 0.92rem; color: var(--text-sub);">
                    <span class="lang-en">${mEn.expansion}</span>
                    <span class="lang-hi">${mHi.expansion}</span>
                </p>
            </div>`;
            }).join('')}
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-triangle-exclamation" style="color: #dc2626;"></i>
                <span class="lang-en">Exam Traps &amp; Negative Marking Pitfalls</span>
                <span class="lang-hi">परीक्षा के जाल एवं नकारात्मक अंकन से बचाव</span>
            </h2>
            <div class="traps-container">
                ${(dataEn.traps || []).map((trapEn, idx) => `
                <div class="trap-card-item">
                    <i class="fas fa-triangle-exclamation" style="color: #dc2626; font-size: 1.15rem; margin-top: 2px;"></i>
                    <div>
                        <strong>
                            <span class="lang-en">Negative Marking Alert #${idx + 1}:</span>
                            <span class="lang-hi">नकारात्मक अंकन चेतावनी #${idx + 1}:</span>
                        </strong>
                        <p style="margin: 0.25rem 0 0 0;">
                            <span class="lang-en">${trapEn}</span>
                            <span class="lang-hi">${dataHi.traps?.[idx] || trapEn}</span>
                        </p>
                    </div>
                </div>`).join('')}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-circle-check" style="color: var(--brand-emerald);"></i>
                <span class="lang-en">Self-Assessment Checklist</span>
                <span class="lang-hi">स्व-मूल्यांकन चेकलिस्ट</span>
            </h2>
            <div class="topic-mastery-checklist">
                ${(dataEn.checklist || []).map((chkEn, idx) => `
                <label class="mastery-check-item">
                    <input type="checkbox" id="chk-mastery-${idx}" class="custom-check" onchange="updateMasteryProgress()">
                    <span class="lang-en">${chkEn}</span>
                    <span class="lang-hi">${dataHi.checklist?.[idx] || chkEn}</span>
                </label>`).join('')}
            </div>
        </div>
    </div>

    <!-- Bottom Sequential Navigation -->
    <div class="bottom-topic-nav">
        ${meta.prevNav ? `<a href="${meta.prevNav.href}" class="topic-nav-btn prev-btn">${meta.prevNav.html}</a>` : `<span class="topic-nav-btn disabled"><i class="fas fa-chevron-left"></i> First Topic</span>`}
        ${meta.nextNav ? `<a href="${meta.nextNav.href}" class="topic-nav-btn next-btn">${meta.nextNav.html}</a>` : `<span class="topic-nav-btn disabled">Final Topic <i class="fas fa-chevron-right"></i></span>`}
    </div>

</main>

<button aria-label="Back to Top" class="back-to-top-btn" id="backToTopBtn">
    <i class="fas fa-arrow-up"></i>
</button>

<!-- Interactive Logic -->
<script>
    const TOPIC_STORAGE_KEY = '${meta.storageKey}';
    const TOPIC_CHECKBOX_ID = '${meta.chkId}';
    const testData = ${JSON.stringify(mergedTestData)};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js"></script>
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=1594eda0"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=d48c181a"></script>
<script src="/assets/js/require-auth.min.js?v=3060658c" type="module"></script>
</body>
</html>`;
}

async function testRender() {
  const p = 'up-upper-primary-teacher/social-studies/indus-valley-civilisation/index.html';
  console.log('Testing translation and render on', p);
  const dataEn = extractTopicData(p);
  const t0 = Date.now();
  const dataHi = await translateTopic(dataEn, dataEn.titleEn, dataEn.titleHi);
  console.log(`Translation completed in ${((Date.now() - t0)/1000).toFixed(2)}s!`);

  const meta = {
    topicNameEn: dataEn.titleEn,
    topicNameHi: dataEn.titleHi,
    topicNumStr: '#3',
    topicBadge: dataEn.badge,
    tags: dataEn.tags,
    hubName: 'Social Studies',
    hubHref: '/up-upper-primary-teacher/social-studies/',
    canonicalUrl: '/up-upper-primary-teacher/social-studies/indus-valley-civilisation/',
    prevNav: dataEn.prevNav,
    nextNav: dataEn.nextNav,
    storageKey: dataEn.storageKey,
    chkId: dataEn.chkId
  };

  const html = renderBilingualPage(meta, dataEn, dataHi);
  fs.writeFileSync(p, html, 'utf8');
  console.log('Saved bilingual HTML to', p);
  console.log('File size:', fs.statSync(p).size, 'bytes');
}

testRender().catch(console.error);
