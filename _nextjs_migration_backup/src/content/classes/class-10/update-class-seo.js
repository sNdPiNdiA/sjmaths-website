// ============================================
// FILE: scripts/update-class-seo.js
// Run with: node scripts/update-class-seo.js
// ============================================

const fs = require('fs');
const path = require('path');

const DOMAIN = 'https://www.sjmaths.com';

const CLASS_CONFIG = {
    'class-9': {
        title: 'Class 9 Mathematics - SJMaths',
        desc: 'Comprehensive study materials for Class 9 Mathematics. Access chapter-wise notes, NCERT solutions, and practice questions to build a strong foundation.',
        kw: 'Class 9 Maths, Class 9 NCERT Solutions, Class 9 Maths Notes, Class 9 Exam Preparation, SJMaths'
    },
    'class-11': {
        title: 'Class 11 Mathematics - SJMaths',
        desc: 'Comprehensive study materials for Class 11 Mathematics. Access chapter-wise notes, NCERT solutions, and practice questions for CBSE and JEE preparation.',
        kw: 'Class 11 Maths, Class 11 NCERT Solutions, Class 11 Maths Notes, Class 11 JEE Preparation, SJMaths'
    },
    'class-12': {
        title: 'Class 12 Mathematics - SJMaths',
        desc: 'Comprehensive study materials for Class 12 Mathematics. Access chapter-wise notes, NCERT solutions, PYQs, and sample papers for Board Exams and JEE.',
        kw: 'Class 12 Maths, Class 12 NCERT Solutions, Class 12 Maths Notes, Class 12 PYQs, Class 12 Board Exam, SJMaths'
    }
};

function updateClassSEO(className) {
    const filePath = path.join('classes', className, 'index.html');
    
    if (!fs.existsSync(filePath)) {
        console.log(`⚠️  Skipping ${className}: File not found at ${filePath}`);
        return;
    }

    let content = fs.readFileSync(filePath, 'utf8');
    const config = CLASS_CONFIG[className];
    const url = `${DOMAIN}/classes/${className}/`;
    let modified = false;

    // Helper to inject tag if missing
    const inject = (checkStr, tagHtml, anchor) => {
        if (!content.includes(checkStr)) {
            if (content.includes(anchor)) {
                content = content.replace(anchor, `${anchor}\n    ${tagHtml}`);
                modified = true;
            }
        }
    };

    // 1. Meta Description
    inject('name="description"', `<meta name="description" content="${config.desc}">`, '<meta charset="UTF-8">');

    // 2. Keywords (Inject after description if possible, else after charset)
    if (!content.includes('name="keywords"')) {
        if (content.includes('name="description"')) {
            // Regex to find the closing > of description and append after it
            content = content.replace(/(<meta name="description"[^>]*>)/, `$1\n    <meta name="keywords" content="${config.kw}">`);
        } else {
            inject('name="keywords"', `<meta name="keywords" content="${config.kw}">`, '<meta charset="UTF-8">');
        }
        modified = true;
    }

    // 3. Robots & Author
    inject('name="robots"', `<meta name="robots" content="index, follow">`, 'name="keywords"');
    inject('name="author"', `<meta name="author" content="SJMaths">`, 'name="robots"');

    // 4. Canonical Link
    inject('rel="canonical"', `<link rel="canonical" href="${url}">`, 'name="author"');

    // 5. Open Graph Tags
    if (!content.includes('property="og:title"')) {
        const ogTags = `
    <!-- Open Graph -->
    <meta property="og:title" content="${config.title}">
    <meta property="og:description" content="${config.desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="${url}">`;
        
        // Inject before viewport
        inject('property="og:title"', ogTags, '<link rel="canonical"');
        // Fallback if canonical wasn't there/found
        if (!content.includes('property="og:title"')) {
             content = content.replace('</head>', `${ogTags}\n</head>`);
             modified = true;
        }
    }

    if (modified) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Updated SEO for ${className}`);
    } else {
        console.log(`✨ ${className} is already up to date.`);
    }
}

console.log('🚀 Updating Class SEO Tags...');
Object.keys(CLASS_CONFIG).forEach(updateClassSEO);