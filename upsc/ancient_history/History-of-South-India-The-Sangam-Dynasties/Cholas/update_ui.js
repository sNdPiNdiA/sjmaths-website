const fs = require('fs');
const path = require('path');

// 1. Update CSS
const cssPath = 'c:/Users/sande/Documents/GitHub/sjmaths-website/upsc/history-culture-guide.css';
let css = fs.readFileSync(cssPath, 'utf8');
if (!css.includes('.mindmap-container')) {
    css += `\n
/* ==================== MINDMAP COMPONENT ==================== */
.mindmap-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    position: relative;
    margin-top: 1rem;
}
.mindmap-node {
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 1.25rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
.mindmap-node:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    border-color: rgba(212, 175, 55, 0.5);
}
.node-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.15rem;
    font-weight: 700;
    color: var(--primary-pre);
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid rgba(212, 175, 55, 0.2);
}
.node-items {
    list-style-type: none;
    padding-left: 0;
    margin: 0;
}
.node-items li {
    font-size: 0.92rem;
    color: var(--text-dark);
    margin-bottom: 0.5rem;
    position: relative;
    padding-left: 1.2rem;
    line-height: 1.4;
}
.node-items li::before {
    content: "•";
    color: #d4af37;
    position: absolute;
    left: 0;
    font-weight: bold;
    font-size: 1.2rem;
    top: -2px;
}
`;
    fs.writeFileSync(cssPath, css);
}

// 2. Update index.html
const htmlPath = 'c:/Users/sande/Documents/GitHub/sjmaths-website/upsc/ancient_history/History-of-South-India-The-Sangam-Dynasties/Cholas/index.html';
let html = fs.readFileSync(htmlPath, 'utf8');
if (!html.includes('id="mindmap-section"')) {
    html = html.replace(
        '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->',
        '<!-- Mindmap / Snapshot (Dynamically Rendered) -->\n            <div class="card-premium" id="mindmap-section" style="display:none;"></div>\n\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->'
    );
    fs.writeFileSync(htmlPath, html);
}

// 3. Update hi/index.html
const hiHtmlPath = 'c:/Users/sande/Documents/GitHub/sjmaths-website/upsc/ancient_history/History-of-South-India-The-Sangam-Dynasties/Cholas/hi/index.html';
let hiHtml = fs.readFileSync(hiHtmlPath, 'utf8');
if (!hiHtml.includes('id="mindmap-section"')) {
    hiHtml = hiHtml.replace(
        '<!-- Deep-Dive Study Guide (Dynamically Rendered) -->',
        '<!-- Mindmap / Snapshot (Dynamically Rendered) -->\n            <div class="card-premium" id="mindmap-section" style="display:none;"></div>\n\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->'
    );
    fs.writeFileSync(hiHtmlPath, hiHtml);
}

console.log("Successfully updated core UI components.");
