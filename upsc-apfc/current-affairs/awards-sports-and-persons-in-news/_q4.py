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

ins('May', [
 I("How many personalities were honoured with the Padma Awards at Rashtrapati Bhavan on May 26, 2026?",
   ["66", "54", "72", "48"], 0,
   "President Murmu honoured 66 distinguished personalities."),
 I("The Pulitzer Prize 2026 for Illustrated Reporting and Commentary (Bloomberg) was shared by:",
   ["R.K. Anand, Suparna Sharma & Natalie Obiko Pearson", "Barkha Dutt & Shekhar Gupta", "Ravish Kumar & Rajdeep Sardesai", "Sukumar Ranganathan & A.K. Bhattacharya"], 0,
   "The Bloomberg trio won the Pulitzer in this category."),
 I("Two Indian peacekeepers received the Dag Hammarskjold Medal posthumously. Their missions were:",
   ["MONUSCO (DR Congo) and UNMISS (South Sudan)", "UNIFIL (Lebanon) and MINUSMA (Mali)", "UNDOF (Golan Heights) and UNAMID (Darfur)", "UNPROFOR (Balkans) and UNTAES"], 0,
   "Lance Havildar Harbhajan Singh served with MONUSCO; Naib Subedar Sujit Kumar Pradhan with UNMISS."),
 I("How many nursing professionals received the National Florence Nightingale Awards 2026?",
   ["15", "10", "12", "20"], 0,
   "15 nursing professionals were honoured; the award was instituted in 1973."),
 I("Karnataka Grameena Bank won a PFRDA National Award for excellence in:",
   ["Atal Pension Yojana enrolment", "PMJDY accounts", "Mudra lending", "PPF collections"], 0,
   "It won for outstanding APY enrolment performance."),
 I("Soma Mandal won the Cambridge Dedicated Teacher Awards 2026 (South Asia) for:",
   ["Environmental education", "Mathematics teaching", "Digital learning tools", "Special education"], 0,
   "She was the South Asia regional winner for environmental education."),
 I("Indian students won the Earth Prize 2026 for an innovation called Plas-Stick that tackles:",
   ["Plastic pollution", "Air pollution", "Water scarcity", "E-waste"], 0,
   "Plas-Stick is an innovative solution to plastic pollution."),
 I("In the SAFF Women's Championship 2026 final (June 6, Fatorda), India beat:",
   ["Bangladesh 3-1", "Nepal 2-0", "Pakistan 4-0", "Sri Lanka 5-1"], 0,
   "India defeated Bangladesh 3-1 for a 6th title, ending a 7-year wait."),
 I("Who became the first Indian to win the Russia Grand Sand Master Cup 2026?",
   ["Sudarsan Pattnaik", "Manas Sahoo", "Srinivas Pitko", "Rahul Arya"], 0,
   "Odisha's Sudarsan Pattnaik won at the II International Festival of Sand Sculpture (June 11)."),
 I("The UN FAO honoured a Tamil Nadu farmer as a Soil Farmer Hero for:",
   ["Sustainable farming", "Record yield", "Organic exports", "Agri-tech startup"], 0,
   "The farmer was recognised for sustainable farming practices.")
])

ins('June', [
 I("The FIFA World Cup 2026 featured how many teams?",
   ["48", "32", "40", "24"], 0,
   "The 23rd edition expanded to 48 teams across USA, Canada and Mexico (June 11 - July)."),
 I("World No Tobacco Day Awards 2026 were conferred by:",
   ["WHO", "UNICEF", "UNESCO", "FAO"], 0,
   "WHO recognised leaders in tobacco control."),
 I("Harbhajan Singh and Sujit Kumar Pradhan were honoured on International Day of UN Peacekeepers with the:",
   ["Dag Hammarskjold Medal", "UN Medal of Honour", "Blue Helmet Award", "Kofi Annan Peace Prize"], 0,
   "They received Dag Hammarskjold Medals on May 29."),
 I("Which chess icon participated in Norway Chess 2026?",
   ["Magnus Carlsen", "Viswanathan Anand", "Gukesh Dommaraju", "Hikaru Nakamura"], 0,
   "Magnus Carlsen featured in the notable June chess event."),
 I("Monaco GP winner Kimi Antonelli drives for which team and holds which nationality?",
   ["Mercedes; Italian", "Ferrari; Italian", "McLaren; British", "Red Bull; Dutch"], 0,
   "The Italian Mercedes driver dominated at Monte Carlo."),
 I("The SAFF Women's Championship 2026 final was played at:",
   ["Fatorda Stadium, Goa", "Salt Lake Stadium, Kolkata", "JLN Stadium, Delhi", "Kanteerava, Bengaluru"], 0,
   "India beat Bangladesh 3-1 at Fatorda Stadium."),
 I("India's first Men's U18 Asia Cup hockey title was sealed at:",
   ["Kakamigahara, Japan", "Muscat, Oman", "Jakarta, Indonesia", "Dhaka, Bangladesh"], 0,
   "India beat Japan 4-1 in the final at Kakamigahara."),
 I("Which team was the runner-up at the FIFA World Cup 2026?",
   ["Argentina", "France", "Brazil", "England"], 0,
   "Spain beat Argentina 1-0 after extra time in the final."),
 I("The FIFA World Cup 2026 title was Spain's:",
   ["Third World Cup win", "First World Cup win", "Second World Cup win", "Fourth World Cup win"], 0,
   "Spain's third crown came in the tournament's 23rd edition."),
 I("The French Open 2026 (Roland Garros) is hosted in which city?",
   ["Paris", "Lyon", "Marseille", "Nice"], 0,
   "Roland Garros is played in Paris each May-June.")
])

open(p, 'w', encoding='utf-8').write(c)
print('Saved. Length:', len(c))
