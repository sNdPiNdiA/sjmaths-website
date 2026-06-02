const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const ROOT_DIR = path.resolve(__dirname, '..');
const SSC_CGL_DIR = path.join(ROOT_DIR, 'ssc-cgl');

const SUBJECTS = [
  { slug: 'quantitative-aptitude', name: 'Quantitative Aptitude' },
  { slug: 'reasoning', name: 'Reasoning & Intelligence' },
  { slug: 'english', name: 'English Language' },
  { slug: 'general-awareness', name: 'General Awareness' },
  { slug: 'computer-knowledge', name: 'Computer Knowledge' },
  { slug: 'statistics', name: 'Statistics' },
  { slug: 'finance-economics', name: 'Finance & Economics' }
];

// Helper to normalize strings for mapping
function normalizeText(text) {
  return text.toLowerCase().replace(/[^a-z0-9]/g, '');
}

function processProgressBars() {
  const syllabusPath = path.join(SSC_CGL_DIR, 'syllabus', 'index.html');
  if (!fs.existsSync(syllabusPath)) {
    console.error('Syllabus file not found!');
    return;
  }

  const syllabusHtml = fs.readFileSync(syllabusPath, 'utf8');
  const $syllabus = cheerio.load(syllabusHtml);

  // Map normalized syllabus item texts to their checkbox IDs
  const syllabusItemsMap = {};
  $syllabus('.subject-card').each((_, card) => {
    const titleLink = $syllabus(card).find('.subject-title a').first();
    const href = titleLink.attr('href') || '';
    const match = href.match(/\/ssc-cgl\/([^/]+)\//);
    if (!match) return;
    const subjectSlug = match[1];

    if (!syllabusItemsMap[subjectSlug]) {
      syllabusItemsMap[subjectSlug] = {};
    }

    $syllabus(card).find('.syllabus-item').each((_, item) => {
      const checkboxId = $syllabus(item).find('.syllabus-checkbox').attr('id');
      const text = $syllabus(item).find('.syllabus-text').text().trim();
      if (checkboxId && text) {
        syllabusItemsMap[subjectSlug][normalizeText(text)] = checkboxId;
      }
    });
  });

  for (const subject of SUBJECTS) {
    const indexPath = path.join(SSC_CGL_DIR, subject.slug, 'index.html');
    if (!fs.existsSync(indexPath)) continue;

    let html = fs.readFileSync(indexPath, 'utf8');
    const $ = cheerio.load(html);

    // 1. Add style rules for the progress tracker if not present
    const styleTag = $('style').first();
    if (styleTag.length > 0) {
      let css = styleTag.html();
      if (!css.includes('.tracker-banner')) {
        css += `
        /* Progress Tracker Styles */
        .tracker-banner {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.5rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.5rem;
            flex-wrap: wrap;
        }
        .tracker-info h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 0.25rem;
        }
        .tracker-info p {
            font-size: 0.9rem;
            color: var(--text-light);
        }
        .tracker-progress-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-grow: 1;
            max-width: 500px;
            justify-content: flex-end;
        }
        .progress-bar-wrapper {
            background: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
            height: 10px;
            width: 100%;
            overflow: hidden;
            position: relative;
        }
        body.dark-mode .progress-bar-wrapper {
            background: rgba(255, 255, 255, 0.1);
        }
        .progress-bar-fill {
            background: var(--accent-gradient);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease-out;
            border-radius: 10px;
        }
        .progress-percentage {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            color: var(--primary);
            min-width: 50px;
            text-align: right;
        }
        .syllabus-checkbox {
            appearance: none;
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border: 2px solid var(--text-light);
            border-radius: 5px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
        }
        .syllabus-checkbox::before {
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.7rem;
            color: #ffffff;
            display: none;
        }
        .syllabus-checkbox:checked {
            background: var(--accent-gradient);
            border-color: transparent;
        }
        .syllabus-checkbox:checked::before {
            display: block;
        }
        .topic-item input[type="checkbox"]:checked + .topic-text {
            color: var(--muted, #9ca3af);
            text-decoration: line-through;
        }
        `;
        styleTag.html(css);
      }
    }

    // 2. Add the progress bar markup
    if ($('.tracker-banner').length === 0) {
      const progressBarHtml = `
        <!-- Progress Tracker Banner -->
        <div class="tracker-banner">
            <div class="tracker-info">
                <h2>${subject.name} Progress</h2>
                <p>Track your completed topics. Progress is saved automatically.</p>
            </div>
            <div class="tracker-progress-container">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar-fill" id="subjectProgressBar"></div>
                </div>
                <div class="progress-percentage" id="subjectProgressPercent">0%</div>
            </div>
        </div>
      `;
      $('.subject-header').after(progressBarHtml);
    }

    // 3. For each topic-item, replace the bullet with a checkbox
    let matchedCount = 0;
    let unmatchedCount = 0;
    
    $('.topic-item').each((i, item) => {
      const textElem = $(item).find('.topic-text');
      const topicText = textElem.text().trim();
      const norm = normalizeText(topicText);
      
      let checkboxId = syllabusItemsMap[subject.slug][norm];
      
      // Fallback: search for sub-matches or partial text
      if (!checkboxId) {
        for (const [syllabusText, id] of Object.entries(syllabusItemsMap[subject.slug])) {
          if (norm.includes(syllabusText) || syllabusText.includes(norm)) {
            checkboxId = id;
            break;
          }
        }
      }

      if (checkboxId) {
        matchedCount++;
        // Replace span.topic-bullet with input.syllabus-checkbox if not already done
        if ($(item).find('.syllabus-checkbox').length === 0) {
          $(item).find('.topic-bullet').replaceWith(`<input type="checkbox" class="syllabus-checkbox" id="${checkboxId}" style="margin-right: 0.5rem;">`);
        }
      } else {
        unmatchedCount++;
        // If not found in syllabus, we generate a unique local one to prevent errors
        const uniqueId = `local-${subject.slug}-${i}`;
        if ($(item).find('.syllabus-checkbox').length === 0) {
          $(item).find('.topic-bullet').replaceWith(`<input type="checkbox" class="syllabus-checkbox" id="${uniqueId}" style="margin-right: 0.5rem;">`);
        }
      }
    });

    console.log(`[${subject.slug}] Checkboxes mapped: ${matchedCount} matched, ${unmatchedCount} created locally`);

    // 4. Inject JS handler for checkboxes & progress calculation
    // Let's remove any existing custom script block for progress first
    $('script').each((_, s) => {
      const scriptContent = $(s).html() || '';
      if (scriptContent.includes('subjectProgressBar')) {
        $(s).remove();
      }
    });

    const scriptCode = `
        document.addEventListener('DOMContentLoaded', () => {
            const checkboxes = document.querySelectorAll('.syllabus-checkbox');
            const progressBar = document.getElementById('subjectProgressBar');
            const progressPercent = document.getElementById('subjectProgressPercent');
            const storedProgress = JSON.parse(localStorage.getItem('ssc-cgl-syllabus-progress')) || {};

            function updateProgress() {
                const total = checkboxes.length;
                const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
                const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;
                if (progressBar) progressBar.style.width = \`\${percentage}%\`;
                if (progressPercent) progressPercent.textContent = \`\${percentage}%\`;
            }

            checkboxes.forEach(checkbox => {
                const id = checkbox.id;
                if (storedProgress[id]) {
                    checkbox.checked = true;
                }

                checkbox.addEventListener('change', () => {
                    storedProgress[checkbox.id] = checkbox.checked;
                    localStorage.setItem('ssc-cgl-syllabus-progress', JSON.stringify(storedProgress));
                    updateProgress();
                });

                // Toggling by clicking parent item (excluding clicks on the anchor links)
                const parent = checkbox.closest('.topic-item');
                if (parent) {
                    parent.addEventListener('click', (e) => {
                        if (e.target !== checkbox && e.target.tagName !== 'A') {
                            checkbox.checked = !checkbox.checked;
                            checkbox.dispatchEvent(new Event('change'));
                        }
                    });
                }
            });

            updateProgress();
        });
    `;

    $('body').append(`<script>${scriptCode}</script>`);

    // Write back updated file
    fs.writeFileSync(indexPath, $.html(), 'utf8');
  }

  console.log('Progress bars successfully integrated into all subject pages!');
}

processProgressBars();
