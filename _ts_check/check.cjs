const ts = require('typescript');
const fs = require('fs');
const p = process.argv[2];
const s = fs.readFileSync(p, 'utf8');
for (const kind of ['JS', 'TS']) {
    const sf = ts.createSourceFile('gen.' + kind.toLowerCase(), s, ts.ScriptTarget.Latest, true,
        kind === 'JS' ? ts.ScriptKind.JS : ts.ScriptKind.TS);
    const diags = ts.getPreEmitDiagnostics ? sf.parseDiagnostics : [];
    const list = (sf.parseDiagnostics || []).filter(d => d.code !== 0);
    console.log('--- ' + kind + ' parse diagnostics: ' + list.length);
    list.forEach(d => {
        const lc = sf.getLineAndCharacterOfPosition(d.start);
        console.log('   ' + d.code + ' @ ' + (lc.line + 1) + ':' + (lc.character + 1) + ' -> ' +
            ts.flattenDiagnosticMessageText(d.messageText, ' '));
    });
}
