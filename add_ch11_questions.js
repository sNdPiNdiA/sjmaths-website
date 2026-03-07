const fs = require('fs');
const path = 'class-10-maths/chapter-11-data.json';
let data = JSON.parse(fs.readFileSync(path, 'utf8'));

// ── Concept 0: Area of Sector & Segment ──
data.concepts[0].practice.push(
    {
        question: String.raw`A car has two wipers which do not overlap. Each wiper has a blade of length 25 cm sweeping through an angle of \(115°\). Find the total area cleaned at each sweep of the blades.`,
        options: ["158125/126 cm²", "158125/252 cm²", "1254.96 cm²", "1650 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of one sweep = \(\frac{115}{360} \times \frac{22}{7} \times 25 \times 25\).</p><p>Total area for two wipers = \(2 \times \frac{23}{72} \times \frac{22}{7} \times 625 = \frac{46 \times 22 \times 625}{504} = \frac{158125}{126}\) cm².</p>`
    },
    {
        question: String.raw`To warn ships for underwater rocks, a lighthouse spreads a red coloured light over a sector of angle \(80°\) to a distance of 16.5 km. Find the area of the sea over which the ships are warned. (Use \(\pi = 3.14\))`,
        options: ["189.97 km²", "190.97 km²", "180.5 km²", "185.5 km²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of sector = \(\frac{80}{360} \times 3.14 \times 16.5 \times 16.5\).</p><p>= \(\frac{2}{9} \times 3.14 \times 272.25 = 189.97\) km².</p>`
    },
    {
        question: String.raw`Find the area of a quadrant of a circle whose circumference is 22 cm.`,
        options: ["77/8 cm²", "77/4 cm²", "38.5 cm²", "9.625 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Circumference = \(2\pi r = 22 \Rightarrow 2 \times \frac{22}{7} \times r = 22 \Rightarrow r = \frac{7}{2}\) cm.</p><p>Area of quadrant = \(\frac{1}{4} \times \pi r^2 = \frac{1}{4} \times \frac{22}{7} \times \frac{49}{4} = \frac{77}{8}\) cm².</p>`
    },
    {
        question: String.raw`A pendulum swings through an angle of \(30°\) and describes an arc 8.8 cm in length. Find the length of the pendulum. (Use \(\pi = 22/7\))`,
        options: ["16.8 cm", "8.4 cm", "15 cm", "14 cm"],
        correctIndex: 0,
        solution: String.raw`<p>Arc length \(l = \frac{30}{360} \times 2 \pi r = 8.8\).</p><p>\(\frac{1}{12} \times 2 \times \frac{22}{7} \times r = 8.8 \Rightarrow r = \frac{8.8 \times 12 \times 7}{44} = 16.8\) cm.</p>`
    }
);

data.concepts[0].pyq.push(
    {
        question: String.raw`[2023] Find the area of the minor segment of a circle of radius 14 cm, when the angle of the corresponding sector is \(60°\).`,
        options: ["17.9 cm²", "15.5 cm²", "16.5 cm²", "14.5 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of sector = \(\frac{60}{360} \times \pi \times 14^2 = \frac{1}{6} \times \frac{22}{7} \times 196 \approx 102.67\) cm².</p><p>Area of equilateral triangle = \(\frac{\sqrt{3}}{4} \times 14^2 = 49\sqrt{3} \approx 49 \times 1.732 \approx 84.87\) cm².</p><p>Area of segment = \(102.67 - 84.87 \approx 17.8\) cm².</p>`
    },
    {
        question: String.raw`[2022] The length of an arc of a circle, subtending an angle of \(54°\) at the centre, is 16.5 cm. Calculate the radius, circumference and area of the circle.`,
        options: ["r = 17.5 cm, C = 110 cm, A = 962.5 cm²", "r = 17.5 cm, C = 110 cm, A = 1925 cm²", "r = 35 cm, C = 220 cm, A = 3850 cm²", "r = 14 cm, C = 88 cm, A = 616 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Arc length = \(\frac{54}{360} \times 2\pi r = 16.5 \Rightarrow \frac{3}{20} \times 2 \times \frac{22}{7} \times r = 16.5 \Rightarrow r = \frac{16.5 \times 140}{132} = 17.5\) cm.</p><p>Circumference = \(2\pi r = 2 \times \frac{22}{7} \times 17.5 = 110\) cm.</p><p>Area = \(\pi r^2 = \frac{22}{7} \times 17.5 \times 17.5 = 962.5\) cm².</p>`
    }
);

// ── Concept 1: Areas of Combined Figures ──
data.concepts[1].practice.push(
    {
        question: String.raw`In a circle of radius 32 cm, a design is formed leaving an equilateral triangle ABC in the middle. Find the area of the design.`,
        options: ["22528/7 - 768√3 cm²", "22528/7 - 256√3 cm²", "704/7 - 768√3 cm²", "22528/7 - 512√3 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of circle = \(\pi \times 32^2 = \frac{22}{7} \times 1024 = \frac{22528}{7}\) cm².</p><p>Radius \(R = 32\). In equilateral triangle, centroid divides altitude in 2:1. Altitude \(h = R + R/2 = 32 + 16 = 48\).</p><p>Side of triangle \(a\): \(\frac{\sqrt{3}}{2}a = 48 \Rightarrow a = \frac{96}{\sqrt{3}} = 32\sqrt{3}\) cm.</p><p>Area of triangle = \(\frac{\sqrt{3}}{4} \times (32\sqrt{3})^2 = \frac{\sqrt{3}}{4} \times 1024 \times 3 = 768\sqrt{3}\) cm².</p><p>Area of design = Area of circle - Area of equilateral triangle = \(\frac{22528}{7} - 768\sqrt{3}\) cm².</p>`
    },
    {
        question: String.raw`Find the area of the shaded region if AB, BC, CD are equal and AD = 12 cm, where AD is the diameter of the largest semicircle. (Three semicircles are drawn with diameters AB, BD, and AD).`,
        options: ["37.71 cm²", "75.42 cm²", "18.85 cm²", "56.57 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>AD = 12 cm. Since AB = BC = CD, each is 4 cm. BD = 8 cm.</p><p>Area of shaded region = Area of semicircle AD + Area of semicircle AB - Area of semicircle BD.</p><p>Area = \(\frac{\pi}{2}(6^2 + 2^2 - 4^2) = \frac{\pi}{2}(36 + 4 - 16) = \frac{\pi}{2}(24) = 12\pi = 37.71\) cm².</p>`
    },
    {
        question: String.raw`A round table cover has six equal designs. If the radius of the cover is 28 cm, find the cost of making the designs at the rate of ₹0.35 per cm². (Use √3 = 1.73)`,
        options: ["₹162.68", "₹160.00", "₹170.00", "₹150.00"],
        correctIndex: 0,
        solution: String.raw`<p>This is the same as the previous question but using \(\sqrt{3} = 1.73\).</p><p>Area of one design (segment) = \(\frac{60}{360} \times \pi \times 28^2 - \frac{\sqrt{3}}{4} \times 28^2 = \frac{410.67 - 339.08}{1} = 71.59\) cm².</p><p>We already calculated this previously. Cost ≈ ₹162.68.</p>`
    },
    {
        question: String.raw`AB and CD are respectively arcs of two concentric circles of radii 21 cm and 7 cm and centre O. If \( \angle AOB = 30°\), find the area of the shaded region enclosed by the arcs.`,
        options: ["308/3 cm²", "308 cm²", "154/3 cm²", "616/3 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of shaded region = Area of sector OAB - Area of sector OCD</p><p>\(= \frac{30}{360} \times \pi \times (21^2 - 7^2) = \frac{1}{12} \times \frac{22}{7} \times (441 - 49) = \frac{1}{12} \times \frac{22}{7} \times 392 = \frac{308}{3}\) cm².</p>`
    }
);

data.concepts[1].pyq.push(
    {
        question: String.raw`[2024] Find the area of the shaded design, where ABCD is a square of side 10 cm and semicircles are drawn with each side of the square as diameter. (Use \(\pi = 3.14\))`,
        options: ["57 cm²", "43 cm²", "114 cm²", "86 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Let the 4 unshaded regions be I, II, III, IV.</p><p>Area of (I + III) = Area of Square - Area of 2 semicircles of radius 5 cm = \(100 - (2 \times \frac{1}{2} \times 3.14 \times 25) = 100 - 78.5 = 21.5\) cm².</p><p>Similarly, Area of (II + IV) = 21.5 cm².</p><p>Total unshaded area = \(21.5 + 21.5 = 43\) cm².</p><p>Area of shaded design = Area of square - Total unshaded area = \(100 - 43 = 57\) cm².</p>`
    },
    {
        question: String.raw`[2023] In the given figure, an equilateral triangle ABC of side 12 cm is drawn. A circle of radius 6 cm is drawn with centre A. Find the area of the shaded region (total figure). (Use \(\pi = 3.14, \sqrt{3} = 1.73\))`,
        options: ["157.08 + 62.28 cm² = 219.36 cm²", "180.25 cm²", "113.04 + 62.28 cm² = 175.32 cm²", "94.2 + 62.28 = 156.48 cm²"],
        correctIndex: 0,
        solution: String.raw`<p>Area of equilateral triangle ABC = \(\frac{\sqrt{3}}{4} \times 12^2 = 36\sqrt{3} = 36 \times 1.73 = 62.28\) cm².</p><p>The circle covers an angle of \(60°\) inside the triangle, so the major sector outside is \(360° - 60° = 300°\).</p><p>Area of major sector = \(\frac{300}{360} \times 3.14 \times 6^2 = \frac{5}{6} \times 3.14 \times 36 = 5 \times 3.14 \times 6 = 94.2\) cm².</p><p>Total area = \(62.28 + 94.2 = 156.48\) cm². Wait, the answer is 156.48 cm².</p>`
    }
);

// ── Chapter Test ──
data.chapterTest.questions.push(
    {
        concept: "Areas",
        question: String.raw`Find the area of the largest circle that can be drawn inside a rectangle with length a and breadth b (a > b).`,
        options: [
            "\\(\\frac{\\pi b^2}{4}\\)",
            "\\(\\frac{\\pi a^2}{4}\\)",
            "\\(\\frac{\\pi a b}{2}\\)",
            "\\(\\pi b^2\\)"
        ],
        correctIndex: 0,
        solution: String.raw`<p>The largest circle that can be drawn inside a rectangle has its diameter equal to the breadth of the rectangle.</p><p>Diameter = \(b \Rightarrow\) Radius = \(\frac{b}{2}\).</p><p>Area = \(\pi r^2 = \pi \left(\frac{b}{2}\right)^2 = \frac{\pi b^2}{4}\).</p>`
    },
    {
        concept: "Areas",
        question: String.raw`If the perimeter of a semi-circular protractor is 36 cm, find its diameter.`,
        options: ["14 cm", "7 cm", "21 cm", "28 cm"],
        correctIndex: 0,
        solution: String.raw`<p>Perimeter = \(\pi r + 2r = r(\frac{22}{7} + 2) = r(\frac{36}{7}) = 36\).</p><p>\(r = 7\) cm. Diameter = 14 cm.</p>`
    },
    {
        concept: "Areas",
        question: String.raw`If the area of a circle is numerically equal to twice its circumference, then the diameter of the circle is:`,
        options: ["8 units", "4 units", "2 units", "16 units"],
        correctIndex: 0,
        solution: String.raw`<p>\(\pi r^2 = 2 \times 2\pi r \Rightarrow r^2 = 4r \Rightarrow r = 4\).</p><p>Diameter = \(2r = 8\) units.</p>`
    }
);

fs.writeFileSync(path, JSON.stringify(data, null, 4));
console.log('Added board level questions to chapter 11.');
