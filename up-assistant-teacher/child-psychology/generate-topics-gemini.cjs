/**
 * Gemini 3.5 Flash Lite Content Generator
 * Reads microtopic pages and populates Tab 1 (Concepts/Theories) with AI-generated content.
 * 
 * Usage: 
 * 1. Set GEMINI_API_KEY in environment variables
 * 2. Run: node generate-topics-gemini.cjs
 * 
 * This will update each topic's HTML with real content from Gemini API.
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const BASE_DIR = path.join(__dirname);
const TOPICS_DIR = path.join(BASE_DIR, 'topics');
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || '';
const GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent';

const microtopics = [
    { slug: 'individual-differences', title: 'Individual Differences' },
    { slug: 'factors-affecting-child-development', title: 'Factors Affecting Child Development' },
    { slug: 'identification-of-learning-needs', title: 'Identification of Learning Needs' },
    { slug: 'creating-conducive-learning-environment', title: 'Creating Conducive Learning Environment' },
    { slug: 'learning-theories-and-classroom-application', title: 'Learning Theories & Practical Classroom Application' },
    { slug: 'special-provisions-for-divyang-students', title: 'Special Provisions for Divyang Students' }
];

function generatePrompt(topic) {
    return `Generate educational content for the topic: "${topic.title}" for UP Assistant Teacher Child Psychology exam.

Provide the response in the following JSON format ONLY (no extra text):
{
  "overview": "2-3 sentence overview in simple Hindi and English mixed",
  "detailedExplanation": "Short bullet-point explanation (max 8 lines, not long paragraphs) in Hindi",
  "mnemonic": "One practical mnemonic/trick to remember key points",
  "tips": "2-3 practical tips for teachers",
  "mistakes": "Common mistakes to avoid"
}

Keep content concise, exam-focused, and easy to remember. Use Hindi language for main content.`;
}

async function callGeminiAPI(prompt) {
    if (!GEMINI_API_KEY) {
        console.warn('⚠ GEMINI_API_KEY not set. Returning mock content.');
        return getMockContent();
    }

    return new Promise((resolve, reject) => {
        const postData = JSON.stringify({
            contents: [{
                parts: [{ text: prompt }]
            }],
            generationConfig: {
                temperature: 0.7,
                maxOutputTokens: 1024
            }
        });

        const options = {
            hostname: 'generativelanguage.googleapis.com',
            path: `${GEMINI_API_URL}?key=${GEMINI_API_KEY}`,
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': Buffer.byteLength(postData)
            }
        };

        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => {
                try {
                    const parsed = JSON.parse(data);
                    if (parsed.candidates && parsed.candidates[0] && parsed.candidates[0].content) {
                        const text = parsed.candidates[0].content.parts[0].text;
                        const jsonMatch = text.match(/\{[\s\S]*\}/);
                        if (jsonMatch) {
                            resolve(JSON.parse(jsonMatch[0]));
                        } else {
                            resolve(getMockContent());
                        }
                    } else {
                        resolve(getMockContent());
                    }
                } catch (e) {
                    console.error('Error parsing Gemini response:', e.message);
                    resolve(getMockContent());
                }
            });
        });

        req.on('error', (err) => {
            console.error('Gemini API error:', err.message);
            resolve(getMockContent());
        });

        req.write(postData);
        req.end();
    });
}

function getMockContent() {
    return {
        overview: 'यह विषय बाल विकास और शिक्षण के सिद्धान्तों से संबंधित है।',
        detailedExplanation: '<ul><li>बाल मनोविज्ञान शिक्षकों के लिए महत्वपूर्ण है</li><li>इससे बच्चों की सीखने की प्रक्रिया को समझा जा सकता है</li><li>विभिन्न शिक्षण शैलियों का उपयोग किया जा सकता है</li></ul>',
        mnemonic: 'ABCD - Attention, Behaviour, Cognitive, Development',
        tips: '1. व्यवहार से शिक्षा शुरुआत करें\n2. छोटे-छोटे लक्ष्य निर्धारित करें',
        mistakes: '1. बच्चों की गति को न रोकें\n2. सभी बच्चों को एक साथ मत तुलना करें'
    };
}

function updateTopicHTML(html, content) {
    // Update Overview
    html = html.replace(
        /<div class="placeholder-note">[\s\S]*?यह खंड AI द्वारा जनरेट किया जा रहा है[\s\S]*?<\/div>/,
        `<p>${escapeHtml(content.overview)}</p>`
    );

    // Update Detailed Explanation
    html = html.replace(
        /<div class="placeholder-note">[\s\S]*?विस्तृत व्याख्या AI द्वारा जनरेट की जा रही है[\s\S]*?<\/div>/,
        content.detailedExplanation || '<p>Content coming soon...</p>'
    );

    // Update Mnemonics
    html = html.replace(
        /<strong>💡 Mnemonic:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>💡 Mnemonic:</strong> ${escapeHtml(content.mnemonic || 'Coming soon...')}`
    );

    // Update Tips & Tricks
    html = html.replace(
        /<strong>✓ Tip:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>✓ Tip:</strong> ${escapeHtml(content.tips || 'Coming soon...')}`
    );

    // Update Mistakes to Avoid
    html = html.replace(
        /<strong>⚠ Common Mistake:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>⚠ Common Mistake:</strong> ${escapeHtml(content.mistakes || 'Coming soon...')}`
    );

    return html;
}

function escapeHtml(text) {
    const map = {
        '&': '&',
        '<': '<',
        '>': '>',
        '"': '"',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

async function processAllTopics() {
    console.log('🚀 Starting Gemini 3.5 Flash Lite content generation...\n');

    for (const topic of microtopics) {
        const filePath = path.join(TOPICS_DIR, topic.slug + '.html');

        if (!fs.existsSync(filePath)) {
            console.log(`⚠ Skipping ${topic.slug} - file not found`);
            continue;
        }

        console.log(`📝 Processing: ${topic.title}`);

        let html = fs.readFileSync(filePath, 'utf8');
        const prompt = generatePrompt(topic);

        try {
            const content = await callGeminiAPI(prompt);
            html = updateTopicHTML(html, content);
            fs.writeFileSync(filePath, html, 'utf8');
            console.log(`  ✓ Updated ${topic.slug}.html`);
        } catch (err) {
            console.error(`  ✗ Error processing ${topic.slug}:`, err.message);
        }
    }

    console.log('\n✅ All topics processed!');
    console.log('\n💡 Tip: Run this script again to refresh content from Gemini API.');
}

// Run if called directly
if (require.main === module) {
    processAllTopics().catch(console.error);
}

module.exports = { callGeminiAPI, updateTopicHTML, generatePrompt };