const fs = require('fs');
const path = require('path');

const topics = [
  'integers-properties-and-operations',
  'bodmas-rule-simplification',
  'lcm-and-hcf-methods-applications'
];

topics.forEach(t => {
  const p = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', t, 'index.html');
  let c = fs.readFileSync(p, 'utf8');

  // 1. Ensure topic-hero-card is a <div> and NOT <header>
  c = c.replace(/<header\s+class="topic-hero-card">/g, '<div class="topic-hero-card">');
  // If there's any remaining </header>, replace with </div>
  c = c.replace(/<\/header>/g, '</div>');

  // Also ensure .topic-hero-card CSS has explicit height: auto !important and display: block !important
  if (!c.includes('.topic-hero-card { display: block !important; height: auto !important;')) {
    c = c.replace(
      '.topic-hero-card {',
      '.topic-hero-card {\n        display: block !important;\n        height: auto !important;\n        min-height: 180px;\n        box-sizing: border-box !important;'
    );
  }

  // 2. Fix all escaped or corrupted characters
  c = c.replaceAll('\x0c', '\\f');
  c = c.replaceAll('♠', '\\f');

  // 3. Normalize multiple backslashes on LaTeX commands to exactly one
  const latexCommands = [
    'frac', 'text', 'times', 'div', 'dots', 'rightarrow', 'right', 'left',
    'mathbb', 'mathbf', 'sum', 'overline', 'le', 'ge', 'neq', 'in', 'notin',
    'subset', 'cup', 'cap', 'infty', 'pm', 'quad', 'sqrt', 'cases'
  ];

  latexCommands.forEach(cmd => {
    // Replace 2 or more backslashes before command with a single backslash
    const re = new RegExp('\\\\{2,}' + cmd + '(?![a-zA-Z])', 'g');
    c = c.replaceAll(re, '\\' + cmd);
  });

  // 4. Fix bare commands without backslash inside math $...$
  // Find all $...$ and $$...$$
  c = c.replace(/\$\$([\s\S]*?)\$\$/g, (match, inner) => {
    let fixed = inner;
    latexCommands.forEach(cmd => {
      // replace unescaped command: e.g. (?<!\\)frac
      const re = new RegExp('(?<!\\\\)\\b' + cmd + '\\b', 'g');
      fixed = fixed.replaceAll(re, '\\' + cmd);
    });
    // Fix set braces: e.g. {1, 2, ...} -> \{1, 2, ...\}
    fixed = fixed.replace(/(?<=\s|=|^)\{([0-9\-\+a-zA-Z\s,\\\\dots]+)\}(?=\s|=|$)/g, '\\{$1\\}');
    return '$$' + fixed + '$$';
  });

  c = c.replace(/(?<!\$)\$([^$\n]+)\$(?!\$)/g, (match, inner) => {
    let fixed = inner;
    latexCommands.forEach(cmd => {
      const re = new RegExp('(?<!\\\\)\\b' + cmd + '\\b', 'g');
      fixed = fixed.replaceAll(re, '\\' + cmd);
    });
    // Fix set braces: e.g. {1, 2, ...} -> \{1, 2, ...\}
    fixed = fixed.replace(/(?<=\s|=|^)\{([0-9\-\+a-zA-Z\s,\\\\dots]+)\}(?=\s|=|$)/g, '\\{$1\\}');
    return '$' + fixed + '$';
  });

  // 5. Special checks for specific text phrases
  c = c.replaceAll('1.2, 0.36, 7.20ightarrow', '1.2, 0.36, 7.20 \\rightarrow ');
  c = c.replaceAll('7.20ightarrow', '7.20 \\rightarrow ');
  c = c.replaceAll('ightarrow', '\\rightarrow');

  // Double check multiple backslashes again
  latexCommands.forEach(cmd => {
    const re = new RegExp('\\\\{2,}' + cmd + '(?![a-zA-Z])', 'g');
    c = c.replaceAll(re, '\\' + cmd);
  });

  fs.writeFileSync(p, c, 'utf8');
  console.log(`Saved pristine ${t}`);
});

// Sync bodmas alias
const bodmasCanon = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', 'bodmas-rule-simplification', 'index.html');
const bodmasAlias = path.join(process.cwd(), 'up-upper-primary-teacher', 'mathematics', 'bodmas-rule-and-brackets-simplification', 'index.html');
if (fs.existsSync(bodmasAlias)) {
  fs.copyFileSync(bodmasCanon, bodmasAlias);
  console.log('Synced bodmas alias.');
}
