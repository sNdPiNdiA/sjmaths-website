const fs = require('fs');
const path = require('path');

const topics = [
    'constituent-assembly-and-making-of-constitution',
    'preamble-of-the-constitution',
    'sources-of-the-indian-constitution',
    'parts-and-schedules-of-the-constitution',
    'citizenship-articles-5-11-and-caa',
    'fundamental-rights-articles-12-35-and-writs',
    'directive-principles-of-state-policy-dpsp-articles-36-51',
    'fundamental-duties-article-51a-and-swaran-singh',
    'union-executive-president-vp-pm-and-cabinet',
    'parliament-lok-sabha-rajya-sabha-and-officers',
    'parliamentary-proceedings-bills-motions-and-committees',
    'state-executive-governor-cm-and-council',
    'state-legislature-assembly-and-council',
    'judiciary-supreme-court-and-high-courts',
    'panchayati-raj-system-73rd-amendment-and-11th-schedule',
    'municipalities-74th-amendment-and-12th-schedule',
    'constitutional-bodies-ec-fc-cag-upsc',
    'statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal'
];

const base = path.join(__dirname, 'ssc-cgl', 'general-awareness', 'general-policy-polity');

let updated = 0;

topics.forEach(slug => {
    const file = path.join(base, slug, 'index.html');
    if (!fs.existsSync(file)) { console.log('Missing: ' + slug); return; }

    let html = fs.readFileSync(file, 'utf8');
    const original = html;

    // Pattern A: orphaned block followed by more CSS and then </head>
    // Match: </style>\n/* Practice Questions Tab Styling */\n...css...\n</head>
    // We need to wrap the CSS back inside <style>
    html = html.replace(
        /(<\/style>)\s*\/\*\s*Practice Questions Tab Styling\s*\*\/\s*([\s\S]+?)((?=<\/head>))/,
        (match, closeStyle, orphanedCss, beforeHead) => {
            // Clean the orphaned CSS: trim whitespace
            const cleanedCss = orphanedCss.trim();
            // If there's actual CSS content, put it into a new <style> block
            if (cleanedCss.length > 0 && cleanedCss !== '') {
                return `${closeStyle}\n    <style>\n        ${cleanedCss}\n    </style>\n    `;
            }
            return closeStyle + '\n    ';
        }
    );

    // Pattern B: Simple case - just the comment line with nothing after
    html = html.replace(/(<\/style>)\s*\/\*\s*Practice Questions Tab Styling\s*\*\/\s*\n?(\s*\n)?(\s*<\/head>)/,
        '$1\n$3'
    );

    if (html !== original) {
        fs.writeFileSync(file, html, 'utf8');
        console.log('Fixed: ' + slug);
        updated++;
    } else {
        // Check if comment still exists
        if (html.includes('Practice Questions Tab Styling')) {
            console.log('STILL HAS COMMENT: ' + slug);
        } else {
            console.log('Already clean: ' + slug);
        }
    }
});

console.log('\nDone. Fixed: ' + updated + '/' + topics.length);
