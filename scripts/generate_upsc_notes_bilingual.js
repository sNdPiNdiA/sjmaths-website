import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { GoogleGenAI } from '@google/genai';
import dotenv from 'dotenv';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const ai = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY
});

let requestCount = 0;
const MODEL_SWITCH_THRESHOLD = 15;
const PRIMARY_MODEL = 'gemini-3.1-flash-lite';
const SECONDARY_MODEL = 'gemini-3.1-flash-lite';

function getModel() {
    if (requestCount < MODEL_SWITCH_THRESHOLD) {
        return PRIMARY_MODEL;
    }
    return SECONDARY_MODEL;
}

async function generateNotesForTopic(topicName, filePath, language) {
    const langLabel = language === 'hi' ? 'HINDI' : 'ENGLISH';
    const model = getModel();
    console.log(`\nGenerating ${langLabel} notes for: ${topicName} (using ${model})`);

    const languageInstruction = language === 'hi'
        ? 'IMPORTANT: Write ALL content in HINDI language only. Use Devanagari script.'
        : 'Write in ENGLISH language only.';

    const prompt = `
    You are an expert UPSC educator. Generate concise but comprehensive study notes for the topic: "${topicName}".
    
    ${languageInstruction}
    
    REQUIREMENTS:
    1. Keep notes BRIEF but cover EVERY important point related to this microtopic
    2. Use bullet points and short paragraphs for easy revision
    3. Focus on facts, dates, provisions, and key concepts
    4. Make it suitable for UPSC Prelims and Mains preparation
    5. Do NOT add any introductory or concluding remarks
    6. Return ONLY the notes content in HTML format
    
    FORMAT:
    - Use <h3> for main subheadings
    - Use <ul><li> for bullet points
    - Use <p> for short explanatory paragraphs
    - Use <strong> for important terms/dates
    - Keep it clean and structured
    
    Generate the notes now:
    `;

    try {
        const response = await ai.models.generateContent({
            model: model,
            contents: prompt,
            config: {
                temperature: 0.3,
                maxOutputTokens: 2000
            }
        });

        const notesContent = response.text;
        requestCount++;

        // Inject notes into the microtopic's index.html
        const topicDir = path.join(__dirname, '..', 'upsc', 'polity', 'Historical-Background-Making-of-Constitution');
        const safeDirName = topicName.replace(/[^a-z0-9]/gi, '-').replace(/-+/g, '-');

        // Find the matching directory
        const dirs = fs.readdirSync(topicDir).filter(d => {
            const dirPath = path.join(topicDir, d);
            return fs.statSync(dirPath).isDirectory() &&
                d.replace(/-/g, ' ').toLowerCase() === topicName.toLowerCase();
        });

        if (dirs.length === 0) {
            console.error(`✗ Directory not found for topic: ${topicName}`);
            return;
        }

        const microtopicDir = path.join(topicDir, dirs[0]);
        const indexHtmlPath = path.join(microtopicDir, 'index.html');

        if (!fs.existsSync(indexHtmlPath)) {
            console.error(`✗ index.html not found in: ${microtopicDir}`);
            return;
        }

        let htmlContent = fs.readFileSync(indexHtmlPath, 'utf8');

        if (language === 'hi') {
            // Inject Hindi notes into .lang-hi section
            const langHiMatch = htmlContent.match(/<div class="lang-hi[^"]*">/);
            if (langHiMatch) {
                // Find the closing </div> of lang-hi section (before </div></div>)
                const startIndex = htmlContent.indexOf('</div>\n</div>', langHiMatch.index);
                if (startIndex !== -1) {
                    const newContent = htmlContent.substring(0, startIndex) +
                        `\n            <!-- DEEP-DIVE STUDY GUIDE START -->\n` +
                        notesContent +
                        `\n            <!-- DEEP-DIVE STUDY GUIDE END -->\n` +
                        htmlContent.substring(startIndex);
                    fs.writeFileSync(indexHtmlPath, newContent, 'utf8');
                    console.log(`✓ Injected HINDI notes into: ${indexHtmlPath}`);
                } else {
                    console.error(`✗ Could not find closing pattern in Hindi section for: ${topicName}`);
                }
            } else {
                console.error(`✗ Could not find .lang-hi section in: ${topicName}`);
            }
        } else {
            // Inject English notes into .lang-en section  
            const langEnMatch = htmlContent.match(/<div class="lang-en">/);
            if (langEnMatch) {
                // Find the closing </div> of lang-en section (before the lang-hi div)
                const startIndex = htmlContent.indexOf('</div>\n\n        </div>', langEnMatch.index);
                if (startIndex === -1) {
                    // Try alternate pattern: </div> followed by newlines and then </div>
                    const startIndex2 = htmlContent.indexOf('</div>\n        </div>', langEnMatch.index);
                    if (startIndex2 !== -1) {
                        const newContent = htmlContent.substring(0, startIndex2) +
                            `\n            <!-- DEEP-DIVE STUDY GUIDE START -->\n` +
                            notesContent +
                            `\n            <!-- DEEP-DIVE STUDY GUIDE END -->\n` +
                            htmlContent.substring(startIndex2);
                        fs.writeFileSync(indexHtmlPath, newContent, 'utf8');
                        console.log(`✓ Injected ENGLISH notes into: ${indexHtmlPath}`);
                    } else {
                        console.error(`✗ Could not find closing pattern for English section: ${topicName}`);
                    }
                } else {
                    const newContent = htmlContent.substring(0, startIndex) +
                        `\n            <!-- DEEP-DIVE STUDY GUIDE START -->\n` +
                        notesContent +
                        `\n            <!-- DEEP-DIVE STUDY GUIDE END -->\n` +
                        htmlContent.substring(startIndex);
                    fs.writeFileSync(indexHtmlPath, newContent, 'utf8');
                    console.log(`✓ Injected ENGLISH notes into: ${indexHtmlPath}`);
                }
            } else {
                console.error(`✗ Could not find .lang-en section in: ${topicName}`);
            }
        }

    } catch (error) {
        console.error(`✗ Failed to generate ${langLabel} notes for ${topicName}:`, error.message);
    }
}

async function processDirectory(dirPath) {
    const items = fs.readdirSync(dirPath);

    for (const item of items) {
        const fullPath = path.join(dirPath, item);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            await processDirectory(fullPath);
        } else if (item === 'index.html') {
            const topicName = path.basename(dirPath).replace(/-/g, ' ');

            await generateNotesForTopic(topicName, fullPath, 'en');
            await new Promise(resolve => setTimeout(resolve, 5000));

            await generateNotesForTopic(topicName, fullPath, 'hi');
            await new Promise(resolve => setTimeout(resolve, 5000));
        }
    }
}

const targetDir = process.argv[2];
if (!targetDir) {
    console.error('Please provide a directory path to process.');
    console.log('Usage: node scripts/generate_upsc_notes_bilingual.js <directory-path>');
    process.exit(1);
}

const fullPath = path.resolve(__dirname, '..', targetDir);
if (!fs.existsSync(fullPath)) {
    console.error(`Directory not found: ${fullPath}`);
    process.exit(1);
}

console.log('Starting BILINGUAL UPSC Notes Generation...');
console.log(`Target Directory: ${fullPath}`);
console.log(`Model Strategy: ${PRIMARY_MODEL} for first ${MODEL_SWITCH_THRESHOLD} requests, then ${SECONDARY_MODEL}\n`);

processDirectory(fullPath)
    .then(() => {
        console.log('\n✅ All notes generated successfully!');
        console.log('Notes saved to: generated-notes-bilingual/Historical-Background-Making-of-Constitution/');
        console.log('  - english/  (English notes)');
        console.log('  - hindi/    (Hindi notes)');
    })
    .catch(err => {
        console.error('\n❌ Error:', err);
    });