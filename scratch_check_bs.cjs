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

  console.log(`=== ${t} ===`);
  
  // Check double backslashes inside math expressions
  const dblMatches = c.match(/\\{2,}[a-zA-Z]+/g);
  console.log('Double backslash commands:', dblMatches ? dblMatches.slice(0, 10) : 'none');
  
  // Check curly braces inside math like ${...}$ vs $\{...\}$
  const bareSetMatches = c.match(/\$\{[0-9]/g);
  console.log('Sets missing backslash on brace (${\\d):', bareSetMatches ? bareSetMatches.length : 0);
});
