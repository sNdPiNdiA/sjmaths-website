import { readFileSync, readdirSync } from 'fs';
import { join } from 'path';

const baseDir = "C:/Users/sande/Documents/GitHub/sjmaths-website/learning/topics/foundations";

const topicFiles = [];
function walk(dir) {
    const entries = readdirSync(dir, { withFileTypes: true });
    for (const entry of entries) {
        const full = join(dir, entry.name);
        if (entry.isDirectory()) {
            walk(full);
        } else if (entry.name.endsWith('.json')) {
            topicFiles.push(full);
        }
    }
}
walk(baseDir);

for (const fullPath of topicFiles) {
    try {
        const raw = readFileSync(fullPath, 'utf8');
        const content = JSON.parse(raw.replace(/^\uFEFF/, ''));
        const qts = content.question_types || [];
        if (qts.length === 0) continue;

        const shortName = fullPath.replace(baseDir, '').replace(/\\/g, '/');
        console.log(`### ${content.topic?.title || shortName}`);
        console.log(`  FILE: ${shortName}`);
        console.log(`  ID: ${content.topic?.id}`);
        for (const t of qts) {
            const poolSize = t.pool?.length || 0;
            const target = poolSize >= 6 ? 0 : (6 - poolSize);
            console.log(`  TYPE: ${t.type_id} | ${t.type_title} | POOL: ${poolSize} | ADD: ${target}`);
        }
        console.log('');
    } catch (e) {
        console.log(`  ERROR in ${fullPath}: ${e.message}`);
    }
}