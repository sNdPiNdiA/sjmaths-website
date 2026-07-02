#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Press-during-British-Rule"

MINDMAP_DATA = {
    "censorship-of-act-1799": {
        "en": [
            {"label": "Wellesley's Censorship", "type": "branch", "date": "1799", "children": [
                {"label": "Lord Wellesley passed Censorship of Press Act 1799, mandating pre-censorship of all printed matters", "type": "leaf"},
                {"label": "Mandated that names of printer, publisher, and editor must be clearly printed on all copies", "type": "leaf"},
                {"label": "Aimed to prevent French Napoleonic expansion propaganda and anti-government reporting", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "वेलेजली की सेंसरशिप", "type": "branch", "date": "1799", "children": [
                {"label": "लॉर्ड वेलेजली ने 1799 का सेंसरशिप अधिनियम पारित किया, जिससे सभी मुद्रित सामग्रियों की पूर्व-सेंसरशिप अनिवार्य हो गई", "type": "leaf"},
                {"label": "यह अनिवार्य किया गया कि प्रिंटर, प्रकाशक और संपादक के नाम सभी प्रतियों पर स्पष्ट रूप से मुद्रित हों", "type": "leaf"},
                {"label": "फ्रांसीसी नेपोलियन प्रचार और ब्रिटिश विरोधी रिपोर्टिंग को रोकने का मुख्य लक्ष्य था", "type": "leaf"}]}
        ]
    },
    "licensing-regulations-1823": {
        "en": [
            {"label": "Adams' Regulations", "type": "branch", "date": "1823", "children": [
                {"label": "John Adams enacted regulations requiring a license to run a press; printing without license became a penal offence", "type": "leaf"},
                {"label": "Empowered government to seize presses; targeted reformist vernacular papers", "type": "leaf"},
                {"label": "Forced Raja Rammohan Roy's Persian journal 'Mirat-ul-Akbar' to cease publication", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "एडम्स के नियमन", "type": "branch", "date": "1823", "children": [
                {"label": "जॉन एडम्स ने प्रेस चलाने के लिए लाइसेंस अनिवार्य किया; बिना लाइसेंस मुद्रण दंडनीय अपराध बन गया", "type": "leaf"},
                {"label": "सरकारों को प्रेस जब्त करने का अधिकार मिला; सुधारवादी स्थानीय पत्रों को निशाना बनाया गया", "type": "leaf"},
                {"label": "राजा राममोहन राय की फारसी पत्रिका 'मिरात-उल-अखबार' को प्रकाशन बंद करने पर मजबूर किया", "type": "leaf"}]}
        ]
    },
    "press-actmetcalfe-act-1835": {
        "en": [
            {"label": "Metcalfe's Liberation", "type": "branch", "date": "1835", "children": [
                {"label": "Charles Metcalfe ('Liberator of Indian Press') repealed John Adams' restrictive 1823 licensing rules", "type": "leaf"},
                {"label": "Required only a simple declaration of place of publication and printer/publisher details", "type": "leaf"},
                {"label": "Encouraged rapid growth of Indian journalism and vernacular newspapers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "मेटकाफ की मुक्ति नीति", "type": "branch", "date": "1835", "children": [
                {"label": "चार्ल्स मेटकाफ ('भारतीय प्रेस के मुक्तिदाता') ने एडम्स के दमनकारी 1823 नियमों को निरस्त किया", "type": "leaf"},
                {"label": "केवल प्रकाशन स्थल और प्रिंटर/प्रकाशक के विवरण की एक साधारण घोषणा अनिवार्य बनाई", "type": "leaf"},
                {"label": "भारतीय पत्रकारिता और स्थानीय समाचार पत्रों के तेजी से विकास को प्रोत्साहित किया", "type": "leaf"}]}
        ]
    },
    "licensing-act-1857": {
        "en": [
            {"label": "Canning's Controls", "type": "branch", "date": "1857", "children": [
                {"label": "Lord Canning imposed licensing restrictions on all presses for one year due to the 1857 Revolt", "type": "leaf"},
                {"label": "Government reserved the right to ban any publication or search premises", "type": "leaf"},
                {"label": "Applied to both European and Indian owned publications alike", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कैनिंग के नियंत्रण", "type": "branch", "date": "1857", "children": [
                {"label": "लॉर्ड कैनिंग ने 1857 के विद्रोह के कारण एक वर्ष के लिए सभी प्रेसों पर लाइसेंसिंग प्रतिबंध लगाए", "type": "leaf"},
                {"label": "सरकार ने किसी भी प्रकाशन पर प्रतिबंध लगाने या परिसरों की तलाशी लेने का अधिकार सुरक्षित रखा", "type": "leaf"},
                {"label": "यूरोपीय और भारतीय दोनों स्वामित्व वाले प्रकाशनों पर समान रूप से लागू किया गया", "type": "leaf"}]}
        ]
    },
    "registration-act-1867": {
        "en": [
            {"label": "Regulatory Framework", "type": "branch", "date": "1867", "children": [
                {"label": "Replaced Metcalfe's 1835 Act; aimed to regulate, not suppress the press", "type": "leaf"},
                {"label": "Mandated printing printer's/publisher's details on all books & submitting copies to the local government", "type": "leaf"},
                {"label": "Allowed government to keep a record of all literature published in the country", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "नियामक ढांचा", "type": "branch", "date": "1867", "children": [
                {"label": "मेटकाफ के 1835 के अधिनियम की जगह ली; प्रेस को नियंत्रित करना, दबाना नहीं लक्ष्य था", "type": "leaf"},
                {"label": "मुद्रित पुस्तकों पर प्रकाशक का नाम छापना व प्रतियां स्थानीय सरकार को देना अनिवार्य बनाया", "type": "leaf"},
                {"label": "सरकार को देश में प्रकाशित सभी साहित्य का रिकॉर्ड रखने की अनुमति मिली", "type": "leaf"}]}
        ]
    },
    "vernacular-press-act-1878": {
        "en": [
            {"label": "Lytton's Gagging Act", "type": "branch", "date": "1878", "children": [
                {"label": "Passed by Lord Lytton to suppress seditious writing in vernacular (Indian language) newspapers; exempted English-language press", "type": "leaf"},
                {"label": "District Magistrate (DM) could demand a security bond promising not to publish anti-government material", "type": "leaf"},
                {"label": "No Right to Appeal: The decision of the DM was final and could not be challenged in any court of law", "type": "leaf"},
                {"label": "Amrita Bazar Patrika (Sisir Kumar Ghosh) converted from Bengali weekly to English weekly overnight to escape the Act", "type": "leaf"}]},
            {"label": "Repeal", "type": "branch", "date": "1882", "children": [
                {"label": "Repealed by Lord Ripon in 1882 after massive protests and political mobilization by early nationalists", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लिटन का गैगिंग एक्ट", "type": "branch", "date": "1878", "children": [
                {"label": "लॉर्ड लिटन द्वारा स्थानीय (भारतीय भाषाओं के) समाचार पत्रों में देशद्रोही लेखन को दबाने हेतु पारित; अंग्रेजी प्रेस को छूट दी गई", "type": "leaf"},
                {"label": "जिला मजिस्ट्रेट (DM) सरकार विरोधी सामग्री न छापने का वादा करने वाले सुरक्षा बांड की मांग कर सकता था", "type": "leaf"},
                {"label": "अपील का कोई अधिकार नहीं: मजिस्ट्रेट का निर्णय अंतिम था और इसे किसी भी न्यायालय में चुनौती नहीं दी जा सकती थी", "type": "leaf"},
                {"label": "अमृत बाजार पत्रिका (शिशिर कुमार घोष) ने इस अधिनियम से बचने के लिए रातों-रात बंगाली साप्ताहिक से अंग्रेजी में रूपांतरण किया", "type": "leaf"}]},
            {"label": "निरसन", "type": "branch", "date": "1882", "children": [
                {"label": "प्रारंभिक राष्ट्रवादियों के भारी विरोध और राजनीतिक लामबंदी के बाद 1882 में लॉर्ड रिपन द्वारा निरस्त किया गया", "type": "leaf"}]}
        ]
    },
    "newspaper-act-1908": {
        "en": [
            {"label": "Swadeshi Backlash", "type": "branch", "date": "1908", "children": [
                {"label": "Newspaper (Incitement to Offences) Act 1908: Empowered DMs to confiscate presses printing extremist content encouraging murder or violence", "type": "leaf"},
                {"label": "Directly targeted newspapers supporting the revolutionary phase of the Swadeshi Movement", "type": "leaf"},
                {"label": "Provisions allowed quick forfeiture of property, leading to closure of several radical nationalist papers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "स्वदेशी आंदोलन पर प्रहार", "type": "branch", "date": "1908", "children": [
                {"label": "समाचार पत्र (अपराधों को बढ़ावा देना) अधिनियम 1908: मजिस्ट्रेटों को हत्या या हिंसा भड़काने वाले समाचार पत्रों की मुद्रण प्रेस जब्त करने की शक्ति दी", "type": "leaf"},
                {"label": "स्वदेशी आंदोलन के क्रांतिकारी चरण का समर्थन करने वाले समाचार पत्रों को सीधे तौर पर निशाना बनाया", "type": "leaf"},
                {"label": "प्रावधानों ने संपत्ति की त्वरित जब्ती की अनुमति दी, जिससे कई कट्टरपंथी राष्ट्रवादी पत्र बंद हो गए", "type": "leaf"}]}
        ]
    },
    "newspaper-incitement-to-offences-act-1908": {
        "en": [
            {"label": "Anti-Terror Regulations", "type": "branch", "date": "1908", "children": [
                {"label": "Specifically targeted publications inciting revolutionary actions or using explosive substances", "type": "leaf"},
                {"label": "Allowed DMs to cancel declarations and seize property without extensive trial procedures", "type": "leaf"},
                {"label": "Aimed to suppress secret societies' publications and anti-British violence campaigns", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आतंकवाद विरोधी नियमन", "type": "branch", "date": "1908", "children": [
                {"label": "विशेष रूप से क्रांतिकारी गतिविधियों या विस्फोटक पदार्थों का उपयोग करने के लिए उकसाने वाले समाचार पत्रों को लक्षित किया", "type": "leaf"},
                {"label": "मजिस्ट्रेटों को बिना व्यापक परीक्षण प्रक्रियाओं के घोषणाओं को रद्द करने और संपत्ति को जब्त करने की अनुमति दी", "type": "leaf"},
                {"label": "गुप्त सोसाइटियों के प्रकाशनों और ब्रिटिश विरोधी हिंसा अभियानों को दबाने का लक्ष्य था", "type": "leaf"}]}
        ]
    },
    "indian-press-act-1910": {
        "en": [
            {"label": "Security Deposits", "type": "branch", "date": "1910", "children": [
                {"label": "Indian Press Act 1910: Re-imposed registration security (Rs 500 to 2,000) for new presses", "type": "leaf"},
                {"label": "Local governments could forfeit security deposits and confiscate presses for offensive/seditious articles", "type": "leaf"},
                {"label": "Severely restricted freedom of press, reviving worst features of Lytton's 1878 Act", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सुरक्षा जमा राशि", "type": "branch", "date": "1910", "children": [
                {"label": "भारतीय प्रेस अधिनियम 1910: नई प्रेसों के लिए पंजीकरण सुरक्षा (500 से 2,000 रु.) को पुनः लागू किया", "type": "leaf"},
                {"label": "प्रांतीय सरकारों को आपत्तिजनक/राजद्रोही लेखों के लिए जमानत राशि और प्रेस जब्त करने का अधिकार दिया", "type": "leaf"},
                {"label": "प्रेस की स्वतंत्रता को गंभीर रूप से प्रतिबंधित किया, जिससे लिटन के 1878 के अधिनियम के दमनकारी प्रावधान बहाल हुए", "type": "leaf"}]}
        ]
    },
    "press-during-and-after-the-first-world-war": {
        "en": [
            {"label": "WWI Censorship", "type": "branch", "date": "1914-1921", "children": [
                {"label": "Defence of India Rules applied to enforce strict pre-censorship during World War I", "type": "leaf"},
                {"label": "Confiscated security deposits of nationalist papers like Annie Besant's 'New India'", "type": "leaf"},
                {"label": "Press Committee (1921) under Tej Bahadur Sapru recommended repeal of the 1910 Act", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "WWI सेंसरशिप", "type": "branch", "date": "1914-1921", "children": [
                {"label": "प्रथम विश्व युद्ध के दौरान सख्त पूर्व-सेंसरशिप लागू करने के लिए डिफेंस ऑफ इंडिया नियम लागू किए गए", "type": "leaf"},
                {"label": "एनी बेसेंट के 'न्यू इंडिया' जैसे राष्ट्रवादी पत्रों की सुरक्षा जमा राशि जब्त की गई", "type": "leaf"},
                {"label": "तेज बहादुर सप्रू की अध्यक्षता में प्रेस समिति (1921) ने 1910 के अधिनियम को निरस्त करने की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "indian-press-act-1931": {
        "en": [
            {"label": "Emergency Measures", "type": "branch", "date": "1931", "children": [
                {"label": "Passed during Civil Disobedience Movement to suppress national propaganda and salt campaign reports", "type": "leaf"},
                {"label": "Gave provincial governments sweeping powers to seize presses for printing nationalist literature", "type": "leaf"},
                {"label": "Mandated security deposits for new publishers and forfeited deposits of critical papers", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आपातकालीन उपाय", "type": "branch", "date": "1931", "children": [
                {"label": "राष्ट्रीय प्रचार और नमक सत्याग्रह की रिपोर्टों को दबाने के लिए सविनय अवज्ञा आंदोलन के दौरान पारित", "type": "leaf"},
                {"label": "प्रांतीय सरकारों को राष्ट्रवादी साहित्य छापने के लिए मुद्रण प्रेसों को जब्त करने के व्यापक अधिकार दिए", "type": "leaf"},
                {"label": "नए प्रकाशकों के लिए सुरक्षा जमा अनिवार्य किया और आलोचनात्मक पत्रों की जमानत राशि जब्त की", "type": "leaf"}]}
        ]
    },
    "indian-press-emergency-powers-act-1931": {
        "en": [
            {"label": "Suppression of Civil Disobedience", "type": "branch", "date": "1931", "children": [
                {"label": "Gave absolute powers to local governments to declare any press printing anti-government materials illegal", "type": "leaf"},
                {"label": "Empowered DMs to seize security deposits and machinery without trial", "type": "leaf"},
                {"label": "Directly targeted Congress circulars, pamphlets, and nationalist bulletins", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सविनय अवज्ञा का दमन", "type": "branch", "date": "1931", "children": [
                {"label": "स्थानीय सरकारों को किसी भी सरकार विरोधी सामग्री छापने वाले प्रेस को अवैध घोषित करने के पूर्ण अधिकार दिए", "type": "leaf"},
                {"label": "बिना मुकदमे के सुरक्षा जमा और मशीनरी को जब्त करने के लिए जिला मजिस्ट्रेटों को सशक्त किया", "type": "leaf"},
                {"label": "कांग्रेस के परिपत्रों, पुस्तिकाओं और राष्ट्रवादी बुलेटिनों को सीधे तौर पर निशाना बनाया", "type": "leaf"}]}
        ]
    },
    "press-during-the-second-world-war": {
        "en": [
            {"label": "WWII Censorship", "type": "branch", "date": "1939-1945", "children": [
                {"label": "Strict pre-censorship enforced under the Defence of India Act", "type": "leaf"},
                {"label": "Banned reporting on the Quit India Movement, Congress committee meetings, and nationalist leaders", "type": "leaf"},
                {"label": "Forced closures of several nationalist newspapers that refused to comply with censorship demands", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "WWII सेंसरशिप", "type": "branch", "date": "1939-1945", "children": [
                {"label": "डिफेंस ऑफ इंडिया एक्ट के तहत सख्त पूर्व-सेंसरशिप लागू की गई", "type": "leaf"},
                {"label": "भारत छोड़ो आंदोलन, कांग्रेस समिति की बैठकों और राष्ट्रवादी नेताओं पर रिपोर्टिंग पर प्रतिबंध लगाया", "type": "leaf"},
                {"label": "सेंसरशिप मांगों का पालन करने से इनकार करने वाले कई राष्ट्रवादी समाचार पत्रों को जबरन बंद कराया", "type": "leaf"}]}
        ]
    },
    "press-regulating-act-1942": {
        "en": [
            {"label": "Quit India Blackout", "type": "branch", "date": "1942", "children": [
                {"label": "Enacted specifically to control information regarding the Quit India Movement protests", "type": "leaf"},
                {"label": "Imposed pre-censorship on all news relating to public disturbances, arrests, and strikes", "type": "leaf"},
                {"label": "Restricted news agency operations and monitored incoming foreign cables", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "भारत छोड़ो ब्लैकआउट", "type": "branch", "date": "1942", "children": [
                {"label": "विशेष रूप से भारत छोड़ो आंदोलन के विरोध प्रदर्शनों के संबंध में जानकारी को नियंत्रित करने के लिए लागू किया गया", "type": "leaf"},
                {"label": "सार्वजनिक अशांति, गिरफ्तारियों और हड़तालों से संबंधित सभी समाचारों पर पूर्व-सेंसरशिप लागू की", "type": "leaf"},
                {"label": "समाचार एजेंसियों के संचालन को प्रतिबंधित किया और आने वाले विदेशी केबलों की निगरानी की", "type": "leaf"}]}
        ]
    },
    "press-inquiry-committee-1947": {
        "en": [
            {"label": "Constitutional Transition", "type": "branch", "date": "1947", "children": [
                {"label": "Set up by the newly independent Government of India to review existing colonial press laws", "type": "leaf"},
                {"label": "Examined press laws in light of the proposed Fundamental Rights (Article 19(1)(a))", "type": "leaf"},
                {"label": "Recommended repeal of the Indian Press (Emergency Powers) Act 1931 and modification of the 1867 Act", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संवैधानिक संक्रमण", "type": "branch", "date": "1947", "children": [
                {"label": "मौजूदा औपनिवेशिक प्रेस कानूनों की समीक्षा के लिए नव स्वतंत्र भारत सरकार द्वारा गठित", "type": "leaf"},
                {"label": "प्रस्तावित मौलिक अधिकारों (अनुच्छेद 19(1)(a)) के आलोक में प्रेस कानूनों की जांच की", "type": "leaf"},
                {"label": "भारतीय प्रेस (आपातकालीन शक्तियां) अधिनियम 1931 को निरस्त करने और 1867 के अधिनियम में संशोधन की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "press-post-independence": {
        "en": [
            {"label": "Democratic Standards", "type": "branch", "date": "Post-1947", "children": [
                {"label": "First Press Commission (1954): Recommended establishment of the Press Council of India to safeguard freedom of press", "type": "leaf"},
                {"label": "Objectionable Matter Act 1951 passed to regulate sensationalism but met with criticism and was eventually repealed", "type": "leaf"},
                {"label": "Introduced the concept of Press Registrar of India to monitor newspaper ownership & print media health", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लोकतांत्रिक मानक", "type": "branch", "date": "1947 के बाद", "children": [
                {"label": "प्रथम प्रेस आयोग (1954): प्रेस की स्वतंत्रता की रक्षा के लिए भारतीय प्रेस परिषद की स्थापना की सिफारिश की", "type": "leaf"},
                {"label": "आपत्तिजनक विषय अधिनियम 1951 सनसनीखेज खबरों को नियंत्रित करने के लिए पारित हुआ लेकिन आलोचना के बाद निरस्त किया गया", "type": "leaf"},
                {"label": "समाचार पत्रों के स्वामित्व और प्रिंट मीडिया के स्वास्थ्य की निगरानी के लिए प्रेस रजिस्ट्रार की अवधारणा शुरू की", "type": "leaf"}]}
        ]
    },
    "james-augustus-hickeys-bengal-gazette": {
        "en": [
            {"label": "The First Newspaper", "type": "branch", "date": "1780-1782", "children": [
                {"label": "Bengal Gazette: First newspaper in India, started by James Augustus Hicky in Calcutta", "type": "leaf"},
                {"label": "Known for its independent stance; criticized Governor-General Warren Hastings and Chief Justice Elijah Impey", "type": "leaf"},
                {"label": "Press confiscated and shut down by the government in 1782 for publishing defamatory reports against officials", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रथम समाचार पत्र", "type": "branch", "date": "1780-1782", "children": [
                {"label": "बंगाल गजट: जेम्स ऑगस्टस हिकी द्वारा कलकत्ता में शुरू किया गया भारत का पहला समाचार पत्र था", "type": "leaf"},
                {"label": "अपने स्वतंत्र रुख के लिए जाना जाता था; गवर्नर-जनरल वारेन हेस्टिंग्स और मुख्य न्यायाधीश एलिजा इम्पे की आलोचना की", "type": "leaf"},
                {"label": "अधिकारियों के खिलाफ मानहानिकारक रिपोर्ट प्रकाशित करने के लिए 1782 में सरकार द्वारा प्रेस जब्त कर बंद कर दिया गया", "type": "leaf"}]}
        ]
    },
    "different-publications-and-journals": {
        "en": [
            {"label": "Early Publications", "type": "branch", "date": "Journals", "children": [
                {"label": "Raja Rammohan Roy published Sambad Kaumudi (Bengali, 1821) and Mirat-ul-Akbar (Persian, 1822) to propagate reform", "type": "leaf"},
                {"label": "Nationalist Press: Kesari (Marathi) & Mahratta (English) by Tilak; Amrita Bazar Patrika by Sisir Kumar Ghosh", "type": "leaf"},
                {"label": "Other Journals: Bengalee (Surendranath Banerjea), The Hindu (G. Subramaniya Aiyar), Swadesamitran (Aiyar), Voice of India (Dadabhai Naoroji)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रारंभिक प्रकाशन", "type": "branch", "date": "पत्रिकाएं", "children": [
                {"label": "राजा राममोहन राय ने सुधारों के प्रचार के लिए 'संवाद कौमुदी' (बंगाली, 1821) और 'मिरात-उल-अखबार' (फारसी, 1822) का प्रकाशन किया", "type": "leaf"},
                {"label": "राष्ट्रवादी प्रेस: तिलक द्वारा केसरी (मराठी) और महरत्ता (अंग्रेजी); शिशिर कुमार घोष द्वारा अमृत बाजार पत्रिका", "type": "leaf"},
                {"label": "अन्य पत्रिकाएं: बंगाली (सुरेंद्रनाथ बनर्जी), द हिंदू (जी. सुब्रमण्यम अय्यर), स्वदेशमित्रन (अय्यर), वॉयस ऑफ इंडिया (दादाभाई नौरोजी)", "type": "leaf"}]}
        ]
    },
    "various-newspapersjournals-and-their-authors": {
        "en": [
            {"label": "Authors & Outlets", "type": "branch", "date": "Editors", "children": [
                {"label": "G. Subramaniya Aiyar: Swadesamitran & The Hindu; promoted nationalist demands in Madras Presidency", "type": "leaf"},
                {"label": "Surendranath Banerjea: Bengalee; champion of constitutional reforms and press freedom", "type": "leaf"},
                {"label": "Dadabhai Naoroji: Voice of India; highlighted economic drain of India", "type": "leaf"},
                {"label": "G.K. Gokhale: Sudharak; focused on social reform and economic critique", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "लेखक और पत्रिकाएं", "type": "branch", "date": "संपादक", "children": [
                {"label": "जी. सुब्रमण्यम अय्यर: स्वदेशमित्रन और द हिंदू; मद्रास प्रेसीडेंसी में राष्ट्रवादी मांगों को बढ़ावा दिया", "type": "leaf"},
                {"label": "सुरेंद्रनाथ बनर्जी: बंगाली; संवैधानिक सुधारों और प्रेस की स्वतंत्रता के प्रबल समर्थक", "type": "leaf"},
                {"label": "दादाभाई नौरोजी: वॉयस ऑफ इंडिया; भारत के आर्थिक दोहन (ड्रेन ऑफ वेल्थ) को रेखांकित किया", "type": "leaf"},
                {"label": "जी.के. गोखले: सुधारक; सामाजिक सुधार और आर्थिक समालोचना पर ध्यान केंद्रित किया", "type": "leaf"}]}
        ]
    },
    "struggle-by-early-nationalists-to-secure-press-freedom": {
        "en": [
            {"label": "Political Education Tool", "type": "branch", "date": "Struggle", "children": [
                {"label": "Early nationalists used press as a non-profit tool for political education, propagating national demands, and mobilizing public opinion", "type": "leaf"},
                {"label": "Surendranath Banerjea: First Indian journalist to be imprisoned (1883) for criticizing a High Court judge's decision in Bengalee", "type": "leaf"},
                {"label": "Tilak's Imprisonments: Jailed in 1897 ( Shivaji speech) and 1908 ( Kesari editorial defending bomb throwing); became a popular nationalist icon", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक शिक्षा का उपकरण", "type": "branch", "date": "संघर्ष", "children": [
                {"label": "प्रारंभिक राष्ट्रवादियों ने प्रेस का उपयोग व्यावसायिक लाभ के बजाय राजनीतिक शिक्षा और मांगों के प्रचार हेतु किया", "type": "leaf"},
                {"label": "सुरेंद्रनाथ बनर्जी: उच्च न्यायालय के न्यायाधीश के फैसले की आलोचना हेतु जेल जाने वाले पहले भारतीय पत्रकार (1883)", "type": "leaf"},
                {"label": "तिलक की जेल यात्राएं: 1897 (शिवाजी उत्सव भाषण) और 1908 (केसरी संपादकीय में बम विस्फोट का बचाव) में जेल; जनवादी राष्ट्रवादी आइकन बने", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "censorship-of-act-1799": "censorship-of-act-1799",
    "licensing-regulations-1823": "licensing-regulations-1823",
    "press-actmetcalfe-act-1835": "press-actmetcalfe-act-1835",
    "licensing-act-1857": "licensing-act-1857",
    "registration-act-1867": "registration-act-1867",
    "vernacular-press-act-1878": "vernacular-press-act-1878",
    "newspaper-act-1908": "newspaper-act-1908",
    "newspaper-incitement-to-offences-act-1908": "newspaper-incitement-to-offences-act-1908",
    "indian-press-act-1910": "indian-press-act-1910",
    "press-during-and-after-the-first-world-war": "press-during-and-after-the-first-world-war",
    "indian-press-act-1931": "indian-press-act-1931",
    "indian-press-emergency-powers-act-1931": "indian-press-emergency-powers-act-1931",
    "press-regulating-act-1942": "press-regulating-act-1942",
    "press-during-the-second-world-war": "press-during-the-second-world-war",
    "press-inquiry-committee-1947": "press-inquiry-committee-1947",
    "press-post-independence": "press-post-independence",
    "james-augustus-hickeys-bengal-gazette": "james-augustus-hickeys-bengal-gazette",
    "different-publications-and-journals": "different-publications-and-journals",
    "various-newspapersjournals-and-their-authors": "various-newspapersjournals-and-their-authors",
    "struggle-by-early-nationalists-to-secure-press-freedom": "struggle-by-early-nationalists-to-secure-press-freedom"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('INC', 'INC (Indian National Congress)')
    title = title.replace('Press ActMetcalfe', 'Press Act (Metcalfe Act)')
    title = title.replace('NewspapersJournals', 'Newspapers & Journals')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'a', 'an', 'about'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def ensure_base_html(path, folder_name):
    if os.path.exists(path):
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    clean_title = get_clean_title(folder_name)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{clean_title} - UPSC Civil Services Study Guide | SJMaths</title>
</head>
<body>
    <!-- Interactive Mindmap -->
</body>
</html>
"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def create_hi_stub(en_html_path, hi_html_path, folder_name):
    if not os.path.exists(en_html_path):
        ensure_base_html(en_html_path, folder_name)
        
    with open(en_html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<html lang="en">', '<html lang="hi">', 1)
    
    clean_title = get_clean_title(folder_name)
    if '<title>' in html:
        html = re.sub(r'<title>[^<]+</title>',
                      f'<title>{clean_title} (Hindi) - UPSC Civil Services Study Guide | SJMaths</title>',
                      html, count=1)
    
    os.makedirs(os.path.dirname(hi_html_path), exist_ok=True)
    with open(hi_html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def inject_mindmap(html_path, folder_name, lang):
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')

    # Remove any old mindmap links/scripts
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
                '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=1">\n']:
        html = html.replace(old, '')
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->', '\n            <!-- Deep-Dive Study Guide (Dynamically Rendered) -->', html, flags=re.DOTALL)
    html = re.sub(r'\s*<!-- Interactive Mindmap -->.*?renderMindmap\(.*?\);\s*</script>', '', html, flags=re.DOTALL)

    clean_title = get_clean_title(folder_name)
    key = folder_name.lower()
    canonical_key = MINDMAP_MAPPINGS.get(key, "early-regulations")
    
    branches = MINDMAP_DATA.get(canonical_key, {}).get(lang, [])
    if not branches:
        branches = [{"label": clean_title, "type": "branch", "date": "Topic", "children": [{"label": "Information structured here for UPSC", "type": "leaf"}]}]
        
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html and '<head>' in html:
        html = html.replace('</head>', css_link + '</head>')

    if lang == 'hi':
        instr = 'किसी कार्ड पर क्लिक करें।'
        title_text = f"{clean_title} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Click any card to expand or collapse.'
        title_text = f"{clean_title} &mdash; Interactive Mindmap"

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
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    elif '<div class="tab-panel active" id="notes-panel" role="tabpanel"' in html:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        html = html.replace(marker, marker + '\n' + mindmap_card, 1)
    elif '<body>' in html:
        html = html.replace('<body>', '<body>\n' + mindmap_card, 1)

    tree_json = json.dumps(mindmap_data, ensure_ascii=False)
    inline_script = f'''
    <!-- Interactive Mindmap -->
    <script src="/assets/js/mindmap-engine.min.js?v=2"></script>
    <script>
    renderMindmap({tree_json}, undefined, '{lang}');
    </script>
'''
    if '</body>' in html:
        html = html.replace('</body>', inline_script + '\n</body>')
    else:
        html += inline_script

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

def main():
    total_en = 0
    total_hi = 0
    
    if not os.path.exists(BASE_DIR):
        print(f"Directory {BASE_DIR} does not exist.")
        return

    for root_dir, dirs, files in os.walk(BASE_DIR):
        dirs[:] = [d for d in dirs if d != 'hi']
        folder_name = os.path.basename(root_dir)
        
        if root_dir == BASE_DIR:
            continue

        en_path = os.path.join(root_dir, 'index.html')
        hi_dir = os.path.join(root_dir, 'hi')
        hi_path = os.path.join(hi_dir, 'index.html')

        ensure_base_html(en_path, folder_name)
        inject_mindmap(en_path, folder_name, 'en')
        total_en += 1

        if not os.path.exists(hi_path):
            create_hi_stub(en_path, hi_path, folder_name)

        inject_mindmap(hi_path, folder_name, 'hi')
        total_hi += 1
        
        print(f"Processed: {folder_name}")

    print(f"\nCreated+patched {total_en} English and {total_hi} Hindi pages.")

if __name__ == '__main__':
    main()
