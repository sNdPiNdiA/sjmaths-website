const fs = require('fs');
const path = require('path');

const topics = [
    "constituent-assembly-and-making-of-constitution",
    "preamble-of-the-constitution",
    "sources-of-the-indian-constitution",
    "parts-and-schedules-of-the-constitution",
    "citizenship-articles-5-11-and-caa",
    "fundamental-rights-articles-12-35-and-writs",
    "directive-principles-of-state-policy-dpsp-articles-36-51",
    "fundamental-duties-article-51a-and-swaran-singh",
    "union-executive-president-vp-pm-and-cabinet",
    "parliament-lok-sabha-rajya-sabha-and-officers",
    "parliamentary-proceedings-bills-motions-and-committees",
    "state-executive-governor-cm-and-council",
    "state-legislature-assembly-and-council",
    "judiciary-supreme-court-and-high-courts",
    "panchayati-raj-system-73rd-amendment-and-11th-schedule",
    "municipalities-74th-amendment-and-12th-schedule",
    "constitutional-bodies-ec-fc-cag-upsc",
    "statutory-and-non-constitutional-bodies-niti-aayog-nhrc-lokpal"
];

const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/general-awareness/general-policy-polity';

// The leaked CSS text pattern that appears in the rendered HTML
const leakedCssPattern = /\.practice-progress-bar \{[\s\S]*?\.q-meta \.time \{ color: #e74c3c; \}/;

topics.forEach(slug => {
    const filePath = path.join(baseDir, slug, 'index.html');
    if (!fs.existsSync(filePath)) {
        console.log(`Skipping: ${slug} (not found)`);
        return;
    }

    let html = fs.readFileSync(filePath, 'utf8');
    const match = html.match(leakedCssPattern);

    if (!match) {
        console.log(`No leaked CSS found in: ${slug}`);
        return;
    }

    const leakedCss = match[0];
    console.log(`Found leaked CSS in: ${slug}`);

    // Remove the leaked CSS from the body
    html = html.replace(leakedCss, '');

    // Find the closing </style> tag and inject CSS properly inside the style block
    const styleEndIdx = html.indexOf('</style>');
    if (styleEndIdx === -1) {
        console.log(`  Warning: No </style> tag found in ${slug}`);
        return;
    }

    // Add CSS before </style>
    html = html.slice(0, styleEndIdx) + leakedCss + '\n    ' + html.slice(styleEndIdx);

    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`  Fixed: ${slug}`);
});

console.log('\nDone! CSS injection fixed in all files.');