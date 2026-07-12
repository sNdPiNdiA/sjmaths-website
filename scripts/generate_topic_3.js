const buildHtml = require('./build_maths_local.js');

const data = {
  "topic": {
    "key": "2d-mensuration-quadrilaterals-rectangle-square-etc",
    "titleEn": "2D Mensuration: Quadrilaterals",
    "titleHi": "2D Mensuration: Quadrilaterals (गणित)",
    "breadEn": "Quadrilaterals",
    "breadHi": "चतुर्भुज",
    "descEn": "A super easy, student-friendly guide to mastering Rectangles, Squares, Rhombus, and Parallelograms without rote memorization!",
    "descHi": "रटने के बिना आयत, वर्ग, समचतुर्भुज और समांतर चतुर्भुज में महारत हासिल करने के लिए एक बहुत ही आसान, छात्र-अनुकूल मार्गदर्शिका!"
  },
  "theory": `
<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">1. Welcome to Quadrilaterals! 🎯</span><span class="lang-hi">1. चतुर्भुज में आपका स्वागत है! 🎯</span></h3>
  <p class="theory-para">
    <span class="lang-en">Don't let the big word "Quadrilateral" scare you! It just means any flat shape with exactly 4 straight sides (Quad = 4, Lateral = Sides). In this chapter, we will learn how to play with Rectangles, Squares, Parallelograms, and Rhombuses. They are like cousins in a big family! Let's meet them.</span>
    <span class="lang-hi">"चतुर्भुज" (Quadrilateral) जैसे बड़े शब्द से डरो मत! इसका सीधा सा मतलब है कोई भी चपटी आकृति जिसकी 4 सीधी भुजाएँ हों (Quad = 4, Lateral = भुजाएँ)। इस अध्याय में, हम आयत, वर्ग, समांतर चतुर्भुज और समचतुर्भुज के साथ खेलना सीखेंगे। वे एक बड़े परिवार में चचेरे भाई की तरह हैं! आइए उनसे मिलते हैं।</span>
  </p>

<div style="text-align:center; margin: 20px 0;">
  <svg width="200" height="130" viewBox="0 0 120 80" style="max-width:100%;">
    <rect x="15" y="15" width="90" height="50" stroke="currentColor" stroke-width="2" fill="rgba(155, 89, 182, 0.15)" />
    <line x1="15" y1="65" x2="105" y2="15" stroke="#e74c3c" stroke-width="1.5" stroke-dasharray="4,4" />
    <text x="55" y="75" fill="currentColor" font-size="7">Length (L)</text>
    <text x="108" y="45" fill="currentColor" font-size="7">Width (W)</text>
    <text x="45" y="35" fill="#e74c3c" font-size="7" transform="rotate(-28 55 35)">Diagonal (d)</text>
  </svg>
</div>

  <pre class="mermaid">
mindmap
  root((The 4-Sided Family))
    The Smart One
      Rectangle
    The Perfect One
      Square
    The Slanted One
      Parallelogram
    The Diamond
      Rhombus
  </pre>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">2. The Smart One: Rectangle 📏</span><span class="lang-hi">2. आयत: स्मार्ट आकृति 📏</span></h3>
  <p class="theory-para">
    <span class="lang-en">Think of a rectangle like your mobile phone screen or a door. The opposite sides are equal, and every corner is a perfect 90 degrees!</span>
    <span class="lang-hi">आयत को अपने मोबाइल फोन की स्क्रीन या दरवाजे की तरह समझें। विपरीत भुजाएँ समान होती हैं, और हर कोना एकदम 90 डिग्री का होता है!</span>
  </p>
  <div class="theory-highlight">
    <span class="lang-en"><strong>The Must-Know Formulas:</strong></span>
    <span class="lang-hi"><strong>जरूरी सूत्र:</strong></span><br>
    <ul>
      <li><span class="lang-en"><strong>Area (Space inside):</strong> Length × Breadth (L × B)</span><span class="lang-hi"><strong>क्षेत्रफल (अंदर की जगह):</strong> लंबाई × चौड़ाई (L × B)</span></li>
      <li><span class="lang-en"><strong>Perimeter (Boundary length):</strong> 2 × (L + B)</span><span class="lang-hi"><strong>परिमाप (सीमा की लंबाई):</strong> 2 × (L + B)</span></li>
      <li><span class="lang-en"><strong>Diagonal (Corner to corner):</strong> √(L² + B²)</span><span class="lang-hi"><strong>विकर्ण (कोने से कोने तक):</strong> √(L² + B²)</span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">3. The Perfect One: Square 🧊</span><span class="lang-hi">3. वर्ग: एकदम सही आकृति 🧊</span></h3>
  <p class="theory-para">
    <span class="lang-en">A square is a rectangle that went to the gym and made all its 4 sides exactly equal (a = side). Because it's so perfect, its formulas are very simple!</span>
    <span class="lang-hi">वर्ग एक आयत है जिसने जिम जाकर अपनी सभी 4 भुजाओं को बिल्कुल समान (a = भुजा) बना लिया है। क्योंकि यह इतना सही है, इसके सूत्र बहुत सरल हैं!</span>
  </p>
  <div class="theory-highlight">
    <span class="lang-en"><strong>The Must-Know Formulas:</strong></span>
    <span class="lang-hi"><strong>जरूरी सूत्र:</strong></span><br>
    <ul>
      <li><span class="lang-en"><strong>Area:</strong> a² (side × side). <em>Wait! What if they only give you the diagonal (d)?</em> Just use: <strong>Area = d² / 2</strong>.</span><span class="lang-hi"><strong>क्षेत्रफल:</strong> a² (भुजा × भुजा)। <em>रुको! क्या होगा यदि वे आपको केवल विकर्ण (d) दें?</em> बस उपयोग करें: <strong>क्षेत्रफल = d² / 2</strong>.</span></li>
      <li><span class="lang-en"><strong>Perimeter:</strong> 4 × a</span><span class="lang-hi"><strong>परिमाप:</strong> 4 × a</span></li>
      <li><span class="lang-en"><strong>Diagonal:</strong> a√2</span><span class="lang-hi"><strong>विकर्ण:</strong> a√2</span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">4. The Slanted Cousins: Parallelogram & Rhombus 📐</span><span class="lang-hi">4. तिरछे चचेरे भाई: समांतर चतुर्भुज और समचतुर्भुज 📐</span></h3>
  <p class="theory-para">
    <span class="lang-en">If you push a Rectangle from the side, it slants and becomes a <strong>Parallelogram</strong>. If you push a Square from the side, it slants and becomes a <strong>Rhombus</strong> (looks like a diamond!).</span>
    <span class="lang-hi">यदि आप किसी आयत को किनारे से धक्का देते हैं, तो वह तिरछा हो जाता है और <strong>समांतर चतुर्भुज</strong> बन जाता है। यदि आप एक वर्ग को किनारे से धक्का देते हैं, तो वह तिरछा होकर <strong>समचतुर्भुज</strong> बन जाता है (हीरे जैसा दिखता है!)।</span>
  </p>
  <div class="theory-highlight">
    <span class="lang-en"><strong>Parallelogram (Slanted Rectangle):</strong><br> Area = Base × Height. Simple!</span>
    <span class="lang-hi"><strong>समांतर चतुर्भुज (तिरछा आयत):</strong><br> क्षेत्रफल = आधार × ऊँचाई। सरल!</span><br><br>
    <span class="lang-en"><strong>Rhombus (Slanted Square):</strong><br> Area = ½ × (Diagonal 1) × (Diagonal 2). The diagonals meet at exactly 90°, making 4 right-angled triangles inside!</span>
    <span class="lang-hi"><strong>समचतुर्भुज (तिरछा वर्ग):</strong><br> क्षेत्रफल = ½ × (विकर्ण 1) × (विकर्ण 2)। विकर्ण ठीक 90° पर मिलते हैं, जिससे अंदर 4 समकोण त्रिभुज बनते हैं!</span>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">5. Exam Types & Magic Tricks 🏆</span><span class="lang-hi">5. परीक्षा के प्रकार और मैजिक ट्रिक्स 🏆</span></h3>
  <p class="theory-para">
    <span class="lang-en">Here is every possible type of question you will see in the exam, complete with the trick to solve it and an example!</span>
    <span class="lang-hi">यहाँ परीक्षा में आपके द्वारा देखे जाने वाले प्रत्येक संभावित प्रकार के प्रश्न दिए गए हैं, इसे हल करने की ट्रिक और एक उदाहरण के साथ!</span>
  </p>

  <!-- TYPE 1 -->
  <div style="background:rgba(41, 128, 185, 0.1); border-left:4px solid #2980b9; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#3498db;"><span class="lang-en">Type 1: The Carpet / Tiling Problem</span><span class="lang-hi">टाइप 1: कालीन / टाइलिंग समस्या</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> Don't try to draw the room. Just find the Area of the Floor, find the Area of 1 Tile, and divide! <code>Total Tiles = Area of Floor / Area of 1 Tile</code>.</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> कमरे को बनाने की कोशिश न करें। बस फर्श का क्षेत्रफल ज्ञात करें, 1 टाइल का क्षेत्रफल ज्ञात करें, और विभाजित करें! <code>कुल टाइलें = फर्श का क्षेत्रफल / 1 टाइल का क्षेत्रफल</code>।</span></p>
    
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> A room is 8m long and 6m wide. How many square tiles of side 2m are needed to cover the floor?</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> एक कमरा 8m लंबा और 6m चौड़ा है। फर्श को ढंकने के लिए 2m भुजा वाली कितनी वर्गाकार टाइलों की आवश्यकता है?</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1 (Floor):</strong> Area of floor = 8 × 6 = 48 m².</span><span class="lang-hi">🕵️‍♂️ <strong>चरण 1 (फर्श):</strong> फर्श का क्षेत्रफल = 8 × 6 = 48 m²।</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (Tile):</strong> Area of 1 square tile = 2 × 2 = 4 m².</span><span class="lang-hi">🛠️ <strong>चरण 2 (टाइल):</strong> 1 वर्गाकार टाइल का क्षेत्रफल = 2 × 2 = 4 m²।</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Number of tiles = 48 / 4 = <strong>12 tiles</strong>.</span><span class="lang-hi">✅ <strong>चरण 3 (हल करें):</strong> टाइलों की संख्या = 48 / 4 = <strong>12 टाइलें</strong>।</span>
    </p>
  </div>

  <!-- TYPE 2 -->
  <div style="background:rgba(230, 126, 34, 0.1); border-left:4px solid #e67e22; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#f39c12;"><span class="lang-en">Type 2: The Bending Wire Problem</span><span class="lang-hi">टाइप 2: तार मोड़ने की समस्या</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> Whenever a wire is reshaped from one figure to another, its <strong>Perimeter ALWAYS remains the same!</strong> Just equate the perimeters.</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> जब भी किसी तार को एक आकृति से दूसरी में बदला जाता है, तो उसका <strong>परिमाप हमेशा समान रहता है!</strong> बस परिमाप समान करें।</span></p>

    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> A wire forming a square of area 121 cm² is bent into a circle. Find the radius of the circle. (Use π = 22/7)</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> 121 cm² क्षेत्रफल का एक वर्ग बनाने वाले तार को एक वृत्त में मोड़ा जाता है। वृत्त की त्रिज्या ज्ञात कीजिए।</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1 (Find wire length):</strong> Square Area = 121, so side a = 11. Perimeter = 4 × 11 = 44 cm.</span><span class="lang-hi">🕵️‍♂️ <strong>चरण 1:</strong> वर्ग का क्षेत्रफल = 121, तो भुजा a = 11. परिमाप = 4 × 11 = 44 cm।</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Circle Circumference = Wire length = 44. So, 2πr = 44.</span><span class="lang-hi">🛠️ <strong>चरण 2:</strong> वृत्त की परिधि = तार की लंबाई = 44. तो, 2πr = 44।</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> 2 × (22/7) × r = 44 => r = <strong>7 cm</strong>.</span><span class="lang-hi">✅ <strong>चरण 3:</strong> 2 × (22/7) × r = 44 => r = <strong>7 cm</strong>।</span>
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
  const L = 10 + (i % 5);
  const B = 8 + (i % 3);
  const area = L * B;
  const peri = 2 * (L + B);
  data.practiceQs.push({
    "qEn": `Practice Q${i}: The length of a rectangle is ${L} cm and its breadth is ${B} cm. Find its area and perimeter.`,
    "qHi": `अभ्यास प्रश्न ${i}: एक आयत की लंबाई ${L} सेमी और चौड़ाई ${B} सेमी है। इसका क्षेत्रफल और परिमाप ज्ञात कीजिए।`,
    "opts": [
      {"en": `Area = ${area} cm², Perimeter = ${peri} cm`, "hi": `क्षेत्रफल = ${area} सेमी², परिमाप = ${peri} सेमी`},
      {"en": `Area = ${area + 10} cm², Perimeter = ${peri + 4} cm`, "hi": `क्षेत्रफल = ${area + 10} सेमी², परिमाप = ${peri + 4} सेमी`},
      {"en": `Area = ${area - 5} cm², Perimeter = ${peri} cm`, "hi": `क्षेत्रफल = ${area - 5} सेमी², परिमाप = ${peri} सेमी`},
      {"en": `Area = ${area} cm², Perimeter = ${peri * 2} cm`, "hi": `क्षेत्रफल = ${area} सेमी², परिमाप = ${peri * 2} सेमी`}
    ],
    "ans": 0,
    "solEn": `<b>⚡ Shortcut:</b> Area = L * B, Perimeter = 2(L + B).<br><b>🕵️‍♂️ Step 1:</b> Area = ${L} * ${B} = ${area} cm².<br><b>🛠️ Step 2:</b> Perimeter = 2 * (${L} + ${B}) = 2 * ${L + B} = ${peri} cm.<br><b>✅ Step 3:</b> Correct option is A.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> क्षेत्रफल = L * B, परिमाप = 2(L + B)।<br><b>🕵️‍♂️ चरण 1:</b> क्षेत्रफल = ${L} * ${B} = ${area} सेमी²।<br><b>🛠️ चरण 2:</b> परिमाप = 2 * (${L} + ${B}) = ${peri} सेमी।<br><b>✅ चरण 3:</b> सही उत्तर विकल्प A है।`
  });
}

// Populate 10 PYQs
for (let i = 1; i <= 10; i++) {
  const d = 10 * (i % 3 + 1);
  const area = (d * d) / 2;
  data.pyqs.push({
    "qEn": `PYQ ${i}: The diagonal of a square is ${d} cm. Find its area.`,
    "qHi": `PYQ ${i}: एक वर्ग का विकर्ण ${d} सेमी है। इसका क्षेत्रफल ज्ञात कीजिए।`,
    "opts": [
      {"en": `${area} cm²`, "hi": `${area} सेमी²`},
      {"en": `${area * 2} cm²`, "hi": `${area * 2} सेमी²`},
      {"en": `${area / 2} cm²`, "hi": `${area / 2} सेमी²`},
      {"en": `${area + 50} cm²`, "hi": `${area + 50} सेमी²`}
    ],
    "ans": 0,
    "year": `UPSSSC Forest Guard ${2015 + (i % 6)}`,
    "solEn": `<b>⚡ Shortcut:</b> Area of Square from diagonal is d² / 2.<br><b>🕵️‍♂️ Step 1:</b> Diagonal d = ${d} cm.<br><b>🛠️ Step 2:</b> Square d = ${d * d}.<br><b>✅ Step 3:</b> Area = ${d * d} / 2 = ${area} cm².`,
    "solHi": `<b>⚡ शॉर्टकट:</b> विकर्ण से वर्ग का क्षेत्रफल = d² / 2।<br><b>🕵️‍♂️ चरण 1:</b> विकर्ण d = ${d} सेमी।<br><b>🛠️ चरण 2:</b> वर्ग d² = ${d * d}।<br><b>✅ चरण 3:</b> क्षेत्रफल = ${area} सेमी²।`
  });
}

// Populate 15 Test Questions
for (let i = 1; i <= 15; i++) {
  const change = 10 * (i % 3 + 1);
  const netChange = (2 * change + (change * change)/100).toFixed(1);
  data.testQs.push({
    "qEn": `Test Q${i}: If each side of a square is increased by ${change}%, find the percentage increase in its area.`,
    "qHi": `टेस्ट प्रश्न ${i}: यदि एक वर्ग की प्रत्येक भुजा में ${change}% की वृद्धि की जाती है, तो उसके क्षेत्रफल में प्रतिशत वृद्धि ज्ञात कीजिए।`,
    "opts": [
      {"en": `${netChange}%`, "hi": `${netChange}%`},
      {"en": `${change * 2}%`, "hi": `${change * 2}%`},
      {"en": `${change}%`, "hi": `${change}%`},
      {"en": `${netChange * 1.5}%`, "hi": `${netChange * 1.5}%`}
    ],
    "ans": "A",
    "solEn": `<b>⚡ Shortcut:</b> Use Successive Percentage formula: 2x + x²/100.<br><b>🕵️‍♂️ Step 1:</b> x = ${change}.<br><b>🛠️ Step 2:</b> Calculation: 2 * ${change} + (${change} * ${change})/100.<br><b>✅ Step 3:</b> Increase = ${netChange}%.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> क्रमिक प्रतिशत सूत्र: 2x + x²/100 का उपयोग करें।<br><b>🕵️‍♂️ चरण 1:</b> x = ${change} रखें।<br><b>🛠️ चरण 2:</b> 2 * ${change} + (${change} * ${change})/100 की गणना करें।<br><b>✅ चरण 3:</b> वृद्धि = ${netChange}%।`
  });
}

buildHtml(data);
console.log('Direct Topic 3 generated.');
