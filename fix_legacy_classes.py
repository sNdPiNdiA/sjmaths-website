from pathlib import Path

root = Path('.')
changed = []
for path in sorted(root.rglob('*.html')):
    text = path.read_text(encoding='utf-8')
    original = text
    text = text.replace('item": "https://sjmaths.com/classes/"', 'item": "https://sjmaths.com/"')
    text = text.replace('url": "https://sjmaths.com/classes/class-12/chapter-wise-notes/"', 'url": "https://sjmaths.com/class-12-maths/chapter-wise-notes/"')
    text = text.replace('url": "https://sjmaths.com/classes/class-12/ncert-exercise-practice/"', 'url": "https://sjmaths.com/class-12-maths/ncert-exercise-practice/"')
    text = text.replace('contentUrl": "https://sjmaths.com/classes/live-class.html"', 'contentUrl": "https://sjmaths.com/"')
    if text != original:
        path.write_text(text, encoding='utf-8')
        changed.append(str(path))

print('changed', len(changed))
for p in changed:
    print(p)
