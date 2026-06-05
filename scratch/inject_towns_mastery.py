import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Important-Urban-Towns\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Important-Urban-Towns\hi\content.json"

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
# SECTION 1: METROPOLITAN GIANTS (HARAPPA, MOHENJO-DARO, RAKHIGARHI)
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which soft soapstone was predominantly used by Harappan artisans to carve the bust of the Priest-King?", ["Steatite", "Chert", "Carnelian", "Lapis Lazuli"], 0, "Steatite (soapstone) was used because it is soft and easy to carve, then hardens when baked."),
    ("The Great Bath of Mohenjo-daro was made watertight by applying a layer of which material?", ["Natural bitumen (tar)", "Lime mortar", "Glazed ceramic paste", "Cedar wood resin"], 0, "A layer of natural bitumen (asphalt/tar) was applied to prevent water leakage."),
    ("At which metropolitan site were parallel rows of circular brick threshing platforms discovered outside the citadel?", ["Harappa", "Mohenjo-daro", "Rakhigarhi", "Lothal"], 0, "Harappa yielded circular brick platforms used for threshing grains near its granaries."),
    ("Which site features nine mounds and is currently recognized as the largest geographic settlement of the IVC?", ["Rakhigarhi", "Harappa", "Mohenjo-daro", "Dholavira"], 0, "Rakhigarhi in Haryana covers over 350-500 hectares, making it the largest IVC site."),
    ("The large pillared Assembly Hall and Collegiate Building were excavated in the Citadel of which city?", ["Mohenjo-daro", "Harappa", "Rakhigarhi", "Banawali"], 0, "Both the Assembly Hall and the Collegiate Building are prominent public monuments at Mohenjo-daro.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("पुरोहित-राजा (Priest-King) की मूर्ति को तराशने के लिए हड़प्पा के कारीगरों द्वारा किस नरम पत्थर का मुख्य रूप से उपयोग किया गया था?", ["सेलखड़ी (Steatite)", "चर्ट (Chert)", "अकीक (Carnelian)", "लाजवर्त (Lapis Lazuli)"], 0, "सेलखड़ी (steatite/soapstone) का उपयोग किया गया था क्योंकि यह नरम होता है और तराशने के बाद गर्म करने पर कठोर हो जाता है।"),
    ("मोहनजोदड़ो के विशाल स्नानागार (Great Bath) को जल-रोधी बनाने के लिए किस सामग्री की परत लगाई गई थी?", ["प्राकृतिक डामर (तारकोल/bitumen)", "चूने का गारा", "चमकदार सिरेमिक लेप", "देवदार की लकड़ी का राल"], 0, "पानी के रिसाव को रोकने के लिए प्राकृतिक डामर (बिटुमेन) की एक परत लगाई गई थी।"),
    ("किले के बाहर अनाज गाहने (threshing) के लिए ईंटों के गोलाकार चबूतरे किस महानगर में खोजे गए थे?", ["हड़प्पा", "मोहनजोदड़ो", "राखीगढ़ी", "लोथल"], 0, "हड़प्पा से अन्नागारों के पास अनाज गाहने के लिए प्रयुक्त गोलाकार ईंटों के चबूतरे मिले हैं।"),
    ("किस स्थल पर नौ टीले मिले हैं और इसे वर्तमान में सिंधु सभ्यता का सबसे बड़ा भौगोलिक स्थल माना जाता है?", ["राखीगढ़ी", "हड़प्पा", "मोहनजोदड़ो", "धोलावीरा"], 0, "हरियाणा का राखीगढ़ी 350-500 हेक्टेयर से अधिक में फैला है, जो इसे सबसे बड़ा स्थल बनाता है।"),
    ("किस शहर के किले (Citadel) में विशाल स्तंभों वाला सभा भवन (Assembly Hall) और कॉलेज भवन खोजा गया था?", ["मोहनजोदड़ो", "हड़प्पा", "राखीगढ़ी", "बनावली"], 0, "सभा भवन और कॉलेज भवन मोहनजोदड़ो के प्रमुख सार्वजनिक स्मारक हैं।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the archaeological findings associated with Harappa: (Select all that apply)", ["Cemetery R-37 with wooden coffin burial", "Circular brick threshing platforms", "Rows of granaries outside the citadel", "The Great Bath"], [0, 1, 2], "Cemetery R-37, circular platforms, and granary rows are at Harappa. The Great Bath is at Mohenjo-daro."),
    ("Identify the public monuments located on the Citadel of Mohenjo-daro: (Select all that apply)", ["The Great Bath", "The Great Granary", "The pillared Assembly Hall", "A massive brick dockyard"], [0, 1, 2], "The Great Bath, Great Granary, and Assembly Hall are at Mohenjo-daro. The dockyard is at Lothal."),
    ("Which features characterize the metropolitan town planning of Rakhigarhi? (Select all that apply)", ["Fortified mounds and citadel structure", "Standardized brick sizes", "Skeletal remains yielding clean DNA samples", "Radial street layout"], [0, 1, 2], "Rakhigarhi features citadels, standard bricks, and genetic cemeteries. Radial streets are typical of Banawali."),
    ("Which elements indicate a standardized municipal authority in these metropolises? (Select all that apply)", ["Grid-patterned wide main streets", "Standardized brick ratios of 4:2:1", "Covered brick drains with inspection chambers", "Monarchial palaces with stone thrones"], [0, 1, 2], "Street grids, standardized brick ratios, and sewerage show municipal coordination. No palaces or thrones exist."),
    ("Select the characteristics of the bronze Dancing Girl figurine: (Select all that apply)", ["Made using the solid lost-wax casting method", "Left arm covered with bangles", "Depicts a young woman in a tribhanga pose", "Carved from a single block of soft steatite"], [0, 1, 2], "The Dancing Girl is bronze (lost-wax), wears arm bangles, and stands in tribhanga. It is metal, not steatite.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा से जुड़े पुरातात्विक अवशेषों का चयन करें: (सभी लागू विकल्प चुनें)", ["लकड़ी के ताबूत शवाधान वाला कब्रिस्तान R-37", "ईंटों के गोलाकार चबूतरे", "किले के बाहर अन्नागारों की कतारें", "विशाल स्नानागार (Great Bath)"], [0, 1, 2], "कब्रिस्तान R-37, गोलाकार चबूतरे और अन्नागार हड़प्पा में हैं। विशाल स्नानागार मोहनजोदड़ो में है।"),
    ("मोहनजोदड़ो के किले पर स्थित सार्वजनिक स्मारकों की पहचान करें: (सभी लागू विकल्प चुनें)", ["विशाल स्नानागार (Great Bath)", "विशाल अन्नागार (Great Granary)", "स्तंभों वाला सभा भवन", "ईंटों का विशाल गोदी बाड़ा"], [0, 1, 2], "विशाल स्नानागार, अन्नागार और सभा भवन मोहनजोदड़ो में हैं। गोदी बाड़ा लोथल में है।"),
    ("राखीगढ़ी के नगर नियोजन की विशेषताएँ कौन सी हैं? (सभी लागू विकल्प चुनें)", ["किलेबंदी वाले टीले और किला संरचना", "मानकीकृत ईंटों का आकार", "डीएनए देने वाले कंकाल अवशेष", "अरीय (radial) सड़कों का लेआउट"], [0, 1, 2], "राखीगढ़ी में टीले, मानक ईंटें और कंकाल कब्रिस्तान हैं। अरीय सड़कें बनावली की विशेषता हैं।"),
    ("इन महानगरों में मानकीकृत नागरिक सत्ता का संकेत किन तत्वों से मिलता है? (सभी लागू विकल्प चुनें)", ["समकोण पर काटती चौड़ी सड़कें", "4:2:1 के अनुपात वाली मानक ईंटें", "निरीक्षण गृहों वाली ढकी नालियां", "पत्थर के सिंहासनों वाले शाही महल"], [0, 1, 2], "सड़कों का जाल, मानक ईंटें और नालियां नागरिक सत्ता दर्शाती हैं। यहाँ कोई राजमहल या सिंहासन नहीं मिले हैं।"),
    ("कांस्य की नर्तकी (Dancing Girl) की मूर्ति की विशेषताएँ चुनें: (सभी लागू विकल्प चुनें)", ["ठोस लुप्त-मोम ढलाई (lost-wax) विधि से निर्मित", "बायां हाथ चूड़ियों से ढका हुआ", "त्रिभंग मुद्रा में खड़ी युवती का चित्रण", "नरम सेलखड़ी के एक खंड से तराशी गई"], [0, 1, 2], "नर्तकी ठोस कांस्य (लुप्त-मोम) से बनी है, बायां हाथ चूड़ियों से ढका है और त्रिभंग मुद्रा में है। यह धातु की है, सेलखड़ी की नहीं।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Great Bath is located at Harappa.", False, "False. The Great Bath is located at Mohenjo-daro."),
    ("Rakhigarhi is situated along the dry channel of the Drishadvati River in Haryana.", True, "True. Rakhigarhi is in Hisar, Haryana, along the dry Drishadvati channel."),
    ("The Priest-King statue is made of bronze.", False, "False. The Priest-King statue is carved from steatite (soapstone)."),
    ("Harappa is situated on the left bank of the Ravi River.", True, "True. Harappa lies along the left bank of the dry bed of the Ravi River."),
    ("The Great Granary is located in the Lower Town of Mohenjo-daro.", False, "False. It is located on the Citadel mound."),
    ("Cemetery R-37 is located at Rakhigarhi.", False, "False. Cemetery R-37 is located at Harappa."),
    ("Recent DNA studies of Rakhigarhi skeletons support the theory of massive Aryan invasions.", False, "False. The DNA analysis shows genetic continuity and indigenous ancestries, contradicting invasion theories."),
    ("Steatite is a hard igneous volcanic stone.", False, "False. Steatite is a very soft talc-rich metamorphic soapstone.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विशाल स्नानागार (Great Bath) हड़प्पा में स्थित है।", False, "असत्य। विशाल स्नानागार मोहनजोदड़ो में स्थित है।"),
    ("राखीगढ़ी हरियाणा में दृषद्वती नदी के सूखे मार्ग पर स्थित है।", True, "सत्य। राखीगढ़ी हरियाणा के हिसार जिले में सूखी हुई दृषद्वती नदी के किनारे है।"),
    ("पुरोहित-राजा की मूर्ति कांसे की बनी है।", False, "असत्य। पुरोहित-राजा की मूर्ति सेलखड़ी (steatite/soapstone) से बनी है।"),
    ("हड़प्पा रावी नदी के बाएं (left) तट पर स्थित है।", True, "सत्य। हड़प्पा रावी नदी के सूखे मार्ग के बाएं किनारे पर स्थित है।"),
    ("विशाल अन्नागार मोहनजोदड़ो के निचले नगर (Lower Town) में स्थित है।", False, "असत्य। यह किले (Citadel) के टीले पर स्थित है।"),
    ("कब्रिस्तान R-37 राखीगढ़ी में स्थित है।", False, "असत्य। कब्रिस्तान R-37 हड़प्पा में स्थित है।"),
    ("राखीगढ़ी के कंकालों के हालिया डीएनए अध्ययनों ने बड़े पैमाने पर आर्य आक्रमण के सिद्धांत का समर्थन किया है।", False, "असत्य। डीएनए विश्लेषण आनुवंशिक निरंतरता और स्वदेशी उत्पत्ति दर्शाता है, जो आक्रमण के सिद्धांत को खारिज करता है।"),
    ("सेलखड़ी (steatite) एक कठोर आग्नेय ज्वालामुखीय पत्थर है।", False, "असत्य। सेलखड़ी एक बहुत ही नरम रूपांतरित साबुन पत्थर (soapstone) है।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The Great Bath is situated at the site of __________.", "Mohenjo-daro", "The Great Bath is at Mohenjo-daro."),
    ("The standardized Harappan brick ratio is __________.", "4:2:1", "The brick dimensions followed a ratio of 4:2:1 (length:width:thickness)."),
    ("Cemetery R-37 is located at the site of __________.", "Harappa", "Cemetery R-37 was excavated at Harappa."),
    ("The largest Harappan site by area is __________.", "Rakhigarhi", "Rakhigarhi is the largest site, covering over 350 hectares."),
    ("The Priest-King bust is carved from a soft stone called __________.", "steatite", "The bust is carved from steatite soapstone."),
    ("The Dancing Girl bronze statue was manufactured using the __________ method.", "lost-wax", "The cire perdue (lost-wax) method was used for bronze casting."),
    ("Rakhigarhi is situated in the modern state of __________.", "Haryana", "Rakhigarhi is in Hisar district, Haryana."),
    ("Harappa is located on the dry bed of the __________ River.", "Ravi", "Harappa is located on the Ravi River, a major tributary of the Indus.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("विशाल स्नानागार (Great Bath) __________ नामक स्थल पर स्थित है।", "मोहनजोदड़ो", "विशाल स्नानागार मोहनजोदड़ो में है।"),
    ("मानकीकृत हड़प्पा ईंटों का अनुपात __________ है।", "4:2:1", "ईंटों का अनुपात 4:2:1 (लंबाई:चौड़ाई:मोटाई) था।"),
    ("कब्रिस्तान R-37 __________ नामक स्थल पर स्थित है।", "हड़प्पा", "कब्रिस्तान R-37 हड़प्पा में स्थित है।"),
    ("क्षेत्रफल की दृष्टि से सबसे बड़ा हड़प्पा स्थल __________ है।", "राखीगढ़ी", "राखीगढ़ी सबसे बड़ा स्थल है, जो 350 हेक्टेयर से अधिक में फैला है।"),
    ("पुरोहित-राजा की मूर्ति को __________ नामक एक नरम पत्थर से तराशा गया है।", "सेलखड़ी", "यह मूर्ति सेलखड़ी (steatite/soapstone) से बनी है।"),
    ("कांस्य की नर्तकी की मूर्ति का निर्माण __________ विधि का उपयोग करके किया गया था।", "लुप्त-मोम", "लुप्त-मोम (lost-wax/cire perdue) ढलाई विधि का उपयोग किया गया था।"),
    ("राखीगढ़ी आधुनिक भारत के __________ राज्य में स्थित है।", "हरियाणा", "राखीगढ़ी हरियाणा के हिसार जिले में है।"),
    ("हड़प्पा __________ नदी के शुष्क मार्ग पर स्थित है।", "रावी", "हड़प्पा रावी नदी के किनारे स्थित है।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the metropolitan public structures with their respective sites:",
        "items": [{"left": "I. The Great Bath", "key": "A"}, {"left": "II. Parallel Rows of Granaries", "key": "B"}, {"left": "III. Largest Cemetery Mounds", "key": "C"}],
        "options": [{"val": "A", "text": "A. Mohenjo-daro"}, {"val": "B", "text": "B. Harappa"}, {"val": "C", "text": "C. Rakhigarhi"}],
        "sol": "Great Bath is at Mohenjo-daro, rows of granaries at Harappa, and largest mounds at Rakhigarhi."
    },
    {
        "type": "Match the Following",
        "q": "Match the metropolitan artifacts with their materials:",
        "items": [{"left": "I. Priest-King Bust", "key": "A"}, {"left": "II. Dancing Girl Statue", "key": "B"}, {"left": "III. Threshing Platforms", "key": "C"}],
        "options": [{"val": "A", "text": "A. Steatite Soapstone"}, {"val": "B", "text": "B. Cast Bronze"}, {"val": "C", "text": "C. Baked Clay Bricks"}],
        "sol": "Priest-King is steatite, Dancing Girl is bronze, and threshing platforms are built of baked bricks."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their modern administrative districts:",
        "items": [{"left": "I. Harappa", "key": "A"}, {"left": "II. Mohenjo-daro", "key": "B"}, {"left": "III. Rakhigarhi", "key": "C"}],
        "options": [{"val": "A", "text": "A. Sahiwal (Punjab, Pakistan)"}, {"val": "B", "text": "B. Larkana (Sindh, Pakistan)"}, {"val": "C", "text": "C. Hisar (Haryana, India)"}],
        "sol": "Harappa is in Sahiwal, Mohenjo-daro in Larkana, and Rakhigarhi in Hisar."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "महानगरों की सार्वजनिक संरचनाओं को उनके संबंधित स्थलों से सुमेलित करें:",
        "items": [{"left": "I. विशाल स्नानागार (Great Bath)", "key": "A"}, {"left": "II. अन्नागारों की दो कतारें", "key": "B"}, {"left": "III. सबसे बड़ा टीला क्षेत्र", "key": "C"}],
        "options": [{"val": "A", "text": "A. मोहनजोदड़ो"}, {"val": "B", "text": "B. हड़प्पा"}, {"val": "C", "text": "C. राखीगढ़ी"}],
        "sol": "विशाल स्नानागार मोहनजोदड़ो में है, अन्नागारों की कतारें हड़प्पा में हैं, और सबसे बड़े टीले राखीगढ़ी में हैं।"
    },
    {
        "type": "Match the Following",
        "q": "महानगरों की कलाकृतियों को उनके निर्माण की सामग्रियों से सुमेलित करें:",
        "items": [{"left": "I. पुरोहित-राजा की मूर्ति", "key": "A"}, {"left": "II. नर्तकी की मूर्ति", "key": "B"}, {"left": "III. अनाज कूटने के चबूतरे", "key": "C"}],
        "options": [{"val": "A", "text": "A. सेलखड़ी (Steatite)"}, {"val": "B", "text": "B. ढला हुआ कांसा (Bronze)"}, {"val": "C", "text": "C. पकी मिट्टी की ईंटें"}],
        "sol": "पुरोहित-राजा सेलखड़ी से, नर्तकी कांसे से, और अनाज कूटने के चबूतरे पकी ईंटों से बने हैं।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके आधुनिक प्रशासनिक जिलों से सुमेलित करें:",
        "items": [{"left": "I. हड़प्पा", "key": "A"}, {"left": "II. मोहनजोदड़ो", "key": "B"}, {"left": "III. राखीगढ़ी", "key": "C"}],
        "options": [{"val": "A", "text": "A. साहीवाल (पंजाब, पाकिस्तान)"}, {"val": "B", "text": "B. लरकाना (सिंध, पाकिस्तान)"}, {"val": "C", "text": "C. हिसार (हरियाणा, भारत)"}],
        "sol": "हड़प्पा साहीवाल में है, मोहनजोदड़ो लरकाना में है, और राखीगढ़ी हिसार में है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the standard ratio of Harappan bricks used in wall construction?", "The ratio is 4:2:1 (length:width:thickness)."),
    ("Where was the famous steatite Priest-King bust discovered?", "It was excavated at Mohenjo-daro."),
    ("What material was applied to the Great Bath to make it watertight?", "A thick layer of natural bitumen (tar/asphalt) was applied."),
    ("On which river bank is Harappa located?", "It is situated on the left bank of the Ravi River."),
    ("In which Indian state is Rakhigarhi located?", "It is located in Haryana."),
    ("What is the approximate geographical area of Rakhigarhi?", "It covers over 350 to 500 hectares across nine mounds."),
    ("What type of burial found at Harappa is unique in the Indus Civilisation?", "A wooden coffin burial made of Himalayan cedar (deodar) wood."),
    ("Which site is often called the 'Mound of the Dead'?", "Mohenjo-daro (which literally translates to Mound of the Dead in Sindhi).")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("दीवारों के निर्माण के लिए प्रयुक्त हड़प्पा ईंटों का मानक अनुपात क्या है?", "अनुपात 4:2:1 (लंबाई:चौड़ाई:मोटाई) है।"),
    ("सेलखड़ी से बनी पुरोहित-राजा (Priest-King) की प्रसिद्ध मूर्ति कहाँ खोजी गई थी?", "इसे मोहनजोदड़ो में खोजा गया था।"),
    ("विशाल स्नानागार (Great Bath) को जल-रोधी बनाने के लिए किस सामग्री का उपयोग किया गया था?", "प्राकृतिक डामर (तारकोल/बिटुमेन) की एक मोटी परत लगाई गई थी।"),
    ("हड़प्पा किस नदी के तट पर स्थित है?", "यह रावी नदी के बाएं तट पर स्थित है।"),
    ("राखीगढ़ी भारत के किस राज्य में स्थित है?", "यह हरियाणा में स्थित है।"),
    ("राखीगढ़ी का अनुमानित भौगोलिक क्षेत्रफल कितना है?", "यह नौ टीलों में फैला है और 350 से 500 हेक्टेयर से अधिक क्षेत्र को कवर करता है।"),
    ("हड़प्पा में खोजा गया कौन सा शवाधान (burial) सिंधु सभ्यता में अद्वितीय है?", "देवदार की लकड़ी के ताबूत (wooden coffin) में दफनाने का साक्ष्य।"),
    ("किस स्थल को अक्सर 'मृतकों का टीला' (Mound of the Dead) कहा जाता है?", "मोहनजोदड़ो को (सिंधी भाषा में इसका शाब्दिक अर्थ यही है)।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Mohenjo-daro had a highly advanced civic planning and drainage system.\nReason (R): Standardized street grids and public drainage channels reflect centralized municipal authority.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Harappa's granaries were located near the river bank outside the citadel.\nReason (R): This facilitated the transport of grain shipments by boat from agricultural fields.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Rakhigarhi is currently considered the largest site of the Indus Valley Civilisation.\nReason (R): Excavations have revealed that the site covers over 350 hectares, surpassing Mohenjo-daro in area.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Great Bath was used for everyday municipal washing by citizens.\nReason (R): Its elaborate architecture and placement on the Citadel suggest it was reserved for ritual purification.", 3, "A is false because it was for ritual use, not everyday washing. R is true."),
    ("Assertion (A): The Priest-King bust represents an actual historical emperor of a Harappan Empire.\nReason (R): There is no direct evidence of monarchy or imperial rule in Harappan archaeology.", 3, "A is false because a monarchy is not proven. R is true."),
    ("Assertion (A): DNA analysis of Rakhigarhi skeletons has revolutionized South Asian prehistory.\nReason (R): The DNA lacks Steppe-related ancestry, showing South Asian gene pools were established before Steppe migrations.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Standardized weights and brick ratios suggest a single unified state in the IVC.\nReason (R): Standardisation can also arise from trade networks and cultural consensus without political unification.", 1, "Both A and R are true but R is not the correct explanation of A (unification remains a debate)."),
    ("Assertion (A): The Dancing Girl is a solid bronze casting.\nReason (R): Solid casting was done using the lost-wax technique where molten metal replaced a wax model.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): मोहनजोदड़ो में एक अत्यधिक उन्नत नगर नियोजन और जल निकासी प्रणाली थी।\nकारण (R): सड़कों का समकोण ग्रिड ढांचा और सार्वजनिक नालियाँ एक सुगठित नागरिक प्रशासन को दर्शाती हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा के अन्नागार किले के बाहर नदी तट के करीब स्थित थे।\nकारण (R): इससे कृषि क्षेत्रों से नावों द्वारा लाए गए अनाज के परिवहन और भंडारण में आसानी होती थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): राखीगढ़ी को वर्तमान में सिंधु घाटी सभ्यता का सबसे बड़ा स्थल माना जाता है।\nकारण (R): उत्खनन से पता चला है कि यह स्थल नौ टीलों में 350 हेक्टेयर से अधिक में फैला है, जो मोहनजोदड़ो से अधिक है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): विशाल स्नानागार का उपयोग नागरिकों द्वारा रोजमर्रा के स्नान के लिए किया जाता था।\nकारण (R): इसकी विस्तृत वास्तुकला और किले (Citadel) पर इसकी स्थिति बताती है कि यह अनुष्ठानिक स्नान के लिए आरक्षित था।", 3, "A असत्य है क्योंकि यह रोजमर्रा के लिए नहीं बल्कि अनुष्ठानिक कार्यों के लिए था। R सत्य है।"),
    ("कथन (A): पुरोहित-राजा की मूर्ति हड़प्पा साम्राज्य के एक वास्तविक ऐतिहासिक सम्राट का प्रतिनिधित्व करती है।\nकारण (R): हड़प्पा पुरातत्व में राजशाही या साम्राज्यवादी शासन का कोई सीधा पुरातात्विक साक्ष्य नहीं मिला है।", 3, "A असत्य है क्योंकि राजशाही प्रमाणित नहीं है। R सत्य है।"),
    ("कथन (A): राखीगढ़ी के कंकालों के डीएनए विश्लेषण ने दक्षिण एशियाई प्रागितिहास में महत्वपूर्ण बदलाव किए हैं।\nकारण (R): डीएनए में स्टेपी से संबंधित आनुवंशिक तत्वों का अभाव है, जो दर्शाता है कि दक्षिण एशियाई मूल के लोग यहाँ पहले से स्थापित थे।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): मानकीकृत बाट और ईंटों के अनुपात सिंधु सभ्यता में एक एकीकृत साम्राज्य का संकेत देते हैं।\nकारण (R): मानकीकरण बिना राजनीतिक एकीकरण के भी सांस्कृतिक सहमति और व्यापारिक नेटवर्क द्वारा संभव हो सकता है।", 1, "A और R दोनों सत्य हैं लेकिन R, A की सही व्याख्या नहीं है (राजनीतिक एकीकरण बहस का विषय है)।"),
    ("कथन (A): नर्तकी (Dancing Girl) की मूर्ति एक ठोस कांस्य ढलाई है।\nकारण (R): ठोस ढलाई लुप्त-मोम (lost-wax) विधि द्वारा की जाती थी जिसमें मोम के मॉडल को पिघलाकर धातु डाली जाती थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Mohenjo-daro:\n1. The name Mohenjo-daro literally translates to 'Mound of the Dead' in Sindhi.\n2. The site was first discovered by Rakhaldas Bannerjee in 1922.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the name origin and discovery of Mohenjo-daro."),
    ("Consider the following statements regarding Harappa:\n1. It was the first site of the civilization to be excavated.\n2. Parallel rows of circular brick threshing platforms have been found outside its citadel.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, reflecting Harappa's discovery priority and crop-threshing findings."),
    ("Consider the following statements regarding the site of Rakhigarhi:\n1. The site is situated along the dry Drishadvati river bed in Haryana.\n2. Recent DNA studies of its skeletal remains indicate genetic continuity of indigenous ancestral lineages.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct. Rakhigarhi is riverine and has yielded critical DNA samples showing indigenous ancestry."),
    ("Consider the following statements regarding the Great Bath:\n1. It was constructed using dressed sandstone blocks imported from Rajasthan.\n2. The outer walls of the bath were decorated with colorful glazed ceramic tiles.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct: The Great Bath is built of baked bricks, not sandstone, and has no glazed tiles."),
    ("Consider the following statements regarding Harappan metropolitan layouts:\n1. The Citadel was always situated to the east of the lower town.\n2. The Lower Town was reserved exclusively for the ruling class and priests.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct: The Citadel lay to the west, and the Lower Town was primarily residential for common citizens.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("मोहनजोदड़ो के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मोहनजोदड़ो का शाब्दिक अर्थ सिंधी भाषा में 'मृतकों का टीला' है।\n2. इस स्थल की खोज सबसे पहले 1922 में राखालदास बनर्जी ने की थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मोहनजोदड़ो के नाम की उत्पत्ति और खोज को दर्शाते हैं।"),
    ("हड़प्पा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह खोजी गई सभ्यता का पहला स्थल था।\n2. इसके किले के बाहर अनाज गाहने के लिए गोलाकार ईंटों के चबूतरे मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो हड़प्पा की खोज की प्राथमिकता और अनाज प्रसंस्करण के साक्ष्यों को दर्शाते हैं।"),
    ("राखीगढ़ी स्थल के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह स्थल हरियाणा में दृषद्वती नदी के सूखे मार्ग पर स्थित है।\n2. यहाँ के कंकालों के हालिया डीएनए अध्ययन स्थानीय लोगों के आनुवंशिक निरंतरता का संकेत देते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं। राखीगढ़ी दृषद्वती के सूखे मार्ग पर है और डीएनए साक्ष्य स्वदेशी उत्पत्ति दर्शाते हैं।"),
    ("विशाल स्नानागार (Great Bath) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसका निर्माण राजस्थान से आयातित तराशे गए बलुआ पत्थरों (sandstone) से किया गया था।\n2. स्नानागार की बाहरी दीवारें रंगीन चमकदार टाइलों से सजाई गई थीं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों में से कोई भी कथन सही नहीं है: विशाल स्नानागार पकी ईंटों से बना है, बलुआ पत्थर से नहीं, और इसमें कोई टाइलें नहीं हैं।"),
    ("हड़प्पा महानगरों के लेआउट के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. किला (Citadel) हमेशा निचले नगर के पूर्व में स्थित होता था।\n2. निचला नगर केवल शासक वर्ग और पुरोहितों के रहने के लिए आरक्षित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों में से कोई भी कथन सही नहीं है: किला पश्चिम में था, और निचला नगर आम नागरिकों तथा कारीगरों के रहने के लिए था।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for q, sol in [
    ("Why did the Harappans construct their granaries near river banks?", "To facilitate the transport of grain shipments by boat from rural agricultural hinterlands directly to the state storage complexes."),
    ("Why was natural bitumen applied to the Great Bath?", "To seal the brickwork and prevent water from leaking or seeping into the surrounding foundations of the Citadel mound."),
    ("Why are the Rakhigarhi skeletal DNA findings significant?", "They suggest that the South Asian ancestral gene pool was formed indigenous to the region, without large migrations from Central Asia during the Harappan era.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पावासियों ने अपने अन्नागार (granaries) नदी तट के पास क्यों बनाए?", "ग्रामीण कृषि क्षेत्रों से नावों द्वारा लाए गए अनाज के सीधे परिवहन और भंडारण को सुगम बनाने के लिए।"),
    ("विशाल स्नानागार (Great Bath) में प्राकृतिक डामर (bitumen) क्यों लगाया गया था?", "ईंटों को जोड़ने वाले गारे को जल-रोधी बनाने और पानी को टीले की नींव में रिसने से रोकने के लिए।"),
    ("राखीगढ़ी के कंकालों के डीएनए (DNA) शोध क्यों महत्वपूर्ण हैं?", "ये दर्शाते हैं कि दक्षिण एशियाई लोगों का पूर्वज समूह इसी क्षेत्र में स्वदेशी रूप से विकसित हुआ था, और हड़प्पा काल में मध्य एशिया से कोई बड़ा प्रवास नहीं हुआ था।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("How did the Harappan street grid system ensure efficient urban traffic?", "By planning wide, parallel avenues crossing at right angles, which separated fast-moving cart traffic from narrow residential alleys."),
    ("How was water supplied to the Great Bath?", "Water was drawn from a large, brick-lined well located in an adjacent room and channeled into the bath through an inlet."),
    ("How did the dual citadel-lower town structure reflect social stratification?", "The raised citadel housed elite public buildings, granaries, and administrative offices, while the larger lower town was built for common citizens and artisans.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा की सड़कों की ग्रिड प्रणाली ने यातायात को कैसे सुगम बनाया?", "सड़कों को समानांतर और समकोण पर काटकर व्यवस्थित किया गया था, जिससे मालवाहक गाड़ियों का आवागमन आसान रहता था और वे रिहायशी तंग गलियों से दूर रहती थीं।"),
    ("विशाल स्नानागार (Great Bath) में पानी की आपूर्ति कैसे की जाती थी?", "पानी पास के एक कमरे में बने ईंटों के विशाल कुएं से निकाला जाता था और नाली के रास्ते स्नानागार में डाला जाता था।"),
    ("किले और निचले नगर के दोहरे विभाजन ने सामाजिक स्तरीकरण को कैसे दर्शाया?", "ऊँचे किले में प्रशासनिक भवन, अनाज भंडार और शासक वर्ग रहते थे, जबकि निचले नगर में आम नागरिक, सैनिक और कारीगर रहते थे।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("Case Study: The Great Bath of Mohenjo-daro", "A monumental public water basin made of baked bricks, gypsum mortar, and watertight bitumen. Features changing rooms and an outlet drain, indicating its use for collective ritual purification rather than daily sanitation."),
    ("Case Study: Rakhigarhi Cemetery Excavations", "Excavations yielded skeletal remains with intact petrous bones, enabling successful ancient DNA sequencing. Results proved genetic continuity of South Asian ancestry without Steppe migrations during the Mature phase."),
    ("Case Study: Parallel Granaries and Circular Platforms of Harappa", "Large storage platforms raised on brick podiums with threshing circles nearby, showing systematic collection, processing, and redistribution of grain by a centralized administrative authority.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: मोहनजोदड़ो का विशाल स्नानागार (Great Bath)", "पकी ईंटों, जिप्सम गारे और बिटुमेन से बना एक विशाल सार्वजनिक जलाशय। इसमें बदलने के कमरे और गंदे पानी की निकासी की नाली थी, जो दैनिक स्वच्छता के बजाय धार्मिक या अनुष्ठानिक सामूहिक स्नान का संकेत देती है।"),
    ("केस स्टडी: राखीगढ़ी कब्रिस्तान का उत्खनन", "कब्रिस्तान से मिले कंकालों के कान की हड्डियों (petrous bones) से प्राचीन डीएनए निकाला गया। इसने साबित किया कि हड़प्पा काल के दौरान कोई बड़ा बाहरी प्रवास नहीं हुआ था, जो इतिहास को नया रूप देता है।"),
    ("केस स्टडी: हड़प्पा के अन्नागार और गोलाकार चबूतरे", "ईंटों के ऊंचे चबूतरों पर बने अन्नागार और पास में अनाज गाहने के गोलाकार चबूतरे दर्शाते हैं कि राज्य स्तर पर अनाज का संग्रह, प्रसंस्करण और पुनर्वितरण एक सुगठित प्रशासनिक व्यवस्था द्वारा किया जाता था।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("Teach the Concept: Harappan Grid Town Planning", "Explain how streets were aligned along cardinal directions (North-South, East-West) to exploit prevailing winds for street cleaning, utilizing standard brick ratios and integrated drainage lines in all sectors."),
    ("Teach the Concept: The Lost-Wax Bronze Casting", "Explain the cire perdue method: modeling in wax, applying clay layers, heating to drain the melted wax, pouring molten bronze, and breaking the mold to reveal solid sculptures like the Dancing Girl."),
    ("Teach the Concept: Archaeological Citadels", "Explain that Citadels were fortified raised mounds containing public, ritual, and administrative spaces, functioning as the civic and political heart of the settlement, separated from residential zones.")
]:
    s1_mastery_eng.append({"type": "Teach the Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा को समझें: हड़प्पा की ग्रिड नगर नियोजन प्रणाली", "समझाएं कि कैसे मुख्य सड़कें दिशाओं (उत्तर-दक्षिण, पूर्व-पश्चिम) के अनुसार समकोण पर काटी जाती थीं ताकि हवा से स्वतः सफाई हो सके, और नालियों का जाल सड़कों के नीचे घर की नालियों से जुड़ा था।"),
    ("अवधारणा को समझें: लुप्त-मोम (Lost-Wax) कांस्य ढलाई विधि", "नर्तकी की मूर्ति बनाने के लिए प्रयुक्त विधि समझाएं: मोम का ढांचा बनाना, मिट्टी की परत चढ़ाना, गर्म करके मोम बाहर निकालना, पिघला हुआ कांसा डालना और ठंडा होने पर मिट्टी तोड़कर मूर्ति निकालना।"),
    ("अवधारणा को समझें: पुरातात्विक किला (Citadel)", "समझाएं कि किला एक मजबूत रक्षात्मक दीवार से घिरा ऊंचा टीला होता था जिसमें सार्वजनिक सभा भवन, अन्नागार और प्रशासनिक कार्यालय होते थे, जो शासक वर्ग के नियंत्रण और सुरक्षा को दर्शाता है।")
]:
    s1_mastery_hin.append({"type": "Teach the Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 2: PORTS, TRADE OUTPOSTS & INDUSTRIAL SUBURBS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which port city features a baked-brick basin identified as a tidal dockyard?", ["Lothal", "Sutkagendor", "Chanhudaro", "Kuntasi"], 0, "Lothal in Gujarat features a massive baked-brick dockyard connected to the Bhogavo River."),
    ("Lothal is situated on the banks of which river in Gujarat?", ["Bhogavo", "Narmada", "Tapi", "Sarasvati"], 0, "Lothal lies along the Bhogavo River, a tributary of the Sabarmati, near the Gulf of Khambhat."),
    ("Which Harappan site is famous for bead-making but completely lacks a fortified citadel?", ["Chanhudaro", "Lothal", "Sutkagendor", "Kuntasi"], 0, "Chanhudaro in Sindh was a major craft suburb that lacked any fortified citadel."),
    ("Sutkagendor, the westernmost frontier outpost of the IVC, is situated along which river?", ["Dasht", "Indus", "Chenab", "Pravara"], 0, "Sutkagendor is situated along the Dasht River in Pakistani Balochistan near the Iran border."),
    ("Which small port and industrial settlement in Gujarat specialized in copper smelting and bead-making?", ["Kuntasi", "Lothal", "Surkotada", "Dholavira"], 0, "Kuntasi in Gujarat functioned as a small port-cum-industrial center specializing in copper and beads.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("किस बंदरगाह शहर में पकी ईंटों से बना एक कुंड मिला है जिसे ज्वारीय गोदी (dockyard) माना गया है?", ["लोथल", "सुतकागेंडोर", "चन्हुदड़ो", "कुंतासी"], 0, "गुजरात के लोथल से पकी ईंटों का एक विशाल गोदी बाड़ा मिला है जो भोगवा नदी से जुड़ा था।"),
    ("लोथल गुजरात में किस नदी के किनारे स्थित है?", ["भोगवा", "नर्मदा", "तापी", "सरस्वती"], 0, "लोथल भोगवा नदी के तट पर स्थित है, जो साबरमती की सहायक नदी है।"),
    ("कौन सा हड़प्पा स्थल मनके बनाने के लिए प्रसिद्ध है, लेकिन वहाँ कोई भी किला (Citadel) नहीं मिला है?", ["चन्हुदड़ो", "लोथल", "सुतकागेंडोर", "कुंतासी"], 0, "सिंध में स्थित चन्हुदड़ो एक शिल्प नगर था जिसमें किलेबंदी वाले किले का पूर्ण अभाव था।"),
    ("सिंधु सभ्यता का सबसे पश्चिमी सीमा स्थल सुतकागेंडोर किस नदी के किनारे स्थित है?", ["दश्त", "सिंधु", "चिनाब", "प्रवर"], 0, "सुतकागेंडोर पाकिस्तान के बलूचिस्तान में दश्त नदी के किनारे स्थित है।"),
    ("गुजरात का कौन सा छोटा बंदरगाह और औद्योगिक केंद्र तांबा गलाने और मनके बनाने में विशेषज्ञता रखता था?", ["कुंतासी", "लोथल", "सुरकोटदा", "धोलावीरा"], 0, "गुजरात का कुंतासी तांबे के काम और मनके बनाने का एक छोटा तटीय औद्योगिक केंद्र था।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the archaeological findings excavated at Lothal: (Select all that apply)", ["Baked-brick tidal dockyard", "Joint/double burials", "Terracotta models of sailing ships", "A citadel-free industrial layout"], [0, 1, 2], "Lothal features a dockyard, double burials, and ship models. Chanhudaro has a citadel-free layout."),
    ("Which crafts were extensively practiced at Chanhudaro? (Select all that apply)", ["Bead manufacturing", "Shell-working and cutting", "Seal engraving", "Iron metallurgy"], [0, 1, 2], "Chanhudaro was famous for beads, shells, and seals. Iron was completely unknown in the Bronze Age."),
    ("Identify the coastal or port sites of the Indus Civilisation: (Select all that apply)", ["Lothal", "Sutkagendor", "Balakot", "Banawali"], [0, 1, 2], "Lothal, Sutkagendor, and Balakot are coastal port sites. Banawali is an inland site in Haryana."),
    ("Select the raw materials imported into ports like Lothal from external trade networks: (Select all that apply)", ["Lapis Lazuli from Badakhshan", "Copper from Oman/Magan", "Gold from Southern India", "Iron ore from Central Asia"], [0, 1, 2], "Lapis lazuli, copper, and gold were imported. Iron was not used or imported."),
    ("Which features are associated with Sutkagendor? (Select all that apply)", ["Situated on the Dasht River near Iran border", "Fortified stone rubble walls", "Acted as a maritime trade buffer post", "Yielded three fortified town sectors"], [0, 1, 2], "Sutkagendor is riverine (Dasht), fortified with stone, and acted as a buffer. Dholavira has three fortified sectors.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("लोथल में मिले प्रमुख पुरातात्विक साक्ष्यों का चयन करें: (सभी लागू विकल्प चुनें)", ["पकी ईंटों का ज्वारीय गोदी बाड़ा", "युगल/संयुक्त शवाधान (Double burials)", "पाल वाले जहाजों के मिट्टी के मॉडल", "किले के बिना बना शिल्प उपनगर"], [0, 1, 2], "लोथल से गोदी बाड़ा, युगल शवाधान और जहाजों के मॉडल मिले हैं। किले के बिना नगर नियोजन चन्हुदड़ो में है।"),
    ("चन्हुदड़ो में किन शिल्पों का बड़े पैमाने पर अभ्यास किया जाता था? (सभी लागू विकल्प चुनें)", ["मनके बनाना (Bead manufacturing)", "शंख उद्योग और कटाई", "मुहरों की नक्काशी", "लोहा धातु कर्म"], [0, 1, 2], "चन्हुदड़ो मनके, शंख और मुहर निर्माण के लिए प्रसिद्ध था। कांस्य युग में लोहे का ज्ञान नहीं था।"),
    ("सिंधु सभ्यता के तटीय या बंदरगाह स्थलों की पहचान करें: (सभी लागू विकल्प चुनें)", ["लोथल", "सुतकागेंडोर", "बालाकोट", "बनावली"], [0, 1, 2], "लोथल, सुतकागेंडोर और बालाकोट तटीय बंदरगाह स्थल हैं। बनावली हरियाणा का एक भीतरी स्थल है।"),
    ("विदेशी व्यापार नेटवर्क से लोथल जैसे बंदरगाहों में आयात किए जाने वाले कच्चे माल का चयन करें: (सभी लागू विकल्प चुनें)", ["बदख्शां से लाजवर्त (Lapis Lazuli)", "ओमान/मगन से तांबा", "दक्षिण भारत से सोना", "मध्य एशिया से कच्चा लोहा"], [0, 1, 2], "लाजवर्त, तांबा और सोना आयातित किए जाते थे। लोहे का कोई उपयोग नहीं था।"),
    ("सुतकागेंडोर से जुड़े लक्षणों का चयन करें: (सभी लागू विकल्प चुनें)", ["ईरान सीमा के पास दश्त नदी पर स्थित", "पत्थर के मलबे की मजबूत किलेबंदी दीवारें", "समुद्री व्यापार के लिए प्रहरी/बफर पोस्ट", "तीन किलेबंदी वाले शहरी क्षेत्र"], [0, 1, 2], "सुतकागेंडोर दश्त नदी के मुहाने पर है, पत्थर से किलेबंद है और बफर पोस्ट था। तीन भागों में धोलावीरा विभाजित है।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Lothal was located along the banks of the Yamuna River.", False, "False. Lothal was located along the Bhogavo River in Gujarat."),
    ("Chanhudaro is the only major Harappan town without a fortified citadel.", True, "True. Chanhudaro completely lacks a raised citadel structure."),
    ("Sutkagendor represents the easternmost boundary of the IVC.", False, "False. It represents the westernmost boundary."),
    ("Joint double burials containing male and female skeletons have been found at Lothal.", True, "True. Several joint double burials were excavated in Lothal's cemetery."),
    ("Chanhudaro was primarily an administrative capital of a Harappan province.", False, "False. Chanhudaro was a dedicated industrial craft suburb."),
    ("Terracotta models of sailing ships have been discovered at Lothal.", True, "True. These models suggest maritime shipping links."),
    ("Kuntasi was an inland site situated in the plains of Haryana.", False, "False. Kuntasi was a small port-cum-industrial site in Gujarat."),
    ("Persian Gulf-type circular seals have been found at Lothal, indicating overseas trade.", True, "True. A circular button seal matching Persian Gulf styles was found at Lothal.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लोथल यमुना नदी के किनारे स्थित था।", False, "असत्य। लोथल गुजरात में भोगवा नदी के किनारे स्थित था।"),
    ("चन्हुदड़ो एकमात्र ऐसा हड़प्पा शहर है जहाँ कोई सुरक्षात्मक किला (citadel) नहीं था।", True, "सत्य। चन्हुदड़ो में सुरक्षात्मक टीले या किले का पूर्ण अभाव था।"),
    ("सुतकागेंडोर सिंधु सभ्यता की सबसे पूर्वी सीमा का प्रतिनिधित्व करता है।", False, "असत्य। यह सबसे पश्चिमी सीमा का प्रतिनिधित्व करता है।"),
    ("लोथल से पुरुष और महिला के कंकालों वाले युगल शवाधान (double burials) मिले हैं।", True, "सत्य। लोथल के कब्रिस्तान से युगल शवाधान के साक्ष्य प्राप्त हुए हैं।"),
    ("चन्हुदड़ो मुख्य रूप से एक हड़प्पा प्रांत की प्रशासनिक राजधानी था।", False, "असत्य। चन्हुदड़ो मुख्य रूप से शिल्पकारों का एक औद्योगिक उपनगर था।"),
    ("लोथल से पाल वाले जहाजों के मिट्टी के मॉडल मिले हैं।", True, "सत्य। ये खिलौने तटीय व्यापार और समुद्री गतिविधियों को दर्शाते हैं।"),
    ("कुंतासी हरियाणा के मैदानों में स्थित एक भीतरी स्थल था।", False, "असत्य। कुंतासी गुजरात के तटीय क्षेत्र में स्थित एक छोटा बंदरगाह-औद्योगिक स्थल था।"),
    ("लोथल से फारस की खाड़ी प्रकार की मुहरें मिली हैं, जो विदेशी व्यापार का संकेत देती हैं।", True, "सत्य। लोथल से एक गोलाकार मुहर मिली है जो फारस की खाड़ी के व्यापारिक केंद्रों से मेल खाती है।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The coastal site of Lothal is situated on the __________ River in Gujarat.", "Bhogavo", "Lothal lies along the Bhogavo River."),
    ("The only major Harappan city that completely lacks a citadel is __________.", "Chanhudaro", "Chanhudaro has no citadel mound."),
    ("The westernmost outpost of the IVC is __________.", "Sutkagendor", "Sutkagendor is the western limit."),
    ("Joint double burials were excavated at the cemetery of __________.", "Lothal", "Lothal contains joint double burials."),
    ("Chanhudaro yielded a brick showing the print of a __________ chasing a cat.", "dog", "A brick with the paw print of a dog chasing a cat was found here."),
    ("Sutkagendor is situated along the __________ River.", "Dasht", "Sutkagendor is situated along the Dasht River."),
    ("A major bead-making workshop and factory was found at both Lothal and __________.", "Chanhudaro", "Both sites had bead-making workshops."),
    ("Balakot, located on the coast of Balochistan, was famous for its __________ industry.", "shell-working", "Balakot was a major shell-working center.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लोथल का तटीय स्थल गुजरात में __________ नदी के किनारे स्थित है।", "भोगवा", "लोथल भोगवा नदी के तट पर स्थित है।"),
    ("एकमात्र प्रमुख हड़प्पा शहर जिसमें किले (citadel) का पूर्ण अभाव था, वह __________ है।", "चन्हुदड़ो", "चन्हुदड़ो में कोई किला नहीं था।"),
    ("सिंधु सभ्यता की सबसे पश्चिमी सीमा चौकी __________ है।", "सुतकागेंडोर", "सुतकागेंडोर पश्चिमी सीमा है।"),
    ("एक ही कब्र में दो कंकालों वाले युगल शवाधान __________ के कब्रिस्तान से मिले हैं।", "लोथल", "लोथल से युगल शवाधान मिले हैं।"),
    ("चन्हुदड़ो से एक ऐसी ईंट मिली है जिस पर बिल्ली का पीछा करते हुए __________ के पंजों के निशान हैं।", "कुत्ते", "कुत्ते और बिल्ली के पंजों के निशान वाली ईंट मिली है।"),
    ("सुतकागेंडोर __________ नदी के किनारे स्थित है।", "दश्त", "सुतकागेंडोर दश्त नदी के किनारे है।"),
    ("लोथल और __________ दोनों स्थानों से मनके बनाने के बड़े कारखाने मिले हैं।", "चन्हुदड़ो", "दोनों स्थलों पर मनके बनाने के कारखाने थे।"),
    ("बलूचिस्तान के तट पर स्थित बालाकोट अपने __________ उद्योग के लिए प्रसिद्ध था।", "शंख", "बालाकोट शंख की कटाई और शिल्प के लिए प्रसिद्ध था।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their primary economic or trade roles:",
        "items": [{"left": "I. Lothal", "key": "A"}, {"left": "II. Chanhudaro", "key": "B"}, {"left": "III. Sutkagendor", "key": "C"}],
        "options": [{"val": "A", "text": "A. Maritime Tidal Port"}, {"val": "B", "text": "B. Industrial Bead Craft Suburb"}, {"val": "C", "text": "C. Western Frontier Trade Post"}],
        "sol": "Lothal was a port, Chanhudaro a craft suburb, and Sutkagendor a western frontier post."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their modern geographic provinces:",
        "items": [{"left": "I. Sutkagendor", "key": "A"}, {"left": "II. Lothal", "key": "B"}, {"left": "III. Chanhudaro", "key": "C"}],
        "options": [{"val": "A", "text": "A. Balochistan (Pakistan)"}, {"val": "B", "text": "B. Gujarat (India)"}, {"val": "C", "text": "C. Sindh (Pakistan)"}],
        "sol": "Sutkagendor is in Balochistan, Lothal in Gujarat, and Chanhudaro in Sindh."
    },
    {
        "type": "Match the Following",
        "q": "Match the unique artifacts with their excavation sites:",
        "items": [{"left": "I. Persian Gulf Style Seal", "key": "A"}, {"left": "II. Cat and Dog Paw Print Brick", "key": "B"}, {"left": "III. Shell Ornaments and Bangles", "key": "C"}],
        "options": [{"val": "A", "text": "A. Lothal"}, {"val": "B", "text": "B. Chanhudaro"}, {"val": "C", "text": "C. Balakot"}],
        "sol": "Persian Gulf seal is at Lothal, paw print brick at Chanhudaro, and shell crafts at Balakot."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "स्थलों को उनकी प्राथमिक आर्थिक या व्यापारिक भूमिकाओं से सुमेलित करें:",
        "items": [{"left": "I. लोथल", "key": "A"}, {"left": "II. चन्हुदड़ो", "key": "B"}, {"left": "III. सुतकागेंडोर", "key": "C"}],
        "options": [{"val": "A", "text": "A. समुद्री ज्वारीय बंदरगाह"}, {"val": "B", "text": "B. औद्योगिक मनका शिल्प उपनगर"}, {"val": "C", "text": "C. पश्चिमी सीमा व्यापार चौकी"}],
        "sol": "लोथल बंदरगाह था, चन्हुदड़ो शिल्प उपनगर था, और सुतकागेंडोर पश्चिमी सीमा चौकी थी।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके आधुनिक भौगोलिक प्रांतों से सुमेलित करें:",
        "items": [{"left": "I. सुतकागेंडोर", "key": "A"}, {"left": "II. लोथल", "key": "B"}, {"left": "III. चन्हुदड़ो", "key": "C"}],
        "options": [{"val": "A", "text": "A. बलूचिस्तान (पाकिस्तान)"}, {"val": "B", "text": "B. गुजरात (भारत)"}, {"val": "C", "text": "C. सिंध (पाकिस्तान)"}],
        "sol": "सुतकागेंडोर बलूचिस्तान में है, लोथल गुजरात में है, और चन्हुदड़ो सिंध में है।"
    },
    {
        "type": "Match the Following",
        "q": "अनूठी खोजों को उनके उत्खनन स्थलों से सुमेलित करें:",
        "items": [{"left": "I. फारस की खाड़ी प्रकार की मुहर", "key": "A"}, {"left": "II. बिल्ली-कुत्ते के पंजों वाली ईंट", "key": "B"}, {"left": "III. शंख की चूड़ियाँ और आभूषण", "key": "C"}],
        "options": [{"val": "A", "text": "A. लोथल"}, {"val": "B", "text": "B. चन्हुदड़ो"}, {"val": "C", "text": "C. बालाकोट"}],
        "sol": "फारस की खाड़ी की मुहर लोथल से, पंजों वाली ईंट चन्हुदड़ो से, और शंख के आभूषण बालाकोट से मिले हैं।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which Indus site has yielded direct evidence of a baked-brick dockyard?", "Lothal."),
    ("Name the river along which Lothal is situated.", "The Bhogavo River."),
    ("Which major Harappan town did not have a citadel?", "Chanhudaro."),
    ("What modern country borders the site of Sutkagendor?", "Iran."),
    ("What was the main trade item manufactured at Chanhudaro?", "Beads (made of carnelian, lapis, jasper, and steatite)."),
    ("What type of burial is unique to Lothal's cemetery?", "Joint double burial (containing two skeletons)."),
    ("Which coastal site in Gujarat shows evidence of a jetty and copper processing?", "Kuntasi."),
    ("Which marine resource was heavily processed at Balakot?", "Marine shells (used for making bangles and beads).")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("किस हड़प्पा स्थल से पकी ईंटों से बने गोदी बाड़े (dockyard) का सीधा साक्ष्य मिला है?", "लोथल।"),
    ("लोथल किस नदी के किनारे स्थित है?", "भोगवा नदी।"),
    ("किस प्रमुख हड़प्पा नगर में कोई किला (Citadel) नहीं था?", "चन्हुदड़ो।"),
    ("सुतकागेंडोर किस आधुनिक देश की सीमा के निकट स्थित है?", "ईरान।"),
    ("चन्हुदड़ो में निर्मित मुख्य व्यापारिक वस्तु क्या थी?", "मनके (beads) जो अकीक, सेलखड़ी आदि से बनते थे।"),
    ("लोथल के कब्रिस्तान से प्राप्त कौन सा शवाधान अद्वितीय है?", "युगल शवाधान (जिसमें दो कंकाल एक साथ हैं)।"),
    ("गुजरात का कौन सा तटीय स्थल जेट्टी (jetty) और तांबा प्रसंस्करण के साक्ष्य दिखाता है?", "कुंतासी।"),
    ("बालाकोट में किस समुद्री संसाधन का बड़े पैमाने पर प्रसंस्करण किया जाता था?", "समुद्री शंख (shell) जिससे चूड़ियाँ बनाई जाती थीं।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Lothal was a key maritime hub of the Indus Civilisation.\nReason (R): A massive baked-brick basin identified as a tidal dockyard was found at Lothal.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Chanhudaro was an unfortified suburb.\nReason (R): It was dedicated to industrial crafts and lacked administrative citadel defenses.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Sutkagendor was built with massive stone fortification walls.\nReason (R): It served as a fortified frontier post to protect trade routes from hostile tribes.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The double burials at Lothal indicate the practice of Sati.\nReason (R): Skeletons in joint burials can result from simultaneous deaths due to epidemics or natural disasters.", 3, "A is false because Sati is not proven. R is true."),
    ("Assertion (A): Chanhudaro bead factories used bronze drills to perforate stones.\nReason (R): Artisans used highly specialized chert drills to perforate hard carnelian beads.", 3, "A is false because chert drills were used, not bronze. R is true."),
    ("Assertion (A): Lothal traded directly with the Persian Gulf and Mesopotamia.\nReason (R): Seals typical of the Persian Gulf and Mesopotamian trade goods have been found at Lothal.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Sutkagendor was located on a fertile river delta.\nReason (R): It is situated in the dry, rocky Makran coast of Balochistan.", 3, "A is false because Makran is dry, not a fertile delta. R is true."),
    ("Assertion (A): Kuntasi was a major administrative capital.\nReason (R): Kuntasi functioned as a small port and craft production outpost in Gujarat.", 3, "A is false because Kuntasi was a small industrial port. R is true.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): लोथल सिंधु सभ्यता का एक प्रमुख समुद्री केंद्र था।\nकारण (R): लोथल में पकी ईंटों से बना एक विशाल कुंड मिला है जिसे ज्वारीय गोदी बाड़ा (dockyard) माना गया है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): चन्हुदड़ो एक बिना किलेबंदी वाला उपनगर था।\nकारण (R): यह मुख्य रूप से शिल्पकारों का नगर था और यहाँ कोई प्रशासनिक किला नहीं था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सुतकागेंडोर का निर्माण पत्थरों की विशाल सुरक्षा दीवारों से किया गया था।\nकारण (R): यह सीमावर्ती क्षेत्रों में व्यापारिक मार्गों को शत्रुतापूर्ण कबीलों से सुरक्षित रखने के लिए बफर चौकी थी।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): लोथल में मिले युगल शवाधान सती प्रथा के साक्ष्य हैं।\nकारण (R): संयुक्त कब्रों में कंकाल महामारी या प्राकृतिक आपदाओं के कारण एक साथ हुई मौतों के भी हो सकते हैं।", 3, "A असत्य है क्योंकि सती प्रमाणित नहीं है। R सत्य है।"),
    ("कथन (A): चन्हुदड़ो के मनका कारखानों में पत्थरों में छेद करने के लिए कांसे के बरमों का उपयोग होता था।\nकारण (R): कारीगरों ने कठोर अकीक के मनकों में छेद करने के लिए विशिष्ट चर्ट पत्थर के बरमों (drills) का उपयोग किया।", 3, "A असत्य है क्योंकि चर्ट के बरमे थे, कांसे के नहीं। R सत्य है।"),
    ("कथन (A): लोथल फारस की खाड़ी और मेसोपोटामिया के साथ सीधा व्यापार करता था।\nकारण (R): लोथल से फारस की खाड़ी शैली की गोलाकार मुहरें और मेसोपोटामियाई व्यापारिक सामान मिले हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सुतकागेंडोर एक उपजाऊ नदी डेल्टा पर स्थित था।\nकारण (R): यह बलूचिस्तान के शुष्क और पथरीले मकरान तट पर स्थित है।", 3, "A असत्य है क्योंकि मकरान शुष्क है, उपजाऊ नहीं। R सत्य है।"),
    ("कथन (A): कुंतासी एक मुख्य प्रशासनिक राजधानी था।\nकारण (R): कुंतासी गुजरात में एक छोटा बंदरगाह और शिल्प उत्पादन केंद्र था।", 3, "A असत्य है क्योंकि यह एक छोटा शिल्प बंदरगाह था। R सत्य है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Lothal:\n1. It featured a dockyard connected to the Bhogavo River.\n2. A major bead factory with working tools was excavated here.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Lothal's dockyard and bead-making facility."),
    ("Consider the following statements regarding Chanhudaro:\n1. It is the only major Harappan city that completely lacks a raised citadel.\n2. A brick showing the paw print of a dog chasing a cat was found here.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Chanhudaro's unique layout and paw print brick."),
    ("Consider the following statements regarding Sutkagendor:\n1. It is situated on the banks of the Dasht River.\n2. It represents the easternmost frontier of the Harappan culture.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: Sutkagendor is the westernmost frontier, not easternmost."),
    ("Consider the following statements regarding joint burials at Lothal:\n1. Double burials always contain two male skeletons.\n2. Pot burials are exclusively found at Lothal.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct: Joint burials contain male-female pairs, and pot burials are common across many sites."),
    ("Consider the following statements regarding peripheral sites:\n1. Balakot was famous for its textile industry.\n2. Kuntasi was located in the Himalayan foothills.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct: Balakot was famous for shell-working, and Kuntasi was located on the coast of Gujarat.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लोथल के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. इसमें भोगवा नदी से जुड़ा एक गोदी बाड़ा (dockyard) था।\n2. यहाँ से काम करने वाले औजारों के साथ एक बड़ा मनका कारखाना मिला है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो लोथल के गोदी बाड़े और मनका कारखाने को दर्शाते हैं।"),
    ("चन्हुदड़ो के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह एकमात्र प्रमुख हड़प्पा शहर है जिसमें सुरक्षात्मक किले (citadel) का पूर्ण अभाव था।\n2. यहाँ से बिल्ली का पीछा करते हुए कुत्ते के पंजे के निशान वाली ईंट मिली है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो चन्हुदड़ो के लेआउट और पंजों के निशान वाली ईंट को दर्शाते हैं।"),
    ("सुतकागेंडोर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह दश्त नदी के किनारे स्थित है।\n2. यह हड़प्पा संस्कृति की सबसे पूर्वी सीमा का प्रतिनिधित्व करता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है: यह सबसे पश्चिमी सीमा है, पूर्वी नहीं।"),
    ("लोथल में मिले संयुक्त शवाधानों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. युगल शवाधानों में हमेशा दो पुरुष कंकाल होते हैं।\n2. कलश शवाधान (pot burials) केवल लोथल में पाए जाते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों में से कोई भी कथन सही नहीं है: युगल कब्रों में स्त्री-पुरुष होते हैं, और कलश शवाधान कई अन्य स्थलों पर भी आम हैं।"),
    ("बाहरी स्थलों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बालाकोट अपने कपड़ा उद्योग के लिए प्रसिद्ध था।\n2. कुंतासी हिमालय की तलहटी में स्थित था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों में से कोई भी कथन सही नहीं है: बालाकोट शंख उद्योग के लिए और कुंतासी गुजरात के तट पर होने के लिए प्रसिद्ध था।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for q, sol in [
    ("Why did the Harappans establish an outpost at Sutkagendor?", "To serve as a fortified port and buffer post for managing maritime trade routes with the Persian Gulf and Mesopotamia, protecting it from inland tribes."),
    ("Why did Chanhudaro lack a fortified citadel?", "Because it was built purely as a craft production suburb rather than a political, administrative, or ceremonial capital."),
    ("Why was Lothal's dockyard built with baked bricks rather than sun-dried bricks?", "To withstand water pressure and erosion caused by constant tidal inflows and outflows from the Bhogavo River and Gulf.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पावासियों ने सुतकागेंडोर में एक चौकी क्यों स्थापित की?", "फारस की खाड़ी और मेसोपोटामिया के साथ समुद्री व्यापार मार्गों की रक्षा करने और उन्हें भीतरी पहाड़ी कबीलों से बचाने के लिए।"),
    ("चन्हुदड़ो में सुरक्षात्मक किला (citadel) क्यों नहीं बनाया गया था?", "क्योंकि इसका विकास प्रशासनिक या राजनीतिक मुख्यालय के बजाय विशुद्ध रूप से एक शिल्पकार उपनगर के रूप में हुआ था।"),
    ("लोथल का गोदी बाड़ा धूप में सुखाई ईंटों के बजाय पकी ईंटों से क्यों बनाया गया था?", "भोगवा नदी और खाड़ी से आने वाले ज्वार-भाटे के पानी के निरंतर बहाव और कटाव को सहने के लिए।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("How did Lothal's dockyard operate using tides?", "Ships entered the basin during high tides through an inlet channel. A wooden sluice gate was lowered at low tide to trap water and float ships for loading/unloading."),
    ("How did bead-makers color carnelian stone red?", "By heating yellowish-brown raw stones in clay pots over open fires, causing iron oxides in the stone to oxidize into a bright red color."),
    ("How did Sutkagendor facilitate overland and sea trade?", "Its location at the Dasht River mouth allowed it to monitor sea traffic while connecting with inland camel caravan routes passing through Iran.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("लोथल के गोदी बाड़े (dockyard) में जहाजों को ज्वार द्वारा कैसे लाया जाता था?", "जहाज उच्च ज्वार के दौरान प्रवेश मार्ग से गोदी में आते थे। कम ज्वार के दौरान पानी को रोकने के लिए लकड़ी का स्लूस द्वार बंद कर दिया जाता था ताकि जहाज तैरते रहें।"),
    ("मनका बनाने वाले अकीक (carnelian) पत्थर को लाल रंग कैसे देते थे?", "पीले-भूरे रंग के कच्चे पत्थरों को मिट्टी के बर्तनों में आग पर गर्म करके, जिससे पत्थर में मौजूद आयरन ऑक्साइड चमकीले लाल रंग में बदल जाता था।"),
    ("सुतकागेंडोर ने थल और समुद्री व्यापार को कैसे सुगम बनाया?", "दश्त नदी के मुहाने पर इसकी स्थिति ने समुद्री व्यापार की निगरानी करने और ईरान के रास्ते चलने वाले थल कारवां मार्गों से जुड़ने में मदद की।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("Case Study: The Lothal Dockyard", "A massive trapezoidal brick basin measuring 217m x 37m, connected to a river channel. It is the earliest known artificial dockyard in the world, showcasing advanced understanding of tidal flow, sluice engineering, and maritime shipping."),
    ("Case Study: Bead Manufacture at Chanhudaro", "Excavations revealed working floors, furnaces, stone chips, and specialized chert drills. The find proves that bead making was a highly structured, state-sponsored industry with specialized labor producing goods for local use and export."),
    ("Case Study: The Sutkagendor Outpost", "Located in the arid Makran coast. It features a walled citadel built of massive stone blocks, showing that the Harappans fortified their trade outposts on hostile frontiers to secure West Asian sea lanes.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: लोथल का गोदी बाड़ा (Dockyard)", "217 मीटर x 37 मीटर का पकी ईंटों का एक विशाल कुंड, जो नदी मार्ग से जुड़ा था। यह विश्व का सबसे प्राचीन कृत्रिम गोदी बाड़ा है, जो ज्वार-भाटे, स्लूस गेट और समुद्री व्यापार के उन्नत ज्ञान को दर्शाता है।"),
    ("केस स्टडी: चन्हुदड़ो में मनका निर्माण", "उत्खनन से भट्टियां, पत्थरों के टुकड़े और विशिष्ट चर्ट बरमे (drills) मिले हैं। यह साबित करता है कि मनका निर्माण एक जटिल औद्योगिक गतिविधि थी जो निर्यात और घरेलू बाजार दोनों के लिए माल तैयार करती थी।"),
    ("केस स्टडी: सुतकागेंडोर की सीमा चौकी", "शुष्क मकरान तट पर स्थित यह स्थल। इसमें पत्थर की दीवारों वाला किला मिला है, जो दर्शाता है कि हड़प्पावासियों ने फारस की खाड़ी के व्यापार मार्गों की रक्षा के लिए अपनी सीमा चौकियों को किलेबंद किया था।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("Teach the Concept: Harappan Bead Making", "Explain the steps: sourcing raw stones (carnelian, jasper, steatite), heating to change color, chipping and grinding to shape, polishing to smooth, and drilling holes using hard chert drills."),
    ("Teach the Concept: Sluice-Gate Siphon Docking", "Explain how a sluice gate works: it is lowered to lock water in a basin when the external tide recedes, preventing ships from grounding on mud during low tides."),
    ("Teach the Concept: Craft Specialisation Suburbs", "Explain that some towns grew exclusively around specialized industrial crafts (like Chanhudaro) without needing administrative citadels or political elites, indicating a decentralized economic network.")
]:
    s2_mastery_eng.append({"type": "Teach the Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा को समझें: हड़प्पा में मनके बनाने की कला", "चरण समझाएं: कच्चे पत्थरों को लाना, गर्म कर रंग बदलना, तराशना और घिसना, पॉलिश करना और फिर चर्ट पत्थर के बरमों से छेद करना।"),
    ("अवधारणा को समझें: स्लूस-गेट (Sluice-Gate) गोदी प्रणाली", "समझाएं कि कैसे स्लूस गेट का उपयोग पानी को कुंड के भीतर रोकने के लिए किया जाता था जब बाहरी समुद्र में भाटा (low tide) आता था, जिससे जहाज तैरते रहते थे।"),
    ("अवधारणा को समझें: शिल्प विशिष्ट उपनगर (Industrial Suburbs)", "समझाएं कि कैसे कुछ नगर (जैसे चन्हुदड़ो) राजनीतिक सत्ता के बिना केवल औद्योगिक गतिविधियों के लिए विकसित हुए, जो एक अत्यंत संगठित आर्थिक और व्यापारिक ढांचे को दर्शाता है।")
]:
    s2_mastery_hin.append({"type": "Teach the Concept", "q": q, "sol": sol})


# =========================================================================
# SECTION 3: REGIONAL ENCLAVES, CITADELS & DRYLAND TOWNS
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which Harappan site is uniquely divided into three fortified sections: Citadel, Middle Town, and Lower Town?", ["Dholavira", "Kalibangan", "Banawali", "Surkotada"], 0, "Dholavira in Gujarat is unique for its three-tier urban layout."),
    ("Dholavira is located on which island in the Kutch district of Gujarat?", ["Khadir Bet", "Diu Island", "Salsette Island", "Majuli Island"], 0, "Dholavira is situated on Khadir Bet island in the Great Rann of Kutch."),
    ("At which site was the earliest ploughed agricultural field in the subcontinent discovered?", ["Kalibangan", "Banawali", "Harappa", "Mohenjo-daro"], 0, "Kalibangan in Rajasthan features a pre-Harappan ploughed field showing furrow grids."),
    ("Which site yielded a well-preserved terracotta model of an agricultural plow?", ["Banawali", "Kalibangan", "Dholavira", "Rakhigarhi"], 0, "Banawali in Haryana yielded a detailed terracotta toy model of a plow."),
    ("At which site in Gujarat were controversial skeletal remains of a horse reported in its upper layers?", ["Surkotada", "Dholavira", "Lothal", "Kuntasi"], 0, "Surkotada has reported skeletal horse remains, which remains debated among archaeologists.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("कौन सा हड़प्पा स्थल विशिष्ट रूप से तीन किलेबंद भागों: किला, मध्य नगर और निचला नगर में विभाजित है?", ["धोलावीरा", "कालीबंगन", "बनावली", "सुरकोटदा"], 0, "गुजरात का धोलावीरा अपने त्रि-स्तरीय नगर नियोजन के लिए प्रसिद्ध है।"),
    ("धोलावीरा गुजरात के कच्छ जिले में किस द्वीप पर स्थित है?", ["खादिर बेट (Khadir Bet)", "दीव द्वीप", "सालसेट द्वीप", "माजुली द्वीप"], 0, "धोलावीरा कच्छ के रन में खादिर बेट द्वीप पर स्थित है।"),
    ("भारतीय उपमहाद्वीप में सबसे पहले जुते हुए खेत के साक्ष्य किस स्थल पर खोजे गए थे?", ["कालीबंगन", "बनावली", "हड़प्पा", "मोहनजोदड़ो"], 0, "राजस्थान के कालीबंगन से पूर्व-हड़प्पा कालीन जुते हुए खेत के साक्ष्य मिले हैं।"),
    ("मिट्टी (terracotta) का बना हल का एक खिलौना किस स्थल से प्राप्त हुआ था?", ["बनावली", "कालीबंगन", "धोलावीरा", "राखीगढ़ी"], 0, "हरियाणा के बनावली से मिट्टी के हल का एक खिलौना मिला है।"),
    ("गुजरात के किस स्थल से ऊपरी स्तरों में घोड़े की हड्डियों के विवादास्पद अवशेष प्राप्त हुए हैं?", ["सुरकोटदा", "धोलावीरा", "लोथल", "कुंतासी"], 0, "सुरकोटदा से घोड़े के अवशेषों की रिपोर्ट की गई है, जो विद्वानों में बहस का विषय है।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Select the unique features discovered at Dholavira: (Select all that apply)", ["Three-tier city division", "Massive stone water reservoirs", "A 10-character gypsum signboard", "A grid ploughed agricultural field"], [0, 1, 2], "Dholavira has three divisions, stone reservoirs, and a signboard. The ploughed field is at Kalibangan."),
    ("Which findings are associated with Kalibangan? (Select all that apply)", ["Pre-Harappan ploughed field furrows", "A series of clay fire altars on brick platforms", "Use of wooden drainage channels", "Radial street patterns"], [0, 1, 2], "Kalibangan has a ploughed field, fire altars, and wooden drains. Radial streets are at Banawali."),
    ("Identify the characteristics of Banawali: (Select all that apply)", ["Radial or concentric street layout", "Terracotta model of a plow", "Rich deposits of barley grains", "Monumental stone reservoirs"], [0, 1, 2], "Banawali has radial streets, a toy plow, and barley. Stone reservoirs are at Dholavira."),
    ("Select the features of Surkotada: (Select all that apply)", ["Fortified rubble stone citadel and lower town", "Oval graves and pot burials", "Debated horse skeletal remains", "Lack of any defensive fortification walls"], [0, 1, 2], "Surkotada has stone forts, oval/pot burials, and horse bones. It was heavily fortified."),
    ("Which sites used local stone instead of baked bricks for fortifications? (Select all that apply)", ["Dholavira", "Surkotada", "Sutkagendor", "Kalibangan"], [0, 1, 2], "Dholavira, Surkotada, and Sutkagendor used stone fortifications. Kalibangan used mud bricks.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("धोलावीरा में खोजी गई अनूठी विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["त्रि-स्तरीय नगर नियोजन", "पत्थर काटकर बनाए गए विशाल जलाशय", "जिप्सम का 10-अक्षरों वाला साइनबोर्ड", "जुता हुआ खेत"], [0, 1, 2], "धोलावीरा में त्रि-स्तरीय विभाजन, जलाशय और साइनबोर्ड हैं। जुता हुआ खेत कालीबंगन में है।"),
    ("कालीबंगन से जुड़े साक्ष्यों का चयन करें: (सभी लागू विकल्प चुनें)", ["पूर्व-हड़प्पा जुते हुए खेत के निशान", "ईंटों के चबूतरे पर अग्निकुंडों की कतार", "लकड़ी की नालियों का उपयोग", "अरीय (radial) सड़कों का जाल"], [0, 1, 2], "कालीबंगन में जुता हुआ खेत, अग्निकुंड और लकड़ी की नालियां हैं। अरीय सड़कें बनावली में हैं।"),
    ("बनावली की विशेषताओं की पहचान करें: (सभी लागू विकल्प चुनें)", ["अरीय (radial) सड़कों का नियोजन", "मिट्टी के हल का मॉडल", "जौ (barley) के समृद्ध अवशेष", "पत्थर के विशाल जलाशय"], [0, 1, 2], "बनावली में अरीय सड़कें, मिट्टी का हल और जौ मिले हैं। विशाल जलाशय धोलावीरा में हैं।"),
    ("सुरकोटदा की विशेषताओं का चयन करें: (सभी लागू विकल्प चुनें)", ["मलबे के पत्थरों से बना किला और निचला नगर", "अंडाकार कब्रें और कलश शवाधान", "घोड़े के विवादास्पद कंकाल अवशेष", "सुरक्षा दीवार का पूर्ण अभाव"], [0, 1, 2], "सुरकोटदा में पत्थर के किले, अंडाकार कब्रें और घोड़े की हड्डियां मिली हैं। यह सुरक्षित शहर था।"),
    ("किलेबंदी के लिए पकी ईंटों के बजाय स्थानीय पत्थरों का उपयोग करने वाले स्थलों का चयन करें: (सभी लागू विकल्प चुनें)", ["धोलावीरा", "सुरकोटदा", "सुतकागेंडोर", "कालीबंगन"], [0, 1, 2], "धोलावीरा, सुरकोटदा और सुतकागेंडोर में पत्थर की दीवारें थीं। कालीबंगन में मुख्य रूप से कच्ची ईंटें थीं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Dholavira is divided into only two parts like other standard Harappan cities.", False, "False. Dholavira is divided into three sections: Citadel, Middle Town, and Lower Town."),
    ("Kalibangan is located in Rajasthan along the Ghaggar River channel.", True, "True. Kalibangan is in Hanumangarh district, Rajasthan, on the Ghaggar bed."),
    ("Dholavira features 16 massive reservoirs to harvest rainwater runoff.", True, "True. Dholavira utilized stone reservoirs to adapt to Kutch's dry climate."),
    ("Banawali had a perfect grid-pattern street layout.", False, "False. Banawali's streets follow an irregular, radial pattern."),
    ("Surkotada is located in the modern state of Haryana.", False, "False. Surkotada is located in the Kutch district of Gujarat."),
    ("The ploughed field at Kalibangan shows grid-pattern furrow marks.", True, "True. The furrows run at right angles, showing dual crop plowing."),
    ("Dholavira's signboard letters are made of solid gold sheet.", False, "False. The letters are made of white gypsum paste."),
    ("Ritual fire altars have been found at both Kalibangan and Lothal.", True, "True. Brick pits with ash and charcoal are present at both sites.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("धोलावीरा अन्य मानक हड़प्पा शहरों की तरह केवल दो भागों में विभाजित है।", False, "असत्य। धोलावीरा तीन भागों: किला, मध्य नगर और निचला नगर में विभाजित है।"),
    ("कालीबंगन राजस्थान में घग्गर नदी के सूखे मार्ग पर स्थित है।", True, "सत्य। कालीबंगन राजस्थान के हनुमानगढ़ जिले में घग्गर नदी के किनारे है।"),
    ("धोलावीरा में वर्षा जल संचयन के लिए 16 विशाल जलाशय मिले हैं।", True, "सत्य। धोलावीरा में वर्षा जल एकत्र करने के लिए विशाल जलाशय बनाए गए थे।"),
    ("बनावली में सड़कों का लेआउट एकदम सटीक ग्रिड प्रतिरूप पर आधारित था।", False, "असत्य। बनावली में सड़कें अनियमित और अरीय (radial) प्रतिरूप का पालन करती थीं।"),
    ("सुरकोटदा आधुनिक भारत के हरियाणा राज्य में स्थित है।", False, "असत्य। सुरकोटदा गुजरात के कच्छ जिले में स्थित है।"),
    ("कालीबंगन के जुते हुए खेत में हल की रेखाएं समकोण ग्रिड बनाती हैं।", True, "सत्य। हल-रेखाएं समकोण पर काटती हैं, जो दोहरी फसल का संकेत देती हैं।"),
    ("धोलावीरा के साइनबोर्ड के अक्षर सोने की चादर से बने हैं।", False, "असत्य। इसके अक्षर सफेद जिप्सम के गाढ़े लेप से बने थे।"),
    ("धार्मिक अग्निकुंड (fire altars) कालीबंगन और लोथल दोनों स्थलों पर मिले हैं।", True, "सत्य। राख और कोयले से युक्त ईंटों के कुंड दोनों स्थलों पर पाए गए हैं।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("Dholavira is situated in the Kutch district of Gujarat on the island of __________ Bet.", "Khadir", "Dholavira is located on Khadir Bet."),
    ("The site showing the earliest ploughed agricultural field is __________.", "Kalibangan", "Kalibangan features the earliest ploughed field."),
    ("A terracotta model of a plow was excavated at __________.", "Banawali", "The toy plow model was found at Banawali."),
    ("The site in Gujarat famous for horse bone findings is __________.", "Surkotada", "Surkotada reported skeletal horse remains."),
    ("The famous 10-character gypsum signboard was found at __________.", "Dholavira", "The signboard was discovered in Dholavira's gateway."),
    ("Kalibangan is situated along the dry bed of the __________ River.", "Ghaggar", "Kalibangan lies along the Ghaggar River."),
    ("Banawali contains streets arranged in a __________ layout rather than a grid.", "radial", "Banawali's layout was radial/concentric."),
    ("Instead of bricks, Dholavira's fortifications were constructed using dressed __________.", "stone", "Dholavira utilized local stone masonry.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("धोलावीरा गुजरात के कच्छ जिले में __________ बेट नामक द्वीप पर स्थित है।", "खादिर", "धोलावीरा खादिर बेट पर स्थित है।"),
    ("उपमहाद्वीप में सबसे पहले जुते हुए खेत के साक्ष्य दर्शाने वाला स्थल __________ है।", "कालीबंगन", "कालीबंगन में जुता हुआ खेत मिला है।"),
    ("मिट्टी (terracotta) का बना हल का खिलौना __________ से उत्खनित किया गया था।", "बनावली", "मिट्टी का हल बनावली से मिला था।"),
    ("गुजरात का वह स्थल जो घोड़े की हड्डियों की खोज के लिए प्रसिद्ध है, वह __________ है।", "सुरकोटदा", "सुरकोटदा से घोड़े के अवशेष मिले थे।"),
    ("जिप्सम का प्रसिद्ध 10-अक्षरों वाला साइनबोर्ड __________ से मिला है।", "धोलावीरा", "यह साइनबोर्ड धोलावीरा के प्रवेश द्वार के फर्श पर मिला था।"),
    ("कालीबंगन __________ नदी के सूखे मार्ग पर स्थित है।", "घग्गर", "कालीबंगन घग्गर नदी के किनारे स्थित है।"),
    ("बनावली में सड़कें ग्रिड के बजाय __________ प्रतिरूप में व्यवस्थित थीं।", "अरीय", "बनावली में अरीय (radial) सड़कों का नियोजन था।"),
    ("ईंटों के स्थान पर, धोलावीरा की किलेबंदी की दीवारों का निर्माण तराशे गए __________ से हुआ था।", "पत्थरों", "धोलावीरा में स्थानीय पत्थरों की वास्तुकला का उपयोग हुआ था।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the sites with their unique civic or engineering features:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Kalibangan", "key": "B"}, {"left": "III. Banawali", "key": "C"}],
        "options": [{"val": "A", "text": "A. Dressed Stone Reservoirs"}, {"val": "B", "text": "B. Wooden Drainage Channels"}, {"val": "C", "text": "C. Radial Street Layout"}],
        "sol": "Dholavira has stone reservoirs, Kalibangan wooden drains, and Banawali radial streets."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their unique archaeological finds:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Kalibangan", "key": "B"}, {"left": "III. Surkotada", "key": "C"}],
        "options": [{"val": "A", "text": "A. 10-Character Inscription"}, {"val": "B", "text": "B. Grid Ploughed Field"}, {"val": "C", "text": "C. Debated Horse Bones"}],
        "sol": "Dholavira has the signboard, Kalibangan the ploughed field, and Surkotada the horse bones."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their modern geographic states in India:",
        "items": [{"left": "I. Kalibangan", "key": "A"}, {"left": "II. Dholavira", "key": "B"}, {"left": "III. Banawali", "key": "C"}],
        "options": [{"val": "A", "text": "A. Rajasthan"}, {"val": "B", "text": "B. Gujarat"}, {"val": "C", "text": "C. Haryana"}],
        "sol": "Kalibangan is in Rajasthan, Dholavira in Gujarat, and Banawali in Haryana."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "स्थलों को उनकी अनूठी नागरिक या तकनीकी विशेषताओं से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा", "key": "A"}, {"left": "II. कालीबंगन", "key": "B"}, {"left": "III. बनावली", "key": "C"}],
        "options": [{"val": "A", "text": "A. पत्थर काटकर बने जलाशय"}, {"val": "B", "text": "B. लकड़ी की नाली प्रणालियाँ"}, {"val": "C", "text": "C. अरीय (radial) सड़कों का जाल"}],
        "sol": "धोलावीरा में जलाशय, कालीबंगन में लकड़ी की नालियां, और बनावली में अरीय सड़कें मिली हैं।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनके अनूठे पुरातात्विक साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा", "key": "A"}, {"left": "II. कालीबंगन", "key": "B"}, {"left": "III. सुरकोटदा", "key": "C"}],
        "options": [{"val": "A", "text": "A. 10-अक्षरों का साइनबोर्ड"}, {"val": "B", "text": "B. जुताई रेखाओं वाला खेत"}, {"val": "C", "text": "C. घोड़े के विवादास्पद अवशेष"}],
        "sol": "धोलावीरा से साइनबोर्ड, कालीबंगन से जुता हुआ खेत, और सुरकोटदा से घोड़े के अवशेष मिले हैं।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को भारत के उनके आधुनिक राज्यों से सुमेलित करें:",
        "items": [{"left": "I. कालीबंगन", "key": "A"}, {"left": "II. धोलावीरा", "key": "B"}, {"left": "III. बनावली", "key": "C"}],
        "options": [{"val": "A", "text": "A. राजस्थान"}, {"val": "B", "text": "B. गुजरात"}, {"val": "C", "text": "C. हरियाणा"}],
        "sol": "कालीबंगन राजस्थान में है, धोलावीरा गुजरात में है, और बनावली हरियाणा में है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Which Harappan site is divided into a Citadel, Middle Town, and Lower Town?", "Dholavira."),
    ("What is the location of Dholavira in Gujarat?", "Khadir Bet island in the Great Rann of Kutch."),
    ("Where was the earliest ploughed field of the subcontinent discovered?", "Kalibangan in Rajasthan."),
    ("Which site yielded a terracotta toy plow?", "Banawali in Haryana."),
    ("Which site is known for horse bone reports in Kutch?", "Surkotada."),
    ("What material was used to make the letters on the Dholavira signboard?", "White gypsum paste/powder."),
    ("Which river dry channel was Kalibangan situated along?", "The Ghaggar River bed."),
    ("Why is Banawali's town plan considered irregular?", "Because its streets follow a radial layout rather than a strict grid pattern.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("कौन सा हड़प्पा स्थल एक किला, मध्य नगर और निचले नगर में विभाजित है?", "धोलावीरा।"),
    ("गुजरात में धोलावीरा की भौगोलिक स्थिति क्या है?", "कच्छ के रन में खादिर बेट द्वीप।"),
    ("भारतीय उपमहाद्वीप में सबसे पहले जुते हुए खेत की खोज कहाँ हुई थी?", "राजस्थान के कालीबंगन में।"),
    ("किस स्थल से मिट्टी का बना खिलौना हल मिला है?", "हरियाणा के बनावली से।"),
    ("कच्छ का कौन सा स्थल घोड़े की हड्डियों की रिपोर्ट के लिए जाना जाता है?", "सुरकोटदा।"),
    ("धोलावीरा साइनबोर्ड के अक्षरों को बनाने के लिए किस सामग्री का उपयोग किया गया था?", "सफेद जिप्सम लेप।"),
    ("कालीबंगन किस नदी के शुष्क मार्ग पर स्थित था?", "घग्गर नदी।"),
    ("बनावली के नगर नियोजन को अनियमित क्यों माना जाता है?", "क्योंकि इसकी सड़कें ग्रिड के बजाय केंद्र से बाहर की ओर (radial) जाती थीं।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): Dholavira has spectacular stone-cut water reservoirs.\nReason (R): Dholavira was located in an arid region of Kutch and needed to harvest scarce monsoonal runoff.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Kalibangan used wooden drainage pipes.\nReason (R): They lacked baked bricks and had to adapt local timber resources for sewerage channels.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Banawali has a radial town plan.\nReason (R): It shows a transition or deviation from the classic Mature Harappan grid layout.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The horse remains at Surkotada prove the Harappans were horse-riding warriors.\nReason (R): The presence of horse bones in late layers is highly debated, and there is no evidence of horse-drawn military chariots in Harappan archaeology.", 3, "A is false because horse-riding warriors are not proven. R is true."),
    ("Assertion (A): Dholavira's architecture is unique in the Indus Civilisation.\nReason (R): Unlike other cities built of baked brick, Dholavira was built extensively using dressed local limestone.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Kalibangan contains brick platforms with fire altars.\nReason (R): The presence of fire altars indicates the practice of fire worship or sacrificial rituals.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Banawali yielded no agricultural finds.\nReason (R): Banawali yielded a high concentration of high-quality barley grains and a toy plow.", 3, "A is false because barley and plow were found. R is true."),
    ("Assertion (A): Surkotada had no fortifications.\nReason (R): Surkotada featured a strongly fortified stone citadel and lower town with gateways.", 3, "A is false because it was fortified. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): धोलावीरा में पत्थर काटकर बनाए गए शानदार जलाशय हैं।\nकारण (R): धोलावीरा कच्छ के शुष्क क्षेत्र में स्थित था जहाँ मानसूनी पानी को सहेजना आवश्यक था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कालीबंगन में गंदे पानी की निकासी के लिए लकड़ी की नालियों का उपयोग किया गया था।\nकारण (R): कालीबंगन में पकी ईंटों की कमी थी, जिसके कारण स्थानीय लकड़ी का उपयोग नाली बनाने के लिए किया गया।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): बनावली में अरीय (radial) सड़कों का नियोजन था।\nकारण (R): बनावली का नगर नियोजन परिपक्व हड़प्पा काल के मानक ग्रिड पैटर्न से विचलन को दर्शाता है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सुरकोटदा में मिले घोड़े के अवशेष साबित करते हैं कि हड़प्पावासी घुड़सवार योद्धा थे।\nकारण (R): सुरकोटदा से प्राप्त हड्डियों की पहचान पर तीव्र बहस है, और युद्ध में रथों या घोड़ों के उपयोग का कोई साक्ष्य नहीं है।", 3, "A असत्य है क्योंकि घुड़सवार योद्धा प्रमाणित नहीं हैं। R सत्य है।"),
    ("कथन (A): धोलावीरा की वास्तुकला सिंधु सभ्यता में अद्वितीय है।\nकारण (R): पकी ईंटों से बने अन्य नगरों के विपरीत, धोलावीरा में तराशे गए स्थानीय चूना पत्थर का व्यापक उपयोग हुआ था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): कालीबंगन से मिट्टी के चबूतरे पर बने अग्निकुंड मिले हैं।\nकारण (R): अग्निकुंडों की उपस्थिति अग्नि पूजा या यज्ञ अनुष्ठानिक गतिविधियों का संकेत देती है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): बनावली से कोई कृषि साक्ष्य नहीं मिला है।\nकारण (R): बनावली से उच्च गुणवत्ता वाले जौ के अनाज और एक खिलौना हल मिला है।", 3, "A असत्य है क्योंकि जौ और हल मिले हैं। R सत्य है।"),
    ("कथन (A): सुरकोटदा में कोई किलेबंदी नहीं थी।\nकारण (R): सुरकोटदा में पत्थरों से बना एक मजबूत किला और सुरक्षित प्रवेश द्वारों वाला निचला नगर था।", 3, "A असत्य है क्योंकि किला मजबूत रूप से सुरक्षित था। R सत्य है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding Dholavira:\n1. The city is divided into Citadel, Middle Town, and Lower Town.\n2. It contains 16 large stone-cut water reservoirs.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Dholavira's three-tier plan and water engineering."),
    ("Consider the following statements regarding Kalibangan:\n1. It contains pre-Harappan ploughed agricultural field furrows.\n2. It has yielded a series of brick-lined fire altars.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, reflecting Kalibangan's ploughed field and ritual altars."),
    ("Consider the following statements regarding Banawali:\n1. Its streets follow a radial or concentric pattern instead of a grid.\n2. A terracotta model of an agricultural plow was found here.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing Banawali's streets and toy plow find."),
    ("Consider the following statements regarding Surkotada:\n1. It has yielded uncontested remains of domestic riding horses.\n2. It completely lacked any fortification walls.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct: The horse remains are highly contested, and the site was strongly fortified with stone walls."),
    ("Consider the following statements regarding Dholavira's signboard:\n1. It was found on the floor of a gateway structure.\n2. The inscription contains ten characters written in Sanskrit.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: The letters are in the undeciphered Indus script, not Sanskrit.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("धोलावीरा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह शहर किला, मध्य नगर और निचले नगर में विभाजित है।\n2. यहाँ पत्थर काटकर बनाए गए 16 बड़े जलाशय मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो धोलावीरा के तीन भागों और विशाल जलाशयों को दर्शाते हैं।"),
    ("कालीबंगन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से पूर्व-हड़प्पा कालीन जुते हुए खेत के निशान मिले हैं।\n2. यहाँ ईंटों के चबूतरों पर अग्निकुंडों की कतार मिली है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो कालीबंगन के जुते हुए खेत और अग्निकुंडों को दर्शाते हैं।"),
    ("बनावली के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ की सड़कें ग्रिड के बजाय अरीय (radial) प्रतिरूप का पालन करती थीं।\n2. यहाँ से मिट्टी का बना खिलौना हल मिला है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो बनावली की सड़कों और खिलौने हल को दर्शाते हैं।"),
    ("सुरकोटदा के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यहाँ से पालतू सवारी वाले घोड़ों के निर्विवाद साक्ष्य मिले हैं।\n2. इस शहर में सुरक्षा दीवारों का पूर्ण अभाव था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों में से कोई भी कथन सही नहीं है: घोड़े के साक्ष्य विवादास्पद हैं और शहर पत्थर की मजबूत दीवारों से सुरक्षित था।"),
    ("धोलावीरा के साइनबोर्ड के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. यह एक विशाल प्रवेश द्वार के फर्श पर गिरा हुआ मिला था।\n2. इसमें संस्कृत भाषा में लिखे दस बड़े अक्षर मिले हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है: अक्षर सिंधु लिपि में हैं, संस्कृत में नहीं।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why/How/Case/Teach (12)
for q, sol in [
    ("Why did the Dholavirans build massive stone-cut water reservoirs?", "To store seasonal rainwater runoff in the arid region of Kutch where perennial freshwater rivers were absent and groundwater was brackish."),
    ("Why is the ploughed field at Kalibangan significant?", "It provides the earliest evidence of grid-pattern agricultural plowing in the subcontinent, showing that they grew two different crops simultaneously."),
    ("Why did Banawali develop a radial town layout?", "It represents a regional variation or planning deviation where streets radiated from the citadel, possibly due to local topographies or slower expansion.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("धोलावीरा के निवासियों ने पत्थर काटकर विशाल जलाशय क्यों बनाए?", "कच्छ के शुष्क क्षेत्र में मौसमी वर्षा के जल को संचित करने के लिए, क्योंकि यहाँ बारहमासी नदियाँ नहीं थीं और भूजल खारा था।"),
    ("कालीबंगन का जुता हुआ खेत क्यों महत्वपूर्ण है?", "यह उपमहाद्वीप में समकोण ग्रिड पर जुताई का सबसे प्राचीन प्रमाण है, जो एक साथ दो अलग-अलग फसलें उगाने की तकनीक को दर्शाता है।"),
    ("बनावली में सड़कों का लेआउट अरीय (radial) क्यों विकसित हुआ?", "यह नगर नियोजन में एक स्थानीय भिन्नता को दर्शाता है जहाँ सड़कें किले से बाहर की ओर जाती थीं, जो शायद भौगोलिक स्थिति के कारण था।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("How did Dholavira's hydraulic system collect water?", "By constructing stone dams across seasonal streams (Manhar and Mansar) and channeling the collected runoff into massive stone-cut reservoirs surrounding the citadel."),
    ("How did Kalibangan agriculturalists plow fields?", "By using wooden plows drawn by oxen, creating shallow crossed furrows to sow crops with different heights (like mustard and chickpea) together."),
    ("How did Surkotada's citadel protect its inhabitants?", "By constructing massive rubble stone fortifications with thick watchtowers and a heavily protected gateway, separating the citadel and residential sectors.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("धोलावीरा की जल प्रणाली पानी कैसे इकट्ठा करती थी?", "मौसमी नदियों (मनहर और मनसर) पर पत्थर के बांध बनाकर पानी को मोड़ा जाता था और उसे शहर के चारों ओर बने जलाशयों में संचित किया जाता था।"),
    ("कालीबंगन के किसान खेतों की जुताई कैसे करते थे?", "बैलों द्वारा खींचे जाने वाले लकड़ी के हलों का उपयोग करके, जिससे समकोण पर काटती नालियां बनती थीं ताकि दो अलग-अलग फसलों (जैसे सरसों और चना) को साथ बोया जा सके।"),
    ("सुरकोटदा के किले ने निवासियों की सुरक्षा कैसे की?", "मलबे के पत्थरों की विशाल दीवारों, ऊंचे बुर्जों और एक संकरे किलेबंद प्रवेश द्वार का निर्माण करके, जो किले और आवासीय क्षेत्र दोनों को सुरक्षा प्रदान करता था।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("Case Study: Dholavira's Water Conservation System", "An network of 16 stone-cut reservoirs capable of storing over 250,000 cubic meters of water. The system displays advanced understanding of slope, check dams, and sedimentation control, showing how Harappans adapted to arid conditions."),
    ("Case Study: The Kalibangan Ploughed Field", "Excavations revealed a grid pattern of furrows in pre-mature levels. The north-south furrows are spaced closely while east-west furrows are wider, which matches modern Rajasthani practices of planting mustard and gram together."),
    ("Case Study: The Surkotada Citadel and Fortifications", "A small, heavily fortified site built of stone rubble and mud brick. Features a central gateway with a ramp and guard rooms, demonstrating that even small peripheral outposts in Kutch had strong military defenses.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: धोलावीरा की जल संचयन प्रणाली", "16 जलाशयों का एक तंत्र जो 2,50,000 घन मीटर से अधिक पानी संचित कर सकता था। यह प्रणाली ढलान, बांधों और गाद नियंत्रण के उन्नत ज्ञान को दर्शाती है, जो शुष्क परिस्थितियों में जीवन को संभव बनाती थी।"),
    ("केस स्टडी: कालीबंगन का जुता हुआ खेत", "पूर्व-हड़प्पा स्तरों में ग्रिड पैटर्न पर जुताई के निशान मिले। उत्तर-दक्षिण दिशा की गलियाँ संकरी और पूर्व-पश्चिम की चौड़ी थीं, जो आधुनिक राजस्थान में सरसों और चने को साथ बोने की प्रथा से मेल खाती हैं।"),
    ("केस स्टडी: सुरकोटदा की किलेबंदी", "मलबे के पत्थरों और कच्ची ईंटों से बना एक छोटा, अत्यधिक सुरक्षित शहर। इसमें गार्ड रूम और रैंप वाला एक केंद्रीय प्रवेश द्वार था, जो दर्शाता है कि सीमावर्ती चौकियों पर सुरक्षा व्यवस्था बहुत मजबूत थी।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("Teach the Concept: Dholavira's Three-Tier City Structure", "Explain that Dholavira is divided into a Citadel (ruling class), a Middle Town (bureaucrats and merchants), and a Lower Town (artisans), all enclosed by stone fortification walls, unlike the two-tier brick layout of eastern sites."),
    ("Teach the Concept: Harappan Fire Altars", "Explain the fire altars found at Kalibangan: clay-lined pits containing charcoal, ash, and a central clay pillar. They are interpreted as evidence of Vedic-like fire worship, though this remains debated."),
    ("Teach the Concept: The Horse in Harappan Archaeology", "Explain the horse bone controversy: Surkotada reported horse teeth and bones in late levels, but many scholars identify them as wild ass (khur) or post-Harappan intrusions, as horses are not depicted on seals.")
]:
    s3_mastery_eng.append({"type": "Teach the Concept", "q": q, "sol": sol})

for q, sol in [
    ("अवधारणा को समझें: धोलावीरा का त्रि-स्तरीय नगर नियोजन", "समझाएं कि धोलावीरा तीन भागों: किला (शासक), मध्य नगर (अधिकारी/व्यापारी) और निचला नगर (कारीगर) में बंटा था, और सभी भाग पत्थर की दीवारों से सुरक्षित थे, जो इसे अन्य शहरों से अलग बनाता है।"),
    ("अवधारणा को समझें: हड़प्पा सभ्यता में अग्निकुंड", "कालीबंगन में मिले अग्निकुंड समझाएं: मिट्टी के गड्ढे जिनमें कोयला, राख और बीच में एक मिट्टी का स्तंभ था। इसे वैदिक यज्ञ कुंडों की तरह अग्नि पूजा का प्रमाण माना जाता है, हालांकि यह अभी भी बहस का विषय है।"),
    ("अवधारणा को समझें: हड़प्पा पुरातत्व में घोड़ा (The Horse)", "घोड़े के साक्ष्यों पर बहस समझाएं: सुरकोटदा से दांत और हड्डियां मिलने की बात कही गई, लेकिन कई विद्वान इन्हें जंगली गधे (खुर) की हड्डियां मानते हैं, क्योंकि मुहरों पर घोड़े का कोई चित्र नहीं मिला है।")
]:
    s3_mastery_hin.append({"type": "Teach the Concept", "q": q, "sol": sol})


# =========================================================================
# WRITE TO FILES
# =========================================================================
# Inject English
with open(ENG_PATH, "r", encoding="utf-8") as f:
    eng_data = json.load(f)

eng_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_eng
eng_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_eng
eng_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_eng

with open(ENG_PATH, "w", encoding="utf-8") as f:
    json.dump(eng_data, f, ensure_ascii=False, indent=2)

print("English content updated successfully with 186 questions!")

# Inject Hindi
with open(HIN_PATH, "r", encoding="utf-8") as f:
    hin_data = json.load(f)

hin_data["deepDive"]["sections"][0]["masteryZone"] = s1_mastery_hin
hin_data["deepDive"]["sections"][1]["masteryZone"] = s2_mastery_hin
hin_data["deepDive"]["sections"][2]["masteryZone"] = s3_mastery_hin

with open(HIN_PATH, "w", encoding="utf-8") as f:
    json.dump(hin_data, f, ensure_ascii=False, indent=2)

print("Hindi content updated successfully with 186 questions!")
print(f"Lengths: S1={len(s1_mastery_eng)} | S2={len(s2_mastery_eng)} | S3={len(s3_mastery_eng)}")
