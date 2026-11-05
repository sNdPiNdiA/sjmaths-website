// Data for Chapter 9: Straight Lines
module.exports = {
  chapterNum: 9,
  chapterName: "Straight Lines",
  chapterSlug: "chapter-9-straight-lines",
  exercises: [
    {
      exNum: 1,
      title: "Objective Type Questions (MCQs)",
      sectionLetter: "Q",
      prevUrl: "../",
      prevText: "← Chapter Index",
      nextUrl: "exemplar-9-2.html",
      nextText: "Exercise 9.2 →",
      questions: [
        {
          id: "exemplar-11-ch9-1",
          type: "mcq",
          question: "If the line $\\frac{x}{a} + \\frac{y}{b} = 1$ passes through the points $(2, -3)$ and $(4, -5)$, then $(a, b)$ is",
          options: [
            "(a) $(1, 1)$",
            "(b) $(-1, 1)$",
            "(c) $(1, -1)$",
            "(d) $(-1, -1)$"
          ],
          solutionSteps: [
            "Substituting $(2, -3)$ into the equation: $\\frac{2}{a} - \\frac{3}{b} = 1$.",
            "Substituting $(4, -5)$ into the equation: $\\frac{4}{a} - \\frac{5}{b} = 1$.",
            "Multiplying the first equation by $2$: $\\frac{4}{a} - \\frac{6}{b} = 2$.",
            "Subtracting this from the second equation: $-\\frac{5}{b} - \\left(-\\frac{6}{b}\\right) = 1 - 2 \\implies \\frac{1}{b} = -1 \\implies b = -1$.",
            "Substitute $b = -1$ into the first equation: $\\frac{2}{a} + 3 = 1 \\implies \\frac{2}{a} = -2 \\implies a = -1$.",
            "Hence, $(a, b) = (-1, -1)$."
          ],
          answer: "(d)"
        },
        {
          id: "exemplar-11-ch9-2",
          type: "mcq",
          question: "The distance of the point $(2, 3)$ from the line $2x - 3y + 9 = 0$ measured along the line $x - y + 1 = 0$ is",
          options: [
            "(a) $\\sqrt{2}$",
            "(b) $2\\sqrt{2}$",
            "(c) $3\\sqrt{2}$",
            "(d) $4\\sqrt{2}$"
          ],
          solutionSteps: [
            "The direction of measurement is parallel to $x - y + 1 = 0$, whose slope is $m = 1$.",
            "Equation of the line passing through $P(2, 3)$ with slope $m = 1$: $y - 3 = 1(x - 2) \\implies x - y + 1 = 0$.",
            "Find the point of intersection $Q$ of $x - y + 1 = 0$ and $2x - 3y + 9 = 0$.",
            "From $x - y + 1 = 0$, $y = x + 1$. Substitute into $2x - 3y + 9 = 0$: $2x - 3(x + 1) + 9 = 0 \\implies -x + 6 = 0 \\implies x = 6, y = 7$.",
            "Point of intersection is $Q(6, 7)$.",
            "Distance $PQ = \\sqrt{(6 - 2)^2 + (7 - 3)^2} = \\sqrt{16 + 16} = \\sqrt{32} = 4\\sqrt{2}$."
          ],
          answer: "(d)"
        },
        {
          id: "exemplar-11-ch9-3",
          type: "mcq",
          question: "A line passes through $P(1, 2)$ such that its intercept between the axes is bisected at $P$. The equation of the line is",
          options: [
            "(a) $x + 2y = 5$",
            "(b) $x - y + 1 = 0$",
            "(c) $2x + y - 4 = 0$",
            "(d) $2x - y = 0$"
          ],
          solutionSteps: [
            "Let the line intercept the coordinate axes at $A(a, 0)$ and $B(0, b)$.",
            "Since $P(1, 2)$ is the midpoint of $AB$, we have $\\frac{a + 0}{2} = 1 \\implies a = 2$.",
            "And $\\frac{0 + b}{2} = 2 \\implies b = 4$.",
            "Using the intercept form $\\frac{x}{a} + \\frac{y}{b} = 1$: $\\frac{x}{2} + \\frac{y}{4} = 1$.",
            "Multiplying by $4$: $2x + y = 4 \\implies 2x + y - 4 = 0$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch9-4",
          type: "mcq",
          question: "The inclination of the line $x - y + 3 = 0$ with the positive direction of the $x$-axis is",
          options: [
            "(a) $45^\\circ$",
            "(b) $135^\\circ$",
            "(c) $60^\\circ$",
            "(d) $30^\\circ$"
          ],
          solutionSteps: [
            "Convert $x - y + 3 = 0$ into slope-intercept form: $y = x + 3$.",
            "The slope of the line is $m = 1$.",
            "Since $m = \\tan\\theta$, $\\tan\\theta = 1 \\implies \\theta = 45^\\circ$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-5",
          type: "mcq",
          question: "If the lines $3x + 4y - 9 = 0$ and $6x + 8y + 15 = 0$ are tangents to the same circle, then the radius of the circle is",
          options: [
            "(a) $\\frac{33}{10}$",
            "(b) $\\frac{33}{20}$",
            "(c) $\\frac{33}{40}$",
            "(d) $\\frac{11}{20}$"
          ],
          solutionSteps: [
            "Rewrite the first equation by multiplying by $2$: $6x + 8y - 18 = 0$.",
            "The two given lines are parallel, so the distance between them is the diameter $2r$ of the circle.",
            "Distance $2r = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}} = \\frac{|15 - (-18)|}{\\sqrt{6^2 + 8^2}} = \\frac{33}{\\sqrt{100}} = \\frac{33}{10}$.",
            "Therefore, the radius $r = \\frac{1}{2} \\times \\frac{33}{10} = \\frac{33}{20}$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch9-6",
          type: "mcq",
          question: "If $p$ is the length of perpendicular from the origin on the line $\\frac{x}{a} + \\frac{y}{b} = 1$ and $a^2, p^2, b^2$ are in A.P., then $a^2 + b^2$ is equal to",
          options: [
            "(a) $ab$",
            "(b) $2ab$",
            "(c) $a^2 b^2$",
            "(d) none of these"
          ],
          solutionSteps: [
            "The perpendicular distance from origin $(0, 0)$ to $\\frac{x}{a} + \\frac{y}{b} - 1 = 0$ is $p = \\frac{1}{\\sqrt{\\frac{1}{a^2} + \\frac{1}{b^2}}}$.",
            "Squaring and inverting: $\\frac{1}{p^2} = \\frac{1}{a^2} + \\frac{1}{b^2} = \\frac{a^2 + b^2}{a^2 b^2}$.",
            "Since $a^2, p^2, b^2$ are in A.P., $2p^2 = a^2 + b^2 \\implies p^2 = \\frac{a^2 + b^2}{2}$.",
            "Substituting $p^2$: $\\frac{2}{a^2 + b^2} = \\frac{a^2 + b^2}{a^2 b^2} \\implies (a^2 + b^2)^2 = 2a^2 b^2 \\implies a^2 + b^2 = \\sqrt{2}ab$.",
            "Thus, $a^2 + b^2$ is not equal to $ab$, $2ab$, or $a^2 b^2$."
          ],
          answer: "(d)"
        },
        {
          id: "exemplar-11-ch9-7",
          type: "mcq",
          question: "The equations of the lines passing through $(1, 2)$ and making an angle of $45^\\circ$ with the line $2x + 3y = 10$ are",
          options: [
            "(a) $5x - y = 3$ and $x + 5y = 11$",
            "(b) $5x + y = 7$ and $x - 5y = -9$",
            "(c) $x - 5y = 3$ and $5x - y = 11$",
            "(d) none of these"
          ],
          solutionSteps: [
            "Slope of $2x + 3y = 10$ is $m_1 = -\\frac{2}{3}$.",
            "Let the required slope be $m$. Then $\\tan 45^\\circ = \\left|\\frac{m - (-2/3)}{1 + m(-2/3)}\\right| = 1$.",
            "$\\frac{3m + 2}{3 - 2m} = \\pm 1$.",
            "Taking positive sign: $3m + 2 = 3 - 2m \\implies 5m = 1 \\implies m = \\frac{1}{5}$. Line: $y - 2 = \\frac{1}{5}(x - 1) \\implies x - 5y = -9$.",
            "Taking negative sign: $3m + 2 = -(3 - 2m) \\implies 3m + 2 = -3 + 2m \\implies m = -5$. Line: $y - 2 = -5(x - 1) \\implies 5x + y = 7$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch9-8",
          type: "mcq",
          question: "The image of the point $(3, 8)$ with respect to the line $x + 3y = 7$ assuming the line to be a plane mirror is",
          options: [
            "(a) $(-1, -4)$",
            "(b) $(-1, 4)$",
            "(c) $(1, -4)$",
            "(d) $(2, -5)$"
          ],
          solutionSteps: [
            "Let the image of $(x_1, y_1) = (3, 8)$ in $ax + by + c = 0$ ($x + 3y - 7 = 0$) be $(x, y)$.",
            "Using the reflection formula: $\\frac{x - x_1}{a} = \\frac{y - y_1}{b} = \\frac{-2(ax_1 + by_1 + c)}{a^2 + b^2}$.",
            "$\\frac{x - 3}{1} = \\frac{y - 8}{3} = \\frac{-2(1(3) + 3(8) - 7)}{1^2 + 3^2} = \\frac{-2(20)}{10} = -4$.",
            "$x - 3 = 1(-4) \\implies x = -1$.",
            "$y - 8 = 3(-4) \\implies y = -4$.",
            "The image point is $(-1, -4)$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-9",
          type: "mcq",
          question: "The acute angle between the lines $y = (2 - \\sqrt{3})x + 5$ and $y = (2 + \\sqrt{3})x - 7$ is",
          options: [
            "(a) $30^\\circ$",
            "(b) $45^\\circ$",
            "(c) $60^\\circ$",
            "(d) $90^\\circ$"
          ],
          solutionSteps: [
            "Here $m_1 = 2 - \\sqrt{3} = \\tan 15^\\circ$ and $m_2 = 2 + \\sqrt{3} = \\tan 75^\\circ$.",
            "Angle $\\theta = 75^\\circ - 15^\\circ = 60^\\circ$.",
            "Alternatively: $\\tan\\theta = \\left|\\frac{(2+\\sqrt{3}) - (2-\\sqrt{3})}{1 + (2+\\sqrt{3})(2-\\sqrt{3})}\\right| = \\left|\\frac{2\\sqrt{3}}{1 + (4-3)}\\right| = \\frac{2\\sqrt{3}}{2} = \\sqrt{3}$.",
            "$\\tan\\theta = \\sqrt{3} \\implies \\theta = 60^\\circ$."
          ],
          answer: "(c)"
        },
        {
          id: "exemplar-11-ch9-10",
          type: "mcq",
          question: "The coordinates of the foot of the perpendicular drawn from the point $(2, 3)$ on the line $3x - y + 4 = 0$ is",
          options: [
            "(a) $\\left(-\\frac{1}{10}, \\frac{37}{10}\\right)$",
            "(b) $\\left(\\frac{1}{10}, \\frac{37}{10}\\right)$",
            "(c) $\\left(-\\frac{1}{10}, -\\frac{37}{10}\\right)$",
            "(d) $\\left(\\frac{2}{5}, \\frac{16}{5}\\right)$"
          ],
          solutionSteps: [
            "Let the foot of perpendicular be $(h, k)$ from $(x_1, y_1) = (2, 3)$ on $3x - y + 4 = 0$.",
            "Using the formula: $\\frac{h - x_1}{a} = \\frac{k - y_1}{b} = -\\frac{ax_1 + by_1 + c}{a^2 + b^2}$.",
            "$\\frac{h - 2}{3} = \\frac{k - 3}{-1} = -\\frac{3(2) - 1(3) + 4}{3^2 + (-1)^2} = -\\frac{7}{10}$.",
            "$h - 2 = 3\\left(-\\frac{7}{10}\\right) = -\\frac{21}{10} \\implies h = 2 - \\frac{21}{10} = -\\frac{1}{10}$.",
            "$k - 3 = -1\\left(-\\frac{7}{10}\\right) = \\frac{7}{10} \\implies k = 3 + \\frac{7}{10} = \\frac{37}{10}$.",
            "Foot of the perpendicular is $\\left(-\\frac{1}{10}, \\frac{37}{10}\\right)$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-11",
          type: "mcq",
          question: "If the lines $2x + y - 3 = 0$, $5x + ky - 3 = 0$ and $3x - y - 2 = 0$ are concurrent, then the value of $k$ is",
          options: [
            "(a) $-2$",
            "(b) $3$",
            "(c) $-1$",
            "(d) $2$"
          ],
          solutionSteps: [
            "Solve the first and third lines for their intersection point:",
            "$2x + y = 3$ and $3x - y = 2$.",
            "Adding the two equations: $5x = 5 \\implies x = 1$.",
            "Substitute $x = 1$ into $2x + y = 3$: $2(1) + y = 3 \\implies y = 1$.",
            "Point of intersection is $(1, 1)$.",
            "Since the three lines are concurrent, $(1, 1)$ must satisfy $5x + ky - 3 = 0$:",
            "$5(1) + k(1) - 3 = 0 \\implies k + 2 = 0 \\implies k = -2$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-12",
          type: "mcq",
          question: "The equation of the line passing through $(-3, 5)$ and perpendicular to the line joining $(2, 5)$ and $(-3, 6)$ is",
          options: [
            "(a) $5x - y + 20 = 0$",
            "(b) $5x + y + 10 = 0$",
            "(c) $x - 5y + 28 = 0$",
            "(d) $5x - y - 20 = 0$"
          ],
          solutionSteps: [
            "Slope of the line joining $(2, 5)$ and $(-3, 6)$: $m_1 = \\frac{6 - 5}{-3 - 2} = -\\frac{1}{5}$.",
            "Slope of perpendicular line is $m = -\\frac{1}{m_1} = 5$.",
            "Equation of line through $(-3, 5)$ with slope $m = 5$: $y - 5 = 5(x - (-3))$.",
            "$y - 5 = 5x + 15 \\implies 5x - y + 20 = 0$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-13",
          type: "mcq",
          question: "The points $(a, 0)$, $(0, b)$ and $(1, 1)$ are collinear if",
          options: [
            "(a) $\\frac{1}{a} + \\frac{1}{b} = 1$",
            "(b) $\\frac{1}{a} - \\frac{1}{b} = 1$",
            "(c) $\\frac{1}{a} + \\frac{1}{b} = 0$",
            "(d) $a + b = 1$"
          ],
          solutionSteps: [
            "Points $A(a, 0)$, $B(0, b)$, and $C(1, 1)$ are collinear if $\\text{Slope of } AB = \\text{Slope of } BC$.",
            "$\\text{Slope of } AB = \\frac{b - 0}{0 - a} = -\\frac{b}{a}$.",
            "$\\text{Slope of } BC = \\frac{1 - b}{1 - 0} = 1 - b$.",
            "Equating: $-\\frac{b}{a} = 1 - b \\implies -b = a(1 - b) \\implies -b = a - ab \\implies a + b = ab$.",
            "Dividing both sides by $ab$: $\\frac{1}{b} + \\frac{1}{a} = 1 \\implies \\frac{1}{a} + \\frac{1}{b} = 1$."
          ],
          answer: "(a)"
        },
        {
          id: "exemplar-11-ch9-14",
          type: "mcq",
          question: "The distance between the parallel lines $9x + 6y - 7 = 0$ and $3x + 2y + 6 = 0$ is",
          options: [
            "(a) $\\frac{19}{2\\sqrt{13}}$",
            "(b) $\\frac{25}{3\\sqrt{13}}$",
            "(c) $\\frac{25}{\\sqrt{13}}$",
            "(d) $\\frac{5}{\\sqrt{13}}$"
          ],
          solutionSteps: [
            "Multiply the second equation by $3$ to align coefficients: $9x + 6y + 18 = 0$.",
            "The lines are $9x + 6y - 7 = 0$ ($C_1 = -7$) and $9x + 6y + 18 = 0$ ($C_2 = 18$).",
            "Distance $d = \\frac{|C_2 - C_1|}{\\sqrt{A^2 + B^2}} = \\frac{|18 - (-7)|}{\\sqrt{9^2 + 6^2}} = \\frac{25}{\\sqrt{81 + 36}} = \\frac{25}{\\sqrt{117}}$.",
            "Since $\\sqrt{117} = 3\\sqrt{13}$, $d = \\frac{25}{3\\sqrt{13}}$."
          ],
          answer: "(b)"
        },
        {
          id: "exemplar-11-ch9-15",
          type: "mcq",
          question: "The area of the triangle formed by the lines $y = 0$, $x = 0$ and $3x + 4y = 12$ is",
          options: [
            "(a) $6$ sq units",
            "(b) $12$ sq units",
            "(c) $24$ sq units",
            "(d) $3$ sq units"
          ],
          solutionSteps: [
            "The line $3x + 4y = 12$ meets the $x$-axis ($y = 0$) at $(4, 0)$.",
            "It meets the $y$-axis ($x = 0$) at $(0, 3)$.",
            "The vertices of the triangle are $(0, 0)$, $(4, 0)$, and $(0, 3)$.",
            "The triangle is right-angled at origin with base $4$ and height $3$.",
            "$\\text{Area} = \\frac{1}{2} \\times 4 \\times 3 = 6$ sq units."
          ],
          answer: "(a)"
        }
      ]
    },
    {
      exNum: 2,
      title: "Short Answer Type Questions",
      sectionLetter: "S",
      prevUrl: "exemplar-9-1.html",
      prevText: "← Exercise 9.1",
      nextUrl: "exemplar-9-3.html",
      nextText: "Exercise 9.3 →",
      questions: [
        {
          id: "exemplar-11-ch9-sa-1",
          type: "subjective",
          question: "Find the equation of the line which passes through the point $(2, 2\\sqrt{3})$ and makes an angle of $75^\\circ$ with the positive direction of the $x$-axis.",
          solutionSteps: [
            "Slope $m = \\tan 75^\\circ = \\tan(45^\\circ + 30^\\circ) = \\frac{\\tan 45^\\circ + \\tan 30^\\circ}{1 - \\tan 45^\\circ\\tan 30^\\circ} = \\frac{1 + 1/\\sqrt{3}}{1 - 1/\\sqrt{3}} = \\frac{\\sqrt{3}+1}{\\sqrt{3}-1} = 2 + \\sqrt{3}$.",
            "Using point-slope form $y - y_1 = m(x - x_1)$ with $(x_1, y_1) = (2, 2\\sqrt{3})$:",
            "$y - 2\\sqrt{3} = (2 + \\sqrt{3})(x - 2)$.",
            "$y - 2\\sqrt{3} = (2 + \\sqrt{3})x - 4 - 2\\sqrt{3}$.",
            "$(2 + \\sqrt{3})x - y - 4 = 0$."
          ],
          answer: "$(2 + \\sqrt{3})x - y - 4 = 0$"
        },
        {
          id: "exemplar-11-ch9-sa-2",
          type: "subjective",
          question: "Find the equation of the line passing through $(-3, 5)$ and perpendicular to the line through $(2, 5)$ and $(-3, 6)$.",
          solutionSteps: [
            "Slope of line joining $(2, 5)$ and $(-3, 6)$ is $m_1 = \\frac{6 - 5}{-3 - 2} = -\\frac{1}{5}$.",
            "Slope of the perpendicular line is $m = -\\frac{1}{m_1} = 5$.",
            "Equation of line passing through $(-3, 5)$ with slope $m = 5$ is $y - 5 = 5(x - (-3))$.",
            "$y - 5 = 5x + 15 \\implies 5x - y + 20 = 0$."
          ],
          answer: "$5x - y + 20 = 0$"
        },
        {
          id: "exemplar-11-ch9-sa-3",
          type: "subjective",
          question: "Find the coordinates of the foot of the perpendicular from the point $(-1, 3)$ to the line $3x - 4y - 16 = 0$.",
          solutionSteps: [
            "Let foot of perpendicular be $(h, k)$ from $(x_1, y_1) = (-1, 3)$ on $3x - 4y - 16 = 0$.",
            "Formula: $\\frac{h - x_1}{a} = \\frac{k - y_1}{b} = -\\frac{ax_1 + by_1 + c}{a^2 + b^2}$.",
            "$\\frac{h - (-1)}{3} = \\frac{k - 3}{-4} = -\\frac{3(-1) - 4(3) - 16}{3^2 + (-4)^2} = -\\frac{-3 - 12 - 16}{25} = -\\frac{-31}{25} = \\frac{31}{25}$.",
            "$h + 1 = 3\\left(\\frac{31}{25}\\right) = \\frac{93}{25} \\implies h = \\frac{93}{25} - 1 = \\frac{68}{25}$.",
            "$k - 3 = -4\\left(\\frac{31}{25}\\right) = -\\frac{124}{25} \\implies k = 3 - \\frac{124}{25} = -\\frac{49}{25}$."
          ],
          answer: "$\\left(\\frac{68}{25}, -\\frac{49}{25}\\right)$"
        },
        {
          id: "exemplar-11-ch9-sa-4",
          type: "subjective",
          question: "Find the value of $k$ so that the line $2x + ky - 9 = 0$ may be perpendicular to the line $3x - 4y + 7 = 0$.",
          solutionSteps: [
            "Slope of $2x + ky - 9 = 0$ is $m_1 = -\\frac{2}{k}$.",
            "Slope of $3x - 4y + 7 = 0$ is $m_2 = \\frac{3}{4}$.",
            "Lines are perpendicular $\\iff m_1 m_2 = -1$.",
            "$\\left(-\\frac{2}{k}\\right)\\left(\\frac{3}{4}\\right) = -1 \\implies -\\frac{6}{4k} = -1 \\implies 4k = 6 \\implies k = \\frac{3}{2}$."
          ],
          answer: "$k = \\frac{3}{2}$"
        },
        {
          id: "exemplar-11-ch9-sa-5",
          type: "subjective",
          question: "Find the distance of the line $4x - y = 0$ from the point $P(4, 1)$ measured along the line making an angle of $135^\\circ$ with the positive direction of the $x$-axis.",
          solutionSteps: [
            "Slope of the line through $P(4, 1)$ is $m = \\tan 135^\\circ = -1$.",
            "Equation of this line: $y - 1 = -1(x - 4) \\implies x + y - 5 = 0 \\implies y = 5 - x$.",
            "Find the point of intersection $Q$ with $4x - y = 0$:",
            "$4x - (5 - x) = 0 \\implies 5x = 5 \\implies x = 1, y = 4$.",
            "Distance $PQ = \\sqrt{(4 - 1)^2 + (1 - 4)^2} = \\sqrt{9 + 9} = \\sqrt{18} = 3\\sqrt{2}$."
          ],
          answer: "$3\\sqrt{2}$"
        },
        {
          id: "exemplar-11-ch9-sa-6",
          type: "subjective",
          question: "Find the equation of the line whose perpendicular distance from the origin is $4$ units and the angle which the normal makes with the positive $x$-axis is $15^\\circ$.",
          solutionSteps: [
            "Using the normal form: $x\\cos\\alpha + y\\sin\\alpha = p$, where $p = 4$ and $\\alpha = 15^\\circ$.",
            "$\\cos 15^\\circ = \\frac{\\sqrt{3}+1}{2\\sqrt{2}}$, $\\sin 15^\\circ = \\frac{\\sqrt{3}-1}{2\\sqrt{2}}$.",
            "Substituting: $x\\left(\\frac{\\sqrt{3}+1}{2\\sqrt{2}}\\right) + y\\left(\\frac{\\sqrt{3}-1}{2\\sqrt{2}}\\right) = 4$.",
            "Multiplying by $2\\sqrt{2}$: $(\\sqrt{3}+1)x + (\\sqrt{3}-1)y = 8\\sqrt{2}$."
          ],
          answer: "$(\\sqrt{3}+1)x + (\\sqrt{3}-1)y = 8\\sqrt{2}$"
        },
        {
          id: "exemplar-11-ch9-sa-7",
          type: "subjective",
          question: "If the lines $ax + 2y + 1 = 0$, $bx + 3y + 1 = 0$ and $cx + 4y + 1 = 0$ are concurrent, prove that $a, b, c$ are in A.P.",
          solutionSteps: [
            "For three lines to be concurrent, the determinant of their coefficients must be zero:",
            "$\\begin{vmatrix} a & 2 & 1 \\\\ b & 3 & 1 \\\\ c & 4 & 1 \\end{vmatrix} = 0$.",
            "Apply elementary row operations $R_2 \\to R_2 - R_1$ and $R_3 \\to R_3 - R_2$:",
            "$\\begin{vmatrix} a & 2 & 1 \\\\ b - a & 1 & 0 \\\\ c - b & 1 & 0 \\end{vmatrix} = 0$.",
            "Expanding along the third column: $1 \\cdot ((b - a)(1) - (c - b)(1)) = 0$.",
            "$b - a - c + b = 0 \\implies 2b = a + c$.",
            "Hence, $a, b, c$ are in Arithmetic Progression (A.P.)."
          ],
          answer: "Hence proved that $a, b, c$ are in A.P."
        },
        {
          id: "exemplar-11-ch9-sa-8",
          type: "subjective",
          question: "Find the equation of the line passing through the intersection of $2x + 3y - 4 = 0$ and $x - 5y = 7$ that has $x$-intercept equal to $-4$.",
          solutionSteps: [
            "From $x - 5y = 7$, $x = 5y + 7$.",
            "Substitute into $2x + 3y - 4 = 0$: $2(5y + 7) + 3y - 4 = 0 \\implies 13y + 10 = 0 \\implies y = -\\frac{10}{13}$.",
            "$x = 5\\left(-\\frac{10}{13}\\right) + 7 = -\\frac{50}{13} + \\frac{91}{13} = \\frac{41}{13}$. Point of intersection is $\\left(\\frac{41}{13}, -\\frac{10}{13}\\right)$.",
            "The line passes through $(-4, 0)$ ($x$-intercept $-4$) and $\\left(\\frac{41}{13}, -\\frac{10}{13}\\right)$.",
            "Slope $m = \\frac{-10/13 - 0}{41/13 - (-4)} = \\frac{-10/13}{93/13} = -\\frac{10}{93}$.",
            "Equation: $y - 0 = -\\frac{10}{93}(x + 4) \\implies 93y = -10x - 40 \\implies 10x + 93y + 40 = 0$."
          ],
          answer: "$10x + 93y + 40 = 0$"
        },
        {
          id: "exemplar-11-ch9-sa-9",
          type: "subjective",
          question: "Find the acute angle between the lines $y - \\sqrt{3}x - 5 = 0$ and $\\sqrt{3}y - x + 6 = 0$.",
          solutionSteps: [
            "Rewrite $y - \\sqrt{3}x - 5 = 0 \\implies y = \\sqrt{3}x + 5$, so slope $m_1 = \\sqrt{3}$.",
            "Rewrite $\\sqrt{3}y - x + 6 = 0 \\implies y = \\frac{1}{\\sqrt{3}}x - \\frac{6}{\\sqrt{3}}$, so slope $m_2 = \\frac{1}{\\sqrt{3}}$.",
            "Using angle formula: $\\tan\\theta = \\left|\\frac{m_1 - m_2}{1 + m_1 m_2}\\right| = \\left|\\frac{\\sqrt{3} - 1/\\sqrt{3}}{1 + \\sqrt{3}(1/\\sqrt{3})}\\right|$.",
            "$\\tan\\theta = \\left|\\frac{2/\\sqrt{3}}{2}\\right| = \\frac{1}{\\sqrt{3}}$.",
            "Since $\\tan\\theta = \\frac{1}{\\sqrt{3}}$, the acute angle $\\theta = 30^\\circ$ (or $\\frac{\\pi}{6}$ radians)."
          ],
          answer: "$30^\\circ$ (or $\\frac{\\pi}{6}$)"
        },
        {
          id: "exemplar-11-ch9-sa-10",
          type: "subjective",
          question: "Find the value of $p$ so that the three lines $3x + y - 2 = 0$, $px + 2y - 3 = 0$ and $2x - y - 3 = 0$ may intersect at one point.",
          solutionSteps: [
            "Solve $3x + y = 2$ and $2x - y = 3$:",
            "Adding gives $5x = 5 \\implies x = 1$.",
            "Substitute $x = 1$ into $3(1) + y = 2 \\implies y = -1$. Point of concurrency is $(1, -1)$.",
            "Since the third line passes through $(1, -1)$: $p(1) + 2(-1) - 3 = 0$.",
            "$p - 2 - 3 = 0 \\implies p = 5$."
          ],
          answer: "$p = 5$"
        },
        {
          id: "exemplar-11-ch9-sa-11",
          type: "subjective",
          question: "If the intercept of a line between the coordinate axes is divided by the point $(-5, 4)$ in the ratio $1 : 2$, find the equation of the line.",
          solutionSteps: [
            "Let the intercepts on axes be $A(a, 0)$ and $B(0, b)$.",
            "Case 1: Ratio $1 : 2$ from $A$ to $B$:",
            "$-5 = \\frac{1(0) + 2(a)}{1 + 2} = \\frac{2a}{3} \\implies a = -\\frac{15}{2}$.",
            "$4 = \\frac{1(b) + 2(0)}{3} = \\frac{b}{3} \\implies b = 12$.",
            "Equation: $\\frac{x}{-15/2} + \\frac{y}{12} = 1 \\implies -\\frac{2x}{15} + \\frac{y}{12} = 1 \\implies 8x - 5y + 60 = 0$.",
            "Case 2: Ratio $2 : 1$ from $A$ to $B$:",
            "$-5 = \\frac{2(0) + 1(a)}{3} = \\frac{a}{3} \\implies a = -15$.",
            "$4 = \\frac{2(b) + 1(0)}{3} = \\frac{2b}{3} \\implies b = 6$.",
            "Equation: $\\frac{x}{-15} + \\frac{y}{6} = 1 \\implies 2x - 5y + 30 = 0$."
          ],
          answer: "$8x - 5y + 60 = 0$ or $2x - 5y + 30 = 0$"
        },
        {
          id: "exemplar-11-ch9-sa-12",
          type: "subjective",
          question: "Find the distance between the parallel lines $15x + 8y - 34 = 0$ and $15x + 8y + 31 = 0$.",
          solutionSteps: [
            "Distance between parallel lines $Ax + By + C_1 = 0$ and $Ax + By + C_2 = 0$ is $d = \\frac{|C_1 - C_2|}{\\sqrt{A^2 + B^2}}$.",
            "Here $A = 15, B = 8, C_1 = -34, C_2 = 31$.",
            "$d = \\frac{|31 - (-34)|}{\\sqrt{15^2 + 8^2}} = \\frac{65}{\\sqrt{225 + 64}} = \\frac{65}{\\sqrt{289}} = \\frac{65}{17}$ units."
          ],
          answer: "$\\frac{65}{17}$ units"
        },
        {
          id: "exemplar-11-ch9-sa-13",
          type: "subjective",
          question: "Find the area of the triangle formed by the line $x\\cos\\alpha + y\\sin\\alpha = p$ with the coordinate axes.",
          solutionSteps: [
            "For the $x$-intercept, put $y = 0$: $x\\cos\\alpha = p \\implies x = \\frac{p}{\\cos\\alpha}$.",
            "For the $y$-intercept, put $x = 0$: $y\\sin\\alpha = p \\implies y = \\frac{p}{\\sin\\alpha}$.",
            "The triangle formed by axes and line is right-angled at origin with legs $\\left|\\frac{p}{\\cos\\alpha}\\right|$ and $\\left|\\frac{p}{\\sin\\alpha}\\right|$.",
            "$\\text{Area} = \\frac{1}{2} \\left|\\frac{p}{\\cos\\alpha} \\cdot \\frac{p}{\\sin\\alpha}\\right| = \\frac{p^2}{2|\\sin\\alpha\\cos\\alpha|} = \\frac{p^2}{|\\sin 2\\alpha|}$ sq units."
          ],
          answer: "$\\frac{p^2}{|\\sin 2\\alpha|}$ sq units"
        },
        {
          id: "exemplar-11-ch9-sa-14",
          type: "subjective",
          question: "Find the coordinates of the image of the point $(1, 2)$ with respect to the line $x - 3y + 4 = 0$.",
          solutionSteps: [
            "Let the image of $(x_1, y_1) = (1, 2)$ in $x - 3y + 4 = 0$ be $(x, y)$.",
            "Formula: $\\frac{x - x_1}{a} = \\frac{y - y_1}{b} = \\frac{-2(ax_1 + by_1 + c)}{a^2 + b^2}$.",
            "$\\frac{x - 1}{1} = \\frac{y - 2}{-3} = \\frac{-2(1(1) - 3(2) + 4)}{1^2 + (-3)^2} = \\frac{-2(-1)}{10} = \\frac{2}{10} = \\frac{1}{5}$.",
            "$x - 1 = \\frac{1}{5} \\implies x = \\frac{6}{5}$.",
            "$y - 2 = -3\\left(\\frac{1}{5}\\right) = -\\frac{3}{5} \\implies y = \\frac{7}{5}$."
          ],
          answer: "$\\left(\\frac{6}{5}, \\frac{7}{5}\\right)$"
        },
        {
          id: "exemplar-11-ch9-sa-15",
          type: "subjective",
          question: "A line is such that its segment between the lines $5x - y + 4 = 0$ and $3x + 4y - 4 = 0$ is bisected at the point $(1, 5)$. Obtain its equation.",
          solutionSteps: [
            "Let the segment end points be $A(x_1, y_1)$ on $5x - y + 4 = 0$ and $B(x_2, y_2)$ on $3x + 4y - 4 = 0$.",
            "From line 1: $y_1 = 5x_1 + 4$.",
            "Since $(1, 5)$ is the midpoint: $x_2 = 2(1) - x_1 = 2 - x_1$ and $y_2 = 2(5) - y_1 = 10 - (5x_1 + 4) = 6 - 5x_1$.",
            "Since $B(x_2, y_2)$ lies on $3x + 4y - 4 = 0$:",
            "$3(2 - x_1) + 4(6 - 5x_1) - 4 = 0 \\implies 6 - 3x_1 + 24 - 20x_1 - 4 = 0 \\implies 26 - 23x_1 = 0 \\implies x_1 = \\frac{26}{23}$.",
            "Then $y_1 = 5\\left(\\frac{26}{23}\\right) + 4 = \\frac{222}{23}$.",
            "Slope $m = \\frac{222/23 - 5}{26/23 - 1} = \\frac{107/23}{3/23} = \\frac{107}{3}$.",
            "Equation through $(1, 5)$ with slope $\\frac{107}{3}$: $y - 5 = \\frac{107}{3}(x - 1) \\implies 107x - 3y - 92 = 0$."
          ],
          answer: "$107x - 3y - 92 = 0$"
        }
      ]
    },
    {
      exNum: 3,
      title: "Long Answer Type Questions",
      sectionLetter: "L",
      prevUrl: "exemplar-9-2.html",
      prevText: "← Exercise 9.2",
      nextUrl: "/class-11-maths/ncert-exemplar-practice/chapter-10-conic-sections/exemplar-10-1.html",
      nextText: "Chapter 10 →",
      questions: [
        {
          id: "exemplar-11-ch9-la-1",
          type: "subjective",
          question: "Find the coordinates of the orthocentre of the triangle whose vertices are $A(-1, 3)$, $B(2, -1)$, and $C(0, 0)$.",
          solutionSteps: [
            "Orthocentre is the point of intersection of altitudes of the triangle.",
            "Slope of $BC$: $m_{BC} = \\frac{-1 - 0}{2 - 0} = -\\frac{1}{2}$.",
            "Altitude from $A(-1, 3)$ is perpendicular to $BC$, so its slope is $m_A = 2$.",
            "Equation of altitude from $A$: $y - 3 = 2(x + 1) \\implies 2x - y + 5 = 0$.",
            "Slope of $AC$: $m_{AC} = \\frac{3 - 0}{-1 - 0} = -3$.",
            "Altitude from $B(2, -1)$ is perpendicular to $AC$, so its slope is $m_B = \\frac{1}{3}$.",
            "Equation of altitude from $B$: $y - (-1) = \\frac{1}{3}(x - 2) \\implies x - 3y - 5 = 0$.",
            "Solve $2x - y + 5 = 0$ and $x - 3y - 5 = 0$: from first equation $y = 2x + 5$.",
            "Substitute into second: $x - 3(2x + 5) - 5 = 0 \\implies -5x - 20 = 0 \\implies x = -4$.",
            "Then $y = 2(-4) + 5 = -3$.",
            "Orthocentre is $(-4, -3)$."
          ],
          answer: "$(-4, -3)$"
        },
        {
          id: "exemplar-11-ch9-la-2",
          type: "subjective",
          question: "If $p$ and $q$ are the lengths of perpendiculars from the origin to the lines $x\\cos\\theta - y\\sin\\theta = k\\cos 2\\theta$ and $x\\sec\\theta + y\\csc\\theta = k$, respectively, prove that $p^2 + 4q^2 = k^2$.",
          solutionSteps: [
            "Perpendicular distance $p$ from $(0, 0)$ to $x\\cos\\theta - y\\sin\\theta - k\\cos 2\\theta = 0$ is:",
            "$p = \\frac{|-k\\cos 2\\theta|}{\\sqrt{\\cos^2\\theta + \\sin^2\\theta}} = k|\\cos 2\\theta| \\implies p^2 = k^2\\cos^2 2\\theta$.",
            "The second line is $\\frac{x}{\\cos\\theta} + \\frac{y}{\\sin\\theta} = k \\implies x\\sin\\theta + y\\cos\\theta - k\\sin\\theta\\cos\\theta = 0$.",
            "Perpendicular distance $q$ from origin is:",
            "$q = \\frac{|-k\\sin\\theta\\cos\\theta|}{\\sqrt{\\sin^2\\theta + \\cos^2\\theta}} = k\\sin\\theta\\cos\\theta = \\frac{k}{2}\\sin 2\\theta$.",
            "$2q = k\\sin 2\\theta \\implies 4q^2 = k^2\\sin^2 2\\theta$.",
            "Adding $p^2 + 4q^2 = k^2\\cos^2 2\\theta + k^2\\sin^2 2\\theta = k^2(\\cos^2 2\\theta + \\sin^2 2\\theta) = k^2$."
          ],
          answer: "$p^2 + 4q^2 = k^2$ (Hence proved)"
        },
        {
          id: "exemplar-11-ch9-la-3",
          type: "subjective",
          question: "A ray of light passing through the point $(1, 2)$ reflects on the $x$-axis at point $A$ and the reflected ray passes through the point $(5, 3)$. Find the coordinates of $A$.",
          solutionSteps: [
            "Let $P = (1, 2)$ and $Q = (5, 3)$. The point of reflection is $A(x, 0)$ on the $x$-axis.",
            "By the laws of reflection, the angle of incidence equals the angle of reflection.",
            "The image of $P(1, 2)$ in the $x$-axis (line $y = 0$) is $P'(1, -2)$.",
            "The reflected ray appears to come from $P'$, so $P'$, $A$, and $Q$ are collinear.",
            "Slope of line $P'Q = \\frac{3 - (-2)}{5 - 1} = \\frac{5}{4}$.",
            "Equation of line $P'Q$: $y - 3 = \\frac{5}{4}(x - 5) \\implies 5x - 4y - 13 = 0$.",
            "Point $A$ is the $x$-intercept of line $P'Q$, so put $y = 0$:",
            "$5x - 13 = 0 \\implies x = \\frac{13}{5}$.",
            "Therefore, $A = \\left(\\frac{13}{5}, 0\\right)$."
          ],
          answer: "$\\left(\\frac{13}{5}, 0\\right)$"
        },
        {
          id: "exemplar-11-ch9-la-4",
          type: "subjective",
          question: "Find the equation of the line passing through the intersection of the lines $x + 2y - 3 = 0$ and $4x - y + 7 = 0$ and which is parallel to $5x + 4y - 20 = 0$.",
          solutionSteps: [
            "Solve the system $x + 2y = 3$ and $4x - y = -7$:",
            "Multiply second equation by $2$: $8x - 2y = -14$.",
            "Add to first: $9x = -11 \\implies x = -\\frac{11}{9}$.",
            "Substitute into first: $-\\frac{11}{9} + 2y = 3 \\implies 2y = \\frac{38}{9} \\implies y = \\frac{19}{9}$.",
            "Intersection point is $\\left(-\\frac{11}{9}, \\frac{19}{9}\\right)$.",
            "The required line is parallel to $5x + 4y - 20 = 0$, so its equation is $5x + 4y + k = 0$.",
            "Substitute the intersection point: $5\\left(-\\frac{11}{9}\\right) + 4\\left(\\frac{19}{9}\\right) + k = 0$.",
            "$\\frac{-55 + 76}{9} + k = 0 \\implies \\frac{21}{9} + k = 0 \\implies k = -\\frac{7}{3}$.",
            "Equation: $5x + 4y - \\frac{7}{3} = 0 \\implies 15x + 12y - 7 = 0$."
          ],
          answer: "$15x + 12y - 7 = 0$"
        },
        {
          id: "exemplar-11-ch9-la-5",
          type: "subjective",
          question: "Find the coordinates of the circumcentre of the triangle whose vertices are $A(1, 3)$, $B(-3, 5)$, and $C(5, -1)$.",
          solutionSteps: [
            "Let the circumcentre be $O(x, y)$. Since $O$ is equidistant from all vertices: $OA^2 = OB^2 = OC^2$.",
            "$OA^2 = (x - 1)^2 + (y - 3)^2 = x^2 + y^2 - 2x - 6y + 10$.",
            "$OB^2 = (x + 3)^2 + (y - 5)^2 = x^2 + y^2 + 6x - 10y + 34$.",
            "$OC^2 = (x - 5)^2 + (y + 1)^2 = x^2 + y^2 - 10x + 2y + 26$.",
            "From $OA^2 = OB^2$: $-2x - 6y + 10 = 6x - 10y + 34 \\implies 8x - 4y + 24 = 0 \\implies 2x - y + 6 = 0$.",
            "From $OA^2 = OC^2$: $-2x - 6y + 10 = -10x + 2y + 26 \\implies 8x - 8y - 16 = 0 \\implies x - y - 2 = 0$.",
            "Subtracting $(x - y - 2 = 0)$ from $(2x - y + 6 = 0)$: $x + 8 = 0 \\implies x = -8$.",
            "Then $-8 - y - 2 = 0 \\implies y = -10$.",
            "Circumcentre is $(-8, -10)$."
          ],
          answer: "$(-8, -10)$"
        },
        {
          id: "exemplar-11-ch9-la-6",
          type: "subjective",
          question: "If one diagonal of a square is along the line $8x - 15y = 0$ and one of its vertices is at $(1, 2)$, find the equations of the sides of the square passing through this vertex.",
          solutionSteps: [
            "The diagonal line $8x - 15y = 0$ does not pass through $(1, 2)$ because $8(1) - 15(2) = -22 \\ne 0$.",
            "In a square, the sides make an angle of $45^\\circ$ with either diagonal.",
            "Slope of the diagonal $8x - 15y = 0$ is $m_1 = \\frac{8}{15}$.",
            "Let $m$ be the slope of a side: $\\tan 45^\\circ = \\left|\\frac{m - 8/15}{1 + 8m/15}\\right| = 1$.",
            "$\\frac{15m - 8}{15 + 8m} = \\pm 1$.",
            "Case 1: $15m - 8 = 15 + 8m \\implies 7m = 23 \\implies m = \\frac{23}{7}$.",
            "Equation of side through $(1, 2)$: $y - 2 = \\frac{23}{7}(x - 1) \\implies 23x - 7y - 9 = 0$.",
            "Case 2: $15m - 8 = -(15 + 8m) \\implies 23m = -7 \\implies m = -\\frac{7}{23}$.",
            "Equation of side through $(1, 2)$: $y - 2 = -\\frac{7}{23}(x - 1) \\implies 7x + 23y - 53 = 0$."
          ],
          answer: "$23x - 7y - 9 = 0$ and $7x + 23y - 53 = 0$"
        },
        {
          id: "exemplar-11-ch9-la-7",
          type: "subjective",
          question: "Find the equations of the lines which pass through the point $(4, 5)$ and make equal angles with the lines $5x - 12y + 6 = 0$ and $3x = 4y - 7$.",
          solutionSteps: [
            "Rewrite lines: $L_1: 5x - 12y + 6 = 0$ (slope $m_1 = \\frac{5}{12}$) and $L_2: 3x - 4y + 7 = 0$ (slope $m_2 = \\frac{3}{4}$).",
            "A line making equal angles with $L_1$ and $L_2$ is parallel to one of the angle bisectors of $L_1$ and $L_2$.",
            "Equations of angle bisectors: $\\frac{5x - 12y + 6}{\\sqrt{25 + 144}} = \\pm \\frac{3x - 4y + 7}{\\sqrt{9 + 16}}$.",
            "$\\frac{5x - 12y + 6}{13} = \\pm \\frac{3x - 4y + 7}{5}$.",
            "Taking $(+)$: $25x - 60y + 30 = 39x - 52y + 91 \\implies 14x + 8y + 61 = 0$ (slope $M_1 = -\\frac{7}{4}$).",
            "Taking $(-)$: $25x - 60y + 30 = -39x + 52y - 91 \\implies 64x - 112y + 121 = 0$ (slope $M_2 = \\frac{4}{7}$).",
            "Line with slope $-\\frac{7}{4}$ through $(4, 5)$: $y - 5 = -\\frac{7}{4}(x - 4) \\implies 7x + 4y - 48 = 0$.",
            "Line with slope $\\frac{4}{7}$ through $(4, 5)$: $y - 5 = \\frac{4}{7}(x - 4) \\implies 4x - 7y + 19 = 0$."
          ],
          answer: "$7x + 4y - 48 = 0$ and $4x - 7y + 19 = 0$"
        },
        {
          id: "exemplar-11-ch9-la-8",
          type: "subjective",
          question: "A variable line passes through the fixed point $(a, b)$ and meets the coordinate axes in $A$ and $B$. Show that the locus of the point of intersection of lines drawn through $A$ parallel to $y$-axis and through $B$ parallel to $x$-axis is $\\frac{a}{x} + \\frac{b}{y} = 1$.",
          solutionSteps: [
            "Let the equation of the variable line in intercept form be $\\frac{x}{h_1} + \\frac{y}{k_1} = 1$.",
            "It meets the $x$-axis at $A(h_1, 0)$ and the $y$-axis at $B(0, k_1)$.",
            "Line through $A$ parallel to $y$-axis is $x = h_1$.",
            "Line through $B$ parallel to $x$-axis is $y = k_1$.",
            "Let their point of intersection be $P(x, y)$, then $x = h_1$ and $y = k_1$.",
            "Since the variable line passes through the fixed point $(a, b)$:",
            "$\\frac{a}{h_1} + \\frac{b}{k_1} = 1$.",
            "Substituting $h_1 = x$ and $k_1 = y$, we obtain the required locus:",
            "$\\frac{a}{x} + \\frac{b}{y} = 1$."
          ],
          answer: "$\\frac{a}{x} + \\frac{b}{y} = 1$ (Hence proved)"
        }
      ]
    }
  ]
};
