const fs = require('fs');
const path = require('path');

function walk(dir) {
    let results = [];
    const list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = path.join(dir, file);
        const stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(file));
        } else if (file.endsWith('.html')) {
            results.push(file);
        }
    });
    return results;
}

const files = walk('upsssc-lower-mains');
let updatedCount = 0;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    
    // 1. Calculate Canonical URL
    // Convert path to unix style
    let relativePath = file.split(path.sep).join('/');
    // Remove index.html
    if (relativePath.endsWith('index.html')) {
        relativePath = relativePath.slice(0, -10);
    }
    const canonicalUrl = `https://sjmaths.com/${relativePath}`;
    
    // 2. Extract Title
    let titleMatch = content.match(/<title>(.*?)<\/title>/);
    let titleText = titleMatch ? titleMatch[1].trim() : "UPSSSC Lower Subordinate Mains Study Material";
    
    // 3. Check for existing Description
    let descMatch = content.match(/<meta name="description" content="(.*?)">/);
    let descText = descMatch ? descMatch[1] : `Complete study material and practice questions for ${titleText.split(' - ')[0]} - UPSSSC Lower Subordinate Mains.`;
    
    let seoTagsToInject = "";
    
    // Description
    if (!content.includes('<meta name="description"')) {
        seoTagsToInject += `\n    <meta name="description" content="${descText}">`;
    }
    
    // Robots
    if (!content.includes('<meta name="robots"')) {
        seoTagsToInject += `\n    <meta name="robots" content="index, follow">`;
    }

    // Canonical
    if (!content.includes('<link rel="canonical"')) {
        seoTagsToInject += `\n    <link rel="canonical" href="${canonicalUrl}">`;
    }
    
    // Open Graph
    if (!content.includes('property="og:title"')) {
        seoTagsToInject += `\n    <meta property="og:title" content="${titleText}">\n    <meta property="og:description" content="${descText}">\n    <meta property="og:url" content="${canonicalUrl}">\n    <meta property="og:type" content="article">\n    <meta property="og:site_name" content="SJMaths">`;
    }

    if (seoTagsToInject.length > 0) {
        // Insert right after title tag
        if (titleMatch) {
            content = content.replace(titleMatch[0], titleMatch[0] + seoTagsToInject);
        } else {
            // fallback to before </head>
            content = content.replace("</head>", seoTagsToInject + "\n</head>");
        }
        
        fs.writeFileSync(file, content, 'utf8');
        updatedCount++;
    }
});

console.log(`Successfully updated SEO tags in ${updatedCount} files.`);
