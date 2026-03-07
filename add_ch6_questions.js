const fs = require('fs');

const path = 'class-10-maths/chapter-6-data.json';
let data = JSON.parse(fs.readFileSync(path, 'utf8'));

// We use String.raw to avoid JS escape parsing, and then we will run fix_ch6_escapes.js

data.concepts[0].practice.push(
    {
        question: String.raw`In \(\triangle ABC\), \(DE \parallel BC\). If \(AD/DB = 2/3\) and \(AC = 18\text{ cm}\), find \(AE\).`,
        options: ['7.2 cm', '10.8 cm', '3.6 cm', '5.4 cm'],
        correctIndex: 0,
        solution: String.raw`<p>By BPT corollary: \(\frac{AD}{AB} = \frac{AE}{AC}\).</p><p>We are given \(\frac{AD}{DB} = \frac{2}{3}\), so \(\frac{AD}{AB} = \frac{2}{2+3} = \frac{2}{5}\).</p><p>\(\frac{2}{5} = \frac{AE}{18}\)</p><p>\(AE = \frac{36}{5} = 7.2\text{ cm}\).</p>`
    },
    {
        question: String.raw`In \(\triangle PQR\), \(S\) and \(T\) are points on \(PQ\) and \(PR\) respectively. If \(PS/PQ = 1/3\) and \(PT/PR = 1/3\), what is the ratio \(ST/QR\)?`,
        options: ['1/2', '1/3', '1/4', 'Cannot be determined'],
        correctIndex: 1,
        solution: String.raw`<p>Since \(\frac{PS}{PQ} = \frac{PT}{PR} = \frac{1}{3}\), by the Converse of BPT, \(ST \parallel QR\).</p><p>Therefore, \(\triangle PST \sim \triangle PQR\) (by AA Similarity, as \(\angle P\) is common and corresponding angles are equal).</p><p>Ratio of corresponding sides \(\frac{ST}{QR} = \frac{PS}{PQ} = \frac{1}{3}\).</p>`
    }
);

data.concepts[0].pyq.push(
    {
        question: String.raw`[2021] In \(\triangle LMN\), \(PQ \parallel MN\) and \(LP/PM = 4/13\). If \(LN = 20.4\text{ cm}\), find \(LQ\).`,
        options: ['4.8 cm', '5.8 cm', '3.8 cm', '6.8 cm'],
        correctIndex: 0,
        solution: String.raw`<p>By BPT: \(\frac{LP}{LM} = \frac{LQ}{LN}\).</p><p>\(\frac{LP}{LM} = \frac{4}{4+13} = \frac{4}{17}\).</p><p>\(\frac{4}{17} = \frac{LQ}{20.4}\)</p><p>\(LQ = \frac{4 \times 20.4}{17} = 4 \times 1.2 = 4.8\text{ cm}\).</p>`
    }
);

data.concepts[1].practice.push(
    {
        question: String.raw`Two isosceles triangles have equal vertical angles and their areas are in the ratio 16:25. The ratio of their corresponding altitudes is:`,
        options: ['16:25', '4:5', '5:4', '256:625'],
        correctIndex: 1,
        solution: String.raw`<p>If the vertical angles are equal, the two base angles are also equal. Thus, the triangles are similar by AAA.</p><p>For similar triangles, the ratio of areas = (ratio of corresponding altitudes)<sup>2</sup>.</p><p>\(\left(\frac{h_1}{h_2}\right)^2 = \frac{16}{25} \Rightarrow \frac{h_1}{h_2} = \frac{4}{5}\).</p>`
    },
    {
        question: String.raw`If \(\triangle ABC \sim \triangle DEF\), \(AB = 2DE\) and the area of \(\triangle ABC\) is 56 sq cm, find the area of \(\triangle DEF\).`,
        options: ['12 sq cm', '14 sq cm', '28 sq cm', '112 sq cm'],
        correctIndex: 1,
        solution: String.raw`<p>Ratio of areas of similar triangles is the square of the ratio of their corresponding sides.</p><p>\(\frac{\text{ar}(ABC)}{\text{ar}(DEF)} = \left(\frac{AB}{DE}\right)^2 = \left(\frac{2}{1}\right)^2 = 4\).</p><p>\(\frac{56}{\text{ar}(DEF)} = 4 \Rightarrow \text{ar}(DEF) = \frac{56}{4} = 14\text{ sq cm}\).</p>`
    }
);

data.concepts[1].pyq.push(
    {
        question: String.raw`[2022] The legs of a right triangle are 3cm and 4cm. What is the length of the altitude drawn from the right angle to the hypotenuse?`,
        options: ['2.4 cm', '2.5 cm', '3.0 cm', '3.5 cm'],
        correctIndex: 0,
        solution: String.raw`<p>First, find the hypotenuse using Pythagoras Theorem: \(c^2 = 3^2 + 4^2 = 25 \Rightarrow c = 5\text{cm}\).</p><p>Let the altitude be \(h\). The triangles formed by the altitude are similar to the large triangle.</p><p>Using the area method: Area = \(\frac{1}{2} \times \text{base} \times \text{height}\).</p><p>Using legs: Area = \(\frac{1}{2} \times 3 \times 4 = 6\).</p><p>Using hypotenuse: Area = \(\frac{1}{2} \times 5 \times h = 6 \Rightarrow 2.5h = 6 \Rightarrow h = 2.4\text{cm}\).</p>`
    }
);

data.chapterTest.questions.push(
    {
        concept: String.raw`Basic Proportionality Theorem`,
        question: String.raw`In \(\triangle ABC\), \(PQ \parallel BC\). If \(AP = 3\text{ cm}\), \(PB = 6\text{ cm}\), and \(AQ = 5\text{ cm}\). Find \(QC\).`,
        options: ['5 cm', '10 cm', '15 cm', '2.5 cm'],
        correctIndex: 1,
        solution: String.raw`By BPT, \(\frac{AP}{PB} = \frac{AQ}{QC}\). \(\frac{3}{6} = \frac{5}{QC} \Rightarrow \frac{1}{2} = \frac{5}{QC} \Rightarrow QC = 10\text{ cm}\).`
    },
    {
        concept: String.raw`Similarity`,
        question: String.raw`A pole measuring 6m long casts a shadow 2m long on the ground. At the same time, a tower casts a shadow 60m long. Determine the height of the tower.`,
        options: ['180 m', '120 m', '60 m', '20 m'],
        correctIndex: 0,
        solution: String.raw`At the same time, shadows form similar triangles. \(\frac{h}{60} = \frac{6}{2} \Rightarrow \frac{h}{60} = 3 \Rightarrow h = 180\text{ m}\).`
    }
);

fs.writeFileSync(path, JSON.stringify(data, null, 4));
console.log('Added 8 new questions successfully.');
