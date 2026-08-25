import re

fpath = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
with open(fpath, 'r', encoding='utf-8') as f:
    c = f.read()

# Find the QUIZZES section - from the comment to the closing };
start_marker = '/* ================= MONTHLY QUIZ BANK'
end_marker = '    };\n\n    /* ================= PREMIUM APP LOGIC */'

s = c.find(start_marker)
e = c.find(end_marker, s) + len('    };\n')

# Read the new quiz content from a separate file
import os
quiz_file = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\_quiz_new.txt'
with open(quiz_file, 'r', encoding='utf-8') as f:
    new_quiz = f.read()

c = c[:s] + new_quiz + c[e:]

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(c)

print('Quiz section replaced successfully')
print('New file length:', len(c))
