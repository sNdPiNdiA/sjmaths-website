const fs = require('fs');
const path = require('path');

const classesDirs = [
    'classes/class-9/ncert-exercise-practice',
    'classes/class-10/ncert-exercise-practice',
    'classes/class-11/ncert-exercise-practice',
    'classes/class-11/chapter-wise-notes',
    'classes/class-12/ncert-exercise-practice',
    'classes/class-12/chapter-wise-notes'
];

// Preconnect tags to add
const PRECONNECT_TAGS = `
    <!-- Performance Optimization: Preconnects -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="preconnect" href="https://cdn.jsdelivr.net">
`;

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let originalContent = content;

    // 1. Inject Preconnects
    if (!content.includes('rel="preconnect" href="https://fonts.googleapis.com"')) {
        // Find the Google Fonts link
        const fontLinkRegex = /<link\s+href="https:\/\/fonts\.googleapis\.com[^>]+>/;
        if (fontLinkRegex.test(content)) {
            content = content.replace(fontLinkRegex, match => PRECONNECT_TAGS.trim() + '\n    ' + match);
        }
    }

    // 2. Switch MathJax to Defer
    // Look for: <script id="MathJax-script" async src="...">
    // Replace with: <script id="MathJax-script" defer src="...">
    const mathJaxRegex = /<script id="MathJax-script" async src="([^"]+)"><\/script>/;
    if (mathJaxRegex.test(content)) {
        content = content.replace(mathJaxRegex, '<script id="MathJax-script" defer src="$1"></script>');
    }

    // 3. Image Lazy Loading
    // Simple regex to add loading="lazy" if not present
    // We avoid the Hero image if possible, but these are exercise pages which usually don't have a hero IMG, just CSS background.
    // The images inside are likely question images or solution steps.

    // Find img tags that DON'T have loading attribute
    // Note: This is a basic regex, might need refinement for complex tags
    const imgRegex = /<img\s+(?![^>]*\bloading=)[^>]*>/gi;
    content = content.replace(imgRegex, (match) => {
        // Insert loading="lazy" after "<img "
        return match.replace('<img ', '<img loading="lazy" ');
    });

    if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Optimized: ${filePath}`);
        return true;
    }
    return false;
}

function traverseDir(dir) {
    if (!fs.existsSync(dir)) return;

    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
            traverseDir(fullPath);
        } else if (file.endsWith('.html')) {
            processFile(fullPath);
        }
    });
}

console.log('Starting Performance Optimization...');
classesDirs.forEach(dir => {
    const fullDir = path.join(__dirname, '..', dir);
    console.log(`Processing ${fullDir}...`);
    traverseDir(fullDir);
});
console.log('Optimization Complete.');
