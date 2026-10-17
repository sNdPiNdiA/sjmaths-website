"""
topic5.py
Topic 5: Tabulation & Table Analysis: Missing Data, Ratios & Multi-Tables
Slug: tabulation-and-table-analysis
"""

import json

TOPIC_5 = {
    "slug": "tabulation-and-table-analysis",
    "titleEn": "Tabulation & Table Analysis: Missing Data & Multi-Tables",
    "titleHi": "सारणीयन एवं तालिका विश्लेषण: लुप्त आंकड़े व बहु-तालिका",
    "pageTitle": "Tabulation & Table Analysis: Missing Data & Multi-Tables | UPSSSC Mains | SJMaths",
    "metaDesc": "Pointwise revision notes, 30 practice MCQs with step-by-step solutions, and a 15-Q test on Tabulation & Table Analysis (Missing Data Tables, Multi-variable tables, and Percentages) for UPSSSC Intermediate Level Mains 2026.",
    "metaTagEn": "Part-1 (9): Data Interpretation & Statistical Analysis | Tabulation & Missing Data",
    "metaTagHi": "भाग-1 (9): डाटा इंटरप्रिटेशन एवं सांख्यिकीय विश्लेषण | सारणीयन एवं लुप्त आंकड़े",
    "subtitleEn": "Exhaustive bilingual guide to complex data tables, missing data reconstruction, multi-variable cross-tabulation, percentage matrices, and speed math methods for UPSSSC Intermediate Level Mains.",
    "subtitleHi": "जटिल सांख्यिकीय तालिकाओं, लुप्त डेटा निर्धारण, बहु-चर क्रॉस-सारणीयन, प्रतिशत आव्यूह और तीव्र गणना विधियों का संपूर्ण द्विभाषी अध्ययन गाइड व अभ्यास सेट।",
    "crumbNameEn": "Tabulation & Table Analysis",
    "crumbNameHi": "सारणीयन एवं तालिका विश्लेषण",

    "notesHtml": """
        <!-- Section 1: Anatomy & Architecture of Statistical Tables -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-table"></i>
                <span class="lang-en">1. Anatomy &amp; Architecture of Statistical Tables</span>
                <span class="lang-hi">1. सांख्यिकीय तालिकाओं की संरचना एवं घटक</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Core Table Components:</strong>
                <br>&bull; <strong>Title (शीर्षक):</strong> Identifies the universe, time period, and unit of measurement.
                <br>&bull; <strong>Stub (पंक्ति शीर्षक):</strong> Extreme left column containing row designations.
                <br>&bull; <strong>Caption (स्तंभ शीर्षक):</strong> Top headers identifying column variables and sub-heads.
                <br>&bull; <strong>Body Cells:</strong> Numerical entries formed at the intersection of rows and columns.
                <br>&bull; <strong>Footnotes &amp; Source Notes:</strong> Crucial explanatory caveats (e.g., '*' indicates estimated figure; figures in brackets denote percentages).</span>
                <span class="lang-hi"><strong>तालिका के प्रमुख घटक:</strong>
                <br>&bull; <strong>शीर्षक (Title):</strong> अध्ययन का विषय, समय अवधि एवं इकाई दर्शाता है।
                <br>&bull; <strong>स्टब (Stub):</strong> सबसे बायां स्तंभ जो पंक्तियों के नाम/विवरण को दर्शाता है।
                <br>&bull; <strong>कैप्शन (Caption):</strong> शीर्ष पर स्थित कॉलम हेडर जो स्तंभ चरों की पहचान करते हैं।
                <br>&bull; <strong>बॉडी (Body):</strong> पंक्तियों और स्तंभों के प्रतिच्छेदन पर स्थित संख्यात्मक आंकड़े।
                <br>&bull; <strong>पाद-टिप्पणी (Footnotes):</strong> विशेष दिशा-निर्देश (उदा. '*' अनुमानित आंकड़ा दर्शाता है; कोष्ठक में प्रतिशत है)।</span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Typology of Statistical Tables</span>
                    <span class="lang-en"><strong>1. Simple (One-Way) Table:</strong> Supplies answers to questions about a single characteristic of data (e.g., Total population by state).
                    <br><strong>2. Two-Way Table:</strong> Interrelates two distinct characteristics (e.g., Population classified by State and Gender).
                    <br><strong>3. Complex / Manifold Table:</strong> Interrelates three or more characteristics simultaneously (e.g., Population classified by State, Gender, and Literacy status).</span>
                    <span class="lang-hi"><strong>सांख्यिकीय तालिकाओं के प्रकार:</strong>
                    <br><strong>1. सरल (एक-पक्षीय) तालिका:</strong> केवल एक विशेषता का विवरण देती है (उदा. राज्यवार कुल जनसंख्या)।
                    <br><strong>2. द्वि-पक्षीय तालिका:</strong> दो विशेषताओं का परस्पर संबंध दर्शाती है (उदा. राज्यवार तथा लिंगवार जनसंख्या)।
                    <br><strong>3. जटिल / बहु-पक्षीय तालिका:</strong> तीन या अधिक विशेषताओं को एक साथ प्रदर्शित करती है (उदा. राज्यवार, लिंगवार तथा साक्षरता-वार जनसंख्या)।</span>
                </li>
            </ul>
        </section>

        <!-- Section 2: Missing Data Tabulation (The #1 UPSSSC Exam Pattern) -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-puzzle-piece"></i>
                <span class="lang-en">2. Missing Data Tabulation: Mathematical Reconstruction</span>
                <span class="lang-hi">2. लुप्त आंकड़ा सारणीयन (Missing Data): गणितीय पुनर्निर्माण</span>
            </h2>
            <p>
                <span class="lang-en">Missing data tables are the most challenging format in UPSSSC exams. In these tables, certain cells are left blank, and candidates must reconstruct them using row/column totals, given ratios, or percentages.</span>
                <span class="lang-hi">लुप्त आंकड़ा तालिकाएं यूपीएसएसएससी में सर्वाधिक अंकदायी व चुनौतीपूर्ण प्रारूप हैं। इनमें कुछ कक्ष खाली छोड़ दिए जाते हैं, जिन्हें पंक्ति/स्तंभ योग, दिए गए अनुपातों अथवा प्रतिशतों की सहायता से हल करना होता है।</span>
            </p>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Branch (शाखा)</span><span class="lang-hi">शाखा</span></th>
                            <th><span class="lang-en">Clerks (लिपिक)</span><span class="lang-hi">लिपिक</span></th>
                            <th><span class="lang-en">Officers (अधिकारी)</span><span class="lang-hi">अधिकारी</span></th>
                            <th><span class="lang-en">Ratio (Clerk : Officer)</span><span class="lang-hi">अनुपात (लिपिक : अधिकारी)</span></th>
                            <th><span class="lang-en">Total Staff (कुल कर्मचारी)</span><span class="lang-hi">कुल कर्मचारी</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Lucknow</strong></td>
                            <td>120</td>
                            <td><strong>[A]</strong></td>
                            <td>3 : 1</td>
                            <td><strong>[B]</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Kanpur</strong></td>
                            <td><strong>[C]</strong></td>
                            <td>35</td>
                            <td>4 : 1</td>
                            <td><strong>[D]</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Varanasi</strong></td>
                            <td>90</td>
                            <td>30</td>
                            <td><strong>[E]</strong></td>
                            <td>120</td>
                        </tr>
                        <tr>
                            <td><strong>Agra</strong></td>
                            <td><strong>[F]</strong></td>
                            <td>40</td>
                            <td>5 : 2</td>
                            <td>140</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="exam-pointer" style="background:var(--planner-bg-surface);border-left:4px solid var(--planner-primary);">
                <h4><span class="lang-en">Mathematical Solution for Missing Values:</span><span class="lang-hi">लुप्त मानों का चरणबद्ध गणितीय समाधान:</span></h4>
                <ul style="line-height:1.75;margin-left:20px;">
                    <li><strong>Cell [A] (Lucknow Officers):</strong> Ratio is 3 : 1. Clerks = 120 (3 parts). 1 part = 120 / 3 = <strong>40</strong> officers.</li>
                    <li><strong>Cell [B] (Lucknow Total):</strong> Total = Clerks (120) + Officers (40) = <strong>160</strong>.</li>
                    <li><strong>Cell [C] (Kanpur Clerks):</strong> Ratio is 4 : 1. Officers = 35 (1 part). Clerks = 4 &times; 35 = <strong>140</strong>.</li>
                    <li><strong>Cell [D] (Kanpur Total):</strong> Total = 140 + 35 = <strong>175</strong>.</li>
                    <li><strong>Cell [E] (Varanasi Ratio):</strong> 90 / 30 = <strong>3 : 1</strong>.</li>
                    <li><strong>Cell [F] (Agra Clerks):</strong> Total = 140, Officers = 40. Clerks = 140 - 40 = <strong>100</strong> (Ratio 100 : 40 = 5 : 2 verified!).</li>
                </ul>
            </div>
        </section>

        <!-- Section 3: Multi-Subject Academic Examination Marks Table -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-graduation-cap"></i>
                <span class="lang-en">3. Multi-Variable Examination Scorecard Model</span>
                <span class="lang-hi">3. बहु-चर परीक्षा प्राप्तांक सारणी मॉडल</span>
            </h2>
            <p>
                <span class="lang-en">In this classic exam framework, maximum marks vary across subjects. Candidates must calculate aggregate scores without confusing raw marks with percentages!</span>
                <span class="lang-hi">इस मानक परीक्षा प्रारूप में प्रत्येक विषय के अधिकतम अंक भिन्न होते हैं। अभ्यर्थियों को बिना भ्रमित हुए कुल प्राप्तांक एवं प्रतिशत की गणना करनी होती है!</span>
            </p>

            <div class="table-container">
                <table class="fact-table">
                    <thead>
                        <tr>
                            <th><span class="lang-en">Candidate</span><span class="lang-hi">अभ्यर्थी</span></th>
                            <th><span class="lang-en">History (Max: 100)</span><span class="lang-hi">इतिहास (पूर्णांक: 100)</span></th>
                            <th><span class="lang-en">Math (Max: 150)</span><span class="lang-hi">गणित (पूर्णांक: 150)</span></th>
                            <th><span class="lang-en">Science (Max: 100)</span><span class="lang-hi">विज्ञान (पूर्णांक: 100)</span></th>
                            <th><span class="lang-en">Hindi (Max: 50)</span><span class="lang-hi">हिन्दी (पूर्णांक: 50)</span></th>
                            <th><span class="lang-en">Total (Max: 400)</span><span class="lang-hi">कुल (पूर्णांक: 400)</span></th>
                            <th><span class="lang-en">Aggregate %</span><span class="lang-hi">कुल प्रतिशत</span></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>Aman</strong></td>
                            <td>78</td>
                            <td>126</td>
                            <td>84</td>
                            <td>42</td>
                            <td><strong>330</strong></td>
                            <td><strong>82.50%</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Bhavna</strong></td>
                            <td>85</td>
                            <td>114</td>
                            <td>76</td>
                            <td>45</td>
                            <td><strong>320</strong></td>
                            <td><strong>80.00%</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Chetan</strong></td>
                            <td>64</td>
                            <td>135</td>
                            <td>90</td>
                            <td>36</td>
                            <td><strong>325</strong></td>
                            <td><strong>81.25%</strong></td>
                        </tr>
                        <tr>
                            <td><strong>Divya</strong></td>
                            <td>92</td>
                            <td>105</td>
                            <td>88</td>
                            <td>40</td>
                            <td><strong>325</strong></td>
                            <td><strong>81.25%</strong></td>
                        </tr>
                        <tr style="background:var(--planner-primary-light);font-weight:bold;">
                            <td><strong>Subject Average</strong></td>
                            <td><strong>79.75</strong></td>
                            <td><strong>120.00</strong></td>
                            <td><strong>84.50</strong></td>
                            <td><strong>40.75</strong></td>
                            <td><strong>325.00</strong></td>
                            <td><strong>81.25%</strong></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="exam-pointer">
                <span class="lang-en"><strong>Key Insights &amp; The Unequal Maximum Marks Fallacy:</strong>
                <br>&bull; <em>Highest percentage in Math:</em> Chetan scored 135/150 = 90.00%.
                <br>&bull; <em>Highest overall scorer:</em> Aman with 330/400 (82.50%).
                <br>&bull; <em>Subject with highest average percentage:</em> Hindi (Average 40.75/50 = 81.50%).
                <br>&bull; <em>The #1 UPSSSC Fallacy:</em> NEVER average the percentage scores of different subjects if maximum marks are unequal! E.g., if a candidate scores 80% in Maths (Max 150 &rarr; 120 marks) and 60% in Hindi (Max 50 &rarr; 30 marks), the true aggregate is <code>(150 / 200) &times; 100 = 75.00%</code>, NOT <code>(80 + 60)/2 = 70.00%</code>! Always sum raw marks first!</span>
                <span class="lang-hi"><strong>प्रमुख निष्कर्ष एवं असमान पूर्णांक का भ्रामक जाल:</strong>
                <br>&bull; <em>गणित में सर्वोच्च प्रतिशत:</em> चेतन ने 135/150 = 90.00% प्राप्त किए।
                <br>&bull; <em>समग्र टॉपर:</em> अमन कुल 330/400 (82.50%) के साथ।
                <br>&bull; <em>सर्वोच्च औसत प्रतिशत वाला विषय:</em> हिन्दी (औसत 40.75/50 = 81.50%)।
                <br>&bull; <em>यूपीएसएसएससी का सबसे बड़ा ट्रैप:</em> यदि विषयों के पूर्णांक अलग-अलग हों, तो कभी भी विषय प्रतिशतों का सीधा औसत न निकालें! उदा. गणित (पूर्णांक 150) में 80% (= 120) और हिन्दी (पूर्णांक 50) में 60% (= 30) पर सही कुल प्रतिशत <code>(150 / 200) &times; 100 = 75.00%</code> होगा, न कि <code>(80 + 60)/2 = 70.00%</code>! हमेशा पहले प्राप्तांकों का योग करें!</span>
            </div>
        </section>

        <!-- Section 4: Speed Calculation Shortcuts for Large Tables -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-tachometer-alt"></i>
                <span class="lang-en">4. Speed Arithmetic Shortcuts for Multi-Row Tables</span>
                <span class="lang-hi">4. बहु-पंक्ति तालिकाओं के लिए तीव्र अंकगणित शॉर्टकट</span>
            </h2>
            <ul class="point-list">
                <li>
                    <span class="key-badge">Column Summation Shortcut</span>
                    <span class="lang-en">When adding large columns of 5 or 6 numbers, add the tens digits first, then add the units digits.
                    <br>&bull; Example: Add 78 + 85 + 64 + 92:
                    <br>&bull; Tens: 70 + 80 + 60 + 90 = 300.
                    <br>&bull; Units: 8 + 5 + 4 + 2 = 19.
                    <br>&bull; Total = 300 + 19 = <strong>319</strong>. Faster by 3x!</span>
                    <span class="lang-hi">बड़े कॉलम का योग करते समय पहले दहाई के अंकों को जोड़ें, फिर इकाई के अंकों को।
                    <br>&bull; उदाहरण: 78 + 85 + 64 + 92 का योग:
                    <br>&bull; दहाई: 70 + 80 + 60 + 90 = 300।
                    <br>&bull; इकाई: 8 + 5 + 4 + 2 = 19।
                    <br>&bull; कुल योग = 319। यह 3 गुना तीव्र गति देता है!</span>
                </li>
                <li>
                    <span class="key-badge">Complementary Pairing to 100 &amp; 50</span>
                    <span class="lang-en">Scan table rows for pairs that add up to round numbers:
                    <br>&bull; <code>38 + 62 = 100</code>, <code>47 + 53 = 100</code>, <code>76 + 24 = 100</code>, <code>35 + 15 = 50</code>.
                    <br>Pairing complementary numbers reduces memory load and eliminates addition errors during timed exams.</span>
                    <span class="lang-hi">तालिका में ऐसे युग्म खोजें जो मिलकर 100 या 50 बनाते हों:
                    <br>&bull; <code>38 + 62 = 100</code>, <code>47 + 53 = 100</code>, <code>76 + 24 = 100</code>, <code>35 + 15 = 50</code>।
                    <br>पूरक संख्याओं के जोड़े बनाकर जोड़ने से परीक्षा के दबाव में गणना त्रुटियां शून्य हो जाती हैं।</span>
                </li>
                <li>
                    <span class="key-badge">Deviation Method for Fast Average</span>
                    <span class="lang-en">To find the average of 78, 85, 64, 92:
                    <br>&bull; Assume base = 80.
                    <br>&bull; Deviations: -2, +5, -16, +12.
                    <br>&bull; Net deviation = (-2 + 5 - 16 + 12) = -1.
                    <br>&bull; Average = 80 + (-1 / 4) = 80 - 0.25 = <strong>79.75</strong>! No big addition needed!</span>
                    <span class="lang-hi">78, 85, 64, 92 का औसत निकालने के लिए:
                    <br>&bull; कल्पित आधार = 80।
                    <br>&bull; विचलन: -2, +5, -16, +12।
                    <br>&bull; शुद्ध विचलन = -1।
                    <br>&bull; औसत = 80 + (-1 / 4) = 80 - 0.25 = <strong>79.75</strong>!</span>
                </li>
                <li>
                    <span class="key-badge">Cross-Multiplication for Table Fractions</span>
                    <span class="lang-en">To compare ratios across rows without dividing: To check if <code>135/160 > 114/135</code>, compare <code>135 &times; 135 = 18,225</code> with <code>160 &times; 114 = 18,240</code>. Since <code>18,225 < 18,240</code>, <code>114/135 > 135/160</code>.</span>
                    <span class="lang-hi">बिना भाग दिए अनुपातों की तुलना: <code>135/160</code> और <code>114/135</code> की तुलना के लिए <code>135 &times; 135 = 18,225</code> और <code>160 &times; 114 = 18,240</code> देखें। चूंकि 18,240 बड़ा है, अतः <code>114/135</code> बड़ा है।</span>
                </li>
            </ul>
        </section>

        <!-- Section 5: Commercial & Demographic Tabulation Models -->
        <section class="notes-section">
            <h2>
                <i class="fas fa-file-invoice-dollar"></i>
                <span class="lang-en">5. Commercial &amp; Demographic Tabulation Models</span>
                <span class="lang-hi">5. वाणिज्यिक एवं जनसांख्यिकीय सारणीयन मॉडल</span>
            </h2>
            <div class="exam-pointer">
                <span class="lang-en"><strong>Core Financial Concepts in Commercial Tables:</strong>
                <br>&bull; <code>Gross Profit = Turnover (Revenue) - Cost of Goods Sold</code>
                <br>&bull; <code>Operating Profit = Gross Profit - Operating Expenses</code>
                <br>&bull; <code>Net Profit = Operating Profit - Tax &amp; Interest</code>
                <br>&bull; <code>Profit Margin % = (Net Profit / Turnover) &times; 100</code></span>
                <span class="lang-hi"><strong>वाणिज्यिक तालिकाओं में प्रमुख वित्तीय सूत्र:</strong>
                <br>&bull; <code>सकल लाभ = कुल राजस्व (Turnover) - बेची गई वस्तुओं की लागत</code>
                <br>&bull; <code>परिचालन लाभ = सकल लाभ - परिचालन व्यय</code>
                <br>&bull; <code>शुद्ध लाभ = परिचालन लाभ - कर एवं ब्याज</code>
                <br>&bull; <code>लाभ मार्जिन % = (शुद्ध लाभ / कुल टर्नओवर) &times; 100</code></span>
            </div>

            <ul class="point-list">
                <li>
                    <span class="key-badge">Demographic &amp; Census Tabulation</span>
                    <span class="lang-en">In Census DI tables:
                    <br>&bull; <strong>Sex Ratio:</strong> Number of females per 1,000 males = <code>(Females / Males) &times; 1,000</code>.
                    <br>&bull; <strong>Literacy Rate:</strong> <code>(Literates / Total Population aged 7+) &times; 100</code>.
                    <br>&bull; <strong>Urbanization Rate:</strong> <code>(Urban Population / Total Population) &times; 100</code>.</span>
                    <span class="lang-hi">जनगणना आधारित डीआई तालिकाओं में:
                    <br>&bull; <strong>लिंगानुपात (Sex Ratio):</strong> प्रति 1,000 पुरुषों पर महिलाओं की संख्या = <code>(महिलाएं / पुरुष) &times; 1,000</code>।
                    <br>&bull; <strong>साक्षरता दर:</strong> <code>(साक्षर व्यक्ति / 7 वर्ष से अधिक कुल जनसंख्या) &times; 100</code>।
                    <br>&bull; <strong>शहरीकरण दर:</strong> <code>(शहरी जनसंख्या / कुल जनसंख्या) &times; 100</code>।</span>
                </li>
            </ul>
        </section>
    """,

    # 30 Curated Practice Questions
    "practiceQuestions": [
        {
            "tag": "Missing Table Value",
            "qEn": "In the Missing Data Table in Section 2, what is the number of Officers in the Lucknow branch (Cell [A])?",
            "qHi": "खंड 2 की लुप्त आंकड़ा तालिका में, लखनऊ शाखा में अधिकारियों की संख्या (कक्ष [A]) क्या है?",
            "opts": [
                ("A", "35", "35"),
                ("B", "40", "40"),
                ("C", "45", "45"),
                ("D", "50", "50")
            ],
            "ans": "B",
            "solEn": "Clerks = 120 and ratio of Clerk : Officer = 3 : 1. Officers = 120 / 3 = 40.",
            "solHi": "लिपिक = 120 और अनुपात = 3 : 1। अधिकारी = 120 / 3 = 40।"
        },
        {
            "tag": "Missing Table Value",
            "qEn": "In the same table, what is the number of Clerks in the Kanpur branch (Cell [C])?",
            "qHi": "उसी तालिका में, कानपुर शाखा में लिपिकों की संख्या (कक्ष [C]) क्या है?",
            "opts": [
                ("A", "130", "130"),
                ("B", "140", "140"),
                ("C", "150", "150"),
                ("D", "120", "120")
            ],
            "ans": "B",
            "solEn": "Officers = 35 and ratio of Clerk : Officer = 4 : 1. Clerks = 4 &times; 35 = 140.",
            "solHi": "अधिकारी = 35 और अनुपात = 4 : 1। लिपिक = 4 &times; 35 = 140।"
        },
        {
            "tag": "Scorecard - Aggregate",
            "qEn": "In the Multi-Variable Scorecard table, who secured the highest aggregate percentage across all 4 subjects?",
            "qHi": "बहु-चर प्राप्तांक तालिका में, चारों विषयों में मिलाकर किसने सर्वोच्च कुल प्रतिशत प्राप्त किया?",
            "opts": [
                ("A", "Aman (82.50%)", "अमन (82.50%)"),
                ("B", "Bhavna (80.00%)", "भावना (80.00%)"),
                ("C", "Chetan (81.25%)", "चेतन (81.25%)"),
                ("D", "Divya (81.25%)", "दिव्या (81.25%)")
            ],
            "ans": "A",
            "solEn": "Aman scored 330 out of 400 = (330 / 400) &times; 100 = 82.50% (Highest).",
            "solHi": "अमन ने 400 में से 330 अंक प्राप्त किए = 82.50% (सर्वोच्च)।"
        },
        {
            "tag": "Scorecard - Subject %",
            "qEn": "What percentage of maximum marks did Chetan score in Mathematics (Max: 150, Score: 135)?",
            "qHi": "चेतन ने गणित में पूर्णांक (150) का कितना प्रतिशत अंक प्राप्त किया (प्राप्तांक: 135)?",
            "opts": [
                ("A", "85.0%", "85.0%"),
                ("B", "88.0%", "88.0%"),
                ("C", "90.0%", "90.0%"),
                ("D", "92.5%", "92.5%")
            ],
            "ans": "C",
            "solEn": "Percentage = (135 / 150) &times; 100 = (9 / 10) &times; 100 = 90.0%.",
            "solHi": "प्रतिशत = (135 / 150) &times; 100 = 90.0%।"
        },
        {
            "tag": "Missing Table Total",
            "qEn": "In Section 2, what is the total number of staff in the Kanpur branch (Cell [D])?",
            "qHi": "खंड 2 में, कानपुर शाखा में कुल कर्मचारियों की संख्या (कक्ष [D]) क्या है?",
            "opts": [
                ("A", "165", "165"),
                ("B", "175", "175"),
                ("C", "180", "180"),
                ("D", "170", "170")
            ],
            "ans": "B",
            "solEn": "Total = Clerks (140) + Officers (35) = 175.",
            "solHi": "कुल = लिपिक (140) + अधिकारी (35) = 175।"
        },
        {
            "tag": "Table Average",
            "qEn": "What is the average marks scored by the 4 candidates in Science (Max: 100)?",
            "qHi": "विज्ञान विषय (पूर्णांक: 100) में 4 अभ्यर्थियों का औसत प्राप्तांक क्या है?",
            "opts": [
                ("A", "84.50", "84.50"),
                ("B", "82.00", "82.00"),
                ("C", "85.00", "85.00"),
                ("D", "83.50", "83.50")
            ],
            "ans": "A",
            "solEn": "Sum = 84 + 76 + 90 + 88 = 338. Average = 338 / 4 = 84.50.",
            "solHi": "योग = 84 + 76 + 90 + 88 = 338। औसत = 338 / 4 = 84.50।"
        },
        {
            "tag": "Scorecard Ratio",
            "qEn": "What is the ratio of marks scored by Aman in History to marks scored by Divya in History?",
            "qHi": "अमन द्वारा इतिहास में प्राप्त अंकों का दिव्या द्वारा इतिहास में प्राप्त अंकों से क्या अनुपात है?",
            "opts": [
                ("A", "39 : 46", "39 : 46"),
                ("B", "78 : 92", "78 : 92"),
                ("C", "39 : 46", "39 : 46"),
                ("D", "41 : 46", "41 : 46")
            ],
            "ans": "A",
            "solEn": "Aman History = 78; Divya History = 92. Ratio = 78 / 92 = 39 / 46.",
            "solHi": "अमन = 78; दिव्या = 92। अनुपात = 78 / 92 = 39 : 46।"
        },
        {
            "tag": "Missing Table Ratio",
            "qEn": "In Section 2, what is the ratio of Clerks to Officers in the Varanasi branch (Cell [E])?",
            "qHi": "खंड 2 में, वाराणसी शाखा में लिपिकों का अधिकारियों से अनुपात (कक्ष [E]) क्या है?",
            "opts": [
                ("A", "3 : 1", "3 : 1"),
                ("B", "4 : 1", "4 : 1"),
                ("C", "2 : 1", "2 : 1"),
                ("D", "5 : 2", "5 : 2")
            ],
            "ans": "A",
            "solEn": "Clerks = 90; Officers = 30. Ratio = 90 / 30 = 3 : 1.",
            "solHi": "लिपिक = 90; अधिकारी = 30। अनुपात = 90 / 30 = 3 : 1।"
        },
        {
            "tag": "Table Difference",
            "qEn": "By how many marks does Chetan's score in Math exceed Bhavna's score in Math?",
            "qHi": "गणित में चेतन का प्राप्तांक भावना के प्राप्तांक से कितने अंक अधिक है?",
            "opts": [
                ("A", "19", "19"),
                ("B", "21", "21"),
                ("C", "23", "23"),
                ("D", "25", "25")
            ],
            "ans": "B",
            "solEn": "Chetan Math = 135; Bhavna Math = 114. Difference = 135 - 114 = 21 marks.",
            "solHi": "चेतन = 135; भावना = 114। अंतर = 135 - 114 = 21 अंक।"
        },
        {
            "tag": "Table Component",
            "qEn": "In statistical tabulation, what is the term used for the row headings on the extreme left of the table?",
            "qHi": "सांख्यिकीय सारणीयन में, तालिका के बाईं ओर स्थित पंक्ति शीर्षकों के लिए किस शब्द का प्रयोग किया जाता है?",
            "opts": [
                ("A", "Caption", "कैप्शन (Caption)"),
                ("B", "Stub", "स्टब (Stub)"),
                ("C", "Body", "बॉडी (Body)"),
                ("D", "Footnote", "पाद-टिप्पणी")
            ],
            "ans": "B",
            "solEn": "The row labels in the extreme left column of a table are formally termed the 'Stub'. Column headers are the 'Caption'.",
            "solHi": "तालिका में बाईं ओर की पंक्तियों के शीर्षकों को 'स्टब (Stub)' कहा जाता है। स्तंभों के शीर्षकों को 'कैप्शन' कहते हैं।"
        },
        {
            "tag": "Missing Table Value",
            "qEn": "In the Agra branch (Section 2), if Total Staff is 140 and Officers are 40, how many Clerks are there (Cell [F])?",
            "qHi": "आगरा शाखा (खंड 2) में, यदि कुल कर्मचारी 140 हैं और अधिकारी 40 हैं, तो लिपिकों की संख्या (कक्ष [F]) कितनी है?",
            "opts": [
                ("A", "90", "90"),
                ("B", "100", "100"),
                ("C", "110", "110"),
                ("D", "95", "95")
            ],
            "ans": "B",
            "solEn": "Clerks = Total Staff (140) - Officers (40) = 100.",
            "solHi": "लिपिक = 140 - 40 = 100।"
        },
        {
            "tag": "Percentage More",
            "qEn": "Aman's score in Science (84) was what percent more than Bhavna's score in Science (76)?",
            "qHi": "विज्ञान में अमन का प्राप्तांक (84) भावना के प्राप्तांक (76) से कितने प्रतिशत अधिक था?",
            "opts": [
                ("A", "10.53%", "10.53%"),
                ("B", "9.52%", "9.52%"),
                ("C", "11.11%", "11.11%"),
                ("D", "8.00%", "8.00%")
            ],
            "ans": "A",
            "solEn": "Difference = 84 - 76 = 8. Base is Bhavna (76). Percentage more = (8 / 76) &times; 100 = (2 / 19) &times; 100 &approx; 10.53%.",
            "solHi": "अंतर = 84 - 76 = 8। आधार = 76। प्रतिशत अधिक = (8 / 76) &times; 100 &approx; 10.53%।"
        },
        {
            "tag": "Subject Total",
            "qEn": "What is the total marks scored by all 4 candidates in Hindi (Max: 50)?",
            "qHi": "हिन्दी (पूर्णांक: 50) में चारों अभ्यर्थियों द्वारा प्राप्त कुल अंक कितने हैं?",
            "opts": [
                ("A", "163", "163"),
                ("B", "160", "160"),
                ("C", "165", "165"),
                ("D", "158", "158")
            ],
            "ans": "A",
            "solEn": "Sum = 42 + 45 + 36 + 40 = 163 marks.",
            "solHi": "कुल योग = 42 + 45 + 36 + 40 = 163 अंक।"
        },
        {
            "tag": "Table Reading",
            "qEn": "Which candidate scored the highest marks in History?",
            "qHi": "इतिहास में किस अभ्यर्थी ने सर्वाधिक अंक प्राप्त किए?",
            "opts": [
                ("A", "Divya (92)", "दिव्या (92)"),
                ("B", "Bhavna (85)", "भावना (85)"),
                ("C", "Aman (78)", "अमन (78)"),
                ("D", "Chetan (64)", "चेतन (64)")
            ],
            "ans": "A",
            "solEn": "Divya scored 92 marks out of 100 in History, which is the highest in the subject.",
            "solHi": "दिव्या ने इतिहास में 92 अंक प्राप्त किए जो सर्वाधिक हैं।"
        },
        {
            "tag": "Weighted Total Check",
            "qEn": "Why is it incorrect to simply average the four raw subject marks (78+126+84+42)/4 to find Aman's aggregate percentage?",
            "qHi": "अमन का कुल प्रतिशत निकालने के लिए चारों विषयों के अंकों के औसत (78+126+84+42)/4 को लेना गलत क्यों है?",
            "opts": [
                ("A", "Because maximum marks for Math is 150 and Hindi is 50, not all 100", "क्योंकि गणित का पूर्णांक 150 और हिन्दी का 50 है, सभी 100 नहीं हैं"),
                ("B", "Because of negative marking", "नकारात्मक अंकन के कारण"),
                ("C", "Because raw marks cannot be added", "क्योंकि कच्चे अंकों को जोड़ा नहीं जा सकता"),
                ("D", "Because average is always an integer", "क्योंकि औसत सदैव पूर्णांक होता है")
            ],
            "ans": "A",
            "solEn": "Subjects have unequal weights (Math is out of 150, Hindi out of 50). Percentage must be calculated against the combined total maximum marks (400), not simple average of marks.",
            "solHi": "पूर्णांक असमान हैं (गणित 150, हिन्दी 50)। कुल प्रतिशत कुल पूर्णांक (400) के सापेक्ष निकाला जाना चाहिए।"
        },
        {
            "tag": "Total Staff Sum",
            "qEn": "Across all 4 branches in Section 2, what is the total number of Officers (40 + 35 + 30 + 40)?",
            "qHi": "खंड 2 की चारों शाखाओं में मिलाकर अधिकारियों की कुल संख्या कितनी है?",
            "opts": [
                ("A", "145", "145"),
                ("B", "150", "150"),
                ("C", "140", "140"),
                ("D", "155", "155")
            ],
            "ans": "A",
            "solEn": "Total Officers = 40 (Lucknow) + 35 (Kanpur) + 30 (Varanasi) + 40 (Agra) = 145.",
            "solHi": "कुल अधिकारी = 40 + 35 + 30 + 40 = 145।"
        },
        {
            "tag": "Total Clerks Sum",
            "qEn": "Across all 4 branches in Section 2, what is the total number of Clerks (120 + 140 + 90 + 100)?",
            "qHi": "खंड 2 की चारों शाखाओं में मिलाकर लिपिकों की कुल संख्या कितनी है?",
            "opts": [
                ("A", "450", "450"),
                ("B", "460", "460"),
                ("C", "440", "440"),
                ("D", "470", "470")
            ],
            "ans": "A",
            "solEn": "Total Clerks = 120 + 140 + 90 + 100 = 450.",
            "solHi": "कुल लिपिक = 120 + 140 + 90 + 100 = 450।"
        },
        {
            "tag": "Grand Total Ratio",
            "qEn": "What is the overall ratio of Clerks to Officers across all 4 branches combined?",
            "qHi": "चारों शाखाओं को मिलाकर लिपिकों का अधिकारियों से समग्र अनुपात क्या है?",
            "opts": [
                ("A", "90 : 29", "90 : 29"),
                ("B", "450 : 145", "450 : 145"),
                ("C", "90 : 29", "90 : 29"),
                ("D", "3 : 1", "3 : 1")
            ],
            "ans": "A",
            "solEn": "Total Clerks = 450; Total Officers = 145. Ratio = 450 / 145 = 90 / 29.",
            "solHi": "कुल लिपिक = 450; कुल अधिकारी = 145। अनुपात = 450 / 145 = 90 : 29।"
        },
        {
            "tag": "Table Average",
            "qEn": "What is the average marks scored in History across all 4 candidates?",
            "qHi": "इतिहास में सभी 4 अभ्यर्थियों का औसत प्राप्तांक क्या है?",
            "opts": [
                ("A", "79.75", "79.75"),
                ("B", "80.50", "80.50"),
                ("C", "78.25", "78.25"),
                ("D", "81.00", "81.00")
            ],
            "ans": "A",
            "solEn": "Sum = 78 + 85 + 64 + 92 = 319. Average = 319 / 4 = 79.75.",
            "solHi": "योग = 319। औसत = 319 / 4 = 79.75।"
        },
        {
            "tag": "Candidate Comparison",
            "qEn": "Who scored the lowest aggregate marks across all subjects?",
            "qHi": "सभी विषयों में मिलाकर सबसे कम कुल अंक किसने प्राप्त किए?",
            "opts": [
                ("A", "Bhavna (320)", "भावना (320)"),
                ("B", "Aman (330)", "अमन (330)"),
                ("C", "Chetan (325)", "चेतन (325)"),
                ("D", "Divya (325)", "दिव्या (325)")
            ],
            "ans": "A",
            "solEn": "Bhavna scored 320 out of 400, which is the lowest total in the group.",
            "solHi": "भावना ने 320 अंक प्राप्त किए जो समूह में सबसे कम है।"
        },
        {
            "tag": "Scorecard Percentage",
            "qEn": "What percentage of the maximum marks (50) did Bhavna score in Hindi (45 marks)?",
            "qHi": "भावना ने हिन्दी के पूर्णांक (50) का कितना प्रतिशत (प्राप्तांक 45) प्राप्त किया?",
            "opts": [
                ("A", "90%", "90%"),
                ("B", "85%", "85%"),
                ("C", "92%", "92%"),
                ("D", "88%", "88%")
            ],
            "ans": "A",
            "solEn": "Percentage = (45 / 50) &times; 100 = 90%.",
            "solHi": "प्रतिशत = (45 / 50) &times; 100 = 90%।"
        },
        {
            "tag": "Branch Largest",
            "qEn": "Which branch has the largest total staff (Lucknow: 160, Kanpur: 175, Varanasi: 120, Agra: 140)?",
            "qHi": "किस शाखा में कर्मचारियों की कुल संख्या सर्वाधिक है?",
            "opts": [
                ("A", "Kanpur (175)", "कानपुर (175)"),
                ("B", "Lucknow (160)", "लखनऊ (160)"),
                ("C", "Agra (140)", "आगरा (140)"),
                ("D", "Varanasi (120)", "वाराणसी (120)")
            ],
            "ans": "A",
            "solEn": "Kanpur branch has 175 staff (140 clerks + 35 officers), which is the highest.",
            "solHi": "कानपुर शाखा में 175 कर्मचारी हैं जो सर्वाधिक हैं।"
        },
        {
            "tag": "Subject Top Score",
            "qEn": "In which subject did Chetan score the lowest percentage relative to the subject's maximum marks?",
            "qHi": "चेतन ने किस विषय के पूर्णांक के सापेक्ष सबसे कम प्रतिशत अंक प्राप्त किए?",
            "opts": [
                ("A", "History (64%)", "इतिहास (64%)"),
                ("B", "Math (90%)", "गणित (90%)"),
                ("C", "Science (90%)", "विज्ञान (90%)"),
                ("D", "Hindi (72%)", "हिन्दी (72%)")
            ],
            "ans": "A",
            "solEn": "History % = 64/100 = 64%. Math = 135/150 = 90%. Science = 90/100 = 90%. Hindi = 36/50 = 72%. Lowest is History (64%).",
            "solHi": "इतिहास में 64%, गणित में 90%, विज्ञान में 90%, हिन्दी में 72%। न्यूनतम इतिहास (64%) में है।"
        },
        {
            "tag": "Branch Officer %",
            "qEn": "In the Agra branch, what percentage of total staff are Officers?",
            "qHi": "आगरा शाखा में कुल कर्मचारियों का कितना प्रतिशत अधिकारी हैं?",
            "opts": [
                ("A", "28.57%", "28.57%"),
                ("B", "25.00%", "25.00%"),
                ("C", "30.00%", "30.00%"),
                ("D", "33.33%", "33.33%")
            ],
            "ans": "A",
            "solEn": "Officers = 40; Total = 140. Percentage = (40 / 140) &times; 100 = 2/7 &times; 100 = 28.57%.",
            "solHi": "अधिकारी = 40; कुल = 140। प्रतिशत = (40 / 140) &times; 100 = 2/7 &times; 100 = 28.57%।"
        },
        {
            "tag": "Table Reading",
            "qEn": "What is the difference between Divya's score in History (92) and Chetan's score in History (64)?",
            "qHi": "दिव्या के इतिहास प्राप्तांक (92) और चेतन के इतिहास प्राप्तांक (64) में क्या अंतर है?",
            "opts": [
                ("A", "28 marks", "28 अंक"),
                ("B", "26 marks", "26 अंक"),
                ("C", "30 marks", "30 अंक"),
                ("D", "24 marks", "24 अंक")
            ],
            "ans": "A",
            "solEn": "92 - 64 = 28 marks.",
            "solHi": "92 - 64 = 28 अंक।"
        },
        {
            "tag": "Math Average",
            "qEn": "What is the average marks scored in Math across all 4 candidates?",
            "qHi": "गणित में सभी 4 अभ्यर्थियों का औसत प्राप्तांक क्या है?",
            "opts": [
                ("A", "120.00", "120.00"),
                ("B", "118.50", "118.50"),
                ("C", "122.00", "122.00"),
                ("D", "125.00", "125.00")
            ],
            "ans": "A",
            "solEn": "Sum = 126 + 114 + 135 + 105 = 480. Average = 480 / 4 = 120.00.",
            "solHi": "योग = 480। औसत = 480 / 4 = 120.00।"
        },
        {
            "tag": "Table Caption",
            "qEn": "In a statistical table, what is the 'Caption'?",
            "qHi": "सांख्यिकीय तालिका में 'कैप्शन' (Caption) क्या होता है?",
            "opts": [
                ("A", "Column headings", "स्तंभों के शीर्षक (Column headings)"),
                ("B", "Row headings", "पंक्तियों के शीर्षक"),
                ("C", "Source of data", "आंकड़ों का स्रोत"),
                ("D", "Total cell", "कुल योग का कक्ष")
            ],
            "ans": "A",
            "solEn": "The headings given to vertical columns are designated as 'Caption'. Row headings are 'Stub'.",
            "solHi": "ऊर्ध्वाधर स्तंभों के शीर्षकों को 'कैप्शन' कहा जाता है।"
        },
        {
            "tag": "Aggregate Equality",
            "qEn": "Which two candidates secured exactly identical aggregate marks in the Scorecard table?",
            "qHi": "प्राप्तांक तालिका में किन दो अभ्यर्थियों ने ठीक एक समान कुल अंक प्राप्त किए?",
            "opts": [
                ("A", "Chetan and Divya (325 marks each)", "चेतन और दिव्या (प्रत्येक 325 अंक)"),
                ("B", "Aman and Bhavna", "अमन और भावना"),
                ("C", "Aman and Chetan", "अमन और चेतन"),
                ("D", "Bhavna and Divya", "भावना और दिव्या")
            ],
            "ans": "A",
            "solEn": "Both Chetan and Divya scored exactly 325 marks out of 400 (81.25%).",
            "solHi": "चेतन और दिव्या दोनों ने 400 में से ठीक 325 अंक (81.25%) प्राप्त किए।"
        },
        {
            "tag": "Branch Smallest",
            "qEn": "Which branch has the smallest total staff?",
            "qHi": "किस शाखा में कर्मचारियों की कुल संख्या न्यूनतम है?",
            "opts": [
                ("A", "Varanasi (120)", "वाराणसी (120)"),
                ("B", "Agra (140)", "आगरा (140)"),
                ("C", "Lucknow (160)", "लखनऊ (160)"),
                ("D", "Kanpur (175)", "कानपुर (175)")
            ],
            "ans": "A",
            "solEn": "Varanasi has 120 staff (90 clerks + 30 officers), which is the lowest.",
            "solHi": "वाराणसी में 120 कर्मचारी हैं जो सबसे कम हैं।"
        },
        {
            "tag": "Overall Percentage",
            "qEn": "What is the grand average percentage across all 4 candidates?",
            "qHi": "चारों अभ्यर्थियों का समग्र औसत प्रतिशत क्या है?",
            "opts": [
                ("A", "81.25%", "81.25%"),
                ("B", "80.50%", "80.50%"),
                ("C", "82.00%", "82.00%"),
                ("D", "81.75%", "81.75%")
            ],
            "ans": "A",
            "solEn": "Average total score = 325 / 400 = (325 / 4) / 100 = 81.25%.",
            "solHi": "औसत कुल प्राप्तांक = 325/400 = 81.25%।"
        }
    ],

    # 15 Mini-Test MCQs
    "testQuestions": [
        {
            "qEn": "In statistical tables, row designations on the extreme left are called:",
            "qHi": "सांख्यिकीय तालिकाओं में सबसे बाईं ओर पंक्ति शीर्षकों को क्या कहा जाता है?",
            "opts": [
                ("A", "Stub", "स्टब (Stub)"),
                ("B", "Caption", "कैप्शन (Caption)"),
                ("C", "Footnote", "पाद-टिप्पणी"),
                ("D", "Headnote", "हेडनोट")
            ]
        },
        {
            "qEn": "In the Section 2 Missing Table, what was the total staff in Lucknow (Cell [B])?",
            "qHi": "खंड 2 की लुप्त तालिका में, लखनऊ में कुल कर्मचारी (कक्ष [B]) कितने थे?",
            "opts": [
                ("A", "160", "160"),
                ("B", "150", "150"),
                ("C", "170", "170"),
                ("D", "180", "180")
            ]
        },
        {
            "qEn": "In the Scorecard table, what is Aman's aggregate percentage (330/400)?",
            "qHi": "प्राप्तांक तालिका में अमन का कुल प्रतिशत (330/400) क्या है?",
            "opts": [
                ("A", "82.50%", "82.50%"),
                ("B", "80.00%", "80.00%"),
                ("C", "85.00%", "85.00%"),
                ("D", "81.25%", "81.25%")
            ]
        },
        {
            "qEn": "In Kanpur branch, what was the number of Clerks (Cell [C])?",
            "qHi": "कानपुर शाखा में लिपिकों की संख्या (कक्ष [C]) क्या थी?",
            "opts": [
                ("A", "140", "140"),
                ("B", "135", "135"),
                ("C", "145", "145"),
                ("D", "150", "150")
            ]
        },
        {
            "qEn": "In the Scorecard table, who scored the highest percentage in History?",
            "qHi": "प्राप्तांक तालिका में इतिहास में सर्वाधिक प्रतिशत अंक किसने प्राप्त किए?",
            "opts": [
                ("A", "Divya (92%)", "दिव्या (92%)"),
                ("B", "Bhavna (85%)", "भावना (85%)"),
                ("C", "Aman (78%)", "अमन (78%)"),
                ("D", "Chetan (64%)", "चेतन (64%)")
            ]
        },
        {
            "qEn": "What is the ratio of Clerks to Officers in Varanasi branch (90 : 30)?",
            "qHi": "वाराणसी शाखा में लिपिकों का अधिकारियों से अनुपात (90 : 30) क्या है?",
            "opts": [
                ("A", "3 : 1", "3 : 1"),
                ("B", "4 : 1", "4 : 1"),
                ("C", "2 : 1", "2 : 1"),
                ("D", "5 : 2", "5 : 2")
            ]
        },
        {
            "qEn": "What is the maximum marks for Mathematics in the Scorecard table?",
            "qHi": "प्राप्तांक तालिका में गणित का पूर्णांक कितना है?",
            "opts": [
                ("A", "150", "150"),
                ("B", "100", "100"),
                ("C", "200", "200"),
                ("D", "125", "125")
            ]
        },
        {
            "qEn": "How many Clerks are there in Agra branch (Cell [F])?",
            "qHi": "आगरा शाखा में कितने लिपिक हैं (कक्ष [F])?",
            "opts": [
                ("A", "100", "100"),
                ("B", "90", "90"),
                ("C", "110", "110"),
                ("D", "105", "105")
            ]
        },
        {
            "qEn": "What is the average marks in Math across the 4 candidates?",
            "qHi": "चारों अभ्यर्थियों का गणित में औसत प्राप्तांक क्या है?",
            "opts": [
                ("A", "120.00", "120.00"),
                ("B", "115.00", "115.00"),
                ("C", "125.00", "125.00"),
                ("D", "118.00", "118.00")
            ]
        },
        {
            "qEn": "Which subject has maximum marks = 50 in the scorecard table?",
            "qHi": "प्राप्तांक तालिका में किस विषय का पूर्णांक 50 है?",
            "opts": [
                ("A", "Hindi", "हिन्दी"),
                ("B", "History", "इतिहास"),
                ("C", "Science", "विज्ञान"),
                ("D", "Math", "गणित")
            ]
        },
        {
            "qEn": "What was the total number of staff in Agra branch?",
            "qHi": "आगरा शाखा में कुल कर्मचारियों की संख्या कितनी थी?",
            "opts": [
                ("A", "140", "140"),
                ("B", "130", "130"),
                ("C", "150", "150"),
                ("D", "145", "145")
            ]
        },
        {
            "qEn": "What is Chetan's score in Science (Max: 100)?",
            "qHi": "विज्ञान (पूर्णांक: 100) में चेतन का प्राप्तांक कितना है?",
            "opts": [
                ("A", "90", "90"),
                ("B", "84", "84"),
                ("C", "76", "76"),
                ("D", "88", "88")
            ]
        },
        {
            "qEn": "What was the total number of staff in Kanpur branch?",
            "qHi": "कानपुर शाखा में कुल कर्मचारियों की संख्या कितनी थी?",
            "opts": [
                ("A", "175", "175"),
                ("B", "165", "165"),
                ("C", "170", "170"),
                ("D", "180", "180")
            ]
        },
        {
            "qEn": "What is the percentage scored by Aman in Hindi (42/50)?",
            "qHi": "अमन द्वारा हिन्दी में प्राप्त अंकों का प्रतिशत (42/50) क्या है?",
            "opts": [
                ("A", "84%", "84%"),
                ("B", "80%", "80%"),
                ("C", "85%", "85%"),
                ("D", "82%", "82%")
            ]
        },
        {
            "qEn": "Column headings in a statistical table are designated as:",
            "qHi": "सांख्यिकीय तालिका में स्तंभों के शीर्षकों को क्या कहा जाता है?",
            "opts": [
                ("A", "Caption", "कैप्शन (Caption)"),
                ("B", "Stub", "स्टब (Stub)"),
                ("C", "Prefatory note", "प्रारंभिक टिप्पणी"),
                ("D", "Footnote", "पाद-टिप्पणी")
            ]
        }
    ],

    "testDataJson": json.dumps([
        {"ans": "A", "solEn": "The row labels in the extreme left column are called Stub.", "solHi": "बाईं ओर की पंक्तियों के शीर्षकों को स्टब (Stub) कहा जाता है।"},
        {"ans": "A", "solEn": "Total = Clerks (120) + Officers (40) = 160.", "solHi": "कुल = 120 + 40 = 160।"},
        {"ans": "A", "solEn": "(330 / 400) &times; 100 = 82.50%.", "solHi": "(330 / 400) &times; 100 = 82.50%।"},
        {"ans": "A", "solEn": "4 &times; 35 = 140.", "solHi": "4 &times; 35 = 140।"},
        {"ans": "A", "solEn": "Divya scored 92/100 = 92% in History.", "solHi": "दिव्या ने इतिहास में 92% अंक प्राप्त किए।"},
        {"ans": "A", "solEn": "90 / 30 = 3 : 1.", "solHi": "90 / 30 = 3 : 1।"},
        {"ans": "A", "solEn": "Maximum marks for Math = 150.", "solHi": "गणित का पूर्णांक 150 है।"},
        {"ans": "A", "solEn": "140 - 40 = 100 clerks.", "solHi": "140 - 40 = 100 लिपिक।"},
        {"ans": "A", "solEn": "480 / 4 = 120.00.", "solHi": "480 / 4 = 120.00।"},
        {"ans": "A", "solEn": "Hindi has maximum marks = 50.", "solHi": "हिन्दी का पूर्णांक 50 है।"},
        {"ans": "A", "solEn": "Agra total staff = 140.", "solHi": "आगरा में कुल कर्मचारी = 140।"},
        {"ans": "A", "solEn": "Chetan scored 90 marks in Science.", "solHi": "चेतन ने विज्ञान में 90 अंक प्राप्त किए।"},
        {"ans": "A", "solEn": "140 + 35 = 175.", "solHi": "140 + 35 = 175।"},
        {"ans": "A", "solEn": "(42 / 50) &times; 100 = 84%.", "solHi": "(42 / 50) &times; 100 = 84%।"},
        {"ans": "A", "solEn": "Column headings are designated as Caption.", "solHi": "स्तंभों के शीर्षकों को कैप्शन (Caption) कहा जाता है।"}
    ])
}
