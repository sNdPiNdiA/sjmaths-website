import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';
import { GoogleGenAI, Type } from '@google/genai';
import dotenv from 'dotenv';

dotenv.config();

const ai = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY
});

const responseSchema = {
    type: Type.OBJECT,
    properties: {
        hero: {
            type: Type.OBJECT,
            properties: {
                title: { type: Type.STRING },
                description: { type: Type.STRING }
            }
        },
        mindmap: {
            type: Type.OBJECT,
            properties: {
                title: { type: Type.STRING },
                description: { type: Type.STRING },
                nodes: {
                    type: Type.ARRAY,
                    items: {
                        type: Type.OBJECT,
                        properties: {
                            title: { type: Type.STRING },
                            icon: { type: Type.STRING, description: "FontAwesome class e.g. fa-book" },
                            items: { type: Type.ARRAY, items: { type: Type.STRING } }
                        }
                    }
                }
            }
        },
        deepDive: {
            type: Type.OBJECT,
            properties: {
                title: { type: Type.STRING },
                description: { type: Type.STRING },
                sections: {
                    type: Type.ARRAY,
                    items: {
                        type: Type.OBJECT,
                        properties: {
                            title: { type: Type.STRING },
                            content: { type: Type.STRING, description: "HTML formatted content string" },
                            masteryZone: {
                                type: Type.ARRAY,
                                items: {
                                    type: Type.OBJECT,
                                    properties: {
                                        type: { type: Type.STRING, enum: ["MCQ", "True/False"] },
                                        q: { type: Type.STRING },
                                        opts: { type: Type.ARRAY, items: { type: Type.STRING } },
                                        ans: { type: Type.INTEGER },
                                        sol: { type: Type.STRING }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        flashcards: {
            type: Type.OBJECT,
            properties: {
                title: { type: Type.STRING },
                description: { type: Type.STRING },
                items: {
                    type: Type.ARRAY,
                    items: {
                        type: Type.OBJECT,
                        properties: {
                            front: { type: Type.STRING },
                            back: { type: Type.STRING },
                            icon: { type: Type.STRING }
                        }
                    }
                }
            }
        }
    }
};

async function generateNotes(filePath) {
    console.log(`Processing: ${filePath}`);
    const html = fs.readFileSync(filePath, 'utf8');
    const $ = cheerio.load(html);
    
    const title = $('title').text().split('-')[0].trim();
    console.log(`Extracting notes for topic: ${title}`);

    const isHindi = filePath.includes('/hi/') || filePath.includes('\\hi\\');
    const languageInstruction = isHindi ? "IMPORTANT: ALL text, explanations, questions, and flashcards MUST be written entirely in HINDI." : "";

    const prompt = `
    You are an expert educator creating high-quality study materials for competitive exams (UPSC, SSC CGL).
    Create comprehensive study notes for the topic: "${title}".
    ${languageInstruction}
    Return a detailed JSON object matching the requested schema.
    Include 3-4 deep dive sections with detailed HTML formatted content.
    Include 1-2 mastery questions per section.
    Include a mindmap and 5 flashcards.
    `;

    if (process.argv.includes('--dummy')) {
        console.log('Generating DUMMY notes (bypassing AI)...');
        const dummyData = {
            hero: { title: title, description: "Detailed study notes and analysis for " + title },
            deepDive: {
                title: "Comprehensive Notes",
                description: "Deep dive into " + title,
                sections: [{
                    title: "Introduction",
                    content: "<p>This is a placeholder for the actual notes about " + title + ".</p>",
                    masteryZone: [{
                        type: "MCQ", q: "What is this topic about?", opts: [title, "Other", "None", "All"], ans: 0, sol: "It is about " + title
                    }]
                }]
            },
            flashcards: {
                title: "Quick Review",
                description: "Flashcards for " + title,
                items: [{ front: "Topic", back: title, icon: "fa-star" }]
            }
        };
        
        const scriptTag = `\n<script type="application/json" id="embedded-study-guide-data">\n${JSON.stringify(dummyData, null, 2)}\n</script>\n`;
        if (html.includes('id="embedded-study-guide-data"')) {
             console.log('File already contains embedded data, skipping.');
             return;
        }
        const updatedHtml = html.replace('</body>', `${scriptTag}</body>`);
        fs.writeFileSync(filePath, updatedHtml, 'utf8');
        console.log(`Successfully updated with DUMMY data: ${filePath}`);
        return;
    }

    try {
        const response = await ai.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: prompt,
            config: {
                responseMimeType: 'application/json',
                responseSchema: responseSchema
            }
        });

        const jsonStr = response.text;
        const data = JSON.parse(jsonStr);

        // Inject into HTML
        const scriptTag = `\n<script type="application/json" id="embedded-study-guide-data">\n${JSON.stringify(data, null, 2)}\n</script>\n`;
        
        // Find where to insert (before </body>)
        if (html.includes('id="embedded-study-guide-data"')) {
            console.log('File already contains embedded data, skipping.');
            return;
        }

        const updatedHtml = html.replace('</body>', `${scriptTag}</body>`);
        fs.writeFileSync(filePath, updatedHtml, 'utf8');
        console.log(`Successfully updated: ${filePath}`);
    } catch (err) {
        console.error('Failed to generate notes:', err);
    }
}
function processDirectory(dirPath) {
    const files = fs.readdirSync(dirPath);
    for (const file of files) {
        const fullPath = path.join(dirPath, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            processDirectory(fullPath);
        } else if (stat.isFile() && file === 'index.html') {
            // Generate notes sequentially to avoid rate limits
            generateNotes(fullPath).catch(err => console.error(err));
            // Wait a few seconds between calls to respect rate limits? 
            // We'll just let them queue up or run, wait, we should await them in a loop.
        }
    }
}

async function processAll(inputPath) {
    const stat = fs.statSync(inputPath);
    if (stat.isDirectory()) {
        console.log(`Scanning directory: ${inputPath}`);
        const htmlFiles = [];
        function findHtml(dir) {
            const items = fs.readdirSync(dir);
            for (const item of items) {
                const fullPath = path.join(dir, item);
                const itemStat = fs.statSync(fullPath);
                if (itemStat.isDirectory()) {
                    findHtml(fullPath);
                } else if (itemStat.isFile() && item === 'index.html') {
                    htmlFiles.push(fullPath);
                }
            }
        }
        findHtml(inputPath);
        console.log(`Found ${htmlFiles.length} topics to process.`);
        for (const file of htmlFiles) {
            await generateNotes(file);
            // Add a small delay to avoid hitting API rate limits (15 RPM is common for free tier)
            await new Promise(resolve => setTimeout(resolve, 4000));
        }
    } else {
        await generateNotes(inputPath);
    }
}

const args = process.argv.slice(2);
if (args.length === 0) {
    console.error('Please provide a file path to process.');
    process.exit(1);
}

processAll(args[0]).then(() => console.log('All processing complete.'));
