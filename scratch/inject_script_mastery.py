import json
import os

ENG_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Script-and-Language\content.json"
HIN_PATH = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\HarappanIndus-Valley-Civilisation\Script-and-Language\hi\content.json"

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
# SECTION 1: CHARACTERISTICS, DECIPHERMENT ATTEMPTS & WRITING DIRECTION
# =========================================================================
s1_mastery_eng = []
s1_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("What is the primary archaeological evidence that the Harappan script was written from right to left?", ["The compression or cramping of symbols on the left margin of seals", "The alphabetical order starting with vowels on the right", "The presence of bilingual plaques in Mesopotamia", "The use of iron pens that left deep grooves on the right side"], 0, "The cramping of symbols on the left margin of seals proves the scribe ran out of space when writing from right to left."),
    ("The total number of distinct signs identified in the Indus script is estimated to be between:", ["20 and 30", "100 and 150", "375 and 400", "1000 and 1200"], 2, "Mainstream concordances identify between 375 and 400 distinct symbols in the script."),
    ("The term 'Boustrophedon' writing system refers to:", ["Writing that is carved only on stone structures", "Writing that alternates direction from line to line", "A script that uses only animal-themed pictographs", "A system read vertically from bottom to top"], 1, "Boustrophedon literally means 'ox-turning' and refers to text alternating directions line-by-line."),
    ("Linguistically, the Harappan script is best categorized as a:", ["Purely alphabetic script", "Logo-syllabic script", "Purely pictographic script", "Cuneiform phonetic script"], 1, "It is logo-syllabic, where signs represent both words (logograms) and phonetic syllables."),
    ("What is the average number of signs found in a standard Harappan inscription?", ["Around 5 signs", "Around 25 signs", "Around 50 signs", "Around 100 signs"], 0, "The average inscription length is extremely short, about 5 signs, with the longest containing 26.")
]:
    s1_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("हड़प्पा लिपि के दाएं से बाएं लिखे जाने का प्राथमिक पुरातात्विक साक्ष्य क्या है?", ["मुहरों के बाएं किनारे पर अक्षरों का संकुचन या सघन होना", "दाहिनी ओर से स्वरों से शुरू होने वाला वर्णमाला क्रम", "मेसोपोटामिया में द्विभाषी पट्टियों की उपस्थिति", "लोहे के कलमों का उपयोग जो दाईं ओर गहरे निशान छोड़ते थे"], 0, "मुहरों के बाएं किनारे पर चिन्हों का संकुचन यह सिद्ध करता है कि दाएं से बाएं लिखते समय अंत में जगह कम पड़ गई थी।"),
    ("सिंधु लिपि में पहचाने गए विशिष्ट चिन्हों की कुल संख्या लगभग कितनी अनुमानित है?", ["20 और 30 के बीच", "100 और 150 के बीच", "375 और 400 के बीच", "1000 और 1200 के बीच"], 2, "मुख्य संकलन ग्रंथों के अनुसार सिंधु लिपि में 375 से 400 के बीच विशिष्ट चिन्ह मिले हैं।"),
    ("'बोउस्ट्रोफेडन' (Boustrophedon) लेखन प्रणाली का तात्पर्य क्या है?", ["लेखन जो केवल पत्थर की संरचनाओं पर खोदा जाता है", "लेखन जो पंक्ति-दर-पंक्ति अपनी दिशा बदलता है", "एक लिपि जो केवल पशु-विषयक चित्रलेखों का उपयोग करती है", "नीचे से ऊपर की ओर लंबवत पढ़ी जाने वाली प्रणाली"], 1, "बोउस्ट्रोफेडन का शाब्दिक अर्थ है 'बैल का मुड़ना', जो प्रत्येक पंक्ति में लेखन दिशा के बदलने को दर्शाता है।"),
    ("भाषाई रूप से हड़प्पा लिपि को किस वर्ग में वर्गीकृत किया जा सकता है?", ["पूर्णतः वर्णमालात्मक लिपि", "लोगो-सिलेबिक (शब्द-अक्षरात्मक) लिपि", "पूर्णतः चित्रात्मक लिपि", "कीलकाक्षर (cuneiform) ध्वन्यात्मक लिपि"], 1, "यह लोगो-सिलेबिक है, जहाँ चिन्ह शब्दों और अक्षरों (ध्वनियों) दोनों को दर्शाते हैं।"),
    ("एक मानक हड़प्पा अभिलेख में पाए जाने वाले चिन्हों की औसत संख्या कितनी है?", ["लगभग 5 चिन्ह", "लगभग 25 चिन्ह", "लगभग 50 चिन्ह", "लगभग 100 चिन्ह"], 0, "अभिलेखों की औसत लंबाई अत्यंत संक्षिप्त है, लगभग 5 चिन्ह, और सबसे लंबा लेख 26 चिन्हों का है।")
]:
    s1_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following indicate that the Indus script was written from right to left? (Select all that apply)", ["Cramping of signs on the left margins of seals", "Overlapping strokes on pottery incisions where left strokes overlap right ones", "Symmetric designs that can only be carved from the right side", "Bilingual translations engraved on Mesopotamian boundary stones"], [0, 1], "Left margin cramping and overlapping pottery strokes prove right-to-left writing direction."),
    ("Select the structural characteristics of the Harappan logo-syllabic script: (Select all that apply)", ["Contains between 375 and 400 distinct signs", "Too many signs for an alphabet but too few for a pictographic system", "Each character represents a word or a syllable", "Lacks any abstract geometric shapes, using only animal drawings"], [0, 1, 2], "The script has 375-400 signs, is logo-syllabic, and contains many abstract geometric symbols."),
    ("Why has the decipherment of the Indus script remained unsuccessful? (Select all that apply)", ["Lack of any bilingual inscription like the Rosetta Stone", "Unknown language family of the Harappan civilisation", "Extreme brevity of the recovered inscriptions", "Complete absence of any computerized concordances"], [0, 1, 2], "Decipherment is blocked by the lack of bilingual texts, unknown language family, and brief texts. Computer concordances do exist."),
    ("Which of the following directions of writing are observed in Harappan inscriptions? (Select all that apply)", ["Right to left in single-line inscriptions", "Alternating directions (Boustrophedon) in multi-line inscriptions", "Top-to-bottom vertical columns in all seals", "Left-to-right starting from the middle of the seal"], [0, 1], "Writing is right-to-left in single lines and alternates (Boustrophedon) in multi-line texts."),
    ("Identify the common graphic representations found in the script symbols: (Select all that apply)", ["Fish symbols with various modifying strokes", "U-shaped or jar-like signs", "Human-like figures carrying bows or sticks", "Exclusively Roman numerals and mathematical signs"], [0, 1, 2], "Fish signs, jar signs, and human-like figures are common; Roman numerals did not exist.")
]:
    s1_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन से साक्ष्य संकेत देते हैं कि सिंधु लिपि दाएं से बाएं लिखी गई थी? (सभी लागू विकल्प चुनें)", ["मुहरों के बाएं किनारे पर अक्षरों का संकुचित होना", "बर्तनों पर खुदे निशानों में बाईं ओर के स्ट्रोक का दाईं ओर के स्ट्रोक के ऊपर होना", "सममित डिजाइन जो केवल दाईं ओर से खोदे जा सकते हैं", "मेसोपोटामिया के सीमा पत्थरों पर उत्कीर्ण द्विभाषी अनुवाद"], [0, 1], "बाएं किनारे का संकुचन और मिट्टी के बर्तनों पर ओवरलैपिंग स्ट्रोक दाएं से बाएं लिखने को प्रमाणित करते हैं।"),
    ("हड़प्पा की लोगो-सिलेबिक लिपि के संरचनात्मक लक्षणों का चयन करें: (सभी लागू विकल्प चुनें)", ["इसमें 375 से 400 के बीच विशिष्ट चिन्ह हैं", "वर्णमाला के लिए बहुत अधिक चिन्ह हैं लेकिन चित्रलिपि के लिए बहुत कम", "प्रत्येक अक्षर किसी शब्द या ध्वनि का प्रतिनिधित्व करता है", "इसमें अमूर्त ज्यामितीय आकृतियों का पूर्ण अभाव है, केवल जानवरों के चित्र हैं"], [0, 1, 2], "सिंधु लिपि में 375-400 चिन्ह हैं, यह लोगो-सिलेबिक है, और इसमें कई अमूर्त ज्यामितीय संकेत हैं।"),
    ("सिंधु लिपि को पढ़ने में अभी तक सफलता क्यों नहीं मिल पाई है? (सभी लागू विकल्प चुनें)", ["रोसेटा स्टोन जैसी किसी द्विभाषी कुंजी का अभाव", "हड़प्पा सभ्यता के भाषा परिवार का अज्ञात होना", "प्राप्त अभिलेखों की लंबाई का अत्यधिक संक्षिप्त होना", "कंप्यूटरीकृत संकलन (concordances) का पूरी तरह से अभाव होना"], [0, 1, 2], "द्विभाषी शिलालेख का न होना, भाषा परिवार का अज्ञात होना और छोटे लेख होना मुख्य कारण हैं। कंप्यूटर इंडेक्स उपलब्ध हैं।"),
    ("हड़प्पा के अभिलेखों में निम्नलिखित में से लेखन की कौन सी दिशाएं देखी गई हैं? (सभी लागू विकल्प चुनें)", ["एकल-पंक्ति अभिलेखों में दाएं से बाएं लिखना", "बहु-पंक्ति अभिलेखों में वैकल्पिक दिशाएं (बोउस्ट्रोफेडन)", "सभी मुहरों पर ऊपर से नीचे लंबवत कॉलम होना", "मुहर के बीच से शुरू होकर बाएं से दाएं लिखना"], [0, 1], "एकल पंक्ति में दाएं से बाएं और बहु-पंक्ति में बोउस्ट्रोफेडन शैली का प्रयोग किया जाता था।"),
    ("लिपि के चिन्हों में पाए जाने वाले सामान्य रेखाचित्रों की पहचान करें: (सभी लागू विकल्प चुनें)", ["विभिन्न संशोधक रेखाओं के साथ मछली के चिन्ह", "यू-आकार (U-shaped) या घड़े जैसे चिन्ह", "धनुष या डंडा लिए हुए मानव जैसी आकृतियां", "विशेष रूप से रोमन अंक और गणितीय संकेत"], [0, 1, 2], "मछली का चिन्ह, यू-आकार का जार और मानव जैसी आकृतियां बहुत सामान्य हैं; रोमन अंक नहीं थे।")
]:
    s1_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Harappan script was a highly simplified alphabetical writing system consisting of 26 letters.", False, "It was logo-syllabic with 375-400 signs, not alphabetic."),
    ("The longest single inscription discovered in the Indus valley contains exactly 26 signs.", True, "True. The longest inscription, found on a seal or pottery sherd, contains 26 characters."),
    ("Boustrophedon writing style involves alternating directions of writing in consecutive lines.", True, "True. The text alternates: line 1 goes right-to-left, line 2 left-to-right, etc."),
    ("Sign cramping on the left margin of seals suggests that writing started from the left.", False, "False. Cramping on the left shows the writer ran out of space as they moved from right to left."),
    ("Archaeologists have found bilingual tablets in Harappa written in both Indus script and Sumerian cuneiform.", False, "False. No bilingual inscriptions have ever been found for the Indus script."),
    ("The 'fish' sign is one of the most common symbols in the Harappan script.", True, "True. The fish sign appears frequently and with several variants."),
    ("A concordance is a systematic compilation of all script signs, their variants, and positions.", True, "True. Concordances compiled by Mahadevan and Parpola are major resources for scholars."),
    ("There is direct evidence of paper or papyrus sheets being used by Harappan scribes.", False, "False. No direct evidence of writing on organic paper or papyrus has survived.")
]:
    s1_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("हड़प्पा लिपि 26 अक्षरों से मिलकर बनी एक अत्यधिक सरल वर्णमाला प्रणाली थी।", False, "यह 375-400 चिन्हों वाली लोगो-सिलेबिक लिपि थी, वर्णमाला नहीं।"),
    ("सिंधु घाटी में खोजे गए सबसे लंबे एकल अभिलेख में ठीक 26 चिन्ह हैं।", True, "सत्य। सबसे लंबा अभिलेख 26 अक्षरों का है।"),
    ("बोउस्ट्रोफेडन लेखन शैली में लगातार आने वाली पंक्तियों में लेखन की दिशा बदलती है।", True, "सत्य। पहली पंक्ति दाएं से बाएं, दूसरी बाएं से दाएं चलती है।"),
    ("मुहरों के बाएं किनारे पर अक्षरों का संकुचन यह दर्शाता है कि लेखन बाईं ओर से शुरू हुआ था।", False, "असत्य। बाएं किनारे पर संकुचन दर्शाता है कि दाईं ओर से शुरू कर बाएं जाते समय जगह कम पड़ी थी।"),
    ("पुरातत्वविदों को हड़प्पा में सिंधु लिपि और सुमेरियन कीलकाक्षर दोनों में लिखी द्विभाषी पट्टियाँ मिली हैं।", False, "असत्य। सिंधु लिपि के लिए कोई भी द्विभाषी अभिलेख कभी नहीं मिला है।"),
    ("हड़प्पा लिपि में 'मछली' का चिन्ह सबसे आम प्रतीकों में से एक है।", True, "सत्य। मछली का चिन्ह विभिन्न संशोधनों के साथ बार-बार दिखाई देता है।"),
    ("एक संकलन ग्रंथ (concordance) सभी लिपि चिन्हों, उनके रूपों और स्थितियों का व्यवस्थित संकलन है।", True, "सत्य। महादेवन और पारपोला के संकलन ग्रंथ सिंधु लिपि के अध्ययन के मुख्य स्रोत हैं।"),
    ("हड़प्पा के लिपिकों द्वारा कागज या पेपिरस (papyrus) के पत्तों के उपयोग के प्रत्यक्ष साक्ष्य मिले हैं।", False, "असत्य। कागज या पेपिरस जैसी कार्बनिक सामग्रियों के कोई प्रत्यक्ष साक्ष्य नहीं बचे हैं।")
]:
    s1_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The writing direction that alternates from right-to-left and left-to-right is called ___________.", "Boustrophedon", "Boustrophedon is the term for alternating writing direction."),
    ("The total count of distinct characters in the Harappan script ranges between ___________.", "375 and 400", "Concordances list between 375 and 400 unique signs."),
    ("The compression of characters occurs on the ___________ margin of steatite seals.", "left", "Cramping is observed on the left margin, proving right-to-left writing."),
    ("A script in which characters stand for words or syllables is called ___________.", "logo-syllabic", "The logo-syllabic script uses signs for words and syllables."),
    ("The longest known Indus inscription contains a sequence of ___________ signs.", "26", "The longest inscription has 26 characters."),
    ("The graphic symbol resembling a ___________ is the most frequently occurring sign.", "fish", "The fish symbol is the most common graphic sign."),
    ("The decipherment of the Indus script is blocked by the absence of a ___________ text.", "bilingual", "No bilingual Rosetta-like stone has been found."),
    ("Overlapping incisions on pottery ___________ verify that right-to-left lines were drawn first.", "graffiti", "Overlapping lines on pottery graffiti confirm the right-to-left direction.")
]:
    s1_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("बारी-बारी से दाएं-से-बाएं और बाएं-से-दाएं बदलने वाली लेखन दिशा को ___________ कहा जाता है।", "बोउस्ट्रोफेडन", "बोउस्ट्रोफेडन (Boustrophedon) बारी-बारी से दिशा बदलने वाली लेखन शैली है।"),
    ("हड़प्पा लिपि में विशिष्ट अक्षरों की कुल संख्या ___________ के बीच है।", "375 और 400", "विभिन्न अध्ययनों में विशिष्ट चिन्हों की संख्या 375 से 400 के बीच मानी गई है।"),
    ("सेलखड़ी की मुहरों पर अक्षरों का संकुचन मुहर के ___________ किनारे पर दिखाई देता है।", "बाएं", "संकुचन बाएं (left) किनारे पर होता है, जो दाएं से बाएं लेखन को दर्शाता है।"),
    ("वह लिपि जिसमें अक्षर शब्दों या ध्वनियों का प्रतिनिधित्व करते हैं, ___________ कहलाती है।", "लोगो-सिलेबिक", "लोगो-सिलेबिक (logo-syllabic) लिपि में अक्षर शब्दों और ध्वनियों के सूचक होते हैं।"),
    ("सिंधु सभ्यता का सबसे लंबा ज्ञात अभिलेख ___________ चिन्हों का है।", "26", "सबसे लंबे अभिलेख में 26 चिन्ह मिले हैं।"),
    ("___________ जैसी दिखने वाली आकृति हड़प्पा लिपि में सबसे अधिक पाई जाने वाली आकृति है।", "मछली", "मछली (fish) की आकृति सबसे अधिक पाई जाने वाली आकृति है।"),
    ("सिंधु लिपि को पढ़ने का कार्य एक ___________ पाठ के अभाव में रुका हुआ है।", "द्विभाषी", "किसी भी द्विभाषी (bilingual) लेख के अभाव में लिपि रहस्य बनी हुई है।"),
    ("मिट्टी के बर्तनों के ___________ पर ओवरलैपिंग स्ट्रोक प्रमाणित करते हैं कि दाईं ओर के अक्षर पहले लिखे गए थे।", "भित्तिचित्रों", "पॉटरी के भित्तिचित्रों (graffiti) पर स्ट्रोक के ऊपर स्ट्रोक से दिशा की पुष्टि होती है।")
]:
    s1_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s1_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the writing terminology with its description:",
        "items": [{"left": "I. Boustrophedon", "key": "A"}, {"left": "II. Logo-syllabic", "key": "B"}, {"left": "III. Concordance", "key": "C"}],
        "options": [{"val": "A", "text": "A. Alternating writing direction line by line"}, {"val": "B", "text": "B. Signs representing words or syllables"}, {"val": "C", "text": "C. Systematic catalog of script symbols and occurrences"}],
        "sol": "Boustrophedon is alternating direction, logo-syllabic represents words/syllables, and concordance is the catalog."
    },
    {
        "type": "Match the Following",
        "q": "Match the script statistics with their significance:",
        "items": [{"left": "I. 375 to 400", "key": "A"}, {"left": "II. 26", "key": "B"}, {"left": "III. 5", "key": "C"}],
        "options": [{"val": "A", "text": "A. Count of distinct signs in the logo-syllabic script"}, {"val": "B", "text": "B. Maximum signs in the longest single inscription"}, {"val": "C", "text": "C. Average sign count in a standard inscription"}],
        "sol": "375-400 signs, 26 is the longest text length, and 5 is the average text length."
    },
    {
        "type": "Match the Following",
        "q": "Match the archaeological observation with its logical deduction:",
        "items": [{"left": "I. Sign cramping on left margin", "key": "A"}, {"left": "II. Overlapping incisions on pots", "key": "B"}, {"left": "III. High number of unique signs", "key": "C"}],
        "options": [{"val": "A", "text": "A. Scribe wrote from right to left"}, {"val": "B", "text": "B. Right-hand strokes were carved first"}, {"val": "C", "text": "C. Script is logo-syllabic rather than alphabetical"}],
        "sol": "Cramping proves right-to-left, overlapping proves right stroke first, and high sign count proves logo-syllabic."
    }
])

s1_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "लेखन शब्दावली को उसके विवरण से सुमेलित करें:",
        "items": [{"left": "I. बोउस्ट्रोफेडन", "key": "A"}, {"left": "II. लोगो-सिलेबिक", "key": "B"}, {"left": "III. संकलन ग्रंथ", "key": "C"}],
        "options": [{"val": "A", "text": "A. पंक्ति-दर-पंक्ति बदलती लेखन दिशा"}, {"val": "B", "text": "B. शब्दों या ध्वनियों को दर्शाने वाले चिन्ह"}, {"val": "C", "text": "C. चिन्हों और उनकी आवृतियों की व्यवस्थित सूची"}],
        "sol": "बोउस्ट्रोफेडन का अर्थ बदलती दिशा है, लोगो-सिलेबिक शब्दों/ध्वनियों का सूचक है, और संकलन ग्रंथ व्यवस्थित सूची है।"
    },
    {
        "type": "Match the Following",
        "q": "लिपि के आंकड़ों को उनके महत्व से सुमेलित करें:",
        "items": [{"left": "I. 375 से 400", "key": "A"}, {"left": "II. 26", "key": "B"}, {"left": "III. 5", "key": "C"}],
        "options": [{"val": "A", "text": "A. लोगो-सिलेबिक लिपि में विशिष्ट चिन्हों की संख्या"}, {"val": "B", "text": "B. सबसे लंबे एकल अभिलेख में चिन्हों की संख्या"}, {"val": "C", "text": "C. एक मानक अभिलेख में चिन्हों की औसत संख्या"}],
        "sol": "375-400 विशिष्ट चिन्ह हैं, 26 सबसे लंबे लेख का आकार है, और 5 औसत चिन्ह संख्या है।"
    },
    {
        "type": "Match the Following",
        "q": "पुरातात्विक साक्ष्य को उसके तार्किक निष्कर्ष से सुमेलित करें:",
        "items": [{"left": "I. बाएं किनारे पर संकुचन", "key": "A"}, {"left": "II. बर्तनों पर ओवरलैपिंग स्ट्रोक", "key": "B"}, {"left": "III. विशिष्ट चिन्हों की बड़ी संख्या", "key": "C"}],
        "options": [{"val": "A", "text": "A. लेखक दाईं ओर से बाईं ओर लिखता था"}, {"val": "B", "text": "B. दाईं ओर का स्ट्रोक पहले काटा गया था"}, {"val": "C", "text": "C. लिपि वर्णमालात्मक नहीं बल्कि लोगो-सिलेबिक है"}],
        "sol": "संकुचन से दाएं से बाएं सिद्ध होता है, ओवरलैपिंग से दायां स्ट्रोक पहले सिद्ध होता है, और चिन्हों की बड़ी संख्या से लोगो-सिलेबिक सिद्ध होता है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("What is the main direction of writing in single-line Indus inscriptions?", "From right to left."),
    ("What is the literal meaning of 'Boustrophedon'?", "Turning like an ox while plowing a field."),
    ("Why is the script termed logo-syllabic?", "Because the sign count is too high for an alphabet and too low for pure pictography, representing words and syllables."),
    ("What is the maximum length of a single continuous inscription found?", "26 signs."),
    ("What evidence on pottery sherds confirms right-to-left writing?", "Overlapping lines where the stroke on the left overrides the stroke on the right."),
    ("Has the Harappan script been deciphered?", "No, it remains undeciphered."),
    ("Which graphic symbol is most frequently repeated in the script?", "The fish symbol."),
    ("What key archaeological discovery is missing that would easily help decipher the script?", "A bilingual inscription (like the Rosetta Stone).")
]:
    s1_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("एकल-पंक्ति के सिंधु अभिलेखों में लेखन की मुख्य दिशा क्या है?", "दाएं से बाएं।"),
    ("शब्द 'बोउस्ट्रोफेडन' का शाब्दिक अर्थ क्या है?", "खेत जोतते समय बैल का मुड़ना।"),
    ("लिपि को लोगो-सिलेबिक क्यों कहा जाता है?", "क्योंकि चिन्हों की संख्या वर्णमाला के लिए बहुत अधिक और शुद्ध चित्रलिपि के लिए बहुत कम है, जो शब्दों और अक्षरों को दर्शाती है।"),
    ("प्राप्त सबसे लंबे निरंतर अभिलेख में अधिकतम कितने चिन्ह हैं?", "26 चिन्ह।"),
    ("मिट्टी के बर्तनों पर कौन सा साक्ष्य दाएं से बाएं लेखन की पुष्टि करता है?", "ओवरलैपिंग रेखाएं जहाँ बाईं ओर का स्ट्रोक दाईं ओर के स्ट्रोक के ऊपर चढ़ता है।"),
    ("क्या हड़प्पा लिपि को सफलतापूर्वक पढ़ा जा चुका है?", "नहीं, यह अभी तक अपठित है।"),
    ("लिपि में कौन सा रेखाचित्र सबसे अधिक दोहराया गया है?", "मछली (fish) का चिन्ह।"),
    ("कौन सी प्रमुख पुरातात्विक खोज गायब है जो लिपि को पढ़ने में सहायक होती?", "एक द्विभाषी शिलालेख (जैसे मिस्र का रोसेटा स्टोन)।")
]:
    s1_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Harappan script was written from right to left.\nReason (R): Inscriptions on steatite seals show sign cramping on their left margins.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Harappan script is classified as alphabetical.\nReason (R): The script contains between 375 and 400 distinct signs, which matches the size of an alphabet.", 3, "A is false and R is false (the high sign count proves it is logo-syllabic, not alphabetical)."),
    ("Assertion (A): Long Harappan inscriptions are written in the Boustrophedon style.\nReason (R): Scribes always started every line on the left margin and wrote towards the right.", 2, "A is true but R is false (Boustrophedon alternates directions rather than starting on the left)."),
    ("Assertion (A): Mainstream scholars agree that the Indus script has not been successfully deciphered.\nReason (R): There is no bilingual inscription to provide a key for translating the characters.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Scribes carved the characters on seals in reverse (mirror-image).\nReason (R): The seals were designed to stamp clay sealings, which would display the correct reading orientation.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The average length of Indus inscriptions is about 50 signs.\nReason (R): The longest single inscription found contains only 26 signs.", 3, "A is false because average length is 5 signs. R is true."),
    ("Assertion (A): Pottery graffiti overlaps confirm the writing direction.\nReason (R): Leftward strokes were carved before rightward strokes, showing a left-to-right flow.", 2, "A is true but R is false (right strokes were carved first, confirming right-to-left flow)."),
    ("Assertion (A): Scribes used perishable materials for administrative books.\nReason (R): No administrative paper, palm leaves, or wood documents have survived in the archaeological record.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s1_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा लिपि दाएं से बाएं लिखी जाती थी।\nकारण (R): सेलखड़ी की मुहरों पर बने लेखों में बाएं किनारे पर अक्षरों का संकुचन दिखाई देता है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): हड़प्पा लिपि को वर्णमाला के रूप में वर्गीकृत किया गया है।\nकारण (R): लिपि में 375 से 400 के बीच विशिष्ट चिन्ह हैं, जो एक वर्णमाला के आकार के अनुकूल है।", 3, "A असत्य है और R भी असत्य है (चिन्हों की बड़ी संख्या लोगो-सिलेबिक सिद्ध करती है, वर्णमाला नहीं)।"),
    ("कथन (A): लंबे हड़प्पा अभिलेख बोउस्ट्रोफेडन शैली में लिखे गए हैं।\nकारण (R): लेखक हमेशा प्रत्येक पंक्ति को बाएं किनारे से शुरू करके दाईं ओर लिखता था।", 2, "A सत्य है लेकिन R असत्य है (बोउस्ट्रोफेडन में दिशा बदलती है, हर पंक्ति बाएं से शुरू नहीं होती)।"),
    ("कथन (A): मुख्यधारा के विद्वान सहमत हैं कि सिंधु लिपि को अभी तक पढ़ा नहीं जा सका है।\nकारण (R): अक्षरों के अनुवाद के लिए कोई भी द्विभाषी अभिलेख उपलब्ध नहीं है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): लेखक मुहरों पर अक्षरों को विपरीत (दर्पण-छवि) रूप में खोदते थे।\nकारण (R): मुहरों का उपयोग मिट्टी पर छाप लगाने के लिए किया जाता था, ताकि छाप पर अक्षर सीधे दिखाई दें।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सिंधु अभिलेखों की औसत लंबाई लगभग 50 चिन्ह है।\nकारण (R): प्राप्त सबसे लंबे एकल अभिलेख में केवल 26 चिन्ह हैं।", 3, "A असत्य है क्योंकि औसत लंबाई 5 चिन्ह है। R सत्य है।"),
    ("कथन (A): मिट्टी के बर्तनों के भित्तिचित्रों के ओवरलैप लेखन की दिशा की पुष्टि करते हैं।\nकारण (R): बाईं ओर के स्ट्रोक पहले लिखे गए थे, जो बाएं से दाएं प्रवाह दर्शाते हैं।", 2, "A सत्य है लेकिन R असत्य है (दाईं ओर के स्ट्रोक पहले लिखे गए थे जो दाएं से बाएं प्रवाह दर्शाते हैं)।"),
    ("कथन (A): प्रशासनिक बही-खातों के लिए लेखकों ने नष्ट होने वाली वस्तुओं का उपयोग किया होगा।\nकारण (R): पुरातात्विक साक्ष्यों में कोई भी प्रशासनिक कागज, ताड़ के पत्ते या लकड़ी के दस्तावेज नहीं बचे हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s1_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the writing direction:\n1. Single-line inscriptions were written from right to left.\n2. The Boustrophedon style alternates directions in multi-line inscriptions.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing single-line and multi-line writing directions."),
    ("Consider the following statements regarding the number of signs:\n1. The Indus script contains fewer than 50 distinct characters.\n2. The script is logo-syllabic in nature.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: it contains 375-400 distinct signs, far more than 50."),
    ("Consider the following statements regarding decipherment hurdles:\n1. The discovery of bilingual seals in Sumeria resolved the translation of the script.\n2. The longest Indus text contains 26 characters, which limits statistical decoding.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: no bilingual seals have been discovered."),
    ("Consider the following statements regarding sign cramping:\n1. Scribes cramped signs on the right margin of seals.\n2. Scribes started writing from left to right on standard seals.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct. Cramping is on the left margin, showing right-to-left writing."),
    ("Consider the following statements regarding the fish symbol:\n1. The fish symbol is the most frequently occurring sign in the script corpus.\n2. The symbol is often modified with strokes or fins to represent different values.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the frequency and modifications of the fish symbol.")
]:
    s1_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("लेखन की दिशा के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. एकल-पंक्ति वाले अभिलेख दाएं से बाएं लिखे जाते थे।\n2. बोउस्ट्रोफेडन शैली बहु-पंक्ति वाले अभिलेखों में बारी-बारी से दिशा बदलती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो एकल और बहु-पंक्ति लेखन दिशा का वर्णन करते हैं।"),
    ("चिन्हों की संख्या के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सिंधु लिपि में 50 से कम विशिष्ट अक्षर हैं।\n2. लिपि स्वरूप में लोगो-सिलेबिक (शब्द-अक्षरात्मक) है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि इसमें 375-400 विशिष्ट चिन्ह हैं।"),
    ("लिपि को पढ़ने की बाधाओं के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सुमेरिया में द्विभाषी मुहरों की खोज से लिपि का अनुवाद हो गया था।\n2. सबसे लंबे सिंधु पाठ में 26 अक्षर हैं, जो सांख्यिकीय डिकोडिंग को सीमित करते हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि कोई द्विभाषी मुहर नहीं मिली है।"),
    ("अक्षरों के संकुचन (cramping) के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. लेखक मुहरों के दाहिने किनारे पर अक्षरों को संकुचित करते थे।\n2. लेखक मानक मुहरों पर बाएं से दाएं लिखना शुरू करते थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। संकुचन बाएं किनारे पर होता है, जो दाएं से बाएं लेखन दर्शाता है।"),
    ("मछली के चिन्ह के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. मछली का चिन्ह पूरी लिपि में सबसे अधिक पाया जाने वाला चिन्ह है।\n2. इस चिन्ह को अक्सर विभिन्न अर्थों के लिए रेखाओं या पंखों के साथ संशोधित किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मछली के चिन्ह की आवृत्ति और उसके रूपों का वर्णन करते हैं।")
]:
    s1_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did Harappan scribes compress their letters on the left margin of seals?", "Because they wrote from right to left and miscalculated the space remaining as they approached the left margin."),
    ("Why is a bilingual inscription necessary to decipher an unknown script like the Indus script?", "It provides a parallel translation in a known language, allowing scholars to map known words and phonetics directly to the unknown signs."),
    ("Why is the script called logo-syllabic instead of alphabetical?", "Because the sign count of 375-400 is too large to represent individual alphabetic sounds, but too small for purely pictographic words, representing both words and syllables.")
]:
    s1_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("हड़प्पा के लिपिक मुहरों के बाएं किनारे पर अक्षरों को क्यों सटाते थे?", "क्योंकि वे दाएं से बाएं लिखते थे और बाएं किनारे की ओर बढ़ते हुए बची हुई जगह का गलत अनुमान लगा लेते थे।"),
    ("सिंधु लिपि जैसी अज्ञात लिपि को पढ़ने के लिए एक द्विभाषी अभिलेख क्यों आवश्यक है?", "यह ज्ञात भाषा में समानांतर अनुवाद प्रदान करता है, जिससे विद्वान ज्ञात शब्दों और ध्वनियों को अज्ञात चिन्हों से जोड़ सकते हैं।"),
    ("लिपि को वर्णमाला के बजाय लोगो-सिलेबिक क्यों कहा जाता है?", "क्योंकि 375-400 चिन्हों की संख्या वर्णमाला के ध्वनियों को दर्शाने के लिए बहुत अधिक है, लेकिन शुद्ध चित्रलिपि के लिए कम है, जो शब्दों और अक्षरों दोनों को दर्शाती है।")
]:
    s1_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did epigraphers prove the right-to-left writing direction of the script?", "By analyzing the physical crowding of signs on the left edge of seals and showing that incisions on the left overrode those on the right in pottery graffiti."),
    ("How does the Boustrophedon writing style change layout from line to line?", "It alternates directions: line 1 runs right-to-left, line 2 curves down and runs left-to-right, line 3 runs right-to-left, and so on."),
    ("How did mirror-image carving of seals relate to their practical usage?", "Seals were carved in reverse so that when pressed into soft clay cargo tags, the resulting sealing impression would display the symbols in their correct, readable format.")
]:
    s1_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("पुरालेखविदों ने लिपि के दाएं से बाएं लिखे जाने को कैसे सिद्ध किया?", "मुहरों के बाएं किनारे पर अक्षरों के जमाव का विश्लेषण करके और यह दिखाकर कि बर्तनों पर बाईं ओर के कट दाईं ओर के कटों के ऊपर चढ़े हुए थे।"),
    ("बोउस्ट्रोफेडन लेखन शैली पंक्ति-दर-पंक्ति लेआउट को कैसे बदलती है?", "यह दिशा बदलती है: पहली पंक्ति दाएं से बाएं, दूसरी पंक्ति नीचे मुड़कर बाएं से दाएं, तीसरी पंक्ति दाएं से बाएं, और इसी तरह चलती है।"),
    ("मुहरों पर अक्षरों की दर्पण-छवि नक्काशी उनके व्यावहारिक उपयोग से कैसे जुड़ी थी?", "मुहरों को विपरीत दिशा में खोदा जाता था ताकि जब उन्हें माल के नरम मिट्टी के टैग पर दबाया जाए, तो प्राप्त छाप में चिन्ह सीधे और पठनीय रूप में दिखाई दें।")
]:
    s1_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: An archaeologist studies a steatite seal from Harappa and notices that the signs on the right are spaced widely, while the final two signs on the left are heavily cramped and overlapping. What deduction does this case study support?", "It supports the deduction that the seal was written from right to left, and that the scribe did not plan the spacing carefully beforehand."),
    ("Case Study: A newly found inscription contains a sequence of 26 symbols, making it the longest known Indus text. Scribes analyze it to find recurring grammatical patterns. Why does its length still hinder decryption?", "The text is still too short for statistical frequency analysis to isolate grammatical rules, syntax structures, or word combinations effectively."),
    ("Case Study: Compare the decoding of Egyptian hieroglyphs using the Rosetta Stone with the Indus script. What is the key difference in availability that explains why one was solved and the other remains unsolved?", "Egyptian hieroglyphs had the Rosetta Stone with parallel Greek and Demotic text. The Indus script lacks any multi-lingual or bilingual texts, leaving no point of comparison.")
]:
    s1_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: एक पुरातत्वविद हड़प्पा से प्राप्त सेलखड़ी की मुहर का अध्ययन करता है और पाता है कि दाईं ओर के अक्षरों में पर्याप्त स्थान है, जबकि बाईं ओर के अंतिम दो अक्षर संकुचित और ओवरलैप हैं। यह केस स्टडी किस निष्कर्ष का समर्थन करती है?", "यह निष्कर्ष देती है कि मुहर पर लेखन दाएं से बाएं किया गया था, और लेखक ने पहले से अक्षरों के बीच की जगह का सही नियोजन नहीं किया था।"),
    ("केस स्टडी: हाल ही में खोजे गए एक अभिलेख में 26 चिन्हों का क्रम है, जो इसे सबसे लंबा ज्ञात सिंधु पाठ बनाता है। लिपिक इसमें व्याकरणिक पैटर्न खोजने का प्रयास करते हैं। इसकी लंबाई अभी भी इसे पढ़ने में बाधा क्यों है?", "व्याकरणिक नियमों, वाक्य संरचनाओं या शब्द संयोजनों को अलग करने के लिए सांख्यिकीय आवृत्ति विश्लेषण (frequency analysis) के लिए यह लंबाई बहुत कम है।"),
    ("केस स्टडी: रोसेटा स्टोन के माध्यम से मिस्र के चित्रलेखों को पढ़ने और सिंधु लिपि की तुलना करें। उपलब्धता में कौन सा अंतर यह समझाता है कि एक हल हो गया और दूसरा अनसुलझा है?", "मिस्र के चित्रलेखों के पास समानांतर ग्रीक और डेमोटिक पाठ वाला रोसेटा स्टोन था। सिंधु लिपि में किसी भी बहुभाषी या द्विभाषी पाठ का पूर्ण अभाव है।")
]:
    s1_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the concept of 'Boustrophedon' to a beginner using a simple analogy.", "Boustrophedon means writing like a bull plowing a field. Instead of lifting the pen and returning to the start of the line, the scribe writes the first line from right to left, then drops to the next line and writes left to right, matching the continuous path of the ox."),
    ("Explain why the Indus script is categorized as 'Logo-syllabic' and not alphabetical.", "An alphabet uses around 20-40 characters to represent individual sounds. A logo-syllabic script uses hundreds of signs (like the Indus script's 375-400 signs) because each symbol represents a whole word (logogram) or a syllable sound, rather than a single letter."),
    ("Explain the phenomenon of 'Sign Cramping' and how it acts as evidence of writing direction.", "Sign cramping occurs when a scribe begins writing on one side of a seal and runs out of physical space as they reach the other edge, causing the final signs to be squished together. In Harappan seals, this squishing is consistently on the left, proving writing began on the right.")
]:
    s1_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक नौसिखिए को एक सरल सादृश्य का उपयोग करके 'बोउस्ट्रोफेडन' की अवधारणा समझाएं।", "बोउस्ट्रोफेडन का अर्थ है खेत जोतने वाले बैल की तरह लिखना। लाइन के अंत में पेन उठाकर वापस शुरुआत में ले जाने के बजाय, लेखक पहली लाइन दाएं से बाएं लिखता है, फिर अगली लाइन में नीचे जाकर बाएं से दाएं लिखता है, जो बैल के चलने के निरंतर मार्ग जैसा है।"),
    ("समझाएं कि सिंधु लिपि को 'लोगो-सिलेबिक' क्यों वर्गीकृत किया गया है, वर्णमाला के रूप में क्यों नहीं।", "वर्णमाला व्यक्तिगत ध्वनियों को दर्शाने के लिए लगभग 20-40 वर्णों का उपयोग करती है। लोगो-सिलेबिक लिपि सैकड़ों चिन्हों (जैसे सिंधु के 375-400 चिन्ह) का उपयोग करती है क्योंकि प्रत्येक प्रतीक एक एकल अक्षर के बजाय एक पूरे शब्द या ध्वनि का प्रतिनिधित्व करता है।"),
    ("अक्षरों के संकुचन (Sign Cramping) की घटना को समझाएं और यह कैसे लेखन की दिशा का प्रमाण है।", "संकुचन तब होता है जब लेखक मुहर के एक तरफ से लिखना शुरू करता है और दूसरे किनारे तक पहुँचते समय जगह कम पड़ जाती है, जिससे अंतिम अक्षर आपस में सट जाते हैं। हड़प्पा की मुहरों में यह संकुचन हमेशा बाईं ओर होता है, जो सिद्ध करता है कि लेखन दाईं ओर से शुरू हुआ था।")
]:
    s1_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 1 Mastery questions populated: {len(s1_mastery_eng)} (Eng), {len(s1_mastery_hin)} (Hin)")

# =========================================================================
# SECTION 2: KEY ARCHAEOLOGICAL INSCRIPTIONS
# =========================================================================
s2_mastery_eng = []
s2_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("At which Harappan site was the famous public 'Signboard' inscription discovered?", ["Mohenjo-daro", "Dholavira", "Harappa", "Kalibangan"], 1, "The ten-sign signboard was discovered at Dholavira in Gujarat."),
    ("The large symbols of the Dholavira Signboard were manufactured using which material?", ["White gypsum crystalline paste", "Baked terracotta clay", "Engraved limestone slabs", "Polished lapis lazuli inlays"], 0, "The letters were shaped out of white gypsum crystalline paste and mounted on wood."),
    ("On what class of objects are the vast majority of Harappan script inscriptions found?", ["Copper tablets", "Household pottery graffiti", "Square steatite seals", "Citadel gateways and pillars"], 2, "Steatite seals constitute the single largest category of objects bearing Indus writing."),
    ("Inscriptions on Indus copper tablets typically feature script signs on one side and what on the other?", ["A map of the city", "An animal figure", "A royal portrait", "A list of numbers"], 1, "Copper tablets typically carry script on one side and an animal image (e.g., unicorn) on the reverse."),
    ("What was the primary function of the steatite seals containing script and animal reliefs?", ["To serve as currency in daily transactions", "To stamp clay tags (sealings) to secure trade goods", "To act as religious gravestones in cemeteries", "To measure agricultural grain allocations"], 1, "Seals were stamped on wet clay sealings (tags) to secure packages and identify ownership in trade.")
]:
    s2_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("प्रसिद्ध सार्वजनिक 'सूचना-पट्ट' (Signboard) अभिलेख किस हड़प्पा स्थल से प्राप्त हुआ था?", ["मोहनजोदड़ो", "धोलावीरा", "हड़प्पा", "कालीबंगन"], 1, "दस अक्षरों वाला सूचना-पट्ट गुजरात के धोलावीरा से प्राप्त हुआ था।"),
    ("धोलावीरा सूचना-पट्ट के बड़े चिन्हों का निर्माण किस सामग्री से किया गया था?", ["सफेद जिप्सम का क्रिस्टलीय लेप", "पकी हुई मिट्टी (terracotta)", "नक्काशीदार चूना पत्थर के फलक", "पॉलिश किया हुआ लाजवर्द (lapis lazuli)"], 0, "सूचना-पट्ट के अक्षर सफेद जिप्सम के लेप से बने थे जिन्हें लकड़ी के बोर्ड पर जड़ा गया था।"),
    ("हड़प्पा लिपि के अधिकांश अभिलेख किस प्रकार की वस्तुओं पर पाए जाते हैं?", ["तांबे की पट्टियां", "घरेलू बर्तनों के भित्तिचित्र", "वर्गाकार सेलखड़ी की मुहरें", "किले के प्रवेश द्वार और स्तंभ"], 2, "सेलखड़ी (steatite) की मुहरें सिंधु लेखन धारण करने वाली वस्तुओं की सबसे बड़ी श्रेणी हैं।"),
    ("सिंधु तांबे की पट्टियों पर सामान्यतः एक तरफ लिपि चिन्ह और दूसरी तरफ क्या बना होता था?", ["शहर का नक्शा", "एक पशु की आकृति", "एक शाही चित्र", "संख्याओं की सूची"], 1, "तांबे की पट्टियों पर एक तरफ अक्षर और दूसरी तरफ जानवर (जैसे एक सींग वाला बैल) बना होता था।"),
    ("लिपि और पशु चित्रों वाली सेलखड़ी मुहरों का प्राथमिक कार्य क्या था?", ["दैनिक लेनदेन में मुद्रा के रूप में कार्य करना", "व्यापारिक माल की सुरक्षा के लिए मिट्टी की छाप (sealings) लगाना", "कब्रिस्तानों में धार्मिक कब्र के पत्थरों के रूप में कार्य करना", "कृषि अनाज के आवंटन को मापना"], 1, "मुहरों को व्यापारिक गठरी पर गीली मिट्टी की छाप लगाने और स्वामित्व की पहचान स्थापित करने के लिए इस्तेमाल किया जाता था।")
]:
    s2_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("On which of the following media has the Harappan script been discovered? (Select all that apply)", ["Steatite seals", "Copper and bronze tablets", "Domestic pottery sherds", "Inscribed ivory rods"], [0, 1, 2, 3], "Indus writing is found on seals, copper tablets, pottery, and ivory rods."),
    ("Select the key details regarding the Dholavira Signboard: (Select all that apply)", ["Features exactly ten symbols", "Mounted above the northern gateway of the Citadel", "Letters are approximately 37 cm high", "Deciphered as a tax warning to visiting traders"], [0, 1, 2], "The board has 10 signs, is 37 cm high, and was at the Citadel northern gate. It is undeciphered."),
    ("Which of the following functions did steatite seals perform? (Select all that apply)", ["Securing goods during long-distance maritime trade", "Identifying merchant ownership or clan identity", "Serving as amuletic charms for protection", "Serving as uniform legal coinage across the empire"], [0, 1, 2], "Seals secured goods, showed identity, and acted as amulets. They were not coinage."),
    ("Identify the features of Indus copper tablets: (Select all that apply)", ["Found primarily at Mohenjo-daro and Harappa", "Feature animal drawings on one side", "Engraved with script signs on the other side", "Used as physical mirrors for elite makeup"], [0, 1, 2], "Copper tablets have script and animals, found at Mohenjo-daro and Harappa. Mirrors were polished bronze plates, not tablets."),
    ("What findings confirm that writing was used by ordinary citizens, not just administrative elites? (Select all that apply)", ["Post-firing graffiti scratched on domestic potsherds", "Inscribed pottery found in commoners' Lower Town residential areas", "Terracotta bangles carrying tiny stamped script signs", "Large gold plaques with legal decrees found in slums"], [0, 1, 2], "Pottery graffiti and inscribed Lower Town artifacts show ordinary use. Gold plaques do not exist.")
]:
    s2_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से किन माध्यमों पर हड़प्पा लिपि की खोज की गई है? (सभी लागू विकल्प चुनें)", ["सेलखड़ी की मुहरें", "तांबे और कांसे की पट्टियां", "घरेलू बर्तनों के टुकड़े", "नक्काशीदार हाथीदांत की छड़ें"], [0, 1, 2, 3], "सिंधु लेखन मुहरों, तांबे की पट्टियों, बर्तनों और हाथीदांत की छड़ों पर पाया गया है।"),
    ("धोलावीरा सूचना-पट्ट के संबंध में सही विवरण चुनें: (सभी लागू विकल्प चुनें)", ["इसमें ठीक दस चिन्ह शामिल हैं", "यह किले के उत्तरी प्रवेश द्वार के ऊपर लगाया गया था", "इसके अक्षरों की ऊंचाई लगभग 37 सेमी है", "इसे व्यापारियों के लिए कर चेतावनी के रूप में पढ़ा गया है"], [0, 1, 2], "बोर्ड पर 10 चिन्ह हैं, प्रत्येक की ऊंचाई 37 सेमी है और इसे उत्तरी प्रवेश द्वार पर लगाया गया था। यह अपठित है।"),
    ("सेलखड़ी की मुहरों द्वारा निम्नलिखित में से कौन से कार्य किए जाते थे? (सभी लागू विकल्प चुनें)", ["लंबी दूरी के समुद्री व्यापार में माल को सुरक्षित करना", "व्यापारी के स्वामित्व या कुल की पहचान बताना", "सुरक्षा के लिए ताबीज के रूप में कार्य करना", "पूरे साम्राज्य में एक समान सिक्कों के रूप में कार्य करना"], [0, 1, 2], "मुहरें माल सुरक्षित करती थीं, पहचान बताती थीं और ताबीज का काम करती थीं। वे सिक्के नहीं थे।"),
    ("सिंधु तांबे की पट्टियों के लक्षणों की पहचान करें: (सभी लागू विकल्प चुनें)", ["मुख्य रूप से मोहनजोदड़ो और हड़प्पा में पाई गई हैं", "एक तरफ पशु चित्र होते हैं", "दूसरी तरफ लिपि चिन्ह खोदे गए हैं", "कुलीन वर्ग के श्रृंगार के लिए धातु के दर्पण का काम करती थीं"], [0, 1, 2], "तांबे की पट्टियाँ मोहनजोदड़ो और हड़प्पा में मिली हैं और उनमें पशु व लेख हैं। दर्पण अलग प्रकार के कांस्य प्लेट होते थे।"),
    ("कौन से साक्ष्य पुष्टि करते हैं कि लेखन का उपयोग केवल शासक वर्ग नहीं बल्कि आम नागरिक भी करते थे? (सभी लागू विकल्प चुनें)", ["घरेलू बर्तनों के टुकड़ों पर पकने के बाद खुरच कर लिखे गए भित्तिचित्र (graffiti)", "निचले नगर में आम निवासियों के घरों से मिले उत्कीर्ण बर्तन", "छोटे अक्षरों की छाप वाले पकी मिट्टी के कंगन", "मलिन बस्तियों से मिले कानूनी आदेशों वाले सोने के बड़े फलक"], [0, 1, 2], "बर्तनों के भित्तिचित्र और निचले नगर में बर्तनों पर लेख आम लोगों द्वारा लेखन के उपयोग को दर्शाते हैं। सोने के फलक नहीं मिले हैं।")
]:
    s2_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("The Dholavira Signboard was recovered from the southern gate of the Citadel.", False, "It was found near the northern gateway of the Citadel at Dholavira."),
    ("The letters of the Dholavira Signboard were made of white gypsum.", True, "True. Crystalline gypsum paste was used to make the letters."),
    ("Steatite (soapstone) was the primary raw material used for making Harappan seals.", True, "True. Steatite was preferred because it was soft to carve and hardened when fired."),
    ("Every single Indus seal discovered has a script inscription on it.", False, "False. Some seals only have animal figures or geometric designs without any script."),
    ("Copper tablets containing script are found in large quantities in almost every Harappan village.", False, "False. They are concentrated in major metropolitan sites like Mohenjo-daro and Harappa."),
    ("Indus script signs have been found scratched on terracotta bangles.", True, "True. Some bangles have tiny script stampings or scratchings."),
    ("The wood backing of the Dholavira Signboard decayed over time, leaving the gypsum inlays in the soil.", True, "True. The wooden frame rotted away, but the gypsum symbols fell and survived in the dirt."),
    ("Writing on pottery was exclusively executed before the pots were baked in the kiln.", False, "False. Much of it was post-firing graffiti, scratched onto the baked pots by their owners.")
]:
    s2_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("धोलावीरा का सूचना-पट्ट किले के दक्षिणी द्वार से प्राप्त किया गया था।", False, "यह धोलावीरा में किले के उत्तरी प्रवेश द्वार से प्राप्त हुआ था।"),
    ("धोलावीरा सूचना-पट्ट के अक्षर सफेद जिप्सम के बने थे।", True, "सत्य। सफेद क्रिस्टलीय जिप्सम लेप से इन अक्षरों को बनाया गया था।"),
    ("हड़प्पा की मुहरें बनाने के लिए सेलखड़ी (steatite) प्राथमिक कच्चा माल थी।", True, "सत्य। सेलखड़ी नरम पत्थर होने के कारण आसानी से काटी जा सकती थी और गर्म करने पर सख्त हो जाती थी।"),
    ("खोजे गए प्रत्येक सिंधु मुहर पर लिपि का एक लेख उत्कीर्ण है।", False, "असत्य। कुछ मुहरों पर बिना किसी लेख के केवल जानवरों के चित्र या ज्यामितीय डिजाइन हैं।"),
    ("लिपि युक्त तांबे की पट्टियां लगभग हर हड़प्पा गांव में बड़ी मात्रा में पाई गई हैं।", False, "असत्य। ये मुख्य रूप से मोहनजोदड़ो और हड़प्पा जैसे बड़े महानगरीय स्थलों तक सीमित हैं।"),
    ("मिट्टी की बनी चूड़ियों पर भी सिंधु लिपि के चिन्ह अंकित मिले हैं।", True, "सत्य। कुछ चूड़ियों पर छोटे अक्षरों की छाप या खरोंच के निशान मिले हैं।"),
    ("धोलावीरा सूचना-पट्ट का लकड़ी का आधार समय के साथ सड़ गया, जिससे जिप्सम के अक्षर मिट्टी में गिर गए।", True, "सत्य। लकड़ी सड़ गई थी लेकिन जिप्सम के अक्षर उसी क्रम में मिट्टी में दबे मिले।"),
    ("बर्तनों पर लेखन विशेष रूप से भट्टी में पकाने से पहले ही किया जाता था।", False, "असत्य। अधिकांश लेखन 'पोस्ट-फायरिंग' (पकाने के बाद) भित्तिचित्रों के रूप में मालिकों द्वारा खुरच कर किया जाता था।")
]:
    s2_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The public signboard containing ten large characters was discovered at ___________.", "Dholavira", "Dholavira yielded the famous public signboard."),
    ("The crystalline material used to shape the signboard characters was ___________.", "gypsum", "The letters were made of gypsum paste."),
    ("Most Indus valley seals were made from a soft stone called ___________.", "steatite", "Steatite (or soapstone) was the primary material for seals."),
    ("The Dholavira Signboard consists of exactly ___________ large symbols.", "10", "The signboard contains 10 letters."),
    ("Engraved copper plates carrying signs and animals likely served as ___________ or amulets.", "tokens", "Copper tablets likely acted as identity tokens or amulets."),
    ("Markings scratched onto pottery after it has been baked are known as ___________.", "graffiti", "Post-firing scratchings on pottery are called graffiti."),
    ("Tiny inscriptions have also been discovered on ___________ rods used for gaming or scaling.", "ivory", "Ivory rods carry miniature script signs."),
    ("The clay impressions left by pressing seals into wet clay are called ___________.", "sealings", "Sealings are the clay impressions of seals.")
]:
    s2_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("दस बड़े अक्षरों वाला सार्वजनिक सूचना-पट्ट ___________ नामक स्थल पर खोजा गया था।", "धोलावीरा", "धोलावीरा में दस बड़े अक्षरों वाला प्रसिद्ध बोर्ड मिला है।"),
    ("सूचना-पट्ट के अक्षरों को आकार देने के लिए प्रयुक्त होने वाला क्रिस्टलीय पदार्थ ___________ था।", "जिप्सम", "ये अक्षर सफेद जिप्सम (gypsum) से बने थे।"),
    ("सिंधु घाटी की अधिकांश मुहरें ___________ नामक नरम पत्थर से बनाई गई थीं।", "सेलखड़ी", "सेलखड़ी (steatite) मुहरों के निर्माण का मुख्य पत्थर था।"),
    ("धोलावीरा सूचना-पट्ट में ठीक ___________ बड़े चिन्ह शामिल हैं।", "10", "सूचना-पट्ट में कुल 10 अक्षर मिले हैं।"),
    ("चिन्ह और पशु आकृतियों वाले तांबे के फलक शायद व्यापारिक ___________ या ताबीज के रूप में कार्य करते थे।", "टोकन", "तांबे की पट्टियों का उपयोग टोकन या ताबीज के रूप में किया जाता था।"),
    ("बर्तनों को पकाने के बाद उन पर खुरच कर बनाए गए निशानों को ___________ कहा जाता है।", "भित्तिचित्र", "पकाने के बाद बने इन स्क्रैच मार्क्स को भित्तिचित्र (graffiti) कहते हैं।"),
    ("खेलने या मापने के काम आने वाली हाथीदांत की ___________ पर भी छोटे अभिलेख मिले हैं।", "छड़ों", "हाथीदांत की छड़ों (ivory rods) पर छोटे अक्षर अंकित हैं।"),
    ("गीली मिट्टी पर मुहर दबाकर छोड़ी गई छाप को ___________ कहा जाता है।", "मुहरबंदी", "मिट्टी पर छोड़ी गई छाप को मुहरबंदी (sealings) कहा जाता है।")
]:
    s2_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s2_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the inscribed objects with their primary materials:",
        "items": [{"left": "I. Civic Signboard", "key": "A"}, {"left": "II. Trade Seals", "key": "B"}, {"left": "III. Gaming/Scale rods", "key": "C"}],
        "options": [{"val": "A", "text": "A. Gypsum paste inlays"}, {"val": "B", "text": "B. Steatite (soapstone)"}, {"val": "C", "text": "C. Ivory (elephant tusk)"}],
        "sol": "Signboard is gypsum, seals are steatite, and gaming rods are ivory."
    },
    {
        "type": "Match the Following",
        "q": "Match the sites with their distinct epigraphic discoveries:",
        "items": [{"left": "I. Dholavira", "key": "A"}, {"left": "II. Mohenjo-daro", "key": "B"}, {"left": "III. Lothal", "key": "C"}],
        "options": [{"val": "A", "text": "A. Ten-character gateway signboard"}, {"val": "B", "text": "B. Abundant copper tablets and seals"}, {"val": "C", "text": "C. Clay sealings on warehouse packages"}],
        "sol": "Dholavira has the signboard, Mohenjo-daro has copper tablets, and Lothal has warehouse sealings."
    },
    {
        "type": "Match the Following",
        "q": "Match the archaeological object with its trade/civic function:",
        "items": [{"left": "I. Steatite Seal", "key": "A"}, {"left": "II. Public Signboard", "key": "B"}, {"left": "III. Clay Sealing", "key": "C"}],
        "options": [{"val": "A", "text": "A. Tool used to imprint merchant identity"}, {"val": "B", "text": "B. Medium to declare authority at city gates"}, {"val": "C", "text": "C. Imprinted clay verifying cargo security"}],
        "sol": "Seal is the imprinting tool, signboard declares gate authority, and sealing verifies cargo security."
    }
])

s2_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "उत्कीर्ण वस्तुओं को उनकी प्राथमिक सामग्रियों से सुमेलित करें:",
        "items": [{"left": "I. नागरिक सूचना-पट्ट", "key": "A"}, {"left": "II. व्यापारिक मुहरें", "key": "B"}, {"left": "III. खेल/मापक छड़ें", "key": "C"}],
        "options": [{"val": "A", "text": "A. सफेद जिप्सम का क्रिस्टलीय लेप"}, {"val": "B", "text": "B. सेलखड़ी (steatite)"}, {"val": "C", "text": "C. हाथीदांत (ivory)"}],
        "sol": "सूचना-पट्ट जिप्सम से, मुहरें सेलखड़ी से, और छड़ें हाथीदांत से बनी थीं।"
    },
    {
        "type": "Match the Following",
        "q": "स्थलों को उनकी विशिष्ट पुरालेख खोजों से सुमेलित करें:",
        "items": [{"left": "I. धोलावीरा", "key": "A"}, {"left": "II. मोहनजोदड़ो", "key": "B"}, {"left": "III. लोथल", "key": "C"}],
        "options": [{"val": "A", "text": "A. प्रवेश द्वार पर दस अक्षरों वाला बोर्ड"}, {"val": "B", "text": "B. प्रचुर मात्रा में तांबे की पट्टियां और मुहरें"}, {"val": "C", "text": "C. गोदाम के पैकेजों पर मिट्टी की मुहरबंदियां (sealings)"}],
        "sol": "धोलावीरा में बोर्ड मिला, मोहनजोदड़ो में तांबे की पट्टियां, और लोथल में पैकेजों पर छाप मिली।"
    },
    {
        "type": "Match the Following",
        "q": "पुरातात्विक वस्तु को उसके व्यापारिक/नागरिक कार्य से सुमेलित करें:",
        "items": [{"left": "I. सेलखड़ी मुहर", "key": "A"}, {"left": "II. सार्वजनिक बोर्ड", "key": "B"}, {"left": "III. मिट्टी की मुहरबंदी", "key": "C"}],
        "options": [{"val": "A", "text": "A. व्यापारी की पहचान छापने का उपकरण"}, {"val": "B", "text": "B. शहर के प्रवेश द्वार पर सत्ता प्रदर्शन का साधन"}, {"val": "C", "text": "C. पैकेटों की सुरक्षा प्रमाणित करने वाली मिट्टी की छाप"}],
        "sol": "मुहर छापने का साधन है, बोर्ड सत्ता प्रदर्शन का साधन है, और मुहरबंदी सुरक्षा प्रमाणित करने वाली छाप है।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Where was the unique ten-sign public inscription found?", "Dholavira, Gujarat."),
    ("What is the approximate height of each gypsum letter on the Dholavira Signboard?", "37 cm."),
    ("What mineral was soft enough to carve seals easily and hardened when heated?", "Steatite."),
    ("What was engraved on the reverse side of most Indus copper tablets?", "An animal figure (such as a unicorn or bull)."),
    ("What civic message is the Dholavira Signboard believed to have conveyed?", "It represents a display of civic authority or city name at the Citadel entrance."),
    ("Where on the Citadel gates was the Dholavira Signboard originally hung?", "Over the northern gateway."),
    ("What is the term for markings scratched on pottery after baking?", "Post-firing graffiti."),
    ("Name a luxury material of animal origin that carries tiny script signs.", "Ivory (used for rods or combs).")
]:
    s2_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("दस अक्षरों वाला अनूठा सार्वजनिक अभिलेख कहाँ मिला था?", "गुजरात के धोलावीरा में।"),
    ("धोलावीरा सूचना-पट्ट के जिप्सम अक्षरों की अनुमानित ऊंचाई क्या है?", "37 सेंटीमीटर।"),
    ("कौन सा खनिज मुहरों को आसानी से तराशने के लिए नरम था और गर्म करने पर कठोर हो जाता था?", "सेलखड़ी (steatite)।"),
    ("सिंधु तांबे की अधिकांश पट्टियों के पीछे की तरफ क्या अंकित था?", "एक पशु आकृति (जैसे एक सींग वाला बैल या सांड)।"),
    ("धोलावीरा सूचना-पट्ट से क्या नागरिक संदेश प्रसारित होने का अनुमान है?", "यह किले के प्रवेश द्वार पर नागरिक सत्ता या शहर के नाम का सार्वजनिक प्रदर्शन माना जाता है।"),
    ("धोलावीरा का सूचना-पट्ट मूल रूप से किले के किस द्वार पर लटकाया गया था?", "उत्तरी प्रवेश द्वार (northern gateway) के ऊपर।"),
    ("पकाने के बाद बर्तनों पर खुरचे गए निशानों को क्या नाम दिया जाता है?", "पोस्ट-फायरिंग भित्तिचित्र (graffiti)।"),
    ("पशु मूल की एक विलासिता सामग्री का नाम बताएं जिस पर छोटे अक्षर लिखे मिले हैं?", "हाथीदांत (ivory - छड़ों या कंघियों पर)।")
]:
    s2_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Dholavira Signboard is classified as a public advertisement or notice.\nReason (R): It was prominently mounted above the northern gateway of the Citadel for all visitors to view.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Steatite was the most common raw material used to manufacture Indus seals.\nReason (R): Steatite is a soft talcose rock that was easy to carve and hardened significantly after firing.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Copper tablets served as the uniform currency of the Indus economy.\nReason (R): Copper tablets are found carrying standard weight specifications and identical animal drawings.", 3, "A is false because there was no metallic coinage in the IVC. R is true regarding the drawings, but they were not currency."),
    ("Assertion (A): The wood of the Dholavira Signboard survived completely intact down to modern times.\nReason (R): The dry saline environment of Dholavira protected organic wood from decay.", 3, "A is false because the wood decayed completely; only the gypsum letters survived in the soil. R is false."),
    ("Assertion (A): Pottery graffiti represents writing by ordinary citizens.\nReason (R): Graffiti was scratched post-firing on everyday domestic pots rather than administrative seals.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Only a single signboard inscription has been discovered in the entire Harappan civilisation.\nReason (R): Public signboards were probably common, but being made of wood, most decayed in the soil.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Dholavira Signboard contains a total of 10 symbols.\nReason (R): The script of the signboard represents a deciphered royal decree of a king named Dholavira.", 2, "A is true but R is false (the script remains undeciphered, and Dholavira is a modern village name, not a king)."),
    ("Assertion (A): Seals were used by merchants to authenticate goods.\nReason (R): Clay tags on packaged goods at Lothal show impressions made by Indus seals.", 0, "Both A and R are true and R is the correct explanation of A.")
]:
    s2_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): धोलावीरा सूचना-पट्ट को एक सार्वजनिक विज्ञापन या सूचना के रूप में वर्गीकृत किया गया है।\nकारण (R): इसे किले के उत्तरी प्रवेश द्वार के ऊपर प्रमुखता से लगाया गया था ताकि सभी आगंतुक इसे देख सकें।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सेलखड़ी (steatite) सिंधु मुहरों के निर्माण के लिए प्रयुक्त सबसे आम कच्चा माल था।\nकारण (R): सेलखड़ी एक नरम पत्थर है जिसे तराशना आसान था और पकाने के बाद यह अत्यंत कठोर हो जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): तांबे की पट्टियों ने सिंधु अर्थव्यवस्था की मानक मुद्रा के रूप में कार्य किया।\nकारण (R): तांबे की पट्टियों पर मानक पशु चित्र और लिपि चिन्ह उत्कीर्ण मिले हैं।", 3, "A असत्य है क्योंकि हड़प्पा सभ्यता में धातु के सिक्के नहीं चलते थे। R सत्य है।"),
    ("कथन (A): धोलावीरा सूचना-पट्ट की लकड़ी आधुनिक काल तक पूरी तरह से सुरक्षित बची रही।\nकारण (R): धोलावीरा के शुष्क खारे वातावरण ने जैविक लकड़ी को सड़ने से बचा लिया।", 3, "A असत्य है क्योंकि लकड़ी पूरी तरह सड़ चुकी थी, केवल जिप्सम के इनले अक्षर बचे रहे। R असत्य है।"),
    ("कथन (A): बर्तनों पर बने भित्तिचित्र (graffiti) आम नागरिकों के लेखन का प्रतिनिधित्व करते हैं।\nकारण (R): भित्तिचित्रों को प्रशासनिक मुहरों के बजाय दैनिक उपयोग के घरेलू बर्तनों पर पकाने के बाद खुरचा जाता था।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): पूरी हड़प्पा सभ्यता में केवल एक ही सूचना-पट्ट अभिलेख खोजा जा सका है।\nकारण (R): सार्वजनिक बोर्ड शायद आम रहे होंगे, लेकिन लकड़ी के बने होने के कारण अधिकांश मिट्टी में सड़ गए।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): धोलावीरा सूचना-पट्ट में कुल 10 प्रतीक मिले हैं।\nकारण (R): सूचना-पट्ट पर लिखा पाठ 'धोलावीरा' नामक राजा के पढ़े गए आदेश का प्रतिनिधित्व करता है।", 2, "A सत्य है लेकिन R असत्य है (लेख अपठित है, और धोलावीरा राजा का नाम नहीं बल्कि आधुनिक स्थल का नाम है)।"),
    ("कथन (A): व्यापारियों द्वारा माल को प्रमाणित करने के लिए मुहरों का उपयोग किया जाता था।\nकारण (R): लोथल में पैक किए गए माल पर मिली मिट्टी की छापों में सिंधु मुहरों के निशान मिले हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।")
]:
    s2_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Dholavira Signboard:\n1. It consists of ten signs made of white gypsum paste.\n2. It was found placed over the northern gateway of the Citadel.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the material, count, and gate location of the signboard."),
    ("Consider the following statements regarding seal materials:\n1. Steatite was preferred for seals because it could be easily carved and hardened by heat.\n2. Copper tablets are found primarily in rural agricultural sites like Allahdino.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: copper tablets are concentrated in urban Mohenjo-daro/Harappa, not rural Allahdino."),
    ("Consider the following statements regarding writing on pottery:\n1. Writing was only scratched on pots before firing in the kiln.\n2. Post-firing graffiti shows that writing was accessible to ordinary residents.\nWhich of the statements given above is/are correct?", 1, "Statement 2 is correct. Statement 1 is incorrect: post-firing graffiti was very common."),
    ("Consider the following statements regarding the gypsum signs:\n1. Each character is about 37 cm high.\n2. The board wood rotted away, but the gypsum paste remained in the soil.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing the size and preservation of the gypsum letters."),
    ("Consider the following statements regarding ivory rods:\n1. Inscribed ivory rods have been found at Mohenjo-daro.\n2. They are believed to be gaming dice or scales.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the location and usage of the ivory rods.")
]:
    s2_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("धोलावीरा सूचना-पट्ट के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसमें सफेद जिप्सम लेप से बने दस चिन्ह शामिल हैं।\n2. यह किले के उत्तरी प्रवेश द्वार के ऊपर रखा हुआ पाया गया था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो बोर्ड की सामग्री, अक्षरों की संख्या और स्थान का विवरण देते हैं।"),
    ("मुहरों की सामग्री के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुहरों के लिए सेलखड़ी को पसंद किया जाता था क्योंकि इसे आसानी से तराश कर गर्म करके कठोर किया जा सकता था।\n2. तांबे की पट्टियां मुख्य रूप से अल्लाहदीनो जैसे ग्रामीण कृषि स्थलों में पाई जाती हैं।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि तांबे की पट्टियाँ मोहनजोदड़ो जैसे शहरी केंद्रों में केंद्रित थीं।"),
    ("बर्तनों पर लेखन के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. बर्तनों पर केवल भट्टी में पकाने से पहले ही अक्षर खुरचे जाते थे।\n2. पकाने के बाद बने भित्तिचित्र दर्शाते हैं कि लेखन आम लोगों के लिए भी सुलभ था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 1, "कथन 2 सही है। कथन 1 गलत है क्योंकि पकाने के बाद खुरच कर लिखना (post-firing graffiti) बहुत आम था।"),
    ("जिप्सम अक्षरों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. प्रत्येक अक्षर की ऊंचाई लगभग 37 सेमी है।\n2. बोर्ड की लकड़ी सड़ गई थी, लेकिन जिप्सम का लेप मिट्टी में उसी रूप में जमा रहा।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो अक्षरों के आकार और उनके संरक्षण की पुष्टि करते हैं।"),
    ("हाथीदांत की छड़ों के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. उत्कीर्ण हाथीदांत की छड़ें मोहनजोदड़ो से प्राप्त हुई हैं।\n2. माना जाता है कि ये छड़ें पासे (dice) या मापक पैमाने थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो हाथीदांत की छड़ों के प्राप्ति स्थल और उनके संभावित उपयोग को स्पष्ट करते हैं।")
]:
    s2_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why did the gypsum letters of the Dholavira Signboard survive while the wood frame decayed?", "Because gypsum is an inorganic mineral paste that does not rot, whereas the wooden board was organic and decomposed in the soil over thousands of years."),
    ("Why were characters carved in reverse (mirror-image) on steatite seals?", "So that when the seal was pressed into wet clay tags, the resulting sealing impression would show the characters in their correct readable orientation."),
    ("Why was the Dholavira Signboard mounted publicly at the Citadel gate?", "To declare civic authority, rules, or the town's name to all incoming merchants and visitors, functioning as a monumental civic notice.")
]:
    s2_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("धोलावीरा सूचना-पट्ट की लकड़ी सड़ जाने के बाद भी जिप्सम के अक्षर क्यों बच गए?", "क्योंकि जिप्सम एक अकार्बनिक खनिज लेप है जो सड़ता नहीं है, जबकि लकड़ी कार्बनिक होने के कारण हजारों वर्षों में मिट्टी में अपघटित हो गई।"),
    ("सेलखड़ी की मुहरों पर अक्षरों को विपरीत (दर्पण-छवि) रूप में क्यों खोदा जाता था?", "ताकि जब मुहर को गीली मिट्टी पर दबाया जाए, तो प्राप्त छाप में अक्षर सीधे और पठनीय रूप में दिखाई दें।"),
    ("धोलावीरा सूचना-पट्ट को किले के द्वार पर सार्वजनिक रूप से क्यों लगाया गया था?", "आने वाले व्यापारियों और आगंतुकों के सामने केंद्रीय प्रशासनिक अधिकार, नियम या शहर का नाम प्रदर्शित करने के लिए, जो एक सार्वजनिक सूचना का कार्य करता था।")
]:
    s2_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How did archaeologists recover and identify the Dholavira Signboard letters in the soil?", "By meticulously excavating the soil near the Citadel gate, identifying the aligned crystalline white gypsum shapes that sat in the soil where the wooden board had rotted away."),
    ("How were steatite seals utilized to secure merchant packaging during transport?", "A knot was tied on the cargo package, soft clay was placed over the knot, and the steatite seal was stamped onto the clay to create an authentic security seal."),
    ("How did post-firing graffiti on domestic pots differ from pre-firing stamps?", "Pre-firing stamps were pressed into wet clay before baking at a workshop, while post-firing graffiti was scratched by individual owners on finished baked pots to show possession.")
]:
    s2_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("पुरातत्वविदों ने मिट्टी में दबे धोलावीरा सूचना-पट्ट के अक्षरों को कैसे खोजा और पहचाना?", "किले के द्वार के पास सावधानीपूर्वक मिट्टी खोदकर, जहाँ लकड़ी सड़ने के बाद मिट्टी में दबे क्रिस्टलीय सफेद जिप्सम के अक्षरों के संरेखण को पहचाना गया।"),
    ("परिवहन के दौरान व्यापारियों के पैकेजों को सुरक्षित करने के लिए मुहरों का उपयोग कैसे किया जाता था?", "सामान की गठरी पर गांठ बांधी जाती थी, गांठ के ऊपर गीली मिट्टी रखी जाती थी, और मुहर को मिट्टी पर दबाकर एक प्रामाणिक सुरक्षा छाप बनाई जाती थी।"),
    ("घरेलू बर्तनों पर पकाने के बाद के भित्तिचित्र (post-firing graffiti) पहले की मुहरों से कैसे भिन्न थे?", "पकाने से पहले की मुहरें कार्यशाला में गीली मिट्टी पर लगाई जाती थीं, जबकि पकाने के बाद के भित्तिचित्र मालिकों द्वारा तैयार बर्तन पर मालिकाना हक जताने के लिए खुरच कर बनाए जाते थे।")
]:
    s2_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: Excavations at Lothal yielded a warehouse with dozens of clay tags showing seal impressions of unicorns and Indus script. None of the original wooden boxes survived. What trade practice does this study prove?", "It proves that seals were used to secure packaging and authenticate cargo during maritime transit, and that clay sealings survived even when the organic cargo boxes rotted."),
    ("Case Study: The placement of the Dholavira Signboard at the northern gateway of the Citadel. If this signboard was meant for public view, what does this tell us about the literacy level or administrative nature of Dholavira?", "It indicates that either a portion of the population was literate or that visual symbols carried standardized public meanings, reflecting a highly organized municipal administration."),
    ("Case Study: A cache of copper tablets is discovered in a single house in Mohenjo-daro, with identical animal designs and text sequences. Why does this suggest they were tokens rather than unique seals?", "Because multiple copies of the exact same script and animal design were held together, showing they were mass-produced tokens, amulets, or standard trading passes rather than individual seals.")
]:
    s2_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: लोथल में उत्खनन से एक गोदाम मिला है जिसमें एक सींग वाले बैल (unicorn) और सिंधु लिपि की छाप वाले दर्जनों मिट्टी के टैग मिले हैं। मूल लकड़ी के बक्से नष्ट हो चुके हैं। यह अध्ययन किस व्यापारिक पद्धति को प्रमाणित करता है?", "यह प्रमाणित करता है कि समुद्री परिवहन के दौरान माल सुरक्षित करने और प्रमाणित करने के लिए मुहरों का उपयोग किया जाता था, और कार्बनिक बक्से नष्ट होने पर भी मिट्टी की छापें बची रहीं।"),
    ("केस स्टडी: किले के उत्तरी द्वार पर धोलावीरा सूचना-पट्ट का स्थान। यदि यह बोर्ड जनता के देखने के लिए था, तो यह धोलावीरा की साक्षरता दर या प्रशासनिक स्वरूप के बारे में क्या दर्शाता है?", "यह दर्शाता है कि या तो आबादी का एक हिस्सा साक्षर था या इन प्रतीकों का जनता के लिए मानक अर्थ था, जो एक सुव्यवस्थित नगर प्रशासन को दर्शाता है।"),
    ("केस स्टडी: मोहनजोदड़ो में एक ही घर से तांबे की कई पट्टियों का संग्रह मिला है, जिन पर एक समान पशु चित्र और पाठ अनुक्रम हैं। यह क्यों संकेत देता है कि वे व्यक्तिगत मुहरों के बजाय टोकन थे?", "क्योंकि एक ही लेख और पशु डिजाइन की कई प्रतियां एक साथ मिली हैं, जो दर्शाती हैं कि वे सामूहिक रूप से उत्पादित टोकन, ताबीज या मानक व्यापारिक पास थे, व्यक्तिगत मुहर नहीं।")
]:
    s2_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the difference between a 'seal' and a 'sealing' to a student.", "A seal is the actual engraved stamp tool made of steatite or copper. A sealing is the clay impression left behind when the seal is pressed into soft wet clay on cargo packages to secure them."),
    ("Explain the significance of the Dholavira Signboard in the history of Indian writing.", "The Dholavira Signboard is the earliest known large-scale public civic inscription in India. It shows that writing was not just used for small private trade labels, but had public, monumental, and civic administrative applications."),
    ("Explain why pottery graffiti is highly valuable for understanding Harappan society.", "While seals are found in wealthy trading contexts, pottery graffiti is found on ordinary domestic pots in lower-class houses. This shows that basic knowledge or use of script symbols was widespread among common citizens, not just confined to elite merchants.")
]:
    s2_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को 'मुहर' (seal) और 'मुहरबंदी' (sealing) के बीच का अंतर समझाएं।", "मुहर वह उत्कीर्ण धातु या सेलखड़ी का उपकरण है जिसका उपयोग ठप्पा लगाने के लिए किया जाता था। मुहरबंदी वह गीली मिट्टी पर छोड़ी गई छाप है जो व्यापारिक गठरियों को सुरक्षित करने के लिए मुहर दबाने से बनती थी।"),
    ("भारतीय लेखन के इतिहास में धोलावीरा सूचना-पट्ट के महत्व को समझाएं।", "धोलावीरा सूचना-पट्ट भारत में बड़े पैमाने पर सार्वजनिक नागरिक अभिलेख का सबसे पुराना उदाहरण है। यह दर्शाता है कि लेखन केवल छोटे व्यापारिक लेबलों तक सीमित नहीं था, बल्कि इसका सार्वजनिक और प्रशासनिक उपयोग भी था।"),
    ("समझाएं कि हड़प्पा समाज को समझने के लिए बर्तनों के भित्तिचित्र (pottery graffiti) क्यों मूल्यवान हैं।", "मुहरें धनी व्यापारिक संदर्भों में मिलती हैं, जबकि बर्तनों के भित्तिचित्र निचले वर्ग के घरों में साधारण बर्तनों पर मिलते हैं। यह दर्शाता है कि लिपि प्रतीकों का बुनियादी ज्ञान या उपयोग केवल धनी व्यापारियों तक सीमित नहीं था, बल्कि आम नागरिकों में भी फैला था।")
]:
    s2_mastery_hin.append({"type": "Teach Concept", "q": q, "sol": sol})

print(f"Section 2 Mastery questions populated: {len(s2_mastery_eng)} (Eng), {len(s2_mastery_hin)} (Hin)")

# =========================================================================
# SECTION 3: LINGUISTIC AFFILIATION THEORIES
# =========================================================================
s3_mastery_eng = []
s3_mastery_hin = []

# MCQ (5)
for q, opts, ans, sol in [
    ("Which Indian scholar is famous for compiling the first comprehensive computer concordance of the Indus script in 1977?", ["S.R. Rao", "Iravatham Mahadevan", "Romila Thapar", "D.D. Kosambi"], 1, "Iravatham Mahadevan compiled the first comprehensive computer concordance of the script in 1977."),
    ("The leading Finnish scholar who has championed the Proto-Dravidian hypothesis of the Harappan language is:", ["Mortimer Wheeler", "Asko Parpola", "John Marshall", "Michael Witzel"], 1, "Asko Parpola is the foremost Finnish linguist supporting the Proto-Dravidian theory."),
    ("Which scholar proposed that the Harappan script was an alphabetical precursor to Sanskrit?", ["S.R. Rao", "Iravatham Mahadevan", "Asko Parpola", "Steve Farmer"], 0, "S.R. Rao argued that the script was alphabetic and represented an early form of Indo-Aryan Sanskrit."),
    ("The Dravidian model reads the 'fish' sign as *min*, which homophonically represents both 'fish' and:", ["Star", "Water", "King", "Barley"], 0, "In Dravidian languages, *min* means both fish and star, which is used to interpret astral signs on seals."),
    ("Who proposed the controversial revisionist theory that the Harappan script was a non-linguistic symbol system?", ["Mahadevan and Parpola", "Farmer, Sproat, and Witzel", "S.R. Rao and B.B. Lal", "John Marshall and Mackay"], 1, "Steve Farmer, Richard Sproat, and Michael Witzel proposed that the script did not encode a spoken language.")
]:
    s3_mastery_eng.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("1977 में सिंधु लिपि का पहला व्यापक कंप्यूटर संकलन (concordance) तैयार करने के लिए कौन से भारतीय विद्वान प्रसिद्ध हैं?", ["एस.आर. राव", "इरावथम महादेवन", "रोमिला थापर", "डी.डी. कोसांबी"], 1, "इरावथम महादेवन ने 1977 में सिंधु लिपि का पहला व्यापक कंप्यूटर संकलन प्रकाशित किया था।"),
    ("हड़प्पा भाषा के आदि-द्रविड़ (Proto-Dravidian) सिद्धांत का समर्थन करने वाले प्रमुख फिनिश विद्वान कौन हैं?", ["मोर्टिमर व्हीलर", "आस्को पारपोला", "जॉन मार्शल", "माइकल विटजेल"], 1, "आस्को पारपोला आदि-द्रविड़ भाषा सिद्धांत के सबसे प्रमुख फिनिश समर्थक हैं।"),
    ("किस विद्वान ने प्रस्ताव दिया था कि हड़प्पा लिपि संस्कृत का एक वर्णमालात्मक पूर्ववर्ती रूप थी?", ["एस.आर. राव", "इरावथम महादेवन", "आस्को पारपोला", "स्टीव फार्मर"], 0, "एस.आर. राव ने दावा किया कि यह लिपि वर्णमाला के समान थी और प्रारंभिक संस्कृत का प्रतिनिधित्व करती थी।"),
    ("द्रविड़ मॉडल में 'मछली' के चिन्ह को *मीन* पढ़ा जाता है, जो समध्वनि (homophone) के रूप में मछली और किसको दर्शाता है?", ["तारा (Star)", "पानी (Water)", "राजा (King)", "जौ (Barley)"], 0, "द्रविड़ भाषाओं में *मीन* का अर्थ मछली और तारा दोनों होता है, जिसका उपयोग मुहरों पर खगोलीय अर्थ निकालने के लिए किया जाता है।"),
    ("यह विवादास्पद वैकल्पिक सिद्धांत किसने दिया कि हड़प्पा लिपि एक गैर-भाषाई प्रतीक प्रणाली थी?", ["महादेवन और पारपोला", "फार्मर, स्प्रोट और विटजेल", "एस.आर. राव और बी.बी. लाल", "जॉन मार्शल और मैके"], 1, "स्टीव फार्मर, रिचर्ड स्प्रोट और माइकल विटजेल ने तर्क दिया कि यह लिपि किसी बोली जाने वाली भाषा को कोड नहीं करती थी।")
]:
    s3_mastery_hin.append({"type": "MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# Multi-Correct MCQ (5)
for q, opts, ans, sol in [
    ("Which of the following scholars advocate for the Dravidian linguistic model of the Indus script? (Select all that apply)", ["Asko Parpola", "Iravatham Mahadevan", "Walter Fairservis", "S.R. Rao"], [0, 1, 2], "Parpola, Mahadevan, and Fairservis support the Dravidian theory. S.R. Rao supports the Indo-Aryan theory."),
    ("Select the core arguments of the non-linguistic symbol hypothesis: (Select all that apply)", ["Average text length is extremely short (4-5 signs)", "Lacks the statistical sign repetitions expected in natural languages", "Symbols acted as heraldic clan markers or ritual signs", "The script has been proven to represent the Sumerian language"], [0, 1, 2], "Farmer, Sproat, and Witzel argue that brief texts, low repetition, and heraldic roles point to a non-linguistic system."),
    ("What are the major language families linked by various theories to the Harappan civilisation? (Select all that apply)", ["Dravidian", "Indo-Aryan (Indo-European)", "Munda (Austroasiatic)", "Sino-Tibetan"], [0, 1, 2], "Dravidian, Indo-Aryan, and Munda are the main proposed language families."),
    ("Why is S.R. Rao's Indo-Aryan/Sanskrit decipherment widely rejected? (Select all that apply)", ["He assigned arbitrary phonetic values to signs to force Sanskrit readings", "Mainstream linguists argue the script is logo-syllabic, not alphabetical", "The grammar of Vedic Sanskrit does not match his translations", "Sanskrit was proven to have originated in South America"], [0, 1, 2], "Rao's theory is rejected due to arbitrary values, alphabetical assumptions, and grammatical mismatch. Sanskrit did not originate in South America."),
    ("Which factors support the Dravidian hypothesis of the Harappan language? (Select all that apply)", ["The survival of Brahui, a Dravidian language, in Baluchistan", "Dravidian substratum elements found in early Rigvedic Sanskrit", "The successful reading of the fish sign using Dravidian homophones", "The discovery of Tamil inscriptions in Harappan ruins"], [0, 1, 2], "Brahui in Baluchistan, Dravidian influences in Rigveda, and Rebus readings support the Dravidian theory. No Tamil inscriptions have been found in Harappa.")
]:
    s3_mastery_eng.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

for q, opts, ans, sol in [
    ("निम्नलिखित में से कौन से विद्वान सिंधु लिपि के द्रविड़ भाषाई मॉडल का समर्थन करते हैं? (सभी लागू विकल्प चुनें)", ["आस्को पारपोला", "इरावथम महादेवन", "वाल्टर फेयरसर्विस", "एस.आर. राव"], [0, 1, 2], "पारपोला, महादेवन और फेयरसर्विस द्रविड़ सिद्धांत के समर्थक हैं। एस.आर. राव आर्य सिद्धांत के समर्थक हैं।"),
    ("गैर-भाषाई प्रतीक सिद्धांत के मुख्य तर्कों का चयन करें: (सभी लागू विकल्प चुनें)", ["अभिलेखों की औसत लंबाई अत्यधिक संक्षिप्त (4-5 चिन्ह) है", "इसमें प्राकृतिक भाषाओं में अपेक्षित अक्षरों के दोहराव का अभाव है", "ये प्रतीक राजकीय कुल चिन्हों या धार्मिक संकेतों का कार्य करते थे", "यह सिद्ध हो चुका है कि यह लिपि सुमेरियन भाषा का प्रतिनिधित्व करती थी"], [0, 1, 2], "फार्मर, स्प्रोट और विटजेल के अनुसार छोटे लेख, कम दोहराव और कुल चिन्हों जैसी विशेषताएं गैर-भाषाई तंत्र का प्रमाण हैं।"),
    ("विभिन्न सिद्धांतों द्वारा हड़प्पा सभ्यता से जुड़े मुख्य भाषा परिवार कौन से हैं? (सभी लागू विकल्प चुनें)", ["द्रविड़ भाषा परिवार", "भारत-आर्य (भारोपीय) परिवार", "मुंडा (ऑस्ट्रो-एशियाई) परिवार", "चीनी-तिब्बती परिवार"], [0, 1, 2], "द्रविड़, भारत-आर्य और मुंडा ही मुख्य प्रस्तावित भाषा परिवार हैं।"),
    ("एस.आर. राव के भारत-आर्य/संस्कृत अनुवाद को व्यापक रूप से क्यों खारिज कर दिया गया है? (सभी लागू विकल्प चुनें)", ["उन्होंने संस्कृत अर्थ निकालने के लिए मनमाने ध्वन्यात्मक मान दिए", "मुख्यधारा के भाषाविद् मानते हैं कि लिपि लोगो-सिलेबिक है, वर्णमाला नहीं", "वैदिक संस्कृत का व्याकरण उनके अनुवादों से मेल नहीं खाता", "यह सिद्ध हो चुका है कि संस्कृत की उत्पत्ति दक्षिण अमेरिका में हुई थी"], [0, 1, 2], "मनमाने ध्वन्यात्मक मान, वर्णमाला की गलत अवधारणा और व्याकरण का मेल न खाना राव के सिद्धांत के खारिज होने के मुख्य कारण हैं।"),
    ("हड़प्पा भाषा के द्रविड़ सिद्धांत को कौन से कारक समर्थन प्रदान करते हैं? (सभी लागू विकल्प चुनें)", ["बलूचिस्तान में द्रविड़ भाषा 'ब्राहुई' (Brahui) का जीवित बचे रहना", "प्रारंभिक ऋग्वैदिक संस्कृत में पाए जाने वाले द्रविड़ भाषा के प्रभाव", "द्रविड़ समध्वनि (Rebus) विधि से मछली के चिन्ह को सफलतापूर्वक पढ़ा जाना", "हड़प्पा के खंडहरों में तमिल भाषा के शिलालेखों का मिलना"], [0, 1, 2], "बलूचिस्तान की ब्राहुई भाषा, ऋग्वेद में द्रविड़ प्रभाव और रीबस पद्धति इसके समर्थक कारक हैं। तमिल शिलालेख वहां नहीं मिले हैं।")
]:
    s3_mastery_hin.append({"type": "Multiple Correct MCQ", "q": q, "opts": opts, "ans": ans, "sol": sol})

# True/False (8)
for q, ans, sol in [
    ("Iravatham Mahadevan was a supporter of the Indo-Aryan hypothesis of the Harappan language.", False, "Mahadevan was a leading proponent of the Proto-Dravidian theory."),
    ("Asko Parpola utilized computers to study the sign distributions and support the Dravidian connection.", True, "True. Parpola did extensive computerized work to support the Dravidian theory."),
    ("The non-linguistic symbol theory states that the Harappan script was not a spoken language.", True, "True. The theory argues it was a system of heraldic and ritual symbols."),
    ("Brahui is a Dravidian language spoken in Baluchistan, near the Indus Valley region.", True, "True. Brahui provides geographical support for the Dravidian theory."),
    ("Munda languages belong to the Indo-European language family.", False, "False. Munda languages belong to the Austroasiatic language family."),
    ("S.R. Rao proposed that late Indus script signs evolved into the Phoenician alphabet.", True, "True. He argued for an evolutionary link from late Indus signs to Phoenician letters."),
    ("Linguists have reached a unanimous consensus that the Indus language was Dravidian.", False, "False. There is no consensus; it remains a matter of intense academic debate."),
    ("Entropy analysis compares the statistical order of script symbols with known languages.", True, "True. Computer entropy studies show Indus sign structures resemble natural languages.")
]:
    s3_mastery_eng.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("इरावथम महादेवन हड़प्पा भाषा के भारत-आर्य (Indo-Aryan) सिद्धांत के समर्थक थे।", False, "महादेवन आदि-द्रविड़ (Proto-Dravidian) सिद्धांत के प्रमुख समर्थक थे।"),
    ("आस्को पारपोला ने अक्षरों के वितरण का अध्ययन करने और द्रविड़ संबंध का समर्थन करने के लिए कंप्यूटर का उपयोग किया था।", True, "सत्य। पारपोला ने कंप्यूटर आधारित अध्ययनों से द्रविड़ सिद्धांत को मजबूत किया।"),
    ("गैर-भाषाई प्रतीक सिद्धांत का मानना है कि सिंधु लिपि कोई बोली जाने वाली भाषा नहीं थी।", True, "सत्य। यह सिद्धांत मानता है कि यह राजकीय कुल चिन्हों और धार्मिक प्रतीकों की प्रणाली थी।"),
    ("ब्राहुई (Brahui) एक द्रविड़ भाषा है जो सिंधु घाटी क्षेत्र के समीप बलूचिस्तान में बोली जाती है।", True, "सत्य। ब्राहुई भाषा का वहां होना द्रविड़ सिद्धांत को भौगोलिक बल देता है।"),
    ("मुंडा भाषाएं भारोपीय (Indo-European) भाषा परिवार से संबंधित हैं।", False, "असत्य। मुंडा भाषाएं ऑस्ट्रो-एशियाई (Austroasiatic) भाषा परिवार का हिस्सा हैं।"),
    ("एस.आर. राव ने प्रस्ताव दिया कि देर के सिंधु लिपि चिन्ह फोनेशियन वर्णमाला में विकसित हुए।", True, "सत्य। उन्होंने देर के हड़प्पा चिन्हों और फोनेशियन अक्षरों में विकासवादी संबंध बताया था।"),
    ("भाषाविदों के बीच आम सहमति बन चुकी है कि सिंधु घाटी की भाषा द्रविड़ भाषा ही थी।", False, "असत्य। कोई सर्वसम्मति नहीं है, यह आज भी एक गंभीर भाषाई विवाद का विषय है।"),
    ("एन्ट्रॉपी विश्लेषण (Entropy analysis) सिंधु लिपि के चिन्हों के सांख्यिकीय क्रम की तुलना ज्ञात भाषाओं से करता है।", True, "सत्य। कंप्यूटर एन्ट्रॉपी अध्ययन दर्शाते हैं कि सिंधु लिपि का क्रम प्राकृतिक भाषाओं जैसा है।")
]:
    s3_mastery_hin.append({"type": "True/False", "q": q, "ans": ans, "sol": sol})

# Fill Blank (8)
for q, ans, sol in [
    ("The scholar who published the computer concordance of the Indus script in 1977 was ___________.", "Iravatham Mahadevan", "Mahadevan compiled the 1977 concordance."),
    ("Asko Parpola is a leading proponent of the ___________ linguistic hypothesis.", "Proto-Dravidian", "Parpola supports the Proto-Dravidian model."),
    ("The Indo-Aryan Sanskrit reading of the script was proposed by ___________ Rao.", "S.R.", "S.R. Rao proposed the Indo-Aryan alphabetical reading."),
    ("The non-linguistic symbol theory was published by Farmer, Sproat, and ___________.", "Witzel", "Steve Farmer, Richard Sproat, and Michael Witzel wrote the paper."),
    ("In Dravidian homophony, the word *min* represents both a fish and a ___________.", "star", "Min stands for both fish and star."),
    ("The Munda languages belong to the ___________ language family.", "Austroasiatic", "Munda is a branch of the Austroasiatic family."),
    ("Conditional ___________ is the mathematical metric used to prove the script has language-like order.", "entropy", "Conditional entropy studies verify language-like ordering."),
    ("A linguistic pocket of Dravidian speakers surviving in Baluchistan is the ___________ language.", "Brahui", "Brahui is the Dravidian pocket in Baluchistan.")
]:
    s3_mastery_eng.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("1977 में सिंधु लिपि का कंप्यूटर संकलन (concordance) प्रकाशित करने वाले विद्वान ___________ थे।", "इरावथम महादेवन", "इरावथम महादेवन ने 1977 में इस संकलन ग्रंथ का संपादन किया था।"),
    ("आस्को पारपोला ___________ भाषाई परिकल्पना के प्रमुख समर्थक हैं।", "आदि-द्रविड़", "पारपोला आदि-द्रविड़ (Proto-Dravidian) सिद्धांत के समर्थक हैं।"),
    ("लिपि के भारत-आर्य संस्कृत पाठ का प्रस्ताव ___________ राव द्वारा दिया गया था।", "एस.आर.", "एस.आर. राव (S.R. Rao) ने संस्कृत आधारित अनुवाद का दावा किया था।"),
    ("गैर-भाषाई प्रतीक सिद्धांत फार्मर, स्प्रोट और ___________ द्वारा प्रकाशित किया गया था।", "विटजेल", "स्टीव फार्मर, रिचर्ड स्प्रोट और माइकल विटजेल (Witzel) ने यह सिद्धांत दिया था।"),
    ("द्रविड़ समध्वनि में शब्द 'मीन' मछली के साथ-साथ ___________ को भी दर्शाता है।", "तारे", "मीन (min) का अर्थ मछली और तारा दोनों होता है।"),
    ("मुंडा भाषाएं मुख्य रूप से ___________ भाषा परिवार से संबंधित हैं।", "ऑस्ट्रो-एशियाई", "मुंडा भाषाएं ऑस्ट्रो-एशियाई (Austroasiatic) परिवार का हिस्सा हैं।"),
    ("गणितीय माप जिसका उपयोग यह साबित करने के लिए किया जाता है कि लिपि में भाषा जैसा क्रम है, वह ___________ है।", "एन्ट्रॉपी", "कंडीशनल एन्ट्रॉपी (entropy) से अक्षरों के तार्किक क्रम का पता चलता है।"),
    ("बलूचिस्तान में आज भी बोली जाने वाली द्रविड़ भाषा का नाम ___________ है।", "ब्राहुई", "ब्राहुई (Brahui) बलूचिस्तान की द्रविड़ भाषा है।")
]:
    s3_mastery_hin.append({"type": "Fill in the Blank", "q": q, "ans": ans, "sol": sol})

# Match the Following (3)
s3_mastery_eng.extend([
    {
        "type": "Match the Following",
        "q": "Match the scholars with their respective script theories:",
        "items": [{"left": "I. Asko Parpola", "key": "A"}, {"left": "II. S.R. Rao", "key": "B"}, {"left": "III. Steve Farmer", "key": "C"}],
        "options": [{"val": "A", "text": "A. Proto-Dravidian language hypothesis"}, {"val": "B", "text": "B. Indo-Aryan Sanskrit hypothesis"}, {"val": "C", "text": "C. Non-linguistic symbol system theory"}],
        "sol": "Parpola supports Dravidian, Rao supports Sanskrit, and Farmer supports the non-linguistic theory."
    },
    {
        "type": "Match the Following",
        "q": "Match the terms with their definitions in script studies:",
        "items": [{"left": "I. Rebus Principle", "key": "A"}, {"left": "II. Concordance", "key": "B"}, {"left": "III. Entropy", "key": "C"}],
        "options": [{"val": "A", "text": "A. Using a pictograph of an object to represent a homophone"}, {"val": "B", "text": "B. Systematic index of symbols across all texts"}, {"val": "C", "text": "C. Statistical predictability of symbol sequences"}],
        "sol": "Rebus uses homophones, concordance is the systematic index, and entropy measures sequence predictability."
    },
    {
        "type": "Match the Following",
        "q": "Match the language families with their connecting evidence:",
        "items": [{"left": "I. Dravidian", "key": "A"}, {"left": "II. Indo-Aryan", "key": "B"}, {"left": "III. Austroasiatic", "key": "C"}],
        "options": [{"val": "A", "text": "A. Brahui language pocket in Baluchistan"}, {"val": "B", "text": "B. Evolutionary arguments linking late Indus signs to Brahmi"}, {"val": "C", "text": "C. Substratum Munda words in Rigveda"}],
        "sol": "Dravidian is linked to Brahui, Indo-Aryan to Brahmi evolution, and Austroasiatic to Rigvedic Munda words."
    }
])

s3_mastery_hin.extend([
    {
        "type": "Match the Following",
        "q": "विद्वानों को उनके संबंधित लिपि सिद्धांतों से सुमेलित करें:",
        "items": [{"left": "I. आस्को पारपोला", "key": "A"}, {"left": "II. एस.आर. राव", "key": "B"}, {"left": "III. स्टीव फार्मर", "key": "C"}],
        "options": [{"val": "A", "text": "A. आदि-द्रविड़ भाषा परिकल्पना"}, {"val": "B", "text": "B. भारत-आर्य संस्कृत परिकल्पना"}, {"val": "C", "text": "C. गैर-भाषाई प्रतीक प्रणाली का सिद्धांत"}],
        "sol": "पारपोला द्रविड़ सिद्धांत के, राव संस्कृत सिद्धांत के, और फार्मर गैर-भाषाई सिद्धांत के समर्थक हैं।"
    },
    {
        "type": "Match the Following",
        "q": "लिपि अध्ययनों में प्रयुक्त तकनीकी पदों को उनके अर्थ से सुमेलित करें:",
        "items": [{"left": "I. रीबस पद्धति (Rebus)", "key": "A"}, {"left": "II. संकलन ग्रंथ", "key": "B"}, {"left": "III. एन्ट्रॉपी", "key": "C"}],
        "options": [{"val": "A", "text": "A. समध्वनि दर्शाने के लिए चित्र का उपयोग"}, {"val": "B", "text": "B. सभी अभिलेखों में अक्षरों की व्यवस्थित सूची"}, {"val": "C", "text": "C. अक्षरों के क्रम की सांख्यिकीय पूर्व-अनुमान्यता (predictability)"}],
        "sol": "रीबस का अर्थ समध्वनि चित्र है, संकलन ग्रंथ व्यवस्थित सूची है, और एन्ट्रॉपी क्रम की पूर्व-अनुमान्यता है।"
    },
    {
        "type": "Match the Following",
        "q": "भाषा परिवारों को उनके जोड़ने वाले पुरातात्विक/भाषाई साक्ष्यों से सुमेलित करें:",
        "items": [{"left": "I. द्रविड़", "key": "A"}, {"left": "II. भारत-आर्य", "key": "B"}, {"left": "III. ऑस्ट्रो-एशियाई", "key": "C"}],
        "options": [{"val": "A", "text": "A. बलूचिस्तान में ब्राहुई भाषा का क्षेत्र"}, {"val": "B", "text": "B. उत्तर-हड़प्पा चिन्हों को ब्राह्मी से जोड़ने वाले विकासात्मक तर्क"}, {"val": "C", "text": "C. ऋग्वेद में पाए जाने वाले मुंडा भाषा के शब्द"}],
        "sol": "द्रविड़ बलूचिस्तान की ब्राहुई से जुड़ता है, भारत-आर्य ब्राह्मी के विकासात्मक तर्क से, और ऑस्ट्रो-एशियाई ऋग्वेद के मुंडा शब्दों से।"
    }
])

# One-Liner (8)
for q, sol in [
    ("Who compiled the first comprehensive computer concordance of the Indus script in 1977?", "Iravatham Mahadevan."),
    ("Name the Dravidian language spoken in Baluchistan that supports the Dravidian hypothesis.", "Brahui."),
    ("Which Finnish scholar is famous for his work on the Dravidian decipherment of the script?", "Asko Parpola."),
    ("What is the core argument of the Farmer-Sproat-Witzel hypothesis?", "The script did not encode a spoken language but was a non-linguistic symbol system representing clans, status, or rituals."),
    ("Why is S.R. Rao's Sanskrit interpretation of the script widely rejected?", "Because it relies on arbitrary sign values and assumes a highly unlikely alphabetical system."),
    ("What Dravidian word homophonically represents both 'fish' and 'star'?", "*Min*."),
    ("What statistical method was used to prove the script has structured ordering similar to human language?", "Conditional entropy analysis."),
    ("What Munda-related language family is proposed as an alternative linguistic model?", "Austroasiatic.")
]:
    s3_mastery_eng.append({"type": "One-Liner", "q": q, "sol": sol})

for q, sol in [
    ("1977 में सिंधु लिपि का पहला कंप्यूटर संकलन किसने तैयार किया था?", "इरावथम महादेवन ने।"),
    ("बलूचिस्तान में बोली जाने वाली उस द्रविड़ भाषा का नाम बताएं जो द्रविड़ सिद्धांत का समर्थन करती है?", "ब्राहुई (Brahui)।"),
    ("सिंधु लिपि के द्रविड़ अनुवाद पर काम करने वाले प्रसिद्ध फिनिश विद्वान कौन हैं?", "आस्को पारपोला (Asko Parpola)।"),
    ("फार्मर-स्प्रोट-विटजेल परिकल्पना का मूल तर्क क्या है?", "सिंधु लिपि कोई बोली जाने वाली भाषा नहीं थी बल्कि कुल, स्तर या धार्मिक अनुष्ठानों को दर्शाने वाला गैर-भाषाई प्रतीक तंत्र थी।"),
    ("एस.आर. राव के संस्कृत आधारित अनुवाद को व्यापक रूप से क्यों अस्वीकार कर दिया गया है?", "क्योंकि यह अक्षरों के मनमाने ध्वन्यात्मक मूल्यों पर निर्भर करता है और एक असंभावित वर्णमाला प्रणाली की कल्पना करता है।"),
    ("कौन सा द्रविड़ शब्द समध्वनि के रूप में 'मछली' और 'तारे' दोनों को दर्शाता है?", "*मीन* (Min)।"),
    ("सिंधु लिपि में मानव भाषा जैसे व्यवस्थित क्रम को सिद्ध करने के लिए किस सांख्यिकीय पद्धति का उपयोग किया गया था?", "कंडीशनल एन्ट्रॉपी विश्लेषण (Conditional entropy analysis)।"),
    ("वैकल्पिक भाषाई मॉडल के रूप में मुंडा से संबंधित किस भाषा परिवार का प्रस्ताव दिया गया है?", "ऑस्ट्रो-एशियाई (Austroasiatic) परिवार।")
]:
    s3_mastery_hin.append({"type": "One-Liner", "q": q, "sol": sol})

# Assertion-Reason (8)
for q, ans, sol in [
    ("Assertion (A): The Proto-Dravidian model is the most widely supported linguistic theory for the Harappan language.\nReason (R): The survival of Brahui, a Dravidian language in Baluchistan, suggests a historic Dravidian presence in the region.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): Steve Farmer and his colleagues argue that the Indus script did not encode a spoken language.\nReason (R): They cite the extreme brevity of the texts and the lack of repeating phonetic structures as key evidence.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): S.R. Rao's decipherment of the script as Sanskrit has been universally accepted.\nReason (R): Most historical linguists reject his readings as arbitrary and morphologically inconsistent.", 3, "A is false because his readings are widely rejected. R is true."),
    ("Assertion (A): The Munda/Austroasiatic language family is a branch of Indo-European.\nReason (R): Rigvedic Sanskrit contains a number of loanwords identified as Munda in origin.", 3, "A is false because Munda is Austroasiatic, not Indo-European. R is true."),
    ("Assertion (A): Computerized entropy analyses have been used to study the Indus script.\nReason (R): Entropy measures the mathematical predictability of sign ordering to compare it with natural languages.", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): In Dravidian rebus writing, the fish sign represents astronomical stars.\nReason (R): In Proto-Dravidian, the word for fish (*min*) is a homophone for star (*min*).", 0, "Both A and R are true and R is the correct explanation of A."),
    ("Assertion (A): The Indus script is identical to the later Brahmi script.\nReason (R): Brahmi emerged in the 3rd century BCE, and there is a historical gap of over 1000 years with no transitional script.", 3, "A is false. R is true and explains why they are not identical."),
    ("Assertion (A): The non-linguistic symbol theory denies that seals were used in trade administration.\nReason (R): Non-linguistic symbols can still represent names, offices, ownership, and cargo details without encoding speech.", 3, "A is false because the theory allows trade administrative use of seals. R is true.")
]:
    s3_mastery_eng.append({"type": "Assertion-Reason", "q": q, "opts": ar_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("कथन (A): हड़प्पा भाषा के लिए आदि-द्रविड़ मॉडल सबसे व्यापक रूप से समर्थित भाषाई सिद्धांत है।\nकारण (R): बलूचिस्तान में द्रविड़ भाषा 'ब्राहुई' का बचा रहना क्षेत्र में ऐतिहासिक द्रविड़ उपस्थिति का संकेत देता है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): स्टीव फार्मर और उनके साथियों का तर्क है कि सिंधु लिपि किसी बोली जाने वाली भाषा को कोड नहीं करती थी।\nकारण (R): वे लेखों की अत्यधिक संक्षिप्तता और बार-बार दोहराए जाने वाले ध्वन्यात्मक ढांचे के अभाव को मुख्य साक्ष्य बताते हैं।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): एस.आर. राव द्वारा सिंधु लिपि को संस्कृत के रूप में पढ़ा जाना सार्वभौमिक रूप से स्वीकार कर लिया गया है।\nकारण (R): अधिकांश ऐतिहासिक भाषाविद् उनके अनुवाद को मनमाना और व्याकरणिक रूप से असंगत मानकर खारिज करते हैं।", 3, "A असत्य है क्योंकि उनका पाठ अस्वीकार कर दिया गया है। R सत्य है।"),
    ("कथन (A): मुंडा/ऑस्ट्रो-एशियाई भाषा परिवार भारोपीय परिवार की एक शाखा है।\nकारण (R): ऋग्वैदिक संस्कृत में कई ऐसे शब्द मिलते हैं जिन्हें मूल रूप से मुंडा भाषा का माना गया है।", 3, "A असत्य है क्योंकि मुंडा ऑस्ट्रो-एशियाई परिवार है, भारोपीय नहीं। R सत्य है।"),
    ("कथन (A): सिंधु लिपि के अध्ययन में कंप्यूटर आधारित एन्ट्रॉपी विश्लेषण का उपयोग किया गया है।\nकारण (R): एन्ट्रॉपी प्राकृतिक भाषाओं से तुलना करने के लिए चिन्हों के सांख्यिकीय क्रम की गणितीय भविष्यवाणी को मापती है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): द्रविड़ रीबस पद्धति में मछली का चिन्ह खगोलीय तारों का प्रतिनिधित्व करता है।\nकारण (R): आदि-द्रविड़ भाषा में मछली के लिए प्रयुक्त शब्द (*मीन*) तारे (*मीन*) का समध्वनि शब्द है।", 0, "A और R दोनों सत्य हैं और R, A की सही व्याख्या है।"),
    ("कथन (A): सिंधु लिपि बाद की ब्राह्मी लिपि के बिल्कुल समान है।\nकारण (R): ब्राह्मी का उदय तीसरी शताब्दी ईसा पूर्व में हुआ था, और दोनों के बीच 1000 से अधिक वर्षों का अंतराल है जिसमें कोई संक्रमणकालीन लिपि नहीं मिलती।", 3, "A असत्य है। R सत्य है और दोनों के भिन्न होने को स्पष्ट करता है।"),
    ("कथन (A): गैर-भाषाई प्रतीक सिद्धांत यह खारिज करता है कि मुहरों का उपयोग व्यापार प्रशासन में किया जाता था।\nकारण (R): गैर-भाषाई प्रतीक भी बिना भाषा कोड किए नाम, पद, स्वामित्व और माल के विवरण का प्रतिनिधित्व कर सकते हैं।", 3, "A असत्य है क्योंकि सिद्धांत मुहरों के प्रशासनिक उपयोग को स्वीकार करता है। R सत्य है।")
]:
    s3_mastery_hin.append({"type": "Assertion-Reason", "q": q, "opts": hin_ar_opts, "ans": ans, "sol": sol})

# Statement-Based (5)
for q, ans, sol in [
    ("Consider the following statements regarding the Dravidian hypothesis:\n1. Asko Parpola and Iravatham Mahadevan are leading scholars of this model.\n2. It matches the geographic presence of the Dravidian-speaking Brahui pocket in Baluchistan.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct and define the scholars and geographical support for the Dravidian model."),
    ("Consider the following statements regarding Indo-Aryan theories:\n1. S.R. Rao proposed that the script was written alphabetically to encode Sanskrit.\n2. His readings are universally accepted by Sanskrit scholars worldwide.\nWhich of the statements given above is/are correct?", 0, "Statement 1 is correct. Statement 2 is incorrect: his Sanskrit readings are widely rejected by mainstream scholars."),
    ("Consider the following statements regarding the non-linguistic symbol theory:\n1. It was proposed by Farmer, Sproat, and Witzel in 2004.\n2. It argues that the Indus script behaves statistically like road signs or heraldry rather than speech.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, describing the proponents and core argument of the non-linguistic theory."),
    ("Consider the following statements regarding the Munda linguistic connection:\n1. Munda belongs to the Austroasiatic language family.\n2. Substratum Munda words in the Rigveda suggest Munda speakers were present in Northwest India.\nWhich of the statements given above is/are correct?", 2, "Both statements are correct, detailing the Austroasiatic Munda family and Rigvedic substratum words."),
    ("Consider the following statements regarding computer entropy analysis:\n1. Entropy studies showed that the script has the exact same structure as random noise.\n2. The sign sequences are entirely unordered, proving a non-linguistic nature.\nWhich of the statements given above is/are correct?", 3, "Neither statement is correct. Entropy studies showed the sign sequences are ordered and resemble natural human language systems, not random noise.")
]:
    s3_mastery_eng.append({"type": "Statement-Based", "q": q, "opts": mcq_opts, "ans": ans, "sol": sol})

for q, ans, sol in [
    ("द्रविड़ सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. आस्को पारपोला और इरावथम महादेवन इस मॉडल के प्रमुख विद्वान हैं।\n2. यह बलूचिस्तान में द्रविड़ भाषी 'ब्राहुई' के भौगोलिक अस्तित्व से मेल खाता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो द्रविड़ सिद्धांत के विद्वानों और उसके भौगोलिक साक्ष्य को स्पष्ट करते हैं।"),
    ("भारत-आर्य सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एस.आर. राव ने प्रस्ताव दिया कि संस्कृत को कोड करने के लिए लिपि वर्णमाला के रूप में लिखी गई थी।\n2. उनका अनुवाद दुनिया भर के संस्कृत विद्वानों द्वारा सर्वसम्मति से स्वीकार किया गया है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 0, "कथन 1 सही है। कथन 2 गलत है क्योंकि उनके अनुवाद को मुख्यधारा के विद्वानों द्वारा खारिज किया गया है।"),
    ("गैर-भाषाई प्रतीक सिद्धांत के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. इसे 2004 में फार्मर, स्प्रोट और विटजेल द्वारा प्रस्तावित किया गया था।\n2. यह तर्क देता है कि सिंधु लिपि सांख्यिकीय रूप से भाषा के बजाय सड़क के संकेतों या राजकीय चिन्हों की तरह व्यवहार करती है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो गैर-भाषाई सिद्धांत के लेखकों और उसके मूल तर्क का वर्णन करते हैं।"),
    ("मुंडा भाषाई संबंध के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. मुंडा भाषा ऑस्ट्रो-एशियाई भाषा परिवार से संबंधित है।\n2. ऋग्वेद में पाए जाने वाले मुंडा शब्द यह दर्शाते हैं कि मुंडा भाषी उत्तर-पश्चिम भारत में उपस्थित थे।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 2, "दोनों कथन सही हैं, जो मुंडा भाषा परिवार और ऋग्वेद में उसके प्रभाव को स्पष्ट करते हैं।"),
    ("कंप्यूटर एन्ट्रॉपी विश्लेषण के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. एन्ट्रॉपी अध्ययनों से सिद्ध हुआ कि सिंधु लिपि की संरचना पूरी तरह से यादृच्छिक कोलाहल (random noise) जैसी है।\n2. अक्षरों का क्रम पूरी तरह से अनियोजित है, जो इसके गैर-भाषाई स्वरूप को सिद्ध करता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?", 3, "दोनों कथन गलत हैं। एन्ट्रॉपी अध्ययनों ने साबित किया कि सिंधु लिपि का क्रम व्यवस्थित है और यादृच्छिक कोलाहल के बजाय मानव भाषाओं से मेल खाता है।")
]:
    s3_mastery_hin.append({"type": "Statement-Based", "q": q, "opts": hin_mcq_opts, "ans": ans, "sol": sol})

# Why (3)
for q, sol in [
    ("Why is the Brahui language of Baluchistan significant in debates about the Indus script?", "Because Brahui is a Dravidian language spoken in Baluchistan, proving that Dravidian languages were historically present in the northwest near the Indus Valley, supporting the Dravidian hypothesis."),
    ("Why did Steve Farmer and his co-authors claim the Indus script is non-linguistic?", "Because the inscriptions are extremely short (averaging 5 signs) with low repeat frequencies, lacking the length and repetition required to carry spoken grammar or sentences."),
    ("Why do linguists use the Rebus principle to interpret signs in a logo-syllabic script?", "Because a logo-syllabic script cannot easily draw abstract words, so it uses the picture of a concrete object that has the same spoken sound (homophone) as the abstract concept.")
]:
    s3_mastery_eng.append({"type": "Why", "q": q, "sol": sol})

for q, sol in [
    ("सिंधु लिपि के विवादों में बलूचिस्तान की ब्राहुई भाषा का क्या महत्व है?", "क्योंकि ब्राहुई बलूचिस्तान में बोली जाने वाली एक द्रविड़ भाषा है, जो यह सिद्ध करती है कि द्रविड़ भाषाएं ऐतिहासिक रूप से उत्तर-पश्चिम में मौजूद थीं, जिससे द्रविड़ सिद्धांत को समर्थन मिलता है।"),
    ("स्टीव फार्मर और उनके सहयोगियों ने सिंधु लिपि को गैर-भाषाई क्यों माना?", "क्योंकि ये लेख बहुत छोटे हैं (औसत 5 चिन्ह) और इनमें अक्षरों का दोहराव बहुत कम है, जो व्याकरणिक वाक्यों या बोली जाने वाली भाषा को कोड करने के लिए आवश्यक संरचनाओं से मेल नहीं खाता।"),
    ("भाषाविद् लोगो-सिलेबिक लिपि में चिन्हों को पढ़ने के लिए रीबस (Rebus) पद्धति का उपयोग क्यों करते हैं?", "क्योंकि ऐसी लिपि में अमूर्त शब्दों के चित्र बनाना कठिन होता है, इसलिए उस ठोस वस्तु के चित्र का उपयोग किया जाता है जिसका उच्चारण अमूर्त शब्द के समान (homophone) होता है।")
]:
    s3_mastery_hin.append({"type": "Why", "q": q, "sol": sol})

# How (3)
for q, sol in [
    ("How does the Rebus principle work in interpreting the fish sign in the Dravidian model?", "The fish sign is read as Dravidian *min*. Since *min* also means star, the fish sign is interpreted to represent astral deities or stars on seals using homophonic substitution."),
    ("How did statistical analysis of conditional entropy challenge the non-linguistic theory?", "By calculating the probability of sign sequences, researchers found that the Indus script has a highly structured sign ordering that behaves like human language, rather than random symbols or coats-of-arms."),
    ("How does the Indo-Aryan hypothesis explain the connection between Harappan signs and historical Brahmi?", "Proponents argue that late Harappan symbols evolved into early Brahmi characters, suggesting a direct graphical transition and continuity of script in ancient India.")
]:
    s3_mastery_eng.append({"type": "How", "q": q, "sol": sol})

for q, sol in [
    ("द्रविड़ मॉडल में मछली के चिन्ह को समझने के लिए रीबस पद्धति कैसे काम करती है?", "मछली के चिन्ह को द्रविड़ शब्द *मीन* पढ़ा जाता है। चूँकि *मीन* का अर्थ तारा भी होता है, इसलिए रीबस पद्धति के अनुसार मछली का चिन्ह मुहरों पर खगोलीय देवताओं या तारों को दर्शाता है।"),
    ("कंडीशनल एन्ट्रॉपी के सांख्यिकीय विश्लेषण ने गैर-भाषाई सिद्धांत को कैसे चुनौती दी?", "चिन्हों के क्रम की संभावनाओं की गणना करके शोधकर्ताओं ने पाया कि सिंधु लिपि में अक्षरों का क्रम अत्यधिक सुव्यवस्थित है जो मानव भाषाओं की तरह व्यवहार करता है, न कि यादृच्छिक प्रतीकों की तरह।"),
    ("भारत-आर्य परिकल्पना हड़प्पा चिन्हों और ऐतिहासिक ब्राह्मी लिपि के बीच के संबंध को कैसे समझाती है?", "इसके समर्थकों का तर्क है कि देर के हड़प्पा चिन्ह धीरे-धीरे ब्राह्मी अक्षरों में विकसित हुए, जो प्राचीन भारत में लिपि की निरंतरता और विकास को दर्शाता है।")
]:
    s3_mastery_hin.append({"type": "How", "q": q, "sol": sol})

# Case Study (3)
for q, sol in [
    ("Case Study: The Brahui language of Baluchistan is surrounded by Indo-Aryan and Iranian languages. What historical linguistic process explains this island of Dravidian speakers, and how does it support Harappan theories?", "It is an enclave or remnant of a much larger prehistoric Dravidian-speaking area that once extended across Northwest India, suggesting the Indus Valley population spoke a Proto-Dravidian language."),
    ("Case Study: Analyzing the 'fish' sign with six strokes. Under the Dravidian model, *min* (fish) plus the word for six (*aru*) translates homophonically to *aru-min*, meaning the Pleiades star cluster. What does this case study demonstrate?", "It demonstrates how Dravidian homophony (rebus writing) is used to translate abstract astronomical meanings from simple pictographic combinations on seals."),
    ("Case Study: Critique S.R. Rao's decipherment of the word 'eka-asva' (one horse) from a seal. Why did historical linguists point out that horses were not domestic staples in the Mature Harappan phase to reject his translation?", "Because his reading conflicted with the archaeological record, which shows that horses were not commonly domesticated or depicted in Mature Harappan culture, proving his translation was anachronistic.")
]:
    s3_mastery_eng.append({"type": "Case Study", "q": q, "sol": sol})

for q, sol in [
    ("केस स्टडी: बलूचिस्तान की ब्राहुई भाषा भारत-आर्य और ईरानी भाषाओं से घिरी हुई है। कौन सी ऐतिहासिक भाषाई प्रक्रिया इस द्रविड़ भाषी द्वीप को समझाती है, और यह हड़प्पा के सिद्धांतों का समर्थन कैसे करती है?", "यह प्रागैतिहासिक काल के एक बड़े द्रविड़-भाषी क्षेत्र का बचा हुआ हिस्सा है जो कभी उत्तर-पश्चिम भारत में फैला था, जो संकेत देता है कि सिंधु घाटी के लोग आदि-द्रविड़ भाषा बोलते थे।"),
    ("केस स्टडी: छह रेखाओं (strokes) के साथ 'मछली' के चिन्ह का विश्लेषण। द्रविड़ मॉडल के तहत, मीन (मछली) और छह (*अरु*) मिलकर समध्वनि के रूप में *अरु-मीन* बनते हैं, जिसका अर्थ कृत्तिका नक्षत्र (Pleiades) होता है। यह केस स्टडी क्या प्रदर्शित करती है?", "यह प्रदर्शित करती है कि मुहरों पर सरल चित्रों के संयोजनों से अमूर्त खगोलीय अर्थ निकालने के लिए द्रविड़ समध्वनि (rebus) का उपयोग कैसे किया जाता है।"),
    ("केस स्टडी: एक मुहर से शब्द 'एक-अश्व' (eka-asva) के एस.आर. राव के अनुवाद की समीक्षा। ऐतिहासिक भाषाविदों ने उनके अनुवाद को खारिज करने के लिए क्यों तर्क दिया कि परिपक्व हड़प्पा काल में घोड़े मुख्य पालतू जानवर नहीं थे?", "क्योंकि उनका अनुवाद पुरातात्विक साक्ष्यों से मेल नहीं खाता था, जो दर्शाते हैं कि परिपक्व हड़प्पा संस्कृति में घोड़े आम तौर पर पालतू या चित्रित नहीं थे, जिससे उनका अनुवाद कालभ्रमित (anachronistic) सिद्ध हुआ।")
]:
    s3_mastery_hin.append({"type": "Case Study", "q": q, "sol": sol})

# Teach Concept (3)
for q, sol in [
    ("Explain the 'Rebus Principle' of writing to a student using a modern English example.", "The Rebus Principle uses the picture of a word that sounds like another word to represent it. For example, to write the abstract message 'I can see you', you could draw pictures of an Eye (I), a tin Can (can), the Sea (see), and a female sheep or Ewe (you)."),
    ("Explain the significance of the Brahui language pocket in Indus valley linguistic debates.", "Brahui is a Dravidian language spoken today in Baluchistan, Pakistan. Because it is thousands of miles away from other Dravidian languages in South India, it acts as a linguistic fossil, proving that Dravidian languages were once spoken in the Indus Valley region before being overtaken by Indo-Aryan languages."),
    ("Explain what a 'Concordance' is in the context of deciphering an ancient script.", "A concordance is a systematic index of all script signs. It catalogues every single inscription, listing which signs appear, their frequencies, what signs appear next to them, and on what materials. It allows scholars to analyze sign distribution mathematically without knowing the actual language.")
]:
    s3_mastery_eng.append({"type": "Teach Concept", "q": q, "sol": sol})

for q, sol in [
    ("एक छात्र को आधुनिक अंग्रेजी/हिंदी उदाहरण का उपयोग करके लेखन की 'रीबस पद्धति' (Rebus Principle) समझाएं।", "रीबस पद्धति में किसी शब्द के चित्र का उपयोग उसकी समध्वनि वाले दूसरे शब्द को दर्शाने के लिए किया जाता है। जैसे हिंदी में 'जग' (पानी का बर्तन) का चित्र बनाकर 'संसार' (जग) के अर्थ को प्रकट करना।"),
    ("सिंधु घाटी के भाषाई विवादों में 'ब्राहुई भाषा क्षेत्र' के महत्व को समझाएं।", "ब्राहुई आज पाकिस्तान के बलूचिस्तान में बोली जाने वाली एक द्रविड़ भाषा है। चूँकि यह दक्षिण भारत की अन्य द्रविड़ भाषाओं से हजारों मील दूर है, यह एक भाषाई जीवाश्म की तरह कार्य करती है, जो प्रमाणित करती है कि बलूचिस्तान/सिंधु क्षेत्र में कभी द्रविड़ भाषाएँ बोली जाती थीं।"),
    ("प्राचीन लिपि को पढ़ने के संदर्भ में 'संकलन ग्रंथ' (Concordance) क्या होता है, समझाएं।", "संकलन ग्रंथ सभी लिपि चिन्हों का एक व्यवस्थित सूचकांक होता है। यह प्रत्येक अभिलेख को सूचीबद्ध करता है कि कौन से चिन्ह दिखाई देते हैं, उनकी आवृत्ति क्या है, उनके बगल में कौन से चिन्ह आते हैं और वे किस सामग्री पर हैं, जिससे गणितीय विश्लेषण संभव होता है।")
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
