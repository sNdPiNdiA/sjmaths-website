const fs = require('fs');
const path = require('path');
const { convertMicrotopicContent } = require('./convert_microtopic_theme.cjs');
const { convertDayContent } = require('./convert_day_theme.cjs');

async function main() {
  console.log('Starting Batch Daylight Theme Upgrade across UPSC ASO platform...\n');

  // 1. Process all 544 Microtopics
  const manifestPath = path.resolve('upsc-aso/all_544_microtopics.json');
  const allTopics = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  let microSuccess = 0;
  for (const t of allTopics) {
    const file = path.resolve(t.filePath);
    if (!fs.existsSync(file)) {
      console.warn(`Warning: file not found: ${t.filePath}`);
      continue;
    }
    const original = fs.readFileSync(file, 'utf8');
    const updated = convertMicrotopicContent(original);
    fs.writeFileSync(file, updated, 'utf8');
    microSuccess++;
  }
  console.log(`[MICROTOPICS] Successfully converted ${microSuccess} / ${allTopics.length} microtopics to daylight theme.`);

  // 2. Process all 97 Day Modules
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  let daySuccess = 0;
  for (const d of existingDays) {
    const original = fs.readFileSync(d.outputPath, 'utf8');
    const updated = convertDayContent(d.outputPath, original);
    fs.writeFileSync(d.outputPath, updated, 'utf8');
    daySuccess++;
  }
  console.log(`[DAY MODULES] Successfully converted ${daySuccess} / ${existingDays.length} day modules to daylight theme.`);

  // 3. Update audit_day_pages.cjs
  const dayAuditPath = path.resolve('upsc-aso/audit_day_pages.cjs');
  let dayAuditContent = fs.readFileSync(dayAuditPath, 'utf8');
  dayAuditContent = dayAuditContent.replace(
    /const hasDarkOverride = html\.includes\('background-color: #060911 !important'\) \|\| html\.includes\('background-color:#060911!important'\);[\s\S]*?missingDarkBody\+\+;\s*issues\.push\('Missing html, body #060911 !important dark theme override'\);\s*\}/,
    `const hasDaylightOverride = (html.includes('background-color: #f8fafc !important') || html.includes('background-color:#f8fafc!important') || html.includes('--bg-base: #f8fafc')) && !html.includes('#060911');
    if (!hasDaylightOverride) {
      missingDarkBody++;
      issues.push('Missing stress-free daylight theme #f8fafc override or contains legacy dark void #060911');
    }`
  );
  fs.writeFileSync(dayAuditPath, dayAuditContent, 'utf8');
  console.log('[AUDIT] Updated audit_day_pages.cjs to validate stress-free daylight theme.');

  // 4. Update audit_all_544_microtopics.cjs
  const microAuditPath = path.resolve('upsc-aso/audit_all_544_microtopics.cjs');
  let microAuditContent = fs.readFileSync(microAuditPath, 'utf8');
  microAuditContent = microAuditContent.replace(
    /\/\/ Dark mode check[\s\S]*?if \(!content\.includes\('#060911'\)\) \{[\s\S]*?issues\.push\('Missing dark theme #060911 background'\);[\s\S]*?\}/,
    `// Daylight UI Theme check (stress-free eye-friendly theme)
  if (!content.includes('--bg-void: #f8fafc') || content.includes('#060911')) {
    issues.push('Missing stress-free daylight theme (--bg-void: #f8fafc) or contains legacy dark void #060911');
  }`
  );
  fs.writeFileSync(microAuditPath, microAuditContent, 'utf8');
  console.log('[AUDIT] Updated audit_all_544_microtopics.cjs to validate stress-free daylight theme.');

  // 5. Update template in generate_microtopics_batch.mjs
  const batchGenPath = path.resolve('upsc-aso/generate_microtopics_batch.mjs');
  let batchGenContent = fs.readFileSync(batchGenPath, 'utf8');
  batchGenContent = convertMicrotopicContent(batchGenContent);
  fs.writeFileSync(batchGenPath, batchGenContent, 'utf8');
  console.log('[GENERATOR] Updated generate_microtopics_batch.mjs HTML template to daylight theme.');

  console.log('\nAll batch theme conversions completed successfully!');
}

main().catch(err => {
  console.error('Fatal error in theme conversion:', err);
  process.exit(1);
});
