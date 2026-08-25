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

ins('July', [
 I("Spain's 2026 FIFA World Cup triumph was the nation's:",
   ["Third World Cup title", "First World Cup title", "Second World Cup title", "Fourth World Cup title"], 0,
   "Spain's third crown followed wins in 2010 and the Nations League era rise."),
 I("Commonwealth Games 2026 host city Glasgow is in:",
   ["Scotland", "England", "Wales", "Australia"], 0,
   "Glasgow, Scotland hosted CWG 2026."),
 I("The 2026 FIFA World Cup was which edition of the tournament?",
   ["23rd", "22nd", "21st", "24th"], 0,
   "It was the 23rd edition and the first with 48 teams."),
 I("The honour conferred on PM Modi by Indonesia in July 2026 was its:",
   ["Highest civilian honour", "Highest military honour", "Top cultural award", "Parliamentary medal"], 0,
   "The Indonesian President conferred Indonesia's highest civilian honour."),
 I("Wimbledon 2026 is played at:",
   ["All England Club, London", "Roland Garros, Paris", "Flushing Meadows, New York", "Melbourne Park"], 0,
   "Wimbledon is held at the All England Lawn Tennis Club in London."),
 I("Consider: (1) WC2026 had 48 teams (2) It was hosted by three countries (3) Spain won a record 4th title. Correct statements:",
   ["1 and 2 only", "2 and 3 only", "1 and 3 only", "All three"], 0,
   "48 teams and tri-nation hosting are correct; it was Spain's third title, not fourth."),
 I("Wimbledon's traditional court surface is:",
   ["Grass", "Clay", "Hard court", "Carpet"], 0,
   "Wimbledon is the grass-court Grand Slam."),
 I("In the WC2026 final, Spain defeated:",
   ["Argentina", "France", "Portugal", "Brazil"], 0,
   "Argentina fell 0-0 in regulation before Spain won 1-0 in extra time."),
 I("The Commonwealth Games 2026 commenced in which month?",
   ["July", "June", "August", "May"], 0,
   "CWG 2026 began in July in Glasgow."),
 I("PM Modi's Indonesian honour recognised primarily:",
   ["India-Indonesia bilateral ties", "Cricket diplomacy", "Bollywood exports", "Climate funding"], 0,
   "It recognised strengthening India-Indonesia bilateral ties.")
])

ins('August', [
 I("The Arjuna Award (Lifetime) 2025 for Football went to:",
   ["I. Arumainayagam", "Sunil Chhetri", "Bhaichung Bhutia", "IM Vijayan"], 0,
   "I. Arumainayagam received the Arjuna Award (Lifetime) for Football."),
 I("Who among these received the Dronacharya Award (Regular) 2025 for Shooting?",
   ["Neha Nandkumar Chavan", "Virender Kumar", "Dharmendra Singh Yadav", "Parveer Singh"], 0,
   "Chavan (Shooting) joined Parveer Singh (Athletics) and Chhote Lal Yadav (Boxing) as Regular Dronacharya awardees."),
 I("The Dronacharya Award (Lifetime) 2025 for Wrestling went to:",
   ["Virender Kumar", "Mahavir Singh Phogat", "Satpal Singh", "Yashvir Singh"], 0,
   "Virender Kumar (Wrestling) and Dharmendra Singh Yadav (Boxing) got Lifetime Dronacharya awards."),
 I("Rashtriya Khel Protsahan Puraskar 2025 was given to:",
   ["Army Paralympic Node, Pune", "SAI Bengaluru Centre", "Navy Rowing Academy", "Air Force Sports Board"], 0,
   "The Army Paralympic Node, Pune received the honour."),
 I("India's maiden overall title at the Commonwealth Fencing Championship 2026 came at:",
   ["Lagos - 35 medals incl. 3 gold on Day 3", "London - 20 medals", "Delhi - 28 medals", "Kuala Lumpur - 30 medals"], 0,
   "India won 35 medals across U23 & Senior divisions in Lagos."),
 I("The Badminton World Championships 2026 were held at:",
   ["Indira Gandhi Indoor Stadium, New Delhi", "Hyderabad's Gachibowli", "Pune's Shiv Chhatrapati", "Chennai's Nehru Indoor"], 0,
   "Treesa Jolly & Gayatri Gopichand reached the Women's Doubles semifinals (Aug 21)."),
 I("Ashish Yadav's silver at World Athletics U20 came in Javelin with a throw of:",
   ["74.09m", "78.02m", "71.55m", "80.11m"], 0,
   "He threw 74.09m for silver; Shahnavaz Khan took long jump bronze."),
 I("Ariha Pangambam created history by winning India's first senior women's individual gold in:",
   ["Aerobic Gymnastics (Asian Championships)", "Rhythmic Gymnastics (Worlds)", "Artistic Swimming (Asiad)", "Trampoline (Asian Indoors)"], 0,
   "The Manipur gymnast won at the Asian Aerobic Gymnastics Championships in the Philippines."),
 I("India's double gold at the Asian Junior Blitz Chess Championship (Aug 17) came from:",
   ["Vignesh Vermula & Saranya Devi", "Praggnanandhaa & Divya", "Nihal Sarin & Vaishali", "Arjun Erigaisi & Humpy"], 0,
   "Vermula won Open gold and Saranya Devi the Girls' gold."),
 I("FIFA's Women's World Cup schedule released Aug 20 covers how many matches for the 10th edition?",
   ["64 matches, June 24 - July 25 next year", "52 matches, June 10 - July 10", "48 matches, August window", "72 matches, May-June"], 0,
   "The 64-match schedule runs June 24 to July 25 next year.")
])

open(p, 'w', encoding='utf-8').write(c)
print('Saved. Length:', len(c))
