# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

TOPIC = "major-universities-institutes"
TOPIC_DISPLAY = "Major Universities and Institutes"
TOPIC_DISPLAY_HI = "प्रमुख विश्वविद्यालय और संस्थान"

BASE_DIR = rf"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\up-special-knowledge\{TOPIC}"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "UP Special Knowledge",
    "parentUrl": "../",
    "current": "Universities & Institutes"
}

hero_en = {
    "title": "Major Universities and Research Institutes of UP",
    "description": "Comprehensive guide to Uttar Pradesh's premier educational institutions, central universities, and top-tier research institutes (like CDRI, IIVR, IIPR, and IGFRI) frequently asked in UPPSC and AHC RO/ARO exams."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Universities & Institutes Mock Test",
        "description": "Test your knowledge on the founding years of central universities, locations of specialized research centers, and agricultural universities in UP. Timed 15-question mock test.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Establishment Timeline of Central Universities in UP",
    "description": "Founding milestones of the 6 Central Universities of Uttar Pradesh.",
    "cards": [
        {
            "period": "University of Allahabad",
            "date": "1887",
            "details": "Known as the **Oxford of the East**. Established as a central university in 2005 but originally founded in 1887."
        },
        {
            "period": "Banaras Hindu University",
            "date": "1916",
            "details": "Founded by **Pandit Madan Mohan Malaviya** under the BHU Act 1915, representing a landmark in national higher education."
        },
        {
            "period": "Aligarh Muslim University",
            "date": "1920",
            "details": "Evolved from the Muhammadan Anglo-Oriental (MAO) College founded by **Sir Syed Ahmad Khan** in 1875."
        },
        {
            "period": "Babasaheb Bhimrao Ambedkar University",
            "date": "1996",
            "details": "Established in Lucknow to promote higher learning for marginalized sections of society."
        },
        {
            "period": "Rajiv Gandhi National Aviation University",
            "date": "2013",
            "details": "India's first aviation university established at Fursatganj, Amethi district."
        },
        {
            "period": "Rani Lakshmi Bai Central Agricultural University",
            "date": "2014",
            "details": "Established in Jhansi as a premier institute for agricultural studies in the Bundelkhand region."
        }
    ]
}

mnemonics_en = {
    "title": "Recall Mnemonics",
    "description": "Memory hooks to associate research institutes with their correct cities.",
    "items": [
        {
            "title": "Mnemonic 1: Lucknow's Specialized Institutes",
            "phrase": "\"D-B-M-S-T (Drug - Botanical - Medicinal - Sugarcane - Toxicology)\"",
            "decryption": "Lucknow hosts a cluster of national institutes:<br>• **D** — Central **D**rug Research Institute (CDRI)<br>• **B** — National **B**otanical Research Institute (NBRI)<br>• **M** — Central Institute of **M**edicinal and Aromatic Plants (CIMAP)<br>• **S** — Indian Institute of **S**ugarcane Research (IISR)<br>• **T** — Indian Institute of **T**oxicology Research (IITR)"
        },
        {
            "title": "Mnemonic 2: Kanpur's Industrial Centers",
            "phrase": "\"S-P-L (Sugar - Pulses - Leather)\"",
            "decryption": "Kanpur's major national and state centers:<br>• **S** — National **S**ugar Institute (NSI)<br>• **P** — Indian Institute of **P**ulses Research (IIPR)<br>• **L** — Government **L**eather Institute"
        },
        {
            "title": "Mnemonic 3: Jhansi's Agricultural Focus",
            "phrase": "\"G-A (Grassland - Agroforestry)\"",
            "decryption": "Jhansi, in Bundelkhand, focuses on dryland farming research:<br>• **G** — Indian **G**rassland and Fodder Research Institute (IGFRI)<br>• **A** — Central **A**groforestry Research Institute (CAFRI)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "Where is the Indian Institute of Vegetable Research (IIVR) located?",
            "answer": "**Shahanshahpur, Varanasi**. (Established in 1999 to boost vegetable crop research).",
            "icon": "fa-carrot"
        },
        {
            "question": "Which is the oldest state university in Uttar Pradesh?",
            "answer": "**University of Lucknow** (established in 1921) or **Chhatrapati Shahu Ji Maharaj University** (formerly Agra University founded in 1927). For state-funded universities, Lucknow is among the oldest, alongside Agra.",
            "icon": "fa-university"
        },
        {
            "question": "Where is the Central Institute for Research on Goats (CIRG) located?",
            "answer": "**Makhdoom, Mathura**.",
            "icon": "fa-hippo"
        },
        {
            "question": "Which institute in UP is dedicated to the carpet industry, and where is it?",
            "answer": "The **Indian Institute of Carpet Technology (IICT)**, located in **Bhadohi** (known as the Carpet City).",
            "icon": "fa-scroll"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing the National Sugar Institute (NSI) with the Indian Institute of Sugarcane Research (IISR). The **National Sugar Institute (NSI)** is in **Kanpur**, whereas the **Indian Institute of Sugarcane Research (IISR)** is in **Lucknow**.",
        "<strong>Trap 2:</strong> Mistaking the founding year of the University of Allahabad. It was founded in **1887** (making it the 4th oldest modern university in India), but it was granted **Central University status in 2005**.",
        "<strong>Trap 3:</strong> Confusing the locations of veterinary research. The **Indian Veterinary Research Institute (IVRI)** is in **Izatnagar, Bareilly**, but the **Central Institute for Research on Goats (CIRG)** is in **Makhdoom, Mathura**.",
        "<strong>Trap 4:</strong> Assuming BHU was founded solely by Madan Mohan Malaviya. While he was the key driver, he co-founded it with **Dr. Annie Besant** and **Darbhanga Maharaja Rameshwar Singh Bahadur** in 1916."
    ]
}

deep_dive_en = [
    {
        "title": "1. Central & State Universities in Uttar Pradesh",
        "content": """<p>Uttar Pradesh has a vast higher education network, including **6 Central Universities** (highest among states along with Delhi) and numerous state-funded universities:</p>
        
        <h3>A. The Six Central Universities</h3>
        <ul>
          <li><strong>University of Allahabad (Prayagraj):</strong> Founded in **1887** by Sir William Muir. Earning the title **'Oxford of the East'** due to its academic prestige. It became a Central University in **2005**.</li>
          <li><strong>Banaras Hindu University (BHU, Varanasi):</strong> Founded in **1916** by Pandit Madan Mohan Malaviya, Annie Besant, and Maharaja Rameshwar Singh. It is one of the largest residential universities in Asia.</li>
          <li><strong>Aligarh Muslim University (AMU, Aligarh):</strong> Evolved from the **Muhammadan Anglo-Oriental (MAO) College** founded in **1875** by Sir Syed Ahmad Khan. It was incorporated as a university in **1920**.</li>
          <li><strong>Babasaheb Bhimrao Ambedkar University (BBAU, Lucknow):</strong> Established in **1996** as a central university.</li>
          <li><strong>Rajiv Gandhi National Aviation University (RGNAU, Amethi):</strong> Established in **2013** at Fursatganj as a specialized central university for aviation studies.</li>
          <li><strong>Rani Lakshmi Bai Central Agricultural University (RLBCAU, Jhansi):</strong> Established in **2014** by an Act of Parliament to address agricultural research in the Bundelkhand region.</li>
        </ul>

        <h3>B. Key State and Specialized Universities</h3>
        <ul>
          <li><strong>Lucknow University:</strong> Established in **1921**.</li>
          <li><strong>Dr. Bhimrao Ambedkar University (Agra):</strong> Founded in **1927** as Agra University. Bounded historically by many old colleges of North India.</li>
          <li><strong>Chaudhary Charan Singh University (Meerut):</strong> Established in **1965** as Meerut University, later renamed after the former Prime Minister.</li>
          <li><strong>Deen Dayal Upadhyaya Gorakhpur University:</strong> Established in **1957**.</li>
          <li><strong>Bhatkhande Sanskriti Vishwavidyalaya (Lucknow):</strong> Evolved from the Bhatkhande Music Institute (originally Marris College of Music, founded in **1926** by Vishnu Narayan Bhatkhande). It was declared a deemed university in 2000 and a state cultural university in 2022.</li>
        </ul>"""
    },
    {
        "title": "2. National & Central Research Institutes of UP",
        "content": """<p>UP hosts a significant number of CSIR, ICAR, and ICMR laboratories. These are highly tested in matching-type questions in AHC RO/ARO exams:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>City Location</th>
                <th>Institute Name</th>
                <th>Abbreviation</th>
                <th>Key Focus Area</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="5"><strong>Lucknow</strong></td>
                <td>Central Drug Research Institute</td>
                <td>CDRI</td>
                <td>Pharmaceutical and drug discovery research.</td>
              </tr>
              <tr>
                <td>National Botanical Research Institute</td>
                <td>NBRI</td>
                <td>Plant taxonomy, biotechnology, and conservation.</td>
              </tr>
              <tr>
                <td>Central Institute of Medicinal and Aromatic Plants</td>
                <td>CIMAP</td>
                <td>Research on essential oils and aromatic plants.</td>
              </tr>
              <tr>
                <td>Indian Institute of Sugarcane Research</td>
                <td>IISR</td>
                <td>Sugarcane cultivation technology and pathology.</td>
              </tr>
              <tr>
                <td>Indian Institute of Toxicology Research</td>
                <td>IITR (ITRC)</td>
                <td>Industrial toxicology and environmental health.</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>Kanpur</strong></td>
                <td>Indian Institute of Pulses Research</td>
                <td>IIPR</td>
                <td>Pulses breeding and crop protection.</td>
              </tr>
              <tr>
                <td>National Sugar Institute</td>
                <td>NSI</td>
                <td>Sugar technology, engineering, and chemical analysis.</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>Jhansi</strong></td>
                <td>Indian Grassland and Fodder Research Institute</td>
                <td>IGFRI</td>
                <td>Fodder crop production and grassland management.</td>
              </tr>
              <tr>
                <td>Central Agroforestry Research Institute</td>
                <td>CAFRI</td>
                <td>Agroforestry systems for semi-arid zones.</td>
              </tr>
              <tr>
                <td><strong>Varanasi</strong></td>
                <td>Indian Institute of Vegetable Research</td>
                <td>IIVR</td>
                <td>Vegetable breeding, post-harvest, and pathology.</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>Izatnagar (Bareilly)</strong></td>
                <td>Indian Veterinary Research Institute</td>
                <td>IVRI</td>
                <td>Animal health, vaccines, and veterinary medicine.</td>
              </tr>
              <tr>
                <td>Central Avian Research Institute</td>
                <td>CARI</td>
                <td>Poultry breeding, nutrition, and management.</td>
              </tr>
              <tr>
                <td><strong>Bhadohi</strong></td>
                <td>Indian Institute of Carpet Technology</td>
                <td>IICT</td>
                <td>Carpet weaving, design, and textile technology.</td>
              </tr>
              <tr>
                <td><strong>Mathura</strong></td>
                <td>Central Institute for Research on Goats</td>
                <td>CIRG</td>
                <td>Goat husbandry, nutrition, and disease control.</td>
              </tr>
              <tr>
                <td><strong>Noida / Greater Noida</strong></td>
                <td>V.V. Giri National Labour Institute</td>
                <td>VVGNLI</td>
                <td>Labor studies, policy research, and training.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. Agricultural & Medical Universities",
        "content": """<p>Specialized sectoral universities in agricultural and medical sciences in UP:</p>
        
        <h3>A. Agricultural Universities</h3>
        <ul>
          <li><strong>Chandra Shekhar Azad (CSA) University of Agriculture & Technology (Kanpur):</strong> Established in **1975**, named after freedom fighter Chandra Shekhar Azad.</li>
          <li><strong>Acharya Narendra Deva University of Agriculture & Technology (Ayodhya):</strong> Founded in **1975** (originally at Kumarganj).</li>
          <li><strong>Sardar Vallabhbhai Patel University of Agriculture & Technology (Meerut):</strong> Established in **2000**.</li>
          <li><strong>Banda University of Agriculture & Technology (Banda):</strong> Established in **2010** to address the dry Bundelkhand farming requirements.</li>
          <li><strong>Sam Higginbottom University of Agriculture, Technology and Sciences (SHUATS, Prayagraj):</strong> Evolved from the Allahabad Agricultural Institute founded in **1910** by Sam Higginbottom. Granted deemed university status in 2000.</li>
        </ul>

        <h3>B. Prominent Medical Universities & Institutes</h3>
        <ul>
          <li><strong>King George's Medical University (KGMU, Lucknow):</strong> Evolved from King George's Medical College founded in **1911**. Upgraded to a state university in **2002**.</li>
          <li><strong>Sanjay Gandhi Postgraduate Institute of Medical Sciences (SGPGIMS, Lucknow):</strong> Established in **1983** as a premier super-specialty medical institute.</li>
          <li><strong>Uttar Pradesh University of Medical Sciences (Saifai, Etawah):</strong> Established in **2016** (originally UP Rural Institute of Medical Sciences and Research).</li>
        </ul>"""
    }
]

# ----------------- HINDI DATA DEFINITIONS -----------------
breadcrumbs_hi = {
    "parent": "यूपी विशेष ज्ञान",
    "parentUrl": "../",
    "current": "विश्वविद्यालय और संस्थान"
}

hero_hi = {
    "title": "उत्तर प्रदेश के प्रमुख विश्वविद्यालय और अनुसंधान संस्थान",
    "description": "उत्तर प्रदेश के प्रमुख केंद्रीय विश्वविद्यालयों, राज्य विश्वविद्यालयों और राष्ट्रीय स्तर के अनुसंधान संस्थानों (जैसे CDRI, IIVR, IIPR, और IGFRI) की विस्तृत सूची, जो परीक्षाओं में बार-बार पूछी जाती है।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "इंटरएक्टिव विश्वविद्यालय और संस्थान मॉक टेस्ट",
        "description": "केंद्रीय विश्वविद्यालयों के स्थापना वर्ष, विशिष्ट अनुसंधान केंद्रों के स्थान और कृषि विश्वविद्यालयों पर आधारित 15-प्रश्न मॉक टेस्ट।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "यूपी में केंद्रीय विश्वविद्यालयों का स्थापना कालक्रम",
    "description": "उत्तर प्रदेश में स्थित 6 केंद्रीय विश्वविद्यालयों के स्थापना मील के पत्थर।",
    "cards": [
        {
            "period": "इलाहाबाद विश्वविद्यालय",
            "date": "1887",
            "details": "इसे **पूर्व का ऑक्सफोर्ड (Oxford of the East)** कहा जाता है। इसे 2005 में केंद्रीय विश्वविद्यालय का दर्जा मिला, लेकिन इसकी मूल स्थापना 1887 में हुई थी।"
        },
        {
            "period": "बनारस हिंदू विश्वविद्यालय",
            "date": "1916",
            "details": "महामना **पंडित मदन मोहन मालवीय** द्वारा बनारस हिंदू विश्वविद्यालय अधिनियम 1915 के तहत स्थापित किया गया।"
        },
        {
            "period": "अलीगढ़ मुस्लिम विश्वविद्यालय",
            "date": "1920",
            "details": "सर **सैयद अहमद खान** द्वारा 1875 में स्थापित 'मुहम्मडन एंग्लो-ओरिएंटल (MAO) कॉलेज' से विकसित हुआ।"
        },
        {
            "period": "बाबासाहेब भीमराव अंबेडकर विश्वविद्यालय",
            "date": "1996",
            "details": "वंचित वर्गों की उच्च शिक्षा को बढ़ावा देने के लिए लखनऊ में केंद्रीय विश्वविद्यालय के रूप में स्थापित किया गया।"
        },
        {
            "period": "राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय",
            "date": "2013",
            "details": "विमानन अध्ययन के लिए भारत का पहला विशिष्ट केंद्रीय विश्वविद्यालय फुर्सतगंज (अमेठी जिला) में स्थापित हुआ।"
        },
        {
            "period": "रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय",
            "date": "2014",
            "details": "बुंदेलखंड क्षेत्र में कृषि शिक्षा को बढ़ावा देने के लिए झांसी में स्थापित किया गया।"
        }
    ]
}

mnemonics_hi = {
    "title": "याद रखने की ट्रिक्स (Mnemonics)",
    "description": "विभिन्न शहरों के संस्थानों को आसानी से याद रखने की ट्रिक्स।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: लखनऊ के प्रमुख संस्थान",
            "phrase": "\"D-B-M-S-T\"",
            "decryption": "लखनऊ में स्थित प्रमुख राष्ट्रीय संस्थान:<br>• **D** — केंद्रीय औषधि अनुसंधान संस्थान (Drug - CDRI)<br>• **B** — राष्ट्रीय वनस्पति अनुसंधान संस्थान (Botanical - NBRI)<br>• **M** — केंद्रीय औषधीय एवं सुगंधित पौधा संस्थान (Medicinal - CIMAP)<br>• **S** — भारतीय गन्ना अनुसंधान संस्थान (Sugarcane - IISR)<br>• **T** — भारतीय विषविज्ञान अनुसंधान संस्थान (Toxicology - IITR)"
        },
        {
            "title": "स्मृति सूत्र 2: कानपुर के प्रमुख केंद्र",
            "phrase": "\"S-P-L (चीनी - दलहन - चमड़ा)\"",
            "decryption": "कानपुर के औद्योगिक और अनुसंधान संस्थान:<br>• **S** — राष्ट्रीय शर्करा संस्थान (Sugar - NSI)<br>• **P** — भारतीय दलहन अनुसंधान संस्थान (Pulses - IIPR)<br>• **L** — राजकीय चमड़ा संस्थान (Leather)"
        },
        {
            "title": "स्मृति सूत्र 3: झांसी के कृषि अनुसंधान",
            "phrase": "\"G-A (घास - कृषि वानिकी)\"",
            "decryption": "बुंदेलखंड के केंद्र झांसी में स्थित अनुसंधान संस्थान:<br>• **G** — भारतीय चारागाह एवं चारा अनुसंधान संस्थान (Grassland - IGFRI)<br>• **A** — केंद्रीय कृषि वानिकी अनुसंधान संस्थान (Agroforestry - CAFRI)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "भारतीय शाक-भाजी (सब्जी) अनुसंधान संस्थान (IIVR) कहाँ स्थित है?",
            "answer": "**शहंशाहपुर, वाराणसी**। (इसकी स्थापना 1999 में हुई थी)।",
            "icon": "fa-carrot"
        },
        {
            "question": "उत्तर प्रदेश का सबसे पुराना राज्य विश्वविद्यालय कौन सा है?",
            "answer": "**लखनऊ विश्वविद्यालय** (स्थापना 1921) या **डॉ. भीमराव अंबेडकर विश्वविद्यालय, आगरा** (पूर्व में आगरा विश्वविद्यालय, स्थापना 1927)।",
            "icon": "fa-university"
        },
        {
            "question": "केंद्रीय बकरी अनुसंधान संस्थान (CIRG) कहाँ स्थित है?",
            "answer": "**मखदूम, मथुरा**।",
            "icon": "fa-hippo"
        },
        {
            "question": "कालीन उद्योग को समर्पित 'भारतीय कालीन प्रौद्योगिकी संस्थान' (IICT) कहाँ स्थित है?",
            "answer": "**भदोही** (जिसे कालीन नगरी के रूप में जाना जाता है)।",
            "icon": "fa-scroll"
        }
    ]
}

traps_hi = {
    "title": "परीक्षा में बचाव योग्य सामान्य भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1:</strong> राष्ट्रीय शर्करा संस्थान (NSI) और भारतीय गन्ना अनुसंधान संस्थान (IISR) में भ्रमित होना। **राष्ट्रीय शर्करा (चीनी) संस्थान (NSI) कानपुर** में है, जबकि **भारतीय गन्ना अनुसंधान संस्थान (IISR) लखनऊ** में है।",
        "<strong>भ्रम 2:</strong> इलाहाबाद विश्वविद्यालय के स्थापना वर्ष को लेकर भ्रम। इसकी स्थापना **1887** में हुई थी (भारत का चौथा सबसे पुराना विश्वविद्यालय), लेकिन इसे **केंद्रीय विश्वविद्यालय का दर्जा 2005** में मिला।",
        "<strong>भ्रम 3:</strong> पशु चिकित्सा अनुसंधान के स्थानों में उलझना। **भारतीय पशु चिकित्सा अनुसंधान संस्थान (IVRI) इज्जतनगर, बरेली** में है, जबकि **केंद्रीय बकरी अनुसंधान संस्थान (CIRG) मखदूम, मथुरा** में है।",
        "<strong>भ्रम 4:</strong> भातखंडे संगीत संस्थान के इतिहास को लेकर भ्रम। इसकी स्थापना मूल रूप से **1926 में पंडित विष्णु नारायण भातखंडे** द्वारा 'मैरिस कॉलेज ऑफ म्यूजिक' के रूप में की गई थी, जिसे बाद में राज्य सांस्कृतिक विश्वविद्यालय का दर्जा मिला।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. उत्तर प्रदेश के केंद्रीय और राज्य विश्वविद्यालय",
        "content": """<p>उत्तर प्रदेश में उच्च शिक्षा का एक व्यापक ढांचा है, जिसमें **6 केंद्रीय विश्वविद्यालय** (दिल्ली के साथ राज्यों में सर्वाधिक) और कई महत्वपूर्ण राज्य विश्वविद्यालय शामिल हैं:</p>
        
        <h3>A. छह केंद्रीय विश्वविद्यालय</h3>
        <ul>
          <li><strong>इलाहाबाद विश्वविद्यालय (प्रयागराज):</strong> सर विलियम मुइर द्वारा **1887** में स्थापित। अपनी शैक्षणिक प्रतिष्ठा के कारण इसे **'पूर्व का ऑक्सफोर्ड'** कहा जाता है। इसे **2005** में केंद्रीय विश्वविद्यालय घोषित किया गया।</li>
          <li><strong>बनारस हिंदू विश्वविद्यालय (BHU, वाराणसी):</strong> वर्ष **1916** में महामना मदन मोहन मालवीय, डॉ. एनी बेसेंट और महाराजा रामेश्वर सिंह द्वारा स्थापित किया गया। यह एशिया के सबसे बड़े आवासीय विश्वविद्यालयों में से एक है।</li>
          <li><strong>अलीगढ़ मुस्लिम विश्वविद्यालय (AMU, अलीगढ़):</strong> यह सर सैयद अहमद खान द्वारा **1875** में स्थापित 'मुहम्मडन एंग्लो-ओरिएंटल (MAO) कॉलेज' से विकसित हुआ, जिसे **1920** में विश्वविद्यालय का दर्जा दिया गया।</li>
          <li><strong>बाबासाहेब भीमराव अंबेडकर विश्वविद्यालय (BBAU, लखनऊ):</strong> समाज के वंचित वर्गों को उच्च शिक्षा प्रदान करने के उद्देश्य से **1996** में स्थापित।</li>
          <li><strong>राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय (RGNAU, अमेटी):</strong> फुर्सतगंज में **2013** में स्थापित देश का पहला विमानन क्षेत्र का विशिष्ट केंद्रीय विश्वविद्यालय।</li>
          <li><strong>रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय (RLBCAU, झांसी):</strong> बुंदेलखंड क्षेत्र की कृषि आवश्यकताओं की पूर्ति के लिए **2014** में संसद के अधिनियम द्वारा स्थापित।</li>
        </ul>

        <h3>B. प्रमुख राज्य और विशिष्ट विश्वविद्यालय</h3>
        <ul>
          <li><strong>लखनऊ विश्वविद्यालय:</strong> स्थापना वर्ष **1921**।</li>
          <li><strong>डॉ. भीमराव अंबेडकर विश्वविद्यालय (आगरा):</strong> वर्ष **1927** में आगरा विश्वविद्यालय के रूप में स्थापित।</li>
          <li><strong>चौधरी चरण सिंह विश्वविद्यालय (मेरठ):</strong> वर्ष **1965** में मेरठ विश्वविद्यालय के रूप में स्थापित।</li>
          <li><strong>दीनदयाल उपाध्याय गोरखपुर विश्वविद्यालय:</strong> स्थापना वर्ष **1957**।</li>
          <li><strong>भातखंडे संस्कृति विश्वविद्यालय (लखनऊ):</strong> मूल रूप से पंडित विष्णु नारायण भातखंडे द्वारा **1926** में स्थापित 'मैरिस कॉलेज ऑफ म्यूजिक' से विकसित हुआ। इसे 2022 में राज्य संस्कृति विश्वविद्यालय का दर्जा दिया गया।</li>
        </ul>"""
    },
    {
        "title": "2. उत्तर प्रदेश के राष्ट्रीय एवं केंद्रीय अनुसंधान संस्थान",
        "content": """<p>उत्तर प्रदेश में सीएसआईआर (CSIR), आईसीएआर (ICAR) और आईसीएमआर (ICMR) के कई प्रमुख संस्थान हैं। ये संस्थान आरओ/आरओ परीक्षाओं में मिलान वाले प्रश्नों में बहुत पूछे जाते हैं:</p>
        
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>शहर/स्थान</th>
                <th>संस्थान का नाम</th>
                <th>संक्षिप्त रूप</th>
                <th>मुख्य अनुसंधान क्षेत्र</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td rowspan="5"><strong>लखनऊ</strong></td>
                <td>केंद्रीय औषधि अनुसंधान संस्थान</td>
                <td>CDRI</td>
                <td>दवाओं की खोज और फार्मास्युटिकल अनुसंधान।</td>
              </tr>
              <tr>
                <td>राष्ट्रीय वनस्पति अनुसंधान संस्थान</td>
                <td>NBRI</td>
                <td>पादप वर्गीकरण, जैव प्रौद्योगिकी और संरक्षण।</td>
              </tr>
              <tr>
                <td>केंद्रीय औषधीय एवं सुगंधित पौधा संस्थान</td>
                <td>CIMAP</td>
                <td>संगठित सुगंधित तेलों और औषधीय पौधों पर शोध।</td>
              </tr>
              <tr>
                <td>भारतीय गन्ना अनुसंधान संस्थान</td>
                <td>IISR</td>
                <td>गन्ने की खेती की तकनीक और रोग नियंत्रण।</td>
              </tr>
              <tr>
                <td>भारतीय विषविज्ञान अनुसंधान संस्थान</td>
                <td>IITR (ITRC)</td>
                <td>औद्योगिक विषविज्ञान और पर्यावरणीय स्वास्थ्य।</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>कानपुर</strong></td>
                <td>भारतीय दलहन अनुसंधान संस्थान</td>
                <td>IIPR</td>
                <td>दालों की नई किस्में और फसल सुरक्षा।</td>
              </tr>
              <tr>
                <td>राष्ट्रीय शर्करा संस्थान</td>
                <td>NSI</td>
                <td>चीनी तकनीकी, इंजीनियरिंग और रासायनिक विश्लेषण।</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>झांसी</strong></td>
                <td>भारतीय चारागाह एवं चारा अनुसंधान संस्थान</td>
                <td>IGFRI</td>
                <td>चारा फसलों का उत्पादन और चारागाह प्रबंधन।</td>
              </tr>
              <tr>
                <td>केंद्रीय कृषि वानिकी अनुसंधान संस्थान</td>
                <td>CAFRI</td>
                <td>अर्ध-शुष्क क्षेत्रों के लिए कृषि वानिकी प्रणालियाँ।</td>
              </tr>
              <tr>
                <td><strong>वाराणसी</strong></td>
                <td>भारतीय शाक-भाजी (सब्जी) अनुसंधान संस्थान</td>
                <td>IIVR</td>
                <td>सब्जियों की नई किस्में और कटाई उपरांत तकनीक।</td>
              </tr>
              <tr>
                <td rowspan="2"><strong>इज्तनगर (बरेली)</strong></td>
                <td>भारतीय पशु चिकित्सा अनुसंधान संस्थान</td>
                <td>IVRI</td>
                <td>पशु स्वास्थ्य, टीके और पशु चिकित्सा विज्ञान।</td>
              </tr>
              <tr>
                <td>केंद्रीय पक्षी अनुसंधान संस्थान</td>
                <td>CARI</td>
                <td>पोल्ट्री (मुर्गी पालन) प्रजनन, पोषण और प्रबंधन।</td>
              </tr>
              <tr>
                <td><strong>भदोही</strong></td>
                <td>भारतीय कालीन प्रौद्योगिकी संस्थान</td>
                <td>IICT</td>
                <td>कालीन बुनाई, डिजाइन और टेक्सटाइल तकनीक।</td>
              </tr>
              <tr>
                <td><strong>मथुरा</strong></td>
                <td>केंद्रीय बकरी अनुसंधान संस्थान</td>
                <td>CIRG</td>
                <td>बकरी पालन, पोषण और रोग नियंत्रण।</td>
              </tr>
              <tr>
                <td><strong>नोएडा / ग्रेटर नोएडा</strong></td>
                <td>वी.वी. गिरि राष्ट्रीय श्रम संस्थान</td>
                <td>VVGNLI</td>
                <td>श्रम अध्ययन, नीतिगत अनुसंधान और प्रशिक्षण।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "3. कृषि और चिकित्सा विश्वविद्यालय",
        "content": """<p>उत्तर प्रदेश के प्रमुख क्षेत्रीय और व्यावसायिक विश्वविद्यालय:</p>
        
        <h3>A. कृषि विश्वविद्यालय</h3>
        <ul>
          <li><strong>चन्द्रशेखर आजाद कृषि एवं प्रौद्योगिकी विश्वविद्यालय (कानपुर):</strong> स्वतंत्रता सेनानी चंद्रशेखर आजाद के नाम पर **1975** में स्थापित।</li>
          <li><strong>आचार्य नरेंद्र देव कृषि एवं प्रौद्योगिकी विश्वविद्यालय (अयोध्या):</strong> वर्ष **1975** में कुमारगंज में स्थापित।</li>
          <li><strong>सरदार वल्लभभाई पटेल कृषि एवं प्रौद्योगिकी विश्वविद्यालय (मेरठ):</strong> वर्ष **2000** में स्थापित।</li>
          <li><strong>बांदा कृषि एवं प्रौद्योगिकी विश्वविद्यालय (बांदा):</strong> बुंदेलखंड की कृषि आवश्यकताओं की पूर्ति के लिए **2010** में स्थापित।</li>
          <li><strong>सैम हिगिनबॉटम कृषि, प्रौद्योगिकी एवं विज्ञान विश्वविद्यालय (SHUATS, प्रयागराज):</strong> **1910** में सैम हिगिनबॉटम द्वारा स्थापित 'इलाहाबाद एग्रीकल्चर इंस्टीट्यूट' से विकसित, जिसे 2000 में डीम्ड विश्वविद्यालय का दर्जा मिला।</li>
        </ul>

        <h3>B. प्रमुख चिकित्सा विश्वविद्यालय और संस्थान</h3>
        <ul>
          <li><strong>किंग जॉर्ज चिकित्सा विश्वविद्यालय (KGMU, लखनऊ):</strong> वर्ष **1911** में स्थापित किंग जॉर्ज मेडिकल कॉलेज से विकसित, जिसे **2002** में राज्य विश्वविद्यालय का दर्जा दिया गया।</li>
          <li><strong>संजय गांधी स्नातकोत्तर आयुर्विज्ञान संस्थान (SGPGIMS, लखनऊ):</strong> सुपर-स्पेशियलिटी चिकित्सा अनुसंधान के लिए **1983** में स्थापित।</li>
          <li><strong>उत्तर प्रदेश आयुर्विज्ञान विश्वविद्यालय (सैफई, इटावा):</strong> सैफई में ग्रामीण आयुर्विज्ञान संस्थान से विकसित कर **2016** में विश्वविद्यालय बनाया गया।</li>
        </ul>"""
    }
]

# ----------------- PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Which of the following is the oldest Central University in Uttar Pradesh?",
        "q_hi": "निम्नलिखित में से उत्तर प्रदेश का सबसे पुराना केंद्रीय विश्वविद्यालय कौन सा है?",
        "opts": [
            "Banaras Hindu University",
            "Aligarh Muslim University",
            "University of Allahabad",
            "Babasaheb Bhimrao Ambedkar University"
        ],
        "opts_hi": [
            "बनारस हिंदू विश्वविद्यालय",
            "अलीगढ़ मुस्लिम विश्वविद्यालय",
            "इलाहाबाद विश्वविद्यालय (University of Allahabad)",
            "बाबासाहेब भीमराव अंबेडकर विश्वविद्यालय"
        ],
        "ans": 2,
        "sol": "The University of Allahabad is the oldest central university in UP, founded in 1887. (It received Central University status in 2005, but by date of establishment, it is the oldest).",
        "sol_hi": "इलाहाबाद विश्वविद्यालय उत्तर प्रदेश का सबसे पुराना केंद्रीय विश्वविद्यालय है, जिसकी स्थापना 1887 में हुई थी। (यद्यपि इसे केंद्रीय विश्वविद्यालय का दर्जा 2005 में मिला, परंतु स्थापना तिथि के आधार पर यह सबसे पुराना है)।"
    },
    {
        "q": "Where is the Indian Institute of Pulses Research (IIPR) located?",
        "q_hi": "भारतीय दलहन अनुसंधान संस्थान (IIPR) निम्नलिखित में से किस स्थान पर स्थित है?",
        "opts": ["Lucknow", "Varanasi", "Kanpur", "Jhansi"],
        "opts_hi": ["लखनऊ", "वाराणसी", "कानपुर (Kanpur)", "झांसी"],
        "ans": 2,
        "sol": "The Indian Institute of Pulses Research (IIPR) is located in Kalyanpur, Kanpur.",
        "sol_hi": "भारतीय दलहन अनुसंधान संस्थान (IIPR) कानपुर के कल्याणपुर में स्थित है।"
    },
    {
        "q": "Match the following research institutes with their correct locations:\n1. IIVR - Varanasi\n2. IVRI - Izatnagar (Bareilly)\n3. IGFRI - Jhansi\n4. CIRG - Mathura\nSelect the correct code:",
        "q_hi": "निम्नलिखित अनुसंधान संस्थानों का उनके सही स्थानों के साथ मिलान करें:\n1. IIVR - वाराणसी\n2. IVRI - इज्जतनगर (बरेली)\n3. IGFRI - झांसी\n4. CIRG - मथुरा\nसही कोड चुनें:",
        "opts": ["All are correctly matched", "1 and 2 only", "2, 3 and 4 only", "1, 3 and 4 only"],
        "opts_hi": ["सभी सही सुमेलित हैं (All are correctly matched)", "केवल 1 और 2", "केवल 2, 3 और 4", "केवल 1, 3 और 4"],
        "ans": 0,
        "sol": "All pairs are correctly matched: IIVR (Vegetable Research) is in Varanasi, IVRI (Veterinary Research) is in Izatnagar, IGFRI (Grassland & Fodder) is in Jhansi, and CIRG (Goat Research) is in Makhdoom, Mathura.",
        "sol_hi": "सभी जोड़े बिल्कुल सही सुमेलित हैं: IIVR (सब्जी) वाराणसी में है, IVRI (पशु चिकित्सा) इज्जतनगर में है, IGFRI (चारागाह) झांसी में है, और CIRG (बकरी) मथुरा में है।"
    },
    {
        "q": "In which year was the Banaras Hindu University (BHU) established by Pandit Madan Mohan Malaviya?",
        "q_hi": "पंडित मदन मोहन मालवीय द्वारा बनारस हिंदू विश्वविद्यालय (BHU) की स्थापना किस वर्ष की गई थी?",
        "opts": ["1911", "1916", "1920", "1905"],
        "opts_hi": ["1911", "1916 (1916)", "1920", "1905"],
        "ans": 1,
        "sol": "BHU was established in Varanasi in the year 1916 under the Banaras Hindu University Act of 1915.",
        "sol_hi": "बनारस हिंदू विश्वविद्यालय (BHU) की स्थापना वर्ष 1916 में की गई थी।"
    },
    {
        "q": "Where is the Indian Institute of Sugarcane Research (IISR) located?",
        "q_hi": "भारतीय गन्ना अनुसंधान संस्थान (IISR) कहाँ स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Meerut", "Gorakhpur"],
        "opts_hi": ["लखनऊ (Lucknow)", "कानपुर", "मेरठ", "गोरखपुर"],
        "ans": 0,
        "sol": "The Indian Institute of Sugarcane Research (IISR) is located in Lucknow.",
        "sol_hi": "भारतीय गन्ना अनुसंधान संस्थान (IISR) लखनऊ में स्थित है।"
    },
    {
        "q": "The National Sugar Institute (NSI) is located in which city of Uttar Pradesh?",
        "q_hi": "राष्ट्रीय शर्करा (चीनी) संस्थान (NSI) उत्तर प्रदेश के किस शहर में स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Gorakhpur", "Bareilly"],
        "opts_hi": ["लखनऊ", "कानपुर (Kanpur)", "गोरखपुर", "बरेली"],
        "ans": 1,
        "sol": "The National Sugar Institute (NSI) is situated in Kanpur.",
        "sol_hi": "राष्ट्रीय शर्करा (चीनी) संस्थान (NSI) कानपुर में स्थित है।"
    },
    {
        "q": "Aligarh Muslim University (AMU) was originally established as Muhammadan Anglo-Oriental (MAO) College in 1875 by whom?",
        "q_hi": "अलीगढ़ मुस्लिम विश्वविद्यालय (AMU) की स्थापना मूल रूप से 1875 में मुहम्मडन एंग्लो-ओरिएंटल (MAO) कॉलेज के रूप में किसके द्वारा की गई थी?",
        "opts": ["Sir Syed Ahmad Khan", "Maulana Abul Kalam Azad", "Liaquat Ali Khan", "Dr. Zakir Husain"],
        "opts_hi": ["सर सैयद अहमद खान (Sir Syed Ahmad Khan)", "मौलाना अबुल कलाम आजाद", "लियाकत अली खान", "डॉ. जाकिर हुसैन"],
        "ans": 0,
        "sol": "Sir Syed Ahmad Khan founded the MAO College in Aligarh in 1875, which later became Aligarh Muslim University in 1920.",
        "sol_hi": "सर सैयद अहमद खान ने 1875 में अलीगढ़ में एमएओ कॉलेज की स्थापना की थी, जो बाद में 1920 में एएमयू बना।"
    },
    {
        "q": "Which state university of Uttar Pradesh was formerly known as Agra University?",
        "q_hi": "उत्तर प्रदेश के किस राज्य विश्वविद्यालय को पूर्व में आगरा विश्वविद्यालय के नाम से जाना जाता था?",
        "opts": [
            "Dr. Bhimrao Ambedkar University, Agra",
            "Chaudhary Charan Singh University, Meerut",
            "Chhatrapati Shahu Ji Maharaj University, Kanpur",
            "Deen Dayal Upadhyaya University, Gorakhpur"
        ],
        "opts_hi": [
            "डॉ. भीमराव अंबेडकर विश्वविद्यालय, आगरा",
            "चौधरी चरण सिंह विश्वविद्यालय, मेरठ",
            "छत्रपति शाहू जी महाराज विश्वविद्यालय, कानपुर",
            "दीनदयाल उपाध्याय विश्वविद्यालय, गोरखपुर"
        ],
        "ans": 0,
        "sol": "Agra University was established in 1927 and was later renamed Dr. Bhimrao Ambedkar University, Agra.",
        "sol_hi": "वर्ष 1927 में स्थापित आगरा विश्वविद्यालय का नाम बदलकर डॉ. भीमराव अंबेडकर विश्वविद्यालय, आगरा किया गया था।"
    },
    {
        "q": "Where is the Indian Institute of Carpet Technology (IICT) located in UP?",
        "q_hi": "उत्तर प्रदेश में 'भारतीय कालीन प्रौद्योगिकी संस्थान' (IICT) कहाँ स्थित है?",
        "opts": ["Bhadohi", "Mirzapur", "Varanasi", "Sonbhadra"],
        "opts_hi": ["भदोही (Bhadohi)", "मिर्जापुर", "वाराणसी", "सोनभद्र"],
        "ans": 0,
        "sol": "The Indian Institute of Carpet Technology (IICT) is situated in Bhadohi, which is famous for carpet production.",
        "sol_hi": "भारतीय कालीन प्रौद्योगिकी संस्थान (IICT) भदोही में स्थित है।"
    },
    {
        "q": "Where is the Central Institute for Research on Goats (CIRG) located?",
        "q_hi": "केंद्रीय बकरी अनुसंधान संस्थान (CIRG) कहाँ स्थित है?",
        "opts": ["Mathura", "Bareilly", "Meerut", "Lalitpur"],
        "opts_hi": ["मथुरा (Mathura)", "बरेली", "मेरठ", "ललितपुर"],
        "ans": 0,
        "sol": "The Central Institute for Research on Goats (CIRG) is located in Makhdoom, Mathura.",
        "sol_hi": "केंद्रीय बकरी अनुसंधान संस्थान (CIRG) मथुरा के मखदूम में स्थित है।"
    },
    {
        "q": "Consider the following statements:\n1. The Central Drug Research Institute (CDRI) is located in Lucknow.\n2. The National Botanical Research Institute (NBRI) is located in Kanpur.\nWhich of the statements given above is/are correct?",
        "q_hi": "निम्नलिखित कथनों पर विचार करें:\n1. केंद्रीय औषधि अनुसंधान संस्थान (CDRI) लखनऊ में स्थित है।\n2. राष्ट्रीय वनस्पति अनुसंधान संस्थान (NBRI) कानपुर में स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1 (1 only)", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the National Botanical Research Institute (NBRI) is also located in Lucknow, not Kanpur.",
        "sol_hi": "पहला कथन सही है। दूसरा कथन गलत है क्योंकि राष्ट्रीय वनस्पति अनुसंधान संस्थान (NBRI) भी लखनऊ में ही स्थित है, न कि कानपुर में।"
    },
    {
        "q": "Which of the following agricultural universities in UP is located in Ayodhya?",
        "q_hi": "उत्तर प्रदेश के निम्नलिखित कृषि विश्वविद्यालयों में से कौन सा अयोध्या में स्थित है?",
        "opts": [
            "Chandra Shekhar Azad University of Agriculture and Technology",
            "Acharya Narendra Deva University of Agriculture and Technology",
            "Sardar Vallabhbhai Patel University of Agriculture and Technology",
            "Banda University of Agriculture and Technology"
        ],
        "opts_hi": [
            "चन्द्रशेखर आजाद कृषि एवं प्रौद्योगिकी विश्वविद्यालय",
            "आचार्य नरेंद्र देव कृषि एवं प्रौद्योगिकी विश्वविद्यालय (Acharya Narendra Deva)",
            "सरदार वल्लभभाई पटेल कृषि एवं प्रौद्योगिकी विश्वविद्यालय",
            "बांदा कृषि एवं प्रौद्योगिकी विश्वविद्यालय"
        ],
        "ans": 1,
        "sol": "Acharya Narendra Deva University of Agriculture and Technology is located in Kumarganj, Ayodhya.",
        "sol_hi": "आचार्य नरेंद्र देव कृषि एवं प्रौद्योगिकी विश्वविद्यालय अयोध्या के कुमारगंज में स्थित है।"
    },
    {
        "q": "Where is the Rajiv Gandhi National Aviation University (RGNAU) located in UP?",
        "q_hi": "उत्तर प्रदेश में राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय (RGNAU) कहाँ स्थित है?",
        "opts": ["Amethi", "Raebareli", "Lucknow", "Noida"],
        "opts_hi": ["अमेठी (Amethi)", "रायबरेली", "लखनऊ", "नोएडा"],
        "ans": 0,
        "sol": "RGNAU is India's first aviation university, located at Fursatganj in Amethi district.",
        "sol_hi": "राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय अमेठी जिले के फुर्सतगंज में स्थित है।"
    },
    {
        "q": "Where is the Indian Grassland and Fodder Research Institute (IGFRI) located?",
        "q_hi": "भारतीय चारागाह एवं चारा अनुसंधान संस्थान (IGFRI) कहाँ स्थित है?",
        "opts": ["Jhansi", "Lalitpur", "Mahoba", "Banda"],
        "opts_hi": ["झांसी (Jhansi)", "ललितपुर", "महोबा", "बांदा"],
        "ans": 0,
        "sol": "The Indian Grassland and Fodder Research Institute (IGFRI) is located in Jhansi.",
        "sol_hi": "भारतीय चारागाह एवं चारा अनुसंधान संस्थान (IGFRI) झांसी में स्थित है।"
    },
    {
        "q": "The University of Allahabad is famously known by which sobriquet?",
        "q_hi": "इलाहाबाद विश्वविद्यालय किस प्रसिद्ध उपनाम से जाना जाता है?",
        "opts": ["Oxford of the East", "Cambridge of India", "Harvard of UP", "Eton of the Ganges"],
        "opts_hi": ["पूर्व का ऑक्सफोर्ड (Oxford of the East)", "भारत का कैम्ब्रिज", "यूपी का हार्वर्ड", "गंगा का ईटन"],
        "ans": 0,
        "sol": "Due to its high academic prestige and production of top administrators/intellectuals, the University of Allahabad is known as the 'Oxford of the East'.",
        "sol_hi": "अपनी उच्च शैक्षणिक गुणवत्ता और प्रशासकों/बुद्धिजीवियों को तैयार करने के कारण इलाहाबाद विश्वविद्यालय को 'पूर्व का ऑक्सफोर्ड' कहा जाता है।"
    },
    {
        "q": "In which city of Uttar Pradesh is the Central Paper and Pulp Research Institute located?",
        "q_hi": "उत्तर प्रदेश के किस शहर में 'केंद्रीय लुगदी एवं कागज अनुसंधान संस्थान' स्थित है?",
        "opts": ["Saharanpur", "Meerut", "Ghaziabad", "Muzaffarnagar"],
        "opts_hi": ["सहारनपुर (Saharanpur)", "मेरठ", "गाजियाबाद", "मुजफ्फरनगर"],
        "ans": 0,
        "sol": "The Central Paper and Pulp Research Institute is located in Saharanpur.",
        "sol_hi": "केंद्रीय लुगदी एवं कागज अनुसंधान संस्थान उत्तर प्रदेश के सहारनपुर जिले में स्थित है।"
    },
    {
        "q": "The Central Potato Research Station is located in which district of Uttar Pradesh?",
        "q_hi": "केंद्रीय आलू अनुसंधान केंद्र उत्तर प्रदेश के किस जिले में स्थित है?",
        "opts": ["Meerut", "Agra", "Farrukhabad", "Kannauj"],
        "opts_hi": ["मेरठ (Meerut)", "आगरा", "फर्रुखाबाद", "कन्नौज"],
        "ans": 0,
        "sol": "The Central Potato Research Station in UP is located in Modipuram, Meerut.",
        "sol_hi": "केंद्रीय आलू अनुसंधान केंद्र मेरठ के मोदीपुरम में स्थित है (यह शिमला स्थित मुख्य सीपीआरआई का क्षेत्रीय केंद्र है)।"
    },
    {
        "q": "Where is the Indian Institute of Handloom Technology (IIHT) located?",
        "q_hi": "भारतीय हथकरघा प्रौद्योगिकी संस्थान (IIHT) कहाँ स्थित है?",
        "opts": ["Varanasi", "Bhadohi", "Lucknow", "Kanpur"],
        "opts_hi": ["वाराणसी (Varanasi)", "भदोही", "लखनऊ", "कानपुर"],
        "ans": 0,
        "sol": "The Indian Institute of Handloom Technology (IIHT) is situated in Chowkaghat, Varanasi.",
        "sol_hi": "भारतीय हथकरघा प्रौद्योगिकी संस्थान (IIHT) वाराणसी के चौकाघाट में स्थित है।"
    },
    {
        "q": "Which state university in Lucknow is dedicated to music and performing arts, upgraded from a famous music college established in 1926?",
        "q_hi": "लखनऊ का कौन सा राज्य विश्वविद्यालय संगीत और प्रदर्शन कला को समर्पित है, जो 1926 में स्थापित एक प्रसिद्ध संगीत कॉलेज से अपग्रेड हुआ है?",
        "opts": [
            "Bhatkhande Sanskriti Vishwavidyalaya",
            "Shakuntala Misra Rehabilitation University",
            "Lucknow University",
            "Ram Manohar Lohia National Law University"
        ],
        "opts_hi": [
            "भातखंडे संस्कृति विश्वविद्यालय (Bhatkhande)",
            "शकुंतला मिश्रा पुनर्वास विश्वविद्यालय",
            "लखनऊ विश्वविद्यालय",
            "राम मनोहर लोहिया राष्ट्रीय विधि विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "Bhatkhande Sanskriti Vishwavidyalaya evolved from Marris College of Music (1926), later Bhatkhande Music Institute, and was upgraded to a state university in 2022.",
        "sol_hi": "भातखंडे संस्कृति विश्वविद्यालय मूल रूप से 1926 में स्थापित मैरिस कॉलेज ऑफ म्यूजिक से विकसित हुआ, जिसे 2022 में राज्य संस्कृति विश्वविद्यालय का दर्जा दिया गया।"
    },
    {
        "q": "Where is the V.V. Giri National Labour Institute located in Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश में 'वी.वी. गिरि राष्ट्रीय श्रम संस्थान' कहाँ स्थित है?",
        "opts": ["Noida", "Lucknow", "Kanpur", "Ghaziabad"],
        "opts_hi": ["नोएडा (Noida)", "लखनऊ", "कानपुर", "गाजियाबाद"],
        "ans": 0,
        "sol": "The V.V. Giri National Labour Institute is a premier national institute for labor studies located in Sector-24, Noida.",
        "sol_hi": "वी.वी. गिरि राष्ट्रीय श्रम संस्थान नोएडा के सेक्टर-24 में स्थित है।"
    },
    # --- ADDITIONAL 20 QUESTIONS TO REACH EXACTLY 50 ---
    {
        "q": "Consider the following statements regarding the Central Universities of UP:\n1. Rani Lakshmi Bai Central Agricultural University is located in Jhansi.\n2. Rajiv Gandhi National Aviation University is located in Raebareli.\nWhich of the statements given above is/are correct?",
        "q_hi": "उत्तर प्रदेश के केंद्रीय विश्वविद्यालयों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय झांसी में स्थित है।\n2. राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय रायबरेली में स्थित है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "opts_hi": ["केवल 1 (1 only)", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because the Rajiv Gandhi National Aviation University is located in Fursatganj, Amethi district (not Raebareli).",
        "sol_hi": "पहला कथन सही है। दूसरा कथन गलत है क्योंकि राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय अमेठी जिले के फुर्सतगंज में स्थित है (न कि रायबरेली में)।"
    },
    {
        "q": "In which year was King George's Medical College (now KGMU) established in Lucknow?",
        "q_hi": "लखनऊ में किंग जॉर्ज मेडिकल कॉलेज (अब KGMU) की स्थापना किस वर्ष की गई थी?",
        "opts": ["1911", "1921", "1905", "1931"],
        "opts_hi": ["1911 (1911)", "1921", "1905", "1931"],
        "ans": 0,
        "sol": "King George's Medical College opened for students in 1911. It was upgraded to a state medical university in 2002.",
        "sol_hi": "किंग जॉर्ज मेडिकल कॉलेज की शुरुआत वर्ष 1911 में हुई थी, जिसे 2002 में राज्य विश्वविद्यालय में अपग्रेड किया गया।"
    },
    {
        "q": "Where is the Central Institute of Medicinal and Aromatic Plants (CIMAP) located?",
        "q_hi": "केंद्रीय औषधीय एवं सुगंधित पौधा संस्थान (CIMAP) कहाँ स्थित है?",
        "opts": ["Lucknow", "Varanasi", "Mathura", "Saharanpur"],
        "opts_hi": ["लखनऊ (Lucknow)", "वाराणसी", "मथुरा", "सहारनपुर"],
        "ans": 0,
        "sol": "CIMAP is a laboratory of CSIR located in Lucknow, dedicated to research on medicinal and aromatic crops.",
        "sol_hi": "CIMAP लखनऊ में स्थित सीएसआईआर (CSIR) की एक प्रयोगशाला है जो औषधीय एवं सुगंधित पौधों पर शोध करती है।"
    },
    {
        "q": "Sam Higginbottom University of Agriculture, Technology and Sciences (SHUATS) is located in which district of UP?",
        "q_hi": "सैम हिगिनबॉटम कृषि, प्रौद्योगिकी एवं विज्ञान विश्वविद्यालय (SHUATS) उत्तर प्रदेश के किस जिले में स्थित है?",
        "opts": ["Prayagraj", "Varanasi", "Kanpur", "Aligarh"],
        "opts_hi": ["प्रयागराज (Prayagraj)", "वाराणसी", "कानपुर", "अलीगढ़"],
        "ans": 0,
        "sol": "SHUATS is located in Naini, Prayagraj, originally established as Allahabad Agricultural Institute in 1910.",
        "sol_hi": "SHUATS प्रयागराज के नैनी में स्थित है, जिसे 1910 में इलाहाबाद कृषि संस्थान के रूप में स्थापित किया गया था।"
    },
    {
        "q": "Where is the state-funded Uttar Pradesh University of Medical Sciences located?",
        "q_hi": "राज्य वित्त पोषित 'उत्तर प्रदेश आयुर्विज्ञान विश्वविद्यालय' कहाँ स्थित है?",
        "opts": ["Saifai (Etawah)", "Gorakhpur", "Greater Noida", "Meerut"],
        "opts_hi": ["सैफई, इटावा (Saifai)", "गोरखपुर", "ग्रेटर नोएडा", "मेरठ"],
        "ans": 0,
        "sol": "The UP University of Medical Sciences is located in Saifai, Etawah district.",
        "sol_hi": "उत्तर प्रदेश आयुर्विज्ञान विश्वविद्यालय सैफई (इटावा जिले) में स्थित है।"
    },
    {
        "q": "Which state university of UP is named after the former Prime Minister of India, located in Meerut?",
        "q_hi": "उत्तर प्रदेश के मेरठ में स्थित कौन सा राज्य विश्वविद्यालय भारत के पूर्व प्रधानमंत्री के नाम पर रखा गया है?",
        "opts": [
            "Chaudhary Charan Singh University",
            "Chandra Shekhar Azad University",
            "Deen Dayal Upadhyaya University",
            "Mahatma Jyotiba Phule Rohilkhand University"
        ],
        "opts_hi": [
            "चौधरी चरण सिंह विश्वविद्यालय (CCS University)",
            "चन्द्रशेखर आजाद विश्वविद्यालय",
            "दीनदयाल उपाध्याय विश्वविद्यालय",
            "महात्मा ज्योतिबा फुले रोहिलखंड विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "Meerut University, established in 1965, was renamed Chaudhary Charan Singh University to honor the former Prime Minister.",
        "sol_hi": "मेरठ विश्वविद्यालय की स्थापना 1965 में हुई थी, जिसका नाम बाद में पूर्व प्रधानमंत्री चौधरी चरण सिंह के सम्मान में बदला गया।"
    },
    {
        "q": "Where is the Indian Veterinary Research Institute (IVRI) located in Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश में 'भारतीय पशु चिकित्सा अनुसंधान संस्थान' (IVRI) कहाँ स्थित है?",
        "opts": ["Izatnagar, Bareilly", "Mathura", "Kanpur", "Modipuram, Meerut"],
        "opts_hi": ["इज्जतनगर, बरेली (Izatnagar)", "मथुरा", "कानपुर", "मोदीपुरम, मेरठ"],
        "ans": 0,
        "sol": "IVRI is located in Izatnagar, Bareilly. It is a premier institute for research in veterinary science and animal health.",
        "sol_hi": "भारतीय पशु चिकित्सा अनुसंधान संस्थान (IVRI) बरेली के इज्जतनगर में स्थित है।"
    },
    {
        "q": "The state university 'Dr. Ram Manohar Lohia National Law University' is located in which city?",
        "q_hi": "राज्य विश्वविद्यालय 'डॉ. राम मनोहर लोहिया राष्ट्रीय विधि विश्वविद्यालय' किस शहर में स्थित है?",
        "opts": ["Lucknow", "Prayagraj", "Noida", "Varanasi"],
        "opts_hi": ["लखनऊ (Lucknow)", "प्रयागराज", "नोएडा", "वाराणसी"],
        "ans": 0,
        "sol": "Dr. Ram Manohar Lohia National Law University (RMLNLU) is a specialized law university located in Lucknow.",
        "sol_hi": "डॉ. राम मनोहर लोहिया राष्ट्रीय विधि विश्वविद्यालय (RMLNLU) लखनऊ में स्थित है।"
    },
    {
        "q": "Where is the Central Institute of Plastics Engineering and Technology (CIPET) located in UP?",
        "q_hi": "उत्तर प्रदेश में 'सेंट्रल इंस्टीट्यूट ऑफ प्लास्टिक इंजीनियरिंग एंड टेक्नोलॉजी' (CIPET) कहाँ स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Noida", "Ghaziabad"],
        "opts_hi": ["लखनऊ (Lucknow)", "कानपुर", "नोएडा", "गाजियाबाद"],
        "ans": 0,
        "sol": "CIPET in UP is located in Amausi, Lucknow.",
        "sol_hi": "केंद्रीय प्लास्टिक इंजीनियरिंग एवं प्रौद्योगिकी संस्थान (CIPET) लखनऊ के अमौसी में स्थित है।"
    },
    {
        "q": "Where is the National Research Centre for Agroforestry (now CAFRI) located?",
        "q_hi": "राष्ट्रीय कृषि वानिकी अनुसंधान केंद्र (अब CAFRI) कहाँ स्थित है?",
        "opts": ["Jhansi", "Banda", "Hamirpur", "Mirzapur"],
        "opts_hi": ["झांसी (Jhansi)", "बांदा", "हमीरपुर", "मिर्जापुर"],
        "ans": 0,
        "sol": "The Central Agroforestry Research Institute (CAFRI), formerly the National Research Centre for Agroforestry, is located in Jhansi.",
        "sol_hi": "केंद्रीय कृषि वानिकी अनुसंधान संस्थान (CAFRI) झांसी में स्थित है।"
    },
    {
        "q": "Which institute in Raebareli is a premier national-level institute for research and training in pharmaceutical sciences?",
        "q_hi": "रायबरेली में कौन सा संस्थान फार्मास्युटिकल विज्ञान में अनुसंधान और प्रशिक्षण के लिए एक प्रमुख राष्ट्रीय स्तर का संस्थान है?",
        "opts": ["NIPER", "CDRI", "CIMAP", "NIB"],
        "opts_hi": ["NIPER (NIPER)", "CDRI", "CIMAP", "NIB"],
        "ans": 0,
        "sol": "The National Institute of Pharmaceutical Education and Research (NIPER) has a campus in Raebareli.",
        "sol_hi": "राष्ट्रीय औषधीय शिक्षा एवं अनुसंधान संस्थान (NIPER) रायबरेली में स्थित है।"
    },
    {
        "q": "The Harish-Chandra Research Institute (HRI), famous for research in Mathematics and Theoretical Physics, is located in which city?",
        "q_hi": "गणित और सैद्धांतिक भौतिकी में उत्कृष्ट अनुसंधान के लिए प्रसिद्ध 'हरीश-चंद्र अनुसंधान संस्थान' (HRI) किस शहर में स्थित है?",
        "opts": ["Prayagraj", "Varanasi", "Kanpur", "Lucknow"],
        "opts_hi": ["प्रयागराज (Prayagraj)", "वाराणसी", "कानपुर", "लखनऊ"],
        "ans": 0,
        "sol": "The Harish-Chandra Research Institute (HRI) is located in Jhunsi, Prayagraj.",
        "sol_hi": "हरीश-चंद्र अनुसंधान संस्थान (HRI) प्रयागराज के झूंसी में स्थित है।"
    },
    {
        "q": "Where is the Central Avian Research Institute (CARI) located?",
        "q_hi": "केंद्रीय पक्षी अनुसंधान संस्थान (CARI) कहाँ स्थित है?",
        "opts": ["Izatnagar, Bareilly", "Makhdoom, Mathura", "Modipuram, Meerut", "Hulas, Saharanpur"],
        "opts_hi": ["इज्जतनगर, बरेली (Izatnagar)", "मखदूम, महुआ", "मोदीपुरम, मेरठ", "हुलास, सहारनपुर"],
        "ans": 0,
        "sol": "The Central Avian Research Institute (CARI) is located in Izatnagar, Bareilly, close to IVRI.",
        "sol_hi": "केंद्रीय पक्षी अनुसंधान संस्थान (CARI) बरेली के इज्जतनगर में स्थित है।"
    },
    {
        "q": "Where is the Birbal Sahni Institute of Palaeosciences located?",
        "q_hi": "बीरबल साहनी पुराविज्ञान संस्थान (Birbal Sahni Institute of Palaeosciences) कहाँ स्थित है?",
        "opts": ["Lucknow", "Prayagraj", "Dehradun", "Varanasi"],
        "opts_hi": ["लखनऊ (Lucknow)", "प्रयागराज", "देहरादून", "वाराणसी"],
        "ans": 0,
        "sol": "The Birbal Sahni Institute of Palaeosciences (formerly Birbal Sahni Institute of Palaeobotany) is located in Lucknow.",
        "sol_hi": "बीरबल साहनी पुराविज्ञान संस्थान (पुरावनस्पति विज्ञान संस्थान) लखनऊ में स्थित है।"
    },
    {
        "q": "Which state agricultural university in Bundelkhand was established in Banda in 2010?",
        "q_hi": "बुंदेलखंड क्षेत्र के बांदा में वर्ष 2010 में कौन सा राज्य कृषि विश्वविद्यालय स्थापित किया गया था?",
        "opts": [
            "Banda University of Agriculture and Technology",
            "Bundelkhand Agricultural Academy",
            "Rani Lakshmi Bai Central Agricultural University",
            "Chandra Shekhar Azad University"
        ],
        "opts_hi": [
            "बांदा कृषि एवं प्रौद्योगिकी विश्वविद्यालय (Banda University)",
            "बुंदेलखंड कृषि अकादमी",
            "रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय",
            "चन्द्रशेखर आजाद विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "Banda University of Agriculture and Technology was established in Banda in 2010 to cater to Bundelkhand's semi-arid farming conditions.",
        "sol_hi": "बांदा कृषि एवं प्रौद्योगिकी विश्वविद्यालय की स्थापना 2010 में बांदा में हुई थी।"
    },
    {
        "q": "Where is the Indian Institute of Information Technology (IIIT) located in Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश में 'भारतीय सूचना प्रौद्योगिकी संस्थान' (IIIT) कहाँ स्थित है?",
        "opts": ["Prayagraj", "Lucknow", "Kanpur", "Noida"],
        "opts_hi": ["प्रयागराज (Prayagraj)", "लखनऊ", "कानपुर", "नोएडा"],
        "ans": 0,
        "sol": "The Indian Institute of Information Technology (IIIT Allahabad) is located in Devghat, Jhalwa, Prayagraj.",
        "sol_hi": "भारतीय सूचना प्रौद्योगिकी संस्थान (IIIT) प्रयागराज के झलवा में स्थित है।"
    },
    {
        "q": "Where is the state-funded specialized university 'Sanjay Gandhi Postgraduate Institute of Medical Sciences' (SGPGIMS) located?",
        "q_hi": "राज्य वित्त पोषित विशिष्ट संस्थान 'संजय गांधी स्नातकोत्तर आयुर्विज्ञान संस्थान' (SGPGIMS) कहाँ स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Saifai", "Varanasi"],
        "opts_hi": ["लखनऊ (Lucknow)", "कानपुर", "सैफई", "वाराणसी"],
        "ans": 0,
        "sol": "SGPGIMS is a premier medical institute located in Lucknow.",
        "sol_hi": "संजय गांधी स्नातकोत्तर आयुर्विज्ञान संस्थान (SGPGIMS) लखनऊ में स्थित है।"
    },
    {
        "q": "Which research center in Meerut is dedicated to research on potato crop development?",
        "q_hi": "मेरठ में आलू की फसल के विकास के लिए कौन सा अनुसंधान केंद्र समर्पित है?",
        "opts": [
            "Central Potato Research Station, Modipuram",
            "Indian Vegetable Research Institute",
            "Central Agroforestry Research Institute",
            "Central Avian Research Institute"
        ],
        "opts_hi": [
            "केंद्रीय आलू अनुसंधान केंद्र, मोदीपुरम (Modipuram)",
            "भारतीय सब्जी अनुसंधान संस्थान",
            "केंद्रीय कृषि वानिकी अनुसंधान संस्थान",
            "केंद्रीय पक्षी अनुसंधान संस्थान"
        ],
        "ans": 0,
        "sol": "The Central Potato Research Station is located at Modipuram, Meerut, functioning under CPRI Shimla.",
        "sol_hi": "मेरठ के मोदीपुरम में केंद्रीय आलू अनुसंधान स्टेशन स्थित है।"
    },
    {
        "q": "Sardar Vallabhbhai Patel University of Agriculture and Technology is located in which district?",
        "q_hi": "सरदार वल्लभभाई पटेल कृषि एवं प्रौद्योगिकी विश्वविद्यालय किस जिले में स्थित है?",
        "opts": ["Meerut", "Banda", "Ayodhya", "Kanpur"],
        "opts_hi": ["मेरठ (Meerut)", "बांदा", "अयोध्या", "कानपुर"],
        "ans": 0,
        "sol": "Sardar Vallabhbhai Patel University of Agriculture and Technology is located in Modipuram, Meerut.",
        "sol_hi": "सरदार वल्लभभाई पटेल कृषि एवं प्रौद्योगिकी विश्वविद्यालय मेरठ के मोदीपुरम में स्थित है।"
    },
    {
        "q": "Where is the Central Institute of Medicinal and Aromatic Plants (CIMAP) located?",
        "q_hi": "केंद्रीय औषधीय एवं सुगंधित पौधा संस्थान (CIMAP) कहाँ स्थित है?",
        "opts": ["Lucknow", "Saharanpur", "Moradabad", "Bareilly"],
        "opts_hi": ["लखनऊ (Lucknow)", "सहारनपुर", "मुरादाबाद", "बरेली"],
        "ans": 0,
        "sol": "CIMAP is situated in Lucknow, researching medicinal and aromatic properties of plants.",
        "sol_hi": "केंद्रीय औषधीय एवं सुगंधित पौधा संस्थान (CIMAP) लखनऊ में स्थित है."
    },
    {
        "q": "Where is the Central Institute for Subtropical Horticulture (CISH) located in Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश में 'केंद्रीय उपोष्णकटिबंधीय बागवानी संस्थान' (CISH) कहाँ स्थित है?",
        "opts": ["Lucknow", "Varanasi", "Saharanpur", "Meerut"],
        "opts_hi": ["लखनऊ (Lucknow)", "वाराणसी", "सहारनपुर", "मेरठ"],
        "ans": 0,
        "sol": "The Central Institute for Subtropical Horticulture (CISH), formerly the Central Mango Research Station, is located in Rehmankhera, Lucknow.",
        "sol_hi": "केंद्रीय उपोष्णकटिबंधीय बागवानी संस्थान (CISH), जिसे पहले केंद्रीय आम अनुसंधान केंद्र के नाम से जाना जाता था, लखनऊ के रहमानखेड़ा में स्थित है।"
    },
    {
        "q": "The Fragrance and Flavour Development Centre (FFDC) is situated in which city of Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश के किस शहर में 'सुगंध एवं स्वाद विकास केंद्र' (FFDC) स्थित है?",
        "opts": ["Kannauj", "Lucknow", "Jaunpur", "Ghazipur"],
        "opts_hi": ["कन्नौज (Kannauj)", "लखनऊ", "जौनपुर", "गाजीपुर"],
        "ans": 0,
        "sol": "The Fragrance and Flavour Development Centre (FFDC) is located in Kannauj, which is famously known as the Perfume Capital of India.",
        "sol_hi": "सुगंध एवं स्वाद विकास केंद्र (FFDC) कन्नौज में स्थित है, जिसे भारत की इत्र राजधानी के रूप में जाना जाता है।"
    },
    {
        "q": "Jagadguru Rambhadracharya State Handicapped University, the first university exclusively for disabled persons, is located in which district of UP?",
        "q_hi": "दिव्यांग व्यक्तियों के लिए विशेष रूप से स्थापित पहला विश्वविद्यालय 'जगद्गुरु रामभद्राचार्य दिव्यांग विश्वविद्यालय' उत्तर प्रदेश के किस जिले में स्थित है?",
        "opts": ["Chitrakoot", "Jhansi", "Prayagraj", "Varanasi"],
        "opts_hi": ["चित्रकूट (Chitrakoot)", "झांसी", "प्रयागराज", "वाराणसी"],
        "ans": 0,
        "sol": "Jagadguru Rambhadracharya Divyanga University was established in Chitrakoot in 2001. It is the first university of its kind exclusively for disabled students.",
        "sol_hi": "जगद्गुरु रामभद्राचार्य दिव्यांग विश्वविद्यालय की स्थापना 2001 में चित्रकूट में की गई थी।"
    },
    {
        "q": "Where is the National Bureau of Fish Genetic Resources (NBFGR) located?",
        "q_hi": "राष्ट्रीय मत्स्य आनुवंशिक संसाधन ब्यूरो (NBFGR) कहाँ स्थित है?",
        "opts": ["Lucknow", "Prayagraj", "Varanasi", "Gorakhpur"],
        "opts_hi": ["लखनऊ (Lucknow)", "प्रयागराज", "वाराणसी", "गोरखपुर"],
        "ans": 0,
        "sol": "The National Bureau of Fish Genetic Resources (NBFGR) is located in Lucknow.",
        "sol_hi": "राष्ट्रीय मत्स्य आनुवंशिक संसाधन ब्यूरो (NBFGR) लखनऊ में स्थित है।"
    },
    {
        "q": "Harcourt Butler Technical University (HBTU) was established in which year, and in which city?",
        "q_hi": "हरकोर्ट बटलर तकनीकी विश्वविद्यालय (HBTU) की स्थापना किस वर्ष और किस शहर में हुई थी?",
        "opts": ["1921, Kanpur", "1959, Kanpur", "1965, Meerut", "1920, Aligarh"],
        "opts_hi": ["1921, कानपुर (1921, Kanpur)", "1959, कानपुर", "1965, मेरठ", "1920, अलीगढ़"],
        "ans": 0,
        "sol": "Harcourt Butler Technological Institute was established in Kanpur in 1921 and was upgraded to a state university (HBTU) in 2016.",
        "sol_hi": "हरकोर्ट बटलर टेक्नोलॉजिकल इंस्टीट्यूट की स्थापना 1921 में कानपुर में की गई थी और इसे 2016 में राज्य विश्वविद्यालय का दर्जा दिया गया था।"
    },
    {
        "q": "Where is the National Institute of Biologicals (NIB) located in Uttar Pradesh?",
        "q_hi": "उत्तर प्रदेश में 'राष्ट्रीय जैविक संस्थान' (NIB) कहाँ स्थित है?",
        "opts": ["Noida", "Lucknow", "Kanpur", "Ghaziabad"],
        "opts_hi": ["नोएडा (Noida)", "लखनऊ", "कानपुर", "गाजियाबाद"],
        "ans": 0,
        "sol": "The National Institute of Biologicals (NIB) is an autonomous institute under the Ministry of Health and Family Welfare, located in Noida.",
        "sol_hi": "राष्ट्रीय जैविक संस्थान (NIB) स्वास्थ्य एवं परिवार कल्याण मंत्रालय के तहत एक स्वायत्त संस्थान है जो नोएडा में स्थित है।"
    },
    {
        "q": "The Indian Institute of Technology (IIT) Kanpur, one of the premier engineering institutions in India, was established in which year?",
        "q_hi": "भारत के प्रमुख इंजीनियरिंग संस्थानों में से एक, भारतीय प्रौद्योगिकी संस्थान (IIT) कानपुर की स्थापना किस वर्ष हुई थी?",
        "opts": ["1959", "1969", "1951", "1980"],
        "opts_hi": ["1959 (1959)", "1969", "1951", "1980"],
        "ans": 0,
        "sol": "IIT Kanpur was established in 1959 with the assistance of a consortium of nine US research universities under the Kanpur Indo-American Programme.",
        "sol_hi": "IIT कानपुर की स्थापना वर्ष 1959 में कानपुर इंडो-अमेरिकन कार्यक्रम के तहत अमेरिकी अनुसंधान विश्वविद्यालयों के सहयोग से की गई थी।"
    },
    {
        "q": "Dr. Shakuntala Misra National Rehabilitation University, dedicated to providing accessible higher education to disabled students, is located in which city?",
        "q_hi": "दिव्यांग छात्रों को सुगम उच्च शिक्षा प्रदान करने के लिए समर्पित 'डॉ. शकुंतला मिश्रा राष्ट्रीय पुनर्वास विश्वविद्यालय' किस शहर में स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Prayagraj", "Varanasi"],
        "opts_hi": ["लखनऊ (Lucknow)", "कानपुर", "प्रयागराज", "वाराणसी"],
        "ans": 0,
        "sol": "Dr. Shakuntala Misra National Rehabilitation University was established by the Government of Uttar Pradesh in Lucknow in 2008.",
        "sol_hi": "डॉ. शकुंतला मिश्रा राष्ट्रीय पुनर्वास विश्वविद्यालय की स्थापना उत्तर प्रदेश सरकार द्वारा 2008 में लखनऊ में की गई थी।"
    },
    {
        "q": "Where is the central campus of Central Institute of Higher Tibetan Studies (CIHTS) located?",
        "q_hi": "केंद्रीय उच्च तिब्बती शिक्षा संस्थान (CIHTS) का मुख्य परिसर कहाँ स्थित है?",
        "opts": ["Sarnath, Varanasi", "Gorakhpur", "Kushinagar", "Mathura"],
        "opts_hi": ["सारनाथ, वाराणसी (Sarnath)", "गोरखपुर", "कुशीनगर", "मथुरा"],
        "ans": 0,
        "sol": "The Central Institute of Higher Tibetan Studies (CIHTS) is a deemed university located in Sarnath, Varanasi, established in 1967.",
        "sol_hi": "केंद्रीय उच्च तिब्बती शिक्षा संस्थान (CIHTS) वाराणसी के सारनाथ में स्थित एक मानद (deemed) विश्वविद्यालय है, जिसकी स्थापना 1967 में हुई थी।"
    },
    {
        "q": "Uttar Pradesh Council of Agricultural Research (UPCAR) is located in which city?",
        "q_hi": "उत्तर प्रदेश कृषि अनुसंधान परिषद (UPCAR) किस शहर में स्थित है?",
        "opts": ["Lucknow", "Kanpur", "Ayodhya", "Jhansi"],
        "opts_hi": ["लखनऊ (Lucknow)", "कानपुर", "अयोध्या", "झांसी"],
        "ans": 0,
        "sol": "The Uttar Pradesh Council of Agricultural Research (UPCAR) was established in 1989 and is located in Lucknow.",
        "sol_hi": "उत्तर प्रदेश कृषि अनुसंधान परिषद (UPCAR) की स्थापना 1989 में हुई थी और यह लखनऊ में स्थित है।"
    }
]

# ----------------- MOCK TEST QUESTIONS (15 Qs) -----------------
mock_test_questions = [
    {
        "q": "Which of the following universities in UP is commonly referred to as the 'Oxford of the East'?",
        "q_hi": "उत्तर प्रदेश के किस विश्वविद्यालय को सामान्यतः 'पूर्व का ऑक्सफोर्ड' कहा जाता है?",
        "opts": [
            "Banaras Hindu University",
            "Aligarh Muslim University",
            "University of Allahabad",
            "Lucknow University"
        ],
        "opts_hi": [
            "बनारस हिंदू विश्वविद्यालय",
            "अलीगढ़ मुस्लिम विश्वविद्यालय",
            "इलाहाबाद विश्वविद्यालय (Allahabad University)",
            "लखनऊ विश्वविद्यालय"
        ],
        "ans": 2,
        "sol": "The University of Allahabad, established in 1887, was known as the 'Oxford of the East' due to its academic prestige.",
        "sol_hi": "इलाहाबाद विश्वविद्यालय को उसकी पूर्व शैक्षणिक ख्याति के कारण 'पूर्व का ऑक्सफोर्ड' कहा जाता था।"
    },
    {
        "q": "The Indian Institute of Pulses Research (IIPR) and the National Sugar Institute (NSI) are both located in which city?",
        "q_hi": "भारतीय दलहन अनुसंधान संस्थान (IIPR) और राष्ट्रीय शर्करा संस्थान (NSI) दोनों किस शहर में स्थित हैं?",
        "opts": ["Lucknow", "Kanpur", "Varanasi", "Bareilly"],
        "opts_hi": ["लखनऊ", "कानपुर (Kanpur)", "वाराणसी", "बरेली"],
        "ans": 1,
        "sol": "Both IIPR and NSI are located in Kanpur.",
        "sol_hi": "IIPR (दलहन) और NSI (चीनी) दोनों ही संस्थान कानपुर में स्थित हैं।"
    },
    {
        "q": "Where is the Indian Institute of Vegetable Research (IIVR) located?",
        "q_hi": "भारतीय शाक-भाजी (सब्जी) अनुसंधान संस्थान (IIVR) कहाँ स्थित है?",
        "opts": ["Lucknow", "Varanasi", "Kanpur", "Mathura"],
        "opts_hi": ["लखनऊ", "वाराणसी (Varanasi)", "कानपुर", "मथुरा"],
        "ans": 1,
        "sol": "IIVR is located in Shahanshahpur, Varanasi.",
        "sol_hi": "IIVR वाराणसी के शहंशाहपुर में स्थित है।"
    },
    {
        "q": "Which central university of UP evolved from the Muhammadan Anglo-Oriental College established in 1875?",
        "q_hi": "उत्तर प्रदेश का कौन सा केंद्रीय विश्वविद्यालय 1875 में स्थापित मुहम्मडन एंग्लो-ओरिएंटल कॉलेज से विकसित हुआ?",
        "opts": [
            "Aligarh Muslim University",
            "Babasaheb Bhimrao Ambedkar University",
            "Banaras Hindu University",
            "University of Allahabad"
        ],
        "opts_hi": [
            "अलीगढ़ मुस्लिम विश्वविद्यालय (AMU)",
            "बाबासाहेब भीमराव अंबेडकर विश्वविद्यालय",
            "बनारस हिंदू विश्वविद्यालय",
            "इलाहाबाद विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "Aligarh Muslim University evolved from the MAO College founded by Sir Syed Ahmad Khan.",
        "sol_hi": "अलीगढ़ मुस्लिम विश्वविद्यालय (AMU) की उत्पत्ति सर सैयद अहमद खान द्वारा स्थापित एमएओ कॉलेज से हुई है।"
    },
    {
        "q": "Where is the Central Institute for Research on Goats (CIRG) located?",
        "q_hi": "केंद्रीय बकरी अनुसंधान संस्थान (CIRG) कहाँ स्थित है?",
        "opts": ["Mathura", "Bareilly", "Jhansi", "Meerut"],
        "opts_hi": ["मथुरा (Mathura)", "बरेली", "झांसी", "मेरठ"],
        "ans": 0,
        "sol": "CIRG is located in Makhdoom near Mathura.",
        "sol_hi": "बकरी अनुसंधान संस्थान (CIRG) मथुरा के मखदूम में स्थित है।"
    },
    {
        "q": "Which CSIR laboratory in Lucknow is famous for botanical research and plant conservation?",
        "q_hi": "लखनऊ में स्थित कौन सी सीएसआईआर प्रयोगशाला वनस्पति अनुसंधान और संरक्षण के लिए प्रसिद्ध है?",
        "opts": ["CDRI", "NBRI", "CIMAP", "IITR"],
        "opts_hi": ["CDRI", "NBRI (NBRI)", "CIMAP", "IITR"],
        "ans": 1,
        "sol": "The National Botanical Research Institute (NBRI) in Lucknow is dedicated to plant sciences.",
        "sol_hi": "राष्ट्रीय वनस्पति अनुसंधान संस्थान (NBRI) लखनऊ में स्थित है।"
    },
    {
        "q": "Where is the Indian Veterinary Research Institute (IVRI) located?",
        "q_hi": "भारतीय पशु चिकित्सा अनुसंधान संस्थान (IVRI) कहाँ स्थित है?",
        "opts": ["Izatnagar, Bareilly", "Makhdoom, Mathura", "Meerut", "Kanpur"],
        "opts_hi": ["इज्जतनगर, बरेली (Izatnagar)", "मखदूम, मथुरा", "मेरठ", "कानपुर"],
        "ans": 0,
        "sol": "IVRI is located in Izatnagar, Bareilly district.",
        "sol_hi": "पशु चिकित्सा अनुसंधान संस्थान (IVRI) बरेली के इज्जतनगर में स्थित है।"
    },
    {
        "q": "The Indian Institute of Sugarcane Research (IISR) is located in which city?",
        "q_hi": "भारतीय गन्ना अनुसंधान संस्थान (IISR) किस शहर में स्थित है?",
        "opts": ["Kanpur", "Lucknow", "Meerut", "Gorakhpur"],
        "opts_hi": ["कानपुर", "लखनऊ (Lucknow)", "मेरठ", "गोरखपुर"],
        "ans": 1,
        "sol": "IISR is located in Lucknow. (Do not confuse it with National Sugar Institute in Kanpur).",
        "sol_hi": "भारतीय गन्ना अनुसंधान संस्थान (IISR) लखनऊ में स्थित है, जबकि राष्ट्रीय शर्करा संस्थान कानपुर में है।"
    },
    {
        "q": "Where is the Indian Institute of Carpet Technology (IICT) located?",
        "q_hi": "भारतीय कालीन प्रौद्योगिकी संस्थान (IICT) कहाँ स्थित है?",
        "opts": ["Bhadohi", "Mirzapur", "Varanasi", "Sonbhadra"],
        "opts_hi": ["भदोही (Bhadohi)", "मिर्जापुर", "वाराणसी", "सोनभद्र"],
        "ans": 0,
        "sol": "IICT is located in Bhadohi, the carpet industrial hub of UP.",
        "sol_hi": "IICT भदोही जिले में स्थित है।"
    },
    {
        "q": "Which state university of UP dedicated to Sanskrit and cultural heritage is situated in Varanasi?",
        "q_hi": "संस्कृत और सांस्कृतिक विरासत को समर्पित उत्तर प्रदेश का कौन सा राज्य विश्वविद्यालय वाराणसी में स्थित है?",
        "opts": [
            "Sampurnanand Sanskrit Vishwavidyalaya",
            "Bhatkhande Music Institute",
            "Siddharth University",
            "Jagatguru Rambhadracharya Handicapped University"
        ],
        "opts_hi": [
            "सम्पूर्णानन्द संस्कृत विश्वविद्यालय (Sampurnanand)",
            "भातखंडे संगीत संस्थान",
            "सिद्धार्थ विश्वविद्यालय",
            "जगद्गुरु रामभद्राचार्य विकलांग विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "Sampurnanand Sanskrit Vishwavidyalaya is located in Varanasi, established in 1958 (evolving from the Government Sanskrit College founded in 1791).",
        "sol_hi": "वाराणसी में स्थित सम्पूर्णानन्द संस्कृत विश्वविद्यालय की स्थापना 1958 में हुई थी।"
    },
    {
        "q": "Where is the Central Agroforestry Research Institute (CAFRI) located?",
        "q_hi": "केंद्रीय कृषि वानिकी अनुसंधान संस्थान (CAFRI) कहाँ स्थित है?",
        "opts": ["Jhansi", "Banda", "Mathura", "Saharanpur"],
        "opts_hi": ["झांसी (Jhansi)", "बांदा", "मथुरा", "सहारनपुर"],
        "ans": 0,
        "sol": "CAFRI is located in Jhansi.",
        "sol_hi": "केंद्रीय कृषि वानिकी अनुसंधान संस्थान (CAFRI) झांसी में स्थित है।"
    },
    {
        "q": "In which city of UP is the V.V. Giri National Labour Institute located?",
        "q_hi": "उत्तर प्रदेश के किस शहर में 'वी.वी. गिरि राष्ट्रीय श्रम संस्थान' स्थित है?",
        "opts": ["Noida", "Lucknow", "Kanpur", "Ghaziabad"],
        "opts_hi": ["नोएडा (Noida)", "लखनऊ", "कानपुर", "गाजियाबाद"],
        "ans": 0,
        "sol": "The V.V. Giri National Labour Institute is located in Noida.",
        "sol_hi": "वी.वी. गिरि राष्ट्रीय श्रम संस्थान नोएडा में स्थित है।"
    },
    {
        "q": "Which of the following is the oldest state-funded university in Uttar Pradesh?",
        "q_hi": "निम्नलिखित में से कौन सा उत्तर प्रदेश का सबसे पुराना राज्य-वित्त पोषित विश्वविद्यालय है?",
        "opts": [
            "University of Lucknow",
            "Chhatrapati Shahu Ji Maharaj University",
            "Dr. Bhimrao Ambedkar University, Agra",
            "Chaudhary Charan Singh University"
        ],
        "opts_hi": [
            "लखनऊ विश्वविद्यालय (University of Lucknow)",
            "छत्रपति शाहू जी महाराज विश्वविद्यालय",
            "डॉ. भीमराव अंबेडकर विश्वविद्यालय, आगरा",
            "चौधरी चरण सिंह विश्वविद्यालय"
        ],
        "ans": 0,
        "sol": "The University of Lucknow was established in 1921, making it one of the oldest state universities in UP.",
        "sol_hi": "लखनऊ विश्वविद्यालय की स्थापना 1921 में हुई थी, जो राज्य विश्वविद्यालयों में सबसे पुरानी है।"
    },
    {
        "q": "Where is the central headquarters of the Indian Institute of Information Technology (IIIT) in UP?",
        "q_hi": "उत्तर प्रदेश में भारतीय सूचना प्रौद्योगिकी संस्थान (IIIT) का मुख्यालय कहाँ है?",
        "opts": ["Prayagraj", "Lucknow", "Kanpur", "Noida"],
        "opts_hi": ["प्रयागराज (Prayagraj)", "लखनऊ", "कानपुर", "नोएडा"],
        "ans": 0,
        "sol": "IIIT Allahabad is located in Jhalwa, Prayagraj.",
        "sol_hi": "IIIT प्रयागराज के झलवा में स्थित है।"
    },
    {
        "q": "Bhatkhande Sanskriti Vishwavidyalaya, a premier state university for music, is located in which city?",
        "q_hi": "संगीत के लिए प्रमुख राज्य विश्वविद्यालय 'भातखंडे संस्कृति विश्वविद्यालय' किस शहर में स्थित है?",
        "opts": ["Lucknow", "Varanasi", "Prayagraj", "Kanpur"],
        "opts_hi": ["लखनऊ (Lucknow)", "वाराणसी", "प्रयागराज", "कानपुर"],
        "ans": 0,
        "sol": "Bhatkhande Sanskriti Vishwavidyalaya is located in Lucknow.",
        "sol_hi": "भातखंडे संस्कृति विश्वविद्यालय लखनऊ में स्थित है।"
    }
]

def build_practice():
    practice_obj = {"practiceQuestions": practice_questions, "mockTestQuestions": mock_test_questions}
    return practice_obj

def build_theory():
    return {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {"title": f"{TOPIC_DISPLAY} Core Study Notes", "description": "Review Universities and Research Institutes of UP.", "sections": deep_dive_en}
    }

def build_mastery():
    return {
        "sections": [
            {
                "title": "1. Central & State Universities",
                "masteryZone": [
                    {"type": "MCQ", "q": "Which is the oldest Central University in UP?", "opts": ["BHU", "AMU", "University of Allahabad", "BBAU"], "ans": 2, "sol": "University of Allahabad is the oldest central university, founded in 1887."},
                    {"type": "MCQ", "q": "In which year was BHU established?", "opts": ["1911", "1916", "1920", "1927"], "ans": 1, "sol": "BHU was established in 1916 by Pandit Madan Mohan Malaviya."},
                    {"type": "True/False", "q": "True or False: Rajiv Gandhi National Aviation University is located in Raebareli.", "ans": False, "sol": "False. It is located at Fursatganj in Amethi district."},
                    {"type": "One-Liner", "q": "What is the historical nickname of Allahabad University?", "sol": "Oxford of the East"}
                ]
            },
            {
                "title": "2. Research Institutes & Centers",
                "masteryZone": [
                    {"type": "MCQ", "q": "Where is the Indian Institute of Pulses Research (IIPR) located?", "opts": ["Lucknow", "Kanpur", "Varanasi", "Jhansi"], "ans": 1, "sol": "IIPR is located in Kanpur."},
                    {"type": "MCQ", "q": "Where is the Indian Institute of Vegetable Research (IIVR) located?", "opts": ["Lucknow", "Kanpur", "Varanasi", "Noida"], "ans": 2, "sol": "IIVR is located in Shahanshahpur, Varanasi."},
                    {"type": "True/False", "q": "True or False: The National Sugar Institute is located in Lucknow.", "ans": False, "sol": "False. The National Sugar Institute is in Kanpur; the Sugarcane Research Institute is in Lucknow."},
                    {"type": "One-Liner", "q": "Where is the Central Institute for Research on Goats (CIRG) located?", "sol": "Makhdoom, Mathura"}
                ]
            },
            {
                "title": "3. Specialized & Agricultural Institutions",
                "masteryZone": [
                    {"type": "MCQ", "q": "Where is the Indian Grassland and Fodder Research Institute (IGFRI) located?", "opts": ["Jhansi", "Banda", "Meerut", "Mathura"], "ans": 0, "sol": "IGFRI is located in Jhansi."},
                    {"type": "MCQ", "q": "Where is the Indian Veterinary Research Institute (IVRI) located?", "opts": ["Mathura", "Izatnagar (Bareilly)", "Kanpur", "Noida"], "ans": 1, "sol": "IVRI is located in Izatnagar, Bareilly."},
                    {"type": "True/False", "q": "True or False: King George's Medical University is located in Kanpur.", "ans": False, "sol": "False. KGMU is located in Lucknow."},
                    {"type": "One-Liner", "q": "Which city hosts the Indian Institute of Carpet Technology (IICT)?", "sol": "Bhadohi"}
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
        "deepDive": {"title": f"{TOPIC_DISPLAY_HI} के मुख्य अध्ययन नोट्स", "description": "उत्तर प्रदेश के प्रमुख विश्वविद्यालयों और अनुसंधान संस्थानों की समीक्षा।", "sections": deep_dive_hi}
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
                "title": "1. केंद्रीय और राज्य विश्वविद्यालय",
                "masteryZone": [
                    {"type": "MCQ", "q": "उत्तर प्रदेश का सबसे पुराना केंद्रीय विश्वविद्यालय कौन सा है?", "opts": ["BHU", "AMU", "इलाहाबाद विश्वविद्यालय", "BBAU"], "ans": 2, "sol": "इलाहाबाद विश्वविद्यालय सबसे पुराना केंद्रीय विश्वविद्यालय है, जिसकी स्थापना 1887 में हुई थी।"},
                    {"type": "MCQ", "q": "BHU की स्थापना किस वर्ष हुई थी?", "opts": ["1911", "1916", "1920", "1927"], "ans": 1, "sol": "BHU की स्थापना 1916 में पंडित मदन मोहन मालवीय द्वारा की गई थी।"},
                    {"type": "True/False", "q": "सही या गलत: राजीव गांधी राष्ट्रीय विमानन विश्वविद्यालय रायबरेली में स्थित है।", "ans": False, "sol": "गलत। यह अमेठी जिले के फुर्सतगंज में स्थित है।"},
                    {"type": "One-Liner", "q": "इलाहाबाद विश्वविद्यालय का ऐतिहासिक उपनाम क्या है?", "sol": "पूर्व का ऑक्सफोर्ड"}
                ]
            },
            {
                "title": "2. अनुसंधान संस्थान और केंद्र",
                "masteryZone": [
                    {"type": "MCQ", "q": "भारतीय दलहन अनुसंधान संस्थान (IIPR) कहाँ स्थित है?", "opts": ["लखनऊ", "कानपुर", "वाराणसी", "झांसी"], "ans": 1, "sol": "IIPR कानपुर में स्थित है।"},
                    {"type": "MCQ", "q": "भारतीय शाक-भाजी (सब्जी) अनुसंधान संस्थान (IIVR) कहाँ स्थित है?", "opts": ["लखनऊ", "कानपुर", "वाराणसी", "नोएडा"], "ans": 2, "sol": "IIVR वाराणसी के शहंशाहपुर में स्थित है।"},
                    {"type": "True/False", "q": "सही या गलत: राष्ट्रीय शर्करा संस्थान लखनऊ में स्थित है।", "ans": False, "sol": "गलत। राष्ट्रीय शर्करा संस्थान कानपुर में है; भारतीय गन्ना अनुसंधान संस्थान लखनऊ में है।"},
                    {"type": "One-Liner", "q": "केंद्रीय बकरी अनुसंधान संस्थान (CIRG) कहाँ स्थित है?", "sol": "मखदूम, महुआ (मथुरा)"}
                ]
            },
            {
                "title": "3. विशिष्ट और कृषि संस्थान",
                "masteryZone": [
                    {"type": "MCQ", "q": "भारतीय चारागाह एवं चारा अनुसंधान संस्थान (IGFRI) कहाँ स्थित है?", "opts": ["झांसी", "बांदा", "मेरठ", "मथुरा"], "ans": 0, "sol": "IGFRI झांसी में स्थित है।"},
                    {"type": "MCQ", "q": "भारतीय पशु चिकित्सा अनुसंधान संस्थान (IVRI) कहाँ स्थित है?", "opts": ["मथुरा", "इज्जतनगर (बरेली)", "कानपुर", "नोएडा"], "ans": 1, "sol": "IVRI बरेली के इज्जतनगर में स्थित है।"},
                    {"type": "True/False", "q": "सही या गलत: किंग जॉर्ज चिकित्सा विश्वविद्यालय कानपुर में स्थित है।", "ans": False, "sol": "गलत। KGMU लखनऊ में स्थित है।"},
                    {"type": "One-Liner", "q": "भारतीय कालीन प्रौद्योगिकी संस्थान (IICT) किस शहर में स्थित है?", "sol": "भदोही"}
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
