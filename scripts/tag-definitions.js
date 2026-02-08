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

async function tagDefinitions() {
    console.log('Starting Definition Tagging...');
    const allFiles = await getFiles(CLASSES_DIR);
    const htmlFiles = allFiles.filter(f => f.endsWith('.html') && f.includes('notes')); // Primarily for notes

    let definitionsFound = 0;

    for (const file of htmlFiles) {
        let content = await readFile(file, 'utf8');
        let modified = false;

        // Pattern: <strong>Term:</strong> or <b>Term</b>:
        // We want to capture "Term" and the definition following it.
        // Simple heuristic: Look for <p><strong>Term:</strong> Definition.</p>

        const defRegex = /<p>\s*<strong>(.*?):<\/strong>\s*(.*?)<\/p>/gi;
        let match;
        const definedTerms = [];

        while ((match = defRegex.exec(content)) !== null) {
            const term = match[1].trim();
            const definition = match[2].trim();

            if (term.length < 50 && definition.length > 10) {
                definedTerms.push({ term, definition });
            }
        }

        if (definedTerms.length > 0) {
            // console.log(`Found ${definedTerms.length} definitions in ${path.basename(file)}`);
            definitionsFound += definedTerms.length;

            // Generate Schema
            // Don't inject if DefinedTerm already exists
            if (!content.includes('"@type": "DefinedTerm"')) {
                const schema = {
                    "@context": "https://schema.org",
                    "@type": "DefinedTermSet",
                    "name": "Key Concepts",
                    "hasDefinedTerm": definedTerms.map(dt => ({
                        "@type": "DefinedTerm",
                        "name": dt.term,
                        "description": dt.definition.replace(/<[^>]*>/g, '') // Strip tags from def
                    }))
                };

                const jsonLd = `
    <!-- Structured Data: DefinedTermSet (AI Generated) -->
    <script type="application/ld+json">
    ${JSON.stringify(schema, null, 2)}
    </script>
`;
                if (content.includes('</head>')) {
                    content = content.replace('</head>', `${jsonLd}\n</head>`);
                    modified = true;
                }
            }
        }

        if (modified) {
            await writeFile(file, content, 'utf8');
        }
    }
    console.log(`Definition Tagging Complete. Definitions Schema Added for ${definitionsFound} terms.`);
}

tagDefinitions().catch(console.error);
