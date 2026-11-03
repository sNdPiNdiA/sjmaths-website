import path from 'node:path';

export function createReferenceUpdater(mapping, fileHashes) {
    const patterns = Object.keys(mapping).map(original => {
        const minified = mapping[original];
        const hash = fileHashes[minified] || 'default';
        const ext = path.extname(original);
        const baseName = original.slice(0, -ext.length);
        const escapedBase = baseName.replace(/\./g, '\\.');
        const escapedExt = ext.replace(/\./g, '\\.');
        return {
            baseName, key: baseName.replace(/^\.\//, ''), minified, hash,
            regex: new RegExp('(\\/?|\\.\\/|\\.\\.\\/)' + escapedBase + '(\\.min)?' + escapedExt + '(\\?v=[a-zA-Z0-9\\.]*)?', 'g'),
        };
    });
    // Detect relevant assets once, rather than scanning each large lesson for
    // every unrelated source. Keep original replacement order and URL semantics.
    const keys = [...new Set(patterns.map(pattern => pattern.key))].sort((a, b) => b.length - a.length);
    const escape = value => value.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const detector = keys.length ? new RegExp(keys.map(escape).join('|'), 'g') : null;
    const containedKeys = new Map(keys.map(key => [key, keys.filter(candidate => key.includes(candidate))]));
    return content => {
        if (!detector) return content;
        const detected = new Set([...content.matchAll(detector)].map(match => match[0]));
        const candidates = new Set([...detected].flatMap(key => containedKeys.get(key)));
        for (const { baseName, key, regex, minified, hash } of patterns) {
            // The includes check retains the original ./vendor alias behaviour.
            if (!candidates.has(key) || !content.includes(baseName)) continue;
            content = content.replace(regex, (match, prefix) => `${prefix}${minified}?v=${hash}`);
        }
        return content;
    };
}
