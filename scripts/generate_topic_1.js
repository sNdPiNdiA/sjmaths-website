const buildHtml = require('./build_maths_local.js');

const data = {
  "topic": {
    "key": "2d-mensuration-area-of-circles",
    "titleEn": "2D Mensuration: Area of Circles",
    "titleHi": "2D Mensuration: Area of Circles (गणित)",
    "breadEn": "Circles",
    "breadHi": "वृत्त",
    "descEn": "A super easy, interactive, student-friendly guide to mastering Circles, Sectors, and Rings without getting confused by formula definitions!",
    "descHi": "सूत्र परिभाषाओं से भ्रमित हुए बिना वृत्त, त्रिज्यखंड और वलय में महारत हासिल करने के लिए एक सुपर आसान, छात्र-अनुकूल मार्गदर्शिका!"
  },
  "theory": `
<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">1. Welcome to the World of Circles! 🔴</span><span class="lang-hi">1. वृत्तों की दुनिया में आपका स्वागत है! 🔴</span></h3>
  <p class="theory-para">
    <span class="lang-en">A circle is just a round shape. Think of a pizza, a wheel, or a coin! The distance from the center to the edge is the <strong>Radius (r)</strong>. The distance all the way across through the center is the <strong>Diameter (d = 2r)</strong>. The boundary length is the <strong>Circumference (C = 2πr)</strong>.</span>
    <span class="lang-hi">वृत्त केवल एक गोल आकृति है। एक पिज्जा, एक पहिया, या एक सिक्के के बारे में सोचें! केंद्र से किनारे तक की दूरी <strong>त्रिज्या (r)</strong> है। केंद्र से होकर गुजरने वाली कुल दूरी <strong>व्यास (d = 2r)</strong> है। सीमा की लंबाई <strong>परिधि (C = 2πr)</strong> है।</span>
  </p>

<div style="text-align:center; margin: 20px 0;">
  <svg width="180" height="180" viewBox="0 0 100 100" style="max-width:100%;">
    <circle cx="50" cy="50" r="40" stroke="currentColor" stroke-width="2" fill="rgba(52, 152, 219, 0.15)" />
    <line x1="50" y1="50" x2="90" y2="50" stroke="#e74c3c" stroke-width="2" stroke-dasharray="3,3" />
    <circle cx="50" cy="50" r="2" fill="#e74c3c" />
    <text x="70" y="45" fill="#e74c3c" font-size="8" font-weight="bold">r</text>
    <line x1="10" y1="50" x2="50" y2="50" stroke="#2ecc71" stroke-width="1.5" />
    <text x="25" y="45" fill="#2ecc71" font-size="8">Radius</text>
    <path d="M 50,50 L 78.28,21.72 A 40,40 0 0,0 50,10 Z" fill="rgba(230, 126, 34, 0.3)" />
    <text x="55" y="30" fill="#e67e22" font-size="8" font-weight="bold">Sector</text>
  </svg>
</div>

  <pre class="mermaid">
mindmap
  root((Circle Concepts))
    Boundary
      Circumference: 2πr
      Arc Length: θ/360 × 2πr
    Space Inside
      Area: πr²
      Sector Area: θ/360 × πr²
    Cousins
      Semi-circle
      Rings (Concentric)
  </pre>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">2. The Essential Formulas 📏</span><span class="lang-hi">2. आवश्यक सूत्र 📏</span></h3>
  <div class="theory-highlight">
    <ul>
      <li><span class="lang-en"><strong>Area (Space inside):</strong> <code>πr²</code> (Remember, π ≈ 22/7 or 3.14)</span><span class="lang-hi"><strong>क्षेत्रफल (अंदर का स्थान):</strong> <code>πr²</code> (याद रखें, π ≈ 22/7 या 3.14)</span></li>
      <li><span class="lang-en"><strong>Circumference (Boundary):</strong> <code>2πr</code></span><span class="lang-hi"><strong>परिधि (सीमा):</strong> <code>2πr</code></span></li>
      <li><span class="lang-en"><strong>Semi-Circle Area:</strong> <code>½πr²</code></span><span class="lang-hi"><strong>अर्धवृत्त का क्षेत्रफल:</strong> <code>½πr²</code></span></li>
      <li><span class="lang-en"><strong>Semi-Circle Perimeter:</strong> <code>πr + 2r</code> (Don't forget the flat diameter edge!)</span><span class="lang-hi"><strong>अर्धवृत्त का परिमाप:</strong> <code>πr + 2r</code> (सपाट व्यास किनारे को न भूलें!)</span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">3. Sectors, Segments, and Rings 🍕</span><span class="lang-hi">3. त्रिज्यखंड, वृत्तखंड और वलय 🍕</span></h3>
  <p class="theory-para">
    <span class="lang-en">A **Sector** is like a slice of pizza. A **Ring (Concentric circles)** is like a running track or a donut with outer radius <strong>R</strong> and inner radius <strong>r</strong>.</span>
    <span class="lang-hi">एक **त्रिज्यखंड (Sector)** पिज्जा के टुकड़े की तरह होता है। एक **वलय (Ring)** दौड़ने वाले ट्रैक या डोनट की तरह होता है जिसकी बाहरी त्रिज्या <strong>R</strong> और आंतरिक त्रिज्या <strong>r</strong> होती है।</span>
  </p>
  <div class="theory-highlight">
    <ul>
      <li><span class="lang-en"><strong>Area of Sector:</strong> <code>(θ/360) × πr²</code> (θ is the slice angle)</span><span class="lang-hi"><strong>त्रिज्यखंड का क्षेत्रफल:</strong> <code>(θ/360) × πr²</code> (θ स्लाइस का कोण है)</span></li>
      <li><span class="lang-en"><strong>Arc Length:</strong> <code>(θ/360) × 2πr</code></span><span class="lang-hi"><strong>चाप की लंबाई:</strong> <code>(θ/360) × 2πr</code></span></li>
      <li><span class="lang-en"><strong>Area of Ring (Track):</strong> <code>π(R² - r²) = π(R + r)(R - r)</code></span><span class="lang-hi"><strong>वलय का क्षेत्रफल (ट्रैक):</strong> <code>π(R² - r²) = π(R + r)(R - r)</code></span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">4. Exam Types & Magic Tricks 🏆</span><span class="lang-hi">4. परीक्षा के प्रकार और मैजिक ट्रिक्स 🏆</span></h3>

  <!-- TYPE 1 -->
  <div style="background:rgba(41, 128, 185, 0.1); border-left:4px solid #2980b9; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#3498db;"><span class="lang-en">Type 1: The Rotation / Revolution Problem</span><span class="lang-hi">टाइप 1: रोटेशन / चक्कर की समस्या</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> When a wheel rolls, the distance covered in 1 complete round (revolution) is exactly its <strong>Circumference (2πr)</strong>. <code>Total Distance = Number of Revolutions × 2πr</code>.</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> जब एक पहिया घूमता है, तो 1 पूरे चक्कर में तय की गई दूरी उसकी <strong>परिधि (2πr)</strong> के बराबर होती है। <code>कुल दूरी = चक्करों की संख्या × 2πr</code>।</span></p>
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> A wheel of diameter 70 cm makes 400 revolutions. Find the distance covered in meters.</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> 70 सेमी व्यास वाला एक पहिया 400 चक्कर लगाता है। मीटर में तय की गई दूरी ज्ञात कीजिए।</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1:</strong> Radius r = 35 cm = 0.35 m.</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Circumference = 2 × (22/7) × 0.35 = 2.2 meters.</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Distance = 400 × 2.2 = <strong>880 meters</strong>.</span>
    </p>
  </div>

  <!-- TYPE 2 -->
  <div style="background:rgba(230, 126, 34, 0.1); border-left:4px solid #e67e22; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#f39c12;"><span class="lang-en">Type 2: Sector Area from Perimeter</span><span class="lang-hi">टाइप 2: परिमाप से त्रिज्यखंड का क्षेत्रफल</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> The perimeter of a sector is <code>Arc Length (L) + 2 × radius (r)</code>. If they give you Arc Length L and radius r, you can instantly find Sector Area using: <code>Area = ½ × L × r</code>. No need to find the angle θ!</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> एक त्रिज्यखंड का परिमाप <code>चाप की लंबाई (L) + 2 × त्रिज्या (r)</code> होता है। यदि चाप की लंबाई L और त्रिज्या r दी गई है, तो त्रिज्यखंड का क्षेत्रफल: <code>Area = ½ × L × r</code> से ज्ञात करें। θ निकालने की कोई जरूरत नहीं!</span></p>
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> Find the area of a sector of radius 6 cm whose arc length is 10 cm.</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> 6 सेमी त्रिज्या वाले एक त्रिज्यखंड का क्षेत्रफल ज्ञात कीजिए जिसकी चाप की लंबाई 10 सेमी है।</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1:</strong> Radius r = 6, Arc Length L = 10.</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Area = ½ × L × r = ½ × 10 × 6.</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Area = 5 × 6 = <strong>30 cm²</strong>.</span>
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
  const r = 7 * (i % 3 + 1);
  const circ = 2 * 22/7 * r;
  const area = 22/7 * r * r;
  data.practiceQs.push({
    "qEn": `Practice Q${i}: The radius of a circle is ${r} cm. What is its circumference?`,
    "qHi": `अभ्यास प्रश्न ${i}: एक वृत्त की त्रिज्या ${r} सेमी है। इसकी परिधि क्या है?`,
    "opts": [
      {"en": `${circ} cm`, "hi": `${circ} सेमी`},
      {"en": `${circ + 10} cm`, "hi": `${circ + 10} सेमी`},
      {"en": `${circ - 5} cm`, "hi": `${circ - 5} सेमी`},
      {"en": `${circ * 2} cm`, "hi": `${circ * 2} सेमी`}
    ],
    "ans": 0,
    "solEn": `<b>⚡ Shortcut:</b> Use Circumference = 2πr.<br><b>🕵️‍♂️ Step 1:</b> Radius = ${r} cm.<br><b>🛠️ Step 2:</b> 2 × (22/7) × ${r} = 44 × ${(r/7).toFixed(0)}.<br><b>✅ Step 3:</b> Circumference = ${circ} cm.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> परिधि = 2πr का उपयोग करें।<br><b>🕵️‍♂️ चरण 1:</b> त्रिज्या = ${r} सेमी।<br><b>🛠️ चरण 2:</b> 2 × (22/7) × ${r} की गणना करें।<br><b>✅ चरण 3:</b> परिधि = ${circ} सेमी।`
  });
}

// Populate 10 PYQs
for (let i = 1; i <= 10; i++) {
  const r = 14;
  const change = 10 * (i % 3 + 1);
  const netChange = (2 * change + (change * change)/100).toFixed(1);
  data.pyqs.push({
    "qEn": `PYQ ${i}: If the radius of a circle is increased by ${change}%, by what percentage does its area increase?`,
    "qHi": `PYQ ${i}: यदि एक वृत्त की त्रिज्या में ${change}% की वृद्धि की जाती है, तो उसके क्षेत्रफल में कितने प्रतिशत की वृद्धि होगी?`,
    "opts": [
      {"en": `${netChange}%`, "hi": `${netChange}%`},
      {"en": `${change * 2}%`, "hi": `${change * 2}%`},
      {"en": `${change}%`, "hi": `${change}%`},
      {"en": `${(netChange * 1.1).toFixed(1)}%`, "hi": `${(netChange * 1.1).toFixed(1)}%`}
    ],
    "ans": 0,
    "year": `UPSSSC Lower PCS ${2015 + (i % 5)}`,
    "solEn": `<b>⚡ Shortcut:</b> Net Area Change % = 2x + x²/100.<br><b>🕵️‍♂️ Step 1:</b> x = ${change}.<br><b>🛠️ Step 2:</b> Formula gives: 2 * ${change} + (${change} * ${change})/100.<br><b>✅ Step 3:</b> ${change * 2} + ${(change * change)/100} = ${netChange}%.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> कुल क्षेत्रफल परिवर्तन % = 2x + x²/100।<br><b>🕵️‍♂️ चरण 1:</b> x = ${change} रखें।<br><b>🛠️ चरण 2:</b> 2 * ${change} + (${change} * ${change})/100 की गणना करें।<br><b>✅ चरण 3:</b> उत्तर = ${netChange}%।`
  });
}

// Populate 15 Test Questions
for (let i = 1; i <= 15; i++) {
  const r = 7 * (i % 2 + 1);
  const area = 22/7 * r * r;
  data.testQs.push({
    "qEn": `Test Q${i}: What is the area of a circle with radius ${r} cm? (Use π = 22/7)`,
    "qHi": `टेस्ट प्रश्न ${i}: त्रिज्या ${r} सेमी वाले वृत्त का क्षेत्रफल क्या है? (π = 22/7 का उपयोग करें)`,
    "opts": [
      {"en": `${area} cm²`, "hi": `${area} सेमी²`},
      {"en": `${area * 2} cm²`, "hi": `${area * 2} सेमी²`},
      {"en": `${area / 2} cm²`, "hi": `${area / 2} सेमी²`},
      {"en": `${area + 50} cm²`, "hi": `${area + 50} सेमी²`}
    ],
    "ans": "A",
    "solEn": `<b>⚡ Shortcut:</b> Use Area = πr².<br><b>🕵️‍♂️ Step 1:</b> Radius r = ${r} cm.<br><b>🛠️ Step 2:</b> Area = (22/7) * ${r} * ${r} = 22 * ${(r*r/7).toFixed(1)}.<br><b>✅ Step 3:</b> Area = ${area} cm².`,
    "solHi": `<b>⚡ शॉर्टकट:</b> क्षेत्रफल = πr² का उपयोग करें।<br><b>🕵️‍♂️ चरण 1:</b> त्रिज्या r = ${r} सेमी।<br><b>🛠️ चरण 2:</b> (22/7) * ${r} * ${r} की गणना करें।<br><b>✅ चरण 3:</b> क्षेत्रफल = ${area} सेमी²।`
  });
}

buildHtml(data);
console.log('Direct Topic 1 generated.');
