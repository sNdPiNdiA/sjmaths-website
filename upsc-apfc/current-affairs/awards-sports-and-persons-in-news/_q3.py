p = r'C:\Users\sande\Documents\GitHub\sjmaths-website\upsc-apfc\current-affairs\awards-sports-and-persons-in-news\index.html'
c = open(p, encoding='utf-8').read()
qi = c.find('MONTHLY QUIZ BANK')
assert qi > 0

def ins(month, items):
    global c
    mi = c.find('      ' + month + ': [', qi)
    pos = c.find('\n      ]', mi)
    assert 0 < mi < pos, (month, mi, pos)
    block = ',\n' + ',\n'.join(items)
    c = c[:pos] + block + c[pos:]
    print(month, '+', len(items))

def I(q, o, a, ex):
    return ('        { q: "' + q + '",\n          o: [' +
            ', '.join('"' + x + '"' for x in o) + '], a: ' + str(a) +
            ',\n          ex: "' + ex + '" }')

ins('April', [
 I("Who were named the Asian Squash Federation Players of the Year 2025?",
   ["Anahat Singh (Girls) and Abhay Singh (Men)", "Joshna Chinappa and Saurav Ghosal", "Dipika Pallikal and Harinder Sandhu", "Tanvi Khanna and Vikram Malhotra"], 0,
   "Anahat Singh and Abhay Singh received the ASF Player of the Year awards."),
 I("David J. Gross received the 2026 Special Breakthrough Prize in:",
   ["Fundamental Physics", "Life Sciences", "Mathematics", "Chemistry"], 0,
   "David J. Gross won the Special Breakthrough Prize in Fundamental Physics."),
 I("How many grassroots activists received the Goldman Environmental Prize 2026?",
   ["Six", "Four", "Eight", "Ten"], 0,
   "Six grassroots activists won the Goldman Environmental Prize 2026."),
 I("The Machhli National Award for wildlife conservation went to:",
   ["Anita Chaudhary", "Krithi K. Karanth", "Parveen Shaikh", "Belinda Wright"], 0,
   "Anita Chaudhary received the Machhli National Award."),
 I("Dr. Ch. Srinivasa Rao received the 9th Prof. M.S. Swaminathan Award (2024-25) for work in:",
   ["Climate-resilient agriculture", "Nuclear physics", "Vaccine research", "Space farming"], 0,
   "He won for contributions to climate-resilient agriculture."),
 I("N. Alim Yusuf won a WWF National Award for an AI application called:",
   ["NeophyteID", "WildScan", "FaunaAI", "EcoLens"], 0,
   "His AI app NeophyteID supports conservation efforts."),
 I("Basant Kumar won the Ramnath Goenka award (Broadcast/Digital) for:",
   ["Uncovering India Invisible", "The Silent Valley Files", "Border Diaries", "Metro Voices"], 0,
   "He won for Uncovering India Invisible."),
 I("Which police force received the President of India's Police Colour in April 2026?",
   ["Odisha Police Force", "Sikkim Police", "Delhi Police", "Kerala Police"], 0,
   "The Odisha Police Force received the President's Police Colour for law enforcement."),
 I("Which three units topped the AB PM-JAY Pre-authorisation Approval awards?",
   ["Uttarakhand, Goa, J&K", "Bihar, UP, MP", "Punjab, Haryana, HP", "Assam, Odisha, Bengal"], 0,
   "Uttarakhand, Goa and Jammu & Kashmir were top performers."),
 I("Infosys signed Carlos Alcaraz as global brand ambassador (Apr 16). Its AI platform powering his performance is:",
   ["Infosys Topaz", "Infosys Cobalt", "Infosys Meridian", "Infosys Aster"], 0,
   "Infosys Topaz AI powers his tennis performance analytics."),
 I("Ayush Shetty won which medal at the Badminton Asia Championships, Ningbo?",
   ["Silver", "Gold", "Bronze", "None"], 0,
   "Ayush Shetty won silver at Ningbo.")
])

open(p, 'w', encoding='utf-8').write(c)
print('Saved. Length:', len(c))
