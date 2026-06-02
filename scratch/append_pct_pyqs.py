import json
import os

new_pyqs = [
    # TYPE 1
    {
        "id": "PCT_PYQ48",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "If $45\\%$ of a number is $0.9$ more than $30\\%$ of it, what is the number?",
            "hi": "यदि किसी संख्या का $45\\%$, उसके $30\\%$ से $0.9$ अधिक है, तो वह संख्या क्या है?"
        },
        "options": "(a) $6$ &emsp; (b) $7$ &emsp; (c) $8$ &emsp; (d) $9$",
        "solution": {
            "en": "Let the number be $N$.<br>$45\\% N - 30\\% N = 0.9 \\implies 15\\% N = 0.9$<br>$N = \\frac{0.9}{0.15} = \\mathbf{6}$.<br><br><strong>Answer: (a) 6</strong>",
            "hi": "मान लीजिए संख्या $N$ है।<br>$45\\% N - 30\\% N = 0.9 \\implies 15\\% N = 0.9$<br>$N = \\frac{0.9}{0.15} = \\mathbf{6}$ है।<br><br><strong>उत्तर: (a) 6</strong>"
        }
    },
    {
        "id": "PCT_PYQ49",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "Seventy-five percent of a number is $15$ more than two-thirds of that number. Find the number.",
            "hi": "एक संख्या का $75\\%$ उस संख्या के दो-तिहाई से $15$ अधिक है। संख्या ज्ञात कीजिए।"
        },
        "options": "(a) $120$ &emsp; (b) $150$ &emsp; (c) $180$ &emsp; (d) $210$",
        "solution": {
            "en": "Let the number be $N$.<br>$75\\% = \\frac{3}{4}$ and two-thirds = \\frac{2}{3}.<br>$\\frac{3}{4}N - \\frac{2}{3}N = 15 \\implies \\frac{9-8}{12}N = 15 \\implies \\frac{N}{12} = 15 \\implies N = \\mathbf{180}$.<br><br><strong>Answer: (c) 180</strong>",
            "hi": "मान लीजिए संख्या $N$ है।<br>$75\\% = \\frac{3}{4}$ और दो-तिहाई = \\frac{2}{3}।<br>$\\frac{3}{4}N - \\frac{2}{3}N = 15 \\implies \\frac{9-8}{12}N = 15 \\implies \\frac{N}{12} = 15 \\implies N = \\mathbf{180}$ है।<br><br><strong>उत्तर: (c) 180</strong>"
        }
    },
    {
        "id": "PCT_PYQ50",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "The difference between $20\\%$ of a number and $10\\%$ of the same number is $120$. What is the number?",
            "hi": "एक संख्या के $20\\%$ और उसी संख्या के $10\\%$ के बीच का अंतर $120$ है। संख्या क्या है?"
        },
        "options": "(a) $1000$ &emsp; (b) $1100$ &emsp; (c) $1200$ &emsp; (d) $1400$",
        "solution": {
            "en": "Let the number be $N$.<br>$20\\% N - 10\\% N = 120 \\implies 10\\% N = 120 \\implies N = \\mathbf{1200}$.<br><br><strong>Answer: (c) 1200</strong>",
            "hi": "मान लीजिए संख्या $N$ है।<br>$20\\% N - 10\\% N = 120 \\implies 10\\% N = 120 \\implies N = \\mathbf{1200}$ है।<br><br><strong>उत्तर: (c) 1200</strong>"
        }
    },
    # TYPE 2
    {
        "id": "PCT_PYQ51",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "If $B$ is $25\\%$ more than $A$, and $C$ is $20\\%$ more than $B$, then what is $A : C$?",
            "hi": "यदि B, A से $25\\%$ अधिक है, और C, B से $20\\%$ अधिक है, तो $A : C$ क्या है?"
        },
        "options": "(a) $3:2$ &emsp; (b) $2:3$ &emsp; (c) $5:4$ &emsp; (d) $4:5$",
        "solution": {
            "en": "Let $A = 100$.<br>$B$ is $25\\%$ more than $A \\implies B = 125$.<br>$C$ is $20\\%$ more than $B \\implies C = 125 \\times 1.20 = 150$.<br>Ratio $A : C = 100 : 150 = \\mathbf{2:3}$.<br><br><strong>Answer: (b) 2:3</strong>",
            "hi": "मान लीजिए $A = 100$ है।<br>B, A से $25\\%$ अधिक है $\implies B = 125$।<br>C, B से $20\\%$ अधिक है $\implies C = 125 \\times 1.20 = 150$।<br>अनुपात $A : C = 100 : 150 = \\mathbf{2:3}$ है।<br><br><strong>उत्तर: (b) 2:3</strong>"
        }
    },
    {
        "id": "PCT_PYQ52",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "If $A$ is $25\\%$ more than $B$, and $B$ is $20\\%$ more than $C$, then what is $A : C$?",
            "hi": "यदि A, B से $25\\%$ अधिक है, और B, C से $20\\%$ अधिक है, तो $A : C$ क्या है?"
        },
        "options": "(a) $3:2$ &emsp; (b) $2:3$ &emsp; (c) $6:5$ &emsp; (d) $5:4$",
        "solution": {
            "en": "Let $C = 100$.<br>$B$ is $20\\%$ more than $C \\implies B = 120$.<br>$A$ is $25\\%$ more than $B \\implies A = 120 \\times 1.25 = 150$.<br>Ratio $A : C = 150 : 100 = \\mathbf{3:2}$.<br><br><strong>Answer: (a) 3:2</strong>",
            "hi": "मान लीजिए $C = 100$ है।<br>B, C से $20\\%$ अधिक है $\implies B = 120$।<br>A, B से $25\\%$ अधिक है $\implies A = 120 \\times 1.25 = 150$।<br>अनुपात $A : C = 150 : 100 = \\mathbf{3:2}$ है।<br><br><strong>उत्तर: (a) 3:2</strong>"
        }
    },
    {
        "id": "PCT_PYQ53",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A student's marks in Mathematics were $20\\%$ more than in Physics. If he scored $72$ in Physics, how many marks did he score in Mathematics?",
            "hi": "एक छात्र के गणित में अंक भौतिकी से $20\\%$ अधिक थे। यदि उसने भौतिकी में $72$ अंक प्राप्त किए, तो उसने गणित में कितने अंक प्राप्त किए?"
        },
        "options": "(a) $82.4$ &emsp; (b) $88.4$ &emsp; (c) $84.4$ &emsp; (d) $86.4$",
        "solution": {
            "en": "Physics marks = $72$.<br>Mathematics marks = $72 \\times (1 + \\frac{20}{100}) = 72 \\times 1.20 = \\mathbf{86.4}$.<br><br><strong>Answer: (d) 86.4</strong>",
            "hi": "भौतिकी में अंक = $72$।<br>गणित में अंक = $72 \\times (1 + \\frac{20}{100}) = 72 \\times 1.20 = \\mathbf{86.4}$ है।<br><br><strong>उत्तर: (d) 86.4</strong>"
        }
    },
    {
        "id": "PCT_PYQ54",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "Three numbers are such that the second is $150\\%$ of the first, and the third is $80\\%$ of the second. What is the ratio of the first to the third?",
            "hi": "तीन संख्याएँ इस प्रकार हैं कि दूसरी, पहली का $150\\%$ है और तीसरी, दूसरी का $80\\%$ है। पहली का तीसरी से अनुपात क्या है?"
        },
        "options": "(a) $5:6$ &emsp; (b) $2:3$ &emsp; (c) $5:4$ &emsp; (d) $5:8$",
        "solution": {
            "en": "Let the first number be $100$.<br>Second number = $150\\% \\text{ of } 100 = 150$.<br>Third number = $80\\% \\text{ of } 150 = 120$.<br>Ratio of first to third = $100 : 120 = \\mathbf{5:6}$.<br><br><strong>Answer: (a) 5:6</strong>",
            "hi": "मान लीजिए पहली संख्या $100$ है।<br>दूसरी संख्या = $100$ का $150\\% = 150$।<br>तीसरी संख्या = $150$ का $80\\% = 120$।<br>पहली का तीसरी से अनुपात = $100 : 120 = \\mathbf{5:6}$ है।<br><br><strong>उत्तर: (a) 5:6</strong>"
        }
    },
    # TYPE 3
    {
        "id": "PCT_PYQ55",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A man spends $80\\%$ of his income. His income has increased by $25\\%$, but his expenditure remains the same. By what percent have his savings increased?",
            "hi": "एक व्यक्ति अपनी आय का $80\\%$ खर्च करता है। उसकी आय में $25\\%$ की वृद्धि हुई है, लेकिन उसका व्यय समान रहता है। उसकी बचत में कितने प्रतिशत की वृद्धि हुई है?"
        },
        "options": "(a) $125\\%$ &emsp; (b) $150\\%$ &emsp; (c) $100\\%$ &emsp; (d) $75\\%$",
        "solution": {
            "en": "Let Income = $100$, Expenditure = $80$, Savings = $20$.<br>New Income = $125$. Expenditure remains = $80$.<br>New Savings = $125 - 80 = 45$.<br>Increase in savings = $45 - 20 = 25$.<br>Percentage increase = $\\frac{25}{20} \\times 100\\% = \\mathbf{125\\%}$.<br><br><strong>Answer: (a) 125%</strong>",
            "hi": "मान लीजिए आय = $100$, व्यय = $80$, बचत = $20$ है।<br>नई आय = $125$। व्यय समान रहता है = $80$।<br>नई बचत = $125 - 80 = 45$।<br>बचत में वृद्धि = $45 - 20 = 25$।<br>प्रतिशत वृद्धि = $\\frac{25}{20} \\times 100\\% = \\mathbf{125\\%}$ है।<br><br><strong>उत्तर: (a) 125%</strong>"
        }
    },
    {
        "id": "PCT_PYQ56",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A man spends $75\\%$ of his income. Due to inflation, his expenses increase by $20\\%$, and his income increases by $10\\%$. What is the percentage change in his savings?",
            "hi": "एक व्यक्ति अपनी आय का $75\\%$ खर्च करता है। मुद्रास्फीति के कारण, उसके खर्चों में $20\\%$ की वृद्धि होती है, और उसकी आय में $10\\%$ की वृद्धि होती है। उसकी बचत में प्रतिशत परिवर्तन क्या है?"
        },
        "options": "(a) $30\\%$ decrease &emsp; (b) $40\\%$ decrease &emsp; (c) $10\\%$ decrease &emsp; (d) $20\\%$ decrease",
        "solution": {
            "en": "Let Income = $100$, Expenditure = $75$, Savings = $25$.<br>New Income = $110$.<br>New Expenditure = $75 \\times 1.20 = 90$.<br>New Savings = $110 - 90 = 20$.<br>Decrease in savings = $25 - 20 = 5$.<br>Percentage decrease = $\\frac{5}{25} \\times 100\\% = \\mathbf{20\\% \\text{ decrease}}$.<br><br><strong>Answer: (d) 20% decrease</strong>",
            "hi": "मान लीजिए आय = $100$, व्यय = $75$, बचत = $25$ है।<br>नई आय = $110$।<br>नया व्यय = $75$ का $120\\% = 90$।<br>नई बचत = $110 - 90 = 20$।<br>बचत में कमी = $25 - 20 = 5$।<br>प्रतिशत कमी = $\\frac{5}{25} \\times 100\\% = \\mathbf{20\\% \\text{ कमी}}$ है।<br><br><strong>उत्तर: (d) 20% decrease</strong>"
        }
    },
    {
        "id": "PCT_PYQ57",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A man spends $70\\%$ of his income. His income increases by $10\\%$ and his expenditure by $5\\%$. What is the percentage increase in his savings?",
            "hi": "एक व्यक्ति अपनी आय का $70\\%$ खर्च करता है। उसकी आय में $10\\%$ की वृद्धि होती है और उसके व्यय में $5\\%$ की। उसकी बचत में प्रतिशत वृद्धि क्या है?"
        },
        "options": "(a) $21.67\\%$ &emsp; (b) $31.67\\%$ &emsp; (c) $41.67\\%$ &emsp; (d) $51.67\\%$.",
        "solution": {
            "en": "Let Income = $100$, Expenditure = $70$, Savings = $30$.<br>New Income = $110$.<br>New Expenditure = $70 \\times 1.05 = 73.5$.<br>New Savings = $110 - 73.5 = 36.5$.<br>Increase in savings = $36.5 - 30 = 6.5$.<br>Percentage increase = $\\frac{6.5}{30} \\times 100\\% \\approx \\mathbf{21.67\\%}$.<br><br><strong>Answer: (a) 21.67%</strong>",
            "hi": "मान लीजिए आय = $100$, व्यय = $70$, बचत = $30$ है।<br>नई आय = $110$।<br>नया व्यय = $70$ का $105\\% = 73.5$।<br>नई बचत = $110 - 73.5 = 36.5$।<br>बचत में वृद्धि = $36.5 - 30 = 6.5$।<br>प्रतिशत वृद्धि = $\\frac{6.5}{30} \\times 100\\% \\approx \\mathbf{21.67\\%}$ है।<br><br><strong>उत्तर: (a) 21.67%</strong>"
        }
    },
    {
        "id": "PCT_PYQ58",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "An employee contributes $20\\%$ of their salary to charity. From the remaining, $40\\%$ is allocated to investments. The rest is divided for education and travel in the ratio $7:5$. If the expense on travel is ₹$6,000$, what is the employee's total salary?",
            "hi": "एक कर्मचारी अपने वेतन का $20\\%$ दान में देता है। शेष में से, $40\\%$ निवेश के लिए आवंटित किया जाता है। शेष राशि को शिक्षा और यात्रा के लिए $7:5$ के अनुपात में विभाजित किया जाता है। यदि यात्रा पर खर्च ₹$6,000$ है, तो कर्मचारी का कुल वेतन क्या है?"
        },
        "options": "(a) ₹$30,000$ &emsp; (b) ₹$25,000$ &emsp; (c) ₹$35,000$ &emsp; (d) ₹$40,000$",
        "solution": {
            "en": "Let total salary be $S$.<br>Remaining after charity = $80\\%$.<br>Remaining after investments = $60\\% \\text{ of } 80\\% = 48\\%$.<br>Travel share = $\\frac{5}{12} \\times 48\\% = 20\\%$.<br>Given $20\\% \\text{ of } S = ₹6,000 \\implies S = \\mathbf{₹30,000}$.<br><br><strong>Answer: (a) ₹30,000</strong>",
            "hi": "मान लीजिए कुल वेतन $S$ है।<br>दान के बाद शेष = $80\\%$।<br>निवेश के बाद शेष = $80\\%$ का $60\\% = 48\\%$।<br>यात्रा का हिस्सा = $\\frac{5}{12} \\times 48\\% = 20\\%$।<br>दिया गया है $S$ का $20\\% = ₹6,000 \\implies S = \\mathbf{₹30,000}$ है।<br><br><strong>उत्तर: (a) ₹30,000</strong>"
        }
    },
    {
        "id": "PCT_PYQ59",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "Out of her total monthly income, a woman spends $60\\%$ on household expenses and $15\\%$ on savings. What percentage of her income is spent on other items?",
            "hi": "अपनी कुल मासिक आय में से, एक महिला घरेलू खर्चों पर $60\\%$ और बचत पर $15\\%$ खर्च करती है। उसकी आय का कितना प्रतिशत अन्य मदों पर खर्च होता है?"
        },
        "options": "(a) $35\\%$ &emsp; (b) $25\\%$ &emsp; (c) $20\\%$ &emsp; (d) $30\\%$",
        "solution": {
            "en": "Percentage spent on other items = $100\\% - (60\\% + 15\\%) = \\mathbf{25\\%}$.<br><br><strong>Answer: (b) 25%</strong>",
            "hi": "अन्य मदों पर खर्च का प्रतिशत = $100\\% - (60\\% + 15\\%) = \\mathbf{25\\%}$ है।<br><br><strong>उत्तर: (b) 25%</strong>"
        }
    },
    # TYPE 4
    {
        "id": "PCT_PYQ60",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "$A$'s salary is $40\\%$ more than $B$'s. If $B$'s salary increases by $20\\%$ and $A$'s increases by $x\\%$, then $A$'s new salary becomes $25\\%$ more than $B$'s new salary. Find the value of $x$.",
            "hi": "A का वेतन B के वेतन से $40\\%$ अधिक है। यदि B के वेतन में $20\\%$ की वृद्धि होती है और A के वेतन में $x\\%$ की वृद्धि होती है, तो A का नया वेतन B के नए वेतन से $25\\%$ अधिक हो जाता है। $x$ का मान ज्ञात कीजिए।"
        },
        "options": "(a) $2.5\\%$ &emsp; (b) $7.14\\%$ &emsp; (c) $10.63\\%$ &emsp; (d) $15.6\\%$",
        "solution": {
            "en": "Let $B = 100 \\implies A = 140$.<br>New $B = 120$.<br>New $A$ must be $25\\%$ more than New $B \\implies$ New $A = 120 \\times 1.25 = 150$.<br>Increase in $A = 150 - 140 = 10$.<br>Percentage increase $x = \\frac{10}{140} \\times 100\\% \\approx \\mathbf{7.14\\%}$.<br><br><strong>Answer: (b) 7.14%</strong>",
            "hi": "मान लीजिए $B = 100 \\implies A = 140$ है।<br>नया $B = 120$।<br>नया $A$, नए $B$ से $25\\%$ अधिक होना चाहिए $\implies$ नया $A = 120 \\times 1.25 = 150$।<br>A में वृद्धि = $150 - 140 = 10$।<br>प्रतिशत वृद्धि $x = \\frac{10}{140} \\times 100\\% \\approx \\mathbf{7.14\\%}$ है।<br><br><strong>उत्तर: (b) 7.14%</strong>"
        }
    },
    # TYPE 5
    {
        "id": "PCT_PYQ61",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A number was mistakenly increased by $25\\%$ instead of decreased by $20\\%$. By what percent is the final result more than the CORRECT value?",
            "hi": "एक संख्या में गलती से $20\\%$ की कमी करने के बजाय $25\\%$ की वृद्धि कर दी गई। अंतिम परिणाम सही मान से कितने प्रतिशत अधिक है?"
        },
        "options": "(a) $56.25\\%$ &emsp; (b) $50.5\\%$ &emsp; (c) $45\\%$ &emsp; (d) $60.25\\%$",
        "solution": {
            "en": "Let the number be $100$.<br>Correct value = $100 - 20\\% = 80$.<br>Wrong value = $100 + 25\\% = 125$.<br>Difference = $125 - 80 = 45$.<br>Percentage more = $\\frac{45}{80} \\times 100\\% = \\mathbf{56.25\\%}$.<br><br><strong>Answer: (a) 56.25%</strong>",
            "hi": "मान लीजिए संख्या $100$ है।<br>सही मान = $100 - 20\\% = 80$।<br>गलत मान = $100 + 25\\% = 125$।<br>अंतर = $125 - 80 = 45$।<br>प्रतिशत अधिक = $\\frac{45}{80} \\times 100\\% = \\mathbf{56.25\\%}$ है।<br><br><strong>उत्तर: (a) 56.25%</strong>"
        }
    },
    {
        "id": "PCT_PYQ62",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "Due to an error, a shopkeeper increases the selling price of a ₹$500$ item by $10\\%$ instead of decreasing it by $10\\%$. What is the percentage increase in price due to this error compared to the correct price?",
            "hi": "एक त्रुटि के कारण, एक दुकानदार ₹$500$ की वस्तु के विक्रय मूल्य में $10\\%$ की कमी करने के बजाय $10\\%$ की वृद्धि कर देता है। इस त्रुटि के कारण सही मूल्य की तुलना में मूल्य में प्रतिशत वृद्धि क्या है?"
        },
        "options": "(a) $20.22\\%$ &emsp; (b) $22.22\\%$ &emsp; (c) $18.18\\%$ &emsp; (d) $25\\%$",
        "solution": {
            "en": "Correct SP = $500 \\times 0.90 = 450$.<br>Wrong SP = $500 \\times 1.10 = 550$.<br>Increase = $550 - 450 = 100$.<br>Percentage increase = $\\frac{100}{450} \\times 100\\% \\approx \\mathbf{22.22\\%}$.<br><br><strong>Answer: (b) 22.22%</strong>",
            "hi": "सही SP = $500 \\times 0.90 = 450$।<br>गलत SP = $500 \\times 1.10 = 550$।<br>वृद्धि = $550 - 450 = 100$।<br>प्रतिशत वृद्धि = $\\frac{100}{450} \\times 100\\% \\approx \\mathbf{22.22\\%}$ है।<br><br><strong>उत्तर: (b) 22.22%</strong>"
        }
    },
    # TYPE 6
    {
        "id": "PCT_PYQ63",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "The population of a village increases by $8\\%$ annually. If the current population is $58,320$, what was it two years ago (approx)?",
            "hi": "एक गाँव की जनसंख्या प्रतिवर्ष $8\\%$ बढ़ती है। यदि वर्तमान जनसंख्या $58,320$ है, तो दो वर्ष पहले यह कितनी थी (लगभग)?"
        },
        "options": "(a) $50,000$ &emsp; (b) $49,900$ &emsp; (c) $49,980$ &emsp; (d) $49,800$",
        "solution": {
            "en": "Let population two years ago be $P$.<br>$P \\times (1.08)^2 = 58,320 \\implies P \\times 1.1664 = 58,320 \\implies P = \\mathbf{50,000}$.<br><br><strong>Answer: (a) 50,000</strong>",
            "hi": "मान लीजिए दो वर्ष पहले की जनसंख्या $P$ थी।<br>$P \\times (1.08)^2 = 58,320 \\implies P \\times 1.1664 = 58,320 \\implies P = \\mathbf{50,000}$ है।<br><br><strong>उत्तर: (a) 50,000</strong>"
        }
    },
    {
        "id": "PCT_PYQ64",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A town has males and females in a ratio of $3:2$. After 5 years, the male population increases by $10\\%$ and the female population by $25\\%$. What is the new ratio of males to females?",
            "hi": "एक शहर में पुरुषों और महिलाओं का अनुपात $3:2$ है। 5 वर्षों के बाद, पुरुषों की जनसंख्या में $10\\%$ और महिलाओं की जनसंख्या में $25\\%$ की वृद्धि होती है। नया अनुपात क्या है?"
        },
        "options": "(a) $3:2$ &emsp; (b) $33:25$ &emsp; (c) $66:50$ &emsp; (d) $6:5$",
        "solution": {
            "en": "Let males = $30$, females = $20$.<br>New males = $30 \\times 1.10 = 33$.<br>New females = $20 \\times 1.25 = 25$.<br>New ratio = \\mathbf{33:25}.<br><br><strong>Answer: (b) 33:25</strong>",
            "hi": "मान लीजिए पुरुष = $30$, महिलाएं = $20$ है।<br>नए पुरुष = $30 \\times 1.10 = 33$।<br>नई महिलाएं = $20 \\times 1.25 = 25$।<br>नया अनुपात = \\mathbf{33:25} है।<br><br><strong>उत्तर: (b) 33:25</strong>"
        }
    },
    # TYPE 7
    {
        "id": "PCT_PYQ65",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "The expenditure of a household on food, clothing, and entertainment is in the ratio $2:4:4$. In the coming year, food is expected to fall by $10\\%$, clothing to rise by $5\\%$, and entertainment to fall by $15\\%$. What is the percent change in total household expenditure?",
            "hi": "भोजन, कपड़े और मनोरंजन पर एक परिवार का व्यय $2:4:4$ के अनुपात में है। आने वाले वर्ष में, भोजन में $10\\%$ की कमी, कपड़ों में $5\\%$ की वृद्धि और मनोरंजन में $15\\%$ की कमी होने की उम्मीद है। कुल घरेलू व्यय में प्रतिशत परिवर्तन क्या है?"
        },
        "options": "(a) $6\\%$ decrease &emsp; (b) $5\\%$ decrease &emsp; (c) $4\\%$ decrease &emsp; (d) $7\\%$ decrease",
        "solution": {
            "en": "Let expenditures be: Food = $20$, Clothing = $40$, Entertainment = $40$. Total = $100$.<br>New Food = $20 \\times 0.90 = 18$.<br>New Clothing = $40 \\times 1.05 = 42$.<br>New Entertainment = $40 \\times 0.85 = 34$.<br>New Total = $18 + 42 + 34 = 94$.<br>Decrease = $100 - 94 = 6 \\implies \\mathbf{6\\% \\text{ decrease}}$.<br><br><strong>Answer: (a) 6% decrease</strong>",
            "hi": "मान लीजिए व्यय: भोजन = $20$, कपड़े = $40$, मनोरंजन = $40$ है। कुल = $100$।<br>नया भोजन = $20 \\times 0.90 = 18$।<br>नए कपड़े = $40 \\times 1.05 = 42$।<br>नया मनोरंजन = $40 \\times 0.85 = 34$।<br>नया कुल = $18 + 42 + 34 = 94$।<br>कमी = $100 - 94 = 6 \\implies \\mathbf{6\\% \\text{ कमी}}$ है।<br><br><strong>उत्तर: (a) 6% decrease</strong>"
        }
    },
    # TYPE 8
    {
        "id": "PCT_PYQ66",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "In an election, $80\\%$ of eligible voters cast their votes. Of these votes, $5\\%$ were declared invalid. If the winning candidate received $11,400$ votes, which accounted for $60\\%$ of the total valid votes, what was the total number of eligible voters enrolled?",
            "hi": "एक चुनाव में, $80\\%$ पात्र मतदाताओं ने अपने मत डाले। इनमें से $5\\%$ मत अमान्य घोषित कर दिए गए। यदि विजेता उम्मीदवार को $11,400$ मत मिले, जो कुल वैध मतों का $60\\%$ था, तो कुल नामांकित पात्र मतदाताओं की संख्या क्या थी?"
        },
        "options": "(a) $25,000$ &emsp; (b) $30,000$ &emsp; (c) $20,000$ &emsp; (d) $28,000$",
        "solution": {
            "en": "Let eligible voters be $V$.<br>Total cast = $0.80V$.<br>Valid votes = $0.95 \\times 0.80V = 0.76V$.<br>Winner's votes = $60\\% \\text{ of } 0.76V = 0.456V$.<br>Given: $0.456V = 11,400 \\implies V = \\frac{11,400}{0.456} = \\mathbf{25,000}$.<br><br><strong>Answer: (a) 25,000</strong>",
            "hi": "मान लीजिए पात्र मतदाता $V$ हैं।<br>कुल डाले गए मत = $0.80V$।<br>वैध मत = $0.95 \\times 0.80V = 0.76V$।<br>विजेता के मत = $0.76V$ का $60\\% = 0.456V$।<br>दिया गया है: $0.456V = 11,400 \\implies V = \\frac{11,400}{0.456} = \\mathbf{25,000}$ है।<br><br><strong>उत्तर: (a) 25,000</strong>"
        }
    },
    # TYPE 9
    {
        "id": "PCT_PYQ67",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A buyer gets two successive discounts of $20\\%$ and $10\\%$ on a ₹$1,000$ item. What is the final price paid?",
            "hi": "एक खरीदार को ₹$1,000$ की वस्तु पर $20\\%$ और $10\\%$ की दो क्रमिक छूट मिलती है। भुगतान किया गया अंतिम मूल्य क्या है?"
        },
        "options": "(a) ₹$700$ &emsp; (b) ₹$720$ &emsp; (c) ₹$740$ &emsp; (d) ₹$750$",
        "solution": {
            "en": "Final Price = $1000 \\times 0.80 \\times 0.90 = \\mathbf{₹720}$.<br><br><strong>Answer: (b) ₹720</strong>",
            "hi": "अंतिम मूल्य = $1000 \\times 0.80 \\times 0.90 = \\mathbf{₹720}$ है।<br><br><strong>उत्तर: (b) ₹720</strong>"
        }
    },
    {
        "id": "PCT_PYQ68",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A television set has a marked price of ₹$20,000$. It is sold after two successive discounts. If the first discount is $15\\%$ and the final selling price is ₹$15,300$, what is the percentage of the second discount?",
            "hi": "एक टेलीविजन सेट का अंकित मूल्य ₹$20,000$ है। इसे दो क्रमिक छूटों के बाद बेचा जाता है। यदि पहली छूट $15\\%$ है और अंतिम विक्रय मूल्य ₹$15,300$ है, तो दूसरी छूट का प्रतिशत क्या है?"
        },
        "options": "(a) $8\\%$ &emsp; (b) $9\\%$ &emsp; (c) $10\\%$ &emsp; (d) $12\\%$",
        "solution": {
            "en": "Price after 1st discount = $20000 \\times 0.85 = 17000$.<br>Let second discount be $d\\%$.<br>$17000 \\times (1 - \\frac{d}{100}) = 15300 \\implies 1 - \\frac{d}{100} = \\frac{15300}{17000} = 0.90 \\implies d = \\mathbf{10\\%}$.<br><br><strong>Answer: (c) 10%</strong>",
            "hi": "पहली छूट के बाद मूल्य = $20000 \\times 0.85 = 17000$।<br>मान लीजिए दूसरी छूट $d\\%$ है।<br>$17000 \\times (1 - \\frac{d}{100}) = 15300 \\implies 1 - \\frac{d}{100} = \\frac{15300}{17000} = 0.90 \\implies d = \\mathbf{10\\%}$ है।<br><br><strong>उत्तर: (c) 10%</strong>"
        }
    },
    {
        "id": "PCT_PYQ69",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A pair of shoes is listed at ₹$800$. After two successive discounts, it is sold for ₹$612$. If the first discount offered was $10\\%$, what was the second discount?",
            "hi": "जूते की एक जोड़ी का मूल्य ₹$800$ सूचीबद्ध है। दो क्रमिक छूटों के बाद, इसे ₹$612$ में बेचा जाता है। यदि दी गई पहली छूट $10\\%$ थी, तो दूसरी छूट क्या थी?"
        },
        "options": "(a) $12\\%$ &emsp; (b) $14\\%$ &emsp; (c) $15\\%$ &emsp; (d) $16\\%$",
        "solution": {
            "en": "Price after 1st discount = $800 \\times 0.90 = 720$.<br>Let second discount be $d\\%$.<br>$720 \\times (1 - \\frac{d}{100}) = 612 \\implies 1 - \\frac{d}{100} = \\frac{612}{720} = 0.85 \\implies d = \\mathbf{15\\%}$.<br><br><strong>Answer: (c) 15%</strong>",
            "hi": "पहली छूट के बाद मूल्य = $800 \\times 0.90 = 720$।<br>मान लीजिए दूसरी छूट $d\\%$ है।<br>$720 \\times (1 - \\frac{d}{100}) = 612 \\implies 1 - \\frac{d}{100} = \\frac{612}{720} = 0.85 \\implies d = \\mathbf{15\\%}$ है।<br><br><strong>उत्तर: (c) 15%</strong>"
        }
    },
    {
        "id": "PCT_PYQ70",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "If the selling price of an article is $90\\%$ of its marked price and the cost price is $80\\%$ of the marked price, what is the profit percentage?",
            "hi": "यदि किसी वस्तु का विक्रय मूल्य उसके अंकित मूल्य का $90\\%$ है और क्रय मूल्य अंकित मूल्य का $80\\%$ है, तो लाभ प्रतिशत क्या है?"
        },
        "options": "(a) $10\\%$ &emsp; (b) $12.5\\%$ &emsp; (c) $15\\%$ &emsp; (d) $20.5\\%$",
        "solution": {
            "en": "Let Marked Price (MP) = $100$.<br>Selling Price (SP) = $90$. Cost Price (CP) = $80$.<br>Profit = $SP - CP = 90 - 80 = 10$.<br>Profit percentage = $\\frac{10}{80} \\times 100\\% = \\mathbf{12.5\\%}$.<br><br><strong>Answer: (b) 12.5%</strong>",
            "hi": "मान लीजिए अंकित मूल्य (MP) = $100$ है।<br>विक्रय मूल्य (SP) = $90$। क्रय मूल्य (CP) = $80$।<br>लाभ = $SP - CP = 90 - 80 = 10$।<br>लाभ प्रतिशत = $\\frac{10}{80} \\times 100\\% = \\mathbf{12.5\\%}$ है।<br><br><strong>उत्तर: (b) 12.5%</strong>"
        }
    },
    {
        "id": "PCT_PYQ71",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A store offers a $25\\%$ discount but charges $5\\%$ VAT on the discounted price. If the marked price is ₹$1,600$, what is the final amount paid?",
            "hi": "एक स्टोर $25\\%$ की छूट देता है लेकिन रियायती मूल्य पर $5\\%$ वैट लेता है। यदि अंकित मूल्य ₹$1,600$ है, तो भुगतान की गई अंतिम राशि क्या है?"
        },
        "options": "(a) ₹$1,200$ &emsp; (b) ₹$1,260$ &emsp; (c) ₹$1,275$ &emsp; (d) ₹$1,320$",
        "solution": {
            "en": "Discounted Price = $1600 \\times 0.75 = 1200$.<br>Final price with VAT = $1200 \\times 1.05 = \\mathbf{₹1,260}$.<br><br><strong>Answer: (b) ₹1,260</strong>",
            "hi": "छूट के बाद मूल्य = $1600 \\times 0.75 = 1200$।<br>वैट के साथ अंतिम मूल्य = $1200 \\times 1.05 = \\mathbf{₹1,260}$ है।<br><br><strong>उत्तर: (b) ₹1,260</strong>"
        }
    },
    {
        "id": "PCT_PYQ72",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A shopkeeper offers a festival deal: 'Flat ₹$150$ off on every purchase above ₹$1,000$.' What is the effective discount percentage if a buyer purchases an item marked ₹$1,200$?",
            "hi": "एक दुकानदार एक त्योहारी डील पेश करता है: '₹$1,000$ से अधिक की प्रत्येक खरीद पर ₹$150$ की फ्लैट छूट।' यदि कोई खरीदार ₹$1,200$ अंकित मूल्य वाली वस्तु खरीदता है तो प्रभावी छूट प्रतिशत क्या है?"
        },
        "options": "(a) $12.5\\%$ &emsp; (b) $15\\%$ &emsp; (c) $10\\%$ &emsp; (d) $14.28\\%$",
        "solution": {
            "en": "Effective Discount = $₹150$. Marked Price = $₹1,200$.<br>Effective Discount Percentage = $\\frac{150}{1200} \\times 100\\% = \\mathbf{12.5\\%}$.<br><br><strong>Answer: (a) 12.5%</strong>",
            "hi": "प्रभावी छूट = $₹150$। अंकित मूल्य = $₹1,200$।<br>प्रभावी छूट प्रतिशत = $\\frac{150}{1200} \\times 100\\% = \\mathbf{12.5\\%}$ है।<br><br><strong>उत्तर: (a) 12.5%</strong>"
        }
    },
    {
        "id": "PCT_PYQ73",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A bookshop advertises: 'Buy 4 books and get the 5th at a $50\\%$ discount.' If the marked price of each book is ₹$480$, what is the effective percentage discount the customer receives on the total purchase of 5 books?",
            "hi": "एक किताबों की दुकान विज्ञापन देती है: '4 किताबें खरीदें और 5वीं पर $50\\%$ की छूट पाएं।' यदि प्रत्येक पुस्तक का अंकित मूल्य ₹$480$ है, तो ग्राहक को 5 पुस्तकों की कुल खरीद पर प्राप्त प्रभावी प्रतिशत छूट क्या है?"
        },
        "options": "(a) $10\\%$ &emsp; (b) $12\\%$ &emsp; (c) $8\\%$ &emsp; (d) $15\\%$",
        "solution": {
            "en": "Normal cost of 5 books = $5 \\times 480 = 2400$.<br>Customer pays = $4 \\times 480 + (0.50 \\times 480) = 1920 + 240 = 2160$.<br>Discount amount = $2400 - 2160 = 240$.<br>Effective discount percentage = $\\frac{240}{2400} \\times 100\\% = \\mathbf{10\\%}$.<br><br><strong>Answer: (a) 10%</strong>",
            "hi": "5 पुस्तकों का सामान्य मूल्य = $5 \\times 480 = 2400$।<br>ग्राहक भुगतान करता है = $4 \\times 480 + (0.50 \\times 480) = 1920 + 240 = 2160$।<br>छूट की राशि = $2400 - 2160 = 240$।<br>प्रभावी छूट प्रतिशत = $\\frac{240}{2400} \\times 100\\% = \\mathbf{10\\%}$ है।<br><br><strong>उत्तर: (a) 10%</strong>"
        }
    },
    {
        "id": "PCT_PYQ74",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A seller offers a combo deal: 'Buy 3 shirts for the price of 2.' If each shirt costs ₹$300$, what is the effective discount/loss percentage for the transaction value compared to list price?",
            "hi": "एक विक्रेता कॉम्बो डील प्रदान करता है: '2 की कीमत पर 3 शर्ट खरीदें।' यदि प्रत्येक शर्ट की कीमत ₹$300$ है, तो सूची मूल्य की तुलना में लेनदेन मूल्य के लिए प्रभावी छूट/हानि प्रतिशत क्या है?"
        },
        "options": "(a) $25.33\\%$ &emsp; (b) $33.33\\%$ &emsp; (c) $30\\%$ &emsp; (d) $20\\%$",
        "solution": {
            "en": "Buyer gets 3 shirts for the price of 2 shirts.<br>Effective discount = 1 shirt free out of 3 shirts.<br>Discount Percentage = $\\frac{1}{3} \\times 100\\% = \\mathbf{33.33\\%}$.<br><br><strong>Answer: (b) 33.33%</strong>",
            "hi": "क्रेता को 2 शर्ट की कीमत पर 3 शर्ट मिलती हैं।<br>प्रभावी छूट = 3 शर्ट में से 1 शर्ट मुफ्त।<br>छूट प्रतिशत = $\\frac{1}{3} \\times 100\\% = \\mathbf{33.33\\%}$ है।<br><br><strong>उत्तर: (b) 33.33%</strong>"
        }
    },
    # TYPE 10
    {
        "id": "PCT_PYQ75",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A businessman invests ₹$50,000$ in items, spends ₹$5,000$ on transportation and ₹$3,000$ on storage. If he sells the items for ₹$63,000$, what is the profit or loss percentage?",
            "hi": "एक व्यवसायी वस्तुओं में ₹$50,000$ का निवेश करता है, परिवहन पर ₹$5,000$ और भंडारण पर ₹$3,000$ खर्च करता है। यदि वह वस्तुओं को ₹$63,000$ में बेचता है, तो लाभ या हानि प्रतिशत क्या है?"
        },
        "options": "(a) $8.62\\%$ profit &emsp; (b) $8.62\\%$ loss &emsp; (c) $10\\%$ profit &emsp; (d) $9\\%$ loss",
        "solution": {
            "en": "Total Cost Price (CP) = $50000 + 5000 + 3000 = 58000$.<br>Selling Price (SP) = $63000$.<br>Since $SP > CP$, it is a Profit = $63000 - 58000 = 5000$.<br>Profit percentage = $\\frac{5000}{58000} \\times 100\\% \\approx \\mathbf{8.62\\% \\text{ profit}}$.<br><br><strong>Answer: (a) 8.62% profit</strong>",
            "hi": "कुल क्रय मूल्य (CP) = $50000 + 5000 + 3000 = 58000$।<br>विक्रय मूल्य (SP) = $63000$।<br>चूंकि $SP > CP$ है, इसलिए लाभ = $63000 - 58000 = 5000$।<br>लाभ प्रतिशत = $\\frac{5000}{58000} \\times 100\\% \\approx \\mathbf{8.62\\% \\text{ लाभ}}$ है।<br><br><strong>उत्तर: (a) 8.62% profit</strong>"
        }
    },
    {
        "id": "PCT_PYQ76",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A shopkeeper bought 100 pens at ₹$10$ each. He sold 60 pens at $20\\%$ profit and the rest at $10\\%$ loss. What is the overall profit or loss percentage?",
            "hi": "एक दुकानदार ने ₹$10$ प्रति पेन की दर से 100 पेन खरीदे। उसने 60 पेन $20\\%$ लाभ पर और शेष को $10\\%$ हानि पर बेचा। कुल लाभ या हानि प्रतिशत क्या है?"
        },
        "options": "(a) $8\\%$ profit (or $2\\%$ per options) &emsp; (b) $1\\%$ loss &emsp; (c) $3\\%$ loss &emsp; (d) $3\\%$ profit",
        "solution": {
            "en": "Total Cost Price = $100 \\times 10 = 1000$.<br>SP of 60 pens = $60 \\times 12 = 720$.<br>SP of 40 pens = $40 \\times 9 = 360$.<br>Total Selling Price = $720 + 360 = 1080$.<br>Profit = $1080 - 1000 = 80$.<br>Overall Profit Percentage = $\\frac{80}{1000} \\times 100\\% = \\mathbf{8\\%}$ (or $8\\%$ overall profit).<br><br><strong>Answer: (a) 8% profit</strong>",
            "hi": "कुल क्रय मूल्य = $100 \\times 10 = 1000$।<br>60 पेनों का SP = $60 \\times 12 = 720$।<br>40 पेनों का SP = $40 \\times 9 = 360$।<br>कुल विक्रय मूल्य = $720 + 360 = 1080$।<br>लाभ = $1080 - 1000 = 80$।<br>कुल लाभ प्रतिशत = $\\frac{80}{1000} \\times 100\\% = \\mathbf{8\\%}$ है।<br><br><strong>उत्तर: (a) 8% profit</strong>"
        }
    },
    {
        "id": "PCT_PYQ77",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A fruit vendor sells 15 kg of apples for ₹$750$, thereby gaining the cost price of 5 kg of apples. What is his profit percentage?",
            "hi": "एक फल विक्रेता ₹$750$ में 15 किलोग्राम सेब बेचता है, जिससे उसे 5 किलोग्राम सेब के क्रय मूल्य का लाभ होता है। उसका लाभ प्रतिशत क्या है?"
        },
        "options": "(a) $28.65\\%$ &emsp; (b) $33.33\\%$ &emsp; (c) $26.32\\%$ &emsp; (d) $31.56\\%$",
        "solution": {
            "en": "Profit = Cost Price of 5 kg.<br>Number of items sold = 15 kg.<br>Profit percentage = $\\frac{5}{15} \\times 100\\% = \\mathbf{33.33\\%}$.<br><br><strong>Answer: (b) 33.33%</strong>",
            "hi": "लाभ = 5 किग्रा का क्रय मूल्य।<br>बेची गई वस्तु = 15 किग्रा।<br>लाभ प्रतिशत = $\\frac{5}{15} \\times 100\\% = \\mathbf{33.33\\%}$ है।<br><br><strong>उत्तर: (b) 33.33%</strong>"
        }
    },
    {
        "id": "PCT_PYQ78",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A bookseller sells 10 pens for ₹$300$, but incurs a loss equal to the cost price of 4 pens. Find the loss percentage.",
            "hi": "एक पुस्तक विक्रेता ₹$300$ में 10 पेन बेचता है, लेकिन उसे 4 पेनों के क्रय मूल्य के बराबर हानि होती है। हानि प्रतिशत ज्ञात कीजिए।"
        },
        "options": "(a) $40\\%$ &emsp; (b) $70\\%$ &emsp; (c) $60\\%$ &emsp; (d) $50\\%$",
        "solution": {
            "en": "Loss = CP of 4 pens.<br>Sells 10 pens $\\implies$ Total CP = CP of 10 pens.<br>Loss Percentage = $\\frac{4}{10} \\times 100\\% = \\mathbf{40\\%}$.<br><br><strong>Answer: (a) 40%</strong>",
            "hi": "हानि = 4 पेनों का CP।<br>10 पेन बेचता है $\implies$ कुल CP = 10 पेनों का CP।<br>हानि प्रतिशत = $\\frac{4}{10} \\times 100\\% = \\mathbf{40\\%}$ है।<br><br><strong>उत्तर: (a) 40%</strong>"
        }
    },
    {
        "id": "PCT_PYQ79",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "A dealer sells a packet of cookies at ₹$120$ after giving a $25\\%$ discount on the marked price. If the profit earned is $20\\%$, find the cost price of the packet.",
            "hi": "एक डीलर अंकित मूल्य पर $25\\%$ की छूट देने के बाद कुकीज़ का एक पैकेट ₹$120$ में बेचता है। यदि अर्जित लाभ $20\\%$ है, तो पैकेट का क्रय मूल्य ज्ञात कीजिए।"
        },
        "options": "(a) ₹$96$ &emsp; (b) ₹$90$ &emsp; (c) ₹$100$ &emsp; (d) ₹$80$",
        "solution": {
            "en": "Selling Price (SP) = $₹120$.<br>Profit = $20\\%$.<br>Cost Price (CP) = $\\frac{SP}{1 + \\text{Profit}\\%} = \\frac{120}{1.20} = \\mathbf{₹100}$.<br><br><strong>Answer: (c) ₹100</strong>",
            "hi": "विक्रय मूल्य (SP) = $₹120$।<br>लाभ = $20\\%$।<br>क्रय मूल्य (CP) = $\\frac{SP}{1 + \\text{लाभ}\\%} = \\frac{120}{1.20} = \\mathbf{₹100}$ है।<br><br><strong>उत्तर: (c) ₹100</strong>"
        }
    },
    {
        "id": "PCT_PYQ80",
        "badge": "CGL 2025 (Sep)",
        "question": {
            "en": "If the selling price of an item is increased by $25\\%$ and the profit also increases from $20\\%$ to $30\\%$, what is the percentage increase in the cost price?",
            "hi": "यदि किसी वस्तु के विक्रय मूल्य में $25\\%$ की वृद्धि की जाती है और लाभ भी $20\\%$ से बढ़कर $30\\%$ हो जाता है, तो क्रय मूल्य में प्रतिशत वृद्धि क्या है?"
        },
        "options": "(a) $45\\%$ &emsp; (b) $5.6\\%$ &emsp; (c) $10.28\\%$ &emsp; (d) $15.38\\%$",
        "solution": {
            "en": "$SP_1 = 1.20 CP_1$.<br>$SP_2 = 1.25 SP_1 = 1.25 \\times 1.20 CP_1 = 1.50 CP_1$.<br>Also, $SP_2 = 1.30 CP_2 \\implies 1.30 CP_2 = 1.50 CP_1 \\implies CP_2 = \\frac{1.50}{1.30} CP_1 \\approx 1.1538 CP_1$.<br>Increase in Cost Price = $15.38\\%$.<br><br><strong>Answer: (d) 15.38%</strong>",
            "hi": "$SP_1 = 1.20 CP_1$।<br>$SP_2 = 1.25 SP_1 = 1.25 \\times 1.20 CP_1 = 1.50 CP_1$।<br>साथ ही, $SP_2 = 1.30 CP_2 \\implies 1.30 CP_2 = 1.50 CP_1 \\implies CP_2 = \\frac{1.50}{1.30} CP_1 \\approx 1.1538 CP_1$।<br>क्रय मूल्य में वृद्धि = $15.38\\%$ है।<br><br><strong>उत्तर: (d) 15.38%</strong>"
        }
    }
]

file_path = "ssc-cgl/quantitative-aptitude/percentage/data/pyqs.json"

with open(file_path, "r", encoding="utf-8") as f:
    existing_pyqs = json.load(f)

# Append new ones
existing_pyqs.extend(new_pyqs)

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(existing_pyqs, f, ensure_ascii=False, indent=2)

print("SUCCESS: Appended", len(new_pyqs), "new PYQs. Total count:", len(existing_pyqs))
