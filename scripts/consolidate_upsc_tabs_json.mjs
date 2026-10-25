import fs from 'fs';
import path from 'path';

const isDryRun = process.argv.includes('--dry-run');

console.log(`Starting UPSC Tabs & JSON Consolidation... [DryRun: ${isDryRun}]`);

const TARGET_TABS = ["notes", "practice", "revision", "mains", "test"];
let totalDirsScanned = 0;
let topicsConsolidated = 0;
let notesCreated = 0;
let fragmentedDeleted = 0;
let manifestsDeleted = 0;
let duplicatePracticeDeleted = 0;
let htmlsUpdated = 0;

function safeReadJson(filePath) {
  try {
    if (fs.existsSync(filePath)) {
      return JSON.parse(fs.readFileSync(filePath, 'utf8'));
    }
  } catch (err) {
    console.warn(`Failed to parse JSON: ${filePath} (${err.message})`);
  }
  return null;
}

function processTopicDir(dir) {
  const tabsDir = path.join(dir, 'tabs');
  const hasTabsDir = fs.existsSync(tabsDir) && fs.statSync(tabsDir).isDirectory();
  const indexHtmlPath = path.join(dir, 'index.html');
  const hasIndexHtml = fs.existsSync(indexHtmlPath);

  if (!hasTabsDir && !hasIndexHtml) return;

  totalDirsScanned++;

  // 1. Ensure tabs directory exists if this is a topic with index.html
  if (!hasTabsDir) {
    // Check if it's a microtopic with page data
    let isMicrotopic = false;
    if (hasIndexHtml) {
      const html = fs.readFileSync(indexHtmlPath, 'utf8');
      if (html.includes('id="upsc-page-data"') || html.includes('class="study-tabs"')) {
        isMicrotopic = true;
      }
    }
    if (!isMicrotopic) return;

    if (!isDryRun) {
      fs.mkdirSync(tabsDir, { recursive: true });
    }
  }

  topicsConsolidated++;

  // 2. Build or verify tabs/notes.json
  const notesPath = path.join(tabsDir, 'notes.json');
  const overviewPath = path.join(tabsDir, 'overview.json');
  const conceptsPath = path.join(tabsDir, 'concepts.json');
  const visualPath = path.join(tabsDir, 'visual.json');
  const comparisonsPath = path.join(tabsDir, 'comparisons.json');

  let notesData = safeReadJson(notesPath);

  if (!notesData) {
    const overview = safeReadJson(overviewPath) || {};
    const concepts = safeReadJson(conceptsPath) || {};
    const visual = safeReadJson(visualPath) || {};
    const comparisons = safeReadJson(comparisonsPath) || {};

    // If all were empty, try extracting from index.html if available
    let extractedOverview = overview;
    let extractedConcepts = concepts;
    let extractedVisual = visual;
    let extractedComparisons = comparisons;

    if (Object.keys(overview).length === 0 && hasIndexHtml) {
      try {
        const html = fs.readFileSync(indexHtmlPath, 'utf8');
        const match = html.match(/<script id="upsc-page-data"[^>]*>([\s\S]*?)<\/script>/);
        if (match) {
          const parsed = JSON.parse(match[1]);
          if (parsed.overview) extractedOverview = parsed.overview;
          if (parsed.concepts) extractedConcepts = parsed.concepts;
          if (parsed.visual) extractedVisual = parsed.visual;
          if (parsed.comparisons) extractedComparisons = parsed.comparisons;
        }
      } catch (e) {}
    }

    notesData = {
      overview: extractedOverview,
      concepts: extractedConcepts,
      visual: extractedVisual,
      comparisons: extractedComparisons
    };

    if (!isDryRun) {
      fs.writeFileSync(notesPath, JSON.stringify(notesData, null, 2), 'utf8');
    }
    notesCreated++;
  } else {
    // notes.json already exists; make sure overview, concepts, visual, comparisons keys exist
    let updated = false;
    for (const key of ['overview', 'concepts', 'visual', 'comparisons']) {
      if (!notesData[key]) {
        const legacyFile = path.join(tabsDir, `${key}.json`);
        const legacyData = safeReadJson(legacyFile);
        if (legacyData) {
          notesData[key] = legacyData;
          updated = true;
        } else {
          notesData[key] = {};
          updated = true;
        }
      }
    }
    if (updated && !isDryRun) {
      fs.writeFileSync(notesPath, JSON.stringify(notesData, null, 2), 'utf8');
    }
  }

  // 3. Delete fragmented JSON files
  for (const legacyPath of [overviewPath, conceptsPath, visualPath, comparisonsPath]) {
    if (fs.existsSync(legacyPath)) {
      if (!isDryRun) {
        fs.unlinkSync(legacyPath);
      }
      fragmentedDeleted++;
    }
  }

  // 4. Ensure practice.json exists in tabs/
  const tabPracticePath = path.join(tabsDir, 'practice.json');
  const rootPracticePath = path.join(dir, 'practice.json');

  if (!fs.existsSync(tabPracticePath)) {
    if (fs.existsSync(rootPracticePath)) {
      if (!isDryRun) {
        fs.copyFileSync(rootPracticePath, tabPracticePath);
      }
    } else {
      // Default practice template
      if (!isDryRun) {
        fs.writeFileSync(tabPracticePath, JSON.stringify({
          levels: { basic: [], conceptual: [], applied: [] }
        }, null, 2), 'utf8');
      }
    }
  }

  // Delete redundant root practice.json
  if (fs.existsSync(rootPracticePath)) {
    if (!isDryRun) {
      fs.unlinkSync(rootPracticePath);
    }
    duplicatePracticeDeleted++;
  }

  // 5. Ensure revision.json exists in tabs/
  const revisionPath = path.join(tabsDir, 'revision.json');
  if (!fs.existsSync(revisionPath)) {
    if (!isDryRun) {
      fs.writeFileSync(revisionPath, JSON.stringify({
        onePageNotes: { columns: [] },
        mnemonics: [],
        flashcards: [],
        frequentlyConfusedFacts: [],
        examDaySheet: { fiveFacts: [], threeTraps: [], oneMnemonic: "" }
      }, null, 2), 'utf8');
    }
  }

  // 6. Ensure mains.json exists in tabs/
  const mainsPath = path.join(tabsDir, 'mains.json');
  if (!fs.existsSync(mainsPath)) {
    if (!isDryRun) {
      fs.writeFileSync(mainsPath, JSON.stringify({
        questions: []
      }, null, 2), 'utf8');
    }
  }

  // 7. Ensure test.json exists in tabs/
  const testPath = path.join(tabsDir, 'test.json');
  if (!fs.existsSync(testPath)) {
    if (!isDryRun) {
      fs.writeFileSync(testPath, JSON.stringify({
        levels: { easy: [], medium: [], hard: [] }
      }, null, 2), 'utf8');
    }
  }

  // 8. Delete redundant root page.manifest.json
  const manifestPath = path.join(dir, 'page.manifest.json');
  if (fs.existsSync(manifestPath)) {
    if (!isDryRun) {
      fs.unlinkSync(manifestPath);
    }
    manifestsDeleted++;
  }

  // 9. Update index.html to set tabs: ["notes", "practice", "revision", "mains", "test"]
  if (hasIndexHtml) {
    try {
      let html = fs.readFileSync(indexHtmlPath, 'utf8');
      let changed = false;

      // Update #upsc-page-data tabs array
      const scriptMatch = html.match(/(<script id="upsc-page-data"[^>]*>)([\s\S]*?)(<\/script>)/);
      if (scriptMatch) {
        try {
          const pageData = JSON.parse(scriptMatch[2]);
          const currentTabsJson = JSON.stringify(pageData.tabs || []);
          const targetTabsJson = JSON.stringify(TARGET_TABS);
          if (currentTabsJson !== targetTabsJson) {
            pageData.tabs = TARGET_TABS;
            html = html.replace(
              scriptMatch[0],
              `${scriptMatch[1]}${JSON.stringify(pageData)}${scriptMatch[3]}`
            );
            changed = true;
          }
        } catch (e) {}
      }

      if (changed) {
        if (!isDryRun) {
          fs.writeFileSync(indexHtmlPath, html, 'utf8');
        }
        htmlsUpdated++;
      }
    } catch (err) {
      console.warn(`Error updating ${indexHtmlPath}: ${err.message}`);
    }
  }
}

function traverseAndConsolidate(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  const isTopicDir = entries.some(e => e.isDirectory() && e.name === 'tabs') ||
    (entries.some(e => e.isFile() && e.name === 'index.html') &&
      entries.some(e => e.isFile() && (e.name === 'practice.json' || e.name === 'content.json' || e.name === 'page.manifest.json')));

  if (isTopicDir) {
    processTopicDir(dir);
  }

  for (const entry of entries) {
    if (entry.isDirectory() && entry.name !== 'tabs' && entry.name !== 'node_modules' && !entry.name.startsWith('.')) {
      traverseAndConsolidate(path.join(dir, entry.name));
    }
  }
}

traverseAndConsolidate(path.resolve('upsc'));

console.log('\n=== Consolidation Summary ===');
console.log(`Total topics consolidated: ${topicsConsolidated}`);
console.log(`notes.json created: ${notesCreated}`);
console.log(`Fragmented JSON files deleted: ${fragmentedDeleted}`);
console.log(`page.manifest.json deleted: ${manifestsDeleted}`);
console.log(`Duplicate root practice.json deleted: ${duplicatePracticeDeleted}`);
console.log(`index.html updated with 5 tabs: ${htmlsUpdated}`);
