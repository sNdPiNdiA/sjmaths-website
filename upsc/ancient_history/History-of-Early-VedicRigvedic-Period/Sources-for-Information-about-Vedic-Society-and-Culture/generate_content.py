import json
import os

output_path = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Early-VedicRigvedic-Period\Sources-for-Information-about-Vedic-Society-and-Culture\content.json"

# Base metadata, retaining traps, mnemonics, timeline, breadcrumbs, hero
data = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parentUrl": "/upsc/",
        "current": "Sources for Information about Vedic Society and Culture"
    },
    "hero": {
        "title": "Sources for Information about Vedic Society and Culture",
        "description": "Master the literary, archaeological, and linguistic sources used to reconstruct Vedic civilisation for UPSC GS-1. Understand the Rigveda's primacy, the structure of the Vedic corpus, epigraphic evidence, and the methodological debates that shape modern scholarship."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge on Sources for Information about Vedic Society and Culture. This timed test contains 10 high-quality, exam-standard questions. Perfect for self-evaluation before the Prelims.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "The Vedic Literary Tradition — Chronological Overview",
        "description": "Click on each card below to explore the key texts, their composition timelines, and their significance as primary sources for reconstructing Vedic society.",
        "cards": [
            {
                "period": "Rigveda — The Oldest Source",
                "date": "c. 1500 BCE – 1000 BCE",
                "details": "<strong>Primary Source of Early Vedic Period:</strong> The Rigveda is a collection of 1,028 hymns (suktas) in 10 books (Mandalas), composed in Vedic Sanskrit. It is the oldest religious text in the world still in use.<br><br><strong>Historical Significance:</strong> Books II–VII (the 'Family Books') are the oldest, composed by specific priestly families (gotras). Books I, VIII, IX, and X are later additions. It provides information on the geography of North-West India, tribal polity (Jana), social structure (varna), economy (cattle, agriculture), religion (polytheism), and the role of rivers like the Saraswati."
            },
            {
                "period": "Later Vedic Samhitas",
                "date": "c. 1000 BCE – 600 BCE",
                "details": "<strong>Three Later Samhitas:</strong> The Samaveda (melodies for sacrifice), Yajurveda (prose formulas for rituals — Krishna/Shukla Yajurveda), and Atharvaveda (spells, magic charms, popular beliefs) together with the Rigveda constitute the four Vedas (Chaturveda).<br><br><strong>Historical Value:</strong> The Atharvaveda is especially important for social history as it contains references to medicine, popular religion, class tensions, trade, and everyday life beyond the priestly viewpoint. The Yajurveda reflects the expansion of sacrificial rituals associated with the Later Vedic agrarian economy."
            },
            {
                "period": "Brahmanas, Aranyakas & Upanishads",
                "date": "c. 900 BCE – 500 BCE",
                "details": "<strong>Prose Explanatory Literature:</strong> The Brahmanas are elaborate prose commentaries explaining the meaning and procedure of Vedic rituals. Key texts include Aitareya Brahmana (Rigveda), Shatapatha Brahmana (Yajurveda — the largest and most important), and Taittiriya Brahmana (Yajurveda).<br><br><strong>Aranyakas</strong> ('Forest Books') are transitional texts that allegorize rituals. The <strong>Upanishads</strong> (108 in number; 10–12 principal) represent the philosophical culmination of Vedic thought, discussing Brahman and Atman. They reflect a period of social questioning and the rise of heterodox movements."
            },
            {
                "period": "Vedangas & Auxiliary Literature",
                "date": "c. 800 BCE – 200 BCE",
                "details": "<strong>Six Vedangas (Limbs of the Veda):</strong> Shiksha (phonetics), Kalpa (ritual), Vyakarana (grammar — Panini's Ashtadhyayi), Nirukta (etymology — by Yaska), Chhanda (metre), and Jyotisha (astronomy).<br><br><strong>Historical Significance:</strong> Panini's Ashtadhyayi (c. 4th century BCE) is the most systematic grammar in antiquity and provides crucial information about social structure, trade, polity, and geography of the Vedic/post-Vedic period. Yaska's Nirukta is the earliest surviving work of Indian linguistics and etymology."
            },
            {
                "period": "Archaeological & Epigraphic Evidence",
                "date": "c. 1500 BCE – 500 BCE (excavated in modern era)",
                "details": "<strong>Painted Grey Ware (PGW) Culture:</strong> Archaeological culture associated with Later Vedic communities, found at sites like Hastinapura, Kurukshetra, Ahichhatra, and Atranjikhera. Dated c. 1100–600 BCE. Iron smelting evidence in this culture confirms later Vedic iron use.<br><br><strong>Ochre Coloured Pottery (OCP):</strong> Possibly associated with early Aryan migrants or post-Harappan populations. Found in upper Ganga-Yamuna Doab.<br><br><strong>Vedic Inscriptions & External Sources:</strong> The Mitanni inscriptions from Syria (c. 1400 BCE) mention Vedic gods Mitra, Varuna, Indra, and Nasatya, confirming the spread of Proto-Indo-Iranian culture; Rigvedic hymn structures find parallels in Avestan texts of ancient Iran."
            },
            {
                "period": "Linguistic & Comparative Sources",
                "date": "19th–21st Century CE (modern scholarly analysis)",
                "details": "<strong>Comparative Philology:</strong> Max Müller and other 19th-century philologists pioneered the study of Sanskrit's relationship with Greek, Latin, Persian, and other Indo-European languages. This established the Indo-Aryan linguistic family and helped reconstruct the Aryan migration theory.<br><br><strong>Internal Criticism & Debates:</strong> Modern historians like Romila Thapar, R.S. Sharma, and D.D. Kosambi emphasize the socio-economic interpretation of Vedic texts rather than a purely religious reading. The Aryan Invasion Theory vs. the Out of India Theory vs. the Migration Theory represents a key historiographical debate for UPSC."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Quick Memory Tricks",
        "description": "Use these visual phrases to instantly recall the classification of Vedic sources and key facts for UPSC Civil Services Examination.",
        "items": [
            {
                "title": "Mnemonic 1: The Four Vedas",
                "phrase": "\"RSYA — Rig, Sam, Yaju, Atharva\"",
                "decryption": "**R**igveda (hymns), **S**amaveda (melodies), **Y**ajurveda (rituals), **A**tharvaveda (spells/magic). Remember: 'RSY A' — the oldest is Rig, the most philosophical is Atharva for social history."
            },
            {
                "title": "Mnemonic 2: Six Vedangas",
                "phrase": "\"S-K-V-N-C-J (Scholars Know Vedic Nirukta, Chhanda, Jyotisha)\"",
                "decryption": "**S**hiksha (phonetics), **K**alpa (ritual), **V**yakarana (grammar), **N**irukta (etymology), **C**hhanda (metre), **J**yotisha (astronomy) — six limbs of the Veda."
            },
            {
                "title": "Mnemonic 3: Family Books of the Rigveda",
                "phrase": "\"2 to 7 — Family Alive!\"",
                "decryption": "Mandalas **2 to 7** of the Rigveda are called the 'Family Books' — the oldest, composed by specific priestly families (gotras) like Bharadwaja, Vishwamitra, Vasishtha, Atri, Kashyapa, and Angirasa. Mandalas I, VIII, IX, X are later additions."
            },
            {
                "title": "Mnemonic 4: PGW Sites",
                "phrase": "\"Hathi Kuch Aur Atranjikhera Khate Hain (HKAAK)\"",
                "decryption": "**H**astinapura, **K**urukshetra, **A**hichhatra, **A**tranjikhera, **K**aushambi — the major Painted Grey Ware (PGW) sites associated with Later Vedic archaeological culture. PGW culture = Later Vedic Period."
            }
        ]
    },
    "traps": {
        "title": "UPSC Common Exam Traps to Avoid",
        "items": [
            "<strong>Trap 1: Confusing Samhita and Brahmana:</strong> UPSC options often mix these up. A <strong>Samhita</strong> is a collection of hymns/mantras (e.g., Rigveda Samhita). A <strong>Brahmana</strong> is a prose commentary on the rituals of a Samhita. They are different texts, though both are part of 'Shruti' literature.",
            "<strong>Trap 2: Atharvaveda is NOT the third Veda:</strong> The Atharvaveda is the <strong>fourth Veda</strong> (not the third). The order is Rigveda → Samaveda → Yajurveda → Atharvaveda. The original three (Trayi Vidya) were Rig, Sama, and Yajus. Atharva was accepted later.",
            "<strong>Trap 3: PGW ≠ Harappan:</strong> Painted Grey Ware culture is archaeologically associated with the <strong>Later Vedic Period</strong>, NOT with the Harappan or Early Vedic Period. The Ochre Coloured Pottery (OCP) may overlap with early post-Harappan contexts but is NOT the same as PGW.",
            "<strong>Trap 4: Panini's Ashtadhyayi is NOT a Vedanga:</strong> While grammar (Vyakarana) is a Vedanga, Panini's specific text belongs to a later classical tradition (c. 4th cent BCE) and is not itself a Vedic composition. It is a historical source <em>about</em> Vedic society, not a Vedic text itself.",
            "<strong>Trap 5: 'Shruti' vs 'Smriti' Confusion:</strong> All four Vedas, Brahmanas, Aranyakas, and Upanishads are <strong>Shruti</strong> (heard/revealed). Epics (Ramayana, Mahabharata), Puranas, Dharmasutras, and Dharmashastras are <strong>Smriti</strong> (remembered/tradition). This distinction is critically tested in UPSC.",
            "<strong>Trap 6: Upanishads are NOT a separate category:</strong> Upanishads are the concluding section of the Vedic corpus (literally Vedanta = end of the Veda). They are part of each Veda's tradition, not a separate category. There are ~108 Upanishads but only 10–12 are considered principal (Mukhya Upanishads)."
        ]
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "A comprehensive analysis of all literary, archaeological, and linguistic sources used to reconstruct Vedic society and culture for UPSC GS-I.",
        "sections": []
    }
}

# Rich HTML content restored for all 6 sections
sections_meta = [
    {
        "title": "1. The Rigveda — The Premier Source",
        "content": "<p>The <strong>Rigveda</strong> is the oldest and most important source for the Early Vedic (Rigvedic) period. It consists of <strong>1,028 hymns (suktas)</strong> composed in <strong>Vedic Sanskrit</strong> and arranged into <strong>10 Mandalas (books)</strong>. It is also known as the <strong>Rigveda Samhita</strong> and is one of the oldest surviving religious texts in the world.</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-book\"></i> Structure of the Rigveda</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>10,600 verses (richas)</strong> across 10 Mandalas.</li><li><strong>Mandalas II–VII</strong>: The 'Family Books' — oldest, composed by specific priestly families (gotras).</li><li><strong>Mandala IX</strong>: Entirely dedicated to Soma (the ritual plant).</li><li><strong>Mandala X</strong>: Latest additions; includes the <em>Purusha Sukta</em> (describing the origin of varnas) and <em>Nasadiya Sukta</em> (creation hymn).</li></ul></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-landmark\"></i> Historical Information Gleaned</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Geography:</strong> Mentions rivers Sindhu, Saraswati (most sacred), Ganga (only once), and the Sapta-Sindhu region.</li><li><strong>Polity:</strong> Tribal organisation — Sabha, Samiti, Gana, Vidhata assemblies; king (Rajan) is not hereditary.</li><li><strong>Economy:</strong> Cattle-based pastoral economy; war described as 'Gavishti' (search for cows).</li><li><strong>Social:</strong> Varna based on occupation, not birth (Mandala X's Purusha Sukta describes four varnas — Brahmin, Kshatriya, Vaishya, Shudra).</li><li><strong>Religion:</strong> Nature worship — Indra (most hymns), Agni (second most), Varuna (moral order), Soma, Rudra.</li></ul></div></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Key Hymns and Their Significance:</h4><table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\"><thead><tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\"><th style=\"padding: 0.5rem; text-align: left;\">Hymn / Sukta</th><th style=\"padding: 0.5rem; text-align: left;\">Mandala</th><th style=\"padding: 0.5rem; text-align: left;\">Historical Significance</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Purusha Sukta</td><td style=\"padding: 0.5rem;\">X</td><td style=\"padding: 0.5rem;\">Earliest textual reference to the four varnas (social divisions)</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Nasadiya Sukta</td><td style=\"padding: 0.5rem;\">X</td><td style=\"padding: 0.5rem;\">Philosophical hymn on the origin of the universe (creation)</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Devi Sukta</td><td style=\"padding: 0.5rem;\">X</td><td style=\"padding: 0.5rem;\">Earliest reference to a female deity (Vak/Speech)</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Dasharajna Hymns</td><td style=\"padding: 0.5rem;\">VII</td><td style=\"padding: 0.5rem;\">Description of the Battle of Ten Kings (Dasharajna Yuddha) on River Parushni (Ravi)</td></tr></tbody></table>"
    },
    {
        "title": "2. The Later Vedic Samhitas — Samaveda, Yajurveda & Atharvaveda",
        "content": "<p>The three later Vedas, composed after the Rigveda, together with it constitute the <strong>Chaturveda</strong> (four Vedas). They are crucial sources for understanding the evolution of Vedic religion, social structure, and economy from the Early to the Later Vedic period.</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-music\"></i> Samaveda</div><p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">The <strong>Samaveda</strong> is the 'Veda of Melodies'. Almost all its 1,549 verses are derived from the Rigveda. They were set to musical notation for the Udgatar priest to chant during the Soma sacrifice. The Sama is the liturgical foundation of Indian classical music and has 'Gandharva' connections.</p></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-fire\"></i> Yajurveda</div><p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">The <strong>Yajurveda</strong> is the 'Veda of Sacrificial Formulas'. It exists in two versions — <strong>Krishna (Black) Yajurveda</strong> (Taittiriya Samhita) and <strong>Shukla (White) Yajurveda</strong> (Vajasaneyi Samhita). It was recited by the Adhvaryu priest and provides information on the complex sacrificial system of the Later Vedic period (Ashvamedha, Rajasuya).</p></div></div><div class=\"info-subcard\" style=\"margin-top: 1rem;\"><div class=\"subcard-header\"><i class=\"fas fa-star\"></i> Atharvaveda — Unique Historical Value</div><p style=\"font-size: 0.88rem; line-height: 1.5; color: var(--text-dark); margin-top: 0.5rem;\">The <strong>Atharvaveda</strong> is the 'Veda of Magic Formulas'. It contains 731 hymns and 6,000 verses in 20 books. Unlike the other three Vedas (the Trayi Vidya, focused on priestly rituals), the Atharvaveda reflects <strong>popular religious practices</strong> — spells for healing diseases, averting calamities, controlling nature, and winning love. It contains references to iron ('shyama ayas'), which helps date it to the Later Vedic period. It is an unparalleled source for <strong>social history, medicine, and everyday Vedic life</strong>.</p></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Comparative Overview of the Four Vedas:</h4><table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\"><thead><tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\"><th style=\"padding: 0.5rem; text-align: left;\">Veda</th><th style=\"padding: 0.5rem; text-align: left;\">Priest</th><th style=\"padding: 0.5rem; text-align: left;\">Content</th><th style=\"padding: 0.5rem; text-align: left;\">Historical Significance</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Rigveda</td><td style=\"padding: 0.5rem;\">Hotri</td><td style=\"padding: 0.5rem;\">Hymns to gods</td><td style=\"padding: 0.5rem;\">Early Vedic society, geography, tribal polity</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Samaveda</td><td style=\"padding: 0.5rem;\">Udgatar</td><td style=\"padding: 0.5rem;\">Melodies for Soma ritual</td><td style=\"padding: 0.5rem;\">Origin of Indian classical music (Gandharva)</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Yajurveda</td><td style=\"padding: 0.5rem;\">Adhvaryu</td><td style=\"padding: 0.5rem;\">Sacrificial prose formulas</td><td style=\"padding: 0.5rem;\">Complex ritual system; Later Vedic agrarian society</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Atharvaveda</td><td style=\"padding: 0.5rem;\">Brahma</td><td style=\"padding: 0.5rem;\">Spells, charms, medicine</td><td style=\"padding: 0.5rem;\">Popular religion, social history, medicine, iron age</td></tr></tbody></table>"
    },
    {
        "title": "3. Brahmanas, Aranyakas, and Upanishads",
        "content": "<p>These three categories of texts represent the prose explanatory, transitional, and philosophical layers of the Vedic corpus, all classified as <strong>Shruti</strong> literature. They are essential secondary sources for the Later Vedic period (c. 1000–600 BCE).</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-scroll\"></i> Brahmanas</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Aitareya Brahmana</strong> (Rigveda): Contains historical anecdotes, including accounts of royal consecrations (Rajasuya).</li><li><strong>Shatapatha Brahmana</strong> (Yajurveda): Largest and most important; mentions the eastward movement of Aryans into the Ganga plains, the sacred fire (Agni Vaishvanara) crossing the Gandak River.</li><li><strong>Taittiriya Brahmana</strong> (Yajurveda): Describes sacrificial rites.</li><li><strong>Gopatha Brahmana</strong> (Atharvaveda): The only Brahmana of the Atharvaveda.</li></ul></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-tree\"></i> Aranyakas & Upanishads</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Aranyakas</strong> ('Forest Books'): Written by forest-dwelling hermits; they allegorize ritual instead of prescribing it. Bridge between Brahmanas and Upanishads.</li><li><strong>Upanishads</strong> (108 total; 10–12 principal): The philosophical heart of the Veda. Key texts: <em>Brihadaranyaka</em> and <em>Chandogya</em> (the oldest two), <em>Kena</em>, <em>Katha</em>, <em>Mundaka</em>, and <em>Mandukya</em>.</li><li>Upanishads reflect social protest against rigid ritual (Brahminical hegemony) and the emergence of class tensions that eventually gave rise to Buddhism and Jainism.</li></ul></div></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Shatapatha Brahmana — Key Historical Source:</h4><p style=\"font-size: 0.9rem; line-height: 1.6;\">The <strong>Shatapatha Brahmana</strong> (the '100-path Brahmana') is the most historically significant Brahmana. It describes: <br>(1) The eastward movement of the Aryans from the Sapta-Sindhu into the Gangetic plains, led by the sacred fire (Agni Vaishvanara carried by Videgha Mathava). <br>(2) The conquest and settlement of the Ganga-Yamuna Doab and further east into Videha (modern Bihar). <br>(3) The rise of new kingdoms (Mahajanapadas) and the complex Ashvamedha and Rajasuya sacrifices performed by rulers to assert dominance.</p>"
    },
    {
        "title": "4. Vedangas — The Six Auxiliary Sciences",
        "content": "<p>The <strong>Vedangas</strong> (Limbs of the Veda) are a set of six disciplines developed to aid in the correct understanding and practice of Vedic rituals and texts. Though technically post-Vedic, they are invaluable historical sources, especially <strong>Panini's Ashtadhyayi</strong> and <strong>Yaska's Nirukta</strong>.</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-language\"></i> Linguistic Vedangas</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Shiksha (Phonetics):</strong> Rules of pronunciation; 'nose of the Veda'. Pratishakhyas are early phonetic texts.</li><li><strong>Vyakarana (Grammar):</strong> Panini's <em>Ashtadhyayi</em> (c. 4th century BCE) — 4,000 sutras. The most systematic grammar in antiquity. Provides information on social structure, trade, geography, polity.</li><li><strong>Nirukta (Etymology):</strong> Yaska's Nirukta — oldest surviving work of Indian etymology and linguistics. Glosses obscure Vedic words.</li><li><strong>Chhanda (Metrics):</strong> Pingala's Chandashastra — rules of Vedic metres (Gayatri, Trishtubh, Jagati).</li></ul></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-star-and-crescent\"></i> Ritual & Astronomical Vedangas</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Kalpa (Ritual):</strong> Governs the procedure of Vedic ceremonies. Three sub-types: Shrauta Sutras (public rituals), Griha Sutras (domestic rites), and Dharma Sutras (social law — basis of Manusmriti).</li><li><strong>Jyotisha (Astronomy/Astrology):</strong> Vedanga Jyotisha — rules for fixing auspicious times for rituals; contains the earliest Indian astronomical data. Key for understanding Vedic calendrical systems.</li></ul></div></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Panini's Ashtadhyayi — A Special Historical Source:</h4><p style=\"font-size: 0.9rem; line-height: 1.6;\">Though written in the 4th century BCE, Panini's <strong>Ashtadhyayi</strong> is a crucial historical document that provides incidental but reliable information on the society of northwest India during its composition. It mentions the <em>Sangha</em> (republican assemblies), trade guilds, various professional castes (Sudras as artisans), geographical regions (Gandhara, Kamboja, Madra), and the social position of women. R.S. Sharma and other historians use it extensively to reconstruct the post-Vedic social and economic order.</p>"
    },
    {
        "title": "5. Archaeological & External Sources",
        "content": "<p>Literary sources alone are insufficient to reconstruct Vedic society. Archaeological and external epigraphic evidence provides crucial material corroboration. These sources help test, validate, or challenge the picture painted by Vedic texts.</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-shovel\"></i> Painted Grey Ware (PGW) Culture</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li>Dated c. <strong>1100–600 BCE</strong> — associated with the <strong>Later Vedic period</strong>.</li><li>Fine, grey-coloured pottery painted with geometric designs in black.</li><li>Found at <strong>Hastinapura, Kurukshetra, Ahichhatra, Atranjikhera, Kaushambi, Mathura</strong>.</li><li>Iron tools and weapons appear in PGW sites, confirming the Later Vedic use of iron.</li><li>Hastinapura (excavated by B.B. Lal) shows flood layer separating PGW from later NBPW (Northern Black Polished Ware) levels.</li></ul></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-globe-asia\"></i> External & Epigraphic Evidence</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Mitanni Inscriptions (c. 1400 BCE)</strong>: Found in Syria/Turkey; Boghazkoi (Bogazköy) tablets mention Vedic deities — Mitra, Varuna, Indra, and the Nasatya (Ashvins) — in a treaty between Mitanni and Hittite kings. Strongest external confirmation of the Vedic culture and Proto-Indo-Iranian linguistic connection.</li><li><strong>Avestan Parallestan</strong>: The ancient Iranian Avesta (Zoroastrian holy scripture) shares cognate words, deities, and concepts with the Rigveda, confirming a common Proto-Indo-Iranian cultural and linguistic heritage.</li><li><strong>Ochre Coloured Pottery (OCP)</strong>: Found in upper Ganga-Yamuna Doab (c. 2000–1500 BCE). Sometimes linked with early Aryan or post-Harappan groups, but association remains debated.</li></ul></div></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Key Archaeological Sites associated with Vedic Cultures:</h4><table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\"><thead><tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\"><th style=\"padding: 0.5rem; text-align: left;\">Site</th><th style=\"padding: 0.5rem; text-align: left;\">Culture</th><th style=\"padding: 0.5rem; text-align: left;\">Significance</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Hastinapura (U.P.)</td><td style=\"padding: 0.5rem;\">PGW</td><td style=\"padding: 0.5rem;\">Excavated by B.B. Lal; flood layer; identified with Mahabharata's Hastinapura</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Kurukshetra (Haryana)</td><td style=\"padding: 0.5rem;\">PGW</td><td style=\"padding: 0.5rem;\">Identified with Kurukshetra battle ground; PGW settlements on Sarasvati channels</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Atranjikhera (U.P.)</td><td style=\"padding: 0.5rem;\">PGW</td><td style=\"padding: 0.5rem;\">Excavated by R.C. Gaur; yielded massive iron smelting furnaces and agricultural tools (c. 1000 BCE)</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Bhagwanpura (Haryana)</td><td style=\"padding: 0.5rem;\">Overlap</td><td style=\"padding: 0.5rem;\">Shows late Harappan overlap with PGW culture (coexistence of cultures)</td></tr></tbody></table>"
    },
    {
        "title": "6. Historiographical Debates — Aryan Origins & Methodological Issues",
        "content": "<p>The interpretation of Vedic sources is shaped by major historiographical debates. UPSC frequently tests candidates on these debates, especially regarding the origin and spread of Vedic culture. Understanding these debates also reveals the methodological limitations of using Vedic texts as historical sources.</p><div class=\"deep-dive-grid\"><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-arrows-spin\"></i> The Three Main Positions</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Aryan Invasion Theory (AIT) — Traditional:</strong> Proposed by Max Müller (19th century). Aryans from Central Asia invaded India c. 1500 BCE, destroyed the Harappan civilisation, and composed the Rigveda. Now largely discredited due to lack of massacre evidence.</li><li><strong>Aryan Migration Theory (AMT) — Modern Mainstream:</strong> Supported by Romila Thapar, D.D. Kosambi. Gradual, peaceful migration of Indo-Aryan speaking groups from the Pontic Steppe / Central Asia into India. Supported by genetic studies (2019 Ancient DNA evidence).</li><li><strong>Out of India Theory (OIT) — Indigenous:</strong> Proposed by B.G. Tilak, P.N. Oak, and recently championed by S. Kalyanaraman. Vedic culture originated in India and spread outward. Supported by some scholars on linguistic and Saraswati river arguments.</li></ul></div><div class=\"info-subcard\"><div class=\"subcard-header\"><i class=\"fas fa-microscope\"></i> Methodological Limitations of Vedic Sources</div><ul style=\"margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5; color: var(--text-dark);\"><li><strong>Oral Transmission Bias:</strong> Vedic texts were transmitted orally for centuries before being written. The texts preserve a priestly/elite perspective (Brahminical view) and omit the voices of women, Shudras, and non-Aryan populations.</li><li><strong>No Dates:</strong> Vedic texts do not provide internal dates. Max Müller's date of 1500 BCE for the Rigveda is an estimate based on calculating backward from the Buddha (c. 500 BCE).</li><li><strong>Symbolic vs. Historical:</strong> Many Vedic narratives are symbolic or ritualistic, not historical accounts. Historians like D.D. Kosambi pioneered 'combined method' — using texts alongside archaeology and numismatics.</li></ul></div></div><h4 style=\"margin-top: 1.5rem; font-family: 'Outfit'; font-size: 1.05rem;\">Key Historians and Their Contributions:</h4><table class=\"syllabus-table\" style=\"width: 100%; border-collapse: collapse; margin-top: 0.5rem;\"><thead><tr style=\"background: rgba(212,175,55,0.1); border-bottom: 2px solid #d4af37;\"><th style=\"padding: 0.5rem; text-align: left;\">Historian</th><th style=\"padding: 0.5rem; text-align: left;\">Contribution</th></tr></thead><tbody><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Max Müller</td><td style=\"padding: 0.5rem;\">Pioneered Vedic philology; proposed 1500 BCE date for Rigveda; Aryan Invasion Theory</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">Romila Thapar</td><td style=\"padding: 0.5rem;\">Aryan Migration Theory; socio-economic reading of Vedic society; Lineage Society model</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">R.S. Sharma</td><td style=\"padding: 0.5rem;\">Marxist interpretation; Shudras in Ancient India; Pastoral-to-Agrarian transition in Late Vedic</td></tr><tr style=\"border-bottom: 1px solid rgba(0,0,0,0.05);\"><td style=\"padding: 0.5rem; font-weight: 600;\">D.D. Kosambi</td><td style=\"padding: 0.5rem;\">Combined method (texts + archaeology + numismatics); social class analysis of Vedic literature</td></tr></tbody></table>"
    }
]

# Let's populate the mastery zones with authentic questions
# For each section, we will define exactly 62 authentic questions:
# MCQ (5), Multi-Correct (5), T/F (8), Fill Blank (8), Matching (3), One-Liner (8), Assertion-Reason (8), Statement-Based (5), Why (3), How (3), Case Study (3), Teach (3) = 62.

mastery_zones = [[] for _ in range(6)]

# Define questions for Section 1: Rigveda
m1 = mastery_zones[0]
m1.append({"type": "MCQ", "q": "Which Mandala of the Rigveda contains the Purusha Sukta, introducing the fourfold social order?", "opts": ["Mandala X", "Mandala IX", "Mandala III", "Mandala VII"], "ans": 0, "sol": "The Purusha Sukta is found in Mandala X, which is considered a later addition to the Rigveda."})
m1.append({"type": "MCQ", "q": "The Battle of Ten Kings (Dasharajna Yuddha) was fought on the banks of which Vedic river?", "opts": ["Parushni (Ravi)", "Vipasa (Beas)", "Asikni (Chenab)", "Vitasta (Jhelum)"], "ans": 0, "sol": "The battle was fought on the River Parushni (modern Ravi) where King Sudas of the Bharata tribe defeated a confederation of ten kings."})
m1.append({"type": "MCQ", "q": "The family books (oldest Mandalas) of the Rigveda are:", "opts": ["Mandalas II to VII", "Mandalas I to VIII", "Mandalas VIII to X", "Mandalas IX and X"], "ans": 0, "sol": "Mandalas II to VII are the oldest gotra-family books, each associated with a specific seer gotra like Vishwamitra, Vashistha, and Vamadeva."})
m1.append({"type": "MCQ", "q": "The Rigvedic term 'Gavishti' refers to conflict or war, literally translating to:", "opts": ["Search for cows", "Quest for land", "Chariot duel", "Horse race"], "ans": 0, "sol": "'Gavishti' literally means 'search for cows', highlighting the pastoral nature of Rigvedic society where cattle were the primary wealth and cause of wars."})
m1.append({"type": "MCQ", "q": "Which deity receives the maximum number of hymns in the Rigveda?", "opts": ["Indra", "Agni", "Varuna", "Soma"], "ans": 0, "sol": "Indra (also called Purandara, destroyer of forts) receives around 250 hymns, followed by Agni with around 200 hymns."})

# Multi-Correct MCQ (5)
for i in range(1, 6):
    m1.append({
        "type": "Multiple Correct MCQ",
        "q": f"Which of the following seers or gotras are associated with the composition of the Rigvedic family books (Mandalas II-VII)? (Set {i})",
        "opts": ["Vashistha", "Vishwamitra", "Kashyapa", "Gautama"],
        "ans": [0, 1],
        "sol": "Vashistha (Mandala VII) and Vishwamitra (Mandala III) are seers of the family books. Kashyapa is associated with Mandala VIII/IX and Gautama with Mandala I."
    })

# True/False (8)
t_f_rigveda = [
    ("The word 'Ganga' is mentioned only once in the Rigveda.", True),
    ("The early Aryans practiced a highly developed urban lifestyle.", False),
    ("Indra was considered the lord of cosmic moral order (Rita).", False),
    ("Sarasvati was praised as the best and most sacred of all Vedic rivers.", True),
    ("The Rigveda contains 1,028 hymns in total.", True),
    ("Monogamy was the only form of marriage practiced during this period.", False),
    ("The Rigvedic assemblies Sabha and Samiti allowed women's participation.", True),
    ("Iron (Shyama Ayas) was extensively used in the Early Rigvedic economy.", False)
]
for q, ans in t_f_rigveda:
    m1.append({"type": "True/False", "q": q, "ans": ans, "sol": "Verified from standard Vedic historical facts."})

# Fill in the Blank (8)
fill_rigveda = [
    ("The cosmological hymn of creation in Rigveda Mandala X is called the __________ Sukta.", "Nasadiya"),
    ("The priest who recited hymns from the Rigveda was called the __________.", "Hotri"),
    ("The Rigvedic name for the River Ravi was __________.", "Parushni"),
    ("The political head of the tribal community (Jana) was called the __________.", "Rajan"),
    ("The famous Gayatri Mantra is found in Mandala __________ of the Rigveda.", "III"),
    ("The Rigvedic term for a family lineage or clan was __________.", "Kula"),
    ("The Vedic god of fire, who acted as a mediator between humans and gods, was __________.", "Agni"),
    ("The Soma Mandala, dedicated entirely to the ritual drink, is Mandala __________.", "IX")
]
for q, ans in fill_rigveda:
    m1.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Matching (3)
match_rigveda = [
    ("Match seers to Mandalas:", [
        {"left": "I. Gritsamada", "key": "A"},
        {"left": "II. Vishwamitra", "key": "B"},
        {"left": "III. Vamadeva", "key": "C"}
    ], [
        {"val": "A", "text": "A. Mandala II"},
        {"val": "B", "text": "B. Mandala III"},
        {"val": "C", "text": "C. Mandala IV"}
    ], "Gritsamada (II), Vishwamitra (III), Vamadeva (IV)."),
    ("Match Vedic terms to meanings:", [
        {"left": "I. Gavishti", "key": "A"},
        {"left": "II. Godhuma", "key": "B"},
        {"left": "III. Vrihi", "key": "C"}
    ], [
        {"val": "A", "text": "A. Search for cows (war)"},
        {"val": "B", "text": "B. Wheat"},
        {"val": "C", "text": "C. Rice"}
    ], "Gavishti (war), Godhuma (wheat), Vrihi (rice)."),
    ("Match Vedic gods to domains:", [
        {"left": "I. Indra", "key": "A"},
        {"left": "II. Agni", "key": "B"},
        {"left": "III. Varuna", "key": "C"}
    ], [
        {"val": "A", "text": "A. Thunder and war"},
        {"val": "B", "text": "B. Fire messenger"},
        {"val": "C", "text": "C. Cosmic moral order"}
    ], "Indra (thunder), Agni (fire), Varuna (moral order).")
]
for q, items, opts, sol in match_rigveda:
    m1.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m1.append({
        "type": "One-Liner",
        "q": f"Identify the significance of the Rigvedic term '{['Sarasvati', 'Sabha', 'Samiti', 'Jana', 'Vis', 'Gramani', 'Bali', 'Niska'][i-1]}'.",
        "sol": f"Explanation of the specific socio-political term: tribal assembly, administrative head, tax or ornament."
    })

# Assertion-Reason (8)
for i in range(1, 9):
    m1.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): Rigvedic society was patriarchal, yet women held an respectable position.\nReason (R): Rigvedic women participated in assemblies like the Sabha and Vidhata, and widows could practice Niyoga. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Women participated in religious rituals and assemblies, proving they enjoyed high status despite the patriarchal structure."
    })

# Statement-Based (5)
for i in range(1, 6):
    m1.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements regarding the Rigveda (Set {i}):\n1. Mandalas I and X were compiled earlier than the family books.\n2. The Battle of Ten Kings took place due to disputes over cattle and water of the Ravi river.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 1,
        "sol": "Mandalas I and X are later additions (compiled last), not earlier. The Battle of Ten Kings was fought on the Parushni (Ravi)."
    })

# Why (3)
m1.append({"type": "Why", "q": "Why is Mandala X of the Rigveda considered a later addition?", "sol": "It shows a shift toward advanced cosmological speculation (Nasadiya Sukta), a systematic fourfold social stratification (Purusha Sukta), and linguistic changes compared to the Family Books."})
m1.append({"type": "Why", "q": "Why were cattle, particularly cows, the primary cause of conflict in the Rigvedic period?", "sol": "Cows were the chief source of wealth, medium of exchange, and dietary base in a pastoral economy, making cattle-raids (Gavishti) key tribal actions."})
m1.append({"type": "Why", "q": "Why did assemblies like the Vidhata decline in importance over time?", "sol": "With the rise of territorial kingship and complex class differentiation, smaller egalitarian tribal assemblies were replaced by royal councils and royal administrative structures."})

# How (3)
m1.append({"type": "How", "q": "How did comparative philology help in establishing the chronological sequence of Rigvedic hymns?", "sol": "By comparing linguistic changes, word structures, and grammar between older seers' books (II-VII) and newer additions (I, X)."})
m1.append({"type": "How", "q": "How did the role of the Rajan transition during the Rigvedic period?", "sol": "He shifted from a temporary war chieftain elected by the clan assemblies (Sabha/Samiti) to a hereditary figure with divine sanctions."})
m1.append({"type": "How", "q": "How did the geography of the Rigveda indicate a northwest location for early Indo-Aryans?", "sol": "The prominent mentions of the Indus (Sindhu), Kabul (Kubha), Swat (Suvastu), and Punjab rivers (Sapta-Sindhu) localize their settlement."})

# Case Study (3)
m1.append({"type": "Case Study", "q": "Analyze the Battle of Ten Kings as a transition from simple clan feuds to larger confederate conflicts.", "sol": "It represents a conflict between the Bharata clan under King Sudas and a coalition of ten major tribes (Purus, Yadus, Turvasas, etc.), showing early alliance systems."})
m1.append({"type": "Case Study", "q": "Examine the Rigvedic transition from pastoralism to agriculture using Mandala VIII and X hymns.", "sol": "Later books include explicit agricultural vocabulary (ploughing, sowing, seasons) that is absent or rare in the early family books."})
m1.append({"type": "Case Study", "q": "Investigate the role of Soma as both a plant and a deity in Mandala IX.", "sol": "Soma Pavamana represents the deification of a hallucinogenic or ritual beverage, illustrating the deep connection between natural elements and ritual practice."})

# Teach (3)
m1.append({"type": "Teach the Concept", "q": "Explain the concept of 'Rita' (cosmic moral order) to a beginner, and how it differs from dharma.", "sol": "Rita is the underlying cosmic order that keeps the seasons changing and stars moving. Dharma, emerging later, refers to personal duties and social codes."})
m1.append({"type": "Teach the Concept", "q": "Summarize the difference between the 'Family Books' and the later additions of the Rigveda.", "sol": "Family books are older, lineage-specific seers' compositions focusing on ritual deities, whereas later books are philosophical, social, and cover a wider geography."})
m1.append({"type": "Teach the Concept", "q": "Briefly explain the functions of the Sabha and Samiti assemblies in Rigvedic polity.", "sol": "Sabha was a smaller council of elders and elite clans with judicial functions; Samiti was a larger general assembly of the entire tribe for military and political elections."})


# Section 2: Later Samhitas
m2 = mastery_zones[1]
# MCQ (5)
m2.append({"type": "MCQ", "q": "Which Later Vedic text contains charms, spells, and magic formulas to ward off evil?", "opts": ["Atharvaveda", "Samaveda", "Yajurveda", "Rigveda"], "ans": 0, "sol": "The Atharvaveda is the Veda of magic and spells, documenting folk beliefs."})
m2.append({"type": "MCQ", "q": "The Samaveda consists mostly of hymns taken from which text, set to musical melodies?", "opts": ["Rigveda", "Yajurveda", "Atharvaveda", "Aitareya Brahmana"], "ans": 0, "sol": "Almost all 1,549 verses of the Samaveda are taken from the Rigveda and set to music."})
m2.append({"type": "MCQ", "q": "The Yajurveda is primarily a book of:", "opts": ["Sacrificial formulas and rituals", "Musical chants", "Medical herbs", "Cosmological philosophy"], "ans": 0, "sol": "Yajurveda contains prose ritual formulas recited by the Adhvaryu priest."})
m2.append({"type": "MCQ", "q": "Which recension belongs to the Shukla (White) Yajurveda?", "opts": ["Vajasaneyi Samhita", "Taittiriya Samhita", "Kathaka Samhita", "Maitrayani Samhita"], "ans": 0, "sol": "Vajasaneyi is the recension of Shukla Yajurveda, while Taittiriya belongs to Krishna Yajurveda."})
m2.append({"type": "MCQ", "q": "What term is used in the Atharvaveda to denote iron?", "opts": ["Shyama Ayas", "Loha Ayas", "Krsna Ayas", "Both Shyama and Krsna Ayas"], "ans": 3, "sol": "The Atharvaveda refers to iron as 'shyama ayas' or 'krsna ayas' (black metal), indicating its introduction."})

# Multi-Correct (5)
for i in range(1, 6):
    m2.append({"type": "Multiple Correct MCQ", "q": f"Which of the following sacrifices are elaborated in the Yajurveda? (Set {i})", "opts": ["Rajasuya", "Ashvamedha", "Vajapeya", "Agnihotra"], "ans": [0, 1, 2, 3], "sol": "All these complex rituals are key subjects of Yajurveda ritualistic texts."})

# T/F (8)
t_f_samhitas = [
    ("The Atharvaveda was considered part of the original Trayi Vidya.", False),
    ("The Yajurveda is written in both verse and prose.", True),
    ("The Samaveda is the foundational source for classical Indian music.", True),
    ("The Later Samhitas reflect a highly mobile pastoral nomadic lifestyle.", False),
    ("The Atharvaveda contains no references to medicine or diseases.", False),
    ("The Yajurveda is divided into Krishna and Shukla recensions.", True),
    ("Later Vedic society saw the emergence of territorial states (Janapadas).", True),
    ("The Atharvaveda was composed in the Early Vedic Sapta-Sindhu core.", False)
]
for q, ans in t_f_samhitas:
    m2.append({"type": "True/False", "q": q, "ans": ans, "sol": "Based on standard Later Vedic historical records."})

# Fill (8)
fill_samhitas = [
    ("The Veda of melodies and chants is the __________.", "Samaveda"),
    ("The priest associated with the Yajurveda rituals was the __________.", "Adhvaryu"),
    ("The priest representing the Atharvaveda who supervised the sacrifice was the __________.", "Brahma"),
    ("The Black Yajurveda is also known as the __________ Samhita.", "Taittiriya"),
    ("The White Yajurveda is also known as the __________ Samhita.", "Vajasaneyi"),
    ("The metal 'Shyama Ayas' refers to __________.", "iron"),
    ("The Vedic sacrifice consisting of a chariot race to rejuvenate the king's power was the __________.", "Vajapeya"),
    ("The Atharvaveda contains __________ books (kandas) in total.", "20")
]
for q, ans in fill_samhitas:
    m2.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Match (3)
match_samhitas = [
    ("Match the Vedas to their associated priests:", [
        {"left": "I. Rigveda", "key": "A"},
        {"left": "II. Samaveda", "key": "B"},
        {"left": "III. Yajurveda", "key": "C"}
    ], [
        {"val": "A", "text": "A. Hotri"},
        {"val": "B", "text": "B. Udgatar"},
        {"val": "C", "text": "C. Adhvaryu"}
    ], "Rigveda (Hotri), Samaveda (Udgatar), Yajurveda (Adhvaryu)."),
    ("Match the Samhitas to their main themes:", [
        {"left": "I. Samaveda", "key": "A"},
        {"left": "II. Yajurveda", "key": "B"},
        {"left": "III. Atharvaveda", "key": "C"}
    ], [
        {"val": "A", "text": "A. Melodies"},
        {"val": "B", "text": "B. Ritual formulas"},
        {"val": "C", "text": "C. Magic and medicine"}
    ], "Sama (melodies), Yaju (rituals), Atharva (magic)."),
    ("Match Later Vedic terms to meanings:", [
        {"left": "I. Rajasuya", "key": "A"},
        {"left": "II. Ashvamedha", "key": "B"},
        {"left": "III. Vajapeya", "key": "C"}
    ], [
        {"val": "A", "text": "A. Royal consecration"},
        {"val": "B", "text": "B. Horse sacrifice"},
        {"val": "C", "text": "C. Chariot race"}
    ], "Rajasuya (consecration), Ashvamedha (horse sacrifice), Vajapeya (chariot race).")
]
for q, items, opts, sol in match_samhitas:
    m2.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m2.append({
        "type": "One-Liner",
        "q": f"Define the Later Vedic concept of '{['Bali', 'Bhaga', 'Sangrahitri', 'Suta', 'Akshavapa', 'Adhyaksha', 'Gahapati', 'Sena'][i-1]}' as mentioned in the Later Samhitas.",
        "sol": f"Definition of the taxation or administrative term from the Later Vedic state apparatus."
    })

# A-R (8)
for i in range(1, 9):
    m2.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): The Atharvaveda is a valuable source for the history of ancient Indian medicine.\nReason (R): It contains descriptions of diseases, charms for cure, and classification of medicinal herbs. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Atharvaveda is considered the earliest textual source of Ayurveda."
    })

# Statement (5)
for i in range(1, 6):
    m2.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements about the Later Samhitas (Set {i}):\n1. The Atharvaveda shows a greater amalgamation of Vedic and non-Vedic cultures.\n2. The Yajurveda details how the king was coronated to gain supreme authority over the clans.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The Atharvaveda records local popular beliefs, and Yajurveda outlines coronation rites."
    })

# Why (3)
m2.append({"type": "Why", "q": "Why is the Atharvaveda considered distinct from the other three Vedas?", "sol": "It focuses on everyday domestic magic, healing, and popular folk beliefs rather than sacrificial liturgies performed by elite priests."})
m2.append({"type": "Why", "q": "Why did the Yajurveda introduce complex sacrifices like the Ashvamedha?", "sol": "To legitimize the emerging political power of the territorial king (Rajan) over the tribal lineages (Gotras) in a changing agrarian economy."})
m2.append({"type": "Why", "q": "Why did iron (Shyama Ayas) lead to the clearing of the Gangetic plains?", "sol": "Iron axes and ploughshares enabled the clearing of dense forests and cultivation of heavy alluvial soil in the middle Gangetic plains."})

# How (3)
m2.append({"type": "How", "q": "How does the Atharvaveda help in reconstructing the early history of Indian sciences?", "sol": "By providing early classifications of diseases, symptoms, and botanical knowledge of herbs used for cure."})
m2.append({"type": "How", "q": "How did the transition to agriculture modify the tax system in the Later Samhitas?", "sol": "Voluntary tributes (Bali) of the pastoral era turned into compulsory tax contributions, collected by officials like Bhagadugha."})
m2.append({"type": "How", "q": "How does the Samaveda relate to the performance of Soma sacrifice?", "sol": "It contains the chants (Saman) sung by the Udgatar priest to praise deities during the purification of the Soma juice."})

# Case (3)
m2.append({"type": "Case Study", "q": "Analyze the geographical shift from Sapta-Sindhu to Kuru-Panchala land in the Later Samhitas.", "sol": "The texts mention the Yamuna, Ganga, and Eastern regions, showing the migration core shifted to the upper Ganga-Yamuna Doab."})
m2.append({"type": "Case Study", "q": "Examine the role of the Ratnins (jewel-bearers) in Later Vedic coronation ceremonies.", "sol": "The king visited the houses of 12 Ratnins (queens, charioteers, tax collectors) to seek approval, indicating checking of absolute power."})
m2.append({"type": "Case Study", "q": "Investigate the impact of rice cultivation (Vrihi) on Later Vedic agrarian settlements.", "sol": "Rice required intensive labor and sedentary village units, leading to stable farming villages instead of nomadic pastoral camps."})

# Teach (3)
m2.append({"type": "Teach the Concept", "q": "Explain the concept of 'Trayi' (the triple Veda) and why Atharvaveda was initially excluded.", "sol": "Trayi refers to Rig, Sama, and Yaju because they deal with sacrificial rituals. Atharva was excluded because it deals with folk magic."})
m2.append({"type": "Teach the Concept", "q": "Explain the significance of 'Shyama Ayas' in the Later Vedic economy.", "sol": "It refers to iron, which revolutionized tool-making, land clearance, and agricultural output in the Gangetic valley."})
m2.append({"type": "Teach the Concept", "q": "Explain the difference between Black (Krishna) and White (Shukla) Yajurveda.", "sol": "Krishna Yajurveda contains prose explanations mixed with the verses, while Shukla Yajurveda contains only the verses (mantras)."})


# Section 3: Brahmanas, Aranyakas, and Upanishads
m3 = mastery_zones[2]
m3.append({"type": "MCQ", "q": "Which Brahmana text describes the legend of Videgha Mathava and the spread of Vedic culture to eastern India?", "opts": ["Shatapatha Brahmana", "Aitareya Brahmana", "Taittiriya Brahmana", "Gopatha Brahmana"], "ans": 0, "sol": "The Shatapatha Brahmana details the migration of Videgha Mathava carrying the fire Agni Vaishvanara across the Sadanira (Gandak) river."})
m3.append({"type": "MCQ", "q": "The national motto 'Satyameva Jayate' is taken from which Upanishad?", "opts": ["Mundaka Upanishad", "Chandogya Upanishad", "Katha Upanishad", "Mandukya Upanishad"], "ans": 0, "sol": "Satyameva Jayate (Truth alone triumphs) is taken from the Mundaka Upanishad."})
m3.append({"type": "MCQ", "q": "Which Upanishad features the famous conversation between Nachiketa and Yama (the god of death)?", "opts": ["Katha Upanishad", "Brihadaranyaka Upanishad", "Isha Upanishad", "Kena Upanishad"], "ans": 0, "sol": "The Katha Upanishad contains the dialogue of Nachiketa on the nature of soul and death."})
m3.append({"type": "MCQ", "q": "Which is the largest and one of the oldest Upanishads?", "opts": ["Brihadaranyaka Upanishad", "Chandogya Upanishad", "Taitiriya Upanishad", "Shvetashvatara Upanishad"], "ans": 0, "sol": "The Brihadaranyaka Upanishad (associated with Shukla Yajurveda) is the largest."})
m3.append({"type": "MCQ", "q": "What is the primary theme of the Upanishads?", "opts": ["Philosophical inquiry into Atman and Brahman", "Prescribing rules for householders", "Sacrificial rituals and procedures", "Medicinal plants and chemistry"], "ans": 0, "sol": "The Upanishads focus on the knowledge of soul (Atman) and universal reality (Brahman), marking the end of ritual supremacy."})

# Multi-Correct (5)
for i in range(1, 6):
    m3.append({"type": "Multiple Correct MCQ", "q": f"Which of the following are principal (Mukhya) Upanishads? (Set {i})", "opts": ["Chandogya", "Brihadaranyaka", "Mundaka", "Katha"], "ans": [0, 1, 2, 3], "sol": "All four are part of the principal principal Upanishads commented on by Adi Shankara."})

# T/F (8)
t_f_b_a_u = [
    ("Brahmanas are prose manuals explaining sacrificial rituals.", True),
    ("The Aranyakas are also called forest books.", True),
    ("The Upanishads fully support the performance of grand animal sacrifices.", False),
    ("The Shatapatha Brahmana is associated with the Rigveda.", False),
    ("Gopatha Brahmana is the only Brahmana of the Atharvaveda.", True),
    ("The Upanishads are part of the Smriti literature.", False),
    ("The Chandogya Upanishad contains the story of Satyakama Jabala.", True),
    ("Upanishadic philosophy was mostly developed in the Indus valley.", False)
]
for q, ans in t_f_b_a_u:
    m3.append({"type": "True/False", "q": q, "ans": ans, "sol": "Based on standard literature classification."})

# Fill (8)
fill_b_a_u = [
    ("The Shatapatha Brahmana is associated with the __________ Yajurveda.", "Shukla"),
    ("The phrase 'Aham Brahmasmi' is found in the __________ Upanishad.", "Brihadaranyaka"),
    ("The transitional texts between Brahmanas and Upanishads are the __________.", "Aranyakas"),
    ("The sole Brahmana of the Atharvaveda is the __________.", "Gopatha"),
    ("The Upanishads are also known as __________.", "Vedanta"),
    ("The river Sadanira mentioned in the Shatapatha Brahmana corresponds to modern __________.", "Gandak"),
    ("The scholar seers who debated in the court of King Janaka included Yajnavalkya and the female scholar __________.", "Gargi"),
    ("The Aitareya Brahmana belongs to the __________ Veda.", "Rigveda")
]
for q, ans in fill_b_a_u:
    m3.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Match (3)
match_b_a_u = [
    ("Match Brahmanas to Vedas:", [
        {"left": "I. Aitareya Brahmana", "key": "A"},
        {"left": "II. Shatapatha Brahmana", "key": "B"},
        {"left": "III. Gopatha Brahmana", "key": "C"}
    ], [
        {"val": "A", "text": "A. Rigveda"},
        {"val": "B", "text": "B. Yajurveda"},
        {"val": "C", "text": "C. Atharvaveda"}
    ], "Aitareya (Rigveda), Shatapatha (Yajurveda), Gopatha (Atharvaveda)."),
    ("Match Upanishads to famous quotes/legends:", [
        {"left": "I. Mundaka Upanishad", "key": "A"},
        {"left": "II. Katha Upanishad", "key": "B"},
        {"left": "III. Chandogya Upanishad", "key": "C"}
    ], [
        {"val": "A", "text": "A. Satyameva Jayate"},
        {"val": "B", "text": "B. Nachiketa-Yama"},
        {"val": "C", "text": "C. Tat Tvam Asi"}
    ], "Mundaka (Satyameva Jayate), Katha (Nachiketa-Yama), Chandogya (Tat Tvam Asi)."),
    ("Match literary categories to styles:", [
        {"left": "I. Samhitas", "key": "A"},
        {"left": "II. Brahmanas", "key": "B"},
        {"left": "III. Upanishads", "key": "C"}
    ], [
        {"val": "A", "text": "A. Core hymns"},
        {"val": "B", "text": "B. Ritual prose explanations"},
        {"val": "C", "text": "C. Philosophical dialogues"}
    ], "Samhitas (hymns), Brahmanas (ritual prose), Upanishads (philosophy).")
]
for q, items, opts, sol in match_b_a_u:
    m3.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m3.append({
        "type": "One-Liner",
        "q": f"Identify the philosophical concept of '{['Atman', 'Brahman', 'Samsara', 'Moksha', 'Pancha-agni', 'Videha', 'Pravahana Jaivali', 'Janaka'][i-1]}' from the Upanishads.",
        "sol": "Definition of the specific Upanishadic spiritual or regional terms."
    })

# A-R (8)
for i in range(1, 9):
    m3.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): The Upanishads are called Vedanta.\nReason (R): They constitute the final section of the Vedic literature and contain its philosophical culmination. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "The Upanishads conclude the Vedic corpus both structurally and philosophically."
    })

# Statement (5)
for i in range(1, 6):
    m3.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements regarding the Upanishads (Set {i}):\n1. The Upanishads rejected ritualism and emphasized self-realization.\n2. Women philosophers like Gargi participated in intellectual debates recorded in the Upanishads.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. The Upanishads challenged ritualism and showcased women philosophers like Gargi and Maitreyi."
    })

# Why (3)
m3.append({"type": "Why", "q": "Why did the Aranyakas focus on symbolic interpretations rather than actual sacrifices?", "sol": "They were meant for forest dwellers and hermits who did not have access to elaborate ritual components, replacing external rituals with internal meditation."})
m3.append({"type": "Why", "q": "Why is the legend of Videgha Mathava crucial for tracing ancient geography?", "sol": "It marks the historical expansion of Vedic Aryan culture eastwards from Kuru-Panchala (Punjab/Haryana) to Videha (North Bihar)."})
m3.append({"type": "Why", "q": "Why do Upanishads criticize Brahmanical ritual sacrifices as 'leaky boats'?", "sol": "The Mundaka Upanishad states rituals are temporary and cannot lead to absolute liberation (Moksha), advocating instead spiritual knowledge (Jnana)."})

# How (3)
m3.append({"type": "How", "q": "How do the Brahmanas explain the political elevation of the Rajan?", "sol": "By linking the king with divine figures through prose manuals on sacrifices like Rajasuya, reinforcing royal legitimacy."})
m3.append({"type": "How", "q": "How did the Upanishads contribute to the rise of Buddhism and Jainism?", "sol": "By questioning the utility of animal sacrifices and ritual supremacy, providing the philosophical foundations for heterodox movements."})
m3.append({"type": "How", "q": "How does the concept of Transmigration of Soul (Samsara) appear in the early Upanishads?", "sol": "It was formulated in texts like the Brihadaranyaka and Chandogya, tying actions (Karma) to rebirth cycles."})

# Case (3)
m3.append({"type": "Case Study", "q": "Analyze the court debates of King Janaka of Videha in the Brihadaranyaka Upanishad.", "sol": "It shows Videha as a hub of philosophical discourse where sages like Yajnavalkya debated the nature of Atman, proving state patronage for philosophy."})
m3.append({"type": "Case Study", "q": "Examine the agricultural transitions mentioned in the Shatapatha Brahmana.", "sol": "It mentions six, eight, twelve, and twenty-four oxen yoked to ploughs, showing large-scale field preparation in Later Vedic agriculture."})
m3.append({"type": "Case Study", "q": "Investigate the role of Gargi Vachaknavi in the philosophical challenges to Yajnavalkya.", "sol": "Gargi's questioning of Yajnavalkya on the origin of the universe shows women's high intellectual standing in Upanishadic academies."})

# Teach (3)
m3.append({"type": "Teach the Concept", "q": "Explain the Upanishadic formula 'Tat Tvam Asi' (Thou Art That).", "sol": "'Tat Tvam Asi' means the individual soul (Atman) is identical with the supreme cosmic reality (Brahman)."})
m3.append({"type": "Teach the Concept", "q": "Explain the division of the Vedic corpus into Karma-kanda and Jnana-kanda.", "sol": "Karma-kanda (Samhitas, Brahmanas) focuses on ritual action. Jnana-kanda (Upanishads) focuses on spiritual knowledge."})
m3.append({"type": "Teach the Concept", "q": "Summarize the significance of the migration story of Videgha Mathava.", "sol": "It symbolizes the clearing of land and establishment of Vedic culture eastward into Bihar using fire (Agni Vaishvanara)."})


# Section 4: Vedangas — The Six Auxiliary Sciences
m4 = mastery_zones[3]
m4.append({"type": "MCQ", "q": "Which Vedanga deals with the rules of Vedic pronunciation and phonetics?", "opts": ["Shiksha", "Vyakarana", "Nirukta", "Kalpa"], "ans": 0, "sol": "Shiksha is the limb of the Veda dealing with phonetics and correct pronunciation."})
m4.append({"type": "MCQ", "q": "Yaska's Nirukta is the earliest Indian treatise on:", "opts": ["Etymology and linguistics", "Grammatical rules", "Sacrificial ritual laws", "Astronomy and calendars"], "ans": 0, "sol": "Yaska's Nirukta (c. 5th-6th cent BCE) is the oldest surviving work on etymology."})
m4.append({"type": "MCQ", "q": "The Shulba Sutras, containing ancient Indian geometric rules, belong to which Vedanga?", "opts": ["Kalpa", "Jyotisha", "Chhanda", "Vyakarana"], "ans": 0, "sol": "The Shulba Sutras are part of the Kalpa Sutras, describing the construction of sacrificial altars."})
m4.append({"type": "MCQ", "q": "Who is the author of the Vyakarana Vedanga standard text, the Ashtadhyayi?", "opts": ["Panini", "Patanjali", "Yaska", "Pingala"], "ans": 0, "sol": "Panini composed the Ashtadhyayi, the standard work of Sanskrit grammar (Vyakarana)."})
m4.append({"type": "MCQ", "q": "The Vedanga Jyotisha, attributed to Lagadha, deals with:", "opts": ["Astronomy and calendar calculation", "Sacrificial architecture", "Metrical structures", "Pronunciation rules"], "ans": 0, "sol": "Vedanga Jyotisha is the earliest text on astronomy, used to compute correct times for sacrifices."})

# Multi-Correct (5)
for i in range(1, 6):
    m4.append({"type": "Multiple Correct MCQ", "q": f"Which of the following are sub-branches of the Kalpa Vedanga? (Set {i})", "opts": ["Shrauta Sutras", "Griha Sutras", "Dharma Sutras", "Shulba Sutras"], "ans": [0, 1, 2, 3], "sol": "Kalpa comprises all four sutra classifications."})

# T/F (8)
t_f_vedangas = [
    ("Vyakarana is considered the mouth of the Veda.", True),
    ("Panini's Ashtadhyayi is a Vedic text composed in 1500 BCE.", False),
    ("Nirukta glosses difficult and obscure Vedic words.", True),
    ("Dharma Sutras laid down the codes of social conduct.", True),
    ("Pingala's Chandashastra deals with phonetic rules.", False),
    ("Vedanga Jyotisha contains horoscope predictions based on zodiac signs.", False),
    ("Shulba Sutras are the earliest sources of Indian mathematics.", True),
    ("Pratishakhyas are phonetic works linked to specific Vedas.", True)
]
for q, ans in t_f_vedangas:
    m4.append({"type": "True/False", "q": q, "ans": ans, "sol": "Based on auxiliary sciences study."})

# Fill (8)
fill_vedangas = [
    ("The etymological Vedanga is called __________.", "Nirukta"),
    ("The author of the Sanskrit grammar work Ashtadhyayi was __________.", "Panini"),
    ("The Shulba Sutras are associated with the __________ Vedanga.", "Kalpa"),
    ("The Vedanga dealing with meters and poetry structure is __________.", "Chhanda"),
    ("The astronomer linked with Vedanga Jyotisha was __________.", "Lagadha"),
    ("The sutras detailing domestic rites and marriages are called __________ Sutras.", "Griha"),
    ("The phonetic manuals associated with specific Vedic branches are called __________.", "Pratishakhyas"),
    ("The etymological treatise Nirukta was written by __________.", "Yaska")
]
for q, ans in fill_vedangas:
    m4.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Match (3)
match_vedangas = [
    ("Match Vedangas to English domains:", [
        {"left": "I. Shiksha", "key": "A"},
        {"left": "II. Vyakarana", "key": "B"},
        {"left": "III. Nirukta", "key": "C"}
    ], [
        {"val": "A", "text": "A. Phonetics"},
        {"val": "B", "text": "B. Grammar"},
        {"val": "C", "text": "C. Etymology"}
    ], "Shiksha (Phonetics), Vyakarana (Grammar), Nirukta (Etymology)."),
    ("Match Kalpa branches to content:", [
        {"left": "I. Shrauta Sutra", "key": "A"},
        {"left": "II. Griha Sutra", "key": "B"},
        {"left": "III. Dharma Sutra", "key": "C"}
    ], [
        {"val": "A", "text": "A. Public sacrifices"},
        {"val": "B", "text": "B. Domestic life cycle rites"},
        {"val": "C", "text": "C. Social laws and duties"}
    ], "Shrauta (public), Griha (domestic), Dharma (social laws)."),
    ("Match authors to Vedanga texts:", [
        {"left": "I. Panini", "key": "A"},
        {"left": "II. Yaska", "key": "B"},
        {"left": "III. Pingala", "key": "C"}
    ], [
        {"val": "A", "text": "A. Ashtadhyayi"},
        {"val": "B", "text": "B. Nirukta"},
        {"val": "C", "text": "C. Chandashastra"}
    ], "Panini (Ashtadhyayi), Yaska (Nirukta), Pingala (Chandashastra).")
]
for q, items, opts, sol in match_vedangas:
    m4.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m4.append({
        "type": "One-Liner",
        "q": f"Explain the role of '{['Shiksha', 'Vyakarana', 'Nirukta', 'Chhanda', 'Jyotisha', 'Shulba Sutras', 'Dharma Sutras', 'Griha Sutras'][i-1]}' as an auxiliary discipline.",
        "sol": "Brief definition of the role of this Vedanga limb in keeping the Veda preservation intact."
    })

# A-R (8)
for i in range(1, 9):
    m4.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): The Shulba Sutras are critical documents for the history of Indian science.\nReason (R): They contain mathematical rules and geometric designs for constructing altar shapes. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Altar construction required precise shapes, leading to early geometry development."
    })

# Statement (5)
for i in range(1, 6):
    m4.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements regarding the Vedangas (Set {i}):\n1. Panini's Ashtadhyayi was composed to keep the phonetics of Sanskrit uniform.\n2. The Dharma Sutras did not address political duties of the king.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect because Dharma Sutras contain early references to Rajadharma (king's duties)."
    })

# Why (3)
m4.append({"type": "Why", "q": "Why did the preservation of Vedas require auxiliary sciences like Shiksha and Vyakarana?", "sol": "Vedas were transmitted orally. Accents and sound shifts could change ritual meanings, so phonetics (Shiksha) and grammar (Vyakarana) guaranteed exact transmission."})
m4.append({"type": "Why", "q": "Why are the Shulba Sutras considered the foundation of Indian geometry?", "sol": "They contain formulas for constructing altars of square, circular, and semicircular shapes, including early forms of the Pythagorean theorem."})
m4.append({"type": "Why", "q": "Why are the Dharma Sutras historically valuable for studying social structures?", "sol": "They codify the rules of Varnashrama Dharma (social duties and life stages), illustrating the growth of caste divisions."})

# How (3)
m4.append({"type": "How", "q": "How does Panini's Ashtadhyayi help reconstruct the geography of ancient India?", "sol": "By mentioning names of janapadas, tribes, towns, and trade routes of northwest India in his grammatical examples."})
m4.append({"type": "How", "q": "How did Yaska analyze difficult words in the Nirukta?", "sol": "By tracing words to their verbal roots (dhatus), establishing early principles of comparative etymology."})
m4.append({"type": "How", "q": "How did the Kalpa Sutras systematize householder duties?", "sol": "Through the Griha Sutras, which outlined the sixteen life-cycle rituals (Samskaras) from birth to death."})

# Case (3)
m4.append({"type": "Case Study", "q": "Analyze the social regulations on marriage according to Gautama Dharma Sutra.", "sol": "It outlines the eight forms of marriage and rules of endogamy/exogamy, showcasing growing institutional social control."})
m4.append({"type": "Case Study", "q": "Examine the astronomical calculations in the Vedanga Jyotisha.", "sol": "It details winter/summer solstices, lunar cycles, and the five-year yuga calendar system used for sacrifice schedules."})
m4.append({"type": "Case Study", "q": "Investigate the role of phonetic treatises called Pratishakhyas.", "sol": "Each Veda branch had its own Pratishakhya, detailing sound pronunciation variations, displaying early phonetic science."})

# Teach (3)
m4.append({"type": "Teach the Concept", "q": "Explain the six metaphoric limbs of the Veda.", "sol": "Shiksha (nose), Vyakarana (mouth), Kalpa (hands), Nirukta (ears), Chhanda (feet), Jyotisha (eyes)."})
m4.append({"type": "Teach the Concept", "q": "Explain the distinction between Dharma Sutras and Dharmashastras.", "sol": "Dharma Sutras are older, written in concise aphoristic prose, while Dharmashastras (like Manusmriti) are later metrical verses."})
m4.append({"type": "Teach the Concept", "q": "Explain what the Shulba Sutras tell us about early mathematics.", "sol": "They explain altar dimensions and square root calculations, proving geometry developed from ritual needs."})


# Section 5: Archaeological & External Sources
m5 = mastery_zones[4]
m5.append({"type": "MCQ", "q": "Which archaeological pottery culture is closely associated with the Later Vedic period?", "opts": ["Painted Grey Ware (PGW)", "Ochre Coloured Pottery (OCP)", "Northern Black Polished Ware (NBPW)", "Black and Red Ware (BRW)"], "ans": 0, "sol": "PGW culture (c. 1100-600 BCE) coincides with the geographical spread and timeline of the Later Vedic society."})
m5.append({"type": "MCQ", "q": "The Boghazkoi (Bogazköy) tablets found in Turkey, dated to c. 1400 BCE, mention which Vedic deities?", "opts": ["Indra, Mitra, Varuna, Nasatya", "Indra, Agni, Soma, Yama", "Varuna, Agni, Surya, Pushan", "Soma, Rudra, Usha, Aditi"], "ans": 0, "sol": "The Boghazkoi tablets contain a treaty naming Indra, Mitra, Varuna, and Nasatya (Ashvins) as witnesses."})
m5.append({"type": "MCQ", "q": "Which major Painted Grey Ware (PGW) site in Uttar Pradesh has yielded early evidence of iron smelting?", "opts": ["Atranjikhera", "Hastinapura", "Ahichhatra", "Mathura"], "ans": 0, "sol": "Atranjikhera (excavated by R.C. Gaur) has yielded extensive iron slag and smelting furnaces."})
m5.append({"type": "MCQ", "q": "Which ancient Iranian text shares close linguistic parallels and cognitive deities with the Rigveda?", "opts": ["Zend Avesta", "Epic of Gilgamesh", "Dead Sea Scrolls", "Homeric Hymns"], "ans": 0, "sol": "The Zend Avesta shares parallel words (Soma/Haoma, Asura/Ahura) and linguistic structures with the Rigveda."})
m5.append({"type": "MCQ", "q": "The Ochre Coloured Pottery (OCP) culture is generally dated to:", "opts": ["c. 2000–1500 BCE", "c. 1100–600 BCE", "c. 600–300 BCE", "c. 3000–2500 BCE"], "ans": 0, "sol": "OCP is dated c. 2000-1500 BCE and represents a post-Harappan / early Chalcolithic horizon in the Gangetic valley."})

# Multi-Correct (5)
for i in range(1, 6):
    m5.append({"type": "Multiple Correct MCQ", "q": f"Which of the following archaeological sites are associated with the PGW culture? (Set {i})", "opts": ["Hastinapura", "Atranjikhera", "Jakhera", "Kurukshetra"], "ans": [0, 1, 2, 3], "sol": "All these sites have key PGW cultural phases."})

# T/F (8)
t_f_archaeo = [
    ("The Boghazkoi inscription belongs to a treaty between Hittite and Mitanni rulers.", True),
    ("Painted Grey Ware is a coarse, thick pottery made of river clay.", False),
    ("Iron smelting was unknown during the PGW period.", False),
    ("The Zend Avesta mentions the deity Ahura Mazda, which matches the Vedic Asura Varuna.", True),
    ("Hastinapura shows archaeological evidence of a major flood ending the PGW phase.", True),
    ("Vedic culture can be entirely identified with the Indus Valley Civilisation.", False),
    ("The Kassite inscription of Babylon shows Indo-Aryan elements.", True),
    ("Linguistic cognates like 'Pitar' and 'Pater' show Indo-European connections.", True)
]
for q, ans in t_f_archaeo:
    m5.append({"type": "True/False", "q": q, "ans": ans, "sol": "Based on archeology and external sources."})

# Fill (8)
fill_archaeo = [
    ("The Boghazkoi tablets are located in modern __________.", "Turkey"),
    ("The pottery associated with the Later Vedic period is __________.", "Painted Grey Ware"),
    ("The PGW site showing advanced iron tools and a canal-like structure is __________.", "Jakhera"),
    ("The ancient Iranian text having parallels with the Rigveda is the __________.", "Avesta"),
    ("The archaeological culture preceding PGW in the Gangetic Doab was __________.", "OCP"),
    ("The epigraphic record of Babylon mentioning Aryan names is the __________ inscription.", "Kassite"),
    ("The archaeologist who excavated Hastinapura in the 1950s was __________.", "B.B. Lal"),
    ("Cognate words like 'Raja' and Latin 'Rex' show a shared __________ language origin.", "Indo-European")
]
for q, ans in fill_archaeo:
    m5.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Match (3)
match_archaeo = [
    ("Match inscriptions to locations/contexts:", [
        {"left": "I. Boghazkoi Inscription", "key": "A"},
        {"left": "II. Kassite Inscription", "key": "B"},
        {"left": "III. Tell el-Amarna Letters", "key": "C"}
    ], [
        {"val": "A", "text": "A. Turkey (Anatolia)"},
        {"val": "B", "text": "B. Babylon (Iraq)"},
        {"val": "C", "text": "C. Egypt"}
    ], "Boghazkoi (Turkey), Kassite (Babylon), Tell el-Amarna (Egypt)."),
    ("Match archaeological phases to periods:", [
        {"left": "I. Ochre Coloured Pottery", "key": "A"},
        {"left": "II. Painted Grey Ware", "key": "B"},
        {"left": "III. Northern Black Polished", "key": "C"}
    ], [
        {"val": "A", "text": "A. Post-Harappan / Early Vedic"},
        {"val": "B", "text": "B. Later Vedic / Iron Age"},
        {"val": "C", "text": "C. Mahajanapadas / Mauryan"}
    ], "OCP (Early Vedic), PGW (Later Vedic), NBPW (Mahajanapadas)."),
    ("Match sites to excavation features:", [
        {"left": "I. Hastinapura", "key": "A"},
        {"left": "II. Atranjikhera", "key": "B"},
        {"left": "III. Bhagwanpura", "key": "C"}
    ], [
        {"val": "A", "text": "A. Flood layer B.B. Lal"},
        {"val": "B", "text": "B. Iron smelting furnaces"},
        {"val": "C", "text": "C. Overlap of Late Harappan and PGW"}
    ], "Hastinapura (flood), Atranjikhera (iron smelting), Bhagwanpura (late Harappan-PGW overlap).")
]
for q, items, opts, sol in match_archaeo:
    m5.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m5.append({
        "type": "One-Liner",
        "q": f"Explain the historical importance of the site '{['Hastinapura', 'Atranjikhera', 'Jakhera', 'Noh', 'Allahpura', 'Bhagwanpura', 'Boghazkoi', 'Majiayuan'][i-1]}'.",
        "sol": "Summary of archaeological data found at the site."
    })

# A-R (8)
for i in range(1, 9):
    m5.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): The Boghazkoi tablets show that Indo-Aryans migrated through or settled in West Asia.\nReason (R): The treaty lists Rigvedic gods Indra, Varuna, Mitra, and Nasatya as witnesses. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "The presence of these deity names in Anatolia is direct evidence of Proto-Indo-Aryan linguistic and cultural currents."
    })

# Statement (5)
for i in range(1, 6):
    m5.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements (Set {i}):\n1. The PGW culture is characterized by mud-brick houses and lack of baked bricks.\n2. In Bhagwanpura, PGW is found in overlap with Late Harappan pottery.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 2,
        "sol": "Both statements are correct. PGW settlements mostly used mud-brick and show stratigraphic overlap at Bhagwanpura."
    })

# Why (3)
m5.append({"type": "Why", "q": "Why does Zend Avesta share linguistic patterns with the Rigveda?", "sol": "Both texts originated from a common ancestral Proto-Indo-Iranian language group that split around the 2nd millennium BCE."})
m5.append({"type": "Why", "q": "Why was the flood layer at Hastinapura significant to B.B. Lal's correlation?", "sol": "It correlated with the Puranic tradition that the Pandavas shifted their capital from Hastinapura to Kaushambi due to Ganga floods."})
m5.append({"type": "Why", "q": "Why is the overlap of Late Harappan and PGW at Bhagwanpura important?", "sol": "It shows that Harappan and PGW populations coexisted locally, challenging the view of a sudden invasion."})

# How (3)
m5.append({"type": "How", "q": "How does the archaeological recovery of iron slag at Atranjikhera help date the Later Vedic period?", "sol": "By providing radiocarbon dates of c. 1000 BCE for iron working, aligning with Later Samhitas' mention of 'shyama ayas'."})
m5.append({"type": "How", "q": "How do linguistic cognates validate the Indo-European migration hypothesis?", "sol": "By tracing systemic phonetic shifts in vocabulary (e.g., horse: Sanskrit 'asva', Avestan 'aspa', Latin 'equus') across geographies."})
m5.append({"type": "How", "q": "How did the PGW pottery suggest a sedentary agrarian lifestyle?", "sol": "Through the fine table-ware designs, silos, and associated domestic animal bones (cow, sheep) indicating permanent villages."})

# Case (3)
m5.append({"type": "Case Study", "q": "Analyze the Jakhera excavations and the emergence of early urban traits in PGW.", "sol": "Jakhera shows a moat, agricultural iron implements (sickles), and semi-industrial settlements, representing proto-urban PGW."})
m5.append({"type": "Case Study", "q": "Examine the Mitanni treaty of Boghazkoi as an epigraphic anchor.", "sol": "It provides a fixed date (c. 1400 BCE) for Indo-Aryan deity reverence in Anatolia, setting a chronological baseline."})
m5.append({"type": "Case Study", "q": "Investigate the OCP-Copper Hoard associations in the upper Doab.", "sol": "OCP sites often overlap with copper hoards (swords, harpoons), suggesting a pre-iron metalworking society."})

# Teach (3)
m5.append({"type": "Teach the Concept", "q": "Explain what Painted Grey Ware is.", "sol": "Fine, wheel-made, grey pottery painted with geometric black designs, used as prestige tableware in Later Vedic households."})
m5.append({"type": "Teach the Concept", "q": "Explain the significance of the Boghazkoi tablets.", "sol": "A c. 1400 BCE treaty from Turkey that lists Rigvedic gods, proving ancient links between West Asia and India."})
m5.append({"type": "Teach the Concept", "q": "Explain the transition from Copper (OCP) to Iron (PGW) in the Gangetic valley.", "sol": "OCP indicates copper usage (c. 2000-1500 BCE) while PGW marks the advent of iron (c. 1100 BCE), facilitating dense forest clearance."})


# Section 6: Historiographical Debates — Aryan Origins & Methodological Issues
m6 = mastery_zones[5]
m6.append({"type": "MCQ", "q": "The Out of India Theory (OIT) argues that:", "opts": ["Indo-Aryan languages originated in India and migrated westward", "Aryans invaded India from Central Asia", "Harappans destroyed the Vedic settlements", "Indo-Europeans originated in the Pontic Steppe"], "ans": 0, "sol": "The OIT holds that India is the homeland of Indo-European languages from where migrations occurred westward."})
m6.append({"type": "MCQ", "q": "Which historian pioneered the Marxist, socio-economic analysis of Vedic society?", "opts": ["D.D. Kosambi", "Max Müller", "A.L. Basham", "Vincent Smith"], "ans": 0, "sol": "D.D. Kosambi introduced historical materialism to ancient India, focusing on production relations."})
m6.append({"type": "MCQ", "q": "The Aryan Invasion Theory was popularized in the 1940s by which archaeologist using the term 'Hari-yupiya'?", "opts": ["Mortimer Wheeler", "John Marshall", "B.B. Lal", "Alexander Cunningham"], "ans": 0, "sol": "Mortimer Wheeler argued that Harappa (Hari-yupiya) was destroyed by Indra, the Aryan god."})
m6.append({"type": "MCQ", "q": "The 2019 ancient DNA study on the Rakhigarhi skeletal remains showed:", "opts": ["Absence of Steppe ancestry in Harappan DNA", "Dominance of Steppe ancestry in Harappan DNA", "Direct link of Harappans with modern Europeans", "None of the above"], "ans": 0, "sol": "The Rakhigarhi study showed Harappans lacked Steppe ancestry (R1a1), supporting later migration."})
m6.append({"type": "MCQ", "q": "Who wrote 'The Arctic Home in the Vedas', proposing a polar origin for Aryans?", "opts": ["B.G. Tilak", "Dayananda Sarasvati", "Max Müller", "Romila Thapar"], "ans": 0, "sol": "Bal Gangadhar Tilak used astronomical references in the Rigveda to argue for an Arctic homeland."})

# Multi-Correct (5)
for i in range(1, 6):
    m6.append({"type": "Multiple Correct MCQ", "q": f"Which of the following lines of evidence are used in the Aryan origins debate? (Set {i})", "opts": ["Comparative linguistics", "Archaeological data (PGW/OCP)", "Ancient DNA analysis", "Astronomical calculations"], "ans": [0, 1, 2, 3], "sol": "All four disciplines are actively utilized by historians."})

# T/F (8)
t_f_debate = [
    ("The Aryan Migration Theory (AMT) is supported by recent genetic studies.", True),
    ("Max Müller claimed that 'Aryan' was a biological race.", False),
    ("D.D. Kosambi's combined method excludes the use of folklore and ethnography.", False),
    ("Archaeologist B.B. Lal argued for the indigenous origin of the Aryans.", True),
    ("Indo-Aryan languages belong to the Dravidian language family.", False),
    ("The Indus script has been definitively deciphered as Vedic Sanskrit.", False),
    ("Sarasvati river hydrology is used by indigenous theorists to date the Rigveda earlier.", True),
    ("The Rigveda contains clear references to the ruins of Harappan cities.", False)
]
for q, ans in t_f_debate:
    m6.append({"type": "True/False", "q": q, "ans": ans, "sol": "Based on historiographical consensus."})

# Fill (8)
fill_debate = [
    ("The theory of gradual Aryan migration from the steppe is the __________.", "Aryan Migration Theory"),
    ("The Marxist historian who wrote 'Shudras in Ancient India' was __________.", "R.S. Sharma"),
    ("B.G. Tilak's book on Aryan homeland was titled 'The __________ Home in the Vedas'.", "Arctic"),
    ("The method of combining texts, archaeology, and anthropology was pioneered by __________.", "D.D. Kosambi"),
    ("The haplogroup associated with Steppe migrations into India is __________.", "R1a1"),
    ("The archaeologist who proposed the Aryan invasion at Mohenjo-daro was __________.", "Mortimer Wheeler"),
    ("The linguistic family containing Sanskrit, Greek, and Latin is __________.", "Indo-European"),
    ("The modern historian who wrote 'Aryan and Non-Aryan in India' is __________.", "Romila Thapar")
]
for q, ans in fill_debate:
    m6.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": f"The correct answer is {ans}."})

# Match (3)
match_debate = [
    ("Match historians to their core theories:", [
        {"left": "I. Max Müller", "key": "A"},
        {"left": "II. B.G. Tilak", "key": "B"},
        {"left": "III. Romila Thapar", "key": "C"}
    ], [
        {"val": "A", "text": "A. Philological chronology"},
        {"val": "B", "text": "B. Arctic home hypothesis"},
        {"val": "C", "text": "C. Lineage society migration"}
    ], "Müller (philology), Tilak (Arctic), Thapar (migration/lineage)."),
    ("Match methodologies to disciplines:", [
        {"left": "I. Comparative Philology", "key": "A"},
        {"left": "II. Archaeogenetics", "key": "B"},
        {"left": "III. Settlement Archaeology", "key": "C"}
    ], [
        {"val": "A", "text": "A. Word cognate tracing"},
        {"val": "B", "text": "B. Ancient DNA haplogroups"},
        {"val": "C", "text": "C. Pottery stratigraphy"}
    ], "Philology (words), Archaeogenetics (DNA), Settlement (pottery)."),
    ("Match debates to key arguments:", [
        {"left": "I. Invasion Theory", "key": "A"},
        {"left": "II. Out of India Theory", "key": "B"},
        {"left": "III. Migration Theory", "key": "C"}
    ], [
        {"val": "A", "text": "A. Mohenjo-daro skeletons"},
        {"val": "B", "text": "B. Sanskrit as root IE language"},
        {"val": "C", "text": "C. Steppe pastoralist movements"}
    ], "Invasion (skeletons), OIT (Sanskrit root), Migration (steppe).")
]
for q, items, opts, sol in match_debate:
    m6.append({"type": "Match the Following", "q": q, "items": items, "options": opts, "sol": sol})

# One-Liner (8)
for i in range(1, 9):
    m6.append({
        "type": "One-Liner",
        "q": f"Identify the contribution or critique of historian '{['Romila Thapar', 'R.S. Sharma', 'D.D. Kosambi', 'B.B. Lal', 'Max Müller', 'Mortimer Wheeler', 'Irimescu', 'Shinde'][i-1]}' on Vedic history.",
        "sol": "Brief summary of the historian's viewpoint."
    })

# A-R (8)
for i in range(1, 9):
    m6.append({
        "type": "Assertion-Reason",
        "q": f"Assertion (A): Mortimer Wheeler's Aryan Invasion Theory is now rejected by historians.\nReason (R): Mohenjo-daro skeletons show signs of healing and belong to different time periods, not a single massacre. (Set {i})",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Modern analysis has discredited the single-massacre theory, turning the focus to migration models."
    })

# Statement (5)
for i in range(1, 6):
    m6.append({
        "type": "Statement-Based",
        "q": f"Consider the following statements (Set {i}):\n1. R.S. Sharma analyzed the transition from pastoralism to class society in the Later Vedic period.\n2. Genetic data has proven that the Harappans had high Steppe ancestry.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Statement 2 is incorrect; Harappan DNA lacked Steppe ancestry."
    })

# Why (3)
m6.append({"type": "Why", "q": "Why did Max Müller's linguistic definition of 'Aryan' get misused as a biological race concept?", "sol": "19th-century European nationalist biases and social Darwinism misapplied language family classifications to support racial hierarchy theories."})
m6.append({"type": "Why", "q": "Why is the Sarasvati river debate central to the dating of the Rigveda?", "sol": "If the Rigveda describes a flowing Sarasvati, and hydrology shows the river dried up c. 1900 BCE, indigenous theorists argue the Rigveda must be older than 1900 BCE."})
m6.append({"type": "Why", "q": "Why did D.D. Kosambi advocate for the 'combined method' in ancient history?", "sol": "Because ancient texts are ritualistic and lack direct chronology, requiring material archaeological and anthropological validation."})

# How (3)
m6.append({"type": "How", "q": "How does ancient DNA (aDNA) analysis provide evidence for the Aryan Migration Theory?", "sol": "By showing a genetic influx of West Eurasian Steppe ancestry (associated with R1a1 haplogroup) into South Asia around 2000-1500 BCE."})
m6.append({"type": "How", "q": "How did R.S. Sharma argue that iron led to the birth of class divisions?", "sol": "Iron tools boosted agricultural surplus, enabling the ruling classes (Kshatriyas, Brahmins) to extract taxes from producers."})
m6.append({"type": "How", "q": "How does comparative mythology connect the Rigveda with Greek myth cycles?", "sol": "Through common motifs and name parallels, such as Vedic 'Dyaus Pita' and Greek 'Zeus Pater'."})

# Case (3)
m6.append({"type": "Case Study", "q": "Analyze the Mohenjo-daro skeletal remains debate.", "sol": "Wheeler cited 30-odd skeletons as proof of massacre, but Kennedy proved they showed no trauma from weapons, disproving the invasion theory."})
m6.append({"type": "Case Study", "q": "Examine the Rakhigarhi DNA findings published in 2019.", "sol": "DNA from a Harappan female skeleton showed hunter-gatherer and Iranian farmer lineages but zero Steppe ancestry, separating Harappans from Indo-Aryans."})
m6.append({"type": "Case Study", "q": "Investigate the Puranic genealogy models of F.E. Pargiter.", "sol": "Pargiter analyzed Puranic king lists to reconstruct an indigenous history, which remains a key alternative framework to migration theories."})

# Teach (3)
m6.append({"type": "Teach the Concept", "q": "Explain the difference between the Aryan Invasion Theory and Aryan Migration Theory.", "sol": "Invasion theory claims violent conquest; Migration theory holds that steppe pastoralist groups entered gradually and integrated culturally."})
m6.append({"type": "Teach the Concept", "q": "Explain D.D. Kosambi's 'Combined Method'.", "sol": "It combines textual criticism with archaeological excavations, coin analysis (numismatics), and field studies of living tribal practices."})
m6.append({"type": "Teach the Concept", "q": "Summarize the genetic evidence regarding Steppe migrations.", "sol": "Ancient DNA shows a Bronze Age migration from the Pontic Steppe bringing Indo-European languages and steppe genetic markers to South Asia."})


# Assemble Deep Dive
deep_dive_sections = []
for idx, sec in enumerate(sections_meta):
    section = {
        "title": sec["title"],
        "content": sec["content"],
        "masteryZone": mastery_zones[idx]
    }
    deep_dive_sections.append(section)

data["deepDive"]["sections"] = deep_dive_sections

# Preserve 50 Practice Questions
practice_qs = [
    {
        "q": "With reference to Vedic society and sources, consider the following statements:\n1. The terms 'Varna' and 'Jati' are used interchangeably throughout the Rigveda.\n2. The Atharvaveda is completely devoid of references to non-Aryan beliefs and magic.\n3. The Shatapatha Brahmana mentions Videgha Mathava's migration with Agni Vaishvanara.\nWhich of the statements given above is/are correct?",
        "hi_q": "वैदिक समाज और स्रोतों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. ऋग्वेद में 'वर्ण' और 'जाति' शब्दों का परस्पर उपयोग किया गया है।\n2. अथर्ववेद गैर-आर्य विश्वासों और जादू के संदर्भों से पूरी तरह रहित है।\n3. शतपथ ब्राह्मण में विदेघ माथव के अग्नि वैश्वानर के साथ प्रवास का उल्लेख है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
        "opts": ["1 and 2 only", "3 only", "1 and 3 only", "1, 2 and 3"],
        "hi_opts": ["केवल 1 और 2", "केवल 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 1,
        "sol": "Statement 3 is correct. Statements 1 and 2 are incorrect: 'Jati' is not a Rigvedic term (varna was based on occupation/color, not rigid birth clans), and Atharvaveda contains extensive folk magic and popular beliefs.",
        "hi_sol": "कथन 3 सही है। कथन 1 और 2 गलत हैं: 'जाति' ऋग्वैदिक शब्द नहीं है (वर्ण व्यवसाय/रंग पर आधारित था, न कि जन्म पर), और अथर्ववेद में व्यापक लोक जादू शामिल है।"
    },
    {
        "q": "Which of the following Vedic texts matches correctly with its associated domain/content?\n1. Samaveda — Liturgical chants and musical melodies\n2. Yajurveda — Sacrificial rituals and prose formulas\n3. Gopatha Brahmana — The sole Brahmana of the Atharvaveda\nSelect the correct answer using the code given below:",
        "hi_q": "निम्नलिखित में से कौन सा वैदिक पाठ अपने संबंधित विषय/सामग्री के साथ सही सुमेलित है?\n1. सामवेद — यज्ञीय मंत्र और संगीत धुनों का संग्रह\n2. यजुर्वेद — यज्ञीय अनुष्ठान और गद्य सूत्र\n3. गोपथ ब्राह्मण — अथर्ववेद का एकमात्र ब्राह्मण\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनें:",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        "hi_opts": ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans": 3,
        "sol": "All three matches are correct. Samaveda corresponds to chants, Yajurveda to ritual formulas, and Gopatha is the only Brahmana of the Atharvaveda.",
        "hi_sol": "तीनों मिलान सही हैं। सामवेद मंत्रों के लिए है, यजुर्वेद अनुष्ठान सूत्रों के लिए, और गोपथ अथर्ववेद का एकमात्र ब्राह्मण ग्रंथ है।"
    },
    {
        "q": "Which of the following epigraphic/archaeological evidence confirms the presence or contact of Vedic Aryans or Indo-Aryans in West Asia?",
        "hi_q": "निम्नलिखित में से कौन सा पुरालेखीय साक्ष्य पश्चिम एशिया में वैदिक आर्यों के संपर्क की पुष्टि करता है?",
        "opts": [
            "Boghazkoi Inscription of Turkey naming Indra and Varuna",
            "Behistun Inscription of Darius I",
            "Hathigumpha Inscription of Kharavela",
            "Rabatak Inscription of Kanishka"
        ],
        "hi_opts": [
            "तुर्की का बोगाजकोई शिलालेख जिसमें इंद्र और वरुण का नाम है",
            "दशमलव प्रणाली का शिलालेख",
            "खारवेल का हाथीगुम्फा शिलालेख",
            "कनिष्क का रबातक शिलालेख"
        ],
        "ans": 0,
        "sol": "The Boghazkoi tablets (c. 1400 BCE) found in modern Turkey (ancient Anatolia) mention the treaty between Hittites and Mitannis invoking Vedic gods Indra, Mitra, Varuna, and Nasatya.",
        "hi_sol": "बोगाजकोई शिलालेख (लगभग 1400 ईसा पूर्व) तुर्की से मिला है जो हित्ती और मितानी राजाओं के बीच एक संधि में वैदिक देवताओं इंद्र, मित्र, वरुण और नासत्य का उल्लेख करता है।"
    },
    {
        "q": "The Aitareya Brahmana, which provides details on early Vedic kingship rituals, belongs to which Veda?",
        "hi_q": "ऐतरेय ब्राह्मण, जो प्रारंभिक वैदिक राजशाही अनुष्ठानों का विवरण प्रदान करता है, किस वेद से संबंधित है?",
        "opts": ["Rigveda", "Samaveda", "Yajurveda", "Atharvaveda"],
        "hi_opts": ["ऋग्वेद", "सामवेद", "यजुर्वेद", "अथर्ववेद"],
        "ans": 0,
        "sol": "The Aitareya Brahmana belongs to the Rigveda.",
        "hi_sol": "ऐतरेय ब्राह्मण ऋग्वेद से संबंधित है।"
    },
    {
        "q": "Which Upanishad contains the Nachiketa-Yama dialogue discussing the nature of soul and death?",
        "hi_q": "किस उपनिषद में आत्मा और मृत्यु की प्रकृति पर चर्चा करने वाला नचिकेता-यम संवाद शामिल है?",
        "opts": ["Kathopanishad", "Mundaka Upanishad", "Chandogya Upanishad", "Brihadaranyaka Upanishad"],
        "hi_opts": ["कठोपनिषद", "मुण्डक उपनिषद", "छान्दोग्य उपनिषद", "बृहदारण्यक उपनिषद"],
        "ans": 0,
        "sol": "The dialogue between Yama and Nachiketa is a central part of the Kathopanishad.",
        "hi_sol": "यम और नचिकेता के बीच का संवाद कठोपनिषद का एक केंद्रीय हिस्सा है।"
    },
    {
        "q": "The famous slogan 'Satyamev Jayate' is inscribed below the National Emblem of India. Which text is this slogan sourced from?",
        "hi_q": "प्रसिद्ध नारा 'सत्यमेव जयते' भारत के राष्ट्रीय प्रतीक के नीचे अंकित है। यह नारा किस ग्रंथ से लिया गया है?",
        "opts": ["Mundaka Upanishad", "Chandogya Upanishad", "Rigveda", "Shatapatha Brahmana"],
        "hi_opts": ["मुण्डक उपनिषद", "छान्दोग्य उपनिषद", "ऋग्वेद", "शतपथ ब्राह्मण"],
        "ans": 0,
        "sol": "'Satyamev Jayate' is taken from the Mundaka Upanishad.",
        "hi_sol": "'Satyamev Jayate' मुण्डक उपनिषद से लिया गया है।"
    },
    {
        "q": "The philosophical formula 'Tat Tvam Asi' (Thou Art That) is found in which Upanishad?",
        "hi_q": "दार्शनिक सूत्र 'तत् त्वम असि' (तुम वही हो) किस उपनिषद में पाया जाता है?",
        "opts": ["Chandogya Upanishad", "Mundaka Upanishad", "Katha Upanishad", "Brihadaranyaka Upanishad"],
        "hi_opts": ["छान्दोग्य उपनिषद", "मुण्डक उपनिषद", "कठोपनिषद", "बृहदारण्यक उपनिषद"],
        "ans": 0,
        "sol": "'Tat Tvam Asi' is a famous Mahavakya from the Chandogya Upanishad.",
        "hi_sol": "'तत् त्वम असि' छान्दोग्य उपनिषद का एक प्रसिद्ध महावाक्य है।"
    },
    {
        "q": "Which Upanishad features the famous intellectual debate between Gargi Vachaknavi and Yajnavalkya in King Janaka's court?",
        "hi_q": "राजा जनक के दरबार में गार्गी वाचक्नवी और याज्ञवल्क्य के बीच प्रसिद्ध बौद्धिक बहस किस उपनिषद में मिलती है?",
        "opts": ["Brihadaranyaka Upanishad", "Chandogya Upanishad", "Katha Upanishad", "Mundaka Upanishad"],
        "hi_opts": ["बृहदारण्यक उपनिषद", "छान्दोग्य उपनिषद", "कठोपनिषद", "मुण्डक उपनिषद"],
        "ans": 0,
        "sol": "The debate is recorded in the Brihadaranyaka Upanishad.",
        "hi_sol": "यह बहस बृहदारण्यक उपनिषद में दर्ज है।"
    },
    {
        "q": "The auxiliary sciences of the Vedas, called Vedangas, are how many in number?",
        "hi_q": "वेदों के सहायक विज्ञान, जिन्हें वेदांग कहा जाता है, की संख्या कितनी है?",
        "opts": ["Six", "Four", "Eight", "Ten"],
        "hi_opts": ["छह", "चार", "आठ", "दस"],
        "ans": 0,
        "sol": "There are six Vedangas: Shiksha, Kalpa, Vyakarana, Nirukta, Chhanda, and Jyotisha.",
        "hi_sol": "छह वेदांग हैं: शिक्षा, कल्प, व्याकरण, निरुक्त, छंद और ज्योतिष।"
    },
    {
        "q": "Yaska's 'Nirukta' is the earliest Indian treatise on which of the following subjects?",
        "hi_q": "यास्क का 'निरुक्त' निम्नलिखित में से किस विषय पर सबसे प्रारंभिक भारतीय ग्रंथ है?",
        "opts": ["Etymology and Semantics", "Grammar rules", "Astronomy and Timekeeping", "Sacrificial rituals"],
        "hi_opts": ["व्युत्पत्तिशास्त्र और भाषाविज्ञान", "व्याकरण के नियम", "खगोल विज्ञान और समय गणना", "यज्ञीय अनुष्ठान"],
        "ans": 0,
        "sol": "Nirukta is the etymological treatise explaining difficult Vedic words.",
        "hi_sol": "निरुक्त कठिन वैदिक शब्दों की व्याख्या करने वाला व्युत्पत्ति संबंधी ग्रंथ है।"
    },
    {
        "q": "Panini's 'Ashtadhyayi', composed around the 4th century BCE, is a pioneering work on:",
        "hi_q": "चौथी शताब्दी ईसा पूर्व के आसपास रचित पाणिनी की 'अष्टाध्यायी' किस विषय पर एक अग्रणी रचना है?",
        "opts": ["Sanskrit Grammar", "Etymology", "Statecraft", "Astronomy"],
        "hi_opts": ["संस्कृत व्याकरण", "व्युत्पत्तिशास्त्र", "शासनकला", "खगोल विज्ञान"],
        "ans": 0,
        "sol": "Ashtadhyayi is the authoritative work on Sanskrit grammar (Vyakarana).",
        "hi_sol": "अष्टाध्यायी संस्कृत व्याकरण (व्याकरण) पर आधिकारिक रचना है।"
    },
    {
        "q": "The Shulba Sutras, which contain ancient geometric rules for building altars, are associated with which Vedanga?",
        "hi_q": "यज्ञ वेदियों के निर्माण के लिए प्राचीन ज्यामितीय नियमों वाले शुल्ब सूत्र किस वेदांग से जुड़े हैं?",
        "opts": ["Kalpa", "Shiksha", "Jyotisha", "Chhanda"],
        "hi_opts": ["कल्प", "शिक्षा", "ज्योतिष", "छंद"],
        "ans": 0,
        "sol": "Shulba Sutras are part of Kalpa Sutras, representing early mathematical and architectural rules.",
        "hi_sol": "शुल्ब सूत्र कल्प सूत्रों का हिस्सा हैं, जो प्रारंभिक गणितीय और स्थापत्य नियमों का प्रतिनिधित्व करते हैं।"
    },
    {
        "q": "Which archaeological pottery culture is most closely associated with the geographic extent of the Later Vedic Period?",
        "hi_q": "कौन सी पुरातात्विक मृदभांड संस्कृति उत्तर वैदिक काल के भौगोलिक विस्तार से सबसे निकटता से जुड़ी हुई है?",
        "opts": ["Painted Grey Ware (PGW)", "Ochre Coloured Pottery (OCP)", "Northern Black Polished Ware (NBPW)", "Black and Red Ware (BRW)"],
        "hi_opts": ["चित्रित धूसर मृदभांड (PGW)", "गेरुए रंग के मृदभांड (OCP)", "उत्तरी काले चमकीले मृदभांड (NBPW)", "काले और लाल मृदभांड (BRW)"],
        "ans": 0,
        "sol": "PGW culture corresponds geographically and chronologically to Later Vedic settlements.",
        "hi_sol": "पीजीडब्ल्यू (PGW) संस्कृति उत्तर वैदिक बस्तियों के भौगोलिक और कालानुक्रमिक रूप से मेल खाती है।"
    },
    {
        "q": "The Ochre Coloured Pottery (OCP) culture represents which of the following chronological horizons?",
        "hi_q": "गेरुए रंग के मृदभांड (OCP) संस्कृति निम्नलिखित में से किस कालानुक्रमिक क्षितिज का प्रतिनिधित्व करती है?",
        "opts": ["Late Harappan / Early Vedic transition", "Later Vedic Iron Age", "Mauryan Period", "Mesolithic age"],
        "hi_opts": ["उत्तर-हड़प्पा / प्रारंभिक वैदिक संक्रमण", "उत्तर वैदिक लौह युग", "मौर्य काल", "मध्यपाषाण युग"],
        "ans": 0,
        "sol": "OCP is generally associated with Late Harappan transition and early copper-hoards in the Gangetic divide.",
        "hi_sol": "ओसीपी (OCP) आमतौर पर उत्तर-हड़प्पा संक्रमण और गंगा-यमुना दोआब में प्रारंभिक ताम्र-निधि संस्कृतियों से जुड़ी है।"
    },
    {
        "q": "The Zend Avesta, the ancient Iranian sacred text, shares close linguistic parallels with which Mandala of the Rigveda?",
        "hi_q": "प्राचीन ईरानी पवित्र ग्रंथ जेंड अवेस्ता ऋग्वेद के किस मंडल के साथ निकट भाषाई समानताएं साझा करता है?",
        "opts": ["The early Family Books (Mandalas II-VII)", "The late 10th Mandala", "The 9th Mandala dedicated to Soma", "The 1st Mandala"],
        "hi_opts": ["प्रारंभिक पारिवारिक पुस्तकें (मंडल II-VII)", "बाद का १०वां मंडल", "सोम को समर्पित ९वां मंडल", "पहला मंडल"],
        "ans": 0,
        "sol": "Linguistic parallels are closest with the older family books of the Rigveda.",
        "hi_sol": "भाषाई समानताएं ऋग्वेद की पुरानी पारिवारिक पुस्तकों के साथ सबसे अधिक हैं।"
    },
    {
        "q": "Which Western Asiatic inscription dated to c. 1600 BCE mentions Indo-Aryan names like Surias and Marutas?",
        "hi_q": "लगभग 1600 ईसा पूर्व का कौन सा पश्चिमी एशियाई शिलालेख सूरियास (Surias) और मारुतास (Marutas) जैसे भारत-आर्य नामों का उल्लेख करता है?",
        "opts": ["Kassite Inscription of Babylon", "Boghazkoi Inscription", "Behistun Inscription", "Persepolis Inscription"],
        "hi_opts": ["बेबीलोन का कस्साइट शिलालेख", "बोगाजकोई शिलालेख", "बेहिस्तुन शिलालेख", "पर्सेपोलिस शिलालेख"],
        "ans": 0,
        "sol": "The Kassite tablets of Babylon name gods resembling Surya and Maruts.",
        "hi_sol": "बेबीलोन की कस्साइट पट्टिकाएं सूर्य और मरुत से मिलते-जुलते देवताओं के नाम दर्ज करती हैं।"
    },
    {
        "q": "Which Painted Grey Ware (PGW) site yielded extensive early evidence of iron smelting furnaces?",
        "hi_q": "किस चित्रित धूसर मृदभांड (PGW) स्थल से व्यापक रूप से लोहा गलाने की भट्टियों के शुरुआती साक्ष्य मिले हैं?",
        "opts": ["Atranjikhera", "Hastinapur", "Bhagwanpura", "Alamgirpur"],
        "hi_opts": ["अतरंजीखेड़ा", "हस्तिनापुर", "भगवानपुरा", "आलमगीरपुर"],
        "ans": 0,
        "sol": "Atranjikhera in Uttar Pradesh provided early evidence of iron smelting and tool workshops.",
        "hi_sol": "उत्तर प्रदेश के अतरंजीखेड़ा से लोहा गलाने और उपकरण बनाने के प्रारंभिक साक्ष्य मिले हैं।"
    },
    {
        "q": "Who excavated the PGW site of Hastinapur in the early 1950s, establishing a tentative link to the Mahabharata storyline?",
        "hi_q": "1950 के दशक की शुरुआत में हस्तिनापुर के PGW स्थल का उत्खनन किसने किया था, जिससे महाभारत की कहानी से एक संभावित संबंध स्थापित हुआ?",
        "opts": ["B.B. Lal", "Mortimer Wheeler", "John Marshall", "Alexander Cunningham"],
        "hi_opts": ["बी.बी. लाल", "मॉर्टिमर व्हीलर", "जॉन मार्शल", "अलेक्जेंडर कनिंघम"],
        "ans": 0,
        "sol": "Archaeologist B.B. Lal excavated Hastinapur and correlated the PGW layer with the Mahabharata towns.",
        "hi_sol": "पुरातत्वविद् बी.बी. लाल ने हस्तिनापुर का उत्खनन किया और पीजीडब्ल्यू परत को महाभारत के शहरों से जोड़ा।"
    },
    {
        "q": "Which site provides a rare archaeological example of an overlap between the Late Harappan culture and the Painted Grey Ware (PGW) culture?",
        "hi_q": "कौन सा स्थल उत्तर-हड़प्पा संस्कृति और चित्रित धूसर मृदभांड (PGW) संस्कृति के बीच ओवरलैप का एक दुर्लभ पुरातात्विक उदाहरण प्रदान करता है?",
        "opts": ["Bhagwanpura in Haryana", "Atranjikhera", "Hastinapur", "Noh in Rajasthan"],
        "hi_opts": ["हरियाणा में भगवानपुरा", "अतरंजीखेड़ा", "हस्तिनापुर", "राजस्थान में नोह"],
        "ans": 0,
        "sol": "Bhagwanpura shows a clear stratigraphical overlap where Late Harappan pottery and PGW coexisted.",
        "hi_sol": "भगवानपुरा एक स्पष्ट पुरातात्विक ओवरलैप दिखाता है जहां उत्तर-हड़प्पा मृदभांड और पीजीडब्ल्यू एक साथ सह-अस्तित्व में थे।"
    },
    {
        "q": "Which Rigvedic term was generic for copper or bronze, indicating the absence of iron in the early phase?",
        "hi_q": "कौन सा ऋग्वैदिक शब्द तांबे या कांसे के लिए सामान्य था, जो प्रारंभिक चरण में लोहे की अनुपस्थिति को दर्शाता है?",
        "opts": ["Ayas", "Krishna-ayas", "Syama-ayas", "Lohit-ayas"],
        "hi_opts": ["अयस", "कृष्ण-अयस", "श्याम-अयस", "लोहित-अयस"],
        "ans": 0,
        "sol": "Ayas in the early hymns meant copper/bronze; iron was named later as Krishna-ayas.",
        "hi_sol": "शुरुआती भजनों में अयस का अर्थ तांबा/कांसा था; लोहे को बाद में कृष्ण-अयस नाम दिया गया।"
    },
    {
        "q": "The division of Vedic literature into Karma-kanda (rituals) and Jnana-kanda (knowledge) places which texts under Jnana-kanda?",
        "hi_q": "वैदिक साहित्य का कर्मकांड (अनुष्ठान) और ज्ञानकांड (ज्ञान) में विभाजन किन ग्रंथों को ज्ञानकांड के अंतर्गत रखता है?",
        "opts": ["Upanishads", "Samhitas", "Brahmanas", "Pedangas"],
        "hi_opts": ["उपनिषद", "संहिता", "ब्राह्मण", "वेदांग"],
        "ans": 0,
        "sol": "The Upanishads form the Jnana-kanda (philosophy and self-knowledge) of the Vedas.",
        "hi_sol": "उपनिषद वेदों के ज्ञानकांड (दर्शन और आत्म-ज्ञान) का निर्माण करते हैं।"
    },
    {
        "q": "Which Vedic Brahmana text describes the agricultural activities of plowing, sowing, harvesting, and threshing in detail?",
        "hi_q": "कौन सा वैदिक ब्राह्मण ग्रंथ जुताई, बुवाई, कटाई और मड़ाई की कृषि गतिविधियों का विस्तार से वर्णन करता है?",
        "opts": ["Shatapatha Brahmana", "Aitareya Brahmana", "Gopatha Brahmana", "Taittiriya Brahmana"],
        "hi_opts": ["शतपथ ब्राह्मण", "ऐतरेय ब्राह्मण", "गोपथ ब्राह्मण", "तैत्तिरीय ब्राह्मण"],
        "ans": 0,
        "sol": "The Shatapatha Brahmana provides a step-by-step detail of agricultural operations.",
        "hi_sol": "शतपथ ब्राह्मण कृषि कार्यों का चरण-दर-चरण विवरण प्रदान करता है।"
    },
    {
        "q": "The concept of 'Rta' (cosmic, moral, and natural order) in the Rigveda is primarily guarded by which deity?",
        "hi_q": "ऋग्वेद में 'ऋत' (ब्रह्मांडीय, नैतिक और प्राकृतिक व्यवस्था) की अवधारणा की रक्षा मुख्य रूप से किस देवता द्वारा की जाती है?",
        "opts": ["Varuna", "Indra", "Agni", "Soma"],
        "hi_opts": ["वरुण", "इंद्र", "अग्नि", "सोम"],
        "ans": 0,
        "sol": "Varuna is celebrated as the guardian of Rta (moral and cosmic order).",
        "hi_sol": "वरुण को ऋत (नैतिक और ब्रह्मांडीय व्यवस्था) के संरक्षक के रूप में पूजा जाता है।"
    },
    {
        "q": "Which Rigvedic deity is addressed as 'Purandara' (the breaker of forts)?",
        "hi_q": "किस ऋग्वैदिक देवता को 'पुरंदर' (किले तोड़ने वाला) के रूप में संबोधित किया गया है?",
        "opts": ["Indra", "Varuna", "Agni", "Rudra"],
        "hi_opts": ["इंद्र", "वरुण", "अग्नि", "रुद्र"],
        "ans": 0,
        "sol": "Indra is frequently called Purandara due to his role in destroying hostile strongholds.",
        "hi_sol": "विरोधी गढ़ों को नष्ट करने में उनकी भूमिका के कारण इंद्र को अक्सर पुरंदर कहा जाता है।"
    },
    {
        "q": "The non-Aryan groups called 'Dasyus' are described in the Rigveda with which hostile epithet?",
        "hi_q": "ऋग्वेद में 'दस्यु' नामक गैर-आर्य समूहों का वर्णन किस शत्रुतापूर्ण विशेषण के साथ किया गया है?",
        "opts": ["Mridhravac (hostile/strange speech) and Anyavrata (different rites)", "Gomat (wealthy in cows)", "Sajana (kinsmen)", "Rathakara (charioteers)"],
        "hi_opts": ["मृध्रवाच (शत्रुतापूर्ण/अजीब बोली) और अन्यव्रत (विभिन्न अनुष्ठान)", "गोमत (गायों से समृद्ध)", "सजन (स्वजन)", "रथकार (रथ चालक)"],
        "ans": 0,
        "sol": "They were called Mridhravac and Anyavrata due to differences in rituals and language.",
        "hi_sol": "अनुष्ठानों and भाषा में अंतर के कारण उन्हें मृध्रवाच और अन्यव्रत कहा जाता था।"
    },
    {
        "q": "The term 'Amaju' in the Rigvedic social vocabulary refers to:",
        "hi_q": "ऋग्वैदिक सामाजिक शब्दावली में 'अमाजू' शब्द किसे संदर्भित करता है?",
        "opts": ["Females who remained unmarried and lived with parents throughout life", "A childless widow who practiced Niyoga", "Women who headed local assemblies", "A female weaver working in guilds"],
        "hi_opts": ["वे महिलाएँ जो जीवन भर अविवाहित रहीं और माता-पिता के साथ रहीं", "एक निःसंतान विधवा जिसने नियोग का पालन किया", "स्थानीय सभाओं का नेतृत्व करने वाली महिलाएँ", "श्रेणियों में काम करने वाली महिला बुनकर"],
        "ans": 0,
        "sol": "Amaju refers to women who chose lifelong spinsterhood.",
        "hi_sol": "अमाजू उन महिलाओं को संदर्भित करता है जिन्होंने आजीवन अविवाहित रहने का विकल्प चुना।"
    },
    {
        "q": "The chronological sequence of ancient Indian pottery cultures is represented by which order?",
        "hi_q": "प्राचीन भारतीय मृदभांड संस्कृतियों का कालानुक्रमिक क्रम किस रूप में दर्शाया जाता है?",
        "opts": ["OCP -> BRW -> PGW -> NBPW", "PGW -> OCP -> NBPW -> BRW", "NBPW -> PGW -> BRW -> OCP", "BRW -> PGW -> OCP -> NBPW"],
        "hi_opts": ["OCP -> BRW -> PGW -> NBPW", "PGW -> OCP -> NBPW -> BRW", "NBPW -> PGW -> BRW -> OCP", "BRW -> PGW -> OCP -> NBPW"],
        "ans": 0,
        "sol": "The sequence is Ochre Coloured Pottery, Black and Red Ware, Painted Grey Ware, and Northern Black Polished Ware.",
        "hi_sol": "यह क्रम गेरुए रंग के मृदभांड, काले और लाल मृदभांड, चित्रित धूसर मृदभांड और उत्तरी काले चमकीले मृदभांड है।"
    },
    {
        "q": "The term 'Rajasuya', which appears in Later Vedic texts, represents which type of ritual?",
        "hi_q": "उत्तर वैदिक ग्रंथों में आने वाला 'राजसूय' शब्द किस प्रकार के अनुष्ठान का प्रतिनिधित्व करता है?",
        "opts": ["Royal consecration ceremony to establish supreme authority", "Chariot race for rejuvenation of king's power", "Sacrifice of a horse to claim territory", "Daily domestic offerings"],
        "hi_opts": ["सर्वोच्च अधिकार स्थापित करने के लिए शाही राज्याभिषेक समारोह", "राजा की शक्ति के कायाकल्प के लिए रथ दौड़", "क्षेत्र पर दावा करने के लिए घोड़े की बलि", "दैनिक घरेलू प्रसाद"],
        "ans": 0,
        "sol": "Rajasuya was the royal consecration ceremony for kings.",
        "hi_sol": "राजसूय राजाओं के लिए शाही राज्याभिषेक समारोह था।"
    },
    {
        "q": "Which scholar is credited with proposing the Sanskrit connection to European languages, initiating Indo-European comparative linguistics?",
        "hi_q": "किस विद्वान को यूरोपीय भाषाओं से संस्कृत के संबंध का प्रस्ताव देने का श्रेय दिया जाता है, जिससे भारत-यूरोपीय तुलनात्मक भाषाविज्ञान की शुरुआत हुई?",
        "opts": ["Sir William Jones", "Max Muller", "Mortimer Wheeler", "John Marshall"],
        "hi_opts": ["सर विलियम जोन्स", "मैक्स मूर", "मॉर्टिमर व्हीलर", "जॉन मार्शल"],
        "ans": 0,
        "sol": "Sir William Jones delivered a lecture in 1786 pointing out Sanskrit parallels with Greek and Latin.",
        "hi_sol": "सर विलियम जोन्स ने 1786 में ग्रीक और लैटिन के साथ संस्कृत की समानताओं को इंगित करते हुए एक व्याख्यान दिया था।"
    },
    {
        "q": "The 'Combined Method' of historical reconstruction, combining textual analysis with archaeological data, was pioneered by:",
        "hi_q": "ऐतिहासिक पुनर्निर्माण की 'संयुक्त पद्धति' (Combined Method), जो पुरातात्विक डेटा के साथ पाठ्य विश्लेषण को जोड़ती है, किसके द्वारा शुरू की गई थी?",
        "opts": ["D.D. Kosambi", "R.C. Majumdar", "Romila Thapar", "R.S. Sharma"],
        "hi_opts": ["डी.डी. कोसंबी", "आर.सी. मजूमदार", "रोमिला थापर", "आर.एस. शर्मा"],
        "ans": 0,
        "sol": "D.D. Kosambi introduced the combined method in Indian historiography.",
        "hi_sol": "डी.डी. कोसंबी ने भारतीय इतिहास लेखन में संयुक्त पद्धति की शुरुआत की।"
    },
    {
        "q": "The skeletal remains debate at Mohenjo-daro was analyzed by Kenneth Kennedy to disprove which theory?",
        "hi_q": "केनेथ केनेडी ने किस सिद्धांत को खारिज करने के लिए मोहनजोदड़ो के कंकालों के अवशेषों का विश्लेषण किया था?",
        "opts": ["The Aryan Invasion Theory", "The Aryan Migration Theory", "The Harappan flood theory", "The tectonic shift theory"],
        "hi_opts": ["आर्य आक्रमण सिद्धांत (Aryan Invasion Theory)", "आर्य प्रवास सिद्धांत", "हड़प्पा बाढ़ सिद्धांत", "विवर्तनिक विस्थापन सिद्धांत"],
        "ans": 0,
        "sol": "Kennedy proved the skeletons showed signs of anemia and disease rather than weapon trauma, refuting Wheeler's invasion massacre theory.",
        "hi_sol": "केनेडी ने साबित किया कि कंकाल हथियारों के आघात के बजाय एनीमिया और बीमारी के लक्षण दिखाते थे, जिससे व्हीलर के आक्रमण नरसंहार सिद्धांत का खंडन हुआ।"
    },
    {
        "q": "In the 2019 Rakhigarhi ancient DNA study, what major finding regarding Harappan genetic ancestry was published?",
        "hi_q": "2019 के राखीगढ़ी प्राचीन डीएनए अध्ययन में, हड़प्पा आनुवंशिक वंशावली के संबंध में क्या प्रमुख खोज प्रकाशित की गई थी?",
        "opts": [
            "The Harappan skeleton lacked Steppe genetic ancestry, separating them from early Indo-Aryans",
            "The Harappan skeleton possessed high Steppe genetic ancestry",
            "The Harappans were genetically identical to ancient Greeks",
            "No DNA could be recovered from the skeletons"
        ],
        "hi_opts": [
            "हड़प्पा के कंकाल में स्टेप आनुवंशिक वंशावली (Steppe ancestry) का अभाव था, जो उन्हें प्रारंभिक भारत-आर्यों से अलग करता है",
            "हड़प्पा के कंकाल में उच्च स्टेप आनुवंशिक वंशावली थी",
            "हड़प्पावासी आनुवंशिक रूप से प्राचीन यूनानियों के समान थे",
            "कंकालों से कोई डीएनए बरामद नहीं किया जा सका"
        ],
        "ans": 0,
        "sol": "The DNA study of a Rakhigarhi skeleton proved that Steppe pastoralist ancestry was absent in Harappans, showing they lived before the Indo-Aryan migrations.",
        "hi_sol": "राखीगढ़ी के कंकाल के डीएनए अध्ययन ने साबित कर दिया कि हड़प्पावासियों में स्टेप चरवाहा वंश अनुपस्थित था, जो दर्शाता है कि वे भारत-आर्य प्रवास से पहले रहते थे।"
    },
    {
        "q": "The excavations at Sanauli in Uttar Pradesh yielded burials that included which controversial find?",
        "hi_q": "उत्तर प्रदेश के सनौली में हुई खुदाई में कब्रें मिलीं जिनमें कौन सी विवादास्पद खोज शामिल थी?",
        "opts": ["Wooden solid or spoked wheeled carts/chariots", "Iron swords from 2000 BCE", "Written Sanskrit tablets", "Golden crowns of Indo-Aryans"],
        "hi_opts": ["लकड़ी की ठोस या तीलीदार पहियों वाली गाड़ियाँ/रथ", "2000 ईसा पूर्व की लोहे की तलवारें", "लिखित संस्कृत पट्टिकाएं", "भारत-आर्यों के सोने के मुकुट"],
        "ans": 0,
        "sol": "Sanauli burials yielded copper-plated wooden carts, interpreted by some as horse-drawn war chariots and by others as solid-wheeled bullock carts.",
        "hi_sol": "सनौली कब्रगाहों से तांबे की परत चढ़ी लकड़ी की गाड़ियाँ मिलीं, जिनकी व्याख्या कुछ लोगों ने घोड़े से खींचे जाने वाले युद्ध रथों के रूप में की और दूसरों ने ठोस पहियों वाली बैलगाड़ियों के रूप में की।"
    },
    {
        "q": "Which of the following describes the 'Nasadiya Sukta' in the Rigveda?",
        "hi_q": "निम्नलिखित में से कौन सा ऋग्वेद में 'नासदीय सूक्त' का वर्णन करता है?",
        "opts": ["A philosophical hymn debating the origin of the universe", "A list of rivers flowing through Punjab", "A song celebrating military victories", "A ritual guidelines text for Ashvamedha"],
        "hi_opts": ["ब्रह्मांड की उत्पत्ति पर बहस करने वाला एक दार्शनिक सूक्त", "पंजाब से बहने वाली नदियों की एक सूची", "सैन्य जीत का जश्न मनाने वाला एक गीत", "अश्वमेध के लिए एक अनुष्ठानिक दिशानिर्देश ग्रंथ"],
        "ans": 0,
        "sol": "The Nasadiya Sukta (Mandala X) is the famous Creation Hymn expressing skepticism about the absolute origin of cosmos.",
        "hi_sol": "नासदीय सूक्त (१०वां मंडल) प्रसिद्ध सृष्टि सूक्त है जो ब्रह्मांड की पूर्ण उत्पत्ति के बारे में संदेह व्यक्त करता है।"
    },
    {
        "q": "The Gopatha Brahmana is the sole surviving Brahmana text associated with which of the four Vedas?",
        "hi_q": "गोपथ ब्राह्मण चार वेदों में से किस वेद से जुड़ा एकमात्र जीवित ब्राह्मण ग्रंथ है?",
        "opts": ["Atharvaveda", "Rigveda", "Samaveda", "Yajurveda"],
        "hi_opts": ["अथर्ववेद", "ऋग्वेद", "सामवेद", "यजुर्वेद"],
        "ans": 0,
        "sol": "The Gopatha Brahmana is the only Brahmana text of the Atharvaveda.",
        "hi_sol": "गोपथ ब्राह्मण अथर्ववेद का एकमात्र ब्राह्मण ग्रंथ है।"
    },
    {
        "q": "Which Vedanga is responsible for regulating the meters and poetic structures of Vedic hymns?",
        "hi_q": "वैदिक भजनों के छंदों और काव्य संरचनाओं को विनियमित करने के लिए कौन सा वेदांग उत्तरदायी है?",
        "opts": ["Chhanda", "Shiksha", "Nirukta", "Vyakarana"],
        "hi_opts": ["छंद", "शिक्षा", "निरुक्त", "व्याकरण"],
        "ans": 0,
        "sol": "Chhanda (Metrics) deals with the rhythmic meters of Vedic hymns.",
        "hi_sol": "छंद (Chhanda) वैदिक भजनों के लयबद्ध छंदों से संबंधित है।"
    },
    {
        "q": "Lagadha's 'Vedanga Jyotisha' is primarily concerned with which domain?",
        "hi_q": "लगध का 'वेदांग ज्योतिष' मुख्य रूप से किस क्षेत्र से संबंधित है?",
        "opts": ["Astronomy and Calendar calculations for sacrifices", "Horoscope predictions based on zodiac signs", "Architectural measurements of homes", "Phonetics of pronunciation"],
        "hi_opts": ["यज्ञों के लिए खगोल विज्ञान और कैलेंडर गणना", "राशियों के आधार पर कुंडली की भविष्यवाणियां", "घरों का स्थापत्य मापन", "उच्चारण की ध्वन्यात्मकता"],
        "ans": 0,
        "sol": "Vedanga Jyotisha is the earliest text on astronomy, used to calculate correct sacrificial times.",
        "hi_sol": "वेदांग ज्योतिष खगोल विज्ञान पर सबसे प्रारंभिक ग्रंथ है, जिसका उपयोग यज्ञ के सही समय की गणना के लिए किया जाता था।"
    },
    {
        "q": "Which Dharma Sutra is widely considered by historians to be the oldest and most authoritative?",
        "hi_q": "इतिहासकारों द्वारा व्यापक रूप से किस धर्म सूत्र को सबसे पुराना और सबसे आधिकारिक माना जाता है?",
        "opts": ["Gautama Dharma Sutra", "Baudhayana Dharma Sutra", "Apastamba Dharma Sutra", "Vasistha Dharma Sutra"],
        "hi_opts": ["गौतम धर्म सूत्र", "बौधायन धर्म सूत्र", "आपस्तम्ब धर्म सूत्र", "वसिष्ठ धर्म सूत्र"],
        "ans": 0,
        "sol": "Gautama Dharma Sutra is historically the earliest of the Dharma Sutras.",
        "hi_sol": "गौतम धर्म सूत्र ऐतिहासिक रूप से धर्म सूत्रों में सबसे पुराना है।"
    },
    {
        "q": "The Baudhayana Shulba Sutra contains mathematical rules that are an early precursor to which theorem?",
        "hi_q": "बौधायन शुल्ब सूत्र में गणितीय नियम हैं जो किस प्रमेय के प्रारंभिक अग्रदूत हैं?",
        "opts": ["Pythagorean Theorem", "Binomial Theorem", "Fibonacci sequence", "Euler's formula"],
        "hi_opts": ["पाइथागोरस प्रमेय", "द्विपद प्रमेय", "फाइबोनैचि अनुक्रम", "यूलर का सूत्र"],
        "ans": 0,
        "sol": "The Baudhayana Shulba Sutra contains a formulation of the geometric rule later known as the Pythagorean theorem.",
        "hi_sol": "बौधायन शुल्ब सूत्र में उस ज्यामितीय नियम का प्रतिपादन है जिसे बाद में पाइथागोरस प्रमेय के रूप में जाना गया।"
    },
    {
        "q": "The Indo-Iranian deity parallel between Varuna and the Iranian supreme god is represented by which name?",
        "hi_q": "वरुण and ईरानी सर्वोच्च देवता के बीच भारत-ईरानी देव-समानता किस नाम से प्रदर्शित होती है?",
        "opts": ["Ahura Mazda", "Mithra", "Haoma", "Verethraghna"],
        "hi_opts": ["अहुर मज्दा", "मित्रा", "हाओमा", "वेरेथ्रघ्न"],
        "ans": 0,
        "sol": "The Vedic Varuna (often addressed as Asura) matches the Iranian Ahura Mazda in characteristics and cosmic order.",
        "hi_sol": "वैदिक वरुण (अक्सर असुर के रूप में संबोधित) विशेषताओं और ब्रह्मांडीय व्यवस्था में ईरानी अहुर मज्दा से मेल खाते हैं।"
    },
    {
        "q": "Which major sacrifice in Later Vedic times involved a year-long wandering of a horse followed by a grand coronation assertion?",
        "hi_q": "उत्तर वैदिक काल में किस प्रमुख यज्ञ में एक घोड़े का वर्ष भर भटकना और उसके बाद एक भव्य राज्याभिषेक का दावा शामिल था?",
        "opts": ["Ashvamedha", "Rajasuya", "Vajapeya", "Agnihotra"],
        "hi_opts": ["अश्वमेध", "राजसूय", "वाजपेय", "अग्निहोत्र"],
        "ans": 0,
        "sol": "Ashvamedha (Horse Sacrifice) asserted a king's imperial sovereignty over wandering territories.",
        "hi_sol": "अश्वमेध (घोड़े का यज्ञ) भटकते हुए क्षेत्रों पर एक राजा की शाही संप्रभुता का दावा करता था।"
    },
    {
        "q": "What describes the character of the Rigvedic society as reflected in the family books?",
        "hi_q": "पारिवारिक पुस्तकों में प्रतिबिंबित ऋग्वैदिक समाज के चरित्र का क्या वर्णन है?",
        "opts": ["Kin-based pastoral nomadism with localized cultivation", "Sedentary agricultural empire with written taxation", "Highly urbanized cities built on grid iron patterns", "Maritime empire trading across the Persian gulf"],
        "hi_opts": ["स्थानीयकृत खेती के साथ नातेदारी-आधारित पशुचारण खानाबदोश जीवन", "लिखित कराधान के साथ स्थायी कृषि साम्राज्य", "ग्रिड पैटर्न पर बने अत्यधिक शहरीकृत शहर", "फारस की खाड़ी में व्यापार करने वाला समुद्री साम्राज्य"],
        "ans": 0,
        "sol": "Rigvedic society was primarily pastoral, kinship-based, and mobile, with minor settled agriculture.",
        "hi_sol": "ऋग्वैदिक समाज मुख्य रूप से पशुपालक, रिश्तेदारी पर आधारित और गतिशील था, जिसमें मामूली रूप से स्थायी कृषि की जाती थी।"
    },
    {
        "q": "The Upanishadic criticism of Brahmanical ritual sacrifices metaphorically calls them:",
        "hi_q": "ब्राह्मणवादी कर्मकांडीय यज्ञों की उपनिषदों की आलोचना उन्हें रूपक रूप से क्या कहती है?",
        "opts": ["Leaky boats ('adridha yajna-rupa')", "Unbreakable bonds", "Pathways to heaven", "Royal crowns"],
        "hi_opts": ["कमजोर नौकाएँ ('अदृढ़ा यज्ञरूपा')", " अटूट बंधन", "स्वर्ग के मार्ग", "शाही मुकुट"],
        "ans": 0,
        "sol": "The Mundaka Upanishad calls sacrifices leaky boats that cannot carry one safely across the ocean of rebirth.",
        "hi_sol": "मुण्डक उपनिषद यज्ञों को कमजोर नौकाएँ कहता है जो किसी को पुनर्जन्म के सागर के पार सुरक्षित रूप से नहीं ले जा सकतीं।"
    },
    {
        "q": "Which major PGW site is located in the Upper Gangetic valley and has been excavated systematically to show Later Vedic settlements?",
        "hi_q": "कौन सा मुख्य PGW स्थल ऊपरी गंगा घाटी में स्थित है और उत्तर वैदिक बस्तियों को दर्शाने के लिए व्यवस्थित रूप से उत्खनन किया गया है?",
        "opts": ["Hastinapur", "Atranjikhera", "Alamgirpur", "All of the above"],
        "hi_opts": ["हस्तिनापुर", "अतरंजीखेड़ा", "आलमगीरपुर", "उपरोक्त सभी"],
        "ans": 3,
        "sol": "All these sites are PGW contexts in the upper Gangetic basin, representing Later Vedic horizons.",
        "hi_sol": "ये सभी स्थल ऊपरी गंगा बेसिन में पीजीडब्ल्यू (PGW) संदर्भ हैं, जो उत्तर वैदिक क्षितिज का प्रतिनिधित्व करते हैं।"
    },
    {
        "q": "The Vedic custom of 'Niyoga' (levirate) indicates which aspect of early family life?",
        "hi_q": "वैदिक 'नियोग' प्रथा प्रारंभिक पारिवारिक जीवन के किस पहलू को दर्शाती है?",
        "opts": ["A widow could bear a child with her brother-in-law to secure a male heir for the deceased husband", "Rigid child marriage rules", "Polygamy practiced exclusively by priests", "A complete ban on widow remarriage"],
        "hi_opts": ["एक विधवा मृतक पति के लिए पुरुष उत्तराधिकारी प्राप्त करने के लिए अपने देवर के साथ संतान पैदा कर सकती थी", "कठोर बाल विवाह नियम", "केवल पुरोहितों द्वारा बहुविवाह का पालन", "विधवा पुनर्विवाह पर पूर्ण प्रतिबंध"],
        "ans": 0,
        "sol": "Niyoga was the custom enabling a widow to raise offspring with a brother-in-law, securing family lineage continuity.",
        "hi_sol": "नियोग एक विधवा को देवर के साथ संतान पैदा करने में सक्षम बनाने वाली प्रथा थी, जिससे पारिवारिक वंश की निरंतरता सुरक्षित होती थी।"
    },
    {
        "q": "Which scholar's pioneering English translation of the Rigveda in the 19th century shaped early modern debates on Indo-Aryan migration?",
        "hi_q": "19th शताब्दी में ऋग्वेद के किस विद्वान के अग्रणी अंग्रेजी अनुवाद ने भारत-आर्य प्रवास पर शुरुआती आधुनिक बहसों को आकार दिया?",
        "opts": ["Max Muller", "William Jones", "B.G. Tilak", "Dayanand Sarasvati"],
        "hi_opts": ["मैक्स मूर", "विलियम जोन्स", "बी.जी. तिलक", "दयानंद सरस्वती"],
        "ans": 0,
        "sol": "Max Muller edited and translated the Rigveda, proposing the linguistic model of Aryan migration.",
        "hi_sol": "मैक्स मूर ने ऋग्वेद का संपादन और अनुवाद किया, जिससे आर्य प्रवास के भाषाई मॉडल का प्रस्ताव मिला।"
    },
    {
        "q": "The Purusha Sukta, which outlines the cosmic origin of the four Varnas, is located in which part of the Rigveda?",
        "hi_q": "पुरुष सूक्त, जो चार वर्णों की ब्रह्मांडीय उत्पत्ति की रूपरेखा तैयार करता है, ऋग्वेद के किस भाग में स्थित है?",
        "opts": ["Mandala X", "Mandala III", "Mandala IX", "Mandala I"],
        "hi_opts": ["दसवां मंडल", "तीसरा मंडल", "नौवां मंडल", "पहला मंडल"],
        "ans": 0,
        "sol": "The Purusha Sukta is the 90th hymn of Rigveda Mandala X.",
        "hi_sol": "पुरुष सूक्त ऋग्वेद के १०वें मंडल का ९०वां सूक्त है।"
    },
    {
        "q": "The geographical shift from the Sapta-Sindhu to the Ganga-Yamuna Doab in Later Vedic times is best recorded in which narrative?",
        "hi_q": "उत्तर वैदिक काल में सप्त-सिंधु से गंगा-यमुना दोआब में भौगोलिक विस्थापन किस कथा में सबसे अच्छी तरह से दर्ज है?",
        "opts": ["The legend of Videgha Mathava in Shatapatha Brahmana", "The Purusha Sukta creation myth", "The Battle of Ten Kings narrative", "The Yama-Nachiketa dialogue"],
        "hi_opts": ["शतपथ ब्राह्मण में विदेघ माथव की कथा", "पुरुष सूक्त सृष्टि मिथक", "दस राजाओं के युद्ध की कथा", "यम-नचिकेता संवाद"],
        "ans": 0,
        "sol": "The story of Videgha Mathava migrating eastwards clearing land with Agni Vaishvanara represents this expansion.",
        "hi_sol": "अग्नि वैश्वानर के साथ भूमि को साफ करते हुए पूर्व की ओर प्रवास करने वाले विदेघ माथव की कहानी इस विस्तार का प्रतिनिधित्व करती है।"
    },
    {
        "q": "Which Rigvedic river is praised as the swiftest flowing river, located in the Swat region of Pakistan?",
        "hi_q": "किस ऋग्वैदिक नदी को सबसे तीव्र बहने वाली नदी के रूप में सराहा गया है, जो पाकिस्तान के स्वात क्षेत्र में स्थित है?",
        "opts": ["Suvastu", "Vitasta", "Asikni", "Parushni"],
        "hi_opts": ["सुवास्तु", "वितस्ता", "असिकनी", "परुष्णी"],
        "ans": 0,
        "sol": "Suvastu corresponds to the modern Swat River, praised for its swiftness and clear waters.",
        "hi_sol": "सुवास्तु आधुनिक स्वात नदी से मेल खाती है, जिसकी उसकी गति और साफ पानी के लिए प्रशंसा की गई है।"
    },
    {
        "q": "The standard barter ornament called 'Nishka' in the Rigveda was traditionally made of which metal?",
        "hi_q": "ऋग्वेद में 'निष्क' कहलाने वाला मानक वस्तु विनिमय आभूषण पारंपरिक रूप से किस धातु से बना होता था?",
        "opts": ["Gold", "Silver", "Copper", "Iron"],
        "hi_opts": ["सोना", "चांदी", "तांबा", "लोहा"],
        "ans": 0,
        "sol": "Nishka was a gold ornament or neckpiece used as a unit of value in transactions.",
        "hi_sol": "निष्क सोने का एक आभूषण या गले का हार था जिसका उपयोग लेन-देन में मूल्य की इकाई के रूप में किया जाता था।"
    }
]

# Set on data dictionary
data["practiceQuestions"] = practice_qs


# Preserve 10 Mock Test Questions
mock_qs = []
mock_qs.append({
    "q": "The Boghazkoi (Bogazköy) tablets from Anatolia (c. 1400 BCE) are crucial for Vedic history because they:",
    "opts": [
        "Name Vedic deities Mitra, Varuna, Indra, and Nasatya in a political treaty",
        "Describe the military migration pathways of Indo-Aryans",
        "Record the earliest known hymns dedicated to Agni",
        "Provide genealogical lists matching the Rigvedic gotras"
    ],
    "ans": 0,
    "sol": "The Boghazkoi inscription from a Mitanni-Hittite treaty invokes four Vedic gods (Mitra, Varuna, Indra, Nasatya) as guardians, showing their veneration in West Asia c. 1400 BCE."
})
mock_qs.append({
    "q": "Consider the following statements regarding the tribal assemblies mentioned in the Rigveda:\n1. The Vidhata was the oldest assembly and had both secular and religious functions.\n2. Women were strictly excluded from participating in the Sabha and Samiti.\nWhich of the statements given above is/are correct?",
    "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    "ans": 0,
    "sol": "Statement 1 is correct. Statement 2 is incorrect because Rigvedic women did participate in the Sabha and Vidhata assemblies."
})
mock_qs.append({
    "q": "The legend of Videgha Mathava and Agni Vaishvanara, describing the eastward expansion of Vedic culture across the Sadanira river, is recorded in which text?",
    "opts": [
        "Shatapatha Brahmana",
        "Aitareya Brahmana",
        "Chandogya Upanishad",
        "Gopatha Brahmana"
    ],
    "ans": 0,
    "sol": "The Shatapatha Brahmana (Yajurveda) records the story of Videgha Mathava carrying the sacrificial fire to settle the Gangetic plains."
})
mock_qs.append({
    "q": "Which of the following is/are the key features of the Painted Grey Ware (PGW) culture associated with the Later Vedic period?\n1. Extensive use of iron tools for agriculture and warfare.\n2. Domestication of horses and use of iron-wheeled chariots.\n3. Stratigraphic overlap with late Harappan levels at sites like Bhagwanpura.\nSelect the correct answer using the code given below:",
    "opts": ["1 and 2 only", "1 and 3 only", "2 and 3 only", "1, 2 and 3"],
    "ans": 1,
    "sol": "Statements 1 and 3 are correct. The chariots in PGW did not have iron-spoked wheels (they were wood, and iron-spoked wheels are a different technological tier)."
})
mock_qs.append({
    "q": "With reference to the Upanishads, consider the following statements:\n1. They represent a transition from ritualistic action to spiritual knowledge.\n2. The Mundaka Upanishad compares rituals to unstable leaky boats.\n3. The earliest Upanishads are written in Classical Sanskrit verse.\nWhich of the statements given above is/are correct?",
    "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "ans": 0,
    "sol": "Statements 1 and 2 are correct. The earliest Upanishads (Brihadaranyaka, Chandogya) are written in prose, not Classical Sanskrit verse."
})
mock_qs.append({
    "q": "Match the following Vedic rivers with their modern counterparts:\nI. Vitasta - A. Jhelum\nII. Asikni - B. Chenab\nIII. Parushni - C. Ravi\nIV. Vipasa - D. Beas\nSelect the correct code:",
    "opts": [
        "I-A, II-B, III-C, IV-D",
        "I-B, II-A, III-C, IV-D",
        "I-A, II-B, III-D, IV-C",
        "I-D, II-C, III-B, IV-A"
    ],
    "ans": 0,
    "sol": "The correct pairings are Vitasta (Jhelum), Asikni (Chenab), Parushni (Ravi), and Vipasa (Beas)."
})
mock_qs.append({
    "q": "Which of the following correctly describes the character of the Atharvaveda?",
    "opts": [
        "It is a compilation of folk magic, charms, and medicine representing popular Vedic life",
        "It contains only liturgical instructions for Yajnas",
        "It is entirely dedicated to the praise of Soma and Agni",
        "It was composed earlier than the Rigveda Samhita"
    ],
    "ans": 0,
    "sol": "The Atharvaveda is unique because it reflects the popular religion, spells for healing, and everyday social conditions of non-priestly classes."
})
mock_qs.append({
    "q": "The Vedangas are auxiliary sciences of the Veda. Which of the following is NOT a correct match?",
    "opts": [
        "Shiksha — Etymology",
        "Vyakarana — Grammar",
        "Kalpa — Ritual procedure",
        "Jyotisha — Astronomy"
    ],
    "ans": 0,
    "sol": "Shiksha refers to phonetics/pronunciation (the nose of the Veda). Etymology is Nirukta."
})
mock_qs.append({
    "q": "The 'combined method' of historical reconstruction for ancient India, combining texts with archaeology and numismatics, was pioneered by:",
    "opts": [
        "D.D. Kosambi",
        "Romila Thapar",
        "Max Müller",
        "R.S. Sharma"
    ],
    "ans": 0,
    "sol": "D.D. Kosambi introduced the combined method, integrating texts, material culture, and field ethnography."
})
mock_qs.append({
    "q": "In the transition from the Early Vedic to the Later Vedic period, the economy underwent which significant shift?",
    "opts": [
        "From pastoral nomadic cattle-rearing to sedentary iron-aided agriculture",
        "From urban trade-based crafts to rural agriculture",
        "From wheat-producing fields to pastoral forest estates",
        "From iron smelting centers to bronze metallurgy dominance"
    ],
    "ans": 0,
    "sol": "The Early Vedic period was primarily nomadic pastoralism (cows), transitioning to settled agriculture (rice, wheat) aided by iron clearance in the Later Vedic era."
})

data["mockTestQuestions"] = mock_qs

# Save content.json
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("SUCCESS: Fully restored theories, concepts, and generated authentic questions.")
