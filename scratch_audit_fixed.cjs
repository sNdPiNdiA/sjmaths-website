const fs = require('fs');
const path = require('path');

const topics = [
  'integers-properties-and-operations',
  'bodmas-rule-simplification',
  'lcm-and-hcf-methods-applications'
];

topics.forEach(t => {
  const p = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', t, 'index.html');
  const c = fs.readFileSync(p, 'utf8');

  console.log(`\n================== AUDIT FOR ${t} ==================`);

  // Check 1: Hero card tag
  const hasHeaderTag = c.includes('<header class="topic-hero-card">') || c.includes('<header');
  console.log(`1. Uses <header> tag: ${hasHeaderTag} (MUST BE FALSE)`);

  // Check 2: Form feed / spade
  const spadeCount = (c.match(/♠|\x0c/g) || []).length;
  console.log(`2. Spade / 0x0c count: ${spadeCount} (MUST BE 0)`);

  // Check 3: Broken ightarrow
  const bareIght = (c.match(/(?<!\\)ightarrow/g) || []).length;
  console.log(`3. Bare ightarrow count: ${bareIght} (MUST BE 0)`);

  // Check 4: Double backslashes on commands
  const dblCommands = (c.match(/\\{2,}(frac|text|times|div|dots|rightarrow)/g) || []).length;
  console.log(`4. Double-backslashed math commands: ${dblCommands} (MUST BE 0)`);

  // Check 5: Total math expressions
  const mathMatches = c.match(/\$\$?[\s\S]*?\$\$?/g) || [];
  console.log(`5. Total math expressions: ${mathMatches.length}`);

  // Check 6: Nav buttons class
  const oldNavBtn = (c.match(/class="nav-btn"/g) || []).length;
  const portalNavBtn = (c.match(/portal-nav-btn/g) || []).length;
  console.log(`6. Old nav-btn: ${oldNavBtn} (MUST BE 0), portal-nav-btn: ${portalNavBtn} (> 0)`);

  // Check 7: Practice MCQs count
  const mcqs = (c.match(/class="mcq-question-card"/g) || []).length;
  console.log(`7. Total practice MCQs: ${mcqs} (MUST BE 12)`);
});
