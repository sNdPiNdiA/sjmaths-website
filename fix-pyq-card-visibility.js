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
    if (!fs.existsSync(file)) {
        console.log('Missing: ' + slug);
        return;
    }
    let html = fs.readFileSync(file, 'utf8');
    const original = html;

    // Fix 1: Broad ".practice-card { display: none; }" -> scoped to [data-level] only
    html = html.replace(
        /\.practice-card \{ display: none; \}\s*\n\s*\.practice-card\.level-active \{ display: block; \}/g,
        '.practice-card[data-level] { display: none; }\n        .practice-card[data-level].level-active { display: block; }'
    );

    // Fix 2: Attribute-listed selectors like .practice-card[data-level="1"], ... { display: none; }
    html = html.replace(
        /\.practice-card\[data-level="1"\][^{]*\{ display: none; \}/g,
        '.practice-card[data-level] { display: none; }'
    );

    // Fix 3: Also ensure .practice-card.level-active overrides properly
    // (already handled above, but let's make sure)

    if (html !== original) {
        fs.writeFileSync(file, html, 'utf8');
        console.log('Fixed: ' + slug);
        updated++;
    } else {
        console.log('No change: ' + slug);
    }
});

console.log('\nDone. Updated: ' + updated + '/' + topics.length);
