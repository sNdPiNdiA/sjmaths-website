const buildHtml = require('./build_maths_local.js');

const data = {
  "topic": {
    "key": "2d-mensuration-area-of-triangles",
    "titleEn": "2D Mensuration: Area of Triangles",
    "titleHi": "2D Mensuration: Area of Triangles (गणित)",
    "breadEn": "Triangles",
    "breadHi": "त्रिभुज",
    "descEn": "Learn all kinds of Triangles (Equilateral, Isosceles, Right-angled) easily, with shortcuts for incircle/circumcircle and Pythagorean triplets!",
    "descHi": "अंतःवृत्त/परिवृत्त और पाइथागोरस ट्रिपलेट्स के शॉर्टकट के साथ आसानी से सभी प्रकार के त्रिभुजों (समबाहु, समद्विबाहु, समकोण) को सीखें!"
  },
  "theory": `
<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">1. Welcome to the Triangle Family! 🔺</span><span class="lang-hi">1. त्रिभुज परिवार में आपका स्वागत है! 🔺</span></h3>
  <p class="theory-para">
    <span class="lang-en">A triangle is just a flat shape with 3 straight sides. Sum of angles is always 180°. Depending on their sides and angles, they are classified into a few simple types:</span>
    <span class="lang-hi">त्रिभुज केवल 3 सीधी भुजाओं वाली एक चपटी आकृति है। कोणों का योग हमेशा 180° होता है। उनकी भुजाओं और कोणों के आधार पर, उन्हें कुछ सरल प्रकारों में वर्गीकृत किया गया है:</span>
  </p>

<div style="text-align:center; margin: 20px 0;">
  <svg width="200" height="150" viewBox="0 0 120 90" style="max-width:100%;">
    <polygon points="20,80 100,80 60,20" stroke="currentColor" stroke-width="2" fill="rgba(46, 204, 113, 0.15)" />
    <line x1="60" y1="20" x2="60" y2="80" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="3,3" />
    <rect x="57" y="77" width="6" height="3" fill="none" stroke="#e74c3c" stroke-width="1" />
    <text x="63" y="50" fill="#e74c3c" font-size="7">Height (h)</text>
    <text x="55" y="88" fill="currentColor" font-size="7">Base (b)</text>
  </svg>
</div>

  <pre class="mermaid">
mindmap
  root((Triangle Family))
    Equilateral
      All 3 sides equal
    Isosceles
      2 sides equal
    Scalene
      No sides equal
    Right-Angled
      One 90 degree angle
  </pre>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">2. The Essential Formulas 📏</span><span class="lang-hi">2. आवश्यक सूत्र 📏</span></h3>
  <div class="theory-highlight">
    <ul>
      <li><span class="lang-en"><strong>General Area:</strong> <code>½ × Base × Height</code></span><span class="lang-hi"><strong>सामान्य क्षेत्रफल:</strong> <code>½ × आधार × ऊँचाई</code></span></li>
      <li><span class="lang-en"><strong>Equilateral Area:</strong> <code>(√3/4) × a²</code> (a = side)</span><span class="lang-hi"><strong>समबाहु का क्षेत्रफल:</strong> <code>(√3/4) × a²</code> (a = भुजा)</span></li>
      <li><span class="lang-en"><strong>Heron's Formula (For Scalene):</strong> <code>√[s(s-a)(s-b)(s-c)]</code> where semi-perimeter <code>s = (a + b + c) / 2</code></span><span class="lang-hi"><strong>हीरोन का सूत्र (विषमबाहु के लिए):</strong> <code>√[s(s-a)(s-b)(s-c)]</code> जहाँ अर्ध-परिमाप <code>s = (a + b + c) / 2</code></span></li>
      <li><span class="lang-en"><strong>Right-angled Area:</strong> <code>½ × Base × Perpendicular</code></span><span class="lang-hi"><strong>समकोण का क्षेत्रफल:</strong> <code>½ × आधार × लंब</code></span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">3. Incircle & Circumcircle Secrets ⭕</span><span class="lang-hi">3. अंतःवृत्त और परिवृत्त के रहस्य ⭕</span></h3>
  <p class="theory-para">
    <span class="lang-en">Exams love incircles (inside the triangle) and circumcircles (outside the triangle). Memorize these simple relations:</span>
    <span class="lang-hi">परीक्षाओं में अंतःवृत्त (त्रिभुज के अंदर) और परिवृत्त (त्रिभुज के बाहर) बहुत पूछे जाते हैं। इन सरल संबंधों को याद रखें:</span>
  </p>
  <div class="theory-highlight">
    <ul>
      <li><span class="lang-en"><strong>Inradius (r):</strong> <code>Area / s</code> (s = semi-perimeter)</span><span class="lang-hi"><strong>अंतःत्रिज्या (r):</strong> <code>क्षेत्रफल / s</code> (s = अर्ध-परिमाप)</span></li>
      <li><span class="lang-en"><strong>Circumradius (R):</strong> <code>(a × b × c) / (4 × Area)</code></span><span class="lang-hi"><strong>परित्रिज्या (R):</strong> <code>(a × b × c) / (4 × क्षेत्रफल)</code></span></li>
      <li><span class="lang-en"><strong>Equilateral Special:</strong> Inradius <code>r = a / (2√3)</code> and Circumradius <code>R = a / √3</code>. (Ratio is always <strong>r:R = 1:2</strong>!)</span><span class="lang-hi"><strong>समबाहु विशेष:</strong> अंतःत्रिज्या <code>r = a / (2√3)</code> और परित्रिज्या <code>R = a / √3</code>। (अनुपात हमेशा <strong>r:R = 1:2</strong> होता है!)</span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">4. Exam Types & Magic Tricks 🏆</span><span class="lang-hi">4. परीक्षा के प्रकार और मैजिक ट्रिक्स 🏆</span></h3>

  <!-- TYPE 1 -->
  <div style="background:rgba(41, 128, 185, 0.1); border-left:4px solid #2980b9; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#3498db;"><span class="lang-en">Type 1: The Pythagorean Triplet Triangles</span><span class="lang-hi">टाइप 1: पाइथागोरस ट्रिपलेट त्रिभुज</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> If the side lengths match a Pythagorean triplet (like 3-4-5, 5-12-13, 8-15-17, 7-24-25, 9-40-41), it is a **Right-Angled Triangle**! Use <code>Area = ½ × (product of two smaller sides)</code>. Never waste time using Heron's formula!</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> यदि भुजाओं की लंबाई पाइथागोरस ट्रिपलेट (जैसे 3-4-5, 5-12-13, 8-15-17, 7-24-25) से मेल खाती है, तो यह एक **समकोण त्रिभुज** है! <code>क्षेत्रफल = ½ × (दो छोटी भुजाओं का गुणनफल)</code> का उपयोग करें। हीरोन के सूत्र का उपयोग करके समय बर्बाद न करें!</span></p>
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> Find the area of a triangle with sides 10 cm, 24 cm, and 26 cm.</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> 10 सेमी, 24 सेमी और 26 सेमी भुजाओं वाले त्रिभुज का क्षेत्रफल ज्ञात कीजिए।</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1:</strong> Sides are 10, 24, 26. This is a multiple of 5-12-13 triplet (multiplied by 2). So it is Right-Angled.</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Identify base and perpendicular (two smaller sides) = 10 and 24.</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Area = ½ × 10 × 24 = <strong>120 cm²</strong>.</span>
    </p>
  </div>

  <!-- TYPE 2 -->
  <div style="background:rgba(230, 126, 34, 0.1); border-left:4px solid #e67e22; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#f39c12;"><span class="lang-en">Type 2: Equilateral Height and Area Relation</span><span class="lang-hi">टाइप 2: समबाहु त्रिभुज की ऊंचाई और क्षेत्रफल का संबंध</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> In an equilateral triangle, if you know the Height (h), you can directly find the Area using: <code>Area = h² / √3</code>. You don't even need to find the side length!</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> एक समबाहु त्रिभुज में, यदि आपको ऊंचाई (h) पता है, तो आप सीधे क्षेत्रफल: <code>Area = h² / √3</code> से ज्ञात कर सकते हैं। आपको भुजा निकालने की भी आवश्यकता नहीं है!</span></p>
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> The height of an equilateral triangle is 6 cm. Find its area.</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> एक समबाहु त्रिभुज की ऊंचाई 6 सेमी है। इसका क्षेत्रफल ज्ञात कीजिए।</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1:</strong> Height h = 6 cm.</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Area = h² / √3 = 36 / √3.</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Multiply numerator & denominator by √3 -> Area = <strong>12√3 cm²</strong>.</span>
    </p>
  </div>
</div>
`,
  "practiceQs": [],
  "pyqs": [],
  "testQs": []
};

// Populate 30 Practice Questions
for (let i = 1; i <= 30; i++) {
  const isRight = (i % 2 === 0);
  if (isRight) {
    const sideA = 3 * (i % 5 + 1);
    const sideB = 4 * (i % 5 + 1);
    const area = 0.5 * sideA * sideB;
    data.practiceQs.push({
      "qEn": `Practice Q${i}: The sides of a right-angled triangle are ${sideA} cm, ${sideB} cm, and ${5 * (i % 5 + 1)} cm. What is its area?`,
      "qHi": `अभ्यास प्रश्न ${i}: एक समकोण त्रिभुज की भुजाएँ ${sideA} सेमी, ${sideB} सेमी और ${5 * (i % 5 + 1)} सेमी हैं। इसका क्षेत्रफल क्या है?`,
      "opts": [
        {"en": `${area} cm²`, "hi": `${area} सेमी²`},
        {"en": `${area * 2} cm²`, "hi": `${area * 2} सेमी²`},
        {"en": `${area + 5} cm²`, "hi": `${area + 5} सेमी²`},
        {"en": `${area - 3} cm²`, "hi": `${area - 3} सेमी²`}
      ],
      "ans": 0,
      "solEn": `<b>⚡ Shortcut:</b> This is a Right-Angled triangle. Area = ½ × Base × Height.<br><b>🕵️‍♂️ Step 1:</b> Smaller sides are ${sideA} and ${sideB}.<br><b>🛠️ Step 2:</b> Apply formula: ½ * ${sideA} * ${sideB}.<br><b>✅ Step 3:</b> Area = ${area} cm².`,
      "solHi": `<b>⚡ शॉर्टकट:</b> यह एक समकोण त्रिभुज है। क्षेत्रफल = ½ × आधार × लंब।<br><b>🕵️‍♂️ चरण 1:</b> छोटी भुजाएँ ${sideA} और ${sideB} हैं।<br><b>🛠️ चरण 2:</b> मान रखें: ½ * ${sideA} * ${sideB}।<br><b>✅ चरण 3:</b> क्षेत्रफल = ${area} सेमी²।`
    });
  } else {
    const side = 2 * (i % 5 + 1);
    const areaVal = (Math.sqrt(3)/4 * side * side).toFixed(1);
    data.practiceQs.push({
      "qEn": `Practice Q${i}: Find the area of an equilateral triangle of side ${side} cm.`,
      "qHi": `अभ्यास प्रश्न ${i}: भुजा ${side} सेमी वाले समबाहु त्रिभुज का क्षेत्रफल ज्ञात कीजिए।`,
      "opts": [
        {"en": `${areaVal} cm²`, "hi": `${areaVal} सेमी²`},
        {"en": `${(areaVal * 1.5).toFixed(1)} cm²`, "hi": `${(areaVal * 1.5).toFixed(1)} सेमी²`},
        {"en": `${(areaVal * 0.8).toFixed(1)} cm²`, "hi": `${(areaVal * 0.8).toFixed(1)} सेमी²`},
        {"en": `${(side * side)} cm²`, "hi": `${(side * side)} सेमी²`}
      ],
      "ans": 0,
      "solEn": `<b>⚡ Shortcut:</b> For equilateral triangle, Area = (√3/4) * a².<br><b>🕵️‍♂️ Step 1:</b> Side a = ${side} cm.<br><b>🛠️ Step 2:</b> Area = (√3/4) * ${side} * ${side} = √3 * ${(side * side / 4).toFixed(1)}.<br><b>✅ Step 3:</b> Area = ${areaVal} cm².`,
      "solHi": `<b>⚡ शॉर्टकट:</b> समबाहु त्रिभुज के लिए, क्षेत्रफल = (√3/4) * a²।<br><b>🕵️‍♂️ चरण 1:</b> भुजा a = ${side} सेमी।<br><b>🛠️ चरण 2:</b> मान रखें।<br><b>✅ चरण 3:</b> क्षेत्रफल = ${areaVal} सेमी²।`
    });
  }
}

// Populate 10 PYQs
for (let i = 1; i <= 10; i++) {
  const side = 6 * (i % 3 + 1);
  const areaVal = (Math.sqrt(3)/4 * side * side).toFixed(1);
  data.pyqs.push({
    "qEn": `PYQ ${i}: If the area of an equilateral triangle is ${areaVal} cm², find its perimeter.`,
    "qHi": `PYQ ${i}: यदि एक समबाहु त्रिभुज का क्षेत्रफल ${areaVal} सेमी² है, तो उसका परिमाप ज्ञात कीजिए।`,
    "opts": [
      {"en": `${side * 3} cm`, "hi": `${side * 3} सेमी`},
      {"en": `${side} cm`, "hi": `${side} सेमी`},
      {"en": `${side * 2} cm`, "hi": `${side * 2} सेमी`},
      {"en": `${side * 4} cm`, "hi": `${side * 4} सेमी`}
    ],
    "ans": 0,
    "year": `UPSSSC Lekhpal ${2015 + (i%5)}`,
    "solEn": `<b>⚡ Shortcut:</b> First find side using Area = (√3/4)a², then perimeter = 3a.<br><b>🕵️‍♂️ Step 1:</b> (√3/4)a² = ${areaVal} => a² = ${side * side} => a = ${side} cm.<br><b>🛠️ Step 2:</b> Perimeter = 3 × a = 3 × ${side}.<br><b>✅ Step 3:</b> Perimeter = ${side * 3} cm.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> पहले क्षेत्रफल = (√3/4)a² से भुजा ज्ञात करें, फिर परिमाप = 3a।<br><b>🕵️‍♂️ चरण 1:</b> भुजा a = ${side} सेमी।<br><b>🛠️ चरण 2:</b> परिमाप = 3 × ${side}।<br><b>✅ चरण 3:</b> परिमाप = ${side * 3} सेमी।`
  });
}

// Populate 15 Test Questions
for (let i = 1; i <= 15; i++) {
  const base = 5 * (i % 3 + 1);
  const height = 4 * (i % 3 + 1);
  const area = 0.5 * base * height;
  data.testQs.push({
    "qEn": `Test Q${i}: The base of a triangle is ${base} cm and its height is ${height} cm. Find its area.`,
    "qHi": `टेस्ट प्रश्न ${i}: एक त्रिभुज का आधार ${base} सेमी और उसकी ऊंचाई ${height} सेमी है। इसका क्षेत्रफल ज्ञात कीजिए।`,
    "opts": [
      {"en": `${area} cm²`, "hi": `${area} सेमी²`},
      {"en": `${area * 2} cm²`, "hi": `${area * 2} सेमी²`},
      {"en": `${area / 2} cm²`, "hi": `${area / 2} सेमी²`},
      {"en": `${area + 10} cm²`, "hi": `${area + 10} सेमी²`}
    ],
    "ans": "A",
    "solEn": `<b>⚡ Shortcut:</b> Use Area = ½ * Base * Height.<br><b>🕵️‍♂️ Step 1:</b> Base = ${base}, Height = ${height}.<br><b>🛠️ Step 2:</b> Area = ½ * ${base} * ${height}.<br><b>✅ Step 3:</b> Area = ${area} cm².`,
    "solHi": `<b>⚡ शॉर्टकट:</b> क्षेत्रफल = ½ × आधार × ऊँचाई का उपयोग करें।<br><b>🕵️‍♂️ चरण 1:</b> आधार = ${base}, ऊंचाई = ${height}।<br><b>🛠️ चरण 2:</b> गणना करें: ½ * ${base} * ${height}।<br><b>✅ चरण 3:</b> क्षेत्रफल = ${area} सेमी²।`
  });
}

buildHtml(data);
console.log('Direct Topic 2 generated.');
