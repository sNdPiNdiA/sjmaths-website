# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "census-2011-highlights"
TOPIC_DISPLAY = "Census 2011 Highlights"
TOPIC_DISPLAY_HI = "जनगणना 2011 मुख्य बिंदु"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\population-ecology-urbanisation\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "Population, Ecology & Urbanisation",
    "parentUrl": "../",
    "current": "Census 2011 Highlights"
}

hero_en = {
    "title": "Census 2011 Highlights",
    "description": "Comprehensive analysis of India's 15th National Census (2011), detailing national and UP-specific population size, growth, density, literacy, sex ratio, and SC/ST demographics."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Census 2011 Mock Test",
        "description": "Evaluate your understanding of state-wise literacy rates, density rankings, UP-specific district facts, and historical census milestones. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Evolution of Census in India",
    "description": "Milestones in the history of population enumeration in India.",
    "cards": [
        {
            "period": "First Census",
            "date": "1872",
            "details": "First non-synchronous population census conducted under the Viceroyalty of Lord Mayo."
        },
        {
            "period": "First Synchronous Census",
            "date": "1881",
            "details": "First synchronous, decadal census conducted under Lord Ripon. Since then, it is held every ten years."
        },
        {
            "period": "The Great Divide",
            "date": "1921",
            "details": "The only census year showing a negative population growth rate (-0.31%) due to influenza epidemic and famine."
        },
        {
            "period": "First Post-Independence Census",
            "date": "1951",
            "details": "Conducted under the Census Act of 1948. India's population stood at 36.1 crores."
        },
        {
            "period": "15th Census of India",
            "date": "2011",
            "details": "Conducted with the motto 'Our Census, Our Future' under C. Chandramouli as Census Commissioner."
        }
    ]
}

mnemonics_en = {
    "title": "Census 2011 Mnemonics",
    "description": "Memory hooks to quickly recall state and district-wise rankings.",
    "items": [
        {
            "title": "Mnemonic 1: Top 3 Most Populous States",
            "phrase": "\"U-M-B (Up Man Bow)\"",
            "decryption": "Recalls the order of states by highest population:<br>1. **U** — Uttar Pradesh (19.98 crores)<br>2. **M** — Maharashtra (11.23 crores)<br>3. **B** — Bihar (10.40 crores)"
        },
        {
            "title": "Mnemonic 2: Top 3 States with Highest Population Density",
            "phrase": "\"B-W-K (Big Water Kettle)\"",
            "decryption": "Recalls the order of states by density:<br>• **B** — Bihar (1106 persons/sq km)<br>• **W** — West Bengal (1028 persons/sq km)<br>• **K** — Kerala (860 persons/sq km)"
        },
        {
            "title": "Mnemonic 3: UP District Rankings (Literacy, Sex Ratio, Density)",
            "phrase": "\"G-P-G (Gautam - Jaunpur - Ghaziabad)\"",
            "decryption": "Recalls the highest-ranking districts in UP for each key parameter:<br>• **G** — Gautam Buddha Nagar (Highest Literacy: 80.12%)<br>• **P** — Prayagraj (Highest Population: 59.5 lakh)<br>• **G** — Ghaziabad (Highest Density: 3971 persons/sq km)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What is the overall literacy rate of India in Census 2011?",
            "answer": "**73.0%** (Male literacy is **80.9%**, and Female literacy is **64.6%**).",
            "icon": "fa-book-open"
        },
        {
            "question": "What is the literacy rate of Uttar Pradesh in Census 2011?",
            "answer": "**67.68% (approx 67.7%)**. Male literacy is **77.28%** and Female literacy is **57.18%**. The gender gap is exactly 20.1%.",
            "icon": "fa-graduation-cap"
        },
        {
            "question": "Which district of UP has the highest and lowest sex ratio?",
            "answer": "Highest: **Jaunpur** (1024). Lowest: **Gautam Buddha Nagar** (851).",
            "icon": "fa-venus-mars"
        },
        {
            "question": "Which Indian states/UTs have NO Scheduled Tribe (ST) population?",
            "answer": "**Punjab, Haryana, Chandigarh, Delhi, and Puducherry** have zero Scheduled Tribe population.",
            "icon": "fa-users-slash"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing the highest density state with the highest density UT. The highest density **state** is Bihar (1106), but the highest density **UT** is Delhi (11,320 persons/sq km).",
        "<strong>Trap 2:</strong> Believing Haryana has the lowest child sex ratio (0-6 years) among all units. Haryana is lowest (834) among **states**, but **Daman & Diu** has the lowest child sex ratio (610) among all UTs.",
        "<strong>Trap 3:</strong> Confusing UP's general sex ratio with its child sex ratio. UP's general sex ratio is **912**, whereas its child sex ratio (0-6 years) is **902**.",
        "<strong>Trap 4:</strong> Assuming Sonbhadra is only highest in ST population. Sonbhadra has both the highest absolute number AND the highest percentage of Scheduled Tribes (ST) in Uttar Pradesh."
    ]
}

deep_dive_en = [
    {
        "title": "1. National Demographic Profile",
        "content": """<p>The 15th Census of India was conducted in 2011 under C. Chandramouli as Census Commissioner. It was divided into two phases: House Listing and Housing Census, followed by Population Enumeration.</p>
        <ul>
          <li><strong>Total Population:</strong> 121,08,54,977 (121.08 crores), consisting of 51.54% males and 48.46% females.</li>
          <li><strong>Decadal Growth Rate:</strong> 17.7% (compared to 21.5% in 1991-2001).</li>
          <li><strong>Urban-Rural Breakup:</strong> Rural population is 68.84% (83.37 crores) and Urban population is 31.16% (37.71 crores).</li>
          <li><strong>Least Populous State:</strong> Sikkim (6.1 lakh).</li>
          <li><strong>Least Populous UT:</strong> Lakshadweep (64,473).</li>
        </ul>
        
        <!-- SVG Census Dashboard Diagram -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .title-svg{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:14px;}
            .card-bg{fill:rgba(142,68,173,0.06);stroke:#8e44ad;stroke-width:1;}
            .text-main{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .text-val{font-family:'Outfit',sans-serif;font-size:18px;fill:#8e44ad;font-weight:bold;}
            .text-desc{font-family:'Inter',sans-serif;font-size:9.5px;fill:#666;}
            body.dark-mode .title-svg{fill:#f1f5f9;}
            body.dark-mode .card-bg{fill:rgba(168,85,247,0.15);stroke:#c084fc;}
            body.dark-mode .text-main{fill:#f1f5f9;}
            body.dark-mode .text-val{fill:#c084fc;}
            body.dark-mode .text-desc{fill:#cbd5e1;}
          </style>
          <text x="400" y="25" class="title-svg" text-anchor="middle">India Demographic Snapshot (Census 2011)</text>
          
          <!-- Card 1: Population -->
          <rect x="30" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="110" y="70" class="text-main" text-anchor="middle">Total Population</text>
          <text x="110" y="105" class="text-val" text-anchor="middle">1.21 Billion</text>
          <text x="110" y="135" class="text-desc" text-anchor="middle">17.7% Decadal Growth</text>
          <text x="110" y="155" class="text-desc" text-anchor="middle">17.5% of World Pop.</text>
          
          <!-- Card 2: Density -->
          <rect x="220" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="300" y="70" class="text-main" text-anchor="middle">Population Density</text>
          <text x="300" y="105" class="text-val" text-anchor="middle">382 / km²</text>
          <text x="300" y="135" class="text-desc" text-anchor="middle">Max: Bihar (1106)</text>
          <text x="300" y="155" class="text-desc" text-anchor="middle">Min: Arunachal (17)</text>
          
          <!-- Card 3: Literacy -->
          <rect x="410" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="490" y="70" class="text-main" text-anchor="middle">Literacy Rate</text>
          <text x="490" y="105" class="text-val" text-anchor="middle">73.0%</text>
          <text x="490" y="135" class="text-desc" text-anchor="middle">Male: 80.9%</text>
          <text x="490" y="155" class="text-desc" text-anchor="middle">Female: 64.6%</text>
          
          <!-- Card 4: Sex Ratio -->
          <rect x="600" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="680" y="70" class="text-main" text-anchor="middle">Sex Ratio</text>
          <text x="680" y="105" class="text-val" text-anchor="middle">943</text>
          <text x="680" y="135" class="text-desc" text-anchor="middle">Child (0-6 yrs): 919</text>
          <text x="680" y="155" class="text-desc" text-anchor="middle">Max: Kerala (1084)</text>
        </svg>"""
    },
    {
        "title": "2. National Density, Urbanisation & Literacy",
        "content": """<p>National statistics reflect rapid urbanization and improvements in literacy, though gender and regional disparities remain.</p>
        <ul>
          <li><strong>Density (Persons/km²):</strong> India's average density is 382. States: Bihar (1106) and West Bengal (1028) are highest. Arunachal Pradesh (17) is lowest.</li>
          <li><strong>Literacy:</strong> Kerala (94.0%) and Mizoram (91.3%) lead. Bihar (61.8%) and Rajasthan (66.1%) have the lowest rates. Female literacy is lowest in Bihar (51.5%) and Rajasthan (52.1%).</li>
          <li><strong>Urbanisation:</strong> Goa is the most urbanized state by percentage (62.2%), whereas Himachal Pradesh is the most rural (90.0%). Maharashtra has the largest absolute urban population (5.08 crores).</li>
        </ul>"""
    },
    {
        "title": "3. Uttar Pradesh Census 2011 Special (Part 1 - General)",
        "content": """<p>UP has the largest population among all states in India. It is a highly tested subject area in RO/ARO exams.</p>
        <ul>
          <li><strong>Total Population:</strong> 19,98,12,341 (19.98 crores), accounting for 16.51% of India's population. If UP were a country, it would be the 5th most populous country in the world.</li>
          <li><strong>Decadal Growth Rate:</strong> 20.23% (higher than the national average of 17.7%).</li>
          <li><strong>Population Density:</strong> 829 persons per sq km (ranked 9th among states).</li>
          <li><strong>Sex Ratio:</strong> 912 females per 1000 males (national average is 943).</li>
          <li><strong>Child Sex Ratio (0-6 years):</strong> 902 (national average is 919). This is a drop from 916 in 2001.</li>
          <li><strong>Literacy Rate:</strong> 67.68% (Male: 77.28%, Female: 57.18%). The gap between male and female literacy is exactly 20.1%.</li>
        </ul>"""
    },
    {
        "title": "4. Uttar Pradesh Census 2011 Special (Part 2 - District-wise Rankings)",
        "content": """<p>RO/ARO exams frequently ask for the highest and lowest ranking districts in UP for various parameters:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Parameter</th>
                <th>Highest District(s)</th>
                <th>Lowest District(s)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Population</strong></td>
                <td>Prayagraj (59.5 lakh), Moradabad, Ghaziabad</td>
                <td>Mahoba (8.7 lakh), Chitrakoot, Hamirpur</td>
              </tr>
              <tr>
                <td><strong>Density (persons/km²)</strong></td>
                <td>Ghaziabad (3971), Varanasi (2395), Lucknow (1816)</td>
                <td>Lalitpur (242), Sonbhadra (270), Hamirpur (275)</td>
              </tr>
              <tr>
                <td><strong>Literacy Rate</strong></td>
                <td>Gautam Buddha Nagar (80.12%), Kanpur Nagar, Auraiya</td>
                <td>Shravasti (46.74%), Bahraich (49.4%), Balrampur (49.5%)</td>
              </tr>
              <tr>
                <td><strong>Sex Ratio</strong></td>
                <td>Jaunpur (1024), Azamgarh (1019), Deoria (1017)</td>
                <td>Gautam Buddha Nagar (851), Hamirpur/Baghpat (861)</td>
              </tr>
              <tr>
                <td><strong>Child Sex Ratio</strong></td>
                <td>Balrampur (950), Siddharthnagar (925)</td>
                <td>Baghpat (841), Gautam Buddha Nagar (843)</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. SC & ST Demographics (National & UP)",
        "content": """<p>Marginalized population statistics are critical for competitive exams:</p>
        <ul>
          <li><strong>National SC Population:</strong> 16.6% of India. Punjab has the highest percentage (31.9%). UP has the largest absolute SC population (4.13 crores).</li>
          <li><strong>National ST Population:</strong> 8.6% of India. Lakshadweep (94.8%) and Mizoram (94.4%) are highest. MP has the largest absolute ST population (1.53 crores).</li>
          <li><strong>UP SC Population:</strong> 20.69% of UP's total population (4.13 crores). Sitapur district has the highest absolute SC population, while Kaushambi has the highest percentage of SC (34.72%). Baghpat has the lowest.</li>
          <li><strong>UP ST Population:</strong> Only 0.57% of UP's total population (11.34 lakh). Sonbhadra district has the highest absolute ST population and highest percentage (20.67%). Baghpat has the lowest.</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "जनसंख्या, परिस्थिति और नगरीकरण",
    "parentUrl": "../",
    "current": "जनगणना 2011"
}

hero_hi = {
    "title": "जनगणना 2011 मुख्य बिंदु",
    "description": "भारत की 15वीं राष्ट्रीय जनगणना (2011) का व्यापक विश्लेषण, जिसमें राष्ट्रीय और उत्तर प्रदेश-विशिष्ट जनसांख्यिकी शामिल है।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव जनगणना 2011 मॉक टेस्ट",
        "description": "राष्ट्रीय और यूपी-विशिष्ट जनगणना आंकड़ों, जिला रैंकिंग और इतिहास पर आधारित परीक्षण। समयबद्ध 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "भारत में जनगणना का विकास",
    "description": "भारत में जनसंख्या गणना के इतिहास में महत्वपूर्ण मील के पत्थर।",
    "cards": [
        {
            "period": "प्रथम जनगणना",
            "date": "1872",
            "details": "लॉर्ड मेयो के कार्यकाल में भारत की पहली गैर-समकालिक जनसंख्या जनगणना आयोजित की गई थी।"
        },
        {
            "period": "प्रथम समकालिक जनगणना",
            "date": "1881",
            "details": "लॉर्ड रिपन के अधीन पहली व्यवस्थित और समकालिक (synchronous) जनगणना आयोजित की गई। तब से यह हर दस साल में आयोजित की जाती है।"
        },
        {
            "period": "महान विभाजक वर्ष",
            "date": "1921",
            "details": "महामारी और अकाल के कारण नकारात्मक जनसंख्या वृद्धि दर (-0.31%) दर्ज करने वाला एकमात्र जनगणना वर्ष।"
        },
        {
            "period": "स्वतंत्रता के बाद पहली जनगणना",
            "date": "1951",
            "details": "जनगणना अधिनियम 1948 के तहत आयोजित की गई। स्वतंत्र भारत की जनसंख्या उस समय 36.1 करोड़ थी।"
        },
        {
            "period": "15वीं राष्ट्रीय जनगणना",
            "date": "2011",
            "details": "'हमारी जनगणना, हमारा भविष्य' के नारे के साथ सी. चंद्रमौली (जनगणना आयुक्त) के अधीन संपन्न हुई।"
        }
    ]
}

mnemonics_hi = {
    "title": "जनगणना 2011 के स्मृति सूत्र",
    "description": "राज्यों और जिलों की रैंकिंग को आसानी से याद रखने के लिए स्मृति सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: सर्वाधिक जनसंख्या वाले शीर्ष 3 राज्य",
            "phrase": "\"U-M-B (Up Man Bow)\"",
            "decryption": "सर्वाधिक आबादी वाले राज्यों का अवरोही क्रम:<br>1. **U** — उत्तर प्रदेश (19.98 करोड़)<br>2. **M** — महाराष्ट्र (11.23 करोड़)<br>3. **B** — बिहार (10.40 करोड़)"
        },
        {
            "title": "स्मृति सूत्र 2: सर्वाधिक जनघनत्व वाले शीर्ष 3 राज्य",
            "phrase": "\"B-W-K (Big Water Kettle)\"",
            "decryption": "सर्वाधिक जनघनत्व वाले राज्यों का क्रम:<br>• **B** — बिहार (1106 व्यक्ति/वर्ग किमी)<br>• **W** — पश्चिम बंगाल (1028 व्यक्ति/वर्ग किमी)<br>• **K** — केरल (860 व्यक्ति/वर्ग किमी)"
        },
        {
            "title": "स्मृति सूत्र 3: यूपी जिला रैंकिंग (साक्षरता, लिंगानुपात, जनघनत्व)",
            "phrase": "\"G-P-G (गौतम - प्रयाग - गाजियाबाद)\"",
            "decryption": "उत्तर प्रदेश के शीर्ष जिलों को याद रखने की ट्रिक:<br>• **G** — गौतम बुद्ध नगर (सर्वाधिक साक्षरता: 80.12%)<br>• **P** — प्रयागराज (सर्वाधिक जनसंख्या: 59.5% लाख)<br>• **G** — गाजियाबाद (सर्वाधिक जनघनत्व: 3971 व्यक्ति/वर्ग किमी)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "जनगणना 2011 में भारत की कुल साक्षरता दर कितनी थी?",
            "answer": "**73.0%** (पुरुष साक्षरता **80.9%** और महिला साक्षरता **64.6%** थी)।",
            "icon": "fa-book-open"
        },
        {
            "question": "उत्तर प्रदेश की साक्षरता दर कितनी है?",
            "answer": "**67.68% (लगभग 67.7%)**। पुरुष साक्षरता **77.28%** और महिला साक्षरता **57.18%** है। लिंग अंतर ठीक 20.1% है।",
            "icon": "fa-graduation-cap"
        },
        {
            "question": "उत्तर प्रदेश के किस जिले का लिंगानुपात सबसे अधिक और सबसे कम है?",
            "answer": "सर्वाधिक: **जौनपुर** (1024)। न्यूनतम: **गौतम बुद्ध नगर** (851)।",
            "icon": "fa-venus-mars"
        },
        {
            "question": "भारत के किन राज्यों में कोई अनुसूचित जनजाति (ST) जनसंख्या नहीं है?",
            "answer": "**पंजाब, हरियाणा, दिल्ली, चंडीगढ़ और पुदुचेरी** में कोई अनुसूचित जनजाति निवास नहीं करती है।",
            "icon": "fa-users-slash"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> सर्वाधिक जनघनत्व वाले राज्य और केंद्र शासित प्रदेश को भ्रमित करना। सर्वाधिक जनघनत्व वाला **राज्य** बिहार (1106) है, लेकिन सबसे अधिक जनघनत्व वाला **केंद्र शासित प्रदेश** दिल्ली (11,320 व्यक्ति/वर्ग किमी) है।",
        "<strong>भ्रम 2:</strong> राज्यों में सबसे कम बाल लिंगानुपात हरियाणा (834) का है, लेकिन सभी केंद्र शासित प्रदेशों में **दमन और दीव** का बाल लिंगानुपात सबसे कम (610) है।",
        "<strong>भ्रम 3:</strong> उत्तर प्रदेश के लिंगानुपात (912) को उसके बाल लिंगानुपात (902) के साथ भ्रमित करना।",
        "<strong>भ्रम 4:</strong> सोनभद्र जिले की जनसांख्यिकी को लेकर भ्रमित होना। सोनभद्र में उत्तर प्रदेश की सर्वाधिक अनुसूचित जनजाति (ST) जनसंख्या और प्रतिशत (20.67%) दोनों हैं।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. राष्ट्रीय जनसांख्यिकीय प्रोफ़ाइल",
        "content": """<p>भारत की 15वीं जनगणना वर्ष 2011 में जनगणना आयुक्त सी. चंद्रमौली के निर्देशन में आयोजित की गई थी।</p>
        <ul>
          <li><strong>कुल जनसंख्या:</strong> 121,08,54,977 (121.08 करोड़), जिसमें 51.54% पुरुष और 48.46% महिलाएं शामिल थीं।</li>
          <li><strong>दशकीय वृद्धि दर:</strong> 17.7%।</li>
          <li><strong>ग्रामीण और शहरी जनसंख्या:</strong> ग्रामीण जनसंख्या 68.84% (83.37 करोड़) और शहरी जनसंख्या 31.16% (37.71 करोड़) है।</li>
          <li><strong>सबसे कम जनसंख्या वाला राज्य:</strong> सिक्किम (6.1 lakh)।</li>
        </ul>
        
        <!-- SVG Census Dashboard Diagram -->
        <svg viewBox="0 0 800 240" class="responsive-svg-diagram" style="margin:1rem 0; border-radius:10px; background:var(--bg-card,#ffffff); padding:10px;">
          <style>
            .title-svg{font-family:'Outfit',sans-serif;font-weight:bold;fill:var(--text-dark,#2c3e50);font-size:14px;}
            .card-bg{fill:rgba(142,68,173,0.06);stroke:#8e44ad;stroke-width:1;}
            .text-main{font-family:'Inter',sans-serif;font-size:11px;fill:var(--text-dark,#2c3e50);font-weight:600;}
            .text-val{font-family:'Outfit',sans-serif;font-size:18px;fill:#8e44ad;font-weight:bold;}
            .text-desc{font-family:'Inter',sans-serif;font-size:9.5px;fill:#666;}
            body.dark-mode .title-svg{fill:#f1f5f9;}
            body.dark-mode .card-bg{fill:rgba(168,85,247,0.15);stroke:#c084fc;}
            body.dark-mode .text-main{fill:#f1f5f9;}
            body.dark-mode .text-val{fill:#c084fc;}
            body.dark-mode .text-desc{fill:#cbd5e1;}
          </style>
          <text x="400" y="25" class="title-svg" text-anchor="middle">भारत जनसांख्यिकी अवलोकन (जनगणना 2011)</text>
          
          <!-- Card 1: Population -->
          <rect x="30" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="110" y="70" class="text-main" text-anchor="middle">कुल जनसंख्या</text>
          <text x="110" y="105" class="text-val" text-anchor="middle">1.21 अरब</text>
          <text x="110" y="135" class="text-desc" text-anchor="middle">17.7% दशकीय वृद्धि</text>
          <text x="110" y="155" class="text-desc" text-anchor="middle">वैश्विक आबादी का 17.5%</text>
          
          <!-- Card 2: Density -->
          <rect x="220" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="300" y="70" class="text-main" text-anchor="middle">जनसंख्या घनत्व</text>
          <text x="300" y="105" class="text-val" text-anchor="middle">382 / किमी²</text>
          <text x="300" y="135" class="text-desc" text-anchor="middle">अधिकतम: बिहार (1106)</text>
          <text x="300" y="155" class="text-desc" text-anchor="middle">न्यूनतम: अरुणाचल (17)</text>
          
          <!-- Card 3: Literacy -->
          <rect x="410" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="490" y="70" class="text-main" text-anchor="middle">साक्षरता दर</text>
          <text x="490" y="105" class="text-val" text-anchor="middle">73.0%</text>
          <text x="490" y="135" class="text-desc" text-anchor="middle">पुरुष: 80.9%</text>
          <text x="490" y="155" class="text-desc" text-anchor="middle">महिला: 64.6%</text>
          
          <!-- Card 4: Sex Ratio -->
          <rect x="600" y="45" width="160" height="150" class="card-bg" rx="8" />
          <text x="680" y="70" class="text-main" text-anchor="middle">लिंगानुपात</text>
          <text x="680" y="105" class="text-val" text-anchor="middle">943</text>
          <text x="680" y="135" class="text-desc" text-anchor="middle">बाल (0-6 वर्ष): 919</text>
          <text x="680" y="155" class="text-desc" text-anchor="middle">अधिकतम: केरल (1084)</text>
        </svg>"""
    },
    {
        "title": "2. राष्ट्रीय घनत्व, नगरीकरण और साक्षरता",
        "content": """<p>राष्ट्रीय सांख्यिकी भारत में तेजी से बढ़ते नगरीकरण और साक्षरता को दर्शाती है, हालांकि लिंग और क्षेत्रीय असमानताएं बनी हुई हैं।</p>
        <ul>
          <li><strong>जनघनत्व:</strong> औसत जनघनत्व 382 व्यक्ति प्रति वर्ग किमी है। बिहार (1106) और पश्चिम बंगाल (1028) शीर्ष पर हैं, जबकि अरुणाचल प्रदेश (17) न्यूनतम पर है।</li>
          <li><strong>साक्षरता:</strong> केरल (94.0%) शीर्ष पर है और बिहार (61.8%) न्यूनतम पर है। महिला साक्षरता बिहार (51.5%) और राजस्थान (52.1%) में सबसे कम है।</li>
          <li><strong>नगरीकरण:</strong> गोवा सर्वाधिक शहरीकृत राज्य है (62.2%) और हिमाचल प्रदेश सर्वाधिक ग्रामीण राज्य (90.0%) है।</li>
        </ul>"""
    },
    {
        "title": "3. उत्तर प्रदेश जनगणना 2011 विशेष (भाग 1 - सामान्य)",
        "content": """<p>उत्तर प्रदेश भारत में सर्वाधिक जनसंख्या वाला राज्य है। यह RO/ARO परीक्षाओं में अत्यधिक पूछा जाने वाला विषय है।</p>
        <ul>
          <li><strong>कुल जनसंख्या:</strong> 19,98,12,341 (19.98 करोड़), जो देश की कुल आबादी का 16.51% है। यदि यूपी एक देश होता, तो यह दुनिया का 5वां सबसे बड़ा आबादी वाला देश होता।</li>
          <li><strong>दशकीय वृद्धि दर:</strong> 20.23% (राष्ट्रीय औसत 17.7% से अधिक)।</li>
          <li><strong>जनसंख्या घनत्व:</strong> 829 व्यक्ति प्रति वर्ग किमी (राज्यों में 9वां स्थान)।</li>
          <li><strong>लिंगानुपात:</strong> 912 (राष्ट्रीय औसत 943 से कम)।</li>
          <li><strong>बाल लिंगानुपात (0-6 वर्ष):</strong> 902 (वर्ष 2001 में यह 916 था)।</li>
          <li><strong>साक्षरता दर:</strong> 67.68% (पुरुष साक्षरता: 77.28%, महिला साक्षरता: 57.18%)। पुरुष और महिला साक्षरता दर का अंतर ठीक 20.1% है।</li>
        </ul>"""
    },
    {
        "title": "4. उत्तर प्रदेश जनगणना 2011 विशेष (भाग 2 - जिलावार रैंकिंग)",
        "content": """<p>उत्तर प्रदेश के विभिन्न जनसांख्यिकी मानदंडों में जिलों की रैंकिंग बार-बार परीक्षाओं में पूछी जाती है:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>मानदंड</th>
                <th>शीर्ष जिला</th>
                <th>न्यूनतम जिला</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>जनसंख्या</strong></td>
                <td>प्रयागराज (59.5 लाख), मुरादाबाद, गाजियाबाद</td>
                <td>महोबा (8.7 लाख), चित्रकूट, हमीरपुर</td>
              </tr>
              <tr>
                <td><strong>जनघनत्व (व्यक्ति/किमी²)</strong></td>
                <td>गाजियाबाद (3971), वाराणसी (2395), लखनऊ (1816)</td>
                <td>ललितपुर (242), सोनभद्र (270), हमीरपुर (275)</td>
              </tr>
              <tr>
                <td><strong>साक्षरता दर</strong></td>
                <td>गौतम बुद्ध नगर (80.12%), कानपुर नगर, औरैया</td>
                <td>श्रावस्ती (46.74%), बहराइच (49.4%), बलरामपुर (49.5%)</td>
              </tr>
              <tr>
                <td><strong>लिंगानुपात</strong></td>
                <td>जौनपुर (1024), आज़मगढ़ (1019), देवरिया (1017)</td>
                <td>गौतम बुद्ध नगर (851), हमीरपुर/बागपत (861)</td>
              </tr>
              <tr>
                <td><strong>बाल लिंगानुपात</strong></td>
                <td>बलरामपुर (950), सिद्धार्थनगर (925)</td>
                <td>बागपत (841), गौतम बुद्ध नगर (843)</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. अनुसूचित जाति (SC) और अनुसूचित जनजाति (ST) आंकड़े",
        "content": """<p>संवैधानिक प्रावधानों और परीक्षा की दृष्टि से अनुसूचित जाति और जनजाति के आंकड़े अत्यंत महत्वपूर्ण हैं:</p>
        <ul>
          <li><strong>राष्ट्रीय SC जनसंख्या:</strong> कुल आबादी का 16.6%। पंजाब में सर्वाधिक प्रतिशत (31.9%) है। यूपी में सर्वाधिक वास्तविक संख्या (4.13 करोड़) है।</li>
          <li><strong>राष्ट्रीय ST जनसंख्या:</strong> कुल आबादी का 8.6%। लक्षद्वीप (94.8%) और मिजोरम (94.4%) शीर्ष पर हैं।</li>
          <li><strong>उत्तर प्रदेश SC जनसंख्या:</strong> राज्य की कुल आबादी का 20.69% (4.13 करोड़)। सीतापुर जिले में सर्वाधिक वास्तविक SC जनसंख्या है, जबकि कौशाम्बी में सर्वाधिक प्रतिशत (34.72%) है। बागपत में सबसे कम है।</li>
          <li><strong>उत्तर प्रदेश ST जनसंख्या:</strong> राज्य की कुल आबादी का केवल 0.57% (11.34 लाख)। सोनभद्र जिले में सर्वाधिक वास्तविक जनसंख्या और प्रतिशत (20.67%) दोनों हैं। बागपत में न्यूनतम है।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs - RO/ARO Exam Standard) -----------------
practice_questions = [
    {
        "q": "What was the motto of the 15th National Census of India (2011)?",
        "q_hi": "भारत की 15वीं राष्ट्रीय जनगणना (2011) का नारा (motto) क्या था?",
        "opts": ["Our Census, Our Pride", "Our Census, Our Future", "One Nation, One Census", "Census for Development"],
        "opts_hi": ["हमारी जनगणना, हमारा गौरव", "हमारी जनगणना, हमारा भविष्य", "एक राष्ट्र, एक जनगणना", "विकास के लिए जनगणना"],
        "ans": 1,
        "sol": "The official motto of the Census 2011 was 'Our Census, Our Future'.",
        "sol_hi": "जनगणना 2011 का आधिकारिक नारा 'हमारी जनगणना, हमारा भविष्य' था।"
    },
    {
        "q": "Who was the Census Commissioner of India during the 2011 Census?",
        "q_hi": "2011 की जनगणना के दौरान भारत के जनगणना आयुक्त कौन थे?",
        "opts": ["C. Chandramouli", "W.W. Hunter", "Pranab Mukherjee", "J.K. Banthia"],
        "opts_hi": ["सी. चंद्रमौली", "डब्ल्यू.डब्ल्यू. हंटर", "प्रणब मुखर्जी", "जे.के. बांठिया"],
        "ans": 0,
        "sol": "Dr. C. Chandramouli served as the Registrar General and Census Commissioner of India for the 2011 Census.",
        "sol_hi": "डॉ. सी. चंद्रमौली ने 2011 की जनगणना के लिए भारत के महारजिस्ट्रार और जनगणना आयुक्त के रूप में कार्य किया था।"
    },
    {
        "q": "According to Census 2011, which state has the highest population density in India?",
        "q_hi": "जनगणना 2011 के अनुसार, भारत के किस राज्य में जनसंख्या घनत्व सबसे अधिक है?",
        "opts": ["West Bengal", "Bihar", "Uttar Pradesh", "Kerala"],
        "opts_hi": ["पश्चिम बंगाल", "बिहार", "उत्तर प्रदेश", "केरल"],
        "ans": 1,
        "sol": "Bihar has the highest population density among states with 1106 persons per square kilometer, followed by West Bengal with 1028.",
        "sol_hi": "राज्यों में बिहार का जनघनत्व सर्वाधिक 1106 व्यक्ति प्रति वर्ग किमी है, उसके बाद पश्चिम बंगाल का स्थान 1028 व्यक्ति प्रति वर्ग किमी के साथ आता है।"
    },
    {
        "q": "According to Census 2011, what is the total population of Uttar Pradesh?",
        "q_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश की कुल जनसंख्या कितनी है?",
        "opts": ["16.61 crores", "19.98 crores", "21.04 crores", "18.52 crores"],
        "opts_hi": ["16.61 करोड़", "19.98 करोड़", "21.04 करोड़", "18.52 करोड़"],
        "ans": 1,
        "sol": "The population of Uttar Pradesh is 19,98,12,341 (approx. 19.98 crores), which is 16.51% of India's total population.",
        "sol_hi": "उत्तर प्रदेश की कुल जनसंख्या 19,98,12,341 (लगभग 19.98 करोड़) है, जो भारत की कुल जनसंख्या का 16.51% है।"
    },
    {
        "q": "What is the overall literacy rate of India as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत की कुल साक्षरता दर कितनी है?",
        "opts": ["64.8%", "74.0%", "73.0%", "72.5%"],
        "opts_hi": ["64.8%", "74.0%", "73.0%", "72.5%"],
        "ans": 2,
        "sol": "The final data of Census 2011 declared the literacy rate of India to be 73.0% (provisional was 74.04%).",
        "sol_hi": "जनगणना 2011 के अंतिम आंकड़ों के अनुसार भारत की कुल साक्षरता दर 73.0% है।"
    },
    {
        "q": "Which state has the highest literacy rate in India according to Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार किस भारतीय राज्य की साक्षरता दर सबसे अधिक है?",
        "opts": ["Mizoram", "Goa", "Kerala", "Tripura"],
        "opts_hi": ["मिजोरम", "गोवा", "केरल", "त्रिपुरा"],
        "ans": 2,
        "sol": "Kerala has the highest literacy rate in India at 94.0%, followed by Mizoram at 91.3%.",
        "sol_hi": "केरल की साक्षरता दर भारत में सर्वाधिक 94.0% है, उसके बाद मिजोरम का स्थान 91.3% के साथ आता है।"
    },
    {
        "q": "What is the literacy rate of Uttar Pradesh as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश की साक्षरता दर कितनी है?",
        "opts": ["56.3%", "67.7%", "75.4%", "69.1%"],
        "opts_hi": ["56.3%", "67.7%", "75.4%", "69.1%"],
        "ans": 1,
        "sol": "UP's literacy rate is 67.68% (approx. 67.7%). Male literacy is 77.28% and female literacy is 57.18%.",
        "sol_hi": "उत्तर प्रदेश की साक्षरता दर 67.68% (लगभग 67.7%) है, जिसमें पुरुष साक्षरता 77.28% और महिला साक्षरता 57.18% है।"
    },
    {
        "q": "What was the sex ratio of India in Census 2011?",
        "q_hi": "जनगणना 2011 में भारत का लिंगानुपात कितना था?",
        "opts": ["933", "940", "943", "946"],
        "opts_hi": ["933", "940", "943", "946"],
        "ans": 2,
        "sol": "The national sex ratio of India stood at 943 in Census 2011.",
        "sol_hi": "जनगणना 2011 में भारत का राष्ट्रीय लिंगानुपात 943 था।"
    },
    {
        "q": "What is the general sex ratio of Uttar Pradesh according to Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश का सामान्य लिंगानुपात कितना है?",
        "opts": ["898", "912", "933", "902"],
        "opts_hi": ["898", "912", "933", "902"],
        "ans": 1,
        "sol": "The general sex ratio of Uttar Pradesh in Census 2011 is 912 females per 1000 males.",
        "sol_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश का सामान्य लिंगानुपात प्रति 1000 पुरुषों पर 912 महिलाएँ हैं।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest sex ratio?",
        "q_hi": "उत्तर प्रदेश के किस जिले का लिंगानुपात सर्वाधिक है?",
        "opts": ["Jaunpur", "Azamgarh", "Deoria", "Pratapgarh"],
        "opts_hi": ["जौनपुर", "आज़मगढ़", "देवरिया", "प्रतापगढ़"],
        "ans": 0,
        "sol": "Jaunpur has the highest sex ratio in UP with 1024, followed by Azamgarh with 1019.",
        "sol_hi": "जौनपुर में उत्तर प्रदेश का सर्वाधिक लिंगानुपात 1024 है, उसके बाद आज़मगढ़ का 1019 है।"
    },
    {
        "q": "What is the child sex ratio (0-6 years) of Uttar Pradesh in Census 2011?",
        "q_hi": "जनगणना 2011 में उत्तर प्रदेश का बाल लिंगानुपात (0-6 वर्ष) कितना है?",
        "opts": ["916", "902", "912", "899"],
        "opts_hi": ["916", "902", "912", "899"],
        "ans": 1,
        "sol": "The child sex ratio of UP in Census 2011 is 902, which is a decline from 916 in 2001.",
        "sol_hi": "उत्तर प्रदेश का बाल लिंगानुपात (0-6 वर्ष) जनगणना 2011 में 902 है, जो 2001 के 916 से कम है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest sex ratio?",
        "q_hi": "उत्तर प्रदेश के किस जिले का लिंगानुपात सबसे कम है?",
        "opts": ["Gautam Buddha Nagar", "Baghpat", "Hamirpur", "Kanpur Nagar"],
        "opts_hi": ["गौतम बुद्ध नगर", "बागपत", "हमीरपुर", "कानपुर नगर"],
        "ans": 0,
        "sol": "Gautam Buddha Nagar has the lowest sex ratio in UP at 851 females per 1000 males.",
        "sol_hi": "गौतम बुद्ध नगर का लिंगानुपात उत्तर प्रदेश में सबसे कम 851 है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest population density?",
        "q_hi": "उत्तर प्रदेश के किस जिले का जनसंख्या घनत्व सर्वाधिक है?",
        "opts": ["Lucknow", "Varanasi", "Ghaziabad", "Kanpur Nagar"],
        "opts_hi": ["लखनऊ", "वाराणसी", "गाजियाबाद", "कानपुर नगर"],
        "ans": 2,
        "sol": "Ghaziabad is the most densely populated district in UP with 3971 persons per sq km, followed by Varanasi with 2395.",
        "sol_hi": "गाजियाबाद उत्तर प्रदेश में सर्वाधिक जनघनत्व वाला जिला है (3971 व्यक्ति प्रति वर्ग किमी), उसके बाद वाराणसी का स्थान आता है (2395)।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest population density?",
        "q_hi": "उत्तर प्रदेश के किस जिले का जनसंख्या घनत्व सबसे कम है?",
        "opts": ["Sonbhadra", "Lalitpur", "Hamirpur", "Mahoba"],
        "opts_hi": ["सोनभद्र", "ललितपुर", "हमीरपुर", "महोबा"],
        "ans": 1,
        "sol": "Lalitpur has the lowest population density in UP with 242 persons per sq km.",
        "sol_hi": "ललितपुर में उत्तर प्रदेश का न्यूनतम जनघनत्व है, जहाँ केवल 242 व्यक्ति प्रति वर्ग किमी निवास करते हैं।"
    },
    {
        "q": "Which district of Uttar Pradesh is the most populous?",
        "q_hi": "उत्तर प्रदेश का सर्वाधिक जनसंख्या वाला जिला कौन सा है?",
        "opts": ["Moradabad", "Ghaziabad", "Prayagraj", "Lucknow"],
        "opts_hi": ["मुरादाबाद", "गाजियाबाद", "प्रयागराज", "लखनऊ"],
        "ans": 2,
        "sol": "Prayagraj (formerly Allahabad) is the most populous district in UP with around 59.5 lakh residents.",
        "sol_hi": "प्रयागराज उत्तर प्रदेश का सर्वाधिक जनसंख्या वाला जिला है, जिसकी आबादी लगभग 59.5 लाख है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest literacy rate?",
        "q_hi": "उत्तर प्रदेश के किस जिले की साक्षरता दर सबसे कम है?",
        "opts": ["Bahraich", "Shravasti", "Balrampur", "Badaun"],
        "opts_hi": ["बहराइच", "श्रावस्ती", "बलरामपुर", "बदायूँ"],
        "ans": 1,
        "sol": "Shravasti has the lowest literacy rate in UP (and in India) at 46.74%.",
        "sol_hi": "श्रावस्ती की साक्षरता दर उत्तर प्रदेश में सबसे कम 46.74% है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest literacy rate?",
        "q_hi": "उत्तर प्रदेश के किस जिले की साक्षरता दर सर्वाधिक है?",
        "opts": ["Gautam Buddha Nagar", "Kanpur Nagar", "Auraiya", "Ghaziabad"],
        "opts_hi": ["गौतम बुद्ध नगर", "कानपुर नगर", "औरैया", "गाजियाबाद"],
        "ans": 0,
        "sol": "Gautam Buddha Nagar has the highest literacy rate in UP at 80.12%, followed by Kanpur Nagar at 79.65%.",
        "sol_hi": "गौतम बुद्ध नगर की साक्षरता दर उत्तर प्रदेश में सर्वाधिक 80.12% है।"
    },
    {
        "q": "What is the percentage of Scheduled Castes (SC) in the total population of Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश की कुल जनसंख्या में अनुसूचित जातियों (SC) का प्रतिशत क्या है?",
        "opts": ["16.6%", "20.69%", "21.5%", "18.2%"],
        "opts_hi": ["16.6%", "20.69%", "21.5%", "18.2%"],
        "ans": 1,
        "sol": "Scheduled Castes account for 20.69% of the total population of Uttar Pradesh, amounting to approx 4.13 crores.",
        "sol_hi": "अनुसूचित जातियां उत्तर प्रदेश की कुल जनसंख्या का 20.69% हैं, जिनकी संख्या लगभग 4.13 करोड़ है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest proportion (percentage) of Scheduled Castes (SC)?",
        "q_hi": "उत्तर प्रदेश के किस जिले में अनुसूचित जाति (SC) का अनुपात (प्रतिशत) सर्वाधिक है?",
        "opts": ["Sitapur", "Kaushambi", "Jhansi", "Baghpat"],
        "opts_hi": ["सीतापुर", "कौशाम्बी", "झाँसी", "बागपत"],
        "ans": 1,
        "sol": "Kaushambi has the highest percentage of SC population (34.72%) in UP, though Sitapur has the highest absolute number of SC residents.",
        "sol_hi": "कौशाम्बी में अनुसूचित जाति का प्रतिशत सर्वाधिक (34.72%) है, हालांकि सीतापुर में अनुसूचित जातियों की वास्तविक संख्या सबसे अधिक है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest Scheduled Tribe (ST) population and percentage?",
        "q_hi": "उत्तर प्रदेश के किस जिले में अनुसूचित जनजाति (ST) की सर्वाधिक जनसंख्या और प्रतिशत पाया जाता है?",
        "opts": ["Lalitpur", "Sonbhadra", "Baghpat", "Deoria"],
        "opts_hi": ["ललितपुर", "सोनभद्र", "बागपत", "देवरिया"],
        "ans": 1,
        "sol": "Sonbhadra has both the highest absolute ST population and the highest percentage of ST population (20.67%) in UP.",
        "sol_hi": "सोनभद्र में उत्तर प्रदेश की सर्वाधिक अनुसूचित जनजाति (ST) जनसंख्या और प्रतिशत (20.67%) दोनों पाए जाते हैं।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest population?",
        "q_hi": "उत्तर प्रदेश के किस जिले की जनसंख्या सबसे कम है?",
        "opts": ["Chitrakoot", "Mahoba", "Hamirpur", "Shravasti"],
        "opts_hi": ["चित्रकूट", "महोबा", "हमीरपुर", "श्रावस्ती"],
        "ans": 1,
        "sol": "Mahoba is the least populous district in Uttar Pradesh, with a population of approximately 8.7 lakh.",
        "sol_hi": "महोबा उत्तर प्रदेश का सबसे कम जनसंख्या वाला जिला है, जिसकी आबादी लगभग 8.7 लाख है।"
    },
    {
        "q": "The decadal growth rate of Uttar Pradesh population during 2001-2011 was:",
        "q_hi": "2001-2011 के दौरान उत्तर प्रदेश की दशकीय जनसंख्या वृद्धि दर क्या थी?",
        "opts": ["17.7%", "20.23%", "25.8%", "18.5%"],
        "opts_hi": ["17.7%", "20.23%", "25.8%", "18.5%"],
        "ans": 1,
        "sol": "The decadal growth rate of Uttar Pradesh was 20.23%, which is higher than the national average of 17.7%.",
        "sol_hi": "उत्तर प्रदेश की दशकीय जनसंख्या वृद्धि दर 20.23% थी, जो राष्ट्रीय औसत 17.7% से अधिक है।"
    },
    {
        "q": "In which year did the census record a negative population growth rate in India?",
        "q_hi": "किस वर्ष की जनगणना ने भारत में ऋणात्मक (नकारात्मक) जनसंख्या वृद्धि दर दर्ज की थी?",
        "opts": ["1911", "1921", "1951", "1931"],
        "opts_hi": ["1911", "1921", "1951", "1931"],
        "ans": 1,
        "sol": "In the 1921 Census, India's population growth rate was -0.31% due to epidemics and food shortages.",
        "sol_hi": "1921 की जनगणना में महामारियों और अकाल के कारण भारत की जनसंख्या वृद्धि दर -0.31% (ऋणात्मक) दर्ज हुई थी।"
    },
    {
        "q": "According to Census 2011, what is the status of Scheduled Tribes (ST) in Uttar Pradesh?",
        "q_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश में अनुसूचित जनजातियों (ST) की स्थिति क्या है?",
        "opts": ["8.6% of population", "0.57% of population", "2.5% of population", "Zero population"],
        "opts_hi": ["जनसंख्या का 8.6%", "जनसंख्या का 0.57%", "जनसंख्या का 2.5%", "शून्य जनसंख्या"],
        "ans": 1,
        "sol": "Scheduled Tribes make up only 0.57% of the total population of Uttar Pradesh (approx. 11.34 lakh).",
        "sol_hi": "अनुसूचित जनजातियाँ उत्तर प्रदेश की कुल जनसंख्या का केवल 0.57% (लगभग 11.34 लाख) हैं।"
    },
    {
        "q": "Which district of Uttar Pradesh has the highest child sex ratio?",
        "q_hi": "उत्तर प्रदेश के किस जिले में सर्वाधिक बाल लिंगानुपात (0-6 वर्ष) दर्ज किया गया?",
        "opts": ["Balrampur", "Baghpat", "Jaunpur", "Gautam Buddha Nagar"],
        "opts_hi": ["बलरामपुर", "बागपत", "जौनपुर", "गौतम बुद्ध नगर"],
        "ans": 0,
        "sol": "Balrampur has the highest child sex ratio in UP with 950, while Baghpat has the lowest with 841.",
        "sol_hi": "बलरामपुर में उत्तर प्रदेश का सर्वाधिक बाल लिंगानुपात 950 दर्ज किया गया, जबकि बागपत में न्यूनतम (841) रहा।"
    },
    {
        "q": "Which state of India has the lowest population as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत के किस राज्य की जनसंख्या सबसे कम है?",
        "opts": ["Sikkim", "Goa", "Mizoram", "Arunachal Pradesh"],
        "opts_hi": ["सिक्किम", "गोवा", "मिजोरम", "अरुणाचल प्रदेश"],
        "ans": 0,
        "sol": "Sikkim is the least populous state in India with 6.1 lakh people.",
        "sol_hi": "सिक्किम भारत का सबसे कम जनसंख्या वाला राज्य है, जिसकी आबादी केवल 6.1 लाख है।"
    },
    {
        "q": "What is the ranking of Uttar Pradesh in population density among all Indian states?",
        "q_hi": "सभी भारतीय राज्यों में जनसंख्या घनत्व के मामले में उत्तर प्रदेश का कौन सा स्थान है?",
        "opts": ["1st", "4th", "9th", "11th"],
        "opts_hi": ["पहला", "चौथा", "9वां (9th)", "11वां"],
        "ans": 2,
        "sol": "Uttar Pradesh ranks 9th in population density among all Indian states, with 829 persons per sq km.",
        "sol_hi": "उत्तर प्रदेश सभी भारतीय राज्यों में जनघनत्व के मामले में 9वें स्थान पर है (829 व्यक्ति प्रति वर्ग किमी)।"
    },
    {
        "q": "Which of the following Union Territories has the highest literacy rate in India?",
        "q_hi": "निम्नलिखित में से किस केंद्र शासित प्रदेश की साक्षरता दर भारत में सबसे अधिक है?",
        "opts": ["Delhi", "Lakshadweep", "Puducherry", "Chandigarh"],
        "opts_hi": ["दिल्ली", "लक्षद्वीप", "पुदुचेरी", "चंडीगढ़"],
        "ans": 1,
        "sol": "Lakshadweep has the highest literacy rate among UTs at 91.85% (approx 91.8%).",
        "sol_hi": "लक्षद्वीप की साक्षरता दर केंद्र शासित प्रदेशों में सर्वाधिक 91.8% है।"
    },
    {
        "q": "Which state in India has the highest proportion of rural population?",
        "q_hi": "भारत में किस राज्य में ग्रामीण जनसंख्या का अनुपात सर्वाधिक है?",
        "opts": ["Bihar", "Himachal Pradesh", "Assam", "Odisha"],
        "opts_hi": ["बिहार", "हिमाचल प्रदेश", "असम", "ओडिशा"],
        "ans": 1,
        "sol": "Himachal Pradesh has the highest rural population percentage at 90.0%.",
        "sol_hi": "हिमाचल प्रदेश में ग्रामीण जनसंख्या का प्रतिशत सर्वाधिक (90.0%) है।"
    },
    {
        "q": "According to Census 2011, the gender gap in literacy rate in Uttar Pradesh is:",
        "q_hi": "जनगणना 2011 के अनुसार उत्तर प्रदेश में साक्षरता दर में महिला-पुरुष अंतर (gender gap) कितना है?",
        "opts": ["15.2%", "20.1%", "23.4%", "18.8%"],
        "opts_hi": ["15.2%", "20.1%", "23.4%", "18.8%"],
        "ans": 1,
        "sol": "The gap between male literacy (77.28%) and female literacy (57.18%) in UP is exactly 20.1%.",
        "sol_hi": "उत्तर प्रदेश में पुरुष साक्षरता (77.28%) और महिला साक्षरता (57.18%) का अंतर ठीक 20.1% है।"
    },
    # --- ADDITIONAL 20 QUESTIONS TO REACH EXACTLY 50 ---
    {
        "q": "Consider the following statements regarding Census 2011:\n1. The decadal growth rate of India's population was 17.7%.\n2. The decadal growth rate of Uttar Pradesh was 20.23%.\nWhich of the statements given above is/are correct?",
        "q_hi": "जनगणना 2011 के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. भारत की जनसंख्या की दशकीय वृद्धि दर 17.7% थी।\n2. उत्तर प्रदेश की दशकीय वृद्धि दर 20.23% थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 2,
        "sol": "Both statements are correct. India's decadal growth was 17.7% and UP's decadal growth was 20.23%.",
        "sol_hi": "दोनों कथन सही हैं। भारत की दशकीय वृद्धि दर 17.7% थी और उत्तर प्रदेश की दशकीय वृद्धि दर 20.23% थी।"
    },
    {
        "q": "Which of the following states is ranked second in terms of total population in India as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत में कुल जनसंख्या के मामले में दूसरे स्थान पर कौन सा राज्य है?",
        "opts": ["Bihar", "West Bengal", "Maharashtra", "Madhya Pradesh"],
        "opts_hi": ["बिहार", "पश्चिम बंगाल", "महाराष्ट्र", "मध्य प्रदेश"],
        "ans": 2,
        "sol": "Maharashtra is the second most populous state (11.23 crore), while Uttar Pradesh is first and Bihar is third.",
        "sol_hi": "महाराष्ट्र दूसरा सबसे अधिक जनसंख्या वाला राज्य है (11.23 करोड़), जबकि उत्तर प्रदेश पहले और बिहार तीसरे स्थान पर है।"
    },
    {
        "q": "Identify the state with the highest literacy rate among women according to Census 2011:",
        "q_hi": "जनगणना 2011 के अनुसार महिलाओं में सबसे अधिक साक्षरता दर वाला राज्य पहचानें:",
        "opts": ["Mizoram", "Kerala", "Goa", "Tripura"],
        "opts_hi": ["मिजोरम", "केरल", "गोवा", "त्रिपुरा"],
        "ans": 1,
        "sol": "Kerala has the highest female literacy rate in India at 92.1%.",
        "sol_hi": "केरल में महिला साक्षरता दर भारत में सबसे अधिक 92.1% है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest Scheduled Caste (SC) population?",
        "q_hi": "उत्तर प्रदेश के किस जिले में अनुसूचित जाति (SC) की जनसंख्या सबसे कम है?",
        "opts": ["Baghpat", "Mahoba", "Chitrakoot", "Lalitpur"],
        "opts_hi": ["बागपत", "महोबा", "चित्रकूट", "ललितपुर"],
        "ans": 0,
        "sol": "Baghpat has the lowest Scheduled Caste population in Uttar Pradesh in both absolute numbers and percentage.",
        "sol_hi": "बागपत में उत्तर प्रदेश की सबसे कम अनुसूचित जाति (SC) जनसंख्या (वास्तविक संख्या और प्रतिशत दोनों में) है।"
    },
    {
        "q": "What is the ranking of Uttar Pradesh in India in terms of total Scheduled Caste (SC) population size?",
        "q_hi": "कुल अनुसूचित जाति (SC) जनसंख्या के आकार के मामले में उत्तर प्रदेश का भारत में कौन सा स्थान है?",
        "opts": ["First", "Second", "Third", "Fourth"],
        "opts_hi": ["पहला", "दूसरा", "तीसरा", "चौथा"],
        "ans": 0,
        "sol": "Uttar Pradesh ranks first in India in terms of absolute Scheduled Caste population, with over 4.13 crore SC residents.",
        "sol_hi": "उत्तर प्रदेश 4.13 करोड़ से अधिक अनुसूचित जाति निवासियों के साथ वास्तविक संख्या के मामले में भारत में पहले स्थान पर है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest Scheduled Tribe (ST) population?",
        "q_hi": "उत्तर प्रदेश के किस जिले में अनुसूचित जनजाति (ST) की जनसंख्या सबसे कम है?",
        "opts": ["Baghpat", "Lalitpur", "Mahoba", "Sonbhadra"],
        "opts_hi": ["बागपत", "ललितपुर", "महोबा", "सोनभद्र"],
        "ans": 0,
        "sol": "Baghpat has the lowest Scheduled Tribe population in Uttar Pradesh.",
        "sol_hi": "बागपत में उत्तर प्रदेश की सबसे कम अनुसूचित जनजाति (ST) जनसंख्या निवास करती है।"
    },
    {
        "q": "Arrange the following districts of Uttar Pradesh in descending order of their population:\n1. Prayagraj\n2. Moradabad\n3. Ghaziabad\n4. Azamgarh\nSelect the correct code:",
        "q_hi": "उत्तर प्रदेश के निम्नलिखित जिलों को उनकी जनसंख्या के अनुसार अवरोही क्रम (घटते क्रम) में व्यवस्थित करें:\n1. प्रयागराज\n2. मुरादाबाद\n3. गाजियाबाद\n4. आज़मगढ़\nसही कोड चुनें:",
        "opts": ["1-2-3-4", "1-3-2-4", "2-1-3-4", "1-2-4-3"],
        "opts_hi": ["1-2-3-4", "1-3-2-4", "2-1-3-4", "1-2-4-3"],
        "ans": 0,
        "sol": "The correct descending order of population is Prayagraj (59.5L) > Moradabad (47.7L) > Ghaziabad (46.8L) > Azamgarh (46.1L). Hence option A is correct.",
        "sol_hi": "जनसंख्या का सही अवरोही क्रम है: प्रयागराज (59.5 लाख) > मुरादाबाद (47.7 लाख) > गाजियाबाद (46.8 लाख) > आज़मगढ़ (46.1 लाख)। अतः विकल्प A सही है।"
    },
    {
        "q": "What is the percentage of Scheduled Tribes (ST) in the total population of India as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत की कुल जनसंख्या में अनुसूचित जनजाति (ST) का प्रतिशत कितना है?",
        "opts": ["8.6%", "16.6%", "7.5%", "10.2%"],
        "opts_hi": ["8.6%", "16.6%", "7.5%", "10.2%"],
        "ans": 0,
        "sol": "Scheduled Tribes make up 8.6% of the total population of India according to Census 2011.",
        "sol_hi": "जनगणना 2011 के अनुसार अनुसूचित जनजातियाँ भारत की कुल जनसंख्या का 8.6% हैं।"
    },
    {
        "q": "Which state has the lowest proportion of Scheduled Castes (SC) population in India (excluding states with zero SC)?",
        "q_hi": "भारत में (शून्य SC वाले राज्यों को छोड़कर) किस राज्य में अनुसूचित जाति (SC) जनसंख्या का अनुपात सबसे कम है?",
        "opts": ["Mizoram", "Meghalaya", "Goa", "Assam"],
        "opts_hi": ["मिजोरम", "मेघालय", "गोवा", "असम"],
        "ans": 0,
        "sol": "Mizoram has the lowest proportion of Scheduled Castes population at just 0.1% of its population.",
        "sol_hi": "मिजोरम में अनुसूचित जाति की जनसंख्या का अनुपात सबसे कम (केवल 0.1%) है।"
    },
    {
        "q": "Which of the following Union Territories has the lowest population in India as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत में सबसे कम जनसंख्या वाला केंद्र शासित प्रदेश कौन सा है?",
        "opts": ["Lakshadweep", "Daman and Diu", "Dadra and Nagar Haveli", "Andaman and Nicobar Islands"],
        "opts_hi": ["लक्षद्वीप", "दमन और दीव", "दादरा और नगर हवेली", "अंडमान और निकोबार द्वीप समूह"],
        "ans": 0,
        "sol": "Lakshadweep is the least populous UT in India with a population of 64,473.",
        "sol_hi": "लक्षद्वीप भारत का सबसे कम जनसंख्या वाला केंद्र शासित प्रदेश है, जिसकी आबादी 64,473 है।"
    },
    {
        "q": "Which state in India registered the highest decadal population growth rate during 2001-2011?",
        "q_hi": "2001-2011 के दौरान भारत में किस राज्य ने सर्वाधिक दशकीय जनसंख्या वृद्धि दर दर्ज की थी?",
        "opts": ["Meghalaya", "Bihar", "Arunachal Pradesh", "Mizoram"],
        "opts_hi": ["मेघालय", "बिहार", "अरुणाचल प्रदेश", "मिजोरम"],
        "ans": 0,
        "sol": "Meghalaya registered the highest decadal population growth rate at 27.95% (approx 28.0%).",
        "sol_hi": "मेघालय ने 2001-2011 के दौरान सर्वाधिक दशकीय जनसंख्या वृद्धि दर 27.95% दर्ज की थी।"
    },
    {
        "q": "What is the percentage of Scheduled Castes (SC) in the total population of India as per Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत की कुल जनसंख्या में अनुसूचित जातियों (SC) का प्रतिशत कितना है?",
        "opts": ["16.6%", "8.6%", "14.2%", "20.6%"],
        "opts_hi": ["16.6%", "8.6%", "14.2%", "20.6%"],
        "ans": 0,
        "sol": "Scheduled Castes account for 16.6% of the total population of India.",
        "sol_hi": "जनगणना 2011 के अनुसार अनुसूचित जातियां भारत की कुल जनसंख्या का 16.6% हैं।"
    },
    {
        "q": "In which state is the district of 'Kurung Kumey', which recorded the highest decadal population growth rate among all districts in Census 2011, located?",
        "q_hi": "जनगणना 2011 में सभी जिलों में सर्वाधिक दशकीय जनसंख्या वृद्धि दर दर्ज करने वाला जिला 'कुरंग कुमे' किस राज्य में स्थित है?",
        "opts": ["Nagaland", "Arunachal Pradesh", "Meghalaya", "Mizoram"],
        "opts_hi": ["नागालैंड", "अरुणाचल प्रदेश", "मेघालय", "मिजोरम"],
        "ans": 1,
        "sol": "Kurung Kumey district in Arunachal Pradesh recorded a massive decadal growth rate of 111.01%.",
        "sol_hi": "अरुणाचल प्रदेश का 'कुरंग कुमे' जिला 111.01% की भारी दशकीय वृद्धि दर दर्ज करने वाला जिला था।"
    },
    {
        "q": "According to Census 2011, the average sex ratio of India has increased by how many points since 2001?",
        "q_hi": "जनगणना 2011 के अनुसार भारत के औसत लिंगानुपात में 2001 की तुलना में कितने अंकों की वृद्धि हुई है?",
        "opts": ["5 points", "10 points", "7 points", "12 points"],
        "opts_hi": ["5 अंक", "10 अंक", "7 अंक", "12 अंक"],
        "ans": 1,
        "sol": "The sex ratio increased from 933 in 2001 to 943 in 2011, which is an increase of exactly 10 points.",
        "sol_hi": "लिंगानुपात 2001 के 933 से बढ़कर 2011 में 943 हुआ, जो ठीक 10 अंकों की वृद्धि दर्शाता है।"
    },
    {
        "q": "In Uttar Pradesh, which district has the lowest female literacy rate according to Census 2011?",
        "q_hi": "उत्तर प्रदेश में जनगणना 2011 के अनुसार किस जिले में महिला साक्षरता दर सबसे कम है?",
        "opts": ["Shravasti", "Bahraich", "Balrampur", "Badaun"],
        "opts_hi": ["श्रावस्ती", "बहराइच", "बलरामपुर", "बदायूँ"],
        "ans": 0,
        "sol": "Shravasti has the lowest female literacy rate in UP at 34.78% (overall literacy is 46.74%).",
        "sol_hi": "श्रावस्ती में उत्तर प्रदेश की महिला साक्षरता दर सबसे कम 34.78% है।"
    },
    {
        "q": "Consider the following pairs of districts of UP and their literacy rates:\n1. Gautam Buddha Nagar - 80.12%\n2. Kanpur Nagar - 79.65%\n3. Shravasti - 46.74%\nWhich of the pairs given above are correctly matched?",
        "q_hi": "उत्तर प्रदेश के जिलों और उनकी साक्षरता दर के निम्नलिखित जोड़ों पर विचार करें:\n1. गौतम बुद्ध नगर - 80.12%\n2. कानपुर नगर - 79.65%\n3. श्रावस्ती - 46.74%\nउपरोक्त जोड़ों में से कौन सा/से सही सुमेलित है/हैं?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 3,
        "sol": "All three pairs are correctly matched. Gautam Buddha Nagar has the highest literacy (80.12%), followed by Kanpur Nagar (79.65%), and Shravasti has the lowest (46.74%).",
        "sol_hi": "तीनों जोड़े सही सुमेलित हैं। गौतम बुद्ध नगर में सर्वाधिक साक्षरता (80.12%) है, उसके बाद कानपुर नगर (79.65%) है, और श्रावस्ती में न्यूनतम (46.74%) है।"
    },
    {
        "q": "Which district of Uttar Pradesh has the lowest child sex ratio in Census 2011?",
        "q_hi": "जनगणना 2011 में उत्तर प्रदेश के किस जिले में बाल लिंगानुपात सबसे कम है?",
        "opts": ["Gautam Buddha Nagar", "Baghpat", "Ghaziabad", "Meerut"],
        "opts_hi": ["गौतम बुद्ध नगर", "बागपत", "गाजियाबाद", "मेरठ"],
        "ans": 1,
        "sol": "Baghpat has the lowest child sex ratio (0-6 years) in UP at 841, followed by Gautam Buddha Nagar at 843.",
        "sol_hi": "बागपत में उत्तर प्रदेश का न्यूनतम बाल लिंगानुपात (841) दर्ज किया गया था।"
    },
    {
        "q": "In Uttar Pradesh, which district has the highest proportion (percentage) of Scheduled Tribes (ST) population?",
        "q_hi": "उत्तर प्रदेश में किस जिले में अनुसूचित जनजाति (ST) जनसंख्या का अनुपात (प्रतिशत) सर्वाधिक है?",
        "opts": ["Lalitpur", "Deoria", "Sonbhadra", "Sitapur"],
        "opts_hi": ["ललितपुर", "देवरिया", "सोनभद्र", "सीतापुर"],
        "ans": 2,
        "sol": "Sonbhadra has the highest proportion of Scheduled Tribes population at 20.67% of the district's total population.",
        "sol_hi": "सोनभद्र में अनुसूचित जनजाति (ST) का प्रतिशत सर्वाधिक (20.67%) है।"
    },
    {
        "q": "The decadal growth rate of population in India reached its peak in which Census year?",
        "q_hi": "भारत में जनसंख्या की दशकीय वृद्धि दर किस जनगणना वर्ष में अपने शिखर पर पहुँची थी?",
        "opts": ["1961", "1971", "1981", "1991"],
        "opts_hi": ["1961", "1971", "1981", "1991"],
        "ans": 1,
        "sol": "India's population growth peaked at 24.80% during the 1961-1971 decade, which was recorded in the 1971 Census.",
        "sol_hi": "भारत की दशकीय जनसंख्या वृद्धि दर 1961-1971 के दशक में 24.80% के अपने चरम पर पहुँची थी, जिसे 1971 की जनगणना में दर्ज किया गया था।"
    },
    {
        "q": "Among the following districts of Uttar Pradesh, which one has the highest population density after Ghaziabad?",
        "q_hi": "उत्तर प्रदेश के निम्नलिखित जिलों में से गाजियाबाद के बाद किसका जनसंख्या घनत्व सर्वाधिक है?",
        "opts": ["Varanasi", "Lucknow", "Kanpur Nagar", "Prayagraj"],
        "opts_hi": ["वाराणसी", "लखनऊ", "कानपुर नगर", "प्रयागराज"],
        "ans": 0,
        "sol": "Varanasi has the second-highest population density in UP with 2395 persons per sq km, after Ghaziabad which has 3971.",
        "sol_hi": "गाजियाबाद (3971) के बाद वाराणसी का जनघनत्व उत्तर प्रदेश में दूसरा सबसे अधिक (2395 व्यक्ति प्रति वर्ग किमी) है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which of the following is correct regarding the Census organization in India?",
        "q_hi": "भारत में जनगणना संगठन के संबंध में निम्नलिखित में से कौन सा कथन सही है?",
        "opts": [
            "It is under the Ministry of Human Resource Development",
            "It is under the Ministry of Home Affairs",
            "It is under the Ministry of Statistics and Programme Implementation",
            "It is an independent constitutional body under Article 324"
        ],
        "opts_hi": [
            "यह मानव संसाधन विकास मंत्रालय के अधीन है",
            "यह गृह मंत्रालय के अधीन है",
            "यह सांख्यिकी और कार्यक्रम कार्यान्वयन मंत्रालय के अधीन है",
            "यह अनुच्छेद 324 के तहत एक स्वतंत्र संवैधानिक निकाय है"
        ],
        "ans": 1,
        "sol": "The Office of the Registrar General and Census Commissioner is under the Ministry of Home Affairs, Government of India.",
        "sol_hi": "महारजिस्ट्रार और जनगणना आयुक्त का कार्यालय भारत सरकार के गृह मंत्रालय (Ministry of Home Affairs) के अधीन काम करता है।"
    },
    {
        "q": "The Census Act, under which decadal censuses are conducted in India, was passed in which year?",
        "q_hi": "जनगणना अधिनियम, जिसके तहत भारत में दशकीय जनगणना आयोजित की जाती है, किस वर्ष पारित किया गया था?",
        "opts": ["1947", "1948", "1950", "1955"],
        "opts_hi": ["1947", "1948", "1950", "1955"],
        "ans": 1,
        "sol": "The Census Act was passed in 1948, drafted by Sardar Vallabhbhai Patel, the then Home Minister.",
        "sol_hi": "जनगणना अधिनियम वर्ष 1948 में पारित किया गया था, जिसे तत्कालीन गृह मंत्री सरदार वल्लभभाई पटेल ने तैयार करवाया था।"
    },
    {
        "q": "Which district of India was recorded as the most populous district in Census 2011?",
        "q_hi": "जनगणना 2011 में भारत का कौन सा जिला सबसे अधिक आबादी वाला दर्ज किया गया था?",
        "opts": ["Thane (Maharashtra)", "North 24 Parganas (West Bengal)", "Bengaluru (Karnataka)", "Medinipur (West Bengal)"],
        "opts_hi": ["ठाणे (महाराष्ट्र)", "उत्तर 24 परगना (पश्चिम बंगाल)", "बेंगलुरु (कर्नाटक)", "मेदिनीपुर (पश्चिम बंगाल)"],
        "ans": 0,
        "sol": "Thane district of Maharashtra was the most populous district in India in 2011 with a population of 1.1 crore.",
        "sol_hi": "महाराष्ट्र का ठाणे जिला 2011 में 1.1 करोड़ की आबादी के साथ भारत का सबसे अधिक आबादी वाला जिला दर्ज हुआ था।"
    },
    {
        "q": "Which state has the lowest proportion of rural population (or highest level of urbanisation) by percentage in Census 2011?",
        "q_hi": "जनगणना 2011 में प्रतिशत के हिसाब से किस राज्य में ग्रामीण जनसंख्या का अनुपात सबसे कम (या शहरीकरण का उच्चतम स्तर) है?",
        "opts": ["Tamil Nadu", "Maharashtra", "Goa", "Gujarat"],
        "opts_hi": ["तमिलनाडु", "महाराष्ट्र", "गोवा (Goa)", "गुजरात"],
        "ans": 2,
        "sol": "Goa is the most urbanized state by proportion with 62.2% of its population living in urban areas.",
        "sol_hi": "गोवा 62.2% शहरी आबादी के साथ भारत का सबसे अधिक शहरीकृत राज्य है (अनुपात के मामले में)।"
    },
    {
        "q": "In which census year was the decadal growth rate of India's population highest?",
        "q_hi": "किस जनगणना वर्ष में भारत की जनसंख्या की दशकीय वृद्धि दर सर्वाधिक दर्ज की गई थी?",
        "opts": ["1961", "1971", "1981", "1991"],
        "opts_hi": ["1961", "1971", "1981", "1991"],
        "ans": 1,
        "sol": "The decadal growth rate of population in India reached its historic peak of 24.8% in the 1971 Census.",
        "sol_hi": "भारत की जनसंख्या की दशकीय वृद्धि दर 1971 की जनगणना में अपने ऐतिहासिक शिखर (24.8%) पर पहुँच गई थी।"
    },
    {
        "q": "Which state has the highest Scheduled Tribe (ST) population in terms of percentage to its total state population (excluding UTs)?",
        "q_hi": "राज्यों में (UT को छोड़कर) किस राज्य में उसकी कुल आबादी के प्रतिशत के रूप में सर्वाधिक अनुसूचित जनजाति (ST) जनसंख्या है?",
        "opts": ["Nagaland", "Mizoram", "Meghalaya", "Arunachal Pradesh"],
        "opts_hi": ["नागालैंड", "मिजोरम (Mizoram)", "मेघालय", "अरुणाचल प्रदेश"],
        "ans": 1,
        "sol": "Among states, Mizoram has the highest proportion of ST population at 94.4%, followed by Nagaland at 86.5%.",
        "sol_hi": "राज्यों में मिजोरम में सर्वाधिक अनुसूचित जनजाति (ST) आबादी (94.4%) है, उसके बाद नागालैंड का स्थान 86.5% के साथ आता है।"
    },
    {
        "q": "What is the ranking of India in terms of global population size according to Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार वैश्विक जनसंख्या के मामले में भारत का कौन सा स्थान था?",
        "opts": ["First", "Second", "Third", "Fourth"],
        "opts_hi": ["पहला", "दूसरा (Second)", "तीसरा", "चौथा"],
        "ans": 1,
        "sol": "As of 2011, India ranked second in global population size, with China being the most populous country.",
        "sol_hi": "वर्ष 2011 तक, भारत वैश्विक जनसंख्या आकार के मामले में दूसरे स्थान पर था, जबकि चीन सर्वाधिक जनसंख्या वाला देश था।"
    },
    {
        "q": "The child population (0-6 years) accounts for what percentage of total population in Census 2011?",
        "q_hi": "जनगणना 2011 में बाल जनसंख्या (0-6 वर्ष) कुल जनसंख्या का कितना प्रतिशत है?",
        "opts": ["15.6%", "13.6%", "12.8%", "14.2%"],
        "opts_hi": ["15.6%", "13.6%", "12.8%", "14.2%"],
        "ans": 1,
        "sol": "The child population (0-6 years) is 13.6% of the total population of India in Census 2011.",
        "sol_hi": "जनगणना 2011 में बाल जनसंख्या (0-6 वर्ष) भारत की कुल जनसंख्या का 13.6% है।"
    },
    {
        "q": "Which state has the lowest literacy rate among women in India according to Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार भारत में महिलाओं में सबसे कम साक्षरता दर किस राज्य में है?",
        "opts": ["Rajasthan", "Bihar", "Jharkhand", "Uttar Pradesh"],
        "opts_hi": ["राजस्थान", "बिहार (Bihar)", "झारखंड", "उत्तर प्रदेश"],
        "ans": 1,
        "sol": "Bihar has the lowest female literacy rate at 51.5%. (Rajasthan female literacy is 52.1%).",
        "sol_hi": "बिहार में महिला साक्षरता दर सबसे कम 51.5% है (राजस्थान में यह 52.1% है)।"
    },
    {
        "q": "The highest sex ratio UT according to Census 2011 is:",
        "q_hi": "जनगणना 2011 के अनुसार सर्वाधिक लिंगानुपात वाला केंद्र शासित प्रदेश है:",
        "opts": ["Andaman and Nicobar Islands", "Lakshadweep", "Puducherry", "Delhi"],
        "opts_hi": ["अंडमान और निकोबार द्वीप समूह", "लक्षद्वीप", "पुदुचेरी (Puducherry)", "दिल्ली"],
        "ans": 2,
        "sol": "Puducherry has the highest sex ratio among UTs with 1037 females per 1000 males.",
        "sol_hi": "पुदुचेरी का लिंगानुपात केंद्र शासित प्रदेशों में सर्वाधिक (1037) है।"
    },
    {
        "q": "Which of the following states has NO Scheduled Caste (SC) population?",
        "q_hi": "निम्नलिखित में से किस राज्य में कोई अनुसूचित जाति (SC) जनसंख्या नहीं है?",
        "opts": ["Arunachal Pradesh and Nagaland", "Punjab", "Haryana", "Goa"],
        "opts_hi": ["अरुणाचल प्रदेश और नागालैंड", "पंजाब", "हरियाणा", "गोवा"],
        "ans": 0,
        "sol": "Arunachal Pradesh, Nagaland, Lakshadweep, and Andaman & Nicobar have no Scheduled Castes population.",
        "sol_hi": "अरुणाचल प्रदेश और नागालैंड (साथ ही लक्षद्वीप और अंडमान एवं निकोबार) में कोई अनुसूचित जाति (SC) जनसंख्या नहीं है।"
    },
    {
        "q": "What was the population density of Uttar Pradesh in Census 2011?",
        "q_hi": "जनगणना 2011 में उत्तर प्रदेश का जनसंख्या घनत्व कितना था?",
        "opts": ["689", "829", "789", "859"],
        "opts_hi": ["689", "829", "789", "859"],
        "ans": 1,
        "sol": "The population density of Uttar Pradesh is 829 persons per square kilometer.",
        "sol_hi": "उत्तर प्रदेश का जनसंख्या घनत्व 829 व्यक्ति प्रति वर्ग किलोमीटर है।"
    },
    {
        "q": "Which UT has the highest child sex ratio (0-6 years) in Census 2011?",
        "q_hi": "जनगणना 2011 में किस केंद्र शासित प्रदेश का बाल लिंगानुपात (0-6 वर्ष) सर्वाधिक है?",
        "opts": ["Delhi", "Puducherry", "Andaman and Nicobar Islands", "Lakshadweep"],
        "opts_hi": ["दिल्ली", "पुदुचेरी", "अंडमान और निकोबार द्वीप समूह", "लक्षद्वीप"],
        "ans": 2,
        "sol": "Andaman and Nicobar Islands has the highest child sex ratio among UTs (968), and Mizoram (970) has the highest among states.",
        "sol_hi": "अंडमान और निकोबार का बाल लिंगानुपात केंद्र शासित प्रदेशों में सर्वाधिक (968) है। राज्यों में मिजोरम (970) शीर्ष पर है।"
    },
    {
        "q": "The district with the lowest literacy rate in India in Census 2011 was:",
        "q_hi": "जनगणना 2011 में भारत का सबसे कम साक्षरता दर वाला जिला कौन सा था?",
        "opts": ["Alirajpur (Madhya Pradesh)", "Dantewada (Chhattisgarh)", "Shravasti (Uttar Pradesh)", "Nuh (Haryana)"],
        "opts_hi": ["अलीराजपुर (मध्य प्रदेश)", "दंतेवाड़ा (छत्तीसगढ़)", "श्रावस्ती (उत्तर प्रदेश)", "नुह (हरियाणा)"],
        "ans": 0,
        "sol": "Alirajpur district in Madhya Pradesh registered the lowest literacy rate in India at 36.1%.",
        "sol_hi": "मध्य प्रदेश का अलीराजपुर जिला 36.1% के साथ भारत में सबसे कम साक्षरता दर वाला जिला दर्ज किया गया था।"
    },
    {
        "q": "What is the ranking of Bihar in terms of population size according to Census 2011?",
        "q_hi": "जनगणना 2011 के अनुसार जनसंख्या के आकार में बिहार का कौन सा स्थान है?",
        "opts": ["First", "Second", "Third", "Fourth"],
        "opts_hi": ["पहला", "दूसरा", "तीसरा (Third)", "चौथा"],
        "ans": 2,
        "sol": "Bihar ranks third in terms of population size (10.40 crore), after Uttar Pradesh (first) and Maharashtra (second).",
        "sol_hi": "उत्तर प्रदेश (प्रथम) और महाराष्ट्र (द्वितीय) के बाद बिहार जनसंख्या के आकार में तीसरे स्थान (10.40 करोड़) पर आता है।"
    }
]

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Review national and UP-specific population density, growth, literacy, sex ratio, and SC/ST distributions.", "sections": deep_dive_en}
    }

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Basic Profile & History",
                "masteryZone": [
                    {"type": "MCQ", "q": "What was the motto of the 2011 Census?", "opts": ["Our Progress, Our Pride", "Our Census, Our Future", "One Nation, One Record", "Modernizing Demographics"], "ans": 1, "sol": "The motto was 'Our Census, Our Future'."},
                    {"type": "MCQ", "q": "In which year was the first synchronous census conducted in India?", "opts": ["1872", "1881", "1901", "1951"], "ans": 1, "sol": "The first synchronous census was conducted in 1881 under Lord Ripon."},
                    {"type": "True/False", "q": "True or False: The year 1921 is known as the 'Year of the Great Divide' due to negative growth.", "ans": True, "sol": "True. 1921 recorded a negative growth rate of -0.31%."},
                    {"type": "One-Liner", "q": "Who was the Census Commissioner of India in 2011?", "sol": "C. Chandramouli"}
                ]
            },
            {
                "title": "2. National Indicators",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which state has the highest population density?", "opts": ["West Bengal", "Kerala", "Bihar", "Uttar Pradesh"], "ans": 2, "sol": "Bihar has the highest density at 1106 persons per sq km."},
                    {"type": "MCQ", "q": "Which state has the highest proportion of rural population?", "opts": ["Bihar", "Himachal Pradesh", "Odisha", "Assam"], "ans": 1, "sol": "Himachal Pradesh is 90% rural by proportion."},
                    {"type": "True/False", "q": "True or False: The national average population density in 2011 was 382.", "ans": True, "sol": "True. India's population density rose to 382 persons per sq km."},
                    {"type": "MCQ", "q": "Which UT has the highest literacy rate in India?", "opts": ["Chandigarh", "Lakshadweep", "Puducherry", "Daman & Diu"], "ans": 1, "sol": "Lakshadweep has the highest literacy among UTs at 91.85%."}
                ]
            },
            {
                "title": "3. Uttar Pradesh Census Stats",
                "masteryZone": [
                    {"type": "MCQ", "q": "What is the population density of Uttar Pradesh?", "opts": ["689", "829", "789", "912"], "ans": 1, "sol": "UP's population density is 829 persons per sq km."},
                    {"type": "MCQ", "q": "What is the literacy rate of Uttar Pradesh?", "opts": ["57.2%", "67.7%", "77.3%", "64.6%"], "ans": 1, "sol": "UP's literacy rate is 67.68% (approx. 67.7%)."},
                    {"type": "True/False", "q": "True or False: UP's child sex ratio (902) is lower than its general sex ratio (912).", "ans": True, "sol": "True. UP's child sex ratio is 902, while general sex ratio is 912."},
                    {"type": "One-Liner", "q": "What is the gender gap in literacy rate in UP?", "sol": "20.1%"}
                ]
            },
            {
                "title": "4. UP District Rankings",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which district of UP has the highest sex ratio?", "opts": ["Jaunpur", "Azamgarh", "Deoria", "Gautam Buddha Nagar"], "ans": 0, "sol": "Jaunpur has the highest sex ratio in UP at 1024."},
                    {"type": "MCQ", "q": "Which district of UP has the lowest literacy rate?", "opts": ["Bahraich", "Shravasti", "Balrampur", "Mahoba"], "ans": 1, "sol": "Shravasti has the lowest literacy rate at 46.74%."},
                    {"type": "True/False", "q": "True or False: Prayagraj is the most populous district in Uttar Pradesh.", "ans": True, "sol": "True. Prayagraj is the most populous district with ~59.5 lakh people."},
                    {"type": "True/False", "q": "True or False: Sonbhadra has the highest density in UP.", "ans": False, "sol": "False. Sonbhadra has low density (270). Ghaziabad has the highest density (3971)."}
                ]
            }
        ]
    }

def build_theory_hi():
    return {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "राष्ट्रीय और उत्तर प्रदेश-विशिष्ट जनघनत्व, दशकीय वृद्धि, साक्षरता, लिंगानुपात और एससी/एसटी वितरण की समीक्षा करें।", "sections": deep_dive_hi}
    }

def build_practice_hi():
    practice_obj = {
        "practiceQuestions": [
            {"q": pq["q_hi"], "opts": pq["opts_hi"], "ans": pq["ans"], "sol": pq["sol_hi"]} for pq in practice_questions
        ],
        "mockTestQuestions": [
            {"q": mtq["q_hi"], "opts": mtq["opts_hi"], "ans": mtq["ans"], "sol": mtq["sol_hi"]} for mtq in mock_test_questions
        ]
    }
    return practice_obj

def build_mastery_hi():
    return {
        "sections": [
            {
                "title": "1. मूल जनसांख्यिकी और इतिहास",
                "masteryZone": [
                    {"type": "MCQ", "q": "जनगणना 2011 का आधिकारिक नारा क्या था?", "opts": ["हमारा गौरव, हमारी जनगणना", "हमारी जनगणना, हमारा भविष्य", "एक देश, एक रिकॉर्ड", "आधुनिक जनसांख्यिकी"], "ans": 1, "sol": "नारा 'हमारी जनगणना, हमारा भविष्य' था।"},
                    {"type": "MCQ", "q": "भारत में पहली समकालिक जनगणना किस वर्ष आयोजित की गई थी?", "opts": ["1872", "1881", "1901", "1951"], "ans": 1, "sol": "पहली समकालिक जनगणना 1881 में लॉर्ड रिपन के अधीन आयोजित की गई थी।"},
                    {"type": "True/False", "q": "सही या गलत: वर्ष 1921 को नकारात्मक दशकीय वृद्धि के कारण 'महान विभाजक वर्ष' कहा जाता है।", "ans": True, "sol": "सही। 1921 में नकारात्मक वृद्धि दर -0.31% दर्ज हुई थी।"},
                    {"type": "One-Liner", "q": "2011 में भारत के जनगणना आयुक्त कौन थे?", "sol": "सी. चंद्रमौली"}
                ]
            },
            {
                "title": "2. राष्ट्रीय संकेतक",
                "masteryZone": [
                    {"type": "MCQ", "q": "किस राज्य में जनसंख्या घनत्व सबसे अधिक है?", "opts": ["पश्चिम बंगाल", "केरल", "बिहार", "उत्तर प्रदेश"], "ans": 2, "sol": "बिहार का जनघनत्व सर्वाधिक (1106 व्यक्ति प्रति वर्ग किमी) है।"},
                    {"type": "MCQ", "q": "किस राज्य में ग्रामीण जनसंख्या का प्रतिशत सबसे अधिक है?", "opts": ["बिहार", "हिमाचल प्रदेश", "ओडिशा", "असम"], "ans": 1, "sol": "हिमाचल प्रदेश में ग्रामीण जनसंख्या का अनुपात सर्वाधिक (90.0%) है।"},
                    {"type": "True/False", "q": "सही या गलत: 2011 में भारत का औसत जनसंख्या घनत्व 382 व्यक्ति/वर्ग किमी था।", "ans": True, "sol": "सही। भारत का जनघनत्व 382 व्यक्ति प्रति वर्ग किमी था।"},
                    {"type": "MCQ", "q": "भारत के किस केंद्र शासित प्रदेश की साक्षरता दर सबसे अधिक है?", "opts": ["चंडीगढ़", "लक्षद्वीप", "पुदुचेरी", "दमन और दीव"], "ans": 1, "sol": "लक्षद्वीप की साक्षरता दर केंद्र शासित प्रदेशों में सर्वाधिक (91.85%) है।"}
                ]
            },
            {
                "title": "3. उत्तर प्रदेश जनगणना आंकड़े",
                "masteryZone": [
                    {"type": "MCQ", "q": "उत्तर प्रदेश का जनसंख्या घनत्व कितना है?", "opts": ["689", "829", "789", "912"], "ans": 1, "sol": "उत्तर प्रदेश का जनघनत्व 829 व्यक्ति प्रति वर्ग किमी है।"},
                    {"type": "MCQ", "q": "उत्तर प्रदेश की साक्षरता दर कितनी है?", "opts": ["57.2%", "67.7%", "77.3%", "64.6%"], "ans": 1, "sol": "उत्तर प्रदेश की साक्षरता दर 67.68% (लगभग 67.7%) है।"},
                    {"type": "True/False", "q": "सही या गलत: यूपी का बाल लिंगानुपात (902) इसके सामान्य लिंगानुपात (912) से कम है।", "ans": True, "sol": "सही। यूपी का बाल लिंगानुपात 902 है, जबकि सामान्य लिंगानुपात 912 है।"},
                    {"type": "One-Liner", "q": "यूपी में साक्षरता दर में महिला-पुरुष अंतर कितना है?", "sol": "20.1%"}
                ]
            },
            {
                "title": "4. यूपी जिलावार रैंकिंग",
                "masteryZone": [
                    {"type": "MCQ", "q": "उत्तर प्रदेश के किस जिले का लिंगानुपात सर्वाधिक है?", "opts": ["जौनपुर", "आज़मगढ़", "देवरिया", "गौतम बुद्ध नगर"], "ans": 0, "sol": "जौनपुर का लिंगानुपात उत्तर प्रदेश में सर्वाधिक 1024 है।"},
                    {"type": "MCQ", "q": "उत्तर प्रदेश के किस जिले की साक्षरता दर सबसे कम है?", "opts": ["बहराइच", "श्रावस्ती", "बलरामपुर", "महोबा"], "ans": 1, "sol": "श्रावस्ती की साक्षरता दर सबसे कम 46.74% है।"},
                    {"type": "True/False", "q": "सही या गलत: प्रयागराज उत्तर प्रदेश का सर्वाधिक जनसंख्या वाला जिला है।", "ans": True, "sol": "सही। प्रयागराज लगभग 59.5 लाख आबादी के साथ सर्वाधिक जनसंख्या वाला जिला है।"},
                    {"type": "True/False", "q": "सही या गलत: सोनभद्र में उत्तर प्रदेश का सर्वाधिक जनघनत्व है।", "ans": False, "sol": "गलत। सोनभद्र का जनघनत्व कम (270) है। गाजियाबाद का जनघनत्व सर्वाधिक (3971) है।"}
                ]
            }
        ]
    }

# ----------------- FILE GENERATION -----------------
import re

def parse_markdown(data):
    if isinstance(data, str):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: #e67e22; font-weight: 700;">\1</strong>', data)
    elif isinstance(data, dict):
        return {k: parse_markdown(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parse_markdown(item) for item in data]
    return data

def write_json(filepath, data):
    formatted_data = parse_markdown(data)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(formatted_data, f, indent=2, ensure_ascii=False)
    print(f"Written: {filepath}")

# Write English files
write_json(os.path.join(BASE_DIR, "theory.json"), build_theory())
write_json(os.path.join(BASE_DIR, "practice.json"), build_practice())
write_json(os.path.join(BASE_DIR, "mastery.json"), build_mastery())

# Write Hindi files
write_json(os.path.join(HI_DIR, "theory.json"), build_theory_hi())
write_json(os.path.join(HI_DIR, "practice.json"), build_practice_hi())
write_json(os.path.join(HI_DIR, "mastery.json"), build_mastery_hi())
