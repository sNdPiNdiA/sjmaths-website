const fs = require('fs');
try {
    const content = fs.readFileSync('test_output_v11.txt', 'utf16le');
    const lines = content.split('\r\n');

    // Parse Summary
    lines.forEach(l => {
        if (l.includes('Passed:') || l.includes('Failed:') || l.includes('Warnings:')) {
            console.log(l.trim());
        }
    });

} catch (e) {
    console.error(e);
}
