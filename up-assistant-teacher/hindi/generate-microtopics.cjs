const fs = require('fs');
const path = require('path');

// ============================================================================
// ENV LOADER
// ============================================================================
if (fs.existsSync('.env')) {
    const envContent = fs.readFileSync('.env', 'utf8');
    for (const line of envContent.split('\n')) {
        const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?(\s*)$/);
        if (match) {
            const key = match[1];
            let value = match[2] || '';
            if (value.startsWith('"') && value.endsWith('"')) value = value.slice(1, -1);
            if (value.startsWith("'") && value.endsWith("'")) value = value.slice(1, -1);
            process.env[key] = process.env[key] || value.trim();
        }
    }
}

const apiKey = process.env.GEMINI_API_KEY;
if (!apiKey) {
    console.error('GEMINI_API_KEY is not set. Please add it to .env file.');
    process.exit(1);
}

// ============================================================================
// CONSTANTS
// ============================================================================
const REQUEST_DELAY_MS = 20000;
const MAX_RETRIES = 5;
let currentModel = 'gemini-3.5-flash-lite';

// ============================================================================
// HINDI MICROTOPICS (Grammar, Unseen Prose, Poetry Passage, Literature)
// ============================================================================
const MICROTOPICS = [
    // --- SECTION 1: HINDI GRAMMAR (हिंदी व्याकरण) ---
    {
        dir: 'varana-vaichaara-savara-evan-vayanjana',
        name: 'Varna Vichar - Swar aur Vyanjan (वर्ण विचार)',
        hindiName: 'वर्ण विचार - स्वर एवं व्यंजन',
        description: 'Hindi Varna Vichar — classification of Swar (vowels) and Vyanjan (consonants), their types, articulation, and phonological properties.',
        keywords: ['Varna Vichar', 'Swar', 'Vyanjan', 'Hindi Phonology', 'Hindi Varnamala', 'Hindi Grammar UP'],
        type: 'grammar'
    },
    {
        dir: 'sanjanyaa-bhaeda-evan-udaaharana',
        name: 'Sangya - Bhed aur Udaharan (संज्ञा)',
        hindiName: 'संज्ञा - भेद एवं उदाहरण',
        description: 'Hindi Sangya (Noun) — types: Vyaktivaachak, Jaativaachak, Bhaavavaachak, Samuudavaachak, Draavyavaachak, their definitions, differences, and examples.',
        keywords: ['Sangya', 'Noun Hindi', 'Vyaktivaachak Sangya', 'Jaativaachak Sangya', 'Bhaavavaachak Sangya', 'Hindi Grammar'],
        type: 'grammar'
    },
    {
        dir: 'saravanaama-vaibhakatai-evan-kaaraka',
        name: 'Sarvanam - Vibhakti aur Karak (सर्वनाम)',
        hindiName: 'सर्वनाम - विभक्ति एवं कारक',
        description: 'Hindi Sarvanam (Pronoun) — types, vibhakti (case markers), karak (case system), and their grammatical role in sentences.',
        keywords: ['Sarvanam', 'Pronoun Hindi', 'Vibhakti', 'Karak', 'Hindi Grammar UP Assistant Teacher'],
        type: 'grammar'
    },
    {
        dir: 'karaiyaa-karataa-karama-kaaraka',
        name: 'Kriya - Karta, Karma, Karak (क्रिया)',
        hindiName: 'क्रिया - कर्ता, कर्म, कारक',
        description: 'Hindi Kriya (Verb) — types (Sakaramak, Akaramak, Preranarth, Yaugik), karta-karma-karak relationships, tense and voice forms.',
        keywords: ['Kriya', 'Verb Hindi', 'Sakaramak Kriya', 'Akaramak Kriya', 'Karta Karma', 'Hindi Grammar'],
        type: 'grammar'
    },
    {
        dir: 'kaaraka-sapatakaaraka-vaivarana',
        name: 'Karak - Saptakarak Vivaran (कारक)',
        hindiName: 'कारक - सप्तकारक विवरण',
        description: 'Hindi Karak (Case System) — the 8 kaarak: Karta, Karma, Karan, Sampraadan, Apaadaan, Sambandh, Adhikaran, Sambodhan — vibhakti signs and usage.',
        keywords: ['Karak', 'Saptakarak', 'Vibhakti Chinha', 'Hindi Case System', 'Karta Karak', 'Hindi Grammar UP'],
        type: 'grammar'
    },
    {
        dir: 'vaakaya-rachanaa-va-parakaara',
        name: 'Vakya - Rachna aur Prakar (वाक्य)',
        hindiName: 'वाक्य - रचना व प्रकार',
        description: 'Hindi Vakya (Sentence) — types by structure (Saral, Sanyukta, Mishrit) and by meaning (Svaekarthak, Nishedhaarthak, Prashnaarthak, etc.), sentence transformation.',
        keywords: ['Vakya', 'Sentence Hindi', 'Saral Vakya', 'Sanyukta Vakya', 'Mishrit Vakya', 'Vakya Bhed', 'Hindi Grammar'],
        type: 'grammar'
    },
    {
        dir: 'avayaya-shabada-vaibhaaga',
        name: 'Avyay - Shabd Vibhag (अव्यय)',
        hindiName: 'अव्यय - शब्द विभाग',
        description: 'Hindi Avyay (Indeclinable Words) — types: Kriyavisheshan, Sambandha-bodhak, Samucchay-bodhak, Vismayadibodhak — definitions, examples, and usage.',
        keywords: ['Avyay', 'Indeclinable Words Hindi', 'Kriyavisheshan', 'Samucchaybodhak', 'Vismayadibodhak', 'Hindi Grammar'],
        type: 'grammar'
    },
    {
        dir: 'upasaraga-evan-paratayaya',
        name: 'Upsarg aur Pratyay (उपसर्ग एवं प्रत्यय)',
        hindiName: 'उपसर्ग एवं प्रत्यय',
        description: 'Hindi Upsarg (Prefix) and Pratyay (Suffix) — Sanskrit, Hindi, Urdu, and English origin prefixes/suffixes, their meanings, and word formation rules.',
        keywords: ['Upsarg', 'Pratyay', 'Prefix Hindi', 'Suffix Hindi', 'Shabd Nirman', 'Hindi Grammar UP'],
        type: 'grammar'
    },
    {
        dir: 'samaasa-bhaeda-va-parakaara',
        name: 'Samas - Bhed aur Prakar (समास)',
        hindiName: 'समास - भेद व प्रकार',
        description: 'Hindi Samas (Compound Words) — 6 types: Avyayibhav, Tatpurush, Karmadharaya, Dwand, Bahuvrihi, Dvandva — definitions, Vigrah (breaking), and examples.',
        keywords: ['Samas', 'Compound Words Hindi', 'Tatpurush Samas', 'Dwand Samas', 'Bahuvrihi Samas', 'Samas Vigrah', 'Hindi Grammar'],
        type: 'grammar'
    },
    {
        dir: 'tarautai-evan-unakaa-saudhaara',
        name: 'Truti aur Unka Sudhar (त्रुटि सुधार)',
        hindiName: 'त्रुटि एवं उनका सुधार',
        description: 'Hindi Truti Sudhar (Error Correction) — common grammatical errors in Hindi sentences, rules for correction, gender/number/case/tense errors.',
        keywords: ['Truti Sudhar', 'Error Correction Hindi', 'Hindi Grammar Mistakes', 'Vaakya Shuddhi', 'UP Assistant Teacher Hindi'],
        type: 'grammar'
    },
    {
        dir: 'varatanaee-va-vaakaya-shaudadhai',
        name: 'Vartani aur Vakya Shuddhi (वर्तनी व शुद्धि)',
        hindiName: 'वर्तनी व वाक्य शुद्धि',
        description: 'Hindi Vartani (Spelling) and Vakya Shuddhi (Sentence Correction) — rules of correct Hindi spelling, common Vartani errors, and sentence purity.',
        keywords: ['Vartani', 'Vakya Shuddhi', 'Hindi Spelling', 'Hindi Sentence Correction', 'Shuddh Hindi', 'Hindi Grammar UP'],
        type: 'grammar'
    },
    {
        dir: 'shabada-rachanaa-va-shabada-bhandaara',
        name: 'Shabd Rachna aur Shabd Bhandar (शब्द भंडार)',
        hindiName: 'शब्द रचना व शब्द भंडार',
        description: 'Hindi Shabd Rachna (Word Formation) and Shabd Bhandar (Vocabulary) — Tatsam, Tadbhav, Deshaj, Videshi words, synonyms, antonyms, Anekarthi, Paryayvachi.',
        keywords: ['Shabd Rachna', 'Shabd Bhandar', 'Tatsam Tadbhav', 'Paryayvachi Shabd', 'Vilom Shabd', 'Anekarthi Shabd', 'Hindi Vocabulary'],
        type: 'grammar'
    },

    // --- SECTION 2: UNSEEN PROSE (अपठित गद्यांश) ---
    {
        dir: 'maukhaya-bhaava-vaishaya-va-shabadaaratha',
        name: 'Mukhya Bhav, Vishay aur Shabdarth (मुख्य भाव)',
        hindiName: 'मुख्य भाव, विषय व शब्दार्थ',
        description: 'Unseen Hindi Prose — identifying the central theme (Mukhya Bhav), subject (Vishay), and word meanings (Shabdarth) from an Apathit Gadyansh.',
        keywords: ['Apathit Gadyansh', 'Mukhya Bhav', 'Vishay', 'Shabdarth', 'Unseen Prose Hindi', 'UP Assistant Teacher'],
        type: 'prose'
    },
    {
        dir: 'vaakaya-sanshaodhana-va-vaakaya-vaishalaeshana',
        name: 'Vakya Sanshodhan aur Vishleshhan (वाक्य संशोधन)',
        hindiName: 'वाक्य संशोधन व वाक्य विश्लेषण',
        description: 'Unseen Hindi Prose — sentence correction (Vakya Sanshodhan) and sentence analysis (Vakya Vishleshhan) from a given passage.',
        keywords: ['Vakya Sanshodhan', 'Vakya Vishleshhan', 'Sentence Analysis Hindi', 'Apathit Gadyansh', 'Hindi Comprehension'],
        type: 'prose'
    },
    {
        dir: 'saaraansha-laekhana',
        name: 'Saransh Lekhan (सारांश लेखन)',
        hindiName: 'सारांश लेखन',
        description: 'Hindi Saransh Lekhan (Summary Writing) — condensing an unseen Hindi passage into a concise summary, key rules, steps, and model answers.',
        keywords: ['Saransh Lekhan', 'Summary Writing Hindi', 'Hindi Prasanshan', 'Apathit Gadyansh Summary', 'UP Assistant Teacher'],
        type: 'prose'
    },
    {
        dir: 'parashanaotatara-evan-vayaakhayaa',
        name: 'Prashnottarar aur Vyakhya (प्रश्नोत्तर)',
        hindiName: 'प्रश्नोत्तर एवं व्याख्या',
        description: 'Unseen Hindi Prose — answering comprehension questions (Prashnottarar) and explaining difficult words/phrases (Vyakhya) from a Gadyansh.',
        keywords: ['Prashnottarar', 'Vyakhya', 'Comprehension Questions Hindi', 'Apathit Gadyansh QA', 'Hindi Passage Questions'],
        type: 'prose'
    },
    {
        dir: 'anauvaada-evan-sankashaepana',
        name: 'Anuvaad aur Sankshepan (अनुवाद एवं संक्षेपण)',
        hindiName: 'अनुवाद एवं संक्षेपण',
        description: 'Hindi Anuvaad (Translation) and Sankshepan (Précis Writing) — translating passages and writing condensed versions with essential meaning preserved.',
        keywords: ['Anuvaad', 'Sankshepan', 'Translation Hindi', 'Précis Writing Hindi', 'Hindi Passage Condensation', 'UP Assistant Teacher'],
        type: 'prose'
    },
    {
        dir: 'laghau-utataraeeya-evan-vaisatarita-parashana',
        name: 'Laghu aur Vistarit Prashna (लघु/विस्तृत प्रश्न)',
        hindiName: 'लघु उत्तरीय एवं विस्तृत प्रश्न',
        description: 'Unseen Hindi Prose — short answer (Laghu Uttariya) and detailed answer (Vistarit Prashna) types, their word limits, structure, and model answers.',
        keywords: ['Laghu Uttariya Prashna', 'Vistarit Prashna', 'Short Answer Hindi', 'Long Answer Hindi', 'Apathit Gadyansh'],
        type: 'prose'
    },
    {
        dir: 'gadayaansha-kaee-bhaashaa-shaailaee-kaa-vaivarana',
        name: 'Gadyansh ki Bhasha Shaili ka Vivaran (भाषा शैली)',
        hindiName: 'गद्यांश की भाषा शैली का विवरण',
        description: 'Unseen Hindi Prose — analyzing the writing style (Bhasha Shaili) of a Gadyansh: descriptive, narrative, argumentative, expository, and satirical styles.',
        keywords: ['Bhasha Shaili', 'Language Style Hindi', 'Gadyansh Style Analysis', 'Varnanmak Shaili', 'Hindi Prose Style', 'UP Assistant Teacher'],
        type: 'prose'
    },
    {
        dir: 'bhaashaika-rachanaa-va-vayaakaranaika-parayaoga',
        name: 'Bhashik Rachna aur Vyakaranik Prayog (भाषिक रचना)',
        hindiName: 'भाषिक रचना व व्याकरणिक प्रयोग',
        description: 'Unseen Hindi Prose — identifying grammatical usage (Vyakaranik Prayog) within a passage: parts of speech, tense, voice, karak, and sentence structures.',
        keywords: ['Bhashik Rachna', 'Vyakaranik Prayog', 'Grammar in Passage Hindi', 'Apathit Gadyansh Grammar', 'Hindi Contextual Grammar'],
        type: 'prose'
    },

    // --- SECTION 3: POETRY PASSAGE (पद्यांश) ---
    {
        dir: 'kaavaya-kaa-maukhaya-bhaava-va-bhaavaaratha',
        name: 'Kavya ka Mukhya Bhav aur Bhavarth (काव्य भाव)',
        hindiName: 'काव्य का मुख्य भाव व भावार्थ',
        description: 'Hindi Poetry Passage — identifying the main sentiment (Mukhya Bhav) and emotional interpretation (Bhavarth) from an unseen Hindi poem (Padyansh).',
        keywords: ['Kavya Bhav', 'Bhavarth', 'Poetry Passage Hindi', 'Apathit Padyansh', 'Mukhya Bhav Kavya', 'UP Assistant Teacher'],
        type: 'poetry'
    },
    {
        dir: 'chhanda-va-chhandabadadhataa',
        name: 'Chhand aur Chhandbaddtha (छंद)',
        hindiName: 'छंद व छंदबद्धता',
        description: 'Hindi Chhand (Metre) — types: Maatrik (Doha, Chaupai, Soratha, Savaiya) and Varnik chhand, their syllable patterns, definitions, and identification in poems.',
        keywords: ['Chhand', 'Hindi Metre', 'Doha Chhand', 'Chaupai Chhand', 'Savaiya', 'Maatrik Varnik Chhand', 'Hindi Poetry Grammar'],
        type: 'poetry'
    },
    {
        dir: 'alankaara-bhaeda-va-udaaharana',
        name: 'Alankar - Bhed aur Udaharan (अलंकार)',
        hindiName: 'अलंकार - भेद व उदाहरण',
        description: 'Hindi Alankar (Figures of Speech) — Shabd Alankar (Anupras, Yamak, Shlesha) and Arth Alankar (Upma, Rupak, Utpreksha, Atishayokti) — definitions and examples.',
        keywords: ['Alankar', 'Figures of Speech Hindi', 'Shabd Alankar', 'Arth Alankar', 'Upma Alankar', 'Rupak Alankar', 'Hindi Poetry'],
        type: 'poetry'
    },
    {
        dir: 'rasa-vaibhaaga-sathaayaee-bhaava-va-udaaharana',
        name: 'Ras - Vibhag, Sthayi Bhav aur Udaharan (रस)',
        hindiName: 'रस - विभाग, स्थायी भाव व उदाहरण',
        description: 'Hindi Ras (Aesthetic Essence) — 9 Ras + Vatsalya Ras, Sthayi Bhav, Vibhav, Anubhav, Vyabhichari Bhav — definitions, examples from poems.',
        keywords: ['Ras', 'Nav Ras', 'Sthayi Bhav', 'Shringaar Ras', 'Veer Ras', 'Karuna Ras', 'Hindi Ras System', 'Hindi Poetry'],
        type: 'poetry'
    },
    {
        dir: 'kaavaya-chaetanaa-va-anaubhaootai',
        name: 'Kavya Chetna aur Anubhuti (काव्य चेतना)',
        hindiName: 'काव्य चेतना व अनुभूति',
        description: 'Hindi Kavya Chetna (Poetic Consciousness) and Anubhuti (Emotional Experience) — the poet\'s sensibility, objective, social message, and inner experience expressed through poems.',
        keywords: ['Kavya Chetna', 'Anubhuti', 'Poetic Consciousness', 'Emotional Experience Poetry', 'Hindi Poetry Analysis', 'UP Assistant Teacher'],
        type: 'poetry'
    },
    {
        dir: 'anaubhava-va-baimaba-vaidhaana',
        name: 'Anubhav aur Bimb Vidhan (अनुभव व बिम्ब)',
        hindiName: 'अनुभव व बिम्ब विधान',
        description: 'Hindi Anubhav (Behavior Manifestation) and Bimb Vidhan (Imagery) — types of Bimb (visual, auditory, tactile), their role and identification in poetry.',
        keywords: ['Anubhav', 'Bimb Vidhan', 'Imagery Hindi Poetry', 'Drishya Bimb', 'Shravya Bimb', 'Poetic Imagery', 'Hindi Poetry UP'],
        type: 'poetry'
    },
    {
        dir: 'kaavaya-rachanaa-va-parakaara',
        name: 'Kavya Rachna aur Prakar (काव्य रचना)',
        hindiName: 'काव्य रचना व प्रकार',
        description: 'Hindi Kavya Rachna (Poetry Composition) — types: Prasthanbhed (Shravan vs. Darshan Kavya), Drishya Kavya, Shravya Kavya, Mahakavya, Khandakavya, Muktak.',
        keywords: ['Kavya Rachna', 'Kavya Prakar', 'Mahakavya', 'Khandakavya', 'Muktak', 'Shravan Kavya', 'Drishya Kavya', 'Hindi Poetry Types'],
        type: 'poetry'
    },
    {
        dir: 'kaavaya-kae-vaibhainana-raoopa-va-vaidhaaen',
        name: 'Kavya ke Vibhinn Roop aur Vidhaen (काव्य रूप)',
        hindiName: 'काव्य के विभिन्न रूप व विधाएं',
        description: 'Hindi Kavya Roop — different forms and genres: SoneT, Ghazal, Rubai, Doha, Chaupai, Pad, Geet, Navgeet, Muktchhanda Kavita — definitions and examples.',
        keywords: ['Kavya Roop', 'Kavya Vidha', 'Ghazal', 'Doha', 'Pad', 'Geet', 'Muktchhanda', 'Hindi Poetry Forms', 'UP Assistant Teacher'],
        type: 'poetry'
    },
    {
        dir: 'kavai-paraichaya-va-kaavaya-gauna',
        name: 'Kavi Parichay aur Kavya Gun (कवि परिचय)',
        hindiName: 'कवि परिचय व काव्य गुण',
        description: 'Hindi Kavi Parichay (Poet Introduction) and Kavya Gun (Poetic Qualities) — the three Guna: Madhura, Ojasvi, Prasad; how they manifest in poetry; linking poets to their Guna.',
        keywords: ['Kavi Parichay', 'Kavya Gun', 'Madhura Gun', 'Ojasvi Gun', 'Prasad Gun', 'Poet Introduction Hindi', 'Hindi Poetry UP'],
        type: 'poetry'
    },
    {
        dir: 'kaavaya-kaa-sandaesha-va-saamaajaika-parabhaava',
        name: 'Kavya ka Sandesh aur Samajik Prabhav (काव्य संदेश)',
        hindiName: 'काव्य का संदेश व सामाजिक प्रभाव',
        description: 'Hindi Poetry\'s social message (Sandesh) and societal impact (Samajik Prabhav) — how literary works reflect social reform, patriotism, and human values.',
        keywords: ['Kavya Sandesh', 'Samajik Prabhav', 'Social Message Poetry', 'Patriotic Poetry Hindi', 'Hindi Literature Society', 'UP Assistant Teacher'],
        type: 'poetry'
    },

    // --- SECTION 4: HINDI LITERATURE (हिंदी साहित्य) ---
    {
        dir: 'bhaarataenadau-haraishachandara-naataka-va-samaaja-saudhaara',
        name: 'Bhartendu Harishchandra - Natak aur Samaj Sudhar (भारतेन्दु)',
        hindiName: 'भारतेन्दु हरिश्चंद्र - नाटक व समाज सुधार',
        description: 'Bhartendu Harishchandra — father of modern Hindi literature, major plays (Andher Nagari, Bharat Durdasha), social reform themes, Bhartendu Yug.',
        keywords: ['Bhartendu Harishchandra', 'Andher Nagari', 'Bharat Durdasha', 'Bhartendu Yug', 'Modern Hindi Literature', 'Hindi Drama'],
        type: 'literature'
    },
    {
        dir: 'mahaavaeera-parasaada-davaivaedaee-sarasavataee-pataraikaa',
        name: 'Mahaveer Prasad Dwivedi - Saraswati Patrika (द्विवेदी)',
        hindiName: 'महावीर प्रसाद द्विवेदी - सरस्वती पत्रिका',
        description: 'Mahaveer Prasad Dwivedi — Dwivedi Yug, Saraswati Patrika, standardization of Hindi prose, Khariboli movement, major works and their significance.',
        keywords: ['Mahaveer Prasad Dwivedi', 'Saraswati Patrika', 'Dwivedi Yug', 'Khariboli Hindi', 'Hindi Prose Standardization', 'Hindi Literature'],
        type: 'literature'
    },
    {
        dir: 'maaithailaeesharana-gaupata-saakaeta-yashaodharaa',
        name: 'Maithilisharan Gupt - Saket, Yashodhara (मैथिलीशरण गुप्त)',
        hindiName: 'मैथिलीशरण गुप्त - साकेत, यशोधरा',
        description: 'Maithilisharan Gupt — Rashtra Kavi, major works (Saket, Yashodhara, Bharat Bharati), themes of nationalism, spirituality, and glorification of Indian women.',
        keywords: ['Maithilisharan Gupt', 'Saket', 'Yashodhara', 'Bharat Bharati', 'Rashtra Kavi', 'Dwivedi Yug Poetry', 'Hindi Epic'],
        type: 'literature'
    },
    {
        dir: 'jayashankara-parasaada-kaamaayanaee-sakandagaupata',
        name: 'Jaishankar Prasad - Kamayani, Skandagupta (जयशंकर प्रसाद)',
        hindiName: 'जयशंकर प्रसाद - कामायनी, स्कंदगुप्त',
        description: 'Jaishankar Prasad — Chhaayavaad pillar, Kamayani (Shraddha-Manu-Ida), Skandagupta, Chandragupta — themes, characters, and literary significance.',
        keywords: ['Jaishankar Prasad', 'Kamayani', 'Skandagupta', 'Chandragupta', 'Chhaayavaad', 'Hindi Mahakavya', 'Hindi Drama'],
        type: 'literature'
    },
    {
        dir: 'saoorayakaanta-taraipaathaee-nairaalaa-raama-kaee-shakatai-paoojaa',
        name: "Suryakant Tripathi 'Nirala' - Ram ki Shakti Puja (निराला)",
        hindiName: "सूर्यकांत त्रिपाठी 'निराला' - राम की शक्ति पूजा",
        description: "Suryakant Tripathi 'Nirala' — Chhaayavaad rebel, free verse (Muktchhanda), Ram ki Shakti Puja, Saroj Smriti — themes, style, rebellion against tradition.",
        keywords: ["Suryakant Tripathi Nirala", "Ram ki Shakti Puja", "Saroj Smriti", "Muktchhanda Poetry", "Chhaayavaad", "Hindi Free Verse"],
        type: 'literature'
    },
    {
        dir: 'saumaitaraanandana-panta-chaidanbaraa',
        name: 'Sumitranandan Pant - Chidambara (सुमित्रानंदन पंत)',
        hindiName: 'सुमित्रानंदन पंत - चिदंबरा',
        description: 'Sumitranandan Pant — nature poet of Chhaayavaad, Chidambara (Sahitya Akademi award), Pallav, Gunjan — themes of beauty, nature, and philosophical exploration.',
        keywords: ['Sumitranandan Pant', 'Chidambara', 'Pallav', 'Gunjan', 'Chhaayavaad Nature Poetry', 'Hindi Romantic Poetry'],
        type: 'literature'
    },
    {
        dir: 'mahaadaevaee-varamaa-yaamaa-naeerajaa',
        name: 'Mahadevi Verma - Yama, Nirja (महादेवी वर्मा)',
        hindiName: 'महादेवी वर्मा - यामा, नीरजा',
        description: 'Mahadevi Verma — Modern Meera, Chhaayavaad poet, Yama, Nirja, Ateet ke Chalchitra — pain, devotion, mystic love themes; prose writings; Sahitya Akademi award.',
        keywords: ['Mahadevi Verma', 'Yama', 'Nirja', 'Ateet ke Chalchitra', 'Modern Meera', 'Chhaayavaad Woman Poet', 'Hindi Literature'],
        type: 'literature'
    },
    {
        dir: 'maunshaee-paraemachanda-gaodaana-kaphana-pancha-paramaeshavara',
        name: 'Munshi Premchand - Godaan, Kafan, Panch Parmeshwar (प्रेमचंद)',
        hindiName: 'मुंशी प्रेमचंद - गोदान, कफन, पंच परमेश्वर',
        description: 'Munshi Premchand — father of Modern Hindi fiction, Godaan (Hori-Dhania), Kafan, Panch Parmeshwar, Nirmala — social realism, peasant life, and moral themes.',
        keywords: ['Munshi Premchand', 'Godaan', 'Kafan', 'Panch Parmeshwar', 'Hindi Novel', 'Hindi Short Story', 'Social Realism Hindi'],
        type: 'literature'
    },
    {
        dir: 'yashapaala-jhaoothaa-sacha-daivayaa',
        name: 'Yashpal - Jhootha Sach, Divya (यशपाल)',
        hindiName: 'यशपाल - झूठा सच, दिव्या',
        description: 'Yashpal — progressive writer, Jhootha Sach (partition saga), Divya, Dada Comrade — themes of partition, social inequality, Marxism, and historical fiction.',
        keywords: ['Yashpal', 'Jhootha Sach', 'Divya', 'Dada Comrade', 'Progressive Hindi Fiction', 'Partition Novel Hindi', 'Pragativad'],
        type: 'literature'
    },
    {
        dir: 'sachachaidaananda-haeeraananda-vaatasayaayana-ajanyaeya-kavaitaa-va-upanayaasa',
        name: "Sacchhidanand Hiranand Vatsyayan 'Agyeya' - Kavita aur Upanyas (अज्ञेय)",
        hindiName: "सच्चिदानंद हीरानंद वात्स्यायन 'अज्ञेय' - कविता व उपन्यास",
        description: "Agyeya (S.H. Vatsyayan) — Prayogvaad pioneer, Shekhar: Ek Jeevani, Nadi ke Dweep — individualism, existentialism; Taar Saptak anthology founder.",
        keywords: ["Agyeya", "Sacchhidanand Vatsyayan", "Shekhar Ek Jeevani", "Nadi ke Dweep", "Taar Saptak", "Prayogvaad", "Hindi Experimental Poetry"],
        type: 'literature'
    },
    {
        dir: 'bhakataikaala-kabaeeradaasa-taulasaeedaasa-saooradaasa',
        name: 'Bhaktikal - Kabirdas, Tulsidas, Surdas (भक्तिकाल)',
        hindiName: 'भक्तिकाल - कबीरदास, तुलसीदास, सूरदास',
        description: 'Hindi Bhaktikal (Devotional Period 1300-1700) — Kabirdas (Dohe, Sakhi), Tulsidas (Ramcharitmanas), Surdas (Sursagar) — their philosophy, works, and impact.',
        keywords: ['Bhaktikal', 'Kabirdas', 'Tulsidas', 'Surdas', 'Ramcharitmanas', 'Sursagar', 'Hindi Medieval Literature', 'Bhakti Movement Poetry'],
        type: 'literature'
    },
    {
        dir: 'raeetaikaala-kaeshavadaasa-baihaaraee-bhaooshana',
        name: 'Ritikal - Keshavdas, Bihari, Bhushan (रीतिकाल)',
        hindiName: 'रीतिकाल - केशवदास, बिहारी, भूषण',
        description: 'Hindi Ritikal (Decorative Period 1650-1850) — Keshavdas (Ramchandrika), Bihari (Bihari Satsai), Bhushan (Shivabavani) — Shringaar, Veerbhav, poetic craft.',
        keywords: ['Ritikal', 'Keshavdas', 'Bihari Satsai', 'Bhushan', 'Shivabavani', 'Ritibaddha Poetry', 'Hindi Classical Literature'],
        type: 'literature'
    },
    {
        dir: 'chhaayaavaada-kae-chaara-paramaukha-satanbha',
        name: 'Chhaayavaad ke Chaar Pramukh Stambh (छायावाद)',
        hindiName: 'छायावाद के चार प्रमुख स्तंभ',
        description: 'Hindi Chhaayavaad (Neo-Romanticism 1918-1936) — the four pillars: Jaishankar Prasad, Suryakant Tripathi Nirala, Sumitranandan Pant, Mahadevi Verma — key features and themes.',
        keywords: ['Chhaayavaad', 'Chhayavad Pillars', 'Hindi Neo-Romanticism', 'Chhaayavaad Features', 'Hindi Modern Poetry Period', 'Prasad Nirala Pant Mahadevi'],
        type: 'literature'
    },
    {
        dir: 'paragataivaada-evan-parayaogavaada',
        name: 'Pragativad aur Prayogvad (प्रगतिवाद एवं प्रयोगवाद)',
        hindiName: 'प्रगतिवाद एवं प्रयोगवाद',
        description: 'Hindi Pragativad (Progressivism, 1936+) and Prayogvad (Experimentalism, 1943+) — key features, major poets/writers, Taar Saptak, social and ideological differences.',
        keywords: ['Pragativad', 'Prayogvad', 'Progressive Literature Hindi', 'Experimental Hindi Poetry', 'Taar Saptak', 'Nai Kavita', 'Hindi Literary Movements'],
        type: 'literature'
    },
    {
        dir: 'samakaalaeena-saahaitaya-haraivansha-raaya-bachachana-kamalaeshavara',
        name: 'Samkalin Sahitya - Harivansh Rai Bachchan, Kamleshwar (समकालीन साहित्य)',
        hindiName: 'समकालीन साहित्य - हरिवंश राय बच्चन, कमलेश्वर',
        description: 'Contemporary Hindi Literature — Harivansh Rai Bachchan (Madhushala, Madhubala), Kamleshwar (Kitne Pakistan), Nayi Kavita, Nayi Kahani movement.',
        keywords: ['Harivansh Rai Bachchan', 'Madhushala', 'Kamleshwar', 'Kitne Pakistan', 'Nayi Kavita', 'Nayi Kahani', 'Contemporary Hindi Literature'],
        type: 'literature'
    }
];

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

// ============================================================================
// GEMINI API CLIENT
// ============================================================================
async function callGemini(prompt, retries = MAX_RETRIES) {
    for (let attempt = 1; attempt <= retries; attempt++) {
        try {
            const url = `https://generativelanguage.googleapis.com/v1beta/models/${currentModel}:generateContent?key=${apiKey}`;
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    contents: [{ parts: [{ text: prompt }] }],
                    generationConfig: {
                        temperature: 0.7,
                        maxOutputTokens: 65536,
                        topP: 0.95,
                    },
                }),
            });

            if (res.status === 429 || res.status === 403) {
                console.log(`  ⚠️ Rate limited. Waiting before retry ${attempt}/${retries}...`);
                const wait = 15000 * Math.pow(2, attempt - 1);
                console.log(`  ⏳ Waiting ${wait / 1000}s...`);
                await sleep(wait);
                continue;
            }

            if (res.status === 503) {
                const wait = REQUEST_DELAY_MS * 2;
                console.log(`  ⏳ Service unavailable (503). Waiting ${wait / 1000}s before retry ${attempt}/${retries}...`);
                await sleep(wait);
                continue;
            }

            if (!res.ok) {
                const errBody = await res.text();
                throw new Error(`Gemini API error ${res.status}: ${errBody.substring(0, 200)}`);
            }

            const data = await res.json();
            const text = data?.candidates?.[0]?.content?.parts?.[0]?.text || '';
            if (!text || text.trim().length === 0) throw new Error('Empty response from API');
            return text;
        } catch (err) {
            if (attempt === retries) throw err;
            console.log(`  ⚠️ Retry ${attempt}/${retries} after error: ${err.message}`);
            await sleep(5000);
        }
    }
    throw new Error('Max retries exceeded');
}

// ============================================================================
// JSON PARSER
// ============================================================================
function parseResponse(raw) {
    if (!raw || typeof raw !== 'string') throw new Error('Invalid response: expected string, got ' + typeof raw);

    let cleaned = raw.trim();
    if (cleaned.startsWith('```json')) cleaned = cleaned.replace(/^```json\s*/, '').replace(/\s*```$/, '');
    else if (cleaned.startsWith('```')) cleaned = cleaned.replace(/^```\s*/, '').replace(/\s*```$/, '');

    cleaned = cleaned.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');

    try { return JSON.parse(cleaned); } catch (err) { }

    const jsonMatch = cleaned.match(/[\{\[][^\s][\s\S]*[\}\]]/);
    if (jsonMatch) {
        const repaired = jsonMatch[0]
            .replace(/(\{|,|\[|\s)([A-Za-z0-9_\-]+)\s*:/g, '$1"$2":')
            .replace(/'([^'\\]*(?:\\.[^'\\]*)*)'/g, '"$1"')
            .replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(repaired); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + repaired + ')')()) ; } catch (e2) { }
        }
    }

    const jsonStart = cleaned.indexOf('{');
    if (jsonStart >= 0) {
        let partial = cleaned.substring(jsonStart);
        partial = partial.replace(/,\s*$/, '');
        let opens = 0, closes = 0, openArr = 0, closeArr = 0;
        let inString = false, escape = false;
        for (let i = 0; i < partial.length; i++) {
            const ch = partial[i];
            if (escape) { escape = false; continue; }
            if (ch === '\\') { escape = true; continue; }
            if (ch === '"') { inString = !inString; continue; }
            if (inString) continue;
            if (ch === '{') opens++;
            else if (ch === '}') closes++;
            else if (ch === '[') openArr++;
            else if (ch === ']') closeArr++;
        }
        if (inString) partial += '"';
        while (openArr > closeArr) { partial += ']'; closeArr++; }
        while (opens > closes) { partial += '}'; closes++; }
        partial = partial.replace(/,\s*([}\]])/g, '$1');
        try { return JSON.parse(partial); } catch (e) {
            try { return JSON.parse(Function('"use strict"; return (' + partial + ')')()) ; } catch (e2) { }
        }
    }

    console.error('❌ Raw response (first 500 chars):', cleaned.substring(0, 500));
    throw new Error('No valid JSON found in response');
}

// ============================================================================
// PROMPT BUILDER — Concepts/Theories Tab (ENGLISH ONLY, NO PARAGRAPHS)
// ============================================================================
function buildConceptsPrompt(topic) {
    let focusInstructions = '';

    if (topic.type === 'literature') {
        focusInstructions = `Since this is a Hindi LITERATURE topic:
- Focus on the **author/poet's life, literary period (Yug), key works with themes, style, characters/plot, famous quotes/lines, and literary significance**.
- In SECTION 2 (Concepts and Theories), structure subcards around: Author Biography, Literary Period/Movement (Yug), Major Works & Themes, Literary Style & Features, Important Lines/Quotes, and Impact on Hindi Literature.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) List of major works, their type (Kavya/Upanyas/Katha/Natak), year, and genre.
  b) Important characters (for prose) OR famous verses/lines (for poetry) with their source.
  c) Key literary features, movement (Yug), and contemporaries.
  d) Previous exam questions linked to this author/work.`;
    } else if (topic.type === 'grammar') {
        focusInstructions = `Since this is a Hindi GRAMMAR topic:
- Focus on **definitions, classification rules, structural formulas, exceptions, and identification techniques**.
- In SECTION 2 (Concepts and Theories), structure subcards around: Core Definition, Classification/Types (Bhed), Rules of Usage, Structural Formulas, Common Exceptions, and Identification Tricks.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) All types/sub-types with definitions and Hindi examples.
  b) Comparison table of similar/confused types.
  c) Step-by-step identification/application method.
  d) Common exam question patterns for this grammar concept.`;
    } else if (topic.type === 'prose') {
        focusInstructions = `Since this is an Apathit GADYANSH (Unseen Prose) skill topic:
- Focus on **comprehension strategies, answering techniques, key skills, and step-by-step methods**.
- In SECTION 2 (Concepts and Theories), structure subcards around: What This Skill Tests, Step-by-Step Approach, Key Skills Required, Marking Scheme Awareness, Common Answer Patterns, and Dos and Don'ts.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) Types of questions asked in this category.
  b) Answer format/structure with word-limit guidelines.
  c) Key language features to look for in a passage.
  d) Common errors in answering this type of question.`;
    } else { // poetry
        focusInstructions = `Since this is an Apathit PADYANSH (Unseen Poetry) or Kavya-Shastra topic:
- Focus on **poetic concepts, analysis strategies, classification of forms/types, and identification techniques**.
- In SECTION 2 (Concepts and Theories), structure subcards around: Core Concept Definition, Types/Classification with examples, Identification Method, Analysis Approach (for poetry passages), Key Rules/Formulas, and Memorization Tricks.
- In SECTION 3 (Important Facts and Data), include tables detailing:
  a) All types/forms with Hindi examples from classic poets.
  b) Key identification signals and distinguishing features.
  c) Famous examples and source poets for each type.
  d) Exam question patterns and expected answer formats.`;
    }

    return `You are an expert faculty member for UP Assistant Teacher (हिंदी) exam preparation. Create ULTRA-COMPREHENSIVE, EXAM-FOCUSED concept notes for the topic: "${topic.name}" (${topic.hindiName}).

TOPIC CONTEXT:
- Subject: Hindi (हिंदी)
- Exam: UP Assistant Teacher Recruitment Examination
- Topic Directory: ${topic.dir}
- Topic Type: ${topic.type} (grammar/prose/poetry/literature)
- Keywords to target: ${topic.keywords.join(', ')}

${focusInstructions}

CRITICAL FORMAT RULES — NO PARAGRAPHS ALLOWED:
1. **STRICTLY NO PARAGRAPHS** — Do NOT use the "paragraph" type anywhere. Every section must be a table, list, or subcards.
2. Content must be **point-wise, bulleted, tabular, and structured** for rapid exam revision.
3. Use **bold** for key terms, names, dates, Hindi terms, and figures within table cells and list items.
4. Content must be **comprehensive and exam-focused** — cover ALL important facts, concepts, and principles that UP Assistant Teacher exam asks.
5. **LANGUAGE: Use ENGLISH ONLY** for all content including headers, rows, and items. Hindi words/terms may appear in bold within English text (e.g., "**Doha** (a rhyming couplet)").

REQUIRED SECTION STRUCTURE (in this exact order):

SECTION 1 — "Detailed Brief Overview" (type: "table")
- A comprehensive overview table with 8-10 rows covering: What/Who, Era/Period, Why Important, Key Features, Sub-types/Major Works, Significance for UP Exam, and other essential facts.
- Headers: ["Aspect", "Key Details"]

SECTION 2 — "Concepts and Theories" (type: "subcards")
- 5-7 subcards, each covering a major sub-topic or theme.
- Each subcard must have a title and detailed point-wise content (NOT paragraphs).
- Include at least 2-3 powerful mnemonics within these subcards.

SECTION 3 — "Important Facts and Data" (type: "table")
- 3-4 detailed tables with 8-12 rows each covering the details specified in the focus instructions above.

SECTION 4 — "Tricks to Remember" (type: "list")
- 6-8 items with "term" = trick title, "definition" = detailed trick explanation
- Include memory tricks, acronyms, association techniques, and quick recall methods in English

SECTION 5 — "Mistakes to Avoid" (type: "list")
- 6-8 items with "term" = common mistake, "definition" = correct fact/rule and why students get confused
- Cover frequently confused concepts and common exam errors

SECTION 6 — "Point-wise Detailed Summary" (type: "list")
- 10-15 items with "term" = key point title, "definition" = concise point-wise summary
- This is the final revision summary covering ALL essential facts

ADDITIONAL REQUIREMENTS:
- "upscNotes": Include 4-6 notes with type "tip" (exam strategy) and "trap" (common traps)
- "keyTakeaways": Include 5-8 concise, high-yield takeaways

OUTPUT FORMAT — Return ONLY valid JSON with this exact structure:
{
  "sections": [
    {
      "title": "Detailed Brief Overview",
      "type": "table",
      "headers": ["Aspect", "Key Details"],
      "rows": [
        ["Aspect 1", "**Key detail** with bold important terms"],
        ["Aspect 2", "Another **important** detail"]
      ]
    },
    {
      "title": "Concepts and Theories",
      "type": "subcards",
      "items": [
        {
          "title": "Sub-topic 1 with **mnemonic**",
          "content": "• Point 1 with **bold** terms\\n• Point 2 with **bold** terms\\n• **Mnemonic:** Phrase to remember"
        }
      ]
    },
    {
      "title": "Important Facts and Data",
      "type": "table",
      "headers": ["Column 1", "Column 2", "Column 3"],
      "rows": [
        ["Data 1", "Data 2", "Data 3"]
      ]
    },
    {
      "title": "Tricks to Remember",
      "type": "list",
      "items": [
        {
          "term": "Trick 1: Title",
          "definition": "Detailed explanation of the trick with **bold** key terms"
        }
      ]
    },
    {
      "title": "Mistakes to Avoid",
      "type": "list",
      "items": [
        {
          "term": "Mistake 1: Common error",
          "definition": "Correct fact and why students get confused"
        }
      ]
    },
    {
      "title": "Point-wise Detailed Summary",
      "type": "list",
      "items": [
        {
          "term": "Key Point 1",
          "definition": "Concise summary point with **bold** key terms"
        }
      ]
    }
  ],
  "upscNotes": [
    {
      "type": "tip",
      "content": "Exam strategy tip for UP Assistant Teacher Hindi"
    },
    {
      "type": "trap",
      "content": "Common trap students fall into"
    }
  ],
  "keyTakeaways": [
    "High-yield takeaway 1",
    "High-yield takeaway 2"
  ]
}

IMPORTANT:
- Use ENGLISH as the primary language. Hindi words/terms should appear bolded within English sentences.
- Every section must be comprehensive and detailed — this is for serious exam preparation.
- Include ALL important facts, figures, names, dates, rules, and concepts.
- The content must be exam-focused with keywords naturally embedded.
- NO paragraphs anywhere — only tables, lists, and subcards.`;
}

// ============================================================================
// FALLBACK CONCEPTS DATA
// ============================================================================
function buildFallbackConcepts(topic) {
    return {
        sections: [
            {
                title: 'Detailed Brief Overview',
                type: 'table',
                headers: ['Aspect', 'Key Details'],
                rows: [
                    ['Topic', `**${topic.name}** (${topic.hindiName})`],
                    ['Subject', '**Hindi (हिंदी)** for UP Assistant Teacher'],
                    ['Status', 'Content under preparation — check back soon for comprehensive notes']
                ]
            }
        ],
        upscNotes: [
            { type: 'tip', content: `This topic is important for UP Assistant Teacher exam. Study ${topic.name} thoroughly.` }
        ],
        keyTakeaways: [
            `Study ${topic.name} thoroughly for UP Assistant Teacher`,
            'Focus on important concepts, facts, and principles',
            'Practice with previous year questions'
        ]
    };
}

// ============================================================================
// MAIN GENERATION LOOP
// ============================================================================
async function main() {
    console.log('╔══════════════════════════════════════════════════════════════╗');
    console.log('║ UP Assistant Teacher - Hindi Microtopics Generator           ║');
    console.log(`║ Model: ${currentModel}                                          ║`);
    console.log('╚══════════════════════════════════════════════════════════════╝\n');

    const totalTopics = MICROTOPICS.length;
    let successCount = 0;
    let failCount = 0;

    for (let i = 0; i < totalTopics; i++) {
        const topic = MICROTOPICS[i];
        console.log(`\n${'='.repeat(80)}`);
        console.log(`[${i + 1}/${totalTopics}] Processing: ${topic.name} [Type: ${topic.type}]`);
        console.log(`${'='.repeat(80)}`);

        const outputDir = path.join(process.cwd(), 'up-assistant-teacher', 'hindi', topic.dir);
        fs.mkdirSync(outputDir, { recursive: true });

        const tabsDir = path.join(outputDir, 'tabs');
        fs.mkdirSync(tabsDir, { recursive: true });

        let conceptsData = null;

        try {
            console.log('  📝 Generating concepts/theories content...');
            const prompt = buildConceptsPrompt(topic);
            const raw = await callGemini(prompt);
            const parsed = parseResponse(raw);

            if (!parsed.sections || !Array.isArray(parsed.sections) || parsed.sections.length === 0) {
                throw new Error('Generated content missing "sections" array');
            }

            // Ensure no paragraph type sections
            const paragraphSections = parsed.sections.filter(s => s.type === 'paragraph');
            if (paragraphSections.length > 0) {
                console.log('  ⚠️ Found paragraph sections — converting to list format...');
                parsed.sections = parsed.sections.map(section => {
                    if (section.type === 'paragraph') {
                        return {
                            title: section.title,
                            type: 'list',
                            items: [{ term: 'Key Point', definition: section.content || '' }]
                        };
                    }
                    return section;
                });
            }

            conceptsData = parsed;
            console.log('  ✅ Concepts content generated successfully!');

            fs.writeFileSync(path.join(tabsDir, 'concepts.json'), JSON.stringify(conceptsData, null, 2), 'utf8');
            console.log('  💾 Saved tabs/concepts.json');

            successCount++;
        } catch (err) {
            console.error(`  ❌ Failed to generate concepts: ${err.message}`);
            conceptsData = buildFallbackConcepts(topic);
            failCount++;
        }

        // Generate index.html with 4-tab structure
        const html = assembleMicrotopicPage(topic, conceptsData);
        fs.writeFileSync(path.join(outputDir, 'index.html'), html, 'utf8');
        console.log('  💾 Saved index.html');

        // Save data.json
        fs.writeFileSync(path.join(outputDir, 'data.json'), JSON.stringify({
            concepts: conceptsData,
            practice: null,
            pyqs: null,
            test: null
        }, null, 2), 'utf8');
        console.log('  💾 Saved data.json');

        console.log(`  🎉 Completed: ${topic.name}`);

        if (i < totalTopics - 1) {
            console.log(`  ⏳ Waiting ${REQUEST_DELAY_MS / 1000}s before next topic...`);
            await sleep(REQUEST_DELAY_MS);
        }
    }

    console.log(`\n${'='.repeat(80)}`);
    console.log(`📊 SUMMARY: ${successCount} succeeded, ${failCount} failed out of ${totalTopics} topics`);
    console.log(`${'='.repeat(80)}`);
    console.log('\n✅ All Hindi microtopic pages generated successfully!');
    console.log('📁 Microtopic folders created under: up-assistant-teacher/hindi/');
}

// ============================================================================
// HTML PAGE ASSEMBLER — 4-Tab Structure for Microtopics
// ============================================================================
function assembleMicrotopicPage(topic, conceptsData) {
    const now = new Date().toISOString();
    const canonicalUrl = `https://sjmaths.com/up-assistant-teacher/hindi/${topic.dir}/`;
    const title = `${topic.hindiName} | हिन्दी | SJMaths`;
    const description = topic.description;

    return `<!DOCTYPE html>
<html lang="hi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <meta name="description" content="${description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="${canonicalUrl}">
    <meta name="keywords" content="${topic.keywords.join(', ')}, UP Assistant Teacher, हिन्दी, Hindi">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">
    <meta property="og:title" content="${title}">
    <meta property="og:description" content="${description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="${canonicalUrl}">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="${title}">
    <meta name="twitter:description" content="${description}">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.95);
            --glass-border: rgba(255, 255, 255, 0.2);
            --shadow-lg: 0 10px 30px -5px rgba(212, 175, 55, 0.1);
            --accent-gradient: linear-gradient(135deg, #d4af37, #c0392b);
        }
        body.dark-mode {
            --glass-bg: rgba(30, 30, 46, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.3);
        }
        .topic-container {
            max-width: 1100px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }
        .breadcrumbs {
            margin-bottom: 1.5rem;
            font-size: 0.88rem;
            color: #64748b;
            background: rgba(255, 255, 255, 0.6);
            display: inline-block;
            padding: 0.6rem 1.2rem;
            border-radius: 999px;
            border: 1px solid rgba(0, 0, 0, 0.04);
        }
        .breadcrumbs a {
            color: #d4af37;
            text-decoration: none;
            font-weight: 500;
        }
        .breadcrumbs a:hover { text-decoration: underline; }
        .breadcrumbs i {
            margin: 0 0.5rem;
            font-size: 0.7rem;
            color: #94a3b8;
        }
        .topic-header {
            background: linear-gradient(135deg, rgba(212, 175, 55, 0.03), rgba(192, 57, 43, 0.03));
            border: 1px solid rgba(212, 175, 55, 0.1);
            border-radius: 1.25rem;
            padding: 2.5rem;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .topic-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: clamp(1.8rem, 5vw, 2.5rem);
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
            line-height: 1.2;
        }
        .topic-desc {
            color: #475569;
            font-size: 1rem;
            line-height: 1.7;
            max-width: 700px;
            margin: 0 auto;
        }
        .topic-meta-bar {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            align-items: center;
            margin-top: 1.5rem;
            padding-top: 1.25rem;
            border-top: 1px solid rgba(0, 0, 0, 0.05);
        }
        .back-link {
            display: inline-block;
            margin-bottom: 1.5rem;
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .back-link:hover { text-decoration: underline; }
        .study-tabs {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            padding: 0.55rem;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            margin-bottom: 2rem;
            position: sticky;
            top: 88px;
            z-index: 100;
            backdrop-filter: blur(16px);
            justify-content: center;
        }
        .tab-btn {
            border: none;
            background: transparent;
            color: #475569;
            padding: 0.65rem 1.1rem;
            border-radius: 999px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9rem;
            font-family: 'Outfit', sans-serif;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            white-space: nowrap;
        }
        .tab-btn:hover {
            background: rgba(212, 175, 55, 0.08);
            color: #d4af37;
        }
        .tab-btn.active {
            background: var(--accent-gradient);
            color: #ffffff;
            box-shadow: 0 8px 20px rgba(212, 175, 55, 0.25);
        }
        .topic-content { min-height: 400px; }
        .tab-panel { display: none; animation: slideUp 0.4s ease-out; }
        .tab-panel.active { display: block; }
        .content-card {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: var(--shadow-lg);
        }
        .content-card h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.3rem;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .content-card h2 i { color: #d4af37; }
        .content-card p, .content-card li {
            font-size: 0.95rem;
            color: var(--text-light);
            line-height: 1.7;
        }
        .content-card ul { margin: 0.5rem 0; padding-left: 1.5rem; }
        .content-card li { margin-bottom: 0.5rem; }
        @media (max-width: 768px) {
            .study-tabs {
                flex-wrap: nowrap;
                overflow-x: auto;
                -webkit-overflow-scrolling: touch;
                padding: 0.4rem;
                scrollbar-width: none;
                justify-content: flex-start;
            }
            .study-tabs::-webkit-scrollbar { display: none; }
            .tab-btn { font-size: 0.85rem; padding: 0.5rem 0.9rem; }
            .topic-container { padding: 0 1rem 2rem; }
            .topic-header { padding: 1.5rem 1rem; }
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes slideUp {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <a href="/up-assistant-teacher/hindi/" class="back-link"><i class="fas fa-arrow-left"></i> <span class="lang-hi">वापस हिन्दी पर जाएँ</span><span class="lang-en">Back to Hindi</span></a>

        <div class="breadcrumbs">
            <a href="/">Home</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/">UP Assistant Teacher</a> <i class="fas fa-chevron-right"></i>
            <a href="/up-assistant-teacher/hindi/">हिन्दी</a> <i class="fas fa-chevron-right"></i>
            <span>${topic.hindiName}</span>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-hi">${topic.hindiName}</span>
                <span class="lang-en">${topic.name}</span>
            </h1>
            <p class="topic-desc">
                <span class="lang-hi">${topic.description}</span>
                <span class="lang-en">${topic.description}</span>
            </p>
            <div class="topic-meta-bar">
                <span style="display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; background: rgba(245, 158, 11, 0.1); color: #b45309; border: 1px solid rgba(245, 158, 11, 0.2);">
                    <i class="fas fa-signal"></i> <span class="lang-hi">मध्यम</span><span class="lang-en">Medium</span>
                </span>
                <span style="display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600; color: #475569; background: rgba(100, 116, 139, 0.06); border: 1px solid rgba(100, 116, 139, 0.12);">
                    <i class="fas fa-clock"></i> <span class="lang-hi">कुल 45 मिनट</span><span class="lang-en">45 min total</span>
                </span>
            </div>
        </div>

        <!-- Tabs Navigation -->
        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="tab-concepts" role="tab" aria-selected="true">
                <i class="fas fa-book-open"></i>
                <span class="lang-hi">1. अवधारणाएँ एवं सिद्धांत</span>
                <span class="lang-en">1. Concepts &amp; Theories</span>
            </button>
            <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
                <i class="fas fa-list-check"></i>
                <span class="lang-hi">2. अभ्यास प्रश्न</span>
                <span class="lang-en">2. Practice Questions</span>
            </button>
            <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
                <i class="fas fa-stopwatch"></i>
                <span class="lang-hi">3. मिनी टेस्ट</span>
                <span class="lang-en">3. Mini Test</span>
            </button>
            <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false">
                <i class="fas fa-redo"></i>
                <span class="lang-hi">4. पुनरावृत्ति</span>
                <span class="lang-en">4. Revision</span>
            </button>
        </div>

        <!-- Tab Content Container -->
        <div class="topic-content" id="topic-content"></div>

        <!-- Embedded Data for Renderer -->
        <script id="upsc-page-data" type="application/json">
        ${JSON.stringify({
            topicId: 'up-assistant-teacher.hindi.' + topic.dir,
            topicName: topic.name,
            hindiName: topic.hindiName,
            subject: 'Hindi',
            subjectDir: 'hindi',
            concepts: conceptsData || null,
            practice: null,
            pyqs: null,
            test: null,
            version: { generator: 'v1', prompt: '1.0' },
            contentHash: 'sha256-placeholder',
            generatedAt: now
        }, null, 2)}
        </script>
    </main>

    <div id="footer-container"></div>

    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const tabButtons = document.querySelectorAll('.tab-btn');
            const tabPanels = document.querySelectorAll('.tab-panel');

            tabButtons.forEach(function(button) {
                button.addEventListener('click', function() {
                    const targetTab = button.getAttribute('data-tab');

                    tabButtons.forEach(function(btn) {
                        btn.classList.remove('active');
                        btn.setAttribute('aria-selected', 'false');
                    });
                    button.classList.add('active');
                    button.setAttribute('aria-selected', 'true');

                    tabPanels.forEach(function(panel) {
                        panel.classList.remove('active');
                        if (panel.id === targetTab) {
                            panel.classList.add('active');
                        }
                    });
                });
            });
        });
    </script>

    <script src="/assets/js/upsc-renderer.min.js" defer data-cfasync="false"></script>
    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>

</html>`;
}

// ============================================================================
// RUN
// ============================================================================
main().catch(err => {
    console.error('Fatal error:', err);
    process.exit(1);
});
