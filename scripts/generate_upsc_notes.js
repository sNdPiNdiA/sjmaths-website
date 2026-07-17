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

async function generateNotesForTopic(topicName, filePath) {
    console.log(`\nGenerating notes for: ${topicName}`);

    const prompt = `
    You are an expert UPSC educator. Generate concise but comprehensive study notes for the topic: "${topicName}".
    
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
            model: 'gemini-3-flash',
            contents: prompt,
            config: {
                temperature: 0.3,
                maxOutputTokens: 2000
            }
        });

        const notesContent = response.text;

        // Create output directory
        const outputDir = path.join(__dirname, '..', 'generated-notes', 'Historical-Background-Making-of-Constitution');
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        // Sanitize filename
        const safeFileName = topicName.replace(/[^a-z0-9]/gi, '-').toLowerCase();
        const outputPath = path.join(outputDir, `${safeFileName}.html`);

        // Create HTML file
        const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${topicName} - Study Notes</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f8f9fa;
            line-height: 1.6;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            text-align: center;
        }
        .header h1 {
            margin: 0;
            font-size: 2rem;
        }
        .notes-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h3 {
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
            margin-top: 30px;
        }
        ul {
            margin: 10px 0;
        }
        li {
            margin: 8px 0;
        }
        strong {
            color: #764ba2;
        }
        .timestamp {
            text-align: center;
            color: #666;
            font-size: 0.9rem;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>${topicName}</h1>
        <p>UPSC Study Notes - Brief and Comprehensive</p>
    </div>
    <div class="notes-container">
        ${notesContent}
    </div>
    <div class="timestamp">
        Generated on ${new Date().toLocaleDateString('en-IN')} | For UPSC Civil Services Exam
    </div>
</body>
</html>`;

        fs.writeFileSync(outputPath, htmlContent, 'utf8');
        console.log(`✓ Saved: ${outputPath}`);

    } catch (error) {
        console.error(`✗ Failed to generate notes for ${topicName}:`, error.message);
    }
}

async function processDirectory(dirPath, parentName = '') {
    const items = fs.readdirSync(dirPath);

    for (const item of items) {
        const fullPath = path.join(dirPath, item);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            // Recursively process subdirectories
            await processDirectory(fullPath, item);
        } else if (item === 'index.html') {
            // Generate notes for this topic
            const topicName = path.basename(dirPath).replace(/-/g, ' ');
            await generateNotesForTopic(topicName, fullPath);

            // Wait 5 seconds between requests to respect rate limits
            await new Promise(resolve => setTimeout(resolve, 5000));
        }
    }
}

// Main execution
const targetDir = process.argv[2];
if (!targetDir) {
    console.error('Please provide a directory path to process.');
    console.log('Usage: node scripts/generate_upsc_notes.js <directory-path>');
    process.exit(1);
}

const fullPath = path.resolve(__dirname, '..', targetDir);
if (!fs.existsSync(fullPath)) {
    console.error(`Directory not found: ${fullPath}`);
    process.exit(1);
}

console.log('Starting UPSC Notes Generation using Gemini 2.5 Flash...');
console.log(`Target Directory: ${fullPath}`);

processDirectory(fullPath)
    .then(() => {
        console.log('\n✅ All notes generated successfully!');
        console.log('Notes saved to: generated-notes/Historical-Background-Making-of-Constitution/');
    })
    .catch(err => {
        console.error('\n❌ Error:', err);
    });