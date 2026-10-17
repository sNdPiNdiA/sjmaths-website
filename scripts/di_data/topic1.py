"""
topic1.py
Topic 1: Data Interpretation Principles, Calculation Shortcuts & Analysis
Slug: data-interpretation-principles-and-techniques
"""

import json

TOPIC_1 = {
    "slug": "data-interpretation-principles-and-techniques",
    "titleEn": "Data Interpretation Principles, Shortcuts & Analysis",
    "titleHi": "डाटा इंटरप्रिटेशन के सिद्धांत, शॉर्टकट व विश्लेषण",
    "pageTitle": "Data Interpretation Principles, Shortcuts & Analysis | UPSSSC Mains | SJMaths",
    "metaDesc": "Comprehensive pointwise study notes, 30 practice MCQs with step-by-step solutions, and a 15-Q interactive test on Data Interpretation principles, percentage formulas, ratio rules, and speed calculation shortcuts for UPSSSC Intermediate Level Mains 2026.",
    "metaTagEn": "Part-1 (9): Data Interpretation & Statistical Analysis | Principles & Foundations",
    "metaTagHi": "भाग-1 (9): डाटा इंटरप्रिटेशन एवं सांख्यिकीय विश्लेषण | मूल सिद्धांत व अवधारणाएं",
    "subtitleEn": "Exhaustive bilingual study notes covering fraction-percentage tables, speed math shortcuts, approximation rules, ratio conversions, and comprehensive practice sets for UPSSSC Intermediate Level Mains 2026.",
    "subtitleHi": "यूपीएसएसएससी इंटरमीडिएट स्तरीय मुख्य परीक्षा 2026 के लिए भिन्न-प्रतिशत रूपांतरण, तीव्र गणना शॉर्टकट, अनुपात नियम एवं अभ्यास प्रश्नों से युक्त संपूर्ण द्विभाषी अध्ययन नोट्स।",
    "crumbNameEn": "DI Principles & Techniques",
    "crumbNameHi": "डीआई सिद्धांत एवं तकनीकें",
    
    "notesHtml": """
        <!-- Section 1: Core Mathematical Pillars -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-calculator"></i>
                <span class="lang-en">1. Core Mathematical Pillars of Data Interpretation</span>
                <span class="lang-hi">1. डाटा इंटरप्रिटेशन (DI) के मूलभूत गणितीय स्तंभ</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Core Exam Rule:</strong> 95% of all DI questions in UPSSSC exams test only four mathematical concepts: (1) Percentages &amp; Percentage Change, (2) Ratios &amp; Proportions, (3) Averages &amp; Weighted Averages, and (4) Rate of Growth. Mastering these four concepts allows you to solve any chart effortlessly.</span>
                <span class="lang-hi"><strong>परीक्षा हेतु मूल नियम:</strong> यूपीएसएसएससी परीक्षाओं में 95% डीआई प्रश्न केवल चार गणितीय अवधारणाओं पर आधारित होते हैं: (1) प्रतिशत एवं प्रतिशत परिवर्तन, (2) अनुपात एवं समानुपात, (3) औसत एवं भारित औसत, तथा (4) संवृद्धि दर। इन चारों पर पकड़ बनाकर आप किसी भी चार्ट को आसानी से हल कर सकते हैं।</span>
            </div>
            
            <ul class="point-list">
                <li>
                    <span class="key-badge">Percentage Calculation</span>
                    <span class="lang-en"><strong>"What percentage is A of B?"</strong> Formula: <code>(A / B) &times; 100</code>. Note: The quantity following 'of' (or 'का' in Hindi) always forms the denominator (base).</span>
                    <span class="lang-hi"><strong>"A, B का कितना प्रतिशत है?"</strong> सूत्र: <code>(A / B) &times; 100</code>। ध्यान दें: 'का' या 'के संदर्भ में' आने वाली राशि सदैव हर (denominator/base) बनती है।</span>
                </li>
                <li>
                    <span class="key-badge">Percentage Increase</span>
                    <span class="lang-en"><strong>"A is what percent more than B?"</strong> Formula: <code>[(A - B) / B] &times; 100</code>. Here B is the base value because comparison is made with respect to B.</span>
                    <span class="lang-hi"><strong>"A, B से कितना प्रतिशत अधिक है?"</strong> सूत्र: <code>[(A - B) / B] &times; 100</code>। यहाँ B आधार मान है क्योंकि तुलना B के सापेक्ष की जा रही है।</span>
                </li>
                <li>
                    <span class="key-badge">Percentage Decrease</span>
                    <span class="lang-en"><strong>"B is what percent less than A?"</strong> Formula: <code>[(A - B) / A] &times; 100</code>. Here A is the base value because comparison is made with respect to A.</span>
                    <span class="lang-hi"><strong>"B, A से कितना प्रतिशत कम है?"</strong> सूत्र: <code>[(A - B) / A] &times; 100</code>। यहाँ A आधार मान है क्योंकि तुलना A के सापेक्ष की जा रही है।</span>
                </li>
                <li>
                    <span class="key-badge">Ratio & Proportion</span>
                    <span class="lang-en">Ratios represent relative magnitude, not absolute numbers. Ratio of <code>A : B = (Value of A) / (Value of B)</code>. To divide total sum S in ratio <code>a : b</code>, Share of A = <code>[a / (a + b)] &times; S</code> and Share of B = <code>[b / (a + b)] &times; S</code>.</span>
                    <span class="lang-hi">अनुपात सापेक्ष परिमाण को दर्शाता है, वास्तविक संख्याओं को नहीं। <code>A : B = (A का मान) / (B का मान)</code>। कुल राशि S को <code>a : b</code> में बांटने पर A का हिस्सा = <code>[a / (a + b)] &times; S</code> तथा B का हिस्सा = <code>[b / (a + b)] &times; S</code> होता है।</span>
                </li>
                <li>
                    <span class="key-badge">Average & Weighted Average</span>
                    <span class="lang-en">Simple Average = <code>(Sum of all values) / (Total number of items)</code>. Weighted Average when groups have different sizes: <code>X_w = (n1&times;x1 + n2&times;x2 + ... + nk&times;xk) / (n1 + n2 + ... + nk)</code>.</span>
                    <span class="lang-hi">साधारण औसत = <code>(सभी मानों का योग) / (पदों की कुल संख्या)</code>। जब विभिन्न समूहों का आकार भिन्न हो, तो भारित औसत: <code>X_w = (n1&times;x1 + n2&times;x2 + ... + nk&times;xk) / (n1 + n2 + ... + nk)</code>।</span>
                </li>
            </ul>
        </section>

        <!-- Section 2: Fraction to Percentage Conversion Table -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-table"></i>
                <span class="lang-en">2. Essential Fraction-to-Percentage Conversion Table</span>
                <span class="lang-hi">2. अनिवार्य भिन्न-से-प्रतिशत रूपांतरण तालिका</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Speed Tip:</strong> Memorizing fraction equivalents from 1/1 to 1/20 cuts DI calculation time by 60%. For example, instead of dividing 4,800 by 6, simply multiply by 16.67% or recognize that 16.67% of 4,800 is 4,800 / 6 = 800.</span>
                <span class="lang-hi"><strong>स्पीड टिप:</strong> 1/1 से 1/20 तक के भिन्न मानों को याद रखने से डीआई गणना का समय 60% घट जाता है। उदाहरणार्थ, 4,800 का 16.67% निकालने के लिए गुणा करने के बजाय सीधे 4,800 &divide; 6 = 800 करें।</span>
            </div>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Fraction (भिन्न)</span><span class="lang-hi">भिन्न (Fraction)</span></th>
                            <th><span class="lang-en">Percentage Value (%)</span><span class="lang-hi">प्रतिशत मान (%)</span></th>
                            <th><span class="lang-en">Derived Multiples (व्युत्पन्न गुणक)</span><span class="lang-hi">व्युत्पन्न गुणक</span></th>
                            <th><span class="lang-en">Quick Exam Application</span><span class="lang-hi">त्वरित परीक्षा अनुप्रयोग</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>1/2</strong></td>
                            <td>50%</td>
                            <td>2/2 = 100%</td>
                            <td>Half of any value</td>
                        </tr>
                        <tr>
                            <td><strong>1/3</strong></td>
                            <td>33.33% (33 1/3%)</td>
                            <td>2/3 = 66.67% (66 2/3%)</td>
                            <td>One-third / Two-thirds share</td>
                        </tr>
                        <tr>
                            <td><strong>1/4</strong></td>
                            <td>25%</td>
                            <td>3/4 = 75%</td>
                            <td>Quarter / Three-quarter allocation</td>
                        </tr>
                        <tr>
                            <td><strong>1/5</strong></td>
                            <td>20%</td>
                            <td>2/5 = 40%, 3/5 = 60%, 4/5 = 80%</td>
                            <td>Quintile shares in demographic DI</td>
                        </tr>
                        <tr>
                            <td><strong>1/6</strong></td>
                            <td>16.67% (16 2/3%)</td>
                            <td>5/6 = 83.33%</td>
                            <td>Frequent in profit-loss & production</td>
                        </tr>
                        <tr>
                            <td><strong>1/7</strong></td>
                            <td>14.28% (14 2/7%)</td>
                            <td>2/7 = 28.57%, 3/7 = 42.85%, 4/7 = 57.14%</td>
                            <td>Very common in UPSSSC PET / Mains</td>
                        </tr>
                        <tr>
                            <td><strong>1/8</strong></td>
                            <td>12.5% (12 1/2%)</td>
                            <td>3/8 = 37.5%, 5/8 = 62.5%, 7/8 = 87.5%</td>
                            <td>Crucial for pie charts (45&deg; = 12.5%)</td>
                        </tr>
                        <tr>
                            <td><strong>1/9</strong></td>
                            <td>11.11% (11 1/9%)</td>
                            <td>2/9 = 22.22%, 4/9 = 44.44%, 7/9 = 77.77%</td>
                            <td>Notice: 1/9 gives repeating 11s</td>
                        </tr>
                        <tr>
                            <td><strong>1/10</strong></td>
                            <td>10%</td>
                            <td>3/10 = 30%, 7/10 = 70%, 9/10 = 90%</td>
                            <td>Standard baseline calculation</td>
                        </tr>
                        <tr>
                            <td><strong>1/11</strong></td>
                            <td>9.09% (9 1/11%)</td>
                            <td>2/11 = 18.18%, 3/11 = 27.27%, 5/11 = 45.45%</td>
                            <td>Notice: 1/11 gives repeating 9s</td>
                        </tr>
                        <tr>
                            <td><strong>1/12</strong></td>
                            <td>8.33% (8 1/3%)</td>
                            <td>5/12 = 41.67%, 7/12 = 58.33%</td>
                            <td>Monthly share of annual total</td>
                        </tr>
                        <tr>
                            <td><strong>1/13</strong></td>
                            <td>7.69%</td>
                            <td>2/13 = 15.38%</td>
                            <td>Approximated as ~7.7% in rapid options</td>
                        </tr>
                        <tr>
                            <td><strong>1/14</strong></td>
                            <td>7.14%</td>
                            <td>Half of 1/7 (14.28% / 2)</td>
                            <td>Bi-weekly share approximation</td>
                        </tr>
                        <tr>
                            <td><strong>1/15</strong></td>
                            <td>6.67% (6 2/3%)</td>
                            <td>2/15 = 13.33%, 4/15 = 26.67%</td>
                            <td>Frequent in interest/growth problems</td>
                        </tr>
                        <tr>
                            <td><strong>1/16</strong></td>
                            <td>6.25% (6 1/4%)</td>
                            <td>3/16 = 18.75%, 5/16 = 31.25%</td>
                            <td>Half of 1/8 (12.5% / 2)</td>
                        </tr>
                        <tr>
                            <td><strong>1/20</strong></td>
                            <td>5%</td>
                            <td>3/20 = 15%, 7/20 = 35%, 11/20 = 55%</td>
                            <td>Standard 5% bracket calculations</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Section 3: Speed Calculation & Mental Math Techniques -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-bolt"></i>
                <span class="lang-en">3. Mental Math &amp; Approximation Techniques</span>
                <span class="lang-hi">3. मानसिक गणना एवं सन्निकटन (Approximation) तकनीकें</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Golden Rule of DI:</strong> Never calculate the exact decimal value until you look at the options! If options are spaced wide apart (e.g., 22%, 35%, 48%, 65%), rounding off numbers to the nearest tens or hundreds gives the correct answer in 5 seconds.</span>
                <span class="lang-hi"><strong>डीआई का स्वर्णिम नियम:</strong> जब तक विकल्प न देख लें, तब तक सटीक दशमलव मान की गणना न करें! यदि विकल्पों में पर्याप्त अंतर है (उदा. 22%, 35%, 48%, 65%), तो संख्याओं को निकटतम दहाई या सैकड़े में पूर्णांकित करके 5 सेकंड में सही उत्तर प्राप्त किया जा सकता है।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">The 10% &amp; 1% Splitting Technique</span>
                    <span class="lang-en">To find any percentage of a number, break it into 10%, 5%, and 1%. Example: Find 16% of 7,400.
                    <br>&bull; 10% of 7,400 = 740
                    <br>&bull; 5% of 7,400 = 370 (half of 10%)
                    <br>&bull; 1% of 7,400 = 74
                    <br>&bull; Total (16%) = 740 + 370 + 74 = <strong>1,184</strong>. No paper multiplication needed!</span>
                    <span class="lang-hi">किसी भी संख्या का प्रतिशत निकालने के लिए उसे 10%, 5% और 1% में तोड़ें। उदाहरण: 7,400 का 16% निकालें:
                    <br>&bull; 7,400 का 10% = 740
                    <br>&bull; 7,400 का 5% = 370 (10% का आधा)
                    <br>&bull; 7,400 का 1% = 74
                    <br>&bull; कुल (16%) = 740 + 370 + 74 = <strong>1,184</strong>। किसी कठिन गुणा की आवश्यकता नहीं!</span>
                </li>
                <li>
                    <span class="key-badge">Comparing Fractions Without Cross-Multiplying</span>
                    <span class="lang-en">To compare two fractions <code>A/B</code> and <code>C/D</code>:
                    <br>1. If Numerator increases while Denominator decreases &rarr; fraction increases definitely.
                    <br>2. Percentage change method: If Numerator grows by +20% but Denominator grows by +40%, the overall fraction has decreased!</span>
                    <span class="lang-hi">दो भिन्नों <code>A/B</code> और <code>C/D</code> की तुलना:
                    <br>1. यदि अंश बढ़ता है और हर घटता है &rarr; भिन्न का मान निश्चित रूप से बढ़ेगा।
                    <br>2. प्रतिशत परिवर्तन विधि: यदि अंश में +20% की वृद्धि होती है लेकिन हर में +40% की वृद्धि होती है, तो समग्र भिन्न का मान घट जाएगा!</span>
                </li>
                <li>
                    <span class="key-badge">Unit Multiplier Traps</span>
                    <span class="lang-en">Always verify the scale unit given in headers: 
                    <br>&bull; 1 Lakh = 100,000 = 10^5
                    <br>&bull; 1 Crore = 100 Lakhs = 10,000,000 = 10^7
                    <br>&bull; 1 Million = 10 Lakhs = 10^6
                    <br>&bull; 1 Billion = 1,000 Million = 100 Crores = 10^9
                    <br>Misreading Lakhs for Crores is the #1 reason candidates mark wrong options in UPSSSC.</span>
                    <span class="lang-hi">हमेशा शीर्षकों में दी गई इकाई की पुष्टि करें:
                    <br>&bull; 1 लाख = 100,000 = 10^5
                    <br>&bull; 1 करोड़ = 100 लाख = 10,000,000 = 10^7
                    <br>&bull; 1 मिलियन = 10 लाख = 10^6
                    <br>&bull; 1 बिलियन = 1,000 मिलियन = 100 करोड़ = 10^9
                    <br>लाख को करोड़ समझ लेना यूपीएसएसएससी में गलत उत्तर देने का सबसे प्रमुख कारण है।</span>
                </li>
            </ul>
        </section>

        <!-- Section 4: Advanced Percentage Concepts & Exam Traps -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-percentage"></i>
                <span class="lang-en">4. Advanced Percentage Concepts &amp; Exam Traps</span>
                <span class="lang-hi">4. उन्नत प्रतिशत अवधारणाएं एवं परीक्षा जाल</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Percentage Points vs. Percentage Increase:</strong> If an interest rate changes from 5% to 8%, it increased by <strong>3 percentage points</strong> (8 - 5 = 3), BUT the <strong>percentage increase</strong> is <code>[(8 - 5) / 5] &times; 100 = 60%</code>! Conflating these two is the single most frequent error candidates commit in UPSSSC mains.</span>
                <span class="lang-hi"><strong>प्रतिशत अंक बनाम प्रतिशत वृद्धि:</strong> यदि ब्याज दर 5% से बढ़कर 8% हो जाती है, तो इसमें <strong>3 प्रतिशत अंकों</strong> की वृद्धि हुई (8 - 5 = 3), लेकिन <strong>प्रतिशत वृद्धि</strong> <code>[(8 - 5) / 5] &times; 100 = 60%</code> है! इन दोनों में भ्रमित होना यूपीएसएसएससी मुख्य परीक्षा में अभ्यर्थियों द्वारा की जाने वाली सबसे सामान्य गलती है।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Successive Percentage Change Formula</span>
                    <span class="lang-en">When a quantity changes by <code>a%</code> and subsequently by <code>b%</code>, the net percentage change is:
                    <br><code>Net % Change = a + b + (a &times; b / 100)</code>
                    <br>&bull; If both increase (+a, +b): <code>Net = a + b + (ab / 100)</code>
                    <br>&bull; If one increases and one decreases (+a, -b): <code>Net = a - b - (ab / 100)</code>
                    <br>&bull; If both decrease (-a, -b): <code>Net = -a - b + (ab / 100)</code>
                    <br><em>Exam Example:</em> If salary increases by 20% and then by 10%, overall increase = <code>20 + 10 + (200 / 100) = 32%</code> (NOT 30%!).</span>
                    <span class="lang-hi">जब कोई राशि पहले <code>a%</code> तथा बाद में <code>b%</code> परिवर्तित होती है, तो शुद्ध प्रतिशत परिवर्तन:
                    <br><code>शुद्ध % परिवर्तन = a + b + (a &times; b / 100)</code>
                    <br>&bull; दोनों में वृद्धि (+a, +b): <code>Net = a + b + (ab / 100)</code>
                    <br>&bull; एक वृद्धि व एक कमी (+a, -b): <code>Net = a - b - (ab / 100)</code>
                    <br>&bull; दोनों में कमी (-a, -b): <code>Net = -a - b + (ab / 100)</code>
                    <br><em>परीक्षा उदाहरण:</em> यदि वेतन में पहले 20% तथा बाद में 10% की वृद्धि होती है, तो कुल वृद्धि = <code>20 + 10 + 2 = 32%</code> (न कि 30%!)।</span>
                </li>
                <li>
                    <span class="key-badge">Base Shifting Technique</span>
                    <span class="lang-en">If A is <code>x%</code> more than B, then B is <code>[x / (100 + x)] &times; 100%</code> less than A.
                    <br>Similarly, if A is <code>x%</code> less than B, then B is <code>[x / (100 - x)] &times; 100%</code> more than A.
                    <br><em>Example:</em> If A's salary is 25% more than B's salary, B's salary is <code>[25 / 125] &times; 100 = 20%</code> less than A's salary.</span>
                    <span class="lang-hi">यदि A, B से <code>x%</code> अधिक है, तो B, A से <code>[x / (100 + x)] &times; 100%</code> कम है।
                    <br>इसी प्रकार यदि A, B से <code>x%</code> कम है, तो B, A से <code>[x / (100 - x)] &times; 100%</code> अधिक है।
                    <br><em>उदाहरण:</em> यदि A का वेतन B से 25% अधिक है, तो B का वेतन A से <code>[25 / 125] &times; 100 = 20%</code> कम है।</span>
                </li>
            </ul>
        </section>

        <!-- Section 5: The Product Constancy (Reciprocal) Master Table -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-balance-scale"></i>
                <span class="lang-en">5. Product Constancy &amp; Inverse Proportionality Table</span>
                <span class="lang-hi">5. गुणनफल स्थिरता एवं व्युत्क्रमानुपात तालिका</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Product Constancy Rule:</strong> Whenever <code>A &times; B = Constant</code> (e.g., <code>Price &times; Consumption = Expenditure</code>, or <code>Speed &times; Time = Distance</code>):
                <br>If A increases by fraction <code>1/n</code> (or <code>a/b</code>), then B must decrease by <code>1/(n + 1)</code> (or <code>a/(a + b)</code>) to keep the total product unchanged.</span>
                <span class="lang-hi"><strong>गुणनफल स्थिरता नियम:</strong> जब भी <code>A &times; B = नियतांक</code> हो (उदा. <code>मूल्य &times; खपत = कुल व्यय</code>, या <code>चाल &times; समय = दूरी</code>):
                <br>यदि A में <code>1/n</code> (या <code>a/b</code>) की वृद्धि होती है, तो गुणनफल को स्थिर रखने हेतु B में <code>1/(n + 1)</code> (या <code>a/(a + b)</code>) की कमी होनी चाहिए।</span>
            </div>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Factor A Increase (+%)</span><span class="lang-hi">कारक A में वृद्धि (+%)</span></th>
                            <th><span class="lang-en">Fractional Increase</span><span class="lang-hi">भिन्न वृद्धि (+a/b)</span></th>
                            <th><span class="lang-en">Fractional Decrease</span><span class="lang-hi">भिन्न कमी (-a/(a+b))</span></th>
                            <th><span class="lang-en">Factor B Decrease (-%)</span><span class="lang-hi">कारक B में आवश्यक कमी (-%)</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr><td><strong>+100%</strong></td><td>+1/1</td><td>-1/2</td><td><strong>-50.00%</strong></td></tr>
                        <tr><td><strong>+50%</strong></td><td>+1/2</td><td>-1/3</td><td><strong>-33.33%</strong></td></tr>
                        <tr><td><strong>+33.33%</strong></td><td>+1/3</td><td>-1/4</td><td><strong>-25.00%</strong></td></tr>
                        <tr><td><strong>+25%</strong></td><td>+1/4</td><td>-1/5</td><td><strong>-20.00%</strong></td></tr>
                        <tr><td><strong>+20%</strong></td><td>+1/5</td><td>-1/6</td><td><strong>-16.67%</strong></td></tr>
                        <tr><td><strong>+16.67%</strong></td><td>+1/6</td><td>-1/7</td><td><strong>-14.28%</strong></td></tr>
                        <tr><td><strong>+14.28%</strong></td><td>+1/7</td><td>-1/8</td><td><strong>-12.50%</strong></td></tr>
                        <tr><td><strong>+12.50%</strong></td><td>+1/8</td><td>-1/9</td><td><strong>-11.11%</strong></td></tr>
                        <tr><td><strong>+11.11%</strong></td><td>+1/9</td><td>-1/10</td><td><strong>-10.00%</strong></td></tr>
                        <tr><td><strong>+10%</strong></td><td>+1/10</td><td>-1/11</td><td><strong>-9.09%</strong></td></tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Section 6: Weighted Averages, Alligation & Rapid Fraction Rules -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-divide"></i>
                <span class="lang-en">6. Weighted Averages, Alligation &amp; Rapid Fraction Comparison</span>
                <span class="lang-hi">6. भारित औसत, मिश्रण (Alligation) एवं तीव्र भिन्न तुलना नियम</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Four Rapid Fraction Comparison Rules:</strong>
                <br>1. <strong>Identical Denominator:</strong> <code>7/15 > 4/15</code> (Higher numerator is larger).
                <br>2. <strong>Identical Numerator:</strong> <code>11/17 > 11/23</code> (Smaller denominator is larger).
                <br>3. <strong>Constant Difference Rule:</strong> If difference <code>(Denominator - Numerator) = k</code> is constant for all proper fractions: <code>11/13 > 9/11 > 7/9 > 5/7</code> (Fraction with highest values is largest).
                <br>4. <strong>Cross-Multiplication Rule:</strong> To compare <code>a/b</code> and <code>c/d</code>, compare <code>(a &times; d)</code> with <code>(b &times; c)</code>. If <code>a &times; d > b &times; c</code>, then <code>a/b > c/d</code>.</span>
                <span class="lang-hi"><strong>तीव्र भिन्न तुलना के चार अचूक नियम:</strong>
                <br>1. <strong>समान हर:</strong> <code>7/15 > 4/15</code> (बड़ा अंश वाली भिन्न बड़ी होती है)।
                <br>2. <strong>समान अंश:</strong> <code>11/17 > 11/23</code> (छोटा हर वाली भिन्न बड़ी होती है)।
                <br>3. <strong>समान अंतर नियम:</strong> यदि सभी उचित भिन्नों में <code>(हर - अंश) = k</code> समान हो: <code>11/13 > 9/11 > 7/9 > 5/7</code> (बड़े अंकों वाली भिन्न सबसे बड़ी होती है)।
                <br>4. <strong>तिर्यक गुणा नियम (Cross-multiplication):</strong> <code>a/b</code> और <code>c/d</code> की तुलना हेतु <code>(a &times; d)</code> व <code>(b &times; c)</code> की तुलना करें। यदि <code>a &times; d > b &times; c</code>, तो <code>a/b > c/d</code>।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Alligation Method in DI Percentages</span>
                    <span class="lang-en">When two sub-groups with percentage attributes <code>P1</code> and <code>P2</code> combine into an overall average <code>P_avg</code>, the ratio of their weights is given by:
                    <br><code>n1 : n2 = (P2 - P_avg) : (P_avg - P1)</code>.
                    <br><em>Exam Application:</em> If male literacy in a district is 80%, female literacy is 60%, and total literacy is 72%, the ratio of males to females is <code>(72 - 60) : (80 - 72) = 12 : 8 = 3 : 2</code>. Solved in 3 seconds!</span>
                    <span class="lang-hi">जब प्रतिशत गुणधर्म <code>P1</code> और <code>P2</code> वाले दो समूह मिलकर कुल औसत <code>P_avg</code> बनाते हैं, तो उनके आकार का अनुपात:
                    <br><code>n1 : n2 = (P2 - P_avg) : (P_avg - P1)</code>।
                    <br><em>परीक्षा अनुप्रयोग:</em> यदि पुरुष साक्षरता 80%, महिला साक्षरता 60% और कुल साक्षरता 72% है, तो पुरुष व महिला जनसंख्या का अनुपात = <code>(72 - 60) : (80 - 72) = 12 : 8 = 3 : 2</code>। केवल 3 सेकंड में हल!</span>
                </li>
                <li>
                    <span class="key-badge">AAGR vs CAGR</span>
                    <span class="lang-en"><strong>Average Annual Growth Rate (AAGR):</strong> <code>AAGR = (Total % Change) / (Number of Intervals)</code>.
                    <br><strong>Compound Annual Growth Rate (CAGR):</strong> <code>CAGR = [(Final Value / Initial Value)^(1/t) - 1] &times; 100</code>.
                    <br><em>Exam Rule:</em> In UPSSSC DI questions, whenever examiners write "वार्षिक औसत संवृद्धि दर" (average annual growth rate), they mean AAGR unless "चक्रवृद्धि" (compound) is explicitly specified.</span>
                    <span class="lang-hi"><strong>औसत वार्षिक संवृद्धि दर (AAGR):</strong> <code>AAGR = (कुल % परिवर्तन) / (अंतरालों की संख्या)</code>।
                    <br><strong>चक्रवृद्धि वार्षिक संवृद्धि दर (CAGR):</strong> <code>CAGR = [(अंतिम मान / प्रारंभिक मान)^(1/t) - 1] &times; 100</code>।
                    <br><em>परीक्षा नियम:</em> यूपीएसएसएससी में जब तक "चक्रवृद्धि" शब्द न लिखा हो, तब तक "औसत वार्षिक वृद्धि दर" का अर्थ साधारण AAGR ही होता है।</span>
                </li>
            </ul>
        </section>

        <!-- Section 7: Visual Graphic Overview of DI Formats -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-chart-pie"></i>
                <span class="lang-en">7. The Four Primary Graphic Displays in DI</span>
                <span class="lang-hi">7. डीआई में चार प्रमुख आरेखीय निरूपण</span>
            </h2>
            <p>
                <span class="lang-en">Examiners present numerical data across four standard formats. Below is an architectural overview of how to approach each display format:</span>
                <span class="lang-hi">परीक्षक चार मानक प्रारूपों में संख्यात्मक डेटा प्रस्तुत करते हैं। प्रत्येक आरेख प्रारूप को हल करने का संरचनात्मक अवलोकन नीचे दिया गया है:</span>
            </p>

            <!-- SVG Visual Diagram -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 1.1: Visual Hierarchy of Data Interpretation Displays</span>
                    <span class="lang-hi">चित्र 1.1: डाटा इंटरप्रिटेशन आरेख प्रारूपों का तुलनात्मक मानचित्र</span>
                </h4>
                <svg viewBox="0 0 680 260" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Visual Overview of DI Types">
                    <!-- Background subtle boxes -->
                    <!-- Box 1: Tables -->
                    <rect x="15" y="20" width="150" height="210" rx="10" fill="#f0fdfa" stroke="#0d9488" stroke-width="2"/>
                    <text x="90" y="55" fill="#0f766e" font-size="16" font-weight="bold" text-anchor="middle">1. Tables (सारणी)</text>
                    <line x1="30" y1="70" x2="150" y2="70" stroke="#0d9488" stroke-width="1.5"/>
                    <text x="90" y="95" fill="#3e5047" font-size="12" text-anchor="middle">Precise cell data</text>
                    <text x="90" y="115" fill="#3e5047" font-size="12" text-anchor="middle">Row/Column sums</text>
                    <text x="90" y="135" fill="#3e5047" font-size="12" text-anchor="middle">Missing data grids</text>
                    <text x="90" y="170" fill="#0d9488" font-size="13" font-weight="bold" text-anchor="middle">Best For:</text>
                    <text x="90" y="190" fill="#182e26" font-size="11" text-anchor="middle">Exact values &amp; ratios</text>

                    <!-- Box 2: Bar Graphs -->
                    <rect x="180" y="20" width="150" height="210" rx="10" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
                    <text x="255" y="55" fill="#1d4ed8" font-size="16" font-weight="bold" text-anchor="middle">2. Bar Charts (दंड)</text>
                    <line x1="195" y1="70" x2="315" y2="70" stroke="#2563eb" stroke-width="1.5"/>
                    <text x="255" y="95" fill="#3e5047" font-size="12" text-anchor="middle">Discrete categories</text>
                    <text x="255" y="115" fill="#3e5047" font-size="12" text-anchor="middle">Grouped comparisons</text>
                    <text x="255" y="135" fill="#3e5047" font-size="12" text-anchor="middle">Stacked totals</text>
                    <text x="255" y="170" fill="#2563eb" font-size="13" font-weight="bold" text-anchor="middle">Best For:</text>
                    <text x="255" y="190" fill="#182e26" font-size="11" text-anchor="middle">Direct visual height</text>

                    <!-- Box 3: Line Graphs -->
                    <rect x="345" y="20" width="150" height="210" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
                    <text x="420" y="55" fill="#b45309" font-size="16" font-weight="bold" text-anchor="middle">3. Line Graphs (रेखा)</text>
                    <line x1="360" y1="70" x2="480" y2="70" stroke="#d97706" stroke-width="1.5"/>
                    <text x="420" y="95" fill="#3e5047" font-size="12" text-anchor="middle">Continuous trends</text>
                    <text x="420" y="115" fill="#3e5047" font-size="12" text-anchor="middle">Time-series data</text>
                    <text x="420" y="135" fill="#3e5047" font-size="12" text-anchor="middle">Slope = Rate of change</text>
                    <text x="420" y="170" fill="#d97706" font-size="13" font-weight="bold" text-anchor="middle">Best For:</text>
                    <text x="420" y="190" fill="#182e26" font-size="11" text-anchor="middle">Growth &amp; fluctuations</text>

                    <!-- Box 4: Pie Charts -->
                    <rect x="510" y="20" width="155" height="210" rx="10" fill="#fdf2f8" stroke="#db2777" stroke-width="2"/>
                    <text x="587" y="55" fill="#be185d" font-size="16" font-weight="bold" text-anchor="middle">4. Pie Charts (वृत्त)</text>
                    <line x1="525" y1="70" x2="650" y2="70" stroke="#db2777" stroke-width="1.5"/>
                    <text x="587" y="95" fill="#3e5047" font-size="12" text-anchor="middle">Proportion of a whole</text>
                    <text x="587" y="115" fill="#3e5047" font-size="12" text-anchor="middle">360&deg; = 100% total</text>
                    <text x="587" y="135" fill="#3e5047" font-size="12" text-anchor="middle">Dual pie comparisons</text>
                    <text x="587" y="170" fill="#db2777" font-size="13" font-weight="bold" text-anchor="middle">Best For:</text>
                    <text x="587" y="190" fill="#182e26" font-size="11" text-anchor="middle">Percentage shares</text>
                </svg>
            </div>
        </section>

        <!-- Section 8: Step-by-Step 5-Question Exemplar Case Study -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-tasks"></i>
                <span class="lang-en">8. Comprehensive Worked Exemplar Case Study</span>
                <span class="lang-hi">8. विस्तृत हल सहित आदर्श केस स्टडी</span>
            </h2>
            <p>
                <span class="lang-en">Study the table below showing the production (in thousands) of 4 smartphone models by Alpha Technologies from 2021 to 2024, and examine the step-by-step mathematical reasoning for 5 standard question models:</span>
                <span class="lang-hi">अल्फा टेक्नोलॉजीज द्वारा 2021 से 2024 तक 4 स्मार्टफोन मॉडलों के उत्पादन (हजारों में) को दर्शाने वाली निम्नलिखित तालिका का अध्ययन करें और 5 मानक परीक्षा प्रश्नों का चरणबद्ध गणितीय हल समझें:</span>
            </p>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Model (मॉडल)</span><span class="lang-hi">मॉडल</span></th>
                            <th><span class="lang-en">2021</span><span class="lang-hi">2021</span></th>
                            <th><span class="lang-en">2022</span><span class="lang-hi">2022</span></th>
                            <th><span class="lang-en">2023</span><span class="lang-hi">2023</span></th>
                            <th><span class="lang-en">2024</span><span class="lang-hi">2024</span></th>
                            <th><span class="lang-en">Total (कुल)</span><span class="lang-hi">कुल</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Alpha Pro</strong></td>
                            <td>40</td>
                            <td>50</td>
                            <td>60</td>
                            <td>75</td>
                            <td><strong>225</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Alpha Air</strong></td>
                            <td>30</td>
                            <td>45</td>
                            <td>40</td>
                            <td>55</td>
                            <td><strong>170</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Alpha Lite</strong></td>
                            <td>60</td>
                            <td>65</td>
                            <td>80</td>
                            <td>95</td>
                            <td><strong>300</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Alpha Max</strong></td>
                            <td>20</td>
                            <td>25</td>
                            <td>30</td>
                            <td>35</td>
                            <td><strong>110</strong></td>
                        </tr>
                        <tr style="background:var(--planner-primary-light);font-weight:bold;">
                            <td><strong>Total (कुल)</strong></td>
                            <td><strong>150</strong></td>
                            <td><strong>185</strong></td>
                            <td><strong>210</strong></td>
                            <td><strong>260</strong></td>
                            <td><strong>805</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="exam-pointer" style="background:var(--planner-bg-surface);border-left:4px solid var(--planner-primary);">
                <h4><span class="lang-en">Step-by-Step Question Model Walkthroughs:</span><span class="lang-hi">प्रश्नों के चरणबद्ध हल का विश्लेषण:</span></h4>
                <ol style="margin-left:20px;line-height:1.75;">
                    <li>
                        <strong><span class="lang-en">Percentage Share:</span><span class="lang-hi">प्रतिशत हिस्सेदारी:</span></strong>
                        <span class="lang-en">What percentage of total 2024 production was contributed by Alpha Lite?
                        <br>&bull; Calculation: <code>(95 / 260) &times; 100 = (95 / 26) &times; 10 &approx; 36.54%</code>.</span>
                        <span class="lang-hi">2024 के कुल उत्पादन में अल्फा लाइट का योगदान कितना प्रतिशत था?
                        <br>&bull; गणना: <code>(95 / 260) &times; 100 = (95 / 26) &times; 10 &approx; 36.54%</code>।</span>
                    </li>
                    <li>
                        <strong><span class="lang-en">Percentage Growth:</span><span class="lang-hi">प्रतिशत संवृद्धि:</span></strong>
                        <span class="lang-en">What was the percentage growth in production of Alpha Pro from 2021 to 2024?
                        <br>&bull; Calculation: <code>[(75 - 40) / 40] &times; 100 = (35 / 40) &times; 100 = 7/8 &times; 100 = 87.5%</code>. (Using fraction 7/8 shortcut!).</span>
                        <span class="lang-hi">2021 से 2024 तक अल्फा प्रो के उत्पादन में प्रतिशत वृद्धि कितनी रही?
                        <br>&bull; गणना: <code>[(75 - 40) / 40] &times; 100 = (35 / 40) &times; 100 = 7/8 &times; 100 = 87.5%</code> (7/8 भिन्न शॉर्टकट द्वारा!)।</span>
                    </li>
                    <li>
                        <strong><span class="lang-en">Ratio Comparison:</span><span class="lang-hi">अनुपात तुलना:</span></strong>
                        <span class="lang-en">Find the ratio of total production of Alpha Air to Alpha Max over the entire 4-year period.
                        <br>&bull; Calculation: Total Air = 170; Total Max = 110. Ratio = <code>170 : 110 = 17 : 11</code>.</span>
                        <span class="lang-hi">संपूर्ण 4 वर्षों में अल्फा एयर और अल्फा मैक्स के कुल उत्पादन का अनुपात क्या है?
                        <br>&bull; गणना: कुल एयर = 170; कुल मैक्स = 110। अनुपात = <code>170 : 110 = 17 : 11</code>।</span>
                    </li>
                    <li>
                        <strong><span class="lang-en">Annual Average:</span><span class="lang-hi">वार्षिक औसत:</span></strong>
                        <span class="lang-en">What is the average annual production of Alpha Lite from 2021 to 2024?
                        <br>&bull; Calculation: Total Lite = 300; Years = 4. Average = <code>300 / 4 = 75 thousand units</code>.</span>
                        <span class="lang-hi">2021 से 2024 तक अल्फा लाइट का औसत वार्षिक उत्पादन कितना है?
                        <br>&bull; गणना: कुल लाइट = 300; वर्ष = 4। औसत = <code>300 / 4 = 75 हजार इकाइयां</code>।</span>
                    </li>
                    <li>
                        <strong><span class="lang-en">Relative Comparison:</span><span class="lang-hi">सापेक्ष तुलना:</span></strong>
                        <span class="lang-en">The production of Alpha Pro in 2023 was what percent more than the production of Alpha Air in 2022?
                        <br>&bull; Alpha Pro 2023 = 60; Alpha Air 2022 = 45.
                        <br>&bull; Difference = 60 - 45 = 15. Base is Air 2022 (45).
                        <br>&bull; Percentage More = <code>(15 / 45) &times; 100 = (1/3) &times; 100 = 33.33%</code>.</span>
                        <span class="lang-hi">2023 में अल्फा प्रो का उत्पादन 2022 में अल्फा एयर के उत्पादन से कितना प्रतिशत अधिक था?
                        <br>&bull; अल्फा प्रो 2023 = 60; अल्फा एयर 2022 = 45।
                        <br>&bull; अंतर = 60 - 45 = 15। आधार एयर 2022 (45) है।
                        <br>&bull; प्रतिशत अधिक = <code>(15 / 45) &times; 100 = (1/3) &times; 100 = 33.33%</code>।</span>
                    </li>
                </ol>
            </div>
        </section>
    """,

    # 30 Curated Practice Questions with complete steps
    "practiceQuestions": [
        {
            "tag": "Percentage Base",
            "qEn": "If salary of A is ₹25,000 and salary of B is ₹30,000, by what percent is B's salary greater than A's salary?",
            "qHi": "यदि A का वेतन ₹25,000 है तथा B का वेतन ₹30,000 है, तो B का वेतन A के वेतन से कितने प्रतिशत अधिक है?",
            "opts": [
                ("A", "16.67%", "16.67%"),
                ("B", "20.00%", "20.00%"),
                ("C", "25.00%", "25.00%"),
                ("D", "15.00%", "15.00%")
            ],
            "ans": "B",
            "solEn": "Difference = 30,000 - 25,000 = 5,000. Base is A's salary (25,000). Percentage greater = (5,000 / 25,000) &times; 100 = 1/5 &times; 100 = 20.00%.",
            "solHi": "अंतर = 30,000 - 25,000 = 5,000। आधार A का वेतन (25,000) है। प्रतिशत अधिक = (5,000 / 25,000) &times; 100 = 1/5 &times; 100 = 20.00%।"
        },
        {
            "tag": "Percentage Base",
            "qEn": "In the question above, by what percent is A's salary less than B's salary?",
            "qHi": "उपरोक्त प्रश्न में, A का वेतन B के वेतन से कितने प्रतिशत कम है?",
            "opts": [
                ("A", "20.00%", "20.00%"),
                ("B", "16.67%", "16.67%"),
                ("C", "15.00%", "15.00%"),
                ("D", "12.50%", "12.50%")
            ],
            "ans": "B",
            "solEn": "Difference = 5,000. Here the base is B's salary (30,000). Percentage less = (5,000 / 30,000) &times; 100 = 1/6 &times; 100 = 16.67%.",
            "solHi": "अंतर = 5,000। यहाँ आधार B का वेतन (30,000) है। प्रतिशत कम = (5,000 / 30,000) &times; 100 = 1/6 &times; 100 = 16.67%।"
        },
        {
            "tag": "Fraction Equivalent",
            "qEn": "What is the fractional equivalent of 37.5%?",
            "qHi": "37.5% का भिन्न मान (fractional equivalent) क्या है?",
            "opts": [
                ("A", "3/8", "3/8"),
                ("B", "5/8", "5/8"),
                ("C", "3/16", "3/16"),
                ("D", "7/16", "7/16")
            ],
            "ans": "A",
            "solEn": "Since 1/8 = 12.5%, 3 &times; (1/8) = 3 &times; 12.5% = 37.5%. Hence, the fraction is 3/8.",
            "solHi": "चूंकि 1/8 = 12.5% होता है, अतः 3 &times; (1/8) = 3 &times; 12.5% = 37.5%। अतः भिन्न मान 3/8 है।"
        },
        {
            "tag": "Fraction Equivalent",
            "qEn": "What is 83.33% of 7,200?",
            "qHi": "7,200 का 83.33% कितना होगा?",
            "opts": [
                ("A", "5,400", "5,400"),
                ("B", "6,000", "6,000"),
                ("C", "6,200", "6,200"),
                ("D", "5,800", "5,800")
            ],
            "ans": "B",
            "solEn": "83.33% is equivalent to 5/6 (or 100% - 16.67% = 1 - 1/6 = 5/6). Value = (5/6) &times; 7,200 = 5 &times; 1,200 = 6,000.",
            "solHi": "83.33% भिन्न मान 5/6 के बराबर होता है (या 100% - 16.67% = 1 - 1/6 = 5/6)। मान = (5/6) &times; 7,200 = 5 &times; 1,200 = 6,000।"
        },
        {
            "tag": "Mental Math Split",
            "qEn": "Find 23% of 4,500 using the splitting method.",
            "qHi": "विभाजन विधि (splitting method) का उपयोग करके 4,500 का 23% ज्ञात कीजिए।",
            "opts": [
                ("A", "1,035", "1,035"),
                ("B", "1,015", "1,015"),
                ("C", "1,055", "1,055"),
                ("D", "985", "985")
            ],
            "ans": "A",
            "solEn": "23% = 20% + 3%. 10% of 4,500 = 450 &rarr; 20% = 900. 1% of 4,500 = 45 &rarr; 3% = 135. Total = 900 + 135 = 1,035.",
            "solHi": "23% = 20% + 3%। 4,500 का 10% = 450 &rarr; 20% = 900। 4,500 का 1% = 45 &rarr; 3% = 135। कुल = 900 + 135 = 1,035।"
        },
        {
            "tag": "Ratio Division",
            "qEn": "An amount of ₹72,000 is divided among X, Y, and Z in the ratio 3 : 4 : 5. What is the share of Y?",
            "qHi": "₹72,000 की राशि को X, Y और Z में 3 : 4 : 5 के अनुपात में विभाजित किया जाता है। Y का हिस्सा क्या है?",
            "opts": [
                ("A", "₹18,000", "₹18,000"),
                ("B", "₹24,000", "₹24,000"),
                ("C", "₹30,000", "₹30,000"),
                ("D", "₹27,000", "₹27,000")
            ],
            "ans": "B",
            "solEn": "Sum of ratio terms = 3 + 4 + 5 = 12. Y's share = (4 / 12) &times; 72,000 = (1/3) &times; 72,000 = ₹24,000.",
            "solHi": "अनुपाती पदों का योग = 3 + 4 + 5 = 12। Y का हिस्सा = (4 / 12) &times; 72,000 = (1/3) &times; 72,000 = ₹24,000।"
        },
        {
            "tag": "Ratio Comparison",
            "qEn": "Which of the following fractions has the highest value: 5/7, 7/9, 9/11, 11/13?",
            "qHi": "निम्नलिखित में से किस भिन्न का मान सर्वाधिक है: 5/7, 7/9, 9/11, 11/13?",
            "opts": [
                ("A", "5/7", "5/7"),
                ("B", "7/9", "7/9"),
                ("C", "9/11", "9/11"),
                ("D", "11/13", "11/13")
            ],
            "ans": "D",
            "solEn": "Rule: When the difference between numerator and denominator is equal (here 2 for all proper fractions), the fraction with the largest numerator has the highest value. 11/13 &approx; 0.846 > 9/11 (0.818) > 7/9 (0.778) > 5/7 (0.714).",
            "solHi": "नियम: जब उचित भिन्नों में अंश और हर का अंतर समान हो (यहाँ सभी में अंतर 2 है), तो सबसे बड़े अंश वाली भिन्न का मान सबसे अधिक होता है। 11/13 &approx; 0.846 > 9/11 > 7/9 > 5/7।"
        },
        {
            "tag": "Weighted Average",
            "qEn": "In a college, Section A has 40 students with average score 65, and Section B has 60 students with average score 75. What is the combined average score?",
            "qHi": "एक कॉलेज में, सेक्शन A में 40 छात्र हैं जिनका औसत प्राप्तांक 65 है, और सेक्शन B में 60 छात्र हैं जिनका औसत प्राप्तांक 75 है। दोनों का संयुक्त औसत प्राप्तांक क्या है?",
            "opts": [
                ("A", "70.0", "70.0"),
                ("B", "71.0", "71.0"),
                ("C", "69.5", "69.5"),
                ("D", "72.0", "72.0")
            ],
            "ans": "B",
            "solEn": "Weights ratio n1 : n2 = 40 : 60 = 2 : 3. Combined Average = (2 &times; 65 + 3 &times; 75) / (2 + 3) = (130 + 225) / 5 = 355 / 5 = 71.0.",
            "solHi": "भार अनुपात n1 : n2 = 40 : 60 = 2 : 3। संयुक्त औसत = (2 &times; 65 + 3 &times; 75) / (2 + 3) = (130 + 225) / 5 = 355 / 5 = 71.0।"
        },
        {
            "tag": "Percentage Change",
            "qEn": "Production of wheat rose from 80 lakh tonnes in 2022 to 92 lakh tonnes in 2023. What was the percentage growth rate?",
            "qHi": "गेहूं का उत्पादन 2022 में 80 लाख टन से बढ़कर 2023 में 92 लाख टन हो गया। प्रतिशत वृद्धि दर क्या थी?",
            "opts": [
                ("A", "12.0%", "12.0%"),
                ("B", "15.0%", "15.0%"),
                ("C", "13.5%", "13.5%"),
                ("D", "16.0%", "16.0%")
            ],
            "ans": "B",
            "solEn": "Increase = 92 - 80 = 12 lakh tonnes. Growth rate = (12 / 80) &times; 100 = 3/20 &times; 100 = 15.0%.",
            "solHi": "वृद्धि = 92 - 80 = 12 लाख टन। वृद्धि दर = (12 / 80) &times; 100 = 3/20 &times; 100 = 15.0%।"
        },
        {
            "tag": "Compound Percentage",
            "qEn": "A city's population increases by 10% in Year 1 and decreases by 10% in Year 2. What is the net percentage change over 2 years?",
            "qHi": "एक शहर की जनसंख्या वर्ष 1 में 10% बढ़ती है और वर्ष 2 में 10% घटती है। 2 वर्षों में शुद्ध प्रतिशत परिवर्तन क्या है?",
            "opts": [
                ("A", "No change (0%)", "कोई परिवर्तन नहीं (0%)"),
                ("B", "1% increase", "1% की वृद्धि"),
                ("C", "1% decrease", "1% की कमी"),
                ("D", "2% decrease", "2% की कमी")
            ],
            "ans": "C",
            "solEn": "Net change formula = a + b + (ab / 100). Here a = +10, b = -10. Net change = 10 - 10 + (10 &times; -10)/100 = 0 - 1 = -1% (1% decrease).",
            "solHi": "शुद्ध परिवर्तन सूत्र = a + b + (ab / 100)। यहाँ a = +10, b = -10। शुद्ध परिवर्तन = 10 - 10 - 100/100 = -1% (1% की कमी)।"
        },
        {
            "tag": "Units Interpretation",
            "qEn": "A budget allocates ₹4.5 crore for education and ₹90 lakh for sports. What is the ratio of education budget to sports budget?",
            "qHi": "एक बजट में शिक्षा के लिए ₹4.5 करोड़ और खेल के लिए ₹90 लाख आवंटित किए गए हैं। शिक्षा बजट का खेल बजट से अनुपात क्या है?",
            "opts": [
                ("A", "1 : 2", "1 : 2"),
                ("B", "5 : 1", "5 : 1"),
                ("C", "4.5 : 9", "4.5 : 9"),
                ("D", "50 : 1", "50 : 1")
            ],
            "ans": "B",
            "solEn": "Convert to same unit: ₹4.5 crore = 450 lakh. Ratio = 450 lakh : 90 lakh = 450 / 90 = 5 : 1.",
            "solHi": "समान इकाई में बदलें: ₹4.5 करोड़ = 450 लाख। अनुपात = 450 लाख : 90 लाख = 5 : 1।"
        },
        {
            "tag": "Percentage Share",
            "qEn": "Out of 1,200 employees, 360 are women. What percentage of the workforce are men?",
            "qHi": "1,200 कर्मचारियों में से 360 महिलाएं हैं। कार्यबल का कितने प्रतिशत पुरुष हैं?",
            "opts": [
                ("A", "30%", "30%"),
                ("B", "60%", "60%"),
                ("C", "70%", "70%"),
                ("D", "75%", "75%")
            ],
            "ans": "C",
            "solEn": "Women percentage = (360 / 1,200) &times; 100 = 30%. Therefore, men percentage = 100% - 30% = 70%. (Or Men = 1,200 - 360 = 840; 840/1,200 = 70%).",
            "solHi": "महिलाओं का प्रतिशत = (360 / 1,200) &times; 100 = 30%। अतः पुरुषों का प्रतिशत = 100% - 30% = 70%।"
        },
        {
            "tag": "Data Display",
            "qEn": "Which diagrammatic format is best suited to show the proportion of various components comprising a single whole total?",
            "qHi": "किसी एकल संपूर्ण योग के विभिन्न घटकों के अनुपात को दर्शाने के लिए कौन सा आरेख प्रारूप सर्वोत्तम है?",
            "opts": [
                ("A", "Line Graph", "रेखा आरेख (Line Graph)"),
                ("B", "Histogram", "आयतचित्र (Histogram)"),
                ("C", "Pie Chart", "पाई चार्ट (Pie Chart)"),
                ("D", "Frequency Polygon", "आवृत्ति बहुभुज")
            ],
            "ans": "C",
            "solEn": "A Pie Chart represents a single aggregate total (100% or 360&deg;) divided into proportional sectors, making it ideal for component distribution.",
            "solHi": "पाई चार्ट एक संपूर्ण योग (100% या 360&deg;) को आनुपातिक त्रिज्यखंडों में विभाजित करके दर्शाता है, जो घटक वितरण हेतु सर्वश्रेष्ठ है।"
        },
        {
            "tag": "Approximation",
            "qEn": "Estimate the value of (4,992 &times; 19.8) / 99.4 to the nearest integer.",
            "qHi": "(4,992 &times; 19.8) / 99.4 का सन्निकट पूर्णांक मान क्या होगा?",
            "opts": [
                ("A", "995", "995"),
                ("B", "998", "998"),
                ("C", "1,000", "1,000"),
                ("D", "1,050", "1,050")
            ],
            "ans": "C",
            "solEn": "Round numbers to nearest convenient values: 4,992 &approx; 5,000; 19.8 &approx; 20; 99.4 &approx; 100. Expression &approx; (5,000 &times; 20) / 100 = 100,000 / 100 = 1,000.",
            "solHi": "सुविधाजनक मानों में सन्निकटन: 4,992 &approx; 5,000; 19.8 &approx; 20; 99.4 &approx; 100। मान &approx; (5,000 &times; 20) / 100 = 1,000।"
        },
        {
            "tag": "Fraction Comparison",
            "qEn": "If the export value grew from ₹450 cr to ₹540 cr while import grew from ₹600 cr to ₹750 cr, which grew at a faster percentage rate?",
            "qHi": "यदि निर्यात मूल्य ₹450 करोड़ से बढ़कर ₹540 करोड़ हुआ जबकि आयात ₹600 करोड़ से बढ़कर ₹750 करोड़ हुआ, तो किसकी प्रतिशत वृद्धि दर अधिक थी?",
            "opts": [
                ("A", "Export (20%)", "निर्यात (20%)"),
                ("B", "Import (25%)", "आयात (25%)"),
                ("C", "Both grew at equal rates", "दोनों की दर समान थी"),
                ("D", "Cannot be determined", "निर्धारित नहीं किया जा सकता")
            ],
            "ans": "B",
            "solEn": "Export Growth = (540 - 450) / 450 = 90 / 450 = 1/5 = 20%. Import Growth = (750 - 600) / 600 = 150 / 600 = 1/4 = 25%. Import grew faster.",
            "solHi": "निर्यात वृद्धि = 90 / 450 = 1/5 = 20%। आयात वृद्धि = 150 / 600 = 1/4 = 25%। अतः आयात की वृद्धि दर अधिक थी।"
        },
        {
            "tag": "Ratio Conversion",
            "qEn": "If A : B = 2 : 3 and B : C = 4 : 5, what is the combined ratio A : B : C?",
            "qHi": "यदि A : B = 2 : 3 तथा B : C = 4 : 5 है, तो संयुक्त अनुपात A : B : C क्या होगा?",
            "opts": [
                ("A", "8 : 12 : 15", "8 : 12 : 15"),
                ("B", "2 : 4 : 5", "2 : 4 : 5"),
                ("C", "6 : 12 : 15", "6 : 12 : 15"),
                ("D", "8 : 10 : 15", "8 : 10 : 15")
            ],
            "ans": "A",
            "solEn": "Multiply A:B by 4 and B:C by 3 to equate B: A = 2 &times; 4 = 8; B = 3 &times; 4 = 12; C = 5 &times; 3 = 15. Hence A : B : C = 8 : 12 : 15.",
            "solHi": "B के मान को समान करने के लिए A:B को 4 से तथा B:C को 3 से गुणा करें: A = 8, B = 12, C = 15। अतः A : B : C = 8 : 12 : 15।"
        },
        {
            "tag": "Average Speed",
            "qEn": "In a DI time-distance chart, a vehicle travels 120 km at 60 km/h and returns at 40 km/h. What is the average speed for the whole journey?",
            "qHi": "एक डीआई समय-दूरी चार्ट में, एक वाहन 120 किमी की दूरी 60 किमी/घंटा से तय करता है और 40 किमी/घंटा से लौटता है। पूरी यात्रा की औसत गति क्या है?",
            "opts": [
                ("A", "50 km/h", "50 किमी/घंटा"),
                ("B", "48 km/h", "48 किमी/घंटा"),
                ("C", "52 km/h", "52 किमी/घंटा"),
                ("D", "45 km/h", "45 किमी/घंटा")
            ],
            "ans": "B",
            "solEn": "Harmonic average formula for equal distances = (2 &times; s1 &times; s2) / (s1 + s2) = (2 &times; 60 &times; 40) / (60 + 40) = 4,800 / 100 = 48 km/h.",
            "solHi": "समान दूरी के लिए औसत चाल = (2 &times; s1 &times; s2) / (s1 + s2) = (2 &times; 60 &times; 40) / 100 = 48 किमी/घंटा।"
        },
        {
            "tag": "Percentage Multiplication",
            "qEn": "What is 14.28% of 56,000?",
            "qHi": "56,000 का 14.28% क्या होगा?",
            "opts": [
                ("A", "7,000", "7,000"),
                ("B", "8,000", "8,000"),
                ("C", "7,800", "7,800"),
                ("D", "8,400", "8,400")
            ],
            "ans": "B",
            "solEn": "14.28% is the fraction 1/7. Value = (1/7) &times; 56,000 = 8,000.",
            "solHi": "14.28% का भिन्न मान 1/7 होता है। मान = (1/7) &times; 56,000 = 8,000।"
        },
        {
            "tag": "Table Reading",
            "qEn": "If monthly expenditure of a company is: Raw Material ₹40k, Rent ₹15k, Salaries ₹35k, and Misc ₹10k, what percentage of total expenditure is spent on Salaries?",
            "qHi": "यदि एक कंपनी का मासिक व्यय कच्चा माल ₹40k, किराया ₹15k, वेतन ₹35k और विविध ₹10k है, तो कुल व्यय का कितना प्रतिशत वेतन पर खर्च होता है?",
            "opts": [
                ("A", "30%", "30%"),
                ("B", "35%", "35%"),
                ("C", "40%", "40%"),
                ("D", "25%", "25%")
            ],
            "ans": "B",
            "solEn": "Total expenditure = 40 + 15 + 35 + 10 = ₹100k. Salaries = ₹35k. Percentage = (35 / 100) &times; 100 = 35%.",
            "solHi": "कुल व्यय = 40 + 15 + 35 + 10 = ₹100k। वेतन = ₹35k। प्रतिशत = (35 / 100) &times; 100 = 35%।"
        },
        {
            "tag": "Percentage Difference",
            "qEn": "Price of petrol increases from ₹90 to ₹108 per litre. By what percentage must a driver reduce fuel consumption to keep expenditure constant?",
            "qHi": "पेट्रोल की कीमत ₹90 से बढ़कर ₹108 प्रति लीटर हो जाती है। व्यय समान रखने के लिए उपभोक्ता को खपत में कितने प्रतिशत की कमी करनी होगी?",
            "opts": [
                ("A", "20.00%", "20.00%"),
                ("B", "16.67%", "16.67%"),
                ("C", "15.00%", "15.00%"),
                ("D", "18.00%", "18.00%")
            ],
            "ans": "B",
            "solEn": "Price increase = (18 / 90) &times; 100 = +20% = +1/5. Consumption reduction formula = [x / (1 + x)] = (1/5) / (6/5) = 1/6 = 16.67%.",
            "solHi": "मूल्य वृद्धि = (18 / 90) &times; 100 = +20% = +1/5। खपत में कमी = 1/(5+1) = 1/6 = 16.67%।"
        },
        {
            "tag": "Base Technique",
            "qEn": "If A is 25% more than B, then B is what percent less than A?",
            "qHi": "यदि A, B से 25% अधिक है, तो B, A से कितना प्रतिशत कम है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "20%", "20%"),
                ("C", "15%", "15%"),
                ("D", "16.67%", "16.67%")
            ],
            "ans": "B",
            "solEn": "Let B = 100, then A = 125. Difference = 25. Base is A (125). Percentage less = (25 / 125) &times; 100 = 1/5 &times; 100 = 20%.",
            "solHi": "माना B = 100, तो A = 125। अंतर = 25। आधार A (125) है। प्रतिशत कम = (25 / 125) &times; 100 = 1/5 &times; 100 = 20%।"
        },
        {
            "tag": "Average Concept",
            "qEn": "The average of 5 consecutive odd numbers is 61. What is the difference between the highest and lowest numbers?",
            "qHi": "5 क्रमागत विषम संख्याओं का औसत 61 है। सबसे बड़ी और सबसे छोटी संख्या में क्या अंतर है?",
            "opts": [
                ("A", "8", "8"),
                ("B", "6", "6"),
                ("C", "10", "10"),
                ("D", "4", "4")
            ],
            "ans": "A",
            "solEn": "Consecutive odd numbers are x, x+2, x+4, x+6, x+8. Difference between highest and lowest is always (n - 1) &times; 2 = (5 - 1) &times; 2 = 8.",
            "solHi": "5 क्रमागत विषम संख्याएं: x, x+2, x+4, x+6, x+8। सबसे बड़ी व सबसे छोटी में अंतर सदैव (n - 1) &times; 2 = 4 &times; 2 = 8 होता है।"
        },
        {
            "tag": "DI Strategy",
            "qEn": "What should a candidate do first upon viewing a complex multi-column table in an exam?",
            "qHi": "परीक्षा में एक जटिल बहु-स्तंभ तालिका (multi-column table) देखते ही अभ्यर्थी को सबसे पहले क्या करना चाहिए?",
            "opts": [
                ("A", "Calculate all column totals immediately", "तुरंत सभी स्तंभों का योग निकालना शुरू करें"),
                ("B", "Read title, column headers, units, and footnotes", "शीर्षक, स्तंभ शीर्षक, इकाइयां और पाद-टिप्पणियां पढ़ें"),
                ("C", "Convert all cells into percentages", "सभी कक्षों को प्रतिशत में बदलें"),
                ("D", "Draw a line graph on rough paper", "रफ शीट पर रेखा आरेख बनाएं")
            ],
            "ans": "B",
            "solEn": "First read the title, column headers, scale units (e.g., in thousands vs lakhs), and scan question stems before doing any unnecessary calculations.",
            "solHi": "सर्वप्रथम तालिका का शीर्षक, कॉलम हेडिंग, इकाइयां (लाख/हजार) पढ़ें और प्रश्नों को देखें ताकि अनावश्यक गणना से बचा जा सके।"
        },
        {
            "tag": "Ratio Application",
            "qEn": "In 2023, the ratio of boys to girls in a school was 5 : 4. If total students were 720, how many girls were enrolled?",
            "qHi": "2023 में एक विद्यालय में बालकों और बालिकाओं का अनुपात 5 : 4 था। यदि कुल विद्यार्थी 720 थे, तो कितनी बालिकाएं नामांकित थीं?",
            "opts": [
                ("A", "320", "320"),
                ("B", "400", "400"),
                ("C", "360", "360"),
                ("D", "300", "300")
            ],
            "ans": "A",
            "solEn": "Total parts = 5 + 4 = 9. Girls = (4 / 9) &times; 720 = 4 &times; 80 = 320.",
            "solHi": "कुल अनुपाती भाग = 5 + 4 = 9। बालिकाएं = (4 / 9) &times; 720 = 4 &times; 80 = 320।"
        },
        {
            "tag": "Percentage Calculation",
            "qEn": "If an item's sales drop from 250 units in January to 200 units in February, what is the percentage decrease?",
            "qHi": "यदि किसी वस्तु की बिक्री जनवरी में 250 इकाइयों से घटकर फरवरी में 200 इकाई हो जाती है, तो प्रतिशत कमी क्या है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "20%", "20%"),
                ("C", "15%", "15%"),
                ("D", "22.5%", "22.5%")
            ],
            "ans": "B",
            "solEn": "Decrease = 250 - 200 = 50. Base is January (250). Percentage decrease = (50 / 250) &times; 100 = 1/5 &times; 100 = 20%.",
            "solHi": "कमी = 250 - 200 = 50। आधार जनवरी (250) है। प्रतिशत कमी = (50 / 250) &times; 100 = 20%।"
        },
        {
            "tag": "Percentage Points Trap",
            "qEn": "The interest rate on farm loans in a state rose from 5% to 8%. By how many percentage points did it increase, and what was the percentage increase?",
            "qHi": "एक राज्य में कृषि ऋण पर ब्याज दर 5% से बढ़कर 8% हो गई। इसमें कितने प्रतिशत अंकों (percentage points) की वृद्धि हुई तथा ब्याज दर में कितने प्रतिशत की वृद्धि हुई?",
            "opts": [
                ("A", "3 percentage points and 60% increase", "3 प्रतिशत अंक तथा 60% की वृद्धि"),
                ("B", "3 percentage points and 3% increase", "3 प्रतिशत अंक तथा 3% की वृद्धि"),
                ("C", "30 percentage points and 60% increase", "30 प्रतिशत अंक तथा 60% की वृद्धि"),
                ("D", "3 percentage points and 37.5% increase", "3 प्रतिशत अंक तथा 37.5% की वृद्धि")
            ],
            "ans": "A",
            "solEn": "Percentage points difference = 8 - 5 = 3 percentage points. Percentage increase = [(8 - 5) / 5] &times; 100 = (3/5) &times; 100 = 60%. Always distinguish between percentage points and percentage increase!",
            "solHi": "प्रतिशत अंकों का अंतर = 8 - 5 = 3 प्रतिशत अंक। प्रतिशत वृद्धि = [(8 - 5) / 5] &times; 100 = (3/5) &times; 100 = 60%। हमेशा प्रतिशत अंक और प्रतिशत वृद्धि में अंतर समझें!"
        },
        {
            "tag": "Fraction Equivalent",
            "qEn": "What is 6.25% of 64,000?",
            "qHi": "64,000 का 6.25% कितना होगा?",
            "opts": [
                ("A", "3,200", "3,200"),
                ("B", "4,000", "4,000"),
                ("C", "4,800", "4,800"),
                ("D", "3,600", "3,600")
            ],
            "ans": "B",
            "solEn": "6.25% is the fraction 1/16. Value = 64,000 / 16 = 4,000.",
            "solHi": "6.25% का भिन्न मान 1/16 होता है। मान = 64,000 / 16 = 4,000।"
        },
        {
            "tag": "Ratio Application",
            "qEn": "In a factory, the ratio of skilled to unskilled workers is 7 : 3. If there are 210 skilled workers, find the total number of workers.",
            "qHi": "एक कारखाने में कुशल और अकुशल श्रमिकों का अनुपात 7 : 3 है। यदि 210 कुशल श्रमिक हैं, तो कुल श्रमिकों की संख्या ज्ञात कीजिए।",
            "opts": [
                ("A", "300", "300"),
                ("B", "270", "270"),
                ("C", "280", "280"),
                ("D", "320", "320")
            ],
            "ans": "A",
            "solEn": "7 parts = 210 &rarr; 1 part = 30. Total parts = 7 + 3 = 10. Total workers = 10 &times; 30 = 300.",
            "solHi": "7 भाग = 210 &rarr; 1 भाग = 30। कुल भाग = 7 + 3 = 10। कुल श्रमिक = 10 &times; 30 = 300।"
        },
        {
            "tag": "Percentage Multiplier",
            "qEn": "To increase a number by 28%, by which decimal factor should it be multiplied?",
            "qHi": "किसी संख्या में 28% की वृद्धि करने के लिए उसे किस दशमलव गुणक से गुणा किया जाना चाहिए?",
            "opts": [
                ("A", "0.28", "0.28"),
                ("B", "1.28", "1.28"),
                ("C", "12.8", "12.8"),
                ("D", "1.028", "1.028")
            ],
            "ans": "B",
            "solEn": "Increasing by 28% means 100% + 28% = 128% = 128 / 100 = 1.28.",
            "solHi": "28% बढ़ाने का अर्थ है 100% + 28% = 128% = 1.28 से गुणा करना।"
        },
        {
            "tag": "Calculation Trap",
            "qEn": "If A's income is 50% of B's income, and B's income is 50% of C's income, then A's income is what percentage of C's income?",
            "qHi": "यदि A की आय B की आय की 50% है, और B की आय C की आय की 50% है, तो A की आय C की आय का कितना प्रतिशत है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "50%", "50%"),
                ("C", "100%", "100%"),
                ("D", "12.5%", "12.5%")
            ],
            "ans": "A",
            "solEn": "Let C = 100. Then B = 50% of 100 = 50. A = 50% of 50 = 25. Thus, A is (25 / 100) &times; 100 = 25% of C.",
            "solHi": "माना C = 100। तो B = 50। A = 50 का 50% = 25। अतः A, C का 25% है।"
        }
    ],

    # 15 Mini-Test MCQs
    "testQuestions": [
        {
            "qEn": "What is the fraction equivalent of 16 2/3%?",
            "qHi": "16 2/3% का भिन्न मान क्या है?",
            "opts": [
                ("A", "1/6", "1/6"),
                ("B", "1/7", "1/7"),
                ("C", "1/8", "1/8"),
                ("D", "1/5", "1/5")
            ]
        },
        {
            "qEn": "If a quantity increases from 50 to 75, what is the percentage increase?",
            "qHi": "यदि कोई मात्रा 50 से बढ़कर 75 हो जाती है, तो प्रतिशत वृद्धि क्या है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "33.33%", "33.33%"),
                ("C", "50%", "50%"),
                ("D", "66.67%", "66.67%")
            ]
        },
        {
            "qEn": "What is 12.5% of 6,400?",
            "qHi": "6,400 का 12.5% क्या होगा?",
            "opts": [
                ("A", "750", "750"),
                ("B", "800", "800"),
                ("C", "850", "850"),
                ("D", "900", "900")
            ]
        },
        {
            "qEn": "If A : B = 3 : 5 and their sum is 240, find the value of B.",
            "qHi": "यदि A : B = 3 : 5 तथा उनका योग 240 है, तो B का मान ज्ञात कीजिए।",
            "opts": [
                ("A", "90", "90"),
                ("B", "150", "150"),
                ("C", "120", "120"),
                ("D", "160", "160")
            ]
        },
        {
            "qEn": "If X is 20% less than Y, then Y is what percent more than X?",
            "qHi": "यदि X, Y से 20% कम है, तो Y, X से कितना प्रतिशत अधिक है?",
            "opts": [
                ("A", "20%", "20%"),
                ("B", "25%", "25%"),
                ("C", "16.67%", "16.67%"),
                ("D", "30%", "30%")
            ]
        },
        {
            "qEn": "Average of 4 numbers is 25. If a 5th number is added, the new average becomes 27. What is the 5th number?",
            "qHi": "4 संख्याओं का औसत 25 है। यदि 5वीं संख्या जोड़ी जाती है, तो नया औसत 27 हो जाता है। 5वीं संख्या क्या है?",
            "opts": [
                ("A", "35", "35"),
                ("B", "37", "37"),
                ("C", "33", "33"),
                ("D", "31", "31")
            ]
        },
        {
            "qEn": "Find 9.09% of 4,400.",
            "qHi": "4,400 का 9.09% ज्ञात कीजिए।",
            "opts": [
                ("A", "400", "400"),
                ("B", "440", "440"),
                ("C", "360", "360"),
                ("D", "480", "480")
            ]
        },
        {
            "qEn": "In a DI chart, export is ₹360 cr and import is ₹450 cr. What is the ratio of export to import?",
            "qHi": "एक डीआई चार्ट में निर्यात ₹360 करोड़ तथा आयात ₹450 करोड़ है। निर्यात का आयात से अनुपात क्या है?",
            "opts": [
                ("A", "4 : 5", "4 : 5"),
                ("B", "5 : 4", "5 : 4"),
                ("C", "3 : 4", "3 : 4"),
                ("D", "6 : 7", "6 : 7")
            ]
        },
        {
            "qEn": "1 Crore is equal to how many Millions?",
            "qHi": "1 करोड़ कितने मिलियन के बराबर होता है?",
            "opts": [
                ("A", "1 Million", "1 मिलियन"),
                ("B", "10 Million", "10 मिलियन"),
                ("C", "100 Million", "100 मिलियन"),
                ("D", "0.1 Million", "0.1 मिलियन")
            ]
        },
        {
            "qEn": "A number is increased by 20% and then decreased by 20%. The net change is:",
            "qHi": "एक संख्या में 20% की वृद्धि की जाती है और फिर 20% की कमी की जाती है। शुद्ध परिवर्तन क्या है?",
            "opts": [
                ("A", "0% (No change)", "0% (कोई परिवर्तन नहीं)"),
                ("B", "4% decrease", "4% की कमी"),
                ("C", "4% increase", "4% की वृद्धि"),
                ("D", "2% decrease", "2% की कमी")
            ]
        },
        {
            "qEn": "What is 66.67% of 1,800?",
            "qHi": "1,800 का 66.67% क्या है?",
            "opts": [
                ("A", "1,200", "1,200"),
                ("B", "1,100", "1,100"),
                ("C", "1,350", "1,350"),
                ("D", "1,400", "1,400")
            ]
        },
        {
            "qEn": "In a pie chart, what central angle represents 25% share of the total?",
            "qHi": "पाई चार्ट में कुल का 25% भाग किस केंद्रीय कोण द्वारा दर्शाया जाता है?",
            "opts": [
                ("A", "45&deg;", "45&deg;"),
                ("B", "60&deg;", "60&deg;"),
                ("C", "90&deg;", "90&deg;"),
                ("D", "120&deg;", "120&deg;")
            ]
        },
        {
            "qEn": "If production increases from 120 tonnes to 150 tonnes, what is the percentage increase?",
            "qHi": "यदि उत्पादन 120 टन से बढ़कर 150 टन हो जाता है, तो प्रतिशत वृद्धि क्या है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "30%", "30%"),
                ("C", "20%", "20%"),
                ("D", "15%", "15%")
            ]
        },
        {
            "qEn": "A ratio 7 : 5 expressed as a percentage of the first quantity to the second is:",
            "qHi": "अनुपात 7 : 5 में पहली राशि दूसरी राशि का कितना प्रतिशत है?",
            "opts": [
                ("A", "140%", "140%"),
                ("B", "125%", "125%"),
                ("C", "150%", "150%"),
                ("D", "71.4%", "71.4%")
            ]
        },
        {
            "qEn": "Average of 50, 70, 90, 110, and 130 is:",
            "qHi": "50, 70, 90, 110 और 130 का औसत क्या है?",
            "opts": [
                ("A", "85", "85"),
                ("B", "90", "90"),
                ("C", "95", "95"),
                ("D", "100", "100")
            ]
        }
    ],

    "testDataJson": json.dumps([
        {"ans": "A", "solEn": "16 2/3% = 50/3% = (50/3)/100 = 50/300 = 1/6.", "solHi": "16 2/3% = 50/3% = 50/300 = 1/6।"},
        {"ans": "C", "solEn": "Increase = 25. Base = 50. (25/50) &times; 100 = 50%.", "solHi": "वृद्धि = 25। आधार = 50। (25/50) &times; 100 = 50%।"},
        {"ans": "B", "solEn": "12.5% = 1/8. 6,400 / 8 = 800.", "solHi": "12.5% = 1/8। 6,400 / 8 = 800।"},
        {"ans": "B", "solEn": "B's share = (5/8) &times; 240 = 5 &times; 30 = 150.", "solHi": "B का हिस्सा = (5/8) &times; 240 = 150।"},
        {"ans": "B", "solEn": "Let Y = 100, then X = 80. Y is more than X by (20/80) &times; 100 = 25%.", "solHi": "माना Y = 100, तो X = 80। Y, X से (20/80) &times; 100 = 25% अधिक है।"},
        {"ans": "A", "solEn": "New total = 5 &times; 27 = 135. Old total = 4 &times; 25 = 100. 5th number = 135 - 100 = 35.", "solHi": "नया योग = 5 &times; 27 = 135। पुराना योग = 4 &times; 25 = 100। 5वीं संख्या = 135 - 100 = 35।"},
        {"ans": "A", "solEn": "9.09% = 1/11. 4,400 / 11 = 400.", "solHi": "9.09% = 1/11। 4,400 / 11 = 400।"},
        {"ans": "A", "solEn": "360 / 450 = 36 / 45 = 4 / 5 = 4 : 5.", "solHi": "360 / 450 = 4 / 5 = 4 : 5।"},
        {"ans": "B", "solEn": "1 Crore = 10,000,000 = 10 Million.", "solHi": "1 करोड़ = 100 लाख = 10 मिलियन।"},
        {"ans": "B", "solEn": "+20 - 20 - (400/100) = -4% (4% decrease).", "solHi": "+20 - 20 - (400/100) = -4% (4% की कमी)।"},
        {"ans": "A", "solEn": "66.67% = 2/3. (2/3) &times; 1,800 = 1,200.", "solHi": "66.67% = 2/3। (2/3) &times; 1,800 = 1,200।"},
        {"ans": "C", "solEn": "25% of 360&deg; = 360&deg; / 4 = 90&deg;.", "solHi": "360&deg; का 25% = 360&deg; / 4 = 90&deg;।"},
        {"ans": "A", "solEn": "Increase = 30. (30 / 120) &times; 100 = 1/4 &times; 100 = 25%.", "solHi": "वृद्धि = 30। (30 / 120) &times; 100 = 1/4 &times; 100 = 25%।"},
        {"ans": "A", "solEn": "(7 / 5) &times; 100 = 7 &times; 20 = 140%.", "solHi": "(7 / 5) &times; 100 = 140%।"},
        {"ans": "B", "solEn": "For an AP with odd terms, the middle term is the average = 90.", "solHi": "समान अंतर वाली 5 संख्याओं में ठीक बीच वाली संख्या औसत होती है = 90।"}
    ])
}
