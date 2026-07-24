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

const years = Array.from({ length: 16 }, (_, i) => 2025 - i);
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function callGemini(promptText) {
  return new Promise((resolve, reject) => {
    const payload = JSON.stringify({
      contents: [{ parts: [{ text: promptText }] }],
      generationConfig: { temperature: 0.35, responseMimeType: 'application/json' },
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
            if (!text) reject(new Error(data.slice(0, 500)));
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

function promptFor(topic) {
  return `Generate SSC CGL Indian Polity Previous Year Question content for topic: "${topic}".
Return ONLY valid JSON array with exactly 16 objects, one for each year in this order: ${years.join(', ')}.
Use bilingual fields with English and Hindi text. Use realistic SSC CGL PYQ/trend-style questions; do not claim exact official wording unless certain.
Every object must have:
year, question_en, question_hi, options [{key:"A", en, hi},...D], answer_key, answer_en, answer_hi, solution_en, solution_hi, topic_en, topic_hi, difficulty, exam_shift_en, exam_shift_hi, repeated_concept_en, repeated_concept_hi, expected_similar_question_en, expected_similar_question_hi, asked_again_en, asked_again_hi, similar_pyq_en, similar_pyq_hi, related_article_en, related_article_hi.
Keep each field concise but useful for SSC CGL revision.`;
}

function esc(value) {
  return String(value ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function parseJson(text) {
  const cleaned = text.replace(/^```json\s*/i, '').replace(/```$/i, '').trim();
  return JSON.parse(cleaned);
}

function renderPyqs(topicName, items) {
  const cards = items.map((item, index) => {
    const options = (item.options || []).map((opt) => `
                    <li><span class="lang-en">(${esc(opt.key)}) ${esc(opt.en)}</span><span class="lang-hi">(${esc(opt.key)}) ${esc(opt.hi)}</span></li>`).join('');
    return `
            <section class="pyq-year-block">
                <h3>${esc(item.year)}</h3>
                <article class="practice-card pyq-card">
                    <div class="level-badge"><span class="lang-en">SSC CGL PYQ Trend ${index + 1}</span><span class="lang-hi">SSC CGL PYQ ट्रेंड ${index + 1}</span></div>
                    <div class="q-text">
                        <p class="lang-en"><strong>Question:</strong> ${esc(item.question_en)}</p>
                        <p class="lang-hi"><strong>प्रश्न:</strong> ${esc(item.question_hi)}</p>
                    </div>
                    <ol class="q-options pyq-options" type="A">${options}
                    </ol>
                    <details class="solution-details">
                        <summary><span class="lang-en"><i class="fas fa-key"></i> Answer & Detailed Solution</span><span class="lang-hi"><i class="fas fa-key"></i> उत्तर और विस्तृत समाधान</span></summary>
                        <div class="solution-body">
                            <div class="correct-answer">
                                <p class="lang-en"><strong>Answer:</strong> (${esc(item.answer_key)}) ${esc(item.answer_en)}</p>
                                <p class="lang-hi"><strong>उत्तर:</strong> (${esc(item.answer_key)}) ${esc(item.answer_hi)}</p>
                            </div>
                            <div class="explanation">
                                <p class="lang-en"><strong>Detailed Solution:</strong> ${esc(item.solution_en)}</p>
                                <p class="lang-hi"><strong>विस्तृत समाधान:</strong> ${esc(item.solution_hi)}</p>
                            </div>
                            <div class="related-concept">
                                <p class="lang-en"><strong>Topic:</strong> ${esc(item.topic_en || topicName)}</p>
                                <p class="lang-hi"><strong>विषय:</strong> ${esc(item.topic_hi)}</p>
                            </div>
                            <div class="q-meta">
                                <span><span class="lang-en"><strong>Difficulty:</strong> ${esc(item.difficulty)}</span><span class="lang-hi"><strong>कठिनाई:</strong> ${esc(item.difficulty)}</span></span>
                                <span><span class="lang-en"><strong>Exam Shift:</strong> ${esc(item.exam_shift_en)}</span><span class="lang-hi"><strong>परीक्षा शिफ्ट:</strong> ${esc(item.exam_shift_hi)}</span></span>
                            </div>
                            <div class="memory-tip">
                                <p class="lang-en"><strong>Repeated Concept:</strong> ${esc(item.repeated_concept_en)}</p>
                                <p class="lang-hi"><strong>बार-बार पूछा गया कॉन्सेप्ट:</strong> ${esc(item.repeated_concept_hi)}</p>
                            </div>
                            <div class="why-wrong">
                                <p class="lang-en"><strong>Expected Similar Question:</strong> ${esc(item.expected_similar_question_en)}</p>
                                <p class="lang-hi"><strong>अपेक्षित समान प्रश्न:</strong> ${esc(item.expected_similar_question_hi)}</p>
                            </div>
                            <div class="related-concept">
                                <p class="lang-en"><strong>Asked Again?</strong> ${esc(item.asked_again_en)}</p>
                                <p class="lang-hi"><strong>फिर पूछा गया?</strong> ${esc(item.asked_again_hi)}</p>
                                <p class="lang-en"><strong>Similar PYQ:</strong> ${esc(item.similar_pyq_en)}</p>
                                <p class="lang-hi"><strong>समान PYQ:</strong> ${esc(item.similar_pyq_hi)}</p>
                                <p class="lang-en"><strong>Related Article:</strong> ${esc(item.related_article_en)}</p>
                                <p class="lang-hi"><strong>संबंधित लेख:</strong> ${esc(item.related_article_hi)}</p>
                            </div>
                        </div>
                    </details>
                </article>
            </section>`;
  }).join('\n');

  return `<!-- Tab 3 Panel: PYQs -->
        <div id="tab-pyqs" class="tab-panel">
            <div class="pyq-timeline">
                <h2><span class="lang-en">Previous Year Questions</span><span class="lang-hi">पिछले वर्ष के प्रश्न</span></h2>
                <p><span class="lang-en">Year-wise SSC CGL polity questions with answer, detailed solution, repeated concept, similar PYQ and expected follow-up question.</span><span class="lang-hi">उत्तर, विस्तृत समाधान, दोहराए गए कॉन्सेप्ट, समान PYQ और अपेक्षित समान प्रश्न के साथ वर्षवार SSC CGL राजनीति प्रश्न।</span></p>
                <div class="pyq-year-chain">${years.map((year) => `<span>${year}</span>`).join('<i class="fas fa-arrow-down"></i>')}</div>
${cards}
            </div>
        </div>`;
}

function injectPyqs(html, pyqHtml) {
  const start = html.indexOf('<!-- Tab 3 Panel: PYQs');
  const end = html.indexOf('<!-- Tab 4 Panel: Mini Test', start);
  if (start === -1 || end === -1) throw new Error('Could not locate Tab 3 PYQ panel');
  return html.slice(0, start) + pyqHtml + '\n\n        ' + html.slice(end);
}

async function main() {
  const base = path.join(root, 'ssc-cgl', 'general-awareness', 'general-policy-polity');
  for (let i = 0; i < topics.length; i += 1) {
    const [name, slug] = topics[i];
    const file = path.join(base, slug, 'index.html');
    const html = fs.readFileSync(file, 'utf8');
    if (html.includes('class="pyq-timeline"')) {
      console.log(`[${i + 1}/${topics.length}] Skipping existing PYQs: ${name}`);
      continue;
    }
    console.log(`[${i + 1}/${topics.length}] Generating PYQs: ${name}`);
    let items = null;
    let lastError = null;
    for (let attempt = 1; attempt <= 3; attempt += 1) {
      try {
        const response = await callGemini(promptFor(name));
        items = parseJson(response);
        break;
      } catch (error) {
        lastError = error;
        console.warn(`[${i + 1}/${topics.length}] Parse/API attempt ${attempt} failed: ${error.message}`);
        await sleep(2500 * attempt);
      }
    }
    if (!items) throw lastError;
    if (!Array.isArray(items) || items.length !== 16) throw new Error(`Expected 16 PYQs for ${name}`);
    fs.writeFileSync(file, injectPyqs(html, renderPyqs(name, items)), 'utf8');
    console.log(`[${i + 1}/${topics.length}] Updated: ${slug}`);
    await sleep(2500);
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
