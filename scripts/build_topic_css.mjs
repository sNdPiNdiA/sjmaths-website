import fs from 'fs';
import path from 'path';

const srcPath = path.join(process.cwd(), 'assets', 'css', 'up-upper-primary-topic.css');
const dstPath = path.join(process.cwd(), 'assets', 'css', 'up-upper-primary-topic.min.css');

const css = fs.readFileSync(srcPath, 'utf8');

// Safe minification
let min = css
    // Remove multi-line comments
    .replace(/\/\*[\s\S]*?\*\//g, '')
    // Normalize newlines and tabs
    .replace(/[\r\n\t]+/g, ' ')
    // Remove spaces around symbols: { } ; : , > + ~
    .replace(/\s*([\{\}\;\:\,\>\+\~])\s*/g, '$1')
    // Restore required spaces for @media queries and calc/var if affected
    .replace(/\band\(/g, 'and (')
    .replace(/\bor\(/g, 'or (')
    .replace(/@media\s+/g, '@media ')
    // Remove multiple spaces
    .replace(/\s{2,}/g, ' ')
    // Remove trailing semicolons before closing brace
    .replace(/;}/g, '}')
    .trim();

fs.writeFileSync(dstPath, min, 'utf8');
console.log(`Original: ${css.length} bytes -> Minified: ${min.length} bytes`);

// Verify brace matching
let depth = 0;
for (let i = 0; i < min.length; i++) {
    if (min[i] === '{') depth++;
    else if (min[i] === '}') depth--;
}
console.log('Brace depth check (must be 0):', depth);
if (depth !== 0) throw new Error('Unbalanced braces in minified CSS!');
