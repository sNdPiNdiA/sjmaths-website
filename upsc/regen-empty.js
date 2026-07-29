/**
 * Regenerate specific Prehistory topics with proper await
 */
import fs from 'fs';
import path from 'path';

if (fs.existsSync('.env')) {
    const envConfig = fs.readFileSync('.env', 'utf8');
    envConfig.split('\n').forEach(line => {
        const [key, value] = line.split('=');
        if (key && value) process.env[key.trim()] = value.trim();
    });
}

import {
    generatePrompt,
    parseResponse,
    normalizeContent,
    translateToBilingual,
    generateSha256Hash,
    PageScorer,
    GeminiClient,
    assemblePage,
    createManifest,
    DEFAULT_GLOSSARY,
} from './upsc-microtopic-template.js';

const apiKey = process.env.GEMINI_API_KEY;

const targetDirs = [
    'Sources-of-Information-of-Pre-History',
    'History-of-Paleolithic-or-Old-Stone-Age',
    'History-of-Mesolithic-or-Middle-Stone-Age'
];

// We can import or reuse the topic definitions from generate-all-prehistory.js
console.log('Regeneration helper ready.');
