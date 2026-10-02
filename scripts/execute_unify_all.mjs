import fs from 'fs';
import path from 'path';

async function safeWrite(file, data) {
  for (let attempt = 1; attempt <= 10; attempt++) {
    try {
      await fs.promises.writeFile(file, data, 'utf8');
      return;
    } catch (e) {
      if (attempt === 10) throw e;
      await new Promise(res => setTimeout(res, 200));
    }
  }
}

function findHtmlFiles(dir) {
  let results = [];
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      results.push(...findHtmlFiles(fullPath));
    } else if (entry.isFile() && entry.name.endsWith('.html')) {
      results.push(fullPath);
    }
  }
  return results;
}

async function run() {
  const files = findHtmlFiles('up-upper-primary-teacher');
  console.log(`Processing ${files.length} HTML files in up-upper-primary-teacher...`);

  let countLegacyReplaced = 0;
  let countCssVersionUpdated = 0;
  let countSubjectHubs = 0;
  let countRootHub = 0;
  let countRedirectsSkipped = 0;

  for (const file of files) {
    let content = await fs.promises.readFile(file, 'utf8');
    const normalizedPath = file.replace(/\\/g, '/');

    // Skip redirect stubs
    if (content.includes('http-equiv="refresh"') || content.includes('window.location.replace')) {
      countRedirectsSkipped++;
      continue;
    }

    // Handle Root Hub
    if (normalizedPath === 'up-upper-primary-teacher/index.html') {
      if (!content.includes('up-upper-primary-topic.min.css')) {
        content = content.replace(
          /(<link href="\/assets\/css\/pages\.min\.css[^"]*" rel="stylesheet"\/>)/,
          '$1\n<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>'
        );
      } else {
        content = content.replace(/up-upper-primary-topic(\.min)?\.css(\?v=[^"']*)?/g, 'up-upper-primary-topic.min.css?v=20261002_03');
      }
      content = content.replace(/\.syllabus-container\s*\{[^}]*margin:[^}]*padding:[^}]*\}/g, '/* .syllabus-container handled by unified topic css */');
      content = content.replace(/\.hero-panel\s*\{[^}]*padding:\s*2\.5rem\s*2rem;[^}]*margin-bottom:\s*2\.25rem;[^}]*\}/g, '/* .hero-panel layout handled by unified topic css */');
      await safeWrite(file, content);
      countRootHub++;
      continue;
    }

    // Handle Subject Hubs
    if (/^up-upper-primary-teacher\/[^\/]+\/index\.html$/.test(normalizedPath)) {
      if (!content.includes('up-upper-primary-topic.min.css')) {
        content = content.replace(
          /(<link href="\/assets\/css\/pages\.min\.css[^"]*" rel="stylesheet"\/>)/,
          '$1\n<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>'
        );
      } else {
        content = content.replace(/up-upper-primary-topic(\.min)?\.css(\?v=[^"']*)?/g, 'up-upper-primary-topic.min.css?v=20261002_03');
      }
      content = content.replace(/\.subject-page-container\s*\{[^}]*margin:[^}]*padding:[^}]*\}/g, '/* .subject-page-container handled by unified topic css */');
      content = content.replace(/\.subject-hero-card\s*\{[^}]*padding:\s*2\.25rem\s*2rem;[^}]*margin-bottom:\s*2rem;[^}]*\}/g, '/* .subject-hero-card layout handled by unified topic css */');
      content = content.replace(/\.top-action-bar\s*\{[^}]*margin-bottom:\s*2rem;[^}]*\}/g, '/* .top-action-bar handled by unified topic css */');
      await safeWrite(file, content);
      countSubjectHubs++;
      continue;
    }

    // Handle Topic Pages with Large Legacy Style Tags
    const legacyStyleRegex = /<style[^>]*>[\s\S]*?\.topic-page-container[\s\S]*?<\/style>/i;
    if (legacyStyleRegex.test(content)) {
      let replacement = '';
      if (normalizedPath.includes('/english/')) {
        replacement = `<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>\n\n<!-- Language Mode Enforcement: English Only -->\n<style>\n    .lang-en { display: inline !important; }\n    .lang-hi { display: none !important; }\n</style>`;
      } else if (normalizedPath.includes('/sanskrit/')) {
        replacement = `<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>\n\n<!-- Language Mode Enforcement: Hindi Only -->\n<style>\n    .lang-hi { display: inline !important; }\n    .lang-en { display: none !important; }\n</style>`;
      } else if (normalizedPath.includes('/hindi/')) {
        replacement = `<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>\n\n<!-- Language Mode Enforcement: Hindi Only -->\n<style>\n    .lang-hi { display: inline !important; }\n    .lang-en { display: none !important; }\n</style>`;
      } else {
        replacement = `<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>`;
      }

      content = content.replace(legacyStyleRegex, replacement);
      content = content.replace(/(<link href="\/assets\/css\/up-upper-primary-topic\.min\.css\?v=20261002_03" rel="stylesheet"\/>\s*)+/g, '<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_03" rel="stylesheet"/>\n');

      await safeWrite(file, content);
      countLegacyReplaced++;
      continue;
    }

    // Handle Topic Pages that already link to up-upper-primary-topic.css or .min.css
    if (content.includes('up-upper-primary-topic')) {
      content = content.replace(/up-upper-primary-topic(\.min)?\.css(\?v=[^"']*)?/g, 'up-upper-primary-topic.min.css?v=20261002_03');
      await safeWrite(file, content);
      countCssVersionUpdated++;
      continue;
    }
  }

  console.log('Execution Summary:');
  console.log(`- Legacy <style> tags stripped and unified: ${countLegacyReplaced}`);
  console.log(`- Existing topic CSS links updated to v20261002_03: ${countCssVersionUpdated}`);
  console.log(`- Subject hub pages updated: ${countSubjectHubs}`);
  console.log(`- Root hub syllabus page updated: ${countRootHub}`);
  console.log(`- Redirect stubs preserved: ${countRedirectsSkipped}`);
  console.log(`Total files handled: ${countLegacyReplaced + countCssVersionUpdated + countSubjectHubs + countRootHub + countRedirectsSkipped}`);
}

run().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
