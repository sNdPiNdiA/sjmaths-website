const fs = require('fs');
const path = require('path');
const vm = require('vm');
const { siteFiles } = require('./seo-html.cjs');

const ROOT = path.resolve(__dirname, '..');

function cleanScriptText(text, isJson = false) {
  let res = text;

  // 1. Remove stray \<span before tags
  res = res.replace(/\\<span\b/g, '<span');

  // 2. For math class names inserted into double quoted strings:
  // change class="math-..." to class='math-...'
  res = res.replace(/(<[a-zA-Z0-9]+[^>]*?class=)"(math-[^"]*)"/g, "$1'$2'");

  if (isJson) {
    // In JSON, any double quote inside an HTML tag attribute
    res = res.replace(/(<[a-zA-Z0-9]+[^>]*?\b[a-zA-Z0-9_-]+=)"([^"]*)"/g, "$1'$2'");
    // Fix stray </span></span> before comma or array close
    res = res.replace(/\]\s*<\/span><\/span>(\s*[,\]])/g, ']}$1');
  }

  // 3. Fix odd number of backslashes before non-JSON-escape characters
  res = res.replace(/(\\+)([^"\\/bfnrt]|u(?![0-9a-fA-F]{4})|$)/g, (match, slashes, nextChar) => {
    if (slashes.length % 2 === 1) {
      return slashes + '\\' + nextChar;
    }
    return match;
  });

  return res;
}

const files = siteFiles().filter(f => f.endsWith('.html'));

let fixedFiles = 0;
let jsonLdFixed = 0;
let embJsonFixed = 0;
let inlineScriptFixed = 0;
let strayScriptFixed = 0;

for (const relPath of files) {
  const absPath = path.join(ROOT, relPath);
  if (!fs.existsSync(absPath)) continue;

  let original = fs.readFileSync(absPath, 'utf8');
  if (!original.trim()) continue;

  let modified = original;
  let fileChanged = false;

  // 1. Check for stray unclosed <script> before <script
  if (/(?:<script>\s*)+(\r?\n\s*<script\b)/i.test(modified)) {
    modified = modified.replace(/(?:<script>\s*)+(\r?\n\s*<script\b)/gi, '$1');
    strayScriptFixed++;
    fileChanged = true;
  }

  // 2. Application/ld+json
  modified = modified.replace(/(<script\b[^>]*type=["']application\/ld\+json["'][^>]*>)([\s\S]*?)(<\/script>)/gi, (full, openTag, inner, closeTag) => {
    try {
      JSON.parse(inner);
      return full;
    } catch (err1) {
      const cleaned = cleanScriptText(inner, true);
      try {
        JSON.parse(cleaned);
        jsonLdFixed++;
        fileChanged = true;
        return openTag + cleaned + closeTag;
      } catch (err2) {
        console.error(`Could not fix JSON-LD in ${relPath}: ${err2.message}`);
        return full;
      }
    }
  });

  // 3. Application/json
  modified = modified.replace(/(<script\b(?![^>]*\bsrc=)[^>]*type=["']application\/json["'][^>]*>)([\s\S]*?)(<\/script>)/gi, (full, openTag, inner, closeTag) => {
    try {
      JSON.parse(inner);
      return full;
    } catch (err1) {
      const cleaned = cleanScriptText(inner, true);
      try {
        JSON.parse(cleaned);
        embJsonFixed++;
        fileChanged = true;
        return openTag + cleaned + closeTag;
      } catch (err2) {
        console.error(`Could not fix EMB JSON in ${relPath}: ${err2.message}`);
        return full;
      }
    }
  });

  // 4. Inline JS scripts: <script> or <script type="text/javascript">
  modified = modified.replace(/(<script\b(?![^>]*\bsrc=)(?:[^>]*type=["'](?:text|application)\/javascript["']|(?![^>]*\btype=))[^>]*>)([\s\S]*?)(<\/script>)/gi, (full, openTag, inner, closeTag) => {
    if (!inner.trim()) return full;
    try {
      new vm.Script(inner, { filename: relPath });
      return full;
    } catch (err1) {
      const cleaned = cleanScriptText(inner, false);
      try {
        new vm.Script(cleaned, { filename: relPath });
        inlineScriptFixed++;
        fileChanged = true;
        return openTag + cleaned + closeTag;
      } catch (err2) {
        console.error(`Could not fix inline JS in ${relPath}: ${err2.message}`);
        return full;
      }
    }
  });

  if (fileChanged && modified !== original) {
    fs.writeFileSync(absPath, modified, 'utf8');
    fixedFiles++;
  }
}

console.log(`\n=== Repair Complete ===`);
console.log(`Total files repaired: ${fixedFiles}`);
console.log(`Stray <script> blocks fixed: ${strayScriptFixed}`);
console.log(`JSON-LD blocks repaired: ${jsonLdFixed}`);
console.log(`Embedded JSON blocks repaired: ${embJsonFixed}`);
console.log(`Inline scripts repaired: ${inlineScriptFixed}`);
