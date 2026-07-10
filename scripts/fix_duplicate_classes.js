const fs = require('fs');

// Fix duplicate class attributes in HTML files
// Pattern: class="first-class" class="second-class" should become class="first-class second-class"

function fixDuplicateClasses(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    const original = content;

    // Fix pattern 1: class="..." class="..." on same line -> class="... ..."
    content = content.replace(
        /class="([^"]*)"\s+class="([^"]*)"/g,
        'class="$1 $2"'
    );

    // Fix pattern 2: class="value" class="value" (same class twice) -> class="value"
    content = content.replace(
        /class="([^"]+)\s+\1"/g,
        'class="$1"'
    );

    // Fix pattern 3: class="..." on previous line, then class="..." on next line (multi-line)
    // This handles: ... class="first-class" ...\n    class="second-class"
    content = content.replace(
        /class="([^"]*)"[^]*?\n\s*class="([^"]*)"/g,
        'class="$1 $2"'
    );

    if (content !== original) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`Fixed duplicate class attributes in: ${filePath}`);
        return true;
    }
    return false;
}

// Process the target file
fixDuplicateClasses('upsssc-lower-mains/history/social-aspects/index.html');
console.log('Done!');
