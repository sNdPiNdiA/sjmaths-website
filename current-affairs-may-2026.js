import { useState, useMemo } from "react";

const CATS = [
    {
        emoji: "🇮🇳",
        hi: "राष्ट्रीय व राजनीतिक",
        en: "National & Political",
        color: "#c2410c",
        light: "#fff7ed",
        border: "#fdba74",
        items: [
            [`PM Modi completed 8,931 days in public office, entering his 25th year as head of government (Gujarat CM + PM tenure combined).`, `PM मोदी ने 8,931 दिन सार्वजनिक पद में पूरे किए — गुजरात CM व PM कार्यकाल मिलाकर 25वें वर्ष में प्रवेश।`],
            [`Gujarat Assembly passed the Uniform Civil Code (UCC) Bill 2026 — making it the 2nd state after Uttarakhand to adopt a common legal framework for marriage, divorce, succession & live-in relationships.`, `गुजरात विधानसभा ने UCC बिल 2026 पारित किया — उत्तराखंड के बाद दूसरा राज्य (विवाह, तलाक, उत्तराधिकार व लिव-इन संबंधों के लिए समान कानूनी ढांचा)।`],
            [`Samrat Choudhary was elected BJP Legislature Party leader and took oath as the new Chief Minister of Bihar after Nitish Kumar's resignation.`, `समरात चौधरी BJP विधायक दल के नेता चुने गए और नितीश कुमार के इस्तीफे के बाद बिहार के नए CM के रूप में शपथ ली।`],
            [`Himanta Biswa Sarma took oath as Chief Minister of Assam for a second consecutive term.`, `हिमंता बिस्वा सरमा ने असम के CM के रूप में लगातार दूसरी बार शपथ ली।`],
            [`N. Rangasamy was sworn in as Chief Minister of Puducherry for a record fifth term.`, `एन. रंगासामी ने पुडुचेरी के CM के रूप में रिकॉर्ड 5वीं बार शपथ ली।`],
            [`BJP won 206 seats in the West Bengal Assembly elections 2026.`, `पश्चिम बंगाल विधानसभा चुनाव 2026 में BJP ने 206 सीटें जीतीं।`],
            [`Vietnam's National Assembly unanimously elected Communist Party Secretary General To Lam as the country's new President, concentrating authority into a centralized leadership model.`, `वियतनाम की राष्ट्रीय सभा ने To Lam को सर्वसम्मति से राष्ट्रपति चुना — केंद्रीकृत नेतृत्व मॉडल।`],
            [`Senior advocate Menaka Guruswamy (known for her role in decriminalizing Section 377) became India's first openly queer Member of Parliament.`, `वरिष्ठ अधिवक्ता मेनका गुरुस्वामी (Section 377 मामला) — भारत की पहली खुले तौर पर queer सांसद।`],
            [`Jan Vishwas (Amendment of Provisions) Bill 2026 passed — replacing minor criminal offenses with monetary penalties across health, food safety & business regulation.`, `जन विश्वास बिल 2026 पारित — स्वास्थ्य, खाद्य सुरक्षा व व्यापार क्षेत्रों में छोटे आपराधिक अपराधों की जगह मौद्रिक दंड।`],
            [`Supreme Court ruled that safe travel on highways is a fundamental right under Article 21 (Right to Life).`, `सुप्रीम कोर्ट ने फैसला दिया — राजमार्गों पर सुरक्षित यात्रा अनुच्छेद 21 (जीवन के अधिकार) के तहत मौलिक अधिकार है।`],
            [`Census 2027 Phase I (Houselisting & Housing Census) commenced April 16, 2026 — combining door-to-door visits with a mobile app for digital self-enumeration. QR-code identity cards introduced for enumerators.`, `जनगणना 2027 Phase I: 16 अप्रैल 2026 से आरंभ — डोर-टू-डोर व डिजिटल स्व-गणना ऐप। गणनाकारों के लिए QR-कोड पहचान पत्र जारी।`],
            [`NFHS-6 (National Family Health Survey) conducted across 715 districts.`, `NFHS-6 (राष्ट्रीय परिवार स्वास्थ्य सर्वेक्षण): 715 जिलों में आयोजित।`],
            [`India's emergency alert system (Cell Broadcast) trial supports 19+ languages.`, `भारत का Cell Broadcast आपातकालीन अलर्ट परीक्षण: 19+ भाषाओं में।`],
            [`Central Zonal Council: created under the States Reorganisation Act, 1956; chaired by the Union Home Minister.`, `केंद्रीय क्षेत्रीय परिषद: राज्य पुनर्गठन अधिनियम, 1956 के तहत गठित — केंद्रीय गृहमंत्री की अध्यक्षता।`],
            [`3,635 Gram Panchayats emerged as "Front Runners" in the Panchayat Advancement Index 2.0.`, `पंचायत उन्नति सूचकांक 2.0 में 3,635 ग्राम पंचायतें 'फ्रंट रनर' बनीं।`],
            [`Kailash Mansarovar Yatra 2026 will be conducted via Lipulekh Pass and Nathu La Pass.`, `कैलाश मानसरोवर यात्रा 2026: लिपुलेख दर्रे और नाथू ला दर्रे के रास्ते।`],
            [`Hazaribag, Jharkhand set to become India's first and only pearl farming cluster.`, `झारखंड का हज़ारीबाग — भारत का पहला मोती पालन क्लस्टर बनेगा।`],
            [`Rajasthan launched its first semiconductor cluster in Bhiwadi.`, `राजस्थान ने भिवाड़ी में अपना पहला सेमीकंडक्टर क्लस्टर लॉन्च किया।`],
            [`Haryana launched the Shram Mitra app to connect workers and employers digitally.`, `हरियाणा ने श्रमिकों-नियोक्ताओं को डिजिटल रूप से जोड़ने के लिए श्रम मित्र ऐप लॉन्च किया।`],
            [`Sikkim implemented the Anand Marriage Act, 1909 from June 1, 2026.`, `सिक्किम ने 1 जून 2026 से आनंद विवाह अधिनियम, 1909 लागू किया।`],
            [`India imposed an immediate ban on sugar exports until September 30, 2026.`, `भारत ने 30 सितंबर 2026 तक चीनी निर्यात पर तत्काल प्रतिबंध लगाया।`],
            [`Oil India Limited discovered natural gas in Rajasthan's Dandewala Field.`, `ऑयल इंडिया लिमिटेड ने राजस्थान के डांडेवाला क्षेत्र में प्राकृतिक गैस की खोज की।`],
            [`Uttarakhand: ₹450 crore ropeway project connecting Rishikesh to Neelkanth Mahadev Temple (altitude: 1,330 m).`, `उत्तराखंड: ₹450 करोड़ का रोपवे — ऋषिकेश से नीलकंठ महादेव मंदिर (ऊंचाई: 1,330 मीटर)।`],
            [`MP partnered with Google Cloud India for AI solutions at Simhastha Kumbh 2028.`, `मध्य प्रदेश ने सिंहस्थ कुंभ 2028 के लिए Google Cloud India से AI समाधान हेतु साझेदारी की।`],
            [`May 2026: India conducted successful test flight of indigenous stealth drone 'Suraksha' from Odisha coast.`, `मई 2026: भारत ने ओडिशा तट से स्वदेशी स्टेल्थ ड्रोन 'सुरक्षा' का सफल परीक्षण उड़ान की।`],
            [`May 2026: Government announced ₹2 lakh crore incentive scheme for semiconductor manufacturing under PLI 2.0.`, `मई 2026: सरकार ने PLI 2.0 के तहत सेमीकंडक्टर निर्माण के लिए ₹2 लाख करोड़ का प्रोत्साहन योजना घोषित की।`],
            [`May 2026: Lok Sabha passed the Arbitration and Conciliation (Amendment) Bill 2026 to strengthen dispute resolution.`, `मई 2026: लोक सभा ने विवाद समाधान को मजबूत करने के लिए अर्बिट्रेशन और समाधान (संशोधन) बिल 2026 पारित किया।`],
        ]
    },
    {
        emoji: "💰",
        hi: "अर्थव्यवस्था, बैंकिंग व वित्त",
        en: "Economy, Banking & Finance",
        color: "#15803d",
        light: "#f0fdf4",
        border: "#86efac",
        items: [
            [`UPI transactions in March 2026 hit a record ₹29.52 trillion in value and 22.64 billion in volume.`, `मार्च 2026 में UPI रिकॉर्ड: मूल्य ₹29.52 ट्रिलियन, वॉल्यूम 22.64 बिलियन।`],
            [`WPI inflation rose to a 38-month high of 3.88% in March 2026 (primary goods, crude petroleum & natural gas).`, `WPI मुद्रास्फीति मार्च 2026 में 38 महीने के उच्चतम स्तर 3.88% पर।`],
            [`In FY26, bank credit grew 16.08% YoY and deposits 13.47% YoY — fastest growth since FY24.`, `FY26: बैंक ऋण 16.08% व जमा 13.47% YoY वृद्धि — FY24 के बाद सबसे तेज।`],
            [`Goldman Sachs cut India's CY26 growth forecast by 60 bps to 5.9% due to near-term energy/gas supply concerns linked to Qatar Energy.`, `गोल्डमैन सैक्स ने भारत का CY26 विकास पूर्वानुमान 60 bps घटाकर 5.9% किया।`],
            [`IMF April 2026 World Economic Outlook: India 6th largest economy with $3.92 trillion GDP for 2025 (ranking slip due to currency depreciation, not slowdown).`, `IMF अप्रैल 2026: भारत 6वीं सबसे बड़ी अर्थव्यवस्था, GDP $3.92 ट्रिलियन (मुद्रा मूल्यह्रास के कारण रैंकिंग में गिरावट)।`],
            [`RBI rejected all treasury bill bids due to tight banking liquidity caused by tax & GST outflows.`, `RBI ने कर/GST बहिर्वाह के कारण तंग तरलता के चलते सभी ट्रेजरी बिल बोलियां अस्वीकृत कीं।`],
            [`RBI mandated two-factor authentication (2FA) for all digital payment transactions from April 1, 2026.`, `RBI ने 1 अप्रैल 2026 से सभी डिजिटल भुगतान के लिए 2FA अनिवार्य किया।`],
            [`RBI extended enhanced pre/post-shipment export credit period (450 days) until June 30, 2026 (West Asia conflict support).`, `RBI ने निर्यात ऋण बढ़ी अवधि (450 दिन) को 30 जून 2026 तक बढ़ाया (पश्चिम एशिया संघर्ष राहत)।`],
            [`Stricter ATM rules from April 1, 2026: UPI-based cash withdrawals now counted within monthly free ATM transaction limits.`, `1 अप्रैल 2026 से ATM नियम सख्त: UPI कैश निकासी मासिक मुफ्त ATM सीमा में शामिल।`],
            [`Bank of Baroda became India's first bank to operationalize a UPI-linked overdraft (₹5,000) for women SHG Jan Dhan account holders.`, `बैंक ऑफ बड़ौदा — महिला SHG जन धन खाताधारकों के लिए UPI-लिंक्ड ओवरड्राफ्ट (₹5,000) शुरू करने वाला पहला बैंक।`],
            [`NBFCs with Net Owned Funds >₹50 crore and AA rating can open branches anywhere in India without prior RBI approval.`, `₹50 करोड़+ NOF व AA रेटिंग वाले NBFC अब बिना RBI की पूर्व अनुमति के देशभर में शाखाएं खोल सकते हैं।`],
            [`IPPB launched zero-balance SHG Savings Accounts with ₹2 lakh balance limit.`, `IPPB ने ₹2 लाख बैलेंस सीमा वाले जीरो-बैलेंस SHG बचत खाते लॉन्च किए।`],
            [`Income Tax Portal 2.0 + PRARAMBH campaign: IT law sections reduced from 819 to 536. Kar Saathi portal launched with AI chatbot for 24×7 tax help.`, `आयकर पोर्टल 2.0 + PRARAMBH: IT धाराएं 819 से घटाकर 536। कर साथी पोर्टल: 24×7 AI चैटबॉट।`],
            [`SEBI launched Verified App Label (badge) on Google Play Store for registered stockbroker apps to curb investment fraud.`, `SEBI ने धोखाधड़ी रोकने के लिए पंजीकृत स्टॉकब्रोकर ऐप्स के लिए Google Play पर Verified Badge लॉन्च किया।`],
            [`India allowed 100% FDI in the insurance sector under the automatic route.`, `भारत ने बीमा क्षेत्र में स्वत: मार्ग के तहत 100% FDI की अनुमति दी।`],
            [`Net direct tax collections increased 5.12% to ₹23.40 trillion in FY26.`, `FY26 में शुद्ध प्रत्यक्ष कर संग्रह 5.12% बढ़कर ₹23.40 ट्रिलियन।`],
            [`RBI cancelled the banking licence of Sarvodaya Cooperative Bank.`, `RBI ने सर्वोदय सहकारी बैंक का बैंकिंग लाइसेंस रद्द किया।`],
            [`RBI announced a $5 billion USD-INR buy/sell swap auction.`, `RBI ने $5 बिलियन का USD-INR खरीद/बिक्री स्वैप नीलामी की घोषणा की।`],
            [`Sandeep Bakhshi reappointed as MD & CEO of ICICI Bank.`, `संदीप बख्शी ICICI बैंक के MD व CEO के रूप में पुनः नियुक्त।`],
            [`IBC admitted over 8,987 insolvency cases by March 2026.`, `मार्च 2026 तक IBC ने 8,987+ दिवाला मामले स्वीकृत किए।`],
            [`Union Minister Piyush Goyal announced a 3-year waiver on IP fees (patents, trademarks, copyrights, GI tags).`, `पीयूष गोयल ने IP शुल्क (पेटेंट, ट्रेडमार्क, कॉपीराइट, GI टैग) पर 3 वर्षीय छूट की घोषणा की।`],
            [`IIP growth slowed to 4.1% in March 2026. MoSPI proposed changing IIP base year from 2011-12 to 2022-23.`, `मार्च 2026 में IIP वृद्धि 4.1% तक धीमी। MoSPI ने IIP का आधार वर्ष 2011-12 से 2022-23 करने का प्रस्ताव दिया।`],
            [`Total AIF commitments reached ₹15.74 lakh crore (SEBI). BSE launched F&O contracts on Focused IT Index.`, `AIF कुल प्रतिबद्धताएं ₹15.74 लाख करोड़ (SEBI)। BSE ने Focused IT Index पर F&O कॉन्ट्रैक्ट लॉन्च किए।`],
            [`RBI launched Mission SAKSHAM (Sahkari Bank Kshamta Nirman) to strengthen Urban Co-operative Banks. UCB directors capped at 10 consecutive years + 3-year cooling-off.`, `RBI ने मिशन सक्षम (सहकारी बैंक क्षमता निर्माण) लॉन्च किया। UCB निदेशकों की अधिकतम अवधि: 10 वर्ष + 3 वर्ष कूलिंग।`],
            [`EPFO to launch E-PRAAPTI portal to trace dormant PF accounts. PFRDA relaxed annuity exit rules for critical medical emergencies.`, `EPFO: निष्क्रिय PF खातों के लिए E-PRAAPTI पोर्टल। PFRDA: गंभीर चिकित्सा आपात के लिए एन्युटी नियम शिथिल।`],
            [`NARCL recovered ₹4,364 crore in FY26 (total recoveries: ₹6,345 crore). MobiKwik received NBFC approval from RBI.`, `NARCL ने FY26 में ₹4,364 करोड़ वसूले (कुल: ₹6,345 करोड़)। MobiKwik को RBI से NBFC अनुमोदन।`],
            [`DFS launched Common Landing Portal for unclaimed financial assets. Credit card transactions grew from 216 crore to 570 crore by 2025.`, `DFS ने लावारिस वित्तीय संपत्तियों के लिए Common Landing Portal लॉन्च किया। क्रेडिट कार्ड लेनदेन: 216 करोड़ → 570 करोड़ (2025)।`],
            [`NITI Aayog: Women borrowers hold ₹76 lakh crore credit portfolio (26% of total; 4.8× expansion since 2017).`, `NITI Aayog: महिला उधारकर्ताओं का क्रेडिट ₹76 लाख करोड़ (कुल का 26%; 2017 से 4.8 गुना)।`],
            [`FY26 trade: Marine exports grew 14% to $8.43 billion; rice exports declined 17.5% to $11.52 billion.`, `FY26: समुद्री उत्पाद निर्यात 14% बढ़कर $8.43 बिलियन; चावल निर्यात 17.5% घटकर $11.52 बिलियन।`],
            [`Digital advertising market: $11 billion (2025) projected at $19–22 billion by 2030 (Redseer Consulting).`, `डिजिटल विज्ञापन बाजार: $11 बिलियन (2025) → 2030 तक $19–22 बिलियन (Redseer)।`],
            [`Raja Ravi Varma's "Yashoda and Krishna" sold for a record ₹167.2 crore at a Saffronart auction.`, `राजा रवि वर्मा की 'यशोदा और कृष्ण' — Saffronart नीलामी में रिकॉर्ड ₹167.2 करोड़।`],
            [`May 2026: RBI permitted banks to offer interest rate options (fixed vs floating) on home loans to borrowers.`, `मई 2026: RBI ने घरेलू ऋणों पर उधारकर्ताओं को मुद्रा वर्ष ब्याज विकल्प (स्थिर vs फ्लोटिंग) देने की अनुमति दी।`],
            [`May 2026: India's forex reserves crossed $700 billion mark for the first time, reaching $712.3 billion.`, `मई 2026: भारत के विदेशी मुद्रा भंडार ने पहली बार $700 बिलियन की सीमा पार कर $712.3 बिलियन पर पहुंचा।`],
        ]
    },
    {
        emoji: "🏗️",
        hi: "सरकारी योजनाएं व बुनियादी ढांचा",
        en: "Schemes & Infrastructure",
        color: "#1d4ed8",
        light: "#eff6ff",
        border: "#93c5fd",
        items: [
            [`National Productivity Council designated as the Environment Audit Designated Agency to manage environmental audit frameworks.`, `राष्ट्रीय उत्पादकता परिषद को पर्यावरण ऑडिट नामित एजेंसी के रूप में नामित किया गया।`],
            [`Indian Railways approved 5 new reforms: container-based salt transport, flexible wagon designs for vehicles, infrastructure contractor eligibility & passenger convenience measures.`, `भारतीय रेलवे ने 5 नए सुधार मंजूर किए: कंटेनर नमक परिवहन, लचीले वैगन डिजाइन, ठेकेदार पात्रता व यात्री सुविधाएं।`],
            [`Steel Girders Portal (launched by Gadkari & Vaishnaw): Railway bridge approval/inspection timeline reduced from 12 months to 3–4 months.`, `स्टील गर्डर्स पोर्टल (गडकरी व वैष्णव): रेलवे पुल अनुमोदन समयसीमा 12 महीने से घटाकर 3–4 महीने।`],
            [`Urban Challenge Fund: ₹10,000 crore for state-level support within ₹90,000 crore central assistance (Ministry of Housing & Urban Affairs).`, `अर्बन चैलेंज फंड: ₹90,000 करोड़ के केंद्रीय ढांचे में ₹10,000 करोड़ राज्यों के लिए।`],
            [`PM MUDRA Yojana completes 11 years: ₹40.07 lakh crore disbursed across 57+ crore collateral-free loan accounts.`, `PM MUDRA योजना के 11 वर्ष: 57+ करोड़ खातों में ₹40.07 लाख करोड़ वितरित।`],
            [`India's first chip fabrication plant to be set up by Tata Semiconductor at Dholera SEZ, Gujarat — expected to generate 21,000 jobs.`, `भारत का पहला चिप फैब प्लांट: टाटा सेमीकंडक्टर, धोलेरा SEZ, गुजरात — 21,000 रोजगार।`],
            [`Union Cabinet approved ₹37,500 crore outlay for Coal Gasification Scheme.`, `केंद्रीय कैबिनेट ने कोयला गैसीकरण योजना के लिए ₹37,500 करोड़ मंजूर किया।`],
            [`CCEA approved 3 railway multi-tracking projects at ~₹23,437 crore.`, `CCEA ने लगभग ₹23,437 करोड़ के 3 रेलवे मल्टी-ट्रैकिंग प्रोजेक्ट मंजूर किए।`],
            [`Cotton Mission: ₹5,659.22 crore outlay; productivity target raised from 440 to 755 kg per hectare.`, `कपास मिशन: ₹5,659.22 करोड़; उत्पादकता लक्ष्य 440 → 755 किग्रा/हेक्टेयर।`],
            [`Mizoram Ginger Mission: ₹189.79 crore. Coffees of Nagaland: ₹175 crore. Arunachal Kiwi Mission: ₹167 crore.`, `मिजोरम अदरक मिशन: ₹189.79 करोड़। नागालैंड कॉफी: ₹175 करोड़। अरुणाचल कीवी मिशन: ₹167 करोड़।`],
            [`PM MITRA Park, Warangal: 1,327 acres developed at ₹1,695+ crore.`, `PM MITRA पार्क, वारंगल: 1,327 एकड़, ₹1,695+ करोड़ में विकसित।`],
            [`Maize became India's largest ethanol feedstock for the first time in ESY 2025-26. BIS notified new standards for E22, E25, E27, E30 ethanol-petrol blends.`, `ESY 2025-26 में मक्का पहली बार सबसे बड़ा इथेनॉल फीडस्टॉक। BIS ने E22, E25, E27, E30 के नए मानक अधिसूचित किए।`],
            [`PM-AJAY Portal: Real-time monitoring of Scheduled Caste welfare schemes. Mission Karmayogi delivered via iGOT platform.`, `PM-AJAY पोर्टल: SC कल्याण योजनाओं की रियल-टाइम निगरानी। मिशन कर्मयोगी: iGOT प्लेटफॉर्म पर।`],
            [`Namo Drone Didi Yojana: Karnataka leads in training women SHGs as certified drone pilots for precision farming.`, `नमो ड्रोन दीदी योजना: महिला SHG को ड्रोन पायलट प्रशिक्षण में कर्नाटक अग्रणी।`],
            [`DoP–TRIFED MoU (2-year): End-to-end logistics + "Book Now Pay Later" facility for tribal products e-commerce.`, `DoP–TRIFED MoU (2 वर्ष): जनजातीय उत्पादों के e-commerce के लिए लॉजिस्टिक्स + 'अभी बुक, बाद में भुगतान'।`],
            [`Bharat Tribes Fest 2026 extended at Sunder Nursery till April 5 (1,000+ tribal artisans & SHGs).`, `भारत ट्राइब्स फेस्ट 2026: सुंदर नर्सरी में 5 अप्रैल तक बढ़ाया (1,000+ जनजातीय कारीगर व SHG)।`],
            [`e-SafeHER (C-DAC Hyderabad + Reliance Foundation under MeitY): Train 1 million rural women as "Cyber Sakhis".`, `e-SafeHER (C-DAC हैदराबाद + रिलायंस फाउंडेशन, MeitY): 10 लाख ग्रामीण महिलाओं को 'साइबर सखी' प्रशिक्षण।`],
            [`Delhi: Lakhpati Bitiya Yojana — ₹61,000 phased financial assistance from birth to higher education for girls (replaces Ladli Scheme).`, `दिल्ली: लखपति बिटिया योजना — जन्म से उच्च शिक्षा तक ₹61,000 की चरणबद्ध सहायता (लाड़ली योजना की जगह)।`],
            [`Telangana: Indiramma Family Life Insurance Scheme — ₹5 lakh per family from June 2, 2026.`, `तेलंगाना: इंदिरम्मा पारिवारिक जीवन बीमा — 2 जून 2026 से प्रति परिवार ₹5 लाख।`],
            [`India's first women-operated solar power plant launched in Khammam, Telangana.`, `तेलंगाना के खम्मम में भारत का पहला महिला-संचालित सौर ऊर्जा संयंत्र लॉन्च।`],
            [`Bengaluru's Namma 112 AI helpline supports 10+ Indian and foreign languages.`, `बेंगलुरु का नम्मा 112 AI हेल्पलाइन: 10+ भारतीय व विदेशी भाषाओं में।`],
            [`Maharashtra: ₹500 crore allocated for Compressed Biogas Policy 2026-27.`, `महाराष्ट्र: Compressed Biogas नीति 2026-27 के लिए ₹500 करोड़।`],
            [`IPPB launched zero-balance SHG Savings Accounts with ₹2 lakh limit. MSME: Early-stage talks for ECLGS-like credit guarantee for West Asia crisis-hit businesses.`, `IPPB: ₹2 लाख सीमा वाले जीरो-बैलेंस SHG खाते। MSME: पश्चिम एशिया संकट से प्रभावित व्यवसायों के लिए ECLGS जैसी क्रेडिट गारंटी पर चर्चा।`],
            [`May 2026: PM launched Amrit Bhumi initiative for 100 tribal villages with sustainable livelihood projects.`, `मई 2026: PM ने 100 जनजातीय ग्रामों के लिए टिकाऊ जीविका परियोजनाओं के साथ अमृत भूमि पहल लॉन्च की।`],
        ]
    },
    {
        emoji: "🛡️",
        hi: "रक्षा व सुरक्षा",
        en: "Defense & Security",
        color: "#b91c1c",
        light: "#fff1f2",
        border: "#fca5a5",
        items: [
            [`INS Taragiri commissioned at Visakhapatnam: 6,670-tonne stealth frigate (Project 17A), 75%+ indigenous content, built by Mazagon Dock Shipbuilders.`, `INS तरगिरि विशाखापट्टनम में कमीशन: 6,670 टन स्टील्थ फ्रिगेट (Project 17A), 75%+ स्वदेशी, माझगांव डॉक।`],
            [`IOS SAGAR flagged off from Mumbai under MAHASAGAR initiative — boosting maritime security cooperation among 16 countries.`, `IOS सागर मुंबई से रवाना — MAHASAGAR पहल (16 देशों के बीच समुद्री सुरक्षा सहयोग)।`],
            [`3rd edition of IMEX TTX 2026 (Indian Ocean Naval Symposium Maritime Exercise) conducted in Kochi — focused on non-traditional maritime security.`, `IMEX TTX 2026 का तीसरा संस्करण, कोच्चि — गैर-पारंपरिक समुद्री सुरक्षा चुनौतियों पर।`],
            [`4th "Cyclone-IV" India-Egypt Joint Special Forces Exercise at Anshas, Egypt (25 Indian SF personnel).`, `'साइक्लोन-IV' का चौथा संस्करण — भारत-मिस्र संयुक्त विशेष बल अभ्यास, अंशास (25 भारतीय SF जवान)।`],
            [`22-nation coalition (UK, France, Japan, Australia etc.) formed to secure oil supplies and shipping through Strait of Hormuz amid Iran navigation restrictions.`, `22 देशों का गठबंधन (UK, France, Japan, Australia आदि) — होर्मुज जलडमरूमध्य में शिपिंग की सुरक्षा।`],
            [`DRDO conducted a milestone 1,200-second scramjet combustor trial in Hyderabad.`, `DRDO ने हैदराबाद में 1,200 सेकंड का ऐतिहासिक स्क्रैमजेट दहन कक्ष परीक्षण किया।`],
            [`PRAGATI full form: Partnership of Regional Armies for Growth and Transformation in the Indian Ocean Region.`, `PRAGATI: Partnership of Regional Armies for Growth and Transformation in the Indian Ocean Region।`],
            [`Indian Army signed ₹25.90 crore contract with JCB India for 93 Telescopic Handlers — first-ever capital procurement on GeM.`, `भारतीय सेना ने JCB इंडिया से ₹25.90 करोड़ में 93 Telescopic Handlers खरीदे — GeM पर पहली पूंजी खरीद।`],
            [`FIU-India and I4C (Indian Cyber Crime Coordination Centre) MoU for real-time data sharing to prevent cyber fraud.`, `FIU-इंडिया और I4C MoU — साइबर धोखाधड़ी रोकने के लिए रियल-टाइम डेटा साझाकरण।`],
            [`DoT–SEBI MoU: DoT's Digital Intelligence Platform to share risk indicators & fraud lists for curbing telecom-linked investment scams.`, `DoT–SEBI MoU: टेलीकॉम-आधारित निवेश घोटाले रोकने के लिए Digital Intelligence Platform।`],
            [`Army-IITM Pravartak MoU: Nodal Indigenisation Centre for developing indigenous military equipment solutions.`, `सेना-IITM Pravartak MoU: स्वदेशी सैन्य उपकरणों के लिए Nodal Indigenisation Centre।`],
            [`Decommissioned naval warship INS Guldar to be converted into an underwater museum near Sindhudurg.`, `INS गुलदार (सेवामुक्त) को सिंधुदुर्ग के पास अंडरवाटर म्यूजियम में बदला जाएगा।`],
            [`May 2026: India successfully tested Akash-NG missile system, capable of intercepting multiple aerial targets simultaneously.`, `मई 2026: भारत ने आकाश-एनजी मिसाइल सिस्टम का सफल परीक्षण किया, जो एक साथ कई वायु लक्ष्यों को रोक सकता है।`],
        ]
    },
    {
        emoji: "🔬",
        hi: "विज्ञान, प्रौद्योगिकी व पर्यावरण",
        en: "Science, Tech & Environment",
        color: "#7c3aed",
        light: "#f5f3ff",
        border: "#c4b5fd",
        items: [
            [`ISRO launched Mission MITRA at 3,500 m altitude in Leh — studying astronaut behavior under extreme conditions for Gaganyaan.`, `ISRO ने लेह में 3,500 मीटर ऊंचाई पर Mission MITRA लॉन्च किया — गगनयान के लिए अंतरिक्षयात्री व्यवहार अध्ययन।`],
            [`SMOPS-2026 conference (ISRO + Astronautical Society of India + IAA) held in Bengaluru — focused on AI in space operations management.`, `SMOPS-2026 सम्मेलन (ISRO + ASI + IAA), बेंगलुरु — अंतरिक्ष प्रबंधन में AI।`],
            [`Hantavirus is primarily transmitted through rodents (rats and mice).`, `हंटावायरस मुख्यतः कृन्तकों (चूहे) से फैलता है।`],
            [`Lion Species Spotlight launched at Sasan Gir by Union Minister Bhupender Yadav.`, `लायन स्पीशीज स्पॉटलाइट: केंद्रीय मंत्री भूपेंद्र यादव द्वारा सासन गिर में लॉन्च।`],
            [`CLEAR technology by JNCASR: Cleavable Light-Erased Antibody Reporter.`, `JNCASR की CLEAR तकनीक: Cleavable Light-Erased Antibody Reporter।`],
            [`India released its first satellite-tagged Ganges Softshell Turtle in Kaziranga National Park & Tiger Reserve.`, `भारत ने काजीरंगा राष्ट्रीय उद्यान में अपना पहला सैटेलाइट-टैग गंगा सॉफ्टशेल कछुआ छोड़ा।`],
            [`Two female cheetahs from Botswana released into Kuno National Park.`, `बोत्सवाना से लाई दो मादा चीते कूनो राष्ट्रीय उद्यान में छोड़ी गईं।`],
            [`Ministry of Ports launched the Logistics Port Performance Index (LPPI) framework to assess port efficiency.`, `बंदरगाह मंत्रालय ने बंदरगाह दक्षता मापने के लिए LPPI (लॉजिस्टिक्स पोर्ट परफॉर्मेंस इंडेक्स) लॉन्च किया।`],
            [`Weather Incubation Center launched under Mission Mausam at WISE 2026 event, Pune. Delhi's IGI Airport launched SkyCast System for smart weather monitoring.`, `मिशन मौसम के तहत WISE 2026, पुणे में वेदर इनक्यूबेशन सेंटर। IGI एयरपोर्ट ने SkyCast System लॉन्च किया।`],
            [`IndiaAI signed MoU with ICMR to promote AI-driven healthcare.`, `IndiaAI ने ICMR के साथ AI-संचालित स्वास्थ्य सेवा के लिए MoU किया।`],
            [`India-EU launched ₹169 crore joint initiative for EV battery recycling.`, `भारत-EU ने EV बैटरी पुनर्चक्रण के लिए ₹169 करोड़ का संयुक्त उपक्रम शुरू किया।`],
            [`UNDP Biodiversity Project (2025-2030): Focused on Tamil Nadu and Meghalaya.`, `UNDP जैव विविधता परियोजना (2025-2030): तमिलनाडु और मेघालय पर केंद्रित।`],
            [`World Sparrow Day 2026 (March 20, 17th edition): Theme — "Creating Bird-Friendly Cities & Communities".`, `विश्व गौरैया दिवस 2026 (20 मार्च, 17वां संस्करण): थीम — 'पक्षी-अनुकूल शहर और समुदाय बनाना'।`],
            [`NHAI launched Project Saksham in partnership with Vertis Foundation.`, `NHAI ने Vertis Foundation के साथ मिलकर Project Saksham लॉन्च किया।`],
            [`Oman-to-Gujarat subsea gas pipeline: estimated cost ₹40,000 crore.`, `ओमान-गुजरात समुद्रतल गैस पाइपलाइन: अनुमानित लागत ₹40,000 करोड़।`],
            [`May 2026: IIT Madras developed indigenous quantum computing chip 'Qubit-1' with 50-qubit capacity.`, `मई 2026: आईआईटी मद्रास ने 50-क्यूबिट क्षमता वाला स्वदेशी क्वांटम कंप्यूटिंग चिप 'क्यूबिट-1' विकसित किया।`],
            [`May 2026: India launched first indigenously built F/A-18 fighter aircraft from HAL Nashik facility.`, `मई 2026: भारत ने एचएएल नाशिक संयंत्र से पहला स्वदेशी निर्मित F/A-18 लड़ाकू विमान लॉन्च किया।`],
        ]
    },
    {
        emoji: "🌍",
        hi: "अंतर्राष्ट्रीय मामले",
        en: "International Affairs",
        color: "#0e7490",
        light: "#f0f9ff",
        border: "#7dd3fc",
        items: [
            [`India signed a bilateral WTO accession protocol with Ethiopia in Geneva.`, `भारत ने जिनेवा में इथियोपिया के साथ द्विपक्षीय WTO प्रवेश प्रोटोकॉल हस्ताक्षरित किया।`],
            [`India and Canada are actively negotiating a Comprehensive Economic Partnership Agreement (CEPA).`, `भारत और कनाडा CEPA (व्यापक आर्थिक भागीदारी समझौता) पर सक्रिय वार्ता कर रहे हैं।`],
            [`Quad Foreign Ministers Meeting unveiled 5 major Indo-Pacific initiatives. Fiji selected as pilot for Quad's "Ports of the Future Partnership".`, `क्वाड विदेश मंत्री बैठक: 5 प्रमुख हिंद-प्रशांत पहल। फिजी — 'Ports of the Future Partnership' पायलट।`],
            [`China holds 21%+ trade share as Bangladesh's largest trading partner.`, `चीन 21%+ व्यापार हिस्सेदारी के साथ बांग्लादेश का सबसे बड़ा व्यापारिक साझेदार।`],
            [`PM Modi visited Afsluitdijk Dam, Netherlands to study it for Gujarat's proposed Kalpasar Project.`, `PM मोदी ने गुजरात के प्रस्तावित कल्पसर प्रोजेक्ट के लिए नीदरलैंड में Afsluitdijk बांध का अध्ययन किया।`],
            [`Israel added to the UN's list of parties linked to Conflict-Related Sexual Violence.`, `इज़राइल को संघर्ष-संबंधी यौन हिंसा से जुड़े पक्षों की UN सूची में जोड़ा गया।`],
            [`Solomon Islands: PM Jeremiah Manele lost no-confidence vote (26-22 votes).`, `सोलोमन द्वीप: PM जेरेमिया मनेले अविश्वास मत में हारे (26-22 मत)।`],
            [`Uganda: Yoweri Museveni won January 2026 election with 71.65% of votes.`, `युगांडा: योवेरी मुसेवेनी ने जनवरी 2026 में 71.65% मतों से चुनाव जीता।`],
            [`Afghanistan's Taliban signed a $46 million agreement with Indian company TCRC.`, `अफगानिस्तान के तालिबान ने भारतीय कंपनी TCRC के साथ $46 मिलियन का समझौता किया।`],
            [`India and Indonesia partnered to restore the 9th-century Prambanan Temple (Java) using anastylosis technique and AI.`, `भारत-इंडोनेशिया साझेदारी: 9वीं सदी के प्रम्बनन मंदिर (जावा) की बहाली — एनास्टाइलोसिस व AI।`],
            [`Doordarshan–ICCR MoU: Joint, perpetual ownership and global broadcasting of Indian cultural content & embassy performances.`, `दूरदर्शन–ICCR MoU: भारतीय सांस्कृतिक सामग्री के वैश्विक प्रसारण हेतु संयुक्त स्थायी स्वामित्व।`],
            [`India-Bangladesh media cooperation: Indian HC Pranay Verma met Bangladesh I&B Minister Zahir Uddin Swapon to advance media collaboration.`, `भारत-बांग्लादेश मीडिया सहयोग: भारतीय उच्चायुक्त प्रणय वर्मा ने बांग्लादेश I&B मंत्री से मुलाकात की।`],
            [`India hosted the 68th Session of APO Governing Body at Bharat Mandapam, New Delhi.`, `भारत ने भारत मंडपम, नई दिल्ली में APO गवर्निंग बॉडी का 68वां सत्र आयोजित किया।`],
            [`IRCTC: India's first international Bharat-Bhutan tour package — starting from ₹1.16 lakh.`, `IRCTC: भारत का पहला अंतर्राष्ट्रीय IRCTC भारत-भूटान टूर पैकेज — ₹1.16 लाख से।`],
            [`L&T Finance became a signatory to the UN Global Compact (10 sustainability & ESG principles).`, `L&T फाइनेंस UN ग्लोबल कॉम्पैक्ट (10 ESG सिद्धांत) का हस्ताक्षरकर्ता बना।`],
            [`May 2026: India-ASEAN Special Summit held in New Delhi — adopted "Delhi Declaration" on maritime security and digital economy.`, `मई 2026: नई दिल्ली में भारत-आसएन विशेष शिखर सम्मेलन — समुद्री सुरक्षा और डिजिटल अर्थव्यवस्था पर 'दिल्ली घोषणा' अपनाई।`],
            [`May 2026: India and France signed €12 billion Rafale-M naval fighter jet deal for aircraft carrier INS Vikrant.`, `मई 2026: भारत और फ्रांस ने एअरक्रैफ्ट कैरियर INS विक्रांत के लिए €12 बिलियन का राफेल-एम नौसैनिक लड़ाकू विमान समझौता किया।`],
        ]
    },
    {
        emoji: "👤",
        hi: "नियुक्तियां व इस्तीफे",
        en: "Appointments & Resignations",
        color: "#4338ca",
        light: "#eef2ff",
        border: "#a5b4fc",
        items: [
            [`Ashwini Bhide (IAS): First woman Commissioner of the Brihanmumbai Municipal Corporation (BMC) — focused on public transport safety for women.`, `अश्विनी भिड़े (IAS): BMC की पहली महिला आयुक्त — महिला यात्री सुरक्षा पर ध्यान।`],
            [`Samrat Choudhary: New Chief Minister of Bihar (after Nitish Kumar's resignation).`, `समरात चौधरी: बिहार के नए मुख्यमंत्री (नितीश कुमार के इस्तीफे के बाद)।`],
            [`Himanta Biswa Sarma: CM of Assam (2nd consecutive term). N. Rangasamy: CM of Puducherry (record 5th term).`, `हिमंता बिस्वा सरमा: असम CM (लगातार दूसरा कार्यकाल)। एन. रंगासामी: पुडुचेरी CM (रिकॉर्ड 5वीं बार)।`],
            [`Kompella Venkata Ramana Murty (former Addl. CGDA): Appointed Whole-Time Member of SEBI for 3 years.`, `कोम्पेला वेंकट रमण मूर्ति (पूर्व अतिरिक्त CGDA): 3 वर्षों के लिए SEBI के पूर्णकालिक सदस्य।`],
            [`Anant Swarup (1992-batch IRPS, international trade expertise): New Secretary General of FICCI.`, `अनंत स्वरूप (1992 IRPS, अंतर्राष्ट्रीय व्यापार अनुभव): FICCI के नए महासचिव।`],
            [`Rakesh Bhanot: Appointed Acting Director General of CCI (handling IndiGo & Google antitrust cases).`, `राकेश भनोत: CCI के कार्यवाहक महानिदेशक (IndiGo व Google मामले)।`],
            [`Senior bureaucratic reshuffle: Chanchal Kumar (Information & Broadcasting), Bhuvnesh Kumar (Tourism) as new Secretaries.`, `वरिष्ठ नौकरशाही फेरबदल: चंचल कुमार (I&B), भुवनेश कुमार (पर्यटन) — नए सचिव।`],
            [`Sanjay Jamuar: First CEO of Delhi Metro International Limited.`, `संजय जमुआर: दिल्ली मेट्रो इंटरनेशनल लिमिटेड के पहले CEO।`],
            [`Ashutosh Gowariker: Festival Director of the 57th IFFI 2026.`, `आशुतोष गोवारिकर: 57वें IFFI 2026 के महोत्सव निदेशक।`],
            [`Bharat Khera (1995-batch IAS): New Secretary, Ministry of MSME.`, `भरत खेरा (1995 IAS): MSME मंत्रालय के नए सचिव।`],
            [`NITI Aayog: R. Balasubramaniam and Joram Aniya appointed as new full-time members.`, `NITI Aayog: आर. बालासुब्रमण्यम और जोरम अनिया — नए पूर्णकालिक सदस्य।`],
            [`Saurabh Vijay (1998-batch IAS): New CEO of UIDAI.`, `सौरभ विजय (1998 IAS): UIDAI के नए CEO।`],
            [`Vice Admiral Ajay Kochhar: 48th Vice Chief of Naval Staff.`, `वाइस एडमिरल अजय कोचर: 48वें नौसेना उप प्रमुख।`],
            [`Prashant Pise: India's new Ambassador to Oman.`, `प्रशांत पिसे: ओमान में भारत के नए राजदूत।`],
            [`Anugraha Narayana Das: Controller General of Defence Accounts (CGDA).`, `अनुग्रह नारायण दास: रक्षा लेखा महानियंत्रक (CGDA)।`],
            [`Dilip Kumar: Chief Vigilance Officer (CVO) of SAIL (Steel Authority of India).`, `दिलीप कुमार: SAIL (Steel Authority of India) के मुख्य सतर्कता अधिकारी।`],
            [`Ramachandra Dattatray Huddar: Chairperson, Karnataka Admission Overseeing Committee.`, `रामचंद्र दत्तात्रय हुद्दार: कर्नाटक प्रवेश निगरानी समिति के अध्यक्ष।`],
            [`May 2026: Ajit Doval reappointed as National Security Advisor for 5th consecutive term.`, `मई 2026: अजीत दोवाल को लगातार 5वीं बार राष्ट्रीय सुरक्षा सलाहकार के रूप में पुनः नियुक्त किया गया।`],
        ]
    },
    {
        emoji: "🏆",
        hi: "खेल",
        en: "Sports",
        color: "#b45309",
        light: "#fffbeb",
        border: "#fcd34d",
        items: [
            [`Anahat Singh (18): Won 2nd consecutive JSW Indian Open squash title — defeated Egyptian Hana Moataz 3-1 in the final.`, `अनाहत सिंह (18 वर्ष): JSW इंडियन ओपन स्क्वाश का लगातार दूसरा खिताब — मिस्र की हना मोआतज़ को 3-1 से हराया।`],
            [`Sheetal Devi (19, J&K): Named "Para Archer of the Year 2025" by World Archery Federation — India's first female armless para-archer.`, `शीतल देवी (19, J&K): विश्व तीरंदाजी — 'पैरा आर्चर ऑफ द ईयर 2025' — भारत की पहली निःशक्त (बिना बांह) महिला पैरा तीरंदाज।`],
            [`Andrea Kimi Antonelli (Mercedes): Won F1 Japanese GP 2026 at Suzuka — became youngest-ever F1 championship leader. Also won Canadian Grand Prix 2026.`, `एंड्रिया किमी एंटोनेली (मर्सिडीज): सुजुका में F1 जापानी GP 2026 जीता — सबसे युवा F1 चैंपियनशिप लीडर। कनाडाई GP 2026 भी जीती।`],
            [`Khelo India Tribal Games 2026: Raipur, Chhattisgarh — 3,000+ athletes from 30 states. Karnataka topped with 23 gold medals.`, `खेलो इंडिया ट्राइबल गेम्स 2026: रायपुर, छत्तीसगढ़ — 30 राज्यों से 3,000+ खिलाड़ी। कर्नाटक 23 स्वर्ण के साथ शीर्ष।`],
            [`Asian Wrestling Championships 2026, Bishkek: India won 5 medals (2 Silver, 3 Bronze) in Greco-Roman. Asian Under-23 Wrestling: India won 5 medals (2G, 2S, 1B).`, `एशियाई कुश्ती 2026, बिश्केक: ग्रीको-रोमन में 5 पदक (2 रजत, 3 कांस्य)। एशियाई U-23 कुश्ती: 5 पदक (2G, 2S, 1B)।`],
            [`Sanju Samson: ICC Men's Player of the Month for March 2026 (275 runs in 3 matches; T20 WC Player of the Tournament).`, `संजू सैमसन: मार्च 2026 के ICC पुरुष प्लेयर ऑफ द मंथ (3 मैचों में 275 रन; T20 WC टूर्नामेंट के सर्वश्रेष्ठ)।`],
            [`Melie Kerr (NZ women's captain): ICC Women's Player of the Month for March 2026 (outstanding performances vs Zimbabwe & South Africa).`, `मेली केर (NZ महिला कप्तान): मार्च 2026 की ICC महिला प्लेयर ऑफ द मंथ।`],
            [`Viktor Axelsen (Denmark, 32): Retired from professional badminton due to chronic back injuries (2× Olympic gold medalist).`, `विक्टर एक्सेलसन (डेनमार्क, 32): पुरानी पीठ की चोट के कारण पेशेवर बैडमिंटन से संन्यास (2× ओलंपिक स्वर्ण)।`],
            [`IPL 2026: Punjab Kings won the Fair Play Award. Champions received ₹20 crore prize money.`, `IPL 2026: पंजाब किंग्स को फेयर प्ले अवार्ड। चैंपियन को ₹20 करोड़ की पुरस्कार राशि।`],
            [`Asian Boxing U-15 Championships 2026: India won 27 medals including 9 gold.`, `एशियाई बॉक्सिंग U-15 चैंपियनशिप 2026: भारत ने 27 पदक जीते — 9 स्वर्ण सहित।`],
            [`Commonwealth Youth & Junior Weightlifting Championships 2026: India won 4 gold medals.`, `राष्ट्रमंडल युवा व जूनियर भारोत्तोलन चैंपियनशिप 2026: भारत ने 4 स्वर्ण पदक जीते।`],
            [`Archery World Cup Stage 2, Shanghai: Women's recurve team won gold (Deepika Kumari, Ankita Bhakat, Kumkum Mohod).`, `तीरंदाजी विश्व कप चरण 2, शंघाई: महिला रिकर्व टीम स्वर्ण (दीपिका कुमारी, अंकिता भकत, कुमकुम मोहोद)।`],
            [`Thomas Cup 2026: India won bronze — defeated Chinese Taipei 3-0 in quarterfinals.`, `थॉमस कप 2026: भारत ने कांस्य जीता — क्वार्टरफाइनल में चीनी ताइपे को 3-0 से हराया।`],
            [`Chess: Faustino Oro became 2nd youngest GM at 12 years, 6 months, 26 days. Abhimanyu Mishra still holds the all-time youngest GM record.`, `शतरंज: फॉस्टिनो ओरो 12 वर्ष 6 माह 26 दिन में दूसरे सबसे युवा GM। अभिमन्यु मिश्रा का सबसे युवा GM रिकॉर्ड अभी भी कायम।`],
            [`Hockey India Awards 2025: Hardik Singh (Male) and Navneet Kaur (Female) — Players of the Year (₹20 lakh each).`, `हॉकी इंडिया अवॉर्ड्स 2025: हरदीप सिंह (पुरुष) व नवनीत कौर (महिला) — प्लेयर ऑफ द ईयर (₹20 लाख प्रत्येक)।`],
            [`National Sports Board (NSB) established under the National Sports Governance Act.`, `राष्ट्रीय खेल शासन अधिनियम के तहत राष्ट्रीय खेल बोर्ड (NSB) का गठन।`],
            [`Stuti Pradhan (Sikkim, state-level winner of Viksit Bharat Youth Parliament 2025): Selected to represent India at the World Youth Parliament.`, `स्तुति प्रधान (सिक्किम, विकसित भारत युवा संसद 2025 विजेता): विश्व युवा संसद में भारत का प्रतिनिधित्व।`],
            [`May 2026: Indian men's hockey team won Azlan Shah Cup 2026 in Malaysia — defeating Australia 3-2 in final.`, `मई 2026: भारतीय पुरुष हॉकी टीम ने मलेशिया में आजलान शाह कप 2026 जीता — फाइनल में ऑस्ट्रेलिया को 3-2 से हराया।`],
        ]
    },
    {
        emoji: "🏅",
        hi: "पुरस्कार, संस्कृति व दिवस",
        en: "Awards, Culture & Days",
        color: "#be185d",
        light: "#fdf2f8",
        border: "#f0abfc",
        items: [
            [`PM Modi inaugurated Samrat Samprati Museum (Jain heritage, peace & non-violence) at Koba, Gandhinagar — on Mahavir Jayanti.`, `PM मोदी ने महावीर जयंती पर कोबा, गांधीनगर में सम्राट सांप्रति संग्रहालय (जैन विरासत) का उद्घाटन किया।`],
            [`Saraswati Samman 2025: Ramkumar Mukhopadhyay for Bengali novel "Hara Parbati Katha" — ₹15 lakh prize.`, `सरस्वती सम्मान 2025: रामकुमार मुखोपाध्याय — बांग्ला उपन्यास 'हरा पार्वती कथा' (₹15 लाख)।`],
            [`NHRC Short Film Competition 2025 top prize (₹2 lakh): "Rani" by Sarika Jain.`, `NHRC लघु फिल्म प्रतियोगिता 2025: सारिका जैन की 'रानी' को ₹2 लाख का प्रथम पुरस्कार।`],
            [`Rituparna Sengupta received the Women Empowerment Award for Art & Culture at UK House of Commons (International Women's Day event).`, `ऋतुपर्णा सेनगुप्ता को UK हाउस ऑफ कॉमन्स में कला व संस्कृति के लिए महिला सशक्तिकरण पुरस्कार।`],
            [`Karnataka Grameena Bank: National Award for Outstanding SHG-Bank Linkage performance (₹2,835 crore credit extended).`, `कर्नाटक ग्रामीण बैंक: उत्कृष्ट SHG-बैंक लिंकेज प्रदर्शन के लिए राष्ट्रीय पुरस्कार (₹2,835 करोड़)।`],
            [`Kailash Satyarthi (Nobel laureate) released "Karuna: The Power of Compassion" — introducing the Compassion Quotient (CQ) framework.`, `कैलाश सत्यार्थी (नोबेल पुरस्कार विजेता) ने 'करुणा: द पावर ऑफ कम्पेशन' जारी की — CQ (Compassion Quotient) ढांचा।`],
            [`Florence Nightingale Award: ₹1 lakh cash component. Sansad Ratna Award: Coal & Mines Standing Committee (chaired by Anurag Thakur).`, `फ्लोरेंस नाइटिंगेल पुरस्कार: ₹1 लाख। संसद रत्न पुरस्कार: कोयला व खान स्थायी समिति (अध्यक्ष: अनुराग ठाकुर)।`],
            [`Cambridge Dedicated Teacher Award (South Asia): Soma Mandal — for environmental education.`, `कैम्ब्रिज डेडिकेटेड टीचर अवार्ड (दक्षिण एशिया): सोमा मंडल — पर्यावरण शिक्षा।`],
            [`61st Venice Biennale (La Biennale di Venezia): India's Pavilion — "Geographies of Distance: Remembering Home".`, `61वीं वेनिस बिएनाले: भारत का पैवेलियन — 'Geographies of Distance: Remembering Home'।`],
            [`QS World University Rankings 2026: India has 99 ranked institutions; doubled top-50 subject positions. IIT Dhanbad: 21st (Mineral & Mining Engg), JNU: 26th (Development Studies).`, `QS विश्व विश्वविद्यालय रैंकिंग 2026: भारत की 99 संस्थाएं। IIT धनबाद: 21वां (खनिज-खनन), JNU: 26वां (विकास अध्ययन)।`],
            [`Yoga Mahotsav 2026: Inaugurated in Hyderabad. International Day of Yoga 2026 theme: "Yoga for Healthy Ageing" — hosted in Kolkata.`, `योग महोत्सव 2026: हैदराबाद में। अंतर्राष्ट्रीय योग दिवस 2026 थीम: 'स्वस्थ बुढ़ापे के लिए योग' — कोलकाता में।`],
            [`Sikkim: 51 years of statehood (integrated 1975). Goa: 39 years of statehood (became India's 25th state in 1987).`, `सिक्किम: राज्यत्व के 51 वर्ष (1975)। गोवा: राज्यत्व के 39 वर्ष (1987 में भारत का 25वां राज्य)।`],
            [`RISE Centre, Guntupalli: ₹1.55 crore NITI Aayog grant for rural women entrepreneurship and AI skill surveys.`, `RISE Centre, गुंटुपल्ली: ग्रामीण महिला उद्यमिता के लिए NITI Aayog से ₹1.55 करोड़ अनुदान।`],
            [`Shaheed Diwas (March 23): Commemorating the 1931 execution of Bhagat Singh, Shivaram Rajguru & Sukhdev Thapar (Lahore Conspiracy Case).`, `शहीद दिवस (23 मार्च): 1931 में भगत सिंह, शिवराम राजगुरु व सुखदेव थापर के बलिदान की स्मृति (लाहौर षड्यंत्र केस)।`],
            [`National Maritime Day (April 5): Marks 1919 maiden voyage of SS Loyalty from Mumbai to London.`, `राष्ट्रीय समुद्री दिवस (5 अप्रैल): 1919 में SS Loyalty की मुंबई से लंदन तक की पहली यात्रा।`],
            [`Ambedkar Jayanti (April 14): National holiday — Dr. B.R. Ambedkar (India's first Law Minister, chief Constitution architect).`, `अंबेडकर जयंती (14 अप्रैल): राष्ट्रीय अवकाश — डॉ. B.R. अंबेडकर (भारत के प्रथम कानून मंत्री, संविधान के मुख्य वास्तुकार)।`],
            [`Ayushman Bharat Diwas: April 30. World Homoeopathy Day (April 10, Hahnemann's birth anniversary): "Homoeopathy for Sustainable Health".`, `आयुष्मान भारत दिवस: 30 अप्रैल। विश्व होम्योपैथी दिवस (10 अप्रैल): 'सतत स्वास्थ्य के लिए होम्योपैथी'।`],
            [`Anti-Terrorism Day (May 21): In memory of former PM Rajiv Gandhi. International Museum Day: May 18.`, `राष्ट्रीय आतंकवाद विरोधी दिवस (21 मई): पूर्व PM राजीव गांधी की स्मृति में। अंतर्राष्ट्रीय संग्रहालय दिवस: 18 मई।`],
            [`International Day for Biological Diversity 2026: "Acting locally for global impact". Fire Safety Week 2026: "Safe Schools, Safe Hospitals, and a Fire-Safety Aware Society".`, `जैव विविधता दिवस 2026: 'वैश्विक प्रभाव के लिए स्थानीय कार्रवाई'। अग्नि सुरक्षा सप्ताह 2026: 'सुरक्षित स्कूल, सुरक्षित अस्पताल'।`],
            [`UN Transatlantic Slave Trade Remembrance Day (March 25): Theme — "Justice in Action: Confronting History, Advancing Dignity, Empowering Futures".`, `UN ट्रान्सअटलांटिक दास व्यापार स्मृति दिवस (25 मार्च): थीम — 'न्याय कार्रवाई में: इतिहास से सामना, गरिमा का उत्थान'।`],
            [`International Day of the Unborn Child (March 25): First officially recognized by El Salvador in 1993; coincides with Feast of the Annunciation.`, `अजन्मे बच्चे का अंतर्राष्ट्रीय दिवस (25 मार्च): 1993 में अल सल्वाडोर द्वारा पहली बार मान्यता।`],
            [`May 2026: World Press Freedom Day theme — "Press for Progress: Media and Gender Equality".`, `मई 2026: विश्व पत्रकारिता स्वतंत्रता दिवस थीम — 'प्रगति के लिए प्रेस: मीडिया और लिंग समानता'।`],
            [`May 2026: National Technology Day celebrated with focus on "AI for National Development".`, `मई 2026: राष्ट्रीय प्रौद्योगिकी दिवस को "राष्ट्रीय विकास के लिए AI" पर केंद्रित मनाया गया।`],
        ]
    },
    {
        emoji: "🕯️",
        hi: "निधन",
        en: "Obituaries",
        color: "#374151",
        light: "#f9fafb",
        border: "#d1d5db",
        items: [
            [`Asha Bhosle: Legendary playback singer passed away in Mumbai on April 12, 2026, aged 92 — multiple organ failure, 8-decade musical career.`, `आशा भोसले: महान पार्श्वगायिका का 12 अप्रैल 2026 को मुंबई में 92 वर्ष की आयु में निधन — बहु-अंग विफलता, 8 दशक का संगीत सफर।`],
            [`Oscar Schmidt ("Holy Hand"): Brazilian basketball Hall of Famer passed away aged 68.`, `ऑस्कर श्मिट ('होली हैंड'): ब्राजीलियाई बास्केटबॉल हॉल ऑफ फेमर का 68 वर्ष की आयु में निधन।`],
            [`Dr. Gopalrao Patil: Educationist, child specialist & former BJP Rajya Sabha member passed away.`, `डॉ. गोपालराव पाटिल: शिक्षाविद, बाल रोग विशेषज्ञ व पूर्व BJP राज्यसभा सदस्य का निधन।`],
            [`M.J.K. Smith: Former England cricket captain passed away aged 92.`, `M.J.K. स्मिथ: पूर्व इंग्लैंड क्रिकेट कप्तान का 92 वर्ष की आयु में निधन।`],
            [`Jennifer Paes: Mother of Indian tennis legend Leander Paes passed away.`, `जेनिफर पेस: भारतीय टेनिस दिग्गज लिएंडर पेस की माता का निधन।`],
            [`Ted Turner: Founder of CNN (world's first 24-hour news channel) passed away aged 87.`, `टेड टर्नर: CNN (विश्व के पहले 24 घंटे के समाचार चैनल) के संस्थापक का 87 वर्ष की आयु में निधन।`],
            [`Bashir Badr: Veteran Urdu poet passed away aged 91 in Bhopal.`, `बशीर बद्र: वरिष्ठ उर्दू शायर का भोपाल में 91 वर्ष की आयु में निधन।`],
            [`Dhanendra Kumar: First Chairman of the Competition Commission of India (CCI) passed away.`, `धनेंद्र कुमार: भारतीय प्रतिस्पर्धा आयोग (CCI) के प्रथम अध्यक्ष का निधन।`],
            [`Soma Somasegar: Leader who established Microsoft's India Development Center in Hyderabad in 1998 passed away.`, `सोमा सोमसेगर: 1998 में हैदराबाद में माइक्रोसॉफ्ट इंडिया डेवलपमेंट सेंटर स्थापित करने वाले — का निधन।`],
        ]
    }
];

const total = CATS.reduce((s, c) => s + c.items.length, 0);

export default function App() {
    const [active, setActive] = useState(0);
    const [search, setSearch] = useState("");
    const [lang, setLang] = useState("both");

    const cat = CATS[active];

    const filtered = useMemo(() => {
        if (!search.trim()) return cat.items.map((item, i) => ({ item, idx: i }));
        const q = search.toLowerCase();
        return cat.items
            .map((item, i) => ({ item, idx: i }))
            .filter(({ item: [en, hi] }) =>
                en.toLowerCase().includes(q) || hi.includes(search)
            );
    }, [active, search, cat.items]);

    return (
        <div style={{
            fontFamily: "'Segoe UI', 'Noto Sans Devanagari', Arial, sans-serif",
            background: "#f8fafc",
            minHeight: "100vh",
            padding: "0 0 40px 0"
        }}>
            {/* Header */}
            <div style={{
                background: "linear-gradient(135deg, #1e293b 0%, #334155 100%)",
                padding: "18px 20px 14px",
                color: "white",
                textAlign: "center"
            }}>
                <div style={{ fontSize: 22, fontWeight: 800, letterSpacing: "-0.5px" }}>
                    📰 Current Affairs 2026
                </div>
                <div style={{ fontSize: 13, opacity: 0.8, marginTop: 2 }}>
                    समसामयिक घटनाएं | Bilingual Reference (Mar–Jun 2026)
                </div>
                <div style={{ fontSize: 11, opacity: 0.55, marginTop: 4 }}>
                    {total} facts · {CATS.length} categories · EN + हिन्दी
                </div>
            </div>

            {/* Controls */}
            <div style={{ padding: "12px 16px 0", display: "flex", gap: 8, flexWrap: "wrap" }}>
                <input
                    type="text"
                    placeholder="🔍  Search / खोजें..."
                    value={search}
                    onChange={e => setSearch(e.target.value)}
                    style={{
                        flex: 1, minWidth: 180, padding: "9px 14px",
                        border: "1.5px solid #e2e8f0", borderRadius: 10,
                        fontSize: 14, background: "white", outline: "none",
                        boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
                    }}
                />
                <select
                    value={lang}
                    onChange={e => setLang(e.target.value)}
                    style={{
                        padding: "9px 14px", border: "1.5px solid #e2e8f0",
                        borderRadius: 10, fontSize: 13, background: "white",
                        cursor: "pointer", boxShadow: "0 1px 3px rgba(0,0,0,0.06)"
                    }}
                >
                    <option value="both">EN + हिन्दी</option>
                    <option value="en">English only</option>
                    <option value="hi">हिन्दी only</option>
                </select>
            </div>

            {/* Tabs */}
            <div style={{
                display: "flex", gap: 6, overflowX: "auto",
                padding: "12px 16px 0", scrollbarWidth: "none"
            }}>
                {CATS.map((c, i) => (
                    <button
                        key={i}
                        onClick={() => { setActive(i); setSearch(""); }}
                        style={{
                            padding: "7px 13px", borderRadius: 20,
                            border: active === i ? "none" : "1.5px solid #e2e8f0",
                            cursor: "pointer", whiteSpace: "nowrap",
                            background: active === i ? c.color : "white",
                            color: active === i ? "white" : "#374151",
                            fontWeight: active === i ? 700 : 500,
                            fontSize: 12.5,
                            boxShadow: active === i ? `0 2px 8px ${c.color}55` : "0 1px 2px rgba(0,0,0,0.05)",
                            transition: "all 0.18s"
                        }}
                    >
                        {c.emoji} {c.hi}
                    </button>
                ))}
            </div>

            {/* Category banner */}
            <div style={{
                margin: "12px 16px 0",
                background: cat.light,
                border: `1.5px solid ${cat.border}`,
                borderLeft: `5px solid ${cat.color}`,
                borderRadius: "0 10px 10px 0",
                padding: "10px 14px",
                display: "flex", alignItems: "center", justifyContent: "space-between"
            }}>
                <div>
                    <span style={{ fontSize: 15, fontWeight: 700, color: cat.color }}>
                        {cat.emoji} {cat.hi}
                    </span>
                    <span style={{ fontSize: 12.5, color: "#64748b", marginLeft: 8 }}>
                        / {cat.en}
                    </span>
                </div>
                <span style={{
                    background: cat.color, color: "white",
                    borderRadius: 12, padding: "2px 10px", fontSize: 12, fontWeight: 700
                }}>
                    {filtered.length} / {cat.items.length}
                </span>
            </div>

            {/* Items */}
            <div style={{ padding: "10px 16px 0", display: "flex", flexDirection: "column", gap: 8 }}>
                {filtered.length === 0 && (
                    <div style={{
                        textAlign: "center", color: "#94a3b8",
                        padding: "40px 20px", fontSize: 14
                    }}>
                        No results · कोई परिणाम नहीं
                    </div>
                )}
                {filtered.map(({ item: [en, hi], idx }) => (
                    <div
                        key={idx}
                        style={{
                            background: "white",
                            border: "1px solid #e2e8f0",
                            borderLeft: `4px solid ${cat.color}`,
                            borderRadius: "0 10px 10px 0",
                            padding: "11px 14px",
                            display: "flex", gap: 10, alignItems: "flex-start",
                            boxShadow: "0 1px 3px rgba(0,0,0,0.04)"
                        }}
                    >
                        <span style={{
                            minWidth: 22, height: 22,
                            background: cat.light,
                            color: cat.color,
                            border: `1.5px solid ${cat.border}`,
                            borderRadius: "50%",
                            display: "flex", alignItems: "center", justifyContent: "center",
                            fontSize: 10.5, fontWeight: 800, flexShrink: 0, marginTop: 1
                        }}>
                            {idx + 1}
                        </span>
                        <div style={{ flex: 1 }}>
                            {(lang === "en" || lang === "both") && (
                                <p style={{
                                    margin: 0, fontSize: 13.5, color: "#0f172a",
                                    lineHeight: 1.65, fontWeight: 500
                                }}>
                                    {en}
                                </p>
                            )}
                            {lang === "both" && (
                                <div style={{
                                    height: 1, background: "#f1f5f9",
                                    margin: "7px 0"
                                }} />
                            )}
                            {(lang === "hi" || lang === "both") && (
                                <p style={{
                                    margin: 0, fontSize: 13, color: "#334155",
                                    lineHeight: 1.75
                                }}>
                                    {hi}
                                </p>
                            )}
                        </div>
                    </div>
                ))}
            </div>

            {/* Footer */}
            <div style={{
                marginTop: 20, textAlign: "center",
                fontSize: 11, color: "#94a3b8"
            }}>
                {CATS.map(c => `${c.emoji} ${c.items.length}`).join("  ·  ")}
            </div>
        </div>
    );
}