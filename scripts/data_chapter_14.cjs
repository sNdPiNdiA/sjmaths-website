// Data for Chapter 14: Probability
module.exports = {
  chapterNum: 14,
  chapterName: "Probability",
  chapterSlug: "chapter-14-probability",
  exercises: [
    {
      exNum: 1,
      title: "Objective Type Questions (MCQs)",
      sectionLetter: "Q",
      prevUrl: "/class-11-maths/ncert-exemplar-practice/chapter-13-statistics/exemplar-13-3.html",
      prevText: "← Chapter 13",
      nextUrl: "exemplar-14-2.html",
      nextText: "Exercise 14.2 →",
      questions: [
        {
          id: "exemplar-11-ch14-1",
          type: "mcq",
          question: "If $P(A) = 0.4$, $P(B) = 0.8$ and $P(B|A) = 0.6$, then $P(A \\cup B)$ is",
          options: [
            "(a) $0.24$",
            "(b) $0.96$",
            "(c) $0.84$",
            "(d) $0.48$"
          ],
          solutionSteps: [
            "By definition of conditional probability: $P(B|A) = \\frac{P(A \\cap B)}{P(A)}$.",
            "Therefore, $P(A \\cap B) = P(A) \\cdot P(B|A) = 0.4 \\times 0.6 = 0.24$.",
            "Using the addition rule of probability: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.",
            "$P(A \\cup B) = 0.4 + 0.8 - 0.24 = 1.20 - 0.24 = 0.96$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch14-2",
          type: "mcq",
          question: "If $A$ and $B$ are mutually exclusive events, then $P(A \\cap B)$ is equal to",
          options: [
            "(a) $1$",
            "(b) $P(A)P(B)$",
            "(c) $0$",
            "(d) $P(A) + P(B)$"
          ],
          solutionSteps: [
            "Two events $A$ and $B$ are mutually exclusive if they cannot occur simultaneously.",
            "That is, their intersection is the empty set: $A \\cap B = \\phi$.",
            "By axiomatic definition of probability, $P(\\phi) = 0$.",
            "Hence, $P(A \\cap B) = 0$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch14-3",
          type: "mcq",
          question: "If $P(A) = \\frac{3}{5}$ and $P(B) = \\frac{1}{5}$, and $A$ and $B$ are mutually exclusive events, then $P(A \\text{ or } B)$ is",
          options: [
            "(a) $\\frac{4}{5}$",
            "(b) $\\frac{2}{5}$",
            "(c) $\\frac{3}{25}$",
            "(d) $\\frac{1}{5}$"
          ],
          solutionSteps: [
            "Since $A$ and $B$ are mutually exclusive, $P(A \\cap B) = 0$.",
            "$P(A \\text{ or } B) = P(A \\cup B) = P(A) + P(B)$.",
            "$P(A \\cup B) = \\frac{3}{5} + \\frac{1}{5} = \\frac{4}{5}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-4",
          type: "mcq",
          question: "Two dice are thrown simultaneously. The probability of getting a doublet of even numbers is",
          options: [
            "(a) $\\frac{1}{6}$",
            "(b) $\\frac{1}{12}$",
            "(c) $\\frac{1}{36}$",
            "(d) $\\frac{5}{36}$"
          ],
          solutionSteps: [
            "When two dice are thrown, the total number of outcomes is $n(S) = 6 \\times 6 = 36$.",
            "Even doublets are: $(2, 2), (4, 4), (6, 6)$.",
            "Number of favourable outcomes $n(E) = 3$.",
            "Probability $P(E) = \\frac{n(E)}{n(S)} = \\frac{3}{36} = \\frac{1}{12}$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch14-5",
          type: "mcq",
          question: "If an event cannot occur, then its probability is",
          options: [
            "(a) $1$",
            "(b) $\\frac{3}{4}$",
            "(c) $\\frac{1}{2}$",
            "(d) $0$"
          ],
          solutionSteps: [
            "An event that is impossible or cannot occur corresponds to the null set $\\phi$.",
            "By axioms of probability, the probability of an impossible event is zero: $P(\\phi) = 0$."
          ],
          answer: "(d)"
        },
        {
          id: "exemplar-11-ch14-6",
          type: "mcq",
          question: "If $P(A) = 0.5$, $P(B) = 0.3$, and $A$ and $B$ are mutually exclusive, then $P(\\text{neither } A \\text{ nor } B)$ is",
          options: [
            "(a) $0.8$",
            "(b) $0.2$",
            "(c) $0.15$",
            "(d) $0.5$"
          ],
          solutionSteps: [
            "Since $A$ and $B$ are mutually exclusive, $P(A \\cup B) = P(A) + P(B) = 0.5 + 0.3 = 0.8$.",
            "The event 'neither $A$ nor $B$' is $(A \\cup B)' = A' \\cap B'$.",
            "$P((A \\cup B)') = 1 - P(A \\cup B) = 1 - 0.8 = 0.2$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch14-7",
          type: "mcq",
          question: "A card is drawn from a well-shuffled pack of $52$ playing cards. The probability that it is a spade or an ace is",
          options: [
            "(a) $\\frac{4}{13}$",
            "(b) $\\frac{17}{52}$",
            "(c) $\\frac{1}{13}$",
            "(d) $\\frac{16}{52}$"
          ],
          solutionSteps: [
            "Total number of cards $n(S) = 52$.",
            "Number of spades $n(\\text{Spade}) = 13$.",
            "Number of aces $n(\\text{Ace}) = 4$.",
            "Intersection $n(\\text{Spade} \\cap \\text{Ace}) = 1$ (ace of spades).",
            "$n(\\text{Spade} \\cup \\text{Ace}) = 13 + 4 - 1 = 16$.",
            "Probability $= \\frac{16}{52} = \\frac{4}{13}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-8",
          type: "mcq",
          question: "Three coins are tossed once. The probability of getting at least two heads is",
          options: [
            "(a) $\\frac{1}{8}$",
            "(b) $\\frac{3}{8}$",
            "(c) $\\frac{1}{2}$",
            "(d) $\\frac{5}{8}$"
          ],
          solutionSteps: [
            "Sample space $S = \\{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\\}$. Total $n(S) = 8$.",
            "Event 'at least two heads' means $2$ heads or $3$ heads.",
            "Favourable outcomes $E = \\{HHT, HTH, THH, HHH\\}$, so $n(E) = 4$.",
            "Probability $P(E) = \\frac{4}{8} = \\frac{1}{2}$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch14-9",
          type: "mcq",
          question: "If $A$ and $B$ are two events such that $P(A) = \\frac{1}{4}$, $P(B) = \\frac{1}{2}$ and $P(A \\cap B) = \\frac{1}{8}$, then $P(\\text{not } A \\text{ and not } B)$ is",
          options: [
            "(a) $\\frac{3}{8}$",
            "(b) $\\frac{5}{8}$",
            "(c) $\\frac{1}{8}$",
            "(d) $\\frac{7}{8}$"
          ],
          solutionSteps: [
            "First find $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = \\frac{1}{4} + \\frac{1}{2} - \\frac{1}{8} = \\frac{2 + 4 - 1}{8} = \\frac{5}{8}$.",
            "By De Morgan's Law, $(\\text{not } A \\text{ and not } B) = A' \\cap B' = (A \\cup B)'$.",
            "$P(A' \\cap B') = 1 - P(A \\cup B) = 1 - \\frac{5}{8} = \\frac{3}{8}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-10",
          type: "mcq",
          question: "The odds in favour of an event are $3 : 5$. The probability of occurrence of the event is",
          options: [
            "(a) $\\frac{3}{5}$",
            "(b) $\\frac{5}{3}$",
            "(c) $\\frac{3}{8}$",
            "(d) $\\frac{5}{8}$"
          ],
          solutionSteps: [
            "If odds in favour of an event $E$ are $a : b$, then the probability of occurrence is $P(E) = \\frac{a}{a + b}$.",
            "Here $a = 3$ and $b = 5$.",
            "$P(E) = \\frac{3}{3 + 5} = \\frac{3}{8}$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch14-11",
          type: "mcq",
          question: "A letter is chosen at random from the word 'ASSASSINATION'. The probability that the letter is a vowel is",
          options: [
            "(a) $\\frac{6}{13}$",
            "(b) $\\frac{7}{13}$",
            "(c) $\\frac{5}{13}$",
            "(d) $\\frac{4}{13}$"
          ],
          solutionSteps: [
            "Total number of letters in 'ASSASSINATION' = $13$.",
            "Vowels present: $A, A, A, I, I, O$.",
            "Number of vowels $n(E) = 3 + 2 + 1 = 6$.",
            "Probability $= \\frac{n(E)}{n(S)} = \\frac{6}{13}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-12",
          type: "mcq",
          question: "If $E$ and $F$ are events such that $P(E) \\le P(F)$ and $P(E \\cap F) > 0$, then which of the following is always true?",
          options: [
            "(a) $E \\subset F$",
            "(b) Occurrence of $E \\implies$ occurrence of $F$",
            "(c) $P(E \\cap F) \\le P(E)$",
            "(d) none of these"
          ],
          solutionSteps: [
            "Since $E \\cap F \\subseteq E$, the probability of a subset cannot exceed the probability of the set.",
            "Hence, $P(E \\cap F) \\le P(E)$ is an axiomatic truth for any arbitrary events $E$ and $F$.",
            "Option (a) and (b) are not necessarily true in general."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch14-13",
          type: "mcq",
          question: "If $P(A \\cup B) = P(A \\cap B)$ for two events $A$ and $B$, then",
          options: [
            "(a) $P(A) = P(B)$",
            "(b) $P(A) + P(B) = 1$",
            "(c) $P(A) = 0$",
            "(d) none of these"
          ],
          solutionSteps: [
            "Recall $P(A \\cup B) - P(A \\cap B) = P(A \\cap B') + P(A' \\cap B)$.",
            "If $P(A \\cup B) = P(A \\cap B)$, then $P(A \\cap B') + P(A' \\cap B) = 0$.",
            "Since probabilities are non-negative, $P(A \\cap B') = 0$ and $P(A' \\cap B) = 0$.",
            "This implies $P(A) = P(A \\cap B) + P(A \\cap B') = P(A \\cap B)$, and similarly $P(B) = P(A \\cap B)$.",
            "Therefore, $P(A) = P(B)$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-14",
          type: "mcq",
          question: "In a non-leap year, the probability of having $53$ Sundays is",
          options: [
            "(a) $\\frac{1}{7}$",
            "(b) $\\frac{2}{7}$",
            "(c) $\\frac{5}{7}$",
            "(d) $\\frac{3}{7}$"
          ],
          solutionSteps: [
            "A non-leap year contains $365$ days.",
            "$365 = 52 \\text{ weeks} + 1 \\text{ day}$.",
            "The $52$ complete weeks contribute exactly $52$ Sundays.",
            "The remaining $1$ day can be any one of: $\\{\\text{Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}\\}$.",
            "There are $7$ equally likely possibilities, of which $1$ is a Sunday.",
            "Probability of $53$ Sundays $= \\frac{1}{7}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch14-15",
          type: "mcq",
          question: "If $A$ and $B$ are two mutually exclusive and exhaustive events, and $P(A) = 2P(B)$, then $P(A)$ is equal to",
          options: [
            "(a) $\\frac{1}{3}$",
            "(b) $\\frac{2}{3}$",
            "(c) $\\frac{1}{2}$",
            "(d) $\\frac{3}{4}$"
          ],
          solutionSteps: [
            "Since $A$ and $B$ are mutually exclusive and exhaustive, $P(A \\cup B) = P(A) + P(B) = 1$.",
            "Given $P(A) = 2P(B)$. Substitute $P(A)$:",
            "$2P(B) + P(B) = 1 \\implies 3P(B) = 1 \\implies P(B) = \\frac{1}{3}$.",
            "Then $P(A) = 2 \\times \\frac{1}{3} = \\frac{2}{3}$."
          ],
          answer: "(b)"
        }
      ]
    },
    {
      exNum: 2,
      title: "Short Answer Type Questions",
      sectionLetter: "S",
      prevUrl: "exemplar-14-1.html",
      prevText: "← Exercise 14.1",
      nextUrl: "exemplar-14-3.html",
      nextText: "Exercise 14.3 →",
      questions: [
        {
          id: "exemplar-11-ch14-sa-1",
          type: "subjective",
          question: "A fair die is rolled. Describe the following events: (i) $A$: getting a prime number, (ii) $B$: getting a number greater than $3$, (iii) $A \\cap B$, (iv) $A \\cup B$. Find their respective probabilities.",
          solutionSteps: [
            "Sample space $S = \\{1, 2, 3, 4, 5, 6\\}$, $n(S) = 6$.",
            "(i) Prime numbers: $A = \\{2, 3, 5\\} \\implies P(A) = \\frac{3}{6} = \\frac{1}{2}$.",
            "(ii) Numbers greater than $3$: $B = \\{4, 5, 6\\} \\implies P(B) = \\frac{3}{6} = \\frac{1}{2}$.",
            "(iii) Intersection: $A \\cap B = \\{5\\} \\implies P(A \\cap B) = \\frac{1}{6}$.",
            "(iv) Union: $A \\cup B = \\{2, 3, 4, 5, 6\\} \\implies P(A \\cup B) = \\frac{5}{6}$."
          ],
          answer: "$P(A) = \\frac{1}{2}, P(B) = \\frac{1}{2}, P(A \\cap B) = \\frac{1}{6}, P(A \\cup B) = \\frac{5}{6}$"
        },
        {
          id: "exemplar-11-ch14-sa-2",
          type: "subjective",
          question: "A coin is tossed twice. If the second throw results in a tail, a die is thrown. Write the sample space of this experiment.",
          solutionSteps: [
            "Outcomes of tossing a coin twice are: $HH, HT, TH, TT$.",
            "If the second throw is a Head ($HH, TH$), no further step is taken.",
            "If the second throw is a Tail ($HT, TT$), a standard die ($1$ to $6$) is rolled.",
            "For $HT$: $\\{HT1, HT2, HT3, HT4, HT5, HT6\\}$.",
            "For $TT$: $\\{TT1, TT2, TT3, TT4, TT5, TT6\\}$.",
            "Sample Space $S = \\{HH, TH, HT1, HT2, HT3, HT4, HT5, HT6, TT1, TT2, TT3, TT4, TT5, TT6\\}$ (Total $14$ sample points)."
          ],
          answer: "$S = \\{HH, TH, HT1, HT2, HT3, HT4, HT5, HT6, TT1, TT2, TT3, TT4, TT5, TT6\\}$"
        },
        {
          id: "exemplar-11-ch14-sa-3",
          type: "subjective",
          question: "If $P(A) = \\frac{2}{11}$, $P(B) = \\frac{5}{11}$ and $P(A \\cup B) = \\frac{6}{11}$, find: (i) $P(A \\cap B)$, (ii) $P(A \\cap B')$, (iii) $P(A' \\cap B')$.",
          solutionSteps: [
            "(i) Using addition theorem: $P(A \\cup B) = P(A) + P(B) - P(A \\cap B)$.",
            "$\\frac{6}{11} = \\frac{2}{11} + \\frac{5}{11} - P(A \\cap B) \\implies P(A \\cap B) = \\frac{7}{11} - \\frac{6}{11} = \\frac{1}{11}$.",
            "(ii) $P(A \\cap B') = P(A) - P(A \\cap B) = \\frac{2}{11} - \\frac{1}{11} = \\frac{1}{11}$.",
            "(iii) By De Morgan's Law: $P(A' \\cap B') = P((A \\cup B)') = 1 - P(A \\cup B) = 1 - \\frac{6}{11} = \\frac{5}{11}$."
          ],
          answer: "(i) $\\frac{1}{11}$, (ii) $\\frac{1}{11}$, (iii) $\\frac{5}{11}$"
        },
        {
          id: "exemplar-11-ch14-sa-4",
          type: "subjective",
          question: "Two dice are thrown. Find the probability of getting a total score of at least $10$.",
          solutionSteps: [
            "Total possible outcomes $n(S) = 6 \\times 6 = 36$.",
            "Score of at least $10$ means a sum of $10, 11,$ or $12$.",
            "Sum = $10$: $(4, 6), (5, 5), (6, 4)$ (3 outcomes).",
            "Sum = $11$: $(5, 6), (6, 5)$ (2 outcomes).",
            "Sum = $12$: $(6, 6)$ (1 outcome).",
            "Total favourable outcomes $n(E) = 3 + 2 + 1 = 6$.",
            "Probability $P(E) = \\frac{6}{36} = \\frac{1}{6}$."
          ],
          answer: "$\\frac{1}{6}$"
        },
        {
          id: "exemplar-11-ch14-sa-5",
          type: "subjective",
          question: "Four cards are drawn at random from a well-shuffled pack of $52$ cards. What is the probability of getting $3$ diamonds and one spade?",
          solutionSteps: [
            "Total ways to draw $4$ cards from $52$ is $n(S) = {}^{52}C_4$.",
            "There are $13$ diamonds and $13$ spades in the deck.",
            "Ways to select $3$ diamonds from $13$: ${}^{13}C_3 = \\frac{13 \\times 12 \\times 11}{6} = 286$.",
            "Ways to select $1$ spade from $13$: ${}^{13}C_1 = 13$.",
            "Total favourable ways $n(E) = {}^{13}C_3 \\times {}^{13}C_1 = 286 \\times 13 = 3718$.",
            "${}^{52}C_4 = \\frac{52 \\times 51 \\times 50 \\times 49}{24} = 270,725$.",
            "Probability $= \\frac{3718}{270725} \\approx 0.0137$."
          ],
          answer: "$\\frac{{}^{13}C_3 \\times {}^{13}C_1}{{}^{52}C_4} = \\frac{2860}{270725} = \\frac{3718}{270725}$"
        },
        {
          id: "exemplar-11-ch14-sa-6",
          type: "subjective",
          question: "A box contains $10$ red, $20$ blue, and $30$ green marbles. Five marbles are drawn from the box. What is the probability that: (i) all will be blue? (ii) at least one will be green?",
          solutionSteps: [
            "Total number of marbles $= 10 + 20 + 30 = 60$. Total ways to choose $5$: ${}^{60}C_5$.",
            "(i) Probability that all $5$ marbles are blue:",
            "$P(\\text{all blue}) = \\frac{{}^{20}C_5}{{}^{60}C_5} = \\frac{15504}{5461512} = \\frac{34}{11977}$.",
            "(ii) Probability that none of the $5$ marbles are green:",
            "Number of non-green marbles $= 60 - 30 = 30$.",
            "$P(\\text{no green}) = \\frac{{}^{30}C_5}{{}^{60}C_5}$.",
            "Probability of at least one green $= 1 - P(\\text{no green}) = 1 - \\frac{{}^{30}C_5}{{}^{60}C_5}$."
          ],
          answer: "(i) $\\frac{{}^{20}C_5}{{}^{60}C_5}$, (ii) $1 - \\frac{{}^{30}C_5}{{}^{60}C_5}$"
        },
        {
          id: "exemplar-11-ch14-sa-7",
          type: "subjective",
          question: "If $A, B, C$ are three mutually exclusive and exhaustive events associated with an experiment, find $P(A)$ given that $P(B) = \\frac{3}{2}P(A)$ and $P(C) = \\frac{1}{2}P(B)$.",
          solutionSteps: [
            "Since $A, B, C$ are mutually exclusive and exhaustive, $P(A) + P(B) + P(C) = 1$.",
            "Let $P(A) = p$.",
            "Then $P(B) = \\frac{3}{2}p$.",
            "And $P(C) = \\frac{1}{2}P(B) = \\frac{1}{2}\\left(\\frac{3}{2}p\\right) = \\frac{3}{4}p$.",
            "Substitute into the sum: $p + \\frac{3}{2}p + \\frac{3}{4}p = 1$.",
            "$\\frac{4p + 6p + 3p}{4} = 1 \\implies \\frac{13p}{4} = 1 \\implies p = \\frac{4}{13}$.",
            "Therefore, $P(A) = \\frac{4}{13}$."
          ],
          answer: "$P(A) = \\frac{4}{13}$"
        },
        {
          id: "exemplar-11-ch14-sa-8",
          type: "subjective",
          question: "In a class of $60$ students, $30$ opted for NCC, $32$ opted for NSS and $24$ opted for both. If one student is selected at random, find the probability that: (i) The student opted for NCC or NSS, (ii) The student opted for neither NCC nor NSS.",
          solutionSteps: [
            "Total students $n(S) = 60$.",
            "$P(\\text{NCC}) = \\frac{30}{60}$, $P(\\text{NSS}) = \\frac{32}{60}$, $P(\\text{NCC} \\cap \\text{NSS}) = \\frac{24}{60}$.",
            "(i) $P(\\text{NCC} \\cup \\text{NSS}) = P(\\text{NCC}) + P(\\text{NSS}) - P(\\text{NCC} \\cap \\text{NSS}) = \\frac{30 + 32 - 24}{60} = \\frac{38}{60} = \\frac{19}{30}$.",
            "(ii) $P(\\text{neither NCC nor NSS}) = 1 - P(\\text{NCC} \\cup \\text{NSS}) = 1 - \\frac{19}{30} = \\frac{11}{30}$."
          ],
          answer: "(i) $\\frac{19}{30}$, (ii) $\\frac{11}{30}$"
        },
        {
          id: "exemplar-11-ch14-sa-9",
          type: "subjective",
          question: "If the letters of the word 'ALGORITHM' are arranged at random in a row, what is the probability that the letters $G, O, R$ must remain together in that order?",
          solutionSteps: [
            "The word 'ALGORITHM' has $9$ distinct letters: $A, L, G, O, R, I, T, H, M$.",
            "Total number of arrangements $n(S) = 9!$.",
            "Treat the block $(GOR)$ as a single entity because the letters must remain together in that exact order.",
            "We now arrange $7$ entities: $(GOR), A, L, I, T, H, M$.",
            "Number of favourable arrangements $n(E) = 7! \\times 1 = 7!$.",
            "Probability $P(E) = \\frac{7!}{9!} = \\frac{7!}{9 \\times 8 \\times 7!} = \\frac{1}{72}$."
          ],
          answer: "$\\frac{1}{72}$"
        },
        {
          id: "exemplar-11-ch14-sa-10",
          type: "subjective",
          question: "An urn contains $6$ red and $4$ black balls. Two balls are drawn without replacement. Find the probability that both balls are red.",
          solutionSteps: [
            "Total balls in the urn $= 6 + 4 = 10$.",
            "Total ways to choose $2$ balls from $10$: $n(S) = {}^{10}C_2 = \\frac{10 \\times 9}{2} = 45$.",
            "Favourable ways to select $2$ red balls from $6$: $n(E) = {}^{6}C_2 = \\frac{6 \\times 5}{2} = 15$.",
            "Probability $P(E) = \\frac{15}{45} = \\frac{1}{3}$.",
            "Alternatively: Probability first is red $= \\frac{6}{10}$. Probability second is red $= \\frac{5}{9}$.",
            "$P = \\frac{6}{10} \\times \\frac{5}{9} = \\frac{30}{90} = \\frac{1}{3}$."
          ],
          answer: "$\\frac{1}{3}$"
        },
        {
          id: "exemplar-11-ch14-sa-11",
          type: "subjective",
          question: "Check whether the following probabilities $P(A)$ and $P(B)$ are consistently defined: $P(A) = 0.5, P(B) = 0.7, P(A \\cap B) = 0.6$.",
          solutionSteps: [
            "Recall that for any two events $A$ and $B$, $A \\cap B \\subseteq A$ and $A \\cap B \\subseteq B$.",
            "This implies $P(A \\cap B) \\le P(A)$ and $P(A \\cap B) \\le P(B)$.",
            "Here $P(A \\cap B) = 0.6$, whereas $P(A) = 0.5$.",
            "Since $0.6 > 0.5$, $P(A \\cap B) > P(A)$, which violates the fundamental probability axiom.",
            "Hence, the given probabilities are NOT consistently defined."
          ],
          answer: "Not consistently defined (since $P(A \cap B) > P(A)$)"
        },
        {
          id: "exemplar-11-ch14-sa-12",
          type: "subjective",
          question: "A committee of two persons is selected from two men and two women. What is the probability that the committee will have: (i) no man? (ii) one man? (iii) two men?",
          solutionSteps: [
            "Total persons $= 2 + 2 = 4$. Total ways to choose $2$: $n(S) = {}^{4}C_2 = 6$.",
            "(i) No man: Both selected persons are women (${}^{2}C_2 = 1$).",
            "$P(\\text{no man}) = \\frac{1}{6}$.",
            "(ii) One man: One man and one woman (${}^{2}C_1 \\times {}^{2}C_1 = 2 \\times 2 = 4$).",
            "$P(\\text{one man}) = \\frac{4}{6} = \\frac{2}{3}$.",
            "(iii) Two men: Both selected are men (${}^{2}C_2 = 1$).",
            "$P(\\text{two men}) = \\frac{1}{6}$."
          ],
          answer: "(i) $\\frac{1}{6}$, (ii) $\\frac{2}{3}$, (iii) $\\frac{1}{6}$"
        },
        {
          id: "exemplar-11-ch14-sa-13",
          type: "subjective",
          question: "If $E$ and $F$ are events such that $P(E) = \\frac{1}{4}, P(F) = \\frac{1}{2}$ and $P(E \\cap F) = \\frac{1}{8}$, find: (i) $P(E \\cup F)$, (ii) $P(\\text{not } E \\text{ and not } F)$.",
          solutionSteps: [
            "(i) Using addition theorem: $P(E \\cup F) = P(E) + P(F) - P(E \\cap F)$.",
            "$P(E \\cup F) = \\frac{1}{4} + \\frac{1}{2} - \\frac{1}{8} = \\frac{2 + 4 - 1}{8} = \\frac{5}{8}$.",
            "(ii) By De Morgan's Law: $(\\text{not } E \\text{ and not } F) = E' \\cap F' = (E \\cup F)'$.",
            "$P(E' \\cap F') = 1 - P(E \\cup F) = 1 - \\frac{5}{8} = \\frac{3}{8}$."
          ],
          answer: "(i) $\\frac{5}{8}$, (ii) $\\frac{3}{8}$"
        },
        {
          id: "exemplar-11-ch14-sa-14",
          type: "subjective",
          question: "A number is chosen at random from the numbers $1$ to $50$. Find the probability that it is divisible by $4$ or $6$.",
          solutionSteps: [
            "Sample space $S = \\{1, 2, \\dots, 50\\}$, so $n(S) = 50$.",
            "Numbers divisible by $4$: $A = \\{4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48\\} \\implies n(A) = 12$.",
            "Numbers divisible by $6$: $B = \\{6, 12, 18, 24, 30, 36, 42, 48\\} \\implies n(B) = 8$.",
            "Numbers divisible by both $4$ and $6$ (LCM of $4$ and $6 = 12$): $A \\cap B = \\{12, 24, 36, 48\\} \\implies n(A \\cap B) = 4$.",
            "$n(A \\cup B) = n(A) + n(B) - n(A \\cap B) = 12 + 8 - 4 = 16$.",
            "Probability $P(A \\cup B) = \\frac{16}{50} = \\frac{8}{25}$."
          ],
          answer: "$\\frac{8}{25}$"
        },
        {
          id: "exemplar-11-ch14-sa-15",
          type: "subjective",
          question: "Three coins are tossed. Let $A$ be the event 'three heads appear', $B$ be 'two heads and one tail appear', $C$ be 'three tails appear', and $D$ be 'a head appears on the first coin'. Are $A$ and $B$ mutually exclusive? Are $A$ and $C$ mutually exclusive?",
          solutionSteps: [
            "Sample space $S = \\{HHH, HHT, HTH, THH, HTT, THT, TTH, TTT\\}$.",
            "Event $A = \\{HHH\\}$.",
            "Event $B = \\{HHT, HTH, THH\\}$.",
            "Event $C = \\{TTT\\}$.",
            "Since $A \\cap B = \\phi$, events $A$ and $B$ cannot occur simultaneously, hence $A$ and $B$ are mutually exclusive.",
            "Since $A \\cap C = \\phi$, events $A$ and $C$ cannot occur simultaneously, hence $A$ and $C$ are mutually exclusive."
          ],
          answer: "Yes, $A$ and $B$ are mutually exclusive; Yes, $A$ and $C$ are mutually exclusive"
        }
      ]
    },
    {
      exNum: 3,
      title: "Long Answer Type Questions",
      sectionLetter: "L",
      prevUrl: "exemplar-14-2.html",
      prevText: "← Exercise 14.2",
      nextUrl: "../",
      nextText: "← Chapter Index",
      questions: [
        {
          id: "exemplar-11-ch14-la-1",
          type: "subjective",
          question: "If $A, B, C$ are three events associated with a random experiment, prove that:<br>$P(A \\cup B \\cup C) = P(A) + P(B) + P(C) - P(A \\cap B) - P(B \\cap C) - P(C \\cap A) + P(A \\cap B \\cap C)$.",
          solutionSteps: [
            "Let $E = B \\cup C$. Then $P(A \\cup B \\cup C) = P(A \\cup E)$.",
            "By the addition theorem for two events: $P(A \\cup E) = P(A) + P(E) - P(A \\cap E)$.",
            "Here $P(E) = P(B \\cup C) = P(B) + P(C) - P(B \\cap C)$.",
            "Also $A \\cap E = A \\cap (B \\cup C) = (A \\cap B) \\cup (A \\cap C)$ by distributivity of intersection over union.",
            "Applying the addition theorem to $(A \\cap B) \\cup (A \\cap C)$:",
            "$P(A \\cap E) = P(A \\cap B) + P(A \\cap C) - P((A \\cap B) \\cap (A \\cap C)) = P(A \\cap B) + P(A \\cap C) - P(A \\cap B \\cap C)$.",
            "Substituting $P(E)$ and $P(A \\cap E)$ into the expansion of $P(A \\cup E)$:",
            "$P(A \\cup B \\cup C) = P(A) + [P(B) + P(C) - P(B \\cap C)] - [P(A \\cap B) + P(A \\cap C) - P(A \\cap B \\cap C)]$.",
            "$= P(A) + P(B) + P(C) - P(A \\cap B) - P(B \\cap C) - P(C \\cap A) + P(A \\cap B \\cap C)$."
          ],
          answer: "Hence proved by axiomatic set probability."
        },
        {
          id: "exemplar-11-ch14-la-2",
          type: "subjective",
          question: "A bag contains $8$ red and $5$ white balls. Three balls are drawn at random. Find the probability that: (i) All three balls are red, (ii) Exactly one ball is red, (iii) At least two balls are red.",
          solutionSteps: [
            "Total balls in the bag $= 8 + 5 = 13$. Total ways to draw $3$ balls: $n(S) = {}^{13}C_3 = \\frac{13 \\times 12 \\times 11}{6} = 286$.",
            "(i) All three balls red:",
            "Ways to select $3$ red balls from $8$: ${}^{8}C_3 = \\frac{8 \\times 7 \\times 6}{6} = 56$.",
            "$P(\\text{all red}) = \\frac{56}{286} = \\frac{28}{143}$.",
            "(ii) Exactly one red ball (and $2$ white balls):",
            "Ways: ${}^{8}C_1 \\times {}^{5}C_2 = 8 \\times 10 = 80$.",
            "$P(\\text{exactly } 1 \\text{ red}) = \\frac{80}{286} = \\frac{40}{143}$.",
            "(iii) At least two red balls (either $2$ red or $3$ red):",
            "Ways for $2$ red and $1$ white: ${}^{8}C_2 \\times {}^{5}C_1 = 28 \\times 5 = 140$.",
            "Ways for $3$ red: ${}^{8}C_3 = 56$.",
            "Total favourable ways $= 140 + 56 = 196$.",
            "$P(\\text{at least } 2 \\text{ red}) = \\frac{196}{286} = \\frac{98}{143}$."
          ],
          answer: "(i) $\\frac{28}{143}$, (ii) $\\frac{40}{143}$, (iii) $\\frac{98}{143}$"
        },
        {
          id: "exemplar-11-ch14-la-3",
          type: "subjective",
          question: "In a relay race, there are $5$ participating teams $A, B, C, D,$ and $E$. (i) What is the probability that $A, B,$ and $C$ finish first, second, and third, respectively? (ii) What is the probability that $A, B,$ and $C$ finish in the first three positions in any order?",
          solutionSteps: [
            "Total number of ways in which $5$ teams can finish the race is $n(S) = 5! = 120$.",
            "(i) $A, B, C$ finish $1^{\\text{st}}, 2^{\\text{nd}}, 3^{\\text{rd}}$ respectively:",
            "Positions $1, 2, 3$ are fixed for $A, B, C$ ($1$ way).",
            "The remaining $2$ teams ($D, E$) can finish in the remaining $2$ positions in $2! = 2$ ways.",
            "Favourable outcomes $= 1 \\times 2 = 2$.",
            "Probability $= \\frac{2}{120} = \\frac{1}{60}$.",
            "(ii) $A, B, C$ finish in the first three positions in any order:",
            "Teams $A, B, C$ can be arranged among the top three spots in $3! = 6$ ways.",
            "Teams $D, E$ take the remaining two spots in $2! = 2$ ways.",
            "Favourable outcomes $= 3! \\times 2! = 6 \\times 2 = 12$.",
            "Probability $= \\frac{12}{120} = \\frac{1}{10}$."
          ],
          answer: "(i) $\\frac{1}{60}$, (ii) $\\frac{1}{10}$"
        },
        {
          id: "exemplar-11-ch14-la-4",
          type: "subjective",
          question: "Two students $X$ and $Y$ appear in an examination. The probability that $X$ qualifies the exam is $0.05$ and that $Y$ qualifies is $0.10$. The probability that both qualify is $0.02$. Find the probability that: (i) Both will not qualify, (ii) At least one of them will not qualify, (iii) Only one of them will qualify.",
          solutionSteps: [
            "Given $P(X) = 0.05, P(Y) = 0.10$, and $P(X \\cap Y) = 0.02$.",
            "$P(X \\cup Y) = P(X) + P(Y) - P(X \\cap Y) = 0.05 + 0.10 - 0.02 = 0.13$.",
            "(i) Both will not qualify: $P(X' \\cap Y') = 1 - P(X \\cup Y) = 1 - 0.13 = 0.87$.",
            "(ii) At least one will not qualify: $(\\text{both qualify})' = (X \\cap Y)'$.",
            "$P((X \\cap Y)') = 1 - P(X \\cap Y) = 1 - 0.02 = 0.98$.",
            "(iii) Only one qualifies: $P(X \\cap Y') + P(X' \\cap Y) = [P(X) - P(X \\cap Y)] + [P(Y) - P(X \\cap Y)]$.",
            "$= (0.05 - 0.02) + (0.10 - 0.02) = 0.03 + 0.08 = 0.11$."
          ],
          answer: "(i) $0.87$, (ii) $0.98$, (iii) $0.11$"
        },
        {
          id: "exemplar-11-ch14-la-5",
          type: "subjective",
          question: "Find the probability that when a hand of $7$ cards is drawn from a well-shuffled pack of $52$ cards, it contains: (i) all $4$ Kings, (ii) exactly $3$ Kings, (iii) at least $3$ Kings.",
          solutionSteps: [
            "Total number of ways to draw $7$ cards from $52$: $n(S) = {}^{52}C_7$.",
            "A deck has $4$ Kings and $48$ non-Kings.",
            "(i) All $4$ Kings: Must choose all $4$ Kings and $3$ cards from the remaining $48$.",
            "Favourable ways $= {}^{4}C_4 \\times {}^{48}C_3 = 1 \\times {}^{48}C_3 = {}^{48}C_3$.",
            "Probability $= \\frac{{}^{48}C_3}{{}^{52}C_7} = \\frac{17296}{133784560} = \\frac{1}{7735}$.",
            "(ii) Exactly $3$ Kings: Choose $3$ Kings from $4$ and $4$ cards from $48$ non-Kings.",
            "Favourable ways $= {}^{4}C_3 \\times {}^{48}C_4 = 4 \\times 194580 = 778,320$.",
            "Probability $= \\frac{778320}{133784560} = \\frac{9}{1547}$.",
            "(iii) At least $3$ Kings = (Exactly $3$ Kings) + (All $4$ Kings):",
            "Probability $= \\frac{{}^{4}C_3 \\times {}^{48}C_4 + {}^{4}C_4 \\times {}^{48}C_3}{{}^{52}C_7} = \\frac{778320 + 17296}{133784560} = \\frac{795616}{133784560} = \\frac{46}{7735}$."
          ],
          answer: "(i) $\\frac{1}{7735}$, (ii) $\\frac{9}{1547}$, (iii) $\\frac{46}{7735}$"
        },
        {
          id: "exemplar-11-ch14-la-6",
          type: "subjective",
          question: "If $P(A) = x, P(B) = y,$ and $P(A \\cap B) = z$, express the following probabilities in terms of $x, y, z$:<br>(i) $P(\\text{neither } A \\text{ nor } B)$,<br>(ii) $P(\\text{exactly one of } A, B)$,<br>(iii) $P(A \\cap B')$.",
          solutionSteps: [
            "We have $P(A \\cup B) = P(A) + P(B) - P(A \\cap B) = x + y - z$.",
            "(i) 'Neither $A$ nor $B$' is $A' \\cap B' = (A \\cup B)'$.",
            "$P(A' \\cap B') = 1 - P(A \\cup B) = 1 - (x + y - z) = 1 - x - y + z$.",
            "(ii) 'Exactly one of $A, B$' occurs if either $(A \\text{ and not } B)$ or $(B \\text{ and not } A)$ occurs.",
            "Probability $= P(A \\cap B') + P(A' \\cap B) = (x - z) + (y - z) = x + y - 2z$.",
            "(iii) $P(A \\cap B') = P(A) - P(A \\cap B) = x - z$."
          ],
          answer: "(i) $1 - x - y + z$, (ii) $x + y - 2z$, (iii) $x - z$"
        },
        {
          id: "exemplar-11-ch14-la-7",
          type: "subjective",
          question: "Four cards are drawn from a well-shuffled deck of $52$ cards. What is the probability of obtaining $2$ red cards and $2$ black cards?",
          solutionSteps: [
            "A standard deck of $52$ cards has $26$ red cards and $26$ black cards.",
            "Total ways to choose $4$ cards from $52$: $n(S) = {}^{52}C_4 = \\frac{52 \\times 51 \\times 50 \\times 49}{24} = 270,725$.",
            "Ways to select $2$ red cards from $26$: ${}^{26}C_2 = \\frac{26 \\times 25}{2} = 325$.",
            "Ways to select $2$ black cards from $26$: ${}^{26}C_2 = \\frac{26 \\times 25}{2} = 325$.",
            "Number of favourable outcomes $n(E) = {}^{26}C_2 \\times {}^{26}C_2 = 325 \\times 325 = 105,625$.",
            "Probability $P(E) = \\frac{105625}{270725} = \\frac{325}{833} \\approx 0.390$."
          ],
          answer: "$\\frac{325}{833}$"
        },
        {
          id: "exemplar-11-ch14-la-8",
          type: "subjective",
          question: "A box contains $100$ tickets numbered $1, 2, \\dots, 100$. Two tickets are chosen at random. It is given that the maximum number on the two chosen tickets is not more than $10$. Find the probability that the minimum number on them is $5$.",
          solutionSteps: [
            "Let event $B$ be 'the maximum number on the two chosen tickets is $\\le 10$'.",
            "Both tickets must be chosen from the set $\\{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\\}$ (10 tickets).",
            "Number of ways to choose $2$ tickets from these $10$: $n(B) = {}^{10}C_2 = \\frac{10 \\times 9}{2} = 45$.",
            "Let event $A$ be 'the minimum number on them is $5$'.",
            "We want the conditional probability $P(A|B) = \\frac{n(A \\cap B)}{n(B)}$.",
            "For $A \\cap B$, both tickets must be in $\\{1, 2, \\dots, 10\\}$, the smaller ticket must be $5$, and the larger ticket must be strictly greater than $5$ (i.e. $6, 7, 8, 9,$ or $10$).",
            "The larger ticket can be any of the $5$ numbers: $\\{6, 7, 8, 9, 10\\}$.",
            "So $n(A \\cap B) = 5$.",
            "Therefore, $P(A|B) = \\frac{5}{45} = \\frac{1}{9}$."
          ],
          answer: "$\\frac{1}{9}$"
        }
      ]
    }
  ]
};
