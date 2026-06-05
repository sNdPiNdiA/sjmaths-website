import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Harappan-Trade\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Harappan-Trade\hi\content.json"

ar_opts = [
    "Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A)",
    "Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A)",
    "Assertion (A) is true but Reason (R) is false",
    "Assertion (A) is false but Reason (R) is true",
    "Both Assertion (A) and Reason (R) are false"
]

hin_ar_opts = [
    "कथन (A) और कारण (R) दोनों सही हैं और कारण (R), कथन (A) की सही व्याख्या है।",
    "कथन (A) और कारण (R) दोनों सही हैं लेकिन कारण (R), कथन (A) की सही व्याख्या नहीं है।",
    "कथन (A) सही है लेकिन कारण (R) गलत है।",
    "कथन (A) गलत है लेकिन कारण (R) सही है।",
    "कथन (A) और कारण (R) दोनों गलत हैं।"
]

mcq_opts = [
    "1 only",
    "2 only",
    "Both 1 and 2",
    "Neither 1 nor 2"
]

hin_mcq_opts = [
    "1 केवल",
    "2 केवल",
    "1 और 2 दोनों",
    "न तो 1 न ही 2"
]

# =========================================================================
# SECTION 1: INTERNAL TRADE & PROCUREMENT STRATEGIES
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following sites was primarily established as a specialized resource outpost for shell procurement and shell-working?", ["Kalibangan", "Nageshwar", "Shortughai", "Banawali"], 1, "Nageshwar and Balakot were established close to the coast in shell-rich areas specifically for procuring shells and crafting shell objects."),
    ("The copper resources of the Khetri belt in Rajasthan were accessed by the Harappans primarily through which strategy?", ["Establishing direct military control", "Organizing localized expeditions to interact with indigenous communities", "Trading with Mesopotamian intermediaries", "Directly importing finished bronze goods from Central Asia"], 1, "Archaeologists believe the Harappans sent expeditions to the Khetri region to interact with the local Ganeshwar-Jodhpura culture and procure copper."),
    ("Which of the following materials was procured from southern Rajasthan and northern Gujarat for making typical rectangular Harappan seals?", ["Lapis Lazuli", "Steatite", "Carnelian", "Tin"], 1, "Steatite (or soapstone) was sourced from southern Rajasthan and northern Gujarat and was widely used for making seals."),
    ("What evidence suggests that the track gauges of Harappan bullock carts were highly standardized?", ["A written manual on cart manufacturing found at Harappa", "Fossilized clay wheel ruts showing widths ranging from 1.1 to 1.8 meters", "Mesopotamian depictions of Indus wheeled carts", "The discovery of identical metal axles at Lothal"], 1, "Fossilized ruts found in archaeological layers at sites like Harappa show track widths between 1.1 and 1.8 meters, matching modern South Asian bullock carts."),
    ("The Harappans procured gold primarily from which region of the Indian subcontinent?", ["Karnataka (Kolar / Nilgiris)", "Khetri (Rajasthan)", "Badakhshan (Afghanistan)", "Kathiawar (Gujarat)"], 0, "Gold was sourced from Karnataka (South India), particularly from regions close to the Kolar gold fields and the Nilgiris.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन सा स्थल मुख्य रूप से शंख (shell) की प्राप्ति और शंख-शिल्प के लिए एक विशिष्ट संसाधन चौकी के रूप में स्थापित किया गया था?", ["कालीबंगन", "नागेश्वर", "शोर्तुघई", "बनावली"], 1, "नागेश्वर और बालाकोट शंख संसाधनों से समृद्ध तटीय क्षेत्रों के निकट स्थापित किए गए थे ताकि शंख वस्तुओं का निर्माण किया जा सके।"),
    ("हड़प्पा वासियों ने मुख्य रूप से किस रणनीति के माध्यम से राजस्थान के खेत्री बेल्ट के तांबा संसाधनों तक पहुँच प्राप्त की?", ["प्रत्यक्ष सैन्य नियंत्रण स्थापित करके", "स्थानीय समुदायों के साथ संपर्क के लिए स्थानीय अभियानों का आयोजन करके", "मेसोपोटामिया के मध्यस्थों के साथ व्यापार करके", "मध्य एशिया से सीधे निर्मित कांस्य वस्तुओं का आयात करके"], 1, "पुरातत्वविदों का मानना है कि हड़प्पा वासियों ने खेत्री क्षेत्र में अभियान भेजे ताकि स्थानीय गणेश्वर-जोधपुरा संस्कृति के लोगों से संपर्क कर तांबा प्राप्त किया जा सके।"),
    ("निम्नलिखित में से कौन सी सामग्री दक्षिणी राजस्थान और उत्तरी गुजरात से विशिष्ट आयताकार हड़प्पा मुहरों को बनाने के लिए प्राप्त की जाती थी?", ["लाजवर्त (Lapis)", "सेलखड़ी (Steatite)", "अकीक (Carnelian)", "टीन"], 1, "सेलखड़ी (या सोपस्टोन) का आयात दक्षिणी राजस्थान और उत्तरी गुजरात से मुहरें बनाने के लिए किया जाता था।"),
    ("कौन सा साक्ष्य यह दर्शाता है कि हड़प्पा की बैलगाड़ियों के पहियों के बीच की दूरी अत्यधिक मानकीकृत थी?", ["हड़प्पा में मिली कार्ट निर्माण की एक लिखित नियमावली", "पुरातात्विक स्तरों में मिले पहियों के निशान जो 1.1 से 1.8 मीटर की चौड़ाई दर्शाते हैं", "मेसोपोटामिया के चित्रों में पहिए वाली गाड़ियों का अंकन", "लोथल में पाए गए एक समान धातु के एक्सल"], 1, "हड़प्पा और अन्य स्थलों से मिले पहियों के निशान 1.1 से 1.8 मीटर चौड़े हैं, जो आज की दक्षिण एशियाई बैलगाड़ियों के समान हैं।"),
    ("हड़प्पा वासियों ने मुख्य रूप से भारतीय उपमहाद्वीप के किस क्षेत्र से सोना प्राप्त किया?", ["कर्नाटक (कोलार / नीलगिरी)", "खेत्री (राजस्थान)", "बदख्शां (अफगानिस्तान)", "काठियावाड़ (गुजरात)"], 0, "सोने की प्राप्ति दक्षिण भारत (कर्नाटक) के कोलार स्वर्ण क्षेत्रों और नीलगिरी पहाड़ियों के पास से की जाती थी।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following animals were utilized by the Harappans as beasts of burden and for pulling agricultural or trade transport? (Select all that apply)", ["Humped cattle (oxen)", "Water buffalo", "Cheetah", "African elephant"], [0, 1], "Oxen (humped cattle) and buffaloes were domesticated and used for pulling carts. Cheetahs were wild and African elephants were not used."),
    ("Select the main sourcing sites within or near the Indian subcontinent for procuring copper for Harappan bronze metallurgy: (Select all that apply)", ["Khetri region of Rajasthan", "Baluchistan highland mines", "Karnataka gold fields", "Nilgiri hills"], [0, 1], "Copper was sourced from Khetri in Rajasthan and Baluchistan. Karnataka and Nilgiris were sources of gold."),
    ("Which of the following raw materials were sourced by the Harappans from the Saurashtra and Gujarat region? (Select all that apply)", ["Agate and Carnelian", "Marine shells", "Lapis Lazuli", "Pamir Jade"], [0, 1], "Gujarat provided carnelian/agate (from Ratanpur) and shells (from Nageshwar/Balakot). Lapis came from Afghanistan and Jade from Central Asia."),
    ("Which features characterized the Harappan weight system used in trade exchanges? (Select all that apply)", ["Lower denominations followed a binary system", "Higher denominations followed a decimal system", "Weights were predominantly made of chert", "Weights were shaped as hollow cylinders"], [0, 1, 2], "Lower denominations were binary (1, 2, 4, 8, 16, 32, up to 12800) and higher ones decimal. They were made of chert and were solid cubes, not hollow cylinders."),
    ("Identify the procurement outposts or resource processing centers established by the Harappans directly near raw material zones: (Select all that apply)", ["Shortughai in northern Afghanistan", "Nageshwar in Saurashtra", "Balakot on the Makran coast", "Ganeshwar in Rajasthan"], [0, 1, 2], "Shortughai (lapis), Nageshwar (shell), and Balakot (shell) were direct Harappan outposts. Ganeshwar was a non-Harappan indigenous site.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन जानवरों का उपयोग हड़प्पा वासियों द्वारा माल ढोने और कृषि या व्यापारिक परिवहन खींचने के लिए किया जाता था? (सभी लागू विकल्प चुनें)", ["कूबड़ वाले बैल", "भैंस", "चीता", "अफ्रीकी हाथी"], [0, 1], "बैल और भैंसों को पालतू बनाया गया था और गाड़ी खींचने के लिए उपयोग किया जाता था। चीता जंगली था और अफ्रीकी हाथी ज्ञात नहीं थे।"),
    ("हड़प्पा कांस्य धातु विज्ञान के लिए तांबा प्राप्त करने के लिए उपमहाद्वीप के भीतर या उसके पास के मुख्य स्रोतों का चयन करें: (सभी लागू विकल्प चुनें)", ["राजस्थान का खेत्री क्षेत्र", "बलूचिस्तान की पर्वतीय खदानें", "कर्नाटक के स्वर्ण क्षेत्र", "नीलगिरि पहाड़ियाँ"], [0, 1], "तांबा राजस्थान के खेत्री और बलूचिस्तान से प्राप्त किया जाता था। कर्नाटक और नीलगिरि सोने के स्रोत थे।"),
    ("निम्नलिखित में से कौन सा कच्चा माल हड़प्पा वासियों द्वारा सौराष्ट्र और गुजरात क्षेत्र से प्राप्त किया जाता था? (सभी लागू विकल्प चुनें)", ["अकीक (Agate) और कार्सिलियन (Carnelian)", "समुद्री शंख (Shells)", "लाजवर्त (Lapis Lazuli)", "पामीर का जेड (Jade)"], [0, 1], "गुजरात से अकीक/गोमेद और शंख मिलते थे। लाजवर्त अफगानिस्तान से और जेड पामीर से आता था।"),
    ("व्यापार विनिमय में प्रयुक्त हड़प्पा कालीन भार (बाट) प्रणाली की क्या विशेषताएं थीं? (सभी लागू विकल्प चुनें)", ["निचले मूल्य द्विआधारी (binary) प्रणाली पर आधारित थे", "उच्च मूल्य दशमलव (decimal) प्रणाली पर आधारित थे", "बाट मुख्य रूप से चर्ट (chert) पत्थर से बने थे", "बाट खोखले बेलनाकार आकार के थे"], [0, 1, 2], "निचले मूल्य द्विआधारी (1, 2, 4, 8, 16, 32...) और उच्च मूल्य दशमलव थे। वे ठोस घनाकार चर्ट पत्थर के थे, खोखले नहीं।"),
    ("कच्चे माल के क्षेत्रों के निकट हड़प्पा वासियों द्वारा स्थापित संसाधन चौकियों या प्रसंस्करण केंद्रों की पहचान करें: (सभी लागू विकल्प चुनें)", ["उत्तरी अफगानिस्तान में शोर्तुघई", "सौराष्ट्र में नागेश्वर", "मकरान तट पर बालाकोट", "राजस्थान में गणेश्वर"], [0, 1, 2], "शोर्तुघई (लाजवर्त), नागेश्वर (शंख) और बालाकोट (शंख) हड़प्पा की बस्तियां थीं। गणेश्वर गैर-हड़प्पा संस्कृति का स्थल था।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Harappans possessed standardized silver coins with value markings for large scale commercial transactions.", False, "False. The Harappans had no monetary system or coinage; all trade was conducted via barter."),
    ("Steatite, used for making Harappan seals, is a very soft stone that could be easily carved.", True, "True. Steatite is a magnesium-rich talc rock (soapstone) that is exceptionally soft and easy to engrave."),
    ("Fossilized clay wheel ruts showing track widths matching modern South Asian bullock carts have been excavated.", True, "True. Excavations have revealed ruts measuring about 1.1 to 1.8 meters apart, mirroring modern track widths."),
    ("Nageshwar was an inland trading outpost located in the dry plains of northern Punjab specializing in lapis lazuli.", False, "False. Nageshwar is a coastal site in Gujarat specializing in shell-working."),
    ("The cubical weights used by Harappan merchants were made from a fine-grained stone called chert.", True, "True. Chert was the most common stone utilized for manufacturing highly standardized cubical weights."),
    ("The higher denominations of the Harappan weights followed a binary progression (1, 2, 4, 8, 16...).", False, "False. The lower denominations followed binary ratios (1 to 64, then 160, 320...), while higher values followed a decimal pattern."),
    ("Water-based riverine transport was completely absent inside the Indus basin.", False, "False. Flat-bottomed river boats were widely used to transport grain and goods along the Indus and Ghaggar-Hakra systems."),
    ("The Ganeshwar-Jodhpura culture of Rajasthan supplied copper to the Harappans.", True, "True. This indigenous copper-producing culture of Rajasthan traded copper with the Harappans in exchange for finished items.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("बड़े पैमाने पर व्यावसायिक लेन-देन के लिए हड़प्पा वासियों के पास मूल्य चिह्नों वाले मानकीकृत चांदी के सिक्के थे।", False, "असत्य। हड़प्पा वासियों के पास कोई मौद्रिक प्रणाली या सिक्के नहीं थे; सारा व्यापार वस्तु विनिमय पर आधारित था।"),
    ("मुहरों के निर्माण में प्रयुक्त सेलखड़ी (Steatite) एक बहुत ही नरम पत्थर है जिसे आसानी से तराशा जा सकता था।", True, "सत्य। सेलखड़ी एक खनिज पत्थर (सोपस्टोन) है जो बहुत नरम होता है और इस पर नक्काशी करना आसान होता है।"),
    ("पुरातात्विक खुदाई में पहियों के ऐसे जीवाश्म निशान मिले हैं जिनकी दूरी आधुनिक दक्षिण एशियाई बैलगाड़ियों के समान है।", True, "सत्य। खुदाई में लगभग 1.1 से 1.8 मीटर की दूरी वाले पहियों के निशान मिले हैं जो आधुनिक बैलगाड़ियों जैसे हैं।"),
    ("नागेश्वर पंजाब के सूखे मैदानों में स्थित लाजवर्त के लिए प्रसिद्ध एक अंतर्देशीय व्यापारिक चौकी थी।", False, "असत्य। नागेश्वर गुजरात में स्थित एक तटीय स्थल है जो शंख-शिल्प के लिए प्रसिद्ध था।"),
    ("हड़प्पा व्यापारियों द्वारा उपयोग किए जाने वाले घनाकार बाट चर्ट (chert) नामक बारीक दानेदार पत्थर से बनाए जाते थे।", True, "सत्य। चर्ट पत्थर का उपयोग करके अत्यधिक मानकीकृत घनाकार बाट बनाए जाते थे।"),
    ("हड़प्पा भार प्रणाली के उच्च मूल्य द्विआधारी (binary) अनुक्रम (1, 2, 4, 8, 16...) का पालन करते थे।", False, "असत्य। निचले भार द्विआधारी अनुपात का पालन करते थे, जबकि उच्च भार दशमलव (decimal) अनुक्रम के थे।"),
    ("सिंधु बेसिन के भीतर जल-आधारित नदी परिवहन का पूर्ण अभाव था।", False, "असत्य। सिंधु और घग्गर-हकरा नदी प्रणालियों में अनाज और माल ढोने के लिए चपटी नावों का व्यापक उपयोग होता था।"),
    ("राजस्थान की गणेश्वर-जोधपुरा संस्कृति हड़प्पा वासियों को तांबे की आपूर्ति करती थी।", True, "सत्य। राजस्थान की इस तांबा-उत्पादक संस्कृति ने हड़प्पा वासियों को तांबा दिया और बदले में हड़प्पा की वस्तुएं प्राप्त कीं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The coastal site of ________ in Gujarat was a specialized settlement for shell procurement and shell-working.", "Nageshwar", "Nageshwar (and Balakot) were designated shell-working outposts."),
    ("While lower weights followed a binary system, higher weights followed a ________ system.", "decimal", "The higher scale of weights was regulated by a decimal system."),
    ("Copper resources were procured from the ________ mines in Rajasthan.", "Khetri", "The Khetri copper belt was a key mining zone."),
    ("Harappan inland land transport relied on wooden carts with solid wheels pulled by ________.", "oxen", "Oxen/bullocks were the primary draft animals used for carts."),
    ("The soft magnesium-rich soapstone used to carve Harappan seals is ________.", "steatite", "Steatite was carved and heated to form white glazed seals."),
    ("Highly standardized weights were predominantly manufactured from a hard stone called ________.", "chert", "Chert was selected due to its durability and resistance to wear."),
    ("The precious metal gold was procured from the Kolar fields located in ________.", "Karnataka", "Karnataka (South India) was the source of gold."),
    ("The Mature Harappan trade was conducted without coins via a system of ________.", "barter", "Goods were directly exchanged through a regulated barter system.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("गुजरात का तटीय स्थल ________ शंख की प्राप्ति और शंख-शिल्प के लिए एक विशिष्ट बस्ती थी।", "नागेश्वर", "नागेश्वर (और मकरान तट पर बालाकोट) शंख-शिल्प के केंद्र थे।"),
    ("जबकि निचले भार द्विआधारी प्रणाली का पालन करते थे, उच्च भार ________ प्रणाली पर आधारित थे।", "दशमलव", "हड़प्पा भार प्रणाली में उच्च मूल्य दशमलव अंतराल पर आधारित थे।"),
    ("तांबा संसाधन मुख्य रूप से राजस्थान की ________ खदानों से प्राप्त किए जाते थे।", "खेत्री", "राजस्थान का खेत्री बेल्ट प्रमुख तांबा स्रोत था।"),
    ("हड़प्पा थल परिवहन ठोस पहियों वाली लकड़ी की गाड़ियों पर निर्भर था जिन्हें ________ द्वारा खींचा जाता था।", "बैलों", "बैलों (oxen) का प्रयोग गाड़ियों को खींचने के लिए किया जाता था।"),
    ("हड़प्पा की मुहरों को तराशने के लिए प्रयुक्त नरम पत्थर को ________ कहा जाता है।", "सेलखड़ी", "सेलखड़ी (steatite) को तराश कर पकाया जाता था।"),
    ("अत्यधिक मानकीकृत बाट मुख्य रूप से ________ नामक कठोर पत्थर से बनाए जाते थे।", "चर्ट", "बाटों के निर्माण के लिए चर्ट (chert) का उपयोग किया जाता था।"),
    ("बहुमूल्य धातु सोना दक्षिण भारत के ________ में स्थित कोलार खदानों से प्राप्त किया जाता था।", "कर्नाटक", "सोना कर्नाटक (दक्षिण भारत) से मँगाया जाता था।"),
    ("परिपक्व हड़प्पा काल में व्यापार सिक्कों के बिना ________ प्रणाली द्वारा संचालित होता था।", "वस्तु विनिमय", "व्यापारिक लेनदेन मानकीकृत वस्तु विनिमय (barter) पर आधारित था।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the raw materials with their primary sourcing regions inside the Indian subcontinent:",
        "items": [{"left": "I. Copper", "key": "A"}, {"left": "II. Gold", "key": "B"}, {"left": "III. Shell", "key": "C"}],
        "options": [{"val": "A", "text": "A. Khetri mines (Rajasthan)"}, {"val": "B", "text": "B. Kolar fields (Karnataka)"}, {"val": "C", "text": "C. Saurashtra coast (Gujarat)"}],
        "sol": "Copper was procured from Khetri, gold from Karnataka, and shell from Gujarat coast."
    },
    {
        "type": "Match the Following",
        "q": "Match the Harappan sites with their specialized trade roles:",
        "items": [{"left": "I. Nageshwar", "key": "A"}, {"left": "II. Shortughai", "key": "B"}, {"left": "III. Ratanpur", "key": "C"}],
        "options": [{"val": "A", "text": "A. Shell procurement outpost"}, {"val": "B", "text": "B. Lapis Lazuli colony"}, {"val": "C", "text": "C. Carnelian resource center"}],
        "sol": "Nageshwar was for shell, Shortughai for lapis lazuli, and Ratanpur in Gujarat for carnelian."
    },
    {
        "type": "Match the Following",
        "q": "Match the materials with the commercial items manufactured from them:",
        "items": [{"left": "I. Chert", "key": "A"}, {"left": "II. Steatite", "key": "B"}, {"left": "III. Carnelian", "key": "C"}],
        "options": [{"val": "A", "text": "A. Standardized weights"}, {"val": "B", "text": "B. Carved seals"}, {"val": "C", "text": "C. Etched beads"}],
        "sol": "Chert was used for weights, steatite for seals, and carnelian for beads."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "कच्चे माल को उपमहाद्वीप के भीतर उनके संबंधित स्रोत क्षेत्रों से सुमेलित करें:",
        "items": [{"left": "I. तांबा", "key": "A"}, {"left": "II. सोना", "key": "B"}, {"left": "III. शंख (Shell)", "key": "C"}],
        "options": [{"val": "A", "text": "A. खेत्री खदानें (राजस्थान)"}, {"val": "B", "text": "B. कोलार क्षेत्र (कर्नाटक)"}, {"val": "C", "text": "C. सौराष्ट्र तट (गुजरात)"}],
        "sol": "तांबा खेत्री से, सोना कर्नाटक से और शंख गुजरात तट से प्राप्त किया जाता था।"
    },
    {
        "type": "Match the Following",
        "q": "हड़प्पा स्थलों को उनकी विशिष्ट व्यापारिक भूमिकाओं से सुमेलित करें:",
        "items": [{"left": "I. नागेश्वर", "key": "A"}, {"left": "II. शोर्तुघई", "key": "B"}, {"left": "III. रतनपुर", "key": "C"}],
        "options": [{"val": "A", "text": "A. शंख प्राप्ति चौकी"}, {"val": "B", "text": "B. लाजवर्त (Lapis) उपनिवेश"}, {"val": "C", "text": "C. अकीक (Carnelian) संसाधन केंद्र"}],
        "sol": "नागेश्वर शंख के लिए, शोर्तुघई लाजवर्त के लिए और रतनपुर अकीक के लिए था।"
    },
    {
        "type": "Match the Following",
        "q": "सामग्रियों को उनसे निर्मित वाणिज्यिक वस्तुओं से सुमेलित करें:",
        "items": [{"left": "I. चर्ट (Chert)", "key": "A"}, {"left": "II. सेलखड़ी (Steatite)", "key": "B"}, {"left": "III. कार्सिलियन (Carnelian)", "key": "C"}],
        "options": [{"val": "A", "text": "A. मानकीकृत बाट (Weights)"}, {"val": "B", "text": "B. नक्काशीदार मुहरें (Seals)"}, {"val": "C", "text": "C. अलंकृत मनके (Beads)"}],
        "sol": "चर्ट से बाट, सेलखड़ी से मुहरें और कार्सिलियन से मनके बनाए जाते थे।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which durable stone was primarily used to manufacture Harappan weights?", "Chert."),
    ("From which southern Indian state did the Harappans procure gold?", "Karnataka."),
    ("In which modern Indian state is the Khetri copper belt located?", "Rajasthan."),
    ("What exchange mechanism was used for trade transactions in the absence of coins?", "The barter system."),
    ("Which animals pulled the solid-wheeled transport carts?", "Oxen (bullocks)."),
    ("Which coastal Gujarat site was established as a shell-working outpost?", "Nageshwar."),
    ("Name the soft soapstone widely used to carve Harappan seals.", "Steatite."),
    ("Did the Harappans use paper money or metal coins for local trade?", "No.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा बाटों के निर्माण के लिए मुख्य रूप से किस पत्थर का उपयोग किया जाता था?", "चर्ट।"),
    ("हड़प्पा वासी सोने की खरीद किस दक्षिण भारतीय राज्य से करते थे?", "कर्नाटक।"),
    ("खेत्री तांबा बेल्ट आधुनिक भारत के किस राज्य में स्थित है?", "राजस्थान।"),
    ("सिक्कों की अनुपस्थिति में व्यापारिक लेनदेन के लिए किस प्रणाली का उपयोग किया जाता था?", "वस्तु विनिमय (Barter) प्रणाली।"),
    ("ठोस पहियों वाली परिवहन गाड़ियों को कौन से जानवर खींचते थे?", "बैल।"),
    ("गुजरात का कौन सा तटीय स्थल शंख-शिल्प चौकी के रूप में स्थापित किया गया था?", "नागेश्वर।"),
    ("हड़प्पा मुहरों को तराशने के लिए प्रयुक्त होने वाले नरम पत्थर का नाम बताएं।", "सेलखड़ी (Steatite)।"),
    ("क्या हड़प्पा वासी स्थानीय व्यापार के लिए कागजी मुद्रा या धातु के सिक्कों का उपयोग करते थे?", "नहीं।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Harappans established outposts in distant locations like Shortughai.\nReason (R): They sought to secure direct access to valuable raw materials such as lapis lazuli.", 0, "Both A and R are true and R explains why outposts like Shortughai were established in resource-rich areas."),
    ("Assertion (A): The Harappan weight system was highly standardized across vast geographic distances.\nReason (R): Standardized weights were crucial to maintain equity and prevent disputes in a complex barter trade.", 0, "Both A and R are true and standardizing weights was necessary to regulate value exchanges in a barter system."),
    ("Assertion (A): Gold objects were cheap and owned by all segments of the Harappan population.\nReason (R): Gold was imported from the far southern part of the peninsula and was a highly valued luxury item.", 3, "A is false because gold was a luxury item limited to elites, while R is true."),
    ("Assertion (A): Steatite was the preferred material for carving detailed Harappan seals.\nReason (R): Steatite is a very soft stone that easily yields to fine engravings and hardens upon firing.", 0, "Both A and R are true and steatite's soft nature made it perfect for intricate seal designs."),
    ("Assertion (A): The Harappan civilization lacked any form of wheeled land carriage.\nReason (R): Terracotta models and clay ruts prove the widespread use of solid-wheeled bullock carts.", 3, "A is false as wheeled carts were common, and R is true."),
    ("Assertion (A): Copper was primarily imported from the gold-rich Nilgiri hills of South India.\nReason (R): Copper was procured from the Khetri belt in Rajasthan and from mining zones in Baluchistan.", 3, "A is false because copper came from Rajasthan/Baluchistan, and R is true."),
    ("Assertion (A): Nageshwar and Balakot were established in the inland deserts to control crop trading.\nReason (R): They were coastal settlements located strategically near marine shell resource zones.", 3, "A is false since they were coastal shell centers, and R is true."),
    ("Assertion (A): Riverine transport was vital for the domestic movement of agricultural grains.\nReason (R): Flat-bottomed river boats allowed bulk cargo to be shipped cheaper and faster than overland bullock carts.", 0, "Both A and R are true and river shipping was the most efficient way to transport heavy bulk crops between cities.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा वासियों ने शोर्तुघई जैसी सुदूर जगहों पर व्यापारिक चौकियाँ स्थापित कीं।\nकारण (R): वे लाजवर्त जैसे मूल्यवान कच्चे माल तक सीधी पहुँच प्राप्त करना चाहते थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि संसाधन प्राप्ति के लिए उपनिवेश बनाए गए थे।"),
    ("कथन (A): हड़प्पा भार प्रणाली विशाल भौगोलिक दूरियों के बावजूद अत्यधिक मानकीकृत थी।\nकारण (R): एक जटिल वस्तु विनिमय प्रणाली में विवादों को रोकने और संतुलन बनाए रखने के लिए मानकीकृत बाट आवश्यक थे।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि वस्तु विनिमय के सुचारू संचालन के लिए बाटों का एक समान होना जरूरी था।"),
    ("कथन (A): सोने की वस्तुएं सस्ती थीं और हड़प्पा की संपूर्ण आबादी के पास मौजूद थीं।\nकारण (R): सोना प्रायद्वीप के सुदूर दक्षिणी भाग से आयात किया जाता था और यह एक मूल्यवान विलासिता की वस्तु थी।", 3, "A गलत है क्योंकि सोना केवल अभिजात वर्ग के पास था, जबकि R सही है।"),
    ("कथन (A): हड़प्पा की विस्तृत मुहरों को तराशने के लिए सेलखड़ी (Steatite) पसंदीदा सामग्री थी।\nकारण (R): सेलखड़ी एक बहुत ही नरम पत्थर है जो बारीक नक्काशी के अनुकूल होता है और पकाने पर सख्त हो जाता है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा सभ्यता में पहिए वाले थल परिवहन का पूर्ण अभाव था।\nकारण (R): मिट्टी के खिलौने और पहियों के निशान ठोस पहियों वाली बैलगाड़ियों के व्यापक उपयोग को साबित करते हैं।", 3, "A गलत है क्योंकि गाड़ियाँ मौजूद थीं, जबकि R सही है।"),
    ("कथन (A): तांबा मुख्य रूप से दक्षिण भारत की नीलगिरि पहाड़ियों से आयात किया जाता था।\nकारण (R): तांबा राजस्थान के खेत्री बेल्ट और बलूचिस्तान के खनन क्षेत्रों से प्राप्त किया जाता था।", 3, "A गलत है क्योंकि तांबा खेत्री/बलूचिस्तान से आता था, और R सही है।"),
    ("कथन (A): नागेश्वर और बालाकोट अनाज व्यापार को नियंत्रित करने के लिए अंतर्देशीय मरुस्थलों में स्थापित किए गए थे।\nकारण (R): वे समुद्री शंख संसाधन क्षेत्रों के पास रणनीतिक रूप से स्थित तटीय बस्तियां थीं।", 3, "A गलत है क्योंकि वे तटीय शंख केंद्र थे, और R सही है।"),
    ("कथन (A): कृषि खाद्यान्नों के घरेलू परिवहन के लिए नदी परिवहन अत्यंत महत्वपूर्ण था।\nकारण (R): चपटे तल वाली नावें बैलगाड़ियों की तुलना में भारी सामान को सस्ता और तेज गति से ले जाने में सक्षम थीं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The Harappan weights were spherical and made of polished iron.\nStatement 2: The weights were regulated by a centralized system without any local variations.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: weights were cubical and made of chert, not iron. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: The Khetri region of Rajasthan supplied copper to Harappan urban sites.\nStatement 2: The Ganeshwar-Jodhpura culture shows non-Harappan pottery but traded copper with Harappans.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. The Ganeshwar-Jodhpura culture was an indigenous non-Harappan group that acted as a copper sourcing partner."),
    ("Consider the following statements:\nStatement 1: Shortughai was a Harappan outpost located in the coastal delta of Gujarat.\nStatement 2: Nageshwar was a shell-working site located in northern Afghanistan.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. Shortughai was in Afghanistan and Nageshwar was in Gujarat (reversed positions)."),
    ("Consider the following statements:\nStatement 1: Shell bangles and ladles manufactured at Nageshwar and Balakot were traded to inland cities like Mohenjo-daro.\nStatement 2: Marine shells were imported from Mesopotamia to make ornaments.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: shells were sourced locally from the Arabian Sea coast, not imported from Mesopotamia."),
    ("Consider the following statements:\nStatement 1: The Harappans developed a system of copper coinage to conduct daily local trade.\nStatement 2: Paper-like birch-bark notes were used as currency denominations.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. The Harappans had no coinage or paper currency; they used barter.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा के बाट गोलाकार थे और पॉलिश किए गए लोहे से बने थे।\nकथन 2: बाटों को बिना किसी स्थानीय भिन्नता के एक केंद्रीकृत प्रणाली द्वारा नियंत्रित किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि बाट घनाकार और चर्ट पत्थर के थे, लोहे के नहीं। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: राजस्थान के खेत्री क्षेत्र ने हड़प्पा के शहरी स्थलों को तांबे की आपूर्ति की।\nकथन 2: गणेश्वर-जोधपुरा संस्कृति गैर-हड़प्पा शैली के बर्तन दिखाती है लेकिन उसने हड़प्पा वासियों के साथ तांबे का व्यापार किया।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। गणेश्वर-जोधपुरा संस्कृति एक स्थानीय समूह थी जिसने हड़प्पा वासियों को तांबा दिया था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: शोर्तुघई गुजरात के तटीय डेल्टा में स्थित एक हड़प्पा चौकी थी।\nकथन 2: नागेश्वर उत्तरी अफगानिस्तान में स्थित एक शंख-शिल्प स्थल था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं क्योंकि शोर्तुघई अफगानिस्तान में था और नागेश्वर गुजरात में था (स्थान बदल दिए गए हैं)।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: नागेश्वर और बालाकोट में बने शंख के कंगन और करछुल अंतर्देशीय शहरों जैसे मोहनजोदड़ो में भेजे जाते थे।\nकथन 2: आभूषण बनाने के लिए मेसोपोटामिया से समुद्री शंख आयात किए जाते थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शंख अरब सागर के तटों से स्थानीय रूप से एकत्र किए जाते थे, मेसोपोटामिया से नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा वासियों ने दैनिक स्थानीय व्यापार संचालित करने के लिए तांबे के सिक्कों की प्रणाली विकसित की थी।\nकथन 2: मुद्रा के रूप में भोजपत्र (birch-bark) के नोटों का उपयोग किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। हड़प्पा वासियों के पास कोई सिक्के या कागजी मुद्रा नहीं थी; वे वस्तु विनिमय का उपयोग करते थे।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans establish coastal outposts like Nageshwar and Balakot far from the core Indus plains?", "These outposts were placed directly near marine shell resource zones. Establishing specialized settlements allowed the Harappans to control shell procurement and process raw shells into finished goods (bangles, ladles) before transporting them inland."),
    ("Why was chert preferred over other stone varieties for manufacturing Harappan weights?", "Chert is a very hard, dense, and fine-grained sedimentary rock. It resists chipping, fracturing, and weathering, ensuring that the standardized weights remained accurate over long periods of commercial use."),
    ("Why was the Khetri copper belt crucial to the Harappan bronze-making industry?", "The Khetri belt in Rajasthan was the richest and most accessible copper deposit near the Indus valley. By sending expeditions to interact with the local Ganeshwar culture, the Harappans secured the copper necessary to alloy with tin to make bronze tools.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने मुख्य सिंधु मैदानों से दूर नागेश्वर और बालाकोट जैसी तटीय चौकियाँ क्यों स्थापित कीं?", "ये चौकियाँ सीधे समुद्री शंख संसाधन क्षेत्रों के पास स्थापित की गई थीं। विशिष्ट बस्तियाँ बसाने से हड़प्पा वासियों को शंख की खरीद को नियंत्रित करने और कच्चे शंखों को अंतर्देशीय शहरों में भेजने से पहले आभूषणों में बदलने की सुविधा मिली।"),
    ("हड़प्पा बाटों (Weights) के निर्माण के लिए अन्य पत्थरों की तुलना में चर्ट (Chert) को क्यों प्राथमिकता दी गई?", "चर्ट एक बहुत ही कठोर, सघन और सूक्ष्म कणों वाला अवसादी पत्थर है। यह टूटने, घिसने और मौसमी प्रभावों का प्रतिरोध करता है, जिससे यह सुनिश्चित होता था कि लंबे समय तक उपयोग के बाद भी बाटों का वजन सटीक बना रहे।"),
    ("हड़प्पा कांस्य निर्माण उद्योग के लिए राजस्थान का खेत्री तांबा क्षेत्र क्यों महत्वपूर्ण था?", "राजस्थान का खेत्री बेल्ट सिंधु घाटी के निकट तांबे का सबसे समृद्ध और सुलभ स्रोत था। यहाँ अभियानों को भेजकर हड़प्पा वासियों ने वह तांबा प्राप्त किया जो कांस्य उपकरण बनाने के लिए टीन के साथ मिलाने के लिए आवश्यक था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the lack of metallic currency affect the regulation of Harappan internal trade?", "The absence of currency meant that trade was based entirely on barter. To keep exchanges fair and trusted, the state regulated the barter system through a highly standardized and uniform weight system of cubical chert weights."),
    ("How did riverine transport support land-based transport in Harappan domestic trade?", "Rivers like the Indus and Ghaggar-Hakra allowed flat-bottomed boats to move bulk, heavy goods like grains and timber easily over long distances, whereas land-based bullock carts handled localized haulage or routes away from rivers."),
    ("How were steatite seals manufactured and finished to achieve their distinctive appearance?", "Artisans carved designs in reverse (intaglio) onto soft steatite blocks. The seals were then coated with a chemical paste and fired in a kiln. This process hardened the soft steatite and gave it a durable, glazed white coat.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("धातु की मुद्रा के अभाव ने हड़प्पा के आंतरिक व्यापार के नियंत्रण को कैसे प्रभावित किया?", "सिक्कों की अनुपस्थिति का अर्थ था कि व्यापार पूरी तरह से वस्तु विनिमय पर आधारित था। इस विनिमय को निष्पक्ष और विश्वसनीय बनाए रखने के लिए, राज्य ने चर्ट के घनाकार बाटों की एक अत्यधिक मानकीकृत भार प्रणाली द्वारा इसे नियंत्रित किया।"),
    ("हड़प्पा के घरेलू व्यापार में नदी परिवहन ने थल-आधारित परिवहन को कैसे सहयोग प्रदान किया?", "सिंधु और घग्गर जैसी नदियों ने चपटी नावों को अनाज और लकड़ी जैसी भारी वस्तुओं को लंबी दूरी तक आसानी से ले जाने की अनुमति दी, जबकि थल मार्ग की बैलगाड़ियाँ छोटी दूरियों और नदियों से दूर के क्षेत्रों का परिवहन संभालती थीं।"),
    ("हड़प्पा की सेलखड़ी (Steatite) मुहरों का निर्माण और उन पर चमक लाने का काम कैसे किया जाता था?", "कारीगर सेलखड़ी के टुकड़ों पर उल्टी नक्काशी करते थे। इसके बाद मुहरों पर एक रासायनिक लेप लगाया जाता था और उन्हें भट्टी में पकाया जाता था। इस प्रक्रिया से सेलखड़ी कठोर हो जाती थी और उसे एक चमकदार सफेद आवरण मिलता था।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Ganeshwar-Jodhpura Culture and Copper Sourcing. Analyze the relation.", "Located in northeastern Rajasthan, the Ganeshwar-Jodhpura culture shows non-Harappan pottery and high copper wealth. Rather than colonizing the area, the Harappans maintained trade contacts, obtaining copper sheets in exchange for pottery and finished bronze ornaments, illustrating peaceful coexistence."),
    ("Case Study: Nageshwar Coastal Shell-Working. Analyze its industrial layout.", "Excavations at Nageshwar reveal massive dumps of shell waste, including shells of Turbinella pyrum. The layout shows houses focused on manufacturing bangles and beads. The lack of agricultural tools suggests that the site was dependent on food imports, functioning purely as an industrial export outpost."),
    ("Case Study: The Metrological Standardization of Weights. Discuss the system.", "Harappan weights show remarkable consistency across Pakistan and northwestern India. Ratios follow a binary system for lower values (1, 2, 4, 8, 16, 32, 64) and decimal values for higher units (160, 200, 320, 640...). This strict consistency across cities indicates centralized political or mercantile regulation.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: गणेश्वर-जोधपुरा संस्कृति और तांबा प्राप्ति। इसके संबंधों का विश्लेषण करें।", "उत्तर-पूर्वी राजस्थान में स्थित गणेश्वर-जोधपुरा संस्कृति में गैर-हड़प्पा शैली के मृदभांड और भारी मात्रा में तांबे के उपकरण मिले हैं। हड़प्पा वासियों ने इस क्षेत्र पर कब्जा करने के बजाय व्यापारिक संबंध बनाए रखे और तांबा प्राप्त किया, जो शांतिपूर्ण सह-अस्तित्व को दर्शाता है।"),
    ("केस स्टडी: नागेश्वर तटीय शंख-शिल्प केंद्र। इसके औद्योगिक स्वरूप का विश्लेषण करें।", "नागेश्वर में खुदाई से शंख के कचरे (waste debris) के विशाल ढेर मिले हैं। यहाँ के घरों का मुख्य काम शंख से कंगन और मनके बनाना था। यहाँ कृषि उपकरणों की कमी यह दर्शाती है कि यह बस्ती भोजन के लिए अन्य शहरों पर निर्भर थी और पूरी तरह से औद्योगिक केंद्र थी।"),
    ("केस स्टडी: भार (बाट) प्रणाली का मानकीकरण। इसके महत्व पर चर्चा करें।", "हड़प्पा के बाटों में पूरे उपमहाद्वीप में अद्भुत समानता दिखती है। निचले बाट द्विआधारी (1, 2, 4, 8, 16...) और उच्च मूल्य दशमलव (160, 200, 320...) थे। शहरों के बीच यह सख्त समानता एक केंद्रीय राजनीतिक या व्यापारिक नियंत्रण का संकेत देती है।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Resource Expeditions versus Resource Colonies.", "Explain to students that the Harappans used two strategies to procure materials: (1) expeditions to areas with local populations (like Khetri for copper) to trade, and (2) establishing direct colonies in uninhabited areas containing specific materials (like Shortughai for lapis or Nageshwar for shells)."),
    ("Teach the Concept: The Binary-Decimal Metrology of Indus Valley.", "Teach the mathematical structure of Harappan weights. Lower weights doubled (1, 2, 4, 8, 16, 32, 64) where the unit weight was about 0.86 grams. Once they reached the 16th ratio (equivalent to value 16), the system transitioned into a decimal structure for heavy bulk items."),
    ("Teach the Concept: Bullock Cart Track Gauge Standardization.", "Explain how archaeologists reconstruct ancient roadways using terracotta toy models of carts and fossilized ruts. The constant track width of 1.1 to 1.8 meters across remote sites suggests that carts were designed to fit standardized road sizes, facilitating long-distance transport.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: संसाधन अभियान बनाम संसाधन उपनिवेश।", "छात्रों को समझाएं कि हड़प्पा वासियों के पास संसाधन जुटाने की दो रणनीतियां थीं: (1) स्थानीय आबादी वाले क्षेत्रों में अभियान भेजना (जैसे तांबे के लिए खेत्री) और (2) विशिष्ट खनिज संपन्न लेकिन निर्जन क्षेत्रों में सीधे बस्तियाँ स्थापित करना (जैसे लाजवर्त के लिए शोर्तुघई या शंख के लिए नागेश्वर)।"),
    ("अवधारणा सिखाएं: सिंधु घाटी की द्विआधारी-दशमलव भार प्रणाली।", "हड़प्पा बाटों की गणितीय संरचना को समझाएं। निचले बाटों का अनुपात दोगुना होता था (1, 2, 4, 8, 16, 32, 64) जहाँ इकाई बाट का वजन लगभग 0.86 ग्राम था। जब वे 16वें अनुपात (मूल्य 16) तक पहुँचते थे, तो भारी थोक वस्तुओं के मापन के लिए प्रणाली दशमलव संरचना में बदल जाती थी।"),
    ("अवधारणा सिखाएं: बैलगाड़ी के पहियों के बीच की चौड़ाई का मानकीकरण।", "समझाएं कि पुरातत्वविद मिट्टी की खिलौना गाड़ियों और पहियों के जीवाश्म निशानों से सड़कों का पुनर्निर्माण कैसे करते हैं। विभिन्न स्थलों पर पहियों के निशानों की चौड़ाई का 1.1 से 1.8 मीटर होना यह दर्शाता है कि गाड़ियाँ सड़कों के मानकों के अनुसार बनाई जाती थीं।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: OVERLAND TRADE & CENTRAL ASIAN NETWORKS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which mountain pass served as the primary overland trading corridor linking the Indus plains to the Quetta valley and Baluchistan highlands?", ["Bolan Pass", "Khyber Pass", "Palghat Pass", "Shipki La"], 0, "The Bolan Pass was the primary overland route connecting the Indus valley plains with Baluchistan and the Iranian plateau."),
    ("The Bactria-Margiana Archaeological Complex (BMAC), which traded extensively with the Harappans, was located in which river valley?", ["Oxus River Valley (Amu Darya)", "Tigris-Euphrates River Valley", "Nile River Valley", "Helmand River Valley"], 0, "The BMAC (also known as the Oxus Civilisation) was situated in the Oxus River basin in Central Asia (northern Afghanistan/Uzbekistan)."),
    ("Which city on the Iranian plateau (Sistan) served as an important transit and processing hub for Harappan lapis lazuli?", ["Shahr-i Sokhta", "Susa", "Persepolis", "Tepe Yahya"], 0, "Shahr-i Sokhta in Sistan (Iran) was a major trade hub where raw lapis lazuli was cut and polished before being exported further west."),
    ("Which of the following semi-precious green stones was imported overland by the Harappans from Central Asia or the Pamir region?", ["Jade", "Carnelian", "Lapis Lazuli", "Turquoise"], 0, "Jade was imported from Central Asia and the Pamir mountains, demonstrating the extensive reach of Harappan overland networks."),
    ("What was the primary geographical source of the turquoise imported by the Harappans?", ["Khorasan (Nishapur) in northeastern Iran", "Kolar fields of Karnataka", "Badakhshan in Afghanistan", "Khetri in Rajasthan"], 0, "Turquoise was imported overland from Khorasan (Nishapur) in northeastern Iran and parts of Central Asia.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("कौन सा पहाड़ी दर्रा सिंधु मैदानों को क्वेटा घाटी और बलूचिस्तान के पर्वतीय क्षेत्रों से जोड़ने वाला मुख्य थल व्यापारिक मार्ग था?", ["बोलन दर्रा", "खैबर दर्रा", "पालघाट दर्रा", "शिपकी ला"], 0, "बोलन दर्रा सिंधु घाटी के मैदानों को बलूचिस्तान और ईरानी पठार से जोड़ने वाला प्राथमिक मार्ग था।"),
    ("हड़प्पा वासियों के साथ व्यापक व्यापार करने वाला 'बैक्टीरिया-मार्गियाना पुरातात्विक परिसर' (BMAC) किस नदी घाटी में स्थित था?", ["आक्सस नदी घाटी (अमु दरिया)", "दजला-फरात नदी घाटी", "नील नदी घाटी", "हेलमंद नदी घाटी"], 0, "BMAC (जिसे आक्सस सभ्यता भी कहा जाता है) मध्य एशिया में आक्सस (अमु दरिया) नदी बेसिन में स्थित था।"),
    ("ईरानी पठार (सीस्तान) का कौन सा शहर हड़प्पा के लाजवर्त (Lapis) पत्थर के लिए एक महत्वपूर्ण पारगमन और प्रसंस्करण केंद्र था?", ["शहर-ए-सोख्ता", "सुसा", "पर्सेपोलिस", "तेपे याह्या"], 0, "सीस्तान (ईरान) में स्थित शहर-ए-सोख्ता एक प्रमुख व्यापारिक केंद्र था जहाँ लाजवर्त को तराशा और पॉलिश किया जाता था।"),
    ("निम्नलिखित में से कौन सा बहुमूल्य हरा पत्थर हड़प्पा वासियों द्वारा मध्य एशिया या पामीर क्षेत्र से आयात किया जाता था?", ["जेड (Jade)", "कार्सिलियन (Carnelian)", "लाजवर्त (Lapis Lazuli)", "फिरोजा (Turquoise)"], 0, "जेड का आयात मध्य एशिया और पामीर के पहाड़ों से किया जाता था, जो हड़प्पा के थल संपर्कों को दर्शाता है।"),
    ("हड़प्पा वासियों द्वारा आयातित फिरोजा (Turquoise) का मुख्य भौगोलिक स्रोत क्या था?", ["उत्तर-पूर्वी ईरान में खुरासान (निशापुर)", "कर्नाटक का कोलार क्षेत्र", "अफगानिस्तान में बदख्शां", "राजस्थान में खेत्री"], 0, "फिरोजा का आयात उत्तर-पूर्वी ईरान के खुरासान (निशापुर) और मध्य एशिया से थल मार्ग द्वारा किया जाता था।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following rare commodities were imported by the Harappans via overland trade routes from Iran and Central Asia? (Select all that apply)", ["Silver", "Turquoise", "Jade", "Carnelian"], [0, 1, 2], "Silver, turquoise, and jade were imported from Iran/Central Asia. Carnelian was a local Indian export from Gujarat."),
    ("Select the historical mountain passes used by Harappan pack-ox caravans to cross the northern ranges: (Select all that apply)", ["Bolan Pass", "Gomal Pass", "Khyber Pass", "Nathu La Pass"], [0, 1, 2], "Bolan, Gomal, and Khyber passes were critical western gateways. Nathu La is in the eastern Himalayas and was not used."),
    ("Which finished goods did the Harappans export overland to Central Asia and the West? (Select all that apply)", ["Cotton textiles", "Ivory carvings", "Etched carnelian beads", "Lapis lazuli blocks"], [0, 1, 2], "Textiles, ivory carvings, and beads were major exports. Lapis lazuli was an import from Badakhshan (though sometimes re-exported after processing)."),
    ("Which sites show strong evidence of interaction between the Harappans and the BMAC (Oxus) civilization? (Select all that apply)", ["Shortughai", "Altyn-Depe", "Mundigak", "Lothal"], [0, 1, 2], "Shortughai, Altyn-Depe, and Mundigak show Northern Oxus-Harappan interactions. Lothal is a southern maritime port."),
    ("Identify the overland transit stations or cities on the Iranian plateau and Afghanistan that linked the Indus plain to the West: (Select all that apply)", ["Shahr-i Sokhta", "Mundigak", "Tepe Yahya", "Ur"], [0, 1, 2], "Shahr-i Sokhta, Mundigak, and Tepe Yahya were overland hubs. Ur was a Mesopotamian port connected by sea.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन सी दुर्लभ वस्तुएं हड़प्पा वासियों द्वारा ईरान और मध्य एशिया से थल मार्गों द्वारा आयात की जाती थीं? (सभी लागू विकल्प चुनें)", ["चांदी", "फिरोजा", "जेड (Jade)", "कार्सिलियन"], [0, 1, 2], "चांदी, फिरोजा और जेड का आयात ईरान/मध्य एशिया से होता था। कार्सिलियन गुजरात से होने वाला निर्यात था।"),
    ("उत्तरी पर्वतों को पार करने के लिए हड़प्पा के कारवानों द्वारा उपयोग किए जाने वाले ऐतिहासिक दर्रों का चयन करें: (सभी लागू विकल्प चुनें)", ["बोलन दर्रा", "गोमल दर्रा", "खैबर दर्रा", "नाथू ला दर्रा"], [0, 1, 2], "बोलन, गोमल और खैबर दर्रे पश्चिमी पर्वत श्रृंखलाओं के मार्ग थे। नाथू ला पूर्वी हिमालय में स्थित है और इसका उपयोग नहीं होता था।"),
    ("हड़प्पा वासी मध्य एशिया और पश्चिम को थल मार्ग द्वारा किन निर्मित वस्तुओं का निर्यात करते थे? (सभी लागू विकल्प चुनें)", ["सूती वस्त्र", "हाथीदांत की नक्काशी", "नक्काशीदार कार्सिलियन मनके", "लाजवर्त के कच्चे ब्लॉक"], [0, 1, 2], "वस्त्र, हाथीदांत और मनके प्रमुख निर्यात थे। लाजवर्त तो बदख्शां से आयात किया जाता था।"),
    ("किन स्थलों से हड़प्पा और आक्सस (BMAC) सभ्यता के बीच संपर्क के मजबूत साक्ष्य मिले हैं? (सभी लागू विकल्प चुनें)", ["शोर्तुघई", "अल्टिन-देपे", "मुंडीगाक", "लोथल"], [0, 1, 2], "शोर्तुघई, अल्टिन-देपे और मुंडीगाक उत्तरी थल मार्ग पर थे। लोथल एक समुद्री बंदरगाह है।"),
    ("ईरानी पठार और अफगानिस्तान के उन पारगमन केंद्रों या शहरों की पहचान करें जो सिंधु मैदान को पश्चिम से जोड़ते थे: (सभी लागू विकल्प चुनें)", ["शहर-ए-सोख्ता", "मुंडीगाक", "तेपे याह्या", "उर"], [0, 1, 2], "शहर-ए-सोख्ता, मुंडीगाक और तेपे याह्या थल मार्ग के केंद्र थे। उर मेसोपोटामिया का बंदरगाह था जो समुद्र से जुड़ा था।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Khyber Pass was an active trade route linking the northern Indus plains with eastern Afghanistan.", True, "True. The Khyber Pass served as a key corridor connecting Punjab and Gandhara with Kabul and Central Asia."),
    ("Jade was imported overland from Karnataka in South India.", False, "False. Jade was imported overland from Central Asia and the Pamir Mountains."),
    ("The Iranian site of Shahr-i Sokhta yielded debitage proving it was a workshop for cutting lapis lazuli.", True, "True. Excavations revealed unworked blocks and waste flakes, showing it processed lapis from Afghanistan."),
    ("The Oxus (BMAC) civilization had absolutely no knowledge of Harappan weight systems or seals.", False, "False. Harappan-style cubical weights, ivory objects, and seals have been recovered from BMAC sites, showing contact."),
    ("Silver was mined directly in the alluvial plains of Sindh and Punjab.", False, "False. The alluvial plains do not have ore deposits; silver was imported from Afghanistan and Iran."),
    ("The Bolan Pass is a strategic gateway connecting Sindh with the Quetta valley in Baluchistan.", True, "True. It was the principal route connecting the southern Indus plains with highland Baluchistan."),
    ("Indus overland trade relied on wheeled horse chariots for fast delivery.", False, "False. There is no evidence of horses or chariots in Harappan trade; they used pack-oxen and slow carts."),
    ("Lapis lazuli beads were manufactured and exported from the northern outpost of Shortughai.", True, "True. Shortughai served as a production and export node for lapis lazuli ornaments.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("खैबर दर्रा उत्तरी सिंधु मैदानों को पूर्वी अफगानिस्तान से जोड़ने वाला एक सक्रिय व्यापारिक मार्ग था।", True, "सत्य। खैबर दर्रा पंजाब को काबुल और मध्य एशिया से जोड़ने वाला एक प्रमुख व्यापारिक मार्ग था।"),
    ("जेड (Jade) का आयात दक्षिण भारत के कर्नाटक से किया जाता था।", False, "असत्य। जेड का आयात मध्य एशिया और पामीर के पहाड़ों से किया जाता था।"),
    ("ईरान के शहर-ए-सोख्ता से कचरा (debitage) मिला है जो यह साबित करता है कि यह लाजवर्त काटने की कार्यशाला थी।", True, "सत्य। यहाँ बिना कटे लाजवर्त के टुकड़े और कचरा मिला है, जो इसके प्रसंस्करण को दर्शाता है।"),
    ("आक्सस (BMAC) सभ्यता को हड़प्पा की बाट प्रणाली या मुहरों का कोई ज्ञान नहीं था।", False, "असत्य। BMAC स्थलों से हड़प्पा शैली के घनाकार बाट, मुहरें और हाथीदांत की वस्तुएं मिली हैं।"),
    ("चांदी का खनन सीधे सिंधु और पंजाब के जलोढ़ मैदानों में किया जाता था।", False, "असत्य। जलोढ़ मैदानों में खनिज अयस्क नहीं हैं; चांदी का आयात ईरान और अफगानिस्तान से होता था।"),
    ("बोलन दर्रा सिंधु को बलूचिस्तान की क्वेटा घाटी से जोड़ने वाला एक रणनीतिक प्रवेश द्वार है।", True, "सत्य। यह मार्ग दक्षिणी सिंधु मैदानों को बलूचिस्तान के पठार से जोड़ता था।"),
    ("सिंधु थल व्यापार तेजी से माल भेजने के लिए घोड़ों वाले रथों पर निर्भर था।", False, "असत्य। हड़प्पा व्यापार में घोड़ों या रथों का कोई प्रमाण नहीं है; वे बैलों और बैलगाड़ियों का उपयोग करते थे।"),
    ("उत्तरी चौकी शोर्तुघई से लाजवर्त के मनकों का निर्माण और निर्यात किया जाता था।", True, "सत्य। शोर्तुघई लाजवर्त के गहनों के निर्माण और निर्यात का एक प्रमुख केंद्र था।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("The Bactria-Margiana Archaeological Complex is located in the basin of the ________ River.", "Oxus", "The BMAC/Oxus civilization is named after the Oxus River (Amu Darya)."),
    ("The principal mountain pass connecting the Indus plains with Baluchistan is the ________ Pass.", "Bolan", "The Bolan Pass was the main gateway to Baluchistan."),
    ("The Iranian plateau site of ________ was a key hub where lapis lazuli was cut and polished.", "Shahr-i Sokhta", "Shahr-i Sokhta processed Badakhshan lapis before western shipment."),
    ("Jade was imported overland by the Harappans from Central Asia or the ________ region.", "Pamir", "Jade was sourced from the Pamir mountains or East Turkestan."),
    ("Turquoise, a blue-green stone, was sourced from ________ in northeastern Iran.", "Khorasan", "Khorasan (Nishapur) was the main source of turquoise."),
    ("Inland plains lacked metal ores, requiring ________ to be imported from Afghanistan and Iran.", "silver", "Silver was brought from Afghanistan and Iran."),
    ("The ancient site of ________ in southern Afghanistan was an important transit hub before Shortughai.", "Mundigak", "Mundigak served as a caravan hub connecting the Indus with the Oxus region."),
    ("Overland trade caravans primarily utilized pack animals such as ________.", "oxen", "Oxen/bulls were the primary pack animals for mountainous trade caravans.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("बैक्टीरिया-मार्गियाना पुरातात्विक परिसर ________ नदी के बेसिन में स्थित है।", "आक्सस", "BMAC सभ्यता आक्सस (अमु दरिया) नदी के किनारे स्थित थी।"),
    ("सिंधु मैदानों को बलूचिस्तान से जोड़ने वाला मुख्य पर्वतीय दर्रा ________ दर्रा है।", "बोलन", "बोलन दर्रा बलूचिस्तान का मुख्य प्रवेश द्वार था।"),
    ("ईरानी पठार का ________ नामक स्थल लाजवर्त पत्थर को काटने और पॉलिश करने का मुख्य केंद्र था।", "शहर-ए-सोख्ता", "शहर-ए-सोख्ता में लाजवर्त का प्रसंस्करण किया जाता था।"),
    ("जेड (Jade) का आयात हड़प्पा वासियों द्वारा मध्य एशिया या ________ क्षेत्र से किया जाता था।", "पामीर", "जेड पामीर के पहाड़ों या मध्य एशिया से मँगाया जाता था।"),
    ("फिरोजा (एक नीला-हरा पत्थर) उत्तर-पूर्वी ईरान के ________ से मँगाया जाता था।", "खुरासान", "खुरासान (निशापुर) फिरोजा का मुख्य स्रोत था।"),
    ("मैदानी भागों में धातुओं की कमी के कारण ________ का आयात अफगानिस्तान और ईरान से किया जाता था।", "चांदी", "चांदी का आयात ईरान और अफगानिस्तान की खदानों से होता था।"),
    ("दक्षिणी अफगानिस्तान में स्थित ________ नामक प्राचीन स्थल शोर्तुघई से पहले एक प्रमुख पारगमन केंद्र था।", "मुंडीगाक", "मुंडीगाक सिंधु मैदान को आक्सस क्षेत्र से जोड़ने वाला कारवां हब था।"),
    ("थल मार्ग के व्यापारिक कारवां मुख्य रूप से ________ जैसे भारवाही पशुओं का उपयोग करते थे।", "बैलों", "बैलों का उपयोग पहाड़ी मार्गों पर कारवां के लिए किया जाता था।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the semi-precious stones with their primary overland sources:",
        "items": [{"left": "I. Jade", "key": "A"}, {"left": "II. Turquoise", "key": "B"}, {"left": "III. Lapis Lazuli", "key": "C"}],
        "options": [{"val": "A", "text": "A. Central Asia / Pamir"}, {"val": "B", "text": "B. Khorasan (Iran)"}, {"val": "C", "text": "C. Badakhshan (Afghanistan)"}],
        "sol": "Jade came from Central Asia/Pamir, turquoise from Khorasan, and lapis from Badakhshan."
    },
    {
        "type": "Match the Following",
        "q": "Match the regions/sites with their archaeological designations in overland networks:",
        "items": [{"left": "I. BMAC", "key": "A"}, {"left": "II. Shahr-i Sokhta", "key": "B"}, {"left": "III. Mundigak", "key": "C"}],
        "options": [{"val": "A", "text": "A. Oxus Civilisation (Central Asia)"}, {"val": "B", "text": "B. Lapis processing hub (Sistan)"}, {"val": "C", "text": "C. Transit hub (Southern Afghanistan)"}],
        "sol": "BMAC is the Oxus civilization, Shahr-i Sokhta is in Sistan, and Mundigak is in southern Afghanistan."
    },
    {
        "type": "Match the Following",
        "q": "Match the mountain passes with their geographic connections:",
        "items": [{"left": "I. Bolan Pass", "key": "A"}, {"left": "II. Khyber Pass", "key": "B"}, {"left": "III. Gomal Pass", "key": "C"}],
        "options": [{"val": "A", "text": "A. Links Sindh with Quetta Valley"}, {"val": "B", "text": "B. Links Punjab with Kabul Valley"}, {"val": "C", "text": "C. Links Indus Plain with Afghan Hills"}],
        "sol": "Bolan connects Sindh-Quetta, Khyber connects Punjab-Kabul, and Gomal connects Indus-Afghan hills."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "बहुमूल्य पत्थरों को उनके मुख्य थल मार्गों के स्रोतों से सुमेलित करें:",
        "items": [{"left": "I. जेड (Jade)", "key": "A"}, {"left": "II. फिरोजा", "key": "B"}, {"left": "III. लाजवर्त", "key": "C"}],
        "options": [{"val": "A", "text": "A. मध्य एशिया / पामीर"}, {"val": "B", "text": "B. खुरासान (ईरान)"}, {"val": "C", "text": "C. बदख्शां (अफगानिस्तान)"}],
        "sol": "जेड पामीर से, फिरोजा खुरासान से और लाजवर्त बदख्शां से आता था।"
    },
    {
        "type": "Match the Following",
        "q": "क्षेत्रों/स्थलों को उनके पुरातात्विक नामों से सुमेलित करें:",
        "items": [{"left": "I. BMAC", "key": "A"}, {"left": "II. शहर-ए-सोख्ता", "key": "B"}, {"left": "III. मुंडीगाक", "key": "C"}],
        "options": [{"val": "A", "text": "A. आक्सस सभ्यता (मध्य एशिया)"}, {"val": "B", "text": "B. लाजवर्त प्रसंस्करण हब (सीस्तान)"}, {"val": "C", "text": "C. पारगमन केंद्र (दक्षिणी अफगानिस्तान)"}],
        "sol": "BMAC आक्सस सभ्यता है, शहर-ए-सोख्ता सीस्तान में है और मुंडीगाक दक्षिणी अफगानिस्तान में है।"
    },
    {
        "type": "Match the Following",
        "q": "पर्वतीय दर्रों को उनके भौगोलिक संपर्कों से सुमेलित करें:",
        "items": [{"left": "I. बोलन दर्रा", "key": "A"}, {"left": "II. खैबर दर्रा", "key": "B"}, {"left": "III. गोमल दर्रा", "key": "C"}],
        "options": [{"val": "A", "text": "A. सिंध को क्वेटा घाटी से जोड़ता है"}, {"val": "B", "text": "B. पंजाब को काबुल घाटी से जोड़ता है"}, {"val": "C", "text": "C. सिंधु मैदान को अफगान पहाड़ियों से जोड़ता है"}],
        "sol": "बोलन सिंध-क्वेटा को, खैबर पंजाब-काबुल को और गोमल सिंधु-अफगान पहाड़ियों को जोड़ता है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the archaeological name for the Oxus Civilisation of Central Asia?", "Bactria-Margiana Archaeological Complex (BMAC)."),
    ("Which mountain pass connects the lower Indus plain with Quetta?", "Bolan Pass."),
    ("From which northeastern Iranian region was turquoise imported?", "Khorasan (Nishapur)."),
    ("Where was jade imported from in the north?", "Central Asia (Pamir Mountains)."),
    ("Which Sistan transit hub processed raw lapis lazuli?", "Shahr-i Sokhta."),
    ("Name a key metal imported by Harappans from Afghanistan.", "Silver."),
    ("Which river basin is BMAC located in?", "Oxus River basin."),
    ("Name the southern Afghan site that linked Indus caravans with Central Asia.", "Mundigak.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("मध्य एशिया की आक्सस सभ्यता का पुरातात्विक नाम क्या है?", "बैक्टीरिया-मार्गियाना पुरातात्विक परिसर (BMAC)।"),
    ("कौन सा दर्रा निचले सिंधु मैदान को क्वेटा से जोड़ता है?", "बोलन दर्रा।"),
    ("उत्तर-पूर्वी ईरान के किस क्षेत्र से फिरोजा का आयात किया जाता था?", "खुरासान (निशापुर)।"),
    ("उत्तर में जेड (Jade) का आयात कहाँ से किया जाता था?", "मध्य एशिया (पामीर पर्वत)।"),
    ("सीस्तान का कौन सा पारगमन केंद्र कच्चे लाजवर्त का प्रसंस्करण करता था?", "शहर-ए-सोख्ता।"),
    ("हड़प्पा वासियों द्वारा अफगानिस्तान से आयात की जाने वाली एक प्रमुख धातु का नाम बताएं।", "चांदी।"),
    ("BMAC किस नदी बेसिन में स्थित है?", "आक्सस (अमु दरिया) नदी बेसिन।"),
    ("दक्षिणी अफगानिस्तान के उस स्थल का नाम बताएं जो कारवां को मध्य एशिया से जोड़ता था।", "मुंडीगाक।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Harappans established a settlement at Shortughai on the Oxus River.\nReason (R): It allowed them to dominate the trade in lapis lazuli and copper from Badakhshan.", 0, "Both A and R are true and R explains why this remote outpost was set up in northern Afghanistan."),
    ("Assertion (A): Traveling overland via mountain passes was fast and comfortable for Harappan traders.\nReason (R): Caravans had to cross rugged mountains with pack animals, facing severe weather and difficult trails.", 3, "A is false because overland travel was slow and arduous; R is true."),
    ("Assertion (A): Turquoise was imported overland from South India.\nReason (R): It was imported from Khorasan in northeastern Iran.", 3, "A is false because turquoise came from Iran/Central Asia, and R is true."),
    ("Assertion (A): Shahr-i Sokhta was a key transit center for lapis lazuli trade.\nReason (R): Raw lapis mined in Badakhshan was transported to Shahr-i Sokhta for processing and value addition before being sent west.", 0, "Both A and R are true and processing raw materials at transit hubs added value before export."),
    ("Assertion (A): The Oxus (BMAC) civilization had no trade relations with the Indus Civilisation.\nReason (R): Harappan seals, weights, and ivory items have been excavated at BMAC sites like Altyn-Depe.", 3, "A is false because there was active trade, and R is true."),
    ("Assertion (A): The Gomal Pass was a vital trading corridor for Harappan caravans.\nReason (R): It connected the Indus Valley plains directly with the highlands of eastern Afghanistan.", 0, "Both A and R are true and the Gomal Pass was a key route for trading with Afghan tribes."),
    ("Assertion (A): The Harappans imported silver to make ornaments and vessels.\nReason (R): The alluvial plains of the Indus basin are completely devoid of silver ore deposits.", 0, "Both A and R are true and the geological absence of metals in the plains necessitated import."),
    ("Assertion (A): Ivory products were imported overland by the Harappans from Central Asia.\nReason (R): Ivory was an export product from the Indus Valley, where elephants were native.", 3, "A is false because ivory was exported, not imported; R is true.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा वासियों ने आक्सस नदी पर शोर्तुघई में एक बस्ती स्थापित की।\nकारण (R): इसने उन्हें बदख्शां से लाजवर्त और तांबे के व्यापार पर नियंत्रण करने की सुविधा दी।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): पर्वतीय दर्रों से थल मार्ग की यात्रा हड़प्पा व्यापारियों के लिए बहुत तेज़ और आरामदायक थी।\nकारण (R): कारवां को पहाड़ी रास्तों पर भारवाही पशुओं के साथ जाना पड़ता था, जहाँ खराब मौसम और कठिन रास्ते थे।", 3, "A गलत है क्योंकि थल मार्ग कठिन और धीमा था; R सही है।"),
    ("कथन (A): फिरोजा का आयात थल मार्ग से दक्षिण भारत से किया जाता था।\nकारण (R): इसका आयात उत्तर-पूर्वी ईरान के खुरासान क्षेत्र से किया जाता था।", 3, "A गलत है क्योंकि फिरोजा ईरान से आता था, और R सही है।"),
    ("कथन (A): शहर-ए-सोख्ता लाजवर्त व्यापार का एक प्रमुख पारगमन केंद्र था।\nकारण (R): बदख्शां से मँगाए गए लाजवर्त को पश्चिम भेजने से पहले यहाँ तराशा और सुधारा जाता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): आक्सस (BMAC) सभ्यता का सिंधु सभ्यता के साथ कोई व्यापारिक संबंध नहीं था।\nकारण (R): अल्टिन-देपे जैसे BMAC स्थलों से हड़प्पा की मुहरें, बाट और हाथीदांत की वस्तुएं मिली हैं।", 3, "A गलत है क्योंकि व्यापारिक संबंध मौजूद थे; R सही है।"),
    ("कथन (A): गोमल दर्रा हड़प्पा कारवां के लिए एक महत्वपूर्ण व्यापारिक गलियारा था।\nकारण (R): यह सिंधु घाटी के मैदानों को सीधे पूर्वी अफगानिस्तान के पर्वतीय क्षेत्रों से जोड़ता था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): हड़प्पा वासी बर्तन और आभूषण बनाने के लिए चांदी का आयात करते थे।\nकारण (R): सिंधु बेसिन के जलोढ़ मैदानों में चांदी के अयस्क का कोई भंडार नहीं था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि अयस्क की कमी से आयात आवश्यक था।"),
    ("कथन (A): हड़प्पा वासियों द्वारा मध्य एशिया से हाथीदांत की वस्तुओं का आयात किया जाता था।\nकारण (R): हाथीदांत सिंधु घाटी से होने वाला एक निर्यात था, जहाँ हाथी बहुतायत में पाए जाते थे।", 3, "A गलत है क्योंकि हाथीदांत निर्यात किया जाता था, और R सही है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: The Bolan Pass connects the Indus plain with the Quetta valley in Baluchistan.\nStatement 2: The Khyber Pass connects Punjab with the Kabul valley.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, representing two major caravan corridors of the Harappans."),
    ("Consider the following statements:\nStatement 1: Silver and turquoise were imported overland from Afghanistan and Iran.\nStatement 2: Tin was imported from Karnataka in South India.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: tin came from Khorasan/Central Asia or Afghanistan, not Karnataka (South India was for gold)."),
    ("Consider the following statements:\nStatement 1: Shahr-i Sokhta is located in eastern Iran near the border of Sistan.\nStatement 2: It served as a vital transit hub for processing Harappan lapis lazuli.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct."),
    ("Consider the following statements:\nStatement 1: The BMAC represents the ancient Baltic-Mediterranean Archaeological Complex.\nStatement 2: It shared cultural and trade exchanges with the Indus Valley Civilisation.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: BMAC stands for Bactria-Margiana Archaeological Complex. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Jade was sourced from the delta of the Indus river.\nStatement 2: Lapis lazuli was sourced from Rajasthan.\nWhich of the statements given above is/are correct?", 3, "Both statements are incorrect. Jade came from Central Asia/Pamir and lapis from Afghanistan.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: बोलन दर्रा सिंधु मैदान को बलूचिस्तान की क्वेटा घाटी से जोड़ता है।\nकथन 2: खैबर दर्रा पंजाब को काबुल घाटी से जोड़ता है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो हड़प्पा काल के दो प्रमुख थल मार्गों को दर्शाते हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: चांदी और फिरोजा का आयात थल मार्ग द्वारा अफगानिस्तान और ईरान से किया जाता था।\nकथन 2: टीन का आयात दक्षिण भारत के कर्नाटक से किया जाता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि टीन मध्य एशिया/अफगानिस्तान से आता था, कर्नाटक से केवल सोना आता था।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: शहर-ए-सोख्ता पूर्वी ईरान में सीस्तान सीमा के पास स्थित है।\nकथन 2: यह हड़प्पा के लाजवर्त पत्थर के प्रसंस्करण के लिए एक प्रमुख पारगमन केंद्र था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: BMAC प्राचीन बाल्टिक-भूमध्यसागरीय पुरातात्विक परिसर को दर्शाता है।\nकथन 2: इसके सिंधु घाटी सभ्यता के साथ सांस्कृतिक और व्यापारिक संबंध थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि BMAC का अर्थ बैक्टीरिया-मार्गियाना पुरातात्विक परिसर है। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: जेड (Jade) का स्रोत सिंधु नदी का डेल्टा क्षेत्र था।\nकथन 2: लाजवर्त का स्रोत राजस्थान का रेगिस्तानी क्षेत्र था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। जेड मध्य एशिया से और लाजवर्त अफगानिस्तान से आता था।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why was silver an important overland import commodity for the Harappans?", "The alluvial plains of Punjab and Sindh lacked any silver deposits. However, silver was highly valued by the Harappan elite for manufacturing luxury vessels and jewelry, requiring regular caravan imports from Afghanistan and Iran."),
    ("Why did Shahr-i Sokhta become a major lapis lazuli processing center?", "It was located at a geographical junction between the lapis mines of Badakhshan and the consumer markets of Mesopotamia and Elam. It was cheaper to transport raw lapis to Shahr-i Sokhta, cut it, and export finished beads than to transport heavy raw stone all the way."),
    ("Why was overland caravan trade slower and more limited compared to riverine and maritime trade?", "Overland trade relied on pack animals (oxen, donkeys) crossing steep mountain passes. This limited the volume of cargo that could be carried, made transport slow, and increased vulnerability to weather and rugged terrain.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("चांदी हड़प्पा वासियों के लिए थल मार्ग से आयात की जाने वाली एक महत्वपूर्ण वस्तु क्यों थी?", "पंजाब और सिंध के जलोढ़ मैदानों में चांदी का कोई भंडार नहीं था। इसके बावजूद, हड़प्पा के अभिजात वर्ग द्वारा बर्तन और गहने बनाने के लिए चांदी को अत्यधिक पसंद किया जाता था, जिसके कारण अफगानिस्तान और ईरान से नियमित कारवां आयात की आवश्यकता होती थी।"),
    ("शहर-ए-सोख्ता लाजवर्त (Lapis) के प्रसंस्करण का एक बड़ा केंद्र क्यों बन गया?", "यह बदख्शां की लाजवर्त खदानों और मेसोपोटामिया/एलाम के उपभोक्ता बाजारों के बीच एक भौगोलिक चौराहे पर स्थित था। भारी कच्चे पत्थर को पूरी दूरी तक ले जाने के बजाय शहर-ए-सोख्ता में लाकर काटना और बेचना अधिक किफायती था।"),
    ("नदी और समुद्री व्यापार की तुलना में थल मार्ग का कारवां व्यापार धीमा और सीमित क्यों था?", "थल मार्ग का व्यापार पहाड़ी दर्रों को पार करने वाले भारवाही पशुओं (बैलों, गधों) पर निर्भर था। इसने माल की मात्रा को सीमित कर दिया, परिवहन को धीमा बना दिया और मौसम व कठिन रास्तों के कारण जोखिम बढ़ा दिया।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How do archaeologists prove the trade links between the Indus Valley and the BMAC (Oxus) civilization?", "Through excavations showing Harappan objects (like etched carnelian beads, ivory rods, and square steatite seals) at BMAC sites like Altyn-Depe and Gonur-Tepe, alongside Oxus-style metal pins found in Harappan layers."),
    ("How did Harappan caravans cross the difficult northern and western mountain ranges?", "They utilized historic natural gaps in the mountains, such as the Bolan, Gomal, and Khyber passes, planning their journeys seasonally to avoid winter snows and taking advantage of caravan stations along the route."),
    ("How was the distribution of lapis lazuli managed overland from the mines to the Mediterranean?", "Lapis was mined in Badakhshan, brought to the outpost of Shortughai, transported via Mundigak in Afghanistan to Shahr-i Sokhta in Iran for cutting, and then traded overland to Susa and Mesopotamian cities.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("पुरातत्वविद सिंधु घाटी और BMAC (आक्सस) सभ्यता के बीच व्यापारिक संबंधों को कैसे सिद्ध करते हैं?", "अल्टिन-देपे और गोनुर-तेपे जैसे BMAC स्थलों पर हड़प्पा की वस्तुओं (जैसे कार्सिलियन के मनके, हाथीदांत की छड़ें और वर्गाकार मुहरें) की खोज से, और हड़प्पा स्तरों में आक्सस शैली के धातु के पिनों की प्राप्ति से।"),
    ("हड़प्पा के कारवां कठिन उत्तरी और पश्चिमी पर्वत श्रृंखलाओं को कैसे पार करते थे?", "वे पहाड़ों के बीच बने प्राकृतिक दर्रों (जैसे बोलन, गोमल और खैबर) का उपयोग करते थे, सर्दियों की बर्फबारी से बचने के लिए मौसम के अनुकूल यात्रा करते थे और रास्ते में बनी चौकियों का सहारा लेते थे।"),
    ("खदानों से लेकर भूमध्य सागर तक लाजवर्त का वितरण थल मार्ग से कैसे प्रबंधित किया जाता था?", "लाजवर्त को बदख्शां में खोदकर निकाला जाता था, शोर्तुघई लाया जाता था, फिर अफगानिस्तान के मुंडीगाक के रास्ते ईरान के शहर-ए-सोख्ता भेजकर काटा जाता था और वहाँ से थल मार्ग द्वारा सुसा और मेसोपोटामिया के शहरों को भेजा जाता था।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Shahr-i Sokhta. Analyze its role in lapis lazuli processing.", "Situated in eastern Iran, Shahr-i Sokhta has yielded over 90% of its lapis lazuli remains in the form of waste flakes and unworked blocks. This indicates that it was a processing colony. Rather than consuming lapis locally, its artisans shaped beads for export to Mesopotamia and Egypt, showing early division of labor."),
    ("Case Study: The Bactria-Margiana Archaeological Complex (BMAC). Analyze the trade footprints.", "BMAC sites in Central Asia show clear evidence of Indus contacts. At Gonur-Tepe, a classic Harappan square seal with a unicorn and script was discovered. In return, Harappan sites yielded BMAC bronze pins and mirrors, illustrating a complex bronze-age exchange network."),
    ("Case Study: Mundigak as an Overland Caravan Station. Discuss its location.", "Located in Kandahar province, Afghanistan, Mundigak was a pre-Harappan site that developed into a crucial transit hub during the Mature Harappan phase. It connected Indus trade routes with Central Asian highlands, providing shelter and water for pack animal caravans.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: शहर-ए-सोख्ता। लाजवर्त (Lapis) के प्रसंस्करण में इसकी भूमिका का विश्लेषण करें।", "पूर्वी ईरान में स्थित शहर-ए-सोख्ता से मिलने वाले लाजवर्त के 90% अवशेष कचरे (waste flakes) के रूप में हैं। यह दर्शाता है कि यह एक प्रसंस्करण केंद्र था। यहाँ के कारीगर स्थानीय उपयोग के बजाय पश्चिमी मेसोपोटामिया और मिस्र के लिए मनके तैयार करते थे।"),
    ("केस स्टडी: बैक्टीरिया-मार्गियाना पुरातात्विक परिसर (BMAC)। इसके व्यापारिक संबंधों का विश्लेषण करें।", "मध्य एशिया के BMAC स्थलों से सिंधु सभ्यता के स्पष्ट संपर्क मिलते हैं। गोनुर-तेपे में एक हड़प्पा कालीन वर्गाकार मुहर मिली है जिस पर एक सींग वाला पशु और लिपि अंकित है। बदले में हड़प्पा में BMAC की धातु की दर्पणें और पिनें मिली हैं।"),
    ("केस स्टडी: मुंडीगाक एक थल कारवां स्टेशन के रूप में। इसकी स्थिति पर चर्चा करें।", "अफगानिस्तान के कंधार प्रांत में स्थित मुंडीगाक एक पूर्व-हड़प्पा स्थल था जो परिपक्व हड़प्पा काल में एक मुख्य पारगमन केंद्र बन गया। यह सिंधु मार्गों को मध्य एशिया के पठारों से जोड़ता था और कारवां के लिए पानी और आश्रय प्रदान करता था।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: The Role of a Transit Processing Hub in Ancient Commerce.", "Explain to students that transit hubs like Shahr-i Sokhta were not just rest stops, but added value. By refining raw lapis into finished beads, they reduced the weight of cargo for long-distance transport and increased the profitability of trade before re-exporting to the west."),
    ("Teach the Concept: Mountain Pass Corridor Geopolitics.", "Explain how narrow mountain passes like Bolan and Gomal controlled all land movement. By maintaining alliances with local hill cultures, the Harappan state secured these gateways to keep caravan routes open for metal and stone imports."),
    ("Teach the Concept: Overland Caravan versus Maritime trade.", "Teach the comparison between land caravan trade (using pack animals, high unit cost, carrying low-weight luxury stones/metals) and maritime trade (using ships, lower cost per ton, capable of carrying heavy timbers, copper, and bulk cotton).")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: प्राचीन वाणिज्य में पारगमन प्रसंस्करण केंद्र (Transit Processing Hub) की भूमिका।", "छात्रों को समझाएं कि शहर-ए-सोख्ता जैसे पारगमन केंद्र केवल विश्राम गृह नहीं थे बल्कि मूल्यवर्धन (value addition) करते थे। कच्चे लाजवर्त को मनकों में बदलकर, उन्होंने परिवहन के लिए वजन कम किया और पश्चिम में निर्यात से पहले लाभ बढ़ाया।"),
    ("अवधारणा सिखाएं: पर्वतीय दर्रों के गलियारों की भू-राजनीति (Geopolitics)।", "समझाएं कि कैसे बोलन और गोमल जैसे संकीर्ण दर्रे थल मार्ग के सभी आंदोलनों को नियंत्रित करते थे। पहाड़ी संस्कृतियों के साथ गठजोड़ बनाए रखकर, हड़प्पा राज्य ने धातु और पत्थर के आयात के लिए कारवां मार्गों को सुरक्षित रखा।"),
    ("अवधारणा सिखाएं: थल कारवां बनाम समुद्री व्यापार।", "थल कारवां व्यापार (भारवाही पशुओं का उपयोग, उच्च इकाई लागत, कम वजन के महंगे पत्थरों/धातुओं का परिवहन) और समुद्री व्यापार (जहाजों का उपयोग, कम लागत, भारी लकड़ी, तांबा और कपास ले जाने में सक्षम) के बीच तुलना सिखाएं।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: MARITIME TRADE & MESOPOTAMIAN CONNECTIONS
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Cuneiform inscriptions of which Mesopotamian king boast that ships of Meluhha, Makan, and Dilmun docked at his capital city?", ["Sargon of Akkad", "Hammurabi", "Naram-Sin", "Gudea of Lagash"], 0, "King Sargon of Akkad (c. 2350 BCE) recorded this boast, verifying direct maritime shipping lines with Meluhha (the Indus valley)."),
    ("In Mesopotamian trade tablets, the land of 'Dilmun', known as a pure transit island, corresponds to which modern region?", ["Bahrain Island", "Oman Peninsula", "Makran Coast", "Yemen"], 0, "Dilmun is identified with the island of Bahrain in the Persian Gulf, serving as a vital intermediate transit port."),
    ("The brick dockyard basin of Lothal was directly connected via a channel to which river estuary?", ["Sabarmati / Bhogavo River estuary", "Indus River estuary", "Narmada River estuary", "Tapti River estuary"], 0, "The Lothal dockyard was connected via an inlet channel to a tidal estuary of the Sabarmati (Bhogavo tributary) River in Gujarat."),
    ("Which fortified coastal station on the Makran coast near the modern Iran-Pakistan border was the westernmost outpost of the Indus Civilisation?", ["Sutkagendor", "Sotka Koh", "Balakot", "Lothal"], 0, "Sutkagendor was the westernmost fortified Harappan outpost, strategically monitoring maritime traffic entering the Persian Gulf."),
    ("What distinct design feature of the circular button seals found at Lothal links them directly to the Persian Gulf trade network?", ["A double-boss backing with circle carvings", "Mesopotamian cuneiform characters", "An image of a humpless bull with wings", "A depiction of a horse-drawn chariot"], 0, "The circular button seals found at Lothal feature a double-boss backing with circle patterns, typical of Gulf seals from Bahrain (Dilmun).")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("किस मेसोपोटामियाई राजा के कीलाक्षर लेखों में गर्व से कहा गया है कि मेलुहा, माकन और दिलमुन के जहाज उसकी राजधानी के बंदरगाह पर आते थे?", ["अक्कड़ के सम्राट सारगोन", "हम्मूराबी", "नराम-सिन", "लागाश के गुडेआ"], 0, "अक्कड़ के राजा सारगोन (लगभग 2350 ईसा पूर्व) ने यह दावा किया था, जो मेलुहा (सिंधु घाटी) के साथ समुद्री संबंधों की पुष्टि करता है।"),
    ("मेसोपोटामिया की पट्टिकाओं में 'दिलमुन' (जिसे एक पवित्र पारगमन बंदरगाह कहा गया) किस आधुनिक क्षेत्र से संबंधित है?", ["बहरीन द्वीप", "ओमान प्रायद्वीप", "मकरान तट", "यमन"], 0, "दिलमुन की पहचान फारस की खाड़ी के बहरीन द्वीप से की जाती है, जो समुद्री व्यापार में मध्यस्थ का काम करता था।"),
    ("लोथल के पकी ईंटों से बने गोदीवाड़ा (dockyard) को एक नहर के माध्यम से किस नदी के मुहाने से जोड़ा गया था?", ["साबरमती / भोगावो नदी मुहाना", "सिंधु नदी मुहाना", "नर्मदा नदी मुहाना", "ताप्ती नदी मुहाना"], 0, "लोथल गोदीवाड़ा गुजरात में साबरमती की सहायक भोगावो नदी के ज्वारीय मुहाने से जुड़ा था।"),
    ("आधुनिक ईरान-पाकिस्तान सीमा के पास मकरान तट पर स्थित कौन सी सुदृढ़ तटीय चौकी सिंधु सभ्यता की सबसे पश्चिमी सीमा थी?", ["सुत्कागेंदोर", "सोत्का कोह", "बालाकोट", "लोथल"], 0, "सुत्कागेंदोर सबसे पश्चिमी हड़प्पा चौकी थी, जिसका निर्माण खाड़ी में जाने वाले समुद्री जहाजों की निगरानी के लिए किया गया था।"),
    ("लोथल से मिली गोल बटन मुहरों की कौन सी डिजाइन उन्हें फारस की खाड़ी के व्यापारिक नेटवर्क से सीधे जोड़ती है?", ["पीछे दोहरे कूबड़ (double-boss) के साथ वृत्ताकार पैटर्न", "मेसोपोटामिया की कीलाक्षर लिपि", "बिना कूबड़ वाले पंखदार बैल का चित्र", "घोड़े से खींचे जाने वाले रथ का अंकन"], 0, "लोथल से मिली खाड़ी की मुहरों के पीछे एक डबल-बॉस (कूबड़) बना है जिस पर वृत्ताकार छेद हैं, जो बहरीन की मुहरों के समान हैं।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multiple Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following geographical names are recorded in Akkadian cuneiform inscriptions representing Persian Gulf trade entities? (Select all that apply)", ["Meluhha (Indus Valley)", "Makan (Oman)", "Dilmun (Bahrain)", "Kemet (Egypt)"], [0, 1, 2], "Meluhha, Makan, and Dilmun are frequently listed. Kemet is the ancient name for Egypt and is not linked to Gulf trade in these tablets."),
    ("Select the primary commodities exported by Meluhha to Mesopotamian cities as recorded in tablets: (Select all that apply)", ["Exotic timbers (teak/ebony)", "Ivory objects", "Carnelian beads", "Bitumen sealant"], [0, 1, 2], "Timbers, ivory, and carnelian beads were major Meluhhan exports. Bitumen was imported by the Harappans from Mesopotamia."),
    ("Identify the coastal ports and maritime stations established by the Harappans to secure the Gulf trade route: (Select all that apply)", ["Lothal", "Sutkagendor", "Sotka Koh", "Kalibangan"], [0, 1, 2], "Lothal, Sutkagendor, and Sotka Koh were coastal ports/stations. Kalibangan is an inland dry-river site in Rajasthan."),
    ("Which items did the Harappans import from Mesopotamian cities in return for their goods? (Select all that apply)", ["Silver", "Bitumen", "Woolen textiles", "Lapis Lazuli"], [0, 1, 2], "Silver, bitumen, and textiles were major Mesopotamian exports. Lapis lazuli was sourced by Harappans from Afghanistan, not Mesopotamia."),
    ("What engineering features characterized the dockyard basin discovered at Lothal? (Select all that apply)", ["Walls built of high-quality fired bricks", "A sluice/lock-gate system at the southern spillway", "An inlet channel to allow tidal water entry", "A roof supported by stone pillars"], [0, 1, 2], "The dockyard featured burnt brick walls, a lock-gate system, and an inlet channel. It was an open basin, not roofed with stone pillars.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("अक्कड़ के कीलाक्षर अभिलेखों में दर्ज फारस की खाड़ी के व्यापारिक भागीदारों में कौन से नाम शामिल हैं? (सभी लागू विकल्प चुनें)", ["मेलुहा (सिंधु घाटी)", "माकन (ओमान)", "दिलमुन (बहरीन)", "केमेट (मिस्र)"], [0, 1, 2], "मेलुहा, माकन और दिलमुन इन अभिलेखों में आते हैं। केमेट मिस्र का प्राचीन नाम है जो इन खाड़ी व्यापार पट्टिकाओं में शामिल नहीं है।"),
    ("मेसोपोटामिया की पट्टिकाओं के अनुसार मेलुहा से निर्यात की जाने वाली मुख्य वस्तुओं का चयन करें: (सभी लागू विकल्प चुनें)", ["दुर्लभ लकड़ियाँ (सागौन/आबनूस)", "हाथीदांत की वस्तुएं", "कार्सिलियन के मनके", "कोलतार (Bitumen)"], [0, 1, 2], "लकड़ी, हाथीदांत और कार्सिलियन मनके मेलुहा के निर्यात थे। कोलतार मेसोपोटामिया से भारत आयात किया जाता था।"),
    ("खाड़ी व्यापार मार्ग को सुरक्षित करने के लिए हड़प्पा वासियों द्वारा स्थापित तटीय बंदरगाहों और केंद्रों की पहचान करें: (सभी लागू विकल्प चुनें)", ["लोथल", "सुत्कागेंदोर", "सोत्का कोह", "कालीबंगन"], [0, 1, 2], "लोथल, सुत्कागेंदोर और सोत्का कोह तटीय बंदरगाह/चौकियाँ थीं। कालीबंगन राजस्थान का अंतर्देशीय स्थल है।"),
    ("हड़प्पा वासी अपने माल के बदले मेसोपोटामिया के शहरों से किन वस्तुओं का आयात करते थे? (सभी लागू विकल्प चुनें)", ["चांदी", "कोलतार (Bitumen)", "ऊनी वस्त्र", "लाजवर्त"], [0, 1, 2], "चांदी, कोलतार और ऊन मेसोपोटामिया से आते थे। लाजवर्त तो अफगानिस्तान से मँगाया जाता था।"),
    ("लोथल में खोजे गए गोदीवाड़ा (dockyard) की क्या विशेषताएं थीं? (सभी लागू विकल्प चुनें)", ["दीवारें उच्च गुणवत्ता वाली पकी ईंटों से बनी थीं", "निकास द्वार पर एक लकड़ी का लॉक-गेट सिस्टम था", "ज्वारीय पानी को अंदर आने देने के लिए एक नहर थी", "पत्थर के खंभों पर टिकी एक छत थी"], [0, 1, 2], "लोथल गोदीवाड़ा में पकी ईंटें, लॉक-गेट और प्रवेश नहर थी। यह एक खुला तालाब था, छत नहीं थी।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Meluhha is the ancient Mesopotamian geographical term used to refer to Egypt.", False, "False. Meluhha is identified with the Indus Valley Civilisation."),
    ("Dilmun (Bahrain) was celebrated in Mesopotamian myths as a pure land with fresh water springs.", True, "True. Cuneiform texts describe Dilmun as a clean, blessed island serving as a peaceful trade port."),
    ("King Sargon of Akkad claimed in his tablets that he invaded and destroyed the cities of Mohenjo-daro and Harappa.", False, "False. Sargon only boasted that ships of Meluhha docked at his capital city, indicating trade, not invasion."),
    ("The walls of the Lothal dockyard basin were built of sun-dried mud-bricks.", False, "False. Burnt bricks were used to resist water pressure and erosion."),
    ("Circular 'Persian Gulf' button seals have been excavated at the port site of Lothal.", True, "True. These seals verify that Lothal hosted Gulf merchants acting as middlemen."),
    ("In cuneiform records, Makan referred to the island of Bahrain.", False, "False. Makan referred to Oman, while Dilmun referred to Bahrain."),
    ("Sutkagendor is situated on the Makran coast near the border of modern Iran.", True, "True. It was the westernmost frontier outpost of the Harappan maritime trade route."),
    ("The clay sealings placed on cargo packages served as security tags to prove the cargo arrived untampered.", True, "True. If the clay sealing remained unbroken, it verified that the package had not been tampered with during shipping.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मेसोपोटामिया के अभिलेखों में प्रयुक्त 'मेलुहा' शब्द प्राचीन मिस्र को दर्शाता है।", False, "असत्य। मेलुहा की पहचान सिंधु घाटी सभ्यता से की जाती है।"),
    ("दिलमुन (बहरीन) को मेसोपोटामिया के मिथकों में ताजे पानी के झरनों वाली एक पवित्र भूमि कहा गया है।", True, "सत्य। कीलाक्षर अभिलेखों में दिलमुन को एक स्वच्छ, समृद्ध द्वीप और शांत व्यापारिक बंदरगाह बताया गया है।"),
    ("अक्कड़ के राजा सारगोन ने अपनी पट्टिकाओं में दावा किया कि उसने सिंधु घाटी पर हमला किया और मोहनजोदड़ो को नष्ट कर दिया।", False, "असत्य। सारगोन ने केवल यह लिखा था कि मेलुहा के जहाजों ने अक्कड़ में लंगर डाला, जो व्यापारिक संबंध दर्शाता है, विजय नहीं।"),
    ("लोथल गोदीवाड़ा बेसिन की दीवारें धूप में सुखाए गए कच्चे ईंटों से बनाई गई थीं।", False, "असत्य। पानी के दबाव और कटाव को रोकने के लिए पकी ईंटों (baked bricks) का उपयोग किया गया था।"),
    ("लोथल के बंदरगाह स्थल से फारस की खाड़ी की गोल बटन मुहरें मिली हैं।", True, "सत्य। ये मुहरें साबित करती हैं कि लोथल में खाड़ी के व्यापारियों का आना-जाना था।"),
    ("कीलाक्षर अभिलेखों में 'माकन' का संबंध बहरीन द्वीप से था।", False, "असत्य। माकन ओमान को दर्शाता था, जबकि दिलमुन बहरीन को दर्शाता था।"),
    ("सुत्कागेंदोर आधुनिक ईरान की सीमा के पास मकरान तट पर स्थित है।", True, "सत्य। यह हड़प्पा समुद्री व्यापार मार्ग की सबसे पश्चिमी सीमा पर स्थित चौकी थी।"),
    ("सामान के बंडलों पर लगाई गई गीली मिट्टी की छापें (sealings) सुरक्षा टैग थीं जो यह साबित करती थीं कि माल सुरक्षित पहुँचा है।", True, "सत्य। यदि मिट्टी की छाप साबुत रहती थी, तो यह साबित होता था कि रास्ते में माल के साथ कोई छेड़छाड़ नहीं की गई है।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blanks (8)
for q, ans, sol in [
    ("In cuneiform inscriptions, the geographical designation ________ refers to the Indus Valley region.", "Meluhha", "Meluhha is the Mesopotamian term for the Indus valley."),
    ("The transit island of Dilmun corresponds to modern ________ in the Persian Gulf.", "Bahrain", "Dilmun is identified with Bahrain."),
    ("Sargon of Akkad boasted that ships from Meluhha docked at the quays of his capital city ________.", "Akkad", "The Akkadian Empire capital city was Akkad."),
    ("The westernmost fortified port outpost of the Harappans on the Makran coast was ________.", "Sutkagendor", "Sutkagendor served as a western coastal fort."),
    ("The Lothal dockyard was connected via an inlet channel to a tributary of the ________ River.", "Sabarmati", "It was built in the delta of the Sabarmati River system."),
    ("Mesopotamian records source nickel-bearing copper from the land of ________, modern Oman.", "Makan", "Makan (or Magan) was the Oman region."),
    ("To secure packages during maritime shipping, Harappans applied clay ________ over knots.", "sealings", "Clay sealings secured package knots and verified identity."),
    ("The coastal monitoring station of ________ Koh is located on the Makran coast near Pasni.", "Sotka", "Sotka Koh monitored maritime trade traffic along the coast.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कीलाक्षर अभिलेखों में प्रयुक्त भौगोलिक नाम ________ सिंधु घाटी क्षेत्र को दर्शाता है।", "मेलुहा", "मेलुहा मेसोपोटामिया में सिंधु घाटी का नाम था।"),
    ("पारगमन द्वीप दिलमुन फारस की खाड़ी के आधुनिक ________ से संबंधित है।", "बहरीन", "दिलमुन की पहचान बहरीन से की जाती है।"),
    ("अक्कड़ के सम्राट सारगोन ने गर्व से लिखा था कि मेलुहा के जहाजों ने उसकी राजधानी ________ के बंदरगाह पर लंगर डाला।", "अक्कड़", "सारगोन की राजधानी अक्कड़ थी।"),
    ("मकरान तट पर स्थित हड़प्पा वासियों का सबसे पश्चिमी तटीय दुर्ग ________ था।", "सुत्कागेंदोर", "सुत्कागेंदोर सबसे पश्चिमी तटीय चौकी थी।"),
    ("लोथल गोदीवाड़ा एक नहर के माध्यम से ________ नदी की एक सहायक धारा से जुड़ा था।", "साबरमती", "यह साबरमती नदी प्रणाली के मुहाने पर स्थित था।"),
    ("मेसोपोटामिया के अभिलेख निकल युक्त तांबे का स्रोत ________ को बताते हैं, जो आधुनिक ओमान है।", "माकन", "माकन ओमान को दर्शाता था जहाँ से तांबा आता था।"),
    ("समुद्री परिवहन के समय बंडलों को सुरक्षित करने के लिए हड़प्पा वासी गांठों पर गीली मिट्टी की ________ लगाते थे।", "छाप", "गीली मिट्टी की छाप (sealings) बंडलों की सुरक्षा के लिए लगाई जाती थी।"),
    ("मकरान तट पर पसनी के पास स्थित तटीय निगरानी चौकी का नाम ________ कोह है।", "सोत्का", "सोत्का कोह मकरान तट पर जहाजों की निगरानी का केंद्र था।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Matchings (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the Mesopotamian cuneiform names with their modern geographical identifications:",
        "items": [{"left": "I. Meluhha", "key": "A"}, {"left": "II. Makan", "key": "B"}, {"left": "III. Dilmun", "key": "C"}],
        "options": [{"val": "A", "text": "A. Indus Valley Civilisation"}, {"val": "B", "text": "B. Oman Peninsula"}, {"val": "C", "text": "C. Bahrain Island"}],
        "sol": "Meluhha is Indus valley, Makan is Oman, and Dilmun is Bahrain."
    },
    {
        "type": "Match the Following",
        "q": "Match the coastal sites with their specific geographical or commercial characteristics:",
        "items": [{"left": "I. Lothal", "key": "A"}, {"left": "II. Sutkagendor", "key": "B"}, {"left": "III. Sotka Koh", "key": "C"}],
        "options": [{"val": "A", "text": "A. Kiln-burnt brick tidal dockyard basin"}, {"val": "B", "text": "B. Western frontier fort on the Iran border"}, {"val": "C", "text": "C. Coastal station on the Makran coast"}],
        "sol": "Lothal has the brick dockyard, Sutkagendor is the western fort, and Sotka Koh is a coastal station."
    },
    {
        "type": "Match the Following",
        "q": "Match the commodities with their commercial direction in Meluhha-Mesopotamia trade:",
        "items": [{"left": "I. Hardwoods and Ivory", "key": "A"}, {"left": "II. Bitumen and Wool", "key": "B"}, {"left": "III. Lapis Lazuli", "key": "C"}],
        "options": [{"val": "A", "text": "A. Export cargo sent to Akkad"}, {"val": "B", "text": "B. Import cargo received from Akkad"}, {"val": "C", "text": "C. Transit item procured from Afghan mines"}],
        "sol": "Meluhha exported hardwoods and ivory, imported bitumen and wool from Akkad, and procured lapis from Badakhshan as a transit item."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "मेसोपोटामिया के कीलाक्षर अभिलेखों में प्रयुक्त नामों को उनके आधुनिक भौगोलिक स्थलों से सुमेलित करें:",
        "items": [{"left": "I. मेलुहा", "key": "A"}, {"left": "II. माकन", "key": "B"}, {"left": "III. दिलमुन", "key": "C"}],
        "options": [{"val": "A", "text": "A. सिंधु घाटी सभ्यता"}, {"val": "B", "text": "B. ओमान प्रायद्वीप"}, {"val": "C", "text": "C. बहरीन द्वीप"}],
        "sol": "मेलुहा सिंधु घाटी है, माकन ओमान है और दिलमुन बहरीन है।"
    },
    {
        "type": "Match the Following",
        "q": "तटीय स्थलों को उनकी विशिष्ट भौगोलिक या व्यावसायिक विशेषताओं से सुमेलित करें:",
        "items": [{"left": "I. लोथल", "key": "A"}, {"left": "II. सुत्कागेंदोर", "key": "B"}, {"left": "III. सोत्का कोह", "key": "C"}],
        "options": [{"val": "A", "text": "A. पकी ईंटों से बना ज्वारीय गोदीवाड़ा"}, {"val": "B", "text": "B. ईरान सीमा के निकट पश्चिमी सीमांत दुर्ग"}, {"val": "C", "text": "C. मकरान तट पर स्थित तटीय निगरानी चौकी"}],
        "sol": "लोथल में ईंटों की गोदी है, सुत्कागेंदोर पश्चिमी दुर्ग है और सोत्का कोह मकरान तट का स्टेशन है।"
    },
    {
        "type": "Match the Following",
        "q": "वस्तुओं को मेलुहा-मेसोपोटामिया व्यापार में उनके आयात-निर्यात की दिशा से सुमेलित करें:",
        "items": [{"left": "I. कीमती लकड़ी और हाथीदांत", "key": "A"}, {"left": "II. कोलतार (Bitumen) और ऊन", "key": "B"}, {"left": "III. लाजवर्त", "key": "C"}],
        "options": [{"val": "A", "text": "A. अक्कड़ भेजा जाने वाला निर्यात माल"}, {"val": "B", "text": "B. अक्कड़ से मिलने वाला आयात माल"}, {"val": "C", "text": "C. अफगान खदानों से प्राप्त पारगमन सामग्री"}],
        "sol": "मेलुहा कीमती लकड़ी और हाथीदांत का निर्यात करता था, अक्कड़ से ऊन और कोलतार का आयात करता था, और लाजवर्त को पारगमन वस्तु के रूप में भेजता था।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What was the cuneiform designation used by Mesopotamians for the Indus Valley Civilisation?", "Meluhha."),
    ("Which Persian Gulf island was referred to as Dilmun in ancient texts?", "Bahrain Island."),
    ("Name the Mesopotamian emperor who boasted of Meluhhan ships docking at Akkad.", "Sargon of Akkad."),
    ("Where in Gujarat is the baked-brick Harappan dockyard basin located?", "Lothal."),
    ("Name the westernmost coastal outpost of the Harappans on the Makran coast.", "Sutkagendor."),
    ("What was the Mesopotamian name for Oman, the source of nickel-bearing copper?", "Makan."),
    ("Which coastal monitoring outpost is located near Sutkagendor?", "Sotka Koh."),
    ("What organic sealant did the Harappans import from Mesopotamia?", "Bitumen.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया वासियों द्वारा सिंधु घाटी सभ्यता के लिए किस कीलाक्षर नाम का प्रयोग किया जाता था?", "मेलुहा।"),
    ("फारस की खाड़ी के किस द्वीप को प्राचीन ग्रंथों में 'दिलमुन' कहा गया था?", "बहरीन द्वीप।"),
    ("उस मेसोपोटामियाई सम्राट का नाम बताएं जिसने मेलुहा के जहाजों के अक्कड़ में लंगर डालने का दावा किया था?", "अक्कड़ के सम्राट सारगोन।"),
    ("गुजरात में पकी ईंटों से बना हड़प्पा का गोदीवाड़ा (dockyard) कहाँ स्थित है?", "लोथल।"),
    ("मकरान तट पर स्थित हड़प्पा वासियों की सबसे पश्चिमी तटीय चौकी कौन सी थी?", "सुत्कागेंदोर।"),
    ("निकल युक्त तांबे के स्रोत ओमान के लिए मेसोपोटामिया का क्या नाम था?", "माकन।"),
    ("सुत्कागेंदोर के निकट मकरान तट पर कौन सी अन्य तटीय निगरानी चौकी स्थित है?", "सोत्का कोह।"),
    ("हड़प्पा वासियों द्वारा मेसोपोटामिया से किस जैविक सीलेंट (sealant) का आयात किया जाता था?", "कोलतार (Bitumen)।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Lothal was a highly advanced maritime port of the Harappan civilization.\nReason (R): It featured a massive brick basin connected to a tidal estuary, complete with a lock-gate sluice to manage shipping tides.", 0, "Both A and R are true and R explains the maritime engine of Lothal dockyard."),
    ("Assertion (A): Mesopotamian records describe Meluhha as a land of uncivilized nomadic tribes.\nReason (R): Inscriptions show that Meluhha exported highly prized luxury goods like gold, carnelian beads, and ivory to Mesopotamia.", 3, "A is false because Meluhha was recognized as a wealthy civilization; R is true."),
    ("Assertion (A): Dilmun served as a critical transit port in the Persian Gulf maritime trade network.\nReason (R): It was geographically situated midway along the shipping lanes connecting the Indus valley with the Tigris-Euphrates basin.", 0, "Both A and R are true and its midway location made Dilmun a natural stopover and trade transit market."),
    ("Assertion (A): Sargon of Akkad successfully invaded and conquered the cities of the Indus Valley.\nReason (R): His cuneiform tablets boast that ships from Meluhha, Makan, and Dilmun docked at the quays of his capital city Akkad.", 3, "A is false because there is no evidence of invasion; the cuneiform tablets only show trade relations; R is true."),
    ("Assertion (A): Clay sealings were vital security measures for long-distance maritime shipping.\nReason (R): If the clay sealing on a cargo package remained unbroken, it proved the goods had not been opened or stolen during transit.", 0, "Both A and R are true and the integrity of sealings was the primary proof of cargo security."),
    ("Assertion (A): Sutkagendor was located in the deep interior of the Punjab plains to control wheat trade.\nReason (R): It was a fortified coastal outpost on the Makran coast near modern Iran, guarding maritime routes.", 3, "A is false since Sutkagendor was a coastal border outpost, and R is true."),
    ("Assertion (A): Makan (Oman) copper was imported by both Mesopotamians and Harappans.\nReason (R): Scientific analysis shows that copper artifacts from both civilizations contain trace levels of nickel matching Omani ores.", 0, "Both A and R are true and nickel trace analysis confirms Oman as the common source of copper in the Gulf."),
    ("Assertion (A): The Harappans traded directly with the kingdom of Egypt via sea routes.\nReason (R): There is no direct textual or archaeological evidence of Harappan merchant ships visiting Egyptian Nile ports.", 3, "A is false because direct trade is unproven; contact was indirect through Mesopotamia/Gulf; R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): लोथल हड़प्पा सभ्यता का एक अत्यधिक विकसित समुद्री बंदरगाह था।\nकारण (R): इसमें एक विशाल ज्वारीय मुहाने से जुड़ा ईंटों का तालाब था, जिसमें जहाजों को तैरता रखने के लिए लॉक-गेट लगा था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): मेसोपोटामिया के ग्रंथों में मेलुहा को असभ्य खानाबदोश जनजातियों का देश कहा गया है।\nकारण (R): कीलाक्षर पट्टिकाओं से पता चलता है कि मेलुहा मेसोपोटामिया को कीमती लकड़ी, लाल अकीक और हाथीदांत जैसी लक्जरी वस्तुएं भेजता था।", 3, "A गलत है क्योंकि मेलुहा को एक समृद्ध व्यापारिक भागीदार माना जाता था, R सही है।"),
    ("कथन (A): फारस की खाड़ी के व्यापार में दिलमुन (बहरीन) एक महत्वपूर्ण पारगमन (transit) बंदरगाह था।\nकारण (R): यह सिंधु मुहाने और मेसोपोटामिया को जोड़ने वाले समुद्री मार्ग के बीच में स्थित था।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या है।"),
    ("कथन (A): अक्कड़ के राजा सारगोन ने सिंधु घाटी पर हमला किया और उस पर विजय प्राप्त की।\nकारण (R): उसके अभिलेखों में लिखा है कि मेलुहा, माकन और दिलमुन के जहाजों ने उसकी राजधानी अक्कड़ में लंगर डाला।", 3, "A गलत है क्योंकि आक्रमण का कोई साक्ष्य नहीं है; केवल व्यापार का उल्लेख है; R सही है।"),
    ("कथन (A): लंबी दूरी के समुद्री परिवहन में बंडलों पर लगी मिट्टी की छापें (sealings) अत्यंत महत्वपूर्ण थीं।\nकारण (R): यदि छाप टूटी नहीं होती थी, तो यह साबित होता था कि यात्रा के दौरान माल के साथ कोई छेड़छाड़ नहीं की गई है।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है।"),
    ("कथन (A): सुत्कागेंदोर गेहूं व्यापार को नियंत्रित करने के लिए पंजाब के भीतरी मैदानी इलाकों में स्थित था।\nकारण (R): यह मकरान तट पर ईरान सीमा के पास स्थित एक सुदृढ़ तटीय चौकी थी जो समुद्री मार्गों की रक्षा करती थी।", 3, "A गलत है क्योंकि यह मकरान तट पर सीमांत दुर्ग था, R सही है।"),
    ("कथन (A): मेसोपोटामिया और हड़प्पा दोनों सभ्यताओं द्वारा माकन (ओमान) के तांबे का आयात किया जाता था।\nकारण (R): वैज्ञानिक विश्लेषण से पता चलता है कि दोनों सभ्यताओं के तांबे के उपकरणों में निकल की अशुद्धियाँ ओमान के अयस्क से मेल खाती हैं।", 0, "A और R दोनों सही हैं और R, कथन A की सही व्याख्या करता है क्योंकि निकल विश्लेषण ने स्रोत सिद्ध किया।"),
    ("कथन (A): हड़प्पा वासी समुद्री मार्ग से सीधे मिस्र के साम्राज्य के साथ व्यापार करते थे।\nकारण (R): हड़प्पा के जहाजों के मिस्र के नील बंदरगाहों पर जाने का कोई सीधा लिखित या पुरातात्विक साक्ष्य नहीं मिला है।", 3, "A गलत है क्योंकि सीधा व्यापार सिद्ध नहीं है; वे खाड़ी/मेसोपोटामिया के माध्यम से जुड़े थे; R सही है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements:\nStatement 1: Sargon of Akkad lived during the late Harappan phase around 1500 BCE.\nStatement 2: Akkadian inscriptions provide direct references to Meluhha, Makan, and Dilmun.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: Sargon reigned around 2350 BCE during the Mature Harappan apex. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: The Lothal dockyard basin was connected via an inlet channel to the Sabarmati river basin.\nStatement 2: The walls of the dockyard basin were built of mud-brick and faced with cut stone columns.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the walls were made of high-quality fired clay bricks, not mud-bricks or stone columns."),
    ("Consider the following statements:\nStatement 1: Meluhha was the cuneiform designation for ancient Egypt.\nStatement 2: Makan represented the copper-rich peninsula of Oman.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: Meluhha is the Indus Valley. Statement 2 is correct."),
    ("Consider the following statements:\nStatement 1: Sutkagendor is located on the Makran coast near the modern Iran-Pakistan border.\nStatement 2: Sotka Koh is another Harappan coastal station also located on the Makran coast.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Both served to secure and monitor Gulf shipping lines."),
    ("Consider the following statements:\nStatement 1: Harappan seals were used as monetary coins with fixed face values.\nStatement 2: Clay sealings were applied to package knots to detect theft and prove origin.\nWhich of the statements given above is/are correct?", 1, "Statement 1 is incorrect: seals were administrative and security tokens, not currency. Statement 2 is correct.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: अक्कड़ का राजा सारगोन लगभग 1500 ईसा पूर्व उत्तर-हड़प्पा काल में रहता था।\nकथन 2: अक्कड़ के अभिलेखों में मेलुहा, माकन और दिलमुन के सीधे संदर्भ मिलते हैं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि सारगोन लगभग 2350 ईसा पूर्व (परिपक्व हड़प्पा काल) में था। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: लोथल गोदीवाड़ा बेसिन साबरमती नदी प्रणाली के मुहाने से एक प्रवेश नहर द्वारा जुड़ा था।\nकथन 2: गोदीवाड़ा की दीवारें कच्ची ईंटों से बनी थीं और उनके सामने पत्थर के बड़े खंभे लगे थे।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि दीवारें पकी ईंटों से बनी थीं, कच्ची ईंटों या पत्थर के खंभों से नहीं।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: मेलुहा प्राचीन मिस्र का कीलाक्षर नाम था।\nकथन 2: माकन ओमान के तांबा समृद्ध प्रायद्वीप का प्रतिनिधित्व करता था।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि मेलुहा सिंधु घाटी को दर्शाता है। कथन 2 सही है।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: सुत्कागेंदोर मकरान तट पर आधुनिक ईरान-पाकिस्तान सीमा के पास स्थित है।\nकथन 2: सोत्का कोह भी मकरान तट पर स्थित एक अन्य हड़प्पा तटीय स्टेशन है।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। दोनों मकरान तट पर तटीय जहाजों की सुरक्षा के लिए बनाए गए थे।"),
    ("निम्नलिखित कथनों पर विचार कीजिए:\nकथन 1: हड़प्पा की मुहरों का उपयोग निश्चित मूल्य वाले मौद्रिक सिक्कों के रूप में किया जाता था।\nकथन 2: पैकेज की गांठों पर मिट्टी की छापें (sealings) चोरी का पता लगाने और स्रोत साबित करने के लिए लगाई जाती थीं।\nउपर्युक्त कथनों में से कौन-सा/से सही है/हैं?", 1, "कथन 1 गलत है क्योंकि मुहरें मुद्रा नहीं थीं; वे सुरक्षा सील थीं। कथन 2 सही है।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Mesopotamian myths and records refer to Dilmun (Bahrain) as a blessed and pure land?", "Dilmun was a peaceful merchant transit port with natural freshwater springs in the middle of the salty Gulf. It lacked monumental military fortifications, serving as a neutral zone where traders from different empires could meet safely."),
    ("Why did the engineers of the Lothal dockyard construct a lock-gate sluice system?", "The dockyard was built in a tidal estuary where water levels varied by several meters between high and low tide. The wooden lock-gate spillway allowed water to be trapped inside the basin during low tide, keeping the docked ships floating and stable for loading."),
    ("Why did the Harappan state fortify remote outposts like Sutkagendor and Sotka Koh along the Makran coast?", "These stations guarded the maritime trade routes entering the Persian Gulf. They provided shelter and freshwater for merchant ships against monsoon storms, monitored sea traffic, and protected valuable cargo from coastal pirates.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("मेसोपोटामिया के ग्रंथों में दिलमुन (बहरीन) को एक धन्य और पवित्र भूमि क्यों कहा गया है?", "दिलमुन फारस की खाड़ी के बीच ताजे पानी के झरनों वाला एक शांत व्यापारिक बंदरगाह था। यहाँ सैन्य दुर्गों के अवशेष नहीं मिले हैं, जिससे यह एक तटस्थ क्षेत्र था जहाँ विभिन्न सभ्यताओं के व्यापारी सुरक्षित मिल सकते थे।"),
    ("लोथल गोदीवाड़ा के इंजीनियरों ने एक लॉक-गेट (sluice-gate) प्रणाली का निर्माण क्यों किया?", "गोदीवाड़ा एक ज्वारीय मुहाने पर बना था जहाँ ज्वार-भाटे के कारण पानी का स्तर काफी बदलता था। लकड़ी के लॉक-गेट ने भाटे (low tide) के समय पानी को बेसिन में रोक कर रखा ताकि जहाजों को तल से टकराने से बचाया जा सके और वे हमेशा तैरते रहें।"),
    ("हड़प्पा राज्य ने मकरान तट पर सुत्कागेंदोर और सोत्का कोह जैसी चौकियों की किलेबंदी क्यों की थी?", "ये चौकियाँ फारस की खाड़ी में प्रवेश करने वाले समुद्री व्यापारिक मार्गों की रक्षा करती थीं। वे जहाजों को मानसूनी तूफानों से बचाती थीं, मीठा पानी उपलब्ध कराती थीं और माल को समुद्री डाकुओं से सुरक्षित रखती थीं।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How does scientific chemical analysis of trace elements prove that Oman supplied copper to both Mesopotamia and the Indus Valley?", "Omani copper ores naturally contain trace levels of nickel. Chemical analysis of copper tools excavated from both Mesopotamia and the Indus Valley reveals similar nickel impurities, proving that Oman (Makan) was their common copper source."),
    ("How did Mesopotamian cuneiform tablets record and verify the import of Harappan goods?", "Mesopotamian scribes kept detailed administrative tablets. They listed imported cargo from Meluhha, including ivory objects, carnelian beads, and valuable woods, specifying the quantities and the merchants involved in the transactions."),
    ("How did Harappan mariners navigate their ships from the Indus delta to the Euphrates-Tigris delta?", "They used coast-hugging navigation, sailing close to the shoreline along the Makran coast, using landmarks, stopping at coastal shelters like Sutkagendor and intermediate transit ports like Bahrain (Dilmun) before entering the Gulf.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("तांबे के उपकरणों के रासायनिक विश्लेषण ने यह कैसे सिद्ध किया कि ओमान ने मेसोपोटामिया और सिंधु घाटी दोनों को तांबे की आपूर्ति की थी?", "ओमान के तांबा अयस्क में प्राकृतिक रूप से निकल की अशुद्धि होती है। मेसोपोटामिया और सिंधु घाटी दोनों से मिले तांबे के औजारों के रासायनिक परीक्षण में भी निकल की समान अशुद्धि पाई गई, जिससे यह सिद्ध हुआ कि ओमान (माकन) दोनों का साझा तांबा स्रोत था।"),
    ("मेसोपोटामिया के कीलाक्षर अभिलेखों में हड़प्पा से आयातित वस्तुओं का विवरण कैसे दर्ज किया जाता था?", "मेसोपोटामिया के मुंशी प्रशासनिक पट्टिकाओं पर विस्तृत ब्योरा रखते थे। वे मेलुहा से आने वाली वस्तुओं (हाथीदांत, कार्सिलियन मनके और कीमती लकड़ियों) की सूची, उनकी मात्रा और सौदे में शामिल व्यापारियों के नाम दर्ज करते थे।"),
    ("हड़प्पा के नाविक अपने जहाजों को सिंधु डेल्टा से दजला-फरात (मेसोपोटामिया) के मुहाने तक कैसे ले जाते थे?", "वे मकरान तट के किनारे-किनारे चलते थे (coast-hugging navigation)। वे जमीन के निशानों का उपयोग करते थे और मकरान तट पर सुत्कागेंदोर व खाड़ी में बहरीन (दिलमुन) जैसे सुरक्षित स्टेशनों पर रुकते हुए यात्रा पूरी करते थे।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Lothal Dockyard Tidal Engineering. Analyze the layout and construction.", "Lothal's dockyard basin (214 x 36 m) was constructed of high-quality kiln-burnt bricks. The basin was connected to the tidal Sabarmati river. During high tide, ships entered through an inlet channel. A wooden gate at the southern spillway was then closed to retain water during low tide, keeping ships afloat, illustrating advanced hydraulic understanding."),
    ("Case Study: Akkadian Trade Tablets. Discuss the textual references to Meluhha.", "Mesopotamian tablets from the reign of Sargon of Akkad list trading commodities. Sargon boasts that ships of Meluhha, Makan, and Dilmun docked at his capital Akkad. The tablets record imports of ivory, gold, lapis lazuli, and carnelian from Meluhha, confirming the scale and direct nature of Indus-Mesopotamian maritime shipping."),
    ("Case Study: Sutkagendor as a Coastal Frontier Fort. Analyze its layout.", "Located on the Dasht River, Sutkagendor consists of a fortified citadel with massive stone-rubble walls and an outer town. It was situated near the sea coast in antiquity. Its heavy defenses suggest it functioned as a border fortress to secure maritime trade lanes, control entry into the Persian Gulf, and store cargo.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: लोथल गोदीवाड़ा की हाइड्रोलिक इंजीनियरिंग। इसके डिजाइन और संचालन का विश्लेषण करें।", "लोथल का गोदीवाड़ा (214 x 36 मीटर) पकी ईंटों से बनाया गया था, जो भोगावो-साबरमती के मुहाने से जुड़ा था। उच्च ज्वार के समय जहाज प्रवेश करते थे। भाटे के समय पानी को रोकने के लिए दक्षिण में लकड़ी का फाटक बंद कर दिया जाता था, जिससे जहाज स्थिर रहते थे, जो हड़प्पा वासियों के ज्वार-भाटे के ज्ञान को दर्शाता है।"),
    ("केस स्टडी: अक्कड़ काल की व्यापारिक पट्टिकाएँ। मेलुहा के लिखित साक्ष्यों का विश्लेषण करें।", "अक्कड़ के सम्राट सारगोन के काल की पट्टिकाएँ व्यापारिक सामानों की सूची देती हैं। सारगोन गर्व से लिखता है कि मेलुहा, माकन और दिलमुन के जहाजों ने उसकी राजधानी अक्कड़ में लंगर डाला। पट्टिकाएँ मेलुहा से प्राप्त लकड़ी, सोने, हाथीदांत और कार्सिलियन मनकों का विवरण देती हैं, जो प्रत्यक्ष समुद्री व्यापार सिद्ध करती हैं।"),
    ("केस स्टडी: सुत्कागेंदोर तटीय सीमा दुर्ग। इसके सुरक्षा लेआउट का विश्लेषण करें।", "दश्त नदी के पास स्थित सुत्कागेंदोर में पत्थरों की विशाल दीवारों से घिरा एक दुर्ग और निचला नगर है। प्राचीन काल में यह समुद्र तट के निकट था। इसकी भारी किलेबंदी यह दर्शाती है कि यह समुद्री मार्गों की सुरक्षा करने, खाड़ी में जाने वाले जहाजों पर नजर रखने और माल भंडारण के लिए एक मजबूत प्रहरी दुर्ग था।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach the Concept: Cuneiform Decipherment and the Meluhha Question.", "Explain to students how historians matched cuneiform records with geography. The items imported from Meluhha (hardwoods, ivory, carnelian) match native products of the Indus Valley. This, combined with the presence of Indus seals in Mesopotamia, confirms that 'Meluhha' refers to the Harappan civilization."),
    ("Teach the Concept: Sluice-Gate Hydrology in Ancient Dockyards.", "Teach how Harappan engineers used the gravity of water and a simple wooden lock-gate to manage tide changes. By trapping high-tide water inside a brick-lined basin, they solved the problem of tidal mud flats, allowing ships to load and unload throughout the year without grounding."),
    ("Teach the Concept: Tamper-Evident Clay Sealings as Commercial Security.", "Explain the process: a merchant packed goods in a bag, tied it with rope, applied wet clay over the knot, and stamped it with a unique seal. If the clay sealing arrived intact, it proved that the goods had not been opened or altered, acting as a security tag without locks.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा सिखाएं: कीलाक्षर लिपि का अर्थ और 'मेलुहा' की पहचान।", "छात्रों को समझाएं कि इतिहासकारों ने कीलाक्षर अभिलेखों को भूगोल से कैसे मिलाया। मेलुहा से आयात की जाने वाली वस्तुएं (कीमती लकड़ी, हाथीदांत, अकीक) सिंधु घाटी के उत्पाद हैं। मेसोपोटामिया में सिंधु की मुहरों के मिलने के साथ यह साबित होता है कि 'मेलुहा' ही सिंधु सभ्यता है।"),
    ("अवधारणा सिखाएं: प्राचीन गोदीवाड़ा में लॉक-गेट (Sluice-gate) हाइड्रोलॉजी।", "समझाएं कि कैसे हड़प्पा वासियों ने ज्वार-भाटे को नियंत्रित करने के लिए पानी के दबाव और लकड़ी के फाटक का उपयोग किया। पकी ईंटों के बेसिन में ज्वार के पानी को रोककर, उन्होंने जहाजों के कीचड़ में फंसने की समस्या को हल किया, जिससे साल भर जहाज बिना किसी बाधा के लोड हो सकते थे।"),
    ("अवधारणा सिखाएं: बंडलों पर मिट्टी की सुरक्षा छाप (sealings)।", "प्रक्रिया को समझाएं: व्यापारी माल को एक बोरी में बांधता था, गांठ पर गीली मिट्टी लगाता था और अपनी मुहर दबाता था। यदि मिट्टी की छाप टूटी नहीं मिलती थी, तो यह साबित होता था कि सामान सुरक्षित पहुँचा है और रास्ते में चोरी या छेड़छाड़ नहीं हुई है।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Write outputs
def inject_mastery(filepath, s1, s2, s3, name):
    if not os.path.exists(filepath):
        print(f"Error: {name} file not found at {filepath}")
        return False
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Verify we are writing to the correct places
    data["deepDive"]["sections"][0]["masteryZone"] = s1
    data["deepDive"]["sections"][1]["masteryZone"] = s2
    data["deepDive"]["sections"][2]["masteryZone"] = s3
    
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"{name} mastery injected successfully!")
    return True

v_eng = inject_mastery(ENG_PATH, s1_mastery_eng, s2_mastery_eng, s3_mastery_eng, "English")
v_hin = inject_mastery(HIN_PATH, s1_mastery_hin, s2_mastery_hin, s3_mastery_hin, "Hindi")

if v_eng and v_hin:
    print("Mastery questions injection complete for both languages!")
else:
    print("Injection failed. Check paths or errors above.")
