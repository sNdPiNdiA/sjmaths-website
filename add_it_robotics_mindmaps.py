#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE_DIR = r"upsc/science_and_tech/IT-Communication-AI-Robotics"

def get_clean_title(folder_name):
    title = re.sub(r'([a-z])([A-Z])', r'\1 \2', folder_name)
    title = title.replace('-', ' ')
    words = []
    acronyms = {'ict', 'ai', 'iot', 'wifi', 'laser', 'lasers', 'negp', 'trai', 'cert', 'cert-in', 'gdpr', 'dpdp', 'upsc', 'gsm', 'cdma', 'lte', 'volte', 'mri', 'nfc', 'nqm', 'lidar'}
    for w in title.split():
        if w.lower() in acronyms:
            words.append(w.upper())
        elif w.lower() in ['of', 'and', 'the', 'for', 'in', 'with', 'against', 'to', 'on', 'some', 'by', 'their', 'vs']:
            words.append(w.lower())
        else:
            words.append(w.capitalize())
    return ' '.join(words)

# Grouped dataset containing fact-rich mindmaps with colons to support sub-branch restructuring
# Every single one of the 29 subdirectories has its own completely unique dataset.
GROUPS = [
    {
        "keys": ["advantages-and-disadvantages-of-artificial-intelligence"],
        "en": [
            {"label": "Pros of Artificial Intelligence", "type": "branch", "date": "AI Pros", "children": [
                {"label": "Automation: Execution of dangerous or repetitive tasks without human fatigue", "type": "leaf"},
                {"label": "Precision: High accuracy in medical diagnostics, weather predictions, and complex data analysis", "type": "leaf"}
            ]},
            {"label": "Cons of Artificial Intelligence", "type": "branch", "date": "AI Cons", "children": [
                {"label": "Costly Setup: Huge computing requirements, massive electrical power consumption, and hardware costs", "type": "leaf"},
                {"label": "Ethical concerns: Algorithmic bias in hiring models, deepfakes spreading disinformation, and lack of human moral judgment", "type": "leaf"},
                {"label": "Job Displacement: Automation of entry-level cognitive jobs like coding, writing, and customer service", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कृत्रिम बुद्धिमत्ता (AI) के लाभ", "type": "branch", "date": "AI लाभ", "children": [
                {"label": "स्वचालन: बिना किसी मानवीय थकान के खतरनाक या दोहराव वाले कार्यों का तेजी से निष्पादन", "type": "leaf"},
                {"label": "सटीकता: चिकित्सा निदान, मौसम पूर्वानुमान और जटिल डेटा विश्लेषण में उच्च सटीकता", "type": "leaf"}
            ]},
            {"label": "कृत्रिम बुद्धिमत्ता (AI) की हानियाँ", "type": "branch", "date": "AI हानियाँ", "children": [
                {"label": "महंगा सेटअप: विशाल कंप्यूटिंग आवश्यकताएं, अत्यधिक बिजली की खपत और हार्डवेयर लागत", "type": "leaf"},
                {"label": "नैतिक चिंताएं: एल्गोरिथम में पूर्वाग्रह, दुष्प्रचार फैलाने वाले डीपफेक और मानवीय नैतिक विवेक की कमी", "type": "leaf"},
                {"label": "नौकरियों का विस्थापन: कोडिंग, लेखन और ग्राहक सेवा जैसी शुरुआती बौद्धिक नौकरियों का स्वचालन", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["artificial-intelligence-and-application"],
        "en": [
            {"label": "Core AI Subfields", "type": "branch", "date": "Subfields", "children": [
                {"label": "Machine Learning: Training statistical models on data to perform tasks without explicit programming rules", "type": "leaf"},
                {"label": "Deep Learning: Utilizes multi-layered artificial neural networks inspired by the human brain to process raw inputs", "type": "leaf"}
            ]},
            {"label": "Key AI Applications", "type": "branch", "date": "Applications", "children": [
                {"label": "Healthcare: Pattern recognition in MRI scans to diagnose tumors, and accelerating chemical drug discovery", "type": "leaf"},
                {"label": "Autonomous vehicles: Real-time sensor processing and navigation pathing in self-driving cars", "type": "leaf"},
                {"label": "Finance: High-frequency trading algorithms, fraud detection models, and customer credit scoring", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मुख्य AI उप-क्षेत्र", "type": "branch", "date": "उप-क्षेत्र", "children": [
                {"label": "मशीन लर्निंग: स्पष्ट प्रोग्रामिंग नियमों के बिना कार्य करने के लिए सांख्यिकीय मॉडलों को प्रशिक्षित करना", "type": "leaf"},
                {"label": "डीप लर्निंग: कच्चे इनपुट को संसाधित करने के लिए मानव मस्तिष्क से प्रेरित बहु-स्तरीय कृत्रिम तंत्रिका नेटवर्क का उपयोग", "type": "leaf"}
            ]},
            {"label": "प्रमुख AI अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "स्वास्थ्य सेवा: ट्यूमर का निदान करने के लिए MRI स्कैन में पैटर्न की पहचान, और दवा खोज को तेज करना", "type": "leaf"},
                {"label": "स्वायत्त वाहन: स्व-चालित कारों में वास्तविक समय सेंसर प्रसंस्करण और नेविगेशन मार्ग निर्धारण", "type": "leaf"},
                {"label": "वित्त क्षेत्र: उच्च आवृत्ति ट्रेडिंग एल्गोरिदम, धोखाधड़ी का पता लगाने वाले मॉडल और क्रेडिट स्कोरिंग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["application-of-superconductors"],
        "en": [
            {"label": "Superconductor Applications", "type": "branch", "date": "Applications", "children": [
                {"label": "MRI Scanners: Superconducting coils generate stable, powerful magnetic fields essential for high-resolution body imaging", "type": "leaf"},
                {"label": "Maglev Trains: Frictionless transit utilizing superconducting magnets for magnetic levitation and propulsion", "type": "leaf"},
                {"label": "Power Transmission: Lossless electrical cables transmitting high currents without heating or resistance losses", "type": "leaf"},
                {"label": "Particle Accelerators: Bends high-energy particle beams in machines like CERN's Large Hadron Collider", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अतिचालक (Superconductor) अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "MRI स्कैनर: अतिचालक कॉइल शरीर की उच्च-रिज़ॉल्यूशन इमेजिंग के लिए आवश्यक शक्तिशाली चुंबकीय क्षेत्र उत्पन्न करते हैं", "type": "leaf"},
                {"label": "मैग्लेव ट्रेनें: चुंबकीय उत्तोलन और प्रणोदन के लिए अतिचालक चुंबक का उपयोग करने वाला घर्षण रहित पारगमन", "type": "leaf"},
                {"label": "विद्युत संचरण: बिना गर्म हुए या प्रतिरोध नुकसान के उच्च धाराओं को प्रसारित करने वाले हानि रहित विद्युत केबल", "type": "leaf"},
                {"label": "कण त्वरक (CERN): सर्न के लार्ज हैड्रॉन कोलाइडर जैसी मशीनों में उच्च-ऊर्जा कण बीम को मोड़ना", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["applications-of-nanotechnology"],
        "en": [
            {"label": "Applied Nanotechnology", "type": "branch", "date": "Uses", "children": [
                {"label": "Targeted Medicine: Nanoparticle drug carriers that navigate body fluids to release medications directly at tumor sites", "type": "leaf"},
                {"label": "Electronics: Transistor channel lengths scaled below 5nm using nanomaterials, boosting processor speeds", "type": "leaf"},
                {"label": "Water Purification: Nanofiber membranes filtering out heavy metal ions, chemical toxins, and viral microbes", "type": "leaf"},
                {"label": "Agriculture: Nano-fertilizers and nano-pesticides releasing active ingredients slowly, minimizing chemical runoff", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "अनुप्रयुक्त नैनो तकनीक", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "लक्षित चिकित्सा: नैनोकण दवा वाहक जो सीधे ट्यूमर साइटों पर दवाओं को छोड़ने के लिए शरीर के तरल पदार्थों में चलते हैं", "type": "leaf"},
                {"label": "इलेक्ट्रॉनिक्स: नैनो-सामग्रियों का उपयोग करके ट्रांजिस्टर चैनलों को 5nm से नीचे सिकोड़ना, प्रोसेसर की गति बढ़ाना", "type": "leaf"},
                {"label": "जल शोधन: नैनोफाइबर झिल्ली (Membrane) जो भारी धातु आयनों, रासायनिक विषाक्त पदार्थों और वायरस को छानती है", "type": "leaf"},
                {"label": "कृषि: नैनो-उर्वरक और नैनो-कीटनाशक जो सक्रिय अवयवों को धीरे-धीरे छोड़ते हैं, रासायनिक अपवाह को कम करते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["applications-of-robotics"],
        "en": [
            {"label": "Robotics in Industries", "type": "branch", "date": "Applications", "children": [
                {"label": "Manufacturing: Automotive assembly lines using high-speed robotic arms for welding, spray painting, and sorting", "type": "leaf"},
                {"label": "Surgical Robotics: Precision operations like the Da Vinci surgical system, reducing invasive incisions and recovery times", "type": "leaf"},
                {"label": "Defense & Exploration: Unmanned aerial vehicles (drones) for surveillance, and rovers exploring celestial bodies like Mars", "type": "leaf"},
                {"label": "Hazardous Operations: Bomb disposal units and disaster recovery robots operating in toxic, radioactive environments", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "उद्योगों में रोबोटिक्स", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "विनिर्माण (Manufacturing): ऑटोमोटिव असेंबली लाइनें जो वेल्डिंग, पेंटिंग और छंटनी के लिए रोबोटिक आर्म्स का उपयोग करती हैं", "type": "leaf"},
                {"label": "सर्जिकल रोबोटिक्स: दा विंची सर्जिकल सिस्टम जैसे सटीक संचालन उपकरण, जो घाव और ठीक होने के समय को कम करते हैं", "type": "leaf"},
                {"label": "रक्षा और अन्वेषण: निगरानी के लिए मानव रहित हवाई वाहन (ड्रोन), और मंगल जैसे खगोलीय पिंडों की खोज करने वाले रोवर", "type": "leaf"},
                {"label": "खतरनाक संचालन: रेडियोधर्मी या विषैले वातावरण में काम करने वाले बम निरोधक दस्ते और आपदा प्रबंधन रोबोट", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["basics-of-nanoscience"],
        "en": [
            {"label": "Nanoscale Fundamentals", "type": "branch", "date": "Scale", "children": [
                {"label": "Size Spectrum: Explores matter in the size range of 1 to 100 nanometers; one nanometer is one-billionth of a meter", "type": "leaf"},
                {"label": "Surface Area Effect: Wavelengths scale down, dramatically increasing surface area-to-volume ratio, making materials highly reactive", "type": "leaf"},
                {"label": "Quantum Confinement: Quantum mechanics dominate properties; alters color, conductivity, and strength of particles", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नैनोस्केल के सिद्धांत", "type": "branch", "date": "पैमाना", "children": [
                {"label": "आकार स्पेक्ट्रम: 1 से 100 नैनोमीटर के आकार सीमा में पदार्थ का अध्ययन; एक नैनोमीटर एक मीटर का एक अरबवां हिस्सा है", "type": "leaf"},
                {"label": "सतह क्षेत्र प्रभाव: सतह से आयतन अनुपात (Surface-to-Volume Ratio) नाटकीय रूप से बढ़ता है, जिससे सामग्री अत्यधिक प्रतिक्रियाशील बनती है", "type": "leaf"},
                {"label": "क्वांटम कंफाइनमेंट (Quantum Confinement): क्वांटम यांत्रिकी गुणों पर हावी होती है; कणों के रंग, चालकता और ताकत को बदलती है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["big-data-initiative-and-privacy"],
        "en": [
            {"label": "Big Data Attributes", "type": "branch", "date": "5 Vs", "children": [
                {"label": "Data Dimensions: Characterized by Volume (huge scale), Velocity (real-time stream analysis), Variety (structured, unstructured formats), Veracity, Value", "type": "leaf"},
                {"label": "Processing tools: Distributed clusters using Apache Hadoop, Spark engines, and NoSQL non-relational databases", "type": "leaf"}
            ]},
            {"label": "Privacy Safeguards", "type": "branch", "date": "Privacy", "children": [
                {"label": "Legal Shield: India's Digital Personal Data Protection (DPDP) Act 2023 regulates data collection, consent mechanisms, and user rights", "type": "leaf"},
                {"label": "GDPR standards: European Union's GDPR sets strict global benchmarks for data minimization, right to be forgotten, and breach penalties", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "बिग डेटा के गुण", "type": "branch", "date": "5 Vs", "children": [
                {"label": "डेटा आयाम: वॉल्यूम (विशाल पैमाना), वेलोसिटी (वास्तविक समय प्रवाह विश्लेषण), वैरायटी (संरचित, असंरचित प्रारूप), वेरासिटी, वैल्यू", "type": "leaf"},
                {"label": "प्रसंस्करण उपकरण: अपाचे हडूप, स्पार्क इंजन और NoSQL गैर-relational डेटाबेस का उपयोग करने वाले वितरित क्लस्टर", "type": "leaf"}
            ]},
            {"label": "गोपनीयता सुरक्षा उपाय", "type": "branch", "date": "गोपनीयता", "children": [
                {"label": "कानूनी सुरक्षा: भारत का डिजिटल व्यक्तिगत डेटा संरक्षण (DPDP) अधिनियम 2023 डेटा संग्रह, सहमति तंत्र को नियंत्रित करता है", "type": "leaf"},
                {"label": "GDPR मानक: यूरोपीय संघ का GDPR डेटा न्यूनता, भूल जाने के अधिकार (Right to be Forgotten) के वैश्विक मानक तय करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["classification-of-robots"],
        "en": [
            {"label": "Robot Typology", "type": "branch", "date": "Classes", "children": [
                {"label": "Industrial: Fixed articulated manipulator arms with multiple degrees of freedom (DoF) for manufacturing", "type": "leaf"},
                {"label": "Service Robots: Semi or fully autonomous systems performing tasks outside factories (medical cleaning, retail guides)", "type": "leaf"},
                {"label": "Autonomous Mobile: Navigation robots utilizing LIDAR and cameras to move through spaces (warehouse AGVs)", "type": "leaf"},
                {"label": "Humanoids: Bipedal robots mimicking human structure and locomotion (e.g. Honda's ASIMO, Boston Dynamics' Atlas)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "रोबोट के प्रकार", "type": "branch", "date": "श्रेणियां", "children": [
                {"label": "औद्योगिक (Industrial): विनिर्माण के लिए कई डिग्री ऑफ फ्रीडम (DoF) वाले स्थिर या जोड़दार मैनिपुलेटर आर्म्स", "type": "leaf"},
                {"label": "सेवा रोबोट (Service): कारखानों से बाहर काम करने वाले अर्ध या पूर्णतः स्वायत्त सिस्टम (जैसे चिकित्सा सफाई, गाइड)", "type": "leaf"},
                {"label": "स्वायत्त मोबाइल (AMRs): गोदामों में सामान ले जाने के लिए लिडार (LIDAR) और कैमरों का उपयोग करने वाले नेविगेशन रोबोट", "type": "leaf"},
                {"label": "ह्यूमनॉइड्स (Humanoids): मानव जैसी शारीरिक संरचना और चाल की नकल करने वाले रोबोट (जैसे बोस्टन डायनेमिक्स का एटलस)", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["computer-terminology-and-fundamental"],
        "en": [
            {"label": "Hardware Fundamentals", "type": "branch", "date": "Hardware", "children": [
                {"label": "CPU Architecture: Central Processing Unit combining Arithmetic Logic Unit (ALU) for calculations and Control Unit (CU) for routing", "type": "leaf"},
                {"label": "Memory Tiering: Fast volatile cache memory, main system RAM, and permanent firmware stored in non-volatile ROM", "type": "leaf"}
            ]},
            {"label": "Logic & Math", "type": "branch", "date": "Logic", "children": [
                {"label": "Binary System: Representation of data using 0 and 1, processed via physical logic gates (AND, OR, NOT, NAND)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "हार्डवेयर की मूल बातें", "type": "branch", "date": "हार्डवेयर", "children": [
                {"label": "CPU आर्किटेक्चर: सेंट्रल प्रोसेसिंग यूनिट जो गणना के लिए ALU और निर्देशों के मार्ग निर्धारण के लिए CU को जोड़ती है", "type": "leaf"},
                {"label": "मेमोरी पदानुक्रम: तीव्र अस्थायी कैश मेमोरी, मुख्य सिस्टम रैम (RAM), और गैर-अस्थिर रोम (ROM) में संग्रहीत फर्मवेयर", "type": "leaf"}
            ]},
            {"label": "तर्क और गणित", "type": "branch", "date": "तर्क", "children": [
                {"label": "बाइनरी सिस्टम: 0 और 1 का उपयोग करके डेटा का प्रतिनिधित्व, जिसे भौतिक लॉजिक गेट्स (AND, OR, NOT) द्वारा संसाधित किया जाता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["cyber-crime-and-security"],
        "en": [
            {"label": "Cyber Attacks Overview", "type": "branch", "date": "Threats", "children": [
                {"label": "Malware: Viruses, Trojan horses (masquerades as benign files), spyware, and file-encrypting ransomware (e.g. WannaCry)", "type": "leaf"},
                {"label": "Social Engineering: Phishing emails and spoofed sites designed to trick users into revealing login credentials", "type": "leaf"},
                {"label": "Network Attacks: DDoS (Distributed Denial of Service) flooding servers with synthetic request traffic to crash services", "type": "leaf"}
            ]},
            {"label": "Defensive Systems", "type": "branch", "date": "Defense", "children": [
                {"label": "Security Tools: Firewalls for packet filtering, end-to-end encryption, and Multi-Factor Authentication (MFA)", "type": "leaf"},
                {"label": "CERT-In: National nodal agency coordinating responses to cyber security emergencies and issuing threat alerts", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "साइबर हमलों का अवलोकन", "type": "branch", "date": "खतरे", "children": [
                {"label": "मैलवेयर: वायरस, ट्रोजन हॉर्स (दिखावटी फाइलें), स्पाइवेयर और फाइलों को लॉक करने वाले रैंसमवेयर (जैसे WannaCry)", "type": "leaf"},
                {"label": "सोशल इंजीनियरिंग: संवेदनशील जानकारी चुराने के लिए उपयोगकर्ताओं को धोखा देने वाले फ़िशिंग ईमेल और फर्जी वेबसाइटें", "type": "leaf"},
                {"label": "नेटवर्क हमले: DDoS (डिस्ट्रीब्यूटेड डिनायल ऑफ सर्विस) जो सर्वर पर फर्जी ट्रैफिक भेजकर सेवाओं को ठप कर देता है", "type": "leaf"}
            ]},
            {"label": "सुरक्षात्मक प्रणालियाँ", "type": "branch", "date": "सुरक्षा", "children": [
                {"label": "सुरक्षा उपकरण: पैकेट फ़िल्टरिंग के लिए फ़ायरवॉल, एंड-टू-एंड एन्क्रिप्शन और मल्टी-फैक्टर ऑथेंटिकेशन (MFA)", "type": "leaf"},
                {"label": "CERT-In: साइबर सुरक्षा आपात स्थितियों पर प्रतिक्रिया का समन्वय करने वाली और थ्रेट अलर्ट जारी करने वाली राष्ट्रीय नोडल एजेंसी", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["cyber-law"],
        "en": [
            {"label": "Cyber Regulations", "type": "branch", "date": "Legal Framework", "children": [
                {"label": "IT Act 2000: Information Technology Act; primary legal framework governing e-commerce, digital signatures, and cyber crimes in India", "type": "leaf"},
                {"label": "Section 66A: Controversial section penalizing sending offensive messages; struck down by Supreme Court in Shreya Singhal case (2015) for violating free speech", "type": "leaf"},
                {"label": "Appellate Tribunal: Special judicial bodies set up to adjudicate dispute cases arising from decisions of adjudicating officers under the IT Act", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "साइबर नियमन", "type": "branch", "date": "कानूनी ढांचा", "children": [
                {"label": "IT अधिनियम 2000: सूचना प्रौद्योगिकी अधिनियम; भारत में ई-कॉमर्स, डिजिटल हस्ताक्षर और साइबर अपराधों को नियंत्रित करने वाला कानून", "type": "leaf"},
                {"label": "धारा 66A: आपत्तिजनक संदेश भेजने पर दंडित करने वाली विवादित धारा; सुप्रीम कोर्ट द्वारा श्रेया सिंघल मामले (2015) में निरस्त", "type": "leaf"},
                {"label": "अपीलीय न्यायाधिकरण: IT अधिनियम के तहत न्यायनिर्णयन अधिकारियों के निर्णयों के खिलाफ विवादों की सुनवाई करने वाले विशेष न्यायिक निकाय", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["definition-and-impact-of-ict-on-society"],
        "en": [
            {"label": "ICT Definition", "type": "branch", "date": "What is ICT", "children": [
                {"label": "Scope: Information and Communication Technology; integration of computing hardware, telecommunications, and enterprise software to access, transmit, and manipulate data", "type": "leaf"}
            ]},
            {"label": "Societal Impact", "type": "branch", "date": "Social Impact", "children": [
                {"label": "Digital Divide: Gap between demographics having access to modern ICT infrastructure (urban areas) and those without (rural pockets)", "type": "leaf"},
                {"label": "Key Enablers: Telemedicine (remote diagnostics), e-learning platforms (democratizing education), and digital financial services", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ICT की परिभाषा", "type": "branch", "date": "ICT क्या है", "children": [
                {"label": "कार्यक्षेत्र: सूचना और संचार प्रौद्योगिकी; डेटा तक पहुँचने और प्रसारित करने के लिए कंप्यूटिंग, दूरसंचार और सॉफ्टवेयर का एकीकरण", "type": "leaf"}
            ]},
            {"label": "समाज पर प्रभाव", "type": "branch", "date": "सामाजिक प्रभाव", "children": [
                {"label": "डिजिटल विभाजन (Digital Divide): आधुनिक ICT बुनियादी ढांचे तक पहुंच वाले (शहरी) और पहुंच से वंचित (ग्रामीण) क्षेत्रों के बीच की खाई", "type": "leaf"},
                {"label": "प्रमुख सहायक: टेलीमेडिसिन (दूरस्थ चिकित्सा), ई-लर्निंग प्लेटफॉर्म (शिक्षा का लोकतंत्रीकरण) और डिजिटल वित्तीय सेवाएं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["evolution-of-telecommunication"],
        "en": [
            {"label": "Telecom Milestones", "type": "branch", "date": "History", "children": [
                {"label": "Early systems: Electric telegraph (Morse code) in the 19th century, transitioning to analog PSTN landline telephone grids", "type": "leaf"},
                {"label": "Optical Age: Deployment of fiber-optic cables utilizing total internal reflection, carrying massive digital data bandwidths globally", "type": "leaf"},
                {"label": "Wireless Shift: Terrestrial cellular networks (1G to 5G) and communication satellites enabling instant global connectivity", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "दूरसंचार के मील के पत्थर", "type": "branch", "date": "इतिहास", "children": [
                {"label": "प्रारंभिक प्रणालियां: 19वीं शताब्दी में विद्युत टेलीग्राफ (मोर्स कोड), जो बाद में एनालॉग PSTN लैंडलाइन टेलीफोन ग्रिड में बदला", "type": "leaf"},
                {"label": "ऑप्टिकल युग: वैश्विक स्तर पर भारी डिजिटल डेटा प्रसारित करने के लिए पूर्ण आंतरिक परावर्तन वाले फाइबर-ऑप्टिक केबल का बिछाना", "type": "leaf"},
                {"label": "वायरलेस संक्रमण: सेलुलर नेटवर्क (1G से 5G) और संचार उपग्रह जो तत्काल वैश्विक कनेक्टिविटी सक्षम करते हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["government-initiatives-in-ict"],
        "en": [
            {"label": "Digital India Initiative", "type": "branch", "date": "Digital India", "children": [
                {"label": "Pillars: Broad program based on 9 pillars including Broadband Highways, Universal Access to Mobile Connectivity, and Public Internet Access", "type": "leaf"},
                {"label": "e-Kranti: National e-Governance Plan 2.0 focusing on electronic delivery of services (health, education, planning, security)", "type": "leaf"}
            ]},
            {"label": "Core Platforms", "type": "branch", "date": "Platforms", "children": [
                {"label": "UMANG app: Unified portal providing access to central and state government services in multiple regional languages", "type": "leaf"},
                {"label": "DigiLocker: Cloud-based platform for issuance, storage, and verification of official documents and certificates digitally", "type": "leaf"},
                {"label": "UPI: Unified Payments Interface; real-time payment system enabling instant inter-bank peer-to-peer money transfers", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "डिजिटल इंडिया पहल", "type": "branch", "date": "डिजिटल इंडिया", "children": [
                {"label": "स्तंभ: ब्रॉडबैंड हाईवे, मोबाइल कनेक्टिविटी तक सार्वभौमिक पहुंच और सार्वजनिक इंटरनेट पहुंच सहित 9 स्तंभों पर आधारित कार्यक्रम", "type": "leaf"},
                {"label": "ई-क्रांति: सेवाओं (स्वास्थ्य, शिक्षा, सुरक्षा) के इलेक्ट्रॉनिक वितरण पर केंद्रित राष्ट्रीय ई-गवर्नेंस योजना 2.0", "type": "leaf"}
            ]},
            {"label": "प्रमुख प्लेटफॉर्म", "type": "branch", "date": "प्लेटफॉर्म", "children": [
                {"label": "उमंग (UMANG) ऐप: कई क्षेत्रीय भाषाओं में केंद्रीय और राज्य सरकार की सेवाओं तक पहुंच प्रदान करने वाला एकीकृत पोर्टल", "type": "leaf"},
                {"label": "डिजिलॉकर (DigiLocker): आधिकारिक दस्तावेजों और प्रमाणपत्रों को डिजिटल रूप से जारी करने, संग्रहीत करने का क्लाउड-आधारित प्लेटफॉर्म", "type": "leaf"},
                {"label": "UPI: यूनिफाइड पेमेंट्स इंटरफेस; तत्काल बैंक-टू-बैंक धन हस्तांतरण को सक्षम करने वाली वास्तविक समय की भुगतान प्रणाली", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["history-of-computers"],
        "en": [
            {"label": "Computing Milestones", "type": "branch", "date": "Milestones", "children": [
                {"label": "Mechanical Era: Abacus calculation systems, Pascaline calculators, and Charles Babbage's Analytical Engine (designed in 1837)", "type": "leaf"},
                {"label": "Electronic Era: Vacuum tube computers (ENIAC, 1945), transition to discrete transistors (2nd gen), and integrated circuits (3rd gen)", "type": "leaf"},
                {"label": "Microprocessor Age: Ted Hoff's invention of Intel 4004 microprocessor (1971), launching personal computers (PCs) and mobile chipsets", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कंप्यूटिंग के मील के पत्थर", "type": "branch", "date": "मील के पत्थर", "children": [
                {"label": "यांत्रिक युग: एबेकस गणना प्रणाली, पास्कलाइन कैलकुलेटर और चार्ल्स बैबेज का विश्लेषणात्मक इंजन (Analytical Engine 1837)", "type": "leaf"},
                {"label": "इलेक्ट्रॉनिक युग: वैक्यूम ट्यूब कंप्यूटर (ENIAC 1945), ट्रांजिस्टर (दूसरी पीढ़ी) और एकीकृत सर्किट (तीसरी पीढ़ी)", "type": "leaf"},
                {"label": "माइक्रोप्रोसेसर युग: इंटेल 4004 माइक्रोप्रोसेसर (1971) का आविष्कार, जिसने पर्सनल कंप्यूटर (PCs) और मोबाइल चिप्स की शुरुआत की", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["internet-of-things"],
        "en": [
            {"label": "IoT Architecture", "type": "branch", "date": "IoT Core", "children": [
                {"label": "Structure: Network of physical objects ('things') embedded with sensors, processing software, and transceivers to exchange data over the internet", "type": "leaf"},
                {"label": "Sensors & Actuators: Sensors collect physical state data (temperature, moisture, pressure) and actuators convert control signals into motion", "type": "leaf"},
                {"label": "Short-range wireless: Low-power communication protocols including Zigbee, Bluetooth Low Energy (BLE), and LoRaWAN", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "IoT आर्किटेक्चर", "type": "branch", "date": "IoT कोर", "children": [
                {"label": "संरचना: इंटरनेट पर डेटा साझा करने के लिए सेंसर, प्रसंस्करण सॉफ्टवेयर और ट्रांसीवर से युक्त भौतिक वस्तुओं ('चीजों') का नेटवर्क", "type": "leaf"},
                {"label": "सेंसर्स और एक्ट्यूएटर्स: सेंसर भौतिक डेटा (तापमान, नमी) एकत्र करते हैं और एक्ट्यूएटर नियंत्रण सिग्नल्स को यांत्रिक गति में बदलते हैं", "type": "leaf"},
                {"label": "कम दूरी के वायरलेस: जिगबी (Zigbee), ब्लूटूथ लो एनर्जी (BLE) और लोरावान (LoRaWAN) सहित कम बिजली वाले संचार प्रोटोकॉल", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["media-transmission-technology"],
        "en": [
            {"label": "Wired Media", "type": "branch", "date": "Physical", "children": [
                {"label": "Fiber Optics: Carries data as light pulses through glass cores, using total internal reflection (TIR) to prevent signal loss over long distances", "type": "leaf"},
                {"label": "Coaxial Copper: Copper core lines surrounded by insulating layers; suffers from attenuation and electromagnetic interference", "type": "leaf"}
            ]},
            {"label": "Wireless Transmission", "type": "branch", "date": "Wireless", "children": [
                {"label": "Electromagnetic Waves: Uses radio waves, microwaves, and satellite links to broadcast signal channels across large terrains", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वायर्ड ट्रांसमिशन माध्यम", "type": "branch", "date": "भौतिक", "children": [
                {"label": "फाइबर ऑप्टिक्स: कांच के तारों के माध्यम से प्रकाश तरंगों के रूप में डेटा ले जाता है, लंबी दूरी पर सिग्नल हानि रोकने के लिए TIR का उपयोग करता है", "type": "leaf"},
                {"label": "कोएक्सियल कॉपर (तांबा): इन्सुलेटिंग परतों से घिरे तांबे के तार; विद्युत चुंबकीय हस्तक्षेप (Interference) और सिग्नल क्षरण का शिकार होते हैं", "type": "leaf"}
            ]},
            {"label": "वायरलेस ट्रांसमिशन", "type": "branch", "date": "वायरलेस", "children": [
                {"label": "विद्युत चुंबकीय तरंगें: बड़े क्षेत्रों में सिग्नल चैनलों को प्रसारित करने के लिए रेडियो तरंगों, सूक्ष्म तरंगों और उपग्रह लिंक का उपयोग", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["ministry-of-communication-and-information-technology"],
        "en": [
            {"label": "Ministry Functions", "type": "branch", "date": "Governance", "children": [
                {"label": "Department of Telecom (DoT): Regulates telecom services, spectrum allocation, and coordinates national broadband networks", "type": "leaf"},
                {"label": "MeitY department: Ministry of Electronics and Information Technology; administers cyber security policies, hardware manufacturing promotions, and IT laws", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "मंत्रालय के कार्य", "type": "branch", "date": "शासन", "children": [
                {"label": "दूरसंचार विभाग (DoT): दूरसंचार सेवाओं, स्पेक्ट्रम आवंटन को विनियमित करता है और राष्ट्रीय ब्रॉडबैंड नेटवर्क का समन्वय करता है", "type": "leaf"},
                {"label": "MeitY विभाग: इलेक्ट्रॉनिक्स और सूचना प्रौद्योगिकी मंत्रालय; साइबर सुरक्षा नीतियों, हार्डवेयर निर्माण और IT कानूनों का प्रबंधन करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["mobile-generations-and-technology"],
        "en": [
            {"label": "Evolution: 1G to 5G", "type": "branch", "date": "Generations", "children": [
                {"label": "1G & 2G: 1G launched voice using analog radio waves; 2G introduced digital cellular networks (GSM/CDMA) and text messaging", "type": "leaf"},
                {"label": "3G & 4G: 3G enabled mobile internet surfing; 4G integrated high-speed packet-data mobile broadband using LTE/VoLTE (Voice over LTE)", "type": "leaf"},
                {"label": "5G standard: Utilizes millimeter wave frequency bands, offering ultra-low latency, high data density, and URLLC communications", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "विकास: 1G से 5G", "type": "branch", "date": "पीढ़ियाँ", "children": [
                {"label": "1G और 2G: 1G ने एनालॉग रेडियो तरंगों का उपयोग करके वॉयस कॉल शुरू की; 2G ने डिजिटल सेलुलर नेटवर्क (GSM/CDMA) और SMS की शुरुआत की", "type": "leaf"},
                {"label": "3G और 4G: 3G ने मोबाइल इंटरनेट सर्फिंग सक्षम की; 4G ने LTE/VoLTE का उपयोग करके उच्च गति मोबाइल ब्रॉडबैंड पेश किया", "type": "leaf"},
                {"label": "5G मानक: मिलीमीटर वेव फ़्रीक्वेंसी बैंड का उपयोग करता है, जो बेहद कम विलंबता (Latency), उच्च डेटा घनत्व और URLLC प्रदान करता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["nanomaterials"],
        "en": [
            {"label": "Nanostructure Categories", "type": "branch", "date": "Nanomaterials", "children": [
                {"label": "Graphene: Two-dimensional sheet of carbon atoms arranged in a hexagonal honeycomb lattice; extremely conductive and strong", "type": "leaf"},
                {"label": "Carbon Nanotubes (CNTs): Cylindrical fullerenes with high aspect ratios, used in aerospace composites and battery electrodes", "type": "leaf"},
                {"label": "Quantum Dots: Semiconductor nanocrystals emitting tunable wavelengths of light, used in display screens and medical diagnostic imaging", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नैनो-संरचना श्रेणियों का वर्गीकरण", "type": "branch", "date": "नैनो-सामग्री", "children": [
                {"label": "ग्राफीन (Graphene): हेक्सागोनल हनीकॉम्ब जाली में व्यवस्थित कार्बन परमाणुओं की द्विवार्षिक शीट; अत्यधिक प्रवाहकीय और मजबूत", "type": "leaf"},
                {"label": "कार्बन नैनोट्यूब (CNTs): उच्च आस्पेक्ट रेशियो वाली बेलनाकार फुलरीन संरचनाएं, एयरोस्पेस और बैटरी में उपयोग की जाती हैं", "type": "leaf"},
                {"label": "क्वांटम डॉट्स (Quantum Dots): अर्धचालक नैनोक्रिस्टल जो विशिष्ट तरंग दैर्ध्य का प्रकाश उत्सर्जित करते हैं, डिस्प्ले स्क्रीन में उपयोगी", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["national-e-governance-plan"],
        "en": [
            {"label": "NeGP Framework", "type": "branch", "date": "NeGP 2006", "children": [
                {"label": "Structure: Launched in 2006; coordinates central, state, and integrated Mission Mode Projects (MMPs) to deliver services digitally", "type": "leaf"},
                {"label": "Rural Reach: Employs Common Service Centres (CSCs) to provide internet access and e-government services to rural villages", "type": "leaf"},
                {"label": "Key Mission Mode Projects: Includes MCA21 (corporate affairs), Passport Seva, Income Tax digitization, and Digital Land Records", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "NeGP का ढांचा", "type": "branch", "date": "NeGP 2006", "children": [
                {"label": "संरचना: 2006 में शुरू; डिजिटल रूप से सेवाएं प्रदान करने के लिए केंद्रीय, राज्य और एकीकृत मिशन मोड प्रोजेक्ट्स (MMPs) का समन्वय करता है", "type": "leaf"},
                {"label": "ग्रामीण पहुंच: ग्रामीण गांवों में इंटरनेट पहुंच और ई-सरकारी सेवाएं प्रदान करने के लिए सामान्य सेवा केंद्रों (CSCs) का उपयोग", "type": "leaf"},
                {"label": "प्रमुख मिशन मोड परियोजनाएं: MCA21 (कॉर्पोरेट मामले), पासपोर्ट सेवा, आयकर डिजिटलीकरण और डिजिटल भूमि रिकॉर्ड शामिल हैं", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["net-neutrality"],
        "en": [
            {"label": "Net Neutrality Concept", "type": "branch", "date": "Net Neutrality", "children": [
                {"label": "Definition: Principle that Internet Service Providers (ISPs) must treat all internet communications equally, without discrimination", "type": "leaf"},
                {"label": "Prohibited Actions: Prevents ISPs from throttling data speeds, blocking access to legal content, or selling fast lanes to specific websites", "type": "leaf"},
                {"label": "TRAI Stance: Telecom Regulatory Authority of India banned zero-rating plans (like Free Basics) in 2016, protecting net neutrality", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "नेट न्यूट्रैलिटी की अवधारणा", "type": "branch", "date": "नेट न्यूट्रैलिटी", "children": [
                {"label": "परिभाषा: यह सिद्धांत कि इंटरनेट सेवा प्रदाताओं (ISPs) को बिना किसी भेदभाव के सभी इंटरनेट संचारों को समान मानना चाहिए", "type": "leaf"},
                {"label": "प्रतिबंधित गतिविधियां: ISPs को डेटा गति कम करने, वैध सामग्री को ब्लॉक करने या विशिष्ट वेबसाइटों को तेज़ गति बेचने से रोकना", "type": "leaf"},
                {"label": "TRAI का रुख: भारतीय दूरसंचार नियामक प्राधिकरण ने 2016 में जीरो-रेटिंग योजनाओं (जैसे फ्री बेसिक्स) पर प्रतिबंध लगा दिया था", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["networking-bluetooth-wifi-hotspot"],
        "en": [
            {"label": "Wireless Protocols", "type": "branch", "date": "Wireless Networks", "children": [
                {"label": "Wi-Fi: IEEE 802.11 standard; provides high-speed wireless local area networks (WLAN) over 2.4 GHz and 5 GHz bands", "type": "leaf"},
                {"label": "Bluetooth: IEEE 802.15.1 standard; personal area network (WPAN) utilizing frequency-hopping spread spectrum for short-range links", "type": "leaf"},
                {"label": "Hotspot: Network routing mechanism allowing devices to share cell-data plans by creating local Wi-Fi access points", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "वायरलेस प्रोटोकॉल", "type": "branch", "date": "वायरलेस नेटवर्क", "children": [
                {"label": "वाई-फाई (Wi-Fi): IEEE 802.11 मानक; 2.4 GHz और 5 GHz बैंड पर उच्च गति वायरलेस स्थानीय नेटवर्क (WLAN) प्रदान करता है", "type": "leaf"},
                {"label": "ब्लूटूथ: IEEE 802.15.1 मानक; कम दूरी के लिंक के लिए फ़्रीक्वेंसी-हॉपिंग स्प्रेड स्पेक्ट्रम का उपयोग करने वाला पर्सनल नेटवर्क (WPAN)", "type": "leaf"},
                {"label": "हॉटस्पॉट: नेटवर्क रूटिंग तंत्र जो उपकरणों को स्थानीय वाई-फाई एक्सेस पॉइंट बनाकर सेल-डेटा साझा करने की अनुमति देता है", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["origination-of-nanoscience-and-technology"],
        "en": [
            {"label": "Historical Milestones", "type": "branch", "date": "History", "children": [
                {"label": "1959 Foundation: Richard Feynman's classic speech 'There's Plenty of Room at the Bottom' suggested direct manipulation of individual atoms", "type": "leaf"},
                {"label": "1974 Coining: Norio Taniguchi coined the term 'nanotechnology' to define high-precision manufacturing processes", "type": "leaf"},
                {"label": "1981 Microscope: Gerd Binnig and Heinrich Rohrer invented the Scanning Tunneling Microscope (STM), enabling imaging of individual atomic surfaces", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "ऐतिहासिक मील के पत्थर", "type": "branch", "date": "इतिहास", "children": [
                {"label": "1959 आधारशिला: रिचर्ड फेनमैन का भाषण 'देयर इज प्लेंटी ऑफ रूम एट द बॉटम' जिसमें एकल परमाणुओं के सीधे हेरफेर का सुझाव दिया गया था", "type": "leaf"},
                {"label": "1974 नामकरण: नोरियो तानिगुची ने उच्च-सटीकता निर्माण प्रक्रियाओं को परिभाषित करने के लिए 'नैनोटेक्नोलॉजी' शब्द का प्रतिपादन किया", "type": "leaf"},
                {"label": "1981 माइक्रोस्कोप: गेर्ड बिन्निंग और हेनरिक रोहरर ने स्कैनिंग टनलिंग माइक्रोस्कोप (STM) का आविष्कार किया, जिससे परमाणुओं को देखना संभव हुआ", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["quantum-computing"],
        "en": [
            {"label": "Quantum Principles", "type": "branch", "date": "Mechanics", "children": [
                {"label": "Superposition: Ability of qubits to exist in states of 0, 1, or both simultaneously, enabling parallel calculation tracks", "type": "leaf"},
                {"label": "Entanglement: Correlation where the measurement of one qubit instantly alters the state of its paired partner across space", "type": "leaf"},
                {"label": "Decoherence: Main hurdle; loss of fragile quantum state due to thermal noise, requiring cryocoolers to keep qubits near absolute zero", "type": "leaf"}
            ]},
            {"label": "India National Quantum Mission", "type": "branch", "date": "NQM 2023", "children": [
                {"label": "Target: Launched in 2023 under DST; aims to build quantum computers with 50-1000 physical qubits in 8 years, and secure quantum networks", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "क्वांटम सिद्धांत", "type": "branch", "date": "यांत्रिकी", "children": [
                {"label": "सुपरपोजीशन: क्यूबिट्स की एक ही समय में 0, 1 या दोनों स्थितियों में मौजूद रहने की क्षमता, जो समानांतर गणना सक्षम करती है", "type": "leaf"},
                {"label": "एन्टांगलमेंट: संबंध जिसमें एक क्यूबिट का मापन अंतरिक्ष में उसके जोड़ेदार साथी की स्थिति को तुरंत बदल देता है", "type": "leaf"},
                {"label": "डिकोहेरेंस (Decoherence): मुख्य बाधा; थर्मल गड़बड़ी के कारण क्वांटम स्थिति का नष्ट होना, जिसके लिए क्रायोकूलर आवश्यक हैं", "type": "leaf"}
            ]},
            {"label": "भारत राष्ट्रीय क्वांटम मिशन", "type": "branch", "date": "NQM 2023", "children": [
                {"label": "लक्ष्य: DST के तहत 2023 में शुरू; 8 वर्षों में 50-1000 भौतिक क्यूबिट वाले क्वांटम कंप्यूटर और सुरक्षित क्वांटम नेटवर्क बनाने का लक्ष्य", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["spectrum"],
        "en": [
            {"label": "Spectrum Management", "type": "branch", "date": "Radio Spectrum", "children": [
                {"label": "Definition: Allocation of electromagnetic frequency bands to cellular network operators, aviation channels, and defense radars", "type": "leaf"},
                {"label": "Auctions: Managed in India by Department of Telecommunications (DoT); grants license rights to telecom companies to broadcast on specific frequencies", "type": "leaf"},
                {"label": "5G Bands: Focuses on low band (sub-1 GHz), mid band (1-6 GHz), and high band (millimeter wave bands above 24 GHz)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "स्पेक्ट्रम प्रबंधन", "type": "branch", "date": "रेडियो स्पेक्ट्रम", "children": [
                {"label": "परिभाषा: सेलुलर नेटवर्क ऑपरेटरों, विमानन चैनलों और रक्षा राडार को विद्युत चुंबकीय आवृत्ति बैंड (Frequency Bands) का आवंटन", "type": "leaf"},
                {"label": "नीलामी: भारत में दूरसंचार विभाग (DoT) द्वारा प्रबंधित; विशिष्ट आवृत्तियों पर प्रसारण के लिए कंपनियों को लाइसेंस अधिकार देना", "type": "leaf"},
                {"label": "5G बैंड: कम बैंड (sub-1 GHz), मध्यम बैंड (1-6 GHz), और उच्च बैंड (24 GHz से ऊपर मिलीमीटर वेव बैंड) पर केंद्रित", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["types-and-applications-of-lasers"],
        "en": [
            {"label": "Laser Characteristics", "type": "branch", "date": "LASER Core", "children": [
                {"label": "Laser Definition: Light Amplification by Stimulated Emission of Radiation; properties include monochromaticity, coherence, and collimation", "type": "leaf"},
                {"label": "Types: Classified by medium into Gas lasers (Helium-Neon, CO2), Solid-state lasers (Ruby, Nd:YAG), and Semiconductor diode lasers", "type": "leaf"}
            ]},
            {"label": "Laser Applications", "type": "branch", "date": "Applications", "children": [
                {"label": "Medical: High-precision eye surgeries (LASIK), dermatologist treatments, and endoscope lasers", "type": "leaf"},
                {"label": "Industries: High-power laser cutting, metal welding, LIDAR sensors for autonomous driving navigation, and barcode scanner modules", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "लेजर की विशेषताएं", "type": "branch", "date": "लेजर कोर", "children": [
                {"label": "लेजर परिभाषा: Light Amplification by Stimulated Emission of Radiation; गुणों में एकवर्णीयता, कला-संबद्धता (Coherence) शामिल हैं", "type": "leaf"},
                {"label": "वर्गीकरण: माध्यम द्वारा गैस लेजर (Helium-Neon, CO2), सॉलिड-स्टेट लेजर (रूबी, Nd:YAG), और सेमीकंडक्टर डायोड लेजर में विभाजित", "type": "leaf"}
            ]},
            {"label": "लेजर के अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                {"label": "चिकित्सा: आँखों की उच्च-सटीकता वाली सर्जरी (LASIK), त्वचा रोग विशेषज्ञ उपचार और एंडोस्कोप लेजर", "type": "leaf"},
                {"label": "उद्योग: उच्च शक्ति लेजर कटिंग, धातु वेल्डिंग, स्वायत्त वाहनों के लिए लिडार (LIDAR) सेंसर और बारकोड स्कैनर", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["types-of-computers"],
        "en": [
            {"label": "Computer Categories", "type": "branch", "date": "Categories", "children": [
                {"label": "Supercomputers: High-performance parallel-processing systems used for climate simulations, nuclear calculations, and cryptography", "type": "leaf"},
                {"label": "Mainframes: Highly stable multi-user machines processing massive transactional databases in banking and insurance sectors", "type": "leaf"},
                {"label": "Minicomputers: Mid-range multi-user servers utilized as local database processors in institutions and universities", "type": "leaf"},
                {"label": "Microcomputers: Desktop PCs, laptops, and tablets powered by single-chip microprocessors", "type": "leaf"},
                {"label": "Embedded systems: Dedicated computer chips performing specific functions within home appliances (ACs, microwave ovens) or cars", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "कंप्यूटर की श्रेणियां", "type": "branch", "date": "श्रेणियां", "children": [
                {"label": "सुपरकंप्यूटर: जलवायु सिमुलेशन, परमाणु गणना और क्रिप्टोग्राफी के लिए उपयोग किए जाने वाले समानांतर-प्रसंस्करण (Parallel Processing) सिस्टम", "type": "leaf"},
                {"label": "मेनफ्रेम: बैंकिंग और बीमा क्षेत्रों में बड़े लेनदेन डेटाबेस को संसाधित करने वाली अत्यधिक स्थिर बहु-उपयोगकर्ता मशीनें", "type": "leaf"},
                {"label": "मिनीकंप्यूटर: मध्यम स्तर के बहु-उपयोगकर्ता सर्वर जो संस्थानों और विश्वविद्यालयों में स्थानीय डेटाबेस प्रोसेसर के रूप में उपयोग होते हैं", "type": "leaf"},
                {"label": "माइक्रोकंप्यूटर: सिंगल-चिप माइक्रोप्रोसेसर द्वारा संचालित डेस्कटॉप पीसी, लैपटॉप, मोबाइल और टैबलेट", "type": "leaf"},
                {"label": "एम्बेडेड सिस्टम (Embedded Systems): कारों या घरेलू उपकरणों (एसी, ओवन) में विशिष्ट कार्य करने के लिए लगाए गए कंप्यूटर चिप्स", "type": "leaf"}
            ]}
        ]
    },
    {
        "keys": ["what-is-nanoscience-and-nanotechnology"],
        "en": [
            {"label": "Definitions & Frameworks", "type": "branch", "date": "Definitions", "children": [
                {"label": "Nanoscience: Study of chemical and physical properties of materials at atomic and molecular scales", "type": "leaf"},
                {"label": "Nanotechnology: Applied engineering focusing on design, production, and utilization of nanometer-scale devices", "type": "leaf"},
                {"label": "Fabrication approaches: Top-down (slicing bulk materials down to nanoscale) and Bottom-up (assembling atom-by-atom or molecular self-assembly)", "type": "leaf"}
            ]}
        ],
        "hi": [
            {"label": "परिभाषाएं और रूपरेखा", "type": "branch", "date": "परिभाषाएं", "children": [
                {"label": "नैनोविज्ञान: परमाणु और आणविक पैमाने पर सामग्रियों के रासायनिक और भौतिक गुणों का अध्ययन", "type": "leaf"},
                {"label": "नैनो तकनीक: नैनोमीटर पैमाने के उपकरणों के डिजाइन, उत्पादन और उपयोग पर केंद्रित व्यावहारिक इंजीनियरिंग", "type": "leaf"},
                {"label": "निर्माण विधियाँ: टॉप-डाउन (बड़ी सामग्री को नैनोस्केल तक काटना) और बॉटम-अप (परमाणु-दर-परमाणु असेंबली)", "type": "leaf"}
            ]}
        ]
    }
]

TRANSLATIONS = {
    "advantages": "लाभ",
    "disadvantages": "हानि",
    "artificial": "कृत्रिम",
    "intelligence": "बुद्धिमत्ता (एआई)",
    "application": "अनुप्रयोग",
    "superconductors": "अतिचालक (सुपरकंडक्टर)",
    "applications": "अनुप्रयोग",
    "nanotechnology": "नैनो तकनीक",
    "robotics": "रोबोटिक्स",
    "basics": "मूल बातें",
    "nanoscience": "नैनोविज्ञान",
    "big": "बिग",
    "data": "डेटा",
    "initiative": "पहल",
    "privacy": "गोपनीयता",
    "classification": "वर्गीकरण",
    "robots": "रोबोट",
    "computer": "कंप्यूटर",
    "terminology": "शब्दावली",
    "fundamental": "बुनियाद",
    "cyber": "साइबर",
    "crime": "अपराध",
    "security": "सुरक्षा",
    "law": "कानून",
    "definition": "परिभाषा",
    "impact": "प्रभाव",
    "ict": "सूचना और संचार प्रौद्योगिकी (ICT)",
    "society": "समाज",
    "evolution": "विकास",
    "telecommunication": "दूरसंचार",
    "government": "सरकारी",
    "initiatives": "पहलें",
    "history": "इतिहास",
    "computers": "कंप्यूटर",
    "internet": "इंटरनेट",
    "things": "वस्तुएं (IoT)",
    "media": "मीडिया",
    "transmission": "प्रसारण",
    "technology": "तकनीक",
    "ministry": "मंत्रालय",
    "information": "सूचना",
    "mobile": "मोबाइल",
    "generations": "पीढ़ियाँ",
    "nanomaterials": "नैनो-पदार्थ",
    "national": "राष्ट्रीय",
    "governance": "शासन (ई-गवर्नेंस)",
    "plan": "योजना",
    "net": "नेट",
    "neutrality": "निष्पक्षता (न्यूट्रैलिटी)",
    "networking": "नेटवर्किंग",
    "bluetooth": "ब्लूटूथ",
    "wifi": "वाई-फाई",
    "hotspot": "हॉटस्पॉट",
    "origination": "उत्पत्ति",
    "quantum": "क्वांटम",
    "computing": "कंप्यूटिंग",
    "spectrum": "स्पेक्ट्रम",
    "types": "प्रकार",
    "lasers": "लेजर",
    "what": "क्या है",
    "is": "है"
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
                {"label": f"Scientific Framework: Analyzing how {t} integrates with IT, communication, and automation systems", "type": "leaf"}
            ]
        },
        {
            "label": f"Processes & Dynamics",
            "type": "branch",
            "date": "Mechanisms",
            "children": [
                {"label": f"Primary Drivers: Factors regulating the development, design, and implementation of {t}", "type": "leaf"},
                {"label": f"Applied Engineering: Exploring the hardware components, communication protocols, and logic of {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"Socio-Economic & Applied Values",
            "type": "branch",
            "date": "Applications",
            "children": [
                {"label": f"Impacts: How advances in {t} affect modern society, industrial efficiency, and digital privacy", "type": "leaf"},
                {"label": f"Case Studies: Notable real-world initiatives, computing platforms, and research models relating to {t}", "type": "leaf"}
            ]
        },
        {
            "label": f"UPSC Exam Syllabus Relevance",
            "type": "branch",
            "date": "UPSC Core",
            "children": [
                {"label": f"Prelims Prep: Key technical terminologies, national policies, and regulatory bodies associated with {t}", "type": "leaf"},
                {"label": f"Mains Answer Writing: Linking {t} with Digital India, security challenges, and national technological missions", "type": "leaf"}
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
                {"label": f"वैज्ञानिक ढांचा: {t} आईटी, संचार और स्वचालन प्रणालियों के साथ कैसे कार्य करता है", "type": "leaf"}
            ]
        },
        {
            "label": f"प्रक्रियाएं and गतिकी",
            "type": "branch",
            "date": "क्रियाविधि",
            "children": [
                {"label": f"प्राथमिक कारक: {t} के विकास, डिजाइन और कार्यान्वयन को नियंत्रित करने वाले तत्व", "type": "leaf"},
                {"label": f"अनुप्रयुक्त इंजीनियरिंग: {t} के हार्डवेयर घटकों, संचार प्रोटोकॉल और तर्क का अध्ययन", "type": "leaf"}
            ]
        },
        {
            "label": f"सामाजिक-आर्थिक और व्यावहारिक महत्व",
            "type": "branch",
            "date": "महत्व",
            "children": [
                {"label": f"प्रभाव: {t} में प्रगति आधुनिक समाज, औद्योगिक दक्षता और डिजिटल गोपनीयता को कैसे प्रभावित करती है", "type": "leaf"},
                {"label": f"क्षेत्रीय मामले: {t} से संबंधित उल्लेखनीय वैश्विक उदाहरण और राष्ट्रीय नीति मॉडल", "type": "leaf"}
            ]
        },
        {
            "label": f"यूपीएससी परीक्षा दृष्टिकोण (UPSC Focus)",
            "type": "branch",
            "date": "परीक्षा",
            "children": [
                {"label": f"प्रारंभिक परीक्षा: {t} से जुड़े तकनीकी नियमों, राष्ट्रीय नीतियों और सामान्य परीक्षा भ्रम", "type": "leaf"},
                {"label": f"मुख्य परीक्षा उत्तर लेखन: {t} को डिजिटल इंडिया, सुरक्षा चुनौतियों और राष्ट्रीय मिशनों से जोड़ना", "type": "leaf"}
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
