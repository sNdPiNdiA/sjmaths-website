const fs = require('fs');
const path = require('path');

const indexPath = path.join('up-assistant-teacher', 'index.html');
let html = fs.readFileSync(indexPath, 'utf8');

// Backup index.html
fs.writeFileSync(path.join('up-assistant-teacher', 'index.html.bak'), html, 'utf8');

const subjectFolders = {
    hindi: 'hindi',
    sanskrit: 'sanskrit',
    eng: 'english',
    sci: 'science',
    math: 'mathematics',
    teach: 'teaching-skills',
    psych: 'child-psychology',
    social: 'environmental-social-studies',
    gk: 'gk-current-affairs',
    reas: 'logical-reasoning',
    it: 'information-technology',
    life: 'life-skill-management'
};

// Get subdirectories for each subject folder
const subjectDirs = {};
for (const [prefix, folder] of Object.entries(subjectFolders)) {
    const dirPath = path.join('up-assistant-teacher', folder);
    if (fs.existsSync(dirPath)) {
        subjectDirs[prefix] = fs.readdirSync(dirPath, { withFileTypes: true })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name)
            .sort();
    } else {
        subjectDirs[prefix] = [];
    }
}

// Custom manual sorting or mapping if needed for subjects where alphabetical order differs from syllabus order
// Let's check subdirs for each
console.log('Subject dirs loaded:', Object.keys(subjectDirs));

// 1. Update subject card titles to have href and external link icon if missing
// Example: <h2 class="subject-title" id="subj-hindi"> ... </h2>
// Subject cards have IDs like id="subj-hindi", id="subj-sanskrit", id="subj-english", id="subj-sci", id="subj-math", id="subj-teaching", id="subj-psych", id="subj-social", id="subj-gk", id="subj-reasoning", id="subj-it", id="subj-life"

const cardSubjectMap = {
    'subj-hindi': 'hindi',
    'subj-sanskrit': 'sanskrit',
    'subj-english': 'english',
    'subj-sci': 'science',
    'subj-math': 'mathematics',
    'subj-teaching': 'teaching-skills',
    'subj-psych': 'child-psychology',
    'subj-social': 'environmental-social-studies',
    'subj-gk': 'gk-current-affairs',
    'subj-reasoning': 'logical-reasoning',
    'subj-it': 'information-technology',
    'subj-life': 'life-skill-management'
};

// Let's update subject titles
for (const [cardId, prefix] of Object.entries(cardSubjectMap)) {
    const folder = subjectFolders[prefix];
    // Find subject-card with this id
    const cardRegex = new RegExp(`(<div class="subject-card"[^>]*id="${cardId}"[^>]*>[\\s\\S]*?<h2 class="subject-title">)([\\s\\S]*?)(<\/h2>)`, 'i');
    html = html.replace(cardRegex, (match, openTag, titleContent, closeTag) => {
        // If titleContent doesn't have an <a> with href, wrap it
        if (!titleContent.includes('href=')) {
            // Extract inner spans (lang-hi, lang-en)
            // titleContent might be <a><span>...</span><span>...</span></a>
            // Let's clean up titleContent inner HTML
            let inner = titleContent.trim();
            if (inner.startsWith('<a>') && inner.endsWith('</a>')) {
                inner = inner.substring(3, inner.length - 4);
            }
            // Add external link icon inside spans if not present
            const updatedInner = inner.replace(/(<\/span>)/g, ' <i class="fas fa-external-link-alt" style="font-size:0.8rem;margin-left:0.5rem;opacity:0.6;"></i>$1');
            return `${openTag}<a href="/up-assistant-teacher/${folder}/">${updatedInner}</a>${closeTag}`;
        }
        return match;
    });
}

// 2. Update checklist items that aren't already wrapped in <a>
// Regex to find <li class="syllabus-item"><input type="checkbox" ... id="PREFIX-mt-G-I"><span class="syllabus-text">...</span></li>
// We want to replace it with:
// <li class="syllabus-item"><a href="/up-assistant-teacher/FOLDER/TOPIC-DIR/" style="text-decoration:none;color:inherit;flex:1;"><input type="checkbox" ... id="PREFIX-mt-G-I"><span class="syllabus-text">...</span></a></li>

// To map each checkbox ID to its topic directory:
// Let's build a global counter or flatten groups per prefix.
// Wait, how are items counted across groups for each prefix?
// Let's check how many total items exist per prefix in index.html, and match them with subjectDirs[prefix].

console.log('Updating checklist items...');

// Let's write a regex replacement for syllabus-item
// Match: <li class="syllabus-item"><input type="checkbox" class="syllabus-checkbox"\s+id="([a-z]+)-mt-(\d+)-(\d+)">(<span class="syllabus-text">[\s\S]*?<\/span>)<\/li>
const itemRegex = /<li class="syllabus-item"><input type="checkbox" class="syllabus-checkbox"\s+id="([a-z]+)-mt-(\d+)-(\d+)">([\s\S]*?)<\/li>/g;

// Keep track of item indices per prefix
const prefixCounters = {};

html = html.replace(itemRegex, (match, prefix, grp, idx, rest) => {
    if (prefix === 'psych' || prefix === 'social' || prefix === 'gk') {
        // Already handled / wrapped in <a>
        return match;
    }

    if (!prefixCounters[prefix]) {
        prefixCounters[prefix] = 0;
    }
    const globalIdx = prefixCounters[prefix]++;
    const dirs = subjectDirs[prefix] || [];
    const topicDir = dirs[globalIdx] || `${prefix}-topic-${globalIdx + 1}`;
    const folder = subjectFolders[prefix];

    return `<li class="syllabus-item"><a href="/up-assistant-teacher/${folder}/${topicDir}/" style="text-decoration:none;color:inherit;flex:1;"><input type="checkbox" class="syllabus-checkbox" id="${prefix}-mt-${grp}-${idx}">${rest}</a></li>`;
});

fs.writeFileSync(indexPath, html, 'utf8');
console.log('Successfully updated up-assistant-teacher/index.html with clickable checklist links!');
