import os
import re

BASE_DIR = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\modern_history\Arrival-of-Europeans-in-India\Portuguese-De-Almeida"
db_script_path = os.path.join(BASE_DIR, "generate_almeida_db.py")

# Clean up previously injected overrides in generate_almeida_db.py to avoid duplicates
if os.path.exists(db_script_path):
    with open(db_script_path, "r", encoding="utf-8") as f:
        code = f.read()
    
    # Remove any previous injection blocks
    code = re.sub(r"# Injecting updated UPSC deep dives and practice questions.*?hi_data\['deepDive'\]\['sections'\]\[4\]\['masteryZone'\] = sec5_hi", "", code, flags=re.DOTALL)
    code = re.sub(r"# Injecting updated UPSC deep dives and practice questions.*?hi_data\['deepDive'\] = \{deep_dive_hi_str\}", "", code, flags=re.DOTALL)
    
    # Let's save the cleaned code first
    with open(db_script_path, "w", encoding="utf-8") as f:
        f.write(code)

# The new UPSC-style practice questions (50 Qs)
# 25 Multi-Statement, 15 Matching, 10 Assertion-Reason
practice_code = '''def make_practice_questions():
    en = []
    hi = []

    # Statement-Based Options
    st_opts_1 = ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"]
    st_opts_1_hi = ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"]

    st_opts_2 = ["Only one statement is correct", "Only two statements are correct", "All three statements are correct", "None of the statements are correct"]
    st_opts_2_hi = ["केवल एक कथन सही है", "केवल दो कथन सही हैं", "सभी तीन कथन सही हैं", "कोई भी कथन सही नहीं है"]

    en_ar_opts = [
        "Both A and R are true and R is the correct explanation of A",
        "Both A and R are true but R is not the correct explanation of A",
        "A is true but R is false",
        "A is false but R is true"
    ]
    hi_ar_opts = [
        "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
        "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
        "A सही है लेकिन R गलत है",
        "A गलत है लेकिन R सही है"
    ]

    # 1. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the establishment of the Estado da Índia in 1505, consider the following statements:
1. It was established as a permanent crown administrative and military state rather than a temporary trading enterprise.
2. Francisco de Almeida was given a non-renewable five-year term as the first Viceroy.
3. The Viceroy was granted absolute financial autonomy, independent of the Casa da Índia in Lisbon.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statement 1 is correct. King Manuel I established the Estado da Índia as a permanent administrative state. Statement 2 is incorrect; Almeida's term was strictly three years to prevent the consolidation of autonomous power. Statement 3 is incorrect; scribes and factors reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's financial control."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1505 में 'एस्टाडो दा इंडिया' की स्थापना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. इसे एक अस्थायी व्यापारिक उद्यम के बजाय एक स्थायी शाही प्रशासनिक और सैन्य राज्य के रूप में स्थापित किया गया था।
2. फ्रांसिस्को डी अल्मेडा को पहले वायसराय के रूप में पांच वर्ष का गैर-नवीकरणीय कार्यकाल दिया गया था।
3. वायसराय को लिस्बन में कासा दा इंडिया से स्वतंत्र, पूर्ण वित्तीय स्वायत्तता प्रदान की गई थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 सही है। राजा मैनुअल प्रथम ने स्थायी प्रशासनिक राज्य के रूप में इसकी स्थापना की। कथन 2 गलत है क्योंकि अल्मेडा का कार्यकाल तीन वर्ष था। कथन 3 गलत है क्योंकि लेखक और कारक सीधे लिस्बन को रिपोर्ट करते थे।"
    })

    # 2. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the strategic objectives of the Portuguese Crown in the Indian Ocean:
1. To establish a total monopoly over the lucrative spice trade by eliminating Arab and Venetian middlemen.
2. To control key oceanic choke points, including the Strait of Malacca and the Persian Gulf, during Almeida's tenure.
3. To enforce a legal naval licensing system on all merchant vessels navigating the Indian Ocean.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. The goals were monopoly and licensing (Cartaz). Statement 2 is incorrect; controlling Malacca and the Persian Gulf was Albuquerque's strategy, not Almeida's, who focused solely on the Indian coastal routes and the Red Sea mouth."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """हिंद महासागर में पुर्तगाली क्राउन के रणनीतिक उद्देश्यों के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. अरब और वेनिस के बिचौलियों को समाप्त करके आकर्षक मसाला व्यापार पर पूर्ण एकाधिकार स्थापित करना।
2. अल्मेडा के कार्यकाल के दौरान मलक्का जलडमरूमध्य और फारस की खाड़ी सहित प्रमुख समुद्री चोक पॉइंट को नियंत्रित करना।
3. हिंद महासागर में नौवहन करने वाले सभी व्यापारिक जहाजों पर एक कानूनी नौसैनिक लाइसेंसिंग प्रणाली लागू करना।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। एकाधिकार और लाइसेंस (कार्टाज) इसके उद्देश्य थे। कथन 2 गलत है क्योंकि मलक्का और फारस की खाड़ी को नियंत्रित करना अल्बुकर्क की रणनीति थी, अल्मेडा की नहीं।"
    })

    # 3. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to Francisco de Almeida's Blue Water Policy, consider the following statements:
1. It prioritized naval supremacy and the control of shipping lanes over territorial land acquisition in India.
2. It was based on the premise that Portugal had sufficient manpower to defend mainland Indian fortresses if needed.
3. It was formally rejected by his successor, Afonso de Albuquerque, who advocated for land-based colonial bases.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. The Blue Water Policy focused on naval dominance and sea lane control, avoiding territorial conquests. Statement 2 is incorrect; it was based on the premise that Portugal's small population and limited resources could NOT support a land empire. Albuquerque shifted to land-based territorial bases."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """फ्रांसिस्को डी अल्मेडा की 'नीले पानी की नीति' (ब्लू वाटर पॉलिसी) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. इसने भारत में क्षेत्रीय भूमि अधिग्रहण के बजाय नौसैनिक वर्चस्व और नौवहन मार्गों के नियंत्रण को प्राथमिकता दी।
2. यह इस आधार पर आधारित था कि पुर्तगाल के पास जरूरत पड़ने पर मुख्य भूमि भारतीय किलों की रक्षा के लिए पर्याप्त जनशक्ति थी।
3. इसे उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क द्वारा औपचारिक रूप से खारिज कर दिया गया था, जिन्होंने भूमि-आधारित औपनिवेशिक ठिकानों की वकालत की थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। नीले पानी की नीति ने नौसैनिक प्रभुत्व पर ध्यान केंद्रित किया। कथन 2 गलत है क्योंकि अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या भूमि साम्राज्य की रक्षा नहीं कर सकती।"
    })

    # 4. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Cartaz system:
1. Rulers allied with the Portuguese, including the Raja of Cochin, were exempt from obtaining Cartazes.
2. Merchant ships holding a Cartaz were prohibited from carrying pepper, ginger, and weapons.
3. Any vessel intercepted without a Cartaz was subject to cargo confiscation and execution or enslavement of the crew.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Cartaz prohibited carrying pepper, ginger, and arms, and unauthorized vessels faced severe penalties. Statement 1 is incorrect; even allied rulers like the Raja of Cochin had to secure Cartazes for their ships."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """कार्टाज प्रणाली के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. कोचीन के राजा सहित पुर्तगालियों के साथ गठबंधन करने वाले शासकों को कार्टाज प्राप्त करने से छूट दी गई थी।
2. कार्टाज धारक व्यापारिक जहाजों को काली मिर्च, अदरक और हथियारों के परिवहन की मनाही थी।
3. बिना कार्टाज के पकड़े गए किसी भी जहाज की सामग्री को जब्त कर लिया जाता था और चालक दल को मार दिया जाता था या गुलाम बना लिया जाता था।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। कार्टाज में काली मिर्च, अदरक और हथियार ले जाने पर प्रतिबंध था। कथन 1 गलत है क्योंकि कोचीन के सहयोगी राजा को भी कार्टाज लेना पड़ता था।"
    })

    # 5. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the fortifications built during Almeida's viceroyalty, consider the following statements:
1. Fort São Tiago was constructed in Kilwa to secure passage and control the gold trade coming from Sofala.
2. Fort Manuel in Cochin was built in alliance with the local Trimumpara Raja to counter the Zamorin of Calicut.
3. Fort St. Angelo was built in Cannanore to regulate the trade of Malabar ginger and horse imports.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 3,
        "sol": "All three statements are correct. Almeida established Fort São Tiago in Kilwa (1505) for Swahili trade, Fort Manuel in Cochin (1505) for alliance protection, and Fort St. Angelo in Cannanore (1505) to regulate ginger and horse imports."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अल्मेडा के कार्यकाल के दौरान निर्मित किलों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. सोफाला से आने वाले सोने के व्यापार को नियंत्रित करने और मार्ग सुरक्षित करने के लिए किलवा में फोर्ट साओ टियागो का निर्माण किया गया था।
2. कालीकट के ज़मोरिन का मुकाबला करने के लिए स्थानीय त्रिमुम्पारा राजा के साथ गठबंधन में कोचीन में फोर्ट मैनुअल का निर्माण किया गया था।
3. मालाबार अदरक व्यापार और घोड़ों के आयात को विनियमित करने के लिए कन्नूर में फोर्ट सेंट एंजेलो का निर्माण किया गया था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 3,
        "sol": "सभी तीन कथन सही हैं। अल्मेडा ने किलवा (1505), कोचीन (1505) और कन्नूर (1505) में इन किलों की स्थापना की।"
    })

    # 6. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Anjadip Fort:
1. It was built on Anjadip Island off the coast of Goa to secure a fresh water station and repair facility.
2. The fort was ordered to be reinforced and expanded by Almeida in 1508.
3. Constant raids from the Adil Shahi Sultanate of Bijapur made the fort unsustainable.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Anjadip Fort was built in 1505 for water supply and ship repair, but was frequently attacked by Bijapur forces. Statement 2 is incorrect; due to high maintenance costs and raids, Almeida ordered the fort's demolition and abandonment in 1506, not reinforcement in 1508."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अंजादीप किले के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसे मीठे पानी की आपूर्ति और जहाजों की मरम्मत की सुविधा सुरक्षित करने के लिए गोवा के तट के पास अंजादीप द्वीप पर बनाया गया था।
2. अल्मेडा द्वारा 1508 में इस किले को मजबूत और विस्तारित करने का आदेश दिया गया था।
3. बीजापुर के आदिल शाही सल्तनत के लगातार हमलों ने इस किले को बनाए रखना असंभव बना दिया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। अंजादीप किला आदिल शाही हमलों के कारण असुरक्षित था। कथन 2 गलत है क्योंकि अल्मेडा ने 1506 में इसे नष्ट करने का आदेश दिया था।"
    })

    # 7. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Battle of Chaul (1508), consider the following statements:
1. The Portuguese patrol fleet was commanded by Lourenço de Almeida, the Viceroy's only son.
2. The Portuguese fleet suffered a crushing defeat, marking their first major naval loss in the Indian Ocean.
3. The conflict was triggered by the disruption of the spice trade of the Mamluk Sultanate of Egypt.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 3,
        "sol": "All three statements are correct. The Mamluk Sultanate constructed a fleet to stop the Portuguese Red Sea blockades. They surprised Lourenço's patrol fleet at Chaul in 1508, resulting in his death and the first major Portuguese defeat."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई (1508) के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. पुर्तगाली गश्ती बेड़े की कमान वायसराय के इकलौते पुत्र लॉरेंको डी अल्मेडा के हाथ में थी।
2. पुर्तगाली बेड़े को करारी हार का सामना करना पड़ा, जो हिंद महासागर में उनकी पहली बड़ी नौसैनिक हार थी।
3. यह संघर्ष मिस्र के ममलुक सल्तनत के मसाला व्यापार में व्यवधान के कारण शुरू हुआ था।
उपर्युक्त कथनों में से कौन-sa/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 3,
        "sol": "सभी तीन कथन सही हैं। ममलुक सल्तनत ने पुर्तगाली नाकेबंदी को रोकने के लिए बेड़ा बनाया और 1508 में चोल में लॉरेंको के बेड़े को पराजित किया।"
    })

    # 8. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Diu (1509):
1. Francisco de Almeida personally led the Portuguese armada to avenge the death of his son.
2. The Portuguese fleet engaged a combined naval coalition of the Mamluks, the Ottoman Empire, and the Gujarat Sultanate.
3. The battle ended in a stalemate, leaving the Arabian Sea trade routes contested.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida led the retaliatory campaign against the Mamluk-Ottoman-Gujarati coalition. Statement 3 is incorrect; the Battle of Diu ended in a decisive Portuguese victory, destroying the coalition fleet and establishing European naval hegemony."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव की लड़ाई (1509) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. फ्रांसिस्को डी अल्मेडा ने अपने पुत्र की मृत्यु का बदला लेने के लिए व्यक्तिगत रूप से पुर्तगाली बेड़े का नेतृत्व किया।
2. पुर्तगाली बेड़े ने ममलुक, ओटोमन साम्राज्य और गुजरात सल्तनत के संयुक्त नौसैनिक गठबंधन का मुकाबला किया।
3. युद्ध का अंत एक गतिरोध के रूप में हुआ, जिससे अरब सागर व्यापार मार्ग विवादित रह गए।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा ने गठबंधन के खिलाफ प्रतिशोध अभियान का नेतृत्व किया। कथन 3 गलत है क्योंकि दीव की लड़ाई पुर्तगालियों की निर्णायक जीत में समाप्त हुई।"
    })

    # 9. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the geopolitical forces involved in the Battle of Chaul, consider the following statements:
1. The Republic of Venice secretly supplied shipbuilding timber to the Mamluks at Alexandria.
2. Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, allied with the Mamluk forces.
3. The Zamorin of Calicut supported the Portuguese patrol fleet against the Egyptian invasion.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Venice supplied timber to Suez to help Mamluks rebuild spice routes, and Malik Ayyaz allied with Amir Husain Al-Kurdi. Statement 3 is incorrect; the Zamorin of Calicut was allied with the Mamluk-Gujarati coalition against the Portuguese."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई में शामिल भू-राजनीतिक ताकतों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. वेनिस गणराज्य ने अलेक्जेंड्रिया में ममलुकों को गुप्त रूप से जहाज निर्माण की लकड़ी की आपूर्ति की।
2. गुजरात सल्तनत के तहत दीव के गवर्नर मलिक अय्याज़ ने ममलुक सेना के साथ गठबंधन किया।
3. कालीकट के ज़मोरिन ने मिस्र के आक्रमण के खिलाफ पुर्तगाली गश्ती बेड़े का समर्थन किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। वेनिस ने ममलुकों की मदद की और मलिक अय्याज़ ने उनके साथ गठबंधन किया। कथन 3 गलत है क्योंकि ज़मोरिन पुर्तगालियों के विरोधी गठबंधन में शामिल था।"
    })

    # 10. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the succession dispute between Almeida and Albuquerque in late 1508:
1. Almeida refused to hand over power, claiming Albuquerque's letters patent were invalid.
2. Albuquerque was imprisoned in Fort Manuel in Cochin by Almeida's orders.
3. The Portuguese Crown eventually recalled Albuquerque and reinstated Almeida for a second term.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida refused to hand over power and imprisoned Albuquerque until he could avenge his son at Diu. Statement 3 is incorrect; after the Battle of Diu, Almeida released Albuquerque, handed over power, and sailed for Europe."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1508 के अंत में अल्मेडा और अल्बुकर्क के बीच उत्तराधिकार विवाद के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. अल्मेडा ने यह दावा करते हुए सत्ता सौंपने से इनकार कर दिया कि अल्बुकर्क के पत्र अमान्य थे।
2. अल्मेडा के आदेश पर अल्बुकर्क को कोचीन के फोर्ट मैनुअल में कैद कर दिया गया था।
3. पुर्तगाली क्राउन ने अंततः अल्बुकर्क को वापस बुला लिया और अल्मेडा को दूसरे कार्यकाल के लिए बहाल किया।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा ने बदला लेने तक सत्ता सौंपने से मना किया और अल्बुकर्क को कैद किया। कथन 3 गलत है क्योंकि दीव की लड़ाई के बाद अल्मेडा ने अल्बुकर्क को सत्ता सौंप दी।"
    })

    # 11. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the death of Francisco de Almeida, consider the following statements:
1. He died in a naval battle against the Ottoman fleet in the Red Sea.
2. He was killed in a beach skirmish with Khoikhoi natives at Table Bay, South Africa.
3. His death occurred in March 1510 during his return voyage to Portugal.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Almeida was killed on March 1, 1510, in a skirmish with Khoikhoi natives over cattle and water at Table Bay, South Africa, during his return voyage. Statement 1 is incorrect."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """फ्रांसिस्को डी अल्मेडा की मृत्यु के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. लाल सागर में ओटोमन बेड़े के खिलाफ एक नौसैनिक युद्ध में उनकी मृत्यु हुई थी।
2. वह दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ एक तट पर झड़प में मारे गए थे।
3. उनकी मृत्यु मार्च 1510 में पुर्तगाल की उनकी वापसी यात्रा के दौरान हुई थी।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। अल्मेडा की मृत्यु 1 मार्च, 1510 को टेबल बे में खोइखोई आदिवासियों के साथ एक झड़प में हुई थी।"
    })

    # 12. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding Malik Ayyaz:
1. He was an ethnic Ottoman noble who served the Gujarat Sultanate.
2. He served as the governor of Diu under Sultan Mahmud Begarha.
3. He commanded the Gujarati fleet that supported Amir Husain Al-Kurdi at Chaul and Diu.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Malik Ayyaz was governor of Diu under Sultan Mahmud Begarha and commanded the local gunboats in the battles. Statement 1 is incorrect; he was a slave convert of Russian origin, not an ethnic Ottoman noble."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """मलिक अय्याज़ के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. वह एक जातीय ओटोमन रईस था जिसने गुजरात सल्तनत की सेवा की थी।
2. उसने सुल्तान महमूद बेगड़ा के तहत दीव के गवर्नर के रूप में कार्य किया।
3. उसने गुजराती बेड़े की कमान संभाली जिसने चोल और दीव में अमीर हुसैन अल-कुर्दी का समर्थन किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। मलिक अय्याज़ सुल्तान महमूद बेगड़ा के अधीन दीव का गवर्नर था। कथन 1 गलत है क्योंकि वह रूसी मूल का दास था, ओटोमन रईस नहीं।"
    })

    # 13. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the legal and navigational terms introduced by the Portuguese, consider the following statements:
1. Mare Clausum refers to the doctrine of the Free Sea, open to all merchant nations.
2. Volta do Mar was a sailing maneuver used to navigate around adverse Atlantic currents.
3. Feitoria was a fortified trading post or warehouse established to store monopoly goods.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Volta do Mar was a critical navigation loop, and Feitoria was the trade warehouse. Statement 1 is incorrect; Mare Clausum refers to the Closed Sea doctrine (exclusive sovereignty), while Mare Liberum refers to the Free Sea."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पुर्तगालियों द्वारा शुरू किए गए कानूनी और नौवहन शब्दों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. मारे क्लॉसम (Mare Clausum) मुक्त समुद्र के सिद्धांत को संदर्भित करता है, जो सभी व्यापारी देशों के लिए खुला हो।
2. वोल्टा डो मार (Volta do Mar) अटलांटिक की प्रतिकूल धाराओं से बचने के लिए इस्तेमाल की जाने वाली एक नौवहन तकनीक थी।
3. फेइटोरिया (Feitoria) एकाधिकार वस्तुओं के भंडारण के लिए स्थापित एक किला नुमा व्यापारिक केंद्र या गोदाम था।
उपर्युक्त कथनों में से कौन-sa/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। वोल्टा डो मार नौवहन तकनीक थी और फेइटोरिया व्यापारिक गोदाम था। कथन 1 गलत है क्योंकि मारे क्लॉसम बंद समुद्र (पुर्तगाली एकाधिकार) को दर्शाता है।"
    })

    # 14. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the 1507 Siege of Cannanore:
1. It was launched by the Kolathiri Raja of Cannanore with the military backing of the Zamorin of Calicut.
2. The Portuguese garrison at Fort St. Angelo was successfully defended by Lourenço de Almeida.
3. The siege ended when a Portuguese reinforcement fleet led by Tristão da Cunha arrived to relieve the garrison.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. The siege was led by Kolathiri forces backed by Calicut, and ended with the arrival of Tristão da Cunha's fleet. Statement 2 is incorrect; the garrison at Cannanore was commanded by Lourenço de Brito, not Lourenço de Almeida, who was patrolling elsewhere."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1507 के कन्नूर की घेराबंदी (Siege of Cannanore) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसे कालीकट के ज़मोरिन के सैन्य समर्थन से कन्नूर के कोलथिरि राजा द्वारा शुरू किया गया था।
2. फोर्ट सेंट एंजेलो में पुर्तगाली गैरीसन की रक्षा लॉरेंको डी अल्मेडा ने सफलतापूर्वक की थी।
3. घेराबंदी तब समाप्त हुई जब गैरीसन को राहत देने के लिए ट्रिस्टाओ दा कुन्हा के नेतृत्व में एक पुर्तगाली सुदृढीकरण बेड़ा आया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। घेराबंदी को ट्रिस्टाओ दा कुन्हा के बेड़े ने समाप्त किया। कथन 2 गलत है क्योंकि कन्नूर गैरीसन कमांडर लॉरेंको डी ब्रिटो थे, लॉरेंको डी अल्मेडा नहीं।"
    })

    # 15. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the composition of the 1505 viceregal expedition, consider the following statements:
1. The fleet carried noblemen, military officers, and specialized Franciscan missionaries.
2. It was the first Portuguese expedition to bring stone and masonry ballast to construct permanent fortifications.
3. The expedition was funded entirely by private Italian banks without Crown backing.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. The fleet carried noblemen and missionaries, and brought building materials for permanent forts. Statement 3 is incorrect; the expedition was commissioned and backed by the Portuguese Crown (King Manuel I), though some foreign merchants participated."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """1505 के वायसराय अभियान की संरचना के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. बेड़े में रईस, सैन्य अधिकारी और विशेष फ्रांसिस्कन मिशनरी शामिल थे।
2. स्थायी किलों के निर्माण के लिए पत्थर और निर्माण सामग्री ले जाने वाला यह पहला पुर्तगाली अभियान था।
3. यह अभियान पूरी तरह से बिना क्राउन समर्थन के निजी इतालवी बैंकों द्वारा वित्त पोषित था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। यह अभियान शाही समर्थन से भेजा गया था, इसलिए कथन 3 गलत है।"
    })

    # 16. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Toro (1476):
1. Francisco de Almeida gained outstanding military renown in Europe during this battle.
2. It was fought as part of the Castilian War of Succession.
3. Almeida commanded the Castilian forces against the Portuguese Crown.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. Almeida gained renown in the Battle of Toro (1476), which was fought during the War of the Castilian Succession. Statement 3 is incorrect; Almeida fought on the Portuguese side supporting King Afonso V, not on the Castilian side."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """टोरो की लड़ाई (1476) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. फ्रांसिस्को डी अल्मेडा ने इस लड़ाई के दौरान यूरोप में उत्कृष्ट सैन्य ख्याति प्राप्त की थी।
2. यह कैस्टिलियन उत्तराधिकार के युद्ध के हिस्से के रूप में लड़ा गया था।
3. अल्मेडा ने पुर्तगाली क्राउन के खिलाफ कैस्टिलियन सेना की कमान संभाली थी।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। टोरो का युद्ध कैस्टिलियन उत्तराधिकार युद्ध का हिस्सा था। कथन 3 गलत है क्योंकि अल्मेडा ने पुर्तगाली राजा का समर्थन किया था, न कि कैस्टिल का।"
    })

    # 17. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the strategic position of Cochin in early Portuguese planning, consider the following statements:
1. Cochin served as the first headquarters of the Portuguese Estado da Índia.
2. The Portuguese built Fort Manuel there to dominate the spice trade of Calicut directly.
3. The Raja of Cochin was an independent sovereign who welcomed the Portuguese to gain autonomy from the Zamorin.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. Cochin was the first capital, and its Raja allied with the Portuguese to escape Zamorin suzerainty. Statement 2 is incorrect; Fort Manuel was built to protect the factory in Cochin and control Cochin's own trade, not Calicut's direct trade, which was blockaded."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """प्रारंभिक पुर्तगाली योजना में कोचीन की रणनीतिक स्थिति के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. कोचीन ने पुर्तगाली एस्टाडो दा इंडिया के पहले मुख्यालय के रूप में कार्य किया।
2. पुर्तगालियों ने सीधे कालीकट के मसाला व्यापार पर हावी होने के लिए वहाँ फोर्ट मैनुअल का निर्माण किया था।
3. कोचीन के राजा एक स्वतंत्र संप्रभु थे जिन्होंने ज़मोरिन से स्वायत्तता प्राप्त करने के लिए पुर्तगालियों का स्वागत किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। कोचीन पहला मुख्यालय था और राजा ने ज़मोरिन के खिलाफ पुर्तगाली गठबंधन स्वीकार किया। कथन 2 गलत है क्योंकि यह किला कोचीन के व्यापार की रक्षा के लिए था, न कि सीधे कालीकट के लिए।"
    })

    # 18. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the role of the Portuguese Scribe (Escrivão) and Factor (Feitor):
1. Scribes were administrative officers who recorded cargo details and trade transactions.
2. Factors reported directly to the Viceroy and could be dismissed by him at will.
3. This division of power acted as a check against corruption and autonomous revolt by the Viceroy.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Scribes recorded cargo, and the system checked the Viceroy's power. Statement 2 is incorrect; factors and scribes in India reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's administrative control."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पुर्तगाली लेखक (Escrivão) और कारक (Feitor) की भूमिका के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. लेखक प्रशासनिक अधिकारी थे जो कार्गो विवरण और व्यापारिक लेनदेन दर्ज करते थे।
2. कारक सीधे वायसराय को रिपोर्ट करते थे और उन्हें वायसराय द्वारा बर्खास्त किया जा सकता था।
3. सत्ता के इस विभाजन ने भ्रष्टाचार और वायसराय द्वारा स्वायत्त विद्रोह के खिलाफ एक जांच के रूप में कार्य किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। यह व्यवस्था भ्रष्टाचार रोकने के लिए थी। कथन 2 गलत है क्योंकि लेखक और कारक सीधे लिस्बन को रिपोर्ट करते थे, न कि वायसराय को।"
    })

    # 19. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Mamluk Sultanate's involvement in the Indian Ocean, consider the following statements:
1. The Mamluks were secretly aided by the Republic of Genoa, which provided financial loans.
2. Amir Husain Al-Kurdi was commissioned to build and command the Egyptian fleet at Suez.
3. The Mamluk naval intervention aimed to restore their transit trade customs revenues.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 1,
        "sol": "Statements 2 and 3 are correct. Amir Husain built the Suez fleet, and the Mamluks aimed to reclaim transit duties. Statement 1 is incorrect; they were secretly aided by Venice (which supplied timber), not Genoa."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """हिंद महासागर में ममलुक सल्तनत की भागीदारी के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. ममलुकों को गुप्त रूप से जेनोआ गणराज्य द्वारा सहायता प्रदान की गई थी, जिसने वित्तीय ऋण प्रदान किए थे।
2. अमीर हुसैन अल-कुर्दी को स्वेज में मिस्र के बेड़े का निर्माण करने और उसकी कमान संभालने के लिए नियुक्त किया गया था।
3. ममलुक नौसैनिक हस्तक्षेप का उद्देश्य उनके पारगमन व्यापार सीमा शुल्क राजस्व को बहाल करना था।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 1,
        "sol": "कथन 2 और 3 सही हैं। अमीर हुसैन ने स्वेज बेड़े की कमान संभाली और ममलुक पारगमन कर बहाल करना चाहते थे। कथन 1 गलत है क्योंकि उन्हें वेनिस ने लकड़ी दी थी, न कि जेनोआ ने।"
    })

    # 20. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Diu (1509):
1. The Portuguese fleet utilized superior long-range artillery that prevented coalition boarding actions.
2. The coalition forces had a clear numerical superiority in terms of combat vessels.
3. Following the battle, the Portuguese immediately annexed Diu and built a massive land fortress.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. The Portuguese used long-range cannons to keep high-walled vessels safe from coalition boarding, despite being outnumbered. Statement 3 is incorrect; Almeida did not annex Diu; he signed a peace treaty with Malik Ayyaz. Diu was annexed much later under Albuquerque and Nuno da Cunha."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव की लड़ाई (1509) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. पुर्तगाली बेड़े ने बेहतर लंबी दूरी की तोपों का इस्तेमाल किया जिसने गठबंधन को उनके जहाजों पर चढ़ने से रोका।
2. गठबंधन सेना के पास लड़ाकू जहाजों के मामले में स्पष्ट संख्यात्मक श्रेष्ठता थी।
3. युद्ध के बाद, पुर्तगालियों ने तुरंत दीव पर कब्जा कर लिया और एक विशाल भूमि किला बनाया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। पुर्तगाली तोपखाना श्रेष्ठ था। कथन 3 गलत है क्योंकि दीव पर तुरंत कब्जा नहीं किया गया था; केवल संधि की गई थी। दीव का विलय बहुत बाद में हुआ था।"
    })

    # 21. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the tactical decisions of Lourenço de Almeida at the Battle of Chaul, consider the following statements:
1. He decided to fight in the shallow river estuary, which restricted the movement of his large naus.
2. His flagship became trapped by a fishing cable, making it an easy target for Gujarati gunboats.
3. He ordered a full retreat, but his command was ignored by the Portuguese officers.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. The shallow Kundalika estuary restricted the naus, and Lourenço's flagship Santo Espírito was pinned down by a cable. Statement 3 is incorrect; Lourenço refused to retreat or abandon ship, fighting until he was killed."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """चोल की लड़ाई में लॉरेंको डी अल्मेडा के रणनीतिक निर्णयों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. उन्होंने उथले नदी के मुहाने पर लड़ने का फैसला किया, जिससे उनके बड़े जहाजों की गति सीमित हो गई।
2. उनका प्रमुख जहाज एक केबल में फंस गया था, जिससे वह गुजराती तोपखानों के लिए एक आसान निशाना बन गया।
3. उन्होंने पूर्ण वापसी का आदेश दिया, लेकिन पुर्तगाली अधिकारियों ने उनके आदेश की अनदेखी की।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। मुहाने का उथला पानी प्रतिकूल था और जहाज फंस गया था। कथन 3 गलत है क्योंकि लॉरेंको ने हटने से इनकार कर दिया था।"
    })

    # 22. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the geopolitical impact of the Portuguese victory at Diu:
1. It broke the spice trade monopoly of Arab merchants in the Arabian Sea.
2. It established European naval dominance in Asia that lasted for nearly four centuries.
3. It forced the Ottoman Empire to completely abandon its naval presence in the Indian Ocean.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 2 are correct. The victory broke the Arab-Mamluk monopoly and established European dominance. Statement 3 is incorrect; the Ottoman Empire did not abandon the region; they sent subsequent naval expeditions under Piri Reis and Seydi Ali Reis in the 1530s-1550s."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """दीव में पुर्तगाली विजय के भू-राजनीतिक प्रभाव के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. इसने अरब सागर में अरब व्यापारियों के मसाला व्यापार एकाधिकार को तोड़ दिया।
2. इसने एशिया में यूरोपीय नौसैनिक वर्चस्व स्थापित किया जो लगभग चार शताब्दियों तक चला।
3. इसने ओटोमन साम्राज्य को हिंद महासागर में अपनी नौसैनिक उपस्थिति को पूरी तरह से छोड़ने के लिए मजबूर किया।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 2 सही हैं। इसने यूरोपीय नौसैनिक युग की शुरुआत की। कथन 3 गलत है क्योंकि ओटोमन साम्राज्य ने नौसेना का उपयोग जारी रखा और बाद में पीरी रईस के तहत अभियान भेजे।"
    })

    # 23. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the transition from Almeida's strategy to Albuquerque's strategy, consider the following statements:
1. Almeida focused on mobile sea power, whereas Albuquerque advocated for fortified coastal bases.
2. Almeida opposed the colonization of land, while Albuquerque promoted settlement and marriage with local women.
3. Both viceroys agreed that the Cartaz system was unnecessary and should be replaced by free trade.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Almeida focused on sea patrols and opposed colonization. Albuquerque advocated for fortified bases and mixed-marriage colonization. Statement 3 is incorrect; both strongly enforced the Cartaz system to maintain their state trade monopoly."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """अल्मेडा की रणनीति से अल्बुकर्क की रणनीति में संक्रमण के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. अल्मेडा ने मोबाइल समुद्री शक्ति पर ध्यान केंद्रित किया, जबकि अल्बुकर्क ने किलेबंद मुख्य भूमि के ठिकानों की वकालत की।
2. अल्मेडा ने भूमि के उपनिवेशीकरण का विरोध किया, जबकि अल्बुकर्क ने बसने और स्थानीय महिलाओं के साथ विवाह को बढ़ावा दिया।
3. दोनों वायसराय इस बात पर सहमत थे कि कार्टाज प्रणाली अनावश्यक थी और इसे मुक्त व्यापार द्वारा प्रतिस्थापित किया जाना चाहिए।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। अल्मेडा समुद्री शक्ति पर और अल्बुकर्क किलेबंदी पर केंद्रित थे। कथन 3 गलत है क्योंकि दोनों कार्टाज व्यवस्था के कट्टर समर्थक थे।"
    })

    # 24. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """Consider the following statements regarding the Battle of Toro (1476):
1. It was fought between Portugal and Castile for control of the Castilian Crown.
2. Francisco de Almeida fought alongside the Castilian forces.
3. The battle helped solidify Almeida's reputation as an elite military strategist.
How many of the statements given above are correct?""",
        "opts": st_opts_2,
        "ans": 1,
        "sol": "Statements 1 and 3 are correct. Toro was a major battle in the Castilian succession dispute, and Almeida's performance cemented his military reputation. Statement 2 is incorrect; Almeida fought for the Portuguese Crown, not Castile."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """टोरो की लड़ाई (1476) के संबंध में निम्नलिखित कथनों पर विचार कीजिए:
1. यह कैस्टिलियन क्राउन के नियंत्रण के लिए पुर्तगाल और कैस्टिल के बीच लड़ा गया था।
2. फ्रांसिस्को डी अल्मेडा ने कैस्टिलियन सेना के साथ मिलकर लड़ाई लड़ी थी।
3. इस युद्ध ने अल्मेडा की एक विशिष्ट सैन्य रणनीतिकार के रूप में प्रतिष्ठा को मजबूत करने में मदद की।
उपर्युक्त कथनों में से कितने सही हैं?""",
        "opts": st_opts_2_hi,
        "ans": 1,
        "sol": "कथन 1 और 3 सही हैं। टोरो युद्ध कैस्टिलियन क्राउन के लिए था और इसमें अल्मेडा ने ख्याति अर्जित की। कथन 2 गलत है क्योंकि उन्होंने पुर्तगाली पक्ष से युद्ध लड़ा था।"
    })

    # 25. Multi-Statement
    en.append({
        "type": "Statement-Based",
        "q": """With reference to the Padroado Real system, consider the following statements:
1. It was an agreement between the Portuguese Crown and the Vatican granting the Crown patronage over religious institutions in Asia.
2. It allowed the Viceroy to appoint bishops and administer church taxes in the Estado da Índia.
3. It integrated Christian missionary expansion directly with the commercial goals of the Portuguese state.
Which of the statements given above is/are correct?""",
        "opts": st_opts_1,
        "ans": 2,
        "sol": "Statements 1 and 3 are correct. Padroado Real was a crown religious patronage system, integrating trade and missionary zeal. Statement 2 is incorrect; the patronage and appointments were vested in the Portuguese Monarch, not the local Viceroy directly, who merely facilitated them."
    })
    hi.append({
        "type": "Statement-Based",
        "q": """पाद्रोआडो रीयल (Padroado Real) प्रणाली के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:
1. यह पुर्तगाली क्राउन और वेटिकन के बीच एक समझौता था जिसने क्राउन को एशिया में धार्मिक संस्थानों पर संरक्षण प्रदान किया।
2. इसने वायसराय को एस्टाडो दा इंडिया में बिशप नियुक्त करने और चर्च करों को प्रशासित करने की अनुमति दी।
3. इसने ईसाई मिशनरी विस्तार को सीधे पुर्तगाली राज्य के व्यावसायिक लक्ष्यों के साथ एकीकृत किया।
उपर्युक्त कथनों में से कौन-सा/से सही है/हैं?""",
        "opts": st_opts_1_hi,
        "ans": 2,
        "sol": "कथन 1 और 3 सही हैं। पाद्रोआडो रीयल शाही संरक्षण प्रणाली थी। कथन 2 गलत है क्योंकि बिशप की नियुक्ति की शक्ति राजा के पास थी, सीधे वायसराय के पास नहीं।"
    })

    # 26. Matching-Type (UPSC Pairs format)
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Fortress - Strategic Location
1. Fort São Tiago - Kilwa (Swahili Coast)
2. Fort Manuel - Cochin (Malabar Coast)
3. Fort St. Angelo - Cannanore (Western India)
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Fort São Tiago was built in Kilwa, Fort Manuel in Cochin, and Fort St. Angelo in Cannanore."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
किला - रणनीतिक स्थान
1. फोर्ट साओ टियागो - किलवा (स्वाहिली तट)
2. फोर्ट मैनुअल - कोचीन (मालाबार तट)
3. फोर्ट सेंट एंजेलो - कन्नूर (पश्चिमी भारत)
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। किलवा में साओ टियागो, कोचीन में फोर्ट मैनुअल और कन्नूर में फोर्ट सेंट एंजेलो स्थापित किया गया था।"
    })

    # 27. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Naval Commander - Fleet / Command Affiliation
1. Amir Husain Al-Kurdi - Mamluk Sultanate Fleet
2. Malik Ayyaz - Ottoman Empire Navy
3. Lourenço de Almeida - Portuguese Patrol Fleet
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 3 are correctly matched. Amir Husain commanded the Mamluk fleet, and Lourenço de Almeida commanded the Portuguese patrol. Pair 2 is incorrectly matched; Malik Ayyaz was the governor of Diu under the Gujarat Sultanate, not a commander of the Ottoman Empire Navy."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
नौसैनिक कमांडर - बेड़ा / कमान संबद्धता
1. अमीर हुसैन अल-कुर्दी - ममलुक सल्तनत बेड़ा
2. मलिक अय्याज़ - ओटोमन साम्राज्य नौसेना
3. लॉरेंको डी अल्मेडा - पुर्तगाली गश्ती बेड़ा
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 3 सही सुमेलित हैं। मलिक अय्याज़ गुजरात सल्तनत के अधीन दीव का गवर्नर था, न कि ओटोमन साम्राज्य नौसेना का कमांडर।"
    })

    # 28. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Historical Event - Calendar Year
1. Construction of Fort Manuel - 1505 CE
2. Battle of Chaul - 1508 CE
3. Battle of Diu - 1509 CE
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Fort Manuel was reinforced in 1505, the Battle of Chaul occurred in 1508, and the Battle of Diu occurred in 1509."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
ऐतिहासिक घटना - कैलेंडर वर्ष
1. फोर्ट मैनुअल का निर्माण - 1505 ईस्वी
2. चोल की लड़ाई - 1508 ईस्वी
3. दीव की लड़ाई - 1509 ईस्वी
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। कोचीन किला 1505 में पत्थरों से मजबूत हुआ, चोल की लड़ाई 1508 में और दीव की लड़ाई 1509 में हुई।"
    })

    # 29. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Strategic Term - Core Concept
1. Cartaz - Compulsory maritime permit
2. Mare Clausum - Freedom of navigation for all
3. Volta do Mar - Atlantic sailing technique
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 3 are correctly matched. Cartaz is a passport, and Volta do Mar is the ocean sailing maneuver. Pair 2 is incorrectly matched; Mare Clausum refers to the doctrine of Closed Seas (exclusive Portuguese sovereignty), not freedom of navigation."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
रणनीतिक शब्द - मूल अवधारणा
1. कार्टाज - अनिवार्य समुद्री परमिट
2. मारे क्लॉसम - सभी के लिए नौवहन की स्वतंत्रता
3. वोल्टा डो मार - अटलांटिक नौवहन तकनीक
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 3 सही सुमेलित हैं। मारे क्लॉसम का अर्थ बंद समुद्र (पुर्तगाली एकाधिकार) था, न कि नेविगेशन की स्वतंत्रता।"
    })

    # 30. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Explorer - Historical Significance
1. Vasco da Gama - First European to round the Cape of Good Hope
2. Bartolomeu Dias - Captain who discovered Brazil
3. Francisco de Almeida - First Viceroy of Portuguese India
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched. Almeida was the first Viceroy. Pair 1 is incorrect; Bartolomeu Dias was the first European to round the Cape of Good Hope in 1488. Pair 2 is incorrect; Pedro Álvares Cabral discovered Brazil in 1500."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली खोजकर्ता - ऐतिहासिक महत्व
1. वास्को डी गामा - केप ऑफ गुड होप का चक्कर लगाने वाले पहले यूरोपीय
2. बारटोलोमियु डियास - ब्राजील की खोज करने वाले कप्तान
3. फ्रांसिस्को डी अल्मेडा - पुर्तगाली भारत के पहले वायसराय
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही है। डियास ने केप ऑफ गुड होप का चक्कर लगाया और कैब्राल ने ब्राजील की खोज की, इसलिए युग्म 1 और 2 गलत हैं।"
    })

    # 31. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Local Ruler - Domain / Kingdom
1. Kolathiri Raja - Kingdom of Cochin
2. Trimumpara Raja - Kingdom of Cannanore
3. Mahmud Begarha - Sultanate of Gujarat
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched; Mahmud Begarha ruled Gujarat. Pair 1 is incorrect; Kolathiri Raja was the ruler of Cannanore. Pair 2 is incorrect; Trimumpara Raja was the ruler of Cochin."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
स्थानीय शासक - क्षेत्र / साम्राज्य
1. कोलथिरि राजा - कोचीन का साम्राज्य
2. त्रिमुम्पारा राजा - कन्नूर का साम्राज्य
3. महमूद बेगड़ा - गुजरात का सल्तनत
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही सुमेलित है। कोलथिरि कन्नूर के और त्रिमुम्पारा कोचीन के शासक थे, इसलिए 1 और 2 गलत हैं।"
    })

    # 32. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Office - Primary Responsibility
1. Feitor (Factor) - Civil and military defense of the province
2. Escrivão (Scribe) - Bookkeeping and recording cargo transactions
3. Capitão-mor (Captain-Major) - Command of naval patrol fleets
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 2 and 3 are correctly matched. Scribes handled bookkeeping, and Captain-Majors led naval patrols. Pair 1 is incorrect; Feitor (Factor) was responsible for commercial trade transactions and managing the factory warehouse, not civil or military provincial defense."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली कार्यालय - प्राथमिक जिम्मेदारी
1. फिटर (कारक) - प्रांत की नागरिक और सैन्य रक्षा
2. एस्क्रिवान (लेखक) - बहीखाता पद्धति और कार्गो रिकॉर्डिंग
3. कैपिटान-मोर (कैप्टन-मेजर) - नौसैनिक गश्ती बेड़े की कमान
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 2 और 3 सही हैं। कारक (Feitor) व्यापार और गोदाम के प्रभारी थे, न कि सैन्य रक्षा के।"
    })

    # 33. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Strategic Battle - Decisive Naval Tactic
1. Battle of Chaul - Operations in shallow river estuary
2. Battle of Diu - Long-range artillery bombardment
3. Siege of Cannanore - High-walled vessel boarding
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Chaul was fought in the Kundalika river estuary, and Diu was decided by Portuguese long-range naval artillery. Pair 3 is incorrect; the Siege of Cannanore was a land-based siege of the fort, not a boarding action."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
रणनीतिक युद्ध - निर्णायक नौसैनिक रणनीति
1. चोल की लड़ाई - उथले नदी के मुहाने पर अभियान
2. दीव की लड़ाई - लंबी दूरी का तोपखाना गोलाबारी
3. कन्नूर की घेराबंदी - ऊंचे जहाजों पर चढ़ाई की रणनीति
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। कन्नूर की घेरावंदी एक थल सेना द्वारा किले की घेराबंदी थी, न कि बोर्डिंग कार्रवाई।"
    })

    # 34. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Monarch - Primary Colonial Action
1. King Manuel I - Commissioned the Estado da Índia in 1505
2. King John II - Signed the Treaty of Tordesillas (1494)
3. King Afonso V - Supported Vasco da Gama's 1498 expedition
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Manuel I established the viceroyalty, and John II signed the Treaty of Tordesillas. Pair 3 is incorrect; Vasco da Gama's expedition was commissioned by King Manuel I, who succeeded King John II. King Afonso V died in 1481, long before the voyage."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली सम्राट - प्राथमिक औपनिवेशिक कार्रवाई
1. राजा मैनुअल प्रथम - 1505 में एस्टाडो दा इंडिया की स्थापना की
2. राजा जॉन द्वितीय - टॉर्डेसिलस की संधि (1494) पर हस्ताक्षर किए
3. राजा अफोंसो पंचम - वास्को डी गामा के 1498 के अभियान का समर्थन किया
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। वास्को डी गामा का अभियान मैनुअल प्रथम द्वारा शुरू किया गया था, न कि अफोंसो पंचम द्वारा।"
    })

    # 35. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Key Fortification - Date of Establishment / Reinforcement
1. Fort Manuel (Cochin) - 1503/1505 CE
2. Fort St. Angelo (Cannanore) - 1505 CE
3. Anjadip Fort - 1506 CE
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Cochin fort was built in 1503 and reinforced in 1505. Cannanore fort was built in 1505. Pair 3 is incorrect; Anjadip Fort was built in 1505 and demolished/abandoned in 1506, not established in 1506."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
प्रमुख किला - स्थापना / सुदृढ़ीकरण की तिथि
1. फोर्ट मैनुअल (कोचीन) - 1503/1505 ईस्वी
2. फोर्ट सेंट एंजेलो (कन्नूर) - 1505 ईस्वी
3. अंजादीप किला - 1506 ईस्वी
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। अंजादीप किला 1505 में स्थापित हुआ था और 1506 में इसे खाली किया गया था।"
    })

    # 36. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Viceroy / Governor - Strategy / Policy focus
1. Francisco de Almeida - Blue Water Policy (Sea Power)
2. Afonso de Albuquerque - Imperial territorial colonization
3. Vasco da Gama - Commercial factors without military presence
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Almeida pioneered naval control, and Albuquerque focused on land empire. Pair 3 is incorrect; Vasco da Gama utilized military force (e.g. bombardment of Calicut in 1502) and established early fortifications during his second voyage, not just peaceful factors."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
वायसराय / गवर्नर - रणनीति / नीति फोकस
1. फ्रांसिस्को डी अल्मेडा - नीले पानी की नीति (समुद्री शक्ति)
2. अल्फांसो डी अल्बुकर्क - साम्राज्यवादी क्षेत्रीय उपनिवेशीकरण
3. वास्को डी गामा - बिना सैन्य उपस्थिति के वाणिज्यिक कारक
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। वास्को डी गामा ने भी सैन्य बल और बमबारी का उपयोग किया था, केवल शांतिपूर्ण व्यापार नहीं।"
    })

    # 37. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Vessel Type - Operational Role
1. Carrack (Nau) - Large armed cargo vessel for global routes
2. Caravel - Fast, highly maneuverable ship for coastal exploration
3. Galley - Oar-powered warship utilized in shallow waters
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 2,
        "sol": "All three pairs are correctly matched. Naus were cargo carriers, Caravels were fast exploration ships, and Galleys used oars for shallow-water maneuverability."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली जहाज प्रकार - परिचालन भूमिका
1. कैरक (नौ) - वैश्विक मार्गों के लिए बड़े सशस्त्र मालवाहक जहाज
2. कार्वेल - तटीय अन्वेषण के लिए तेज, अत्यधिक गतिशील जहाज
3. गैली - उथले पानी में उपयोग किया जाने वाला पतवार चालित युद्धपोत
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 2,
        "sol": "सभी तीन युग्म सही सुमेलित हैं। कैरक, कार्वेल और गैली की भूमिकाएं सही वर्णित हैं।"
    })

    # 38. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Geographic Point - Strategic Connection
1. Kilwa - Control of Swahili Gold Trade
2. Cochin - Capital of early Estado da Índia
3. Diu - Choke point at the mouth of the Red Sea
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Kilwa controlled the gold route, and Cochin was the capital. Pair 3 is incorrect; Diu is off the Gujarat coast in Western India, not at the mouth of the Red Sea (which is Bab-el-Mandeb/Aden)."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
भौगोलिक बिंदु - रणनीतिक संबंध
1. किलवा - स्वाहिली सोने के व्यापार का नियंत्रण
2. कोचीन - प्रारंभिक एस्टाडो दा इंडिया की राजधानी
3. दीव - लाल सागर के मुहाने पर चोक पॉइंट
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। दीव गुजरात तट पर है, लाल सागर के मुहाने पर अदन या बाब-अल-मन्देब है।"
    })

    # 39. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Historical Source - Primary Context
1. Pero Vaz de Caminha's Letter - Report on the discovery of Brazil
2. Roteiro - Logbook of Vasco da Gama's first voyage
3. Comentários de Afonso de Albuquerque - Chronicles of Almeida's military actions in Castile
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 1,
        "sol": "Pairs 1 and 2 are correctly matched. Caminha's letter reported Brazil's discovery, and Roteiro was Gama's log. Pair 3 is incorrect; the Commentaries of Afonso de Albuquerque document Albuquerque's own governorship and policies in Asia, not Almeida's Castilian military campaigns."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
ऐतिहासिक स्रोत - प्राथमिक संदर्भ
1. पेरो वाज़ डे कामिन्या का पत्र - ब्राजील की खोज पर रिपोर्ट
2. रोटेइरो - वास्को डी गामा की पहली यात्रा की लॉगबुक
3. अल्फांसो डी अल्बुकर्क के कमेंट्रीस - कैस्टिल में अल्मेडा की सैन्य कार्रवाई का इतिहास
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 1,
        "sol": "युग्म 1 और 2 सही हैं। अल्बुकर्क की टिप्पणियां अल्बुकर्क के अपने गवर्नरशिप के इतिहास को बताती हैं, अल्मेडा के कैस्टिलियन युद्धों को नहीं।"
    })

    # 40. Matching-Type
    en.append({
        "type": "MCQ",
        "q": """Consider the following pairs:
Portuguese Military Commander - Death / Skirmish Site
1. Lourenço de Almeida - Estuary at Table Bay
2. Francisco de Almeida - River mouth at Chaul
3. Bartolomeu Dias - Open seas off the Cape of Good Hope
How many of the above pairs are correctly matched?""",
        "opts": ["Only one pair", "Only two pairs", "All three pairs", "None of the pairs"],
        "ans": 0,
        "sol": "Only pair 3 is correctly matched; Bartolomeu Dias drowned during a storm off the Cape of Good Hope in 1500. Pair 1 is incorrect; Lourenço de Almeida was killed at the Battle of Chaul. Pair 2 is incorrect; Francisco de Almeida was killed at Table Bay, South Africa."
    })
    hi.append({
        "type": "MCQ",
        "q": """निम्नलिखित युग्मों पर विचार कीजिए:
पुर्तगाली सैन्य कमांडर - मृत्यु / झड़प का स्थान
1. लॉरेंको डी अल्मेडा - टेबल बे का मुहाना
2. फ्रांसिस्को डी अल्मेडा - चोल में नदी का मुहाना
3. बारटोलोमियु डियास - केप ऑफ गुड होप के पास खुला समुद्र
उपर्युक्त युग्मों में से कितने सही सुमेलित हैं?""",
        "opts": ["केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म", "कोई भी युग्म नहीं"],
        "ans": 0,
        "sol": "केवल युग्म 3 सही सुमेलित है। लॉरेंको चोल में और फ्रांसिस्को टेबल बे में मारे गए थे, इसलिए 1 और 2 गलत हैं।"
    })

    # 41. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): King Manuel I established a permanent viceroyalty in India in 1505 CE.
Reason (R): The Portuguese Crown realized that sending temporary annual armadas was insufficient to enforce a trade monopoly against hostile local alliances.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason correctly explains the Assertion. The permanent administrative state was created because seasonal fleets could not maintain security or enforce trade monopoly."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): राजा मैनुअल प्रथम ने 1505 ईस्वी में भारत में एक स्थायी वायसराय पद की स्थापना की।
कारण (R): पुर्तगाली क्राउन ने महसूस किया कि विरोधी स्थानीय गठबंधनों के खिलाफ व्यापार एकाधिकार लागू करने के लिए मौसमी वार्षिक बेड़े भेजना नाकाफी था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। स्थायी प्रशासन की स्थापना मौसमी बेड़ों की अक्षमता के कारण हुई थी।"
    })

    # 42. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida strongly opposed the acquisition of land territories in India.
Reason (R): He formulated the Blue Water Policy, believing that Portuguese power should reside entirely on naval control of sea lanes due to manpower limitations.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Almeida opposed land bases because he believed that sea supremacy was sufficient and that land fortresses would drain resources."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा ने भारत में भूमि क्षेत्रों के अधिग्रहण का कड़ा विरोध किया।
कारण (R): उन्होंने नीले पानी की नीति (ब्लू वाटर पॉलिसी) का प्रतिपादन किया, यह मानते हुए कि जनशक्ति की सीमाओं के कारण पुर्तगाली शक्ति पूरी तरह से समुद्री मार्गों के नौसैनिक नियंत्रण पर आधारित होनी चाहिए।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। अल्मेडा ने जनशक्ति की कमी के कारण भूमि अधिग्रहण का विरोध किया।"
    })

    # 43. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Rulers allied with the Portuguese, such as the Raja of Cochin, were exempt from obtaining the Cartaz maritime license.
Reason (R): The Portuguese Crown asserted complete sovereign jurisdiction under the legal doctrine of Mare Clausum.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Assertion is false, but Reason is true. Rulers allied with the Portuguese, including the Raja of Cochin, were NOT exempt from obtaining Cartazes; they had to secure licenses for all their ships. The Reason is true, as Mare Clausum was the legal justification used to claim sovereignty over the sea."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): पुर्तगालियों के साथ गठबंधन करने वाले शासकों, जैसे कि कोचीन के राजा, को कार्टाज समुद्री लाइसेंस प्राप्त करने से छूट दी गई थी।
कारण (R): पुर्तगाली क्राउन ने मारे क्लॉसम के कानूनी सिद्धांत के तहत पूर्ण संप्रभु अधिकार क्षेत्र का दावा किया था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A गलत है, लेकिन R सही है। कोचीन के राजा को भी कार्टाज लाइसेंस लेना पड़ता था, कोई छूट नहीं थी।"
    })

    # 44. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Scribes and financial factors in the Estado da Índia reported directly to the Viceroy.
Reason (R): The Portuguese Crown wanted to ensure that the Viceroy possessed unified control over civil, judicial, and financial affairs.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Both Assertion and Reason are false. Scribes and factors reported directly to the Casa da Índia in Lisbon, bypassing the Viceroy's control. The Reason is false; the Crown designed this separation of powers specifically to check the Viceroy and prevent autonomous rebellion."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): एस्टाडो दा इंडिया में लेखक (Scribes) और वित्तीय कारक (Factors) सीधे वायसराय को रिपोर्ट करते थे।
कारण (R): पुर्तगाली क्राउन यह सुनिश्चित करना चाहता था कि वायसराय के पास नागरिक, न्यायिक और वित्तीय मामलों पर एकीकृत नियंत्रण हो।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A और R दोनों गलत हैं। वे सीधे लिस्बन को रिपोर्ट करते थे, और क्राउन ने ऐसा नियंत्रण को रोकने तथा वायसराय पर नजर रखने के लिए किया था।"
    })

    # 45. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Almeida ordered the demolition and abandonment of the Anjadip Fort in late 1506 CE.
Reason (R): The fort suffered constant raids from the forces of the Adil Shahi Sultanate of Bijapur and was too costly to maintain.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason correctly explains the Assertion. Due to persistent raids from Bijapur forces and high logistical maintenance costs, Almeida decided to demolish and abandon Anjadip."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): अल्मेडा ने 1506 ईस्वी के अंत में अंजादीप किले को ध्वस्त करने और इसे छोड़ने का आदेश दिया।
कारण (R): इस किले पर बीजापुर के आदिल शाही सल्तनत की सेना द्वारा लगातार हमले किए जा रहे थे और इसका रखरखाव बहुत महंगा था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। बीजापुर के हमलों और भारी खर्च के कारण 1506 में इस किले को छोड़ दिया गया था।"
    })

    # 46. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Battle of Chaul in 1508 resulted in the death of Lourenço de Almeida, the Viceroy's son.
Reason (R): His flagship became trapped by a fishing cable in the shallow waters of the Kundalika river estuary, exposing it to heavy coalition fire.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Lourenço's ship Santo Espírito was pinned down by a cable, preventing it from maneuvering, leading to his heroic death under heavy fire."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): 1508 में चोल की लड़ाई के कारण वायसराय के पुत्र लॉरेंको डी अल्मेडा की मृत्यु हो गई।
कारण (R): उनका प्रमुख जहाज कुंडलिका नदी के मुहाने के उथले पानी में एक मछली पकड़ने वाले केबल में फंस गया था, जिससे वह गठबंधन की भारी गोलाबारी की चपेट में आ गया था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। लॉरेंको का जहाज केबल में फंस गया था, जिससे वह अपनी गतिशीलता खो बैठा और मारा गया।"
    })

    # 47. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida refused to surrender the office of Governor to Afonso de Albuquerque in late 1508.
Reason (R): Almeida disputed the validity of Albuquerque's credentials and swore to avenge his son's death first.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. Almeida delayed the transfer of power and imprisoned Albuquerque because he was determined to retaliate against the coalition fleet at Diu."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा ने 1508 के अंत में अल्फांसो डी अल्बुकर्क को गवर्नर का पद सौंपने से इनकार कर दिया।
कारण (R): अल्मेडा ने अल्बुकर्क के दस्तावेजों की वैधता पर विवाद उठाया और पहले अपने पुत्र की मृत्यु का बदला लेने की प्रतिज्ञा की थी।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। अल्मेडा अपने बेटे की मौत का बदला लेने के लिए प्रतिबद्ध थे, इसलिए उन्होंने उत्तराधिकार को टाला।"
    })

    # 48. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Battle of Diu (1509) ended Arab and Egyptian dominance over the Indian Ocean trade routes.
Reason (R): The crushing Portuguese victory established European naval hegemony in Asia for the next 400 years.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 0,
        "sol": "Both Assertion and Reason are true, and the Reason is the correct explanation of the Assertion. The Mamluk fleet's destruction at Diu ended their monopoly and permanently secured European naval supremacy in the region."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): दीव की लड़ाई (1509) ने हिंद महासागर के व्यापार मार्गों पर अरब और मिस्र के प्रभुत्व को समाप्त कर दिया।
कारण (R): पुर्तगालियों की इस शानदार जीत ने अगले 400 वर्षों के लिए एशिया में यूरोपीय नौसैनिक वर्चस्व स्थापित किया।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 0,
        "sol": "A और R दोनों सही हैं और R, A की सही व्याख्या करता है। दीव की लड़ाई में गठबंधन की हार ने यूरोपीय समुद्री युग की शुरुआत की।"
    })

    # 49. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): The Republic of Venice openly and officially declared war on the Portuguese Empire in 1507.
Reason (R): Venice was losing its monopoly over the Mediterranean spice trade due to the Portuguese blockade of the Red Sea.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Assertion is false, but Reason is true. Venice did NOT declare war openly or officially; instead, they worked secretly, supplying shipbuilding timber to the Mamluks of Egypt to fight the Portuguese. The Reason is true, as the Portuguese Cape Route monopoly bypassed Alexandria, threatening Venetian trade."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): वेनिस गणराज्य ने 1507 में आधिकारिक तौर पर पुर्तगाली साम्राज्य के खिलाफ युद्ध की घोषणा की थी।
कारण (R): लाल सागर की पुर्तगाली नाकेबंदी के कारण वेनिस भूमध्यसागरीय मसाला व्यापार पर अपना एकाधिकार खो रहा था।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-sa सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A गलत है, लेकिन R सही है। वेनिस ने युद्ध की घोषणा नहीं की, बल्कि ममलुकों को गुप्त रूप से लकड़ी देकर मदद की थी।"
    })

    # 50. Assertion-Reason
    en.append({
        "type": "Assertion-Reason",
        "q": """Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):
Assertion (A): Francisco de Almeida was buried with full military honors in Lisbon in 1510.
Reason (R): King Manuel I wanted to celebrate his historic victory at the Battle of Diu.
In the context of the above statements, which of the following is correct?""",
        "opts": en_ar_opts,
        "ans": 3,
        "sol": "Both Assertion and Reason are false. Almeida was not buried in Lisbon; he was killed and buried in an unmarked grave on the beach of Table Bay, South Africa, in March 1510. The Reason is false, as his death occurred during his return voyage and he never reached Lisbon."
    })
    hi.append({
        "type": "Assertion-Reason",
        "q": """नीचे दो कथन दिए गए हैं, एक को अभिकथन (A) और दूसरे को कारण (R) के रूप में लेबल किया गया है:
अभिकथन (A): फ्रांसिस्को डी अल्मेडा को 1510 में लिस्बन में पूर्ण सैन्य सम्मान के साथ दफनाया गया था।
कारण (R): राजा मैनुअल प्रथम दीव की लड़ाई में उनकी ऐतिहासिक जीत का जश्न मनाना चाहते थे।
उपर्युक्त कथनों के संदर्भ में, निम्नलिखित में से कौन-सा सही है?""",
        "opts": hi_ar_opts,
        "ans": 3,
        "sol": "A और R दोनों गलत हैं। अल्मेडा की दक्षिण अफ्रीका के टेबल बे पर मौत हो गई और उन्हें वहीं दफनाया गया, वे लिस्बन कभी नहीं पहुंचे।"
    })

    return en, hi'''

# Let's define deep_dive_en and deep_dive_hi
deep_dive_en = {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Master Francisco de Almeida's viceroyalty, strategic doctrines, fortifications, key naval battles, and historical legacy in India.",
    "sections": [
        {
            "title": "1. Geopolitical Genesis & Establishment of the Estado da Índia (1505)",
            "content": "<p><strong>Strategic Transition of Portuguese Imperial Policy:</strong> Following Vasco da Gama's navigation of the Cape Route in 1498 and Pedro Álvares Cabral's militarized expedition in 1500, the Portuguese Crown (King Manuel I) recognized that annual commercial expeditions (Armadas da Índia) were structurally inadequate. The Indian Ocean maritime trade network was highly sophisticated, dominated by wealthy merchant syndicates from Gujarat, Malabar, East Africa, and the Red Sea, and protected by local powers like the Zamorin of Calicut. To secure a monopoly over the spice trade and exclude Muslim and European competitors, Lisbon realized it needed to establish a permanent, sovereign military and administrative state in Asia. This led to the creation of the <em>Estado da Índia</em> in 1505.</p><p><strong>The Commissioning of Francisco de Almeida:</strong> In 1505, Francisco de Almeida, a distinguished nobleman, diplomat, and military veteran of the Castilian succession wars (Battle of Toro, 1476) and the Christian conquest of Granada, was appointed as the first Viceroy and Governor-General. He was granted plenipotentiary civil, judicial, and military authority to represent the Portuguese Crown in Asia. Departing Lisbon on March 25, 1505, with 21 ships and 1,500 soldiers, Almeida's mandate was to secure trade routes, build coastal fortifications, enforce a trade monopoly, and crush the naval power of Venice's trade partners, particularly the Mamluk Sultanate of Egypt.</p><p><strong>Administrative Checks and Balances:</strong> To prevent the concentration of absolute power in the hands of the Viceroy, the Portuguese Crown implemented strict institutional controls. Scribes (<em>escrivães</em>) and financial factors (<em>feitores</em>) reported directly to the <em>Casa da Índia</em> in Lisbon, bypassing the Viceroy's financial authority. Furthermore, the Viceroy was appointed for a strict, non-renewable three-year term, setting a precedent that minimized the risk of autonomous provincial rebellion.</p>"
        },
        {
            "title": "2. The Philosophy of the Blue Water Policy & Mare Clausum",
            "content": "<p><strong>The Strategic Philosophy of Política da Água Azul:</strong> Unlike his successor Afonso de Albuquerque, who advocated for a land-based territorial empire with colonial settlements, Francisco de Almeida believed that Portugal's severe demographic limitations and limited resources made land conquest in India unsustainable. He formulated the <em>Blue Water Policy</em> (<em>Política da Água Azul</em>), arguing that Portuguese supremacy must reside entirely on the sea. In his famous correspondence to King Manuel I, Almeida declared: <em>\"As long as you may be powerful at sea, you will hold India as yours; and if you do not possess this power, little will avail you a fortress on shore.\"</em></p><p><strong>Tactical Enforcement:</strong> The policy prioritized naval mobility, cruising squadrons, and control of critical shipping lanes over territorial conquest. The Portuguese leveraged superior ship design (large naus and fast caravels) and ship-borne naval artillery (cannon broadsides) to dominate the ocean, bypassing land-based military conflicts with powerful mainland Indian empires like the Vijayanagara Empire or the Deccan Sultanates.</p><p><strong>The Cartaz-Armada System:</strong> To enforce their maritime sovereignty under the legal doctrine of <em>Mare Clausum</em> (Closed Sea), the Portuguese introduced the <em>Cartaz</em> system. Every merchant vessel operating in the Indian Ocean was forced to purchase a Cartaz (licensing permit) from Portuguese authorities. Rulers allied with Portugal, such as the Raja of Cochin, were not exempt from this licensing. This pass prohibited carrying weapons, pepper, ginger, or other royal monopoly goods, and forced ships to route through Portuguese ports to pay heavy customs duties. Any ship found without a Cartaz was subject to immediate seizure, confiscation of cargo, and the execution or enslavement of its crew.</p>"
        },
        {
            "title": "3. Strategic Fortifications & Indian Ocean Alliances",
            "content": "<p><strong>The Four Pillars of Maritime Defense:</strong> To support the Blue Water Policy's cruising patrols, Almeida's expedition was instructed to construct strategically located coastal and island fortifications to serve as safe harbors, fresh water stations, and warehouses (<em>feitorias</em>). The four key fortifications established or consolidated during his tenure were:</p><ul><li><strong>Fort São Tiago (Kilwa, East Africa):</strong> Built in 1505 on the Swahili Coast to secure the passage across the Indian Ocean and control the lucrative gold trade coming from Sofala.</li><li><strong>Fort Manuel (Cochin):</strong> Initially constructed as a wooden palisade in 1503, Almeida reinforced it in 1505 with stone bastions. Cochin served as the first administrative capital of the Estado da Índia, secured through a political alliance with the Trimumpara Raja, who sought Portuguese protection against the dominant Zamorin of Calicut.</li><li><strong>Fort St. Angelo (Cannanore):</strong> Built in late 1505 on a triangular spit of land. This fort secured the trade of Malabar ginger and horse imports, and famously withstood the grueling 1507 Siege of Cannanore launched by local forces backed by Calicut.</li><li><strong>Anjadip Fort:</strong> Built in 1505 on Anjadip Island off the coast of Goa to provide a vital fresh water supply and ship repair facility. However, due to constant raids from the forces of the Adil Shahi Sultanate of Bijapur and the high cost of maintenance, Almeida ordered its demolition and abandonment in 1506.</li></ul>"
        },
        {
            "title": "4. The Battle of Chaul (1508) & Mamluk Intervention",
            "content": "<p><strong>Outbreak of Geopolitical Conflict:</strong> The aggressive Portuguese blockade of the Red Sea and the Persian Gulf severely disrupted the spice monopoly of the Mamluk Sultanate of Egypt, which relied on transit customs duties for its economic survival. Backed secretly by Venice (which supplied shipbuilding timber via Alexandria to Suez) and supported by Ottoman specialists, Egypt constructed a war fleet at Suez. Commanded by Amir Husain Al-Kurdi, the Mamluk fleet sailed to India and allied with Malik Ayyaz, the governor of Diu under the Gujarat Sultanate, and the Zamorin of Calicut to expel the Portuguese.</p><p><strong>The Clash at Chaul:</strong> In March 1508, the coalition fleet surprised a smaller Portuguese patrol fleet in the shallow waters of the Kundalika River estuary at Chaul. The Portuguese fleet was commanded by Lourenço de Almeida, the Viceroy's only son. The shallow river restricted the maneuverability of the heavy Portuguese naus, exposing them to agile Gujarati dhows. During the battle, Lourenço's flagship, the <em>Santo Espírito</em>, was trapped by a fishing cable and pinned down. Despite sustaining severe wounds, Lourenço refused to surrender or abandon ship, fighting valiantly until a cannonball struck and killed him. The battle ended in a major Portuguese defeat, temporarily shattering their myth of naval invincibility in Asian waters.</p>"
        },
        {
            "title": "5. The Battle of Diu (1509) & Legacy of Sea Power",
            "content": "<p><strong>Francisco de Almeida's Retaliation:</strong> Shattered by the death of his only son, Viceroy Francisco de Almeida swore a personal oath of revenge. When his designated successor Afonso de Albuquerque arrived in Cochin in late 1508 with royal patents to assume the governorship, Almeida refused to hand over power. He claimed that Albuquerque's papers were invalid and subsequently imprisoned him in Fort Manuel, declaring: <em>\"I must first seek the blood of my son.\"</em> Almeida personally assembled a powerful armada of 19 ships and 1,300 soldiers and sailed north to locate the coalition fleet.</p><p><strong>The Decisive Clash & Imperial Legacy:</strong> On February 3, 1509, the Portuguese fleet engaged the Mamluk-Ottoman-Gujarati navy off the coast of Diu. Using superior naval artillery, long-range bombardment, and high-walled vessels that prevented coalition boarding tactics, Almeida achieved a crushing victory. The Mamluk fleet was destroyed, and Malik Ayyaz was forced to sign a peace treaty, releasing prisoners and paying a massive indemnity. The Battle of Diu is considered one of the most critical naval battles in history, as it ended Arab and Egyptian monopoly over the Indian Ocean and established European naval dominance in Asia for the next 400 years. Having avenged his son, Almeida released Albuquerque and departed for Portugal, but was killed in March 1510 in a skirmish with Khoikhoi natives over water at Table Bay, South Africa.</p>"
        }
    ]
}

deep_dive_hi = {
    "title": "पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)",
    "description": "फ्रांसिस्को डी अल्मेडा के वायसराय कार्यकाल, रणनीतिक सिद्धांतों, किलों, प्रमुख नौसैनिक लड़ाइयों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।",
    "sections": [
        {
            "title": "1. भू-राजनीतिक उत्पत्ति और एस्टाडो दा इंडिया की स्थापना (1505)",
            "content": "<p><strong>पुर्तगाली साम्राज्यवादी नीति का रणनीतिक संक्रमण:</strong> 1498 में वास्को डी गामा द्वारा केप मार्ग की खोज और 1500 में पेड्रो अल्वारेज़ कैब्राल के सैन्य अभियान के बाद, पुर्तगाली क्राउन (राजा मैनुअल प्रथम) ने महसूस किया कि वार्षिक व्यावसायिक अभियान (अर्माडा) संरचनात्मक रूप से अपर्याप्त थे। हिंद महासागर का समुद्री व्यापार अत्यधिक परिष्कृत था, जिस पर गुजरात, मालाबार, पूर्वी अफ्रीका और लाल सागर के समृद्ध व्यापारी सिंडिकेट का वर्चस्व था, और उन्हें कालीकट के ज़मोरिन जैसे स्थानीय शासकों का संरक्षण प्राप्त था। मसाला व्यापार पर एकाधिकार हासिल करने के लिए, लिस्बन ने महसूस किया कि उसे एशिया में एक स्थायी, संप्रभु सैन्य और प्रशासनिक राज्य स्थापित करने की आवश्यकता है। इसके परिणामस्वरूप 1505 में <em>एस्टाडो दा इंडिया</em> का गठन हुआ।</p><p><strong>फ्रांसिस्को डी अल्मेडा की नियुक्ति:</strong> 1505 में, कैस्टिलियन उत्तराधिकार युद्धों (टोरो का युद्ध, 1476) और ग्रेनाडा की विजय के एक प्रतिष्ठित कुलीन और सैन्य दिग्गज फ्रांसिस्को डी अल्मेडा को पहले वायसराय और गवर्नर-जनरल के रूप में नियुक्त किया गया था। उन्हें एशिया में पुर्तगाली क्राउन का प्रतिनिधित्व करने के लिए पूर्ण नागरिक, न्यायिक और सैन्य अधिकार दिए गए थे। 25 मार्च, 1505 को 21 जहाजों और 1,500 सैनिकों के साथ रवाना होकर, अल्मेडा का मुख्य कार्य समुद्री मार्गों को सुरक्षित करना, तटीय किलों का निर्माण करना, एकाधिकार लागू करना और ममलुक सल्तनत की नौसैनिक शक्ति को नष्ट करना था।</p><p><strong>प्रशासनिक नियंत्रण और संतुलन:</strong> वायसराय के हाथों में पूर्ण शक्ति के संकेंद्रण को रोकने के लिए, पुर्तगाली क्राउन ने कड़े नियंत्रण लागू किए। लेखक (<em>escrivães</em>) और वित्तीय कारक (<em>feitores</em>) वायसराय को दरकिनार कर सीधे लिस्बन में <em>कासा दा इंडिया</em> को रिपोर्ट करते थे। इसके अतिरिक्त, वायसराय का कार्यकाल कड़ाई से तीन वर्ष तक सीमित रखा गया था, जिसने किसी भी संभावित प्रांतीय विद्रोह के जोखिम को कम कर दिया।</p>"
        },
        {
            "title": "2. नीले पानी की नीति और मारे क्लॉसम का सिद्धांत",
            "content": "<p><strong>नीले पानी की नीति (ब्लू वाटर पॉलिसी) का दर्शन:</strong> अपने उत्तराधिकारी अल्फांसो डी अल्बुकर्क के विपरीत, जिसने क्षेत्रीय और भू-भाग आधारित साम्राज्य का समर्थन किया, फ्रांसिस्को डी अल्मेडा का मानना था कि पुर्तगाल की सीमित जनसंख्या और संसाधन भारत में भूमि-आधारित साम्राज्य को नहीं संभाल सकते। उन्होंने <em>ब्लू Water Policy</em> (नीले पानी की नीति) का प्रतिपादन किया, जिसके अनुसार पुर्तगाली शक्ति का आधार केवल समुद्र होना चाहिए। अल्मेडा ने राजा मैनुअल प्रथम को लिखा था: <em>'जब तक आप समुद्र पर शक्तिशाली रहेंगे, भारत आपका रहेगा; और यदि आपके पास यह शक्ति नहीं है, तो भूमि पर बने किले आपके किसी काम नहीं आएंगे।'</em></p><p><strong>नीति का कार्यान्वयन:</strong> इस रणनीति के तहत भूमि विजय के बजाय समुद्री गश्ती, गश्ती जहाजों और नौसैनिक वर्चस्व को प्राथमिकता दी गई। पुर्तगालियों ने बेहतर जहाज डिजाइन और जहाज पर लगी तोपों (नौसैनिक तोपखाने) के उपयोग से हिंद महासागर पर नियंत्रण किया, और विजयनगर साम्राज्य या डेक्कन सल्तनत जैसी मुख्य भूमि की शक्तियों के साथ भूमि-आधारित संघर्षों से दूरी बनाए रखी।</p><p><strong>कार्टाज-अर्माडा प्रणाली:</strong> <em>मारे क्लॉसम</em> (बंद समुद्र) के सिद्धांत के तहत अपनी संप्रभुता लागू करने के लिए पुर्तगालियों ने <em>कार्टाज</em> प्रणाली शुरू की। हिंद महासागर में व्यापार करने वाले सभी जहाजों को पुर्तगाली अधिकारियों से यह लाइसेंस (कार्टाज) खरीदना पड़ता था। कोचीन के राजा जैसे सहयोगी शासक भी इससे मुक्त नहीं थे। इस पास के तहत जहाजों को हथियार, काली मिर्च और अदरक ले जाने की मनाही थी और उन्हें सीमा शुल्क चुकाने के लिए पुर्तगाली बंदरगाहों पर रुकना पड़ता था। बिना कार्टाज के पाए जाने वाले जहाजों को जब्त कर लिया जाता था और चालक दल को मौत की सजा या दासता में धकेल दिया जाता था।</p>"
        },
        {
            "title": "3. रणनीतिक किलेबंदी और हिंद महासागर के गठबंधन",
            "content": "<p><strong>नौसैनिक रक्षा के चार स्तंभ:</strong> अपनी नौसैनिक नीति के समर्थन के लिए अल्मेडा ने रणनीतिक स्थानों पर चार प्रमुख किलों का निर्माण और सुदृढ़ीकरण किया, जो जहाजों के लिए सुरक्षित बंदरगाह, जल आपूर्ति और गोदाम (<em>feitorias</em>) के रूप में कार्य करते थे:</p><ul><li><strong>फोर्ट साओ टियागो (किलवा, पूर्वी अफ्रीका):</strong> हिंद महासागर पार करने वाले जहाजों की सुरक्षा और सोफाला के सोने के व्यापार को नियंत्रित करने के लिए 1505 में स्वाहिली तट पर स्थापित किया गया।</li><li><strong>फोर्ट मैनुअल (कोचीन):</strong> कोचीन के राजा के साथ गठबंधन के तहत 1503 में लकड़ी से बने इस किले को अल्मेडा ने 1505 में पत्थर के बुर्जों से मजबूत किया, जो भारत में पहला यूरोपीय किला बना। यह पहला मुख्यालय भी था।</li><li><strong>फोर्ट सेंट एंजेलो (कन्नूर):</strong> 1505 में मालाबार अदरक के व्यापार और घोड़ों के आयात पर नियंत्रण के लिए निर्मित। इसने 1507 में कन्नूर की प्रसिद्ध घेराबंदी का सफलतापूर्वक सामना किया।</li><li><strong>अंजादीप किला:</strong> गोवा के तट के पास मीठे पानी और जहाजों की मरम्मत के लिए 1505 में बनाया गया था, लेकिन बीजापुर के आदिल शाही सैनिकों के लगातार हमलों के कारण 1506 में इसे गिराकर छोड़ दिया गया।</li></ul>"
        },
        {
            "title": "4. चोल की लड़ाई (1508) और ममलुक हस्तक्षेप",
            "content": "<p><strong>भू-राजनीतिक संघर्ष की शुरुआत:</strong> लाल सागर में पुर्तगाली नाकेबंदी के कारण मिस्र की ममलुक सल्तनत का मसाला व्यापार बुरी तरह प्रभावित हुआ, जिसने मिस्र की अर्थव्यवस्था को खतरे में डाल दिया। वेनिस (जिसने स्वेज को जहाज निर्माण की लकड़ी दी थी) और ओटोमन तोपचियों के गुप्त सहयोग से ममलुकों ने स्वेज में एक युद्धपोत बेड़े का निर्माण किया। अमीर हुसैन अल-कुर्दी के नेतृत्व में यह बेड़ा भारत आया और गुजरात सल्तनत के दीव के गवर्नर मलिक अय्याज़ तथा कालीकट के ज़मोरिन के साथ गठबंधन किया।</p><p><strong>चोल का युद्ध और लॉरेंको की मृत्यु:</strong> मार्च 1508 में, इस संयुक्त गठबंधन ने चोल (Chaul) के उथले मुहाने में वायसराय के पुत्र लॉरेंको डी अल्मेडा के नेतृत्व वाले छोटे पुर्तगाली गश्ती दल पर अचानक हमला कर दिया। उथले पानी में पुर्तगाली जहाजों की गतिशीलता सीमित हो गई। लॉरेंको का प्रमुख जहाज <em>सेंटो एस्पिरिटो</em> एक केबल में फंस गया। पैर में गंभीर चोट लगने के बाद भी लॉरेंको ने आत्मसमर्पण करने से मना कर दिया और अंततः एक तोप के गोले की चपेट में आने से उनकी मृत्यु हो गई। यह पुर्तगालियों की पहली बड़ी नौसैनिक पराजय थी।</p>"
        },
        {
            "title": "5. दीव की लड़ाई (1509) और समुद्री शक्ति की विरासत",
            "content": "<p><strong>फ्रांसिस्को डी अल्मेडा का प्रतिशोध:</strong> अपने इकलौते पुत्र की मृत्यु से दुखी वायसराय फ्रांसिस्को डी अल्मेडा ने प्रतिशोध की प्रतिज्ञा ली। जब उनके उत्तराधिकारी अल्फांसो डी अल्बुकर्क 1508 के अंत में गवर्नर का पद संभालने के लिए शाही दस्तावेजों के साथ पहुंचे, तो अल्मेडा ने सत्ता सौंपने से इनकार कर दिया और उन्हें कोचीन के किले में कैद कर दिया। अल्मेडा ने 19 जहाजों और 1,300 सैनिकों का एक विशाल बेड़ा तैयार किया और गठबंधन बेड़े को नष्ट करने के लिए उत्तर की ओर बढ़ गए।</p><p><strong>दीव का निर्णायक युद्ध और विरासत:</strong> 3 फरवरी, 1509 को पुर्तगाली बेड़े का दीव के तट पर ममलुक-ओटोमन-गुजराती गठबंधन के साथ आमना-सामना हुआ। अपनी श्रेष्ठ तोप कला, भारी गोलाबारी और ऊंचे जहाजों का उपयोग करके अल्मेडा ने एक विनाशकारी विजय प्राप्त की। ममलुक बेड़ा पूरी तरह नष्ट हो गया और मलिक अय्याज़ को संधि करने, पुर्तगाली कैदियों को छोड़ने तथा भारी हर्जाना देने के लिए मजबूर होना पड़ा। दीव के इस युद्ध ने हिंद महासागर में यूरोपीय नौसैनिक वर्चस्व की नींव रखी जो अगले 400 वर्षों तक कायम रही। इसके बाद, अल्मेडा अल्बुकर्क को सत्ता सौंपकर पुर्तगाल के लिए रवाना हुए, लेकिन मार्च 1510 में दक्षिण अफ्रीका के टेबल बे में खोइखोई आदिवासियों के साथ पानी के विवाद में मारे गए।</p>"
        }
    ]
}

# Read generate_almeida_db.py content
with open(db_script_path, "r", encoding="utf-8") as f:
    code = f.read()

# Replace make_practice_questions
pattern = re.compile(r"def make_practice_questions\(\):.*?return en, hi", re.DOTALL)
code, count = pattern.subn(practice_code, code)
print(f"Replaced make_practice_questions: {count} times")

# Define the new deepDive dicts as strings in python formatting
deep_dive_en_str = repr(deep_dive_en)
deep_dive_hi_str = repr(deep_dive_hi)

# We want to replace the old deepDive inside en_data/hi_data structures
# Let's inject code at the end of the script before dump to overwrite them
override_code = f"""
# Injecting updated UPSC deep dives and practice questions
en_data['deepDive'] = {deep_dive_en_str}
en_data['deepDive']['sections'][0]['masteryZone'] = sec1_en
en_data['deepDive']['sections'][1]['masteryZone'] = sec2_en
en_data['deepDive']['sections'][2]['masteryZone'] = sec3_en
en_data['deepDive']['sections'][3]['masteryZone'] = sec4_en
en_data['deepDive']['sections'][4]['masteryZone'] = sec5_en

hi_data['deepDive'] = {deep_dive_hi_str}
hi_data['deepDive']['sections'][0]['masteryZone'] = sec1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = sec2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = sec3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = sec4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = sec5_hi
"""

# Let's locate the line "with open(os.path.join(BASE_DIR, 'content.json')" and put the override code right before it
write_pattern = "with open(os.path.join(BASE_DIR, 'content.json')"
if write_pattern in code:
    code = code.replace(write_pattern, override_code + "\n" + write_pattern)
    print("Injected override_code before writing json files.")
else:
    print("Error: Could not find JSON write pattern to inject override_code.")

# Write updated script back to generate_almeida_db.py
with open(db_script_path, "w", encoding="utf-8") as f:
    f.write(code)

print("SUCCESS: Finished patching generate_almeida_db.py")
