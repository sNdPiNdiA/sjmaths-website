#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs, json

INDEX = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
JSON_FILE = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\_quiz_data.json'

with codecs.open(INDEX, 'r', encoding='utf-8') as f:
    c = f.read()

with codecs.open(JSON_FILE, 'r', encoding='utf-8') as f:
    questions = json.load(f)

lines = []
lines.append('    /* ================= MONTHLY QUIZ BANK (15+ UPSC-style MCQs per month) ================= */')
lines.append('    const QUIZZES = {')
for month, qlist in questions.items():
    lines.append('      ' + month + ': [')
    for i, item in enumerate(qlist):
        comma = ',' if i < len(qlist) - 1 else ''
        o_str = ', '.join('"' + opt.replace('"', '\\"') + '"' for opt in item['o'])
        q_str = item['q'].replace('"', '\\"')
        ex_str = item['ex'].replace('"', '\\"')
        lines.append('        { q: "' + q_str + '",')
        lines.append('          o: [' + o_str + '], a: ' + str(item['a']) + ',')
        lines.append('          ex: "' + ex_str + '" }' + comma)
    lines.append('      ],')
lines.append('    };')
lines.append('')

new_quiz_js = '\n'.join(lines)

start_marker = '/* ================= MONTHLY QUIZ BANK'
end_marker = '    };\n\n    /* ================= PREMIUM APP LOGIC */'

s = c.find(start_marker)
e = c.find(end_marker, s) + len('    };\n')

if s < 0 or e < 0:
    print('ERROR: markers not found')
    print('start:', s, 'end:', e)
else:
    c = c[:s] + new_quiz_js + c[e:]
    with codecs.open(INDEX, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Quiz bank replaced!')
    print('New file length:', len(c))
    print('Total questions:', sum(len(v) for v in questions.values()))
