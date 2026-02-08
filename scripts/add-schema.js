const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');

async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = path.resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.flat();
}

function cleanText(text) {
    if (!text) return '';
    return text.replace(/<[^>]*>/g, ' ') // Remove tags
        .replace(/\s+/g, ' ')     // Normalize whitespace
        .replace(/&nbsp;/g, ' ')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&amp;/g, '&')
        .trim();
}

async function addSchema() {
    console.log('Starting Schema Injection...');
    const allFiles = await getFiles(CLASSES_DIR);
    const exerciseFiles = allFiles.filter(f => f.includes('exercise-') && f.endsWith('.html'));

    console.log(`Found ${exerciseFiles.length} Exercise Files.`);

    let updatedCount = 0;
    let skippedCount = 0;

    for (const file of exerciseFiles) {
        let content = await readFile(file, 'utf8');

        // 1. Check existing Schema
        if (content.includes('"@type": "QAPage"') || content.includes('"@type":"QAPage"')) {
            // console.log(`Skipping (Existing Schema): ${path.basename(file)}`);
            skippedCount++;
            continue;
        }

        // 2. Parse Questions and Answers
        // Structure: 
        // <section id="q1" ...> <h2>Question 1</h2> ... <div class="solution"> ... </div> </section>

        const sectionRegex = /<section id="q\d+"[^>]*>([\s\S]*?)<\/section>/gi;
        let match;
        const questions = [];

        while ((match = sectionRegex.exec(content)) !== null) {
            const sectionContent = match[1];

            // Extract Question Text (everything before <button class="solution-btn"> or <div class="solution">)
            // Usually between <h2>Question X</h2> and <button...

            const qTextMatch = sectionContent.match(/<h2>Question \d+<\/h2>([\s\S]*?)(<button|<div class="solution")/i);
            const rawQText = qTextMatch ? qTextMatch[1] : '';
            const cleanQText = cleanText(rawQText);

            // Extract Answer Text
            const aTextMatch = sectionContent.match(/<div class="solution">([\s\S]*?)<\/div>/i);
            const rawAText = aTextMatch ? aTextMatch[1] : '';
            const cleanAText = cleanText(rawAText);

            if (cleanQText && cleanAText) {
                questions.push({
                    q: cleanQText,
                    a: cleanAText
                });
            }
        }

        if (questions.length === 0) {
            // console.log(`Skipping (No Q&A found): ${path.basename(file)}`);
            continue;
        }

        // 3. Construct JSON-LD
        const schema = {
            "@context": "https://schema.org",
            "@type": "QAPage",
            "mainEntity": questions.map((item, index) => ({
                "@type": "Question",
                "name": `Question ${index + 1}`,
                "text": item.q.substring(0, 150) + (item.q.length > 150 ? '...' : ''),
                "answerCount": 1,
                "upvoteCount": 0,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": item.a.substring(0, 300) + (item.a.length > 300 ? '...' : ''), // Truncate for schema to avoid bloating
                    "upvoteCount": 0,
                    "url": `https://www.sjmaths.com/classes/${path.relative(CLASSES_DIR, file).replace(/\\/g, '/')}#q${index + 1}`
                }
            }))
        };

        const jsonLdBlock = `
  <!-- Structured Data: QAPage (AI Generated) -->
  <script type="application/ld+json">
${JSON.stringify(schema, null, 2)}
  </script>
`;

        // 4. Inject
        if (content.includes('</head>')) {
            content = content.replace('</head>', `${jsonLdBlock}\n</head>`);
            await writeFile(file, content, 'utf8');
            // console.log(`Updated: ${path.basename(file)} with ${questions.length} questions`);
            updatedCount++;
        }
    }

    console.log(`Schema Injection Complete. Updated: ${updatedCount}, Skipped/No-Match: ${skippedCount}`);
}

addSchema().catch(console.error);
