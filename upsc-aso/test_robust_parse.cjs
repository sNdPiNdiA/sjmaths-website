const fs = require('fs');

function loadEnv() {
  for (const p of ['.env', '../.env', 'upsc-aso/.env']) {
    if (fs.existsSync(p)) {
      for (const line of fs.readFileSync(p, 'utf8').split('\n')) {
        const m = line.match(/^\s*GEMINI_API_KEY\s*=\s*(.*)\s*$/);
        if (m) return m[1].trim().replace(/^['"]|['"]$/g, '');
      }
    }
  }
  return null;
}

const key = loadEnv();

function sanitizeAndParseJson(raw) {
  let cleaned = raw.trim();
  // Strip any accidental markdown fences
  if (cleaned.startsWith('```json')) {
    cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
  } else if (cleaned.startsWith('```')) {
    cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');
  }

  // First try direct JSON.parse
  try {
    return JSON.parse(cleaned);
  } catch (err1) {
    console.log('Direct JSON.parse failed (' + err1.message + '). Attempting intelligent repair...');
  }

  // Repair strategy:
  // Step A: Replace all single backslashes that are not part of valid JSON escapes
  // Valid JSON escapes: \", \\, \/, \b, \f, \n, \r, \t, \u[0-9a-fA-F]{4}
  // But note: In LaTeX, \frac, \nu, \rho, \tau, \theta are common.
  // To protect LaTeX, we can regex-replace backslashes inside string literals:
  let repaired = '';
  let inString = false;
  let isEscaped = false;

  for (let i = 0; i < cleaned.length; i++) {
    const ch = cleaned[i];
    if (inString) {
      if (isEscaped) {
        // We just saw a backslash
        isEscaped = false;
        // Check if ch is a valid JSON escape: ", \, /, b, f, n, r, t, u
        // BUT if it's followed by letters (like \frac, \rho, \nu, \tau), we want literal backslash!
        const nextChars = cleaned.slice(i, i + 5);
        if (/^(frac|nu|rho|tau|theta|partial|alpha|beta|gamma|sigma|lambda|mu|times|cdot|approx|infty|text|left|right|sqrt|mathbf|rm|int)/.test(nextChars)) {
          // This is a LaTeX keyword where \f, \n, \r, \t was meant as LaTeX, not JSON escape!
          repaired += '\\\\' + ch;
        } else if (/^["\\/bfnrt]/.test(ch) || (ch === 'u' && /^[0-9a-fA-F]{4}/.test(cleaned.slice(i + 1, i + 5)))) {
          // Standard JSON escape
          repaired += '\\' + ch;
        } else {
          // Invalid escape, double the backslash
          repaired += '\\\\' + ch;
        }
      } else {
        if (ch === '\\') {
          isEscaped = true;
        } else if (ch === '"') {
          inString = false;
          repaired += ch;
        } else {
          // Handle unescaped control characters inside JSON strings (e.g. raw newlines)
          if (ch === '\n') repaired += '\\n';
          else if (ch === '\r') repaired += '\\r';
          else if (ch === '\t') repaired += '\\t';
          else repaired += ch;
        }
      }
    } else {
      if (ch === '"') inString = true;
      repaired += ch;
    }
  }

  try {
    return JSON.parse(repaired);
  } catch (err2) {
    console.error('Repaired JSON.parse also failed:', err2.message);
    // Write out repaired for debugging
    fs.writeFileSync('upsc-aso/debug_failed_repaired.json', repaired);
    throw err2;
  }
}

async function testSingleCall() {
  const model = 'gemini-3.5-flash-lite';
  console.log(`Testing API call with model: ${model}`);
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent?key=${key}`;
  
  const prompt = `You are an aerospace engineering professor.
Return strict JSON with this exact structure:
{
  "title": "Density",
  "definition": "Density $\\\\rho = \\\\frac{m}{V}$ with units $[kg/m^3]$.",
  "derivation": "From ideal gas law, $P = \\\\rho R T \\\\implies \\\\rho = \\\\frac{P}{RT}$.",
  "questions": [
    {
      "id": 1,
      "question": "What happens to air density $\\\\rho$ as altitude increases?",
      "options": ["A. Increases", "B. Decreases exponentially", "C. Remains constant", "D. Decreases linearly"],
      "correct_index": 1,
      "explanation": "Because $P$ and $T$ drop in the troposphere, $\\\\rho$ decreases exponentially according to the barometric formula."
    }
  ]
}

CRITICAL: Escape all LaTeX backslashes with double backslashes (\\\\rho, \\\\frac, \\\\implies). Return raw JSON only.`;

  const res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      contents: [{ parts: [{ text: prompt }] }],
      generationConfig: {
        responseMimeType: 'application/json',
        temperature: 0.2
      }
    })
  });

  const data = await res.json();
  const rawText = data.candidates[0].content.parts[0].text;
  console.log('Raw text snippet:', rawText.slice(0, 200));

  const parsed = sanitizeAndParseJson(rawText);
  console.log('Successfully parsed! Keys:', Object.keys(parsed));
  console.log('Definition:', parsed.definition);
  console.log('Derivation:', parsed.derivation);
}

testSingleCall().catch(console.error);
