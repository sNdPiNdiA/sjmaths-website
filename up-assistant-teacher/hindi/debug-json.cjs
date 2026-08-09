const fs = require('fs');
const path = require('path');

if (fs.existsSync('.env')) {
    for (const line of fs.readFileSync('.env', 'utf8').split('\n')) {
        const m = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?$/);
        if (m) {
            let v = (m[2] || '').trim();
            if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) v = v.slice(1, -1);
            process.env[m[1]] = process.env[m[1]] || v;
        }
    }
}
const apiKey = process.env.GEMINI_API_KEY;

async function main() {
    const res = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: 'Return a JSON object with one key "test" whose value is the string: He said "hello world" and wrote Madhushala (a famous work) in 1935.' }] }],
                generationConfig: { temperature: 0.1, maxOutputTokens: 200 }
            })
        }
    );
    const data = await res.json();
    const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
    console.log('RAW:', JSON.stringify(text));

    // Now actually test with the kavi parichay response but save raw
    const res2 = await fetch(
        `https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent?key=${apiKey}`,
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: `Generate a JSON with sections array for "Kavi Parichay aur Kavya Gun". Return ONLY the first section (Detailed Brief Overview table) with 4 rows. No markdown fences. Valid JSON only.` }] }],
                generationConfig: { temperature: 0.3, maxOutputTokens: 1000 }
            })
        }
    );
    const data2 = await res2.json();
    const text2 = data2?.candidates?.[0]?.content?.parts?.[0]?.text || '';
    fs.writeFileSync('debug-raw.txt', text2, 'utf8');
    console.log('\nRAW2 saved to debug-raw.txt');
    
    // Show chars around position 1508
    const pos = 1508;
    const start = Math.max(0, pos - 50);
    const end = Math.min(text2.length, pos + 50);
    console.log(`\nChars around position ${pos}:`);
    console.log(JSON.stringify(text2.substring(start, end)));
    console.log('Char codes:', [...text2.substring(pos-5, pos+5)].map(c => c.charCodeAt(0)));
}

main().catch(console.error);
