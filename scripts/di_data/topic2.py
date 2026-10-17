"""
topic2.py
Topic 2: Statistical Analysis & Diagrammatic Inferences: Measures & Trends
Slug: statistical-analysis-and-diagrammatic-inference
"""

import json

TOPIC_2 = {
    "slug": "statistical-analysis-and-diagrammatic-inference",
    "titleEn": "Statistical Analysis & Diagrammatic Inferences",
    "titleHi": "सांख्यिकीय विश्लेषण एवं आरेखीय निष्कर्ष",
    "pageTitle": "Statistical Analysis & Diagrammatic Inferences: Notes | UPSSSC Mains | SJMaths",
    "metaDesc": "Pointwise study notes, 30 practice questions with full mathematical solutions, and a 15-Q test on Statistical Analysis (Mean, Median, Mode, Range, Ogives, Histograms, and Diagrammatic Inferences) for UPSSSC Intermediate Level Mains 2026.",
    "metaTagEn": "Part-1 (9): Data Interpretation & Statistical Analysis | Central Tendency & Inferences",
    "metaTagHi": "भाग-1 (9): डाटा इंटरप्रिटेशन एवं सांख्यिकीय विश्लेषण | केंद्रीय प्रवृत्ति एवं निष्कर्ष",
    "subtitleEn": "Comprehensive study guide covering Mean, Median, Mode, Standard Deviation, Frequency Polygons, Cumulative Ogives, and sound deductive inferences from diagrams for UPSSSC Intermediate Level Mains.",
    "subtitleHi": "माध्य, माध्यिका, बहुलक, मानक विचलन, आवृत्ति बहुभुज, संचयी आवृत्ति तोरण (ओजाइव) व आरेखों से तार्किक निष्कर्ष निकालने हेतु विस्तृत अध्ययन नोट्स व अभ्यास प्रश्न।",
    "crumbNameEn": "Statistical Analysis & Inferences",
    "crumbNameHi": "सांख्यिकीय विश्लेषण व निष्कर्ष",

    "notesHtml": """
        <!-- Section 1: Measures of Central Tendency -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-chart-line"></i>
                <span class="lang-en">1. Measures of Central Tendency (Mean, Median &amp; Mode)</span>
                <span class="lang-hi">1. केंद्रीय प्रवृत्ति के माप (माध्य, माध्यिका एवं बहुलक)</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Empirical Formula Alert:</strong> For moderately skewed unimodal frequency distributions, remember Pearson's empirical relationship: <code>Mode = 3 &times; Median - 2 &times; Mean</code> (or <code>Mode - Mean = 3 &times; (Median - Mean)</code>). This is asked in nearly every UPSSSC exam!</span>
                <span class="lang-hi"><strong>अनुभवजन्य सूत्र चेतावनी:</strong> असममित आवृत्ति वितरण के लिए पियर्सन का सूत्र याद रखें: <code>बहुलक = 3 &times; माध्यिका - 2 &times; माध्य</code>। यह प्रश्न लगभग प्रत्येक यूपीएसएसएससी परीक्षा में पूछा जाता है!</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Arithmetic Mean (माध्य)</span>
                    <span class="lang-en">For ungrouped data: <code>X&#772; = (&sum; x) / n</code>. For grouped frequency distribution: <code>X&#772; = (&sum; f_i &times; x_i) / (&sum; f_i)</code>, where <code>x_i</code> is the class mark (midpoint of class interval = (Lower limit + Upper limit) / 2).</span>
                    <span class="lang-hi">अवर्गीकृत डेटा के लिए: <code>X&#772; = (&sum; x) / n</code>। वर्गीकृत बारंबारता बंटन के लिए: <code>X&#772; = (&sum; f_i &times; x_i) / N</code>, जहाँ <code>x_i</code> वर्ग चिह्न (वर्ग अंतराल का मध्य बिंदु = (निम्न सीमा + उच्च सीमा) / 2) है।</span>
                </li>
                <li>
                    <span class="key-badge">Median (माध्यिका)</span>
                    <span class="lang-en">The positional middle value after arranging data in ascending order.
                    <br>&bull; If n is odd: <code>Median = [(n + 1) / 2]th term</code>.
                    <br>&bull; If n is even: <code>Median = Average of (n/2)th and [(n/2) + 1]th terms</code>.
                    <br>&bull; For Grouped Continuous Data: <code>Median = L + [((N/2) - cf) / f] &times; h</code> (where L = lower limit of median class, N = &sum; f, cf = cumulative frequency of preceding class, f = frequency of median class, h = class width).</span>
                    <span class="lang-hi">डेटा को आरोही क्रम में व्यवस्थित करने पर ठीक बीच का मान।
                    <br>&bull; यदि n विषम है: <code>माध्यिका = [(n + 1) / 2]वाँ पद</code>।
                    <br>&bull; यदि n सम है: <code>माध्यिका = [(n/2)वें पद और ((n/2) + 1)वें पद का औसत]</code>।
                    <br>&bull; वर्गीकृत सतत डेटा: <code>माध्यिका = L + [((N/2) - cf) / f] &times; h</code>।</span>
                </li>
                <li>
                    <span class="key-badge">Mode (बहुलक)</span>
                    <span class="lang-en">The most frequently occurring value in the dataset.
                    <br>&bull; For Grouped Data: <code>Mode = L + [(f1 - f0) / (2f1 - f0 - f2)] &times; h</code> (where L = lower limit of modal class, f1 = frequency of modal class, f0 = frequency of preceding class, f2 = frequency of succeeding class, h = class width).</span>
                    <span class="lang-hi">दिए गए आँकड़ों में सर्वाधिक बार आने वाला मान।
                    <br>&bull; वर्गीकृत डेटा: <code>बहुलक = L + [(f1 - f0) / (2f1 - f0 - f2)] &times; h</code>।</span>
                </li>
            </ul>
        </section>

        <!-- Section 2: Measures of Dispersion & Consistency -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-arrows-alt-h"></i>
                <span class="lang-en">2. Measures of Dispersion &amp; Consistency</span>
                <span class="lang-hi">2. अपकिरण के माप एवं स्थिरता (Consistency) का आकलन</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Consistency Principle:</strong> The team, company, or player with the <em>LOWER</em> Coefficient of Variation (C.V.) or smaller Standard Deviation is considered more consistent, stable, and reliable.</span>
                <span class="lang-hi"><strong>स्थिरता का सिद्धांत:</strong> जिस टीम, कंपनी या खिलाड़ी का विचरण गुणांक (C.V.) या मानक विचलन <em>कम</em> होता है, उसे अधिक सुसंगत, स्थिर और विश्वसनीय माना जाता है।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Range (परास / विस्तार)</span>
                    <span class="lang-en"><code>Range = Highest Value - Lowest Value</code>. Relative measure is Coefficient of Range = <code>(H - L) / (H + L)</code>.</span>
                    <span class="lang-hi"><code>परास = उच्चतम मान - न्यूनतम मान</code>। सापेक्ष माप (विस्तार गुणांक) = <code>(H - L) / (H + L)</code>।</span>
                </li>
                <li>
                    <span class="key-badge">Variance &amp; Standard Deviation</span>
                    <span class="lang-en">Variance (&sigma;^2) = <code>&sum;(x - X&#772;)^2 / n</code>.
                    <br>Standard Deviation (&sigma;) = <code>&radic;(Variance)</code>. Always positive. SD is in the same units as the original data.</span>
                    <span class="lang-hi">प्रसरण (Variance, &sigma;^2) = <code>&sum;(x - X&#772;)^2 / n</code>।
                    <br>मानक विचलन (&sigma;) = <code>&radic;(प्रसरण)</code>। यह सदैव धनात्मक होता है तथा मूल डेटा की इकाई में मापा जाता है।</span>
                </li>
                <li>
                    <span class="key-badge">Coefficient of Variation (C.V.)</span>
                    <span class="lang-en"><code>C.V. = (&sigma; / X&#772;) &times; 100</code>. It is a unit-free percentage used to compare dispersion between two datasets having different units or different means.</span>
                    <span class="lang-hi"><code>विचरण गुणांक (C.V.) = (&sigma; / X&#772;) &times; 100</code>। यह एक इकाई-रहित प्रतिशत माप है जिसका उपयोग दो भिन्न औसत वाले डेटासेट की स्थिरता की तुलना करने में होता है।</span>
                </li>
            </ul>
        </section>

        <!-- Section 3: Cumulative Frequency Curves (Ogives) & Visual Diagram -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-bezier-curve"></i>
                <span class="lang-en">3. Cumulative Frequency Curves (Ogives) &amp; Graphical Median</span>
                <span class="lang-hi">3. संचयी आवृत्ति वक्र (तोरण / ओजाइव) एवं ग्राफीय माध्यिका</span>
            </h2>
            <p>
                <span class="lang-en">An Ogive is a smooth cumulative frequency polygon. There are two types: <strong>'Less than' Ogive</strong> (rises from bottom-left to top-right) and <strong>'More than' Ogive</strong> (falls from top-left to bottom-right). Their point of intersection has the X-coordinate equal to the <strong>Median</strong> and Y-coordinate equal to <strong>N / 2</strong>.</span>
                <span class="lang-hi">तोरण (ओजाइव) एक सुगम संचयी आवृत्ति वक्र होता है। यह दो प्रकार का होता है: <strong>'से कम' तोरण</strong> (नीचे से ऊपर की ओर बढ़ता हुआ) और <strong>'से अधिक' तोरण</strong> (ऊपर से नीचे गिरता हुआ)। दोनों वक्रों का प्रतिच्छेदन बिंदु X-अक्ष पर <strong>माध्यिका</strong> और Y-अक्ष पर <strong>N / 2</strong> मान प्रदर्शित करता है।</span>
            </p>

            <!-- SVG Diagram for Dual Ogive -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 2.1: Determination of Median via Dual Ogive Curves (N = 100 Students)</span>
                    <span class="lang-hi">चित्र 2.1: द्वि-तोरण वक्रों द्वारा माध्यिका का निर्धारण (N = 100 विद्यार्थी)</span>
                </h4>
                <svg viewBox="0 0 680 320" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Dual Ogive Curves intersecting at Median">
                    <!-- Grid Lines -->
                    <line x1="80" y1="250" x2="620" y2="250" stroke="#cbd5e1" stroke-width="1.5"/>
                    <line x1="80" y1="40" x2="80" y2="250" stroke="#cbd5e1" stroke-width="1.5"/>
                    
                    <!-- Dotted grid -->
                    <line x1="80" y1="145" x2="620" y2="145" stroke="#94a3b8" stroke-dasharray="4,4"/>
                    <line x1="350" y1="40" x2="350" y2="250" stroke="#94a3b8" stroke-dasharray="4,4"/>

                    <!-- X-Axis Labels (Marks) -->
                    <text x="80" y="270" fill="#64748b" font-size="12" text-anchor="middle">0</text>
                    <text x="170" y="270" fill="#64748b" font-size="12" text-anchor="middle">20</text>
                    <text x="260" y="270" fill="#64748b" font-size="12" text-anchor="middle">40</text>
                    <text x="350" y="270" fill="#0d9488" font-size="14" font-weight="bold" text-anchor="middle">Median = 50</text>
                    <text x="440" y="270" fill="#64748b" font-size="12" text-anchor="middle">60</text>
                    <text x="530" y="270" fill="#64748b" font-size="12" text-anchor="middle">80</text>
                    <text x="620" y="270" fill="#64748b" font-size="12" text-anchor="middle">100</text>
                    <text x="350" y="295" fill="#182e26" font-size="13" font-weight="bold" text-anchor="middle">Marks Scored (प्राप्तांक &rarr;)</text>

                    <!-- Y-Axis Labels (Cumulative Frequency) -->
                    <text x="70" y="255" fill="#64748b" font-size="12" text-anchor="end">0</text>
                    <text x="70" y="200" fill="#64748b" font-size="12" text-anchor="end">25</text>
                    <text x="70" y="150" fill="#0d9488" font-size="13" font-weight="bold" text-anchor="end">N/2 = 50</text>
                    <text x="70" y="95" fill="#64748b" font-size="12" text-anchor="end">75</text>
                    <text x="70" y="45" fill="#64748b" font-size="12" text-anchor="end">N = 100</text>

                    <!-- 'Less Than' Ogive Curve (Green Teal) -->
                    <path d="M 80 250 Q 200 230 260 200 T 350 145 T 480 80 T 620 40" fill="none" stroke="#0d9488" stroke-width="3.5"/>
                    <text x="580" y="30" fill="#0f766e" font-size="13" font-weight="bold">'Less than' Ogive</text>

                    <!-- 'More Than' Ogive Curve (Coral Orange) -->
                    <path d="M 80 40 Q 180 70 260 100 T 350 145 T 480 215 T 620 250" fill="none" stroke="#ea580c" stroke-width="3.5"/>
                    <text x="130" y="30" fill="#c2410c" font-size="13" font-weight="bold">'More than' Ogive</text>

                    <!-- Intersection Point Dot -->
                    <circle cx="350" cy="145" r="7" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
                    <text x="365" y="140" fill="#dc2626" font-size="13" font-weight="bold">Intersection (50, 50)</text>
                </svg>
                <div style="font-size:0.88rem;color:var(--planner-text-muted);margin-top:0.5rem;">
                    <span class="lang-en">The intersection point of both ogives drops down to the X-axis at exactly 50, which is the Median mark.</span>
                    <span class="lang-hi">दोनों तोरण वक्रों का प्रतिच्छेद बिंदु X-अक्ष पर ठीक 50 पर मिलता है, जो कि माध्यिका अंक है।</span>
                </div>
            </div>
        </section>

        <!-- Section 4: Drawing Diagrammatic Inferences & Critical Fallacies -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-brain"></i>
                <span class="lang-en">4. Rules of Diagrammatic Inference &amp; Trap Avoidance</span>
                <span class="lang-hi">4. आरेखीय निष्कर्ष के नियम एवं भ्रामक त्रुटियों से बचाव</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Critical Exam Principle:</strong> In questions asking <em>"Which of the following conclusions can be definitively drawn from the graph?"</em>, stick strictly to the stated data. Never extrapolate trends beyond the boundary years or assume causation where only correlation is visible.</span>
                <span class="lang-hi"><strong>अति-महत्वपूर्ण परीक्षा सिद्धांत:</strong> जब प्रश्न पूछे कि <em>"आरेख से कौन सा निष्कर्ष निश्चित रूप से निकाला जा सकता है?"</em>, तो केवल दिए गए डेटा तक सीमित रहें। दिए गए वर्षों से आगे का अनुमान न लगाएं और न ही केवल सह-संबंध देखकर कार्य-कारण संबंध मान लें।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Fallacy of False Trend Extrapolation</span>
                    <span class="lang-en">If production rose steadily from 2021 to 2024, you CANNOT conclude that production will rise in 2025 unless explicitly stated by a linear forecasting model.</span>
                    <span class="lang-hi">यदि 2021 से 2024 तक उत्पादन लगातार बढ़ा है, तो आप यह निष्कर्ष नहीं निकाल सकते कि 2025 में भी बढ़ेगा, जब तक कि स्पष्ट भविष्यवाणी मॉडल न दिया हो।</span>
                </li>
                <li>
                    <span class="key-badge">Rate of Increase vs Absolute Increase</span>
                    <span class="lang-en">A declining slope on a line graph does NOT mean absolute values are decreasing. It only means the <em>rate of growth</em> is slowing down, as long as the value is still higher than the previous year.</span>
                    <span class="lang-hi">रेखा आरेख पर ढलान का कम होना वास्तविक मानों में गिरावट का संकेत नहीं देता। इसका केवल यह अर्थ है कि <em>वृद्धि की दर</em> धीमी हो गई है, जबकि कुल मान अभी भी पिछले वर्ष से अधिक हो सकता है।</span>
                </li>
                <li>
                    <span class="key-badge">Broken Axis Distortion</span>
                    <span class="lang-en">Examiners frequently use a zigzag broken scale (kink) on the Y-axis (starting from 90 instead of 0). This exaggerates tiny differences visually. Always read the numerical coordinates on the axis, not just the bar heights visually!</span>
                    <span class="lang-hi">परीक्षक अक्सर Y-अक्ष पर शून्य के बजाय 90 से शुरू होने वाला खंडित पैमाना (kink) देते हैं। इससे छोटे अंतर भी बहुत बड़े दिखने लगते हैं। केवल बार की ऊंचाई देखकर अनुमान न लगाएं, हमेशा अक्ष के अंकों को पढ़ें!</span>
                </li>
            </ul>
        </section>

        <!-- Section 5: Grouped Frequency Table Exemplar -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-calculator"></i>
                <span class="lang-en">5. Worked Statistical Exemplar: Grouped Distribution</span>
                <span class="lang-hi">5. विस्तृत हल सहित सांख्यिकीय उदाहरण: वर्गीकृत बारंबारता</span>
            </h2>
            <p>
                <span class="lang-en">Consider the test score distribution of 50 candidates in an examination:</span>
                <span class="lang-hi">एक परीक्षा में 50 अभ्यर्थियों के प्राप्तांक वितरण पर विचार कीजिए:</span>
            </p>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Class Interval (Marks)</span><span class="lang-hi">वर्ग अंतराल (अंक)</span></th>
                            <th><span class="lang-en">Frequency (f)</span><span class="lang-hi">बारंबारता (f)</span></th>
                            <th><span class="lang-en">Midpoint (x)</span><span class="lang-hi">मध्य बिंदु (x)</span></th>
                            <th><span class="lang-en">f &times; x</span><span class="lang-hi">f &times; x</span></th>
                            <th><span class="lang-en">Cumulative Frequency (cf)</span><span class="lang-hi">संचयी बारंबारता (cf)</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>0 &ndash; 10</td>
                            <td>5</td>
                            <td>5</td>
                            <td>25</td>
                            <td>5</td>
                        </tr>
                        <tr>
                            <td>10 &ndash; 20</td>
                            <td>12</td>
                            <td>15</td>
                            <td>180</td>
                            <td>17</td>
                        </tr>
                        <tr>
                            <td>20 &ndash; 30 (Median Class)</td>
                            <td>18</td>
                            <td>25</td>
                            <td>450</td>
                            <td>35</td>
                        </tr>
                        <tr>
                            <td>30 &ndash; 40</td>
                            <td>10</td>
                            <td>35</td>
                            <td>350</td>
                            <td>45</td>
                        </tr>
                        <tr>
                            <td>40 &ndash; 50</td>
                            <td>5</td>
                            <td>45</td>
                            <td>225</td>
                            <td>50</td>
                        </tr>
                        <tr style="background:var(--planner-primary-light);font-weight:bold;">
                            <td><strong>Total</strong></td>
                            <td><strong>N = 50</strong></td>
                            <td>&mdash;</td>
                            <td><strong>&sum; fx = 1,230</strong></td>
                            <td>&mdash;</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="exam-pointer" style="background:var(--planner-bg-surface);border-left:4px solid var(--planner-primary);">
                <h4><span class="lang-en">Step-by-Step Statistical Calculations:</span><span class="lang-hi">चरणबद्ध सांख्यिकीय गणनाएं:</span></h4>
                <ol style="margin-left:20px;line-height:1.75;">
                    <li>
                        <strong><span class="lang-en">Mean:</span><span class="lang-hi">माध्य:</span></strong>
                        <code>X&#772; = &sum;fx / N = 1,230 / 50 = 24.6 marks</code>.
                    </li>
                    <li>
                        <strong><span class="lang-en">Median:</span><span class="lang-hi">माध्यिका:</span></strong>
                        N/2 = 50 / 2 = 25. Median class is 20&ndash;30 (since cf = 35 &ge; 25).
                        <br>L = 20, cf = 17, f = 18, h = 10.
                        <br><code>Median = 20 + [(25 - 17) / 18] &times; 10 = 20 + (8 / 18) &times; 10 = 20 + 4.44 = 24.44 marks</code>.
                    </li>
                    <li>
                        <strong><span class="lang-en">Mode:</span><span class="lang-hi">बहुलक:</span></strong>
                        Modal class is 20&ndash;30 (highest frequency = 18).
                        <br>L = 20, f1 = 18, f0 = 12, f2 = 10, h = 10.
                        <br><code>Mode = 20 + [(18 - 12) / (2&times;18 - 12 - 10)] &times; 10 = 20 + [6 / (36 - 22)] &times; 10 = 20 + (6/14)&times;10 = 20 + 4.29 = 24.29 marks</code>.
                    </li>
                    <li>
                        <strong><span class="lang-en">Empirical Formula Check:</span><span class="lang-hi">अनुभवजन्य सूत्र सत्यापन:</span></strong>
                        <code>Mode &approx; 3 &times; Median - 2 &times; Mean = 3(24.44) - 2(24.6) = 73.32 - 49.20 = 24.12 marks</code> (Matches modal calculation closely).
                    </li>
                </ol>
            </div>
        </section>
    """,

    # 30 Curated Practice Questions
    "practiceQuestions": [
        {
            "tag": "Empirical Formula",
            "qEn": "In a moderately asymmetrical distribution, the mean is 30 and the median is 28. What is the value of the mode?",
            "qHi": "एक मध्यम असममित आवृत्ति बंटन में, माध्य 30 है और माध्यिका 28 है। बहुलक का मान क्या होगा?",
            "opts": [
                ("A", "24", "24"),
                ("B", "26", "26"),
                ("C", "28", "28"),
                ("D", "32", "32")
            ],
            "ans": "A",
            "solEn": "Mode = 3 &times; Median - 2 &times; Mean = 3(28) - 2(30) = 84 - 60 = 24.",
            "solHi": "बहुलक = 3 &times; माध्यिका - 2 &times; माध्य = 3(28) - 2(30) = 84 - 60 = 24।"
        },
        {
            "tag": "Median Calculation",
            "qEn": "Find the median of the following set of observations: 14, 22, 9, 35, 18, 27, 41.",
            "qHi": "निम्नलिखित प्रेक्षणों की माध्यिका ज्ञात कीजिए: 14, 22, 9, 35, 18, 27, 41।",
            "opts": [
                ("A", "18", "18"),
                ("B", "22", "22"),
                ("C", "27", "27"),
                ("D", "23", "23")
            ],
            "ans": "B",
            "solEn": "Arrange in ascending order: 9, 14, 18, 22, 27, 35, 41. Number of terms n = 7 (odd). Median = (7 + 1)/2 = 4th term = 22.",
            "solHi": "आरोही क्रम: 9, 14, 18, 22, 27, 35, 41। पदों की संख्या n = 7 (विषम)। माध्यिका = (7 + 1)/2 = चौथा पद = 22।"
        },
        {
            "tag": "Median Even Terms",
            "qEn": "Find the median of the observations: 12, 18, 7, 25, 30, 15, 21, 9.",
            "qHi": "प्रेक्षणों की माध्यिका ज्ञात कीजिए: 12, 18, 7, 25, 30, 15, 21, 9।",
            "opts": [
                ("A", "15.0", "15.0"),
                ("B", "16.5", "16.5"),
                ("C", "18.0", "18.0"),
                ("D", "17.0", "17.0")
            ],
            "ans": "B",
            "solEn": "Arrange in ascending order: 7, 9, 12, 15, 18, 21, 25, 30. n = 8 (even). Median = Average of 4th (15) and 5th (18) terms = (15 + 18)/2 = 16.5.",
            "solHi": "आरोही क्रम: 7, 9, 12, 15, 18, 21, 25, 30। n = 8 (सम)। माध्यिका = (15 + 18)/2 = 33/2 = 16.5।"
        },
        {
            "tag": "Mode Identification",
            "qEn": "What is the mode of the data: 4, 7, 9, 7, 12, 7, 15, 9, 7, 18, 12?",
            "qHi": "दिए गए आंकड़ों का बहुलक क्या है: 4, 7, 9, 7, 12, 7, 15, 9, 7, 18, 12?",
            "opts": [
                ("A", "9", "9"),
                ("B", "7", "7"),
                ("C", "12", "12"),
                ("D", "10", "10")
            ],
            "ans": "B",
            "solEn": "The number 7 appears with the highest frequency (4 times). Therefore, the mode is 7.",
            "solHi": "संख्या 7 सर्वाधिक बार (4 बार) आई है। अतः बहुलक 7 है।"
        },
        {
            "tag": "Range & Coefficient",
            "qEn": "The daily wages of 6 workers are ₹450, ₹600, ₹380, ₹720, ₹500, ₹850. What is the Range of the wages?",
            "qHi": "6 श्रमिकों की दैनिक मजदूरी ₹450, ₹600, ₹380, ₹720, ₹500, ₹850 है। मजदूरी का विस्तार (Range) क्या है?",
            "opts": [
                ("A", "₹470", "₹470"),
                ("B", "₹450", "₹450"),
                ("C", "₹400", "₹400"),
                ("D", "₹500", "₹500")
            ],
            "ans": "A",
            "solEn": "Highest wage (H) = ₹850; Lowest wage (L) = ₹380. Range = H - L = 850 - 380 = ₹470.",
            "solHi": "उच्चतम मान (H) = ₹850; न्यूनतम मान (L) = ₹380। विस्तार = 850 - 380 = ₹470।"
        },
        {
            "tag": "Standard Deviation",
            "qEn": "If the variance of a dataset is 144, what is the standard deviation?",
            "qHi": "यदि किसी डेटासेट का प्रसरण (variance) 144 है, तो उसका मानक विचलन क्या होगा?",
            "opts": [
                ("A", "12", "12"),
                ("B", "&plusmn;12", "&plusmn;12"),
                ("C", "72", "72"),
                ("D", "14.4", "14.4")
            ],
            "ans": "A",
            "solEn": "Standard Deviation (&sigma;) = &radic;(Variance) = &radic;(144) = 12. Standard deviation is always defined as the positive square root of variance.",
            "solHi": "मानक विचलन (&sigma;) = &radic;(प्रसरण) = &radic;(144) = 12। मानक विचलन सदैव धनात्मक वर्गमूल होता है।"
        },
        {
            "tag": "Coefficient of Variation",
            "qEn": "Team X has mean score 80 with SD 8. Team Y has mean score 60 with SD 9. Which team is more consistent?",
            "qHi": "टीम X का औसत स्कोर 80 और मानक विचलन 8 है। टीम Y का औसत स्कोर 60 और मानक विचलन 9 है। कौन सी टीम अधिक सुसंगत (consistent) है?",
            "opts": [
                ("A", "Team X (CV = 10%)", "टीम X (CV = 10%)"),
                ("B", "Team Y (CV = 15%)", "टीम Y (CV = 15%)"),
                ("C", "Both are equally consistent", "दोनों समान रूप से सुसंगत हैं"),
                ("D", "Cannot be determined", "निर्धारित नहीं किया जा सकता")
            ],
            "ans": "A",
            "solEn": "CV_X = (8/80) &times; 100 = 10%. CV_Y = (9/60) &times; 100 = 15%. Lower CV indicates higher consistency. Team X is more consistent.",
            "solHi": "CV_X = (8/80) &times; 100 = 10%। CV_Y = (9/60) &times; 100 = 15%। कम CV अधिक स्थिरता को दर्शाता है। अतः टीम X अधिक सुसंगत है।"
        },
        {
            "tag": "Ogive Intersection",
            "qEn": "The 'Less than' ogive and 'More than' ogive of a frequency distribution intersect at point (35, 40). What is the median of the distribution?",
            "qHi": "एक बारंबारता बंटन का 'से कम' तोरण और 'से अधिक' तोरण बिंदु (35, 40) पर प्रतिच्छेद करते हैं। बंटन की माध्यिका क्या है?",
            "opts": [
                ("A", "40", "40"),
                ("B", "35", "35"),
                ("C", "75", "75"),
                ("D", "80", "80")
            ],
            "ans": "B",
            "solEn": "The X-coordinate of the intersection of both ogives always represents the Median. Hence Median = 35. (The Y-coordinate represents N/2 = 40 &rarr; Total N = 80).",
            "solHi": "दोनों तोरण वक्रों के प्रतिच्छेद बिंदु का X-निर्देशांक सदैव माध्यिका को दर्शाता है। अतः माध्यिका = 35 है (तथा Y-निर्देशांक N/2 = 40 दर्शाता है)।"
        },
        {
            "tag": "Histogram Principle",
            "qEn": "In a histogram representing continuous grouped data, what does the area of each rectangle represent?",
            "qHi": "सतत वर्गीकृत आँकड़ों को दर्शाने वाले आयतचित्र (histogram) में प्रत्येक आयत का क्षेत्रफल क्या प्रदर्शित करता है?",
            "opts": [
                ("A", "Class frequency", "वर्ग बारंबारता (Class frequency)"),
                ("B", "Class mark", "वर्ग चिह्न"),
                ("C", "Cumulative frequency", "संचयी बारंबारता"),
                ("D", "Class interval width", "वर्ग अंतराल की चौड़ाई")
            ],
            "ans": "A",
            "solEn": "In a histogram, the area of each bar is proportional to the frequency of that class interval.",
            "solHi": "आयतचित्र में प्रत्येक आयत का क्षेत्रफल उस वर्ग अंतराल की बारंबारता के समानुपाती होता है।"
        },
        {
            "tag": "Mean Transformation",
            "qEn": "The mean of 10 observations is 25. If each observation is multiplied by 3 and then 5 is added, what will be the new mean?",
            "qHi": "10 प्रेक्षणों का माध्य 25 है। यदि प्रत्येक प्रेक्षण को 3 से गुणा किया जाए और फिर उसमें 5 जोड़ दिया जाए, तो नया माध्य क्या होगा?",
            "opts": [
                ("A", "75", "75"),
                ("B", "80", "80"),
                ("C", "30", "30"),
                ("D", "85", "85")
            ],
            "ans": "B",
            "solEn": "If every observation y = 3x + 5, then New Mean = 3(Old Mean) + 5 = 3(25) + 5 = 75 + 5 = 80.",
            "solHi": "यदि प्रत्येक प्रेक्षण में y = 3x + 5 किया जाए, तो नया माध्य = 3 &times; 25 + 5 = 80 होगा।"
        },
        {
            "tag": "SD Transformation",
            "qEn": "The standard deviation of a dataset is 6. If 4 is added to each observation, what is the new standard deviation?",
            "qHi": "एक डेटासेट का मानक विचलन 6 है। यदि प्रत्येक प्रेक्षण में 4 जोड़ दिया जाए, तो नया मानक विचलन क्या होगा?",
            "opts": [
                ("A", "10", "10"),
                ("B", "6", "6"),
                ("C", "24", "24"),
                ("D", "2", "2")
            ],
            "ans": "B",
            "solEn": "Standard deviation is independent of change of origin. Adding or subtracting a constant to all data points leaves the standard deviation unchanged (still 6).",
            "solHi": "मानक विचलन मूल बिंदु के परिवर्तन (जोड़ने या घटाने) से अप्रभावित रहता है। अतः नया मानक विचलन भी 6 ही रहेगा।"
        },
        {
            "tag": "Missing Frequency",
            "qEn": "The mean of the numbers 6, 8, 11, x, and 15 is 10. What is the value of x?",
            "qHi": "संख्याओं 6, 8, 11, x और 15 का माध्य 10 है। x का मान क्या है?",
            "opts": [
                ("A", "10", "10"),
                ("B", "12", "12"),
                ("C", "14", "14"),
                ("D", "8", "8")
            ],
            "ans": "A",
            "solEn": "Sum = 5 &times; 10 = 50. 6 + 8 + 11 + x + 15 = 40 + x = 50 &rarr; x = 50 - 40 = 10.",
            "solHi": "कुल योग = 5 &times; 10 = 50। 40 + x = 50 &rarr; x = 10।"
        },
        {
            "tag": "Inference Logic",
            "qEn": "A line graph shows that Company A's car sales were 10,000 in 2021, 15,000 in 2022, and 20,000 in 2023. Which conclusion is definitively true?",
            "qHi": "एक रेखा आरेख दर्शाता है कि कंपनी A की कार बिक्री 2021 में 10,000, 2022 में 15,000 और 2023 में 20,000 थी। कौन सा निष्कर्ष निश्चित रूप से सत्य है?",
            "opts": [
                ("A", "Company A had the highest market share in India", "कंपनी A की भारत में बाजार हिस्सेदारी सर्वाधिक थी"),
                ("B", "Sales increased by exactly 5,000 units each year", "बिक्री में प्रति वर्ष ठीक 5,000 इकाइयों की वृद्धि हुई"),
                ("C", "Sales will reach 25,000 in 2024", "2024 में बिक्री 25,000 तक पहुंच जाएगी"),
                ("D", "Profits doubled over the three years", "तीन वर्षों में लाभ दोगुना हो गया")
            ],
            "ans": "B",
            "solEn": "Only option B is a direct, verified mathematical fact from the data (15k - 10k = 5k; 20k - 15k = 5k). Market share, future 2024 sales, and profits are unstated assumptions.",
            "solHi": "केवल विकल्प B दिए गए आंकड़ों से प्रमाणित सत्य है (15k - 10k = 5k तथा 20k - 15k = 5k)। अन्य सभी अनुमान हैं।"
        },
        {
            "tag": "Symmetric Distribution",
            "qEn": "For a perfectly symmetric normal distribution curve, which relation holds true?",
            "qHi": "पूर्णतः सममित (symmetrical) सामान्य बंटन वक्र के लिए कौन सा संबंध सत्य है?",
            "opts": [
                ("A", "Mean > Median > Mode", "माध्य > माध्यिका > बहुलक"),
                ("B", "Mean < Median < Mode", "माध्य < माध्यिका < बहुलक"),
                ("C", "Mean = Median = Mode", "माध्य = माध्यिका = बहुलक"),
                ("D", "Mean = Mode &ne; Median", "माध्य = बहुलक &ne; माध्यिका")
            ],
            "ans": "C",
            "solEn": "In a perfectly symmetrical distribution, the Mean, Median, and Mode coincide at the exact center (Mean = Median = Mode).",
            "solHi": "पूर्णतः सममित वितरण में माध्य, माध्यिका और बहुलक तीनों का मान ठीक केंद्र में संपाती (समान) होता है।"
        },
        {
            "tag": "Grouped Median Class",
            "qEn": "For a grouped dataset with N = 60, in which cumulative frequency (cf) range does the median class fall?",
            "qHi": "N = 60 वाले वर्गीकृत डेटासेट के लिए माध्यिका वर्ग किस संचयी बारंबारता (cf) मान पर स्थित होता है?",
            "opts": [
                ("A", "First class where cf &ge; 30", "पहला वर्ग जहां cf &ge; 30 हो"),
                ("B", "First class where cf &ge; 60", "पहला वर्ग जहां cf &ge; 60 हो"),
                ("C", "Class with lowest frequency", "न्यूनतम बारंबारता वाला वर्ग"),
                ("D", "Class with midpoint 30", "मध्य बिंदु 30 वाला वर्ग")
            ],
            "ans": "A",
            "solEn": "The median class is the first class interval whose cumulative frequency is greater than or equal to N/2 = 60/2 = 30.",
            "solHi": "माध्यिका वर्ग वह पहला वर्ग अंतराल होता है जिसकी संचयी बारंबारता N/2 = 60/2 = 30 के बराबर या उससे अधिक होती है।"
        },
        {
            "tag": "Empirical Relationship",
            "qEn": "If Mode = 18 and Mean = 24, find the Median using the empirical formula.",
            "qHi": "यदि बहुलक = 18 तथा माध्य = 24 है, तो अनुभवजन्य सूत्र का उपयोग करके माध्यिका ज्ञात कीजिए।",
            "opts": [
                ("A", "20", "20"),
                ("B", "21", "21"),
                ("C", "22", "22"),
                ("D", "23", "23")
            ],
            "ans": "C",
            "solEn": "Mode = 3(Median) - 2(Mean) &rarr; 18 = 3(Median) - 2(24) &rarr; 18 = 3(Median) - 48 &rarr; 3(Median) = 66 &rarr; Median = 22.",
            "solHi": "18 = 3(माध्यिका) - 48 &rarr; 3(माध्यिका) = 66 &rarr; माध्यिका = 22।"
        },
        {
            "tag": "Frequency Polygon",
            "qEn": "A frequency polygon is constructed by plotting frequency against which parameter on the X-axis?",
            "qHi": "आवृत्ति बहुभुज (frequency polygon) का निर्माण X-अक्ष पर किस मान के विरुद्ध आवृत्ति को आलेखित करके किया जाता है?",
            "opts": [
                ("A", "Lower class limit", "निम्न वर्ग सीमा"),
                ("B", "Upper class limit", "उच्च वर्ग सीमा"),
                ("C", "Class mark (Midpoint)", "वर्ग चिह्न (मध्य बिंदु)"),
                ("D", "Cumulative frequency", "संचयी बारंबारता")
            ],
            "ans": "C",
            "solEn": "A frequency polygon plots frequencies against the midpoints (class marks) of each class interval, joined by straight lines.",
            "solHi": "आवृत्ति बहुभुज में आवृत्तियों को वर्ग अंतरालों के मध्य बिंदुओं (वर्ग चिह्न) के विरुद्ध आलेखित किया जाता है।"
        },
        {
            "tag": "Mean Deviation",
            "qEn": "What is the mean deviation about the mean for the observations: 3, 5, 7, 9, 11?",
            "qHi": "प्रेक्षणों 3, 5, 7, 9, 11 के लिए माध्य के सापेक्ष माध्य विचलन क्या है?",
            "opts": [
                ("A", "2.0", "2.0"),
                ("B", "2.4", "2.4"),
                ("C", "3.0", "3.0"),
                ("D", "1.6", "1.6")
            ],
            "ans": "B",
            "solEn": "Mean = (3+5+7+9+11)/5 = 35/5 = 7. Deviations |x - Mean|: |3-7|=4, |5-7|=2, |7-7|=0, |9-7|=2, |11-7|=4. Sum = 4+2+0+2+4 = 12. Mean Deviation = 12 / 5 = 2.4.",
            "solHi": "माध्य = 7। विचलन |x - 7| = 4, 2, 0, 2, 4। योग = 12। माध्य विचलन = 12 / 5 = 2.4।"
        },
        {
            "tag": "Variance Calculation",
            "qEn": "Find the variance of the numbers: 2, 4, 6, 8, 10.",
            "qHi": "संख्याओं 2, 4, 6, 8, 10 का प्रसरण (variance) ज्ञात कीजिए।",
            "opts": [
                ("A", "8", "8"),
                ("B", "10", "10"),
                ("C", "6", "6"),
                ("D", "4", "4")
            ],
            "ans": "A",
            "solEn": "Mean = 6. Squared deviations (x - 6)^2: (2-6)^2=16, (4-6)^2=4, (6-6)^2=0, (8-6)^2=4, (10-6)^2=16. Sum = 40. Variance = 40 / 5 = 8.",
            "solHi": "माध्य = 6। विचलनों का वर्ग = 16 + 4 + 0 + 4 + 16 = 40। प्रसरण = 40 / 5 = 8।"
        },
        {
            "tag": "Cumulative Frequency Type",
            "qEn": "The 'Less than' cumulative frequency of the last class interval in a distribution always equals:",
            "qHi": "किसी बंटन में अंतिम वर्ग अंतराल की 'से कम' संचयी बारंबारता सदैव किसके बराबर होती है?",
            "opts": [
                ("A", "Zero", "शून्य"),
                ("B", "Total frequency N", "कुल बारंबारता N"),
                ("C", "Median", "माध्यिका"),
                ("D", "Mean", "माध्य")
            ],
            "ans": "B",
            "solEn": "The cumulative frequency of the final class interval aggregates all frequencies and therefore always equals the total number of observations (N).",
            "solHi": "अंतिम वर्ग अंतराल की संचयी आवृत्ति सभी आवृत्तियों का कुल योग होती है, अतः यह सदैव N के बराबर होती है।"
        },
        {
            "tag": "Diagrammatic Inference",
            "qEn": "A bar chart compares rainfall across 5 districts. District P has 120 cm and District Q has 60 cm. Which statement is correct?",
            "qHi": "एक दंड आरेख 5 जिलों में वर्षा की तुलना करता है। जिला P में 120 सेमी और जिला Q में 60 सेमी वर्षा हुई। कौन सा कथन सही है?",
            "opts": [
                ("A", "District P received 100% more rainfall than District Q", "जिला P में जिला Q की तुलना में 100% अधिक वर्षा हुई"),
                ("B", "District P received 50% more rainfall than District Q", "जिला P में जिला Q की तुलना में 50% अधिक वर्षा हुई"),
                ("C", "District Q received 100% less rainfall than District P", "जिला Q में जिला P की तुलना में 100% कम वर्षा हुई"),
                ("D", "District P received double the rainfall of all other districts", "जिला P में अन्य सभी जिलों से दोगुनी वर्षा हुई")
            ],
            "ans": "A",
            "solEn": "Difference = 120 - 60 = 60 cm. Percentage more than Q = (60 / 60) &times; 100 = 100%.",
            "solHi": "अंतर = 120 - 60 = 60 सेमी। Q से प्रतिशत अधिक = (60 / 60) &times; 100 = 100%।"
        },
        {
            "tag": "Median Property",
            "qEn": "Which measure of central tendency is least affected by extreme outlier values?",
            "qHi": "केंद्रीय प्रवृत्ति का कौन सा माप चरम मानों (outliers) से सबसे कम प्रभावित होता है?",
            "opts": [
                ("A", "Arithmetic Mean", "समांतर माध्य"),
                ("B", "Median", "माध्यिका"),
                ("C", "Range", "विस्तार"),
                ("D", "Standard Deviation", "मानक विचलन")
            ],
            "ans": "B",
            "solEn": "Median is a positional average and depends only on the rank order of items, making it immune to extreme outlier values (unlike Mean and Range).",
            "solHi": "माध्यिका एक स्थितिक औसत है और केवल क्रम पर निर्भर करती है, अतः यह चरम मानों (outliers) से प्रभावित नहीं होती।"
        },
        {
            "tag": "Weighted Mean Calculation",
            "qEn": "A student scores 70 in Hindi (weight 1), 80 in English (weight 2), and 90 in Math (weight 3). What is his weighted average score?",
            "qHi": "एक छात्र हिंदी में 70 (भार 1), अंग्रेजी में 80 (भार 2) और गणित में 90 (भार 3) अंक प्राप्त करता है। उसका भारित औसत अंक क्या है?",
            "opts": [
                ("A", "80.0", "80.0"),
                ("B", "83.33", "83.33"),
                ("C", "85.0", "85.0"),
                ("D", "82.5", "82.5")
            ],
            "ans": "B",
            "solEn": "Weighted sum = 1(70) + 2(80) + 3(90) = 70 + 160 + 270 = 500. Sum of weights = 1 + 2 + 3 = 6. Weighted Mean = 500 / 6 = 83.33.",
            "solHi": "भारित योग = 70 + 160 + 270 = 500। भारों का योग = 6। भारित औसत = 500 / 6 = 83.33।"
        },
        {
            "tag": "Qualitative Data",
            "qEn": "Which average is best suited for qualitative categorical data such as shoe size, t-shirt size, or consumer brand preference?",
            "qHi": "जूते का आकार, टी-शर्ट का आकार या उपभोक्ता ब्रांड वरीयता जैसे गुणात्मक डेटा के लिए कौन सा औसत सर्वोत्तम है?",
            "opts": [
                ("A", "Arithmetic Mean", "समांतर माध्य"),
                ("B", "Median", "माध्यिका"),
                ("C", "Mode", "बहुलक"),
                ("D", "Geometric Mean", "गुणोत्तर माध्य")
            ],
            "ans": "C",
            "solEn": "Mode identifies the most common/popular category and is the only central tendency measure applicable to nominal/categorical data.",
            "solHi": "बहुलक सबसे लोकप्रिय या सामान्य श्रेणी को दर्शाता है, जो गुणात्मक डेटा के लिए सर्वोत्तम है।"
        },
        {
            "tag": "Open-Ended Classes",
            "qEn": "In a frequency table with open-ended class intervals (e.g., 'Below 20' or 'Above 80'), which central measure can still be accurately determined?",
            "qHi": "खुले सिरे वाले वर्ग अंतरालों (जैसे '20 से कम' या '80 से अधिक') वाली तालिका में किस केंद्रीय माप को सटीक रूप से ज्ञात किया जा सकता है?",
            "opts": [
                ("A", "Mean", "माध्य"),
                ("B", "Median", "माध्यिका"),
                ("C", "Standard Deviation", "मानक विचलन"),
                ("D", "Variance", "प्रसरण")
            ],
            "ans": "B",
            "solEn": "The median depends only on the middle position and does not require knowledge of extreme boundary limits, making it calculable for open-ended tables.",
            "solHi": "माध्यिका मध्य पद की स्थिति पर निर्भर करती है और इसमें सिरों के सटीक मान की आवश्यकता नहीं होती, अतः यह ज्ञात की जा सकती है।"
        },
        {
            "tag": "Inference Question",
            "qEn": "If the correlation coefficient between expenditure on advertising and sales is +0.92, what can be inferred?",
            "qHi": "यदि विज्ञापन पर व्यय और बिक्री के बीच सह-संबंध गुणांक +0.92 है, तो क्या निष्कर्ष निकाला जा सकता है?",
            "opts": [
                ("A", "Strong positive relationship between advertising and sales", "विज्ञापन और बिक्री के बीच मजबूत धनात्मक संबंध है"),
                ("B", "Advertising caused exactly 92% of sales", "विज्ञापन ने ठीक 92% बिक्री उत्पन्न की"),
                ("C", "Sales will decrease if advertising increases", "विज्ञापन बढ़ने पर बिक्री घटेगी"),
                ("D", "Advertising expenditure is equal to sales", "विज्ञापन व्यय बिक्री के बराबर है")
            ],
            "ans": "A",
            "solEn": "A correlation coefficient close to +1 indicates a strong positive linear relationship between the two variables.",
            "solHi": "+0.92 का सह-संबंध गुणांक दोनों चरों के बीच मजबूत धनात्मक रैखिक संबंध को प्रमाणित करता है।"
        },
        {
            "tag": "Median Graphical",
            "qEn": "Which graphical representation can be used directly to partition data into quartiles and percentiles?",
            "qHi": "डेटा को चतुर्थक (quartiles) और शतमक (percentiles) में विभाजित करने के लिए किस आरेख का सीधा उपयोग किया जा सकता है?",
            "opts": [
                ("A", "Bar Graph", "दंड आरेख"),
                ("B", "Pie Chart", "पाई चार्ट"),
                ("C", "Cumulative Frequency Curve (Ogive)", "संचयी बारंबारता वक्र (ओजाइव)"),
                ("D", "Line Chart", "रेखा आरेख")
            ],
            "ans": "C",
            "solEn": "An Ogive allows graphical location of any positional measure: Q1 at N/4, Median at N/2, Q3 at 3N/4, and percentiles at Pk = (k/100)N.",
            "solHi": "तोरण (ओजाइव) से Q1 (N/4), माध्यिका (N/2), Q3 (3N/4) तथा किसी भी शतमक की स्थिति सीधे ज्ञात की जा सकती है।"
        },
        {
            "tag": "Class Mark",
            "qEn": "What is the class mark and class width of the interval 35 &ndash; 45?",
            "qHi": "वर्ग अंतराल 35 &ndash; 45 का वर्ग चिह्न और वर्ग विस्तार क्या है?",
            "opts": [
                ("A", "Class mark = 40, Width = 10", "वर्ग चिह्न = 40, विस्तार = 10"),
                ("B", "Class mark = 10, Width = 40", "वर्ग चिह्न = 10, विस्तार = 40"),
                ("C", "Class mark = 45, Width = 35", "वर्ग चिह्न = 45, विस्तार = 35"),
                ("D", "Class mark = 80, Width = 10", "वर्ग चिह्न = 80, विस्तार = 10")
            ],
            "ans": "A",
            "solEn": "Class mark (midpoint) = (35 + 45)/2 = 80/2 = 40. Class width = Upper - Lower = 45 - 35 = 10.",
            "solHi": "वर्ग चिह्न = (35 + 45)/2 = 40। वर्ग विस्तार = 45 - 35 = 10।"
        },
        {
            "tag": "Relative Frequency",
            "qEn": "In a sample of 250 items, 45 items belong to Category A. What is the relative frequency of Category A?",
            "qHi": "250 मदों के नमूने में, 45 मदें श्रेणी A की हैं। श्रेणी A की सापेक्ष बारंबारता (relative frequency) क्या है?",
            "opts": [
                ("A", "0.18", "0.18"),
                ("B", "0.45", "0.45"),
                ("C", "0.20", "0.20"),
                ("D", "0.15", "0.15")
            ],
            "ans": "A",
            "solEn": "Relative frequency = Category frequency / Total sample size = 45 / 250 = 9 / 50 = 0.18 (or 18%).",
            "solHi": "सापेक्ष बारंबारता = श्रेणी बारंबारता / कुल आकार = 45 / 250 = 0.18 (या 18%)।"
        },
        {
            "tag": "Sum of Deviations",
            "qEn": "The algebraic sum of deviations of a set of observations taken from their arithmetic mean is always:",
            "qHi": "किसी प्रेक्षण समुच्चय के समांतर माध्य से लिए गए विचलनों का बीजगणितीय योग सदैव होता है:",
            "opts": [
                ("A", "Always positive", "सदैव धनात्मक"),
                ("B", "Always zero", "सदैव शून्य"),
                ("C", "Always negative", "सदैव ऋणात्मक"),
                ("D", "Equal to standard deviation", "मानक विचलन के बराबर")
            ],
            "ans": "B",
            "solEn": "Fundamental mathematical property: &sum;(x_i - X&#772;) = 0. The sum of positive deviations exactly cancels the sum of negative deviations.",
            "solHi": "मूलभूत सांख्यिकीय गुण: समांतर माध्य से लिए गए विचलनों का बीजगणितीय योग &sum;(x_i - X&#772;) सदैव शून्य (0) होता है।"
        }
    ],

    # 15 Mini-Test MCQs
    "testQuestions": [
        {
            "qEn": "If Mean = 32 and Median = 30, what is the Mode in an empirical distribution?",
            "qHi": "यदि माध्य = 32 और माध्यिका = 30 है, तो अनुभवजन्य सूत्रानुसार बहुलक क्या होगा?",
            "opts": [
                ("A", "26", "26"),
                ("B", "28", "28"),
                ("C", "31", "31"),
                ("D", "34", "34")
            ]
        },
        {
            "qEn": "Find the median of: 8, 15, 3, 21, 12, 18, 9.",
            "qHi": "संख्याओं 8, 15, 3, 21, 12, 18, 9 की माध्यिका क्या है?",
            "opts": [
                ("A", "12", "12"),
                ("B", "15", "15"),
                ("C", "9", "9"),
                ("D", "13.5", "13.5")
            ]
        },
        {
            "qEn": "If variance of a data series is 81, what is the standard deviation?",
            "qHi": "यदि एक डेटा श्रेणी का प्रसरण 81 है, तो मानक विचलन क्या है?",
            "opts": [
                ("A", "9", "9"),
                ("B", "&plusmn;9", "&plusmn;9"),
                ("C", "40.5", "40.5"),
                ("D", "18", "18")
            ]
        },
        {
            "qEn": "The intersection point of 'Less than' and 'More than' ogives gives which value on the X-axis?",
            "qHi": "'से कम' और 'से अधिक' तोरण वक्रों का प्रतिच्छेद बिंदु X-अक्ष पर कौन सा मान देता है?",
            "opts": [
                ("A", "Mean", "माध्य"),
                ("B", "Median", "माध्यिका"),
                ("C", "Mode", "बहुलक"),
                ("D", "Range", "परास")
            ]
        },
        {
            "qEn": "If each value in a dataset is doubled, what happens to the standard deviation?",
            "qHi": "यदि किसी डेटासेट के प्रत्येक मान को दोगुना कर दिया जाए, तो मानक विचलन पर क्या प्रभाव पड़ेगा?",
            "opts": [
                ("A", "Remains unchanged", "अपरिवर्तित रहेगा"),
                ("B", "Doubles", "दोगुना हो जाएगा"),
                ("C", "Quadruples", "चार गुना हो जाएगा"),
                ("D", "Becomes half", "आधा हो जाएगा")
            ]
        },
        {
            "qEn": "What is the mode of: 11, 14, 11, 19, 14, 23, 14, 18, 14?",
            "qHi": "संख्याओं 11, 14, 11, 19, 14, 23, 14, 18, 14 का बहुलक क्या है?",
            "opts": [
                ("A", "11", "11"),
                ("B", "14", "14"),
                ("C", "19", "19"),
                ("D", "16", "16")
            ]
        },
        {
            "qEn": "Find the range of the scores: 42, 68, 29, 95, 51, 84.",
            "qHi": "प्राप्तांकों 42, 68, 29, 95, 51, 84 का विस्तार (range) ज्ञात कीजिए।",
            "opts": [
                ("A", "66", "66"),
                ("B", "53", "53"),
                ("C", "70", "70"),
                ("D", "64", "64")
            ]
        },
        {
            "qEn": "Which measure is most suitable for describing the average wage when extreme executive salaries distort the data?",
            "qHi": "जब कुछ अधिकारियों का अत्यधिक उच्च वेतन औसत को बिगाड़ रहा हो, तो औसत मजदूरी दर्शाने के लिए कौन सा माप सबसे उपयुक्त है?",
            "opts": [
                ("A", "Arithmetic Mean", "समांतर माध्य"),
                ("B", "Median", "माध्यिका"),
                ("C", "Range", "विस्तार"),
                ("D", "Harmonic Mean", "हरात्मक माध्य")
            ]
        },
        {
            "qEn": "For a symmetrical distribution with Mean = 50, what are the Median and Mode?",
            "qHi": "माध्य = 50 वाले एक सममित बंटन के लिए माध्यिका और बहुलक क्या होंगे?",
            "opts": [
                ("A", "Median = 50, Mode = 50", "माध्यिका = 50, बहुलक = 50"),
                ("B", "Median = 45, Mode = 55", "माध्यिका = 45, बहुलक = 55"),
                ("C", "Median = 50, Mode = 0", "माध्यिका = 50, बहुलक = 0"),
                ("D", "Cannot be determined", "निर्धारित नहीं किया जा सकता")
            ]
        },
        {
            "qEn": "Mean of 5 numbers is 18. If one number is excluded, the mean becomes 16. What was the excluded number?",
            "qHi": "5 संख्याओं का माध्य 18 है। यदि एक संख्या हटा दी जाए, तो माध्य 16 हो जाता है। हटाई गई संख्या क्या थी?",
            "opts": [
                ("A", "24", "24"),
                ("B", "26", "26"),
                ("C", "28", "28"),
                ("D", "30", "30")
            ]
        },
        {
            "qEn": "What is the Coefficient of Variation if Mean = 50 and SD = 5?",
            "qHi": "यदि माध्य = 50 और मानक विचलन = 5 है, तो विचरण गुणांक (CV) क्या होगा?",
            "opts": [
                ("A", "5%", "5%"),
                ("B", "10%", "10%"),
                ("C", "25%", "25%"),
                ("D", "50%", "50%")
            ]
        },
        {
            "qEn": "In a histogram, the widths of the rectangles are proportional to:",
            "qHi": "आयतचित्र में आयतों की चौड़ाई किसके समानुपाती होती है?",
            "opts": [
                ("A", "Class frequency", "वर्ग आवृत्ति"),
                ("B", "Class interval width", "वर्ग अंतराल की चौड़ाई"),
                ("C", "Cumulative frequency", "संचयी बारंबारता"),
                ("D", "Mean deviation", "माध्य विचलन")
            ]
        },
        {
            "qEn": "What is the algebraic sum of deviations of 12, 16, 20 from their mean 16?",
            "qHi": "संख्याओं 12, 16, 20 का उनके माध्य 16 से विचलनों का बीजगणितीय योग क्या है?",
            "opts": [
                ("A", "0", "0"),
                ("B", "4", "4"),
                ("C", "8", "8"),
                ("D", "-4", "-4")
            ]
        },
        {
            "qEn": "Find the median of the first 8 prime numbers: 2, 3, 5, 7, 11, 13, 17, 19.",
            "qHi": "प्रथम 8 अभाज्य संख्याओं (2, 3, 5, 7, 11, 13, 17, 19) की माध्यिका क्या है?",
            "opts": [
                ("A", "7", "7"),
                ("B", "9", "9"),
                ("C", "11", "11"),
                ("D", "8.5", "8.5")
            ]
        },
        {
            "qEn": "In a graph, if the curve is strictly increasing, what can be deduced about the rate of growth?",
            "qHi": "यदि एक ग्राफ में वक्र निरंतर ऊपर की ओर बढ़ रहा है, तो संवृद्धि दर के बारे में क्या कहा जा सकता है?",
            "opts": [
                ("A", "Growth rate is always positive", "संवृद्धि दर सदैव धनात्मक है"),
                ("B", "Growth rate is constant", "संवृद्धि दर स्थिर है"),
                ("C", "Growth rate is negative", "संवृद्धि दर ऋणात्मक है"),
                ("D", "Growth rate is zero", "संवृद्धि दर शून्य है")
            ]
        }
    ],

    "testDataJson": json.dumps([
        {"ans": "A", "solEn": "Mode = 3(30) - 2(32) = 90 - 64 = 26.", "solHi": "बहुलक = 3(30) - 2(32) = 90 - 64 = 26।"},
        {"ans": "A", "solEn": "Ascending: 3, 8, 9, 12, 15, 18, 21. Middle term (4th) = 12.", "solHi": "आरोही क्रम: 3, 8, 9, 12, 15, 18, 21। चौथा पद = 12।"},
        {"ans": "A", "solEn": "SD = &radic;(81) = 9.", "solHi": "मानक विचलन = &radic;(81) = 9।"},
        {"ans": "B", "solEn": "The X-coordinate of intersection of two ogives gives the Median.", "solHi": "दो तोरण वक्रों का प्रतिच्छेद बिंदु X-अक्ष पर माध्यिका देता है।"},
        {"ans": "B", "solEn": "SD changes with scale. If each x is multiplied by 2, new SD = 2 &times; Old SD.", "solHi": "पैमाने के परिवर्तन से मानक विचलन उसी अनुपात में बदलता है। 2 से गुणा करने पर नया SD दोगुना होगा।"},
        {"ans": "B", "solEn": "14 occurs four times (highest frequency).", "solHi": "14 सर्वाधिक 4 बार आया है, अतः बहुलक 14 है।"},
        {"ans": "A", "solEn": "Range = Highest (95) - Lowest (29) = 66.", "solHi": "परास = 95 - 29 = 66।"},
        {"ans": "B", "solEn": "Median is unaffected by extreme outliers and represents central income best.", "solHi": "माध्यिका चरम मानों से प्रभावित नहीं होती, अतः वेतन वितरण हेतु सर्वोत्तम है।"},
        {"ans": "A", "solEn": "In symmetrical distribution: Mean = Median = Mode = 50.", "solHi": "सममित बंटन में माध्य = माध्यिका = बहुलक = 50।"},
        {"ans": "B", "solEn": "Old sum = 5 &times; 18 = 90. New sum = 4 &times; 16 = 64. Excluded number = 90 - 64 = 26.", "solHi": "पुराना योग = 90। नया योग = 64। हटाई गई संख्या = 90 - 64 = 26।"},
        {"ans": "B", "solEn": "CV = (5/50) &times; 100 = 10%.", "solHi": "CV = (5/50) &times; 100 = 10%।"},
        {"ans": "B", "solEn": "Histogram rectangle widths represent class intervals (Upper limit - Lower limit).", "solHi": "आयत की चौड़ाई वर्ग अंतराल के विस्तार को दर्शाती है।"},
        {"ans": "A", "solEn": "(12-16) + (16-16) + (20-16) = -4 + 0 + 4 = 0.", "solHi": "-4 + 0 + 4 = 0।"},
        {"ans": "B", "solEn": "Primes: 2, 3, 5, 7, 11, 13, 17, 19. Median = (7 + 11)/2 = 18/2 = 9.", "solHi": "माध्यिका = (7 + 11)/2 = 9।"},
        {"ans": "A", "solEn": "An increasing curve has positive slope &Delta;y/&Delta;x > 0, meaning growth rate is positive.", "solHi": "बढ़ते हुए वक्र का ढाल धनात्मक होता है, अर्थात संवृद्धि दर सदैव धनात्मक है।"}
    ])
}
