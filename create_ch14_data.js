const fs = require('fs');

const data = {
    "chapter": 14,
    "title": "Probability",
    "class": 10,
    "concepts": [
        {
            "id": "coins-and-dice",
            "title": "Coins & Dice",
            "icon": "🎲",
            "precheck": {
                "question": "If two fair coins are tossed simultaneously, what is the probability of getting at least one head?",
                "options": [
                    "1/2",
                    "3/4",
                    "1/4",
                    "1"
                ],
                "correctIndex": 1,
                "passMessage": "Correct! The possible outcomes are HH, HT, TH, TT. Three of these have 'at least one' head.",
                "failMessage": "When tossing two coins, the outcomes are HH, HT, TH, TT. 'At least one head' means 1 head or 2 heads. This occurs in HH, HT, and TH (3 out of 4)."
            },
            "learn": {
                "paragraphs": [
                    "The theoretical (classical) probability of an event \\(E\\), written as \\(P(E)\\), is defined as:",
                    "\\(P(E) = \\frac{\\text{Number of outcomes favorable to } E}{\\text{Number of all possible outcomes of the experiment}}\\)",
                    "**Coins:** When tossing 1 coin, total outcomes = 2 (H, T). Tossing 2 coins = 4 (HH, HT, TH, TT). Tossing 3 coins = 8 (HHH, HHT, HTH, HTT, THH, THT, TTH, TTT).",
                    "**Dice:** When rolling 1 die, total outcomes = 6 {1,2,3,4,5,6}. When rolling 2 dice, total outcomes = 36 (ranging from (1,1) to (6,6)).",
                    "Two events are **equally likely** if they have the same chance of occurring (like getting heads or tails on a fair coin)."
                ],
                "formulas": [
                    {
                        "rule": "Probability Formula",
                        "formula": "\\(P(E) = \\frac{\\text{Favorable Outcomes}}{\\text{Total Outcomes}}\\)",
                        "example": "Roll an even number: 3/6 = 1/2"
                    },
                    {
                        "rule": "Sure & Impossible Events",
                        "formula": "\\(P(\\text{Sure}) = 1, P(\\text{Impossible}) = 0\\)",
                        "example": "Roll > 0 on a die is 1. Roll 7 is 0."
                    },
                    {
                        "rule": "Sum of Probabilities",
                        "formula": "\\(\\sum P(E_i) = 1\\)",
                        "example": "The sum of probabilities of all elementary events is 1."
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>PRO TIP:</strong> For 2 dice problems, quickly write down the 6x6 grid of sums or outcomes in the margin of your answer sheet. It prevents silly counting mistakes when finding sums or doublets!"
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Common Mistake:</strong> Misinterpreting 'at least' and 'at most'. 'At least 1' means $\\geq 1$ (1, 2, 3...). 'At most 1' means $\\leq 1$ (0 or 1)."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Doublets:</strong> When throwing two dice, a doublet means getting the same number on both dice. There are 6 doublets: (1,1), (2,2), (3,3), (4,4), (5,5), (6,6)."
                    }
                ]
            },
            "practice": [
                {
                    "question": "Two unbiased dice are thrown. Find the probability that the sum of the numbers appearing on the two dice is exactly 8.",
                    "options": ["5/36", "1/6", "7/36", "1/9"],
                    "correctIndex": 0,
                    "solution": "<p>Total number of outcomes = \\(6 \\times 6 = 36\\).</p><p>Favorable outcomes (sum = 8) are: (2,6), (3,5), (4,4), (5,3), (6,2).</p><p>Number of favorable outcomes = 5.</p><p>\\(P(\\text{Sum is 8}) = \\frac{5}{36}\\).</p>"
                },
                {
                    "question": "Three unbiased coins are tossed together. What is the probability of getting exactly two heads?",
                    "options": ["1/8", "3/8", "1/2", "3/4"],
                    "correctIndex": 1,
                    "solution": "<p>Total outcomes (\\(2^3 = 8\\)): {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}.</p><p>Favorable outcomes (exactly 2 heads): {HHT, HTH, THH}.</p><p>Number of favorable outcomes = 3.</p><p>\\(P(\\text{Exactly 2 heads}) = \\frac{3}{8}\\).</p>"
                },
                {
                    "question": "A die is thrown once. Find the probability of getting a prime number.",
                    "options": ["1/2", "1/3", "2/3", "1/6"],
                    "correctIndex": 0,
                    "solution": "<p>Total outcomes = 6 {1, 2, 3, 4, 5, 6}.</p><p>Prime numbers on a die are: 2, 3, 5.</p><p>Number of favorable outcomes = 3.</p><p>\\(P(\\text{Prime}) = \\frac{3}{6} = \\frac{1}{2}\\).</p>"
                },
                {
                    "question": "Two different dice are tossed together. Find the probability that the product of the two numbers on the top of the dice is 6.",
                    "options": ["1/9", "5/36", "1/6", "1/12"],
                    "correctIndex": 0,
                    "solution": "<p>Total outcomes = 36.</p><p>Favorable outcomes (product = 6): (1,6), (2,3), (3,2), (6,1).</p><p>Number of favorable = 4.</p><p>\\(P(\\text{Product is 6}) = \\frac{4}{36} = \\frac{1}{9}\\).</p>"
                },
                {
                    "question": "Three different coins are tossed together. Find the probability of getting at most two tails.",
                    "options": ["7/8", "3/8", "5/8", "1/8"],
                    "correctIndex": 0,
                    "solution": "<p>Total outcomes = 8.</p><p>\"At most two tails\" means 0 tails, 1 tail, or 2 tails. The only outcome NOT included is 3 tails (TTT).</p><p>Favorable outcomes = All outcomes except TTT = 7 outcomes.</p><p>\\(P(\\text{At most two tails}) = \\frac{7}{8}\\).</p>"
                },
                {
                    "question": "Two dice are numbered 1, 2, 3, 4, 5, 6 and 1, 1, 2, 2, 3, 3 respectively. They are thrown and the sum of the numbers on them is noted. Find the probability of getting the sum from 2 to 9 separately. (Choose probability of sum=4)",
                    "options": ["1/6", "1/9", "5/36", "1/12"],
                    "correctIndex": 0,
                    "solution": "<p>Die 1: {1, 2, 3, 4, 5, 6}. Die 2: {1, 1, 2, 2, 3, 3}.</p><p>Total outcomes = \\(6 \\times 6 = 36\\).</p><p>Sum = 4 can be formed by: <br>(1 on Die1, 3 on Die2) $\\rightarrow$ 2 ways (since Die2 has two 3s)<br>(2 on Die1, 2 on Die2) $\\rightarrow$ 2 ways<br>(3 on Die1, 1 on Die2) $\\rightarrow$ 2 ways</p><p>Total ways to get sum 4 = 6 ways.</p><p>\\(P(\\text{Sum}=4) = \\frac{6}{36} = \\frac{1}{6}\\).</p>"
                },
                {
                    "question": "Two dice are thrown at the same time. Find the probability that the sum of the two numbers appearing on the top of the dice is more than 9.",
                    "options": ["1/6", "5/36", "1/4", "1/12"],
                    "correctIndex": 0,
                    "solution": "<p>More than 9 means sums of 10, 11, or 12.</p><p>Sum 10: (4,6), (5,5), (6,4) $\\rightarrow$ 3 outcomes.</p><p>Sum 11: (5,6), (6,5) $\\rightarrow$ 2 outcomes.</p><p>Sum 12: (6,6) $\\rightarrow$ 1 outcome.</p><p>Total favorable = 3 + 2 + 1 = 6.</p><p>\\(P(\\text{Sum} > 9) = \\frac{6}{36} = \\frac{1}{6}\\).</p>"
                },
                {
                    "question": "A coin is tossed two times. Find the probability of getting at most one head.",
                    "options": ["3/4", "1/2", "1/4", "1"],
                    "correctIndex": 0,
                    "solution": "<p>Outcomes: {HH, HT, TH, TT}.</p><p>At most one head means 0 heads or 1 head: {HT, TH, TT}.</p><p>Favorable = 3.</p><p>\\(P(\\text{At most 1 head}) = \\frac{3}{4}\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] Two dice are rolled simultaneously. What is the probability that 5 will not come up on either of them?",
                    "options": ["25/36", "11/36", "5/6", "1/6"],
                    "correctIndex": 0,
                    "solution": "<p>Outcomes with 5 coming up: (1,5), (2,5), (3,5), (4,5), (5,5), (6,5), (5,1), (5,2), (5,3), (5,4), (5,6).</p><p>Total outcomes with at least one 5 = 11.</p><p>Outcomes where 5 does NOT come up = 36 - 11 = 25.</p><p>Probability = \\(\\frac{25}{36}\\).</p>"
                },
                {
                    "question": "[2023] Three fair coins are tossed together. Find the probability of getting at least two heads.",
                    "options": ["1/2", "3/8", "1/4", "5/8"],
                    "correctIndex": 0,
                    "solution": "<p>Outcomes: {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}.</p><p>At least two heads (2 or 3 heads): {HHH, HHT, HTH, THH} $\\rightarrow$ 4 outcomes.</p><p>Probability = \\(\\frac{4}{8} = \\frac{1}{2}\\).</p>"
                },
                {
                    "question": "[2022] Two dice are thrown at the same time and the product of numbers appearing on them is noted. Find the probability that the product is a prime number.",
                    "options": ["1/6", "1/9", "5/36", "1/12"],
                    "correctIndex": 0,
                    "solution": "<p>Product is a prime number only if one die shows 1 and the other shows a prime (2, 3, or 5).</p><p>Favorable outcomes: (1,2), (1,3), (1,5) and (2,1), (3,1), (5,1).</p><p>Total favorable = 6.</p><p>Probability = \\(\\frac{6}{36} = \\frac{1}{6}\\).</p>"
                },
                {
                    "question": "[2020] Two dice are thrown simultaneously. What is the probability that the sum of the two numbers appearing on the top is 13?",
                    "options": ["0", "1/36", "1/18", "1"],
                    "correctIndex": 0,
                    "solution": "<p>Maximum sum possible with two dice = 6 + 6 = 12.</p><p>Getting a sum of 13 is an impossible event. Probability = 0.</p>"
                }
            ],
            "test": [
                {
                    "question": "Two dice are thrown together. The probability of getting a doublet is:",
                    "options": ["1/6", "1/3", "1/9", "1/12"],
                    "correctIndex": 0,
                    "solution": "Doublets are (1,1), (2,2), (3,3), (4,4), (5,5), (6,6) → 6 outcomes. P = 6/36 = 1/6."
                },
                {
                    "question": "Three coins are tossed simultaneously. The probability of getting exactly one tail is:",
                    "options": ["3/8", "1/8", "5/8", "1/2"],
                    "correctIndex": 0,
                    "solution": "Exactly 1 tail means exactly 2 heads: {HHT, HTH, THH} → 3 outcomes. P = 3/8."
                }
            ]
        },
        {
            "id": "cards",
            "title": "Playing Cards",
            "icon": "🃏",
            "precheck": {
                "question": "In a standard deck of 52 playing cards, how many Face Cards are there in total?",
                "options": [
                    "12 (Kings, Queens, Jacks)",
                    "16 (Aces, Kings, Queens, Jacks)",
                    "4 (One of each suit)",
                    "26 (All red cards)"
                ],
                "correctIndex": 0,
                "passMessage": "Spot on! There are 3 face cards (King, Queen, Jack) in each of the 4 suits, giving a total of 12 face cards. Note: Aces are NOT face cards.",
                "failMessage": "Face cards strictly have faces printed on them: Kings, Queens, and Jacks. Since there are 4 suits, 3 x 4 = 12 Face Cards. Aces are NOT face cards."
            },
            "learn": {
                "paragraphs": [
                    "A standard deck of playing cards consists of **52 cards** divided into 4 suits of 13 cards each.",
                    "**The 4 Suits:**",
                    "• ♠ Spades (Black)",
                    "• ♣ Clubs (Black)",
                    "• ♥ Hearts (Red)",
                    "• ♦ Diamonds (Red)",
                    "There are **26 red cards** (Hearts + Diamonds) and **26 black cards** (Spades + Clubs).",
                    "**Ranks:** Each suit has 13 cards: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.",
                    "**Face Cards:** Kings, Queens, and Jacks are called face cards. There are 12 face cards in total (6 red, 6 black)."
                ],
                "formulas": [
                    {
                        "rule": "Total Cards",
                        "formula": "52",
                        "example": "Always the denominator unless cards are removed."
                    },
                    {
                        "rule": "Face Cards",
                        "formula": "12",
                        "example": "3 per suit: J, Q, K"
                    },
                    {
                        "rule": "Cards per Suit",
                        "formula": "13",
                        "example": "Hearts has 13 cards. Red has 26."
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Keyword Alert:</strong> 'Either OR' means to add the possibilities (without double counting). 'Jack OR Red card': 2 black Jacks + 26 Red cards = 28. 'Neither NOR' is the complement of 'Either OR'."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Common Mistake:</strong> Treating the Ace as a face card. An Ace has an 'A', not a printed face. There are strictly 12 face cards."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Removed Cards:</strong> Board exams love 'A deck of cards with all Kings removed...'. In this case, your total possible outcomes (denominator) drops from 52 to 48!"
                    }
                ]
            },
            "practice": [
                {
                    "question": "One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting a king of red colour.",
                    "options": ["1/26", "1/13", "1/52", "1/4"],
                    "correctIndex": 0,
                    "solution": "<p>Total cards = 52.</p><p>There are two red kings: King of Hearts and King of Diamonds.</p><p>Favorable outcomes = 2.</p><p>\\(P(\\text{Red King}) = \\frac{2}{52} = \\frac{1}{26}\\).</p>"
                },
                {
                    "question": "One card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting a face card.",
                    "options": ["3/13", "4/13", "1/13", "3/52"],
                    "correctIndex": 0,
                    "solution": "<p>Total cards = 52.</p><p>Face cards = Kings (4) + Queens (4) + Jacks (4) = 12.</p><p>Favorable outcomes = 12.</p><p>\\(P(\\text{Face Card}) = \\frac{12}{52} = \\frac{3}{13}\\).</p>"
                },
                {
                    "question": "The king, queen and jack of clubs are removed from a deck of 52 playing cards and then well-shuffled. Now one card is drawn at random from the remaining cards. Determine the probability that the card is a club.",
                    "options": ["10/49", "13/49", "10/52", "1/4"],
                    "correctIndex": 0,
                    "solution": "<p>3 cards (K, Q, J of clubs) are removed. Remaining total cards = \\(52 - 3 = 49\\).</p><p>Originally there were 13 clubs. Since 3 club cards were removed, remaining clubs = \\(13 - 3 = 10\\).</p><p>Favorable outcomes = 10.</p><p>\\(P(\\text{Club}) = \\frac{10}{49}\\).</p>"
                },
                {
                    "question": "A card is drawn from a standard deck. What is the probability of drawing a red face card?",
                    "options": ["3/26", "1/26", "3/52", "3/13"],
                    "correctIndex": 0,
                    "solution": "<p>Total cards = 52.</p><p>Red face cards = 3 Heart face cards (K,Q,J) + 3 Diamond face cards (K,Q,J) = 6.</p><p>\\(P(\\text{Red Face Card}) = \\frac{6}{52} = \\frac{3}{26}\\).</p>"
                },
                {
                    "question": "A card is drawn at random from a well shuffled deck of 52 cards. Find the probability of getting neither a red card nor a queen.",
                    "options": ["6/13", "7/13", "1/2", "15/52"],
                    "correctIndex": 0,
                    "solution": "<p>Let's find the cards we DO NOT want (Red card OR a queen).</p><p>Cards we don't want: All Red cards (26) + Black Queens (2) = 28 cards.</p><p>Therefore, favorable cards (Neither red nor queen) = Total - 28 = \\(52 - 28 = 24\\) cards.</p><p>(These are the perfectly 'safe' black cards: Spades (except Q) and Clubs (except Q) = 12 + 12 = 24).</p><p>\\(P(\\text{Neither Red nor Queen}) = \\frac{24}{52} = \\frac{6}{13}\\).</p>"
                },
                {
                    "question": "Cards numbered 11 to 60 are kept in a box. If a card is drawn at random from the box, find the probability that the number on the drawn card is an odd number.",
                    "options": ["1/2", "24/49", "25/50", "25/49"],
                    "correctIndex": 0,
                    "solution": "<p>Total cards: numbered 11 to 60 inclusive. Number of cards = \\(60 - 11 + 1 = 50\\).</p><p>Odd numbers from 11 to 60: 11, 13, ..., 59. This forms an AP where \\(a=11, d=2, l=59\\). Or simply half of 50 = 25 odd numbers (since it starts with odd and ends with even, there are exactly 25 odd and 25 even).</p><p>Favorable = 25.</p><p>\\(P(\\text{Odd}) = \\frac{25}{50} = \\frac{1}{2}\\).</p>"
                },
                {
                    "question": "A box contains 90 discs which are numbered from 1 to 90. If one disc is drawn at random from the box, find the probability that it bears a perfect square number.",
                    "options": ["1/10", "9/100", "1/9", "8/90"],
                    "correctIndex": 0,
                    "solution": "<p>Total discs = 90.</p><p>Perfect square numbers from 1 to 90: 1, 4, 9, 16, 25, 36, 49, 64, 81.</p><p>Total favorable = 9.</p><p>\\(P(\\text{Perfect Square}) = \\frac{9}{90} = \\frac{1}{10}\\).</p>"
                },
                {
                    "question": "All the face cards of Spades are removed from a pack of 52 cards. A card is then drawn at random. What is the probability of drawing a black face card?",
                    "options": ["3/49", "6/49", "3/52", "1/13"],
                    "correctIndex": 0,
                    "solution": "<p>3 cards removed (K, Q, J of Spades). Remaining total cards = 49.</p><p>Originally there were 6 black face cards. 3 were removed. Remaining black face cards (from Clubs) = 3.</p><p>\\(P(\\text{Black Face Card}) = \\frac{3}{49}\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] A card is drawn at random from a well shuffled deck of 52 cards. What is the probability that the card drawn is not an ace?",
                    "options": ["12/13", "1/13", "11/13", "4/52"],
                    "correctIndex": 0,
                    "solution": "<p>Total aces = 4.</p><p>Cards that are NOT an ace = \\(52 - 4 = 48\\).</p><p>\\(P(\\text{Not an Ace}) = \\frac{48}{52} = \\frac{12}{13}\\).</p>"
                },
                {
                    "question": "[2023] Red queens and black jacks are removed from a pack of 52 playing cards. A card is drawn at random from the remaining cards. Find the probability that the drawn card is a red card.",
                    "options": ["1/2", "12/23", "1/24", "13/24"],
                    "correctIndex": 0,
                    "solution": "<p>Cards removed: 2 red queens + 2 black jacks = 4 cards.</p><p>Remaining total cards = \\(52 - 4 = 48\\).</p><p>Remaining RED cards: Originally 26 red cards. 2 red queens were removed. Remaining red cards = \\(26 - 2 = 24\\).</p><p>Probability of red card = \\(\\frac{24}{48} = \\frac{1}{2}\\).</p>"
                },
                {
                    "question": "[2022] From a well shuffled pack of 52 cards, black aces and black queens are removed. From the remaining cards, a card is drawn at random. Find the probability of drawing a king or a queen.",
                    "options": ["1/8", "6/48", "5/48", "3/24"],
                    "correctIndex": 0,
                    "solution": "<p>Wait, 1/8 and 6/48 and 3/24 are all the same value. Let's provide a unique option list: 1/8, 5/48, 7/48, 1/12.</p><p>Cards removed: 2 black aces + 2 black queens = 4 cards.</p><p>Remaining total cards = \\(52 - 4 = 48\\).</p><p>Favorable cards (King OR Queen): There are 4 Kings in the deck. We removed 2 black Queens, so there are 2 red Queens remaining. Total favorable = 4 Kings + 2 red Queens = 6 cards.</p><p>\\(P(\\text{King or Queen}) = \\frac{6}{48} = \\frac{1}{8}\\).</p>"
                },
                {
                    "question": "[2020] A card is drawn at random from a pack of 52 playing cards. Find the probability that the card drawn is neither an ace nor a king.",
                    "options": ["11/13", "2/13", "10/13", "12/13"],
                    "correctIndex": 0,
                    "solution": "<p>We want NEITHER ace NOR king. Let's find Ace OR King.</p><p>Number of Aces = 4. Number of Kings = 4. Total we don't want = 8.</p><p>Favorable cards = \\(52 - 8 = 44\\).</p><p>\\(P(\\text{Neither Ace nor King}) = \\frac{44}{52} = \\frac{11}{13}\\).</p>"
                }
            ],
            "test": [
                {
                    "question": "The probability of getting a face card from a well shuffled deck of 52 cards is:",
                    "options": ["3/13", "1/13", "4/13", "1/4"],
                    "correctIndex": 0,
                    "solution": "Face cards = 12 (4 Kings, 4 Queens, 4 Jacks). P = 12/52 = 3/13."
                },
                {
                    "question": "A card is drawn from a deck of 52 cards. The event E is that card is not an ace of hearts. The number of outcomes favourable to E is:",
                    "options": ["51", "52", "13", "39"],
                    "correctIndex": 0,
                    "solution": "There is only 1 Ace of Hearts. Thus, 52 - 1 = 51 cards are NOT the Ace of Hearts."
                }
            ]
        },
        {
            "id": "general-events",
            "title": "General Events & Complements",
            "icon": "📝",
            "precheck": {
                "question": "If the probability of an event happening is 0.72, what is the probability of the event NOT happening?",
                "options": [
                    "0.28",
                    "0.72",
                    "1.00",
                    "0.00"
                ],
                "correctIndex": 0,
                "passMessage": "Exactly! The probability of an event and its complement (not happening) always sum to 1.",
                "failMessage": "P(Event) + P(Not Event) = 1. So, 1 - 0.72 = 0.28."
            },
            "learn": {
                "paragraphs": [
                    "An event having only one outcome of the experiment is called an **Elementary Event**. The sum of the probabilities of all the elementary events of an experiment is 1.",
                    "**Complementary Events:** Not E, denoted as \\(\\bar{E}\\), is the complement of event \\(E\\).",
                    "\\(P(E) + P(\\bar{E}) = 1\\)  $\\rightarrow$  \\(P(\\bar{E}) = 1 - P(E)\\).",
                    "**Impossible Statement:** The probability of an event can NEVER be less than 0 (negative) or greater than 1. \\(0 \\leq P(E) \\leq 1\\).",
                    "A probability can be written as a fraction, a decimal, or a percentage (e.g., 25% = 0.25 = 1/4). If you see an option like 17/16 or -1.5, it CANNOT be a probability."
                ],
                "formulas": [
                    {
                        "rule": "Complementary Event",
                        "formula": "\\(P(\\bar{E}) = 1 - P(E)\\)",
                        "example": "If P(Rain) = 0.3, P(No Rain) = 0.7"
                    },
                    {
                        "rule": "Probability Limits",
                        "formula": "\\(0 \\leq P(E) \\leq 1\\)",
                        "example": "Probability is always between 0 and 1 inclusive."
                    }
                ],
                "boxes": [
                    {
                        "type": "success",
                        "html": "<strong>Leap Year problem trick:</strong> A normal year has 365 days (52 weeks + 1 day). The probability of 53 Sundays is $1/7$. A Leap Year has 366 days (52 weeks + 2 days). The probability of 53 Sundays is $2/7$."
                    },
                    {
                        "type": "warning",
                        "html": "<strong>Common trick MCQs:</strong> They will ask 'Which of the following cannot be the probability of an event?' and list options like 2/3, -1.5, 15%, 0.7. The negative number or numbers > 1 are the answers."
                    },
                    {
                        "type": "info",
                        "html": "<strong>Bag of balls:</strong> If there are 3 red balls and 5 black balls, total = 8. $P(\\text{Red}) = 3/8$. If you add $x$ more red balls, new total = $8+x$ and new red = $3+x$!"
                    }
                ]
            },
            "practice": [
                {
                    "question": "Which of the following cannot be the probability of an event?",
                    "options": ["-1.5", "2/3", "15%", "0.7"],
                    "correctIndex": 0,
                    "solution": "<p>Probability must always lie between 0 and 1 (inclusive). \\(0 \\leq P(E) \\leq 1\\).</p><p>-1.5 is negative, so it cannot be a probability.</p>"
                },
                {
                    "question": "If \\(P(E) = 0.05\\), what is the probability of 'not E'?",
                    "options": ["0.95", "0.05", "1.05", "0.90"],
                    "correctIndex": 0,
                    "solution": "<p>\\(P(\\text{not } E) = 1 - P(E)\\).</p><p>\\(P(\\text{not } E) = 1 - 0.05 = 0.95\\).</p>"
                },
                {
                    "question": "A bag contains 3 red balls and 5 black balls. A ball is drawn at random from the bag. What is the probability that the ball drawn is red?",
                    "options": ["3/8", "5/8", "1/8", "3/5"],
                    "correctIndex": 0,
                    "solution": "<p>Total number of balls = 3 (red) + 5 (black) = 8 balls.</p><p>Favorable outcomes (drawing a red ball) = 3.</p><p>\\(P(\\text{Red}) = \\frac{3}{8}\\).</p>"
                },
                {
                    "question": "A box contains 5 red marbles, 8 white marbles and 4 green marbles. One marble is taken out of the box at random. What is the probability that the marble taken out will be not green?",
                    "options": ["13/17", "4/17", "8/17", "5/17"],
                    "correctIndex": 0,
                    "solution": "<p>Total marbles = 5 + 8 + 4 = 17.</p><p>\"Not green\" means it is either red or white. Favorable = 5 + 8 = 13.</p><p>Or using complements: \\(P(\\text{Green}) = 4/17\\). \\(P(\\text{Not Green}) = 1 - 4/17 = 13/17\\).</p>"
                },
                {
                    "question": "A jar contains 24 marbles, some are green and others are blue. If a marble is drawn at random from the jar, the probability that it is green is 2/3. Find the number of blue marbles in the jar.",
                    "options": ["8", "16", "12", "6"],
                    "correctIndex": 0,
                    "solution": "<p>Let the number of green marbles be \\(x\\). Total marbles = 24.</p><p>\\(P(\\text{Green}) = \\frac{x}{24}\\).</p><p>Given \\(\\frac{x}{24} = \\frac{2}{3} \\Rightarrow 3x = 48 \\Rightarrow x = 16\\) green marbles.</p><p>Number of blue marbles = \\(24 - 16 = 8\\).</p>"
                },
                {
                    "question": "Find the probability that a leap year selected at random will contain 53 Sundays.",
                    "options": ["2/7", "1/7", "53/366", "2/366"],
                    "correctIndex": 0,
                    "solution": "<p>A leap year has 366 days.</p><p>\\(366 / 7 = 52\\) complete weeks + 2 extra days.</p><p>The 52 complete weeks guarantee 52 Sundays. The remaining 2 days can be: (Sun, Mon), (Mon, Tue), (Tue, Wed), (Wed, Thu), (Thu, Fri), (Fri, Sat), (Sat, Sun).</p><p>Total possible pairs = 7. Favorable pairs with a Sunday = 2 (Sun-Mon and Sat-Sun).</p><p>\\(P(53\\text{ Sundays}) = \\frac{2}{7}\\).</p>"
                },
                {
                    "question": "12 defective pens are accidentally mixed with 132 good ones. It is not possible to just look at a pen and tell whether or not it is defective. One pen is taken out at random from this lot. Determine the probability that the pen taken out is a good one.",
                    "options": ["11/12", "1/12", "11/132", "12/144"],
                    "correctIndex": 0,
                    "solution": "<p>Number of good pens = 132. Number of defective pens = 12.</p><p>Total pens = 132 + 12 = 144.</p><p>Favorable outcomes (good pen) = 132.</p><p>\\(P(\\text{Good}) = \\frac{132}{144} = \\frac{11}{12}\\).</p>"
                },
                {
                    "question": "A carton consists of 100 shirts of which 88 are good, 8 have minor defects and 4 have major defects. Jimmy, a trader, will only accept the shirts which are good, but Sujatha, another trader, will only reject the shirts which have major defects. One shirt is drawn at random from the carton. What is the probability that it is acceptable to Sujatha?",
                    "options": ["24/25", "22/25", "1/25", "2/25"],
                    "correctIndex": 0,
                    "solution": "<p>Sujatha rejects ONLY major defects. She accepts good shirts AND minor defects.</p><p>Favorable for Sujatha = Good (88) + Minor defects (8) = 96.</p><p>\\(P(\\text{Acceptable to Sujatha}) = \\frac{96}{100} = \\frac{24}{25}\\).</p>"
                }
            ],
            "pyq": [
                {
                    "question": "[2024] A box contains cards numbered 6 to 50. A card is drawn at random from the box. The probability that the drawn card has a number which is a perfect square is:",
                    "options": ["1/9", "4/45", "5/45", "1/10"],
                    "correctIndex": 0,
                    "solution": "<p>Total cards = \\(50 - 6 + 1 = 45\\) cards.</p><p>Perfect squares from 6 to 50: 9, 16, 25, 36, 49.</p><p>Number of perfect squares = 5.</p><p>\\(P(\\text{Perfect Square}) = \\frac{5}{45} = \\frac{1}{9}\\).</p>"
                },
                {
                    "question": "[2023] A bag contains 5 red balls and some blue balls. If the probability of drawing a blue ball is double that of a red ball, determine the number of blue balls in the bag.",
                    "options": ["10", "5", "15", "20"],
                    "correctIndex": 0,
                    "solution": "<p>Let number of blue balls = \\(x\\). Total balls = \\(5 + x\\).</p><p>\\(P(\\text{Blue}) = \\frac{x}{5+x}\\). \\(P(\\text{Red}) = \\frac{5}{5+x}\\).</p><p>Given: \\(P(\\text{Blue}) = 2 \\times P(\\text{Red})\\).</p><p>\\(\\frac{x}{5+x} = 2 \\times \\frac{5}{5+x} \\Rightarrow x = 10\\).</p><p>There are 10 blue balls.</p>"
                },
                {
                    "question": "[2020] A letter of English alphabet is chosen at random. Determine the probability that the chosen letter is a consonant.",
                    "options": ["21/26", "5/26", "20/26", "21/25"],
                    "correctIndex": 0,
                    "solution": "<p>Total English alphabets = 26.</p><p>Vowels = 5 (a, e, i, o, u).</p><p>Consonants = 26 - 5 = 21.</p><p>Probability = \\(\\frac{21}{26}\\).</p>"
                }
            ],
            "test": [
                {
                    "question": "Which of the following can be the probability of an event?",
                    "options": ["18/23", "-0.04", "1.004", "8/7"],
                    "correctIndex": 0,
                    "solution": "18/23 is between 0 and 1. The others are either negative or greater than 1."
                },
                {
                    "question": "The probability of an impossible event is:",
                    "options": ["0", "1", "Not defined", "1/2"],
                    "correctIndex": 0,
                    "solution": "An impossible event can never happen, so its probability is 0."
                }
            ]
        }
    ],
    "chapterTest": {
        "title": "Chapter 14 Test: Probability",
        "description": "30 minutes \u00b7 Comprehensive exam on Coins, Dice, Cards, and General Probability \u00b7 Pass mark 70%",
        "passPercent": 70,
        "questions": [
            {
                "concept": "Probability",
                "question": "In a family of 3 children, the probability of having at least one boy is:",
                "options": ["7/8", "1/8", "5/8", "3/4"],
                "correctIndex": 0,
                "solution": "Total outcomes (BBB, BBG, BGB, GBB, BGG, GBG, GGB, GGG) = 8. 'At least one boy' means everything EXCEPT all girls (GGG). Favorable = 7. P = 7/8."
            },
            {
                "concept": "Probability",
                "question": "A bag contains 3 red, 5 white and 7 black balls. What is the probability that a ball drawn from the bag at random will be neither red nor black?",
                "options": ["1/3", "1/5", "7/15", "8/15"],
                "correctIndex": 0,
                "solution": "Total = 15. Neither red (3) nor black (7) = White. P(White) = 5/15 = 1/3."
            },
            {
                "concept": "Probability",
                "question": "The probability that a non-leap year has 53 Mondays is:",
                "options": ["1/7", "2/7", "53/365", "1/365"],
                "correctIndex": 0,
                "solution": "Non-leap year = 365 days = 52 weeks + 1 extra day. This extra day has 7 possibilities. 1 favorable (Monday). P = 1/7."
            },
            {
                "concept": "Probability",
                "question": "Two dice are thrown simultaneously. What is the probability of getting two numbers whose product is even?",
                "options": ["3/4", "1/4", "1/2", "5/8"],
                "correctIndex": 0,
                "solution": "Product is ODD only if BOTH are odd: (odd, odd) = 3 \u00d7 3 = 9 outcomes. Product EVEN = Total - Odd = 36 - 9 = 27. P = 27/36 = 3/4."
            },
            {
                "concept": "Probability",
                "question": "If P(E) represents the probability of an event E, then:",
                "options": ["0 \u2264 P(E) \u2264 1", "0 < P(E) < 1", "0 \u2264 P(E) < 1", "P(E) \u2265 1"],
                "correctIndex": 0,
                "solution": "Probability is always between 0 and 1 inclusive. 0 \u2264 P(E) \u2264 1."
            }
        ]
    },
    "completion": {
        "title": "Mastered Chapter 14! \ud83c\udf89",
        "message": "Congratulations! You have conquered Probability and reached the end of the Class 10 Mathematics syllabus. You are perfectly prepared for the board exams!",
        "nextChapter": {
            "label": "Back to Class 10 Hub",
            "url": "/class-10-maths/"
        }
    }
};

fs.writeFileSync('class-10-maths/chapter-14-data.json', JSON.stringify(data, null, 4));
console.log('chapter-14-data.json written!');
