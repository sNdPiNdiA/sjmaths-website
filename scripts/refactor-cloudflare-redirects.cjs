const fs = require('fs');
const path = require('path');
const { ROOT } = require('./seo-html.cjs');

const file = path.join(ROOT, '_redirects');
const source = fs.readFileSync(file, 'utf8');

const rules = source.split(/\r?\n/).map(raw => {
  const [sourcePath, destination, status, ...extra] = raw.trim().split(/\s+/);
  if (!sourcePath?.startsWith('/') || !destination || !/^\d{3}$/.test(status || '') || extra.length) return null;
  return { source: sourcePath, destination, status: Number(status) };
}).filter(Boolean);

// These broad fallbacks either pointed at missing files or converted unrelated
// retired URLs into homepage soft 404s. Real ebook PDFs must remain fetchable.
const removedSources = new Set([
  '/wp-content/*',
  '/images/*',
  '/maths-mastery/*',
  '/assets/ebooks/*',
  '/sarkari-jobs/*',
  '/sarkari-jobs',
  '/app/*',
  '/classes/*',
]);

// These fixed-prefix wildcards still need to match meaningful descendant URLs.
// All other fixed-prefix wildcards become exact trailing-slash redirects so they
// no longer consume Cloudflare's 100-rule dynamic budget.
const retainedFixedWildcards = new Set([
  '/current-affairs/daily/*',
  '/current-affairs/topic/*',
  '/upsc/geography/Climatology/Various-Types-of-Wind-Seasonal-Local-Wind-etc/*',
]);

const normalized = [];
for (const rule of rules) {
  if (removedSources.has(rule.source)) continue;
  if (rule.source.endsWith('/*') && !rule.source.includes(':') &&
      !rule.destination.includes(':splat') && !retainedFixedWildcards.has(rule.source)) {
    normalized.push({ ...rule, source: rule.source.slice(0, -1) });
  } else {
    normalized.push(rule);
  }
}

const aliases = [];
function addAlias(sourcePath, destination, bothSlashForms = true) {
  const withoutSlash = sourcePath.replace(/\/$/, '');
  aliases.push({ source: withoutSlash, destination, status: 301 });
  if (bothSlashForms) aliases.push({ source: withoutSlash + '/', destination, status: 301 });
}

// Search Console legacy topic slugs with direct current equivalents.
const topicAliases = [
  ['/upsc/medieval-history/Bhakti-and-Sufi-Movements/Sufi-Movement-Features-Characteristics-and-Stages', '/upsc/medieval-history/Bhakti-and-Sufi-Movements/Sufi-Movement-Features/'],
  ['/upsc/medieval-history/Mughal-Rule/Jahangir-Territorial-Consolidation-and-Expansion-Mewar-East-India-Kangra', '/upsc/medieval-history/Mughal-Rule/Jahangir-Territorial-Consolidation-and-Expansion/'],
  ['/upsc/medieval-history/Mughal-Rule/Akbar-Early-Expansion-Early-Expansion-of-the-Empire-1560-76', '/upsc/medieval-history/Mughal-Rule/Akbar-Early-Expansion-Early-Expansion-of-the-Empire/'],
  ['/upsc/modern-history/Third-Phase-of-National-Movement/Individual-Satyagraha-1941', '/upsc/modern-history/Third-Phase-of-National-Movement/Individual-Satyagraha/'],
  ['/upsc/modern-history/Third-Phase-of-National-Movement/Cripps-Mission-1942', '/upsc/modern-history/Third-Phase-of-National-Movement/Cripps-Mission/'],
  ['/upsc/modern-history/Third-Phase-of-National-Movement/Pakistan-Resolution-23-Mar-1940', '/upsc/modern-history/Third-Phase-of-National-Movement/Pakistan-Resolution/'],
  ['/upsc/modern-history/Third-Phase-of-National-Movement/Poona-Pact-1932', '/upsc/modern-history/Third-Phase-of-National-Movement/Poona-Pact/'],
  ['/upsc/modern-history/First-Phase-of-National-Movement-1905-1917/Key-Sessions-of-the-Indian-National-Congress', '/upsc/modern-history/First-Phase-of-National-Movement-1905-1917/Key-Sessions-of-the-Indian-National-Congress-INC/'],
  ['/upsc/science-and-tech/Biotechnology-Biology/Intellectual-Property-Rights-Meaning-and-Types', '/upsc/science-and-tech/Biotechnology-Biology/Intellectual-Property-Rights/'],
  ['/upsc/science-and-tech/Biotechnology-Biology/Inheritance-Genetics', '/upsc/science-and-tech/Biotechnology-Biology/Inheritance/'],
  ['/upsc/ancient-history/Mauryan-Empire/Administration-Important-Offices', '/upsc/ancient-history/Mauryan-Empire/Administration/'],
  ['/upsc/ancient-history/Mauryan-Empire/Sources-of-Information-Coins-and-Sites', '/upsc/ancient-history/Mauryan-Empire/Sources-of-Information/Coins-and-Sites/'],
  ['/upsc/modern-history/The-Revolt-of-1857/Local-Government-Royal-Commission-on-Decentralization-1908', '/upsc/modern-history/The-Revolt-of-1857/Local-Government-Royal-Commission-on-Decentralization/'],
  ['/upsc/art-and-culture/Religion-Language-and-Literature/Bhakti-Movement-Religions', '/upsc/art-and-culture/Religion-Language-and-Literature/Bhakti-Movement/'],
  ['/upsc/modern-history/Education-during-British-Rule/Kothari-Education-Commission-1964-66', '/upsc/modern-history/Education-during-British-Rule/Kothari-Education-Commission/'],
  ['/upsc/economy/Service-Sector-in-Indian-Economy/National-Investment-and-Infrastructure-Fund-NIIF', '/upsc/economy/Service-Sector-in-Indian-Economy/National-Investment-and-Infrastructure-Fund/'],
  ['/upsc/environment/Climate-Change-Environmental-Administration/National-Board-for-Wildlife-NBWL', '/upsc/environment/Climate-Change-Environmental-Administration/National-Board-for-Wildlife/'],
  ['/upsc/geography/Geomorphology/Theories-Distribution-of-Continents-Oceans', '/upsc/geography/Geomorphology/Theories/'],
  ['/upsc/environment/Resources-Energy-Pollution/Algal-Bloom-Water-Pollution', '/upsc/environment/Resources-Energy-Pollution/Algal-Bloom/'],
  ['/upsc/environment/Pollution-Occupational-Hazards/Biological-Pollution-Corrective-actions', '/upsc/environment/Pollution-Occupational-Hazards/Biological-Pollution/'],
  ['/upsc/economy/External-Sector-International-Organizations/International-Development-Association-IDA', '/upsc/economy/External-Sector-International-Organizations/International-Development-Association/'],
  ['/upsc/environment/Climate-Change-Environmental-Administration/EU-Initiatives-Climate', '/upsc/environment/Climate-Change-Environmental-Administration/EU-Initiatives/'],
  ['/upsc/environment/Climate-Change-Environmental-Administration/National-Action-Plan-for-Climate-Change-NAPCC', '/upsc/environment/Climate-Change-Environmental-Administration/National-Action-Plan-for-Climate-Change/'],
  ['/upsc/polity/Union-Executive-Legislature-Parliament/Devices-of-Parliamentary-Proceedings-Duplicate-in-prompt', '/upsc/polity/Union-Executive-Legislature-Parliament/Devices-of-Parliamentary-Proceedings/'],
  ['/upsc/economy/External-Sector-International-Organizations/International-Fund-for-Agricultural-Development-IFAD', '/upsc/economy/External-Sector-International-Organizations/International-Fund-for-Agricultural-Development/'],
  ['/upsc/economy/Industry-Infrastructure-in-Indian-Economy/Dedicated-Freight-Corridor-DFC', '/upsc/economy/Industry-Infrastructure-in-Indian-Economy/Dedicated-Freight-Corridor/'],
  ['/upsc/economy/Public-Finance-Taxation/Methods-of-Taxation-Progressive-Regressive-Proportional', '/upsc/economy/Public-Finance-Taxation/Methods-of-Taxation/'],
  ['/upsc/geography/Geomorphology/Biological-Weathering-Processes', '/upsc/geography/Geomorphology/Biological-Weathering/'],
  ['/upsc/environment/Nutrient-Cycling-Biodiversity/International-Union-for-Conservation-of-Nature-IUCN', '/upsc/environment/Nutrient-Cycling-Biodiversity/International-Union-for-Conservation-of-Nature/'],
  ['/upsc/environment/Pollution-Occupational-Hazards/Continuous-Ambient-Air-Quality-Monitoring-System-CAAQMS', '/upsc/environment/Pollution-Occupational-Hazards/Continuous-Ambient-Air-Quality-Monitoring-System/'],
  ['/upsc/environment/Terrestrial-Aquatic-Ecosystems/Mangroves-in-India', '/upsc/environment/Terrestrial-Aquatic-Ecosystems/Mangroves/'],
  ['/upsc/geography/Geomorphology/Ground-Water-Karst-Topography', '/upsc/geography/Geomorphology/Ground-Water/'],
];

for (const [sourcePath, destination] of topicAliases) {
  addAlias(sourcePath, destination);
  for (const [canonical, legacy] of [
    ['/ancient-history/', '/ancient_history/'],
    ['/modern-history/', '/modern_history/'],
    ['/medieval-history/', '/medieval_history/'],
    ['/science-and-tech/', '/science_and_tech/'],
    ['/art-and-culture/', '/art_and_culture/'],
  ]) {
    if (sourcePath.includes(canonical)) addAlias(sourcePath.replace(canonical, legacy), destination);
  }
}

for (const [sourcePath, destination] of [
  ['/ssc-cgl/quantitative-aptitude/right-prism-right-circular-cone-right-circular-cylinder/3d-figures-prism-cone-cylinder-sphere-pyramids', '/ssc-cgl/quantitative-aptitude/right-prism-right-circular-cone-right-circular-cylinder/'],
  ['/ssc-cgl/computer-knowledge/windows-explorer/windows-explorer-keyboard-shortcuts', '/ssc-cgl/computer-knowledge/windows-explorer/'],
  ['/ssc-cgl/quantitative-aptitude/elementary-surds/elementary-surds-rationalization-surds-comparison', '/ssc-cgl/quantitative-aptitude/elementary-surds/'],
  ['/ssc-cgl/finance-economics/non-profit-organisations-accounts/non-profit-accounts-receipts-payments-bills-of-exchange', '/ssc-cgl/finance-economics/non-profit-organisations-accounts-bills-of-exchange/'],
  ['/ssc-cgl/quantitative-aptitude/tables-and-graphs', '/ssc-cgl/quantitative-aptitude/mean-median-mode/'],
  ['/ssc-cgl/quantitative-aptitude/triangle-and-its-centres/congruence-similarity-of-triangles-theorems', '/ssc-cgl/quantitative-aptitude/congruence-and-similarity-of-triangles/'],
  ['/ssc-cgl/quantitative-aptitude/regular-polygons/regular-polygons-interior-exterior-angles-diagonals-calculation', '/ssc-cgl/quantitative-aptitude/regular-polygons/'],
  ['/ssc-cgl/finance-economics/theory-of-production-and-cost/theory-of-production-and-cost-forms-of-market', '/ssc-cgl/finance-economics/theory-of-production-and-cost/'],
  ['/ssc-cgl/general-awareness/basic-science-awareness/biology-nutrition-vitamins-human-diseases-plant-biology/hi', '/ssc-cgl/general-awareness/basic-science-awareness/biology-nutrition-vitamins-human-diseases-plant-biology/'],
  ['/current-affairs/weekly/2026-w24', '/current-affairs/weekly/2026/06/2026-06-08/'],
  ['/current-affairs/weekly/2026-w01', '/current-affairs/weekly/'],
  ['/current-affairs/bimonthly/2026-06-h1', '/current-affairs/bimonthly/'],
  ['/current-affairs/quiz', '/current-affairs/'],
  ['/classes', '/'],
  ['/class-9-maths/ncert-examplar-practice/chapter-7-triangles', '/class-9-maths/ncert-examplar-practice/chapter-9-triangles/exemplar-9-1'],
]) addAlias(sourcePath, destination);

addAlias(
  '/upsc/environment/Climate-Change-Environmental-Administration/National-Action-Plan-for-Climate-Change-NAPCC/index.html',
  '/upsc/environment/Climate-Change-Environmental-Administration/National-Action-Plan-for-Climate-Change/',
  false,
);

addAlias(
  '/class-9-maths/ncert-examplar-practice/chapter-7-triangles/exemplar-7-1.html',
  '/class-9-maths/ncert-examplar-practice/chapter-9-triangles/exemplar-9-1',
  false,
);

const bySource = new Map();
for (const rule of [...normalized, ...aliases]) bySource.set(rule.source, rule);
const allRules = [...bySource.values()];
const staticRules = allRules.filter(rule => !/[:*]/.test(rule.source));
const dynamicRules = allRules.filter(rule => /[:*]/.test(rule.source));

function topLevel(rule) {
  return rule.source.split('/')[1] || 'root';
}

function renderSection(title, sectionRules) {
  const output = [`# ${title}`];
  const groups = new Map();
  for (const rule of sectionRules) {
    const group = topLevel(rule);
    if (!groups.has(group)) groups.set(group, []);
    groups.get(group).push(rule);
  }
  for (const [group, groupRules] of groups) {
    output.push(`# /${group}`);
    for (const rule of groupRules) {
      output.push(`${rule.source} ${rule.destination} ${rule.status}`);
    }
    output.push('');
  }
  if (output.at(-1) === '') output.pop();
  return output;
}

const output = [
  '# Cloudflare Pages routing for SJMaths',
  '# Keep every exact source above every wildcard or placeholder source.',
  '# Cloudflare supports at most 2,000 static and 100 dynamic rules per file.',
  '',
  ...renderSection('Static redirects', staticRules),
  '',
  ...renderSection('Dynamic redirects and asset rewrites', dynamicRules),
  '',
].join('\n');

fs.writeFileSync(file, output);
console.log(JSON.stringify({ before: rules.length, after: allRules.length, static: staticRules.length, dynamic: dynamicRules.length }, null, 2));
