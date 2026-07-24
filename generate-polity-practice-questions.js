const fs = require('fs');
const path = require('path');
const https = require('https');

// Read API Key from .env
const envContent = fs.readFileSync('c:/Users/sande/Documents/GitHub/sjmaths-website/.env', 'utf8');
const keyMatch = envContent.match(/GEMINI_API_KEY\s*=\s*(.*)/);
const apiKey = keyMatch ? keyMatch[1].trim() : '';

if (!apiKey) {
    console.error('ERROR: GEMINI_API_KEY not found in .env file!');
    process.exit(1);
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// Call Gemini API with fallback
async function callGemini(promptText) {
    const modelsToTry = ['gemini-3.5-flash-lite', 'gemini-3.1-flash-lite', 'gemini-3.6-flash'];
    let lastError = null;

    for (const modelName of modelsToTry) {
        try {
            const resText = await new Promise((resolve, reject) => {
                const payload = JSON.stringify({
                    contents: [{
                        parts: [{ text: promptText }]
                    }]
                });

                const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + modelName + ':generateContent?key=' + apiKey;
                const req = https.request(url, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Content-Length': Buffer.byteLength(payload)
                    }
                }, (res) => {
                    let data = '';
                    res.on('data', chunk => data += chunk);
                    res.on('end', () => {
                        try {
                            const json = JSON.parse(data);
                            if (json.candidates && json.candidates[0] && json.candidates[0].content) {
                                resolve(json.candidates[0].content.parts[0].text);
                            } else {
                                reject(new Error(data));
                            }
                        } catch (e) {
                            reject(e);
                        }
                    });
                });

                req.on('error', reject);
                req.write(payload);
                req.end();
            });

            return resText;
        } catch (err) {
            console.warn(`[Warning] Model ${modelName} failed: ${err.message.substring(0, 100)}...`);
            lastError = err;
            await sleep(2000);
        }
    }
    throw lastError;
}

// The 18 polity topics with their slugs
const polityTopics = [
    { name: "Constituent Assembly & Making of Constitution", slug: "constituent-assembly-and-making-of-constitution" },
    { name: "Preamble of the Constitution", slug: "preamble-of-the-constitution" },
    { name: "Sources of the Indian Constitution", slug: "sources-of-the-indian-constitution" },
    { name: "Parts & Schedules of the Constitution", slug: "parts-and-schedules-of-the-constitution" },
    { name: "Citizenship (Articles 5-11 & CAA)", slug: "citizenship-articles-5-11-and-caa" },
    { name: "Fundamental Rights (Articles 12-35 & Writs)", slug: "fundamental-rights-articles-12-35-and-writs" },
    { name: "Directive Principles of State Policy (DPSP, Articles 36-51)", slug: "directive-principles-of-state-policy-dpsp-articles-36-51" },
    { name: "Fundamental Duties (Article 51A & Swaran Singh)", slug: "fundamental-duties-article-51a-and-swaran-singh" },
    { name: "Union Executive: President, VP, PM & Cabinet", slug: "union-executive-president-vp-pm-and-cabinet" },
    { name: "Parliament: Lok Sabha, Rajya Sabha & Officers", slug: "parliament-lok-sabha-rajya-sabha-and-officers" },
    { name: "Parliamentary Proceedings: Bills, Motions & Committees", slug: "parliamentary-proceedings-bills-motions-and-committees" },
    { name: "State Executive: Governor, CM & Council", slug: "state-executive-governor-cm-and-council" },
    { name: "State Legislature: Assembly & Council", slug: "state-legislature-assembly-and-council" },
    { name: "Judiciary: Supreme Court & High Courts", slug: "judiciary-supreme-court-and-high-courts" },
    { name: "Panchayati Raj System (73rd Amendment & 11th Schedule)", slug: "panchayati-raj-system-73rd-amendment-and-11th-schedule" },
    { name: "Municipalities (74th Amendment & 12th Schedule)", slug: "municipalities-74th-amendment-and-12th-schedule" },
    { name: "Constitutional Bodies: EC, FC, CAG, UPSC", slug: "constitutional-bodies-ec-fc-cag-upsc" },
    { name: "Statutory & Non-Constitutional Bodies: NITI Aayog, NHRC, Lokpal", slug: "statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal" }
];

function buildPrompt(topicName) {
    return `You are a Senior SSC CGL Polity Faculty member. Generate 49 BILINGUAL (English & Hindi) practice questions on "${topicName}" for SSC CGL exam.

STRICT FORMAT: Generate 7 questions for each of the 7 levels below:

Level 1: Basic Recall (7 questions)
Level 2: Conceptual (7 questions)
Level 3: Statement Based (7 questions)
Level 4: Assertion-Reason (7 questions)
Level 5: Match the Following (7 questions)
Level 6: Previous Trend Style (7 questions)
Level 7: Mixed Questions (7 questions)

For EVERY question, include ALL these fields in BILINGUAL:
- Question: (English + Hindi)
- Options: A, B, C, D (English + Hindi)
- Correct Answer: (English + Hindi)
- Detailed Explanation: (English + Hindi)
- Why Others Are Wrong: (English + Hindi)
- Memory Tip: (English + Hindi)
- Related Concept: (English + Hindi)
- Difficulty: Easy/Medium/Hard
- Time Required: X seconds

OUTPUT FORMAT:
Use exact HTML structure below for each question card:

<div class="practice-card" data-level="1" data-difficulty="Easy" data-time="30s">
  <div class="level-badge"><span class="lang-en">Level 1: Basic Recall</span><span class="lang-hi">स्तर 1: मूल स्मरण</span></div>
  <div class="q-number"><span class="lang-en"><strong>Q1.</strong></span><span class="lang-hi"><strong>प्र 1.</strong></span></div>
  <div class="q-text">
    <p class="lang-en">Question in English?</p>
    <p class="lang-hi">प्रश्न हिंदी में?</p>
  </div>
  <div class="q-options">
    <div class="option"><span class="lang-en">(A) Option A</span><span class="lang-hi">(A) विकल्प A</span></div>
    <div class="option"><span class="lang-en">(B) Option B</span><span class="lang-hi">(B) विकल्प B</span></div>
    <div class="option"><span class="lang-en">(C) Option C</span><span class="lang-hi">(C) विकल्प C</span></div>
    <div class="option"><span class="lang-en">(D) Option D</span><span class="lang-hi">(D) विकल्प D</span></div>
  </div>
  <details class="solution-details">
    <summary><span class="lang-en"><i class="fas fa-key"></i> View Solution</span><span class="lang-hi"><i class="fas fa-key"></i> हल देखें</span></summary>
    <div class="solution-body">
      <div class="correct-answer">
        <p class="lang-en"><strong>Correct Answer:</strong> (A) Option</p>
        <p class="lang-hi"><strong>सही उत्तर:</strong> (A) विकल्प</p>
      </div>
      <div class="explanation">
        <p class="lang-en"><strong>Detailed Explanation:</strong> Explanation in English...</p>
        <p class="lang-hi"><strong>विस्तृत व्याख्या:</strong> हिंदी में व्याख्या...</p>
      </div>
      <div class="why-wrong">
        <p class="lang-en"><strong>Why Others Are Wrong:</strong> Explanation of incorrect options...</p>
        <p class="lang-hi"><strong>अन्य क्यों गलत हैं:</strong> गलत विकल्पों की व्याख्या...</p>
      </div>
      <div class="memory-tip">
        <p class="lang-en"><strong><i class="fas fa-lightbulb"></i> Memory Tip:</strong> Tip to remember...</p>
        <p class="lang-hi"><strong><i class="fas fa-lightbulb"></i> याद रखने की टिप:</strong> याद रखने का तरीका...</p>
      </div>
      <div class="related-concept">
        <p class="lang-en"><strong>Related Concept:</strong> Concept name</p>
        <p class="lang-hi"><strong>संबंधित अवधारणा:</strong> अवधारणा का नाम</p>
      </div>
      <div class="q-meta">
        <span class="difficulty"><span class="lang-en">Difficulty:</span><span class="lang-hi">कठिनाई:</span> Easy/Medium/Hard</span>
        <span class="time"><span class="lang-en">Time:</span><span class="lang-hi">समय:</span> 30s</span>
      </div>
    </div>
  </details>
</div>

Return your output between [PRACTICE_START] and [PRACTICE_END] tags.`;
}

function parseContent(aiText) {
    const regex = /\[PRACTICE_START\]([\s\S]*?)\[PRACTICE_END\]/;
    const match = aiText.match(regex);
    return match ? match[1].trim() : aiText.trim();
}

function buildPracticeCSS() {
    return `
        /* Practice Questions Tab Styling */
        .practice-progress-bar {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1rem 1.25rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-lg);
        }
        
        .practice-stats {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 0.75rem;
        }
        
        .practice-stats span {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-dark);
        }
        
        .practice-stats .stat-highlight {
            color: var(--primary);
            font-size: 1rem;
        }
        
        .progress-track {
            display: flex;
            gap: 0.35rem;
            align-items: center;
        }
        
        .progress-dot {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #e2e8f0;
            transition: all 0.3s ease;
        }
        
        .progress-dot.completed { background: #2ecc71; }
        .progress-dot.current { background: var(--primary); transform: scale(1.3); }
        
        .level-navigation {
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            overflow-x: auto;
            padding-bottom: 0.5rem;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        
        .level-navigation::-webkit-scrollbar { display: none; }
        
        .level-btn {
            background: transparent;
            border: 1px solid rgba(142, 68, 173, 0.2);
            outline: none;
            padding: 0.5rem 0.75rem;
            font-family: 'Outfit', sans-serif;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-light);
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.25s ease;
            white-space: nowrap;
            flex-shrink: 0;
        }
        
        .level-btn:hover { background: rgba(142, 68, 173, 0.05); color: var(--primary); }
        
        .level-btn.active {
            background: var(--accent-gradient);
            color: #fff;
            border-color: transparent;
            box-shadow: 0 4px 10px rgba(142, 68, 173, 0.25);
        }
        
        .level-section { display: none; }
        .level-section.active { display: block; }
        
        .level-header {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--primary);
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
        }
        
        .practice-card {
            background: #fff;
            border: 1px solid rgba(142, 68, 173, 0.12);
            border-radius: 0.85rem;
            padding: 1.15rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 3px 10px rgba(0,0,0,0.03);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        
        .practice-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(142, 68, 173, 0.1);
        }
        
        .level-badge {
            display: inline-block;
            background: rgba(142, 68, 173, 0.08);
            color: var(--primary);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            margin-bottom: 0.6rem;
        }
        
        .q-number {
            font-size: 0.9rem;
            color: var(--text-dark);
            margin-bottom: 0.5rem;
        }
        
        .q-text {
            font-size: 0.95rem;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 0.75rem;
            line-height: 1.5;
        }
        
        .q-options {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0.5rem;
            margin-bottom: 0.85rem;
        }
        
        @media (max-width: 600px) {
            .q-options { grid-template-columns: 1fr; }
        }
        
        .option {
            background: rgba(0,0,0,0.02);
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 6px;
            padding: 0.5rem 0.75rem;
            font-size: 0.88rem;
            color: #34495e;
        }
        
        .option.correct {
            background: rgba(46, 204, 113, 0.08);
            border-color: rgba(46, 204, 113, 0.3);
        }
        
        details.solution-details {
            margin-top: 0.6rem;
            border-top: 1px dashed rgba(0,0,0,0.08);
            padding-top: 0.5rem;
        }
        
        details.solution-details summary {
            font-weight: 700;
            color: var(--primary);
            cursor: pointer;
            font-size: 0.88rem;
            user-select: none;
            outline: none;
            padding: 0.4rem 0;
        }
        
        .solution-body {
            margin-top: 0.75rem;
            background: rgba(142, 68, 173, 0.03);
            border-radius: 8px;
            padding: 1rem;
            font-size: 0.88rem;
            line-height: 1.6;
        }
        
        .solution-body > div {
            margin-bottom: 0.7rem;
            padding-bottom: 0.7rem;
            border-bottom: 1px solid rgba(0,0,0,0.04);
        }
        
        .solution-body > div:last-child {
            margin-bottom: 0;
            padding-bottom: 0;
            border-bottom: none;
        }
        
        .correct-answer { color: #27ae60; font-weight: 700; }
        
        .explanation { color: var(--text-dark); }
        
        .why-wrong {
            background: rgba(231, 76, 60, 0.04);
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            border-left: 3px solid rgba(231, 76, 60, 0.3);
        }
        
        .memory-tip {
            background: linear-gradient(135deg, rgba(241, 196, 15, 0.1), rgba(230, 126, 34, 0.1));
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            border-left: 3px solid #f39c12;
        }
        
        .related-concept {
            background: rgba(52, 152, 219, 0.06);
            padding: 0.5rem 0.75rem;
            border-radius: 6px;
            border-left: 3px solid #3498db;
        }
        
        .q-meta {
            display: flex;
            gap: 1rem;
            font-size: 0.8rem;
            color: var(--text-light);
            font-weight: 600;
        }
        
        .q-meta .difficulty { color: var(--primary); }
        .q-meta .time { color: #e74c3c; }`;
}

function injectIntoPage(existingHtml, practiceContent, cssStyles) {
    // Add practice CSS to the head
    const cssEndMarker = '</style>';
    const cssIndex = existingHtml.indexOf(cssEndMarker);
    if (cssIndex !== -1) {
        existingHtml = existingHtml.slice(0, cssIndex + cssEndMarker.length) + cssStyles + existingHtml.slice(cssIndex + cssEndMarker.length);
    }

    // Replace the coming soon placeholder in Tab 2 with practice content
    const tab2Start = '<!-- Tab 2 Panel: Practice Questions (Coming Soon) -->';
    const tab2End = '<!-- Tab 3 Panel: PYQs (Coming Soon) -->';

    const startIdx = existingHtml.indexOf(tab2Start);
    const endIdx = existingHtml.indexOf(tab2End);

    if (startIdx !== -1 && endIdx !== -1) {
        const tab2Html = `<!-- Tab 2 Panel: Practice Questions -->
        <div id="tab-practice" class="tab-panel">
            <div class="practice-progress-bar">
                <div class="practice-stats">
                    <span><span class="lang-en">Total Questions:</span><span class="lang-hi">कुल प्रश्न:</span> <span class="stat-highlight">49</span></span>
                    <span><span class="lang-en">Attempted:</span><span class="lang-hi">प्रयास किए:</span> <span class="stat-highlight" id="attemptedCount">0</span></span>
                    <span><span class="lang-en">Correct:</span><span class="lang-hi">सही:</span> <span class="stat-highlight" id="correctCount">0</span></span>
                    <span><span class="lang-en">Score:</span><span class="lang-hi">स्कोर:</span> <span class="stat-highlight" id="scoreDisplay">0%</span></span>
                </div>
                <div class="progress-track" id="progressTrack"></div>
            </div>
            
            <div class="level-navigation" id="levelNav">
                <button class="level-btn active" data-level="1"><span class="lang-en">L1: Basic Recall</span><span class="lang-hi">L1: मूल स्मरण</span></button>
                <button class="level-btn" data-level="2"><span class="lang-en">L2: Conceptual</span><span class="lang-hi">L2: अवधारणात्मक</span></button>
                <button class="level-btn" data-level="3"><span class="lang-en">L3: Statement</span><span class="lang-hi">L3: कथन आधारित</span></button>
                <button class="level-btn" data-level="4"><span class="lang-en">L4: Assertion-Reason</span><span class="lang-hi">L4: अभिकथन-कारण</span></button>
                <button class="level-btn" data-level="5"><span class="lang-en">L5: Match</span><span class="lang-hi">L5: मिलान</span></button>
                <button class="level-btn" data-level="6"><span class="lang-en">L6: Trend Style</span><span class="lang-hi">L6: ट्रेंड शैली</span></button>
                <button class="level-btn" data-level="7"><span class="lang-en">L7: Mixed</span><span class="lang-hi">L7: मिश्रित</span></button>
            </div>
            
            ${practiceContent}
        </div>`;

        existingHtml = existingHtml.slice(0, startIdx) + tab2Html + existingHtml.slice(endIdx);
    }

    // Add level navigation script at the end
    const scriptEnd = '</script>';
    const lastScriptIdx = existingHtml.lastIndexOf(scriptEnd);
    if (lastScriptIdx !== -1) {
        const navScript = `
        <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Level navigation
            const levelBtns = document.querySelectorAll('#levelNav .level-btn');
            const levelSections = document.querySelectorAll('.level-section');
            
            levelBtns.forEach(btn => {
                btn.addEventListener('click', function() {
                    levelBtns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');
                    levelSections.forEach(s => s.classList.remove('active'));
                    const target = document.getElementById('level-' + this.dataset.level);
                    if (target) target.classList.add('active');
                });
            });
            
            // Progress tracking
            const totalQuestions = 49;
            const progressTrack = document.getElementById('progressTrack');
            if (progressTrack) {
                for (let i = 1; i <= totalQuestions; i++) {
                    const dot = document.createElement('span');
                    dot.className = 'progress-dot';
                    dot.dataset.qId = i;
                    progressTrack.appendChild(dot);
                }
            }
            
            // Track solution views
            const details = document.querySelectorAll('.solution-details');
            details.forEach((det, idx) => {
                det.addEventListener('toggle', function() {
                    if (this.open) {
                        const dots = document.querySelectorAll('.progress-dot');
                        if (dots[idx]) {
                            dots[idx].classList.add('completed');
                        }
                        const attempted = document.querySelectorAll('.progress-dot.completed').length;
                        const attemptedCount = document.getElementById('attemptedCount');
                        if (attemptedCount) attemptedCount.textContent = attempted + '/' + totalQuestions;
                    }
                });
            });
        });
        </script>`;
        existingHtml = existingHtml.slice(0, lastScriptIdx + scriptEnd.length) + navScript + existingHtml.slice(lastScriptIdx + scriptEnd.length);
    }

    return existingHtml;
}

async function runGenerator() {
    console.log('🚀 Starting Polity Practice Questions Generator...');
    console.log(`📋 Total topics to process: ${polityTopics.length}\n`);

    for (let i = 0; i < polityTopics.length; i++) {
        const topic = polityTopics[i];
        const targetDir = path.join(
            'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/general-policy-polity',
            topic.slug
        );
        const targetFile = path.join(targetDir, 'index.html');

        if (!fs.existsSync(targetFile)) {
            console.error(`❌ File not found for ${topic.name}, skipping...`);
            continue;
        }

        console.log(`⏳ [${i + 1}/${polityTopics.length}] Generating practice questions for: ${topic.name}`);

        const prompt = buildPrompt(topic.name);

        try {
            const aiResponse = await callGemini(prompt);
            const practiceContent = parseContent(aiResponse);
            const cssStyles = buildPracticeCSS();

            const existingHtml = fs.readFileSync(targetFile, 'utf8');
            const updatedHtml = injectIntoPage(existingHtml, practiceContent, cssStyles);

            fs.writeFileSync(targetFile, updatedHtml, 'utf8');
            console.log(`✅ Updated: ${targetFile}`);
        } catch (err) {
            console.error(`❌ Failed for topic: ${topic.name}`, err.message);
        }

        await sleep(4000);
    }
    console.log('\n🎉 Practice Questions Generation Completed!');
}

runGenerator();