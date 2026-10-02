import fs from 'fs';

async function testPages() {
  const urls = [
    'http://localhost:8082/up-upper-primary-teacher/mathematics/algebraic-identities/',
    'http://localhost:8082/up-upper-primary-teacher/science/acids-bases-salts-ph/',
    'http://localhost:8082/up-upper-primary-teacher/mathematics/linear-equations-in-one-variable/',
    'http://localhost:8082/class-10-maths/'
  ];

  for (const url of urls) {
    try {
      const res = await fetch(url);
      const text = await res.text();
      console.log(`\nURL: ${url}`);
      console.log(`Status: ${res.status}`);
      console.log(`Contains katex.min.css: ${text.includes('katex.min.css')}`);
      console.log(`Contains auto-render.min.js: ${text.includes('auto-render.min.js')}`);
      console.log(`Contains renderMathInElement: ${text.includes('renderMathInElement')}`);
      const hasDoubleDollar = text.includes("left: '$$'") || text.includes('left: "$$"');
      console.log(`Proper $$ delimiter: ${hasDoubleDollar}`);
    } catch (e) {
      console.error(`Error fetching ${url}:`, e.message);
    }
  }
}

testPages();
