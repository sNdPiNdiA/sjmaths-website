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

ins('February', [
 I("At the 68th Grammy Awards, the Song of the Year went to:",
   ["Billie Eilish - Wildflower", "Bad Bunny - DeBI TiRAR MaS FOToS", "Kendrick Lamar & SZA - Luther", "Olivia Dean"], 0,
   "Billie Eilish won Song of the Year for 'Wildflower'."),
 I("Which artists won the Record of the Year Grammy for 'Luther'?",
   ["Kendrick Lamar & SZA", "Billie Eilish & FINNEAS", "Bruno Mars & Lady Gaga", "Sabrina Carpenter"], 0,
   "Kendrick Lamar & SZA won Record of the Year."),
 I("Who won the Best New Artist Grammy at the 68th awards?",
   ["Olivia Dean", "Chappell Roan", "Gracie Abrams", "Benson Boone"], 0,
   "Olivia Dean won Best New Artist."),
 I("Arundhati Roy won the Mathrubhumi Book of the Year 2026 for:",
   ["Mother Mary Comes to Me", "The God of Small Things", "Ministry of Utmost Happiness", "My Seditious Heart"], 0,
   "She won for 'Mother Mary Comes to Me' (Rs 2 lakh prize)."),
 I("Victoria Beckham was made a Knight of the Order of Arts and Letters by:",
   ["France", "Britain", "Italy", "Spain"], 0,
   "France's Ministry of Culture conferred the honour."),
 I("Our Lady of Grace Cathedral, Vasai received an Award of Merit under which UNESCO programme?",
   ["Asia-Pacific Awards for Cultural Heritage Conservation", "World Heritage List", "Creative Cities Network", "Memory of the World"], 0,
   "It received the Award of Merit in the 2025 UNESCO Asia-Pacific Heritage Awards."),
 I("Isha Foundation instituted which new national honour?",
   ["Bhavya Bharat Bhushan Award", "Bharat Gaurav Samman", "Rashtra Seva Puraskar", "Bharat Shanti Medal"], 0,
   "The 'Bhavya Bharat Bhushan Award' covers national security, arts, science and literature."),
 I("The 22nd Upendra Nath Brahma 'Soldier of Humanity' Award 2025 went to:",
   ["Gyalyum Ashi Dorji Wangmo Wangchuck", "Sonam Wangchuk", "Tenzin Gyatso", "Annie Raja"], 0,
   "The Queen Mother of Bhutan received the award."),
 I("Where was the 6th National Rafting Championship (Feb 19-22) held?",
   ["Shibnote, Doda on the Chenab River, J&K", "Rishikesh on the Ganga", "Coorg on the Barapole", "Zanskar River, Ladakh"], 0,
   "It was organised by J&K Tourism and Doda Administration at Shibnote, Doda."),
 I("India's medal haul at the Asian Boxing U15 Championships, Tashkent was:",
   ["27 medals including 9 gold", "20 medals including 5 gold", "15 medals including 7 gold", "30 medals including 12 gold"], 0,
   "India won 27 medals (9 gold); the girls' team topped with 7 gold."),
 I("Dr. Bhargav Mallappa received the royal honour of 'Dato' from:",
   ["Kerajaan Kutai Mulawarman, Indonesia", "Sultan of Johor, Malaysia", "King of Thailand", "Brunei Darussalam"], 0,
   "The Indonesian royal house of Kutai Mulawarman conferred the 'Dato' title.")
])

open(p, 'w', encoding='utf-8').write(c)
print('Saved. Length:', len(c))
