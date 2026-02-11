
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.join(__dirname, '..', 'classes', 'class-11', 'tests');

// Template for the new HTML file
const getHtmlTemplate = (jsonFileName, title, depth) => {
    // Determine relative path to assets based on depth
    // depth 0 = tests/
    // depth 1 = tests/full-length-tests/
    // depth 2 = tests/unit-wise/unit-X/
    //
    // assets is at classes/assets/ (actually root assets/ so ../../../ from classes/class-11/tests)
    //
    // From tests/ (depth 0): ../../../assets/
    // From tests/full-length-tests/ (depth 1): ../../../../assets/
    // From tests/unit-wise/unit-X/ (depth 2): ../../../../../assets/

    let relativeAssetsPath = '../../../assets';
    if (depth === 1) relativeAssetsPath = '../../../../assets';
    if (depth === 2) relativeAssetsPath = '../../../../../assets';

    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} | Class 11 Maths</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="${relativeAssetsPath}/css/test-interface.min.css">
    
    <script>
        window.MathJax = {
            tex: { inlineMath: [['$', '$'], ['\\(', '\\)']] },
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
                <button id="paletteToggle" style="background:none; border:none; color:#2c3e50; cursor:pointer; display:none; font-size:1.1rem; margin-left: auto;">
                    <i class="fas fa-chevron-up"></i>
                </button>
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
        <button class="btn-nav btn-reset" id="btnReset">Reset</button>
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

    <script src="${relativeAssetsPath}/js/test-engine.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            fetch('${jsonFileName}')
                .then(response => response.json())
                .then(data => {
                    data.exitUrl = '../index.html';
                    new TestEngine(data);
                });
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
};

// Function to extract testConfig from HTML content
const extractTestConfig = (htmlContent) => {
    const regex = /const\s+testConfig\s*=\s*({[\s\S]*?});\s*document\.addEventListener/m;
    const match = htmlContent.match(regex);
    if (match && match[1]) {
        try {
            // Need to make the string valid JSON-like to parse it or just eval it (safe in this context since we trust our own files)
            // However, eval is dangerous. Let's try to clean it up or use a VM if needed.
            // But since this is a dev script, let's use a Function constructor for simple parsing if structure is simple JS object.

            // Replaces commented lines which might break Function parsing
            const cleanObjStr = match[1].replace(/\/\/.*$/gm, '');

            const getConfig = new Function(`return ${cleanObjStr};`);
            return getConfig();
        } catch (e) {
            console.error("Error parsing JS object:", e);
            return null;
        }
    }
    return null;
};

// Recursive function to walk directories
const walk = (dir, depth = 0) => {
    const list = fs.readdirSync(dir);
    list.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat && stat.isDirectory()) {
            walk(filePath, depth + 1);
        } else {
            // Process HTML files, skipping those we already converted (check if JSON exists)
            // Also skip non-test HTML files if any
            if (file.endsWith('.html') && file !== 'index.html') {
                const basename = path.basename(file, '.html');
                const jsonPath = path.join(dir, basename + '.json');

                // If json doesn't exist, we might need to migrate
                if (!fs.existsSync(jsonPath)) {
                    const content = fs.readFileSync(filePath, 'utf8');

                    // Check if file contains testConfig
                    if (content.includes('const testConfig = {')) {
                        console.log(`Migrating ${filePath}...`);

                        const config = extractTestConfig(content);
                        if (config) {
                            // 1. Write JSON file
                            // Add headers/subheaders if missing (can infer from filename or existing content)
                            // For simplicity, we keep what's in config.

                            // Adjust heading if missing
                            if (!config.heading) {
                                config.heading = basename.charAt(0).toUpperCase() + basename.slice(1).replace(/-/g, ' ');
                            }
                            if (!config.subHeading) {
                                config.subHeading = "Class 11 Mathematics";
                            }

                            fs.writeFileSync(jsonPath, JSON.stringify(config, null, 2));
                            console.log(`Created ${jsonPath}`);

                            // 2. Overwrite HTML file with template
                            const title = config.heading;
                            const newHtml = getHtmlTemplate(basename + '.json', title, depth);
                            fs.writeFileSync(filePath, newHtml);
                            console.log(`Updated ${filePath}`);
                        } else {
                            console.error(`Failed to extract config from ${filePath}`);
                        }
                    }
                } else {
                    console.log(`Skipping ${file} - JSON already exists.`);
                }
            }
        }
    });
};

console.log('Starting migration...');
walk(ROOT_DIR);
console.log('Migration complete.');
