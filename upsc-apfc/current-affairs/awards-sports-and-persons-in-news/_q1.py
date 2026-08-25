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

ins('January', [
 I("Who won the Best Debut category at the Ramnath Goenka Sahitya Samman 2025 for 'The Many Lives of Syeda X'?",
   ["Neha Dixit", "Subi Taba", "Shinie Antony", "Namita Gokhale"], 0,
   "Neha Dixit won Best Debut; Subi Taba took Best Fiction and Sudeep Chakravarti Best Non-Fiction."),
 I("The Ramnath Goenka Best Non-Fiction prize went to Sudeep Chakravarti for which book?",
   ["Fallen City", "Tales from the Dawn-Lit Mountains", "Eden Abandoned", "Mother Mary Comes to Me"], 0,
   "Sudeep Chakravarti won Best Non-Fiction for 'Fallen City'."),
 I("Subi Taba won the Ramnath Goenka Best Fiction award 2025 for:",
   ["Tales from the Dawn-Lit Mountains", "The Many Lives of Syeda X", "Fallen City", "Eden Abandoned"], 0,
   "Subi Taba won for 'Tales from the Dawn-Lit Mountains'."),
 I("Who received the Bhartendu Harishchandra Lifetime Achievement Award (January 2026)?",
   ["Namita Gokhale", "Chandrashekhara Kambara", "Shinie Antony", "Ilaiyaraaja"], 0,
   "Namita Gokhale received the Bhartendu Harishchandra Lifetime Achievement Award."),
 I("Shinie Antony won the Ruskin Bond Award for Fiction for:",
   ["Eden Abandoned: Story of Lilith", "Fallen City", "Wildflower", "Hamnet"], 0,
   "Shinie Antony won for 'Eden Abandoned: Story of Lilith'."),
 I("Major Swathi Shantha Kumar received the UN Secretary-General's Award 2025 for which initiative?",
   ["Equal Partners, Lasting Peace", "Green Borders", "Healers of Hope", "Wings of Unity"], 0,
   "She received it for 'Equal Partners, Lasting Peace'."),
 I("K T Thomas was posthumously announced Padma Vibhushan (January 2026) in which field?",
   ["Public Affairs", "Art", "Science", "Sports"], 0,
   "K T Thomas was named for the Padma Vibhushan in Public Affairs."),
 I("Which music legend received the Padmapani Award at the Ajanta-Ellora International Film Festival 2026?",
   ["Ilaiyaraaja", "A.R. Rahman", "Lata Mangeshkar", "Shankar Mahadevan"], 0,
   "Ilaiyaraaja received the Padmapani Award."),
 I("Wagner Moura's 2026 Golden Globe for Best Actor (Drama) made him the first winner from:",
   ["Brazil", "Portugal", "Argentina", "Mexico"], 0,
   "He became the first Brazilian actor to win a Golden Globe for Best Actor in a Drama."),
 I("Who took charge as the first woman Chief Secretary of West Bengal on January 1, 2026?",
   ["Nandini Chakravorty", "Alka Lamba", "Leena Nair", "Girija Vaidyanathan"], 0,
   "Nandini Chakravorty became the first woman Chief Secretary of West Bengal."),
 I("Zou Jiayi (China) assumed office as President of the AIIB on January 16, 2026. AIIB stands for:",
   ["Asian Infrastructure Investment Bank", "Asian International Investment Bureau", "Africa Infrastructure Investment Bank", "Asian Innovation and Investment Board"], 0,
   "AIIB is the Asian Infrastructure Investment Bank."),
 I("Which new sport makes its Olympic debut at the Milan Cortina Winter Games 2026?",
   ["Ski Mountaineering", "Curling Mixed Doubles", "Snowboarding Big Air", "Biathlon Relay"], 0,
   "Ski Mountaineering is the newest discipline among the 8 sports and 15 disciplines.")
])

open(p, 'w', encoding='utf-8').write(c)
print('Saved. Length:', len(c))
