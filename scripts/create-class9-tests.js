const fs = require('fs');
const path = require('path');

const chapters = [
    { num: 1, name: "Number Systems", folder: "chapter-1-number-systems" },
    { num: 2, name: "Polynomials", folder: "chapter-2-polynomials" },
    { num: 3, name: "Coordinate Geometry", folder: "chapter-3-coordinate-geometry" },
    { num: 4, name: "Linear Equations in Two Variables", folder: "chapter-4-linear-equations-in-two-variables" },
    { num: 5, name: "Intro to Euclid's Geometry", folder: "chapter-5-introduction-to-euclids-geometry" },
    { num: 6, name: "Lines and Angles", folder: "chapter-6-lines-and-angles" },
    { num: 7, name: "Triangles", folder: "chapter-7-triangles" },
    { num: 8, name: "Quadrilaterals", folder: "chapter-8-quadrilaterals" },
    { num: 9, name: "Circles", folder: "chapter-9-circles" },
    { num: 10, name: "Heron's Formula", folder: "chapter-10-herons-formula" },
    { num: 11, name: "Surface Areas and Volumes", folder: "chapter-11-surface-areas-and-volumes" },
    { num: 12, name: "Statistics", folder: "chapter-12-statistics" }
];

const baseDir = path.join(__dirname, '../classes/class-9/tests/chapter-wise');

const testTypes = [
    { type: 'basic', label: 'Basic Test', time: 20 },
    { type: 'standard', label: 'Standard Test', time: 30 },
    { type: 'hard', label: 'HOTS Test', time: 45 }
];

function createTestFile(chapter, testType) {
    const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${testType.label} - ${chapter.name} | Class 9 Maths</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../../../../../assets/css/test-interface.min.css">
    
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\\\(', '\\\\)']] },
            svg: { fontCache: 'global' }
        };
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <div class="test-header">
        <div class="logo">SJMaths Test Series</div>
        <div class="timer-badge">
            <i class="fas fa-clock"></i>
            <span id="timerDisplay">00:00</span>
        </div>
    </div>

    <div class="test-container">
        <main class="question-panel">
            <div class="section-header" id="qSection">Section A</div>
            <div class="q-header">
                <span id="qNumber">Question 1</span>
                <span id="qMarks">(1 Mark)</span>
            </div>
            <div class="q-text" id="qText">Loading Question...</div>
            <div id="inputArea"></div>
            <div id="solutionArea" class="solution-div"></div>
        </main>

        <aside class="nav-panel">
            <div style="display:flex; align-items:center; margin-bottom:1rem;">
                <h3 style="margin:0; font-size:1rem;">Question Palette</h3>
            </div>
            <div id="paletteBody">
                <div class="palette-grid" id="questionPalette"></div>
                <div style="margin-top: 2rem; font-size: 0.8rem; color: #666;">
                    <div style="display:flex; gap:8px; align-items:center; margin-bottom:5px;">
                        <span style="width:12px; height:12px; background:#27ae60; border-radius:50%;"></span> Answered
                    </div>
                    <div style="display:flex; gap:8px; align-items:center; margin-bottom:5px;">
                        <span style="width:12px; height:12px; background:#c0392b; border-radius:50%;"></span> Visited
                    </div>
                    <div style="display:flex; gap:8px; align-items:center;">
                        <span style="width:12px; height:12px; border:1px solid #ccc; border-radius:50%;"></span> Not Visited
                    </div>
                </div>
            </div>
        </aside>
    </div>

    <div class="test-footer">
        <!-- Exit button injected by JS -->
        <div style="flex:1"></div>
        <button class="btn-nav btn-prev" id="btnPrev">Previous</button>
        <button class="btn-nav btn-next" id="btnNext">Next</button>
    </div>

    <div class="result-overlay" id="resultModal">
        <div class="result-card">
            <div class="score-circle">
                <div class="score-text"></div>
            </div>
            <div id="resultMessage"></div>
            <button class="btn-nav btn-submit" onclick="closeResult()" style="margin-top:1.5rem;">Review Answers</button>
            <a href="../index.html" style="display:block; margin-top:1rem; color:#666; text-decoration:none;">Back to Tests</a>
        </div>
    </div>

    <script src="../../../../../assets/js/test-engine.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            fetch('${testType.type}.json')
                .then(response => response.json())
                .then(data => {
                    // Merge config from JSON with page-specific config
                    const config = {
                        ...data,
                        topic: '${chapter.name} - ${testType.label}',
                        timeLimit: ${testType.time},
                        chapterName: '${chapter.name}',
                        chapterUrl: '../index.html',
                        exitUrl: '../index.html'
                    };
                    new TestEngine(config);
                })
                .catch(err => console.error('Error loading test data:', err));

            const toggleBtn = document.getElementById('paletteToggle');
            const navPanel = document.querySelector('.nav-panel');
            if(toggleBtn && navPanel) {
                toggleBtn.addEventListener('click', () => {
                    navPanel.classList.toggle('collapsed');
                    toggleBtn.querySelector('i').style.transform = navPanel.classList.contains('collapsed') ? 'rotate(180deg)' : 'rotate(0deg)';
                });
            }
        });
    </script>
</body>
</html>`;

    const jsonContent = `{
  "questions": [
    {
      "id": 1,
      "type": "mcq",
      "question": "Sample Question for ${chapter.name} (${testType.label}). What is 2 + 2?",
      "options": ["3", "4", "5", "6"],
      "correctAnswer": 1,
      "explanation": "2 + 2 = 4"
    }
  ]
}`; // Minimal valid JSON structure

    const chapterDir = path.join(baseDir, chapter.folder);

    // Create directory if it doesn't exist (though it should)
    if (!fs.existsSync(chapterDir)) {
        fs.mkdirSync(chapterDir, { recursive: true });
    }

    const htmlPath = path.join(chapterDir, `${testType.type}.html`);
    const jsonPath = path.join(chapterDir, `${testType.type}.json`);

    // Only create JSON if it doesn't exist to avoid overwriting existing data
    // For HTML, we might want to overwrite to ensure latest structure, but let's be safe and check
    // Actually, for this task, I'll overwrite HTML to ensure consistency, but skip JSON if it exists and has content > 100 chars (heuristic)

    fs.writeFileSync(htmlPath, htmlContent);
    console.log(`Created ${htmlPath}`);

    if (!fs.existsSync(jsonPath)) {
        fs.writeFileSync(jsonPath, jsonContent);
        console.log(`Created ${jsonPath}`);
    } else {
        const stats = fs.statSync(jsonPath);
        if (stats.size < 50) { // If it's basically empty/invalid
            fs.writeFileSync(jsonPath, jsonContent);
            console.log(`Overwrote empty/small ${jsonPath}`);
        } else {
            console.log(`Skipped existing JSON ${jsonPath}`);
        }
    }
}

chapters.forEach(chapter => {
    testTypes.forEach(testType => {
        createTestFile(chapter, testType);
    });
});
