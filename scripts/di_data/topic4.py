"""
topic4.py
Topic 4: Pie Chart Interpretation: Degrees, Percentages & Dual Charts
Slug: pie-chart-interpretation-and-analysis
"""

import json

TOPIC_4 = {
    "slug": "pie-chart-interpretation-and-analysis",
    "titleEn": "Pie Chart Interpretation: Degrees & Dual Charts",
    "titleHi": "पाई चार्ट व्याख्या: अंश कोण, प्रतिशत व द्वि-चार्ट",
    "pageTitle": "Pie Chart Interpretation: Degrees, Percentages & Dual Charts | UPSSSC Mains | SJMaths",
    "metaDesc": "Exhaustive pointwise study notes, 30 practice MCQs with detailed mathematical explanations, and a 15-Q mini test on Pie Charts (Degree-to-Percentage conversion, Dual Pie Charts, and Mixed DI) for UPSSSC Intermediate Level Mains 2026.",
    "metaTagEn": "Part-1 (9): Data Interpretation & Statistical Analysis | Pie Charts & Angle Conversions",
    "metaTagHi": "भाग-1 (9): डाटा इंटरप्रिटेशन एवं सांख्यिकीय विश्लेषण | पाई चार्ट एवं अंश कोण रूपांतरण",
    "subtitleEn": "Master single and dual pie charts, degree-to-percentage conversions (360° = 100%), central angles, and speed calculation shortcuts for UPSSSC Intermediate Level Mains.",
    "subtitleHi": "एकल व द्वि-पाई चार्ट, अंश-प्रतिशत रूपांतरण (360° = 100%), केंद्रीय कोण और तीव्र गणना शॉर्टकट की संपूर्ण मार्गदर्शिका यूपीएसएसएससी मुख्य परीक्षा हेतु।",
    "crumbNameEn": "Pie Chart Interpretation",
    "crumbNameHi": "पाई चार्ट व्याख्या",

    "notesHtml": """
        <!-- Section 1: Fundamentals of Pie Charts & Angle-Percentage Mathematics -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-chart-pie"></i>
                <span class="lang-en">1. Mathematical Fundamentals of Pie Charts</span>
                <span class="lang-hi">1. पाई चार्ट के मूलभूत गणितीय नियम</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Universal Circular Equivalence:</strong> A full circle spans 360&deg; at its center, representing 100% of the aggregate total.
                <br>&bull; <code>1% = 3.6&deg;</code> (To convert percent to angle, multiply by 3.6)
                <br>&bull; <code>1&deg; = 10/36% = 5/18% &approx; 0.278%</code> (To convert angle to percent, divide by 3.6 or multiply by 5/18)
                <br>&bull; <code>Central Angle (&theta;) = (Sector Value / Grand Total) &times; 360&deg;</code></span>
                <span class="lang-hi"><strong>सार्वभौमिक वृत्तीय तुल्यता:</strong> एक संपूर्ण वृत्त अपने केंद्र पर 360&deg; का कोण बनाता है, जो कुल योग के 100% को प्रदर्शित करता है।
                <br>&bull; <code>1% = 3.6&deg;</code> (प्रतिशत को कोण में बदलने के लिए 3.6 से गुणा करें)
                <br>&bull; <code>1&deg; = 5/18% &approx; 0.278%</code> (कोण को प्रतिशत में बदलने के लिए 3.6 से भाग दें या 5/18 से गुणा करें)
                <br>&bull; <code>केंद्रीय कोण (&theta;) = (त्रिज्यखंड का मान / कुल योग) &times; 360&deg;</code></span>
            </div>

            <!-- Table of Angle-Percentage Reference -->
            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Percentage (%)</span><span class="lang-hi">प्रतिशत (%)</span></th>
                            <th><span class="lang-en">Central Angle (Degrees)</span><span class="lang-hi">केंद्रीय कोण (अंश / Degree)</span></th>
                            <th><span class="lang-en">Fraction of Circle</span><span class="lang-hi">वृत्त का भिन्न भाग</span></th>
                            <th><span class="lang-en">Quick Calculation Shortcut</span><span class="lang-hi">गणना शॉर्टकट</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>5%</strong></td>
                            <td>18&deg;</td>
                            <td>1/20</td>
                            <td>Divide total by 20</td>
                        </tr>
                        <tr>
                            <td><strong>10%</strong></td>
                            <td>36&deg;</td>
                            <td>1/10</td>
                            <td>Move decimal one place left</td>
                        </tr>
                        <tr>
                            <td><strong>12.5%</strong></td>
                            <td>45&deg;</td>
                            <td>1/8</td>
                            <td>Half of a right angle</td>
                        </tr>
                        <tr>
                            <td><strong>15%</strong></td>
                            <td>54&deg;</td>
                            <td>3/20</td>
                            <td>36&deg; + 18&deg;</td>
                        </tr>
                        <tr>
                            <td><strong>20%</strong></td>
                            <td>72&deg;</td>
                            <td>1/5</td>
                            <td>36&deg; &times; 2</td>
                        </tr>
                        <tr>
                            <td><strong>25%</strong></td>
                            <td>90&deg;</td>
                            <td>1/4</td>
                            <td>Right angle (One quadrant)</td>
                        </tr>
                        <tr>
                            <td><strong>30%</strong></td>
                            <td>108&deg;</td>
                            <td>3/10</td>
                            <td>36&deg; &times; 3</td>
                        </tr>
                        <tr>
                            <td><strong>33.33%</strong></td>
                            <td>120&deg;</td>
                            <td>1/3</td>
                            <td>One-third of 360&deg;</td>
                        </tr>
                        <tr>
                            <td><strong>40%</strong></td>
                            <td>144&deg;</td>
                            <td>2/5</td>
                            <td>72&deg; &times; 2</td>
                        </tr>
                        <tr>
                            <td><strong>50%</strong></td>
                            <td>180&deg;</td>
                            <td>1/2</td>
                            <td>Straight diameter line</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Single Pie Chart SVG -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 4.1: Monthly Household Expenditure Budget (Total = ₹80,000 / Month)</span>
                    <span class="lang-hi">चित्र 4.1: मासिक पारिवारिक व्यय बजट (कुल व्यय = ₹80,000 / माह)</span>
                </h4>
                <svg viewBox="0 0 680 320" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Single Pie Chart for Household Budget">
                    <g transform="translate(180, 160)">
                        <!-- Food: 30% (108 deg): from -90 to 18 deg -->
                        <path d="M 0 0 L 0 -130 A 130 130 0 0 1 123.6 40.2 Z" fill="#0d9488" stroke="#ffffff" stroke-width="2"/>
                        <!-- Rent: 20% (72 deg): from 18 to 90 deg -->
                        <path d="M 0 0 L 123.6 40.2 A 130 130 0 0 1 0 130 Z" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
                        <!-- Education: 15% (54 deg): from 90 to 144 deg -->
                        <path d="M 0 0 L 0 130 A 130 130 0 0 1 -105.2 76.4 Z" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>
                        <!-- Savings: 15% (54 deg): from 144 to 198 deg -->
                        <path d="M 0 0 L -105.2 76.4 A 130 130 0 0 1 -123.6 -40.2 Z" fill="#10b981" stroke="#ffffff" stroke-width="2"/>
                        <!-- Transport: 10% (36 deg): from 198 to 234 deg -->
                        <path d="M 0 0 L -123.6 -40.2 A 130 130 0 0 1 -76.4 -105.2 Z" fill="#8b5cf6" stroke="#ffffff" stroke-width="2"/>
                        <!-- Misc: 10% (36 deg): from 234 to 270 deg -->
                        <path d="M 0 0 L -76.4 -105.2 A 130 130 0 0 1 0 -130 Z" fill="#ec4899" stroke="#ffffff" stroke-width="2"/>

                        <!-- Center hole for donut aesthetic -->
                        <circle cx="0" cy="0" r="45" fill="var(--planner-bg-surface)" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="0" y="5" fill="#182e26" font-size="13" font-weight="bold" text-anchor="middle">₹80,000</text>
                    </g>

                    <!-- Legend & Details on the right side -->
                    <g transform="translate(360, 45)">
                        <rect x="0" y="0" width="16" height="16" rx="3" fill="#0d9488"/>
                        <text x="25" y="13" fill="#182e26" font-size="13" font-weight="bold">Food (भोजन): 30% (108&deg;) = ₹24,000</text>

                        <rect x="0" y="35" width="16" height="16" rx="3" fill="#f59e0b"/>
                        <text x="25" y="48" fill="#182e26" font-size="13" font-weight="bold">Rent (किराया): 20% (72&deg;) = ₹16,000</text>

                        <rect x="0" y="70" width="16" height="16" rx="3" fill="#2563eb"/>
                        <text x="25" y="83" fill="#182e26" font-size="13" font-weight="bold">Education (शिक्षा): 15% (54&deg;) = ₹12,000</text>

                        <rect x="0" y="105" width="16" height="16" rx="3" fill="#10b981"/>
                        <text x="25" y="118" fill="#182e26" font-size="13" font-weight="bold">Savings (बचत): 15% (54&deg;) = ₹12,000</text>

                        <rect x="0" y="140" width="16" height="16" rx="3" fill="#8b5cf6"/>
                        <text x="25" y="153" fill="#182e26" font-size="13" font-weight="bold">Transport (परिवहन): 10% (36&deg;) = ₹8,000</text>

                        <rect x="0" y="175" width="16" height="16" rx="3" fill="#ec4899"/>
                        <text x="25" y="188" fill="#182e26" font-size="13" font-weight="bold">Misc (विविध): 10% (36&deg;) = ₹8,000</text>

                        <line x1="0" y1="205" x2="280" y2="205" stroke="#cbd5e1" stroke-width="1.5"/>
                        <text x="0" y="225" fill="#0f766e" font-size="13" font-weight="bold">Total: 100% (360&deg;) = ₹80,000 / month</text>
                    </g>
                </svg>
            </div>
        </section>

        <!-- Section 2: Dual (Double) Pie Chart Analysis Rules -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-layer-group"></i>
                <span class="lang-en">2. Dual (Double) Pie Charts: Analysis Rules &amp; Traps</span>
                <span class="lang-hi">2. द्वि (डबल) पाई चार्ट: विश्लेषण नियम एवं सावधानियां</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>The Cardinal Law of Dual Pie Charts:</strong>
                <br>NEVER directly compare or subtract percentage slices from two different pie charts!
                <br>&bull; Example: In Chart 1 (Total = ₹40 Lakh), Department A is 25% (= ₹10 Lakh).
                <br>&bull; In Chart 2 (Total = ₹80 Lakh), Department A is 20% (= ₹16 Lakh).
                <br><em>Trap:</em> Candidate thinks Department A's budget decreased from 25% to 20%. In reality, the budget <strong>increased from ₹10 Lakh to ₹16 Lakh (+60%)</strong>! Always calculate the absolute value using the respective total base!</span>
                <span class="lang-hi"><strong>डबल पाई चार्ट का सर्वोच्च नियम:</strong>
                <br>दो अलग-अलग पाई चार्टों के प्रतिशत मानों को कभी भी सीधे न जोड़ें और न ही घटाएं!
                <br>&bull; उदाहरण: चार्ट 1 (कुल = ₹40 लाख) में विभाग A का 25% (= ₹10 लाख) है।
                <br>&bull; चार्ट 2 (कुल = ₹80 लाख) में विभाग A का 20% (= ₹16 लाख) है।
                <br><em>भ्रम:</em> छात्र सोचते हैं कि बजट 25% से घटकर 20% हो गया। वास्तविकता में बजट <strong>₹10 लाख से बढ़कर ₹16 लाख (+60%)</strong> हो गया! हमेशा संबंधित कुल आधार का उपयोग करके वास्तविक मान निकालें!</span>
            </div>

            <!-- Dual Pie Chart SVG -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 4.2: Dual Pie Chart — Budget Allocation: 2023 (₹40 Lakh) vs 2024 (₹60 Lakh)</span>
                    <span class="lang-hi">चित्र 4.2: द्वि-पाई चार्ट — बजट आवंटन: 2023 (₹40 लाख) बनाम 2024 (₹60 लाख)</span>
                </h4>
                <svg viewBox="0 0 680 270" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Dual Pie Charts comparing 2023 and 2024">
                    <!-- Left Circle: 2023 (Total = 40 Lakh) -->
                    <g transform="translate(160, 130)">
                        <!-- Marketing: 25% (90 deg) -->
                        <path d="M 0 0 L 0 -90 A 90 90 0 0 1 90 0 Z" fill="#0d9488" stroke="#ffffff" stroke-width="2"/>
                        <!-- R&D: 35% (126 deg) -->
                        <path d="M 0 0 L 90 0 A 90 90 0 0 1 -52.9 72.8 Z" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>
                        <!-- Operations: 40% (144 deg) -->
                        <path d="M 0 0 L -52.9 72.8 A 90 90 0 0 1 0 -90 Z" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>
                        
                        <circle cx="0" cy="0" r="30" fill="var(--planner-bg-surface)"/>
                        <text x="0" y="4" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">₹40 L</text>
                        <text x="0" y="115" fill="#182e26" font-size="14" font-weight="bold" text-anchor="middle">Year 2023 (वर्ष 2023)</text>
                    </g>

                    <!-- Right Circle: 2024 (Total = 60 Lakh) -->
                    <g transform="translate(480, 130)">
                        <!-- Marketing: 30% (108 deg) -->
                        <path d="M 0 0 L 0 -90 A 90 90 0 0 1 85.6 27.8 Z" fill="#0d9488" stroke="#ffffff" stroke-width="2"/>
                        <!-- R&D: 30% (108 deg) -->
                        <path d="M 0 0 L 85.6 27.8 A 90 90 0 0 1 -27.8 85.6 Z" fill="#2563eb" stroke="#ffffff" stroke-width="2"/>
                        <!-- Operations: 40% (144 deg) -->
                        <path d="M 0 0 L -27.8 85.6 A 90 90 0 0 1 0 -90 Z" fill="#f59e0b" stroke="#ffffff" stroke-width="2"/>

                        <circle cx="0" cy="0" r="30" fill="var(--planner-bg-surface)"/>
                        <text x="0" y="4" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">₹60 L</text>
                        <text x="0" y="115" fill="#182e26" font-size="14" font-weight="bold" text-anchor="middle">Year 2024 (वर्ष 2024)</text>
                    </g>

                    <!-- Central Legend below -->
                    <g transform="translate(170, 245)">
                        <rect x="0" y="0" width="14" height="14" rx="2" fill="#0d9488"/>
                        <text x="20" y="12" fill="#182e26" font-size="12">Marketing (मार्केटिंग)</text>

                        <rect x="150" y="0" width="14" height="14" rx="2" fill="#2563eb"/>
                        <text x="170" y="12" fill="#182e26" font-size="12">R&amp;D (अनुसंधान)</text>

                        <rect x="270" y="0" width="14" height="14" rx="2" fill="#f59e0b"/>
                        <text x="290" y="12" fill="#182e26" font-size="12">Operations (परिचालन)</text>
                    </g>
                </svg>
            </div>
        </section>

        <!-- Section 3: Speed Shortcuts for Pie Charts -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-bolt"></i>
                <span class="lang-en">3. Speed Calculation Shortcuts for Single &amp; Mixed Pie Charts</span>
                <span class="lang-hi">3. पाई चार्ट के लिए तीव्र गणना शॉर्टकट</span>
            </h2>
            <ul class="point-list">
                <li>
                    <span class="key-badge">Shortcut 1: Direct Ratio of Sectors</span>
                    <span class="lang-en">To find the ratio between two sectors within the SAME pie chart, you DO NOT need to calculate their rupee values. The ratio of their degrees or percentages IS their ratio!
                    <br>&bull; Example: In Figure 4.1, Ratio of Food (30%) to Transport (10%) = <code>30 : 10 = 3 : 1</code> (or 108&deg; : 36&deg; = 3 : 1). Exact answers in 2 seconds!</span>
                    <span class="lang-hi">एक ही पाई चार्ट के दो त्रिज्यखंडों का अनुपात निकालने के लिए उनके वास्तविक रुपये मान निकालने की आवश्यकता नहीं है। उनके कोणों या प्रतिशत का अनुपात ही अंतिम अनुपात होता है!
                    <br>&bull; भोजन (30%) का परिवहन (10%) से अनुपात = <code>30 : 10 = 3 : 1</code>।</span>
                </li>
                <li>
                    <span class="key-badge">Shortcut 2: Difference of Two Sectors</span>
                    <span class="lang-en">To find the difference in expenditure between Food (30%) and Rent (20%):
                    <br>&bull; Subtract percentages first: 30% - 20% = 10%.
                    <br>&bull; Calculate only once: 10% of ₹80,000 = <strong>₹8,000</strong>. Never calculate Food (₹24,000) and Rent (₹16,000) separately!</span>
                    <span class="lang-hi">भोजन (30%) और किराए (20%) के व्यय का अंतर निकालने के लिए:
                    <br>&bull; पहले प्रतिशत घटाएं: 30% - 20% = 10%।
                    <br>&bull; फिर एक बार में निकालें: 80,000 का 10% = <strong>₹8,000</strong>। दोनों का अलग-अलग मान न निकालें!</span>
                </li>
                <li>
                    <span class="key-badge">Shortcut 3: Sector "What Percent More"</span>
                    <span class="lang-en">"Food expenditure is what percent more than Rent expenditure?"
                    <br>&bull; Calculation: <code>[(30% - 20%) / 20%] &times; 100 = (10 / 20) &times; 100 = 50%</code>. No rupee values needed!</span>
                    <span class="lang-hi">"भोजन पर व्यय, किराए के व्यय से कितना प्रतिशत अधिक है?"
                    <br>&bull; गणना: <code>[(30% - 20%) / 20%] &times; 100 = (10 / 20) &times; 100 = 50%</code>। वास्तविक रुपयों की कोई आवश्यकता नहीं!</span>
                </li>
            </ul>
        </section>

        <!-- Section 4: Combination DI (Pie Chart + Tabular Ratios) & Missing Angles -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-table-cells"></i>
                <span class="lang-en">4. Combination DI: Pie Charts with Accompanying Tables</span>
                <span class="lang-hi">4. मिश्रित डीआई: पाई चार्ट एवं संलग्न तालिकाएं</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>The Two-Stage Solving Protocol:</strong> In combination sets, the Pie Chart distributes the aggregate universe across primary departments/states, while an accompanying Table breaks each sector into internal demographic ratios (e.g., Male : Female, Officer : Clerk, Literate : Illiterate).
                <br>&bull; <em>Formula:</em> <code>Sub-component Value = Grand Total &times; (Sector % / 100) &times; [Sub-category Ratio / Sum of Ratios]</code></span>
                <span class="lang-hi"><strong>दो-चरणीय हल विधि:</strong> मिश्रित सेटों में पाई चार्ट कुल संख्या को विभागों/राज्यों में बांटता है, जबकि तालिका प्रत्येक क्षेत्र को आंतरिक जनसांख्यिकीय अनुपात (उदा. पुरुष : महिला, अधिकारी : लिपिक) में विभाजित करती है।
                <br>&bull; <em>सूत्र:</em> <code>उप-घटक मान = कुल योग &times; (क्षेत्र % / 100) &times; [उप-श्रेणी अनुपात / कुल अनुपाती योग]</code></span>
            </div>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Department (विभाग)</span><span class="lang-hi">विभाग</span></th>
                            <th><span class="lang-en">Pie Share (%)</span><span class="lang-hi">पाई हिस्सेदारी (%)</span></th>
                            <th><span class="lang-en">Male : Female Ratio</span><span class="lang-hi">पुरुष : महिला अनुपात</span></th>
                            <th><span class="lang-en">Fast Computational Formula</span><span class="lang-hi">त्वरित गणना सूत्र</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>IT</strong></td>
                            <td>25% (90&deg;)</td>
                            <td>3 : 2</td>
                            <td>Females = Total &times; 0.25 &times; (2/5) = 10% of Total</td>
                        </tr>
                        <tr>
                            <td><strong>HR</strong></td>
                            <td>15% (54&deg;)</td>
                            <td>1 : 2</td>
                            <td>Females = Total &times; 0.15 &times; (2/3) = 10% of Total</td>
                        </tr>
                        <tr>
                            <td><strong>Finance</strong></td>
                            <td>20% (72&deg;)</td>
                            <td>3 : 1</td>
                            <td>Males = Total &times; 0.20 &times; (3/4) = 15% of Total</td>
                        </tr>
                        <tr>
                            <td><strong>Sales</strong></td>
                            <td>30% (108&deg;)</td>
                            <td>5 : 1</td>
                            <td>Males = Total &times; 0.30 &times; (5/6) = 25% of Total</td>
                        </tr>
                        <tr>
                            <td><strong>Operations</strong></td>
                            <td>10% (36&deg;)</td>
                            <td>1 : 1</td>
                            <td>Females = Total &times; 0.10 &times; (1/2) = 5% of Total</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <ul class="point-list" style="margin-top:1rem;">
                <li>
                    <span class="key-badge">Missing Sector Angle Rule</span>
                    <span class="lang-en">Because the sum of all central angles in any circle is identically 360&deg; (or 100%), an unlabelled sector <code>X</code> is uniquely found by:
                    <br><code>&theta;_X = 360&deg; - (&theta;_1 + &theta;_2 + ... + &theta;_k)</code>.</span>
                    <span class="lang-hi">चूंकि वृत्त के सभी केंद्रीय कोणों का योग ठीक 360&deg; (या 100%) होता है, अतः किसी अज्ञात क्षेत्र <code>X</code> का कोण:
                    <br><code>&theta;_X = 360&deg; - (&theta;_1 + &theta;_2 + ... + &theta;_k)</code>।</span>
                </li>
            </ul>
        </section>
    """,

    # 30 Curated Practice Questions
    "practiceQuestions": [
        {
            "tag": "Degree to Percentage",
            "qEn": "A sector in a pie chart has a central angle of 54&deg;. What percentage of the total does it represent?",
            "qHi": "एक पाई चार्ट में एक त्रिज्यखंड का केंद्रीय कोण 54&deg; है। यह कुल का कितना प्रतिशत प्रदर्शित करता है?",
            "opts": [
                ("A", "15%", "15%"),
                ("B", "18%", "18%"),
                ("C", "12.5%", "12.5%"),
                ("D", "20%", "20%")
            ],
            "ans": "A",
            "solEn": "Percentage = (Angle / 360) &times; 100 = (54 / 360) &times; 100 = 54 / 3.6 = 15%.",
            "solHi": "प्रतिशत = (54 / 360) &times; 100 = 54 / 3.6 = 15%।"
        },
        {
            "tag": "Percentage to Degree",
            "qEn": "If salary expenditure accounts for 35% of an organization's budget, what is its central angle on a pie chart?",
            "qHi": "यदि वेतन व्यय किसी संगठन के बजट का 35% है, तो पाई चार्ट पर इसका केंद्रीय कोण क्या होगा?",
            "opts": [
                ("A", "126&deg;", "126&deg;"),
                ("B", "130&deg;", "130&deg;"),
                ("C", "135&deg;", "135&deg;"),
                ("D", "120&deg;", "120&deg;")
            ],
            "ans": "A",
            "solEn": "Angle = Percent &times; 3.6&deg; = 35 &times; 3.6 = 126&deg;.",
            "solHi": "केंद्रीय कोण = 35 &times; 3.6&deg; = 126&deg;।"
        },
        {
            "tag": "Single Pie - Value",
            "qEn": "Based on Figure 4.1 (Total = ₹80,000), how much money is spent monthly on Education and Savings combined?",
            "qHi": "चित्र 4.1 के आधार पर (कुल = ₹80,000), शिक्षा और बचत पर मिलाकर प्रतिमाह कितनी राशि खर्च होती है?",
            "opts": [
                ("A", "₹20,000", "₹20,000"),
                ("B", "₹24,000", "₹24,000"),
                ("C", "₹28,000", "₹28,000"),
                ("D", "₹16,000", "₹16,000")
            ],
            "ans": "B",
            "solEn": "Education = 15%; Savings = 15%. Combined = 30%. Value = 30% of ₹80,000 = ₹24,000.",
            "solHi": "शिक्षा = 15%; बचत = 15%। कुल = 30%। 80,000 का 30% = ₹24,000।"
        },
        {
            "tag": "Single Pie - Ratio",
            "qEn": "In Figure 4.1, what is the ratio of expenditure on Food to expenditure on Rent?",
            "qHi": "चित्र 4.1 में, भोजन पर व्यय का किराए पर व्यय से क्या अनुपात है?",
            "opts": [
                ("A", "3 : 2", "3 : 2"),
                ("B", "2 : 3", "2 : 3"),
                ("C", "5 : 4", "5 : 4"),
                ("D", "4 : 3", "4 : 3")
            ],
            "ans": "A",
            "solEn": "Direct ratio from percentages: Food (30%) : Rent (20%) = 30 : 20 = 3 : 2.",
            "solHi": "प्रतिशत से सीधा अनुपात: 30 : 20 = 3 : 2।"
        },
        {
            "tag": "Single Pie - Difference",
            "qEn": "In Figure 4.1, by how much does monthly expenditure on Food exceed monthly expenditure on Transport?",
            "qHi": "चित्र 4.1 में, भोजन पर मासिक व्यय परिवहन पर मासिक व्यय से कितना अधिक है?",
            "opts": [
                ("A", "₹12,000", "₹12,000"),
                ("B", "₹14,000", "₹14,000"),
                ("C", "₹16,000", "₹16,000"),
                ("D", "₹18,000", "₹18,000")
            ],
            "ans": "C",
            "solEn": "Food % = 30%; Transport % = 10%. Difference = 20%. 20% of ₹80,000 = ₹16,000.",
            "solHi": "प्रतिशत अंतर = 30% - 10% = 20%। 80,000 का 20% = ₹16,000।"
        },
        {
            "tag": "Dual Pie - Value",
            "qEn": "In Figure 4.2, what was the absolute expenditure on Marketing in 2024?",
            "qHi": "चित्र 4.2 में, वर्ष 2024 में मार्केटिंग पर वास्तविक व्यय कितना था?",
            "opts": [
                ("A", "₹15 Lakh", "₹15 लाख"),
                ("B", "₹18 Lakh", "₹18 लाख"),
                ("C", "₹20 Lakh", "₹20 लाख"),
                ("D", "₹12 Lakh", "₹12 लाख")
            ],
            "ans": "B",
            "solEn": "2024 Marketing share = 30%. Total budget in 2024 = ₹60 Lakh. Value = 30% of 60 Lakh = ₹18 Lakh.",
            "solHi": "2024 में मार्केटिंग = 30%। कुल बजट = ₹60 लाख। 60 लाख का 30% = ₹18 लाख।"
        },
        {
            "tag": "Dual Pie - Growth",
            "qEn": "In Figure 4.2, what was the percentage increase in Marketing budget from 2023 to 2024?",
            "qHi": "चित्र 4.2 में, 2023 से 2024 तक मार्केटिंग बजट में कितने प्रतिशत की वृद्धि हुई?",
            "opts": [
                ("A", "5%", "5%"),
                ("B", "50%", "50%"),
                ("C", "80%", "80%"),
                ("D", "60%", "60%")
            ],
            "ans": "C",
            "solEn": "2023 Marketing = 25% of ₹40 L = ₹10 Lakh. 2024 Marketing = 30% of ₹60 L = ₹18 Lakh. Increase = 18 - 10 = ₹8 Lakh. Percentage increase = (8 / 10) &times; 100 = 80%.",
            "solHi": "2023 मार्केटिंग = 40 लाख का 25% = ₹10 लाख। 2024 मार्केटिंग = 60 लाख का 30% = ₹18 लाख। वृद्धि = 18 - 10 = ₹8 लाख। प्रतिशत वृद्धि = (8 / 10) &times; 100 = 80%।"
        },
        {
            "tag": "Dual Pie - Comparison",
            "qEn": "In Figure 4.2, how much was allocated to Operations in 2024 compared to 2023?",
            "qHi": "चित्र 4.2 में, 2023 की तुलना में 2024 में परिचालन (Operations) हेतु कितनी राशि आवंटित की गई?",
            "opts": [
                ("A", "₹16 L in 2023 and ₹24 L in 2024 (+₹8 L)", "2023 में ₹16 लाख और 2024 में ₹24 लाख (+₹8 लाख)"),
                ("B", "Both years had equal rupees because both were 40%", "दोनों वर्षों में बराबर रुपये थे क्योंकि दोनों 40% थे"),
                ("C", "₹20 L in 2023 and ₹25 L in 2024", "2023 में ₹20 लाख और 2024 में ₹25 लाख"),
                ("D", "₹12 L in 2023 and ₹18 L in 2024", "2023 में ₹12 लाख और 2024 में ₹18 लाख")
            ],
            "ans": "A",
            "solEn": "Operations 2023 = 40% of 40 L = ₹16 Lakh. Operations 2024 = 40% of 60 L = ₹24 Lakh. Difference = +₹8 Lakh.",
            "solHi": "2023 परिचालन = 40 लाख का 40% = ₹16 लाख। 2024 परिचालन = 60 लाख का 40% = ₹24 लाख। अंतर = +₹8 लाख।"
        },
        {
            "tag": "Central Angle Calculation",
            "qEn": "In a village of 1,800 residents, 450 work in agriculture. What central angle represents agriculture on a pie chart?",
            "qHi": "1,800 निवासियों वाले एक गांव में 450 लोग कृषि कार्य करते हैं। पाई चार्ट पर कृषि को कौन सा केंद्रीय कोण प्रदर्शित करेगा?",
            "opts": [
                ("A", "75&deg;", "75&deg;"),
                ("B", "90&deg;", "90&deg;"),
                ("C", "100&deg;", "100&deg;"),
                ("D", "120&deg;", "120&deg;")
            ],
            "ans": "B",
            "solEn": "Fraction = 450 / 1,800 = 1/4. Angle = (1/4) &times; 360&deg; = 90&deg;.",
            "solHi": "भिन्न = 450 / 1,800 = 1/4। केंद्रीय कोण = 1/4 &times; 360&deg; = 90&deg;।"
        },
        {
            "tag": "Mixed Pie - Ratio",
            "qEn": "In Figure 4.1, if savings (15%) is further divided into Mutual Funds and Bank FD in ratio 2 : 1, how much money goes into Mutual Funds?",
            "qHi": "चित्र 4.1 में, यदि बचत (15%) को आगे म्यूचुअल फंड और बैंक एफडी में 2 : 1 के अनुपात में विभाजित किया जाए, तो म्यूचुअल फंड में कितनी राशि जाती है?",
            "opts": [
                ("A", "₹6,000", "₹6,000"),
                ("B", "₹8,000", "₹8,000"),
                ("C", "₹4,000", "₹4,000"),
                ("D", "₹10,000", "₹10,000")
            ],
            "ans": "B",
            "solEn": "Total savings = 15% of ₹80,000 = ₹12,000. Mutual Funds share = (2/3) &times; 12,000 = ₹8,000.",
            "solHi": "कुल बचत = 80,000 का 15% = ₹12,000। म्यूचुअल फंड = (2/3) &times; 12,000 = ₹8,000।"
        },
        {
            "tag": "Central Angle",
            "qEn": "A pie chart sector of 72&deg; represents how much percentage?",
            "qHi": "72&deg; का केंद्रीय कोण कितने प्रतिशत को दर्शाता है?",
            "opts": [
                ("A", "15%", "15%"),
                ("B", "20%", "20%"),
                ("C", "25%", "25%"),
                ("D", "18%", "18%")
            ],
            "ans": "B",
            "solEn": "Percentage = 72 / 3.6 = 20% (or 72/360 = 1/5 = 20%).",
            "solHi": "प्रतिशत = 72 / 3.6 = 20%।"
        },
        {
            "tag": "Degree to Quantity",
            "qEn": "In a pie chart with total sales = ₹7,20,000, what is the value corresponding to an angle of 40&deg;?",
            "qHi": "₹7,20,000 की कुल बिक्री वाले पाई चार्ट में 40&deg; कोण का मान क्या होगा?",
            "opts": [
                ("A", "₹80,000", "₹80,000"),
                ("B", "₹72,000", "₹72,000"),
                ("C", "₹90,000", "₹90,000"),
                ("D", "₹85,000", "₹85,000")
            ],
            "ans": "A",
            "solEn": "Value = (40 / 360) &times; 720,000 = (1/9) &times; 720,000 = ₹80,000.",
            "solHi": "मान = (40 / 360) &times; 7,20,000 = (1/9) &times; 7,20,000 = ₹80,000।"
        },
        {
            "tag": "Dual Pie - Ratio",
            "qEn": "In Figure 4.2, what is the ratio of R&D expenditure in 2023 to R&D expenditure in 2024?",
            "qHi": "चित्र 4.2 में, 2023 में R&D व्यय का 2024 में R&D व्यय से क्या अनुपात है?",
            "opts": [
                ("A", "7 : 9", "7 : 9"),
                ("B", "14 : 18", "14 : 18"),
                ("C", "7 : 9", "7 : 9"),
                ("D", "5 : 6", "5 : 6")
            ],
            "ans": "A",
            "solEn": "2023 R&D = 35% of ₹40 L = ₹14 Lakh. 2024 R&D = 30% of ₹60 L = ₹18 Lakh. Ratio = 14 / 18 = 7 : 9.",
            "solHi": "2023 R&D = 40 लाख का 35% = ₹14 लाख। 2024 R&D = 60 लाख का 30% = ₹18 लाख। अनुपात = 14 : 18 = 7 : 9।"
        },
        {
            "tag": "Sector Difference",
            "qEn": "In a pie chart, Sector X is 120&deg; and Sector Y is 48&deg;. Total value is ₹54,000. What is the difference between Sector X and Y?",
            "qHi": "एक पाई चार्ट में, त्रिज्यखंड X 120&deg; है और Y 48&deg; है। कुल मान ₹54,000 है। X और Y के बीच का अंतर क्या है?",
            "opts": [
                ("A", "₹10,800", "₹10,800"),
                ("B", "₹12,000", "₹12,000"),
                ("C", "₹9,600", "₹9,600"),
                ("D", "₹11,400", "₹11,400")
            ],
            "ans": "A",
            "solEn": "Difference in angle = 120&deg; - 48&deg; = 72&deg;. Value = (72 / 360) &times; 54,000 = (1/5) &times; 54,000 = ₹10,800.",
            "solHi": "कोणों का अंतर = 120&deg; - 48&deg; = 72&deg;। अंतर = (72 / 360) &times; 54,000 = 1/5 &times; 54,000 = ₹10,800।"
        },
        {
            "tag": "Angle Representation",
            "qEn": "What central angle represents the fraction 3/8 on a pie chart?",
            "qHi": "पाई चार्ट पर भिन्न 3/8 को कौन सा केंद्रीय कोण दर्शाता है?",
            "opts": [
                ("A", "135&deg;", "135&deg;"),
                ("B", "125&deg;", "125&deg;"),
                ("C", "140&deg;", "140&deg;"),
                ("D", "150&deg;", "150&deg;")
            ],
            "ans": "A",
            "solEn": "Angle = (3/8) &times; 360&deg; = 3 &times; 45&deg; = 135&deg;.",
            "solHi": "कोण = (3/8) &times; 360&deg; = 135&deg;।"
        },
        {
            "tag": "Single Pie - Percentage More",
            "qEn": "In Figure 4.1, expenditure on Food (30%) is what percent more than expenditure on Rent (20%)?",
            "qHi": "चित्र 4.1 में, भोजन पर व्यय (30%) किराए पर व्यय (20%) से कितने प्रतिशत अधिक है?",
            "opts": [
                ("A", "50%", "50%"),
                ("B", "10%", "10%"),
                ("C", "33.33%", "33.33%"),
                ("D", "25%", "25%")
            ],
            "ans": "A",
            "solEn": "Percentage more = [(30 - 20) / 20] &times; 100 = (10 / 20) &times; 100 = 50%.",
            "solHi": "प्रतिशत अधिक = [(30 - 20) / 20] &times; 100 = 50%।"
        },
        {
            "tag": "Pie Chart Property",
            "qEn": "Can a pie chart display negative values or continuous time trends directly?",
            "qHi": "क्या एक पाई चार्ट ऋणात्मक मानों (negative values) या सतत समय प्रवृत्तियों को सीधे प्रदर्शित कर सकता है?",
            "opts": [
                ("A", "No, pie charts require non-negative component shares adding up to a positive whole", "नहीं, पाई चार्ट के लिए गैर-ऋणात्मक घटक आवश्यक हैं जो मिलकर धनात्मक योग बनाते हैं"),
                ("B", "Yes, by using dashed angles", "हाँ, डैश्ड कोणों का उपयोग करके"),
                ("C", "Yes, for temperatures only", "हाँ, केवल तापमान के लिए"),
                ("D", "Only in 3D pie charts", "केवल 3D पाई चार्ट में")
            ],
            "ans": "A",
            "solEn": "A pie chart requires all slices to be non-negative proportions of an aggregate whole (100% or 360&deg;). It cannot represent negative numbers.",
            "solHi": "पाई चार्ट संपूर्ण योग के गैर-ऋणात्मक आनुपातिक भागों को दर्शाता है; यह ऋणात्मक मान प्रदर्शित नहीं कर सकता।"
        },
        {
            "tag": "Central Angle",
            "qEn": "If a candidate in an election secured 40% of votes, what is the central angle for his share?",
            "qHi": "यदि एक चुनाव में किसी प्रत्याशी ने 40% मत प्राप्त किए, तो उसके हिस्से का केंद्रीय कोण क्या है?",
            "opts": [
                ("A", "144&deg;", "144&deg;"),
                ("B", "140&deg;", "140&deg;"),
                ("C", "150&deg;", "150&deg;"),
                ("D", "136&deg;", "136&deg;")
            ],
            "ans": "A",
            "solEn": "Angle = 40 &times; 3.6&deg; = 144&deg;.",
            "solHi": "कोण = 40 &times; 3.6&deg; = 144&deg;।"
        },
        {
            "tag": "Dual Pie Total Ratio",
            "qEn": "In Figure 4.2, what is the ratio of total budget in 2023 to total budget in 2024?",
            "qHi": "चित्र 4.2 में, वर्ष 2023 के कुल बजट का वर्ष 2024 के कुल बजट से क्या अनुपात है?",
            "opts": [
                ("A", "2 : 3", "2 : 3"),
                ("B", "3 : 2", "3 : 2"),
                ("C", "4 : 5", "4 : 5"),
                ("D", "1 : 2", "1 : 2")
            ],
            "ans": "A",
            "solEn": "Total 2023 = ₹40 Lakh; Total 2024 = ₹60 Lakh. Ratio = 40 / 60 = 2 : 3.",
            "solHi": "2023 का कुल = 40 लाख; 2024 का कुल = 60 लाख। अनुपात = 40 : 60 = 2 : 3।"
        },
        {
            "tag": "Three Sector Sum",
            "qEn": "In Figure 4.1, what percentage of total expenditure is spent on Food, Rent, and Education combined?",
            "qHi": "चित्र 4.1 में, भोजन, किराया और शिक्षा को मिलाकर कुल व्यय का कितना प्रतिशत खर्च होता है?",
            "opts": [
                ("A", "65%", "65%"),
                ("B", "60%", "60%"),
                ("C", "70%", "70%"),
                ("D", "55%", "55%")
            ],
            "ans": "A",
            "solEn": "Food (30%) + Rent (20%) + Education (15%) = 65%.",
            "solHi": "30% + 20% + 15% = 65%।"
        },
        {
            "tag": "Mixed Pie + Table",
            "qEn": "In Figure 4.1, if 25% of the Food expenditure is spent on dairy products, what is the monthly expenditure on dairy?",
            "qHi": "चित्र 4.1 में, यदि भोजन व्यय का 25% डेयरी उत्पादों पर खर्च होता है, तो डेयरी पर मासिक व्यय कितना है?",
            "opts": [
                ("A", "₹6,000", "₹6,000"),
                ("B", "₹5,000", "₹5,000"),
                ("C", "₹4,800", "₹4,800"),
                ("D", "₹7,200", "₹7,200")
            ],
            "ans": "A",
            "solEn": "Food expenditure = 30% of ₹80,000 = ₹24,000. Dairy = 25% of 24,000 = (1/4) &times; 24,000 = ₹6,000.",
            "solHi": "भोजन व्यय = 80,000 का 30% = ₹24,000। डेयरी = 24,000 का 25% = ₹6,000।"
        },
        {
            "tag": "Central Angle",
            "qEn": "What percentage does an angle of 108&deg; represent in a pie chart?",
            "qHi": "एक पाई चार्ट में 108&deg; का कोण कितने प्रतिशत को दर्शाता है?",
            "opts": [
                ("A", "30%", "30%"),
                ("B", "28%", "28%"),
                ("C", "32%", "32%"),
                ("D", "35%", "35%")
            ],
            "ans": "A",
            "solEn": "Percentage = 108 / 3.6 = 30%.",
            "solHi": "प्रतिशत = 108 / 3.6 = 30%।"
        },
        {
            "tag": "Remaining Angle",
            "qEn": "In a 4-sector pie chart, three sectors are 90&deg;, 120&deg;, and 80&deg;. What is the angle of the fourth sector?",
            "qHi": "4 त्रिज्यखंडों वाले पाई चार्ट में, तीन कोण 90&deg;, 120&deg; और 80&deg; हैं। चौथे त्रिज्यखंड का कोण क्या है?",
            "opts": [
                ("A", "70&deg;", "70&deg;"),
                ("B", "80&deg;", "80&deg;"),
                ("C", "60&deg;", "60&deg;"),
                ("D", "75&deg;", "75&deg;")
            ],
            "ans": "A",
            "solEn": "Sum of all sectors = 360&deg;. Fourth sector = 360 - (90 + 120 + 80) = 360 - 290 = 70&deg;.",
            "solHi": "चौथा कोण = 360&deg; - (90 + 120 + 80) = 360 - 290 = 70&deg;।"
        },
        {
            "tag": "Dual Pie Sector Shift",
            "qEn": "In Figure 4.2, R&D budget was 35% in 2023 and 30% in 2024. Did the absolute rupee budget for R&D increase or decrease?",
            "qHi": "चित्र 4.2 में, R&D बजट 2023 में 35% और 2024 में 30% था। क्या R&D का वास्तविक रुपया बजट बढ़ा या घटा?",
            "opts": [
                ("A", "Increased by ₹4 Lakh (from ₹14 L to ₹18 L)", "₹4 लाख बढ़ा (₹14 लाख से ₹18 लाख)"),
                ("B", "Decreased by 5%", "5% घटा"),
                ("C", "Remained constant", "स्थिर रहा"),
                ("D", "Decreased by ₹2 Lakh", "₹2 लाख घटा")
            ],
            "ans": "A",
            "solEn": "2023 R&D = 35% of ₹40 L = ₹14 Lakh. 2024 R&D = 30% of ₹60 L = ₹18 Lakh. It increased by ₹4 Lakh despite the lower percentage share!",
            "solHi": "2023 R&D = ₹14 लाख; 2024 R&D = ₹18 लाख। प्रतिशत हिस्सा घटने के बावजूद वास्तविक बजट ₹4 लाख बढ़ा!"
        },
        {
            "tag": "Ratio to Angle",
            "qEn": "A pie chart divides a budget into three items in the ratio 1 : 2 : 3. What is the central angle of the largest item?",
            "qHi": "एक पाई चार्ट बजट को 1 : 2 : 3 के अनुपात में तीन मदों में विभाजित करता है। सबसे बड़ी मद का केंद्रीय कोण क्या है?",
            "opts": [
                ("A", "180&deg;", "180&deg;"),
                ("B", "150&deg;", "150&deg;"),
                ("C", "120&deg;", "120&deg;"),
                ("D", "160&deg;", "160&deg;")
            ],
            "ans": "A",
            "solEn": "Total parts = 1 + 2 + 3 = 6. Largest item = (3/6) &times; 360&deg; = 180&deg;.",
            "solHi": "कुल भाग = 6। सबसे बड़ा भाग = (3/6) &times; 360&deg; = 180&deg;।"
        },
        {
            "tag": "Percentage Calculation",
            "qEn": "What is the angle of a slice representing 12.5%?",
            "qHi": "12.5% को प्रदर्शित करने वाले त्रिज्यखंड का कोण क्या है?",
            "opts": [
                ("A", "45&deg;", "45&deg;"),
                ("B", "40&deg;", "40&deg;"),
                ("C", "50&deg;", "50&deg;"),
                ("D", "36&deg;", "36&deg;")
            ],
            "ans": "A",
            "solEn": "12.5% = 1/8. Angle = 360&deg; / 8 = 45&deg;.",
            "solHi": "12.5% = 1/8। कोण = 360&deg; / 8 = 45&deg;।"
        },
        {
            "tag": "Central Angle",
            "qEn": "A pie chart slice has an angle of 18&deg;. What percentage does it represent?",
            "qHi": "एक पाई चार्ट के 18&deg; कोण का त्रिज्यखंड कितने प्रतिशत को दर्शाता है?",
            "opts": [
                ("A", "5%", "5%"),
                ("B", "6%", "6%"),
                ("C", "4%", "4%"),
                ("D", "2.5%", "2.5%")
            ],
            "ans": "A",
            "solEn": "Percentage = 18 / 3.6 = 5%.",
            "solHi": "प्रतिशत = 18 / 3.6 = 5%।"
        },
        {
            "tag": "Combined Slices",
            "qEn": "In Figure 4.1, if Rent (20%) and Transport (10%) are combined, what is their combined central angle?",
            "qHi": "चित्र 4.1 में, यदि किराया (20%) और परिवहन (10%) को मिला दिया जाए, तो उनका संयुक्त केंद्रीय कोण क्या होगा?",
            "opts": [
                ("A", "108&deg;", "108&deg;"),
                ("B", "100&deg;", "100&deg;"),
                ("C", "90&deg;", "90&deg;"),
                ("D", "120&deg;", "120&deg;")
            ],
            "ans": "A",
            "solEn": "Combined % = 20% + 10% = 30%. Angle = 30 &times; 3.6&deg; = 108&deg;.",
            "solHi": "संयुक्त % = 30%। कोण = 30 &times; 3.6&deg; = 108&deg;।"
        },
        {
            "tag": "Dual Pie Share",
            "qEn": "In Figure 4.2, what was the total expenditure on Operations across both years combined?",
            "qHi": "चित्र 4.2 में, दोनों वर्षों को मिलाकर परिचालन (Operations) पर कुल कितना व्यय हुआ?",
            "opts": [
                ("A", "₹40 Lakh", "₹40 लाख"),
                ("B", "₹38 Lakh", "₹38 लाख"),
                ("C", "₹42 Lakh", "₹42 लाख"),
                ("D", "₹36 Lakh", "₹36 लाख")
            ],
            "ans": "A",
            "solEn": "2023 Operations = ₹16 Lakh; 2024 Operations = ₹24 Lakh. Total = 16 + 24 = ₹40 Lakh.",
            "solHi": "2023 परिचालन = ₹16 लाख; 2024 परिचालन = ₹24 लाख। कुल = ₹40 लाख।"
        },
        {
            "tag": "Central Angle",
            "qEn": "What central angle represents 60% of a circle?",
            "qHi": "एक वृत्त का 60% भाग किस केंद्रीय कोण द्वारा दर्शाया जाता है?",
            "opts": [
                ("A", "216&deg;", "216&deg;"),
                ("B", "200&deg;", "200&deg;"),
                ("C", "220&deg;", "220&deg;"),
                ("D", "180&deg;", "180&deg;")
            ],
            "ans": "A",
            "solEn": "Angle = 60 &times; 3.6&deg; = 216&deg;.",
            "solHi": "कोण = 60 &times; 3.6&deg; = 216&deg;।"
        }
    ],

    # 15 Mini-Test MCQs
    "testQuestions": [
        {
            "qEn": "What central angle represents 10% on a pie chart?",
            "qHi": "पाई चार्ट में 10% भाग किस केंद्रीय कोण द्वारा दर्शाया जाता है?",
            "opts": [
                ("A", "36&deg;", "36&deg;"),
                ("B", "30&deg;", "30&deg;"),
                ("C", "40&deg;", "40&deg;"),
                ("D", "45&deg;", "45&deg;")
            ]
        },
        {
            "qEn": "A central angle of 90&deg; corresponds to what percentage of the total?",
            "qHi": "90&deg; का केंद्रीय कोण कुल का कितना प्रतिशत होता है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "20%", "20%"),
                ("C", "30%", "30%"),
                ("D", "33.33%", "33.33%")
            ]
        },
        {
            "qEn": "In Figure 4.1 (Total = ₹80,000), how much is spent on Rent (20%)?",
            "qHi": "चित्र 4.1 में (कुल = ₹80,000), किराए (20%) पर कितनी राशि खर्च होती है?",
            "opts": [
                ("A", "₹16,000", "₹16,000"),
                ("B", "₹15,000", "₹15,000"),
                ("C", "₹18,000", "₹18,000"),
                ("D", "₹12,000", "₹12,000")
            ]
        },
        {
            "qEn": "In Figure 4.1, what is the ratio of Food (30%) to Education (15%)?",
            "qHi": "चित्र 4.1 में, भोजन (30%) का शिक्षा (15%) से क्या अनुपात है?",
            "opts": [
                ("A", "2 : 1", "2 : 1"),
                ("B", "3 : 1", "3 : 1"),
                ("C", "1 : 2", "1 : 2"),
                ("D", "4 : 3", "4 : 3")
            ]
        },
        {
            "qEn": "In Figure 4.2, what was the R&D budget in 2023 (Total = ₹40 L, R&D = 35%)?",
            "qHi": "चित्र 4.2 में, 2023 में R&D बजट कितना था (कुल = ₹40 लाख, R&D = 35%)?",
            "opts": [
                ("A", "₹14 Lakh", "₹14 लाख"),
                ("B", "₹12 Lakh", "₹12 लाख"),
                ("C", "₹15 Lakh", "₹15 लाख"),
                ("D", "₹16 Lakh", "₹16 लाख")
            ]
        },
        {
            "qEn": "What is the central angle for a sector representing 1/6th of a pie chart?",
            "qHi": "पाई चार्ट के 1/6 भाग को प्रदर्शित करने वाले त्रिज्यखंड का केंद्रीय कोण क्या होगा?",
            "opts": [
                ("A", "60&deg;", "60&deg;"),
                ("B", "50&deg;", "50&deg;"),
                ("C", "45&deg;", "45&deg;"),
                ("D", "72&deg;", "72&deg;")
            ]
        },
        {
            "qEn": "In Figure 4.1, what is the central angle corresponding to Food (30%)?",
            "qHi": "चित्र 4.1 में, भोजन (30%) का केंद्रीय कोण कितना है?",
            "opts": [
                ("A", "108&deg;", "108&deg;"),
                ("B", "100&deg;", "100&deg;"),
                ("C", "112&deg;", "112&deg;"),
                ("D", "90&deg;", "90&deg;")
            ]
        },
        {
            "qEn": "If a pie chart has 5 sectors with angles 70&deg;, 80&deg;, 90&deg;, 50&deg;, what is the angle of the fifth sector?",
            "qHi": "यदि एक पाई चार्ट के 5 त्रिज्यखंडों में से 4 कोण 70&deg;, 80&deg;, 90&deg;, 50&deg; हैं, तो 5वें त्रिज्यखंड का कोण क्या है?",
            "opts": [
                ("A", "70&deg;", "70&deg;"),
                ("B", "80&deg;", "80&deg;"),
                ("C", "60&deg;", "60&deg;"),
                ("D", "75&deg;", "75&deg;")
            ]
        },
        {
            "qEn": "In Figure 4.2, what was the Marketing budget in 2023 (25% of ₹40 L)?",
            "qHi": "चित्र 4.2 में, 2023 में मार्केटिंग बजट कितना था (₹40 लाख का 25%)?",
            "opts": [
                ("A", "₹10 Lakh", "₹10 लाख"),
                ("B", "₹8 Lakh", "₹8 लाख"),
                ("C", "₹12 Lakh", "₹12 लाख"),
                ("D", "₹9 Lakh", "₹9 लाख")
            ]
        },
        {
            "qEn": "What angle represents 50% in a pie chart?",
            "qHi": "पाई चार्ट में 50% को कौन सा कोण प्रदर्शित करता है?",
            "opts": [
                ("A", "180&deg;", "180&deg;"),
                ("B", "90&deg;", "90&deg;"),
                ("C", "120&deg;", "120&deg;"),
                ("D", "270&deg;", "270&deg;")
            ]
        },
        {
            "qEn": "In Figure 4.1, if Transport is 10%, how much is spent on Transport monthly?",
            "qHi": "चित्र 4.1 में, यदि परिवहन 10% है, तो परिवहन पर मासिक व्यय कितना है?",
            "opts": [
                ("A", "₹8,000", "₹8,000"),
                ("B", "₹6,000", "₹6,000"),
                ("C", "₹7,500", "₹7,500"),
                ("D", "₹10,000", "₹10,000")
            ]
        },
        {
            "qEn": "If an angle is 144&deg;, what percentage does it represent?",
            "qHi": "यदि कोण 144&deg; है, तो यह कितने प्रतिशत को दर्शाता है?",
            "opts": [
                ("A", "40%", "40%"),
                ("B", "36%", "36%"),
                ("C", "45%", "45%"),
                ("D", "42%", "42%")
            ]
        },
        {
            "qEn": "In Figure 4.2, what was the Operations budget in 2024 (40% of ₹60 L)?",
            "qHi": "चित्र 4.2 में, 2024 में परिचालन बजट कितना था (₹60 लाख का 40%)?",
            "opts": [
                ("A", "₹24 Lakh", "₹24 लाख"),
                ("B", "₹20 Lakh", "₹20 लाख"),
                ("C", "₹22 Lakh", "₹22 लाख"),
                ("D", "₹25 Lakh", "₹25 लाख")
            ]
        },
        {
            "qEn": "Which formula correctly converts an angle &theta; into percentage?",
            "qHi": "कोण &theta; को प्रतिशत में बदलने का सही सूत्र कौन सा है?",
            "opts": [
                ("A", "(&theta; / 360) &times; 100", "(&theta; / 360) &times; 100"),
                ("B", "(&theta; / 100) &times; 360", "(&theta; / 100) &times; 360"),
                ("C", "&theta; &times; 3.6", "&theta; &times; 3.6"),
                ("D", "&theta; / 180", "&theta; / 180")
            ]
        },
        {
            "qEn": "In Figure 4.1, how much more is spent on Rent (₹16,000) than on Education (₹12,000)?",
            "qHi": "चित्र 4.1 में, किराए (₹16,000) पर शिक्षा (₹12,000) से कितनी अधिक राशि खर्च होती है?",
            "opts": [
                ("A", "₹4,000", "₹4,000"),
                ("B", "₹3,000", "₹3,000"),
                ("C", "₹5,000", "₹5,000"),
                ("D", "₹2,000", "₹2,000")
            ]
        }
    ],

    "testDataJson": json.dumps([
        {"ans": "A", "solEn": "10% of 360&deg; = 36&deg;.", "solHi": "360&deg; का 10% = 36&deg;।"},
        {"ans": "A", "solEn": "(90 / 360) &times; 100 = 25%.", "solHi": "(90 / 360) &times; 100 = 25%।"},
        {"ans": "A", "solEn": "20% of ₹80,000 = ₹16,000.", "solHi": "80,000 का 20% = ₹16,000।"},
        {"ans": "A", "solEn": "30% : 15% = 2 : 1.", "solHi": "30 : 15 = 2 : 1।"},
        {"ans": "A", "solEn": "35% of 40 L = 0.35 &times; 40 = ₹14 Lakh.", "solHi": "40 लाख का 35% = ₹14 लाख।"},
        {"ans": "A", "solEn": "360&deg; / 6 = 60&deg;.", "solHi": "360&deg; / 6 = 60&deg;।"},
        {"ans": "A", "solEn": "30 &times; 3.6&deg; = 108&deg;.", "solHi": "30 &times; 3.6&deg; = 108&deg;।"},
        {"ans": "A", "solEn": "360 - (70 + 80 + 90 + 50) = 360 - 290 = 70&deg;.", "solHi": "360 - 290 = 70&deg;।"},
        {"ans": "A", "solEn": "25% of 40 L = ₹10 Lakh.", "solHi": "40 लाख का 25% = ₹10 लाख।"},
        {"ans": "A", "solEn": "Half circle = 180&deg;.", "solHi": "आधा वृत्त = 180&deg;।"},
        {"ans": "A", "solEn": "10% of 80,000 = ₹8,000.", "solHi": "80,000 का 10% = ₹8,000।"},
        {"ans": "A", "solEn": "144 / 3.6 = 40%.", "solHi": "144 / 3.6 = 40%।"},
        {"ans": "A", "solEn": "40% of 60 L = ₹24 Lakh.", "solHi": "60 लाख का 40% = ₹24 लाख।"},
        {"ans": "A", "solEn": "Percentage = (Angle / 360) &times; 100.", "solHi": "प्रतिशत = (कोण / 360) &times; 100।"},
        {"ans": "A", "solEn": "16,000 - 12,000 = ₹4,000.", "solHi": "16,000 - 12,000 = ₹4,000।"}
    ])
}
