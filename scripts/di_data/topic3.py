"""
topic3.py
Topic 3: Line Graphs & Bar Graphs Interpretation: Trends & Comparisons
Slug: line-graphs-and-bar-graphs-interpretation
"""

import json

TOPIC_3 = {
    "slug": "line-graphs-and-bar-graphs-interpretation",
    "titleEn": "Line Graphs & Bar Graphs Interpretation",
    "titleHi": "रेखा आरेख एवं बार ग्राफ व्याख्या व विश्लेषण",
    "pageTitle": "Line Graphs & Bar Graphs Interpretation: Practice & Notes | UPSSSC Mains | SJMaths",
    "metaDesc": "Comprehensive revision notes, 30 practice MCQs with worked solutions, and a 15-Q test on Line Graphs & Bar Graphs (Simple, Grouped, Stacked, Trend Analysis, and Profit-Loss) for UPSSSC Intermediate Level Mains 2026.",
    "metaTagEn": "Part-1 (9): Data Interpretation & Statistical Analysis | Bar Graphs & Line Charts",
    "metaTagHi": "भाग-1 (9): डाटा इंटरप्रिटेशन एवं सांख्यिकीय विश्लेषण | दंड आरेख व रेखा ग्राफ",
    "subtitleEn": "Master Simple, Grouped, and Subdivided Bar Charts alongside single and multiple trend line graphs. Detailed models for Profit-Loss, Trade Balance (Exports-Imports), and Production-Sales for UPSSSC Mains.",
    "subtitleHi": "सरल, बहु-दंड व उप-विभाजित बार ग्राफ तथा एकल व बहु-रेखा आरेखों की संपूर्ण व्याख्या। व्यापार संतुलन (आयात-निर्यात), लाभ-हानि व उत्पादन-बिक्री के मॉडल यूपीएसएसएससी मुख्य परीक्षा हेतु।",
    "crumbNameEn": "Line & Bar Graphs",
    "crumbNameHi": "रेखा व बार ग्राफ",

    "notesHtml": """
        <!-- Section 1: Bar Graph Varieties & Analysis Rules -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-chart-bar"></i>
                <span class="lang-en">1. Typology of Bar Charts &amp; Comparative Rules</span>
                <span class="lang-hi">1. दंड आरेखों (Bar Charts) के प्रकार एवं तुलनात्मक नियम</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Direct Visual Rule:</strong> In bar charts, categories are discrete. The <em>width</em> of all bars is identical and arbitrary; only the <em>height (or length)</em> of each bar is mathematically proportional to the measured variable. Always check whether bars are grouped side-by-side or stacked on top of one another!</span>
                <span class="lang-hi"><strong>प्रत्यक्ष आरेखीय नियम:</strong> दंड आरेख में श्रेणियां असतत (discrete) होती हैं। सभी दंडों की <em>चौड़ाई</em> एकसमान और स्वेच्छ होती है; केवल उनकी <em>ऊंचाई (या लंबाई)</em> ही चर के मान के समानुपाती होती है। हमेशा देखें कि दंड पास-पास रखे हैं (Grouped) या एक के ऊपर एक जुड़े हैं (Stacked)!</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Simple Bar Chart</span>
                    <span class="lang-en">Represents a single independent variable across categories or years (e.g., Annual turnover of one company from 2020 to 2024).</span>
                    <span class="lang-hi">वर्षों या श्रेणियों में केवल एक चर को प्रदर्शित करता है (उदा. 2020 से 2024 तक किसी एक कंपनी का वार्षिक टर्नओवर)।</span>
                </li>
                <li>
                    <span class="key-badge">Grouped (Multiple) Bar Chart</span>
                    <span class="lang-en">Displays two or three related variables adjacent to each other for every category (e.g., Production vs Sales of Cars and Bikes). Useful for direct side-by-side comparative analysis.</span>
                    <span class="lang-hi">प्रत्येक श्रेणी के लिए दो या तीन संबंधित चरों को पास-पास दंड बनाकर प्रदर्शित करता है (उदा. कारों और बाइकों का उत्पादन बनाम बिक्री)। प्रत्यक्ष तुलना हेतु सर्वोत्तम।</span>
                </li>
                <li>
                    <span class="key-badge">Subdivided (Stacked) Bar Chart</span>
                    <span class="lang-en">A single total bar is segmented into its component parts (e.g., Total college students broken into Arts, Science, Commerce). Height represents the aggregate, and segment heights show component shares.</span>
                    <span class="lang-hi">एक कुल दंड को उसके घटक भागों में विभाजित किया जाता है (उदा. कॉलेज के कुल विद्यार्थियों में कला, विज्ञान व वाणिज्य संकाय के छात्र)। कुल ऊंचाई योग दर्शाती है।</span>
                </li>
                <li>
                    <span class="key-badge">Percentage Stacked Bar Chart</span>
                    <span class="lang-en">All bars are normalized to an identical 100% height. Each segment represents the percentage share of that component. Ideal for comparing relative proportions when total volumes differ significantly.</span>
                    <span class="lang-hi">सभी दंडों की ऊंचाई 100% के बराबर रखी जाती है। प्रत्येक खंड घटक की प्रतिशत हिस्सेदारी दर्शाता है। जब कुल योग बहुत भिन्न हों, तो अनुपात की तुलना के लिए आदर्श।</span>
                </li>
                <li>
                    <span class="key-badge">Deviation Bar Chart</span>
                    <span class="lang-en">Features a central zero baseline. Positive deviations (profits, net trade surplus, budget surplus) extend upwards/rightwards, while negative deviations (losses, trade deficits) extend downwards/leftwards.</span>
                    <span class="lang-hi">इसमें एक केंद्रीय शून्य आधार रेखा होती है। धनात्मक विचलन (लाभ, अधिशेष) ऊपर की ओर तथा ऋणात्मक विचलन (हानि, घाटा) नीचे की ओर प्रदर्शित किए जाते हैं।</span>
                </li>
            </ul>

            <!-- SVG Diagram: Grouped Bar Chart -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 3.1: Annual Production vs Sales (in Thousand Units) of Alpha Motors (2020–2024)</span>
                    <span class="lang-hi">चित्र 3.1: अल्फा मोटर्स का वार्षिक उत्पादन बनाम बिक्री (हजार इकाइयों में) (2020–2024)</span>
                </h4>
                <svg viewBox="0 0 680 320" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Grouped Bar Chart showing Production and Sales">
                    <!-- Grid Lines -->
                    <line x1="70" y1="240" x2="640" y2="240" stroke="#cbd5e1" stroke-width="1.5"/>
                    <line x1="70" y1="190" x2="640" y2="190" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="140" x2="640" y2="140" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="90" x2="640" y2="90" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="40" x2="640" y2="40" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="40" x2="70" y2="240" stroke="#cbd5e1" stroke-width="1.5"/>

                    <!-- Y-Axis Labels -->
                    <text x="60" y="245" fill="#64748b" font-size="12" text-anchor="end">0</text>
                    <text x="60" y="195" fill="#64748b" font-size="12" text-anchor="end">25</text>
                    <text x="60" y="145" fill="#64748b" font-size="12" text-anchor="end">50</text>
                    <text x="60" y="95" fill="#64748b" font-size="12" text-anchor="end">75</text>
                    <text x="60" y="45" fill="#64748b" font-size="12" text-anchor="end">100</text>

                    <!-- Group 1: 2020 (Prod: 40, Sales: 35) -->
                    <rect x="100" y="160" width="35" height="80" rx="3" fill="#0d9488"/>
                    <text x="117" y="152" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">40</text>
                    <rect x="140" y="170" width="35" height="70" rx="3" fill="#f59e0b"/>
                    <text x="157" y="162" fill="#b45309" font-size="11" font-weight="bold" text-anchor="middle">35</text>
                    <text x="137" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2020</text>

                    <!-- Group 2: 2021 (Prod: 60, Sales: 50) -->
                    <rect x="210" y="120" width="35" height="120" rx="3" fill="#0d9488"/>
                    <text x="227" y="112" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">60</text>
                    <rect x="250" y="140" width="35" height="100" rx="3" fill="#f59e0b"/>
                    <text x="267" y="132" fill="#b45309" font-size="11" font-weight="bold" text-anchor="middle">50</text>
                    <text x="247" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2021</text>

                    <!-- Group 3: 2022 (Prod: 75, Sales: 70) -->
                    <rect x="320" y="90" width="35" height="150" rx="3" fill="#0d9488"/>
                    <text x="337" y="82" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">75</text>
                    <rect x="360" y="100" width="35" height="140" rx="3" fill="#f59e0b"/>
                    <text x="377" y="92" fill="#b45309" font-size="11" font-weight="bold" text-anchor="middle">70</text>
                    <text x="357" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2022</text>

                    <!-- Group 4: 2023 (Prod: 80, Sales: 65) -->
                    <rect x="430" y="80" width="35" height="160" rx="3" fill="#0d9488"/>
                    <text x="447" y="72" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">80</text>
                    <rect x="470" y="110" width="35" height="130" rx="3" fill="#f59e0b"/>
                    <text x="487" y="102" fill="#b45309" font-size="11" font-weight="bold" text-anchor="middle">65</text>
                    <text x="467" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2023</text>

                    <!-- Group 5: 2024 (Prod: 95, Sales: 90) -->
                    <rect x="540" y="50" width="35" height="190" rx="3" fill="#0d9488"/>
                    <text x="557" y="42" fill="#0f766e" font-size="11" font-weight="bold" text-anchor="middle">95</text>
                    <rect x="580" y="60" width="35" height="180" rx="3" fill="#f59e0b"/>
                    <text x="597" y="52" fill="#b45309" font-size="11" font-weight="bold" text-anchor="middle">90</text>
                    <text x="577" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2024</text>

                    <!-- Legend -->
                    <rect x="230" y="285" width="16" height="16" rx="2" fill="#0d9488"/>
                    <text x="255" y="298" fill="#182e26" font-size="13">Production (उत्पादन)</text>
                    <rect x="410" y="285" width="16" height="16" rx="2" fill="#f59e0b"/>
                    <text x="435" y="298" fill="#182e26" font-size="13">Sales (बिक्री)</text>
                </svg>
            </div>
        </section>

        <!-- Section 2: Line Graph Trends & Commercial Models -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-chart-line"></i>
                <span class="lang-en">2. Line Graphs: Trade Balance &amp; Profit-Loss Models</span>
                <span class="lang-hi">2. रेखा आरेख: व्यापार संतुलन एवं लाभ-हानि मॉडल</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>The Comprehensive Profit-Loss Framework in DI:</strong>
                <br>&bull; <code>Profit % = [(Income - Expenditure) / Expenditure] &times; 100</code>
                <br>&bull; <code>Income = Expenditure &times; [1 + (Profit % / 100)]</code>
                <br>&bull; <code>Expenditure = Income / [1 + (Profit % / 100)]</code>
                <br>&bull; <em>Ratio of Incomes:</em> If two companies have expenditures in ratio <code>E1 : E2 = a : b</code> and profit percentages <code>P1%</code> and <code>P2%</code>:
                <br><code>Income Ratio (I1 : I2) = [a &times; (100 + P1)] : [b &times; (100 + P2)]</code>
                <br>&bull; <em>Equal Income Case:</em> If incomes in two years are identical, their expenditures are in inverse ratio of their multiplier: <code>E1 / E2 = (100 + P2) / (100 + P1)</code>.</span>
                <span class="lang-hi"><strong>डीआई में लाभ-हानि का संपूर्ण गणितीय ढांचा:</strong>
                <br>&bull; <code>लाभ % = [(आय - व्यय) / व्यय] &times; 100</code>
                <br>&bull; <code>आय = व्यय &times; [1 + (लाभ % / 100)]</code>
                <br>&bull; <code>व्यय = आय / [1 + (लाभ % / 100)]</code>
                <br>&bull; <em>आय का अनुपात:</em> यदि दो कंपनियों के व्यय का अनुपात <code>a : b</code> है और लाभ % क्रमशः <code>P1</code> और <code>P2</code> हैं:
                <br><code>I1 : I2 = [a &times; (100 + P1)] : [b &times; (100 + P2)]</code>
                <br>&bull; <em>समान आय की स्थिति:</em> यदि दो वर्षों में आय समान हो, तो व्यय का अनुपात व्युत्क्रमानुपाती होता है: <code>E1 / E2 = (100 + P2) / (100 + P1)</code>।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">International Trade &amp; Balance of Trade</span>
                    <span class="lang-en"><strong>Trade Balance = Exports - Imports</strong>
                    <br>&bull; <strong>Trade Surplus:</strong> When Exports &gt; Imports (Trade balance is positive).
                    <br>&bull; <strong>Trade Deficit:</strong> When Imports &gt; Exports (Trade balance is negative).
                    <br>&bull; <strong>Export-to-Import Ratio Graphs:</strong>
                    <br>&nbsp;&nbsp;&bull; If <code>Exports / Imports > 1.0</code> &rarr; Trade Surplus.
                    <br>&nbsp;&nbsp;&bull; If <code>Exports / Imports < 1.0</code> &rarr; Trade Deficit.
                    <br>&nbsp;&nbsp;&bull; <em>Critical Exam Rule:</em> From a ratio graph of Exports/Imports alone, you <strong>CANNOT</strong> calculate the actual dollar value of exports or imports unless at least one absolute dollar figure is provided!</span>
                    <span class="lang-hi"><strong>अंतर्राष्ट्रीय व्यापार एवं व्यापार संतुलन</strong>
                    <br>&bull; <strong>व्यापार संतुलन = निर्यात - आयात</strong>
                    <br>&bull; <strong>व्यापार अधिशेष (Trade Surplus):</strong> जब निर्यात &gt; आयात हो (धनात्मक)।
                    <br>&bull; <strong>व्यापार घाटा (Trade Deficit):</strong> जब आयात &gt; निर्यात हो (ऋणात्मक)।
                    <br>&bull; <strong>निर्यात-से-आयात अनुपात ग्राफ:</strong>
                    <br>&nbsp;&nbsp;&bull; यदि <code>निर्यात / आयात > 1.0</code> &rarr; व्यापार अधिशेष।
                    <br>&nbsp;&nbsp;&bull; यदि <code>निर्यात / आयात < 1.0</code> &rarr; व्यापार घाटा।
                    <br>&nbsp;&nbsp;&bull; <em>अनिवार्य परीक्षा नियम:</em> केवल अनुपात ग्राफ से किसी वर्ष के वास्तविक डॉलर मूल्य की गणना <strong>नहीं</strong> की जा सकती जब तक कि कोई एक वास्तविक राशि न दी गई हो!</span>
                </li>
                <li>
                    <span class="key-badge">Slope &amp; Growth Trajectory in Line Graphs</span>
                    <span class="lang-en">The slope of a line segment between two successive time points represents the rate of change per unit time:
                    <br>&bull; Steepest upward slope &rarr; Maximum absolute growth.
                    <br>&bull; Steepest downward slope &rarr; Maximum absolute decline.
                    <br>&bull; Horizontal line segment &rarr; Zero growth (Status quo).
                    <br><em>Note:</em> The year with the highest absolute increase is often NOT the year with the highest percentage increase (due to different base values).</span>
                    <span class="lang-hi">दो समय बिंदुओं के बीच रेखा खंड का ढलान प्रति इकाई समय में परिवर्तन की दर को दर्शाता है:
                    <br>&bull; सर्वाधिक तीव्र ऊर्ध्वगामी ढलान &rarr; अधिकतम वास्तविक वृद्धि।
                    <br>&bull; सर्वाधिक तीव्र अधोगामी ढलान &rarr; अधिकतम वास्तविक गिरावट।
                    <br>&bull; क्षैतिज रेखा खंड &rarr; शून्य वृद्धि (स्थिरता)।
                    <br><em>ध्यान दें:</em> सर्वाधिक वास्तविक वृद्धि वाला वर्ष और सर्वाधिक प्रतिशत वृद्धि वाला वर्ष भिन्न हो सकते हैं (आधार मान भिन्न होने के कारण)।</span>
                </li>
            </ul>

            <!-- SVG Diagram: Multi-Line Graph for Imports vs Exports -->
            <div class="chart-container" style="background:var(--planner-bg-surface);border:1px solid var(--planner-border);border-radius:var(--card-radius);padding:1.5rem;margin:1.5rem 0;text-align:center;">
                <h4 style="margin-top:0;font-family:'Outfit',sans-serif;color:var(--planner-text-heading);">
                    <span class="lang-en">Figure 3.2: Merchandise Imports &amp; Exports of Country X (US$ Billion, 2020–2024)</span>
                    <span class="lang-hi">चित्र 3.2: देश X का वस्तुगत आयात एवं निर्यात (अमेरिकी डॉलर बिलियन में, 2020–2024)</span>
                </h4>
                <svg viewBox="0 0 680 320" width="100%" height="auto" style="max-width:680px;font-family:'DM Sans',sans-serif;" role="img" aria-label="Multi-Line Graph showing Imports and Exports">
                    <!-- Grid -->
                    <line x1="70" y1="240" x2="640" y2="240" stroke="#cbd5e1" stroke-width="1.5"/>
                    <line x1="70" y1="180" x2="640" y2="180" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="120" x2="640" y2="120" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="60" x2="640" y2="60" stroke="#f1f5f9" stroke-width="1"/>
                    <line x1="70" y1="40" x2="70" y2="240" stroke="#cbd5e1" stroke-width="1.5"/>

                    <!-- Y-Axis Labels -->
                    <text x="60" y="245" fill="#64748b" font-size="12" text-anchor="end">0</text>
                    <text x="60" y="185" fill="#64748b" font-size="12" text-anchor="end">20</text>
                    <text x="60" y="125" fill="#64748b" font-size="12" text-anchor="end">40</text>
                    <text x="60" y="65" fill="#64748b" font-size="12" text-anchor="end">60</text>

                    <!-- X-Axis Labels -->
                    <text x="130" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2020</text>
                    <text x="245" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2021</text>
                    <text x="360" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2022</text>
                    <text x="475" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2023</text>
                    <text x="590" y="260" fill="#334155" font-size="13" font-weight="bold" text-anchor="middle">2024</text>

                    <!-- Line 1: Imports (Red/Rose line: 2020=30, 2021=45, 2022=40, 2023=55, 2024=50) -->
                    <!-- Coordinates: 2020=(130, 150), 2021=(245, 105), 2022=(360, 120), 2023=(475, 75), 2024=(590, 90) -->
                    <polyline points="130,150 245,105 360,120 475,75 590,90" fill="none" stroke="#e11d48" stroke-width="3"/>
                    <circle cx="130" cy="150" r="5" fill="#e11d48"/>
                    <text x="130" y="140" fill="#e11d48" font-size="11" font-weight="bold" text-anchor="middle">30</text>
                    <circle cx="245" cy="105" r="5" fill="#e11d48"/>
                    <text x="245" y="95" fill="#e11d48" font-size="11" font-weight="bold" text-anchor="middle">45</text>
                    <circle cx="360" cy="120" r="5" fill="#e11d48"/>
                    <text x="360" y="110" fill="#e11d48" font-size="11" font-weight="bold" text-anchor="middle">40</text>
                    <circle cx="475" cy="75" r="5" fill="#e11d48"/>
                    <text x="475" y="65" fill="#e11d48" font-size="11" font-weight="bold" text-anchor="middle">55</text>
                    <circle cx="590" cy="90" r="5" fill="#e11d48"/>
                    <text x="590" y="80" fill="#e11d48" font-size="11" font-weight="bold" text-anchor="middle">50</text>

                    <!-- Line 2: Exports (Teal line: 2020=25, 2021=35, 2022=45, 2023=50, 2024=60) -->
                    <!-- Coordinates: 2020=(130, 165), 2021=(245, 135), 2022=(360, 105), 2023=(475, 90), 2024=(590, 60) -->
                    <polyline points="130,165 245,135 360,105 475,90 590,60" fill="none" stroke="#0d9488" stroke-width="3"/>
                    <circle cx="130" cy="165" r="5" fill="#0d9488"/>
                    <text x="130" y="185" fill="#0d9488" font-size="11" font-weight="bold" text-anchor="middle">25</text>
                    <circle cx="245" cy="135" r="5" fill="#0d9488"/>
                    <text x="245" y="155" fill="#0d9488" font-size="11" font-weight="bold" text-anchor="middle">35</text>
                    <circle cx="360" cy="105" r="5" fill="#0d9488"/>
                    <text x="360" y="95" fill="#0d9488" font-size="11" font-weight="bold" text-anchor="middle">45</text>
                    <circle cx="475" cy="90" r="5" fill="#0d9488"/>
                    <text x="475" y="110" fill="#0d9488" font-size="11" font-weight="bold" text-anchor="middle">50</text>
                    <circle cx="590" cy="60" r="5" fill="#0d9488"/>
                    <text x="590" y="50" fill="#0d9488" font-size="11" font-weight="bold" text-anchor="middle">60</text>

                    <!-- Legend -->
                    <line x1="220" y1="295" x2="250" y2="295" stroke="#e11d48" stroke-width="3"/>
                    <circle cx="235" cy="295" r="4" fill="#e11d48"/>
                    <text x="260" y="299" fill="#182e26" font-size="13">Imports (आयात)</text>

                    <line x1="410" y1="295" x2="440" y2="295" stroke="#0d9488" stroke-width="3"/>
                    <circle cx="425" cy="295" r="4" fill="#0d9488"/>
                    <text x="450" y="299" fill="#182e26" font-size="13">Exports (निर्यात)</text>
                </svg>
                <div style="font-size:0.88rem;color:var(--planner-text-muted);margin-top:0.5rem;">
                    <span class="lang-en">Trade Surplus occurred in 2022 ($45B &gt; $40B) and 2024 ($60B &gt; $50B). Trade Deficit occurred in 2020, 2021, and 2023.</span>
                    <span class="lang-hi">व्यापार अधिशेष (Trade Surplus) वर्ष 2022 और 2024 में हुआ। वर्ष 2020, 2021 और 2023 में व्यापार घाटा (Trade Deficit) रहा।</span>
                </div>
            </div>
        </section>

        <!-- Section 3: Analysis of Figures 3.1 and 3.2 -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-search-dollar"></i>
                <span class="lang-en">3. Worked Mathematical Calculations on the Visual Graphs</span>
                <span class="lang-hi">3. आरेखों पर आधारित प्रमुख गणितीय गणनाएं</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Analysis of Figure 3.1 (Alpha Motors):</strong>
                <br>&bull; <em>Unsold Inventory in 2023:</em> Production = 80, Sales = 65 &rarr; Unsold stock = 80 - 65 = 15 thousand units.
                <br>&bull; <em>Percentage of Production Sold in 2024:</em> (90 / 95) &times; 100 = (18 / 19) &times; 100 &approx; <strong>94.74%</strong>.
                <br>&bull; <em>Ratio of Sales in 2020 to Sales in 2024:</em> 35 : 90 = <strong>7 : 18</strong>.</span>
                <span class="lang-hi"><strong>चित्र 3.1 (अल्फा मोटर्स) का विश्लेषण:</strong>
                <br>&bull; <em>2023 में अनबिकी गाड़ियां:</em> उत्पादन = 80, बिक्री = 65 &rarr; शेष स्टॉक = 80 - 65 = 15 हजार इकाइयां।
                <br>&bull; <em>2024 में बेची गई कारों का प्रतिशत:</em> (90 / 95) &times; 100 &approx; <strong>94.74%</strong>।
                <br>&bull; <em>2020 की बिक्री का 2024 की बिक्री से अनुपात:</em> 35 : 90 = <strong>7 : 18</strong>।</span>
            </div>

            <div class="exam-pointer" style="background:var(--planner-bg-surface);border-left:4px solid var(--planner-warning);">
                <span class="lang-en"><strong>Analysis of Figure 3.2 (Foreign Trade):</strong>
                <br>&bull; <em>Maximum Trade Deficit Year:</em> 2021 (Imports = $45B, Exports = $35B &rarr; Deficit = <strong>$10 Billion</strong>).
                <br>&bull; <em>Maximum Trade Surplus Year:</em> 2024 (Exports = $60B, Imports = $50B &rarr; Surplus = <strong>$10 Billion</strong>).
                <br>&bull; <em>Percentage Growth in Exports from 2020 to 2024:</em> [(60 - 25) / 25] &times; 100 = (35 / 25) &times; 100 = <strong>140%</strong>.</span>
                <span class="lang-hi"><strong>चित्र 3.2 (विदेशी व्यापार) का विश्लेषण:</strong>
                <br>&bull; <em>सर्वाधिक व्यापार घाटे का वर्ष:</em> 2021 (आयात = $45B, निर्यात = $35B &rarr; घाटा = <strong>$10 बिलियन</strong>)।
                <br>&bull; <em>सर्वाधिक व्यापार अधिशेष का वर्ष:</em> 2024 (निर्यात = $60B, आयात = $50B &rarr; अधिशेष = <strong>$10 बिलियन</strong>)।
                <br>&bull; <em>2020 से 2024 तक निर्यात में प्रतिशत वृद्धि:</em> [(60 - 25) / 25] &times; 100 = <strong>140%</strong>।</span>
            </div>
        </section>
    """,

    # 30 Curated Practice Questions
    "practiceQuestions": [
        {
            "tag": "Bar Graph - Ratio",
            "qEn": "Based on Figure 3.1, what is the ratio of total production in 2020 and 2021 combined to total sales in 2023 and 2024 combined?",
            "qHi": "चित्र 3.1 के आधार पर, 2020 और 2021 के कुल उत्पादन का 2023 और 2024 की कुल बिक्री से अनुपात क्या है?",
            "opts": [
                ("A", "20 : 31", "20 : 31"),
                ("B", "100 : 155", "100 : 155"),
                ("C", "20 : 31", "20 : 31"),
                ("D", "25 : 32", "25 : 32")
            ],
            "ans": "A",
            "solEn": "Production (2020 + 2021) = 40 + 60 = 100. Sales (2023 + 2024) = 65 + 90 = 155. Ratio = 100 / 155 = 20 / 31.",
            "solHi": "उत्पादन (2020 + 2021) = 40 + 60 = 100। बिक्री (2023 + 2024) = 65 + 90 = 155। अनुपात = 100 : 155 = 20 : 31।"
        },
        {
            "tag": "Bar Graph - Growth",
            "qEn": "In Figure 3.1, in which year did production show the highest percentage increase compared to its previous year?",
            "qHi": "चित्र 3.1 में, पिछले वर्ष की तुलना में किस वर्ष उत्पादन में सर्वाधिक प्रतिशत वृद्धि दर्ज की गई?",
            "opts": [
                ("A", "2021", "2021"),
                ("B", "2022", "2022"),
                ("C", "2023", "2023"),
                ("D", "2024", "2024")
            ],
            "ans": "A",
            "solEn": "2021 Growth: (60 - 40)/40 = 20/40 = 50.0%. 2022: (75 - 60)/60 = 25.0%. 2023: (80 - 75)/75 = 6.67%. 2024: (95 - 80)/80 = 18.75%. Highest is 2021 (50%).",
            "solHi": "2021 में वृद्धि: (60 - 40)/40 = 50%। 2022: 25%। 2023: 6.67%। 2024: 18.75%। सर्वाधिक 2021 में (50%) रही।"
        },
        {
            "tag": "Bar Graph - Percentage",
            "qEn": "In Figure 3.1, in which year was the unsold stock (Production - Sales) the maximum?",
            "qHi": "चित्र 3.1 में, किस वर्ष अनबिका स्टॉक (उत्पादन - बिक्री) सर्वाधिक था?",
            "opts": [
                ("A", "2020", "2020"),
                ("B", "2021", "2021"),
                ("C", "2023", "2023"),
                ("D", "2022", "2022")
            ],
            "ans": "C",
            "solEn": "Unsold: 2020 = 40-35=5; 2021 = 60-50=10; 2022 = 75-70=5; 2023 = 80-65=15; 2024 = 95-90=5. Maximum is 2023 (15 thousand units).",
            "solHi": "अनबिका स्टॉक: 2020 में 5, 2021 में 10, 2022 में 5, 2023 में 15, 2024 में 5। सर्वाधिक 2023 (15 हजार) में था।"
        },
        {
            "tag": "Bar Graph - Average",
            "qEn": "What is the average annual sales of Alpha Motors over the 5-year period (2020–2024)?",
            "qHi": "5 वर्षों (2020–2024) में अल्फा मोटर्स की औसत वार्षिक बिक्री कितनी है?",
            "opts": [
                ("A", "60 thousand units", "60 हजार इकाइयां"),
                ("B", "62 thousand units", "62 हजार इकाइयां"),
                ("C", "65 thousand units", "65 हजार इकाइयां"),
                ("D", "70 thousand units", "70 हजार इकाइयां")
            ],
            "ans": "B",
            "solEn": "Total sales = 35 + 50 + 70 + 65 + 90 = 310. Average = 310 / 5 = 62 thousand units.",
            "solHi": "कुल बिक्री = 35 + 50 + 70 + 65 + 90 = 310। औसत = 310 / 5 = 62 हजार इकाइयां।"
        },
        {
            "tag": "Line Graph - Deficit",
            "qEn": "According to Figure 3.2, what was the total trade deficit across the years when imports exceeded exports?",
            "qHi": "चित्र 3.2 के अनुसार, उन वर्षों का कुल व्यापार घाटा कितना था जब आयात निर्यात से अधिक था?",
            "opts": [
                ("A", "$15 Billion", "$15 बिलियन"),
                ("B", "$20 Billion", "$20 बिलियन"),
                ("C", "$25 Billion", "$25 बिलियन"),
                ("D", "$10 Billion", "$10 बिलियन")
            ],
            "ans": "B",
            "solEn": "Imports > Exports in: 2020 (30 - 25 = 5), 2021 (45 - 35 = 10), and 2023 (55 - 50 = 5). Total Deficit = 5 + 10 + 5 = $20 Billion.",
            "solHi": "घाटे वाले वर्ष: 2020 (30 - 25 = 5), 2021 (45 - 35 = 10), तथा 2023 (55 - 50 = 5)। कुल घाटा = 5 + 10 + 5 = $20 बिलियन।"
        },
        {
            "tag": "Line Graph - Ratio",
            "qEn": "In Figure 3.2, what is the ratio of total exports to total imports over all 5 years?",
            "qHi": "चित्र 3.2 में, सभी 5 वर्षों में कुल निर्यात का कुल आयात से अनुपात क्या है?",
            "opts": [
                ("A", "43 : 44", "43 : 44"),
                ("B", "215 : 220", "215 : 220"),
                ("C", "43 : 44", "43 : 44"),
                ("D", "41 : 44", "41 : 44")
            ],
            "ans": "A",
            "solEn": "Total Exports = 25 + 35 + 45 + 50 + 60 = 215. Total Imports = 30 + 45 + 40 + 55 + 50 = 220. Ratio = 215 / 220 = 43 / 44.",
            "solHi": "कुल निर्यात = 215। कुल आयात = 220। अनुपात = 215 : 220 = 43 : 44।"
        },
        {
            "tag": "Line Graph - Percentage",
            "qEn": "In Figure 3.2, exports in 2024 were what percentage of imports in 2024?",
            "qHi": "चित्र 3.2 में, 2024 में निर्यात उसी वर्ष के आयात का कितना प्रतिशत था?",
            "opts": [
                ("A", "110%", "110%"),
                ("B", "120%", "120%"),
                ("C", "125%", "125%"),
                ("D", "83.33%", "83.33%")
            ],
            "ans": "B",
            "solEn": "Exports in 2024 = $60B; Imports in 2024 = $50B. Percentage = (60 / 50) &times; 100 = 120%.",
            "solHi": "2024 में निर्यात = $60B; आयात = $50B। प्रतिशत = (60 / 50) &times; 100 = 120%।"
        },
        {
            "tag": "Profit & Loss DI",
            "qEn": "A company's expenditure in 2022 was ₹400 crore and its profit was 25%. What was its income?",
            "qHi": "2022 में एक कंपनी का व्यय ₹400 करोड़ था और उसका लाभ 25% था। उसकी आय क्या थी?",
            "opts": [
                ("A", "₹480 crore", "₹480 करोड़"),
                ("B", "₹500 crore", "₹500 करोड़"),
                ("C", "₹525 crore", "₹525 करोड़"),
                ("D", "₹450 crore", "₹450 करोड़")
            ],
            "ans": "B",
            "solEn": "Income = Expenditure &times; (1 + Profit/100) = 400 &times; (1 + 0.25) = 400 &times; 1.25 = ₹500 crore.",
            "solHi": "आय = व्यय &times; 1.25 = 400 &times; 1.25 = ₹500 करोड़।"
        },
        {
            "tag": "Profit & Loss DI",
            "qEn": "If income of a company in 2023 was ₹660 crore and it earned 10% profit, what was its expenditure?",
            "qHi": "यदि 2023 में कंपनी की आय ₹660 करोड़ थी और उसने 10% लाभ कमाया, तो उसका व्यय कितना था?",
            "opts": [
                ("A", "₹600 crore", "₹600 करोड़"),
                ("B", "₹594 crore", "₹594 करोड़"),
                ("C", "₹610 crore", "₹610 करोड़"),
                ("D", "₹580 crore", "₹580 करोड़")
            ],
            "ans": "A",
            "solEn": "Expenditure = Income / (1 + Profit/100) = 660 / 1.10 = ₹600 crore.",
            "solHi": "व्यय = 660 / 1.10 = ₹600 करोड़।"
        },
        {
            "tag": "Bar Graph - Subdivided",
            "qEn": "In a subdivided bar chart of a school with 500 students, Boys segment is 280. What percentage of the bar is occupied by Girls?",
            "qHi": "500 विद्यार्थियों वाले विद्यालय के उप-विभाजित दंड आरेख में बालकों का खंड 280 है। बालिकाओं द्वारा दंड का कितना प्रतिशत भाग घेरा गया है?",
            "opts": [
                ("A", "56%", "56%"),
                ("B", "44%", "44%"),
                ("C", "48%", "48%"),
                ("D", "42%", "42%")
            ],
            "ans": "B",
            "solEn": "Girls = 500 - 280 = 220. Percentage = (220 / 500) &times; 100 = 44%.",
            "solHi": "बालिकाएं = 500 - 280 = 220। प्रतिशत = (220 / 500) &times; 100 = 44%।"
        },
        {
            "tag": "Line Graph - Slope",
            "qEn": "On a line graph plotting GDP over time, what does a steep upward slope between two points indicate?",
            "qHi": "समय के साथ जीडीपी दर्शाने वाले रेखा आरेख पर दो बिंदुओं के बीच तीव्र ऊपर की ओर ढलान क्या दर्शाता है?",
            "opts": [
                ("A", "Rapid rate of economic growth", "आर्थिक संवृद्धि की तीव्र दर"),
                ("B", "Stagnant economy", "स्थिर अर्थव्यवस्था"),
                ("C", "High inflation only", "केवल उच्च मुद्रास्फीति"),
                ("D", "Declining production", "घटता हुआ उत्पादन")
            ],
            "ans": "A",
            "solEn": "Slope = &Delta;Y / &Delta;X. A steep positive slope indicates a high positive rate of change (rapid growth).",
            "solHi": "ढाल = &Delta;Y / &Delta;X। तीव्र धनात्मक ढाल तेजी से हो रहे परिवर्तन (संवृद्धि) को दर्शाता है।"
        },
        {
            "tag": "Stacked Bar - Comparison",
            "qEn": "In a 100% stacked bar chart, why are the total heights of all bars identical across all years?",
            "qHi": "100% स्टैक्ड बार चार्ट में सभी वर्षों के लिए सभी दंडों की कुल ऊंचाई समान क्यों होती है?",
            "opts": [
                ("A", "Because absolute production was equal", "क्योंकि वास्तविक उत्पादन बराबर था"),
                ("B", "Because each bar represents 100% of its respective total", "क्योंकि प्रत्येक दंड अपने संबंधित योग के 100% को दर्शाता है"),
                ("C", "Because of graphing errors", "आरेखीय त्रुटि के कारण"),
                ("D", "To hide missing data", "अज्ञात डेटा छिपाने के लिए")
            ],
            "ans": "B",
            "solEn": "A percentage stacked bar chart normalizes every aggregate to 100% to allow direct comparison of relative percentage shares.",
            "solHi": "100% स्टैक्ड बार चार्ट प्रत्येक योग को 100% में बदलता है ताकि केवल प्रतिशत अंशों की तुलना की जा सके।"
        },
        {
            "tag": "Line Graph - Growth Rate",
            "qEn": "In Figure 3.2, what was the percentage increase in imports from 2020 ($30B) to 2023 ($55B)?",
            "qHi": "चित्र 3.2 में, 2020 ($30B) से 2023 ($55B) तक आयात में कितने प्रतिशत की वृद्धि हुई?",
            "opts": [
                ("A", "83.33%", "83.33%"),
                ("B", "75.00%", "75.00%"),
                ("C", "80.00%", "80.00%"),
                ("D", "66.67%", "66.67%")
            ],
            "ans": "A",
            "solEn": "Increase = 55 - 30 = 25. Percentage = (25 / 30) &times; 100 = (5/6) &times; 100 = 83.33%.",
            "solHi": "वृद्धि = 55 - 30 = 25। प्रतिशत = (25 / 30) &times; 100 = 5/6 &times; 100 = 83.33%।"
        },
        {
            "tag": "Bar Graph - Ratio",
            "qEn": "In Figure 3.1, what is the ratio of production to sales in the year 2022?",
            "qHi": "चित्र 3.1 में, वर्ष 2022 में उत्पादन का बिक्री से अनुपात क्या है?",
            "opts": [
                ("A", "15 : 14", "15 : 14"),
                ("B", "14 : 15", "14 : 15"),
                ("C", "5 : 4", "5 : 4"),
                ("D", "8 : 7", "8 : 7")
            ],
            "ans": "A",
            "solEn": "Production 2022 = 75; Sales 2022 = 70. Ratio = 75 / 70 = 15 / 14.",
            "solHi": "उत्पादन 2022 = 75; बिक्री 2022 = 70। अनुपात = 75 : 70 = 15 : 14।"
        },
        {
            "tag": "Profit Comparison Trap",
            "qEn": "Company P had 20% profit on ₹100 cr expenditure. Company Q had 25% profit on ₹60 cr expenditure. Which company made higher rupee profit?",
            "qHi": "कंपनी P को ₹100 करोड़ व्यय पर 20% लाभ हुआ। कंपनी Q को ₹60 करोड़ व्यय पर 25% लाभ हुआ। किस कंपनी ने रुपये में अधिक लाभ कमाया?",
            "opts": [
                ("A", "Company P (₹20 cr)", "कंपनी P (₹20 करोड़)"),
                ("B", "Company Q (₹15 cr)", "कंपनी Q (₹15 करोड़)"),
                ("C", "Both made equal rupee profit", "दोनों का लाभ बराबर था"),
                ("D", "Cannot be determined", "निर्धारित नहीं किया जा सकता")
            ],
            "ans": "A",
            "solEn": "Profit P = 20% of 100 = ₹20 cr. Profit Q = 25% of 60 = ₹15 cr. Company P made higher absolute profit despite having a lower percentage profit.",
            "solHi": "P का लाभ = 100 का 20% = ₹20 करोड़। Q का लाभ = 60 का 25% = ₹15 करोड़। अतः कंपनी P ने रुपये में अधिक लाभ कमाया।"
        },
        {
            "tag": "Bar Graph - Total Share",
            "qEn": "In Figure 3.1, production in 2024 (95k) represents approximately what percentage of the total 5-year production (350k)?",
            "qHi": "चित्र 3.1 में, 2024 का उत्पादन (95k) कुल 5 वर्षों के उत्पादन (350k) का लगभग कितना प्रतिशत है?",
            "opts": [
                ("A", "25.5%", "25.5%"),
                ("B", "27.1%", "27.1%"),
                ("C", "29.4%", "29.4%"),
                ("D", "31.2%", "31.2%")
            ],
            "ans": "B",
            "solEn": "Total production = 40 + 60 + 75 + 80 + 95 = 350. Percentage = (95 / 350) &times; 100 = 19/70 &times; 100 &approx; 27.14%.",
            "solHi": "कुल उत्पादन = 350। प्रतिशत = (95 / 350) &times; 100 &approx; 27.14%।"
        },
        {
            "tag": "Line Graph - Fluctuations",
            "qEn": "In Figure 3.2, which year registered a decrease in imports compared to its preceding year?",
            "qHi": "चित्र 3.2 में, पिछले वर्ष की तुलना में किस वर्ष आयात में गिरावट दर्ज की गई?",
            "opts": [
                ("A", "2021", "2021"),
                ("B", "2022 and 2024", "2022 और 2024"),
                ("C", "2023", "2023"),
                ("D", "No year showed a decrease", "किसी वर्ष में गिरावट नहीं हुई")
            ],
            "ans": "B",
            "solEn": "Imports dropped in 2022 (40 vs 45 in 2021) and in 2024 (50 vs 55 in 2023).",
            "solHi": "आयात 2022 में (40 vs 45) तथा 2024 में (50 vs 55) गिरा।"
        },
        {
            "tag": "Line Graph - Consecutive Growth",
            "qEn": "In Figure 3.2, how many consecutive years of growth did Exports experience?",
            "qHi": "चित्र 3.2 में, निर्यात ने लगातार कितने वर्षों तक निरंतर वृद्धि दर्ज की?",
            "opts": [
                ("A", "All 4 consecutive intervals (2020 to 2024)", "सभी 4 अंतरालों में (2020 से 2024 तक)"),
                ("B", "Only 2 years", "केवल 2 वर्ष"),
                ("C", "Only 3 years", "केवल 3 वर्ष"),
                ("D", "None", "कोई नहीं")
            ],
            "ans": "A",
            "solEn": "Exports rose every single year: 25 &rarr; 35 &rarr; 45 &rarr; 50 &rarr; 60. That is continuous growth across all 4 yearly transitions.",
            "solHi": "निर्यात प्रत्येक वर्ष बढ़ा: 25 से 35, 45, 50, 60। अतः सभी 4 अंतरालों में निरंतर वृद्धि रही।"
        },
        {
            "tag": "Bar Chart - Comparative Ratio",
            "qEn": "If in 2023 Alpha Motors sold 65 thousand units at an average price of ₹5 lakh per unit, what was its total sales revenue?",
            "qHi": "यदि 2023 में अल्फा मोटर्स ने 65 हजार कारें ₹5 लाख प्रति कार के औसत मूल्य पर बेचीं, तो उसका कुल बिक्री राजस्व कितना था?",
            "opts": [
                ("A", "₹3,250 crore", "₹3,250 करोड़"),
                ("B", "₹325 crore", "₹325 करोड़"),
                ("C", "₹32,500 crore", "₹32,500 करोड़"),
                ("D", "₹650 crore", "₹650 करोड़")
            ],
            "ans": "A",
            "solEn": "65,000 &times; ₹5,00,000 = ₹32,500,000,000 = ₹3,250 crore. (1 crore = 10^7).",
            "solHi": "65,000 &times; ₹5,00,000 = ₹32,50,00,00,000 = ₹3,250 करोड़।"
        },
        {
            "tag": "Bar Chart - Percentage More",
            "qEn": "In Figure 3.1, sales in 2022 (70k) was what percent more than sales in 2020 (35k)?",
            "qHi": "चित्र 3.1 में, 2022 की बिक्री (70k) 2020 की बिक्री (35k) से कितने प्रतिशत अधिक थी?",
            "opts": [
                ("A", "50%", "50%"),
                ("B", "100%", "100%"),
                ("C", "200%", "200%"),
                ("D", "75%", "75%")
            ],
            "ans": "B",
            "solEn": "Increase = 70 - 35 = 35k. Percentage more = (35 / 35) &times; 100 = 100%.",
            "solHi": "वृद्धि = 70 - 35 = 35k। प्रतिशत अधिक = (35 / 35) &times; 100 = 100%।"
        },
        {
            "tag": "Line Graph - Average Difference",
            "qEn": "What is the difference between average annual imports and average annual exports in Figure 3.2?",
            "qHi": "चित्र 3.2 में औसत वार्षिक आयात और औसत वार्षिक निर्यात के बीच क्या अंतर है?",
            "opts": [
                ("A", "$1 Billion", "$1 बिलियन"),
                ("B", "$2 Billion", "$2 बिलियन"),
                ("C", "$1.5 Billion", "$1.5 बिलियन"),
                ("D", "$0.5 Billion", "$0.5 बिलियन")
            ],
            "ans": "A",
            "solEn": "Avg Imports = 220 / 5 = $44B. Avg Exports = 215 / 5 = $43B. Difference = 44 - 43 = $1 Billion.",
            "solHi": "औसत आयात = 220 / 5 = $44B। औसत निर्यात = 215 / 5 = $43B। अंतर = 44 - 43 = $1 बिलियन।"
        },
        {
            "tag": "Horizontal Bar Chart",
            "qEn": "When data category labels are very lengthy (e.g. detailed government schemes), which bar orientation is preferred?",
            "qHi": "जब श्रेणियों के नाम बहुत लंबे हों (जैसे विस्तृत सरकारी योजनाएं), तो किस दंड अभिविन्यास (bar orientation) को प्राथमिकता दी जाती है?",
            "opts": [
                ("A", "Horizontal Bar Chart", "क्षैतिज दंड आरेख (Horizontal)"),
                ("B", "Vertical Bar Chart", "ऊर्ध्वाधर दंड आरेख (Vertical)"),
                ("C", "Line Graph", "रेखा आरेख"),
                ("D", "Pie Chart", "पाई चार्ट")
            ],
            "ans": "A",
            "solEn": "Horizontal bar charts provide ample horizontal space along the Y-axis to display lengthy text labels without crowding or tilting.",
            "solHi": "क्षैतिज दंड आरेख में लंबे पाठ्य शीर्षकों को बिना घुमाए स्पष्ट रूप से लिखने के लिए पर्याप्त स्थान मिलता है।"
        },
        {
            "tag": "Profit % Model",
            "qEn": "Expenditure is ₹200 cr and Income is ₹260 cr. What is the profit percentage?",
            "qHi": "व्यय ₹200 करोड़ है और आय ₹260 करोड़ है। लाभ प्रतिशत क्या है?",
            "opts": [
                ("A", "25%", "25%"),
                ("B", "30%", "30%"),
                ("C", "35%", "35%"),
                ("D", "23.07%", "23.07%")
            ],
            "ans": "B",
            "solEn": "Profit = 260 - 200 = ₹60 cr. Profit % = (60 / 200) &times; 100 = 30%.",
            "solHi": "लाभ = 260 - 200 = ₹60 करोड़। लाभ % = (60 / 200) &times; 100 = 30%।"
        },
        {
            "tag": "Loss % Model",
            "qEn": "Expenditure is ₹500 cr and Income is ₹450 cr. What is the loss percentage?",
            "qHi": "व्यय ₹500 करोड़ है और आय ₹450 करोड़ है। हानि प्रतिशत क्या है?",
            "opts": [
                ("A", "10%", "10%"),
                ("B", "11.11%", "11.11%"),
                ("C", "9.09%", "9.09%"),
                ("D", "12.5%", "12.5%")
            ],
            "ans": "A",
            "solEn": "Loss = 500 - 450 = ₹50 cr. Loss % = (50 / 500) &times; 100 = 10%. (Base is always Expenditure).",
            "solHi": "हानि = 500 - 450 = ₹50 करोड़। हानि % = (50 / 500) &times; 100 = 10% (आधार सदैव व्यय होता है)।"
        },
        {
            "tag": "Bar Graph - Percentage Share",
            "qEn": "In 2021 (Figure 3.1), sales (50k) represented what percentage of production (60k)?",
            "qHi": "2021 में (चित्र 3.1), बिक्री (50k) उत्पादन (60k) का कितना प्रतिशत थी?",
            "opts": [
                ("A", "83.33%", "83.33%"),
                ("B", "80.00%", "80.00%"),
                ("C", "85.00%", "85.00%"),
                ("D", "75.00%", "75.00%")
            ],
            "ans": "A",
            "solEn": "Percentage = (50 / 60) &times; 100 = (5/6) &times; 100 = 83.33%.",
            "solHi": "प्रतिशत = (50 / 60) &times; 100 = 5/6 &times; 100 = 83.33%।"
        },
        {
            "tag": "Line Graph - Peak",
            "qEn": "In Figure 3.2, which year recorded the peak value for Merchandise Exports?",
            "qHi": "चित्र 3.2 में, किस वर्ष वस्तुगत निर्यात का शिखर (उच्चतम) मान दर्ज किया गया?",
            "opts": [
                ("A", "2023", "2023"),
                ("B", "2024", "2024"),
                ("C", "2022", "2022"),
                ("D", "2021", "2021")
            ],
            "ans": "B",
            "solEn": "Peak export occurred in 2024 at $60 Billion.",
            "solHi": "निर्यात का शिखर मान 2024 में $60 बिलियन दर्ज किया गया।"
        },
        {
            "tag": "Line Graph - Trough",
            "qEn": "In Figure 3.2, which year recorded the lowest value for Merchandise Imports?",
            "qHi": "चित्र 3.2 में, किस वर्ष वस्तुगत आयात का न्यूनतम मान दर्ज किया गया?",
            "opts": [
                ("A", "2020", "2020"),
                ("B", "2022", "2022"),
                ("C", "2021", "2021"),
                ("D", "2024", "2024")
            ],
            "ans": "A",
            "solEn": "Lowest import was in 2020 at $30 Billion.",
            "solHi": "आयात का न्यूनतम मान 2020 में $30 बिलियन था।"
        },
        {
            "tag": "Grouped Bar - Ratio",
            "qEn": "In Figure 3.1, what was the ratio of total production in 2024 to total production in 2020?",
            "qHi": "चित्र 3.1 में, 2024 के कुल उत्पादन का 2020 के कुल उत्पादन से क्या अनुपात था?",
            "opts": [
                ("A", "19 : 8", "19 : 8"),
                ("B", "95 : 40", "95 : 40"),
                ("C", "19 : 8", "19 : 8"),
                ("D", "23 : 10", "23 : 10")
            ],
            "ans": "A",
            "solEn": "Production 2024 = 95; Production 2020 = 40. Ratio = 95 / 40 = 19 / 8.",
            "solHi": "उत्पादन 2024 = 95; उत्पादन 2020 = 40। अनुपात = 95 : 40 = 19 : 8।"
        },
        {
            "tag": "Trade Balance Condition",
            "qEn": "When Merchandise Exports exceed Merchandise Imports, what is the resulting economic condition called?",
            "qHi": "जब वस्तुगत निर्यात वस्तुगत आयात से अधिक होता है, तो परिणामी आर्थिक स्थिति को क्या कहा जाता है?",
            "opts": [
                ("A", "Trade Deficit", "व्यापार घाटा (Trade Deficit)"),
                ("B", "Trade Surplus", "व्यापार अधिशेष (Trade Surplus)"),
                ("C", "Fiscal Deficit", "राजकोषीय घाटा"),
                ("D", "Revenue Deficit", "राजस्व घाटा")
            ],
            "ans": "B",
            "solEn": "Exports > Imports produces a Trade Surplus (favorable balance of trade).",
            "solHi": "निर्यात > आयात होने पर व्यापार अधिशेष (Trade Surplus) की स्थिति होती है।"
        },
        {
            "tag": "Visual Trap",
            "qEn": "Why should a candidate avoid judging percentage growth purely by visually comparing heights of bars from different graphs?",
            "qHi": "विभिन्न आरेखों के दंडों की केवल ऊंचाई देखकर प्रतिशत वृद्धि का अनुमान लगाने से अभ्यर्थी को क्यों बचना चाहिए?",
            "opts": [
                ("A", "Scales and base units may differ between different graphs", "विभिन्न आरेखों में पैमाने (scales) और आधार इकाइयां भिन्न हो सकती हैं"),
                ("B", "Bars are drawn randomly", "दंड अनियमित रूप से बनाए जाते हैं"),
                ("C", "Colors distort the height", "रंगों से ऊंचाई बदल जाती है"),
                ("D", "Percentage is always equal to bar width", "प्रतिशत सदैव दंड की चौड़ाई के बराबर होता है")
            ],
            "ans": "A",
            "solEn": "Different graphs often have different Y-axis scale divisions or baseline values. Visual heights can be profoundly misleading without reading the numerical axes.",
            "solHi": "अलग-अलग आरेखों में Y-अक्ष का पैमाना भिन्न हो सकता है, जिससे केवल ऊंचाई देखकर अनुमान लगाने पर भ्रम हो सकता है।"
        }
    ],

    # 15 Mini-Test MCQs
    "testQuestions": [
        {
            "qEn": "In Figure 3.1, what was the total sales of Alpha Motors in 2020 and 2024 combined?",
            "qHi": "चित्र 3.1 में, 2020 और 2024 को मिलाकर अल्फा मोटर्स की कुल बिक्री कितनी थी?",
            "opts": [
                ("A", "125 thousand units", "125 हजार इकाइयां"),
                ("B", "130 thousand units", "130 हजार इकाइयां"),
                ("C", "135 thousand units", "135 हजार इकाइयां"),
                ("D", "120 thousand units", "120 हजार इकाइयां")
            ]
        },
        {
            "qEn": "In Figure 3.2, in which year was the trade balance most favorable (highest surplus)?",
            "qHi": "चित्र 3.2 में, किस वर्ष व्यापार संतुलन सर्वाधिक अनुकूल (सर्वोच्च अधिशेष) रहा?",
            "opts": [
                ("A", "2020", "2020"),
                ("B", "2022", "2022"),
                ("C", "2024", "2024"),
                ("D", "2021", "2021")
            ]
        },
        {
            "qEn": "If expenditure is ₹800 cr and profit is 20%, what is the income?",
            "qHi": "यदि व्यय ₹800 करोड़ है और लाभ 20% है, तो आय क्या है?",
            "opts": [
                ("A", "₹960 cr", "₹960 करोड़"),
                ("B", "₹1,000 cr", "₹1,000 करोड़"),
                ("C", "₹940 cr", "₹940 करोड़"),
                ("D", "₹980 cr", "₹980 करोड़")
            ]
        },
        {
            "qEn": "In Figure 3.1, what was the percentage increase in sales from 2021 (50k) to 2022 (70k)?",
            "qHi": "चित्र 3.1 में, 2021 (50k) से 2022 (70k) तक बिक्री में कितने प्रतिशत की वृद्धि हुई?",
            "opts": [
                ("A", "35%", "35%"),
                ("B", "40%", "40%"),
                ("C", "45%", "45%"),
                ("D", "30%", "30%")
            ]
        },
        {
            "qEn": "In Figure 3.2, what was the trade deficit in the year 2021?",
            "qHi": "चित्र 3.2 में, वर्ष 2021 में व्यापार घाटा कितना था?",
            "opts": [
                ("A", "$5 Billion", "$5 बिलियन"),
                ("B", "$10 Billion", "$10 बिलियन"),
                ("C", "$15 Billion", "$15 बिलियन"),
                ("D", "$8 Billion", "$8 बिलियन")
            ]
        },
        {
            "qEn": "If a bar chart uses a zigzag break (kink) on the Y-axis from 0 to 100, what is its primary effect?",
            "qHi": "यदि कोई बार चार्ट Y-अक्ष पर 0 से 100 तक ज़िगज़ैग ब्रेक का उपयोग करता है, तो इसका मुख्य प्रभाव क्या होता है?",
            "opts": [
                ("A", "Visually magnifies small differences above 100", "100 से ऊपर के छोटे अंतरों को दृष्टिगत रूप से बड़ा दिखाता है"),
                ("B", "Reduces calculation accuracy", "गणना की सटीकता घटाता है"),
                ("C", "Inverts the values", "मानों को उल्टा कर देता है"),
                ("D", "Eliminates percentages", "प्रतिशत को समाप्त करता है")
            ]
        },
        {
            "qEn": "In Figure 3.1, in which year was the ratio of sales to production the lowest?",
            "qHi": "चित्र 3.1 में, किस वर्ष बिक्री का उत्पादन से अनुपात न्यूनतम था?",
            "opts": [
                ("A", "2023 (65/80 = 81.25%)", "2023 (65/80 = 81.25%)"),
                ("B", "2020 (35/40 = 87.5%)", "2020 (35/40 = 87.5%)"),
                ("C", "2024 (90/95 = 94.7%)", "2024 (90/95 = 94.7%)"),
                ("D", "2022 (70/75 = 93.3%)", "2022 (70/75 = 93.3%)")
            ]
        },
        {
            "qEn": "Total exports across 2020–2024 in Figure 3.2 was:",
            "qHi": "चित्र 3.2 में 2020–2024 के दौरान कुल निर्यात कितना था?",
            "opts": [
                ("A", "$210 Billion", "$210 बिलियन"),
                ("B", "$215 Billion", "$215 बिलियन"),
                ("C", "$220 Billion", "$220 बिलियन"),
                ("D", "$225 Billion", "$225 बिलियन")
            ]
        },
        {
            "qEn": "If income is ₹520 cr and expenditure is ₹400 cr, profit % is:",
            "qHi": "यदि आय ₹520 करोड़ है और व्यय ₹400 करोड़ है, तो लाभ % है:",
            "opts": [
                ("A", "30%", "30%"),
                ("B", "25%", "25%"),
                ("C", "23%", "23%"),
                ("D", "35%", "35%")
            ]
        },
        {
            "qEn": "In a line graph, if two curves intersect at a specific year, what does it signify?",
            "qHi": "रेखा आरेख में यदि किसी विशिष्ट वर्ष में दो वक्र एक-दूसरे को काटते हैं, तो इसका क्या अर्थ है?",
            "opts": [
                ("A", "The values of both variables are equal in that year", "उस वर्ष दोनों चरों के मान समान हैं"),
                ("B", "Growth rate is zero", "संवृद्धि दर शून्य है"),
                ("C", "Both companies incurred losses", "दोनों कंपनियों को हानि हुई"),
                ("D", "Production ceased", "उत्पादन बंद हो गया")
            ]
        },
        {
            "qEn": "In Figure 3.1, what was the total production across all 5 years?",
            "qHi": "चित्र 3.1 में सभी 5 वर्षों का कुल उत्पादन कितना था?",
            "opts": [
                ("A", "350 thousand units", "350 हजार इकाइयां"),
                ("B", "340 thousand units", "340 हजार इकाइयां"),
                ("C", "360 thousand units", "360 हजार इकाइयां"),
                ("D", "330 thousand units", "330 हजार इकाइयां")
            ]
        },
        {
            "qEn": "In Figure 3.2, by what percentage did exports grow from 2021 ($35B) to 2022 ($45B)?",
            "qHi": "चित्र 3.2 में, 2021 ($35B) से 2022 ($45B) तक निर्यात में कितने प्रतिशत की वृद्धि हुई?",
            "opts": [
                ("A", "28.57%", "28.57%"),
                ("B", "25.00%", "25.00%"),
                ("C", "30.00%", "30.00%"),
                ("D", "22.22%", "22.22%")
            ]
        },
        {
            "qEn": "A bar chart where segments of each bar add up to 100% is called a:",
            "qHi": "वह बार चार्ट जिसके प्रत्येक दंड के खंड मिलकर 100% बनाते हैं, क्या कहलाता है?",
            "opts": [
                ("A", "Simple bar chart", "सरल दंड आरेख"),
                ("B", "Percentage bar chart", "प्रतिशत दंड आरेख"),
                ("C", "Multiple bar chart", "बहु-दंड आरेख"),
                ("D", "Histogram", "आयतचित्र")
            ]
        },
        {
            "qEn": "If a company's income is ₹720 cr with 20% loss, what was its expenditure?",
            "qHi": "यदि 20% हानि के साथ कंपनी की आय ₹720 करोड़ है, तो उसका व्यय कितना था?",
            "opts": [
                ("A", "₹900 cr", "₹900 करोड़"),
                ("B", "₹864 cr", "₹864 करोड़"),
                ("C", "₹850 cr", "₹850 करोड़"),
                ("D", "₹880 cr", "₹880 करोड़")
            ]
        },
        {
            "qEn": "In Figure 3.1, what was the average annual production from 2020 to 2024?",
            "qHi": "चित्र 3.1 में 2020 से 2024 तक औसत वार्षिक उत्पादन कितना था?",
            "opts": [
                ("A", "70 thousand units", "70 हजार इकाइयां"),
                ("B", "68 thousand units", "68 हजार इकाइयां"),
                ("C", "72 thousand units", "72 हजार इकाइयां"),
                ("D", "65 thousand units", "65 हजार इकाइयां")
            ]
        }
    ],

    "testDataJson": json.dumps([
        {"ans": "A", "solEn": "Sales: 2020 (35) + 2024 (90) = 125 thousand units.", "solHi": "बिक्री: 2020 में 35 + 2024 में 90 = 125 हजार इकाइयां।"},
        {"ans": "C", "solEn": "Surplus in 2024 = $60B - $50B = $10B (highest surplus).", "solHi": "2024 में अधिशेष = 60 - 50 = $10B (सर्वोच्च)।"},
        {"ans": "A", "solEn": "Income = 800 &times; 1.20 = ₹960 crore.", "solHi": "आय = 800 &times; 1.20 = ₹960 करोड़।"},
        {"ans": "B", "solEn": "Increase = 70 - 50 = 20. (20 / 50) &times; 100 = 40%.", "solHi": "वृद्धि = 20। (20 / 50) &times; 100 = 40%।"},
        {"ans": "B", "solEn": "Deficit = Imports (45) - Exports (35) = $10 Billion.", "solHi": "घाटा = आयात (45) - निर्यात (35) = $10 बिलियन।"},
        {"ans": "A", "solEn": "A kink compresses the 0-100 zone, visually exaggerating variations above 100.", "solHi": "यह 0 से 100 के क्षेत्र को दबाकर ऊपर के छोटे अंतरों को बड़ा दिखाता है।"},
        {"ans": "A", "solEn": "2023 ratio = 65 / 80 = 81.25% (lowest of all years).", "solHi": "2023 में 65/80 = 81.25% न्यूनतम था।"},
        {"ans": "B", "solEn": "25 + 35 + 45 + 50 + 60 = $215 Billion.", "solHi": "25 + 35 + 45 + 50 + 60 = $215 बिलियन।"},
        {"ans": "A", "solEn": "Profit = 120. (120 / 400) &times; 100 = 30%.", "solHi": "लाभ = 120। (120 / 400) &times; 100 = 30%।"},
        {"ans": "A", "solEn": "Intersection point coordinates mean both lines have identical values at that year.", "solHi": "प्रतिच्छेद बिंदु पर दोनों चरों के संख्यात्मक मान बराबर होते हैं।"},
        {"ans": "A", "solEn": "40 + 60 + 75 + 80 + 95 = 350 thousand units.", "solHi": "40 + 60 + 75 + 80 + 95 = 350 हजार इकाइयां।"},
        {"ans": "A", "solEn": "Increase = 45 - 35 = 10. (10 / 35) &times; 100 = 2/7 &times; 100 = 28.57%.", "solHi": "वृद्धि = 10। (10 / 35) &times; 100 = 2/7 &times; 100 = 28.57%।"},
        {"ans": "B", "solEn": "Percentage bar charts normalize totals to 100%.", "solHi": "प्रतिशत बार चार्ट में प्रत्येक दंड का कुल योग 100% होता है।"},
        {"ans": "A", "solEn": "With 20% loss: Income = Expenditure &times; 0.80 &rarr; Expenditure = 720 / 0.80 = ₹900 crore.", "solHi": "व्यय = 720 / 0.80 = ₹900 करोड़।"},
        {"ans": "A", "solEn": "Total production = 350. Average = 350 / 5 = 70 thousand units.", "solHi": "कुल उत्पादन = 350। औसत = 350 / 5 = 70 हजार इकाइयां।"}
    ])
}
