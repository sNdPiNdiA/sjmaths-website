// Independent pre-optimization oracle, used only for tests/measurement.
import path from 'node:path';
export function legacyReferenceUpdater(mapping, fileHashes) {
    const patterns = Object.keys(mapping).map(original => {
        const minified = mapping[original], ext = path.extname(original);
        const baseName = original.slice(0, -ext.length);
        return { baseName, minified, hash: fileHashes[minified] || 'default',
            regex: new RegExp('(\\/?|\\.\\/|\\.\\.\\/)' + baseName.replace(/\./g, '\\.') + '(\\.min)?' + ext.replace(/\./g, '\\.') + '(\\?v=[a-zA-Z0-9\\.]*)?', 'g') };
    });
    return content => {
        for (const { baseName, regex, minified, hash } of patterns) {
            if (!content.includes(baseName)) continue;
            content = content.replace(regex, (match, prefix) => `${prefix}${minified}?v=${hash}`);
        }
        return content;
    };
}
