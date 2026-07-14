const fs = require('fs');
let html = fs.readFileSync('upsc/index.html', 'utf8');

const categories = [
    'ancient-history',
    'medieval-history',
    'modern-history',
    'art-and-culture',
    'geography',
    'environment',
    'polity',
    'economy',
    'science-and-tech'
];

categories.forEach(cat => {
    // Only replace the exact category link, not the sub-links
    const regex = new RegExp(`href="\\.\\/${cat}\\/"`, 'g');
    html = html.replace(regex, `href="#"`);
});

fs.writeFileSync('upsc/index.html', html);
console.log('Fixed upsc/index.html empty directory links');
