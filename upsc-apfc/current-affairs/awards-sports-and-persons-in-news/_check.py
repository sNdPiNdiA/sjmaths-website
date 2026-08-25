fpath = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()
print('File loaded:', len(c))
print('QUIZZES marker:', c.find('MONTHLY QUIZ BANK'))
print('PREMIUM APP LOGIC:', c.find('PREMIUM APP LOGIC'))
