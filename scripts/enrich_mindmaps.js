import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';

dotenv.config();
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
if (!GEMINI_API_KEY) {
    console.error('No GEMINI_API_KEY found in .env');
    process.exit(1);
}

const listPath = path.resolve('C:\\Users\\sande\\.gemini\\antigravity-ide\\brain\\4b598b8c-9247-48f0-8588-7745331b8e9a\\thin_content_pages.md');
const listContent = fs.readFileSync(listPath, 'utf8');

const lines = listContent.split('\n');
const targetFiles = [];

for (const line of lines) {
    const match = line.match(/\|\s*(\d+)\s*\|\s*\`([^\`]+)\`/);
    if (match) {
        const wc = parseInt(match[1]);
        if (wc < 300) {
            targetFiles.push(match[2]);
        }
    }
}

console.log(`Found ${targetFiles.length} files to process.`);

function jsonToNoscriptHtml(node) {
    let html = `<li><strong>${node.label.replace(/\n/g, ' ')}</strong>`;
    if (node.date) {
        html += ` (${node.date})`;
    }
    if (node.children && node.children.length > 0) {
        html += '\n<ul>\n';
        for (const child of node.children) {
            html += jsonToNoscriptHtml(child) + '\n';
        }
        html += '</ul>\n';
    }
    html += '</li>';
    return html;
}

async function generateMindmapForTopic(topic) {
    const prompt = `You are a UPSC expert. Generate a highly comprehensive study mindmap for the topic: "${topic}". \n\nOutput ONLY a raw, valid JSON object (no markdown formatting, no backticks, just the JSON). The JSON must exactly match this schema:\n{\n  "label": "Main Topic Name",\n  "type": "root",\n  "children": [\n    {\n      "label": "Major Category 1",\n      "type": "branch",\n      "date": "Short subtitle (optional)",\n      "children": [\n        {\n           "label": "Sub-category or detailed fact",\n           "type": "leaf"\n        },\n        {\n           "label": "Another sub-category",\n           "type": "sub",\n           "date": "optional",\n           "children": [ {"label": "Deep detail", "type": "leaf"} ]\n        }\n      ]\n    }\n  ]\n}\n\nEnsure there are at least 4 main branches, and each branch has several children. Keep labels concise but highly informative for a UPSC aspirant.`;

    let retries = 3;
    while (retries > 0) {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemma-4-31b-it:generateContent?key=${GEMINI_API_KEY}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: prompt }] }],
                generationConfig: { temperature: 0.2 }
            })
        });
        
        if (!response.ok) {
            const errText = await response.text();
            if (response.status === 429) {
                if (errText.includes('Quota exceeded') || errText.includes('RESOURCE_EXHAUSTED')) {
                    console.error('DAILY QUOTA EXCEEDED! Exiting.');
                    process.exit(1);
                }
                console.warn(`Rate limited. Waiting 10s...`);
                await new Promise(r => setTimeout(r, 10000));
                retries--;
                continue;
            }
            throw new Error(`API Error: ${response.status} ${response.statusText} - ${errText}`);
        }
        
        const data = await response.json();
        let text = data.candidates[0].content.parts[0].text;
        const firstBrace = text.indexOf('{');
        const lastBrace = text.lastIndexOf('}');
        if (firstBrace !== -1 && lastBrace !== -1) {
            text = text.substring(firstBrace, lastBrace + 1);
        }
        return JSON.parse(text);
    }
    throw new Error('Max retries reached due to 429 Too Many Requests');
}

function countWordsInHtml(html) {
    let text = html.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, ' ');
    text = text.replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, ' ');
    text = text.replace(/<[^>]+>/g, ' ');
    text = text.replace(/\s+/g, ' ').trim();
    return text.split(' ').filter(word => word.length > 1).length;
}

async function processFile(relPath) {
    const absPath = path.resolve(relPath);
    let html = fs.readFileSync(absPath, 'utf8');
    
    // Check if it's already over 300 words (i.e. successfully enriched today)
    if (countWordsInHtml(html) > 300) {
        console.log(`Skipping ${relPath} - already > 300 words`);
        return false;
    }
    
    // Strip old mindmaps to ensure fresh Gemini generation
    if (html.includes('mindmap-engine.min.js')) {
        html = html.replace(/<!-- Interactive Mindmap -->[\s\S]*?(?=<!-- Mnemonics|<!-- Evolution|<!-- UPSC Warning|<!-- Tab Navigation)/, '');
        html = html.replace(/<!-- Interactive Mindmap -->[\s\S]*?renderMindmap[\s\S]*?<\/script>/, '');
        console.log(`Stripped old tiny mindmap from ${relPath}`);
    }
    
    const titleMatch = html.match(/<title>([^<]+)<\/title>/);
    if (!titleMatch) return false;
    const topic = titleMatch[1].split(' - ')[0].trim();
    
    console.log(`Processing: ${topic}`);
    
    try {
        const mindmapData = await generateMindmapForTopic(topic);
        
        // 1. Inject CSS
        if (!html.includes('mindmap.min.css')) {
            html = html.replace(
                /<link rel="stylesheet" href="\/assets\/css\/competitive-exam-guide\.min\.css[^"]*">/,
                `$&\n    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=859b1f14">`
            );
        }
        
        // 2. Inject Mindmap UI
        const uiHtml = `
            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> ${topic} &mdash; Interactive Mindmap</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.
                </p>
                <div id="prehistory-mindmap-container">
    <noscript class="noscript-mindmap">
      <p>This is a static text representation of the interactive mindmap. Detailed nodes and hierarchy:</p>
      <ul>
        ${jsonToNoscriptHtml(mindmapData)}
      </ul>
    </noscript>
</div>
            </div>
`;
        
        // Insert after Timeline Framework
        const timelineRegex = /(<div class="interactive-timeline"><\/div>\s*<\/div>)/;
        if (timelineRegex.test(html)) {
            html = html.replace(timelineRegex, `$1\n${uiHtml}`);
        } else {
            // Fallback: insert before Mnemonics or Tabs Navigation
            const fallbackRegex = /(<!-- Mnemonics & Memory Hacks \(Dynamically Rendered\) -->|<!-- Tab Navigation Button -->)/;
            html = html.replace(fallbackRegex, `${uiHtml}\n            $1`);
        }
        
        // 3. Inject JS
        const jsHtml = `
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=ea088f0d"></script>
    <script>
    renderMindmap(${JSON.stringify(mindmapData)}, undefined, 'en');
    </script>
`;
        html = html.replace(/<\/body>/, `${jsHtml}\n</body>`);
        
        fs.writeFileSync(absPath, html, 'utf8');
        console.log(`Success: ${topic}`);
        return true;
    } catch (e) {
        console.error(`Error processing ${topic}:`, e.message);
        return true;
    }
}

async function main() {
    for (let i = 0; i < targetFiles.length; i++) {
        const didApiCall = await processFile(targetFiles[i]);
        console.log(`Completed ${i + 1} / ${targetFiles.length}`);
        if (didApiCall) {
            await new Promise(r => setTimeout(r, 4500)); // sleep 4.5s to stay under 15 RPM
        }
    }
}

main();
