const fs = require('fs');
const path = require('path');

const baseDirs = [
    'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/quantitative-aptitude',
    'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/statistics'
];

function processFile(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let original = content;

    // We want to replace "15 SEO-Friendly FAQs" or similar SEO texts with "Frequently Asked Questions" / "अक्सर पूछे जाने वाले प्रश्न"
    // Let's look for headings like:
    // <h[23]><span class="lang-en">15 SEO-Friendly FAQs</span><span class="lang-hi">...</span></h[23]>
    // Or just clean up the word "SEO-Friendly" or "SEO-friendly" or "एसईओ-अनुकूल" or "SEO-अनुकूल" to just "Frequently Asked Questions" / "अक्सर पूछे जाने वाले प्रश्न"
    
    // Pattern matches:
    // 15 SEO-Friendly FAQs -> Frequently Asked Questions
    // 15 SEO-friendly FAQs -> Frequently Asked Questions
    // 15 एसईओ-अनुकूल अक्सर पूछे जाने वाले प्रश्न -> अक्सर पूछे जाने वाले प्रश्न
    // 15 SEO-अनुकूल अक्सर पूछे जाने वाले प्रश्न -> अक्सर पूछे जाने वाले प्रश्न
    // 15 एसईओ-अनुकूल एफएक्यू -> अक्सर पूछे जाने वाले प्रश्न
    // 15 SEO-अनुकूल प्रश्नोत्तर -> अक्सर पूछे जाने वाले प्रश्न
    // 15 SEO-अनुकूल FAQs -> अक्सर पूछे जाने वाले प्रश्न
    // 15 एसईओ-अनुकूल अक्सर पूछे जाने वाले प्रश्न (FAQs) -> अक्सर पूछे जाने वाले प्रश्न

    content = content.replace(/15 SEO-Friendly FAQs/gi, 'Frequently Asked Questions');
    content = content.replace(/15 SEO-friendly FAQs/gi, 'Frequently Asked Questions');
    content = content.replace(/15 एसईओ-अनुकूल अक्सर पूछे जाने वाले प्रश्न/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/15 SEO-अनुकूल अक्सर पूछे जाने वाले प्रश्न/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/15 एसईओ-अनुकूल एफएक्यू/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/15 SEO-अनुकूल प्रश्नोत्तर/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/15 SEO-अनुकूल FAQs/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/15 एसईओ-अनुकूल अक्सर पूछे जाने वाले प्रश्न \(FAQs\)/g, 'अक्सर पूछे जाने वाले प्रश्न');

    // Just in case there are other variations with "SEO-Friendly FAQs" or "SEO-friendly FAQs"
    content = content.replace(/SEO-Friendly FAQs/gi, 'Frequently Asked Questions');
    content = content.replace(/SEO-friendly FAQs/gi, 'Frequently Asked Questions');
    content = content.replace(/एसईओ-अनुकूल अक्सर पूछे जाने वाले प्रश्न/g, 'अक्सर पूछे जाने वाले प्रश्न');
    content = content.replace(/SEO-अनुकूल अक्सर पूछे जाने वाले प्रश्न/g, 'अक्सर पूछे जाने वाले प्रश्न');

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Updated FAQs header in: ${filePath}`);
    }
}

function walkDir(dir) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const fullPath = path.join(dir, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            walkDir(fullPath);
        } else if (file === 'index.html') {
            processFile(fullPath);
        }
    }
}

baseDirs.forEach(dir => {
    if (fs.existsSync(dir)) {
        walkDir(dir);
    }
});

console.log('Cleanup of SEO texts completed.');
