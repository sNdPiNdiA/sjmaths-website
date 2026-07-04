#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/science_and_tech/Biotechnology-Biology"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'bt', 'dna', 'rna', 'ipr', 'crispr', 'gmo', 'gmos', 'pbr', 'pbrs', 'wipo', 'trips', 'hiv', 'tb', 'dbt', 'ahwr', 'atgm'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Grouped dataset containing fact-rich mindmaps with colons to support sub-branch restructuring
# Every single one of the 60 subdirectories has its own completely unique dataset.
GROUPS = [
    {
        "keys": ["achievements-of-biotechnology-in-different-fields"],
        "en": [
            {"label": "Agriculture & Food", "type": "branch", "date": "Agriculture", "children": [
                {"label": "Crop Yields: Pest-resistant crops (Bt Cotton) and nutrient-enriched foods (Golden Rice)", "type": "leaf"},
                {"label": "Stress Tolerance: Drought-tolerant maize and flood-resistant rice varieties", "type": "leaf"}
            ]},
            {"label": "Medicine & Industry", "type": "branch", "date": "Medicine", "children": [
                {"label": "Gene Therapy: Correcting hereditary diseases by introducing normal genes into patient cells", "type": "leaf"},
                {"label": "Bioremediation: Microbes engineered to digest oil spills and toxic heavy metals", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कृषि और खाद्य क्षेत्र", "type": "branch", "date": "कृषि", "children": [
                {"label": "फसल पैदावार: कीट-प्रतिरोधी फसलें (जैसे बीटी कॉटन) और पोषक तत्वों से भरपूर खाद्य पदार्थ (जैसे गोल्डन राइस)", "type": "leaf"},
                {"label": "तनाव सहनशीलता: सूखा-सहिष्णु मक्का और बाढ़-प्रतिरोधी धान की किस्में", "type": "leaf"}
            ]},
            {"label": "चिकित्सा और उद्योग", "type": "branch", "date": "चिकित्सा", "children": [
                {"label": "जीन थेरेपी: रोगी की कोशिकाओं में सामान्य जीन पेश करके आनुवंशिक रोगों को ठीक करना", "type": "leaf"},
                {"label": "बायोरेमेडिएशन: तेल रिसाव और जहरीली भारी धातुओं को पचाने के लिए इंजीनियर्ड रोगाणु", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["animal-and-insect-biotechnology"],
        "en": [
            {"label": "Animal Biotechnology", "type": "branch", "date": "Animals", "children": [
                {"label": "Transgenics: Generating transgenic livestock to produce pharmaceutical proteins in milk (biopharming)", "type": "leaf"},
                {"label": "Cloning: Somatic Cell Nuclear Transfer (SCNT) technique; produced Dolly the sheep and Noorie the pashmina goat", "type": "leaf"}
            ]},
            {"label": "Insect Biotechnology", "type": "branch", "date": "Insects", "children": [
                {"label": "Sterile Insect Technique: Releasing sterile male mosquitoes to suppress vectors of Dengue and Zika", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पशु जैव प्रौद्योगिकी", "type": "branch", "date": "पशु", "children": [
                {"label": "ट्रांसजेनिक्स: दूध में दवा प्रोटीन का उत्पादन (बायोफार्मा) करने के लिए ट्रांसजेनिक पशुधन बनाना", "type": "leaf"},
                {"label": "क्लोनिंग: दैहिक कोशिका परमाणु स्थानांतरण (SCNT) तकनीक; डोली भेड़ और नूरी पश्मीना बकरी का निर्माण", "type": "leaf"}
            ]},
            {"label": "कीट जैव प्रौद्योगिकी", "type": "branch", "date": "कीट", "children": [
                {"label": "बाँझ कीट तकनीक: डेंगू और जीका के वाहकों को दबाने के लिए बाँझ नर मच्छरों को छोड़ना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biological-fuel-generation"],
        "en": [
            {"label": "Biofuel Generations", "type": "branch", "date": "Biofuels", "children": [
                {"label": "1st Generation: Produced from food crops (starch, sugar, vegetable oil) yielding bioethanol and biodiesel", "type": "leaf"},
                {"label": "2nd Generation: Derived from non-food lignocellulosic biomass (wood, crop residues, straw)", "type": "leaf"},
                {"label": "3rd Generation: Cultivated from lipid-rich microalgae, requiring minimal arable land", "type": "leaf"},
                {"label": "4th Generation: Electrofuels and genetically modified algae absorbing CO2 directly to generate hydrocarbons", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव ईंधन की पीढ़ियां", "type": "branch", "date": "जैव ईंधन", "children": [
                {"label": "पहली पीढ़ी: खाद्य फसलों (स्टार्च, चीनी, वनस्पति तेल) से उत्पादित बायोएथेनॉल और बायोडीजल", "type": "leaf"},
                {"label": "दूसरी पीढ़ी: गैर-खाद्य लिग्नोसेल्युलोसिक बायोमास (लकड़ी, फसल अवशेष, पुआल) से प्राप्त", "type": "leaf"},
                {"label": "तीसरी पीढ़ी: लिपिड-समृद्ध सूक्ष्म शैवाल (Microalgae) से संवर्धित, न्यूनतम कृषि भूमि की आवश्यकता", "type": "leaf"},
                {"label": "चौथी पीढ़ी: इलेक्ट्रोफ्यूल और सीधे हाइड्रोकार्बन उत्पन्न करने के लिए CO2 को अवशोषित करने वाले आनुवंशिक रूप से संशोधित शैवाल", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biotechnology-and-medicine"],
        "en": [
            {"label": "Diagnostics & Vaccines", "type": "branch", "date": "Diagnostics", "children": [
                {"label": "PCR assays: Polymerase Chain Reaction to replicate DNA, enabling ultra-early detection of viral infections", "type": "leaf"},
                {"label": "Recombinant Vaccines: Hepatitis B vaccine produced by cloning viral antigen genes in yeast cells", "type": "leaf"}
            ]},
            {"label": "Therapeutic Biotech", "type": "branch", "date": "Therapeutics", "children": [
                {"label": "Humulin: First recombinant human insulin produced in E. coli bacteria (licensed in 1982)", "type": "leaf"},
                {"label": "Monoclonal Antibodies: Lab-engineered proteins targeting specific receptors on cancer cells", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "निदान और टीके", "type": "branch", "date": "निदान", "children": [
                {"label": "PCR परीक्षण: डीएनए की नकल बनाने के लिए पोलीमरेज़ चेन रिएक्शन, वायरस का बहुत पहले पता लगाना", "type": "leaf"},
                {"label": "पुनः संयोजक टीके (Recombinant): यीस्ट कोशिकाओं में वायरल एंटीजन जीन की क्लोनिंग करके उत्पादित हेपेटाइटिस बी टीका", "type": "leaf"}
            ]},
            {"label": "चिकित्सीय जैव प्रौद्योगिकी", "type": "branch", "date": "उपचार", "children": [
                {"label": "ह्युमुलिन (Humulin): ई. कोली बैक्टीरिया में उत्पादित पहला पुनः संयोजक मानव इंसुलिन (1982)", "type": "leaf"},
                {"label": "मोनोक्लोनल एंटीबॉडी: कैंसर कोशिकाओं पर विशिष्ट रिसेप्टर्स को लक्षित करने के लिए लैब-इंजीनियर्ड प्रोटीन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["biotechnology-in-india"],
        "en": [
            {"label": "Indian Institutional Setup", "type": "branch", "date": "Institutions", "children": [
                {"label": "Department of Biotechnology (DBT): Formed in 1986 under Ministry of Science and Technology to oversee research funding", "type": "leaf"},
                {"label": "GEAC regulator: Genetic Engineering Appraisal Committee under MoEFCC; statutory body approving commercial trials of GMOs", "type": "leaf"},
                {"label": "BIRAC unit: Biotechnology Industry Research Assistance Council; supports startups and industrial R&D projects", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "भारतीय संस्थागत ढांचा", "type": "branch", "date": "संस्थान", "children": [
                {"label": "जैव प्रौद्योगिकी विभाग (DBT): अनुसंधान वित्तपोषण की निगरानी के लिए विज्ञान और प्रौद्योगिकी मंत्रालय के तहत 1986 में गठित", "type": "leaf"},
                {"label": "GEAC नियामक: पर्यावरण मंत्रालय (MoEFCC) के तहत आनुवंशिक इंजीनियरिंग मूल्यांकन समिति; GMOs के वाणिज्यिक परीक्षणों को मंजूरी देने वाला वैधानिक निकाय", "type": "leaf"},
                {"label": "BIRAC इकाई: जैव प्रौद्योगिकी उद्योग अनुसंधान सहायता परिषद; स्टार्टअप्स और औद्योगिक R&D परियोजनाओं का समर्थन करती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["classification-and-domains-of-life"],
        "en": [
            {"label": "Three Domain System", "type": "branch", "date": "3 Domains", "children": [
                {"label": "Archaea: Single-celled prokaryotes with distinctive ribosomal RNA, surviving in extreme environments (hydrothermal vents)", "type": "leaf"},
                {"label": "Bacteria: True single-celled prokaryotic microorganisms lacking nuclear membranes and membrane-bound organelles", "type": "leaf"},
                {"label": "Eukarya: Organisms containing complex cells with defined nuclei, encompassing Protists, Fungi, Plants, and Animals", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "तीन डोमेन प्रणाली", "type": "branch", "date": "3 डोमेन", "children": [
                {"label": "आर्किया (Archaea): विशिष्ट राइबोसोमल आरएनए वाले एक-कोशकीय प्रोकैरियोट्स, जो चरम वातावरण (गर्म झरनों) में जीवित रहते हैं", "type": "leaf"},
                {"label": "बैक्टीरिया (Bacteria): परमाणु झिल्ली और झिल्ली-बद्ध अंगों से रहित सच्चे एक-कोशकीय प्रोकैरियोटिक सूक्ष्मजीव", "type": "leaf"},
                {"label": "यूकेरिया (Eukarya): परिभाषित नाभिक वाली जटिल कोशिकाओं वाले जीव, जिनमें प्रोटिस्ट, कवक, पौधे और जानवर शामिल हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["communicable-diseases"],
        "en": [
            {"label": "Transmission & Pathogens", "type": "branch", "date": "Pathogens", "children": [
                {"label": "Bacterial: Tuberculosis (caused by Mycobacterium tuberculosis), Cholera (Vibrio cholerae), and Typhoid", "type": "leaf"},
                {"label": "Viral: Influenza, Dengue (Flavivirus transmitted by Aedes aegypti), Hepatitis, and HIV/AIDS", "type": "leaf"},
                {"label": "Protozoan: Malaria (Plasmodium species transmitted by female Anopheles mosquitoes)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संचरण और रोगजनक", "type": "branch", "date": "रोगजनक", "children": [
                {"label": "बैक्टीरिया जनित: तपेदिक (माइकोबैक्टीरियम ट्यूबरकुलोसिस के कारण), हैजा (विब्रियो कोलेरी), और टाइफाइड", "type": "leaf"},
                {"label": "वायरल (विषाणु): इन्फ्लुएंजा, डेंगू (एडिस एजिप्टी द्वारा फैलने वाला फ्लेविवायरस), हेपेटाइटिस, और एचआईवी/एड्स", "type": "leaf"},
                {"label": "प्रोटोजोआ जनित: मलेरिया (मादा एनोफिलीज मच्छरों द्वारा प्रसारित प्लास्मोडियम प्रजाति)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["department-of-bt"],
        "en": [
            {"label": "DBT Administration", "type": "branch", "date": "DBT", "children": [
                {"label": "History: Established in 1986; operates under Ministry of Science & Technology, Government of India", "type": "leaf"},
                {"label": "Autonomous Institutes: Administers NII (Immunology), NCCS (Cell Science), and InStem (Stem Cell Science)", "type": "leaf"},
                {"label": "Key Programs: Genome India Project (mapping diversity of Indian genome) and National Biopharma Mission", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "DBT प्रशासन", "type": "branch", "date": "DBT", "children": [
                {"label": "इतिहास: 1986 में स्थापित; भारत सरकार के विज्ञान और प्रौद्योगिकी मंत्रालय के तहत संचालित", "type": "leaf"},
                {"label": "स्वायत्त संस्थान: NII (प्रतिरक्षा विज्ञान), NCCS (कोशिका विज्ञान), और InStem (स्टेम सेल विज्ञान) का प्रशासन करता है", "type": "leaf"},
                {"label": "प्रमुख कार्यक्रम: जीनोम इंडिया प्रोजेक्ट (भारतीय जीनोम की विविधता का मानचित्रण) और राष्ट्रीय बायोफार्मा मिशन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["designer-babies-or-three-parents-babies"],
        "en": [
            {"label": "Mitochondrial Replacement Therapy", "type": "branch", "date": "MRT", "children": [
                {"label": "Concept: In vitro fertilization technique replacing faulty maternal mitochondrial DNA with healthy donor mitochondria", "type": "leaf"},
                {"label": "Methods: Maternal Spindle Transfer (done before fertilization) and Pronuclear Transfer (done after fertilization)", "type": "leaf"},
                {"label": "Genetic makeup: Child inherits nuclear DNA from mother and father (~99.8%) and mitochondrial DNA from donor (~0.2%)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "माइटोकॉन्ड्रियल रिप्लेसमेंट थेरेपी", "type": "branch", "date": "MRT", "children": [
                {"label": "अवधारणा: इन विट्रो फर्टिलाइजेशन तकनीक जो त्रुटिपूर्ण मातृ माइटोकॉन्ड्रियल डीएनए को स्वस्थ दाता माइटोकॉन्ड्रिया से बदलती है", "type": "leaf"},
                {"label": "विधियाँ: मातृ स्पिंडल स्थानांतरण (निषेचन से पहले) और प्रोन्यूक्लियर स्थानांतरण (निषेचन के बाद)", "type": "leaf"},
                {"label": "आनुवंशिक संरचना: बच्चे को माता और पिता से परमाणु डीएनए (~99.8%) और दाता से माइटोकॉन्ड्रियल डीएनए (~0.2%) विरासत में मिलता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["dna-sequencing"],
        "en": [
            {"label": "Sequencing Technologies", "type": "branch", "date": "Sequencing", "children": [
                {"label": "Sanger Method: 1st generation; uses chain-terminating dideoxynucleotides, highly accurate for short DNA fragments", "type": "leaf"},
                {"label": "Next-Generation (NGS): 2nd generation; high-throughput massive parallel sequencing, reading millions of fragments simultaneously", "type": "leaf"},
                {"label": "Third-Generation: Nanopore sequencing; monitors ionic current changes as single DNA strands pass through synthetic nanopores", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डीएनए अनुक्रमण तकनीकें", "type": "branch", "date": "अनुक्रमण", "children": [
                {"label": "सेंगर विधि: पहली पीढ़ी; चेन-टर्मिनेटिंग डिडोक्सीन्यूक्लियोटाइड्स का उपयोग करती है, छोटे टुकड़ों के लिए अत्यधिक सटीक", "type": "leaf"},
                {"label": "नेक्स्ट-जेनरेशन (NGS): दूसरी पीढ़ी; बड़े पैमाने पर समानांतर अनुक्रमण (Parallel Sequencing), एक साथ लाखों टुकड़ों को पढ़ना", "type": "leaf"},
                {"label": "तीसरी पीढ़ी: नैनोपोर अनुक्रमण; कृत्रिम नैनोपोर से एकल डीएनए स्ट्रैंड गुजरने पर आयनिक धारा परिवर्तनों की निगरानी", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["dna-the-genetic-material"],
        "en": [
            {"label": "DNA Structure", "type": "branch", "date": "DNA Basics", "children": [
                {"label": "Double Helix: Discovered by Watson and Crick (1953); composed of two antiparallel polynucleotide chains coiled around a central axis", "type": "leaf"},
                {"label": "Nucleotides: Consist of deoxyribose sugar, phosphate group, and nitrogenous bases (Adenine, Thymine, Cytosine, Guanine)", "type": "leaf"},
                {"label": "Complementary Pairing: Adenine binds to Thymine via two hydrogen bonds; Guanine binds to Cytosine via three hydrogen bonds", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डीएनए की संरचना", "type": "branch", "date": "डीएनए बुनियादी", "children": [
                {"label": "डबल हेलिक्स: वाटसन और क्रिक (1953) द्वारा खोजा गया; एक केंद्रीय धुरी के चारों ओर कुंडलित दो एंटीपैरेलल पॉलीन्यूक्लियोटाइड श्रृंखलाएं", "type": "leaf"},
                {"label": "न्यूक्लियोटाइड्स: डीऑक्सीराइबोज शर्करा, फॉस्फेट समूह और नाइट्रोजनस बेस (एडेनिन, थाइमिन, साइटोसिन, गुआनिन) से बने होते हैं", "type": "leaf"},
                {"label": "पूरक युग्मन (Pairing): एडेनिन दो हाइड्रोजन बांड द्वारा थाइमिन से जुड़ता है; गुआनिन तीन हाइड्रोजन बांड द्वारा साइटोसिन से जुड़ता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["economic-zoology-beneficial-animals"],
        "en": [
            {"label": "Beneficial Insect Cultivation", "type": "branch", "date": "Insects", "children": [
                {"label": "Apiculture: Rearing honeybees (Apis mellifera) to harvest honey, royal jelly, and beeswax used in cosmetics", "type": "leaf"},
                {"label": "Sericulture: Rearing silkworms (Bombyx mori) feeding on mulberry leaves to extract natural silk threads from cocoons", "type": "leaf"},
                {"label": "Lac culture: Cultivation of lac insect (Laccifer lacca) secreting natural resin used in varnishes and sealants", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "लाभकारी कीट संवर्धन", "type": "branch", "date": "कीट", "children": [
                {"label": "मधुमक्खी पालन (Apiculture): शहद, रॉयल जेली और सौंदर्य प्रसाधनों में प्रयुक्त मोम निकालने के लिए मधुमक्खियों का पालन", "type": "leaf"},
                {"label": "रेशम उत्पादन (Sericulture): कोकून से प्राकृतिक रेशम के धागे निकालने के लिए शहतूत की पत्तियों पर रेशम के कीड़ों का पालन", "type": "leaf"},
                {"label": "लाख संवर्धन (Lac culture): लाख के कीट (लैसिफर लक्का) का संवर्धन जो वार्निश और सीलेंट में इस्तेमाल होने वाले प्राकृतिक राल का स्राव करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["economic-zoology-harmful-animals"],
        "en": [
            {"label": "Agricultural & Health Pests", "type": "branch", "date": "Pests", "children": [
                {"label": "Crop Pests: Desert locusts (Schistocerca gregaria) forming swarms that devastate vast agricultural crop fields", "type": "leaf"},
                {"label": "Disease Vectors: Anopheles mosquitoes carrying malaria parasites; houseflies transmitting pathogens of typhoid", "type": "leaf"},
                {"label": "Storage Pests: Rice weevil (Sitophilus oryzae) destroying harvested grains in storage silos", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कृषि और स्वास्थ्य कीट", "type": "branch", "date": "कीट", "children": [
                {"label": "फसल कीट: रेगिस्तानी टिड्डियाँ (शिटोसर्का ग्रेगेरिया) जो विशाल कृषि फसलों को नष्ट करने वाले झुंड बनाती हैं", "type": "leaf"},
                {"label": "रोग वाहक: मलेरिया परजीवी ले जाने वाले एनोफिलीज मच्छर; टाइफाइड के रोगजनकों को प्रसारित करने वाली घरेलू मक्खियाँ", "type": "leaf"},
                {"label": "भंडारण कीट: अनाज गोदामों में काटी गई फसलों को नष्ट करने वाले चावल के घुन (सिटोफिलस ओरिजी)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-adrenal-glands"],
        "en": [
            {"label": "Adrenal Structure & Hormones", "type": "branch", "date": "Adrenal", "children": [
                {"label": "Anatomy: Paired triangular glands situated on top of both kidneys; consists of outer cortex and inner medulla", "type": "leaf"},
                {"label": "Adrenal Cortex: Secretes Aldosterone (regulates salt balance) and Cortisol (stress response, elevates blood glucose)", "type": "leaf"},
                {"label": "Adrenal Medulla: Secretes Epinephrine (Adrenaline) and Norepinephrine; triggers 'fight-or-flight' sympathetic reactions", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अधिवृक्क (Adrenal) संरचना और हार्मोन", "type": "branch", "date": "अधिवृक्क", "children": [
                {"label": "शारीरिक रचना: दोनों गुर्दों के ऊपर स्थित त्रिकोणीय ग्रंथियों की जोड़ी; बाहरी कोर्टेक्स और आंतरिक मेडुला से बनी", "type": "leaf"},
                {"label": "अधिवृक्क कोर्टेक्स: एल्डोस्टेरोन (नमक संतुलन) और कोर्टिसोल (तनाव प्रतिक्रिया, ग्लूकोज बढ़ाना) का स्राव करता है", "type": "leaf"},
                {"label": "अधिवृक्क मेडुला: एपिनेफ्रीन (एड्रेनालाईन) और नोरइपिनेफ्रीन का स्राव; संकट में 'लड़ो या भागो' प्रतिक्रियाओं को सक्रिय करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-hypothalamus"],
        "en": [
            {"label": "Hypothalamus Functions", "type": "branch", "date": "Hypothalamus", "children": [
                {"label": "Command Center: Basal part of diencephalon in forebrain; bridges nervous system and endocrine system", "type": "leaf"},
                {"label": "Releasing Hormones: Secretes GnRH (stimulates gonadotropins) and TRH to regulate anterior pituitary secretions", "type": "leaf"},
                {"label": "Inhibiting Hormones: Secretes Somatostatin to inhibit growth hormone release from pituitary", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "हाइपोथैलेमस के कार्य", "type": "branch", "date": "हाइपोथैलेमस", "children": [
                {"label": "कमांड सेंटर: अग्रमस्तिष्क में डायेंसिफ़ेलॉन का बेसल भाग; तंत्रिका तंत्र और अंतःस्रावी तंत्र को जोड़ता है", "type": "leaf"},
                {"label": "रिलीजिंग हार्मोन: पीयूष ग्रंथि के स्राव को नियंत्रित करने के लिए GnRH और TRH का स्राव करता है", "type": "leaf"},
                {"label": "इनहिबिटिंग हार्मोन: पीयूष ग्रंथि से वृद्धि हार्मोन (Growth Hormone) के स्राव को रोकने के लिए सोमेटोस्टैटिन का स्राव", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-pineal-body-epiphysis", "endocrine-system-pineal-body"],
        "en": [
            {"label": "Pineal Gland Core", "type": "branch", "date": "Pineal", "children": [
                {"label": "Anatomy: Small pinecone-shaped endocrine gland located on epithalamus on dorsal side of forebrain", "type": "leaf"},
                {"label": "Melatonin: Secretes hormone Melatonin; regulates 24-hour circadian rhythm (sleep-wake cycle) and body temperature", "type": "leaf"},
                {"label": "Light Sensitivity: Secretion peaks during darkness, suppressed by light inputs received via retina pathway", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पीनियल ग्रंथि कोर", "type": "branch", "date": "पीनियल", "children": [
                {"label": "शारीरिक रचना: अग्रमस्तिष्क के पृष्ठीय भाग पर एपिथैलेमस में स्थित छोटी चीड़ के शंकु के आकार की अंतःस्रावी ग्रंथि", "type": "leaf"},
                {"label": "मेलाटोनिन (Melatonin): मेलाटोनिन हार्मोन का स्राव; 24 घंटे की सर्केडियन लय (नींद-जागने का चक्र) को नियंत्रित करता है", "type": "leaf"},
                {"label": "प्रकाश संवेदनशीलता: स्राव अंधेरे के दौरान चरम पर होता है, रेटिना से मिलने वाले प्रकाश संकेतों द्वारा दबाया जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-pituitary-gland-hypophysis", "endocrine-system-pituitary-gland"],
        "en": [
            {"label": "Master Gland Anatomy", "type": "branch", "date": "Pituitary", "children": [
                {"label": "Structure: Small pea-sized gland located in a bony cavity called Sella Turcica, attached to hypothalamus", "type": "leaf"},
                {"label": "Anterior Pituitary: Secretes Growth Hormone (GH), Prolactin, Thyroid Stimulating Hormone (TSH), and LH/FSH", "type": "leaf"},
                {"label": "Posterior Pituitary: Stores and releases Oxytocin (triggers uterine contraction) and Vasopressin (ADH; regulates water reabsorption)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पीयूष ग्रंथि (Pituitary)", "type": "branch", "date": "पीयूष", "children": [
                {"label": "शारीरिक रचना: सेला टर्शिका नामक हड्डी की गुहा में स्थित मटर के आकार की ग्रंथि, जो हाइपोथैलेमस से जुड़ी होती है", "type": "leaf"},
                {"label": "अग्र पीयूष (Anterior): वृद्धि हार्मोन (GH), प्रोलैक्टिन, थायराइड उत्तेजक हार्मोन (TSH) और LH/FSH का स्राव करता है", "type": "leaf"},
                {"label": "पश्च पीयूष (Postery): ऑक्सीटोसिन (गर्भाशय संकुचन) और वासोप्रेसिन (ADH; जल पुनरावशोषण) का भंडारण और रिलीज करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-reproductive-glands"],
        "en": [
            {"label": "Gonadal Endocrine Roles", "type": "branch", "date": "Gonads", "children": [
                {"label": "Testes: Secretes Androgens (primarily Testosterone) from Leydig cells; regulates male secondary sexual characters and spermatogenesis", "type": "leaf"},
                {"label": "Ovaries: Secretes Estrogen (produced by growing ovarian follicles) and Progesterone (secreted by corpus luteum, supports pregnancy)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जनन ग्रंथियों की भूमिका", "type": "branch", "date": "जनन ग्रंथियां", "children": [
                {"label": "वृषण (Testes): लेडिग कोशिकाओं से एण्ड्रोजन (टेस्टोस्टेरोन) का स्राव; पुरुष यौन लक्षणों और शुक्राणुजनन को नियंत्रित करता है", "type": "leaf"},
                {"label": "अंडाशय (Ovaries): एस्ट्रोजन (बढ़ते रोमों द्वारा उत्पादित) और प्रोजेस्टेरोन (कॉर्पस ल्यूटियम द्वारा स्रावित, गर्भावस्था का समर्थन) का स्राव", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["endocrine-system-thyroid"],
        "en": [
            {"label": "Thyroid Core", "type": "branch", "date": "Thyroid", "children": [
                {"label": "Anatomy: Butterfly-shaped bilateral lobed gland located on either side of trachea in neck, connected by isthmus", "type": "leaf"},
                {"label": "Thyroid Hormones: Secretes Thyroxine (T4) and Triiodothyronine (T3) containing iodine; regulates Basal Metabolic Rate (BMR)", "type": "leaf"},
                {"label": "Calcitonin: Secretes Thyrocalcitonin (TCT) hormone, lowering blood calcium levels by promoting bone deposition", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "थायराइड ग्रंथि", "type": "branch", "date": "थायराइड", "children": [
                {"label": "शारीरिक रचना: गर्दन में श्वासनली (Trachea) के दोनों ओर स्थित तितली के आकार की ग्रंथि, जो इस्थमस द्वारा जुड़ी होती है", "type": "leaf"},
                {"label": "थायराइड हार्मोन: आयोडीन युक्त थायरोक्सिन (T4) और ट्राई-आयोडोथायरोनिन (T3) का स्राव; बेसल मेटाबॉलिक रेट (BMR) का नियमन", "type": "leaf"},
                {"label": "कैल्सीटोनिन: थायरोकैल्सीटोनिन (TCT) हार्मोन का स्राव, जो हड्डियों में जमाव को बढ़ावा देकर रक्त कैल्शियम के स्तर को कम करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["excretory-system"],
        "en": [
            {"label": "Human Urinary System", "type": "branch", "date": "Excretory", "children": [
                {"label": "Kidneys: Paired bean-shaped organs containing functional filtration units called Nephrons", "type": "leaf"},
                {"label": "Nephron Anatomy: Glomerulus (blood filtration), Bowman's Capsule, and Loop of Henle regulating urine concentration", "type": "leaf"},
                {"label": "Excretory Waste: Humans are Ureotelic, secreting urea synthesized in the liver via the ornithine cycle", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मानव उत्सर्जन प्रणाली", "type": "branch", "date": "उत्सर्जन", "children": [
                {"label": "गुर्दे (Kidneys): सेम के आकार के अंगों की जोड़ी जिसमें नेफ्रॉन (Nephrons) नामक कार्यात्मक निस्पंदन इकाइयां होती हैं", "type": "leaf"},
                {"label": "नेफ्रॉन संरचना: ग्लोमेरुलस (रक्त निस्पंदन), बोमन कैप्सूल, और मूत्र सांद्रता को नियंत्रित करने वाला हेनले का लूप", "type": "leaf"},
                {"label": "उत्सर्जी अपशिष्ट: मनुष्य यूरियोटैलिक (Ureotelic) हैं, जो यकृत में ऑर्निथिन चक्र द्वारा संश्लेषित यूरिया का उत्सर्जन करते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["food-and-beverage-biotechnology"],
        "en": [
            {"label": "Food Fermentation & Enzymes", "type": "branch", "date": "Food BT", "children": [
                {"label": "Fermentation: Yeast (Saccharomyces cerevisiae) fermenting sugars to produce carbon dioxide (bread rising) and ethanol (brewing)", "type": "leaf"},
                {"label": "Enzymes: Chymosin produced in genetically engineered microbes used to curdle milk in industrial cheese production", "type": "leaf"},
                {"label": "Probiotics: Live beneficial bacterial cultures (Lactobacillus acidophilus) promoting intestinal digestive health", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "खाद्य किण्वन और एंजाइम", "type": "branch", "date": "खाद्य BT", "children": [
                {"label": "किण्वन (Fermentation): यीस्ट द्वारा शर्करा का किण्वन करके कार्बन डाइऑक्साइड (ब्रेड फुलाना) और एथेनॉल बनाना", "type": "leaf"},
                {"label": "एंजाइम: पनीर निर्माण में दूध को फाड़ने के लिए आनुवंशिक रूप से संशोधित रोगाणुओं में उत्पादित काइमोसिन (Chymosin)", "type": "leaf"},
                {"label": "प्रोबायोटिक्स: जीवित लाभकारी बैक्टीरिया (लैक्टोबैसिलस) जो आंतों के पाचन स्वास्थ्य को बढ़ावा देते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["gene-expression"],
        "en": [
            {"label": "Transcription & Translation", "type": "branch", "date": "Expression", "children": [
                {"label": "Transcription: Synthesis of single-stranded messenger RNA (mRNA) from DNA template, mediated by RNA Polymerase enzyme", "type": "leaf"},
                {"label": "Translation: Ribosomes decoding mRNA codons to synthesize polypeptide chains, supported by tRNA amino-acid carriers", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ट्रांसक्रिप्शन और ट्रांसलेशन", "type": "branch", "date": "अभिव्यक्ति", "children": [
                {"label": "ट्रांसक्रिप्शन (अनुलेखन): आरएनए पोलीमरेज़ एंजाइम द्वारा डीएनए टेम्पलेट से एकल-स्ट्रैंडेड मैसेंजर आरएनए (mRNA) का संश्लेषण", "type": "leaf"},
                {"label": "ट्रांसलेशन (अनुवाद): राइबोसोम द्वारा प्रोटीन श्रृंखलाओं को संश्लेषित करने के लिए mRNA कोडन को डिकोड करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["gene-regulation"],
        "en": [
            {"label": "Regulatory Mechanisms", "type": "branch", "date": "Regulation", "children": [
                {"label": "Lac Operon: Classic bacterial model in E. coli; expression of lactose digesting genes controlled by operator-repressor binding", "type": "leaf"},
                {"label": "Epigenetics: Modifying DNA expression via DNA methylation or histone acetylation without altering genetic sequence", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नियामक तंत्र", "type": "branch", "date": "नियमन", "children": [
                {"label": "लैक ऑपेरॉन (Lac Operon): ई. कोली में जीवाणु मॉडल; ऑपरेटर-रिप्रेशर बाइंडिंग द्वारा नियंत्रित लैक्टोज पाचन जीन की अभिव्यक्ति", "type": "leaf"},
                {"label": "एपिजेनेटिक्स (Epigenetics): आनुवंशिक अनुक्रम को बदले बिना डीएनए मिथाइलेशन या हिस्टोन एसिटिलेशन द्वारा जीन अभिव्यक्ति को बदलना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["general-biologyclassification-of-living-thingsviruses"],
        "en": [
            {"label": "Classification of Living Things", "type": "branch", "date": "Classification", "children": [
                {"label": "Taxonomy Hierarchy: Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species", "type": "leaf"},
                {"label": "Five Kingdoms: Monera (prokaryotes), Protista (unicellular eukaryotes), Fungi, Plantae, Animalia", "type": "leaf"}
            ]},
            {"label": "Virus Characteristics", "type": "branch", "date": "Viruses", "children": [
                {"label": "Structure: Non-cellular entities consisting of a nucleic acid core (DNA or RNA) enclosed within a protein coat called Capsid", "type": "leaf"},
                {"label": "Replication: Obligate intracellular parasites; can only replicate inside active living host cells by hijacking machinery", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जीवों का वर्गीकरण", "type": "branch", "date": "वर्गीकरण", "children": [
                {"label": "वर्गीकरण पदानुक्रम: डोमेन, जगत (Kingdom), संघ (Phylum), वर्ग, गण, कुल, वंश, और जाति (Species)", "type": "leaf"},
                {"label": "पांच जगत प्रणाली: मोनेरा (प्रोकैरियोट्स), प्रोटिस्टा (एक-कोशकीय यूकेरियोट्स), कवक (Fungi), पादप और जंतु जगत", "type": "leaf"}
            ]},
            {"label": "विषाणु (Virus) के लक्षण", "type": "branch", "date": "विषाणु", "children": [
                {"label": "संरचना: अकोशिकीय जीव जिनमें न्यूक्लिक एसिड कोर (डीएनए या आरएनए) होता है, जो कैप्सिड नामक प्रोटीन कोट के भीतर बंद होता है", "type": "leaf"},
                {"label": "प्रतिकृति: परजीवी जीव; मेजबान कोशिकाओं के मशीनरी तंत्र पर कब्जा करके केवल जीवित कोशिकाओं के भीतर ही प्रजनन कर सकते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["genetic-engineering"],
        "en": [
            {"label": "Tools & Techniques", "type": "branch", "date": "Engineering", "children": [
                {"label": "CRISPR-Cas9: Gene editing tool adapted from bacterial immunity, using guide RNA to cut DNA at precise target sites", "type": "leaf"},
                {"label": "Vector Insertion: Inserting foreign genes into host genomes using modified plasmids or viral delivery vectors", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उपकरण और तकनीकें", "type": "branch", "date": "इंजीनियरिंग", "children": [
                {"label": "CRISPR-Cas9: जीवाणु प्रतिरक्षा से ली गई जीन संपादन तकनीक, जो लक्षित साइटों पर डीएनए काटने के लिए गाइड आरएनए का उपयोग करती है", "type": "leaf"},
                {"label": "वेक्टर इंसर्शन: संशोधित प्लास्मिड या वायरल वैक्टर का उपयोग करके मेजबान जीनोम में बाहरी जीन को डालना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["genetics-and-biotechnology"],
        "en": [
            {"label": "Genetic Foundations", "type": "branch", "date": "Genetics Core", "children": [
                {"label": "Genomics: Branch analyzing complete genetic sequences (genomes) to identify genetic markers and mutations", "type": "leaf"},
                {"label": "Marker Assisted Selection: Accelerating conventional breeding by selecting plants with specific DNA markers associated with traits", "type": "leaf"}
            ]},
            {"label": "Biotechnology Applications", "type": "branch", "date": "Biotech Apps", "children": [
                {"label": "Gene Editing: Using CRISPR-Cas9 to make site-specific double-strand breaks in DNA for precise modification", "type": "leaf"},
                {"label": "Transgenics: Inserting recombinant DNA sequences into host genomes to express foreign proteins or traits", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "आनुवंशिकी के मूल सिद्धांत", "type": "branch", "date": "आनुवंशिकी", "children": [
                {"label": "जीनोमिक्स: आनुवंशिक मार्करों और उत्परिवर्तन की पहचान करने के लिए पूर्ण आनुवंशिक अनुक्रमों (जीनोम) का विश्लेषण करने वाली शाखा", "type": "leaf"},
                {"label": "मार्कर असिस्टेड सिलेक्शन: लक्षणों से जुड़े विशिष्ट डीएनए मार्करों वाले पौधों का चयन करके पारंपरिक प्रजनन को तेज करना", "type": "leaf"}
            ]},
            {"label": "जैव प्रौद्योगिकी अनुप्रयोग", "type": "branch", "date": "Biotech अनुप्रयोग", "children": [
                {"label": "जीन संपादन (Gene Editing): विशिष्ट लक्षित साइटों पर डीएनए को काटने और बदलने के लिए CRISPR-Cas9 का उपयोग", "type": "leaf"},
                {"label": "ट्रांसजेनिक्स: बाहरी प्रोटीन या लक्षणों को व्यक्त करने के लिए मेजबान जीनोम में पुनः संयोजक डीएनए अनुक्रम डालना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["global-warming-and-the-significance-of-fossils-fuels"],
        "en": [
            {"label": "Global Warming", "type": "branch", "date": "Global Warming", "children": [
                {"label": "Greenhouse Effect: Traps outgoing infrared heat radiation in the atmosphere via greenhouse gases like CO2, CH4, and N2O", "type": "leaf"},
                {"label": "Consequences: Rising average temperatures, thermal expansion of oceans, melting glaciers, and shifting agricultural zones", "type": "leaf"}
            ]},
            {"label": "Significance of Fossil Fuels", "type": "branch", "date": "Fossil Fuels", "children": [
                {"label": "Energy Density: Concentrated hydrocarbons providing high energy output, historically driving the industrial revolution", "type": "leaf"},
                {"label": "Baseload Power: Offers reliable, non-intermittent electricity generation compared to early solar and wind platforms", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ग्लोबल वार्मिंग", "type": "branch", "date": "ग्लोबल वार्मिंग", "children": [
                {"label": "ग्रीनहाउस प्रभाव: CO2, CH4 और N2O जैसी ग्रीनहाउस गैसों के माध्यम से वातावरण में अवरक्त ऊष्मा विकिरण को रोकना", "type": "leaf"},
                {"label": "परिणाम: औसत तापमान में वृद्धि, महासागरों का तापीय विस्तार, ग्लेशियरों का पिघलना और कृषि चक्र में बदलाव", "type": "leaf"}
            ]},
            {"label": "जीवाश्म ईंधन का महत्व", "type": "branch", "date": "जीवाश्म ईंधन", "children": [
                {"label": "ऊर्जा घनत्व: संकेंद्रित हाइड्रोकार्बन जो उच्च ऊर्जा उत्पादन प्रदान करते हैं, जिन्होंने ऐतिहासिक रूप से औद्योगिक क्रांति को गति दी", "type": "leaf"},
                {"label": "बेसलोड बिजली: शुरुआती सौर और पवन ऊर्जा की तुलना में विश्वसनीय, निरंतर बिजली उत्पादन प्रदान करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["human-animal-evolution"],
        "en": [
            {"label": "Evolutionary Milestones", "type": "branch", "date": "Evolution", "children": [
                {"label": "Darwinism: Theory of natural selection; organisms with advantageous traits survive and reproduce more successfully", "type": "leaf"},
                {"label": "Hominid divergence: Split from common primate ancestors ~6 million years ago, leading to bipedalism and larger brain capacity (Homo sapiens)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विकासवादी मील के पत्थर", "type": "branch", "date": "विकास", "children": [
                {"label": "डार्विनवाद: प्राकृतिक चयन का सिद्धांत; लाभकारी लक्षणों वाले जीव जीवित रहते हैं और अधिक सफलतापूर्वक प्रजनन करते हैं", "type": "leaf"},
                {"label": "होमिनिड विचलन: लगभग 6 मिलियन वर्ष पूर्व वानरों से अलग होना, जिससे द्विपदवाद (Bipedalism) और बड़े मस्तिष्क का विकास हुआ", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["industrial-genetics"],
        "en": [
            {"label": "Industrial Microbial Yields", "type": "branch", "date": "Industrial Genetics", "children": [
                {"label": "Strain Improvement: Mutagenesis and genetic editing of microbial strains to optimize yield of enzymes, amino acids, and organic acids", "type": "leaf"},
                {"label": "Bioreactors: Large vessels maintaining optimal temperature, pH, and oxygen to ferment engineered microbes at scale", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "औद्योगिक सूक्ष्मजीव उत्पादन", "type": "branch", "date": "औद्योगिक आनुवंशिकी", "children": [
                {"label": "स्ट्रेन सुधार: एंजाइमों, अमीनो एसिड और कार्बनिक अम्लों के उत्पादन को बढ़ाने के लिए सूक्ष्मजीव उपभेदों का अनुवांशिक संपादन", "type": "leaf"},
                {"label": "बायोरिएक्टर (Bioreactors): बड़े बर्तन जो बड़े पैमाने पर सूक्ष्मजीवों को किण्वित करने के लिए अनुकूलतम तापमान, पीएच बनाए रखते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["inheritance-genetics", "inheritance"],
        "en": [
            {"label": "Mendelian Inheritance", "type": "branch", "date": "Mendelian", "children": [
                {"label": "Gregor Mendel: Monohybrid and dihybrid crosses of pea plants established rules of genetic transmission", "type": "leaf"},
                {"label": "Mendel's Laws: Law of Segregation (alleles separate during gamete formation) and Law of Independent Assortment", "type": "leaf"},
                {"label": "Chromosomal Theory: Sutton and Boveri identified chromosomes as carriers of Mendelian genetic factors", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मेंडेलियन आनुवंशिकी", "type": "branch", "date": "मेंडेलियन", "children": [
                {"label": "ग्रेगर मेंडल: मटर के पौधों पर एकसंकर (Monohybrid) और द्विसंकर (Dihybrid) प्रयोगों से आनुवंशिक संचरण के नियम स्थापित किए", "type": "leaf"},
                {"label": "मेंडल के नियम: पृथक्करण का नियम (युग्मक निर्माण के दौरान एलील अलग होते हैं) और स्वतंत्र अपव्यूहन का नियम", "type": "leaf"},
                {"label": "गुणसूत्र सिद्धांत: सटन और बोवेरी ने गुणसूत्रों (Chromosomes) को मेंडेलियन आनुवंशिक कारकों के वाहक के रूप में पहचाना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["intellectual-property-rights-meaning-and-types", "intellectual-property-rights"],
        "en": [
            {"label": "IPR Categorization", "type": "branch", "date": "IPR Types", "children": [
                {"label": "Patents: Temporary monopoly rights (20 years in India) granted to inventors for novel, industrial-grade technological solutions", "type": "leaf"},
                {"label": "Copyrights: Protection for literary, dramatic, musical, and artistic works, lasting for author's life plus 60 years", "type": "leaf"},
                {"label": "Trademarks: Symbols, names, or designs identifying commercial sources of goods or services, preventing consumer confusion", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "IPR का वर्गीकरण", "type": "branch", "date": "IPR प्रकार", "children": [
                {"label": "पेटेंट (Patents): नवीन, औद्योगिक-ग्रेड तकनीकी समाधानों के लिए आविष्कारकों को दिए गए अस्थायी एकाधिकार अधिकार (भारत में 20 वर्ष)", "type": "leaf"},
                {"label": "कॉपीराइट (Copyrights): साहित्यिक, नाटकीय, संगीत और कलात्मक कार्यों के लिए संरक्षण, लेखक के जीवनकाल प्लस 60 वर्ष तक", "type": "leaf"},
                {"label": "ट्रेडमार्क (Trademarks): वस्तुओं या सेवाओं के व्यावसायिक स्रोतों की पहचान करने वाले प्रतीक, नाम या डिज़ाइन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ipr-and-agriculture"],
        "en": [
            {"label": "Agricultural Intellectual Property", "type": "branch", "date": "IPR Agriculture", "children": [
                {"label": "PPV&FR Act 2001: Protection of Plant Varieties and Farmers' Rights in India; protects breeders' IP while safeguarding traditional farmers' seed exchange rights", "type": "leaf"},
                {"label": "TRIPS Agreement: WTO treaty mandating intellectual property standards, allowing patenting of microorganisms and GM crop varieties", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कृषि बौद्धिक संपदा", "type": "branch", "date": "IPR कृषि", "children": [
                {"label": "PPV&FR अधिनियम 2001: भारत में पौधों की किस्मों और किसानों के अधिकारों का संरक्षण अधिनियम; किसानों के बीज विनिमय अधिकारों की रक्षा", "type": "leaf"},
                {"label": "TRIPS समझौता: WTO संधि जो बौद्धिक संपदा मानकों को अनिवार्य करती है, सूक्ष्मजीवों और जीएम किस्मों के पेटेंट की अनुमति देती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["landfilling-technologies"],
        "en": [
            {"label": "Engineering Landfills", "type": "branch", "date": "Landfills", "children": [
                {"label": "Composite Liners: Heavy high-density polyethylene (HDPE) liners layered over clay to prevent groundwater contamination", "type": "leaf"},
                {"label": "Leachate Extraction: Perforated pipe networks collecting toxic fluids and pumping them to wastewater treatment stations", "type": "leaf"},
                {"label": "Methane recovery: Pipe wells capturing landfill gas (methane) to combust it for electricity generation or flaring", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "इंजीनियरिंग लैंडफिल तकनीक", "type": "branch", "date": "लैंडफिल", "children": [
                {"label": "मिश्रित परत (Liners): भूजल संदूषण को रोकने के लिए मिट्टी के ऊपर बिछाई गई भारी उच्च-घनत्व पॉलीथीन (HDPE) परतें", "type": "leaf"},
                {"label": "लीचेट निष्कर्षण: छिद्रित पाइप नेटवर्क जो जहरीले तरल पदार्थों को एकत्र करते हैं और उन्हें उपचार स्टेशनों पर भेजते हैं", "type": "leaf"},
                {"label": "मीथेन रिकवरी: पाइप कुएं जो लैंडफिल गैस (मीथेन) को पकड़ते हैं ताकि बिजली उत्पादन के लिए इसका दहन किया जा सके", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["microbes-and-the-geological-environment"],
        "en": [
            {"label": "Geomicrobiology", "type": "branch", "date": "Geomicrobiology", "children": [
                {"label": "Bio-weathering: Microbial acids (oxalic, citric) leaching minerals from rocky substrates, initiating soil formation", "type": "leaf"},
                {"label": "Ore Biomining: Acidophilic iron/sulfur oxidizers (Acidithiobacillus) dissolving low-grade copper and gold ores to extract metals", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जियोमाइक्रोबायोलॉजी", "type": "branch", "date": "जियोमाइक्रोबायोलॉजी", "children": [
                {"label": "जैव-अपक्षय (Bio-weathering): चट्टानों से खनिजों को बाहर निकालने वाले माइक्रोबियल एसिड (ऑक्सेलिक), जिससे मिट्टी निर्माण शुरू होता है", "type": "leaf"},
                {"label": "बायोमाइनिंग: तांबा और सोना निकालने के लिए अयस्कों को घोलने वाले एसिडोफिलिक आयरन/सल्फर ऑक्सीडाइज़र", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["microbial-ecology-environmental-biotechnology"],
        "en": [
            {"label": "Microbial Interactions", "type": "branch", "date": "Microbial Ecology", "children": [
                {"label": "Biostimulation: Injecting nutrients (nitrogen, phosphorus) into contaminated groundwater grids to stimulate native pollutant-eating microbes", "type": "leaf"},
                {"label": "Bioaugmentation: Adding specialized, laboratory-cultured microbial strains to digest persistent organic pollutants (pesticides, plastics)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सूक्ष्मजीव पारिस्थितिकी", "type": "branch", "date": "पर्यावरण BT", "children": [
                {"label": "बायोस्टिमुलेशन: प्रदूषक खाने वाले रोगाणुओं को सक्रिय करने के लिए प्रदूषित भूजल में पोषक तत्व (नाइट्रोजन, फास्फोरस) डालना", "type": "leaf"},
                {"label": "बायोऑगमेंटेशन: कीटनाशकों और प्लास्टिक जैसे जैविक प्रदूषकों को पचाने के लिए विशेष, प्रयोगशाला-संवर्धित रोगाणु डालना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mutation"],
        "en": [
            {"label": "Mutational Variations", "type": "branch", "date": "Mutation", "children": [
                {"label": "Point Mutation: Single nucleotide substitution; causes sickle cell anemia (Valine substituted for Glutamic acid in beta-globin)", "type": "leaf"},
                {"label": "Frame-shift: Insertions or deletions of nucleotides (not multiples of three), shifting the reading frame of codons", "type": "leaf"},
                {"label": "Mutagens: Physical agents (UV radiation, X-rays) or chemical molecules inducing DNA damage and errors", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उत्परिवर्तन (Mutation) के प्रकार", "type": "branch", "date": "उत्परिवर्तन", "children": [
                {"label": "बिंदु उत्परिवर्तन (Point): एकल न्यूक्लियोटाइड प्रतिस्थापन; सिकल सेल एनीमिया का कारण (ग्लूटामिक एसिड की जगह वेलिन)", "type": "leaf"},
                {"label": "फ्रेम-शिफ्ट: न्यूक्लियोटाइड्स का जुड़ना या निकलना (तीन के गुणज नहीं), जिससे कोडन का रीडिंग फ्रेम बदल जाता है", "type": "leaf"},
                {"label": "उत्परिवर्तक (Mutagens): डीएनए क्षति और त्रुटियों को प्रेरित करने वाले भौतिक कारक (यूवी विकिरण) या रासायनिक अणु", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["non-communicable-diseases"],
        "en": [
            {"label": "Chronic Health Conditions", "type": "branch", "date": "NCDs", "children": [
                {"label": "Cardiovascular: Hypertension and atherosclerosis caused by plaque build-up in arteries, blocking blood flow", "type": "leaf"},
                {"label": "Diabetes: Type 1 (lack of insulin production) and Type 2 (cellular insulin resistance related to obesity)", "type": "leaf"},
                {"label": "Oncological: Cancer; uncontrolled cell division triggered by genetic mutations in oncogenes and tumor suppressors", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गैर-संचारी रोग (NCDs)", "type": "branch", "date": "NCDs", "children": [
                {"label": "हृदय रोग: धमनियों में प्लाक जमने के कारण होने वाला उच्च रक्तचाप और एथेरोस्क्लेरोसिस, जो रक्त प्रवाह को रोकता है", "type": "leaf"},
                {"label": "मधुमेह (Diabetes): टाइप 1 (इंसुलिन उत्पादन की कमी) और टाइप 2 (मोटापे से जुड़ी सेलुलर इंसुलिन प्रतिरोध)", "type": "leaf"},
                {"label": "कैंसर (Oncological): ट्यूमर सप्रेसर्स और ऑन्कोजीन में उत्परिवर्तन से शुरू होने वाला अनियंत्रित कोशिका विभाजन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nutrition-classification-by-source-of-energy-and-carbon"],
        "en": [
            {"label": "Nutritional Modalities", "type": "branch", "date": "Nutrition Classes", "children": [
                {"label": "Photoautotrophs: Utilize light energy and Carbon Dioxide to synthesize organic molecules (green plants, cyanobacteria)", "type": "leaf"},
                {"label": "Chemoautotrophs: Extract energy from chemical oxidation of inorganic compounds (sulfur bacteria, nitrifying bacteria)", "type": "leaf"},
                {"label": "Photoheterotrophs: Utilize light energy but must ingest pre-formed organic compounds for carbon source", "type": "leaf"},
                {"label": "Chemoheterotrophs: Obtain both energy and carbon sources from pre-existing organic matter (animals, fungi, most bacteria)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पोषण वर्गीकरण (ऊर्जा और कार्बन)", "type": "branch", "date": "पोषण वर्ग", "children": [
                {"label": "प्रकाश-स्वपोषी (Photoautotrophs): कार्बनिक अणुओं को संश्लेषित करने के लिए प्रकाश ऊर्जा और CO2 का उपयोग (हरे पौधे)", "type": "leaf"},
                {"label": "रसायन-स्वपोषी (Chemoautotrophs): अकार्बनिक यौगिकों के रासायनिक ऑक्सीकरण से ऊर्जा प्राप्त करना (सल्फर बैक्टीरिया)", "type": "leaf"},
                {"label": "प्रकाश-परपोषी (Photoheterotrophs): प्रकाश ऊर्जा का उपयोग करते हैं लेकिन कार्बन के लिए कार्बनिक यौगिकों का सेवन करते हैं", "type": "leaf"},
                {"label": "रसायन-परपोषी (Chemoheterotrophs): पहले से मौजूद कार्बनिक पदार्थों से ऊर्जा और कार्बन दोनों प्राप्त करना (जानवर, कवक)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["origin-of-life-and-cells"],
        "en": [
            {"label": "Abiotic Origins & Organelles", "type": "branch", "date": "Origin of Life", "children": [
                {"label": "Chemical Evolution: Oparin-Haldane hypothesis; primitive atmosphere chemical reactions yielding organic monomers", "type": "leaf"},
                {"label": "Miller-Urey experiment: Simulated primitive Earth conditions; spark discharges yielded amino acids from methane, ammonia, and water", "type": "leaf"},
                {"label": "Endosymbiotic Theory: Mitochondria and chloroplasts originated as free-living prokaryotes engulfed by ancestral eukaryotic cells", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अजैविक उत्पत्ति और कोशिकाएं", "type": "branch", "date": "जीवन की उत्पत्ति", "children": [
                {"label": "रासायनिक विकास: ओपेरिन-हल्दाने परिकल्पना; आदिम वायुमंडलीय प्रतिक्रियाओं द्वारा कार्बनिक मोनोमर्स का उत्पादन", "type": "leaf"},
                {"label": "मिलर-यूरे प्रयोग: आदिम पृथ्वी की परिस्थितियों का अनुकरण; चिंगारी निर्वहन से अमीनो एसिड का निर्माण", "type": "leaf"},
                {"label": "एंडोसिम्बायोटिक सिद्धांत: माइटोकॉन्ड्रिया और क्लोरोप्लास्ट की उत्पत्ति आदिम यूकेरियोटिक कोशिकाओं द्वारा निगले गए प्रोकैरियोट्स से हुई", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["patent-protection-trade-secrets"],
        "en": [
            {"label": "Protection Strategies", "type": "branch", "date": "Patents vs Secrets", "children": [
                {"label": "Patent Route: Requires public disclosure of invention in exchange for 20 years of legally protected monopoly", "type": "leaf"},
                {"label": "Trade Secret Route: Monopolies maintained indefinitely through internal non-disclosure agreements, security, and access barriers (e.g. Coca-Cola formula)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "संरक्षण रणनीतियाँ", "type": "branch", "date": "पेटेंट बनाम सीक्रेट", "children": [
                {"label": "पेटेंट मार्ग: 20 वर्षों के कानूनी रूप से संरक्षित एकाधिकार के बदले आविष्कार के सार्वजनिक प्रकटीकरण की आवश्यकता", "type": "leaf"},
                {"label": "व्यापार रहस्य मार्ग: आंतरिक गैर-प्रकटीकरण समझौतों और सुरक्षा बाधाओं (जैसे कोका-कोला फॉर्मूला) द्वारा बनाए रखा गया एकाधिकार", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["pharmaceuticals-and-biopharmaceuticals"],
        "en": [
            {"label": "Biopharma Production", "type": "branch", "date": "Biopharma", "children": [
                {"label": "Traditional Pharma: Synthesized via chemical reactions, targeting chemical compounds and receptors", "type": "leaf"},
                {"label": "Biopharmaceuticals: Large complex macromolecules produced in living cells (host cells like mammalian CHO lines or yeast)", "type": "leaf"},
                {"label": "Key Products: Recombinant clotting factor VIII (hemophilia therapy) and erythropoietin (anemia treatment)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बायोफार्मा उत्पादन", "type": "branch", "date": "बायोफार्मा", "children": [
                {"label": "पारंपरिक फार्मा: रासायनिक प्रतिक्रियाओं के माध्यम से संश्लेषित, रासायनिक यौगिकों और रिसेप्टर्स को लक्षित करना", "type": "leaf"},
                {"label": "बायोफार्मास्यूटिकल्स: जीवित कोशिकाओं (जैसे स्तनधारी CHO लाइनों या खमीर) में उत्पादित बड़े जटिल मैक्रोमोलेक्यूल्स", "type": "leaf"},
                {"label": "प्रमुख उत्पाद: पुनः संयोजक क्लॉटिंग फैक्टर VIII (हीमोफिलिया थेरेपी) और एरिथ्रोपोइटिन (एनीमिया उपचार)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["photosynthesis"],
        "en": [
            {"label": "Photosynthesis Pathways", "type": "branch", "date": "Photosynthesis", "children": [
                {"label": "Light Reactions: Occurs in thylakoid membranes; splits water molecules (photolysis) to yield Oxygen, ATP, and NADPH", "type": "leaf"},
                {"label": "Dark Reactions: Occurs in stroma; Calvin cycle fixing CO2 into sugars using ATP and NADPH (catalyzed by RuBisCO)", "type": "leaf"},
                {"label": "C4 & CAM: Structural modifications minimizing photorespiration in hot dry climates by separating initial carbon capture and Calvin cycle", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "प्रकाश संश्लेषण मार्ग", "type": "branch", "date": "प्रकाश संश्लेषण", "children": [
                {"label": "प्रकाश रासायनिक अभिक्रिया: थायलाकोइड झिल्ली में; ऑक्सीजन, एटीपी और एनएडीपीएच उत्पन्न करने के लिए पानी का विखंडन", "type": "leaf"},
                {"label": "अप्रकाशिक अभिक्रिया (Calvin): स्ट्रोमा में; RuBisCO द्वारा उत्प्रेरित ATP और NADPH का उपयोग करके CO2 का शर्करा में निर्धारण", "type": "leaf"},
                {"label": "C4 और CAM: गर्म शुष्क जलवायु में प्रारंभिक कार्बन कैप्चर और केल्विन चक्र को अलग करके प्रकाश-श्वसन (Photorespiration) को कम करना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["plant-and-forest-biotechnology"],
        "en": [
            {"label": "Plant Biotechnology", "type": "branch", "date": "Plant BT", "children": [
                {"label": "Micropropagation: Regenerating thousands of clonal plantlets from single tissue explants in sterile nutrient media", "type": "leaf"},
                {"label": "Genetic Modification: Inserting genes for herbicide resistance or pest protection (e.g. Bt genes) into crops", "type": "leaf"}
            ]},
            {"label": "Forest Biotechnology", "type": "branch", "date": "Forest BT", "children": [
                {"label": "Wood Quality: Enhancing density, growth rates, and pulping efficiency of timber tree species", "type": "leaf"},
                {"label": "Disease Resistance: Developing transgenic trees resistant to fungal blights and insect infestations", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पादप जैव प्रौद्योगिकी", "type": "branch", "date": "पादप BT", "children": [
                {"label": "सूक्ष्मप्रवर्धन (Micropropagation): बाँझ पोषक मीडिया में एकल ऊतक से हजारों क्लोनल पौधों का पुनर्जनन", "type": "leaf"},
                {"label": "आनुवंशिक संशोधन: फसलों में शाकनाशी सहिष्णुता या कीट प्रतिरोध (जैसे बीटी जीन) डालना", "type": "leaf"}
            ]},
            {"label": "वन जैव प्रौद्योगिकी", "type": "branch", "date": "वन BT", "children": [
                {"label": "लकड़ी की गुणवत्ता: इमारती लकड़ी की प्रजातियों के घनत्व, विकास दर और लुगदी (Pulping) दक्षता में सुधार", "type": "leaf"},
                {"label": "रोग प्रतिरोध: कवक संक्रमण और कीटों के हमलों के खिलाफ जंगलों में प्रतिरोधी ट्रांसजेनिक पेड़ों का विकास", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["plant-animal-nutrition"],
        "en": [
            {"label": "Macronutrients & Micronutrients", "type": "branch", "date": "Nutrition", "children": [
                {"label": "Plant Mineral Nutrition: Needs Nitrogen (leaves), Phosphorus (roots), Potassium (stomata regulation), and Micronutrients (Iron, Zinc)", "type": "leaf"},
                {"label": "Animal Nutrition: Core digestion of carbohydrates, proteins (broken down into amino acids), fats, and vitamins", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मैक्रोन्यूट्रिएंट्स और माइक्रोन्यूट्रिएंट्स", "type": "branch", "date": "पोषण", "children": [
                {"label": "पादप खनिज पोषण: नाइट्रोजन (पत्तियां), फास्फोरस (जड़ें), पोटेशियम (रंध्र नियमन) और सूक्ष्म पोषक तत्वों (लोहा, जस्ता) की आवश्यकता", "type": "leaf"},
                {"label": "पशु पोषण: कार्बोहाइड्रेट, प्रोटीन (अमीनो एसिड में टूटना), वसा और विटामिन का पाचन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["plant-breeders-rights"],
        "en": [
            {"label": "Plant Variety Protection", "type": "branch", "date": "Breeders Rights", "children": [
                {"label": "UPOV Convention: International treaty defining plant breeders' rights, requiring protected varieties to be Distinct, Uniform, and Stable (DUS)", "type": "leaf"},
                {"label": "Farmers' Exemption: Allows traditional farmers to save, sow, resow, exchange, or share seeds of protected varieties (under PPV&FR Act)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "पादप किस्म संरक्षण", "type": "branch", "date": "प्रजनक अधिकार", "children": [
                {"label": "UPOV कन्वेंशन: पौधों के प्रजनकों के अधिकारों को परिभाषित करने वाली अंतर्राष्ट्रीय संधि, जिसके तहत संरक्षित किस्में विशिष्ट, एकसमान होनी चाहिए", "type": "leaf"},
                {"label": "किसानों की छूट: पारंपरिक किसानों को संरक्षित किस्मों के बीजों को बचाने, बोने, विनिमय करने या साझा करने की अनुमति (PPV&FR के तहत)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["protection-of-biotechnological-inventions"],
        "en": [
            {"label": "Biotech Patentability", "type": "branch", "date": "Biotech Patents", "children": [
                {"label": "Eligible Inventions: Genetically engineered microbes, purified DNA constructs, and transgenic plants (subject to national laws)", "type": "leaf"},
                {"label": "Indian Patent Act Section 3(j): Excludes plants and animals in whole or part (other than microorganisms) from patentability", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बायोटेक पेटेंट पात्रता", "type": "branch", "date": "बायोटेक पेटेंट", "children": [
                {"label": "पात्र आविष्कार: आनुवंशिक रूप से संशोधित रोगाणु, शुद्ध डीएनए संरचनाएं और ट्रांसजेनिक पौधे (राष्ट्रीय कानूनों के अधीन)", "type": "leaf"},
                {"label": "भारतीय पेटेंट अधिनियम धारा 3(j): पौधों और जानवरों को पूरी तरह या आंशिक रूप से (सूक्ष्मजीवों को छोड़कर) पेटेंट पात्रता से बाहर करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["recombinant-dna-technology"],
        "en": [
            {"label": "rDNA Methodology", "type": "branch", "date": "rDNA Tech", "children": [
                {"label": "Restriction Endonucleases: Molecular scissors cutting double-stranded DNA at specific palindromic recognition sequences", "type": "leaf"},
                {"label": "DNA Ligase: Molecular glue linking DNA fragments by catalyzing phosphodiester bond formation", "type": "leaf"},
                {"label": "Plasmids: Extrachromosomal circular DNA molecules in bacteria used as cloning vectors to replicate target inserts", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "rDNA कार्यप्रणाली", "type": "branch", "date": "rDNA तकनीक", "children": [
                {"label": "प्रतिबंध एंडोन्यूक्लिएज: आणविक कैंची जो विशिष्ट पैलिंड्रोमिक अनुक्रमों पर डबल-स्ट्रैंडेड डीएनए को काटती है", "type": "leaf"},
                {"label": "डीएनए लाइगेज: फॉस्फोडाइस्टर बॉन्ड गठन को उत्प्रेरित करके डीएनए के टुकड़ों को जोड़ने वाला आणविक गोंद", "type": "leaf"},
                {"label": "प्लास्मिड: बैक्टीरिया में अतिरिक्त-गुणसूत्रीय गोलाकार डीएनए अणु, जो लक्षित जीन प्रतियों को दोहराने के लिए क्लोनिंग वैक्टर के रूप में उपयोग होते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["reproductive-system"],
        "en": [
            {"label": "Human Reproduction", "type": "branch", "date": "Reproductive", "children": [
                {"label": "Gametogenesis: Spermatogenesis in testes producing haploid sperm; Oogenesis in ovaries yielding haploid ova", "type": "leaf"},
                {"label": "Hormonal Loops: GnRH release from hypothalamus triggers FSH (follicle growth) and LH (triggers ovulation) from anterior pituitary", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मानव प्रजनन प्रणाली", "type": "branch", "date": "प्रजनन", "children": [
                {"label": "युग्मकजनन (Gametogenesis): वृषण में शुक्राणुजनन (शुक्राणु उत्पादन); अंडाशय में अंडजनन (Oogenesis) जो अगुणित अंड बनाता है", "type": "leaf"},
                {"label": "हार्मोनल लूप: हाइपोथैलेमस से GnRH रिलीज होने से पीयूष ग्रंथि से FSH (रोम विकास) और LH (अंडोत्सर्ग) रिलीज होता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["respiratory-system-external-and-internal-respiration"],
        "en": [
            {"label": "Respiratory Physics", "type": "branch", "date": "Respiration", "children": [
                {"label": "External Respiration: Gas exchange across alveolar-capillary membranes in lungs; oxygen diffuses into blood, carbon dioxide diffuses out", "type": "leaf"},
                {"label": "Internal Respiration: Gas exchange at tissue level; oxygen diffuses from capillary blood into systemic cells", "type": "leaf"},
                {"label": "Oxygen Transport: Driven primarily by reversible binding to Hemoglobin molecules in red blood cells", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "श्वसन भौतिकी", "type": "branch", "date": "श्वसन", "children": [
                {"label": "बाह्य श्वसन: फेफड़ों में वायुकोशीय-केशिका (Alveolar-Capillary) झिल्ली में गैस विनिमय; ऑक्सीजन रक्त में मिलती है, CO2 बाहर निकलती है", "type": "leaf"},
                {"label": "आंतरिक श्वसन: ऊतक स्तर पर गैस विनिमय; ऑक्सीजन केशिका रक्त से निकलकर ऊतक कोशिकाओं में विसरित होती है", "type": "leaf"},
                {"label": "ऑक्सीजन परिवहन: मुख्य रूप से लाल रक्त कोशिकाओं में हीमोग्लोबिन अणुओं के साथ प्रतिवर्ती (Reversible) बंधन द्वारा संचालित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["respiratory-system-in-humans-and-animals"],
        "en": [
            {"label": "Respiratory Structures", "type": "branch", "date": "Respiratory Tract", "children": [
                {"label": "Human Tract: Nasal cavity, Pharynx, Larynx, Trachea, Bronchi, and Alveoli (air sacs surrounded by capillaries)", "type": "leaf"},
                {"label": "Animal Organs: Gills in fish (countercurrent exchange), tracheal tubes in insects, and moist skin in amphibians", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "श्वसन संरचनाएं", "type": "branch", "date": "श्वसन पथ", "children": [
                {"label": "मानव श्वसन पथ: नासिका गुहा, ग्रसनी (Pharynx), स्वरयंत्र (Larynx), श्वासनली (Trachea), ब्रोन्ची और वायुकोश (Alveoli)", "type": "leaf"},
                {"label": "पशु श्वसन अंग: मछलियों में गलफड़े (Countercurrent विनिमय), कीटों में श्वासनली नलिकाएं, और उभयचरों में नम त्वचा", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["skeletal-and-muscular-systems"],
        "en": [
            {"label": "Movement & Skeletal Structure", "type": "branch", "date": "Skeletal & Muscle", "children": [
                {"label": "Human Skeleton: 206 bones; divided into Axial skeleton (skull, spine, ribs) and Appendicular skeleton (limbs, girdles)", "type": "leaf"},
                {"label": "Muscle contraction: Sliding filament theory; actin and myosin filaments slide past each other driven by calcium release and ATP", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "गति और कंकाल संरचना", "type": "branch", "date": "कंकाल और मांसपेशी", "children": [
                {"label": "मानव कंकाल: 206 हड्डियां; अक्षीय कंकाल (खोपड़ी, रीढ़, पसलियां) और उपांगीय कंकाल (अंगों की हड्डियां) में विभाजित", "type": "leaf"},
                {"label": "मांसपेशियों का संकुचन: स्लाइडिंग फिलामेंट सिद्धांत; कैल्शियम रिलीज और एटीपी द्वारा संचालित एक्टिन और मायोसिन फिलामेंट्स का खिसकना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["the-digestive-system"],
        "en": [
            {"label": "Human Alimentary Canal", "type": "branch", "date": "Digestion", "children": [
                {"label": "Path: Mouth (salivary amylase digestion), Esophagus, Stomach (pepsin, HCl secretion), Small Intestine, Large Intestine", "type": "leaf"},
                {"label": "Absorption: Villi and microvilli in small intestine walls expanding surface area to absorb sugars, amino acids, and fats", "type": "leaf"},
                {"label": "Accessory Glands: Liver (produces bile emulsifying fats) and Pancreas (secretes trypsin, amylase, lipase enzymes)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मानव आहार नाल", "type": "branch", "date": "पाचन", "children": [
                {"label": "मार्ग: मुंह (लार एमाइलेज पाचन), ग्रासनली, आमाशय (पेप्सिन, HCl स्राव), छोटी आंत, बड़ी आंत", "type": "leaf"},
                {"label": "अवशोषण: शर्करा, अमीनो एसिड और वसा को अवशोषित करने के लिए सतह क्षेत्र बढ़ाने वाली छोटी आंत की दीवारों में विली (Villi)", "type": "leaf"},
                {"label": "सहायक ग्रंथियां: यकृत (पित्त का उत्पादन जो वसा को इमल्सीफाइ करता है) और अग्न्याशय (ट्रिप्सिन, एमाइलेज का स्राव)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["the-transport-system-in-organisms"],
        "en": [
            {"label": "Transport Mechanisms", "type": "branch", "date": "Circulation", "children": [
                {"label": "Plants: Xylem (vessels, tracheids transporting water upward via transpiration pull) and Phloem (sieve tubes transporting organic solutes)", "type": "leaf"},
                {"label": "Animals: Closed circulatory system in vertebrates (four-chambered heart in mammals/birds pumping double circulation loops)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिवहन तंत्र", "type": "branch", "date": "परिसंचरण", "children": [
                {"label": "पौधे: जाइलम (वाष्पोत्सर्जन खिंचाव द्वारा पानी का परिवहन करने वाली वाहिकाएं) और फ्लोएम (कार्बनिक विलेय ले जाने वाली चालनी नलिकाएं)", "type": "leaf"},
                {"label": "पशु: कशेरुकियों में बंद परिसंचरण तंत्र (स्तनधारियों/पक्षियों में चार कक्षीय हृदय जो दोहरा परिसंचरण पंप करता है)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["tissues"],
        "en": [
            {"label": "Tissue Classifications", "type": "branch", "date": "Tissues", "children": [
                {"label": "Animal Tissues: Epithelial (protection), Connective (bone, cartilage, blood), Muscular (movement), and Neural (impulse transmission)", "type": "leaf"},
                {"label": "Plant Tissues: Meristematic (active division zones) and Permanent tissues (parenchyma, collenchyma, sclerenchyma)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ऊतकों का वर्गीकरण", "type": "branch", "date": "ऊतक", "children": [
                {"label": "जंतु ऊतक: उपकला (Epithelial), संयोजी (हड्डी, उपास्थि, रक्त), पेशीय (गति), और तंत्रिका ऊतक (आवेग संचरण)", "type": "leaf"},
                {"label": "पादप ऊतक: विभज्योतक (सक्रिय विभाजन क्षेत्र) और स्थायी ऊतक (पेरेन्काइमा, कोलेनकाइमा, स्क्लेरेन्काइमा)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["various-fields-of-bt"],
        "en": [
            {"label": "Biotech Classifications", "type": "branch", "date": "Biotech Fields", "children": [
                {"label": "Red BT: Medical applications including vaccine development, gene therapies, and stem cell research", "type": "leaf"},
                {"label": "Green BT: Agricultural applications including transgenic pest-resistant crops and biofertilizers", "type": "leaf"},
                {"label": "White BT: Industrial applications including industrial enzymes, biofuels, and bioplastics", "type": "leaf"},
                {"label": "Blue BT: Marine applications utilizing aquatic organisms to synthesize drugs and industrial enzymes", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "जैव प्रौद्योगिकी का वर्गीकरण", "type": "branch", "date": "BT क्षेत्र", "children": [
                {"label": "रेड BT (लाल): टीका विकास, जीन थेरेपी और स्टेम सेल अनुसंधान सहित चिकित्सा अनुप्रयोग", "type": "leaf"},
                {"label": "ग्रीन BT (हरा): ट्रांसजेनिक कीट-प्रतिरोधी फसलों और जैव उर्वरकों सहित कृषि अनुप्रयोग", "type": "leaf"},
                {"label": "व्हाइट BT (सफेद): औद्योगिक एंजाइम, जैव ईंधन और बायोप्लास्टिक सहित औद्योगिक अनुप्रयोग", "type": "leaf"},
                {"label": "ब्लू BT (नीला): दवाओं और औद्योगिक एंजाइमों को संश्लेषित करने के लिए जलीय जीवों का उपयोग करने वाले समुद्री अनुप्रयोग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["waste-water-and-sewage-treatment"],
        "en": [
            {"label": "Sewage Treatment Process", "type": "branch", "date": "Sewage Treatment", "children": [
                {"label": "Primary Treatment: Physical separation of grit and large suspended solids via screening and sedimentation tanks", "type": "leaf"},
                {"label": "Secondary Treatment: Biological process; aerobic digestion using activated sludge, reducing Biological Oxygen Demand (BOD)", "type": "leaf"},
                {"label": "Tertiary Treatment: Chemical disinfection (chlorination or UV irradiation) to remove nitrates and phosphates before release", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "सीवेज उपचार प्रक्रिया", "type": "branch", "date": "सीवेज उपचार", "children": [
                {"label": "प्राथमिक उपचार: स्क्रीनिंग और अवसादन टैंकों के माध्यम से ग्रिट और बड़े निलंबित ठोस पदार्थों का भौतिक पृथक्करण", "type": "leaf"},
                {"label": "द्वितीयक उपचार: जैविक प्रक्रिया; सक्रिय कीचड़ (Activated Sludge) का उपयोग करके वायवीय पाचन, जैविक ऑक्सीजन मांग (BOD) को कम करना", "type": "leaf"},
                {"label": "तृतीयक उपचार: विसर्जन से पहले नाइट्रेट और फॉस्फेट को हटाने के लिए रासायनिक कीटाणुशोधन (क्लोरीनीकरण या यूवी किरणें)", "type": "leaf"}
            ]}
        ]
    }
]

TRANSLATIONS = {
    "achievements": "उपलब्धियां",
    "biotechnology": "जैव प्रौद्योगिकी",
    "different": "विभिन्न",
    "fields": "क्षेत्रों",
    "animal": "पशु",
    "insect": "कीट",
    "biological": "जैविक",
    "fuel": "ईंधन",
    "generation": "उत्पादन",
    "medicine": "चिकित्सा",
    "india": "भारत",
    "classification": "वर्गीकरण",
    "domains": "डोमेन",
    "life": "जीवन",
    "communicable": "संचारी",
    "diseases": "रोग (बीमारियां)",
    "department": "विभाग",
    "designer": "डिजाइनर",
    "babies": "शिशु (बेबी)",
    "three": "तीन",
    "parents": "अभिभावक",
    "sequencing": "अनुक्रमण",
    "genetic": "आनुवंशिक",
    "material": "सामग्री",
    "economic": "आर्थिक",
    "zoology": "प्राणिविज्ञान",
    "beneficial": "लाभकारी",
    "animals": "जीव (पशु)",
    "harmful": "हानिकारक",
    "endocrine": "अंतःस्रावी",
    "system": "तंत्र (प्रणाली)",
    "adrenal": "अधिवृक्क",
    "glands": "ग्रंथियां",
    "hypothalamus": "हाइपोथैलेमस",
    "pineal": "पीनियल",
    "body": "पिंड",
    "epiphysis": "एपिफिसिस",
    "pituitary": "पीयूष (पिट्यूटरी)",
    "gland": "ग्रंथि",
    "hypophysis": "हाइपोफिसिस",
    "reproductive": "प्रजनन",
    "thyroid": "थायराइड",
    "excretory": "उत्सर्जन",
    "food": "खाद्य",
    "beverage": "पेय",
    "gene": "जीन",
    "expression": "अभिव्यक्ति",
    "regulation": "नियमन",
    "general": "सामान्य",
    "biology": "जीव विज्ञान",
    "living": "जीवित",
    "things": "चीजें",
    "viruses": "विषाणु (वायरस)",
    "engineering": "इंजीनियरिंग",
    "genetics": "आनुवंशिकी",
    "global": "वैश्विक",
    "warming": "तपन (वार्मिंग)",
    "significance": "महत्व",
    "fossils": "जीवाश्म",
    "evolution": "विकास",
    "industrial": "औद्योगिक",
    "inheritance": "वंशानुक्रम (विरासत)",
    "intellectual": "बौद्धिक",
    "property": "संपदा",
    "rights": "अधिकार (IPR)",
    "meaning": "अर्थ",
    "types": "प्रकार",
    "agriculture": "कृषि",
    "landfilling": "लैंडफिलिंग",
    "technologies": "तकनीकें",
    "microbes": "रोगाणु (माइक्रोब्स)",
    "geological": "भूवैज्ञानिक",
    "environment": "पर्यावरण",
    "microbial": "सूक्ष्मजीव",
    "ecology": "पारिस्थितिकी",
    "environmental": "पर्यावरणीय",
    "mutation": "उत्परिवर्तन",
    "non-communicable": "गैर-संचारी",
    "nutrition": "पोषण",
    "source": "स्रोत",
    "carbon": "कार्बन",
    "origin": "उत्पत्ति",
    "cells": "कोशिकाएं",
    "patent": "पेटेंट",
    "protection": "संरक्षण",
    "trade": "व्यापार",
    "secrets": "रहस्य (सीक्रेट)",
    "pharmaceuticals": "दवाएं (फार्मास्यूटिकल्स)",
    "biopharmaceuticals": "बायोफार्मास्यूटिकल्स",
    "photosynthesis": "प्रकाश संश्लेषण",
    "plant": "पादप (पौधे)",
    "forest": "वन",
    "breeders": "प्रजनक",
    "inventions": "आविष्कार",
    "recombinant": "पुनः संयोजक",
    "respiratory": "श्वसन",
    "external": "बाहरी",
    "internal": "आंतरिक",
    "respiration": "श्वसन क्रिया",
    "humans": "मनुष्य",
    "skeletal": "कंकाल",
    "muscular": "पेशीय",
    "systems": "प्रणालियाँ",
    "digestive": "पाचन",
    "transport": "परिवहन",
    "organisms": "जीवों",
    "tissues": "ऊतक (Tissues)",
    "various": "विभिन्न",
    "waste": "अपशिष्ट",
    "water": "जल",
    "sewage": "सीवेज",
    "treatment": "उपचार"
}

def get_hindi_title(clean_title):
    words = clean_title.split()
    translated_words = []
    for w in words:
        w_clean = w.strip("()-,.vs")
        w_lower = w_clean.lower()
        matched = False
        for k, v in TRANSLATIONS.items():
            if k == w_lower:
                translated_words.append(v)
                matched = True
                break
        if not matched:
            translated_words.append(w)
    return ' '.join(translated_words)

def get_dynamic_branches_en(clean_title):
    t = clean_title
    return [
        {
            "label": f"Core Concept of {t}",
            "type": "branch",
            "date": "Overview",
            "children": [
                {"label": f"Definition: Understanding the fundamental characteristics, definitions, and scope of {t}", "type": "leaf"},
                {"label": f"Scientific Framework: Analyzing how {t} integrates with physiological, molecular, and biological systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the development, pathways, and replication of {t}", "type": "leaf"},
                {"label": f"Applied Engineering: Exploring the biochemical pathways, laboratory models, and functions of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Socio-Economic & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How advances in {t} affect human health, biodiversity preservation, and agricultural yields", "type": "leaf"},
                {"label": f"Case Studies: Notable biotechnology products, clinical therapies, and research designs relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key technical terminologies, regulatory bodies, and safety guidelines associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with bio-ethics, healthcare systems, intellectual property rights, and food security", "type": "leaf"}
            ]
        }
    ]

def get_dynamic_branches_hi(clean_title_hi):
    t = clean_title_hi
    return [
        {
            "label": f"{t} की मूल अवधारणा",
            "type": "branch",
            "date": "अवधारणा",
            "children": [
                {"label": f"परिभाषा: {t} की बुनियादी विशेषताओं, परिभाषाओं और कार्यक्षेत्र को समझना", "type": "leaf"},
                {"label": f"वैज्ञानिक ढांचा: {t} शारीरिक, आणविक और जैविक प्रणालियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं और गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के विकास, जैव रासायनिक मार्गों और प्रतिकृति को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"अनुप्रयुक्त इंजीनियरिंग: {t} के प्रयोगशाला मॉडलों, जैव रासायनिक मार्गों और कार्यों का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"सामाजिक-आर्थिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में प्रगति मानव स्वास्थ्य, जैव विविधता संरक्षण और कृषि पैदावार को कैसे प्रभावित करती है", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और राष्ट्रीय जैव प्रौद्योगिकी उत्पाद", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े तकनीकी नियमों, राष्ट्रीय नियामक निकायों और सुरक्षा नियमों का अध्ययन", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को जैव-नैतिकता, बौद्धिक संपदा अधिकारों (IPR) और खाद्य सुरक्षा से जोड़ना", "type": "leaf"}
            ]
        }
    ]

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()
    
    # Check group mappings first to return extremely rich detailed data
    for g in GROUPS:
        for k in g["keys"]:
            if k in fl:
                return g["hi"] if is_hindi else g["en"]
            
    # Fallback to dynamic, non-overlapping generated branches using folder name
    clean_title = get_clean_title(folder_name)
    if is_hindi:
        hindi_title = get_hindi_title(clean_title)
        return get_dynamic_branches_hi(hindi_title)
    else:
        return get_dynamic_branches_en(clean_title)

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('\r\n', '\n')
    
    # Clean previous mindmap elements to prevent duplicate inserts
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=3">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css">\n']:
        html = html.replace(old, '')
    
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    folder_path = os.path.dirname(html_path)
    folder_name = os.path.basename(folder_path)
    if folder_name == 'hi':
        folder_name = os.path.basename(os.path.dirname(folder_path))

    clean_title = get_clean_title(folder_name)
    topic_name = clean_title
    cj = os.path.join(os.path.dirname(html_path), "content.json")
    if os.path.exists(cj):
        try:
            topic_name = json.load(open(cj, encoding='utf-8')).get('hero', {}).get('title', topic_name)
        except Exception:
            pass

    branches = get_custom_branches(folder_name, is_hindi)
    
    # Restructure branches dynamically to add more branches before leaves
    def restructure_node(node):
        res = {}
        for k, v in node.items():
            if k == "children":
                res["children"] = [restructure_node(c) for c in v]
            else:
                res[k] = v
        
        if res.get("type") == "leaf":
            label = res.get("label", "")
            if ":" in label:
                parts = label.split(":", 1)
                header = parts[0].strip()
                desc = parts[1].strip()
                if len(header) < 40 and not header.startswith("http") and not re.match(r'^\d+$', header):
                    sub_labels = [s.strip() for s in desc.split(";") if s.strip()]
                    sub_children = []
                    for sub in sub_labels:
                        if sub:
                            sub_cap = sub[0].upper() + sub[1:] if len(sub) > 1 else sub.upper()
                            sub_children.append({"label": sub_cap, "type": "leaf"})
                    return {
                        "label": header,
                        "type": "branch",
                        "children": sub_children
                    }
        return res

    branches = [restructure_node(b) for b in branches]
    
    # Capitalize lines appropriately in the label
    root_label = clean_title.replace(" Of ", " of ").replace(" And ", " and ").replace(" The ", " the ").replace(" In ", " in ").replace(" With ", " with ").replace(" To ", " to ").replace(" On ", " on ").replace(" By ", " by ")
    
    # Format multiline label for readability in the mindmap node
    words = root_label.split()
    formatted_label = ""
    for idx, word in enumerate(words):
        formatted_label += word
        if (idx + 1) % 3 == 0 and (idx + 1) < len(words):
            formatted_label += "\n"
        else:
            formatted_label += " "
    formatted_label = formatted_label.strip()

    mindmap_data = {"label": formatted_label, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand — opening one automatically closes its siblings.'
        title_text = f"{topic_name} &mdash; Interactive Mindmap"

    mindmap_card = f'''            <!-- Interactive Mindmap -->
            <div class="card-premium" id="mindmap-card">
                <h2 class="card-title"><i class="fas fa-diagram-project"></i> {title_text}</h2>
                <p style="color:var(--text-light);font-size:.87rem;margin-bottom:1.25rem;">
                    <i class="fas fa-circle-info" style="color:#8b5cf6;margin-right:5px;"></i>
                    {instr}
                </p>
                <div id="prehistory-mindmap-container"></div>
            </div>
'''
    deep_dive_pattern = r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)'
    if re.search(deep_dive_pattern, html):
        html = re.sub(deep_dive_pattern, mindmap_card + r'\1', html)
    else:
        tab1_marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if tab1_marker in html:
            html = html.replace(tab1_marker, tab1_marker + '\n' + mindmap_card, 1)

    tree_json = json.dumps(mindmap_data)
    lang_str = "'hi'" if is_hindi else "'en'"
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, {lang_str});
    </script>
'''
    html = html.replace('</body>', inline_script + '\n</body>')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Patched: {html_path}")
    return True

def create_hi_stub(en_html_path, hi_html_path, folder_name, hindi_title):
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    # Update navigation and language toggle to point to English version
    html = html.replace('<a href="hi/">Hindi Version</a>', '<a href="../">English Version</a>', 1)
    html = html.replace('<a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>', 
                        '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>', 1)

    # Update canonical
    html = re.sub(
        r'<link rel="canonical" href="([^"]+)"',
        lambda m: f'<link rel="canonical" href="{m.group(1).rstrip("/")}/hi/"',
        html, count=1
    )
    html = re.sub(r'<title>[^<]+</title>',
                  f'<title>{hindi_title} - UPSC सिविल सेवा अध्ययन गाइड | SJMaths</title>',
                  html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"',
                  f'<meta name="description" content="{hindi_title} पर विस्तृत UPSC अध्ययन गाइड। माइंडमैप, नोट्स, मनेमोनिक्स और प्रश्नोत्तर।"',
                  html, count=1)
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total = 0
    # First pass: find all English index.html files and generate Hindi stubs if missing
    for root, dirs, files in os.walk(BASE_DIR):
        parts = os.path.relpath(root, BASE_DIR).split(os.sep)
        is_hindi = 'hi' in parts
        if not is_hindi and 'index.html' in files:
            en_html_path = os.path.join(root, 'index.html')
            hi_dir = os.path.join(root, 'hi')
            hi_html_path = os.path.join(hi_dir, 'index.html')
            if not os.path.exists(hi_html_path):
                folder_name = os.path.basename(root)
                clean_title = get_clean_title(folder_name)
                hindi_title = get_hindi_title(clean_title)
                try:
                    create_hi_stub(en_html_path, hi_html_path, folder_name, hindi_title)
                    print(f"Created Hindi stub: {hi_html_path}")
                except Exception as e:
                    print(f"Error creating Hindi stub for {folder_name}: {e}")

    # Second pass: process and patch all index.html files
    for root, dirs, files in os.walk(BASE_DIR):
        parts = os.path.relpath(root, BASE_DIR).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                try:
                    process_file(os.path.join(root, file), is_hindi)
                    total += 1
                except Exception as e:
                    print(f"Error processing {os.path.join(root, file)}: {e}")
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
