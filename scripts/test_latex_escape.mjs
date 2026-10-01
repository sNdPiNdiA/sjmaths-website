import { jsonrepair } from 'jsonrepair';

function sanitizeLatex(text) {
  return text
    .replace(/\t(?=(?:o|heta|imes|au)\b)/g, '\\t')
    .replace(/\b(?=(?:eta|egin)\b)/g, '\\b')
    .replace(/\f(?=(?:rac)\b)/g, '\\f')
    .replace(/\n(?=(?:eq|abla|u)\b)/g, '\\n')
    .replace(/(?<!\\)\\(?![\\"/bfnrt]|u[0-9a-fA-F]{4})([a-zA-Z]+)/g, '\\\\$1');
}

// Let's test on raw string
const testRaw = '{"stmt": "Let $f: [a, b] \\to \\mathbb{R}$ and $c \\in (a, b)$ with $f\'(c) = 0$"}';
console.log('Original parsed:');
function sanitizeRawGeminiJson(raw) {
  return raw.replace(/(?<!\\)\\([a-zA-Z]+)/g, '\\\\$1');
}

const rawFromGemini = '{"stmt": "Let $f: [a, b] \\to \\mathbb{R}$ and $c \\in (a, b)$ with \\frac{1}{2} and \\theta"}';
const sanitized = sanitizeRawGeminiJson(rawFromGemini);
console.log('Sanitized string:');
console.log(sanitized);
const repaired = jsonrepair(sanitized);
const parsed = JSON.parse(repaired);
console.log('Successfully parsed:');
console.log(parsed.stmt);
