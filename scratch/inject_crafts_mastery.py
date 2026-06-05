import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Crafts\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Crafts\hi\content.json"

mcq_opts = ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"]
ar_opts = [
    "Both A and R are true and R is the correct explanation of A",
    "Both A and R are true but R is not the correct explanation of A",
    "A is true but R is false",
    "A is false but R is true"
]

hin_mcq_opts = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"]
hin_ar_opts = [
    "A और R दोनों सत्य हैं और R, A की सही व्याख्या है",
    "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है",
    "A सत्य है लेकिन R असत्य है",
    "A असत्य है लेकिन R सत्य है"
]

# =========================================================================
# SECTION 1: BEAD-MAKING, SHELL-WORKING & GEMSTONE PROCESSING
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following Harappan sites yielded specialized bead-making workshops with furnaces and drills?", ["Chanhudaro and Lothal", "Nageshwar and Balakot", "Kalibangan and Ropar", "Sutkagendor and Kot Diji"], 0, "Bead factories, including raw materials, working benches, kilns, and micro-drills, were discovered at Chanhudaro and Lothal."),
    ("The vibrant red color of Harappan carnelian beads was obtained by:", ["Firing the raw yellow-brown pebbles in specialized kilns", "Dipping the beads in copper oxide solutions", "Painting the finished stones with red manganese ink", "Importing naturally red stones from Mesopotamia"], 0, "The deep red of carnelian was achieved by heat-treating/firing the raw yellow-brown chalcedony stone in ovens."),
    ("Which coastal Harappan sites functioned as dedicated shell-working centers?", ["Nageshwar and Balakot", "Chanhudaro and Amri", "Harappa and Kalibangan", "Dholavira and Banawali"], 0, "Located on the coast, Nageshwar (Gujarat) and Balakot (Balochistan) were dedicated shell-working factories."),
    ("Lapis Lazuli, highly prized in the Indus Valley, was imported from:", ["Badakhshan (via Shortughai in Afghanistan)", "Khetri mines in Rajasthan", "The Deccan plateau in Central India", "The Persian Gulf ports of Dilmun"], 0, "Lapis Lazuli was sourced from Badakhshan in Afghanistan, where the Harappans established a colony at Shortughai."),
    ("Specialized Harappan micro-drills used for boring holes in hard carnelian beads were made of:", ["Ernestite (a very hard chert)", "Polished bronze alloy", "Tempered iron rods", "Carved ivory tips"], 0, "Ernestite chert drills were extremely hard and used to drill through hard gemstone beads.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किस हड़प्पा स्थल से भट्टियों और ड्रिलों से युक्त विशिष्ट मनका-निर्माण कार्यशालाएं मिली हैं?", ["चन्हुदड़ो और लोथल", "नागेश्वर और बालाकोट", "कालीबंगन और रोपड़", "सुतकागेंडोर और कोट दीजी"], 0, "मनका बनाने के कारखाने, जिनमें कच्चा माल, काम करने के चबूतरे, भट्टियां और सूक्ष्म-ड्रिल शामिल हैं, चन्हुदड़ो और लोथल से मिले हैं।"),
    ("हड़प्पा के अकीक (carnelian) के मनकों का गहरा लाल रंग कैसे प्राप्त किया जाता था?", ["कच्चे पीले-भूरे पत्थरों को विशिष्ट भट्टियों में पकाकर", "मनकों को कॉपर ऑक्साइड के घोल में डुबोकर", "तैयार पत्थरों को लाल मैंगनीज स्याही से रंगकर", "मेसोपोटामिया से प्राकृतिक लाल पत्थर आयात करके"], 0, "अकीक का गहरा लाल रंग कच्चे पीले-भूरे पत्थरों को भट्टी में पकाकर (उष्मा उपचार द्वारा) प्राप्त किया जाता था।"),
    ("कौन से तटीय हड़प्पा स्थल शंख शिल्प (shell-working) के प्रमुख केंद्र थे?", ["नागेश्वर और बालाकोट", "चन्हुदड़ो और आमरी", "हड़प्पा और कालीबंगन", "धोलावीरा और बनावली"], 0, "नागेश्वर (गुजरात) और बालाकोट (बलूचिस्तान) समुद्र तट पर स्थित होने के कारण शंख उद्योग के प्रमुख कारखाने थे।"),
    ("सिंधु घाटी में अत्यधिक मूल्यवान माना जाने वाला लाजवर्द (Lapis Lazuli) कहाँ से आयात किया जाता था?", ["बदख्शां (अफगानिस्तान में शोरतूघई के माध्यम से)", "राजस्थान में खेतड़ी खदानों से", "मध्य भारत में दक्कन के पठार से", "दिलमुन के फारस की खाड़ी के बंदरगाहों से"], 0, "लाजवर्द का आयात अफगानिस्तान के बदख्शां क्षेत्र से होता था, जहाँ हड़प्पा वासियों ने शोरतूघई नामक व्यापारिक चौकी स्थापित की थी।"),
    ("कठोर अकीक के मनकों में छेद करने के लिए प्रयुक्त सूक्ष्म-ड्रिल (micro-drills) किस पत्थर से बने होते थे?", ["अर्नेस्टाइट (अत्यंत कठोर चर्ट)", "पॉलिश किए गए कांसे से", "कठोर लोहे की छड़ों से", "नक्काशीदार हाथीदांत की युक्तियों से"], 0, "अर्नेस्टाइट (Ernestite) चर्ट से बने ड्रिल अत्यंत कठोर थे और इनका उपयोग पत्थरों में छेद करने के लिए किया जाता था।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following gemstones were processed by Harappan lapidaries? (Select all that apply)", ["Carnelian", "Lapis Lazuli", "Steatite", "Turquoise"], [0, 1, 2, 3], "Carnelian, lapis, steatite, and turquoise were all processed in Harappan lapidary shops."),
    ("Select the objects manufactured from marine shells in coastal workshops: (Select all that apply)", ["Bangles", "Ladles", "Furniture inlays", "Heavy anchors"], [0, 1, 2], "Artisans made bangles, ladles, and furniture inlays from shell; heavy anchors were rough limestone blocks."),
    ("Identify the sites containing excavated bead-making workshops: (Select all that apply)", ["Chanhudaro", "Lothal", "Harappa", "Shortughai"], [0, 1, 2], "Bead factories were found at Chanhudaro and Lothal, with evidence of bead craft also at Harappa. Shortughai was a raw trading post."),
    ("Which regions supplied raw craft materials to the Harappan cities? (Select all that apply)", ["Badakhshan for Lapis Lazuli", "Gujarat for Carnelian", "Rajasthan for Steatite", "Central India for Iron"], [0, 1, 2], "Lapis came from Badakhshan, carnelian from Gujarat, and steatite from Rajasthan. Iron was unknown in the Bronze Age."),
    ("Select the characteristic features of the Nageshwar shell craft industry: (Select all that apply)", ["Direct proximity to coastal shell resources", "Heaps of discarded shell waste showing workshop sites", "Specialized shell-sawing bronze tools", "Mass production of gold-plated mirrors"], [0, 1, 2], "Nageshwar had marine shell access, waste heaps, and bronze saws. Gold-plated glass mirrors did not exist.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन रत्नों का प्रसंस्करण हड़प्पा के शिल्पकारों द्वारा किया जाता था? (सभी लागू विकल्प चुनें)", ["अकीक (Carnelian)", "लाजवर्द (Lapis)", "सेलखड़ी (Steatite)", "फ़िरोज़ा (Turquoise)"], [0, 1, 2, 3], "अकीक, लाजवर्द, सेलखड़ी और फ़िरोज़ा का प्रसंस्करण मनका उद्योगों में किया जाता था।"),
    ("तटीय कार्यशालाओं में समुद्री शंखों से निर्मित वस्तुओं का चयन करें: (सभी लागू विकल्प चुनें)", ["चूड़ियाँ", "कड़छी (Ladles)", "फर्नीचर पच्चीकारी", "भारी लंगर"], [0, 1, 2], "शंख से चूड़ियाँ, कड़छी और पच्चीकारी के टुकड़े बनाए जाते थे; लंगर चूना पत्थर के खंड होते थे।"),
    ("उन स्थलों की पहचान करें जहाँ से मनका बनाने की कार्यशालाएं मिली हैं: (सभी लागू विकल्प चुनें)", ["चन्हुदड़ो", "लोथल", "हड़प्पा", "शोरतूघई"], [0, 1, 2], "चन्हुदड़ो और लोथल मनका उद्योग के मुख्य केंद्र थे, और हड़प्पा में भी इसके साक्ष्य मिले हैं। शोरतूघई केवल रत्नों की व्यापार चौकी थी।"),
    ("कौन से क्षेत्र हड़प्पा शहरों को शिल्प के लिए कच्चा माल आपूर्ति करते थे? (सभी लागू विकल्प चुनें)", ["लाजवर्द के लिए बदख्शां", "अकीक के लिए गुजरात", "सेलखड़ी के लिए राजस्थान", "लोहे के लिए मध्य भारत"], [0, 1, 2], "लाजवर्द बदख्शां से, अकीक गुजरात से, और सेलखड़ी राजस्थान से आती थी। लोहा कांस्य युग में अज्ञात था।"),
    ("नागेश्वर शंख शिल्प उद्योग की विशिष्ट विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["तटीय शंख संसाधनों के समीप स्थित होना", "कार्यशाला स्थलों को दर्शाते कचरे के ढेर मिलना", "शंख काटने के लिए कांसे की विशिष्ट आरी", "सोने के पानी चढ़े दर्पणों का भारी निर्माण"], [0, 1, 2], "नागेश्वर तटीय नागेश्वर में शंखों के कचरे के ढेर और काटने के औजार मिले हैं। दर्पण कांच के नहीं होते थे।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Lapis Lazuli was imported primarily from Egypt during the Mature Harappan phase.", False, "It was imported from Badakhshan in Afghanistan via Shortughai."),
    ("Carnelian stones naturally occur as bright red pebbles in Gujarat and require no heating.", False, "They occur as yellow-brown pebbles and require firing in ovens to oxidize the iron and turn red."),
    ("Nageshwar and Balakot were major centers for shell-working crafts.", True, "True. These coastal sites specialized in processing shells into ornaments and inlays."),
    ("Chanhudaro was a heavily fortified city with a prominent administrative Citadel mound.", False, "False. Chanhudaro was an unfortified industrial suburb with no Citadel."),
    ("Drills used for boring holes in beads were made of soft steatite.", False, "False. Drills were made of Ernestite chert, which is extremely hard."),
    ("Turquoise, a greenish-blue gemstone, was sourced from northeastern Iran and Khorasan.", True, "True. Turquoise was imported from Iran into the Indus Valley."),
    ("Shell ornaments processed on the coast were widely exported to inland metropolitan centers like Harappa.", True, "True. Shell bangles and inlays were highly valued inland luxury items."),
    ("Steatite is a soft talcose rock that was easily carved into disc beads and seals.", True, "True. Steatite (soapstone) is very soft and easily carved, hardening upon firing.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("परिपक्व हड़प्पा काल के दौरान लाजवर्द (Lapis Lazuli) का आयात मुख्य रूप से मिस्र से होता था।", False, "इसका आयात बलूचिस्तान/अफगानिस्तान के मार्ग से बदख्शां से होता था।"),
    ("अकीक (carnelian) पत्थर प्राकृतिक रूप से गुजरात में गहरे लाल रंग के मिलते थे और इन्हें गर्म करने की आवश्यकता नहीं थी।", False, "ये प्राकृतिक रूप से पीले-भूरे मिलते थे और लाल रंग प्राप्त करने के लिए इन्हें भट्टी में पकाना पड़ता था।"),
    ("नागेश्वर और बालाकोट शंख शिल्प के प्रमुख केंद्र थे।", True, "सत्य। नागेश्वर और बालाकोट तटीय शंख शिल्प के सबसे प्रमुख विनिर्माण स्थल थे।"),
    ("चन्हुदड़ो एक सुदृढ़ प्राचीर से घिरा शहर था जिसमें एक प्रशासनिक किला (Citadel) टीला था।", False, "असत्य। चन्हुदड़ो बिना किलेबंदी वाला एक औद्योगिक उपनगर था, जहाँ कोई किला नहीं मिला।"),
    ("मनकों में छेद करने के लिए प्रयुक्त होने वाले ड्रिल नरम सेलखड़ी पत्थर के बने होते थे।", False, "असत्य। ड्रिल कठोर अर्नेस्टाइट चर्ट के बने होते थे ताकि वे पत्थर छेद सकें।"),
    ("नीले-हरे रंग का रत्न फ़िरोज़ा (Turquoise) उत्तर-पूर्वी ईरान और खुरासान से मंगाया जाता था।", True, "सत्य। फ़िरोज़ा का आयात ईरान के क्षेत्रों से किया जाता था।"),
    ("तटीय इलाकों में निर्मित शंख के आभूषणों का निर्यात हड़प्पा जैसे मैदानी शहरों को किया जाता था।", True, "सत्य। शंख की चूड़ियाँ और पच्चीकारी के सामान अंतर्देशीय शहरों में भेजे जाते थे।"),
    ("सेलखड़ी (steatite) एक नरम पत्थर है जिसे आसानी से तराश कर मनके और मुहरें बनाई जा सकती थीं।", True, "सत्य। सेलखड़ी (soapstone) अत्यधिक नरम पत्थर है जो पकाने पर कठोर हो जाता था।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("Specialized bead manufacturing workshops were discovered at Chanhudaro and ___________.", "Lothal", "Lothal and Chanhudaro were the primary bead factories."),
    ("The chemical change that turns yellow-brown chalcedony to red carnelian is triggered by ___________.", "heating", "Heating (firing) causes iron oxides to turn the stone red."),
    ("Specialized shell-cutting workshops were concentrated at coastal Nageshwar and ___________.", "Balakot", "Balakot in Balochistan was a key shell-processing center."),
    ("The Harappan trade outpost established near the Badakhshan Lapis Lazuli mines was ___________.", "Shortughai", "Shortughai was the Lapis Lazuli trading colony in Afghanistan."),
    ("Bead drill bits were manufactured from a highly durable chert known as ___________.", "Ernestite", "Ernestite is the specific hard chert used for drills."),
    ("The soft talcose stone carved to make seals and micro-beads is ___________.", "steatite", "Steatite (or soapstone) was widely used for seals and beads."),
    ("Turquoise gemstone was imported into the Indus Valley primarily from ___________.", "Iran", "Turquoise came from northeastern Iran."),
    ("Shell slices cut into geometric shapes for furniture decoration were used as ___________.", "inlays", "Shell segments were used as inlays for wooden furniture.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मनका बनाने के विशिष्ट कारखाने चन्हुदड़ो और ___________ से प्राप्त हुए हैं।", "लोथल", "चन्हुदड़ो और लोथल मनका विनिर्माण के प्रमुख स्थल थे।"),
    ("पीले-भूरे पत्थर को लाल अकीक (carnelian) में बदलने वाली रासायनिक प्रक्रिया ___________ द्वारा शुरू होती थी।", "गर्म करने", "पत्थर को भट्टी में गर्म करने (पकाने) से आयरन ऑक्साइड लाल रंग देता था।"),
    ("शंख काटने की विशिष्ट कार्यशालाएं तटीय नागेश्वर और ___________ में केंद्रित थीं।", "बालाकोट", "बालाकोट बलूचिस्तान का एक तटीय शंख शिल्प केंद्र था।"),
    ("बदख्शां के लाजवर्द खानों के पास स्थापित हड़प्पा व्यापारिक चौकी का नाम ___________ था।", "शोरतूघई", "शोरतूघई (Shortughai) अफगानिस्तान में स्थापित व्यापारिक बस्ती थी।"),
    ("मनका छेदने के ड्रिल बिट्स एक अत्यधिक टिकाऊ पत्थर से बनते थे जिसे ___________ कहा जाता था।", "अर्नेस्टाइट", "अर्नेस्टाइट (Ernestite) चर्ट का उपयोग ड्रिल बनाने में होता था।"),
    ("मुहरें और सूक्ष्म मनके बनाने के लिए तराशा जाने वाला नरम पत्थर ___________ कहलाता था।", "सेलखड़ी", "सेलखड़ी (steatite) मुहरों और मनकों का मुख्य पत्थर था।"),
    ("सिंधु घाटी में फ़िरोज़ा (Turquoise) रत्न का आयात मुख्य रूप से ___________ से होता था।", "ईरान", "फ़िरोज़ा का आयात ईरान के क्षेत्रों से किया जाता था।"),
    ("लकड़ी के फर्नीचर को सजाने के लिए ज्यामितीय आकारों में काटे गए शंख के टुकड़ों का उपयोग ___________ के रूप में होता था।", "पच्चीकारी", "शंख के टुकड़ों का उपयोग पच्चीकारी (inlays) के लिए किया जाता था।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their representative craft findings:",
        "items": [{"left": "I. Chanhudaro", "key": "A"}, {"left": "II. Nageshwar", "key": "B"}, {"left": "III. Shortughai", "key": "C"}],
        "options": [{"val": "A", "text": "A. Bead factories and Ernestite drill bits"}, {"val": "B", "text": "B. Heaps of shell waste and bangles"}, {"val": "C", "text": "C. Lapis lazuli trade outpost"}],
        "sol": "Chanhudaro has bead drills, Nageshwar has shell waste, and Shortughai was the lapis outpost."
    },
    {
        "type": "Match the Following",
        "q": "Match the gemstones with their primary geological sources:",
        "items": [{"left": "I. Lapis Lazuli", "key": "A"}, {"left": "II. Carnelian", "key": "B"}, {"left": "III. Steatite", "key": "C"}],
        "options": [{"val": "A", "text": "A. Badakhshan (Afghanistan)"}, {"val": "B", "text": "B. Gulf of Khambhat (Gujarat)"}, {"val": "C", "text": "C. Aravalli Hills (Rajasthan)"}],
        "sol": "Lapis is from Badakhshan, carnelian from Gujarat, and steatite from Rajasthan."
    },
    {
        "type": "Match the Following",
        "q": "Match the raw materials with their finished craft products:",
        "items": [{"left": "I. Turbinella Pyrum (Conch)", "key": "A"}, {"left": "II. Steatite Paste", "key": "B"}, {"left": "III. Chalcedony pebbles", "key": "C"}],
        "options": [{"val": "A", "text": "A. Sawed bangles and ladles"}, {"val": "B", "text": "B. Micro-beads for necklaces"}, {"val": "C", "text": "C. Kiln-heated red carnelian beads"}],
        "sol": "Conch shell makes bangles, steatite paste makes micro-beads, and chalcedony heated makes red carnelian."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "हड़प्पा स्थलों को उनके प्रतिनिधि शिल्प साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. चन्हुदड़ो", "key": "A"}, {"left": "II. नागेश्वर", "key": "B"}, {"left": "III. शोरतूघई", "key": "C"}],
        "options": [{"val": "A", "text": "A. मनका कारखाने और अर्नेस्टाइट ड्रिल बिट्स"}, {"val": "B", "text": "B. शंख के कचरे के ढेर और चूड़ियाँ"}, {"val": "C", "text": "C. लाजवर्द रत्न की व्यापारिक चौकी"}],
        "sol": "चन्हुदड़ो में मनका ड्रिल, नागेश्वर में शंख कचरा, और शोरतूघई लाजवर्द चौकी थी।"
    },
    {
        "type": "Match the Following",
        "q": "रत्नों को उनके प्राथमिक भूवैज्ञानिक स्रोतों से सुमेलित करें:",
        "items": [{"left": "I. लाजवर्द (Lapis)", "key": "A"}, {"left": "II. अकीक (Carnelian)", "key": "B"}, {"left": "III. सेलखड़ी (Steatite)", "key": "C"}],
        "options": [{"val": "A", "text": "A. बदख्शां (अफगानिस्तान)"}, {"val": "B", "text": "B. खंभात की खाड़ी (गुजरात)"}, {"val": "C", "text": "C. अरावली पहाड़ियाँ (राजस्थान)"}],
        "sol": "लाजवर्द बदख्शां से, अकीक गुजरात से, और सेलखड़ी राजस्थान से आती थी।"
    },
    {
        "type": "Match the Following",
        "q": "कच्चे माल को उनके तैयार शिल्प उत्पादों से सुमेलित करें:",
        "items": [{"left": "I. शंख (Conch)", "key": "A"}, {"left": "II. सेलखड़ी पेस्ट", "key": "B"}, {"left": "III. पीला कैल्सीडोनी पत्थर", "key": "C"}],
        "options": [{"val": "A", "text": "A. काटी गई चूड़ियाँ और कड़छी"}, {"val": "B", "text": "B. हार के लिए बने सूक्ष्म मनके"}, {"val": "C", "text": "C. भट्टी में पकाया लाल अकीक मनका"}],
        "sol": "शंख से चूड़ियाँ, सेलखड़ी पेस्ट से सूक्ष्म मनके, और कैल्सीडोनी गर्म करने से लाल अकीक बनता था।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which site functioned as a major unfortified industrial suburb for bead-making?", "Chanhudaro in Sindh."),
    ("What process was used to turn yellow-brown raw pebbles into red carnelian?", "Kiln-heating or firing."),
    ("Name the northernmost trade colony established to control Lapis Lazuli trade.", "Shortughai in Badakhshan, Afghanistan."),
    ("What coastal site in Balochistan was famous for its shell industry?", "Balakot."),
    ("Which soft soapstone was used to make beads and seals?", "Steatite."),
    ("What stone material was used for the micro-drill bits?", "Ernestite (a very hard chert)."),
    ("Name two objects made from marine shells.", "Bangles and furniture inlays."),
    ("Where did the Harappans source turquoise from?", "Northeastern Iran.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("मनका बनाने के लिए एक प्रमुख बिना किलेबंदी वाले औद्योगिक उपनगर के रूप में कौन सा स्थल कार्य करता था?", "सिंध का चन्हुदड़ो।"),
    ("पीले-भूरे कच्चे पत्थरों को लाल अकीक (carnelian) में बदलने के लिए किस प्रक्रिया का उपयोग किया जाता था?", "भट्टी में पकाना (kiln-heating)।"),
    ("लाजवर्द (lapis) व्यापार को नियंत्रित करने के लिए स्थापित हड़प्पा की सबसे उत्तरी व्यापारिक चौकी का नाम क्या है?", "अफगानिस्तान के बदख्शां में स्थित शोरतूघई।"),
    ("बलूचिस्तान में शंख उद्योग के लिए कौन सा तटीय स्थल प्रसिद्ध था?", "बालाकोट।"),
    ("मनके और मुहरें बनाने के लिए किस नरम साबुन-पत्थर (soapstone) का उपयोग किया जाता था?", "सेलखड़ी (steatite)।"),
    ("सूक्ष्म मनकों में छेद करने वाले ड्रिल बिट्स किस पत्थर के बने होते थे?", "अर्नेस्टाइट (एक अत्यंत कठोर चर्ट पत्थर)।"),
    ("समुद्री शंखों से बनी दो वस्तुओं के नाम बताएं।", "चूड़ियाँ और फर्नीचर पर जड़ने की पच्चीकारी।"),
    ("हड़प्पा वासी फ़िरोज़ा (turquoise) रत्न कहाँ से मंगाते थे?", "उत्तर-पूर्वी ईरान से।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Chanhudaro was a dedicated industrial craft suburb of Mohenjo-daro.\nReason (R): It completely lacked fortified administrative citadels and palaces.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Nageshwar was a major production center for shell bangles and inlays.\nReason (R): The site is located directly on the coast, providing access to marine shell resources.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Lapis Lazuli was imported from the Khetri mines of Rajasthan.\nReason (R): Shortughai was a Harappan trade colony established near Lapis mines in Afghanistan.", 3, "A is false because Lapis Lazuli came from Afghanistan, not Rajasthan. R is true."),
    ("Assertion (A): Carnelian beads were heated in specialized clay pots in kilns.\nReason (R): Heating drives off water and oxidizes iron inside the stone, turning it deep red.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Scribes used bronze drills to bore holes in hard carnelian beads.\nReason (R): Bronze alloy is harder than carnelian, allowing easy drilling of stone.", 3, "A is false because bronze was too soft; hard Ernestite chert drills were used. R is false."),
    ("Assertion (A): Finished shell ornaments have been excavated at inland Mohenjo-daro.\nReason (R): Shell bangles and inlays were traded from coastal factories to inland cities.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Faience was a natural gemstone mined in the Baluchistan hills.\nReason (R): Faience is a synthetic glassy material made by firing silica sand paste.", 3, "A is false because it was artificial. R is true and explains how it was made."),
    ("Assertion (A): Steatite paste beads were widely used for necklaces.\nReason (R): Steatite paste could be easily extruded to produce tiny micro-beads.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): चन्हुदड़ो मोहनजोदड़ो का एक समर्पित औद्योगिक शिल्प उपनगर था।\nकारण (R): यहाँ किलेबंदी वाले प्रशासनिक दुर्गों और महलों का पूर्ण अभाव था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): नागेश्वर शंख की चूड़ियों और पच्चीकारी के सामानों का एक प्रमुख विनिर्माण केंद्र था।\nकारण (R): यह स्थल सीधे समुद्र तट पर स्थित था, जिससे समुद्री शंखों तक सीधी पहुंच थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): लाजवर्द (Lapis Lazuli) का आयात राजस्थान की खेतड़ी खानों से किया जाता था।\nकारण (R): शोरतूघई अफगानिस्तान में लाजवर्द खदानों के पास स्थापित एक हड़प्पा व्यापार चौकी थी।", 3, "A असत्य है क्योंकि लाजवर्द अफगानिस्तान से आता था। R सत्य है।"),
    ("कथन (A): अकीक (carnelian) के मनकों को भट्टियों में मिट्टी के बर्तनों में रखकर गर्म किया जाता था।\nकारण (R): गर्म करने से पत्थर के अंदर का पानी निकल जाता था और आयरन ऑक्साइड का ऑक्सीकरण होने से वह गहरा लाल हो जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): लेखक कठोर अकीक के मनकों में छेद करने के लिए कांसे के ड्रिलों का उपयोग करते थे।\nकारण (R): कांसे की मिश्र धातु अकीक पत्थर से अधिक कठोर होती है, जिससे छेद करना आसान था।", 3, "A असत्य है क्योंकि कांसा बहुत नरम था, कठोर अर्नेस्टाइट चर्ट के ड्रिल प्रयुक्त होते थे। R असत्य है।"),
    ("कथन (A): तैयार शंख के आभूषणों के अवशेष अंतर्देशीय मोहनजोदड़ो में मिले हैं।\nकारण (R): शंख की चूड़ियाँ और पच्चीकारी तटीय कारखानों से अंतर्देशीय बड़े शहरों को व्यापार द्वारा भेजी जाती थीं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): फेयॉन्स (faience) बलूचिस्तान की पहाड़ियों से उत्खनित एक प्राकृतिक रत्न था।\nकारण (R): फेयॉन्स एक कृत्रिम कांच जैसा पदार्थ था जो सिलिका रेत के पेस्ट को भट्टी में पकाकर बनता था।", 3, "A असत्य है क्योंकि यह कृत्रिम था। R सत्य है।"),
    ("कथन (A): सेलखड़ी पेस्ट के बने मनकों का उपयोग हार बनाने के लिए व्यापक रूप से होता था।\nकारण (R): सेलखड़ी पेस्ट को बारीक छिद्रों से दबाकर (extruding) सूक्ष्म मनके आसानी से बनाए जा सकते थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding bead factories:\n1. Bead-making kilns and working areas were discovered at Chanhudaro and Lothal.\n2. Artisans utilized specialized micro-drills made of Ernestite chert to drill the beads.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing bead factory locations and drill materials."),
    ("Consider the following statements regarding Lapis Lazuli trade:\n1. Lapis Lazuli was imported from Badakhshan via the Shortughai outpost.\n2. Shortughai was located in southern India near the Nilgiri hills.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Shortughai was in northeastern Afghanistan."),
    ("Consider the following statements regarding shell processing:\n1. Balakot was a coastal shell factory specializing in bangles and inlays.\n2. Shell ornaments were restricted to coastal areas and never found at inland sites.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: shell objects were exported in large quantities to inland sites like Harappa."),
    ("Consider the following statements regarding carnelian heating:\n1. Heating yellow-brown chalcedony in kilns turns it into deep red carnelian.\n2. Steatite is a hard volcanic rock that is impossible to carve without diamonds.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: steatite (soapstone) is very soft and easily carved."),
    ("Consider the following statements regarding raw material sourcing:\n1. Turquoise was imported from Iran.\n2. Lapis Lazuli came from Badakhshan.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing turquoise and lapis sources.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मनका कारखानों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मनका बनाने की भट्टियां और काम करने के क्षेत्र चन्हुदड़ो और लोथल से मिले हैं।\n2. शिल्पकार मनकों में छेद करने के लिए अर्नेस्टाइट चर्ट से बने सूक्ष्म ड्रिलों का उपयोग करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मनका कारखानों के स्थानों और ड्रिल पत्थर का वर्णन करते हैं।"),
    ("लाजवर्द व्यापार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लाजवर्द का आयात शोरतूघई चौकी के माध्यम से बदख्शां से किया जाता था।\n2. शोरतूघई दक्षिणी भारत में नीलगिरी पहाड़ियों के पास स्थित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शोरतूघई उत्तर-पूर्वी अफगानिस्तान में स्थित था।"),
    ("शंख प्रसंस्करण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बालाकोट शंख की चूड़ियाँ और पच्चीकारी बनाने वाला एक तटीय कारखाना था।\n2. शंख के आभूषण तटीय क्षेत्रों तक ही सीमित थे और कभी अंतर्देशीय स्थलों पर नहीं मिले।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि शंख की वस्तुओं का निर्यात भारी मात्रा में मैदानी शहरों को होता था।"),
    ("अकीक (carnelian) को गर्म करने के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पीले-भूरे पत्थरों को भट्टी में गर्म करने से वे गहरे लाल रंग में बदल जाते थे।\n2. सेलखड़ी एक कठोर ज्वालामुखीय चट्टान है जिसे बिना हीरे के तराशना असंभव था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि सेलखड़ी (steatite) अत्यंत नरम पत्थर है जिसे आसानी से तराशा जा सकता था।"),
    ("कच्ची सामग्रियों के स्रोतों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. फ़िरोज़ा (Turquoise) का आयात ईरान से किया जाता था।\n2. लाजवर्द का आयात बदख्शां से होता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो फ़िरोज़ा और लाजवर्द के स्रोतों को स्पष्ट करते हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the Harappans establish trade posts like Shortughai in Badakhshan?", "To secure direct access to the region's high-value raw Lapis Lazuli mines and control the trade routes coming from Central Asia."),
    ("Why did raw chalcedony pebbles require heat treatment in kilns?", "Because heating drives off water and oxidizes the trace iron content within the stone, changing the dull yellow-brown color into a beautiful deep red carnelian."),
    ("Why were shell-working centers located directly on the coast at sites like Nageshwar and Balakot?", "To reduce transportation costs by processing the heavy raw marine conch shells directly at the harvest sites before shipping the lightweight finished bangles and inlays inland.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा वासियों ने बदख्शां में शोरतूघई जैसी व्यापारिक चौकियां क्यों स्थापित की थीं?", "क्षेत्र की मूल्यवान लाजवर्द खदानों तक सीधी पहुंच सुरक्षित करने और मध्य एशिया से आने वाले व्यापार मार्गों को नियंत्रित करने के लिए।"),
    ("पीले-भूरे कैल्सीडोनी पत्थरों को भट्टी में पकाने (उष्मा उपचार) की आवश्यकता क्यों थी?", "क्योंकि गर्म करने से पत्थर के अंदर की नमी निकल जाती थी और लोहे के अंशों का ऑक्सीकरण होने से उसका पीला रंग गहरे लाल अकीक (carnelian) में बदल जाता था।"),
    ("नागेश्वर और बालाकोट जैसे शंख-शिल्प केंद्र सीधे समुद्र तट पर ही क्यों स्थापित किए गए थे?", "कच्चे भारी शंखों के परिवहन खर्च को बचाने के लिए, ताकि समुद्र से शंख निकालकर वहीं कारखाने में हल्की चूड़ियाँ और पच्चीकारी बनाकर सीधे बड़े शहरों को भेजी जा सकें।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did lapidaries make carnelian beads?", "By chipping raw stone into drafts, baking them to obtain red color, grinding them on sandstone slabs, polishing them, and boring holes with specialized chert drills."),
    ("How were shell bangles manufactured from raw conch shells?", "Artisans used curved bronze saws to slice the shell spire into rings, ground the rough edges on sandstone blocks, and polished them to create smooth bangles."),
    ("How were steatite paste micro-beads produced?", "By grinding soapstone scraps into a fine paste, extruding it through tiny stencils to form micro-beads, and firing them in a kiln to whiten and harden them.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("मनका निर्माता अकीक के मनके कैसे बनाते थे?", "कच्चे पत्थरों को तराश कर आकार देते थे, उन्हें भट्टी में पकाकर लाल करते थे, बलुआ पत्थर पर घिसकर चिकना करते थे, और विशिष्ट चर्ट ड्रिलों से छेद करते थे।"),
    ("कच्चे शंखों से शंख की चूड़ियाँ कैसे बनाई जाती थीं?", "शिल्पकार कांसे की घुमावदार आरी से शंख के शिखरों को काटकर छल्ले बनाते थे, उन्हें बलुआ पत्थर पर घिसकर चिकना करते थे और चमकाते थे।"),
    ("सेलखड़ी के पेस्ट से सूक्ष्म मनके (micro-beads) कैसे बनाए जाते थे?", "सेलखड़ी के बचे टुकड़ों को पीसकर महीन पेस्ट बनाया जाता था, फिर उसे छोटे सुराखों से दबाकर धागे पर बारीक दाने निकाले जाते थे, और अंत में भट्टी में पकाकर कठोर किया जाता था।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Excavations at Chanhudaro revealed sorting jars filled with unfinished carnelian beads, broken chert drills, and heating hearths under a shaded workshop bench. What does this study prove about the organization of Harappan craft?", "It proves that bead manufacturing was a highly organized, standardized, and specialized factory-like industry operating in urban craft blocks."),
    ("Case Study: Excavations at Nageshwar yielded massive heaps of discarded shell spires and debitage. Almost no whole conch shells were found. What economic process does this case study demonstrate?", "It demonstrates that Nageshwar was a primary manufacturing site where raw shells were processed and waste was discarded locally, while finished bangles were exported to inland cities."),
    ("Case Study: Compare the sourcing of Lapis Lazuli at Shortughai with local Rajasthan steatite. What does this comparison tell us about the scale of Harappan raw material procurement?", "It shows a dual procurement system: local regional sourcing (steatite from Rajasthan) combined with long-distance state-sponsored colonies (lapis from Afghanistan) to secure prestige materials.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: चन्हुदड़ो में उत्खनन से छाँटे गए मनकों के बर्तन, आधे बने अकीक मनके, टूटे चर्ट ड्रिल और काम करने के चबूतरे के पास भट्टियों के अवशेष मिले हैं। यह अध्ययन हड़प्पा शिल्प के बारे में क्या प्रमाणित करता है?", "यह प्रमाणित करता है कि मनका निर्माण एक अत्यधिक संगठित, मानकीकृत और विशिष्ट कारखाना-जैसी व्यवस्था थी जो शहरी शिल्प ब्लॉक में संचालित होती थी।"),
    ("केस स्टडी: नागेश्वर में उत्खनन से शंख के कटे हुए शिखरों और बचे हुए छिलकों के बड़े ढेर मिले हैं। पूरे समूचे शंख बहुत कम मिले हैं। यह केस स्टडी किस आर्थिक पद्धति को प्रदर्शित करती है?", "यह दर्शाती है कि नागेश्वर एक प्राथमिक विनिर्माण स्थल था जहाँ कच्चे माल का प्रसंस्करण करके कचरा स्थानीय स्तर पर फेंक दिया जाता था, जबकि तैयार चूड़ियों का निर्यात किया जाता था।"),
    ("केस स्टडी: शोरतूघई से लाजवर्द की प्राप्ति और राजस्थान से स्थानीय सेलखड़ी की प्राप्ति की तुलना करें। यह तुलना हड़प्पा के कच्चे माल की प्राप्ति के पैमाने के बारे में क्या बताती है?", "यह एक दोहरी खरीद प्रणाली को दर्शाती है: स्थानीय क्षेत्रीय खरीद (राजस्थान से सेलखड़ी) और प्रतिष्ठा की वस्तुओं को सुरक्षित करने के लिए लंबी दूरी की राज्य-प्रायोजित बस्तियाँ (अफगानिस्तान से लाजवर्द)।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Lapidary Craft' in the Harappan Civilisation to a beginner.", "Lapidary craft is the art of turning raw, rough rocks into polished gemstone beads and ornaments. In Harappa, this involved heating stone in ovens to change its color, grinding it on stone blocks, and using specialized chert drills to drill microscopic holes for necklaces."),
    ("Explain how coastal Nageshwar and Balakot acted as specialized industrial suburbs.", "Nageshwar and Balakot were not large administrative capitals like Mohenjo-daro. Instead, they were specialized industrial towns built on the coast to harvest marine shells, carve them into bangles and inlays, and supply finished goods to the empire's trade network."),
    ("Explain why 'Ernestite' chert drills were a key technological innovation in lapidary craft.", "Ernestite is a rare, ultra-dense chert. Standard bronze drills were too soft and would bend or wear down when drilling hard stones like carnelian and jasper. Developing Ernestite drills allowed the Harappans to mass-produce stone beads with precise holes.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक नौसिखिए को हड़प्पा सभ्यता में 'रत्न-शिल्प (Lapidary Craft)' की अवधारणा समझाएं।", "रत्न-शिल्प कच्चे, खुरदरे पत्थरों को पॉलिश करके रत्नों और मनकों में बदलने की कला है। हड़प्पा में, इसमें पत्थर का रंग बदलने के लिए उसे भट्टियों में पकाना, पत्थर की घिसाई करना और हार के लिए बारीक छेद करने हेतु चर्ट के सूक्ष्म ड्रिलों का उपयोग करना शामिल था।"),
    ("समझाएं कि कैसे तटीय नागेश्वर और बालाकोट विशिष्ट औद्योगिक उपनगरों के रूप में कार्य करते थे।", "नागेश्वर और बालाकोट मोहनजोदड़ो जैसे बड़े प्रशासनिक केंद्र नहीं थे। बल्कि, वे तटीय क्षेत्रों में स्थापित विशिष्ट औद्योगिक कस्बे थे जिनका कार्य समुद्र से शंख निकालना, उनकी चूड़ियाँ बनाना और साम्राज्य के व्यापारिक नेटवर्क को तैयार माल की आपूर्ति करना था।"),
    ("समझाएं कि मनका उद्योग में 'अर्नेस्टाइट' चर्ट ड्रिल एक प्रमुख तकनीकी नवाचार क्यों था।", "अर्नेस्टाइट एक अत्यंत सघन और कठोर चर्ट पत्थर है। साधारण कांसे के ड्रिल बहुत नरम थे और अकीक जैसे पत्थरों में छेद करते समय मुड़ या घिस जाते थे। अर्नेस्टाइट ड्रिल के आविष्कार ने हड़प्पा वासियों को कठोर पत्थरों में सटीक छेद वाले मनके बनाने में सक्षम बनाया।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 1 Mastery questions populated: {len(s1_mastery_eng)} (Eng), {len(s1_mastery_hin)} (Hin)")

# =========================================================================
# SECTION 2: METALLURGY, BRONZE CASTING & SCULPTURE
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("What specialized metallurgical technique was used to cast bronze statues like the Dancing Girl?", ["Lost-Wax casting (cire perdue)", "Sand-casting with wood stencils", "Forging with iron hammers", "Electro-plating with gold leaf"], 0, "The lost-wax method (cire perdue) was used for both solid and hollow bronze figures."),
    ("The primary metal alloy component added to copper by Harappan smiths to manufacture bronze was:", ["Tin", "Iron", "Zinc", "Lead"], 0, "Tin was alloyed with copper to manufacture bronze tools and statues."),
    ("Where was the famous steatite bust of the Priest-King discovered?", ["Mohenjo-daro", "Harappa", "Lothal", "Kalibangan"], 0, "The Priest-King steatite sculpture was excavated at Mohenjo-daro."),
    ("The realistic red sandstone male torso showing detachable limbs was excavated at which site?", ["Harappa", "Mohenjo-daro", "Dholavira", "Lothal"], 0, "The red sandstone torso showing socket joints was found at Harappa."),
    ("Harappan terracotta figurines were primarily manufactured using which technique?", ["Hand-modeling (pinching method)", "Two-part clay mold casting", "Potter's wheel turning", "Carving from solid baked clay blocks"], 0, "Terracotta figures were hand-modeled, often utilizing a pinching method for facial details.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("कांस्य नर्तकी (Dancing Girl) जैसी कांस्य मूर्तियों को ढालने के लिए किस विशिष्ट तकनीकी का प्रयोग किया जाता था?", ["लुप्त-मोम ढलाई पद्धति (cire perdue)", "लकड़ी के स्टेंसिल से बालू-ढलाई", "लोहे के हथौड़ों से ढलाई", "सोने के पानी से इलेक्ट्रो-प्लेटिंग"], 0, "खोखली और ठोस कांस्य मूर्तियों को ढालने के लिए लुप्त-मोम पद्धति (lost-wax casting) का उपयोग किया जाता था।"),
    ("कांस्य (bronze) बनाने के लिए हड़प्पा के धातुकारों द्वारा तांबे में मिलाई जाने वाली प्राथमिक मिश्र धातु क्या थी?", ["टिन", "लोहा", "जस्ता", "शीशा"], 0, "तांबे में टिन (tin) मिलाकर कांस्य के उपकरण और मूर्तियां बनाई जाती थीं।"),
    ("पुरोहित-राजा (Priest-King) की प्रसिद्ध सेलखड़ी की अर्ध-मूर्ति कहाँ खोजी गई थी?", ["मोहनजोदड़ो", "हड़प्पा", "लोथल", "कालीबंगन"], 0, "पुरोहित-राजा की सेलखड़ी से बनी मूर्ति मोहनजोदड़ो से प्राप्त हुई थी।"),
    ("अलग होने वाले हाथ-पैर जोड़ने के सॉकेट वाला यथार्थवादी लाल बलुआ पत्थर का मानव धड़ किस स्थल से मिला है?", ["हड़प्पा", "मोहनजोदड़ो", "धोलावीरा", "लोथल"], 0, "सॉकेट जोड़ों वाला लाल बलुआ पत्थर का मानव धड़ हड़प्पा से खोजा गया था।"),
    ("हड़प्पा की मिट्टी की मूर्तियाँ (terracotta figurines) मुख्य रूप से किस तकनीक से बनाई जाती थीं?", ["हाथ से गढ़ना (पिंचिंग विधि)", "दो-भाग वाले मिट्टी के सांचे में ढलाई", "कुम्हार के चाक पर घुमाना", "पके हुए मिट्टी के ठोस ब्लॉकों से नक्काशी"], 0, "मिट्टी की मूर्तियां हाथ से गढ़ी (hand-modeled) जाती थीं, जिनमें नाक-कान बनाने के लिए उंगलियों से मिट्टी दबाई (pinch) जाती थी।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which bronze figures were cast using the lost-wax casting technique? (Select all that apply)", ["The Dancing Girl statue", "The bronze humped bull from Mohenjo-daro", "The bronze buffalo figurine", "Iron chariot models from Harappa"], [0, 1, 2], "Dancing Girl, bronze bull, and bronze buffalo were lost-wax cast. Iron did not exist."),
    ("Select the copper and bronze tools manufactured by Harappan metal smiths: (Select all that apply)", ["Flat chisels and knives", "Curved saws with offset teeth", "Fish hooks and razors", "Mid-ribbed long swords"], [0, 1, 2], "Chisels, saws, and fish hooks were common. Mid-ribbed long swords are absent from IVC sites."),
    ("What are the key details of the Priest-King steatite bust? (Select all that apply)", ["Carved from soft steatite stone", "Draped in a shawl featuring trefoil decorations", "Features elongated, meditative, half-closed eyes", "Wearing a golden crown decorated with rubies"], [0, 1, 2], "It is steatite, wears a trefoil shawl, and has meditative eyes. No golden crown was found."),
    ("Identify the materials used to carve three-dimensional sculptures: (Select all that apply)", ["Steatite", "Bronze", "Red sandstone", "Cast iron"], [0, 1, 2], "Steatite, bronze, and sandstone were carved. Iron did not exist."),
    ("Which of the following characterises Harappan terracotta art? (Select all that apply)", ["Mainly hand-modeled using clay pinching", "Represents folk toys like toy carts and sliding monkeys", "Includes depictions of Mother Goddesses with fan-shaped headdresses", "Constructed using advanced stone-masonry techniques"], [0, 1, 2], "Terracotta is hand-modeled, represents toys, and includes Mother Goddesses. It is not stone-masonry.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("लुप्त-मोम ढलाई तकनीक का उपयोग करके किन कांस्य आकृतियों को ढाला गया था? (सभी लागू विकल्प चुनें)", ["कांस्य नर्तकी की मूर्ति", "मोहनजोदड़ो से कांस्य का कूबड़ वाला सांड", "कांस्य भैंसे की मूर्ति", "हड़प्पा से लोहे के रथ का मॉडल"], [0, 1, 2], "नर्तकी, सांड और भैंसे की कांस्य मूर्तियाँ मिली हैं। लोहे का अस्तित्व नहीं था।"),
    ("हड़प्पा के धातुकारों द्वारा बनाए गए तांबे और कांसे के उपकरणों का चयन करें: (सभी लागू विकल्प चुनें)", ["चपटी छेनी और चाकू", "टेढ़े दांतों वाली घुमावदार आरी", "मछली पकड़ने के कांटे और उस्तरे", "मध्य-पसली वाली लंबी तलवारें"], [0, 1, 2], "छेनी, आरी और मछली के कांटे आम थे। लंबी तलवारें हड़प्पा स्थलों से नहीं मिली हैं।"),
    ("पुरोहित-राजा की सेलखड़ी की अर्ध-मूर्ति के मुख्य लक्षण क्या हैं? (सभी लागू विकल्प चुनें)", ["नरम सेलखड़ी पत्थर से तराशी गई है", "तिपतिया अलंकरण वाले शॉल से ढकी है", "आँखें लंबी, ध्यान की मुद्रा में आधी बंद हैं", "माणिक जड़ा सोने का मुकुट पहने है"], [0, 1, 2], "यह सेलखड़ी की है, तिपतिया शॉल ओढ़े है और ध्यानमग्न आँखें हैं। सोने का मुकुट नहीं था।"),
    ("त्रि-आयामी मूर्तियां बनाने के लिए प्रयुक्त सामग्रियों की पहचान करें: (सभी लागू विकल्प चुनें)", ["सेलखड़ी (Steatite)", "कांसा (Bronze)", "लाल बलुआ पत्थर (Red sandstone)", "ढला हुआ लोहा (Cast iron)"], [0, 1, 2], "सेलखड़ी, कांसा और बलुआ पत्थर प्रयुक्त होते थे। लोहे का उपयोग नहीं होता था।"),
    ("निम्नलिखित में से कौन हड़प्पा टेराकोटा कला को दर्शाता है? (सभी लागू विकल्प चुनें)", ["मुख्य रूप से हाथ से मिट्टी पिंच करके बनाया जाना", "खिलौना गाड़ियों और सरकने वाले बंदरों जैसे लोक खिलौने", "पंखा मुकुट वाली मातृदेवी की मूर्तियों का चित्रण", "उन्नत पत्थर की नक्काशी तकनीक से निर्माण"], [0, 1, 2], "टेराकोटा हाथ से बना था, इसमें खिलौने और मातृदेवी शामिल थीं। यह पत्थर की नक्काशी नहीं है।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Harappans possessed advanced iron metallurgy, manufacturing heavy steel swords.", False, "Iron was completely unknown to the Harappans; they used copper and bronze."),
    ("The Dancing Girl statue was cast in bronze using the lost-wax (cire perdue) method.", True, "True. She is a premier example of early Bronze Age lost-wax casting."),
    ("The lost-wax method involves creating a wax model that is later replaced by molten bronze.", True, "True. The wax melts and is replaced by liquid bronze inside a clay mold."),
    ("The Priest-King sculpture shows a high degree of artistic realism, wearing a trefoil-patterned shawl.", True, "True. The bust features a cloak with trefoil decorations once filled with red paste."),
    ("The red sandstone torso showing detailed anatomy was discovered at Mohenjo-daro.", False, "False. It was excavated at Harappa."),
    ("Terracotta toys include kinetic figures like monkeys that could slide down a string.", True, "True. Sliding monkeys and moving-head bulls represent early kinetic toys."),
    ("Harappans used two-part metal molds to mass-produce bronze statues.", False, "False. Bronze statues were unique hand-made lost-wax items, not mass-produced in metal molds."),
    ("Copper was sourced primarily from the Khetri mines of Rajasthan.", True, "True. Khetri mines were the main source of copper for Harappan smiths.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा वासियों के पास उन्नत लौह धातुकर्म था, और वे भारी स्टील की तलवारें बनाते थे।", False, "लोहा हड़प्पा सभ्यता में पूरी तरह अज्ञात था; वे तांबे और कांसे का उपयोग करते थे।"),
    ("कांस्य नर्तकी की मूर्ति को लुप्त-मोम (lost-wax) पद्धति से बनाया गया था।", True, "सत्य। यह प्रारंभिक कांस्य युग की लुप्त-मोम ढलाई का सबसे प्रसिद्ध उदाहरण है।"),
    ("लुप्त-मोम पद्धति में पहले मोम का मॉडल बनाया जाता है जिसे बाद में पिघली हुई धातु से बदल दिया जाता है।", True, "सत्य। मिट्टी के सांचे में गर्म करने पर मोम निकल जाता है और उसकी जगह कांसा ले लेता है।"),
    ("पुरोहित-राजा की मूर्ति में कलात्मक यथार्थवाद है और वह तिपतिया पैटर्न वाला शॉल ओढ़े हैं।", True, "सत्य। शॉल पर तिपतिया आकृतियाँ हैं जिनमें कभी लाल रंग भरा होता था।"),
    ("शारीरिक रचना दर्शाने वाला लाल बलुआ पत्थर का मानव धड़ मोहनजोदड़ो से खोजा गया था।", False, "असत्य। यह हड़प्पा से खोजा गया था।"),
    ("मिट्टी के खिलौनों में धागे पर सरकने वाले बंदर जैसी गतिज (kinetic) आकृतियाँ भी शामिल थीं।", True, "सत्य। धागे पर सरकने वाले बंदर और सिर हिलाने वाले बैल इसके उदाहरण हैं।"),
    ("हड़प्पा वासी कांस्य मूर्तियों का बड़े पैमाने पर उत्पादन करने के लिए धातु के दो-भाग वाले सांचों का उपयोग करते थे।", False, "असत्य। कांस्य मूर्तियाँ लुप्त-मोम पद्धति से बनाई जाने वाली अद्वितीय कलाकृतियाँ थीं, सांचे से बड़े पैमाने पर नहीं बनती थीं।"),
    ("तांबा मुख्य रूप से राजस्थान की खेतड़ी खदानों से प्राप्त किया जाता था।", True, "सत्य। खेतड़ी की खदानें हड़प्पा वासियों के लिए तांबे की आपूर्ति का मुख्य स्रोत थीं।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The technical French/Latin name for the lost-wax casting technique is ___________.", "cire perdue", "Cire perdue is the alternate term for lost-wax casting."),
    ("The famous bronze figurine of a standing female holding her hand on her hip is the ___________.", "Dancing Girl", "The 4-inch Mohenjo-daro bronze is known as the Dancing Girl."),
    ("Copper was sourced primarily from the ___________ mines in modern Rajasthan.", "Khetri", "Khetri mines supplied copper to Harappan sites."),
    ("The Priest-King bust is carved from a soft, talcose rock called ___________.", "steatite", "Steatite (or soapstone) was used to carve the Priest-King."),
    ("The red sandstone torso features circular ___________ to connect movable head and arms.", "sockets", "Socket joints allowed separate limbs to be attached."),
    ("Hand-modeled baked clay figures and toys are known as ___________.", "terracotta", "Terracotta refers to baked clay artwork."),
    ("Tin was mixed with copper in workshops to manufacture the alloy ___________.", "bronze", "Bronze is an alloy of copper and tin."),
    ("Copper saws were designed with ___________ teeth to facilitate cutting wood.", "offset", "Offset teeth prevent the saw blade from binding.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लुप्त-मोम ढलाई तकनीक का तकनीकी फ्रांसीसी/लैटिन नाम ___________ है।", "cire perdue", "लुप्त-मोम पद्धति को cire perdue भी कहा जाता है।"),
    ("अपने कूल्हे पर हाथ रखे खड़ी स्त्री की प्रसिद्ध कांस्य मूर्ति को ___________ कहा जाता है।", "नर्तकी", "चार इंच की मोहनजोदड़ो कांस्य मूर्ति को 'नर्तकी' (Dancing Girl) नाम दिया गया है।"),
    ("तांबा मुख्य रूप से आधुनिक राजस्थान की ___________ खदानों से मंगाया जाता था।", "खेतड़ी", "खेतड़ी (Khetri) की खानें तांबे का मुख्य स्रोत थीं।"),
    ("पुरोहित-राजा की मूर्ति को ___________ नामक नरम पत्थर से तराशा गया है।", "सेलखड़ी", "सेलखड़ी (steatite) पत्थर का उपयोग पुरोहित-राजा की मूर्ति में हुआ था।"),
    ("लाल बलुआ पत्थर के मानव धड़ में चलने वाले हाथ-पैर जोड़ने के लिए गोल ___________ बने हैं।", "सॉकेट", "सॉकेट (sockets) या छेद अलग से हाथ-पैर जोड़ने के लिए थे।"),
    ("हाथ से गढ़कर पकाए गए मिट्टी के खिलौनों और मूर्तियों को ___________ कहा जाता है।", "टेराकोटा", "पकी मिट्टी के इन शिल्पों को टेराकोटा (terracotta) कहा जाता है।"),
    ("धातुशालाओं में मिश्र धातु बनाने के लिए तांबे में टिन मिलाया जाता था, जिसे ___________ कहते हैं।", "कांसा", "तांबे और टिन के मिश्रण से कांसा (bronze) बनता है।"),
    ("लकड़ी काटने की सुविधा के लिए तांबे की आरी के दांतों को ___________ (तिरछा) सेट किया जाता था।", "ऑफसेट", "दांतों को ऑफसेट (offset) सेट करने से आरी लकड़ी में फंसती नहीं थी।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sculptures with their primary materials:",
        "items": [{"left": "I. Dancing Girl", "key": "A"}, {"left": "II. Priest-King", "key": "B"}, {"left": "III. Male Torso", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lost-wax cast bronze"}, {"val": "B", "text": "B. Carved steatite (soapstone)"}, {"val": "C", "text": "C. Red jasper/sandstone"}],
        "sol": "Dancing Girl is bronze, Priest-King is steatite, and Male Torso is red sandstone."
    },
    {
        "type": "Match the Following",
        "q": "Match the crafts with their characteristic techniques:",
        "items": [{"left": "I. Bronze figurines", "key": "A"}, {"left": "II. Terracotta toys", "key": "B"}, {"left": "III. Stone sculptures", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lost-wax casting (cire perdue)"}, {"val": "B", "text": "B. Hand-modeling and pinching clay"}, {"val": "C", "text": "C. Fine carving with chert drills and firing"}],
        "sol": "Bronze uses lost-wax, terracotta is hand-modeled, and stone is carved/fired."
    },
    {
        "type": "Match the Following",
        "q": "Match the tools/figurines with their archaeological sites:",
        "items": [{"left": "I. Dancing Girl", "key": "A"}, {"left": "II. Male Torso", "key": "B"}, {"left": "III. Copper fish hooks", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mohenjo-daro Citadel ruins"}, {"val": "B", "text": "B. Harappa residential mounds"}, {"val": "C", "text": "C. Lothal and coastal port sites"}],
        "sol": "Dancing Girl is from Mohenjo-daro, torso from Harappa, and fish hooks from Lothal/coastal sites."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "मूर्तियों को उनके प्राथमिक विनिर्माण घटकों से सुमेलित करें:",
        "items": [{"left": "I. कांस्य नर्तकी", "key": "A"}, {"left": "II. पुरोहित-राजा", "key": "B"}, {"left": "III. पुरुष धड़", "key": "C"}],
        "options": [{"val": "A", "text": "A. लुप्त-मोम ढलाई पद्धति से बना कांसा"}, {"val": "B", "text": "B. नक्काशीदार सेलखड़ी (soapstone)"}, {"val": "C", "text": "C. लाल बलुआ पत्थर"}],
        "sol": "नर्तकी कांस्य की है, पुरोहित-राजा सेलखड़ी का है, और धड़ लाल बलुआ पत्थर का है।"
    },
    {
        "type": "Match the Following",
        "q": "शिल्प विधाओं को उनकी विशिष्ट तकनीकों से सुमेलित करें:",
        "items": [{"left": "I. कांस्य मूर्तियाँ", "key": "A"}, {"left": "II. मिट्टी के खिलौने", "key": "B"}, {"left": "III. पाषाण मूर्तियाँ", "key": "C"}],
        "options": [{"val": "A", "text": "A. लुप्त-मोम पद्धति (cire perdue)"}, {"val": "B", "text": "B. हाथ से गढ़ना और मिट्टी दबाना (pinching)"}, {"val": "C", "text": "C. चर्ट औजारों से नक्काशी और पकाना"}],
        "sol": "कांस्य में लुप्त-मोम प्रयुक्त होता था, खिलौने हाथ से बनते थे, और पत्थर की नक्काशी व पकाई होती थी।"
    },
    {
        "type": "Match the Following",
        "q": "उपकरणों/मूर्तियों को उनके प्राप्ति स्थलों से सुमेलित करें:",
        "items": [{"left": "I. कांस्य नर्तकी", "key": "A"}, {"left": "II. पुरुष धड़", "key": "B"}, {"left": "III. तांबे के मछली कांटे", "key": "C"}],
        "options": [{"val": "A", "text": "A. मोहनजोदड़ो के खंडहर"}, {"val": "B", "text": "B. हड़प्पा के आवासीय टीले"}, {"val": "C", "text": "C. लोथल और तटीय गोदीवाड़ा क्षेत्र"}],
        "sol": "नर्तकी मोहनजोदड़ो से, धड़ हड़प्पा से, और मछली कांटे लोथल/तटीय बंदरगाहों से मिले हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What metallurgical technique was used to manufacture hollow bronze statues?", "The lost-wax casting technique (cire perdue)."),
    ("Where was the steatite bust of the Priest-King discovered?", "Mohenjo-daro."),
    ("Which metal was alloyed with copper to manufacture bronze?", "Tin."),
    ("Name the main mining area in Rajasthan that supplied copper.", "Khetri mines."),
    ("Why did the red sandstone torso from Harappa have socket holes?", "To connect detachable head and arms, forming a composite statue."),
    ("What is the approximate height of the bronze Dancing Girl figurine?", "4 inches (10.5 cm)."),
    ("Were Harappan terracotta toys hand-modeled or molded?", "Hand-modeled."),
    ("What key military weapons are completely absent in Harappan bronze tool kits?", "Specialized armor, helmets, and long swords.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("खोखली कांस्य मूर्तियाँ बनाने के लिए किस धातुकर्म तकनीक का उपयोग किया जाता था?", "लुप्त-मोम ढलाई पद्धति (lost-wax casting या cire perdue)।"),
    ("पुरोहित-राजा (Priest-King) की अर्ध-मूर्ति कहाँ मिली थी?", "मोहनजोदड़ो में।"),
    ("कांसा बनाने के लिए तांबे में किस धातु को मिश्रित किया जाता था?", "टिन (tin)।"),
    ("राजस्थान के उस मुख्य खनन क्षेत्र का नाम बताएं जो तांबे की आपूर्ति करता था?", "खेतड़ी (Khetri) खदानें।"),
    ("हड़प्पा से प्राप्त लाल बलुआ पत्थर के धड़ में सॉकेट छेद क्यों बने थे?", "चलने वाले अलग सिर और हाथ जोड़ने के लिए, जिससे एक संयुक्त मूर्ति बनती थी।"),
    ("कांस्य नर्तकी मूर्ति की अनुमानित ऊंचाई क्या है?", "4 इंच (10.5 सेमी)।"),
    ("क्या हड़प्पा के मिट्टी के खिलौने हाथ से बने थे या सांचे में ढाले गए थे?", "हाथ से बने (hand-modeled) थे।"),
    ("हड़प्पा के कांस्य उपकरणों में युद्ध के कौन से प्रमुख हथियार पूरी तरह गायब हैं?", "विशेष सैनिक कवच (armor), हेलमेट और लंबी तलवारें।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappans are celebrated for their highly realistic bronze sculptures.\nReason (R): They utilized the lost-wax (cire perdue) technique, which allowed detailed metallic reproduction.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Priest-King bust is carved from hard granite stone.\nReason (R): Granite is highly resistant to weathering, explaining the bust's survival.", 3, "A is false because it is carved from soft steatite. R is false."),
    ("Assertion (A): Tin was alloyed with copper to manufacture bronze tools.\nReason (R): Copper is too soft on its own, and adding tin increases structural hardness.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Iron chisels were preferred by Harappan stonemasons.\nReason (R): Scribes recorded massive iron ore shipments coming from the Indus delta.", 3, "Both A and R are false (iron was unknown to the Harappans)."),
    ("Assertion (A): Terracotta figurines reflect a popular, folk artistic tradition.\nReason (R): Terracotta objects were hand-modeled, cheap, and widely distributed in common domestic quarters.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The red sandstone torso from Harappa displays socket connections.\nReason (R): Scribes used socketed joints to mount statues on monumental stone pillars.", 2, "A is true but R is false (statues were small and domestic, not mounted on pillars)."),
    ("Assertion (A): Saws carved by Harappans had teeth set in a straight line.\nReason (R): Offset teeth prevent the saw blade from getting stuck in wood during cutting.", 3, "A is false because teeth were offset. R is true."),
    ("Assertion (A): The Dancing Girl is depicted standing in a fluid, expressive pose.\nReason (R): She is shown with one hand on her hip in the tribhanga dancing posture.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा वासी अपनी अत्यधिक यथार्थवादी कांस्य मूर्तियों के लिए प्रसिद्ध हैं।\nकारण (R): वे लुप्त-मोम (cire perdue) तकनीक का उपयोग करते थे, जिससे धातु पर बारीक विवरण उकेरे जा सकते थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): पुरोहित-राजा की मूर्ति को कठोर ग्रेनाइट पत्थर से तराशा गया है।\nकारण (R): ग्रेनाइट अपक्षय के प्रति बहुत प्रतिरोधी होता है, जिससे यह मूर्ति बची रही।", 3, "A असत्य है क्योंकि यह नरम सेलखड़ी से बनी है। R असत्य है।"),
    ("कथन (A): कांस्य के उपकरण बनाने के लिए तांबे में टिन मिलाया जाता था।\nकारण (R): शुद्ध तांबा बहुत नरम होता है, और टिन मिलाने से धातु की कठोरता बढ़ जाती है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के राजमिस्त्री लोहे की छेनियों को पसंद करते थे।\nकारण (R): लेखकों ने सिंधु डेल्टा से आने वाले लोहे के बड़े लदानों को दर्ज किया था।", 3, "A और R दोनों असत्य हैं (लोहा हड़प्पा में अज्ञात था)।"),
    ("कथन (A): मिट्टी की आकृतियाँ (terracotta) एक लोकप्रिय लोक कला परंपरा को दर्शाती हैं।\nकारण (R): ये आकृतियाँ हाथ से बनी, सस्ती और आम लोगों के घरों में प्रचुर मात्रा में फैली थीं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा से मिले लाल बलुआ पत्थर के धड़ में सॉकेट जोड़ बने हैं।\nकारण (R): शिल्पकार मूर्तियों को सार्वजनिक पत्थर के स्तंभों पर लगाने के लिए इन जोड़ों का उपयोग करते थे।", 2, "A सत्य है लेकिन R असत्य है (मूर्तियाँ छोटी थीं, स्तंभों पर लगाने के लिए नहीं)।"),
    ("कथन (A): हड़प्पा वासियों द्वारा बनाई गई आरी के दांत एक सीधी रेखा में होते थे।\nकारण (R): दांतों को ऑफसेट करने से लकड़ी काटते समय आरी की ब्लेड फंसने से बचती थी।", 3, "A असत्य है क्योंकि दांत ऑफसेट (टेढ़े-मेढ़े) होते थे। R सत्य है।"),
    ("कथन (A): कांस्य नर्तकी की मूर्ति एक लचीली और सहज मुद्रा में खड़ी दिखाई गई है।\nकारण (R): वह एक हाथ कूल्हे पर रखकर त्रिभंग नृत्य मुद्रा में खड़ी है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the lost-wax casting technique:\n1. The wax model was melted out before pouring molten bronze.\n2. Both solid and hollow bronze figures were cast using this method.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing lost-wax bronze casting."),
    ("Consider the following statements regarding tool metallurgy:\n1. Saws featured offset teeth to prevent binding.\n2. Iron was added to copper to make tools hard.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: iron was unknown."),
    ("Consider the following statements regarding stone sculptures:\n1. The Priest-King is carved from steatite.\n2. The red male torso is from Mohenjo-daro.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: the torso is from Harappa."),
    ("Consider the following statements regarding terracotta toys:\n1. Toy wheels were solid with no spokes.\n2. Many toys featured moving parts like sliding monkeys.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing solid wheels and kinetic sliding monkeys."),
    ("Consider the following statements regarding bronze items:\n1. Bronze armor and helmets are common at Harappa.\n2. The Dancing Girl figurine shows she wore bangles on her left arm.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: Harappans lacked metal armor or helmets.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लुप्त-मोम ढलाई पद्धति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पिघला हुआ कांसा डालने से पहले मोम के मॉडल को पिघलाकर निकाल दिया जाता था।\n2. इस विधि से खोखली और ठोस दोनों प्रकार की कांस्य मूर्तियाँ ढाली जाती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो लुप्त-मोम ढलाई प्रक्रिया का वर्णन करते हैं।"),
    ("उपकरण धातुकर्म के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. लकड़ी में फंसने से बचाने के लिए आरी के दांत ऑफसेट सेट किए जाते थे।\n2. औजारों को कठोर बनाने के लिए तांबे में लोहा मिलाया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि लोहा सिंधु सभ्यता में अज्ञात था।"),
    ("पाषाण मूर्तियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. पुरोहित-राजा की मूर्ति सेलखड़ी से बनी है।\n2. लाल पुरुष धड़ मोहनजोदड़ो से प्राप्त हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि पुरुष धड़ हड़प्पा से मिला था।"),
    ("मिट्टी के खिलौनों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. खिलौना पहिये ठोस थे, उनमें तीलियाँ नहीं थीं।\n2. कई खिलौनों में चलने वाले भाग थे, जैसे सरकने वाले बंदर।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो ठोस पहियों और गतिज खिलौनों का वर्णन करते हैं।"),
    ("कांस्य की वस्तुओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा में कांस्य के कवच और हेलमेट प्रचुर मात्रा में मिले हैं।\n2. कांस्य नर्तकी मूर्ति की बाईं भुजा चूड़ियों से भरी हुई दिखाई देती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि हड़प्पा वासी धातु के सैन्य कवच नहीं बनाते थे।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the copper saws of the Harappans feature offset teeth?", "To cut a groove wider than the blade itself, preventing the blade from binding or getting stuck in the wood during sawing."),
    ("Why did the sculptor carve socket holes into the red sandstone male torso from Harappa?", "To allow detachable limbs (head and arms) to be carved separately and attached to the main torso, forming a composite sculpture."),
    ("Why did the Harappans rely on importing tin from Afghanistan and Central Asia?", "Because the local Indus Valley region had no tin deposits, and tin was essential to alloy with copper to produce harder bronze tools.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के तांबे की आरी में दांतों को ऑफसेट (तिरछा) क्यों लगाया जाता था?", "ताकि आरी ब्लेड की मोटाई से थोड़ा चौड़ा कट बना सके, जिससे लकड़ी काटते समय ब्लेड फंसने या रुकने से बचती थी।"),
    ("शिल्पकार ने हड़प्पा से प्राप्त लाल बलुआ पत्थर के पुरुष धड़ में सॉकेट छेद क्यों खोदे थे?", "ताकि अलग से तराशे गए हाथ-पैर और सिर को धड़ से जोड़ा जा सके, जिससे एक संयुक्त (composite) मूर्ति तैयार हो सके।"),
    ("हड़प्पा वासी अफगानिस्तान और मध्य एशिया से टिन आयात करने पर क्यों निर्भर थे?", "क्योंकि स्थानीय सिंधु घाटी क्षेत्र में टिन का कोई भंडार नहीं था, और तांबे के साथ मिलाने के लिए टिन अनिवार्य था ताकि मजबूत कांस्य बनाया जा सके।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How does the lost-wax casting technique (cire perdue) work?", "The artist sculpts a figure in wax, encases it in clay, fires the clay mold so the wax melts and drains out, pours molten bronze into the empty cavity, and breaks the clay mold after cooling."),
    ("How did Harappan sculptors finish the details on steatite statues like the Priest-King?", "They carved the soft steatite stone, smoothed the surfaces, engraved details (like the trefoil patterns), and baked the bust in a kiln to whiten and harden the talc stone."),
    ("How did toy-makers create kinetic or moving elements in terracotta figures?", "By using clay axles for wheels, and drilling holes to run string or fiber through animal heads and limbs, allowing kids to pull strings and move the parts.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("लुप्त-मोम ढलाई तकनीक (cire perdue) कैसे काम करती है?", "कलाकार मोम की मूर्ति बनाता है, उसे मिट्टी के लेप से ढकता है, सांचे को गर्म कर मोम बाहर निकालता है, खाली जगह में पिघला कांसा भरता है, और ठंडा होने पर मिट्टी तोड़कर मूर्ति निकालता है।"),
    ("हड़प्पा के मूर्तिकार सेलखड़ी की मूर्तियों पर विवरणों को कैसे अंतिम रूप देते थे?", "वे नरम सेलखड़ी पत्थर पर नक्काशी करते थे, सतह को चिकना करते थे, तिपतिया डिज़ाइन उकेरते थे, और अंत में भट्टी में पकाकर पत्थर को कठोर व सफेद बनाते थे।"),
    ("खिलौना निर्माता मिट्टी के खिलौनों में चलने या हिलने वाले पुर्जे कैसे बनाते थे?", "पहियों के लिए मिट्टी की धुरी बनाकर, और जानवरों के सिर व हाथ-पैरों में छेद करके धागा पिरोते थे, जिससे धागा खींचने पर वे हिल सकें।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The bronze Dancing Girl features a relaxed tribhanga dance pose, with her hair in a bun and 24 bangles on her left arm. What does this case study tell us about Harappan society?", "It shows that dance, personal adornment, and female artistic representation were integrated into daily life, and metallurgy was highly developed."),
    ("Case Study: Analyze the copper source at the Khetri mines of Rajasthan. How did the Harappan state manage raw materials without controlling the region politically?", "Through a trade network with the local Ganeshwar-Jodhpura chalcolithic culture, exchanging agricultural food surplus and finished tools for raw copper ingots."),
    ("Case Study: Compare Harappan stone sculptures with monumental Egyptian statues. Why are Harappan works so small (under 20 cm)?", "It reflects a commercial, civic society that prioritized domestic utility, personal ornaments, and small-scale portable art over grand royal monuments.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: कांस्य नर्तकी (Dancing Girl) त्रिभंग नृत्य मुद्रा में खड़ी है, उसके बाल जूड़े में हैं और उसकी बाईं बांह में 24 चूड़ियाँ हैं। यह केस स्टडी हड़प्पा समाज के बारे में क्या बताती है?", "यह दर्शाती है कि नृत्य कला, शारीरिक श्रृंगार और महिला कलात्मक प्रदर्शन दैनिक जीवन का हिस्सा थे, और कांस्य ढलाई धातुकर्म अत्यंत उन्नत था।"),
    ("केस स्टडी: राजस्थान की खेतड़ी खानों के तांबा स्रोत का विश्लेषण। हड़प्पा राज्य ने राजनीतिक नियंत्रण के बिना कच्चे माल का प्रबंधन कैसे किया?", "स्थानीय गणेशवार-जोधपुरा ताम्रपाषाण संस्कृति के साथ व्यापारिक नेटवर्क के माध्यम से, जहाँ कृषि अधिशेष और तैयार उपकरणों के बदले तांबे की सिल्लियाँ ली जाती थीं।"),
    ("केस स्टडी: मिस्र की विशाल मूर्तियों के साथ हड़प्पा की पाषाण मूर्तियों की तुलना करें। हड़प्पा के शिल्पों का आकार इतना छोटा (20 सेमी से कम) क्यों है?", "यह एक व्यापारिक और नागरिक समाज को दर्शाता है जिसने राजसी प्रदर्शन के बजाय घरेलू उपयोग, व्यक्तिगत आभूषणों और पोर्टेबल लोक कला को प्राथमिकता दी।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the 'Lost-Wax Casting' method to a student using a step-by-step model.", "Imagine making a toy out of wax. Cover it in mud and let it dry. Poke a hole in the mud and heat it over fire; the wax melts and flows out like water. Now pour melted bronze into that hollow mud shape. Let it cool, break the mud shell, and your metal toy is ready."),
    ("Explain the concept of 'Bronze Age Metallurgy' and why alloying copper with tin was important.", "Pure copper is relatively soft and bends easily under pressure. By mixing copper with tin to create the alloy bronze, metal smiths produced tools and weapons that were significantly harder and sharper, advancing agriculture and construction."),
    ("Explain the cultural meaning behind 'Mother Goddess Terracotta Figurines'.", "These figurines were hand-modeled female figures with elaborate headdresses, believed to represent fertility, birth, and nature. They were worshiped in common households, indicating the presence of domestic religious rituals.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को चरण-दर-चरण 'लुप्त-मोम ढलाई' (Lost-Wax Casting) की अवधारणा समझाएं।", "कल्पना करें कि आपने मोम का खिलौना बनाया। उस पर गीली मिट्टी लपेट कर सुखा लिया। उसमें एक छोटा छेद करके आग पर गर्म किया; मोम पिघलकर बाहर निकल गया। अब उस खाली सांचे में पिघला कांसा भर दिया। ठंडा होने पर मिट्टी तोड़ दी, और कांसे का खिलौना तैयार है।"),
    ("कांस्य युगीन धातुकर्म (Bronze Age Metallurgy) की अवधारणा समझाएं और तांबे में टिन मिलाना क्यों महत्वपूर्ण था।", "शुद्ध तांबा अपेक्षाकृत नरम होता है और दवाब में आसानी से मुड़ जाता है। तांबे में टिन मिलाकर मिश्र धातु कांसा (bronze) बनाने से, औजार बहुत अधिक कठोर और धारदार बनते थे, जिससे खेती और भवन निर्माण में सहायता मिली।"),
    ("मिट्टी की 'मातृदेवी की मूर्तियों' (Mother Goddess Terracotta Figurines) का सांस्कृतिक महत्व समझाएं।", "ये मूर्तियां हाथ से बनी महिला आकृतियां थीं जिन पर भारी हीरे-जवाहरात और मुकुट बने थे। इन्हें उर्वरता, शिशु-जन्म और प्रकृति का प्रतीक माना जाता था और घरों में पूजा जाता था, जो घरेलू धार्मिक अनुष्ठान दर्शाते हैं।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 2 Mastery questions populated: {len(s2_mastery_eng)} (Eng), {len(s2_mastery_hin)} (Hin)")

# =========================================================================
# SECTION 3: POTTERY TRADITIONS, SEAL CARVING & BRICKS
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("What was the highly standardized dimensional ratio (length:width:thickness) maintained by Harappan bricks?", ["4:2:1", "3:2:1", "5:3:1", "2:1:1"], 0, "All Mature Harappan bricks (baked or dried) adhered to a strict 4:2:1 ratio."),
    ("The most characteristic style of painted Harappan pottery is:", ["Painted black-on-red ware", "Ochre colored pottery (OCP)", "Northern Black Polished ware (NBPW)", "Painted grey ware (PGW)"], 0, "Painted black-on-red ware is the signature ceramic tradition of the Indus Civilisation."),
    ("What stone material was utilized to manufacture standardized cubic weights?", ["Chert", "Steatite", "Lapis Lazuli", "Basalt"], 0, "Cubical commercial weights were manufactured from high-quality chert stone."),
    ("The perforated pottery jars discovered in Indus cities were characterized by:", ["Circular holes all over the body except the base", "A single large hole at the bottom", "Elaborate narrative gold reliefs", "Square stamps of the royal dynasty"], 0, "Perforated jars featured small circular holes throughout the body, likely for straining beer or liquids."),
    ("What did scribes do to steatite seals after carving to make them durable and white?", ["Baked them in high-temperature kilns", "Coated them with liquid gold foil", "Dipped them in lead oxide glaze", "Polished them with Rohri chert powder"], 0, "Steatite seals were baked in kilns to whiten, harden, and glaze the soft talc stone.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा की ईंटों में लंबाई, चौड़ाई और मोटाई का कौन सा मानकीकृत अनुपात बनाए रखा गया था?", ["4:2:1", "3:2:1", "5:3:1", "2:1:1"], 0, "सभी परिपक्व हड़प्पा ईंटों (चाहे पकी हों या सूखी) में 4:2:1 का सख्त अनुपात था।"),
    ("हड़प्पा के चित्रित मृदभांड (pottery) की सबसे विशिष्ट शैली कौन सी है?", ["लाल सतह पर काले रंग के चित्रित बर्तन (black-on-red ware)", "गेरूए रंग के मृदभांड (OCP)", "उत्तरी काली चमकीली पॉलिश वाले बर्तन (NBPW)", "चित्रित धूसर मृदभांड (PGW)"], 0, "लाल सतह पर काले रंग से रंगे बर्तन (black-on-red ware) हड़प्पा की हस्ताक्षर मृदभांड परंपरा है।"),
    ("मानकीकृत चौकोर बाटों (commercial weights) के निर्माण के लिए किस पत्थर का उपयोग किया जाता था?", ["चर्ट (Chert)", "सेलखड़ी (Steatite)", "लाजवर्द (Lapis)", "बेसाल्ट (Basalt)"], 0, "व्यापारिक बाटों के निर्माण के लिए उच्च गुणवत्ता वाले कठोर चर्ट पत्थर का उपयोग किया जाता था।"),
    ("सिंधु शहरों में पाए जाने वाले छिद्रित मिट्टी के बर्तनों (perforated jars) की क्या विशेषता थी?", ["तलवे को छोड़कर पूरे शरीर पर गोल-गोल सुराख होना", "तलवे में एक बड़ा छेद होना", "सोने के पानी वाली नक्काशी होना", "शाही राजवंश की चौकोर मुहरें होना"], 0, "छिद्रित जारों में तलवे को छोड़कर पूरे बर्तन पर छोटे-छोटे छेद होते थे, जो पेय छानने के काम आते थे।"),
    ("तराशने के बाद सेलखड़ी की मुहरों को कठोर और सफेद बनाने के लिए लेखक क्या करते थे?", ["उन्हें उच्च तापमान वाली भट्टी में पकाते थे", "उन पर सोने के वर्क की परत चढ़ाते थे", "उन्हें सीसे के घोल में डुबोते थे", "रोहरी चर्ट के पाउडर से घिसाई करते थे"], 0, "सेलखड़ी की मुहरों को तराशने के बाद भट्टी में पकाया जाता था, जिससे वे सफेद व अत्यधिक कठोर हो जाती थीं।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following designs are commonly painted on Harappan black-on-red pottery? (Select all that apply)", ["Intersecting circles", "Pipal leaf motifs", "Fish scale patterns", "Representations of horse riders"], [0, 1, 2], "Intersecting circles, pipal leaves, and fish scales were common; horses were not depicted on pottery."),
    ("Select the features of Mature Harappan brick technology: (Select all that apply)", ["Standardized 4:2:1 dimensional ratio", "Kiln-baked bricks used for drains and sewers", "Sun-dried mud bricks used for ordinary housing", "Standard size of 10 meters long for public monuments"], [0, 1, 2], "Bricks followed the 4:2:1 ratio, and were kiln-baked or sun-dried. No 10-meter bricks existed."),
    ("What are the characteristics of the standardized chert weights? (Select all that apply)", ["Cubic shapes with no markings", "Lower values followed a binary scale (1, 2, 4, 8, 16, 32...)", "Higher values transitioned to a decimal scale", "Made from soft talcose clay easily altered by merchants"], [0, 1, 2], "Weights were cubic, unmarked, and binary-decimal. They were made of hard chert, not soft clay."),
    ("Identify the types of ceramic vessels recovered from Indus sites: (Select all that apply)", ["Painted black-on-red storage jars", "Perforated jars for liquid processing", "Plain, unpainted daily utilitarian pots", "Glazed porcelain bowls imported from China"], [0, 1, 2], "Painted jars, perforated jars, and plain utilitarian pots are common; porcelain did not exist then."),
    ("Which elements were carved on square steatite seals? (Select all that apply)", ["Linguistic script characters at the top", "Exquisite animal reliefs (unicorn, bull, tiger)", "A small perforated boss on the back for threading", "Portraits of ruling kings named on the seals"], [0, 1, 2], "Seals had script, animal reliefs, and a loop/boss on the back. No portraits of kings have been found.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा के लाल और काले बर्तनों पर सामान्यतः कौन से डिज़ाइन चित्रित मिलते हैं? (सभी लागू विकल्प चुनें)", ["एक-दूसरे को काटते वृत्त", "पीपल के पत्तों की आकृतियाँ", "मछली के शल्क (scales) का डिज़ाइन", "घोड़े के सवारों के चित्र"], [0, 1, 2], "बर्तनों पर वृत्त, पीपल के पत्ते और मछली के शल्क आम थे; बर्तनों पर घोड़ों के चित्र नहीं मिले हैं।"),
    ("परिपक्व हड़प्पा ईंट निर्माण तकनीक के लक्षणों का चयन करें: (सभी लागू विकल्प चुनें)", ["4:2:1 का मानकीकृत आकार अनुपात", "नालियों और सीवरों के लिए भट्टी में पकी ईंटें", "साधारण घरों के लिए धूप में सुखाई गई मिट्टी की ईंटें", "सार्वजनिक स्मारकों के लिए 10 मीटर लंबी ईंटें"], [0, 1, 2], "ईंटें 4:2:1 अनुपात में थीं, और पक्की या सूखी प्रयुक्त होती थीं। 10 मीटर की ईंटें नहीं थीं।"),
    ("मानकीकृत चर्ट बाटों (weights) की विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["बिना किसी निशान वाले चौकोर घन आकार", "कम वजन वाले मानों में द्वि-आधारी श्रृंखला (1, 2, 4, 8, 16...)", "अधिक वजन वाले मानों में दशमलव प्रणाली का प्रयोग", "नरम मिट्टी से बने बाट जिन्हें व्यापारी आसानी से घिस सकते थे"], [0, 1, 2], "बाट चौकोर, अचिह्नित और द्वि-आधारी/दशमलव वाले थे। वे कठोर चर्ट के होते थे, नरम मिट्टी के नहीं।"),
    ("सिंधु स्थलों से प्राप्त मिट्टी के बर्तनों के प्रकारों की पहचान करें: (सभी लागू विकल्प चुनें)", ["लाल और काले रंग के बड़े भंडारण जार", "पेय छानने के लिए छिद्रित जार", "साधारण, बिना चित्रकारी वाले दैनिक उपयोग के बर्तन", "चीन से आयातित शीशेदार चीनी मिट्टी (porcelain) के कटोरे"], [0, 1, 2], "भंडारण जार, छिद्रित जार और साधारण बर्तन प्रयुक्त होते थे; चीनी मिट्टी (porcelain) का आविष्कार तब नहीं हुआ था।"),
    ("सेलखड़ी की चौकोर मुहरों पर कौन से तत्व उकेरे जाते थे? (सभी लागू विकल्प चुनें)", ["ऊपरी हिस्से में खोदे गए लिपि चिन्ह", "जानवरों के सुंदर चित्र (एक सींग वाला सांड, बैल, बाघ)", "पीछे की तरफ धागा डालने के लिए छेद वाला उठा हुआ बटन (boss)", "मुहरों पर नाम सहित शासक राजाओं के चित्र"], [0, 1, 2], "मुहरों पर लेख, पशु चित्र और पीछे धागे का बटन होता था। राजाओं के चित्र नहीं मिले हैं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("All Harappan bricks were made using standardized wooden molds to ensure uniform ratios.", True, "True. The uniformity of ratios proves wooden molds were used."),
    ("The standard brick ratio of 4:2:1 stands for Length : Width : Thickness.", True, "True. Standard dimensions like 28 × 14 × 7 cm maintain this ratio."),
    ("Perforated jars had holes only on the base, serving as flower pots.", False, "False. They had small holes all over the body, likely for straining beer or liquids."),
    ("Standard commercial weights were made of soft steatite so they could be adjusted easily.", False, "False. Weights were made of hard chert to prevent wearing out and cheating."),
    ("Plain, unpainted utilitarian pottery was far more common than decorated painted ware in daily life.", True, "True. Utilitarian plain pots constitute over 90% of the pottery corpus."),
    ("Seals were painted with deep red slip before being stamped on clay packages.", False, "False. Seals were pressed directly into wet clay sealings without paint."),
    ("The lower weights followed a binary progression, while higher units followed decimal progression.", True, "True. Scribes used binary (1, 2, 4, 8, 16...) and decimal systems."),
    ("Kiln-baked bricks were preferred over sun-dried bricks for building public sewers and bathing tanks.", True, "True. Baked bricks resisted water erosion in drainage structures.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("एक समान आकार अनुपात सुनिश्चित करने के लिए सभी हड़प्पा ईंटें मानकीकृत लकड़ी के सांचों से बनाई जाती थीं।", True, "सत्य। ईंटों की एकरूपता लकड़ी के सांचों (wooden molds) के उपयोग को सिद्ध करती है।"),
    ("ईंटों का मानक अनुपात 4:2:1 लंबाई : चौड़ाई : मोटाई को दर्शाता है।", True, "सत्य। मानक आकार जैसे 28 × 14 × 7 सेमी इसी अनुपात में थे।"),
    ("छिद्रित जारों में केवल तलवे में छेद होते थे, और इनका उपयोग गमलों के रूप में होता था।", False, "असत्य। इनमें पूरे बर्तन पर छेद होते थे, जो पेय छानने के काम आते थे।"),
    ("व्यापारिक बाट नरम सेलखड़ी के बने होते थे ताकि आवश्यकतानुसार उनका वजन बदला जा सके।", False, "असत्य। बाट कठोर चर्ट के होते थे ताकि घर्षण से उनका वजन न घटे और धोखाधड़ी न हो।"),
    ("दैनिक जीवन में चित्रकारी वाले बर्तनों की तुलना में बिना चित्र वाले सादे बर्तन अधिक आम थे।", True, "सत्य। सादे बर्तन कुल बर्तनों का 90% से अधिक हैं।"),
    ("मिट्टी के पैकेजों पर छाप लगाने से पहले मुहरों को गहरे लाल रंग में रंगा जाता था।", False, "असत्य। मुहरों को बिना किसी रंग के सीधे गीली मिट्टी पर दबाया जाता था।"),
    ("कम वजन वाले बाट द्वि-आधारी श्रेणी में थे, जबकि भारी बाट दशमलव श्रेणी में थे।", True, "सत्य। बाटों में द्वि-आधारी (binary) और दशमलव दोनों प्रणालियों का मिश्रण था।"),
    ("सार्वजनिक नालियों और स्नान गृहों के निर्माण के लिए पक्की ईंटों को सूखी ईंटों की तुलना में प्राथमिकता दी जाती थी।", True, "सत्य। पक्की ईंटें पानी के संपर्क में आने पर गलती नहीं थीं।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The standardized dimensional ratio of Mature Harappan bricks (L:W:T) was ___________.", "4:2:1", "All bricks adhered to the 4:2:1 ratio."),
    ("The primary pottery style of the Indus Civilisation is painted ___________ ware.", "black-on-red", "Painted black-on-red ware is the dominant ceramic style."),
    ("Clay jars containing multiple small holes all over their body are known as ___________ jars.", "perforated", "Perforated jars feature holes across the body."),
    ("Cubic commercial weights were manufactured from a highly durable stone called ___________.", "chert", "Chert was the preferred hard stone for weights."),
    ("The binary scale of weights progressed as 1, 2, 4, 8, ___________, and so on.", "16", "The binary series doubles at each step (1, 2, 4, 8, 16...)."),
    ("Bricks exposed directly to water in sewers and bathing tanks were ___________-baked.", "kiln", "Kiln-baked bricks were used for drains."),
    ("Square steatite seals carried animal reliefs accompanied by ___________ symbols at the top.", "script", "Script symbols accompanied animal figures on seals."),
    ("Standard Harappan ceramics were thrown on the potter's ___________.", "wheel", "Wheel-made pottery was the norm.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("परिपक्व हड़प्पा ईंटों का लंबाई : चौड़ाई : मोटाई का मानकीकृत अनुपात ___________ था।", "4:2:1", "सभी ईंटें 4:2:1 के अनुपात में बनाई जाती थीं।"),
    ("सिंधु सभ्यता के चित्रित मृदभांडों की प्राथमिक शैली ___________ मृदभांड थी।", "लाल और काले", "लाल पृष्ठभूमि पर काली चित्रकारी (black-on-red) मुख्य शैली थी।"),
    ("मिट्टी के जिन बर्तनों पर पूरे शरीर पर छोटे-छोटे छेद होते थे, उन्हें ___________ जार कहा जाता था।", "छिद्रित", "इन्हें छिद्रित जार (perforated jars) कहा जाता था।"),
    ("चौकोर व्यापारिक बाटों का निर्माण एक अत्यधिक टिकाऊ पत्थर से होता था जिसे ___________ कहते थे।", "चर्ट", "चर्ट (chert) पत्थर बाट बनाने में प्रयुक्त होता था।"),
    ("बाटों की द्वि-आधारी श्रृंखला 1, 2, 4, 8, ___________ आदि के रूप में आगे बढ़ती थी।", "16", "द्वि-आधारी श्रृंखला प्रत्येक चरण में दुगुनी होती थी (1, 2, 4, 8, 16...)।"),
    ("नालियों और स्नान कुंडों में पानी के संपर्क में आने वाली ईंटें ___________ में पकाई जाती थीं।", "भट्टी", "पानी प्रतिरोधी बनाने के लिए उन्हें भट्टी (kiln) में पकाया जाता था।"),
    ("सेलखड़ी की वर्गाकार मुहरों पर पशु चित्रों के साथ ऊपरी हिस्से में ___________ के अक्षर अंकित थे।", "लिपि", "मुहरों पर पशु चित्रों के साथ सिंधु लिपि (script) अंकित होती थी।"),
    ("मानक हड़प्पा बर्तनों का निर्माण कुम्हार के ___________ पर किया जाता था।", "चाक", "हड़प्पा के अधिकांश बर्तन चाक (potter's wheel) पर बनाए जाते थे।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the craft items with their standardized ratios or materials:",
        "items": [{"left": "I. Standard Bricks", "key": "A"}, {"left": "II. Commercial Weights", "key": "B"}, {"left": "III. Stamped Seals", "key": "C"}],
        "options": [{"val": "A", "text": "A. Strict 4:2:1 dimension ratio"}, {"val": "B", "text": "B. Cubical cut Rohri chert stone"}, {"val": "C", "text": "C. Kiln-fired glazed steatite soapstone"}],
        "sol": "Bricks have 4:2:1 ratio, weights are chert, and seals are steatite."
    },
    {
        "type": "Match the Following",
        "q": "Match the pottery types with their estimated usage:",
        "items": [{"left": "I. Perforated Jars", "key": "A"}, {"left": "II. Black-on-Red Ware", "key": "B"}, {"left": "III. Miniature Pots", "key": "C"}],
        "options": [{"val": "A", "text": "A. Straining fermented beverages or beer"}, {"val": "B", "text": "B. Liquid storage and ritual ceremonies"}, {"val": "C", "text": "C. Storing luxury perfumes and cosmetics"}],
        "sol": "Perforated jars strain beer, black-on-red is for storage/ritual, and miniature pots hold cosmetics."
    },
    {
        "type": "Match the Following",
        "q": "Match the weight scales with their mathematical systems:",
        "items": [{"left": "I. Lower weight units (1, 2, 4, 8, 16)", "key": "A"}, {"left": "II. Higher weight units (100, 200, 500)", "key": "B"}, {"left": "III. Base commercial weight (13.63 grams)", "key": "C"}],
        "options": [{"val": "A", "text": "A. Binary doubling progression"}, {"val": "B", "text": "B. Decimal multiples system"}, {"val": "C", "text": "C. Unit value equivalent to ratio mark 16"}],
        "sol": "Lower units are binary, higher units decimal, and base weight matches ratio unit 16."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "शिल्प वस्तुओं को उनके मानकों या सामग्रियों से सुमेलित करें:",
        "items": [{"left": "I. मानक ईंटें", "key": "A"}, {"left": "II. व्यापारिक बाट", "key": "B"}, {"left": "III. अंकित मुहरें", "key": "C"}],
        "options": [{"val": "A", "text": "A. 4:2:1 का निश्चित आकार अनुपात"}, {"val": "B", "text": "B. घनीकृत रूप में कटा चर्ट पत्थर"}, {"val": "C", "text": "C. भट्टी में पकाया गया सेलखड़ी (soapstone)"}],
        "sol": "ईंटें 4:2:1 अनुपात में थीं, बाट चर्ट के थे, और मुहरें सेलखड़ी की थीं।"
    },
    {
        "type": "Match the Following",
        "q": "मिट्टी के बर्तनों को उनके संभावित उपयोगों से सुमेलित करें:",
        "items": [{"left": "I. छिद्रित जार", "key": "A"}, {"left": "II. लाल और काले बर्तन", "key": "B"}, {"left": "III. लघु (Miniature) पात्र", "key": "C"}],
        "options": [{"val": "A", "text": "A. नशीले पेय या बीयर छानने के लिए"}, {"val": "B", "text": "B. अनाज/जल भंडारण और उत्सवों में"}, {"val": "C", "text": "C. इत्र और सौंदर्य प्रसाधनों को रखने के लिए"}],
        "sol": "छिद्रित जार पेय छानने के लिए, लाल व काले बर्तन भंडारण के लिए, और लघु पात्र इत्र के लिए प्रयुक्त होते थे।"
    },
    {
        "type": "Match the Following",
        "q": "बाटों की माप प्रणालियों को उनके गणितीय मानों से सुमेलित करें:",
        "items": [{"left": "I. कम वजन मान (1, 2, 4, 8, 16)", "key": "A"}, {"left": "II. उच्च वजन मान (100, 200, 500)", "key": "B"}, {"left": "III. आधार व्यापारिक बाट (13.63 ग्राम)", "key": "C"}],
        "options": [{"val": "A", "text": "A. द्वि-आधारी (binary) गुणन प्रणाली"}, {"val": "B", "text": "B. दशमलव गुणन प्रणाली"}, {"val": "C", "text": "C. अनुपात प्रणाली के अंक 16 के समतुल्य मान"}],
        "sol": "कम वजन द्वि-आधारी है, उच्च वजन दशमलव है, और आधार बाट अंक 16 के समतुल्य है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the standard ratio of length, width, and thickness of Harappan bricks?", "4:2:1."),
    ("Which stone was cut and polished to form standardized cubical weights?", "Chert."),
    ("What was the primary function of perforated clay jars?", "To strain fermented liquids/beer or burn incense."),
    ("What motifs are most common on painted black-on-red pottery?", "Geometric intersecting circles, pipal leaves, and fish scales."),
    ("What is the base weight unit of the binary scale?", "Approximately 13.63 grams (equivalent to unit 16)."),
    ("Where were kiln-baked bricks preferred over sun-dried bricks?", "In public sewers, drains, and Citadel foundations."),
    ("What feature on the back of seals allowed them to be threaded and carried?", "A small pierced boss or button."),
    ("Were Harappan pottery vessels hand-built or wheel-thrown?", "Wheel-thrown.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा ईंटों की लंबाई, चौड़ाई और मोटाई का मानक अनुपात क्या है?", "4:2:1।"),
    ("मानकीकृत चौकोर बाट बनाने के लिए किस पत्थर को काटा और चमकाया जाता था?", "चर्ट (Chert)।"),
    ("छिद्रित जारों (perforated jars) का प्राथमिक कार्य क्या माना जाता है?", "पेय पदार्थ छानना या धूप बत्ती जलाना।"),
    ("चित्रित लाल और काले बर्तनों पर सबसे आम आकृतियाँ कौन सी हैं?", "एक-दूसरे को काटते वृत्त, पीपल के पत्ते और मछली के शल्क।"),
    ("द्वि-आधारी प्रणाली में आधार वजन इकाई क्या थी?", "लगभग 13.63 ग्राम (इकाई मान 16 के बराबर)।"),
    ("धूप में सुखाई ईंटों की तुलना में पक्की ईंटों का उपयोग कहाँ अधिक होता था?", "सार्वजनिक नालियों, सीवरों और किले के चबूतरे की नींव में।"),
    ("मुहरों के पीछे धागा पिरोने के लिए क्या बना होता था?", "एक छोटा उठा हुआ बटन (boss) जिसमें छेद होता था।"),
    ("क्या हड़प्पा के बर्तन हाथ से बने थे या कुम्हार के चाक पर?", "चाक पर बने (wheel-thrown) थे।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Kiln-baked bricks were used to line drains and sewers.\nReason (R): Baked bricks are water-resistant and do not erode or dissolve when exposed to moisture.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappan weights were highly standardized across all sites.\nReason (R): Weights were made of soft talc, allowing merchants to scrape and adjust them easily.", 2, "A is true but R is false (weights were made of hard chert, not soft talc, to prevent wear and cheating)."),
    ("Assertion (A): Painted black-on-red pottery was the only ceramic type manufactured.\nReason (R): Over 90% of excavated pottery consists of plain, unpainted utilitarian ware.", 3, "A is false because plain pottery was far more common. R is true."),
    ("Assertion (A): The brick ratio of 4:2:1 was maintained across all Mature Harappan sites.\nReason (R): Builders utilized standardized wooden molds and municipal rules to ensure uniformity.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Perforated jars were used as oil lamps.\nReason (R): They contain circular perforations all over the body to release heat or strain liquids.", 3, "A is false. R is true and explains the physical shape of perforated jars."),
    ("Assertion (A): Steatite seals were fired in ovens after carving.\nReason (R): Firing steatite creates a white glazed surface and increases the hardness of the soapstone.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The lower weights followed a binary progression.\nReason (R): Scribes used a progression of 1, 2, 4, 8, 16, 32, 64.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Seals were painted with elaborate scenes of battle.\nReason (R): Scribes carved a single animal relief and a short script inscription on square seals.", 3, "A is false because seals carried animals/script without battle paintings. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): नालियों और सीवरों के अस्तर के लिए भट्टी में पकी ईंटों का उपयोग किया जाता था।\nकारण (R): पक्की ईंटें जल प्रतिरोधी होती हैं और पानी के संपर्क में आने पर गलती या नष्ट नहीं होती हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के बाट सभी स्थलों पर अत्यधिक मानकीकृत थे।\nकारण (R): बाट नरम साबुन-पत्थर के बने होते थे, जिससे व्यापारी आसानी से घिसकर वजन समायोजित कर सकते थे।", 2, "A सत्य है लेकिन R असत्य है (बाट कठोर चर्ट के होते थे ताकि वजन में धोखाधड़ी न की जा सके)।"),
    ("कथन (A): हड़प्पा काल में केवल लाल और काले रंग के चित्रित बर्तनों का ही निर्माण होता था।\nकारण (R): उत्खनन में मिले 90% से अधिक बर्तन साधारण, बिना चित्रकारी वाले दैनिक उपयोग के हैं।", 3, "A असत्य है क्योंकि सादे बर्तन बहुत आम थे। R सत्य है।"),
    ("कथन (A): परिपक्व हड़प्पा काल में 4:2:1 का ईंट अनुपात सभी क्षेत्रों में समान था।\nकारण (R): निर्माणकर्ता एकरूपता सुनिश्चित करने के लिए मानकीकृत लकड़ी के सांचों और नगर पालिका नियमों का उपयोग करते थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): छिद्रित जारों का उपयोग तेल के दीयों के रूप में किया जाता था।\nकारण (R): इनमें ऊष्मा बाहर निकालने या पेय छानने के लिए पूरे शरीर पर छिद्र बने होते थे।", 3, "A असत्य है। R सत्य है।"),
    ("कथन (A): सेलखड़ी की मुहरों को नक्काशी के बाद भट्टियों में पकाया जाता था।\nकारण (R): सेलखड़ी को पकाने से उसकी सतह सफेद व चमकीली हो जाती थी और पत्थर की कठोरता बढ़ जाती थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कम वजन वाले बाटों में द्वि-आधारी पद्धति का उपयोग होता था।\nकारण (R): बाटों का अनुपात 1, 2, 4, 8, 16, 32, 64 की श्रृंखला में बढ़ता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मुहरों पर युद्धों के विस्तृत दृश्यों की चित्रकारी की जाती थी।\nकारण (R): वर्गाकार मुहरों पर लेखक पशु चित्रों के साथ संक्षिप्त लिपि चिन्ह खोदते थे।", 3, "A असत्य है क्योंकि मुहरों पर युद्ध के दृश्य नहीं थे। R सत्य है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the brick ratio:\n1. The standardized ratio of Harappan bricks (L:W:T) was exactly 4:2:1.\n2. Kiln-baked bricks were used in drainage channels to resist water erosion.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing brick ratios and drain construction."),
    ("Consider the following statements regarding weights:\n1. Standard cubical weights were made from high-quality chert.\n2. Scribes adjusted weight sizes using gold leaf covers.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: weights were unmarked and unplated, with mass controlled by stone size."),
    ("Consider the following statements regarding pottery types:\n1. Plain unpainted ware was more common than painted ware.\n2. Perforated jars contain small circular holes all over the body.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing plain ware and perforated jars."),
    ("Consider the following statements regarding seals:\n1. Seals were made of soft steatite which was fired to harden.\n2. The backs of seals had spoked wheels to allow them to be rolled.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: backs of seals had a loop/boss for threading, not wheels."),
    ("Consider the following statements regarding weight systems:\n1. Scribes used a binary system for low weights.\n2. Scribes used a decimal system for higher weights.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing the binary-decimal system.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("ईंटों के अनुपात के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. हड़प्पा की ईंटों का लंबाई : चौड़ाई : मोटाई का अनुपात ठीक 4:2:1 था।\n2. पानी के कटाव को रोकने के लिए नालियों में भट्टी में पकी ईंटों का उपयोग किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो ईंट अनुपात और नालियों के निर्माण को स्पष्ट करते हैं।"),
    ("बाटों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मानक घनीय बाटों का निर्माण उच्च गुणवत्ता वाले चर्ट से होता था।\n2. लेखक सोने की परतों से बाटों के आकार को समायोजित करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि बाटों पर कोई कोटिंग नहीं की जाती थी, वजन केवल पत्थर काटकर तय होता था।"),
    ("मृदभांडों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दैनिक जीवन में सादे बर्तन चित्रित बर्तनों की तुलना में अधिक आम थे।\n2. छिद्रित जारों में पूरे शरीर पर छोटे गोल छेद बने होते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो सादे बर्तनों और छिद्रित जार की संरचना का वर्णन करते हैं।"),
    ("मुहरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरें नरम सेलखड़ी की बनती थीं जिसे पकाकर कठोर किया जाता था।\n2. मुहरों के पीछे तीलियों वाले पहिये लगे होते थे ताकि उन्हें घुमाया जा सके।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि मुहरों के पीछे धागे का छेद (boss) होता था, पहिये नहीं।"),
    ("बाट प्रणालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कम भार वाले बाटों में द्वि-आधारी पद्धति प्रयुक्त होती थी।\n2. अधिक भार वाले बाटों में दशमलव पद्धति प्रयुक्त होती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो बाटों की द्वि-आधारी व दशमलव प्रणालियों को स्पष्ट करते हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the brick ratio of 4:2:1 remain identical across all cities?", "Because of standardized wooden molds and strict municipal regulations, ensuring uniform architectural dimensions for cities separated by thousands of kilometers."),
    ("Why did builders use kiln-baked bricks in drainage structures rather than mud bricks?", "Because firing clay in kilns changes its chemical structure, making it highly water-resistant and preventing it from melting or eroding under flowing water."),
    ("Why was chert preferred for manufacturing commercial weights?", "Because chert is an extremely hard, fine-grained silica rock that does not chip or wear away easily, keeping the weights highly accurate and preventing merchant fraud.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा की ईंटों का 4:2:1 अनुपात इतने विस्तृत साम्राज्य में एक समान क्यों रहा?", "मानकीकृत लकड़ी के सांचों और सख्त नगर पालिका विनियमों के कारण, जिससे हजारों किलोमीटर दूर स्थित शहरों में भी एक समान निर्माण आकारों का पालन सुनिश्चित हुआ।"),
    ("निर्माणकर्ता नालियों में मिट्टी की ईंटों के बजाय भट्टी में पकी ईंटों का उपयोग क्यों करते थे?", "क्योंकि भट्टी में पकाने से मिट्टी की संरचना बदल जाती है, जिससे वह जल प्रतिरोधी हो जाती है और बहते पानी के संपर्क में आने पर गलती या बहती नहीं है।"),
    ("व्यापारिक बाटों के विनिर्माण के लिए चर्ट पत्थर को प्राथमिकता क्यों दी जाती थी?", "क्योंकि चर्ट अत्यंत कठोर और बारीक सिलिका पत्थर है जो आसानी से टूटता या घिसता नहीं है, जिससे बाटों का वजन सही बना रहता था और व्यापार में धोखाधड़ी नहीं होती थी।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How were Harappan bricks shaped and baked?", "Wet clay was pressed into open wooden molds with a 4:2:1 ratio, dried in the sun to solidify, and then fired in large, wood-burning brick kilns to make them durable."),
    ("How did the binary-decimal weights system progress?", "The lower values progressed as a binary doubling system (1, 2, 4, 8, 16, 32, 64) up to a value of 12,800, while the larger units transitioned to a decimal system (e.g. 100, 200, 500) for bulk trade."),
    ("How was the painted design applied to the red-and-black pottery?", "A smooth slip of red iron-rich clay was applied to the wheel-thrown pot as a glaze, geometric or floral motifs were painted on it in black manganese pigment, and the vessel was baked in a kiln.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा की ईंटों को कैसे आकार दिया जाता था और पकाया जाता था?", "गीली मिट्टी को 4:2:1 अनुपात वाले लकड़ी के सांचों में दबाया जाता था, ठोस करने के लिए धूप में सुखाया जाता था, और फिर लकड़ी से जलने वाले बड़े भट्टों (kilns) में पकाया जाता था।"),
    ("बाटों की द्वि-आधारी व दशमलव प्रणालियों का क्रम कैसे बढ़ता था?", "कम भार वाले मान द्वि-आधारी पद्धति (1, 2, 4, 8, 16, 32...) में दुगुने होते हुए 12,800 तक जाते थे, जबकि बड़े बाट दशमलव पद्धति (100, 200, 500) के अनुसार बढ़ते थे।"),
    ("लाल और काले बर्तनों पर चित्रित डिज़ाइनों को कैसे लगाया जाता था?", "चाक पर बने बर्तन पर लोहे से समृद्ध लाल गेरू का चिकना लेप चढ़ाया जाता था, उस पर काली स्याही (मैंगनीज पिगमेंट) से चित्र बनाए जाते थे और फिर उसे भट्टी में पकाया जाता था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Great Bath at Mohenjo-daro uses tightly fitted baked bricks, gypsum mortar, and a backing of bitumen. What does this engineering case study prove?", "It proves that Harappan builders possessed advanced hydraulic engineering knowledge, using baked bricks and waterproofing to prevent water leaks and ensure hygiene."),
    ("Case Study: Excavations at Mohenjo-daro yielded a set of chert cubic weights with a deviation of less than 1% from the base weight of 13.63 grams. What does this accuracy suggest about trade?", "It suggests a highly regulated trade environment with municipal commercial inspectors verifying weights to prevent fraud and maintain uniform trade standards."),
    ("Case Study: Analysis of the 'Unicorn' seal. It represents over 60% of all seals found, carrying the same animal relief and similar brief texts. What administrative role does this suggest?", "It suggests that the unicorn was the official emblem of the dominant ruling clan or merchant guild, representing centralized administrative authority in seal stampings.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: मोहनजोदड़ो के विशाल स्नानकुंड (Great Bath) में पक्की ईंटें, जिप्सम गारा और पीछे डामर (bitumen) की परत लगाई गई है। यह इंजीनियरिंग केस स्टडी क्या प्रमाणित करती है?", "यह प्रमाणित करती है कि हड़प्पा के निर्माताओं को उन्नत जल-निकासी व इंजीनियरिंग का ज्ञान था, जिन्होंने स्नानकुंड से पानी का रिसाव रोकने और स्वच्छता सुनिश्चित करने के लिए पक्की ईंटों व डामर का उपयोग किया।"),
    ("केस स्टडी: मोहनजोदड़ो में उत्खनन से मिले चर्ट के चौकोर बाटों का वजन आधार वजन 13.63 ग्राम से 1% से भी कम विचलित था। यह शुद्धता व्यापार के बारे में क्या संकेत देती है?", "यह नगर पालिका के वाणिज्यिक निरीक्षकों द्वारा बाटों की नियमित जाँच और मानकीकृत व्यापारिक नियमों की उपस्थिति दर्शाती है ताकि धोखाधड़ी को रोका जा सके।"),
    ("केस स्टडी: 'एक सींग वाले पशु' (Unicorn) वाली मुहर का विश्लेषण। यह प्राप्त सभी मुहरों का 60% से अधिक है, जिन पर एक समान पशु चित्र और संक्षिप्त लेख हैं। यह क्या प्रशासनिक भूमिका दर्शाता है?", "यह संकेत देता है कि एक सींग वाला पशु (unicorn) सिंधु घाटी के शासक वर्ग या प्रमुख व्यापारिक संघ का आधिकारिक प्रतीक चिन्ह था, जो नागरिक अधिकार को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of the '4:2:1 Brick Ratio' to a high school student.", "The ratio means the length of the brick is double the width, and the width is double the thickness (e.g. 28 × 14 × 7 cm). This specific ratio allows bricks to be laid in alternating headers and stretchers (known as the English bond), which locks them together to form extremely strong walls."),
    ("Explain the difference between the 'Binary' and 'Decimal' systems in Harappan weights.", "The binary system was used for smaller weights (1, 2, 4, 8, 16, 32...) which doubled at each step, ideal for local daily market exchanges. The decimal system was used for much larger weights (e.g. multiples of ten/hundred), designed for bulk shipping, taxation, and international trade."),
    ("Explain the difference between 'Pre-firing Stamp' and 'Post-firing Graffiti' on pottery.", "A pre-firing stamp was pressed into the wet clay at a manufacturing workshop to mark the potter's trademark before baking. Post-firing graffiti was scratched onto the finished, baked pot by individual owners using sharp stones to denote personal possession or quantity marks.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक माध्यमिक छात्र को '4:2:1 ईंट अनुपात' की अवधारणा समझाएं।", "इस अनुपात का अर्थ है कि ईंट की लंबाई उसकी चौड़ाई की दोगुनी और चौड़ाई उसकी मोटाई की दोगुनी होती है (जैसे 28 × 14 × 7 सेमी)। यह अनुपात ईंटों को एक-दूसरे के ऊपर बारी-बारी से लंबवत और समानांतर (इंग्लिश बॉन्ड) रखने की अनुमति देता है, जिससे दीवारें अत्यंत मजबूत बनती हैं।"),
    ("हड़प्पा के बाटों में 'द्वि-आधारी' (Binary) और 'दशमलव' (Decimal) प्रणालियों के अंतर को समझाएं।", "द्वि-आधारी प्रणाली छोटे बाटों (1, 2, 4, 8, 16, 32...) के लिए थी जो हर कदम पर दुगुनी होती थी, यह दैनिक घरेलू खरीद के लिए आदर्श थी। दशमलव प्रणाली बहुत बड़े बाटों (जैसे 100, 200, 500) के लिए थी, जो बड़े लदानों, करों और अंतरराष्ट्रीय व्यापार के लिए डिज़ाइन की गई थी।"),
    ("मिट्टी के बर्तनों पर 'पकाने से पहले की छाप' (Pre-firing Stamp) और 'पकाने के बाद के भित्तिचित्र' (Post-firing Graffiti) का अंतर समझाएं।", "पकाने से पहले की छाप कार्यशाला में गीली मिट्टी पर कुम्हार द्वारा अपना ट्रेडमार्क लगाने के लिए दबाई जाती थी। पकाने के बाद के भित्तिचित्र बर्तनों को भट्टी से निकालने के बाद मालिकों द्वारा नुकीले पत्थर से अपना नाम या मालिकाना हक जताने के लिए खरोंच कर बनाए जाते थे।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 3 Mastery questions populated: {len(s3_mastery_eng)} (Eng), {len(s3_mastery_hin)} (Hin)")


# =========================================================================
# WRITE BACK INJECTED DATA
# =========================================================================

# English injection
if os.path.exists(ENG_PATH):
    with open(ENG_PATH, "r", encoding="utf-8") as f:
        eng_data = json.load(f)
    
    eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
    eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
    eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng
    
    with open(ENG_PATH, "w", encoding="utf-8") as f:
        json.dump(eng_data, f, ensure_ascii=False, indent=2)
    print("English mastery injected successfully!")
else:
    print(f"Error: English file not found at {ENG_PATH}")

# Hindi injection
if os.path.exists(HIN_PATH):
    with open(HIN_PATH, "r", encoding="utf-8") as f:
        hin_data = json.load(f)
    
    hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin
    hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin
    hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin
    
    with open(HIN_PATH, "w", encoding="utf-8") as f:
        json.dump(hin_data, f, ensure_ascii=False, indent=2)
    print("Hindi mastery injected successfully!")
else:
    print(f"Error: Hindi file not found at {HIN_PATH}")
