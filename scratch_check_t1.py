with open('up-upper-primary-teacher/mathematics/natural-and-whole-numbers/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = c.find('Natural Numbers')
print(c[idx-400:idx+200])
