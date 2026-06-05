import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Town-Planning\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Town-Planning\hi\content.json"

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
# SECTION 1: GRID IRON STREETS, CITADELS & LOWER TOWNS
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which feature of Harappan streets was designed to facilitate natural cleansing by prevailing winds?", ["Cardinal alignment (North-South, East-West)", "Paving with baked bricks", "Steep downward slope", "Deep drainage channels on both sides"], 0, "Streets were aligned along cardinal directions so winds blowing through them would sweep away dust naturally."),
    ("Which mature Harappan site is characterized by radial street layouts instead of the typical grid iron pattern?", ["Banawali", "Mohenjo-daro", "Harappa", "Kalibangan"], 0, "Banawali in Haryana deviates from the grid plan, featuring roads that radiate from the citadel."),
    ("Which Harappan city represents a unique three-tier urban division consisting of a Citadel, Middle Town, and Lower Town?", ["Dholavira", "Lothal", "Surkotada", "Chanhudaro"], 0, "Dholavira is uniquely divided into three fortified zones, whereas most other cities had a dual-sector division."),
    ("Which major Indus Valley settlement in Sindh is notable for completely lacking a fortified citadel mound?", ["Chanhudaro", "Mohenjo-daro", "Amri", "Kot Diji"], 0, "Chanhudaro was an unfortified craft-producing center that did not feature a raised citadel mound."),
    ("At which site was the Citadel separated from the Lower Town by a mud-brick wall but built on the same flat level?", ["Lothal", "Surkotada", "Kalibangan", "Harappa"], 0, "Lothal's Citadel was not raised on a high mound but was built at the same elevation, separated by an internal mud-brick wall.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("सड़कों की धूल को हवा द्वारा स्वतः साफ करने के लिए हड़प्पा वासियों ने सड़कों का कैसा नियोजन किया था?", ["दिशा संरेखण (उत्तर-दक्षिण, पूर्व-पश्चिम)", "पकी ईंटों से पक्की करना", "तेज ढलान देना", "दोनों तरफ गहरी नालियां बनाना"], 0, "सड़कों को उत्तर-दक्षिण और पूर्व-पश्चिम दिशाओं में संरेखित किया गया था ताकि बहने वाली हवाएं धूल को स्वतः उड़ा ले जाएं।"),
    ("किस हड़प्पा स्थल पर ग्रिड प्रणाली के बजाय अरीय (radial) सड़कों का नियोजन मिला है?", ["बनावली", "मोहनजोदड़ो", "हड़प्पा", "कालीबंगन"], 0, "हरियाणा के बनावली में सड़कें ग्रिड प्रणाली के बजाय किले से बाहर की ओर अरीय (radial) प्रतिरूप में व्यवस्थित मिली हैं।"),
    ("कौन सा हड़प्पा शहर किला, मध्य नगर और निचले नगर के रूप में त्रि-स्तरीय विभाजन को दर्शाता है?", ["धोलावीरा", "लोथल", "सुरकोटदा", "चन्हुदड़ो"], 0, "धोलावीरा तीन अलग-अलग किलेबंद नगर क्षेत्रों में विभाजित है, जबकि अन्य में दो भागों का विभाजन था।"),
    ("सिंध में स्थित कौन सा प्रमुख हड़प्पा स्थल है जिसमें कोई सुरक्षात्मक किला (citadel) नहीं मिला है?", ["चन्हुदड़ो", "मोहनजोदड़ो", "आमरी", "कोटदीजी"], 0, "चन्हुदड़ो एक शिल्प उत्पादन केंद्र था जिसमें कोई ऊँचा किला नहीं बनाया गया था।"),
    ("किस स्थल पर किला निचले नगर से अलग तो था, लेकिन किसी ऊंचे टीले के बजाय समान समतल स्तर पर बना था?", ["लोथल", "सुरकोटदा", "कालीबंगन", "हड़प्पा"], 0, "लोथल का किला निचले नगर के समान स्तर पर बना था और उसे केवल एक आंतरिक कच्ची ईंट की दीवार से विभाजित किया गया था।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which features are associated with the layout of Dholavira? (Select all that apply)", ["Three-tier fortified division", "Use of dressed limestone for fortifications", "Massive stone check dams and reservoirs", "A radial street grid pattern"], [0, 1, 2], "Dholavira has 3 tiers, stone walls, and dams. Its streets follow a grid, not radial layouts (radial is Banawali)."),
    ("Select the unique characteristics of the site of Banawali: (Select all that apply)", ["Radial streets radiating from the citadel", "Irrational non-grid town layout", "Lack of systematic public drainage", "A massive brick-lined dockyard"], [0, 1, 2], "Banawali has radial streets, a non-grid layout, and poor drainage. The dockyard is located at Lothal."),
    ("Which elements characterize the Citadel mound in Harappan cities? (Select all that apply)", ["Located on the western side of the settlement", "Raised on massive mud-brick platforms", "Housed administrative and public assembly buildings", "Reserved primarily for low-income artisans"], [0, 1, 2], "Citadels lay in the west, on raised platforms, housing public monuments. Artisans lived in the Lower Town."),
    ("What was the primary function of Harappan city fortification walls? (Select all that apply)", ["Defense against human adversaries", "Protection from river floods", "Regulation of trade and collection of customs", "Religious isolation of priest classes"], [0, 1, 2], "Walls served defense, flood prevention, and trade/tax regulation. There is no evidence of priestly isolation."),
    ("Select the sites that display a dual-fortified structure where the Citadel and Lower Town were fortified separately: (Select all that apply)", ["Kalibangan", "Surkotada", "Harappa", "Chanhudaro"], [0, 2], "Kalibangan and Harappa had separately fortified sectors. Surkotada had a unified wall enclosing both. Chanhudaro lacked walls entirely.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("धोलावीरा के नगर नियोजन से जुड़े कौन से लक्षण हैं? (सभी लागू विकल्प चुनें)", ["त्रि-स्तरीय किलेबंद विभाजन", "किलेबंदी के लिए तराशे गए पत्थरों का उपयोग", "विशाल जलाशय और चेक डैम", "सड़कों का अरीय (radial) ढांचा"], [0, 1, 2], "धोलावीरा में 3 स्तर, पत्थर की दीवारें और जलाशय मिले हैं। यहाँ ग्रिड पैटर्न था, अरीय नहीं (अरीय बनावली में था)।"),
    ("बनावली स्थल की अनूठी विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["किले के टीले से बाहर की ओर अरीय सड़कें", "अनियमित और गैर-ग्रिड शहरी व्यवस्था", "व्यवस्थित सार्वजनिक सीवर प्रणाली का अभाव", "ईंटों से निर्मित विशाल गोदी बाड़ा (dockyard)"], [0, 1, 2], "बनावली में अरीय सड़कें, गैर-ग्रिड लेआउट और कमजोर जल निकासी थी। गोदी बाड़ा लोथल में स्थित है।"),
    ("हड़प्पा शहरों में किले (Citadel) के टीले को कौन से तत्व रेखांकित करते हैं? (सभी लागू विकल्प चुनें)", ["शहर के पश्चिमी भाग में स्थित होना", "मिट्टी की ईंटों के विशाल चबूतरे पर निर्मित होना", "प्रशासनिक और सार्वजनिक भवनों का होना", "मुख्य रूप से गरीब कारीगरों का निवास क्षेत्र होना"], [0, 1, 2], "किला पश्चिम में चबूतरे पर था और उसमें सार्वजनिक भवन थे। कारीगर निचले नगर में रहते थे।"),
    ("हड़प्पा नगरों की रक्षा दीवारों (fortification) का मुख्य कार्य क्या था? (सभी लागू विकल्प चुनें)", ["बाहरी शत्रुओं से सुरक्षा", "नदी की बाढ़ से बचाव", "व्यापार नियंत्रण और चुंगी कर की वसूली", "पुरोहित वर्ग को धार्मिक रूप से अलग रखना"], [0, 1, 2], "दीवारें रक्षा, बाढ़ नियंत्रण और चुंगी कर के लिए थीं। धार्मिक अलगाव का कोई पुरातात्विक साक्ष्य नहीं है।"),
    ("उन स्थलों का चयन करें जहाँ किला और निचला नगर दोनों अलग-अलग प्राचीर से घिरे हुए थे: (सभी लागू विकल्प चुनें)", ["कालीबंगन", "सुरकोटदा", "हड़प्पा", "चन्हुदड़ो"], [0, 2], "कालीबंगन और हड़प्पा में किला और आवासीय क्षेत्र अलग-अलग प्राचीर से घिरे थे। सुरकोटदा में साझी दीवार थी, और चन्हुदड़ो में प्राचीर थी ही नहीं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Banawali featured streets that crossed at exact right angles forming a perfect grid.", False, "False. Banawali featured a radial pattern with irregular roads."),
    ("Chanhudaro was surrounded by a massive stone defensive wall over 5 meters thick.", False, "False. Chanhudaro is the only major site that completely lacked fortifications."),
    ("Dholavira is situated in the Kutch region of Gujarat and has three fortified sectors.", True, "True. Dholavira in Kutch is divided into a Citadel, Middle Town, and Lower Town."),
    ("Harappan main avenues were aligned North-South and East-West to utilize winds for cleaning.", True, "True. The cardinal alignment allowed prevailing winds to naturally blow dust off streets."),
    ("The fortifications at Dholavira utilized local dressed limestone rubble.", True, "True. Dholavira used local dressed limestone rather than baked bricks for fortifications."),
    ("Lothal's Citadel was built on a separate raised artificial mud-brick mound.", False, "False. Lothal's Citadel was on the same level, divided internally by a brick wall."),
    ("Kalibangan featured separately fortified Citadel and Lower Town sectors.", True, "True. Unlike unified wall sites, Kalibangan had separate fortification walls for both."),
    ("No Harappan city wall featured defensive gateways or watchtowers.", False, "False. Gates and watchtowers have been found at Surkotada, Dholavira, and Harappa.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("बनावली में सड़कें समकोण पर काटकर एक आदर्श ग्रिड का निर्माण करती थीं।", False, "असत्य। बनावली में अरीय और अनियमित सड़कें मिली हैं।"),
    ("चन्हुदड़ो 5 मीटर चौड़ी विशाल पत्थर की सुरक्षा दीवार से घिरा हुआ था।", False, "असत्य। चन्हुदड़ो एकमात्र ऐसा प्रमुख स्थल है जहाँ कोई भी नगर सुरक्षा दीवार नहीं मिली है।"),
    ("धोलावीरा गुजरात के कच्छ क्षेत्र में स्थित है और इसके तीन किलेबंद भाग हैं।", True, "सत्य। धोलावीरा कच्छ में है और यह किला, मध्य नगर और निचले नगर में विभाजित है।"),
    ("सड़कों को उत्तर-दक्षिण और पूर्व-पश्चिम दिशाओं में हवा से स्वतः सफाई के लिए संरेखित किया गया था।", True, "सत्य। यह दिशा संरेखण हवा के बहाव से धूल साफ करने में सहायक था।"),
    ("धोलावीरा की प्राचीर में स्थानीय तराशे गए चूना पत्थर के टुकड़ों का उपयोग हुआ था।", True, "सत्य। धोलावीरा में प्राचीर बनाने के लिए ईंटों के स्थान पर स्थानीय पत्थरों का बहुतायत से उपयोग किया गया था।"),
    ("लोथल का किला मिट्टी की ईंटों से बने एक अलग ऊंचे टीले पर स्थापित किया गया था।", False, "असत्य। लोथल का किला निचले नगर के समान धरातल स्तर पर था, जो केवल एक आंतरिक दीवार से पृथक था।"),
    ("कालीबंगन में किला और निचला नगर दोनों अलग-अलग सुरक्षा प्राचीर से घिरे हुए थे।", True, "सत्य। सुरकोटदा के साझी प्राचीर के विपरीत, कालीबंगन के दोनों भाग अलग-अलग प्राचीर से सुरक्षित थे।"),
    ("किसी भी हड़प्पा सुरक्षा दीवार में पहरेदारों के कक्ष या सुरक्षा द्वार नहीं थे।", False, "असत्य। सुरकोटदा, धोलावीरा और हड़प्पा में सुरक्षा प्रवेश द्वार और प्रहरी कक्ष मिले हैं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The mature Harappan site showing a radial street layout is __________.", "Banawali", "Banawali features radial layouts radiating from the citadel mound."),
    ("The only major Indus Valley town that lacked a fortified Citadel is __________.", "Chanhudaro", "Chanhudaro lacks a citadel and was primarily a manufacturing suburb."),
    ("Dholavira is unique because its city layout is divided into __________ distinct fortified parts.", "three", "Dholavira has three sections: Citadel, Middle Town, and Lower Town."),
    ("Typical Harappan streets crossed each other at __________ angles.", "right", "Avenues crossed at 90-degree right angles, creating a grid."),
    ("Street alignments let prevailing __________ naturally sweep away dust.", "winds", "Winds blowing through cardinal streets acted as a natural vacuum."),
    ("The Citadel mound was typically positioned in the __________ part of the city.", "western", "Citadels lay to the west, representing administrative authority."),
    ("Commoners, merchants, and artisans lived in the sector known as the __________.", "Lower Town", "The Lower Town in the east was the general residential zone."),
    ("At Kalibangan, the Citadel and the Lower Town were fortified __________.", "separately", "Kalibangan features separate fortifications for both sectors.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("अरीय (radial) सड़क नियोजन दर्शाने वाला परिपक्व हड़प्पा स्थल __________ है।", "बनावली", "बनावली में किले से बाहर की ओर अरीय सड़कें मिलती हैं।"),
    ("बिना किसी किले (Citadel) वाला एकमात्र प्रमुख हड़प्पा नगर __________ है।", "चन्हुदड़ो", "चन्हुदड़ो में किला नहीं था और यह मुख्य रूप से शिल्प उत्पादन क्षेत्र था।"),
    ("धोलावीरा का नगर लेआउट विशिष्ट रूप से __________ भागों में विभाजित है।", "तीन", "धोलावीरा में तीन भाग: किला, मध्य नगर और निचला नगर हैं।"),
    ("हड़प्पा की प्रमुख सड़कें एक-दूसरे को __________ कोण पर काटती थीं।", "समकोण", "सड़कें 90 डिग्री के समकोण पर कटती थीं, जिससे ग्रिड बनता था।"),
    ("सड़कों के सीधे संरेखण से बहने वाली __________ स्वतः धूल साफ कर देती थी।", "हवा", "उत्तर-दक्षिण और पूर्व-पश्चिम संरेखण से हवा धूल को साफ करती थी।"),
    ("प्रशासनिक किला (Citadel) आमतौर पर शहर के __________ दिशा में बनाया जाता था।", "पश्चिमी", "किला पश्चिम की तरफ ऊंचे चबूतरे पर प्रशासनिक कार्यों के लिए बनाया जाता था।"),
    ("आम लोगों, व्यापारियों और कारीगरों के रिहायशी क्षेत्र को __________ कहा जाता था।", "निचला नगर", "पूर्वी भाग में स्थित बड़े आवासीय क्षेत्र को निचला नगर कहते थे।"),
    ("कालीबंगन में किला और निचला नगर दोनों __________ रूप से प्राचीर से घिरे थे।", "अलग-अलग", "कालीबंगन में दोनों खंडों की अपनी अलग-अलग किलेबंदी दीवारें थीं।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their representative street layouts:",
        "items": [{"left": "I. Mohenjo-daro", "key": "A"}, {"left": "II. Banawali", "key": "B"}, {"left": "III. Chanhudaro", "key": "C"}],
        "options": [{"val": "A", "text": "A. Grid iron pattern with broad main avenues"}, {"val": "B", "text": "B. Radial streets radiating from citadel mound"}, {"val": "C", "text": "C. Irregular lanes without formal grid or citadel"}],
        "sol": "Mohenjo-daro has a standard grid, Banawali radial streets, and Chanhudaro irregular citadel-free lanes."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their urban division layouts:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Chanhudaro", "key": "B"}, {"left": "III. Surkotada", "key": "C"}],
        "options": [{"val": "A", "text": "A. Three-tier division (Citadel, Middle, Lower)"}, {"val": "B", "text": "B. Single unfortified sector with craft suburbs"}, {"val": "C", "text": "C. Dual sectors enclosed by a shared outer wall"}],
        "sol": "Dholavira is three-tier, Chanhudaro has no fortification/citadel, and Surkotada has a single shared fortification."
    },
    {
        "type": "Match the Following",
        "q": "Match the site fortifications with their materials:",
        "items": [{"left": "I. Dholavira Fortifications", "key": "A"}, {"left": "II. Harappa Citadel Wall", "key": "B"}, {"left": "III. Kalibangan Platforms", "key": "C"}],
        "options": [{"val": "A", "text": "A. Rubble and dressed local limestone blocks"}, {"val": "B", "text": "B. Mud-brick core faced with baked bricks"}, {"val": "C", "text": "C. Sun-dried clay bricks and clay plaster"}],
        "sol": "Dholavira used limestone blocks, Harappa used a mud-brick core with baked brick veneer, and Kalibangan used sun-dried clay bricks."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके प्रतिनिधि सड़क लेआउट से सुमेलित करें:",
        "items": [{"left": "I. मोहनजोदड़ो", "key": "A"}, {"left": "II. बनावली", "key": "B"}, {"left": "III. चन्हुदड़ो", "key": "C"}],
        "options": [{"val": "A", "text": "A. चौड़े मार्गों के साथ ग्रिड पैटर्न"}, {"val": "B", "text": "B. किले के टीले से निकलती अरीय सड़कें"}, {"val": "C", "text": "C. बिना किसी ग्रिड या किले के अनियमित गलियाँ"}],
        "sol": "मोहनजोदड़ो में ग्रिड सड़कों का जाल, बनावली में अरीय सड़कें, और चन्हुदड़ो में बिना किले के अनियमित गलियां मिली हैं।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके शहरी विभाजन प्रतिरूपों से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा", "key": "A"}, {"left": "II. चन्हुदड़ो", "key": "B"}, {"left": "III. सुरकोटदा", "key": "C"}],
        "options": [{"val": "A", "text": "A. त्रि-स्तरीय विभाजन (किला, मध्य नगर, निचला नगर)"}, {"val": "B", "text": "B. शिल्प उपनगरों वाला बिना सुरक्षा दीवार का एकल क्षेत्र"}, {"val": "C", "text": "C. एक ही बाहरी सुरक्षा प्राचीर से घिरे दोहरे क्षेत्र"}],
        "sol": "धोलावीरा त्रि-स्तरीय है, चन्हुदड़ो बिना किलेबंदी का शिल्प क्षेत्र है, और सुरकोटदा में दोनों भाग साझी प्राचीर से सुरक्षित हैं।"
    },
    {
        "type": "Match the Following",
        "q": "सुरक्षा दीवारों और संरचनाओं को उनके प्रयुक्त माल से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा की सुरक्षा दीवार", "key": "A"}, {"left": "II. हड़प्पा की किला दीवार", "key": "B"}, {"left": "III. कालीबंगन के चबूतरे", "key": "C"}],
        "options": [{"val": "A", "text": "A. मलबे और तराशे हुए चूना पत्थर के खंड"}, {"val": "B", "text": "B. पकी ईंटों के बाहरी आवरण वाली मिट्टी की ईंटें"}, {"val": "C", "text": "C. धूप में सुखाई गई मिट्टी की ईंटें और मिट्टी का लेप"}],
        "sol": "धोलावीरा में चूना पत्थर, हड़प्पा में पकी ईंटों के आवरण वाली मिट्टी की ईंटें, और कालीबंगन में कच्ची मिट्टी की ईंटें प्रयुक्त होती थीं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What was the unique geometric configuration of roads in Banawali?", "A radial road pattern radiating from the fortified citadel mound."),
    ("Which mature Harappan settlement is split into three separately fortified tiers?", "Dholavira in Gujarat."),
    ("Why did the Harappans align their streets strictly along cardinal directions?", "To let prevailing winds sweep the avenues clean naturally."),
    ("Which major craft-focused settlement in Sindh completely lacked a citadel?", "Chanhudaro."),
    ("Where did the administrative and public assemblies take place in Harappan towns?", "On the western raised Citadel mound."),
    ("Name the site where the Citadel and Lower Town were separately fortified.", "Kalibangan in Rajasthan."),
    ("What stone material did Dholavira use for its massive fortification walls?", "Dressed local limestone and rubble stone."),
    ("What was the structural purpose of raising Citadels on mud-brick platforms?", "To elevate them above river floods and provide an administrative vantage point.")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("बनावली में सड़कों का विशिष्ट ज्यामितीय प्रतिरूप क्या था?", "किलेबंद किले से बाहर की ओर जाती हुई अरीय (radial) सड़कों का नियोजन।"),
    ("कौन सा परिपक्व हड़प्पा स्थल तीन अलग-अलग प्राचीरयुक्त स्तरों में बंटा है?", "गुजरात में स्थित धोलावीरा।"),
    ("हड़प्पा वासियों ने सड़कों को दिशा संरेखण (cardinal alignment) में क्यों रखा?", "ताकि बहने वाली हवाएं मुख्य सड़कों की धूल को स्वतः साफ कर सकें।"),
    ("सिंध में स्थित कौन सा शिल्प केंद्र पूरी तरह से किले विहीन (citadel-free) था?", "चन्हुदड़ो।"),
    ("हड़प्पा शहरों में प्रशासनिक और सार्वजनिक सभाएं किस भाग में आयोजित होती थीं?", "पश्चिमी भाग में स्थित ऊंचे किले (Citadel) के टीले पर।"),
    ("उस स्थल का नाम बताइए जहाँ किला और निचला नगर अलग-अलग प्राचीर से घिरे थे।", "राजस्थान का कालीबंगन।"),
    ("धोलावीरा ने अपनी विशाल प्राचीर के निर्माण में किस पत्थर का उपयोग किया?", "तराशे हुए स्थानीय चूना पत्थर और पत्थर के मलबे का।"),
    ("किले के भवनों को ऊंचे मिट्टी के चबूतरे पर बनाने का ढांचागत उद्देश्य क्या था?", "उन्हें मौसमी बाढ़ से बचाना और प्रशासनिक ऊंचाई प्रदान करना।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappan main avenues crossed at right angles, forming a grid layout aligned to cardinal wind directions.\nReason (R): This grid alignment utilized winds to naturally sweep dust and keep streets clean.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Chanhudaro completely lacked a raised administrative Citadel mound.\nReason (R): It functioned primarily as a craft manufacturing suburb specializing in bead and shell industries.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Dholavira's town planning is highly distinct from other mature Harappan metropolises.\nReason (R): It features a three-tier fortified layout (Citadel, Middle Town, and Lower Town) instead of a dual layout.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Banawali represents the model example of standard Harappan grid town planning.\nReason (R): Banawali's streets radiated outwards from the citadel mound in a radial layout.", 3, "A is false because Banawali deviated from the grid. R is true."),
    ("Assertion (A): Harappans built their Citadels on massive clay and mud-brick platforms.\nReason (R): These elevated platforms protected public and administrative offices from seasonal river inundations.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Fortifications at Dholavira were built primarily of baked bricks imported from Sindh.\nReason (R): Dholavira's builders utilized locally abundant dressed limestone and rubble for fortifications.", 3, "A is false because Dholavira fortifications were stone, not imported bricks. R is true."),
    ("Assertion (A): Lothal had a high citadel mound physically separated from the Lower Town by a deep defensive moat.\nReason (R): Lothal's Citadel sat on the same level as its Lower Town, separated only by an internal mud-brick wall.", 3, "A is false because Lothal had no moat separating them. R is true."),
    ("Assertion (A): Fortification walls around Harappan towns served multiple purposes beyond defense.\nReason (R): They acted as flood protection, regulated entry of trade goods, and facilitated customs collection.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा के मुख्य मार्ग एक-दूसरे को समकोण पर काटते थे और हवा की दिशा में संरेखित थे।\nकारण (R): सड़कों का यह संरेखण हवा के बहाव का उपयोग करके धूल को स्वतः साफ करने के लिए नियोजित था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): चन्हुदड़ो में प्रशासनिक कार्यों के लिए कोई अलग से बना किला (Citadel) नहीं था।\nकारण (R): यह मुख्य रूप से मनके और शंख बनाने के उद्योगों में लगा एक शिल्प उत्पादन उपनगर था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): धोलावीरा का नगर नियोजन अन्य परिपक्व हड़प्पा महानगरों से काफी भिन्न है।\nकारण (R): इसमें दोहरे विभाजन के स्थान पर त्रि-स्तरीय किलेबंद (किला, मध्य नगर, निचला नगर) व्यवस्था मिलती है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): बनावली हड़प्पा की मानक ग्रिड योजना का सबसे उत्कृष्ट उदाहरण प्रस्तुत करता है।\nकारण (R): बनावली की सड़कें ग्रिड के बजाय किले के टीले से बाहर की ओर अरीय (radial) रूप में व्यवस्थित थीं।", 3, "A असत्य है क्योंकि बनावली ग्रिड से अलग था। R सत्य है।"),
    ("कथन (A): हड़प्पावासियों ने अपने किलों का निर्माण विशाल मिट्टी के चबूतरे पर किया।\nकारण (R): इन ऊंचे चबूतरों ने प्रशासनिक और सार्वजनिक कार्यालयों को नदियों की मौसमी बाढ़ से सुरक्षित रखा।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): धोलावीरा की प्राचीर का निर्माण मुख्य रूप से सिंध से आयातित पकी ईंटों से किया गया था।\nकारण (R): धोलावीरा के निर्माताओं ने प्राचीर के निर्माण में स्थानीय रूप से प्रचुर तराशे गए चूना पत्थरों का उपयोग किया।", 3, "A असत्य है क्योंकि धोलावीरा में पत्थर का प्रयोग हुआ, पकी ईंटों का आयात नहीं। R सत्य है।"),
    ("कथन (A): लोथल में एक ऊँचा किला था जो निचले नगर से एक गहरी सुरक्षा खाई द्वारा अलग किया गया था।\nकारण (R): लोथल का किला निचले नगर के ही समान धरातल स्तर पर था, जो केवल एक आंतरिक मिट्टी की ईंट की दीवार से विभाजित था।", 3, "A असत्य है क्योंकि वहाँ कोई सुरक्षा खाई पृथक्करण नहीं था। R सत्य है।"),
    ("कथन (A): हड़प्पा शहरों के चारों ओर बनी सुरक्षा दीवारें केवल सैन्य आक्रमण से सुरक्षा के अतिरिक्त अन्य कार्य भी करती थीं।\nकारण (R): वे बाढ़ से बचाव करती थीं, व्यापारिक वस्तुओं के प्रवेश को नियंत्रित करती थीं और चुंगी कर वसूलने में सहायक थीं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan street plans:\n1. Main avenues were constructed up to 9 meters wide to accommodate heavy traffic.\n2. Banawali is the only mature Harappan site where roads follow a radial grid pattern.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct: main streets were wide and Banawali is unique for its radial layout."),
    ("Consider the following statements regarding the site of Chanhudaro:\n1. It featured a fortified residential enclave for wealthy merchants.\n2. It is characterized by the absence of a distinct administrative citadel mound.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: Chanhudaro lacked fortification walls entirely."),
    ("Consider the following statements regarding Dholavira's city divisions:\n1. The Middle Town was fortified separately from the Citadel and Lower Town.\n2. The entire settlement was enclosed by massive limestone fortification walls.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and highlight Dholavira's unique three-tier stone fortifications."),
    ("Consider the following statements regarding Citadels:\n1. Citadels were positioned to the east of Lower Towns to capture morning sunlight.\n2. They were raised on platforms made of mud-bricks and clay silt.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: Citadels were positioned to the west, not east."),
    ("Consider the following statements regarding regional fortifying variants:\n1. At Kalibangan, both Citadel and Lower Town were fortified separately.\n2. Surkotada featured a single fortification wall enclosing both the Citadel and residential sectors.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Kalibangan's separate and Surkotada's unified fortification walls.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा के सड़क नियोजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुख्य मार्गों की चौड़ाई 9 मीटर तक होती थी ताकि गाड़ियाँ सुगमता से चल सकें।\n2. बनावली एकमात्र ऐसा परिपक्व हड़प्पा स्थल है जहाँ सड़कें अरीय (radial) प्रतिरूप का पालन करती थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं: मुख्य सड़कें चौड़ी थीं और बनावली अरीय प्रतिरूप के लिए प्रसिद्ध है।"),
    ("चन्हुदड़ो स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें समृद्ध व्यापारियों के रहने के लिए एक अलग किला क्षेत्र बनाया गया था।\n2. यह स्थल बिना किसी पृथक प्रशासनिक किले (Citadel) के टीले के पाया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि चन्हुदड़ो में सुरक्षात्मक प्राचीर या किला नहीं था।"),
    ("धोलावीरा के नगर विभाजन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मध्य नगर किले और निचले नगर से अलग रूप से किलेबंद था।\n2. पूरा शहर स्थानीय चूना पत्थर की विशाल सुरक्षा प्राचीर से घिरा हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और धोलावीरा की विशिष्ट त्रि-स्तरीय पत्थर की किलेबंदी का वर्णन करते हैं।"),
    ("किले (Citadel) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. सुबह की धूप प्राप्त करने के लिए किलों को हमेशा निचले नगर के पूर्व में बनाया जाता था।\n2. किलों का निर्माण कच्ची ईंटों और मिट्टी से बने ऊंचे चबूतरों पर किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि किलों को हमेशा पश्चिम दिशा में बनाया जाता था।"),
    ("क्षेत्रीय किलेबंदी भिन्नताओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कालीबंगन में किला और निचला नगर दोनों अलग-अलग सुरक्षा दीवारों से घिरे थे।\n2. सुरकोटदा में एक ही साझी सुरक्षा दीवार थी जिसके भीतर किला और निचला नगर दोनों समाहित थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और कालीबंगन तथा सुरकोटदा की प्राचीर भिन्नताओं को स्पष्ट करते हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Harappan architects align streets strictly along North-South and East-West directions?", "To harness prevailing winds to act as a natural sweeping mechanism, blowing dust off the avenues without manual cleaning."),
    ("Why did the industrial settlement of Chanhudaro lack a fortified citadel?", "Because it was primarily a manufacturing suburb dedicated to craft production (beads, shells) rather than an administrative seat or royal residence."),
    ("Why did Dholavira incorporate a three-tier town layout with Citadel, Middle Town, and Lower Town?", "It reflected a distinct social hierarchy and administrative structure, possibly accommodating an intermediary bureaucrat/merchant class in the Middle Town.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के वास्तुकारों ने सड़कों को उत्तर-दक्षिण और पूर्व-पश्चिम दिशाओं में ही क्यों संरेखित किया?", "बहने वाली हवाओं का उपयोग करके सड़कों की धूल को प्राकृतिक रूप से साफ करने के लिए ताकि बिना किसी मानवीय प्रयास के सफाई हो सके।"),
    ("औद्योगिक बस्ती चन्हुदड़ो में सुरक्षात्मक किला (citadel) क्यों नहीं बनाया गया था?", "क्योंकि यह मुख्य रूप से शिल्प उत्पादन (मनके, शंख) के लिए समर्पित एक औद्योगिक बस्ती थी, न कि कोई प्रशासनिक राजधानी या राजकीय मुख्यालय।"),
    ("धोलावीरा ने किला, मध्य नगर और निचले नगर की त्रि-स्तरीय योजना क्यों अपनाई?", "यह विशिष्ट सामाजिक स्तरीकरण और प्रशासनिक व्यवस्था को दर्शाता है, जिसमें मध्य नगर संभवतः मध्यस्थ प्रशासनिक अधिकारियों या व्यापारियों के रहने के लिए बना था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the grid iron street layout contribute to urban traffic management?", "By separating major broad avenues for carts from narrow domestic lanes, minimizing traffic blockages in residential zones."),
    ("How did Banawali's town planning deviate from the standard Harappan urban blueprint?", "It featured irregular radial roads rather than a grid pattern, and both citadel and lower town sat on a single mound, showing poor drainage layout."),
    ("How did fortification walls assist in the economic regulation of Harappan settlements?", "They acted as custom barriers and checkpoints, allowing administrators to inspect trade cargo, prevent smuggling, and collect taxes/tributes.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("सड़कों के ग्रिड प्रतिरूप ने शहरी यातायात प्रबंधन में कैसे सहायता की?", "इसने मालवाहक बैलगाड़ियों के लिए चौड़े मार्गों को घरों की तंग गलियों से पृथक रखा, जिससे आवासीय क्षेत्रों में भीड़-भाड़ नहीं होती थी।"),
    ("बनावली के नगर नियोजन ने मानक हड़प्पा मॉडल से किस प्रकार विचलन प्रदर्शित किया?", "यहाँ ग्रिड पैटर्न के बजाय अरीय (radial) और अनियमित सड़कें मिली हैं, और किला तथा आवासीय क्षेत्र एक ही टीले पर बने हैं जहाँ व्यवस्थित सीवरों की कमी थी।"),
    ("सुरक्षा प्राचीरों ने हड़प्पा बस्तियों के आर्थिक नियमन में कैसे मदद की?", "वे टोल गेट और प्रवेश चौकियों का काम करती थीं, जहाँ अधिकारी आने वाले व्यापारिक माल का निरीक्षण करते थे, तस्करी रोकते थे और कर वसूलते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Dholavira's Three-Tier Planning", "Located in Kutch, Dholavira represents a unique tripartite layout. The Citadel (Castle & Bailey) was fortified with massive dressed stone walls. Adjacent lay the Middle Town, housing administrative elites, and the Lower Town for the general public, proving a highly stratified administrative hierarchy."),
    ("Case Study: Chanhudaro Craft Suburb Layout", "Chanhudaro lacks any defensive walls or citadel mound. Excavations yielded bead-making factories, metal workshops, and shell-cutter tools, demonstrating that unfortified towns were integrated economic nodes whose security relied on the larger fortified capitals like Mohenjo-daro."),
    ("Case Study: Banawali's Deviant Planning", "Banawali in Haryana shows radial streets and a single mound layout. Despite having mature Harappan artifacts like toys and weights, its lack of a grid iron plan and covered brick drains demonstrates that regional capitals adapted planning designs to local topographies.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: धोलावीरा का त्रि-स्तरीय नियोजन", "कच्छ में स्थित धोलावीरा एक विशिष्ट त्रि-स्तरीय नगर योजना का प्रतिनिधित्व करता है। इसका किला (Castle and Bailey) तराशे गए पत्थरों से किलेबंद था। इसके बाद मध्य नगर था जहाँ प्रशासनिक अधिकारी रहते थे, और सबसे नीचे निचला नगर था जो आम लोगों के लिए था, जो एक संगठित प्रशासनिक व्यवस्था को दर्शाता है।"),
    ("केस स्टडी: चन्हुदड़ो शिल्प बस्ती नियोजन", "चन्हुदड़ो में सुरक्षात्मक प्राचीर या किले का अभाव था। यहाँ मनके बनाने के कारखाने और धातु कार्यशालाएँ मिली हैं, जिससे पता चलता है कि यह बस्ती एक शुद्ध औद्योगिक केंद्र थी जिसकी सुरक्षा मोहनजोदड़ो जैसे बड़े सुरक्षा दुर्गों पर निर्भर थी।"),
    ("केस स्टडी: बनावली का विचलित नियोजन", "हरियाणा के बनावली में अरीय सड़कें और एक ही टीले पर किले तथा निचले नगर की स्थिति मिली है। यद्यपि यहाँ मानक हड़प्पा बाट और खिलौने मिले हैं, लेकिन व्यवस्थित ग्रिड सड़कों और ढके हुए सीवरों का अभाव यह दर्शाता है कि क्षेत्रीय स्तरों पर नगर नियोजन स्थानीय प्राथमिकताओं के अनुरूप बदल जाता था।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: Grid Iron Planning & Wind Cleansing", "Explain how aligning streets North-South and East-West creates wind tunnels. As the wind blows, it accelerates through these pathways, naturally clearing away dust and organic debris, proving the Harappans incorporated environmental aerodynamics into urban planning."),
    ("Teach Concept: Citadel-Lower Town Dichotomy", "Explain the socio-spatial division. The west had the raised Citadel (administrative, public assemblies, elite residences, and food security granaries). The east had the Lower Town (larger, street grids, residential quarters for common citizens and artisans, showing class-based zoning)."),
    ("Teach Concept: Defensive and Protective Fortification Systems", "Teach how fortifications were not just military. They were barriers to prevent seasonal flooding, custom barriers to verify goods and collect tribute/tax from traders, and symbols of political authority constructed with massive labor investment.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): ग्रिड नियोजन और हवा से सफाई", "समझाएं कि सड़कों को उत्तर-दक्षिण और पूर्व-पश्चिम दिशा में संरेखित करने से वे 'विंड टनल' (हवा के मार्ग) बन जाती थीं। जब हवा चलती थी, तो वह इन मार्गों से तीव्र गति से गुजरती थी और धूल-कचरे को स्वतः साफ कर देती थी। यह पर्यावरणीय वास्तुकला का अनुपम उदाहरण है।"),
    ("अवधारणा समझाएं (Teach Concept): किला-निचला नगर का दोहरा विभाजन", "सामाजिक और स्थानिक विभाजन को स्पष्ट करें। पश्चिम में स्थित किला (Citadel) प्रशासनिक भवनों, सार्वजनिक सभाओं और अन्नागारों के लिए कच्चे चबूतरे पर बना था। पूर्व में स्थित निचला नगर बड़ा था जहाँ आम लोग, व्यापारी और सैनिक ग्रिड प्रतिरूप वाली सड़कों के किनारे रहते थे।"),
    ("अवधारणा समझाएं (Teach Concept): रक्षा दीवार प्रणाली के बहु-आयामी कार्य", "समझाएं कि हड़प्पा की नगर दीवारें केवल बाहरी सैन्य हमलों के लिए नहीं थीं। वे मौसमी बाढ़ के पानी को नगर में आने से रोकती थीं, सीमा शुल्क प्रवेश द्वार का कार्य करती थीं जहाँ व्यापारिक वस्तुओं पर कर वसूला जाता था, और केंद्रीय सत्ता का भव्य प्रतीक थीं।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: SANITATION, PUBLIC DRAINAGE & PRIVATE DRAINS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which site features hollowed-out wooden logs used as drainage conduits instead of baked-brick sewers?", ["Kalibangan", "Mohenjo-daro", "Lothal", "Banawali"], 0, "Kalibangan in Rajasthan is unique for its wooden drainage conduits, which represent a regional exception."),
    ("Approximately how many brick-lined water wells have been excavated at Mohenjo-daro alone?", ["Over 700", "Under 100", "Exactly 300", "Over 2000"], 0, "Archaeological surveys indicate Mohenjo-daro had over 700 public and private wells."),
    ("What device was installed beneath residential drains to trap solid waste before liquid entered main sewers?", ["Brick-lined soak pit (cesspit)", "Terracotta sieve", "Charcoal sand filter", "Copper mesh screen"], 0, "Soak pits allowed solid sediment to settle at the bottom, while only wastewater flowed out into public sewers."),
    ("Why were wedge-shaped (trapezoidal) bricks specifically utilized inside Harappan water wells?", ["To resist inward lateral soil pressure and form a circular wall", "To prevent water from evaporating", "To absorb moisture faster", "To decoration purposes"], 0, "Wedge-shaped bricks have radial edges that lock together under compression, creating strong circular well shafts."),
    ("How did double-story Harappan houses discharge wastewater from upper-floor bathrooms?", ["Through vertical clay pipes embedded inside house walls", "Through open channels on balconies", "By pouring it directly onto streets", "Through wooden gutters on roofs"], 0, "Vertical terracotta pipe sleeves were built directly into the thickness of house walls to channel sewage down.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("पकी ईंटों के स्थान पर खोखली लकड़ी के तनों को नाली के रूप में प्रयोग करने का साक्ष्य किस स्थल से मिला है?", ["कालीबंगन", "मोहनजोदड़ो", "लोथल", "बनावली"], 0, "राजस्थान के कालीबंगन से लकड़ी की नालियों का उपयोग मिला है जो हड़प्पा सभ्यता में एक अपवाद है।"),
    ("मोहनजोदड़ो में अकेले ही ईंटों से बने लगभग कितने कुएं खोजे गए हैं?", ["700 से अधिक", "100 से कम", "ठीक 300", "2000 से अधिक"], 0, "मोहनजोदड़ो में पुरातात्विक सर्वेक्षणों के अनुसार 700 से अधिक सार्वजनिक और निजी कुएं थे।"),
    ("सड़क के मुख्य नालों में पानी जाने से पहले ठोस कचरे को रोकने के लिए घरों के निकास पर क्या लगाया जाता था?", ["ईंटों से बना शोषक गड्ढा (soak pit)", "मिट्टी की छलनी", "कोयला और रेत का फिल्टर", "तांबे की जाली का पर्दा"], 0, "शोषक गड्ढे (cesspits) ठोस अपशिष्ट को नीचे जमा कर लेते थे, और केवल तरल पानी मुख्य नाली में बह जाता था।"),
    ("हड़प्पा के कुओं के निर्माण में त्रिकोणीय/फानाकार (wedge-shaped) ईंटों का उपयोग विशेष रूप से क्यों किया जाता था?", ["मिट्टी के दबाव को सहने और पूर्ण गोलाकार दीवार बनाने के लिए", "पानी को भाप बनने से रोकने के लिए", "नमी को तेजी से सोखने के लिए", "सजावटी प्रतिरूप बनाने के लिए"], 0, "फानाकार ईंटों के सिरे एक-दूसरे में फंसकर दबाव में गोलाकार दीवार को मजबूत और स्थायी बनाते थे।"),
    ("दो मंजिला हड़प्पा घरों में ऊपरी मंजिल के स्नानघरों से गंदा पानी कैसे निकाला जाता था?", ["दीवारों के भीतर गड़े ऊर्ध्वाधर (vertical) मिट्टी के पाइपों से", "बालकनी के खुले रास्तों से", "सीधे सड़क पर गिराकर", "छत पर लकड़ी के परनालों से"], 0, "मिट्टी के पाइपों को घरों की दीवारों के भीतर ही लगाया जाता था ताकि गंदा पानी सीधे नीचे मुख्य नाली में चला जाए।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which features characterized private residential sanitation in Harappan houses? (Select all that apply)", ["Bathrooms with sloping brick-paved floors", "Vertical clay pipes embedded inside walls", "Soak pits at sewer connections to trap solids", "Direct discharge from toilets onto open streets"], [0, 1, 2], "Bathrooms sloped, used wall pipes, and connected to soak pits. Direct street discharge was strictly forbidden."),
    ("Select the structural elements of the public street drainage system: (Select all that apply)", ["Paved with flat bricks below street level", "Covered with removable brick slabs or stone blocks", "Equipped with cleanup manholes at regular intervals", "Fitted with open garbage incinerators at junctions"], [0, 1, 2], "Public drains were paved, covered, and had inspection manholes. Incinerators were not part of the system."),
    ("What made the sanitation system at Kalibangan unique? (Select all that apply)", ["Use of hollowed-out wooden logs for drainage", "Lack of a standard baked-brick public sewerage network", "Separate domestic well in every single room", "Discharge of sewage directly into the local river"], [0, 1], "Kalibangan used wooden drains and lacked standard brick sewers. Rooms did not each have wells, nor did they dump in rivers."),
    ("Identify the elements associated with Harappan water management: (Select all that apply)", ["Private house wells placed near the entrance for travelers", "Over 700 wells inside Mohenjo-daro", "Extensive brick-built public wells on street corners", "Massive iron pipes for water distribution"], [0, 1, 2], "Wells lay near entrances, numbered over 700 at Mohenjo-daro, and sat on street corners. No iron pipes existed."),
    ("Which aspects describe the drainage network at the site of Banawali? (Select all that apply)", ["General absence of systematic street drains", "Use of earthenware jars at street corners to collect waste", "Poor drainage layout despite mature artifacts", "A network of stone-lined canals running to rivers"], [0, 1, 2], "Banawali lacked systematic drains, used corner pottery jars, and was poorly drained. No stone canals ran to rivers.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा के घरों में निजी स्वच्छता के कौन से लक्षण पाए जाते थे? (सभी लागू विकल्प चुनें)", ["ढलान वाले ईंटों के फर्श वाले स्नानघर", "दीवारों के भीतर गड़े मिट्टी के निकास पाइप", "ठोस कचरे को रोकने के लिए नालियों में बने शोषक गड्ढे", "शौचालय का कचरा सीधे खुली सड़कों पर गिराना"], [0, 1, 2], "स्नानघरों में ढलान थी, दीवारों में पाइप थे और वे शोषक गड्ढों से जुड़े थे। सड़कों पर कचरा सीधे गिराना वर्जित था।"),
    ("सार्वजनिक सड़क जल निकासी प्रणाली के संरचनात्मक तत्वों का चयन करें: (सभी लागू विकल्प चुनें)", ["सड़क के स्तर से नीचे चपटी ईंटों से पक्के किए जाना", "हटाए जाने योग्य ईंटों की शिलाओं या पत्थरों से ढके जाना", "नियमित अंतराल पर सफाई के लिए मैनहोल बने होना", "चौराहों पर खुली कचरा भट्टियों का लगा होना"], [0, 1, 2], "सड़क की नालियां पक्की, ढकी और निरीक्षण मैनहोल युक्त थीं। कचरा भट्टियां प्रणाली में शामिल नहीं थीं।"),
    ("कालीबंगन की स्वच्छता व्यवस्था को क्या विशिष्ट बनाता था? (सभी लागू विकल्प चुनें)", ["जल निकासी के लिए खोखली लकड़ी के तनों का उपयोग", "मानक पकी ईंटों के सार्वजनिक सीवर नेटवर्क का अभाव", "प्रत्येक कमरे में एक अलग कुआं होना", "गंदे पानी का सीधे स्थानीय नदी में बहाया जाना"], [0, 1], "कालीबंगन में लकड़ी की नालियां थीं और पकी ईंटों के सार्वजनिक सीवरों का अभाव था। कमरों में कुएं या नदी में सीधा बहाव नहीं था।"),
    ("हड़प्पा जल प्रबंधन से जुड़े तत्वों की पहचान करें: (सभी लागू विकल्प चुनें)", ["राहगीरों के लिए घर के प्रवेश द्वार के पास बने निजी कुएं", "मोहनजोदड़ो के भीतर मिले 700 से अधिक कुएं", "सड़कों के कोनों पर बने बड़े सार्वजनिक कुएं", "पानी वितरण के लिए लोहे के विशाल पाइप"], [0, 1, 2], "कुएं प्रवेश द्वार के पास, गलियों में और कुल संख्या 700 से अधिक थी। लोहे के पाइप अनुपस्थित थे।"),
    ("बनावली स्थल की जल निकासी व्यवस्था का वर्णन किन पहलुओं से होता है? (सभी लागू विकल्प चुनें)", ["व्यवस्थित सड़क नालियों का सामान्यतः अभाव", "कचरा इकट्ठा करने के लिए सड़क के कोनों पर शोषक मटकों का होना", "परिपक्व अवशेषों के बावजूद कमजोर जल निकासी व्यवस्था", "नदियों तक जाती हुई पत्थरों से बनी नहरों का जाल"], [0, 1, 2], "बनावली में व्यवस्थित सीवरों का अभाव था, कोनों पर मटके रखे जाते थे और जल निकासी कमजोर थी। पत्थरों की नहरें नहीं थीं।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Main street sewers were deliberately left completely open for ventilation.", False, "False. Main sewers were covered with stone blocks or brick slabs to maintain hygiene."),
    ("Residential wastewater entered street sewers directly without passing through cesspits.", False, "False. House drains emptied into soak pits first to trap solid debris."),
    ("Wooden logs were hollowed out to construct drainage channels at Kalibangan.", True, "True. Kalibangan is famous for using wooden drainage pipes, an exception in the IVC."),
    ("Mohenjo-daro had no more than 50 wells, forcing citizens to rely on the Indus River.", False, "False. Mohenjo-daro had over 700 brick-lined water wells."),
    ("Wastewater from upper floors was channeled down using clay pipes embedded in walls.", True, "True. Terracotta pipes were embedded in wall interiors to carry waste down cleanly."),
    ("Wedge-shaped bricks were used to pave the flat street drain bottoms.", False, "False. Wedge-shaped bricks were used to construct circular well shafts."),
    ("Inspection chambers along street drains had removable covers for cleaning.", True, "True. Removable stone or brick covers allowed municipal cleaners to inspect sewers."),
    ("Banawali had a drainage network that surpassed Mohenjo-daro's in quality.", False, "False. Banawali lacked systematic drains and relied on corner pottery jars.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हवा आने-जाने के लिए सड़कों के मुख्य नालों को जानबूझकर खुला रखा जाता था।", False, "असत्य। नालियों को ईंटों या पत्थर के स्लैब से ढका जाता था ताकि स्वच्छता बनी रहे।"),
    ("घरों का गंदा पानी बिना किसी शोषक गड्ढे के सीधे सड़क की नाली में बह जाता था।", False, "असत्य। पहले पानी शोषक गड्ढे (cesspit) में जाता था जहाँ ठोस कचरा रुकता था।"),
    ("कालीबंगन में जल निकासी के लिए लकड़ी के तनों को खोखला करके पाइप बनाए गए थे।", True, "सत्य। कालीबंगन अपनी अनोखी लकड़ी की नालियों के लिए प्रसिद्ध है।"),
    ("मोहनजोदड़ो में केवल 50 कुएँ थे और लोग मुख्य रूप से सिंधु नदी पर निर्भर थे।", False, "असत्य। मोहनजोदड़ो में 700 से अधिक कुएँ थे जो भूजल सुरक्षा सुनिश्चित करते थे।"),
    ("ऊपरी मंजिलों के स्नानघरों का गंदा पानी दीवारों में गड़े मिट्टी के पाइपों से नीचे लाया जाता था।", True, "सत्य। मिट्टी के पाइपों को दीवारों में छुपाया जाता था ताकि गंदा पानी सुरक्षित नीचे आ सके।"),
    ("सड़कों की समतल नालियों के तल को पक्का करने के लिए फानाकार ईंटों का उपयोग होता था।", False, "असत्य। फानाकार (wedge-shaped) ईंटों का उपयोग गोलाकार कुओं के निर्माण में होता था।"),
    ("नालियों के निरीक्षण मैनहोलों पर हटाने योग्य ढक्कन लगे होते थे।", True, "सत्य। हटाने योग्य ढक्कन सफाईकर्मियों को निरीक्षण और गाद निकालने की सुविधा देते थे।"),
    ("बनावली में मोहनजोदड़ो से भी अधिक उन्नत और गुणवत्तापूर्ण सीवर जाल था।", False, "असत्य। बनावली में व्यवस्थित सीवरों की कमी थी और लोग कोनों पर मटके रखते थे।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("Wooden drainage channels are uniquely found at the site of __________.", "Kalibangan", "Kalibangan is the only site with hollowed-out wooden log drains."),
    ("To construct circular wells, Harappan masonry utilized __________ bricks.", "wedge-shaped", "Wedge-shaped (trapezoidal) bricks formed perfect circular rings."),
    ("The total count of wells excavated at Mohenjo-daro is over __________.", "700", "Mohenjo-daro featured over 700 public and private wells."),
    ("Solid waste was trapped in residential __________ before water left the house.", "soak pits", "Soak pits (cesspools) filtered solid waste from household water."),
    ("Street drains were covered and featured regular __________ for maintenance.", "manholes", "Cleanup manholes (inspection chambers) were placed along main streets."),
    ("Terracotta pipes inside walls carried wastewater down from __________ stories.", "upper", "Vertical clay pipes carried sewage down from second-floor bathrooms."),
    ("At Banawali, street corners featured earthenware __________ to collect waste.", "jars", "Pottery jars (pots) were used at Banawali due to the lack of sewers."),
    ("Street drain channels were paved at the bottom with __________ bricks.", "flat", "Flat bricks were laid tightly to prevent sewage from seeping into soil.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लकड़ी के खोखले तनों से बनी अनूठी नालियां __________ स्थल पर मिली हैं।", "कालीबंगन", "कालीबंगन में लकड़ी की नालियों का अपवाद स्वरूप प्रयोग किया गया था।"),
    ("गोलाकार कुओं के निर्माण के लिए हड़प्पा के कारीगर __________ ईंटों का उपयोग करते थे।", "फानाकार", "फानाकार (wedge-shaped) ईंटें कुएं की दीवार को गोलाई और स्थिरता देती थीं।"),
    ("मोहनजोदड़ो में कुल खोजे गए कुओं की संख्या __________ से अधिक है।", "700", "मोहनजोदड़ो में 700 से अधिक कुएँ मिले हैं।"),
    ("घरों का गंदा पानी बाहर जाने से पहले ठोस कचरा रोकने के लिए __________ में जाता था।", "शोषक गड्ढे", "शोषक गड्ढे (soak pits) ठोस मलबे को नीचे रोक लेते थे।"),
    ("नालियों के रखरखाव और गाद निकालने के लिए नियमित अंतराल पर __________ बने थे।", "मैनहोल", "सड़कों की नालियों में निरीक्षण कक्ष या मैनहोल (inspection chambers) थे।"),
    ("दीवारों के अंदर के पाइप __________ मंजिल से गंदा पानी नीचे लाते थे।", "ऊपरी", "ऊपरी मंजिल (upper/second floor) के स्नानघरों से पानी नीचे लाया जाता था।"),
    ("बनावली में नालियों की कमी के कारण सड़कों के कोनों पर मिट्टी के __________ रखे थे।", "मटके", "बनावली में जल निकासी के अभाव में सड़कों पर शोषक मटके रखे जाते थे।"),
    ("सड़कों की नालियों के निचले तल को __________ ईंटों से पक्का किया जाता था।", "चपटी", "नालियों के धरातल को चपटी (flat) ईंटों से पक्का किया जाता था ताकि रिसाव न हो।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sanitation features with their respective sites:",
        "items": [{"left": "I. Wooden drainage channels", "key": "A"}, {"left": "II. Corner pottery waste jars", "key": "B"}, {"left": "III. Standard brick-lined soak pits", "key": "C"}],
        "options": [{"val": "A", "text": "A. Kalibangan (Rajasthan)"}, {"val": "B", "text": "B. Banawali (Haryana)"}, {"val": "C", "text": "C. Mohenjo-daro (Sindh)"}],
        "sol": "Wooden drains are at Kalibangan, corner jars at Banawali, and standard soak pits at Mohenjo-daro."
    },
    {
        "type": "Match the Following",
        "q": "Match the sanitary structures with their engineering functions:",
        "items": [{"left": "I. Residential soak pit", "key": "A"}, {"left": "II. Inspection manhole", "key": "B"}, {"left": "III. Inner-wall terracotta pipe", "key": "C"}],
        "options": [{"val": "A", "text": "A. Trapping solid debris before water enters public sewers"}, {"val": "B", "text": "B. Sewer inspection, desilting, and municipal cleanup"}, {"val": "C", "text": "C. Channelling waste down from double-story bathrooms"}],
        "sol": "Soak pits trap solids, manholes facilitate desilting, and wall pipes carry waste from upper floors."
    },
    {
        "type": "Match the Following",
        "q": "Match the water resource structures with their characteristics:",
        "items": [{"left": "I. Dholavira Reservoirs", "key": "A"}, {"left": "II. Mohenjo-daro Wells", "key": "B"}, {"left": "III. Kalibangan Wells", "key": "C"}],
        "options": [{"val": "A", "text": "A. Rock-cut stone reservoirs fed by check dams"}, {"val": "B", "text": "B. Over 700 brick-lined circular groundwater shafts"}, {"val": "C", "text": "C. Scarce wells, with households relying on rain cisterns"}],
        "sol": "Dholavira has stone reservoirs, Mohenjo-daro has 700+ brick wells, and Kalibangan has very few wells."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "स्वच्छता व्यवस्था के विशिष्ट लक्षणों को उनके स्थलों से सुमेलित करें:",
        "items": [{"left": "I. लकड़ी के तनों की नालियाँ", "key": "A"}, {"left": "II. सड़क किनारे शोषक मटके", "key": "B"}, {"left": "III. ईंटों से बने मानक शोषक गड्ढे", "key": "C"}],
        "options": [{"val": "A", "text": "A. कालीबंगन (राजस्थान)"}, {"val": "B", "text": "B. बनावली (हरियाणा)"}, {"val": "C", "text": "C. मोहनजोदड़ो (सिंध)"}],
        "sol": "लकड़ी की नालियां कालीबंगन में, शोषक मटके बनावली में, और ईंटों के शोषक गड्ढे मोहनजोदड़ो में मिले हैं।"
    },
    {
        "type": "Match the Following",
        "q": "स्वच्छता संरचनाओं को उनके इंजीनियरिंग कार्यों से सुमेलित करें:",
        "items": [{"left": "I. घरेलू शोषक गड्ढा (Soak pit)", "key": "A"}, {"left": "II. निरीक्षण मैनहोल", "key": "B"}, {"left": "III. दीवार के भीतर का पाइप", "key": "C"}],
        "options": [{"val": "A", "text": "A. मुख्य नाली में जाने से पहले ठोस कचरे को रोकना"}, {"val": "B", "text": "B. सीवर की सफाई, गाद निकालना और निरीक्षण करना"}, {"val": "C", "text": "C. दो मंजिला स्नानघरों से गंदे पानी को नीचे लाना"}],
        "sol": "शोषक गड्ढा ठोस रोकता है, मैनहोल गाद निकालने के लिए है, और दीवार पाइप ऊपरी मंजिल के पानी के लिए है।"
    },
    {
        "type": "Match the Following",
        "q": "जल संचयन संरचनाओं को उनकी विशेषताओं से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा के जलाशय", "key": "A"}, {"left": "II. मोहनजोदड़ो के कुएं", "key": "B"}, {"left": "III. कालीबंगन के कुएं", "key": "C"}],
        "options": [{"val": "A", "text": "A. पत्थरों को काटकर बने चेक डैम से जुड़े विशाल जलाशय"}, {"val": "B", "text": "B. 700 से अधिक ईंटों से बने गोलाकार भूजल कुएं"}, {"val": "C", "text": "C. अत्यंत दुर्लभ कुएं, अधिकांश घर वर्षा जल पर निर्भर"}],
        "sol": "धोलावीरा में पत्थर के जलाशय, मोहनजोदड़ो में 700 से अधिक कुएं, और कालीबंगन में कुएं बहुत कम मिले हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What was the primary material used to cover the public street sewers?", "Baked brick slabs or flat limestone blocks."),
    ("Why did Harappan masons use wedge-shaped bricks in wells?", "The angled sides lock together under soil pressure, keeping the circular wall intact."),
    ("How did Harappan cleaners inspect and clear blockages in covered drains?", "Through regular rectangular inspection manholes built along the street paths."),
    ("Which site features hollowed-out wooden log conduits instead of standard brick drains?", "Kalibangan in Rajasthan."),
    ("How was solid domestic waste filtered before wastewater entered public sewers?", "It was collected in residential soak pits where solid sediment settled to the bottom."),
    ("What is the estimated number of brick-lined wells discovered at Mohenjo-daro?", "Over 700 wells."),
    ("How was wastewater channeled from the second floor of a double-story house?", "Through vertical terracotta pipe sleeves embedded directly inside house walls."),
    ("What temporary waste disposal system was used at Banawali due to poor drainage layout?", "Earthenware pottery jars placed at street corners to collect liquid runoff.")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("सार्वजनिक सड़क सीवरों को ढकने के लिए मुख्य रूप से किस सामग्री का उपयोग किया जाता था?", "पकी ईंटों की शिलाओं या चूना पत्थर के चौकोर खंडों का।"),
    ("कुओं में फानाकार (wedge-shaped) ईंटों के उपयोग का क्या कारण था?", "ईंटों के कोण दबाव में एक-दूसरे को जकड़ लेते थे, जिससे कुएं का घेरा ढहता नहीं था।"),
    ("सफाईकर्मी ढकी हुई नालियों की रुकावटों को कैसे दूर करते थे?", "सड़कों के साथ बने नियमित आयताकार निरीक्षण मैनहोलों (inspection manholes) के माध्यम से।"),
    ("किस स्थल पर पकी ईंटों के बजाय खोखले लकड़ी के तनों की नालियां मिली हैं?", "राजस्थान के कालीबंगन में।"),
    ("नालियों में बहने वाले गंदे पानी से ठोस कचरे को कैसे अलग किया जाता था?", "घरों के मुहाने पर बने शोषक गड्ढों में कचरा बैठ जाता था और केवल तरल बह जाता था।"),
    ("मोहनजोदड़ो में ईंटों से बने कितने कुओं के अवशेष मिले हैं?", "700 से अधिक कुएं।"),
    ("दो मंजिला घरों की ऊपरी मंजिल से गंदे पानी का निकास कैसे किया जाता था?", "दीवारों के भीतर गड़े मिट्टी (terracotta) के ऊर्ध्वाधर पाइपों के माध्यम से।"),
    ("व्यवस्थित नालियों के अभाव में बनावली में कचरा संग्रहण के लिए क्या वैकल्पिक व्यवस्था थी?", "सड़कों के मोड़ों पर बड़े मिट्टी के मटके (pottery jars) रखे जाते थे।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Public street drains were covered with brick slabs or stone blocks.\nReason (R): Covered sewers prevented noxious odors and reduced the risk of waterborne epidemics.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Kalibangan houses had hollowed-out wooden logs for drainage conduits.\nReason (R): Kalibangan completely lacked clay deposits to manufacture standard terracotta drainage pipes.", 2, "A is true but R is false (clay was available; wooden drains were just a local preference)."),
    ("Assertion (A): Residential wastewater did not discharge directly into public street sewers.\nReason (R): Soak pits trapped solid waste first, allowing only liquid runoff to enter main drains.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Wedge-shaped bricks were used to pave the flat floors of street drains.\nReason (R): Wedge-shaped bricks are designed to lock together under compression, ideal for circular shafts.", 3, "A is false because flat bricks paved drains. R is true."),
    ("Assertion (A): Mohenjo-daro had over 700 wells, proving highly secure groundwater management.\nReason (R): Most houses had private wells located near the entrance for family use and travelers.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Terracotta pipe sleeves were embedded inside the thickness of house walls.\nReason (R): These pipes carried clean drinking water from street reservoirs up to second-story bathrooms.", 2, "A is true. R is false because they carried wastewater down, not drinking water up."),
    ("Assertion (A): Banawali streets completely lacked a systematic network of covered brick sewers.\nReason (R): Banawali was a rural agricultural site that did not belong to the mature Harappan culture.", 2, "A is true. R is false because Banawali was a mature town with standard weights, but just had poor drainage."),
    ("Assertion (A): Street sewers required regular desilting and maintenance by municipal workers.\nReason (R): Rectangular manholes with removable stone covers were constructed at regular intervals along main streets.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): सड़कों के मुख्य सीवर ईंटों के स्लैब या पत्थरों से ढके होते थे।\nकारण (R): ढके हुए सीवर दुर्गंध को रोकते थे और जल जनित महामारियों के खतरे को कम करते थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कालीबंगन के घरों में जल निकासी के लिए खोखले लकड़ी के तनों का उपयोग किया गया था।\nकारण (R): कालीबंगन में मिट्टी के बर्तन और मानक पाइप बनाने के लिए चिकनी मिट्टी का पूर्ण अभाव था।", 2, "A सत्य है लेकिन R असत्य है (मिट्टी प्रचुर मात्रा में थी; लकड़ी का उपयोग स्थानीय पसंद थी)।"),
    ("कथन (A): घरों से निकलने वाला गंदा पानी बिना किसी रुकावट के सीधे मुख्य नाली में गिरता था।\nकारण (R): शोषक गड्ढे पहले ठोस मलबे को जमा कर लेते थे जिससे मुख्य सीवर में रुकावट नहीं आती थी।", 3, "A असत्य है क्योंकि गंदा पानी सीधे नहीं बल्कि शोषक गड्ढे से होकर जाता था। R सत्य है।"),
    ("कथन (A): सड़कों की नालियों के समतल फर्श को पक्का करने के लिए फानाकार ईंटों का उपयोग किया जाता था।\nकारण (R): फानाकार ईंटें दबाव में एक-दूसरे में फंस जाती हैं, जो कुओं की गोलाकार दीवारों के लिए आदर्श थीं।", 3, "A असत्य है क्योंकि नालियों में चपटी ईंटें लगती थीं। R सत्य है।"),
    ("कथन (A): मोहनजोदड़ो में 700 से अधिक कुएँ थे, जो उन्नत भूजल सुरक्षा प्रणाली को सिद्ध करते हैं।\nकारण (R): अधिकांश कुएँ घर के प्रवेश द्वार के समीप बनाए जाते थे ताकि बाहरी राहगीर भी उनका उपयोग कर सकें।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मिट्टी (terracotta) के पाइपों को घरों की दीवारों के भीतर ही लगाया जाता था।\nकारण (R): ये पाइप मुख्य जलाशयों से पीने के स्वच्छ जल को खींचकर ऊपरी मंजिलों तक पहुँचाने के काम आते थे।", 2, "A सत्य है लेकिन R असत्य है क्योंकि ये पाइप गंदे पानी को नीचे लाते थे, स्वच्छ पानी को ऊपर नहीं ले जाते थे।"),
    ("कथन (A): बनावली की सड़कों पर पकी ईंटों से बने ढके हुए सीवरों का व्यवस्थित जाल नहीं था।\nकारण (R): बनावली एक पूर्णतः ग्रामीण कृषि क्षेत्र था जो हड़प्पा के शहरी चरण में शामिल नहीं था।", 2, "A सत्य है लेकिन R असत्य है क्योंकि बनावली परिपक्व शहरी चरण का हिस्सा था, यद्यपि यहाँ जल निकासी कमजोर थी।"),
    ("कथन (A): नगर निगम के कर्मचारियों द्वारा सड़कों के सीवरों से नियमित गाद निकालना और सफाई करना आवश्यक था।\nकारण (R): मुख्य सड़कों पर सीवर लाइनों के ऊपर नियमित स्थानों पर हटाने योग्य पत्थरों के मैनहोल ढक्कन लगे थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan public drains:\n1. Drains were constructed with a slight gradient or slope to ensure smooth flow.\n2. Covered street drains completely lacked inspection chambers or manholes.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: regular manholes were provided for cleaning."),
    ("Consider the following statements regarding Kalibangan's drains:\n1. It featured standard public baked-brick sewers along all primary roads.\n2. Hollowed-out wooden log conduits were used in place of standard clay sewers.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: Kalibangan lacked brick street sewers."),
    ("Consider the following statements regarding soak pits:\n1. Soak pits were designed to collect solid organic debris inside residential properties.\n2. Only liquid effluent was allowed to drain out into the municipal sewer line.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and define the filtration mechanism of Harappan soak pits."),
    ("Consider the following statements regarding wells:\n1. Circular wells were lined using wedge-shaped bricks to resist soil pressure.\n2. Over 700 brick wells have been excavated inside Mohenjo-daro.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, illustrating the architecture and count of wells at Mohenjo-daro."),
    ("Consider the following statements regarding household drains:\n1. Bathrooms were paved with flat bricks and sloped to carry wastewater away.\n2. Clay pipes embedded inside house walls channeled waste from upper stories.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and describe the domestic drainage design of Harappan houses.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा की सार्वजनिक नालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. नालियों का निर्माण पानी के सुचारू प्रवाह के लिए हल्के ढलान के साथ किया जाता था।\n2. ढकी हुई नालियों में सफाई के लिए कोई निरीक्षण कक्ष (manholes) नहीं बने थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि नालियों की सफाई के लिए नियमित मैनहोल बने थे।"),
    ("कालीबंगन की नालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ सभी मुख्य सड़कों पर पकी ईंटों से बने सार्वजनिक सीवर मिले हैं।\n2. मिट्टी के नालों के स्थान पर खोखली लकड़ी के तनों का जल निकासी के लिए उपयोग किया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि कालीबंगन में पकी ईंटों के सीवरों का अभाव था।"),
    ("शोषक गड्ढों (soak pits) के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इन्हें घरों से निकलने वाले ठोस जैविक कचरे को एकत्र करने के लिए बनाया जाता था।\n2. केवल तरल भाग को ही बाहर बहकर सार्वजनिक सीवर में जाने दिया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और हड़प्पा शोषक गड्ढों की कार्यप्रणाली को स्पष्ट करते हैं।"),
    ("कुओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. गोलाकार कुओं में बाहरी दबाव झेलने के लिए फानाकार ईंटें लगाई जाती थीं।\n2. मोहनजोदड़ो के भीतर से 700 से अधिक ईंटों के कुएं मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मोहनजोदड़ो के कुओं की संख्या और बनावट को स्पष्ट करते हैं।"),
    ("घरेलू नालियों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्नानघरों के फर्श ढलान वाले होते थे और उन्हें चपटी ईंटों से पक्का किया जाता था।\n2. घरों की दीवारों के भीतर दबे मिट्टी के पाइप ऊपरी मंजिल का गंदा पानी लाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और घरों के भीतर जल निकासी के लेआउट को दर्शाते हैं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why were street sewer lines covered with removable brick slabs or stone blocks?", "To prevent bad odors, maintain sanitary conditions, protect public health, and allow easy removal for desilting."),
    ("Why did the Harappan sanitation network incorporate soak pits at residential exits?", "To filter out solid waste and sludge, preventing it from choking the main sewers and ensuring only liquid waste entered street drains."),
    ("Why were domestic wells often positioned near the outer entrance doors of Harappan houses?", "To allow family members easy access and to let travelers and neighbors draw water without breaching the family's privacy inside the courtyard.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("सड़कों की सीवर लाइनों को हटाने योग्य ईंटों या पत्थरों से क्यों ढका जाता था?", "दुर्गंध रोकने, स्वच्छता बनाए रखने, सार्वजनिक स्वास्थ्य की रक्षा करने और सफाई के लिए उन्हें आसानी से हटाने की सुविधा देने के लिए।"),
    ("हड़प्पा की जल निकासी प्रणाली में घरों के निकास पर शोषक गड्ढे (soak pits) क्यों लगाए गए थे?", "ठोस कचरे और कीचड़ को छानने के लिए ताकि वह मुख्य सीवर में जाकर रुकावट पैदा न करे और केवल पानी नाली में बहे।"),
    ("घरों के कुएं अक्सर मुख्य प्रवेश द्वार के निकट ही क्यों बनाए जाते थे?", "ताकि घर के सदस्यों के साथ-साथ राहगीरों और पड़ोसियों को भी पानी मिल सके और उन्हें घर के आंतरिक आंगन की गोपनीयता भंग न करनी पड़े।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How was wastewater channeled from upper floors in double-story Harappan homes?", "Through vertical terracotta pipe sleeves embedded inside the house walls, discharging into street-level drains through a wall aperture."),
    ("How did Kalibangan's private drainage systems differ from Mohenjo-daro's?", "Kalibangan relied on hollowed-out wooden logs for domestic conduits and lacked standard baked-brick public sewers, whereas Mohenjo-daro used brick-lined drains throughout."),
    ("How did the geometry of wedge-shaped bricks ensure the stability of circular wells?", "The radial sides of wedge-shaped bricks lock together tightly under soil pressure, preventing the circular well shaft from collapsing inward.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("दो मंजिला हड़प्पा घरों की ऊपरी मंजिलों से गंदे पानी का निकास कैसे किया जाता था?", "दीवारों के भीतर गड़े मिट्टी के नलदार पाइपों (terracotta pipes) के माध्यम से, जो नीचे गली की नाली में खुलते थे।"),
    ("कालीबंगन की घरेलू नाली प्रणाली मोहनजोदड़ो से किस प्रकार भिन्न थी?", "कालीबंगन में लकड़ी के खोखले तनों का नाली के रूप में प्रयोग किया गया था और सार्वजनिक ईंट सीवरों की कमी थी, जबकि मोहनजोदड़ो में हर जगह पकी ईंटों के सीवर थे।"),
    ("फानाकार (wedge-shaped) ईंटों की ज्यामिति कुओं की स्थिरता कैसे सुनिश्चित करती थी?", "ईंटों के तिरछे हिस्से बाहरी मिट्टी के दबाव में आपस में कस जाते थे, जिससे गोलाकार कुआं अंदर की तरफ धंसने से बच जाता था।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Mohenjo-daro's Groundwater Network", "Mohenjo-daro featured over 700 wells, meaning a well was available every third house. Placed near street entrances, these wells provided clean water security. Wedge-shaped bricks prevented structural collapse, showing advanced hydraulic engineering unmatched by contemporary civilizations."),
    ("Case Study: Covered Sewers of Mohenjo-daro", "Mohenjo-daro's streets were aligned with brick-lined drains laid below road levels, sloped for gravity-driven flow. Removable stone covers and regular inspection manholes enabled municipal cleaning, showcasing a highly structured civic management."),
    ("Case Study: Kalibangan's Wooden Drains", "At Kalibangan, archaeologists discovered hollowed-out sal or teak logs used as domestic drainage pipes. Combined with a lack of brick-lined public street drains, this proves that regional centers adapted sanitation systems to locally available timber and materials.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: मोहनजोदड़ो का भूजल कुआं नेटवर्क", "मोहनजोदड़ो में 700 से अधिक कुएँ मिले हैं, यानी हर तीसरे घर में एक कुआँ था। प्रवेश द्वार के पास बने ये कुएँ स्वच्छ जल सुरक्षा प्रदान करते थे। फानाकार ईंटों ने संरचना को ढहने से बचाया, जो तत्कालीन विश्व में बेजोड़ जल इंजीनियरिंग को दर्शाता है।"),
    ("केस स्टडी: मोहनजोदड़ो के ढके सीवर", "मोहनजोदड़ो की सड़कों के नीचे पकी ईंटों के नाले ढलान के साथ बनाए गए थे ताकि पानी का प्रवाह बना रहे। हटाने योग्य पत्थर के ढक्कन और नियमित मैनहोलों ने नगरपालिका द्वारा सीवरों की सफाई को सक्षम बनाया, जो संगठित नागरिक शासन को दर्शाता है।"),
    ("केस स्टडी: कालीबंगन की लकड़ी की नालियां", "कालीबंगन में पुराविदों को साल या सागौन की लकड़ी के तनों को खोखला करके बनाई गई नालियां मिली हैं। सार्वजनिक ईंट की नालियों के अभाव के साथ यह सिद्ध करता है कि क्षेत्रीय केंद्रों ने स्थानीय रूप से उपलब्ध लकड़ी के संसाधनों के आधार पर नालियों का निर्माण किया।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: Residential Soak Pits", "Explain how soak pits act as gravity filters. Household wastewater enters a brick pit beneath the street. Heavy solid particles sink to the bottom, forming sludge. Clearer water overflows from the top into the public street sewer, preventing blockage."),
    ("Teach Concept: Public Sanitation & Clean-up Manholes", "Teach the civic system of street drains. Paved with flat bricks, covered with slabs, and fitted with rectangular manholes. Removable covers let workers scoop out silt periodically. Contrast this with Mesopotamian open street gutters to show superior hygiene."),
    ("Teach Concept: Hydraulic Engineering of Wells", "Describe the physics of well building. Standard rectangular bricks slip when arranged in a circle because their sides are parallel. Wedge-shaped bricks have angled edges that align perfectly around a center, creating a compression arch that holds back wet earth.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): घरेलू शोषक गड्ढे (Soak Pits)", "समझाएं कि शोषक गड्ढे गुरुत्वाकर्षण फिल्टर के रूप में कैसे कार्य करते हैं। घरों का पानी गली के नीचे बने ईंट के गड्ढे में गिरता है। भारी ठोस कण नीचे बैठ जाते हैं और कीचड़ बन जाते हैं। साफ तरल पानी ऊपर से बहकर मुख्य नाली में चला जाता है, जिससे रुकावट नहीं होती।"),
    ("अवधारणा समझाएं (Teach Concept): सार्वजनिक स्वच्छता और मैनहोल प्रणाली", "सड़क की नालियों के नागरिक तंत्र को समझाएं। चपटी ईंटों से पक्के, स्लैब से ढके और आयताकार मैनहोलों से युक्त नाले। हटाने योग्य ढक्कन सफाईकर्मियों को गाद निकालने की अनुमति देते थे। इसकी तुलना मेसोपोटामिया की खुली नालियों से करें जो गंदगी से भरी रहती थीं।"),
    ("अवधारणा समझाएं (Teach Concept): कुओं की जल वास्तुकला और भौतिकी", "कुआं निर्माण की भौतिकी समझाएं। सामान्य आयताकार ईंटों को गोले में लगाने पर वे खिसक जाती हैं क्योंकि उनके किनारे समानांतर होते हैं। फानाकार ईंटों के कोण ऐसे होते हैं जो केंद्र के चारों ओर पूरी तरह फिट बैठते हैं और एक मजबूत मेहराब बनाते हैं जो मिट्टी के दबाव को रोकता है।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: BRICK TECHNOLOGY, METROLOGY & CIVIC ARCHITECTURE
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("What was the highly standardized dimension ratio (length:width:thickness) followed by Harappan builders for all bricks?", ["4:2:1", "3:2:1", "5:3:1", "4:3:2"], 0, "Both sun-dried and burnt bricks followed the strict mathematical ratio of 4:2:1."),
    ("Which material was standard for carving the cubical weights used in Harappan trade?", ["Chert", "Steatite", "Lapis Lazuli", "Sandstone"], 0, "Chert, a hard microcrystalline quartz, was standard for producing cubical trade weights."),
    ("Which adhesive binder was used to secure the baked bricks and waterproof the Great Bath of Mohenjo-daro?", ["Gypsum mortar", "Asphalt slurry", "Mud paste", "Lime-silica sand"], 0, "Gypsum mortar was used as the binding agent between the bricks, which were then sealed with bitumen."),
    ("What was the weight in grams of the basic unit of Harappan metrology (equivalent to weight ratio 16)?", ["13.63 grams", "5.51 grams", "27.46 grams", "8.25 grams"], 0, "The basic unit weight (ratio 16) corresponds to approximately 13.63 grams in modern metrology."),
    ("What brick-laying pattern was used by Harappan builders to provide maximum strength and load-bearing capacity to walls?", ["English bond (interlocking headers and stretchers)", "Flemish bond", "Stack bond", "Running bond"], 0, "The English bond pattern, where headers and stretchers alternate in successive courses, was used for strength.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा के निर्माताओं द्वारा सभी ईंटों के लिए किस मानकीकृत आयाम अनुपात (लंबाई:चौड़ाई:मोटाई) का पालन किया जाता था?", ["4:2:1", "3:2:1", "5:3:1", "4:3:2"], 0, "धूप में सुखाई गई (कच्ची) और पकी दोनों ईंटें हमेशा 4:2:1 के गणितीय अनुपात में बनाई जाती थीं।"),
    ("हड़प्पा व्यापार में प्रयुक्त होने वाले घनाकार बाट बनाने के लिए किस पत्थर का मानक रूप से उपयोग किया जाता था?", ["चर्ट (Chert)", "सेलखड़ी (Steatite)", "लाजवर्त (Lapis)", "बलुआ पत्थर (Sandstone)"], 0, "चर्ट नामक अत्यंत कठोर पत्थर का उपयोग मानकीकृत घनाकार बाट बनाने के लिए किया जाता था।"),
    ("मोहनजोदड़ो के विशाल स्नानागार (Great Bath) को जोड़ने और जल-रोधी बनाने के लिए किस गारे का उपयोग किया गया था?", ["जिप्सम का गारा", "डामर का लेप", "मिट्टी का गारा", "चूना-सिलिका रेत"], 0, "ईंटों को जोड़ने के लिए जिप्सम के गारे (gypsum mortar) का उपयोग किया गया था, जिसके ऊपर डामर की सील लगाई गई थी।"),
    ("हड़प्पा मापन प्रणाली की आधार इकाई (अनुपात 16 के समतुल्य बाट) का आधुनिक वजन ग्राम में कितना था?", ["13.63 ग्राम", "5.51 ग्राम", "27.46 ग्राम", "8.25 ग्राम"], 0, "हड़प्पा मापन में प्रयुक्त अनुपात 16 की आधार इकाई का आधुनिक मान लगभग 13.63 ग्राम था।"),
    ("दीवारों को अधिकतम मजबूती और भार वहन क्षमता देने के लिए हड़प्पा के निर्माता ईंट बिछाने के किस पैटर्न का उपयोग करते थे?", ["इंग्लिश बांड (English bond - एक-दूसरे में फंसाकर)", "फ्लेमिश बांड", "स्टैक बांड", "रनिंग बांड"], 0, "इंग्लिश बांड पैटर्न का उपयोग किया जाता था, जहाँ ईंटों को एक-दूसरे के जोड़ों पर फंसाकर (interlocking) लगाया जाता था।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the architectural and structural features of the Great Bath: (Select all that apply)", ["Lined with tightly fitted baked bricks", "Bound with gypsum mortar", "Waterproofed with a layer of natural bitumen", "Surrounded by a moat filled with river water"], [0, 1, 2], "The Bath was brick-paved, bound with gypsum, and sealed with bitumen. It had no surrounding moat."),
    ("Which characteristics describe the Great Granaries of Harappa and Mohenjo-daro? (Select all that apply)", ["Raised on high brick platforms to avoid floods", "Equipped with under-floor air ventilation ducts", "Constructed near river banks for grain shipping", "Contained large stone statues of fertility deities"], [0, 1, 2], "Granaries were raised, had air ducts, and sat near rivers for trade. No statues were found inside them."),
    ("Select the features of the Harappan weight and metrology systems: (Select all that apply)", ["Weights were standard cubical blocks of chert", "Binary scales (1, 2, 4, 8... 64) for lower weights", "Decimal scales for higher value weights", "Bronze scales and ivory rulers for length"], [0, 1, 2, 3], "All listed items are verified components of Harappan metrological standardisation, including binary/decimal weights and rulers."),
    ("Which materials were key to Harappan public civic architecture? (Select all that apply)", ["Baked bricks of 4:2:1 ratio", "Gypsum mortar for binding", "Natural bitumen for waterproofing", "Iron reinforcement beams in walls"], [0, 1, 2], "Bricks, gypsum, and bitumen were central to construction. Iron was unknown to the Bronze Age Harappans."),
    ("What features defined the Collegiate complexes and Assembly Halls of Mohenjo-daro? (Select all that apply)", ["The Assembly Hall contained 20 brick pillars in rows", "Located on the western Citadel mound", "Collegiate Building featured a central courtyard", "Housed the gold throne of the ruling monarch"], [0, 1, 2], "The Assembly Hall had 20 pillars, sat on the Citadel, and the Collegiate had a courtyard. No monarchial thrones existed.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("विशाल स्नानागार (Great Bath) की वास्तुशिल्प विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["सटीक रूप से जुड़ी पकी ईंटों से निर्मित होना", "ईंटों को जोड़ने के लिए जिप्सम गारे का प्रयोग", "जल-रोधी बनाने के लिए प्राकृतिक डामर का लेप", "नदी के पानी से भरी एक गहरी खाई से घिरा होना"], [0, 1, 2], "स्नानागार में ईंटें, जिप्सम गारा और डामर का उपयोग हुआ था। इसके चारों ओर कोई सुरक्षा खाई नहीं थी।"),
    ("हड़प्पा और मोहनजोदड़ो के विशाल अन्नागारों (Granaries) का वर्णन कौन सी विशेषताएँ करती हैं? (सभी लागू विकल्प चुनें)", ["बाढ़ से बचाने के लिए ऊंचे ईंटों के चबूतरे पर होना", "सीलन रोकने के लिए हवा आने-जाने के रास्तों (air ducts) का होना", "अनाज के परिवहन के लिए नदी तटों के पास स्थित होना", "अंदर उर्वरता के देवताओं की विशाल पत्थर की मूर्तियाँ होना"], [0, 1, 2], "अन्नागार चबूतरों पर बने थे, हवादार थे और नदी के पास थे। अंदर कोई धार्मिक मूर्तियां नहीं मिली हैं।"),
    ("हड़प्पा के बाट और माप प्रणालियों की विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["बाट मुख्य रूप से घनाकार चर्ट पत्थर के होते थे", "कम वजन के लिए द्वि-आधारी (binary - 1, 2, 4, 8... 64) प्रणाली", "उच्च मूल्यों के वजन के लिए दशमलव (decimal) प्रणाली", "लंबाई मापने के लिए कांसे के पैमाने और हाथीदांत के स्केल"], [0, 1, 2, 3], "सभी चारों विकल्प हड़प्पा के बाट-माप प्रणाली के प्रामाणिक और वैज्ञानिक लक्षण हैं।"),
    ("हड़प्पा वास्तुकला और नागरिक संरचनाओं के प्रमुख घटक कौन से थे? (सभी लागू विकल्प चुनें)", ["4:2:1 अनुपात की पकी ईंटें", "ईंटों को जोड़ने के लिए जिप्सम का गारा", "जल-रोधी बनाने के लिए प्राकृतिक डामर (tar)", "दीवारों को सहारा देने के लिए लोहे के गार्डर"], [0, 1, 2], "ईंटें, जिप्सम और डामर निर्माण के मुख्य आधार थे। कांस्य युगीन हड़प्पा वासियों को लोहे का ज्ञान नहीं था।"),
    ("मोहनजोदड़ो के कॉलेज भवन (Collegiate Building) और सभा भवन को क्या परिभाषित करता है? (सभी लागू विकल्प चुनें)", ["सभा भवन में 20 ईंटों के स्तंभ कतारों में बने थे", "ये संरचनाएं पश्चिमी किले (Citadel) के टीले पर स्थित थीं", "कॉलेज भवन में एक बड़ा मध्य आंगन और कमरे थे", "इनमें शासक सम्राट का सोने का सिंहासन रखा था"], [0, 1, 2], "सभा भवन में 20 स्तंभ थे, ये किले पर थे और कॉलेज भवन में आंगन था। सम्राट के सोने के सिंहासन का कोई साक्ष्य नहीं है।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Mud bricks followed a different dimensional ratio than baked bricks.", False, "False. Both mud and baked bricks adhered to the strict 4:2:1 ratio."),
    ("Chert weights were used exclusively in Gujarat and not standardized in Punjab.", False, "False. Cubical chert weights were standardized across the entire Harappan territory."),
    ("The Great Bath was waterproofed using natural bitumen (asphalt).", True, "True. A layer of natural bitumen made the Great Bath watertight."),
    ("The Assembly Hall at Mohenjo-daro featured twenty brick pillars arranged in rows.", True, "True. The square hall featured 20 brick pillars (4 rows of 5)."),
    ("The basic weight unit of Harappan trade was equivalent to 13.63 grams.", True, "True. Ratio 16 corresponds to 13.63 grams in modern measurements."),
    ("Harappans used the Flemish bond pattern for building thick walls.", False, "False. They used the English bond pattern, which alternates headers and stretchers."),
    ("Under-floor air ducts inside granaries prevented moisture from spoiling grains.", True, "True. Air ducts allowed wind circulation to keep the floor dry."),
    ("The Collegiate Building was a residential palace for a single ruling monarch.", False, "False. It was a large institutional building with a courtyard, likely for priests or scholars.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कच्ची मिट्टी की ईंटें पकी ईंटों से अलग आकार अनुपात में बनाई जाती थीं।", False, "असत्य। कच्ची और पकी दोनों ईंटें 4:2:1 के समान अनुपात का पालन करती थीं।"),
    ("चर्ट के बाट केवल गुजरात में उपयोग होते थे और पंजाब में मानकीकृत नहीं थे।", False, "असत्य। चर्ट के घनाकार बाट पूरी हड़प्पा सभ्यता में मानकीकृत और एक समान थे।"),
    ("विशाल स्नानागार (Great Bath) को जल-रोधी बनाने के लिए प्राकृतिक डामर का प्रयोग हुआ था।", True, "सत्य। पानी के रिसाव को रोकने के लिए डामर (bitumen) की मोटी परत लगाई गई थी।"),
    ("मोहनजोदड़ो के सभा भवन में बीस ईंटों के खंभे कतारों में व्यवस्थित थे।", True, "सत्य। इस चौकोर सभा भवन में 20 स्तंभ (4 कतारों में 5-5) मिले हैं।"),
    ("हड़प्पा व्यापार के बाटों की आधार इकाई लगभग 13.63 ग्राम के बराबर थी।", True, "सत्य। अनुपात 16 का मान आधुनिक मापन में 13.63 ग्राम पाया गया है।"),
    ("हड़प्पावासी दीवारें बनाने के लिए फ्लेमिश बांड (Flemish bond) का उपयोग करते थे।", False, "असत्य। वे इंग्लिश बांड (English bond) पैटर्न का उपयोग करते थे।"),
    ("अन्नागारों में फर्श के नीचे बने हवा के रास्तों ने नमी से अनाज को सड़ने से बचाया।", True, "सत्य। हवा के रास्तों (air ducts) से हवा का संचरण होता था जो सीलन नहीं होने देता था।"),
    ("कॉलेज भवन (Collegiate Building) एक एकल शासक सम्राट का निजी महल था।", False, "असत्य। यह एक बड़ा सार्वजनिक संस्थान था, जो पुरोहितों या प्रशासनिक सभा के उपयोग में आता था।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The standard dimension ratio of Harappan bricks is __________.", "4:2:1", "All bricks followed the ratio 4:2:1 (length:width:thickness)."),
    ("Harappan cubical trade weights were carved from a hard stone called __________.", "chert", "Chert was selected due to its hardness and resistance to wear."),
    ("The baked bricks in the Great Bath were bound together with __________ mortar.", "gypsum", "Gypsum mortar served as the binding agent between bricks."),
    ("The waterproofing agent applied to the Great Bath was natural __________.", "bitumen", "Bitumen (asphalt/tar) was applied to seal the bricks."),
    ("The base weight unit (ratio 16) was equivalent to __________ grams.", "13.63", "The basic unit weight corresponds to 13.63 grams."),
    ("The interlocking brick pattern used by Harappans is called the __________ bond.", "English", "The English bond pattern alternates headers and stretchers for strength."),
    ("The square Assembly Hall at Mohenjo-daro was supported by __________ brick pillars.", "twenty", "Twenty square brick pillars arranged in four rows supported the roof."),
    ("Granaries featured under-floor __________ ducts to protect grain from dampness.", "air ventilation", "Air ventilation ducts circulated air beneath the granary floor.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मानक हड़प्पा ईंटों की लंबाई, चौड़ाई और मोटाई का अनुपात __________ था।", "4:2:1", "ईंटों का अनुपात हमेशा 4:2:1 होता था (जैसे 28 x 14 x 7 सेमी)।"),
    ("हड़प्पा के घनाकार व्यापारिक बाट __________ नामक पत्थर से बनाए जाते थे।", "चर्ट", "बाट बनाने के लिए घिसावट रोधी कठोर चर्ट पत्थर का प्रयोग किया जाता था।"),
    ("विशाल स्नानागार की ईंटों को जोड़ने के लिए __________ के गारे का उपयोग होता था।", "जिप्सम", "ईंटों को आपस में चिपकाने के लिए जिप्सम के गारे का प्रयोग किया जाता था।"),
    ("विशाल स्नानागार के भीतर पानी रोकने के लिए प्रयुक्त सीलेंट प्राकृतिक __________ था।", "डामर", "प्राकृतिक डामर (बिटुमेन/तारकोल) की सील पानी का रिसाव रोकती थी।"),
    ("हड़प्पा बाटों की आधार इकाई (अनुपात 16) __________ ग्राम के समतुल्य थी।", "13.63", "आधार इकाई का भार 13.63 ग्राम था।"),
    ("दीवारों के निर्माण में ईंटें फंसाकर लगाने की पद्धति को __________ बांड कहते हैं।", "इंग्लिश", "इंटरलॉकिंग प्रणाली को इंग्लिश बांड (English bond) कहा जाता है।"),
    ("मोहनजोदड़ो के वर्गाकार सभा भवन की छत __________ खंभों पर टिकी हुई थी।", "बीस", "सभा भवन में 20 ईंटों के स्तंभ थे जो चार कतारों में व्यवस्थित थे।"),
    ("सीलन से अनाज को बचाने के लिए अन्नागारों के नीचे __________ के रास्ते बनाए जाते थे।", "हवा निकासी", "हवा निकासी (air ventilation) के रास्तों से अनाज सूखा रहता था।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the civic structures with their core functions or characteristics:",
        "items": [{"left": "I. The Great Bath", "key": "A"}, {"left": "II. The Great Granary", "key": "B"}, {"left": "III. The Assembly Hall", "key": "C"}],
        "options": [{"val": "A", "text": "A. Ritual purification and bitumen-sealed pool"}, {"val": "B", "text": "B. Ventilation-ducted food security storage"}, {"val": "C", "text": "C. Pillared civic assembly and council chamber"}],
        "sol": "Great Bath is for ritual purification, Granary for storage with air ducts, and Assembly Hall for council meetings."
    },
    {
        "type": "Match the Following",
        "q": "Match the metrological components with their descriptions:",
        "items": [{"left": "I. Chert cubical weights", "key": "A"}, {"left": "II. English bond brickwork", "key": "B"}, {"left": "III. Binary metrology scale", "key": "C"}],
        "options": [{"val": "A", "text": "A. Standardized heavy stone units of trade"}, {"val": "B", "text": "B. Interlocking stretchers and headers for wall strength"}, {"val": "C", "text": "C. Geometric progression (1, 2, 4, 8... 64) for small weights"}],
        "sol": "Chert weights are trade units, English bond is interlocking brickwork, and binary scale is geometric progression."
    },
    {
        "type": "Match the Following",
        "q": "Match the site locations with their architectural landmarks:",
        "items": [{"left": "I. Mohenjo-daro Citadel", "key": "A"}, {"left": "II. Harappa River-front", "key": "B"}, {"left": "III. Lothal Dockyard basin", "key": "C"}],
        "options": [{"val": "A", "text": "A. Great Bath, Collegiate Building, and Assembly Hall"}, {"val": "B", "text": "B. Double rows of six granaries and circular platforms"}, {"val": "C", "text": "C. Paki-brick tidal basin connected to Sabarmati river"}],
        "sol": "Mohenjo-daro has the Great Bath, Harappa has the double row of granaries, and Lothal has the dockyard basin."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "सार्वजनिक संरचनाओं को उनके मुख्य कार्यों और विशेषताओं से सुमेलित करें:",
        "items": [{"left": "I. विशाल स्नानागार (Great Bath)", "key": "A"}, {"left": "II. विशाल अन्नागार (Granary)", "key": "B"}, {"left": "III. सभा भवन (Assembly Hall)", "key": "C"}],
        "options": [{"val": "A", "text": "A. अनुष्ठानिक शुद्धि और डामर की सील वाला जलाशय"}, {"val": "B", "text": "B. हवा निकासी रास्तों से युक्त खाद्य सुरक्षा भंडार"}, {"val": "C", "text": "C. स्तंभों वाला नागरिक परिषद और सामूहिक सभा स्थल"}],
        "sol": "विशाल स्नानागार अनुष्ठानिक शुद्धि के लिए, अन्नागार हवादार अनाज भंडार के लिए, और सभा भवन परिषद बैठकों के लिए था।"
    },
    {
        "type": "Match the Following",
        "q": "मापन घटकों को उनके सटीक विवरण से सुमेलित करें:",
        "items": [{"left": "I. चर्ट के घनाकार बाट", "key": "A"}, {"left": "II. इंग्लिश बांड चिनाई", "key": "B"}, {"left": "III. द्वि-आधारी माप प्रणाली", "key": "C"}],
        "options": [{"val": "A", "text": "A. व्यापार के लिए प्रयुक्त मानकीकृत पत्थर के बाट"}, {"val": "B", "text": "B. दीवारों की मजबूती के लिए ईंटें फंसाकर लगाने की चिनाई"}, {"val": "C", "text": "C. छोटे बाटों के लिए ज्यामितीय प्रगति (1, 2, 4, 8... 64)"}],
        "sol": "चर्ट के बाट व्यापार के मानकीकृत बाट हैं, इंग्लिश बांड इंटरलॉकिंग चिनाई है, और द्वि-आधारी माप ज्यामितीय प्रगति है।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके प्रमुख वास्तुशिल्प स्मारकों से सुमेलित करें:",
        "items": [{"left": "I. मोहनजोदड़ो किला", "key": "A"}, {"left": "II. हड़प्पा नदी तट", "key": "B"}, {"left": "III. लोथल गोदी बाड़ा", "key": "C"}],
        "options": [{"val": "A", "text": "A. विशाल स्नानागार, कॉलेज भवन और सभा भवन"}, {"val": "B", "text": "B. छह-छह अन्नागारों की दो कतारें और अनाज कूटने के चबूतरे"}, {"val": "C", "text": "C. साबरमती नदी से जुड़ा पकी ईंटों का ज्वारीय गोदी बेसिन"}],
        "sol": "मोहनजोदड़ो किले पर विशाल स्नानागार है, हड़प्पा में अन्नागारों की कतारें हैं, और लोथल में गोदी बाड़ा मिला है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the standardized length-to-width-to-thickness ratio of Harappan bricks?", "The ratio is 4:2:1."),
    ("Which hard, fine-grained mineral was used to carve trade weights?", "Chert."),
    ("What was the weight value in grams of the primary base weight (ratio 16)?", "Approximately 13.63 grams."),
    ("How did Harappan builders ensure the Great Bath pool was leak-proof?", "By coating the bricks with a layer of natural bitumen (asphalt)."),
    ("What is the term for the interlocking brick masonry technique used for walls?", "English bond."),
    ("Why were Harappan granaries raised on high brick foundations?", "To keep stored grain dry, protected from floods and ground moisture."),
    ("How many pillars supported the roof of the square Assembly Hall at Mohenjo-daro?", "20 brick pillars in 4 rows of 5."),
    ("What was the probable purpose of the Collegiate Building at Mohenjo-daro?", "It served as a priestly commune, academic college, or municipal office complex.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा सभ्यता में ईंटों की लंबाई, चौड़ाई और मोटाई का मानक अनुपात क्या था?", "अनुपात 4:2:1 था।"),
    ("व्यापारिक बाटों को तराशने के लिए किस कठोर सूक्ष्म-क्रिस्टलीय खनिज का उपयोग किया जाता था?", "चर्ट (Chert) का।"),
    ("आधार वजन इकाई (अनुपात 16) का वजन आधुनिक माप में कितने ग्राम था?", "लगभग 13.63 ग्राम।"),
    ("हड़प्पा वासियों ने विशाल स्नानागार के कुंड को रिसाव-रोधी कैसे बनाया?", "पकी ईंटों पर प्राकृतिक डामर (बिटुमेन) की एक मोटी परत चढ़ाकर।"),
    ("दीवारों के निर्माण में ईंटों को आपस में फंसाने की तकनीक को क्या कहा जाता है?", "इंग्लिश बांड (English bond)।"),
    ("हड़प्पा के अन्नागारों को ईंटों के ऊंचे चबूतरों पर क्यों बनाया जाता था?", "ताकि अनाज बाढ़ के पानी और जमीन की सीलन से बचा रहे।"),
    ("मोहनजोदड़ो के वर्गाकार सभा भवन की छत को सहारा देने के लिए कितने स्तंभ थे?", "20 ईंटों के स्तंभ (5-5 के 4 कतारों में)।"),
    ("मोहनजोदड़ो में मिले कॉलेज भवन (Collegiate Building) का संभावित उपयोग क्या था?", "यह पुरोहितों के रहने का स्थान, शैक्षणिक कॉलेज या नगरपालिका कार्यालय रहा होगा।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Harappan bricks across all settlements followed a highly uniform ratio of 4:2:1.\nReason (R): This uniform standardisation implies a central administrative authority coordinating civic standards.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Great Bath of Mohenjo-daro was made watertight using natural bitumen.\nReason (R): Natural bitumen is a naturally occurring water-resistant sealant that adheres strongly to bricks.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappan weights followed a binary system for small transactions and a decimal system for higher values.\nReason (R): The dual scale allowed for highly precise micro-measurements and simplified calculations for large trade shipments.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Assembly Hall at Mohenjo-daro functioned as a temple for the chief deity.\nReason (R): No religious idols, altars, or ritual items have been excavated inside the Assembly Hall.", 3, "A is false because it was not a temple. R is true."),
    ("Assertion (A): Granaries were constructed on elevated brick podiums with under-floor air ducts.\nReason (R): Circulating air kept the floor dry, preventing grain from rotting due to moisture and mildew.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappans built walls using the English bond pattern to save bricks.\nReason (R): The English bond is an interlocking laying technique that maximizes structural strength.", 3, "A is false because English bond was for strength, not to save bricks. R is true."),
    ("Assertion (A): Harappan trade weights were carved out of soft steatite soapstone.\nReason (R): Steatite is easily carved and was preferred for seals, whereas trade weights required hard, wear-resistant chert.", 3, "A is false because weights were chert, not steatite. R is true."),
    ("Assertion (A): The Collegiate Building was a residential palace of a single monarch.\nReason (R): The presence of a large courtyard, multiple rooms, and proximity to the Great Bath suggests it was a priestly or administrative complex.", 3, "A is false because no monarchy is archaeologically verified. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): सभी हड़प्पा बस्तियों में ईंटों का अनुपात अत्यधिक मानकीकृत 4:2:1 था।\nकारण (R): यह एकरूपता एक सुव्यवस्थित प्रशासनिक प्राधिकारी द्वारा नागरिक मानकों के नियमन को दर्शाती है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो के विशाल स्नानागार को प्राकृतिक डामर से जल-रोधी बनाया गया था।\nकारण (R): प्राकृतिक डामर पानी को रोकने वाला सीलेंट है जो ईंटों के साथ मजबूती से चिपक जाता है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के बाटों में छोटे वजन के लिए द्वि-आधारी और बड़े मूल्यों के लिए दशमलव प्रणाली थी।\nकारण (R): इस दोहरी प्रणाली ने सूक्ष्म मापन को सटीक बनाया और भारी माल की गणना को सरल किया।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मोहनजोदड़ो का सभा भवन मुख्य देवता का एक मंदिर था।\nकारण (R): सभा भवन के भीतर से कोई भी धार्मिक मूर्तियां, वेदी या पूजा के सामान नहीं मिले हैं।", 3, "A असत्य है क्योंकि यह मंदिर नहीं था। R सत्य है।"),
    ("कथन (A): अन्नागार ऊंचे ईंटों के चबूतरे पर हवा के रास्तों (air ducts) के साथ बनाए जाते थे।\nकारण (R): हवा का निरंतर प्रवाह फर्श को सूखा रखता था जिससे अनाज सीलन और फफूंद से सड़ता नहीं था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा वासियों ने ईंटें बचाने के लिए इंग्लिश बांड चिनाई तकनीक अपनाई थी।\nकारण (R): इंग्लिश बांड ईंट बिछाने की इंटरलॉकिंग विधि है जो दीवार को अधिकतम भार वहन क्षमता देती है।", 3, "A असत्य है क्योंकि यह मजबूती के लिए था, ईंटें बचाने के लिए नहीं। R सत्य है।"),
    ("कथन (A): हड़प्पा के व्यापारिक बाटों को तराशने के लिए नरम सेलखड़ी पत्थर का उपयोग होता था।\nकारण (R): सेलखड़ी नरम होता है और मुहरों के लिए उपयुक्त था, जबकि बाटों के लिए घिसावट रोधी कठोर चर्ट चाहिए था।", 3, "A असत्य है क्योंकि बाट चर्ट के बने थे, सेलखड़ी के नहीं। R सत्य है।"),
    ("कथन (A): कॉलेज भवन (Collegiate Building) एक शक्तिशाली राजा का निजी आवासीय महल था।\nकारण (R): बड़े आंगन, कई कमरों और स्नानागार के निकट इसकी स्थिति संकेत करती है कि यह पुरोहितों या प्रशासनिक अधिकारियों का परिसर था।", 3, "A असत्य है क्योंकि राजशाही का कोई पुरातात्विक प्रमाण नहीं मिला है। R सत्य है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Harappan bricks:\n1. The standardized ratio of 4:2:1 was applied to both burnt and mud bricks.\n2. Standard domestic brick sizes were typically 28cm x 14cm x 7cm.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct: both brick types followed the ratio, and 28x14x7 was the standard size."),
    ("Consider the following statements regarding metrology:\n1. Cubical weights were carved from chert blocks.\n2. The base weight unit ratio 16 was equivalent to 13.63 grams.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the material and base weight of the metrological system."),
    ("Consider the following statements regarding the Great Bath:\n1. Gypsum mortar bound the brickwork together.\n2. Natural bitumen (asphalt) made the pool watertight.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, illustrating the mortar and waterproofing sealant of the Great Bath."),
    ("Consider the following statements regarding Mohenjo-daro structures:\n1. The pillared Assembly Hall featured twenty brick pillars.\n2. The Collegiate Building featured a gold-plated altar for ritual fire offerings.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: no gold-plated fire altars have been found there."),
    ("Consider the following statements regarding construction techniques:\n1. English bond interlocking pattern was used for laying walls.\n2. Granaries featured air vents to prevent dampness.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the English bond pattern and granary ventilation.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा की ईंटों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कच्चे और पके दोनों प्रकार के ईंटों के लिए 4:2:1 का अनुपात लागू किया गया था।\n2. घरों के लिए मानक ईंटों का आकार आमतौर पर 28 सेमी x 14 सेमी x 7 सेमी था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं: दोनों प्रकार की ईंटें अनुपात का पालन करती थीं और 28x14x7 मानक आकार था।"),
    ("हड़प्पा बाट-माप के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. घनाकार बाट चर्ट पत्थर के खंडों से बनाए जाते थे।\n2. मूल बाट इकाई अनुपात 16 का मान लगभग 13.63 ग्राम के बराबर था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और बाटों की सामग्री तथा आधार वजन मान को स्पष्ट करते हैं।"),
    ("विशाल स्नानागार के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. ईंटों की चिनाई को जोड़ने के लिए जिप्सम गारे का प्रयोग किया गया था।\n2. कुंड को जल-रोधी बनाने के लिए प्राकृतिक डामर (बिटुमेन) का उपयोग हुआ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं और स्नानागार के गारे तथा जल-रोधी परत की जानकारी देते हैं।"),
    ("मोहनजोदड़ो की संरचनाओं के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. स्तंभों वाले सभा भवन में ईंटों के कुल बीस खंभे मिले हैं।\n2. कॉलेज भवन में अग्नि पूजा के लिए सोने की परत चढ़ी एक वेदी मिली है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि वहाँ सोने की परत वाली वेदी का कोई साक्ष्य नहीं है।"),
    ("हड़प्पा निर्माण तकनीकों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. दीवारें बनाने के लिए इंग्लिश बांड की इंटरलॉकिंग चिनाई की जाती थी।\n2. अन्नागारों में सीलन रोकने के लिए हवा निकासी के छेद बनाए जाते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो इंग्लिश बांड चिनाई और अन्नागार की हवादार तकनीक का वर्णन करते हैं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Harappan walls utilize the English bond laying pattern?", "Because alternating headers and stretchers prevents vertical joints from aligning, distributing loads evenly and maximizing wall strength."),
    ("Why were granaries built on raised platforms with under-floor air vents?", "To circulate air beneath stored grain, protecting it from groundwater moisture, flood inundation, and mildew rot."),
    ("Why was chert selected as the primary material for trade weights?", "Chert is a highly dense, hard quartz that resists chipping, scratching, and wear, ensuring weights remained highly accurate and tamper-proof over time.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा की दीवारों में इंग्लिश बांड चिनाई पद्धति का उपयोग क्यों किया गया?", "क्योंकि एकांतर रूप से लंबाई और चौड़ाई के बल ईंटें रखने से जोड़ एक सीध में नहीं आते, जिससे भार बराबर बंटता है और दीवार अत्यधिक मजबूत बनती है।"),
    ("अन्नागारों को ऊंचे चबूतरों और फर्श के नीचे हवा निकासी रास्तों के साथ क्यों बनाया जाता था?", "अनाज के नीचे हवा का संचार करने के लिए, जिससे उसे भूजल की नमी, बाढ़ के पानी और फफूंद लगने से बचाया जा सके।"),
    ("व्यापारिक बाटों के लिए मुख्य रूप से चर्ट पत्थर को ही क्यों चुना गया था?", "चर्ट एक अत्यंत सघन और कठोर क्वार्ट्ज खनिज है, जिसमें घिसावट या खरोंच नहीं आती, जिससे बाटों की शुद्धता लंबे समय तक सुरक्षित रहती थी और हेरफेर संभव नहीं था।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did the metrology system combine binary and decimal scales?", "Lower weights progressed geometrically (1, 2, 4, 8, 16, 32, 64) for precise local retail trade, while higher weights transitioned to decimal scales (100, 200, 500...) for bulk commercial goods."),
    ("How was the Great Bath filled and drained?", "It was filled with fresh water drawn from a brick well in an adjacent room and drained via a corbelled brick sewer at the bottom for periodic cleaning."),
    ("How did standard brick ratios reflect political or social organisation?", "Adhering to a strict 4:2:1 ratio for millions of bricks across settlements separated by 1000 miles shows a highly centralized regulation of construction standards.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा बाट प्रणाली में द्वि-आधारी और दशमलव पैमानों को किस प्रकार संयोजित किया गया था?", "छोटे लेन-देन के लिए बाट द्वि-आधारी श्रेणी (1, 2, 4, 8... 64) में चलते थे, जबकि थोक व्यापार और बड़े वजनों के लिए वे दशमलव श्रेणी (100, 200, 500...) में बदल जाते थे।"),
    ("विशाल स्नानागार को किस प्रकार भरा और खाली किया जाता था?", "कुंड को पास के कमरे में बने एक बड़े कुएं से पानी खींचकर भरा जाता था और सफाई के लिए तल में बने एक बड़े मेहराबदार सीवर नाले से पानी बाहर निकाला जाता था।"),
    ("मानक ईंटों के अनुपात ने राजनीतिक या सामाजिक संगठन को कैसे दर्शाया?", "हजार मील दूर फैली विभिन्न बस्तियों में लाखों ईंटों के निर्माण में 4:2:1 के अनुपात का कड़ाई से पालन होना एक अत्यधिक कुशल केंद्रीय मानक नियामक तंत्र की पुष्टि करता है।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Great Bath's Waterproofing Engineering", "The Great Bath pool features a floor of baked bricks set on edge, bound with gypsum mortar. Behind this layout sat a brick wall lined with a 2cm thick layer of natural asphalt (bitumen), backed by mud-brick backing, demonstrating advanced waterproofing capabilities."),
    ("Case Study: Harappan Chert Metrological Standardisation", "Archaeologists discovered that weights from Harappa, Mohenjo-daro, and Lothal were mathematically identical. Carved from chert as polished cubes, these weights prove a highly regulated economic system that facilitated dispute-free interstate commerce and tax assessment."),
    ("Case Study: The Granaries of Harappa and Mohenjo-daro", "The Great Granary at Harappa consists of 12 rooms in two rows. Mohenjo-daro's granary features 27 brick platforms with wooden superstructure sockets. Both were situated near rivers, showing a state-managed food reserve and trade logistics network.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: विशाल स्नानागार की जल-रोधी इंजीनियरिंग", "विशाल स्नानागार के फर्श पर खड़ी ईंटें बिछाई गई थीं जिन्हें जिप्सम गारे से जोड़ा गया था। इसके पीछे एक ईंट की दीवार पर 2 सेमी मोटी प्राकृतिक डामर (बिटुमेन) की परत लगाई गई थी, जिसके बाहर कच्ची ईंटों का सहारा था, जो उत्कृष्ट जल-रोधी इंजीनियरिंग का प्रमाण है।"),
    ("केस स्टडी: चर्ट बाटों का मानकीकरण", "पुराविदों ने पाया कि हड़प्पा, मोहनजोदड़ो और लोथल से मिले बाट गणितीय रूप से बिल्कुल समान थे। चर्ट से तराशे गए ये चिकने घनाकार बाट एक एकीकृत कर प्रणाली और विवाद-मुक्त अंतर-राज्यीय वाणिज्य की पुष्टि करते हैं।"),
    ("केस स्टडी: हड़प्पा और मोहनजोदड़ो के अन्नागार", "हड़प्पा के अन्नागार में दो कतारों में 12 कमरे हैं, जबकि मोहनजोदड़ो में लकड़ी की छत के सुरागों से युक्त 27 चबूतरे मिले हैं। नदी के पास इनकी स्थिति अनाज के भंडारण और जलीय व्यापार की सुदृढ़ व्यवस्था को दर्शाती है।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Teach Concept: The English Bond Construction Method", "Explain how laying bricks in alternating rows of stretchers (lengthwise) and headers (crosswise) creates an interlocking network. This prevents continuous vertical joints, making the wall highly stable against seismic activity and heavy loads, a standard still used today."),
    ("Teach Concept: Binary vs. Decimal Metrology", "Teach how the system utilized a dual progression. For small trade (spices, precious metals), weights followed binary doubles: 1, 2, 4, 8, 16 (basic unit 13.63g), up to 64. For bulk cargo (grains, cotton), it transitioned to decimal scales (160, 200, 320, 640, 1600...), combining accuracy with scale."),
    ("Teach Concept: Granary Ventilation & Air Flow Engineering", "Explain the thermodynamic layout. Grains spoil when trapped with moisture. By building granary podiums high with deep wooden floor vents, the wind blew through the channels beneath the grain crates, carrying away rising ground humidity and preventing mold growth.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा समझाएं (Teach Concept): इंग्लिश बांड चिनाई पद्धति", "समझाएं कि ईंटों को एक कतार में लंबाई में (stretchers) और अगली कतार में चौड़ाई में (headers) रखने से इंटरलॉकिंग जाल कैसे बनता है। यह खड़े जोड़ों को एक सीध में आने से रोकता है, जिससे भूकंप या अत्यधिक भार में भी दीवारें नहीं गिरतीं।"),
    ("अवधारणा समझाएं (Teach Concept): द्वि-आधारी बनाम दशमलव मापन प्रणाली", "समझाएं कि कैसे हड़प्पा वासियों ने दोहरी व्यवस्था का उपयोग किया। छोटे बाट (मसाले, धातु) द्वि-आधारी दोहरे प्रतिरूप: 1, 2, 4, 8, 16 (आधार 13.63 ग्राम), 32, 64 तक थे। बड़े अनाज या सूती कपड़ों के थोक माल के लिए वे दशमलव श्रेणी (160, 200, 320, 640, 1600...) में बदल जाते थे।"),
    ("अवधारणा समझाएं (Teach Concept): अन्नागारों में वायु-संचार की इंजीनियरिंग", "समझाएं कि नमी मिलने पर अनाज सड़ जाता है। अन्नागार के चबूतरे ऊंचे बनाकर उनके बीच गहरी गलियां छोड़ी गई थीं। जब हवा इन गलियों से गुजरती थी, तो वह फर्श के नीचे की नमी को सोख लेती थी, जिससे अनाज फफूंद लगने से बच जाता था।")
]:
    s3_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})


# Load content files and inject
with open(ENG_PATH, "r", encoding="utf-8") as f:
    eng_data = json.load(f)

with open(HIN_PATH, "r", encoding="utf-8") as f:
    hin_data = json.load(f)

# Inject Section 1
eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin

# Inject Section 2
eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin

# Inject Section 3
eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng
hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin

# Save files
with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Mastery Zone questions injected successfully!")
