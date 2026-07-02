#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import json

BASE = r"upsc/geography/Biogeography"

def get_clean_title(folder_name):
    title = folder_name.replace('-', ' ')
    skip = {'of', 'and', 'the', 'for', 'in', 'with', 'to', 'on', 'by', 'or', 'its', 'a', 'an'}
    return ' '.join(w if w.lower() in skip else w.capitalize() for w in title.split())

def get_custom_branches(folder_name, is_hindi):
    fl = folder_name.lower()

    # 1. Afforestation
    if fl == 'afforestation':
        if is_hindi:
            return [
                {"label": "वनरोपण: परिभाषा और उद्देश्य", "type": "branch", "date": "परिभाषा", "children": [
                    {"label": "परिभाषा: उन क्षेत्रों में वन लगाना जहाँ पहले कभी वन नहीं थे (Reforestation से अलग)", "type": "leaf"},
                    {"label": "NFAP: राष्ट्रीय वनारोपण कार्यक्रम; CAMPA (Compensatory Afforestation Fund); 2016 अधिनियम", "type": "leaf"},
                    {"label": "लक्ष्य: भारत का लक्ष्य 2030 तक 33% भूमि पर वन/वृक्ष आवरण; NDC प्रतिबद्धता 2.5-3 अरब टन CO₂ अवशोषण", "type": "leaf"}
                ]},
                {"label": "प्रमुख वनरोपण कार्यक्रम और योजनाएँ", "type": "branch", "date": "योजनाएँ", "children": [
                    {"label": "ग्रीन इंडिया मिशन: NAPCC के 8 मिशनों में एक; 5 मिलियन हेक्टेयर वन बढ़ाना/सुधारना", "type": "leaf"},
                    {"label": "CAMPA: Compensatory Afforestation Fund Management & Planning Authority; वन भूमि के बदले धन", "type": "leaf"},
                    {"label": "नमामि गंगे: गंगा के किनारे 30,000 हेक्टेयर में वनरोपण; 'वन गंगा' अभियान", "type": "leaf"},
                    {"label": "सामाजिक वानिकी: किसानों को उनकी बंजर भूमि पर वृक्षारोपण के लिए प्रोत्साहन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Afforestation: Definition & Goals", "type": "branch", "date": "Definition", "children": [
                    {"label": "Afforestation = planting trees on land that previously had NO forest cover (distinct from reforestation)", "type": "leaf"},
                    {"label": "CAMPA (2016): Compensatory Afforestation Fund Management & Planning Authority for forest diversion funds", "type": "leaf"},
                    {"label": "India's NDC Goal: 33% green cover target; absorb 2.5-3 billion tonnes CO₂ by 2030 through forests", "type": "leaf"}
                ]},
                {"label": "Key Afforestation Programmes", "type": "branch", "date": "Schemes", "children": [
                    {"label": "Green India Mission: One of NAPCC's 8 missions; restore/enhance 5 million hectares of forest", "type": "leaf"},
                    {"label": "CAMPA Funds: States receive compensatory funds when forest land is diverted for non-forest use", "type": "leaf"},
                    {"label": "Namami Gange: 30,000 ha afforestation along Ganga banks; 'Van Ganga' component", "type": "leaf"},
                    {"label": "Social Forestry: Encouraging farmers to plant trees on degraded and private wastelands", "type": "leaf"}
                ]}
            ]

    # 2. Deforestation
    elif fl == 'deforestation':
        if is_hindi:
            return [
                {"label": "वनों की कटाई: कारण", "type": "branch", "date": "कारण", "children": [
                    {"label": "कृषि विस्तार: स्थानांतरित खेती (Jhum/Slash-and-Burn), वाणिज्यिक खेती के लिए वन भूमि का रूपांतरण", "type": "leaf"},
                    {"label": "बुनियादी ढांचा: सड़कें, बाँध, खनन परियोजनाएँ; उदा. नर्मदा बाँध, अटल टनल", "type": "leaf"},
                    {"label": "जनसंख्या दबाव: ईंधन लकड़ी और चारे की माँग; अनधिकृत अतिक्रमण", "type": "leaf"},
                    {"label": "वाणिज्यिक लकड़ी: अवैध कटाई (Illegal Logging); कागज उद्योग के लिए लुगदी (Pulpwood)", "type": "leaf"}
                ]},
                {"label": "प्रभाव और भारतीय संदर्भ", "type": "branch", "date": "प्रभाव", "children": [
                    {"label": "जलवायु प्रभाव: कार्बन अवशोषण में कमी; स्थानीय वर्षा पैटर्न में बदलाव; ताप द्वीप प्रभाव", "type": "leaf"},
                    {"label": "जैव विविधता हानि: प्रजातियों के आवास का विनाश; भारत में 5% प्रजातियाँ लुप्तप्राय", "type": "leaf"},
                    {"label": "FSI रिपोर्ट 2021: भारत का वन आवरण 7,13,789 वर्ग किमी (21.71%); लक्ष्य 33% से बहुत कम", "type": "leaf"},
                    {"label": "मृदा क्षरण: जड़ों की अनुपस्थिति से भूमि कटाव, भूस्खलन, बाढ़ की बढ़ती आवृत्ति", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Deforestation: Causes", "type": "branch", "date": "Causes", "children": [
                    {"label": "Agricultural Expansion: Jhum cultivation (slash-and-burn), commercial plantation replacing forests", "type": "leaf"},
                    {"label": "Infrastructure: Roads, dams, mining; e.g., Narmada Dam, railway expansion through forests", "type": "leaf"},
                    {"label": "Population Pressure: Fuelwood demand, fodder collection, unauthorized encroachment on forest land", "type": "leaf"},
                    {"label": "Commercial Logging: Illegal logging for timber; pulpwood for paper industry", "type": "leaf"}
                ]},
                {"label": "Impacts & Indian Context", "type": "branch", "date": "Impacts", "children": [
                    {"label": "Climate Impact: Reduced carbon sink; altered local rainfall; urban heat island intensification", "type": "leaf"},
                    {"label": "Biodiversity Loss: Habitat destruction; ~5% Indian species threatened; IUCN Red List concerns", "type": "leaf"},
                    {"label": "FSI Report 2021: India's forest cover = 7,13,789 sq km (21.71%); far below the 33% target", "type": "leaf"},
                    {"label": "Soil Degradation: Loss of root systems causes erosion, landslides, flash flooding frequency", "type": "leaf"}
                ]}
            ]

    # 3. Factors Responsible for Soil Formation
    elif 'factors' in fl and 'soil' in fl:
        if is_hindi:
            return [
                {"label": "मृदा निर्माण के कारक (CLORPT मॉडल)", "type": "branch", "date": "5 कारक", "children": [
                    {"label": "जलवायु (C): सर्वाधिक प्रभावशाली; तापमान और वर्षा; उष्णकटिबंधीय में तेज़ अपक्षय, ध्रुवीय क्षेत्रों में धीमा", "type": "leaf"},
                    {"label": "जीव (O): पौधे, पशु और सूक्ष्मजीव; ह्यूमस निर्माण; केंचुए — 'मृदा के इंजीनियर'", "type": "leaf"},
                    {"label": "मूल शैल (R): जनक सामग्री; ग्रेनाइट से बालुई मृदा; बेसाल्ट से काली मृदा (रेगुर)", "type": "leaf"},
                    {"label": "स्थलाकृति (R): ढाल; पहाड़ी क्षेत्रों में पतली मृदा; मैदानों में गहरी जलोढ़ मृदा", "type": "leaf"},
                    {"label": "समय (T): पुरानी मृदा अधिक विकसित; परिपक्व मृदा में स्पष्ट क्षितिज (Horizons)", "type": "leaf"}
                ]},
                {"label": "भारत में मृदा निर्माण पर प्रभाव", "type": "branch", "date": "भारतीय संदर्भ", "children": [
                    {"label": "दक्षिणी पठार: बेसाल्ट से निर्मित रेगुर (काली) मृदा; कपास की खेती के लिए आदर्श", "type": "leaf"},
                    {"label": "इंडो-गंगेटिक मैदान: हिमालय से लाई गई जलोढ़; बहुत उपजाऊ; खरीफ और रबी दोनों फसलें", "type": "leaf"},
                    {"label": "लेटेराइट (पश्चिमी घाट): भारी वर्षा और उच्च तापमान; Fe-Al ऑक्साइड से भरपूर; अम्लीय", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Factors of Soil Formation (CLORPT Model)", "type": "branch", "date": "5 Factors", "children": [
                    {"label": "Climate (C): Most dominant factor; temperature + rainfall determine weathering rate and organic matter", "type": "leaf"},
                    {"label": "Organisms (O): Plants, fauna and microbes; humus formation; earthworms as 'soil engineers'", "type": "leaf"},
                    {"label": "Parent Material (R): Granite → sandy soil; Basalt → Black (Regur) soil; Limestone → calcareous soil", "type": "leaf"},
                    {"label": "Relief/Topography (R): Steep slopes = thin soils; plains = deep alluvial soils with better water retention", "type": "leaf"},
                    {"label": "Time (T): Older soils = more developed horizons; mature soils show clear A-B-C horizon profile", "type": "leaf"}
                ]},
                {"label": "Soil Formation in Indian Context", "type": "branch", "date": "India Context", "children": [
                    {"label": "Deccan Plateau: Basalt → Regur (Black soil); moisture-retentive; ideal for rainfed cotton cultivation", "type": "leaf"},
                    {"label": "Indo-Gangetic Plain: Himalayan alluvium; highly fertile; supports rabi and kharif crops", "type": "leaf"},
                    {"label": "Laterite (Western Ghats): Heavy rainfall + high temp → Fe-Al oxide-rich; acidic; poor nutrients", "type": "leaf"}
                ]}
            ]

    # 4. Forests its Various Aspects
    elif 'forests' in fl:
        if is_hindi:
            return [
                {"label": "वन: प्रकार और वर्गीकरण", "type": "branch", "date": "भारतीय वन", "children": [
                    {"label": "उष्णकटिबंधीय सदाबहार: 200+ सेमी वर्षा; पश्चिमी घाट, A&N द्वीप; तीन-स्तरीय छत्र; रोसवुड, महोगनी", "type": "leaf"},
                    {"label": "उष्णकटिबंधीय पर्णपाती: 100-200 सेमी; MP, UP, महाराष्ट्र; सागवान, साल; 'मानसून वन'", "type": "leaf"},
                    {"label": "उष्णकटिबंधीय कंटीले: 50-100 सेमी; राजस्थान, गुजरात; बबूल, खेजड़ी; सूखा प्रतिरोधी", "type": "leaf"},
                    {"label": "पर्वतीय वन: शीतोष्ण; हिमाचल-उत्तराखंड; देवदार, चीड़, बुराँश; 1500-3000 मीटर", "type": "leaf"},
                    {"label": "मैंग्रोव: तटीय/ज्वारीय; सुंदरबन, भितरकनिका, पिचावरम; सुंदरी वृक्ष", "type": "leaf"}
                ]},
                {"label": "वनों के कार्य और महत्व", "type": "branch", "date": "महत्व", "children": [
                    {"label": "पारिस्थितिक: CO₂ अवशोषण, O₂ उत्सर्जन, जल चक्र, जैव विविधता आवास", "type": "leaf"},
                    {"label": "आर्थिक: लकड़ी, औषधीय पौधे, NTFP (Non-Timber Forest Products); वन आधारित आजीविका", "type": "leaf"},
                    {"label": "सामाजिक: आदिवासी समुदायों की आजीविका; वन अधिकार अधिनियम 2006 का महत्व", "type": "leaf"},
                    {"label": "भारत वन स्थिति रिपोर्ट (FSI 2021): 7.13 लाख वर्ग किमी वन; 21.71% भौगोलिक क्षेत्र", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Forests: Types & Classification", "type": "branch", "date": "Indian Forests", "children": [
                    {"label": "Tropical Evergreen: 200+ cm rainfall; Western Ghats, A&N Islands; three-tiered canopy; Rosewood, Ebony", "type": "leaf"},
                    {"label": "Tropical Deciduous: 100-200 cm; MP, UP, Maharashtra; Teak, Sal; called 'Monsoon Forests'", "type": "leaf"},
                    {"label": "Tropical Thorny: 50-100 cm; Rajasthan, Gujarat; Acacia, Khejri; deep-rooted drought-adapted", "type": "leaf"},
                    {"label": "Montane Forests: Temperate; HP-Uttarakhand; Deodar, Chir Pine, Rhododendron; 1500-3000m", "type": "leaf"},
                    {"label": "Mangroves: Tidal/Coastal; Sundarbans, Bhitarkanika, Pichavaram; Sundari tree; salt-tolerant", "type": "leaf"}
                ]},
                {"label": "Functions & Importance of Forests", "type": "branch", "date": "Importance", "children": [
                    {"label": "Ecological: CO₂ sink, O₂ production, water cycle regulation, biodiversity habitat", "type": "leaf"},
                    {"label": "Economic: Timber, medicinal plants, NTFPs (Non-Timber Forest Products); livelihoods", "type": "leaf"},
                    {"label": "Social: Tribal livelihoods; Forest Rights Act 2006; recognition of community rights over forests", "type": "leaf"},
                    {"label": "FSI 2021: India's forest = 7.13 lakh sq km = 21.71% of geographical area", "type": "leaf"}
                ]}
            ]

    # 5. Monoculture Plantation
    elif 'monoculture' in fl:
        if is_hindi:
            return [
                {"label": "एकल-संस्कृति वृक्षारोपण: परिभाषा", "type": "branch", "date": "परिभाषा", "children": [
                    {"label": "एक बड़े क्षेत्र में केवल एक प्रजाति के पेड़ लगाना; उदा: नीलगिरि (Eucalyptus), अकेशिया, रबर, तेल पाम", "type": "leaf"},
                    {"label": "वाणिज्यिक उद्देश्य: कागज उद्योग, रबर, बायोफ्यूल, लकड़ी के लिए बड़े पैमाने पर रोपण", "type": "leaf"}
                ]},
                {"label": "समस्याएँ और विवाद", "type": "branch", "date": "समस्याएँ", "children": [
                    {"label": "जल अवशोषण: नीलगिरि (Eucalyptus) अत्यधिक जल शोषण करता है; भूजल स्तर गिरता है", "type": "leaf"},
                    {"label": "जैव विविधता हानि: केवल एक प्रजाति से पक्षी, कीट और अन्य वनस्पतियाँ नष्ट होती हैं", "type": "leaf"},
                    {"label": "मृदा अम्लता: कुछ प्रजातियाँ (नीलगिरि) मृदा को अम्लीय बनाती हैं; अन्य पौधों के लिए हानिकारक", "type": "leaf"},
                    {"label": "विकल्प: मिश्रित वृक्षारोपण (Agroforestry); देशज प्रजातियों का उपयोग; बहु-स्तरीय वन", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Monoculture Plantation: Definition", "type": "branch", "date": "Definition", "children": [
                    {"label": "Growing a single tree species over a large area; examples: Eucalyptus, Acacia, Rubber, Oil Palm", "type": "leaf"},
                    {"label": "Commercial purpose: Paper pulp industry, rubber, biofuel, timber supply in shortest time", "type": "leaf"}
                ]},
                {"label": "Problems & Controversies", "type": "branch", "date": "Problems", "children": [
                    {"label": "Water Depletion: Eucalyptus extracts massive groundwater; called 'ecological thirsty tree'", "type": "leaf"},
                    {"label": "Biodiversity Loss: Single species = no habitat for birds, insects, native understory plants", "type": "leaf"},
                    {"label": "Soil Acidification: Some species (Eucalyptus) acidify soil; allelopathic chemicals suppress other plants", "type": "leaf"},
                    {"label": "Alternative: Mixed/Agroforestry; use of indigenous species; multi-tiered plantation systems", "type": "leaf"}
                ]}
            ]

    # 6. Reforestation
    elif fl == 'reforestation':
        if is_hindi:
            return [
                {"label": "पुनर्वनीकरण: परिभाषा और अंतर", "type": "branch", "date": "परिभाषा", "children": [
                    {"label": "परिभाषा: उन क्षेत्रों में वन पुनः लगाना जहाँ पहले वन थे लेकिन कट/नष्ट हो गए (Afforestation से अलग)", "type": "leaf"},
                    {"label": "प्राकृतिक पुनर्जनन (Natural Regeneration): वनों को प्राकृतिक रूप से उगने देना; खर्चीला लेकिन अधिक टिकाऊ", "type": "leaf"}
                ]},
                {"label": "प्रमुख कार्यक्रम और सफलता की कहानियाँ", "type": "branch", "date": "कार्यक्रम", "children": [
                    {"label": "CAMPA: Compensatory Afforestation; नष्ट वनों के बदले नए वन उगाने का अनिवार्य प्रावधान", "type": "leaf"},
                    {"label": "राजस्थान: अरावली की पहाड़ियों में पुनर्वनीकरण; मरुस्थलीकरण को रोकने में सफलता", "type": "leaf"},
                    {"label": "उत्तर-पूर्व भारत: जलग्रहण क्षेत्रों में पुनर्वनीकरण; भूस्खलन और बाढ़ नियंत्रण", "type": "leaf"},
                    {"label": "वायुमंडलीय लाभ: प्रत्येक हेक्टेयर वन प्रतिवर्ष लगभग 5-20 टन CO₂ अवशोषित करता है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Reforestation: Definition & Distinction", "type": "branch", "date": "Definition", "children": [
                    {"label": "Re-planting forests where they previously existed but were cleared (distinct from afforestation)", "type": "leaf"},
                    {"label": "Natural Regeneration: Allowing forests to regrow naturally; low-cost but requires decades", "type": "leaf"}
                ]},
                {"label": "Key Programmes & Success Stories", "type": "branch", "date": "Programmes", "children": [
                    {"label": "CAMPA: Compensatory Afforestation fund mandates reforestation when forests are diverted", "type": "leaf"},
                    {"label": "Aravalli, Rajasthan: Reforestation to check desertification; groundwater recharge benefit", "type": "leaf"},
                    {"label": "Northeast India: Watershed reforestation programs for landslide and flood control", "type": "leaf"},
                    {"label": "Carbon Benefit: Each reforested hectare absorbs ~5-20 tonnes of CO₂ per year", "type": "leaf"}
                ]}
            ]

    # 7. Soil Classification
    elif 'soil-classification' in fl:
        if is_hindi:
            return [
                {"label": "भारत में मृदा वर्गीकरण (ICAR आधारित)", "type": "branch", "date": "8 मृदा प्रकार", "children": [
                    {"label": "जलोढ़ मृदा: 43% भारत; उत्तर भारतीय मैदान; खादर (नई) और बांगर (पुरानी); बहुत उपजाऊ", "type": "leaf"},
                    {"label": "काली (रेगुर) मृदा: महाराष्ट्र, MP, Gujarat, AP; बेसाल्ट से निर्मित; स्वयं जुताई; कपास के लिए", "type": "leaf"},
                    {"label": "लाल और पीली मृदा: दक्षिण भारत; Fe₂O₃ (लौह ऑक्साइड) से लाल रंग; कम उपजाऊ", "type": "leaf"},
                    {"label": "लेटेराइट मृदा: पश्चिमी घाट, उत्तर-पूर्व; भारी वर्षा से निक्षालन; ईंट बनाने में उपयोग", "type": "leaf"},
                    {"label": "मरुस्थलीय मृदा: राजस्थान; बालुई; कम जीवांश; सिंचाई से उपजाऊ बनाई जा सकती है", "type": "leaf"},
                    {"label": "पर्वतीय/वन मृदा: हिमालय; कार्बनिक पदार्थ से भरपूर; ऊपरी ढलानों पर पतली", "type": "leaf"}
                ]},
                {"label": "USDA टेक्सचर वर्गीकरण", "type": "branch", "date": "वैज्ञानिक वर्गीकरण", "children": [
                    {"label": "बालुई (Sandy): 70%+ रेत; तीव्र जल निकासी; कम जल धारण क्षमता; Rajasthan", "type": "leaf"},
                    {"label": "चिकनी (Clay): 40%+ मृत्तिका; उच्च जल धारण; संकुचन-सूजन; रेगुर इसी श्रेणी में", "type": "leaf"},
                    {"label": "दोमट (Loam): रेत, मृत्तिका, गाद का आदर्श मिश्रण; सर्वोत्तम कृषि मृदा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Soil Classification in India (ICAR-based)", "type": "branch", "date": "8 Soil Types", "children": [
                    {"label": "Alluvial Soil: 43% of India; North Indian plains; Khadar (new) vs Bhangar (old); very fertile", "type": "leaf"},
                    {"label": "Black (Regur) Soil: Maharashtra, MP, Gujarat, AP; from Basalt; self-ploughing; ideal for cotton", "type": "leaf"},
                    {"label": "Red & Yellow Soil: South India; Fe₂O₃ gives red color; relatively less fertile than alluvial", "type": "leaf"},
                    {"label": "Laterite Soil: Western Ghats, NE India; heavy leaching; used for brick-making; tea and coffee", "type": "leaf"},
                    {"label": "Desert Soil: Rajasthan; sandy; low humus; can be productive with irrigation (IGNP canal)", "type": "leaf"},
                    {"label": "Mountain/Forest Soil: Himalayas; rich in organic matter; thin on upper slopes; acidic", "type": "leaf"}
                ]},
                {"label": "USDA Textural Classification", "type": "branch", "date": "Scientific Classification", "children": [
                    {"label": "Sandy: 70%+ sand particles; rapid drainage; low water retention; Rajasthan desert soils", "type": "leaf"},
                    {"label": "Clay: 40%+ clay; high water retention; shrink-swell; Regur (Black soil) is clay-dominated", "type": "leaf"},
                    {"label": "Loam: Ideal sand-clay-silt mix; best agricultural soil; good drainage AND moisture retention", "type": "leaf"}
                ]}
            ]

    # 8. Soil Erosion and Conservation
    elif 'erosion' in fl:
        if is_hindi:
            return [
                {"label": "मृदा अपरदन: प्रकार और कारण", "type": "branch", "date": "प्रकार", "children": [
                    {"label": "परत अपरदन (Sheet Erosion): वर्षा से ऊपरी मृदा की पतली परत हटना; सर्वाधिक हानिकारक", "type": "leaf"},
                    {"label": "नालीदार अपरदन (Rill/Gully): छोटी-बड़ी नालियाँ; मध्यप्रदेश में 'उत्खात भूमि' (Ravines)", "type": "leaf"},
                    {"label": "पवन अपरदन (Wind Erosion): राजस्थान/गुजरात; रेत के टीले; बालू का प्रवाह", "type": "leaf"},
                    {"label": "चंबल घाटी: गहरी खड्डें; 4 मिलियन हेक्टेयर भूमि क्षरण; 'बीहड़'", "type": "leaf"}
                ]},
                {"label": "मृदा संरक्षण के उपाय", "type": "branch", "date": "संरक्षण", "children": [
                    {"label": "समोच्च जुताई (Contour Ploughing): ढाल के विपरीत जुताई; जल बहाव कम करना", "type": "leaf"},
                    {"label": "वेदिका खेती (Terrace Farming): पहाड़ी ढलानों पर सीढ़ीदार खेती; उत्तर-पूर्व भारत में प्रचलित", "type": "leaf"},
                    {"label": "विंडब्रेक (Shelter Belts): मरुस्थलीय क्षेत्रों में पेड़ों की पंक्तियाँ; राजस्थान में 'थार ग्रेट वॉल'", "type": "leaf"},
                    {"label": "चेक डैम: नालियों में छोटे बाँध; जल संचयन और मृदा संरक्षण; गुजरात मॉडल", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Soil Erosion: Types & Causes", "type": "branch", "date": "Types", "children": [
                    {"label": "Sheet Erosion: Thin layer of topsoil removed by rainwater; most damaging yet least visible", "type": "leaf"},
                    {"label": "Rill/Gully Erosion: Finger-like channels growing into deep ravines; Chambal Valley 'Badlands'", "type": "leaf"},
                    {"label": "Wind Erosion: Rajasthan/Gujarat deserts; sand dunes; loess deposition downwind", "type": "leaf"},
                    {"label": "Chambal Ravines: Deep gullies; ~4 million ha degraded land; 'Beehad' in Hindi", "type": "leaf"}
                ]},
                {"label": "Soil Conservation Measures", "type": "branch", "date": "Conservation", "children": [
                    {"label": "Contour Ploughing: Ploughing across the slope; reduces water runoff velocity significantly", "type": "leaf"},
                    {"label": "Terrace Farming: Step-like fields on hill slopes; practiced extensively in NE India", "type": "leaf"},
                    {"label": "Windbreaks/Shelter Belts: Rows of trees in desert areas; used in Rajasthan along IGNP", "type": "leaf"},
                    {"label": "Check Dams: Small barriers in gullies; water harvesting + sediment trapping; Gujarat model", "type": "leaf"}
                ]}
            ]

    # 9. Soil Forming Processes
    elif 'soil-forming-processes' in fl:
        if is_hindi:
            return [
                {"label": "मृदा निर्माण की प्रक्रियाएँ: मुख्य 4", "type": "branch", "date": "प्रक्रियाएँ", "children": [
                    {"label": "ह्यूमिफिकेशन (Humification): कार्बनिक पदार्थों का ह्यूमस में रूपांतरण; मृदा की उर्वरता बढ़ाता है", "type": "leaf"},
                    {"label": "खनिजीकरण (Mineralization): ह्यूमस का खनिज पोषक तत्वों में टूटना; पौधों के लिए उपयोगी", "type": "leaf"},
                    {"label": "रसायनिक अपक्षय (Chemical Weathering): जल-अपघटन, ऑक्सीकरण, कार्बोनेटीकरण; खनिजों का घुलना", "type": "leaf"},
                    {"label": "यांत्रिक अपक्षय (Physical Weathering): तापमान परिवर्तन, हिम क्रिया; शैलों का टूटना", "type": "leaf"}
                ]},
                {"label": "विशिष्ट मृदा निर्माण प्रक्रियाएँ", "type": "branch", "date": "विशिष्ट प्रक्रियाएँ", "children": [
                    {"label": "पॉडसोलाइजेशन: शंकुधारी वनों में; अम्लीय ह्यूमस; ऊपरी परत से Fe-Al का निक्षालन; ठंडी जलवायु", "type": "leaf"},
                    {"label": "लेटेराइजेशन: उष्णकटिबंधीय; भारी वर्षा; Si का निक्षालन; Fe-Al ऑक्साइड शेष रहते हैं", "type": "leaf"},
                    {"label": "कैल्सीफिकेशन: शुष्क क्षेत्रों में; Ca कार्बोनेट का संचय; राजस्थान की मृदाएँ", "type": "leaf"},
                    {"label": "ग्लेइजेशन: जलभराव वाली मृदाएँ; अवायवीय स्थितियाँ; Fe कम होकर नीले-ग्रे रंग की मृदा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Key Soil Forming Processes", "type": "branch", "date": "Main 4", "children": [
                    {"label": "Humification: Organic matter → humus conversion; improves soil fertility, structure and water retention", "type": "leaf"},
                    {"label": "Mineralization: Humus broken into mineral nutrients (N, P, K); made available to plants", "type": "leaf"},
                    {"label": "Chemical Weathering: Hydrolysis, oxidation, carbonation; minerals dissolved or transformed", "type": "leaf"},
                    {"label": "Physical Weathering: Temperature changes, frost action; rock broken into smaller fragments", "type": "leaf"}
                ]},
                {"label": "Specific Pedogenic Processes", "type": "branch", "date": "Specific", "children": [
                    {"label": "Podzolization: Coniferous forests; acidic humus leaches Fe-Al down profile; cold climate", "type": "leaf"},
                    {"label": "Laterization: Tropical; heavy rain leaches Si; Fe-Al oxides remain; red/laterite soils", "type": "leaf"},
                    {"label": "Calcification: Arid areas; CaCO₃ accumulates in B horizon; Rajasthan caliche soils", "type": "leaf"},
                    {"label": "Gleization: Waterlogged soils; anaerobic; Fe reduced → bluish-grey 'gley' soils; paddy fields", "type": "leaf"}
                ]}
            ]

    # 10. Soil Profiles and Horizons
    elif 'profiles' in fl or 'horizons' in fl:
        if is_hindi:
            return [
                {"label": "मृदा परिच्छेदिका और क्षितिज (A-B-C-R मॉडल)", "type": "branch", "date": "मृदा क्षितिज", "children": [
                    {"label": "O क्षितिज: कार्बनिक परत; पत्तियाँ और मृत पदार्थ; सूक्ष्मजीव सर्वाधिक; ह्यूमस का स्रोत", "type": "leaf"},
                    {"label": "A क्षितिज (टॉपसॉइल): ह्यूमस से समृद्ध; जड़ें और जीव; सर्वाधिक उपजाऊ; कृषि के लिए महत्वपूर्ण", "type": "leaf"},
                    {"label": "B क्षितिज (सबसॉइल): निक्षालित खनिजों का जमाव; Fe-Al-Ca; कम जैविक गतिविधि", "type": "leaf"},
                    {"label": "C क्षितिज: आंशिक रूप से अपक्षयित जनक सामग्री; मृदा निर्माण की प्रारंभिक अवस्था", "type": "leaf"},
                    {"label": "R क्षितिज (बेडरॉक): अपक्षयित मूल शैल; ग्रेनाइट, बेसाल्ट, चूनापत्थर आदि", "type": "leaf"}
                ]},
                {"label": "UPSC महत्व: मृदा परिच्छेदिका का अनुप्रयोग", "type": "branch", "date": "अनुप्रयोग", "children": [
                    {"label": "A क्षितिज क्षरण = कृषि संकट: ऊपरी मृदा का नष्ट होना दीर्घकालिक खाद्य सुरक्षा पर प्रभाव", "type": "leaf"},
                    {"label": "B क्षितिज में कठोर परत (Hardpan): जलनिकासी अवरुद्ध; जलभराव की समस्या", "type": "leaf"},
                    {"label": "परिपक्व बनाम अपरिपक्व मृदा: स्पष्ट क्षितिज = परिपक्व; अस्पष्ट = युवा/अपरिपक्व मृदा", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Soil Profile & Horizons (O-A-B-C-R Model)", "type": "branch", "date": "Horizons", "children": [
                    {"label": "O Horizon: Organic layer; leaf litter, dead matter; maximum microbial activity; source of humus", "type": "leaf"},
                    {"label": "A Horizon (Topsoil): Humus-rich; roots and organisms; most fertile; critical for agriculture", "type": "leaf"},
                    {"label": "B Horizon (Subsoil): Illuvial layer; accumulation of leached Fe, Al, Ca minerals; less biotic", "type": "leaf"},
                    {"label": "C Horizon: Partially weathered parent material; transition between soil and bedrock", "type": "leaf"},
                    {"label": "R Horizon (Bedrock): Unweathered parent rock; Granite, Basalt, Limestone etc.", "type": "leaf"}
                ]},
                {"label": "UPSC Application of Soil Profile", "type": "branch", "date": "Application", "children": [
                    {"label": "A Horizon erosion = food security crisis: Topsoil loss takes 100s of years to regenerate", "type": "leaf"},
                    {"label": "Hardpan in B horizon: Blocks drainage; creates waterlogging; common in irrigated soils", "type": "leaf"},
                    {"label": "Mature vs Immature Soil: Distinct horizons = mature/zonal; absent horizons = young/azonal", "type": "leaf"}
                ]}
            ]

    # 11. Stages of Soil Formation
    elif 'stages' in fl:
        if is_hindi:
            return [
                {"label": "मृदा निर्माण की अवस्थाएँ", "type": "branch", "date": "चरण", "children": [
                    {"label": "चरण 1 - शैल अपक्षय: यांत्रिक और रासायनिक अपक्षय से शैलों का विखंडन; खनिज मुक्त होते हैं", "type": "leaf"},
                    {"label": "चरण 2 - जैविक उपनिवेशन: काई (Lichen), Mosses; जैव कार्बनिक पदार्थ का पहला संचय; 'Pioneer Species'", "type": "leaf"},
                    {"label": "चरण 3 - ह्यूमस निर्माण: मृत जीव और पौधों का सड़ना → ह्यूमस; जीवाणु और कवक की भूमिका", "type": "leaf"},
                    {"label": "चरण 4 - क्षितिज विकास: A-B-C क्षितिज स्पष्ट होने लगते हैं; पोषक तत्वों का ऊर्ध्वाधर वितरण", "type": "leaf"},
                    {"label": "चरण 5 - परिपक्व मृदा: पूर्ण विकसित परिच्छेदिका; स्थानीय जलवायु के अनुसार प्रकार निर्धारित", "type": "leaf"}
                ]},
                {"label": "पारिस्थितिक अनुक्रमण से संबंध", "type": "branch", "date": "अनुक्रमण", "children": [
                    {"label": "लिथिक अनुक्रमण (Lithosere): चट्टानी सतह से मृदा निर्माण की पूर्ण प्रक्रिया; सैकड़ों वर्षों में", "type": "leaf"},
                    {"label": "Climax Community: परिपक्व मृदा पर ही Climax vegetation विकसित होती है", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Stages of Soil Formation", "type": "branch", "date": "Stages", "children": [
                    {"label": "Stage 1 - Rock Weathering: Mechanical/chemical breakdown of parent rock; minerals released", "type": "leaf"},
                    {"label": "Stage 2 - Biological Colonization: Lichens and mosses as pioneer species; first organic matter", "type": "leaf"},
                    {"label": "Stage 3 - Humus Formation: Decomposition of dead organisms → humus; bacteria and fungi key", "type": "leaf"},
                    {"label": "Stage 4 - Horizon Development: A-B-C horizons differentiate; vertical nutrient distribution forms", "type": "leaf"},
                    {"label": "Stage 5 - Mature Soil: Fully developed profile; soil type determined by local climate (zonal)", "type": "leaf"}
                ]},
                {"label": "Link with Ecological Succession", "type": "branch", "date": "Succession Link", "children": [
                    {"label": "Lithosere: Complete succession from bare rock → mature soil → climax community over centuries", "type": "leaf"},
                    {"label": "Climax vegetation: Only develops once mature, well-horizoned soil has formed in an area", "type": "leaf"}
                ]}
            ]

    # 12. Types of Natural Vegetation
    elif 'vegetation' in fl:
        if is_hindi:
            return [
                {"label": "प्राकृतिक वनस्पति: भारत में प्रमुख प्रकार", "type": "branch", "date": "6 प्रकार", "children": [
                    {"label": "उष्णकटिबंधीय वर्षा वन: 200+ सेमी; पश्चिमी घाट, अंडमान; सदाबहार; 3 स्तरीय छत्र; जैव विविधता हॉटस्पॉट", "type": "leaf"},
                    {"label": "उष्णकटिबंधीय पर्णपाती: 100-200 सेमी; मानसूनी वन; सागवान, साल; भारत का सर्वाधिक वन आवरण", "type": "leaf"},
                    {"label": "उष्णकटिबंधीय कंटीले: <50 सेमी; राजस्थान, गुजरात; बबूल, नागफनी; CAM प्रकाश संश्लेषण", "type": "leaf"},
                    {"label": "मैंग्रोव: ज्वारीय तट; लवण-सहिष्णु; वायवीय जड़ें (Pneumatophores); सुंदरी, राइजोफोरा", "type": "leaf"},
                    {"label": "अल्पाइन और उप-अल्पाइन: 3000+ मीटर; रोडोडेंड्रोन, जुनिपर, बर्च; टिम्बरलाइन के ऊपर घास", "type": "leaf"},
                    {"label": "लिटोरल और दलदली वनस्पति: झीलें, नदी किनारे; नरकट, कमल; आर्द्रभूमि पारिस्थितिकी", "type": "leaf"}
                ]},
                {"label": "वनस्पति और जलवायु का संबंध", "type": "branch", "date": "जलवायु-वनस्पति", "children": [
                    {"label": "Koppen जलवायु वर्गीकरण: Af (उष्णकटिबंधीय वर्षा), BSh (अर्ध-शुष्क), Cwg (मानसून)", "type": "leaf"},
                    {"label": "हिमालयी ऊर्ध्वाधर वनस्पति क्षेत्र: पर्णपाती → शंकुधारी → अल्पाइन घास → बर्फ", "type": "leaf"}
                ]}
            ]
        else:
            return [
                {"label": "Types of Natural Vegetation in India", "type": "branch", "date": "6 Types", "children": [
                    {"label": "Tropical Rain Forests: 200+ cm; Western Ghats, Andamans; evergreen; 3-tier canopy; hotspot", "type": "leaf"},
                    {"label": "Tropical Deciduous: 100-200 cm; Monsoon forests; Teak, Sal; covers largest forest area in India", "type": "leaf"},
                    {"label": "Tropical Thorny: <50 cm; Rajasthan, Gujarat; Acacia, Cactus; CAM photosynthesis for water saving", "type": "leaf"},
                    {"label": "Mangroves: Tidal zones; salt-tolerant; Pneumatophores (breathing roots); Sundari, Rhizophora", "type": "leaf"},
                    {"label": "Alpine/Sub-alpine: 3000+ m; Rhododendron, Juniper, Birch; grassland above timberline (Bugyals)", "type": "leaf"},
                    {"label": "Littoral & Swamp: Lakes, river banks; Reeds, Lotus; wetland ecology; biodiversity reservoirs", "type": "leaf"}
                ]},
                {"label": "Vegetation & Climate Relationship", "type": "branch", "date": "Climate-Vegetation", "children": [
                    {"label": "Koppen Classification: Af (tropical rainforest), BSh (semi-arid), Cwg (monsoon India)", "type": "leaf"},
                    {"label": "Himalayan Altitudinal Zones: Deciduous → Coniferous → Alpine meadows → Snow/Ice", "type": "leaf"}
                ]}
            ]

    # Fallback
    else:
        if is_hindi:
            return [{"label": "जैवभूगोल", "type": "branch", "date": "भूगोल", "children": [
                {"label": "मृदा, वन और वनस्पति से संबंधित UPSC महत्वपूर्ण विषय", "type": "leaf"}]}]
        else:
            return [{"label": "Biogeography", "type": "branch", "date": "Geography", "children": [
                {"label": "Key UPSC topics related to soils, forests and vegetation", "type": "leaf"}]}]

def process_file(html_path, is_hindi):
    print(f"Processing: {html_path} (is_hindi={is_hindi})")
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('\r\n', '\n')
    for old in ['    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n',
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
    mindmap_data = {"label": clean_title, "type": "root", "children": branches}

    css_link = '    <link rel="stylesheet" href="/assets/css/mindmap.min.css?v=2">\n'
    if css_link not in html:
        html = html.replace('</head>', css_link + '</head>')

    if is_hindi:
        instr = 'किसी <strong style="color:#a78bfa;">बैंगनी</strong> या <strong style="color:#2ecc71;">हरे</strong> <strong>+</strong> पर क्लिक करें।'
        title_text = f"{topic_name} &mdash; इंटरैक्टिव माइंडमैप"
    else:
        instr = 'Tap a <strong style="color:#a78bfa;">purple</strong> or <strong style="color:#2ecc71;">green</strong> <strong>+</strong> to expand.'
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
    if re.search(r'<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">', html):
        html = re.sub(r'(<!-- Deep-Dive Study Guide \(Dynamically Rendered\) -->\s*<div class="card-premium" id="deep-dive-section">)', mindmap_card + r'\1', html)
    else:
        marker = '<div class="tab-panel active" id="notes-panel" role="tabpanel" aria-labelledby="notes-panel">'
        if marker in html:
            html = html.replace(marker, marker + '\n' + mindmap_card, 1)

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

def main():
    total = 0
    for root, dirs, files in os.walk(BASE):
        parts = os.path.relpath(root, BASE).split(os.sep)
        is_hindi = 'hi' in parts
        for file in files:
            if file == "index.html":
                process_file(os.path.join(root, file), is_hindi)
                total += 1
    print(f"\nDone! Patched {total} files.")

if __name__ == '__main__':
    main()
