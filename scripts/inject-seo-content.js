// inject-seo-content.js
//
// Injects <noscript> SEO content into HTML pages that rely on
// JavaScript to render their core content from JSON files.
//
// Two page types handled:
//   1. Maths chapter pages (class-X-maths/chapter-N-*.html)
//   2. AHC RO ARO and UPSC topic pages
//
// Usage: node scripts/inject-seo-content.js [--dry-run]

const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const DRY_RUN = process.argv.includes('--dry-run');

// Marker comments for idempotent injection
const SEO_START = '<!-- SEO_NOSCRIPT_START -->';
const SEO_END = '<!-- SEO_NOSCRIPT_END -->';

const stats = {
  chapterPages: 0,
  chapterInjected: 0,
  topicPages: 0,
  topicInjected: 0,
  skipped: 0,
  errors: 0,
};

// ─── Utility Functions ──────────────────────────────────────────

function stripHtml(html) {
  return html
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/gi, ' ')
    .replace(/&amp;/gi, '&')
    .replace(/&lt;/gi, '<')
    .replace(/&gt;/gi, '>')
    .replace(/&quot;/gi, '"')
    .replace(/&#39;/gi, "'")
    .replace(/\s+/g, ' ')
    .trim();
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function stripOldSeoContent(html) {
  const startIdx = html.indexOf(SEO_START);
  const endIdx = html.indexOf(SEO_END);
  if (startIdx === -1 || endIdx === -1) return html;
  return html.slice(0, startIdx) + html.slice(endIdx + SEO_END.length);
}

function readJsonSafe(filePath) {
  try {
    return JSON.parse(fs.readFileSync(filePath, 'utf8'));
  } catch {
    return null;
  }
}

// ─── Maths Chapter Pages ────────────────────────────────────────

function buildChapterSeoHtml(data) {
  const parts = [];

  parts.push(`<div style="padding:20px;max-width:960px;margin:0 auto;font-family:sans-serif;line-height:1.7">`);
  parts.push(`<h2>${escapeHtml(data.chapterTitle || 'Study Notes')}</h2>`);

  if (data.concepts && Array.isArray(data.concepts)) {
    for (const concept of data.concepts) {
      parts.push(`<h3>${escapeHtml(concept.title || '')}</h3>`);

      // Learning paragraphs
      if (concept.learn && concept.learn.paragraphs) {
        for (const p of concept.learn.paragraphs) {
          const text = stripHtml(p.replace(/\*\*/g, ''));
          parts.push(`<p>${escapeHtml(text)}</p>`);
        }
      }

      // Formulas
      if (concept.learn && concept.learn.formulas) {
        for (const f of concept.learn.formulas) {
          parts.push(`<p><strong>${escapeHtml(f.rule || '')}:</strong> ${escapeHtml(f.formula || '')}${f.example ? ' — ' + escapeHtml(f.example) : ''}</p>`);
        }
      }

      // Info boxes
      if (concept.learn && concept.learn.boxes) {
        for (const box of concept.learn.boxes) {
          const text = stripHtml(box.html || '');
          if (text) {
            parts.push(`<p><em>${escapeHtml(text)}</em></p>`);
          }
        }
      }

      // First 3 practice questions as sample
      if (concept.practice && concept.practice.length > 0) {
        parts.push(`<h4>Sample Practice Questions</h4><ol>`);
        const sampleQs = concept.practice.slice(0, 3);
        for (const q of sampleQs) {
          parts.push(`<li>${escapeHtml(stripHtml(q.question))} — Answer: ${escapeHtml(q.options?.[q.correctIndex] || '')}${q.solution ? '. ' + escapeHtml(stripHtml(q.solution)) : ''}</li>`);
        }
        parts.push(`</ol>`);
      }

      // First 2 PYQs
      if (concept.pyq && concept.pyq.length > 0) {
        parts.push(`<h4>Previous Year Questions</h4><ol>`);
        const samplePyq = concept.pyq.slice(0, 2);
        for (const q of samplePyq) {
          parts.push(`<li>${escapeHtml(stripHtml(q.question))}</li>`);
        }
        parts.push(`</ol>`);
      }
    }
  }

  parts.push(`</div>`);
  return parts.join('\n');
}

function processChapterPages() {
  const classPattern = /^class-(?:9|10|11|12)-maths$/;
  const dirs = fs.readdirSync(ROOT_DIR).filter(d => {
    return classPattern.test(d) && fs.statSync(path.join(ROOT_DIR, d)).isDirectory();
  });

  for (const classDir of dirs) {
    const classPath = path.join(ROOT_DIR, classDir);
    const files = fs.readdirSync(classPath);

    for (const file of files) {
      if (!/^chapter-\d+-.*\.html$/.test(file)) continue;

      const htmlPath = path.join(classPath, file);
      const chapterNum = file.match(/chapter-(\d+)/)?.[1];
      if (!chapterNum) continue;

      const jsonPath = path.join(classPath, `chapter-${chapterNum}-data.json`);
      stats.chapterPages++;

      if (!fs.existsSync(jsonPath)) {
        stats.skipped++;
        continue;
      }

      const data = readJsonSafe(jsonPath);
      if (!data) {
        stats.errors++;
        continue;
      }

      let html = fs.readFileSync(htmlPath, 'utf8');
      html = stripOldSeoContent(html);

      const seoHtml = buildChapterSeoHtml(data);
      const noscriptBlock = `${SEO_START}\n<noscript>\n${seoHtml}\n</noscript>\n${SEO_END}`;

      // Insert before closing </div> of cl-wizard
      const wizardTarget = '<div class="cl-wizard" id="cl-wizard">';
      const wizardIdx = html.indexOf(wizardTarget);
      if (wizardIdx === -1) {
        // Try inserting before </body>
        const bodyIdx = html.indexOf('</body>');
        if (bodyIdx === -1) {
          stats.errors++;
          continue;
        }
        html = html.slice(0, bodyIdx) + '\n' + noscriptBlock + '\n' + html.slice(bodyIdx);
      } else {
        // Find the closing </div> for cl-wizard
        const afterWizard = html.indexOf('</div>', wizardIdx + wizardTarget.length);
        if (afterWizard === -1) {
          stats.errors++;
          continue;
        }
        // Insert the noscript content inside the wizard div, before its closing tag
        const loadingEnd = html.indexOf('</div>', wizardIdx + wizardTarget.length);
        html = html.slice(0, afterWizard) + '\n' + noscriptBlock + '\n' + html.slice(afterWizard);
      }

      if (!DRY_RUN) {
        fs.writeFileSync(htmlPath, html, 'utf8');
      }
      stats.chapterInjected++;
      console.log(`✅ Chapter: ${classDir}/${file}`);
    }
  }
}

// ─── AHC RO ARO / UPSC Topic Pages ─────────────────────────────

function buildTopicSeoHtml(data) {
  const parts = [];
  parts.push(`<div style="padding:20px;max-width:960px;margin:0 auto;font-family:sans-serif;line-height:1.7">`);

  // Hero
  if (data.hero) {
    parts.push(`<h2>${escapeHtml(data.hero.title || '')}</h2>`);
    if (data.hero.description) {
      parts.push(`<p>${escapeHtml(data.hero.description)}</p>`);
    }
  }

  // Deep Dive sections (the richest content)
  if (data.deepDive && data.deepDive.sections) {
    for (const section of data.deepDive.sections) {
      parts.push(`<h3>${escapeHtml(section.title || '')}</h3>`);
      if (section.content) {
        // The content field already contains HTML — strip SVGs and scripts but keep text/tables
        const cleanContent = section.content
          .replace(/<svg[\s\S]*?<\/svg>/gi, '')
          .replace(/<script[\s\S]*?<\/script>/gi, '')
          .replace(/<style[\s\S]*?<\/style>/gi, '');
        parts.push(cleanContent);
      }
    }
  }

  // Timeline
  if (data.timeline && data.timeline.cards && data.timeline.cards.length > 0) {
    parts.push(`<h3>${escapeHtml(data.timeline.title || 'Timeline')}</h3>`);
    parts.push(`<ol>`);
    for (const card of data.timeline.cards) {
      parts.push(`<li><strong>${escapeHtml(card.date || '')} — ${escapeHtml(card.period || '')}</strong>: ${escapeHtml(card.details || '')}</li>`);
    }
    parts.push(`</ol>`);
  }

  // Flashcards as Q&A
  if (data.flashcards && data.flashcards.items && data.flashcards.items.length > 0) {
    parts.push(`<h3>Key Questions &amp; Answers</h3>`);
    parts.push(`<dl>`);
    for (const fc of data.flashcards.items) {
      parts.push(`<dt><strong>${escapeHtml(stripHtml(fc.question || ''))}</strong></dt>`);
      parts.push(`<dd>${escapeHtml(stripHtml(fc.answer || ''))}</dd>`);
    }
    parts.push(`</dl>`);
  }

  // Mnemonics
  if (data.mnemonics && data.mnemonics.items && data.mnemonics.items.length > 0) {
    parts.push(`<h3>Memory Aids</h3>`);
    parts.push(`<ul>`);
    for (const m of data.mnemonics.items) {
      parts.push(`<li><strong>${escapeHtml(m.title || '')}</strong>: ${escapeHtml(stripHtml(m.decryption || ''))}</li>`);
    }
    parts.push(`</ul>`);
  }

  // Traps
  if (data.traps && data.traps.items && data.traps.items.length > 0) {
    parts.push(`<h3>Common Exam Traps</h3>`);
    parts.push(`<ul>`);
    for (const trap of data.traps.items) {
      parts.push(`<li>${escapeHtml(stripHtml(trap))}</li>`);
    }
    parts.push(`</ul>`);
  }

  parts.push(`</div>`);
  return parts.join('\n');
}

function processTopicPages(baseDir) {
  if (!fs.existsSync(baseDir)) return;

  // Walk all index.html files in subdirectories (not the root index)
  function walkDirs(dir, depth = 0) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });

    for (const entry of entries) {
      if (entry.isDirectory()) {
        // Skip 'hi' (Hindi version) directories for now
        if (entry.name === 'hi' || entry.name === 'node_modules' || entry.name.startsWith('.')) continue;
        walkDirs(path.join(dir, entry.name), depth + 1);
      }
    }

    // Only process topic pages (depth >= 2 means we're inside subject/topic/)
    if (depth < 2) return;

    const indexPath = path.join(dir, 'index.html');
    if (!fs.existsSync(indexPath)) return;

    stats.topicPages++;

    // Try theory.json first (richer), then content.json
    const theoryPath = path.join(dir, 'theory.json');
    const contentPath = path.join(dir, 'content.json');

    let data = null;
    if (fs.existsSync(theoryPath)) {
      data = readJsonSafe(theoryPath);
    } else if (fs.existsSync(contentPath)) {
      data = readJsonSafe(contentPath);
    }

    if (!data) {
      stats.skipped++;
      return;
    }

    // Check if there's meaningful content to inject
    const hasDeepDive = data.deepDive?.sections?.length > 0;
    const hasTimeline = data.timeline?.cards?.length > 0;
    const hasFlashcards = data.flashcards?.items?.length > 0;
    if (!hasDeepDive && !hasTimeline && !hasFlashcards) {
      stats.skipped++;
      return;
    }

    let html = fs.readFileSync(indexPath, 'utf8');
    html = stripOldSeoContent(html);

    const seoHtml = buildTopicSeoHtml(data);
    const noscriptBlock = `${SEO_START}\n<noscript>\n${seoHtml}\n</noscript>\n${SEO_END}`;

    // Insert inside #notes-panel, before the tab navigation button
    const notesPanel = 'id="notes-panel"';
    const notesPanelIdx = html.indexOf(notesPanel);

    if (notesPanelIdx !== -1) {
      // Find the closing </div> of notes-panel
      // Strategy: insert before the "Next: Practice Zone" button div
      const nextBtnText = "Next: Practice Zone";
      const nextBtnIdx = html.indexOf(nextBtnText, notesPanelIdx);
      if (nextBtnIdx !== -1) {
        // Go back to find the <div that contains this button
        const divStart = html.lastIndexOf('<div', nextBtnIdx);
        if (divStart > notesPanelIdx) {
          html = html.slice(0, divStart) + noscriptBlock + '\n' + html.slice(divStart);
        } else {
          // Fallback: insert before </body>
          const bodyIdx = html.indexOf('</body>');
          html = html.slice(0, bodyIdx) + '\n' + noscriptBlock + '\n' + html.slice(bodyIdx);
        }
      } else {
        // Fallback: insert before </body>
        const bodyIdx = html.indexOf('</body>');
        html = html.slice(0, bodyIdx) + '\n' + noscriptBlock + '\n' + html.slice(bodyIdx);
      }
    } else {
      // Fallback: insert before </body>
      const bodyIdx = html.indexOf('</body>');
      if (bodyIdx === -1) {
        stats.errors++;
        return;
      }
      html = html.slice(0, bodyIdx) + '\n' + noscriptBlock + '\n' + html.slice(bodyIdx);
    }

    if (!DRY_RUN) {
      fs.writeFileSync(indexPath, html, 'utf8');
    }
    stats.topicInjected++;
    const relPath = path.relative(ROOT_DIR, indexPath).replace(/\\/g, '/');
    console.log(`✅ Topic: ${relPath}`);
  }

  walkDirs(baseDir);
}

// ─── Main ───────────────────────────────────────────────────────

function main() {
  console.log(`${DRY_RUN ? '[dry-run] ' : ''}Injecting SEO noscript content...\n`);

  // 1. Maths chapter pages
  console.log('=== Maths Chapter Pages ===');
  processChapterPages();

  // 2. AHC RO ARO topic pages
  console.log('\n=== AHC RO ARO Topic Pages ===');
  processTopicPages(path.join(ROOT_DIR, 'ahc-ro-aro'));

  // 3. UPSC topic pages
  console.log('\n=== UPSC Topic Pages ===');
  processTopicPages(path.join(ROOT_DIR, 'upsc'));

  // Summary
  console.log('\n─── Summary ───');
  console.table({
    'Chapter pages found': stats.chapterPages,
    'Chapter pages injected': stats.chapterInjected,
    'Topic pages found': stats.topicPages,
    'Topic pages injected': stats.topicInjected,
    'Skipped (no JSON/no content)': stats.skipped,
    'Errors': stats.errors,
  });
}

main();
