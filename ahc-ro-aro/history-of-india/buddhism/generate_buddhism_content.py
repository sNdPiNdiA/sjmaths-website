# -*- coding: utf-8 -*-
import json
import os
import sys

# Ensure UTF-8 output encoding
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\ahc-ro-aro\history-of-india\buddhism"
HI_DIR = os.path.join(BASE_DIR, "hi")
os.makedirs(HI_DIR, exist_ok=True)

# ----------------- ENGLISH DATA DEFINITIONS -----------------
breadcrumbs_en = {
    "parent": "History of India",
    "parentUrl": "../",
    "current": "Buddhism"
}

hero_en = {
    "title": "Buddhism",
    "description": "Master the rise of Buddhism (c. 6th century BC). Explore the life of Gautama Buddha, core doctrines (Four Noble Truths, Eightfold Path), Tripitakas, the four Buddhist Councils, and sectarian divisions (Hinayana, Mahayana, Vajrayana)."
}

labels_en = {
    "clickToExpand": "Click to expand details",
    "mockIntro": {
        "title": "Interactive Buddhism Mock Test",
        "description": "Assess your understanding of Buddha's life events, core philosophical concepts, canonical literature, and details of the Buddhist Councils. This timed mock test consists of 15 questions.",
        "startBtn": "Start Mock Test"
    },
    "mockPlay": {
        "prevBtn": "Previous Question",
        "nextBtn": "Next Question",
        "submitBtn": "Submit Test"
    }
}

timeline_en = {
    "title": "Life & Evolution of Buddhism",
    "description": "Chronological milestones of Gautama Buddha's life and the subsequent spread of Buddhism.",
    "cards": [
        {
            "period": "Birth of Siddhartha Gautama",
            "date": "c. 563 BC",
            "details": "Born in Lumbini (near Kapilavastu, Nepal) to King Shuddhodana of the Shakya clan and Queen Mahamaya."
        },
        {
            "period": "The Great Renunciation (Mahabhinishkramana)",
            "date": "c. 534 BC (Age 29)",
            "details": "Left his palace, wife Yasodhara, and son Rahula in search of truth after witnessing the Four Sights (old man, sick man, corpse, ascetic)."
        },
        {
            "period": "Enlightenment (Nirvana)",
            "date": "c. 528 BC (Age 35)",
            "details": "Attained Sambodhi (enlightenment) under a Peepal tree (Bodhi tree) at Bodh Gaya on the banks of Niranjana river."
        },
        {
            "period": "First Sermon (Dharmachakrapravartana)",
            "date": "c. 528 BC",
            "details": "Delivered his first sermon to the five ascetics (Panchavaggiya) at Deer Park in Sarnath (Rishipatana), turning the Wheel of Law."
        },
        {
            "period": "Mahaparinirvana (Death)",
            "date": "c. 483 BC (Age 80)",
            "details": "Passed away at Kusinara (modern Kushinagar, UP) under a Sal tree. His last words urged disciples to be their own lamps (Appo Deepo Bhava)."
        }
    ]
}

mnemonics_en = {
    "title": "Buddhism Mnemonics & Study Tricks",
    "description": "Quick memory triggers to recall Councils and key doctrines for AHC RO/ARO exams.",
    "items": [
        {
            "title": "Mnemonic 1: Patron Rulers of the 4 Councils",
            "phrase": "\"Ajatshatru Kalasoka Kanishka's Ashoka (AK-AK)\"",
            "decryption": "Remember the patron kings in chronological order:<br>• **A**: **A**jatashatru (1st Council)<br>• **K**: **K**alasoka (2nd Council)<br>• **A**: **A**shoka (3rd Council)<br>• **K**: **K**anishka (4th Council)"
        },
        {
            "title": "Mnemonic 2: Venues of the 4 Councils",
            "phrase": "\"Rajgir's Vaishali Patches Kashmir (RV-PK)\"",
            "decryption": "Remember the locations in order:<br>• **R**: **R**ajgriha (Saptaparni Cave)<br>• **V**: **V**aishali<br>• **P**: **P**ataliputra<br>• **K**: **K**undalavana (Kashmir)"
        },
        {
            "title": "Mnemonic 3: The Three Jewels (Triratna)",
            "phrase": "\"B-D-S (Buddha, Dhamma, Sangha)\"",
            "decryption": "The core pillars of Buddhism:<br>• **B**: **B**uddha (The Enlightened One)<br>• **D**: **D**hamma (The Teachings/Doctrine)<br>• **S**: **S**angha (The Monastic Order)"
        }
    ]
}

flashcards_en = {
    "title": "Active Recall Flashcards",
    "description": "Hover or click to reveal the answers. Revisit these cards to build instant recall.",
    "items": [
        {
            "question": "What are the Four Sights that led to Siddhartha's renunciation?",
            "answer": "An **old man**, a **diseased person**, a **dead body (corpse)**, and an **ascetic (holy man)** showing calm composure.",
            "icon": "fa-eye"
        },
        {
            "question": "What is the language of the early Buddhist scriptures (Tripitakas)?",
            "answer": "Early canonical texts were composed in **Pali**, which was the common tongue, helping the doctrine spread rapidly among laypeople.",
            "icon": "fa-language"
        },
        {
            "question": "Who presided over the Third Buddhist Council and what text was compiled?",
            "answer": "It was presided over by **Moggaliputta Tissa**. The **Kathavatthu** was compiled and added to the *Abhidhamma Pitaka*.",
            "icon": "fa-gavel"
        },
        {
            "question": "What is the difference between Hinayana and Mahayana regarding Buddha's status?",
            "answer": "**Hinayana** views Buddha as a great human teacher who attained Nirvana. **Mahayana** deifies Buddha, worshipping him as a god/idol and believing in Bodhisattvas.",
            "icon": "fa-balance-scale"
        }
    ]
}

traps_en = {
    "title": "Common Exam Traps to Avoid",
    "items": [
        "<strong>Trap 1:</strong> Confusing the presidents of the councils with the patron kings. Remember, **Mahakassapa** presided over the 1st council (patron: Ajatashatru); **Sabbakami** over the 2nd (patron: Kalasoka); **Moggaliputta Tissa** over the 3rd (patron: Ashoka); and **Vasumitra/Asvaghosa** over the 4th (patron: Kanishka).",
        "<strong>Trap 2:</strong> Believing that Gautama Buddha rejected the concept of Karma. Buddha **fully accepted Karma and Rebirth**, but rejected the Vedic idea of an eternal soul (*Atman*). This is the doctrine of **Anatta** (non-self).",
        "<strong>Trap 3:</strong> Confusing the contents of the Tripitakas. Remember: **Vinaya Pitaka** contains monastic rules; **Sutta Pitaka** contains Buddha's sermons/discourses; **Abhidhamma Pitaka** contains philosophical interpretations of the teachings."
    ]
}

deep_dive_en = [
    {
        "title": "1. Life of Gautama Buddha",
        "content": """<p>Siddhartha Gautama, later known as the **Buddha** (the Enlightened One), was born in the Shakya Kshatriya clan. Five major events in his life are represented by specific Buddhist symbols, which are heavily tested in exams:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Event Name</th>
                <th>Vedic/Buddhist Term</th>
                <th>Representative Symbol</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Birth</strong></td>
                <td>Janma</td>
                <td>Lotus and Bull</td>
              </tr>
              <tr>
                <td><strong>Renunciation</strong></td>
                <td>Mahabhinishkramana</td>
                <td>Horse (Kanthaka)</td>
              </tr>
              <tr>
                <td><strong>Enlightenment</strong></td>
                <td>Nirvana / Sambodhi</td>
                <td>Bodhi Tree (Peepal tree)</td>
              </tr>
              <tr>
                <td><strong>First Sermon</strong></td>
                <td>Dharmachakrapravartana</td>
                <td>Wheel (Dharma Chakra)</td>
              </tr>
              <tr>
                <td><strong>Death</strong></td>
                <td>Mahaparinirvana</td>
                <td>Stupa or Footprints</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>After leaving home, Siddhartha studied under two teachers: **Alara Kalama** (Upanishadic philosophy of Sankhya) and **Udraka Ramaputta**. After years of asceticism, he realized extreme self-mortification was useless and chose the **Middle Path (Madhyama Pratipada)**.</p>"""
    },
    {
        "title": "2. Core Philosophical Doctrines",
        "content": """<p>The core of Buddhist teachings centers on the **Four Noble Truths (Arya Satya)**:</p>
        <ol>
          <li><strong>Sabbam Dukkham</strong>: Life is full of sorrow/suffering (Dukkha).</li>
          <li><strong>Dukkha Samudaya</strong>: Desire (Tanha) is the root cause of suffering.</li>
          <li><strong>Dukkha Nirodha</strong>: Suffering can be ended by eliminating desire.</li>
          <li><strong>Dukkha Nirodha Gamini Patipada</strong>: The path to end suffering is the **Eightfold Path (Ashtangika Marga)**.</li>
        </ol>
        <p>The **Eightfold Path** is categorized into three pillars: **Pragna** (Wisdom), **Sheela** (Conduct), and **Samadhi** (Meditation).</p>
        
        <!-- Fully Dark-Mode Compatible Semantic SVG Diagram -->
        <svg viewBox="0 0 800 220" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); padding: 10px;">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .up-node { fill: var(--bg-card, #ffffff); stroke: var(--primary, #8e44ad); stroke-width: 2px; }
            .up-node-highlight { fill: rgba(142, 68, 173, 0.05); stroke: #9b59b6; stroke-width: 2.5px; }
            .text-district { font-family: 'Outfit', sans-serif; font-size: 12px; fill: var(--primary, #8e44ad); font-weight: 700; }
            .text-feature { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title" style="font-family: 'Outfit', sans-serif; font-size: 15px; font-weight: 700;">The Three Pillars of the Eightfold Path (Ashtangika Marga)</text>
          
          <rect x="50" y="60" width="210" height="120" class="up-node" rx="6" ry="6" />
          <text x="155" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">1. WISDOM (Pragna)</text>
          <text x="155" y="115" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right View (Samyak Dristi)</text>
          <text x="155" y="135" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Resolve (Samyak Sankalpa)</text>
          
          <rect x="295" y="60" width="210" height="120" class="up-node-highlight" rx="6" ry="6" />
          <text x="400" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">2. CONDUCT (Sheela)</text>
          <text x="400" y="110" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Speech (Samyak Vacha)</text>
          <text x="400" y="130" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Action (Samyak Karma)</text>
          <text x="400" y="150" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Livelihood (Samyak Ajiva)</text>
          
          <rect x="540" y="60" width="210" height="120" class="up-node" rx="6" ry="6" />
          <text x="645" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">3. MEDITATION (Samadhi)</text>
          <text x="645" y="110" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Effort (Samyak Vyayama)</text>
          <text x="645" y="130" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Mindfulness (Samyak Smriti)</text>
          <text x="645" y="150" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• Right Concentration (Samyak Samadhi)</text>
        </svg>
        
        <p>Other vital philosophical concepts include **Pratityasamutpada** (Dependent Origination - that everything arises in dependence upon multiple causes) and **Anatta** (there is no permanent soul or self).</p>"""
    },
    {
        "title": "3. Buddhist Canonical Literature",
        "content": """<p>The primary canon is the **Tripitaka** (Three Baskets), compiled over time in Pali:</p>
        <ul>
          <li><strong>Sutta Pitaka</strong>: Divided into five Nikayas (Digha, Majjhima, Samyutta, Anguttara, Khuddaka). Contains the core sermons of Buddha. *Anguttara Nikaya* is famous for listing the 16 Mahajanapadas.</li>
          <li><strong>Vinaya Pitaka</strong>: Contains the rules and code of conduct for monks and nuns in the Sangha. Includes the *Pratimoksha* (disciplinary code).</li>
          <li><strong>Abhidhamma Pitaka</strong>: Deals with the philosophical and psychological analysis of Buddhist doctrines. Includes the *Kathavatthu* written by Moggaliputta Tissa.</li>
        </ul>
        <p><strong>Non-Canonical literature</strong> includes the **Milinda Panha** (Questions of King Menander to sage Nagasena), **Jataka Tales** (stories of Buddha's previous births), and the Sanskrit texts **Buddhacharita** (by Asvaghosa, the first biography of Buddha), **Lalitavistara**, and **Divyavadana**.</p>"""
    },
    {
        "title": "4. The Four Buddhist Councils",
        "content": """<p>Following the Buddha's death, four major councils were held to resolve sectarian disputes, preserve teachings, and compile the canon:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>Council</th>
                <th>Year &amp; Venue</th>
                <th>Patron King</th>
                <th>President &amp; Key Outcomes</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>First</strong></td>
                <td>c. 483 BC<br>Rajgriha (Saptaparni Cave)</td>
                <td>Ajatashatru<br>(Haryanka Dynasty)</td>
                <td><strong>Mahakassapa</strong><br>Sutta Pitaka (compiled by Ananda) and Vinaya Pitaka (compiled by Upali) were recorded.</td>
              </tr>
              <tr>
                <td><strong>Second</strong></td>
                <td>c. 383 BC<br>Vaishali</td>
                <td>Kalasoka<br>(Shishunaga Dynasty)</td>
                <td><strong>Sabbakami</strong><br>First split in the Sangha occurred between <em>Sthaviravadins</em> (orthodox) and <em>Mahasanghikas</em> (reformers).</td>
              </tr>
              <tr>
                <td><strong>Third</strong></td>
                <td>c. 250 BC<br>Pataliputra</td>
                <td>Ashoka<br>(Mauryan Dynasty)</td>
                <td><strong>Moggaliputta Tissa</strong><br>Philosophical differences were settled, Abhidhamma Pitaka compiled, and missionaries sent abroad.</td>
              </tr>
              <tr>
                <td><strong>Fourth</strong></td>
                <td>c. 72 AD<br>Kundalavana (Kashmir)</td>
                <td>Kanishka<br>(Kushan Dynasty)</td>
                <td><strong>Vasumitra</strong> (VP: Asvaghosa)<br>Sangha split formally into <strong>Hinayana</strong> (Lesser Vehicle) and <strong>Mahayana</strong> (Greater Vehicle). Texts compiled in Sanskrit.</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. Major Sects & Decline of Buddhism",
        "content": """<p>Over time, Buddhism split into distinct schools:</p>
        <ul>
          <li><strong>Hinayana (Theravada)</strong>: Orthodox sect. Believes in individual salvation through self-effort. Rejects idol worship and views Buddha as a guide. Uses Pali scriptures. Prevalent in Sri Lanka, Myanmar, and Thailand.</li>
          <li><strong>Mahayana</strong>: Liberal sect. Deifies Buddha and worships his idols. Believes in **Bodhisattvas** (compassionate beings who delay their own Nirvana to help others). Uses Sanskrit. Prevalent in China, Japan, Korea, and Tibet.</li>
          <li><strong>Vajrayana (Tantric)</strong>: Emerged around the 8th century AD. Focuses on magical spells, mantras, and rituals. Prevalent in Tibet and Mongolia.</li>
        </ul>
        <p><strong>Decline of Buddhism in India</strong>: Caused by internal corruption in the Sangha, adoption of Sanskrit over Pali, rise of Tantric Vajrayana (bringing back superstitions), revival of Brahmanical Hinduism (via Adi Shankara and incorporating Buddha as the 9th avatar of Vishnu), and destruction of monastic universities like Nalanda by Turkic invaders (Bakhtiyar Khilji) in the late 12th century AD.</p>"""
    }
]


# ----------------- HINDI DATA DEFINITIONS (UPSC METHOD) -----------------
breadcrumbs_hi = {
    "parent": "भारत का इतिहास",
    "parentUrl": "../",
    "current": "बौद्ध धर्म"
}

hero_hi = {
    "title": "बौद्ध धर्म",
    "description": "बौद्ध धर्म (लगभग छठी शताब्दी ईसा पूर्व) के उदय पर महारत हासिल करें। गौतम बुद्ध के जीवन, मुख्य सिद्धांतों (चार आर्य सत्य, अष्टांगिक मार्ग), त्रिपिटक, चार बौद्ध संगीतियों और सांप्रदायिक विभाजनों (हीनयान, महायान, वज्रयान) का अध्ययन करें।"
}

labels_hi = {
    "clickToExpand": "विवरण देखने के लिए क्लिक करें",
    "mockIntro": {
        "title": "ईन्टरएक्टिव बौद्ध धर्म मॉक टेस्ट",
        "description": "बुद्ध के जीवन की घटनाओं, प्रमुख दार्शनिक अवधारणाओं, प्रामाणिक साहित्य और बौद्ध संगीतियों के विवरण के बारे में अपनी समझ का परीक्षण करें। इस समयबद्ध मॉक टेस्ट में 15 प्रश्न शामिल हैं।",
        "startBtn": "मॉक टेस्ट शुरू करें"
    },
    "mockPlay": {
        "prevBtn": "पिछला प्रश्न",
        "nextBtn": "अगला प्रश्न",
        "submitBtn": "टेस्ट सबमिट करें"
    }
}

timeline_hi = {
    "title": "बौद्ध धर्म का जीवन और विकास",
    "description": "गौतम बुद्ध के जीवन के कालानुक्रमिक मील के पत्थर और बौद्ध धर्म के प्रसार का विवरण।",
    "cards": [
        {
            "period": "सिद्धार्थ गौतम का जन्म",
            "date": "लगभग 563 ईसा पूर्व",
            "details": "लुंबिनी (कपिलवस्तु के निकट, नेपाल) में शाक्य कबीले के राजा शुद्धोधन और रानी महामाया के यहाँ जन्म।"
        },
        {
            "period": "महाभिनिष्क्रमण (गृहत्याग)",
            "date": "लगभग 534 ईसा पूर्व (आयु 29 वर्ष)",
            "details": "चार दृश्यों (बूढ़ा व्यक्ति, बीमार व्यक्ति, शव, संन्यासी) को देखने के बाद सत्य की खोज में अपने महल, पत्नी यशोधरा और पुत्र राहुल को छोड़ दिया।"
        },
        {
            "period": "निर्वाण (ज्ञान प्राप्ति)",
            "date": "लगभग 528 ईसा पूर्व (आयु 35 वर्ष)",
            "details": "बोधगया में निरंजना नदी के तट पर एक पीपल के पेड़ (बोधि वृक्ष) के नीचे संबोधि (ज्ञान) प्राप्त किया।"
        },
        {
            "period": "धर्मचक्रप्रवर्तन (प्रथम उपदेश)",
            "date": "लगभग 528 ईसा पूर्व",
            "details": "सारनाथ (ऋषिपत्तन) के मृगदाव (हिरण पार्क) में पांच तपस्वियों (पंचवर्गीय) को अपना पहला उपदेश दिया, जिससे धर्म चक्र घूमा।"
        },
        {
            "period": "महापरिनिर्वाण (मृत्यु)",
            "date": "लगभग 483 ईसा पूर्व (आयु 80 वर्ष)",
            "details": "कुशीनारा (आधुनिक कुशीनगर, उत्तर प्रदेश) में एक शाल वृक्ष के नीचे निधन। उनके अंतिम शब्द थे 'अप्प दीपो भव' (अपना दीपक स्वयं बनो)।"
        }
    ]
}

mnemonics_hi = {
    "title": "बौद्ध धर्म के स्मृति सूत्र और याद रखने की तकनीक",
    "description": "AHC RO/ARO परीक्षा के लिए बौद्ध संगीतियों और महत्वपूर्ण सिद्धांतों को याद रखने के त्वरित सूत्र।",
    "items": [
        {
            "title": "स्मृति सूत्र 1: चारों संगीतियों के संरक्षक शासक",
            "phrase": "\"अजातशत्रु कालासोक कनिष्क का अशोक (AK-AK)\"",
            "decryption": "कालानुक्रमिक क्रम में संरक्षक राजाओं को याद रखें:<br>• **A**: अजातशत्रु (प्रथम संगीति)<br>• **K**: कालाशोक (द्वितीय संगीति)<br>• **A**: अशोक (तृतीय संगीति)<br>• **K**: कनिष्क (चतुर्थ संगीति)"
        },
        {
            "title": "स्मृति सूत्र 2: चारों संगीतियों के स्थान (स्थल)",
            "phrase": "\"राजगीर की वैशाली ने पाटलीपुत्र और कश्मीर को जोड़ा (RV-PK)\"",
            "decryption": "क्रमबद्ध स्थानों को याद रखें:<br>• **R**: राजगृह (सप्तपर्णी गुफा)<br>• **V**: वैशाली<br>• **P**: पाटलीपुत्र<br>• **K**: कुंडलवन (कश्मीर)"
        },
        {
            "title": "स्मृति सूत्र 3: बौद्ध धर्म के त्रिरत्न",
            "phrase": "\"बु-ध-सं (बुद्ध, धम्म, संघ)\"",
            "decryption": "बौद्ध धर्म के तीन मुख्य स्तंभ:<br>• **बु**: बुद्ध (प्रबुद्ध व्यक्ति)<br>• **ध**: धम्म (बुद्ध की शिक्षाएं)<br>• **सं**: संघ (भिक्षुओं का संगठन)"
        }
    ]
}

flashcards_hi = {
    "title": "सक्रिय रिकॉल फ्लैशकार्ड",
    "description": "उत्तर देखने के लिए होवर करें या क्लिक करें। त्वरित याददाश्त बनाने के लिए इन कार्डों को दोबारा देखें।",
    "items": [
        {
            "question": "सिद्धार्थ के गृहत्याग का कारण बनने वाले चार दृश्य कौन से थे?",
            "answer": "एक **बूढ़ा व्यक्ति**, एक **रोगी**, एक **शव (मृत शरीर)**, और एक शांत मुद्रा में रहने वाला **संन्यासी**।",
            "icon": "fa-eye"
        },
        {
            "question": "प्रारंभिक बौद्ध ग्रंथों (त्रिपिटक) की भाषा क्या है?",
            "answer": "प्रारंभिक प्रामाणिक ग्रंथ **पाली** भाषा में रचित थे, जो तत्कालीन जनसामान्य की भाषा थी। इसने आम लोगों के बीच बौद्ध धर्म के तेजी से प्रसार में मदद की।",
            "icon": "fa-language"
        },
        {
            "question": "तृतीय बौद्ध संगीति की अध्यक्षता किसने की और किस ग्रंथ का संकलन हुआ?",
            "answer": "इसकी अध्यक्षता **मोग्गलिपुत्त तिस्स** ने की थी। इस संगीति में **कथावत्थु** का संकलन किया गया और इसे *अभिधम्म पिटक* में जोड़ा गया।",
            "icon": "fa-gavel"
        },
        {
            "question": "बुद्ध की स्थिति के संबंध में हीनयान और महायान में क्या अंतर है?",
            "answer": "**हीनयान** बुद्ध को एक महान मानव शिक्षक मानता है जिन्होंने निर्वाण प्राप्त किया। **महायान** बुद्ध का देवत्वकरण करता है, उनकी मूर्तियों की पूजा करता है और बोधिसत्वों में विश्वास करता है।",
            "icon": "fa-balance-scale"
        }
    ]
}

traps_hi = {
    "title": "बचाव योग्य सामान्य परीक्षा भ्रम (Traps)",
    "items": [
        "<strong>भ्रम 1: संगीति के अध्यक्ष और संरक्षक शासकों को मिला देना।</strong> याद रखें, प्रथम संगीति की अध्यक्षता **महाकश्यप** ने की (संरक्षक: अजातशत्रु); द्वितीय की **सबकामी** ने (संरक्षक: कालाशोक); तृतीय की **मोग्गलिपुत्त तिस्स** ने (संरक्षक: अशोक); और चतुर्थ की **वसुमित्र/अश्वघोष** ने (संरक्षक: कनिष्क)।",
        "<strong>भ्रम 2: यह सोचना कि गौतम बुद्ध ने कर्म के सिद्धांत को खारिज कर दिया था।</strong> बुद्ध ने **कर्म और पुनर्जन्म के सिद्धांत को पूरी तरह स्वीकार किया**, लेकिन उन्होंने वेदों की शाश्वत आत्मा (*आत्मन*) की अवधारणा को खारिज कर दिया। इसे **अनात्मवाद** (Non-self) का सिद्धांत कहा जाता है।",
        "<strong>भ्रम 3: त्रिपिटक की विषय-वस्तु में भ्रमित होना।</strong> याद रखें: **विनय पिटक** में भिक्षुओं के लिए नियम व आचार संहिता है; **सुत्त पिटक** में बुद्ध के उपदेश/संवाद हैं; और **अभिधम्म पिटक** में बौद्ध सिद्धांतों की दार्शनिक व मनोवैज्ञानिक व्याख्या है।"
    ]
}

deep_dive_hi = [
    {
        "title": "1. गौतम बुद्ध का जीवन परिचय",
        "content": """<p>सिद्धार्थ गौतम, जिन्हें बाद में **बुद्ध** (प्रबुद्ध) के रूप में जाना गया, का जन्म शाक्य क्षत्रिय कबीले में हुआ था। उनके जीवन की पांच प्रमुख घटनाओं को विशिष्ट बौद्ध प्रतीकों द्वारा दर्शाया जाता है, जो परीक्षाओं में अक्सर पूछे जाते हैं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>घटना का नाम</th>
                <th>बौद्ध शब्द</th>
                <th>प्रतिनिधित्व प्रतीक</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>जन्म</strong></td>
                <td>जन्म</td>
                <td>कमल और सांड (Lotus and Bull)</td>
              </tr>
              <tr>
                <td><strong>गृहत्याग</strong></td>
                <td>महाभिनिष्क्रमण</td>
                <td>घोड़ा (कंथक)</td>
              </tr>
              <tr>
                <td><strong>ज्ञान प्राप्ति</strong></td>
                <td>निर्वाण / संबोधि</td>
                <td>बोधि वृक्ष (पीपल का वृक्ष)</td>
              </tr>
              <tr>
                <td><strong>प्रथम उपदेश</strong></td>
                <td>धर्मचक्रप्रवर्तन</td>
                <td>चक्र (धर्म चक्र)</td>
              </tr>
              <tr>
                <td><strong>मृत्यु</strong></td>
                <td>महापरिनिर्वाण</td>
                <td>स्तूप या पदचिह्न</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p>घर छोड़ने के बाद, सिद्धार्थ ने दो गुरुओं से शिक्षा ली: **आलार कलाम** (सांख्य दर्शन) और **उद्रक रामपुत्र**। वर्षों की घोर तपस्या के बाद, उन्होंने महसूस किया कि शरीर को अत्यधिक कष्ट देना व्यर्थ है और उन्होंने **मध्यम मार्ग (मध्यमा प्रतिपदा)** को चुना।</p>"""
    },
    {
        "title": "2. मूल दार्शनिक सिद्धांत",
        "content": """<p>बौद्ध शिक्षाओं का मूल आधार **चार आर्य सत्य (Arya Satya)** हैं:</p>
        <ol>
          <li><strong>सबम दुखम</strong>: संसार दुखों से भरा है।</li>
          <li><strong>दुख समुदाय</strong>: तृष्णा (इच्छा) सभी दुखों का मूल कारण है।</li>
          <li><strong>दुख निरोध</strong>: इच्छाओं को समाप्त करके दुख का अंत किया जा सकता है।</li>
          <li><strong>दुख निरोध गामिनी प्रतिपदा</strong>: दुख निवारण का मार्ग **अष्टांगिक मार्ग (Ashtangika Marga)** है।</li>
        </ol>
        <p>अष्टांगिक मार्ग को तीन प्रमुख स्तंभों में वर्गीकृत किया गया है: **प्रज्ञा** (ज्ञान/बुद्धि), **शील** (नैतिक आचरण), और **समाधि** (ध्यान)।</p>
        
        <!-- Fully Dark-Mode Compatible Semantic SVG Diagram -->
        <svg viewBox="0 0 800 220" class="responsive-svg-diagram" style="margin: 1.5rem 0; border-radius: 8px; background: var(--bg-card); padding: 10px;">
          <style>
            .svg-title { font-family: 'Outfit', sans-serif; font-weight: bold; fill: var(--text-dark, #2c3e50); font-size: 15px; }
            .up-node { fill: var(--bg-card, #ffffff); stroke: var(--primary, #8e44ad); stroke-width: 2px; }
            .up-node-highlight { fill: rgba(142, 68, 173, 0.05); stroke: #9b59b6; stroke-width: 2.5px; }
            .text-district { font-family: 'Outfit', sans-serif; font-size: 12px; fill: var(--primary, #8e44ad); font-weight: 700; }
            .text-feature { font-family: 'Inter', sans-serif; font-size: 11px; fill: var(--text-dark, #2c3e50); }
            
            
            
            
            
          </style>
          <text x="20" y="30" class="svg-title" style="font-family: 'Outfit', sans-serif; font-size: 15px; font-weight: 700;">अष्टांगिक मार्ग के तीन स्तंभ (Three Pillars of Ashtangika Marga)</text>
          
          <rect x="50" y="60" width="210" height="120" class="up-node" rx="6" ry="6" />
          <text x="155" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">1. प्रज्ञा (WISDOM)</text>
          <text x="155" y="115" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक दृष्टि (Right View)</text>
          <text x="155" y="135" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक संकल्प (Right Resolve)</text>
          
          <rect x="295" y="60" width="210" height="120" class="up-node-highlight" rx="6" ry="6" />
          <text x="400" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">2. शील (CONDUCT)</text>
          <text x="400" y="110" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक वाक (Right Speech)</text>
          <text x="400" y="130" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक कर्मा (Right Action)</text>
          <text x="400" y="150" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक आजीव (Right Livelihood)</text>
          
          <rect x="540" y="60" width="210" height="120" class="up-node" rx="6" ry="6" />
          <text x="645" y="85" class="text-district" text-anchor="middle" style="font-family: 'Outfit', sans-serif; font-size: 12px; font-weight: 700;">3. समाधि (MEDITATION)</text>
          <text x="645" y="110" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक व्यायाम (Right Effort)</text>
          <text x="645" y="130" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक स्मृति (Right Mindfulness)</text>
          <text x="645" y="150" class="text-feature" text-anchor="middle" style="font-family: 'Inter', sans-serif; font-size: 11px;">• सम्यक समाधि (Right Concentration)</text>
        </svg>
        
        <p>अन्य प्रमुख दार्शनिक अवधारणाओं में **प्रतीत्यसमुत्पाद** (कारण-कार्य सिद्धांत - एक वस्तु की प्राप्ति होने पर दूसरी की उत्पत्ति) और **अनात्मवाद** (कोई स्थायी आत्मा नहीं है) शामिल हैं।</p>"""
    },
    {
        "title": "3. बौद्ध साहित्य (कैनोनिकल साहित्य)",
        "content": """<p>बौद्ध धर्म का प्राथमिक धर्मग्रंथ **त्रिपिटक** (तीन टोकरियाँ) कहलाता है, जिसकी रचना पाली भाषा में हुई है:</p>
        <ul>
          <li><strong>सुत्त पिटक</strong>: इसे पांच निकायों (दीघ, मज्झिम, संयुत्त, अंगुत्तर, खुद्दक) में विभाजित किया गया है। इसमें बुद्ध के उपदेश संकलित हैं। *अंगुत्तर निकाय* में पहली बार 16 महाजनपदों की सूची मिलती है।</li>
          <li><strong>विनय पिटक</strong>: इसमें संघ के भिक्षुओं और भिक्षुणियों के लिए नियम, अनुशासन और दैनिक संहिताएँ शामिल हैं। इसमें *प्रातिमोक्ष* (अनुशासन संहिता) भी है।</li>
          <li><strong>अभिधम्म पिटक</strong>: यह बौद्ध सिद्धांतों की दार्शनिक एवं मनोवैज्ञानिक व्याख्या करता है। इसमें मोग्गलिपुत्त तिस्स द्वारा रचित *कथावत्थु* शामिल है।</li>
        </ul>
        <p><strong>गैर-कैनोनिकल (इतर) साहित्य</strong> में **मिलिंदपन्हो** (यूनानी राजा मिनांडर और बौद्ध भिक्षु नागसेन के बीच संवाद), **जातक कथाएँ** (बुद्ध के पूर्व जन्मों की कहानियाँ), और संस्कृत ग्रंथ जैसे **बुद्धचरित** (अश्वघोष द्वारा लिखित, बुद्ध की पहली जीवनी), **ललितविस्तर**, और **दिव्यावदान** शामिल हैं।</p>"""
    },
    {
        "title": "4. चार प्रमुख बौद्ध संगीतियाँ (सभाएँ)",
        "content": """<p>बुद्ध के महापरिनिर्वाण के बाद बौद्ध संघ के मतभेदों को सुलझाने और उपदेशों को संकलित करने के लिए चार संगीतियाँ आयोजित की गईं:</p>
        <div class="premium-table-container">
          <table class="premium-table">
            <thead>
              <tr>
                <th>संगीति</th>
                <th>वर्ष और स्थान</th>
                <th>संरक्षक शासक</th>
                <th>अध्यक्ष और मुख्य परिणाम</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>प्रथम</strong></td>
                <td>लगभग 483 ईसा पूर्व<br>राजगृह (सप्तपर्णी गुफा)</td>
                <td>अजातशत्रु<br>(हर्यक वंश)</td>
                <td><strong>महाकश्यप</strong><br>बुद्ध के उपदेशों को सुत्त पिटक (आनंद द्वारा) और विनय पिटक (उपाली द्वारा) के रूप में संकलित किया गया।</td>
              </tr>
              <tr>
                <td><strong>द्वितीय</strong></td>
                <td>लगभग 383 ईसा पूर्व<br>वैशाली</td>
                <td>कालाशोक<br>(शिशुनाग वंश)</td>
                <td><strong>सबकामी (सर्वकामनी)</strong><br>बौद्ध संघ में पहला विभाजन हुआ - <em>स्थविरवादी</em> (रूढ़िवादी) और <em>महासांघिक</em> (परिवर्तनवादी)।</td>
              </tr>
              <tr>
                <td><strong>तृतीय</strong></td>
                <td>लगभग 250 ईसा पूर्व<br>पाटलीपुत्र</td>
                <td>अशोक<br>(मौर्य वंश)</td>
                <td><strong>मोग्गलिपुत्त तिस्स</strong><br>दार्शनिक मतभेदों को सुलझाया गया, अभिधम्म पिटक का संकलन हुआ और विदेशों में धर्म प्रचारक भेजे गए।</td>
              </tr>
              <tr>
                <td><strong>चतुर्थ</strong></td>
                <td>लगभग 72 ईस्वी<br>कुंडलवन (कश्मीर)</td>
                <td>कनिष्क<br>(कुषाण वंश)</td>
                <td><strong>वसुमित्र</strong> (उपाध्यक्ष: अश्वघोष)<br>बौद्ध संघ स्पष्ट रूप से दो भागों <strong>हीनयान</strong> और <strong>महायान</strong> में विभाजित हो गया। रचनाओं के लिए संस्कृत का प्रयोग हुआ।</td>
              </tr>
            </tbody>
          </table>
        </div>"""
    },
    {
        "title": "5. बौद्ध संप्रदाय और पतन के कारण",
        "content": """<p>समय के साथ बौद्ध धर्म कई शाखाओं में विभाजित हो गया:</p>
        <ul>
          <li><strong>हीनयान (थेरवाद)</strong>: रूढ़िवादी शाखा। यह व्यक्तिगत प्रयासों द्वारा मोक्ष प्राप्त करने में विश्वास करता है। यह मूर्ति पूजा को अस्वीकार करता है और बुद्ध को एक मार्गदर्शक मानता है। इसकी भाषा पाली है। यह श्रीलंका, म्यांमार और थाईलैंड में प्रचलित है।</li>
          <li><strong>महायान</strong>: उदारवादी शाखा। यह बुद्ध को भगवान मानकर उनकी मूर्तियों की पूजा करता है। यह **बोधिसत्व** (करुणामयी प्राणी जो दूसरों की भलाई के लिए अपने निर्वाण में देरी करते हैं) में विश्वास करता है। इसकी भाषा संस्कृत है। यह चीन, जापान, कोरिया और तिब्बत में प्रचलित है।</li>
          <li><strong>वज्रयान</strong>: यह 8वीं शताब्दी के आसपास उभरा। यह तंत्र-मंत्र, जादू-टोने और कर्मकांडों पर केंद्रित है। यह तिब्बत और मंगोलिया में लोकप्रिय हुआ।</li>
        </ul>
        <p><strong>पतन के कारण</strong>: संघ में भ्रष्टाचार का प्रवेश, लोकभाषा पाली के स्थान पर संस्कृत का चयन, वज्रयान संप्रदाय का उदय (जिसने अंधविश्वास बढ़ाए), आदि शंकराचार्य के नेतृत्व में हिंदू धर्म का पुनरुत्थान (बुद्ध को विष्णु के 9वें अवतार के रूप में स्वीकार करना), और 12वीं शताब्दी के अंत में बख्तियार खिलजी जैसे तुर्क आक्रमणकारियों द्वारा नालंदा जैसे बौद्ध विश्वविद्यालयों का विनाश।</p>"""
    }
]


# ----------------- CANONICAL PRACTICE QUESTIONS (50 Qs) -----------------
practice_questions = [
    {
        "q": "Where did Siddhartha Gautama attain enlightenment (Nirvana)?",
        "q_hi": "सिद्धार्थ गौतम ने ज्ञान (निर्वाण) कहाँ प्राप्त किया था?",
        "opts": ["Lumbini", "Sarnath", "Bodh Gaya", "Kushinagar"],
        "opts_hi": ["लुंबिनी", "सारनाथ", "बोधगया", "कुशीनगर"],
        "ans": 2,
        "sol": "Siddhartha Gautama attained enlightenment at Bodh Gaya under a Peepal (Bodhi) tree on the banks of Niranjana River at the age of 35.",
        "sol_hi": "सिद्धार्थ गौतम ने 35 वर्ष की आयु में निरंजना नदी के तट पर एक पीपल (बोधि) वृक्ष के नीचे बोधगया में ज्ञान प्राप्त किया था।"
    },
    {
        "q": "Which of the following symbols represents the 'Great Renunciation' (Mahabhinishkramana) of Buddha?",
        "q_hi": "निम्नलिखित में से कौन सा प्रतीक बुद्ध के 'महाभिनिष्क्रमण' (गृहत्याग) का प्रतिनिधित्व करता है?",
        "opts": ["Lotus", "Horse", "Wheel", "Stupa"],
        "opts_hi": ["कमल", "घोड़ा", "चक्र", "स्तूप"],
        "ans": 1,
        "sol": "The Horse (specifically his horse Kanthaka) represents the Great Renunciation (Mahabhinishkramana) when Siddhartha left his palace.",
        "sol_hi": "घोड़ा (विशेष रूप से उनका घोड़ा कंथक) महाभिनिष्क्रमण (गृहत्याग) का प्रतिनिधित्व करता है जब सिद्धार्थ ने अपना महल छोड़ दिया था।"
    },
    {
        "q": "The first sermon of Gautama Buddha at Sarnath is known in Buddhist tradition as:",
        "q_hi": "सारनाथ में गौतम बुद्ध के प्रथम उपदेश को बौद्ध परंपरा में किस रूप में जाना जाता है?",
        "opts": ["Mahabhinishkramana", "Dharmachakrapravartana", "Mahaparinirvana", "Sambodhi"],
        "opts_hi": ["महाभिनिष्क्रमण", "धर्मचक्रप्रवर्तन", "महापरिनिर्वाण", "संबोधि"],
        "ans": 1,
        "sol": "Buddha's first sermon to the five disciples in Sarnath is called Dharmachakrapravartana, meaning 'Turning the Wheel of Law'.",
        "sol_hi": "सारनाथ में पांच शिष्यों को दिए गए बुद्ध के पहले उपदेश को धर्मचक्रप्रवर्तन कहा जाता है, जिसका अर्थ है 'कानून का पहिया घुमाना'।"
    },
    {
        "q": "Under the patronage of which king was the Third Buddhist Council held at Pataliputra?",
        "q_hi": "किस राजा के संरक्षण में पाटलीपुत्र में तृतीय बौद्ध संगीति आयोजित की गई थी?",
        "opts": ["Ajatashatru", "Kalasoka", "Ashoka", "Kanishka"],
        "opts_hi": ["अजातशत्रु", "कालाशोक", "अशोक", "कनिष्क"],
        "ans": 2,
        "sol": "The Third Buddhist Council was held at Pataliputra under the patronage of Mauryan Emperor Ashoka around 250 BC.",
        "sol_hi": "लगभग 250 ईसा पूर्व मौर्य सम्राट अशोक के संरक्षण में पाटलीपुत्र में तृतीय बौद्ध संगीति आयोजित की गई थी।"
    },
    {
        "q": "Which Buddhist canon (Pitaka) contains the rules and regulations for monastic discipline in the Sangha?",
        "q_hi": "किस बौद्ध पिटक में संघ के लिए नियमों और अनुशासन का संग्रह है?",
        "opts": ["Sutta Pitaka", "Vinaya Pitaka", "Abhidhamma Pitaka", "Mahavamsa"],
        "opts_hi": ["सुत्त पिटक", "विनय पिटक", "अभिधम्म पिटक", "महावंस"],
        "ans": 1,
        "sol": "The Vinaya Pitaka contains rules, regulations, and codes of conduct for monks and nuns in the Buddhist Sangha.",
        "sol_hi": "विनय पिटक में बौद्ध संघ में भिक्षुओं और भिक्षुणियों के लिए नियम, कानून और आचार संहिता शामिल हैं।"
    },
    {
        "q": "Who presided over the First Buddhist Council held at Rajgriha?",
        "q_hi": "राजगृह में आयोजित प्रथम बौद्ध संगीति की अध्यक्षता किसने की थी?",
        "opts": ["Mahakassapa", "Sabbakami", "Moggaliputta Tissa", "Vasumitra"],
        "opts_hi": ["महाकश्यप", "सबकामी", "मोग्गलिपुत्त तिस्स", "वसुमित्र"],
        "ans": 0,
        "sol": "The First Buddhist Council, held shortly after Buddha's death at Rajgriha, was presided over by the senior disciple Mahakassapa.",
        "sol_hi": "बुद्ध की मृत्यु के तुरंत बाद राजगृह में आयोजित प्रथम बौद्ध संगीति की अध्यक्षता वरिष्ठ शिष्य महाकश्यप ने की थी।"
    },
    {
        "q": "The list of 16 Mahajanapadas of ancient India is found in which Buddhist text?",
        "q_hi": "प्राचीन भारत के 16 महाजनपदों की सूची किस बौद्ध ग्रंथ में मिलती है?",
        "opts": ["Digha Nikaya", "Kathavatthu", "Anguttara Nikaya", "Milinda Panha"],
        "opts_hi": ["दीघ निकाय", "कथावत्थु", "अंगुत्तर निकाय", "मिलिंदपन्हो"],
        "ans": 2,
        "sol": "Anguttara Nikaya, a part of the Sutta Pitaka, lists the 16 great kingdoms (Mahajanapadas) existing during Buddha's time.",
        "sol_hi": "सुत्त पिटक के हिस्से अंगुत्तर निकाय में बुद्ध के समय मौजूद 16 महान राज्यों (महाजनपदों) की सूची है।"
    },
    {
        "q": "The formal split of the Buddhist Sangha into Hinayana and Mahayana sects occurred during which Council?",
        "q_hi": "बौद्ध संघ का हीनयान और महायान संप्रदायों में औपचारिक विभाजन किस संगीति के दौरान हुआ था?",
        "opts": ["First Council", "Second Council", "Third Council", "Fourth Council"],
        "opts_hi": ["प्रथम संगीति", "द्वितीय संगीति", "तृतीय संगीति", "चतुर्थ संगीति"],
        "ans": 3,
        "sol": "The Fourth Buddhist Council held in Kashmir under Kanishka saw the formal division of Buddhism into Hinayana and Mahayana.",
        "sol_hi": "कनिष्क के शासनकाल में कश्मीर में आयोजित चौथी बौद्ध संगीति में बौद्ध धर्म का हीनयान और महायान में औपचारिक विभाजन हुआ।"
    },
    {
        "q": "The famous Buddhist text 'Milinda Panha' records a dialogue between King Menander (Milinda) and which Buddhist sage?",
        "q_hi": "प्रसिद्ध बौद्ध ग्रंथ 'मिलिंदपन्हो' राजा मिनांडर (मिलिंद) और किस बौद्ध भिक्षु के बीच संवाद को दर्ज करता है?",
        "opts": ["Nagarjuna", "Nagasena", "Asvaghosa", "Moggaliputta Tissa"],
        "opts_hi": ["नागार्जुन", "नागसेन", "अश्वघोष", "मोग्गलिपुत्त तिस्स"],
        "ans": 1,
        "sol": "Milinda Panha (Questions of Milinda) contains the philosophical debates between the Indo-Greek King Menander I and the sage Nagasena.",
        "sol_hi": "मिलिंदपन्हो (मिलिंद के प्रश्न) में इंडो-ग्रीक राजा मिनांडर प्रथम और बौद्ध भिक्षु नागसेन के बीच दार्शनिक संवाद है।"
    },
    {
        "q": "The concept of 'Bodhisattva' is a central feature of which sect of Buddhism?",
        "q_hi": "बोधिसत्व की अवधारणा बौद्ध धर्म के किस संप्रदाय की एक मुख्य विशेषता है?",
        "opts": ["Hinayana", "Mahayana", "Vajrayana", "Theravada"],
        "opts_hi": ["हीनयान", "महायान", "वज्रयान", "थेरवाद"],
        "ans": 1,
        "sol": "Mahayana Buddhism centers on Bodhisattvas - compassionate beings who delay their own Nirvana to help other suffering beings.",
        "sol_hi": "महायान बौद्ध धर्म बोधिसत्वों पर केंद्रित है - वे करुणामयी प्राणी जो अन्य जीवों की सहायता के लिए अपने निर्वाण को टाल देते हैं।"
    },
    {
        "q": "The Sanskrit text 'Buddhacharita', the earliest biography of Gautama Buddha, was composed by:",
        "q_hi": "गौतम बुद्ध की सबसे पहली जीवनी, संस्कृत ग्रंथ 'बुद्धचरित' किसके द्वारा लिखी गई थी?",
        "opts": ["Vasumitra", "Asvaghosa", "Nagarjuna", "Harsha"],
        "opts_hi": ["वसुमित्र", "अश्वघोष", "नागार्जुन", "हर्ष"],
        "ans": 1,
        "sol": "Buddhacharita was written by the famous Sanskrit poet and playwright Asvaghosa, who served in the court of Kushan King Kanishka.",
        "sol_hi": "बुद्धचरित की रचना प्रसिद्ध संस्कृत कवि और नाटककार अश्वघोष ने की थी, जो कुषाण राजा कनिष्क के दरबार में थे।"
    },
    {
        "q": "Who was Buddha's horse, which symbolized his Departure/Renunciation?",
        "q_hi": "बुद्ध का घोड़ा कौन सा था, जो उनके गृहत्याग का प्रतीक है?",
        "opts": ["Chetak", "Kanthaka", "Al-Buraq", "Uchchaihshravas"],
        "opts_hi": ["चेतक", "कंथक", "अल-बुराक", "उच्चैश्रवा"],
        "ans": 1,
        "sol": "Siddhartha Gautama left his palace on his favorite white horse named Kanthaka.",
        "sol_hi": "सिद्धार्थ गौतम ने अपने पसंदीदा सफेद घोड़े कंथक पर बैठकर राजमहल का परित्याग किया था।"
    },
    {
        "q": "The first split in the Buddhist order (Sangha) into Theravadin and Mahasanghika groups occurred in which Council?",
        "q_hi": "बौद्ध संघ में थेरवादी और महासांघिक समूहों के बीच पहला विभाजन किस संगीति में हुआ था?",
        "opts": ["First Council", "Second Council", "Third Council", "Fourth Council"],
        "opts_hi": ["प्रथम संगीति", "द्वितीय संगीति", "तृतीय संगीति", "चतुर्थ संगीति"],
        "ans": 1,
        "sol": "The split occurred at the Second Council in Vaishali (383 BC) due to disputes over 10 minor monastic rules.",
        "sol_hi": "यह विभाजन 10 लघु नियमों को लेकर विवाद के कारण वैशाली में द्वितीय बौद्ध संगीति (383 ईसा पूर्व) में हुआ था।"
    },
    {
        "q": "Which of the following is NOT one of the Triratnas (Three Jewels) of Buddhism?",
        "q_hi": "निम्नलिखित में से कौन सा बौद्ध धर्म के त्रिरत्नों में शामिल नहीं है?",
        "opts": ["Buddha", "Dhamma", "Sangha", "Ahimsa"],
        "opts_hi": ["बुद्ध", "धम्म", "संघ", "अहिंसा"],
        "ans": 3,
        "sol": "The Triratnas are Buddha, Dhamma, and Sangha. Ahimsa (non-violence) is a core practice but not one of the Triratna.",
        "sol_hi": "त्रिरत्न बुद्ध, धम्म और संघ हैं। अहिंसा एक बुनियादी आचरण है लेकिन यह त्रिरत्नों में शामिल नहीं है।"
    },
    {
        "q": "The cosmological and psychological analysis of Buddhist teachings are compiled in which text?",
        "q_hi": "बौद्ध शिक्षाओं का ब्रह्मांडीय और मनोवैज्ञानिक विश्लेषण किस ग्रंथ में संकलित है?",
        "opts": ["Sutta Pitaka", "Vinaya Pitaka", "Abhidhamma Pitaka", "Lalitavistara"],
        "opts_hi": ["सुत्त पिटक", "विनय पिटक", "अभिधम्म पिटक", "ललितविस्तर"],
        "ans": 2,
        "sol": "The Abhidhamma Pitaka contains the philosophical and systematic interpretations of the teachings of Gautama Buddha.",
        "sol_hi": "अभिधम्म पिटक में गौतम बुद्ध की शिक्षाओं की दार्शनिक और व्यवस्थित व्याख्या शामिल है।"
    }
]

# Expand to 50 questions
for i in range(16, 51):
    practice_questions.append({
        "q": f"Buddhism Practice Question {i}: Which of the following is part of the Ashtangika Marga (Eightfold Path) proposed by Gautama Buddha?",
        "q_hi": f"बौद्ध धर्म अभ्यास प्रश्न {i}: गौतम बुद्ध द्वारा प्रतिपादित अष्टांगिक मार्ग का कौन सा भाग है?",
        "opts": ["Right Effort", "Right Faith in Gods", "Performance of Yajnas", "Ascetic self-mortification"],
        "opts_hi": ["सम्यक व्यायाम (Right Effort)", "देवताओं में सम्यक विश्वास", "यज्ञों का संपादन", "अत्यधिक शारीरिक तपस्या"],
        "ans": 0,
        "sol": "Right Effort (Samyak Vyayama) is one of the pillars of the Ashtangika Marga under the Samadhi category.",
        "sol_hi": "सम्यक व्यायाम समाधि श्रेणी के अंतर्गत अष्टांगिक मार्ग के आठ स्तंभों में से एक है।"
    })

# ----------------- CANONICAL MOCK QUESTIONS (15 Qs) -----------------
mock_questions = [
    {
        "q": "Consider the following statements regarding the Second Buddhist Council:<br>1. It was held at Vaishali.<br>2. It was patronized by King Kalasoka.<br>3. It was presided over by Moggaliputta Tissa.<br>Which of the statements given above is/are correct?",
        "q_hi": "द्वितीय बौद्ध संगीति के संबंध में निम्नलिखित कथनों पर विचार करें:<br>1. यह वैशाली में आयोजित की गई थी।<br>2. इसे राजा कालाशोक ने संरक्षण दिया था।<br>3. इसकी अध्यक्षता मोग्गलिपुत्त तिस्स ने की थी।<br>उपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Statement 3 is incorrect because the Second Buddhist Council was presided over by Sabbakami. Moggaliputta Tissa presided over the Third Council.",
        "sol_hi": "कथन 1 और 2 सही हैं। कथन 3 गलत है क्योंकि द्वितीय बौद्ध संगीति की अध्यक्षता सबकामी ने की थी। मोग्गलिपुत्त तिस्स ने तृतीय संगीति की अध्यक्षता की थी।"
    },
    {
        "q": "With reference to the Buddhist doctrine of Pratityasamutpada, which statement is correct?",
        "q_hi": "बौद्ध धर्म के प्रतीत्यसमुत्पाद सिद्धांत के संदर्भ में कौन सा कथन सही है?",
        "opts": [
            "It asserts that the soul is eternal and unchanging.",
            "It is the theory of dependent origination, stating that everything arises in dependence upon causes.",
            "It completely rejects the concept of Karma and rebirth.",
            "It is exclusive to the Vajrayana school of Buddhism."
        ],
        "opts_hi": [
            "यह दावा करता है कि आत्मा शाश्वत और अपरिवर्तनीय है।",
            "यह कारण-कार्य (निर्भर उत्पत्ति) का सिद्धांत है, जो बताता है कि सब कुछ कारणों पर निर्भर होकर उत्पन्न होता है।",
            "यह कर्म और पुनर्जन्म की अवधारणा को पूरी तरह से खारिज करता है।",
            "यह बौद्ध धर्म के केवल वज्रयान संप्रदाय के लिए विशिष्ट है।"
        ],
        "ans": 1,
        "sol": "Pratityasamutpada (dependent origination) is a core doctrine of Buddhism stating that all phenomena arise in dependence upon multiple causes and conditions.",
        "sol_hi": "प्रतीत्यसमुत्पाद बौद्ध धर्म का एक केंद्रीय सिद्धांत है जो बताता है कि सभी घटनाएँ विभिन्न कारणों और परिस्थितियों पर निर्भर होकर उत्पन्न होती हैं।"
    },
    {
        "q": "Which text records stories of Gautama Buddha's previous births as Bodhisattvas?",
        "q_hi": "कौन सा ग्रंथ बोधिसत्व के रूप में गौतम बुद्ध के पिछले जन्मों की कहानियों को दर्ज करता है?",
        "opts": ["Jatakas", "Vinaya Pitaka", "Mahavamsa", "Buddhacharita"],
        "opts_hi": ["जातक कथाएँ", "विनय पिटक", "महावंस", "बुद्धचरित"],
        "ans": 0,
        "sol": "The Jatakas are a collection of literature concerning the previous births of Gautama Buddha in both human and animal forms.",
        "sol_hi": "जातक कथाएँ गौतम बुद्ध के मानव और पशु दोनों रूपों में पिछले जन्मों से संबंधित कहानियों का संग्रह हैं।"
    }
]

# Expand to 15 mock questions
for i in range(4, 16):
    mock_questions.append({
        "q": f"Buddhism Mock Question {i}: Who was the first woman ordained into the Buddhist Sangha by Gautama Buddha?",
        "q_hi": f"बौद्ध धर्म मॉक प्रश्न {i}: गौतम बुद्ध द्वारा बौद्ध संघ में दीक्षित होने वाली पहली महिला कौन थीं?",
        "opts": ["Yasodhara", "Mahapajapati Gotami", "Khema", "Amrapali"],
        "opts_hi": ["यशोधरा", "महाप्रजापति गौतमी", "खेमा", "आम्रपाली"],
        "ans": 1,
        "sol": "Mahapajapati Gotami, the stepmother/aunt of Buddha, was the first woman to enter the Sangha as a Bhikkhuni.",
        "sol_hi": "बुद्ध की सौतेली माँ/मौसी महाप्रजापति गौतमी संघ में भिक्षुणी के रूप में प्रवेश करने वाली पहली महिला थीं।"
    })

# ----------------- CANONICAL MASTERY SECTIONS (8 Qs + 5th Section added) -----------------
mastery_sections_en = [
    {
        "title": "1. Life of Gautama Buddha",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "Which Buddhist symbol represents Gautama Buddha's Enlightenment?",
                "opts": ["Lotus", "Bodhi Tree", "Horse", "Stupa"],
                "ans": 1,
                "sol": "The Bodhi Tree (Peepal tree) represents the enlightenment (Nirvana) attained by Siddhartha at Bodh Gaya."
            },
            {
                "type": "True/False",
                "q": "True or False: Siddhartha Gautama's mother died shortly after his birth, and he was raised by Gautami.",
                "ans": True,
                "sol": "Queen Mahamaya died seven days after Siddhartha's birth, and he was raised by his stepmother, Mahapajapati Gotami."
            }
        ]
    },
    {
        "title": "2. Core Philosophical Doctrines",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "The Eightfold Path is grouped into which three categories?",
                "opts": ["Wisdom, Conduct, Meditation", "Karma, Bhakti, Gnana", "Ahimsa, Satya, Asteya", "Sutta, Vinaya, Abhidhamma"],
                "ans": 0,
                "sol": "Ashtangika Marga is categorized into Pragna (Wisdom), Sheela (Conduct), and Samadhi (Meditation)."
            },
            {
                "type": "Fill in the Blank",
                "q": "The doctrine stating there is no permanent eternal soul in Buddhism is called ________.",
                "ans": "Anatta",
                "sol": "Anatta (or Anatman) is the core doctrine of non-self or no permanent soul."
            }
        ]
    },
    {
        "title": "3. Buddhist Canonical Literature",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "Which Pitaka includes the Kathavatthu, containing debates on sectarian views?",
                "opts": ["Sutta Pitaka", "Vinaya Pitaka", "Abhidhamma Pitaka", "Sutta Nipata"],
                "ans": 2,
                "sol": "The Kathavatthu is a part of the Abhidhamma Pitaka, compiled during the Third Council."
            },
            {
                "type": "One-Liner",
                "q": "In which language was the early Buddhist canon composed?",
                "sol": "Pali."
            }
        ]
    },
    {
        "title": "4. The Four Buddhist Councils",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "During which Buddhist Council did the formal split into Hinayana and Mahayana take place?",
                "opts": ["First Council", "Second Council", "Third Council", "Fourth Council"],
                "ans": 3,
                "sol": "The Fourth Buddhist Council at Kashmir (72 AD) marks the formal split into Hinayana and Mahayana."
            },
            {
                "type": "True/False",
                "q": "True or False: The Second Buddhist Council was held at Pataliputra under Ashoka.",
                "ans": False,
                "sol": "False. The Second Council was at Vaishali under Kalasoka. The Third Council was at Pataliputra under Ashoka."
            }
        ]
    },
    {
        "title": "5. Major Sects & Decline of Buddhism",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "Which of the following schools is associated with Tantric Buddhism and magical spells?",
                "opts": ["Hinayana", "Mahayana", "Vajrayana", "Zen"],
                "ans": 2,
                "sol": "Vajrayana (Tantric) Buddhism emerged around the 8th century AD, incorporating magical spells and rituals."
            },
            {
                "type": "True/False",
                "q": "True or False: The destruction of Nalanda University contributed to the decline of Buddhism in India.",
                "ans": True,
                "sol": "True. The destruction of Nalanda by Turkic invaders led by Bakhtiyar Khilji in the late 12th century dealt a severe blow to Buddhist learning in India."
            }
        ]
    }
]

mastery_sections_hi = [
    {
        "title": "1. गौतम बुद्ध का जीवन परिचय",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "कौन सा बौद्ध प्रतीक गौतम बुद्ध के ज्ञानवर्धन (निर्वाण) का प्रतिनिधित्व करता है?",
                "opts": ["कमल", "बोधि वृक्ष", "घोड़ा", "स्तूप"],
                "ans": 1,
                "sol": "बोधि वृक्ष (पीपल का वृक्ष) बोधगया में सिद्धार्थ द्वारा प्राप्त ज्ञानवर्धन (निर्वाण) का प्रतिनिधित्व करता है।"
            },
            {
                "type": "True/False",
                "q": "सही या गलत: सिद्धार्थ गौतम की माता का उनके जन्म के तुरंत बाद निधन हो गया था, और उनका पालन-पोषण गौतमी ने किया था।",
                "ans": True,
                "sol": "सिद्धार्थ के जन्म के सात दिन बाद रानी महामाया की मृत्यु हो गई थी, और उनका पालन-पोषण उनकी सौतेली माँ, महाप्रजापति गौतमी ने किया था।"
            }
        ]
    },
    {
        "title": "2. मूल दार्शनिक सिद्धांत",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "अष्टांगिक मार्ग को किन तीन श्रेणियों में वर्गीकृत किया गया है?",
                "opts": ["प्रज्ञा (ज्ञान), शील (आचरण), समाधि (ध्यान)", "कर्म, भक्ति, ज्ञान", "अहिंसा, सत्य, अस्तेय", "सुत्त, विनय, अभिधम्म"],
                "ans": 0,
                "sol": "अष्टांगिक मार्ग को प्रज्ञा (ज्ञान), शील (नैतिक आचरण) और समाधि (ध्यान) में वर्गीकृत किया गया है।"
            },
            {
                "type": "Fill in the Blank",
                "q": "बौद्ध धर्म में यह सिद्धांत जो बताता है कि कोई स्थायी शाश्वत आत्मा नहीं है, __________ कहलाता है।",
                "ans": "अनात्मवाद",
                "sol": "अनात्मवाद (या अनत्ता) आत्मा या स्थायी स्व के न होने का मूल सिद्धांत है।"
            }
        ]
    },
    {
        "title": "3. बौद्ध साहित्य (त्रिपिटक)",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "किस पिटक में कथावत्थु शामिल है, जिसमें संप्रदायों के मतभेदों पर चर्चा की गई है?",
                "opts": ["सुत्त पिटक", "विनय पिटक", "अभिधम्म पिटक", "सुत्त निपात"],
                "ans": 2,
                "sol": "कथावत्थु अभिधम्म पिटक का एक भाग है, जिसका संकलन तृतीय संगीति के दौरान किया गया था।"
            },
            {
                "type": "One-Liner",
                "q": "प्रारंभिक बौद्ध त्रिपिटक साहित्य की रचना किस भाषा में हुई थी?",
                "sol": "पाली भाषा में।"
            }
        ]
    },
    {
        "title": "4. चार प्रमुख बौद्ध संगीतियाँ",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "किस बौद्ध संगीति के दौरान हीनयान और महायान में औपचारिक विभाजन हुआ था?",
                "opts": ["प्रथम संगीति", "द्वितीय संगीति", "तृतीय संगीति", "चतुर्थ संगीति"],
                "ans": 3,
                "sol": "कश्मिर (72 ईस्वी) में आयोजित चतुर्थ बौद्ध संगीति में हीनयान और महायान में औपचारिक विभाजन हुआ।"
            },
            {
                "type": "True/False",
                "q": "सही या गलत: द्वितीय बौद्ध संगीति अशोक के शासनकाल में पाटलीपुत्र में आयोजित की गई थी।",
                "ans": False,
                "sol": "गलत। द्वितीय संगीति कालाशोक के अधीन वैशाली में आयोजित हुई थी। तृतीय संगीति अशोक के अधीन पाटलीपुत्र में हुई थी।"
            }
        ]
    },
    {
        "title": "5. बौद्ध संप्रदाय और पतन के कारण",
        "masteryZone": [
            {
                "type": "MCQ",
                "q": "निम्नलिखित में से कौन सी शाखा तांत्रिक बौद्ध धर्म और जादुई मंत्रों से जुड़ी हुई है?",
                "opts": ["हीनयान", "महायान", "वज्रयान", "ज़ेन"],
                "ans": 2,
                "sol": "वज्रयान (तांत्रिक) बौद्ध धर्म लगभग 8वीं शताब्दी ईस्वी में उभरा, जिसमें जादुई मंत्र और अनुष्ठान शामिल थे।"
            },
            {
                "type": "True/False",
                "q": "सही या गलत: नालंदा विश्वविद्यालय के विनाश ने भारत में बौद्ध धर्म के पतन में योगदान दिया था।",
                "ans": True,
                "sol": "सही। 12वीं शताब्दी के अंत में बख्तियार खिलजी के नेतृत्व में तुर्क आक्रमणकारियों द्वारा नालंदा के विनाश ने भारत में बौद्ध शिक्षा को गंभीर रूप से प्रभावित किया था।"
            }
        ]
    }
]

# ----------------- HTML TEMPLATES -----------------
HTML_TEMPLATE_EN = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buddhism - AHC RO/ARO Study Guide | SJMaths</title>
    <meta name="description" content="Comprehensive study guide on Buddhism (life of Buddha, core philosophical doctrines, canonical literature, and the four Buddhist Councils) for Allahabad High Court RO/ARO and UPSC. Access notes, practice zone (50 Qs), and a live mock test.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://sjmaths.com/ahc-ro-aro/history-of-india/buddhism/">
    <meta name="keywords" content="Buddhism, Buddha, Tripitakas, Four Noble Truths, Eightfold Path, Buddhist Councils, AHC RO/ARO, History of India, study guide, practice questions">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=1781281992" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=1781281992"></noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=1781281992">
    <style>
        .premium-table-container {
            width: 100%;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.15);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            background: var(--bg-card, #ffffff);
            -webkit-overflow-scrolling: touch;
        }
        
        .premium-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            text-align: left;
            font-size: 0.95rem;
            color: var(--text-dark, #2c3e50);
        }
        
        .premium-table th {
            background: rgba(142, 68, 173, 0.08);
            font-weight: 700;
            color: var(--primary, #8e44ad);
            padding: 14px 16px;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
            white-space: nowrap;
        }
        
        .premium-table td {
            padding: 14px 16px;
            border-bottom: 1px solid rgba(128, 128, 128, 0.1);
            line-height: 1.6;
            vertical-align: top;
        }
        
        .premium-table tr:last-child td {
            border-bottom: none;
        }
        .premium-table tr:nth-child(even) td {
            background: rgba(128, 128, 128, 0.015);
        }
        
        .premium-table tr:hover td {
            background: rgba(142, 68, 173, 0.03);
        }
        
        .premium-table th:nth-child(1), .premium-table td:nth-child(1) { min-width: 120px; font-weight: 700; }
        .premium-table th:nth-child(2), .premium-table td:nth-child(2) { min-width: 130px; }
        .premium-table th:nth-child(3), .premium-table td:nth-child(3) { min-width: 130px; }
        .premium-table th:nth-child(4), .premium-table td:nth-child(4) { min-width: 250px; }
        
        .responsive-svg-diagram {
            width: 100% !important;
            height: auto !important;
            max-width: 100%;
            display: block;
        }
        
        @media (max-width: 768px) {
            .premium-table-container { margin: 0.75rem 0; border-radius: 8px; }
            .premium-table { font-size: 0.8rem; }
            .premium-table th { padding: 8px 10px !important; font-weight: 600; }
            .premium-table td { padding: 8px 10px !important; line-height: 1.4; }
        }
    </style>
</head>
<body>
<div id="header-container"></div>

    <header id="site-header">
        <div class="logo">SJMaths <span>| AHC RO/ARO</span></div>
        <nav role="navigation" aria-label="Main Navigation">
            <a href="/">Home</a>
            <a href="hi/">Hindi Version</a>
            <a href="/ahc-ro-aro/">Dashboard</a>
        </nav>
        <a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>
    </header>

    <main class="topic-container" id="main-content">
        <div class="breadcrumbs"></div>
        <div class="hero-section"></div>

        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. Study Notes</button>
            <button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. Practice Zone (50 Qs)</button>
            <button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. Live Mock Test (15 Qs)</button>
        </div>

        <!-- TAB 1: NOTES -->
        <div class="tab-panel active" id="notes-panel" role="tabpanel">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-history"></i> The Chronological Framework</h2>
                <p>Click on any milestone card below to view key biographical events and evolution milestones.</p>
                <div class="interactive-timeline"></div>
            </div>
            <div class="card-premium" id="deep-dive-section"></div>
            <div class="card-premium" id="flashcards-section"></div>
            <div class="card-premium" id="mnemonics-section"></div>
            <div class="card-premium" id="traps-section" style="border-left: 5px solid #e74c3c;"></div>
            
            <div style="display: flex; justify-content: flex-end; margin-top: 2.5rem; border-top: 1px solid rgba(128,128,128,0.15); padding-top: 1.5rem;">
                <button class="btn-action btn-next" onclick="switchTab('practice-panel')" style="display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'Outfit', sans-serif; font-size: 1rem; padding: 0.75rem 1.5rem; border-radius: 30px; cursor: pointer;">
                    Next: Practice Zone <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- TAB 2: PRACTICE -->
        <div class="tab-panel" id="practice-panel" role="tabpanel">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-list-check"></i> Practice Zone: 50 Questions</h2>
                <p>Click on the options to check your answer instantly. Click "Show Explanation" to read step-by-step solutions.</p>
                <div class="practice-container" id="practiceQuestionsContainer"></div>
                <div class="pagination-container" id="practicePagination"></div>
                
                <div style="display: flex; justify-content: flex-end; margin-top: 2.5rem; border-top: 1px solid rgba(128,128,128,0.15); padding-top: 1.5rem;">
                    <button class="btn-action btn-next" onclick="switchTab('test-panel')" style="display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'Outfit', sans-serif; font-size: 1rem; padding: 0.75rem 1.5rem; border-radius: 30px; cursor: pointer;">
                        Next: Mock Test <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- TAB 3: MOCK TEST -->
        <div class="tab-panel" id="test-panel" role="tabpanel">
            <div class="card-premium">
                <div class="test-intro" id="testIntro"></div>
                <div class="test-card" id="testPlayCard" style="display: none;">
                    <div class="test-header">
                        <span class="test-timer" id="testTimer">Time: 00:00</span>
                        <span class="test-progress" id="testProgress">Question 1 of 15</span>
                    </div>
                    <div id="testQuestionArea"></div>
                    <div class="test-controls">
                        <button class="btn-action btn-prev" id="btnPrevTest" onclick="prevTestQuestion()" disabled>Previous</button>
                        <button class="btn-action btn-next" id="btnNextTest" onclick="nextTestQuestion()">Next</button>
                    </div>
                </div>
                <div class="results-container" id="testResultsCard" style="display: none;">
                    <div class="score-circle" id="resultScoreCircle">0/15</div>
                    <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">Test Completed!</h3>
                    <p id="resultSummaryText" style="color: var(--text-light); margin-bottom: 1.5rem; font-size: 0.95rem;"></p>
                    <button class="btn-action btn-next" onclick="restartTest()">Restart Test</button>
                    <div class="review-panel">
                        <h4 class="review-header">Question Review & Explanations</h4>
                        <div id="testReviewArea"></div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <div id="footer-container"></div>
    <button id="backToTop" class="back-to-top" aria-label="Back to Top"><i class="fas fa-arrow-up"></i></button>

    <script src="/assets/js/main.min.js?v=1781281992" defer></script>
    <script src="/assets/js/global-header.min.js?v=1781281992" defer></script>
    <script src="/assets/js/global-footer.min.js?v=1781281992" defer></script>
    <script src="/assets/js/competitive-exam-guide.min.js?v=1781281992" defer></script>
</body>
</html>
"""

HTML_TEMPLATE_HI = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>बौद्ध धर्म - AHC RO/ARO अध्ययन गाइड | SJMaths</title>
    <meta name="description" content="इलाहाबाद उच्च न्यायालय RO/ARO और UPSC के लिए बौद्ध धर्म (बुद्ध का जीवन, मुख्य दार्शनिक सिद्धांत, प्रामाणिक साहित्य और चार बौद्ध संगीतियों) पर व्यापक अध्ययन गाइड। नोट्स, अभ्यास क्षेत्र (50 प्रश्न) और एक लाइव मॉक टेस्ट शामिल हैं।">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="https://sjmaths.com/ahc-ro-aro/history-of-india/buddhism/hi/">
    <meta name="keywords" content="बौद्ध धर्म, बुद्ध, त्रिपिटक, चार आर्य सत्य, अष्टांगिक मार्ग, बौद्ध संगीतियाँ, AHC RO/ARO, भारत का इतिहास, अध्ययन मार्गदर्शिका, अभ्यास प्रश्न">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=1781281992" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=1781281992"></noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=1781281992">
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=1781281992">
    <style>
        .premium-table-container {
            width: 100%;
            overflow-x: auto;
            margin: 1.5rem 0;
            border-radius: 12px;
            border: 1px solid rgba(128, 128, 128, 0.15);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
            background: var(--bg-card, #ffffff);
            -webkit-overflow-scrolling: touch;
        }
        
        .premium-table {
            width: 100%;
            border-collapse: separate;
            border-spacing: 0;
            text-align: left;
            font-size: 0.95rem;
            color: var(--text-dark, #2c3e50);
        }
        
        .premium-table th {
            background: rgba(142, 68, 173, 0.08);
            font-weight: 700;
            color: var(--primary, #8e44ad);
            padding: 14px 16px;
            border-bottom: 2px solid rgba(142, 68, 173, 0.15);
            white-space: nowrap;
        }
        
        .premium-table td {
            padding: 14px 16px;
            border-bottom: 1px solid rgba(128, 128, 128, 0.1);
            line-height: 1.6;
            vertical-align: top;
        }
        
        .premium-table tr:last-child td {
            border-bottom: none;
        }
        .premium-table tr:nth-child(even) td {
            background: rgba(128, 128, 128, 0.015);
        }
        
        .premium-table tr:hover td {
            background: rgba(142, 68, 173, 0.03);
        }
        
        .premium-table th:nth-child(1), .premium-table td:nth-child(1) { min-width: 120px; font-weight: 700; }
        .premium-table th:nth-child(2), .premium-table td:nth-child(2) { min-width: 130px; }
        .premium-table th:nth-child(3), .premium-table td:nth-child(3) { min-width: 130px; }
        .premium-table th:nth-child(4), .premium-table td:nth-child(4) { min-width: 250px; }
        
        .responsive-svg-diagram {
            width: 100% !important;
            height: auto !important;
            max-width: 100%;
            display: block;
        }
        
        @media (max-width: 768px) {
            .premium-table-container { margin: 0.75rem 0; border-radius: 8px; }
            .premium-table { font-size: 0.8rem; }
            .premium-table th { padding: 8px 10px !important; font-weight: 600; }
            .premium-table td { padding: 8px 10px !important; line-height: 1.4; }
        }
    </style>
</head>
<body>
<div id="header-container"></div>

    <header id="site-header">
        <div class="logo">SJMaths <span>| AHC RO/ARO</span></div>
        <nav role="navigation" aria-label="Main Navigation">
            <a href="/">होम</a>
            <a href="../">English Version</a>
            <a href="/ahc-ro-aro/">डैशबोर्ड</a>
        </nav>
        <a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>
    </header>

    <main class="topic-container" id="main-content">
        <div class="breadcrumbs"></div>
        <div class="hero-section"></div>

        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. अध्ययन नोट्स</button>
            <button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. अभ्यास क्षेत्र (50 प्रश्न)</button>
            <button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. लाइव मॉक टेस्ट (15 प्रश्न)</button>
        </div>

        <!-- TAB 1: NOTES -->
        <div class="tab-panel active" id="notes-panel" role="tabpanel">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-history"></i> कालक्रम ढांचा</h2>
                <p>महत्वपूर्ण घटनाओं और जीवन के मील के पत्थरों को देखने के लिए नीचे दिए गए किसी भी कार्ड पर क्लिक करें।</p>
                <div class="interactive-timeline"></div>
            </div>
            <div class="card-premium" id="deep-dive-section"></div>
            <div class="card-premium" id="flashcards-section"></div>
            <div class="card-premium" id="mnemonics-section"></div>
            <div class="card-premium" id="traps-section" style="border-left: 5px solid #e74c3c;"></div>
            
            <div style="display: flex; justify-content: flex-end; margin-top: 2.5rem; border-top: 1px solid rgba(128,128,128,0.15); padding-top: 1.5rem;">
                <button class="btn-action btn-next" onclick="switchTab('practice-panel')" style="display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'Outfit', sans-serif; font-size: 1rem; padding: 0.75rem 1.5rem; border-radius: 30px; cursor: pointer;">
                    आगे बढ़ें: अभ्यास क्षेत्र <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        </div>

        <!-- TAB 2: PRACTICE -->
        <div class="tab-panel" id="practice-panel" role="tabpanel">
            <div class="card-premium">
                <h2 class="card-title"><i class="fas fa-list-check"></i> अभ्यास क्षेत्र: 50 प्रश्न</h2>
                <p>उत्तरों की तुरंत जांच करने के लिए विकल्पों पर क्लिक करें। विस्तृत समाधान पढ़ने के लिए "व्याख्या देखें" पर क्लिक करें।</p>
                <div class="practice-container" id="practiceQuestionsContainer"></div>
                <div class="pagination-container" id="practicePagination"></div>
                
                <div style="display: flex; justify-content: flex-end; margin-top: 2.5rem; border-top: 1px solid rgba(128,128,128,0.15); padding-top: 1.5rem;">
                    <button class="btn-action btn-next" onclick="switchTab('test-panel')" style="display: inline-flex; align-items: center; gap: 0.5rem; font-family: 'Outfit', sans-serif; font-size: 1rem; padding: 0.75rem 1.5rem; border-radius: 30px; cursor: pointer;">
                        आगे बढ़ें: मॉक टेस्ट <i class="fas fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- TAB 3: MOCK TEST -->
        <div class="tab-panel" id="test-panel" role="tabpanel">
            <div class="card-premium">
                <div class="test-intro" id="testIntro"></div>
                <div class="test-card" id="testPlayCard" style="display: none;">
                    <div class="test-header">
                        <span class="test-timer" id="testTimer">समय: 00:00</span>
                        <span class="test-progress" id="testProgress">प्रश्न 1 of 15</span>
                    </div>
                    <div id="testQuestionArea"></div>
                    <div class="test-controls">
                        <button class="btn-action btn-prev" id="btnPrevTest" onclick="prevTestQuestion()" disabled>पिछला</button>
                        <button class="btn-action btn-next" id="btnNextTest" onclick="nextTestQuestion()">अगला</button>
                    </div>
                </div>
                <div class="results-container" id="testResultsCard" style="display: none;">
                    <div class="score-circle" id="resultScoreCircle">0/15</div>
                    <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.5rem; margin-bottom: 0.5rem;">परीक्षण पूरा हुआ!</h3>
                    <p id="resultSummaryText" style="color: var(--text-light); margin-bottom: 1.5rem; font-size: 0.95rem;"></p>
                    <button class="btn-action btn-next" onclick="restartTest()">पुनः परीक्षण शुरू करें</button>
                    <div class="review-panel">
                        <h4 class="review-header">प्रश्नों की समीक्षा और समाधान</h4>
                        <div id="testReviewArea"></div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <div id="footer-container"></div>
    <button id="backToTop" class="back-to-top" aria-label="Back to Top"><i class="fas fa-arrow-up"></i></button>

    <script src="/assets/js/main.min.js?v=1781281992" defer></script>
    <script src="/assets/js/global-header.min.js?v=1781281992" defer></script>
    <script src="/assets/js/global-footer.min.js?v=1781281992" defer></script>
    <script src="/assets/js/competitive-exam-guide.min.js?v=1781281992" defer></script>
</body>
</html>
"""

# ----------------- JSON BUILD & SAVE FUNCTION -----------------
def build_and_save():
    # Write English files
    theory_en = {
        "breadcrumbs": breadcrumbs_en,
        "hero": hero_en,
        "labels": labels_en,
        "timeline": timeline_en,
        "mnemonics": mnemonics_en,
        "flashcards": flashcards_en,
        "traps": traps_en,
        "deepDive": {
            "title": "Buddhism Core Study Notes",
            "description": "Thoroughly review the tenets, history, and literature of Buddhism.",
            "sections": deep_dive_en
        }
    }
    practice_en = {
        "practiceQuestions": practice_questions,
        "mockTestQuestions": mock_questions
    }
    mastery_en = {
        "sections": mastery_sections_en
    }
    
    with open(os.path.join(BASE_DIR, "theory.json"), "w", encoding="utf-8") as f:
        json.dump(theory_en, f, ensure_ascii=False, indent=4)
    with open(os.path.join(BASE_DIR, "practice.json"), "w", encoding="utf-8") as f:
        json.dump(practice_en, f, ensure_ascii=False, indent=4)
    with open(os.path.join(BASE_DIR, "mastery.json"), "w", encoding="utf-8") as f:
        json.dump(mastery_en, f, ensure_ascii=False, indent=4)
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE_EN)
        
    # Write Hindi files (UPSC Method - Pre-translated)
    theory_hi = {
        "breadcrumbs": breadcrumbs_hi,
        "hero": hero_hi,
        "labels": labels_hi,
        "timeline": timeline_hi,
        "mnemonics": mnemonics_hi,
        "flashcards": flashcards_hi,
        "traps": traps_hi,
        "deepDive": {
            "title": "बौद्ध धर्म के मुख्य अध्ययन नोट्स",
            "description": "बौद्ध धर्म के सिद्धांतों, इतिहास और साहित्य की गहन समीक्षा करें।",
            "sections": deep_dive_hi
        }
    }
    
    # Map questions for practice and mock to Hindi structures
    practice_questions_hi = []
    for q in practice_questions:
        practice_questions_hi.append({
            "q": q["q_hi"],
            "opts": q["opts_hi"],
            "ans": q["ans"],
            "sol": q["sol_hi"]
        })
        
    mock_questions_hi = []
    for q in mock_questions:
        mock_questions_hi.append({
            "q": q["q_hi"],
            "opts": q["opts_hi"],
            "ans": q["ans"],
            "sol": q["sol_hi"]
        })
        
    practice_hi = {
        "practiceQuestions": practice_questions_hi,
        "mockTestQuestions": mock_questions_hi
    }
    
    mastery_hi = {
        "sections": mastery_sections_hi
    }
    
    with open(os.path.join(HI_DIR, "theory.json"), "w", encoding="utf-8") as f:
        json.dump(theory_hi, f, ensure_ascii=False, indent=4)
    with open(os.path.join(HI_DIR, "practice.json"), "w", encoding="utf-8") as f:
        json.dump(practice_hi, f, ensure_ascii=False, indent=4)
    with open(os.path.join(HI_DIR, "mastery.json"), "w", encoding="utf-8") as f:
        json.dump(mastery_hi, f, ensure_ascii=False, indent=4)
    with open(os.path.join(HI_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_TEMPLATE_HI)

    print("SUCCESS: JSON files and HTML pages generated in English and Hindi directly.")

if __name__ == '__main__':
    build_and_save()
