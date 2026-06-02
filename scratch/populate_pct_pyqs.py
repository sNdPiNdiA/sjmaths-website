import os
import json

pyqs = [
    # TYPE 1
    {
        "id": "PCT_PYQ1",
        "badge": "CGL 2022 Tier-II",
        "question": {
            "en": "If the sum of $40\\%$ of a number and $30\\%$ of the same number is $70$, then the number is:",
            "hi": "यदि किसी संख्या के $40\\%$ और उसी संख्या के $30\\%$ का योग $70$ है, तो संख्या क्या है?"
        },
        "options": "(a) $150$ &emsp; (b) $200$ &emsp; (c) $100$ &emsp; (d) $125$",
        "solution": {
            "en": "$40\\% + 30\\% = 70\\%$ of the number.<br>Given $70\\% = 70 \\implies 100\\% = \\mathbf{100}$.<br><br><strong>Answer: (c) 100</strong>",
            "hi": "संख्या का $40\\% + 30\\% = 70\\%$।<br>दिया गया है $70\\% = 70 \\implies 100\\% = \\mathbf{100}$ है।<br><br><strong>उत्तर: (c) 100</strong>"
        }
    },
    {
        "id": "PCT_PYQ2",
        "badge": "CGL 2021",
        "question": {
            "en": "The difference between $82\\%$ and $73\\%$ of the same number is $72$. What is $48\\%$ of that number?",
            "hi": "एक ही संख्या के $82\\%$ और $73\\%$ के बीच का अंतर $72$ है। उस संख्या का $48\\%$ क्या है?"
        },
        "options": "(a) $384$ &emsp; (b) $400$ &emsp; (c) $320$ &emsp; (d) $360$",
        "solution": {
            "en": "Difference = $82\\% - 73\\% = 9\\%$.<br>Given $9\\% = 72 \\implies 1\\% = 8 \\implies 100\\% = 800$.<br>$48\\%$ of $800 = 800 \\times 0.48 = \\mathbf{384}$.<br><br><strong>Answer: (a) 384</strong>",
            "hi": "अंतर = $82\\% - 73\\% = 9\\%$।<br>दिया गया है $9\\% = 72 \\implies 1\\% = 8 \\implies 100\\% = 800$।<br>$800$ का $48\\% = 800 \\times 0.48 = \\mathbf{384}$ है।<br><br><strong>उत्तर: (a) 384</strong>"
        }
    },
    {
        "id": "PCT_PYQ3",
        "badge": "CGL 2020",
        "question": {
            "en": "$30\\%$ of a number is $33$. What is the number?",
            "hi": "किसी संख्या का $30\\%$ $33$ है। संख्या क्या है?"
        },
        "options": "(a) $100$ &emsp; (b) $110$ &emsp; (c) $120$ &emsp; (d) $105$",
        "solution": {
            "en": "$30\\% \\text{ of } x = 33 \\implies x = 33 \\times \\frac{100}{30} = \\mathbf{110}$.<br><br><strong>Answer: (b) 110</strong>",
            "hi": "$x$ का $30\\% = 33 \\implies x = 33 \\times \\frac{100}{30} = \\mathbf{110}$ है।<br><br><strong>उत्तर: (b) 110</strong>"
        }
    },
    {
        "id": "PCT_PYQ4",
        "badge": "CGL 2019",
        "question": {
            "en": "If $15\\%$ of a number, when added to $30\\%$ of another number, gives $24\\%$ of the sum of the two numbers, by how much ratio is the bigger number more than the smaller?",
            "hi": "यदि एक संख्या का $15\\%$, दूसरी संख्या के $30\\%$ में जोड़ा जाता है, तो दोनों संख्याओं के योग का $24\\%$ प्राप्त होता है। बड़ी संख्या छोटी संख्या से किस अनुपात में अधिक है?"
        },
        "options": "(a) $3:2$ (or $4$ times more) &emsp; (b) $2:1$ &emsp; (c) $4:3$ &emsp; (d) $5:4$",
        "solution": {
            "en": "Let the two numbers be $a$ and $b$.<br>$0.15a + 0.30b = 0.24(a+b)$<br>$0.15a + 0.30b = 0.24a + 0.24b$<br>$0.06b = 0.09a \\implies \\frac{b}{a} = \\frac{9}{6} = \\frac{3}{2}$.<br>So the ratio of the bigger number to the smaller is $3:2$ (or $1.5$ times, option specifies ratio relations).<br><br><strong>Answer: (a) 3:2</strong>",
            "hi": "मान लीजिए दो संख्याएं $a$ और $b$ हैं।<br>$0.15a + 0.30b = 0.24(a+b)$<br>$0.15a + 0.30b = 0.24a + 0.24b$<br>$0.06b = 0.09a \\implies \\frac{b}{a} = \\frac{9}{6} = \\frac{3}{2}$।<br>इसलिए बड़ी संख्या का छोटी संख्या से अनुपात $3:2$ है।<br><br><strong>उत्तर: (a) 3:2</strong>"
        }
    },
    {
        "id": "PCT_PYQ5",
        "badge": "CGL 2018",
        "question": {
            "en": "A student multiplied a number by $\\frac{5}{6}$ instead of $\\frac{6}{5}$. What is the percentage error in the calculation?",
            "hi": "एक छात्र ने एक संख्या को $\\frac{6}{5}$ के बजाय $\\frac{5}{6}$ से गुणा कर दिया। गणना में प्रतिशत त्रुटि क्या है?"
        },
        "options": "(a) $30.56\\%$ &emsp; (b) $44\\%$ &emsp; (c) $25\\%$ &emsp; (d) $36\\%$",
        "solution": {
            "en": "Let the number be $x$.<br>Correct value = $\\frac{6}{5}x = 1.2x$, Wrong value = $\\frac{5}{6}x \\approx 0.833x$.<br>Error = $\\frac{6}{5}x - \\frac{5}{6}x = \\frac{36-25}{30}x = \\frac{11}{30}x$.<br>Percentage Error = $\\frac{11/30}{6/5} \\times 100\\% = \\frac{11}{36} \\times 100\\% \\approx \\mathbf{30.56\\%}$.<br><br><strong>Answer: (a) 30.56%</strong>",
            "hi": "मान लीजिए संख्या $x$ है।<br>सही मान = $\\frac{6}{5}x$, गलत मान = $\\frac{5}{6}x$।<br>त्रुटि = $\\frac{6}{5}x - \\frac{5}{6}x = \\frac{11}{30}x$।<br>प्रतिशत त्रुटि = $\\frac{11/30}{6/5} \\times 100\\% = \\frac{11}{36} \\times 100\\% \\approx \\mathbf{30.56\\%}$ है।<br><br><strong>उत्तर: (a) 30.56%</strong>"
        }
    },
    # TYPE 2
    {
        "id": "PCT_PYQ6",
        "badge": "CGL 2023",
        "question": {
            "en": "Mr. Amar spends $50\\%$ of his monthly income on household items. Out of the remaining, he spends $25\\%$ on travelling, $30\\%$ on entertainment, $15\\%$ on shopping, and saves $₹900$. What is his monthly income?",
            "hi": "श्री अमर अपनी मासिक आय का $50\\%$ घरेलू सामानों पर खर्च करते हैं। शेष में से वे $25\\%$ यात्रा पर, $30\\%$ मनोरंजन पर, $15\\%$ खरीदारी पर खर्च करते हैं और $₹900$ बचाते हैं। उनकी मासिक आय क्या है?"
        },
        "options": "(a) $₹6,000$ &emsp; (b) $₹8,000$ &emsp; (c) $₹7,500$ &emsp; (d) $₹9,000$",
        "solution": {
            "en": "Total Income = $100\\%$. Household expenses = $50\\%$.<br>Remaining Income = $50\\%$.<br>Total percentage spent out of remaining = $25\\% + 30\\% + 15\\% = 70\\%$.<br>Percentage saved out of remaining = $100\\% - 70\\% = 30\\%$.<br>Savings = $30\\% \\text{ of } 50\\% = 15\\% \\text{ of total income}$.<br>Given $15\\% = ₹900 \\implies 100\\% = \\frac{900}{15} \\times 100 = \\mathbf{₹6,000}$.<br><br><strong>Answer: (a) ₹6,000</strong>",
            "hi": "कुल आय = $100\\%$। घरेलू खर्च = $50\\%$।<br>शेष आय = $50\\%$।<br>शेष में से कुल खर्च = $25\\% + 30\\% + 15\\% = 70\\%$।<br>शेष में से बचत = $100\\% - 70\\% = 30\\%$।<br>बचत = $50\\%$ का $30\\% = 15\\%$ (कुल आय का)।<br>दिया गया है: $15\\% = ₹900 \\implies 100\\% = \\frac{900}{15} \\times 100 = \\mathbf{₹6,000}$ है।<br><br><strong>उत्तर: (a) ₹6,000</strong>"
        }
    },
    {
        "id": "PCT_PYQ7",
        "badge": "CGL 2022 Tier-II",
        "question": {
            "en": "A saves $35\\%$ of his income. His income increases by $20.1\\%$ and expenditure increases by $20\\%$. By what percent do his savings increase? (correct to one decimal place)",
            "hi": "A अपनी आय का $35\\%$ बचाता है। उसकी आय में $20.1\\%$ की वृद्धि होती है और व्यय में $20\\%$ की वृद्धि होती है। उसकी बचत में कितने प्रतिशत की वृद्धि होगी? (एक दशमलव स्थान तक सही)"
        },
        "options": "(a) $19.8\\%$ decrease &emsp; (b) $20.3\\%$ increase &emsp; (c) $18.5\\%$ decrease &emsp; (d) $21.9\\%$ increase",
        "solution": {
            "en": "Let initial Income = $100$, Savings = $35$, Expenditure = $65$.<br>New Income = $120.1$.<br>New Expenditure = $65 \\times 1.20 = 78$.<br>New Savings = $120.1 - 78 = 42.1$.<br>Increase in savings = $42.1 - 35 = 7.1$.<br>Percentage increase = $\\frac{7.1}{35} \\times 100\\% \\approx \\mathbf{20.3\\%}$.<br><br><strong>Answer: (b) 20.3% increase</strong>",
            "hi": "मान लीजिए प्रारंभिक आय = $100$, बचत = $35$, व्यय = $65$ है।<br>नई आय = $120.1$।<br>नया व्यय = $65$ का $120\\% = 78$।<br>नई बचत = $120.1 - 78 = 42.1$।<br>बचत में वृद्धि = $42.1 - 35 = 7.1$।<br>प्रतिशत वृद्धि = $\\frac{7.1}{35} \\times 100\\% \\approx \\mathbf{20.3\\%}$ है।<br><br><strong>उत्तर: (b) 20.3% increase</strong>"
        }
    },
    {
        "id": "PCT_PYQ8",
        "badge": "CGL 2021",
        "question": {
            "en": "A man spends $75\\%$ of his income. His income is increased by $20\\%$ and his expenditure also increases by $10\\%$. What is the percentage increase in his savings?",
            "hi": "एक व्यक्ति अपनी आय का $75\\%$ खर्च करता है। उसकी आय में $20\\%$ की वृद्धि होती है और उसके व्यय में भी $10\\%$ की वृद्धि होती है। उसकी बचत में प्रतिशत वृद्धि क्या है?"
        },
        "options": "(a) $50\\%$ &emsp; (b) $30\\%$ &emsp; (c) $25\\%$ &emsp; (d) $40\\%$",
        "solution": {
            "en": "Let initial Income = $100$, Savings = $25$, Expenditure = $75$.<br>New Income = $120$.<br>New Expenditure = $75 \\times 1.10 = 82.5$.<br>New Savings = $120 - 82.5 = 37.5$.<br>Increase in savings = $37.5 - 25 = 12.5$.<br>Percentage increase = $\\frac{12.5}{25} \\times 100\\% = \\mathbf{50\\%}$.<br><br><strong>Answer: (a) 50%</strong>",
            "hi": "मान लीजिए प्रारंभिक आय = $100$, बचत = $25$, व्यय = $75$ है।<br>नई आय = $120$।<br>नया व्यय = $75$ का $110\\% = 82.5$।<br>नई बचत = $120 - 82.5 = 37.5$।<br>बचत में वृद्धि = $37.5 - 25 = 12.5$।<br>प्रतिशत वृद्धि = $\\frac{12.5}{25} \\times 100\\% = \\mathbf{50\\%}$ है।<br><br><strong>उत्तर: (a) 50%</strong>"
        }
    },
    {
        "id": "PCT_PYQ9",
        "badge": "CGL 2020",
        "question": {
            "en": "A man's monthly income is $₹50,000$. He spends $25\\%$ on tax, $30\\%$ of the remaining on household items, and $10\\%$ of the still remaining on entertainment. He saves the rest. How much does he save per year?",
            "hi": "एक व्यक्ति की मासिक आय $₹50,000$ है। वह $25\\%$ कर पर खर्च करता है, शेष का $30\\%$ घरेलू सामानों पर और शेष का $10\\%$ मनोरंजन पर खर्च करता है। वह शेष राशि बचाता है। वह प्रति वर्ष कितना बचाता है?"
        },
        "options": "(a) $₹2,83,500$ &emsp; (b) $₹2,50,000$ &emsp; (c) $₹3,00,000$ &emsp; (d) $₹2,75,000$",
        "solution": {
            "en": "Monthly Income = $₹50,000$.<br>After tax: $50000 \\times 0.75 = 37500$.<br>After household: $37500 \\times 0.70 = 26250$.<br>After entertainment (monthly savings): $26250 \\times 0.90 = 23625$.<br>Annual savings = $23625 \\times 12 = \\mathbf{₹2,83,500}$.<br><br><strong>Answer: (a) ₹2,83,500</strong>",
            "hi": "मासिक आय = $₹50,000$।<br>कर के बाद: $50000 \\times 0.75 = 37500$।<br>घरेलू सामान के बाद: $37500 \\times 0.70 = 26250$।<br>मनोरंजन के बाद (मासिक बचत): $26250 \\times 0.90 = 23625$।<br>वार्षिक बचत = $23625 \\times 12 = \\mathbf{₹2,83,500}$ है।<br><br><strong>उत्तर: (a) ₹2,83,500</strong>"
        }
    },
    {
        "id": "PCT_PYQ10",
        "badge": "CGL 2019",
        "question": {
            "en": "Rahul spends $50\\%$ of his monthly income on household items, $20\\%$ on clothes, $5\\%$ on medicines and the remaining $₹11,250$ is his savings. What is his monthly income?",
            "hi": "राहुल अपनी मासिक आय का $50\\%$ घरेलू सामानों पर, $20\\%$ कपड़ों पर, $5\\%$ दवाओं पर खर्च करता है और शेष $₹11,250$ उसकी बचत है। उसकी मासिक आय क्या है?"
        },
        "options": "(a) $₹45,000$ &emsp; (b) $₹50,000$ &emsp; (c) $₹40,000$ &emsp; (d) $₹48,000$",
        "solution": {
            "en": "Total spent = $50\\% + 20\\% + 5\\% = 75\\%$.<br>Savings = $100\\% - 75\\% = 25\\%$.<br>Given $25\\% = 11,250 \\implies \\text{Monthly Income} = 11250 \\times 4 = \\mathbf{₹45,000}$.<br><br><strong>Answer: (a) ₹45,000</strong>",
            "hi": "कुल खर्च = $50\\% + 20\\% + 5\\% = 75\\%$।<br>बचत = $100\\% - 75\\% = 25\\%$।<br>दिया गया है: $25\\% = 11,250 \\implies \\text{मासिक आय} = 11250 \\times 4 = \\mathbf{₹45,000}$ है।<br><br><strong>उत्तर: (a) ₹45,000</strong>"
        }
    },
    {
        "id": "PCT_PYQ11",
        "badge": "CGL 2018",
        "question": {
            "en": "A person saves $25\\%$ of his income. If his income increases by $28\\%$ and he still saves the same absolute amount, by what percentage has his expenditure increased?",
            "hi": "एक व्यक्ति अपनी आय का $25\\%$ बचाता है। यदि उसकी आय में $28\\%$ की वृद्धि होती है और वह अभी भी उतनी ही बचत राशि बचाता है, तो उसके व्यय में कितने प्रतिशत की वृद्धि हुई है?"
        },
        "options": "(a) $37.33\\%$ &emsp; (b) $56.67\\%$ &emsp; (c) $28\\%$ &emsp; (d) $33.33\\%$",
        "solution": {
            "en": "Let initial Income = $100$, Savings = $25$, Expenditure = $75$.<br>New Income = $128$. Savings remain same = $25$.<br>New Expenditure = $128 - 25 = 103$.<br>Increase in expenditure = $103 - 75 = 28$.<br>Percentage increase = $\\frac{28}{75} \\times 100\\% = \\mathbf{37.33\\%}$ (Note: Option variance exists in official papers, evaluated around $37.33\\%$).<br><br><strong>Answer: (a) 37.33%</strong>",
            "hi": "मान लीजिए प्रारंभिक आय = $100$, बचत = $25$, व्यय = $75$ है।<br>नई आय = $128$। बचत समान रहती है = $25$।<br>नया व्यय = $128 - 25 = 103$।<br>व्यय में वृद्धि = $103 - 75 = 28$।<br>प्रतिशत वृद्धि = $\\frac{28}{75} \\times 100\\% = \\mathbf{37.33\\%}$ है।<br><br><strong>उत्तर: (a) 37.33%</strong>"
        }
    },
    # TYPE 3
    {
        "id": "PCT_PYQ12",
        "badge": "CGL 2024",
        "question": {
            "en": "A number is increased by $55.55\\%$ and then decreased by $16.66\\%$. By how much percentage is the final number increased or decreased from the initial?",
            "hi": "एक संख्या में पहले $55.55\\%$ की वृद्धि की जाती है और फिर $16.66\\%$ की कमी की जाती है। अंतिम संख्या प्रारंभिक संख्या से कितने प्रतिशत बढ़ी या घटी है?"
        },
        "options": "(a) Increased by $30\\%$ &emsp; (b) Decreased by $30\\%$ &emsp; (c) Increased by $25\\%$ &emsp; (d) Decreased by $25\\%$",
        "solution": {
            "en": "$55.55\\% = \\frac{5}{9} \\implies \\text{factor} = \\frac{14}{9}$.<br>$16.66\\% = \\frac{1}{6} \\implies \\text{factor} = \\frac{5}{6}$.<br>Net multiplier = $\\frac{14}{9} \\times \\frac{5}{6} = \\frac{70}{54} = \\frac{35}{27}$.<br>Percentage change = $\\frac{35 - 27}{27} \\times 100\\% \\approx 29.6\\% \\approx \\mathbf{30\\% \\text{ increase}}$.<br><br><strong>Answer: (a) Increased by 30%</strong>",
            "hi": "$55.55\\% = \\frac{5}{9} \\implies$ गुणक = $\\frac{14}{9}$।<br>$16.66\\% = \\frac{1}{6} \\implies$ गुणक = $\\frac{5}{6}$।<br>कुल गुणक = $\\frac{14}{9} \\times \\frac{5}{6} = \\frac{70}{54} = \\frac{35}{27}$।<br>प्रतिशत परिवर्तन = $\\frac{35 - 27}{27} \\times 100\\% \\approx 29.6\\% \\approx \\mathbf{30\\% \\text{ वृद्धि}}$ है।<br><br><strong>उत्तर: (a) Increased by 30%</strong>"
        }
    },
    {
        "id": "PCT_PYQ13",
        "badge": "CGL 2024",
        "question": {
            "en": "The price of sugar is increased by $20\\%$. A family decreased its consumption by $30\\%$. The expenditure of the family on sugar is:",
            "hi": "चीनी की कीमत में $20\\%$ की वृद्धि हुई। एक परिवार ने अपनी खपत में $30\\%$ की कमी कर दी। चीनी पर परिवार का व्यय क्या होगा?"
        },
        "options": "(a) Decreased by $16\\%$ &emsp; (b) Decreased by $10\\%$ &emsp; (c) Increased by $16\\%$ &emsp; (d) Increased by $10\\%$",
        "solution": {
            "en": "Net multiplier = $1.20 \\times 0.70 = 0.84$.<br>Decrease = $1 - 0.84 = 0.16 = \\mathbf{16\\% \\text{ decrease}}$.<br><br><strong>Answer: (a) Decreased by 16%</strong>",
            "hi": "कुल गुणक = $1.20 \\times 0.70 = 0.84$।<br>कमी = $1 - 0.84 = 0.16 = \\mathbf{16\\% \\text{ कमी}}$ है।<br><br><strong>उत्तर: (a) Decreased by 16%</strong>"
        }
    },
    {
        "id": "PCT_PYQ14",
        "badge": "CGL 2023",
        "question": {
            "en": "When the price of an item was reduced by $20\\%$, its sale increased by $x\\%$. If there is an increase of $25\\%$ in revenue, then find the value of $x$.",
            "hi": "जब किसी वस्तु की कीमत में $20\\%$ की कमी की गई, तो उसकी बिक्री में $x\\%$ की वृद्धि हुई। यदि राजस्व में $25\\%$ की वृद्धि होती है, तो $x$ का मान ज्ञात कीजिए।"
        },
        "options": "(a) $55.35$ &emsp; (b) $57.75$ &emsp; (c) $56.25$ &emsp; (d) $54.35$",
        "solution": {
            "en": "Revenue = Price $\\times$ Sale.<br>Given: $0.80 \\times (1 + \\frac{x}{100}) = 1.25 \\implies 1 + \\frac{x}{100} = 1.5625 \\implies \\frac{x}{100} = 0.5625 \\implies x = \\mathbf{56.25}$.<br><br><strong>Answer: (c) 56.25</strong>",
            "hi": "राजस्व = कीमत $\\times$ बिक्री।<br>दिया गया है: $0.80 \times (1 + \\frac{x}{100}) = 1.25 \\implies 1 + \\frac{x}{100} = 1.5625 \\implies \\frac{x}{100} = 0.5625 \\implies x = \\mathbf{56.25}$ है।<br><br><strong>उत्तर: (c) 56.25</strong>"
        }
    },
    {
        "id": "PCT_PYQ15",
        "badge": "CGL 2022 Tier-II",
        "question": {
            "en": "When the price of an item was reduced by $20\\%$, its sale increased by $x\\%$. If revenue increases by $60\\%$, then find $x$.",
            "hi": "जब किसी वस्तु की कीमत में $20\\%$ की कमी की गई, तो उसकी बिक्री में $x\\%$ की वृद्धि हुई। यदि राजस्व में $60\\%$ की वृद्धि होती है, तो $x$ ज्ञात कीजिए।"
        },
        "options": "(a) $100\\%$ &emsp; (b) $80\\%$ &emsp; (c) $120\\%$ &emsp; (d) $90\\%$",
        "solution": {
            "en": "$0.80 \\times (1 + \\frac{x}{100}) = 1.60 \\implies 1 + \\frac{x}{100} = 2 \\implies \\frac{x}{100} = 1 \\implies x = \\mathbf{100\\%}$.<br><br><strong>Answer: (a) 100%</strong>",
            "hi": "$0.80 \times (1 + \\frac{x}{100}) = 1.60 \\implies 1 + \\frac{x}{100} = 2 \\implies \\frac{x}{100} = 1 \\implies x = \\mathbf{100\\%}$ है।<br><br><strong>उत्तर: (a) 100%</strong>"
        }
    },
    {
        "id": "PCT_PYQ16",
        "badge": "CGL 2021",
        "question": {
            "en": "The price of sugar is increased by $18\\%$. By what percent, correct to one decimal place, should a person decrease his consumption so that expenditure increases by only $12\\%$?",
            "hi": "चीनी की कीमत में $18\\%$ की वृद्धि हुई है। एक व्यक्ति को अपनी खपत में कितने प्रतिशत की कमी करनी चाहिए (एक दशमलव स्थान तक सही) ताकि व्यय केवल $12\\%$ बढ़े?"
        },
        "options": "(a) $5.1\\%$ &emsp; (b) $5.5\\%$ &emsp; (c) $6.0\\%$ &emsp; (d) $4.8\\%$",
        "solution": {
            "en": "Let initial Price = $100$, Consumption = $100$, Expenditure = $10000$.<br>New Price = $118$. New Expenditure = $11200$.<br>New Consumption = $\\frac{11200}{118} \\approx 94.915$.<br>Decrease in consumption = $100 - 94.915 = 5.085\\% \\approx \\mathbf{5.1\\%}$.<br><br><strong>Answer: (a) 5.1%</strong>",
            "hi": "मान लीजिए प्रारंभिक मूल्य = $100$, खपत = $100$, व्यय = $10000$ है।<br>नया मूल्य = $118$। नया व्यय = $11200$।<br>नई खपत = $\\frac{11200}{118} \\approx 94.915$।<br>खपत में कमी = $100 - 94.915 = 5.085\\% \\approx \\mathbf{5.1\\%}$ है।<br><br><strong>उत्तर: (a) 5.1%</strong>"
        }
    },
    {
        "id": "PCT_PYQ17",
        "badge": "CGL 2020",
        "question": {
            "en": "When the price of an article was reduced by $20\\%$, its sale increased by $80\\%$. What was the net effect on the revenue?",
            "hi": "जब किसी वस्तु की कीमत में $20\\%$ की कमी की गई, तो उसकी बिक्री में $80\\%$ की वृद्धि हुई। राजस्व पर शुद्ध प्रभाव क्या था?"
        },
        "options": "(a) $44\\%$ increase &emsp; (b) $44\\%$ decrease &emsp; (c) $60\\%$ increase &emsp; (d) $60\\%$ decrease",
        "solution": {
            "en": "Net multiplier = $0.80 \\times 1.80 = 1.44 \\implies \\mathbf{44\\% \\text{ increase}}$.<br><br><strong>Answer: (a) Increased by 44%</strong>",
            "hi": "कुल गुणक = $0.80 \\times 1.80 = 1.44 \\implies \\mathbf{44\\% \\text{ वृद्धि}}$ है।<br><br><strong>उत्तर: (a) Increased by 44%</strong>"
        }
    },
    {
        "id": "PCT_PYQ18",
        "badge": "CGL 2019",
        "question": {
            "en": "If an electricity bill is paid before the due date, one gets a reduction of $4\\%$ on the amount. If the bill amount is $₹2,250$ and it is paid before due date, how much does one pay?",
            "hi": "यदि बिजली बिल का भुगतान नियत तारीख से पहले किया जाता है, तो किसी को राशि पर $4\\%$ की छूट मिलती है। यदि बिल राशि $₹2,250$ है और इसका भुगतान नियत तारीख से पहले किया जाता है, तो भुगतान कितना होगा?"
        },
        "options": "(a) $₹2,160$ &emsp; (b) $₹2,200$ &emsp; (c) $₹2,180$ &emsp; (d) $₹2,150$",
        "solution": {
            "en": "Amount to pay = $2250 \\times (1 - 0.04) = 2250 \\times 0.96 = \\mathbf{₹2,160}$.<br><br><strong>Answer: (a) ₹2,160</strong>",
            "hi": "भुगतान की जाने वाली राशि = $2250 \\times (1 - 0.04) = 2250 \\times 0.96 = \\mathbf{₹2,160}$ है।<br><br><strong>उत्तर: (a) ₹2,160</strong>"
        }
    },
    # TYPE 4
    {
        "id": "PCT_PYQ19",
        "badge": "CGL 2024",
        "question": {
            "en": "A number is first decreased by $18\\%$ and the resulting number is then increased by $25\\%$. What is the overall percentage change?",
            "hi": "एक संख्या में पहले $18\\%$ की कमी की जाती है और परिणामी संख्या में फिर $25\\%$ की वृद्धि की जाती है। कुल प्रतिशत परिवर्तन क्या है?"
        },
        "options": "(a) Increased by $2.5\\%$ &emsp; (b) Decreased by $2.5\\%$ &emsp; (c) Increased by $3\\%$ &emsp; (d) Decreased by $3\\%$",
        "solution": {
            "en": "Net multiplier = $0.82 \\times 1.25 = 1.025 \\implies \\mathbf{2.5\\% \\text{ increase}}$.<br><br><strong>Answer: (a) Increased by 2.5%</strong>",
            "hi": "कुल गुणक = $0.82 \\times 1.25 = 1.025 \\implies \\mathbf{2.5\\% \\text{ वृद्धि}}$ है।<br><br><strong>उत्तर: (a) Increased by 2.5%</strong>"
        }
    },
    {
        "id": "PCT_PYQ20",
        "badge": "CGL 2023",
        "question": {
            "en": "Two successive price increases of $10\\%$ and $10\\%$ are equivalent to a single price increase of:",
            "hi": "$10\\%$ और $10\\%$ की दो क्रमिक मूल्य वृद्धि किसके बराबर हैं?"
        },
        "options": "(a) $21\\%$ &emsp; (b) $20\\%$ &emsp; (c) $22\\%$ &emsp; (d) $19\\%$",
        "solution": {
            "en": "Successive = $10 + 10 + \\frac{100}{100} = \\mathbf{21\\%}$.<br><br><strong>Answer: (a) 21%</strong>",
            "hi": "क्रमिक परिवर्तन = $10 + 10 + \\frac{100}{100} = \\mathbf{21\\%}$ है।<br><br><strong>उत्तर: (a) 21%</strong>"
        }
    },
    {
        "id": "PCT_PYQ21",
        "badge": "CGL 2022",
        "question": {
            "en": "Raman's salary was decreased by $50\\%$ and then increased by $50\\%$. How much percent does he lose?",
            "hi": "रमन के वेतन में $50\\%$ की कमी की गई और फिर $50\\%$ की वृद्धि की गई। उसे कितने प्रतिशत की हानि होती है?"
        },
        "options": "(a) $25\\%$ &emsp; (b) $20\\%$ &emsp; (c) $50\\%$ &emsp; (d) $0\\%$",
        "solution": {
            "en": "Net multiplier = $0.50 \\times 1.50 = 0.75$.<br>Loss = $1 - 0.75 = 0.25 = \\mathbf{25\\%}$.<br><br><strong>Answer: (a) 25%</strong>",
            "hi": "कुल गुणक = $0.50 \\times 1.50 = 0.75$।<br>हानि = $1 - 0.75 = 0.25 = \\mathbf{25\\%}$ है।<br><br><strong>उत्तर: (a) 25%</strong>"
        }
    },
    {
        "id": "PCT_PYQ22",
        "badge": "CGL 2021",
        "question": {
            "en": "If each side of a cube is decreased by $12\\%$, then the percentage decrease in its surface area is:",
            "hi": "यदि किसी घन की प्रत्येक भुजा में $12\\%$ की कमी की जाती है, तो उसके पृष्ठीय क्षेत्रफल में प्रतिशत कमी क्या होगी?"
        },
        "options": "(a) $22.56\\%$ &emsp; (b) $24\\%$ &emsp; (c) $21.44\\%$ &emsp; (d) $23.04\\%$",
        "solution": {
            "en": "Surface Area $\\propto \\text{side}^2$.<br>Side factor = $0.88$. New Surface Area factor = $(0.88)^2 = 0.7744$.<br>Decrease = $1 - 0.7744 = 0.2256 = \\mathbf{22.56\\%}$.<br><br><strong>Answer: (a) 22.56%</strong>",
            "hi": "पृष्ठीय क्षेत्रफल $\\propto \\text{भुजा}^2$।<br>भुजा गुणक = $0.88$। नया पृष्ठीय क्षेत्रफल गुणक = $(0.88)^2 = 0.7744$।<br>कमी = $1 - 0.7744 = 0.2256 = \\mathbf{22.56\\%}$ है।<br><br><strong>उत्तर: (a) 22.56%</strong>"
        }
    },
    {
        "id": "PCT_PYQ23",
        "badge": "CGL 2020",
        "question": {
            "en": "The population of a country increases by $8\\%$ in Year 1, $5\\%$ in Year 2 and $10\\%$ in Year 3. If present population is $43,65,900$, what was the population 3 years ago?",
            "hi": "एक देश की जनसंख्या में पहले वर्ष में $8\\%$, दूसरे वर्ष में $5\\%$ और तीसरे वर्ष में $10\\%$ की वृद्धि होती है। यदि वर्तमान जनसंख्या $43,65,900$ है, तो 3 वर्ष पहले जनसंख्या कितनी थी?"
        },
        "options": "(a) $35,00,000$ &emsp; (b) $36,00,000$ &emsp; (c) $32,00,000$ &emsp; (d) $38,00,000$",
        "solution": {
            "en": "Let population 3 years ago be $P$.<br>$P \\times 1.08 \\times 1.05 \\times 1.10 = 43,65,900$<br>$P \\times 1.2474 = 43,65,900 \\implies P = \\frac{43,65,900}{1.2474} = \\mathbf{35,00,000}$.<br><br><strong>Answer: (a) 35,00,000</strong>",
            "hi": "मान लीजिए 3 वर्ष पहले की जनसंख्या $P$ थी।<br>$P \\times 1.08 \\times 1.05 \\times 1.10 = 43,65,900$<br>$P \\times 1.2474 = 43,65,900 \\implies P = \\frac{43,65,900}{1.2474} = \\mathbf{35,00,000}$ है।<br><br><strong>उत्तर: (a) 35,00,000</strong>"
        }
    },
    {
        "id": "PCT_PYQ24",
        "badge": "CGL 2018",
        "question": {
            "en": "On a marked price, the difference of selling prices with a discount of $30\\%$ and two successive discounts of $20\\%$ and $10\\%$ is $₹72$. Find the marked price.",
            "hi": "अंकित मूल्य पर, $30\\%$ की एकल छूट और $20\\%$ तथा $10\\%$ की दो क्रमिक छूटों के विक्रय मूल्य का अंतर $₹72$ है। अंकित मूल्य ज्ञात कीजिए।"
        },
        "options": "(a) $₹3,600$ &emsp; (b) $₹3,000$ &emsp; (c) $₹4,000$ &emsp; (d) $₹3,500$",
        "solution": {
            "en": "First selling price factor = $1 - 0.30 = 0.70$.<br>Second successive factor = $(1 - 0.20)(1 - 0.10) = 0.80 \\times 0.90 = 0.72$.<br>Difference = $0.72 - 0.70 = 0.02$ of MP.<br>Given $0.02 \\text{ of MP} = 72 \\implies \\text{MP} = \\frac{72}{0.02} = \\mathbf{₹3,600}$.<br><br><strong>Answer: (a) ₹3,600</strong>",
            "hi": "पहला विक्रय मूल्य कारक = $1 - 0.30 = 0.70$।<br>दूसरा क्रमिक कारक = $(1 - 0.20)(1 - 0.10) = 0.80 \\times 0.90 = 0.72$।<br>अंतर = MP का $0.72 - 0.70 = 0.02$।<br>दिया गया है: MP का $0.02 = 72 \\implies \\text{MP} = \\frac{72}{0.02} = \\mathbf{₹3,600}$ है।<br><br><strong>उत्तर: (a) ₹3,600</strong>"
        }
    },
    # TYPE 5
    {
        "id": "PCT_PYQ25",
        "badge": "CGL 2024",
        "question": {
            "en": "If $A$'s income is $50\\%$ less than $B$'s, then $B$'s income is what percent more than $A$'s?",
            "hi": "यदि $A$ की आय $B$ की आय से $50\\%$ कम है, तो $B$ की आय $A$ की आय से कितने प्रतिशत अधिक है?"
        },
        "options": "(a) $100\\%$ &emsp; (b) $50\\%$ &emsp; (c) $75\\%$ &emsp; (d) $150\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 50$.<br>$B$ is more than $A$ by $50$.<br>Percentage more = $\\frac{50}{50} \\times 100\\% = \\mathbf{100\\%}$.<br><br><strong>Answer: (a) 100%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 50$ है।<br>$B$, $A$ से $50$ अधिक है।<br>प्रतिशत अधिक = $\\frac{50}{50} \\times 100\\% = \\mathbf{100\\%}$ है।<br><br><strong>उत्तर: (a) 100%</strong>"
        }
    },
    {
        "id": "PCT_PYQ26",
        "badge": "CGL 2023",
        "question": {
            "en": "If $A$'s income is $25\\%$ less than $B$'s, by how much percentage is $B$'s income more than $A$'s?",
            "hi": "यदि $A$ की आय $B$ की आय से $25\\%$ कम है, तो $B$ की आय $A$ की आय से कितने प्रतिशत अधिक है?"
        },
        "options": "(a) $33.33\\%$ &emsp; (b) $25\\%$ &emsp; (c) $20\\%$ &emsp; (d) $30\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 75$.<br>Percentage more = $\\frac{25}{75} \\times 100\\% = \\mathbf{33.33\\%}$.<br><br><strong>Answer: (a) 33.33%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 75$ है।<br>प्रतिशत अधिक = $\\frac{25}{75} \\times 100\\% = \\mathbf{33.33\\%}$ है।<br><br><strong>उत्तर: (a) 33.33%</strong>"
        }
    },
    {
        "id": "PCT_PYQ27",
        "badge": "CGL 2022",
        "question": {
            "en": "The income of $A$ is $50\\%$ more than that of $B$. If $A$'s income increases by $40\\%$ and $B$'s increases by $90\\%$, find the percentage increase in their combined income.",
            "hi": "A की आय B की आय से $50\\%$ अधिक है। यदि A की आय में $40\\%$ और B की आय में $90\\%$ की वृद्धि होती है, तो उनकी संयुक्त आय में प्रतिशत वृद्धि ज्ञात कीजिए।"
        },
        "options": "(a) $60\\%$ &emsp; (b) $50\\%$ &emsp; (c) $55\\%$ &emsp; (d) $65\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 150$. Combined income = $250$.<br>New $A = 150 \\times 1.40 = 210$.<br>New $B = 100 \\times 1.90 = 190$.<br>New combined income = $210 + 190 = 400$.<br>Increase = $400 - 250 = 150$.<br>Percentage increase = $\\frac{150}{250} \\times 100\\% = \\mathbf{60\\%}$.<br><br><strong>Answer: (a) 60%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 150$ है। संयुक्त आय = $250$।<br>नया $A = 150 \\times 1.40 = 210$।<br>नया $B = 100 \\times 1.90 = 190$।<br>नई संयुक्त आय = $210 + 190 = 400$।<br>वृद्धि = $400 - 250 = 150$।<br>प्रतिशत वृद्धि = $\\frac{150}{250} \\times 100\\% = \\mathbf{60\\%}$ है।<br><br><strong>उत्तर: (a) 60%</strong>"
        }
    },
    {
        "id": "PCT_PYQ28",
        "badge": "CGL 2021",
        "question": {
            "en": "If $A$ is $20\\%$ less than $B$, and $C$ is $30\\%$ more than $D$. If $D$ is $25\\%$ less than $A$, then which of the following relations holds true?",
            "hi": "यदि $A$, $B$ से $20\\%$ कम है, और $C$, $D$ से $30\\%$ अधिक है। यदि $D$, $A$ से $25\\%$ कम है, तो निम्नलिखित में से कौन सा संबंध सत्य है?"
        },
        "options": "(a) $C > B > A > D$ &emsp; (b) $B > C > A > D$ &emsp; (c) $B > A > C > D$ &emsp; (d) $C > A > B > D$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 80$.<br>$D$ is $25\\%$ less than $A \\implies D = 80 \\times 0.75 = 60$.<br>$C$ is $30\\%$ more than $D \\implies C = 60 \\times 1.30 = 78$.<br>Comparing the values: $B(100) > A(80) > C(78) > D(60)$. Depending on options: $\\mathbf{B > A > C > D}$ (or options evaluation).<br><br><strong>Answer: (c) B > A > C > D</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 80$ है।<br>$D$, $A$ से $25\\%$ कम है $\implies D = 80 \\times 0.75 = 60$।<br>$C$, $D$ से $30\\%$ अधिक है $\implies C = 60 \\times 1.30 = 78$।<br>मानों की तुलना करने पर: $B(100) > A(80) > C(78) > D(60)$। इस प्रकार $\\mathbf{B > A > C > D}$ सत्य है।<br><br><strong>उत्तर: (c) B > A > C > D</strong>"
        }
    },
    {
        "id": "PCT_PYQ29",
        "badge": "CGL 2020",
        "question": {
            "en": "If $A$ is $28\\%$ more than $B$ and $C$ is $25\\%$ less than the sum of $A$ and $B$, find by what percent $C$ is more than $A$ (correct to one decimal place).",
            "hi": "यदि A, B से $28\\%$ अधिक है और C, A और B के योग से $25\\%$ कम है, तो ज्ञात कीजिए कि C, A से कितने प्रतिशत अधिक है (एक दशमलव स्थान तक सही)।"
        },
        "options": "(a) $33.6\\%$ &emsp; (b) $32.2\\%$ &emsp; (c) $43.0\\%$ &emsp; (d) $28.5\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 128$.<br>Sum $(A+B) = 228$.<br>$C = 228 \\times 0.75 = 171$.<br>Difference $(C-A) = 171 - 128 = 43$.<br>Percentage more = $\\frac{43}{128} \\times 100\\% \\approx \\mathbf{33.6\\%}$.<br><br><strong>Answer: (a) 33.6%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 128$ है।<br>योग $(A+B) = 228$।<br>$C = 228 \\times 0.75 = 171$।<br>अंतर $(C-A) = 171 - 128 = 43$।<br>प्रतिशत अधिक = $\\frac{43}{128} \\times 100\\% \\approx \\mathbf{33.6\\%}$ है।<br><br><strong>उत्तर: (a) 33.6%</strong>"
        }
    },
    {
        "id": "PCT_PYQ30",
        "badge": "CGL 2019",
        "question": {
            "en": "In an examination, $A$ got $25\\%$ more marks than $B$, $B$ got $10\\%$ less than $C$, and $C$ got $25\\%$ more than $D$. If $D$ got $320$ marks out of $500$, find the marks obtained by $A$.",
            "hi": "एक परीक्षा में, A को B से $25\\%$ अधिक अंक मिले, B को C से $10\\%$ कम मिले, और C को D से $25\\%$ अधिक मिले। यदि D को $500$ में से $320$ अंक मिले, तो A द्वारा प्राप्त अंक ज्ञात कीजिए।"
        },
        "options": "(a) $450$ &emsp; (b) $460$ &emsp; (c) $400$ &emsp; (d) $480$",
        "solution": {
            "en": "$D = 320$.<br>$C = 320 \\times 1.25 = 400$.<br>$B = 400 \\times 0.90 = 360$.<br>$A = 360 \\times 1.25 = \\mathbf{450}$.<br><br><strong>Answer: (a) 450</strong>",
            "hi": "$D = 320$।<br>$C = 320 \\times 1.25 = 400$।<br>$B = 400 \\times 0.90 = 360$।<br>$A = 360 \\times 1.25 = \\mathbf{450}$ है।<br><br><strong>उत्तर: (a) 450</strong>"
        }
    },
    # TYPE 6
    {
        "id": "PCT_PYQ31",
        "badge": "CGL 2023",
        "question": {
            "en": "The population of a village was $9,600$. If males increased by $8\\%$ and females by $5\\%$ in a year, the population became $10,176$. How many males were there before?",
            "hi": "एक गाँव की जनसंख्या $9,600$ थी। यदि एक वर्ष में पुरुषों की संख्या में $8\\%$ और महिलाओं की संख्या में $5\\%$ की वृद्धि हुई, तो जनसंख्या $10,176$ हो गई। पहले पुरुषों की संख्या कितनी थी?"
        },
        "options": "(a) $4,800$ &emsp; (b) $3,200$ &emsp; (c) $5,000$ &emsp; (d) $4,500$",
        "solution": {
            "en": "Total increase = $10176 - 9600 = 576$.<br>Let males = $m \\implies$ females = $9600 - m$.<br>$0.08m + 0.05(9600 - m) = 576$<br>$0.08m + 480 - 0.05m = 576 \\implies 0.03m = 96 \\implies m = \\mathbf{3,200}$. (Note: Option evaluation and standard keys list $3,200$ or adjusted results).<br><br><strong>Answer: (b) 3,200</strong>",
            "hi": "कुल वृद्धि = $10176 - 9600 = 576$।<br>मान लीजिए पुरुष = $m \\implies$ महिलाएं = $9600 - m$।<br>$0.08m + 0.05(9600 - m) = 576$<br>$0.08m + 480 - 0.05m = 576 \\implies 0.03m = 96 \\implies m = \\mathbf{3,200}$ है।<br><br><strong>उत्तर: (b) 3,200</strong>"
        }
    },
    {
        "id": "PCT_PYQ32",
        "badge": "CGL 2022",
        "question": {
            "en": "If $60\\%$ of students in a school are boys and the number of girls is $972$, how many boys are there in the school?",
            "hi": "यदि एक स्कूल में $60\\%$ छात्र लड़के हैं और लड़कियों की संख्या $972$ है, तो स्कूल में लड़कों की संख्या कितनी है?"
        },
        "options": "(a) $1,458$ &emsp; (b) $1,500$ &emsp; (c) $1,320$ &emsp; (d) $1,200$",
        "solution": {
            "en": "Percentage of girls = $100\\% - 60\\% = 40\\%$.<br>Given: $40\\% = 972 \\implies 1\\% = 24.3$.<br>Number of boys ($60\\%$) = $24.3 \\times 60 = \\mathbf{1,458}$.<br><br><strong>Answer: (a) 1,458</strong>",
            "hi": "लड़कियों का प्रतिशत = $100\\% - 60\\% = 40\\%$।<br>दिया गया है: $40\\% = 972 \\implies 1\\% = 24.3$।<br>लड़कों की संख्या ($60\\%$) = $24.3 \\times 60 = \\mathbf{1,458}$ है।<br><br><strong>उत्तर: (a) 1,458</strong>"
        }
    },
    {
        "id": "PCT_PYQ33",
        "badge": "CGL 2020",
        "question": {
            "en": "In a hotel, $60\\%$ had vegetarian lunch, $30\\%$ had non-vegetarian lunch, and $15\\%$ had both. If $96$ people were present, how many did not eat either?",
            "hi": "एक होटल में, $60\\%$ ने शाकाहारी भोजन किया, $30\\%$ ने मांसाहारी भोजन किया और $15\\%$ ने दोनों किया। यदि $96$ लोग उपस्थित थे, तो कितने लोगों ने दोनों में से कुछ भी नहीं खाया?"
        },
        "options": "(a) $24$ &emsp; (b) $20$ &emsp; (c) $18$ &emsp; (d) $30$",
        "solution": {
            "en": "Total eating at least one = $60\\% + 30\\% - 15\\% = 75\\%$.<br>Did not eat either = $100\\% - 75\\% = 25\\%$.<br>Number of people = $25\\% \\text{ of } 96 = \\mathbf{24}$.<br><br><strong>Answer: (a) 24</strong>",
            "hi": "कम से कम एक खाने वाले = $60\\% + 30\\% - 15\\% = 75\\%$।<br>कुछ भी न खाने वाले = $100\\% - 75\\% = 25\\%$।<br>लोगों की संख्या = $96$ का $25\\% = \\mathbf{24}$ है।<br><br><strong>उत्तर: (a) 24</strong>"
        }
    },
    # TYPE 7
    {
        "id": "PCT_PYQ34",
        "badge": "CGL 2024",
        "question": {
            "en": "A man donates $30\\%$ of his wealth to charity. Of the remaining, $30\\%$ and $25\\%$ go to his wife and son respectively. The rest is divided equally among his 3 daughters; one daughter gets $₹42$ lakh. Find his total wealth.",
            "hi": "एक व्यक्ति अपनी संपत्ति का $30\\%$ दान करता है। शेष में से क्रमशः $30\\%$ और $25\\%$ उसकी पत्नी और पुत्र को जाते हैं। शेष राशि को उसकी 3 बेटियों में बराबर बांटा जाता है; एक बेटी को $₹42$ लाख मिलते हैं। उसकी कुल संपत्ति ज्ञात कीजिए।"
        },
        "options": "(a) $₹400$ lakhs &emsp; (b) $₹350$ lakhs &emsp; (c) $₹450$ lakhs &emsp; (d) $₹500$ lakhs",
        "solution": {
            "en": "Remaining after charity = $70\\%$.<br>Sum given to wife and son = $30\\% + 25\\% = 55\\%$ of the remaining.<br>So remaining for daughters = $45\\% \\text{ of } 70\\% = 31.5\\%$ of total.<br>Each daughter gets = $\\frac{31.5\\%}{3} = 10.5\\%$.<br>Given: $10.5\\% = ₹42 \\text{ lakhs} \\implies \\text{Total Wealth} = \\frac{42}{10.5} \\times 100 = \\mathbf{₹400 \\text{ lakhs}}$.<br><br><strong>Answer: (a) ₹400 lakhs</strong>",
            "hi": "दान के बाद शेष = $70\\%$।<br>पत्नी और पुत्र को दिया गया योग = शेष का $30\\% + 25\\% = 55\\%$।<br>तो बेटियों के लिए शेष = $70\\%$ का $45\\% = 31.5\\%$ (कुल का)।<br>प्रत्येक बेटी को प्राप्त होता है = $\\frac{31.5\\%}{3} = 10.5\\%$।<br>दिया गया है: $10.5\\% = ₹42$ लाख $\implies$ कुल संपत्ति = $\\frac{42}{10.5} \\times 100 = \\mathbf{₹400 \\text{ लाख}}$ है।<br><br><strong>उत्तर: (a) ₹400 lakhs</strong>"
        }
    },
    {
        "id": "PCT_PYQ35",
        "badge": "CGL 2023",
        "question": {
            "en": "A man's annual income increased by $₹5$ lakhs but the tax rate fell from $12\\%$ to $10\\%$. He now pays $₹10,000$ more income tax. Find his original income.",
            "hi": "एक व्यक्ति की वार्षिक आय में $₹5$ लाख की वृद्धि हुई लेकिन आयकर की दर $12\\%$ से घटकर $10\\%$ हो गई। अब वह $₹10,000$ अधिक आयकर देता है। उसकी मूल आय ज्ञात कीजिए।"
        },
        "options": "(a) $₹20$ lakhs &emsp; (b) $₹25$ lakhs &emsp; (c) $₹15$ lakhs &emsp; (d) $₹18$ lakhs",
        "solution": {
            "en": "Let original income be $I$ (in lakhs).<br>Original tax = $0.12I$. New income = $(I + 5)$. New tax = $0.10(I + 5)$.<br>Given: New Tax - Old Tax = $₹10,000 = ₹0.1$ lakh.<br>$0.10(I + 5) - 0.12I = 0.1$<br>$0.10I + 0.5 - 0.12I = 0.1 \\implies 0.02I = 0.4 \\implies I = \\mathbf{₹20 \\text{ lakhs}}$.<br><br><strong>Answer: (a) ₹20 lakhs</strong>",
            "hi": "मान लीजिए मूल आय $I$ (लाख में) है।<br>मूल कर = $0.12I$। नई आय = $(I + 5)$। नया कर = $0.10(I + 5)$।<br>दिया गया है: नया कर - पुराना कर = $₹10,000 = ₹0.1$ लाख।<br>$0.10(I + 5) - 0.12I = 0.1$<br>$0.10I + 0.5 - 0.12I = 0.1 \\implies 0.02I = 0.4 \\implies I = \\mathbf{₹20 \\text{ लाख}}$ है।<br><br><strong>उत्तर: (a) ₹20 lakhs</strong>"
        }
    },
    # TYPE 8
    {
        "id": "PCT_PYQ36",
        "badge": "CGL 2022",
        "question": {
            "en": "If income tax is increased by $19\\%$, the net income is reduced by $1\\%$. Find the rate of income tax.",
            "hi": "यदि आयकर में $19\\%$ की वृद्धि की जाती है, तो शुद्ध आय में $1\\%$ की कमी होती है। आयकर की दर ज्ञात कीजिए।"
        },
        "options": "(a) $5\\%$ &emsp; (b) $4\\%$ &emsp; (c) $6\\%$ &emsp; (d) $4.5\\%$",
        "solution": {
            "en": "Formula: $\\text{Tax Rate} = \\frac{\\text{Decrease in Net Income}\\%}{\\text{Increase in Tax}\\% + \\text{Decrease in Net Income}\\%} \\times 100\\%$.<br>$\\text{Tax Rate} = \\frac{1}{19 + 1} \\times 100\\% = \\mathbf{5\\%}$.<br><br><strong>Answer: (a) 5%</strong>",
            "hi": "सूत्र: $\\text{कर दर} = \\frac{\\text{शुद्ध आय में कमी}\\%}{\\text{कर में वृद्धि}\\% + \\text{शुद्ध आय में कमी}\\%} \\times 100\\%$।<br>$\\text{कर दर} = \\frac{1}{19 + 1} \\times 100\\% = \\mathbf{5\\%}$ है।<br><br><strong>उत्तर: (a) 5%</strong>"
        }
    },
    {
        "id": "PCT_PYQ37",
        "badge": "CGL 2021",
        "question": {
            "en": "If the numerator of a fraction is increased by $80\\%$ and the denominator is increased by $120\\%$, the resultant fraction is $\\frac{7}{22}$. What is the original fraction?",
            "hi": "यदि किसी भिन्न के अंश में $80\\%$ की वृद्धि की जाती है और हर में $120\\%$ की वृद्धि की जाती है, तो परिणामी भिन्न $\\frac{7}{22}$ होती है। मूल भिन्न क्या है?"
        },
        "options": "(a) $7/18$ &emsp; (b) $7/12$ &emsp; (c) $5/12$ &emsp; (d) $9/14$",
        "solution": {
            "en": "Let original fraction be $\\frac{n}{d}$.<br>$\\frac{1.8n}{2.2d} = \\frac{7}{22} \\implies \\frac{n}{d} = \\frac{7}{22} \\times \\frac{22}{18} = \\mathbf{\\frac{7}{18}}$. (Note: SSC evaluated answer sheet key varies, matching standard calculation $\\mathbf{7/18}$).<br><br><strong>Answer: (a) 7/18</strong>",
            "hi": "मान लीजिए मूल भिन्न $\\frac{n}{d}$ है।<br>$\\frac{1.8n}{2.2d} = \\frac{7}{22} \\implies \\frac{n}{d} = \\frac{7}{22} \\times \\frac{22}{18} = \\mathbf{\\frac{7}{18}}$ है।<br><br><strong>उत्तर: (a) 7/18</strong>"
        }
    },
    {
        "id": "PCT_PYQ38",
        "badge": "CGL 2020",
        "question": {
            "en": "Two numbers are $40\\%$ and $80\\%$ lesser than a third number. By what percent must the second number be increased to equal the first?",
            "hi": "दो संख्याएँ एक तीसरी संख्या से $40\\%$ और $80\\%$ कम हैं। पहली संख्या के बराबर होने के लिए दूसरी संख्या में कितने प्रतिशत की वृद्धि की जानी चाहिए?"
        },
        "options": "(a) $200\\%$ &emsp; (b) $100\\%$ &emsp; (c) $150\\%$ &emsp; (d) $250\\%$",
        "solution": {
            "en": "Let the third number = $100$.<br>First number = $100 - 40 = 60$.<br>Second number = $100 - 80 = 20$.<br>Increase required from $20$ to $60$ is $40$.<br>Percentage increase = $\\frac{40}{20} \\times 100\\% = \\mathbf{200\\%}$.<br><br><strong>Answer: (a) 200%</strong>",
            "hi": "मान लीजिए तीसरी संख्या = $100$ है।<br>पहली संख्या = $100 - 40 = 60$।<br>दूसरी संख्या = $100 - 80 = 20$।<br>$20$ से $60$ तक आवश्यक वृद्धि $40$ है।<br>प्रतिशत वृद्धि = $\\frac{40}{20} \\times 100\\% = \\mathbf{200\\%}$ है।<br><br><strong>उत्तर: (a) 200%</strong>"
        }
    },
    {
        "id": "PCT_PYQ39",
        "badge": "CGL 2019",
        "question": {
            "en": "A number is increased by $20\\%$ and then decreased by $20\\%$. Find the net percentage change.",
            "hi": "एक संख्या में $20\\%$ की वृद्धि की जाती है और फिर $20\\%$ की कमी की जाती है। शुद्ध प्रतिशत परिवर्तन ज्ञात कीजिए।"
        },
        "options": "(a) Decreased by $4\\%$ &emsp; (b) Increased by $4\\%$ &emsp; (c) No change &emsp; (d) Decreased by $2\\%$",
        "solution": {
            "en": "Net change = $1.20 \\times 0.80 = 0.96 \\implies \\mathbf{4\\% \\text{ decrease}}$.<br><br><strong>Answer: (a) Decreased by 4%</strong>",
            "hi": "शुद्ध परिवर्तन = $1.20 \\times 0.80 = 0.96 \\implies \\mathbf{4\\% \\text{ कमी}}$ है।<br><br><strong>उत्तर: (a) Decreased by 4%</strong>"
        }
    },
    {
        "id": "PCT_PYQ40",
        "badge": "CGL 2018",
        "question": {
            "en": "In a class of $60$ students and $5$ teachers, each student gets sweets equal to $20\\%$ of total students and each teacher gets sweets equal to $30\\%$ of total students. What is the total number of sweets distributed?",
            "hi": "60 छात्रों और 5 शिक्षकों की एक कक्षा में, प्रत्येक छात्र को कुल छात्रों के $20\\%$ के बराबर मिठाइयाँ मिलती हैं और प्रत्येक शिक्षक को कुल छात्रों के $30\\%$ के बराबर मिठाइयाँ मिलती हैं। वितरित की गई मिठाइयों की कुल संख्या क्या है?"
        },
        "options": "(a) $810$ &emsp; (b) $720$ &emsp; (c) $840$ &emsp; (d) $780$",
        "solution": {
            "en": "Total students = $60$. Sweets per student = $20\\% \\text{ of } 60 = 12$.<br>Total sweets for students = $60 \\times 12 = 720$.<br>Sweets per teacher = $30\\% \\text{ of } 60 = 18$.<br>Total sweets for teachers = $5 \\times 18 = 90$.<br>Total sweets = $720 + 90 = \\mathbf{810}$.<br><br><strong>Answer: (a) 810</strong>",
            "hi": "कुल छात्र = $60$। प्रति छात्र मिठाई = $60$ का $20\\% = 12$।<br>छात्रों के लिए कुल मिठाइयाँ = $60 \\times 12 = 720$।<br>प्रति शिक्षक मिठाई = $60$ का $30\\% = 18$।<br>शिक्षकों के लिए कुल मिठाइयाँ = $5 \\times 18 = 90$।<br>कुल मिठाइयाँ = $720 + 90 = \\mathbf{810}$ हैं।<br><br><strong>उत्तर: (a) 810</strong>"
        }
    },
    {
        "id": "PCT_PYQ41",
        "badge": "CGL 2017",
        "question": {
            "en": "In a college election between two candidates, one candidate got $55\\%$ of the total valid votes. $15\\%$ of the votes were invalid. If total votes polled were $15,200$, what is the number of valid votes the winner got?",
            "hi": "दो उम्मीदवारों के बीच एक कॉलेज चुनाव में, एक उम्मीदवार को कुल वैध मतों का $55\\%$ मिला। $15\\%$ मत अमान्य थे। यदि कुल डाले गए मत $15,200$ थे, तो विजेता को कितने वैध मत मिले?"
        },
        "options": "(a) $7,106$ &emsp; (b) $6,840$ &emsp; (c) $7,500$ &emsp; (d) $7,200$",
        "solution": {
            "en": "Valid votes = $85\\% \\text{ of } 15,200 = 12,920$.<br>Winner's votes = $55\\% \\text{ of } 12,920 = \\mathbf{7,106}$.<br><br><strong>Answer: (a) 7,106</strong>",
            "hi": "वैध मत = $15,200$ का $85\\% = 12,920$।<br>विजेता के मत = $12,920$ का $55\\% = \\mathbf{7,106}$ है।<br><br><strong>उत्तर: (a) 7,106</strong>"
        }
    },
    {
        "id": "PCT_PYQ42",
        "badge": "CGL 2017",
        "question": {
            "en": "In a test of $80$ questions of $1$ mark each, Ankita answers $65\\%$ of the first $40$ questions correctly. What percent of the next $40$ questions must she answer correctly to score $80\\%$ overall in the test?",
            "hi": "प्रत्येक 1 अंक वाले 80 प्रश्नों की एक परीक्षा में, अंकिता पहले 40 प्रश्नों में से $65\\%$ का सही उत्तर देती है। परीक्षा में कुल $80\\%$ अंक प्राप्त करने के लिए उसे अगले 40 प्रश्नों में से कितने प्रतिशत का सही उत्तर देना होगा?"
        },
        "options": "(a) $95\\%$ &emsp; (b) $90\\%$ &emsp; (c) $85\\%$ &emsp; (d) $92\\%$",
        "solution": {
            "en": "Total marks needed = $80\\% \\text{ of } 80 = 64$.<br>Marks secured in first 40 = $65\\% \\text{ of } 40 = 26$.<br>Marks needed in next 40 = $64 - 26 = 38$.<br>Percentage required = $\\frac{38}{40} \\times 100\\% = \\mathbf{95\\%}$.<br><br><strong>Answer: (a) 95%</strong>",
            "hi": "आवश्यक कुल अंक = $80$ का $80\\% = 64$।<br>पहले 40 में प्राप्त अंक = $40$ का $65\\% = 26$।<br>अगले 40 में आवश्यक अंक = $64 - 26 = 38$।<br>आवश्यक प्रतिशत = $\\frac{38}{40} \\times 100\\% = \\mathbf{95\\%}$ है।<br><br><strong>उत्तर: (a) 95%</strong>"
        }
    },
    # TYPE 9 (2025 Pattern)
    {
        "id": "PCT_PYQ43",
        "badge": "CGL 2025 Model",
        "question": {
            "en": "A number is increased by $55.55\\%$ and then decreased by $16.66\\%$. What is the net percentage change?",
            "hi": "एक संख्या में पहले $55.55\\%$ की वृद्धि की जाती है और फिर $16.66\\%$ की कमी की जाती है। शुद्ध प्रतिशत परिवर्तन क्या है?"
        },
        "options": "(a) $+30\\%$ &emsp; (b) $-30\\%$ &emsp; (c) $+25\\%$ &emsp; (d) $-25\\%$",
        "solution": {
            "en": "Let factor conversions be:<br>$55.55\\% = \\frac{5}{9} \\implies 1 + \\frac{5}{9} = \\frac{14}{9}$.<br>$16.66\\% = \\frac{1}{6} \\implies 1 - \\frac{1}{6} = \\frac{5}{6}$.<br>Combined multiplier = $\\frac{14}{9} \\times \\frac{5}{6} = \\frac{35}{27}$.<br>Increase = $\\frac{35-27}{27} \\times 100\\% \\approx \\mathbf{+30\\%}$.<br><br><strong>Answer: (a) +30%</strong>",
            "hi": "भिन्न रूपांतरण:<br>$55.55\\% = \\frac{5}{9} \\implies 1 + \\frac{5}{9} = \\frac{14}{9}$।<br>$16.66\\% = \\frac{1}{6} \\implies 1 - \\frac{1}{6} = \\frac{5}{6}$।<br>संयुक्त गुणक = $\\frac{14}{9} \\times \\frac{5}{6} = \\frac{35}{27}$।<br>वृद्धि = $\\frac{35-27}{27} \\times 100\\% \\approx \\mathbf{+30\\%}$ है।<br><br><strong>उत्तर: (a) +30%</strong>"
        }
    },
    {
        "id": "PCT_PYQ44",
        "badge": "CGL 2025 Model",
        "question": {
            "en": "If each side of a cube is decreased by $12\\%$, find the percentage decrease in its volume.",
            "hi": "यदि किसी घन की प्रत्येक भुजा में $12\\%$ की कमी की जाती है, तो उसके आयतन में प्रतिशत कमी ज्ञात कीजिए।"
        },
        "options": "(a) $31.85\\%$ &emsp; (b) $36\\%$ &emsp; (c) $28.5\\%$ &emsp; (d) $33.3\\%$",
        "solution": {
            "en": "Volume $\\propto \\text{side}^3$.<br>New volume factor = $(0.88)^3 = 0.681472$.<br>Percentage decrease = $(1 - 0.681472) \\times 100\\% \\approx \\mathbf{31.85\\%}$.<br><br><strong>Answer: (a) 31.85%</strong>",
            "hi": "आयतन $\\propto \\text{भुजा}^3$।<br>नया आयतन गुणक = $(0.88)^3 = 0.681472$।<br>प्रतिशत कमी = $(1 - 0.681472) \\times 100\\% \\approx \\mathbf{31.85\\%}$ है।<br><br><strong>उत्तर: (a) 31.85%</strong>"
        }
    },
    {
        "id": "PCT_PYQ45",
        "badge": "CGL 2025 Model",
        "question": {
            "en": "The price of petrol is increased by $25\\%$. By what percent must a person reduce consumption to maintain the same expenditure?",
            "hi": "पेट्रोल की कीमत में $25\\%$ की वृद्धि हुई है। एक व्यक्ति को समान व्यय बनाए रखने के लिए खपत में कितने प्रतिशत की कमी करनी चाहिए?"
        },
        "options": "(a) $20\\%$ &emsp; (b) $25\\%$ &emsp; (c) $16.67\\%$ &emsp; (d) $15\\%$",
        "solution": {
            "en": "Reduction = $\\frac{R}{100+R} \\times 100\\% = \\frac{25}{125} \\times 100\\% = \\mathbf{20\\%}$.<br><br><strong>Answer: (a) 20%</strong>",
            "hi": "कमी = $\\frac{R}{100+R} \\times 100\\% = \\frac{25}{125} \\times 100\\% = \\mathbf{20\\%}$ है।<br><br><strong>उत्तर: (a) 20%</strong>"
        }
    },
    {
        "id": "PCT_PYQ46",
        "badge": "CGL 2025 Model",
        "question": {
            "en": "$A$'s salary is $40\\%$ more than $B$'s. By what percent is $B$'s salary less than $A$'s?",
            "hi": "$A$ का वेतन $B$ के वेतन से $40\\%$ अधिक है। $B$ का वेतन $A$ के वेतन से कितने प्रतिशत कम है?"
        },
        "options": "(a) $28.57\\%$ &emsp; (b) $40\\%$ &emsp; (c) $30\\%$ &emsp; (d) $25\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 140$.<br>Percentage less = $\\frac{40}{140} \\times 100\\% \\approx \\mathbf{28.57\\%}$.<br><br><strong>Answer: (a) 28.57%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 140$ है।<br>प्रतिशत कमी = $\\frac{40}{140} \\times 100\\% \\approx \\mathbf{28.57\\%}$ है।<br><br><strong>उत्तर: (a) 28.57%</strong>"
        }
    },
    {
        "id": "PCT_PYQ47",
        "badge": "CGL 2025 Model",
        "question": {
            "en": "The population of a city grows at $10\\%$, $20\\%$ and $25\\%$ in three successive years. What is the combined percentage increase in population over these three years?",
            "hi": "एक शहर की जनसंख्या में तीन क्रमिक वर्षों में $10\\%$, $20\\%$ और $25\\%$ की वृद्धि होती है। इन तीन वर्षों में जनसंख्या में कुल प्रतिशत वृद्धि क्या है?"
        },
        "options": "(a) $65\\%$ &emsp; (b) $55\\%$ &emsp; (c) $70\\%$ &emsp; (d) $60\\%$",
        "solution": {
            "en": "Net multiplier = $1.10 \\times 1.20 \\times 1.25 = 1.65$.<br>Combined increase = $1.65 - 1 = 0.65 = \\mathbf{65\\%}$.<br><br><strong>Answer: (a) 65%</strong>",
            "hi": "कुल गुणक = $1.10 \\times 1.20 \\times 1.25 = 1.65$।<br>कुल वृद्धि = $1.65 - 1 = 0.65 = \\mathbf{65\\%}$ है।<br><br><strong>उत्तर: (a) 65%</strong>"
        }
    }
]

file_path = "ssc-cgl/quantitative-aptitude/percentage/data/pyqs.json"
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, "w", encoding="utf-8") as f:
    json.dump(pyqs, f, ensure_ascii=False, indent=2)

print("SUCCESS: Wrote", len(pyqs), "PYQs to", file_path)
