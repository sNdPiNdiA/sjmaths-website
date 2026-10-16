const fs = require('fs');
const path = require('path');

const compDir = path.resolve('upsssc-computer');
const entries = fs.readdirSync(compDir, { withFileTypes: true });

let updatedCount = 0;

for (const entry of entries) {
    if (entry.isDirectory()) {
        const indexPath = path.join(compDir, entry.name, 'index.html');
        if (fs.existsSync(indexPath)) {
            let content = fs.readFileSync(indexPath, 'utf8');

            // 1. Remove floating top-controls button
            content = content.replace(/<div class="top-controls">\s*<button class="lang-toggle-btn"[^>]*>A\/अ<\/button>\s*<\/div>/g, '');

            // 2. Fix breadcrumbs
            const oldBreadcrumbRegex = /<a class="lang-en" href="\/upsssc-lower-mains\/">UPSSSC Lower Subordinate<\/a>\s*<a class="lang-hi" href="\/upsssc-lower-mains\/">UPSSSC लोअर सबऑर्डिनेट<\/a>\s*<i class="fas fa-chevron-right"><\/i>/g;
            const newBreadcrumbMiddle = `<a class="lang-en" href="/upsssc-intermediate-level/">UPSSSC Mains</a>\n<a class="lang-hi" href="/upsssc-intermediate-level/">UPSSSC मुख्य परीक्षा</a>\n<i class="fas fa-chevron-right"></i>\n<a class="lang-en" href="/upsssc-computer/">Computer & IT</a>\n<a class="lang-hi" href="/upsssc-computer/">कंप्यूटर एवं सूचना प्रौद्योगिकी</a>\n<i class="fas fa-chevron-right"></i>`;
            content = content.replace(oldBreadcrumbRegex, newBreadcrumbMiddle);

            // 3. Remove inline gradient on submit button
            content = content.replace(/background:linear-gradient\(135deg,#27ae60,#2ecc71\);[^"]*/g, 'background:#059669;color:white;border:none;border-radius:8px;font-size:1.05rem;font-weight:700;cursor:pointer;box-shadow:0 4px 12px rgba(5,150,105,0.25);');

            // 4. Update JSON-LD schemas
            content = content.replace(/"item":\s*"https:\/\/sjmaths\.com\/upsssc-lower-mains\/"/g, '"item": "https://sjmaths.com/upsssc-intermediate-level/"');
            content = content.replace(/"name":\s*"Upsssc Lower Mains"/g, '"name": "UPSSSC Mains"');

            fs.writeFileSync(indexPath, content, 'utf8');
            updatedCount++;
        }
    }
}

console.log(`Updated ${updatedCount} Computer topic pages.`);
