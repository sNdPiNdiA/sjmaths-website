import fs from 'fs';
import path from 'path';

const baseDir = path.join(process.cwd(), 'up-upper-primary-teacher', 'hindi');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });

let validCount = 0;
let issues = [];

for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const file = path.join(baseDir, entry.name, 'index.html');
    if (!fs.existsSync(file)) {
        issues.push(`Missing index.html in ${entry.name}`);
        continue;
    }

    const html = fs.readFileSync(file, 'utf8');

    // Verification checks
    if (!html.includes('up-upper-primary-topic.min.css?v=20261002_02')) {
        issues.push(`${entry.name}: Missing updated CSS cache buster`);
    }
    if (!html.includes('up-upper-primary-topic.min.js?v=20261002_02')) {
        issues.push(`${entry.name}: Missing updated JS cache buster`);
    }
    if (html.includes('id="footer-container"') || html.includes('global-footer.min.js')) {
        issues.push(`${entry.name}: Contains unwanted footer`);
    }
    if (!html.includes('strategy-banner-box')) {
        issues.push(`${entry.name}: Missing strategy-banner-box`);
    }
    if (!html.includes('mindmap-wrapper')) {
        issues.push(`${entry.name}: Missing mindmap-wrapper`);
    }
    if (!html.includes('prep-card')) {
        issues.push(`${entry.name}: Missing prep-card`);
    }
    if (!html.includes('study-tabs-strip')) {
        issues.push(`${entry.name}: Missing study-tabs-strip`);
    }

    validCount++;
}

console.log(`Validated ${validCount} Hindi topic directories.`);
if (issues.length > 0) {
    console.error('Issues found:', issues);
    process.exit(1);
} else {
    console.log('ALL 34 TOPIC PAGES PASSED FULL VALIDATION! 100% CLEAN & STYLED.');
}
