#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, re, json

BASE_DIR = r"upsc/modern_history/Important-Personalities"

MINDMAP_DATA = {
    "raja-ram-mohan-roy": {
        "en": [
            {"label": "Renaissance Father", "type": "branch", "date": "1772-1833", "children": [
                {"label": "Brahmo Sabha (1828); renamed Brahmo Samaj (1830) to propagate monotheism", "type": "leaf"},
                {"label": "Gift to Monotheists (Tuhfat-ul-Muwahhidin, 1809) in Persian; Precepts of Jesus (1820)", "type": "leaf"}]},
            {"label": "Journals & Education", "type": "branch", "date": "Press", "children": [
                {"label": "Sambad Kaumudi (Bengali weekly) and Mirat-ul-Akbar (Persian journal)", "type": "leaf"},
                {"label": "Founded Hindu College (1817) with David Hare; Vedanta College (1825)", "type": "leaf"}]},
            {"label": "Reforms & Title", "type": "branch", "date": "Sati", "children": [
                {"label": "Advocated Sati abolition; led to Sati Prohibition Regulation XVII (1829) under Bentinck", "type": "leaf"},
                {"label": "Title 'Raja' given by Mughal Emperor Akbar II (sent to England to lobby for pension)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "पुनर्जागरण के जनक", "type": "branch", "date": "1772-1833", "children": [
                {"label": "एकेश्वरवाद के प्रचार हेतु ब्रह्म सभा (1828); बाद में ब्रह्म समाज (1830) नामकरण", "type": "leaf"},
                {"label": "फारसी में एकेश्वरवादियों को उपहार (तुहफ़त-उल-मुवाहिदीन, 1809); प्रीसेप्ट्स ऑफ जीसस (1820)", "type": "leaf"}]},
            {"label": "पत्रिकाएँ और शिक्षा", "type": "branch", "date": "प्रेस", "children": [
                {"label": "संवाद कौमुदी (बंगाली साप्ताहिक) और मिरात-उल-अखबार (फारसी पत्रिका) का प्रकाशन", "type": "leaf"},
                {"label": "डेविड हेयर के साथ हिंदू कॉलेज (1817); वेदांत कॉलेज (1825) की स्थापना", "type": "leaf"}]},
            {"label": "सुधार और उपाधि", "type": "branch", "date": "सती", "children": [
                {"label": "सती उन्मूलन आंदोलन; विलियम बेंटिक द्वारा सती निषेध नियमन XVII (1829) पारित कराया", "type": "leaf"},
                {"label": "मुगल सम्राट अकबर द्वितीय द्वारा 'राजा' की उपाधि (पेंशन के संबंध में इंग्लैंड भेजा गया)", "type": "leaf"}]}
        ]
    },
    "swami-dayananda-saraswati": {
        "en": [
            {"label": "Arya Samaj", "type": "branch", "date": "1824-1883", "children": [
                {"label": "Founded Arya Samaj (1875 at Bombay, later Lahore) as reform movement", "type": "leaf"},
                {"label": "Satyarth Prakash (1874) - primary text written in Hindi", "type": "leaf"}]},
            {"label": "Slogans & Philosophy", "type": "branch", "date": "Vedas", "children": [
                {"label": "Go Back to Vedas (Vedas as source of all truth); rejected post-Vedic texts & Puranas", "type": "leaf"},
                {"label": "Shuddhi Movement to reconvert non-Hindus; opposed caste by birth & idol worship", "type": "leaf"}]},
            {"label": "Legacy", "type": "branch", "date": "Education", "children": [
                {"label": "DAV (Dayanand Anglo-Vedic) schools started (Lala Hansraj); Gurukul Kangri (Swami Shraddhanand)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "आर्य समाज", "type": "branch", "date": "1824-1883", "children": [
                {"label": "सुधार आंदोलन के रूप में आर्य समाज (1875 में बॉम्बे, बाद में लाहौर) की स्थापना की", "type": "leaf"},
                {"label": "सत्यार्थ प्रकाश (1874) - हिंदी में लिखित मुख्य ग्रंथ", "type": "leaf"}]},
            {"label": "नारे और दर्शन", "type": "branch", "date": "वेद", "children": [
                {"label": "'वेदों की ओर लौटो' का नारा दिया (वेदों को परम सत्य माना); उत्तर-वैदिक ग्रंथों व पुराणों को नकारा", "type": "leaf"},
                {"label": "गैर-हिंदुओं के धर्म परिवर्तन हेतु शुद्धि आंदोलन; जन्म आधारित जाति व्यवस्था व मूर्ति पूजा का विरोध", "type": "leaf"}]},
            {"label": "विरासत", "type": "branch", "date": "शिक्षा", "children": [
                {"label": "डीएवी (दयानंद एंग्लो-वैदिक) स्कूलों की शुरुआत (लाला हंसराज); गुरुकुल कांगड़ी (स्वामी श्रद्धानंद)", "type": "leaf"}]}
        ]
    },
    "swami-vivekananda": {
        "en": [
            {"label": "Ramakrishna Mission", "type": "branch", "date": "1863-1902", "children": [
                {"label": "Founded Ramakrishna Mission (1897) at Belur, Bengal to spread Neo-Vedanta & serve humanity", "type": "leaf"},
                {"label": "Guru: Ramakrishna Paramahamsa (realized unity of all religions)", "type": "leaf"}]},
            {"label": "Global Impact", "type": "branch", "date": "1893 Chicago", "children": [
                {"label": "Speech at Parliament of Religions, Chicago (1893); introduced Yoga & Vedanta to West", "type": "leaf"}]},
            {"label": "Literary Works", "type": "branch", "date": "Publications", "children": [
                {"label": "Prabuddha Bharata (English journal) and Udbodhan (Bengali monthly)", "type": "leaf"},
                {"label": "Books: Jnana Yoga, Bhakti Yoga, Raja Yoga, Karma Yoga", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "रामकृष्ण मिशन", "type": "branch", "date": "1863-1902", "children": [
                {"label": "नव-वेदांत के प्रसार और मानव सेवा हेतु बेलूर (बंगाल) में रामकृष्ण मिशन (1897) की स्थापना की", "type": "leaf"},
                {"label": "गुरु: रामकृष्ण परमहंस (जिन्होंने सभी धर्मों की सत्यता और एकता का अनुभव किया)", "type": "leaf"}]},
            {"label": "वैश्विक प्रभाव", "type": "branch", "date": "1893 शिकागो", "children": [
                {"label": "शिकागो धर्म संसद (1893) में ऐतिहासिक भाषण; पश्चिम जगत को योग और वेदांत से परिचित कराया", "type": "leaf"}]},
            {"label": "साहित्यिक कृतियाँ", "type": "branch", "date": "प्रकाशन", "children": [
                {"label": "प्रबुद्ध भारत (अंग्रेजी पत्रिका) और उद्बोधन (बंगाली मासिक) का संचालन", "type": "leaf"},
                {"label": "पुस्तकें: ज्ञान योग, भक्ति योग, राज योग, कर्म योग", "type": "leaf"}]}
        ]
    },
    "ishwar-chandra-vidyasagar": {
        "en": [
            {"label": "Widow Emancipation", "type": "branch", "date": "Widows", "children": [
                {"label": "Campaigned for widow remarriage; petition led to Hindu Widow Remarriage Act XV (1856)", "type": "leaf"},
                {"label": "Conducted the first legal Hindu widow remarriage in 1856 (his son also married a widow)", "type": "leaf"}]},
            {"label": "Education & Language", "type": "branch", "date": "Sanskrit College", "children": [
                {"label": "Principal of Sanskrit College; opened admission to non-Brahmin students", "type": "leaf"},
                {"label": "Sharnamuto (Bengali primer Shishu Shiksha) and Varna Parichay (simplified Bengali script)", "type": "leaf"},
                {"label": "Established Bethune School (1849) for girls with JED Bethune", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "विधवा कल्याण", "type": "branch", "date": "विधवाएँ", "children": [
                {"label": "विधवा पुनर्विवाह हेतु आंदोलन; याचिका के कारण हिंदू विधवा पुनर्विवाह अधिनियम XV (1856) पारित", "type": "leaf"},
                {"label": "1856 में पहला कानूनी हिंदू विधवा पुनर्विवाह संपन्न कराया (स्वयं के पुत्र का विवाह भी विधवा से कराया)", "type": "leaf"}]},
            {"label": "शिक्षा और भाषा", "type": "branch", "date": "संस्कृत कॉलेज", "children": [
                {"label": "संस्कृत कॉलेज के प्राचार्य; गैर-ब्राह्मण छात्रों के लिए भी संस्कृत का अध्ययन खोला", "type": "leaf"},
                {"label": "वर्ण परिचय (बंगाली लिपि का सरलीकरण) और शिशु शिक्षा का संपादन किया", "type": "leaf"},
                {"label": "जे.ई.डी. बेथून के साथ मिलकर बालिकाओं के लिए बेथून स्कूल (1849) की स्थापना की", "type": "leaf"}]}
        ]
    },
    "dr-bhimrao-ramji-ambedkar": {
        "en": [
            {"label": "Organizations", "type": "branch", "date": "Groups", "children": [
                {"label": "Bahishkrit Hitakarini Sabha (1924) to spread education among depressed classes", "type": "leaf"},
                {"label": "Independent Labour Party (1936); Scheduled Castes Federation (1942)", "type": "leaf"}]},
            {"label": "Movements & Pacts", "type": "branch", "date": "Agitations", "children": [
                {"label": "Mahad Satyagraha (1927) for untouchables' right to draw water from Chavdar tank", "type": "leaf"},
                {"label": "Attended all three Round Table Conferences (1830-32) representing depressed classes", "type": "leaf"},
                {"label": "Poona Pact (1932) signed with Madan Mohan Malaviya (representing Gandhi) for reserved seats", "type": "leaf"}]},
            {"label": "Books & Conversion", "type": "branch", "date": "Ideas", "children": [
                {"label": "Annihilation of Caste (1936), The Untouchables, Who Were the Shudras?", "type": "leaf"},
                {"label": "Converted to Buddhism in Nagpur (1956) along with half a million followers", "type": "leaf"}]},
            {"label": "Nation Building", "type": "branch", "date": "Constitution", "children": [
                {"label": "Chairman of Drafting Committee of Indian Constitution; India's first Law Minister", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संगठन", "type": "branch", "date": "समूह", "children": [
                {"label": "वंचित वर्गों में शिक्षा के प्रसार हेतु बहिष्कृत हितकारिणी सभा (1924) की स्थापना", "type": "leaf"},
                {"label": "इंडिपेंडेंट लेबर पार्टी (1936) और अनुसूचित जाति संघ (1942) का गठन किया", "type": "leaf"}]},
            {"label": "आंदोलन और समझौते", "type": "branch", "date": "सत्याग्रह", "children": [
                {"label": "महाड़ सत्याग्रह (1927): चवदार तालाब से वंचितों के जल उपयोग के अधिकार हेतु संघर्ष", "type": "leaf"},
                {"label": "दलित वर्ग के प्रतिनिधि के रूप में तीनों गोलमेज सम्मेलनों (1930-32) में भाग लिया", "type": "leaf"},
                {"label": "गांधीजी की ओर से मदन मोहन मालवीय के साथ ऐतिहासिक पूना पैक्ट (1932) पर हस्ताक्षर", "type": "leaf"}]},
            {"label": "साहित्य और धर्म परिवर्तन", "type": "branch", "date": "विचार", "children": [
                {"label": "जाति का उच्छेद (Annihilation of Caste, 1936), शूद्र कौन थे? (Who Were the Shudras?)", "type": "leaf"},
                {"label": "नागपुर में बौद्ध धर्म स्वीकार किया (1956) और नवयान शाखा की नींव रखी", "type": "leaf"}]},
            {"label": "राष्ट्र निर्माण", "type": "branch", "date": "संविधान", "children": [
                {"label": "संविधान सभा की मसौदा (प्रारूप) समिति के अध्यक्ष; स्वतंत्र भारत के प्रथम कानून मंत्री", "type": "leaf"}]}
        ]
    },
    "jyotiba-phule": {
        "en": [
            {"label": "Satyashodhak Samaj", "type": "branch", "date": "1827-1890", "children": [
                {"label": "Founded Satyashodhak Samaj (1873) in Maharashtra to challenge Brahminical supremacy", "type": "leaf"},
                {"label": "Advocated social justice, equal rights, and rejected middleman priests", "type": "leaf"}]},
            {"label": "Education Works", "type": "branch", "date": "Pune Schools", "children": [
                {"label": "Established first girls' school in India at Bhide Wada, Pune (1848) with Savitribai Phule", "type": "leaf"},
                {"label": "Opened home for prevention of infanticide (widow shelter) in 1863", "type": "leaf"}]},
            {"label": "Books", "type": "branch", "date": "Publications", "children": [
                {"label": "Gulamgiri (Slavery, 1873) - dedicated to the American movement against slavery", "type": "leaf"},
                {"label": "Shetrachyacha Asud (Whipcord of the Cultivator) and Sarvajanik Satyadharma", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "सत्यशोधक समाज", "type": "branch", "date": "1827-1890", "children": [
                {"label": "महाराष्ट्र में ब्राह्मणवादी वर्चस्व को चुनौती देने हेतु सत्यशोधक समाज (1873) की स्थापना की", "type": "leaf"},
                {"label": "सामाजिक न्याय और समान अधिकारों की वकालत की; पुरोहित वर्ग की मध्यस्थता का विरोध किया", "type": "leaf"}]},
            {"label": "शिक्षा क्षेत्र में योगदान", "type": "branch", "date": "पुणे स्कूल", "children": [
                {"label": "पत्नी सावित्रीबाई फुले के साथ भिडे वाडा (पुणे) में प्रथम बालिका विद्यालय (1848) खोला", "type": "leaf"},
                {"label": "बाल हत्या रोकने हेतु भारत का पहला शिशुगृह/विधवा आश्रय गृह (1863) खोला", "type": "leaf"}]},
            {"label": "साहित्यिक कृतियाँ", "type": "branch", "date": "प्रकाशन", "children": [
                {"label": "गुलामगिरी (1873) - इसे अमेरिकी दास प्रथा विरोधी आंदोलन को समर्पित किया", "type": "leaf"},
                {"label": "शेतकऱ्यांचा आसूड (किसान का कोड़ा) और सार्वजनिक सत्यधर्म नामक कृतियाँ लिखीं", "type": "leaf"}]}
        ]
    },
    "keshab-chandra-sen": {
        "en": [
            {"label": "Brahmo Samaj Splits", "type": "branch", "date": "1838-1884", "children": [
                {"label": "Joined Brahmo Samaj (1857); split with Debendranath Tagore in 1866", "type": "leaf"},
                {"label": "Founded Brahmo Samaj of India (1866) (Tagore's faction became Adi Brahmo Samaj)", "type": "leaf"},
                {"label": "Second Split (1878): Followers broke away to form Sadharan Brahmo Samaj after Sen married his minor daughter to Cooch Behar Prince", "type": "leaf"}]},
            {"label": "Socio-Legal Acts", "type": "branch", "date": "Reforms", "children": [
                {"label": "Efforts led to Native Marriage Act / Civil Marriage Act (1872) fixing marriageable ages", "type": "leaf"},
                {"label": "Founded the Indian Reform Association (1870)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "ब्रह्म समाज में विभाजन", "type": "branch", "date": "1838-1884", "children": [
                {"label": "1857 में ब्रह्म समाज में शामिल हुए; 1866 में देवेंद्रनाथ टैगोर से वैचारिक मतभेद पर अलग हुए", "type": "leaf"},
                {"label": "भारतीय ब्रह्म समाज (1866) की स्थापना की (टैगोर का धड़ा 'आदि ब्रह्म समाज' कहलाया)", "type": "leaf"},
                {"label": "द्वितीय विभाजन (1878): सेन द्वारा अपनी अल्पायु पुत्री का विवाह कूचबिहार के राजा से करने पर अनुयायियों ने 'साधारण ब्रह्म समाज' बनाया", "type": "leaf"}]},
            {"label": "कानूनी सुधार", "type": "branch", "date": "सुधार", "children": [
                {"label": "उनके प्रयासों से नेटिव मैरिज एक्ट / सिविल मैरिज एक्ट (1872) पारित हुआ, जिसने बाल विवाह प्रतिबंधित किया", "type": "leaf"},
                {"label": "इंडियन रिफॉर्म एसोसिएशन (भारतीय सुधार संघ, 1870) की स्थापना की", "type": "leaf"}]}
        ]
    },
    "mahadev-govind-ranade": {
        "en": [
            {"label": "Organizations", "type": "branch", "date": "Reforms", "children": [
                {"label": "Co-founded Poona Sarvajanik Sabha (1870) to represent people's voice to government", "type": "leaf"},
                {"label": "Prarthana Samaj (1867) active member & leader; Indian National Social Conference (1887)", "type": "leaf"}]},
            {"label": "Judicial & Academic", "type": "branch", "date": "Legacy", "children": [
                {"label": "Judge of Bombay High Court; mentor to Gopal Krishna Gokhale & Bal Gangadhar Tilak", "type": "leaf"},
                {"label": "Advocated industrialization, Swadeshi economy, and widow remarriage (Widow Marriage Association 1861)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "संगठन", "type": "branch", "date": "सुधार", "children": [
                {"label": "जनता की आवाज़ सरकार तक पहुँचाने हेतु पूना सार्वजनिक सभा (1870) के सह-संस्थापक बने", "type": "leaf"},
                {"label": "प्रार्थना समाज (1867) के प्रमुख मार्गदर्शक; भारतीय राष्ट्रीय सामाजिक सम्मेलन (1887) की शुरुआत की", "type": "leaf"}]},
            {"label": "न्यायिक और शैक्षणिक योगदान", "type": "branch", "date": "विरासत", "children": [
                {"label": "बॉम्बे हाई कोर्ट के न्यायाधीश; गोपाल कृष्ण गोखले और बाल गंगाधर तिलक के राजनीतिक गुरु", "type": "leaf"},
                {"label": "स्वदेशी अर्थव्यवस्था, औद्योगीकरण और विधवा पुनर्विवाह (विधवा विवाह संघ, 1861) का समर्थन किया", "type": "leaf"}]}
        ]
    },
    "pandita-ramabai": {
        "en": [
            {"label": "Education & Shelters", "type": "branch", "date": "Institutions", "children": [
                {"label": "Arya Mahila Samaj (1882) founded in Pune to promote women's education", "type": "leaf"},
                {"label": "Sharada Sadan (1889): Home/school for young Hindu widows in Bombay", "type": "leaf"},
                {"label": "Mukti Mission (Kedgaon): Sanctuary for young widows and abandoned girls", "type": "leaf"}]},
            {"label": "Titles & Books", "type": "branch", "date": "Achievements", "children": [
                {"label": "Title 'Pandita' and 'Sarasvati' awarded by Calcutta University for Sanskrit scholarship", "type": "leaf"},
                {"label": "Book: The High-Caste Hindu Woman (1887) highlighting plight of child widows", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "शिक्षा और आश्रय गृह", "type": "branch", "date": "संस्थान", "children": [
                {"label": "महिला शिक्षा के प्रसार हेतु पुणे में आर्य महिला समाज (1882) की स्थापना की", "type": "leaf"},
                {"label": "शारदा सदन (1889): बॉम्बे में युवा हिंदू विधवाओं के लिए स्कूल और आवासीय गृह", "type": "leaf"},
                {"label": "मुक्ति मिशन (केडगाँव): बेसहारा लड़कियों और युवा विधवाओं के लिए पुनर्वास केंद्र", "type": "leaf"}]},
            {"label": "उपाधियाँ और पुस्तकें", "type": "branch", "date": "उपलब्धियां", "children": [
                {"label": "कलकत्ता विश्वविद्यालय द्वारा संस्कृत विद्वता हेतु 'पंडिता' और 'सरस्वती' की उपाधि प्रदान की गई", "type": "leaf"},
                {"label": "पुस्तक: द हाई-कास्ट हिंदू वुमन (1887) जिसमें बाल विधवाओं के शोषण का चित्रण किया गया", "type": "leaf"}]}
        ]
    },
    "annie-besanttheosophical-society": {
        "en": [
            {"label": "Theosophical Society", "type": "branch", "date": "1847-1933", "children": [
                {"label": "Founded in New York (1875) by Madame Blavatsky and Colonel Olcott", "type": "leaf"},
                {"label": "Besant joined in 1889; shifted headquarters to Adyar near Madras (1882)", "type": "leaf"},
                {"label": "Preached ancient religions (Hinduism, Buddhism, Zoroastrianism) as source of occult truth", "type": "leaf"}]},
            {"label": "Besant's Institutions", "type": "branch", "date": "Education", "children": [
                {"label": "Established Central Hindu College at Varanasi (1898); later became BHU (1916) with Malaviya", "type": "leaf"}]},
            {"label": "Home Rule & Congress", "type": "branch", "date": "Politics", "children": [
                {"label": "Home Rule League (1916) launched along with Tilak; Journals: New India & Commonweal", "type": "leaf"},
                {"label": "First woman President of Indian National Congress (Calcutta Session, 1917)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "थियोसोफिकल सोसाइटी", "type": "branch", "date": "1847-1933", "children": [
                {"label": "मैडम ब्लावत्स्की और कर्नल ओलकोट द्वारा न्यूयॉर्क में स्थापना (1875)", "type": "leaf"},
                {"label": "एनी बेसेंट 1889 में शामिल हुईं; मुख्यालय अड्यार (मद्रास के पास) स्थानांतरित किया गया (1882)", "type": "leaf"},
                {"label": "प्राचीन धर्मों (हिंदू, बौद्ध, पारसी) को दिव्य सत्यों का मुख्य स्रोत बताया", "type": "leaf"}]},
            {"label": "बेसेंट के संस्थान", "type": "branch", "date": "शिक्षा", "children": [
                {"label": "वाराणसी में सेंट्रल हिंदू कॉलेज (1898) की स्थापना; मदन मोहन मालवीय के सहयोग से बीएचयू (1916) बना", "type": "leaf"}]},
            {"label": "होम रूल और कांग्रेस", "type": "branch", "date": "राजनीति", "children": [
                {"label": "तिलक के साथ होम रूल लीग (1916) शुरू की; पत्रिकाएँ: न्यू इंडिया और कॉमनवील", "type": "leaf"},
                {"label": "भारतीय राष्ट्रीय कांग्रेस की प्रथम महिला अध्यक्ष बनीं (कलकत्ता अधिवेशन, 1917)", "type": "leaf"}]}
        ]
    },
    "sarojini-naidu": {
        "en": [
            {"label": "Political Career", "type": "branch", "date": "1879-1949", "children": [
                {"label": "First Indian woman President of Indian National Congress (Cawnpore Session, 1925)", "type": "leaf"},
                {"label": "Led Salt Satyagraha at Dharasana Salt Works (1930) after Gandhi's arrest", "type": "leaf"},
                {"label": "First woman Governor of United Provinces (modern Uttar Pradesh) in independent India", "type": "leaf"}]},
            {"label": "Poetry & Titles", "type": "branch", "date": "Literary", "children": [
                {"label": "Known as the 'Nightingale of India' (Bharat Kokila) for her lyrical poetry", "type": "leaf"},
                {"label": "Poetry books: The Golden Threshold (1905), The Feather of the Dawn", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "राजनीतिक करियर", "type": "branch", "date": "1879-1949", "children": [
                {"label": "भारतीय राष्ट्रीय कांग्रेस की प्रथम भारतीय महिला अध्यक्ष (कानपुर अधिवेशन, 1925)", "type": "leaf"},
                {"label": "गांधीजी की गिरफ्तारी के बाद धरासणा नमक सत्याग्रह (1930) का कुशल नेतृत्व किया", "type": "leaf"},
                {"label": "स्वतंत्र भारत में संयुक्त प्रांत (आधुनिक उत्तर प्रदेश) की प्रथम महिला राज्यपाल बनीं", "type": "leaf"}]},
            {"label": "काव्य और उपाधियाँ", "type": "branch", "date": "साहित्यिक", "children": [
                {"label": "अपनी सुरीली कविताओं के लिए 'भारत कोकिला' (नाइटिंगेल ऑफ इंडिया) के रूप में प्रसिद्ध", "type": "leaf"},
                {"label": "काव्य संग्रह: द गोल्डन थ्रेशहोल्ड (1905), द फेदर ऑफ द डॉन", "type": "leaf"}]}
        ]
    },
    "sri-ramakrishna-paramahamsa": {
        "en": [
            {"label": "Teachings", "type": "branch", "date": "1836-1886", "children": [
                {"label": "Priest at Dakshineswar Kali Temple; preached unity of all religions (Sada Dharma)", "type": "leaf"},
                {"label": "Advocated direct spiritual experience over rituals and dogmas", "type": "leaf"},
                {"label": "Motto: 'Service to man is service to God' (Jiva is Shiva)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "उपदेश और दर्शन", "type": "branch", "date": "1836-1886", "children": [
                {"label": "दक्षिणेश्वर काली मंदिर के पुजारी; सभी धर्मों की एकता और सत्यता का प्रचार किया", "type": "leaf"},
                {"label": "शास्त्रों और कर्मकांडों के ऊपर प्रत्यक्ष आध्यात्मिक अनुभूति को सर्वोपरि माना", "type": "leaf"},
                {"label": "सिद्धांत: 'मानव सेवा ही माधव सेवा है' (शिव भाव से जीव सेवा)", "type": "leaf"}]}
        ]
    },
    "syed-ahmad-khan": {
        "en": [
            {"label": "Aligarh Movement", "type": "branch", "date": "1817-1898", "children": [
                {"label": "Founded Mohammedan Anglo-Oriental College (1875) at Aligarh; later Aligarh Muslim University", "type": "leaf"},
                {"label": "Advocated western scientific education & social reforms among Muslims", "type": "leaf"}]},
            {"label": "Journals & Societies", "type": "branch", "date": "Reforms", "children": [
                {"label": "Tahzib-ul-Akhlaq (Social Reformer journal) in Urdu; Scientific Society (1864)", "type": "leaf"},
                {"label": "Opposed purdah system, polygamy, and advocated women's education", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "अलीगढ़ आंदोलन", "type": "branch", "date": "1817-1898", "children": [
                {"label": "अलीगढ़ में मोहम्मडन एंग्लो-ओरिएंटल कॉलेज (1875) की स्थापना की; जो बाद में अलीगढ़ मुस्लिम विश्वविद्यालय बना", "type": "leaf"},
                {"label": "मुसलमानों में पश्चिमी वैज्ञानिक शिक्षा और सामाजिक सुधारों के कट्टर पक्षधर थे", "type": "leaf"}]},
            {"label": "पत्रिकाएँ और समितियाँ", "type": "branch", "date": "सुधार", "children": [
                {"label": "उर्दू में तहज़ीब-उल-अख़लाक़ (सभ्यता और नैतिकता) पत्रिका; साइंटिफिक सोसाइटी (1864)", "type": "leaf"},
                {"label": "पर्दा प्रथा, बहुविवाह का विरोध किया तथा स्त्री शिक्षा का दृढ़ समर्थन किया", "type": "leaf"}]}
        ]
    },
    "baba-dayal-das": {
        "en": [
            {"label": "Nirankari Movement", "type": "branch", "date": "Sikh Reform", "children": [
                {"label": "Founded Nirankari Movement (1840s) within Sikhism to remove non-Sikh rituals", "type": "leaf"},
                {"label": "Emphasized worship of 'Nirankar' (the formless God); opposed idol worship & empty rituals", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "निरंकारी आंदोलन", "type": "branch", "date": "सिख सुधार", "children": [
                {"label": "सिख धर्म में सुधार और ब्राह्मणी कर्मकांडों को हटाने हेतु निरंकारी आंदोलन (1840 के दशक) की शुरुआत की", "type": "leaf"},
                {"label": "निराकार (अकाल पुरख) की आराधना पर बल दिया; मूर्ति पूजा और अंधविश्वासों का पुरजोर विरोध किया", "type": "leaf"}]}
        ]
    },
    "aspects-of-women-emancipation-education": {
        "en": [
            {"label": "Pioneering Efforts", "type": "branch", "date": "Schools", "children": [
                {"label": "Christian Missionaries established first girls' schools in 1810s-20s", "type": "leaf"},
                {"label": "Bethune School (1849) by JED Bethune in Calcutta was landmark for secular female education", "type": "leaf"}]},
            {"label": "Official Policies", "type": "branch", "date": "Acts", "children": [
                {"label": "Wood's Despatch (1854) gave first official state grant/support for female education", "type": "leaf"},
                {"label": "Hunter Commission (1882) recommended liberal grants-in-aid & teacher training for girls' schools", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "शुरुआती प्रयास", "type": "branch", "date": "स्कूल", "children": [
                {"label": "ईसाई मिशनरियों ने 1810 और 1820 के दशक में पहले बालिका विद्यालयों की स्थापना की", "type": "leaf"},
                {"label": "कलकत्ता में जे.ई.डी. बेथून द्वारा स्थापित बेथून स्कूल (1849) धर्मनिरपेक्ष महिला शिक्षा का मील का पत्थर था", "type": "leaf"}]},
            {"label": "सरकारी नीतियां", "type": "branch", "date": "अधिनियम", "children": [
                {"label": "वुड्स डिस्पैच (1854) ने महिला शिक्षा के लिए पहली बार सरकारी अनुदान और सहायता को मंजूरी दी", "type": "leaf"},
                {"label": "हंटर आयोग (1882) ने बालिका विद्यालयों के लिए उदार अनुदान और शिक्षिका प्रशिक्षण की सिफारिश की", "type": "leaf"}]}
        ]
    },
    "aspects-of-women-emancipation-widow-remarriage": {
        "en": [
            {"label": "Legal Reforms", "type": "branch", "date": "Acts", "children": [
                {"label": "Hindu Widow Remarriage Act XV (1856) legalized remarriages; championed by Vidyasagar", "type": "leaf"},
                {"label": "Lord Canning signed the act into law (drafted by Lord Dalhousie)", "type": "leaf"}]},
            {"label": "Key Activists", "type": "branch", "date": "Leaders", "children": [
                {"label": "DK Karve: Opened Hindu Widow's Home in Pune (1896); established Indian Women's University (1916)", "type": "leaf"},
                {"label": "Vishnushastri Pandit: Founded Widow Marriage Association (1866) in Maharashtra", "type": "leaf"},
                {"label": "Veerasalingam Pantulu: Led widow remarriage movement in South India (Andhra)", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "कानूनी सुधार", "type": "branch", "date": "अधिनियम", "children": [
                {"label": "हिंदू विधवा पुनर्विवाह अधिनियम XV (1856) द्वारा पुनर्विवाह को वैध बनाया गया (विद्यासागर का मुख्य योगदान)", "type": "leaf"},
                {"label": "लॉर्ड कैनिंग ने इस अधिनियम पर हस्ताक्षर कर इसे कानून बनाया (लॉर्ड डलहौजी द्वारा तैयार प्रारूप)", "type": "leaf"}]},
            {"label": "प्रमुख कार्यकर्ता", "type": "branch", "date": "नेता", "children": [
                {"label": "डी.के. कर्वे: पुणे में अनाथ बालिका आश्रम (1896) खोला; 1916 में प्रथम महिला विश्वविद्यालय की स्थापना की", "type": "leaf"},
                {"label": "विष्णुशास्त्री पंडित: महाराष्ट्र में विधवा विवाह संघ (1866) की स्थापना की", "type": "leaf"},
                {"label": "वीरेशलिंगम पंतुलु: दक्षिण भारत (आंध्र प्रदेश) में विधवा पुनर्विवाह आंदोलन का नेतृत्व किया", "type": "leaf"}]}
        ]
    },
    "aspects-of-women-emancipation-legislation-and-women-organisation": {
        "en": [
            {"label": "Major Legislations", "type": "branch", "date": "Acts", "children": [
                {"label": "Sati Prohibition Regulation XVII (1829) under William Bentinck", "type": "leaf"},
                {"label": "Female Infanticide Prevention Act (1870)", "type": "leaf"},
                {"label": "Age of Consent Act (1891): Raised girl's marriage age to 12 (due to Behramji Malabari)", "type": "leaf"},
                {"label": "Sarda Act / Child Marriage Restraint Act (1929): Min. age 14 for girls & 18 for boys", "type": "leaf"}]},
            {"label": "Early Organisations", "type": "branch", "date": "Groups", "children": [
                {"label": "Bharat Stree Mahamandal (1910) at Allahabad by Sarala Devi Chaudhurani (first national body)", "type": "leaf"},
                {"label": "Women's Indian Association (WIA, 1917) by Annie Besant, Dorothy Jinarajadasa, Margaret Cousins", "type": "leaf"},
                {"label": "All India Women's Conference (AIWC, 1927) founded by Margaret Cousins", "type": "leaf"}]}
        ],
        "hi": [
            {"label": "प्रमुख कानून", "type": "branch", "date": "अधिनियम", "children": [
                {"label": "विलियम बेंटिक के समय सती प्रथा निषेध नियमन XVII (1829) पारित किया गया", "type": "leaf"},
                {"label": "कन्या शिशु हत्या रोकथाम अधिनियम (1870)", "type": "leaf"},
                {"label": "एज ऑफ कंसेंट एक्ट (1891): बहरामजी मालाबारी के प्रयासों से लड़की के विवाह की न्यूनतम आयु 12 वर्ष की गई", "type": "leaf"},
                {"label": "शारदा अधिनियम (1929): विवाह की न्यूनतम आयु लड़की हेतु 14 वर्ष और लड़के हेतु 18 वर्ष निर्धारित", "type": "leaf"}]},
            {"label": "महिला संगठन", "type": "branch", "date": "समूह", "children": [
                {"label": "भारत स्त्री महामंडल (1910, इलाहाबाद): सरला देवी चौधुरानी द्वारा स्थापित (पहला राष्ट्रीय महिला संगठन)", "type": "leaf"},
                {"label": "विमेंस इंडियन एसोसिएशन (WIA, 1917): एनी बेसेंट, मार्गरेट कजिन्स और डोरोथी जीनराजदास द्वारा स्थापित", "type": "leaf"},
                {"label": "अखिल भारतीय महिला सम्मेलन (AIWC, 1927): मार्गरेट कजिन्स द्वारा स्थापित", "type": "leaf"}]}
        ]
    }
}

# Mapping folder variations to canonical keys
MINDMAP_MAPPINGS = {
    "annie-besanttheosophical-society": "annie-besanttheosophical-society",
    "aspects-of-women-emancipation-education": "aspects-of-women-emancipation-education",
    "aspects-of-women-emancipation-legislation-and-women-organisation": "aspects-of-women-emancipation-legislation-and-women-organisation",
    "aspects-of-women-emancipation-widow-remarriage": "aspects-of-women-emancipation-widow-remarriage",
    "baba-dayal-das": "baba-dayal-das",
    "dr-bhimrao-ramji-ambedkar": "dr-bhimrao-ramji-ambedkar",
    "ishwar-chandra-vidyasagar": "ishwar-chandra-vidyasagar",
    "jyotiba-phule": "jyotiba-phule",
    "keshab-chandra-sen": "keshab-chandra-sen",
    "mahadev-govind-ranade": "mahadev-govind-ranade",
    "pandita-ramabai": "pandita-ramabai",
    "raja-ram-mohan-roy": "raja-ram-mohan-roy",
    "sarojini-naidu": "sarojini-naidu",
    "sri-ramakrishna-paramahamsa": "sri-ramakrishna-paramahamsa",
    "swami-dayananda-saraswati": "swami-dayananda-saraswati",
    "swami-vivekananda": "swami-vivekananda",
    "syed-ahmad-khan": "syed-ahmad-khan"
}

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    title = title.replace('Theosophical', ' & Theosophical')
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
    canonical_key = MINDMAP_MAPPINGS.get(key, key)
    
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
