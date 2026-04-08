import os
import re

root = os.path.abspath(os.path.dirname(__file__))
legacy_pattern = re.compile(r'href=["\'](?:/classes/|classes/)|https?://(?:www\.)?sjmaths\.com/classes/')
bad_meta_pattern = re.compile(r'linkrel=|metaname=|metaproperty=', re.IGNORECASE)

with open('cleanup_candidates.txt', 'w', encoding='utf-8') as out:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in {'.git', 'node_modules', '.firebase', '.vscode'}]
        for fn in filenames:
            if fn.endswith(('.html', '.js')):
                fp = os.path.join(dirpath, fn)
                try:
                    txt = open(fp, 'r', encoding='utf-8', errors='ignore').read()
                except Exception:
                    continue
                if legacy_pattern.search(txt):
                    out.write('legacy:' + fp + '\n')
            if fn.endswith('.html'):
                fp = os.path.join(dirpath, fn)
                try:
                    txt = open(fp, 'r', encoding='utf-8', errors='ignore').read()
                except Exception:
                    continue
                if bad_meta_pattern.search(txt):
                    out.write('badmeta:' + fp + '\n')
