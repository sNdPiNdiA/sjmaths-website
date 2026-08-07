/**
 * Generator: Creates subject subfolders with index.html pages listing all microtopics
 * for UP Assistant Teacher syllabus.
 */
const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname);

const subjects = [
    {
        folder: 'hindi',
        title: 'हिन्दी',
        titleEn: 'Hindi',
        marks: 'लगभग 13-14 अंक (40 Marks - 3 Languages combined)',
        icon: 'fas fa-book',
        subtitle: 'हिंदी व्याकरण, अपठित गद्यांश, पद्यांश, हिंदी साहित्य',
        subtitleEn: 'Hindi Grammar, Unseen Prose, Poetry, Hindi Literature',
        sections: [
            {
                title: 'हिंदी व्याकरण',
                titleEn: 'Hindi Grammar',
                count: 12,
                topics: [
                    'वर्ण विचार (स्वर एवं व्यंजन)',
                    'संज्ञा - भेद एवं उदाहरण',
                    'सर्वनाम - विभक्ति एवं कारक',
                    'क्रिया - कर्ता, कर्म, कारक',
                    'कारक - सप्तकारक विवरण',
                    'वाक्य - रचना व प्रकार',
                    'अव्यय - शब्द विभाग',
                    'उपसर्ग एवं प्रत्यय',
                    'समास - भेद व प्रकार',
                    'त्रुटि एवं उनका सुधार',
                    'वर्तनी व वाक्य शुद्धि',
                    'शब्द रचना व शब्द भंडार'
                ]
            },
            {
                title: 'अपठित गद्यांश',
                titleEn: 'Unseen Prose',
                count: 8,
                topics: [
                    'मुख्य भाव, विषय व शब्दार्थ',
                    'वाक्य संशोधन व वाक्य विश्लेषण',
                    'सारांश लेखन',
                    'प्रश्नोत्तर एवं व्याख्या',
                    'अनुवाद एवं संक्षेपण',
                    'लघु उत्तरीय एवं विस्तृत प्रश्न',
                    'गद्यांश की भाषा शैली का विवरण',
                    'भाषिक रचना व व्याकरणिक प्रयोग'
                ]
            },
            {
                title: 'पद्यांश',
                titleEn: 'Poetry Passage',
                count: 10,
                topics: [
                    'काव्य का मुख्य भाव व भावार्थ',
                    'छंद व छंदबद्धता',
                    'अलंकार - भेद व उदाहरण',
                    'रस - विभाग, स्थायी भाव व उदाहरण',
                    'काव्य चेतना व अनुभूति',
                    'अनुभव व बिम्ब विधान',
                    'काव्य रचना व प्रकार',
                    'काव्य के विभिन्न रूप व विधाएं',
                    'कवि परिचय व काव्य गुण',
                    'काव्य का संदेश व सामाजिक प्रभाव'
                ]
            },
            {
                title: 'हिंदी साहित्य',
                titleEn: 'Hindi Literature',
                count: 15,
                topics: [
                    'भारतेन्दु हरिश्चंद्र - नाटक व समाज सुधार',
                    'महावीर प्रसाद द्विवेदी - सरस्वती पत्रिका',
                    'मैथिलीशरण गुप्त - साकेत, यशोधरा',
                    'जयशंकर प्रसाद - कामायनी, स्कंदगुप्त',
                    "सूर्यकांत त्रिपाठी 'निराला' - राम की शक्ति पूजा",
                    'सुमित्रानंदन पंत - चिदंबरा',
                    'महादेवी वर्मा - यामा, नीरजा',
                    'मुंशी प्रेमचंद - गोदान, कफन, पंच परमेश्वर',
                    'यशपाल - झूठा सच, दिव्या',
                    "सच्चिदानंद हीरानंद वात्स्यायन 'अज्ञेय' - कविता व उपन्यास",
                    'भक्तिकाल - कबीरदास, तुलसीदास, सूरदास',
                    'रीतिकाल - केशवदास, बिहारी, भूषण',
                    'छायावाद के चार प्रमुख स्तंभ',
                    'प्रगतिवाद एवं प्रयोगवाद',
                    'समकालीन साहित्य - हरिवंश राय बच्चन, कमलेश्वर'
                ]
            }
        ]
    },
    {
        folder: 'sanskrit',
        title: 'संस्कृत',
        titleEn: 'Sanskrit',
        marks: 'लगभग 13-14 अंक (40 Marks - 3 Languages combined)',
        icon: 'fas fa-om',
        subtitle: 'संस्कृत व्याकरण, अपठित गद्यांश, पद्यांश, संस्कृत साहित्य',
        subtitleEn: 'Sanskrit Grammar, Unseen Prose, Poetry, Sanskrit Literature',
        sections: [
            {
                title: 'संस्कृत व्याकरण',
                titleEn: 'Sanskrit Grammar',
                count: 12,
                topics: [
                    'वर्णमाला - स्वर व व्यंजन (माहेश्वर सूत्र)',
                    'संज्ञा - षड्जाति व रूप',
                    'सर्वनाम - शब्द रूप एवं प्रयोग',
                    'क्रिया - धातु रूप व दशलकार',
                    'कारक एवं विभक्ति विवरण',
                    'वाक्य रचना व वाक्य प्रकार',
                    'अव्यय - शब्द भेद एवं प्रयोग',
                    'उपसर्ग एवं प्रत्यय (कृत् व तद्धित)',
                    'समास - भेद व विग्रह',
                    'संधि - स्वर, व्यंजन एवं विसर्ग',
                    'शुद्धि-संशोधन (वाक्य व पद)',
                    'शब्द रूप एवं शब्द निर्माण'
                ]
            },
            {
                title: 'अपठित गद्यांश',
                titleEn: 'Unseen Prose',
                count: 8,
                topics: [
                    'मुख्य भाव, विषय व शब्दार्थ',
                    'वाक्य संशोधन व पद परिचय',
                    'सारांश लेखन',
                    'प्रश्नोत्तर एवं अर्थग्रहण',
                    'अनुवाद एवं संक्षेपण',
                    'लघु उत्तरीय एवं विस्तृत प्रश्न',
                    'गद्यांश की भाषा शैली',
                    'भाषिक रचना व व्याकरणिक प्रयोग'
                ]
            },
            {
                title: 'पद्यांश',
                titleEn: 'Poetry Passage',
                count: 10,
                topics: [
                    'काव्य का मुख्य भाव व अन्वय',
                    'छंद व छंद विधान (अनुष्टुप्, उपजाति आदि)',
                    'अलंकार - उपमा, रूपक, उत्प्रेक्षा आदि',
                    'रस - रस निष्पत्ति व स्थायी भाव',
                    'सुभाषित एवं सूक्तियां',
                    'काव्य सौंदर्य व अनुभूति',
                    'काव्य रचना व श्लोक व्याख्या',
                    'काव्य के विभिन्न रूप (महाकाव्य, खण्डकाव्य)',
                    'कवि परिचय व रीति-गुण',
                    'श्लोक का संदेश व नैतिक शिक्षा'
                ]
            },
            {
                title: 'संस्कृत साहित्य',
                titleEn: 'Sanskrit Literature',
                count: 12,
                topics: [
                    'महर्षि वाल्मीकि - रामायण',
                    'महाकवि कालिदास - अभिज्ञानशाकुन्तलम्, मेघदूतम्',
                    'भवभूति - उत्तररामचरितम्',
                    'भारवि - किरातार्जुनीयम्',
                    'दण्डी - दशकुमारचरितम्',
                    'वेदव्यास - महाभारत',
                    'भास - स्वप्नवासवदत्तम् व 13 नाटक',
                    'अश्वघोष - बुद्धचरितम्',
                    'बाणभट्ट - कादम्बरी व हर्षचरितम्',
                    'जयदेव - गीतगोविन्दम्',
                    'माघ - शिशुपालवधम्',
                    'संस्कृत महाकाव्य, नाटक एवं कथा साहित्य'
                ]
            }
        ]
    },
    {
        folder: 'english',
        title: 'अंग्रेजी',
        titleEn: 'English',
        marks: 'लगभग 13-14 अंक (40 Marks - 3 Languages combined)',
        icon: 'fas fa-language',
        subtitle: 'English Grammar, Unseen Prose Comprehension, English Literature',
        subtitleEn: 'English Grammar, Unseen Prose Comprehension, English Literature',
        sections: [
            {
                title: 'अंग्रेजी व्याकरण',
                titleEn: 'English Grammar',
                count: 12,
                topics: [
                    'Tenses - All 12 Tenses (काल)',
                    'Articles - A, An, The (आर्टिकल्स)',
                    'Prepositions - Usage & Examples (संबंधबोधक अव्यय)',
                    'Conjunctions - Types & Usage (समुच्चयबोधक अव्यय)',
                    'Pronouns - Personal, Reflexive, Demonstrative (सर्वनाम)',
                    'Nouns - Countable, Uncountable, Collective (संज्ञा)',
                    'Verbs - Transitive, Intransitive, Modal (क्रिया)',
                    'Adjectives - Comparative, Superlative (विशेषण)',
                    'Adverbs - Types & Position (क्रियाविशेषण)',
                    'Subject-Verb Agreement (कर्ता-क्रिया सामंजस्य)',
                    'Error Spotting & Sentence Correction (त्रुटि पहचान)',
                    'Fill in the Blanks & Sentence Completion (रिक्त स्थान पूर्ति)'
                ]
            },
            {
                title: 'अपठित गद्यांश',
                titleEn: 'Unseen Prose Comprehension',
                count: 10,
                topics: [
                    'Reading Comprehension - Main Idea (पठन बोध - मुख्य विचार)',
                    'Reading Comprehension - Inference (पठन बोध - निष्कर्ष एवं अनुमान)',
                    'Reading Comprehension - Vocabulary in Context (पठन बोध - शब्दावली)',
                    "Reading Comprehension - Tone & Author's View (पठन बोध - लेखक का दृष्टिकोण)",
                    'Summary Writing (सारांश लेखन)',
                    'Note Making & Paraphrasing (नोट निर्माण एवं व्याख्या)',
                    'Short Answer & Long Answer Questions (लघु/विस्तृत प्रश्न)',
                    'Textual Grammar & Usage (पाठ्य व्याकरण एवं प्रयोग)',
                    'Coherence & Cohesion in Text (सुसंगति एवं संयोजन)',
                    'Critical Analysis of Passage (गद्यांश का गहन विश्लेषण)'
                ]
            },
            {
                title: 'अंग्रेजी साहित्य',
                titleEn: 'English Literature',
                count: 15,
                topics: [
                    'William Shakespeare - Plays & Sonnets',
                    'Jane Austen - Pride and Prejudice',
                    'Charles Dickens - Great Expectations, Oliver Twist',
                    'Mark Twain - Adventures of Tom Sawyer',
                    'Rabindranath Tagore - Gitanjali, Kabuliwala',
                    'William Wordsworth - Romantic Poetry',
                    'John Keats - Odes & Sonnets',
                    'Robert Frost - Modern American Poetry',
                    'T.S. Eliot - Modernist Poetry',
                    'Poetry Comprehension - Themes & Devices',
                    'Novel Comprehension - Character Analysis',
                    'Short Story - Plot & Moral',
                    'Literary Devices - Metaphor, Simile, Alliteration',
                    'Prose Style - Narrative & Descriptive',
                    'Vocabulary Building - Synonyms, Antonyms, One-word Substitution'
                ]
            }
        ]
    },
    {
        folder: 'science',
        title: 'विज्ञान',
        titleEn: 'Science',
        marks: '10 अंक (10 Marks)',
        icon: 'fas fa-flask',
        subtitle: 'दैनिक जीवन में विज्ञान, भौतिक विज्ञान, जीव विज्ञान, पर्यावरण',
        subtitleEn: 'Science in Daily Life, Physics, Biology, Environment',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 12,
                topics: [
                    'Science in Daily Life (दैनिक जीवन में विज्ञान)',
                    'Motion (गति)',
                    'Force (बल)',
                    'Energy (ऊर्जा)',
                    'Distance (दूरी)',
                    'Light (प्रकाश)',
                    'Sound (ध्वनि)',
                    'The Living World (जीवों की दुनिया)',
                    'Human Body Health (मानव शरीर स्वास्थ्य)',
                    'Hygiene & Nutrition (स्वच्छता एवं पोषण)',
                    'Environment & Natural Resources (पर्यावरण एवं प्राकृतिक संसाधन)',
                    'Matter & States of Matter (पदार्थ एवं पदार्थ की अवस्थाएं)'
                ]
            }
        ]
    },
    {
        folder: 'mathematics',
        title: 'गणित',
        titleEn: 'Mathematics',
        marks: '20 अंक (20 Marks)',
        icon: 'fas fa-calculator',
        subtitle: 'अंकगणित, बीजगणित, ज्यामिति, मापन, सांख्यिकी',
        subtitleEn: 'Arithmetic, Algebra, Geometry, Mensuration, Statistics',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 18,
                topics: [
                    'Numerical Ability (अंकीय क्षमता)',
                    'Mathematical Operations (गणितीय संक्रियाएं)',
                    'Decimals (दशमलव)',
                    'Place Value (स्थानीयमान)',
                    'Fractions (भिन्न)',
                    'Interest - Simple & Compound (साधारण व चक्रवृद्धि ब्याज)',
                    'Profit & Loss (लाभ-हानि)',
                    'Percentage & Divisibility (प्रतिशत विभाज्य)',
                    'Factors & Factorization (गुणनखण्ड)',
                    'Unitary Method (ऐकिक नियम)',
                    'General Algebra (सामान्य बीजगणित)',
                    'Area - Mensuration 2D (क्षेत्रफल)',
                    'Average (औसत)',
                    'Volume - Mensuration 3D (आयतन)',
                    'Ratio & Proportion (अनुपात एवं समानुपात)',
                    'Algebraic Identities (सर्वसमिकाएं)',
                    'General Geometry (सामान्य ज्यामिति)',
                    'General Statistics (सामान्य सांख्यिकी)'
                ]
            }
        ]
    },
    {
        folder: 'teaching-skills',
        title: 'शिक्षण कौशल',
        titleEn: 'Teaching Skills',
        marks: '10 अंक (10 Marks)',
        icon: 'fas fa-chalkboard-teacher',
        subtitle: 'शिक्षण विधियाँ, सिद्धान्त, समावेशी शिक्षा, मूल्यांकन',
        subtitleEn: 'Teaching Methods, Principles, Inclusive Education, Evaluation',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 8,
                topics: [
                    'Teaching Methods & Skills (शिक्षण की विधियाँ एवं कौशल)',
                    'Principles of Teaching & Learning (शिक्षण अधिगम के सिद्धान्त)',
                    'Current Indian Society & Elementary Education (वर्तमान भारतीय समाज एवं प्रारम्भिक शिक्षा)',
                    'Inclusive Education (समावेशी शिक्षा)',
                    'New Initiatives in Elementary Education (प्रारम्भिक शिक्षा के नवीन प्रयास)',
                    'Educational Evaluation & Measurement (शैक्षिक मूल्यांकन एवं मापन)',
                    'Initial Reading Skills (आरम्भिक पठन कौशल)',
                    'Educational Management & Administration (शैक्षिक प्रबन्धन एवं प्रशासन)'
                ]
            }
        ]
    },
    {
        folder: 'child-psychology',
        title: 'बाल मनोविज्ञान',
        titleEn: 'Child Psychology',
        marks: '10 अंक (10 Marks)',
        icon: 'fas fa-child',
        subtitle: 'बाल विकास, सीखने के सिद्धान्त, वैयक्तिक भिन्नता',
        subtitleEn: 'Child Development, Learning Theories, Individual Differences',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 6,
                topics: [
                    'Individual Differences (वैयक्तिक भिन्नता)',
                    'Factors Affecting Child Development (बाल विकास को प्रभावित करने वाले कारक)',
                    'Identification of Learning Needs (सीखने की आवश्यकता की पहचान)',
                    'Creating Conducive Learning Environment (पढ़ने के लिए वातावरण का सृजन करना)',
                    'Learning Theories & Practical Classroom Application (सीखने के सिद्धान्त तथा कक्षा-शिक्षण में व्यावहारिक उपयोगिता)',
                    'Special Provisions for Divyang Students (दिव्यांग छात्रों हेतु विशेष व्यवस्था)'
                ]
            }
        ]
    },
    {
        folder: 'environmental-social-studies',
        title: 'पर्यावरण एवं सामाजिक अध्ययन',
        titleEn: 'Environmental & Social Studies',
        marks: '10 अंक (10 Marks)',
        icon: 'fas fa-globe-asia',
        subtitle: 'भूगोल, इतिहास, नागरिक शास्त्र, अर्थव्यवस्था, पर्यावरण',
        subtitleEn: 'Geography, History, Civics, Economy, Environment',
        sections: [
            {
                title: 'भूगोल',
                titleEn: 'Geography',
                topics: [
                    'Structure of the Earth (पृथ्वी की संरचना - क्रस्ट, मैंटल, कोर)',
                    'Latitudes & Longitudes (अक्षांश और देशान्तर, समय क्षेत्र)',
                    'Solar System & Earth\'s Motions (सौरमण्डल और पृथ्वी की गतियां)',
                    'Continents & Oceans (महाद्वीप एवं महासागर)',
                    'Ocean Currents & Marine Life (महासागरीय धाराएं व जीव)',
                    'Physical Divisions & Mountains of India (भारत के भौतिक प्रदेश एवं पर्वत)',
                    'River Systems & Lakes of India (भारत की नदियाँ एवं झीलें)',
                    'Soil, Climate & Monsoon in India (भारत की मिट्टी, जलवायु एवं मानसून)',
                    'Natural Resources: Forests, Minerals & Energy (प्राकृतिक सम्पदा: वन, खनिज व ऊर्जा)'
                ]
            },
            {
                title: 'इतिहास एवं संस्कृति',
                titleEn: 'Indian History & Culture',
                topics: [
                    'Revolt of 1857: Causes & Impact (1857 का प्रथम स्वतंत्रता संग्राम)',
                    'Social & Religious Reformers (भारतीय समाज सुधारक एवं आंदोलन)',
                    'Indian National Movement & Gandhian Era (भारतीय राष्ट्रीय आंदोलन एवं गांधी युग)',
                    'Revolutionary Movements & Netaji Subhas Chandra Bose (क्रांतिकारी आंदोलन एवं नेताजी)',
                    'Art, Architecture, Music & Dance of India (भारत की कला, संगीत, नृत्य व त्योहार)',
                    'UNESCO Heritage Sites in India (भारत के प्रमुख यूनेस्को धरोहर स्थल)'
                ]
            },
            {
                title: 'नागरिक शास्त्र एवं संविधान',
                titleEn: 'Civics & Constitution',
                topics: [
                    'Preamble & Features of the Constitution (संविधान की प्रस्तावना व मुख्य विशेषताएं)',
                    'Fundamental Rights, Duties & DPSPs (मौलिक अधिकार, कर्तव्य व नीति निदेशक तत्व)',
                    'Governance System: Union & State Legislature, Judiciary (शासन व्यवस्था: कार्यपालिका, विधायिका व न्यायपालिका)',
                    'Local Self-Government: Panchayati Raj System (स्थानीय स्वशासन: पंचायती राज व्यवस्था)'
                ]
            },
            {
                title: 'भारतीय अर्थव्यवस्था',
                titleEn: 'Indian Economy',
                topics: [
                    'Sectors, GDP & Planning (अर्थव्यवस्था के क्षेत्र, जीडीपी व पंचवर्षीय योजनाएं)',
                    'Current Challenges: Poverty, Unemployment & Inflation (अर्थव्यवस्था की चुनौतियाँ: गरीबी, बेरोजगारी व मुद्रास्फीति)',
                    'Banking System, RBI & Economic Reforms (बैंकिंग प्रणाली, आरबीआई व आर्थिक सुधार)'
                ]
            },
            {
                title: 'पर्यावरण, आपदा एवं सड़क सुरक्षा',
                titleEn: 'Environment & Road Safety',
                topics: [
                    'Environmental Conservation & Biodiversity (पर्यावरण संरक्षण, पारिस्थितिकी व जैव विविधता)',
                    'Pollution: Causes, Effects & Control (प्रदूषण: कारण, प्रभाव व रोकथाम)',
                    'Natural Disasters & Management (प्राकृतिक आपदा प्रबंधन व शमन)',
                    'Traffic Rules & Road Safety (यातायात एवं सड़क सुरक्षा के नियम)'
                ]
            }
        ]
    },
    {
        folder: 'gk-current-affairs',
        title: 'सामान्य ज्ञान / समसामयिक घटनाएँ',
        titleEn: 'GK / Current Affairs',
        marks: '30 अंक (30 Marks)',
        icon: 'fas fa-globe',
        subtitle: 'राष्ट्रीय, अंतर्राष्ट्रीय एवं राज्य स्तरीय समसामयिकी',
        subtitleEn: 'National, International & State Level Current Events',
        sections: [
            {
                title: 'समसामयिक घटनाएँ',
                titleEn: 'Current Events',
                topics: [
                    'National & International Events (राष्ट्रीय एवं अंतर्राष्ट्रीय घटनाएँ)',
                    'Uttar Pradesh State Specific Current Affairs (उत्तर प्रदेश विशेष समसामयिकी)',
                    'Summits, Conferences & Bilateral Meets (शिखर सम्मेलन, बैठकें एवं द्विपक्षीय समझौते)',
                    'Indices, Reports & Rankings (सूचकांक, रिपोर्ट एवं रैंकिंग)',
                    'Government Schemes: Union & UP Government (सरकारी योजनाएँ - केंद्र व राज्य सरकार)',
                    'Military Exercises, Space Missions & Defense News (सैन्य अभ्यास, अंतरिक्ष मिशन व रक्षा समाचार)',
                    'Science, Tech & Environment Current Affairs (विज्ञान, तकनीक व पर्यावरण समाचार)'
                ]
            },
            {
                title: 'स्थान एवं व्यक्तित्व',
                titleEn: 'Places & Personalities',
                topics: [
                    'Prominent Places & Geography in News (चर्चित स्थल)',
                    'Famous Personalities in News (चर्चित व्यक्तित्व)',
                    'Appointments: National & International (महत्वपूर्ण नियुक्तियाँ)',
                    'Obits: Prominent Demises (चर्चित निधन)'
                ]
            },
            {
                title: 'रचनाएँ एवं पुस्तकें',
                titleEn: 'Books & Literary Works',
                topics: [
                    'Famous Historical Books & Authors (प्रसिद्ध ऐतिहासिक पुस्तकें और लेखक)',
                    'Recent Books & Authors in News (हाल ही में चर्चित पुस्तकें एवं उनके लेखक)',
                    'Literary Awards & Honors (साहित्यिक पुरस्कार व सम्मान - जैसे ज्ञानपीठ, व्यास सम्मान)'
                ]
            },
            {
                title: 'राष्ट्रीय एवं अंतर्राष्ट्रीय पुरस्कार',
                titleEn: 'Awards & Honors',
                topics: [
                    'Nobel Prizes, Oscar & International Awards (नोबेल पुरस्कार, ऑस्कर व प्रमुख अंतर्राष्ट्रीय पुरस्कार)',
                    'National Awards: Bharat Ratna, Padma Awards, Gallantry Awards (राष्ट्रीय पुरस्कार: भारत रत्न, पद्म पुरस्कार)',
                    'National Film Awards & Sports Awards (राष्ट्रीय फिल्म पुरस्कार व खेल पुरस्कार)'
                ]
            },
            {
                title: 'खेल-कूद एवं प्रतियोगिताएँ',
                titleEn: 'Sports & Games',
                topics: [
                    'Olympic Games, Paralympics & Commonwealth (ओलंपिक, पैरालिंपिक व राष्ट्रमंडल खेल)',
                    'Cricket: ICC Tournaments, IPL & Bilateral Series (क्रिकेट प्रतियोगिताएँ)',
                    'Tennis: Grand Slams & Badminton Championships (ग्रैंड स्लैम व अन्य टेनिस/बैडमिंटन खेल)',
                    'Other Sports: Football World Cup, Hockey & Athletics (अन्य प्रमुख खेल व कप)'
                ]
            },
            {
                title: 'भारतीय संस्कृति एवं कला',
                titleEn: 'Indian Culture & Heritage',
                topics: [
                    'Indian Art Forms: Paintings, Crafts & Sculptures (भारतीय चित्रकला, हस्तशिल्प व मूर्तिकला)',
                    'Classical & Folk Dances of India (भारत के शास्त्रीय एवं लोक नृत्य)',
                    'Indian Classical Music & Musical Instruments (भारतीय शास्त्रीय संगीत व वाद्य यंत्र)',
                    'Fairs, Festivals & Cultural Tourism of India (प्रमुख मेले, त्योहार व सांस्कृतिक पर्यटन)',
                    'Ancient Indian Monuments, Temples & Architecture (प्राचीन स्मारक, मंदिर व स्थापत्य कला)'
                ]
            }
        ]
    },
    {
        folder: 'logical-reasoning',
        title: 'तार्किक ज्ञान',
        titleEn: 'Logical Reasoning',
        marks: '5 अंक (5 Marks)',
        icon: 'fas fa-brain',
        subtitle: 'सामान्य तार्किक अभिरुचि के सभी विषय',
        subtitleEn: 'All Topics of General Logical Reasoning Ability',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 18,
                topics: [
                    'Analogies (सादृश्यता)',
                    'Assertion and Reason (कथन और कारण)',
                    'Binary Logic (द्विआधारी तर्क)',
                    'Classification - Odd One Out (वर्गीकरण)',
                    'Clocks and Calendars (घड़ियाँ एवं कैलेंडर)',
                    'Coded Inequalities (कूट असमानताएँ)',
                    'Coding-Decoding (कोडिंग-डिकोडिंग)',
                    'Critical Reasoning (गंभीर तर्कशक्ति)',
                    'Cubes & Dices (घन एवं पासा)',
                    'Number Series (संख्या शृंखला)',
                    'Puzzles (पहेलियाँ)',
                    'Symbols and Notations (प्रतीक एवं संकेत)',
                    'Venn Diagrams and Dice (वेन आरेख एवं पासा)',
                    'Data Interpretation (आँकड़ा व्याख्या)',
                    'Direction Sense Test (दिशा ज्ञान परीक्षण)',
                    'Grouping and Selections (समूहीकरण एवं चयन)',
                    'Inferences & Deductions (निष्कर्ष एवं अनुमान)',
                    'Letter Series (वर्ण शृंखला)'
                ]
            }
        ]
    },
    {
        folder: 'information-technology',
        title: 'सूचना तकनीकी',
        titleEn: 'Information Technology',
        marks: '5 अंक (5 Marks)',
        icon: 'fas fa-desktop',
        subtitle: 'कंप्यूटर, इंटरनेट, डिजिटल शिक्षण साधन',
        subtitleEn: 'Computers, Internet, Digital Teaching Tools',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 8,
                topics: [
                    'Teaching Skills Development (शिक्षण कौशल विकास)',
                    'IT in Classroom Teaching & School Management (कक्षा-शिक्षण तथा विद्यालय प्रबन्धन में सूचना तकनीकी)',
                    'Computers - Fundamentals & Applications (कम्प्यूटर - आधारभूत संरचना व अनुप्रयोग)',
                    'Internet - Educational Applications & Web Tools (इन्टरनेट - शैक्षिक उपयोग)',
                    'Smartphones & Digital Teaching Gadgets (स्मार्टफोन व डिजिटल शिक्षण साधन)',
                    'OER - Open Educational Resources (मुक्त शैक्षिक संसाधन)',
                    'Educational Apps, Portals & Software (शिक्षण में उपयोगी ऐप्स व पोर्टल्स)',
                    'Usage of Digital Learning Materials / E-Content (डिजिटल शिक्षण-सामग्री के उपयोग की जानकारी)'
                ]
            }
        ]
    },
    {
        folder: 'life-skill-management',
        title: 'जीवन कौशल / प्रबन्धन एवं अभिवृत्ति',
        titleEn: 'Life Skill / Management & Attitude',
        marks: '10 अंक (10 Marks)',
        icon: 'fas fa-heart',
        subtitle: 'व्यावसायिक आचरण, प्रेरणा, शिक्षक की भूमिका, मूल्य',
        subtitleEn: 'Professional Conduct, Motivation, Role of Teacher, Values',
        sections: [
            {
                title: 'विषय सूची',
                titleEn: 'Topics List',
                count: 5,
                topics: [
                    'Professional Conduct & Ethics (व्यावसायिक आचरण एवं नीति)',
                    'Motivation & Its Role in Learning (प्रेरणा एवं अधिगम में इसकी भूमिका)',
                    'Role of Teacher - Facilitator, Monitor, Leader, Guide, Counselor (शिक्षण की भूमिका)',
                    'Constitutional & Human Values (संवैधानिक और मानवीय मूल्य)',
                    'Effective Implementation of Reward & Punishment System (दण्ड एवं पुरस्कार व्यवस्था का प्रभावी प्रयोग)'
                ]
            }
        ]
    }
];

function transliterate(text) {
    const map = {
        'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
        'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'ङ': 'nga',
        'च': 'cha', 'छ': 'chha', 'ज': 'ja', 'झ': 'jha', 'ञ': 'nya',
        'ट': 'ta', 'ठ': 'tha', 'ड': 'da', 'ढ': 'dha', 'ण': 'na',
        'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na',
        'प': 'pa', 'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma',
        'य': 'ya', 'र': 'ra', 'ल': 'la', 'व': 'va',
        'श': 'sha', 'ष': 'sha', 'स': 'sa', 'ह': 'ha',
        'क्ष': 'ksha', 'त्र': 'tra', 'ज्ञ': 'gya',
        'ा': 'a', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ं': 'n', 'ः': 'h', 'ँ': 'n',
        '्': ''
    };
    
    let result = '';
    for (let char of text) {
        if (map[char] !== undefined) {
            result += map[char];
        } else if (/[a-zA-Z0-9\s-]/.test(char)) {
            result += char;
        } else if (char === ' ') {
            result += ' ';
        }
    }
    return result.toLowerCase()
        .trim()
        .replace(/[\s-]+/g, '-');
}

function getSlug(topic) {
    if (/[\u0900-\u097F]/.test(topic)) {
        const match = topic.match(/^[a-zA-Z0-9\s:&,-]+/);
        if (match && match[0].trim().length > 3) {
            return match[0].toLowerCase()
                .replace(/[^a-z0-9\s-]/g, '')
                .trim()
                .replace(/[\s-]+/g, '-');
        }
        return transliterate(topic);
    }

    let english = topic;
    const match = topic.match(/^(.*?)\s*\([\u0900-\u097F]/);
    if (match) {
        english = match[1];
    } else {
        const matchParen = topic.match(/^(.*?)\s*\(/);
        if (matchParen) {
            english = matchParen[1];
        }
    }
    return english.toLowerCase()
        .replace(/[^a-z0-9\s-]/g, '')
        .trim()
        .replace(/[\s-]+/g, '-');
}

function generateSubjectPage(subject) {
    const totalTopics = subject.sections.reduce((sum, s) => sum + s.topics.length, 0);

    const sectionsHtml = subject.sections.map((section, secIdx) => {
        const itemsHtml = section.topics.map((topic, i) => {
            const id = `${subject.folder}-mt-${secIdx + 1}-${i + 1}`;
            const slug = getSlug(topic);
            return `                                <li class="syllabus-item"><a href="/up-assistant-teacher/${subject.folder}/${slug}/" style="text-decoration:none;color:inherit;flex:1;"><input type="checkbox" class="syllabus-checkbox" id="${id}"><span class="syllabus-text">${topic}</span></a></li>`;
        }).join('\n');

        return `                        <details class="syllabus-subsection" data-prefix="${subject.folder}" data-grp-idx="${secIdx + 1}" open>
                            <summary class="subsection-summary">
                                <span class="subsection-title">
                                    <span class="lang-hi">${section.title}</span>
                                    <span class="lang-en">${section.titleEn}</span>
                                </span>
                                <div class="subsection-meta">
                                    <span class="subsection-progress" id="${subject.folder}-prog-${secIdx + 1}">0/${section.topics.length}</span>
                                    <i class="fas fa-chevron-down toggle-icon"></i>
                                </div>
                            </summary>
                            <ul class="syllabus-list">
${itemsHtml}
                            </ul>
                        </details>`;
    }).join('\n');

    return `<!DOCTYPE html>
<html lang="hi">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${subject.title} - UP Assistant Teacher Syllabus Micro Topics | SJMaths</title>
    <meta name="description" content="${subject.title} micro-topic syllabus for UP Assistant Teacher Recruitment Examination. ${totalTopics} microtopics with interactive tracking.">
    <link rel="icon" type="image/png" href="/favicon.png">
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
            --accent-gradient: linear-gradient(135deg, #d4af37, #2980b9);
        }
        body.dark-mode {
            --glass-bg: rgba(30, 30, 46, 0.95);
            --glass-border: rgba(255, 255, 255, 0.05);
            --shadow-lg: 0 10px 30px -5px rgba(0, 0, 0, 0.3);
        }
        .syllabus-container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 2.5rem 1.5rem;
            animation: fadeIn 0.5s ease-out;
        }
        .syllabus-header {
            text-align: center;
            margin-bottom: 2rem;
        }
        .syllabus-header h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.2rem;
            font-weight: 800;
            background: var(--accent-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .syllabus-header .subject-icon {
            font-size: 2.5rem;
            color: #d4af37;
            margin-bottom: 0.5rem;
        }
        .syllabus-header p {
            font-size: 1rem;
            color: var(--text-light);
        }
        .marks-badge {
            display: inline-block;
            background: rgba(212, 175, 55, 0.1);
            color: #d4af37;
            padding: 0.3rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        .back-link {
            display: inline-block;
            margin-bottom: 1.5rem;
            color: #d4af37;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
        }
        .back-link:hover {
            text-decoration: underline;
        }
        .tracker-banner {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 1.25rem;
            box-shadow: var(--shadow-lg);
            padding: 1.25rem;
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .tracker-info h2 {
            font-family: 'Outfit', sans-serif;
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-dark);
            margin: 0;
        }
        .tracker-info p {
            font-size: 0.85rem;
            color: var(--text-light);
            margin: 0.25rem 0 0;
        }
        .tracker-progress-container {
            display: flex;
            align-items: center;
            gap: 1rem;
            flex-grow: 1;
            max-width: 400px;
            justify-content: flex-end;
        }
        .progress-bar-wrapper {
            background: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
            height: 10px;
            width: 100%;
            overflow: hidden;
        }
        .progress-bar-fill {
            background: var(--accent-gradient);
            height: 100%;
            width: 0%;
            transition: width 0.4s ease-out;
            border-radius: 10px;
        }
        .progress-percentage {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1rem;
            color: #d4af37;
            min-width: 45px;
            text-align: right;
        }
        details.syllabus-subsection {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 12px;
            margin-bottom: 1rem;
            box-shadow: var(--shadow-lg);
            overflow: hidden;
        }
        summary.subsection-summary {
            padding: 1rem 1.25rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            list-style: none;
            user-select: none;
        }
        summary.subsection-summary::-webkit-details-marker {
            display: none;
        }
        .subsection-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-dark);
            margin: 0;
            flex-grow: 1;
            padding-right: 1rem;
        }
        .subsection-meta {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }
        .subsection-progress {
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.5rem;
            background: rgba(0, 0, 0, 0.05);
            color: var(--text-light);
            border-radius: 12px;
            white-space: nowrap;
        }
        .subsection-progress.completed {
            background: rgba(46, 204, 113, 0.15);
            color: #2ecc71;
        }
        .toggle-icon {
            font-size: 0.8rem;
            color: var(--text-light);
            transition: transform 0.3s ease;
        }
        details.syllabus-subsection[open] .toggle-icon {
            transform: rotate(180deg);
            color: #d4af37;
        }
        .syllabus-list {
            list-style: none;
            padding: 0.5rem 1rem 1rem;
            margin: 0;
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .syllabus-item {
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            padding: 0.5rem 0.7rem;
            border-radius: 8px;
            transition: background-color 0.2s ease;
            cursor: pointer;
            border: 1px solid transparent;
        }
        .syllabus-item:hover {
            background: rgba(212, 175, 55, 0.03);
            border-color: rgba(212, 175, 55, 0.05);
        }
        .syllabus-checkbox {
            appearance: none;
            -webkit-appearance: none;
            width: 18px;
            height: 18px;
            border: 2px solid var(--text-light);
            border-radius: 5px;
            outline: none;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            transition: all 0.2s ease;
            flex-shrink: 0;
            margin-top: 2px;
        }
        .syllabus-checkbox::before {
            content: "\\f00c";
            font-family: "Font Awesome 6 Free";
            font-weight: 900;
            font-size: 0.7rem;
            color: #ffffff;
            display: none;
        }
        .syllabus-checkbox:checked {
            background: var(--accent-gradient);
            border-color: transparent;
        }
        .syllabus-checkbox:checked::before {
            display: block;
        }
        .syllabus-text {
            font-size: 0.95rem;
            color: var(--text-light);
            line-height: 1.5;
            transition: color 0.2s ease, text-decoration 0.2s ease;
        }
        .syllabus-checkbox:checked+.syllabus-text {
            color: var(--muted, #9ca3af);
            text-decoration: line-through;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>
    <div id="header-container"></div>

    <main class="syllabus-container" id="main-content">
        <a href="/up-assistant-teacher/" class="back-link"><i class="fas fa-arrow-left"></i> <span class="lang-hi">वापस सिलेबस पर जाएँ</span><span class="lang-en">Back to Syllabus</span></a>

        <div class="syllabus-header">
            <div class="subject-icon"><i class="${subject.icon}"></i></div>
            <h1>
                <span class="lang-hi">${subject.title}</span>
                <span class="lang-en">${subject.titleEn}</span>
            </h1>
            <p>
                <span class="lang-hi">${subject.subtitle} — कुल ${totalTopics} माइक्रो-टॉपिक</span>
                <span class="lang-en">${subject.subtitleEn} — Total ${totalTopics} Microtopics</span>
            </p>
            <div class="marks-badge">${subject.marks}</div>
        </div>

        <div class="tracker-banner">
            <div class="tracker-info">
                <h2><span class="lang-hi">${subject.title} प्रगति</span><span class="lang-en">${subject.titleEn} Progress</span></h2>
                <p><span class="lang-hi">विषयों को पूरा करने के बाद चेक करें। प्रगति अपने आप सहेजी जाती है।</span><span class="lang-en">Check off topics as you cover them. Progress is saved automatically.</span></p>
            </div>
            <div class="tracker-progress-container">
                <div class="progress-bar-wrapper">
                    <div class="progress-bar-fill" id="syllabusProgressBar"></div>
                </div>
                <div class="progress-percentage" id="syllabusProgressPercent">0%</div>
            </div>
        </div>

${sectionsHtml}
    </main>

    <div id="footer-container"></div>

    <button id="backToTop" class="back-to-top" aria-label="Back to Top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const progressBar = document.getElementById('syllabusProgressBar');
            const progressPercent = document.getElementById('syllabusProgressPercent');

            // Local language toggle state
            window.toggleLocalLanguage = function () {
                const isHi = document.body.classList.toggle('lang-mode-hi');
                localStorage.setItem('sjmaths_preferred_language', isHi ? 'hi' : 'en');
            };

            // Restore Language Preference
            if (localStorage.getItem('sjmaths_preferred_language') === 'hi') {
                document.body.classList.add('lang-mode-hi');
            }

            const checkboxes = document.querySelectorAll('.syllabus-checkbox');
            const storedProgress = JSON.parse(localStorage.getItem('up-assistant-teacher-${subject.folder}-progress')) || {};

            checkboxes.forEach(checkbox => {
                const id = checkbox.id;
                if (storedProgress[id]) {
                    checkbox.checked = true;
                }

                checkbox.addEventListener('change', () => {
                    storedProgress[checkbox.id] = checkbox.checked;
                    localStorage.setItem('up-assistant-teacher-${subject.folder}-progress', JSON.stringify(storedProgress));
                    updateProgress();
                });

                const parent = checkbox.closest('.syllabus-item');
                if (parent) {
                    parent.addEventListener('click', (e) => {
                        if (e.target !== checkbox && e.target.tagName !== 'A') {
                            checkbox.checked = !checkbox.checked;
                            checkbox.dispatchEvent(new Event('change'));
                        }
                    });
                }
            });

            function updateProgress() {
                const total = checkboxes.length;
                const checked = Array.from(checkboxes).filter(cb => cb.checked).length;
                const percentage = total > 0 ? Math.round((checked / total) * 100) : 0;

                if (progressBar) progressBar.style.width = percentage + '%';
                if (progressPercent) progressPercent.textContent = percentage + '%';

                const subsections = document.querySelectorAll('.syllabus-subsection');
                subsections.forEach(sub => {
                    const prefix = sub.getAttribute('data-prefix');
                    const grpIdx = sub.getAttribute('data-grp-idx');
                    const subCheckboxes = sub.querySelectorAll('.syllabus-checkbox');
                    const subTotal = subCheckboxes.length;
                    const subChecked = Array.from(subCheckboxes).filter(cb => cb.checked).length;

                    const progEl = document.getElementById(prefix + '-prog-' + grpIdx);
                    if (progEl) {
                        progEl.textContent = subChecked + '/' + subTotal;
                        if (subChecked === subTotal && subTotal > 0) {
                            progEl.classList.add('completed');
                        } else {
                            progEl.classList.remove('completed');
                        }
                    }
                });
            }

            updateProgress();
        });
    </script>

    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=6e28faa6" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=bd5be716" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>

</html>`;
}

let totalAll = 0;
subjects.forEach(subject => {
    const dir = path.join(BASE_DIR, subject.folder);
    if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
    }
    const html = generateSubjectPage(subject);
    const filePath = path.join(dir, 'index.html');
    fs.writeFileSync(filePath, html, 'utf8');
    const count = subject.sections.reduce((s, sec) => s + sec.topics.length, 0);
    totalAll += count;
    console.log(`✓ Created ${subject.folder}/index.html (${count} microtopics)`);
});

console.log(`\n✅ Done! Created ${subjects.length} subject folders with ${totalAll} total microtopics.`);

if (typeof module !== 'undefined') {
    module.exports = { subjects, getSlug };
}