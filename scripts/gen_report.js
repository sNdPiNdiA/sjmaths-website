const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');
const summaryPath = path.join(ROOT_DIR, '404_summary.json');
const artifactPath = path.join(ROOT_DIR, '404_report.md');

const data = JSON.parse(fs.readFileSync(summaryPath, 'utf8'));
const { total404, uniqueMissingLinks, missingLinks } = data;

// Sort by frequency
const sortedLinks = Object.entries(missingLinks)
  .sort((a, b) => b[1].length - a[1].length);

let md = `# 404 Broken Links Report\n\n`;
md += `**Total 404 Errors:** ${total404}\n`;
md += `**Unique Missing URLs:** ${uniqueMissingLinks}\n\n`;
md += `## Top 50 Most Frequent Missing URLs\n\n`;
md += `| Missing URL | Number of occurrences | Example File |\n`;
md += `|-------------|-----------------------|--------------|\n`;

for (let i = 0; i < Math.min(50, sortedLinks.length); i++) {
  const [link, files] = sortedLinks[i];
  const exampleFile = files[0];
  md += `| \`${link}\` | ${files.length} | \`${exampleFile}\` |\n`;
}

fs.writeFileSync(artifactPath, md);
console.log('Report generated at 404_report.md');
