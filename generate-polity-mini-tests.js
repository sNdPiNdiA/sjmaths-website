const fs = require('fs');
const path = require('path');
const https = require('https');

const root = __dirname;
const envPath = path.join(root, '.env');
const envContent = fs.existsSync(envPath) ? fs.readFileSync(envPath, 'utf8') : '';
const apiKey = (envContent.match(/GEMINI_API_KEY\s*=\s*(.+)/) || [])[1]?.trim();

if (!apiKey) {
  console.error('ERROR: GEMINI_API_KEY not found in .env');
  process.exit(1);
}

const baseDir = path.join(root, 'ssc-cgl', 'general-awareness', 'general-policy-polity');
const topics = [
  ['Constituent Assembly & Making of Constitution', 'constituent-assembly-and-making-of-constitution'],
  ['Preamble of the Constitution', 'preamble-of-the-constitution'],
  ['Sources of the Indian Constitution', 'sources-of-the-indian-constitution'],
  ['Parts & Schedules of the Constitution', 'parts-and-schedules-of-the-constitution'],
  ['Citizenship (Articles 5-11 & CAA)', 'citizenship-articles-5-11-and-caa'],
  ['Fundamental Rights (Articles 12-35 & Writs)', 'fundamental-rights-articles-12-35-and-writs'],
  ['Directive Principles of State Policy (DPSP, Articles 36-51)', 'directive-principles-of-state-policy-dpsp-articles-36-51'],
  ['Fundamental Duties (Article 51A & Swaran Singh)', 'fundamental-duties-article-51a-and-swaran-singh'],
  ['Union Executive: President, VP, PM & Cabinet', 'union-executive-president-vp-pm-and-cabinet'],
  ['Parliament: Lok Sabha, Rajya Sabha & Officers', 'parliament-lok-sabha-rajya-sabha-and-officers'],
  ['Parliamentary Proceedings: Bills, Motions & Committees', 'parliamentary-proceedings-bills-motions-and-committees'],
  ['State Executive: Governor, CM & Council', 'state-executive-governor-cm-and-council'],
  ['State Legislature: Assembly & Council', 'state-legislature-assembly-and-council'],
  ['Judiciary: Supreme Court & High Courts', 'judiciary-supreme-court-and-high-courts'],
  ['Panchayati Raj System (73rd Amendment & 11th Schedule)', 'panchayati-raj-system-73rd-amendment-and-11th-schedule'],
  ['Municipalities (74th Amendment & 12th Schedule)', 'municipalities-74th-amendment-and-12th-schedule'],
  ['Constitutional Bodies: EC, FC, CAG, UPSC', 'constitutional-bodies-ec-fc-cag-upsc'],
  ['Statutory & Non-Constitutional Bodies: NITI Aayog, NHRC, Lokpal', 'statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal'],
];

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function callGemini(promptText) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      contents: [{ parts: [{ text: promptText }] }],
      generationConfig: { temperature: 0.45, responseMimeType: 'application/json' },
    });

    const req = https.request(
      `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`,
      { method: 'POST', headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(payload) } },
      (res) => {
        let data = '';
        res.on('data', (chunk) => (data += chunk));
        res.on('end', () => {
          try {
            const json = JSON.parse(data);
            const text = json.candidates?.[0]?.content?.parts?.[0]?.text;
            if (!text) reject(new Error(data.slice(0, 600)));
            else resolve(text);
          } catch (error) {
            reject(error);
          }
        });
      }
    );
    req.on('error', reject);
    req.write(payload);
    req.end();
  });
}

function buildPrompt(topicName) {
  return `Generate a fresh SSC CGL-level Indian Polity mini test for topic: "${topicName}".
Return ONLY valid JSON array with exactly 10 objects.
Questions must be new, exam-level, bilingual, and not copied from previous practice/PYQ content.
Mix SSC CGL styles: direct fact, article/schedule matching, statement-based, assertion-reason, and conceptual application.
Each object must contain:
question_en, question_hi,
options: [{key:"A", en, hi}, {key:"B", en, hi}, {key:"C", en, hi}, {key:"D", en, hi}],
answer_key, answer_en, answer_hi,
solution_en, solution_hi,
concept_en, concept_hi,
difficulty ("Easy"|"Medium"|"Hard"),
time_seconds (integer 35-75).
Keep language clear for SSC CGL Tier 1/Tier 2 revision.`;
}

function parseJson(text) {
  return JSON.parse(text.replace(/^```json\s*/i, '').replace(/```$/i, '').trim());
}

function esc(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function titleCase(slug) {
  return slug.split('-').map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
}

function renderQuestion(slug, item, index) {
  const qid = `${slug}-mini-${index + 1}`;
  const options = item.options.map((opt) => `
                        <label class="option mini-test-option">
                            <input type="radio" name="${qid}" value="${esc(opt.key)}">
                            <span class="lang-en">(${esc(opt.key)}) ${esc(opt.en)}</span>
                            <span class="lang-hi">(${esc(opt.key)}) ${esc(opt.hi)}</span>
                        </label>`).join('');

  return `
                <article class="practice-card mini-test-question" data-mini-answer="${esc(item.answer_key)}" data-question-id="${index + 1}">
                    <div class="level-badge"><span class="lang-en">SSC CGL Mini Test Q${index + 1}</span><span class="lang-hi">SSC CGL मिनी टेस्ट प्रश्न ${index + 1}</span></div>
                    <div class="q-text">
                        <p class="lang-en"><strong>Q${index + 1}.</strong> ${esc(item.question_en)}</p>
                        <p class="lang-hi"><strong>प्र${index + 1}.</strong> ${esc(item.question_hi)}</p>
                    </div>
                    <div class="q-options mini-test-options">${options}
                    </div>
                    <details class="solution-details mini-test-solution">
                        <summary><span class="lang-en"><i class="fas fa-key"></i> View Solution</span><span class="lang-hi"><i class="fas fa-key"></i> समाधान देखें</span></summary>
                        <div class="solution-body">
                            <div class="correct-answer">
                                <p class="lang-en"><strong>Correct Answer:</strong> (${esc(item.answer_key)}) ${esc(item.answer_en)}</p>
                                <p class="lang-hi"><strong>सही उत्तर:</strong> (${esc(item.answer_key)}) ${esc(item.answer_hi)}</p>
                            </div>
                            <div class="explanation">
                                <p class="lang-en"><strong>Detailed Solution:</strong> ${esc(item.solution_en)}</p>
                                <p class="lang-hi"><strong>विस्तृत समाधान:</strong> ${esc(item.solution_hi)}</p>
                            </div>
                            <div class="related-concept">
                                <p class="lang-en"><strong>Concept Tested:</strong> ${esc(item.concept_en)}</p>
                                <p class="lang-hi"><strong>परीक्षित अवधारणा:</strong> ${esc(item.concept_hi)}</p>
                            </div>
                            <div class="q-meta">
                                <span><span class="lang-en"><strong>Difficulty:</strong> ${esc(item.difficulty)}</span><span class="lang-hi"><strong>कठिनाई:</strong> ${esc(item.difficulty)}</span></span>
                                <span><span class="lang-en"><strong>Target Time:</strong> ${esc(item.time_seconds)}s</span><span class="lang-hi"><strong>लक्ष्य समय:</strong> ${esc(item.time_seconds)}s</span></span>
                            </div>
                        </div>
                    </details>
                </article>`;
}

function renderMiniTest(topicName, slug, items) {
  return `<!-- Tab 4 Panel: Mini Test -->
        <div id="tab-mini-test" class="tab-panel">
            <div class="mini-test-container" data-mini-test>
                <h2><span class="lang-en">Mini Test: ${esc(topicName)}</span><span class="lang-hi">मिनी टेस्ट: ${esc(topicName)}</span></h2>
                <p><span class="lang-en">Fresh SSC CGL-level questions generated for this topic. Submit to view score and detailed solutions.</span><span class="lang-hi">इस विषय के लिए नए SSC CGL स्तर के प्रश्न। स्कोर और विस्तृत समाधान देखने के लिए सबमिट करें।</span></p>
                <div class="q-meta mini-test-summary">
                    <span><strong>Questions:</strong> 10</span>
                    <span><strong>Mode:</strong> SSC CGL Topic Test</span>
                    <span><strong>Time Target:</strong> 10 minutes</span>
                </div>
${items.map((item, index) => renderQuestion(slug, item, index)).join('\n')}
                <div class="mini-test-actions">
                    <button type="button" class="next-tab-btn mini-test-submit">Submit Test</button>
                    <button type="button" class="level-btn mini-test-reset">Reset</button>
                </div>
                <div class="mini-test-results" style="display:none;">
                    <h3><span class="lang-en">Your Performance</span><span class="lang-hi">आपका प्रदर्शन</span></h3>
                    <p><span class="lang-en"><strong>Score:</strong> <span class="mini-test-score">0/10</span></span><span class="lang-hi"><strong>स्कोर:</strong> <span class="mini-test-score-hi">0/10</span></span></p>
                    <p><span class="lang-en"><strong>Accuracy:</strong> <span class="mini-test-accuracy">0%</span></span><span class="lang-hi"><strong>सटीकता:</strong> <span class="mini-test-accuracy-hi">0%</span></span></p>
                    <p><span class="lang-en"><strong>Revision Recommendation:</strong> Revisit wrong questions and their concepts before retesting.</span><span class="lang-hi"><strong>पुनरीक्षण सुझाव:</strong> गलत प्रश्नों और उनकी अवधारणाओं को दोबारा पढ़कर फिर टेस्ट दें।</span></p>
                </div>
            </div>
        </div>`;
}

const miniTestScript = `    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('[data-mini-test]').forEach(function(test) {
                var submit = test.querySelector('.mini-test-submit');
                var reset = test.querySelector('.mini-test-reset');
                var results = test.querySelector('.mini-test-results');

                function resetTest() {
                    test.querySelectorAll('input[type="radio"]').forEach(function(input) { input.checked = false; });
                    test.querySelectorAll('.mini-test-question').forEach(function(card) {
                        card.classList.remove('mini-correct', 'mini-wrong');
                        var solution = card.querySelector('.mini-test-solution');
                        if (solution) solution.open = false;
                    });
                    if (results) results.style.display = 'none';
                }

                if (submit) {
                    submit.addEventListener('click', function() {
                        var questions = Array.prototype.slice.call(test.querySelectorAll('.mini-test-question'));
                        var correct = 0;
                        questions.forEach(function(card) {
                            var answer = card.getAttribute('data-mini-answer');
                            var selected = card.querySelector('input[type="radio"]:checked');
                            var solution = card.querySelector('.mini-test-solution');
                            card.classList.remove('mini-correct', 'mini-wrong');
                            if (selected && selected.value === answer) {
                                correct += 1;
                                card.classList.add('mini-correct');
                            } else {
                                card.classList.add('mini-wrong');
                            }
                            if (solution) solution.open = true;
                        });
                        var total = questions.length || 10;
                        var accuracy = Math.round((correct / total) * 100);
                        test.querySelectorAll('.mini-test-score, .mini-test-score-hi').forEach(function(el) { el.textContent = correct + '/' + total; });
                        test.querySelectorAll('.mini-test-accuracy, .mini-test-accuracy-hi').forEach(function(el) { el.textContent = accuracy + '%'; });
                        if (results) results.style.display = 'block';
                    });
                }
                if (reset) reset.addEventListener('click', resetTest);
                resetTest();
            });
        });
    </script>
`;

function injectMiniTest(html, tabHtml) {
  const start = html.indexOf('<!-- Tab 4 Panel');
  const end = html.indexOf('</main>', start);
  if (start === -1 || end === -1) throw new Error('Could not locate Tab 4 panel');
  return html.slice(0, start) + tabHtml + '\n\n    ' + html.slice(end);
}

async function getQuestions(topicName) {
  let lastError;
  for (let attempt = 1; attempt <= 3; attempt += 1) {
    try {
      const response = await callGemini(buildPrompt(topicName));
      const parsed = parseJson(response);
      if (!Array.isArray(parsed) || parsed.length !== 10) throw new Error('Expected exactly 10 questions');
      return parsed;
    } catch (error) {
      lastError = error;
      console.warn(`Attempt ${attempt} failed for ${topicName}: ${error.message}`);
      await sleep(2500 * attempt);
    }
  }
  throw lastError;
}

async function main() {
  for (let i = 0; i < topics.length; i += 1) {
    const [topicName, slug] = topics[i];
    const file = path.join(baseDir, slug, 'index.html');
    if (!fs.existsSync(file)) {
      console.warn(`Skipping missing file: ${slug}`);
      continue;
    }
    console.log(`[${i + 1}/${topics.length}] Generating fresh mini test: ${topicName}`);
    const questions = await getQuestions(topicName);
    let html = fs.readFileSync(file, 'utf8');
    html = injectMiniTest(html, renderMiniTest(topicName, slug, questions));
    html = html.replace(/<script>\s*document\.addEventListener\('DOMContentLoaded', function\(\) \{\s*document\.querySelectorAll\('\[data-mini-test\]'\)[\s\S]*?<\/script>\s*/g, '');
    html = html.replace('</body>', miniTestScript + '</body>');
    fs.writeFileSync(file, html, 'utf8');
    console.log(`[${i + 1}/${topics.length}] Updated: ${slug}`);
    await sleep(2500);
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
