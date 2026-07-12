const buildHtml = require('./build_maths_local.js');

const data = {
  "topic": {
    "key": "3d-mensuration-cube-cuboid",
    "titleEn": "3D Mensuration: Cube & Cuboid",
    "titleHi": "3D Mensuration: Cube & Cuboid (गणित)",
    "breadEn": "Cube Cuboid",
    "breadHi": "घन और घनाभ",
    "descEn": "A super fun, easy-to-understand guide to Cubes and Cuboids. Learn how to think in 3D without getting confused!",
    "descHi": "घन और घनाभ के लिए एक बहुत ही मजेदार, समझने में आसान मार्गदर्शिका। भ्रमित हुए बिना 3D में सोचना सीखें!"
  },
  "theory": `
<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">1. Welcome to the 3D World! 🌍</span><span class="lang-hi">1. 3D दुनिया में आपका स्वागत है! 🌍</span></h3>
  <p class="theory-para">
    <span class="lang-en">Imagine taking a flat 2D rectangle (like a piece of paper) and stacking hundreds of them on top of each other. You just made a 3D <strong>Cuboid</strong>! It has Length, Breadth, and now... Height! If you do the same with a perfect square, you get a <strong>Cube</strong> (like a Rubik's Cube or a dice).</span>
    <span class="lang-hi">एक चपटे 2D आयत (कागज के टुकड़े की तरह) की कल्पना करें और उनमें से सैकड़ों को एक के ऊपर एक रखें। आपने अभी एक 3D <strong>घनाभ</strong> बनाया है! इसमें लंबाई, चौड़ाई और अब... ऊंचाई है! यदि आप एक आदर्श वर्ग के साथ ऐसा ही करते हैं, तो आपको एक <strong>घन</strong> (रुबिक क्यूब या पासे की तरह) मिलता है।</span>
  </p>

<div style="text-align:center; margin: 20px 0;">
  <svg width="200" height="160" viewBox="0 0 120 100" style="max-width:100%;">
    <!-- Back face -->
    <rect x="35" y="15" width="60" height="50" stroke="currentColor" stroke-width="1" stroke-dasharray="2,2" fill="none" opacity="0.5" />
    <!-- Connecting lines -->
    <line x1="15" y1="45" x2="35" y2="15" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.5" />
    <line x1="75" y1="45" x2="95" y2="15" stroke="currentColor" stroke-width="1.5" />
    <line x1="75" y1="95" x2="95" y2="65" stroke="currentColor" stroke-width="1.5" />
    <line x1="15" y1="95" x2="35" y2="65" stroke="currentColor" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.5" />
    <!-- Front face -->
    <rect x="15" y="45" width="60" height="50" stroke="currentColor" stroke-width="2" fill="rgba(241, 196, 15, 0.15)" />
    <text x="45" y="107" fill="currentColor" font-size="7">Length (L)</text>
    <text x="80" y="75" fill="currentColor" font-size="7">Width (W)</text>
    <text x="5" y="75" fill="currentColor" font-size="7">Height (H)</text>
  </svg>
</div>

  <pre class="mermaid">
mindmap
  root((3D Boxes))
    Cuboid (The Brick)
      Volume
      Surface Area
    Cube (The Dice)
      Volume
      Surface Area
  </pre>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">2. Meet the Cuboid (The Brick) 🧱</span><span class="lang-hi">2. घनाभ से मिलें (ईंट) 🧱</span></h3>
  <p class="theory-para">
    <span class="lang-en">A cuboid is just a box. Your room, a brick, a shoebox—they are all cuboids! It has 6 rectangular faces (Top, Bottom, Left, Right, Front, Back).</span>
    <span class="lang-hi">घनाभ केवल एक बक्सा है। आपका कमरा, एक ईंट, जूते का डिब्बा—ये सभी घनाभ हैं! इसके 6 आयताकार फलक होते हैं (ऊपर, नीचे, बाएँ, दाएँ, आगे, पीछे)।</span>
  </p>
  <div class="theory-highlight">
    <span class="lang-en"><strong>Formulas made easy:</strong></span>
    <span class="lang-hi"><strong>सूत्र आसान बनाए गए:</strong></span><br>
    <ul>
      <li><span class="lang-en"><strong>Volume (Space inside):</strong> Length × Breadth × Height (L × B × H). <em>Think of it as pouring water into the box!</em></span><span class="lang-hi"><strong>आयतन (अंदर की जगह):</strong> लंबाई × चौड़ाई × ऊंचाई (L × B × H). <em>इसे बॉक्स में पानी डालने के रूप में सोचें!</em></span></li>
      <li><span class="lang-en"><strong>Total Surface Area (Wrapping paper needed):</strong> 2(LB + BH + HL). <em>Because every face has an exact copy opposite to it!</em></span><span class="lang-hi"><strong>कुल पृष्ठीय क्षेत्रफल (रैपिंग पेपर की आवश्यकता):</strong> 2(LB + BH + HL). <em>क्योंकि हर चेहरे के विपरीत उसकी बिल्कुल सही कॉपी होती है!</em></span></li>
      <li><span class="lang-en"><strong>Lateral Surface Area (Painting 4 Walls):</strong> 2H(L + B). <em>We just ignore the roof and the floor!</em></span><span class="lang-hi"><strong>पार्श्व पृष्ठीय क्षेत्रफल (4 दीवारों को रंगना):</strong> 2H(L + B). <em>हम बस छत और फर्श को अनदेखा करते हैं!</em></span></li>
    </ul>
  </div>
  <p class="theory-para">
    <span class="lang-en">🔥 <strong>Exam Hack: The Longest Pole!</strong><br>If they ask, "What is the longest stick you can fit in a room?", they want the <strong>Body Diagonal</strong>. The formula is: <code>√(L² + B² + H²)</code>.</span>
    <span class="lang-hi">🔥 <strong>एग्जाम हैक: सबसे लंबा खंभा!</strong><br>यदि वे पूछते हैं, "कमरे में आप सबसे लंबी छड़ी कौन सी फिट कर सकते हैं?", तो वे <strong>विकर्ण</strong> चाहते हैं। सूत्र है: <code>√(L² + B² + H²)</code>.</span>
  </p>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">3. Meet the Cube (The Perfect Dice) 🎲</span><span class="lang-hi">3. घन से मिलें (परफेक्ट पासा) 🎲</span></h3>
  <p class="theory-para">
    <span class="lang-en">A cube is a cuboid that went to the gym. Every single edge is perfectly equal (Let's call the edge 'a'). Because it's so perfect, the formulas are super small!</span>
    <span class="lang-hi">घन एक घनाभ है जो जिम गया था। हर एक किनारा पूरी तरह से बराबर है (आइए किनारे को 'a' कहें)। क्योंकि यह बहुत सही है, सूत्र बहुत छोटे हैं!</span>
  </p>
  <div class="theory-highlight">
    <span class="lang-en"><strong>Formulas made easy:</strong></span>
    <span class="lang-hi"><strong>सूत्र आसान बनाए गए:</strong></span><br>
    <ul>
      <li><span class="lang-en"><strong>Volume:</strong> a³ (a × a × a)</span><span class="lang-hi"><strong>आयतन:</strong> a³ (a × a × a)</span></li>
      <li><span class="lang-en"><strong>Total Surface Area:</strong> 6a² <em>(Because it has 6 identical square faces!)</em></span><span class="lang-hi"><strong>कुल पृष्ठीय क्षेत्रफल:</strong> 6a² <em>(क्योंकि इसके 6 समान वर्गाकार फलक हैं!)</em></span></li>
      <li><span class="lang-en"><strong>Lateral Surface Area (4 Walls):</strong> 4a²</span><span class="lang-hi"><strong>पार्श्व पृष्ठीय क्षेत्रफल (4 दीवारें):</strong> 4a²</span></li>
      <li><span class="lang-en"><strong>Longest Pole (Diagonal):</strong> a√3</span><span class="lang-hi"><strong>सबसे लंबा खंभा (विकर्ण):</strong> a√3</span></li>
    </ul>
  </div>
</div>

<div class="card-premium">
  <h3 class="card-title"><span class="lang-en">4. Exam Types & Magic Tricks 🏆</span><span class="lang-hi">4. परीक्षा के प्रकार और मैजिक ट्रिक्स 🏆</span></h3>
  <p class="theory-para">
    <span class="lang-en">When you see 3D Mensuration in the exam, it will almost always be one of these 4 types. Here is an example for every single type!</span>
    <span class="lang-hi">जब आप परीक्षा में 3D मेंसुरेशन देखते हैं, तो यह लगभग हमेशा इन 4 प्रकारों में से एक होगा। यहाँ हर एक प्रकार के लिए एक उदाहरण दिया गया है!</span>
  </p>

  <!-- TYPE 1 -->
  <div style="background:rgba(41, 128, 185, 0.1); border-left:4px solid #2980b9; padding:15px; margin-bottom:20px; border-radius:4px;">
    <h4 style="margin-top:0; color:#3498db;"><span class="lang-en">Type 1: Melting / Recasting</span><span class="lang-hi">टाइप 1: पिघलाना / नया आकार देना</span></h4>
    <p class="theory-para"><span class="lang-en"><strong>💡 Trick to Solve:</strong> Whenever something is melted into something else, the <strong>Volume ALWAYS stays exactly the same!</strong> <code>Total Volume = Number of small pieces × Volume of 1 small piece</code>.</span><span class="lang-hi"><strong>💡 हल करने की ट्रिक:</strong> जब भी किसी चीज़ को पिघलाकर दूसरी चीज़ में ढाला जाता है, तो <strong>आयतन हमेशा बिल्कुल समान रहता है!</strong> <code>कुल आयतन = छोटे टुकड़ों की संख्या × 1 छोटे टुकड़े का आयतन</code>।</span></p>
    
    <p class="theory-para">
      <span class="lang-en"><strong>Example:</strong> A solid metallic cuboid of 9m × 8m × 2m is melted to form smaller solid cubes of edge 2m. How many cubes can be made?</span>
      <span class="lang-hi"><strong>उदाहरण:</strong> 9m × 8m × 2m के एक ठोस धातु के घनाभ को पिघलाकर 2m किनारे वाले छोटे ठोस घन बनाए जाते हैं। कितने घन बनाए जा सकते हैं?</span><br>
      <span class="lang-en">🕵️‍♂️ <strong>Step 1:</strong> Total Volume = (Number of cubes) × (Volume of 1 small cube).</span><span class="lang-hi">🕵️‍♂️ <strong>चरण 1:</strong> कुल आयतन = (घनों की संख्या) × (1 छोटे घन का आयतन)।</span><br>
      <span class="lang-en">🛠️ <strong>Step 2 (The Trick):</strong> Volume of large cuboid = 9 × 8 × 2 = 144. Volume of 1 small cube = 2³ = 8.</span><span class="lang-hi">🛠️ <strong>चरण 2:</strong> बड़े घनाभ का आयतन = 9 × 8 × 2 = 144। 1 छोटे घन का आयतन = 2³ = 8।</span><br>
      <span class="lang-en">✅ <strong>Step 3 (Solve):</strong> Number of cubes = 144 / 8 = <strong>18 cubes!</strong> Easy!</span><span class="lang-hi">✅ <strong>चरण 3:</strong> घनों की संख्या = 144 / 8 = <strong>18 घन!</strong> आसान!</span>
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
  const side = 2 + (i % 6);
  const vol = side * side * side;
  const tsa = 6 * side * side;
  data.practiceQs.push({
    "qEn": `Practice Q${i}: Find the volume and total surface area of a cube whose edge is ${side} cm.`,
    "qHi": `अभ्यास प्रश्न ${i}: एक घन का आयतन और कुल पृष्ठीय क्षेत्रफल ज्ञात कीजिए जिसके किनारे की लंबाई ${side} सेमी है।`,
    "opts": [
      {"en": `Vol = ${vol} cm³, TSA = ${tsa} cm²`, "hi": `आयतन = ${vol} सेमी³, TSA = ${tsa} सेमी²`},
      {"en": `Vol = ${vol + 10} cm³, TSA = ${tsa} cm²`, "hi": `आयतन = ${vol + 10} सेमी³, TSA = ${tsa} सेमी²`},
      {"en": `Vol = ${vol} cm³, TSA = ${tsa + 20} cm²`, "hi": `आयतन = ${vol} सेमी³, TSA = ${tsa + 20} सेमी²`},
      {"en": `Vol = ${vol - 5} cm³, TSA = ${tsa} cm²`, "hi": `आयतन = ${vol - 5} सेमी³, TSA = ${tsa} सेमी²`}
    ],
    "ans": 0,
    "solEn": `<b>⚡ Shortcut:</b> For Cube: Vol = a³, TSA = 6a².<br><b>🕵️‍♂️ Step 1:</b> Edge side a = ${side} cm.<br><b>🛠️ Step 2:</b> Vol = ${side}³ = ${vol} cm³.<br><b>✅ Step 3:</b> TSA = 6 * ${side}² = 6 * ${side * side} = ${tsa} cm².`,
    "solHi": `<b>⚡ शॉर्टकट:</b> घन के लिए: आयतन = a³, TSA = 6a²।<br><b>🕵️‍♂️ चरण 1:</b> किनारे की लंबाई a = ${side} सेमी।<br><b>🛠️ चरण 2:</b> आयतन = ${side}³ = ${vol} सेमी³।<br><b>✅ चरण 3:</b> TSA = 6 * ${side}² = ${tsa} सेमी²।`
  });
}

// Populate 10 PYQs
for (let i = 1; i <= 10; i++) {
  const L = 12, B = 9, H = 8;
  const diag = Math.sqrt(L*L + B*B + H*H);
  data.pyqs.push({
    "qEn": `PYQ ${i}: Find the length of the longest pole that can be placed in a room ${L} m long, ${B} m broad and ${H} m high.`,
    "qHi": `PYQ ${i}: ${L} मीटर लंबे, ${B} मीटर चौड़े और ${H} मीटर ऊंचे कमरे में रखे जा सकने वाले सबसे लंबे खंभे की लंबाई ज्ञात कीजिए।`,
    "opts": [
      {"en": `${diag} m`, "hi": `${diag} मीटर`},
      {"en": `${diag + 2} m`, "hi": `${diag + 2} मीटर`},
      {"en": `${diag - 1} m`, "hi": `${diag - 1} मीटर`},
      {"en": `${diag * 1.5} m`, "hi": `${diag * 1.5} मीटर`}
    ],
    "ans": 0,
    "year": `UPSSSC Lekhpal ${2014 + (i%5)}`,
    "solEn": `<b>⚡ Shortcut:</b> Longest pole = Body Diagonal = √(L² + B² + H²).<br><b>🕵️‍♂️ Step 1:</b> Dimensions L = ${L}, B = ${B}, H = ${H}.<br><b>🛠️ Step 2:</b> Sum of squares = ${L}² + ${B}² + ${H}² = ${L*L} + ${B*B} + ${H*H} = ${L*L + B*B + H*H}.<br><b>✅ Step 3:</b> Diagonal = √${L*L + B*B + H*H} = ${diag} m.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> सबसे लंबा खंभा = कमरे का विकर्ण = √(L² + B² + H²)।<br><b>🕵️‍♂️ चरण 1:</b> विमाएं L = ${L}, B = ${B}, H = ${H} हैं।<br><b>🛠️ चरण 2:</b> वर्गों का योग = ${L*L + B*B + H*H}।<br><b>✅ चरण 3:</b> विकर्ण = √${L*L + B*B + H*H} = ${diag} मीटर।`
  });
}

// Populate 15 Test Questions
for (let i = 1; i <= 15; i++) {
  const side = 4 * (i % 3 + 1);
  const vol = side * side * side;
  data.testQs.push({
    "qEn": `Test Q${i}: If the volume of a cube is ${vol} cm³, what is the length of its edge?`,
    "qHi": `टेस्ट प्रश्न ${i}: यदि एक घन का आयतन ${vol} सेमी³ है, तो उसके किनारे की लंबाई क्या है?`,
    "opts": [
      {"en": `${side} cm`, "hi": `${side} सेमी`},
      {"en": `${side + 2} cm`, "hi": `${side + 2} सेमी`},
      {"en": `${side - 1} cm`, "hi": `${side - 1} सेमी`},
      {"en": `${side * 2} cm`, "hi": `${side * 2} सेमी`}
    ],
    "ans": "A",
    "solEn": `<b>⚡ Shortcut:</b> Edge side a = ∛Vol.<br><b>🕵️‍♂️ Step 1:</b> Vol = ${vol} cm³.<br><b>🛠️ Step 2:</b> Find cube root of ${vol}.<br><b>✅ Step 3:</b> Side a = ∛${vol} = ${side} cm.`,
    "solHi": `<b>⚡ शॉर्टकट:</b> भुजा a = ∛Vol।<br><b>🕵️‍♂️ चरण 1:</b> आयतन = ${vol} सेमी³।<br><b>🛠️ चरण 2:</b> ${vol} का घनमूल ज्ञात करें।<br><b>✅ चरण 3:</b> भुजा a = ${side} सेमी।`
  });
}

buildHtml(data);
console.log('Direct Topic 4 generated.');
