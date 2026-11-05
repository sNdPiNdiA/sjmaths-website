// Data for Chapter 13: Statistics
module.exports = {
  chapterNum: 13,
  chapterName: "Statistics",
  chapterSlug: "chapter-13-statistics",
  exercises: [
    {
      exNum: 1,
      title: "Objective Type Questions (MCQs)",
      sectionLetter: "Q",
      prevUrl: "/class-11-maths/ncert-exemplar-practice/chapter-12-limits-derivatives/exemplar-12-3.html",
      prevText: "← Chapter 12",
      nextUrl: "exemplar-13-2.html",
      nextText: "Exercise 13.2 →",
      questions: [
        {
          id: "exemplar-11-ch13-1",
          type: "mcq",
          question: "The mean deviation of the data $3, 10, 10, 4, 7, 10, 5$ from the mean is",
          options: [
            "(a) $2$",
            "(b) $2.57$",
            "(c) $3$",
            "(d) $3.75$"
          ],
          solutionSteps: [
            "Calculate the arithmetic mean $\\bar{x}$:",
            "$\\bar{x} = \\frac{3 + 10 + 10 + 4 + 7 + 10 + 5}{7} = \\frac{49}{7} = 7$.",
            "Calculate the absolute deviations $|x_i - \\bar{x}|$:",
            "$|3 - 7| = 4, |10 - 7| = 3, |10 - 7| = 3, |4 - 7| = 3, |7 - 7| = 0, |10 - 7| = 3, |5 - 7| = 2$.",
            "Sum of absolute deviations $\\sum |x_i - \\bar{x}| = 4 + 3 + 3 + 3 + 0 + 3 + 2 = 18$.",
            "Mean Deviation $MD(\\bar{x}) = \\frac{\\sum |x_i - \\bar{x}|}{n} = \\frac{18}{7} \\approx 2.57$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch13-2",
          type: "mcq",
          question: "The variance of the first $n$ natural numbers is",
          options: [
            "(a) $\\frac{n^2 - 1}{12}$",
            "(b) $\\frac{n^2 - 1}{6}$",
            "(c) $\\frac{n(n + 1)}{12}$",
            "(d) $\\frac{n^2 + 1}{12}$"
          ],
          solutionSteps: [
            "Mean of first $n$ natural numbers $\\bar{x} = \\frac{n(n + 1)}{2n} = \\frac{n + 1}{2}$.",
            "Sum of squares of first $n$ natural numbers $\\sum x_i^2 = \\frac{n(n + 1)(2n + 1)}{6}$.",
            "Variance $\\sigma^2 = \\frac{\\sum x_i^2}{n} - (\\bar{x})^2 = \\frac{(n + 1)(2n + 1)}{6} - \\frac{(n + 1)^2}{4}$.",
            "$\\sigma^2 = \\frac{n + 1}{12}[2(2n + 1) - 3(n + 1)] = \\frac{n + 1}{12}[4n + 2 - 3n - 3] = \\frac{(n + 1)(n - 1)}{12} = \\frac{n^2 - 1}{12}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch13-3",
          type: "mcq",
          question: "If the standard deviation of numbers $2, 3, 2x, 11$ is $3.5$, then the variance of the numbers is",
          options: [
            "(a) $3.5$",
            "(b) $7$",
            "(c) $12.25$",
            "(d) $1.87$"
          ],
          solutionSteps: [
            "Standard deviation $\\sigma = 3.5$.",
            "By definition, Variance $= \\sigma^2$.",
            "Variance $= (3.5)^2 = 12.25$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-4",
          type: "mcq",
          question: "If the variance of a set of observations is $16$ and each observation is multiplied by $3$, the variance of the resulting observations is",
          options: [
            "(a) $16$",
            "(b) $48$",
            "(c) $144$",
            "(d) $9$"
          ],
          solutionSteps: [
            "Let initial observations have variance $\\sigma^2 = 16$.",
            "If each observation $x_i$ is transformed into $y_i = c \\cdot x_i$, then $\\sigma_y^2 = c^2 \\sigma_x^2$.",
            "Here $c = 3$, so new variance $= 3^2 \\times 16 = 9 \\times 16 = 144$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-5",
          type: "mcq",
          question: "If each observation in a data set is increased by $5$, then the standard deviation",
          options: [
            "(a) increases by $5$",
            "(b) decreases by $5$",
            "(c) remains unchanged",
            "(d) becomes $5$ times"
          ],
          solutionSteps: [
            "Standard deviation is independent of the change of origin.",
            "If $y_i = x_i + a$, then $\\bar{y} = \\bar{x} + a$, so $(y_i - \\bar{y}) = (x_i + a - (\\bar{x} + a)) = x_i - \\bar{x}$.",
            "Hence, the deviations from the mean remain identical.",
            "Thus, the standard deviation remains unchanged."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-6",
          type: "mcq",
          question: "The mean of $100$ observations is $50$ and their standard deviation is $5$. The sum of all squares of the observations is",
          options: [
            "(a) $50,000$",
            "(b) $250,000$",
            "(c) $252,500$",
            "(d) $255,000$"
          ],
          solutionSteps: [
            "Given $n = 100$, $\\bar{x} = 50$, and $\\sigma = 5 \\implies \\sigma^2 = 25$.",
            "Using the variance formula: $\\sigma^2 = \\frac{\\sum x_i^2}{n} - (\\bar{x})^2$.",
            "$25 = \\frac{\\sum x_i^2}{100} - (50)^2 = \\frac{\\sum x_i^2}{100} - 2500$.",
            "$\\frac{\\sum x_i^2}{100} = 2525 \\implies \\sum x_i^2 = 252,500$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-7",
          type: "mcq",
          question: "The coefficient of variation for a distribution with mean $40$ and standard deviation $8$ is",
          options: [
            "(a) $20\\%$",
            "(b) $25\\%$",
            "(c) $15\\%$",
            "(d) $32\\%$"
          ],
          solutionSteps: [
            "Formula for Coefficient of Variation: $\\text{C.V.} = \\frac{\\sigma}{\\bar{x}} \\times 100$.",
            "Given $\\sigma = 8$ and $\\bar{x} = 40$.",
            "$\\text{C.V.} = \\frac{8}{40} \\times 100 = \\frac{1}{5} \\times 100 = 20\\%$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch13-8",
          type: "mcq",
          question: "For two data sets $A$ and $B$, $\\text{C.V.}_A = 40\\%$ and $\\text{C.V.}_B = 55\\%$. Which data set is more consistent?",
          options: [
            "(a) $A$",
            "(b) $B$",
            "(c) Both equally consistent",
            "(d) Cannot be determined"
          ],
          solutionSteps: [
            "The series having a smaller coefficient of variation is said to be more consistent or less variable.",
            "Here $\\text{C.V.}_A = 40\\% < \\text{C.V.}_B = 55\\%$.",
            "Therefore, series $A$ is more consistent than series $B$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch13-9",
          type: "mcq",
          question: "The mean deviation about the median for the observations $11, 3, 8, 7, 5, 14, 10, 2, 9$ is",
          options: [
            "(a) $2.5$",
            "(b) $2.8$",
            "(c) $3.0$",
            "(d) $3.4$"
          ],
          solutionSteps: [
            "Arrange data in ascending order: $2, 3, 5, 7, 8, 9, 10, 11, 14$.",
            "Number of observations $n = 9$ (odd).",
            "$\\text{Median } M = \\left(\\frac{9 + 1}{2}\\right)^{\\text{th}} \\text{ observation} = 5^{\\text{th}} \\text{ observation} = 8$.",
            "Absolute deviations $|x_i - M|$: $|2 - 8| = 6, |3 - 8| = 5, |5 - 8| = 3, |7 - 8| = 1, |8 - 8| = 0, |9 - 8| = 1, |10 - 8| = 2, |11 - 8| = 3, |14 - 8| = 6$.",
            "Sum $\\sum |x_i - M| = 6 + 5 + 3 + 1 + 0 + 1 + 2 + 3 + 6 = 27$.",
            "$MD(M) = \\frac{\\sum |x_i - M|}{n} = \\frac{27}{9} = 3.0$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-10",
          type: "mcq",
          question: "The range of the data $12, 25, 15, 18, 35, 29, 40, 10, 22$ is",
          options: [
            "(a) $25$",
            "(b) $28$",
            "(c) $30$",
            "(d) $40$"
          ],
          solutionSteps: [
            "Maximum observation $X_{\\max} = 40$.",
            "Minimum observation $X_{\\min} = 10$.",
            "$\\text{Range} = X_{\\max} - X_{\\min} = 40 - 10 = 30$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-11",
          type: "mcq",
          question: "If the standard deviation of $x_1, x_2, \\dots, x_n$ is $\\sigma$, then the standard deviation of $ax_1 + b, ax_2 + b, \\dots, ax_n + b$ is",
          options: [
            "(a) $a\\sigma + b$",
            "(b) $|a|\\sigma$",
            "(c) $a^2\\sigma$",
            "(d) $|a|\\sigma + b$"
          ],
          solutionSteps: [
            "Let $y_i = ax_i + b$. Then $\\bar{y} = a\\bar{x} + b$.",
            "$y_i - \\bar{y} = (ax_i + b) - (a\\bar{x} + b) = a(x_i - \\bar{x})$.",
            "Variance $\\sigma_y^2 = \\frac{1}{n}\\sum (y_i - \\bar{y})^2 = \\frac{1}{n}\\sum a^2(x_i - \\bar{x})^2 = a^2 \\sigma_x^2$.",
            "Standard deviation $\\sigma_y = \\sqrt{a^2\\sigma_x^2} = |a|\\sigma$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch13-12",
          type: "mcq",
          question: "The mean and variance of $7$ observations are $8$ and $16$, respectively. If five of the observations are $2, 4, 10, 12, 14$, then the remaining two observations are",
          options: [
            "(a) $6$ and $8$",
            "(b) $5$ and $9$",
            "(c) $4$ and $10$",
            "(d) $7$ and $7$"
          ],
          solutionSteps: [
            "Let the remaining two observations be $x$ and $y$.",
            "Sum of $7$ observations: $2 + 4 + 10 + 12 + 14 + x + y = 7 \\times 8 = 56 \\implies 42 + x + y = 56 \\implies x + y = 14$.",
            "Sum of squares: $\\sigma^2 = \\frac{\\sum x_i^2}{7} - (\\bar{x})^2 \\implies 16 = \\frac{\\sum x_i^2}{7} - 64 \\implies \\sum x_i^2 = 7 \\times 80 = 560$.",
            "Sum of squares of five known observations: $2^2 + 4^2 + 10^2 + 12^2 + 14^2 = 4 + 16 + 100 + 144 + 196 = 460$.",
            "Therefore, $x^2 + y^2 = 560 - 460 = 100$.",
            "$(x + y)^2 = x^2 + y^2 + 2xy \\implies 14^2 = 100 + 2xy \\implies 196 = 100 + 2xy \\implies 2xy = 96 \\implies xy = 48$.",
            "Quadratic equation: $t^2 - 14t + 48 = 0 \\implies (t - 6)(t - 8) = 0 \\implies t = 6, 8$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch13-13",
          type: "mcq",
          question: "Consider the numbers $1, 2, 3, 4, 5, 6, 7, 8, 9, 10$. If $1$ is added to each number, the variance of the numbers will",
          options: [
            "(a) increase by $1$",
            "(b) decrease by $1$",
            "(c) remain the same",
            "(d) become double"
          ],
          solutionSteps: [
            "Variance is independent of change of origin.",
            "Adding a constant to each observation shifts the distribution as a whole without altering the spread or dispersion.",
            "Hence, the variance remains identical."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch13-14",
          type: "mcq",
          question: "If $\\sum_{i=1}^{10} (x_i - 5) = 10$ and $\\sum_{i=1}^{10} (x_i - 5)^2 = 40$, then the standard deviation of $x_1, x_2, \\dots, x_{10}$ is",
          options: [
            "(a) $\\sqrt{3}$",
            "(b) $3$",
            "(c) $4$",
            "(d) $\\sqrt{5}$"
          ],
          solutionSteps: [
            "Let $d_i = x_i - 5$.",
            "Then $\\sigma_x = \\sigma_d = \\sqrt{\\frac{\\sum d_i^2}{n} - \\left(\\frac{\\sum d_i}{n}\\right)^2}$.",
            "Substitute $n = 10$, $\\sum d_i = 10$, and $\\sum d_i^2 = 40$:",
            "$\\sigma = \\sqrt{\\frac{40}{10} - \\left(\\frac{10}{10}\\right)^2} = \\sqrt{4 - 1^2} = \\sqrt{3}$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch13-15",
          type: "mcq",
          question: "The algebraic sum of the deviations of a set of $n$ values from their arithmetic mean is always",
          options: [
            "(a) $> 0$",
            "(b) $< 0$",
            "(c) $0$",
            "(d) $n$"
          ],
          solutionSteps: [
            "By definition, $\\bar{x} = \\frac{\\sum x_i}{n} \\implies \\sum x_i = n\\bar{x}$.",
            "Sum of deviations from mean: $\\sum (x_i - \\bar{x}) = \\sum x_i - \\sum \\bar{x} = n\\bar{x} - n\\bar{x} = 0$.",
            "Therefore, the algebraic sum of deviations from the arithmetic mean is always zero."
          ],
          answer: "(c)"
        }
      ]
    },
    {
      exNum: 2,
      title: "Short Answer Type Questions",
      sectionLetter: "S",
      prevUrl: "exemplar-13-1.html",
      prevText: "← Exercise 13.1",
      nextUrl: "exemplar-13-3.html",
      nextText: "Exercise 13.3 →",
      questions: [
        {
          id: "exemplar-11-ch13-sa-1",
          type: "subjective",
          question: "Find the mean deviation about the mean for the data: $4, 7, 8, 9, 10, 12, 13, 17$.",
          solutionSteps: [
            "Mean $\\bar{x} = \\frac{4 + 7 + 8 + 9 + 10 + 12 + 13 + 17}{8} = \\frac{80}{8} = 10$.",
            "Compute deviations $|x_i - \\bar{x}|$: $|4 - 10| = 6, |7 - 10| = 3, |8 - 10| = 2, |9 - 10| = 1, |10 - 10| = 0, |12 - 10| = 2, |13 - 10| = 3, |17 - 10| = 7$.",
            "Sum $\\sum |x_i - \\bar{x}| = 6 + 3 + 2 + 1 + 0 + 2 + 3 + 7 = 24$.",
            "$MD(\\bar{x}) = \\frac{24}{8} = 3$."
          ],
          answer: "$3$"
        },
        {
          id: "exemplar-11-ch13-sa-2",
          type: "subjective",
          question: "Find the mean deviation about the median for the observations: $39, 72, 48, 41, 43, 40, 45, 54, 70, 62$.",
          solutionSteps: [
            "Arrange data in ascending order: $39, 40, 41, 43, 45, 48, 54, 62, 70, 72$.",
            "Here $n = 10$ (even). Median is the average of $5^{\\text{th}}$ and $6^{\\text{th}}$ terms:",
            "$M = \\frac{45 + 48}{2} = 46.5$.",
            "Compute $|x_i - M|$: $|39 - 46.5| = 7.5, |40 - 46.5| = 6.5, |41 - 46.5| = 5.5, |43 - 46.5| = 3.5, |45 - 46.5| = 1.5, |48 - 46.5| = 1.5, |54 - 46.5| = 7.5, |62 - 46.5| = 15.5, |70 - 46.5| = 23.5, |72 - 46.5| = 25.5$.",
            "Sum $\\sum |x_i - M| = 7.5 + 6.5 + 5.5 + 3.5 + 1.5 + 1.5 + 7.5 + 15.5 + 23.5 + 25.5 = 98$.",
            "$MD(M) = \\frac{98}{10} = 9.8$."
          ],
          answer: "$9.8$"
        },
        {
          id: "exemplar-11-ch13-sa-3",
          type: "subjective",
          question: "Find the variance and standard deviation of the numbers: $6, 7, 10, 12, 13, 4, 8, 12$.",
          solutionSteps: [
            "Number of observations $n = 8$.",
            "Sum $\\sum x_i = 6 + 7 + 10 + 12 + 13 + 4 + 8 + 12 = 72$.",
            "Mean $\\bar{x} = \\frac{72}{8} = 9$.",
            "Sum of squares of deviations $\\sum (x_i - \\bar{x})^2$:",
            "$(6 - 9)^2 + (7 - 9)^2 + (10 - 9)^2 + (12 - 9)^2 + (13 - 9)^2 + (4 - 9)^2 + (8 - 9)^2 + (12 - 9)^2$",
            "$= 9 + 4 + 1 + 9 + 16 + 25 + 1 + 9 = 74$.",
            "Variance $\\sigma^2 = \\frac{74}{8} = 9.25$.",
            "Standard deviation $\\sigma = \\sqrt{9.25} \\approx 3.04$."
          ],
          answer: "Variance $= 9.25$, Standard Deviation $\\approx 3.04$"
        },
        {
          id: "exemplar-11-ch13-sa-4",
          type: "subjective",
          question: "The mean and standard deviation of $20$ observations are found to be $10$ and $2$, respectively. On rechecking, it was found that an observation $8$ was incorrect. Calculate the correct mean and standard deviation if the wrong item is omitted.",
          solutionSteps: [
            "Given $n = 20, \\bar{x} = 10, \\sigma = 2$.",
            "Incorrect sum $\\sum x_i = 20 \\times 10 = 200$.",
            "Omitting the wrong observation $8$: New $n' = 19$, Correct sum $= 200 - 8 = 192$.",
            "Correct mean $\\bar{x}' = \\frac{192}{19} \\approx 10.11$.",
            "Given $\\sigma^2 = 4 \\implies \\frac{\\sum x_i^2}{20} - 10^2 = 4 \\implies \\frac{\\sum x_i^2}{20} = 104 \\implies \\sum x_i^2 = 2080$.",
            "Correct sum of squares $= 2080 - 8^2 = 2080 - 64 = 2016$.",
            "Correct variance $\\sigma'^2 = \\frac{2016}{19} - \\left(\\frac{192}{19}\\right)^2 = \\frac{2016 \\times 19 - 36864}{361} = \\frac{38304 - 36864}{361} = \\frac{1440}{361} \\approx 3.99$.",
            "Correct standard deviation $\\sigma' = \\sqrt{\\frac{1440}{361}} = \\frac{12\\sqrt{10}}{19} \\approx 1.997$."
          ],
          answer: "Correct Mean $= 10.11$, Correct S.D. $\\approx 2.00$"
        },
        {
          id: "exemplar-11-ch13-sa-5",
          type: "subjective",
          question: "Find the mean deviation about the mean for the discrete frequency distribution: $x_i = [5, 10, 15, 20, 25]$, $f_i = [7, 4, 6, 3, 5]$.",
          solutionSteps: [
            "$N = \\sum f_i = 7 + 4 + 6 + 3 + 5 = 25$.",
            "$\\sum f_i x_i = 5(7) + 10(4) + 15(6) + 20(3) + 25(5) = 35 + 40 + 90 + 60 + 125 = 350$.",
            "Mean $\\bar{x} = \\frac{350}{25} = 14$.",
            "Absolute deviations $|x_i - \\bar{x}|$: $|5 - 14| = 9, |10 - 14| = 4, |15 - 14| = 1, |20 - 14| = 6, |25 - 14| = 11$.",
            "$\\sum f_i |x_i - \\bar{x}| = 7(9) + 4(4) + 6(1) + 3(6) + 5(11) = 63 + 16 + 6 + 18 + 55 = 158$.",
            "$MD(\\bar{x}) = \\frac{\\sum f_i |x_i - \\bar{x}|}{N} = \\frac{158}{25} = 6.32$."
          ],
          answer: "$6.32$"
        },
        {
          id: "exemplar-11-ch13-sa-6",
          type: "subjective",
          question: "Find the mean deviation about the median for the data: $x_i = [10, 15, 20, 25, 30, 35]$, $f_i = [3, 2, 5, 8, 4, 3]$.",
          solutionSteps: [
            "Compute cumulative frequencies ($cf$):",
            "$x_i$: $10 (cf=3), 15 (cf=5), 20 (cf=10), 25 (cf=18), 30 (cf=22), 35 (cf=25)$.",
            "$N = 25$. $\\frac{N + 1}{2} = 13^{\\text{th}}$ observation.",
            "The observation corresponding to cumulative frequency $\\ge 13$ is $x_i = 25$, so Median $M = 25$.",
            "Absolute deviations $|x_i - M|$: $|10 - 25| = 15, |15 - 25| = 10, |20 - 25| = 5, |25 - 25| = 0, |30 - 25| = 5, |35 - 25| = 10$.",
            "$\\sum f_i |x_i - M| = 3(15) + 2(10) + 5(5) + 8(0) + 4(5) + 3(10) = 45 + 20 + 25 + 0 + 20 + 30 = 140$.",
            "$MD(M) = \\frac{140}{25} = 5.6$."
          ],
          answer: "$5.6$"
        },
        {
          id: "exemplar-11-ch13-sa-7",
          type: "subjective",
          question: "Two manufacturing plants $A$ and $B$ produce steel tubes. For Plant $A$, mean length $\\bar{x}_A = 50\\text{ cm}$, $\\sigma_A = 5\\text{ cm}$; for Plant $B$, $\\bar{x}_B = 60\\text{ cm}$, $\\sigma_B = 6\\text{ cm}$. Compare their variability.",
          solutionSteps: [
            "Coefficient of Variation for Plant $A$: $\\text{C.V.}_A = \\frac{\\sigma_A}{\\bar{x}_A} \\times 100 = \\frac{5}{50} \\times 100 = 10\\%$.",
            "Coefficient of Variation for Plant $B$: $\\text{C.V.}_B = \\frac{\\sigma_B}{\\bar{x}_B} \\times 100 = \\frac{6}{60} \\times 100 = 10\\%$.",
            "Since $\\text{C.V.}_A = \\text{C.V.}_B = 10\\%$, both manufacturing plants exhibit equal consistency and identical variability in production."
          ],
          answer: "Both plants have equal consistency ($\text{C.V.} = 10\\%$)"
        },
        {
          id: "exemplar-11-ch13-sa-8",
          type: "subjective",
          question: "The mean of $5$ observations is $4.4$ and their variance is $8.24$. If three of the observations are $1, 2,$ and $6$, find the other two observations.",
          solutionSteps: [
            "Let the other two observations be $x$ and $y$.",
            "Mean: $\\frac{1 + 2 + 6 + x + y}{5} = 4.4 \\implies 9 + x + y = 22 \\implies x + y = 13$.",
            "Variance: $\\frac{1^2 + 2^2 + 6^2 + x^2 + y^2}{5} - (4.4)^2 = 8.24$.",
            "$\\frac{1 + 4 + 36 + x^2 + y^2}{5} - 19.36 = 8.24 \\implies \\frac{41 + x^2 + y^2}{5} = 27.60$.",
            "$41 + x^2 + y^2 = 138 \\implies x^2 + y^2 = 97$.",
            "$(x + y)^2 = x^2 + y^2 + 2xy \\implies 13^2 = 97 + 2xy \\implies 169 = 97 + 2xy \\implies 2xy = 72 \\implies xy = 36$.",
            "Equation: $t^2 - 13t + 36 = 0 \\implies (t - 4)(t - 9) = 0 \\implies t = 4, 9$."
          ],
          answer: "$4$ and $9$"
        },
        {
          id: "exemplar-11-ch13-sa-9",
          type: "subjective",
          question: "Find the standard deviation for the first $10$ multiples of $3$.",
          solutionSteps: [
            "The first $10$ multiples of $3$ are: $3, 6, 9, 12, 15, 18, 21, 24, 27, 30$.",
            "These can be written as $3 \\times (1, 2, 3, \\dots, 10)$.",
            "Variance of first $n = 10$ natural numbers is $\\frac{n^2 - 1}{12} = \\frac{10^2 - 1}{12} = \\frac{99}{12} = \\frac{33}{4} = 8.25$.",
            "Multiplying each number by $3$ scales standard deviation by $3$:",
            "$\\sigma = 3 \\times \\sqrt{8.25} = 3 \\times \\frac{\\sqrt{33}}{2} = \\frac{3\\sqrt{33}}{2} \\approx 8.62$."
          ],
          answer: "$\\frac{3\\sqrt{33}}{2} \\approx 8.62$"
        },
        {
          id: "exemplar-11-ch13-sa-10",
          type: "subjective",
          question: "The sum and sum of squares corresponding to $10$ observations are given by $\\sum (x_i - 5) = 3$ and $\\sum (x_i - 5)^2 = 43$. Find the mean and standard deviation.",
          solutionSteps: [
            "Let $u_i = x_i - 5$, with $n = 10$.",
            "$\\bar{u} = \\frac{\\sum u_i}{n} = \\frac{3}{10} = 0.3$.",
            "Mean $\\bar{x} = 5 + \\bar{u} = 5 + 0.3 = 5.3$.",
            "Variance $\\sigma^2 = \\frac{\\sum u_i^2}{n} - (\\bar{u})^2 = \\frac{43}{10} - (0.3)^2 = 4.3 - 0.09 = 4.21$.",
            "Standard deviation $\\sigma = \\sqrt{4.21} \\approx 2.05$."
          ],
          answer: "Mean $= 5.3$, Standard Deviation $\\approx 2.05$"
        },
        {
          id: "exemplar-11-ch13-sa-11",
          type: "subjective",
          question: "Find the coefficient of variation for the following observations: $35, 40, 42, 45, 48, 50$.",
          solutionSteps: [
            "$n = 6$. Sum $\\sum x_i = 35 + 40 + 42 + 45 + 48 + 50 = 260$.",
            "Mean $\\bar{x} = \\frac{260}{6} = \\frac{130}{3} \\approx 43.33$.",
            "Deviations $(x_i - \\bar{x})$: $35 - 43.33 = -8.33, 40 - 43.33 = -3.33, 42 - 43.33 = -1.33, 45 - 43.33 = 1.67, 48 - 43.33 = 4.67, 50 - 43.33 = 6.67$.",
            "Sum of squared deviations $\\sum (x_i - \\bar{x})^2 \\approx 69.39 + 11.09 + 1.77 + 2.79 + 21.81 + 44.49 = 151.34$.",
            "Variance $\\sigma^2 = \\frac{151.34}{6} \\approx 25.22 \\implies \\sigma = \\sqrt{25.22} \\approx 5.02$.",
            "$\\text{C.V.} = \\frac{5.02}{43.33} \\times 100 \\approx 11.59\\%$."
          ],
          answer: "$\\approx 11.59\\%$"
        },
        {
          id: "exemplar-11-ch13-sa-12",
          type: "subjective",
          question: "Prove that the variance of the first $2n$ even natural numbers is $\\frac{4(4n^2 - 1)}{12} = \\frac{4n^2 - 1}{3}$.",
          solutionSteps: [
            "The first $2n$ even natural numbers are $2, 4, 6, \\dots, 4n$.",
            "This can be written as $2(1, 2, 3, \\dots, 2n)$.",
            "The variance of the first $N = 2n$ natural numbers is $\\frac{N^2 - 1}{12} = \\frac{(2n)^2 - 1}{12} = \\frac{4n^2 - 1}{12}$.",
            "Since each number is multiplied by $2$, the variance is multiplied by $2^2 = 4$:",
            "$\\text{Variance} = 4 \\times \\frac{4n^2 - 1}{12} = \\frac{4n^2 - 1}{3}$."
          ],
          answer: "$\\frac{4n^2 - 1}{3}$ (Hence proved)"
        },
        {
          id: "exemplar-11-ch13-sa-13",
          type: "subjective",
          question: "Find the mean deviation about the mean for the discrete distribution: $x_i = [2, 4, 6, 8, 10]$, $f_i = [1, 3, 5, 3, 1]$.",
          solutionSteps: [
            "$N = \\sum f_i = 1 + 3 + 5 + 3 + 1 = 13$.",
            "$\\sum f_i x_i = 2(1) + 4(3) + 6(5) + 8(3) + 10(1) = 2 + 12 + 30 + 24 + 10 = 78$.",
            "Mean $\\bar{x} = \\frac{78}{13} = 6$.",
            "Deviations $|x_i - 6|$: $|2 - 6| = 4, |4 - 6| = 2, |6 - 6| = 0, |8 - 6| = 2, |10 - 6| = 4$.",
            "$\\sum f_i |x_i - \\bar{x}| = 1(4) + 3(2) + 5(0) + 3(2) + 1(4) = 4 + 6 + 0 + 6 + 4 = 20$.",
            "$MD(\\bar{x}) = \\frac{20}{13} \\approx 1.54$."
          ],
          answer: "$\\frac{20}{13} \\approx 1.54$"
        },
        {
          id: "exemplar-11-ch13-sa-14",
          type: "subjective",
          question: "An analysis of monthly wages paid to workers in two firms $A$ and $B$ gave: Number of wage earners $n_A = 500, n_B = 600$; Mean monthly wage $\\bar{x}_A = 186, \\bar{x}_B = 175$; Variance $\\sigma_A^2 = 81, \\sigma_B^2 = 100$. (i) Which firm pays a larger total amount? (ii) Which firm shows greater variability in individual wages?",
          solutionSteps: [
            "(i) Total monthly wage bill = $n \\times \\bar{x}$.",
            "For firm $A$: $500 \\times 186 = 93,000$.",
            "For firm $B$: $600 \\times 175 = 105,000$.",
            "Firm $B$ pays a larger amount ($105,000 > 93,000$).",
            "(ii) Variability is determined by Coefficient of Variation (C.V.):",
            "$\\sigma_A = \\sqrt{81} = 9 \\implies \\text{C.V.}_A = \\frac{9}{186} \\times 100 \\approx 4.84\\%$.",
            "$\\sigma_B = \\sqrt{100} = 10 \\implies \\text{C.V.}_B = \\frac{10}{175} \\times 100 \\approx 5.71\\%$.",
            "Since $\\text{C.V.}_B > \\text{C.V.}_A$, firm $B$ shows greater variability in wages."
          ],
          answer: "(i) Firm $B$, (ii) Firm $B$"
        },
        {
          id: "exemplar-11-ch13-sa-15",
          type: "subjective",
          question: "The standard deviation of $15$ observations is $6$. If each observation is multiplied by $-2$ and then decreased by $3$, find the new variance and new standard deviation.",
          solutionSteps: [
            "Let original observations be $x_i$ with $\\sigma_x = 6$.",
            "Transformed observations $y_i = -2x_i - 3$.",
            "Under the linear transformation $y_i = ax_i + b$, $\\sigma_y = |a|\\sigma_x$.",
            "Here $a = -2$, so $\\sigma_y = |-2| \\times 6 = 2 \\times 6 = 12$.",
            "New Variance $\\sigma_y^2 = 12^2 = 144$."
          ],
          answer: "New Variance $= 144$, New S.D. $= 12$"
        }
      ]
    },
    {
      exNum: 3,
      title: "Long Answer Type Questions",
      sectionLetter: "L",
      prevUrl: "exemplar-13-2.html",
      prevText: "← Exercise 13.2",
      nextUrl: "/class-11-maths/ncert-exemplar-practice/chapter-14-probability/exemplar-14-1.html",
      nextText: "Chapter 14 →",
      questions: [
        {
          id: "exemplar-11-ch13-la-1",
          type: "subjective",
          question: "Calculate the mean, variance, and standard deviation for the following continuous frequency distribution using the shortcut step-deviation method:<br>Classes: $30-40, 40-50, 50-60, 60-70, 70-80, 80-90, 90-100$;<br>Frequencies: $3, 7, 12, 15, 8, 3, 2$.",
          solutionSteps: [
            "Mid-points $x_i$: $35, 45, 55, 65, 75, 85, 95$.",
            "Class width $h = 10$. Choose assumed mean $A = 65$.",
            "Step deviation $u_i = \\frac{x_i - 65}{10}$: $-3, -2, -1, 0, 1, 2, 3$.",
            "Frequencies $f_i$: $3, 7, 12, 15, 8, 3, 2$. $N = \\sum f_i = 50$.",
            "Products $f_i u_i$: $3(-3) = -9, 7(-2) = -14, 12(-1) = -12, 15(0) = 0, 8(1) = 8, 3(2) = 6, 2(3) = 6$.",
            "$\\sum f_i u_i = -35 + 20 = -15$.",
            "Products $f_i u_i^2$: $3(9) = 27, 7(4) = 28, 12(1) = 12, 15(0) = 0, 8(1) = 8, 3(4) = 12, 2(9) = 18$.",
            "$\\sum f_i u_i^2 = 27 + 28 + 12 + 0 + 8 + 12 + 18 = 105$.",
            "Mean $\\bar{x} = A + \\left(\\frac{\\sum f_i u_i}{N}\\right)h = 65 + \\left(\\frac{-15}{50}\\right)10 = 65 - 3 = 62$.",
            "Variance $\\sigma^2 = h^2 \\left[\\frac{\\sum f_i u_i^2}{N} - \\left(\\frac{\\sum f_i u_i}{N}\\right)^2\\right] = 100 \\left[\\frac{105}{50} - \\left(-\\frac{15}{50}\\right)^2\\right] = 100 [2.10 - 0.09] = 100(2.01) = 201$.",
            "Standard deviation $\\sigma = \\sqrt{201} \\approx 14.18$."
          ],
          answer: "Mean $= 62$, Variance $= 201$, S.D. $\\approx 14.18$"
        },
        {
          id: "exemplar-11-ch13-la-2",
          type: "subjective",
          question: "Find the mean deviation about the median for the grouped continuous data:<br>Classes: $0-10, 10-20, 20-30, 30-40, 40-50, 50-60$;<br>Frequencies: $6, 7, 15, 16, 4, 2$.",
          solutionSteps: [
            "Compute cumulative frequencies ($cf$):",
            "$0-10: f=6, cf=6$; $10-20: f=7, cf=13$; $20-30: f=15, cf=28$; $30-40: f=16, cf=44$; $40-50: f=4, cf=48$; $50-60: f=2, cf=50$.",
            "$N = 50 \\implies \\frac{N}{2} = 25$. Median class is $20-30$ ($cf=28$).",
            "Median $M = l + \\left(\\frac{N/2 - cf_0}{f}\\right)h = 20 + \\left(\\frac{25 - 13}{15}\\right)10 = 20 + \\frac{120}{15} = 20 + 8 = 28$.",
            "Mid-points $x_i$: $5, 15, 25, 35, 45, 55$.",
            "Deviations $|x_i - 28|$: $|5 - 28| = 23, |15 - 28| = 13, |25 - 28| = 3, |35 - 28| = 7, |45 - 28| = 17, |55 - 28| = 27$.",
            "$\\sum f_i |x_i - M| = 6(23) + 7(13) + 15(3) + 16(7) + 4(17) + 2(27) = 138 + 91 + 45 + 112 + 68 + 54 = 508$.",
            "$MD(M) = \\frac{508}{50} = 10.16$."
          ],
          answer: "$10.16$"
        },
        {
          id: "exemplar-11-ch13-la-3",
          type: "subjective",
          question: "The mean and standard deviation of $100$ observations were calculated as $40$ and $5.1$, respectively, by a student who took by mistake $50$ instead of $40$ for one observation. What are the correct mean and standard deviation?",
          solutionSteps: [
            "Given $n = 100, \\bar{x} = 40, \\sigma = 5.1$.",
            "Incorrect sum $\\sum x_i = 100 \\times 40 = 4000$.",
            "Correct sum $\\sum x'_i = 4000 - 50 + 40 = 3990$.",
            "Correct mean $\\bar{x}' = \\frac{3990}{100} = 39.9$.",
            "Incorrect $\\sigma^2 = (5.1)^2 = 26.01$.",
            "$\\frac{\\sum x_i^2}{100} - (40)^2 = 26.01 \\implies \\sum x_i^2 = 100(1600 + 26.01) = 162,601$.",
            "Correct sum of squares $\\sum (x'_i)^2 = 162601 - 50^2 + 40^2 = 162601 - 2500 + 1600 = 161,701$.",
            "Correct variance $\\sigma'^2 = \\frac{161701}{100} - (39.9)^2 = 1617.01 - 1592.01 = 25$.",
            "Correct standard deviation $\\sigma' = \\sqrt{25} = 5$."
          ],
          answer: "Correct Mean $= 39.9$, Correct S.D. $= 5$"
        },
        {
          id: "exemplar-11-ch13-la-4",
          type: "subjective",
          question: "Two samples of sizes $n_1 = 50$ and $n_2 = 100$ have means $\\bar{x}_1 = 54.1$ and $\\bar{x}_2 = 50.3$ and standard deviations $\\sigma_1 = 8$ and $\\sigma_2 = 7$, respectively. Find the mean and standard deviation of the combined sample of size $150$.",
          solutionSteps: [
            "Combined Mean $\\bar{x} = \\frac{n_1 \\bar{x}_1 + n_2 \\bar{x}_2}{n_1 + n_2} = \\frac{50(54.1) + 100(50.3)}{150} = \\frac{2705 + 5030}{150} = \\frac{7735}{150} \\approx 51.57$.",
            "Deviations of individual means from combined mean:",
            "$d_1 = \\bar{x}_1 - \\bar{x} = 54.1 - 51.57 = 2.53$.",
            "$d_2 = \\bar{x}_2 - \\bar{x} = 50.3 - 51.57 = -1.27$.",
            "Combined Variance formula: $\\sigma^2 = \\frac{n_1(\\sigma_1^2 + d_1^2) + n_2(\\sigma_2^2 + d_2^2)}{n_1 + n_2}$.",
            "$\\sigma_1^2 + d_1^2 = 64 + (2.53)^2 = 64 + 6.4009 = 70.4009$.",
            "$\\sigma_2^2 + d_2^2 = 49 + (-1.27)^2 = 49 + 1.6129 = 50.6129$.",
            "Numerator $= 50(70.4009) + 100(50.6129) = 3520.045 + 5061.29 = 8581.335$.",
            "$\\sigma^2 = \\frac{8581.335}{150} \\approx 57.21$.",
            "Combined standard deviation $\\sigma = \\sqrt{57.21} \\approx 7.56$."
          ],
          answer: "Combined Mean $\\approx 51.57$, Combined S.D. $\\approx 7.56$"
        },
        {
          id: "exemplar-11-ch13-la-5",
          type: "subjective",
          question: "Find the mean, variance, and standard deviation of the continuous frequency distribution:<br>Diameter (mm): $33-36, 37-40, 41-44, 45-48, 49-52$;<br>Number of screws: $15, 17, 21, 22, 25$.",
          solutionSteps: [
            "Adjusting classes to continuous intervals: $32.5-36.5, 36.5-40.5, 40.5-44.5, 44.5-48.5, 48.5-52.5$.",
            "Class width $h = 4$. Mid-points $x_i$: $34.5, 38.5, 42.5, 46.5, 50.5$.",
            "Assumed mean $A = 42.5$. $u_i = \\frac{x_i - 42.5}{4}$: $-2, -1, 0, 1, 2$.",
            "Frequencies $f_i$: $15, 17, 21, 22, 25$. $N = 100$.",
            "$f_i u_i$: $15(-2) = -30, 17(-1) = -17, 21(0) = 0, 22(1) = 22, 25(2) = 50$.",
            "$\\sum f_i u_i = -47 + 72 = 25$.",
            "$f_i u_i^2$: $15(4) = 60, 17(1) = 17, 21(0) = 0, 22(1) = 22, 25(4) = 100$.",
            "$\\sum f_i u_i^2 = 60 + 17 + 0 + 22 + 100 = 199$.",
            "Mean $\\bar{x} = 42.5 + \\left(\\frac{25}{100}\\right)4 = 42.5 + 1 = 43.5\\text{ mm}$.",
            "Variance $\\sigma^2 = 4^2 \\left[\\frac{199}{100} - \\left(\\frac{25}{100}\\right)^2\\right] = 16 [1.99 - 0.0625] = 16(1.9275) = 30.84$.",
            "Standard deviation $\\sigma = \\sqrt{30.84} \\approx 5.55\\text{ mm}$."
          ],
          answer: "Mean $= 43.5\\text{ mm}$, Variance $= 30.84$, S.D. $\\approx 5.55\\text{ mm}$"
        },
        {
          id: "exemplar-11-ch13-la-6",
          type: "subjective",
          question: "If $\\bar{x}$ is the mean and $\\sigma^2$ is the variance of $n$ observations $x_1, x_2, \\dots, x_n$, prove that the variance of $ax_1, ax_2, \\dots, ax_n$ is $a^2\\sigma^2$, and hence find the variance of $5, 10, 15, 20, 25$.",
          solutionSteps: [
            "Let $y_i = ax_i$. Then $\\bar{y} = \\frac{1}{n}\\sum ax_i = a\\bar{x}$.",
            "Variance of $y$: $\\sigma_y^2 = \\frac{1}{n}\\sum (y_i - \\bar{y})^2 = \\frac{1}{n}\\sum (ax_i - a\\bar{x})^2 = \\frac{a^2}{n}\\sum (x_i - \\bar{x})^2 = a^2 \\sigma_x^2$.",
            "To find variance of $5, 10, 15, 20, 25$, write as $5 \\times (1, 2, 3, 4, 5)$.",
            "Here $a = 5$ and $x_i = 1, 2, 3, 4, 5$ ($n = 5$).",
            "Variance of first $5$ natural numbers $\\sigma^2 = \\frac{n^2 - 1}{12} = \\frac{25 - 1}{12} = \\frac{24}{12} = 2$.",
            "Therefore, required variance $= a^2 \\sigma^2 = 5^2 \\times 2 = 25 \\times 2 = 50$."
          ],
          answer: "Variance $= 50$"
        },
        {
          id: "exemplar-11-ch13-la-7",
          type: "subjective",
          question: "The frequencies of two series $X$ and $Y$ with the same mean $25$ are given. Series $X$ has standard deviation $\\sigma_X = 4.2$ and Series $Y$ has $\\sigma_Y = 5.6$. Which series is more dispersed? Justify algebraically using the coefficient of variation.",
          solutionSteps: [
            "Both distributions have identical arithmetic means: $\\bar{x}_X = \\bar{x}_Y = 25$.",
            "Coefficient of Variation is given by $\\text{C.V.} = \\frac{\\sigma}{\\bar{x}} \\times 100$.",
            "$\\text{C.V.}_X = \\frac{\\sigma_X}{\\bar{x}_X} \\times 100 = \\frac{4.2}{25} \\times 100 = 4.2 \\times 4 = 16.8\\%$.",
            "$\\text{C.V.}_Y = \\frac{\\sigma_Y}{\\bar{x}_Y} \\times 100 = \\frac{5.6}{25} \\times 100 = 5.6 \\times 4 = 22.4\\%$.",
            "Since $\\text{C.V.}_Y > \\text{C.V.}_X$, Series $Y$ has a higher relative dispersion and greater variability.",
            "Hence, Series $Y$ is more dispersed, while Series $X$ is more stable and consistent."
          ],
          answer: "Series $Y$ is more dispersed ($\text{C.V.} = 22.4\\%$ vs $16.8\\%$)"
        },
        {
          id: "exemplar-11-ch13-la-8",
          type: "subjective",
          question: "Calculate the mean deviation about the mean for the continuous grouped distribution:<br>Age (years): $10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80$;<br>Number of persons: $4, 8, 10, 16, 12, 6, 4$.",
          solutionSteps: [
            "Mid-points $x_i$: $15, 25, 35, 45, 55, 65, 75$.",
            "Frequencies $f_i$: $4, 8, 10, 16, 12, 6, 4$. Total $N = 60$.",
            "$f_i x_i$: $4(15) = 60, 8(25) = 200, 10(35) = 350, 16(45) = 720, 12(55) = 660, 6(65) = 390, 4(75) = 300$.",
            "$\\sum f_i x_i = 60 + 200 + 350 + 720 + 660 + 390 + 300 = 2680$.",
            "Mean $\\bar{x} = \\frac{2680}{60} = \\frac{134}{3} \\approx 44.67$.",
            "Deviations $|x_i - \\bar{x}|$: $|15 - 44.67| = 29.67, |25 - 44.67| = 19.67, |35 - 44.67| = 9.67, |45 - 44.67| = 0.33, |55 - 44.67| = 10.33, |65 - 44.67| = 20.33, |75 - 44.67| = 30.33$.",
            "$\\sum f_i |x_i - \\bar{x}| = 4(29.67) + 8(19.67) + 10(9.67) + 16(0.33) + 12(10.33) + 6(20.33) + 4(30.33)$",
            "$= 118.68 + 157.36 + 96.70 + 5.28 + 123.96 + 121.98 + 121.32 = 745.28$.",
            "$MD(\\bar{x}) = \\frac{745.28}{60} \\approx 12.42$ years."
          ],
          answer: "Mean $= 44.67$ years, $MD(\\bar{x}) \\approx 12.42$ years"
        }
      ]
    }
  ]
};
