from .helpers import add_mcq, add_multi_mcq, add_stmt, add_ar

practice_en = []
practice_hi = []

# UPSC-style practice questions — 50 total
# Format: mix of MCQ, Multi-correct, Statement-based, Assertion-Reason

# --- MCQ (15) ---
add_mcq(practice_en, practice_hi,
    "The Mesolithic period in India is generally dated to approximately:",
    "भारत में मध्यपाषाण काल की तिथि सामान्यतः किस रूप में मानी जाती है:",
    ["40,000–10,000 BCE", "12,000–2,500 BCE", "5,000–1,500 BCE", "1,00,000–40,000 BCE"],
    ["40,000–10,000 ईसा पूर्व", "12,000–2,500 ईसा पूर्व", "5,000–1,500 ईसा पूर्व", "1,00,000–40,000 ईसा पूर्व"],
    1,
    "The Indian Mesolithic broadly spans c. 12,000–2,500 BCE, corresponding to the post-glacial Holocene.",
    "भारतीय मध्यपाषाण काल लगभग 12,000–2,500 ईसा पूर्व तक फैला है, जो हिमयुगोत्तर होलोसीन के अनुरूप है।"
)

add_mcq(practice_en, practice_hi,
    "The defining tool technology of the Mesolithic period is:",
    "मध्यपाषाण काल की परिभाषित उपकरण प्रौद्योगिकी है:",
    ["Polished stone axes", "Microliths (geometric miniaturised tools)", "Hand-axes and cleavers", "Copper and bronze tools"],
    ["पॉलिश किए गए पत्थर के कुल्हाड़े", "सूक्ष्म पाषाण (ज्यामितीय लघु उपकरण)", "हैंड-एक्स और क्लीवर", "तांबे और कांसे के उपकरण"],
    1,
    "Microliths — small, geometric, standardised blades made from chert or chalcedony — define the Mesolithic period globally.",
    "सूक्ष्म पाषाण — चर्ट या चाल्सीडोनी से बने छोटे, ज्यामितीय, मानकीकृत ब्लेड — विश्व स्तर पर मध्यपाषाण काल को परिभाषित करते हैं।"
)

add_mcq(practice_en, practice_hi,
    "The Mesolithic period corresponds to which geological epoch?",
    "मध्यपाषाण काल किस भूवैज्ञानिक युग से मेल खाता है?",
    ["Pleistocene", "Holocene", "Miocene", "Oligocene"],
    ["प्लीस्टोसीन", "होलोसीन", "मायोसीन", "ऑलिगोसीन"],
    1,
    "The Holocene epoch began c. 11,700 years ago, coinciding with the start of the Indian Mesolithic cultural phase.",
    "होलोसीन युग लगभग 11,700 वर्ष पहले शुरू हुआ, जो भारतीय मध्यपाषाण सांस्कृतिक चरण की शुरुआत के साथ मेल खाता है।"
)

add_mcq(practice_en, practice_hi,
    "Which of the following correctly describes a 'composite tool' in the Mesolithic context?",
    "निम्नलिखित में से कौन मध्यपाषाण संदर्भ में 'संयुक्त उपकरण' का सही वर्णन करता है?",
    ["A single large stone scraped on both faces", "Multiple microliths hafted together into a wooden or bone handle", "A polished stone grinding platform", "A copper blade with a bone handle"],
    ["दोनों सतहों पर छिली हुई एकल बड़ी पत्थर", "एक लकड़ी या हड्डी के हैंडल में एक साथ जड़े कई सूक्ष्म पाषाण", "एक पॉलिश किया हुआ पत्थर पीसने का प्लेटफार्म", "हड्डी के हैंडल वाली तांबे की ब्लेड"],
    1,
    "Composite tools combine multiple microliths into a single functional implement — one of the key Mesolithic technological innovations.",
    "संयुक्त उपकरण कई सूक्ष्म पाषाणों को एक ही कार्यात्मक उपकरण में जोड़ते हैं — मध्यपाषाण काल के प्रमुख तकनीकी नवाचारों में से एक।"
)

add_mcq(practice_en, practice_hi,
    "The principal raw material used for making microliths in India was:",
    "भारत में सूक्ष्म पाषाण बनाने के लिए उपयोग की जाने वाली प्रमुख कच्ची सामग्री थी:",
    ["Obsidian and marble", "Chert and chalcedony", "Granite and sandstone", "Basalt and limestone"],
    ["ऑब्सीडियन और संगमरमर", "चर्ट और चाल्सीडोनी", "ग्रेनाइट और बलुआ पत्थर", "बेसाल्ट और चूना पत्थर"],
    1,
    "Chert and chalcedony (fine-grained, silica-rich stones) were preferred for their sharp conchoidal fracture and availability.",
    "चर्ट और चाल्सीडोनी (बारीक दाने वाले, सिलिका-समृद्ध पत्थर) अपने तेज शंखाभ फ्रैक्चर और उपलब्धता के कारण पसंद किए जाते थे।"
)

add_mcq(practice_en, practice_hi,
    "Bagor on the Kothari River is significant because it:",
    "कोठारी नदी पर बागोर महत्वपूर्ण है क्योंकि यह:",
    ["Is the oldest Paleolithic site in India", "Is the largest Mesolithic site in India with three-phase stratigraphy", "Contains the largest Mesolithic burial ground in the world", "Shows the first evidence of rice cultivation in India"],
    ["भारत का सबसे पुराना पुरापाषाणकालीन स्थल है", "तीन-चरण स्तरविन्यास के साथ भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है", "दुनिया का सबसे बड़ा मध्यपाषाणकालीन शवाधान स्थल है", "भारत में चावल की खेती का पहला साक्ष्य दिखाता है"],
    1,
    "Bagor has three distinct phases (Mesolithic → Chalcolithic → Historical) and is the largest known Mesolithic site.",
    "बागोर में तीन अलग-अलग चरण हैं (मध्यपाषाण → ताम्रपाषाण → ऐतिहासिक) और यह सबसे बड़ा ज्ञात मध्यपाषाणकालीन स्थल है।"
)

add_mcq(practice_en, practice_hi,
    "The earliest evidence of interpersonal violence in Indian prehistory comes from:",
    "भारतीय प्रागैतिहास में व्यक्तिगत हिंसा का सबसे पहला साक्ष्य कहाँ से मिलता है:",
    ["Damdama — a skeleton pierced by a bone spear", "Sarai Nahar Rai — a skeleton with a microlithic arrowhead in the pelvis", "Bhimbetka — a rock painting showing combat", "Langhnaj — a crushed skull found in the burial layer"],
    ["दमदमा — हड्डी के भाले से छिदा कंकाल", "सराय नाहर राय — कूल्हे में सूक्ष्म पाषाण तीर नोक वाला कंकाल", "भीमबेटका — युद्ध दिखाने वाली एक शैल चित्रकारी", "लांघनाज — दफन परत में मिली कुचली खोपड़ी"],
    1,
    "The skeleton at Sarai Nahar Rai with an embedded microlithic arrowhead in the pelvis is the oldest physical evidence of human lethal conflict in India.",
    "सराय नाहर राय में कूल्हे में धँसी सूक्ष्म पाषाण तीर की नोक वाला कंकाल भारत में मानव घातक संघर्ष का सबसे पुराना भौतिक साक्ष्य है।"
)

add_mcq(practice_en, practice_hi,
    "Who excavated the Ganga valley Mesolithic sites of Sarai Nahar Rai, Mahadaha, and Damdama?",
    "सराय नाहर राय, महदहा और दमदमा के गंगा घाटी मध्यपाषाणकालीन स्थलों का उत्खनन किसने किया?",
    ["H.D. Sankalia", "V.N. Misra", "G.R. Sharma", "B.B. Lal"],
    ["एच.डी. सांकलिया", "वी.एन. मिश्रा", "जी.आर. शर्मा", "बी.बी. लाल"],
    2,
    "G.R. Sharma of Allahabad University excavated all three Pratapgarh district Mesolithic sites.",
    "इलाहाबाद विश्वविद्यालय के जी.आर. शर्मा ने प्रतापगढ़ जिले के तीनों मध्यपाषाणकालीन स्थलों का उत्खनन किया।"
)

add_mcq(practice_en, practice_hi,
    "Bhimbetka was inscribed as a UNESCO World Heritage Site in:",
    "भीमबेटका को UNESCO विश्व धरोहर स्थल के रूप में कब नामांकित किया गया था:",
    ["1986", "1993", "2003", "2011"],
    ["1986", "1993", "2003", "2011"],
    2,
    "Bhimbetka was inscribed as a UNESCO World Heritage Site in 2003.",
    "भीमबेटका को 2003 में UNESCO विश्व धरोहर स्थल के रूप में नामांकित किया गया था।"
)

add_mcq(practice_en, practice_hi,
    "The transition from Mesolithic to Neolithic is primarily characterised by the shift from:",
    "मध्यपाषाण से नवपाषाण काल में संक्रमण मुख्य रूप से किसमें बदलाव द्वारा चित्रित है:",
    ["Stone to copper tools", "Foraging and pastoralism to sedentary agriculture and pottery-making", "Rock art to script writing", "Semi-nomadic to fully nomadic lifestyle"],
    ["पत्थर से तांबे के उपकरण", "भोजन संग्रह और पशुपालन से स्थायी कृषि और मिट्टी के बर्तन बनाने तक", "शैल कला से लिपि लेखन तक", "अर्ध-घुमंतू से पूरी तरह घुमंतू जीवन शैली"],
    1,
    "The Neolithic revolution is defined by food production (farming + herding) replacing food collection, and the development of pottery.",
    "नवपाषाण क्रांति को खाद्य उत्पादन (खेती + पशुपालन) द्वारा खाद्य संग्रह को प्रतिस्थापित करने और मिट्टी के बर्तनों के विकास द्वारा परिभाषित किया जाता है।"
)

add_mcq(practice_en, practice_hi,
    "Which of the following correctly differentiates Mesolithic from Paleolithic tool technology?",
    "निम्नलिखित में से कौन सा मध्यपाषाणकालीन उपकरण प्रौद्योगिकी को पुरापाषाणकालीन से सही ढंग से अलग करता है?",
    ["Paleolithic tools are smaller; Mesolithic tools are larger", "Mesolithic tools (microliths) are smaller, standardised, and more specialised than large Paleolithic tools", "Mesolithic tools were exclusively made of copper", "Paleolithic tools are geometric; Mesolithic tools are non-geometric"],
    ["पुरापाषाणकालीन उपकरण छोटे हैं; मध्यपाषाणकालीन उपकरण बड़े हैं", "मध्यपाषाणकालीन उपकरण (सूक्ष्म पाषाण) बड़े पुरापाषाणकालीन उपकरणों की तुलना में छोटे, मानकीकृत और अधिक विशेष हैं", "मध्यपाषाणकालीन उपकरण विशेष रूप से तांबे से बने थे", "पुरापाषाणकालीन उपकरण ज्यामितीय हैं; मध्यपाषाणकालीन उपकरण गैर-ज्यामितीय हैं"],
    1,
    "The miniaturisation and standardisation of microliths distinguishes Mesolithic tool technology from the large, less standardised Paleolithic tools.",
    "सूक्ष्म पाषाणों का लघुकरण और मानकीकरण मध्यपाषाणकालीन उपकरण प्रौद्योगिकी को बड़े, कम मानकीकृत पुरापाषाणकालीन उपकरणों से अलग करता है।"
)

add_mcq(practice_en, practice_hi,
    "The dominant pigment used in Bhimbetka Mesolithic rock art, red haematite, comes from which mineral family?",
    "भीमबेटका मध्यपाषाणकालीन शैल कला में उपयोग किया जाने वाला प्रमुख रंगद्रव्य, लाल हेमेटाइट, किस खनिज परिवार से आता है?",
    ["Silicate minerals", "Iron oxides", "Carbonate minerals", "Sulphide minerals"],
    ["सिलिकेट खनिज", "आयरन ऑक्साइड", "कार्बोनेट खनिज", "सल्फाइड खनिज"],
    1,
    "Haematite (Fe₂O₃) is an iron oxide mineral — one of the most chemically stable natural pigments.",
    "हेमेटाइट (Fe₂O₃) एक आयरन ऑक्साइड खनिज है — सबसे रासायनिक रूप से स्थिर प्राकृतिक रंगद्रव्यों में से एक।"
)

add_mcq(practice_en, practice_hi,
    "V.S. Wakankar is associated with the discovery of which prehistoric site?",
    "वी.एस. वाकणकर किस प्रागैतिहासिक स्थल की खोज से जुड़े हैं?",
    ["Bagor", "Langhnaj", "Bhimbetka", "Adamgarh"],
    ["बागोर", "लांघनाज", "भीमबेटका", "आदमगढ़"],
    2,
    "V.S. Wakankar discovered the Bhimbetka rock shelter complex in 1957-58.",
    "वी.एस. वाकणकर ने 1957-58 में भीमबेटका शैल आश्रय परिसर की खोज की।"
)

add_mcq(practice_en, practice_hi,
    "The concept of 'broad-spectrum revolution' in Mesolithic subsistence refers to:",
    "मध्यपाषाणकालीन जीवन निर्वाह में 'व्यापक-स्पेक्ट्रम क्रांति' की अवधारणा से तात्पर्य है:",
    ["Revolution in agricultural tools to improve crop yield", "Diversification of food sources from hunting large game to multiple resources including fish, plants, and small animals", "Development of broad-bladed metal weapons", "Introduction of widespread grain cultivation across the subcontinent"],
    ["फसल उत्पादन बढ़ाने के लिए कृषि उपकरणों में क्रांति", "बड़े शिकार से मछली, पौधों और छोटे जानवरों सहित कई संसाधनों तक खाद्य स्रोतों का विविधीकरण", "व्यापक-ब्लेड वाले धातु हथियारों का विकास", "उपमहाद्वीप में व्यापक अनाज की खेती का परिचय"],
    1,
    "The broad-spectrum revolution describes the Mesolithic shift from specialised large-game hunting to multi-source foraging.",
    "व्यापक-स्पेक्ट्रम क्रांति विशेष बड़े-शिकार शिकार से बहु-स्रोत भोजन संग्रह में मध्यपाषाणकालीन बदलाव का वर्णन करती है।"
)

add_mcq(practice_en, practice_hi,
    "Which period marks the end of the Mesolithic in the Indian context?",
    "भारतीय संदर्भ में मध्यपाषाण काल का अंत कौन से काल में होता है?",
    ["Advent of iron technology", "Beginning of the Neolithic with food production and pottery", "Start of the Bronze Age", "End of the Pleistocene"],
    ["लौह प्रौद्योगिकी का आगमन", "खाद्य उत्पादन और मिट्टी के बर्तनों के साथ नवपाषाण काल की शुरुआत", "कांस्य युग की शुरुआत", "प्लीस्टोसीन का अंत"],
    1,
    "The Neolithic food-producing revolution (farming + pottery) marks the end of the Mesolithic hunter-gatherer phase.",
    "नवपाषाण खाद्य-उत्पादन क्रांति (खेती + मिट्टी के बर्तन) मध्यपाषाणकालीन शिकारी-संग्रहकर्ता चरण के अंत को चिह्नित करती है।"
)

# --- Multi-Correct MCQ (15) ---
add_multi_mcq(practice_en, practice_hi,
    "Which of the following are correct about Mesolithic stone tool technology? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन पत्थर उपकरण प्रौद्योगिकी के बारे में सही हैं? (सभी सही विकल्प चुनें)",
    ["Microliths were smaller and more specialised than Paleolithic tools", "Pressure flaking was used to shape microliths precisely", "Composite tools combined multiple microliths in organic handles", "Microliths were predominantly made from polished granite"],
    ["सूक्ष्म पाषाण पुरापाषाणकालीन उपकरणों की तुलना में छोटे और अधिक विशेष थे", "सूक्ष्म पाषाणों को सटीक रूप से आकार देने के लिए दबाव फ्लेकिंग का उपयोग किया जाता था", "संयुक्त उपकरणों में जैविक हैंडल में कई सूक्ष्म पाषाण संयुक्त होते थे", "सूक्ष्म पाषाण मुख्य रूप से पॉलिश किए गए ग्रेनाइट से बने थे"],
    [0, 1, 2],
    "All three first options are correct. Microliths were made from silica-rich stones (chert/chalcedony), not polished granite.",
    "पहले तीनों विकल्प सही हैं। सूक्ष्म पाषाण सिलिका-समृद्ध पत्थरों (चर्ट/चाल्सीडोनी) से बने थे, पॉलिश किए गए ग्रेनाइट से नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which climatic changes drove the cultural transition from Paleolithic to Mesolithic? (Select all that apply)",
    "पुरापाषाण से मध्यपाषाण काल में सांस्कृतिक संक्रमण को किन जलवायु परिवर्तनों ने प्रेरित किया? (सभी सही विकल्प चुनें)",
    ["Warming temperatures after the Last Glacial Maximum", "Rise in sea levels reducing coastal habitats", "Shift from grasslands to forests and woodlands", "Onset of a new glaciation that froze the subcontinent"],
    ["अंतिम हिमाच्छादन अधिकतम के बाद तापमान में वृद्धि", "समुद्र के स्तर में वृद्धि से तटीय आवास कम हुए", "घास के मैदानों से जंगलों और वनों में बदलाव", "नई हिमाच्छादन की शुरुआत जिसने उपमहाद्वीप को जमा दिया"],
    [0, 1, 2],
    "The three correct answers describe post-glacial warming. A new glaciation did not occur — the planet warmed during the Holocene.",
    "तीन सही उत्तर हिमयुगोत्तर ताप का वर्णन करते हैं। कोई नई हिमाच्छादन नहीं हुई — होलोसीन के दौरान ग्रह गर्म हुआ।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are documented at Mesolithic Ganga valley sites (Sarai Nahar Rai, Mahadaha, Damdama)? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन गंगा घाटी स्थलों (सराय नाहर राय, महदहा, दमदमा) पर दस्तावेजीकृत हैं? (सभी सही विकल्प चुनें)",
    ["Intra-settlement human burials", "Microliths as grave goods", "Bone ornaments (necklaces/earrings)", "Burnt mud-brick walls of permanent houses"],
    ["बस्ती-अंतर्गत मानव शवाधान", "कब्र के सामान के रूप में सूक्ष्म पाषाण", "हड्डी के आभूषण (हार/झुमके)", "स्थायी घरों की जली हुई मिट्टी की ईंटों की दीवारें"],
    [0, 1, 2],
    "Intra-settlement burials, microliths, and bone ornaments are all documented. There are no permanent mud-brick structures at Mesolithic sites.",
    "बस्ती-अंतर्गत शवाधान, सूक्ष्म पाषाण और हड्डी के आभूषण सभी दस्तावेजीकृत हैं। मध्यपाषाणकालीन स्थलों पर कोई स्थायी मिट्टी-ईंट संरचनाएं नहीं हैं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following correctly identify features of the Bhimbetka rock art site? (Select all that apply)",
    "निम्नलिखित में से कौन से भीमबेटका शैल कला स्थल की सही विशेषताएं पहचानते हैं? (सभी सही विकल्प चुनें)",
    ["Located near Bhopal in Madhya Pradesh", "Has over 700 rock shelters with paintings", "Discovered by V.S. Wakankar in 1957-58", "Shows paintings exclusively from the Mesolithic period"],
    ["मध्य प्रदेश में भोपाल के पास स्थित", "चित्रकारी के साथ 700 से अधिक शैल आश्रय हैं", "1957-58 में वी.एस. वाकणकर द्वारा खोजा गया", "केवल मध्यपाषाण काल से चित्रकारी दिखाता है"],
    [0, 1, 2],
    "The first three options are correct. Bhimbetka has paintings from multiple periods (Paleolithic through to historical), not exclusively Mesolithic.",
    "पहले तीन विकल्प सही हैं। भीमबेटका में कई कालों की चित्रकारी है (पुरापाषाण से ऐतिहासिक तक), केवल मध्यपाषाण काल से नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following characterise the Mesolithic subsistence economy? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन जीवन निर्वाह अर्थव्यवस्था की विशेषता बताते हैं? (सभी सही विकल्प चुनें)",
    ["Broad-spectrum foraging including hunting, fishing, and plant gathering", "Semi-nomadic seasonal movements following resources", "Early domestication of animals at sites like Bagor and Adamgarh", "Full-scale irrigated paddy cultivation in the Ganga valley"],
    ["शिकार, मछली पकड़ने और पौधों के संग्रह सहित व्यापक-स्पेक्ट्रम भोजन संग्रह", "संसाधनों का अनुसरण करते हुए अर्ध-घुमंतू मौसमी गतिविधियाँ", "बागोर और आदमगढ़ जैसे स्थलों पर जानवरों का प्रारंभिक पालतूकरण", "गंगा घाटी में पूर्ण पैमाने पर सिंचित धान की खेती"],
    [0, 1, 2],
    "The first three are correct. Irrigated paddy cultivation belongs to the Neolithic phase, not the Mesolithic.",
    "पहले तीन सही हैं। सिंचित धान की खेती नवपाषाण चरण से संबंधित है, मध्यपाषाण से नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are examples of geometric microliths? (Select all that apply)",
    "निम्नलिखित में से कौन से ज्यामितीय सूक्ष्म पाषाणों के उदाहरण हैं? (सभी सही विकल्प चुनें)",
    ["Triangles", "Trapeze", "Lunate (crescent)", "Handaxe"],
    ["त्रिकोण", "ट्रेपेज़ (समलम्ब)", "लूनेट (अर्धचंद्र)", "हैंड एक्स"],
    [0, 1, 2],
    "Triangles, trapeze, and lunates (crescents) are all geometric microlith types. Handaxes are large Paleolithic tools, not microliths.",
    "त्रिकोण, ट्रेपेज़ और लूनेट सभी ज्यामितीय सूक्ष्म पाषाण प्रकार हैं। हैंड एक्स बड़े पुरापाषाणकालीन उपकरण हैं, सूक्ष्म पाषाण नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following correctly identify site-specific Mesolithic findings? (Select all that apply)",
    "निम्नलिखित में से कौन से स्थल-विशिष्ट मध्यपाषाणकालीन निष्कर्षों की सही पहचान करते हैं? (सभी सही विकल्प चुनें)",
    ["Damdama: 41 human burials including triple burials", "Langhnaj: excavated by H.D. Sankalia in the Sabarmati basin", "Bagor: earliest animal domestication evidence in India", "Mahadaha: contains polished stone axes (Neolithic tool kit)"],
    ["दमदमा: तिहरी कब्रों सहित 41 मानव कब्रें", "लांघनाज: साबरमती बेसिन में एच.डी. सांकलिया द्वारा उत्खनित", "बागोर: भारत में सबसे पहले पशुपालन साक्ष्य", "महदहा: पॉलिश किए गए पत्थर के कुल्हाड़े (नवपाषाण उपकरण सेट) है"],
    [0, 1, 2],
    "All first three are correct. Mahadaha is a Mesolithic site with microliths and bone ornaments, not polished axes (which are Neolithic).",
    "पहले तीन सही हैं। महदहा सूक्ष्म पाषाण और हड्डी के आभूषणों वाला मध्यपाषाणकालीन स्थल है, पॉलिश किए गए कुल्हाड़े (जो नवपाषाणकालीन हैं) नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are indicators of social differentiation in Mesolithic burial sites? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन शवाधान स्थलों में सामाजिक भेद के संकेतक हैं? (सभी सही विकल्प चुनें)",
    ["Variation in the richness of grave goods between burials", "Multiple burials (double and triple) versus single burials", "Presence of bone ornaments only in some graves", "Use of written tomb inscriptions marking social rank"],
    ["शवाधानों के बीच कब्र के सामान की समृद्धि में भिन्नता", "एकल शवाधान के विपरीत कई शवाधान (दोहरे और तिहरे)", "केवल कुछ कब्रों में हड्डी के आभूषणों की उपस्थिति", "सामाजिक रैंक दर्शाने वाले लिखित कब्र शिलालेख"],
    [0, 1, 2],
    "Variation in grave goods, multiple burials, and selective ornament placement all indicate social ranking. Written inscriptions were impossible in the pre-literate Mesolithic.",
    "कब्र के सामान में भिन्नता, कई शवाधान और चयनात्मक आभूषण प्लेसमेंट सभी सामाजिक रैंकिंग को इंगित करते हैं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which ecological settings supported Mesolithic communities in the Ganga plains? (Select all that apply)",
    "गंगा के मैदानों में किन पारिस्थितिक स्थापनाओं ने मध्यपाषाणकालीन समुदायों का समर्थन किया? (सभी सही विकल्प चुनें)",
    ["Oxbow lakes providing year-round freshwater and fish", "Dense monsoon forests providing small game and plant foods", "River floodplains with seasonal wild plant resources", "Himalayan glaciers providing stone raw material nearby"],
    ["साल भर मीठे पानी और मछली प्रदान करने वाली गोखुर झीलें", "छोटे शिकार और पौधों के खाद्य पदार्थ प्रदान करने वाले घने मानसून जंगल", "मौसमी जंगली पौधों के संसाधनों के साथ नदी की बाढ़ के मैदान", "पास में पत्थर कच्चे माल प्रदान करने वाले हिमालयी हिमनद"],
    [0, 1, 2],
    "Oxbow lakes, monsoon forests, and river floodplains all supported Ganga valley Mesolithic life. Himalayan glaciers were not a stone raw material source for these sites.",
    "गोखुर झीलें, मानसून जंगल और नदी बाढ़ के मैदान सभी ने गंगा घाटी मध्यपाषाणकालीन जीवन का समर्थन किया।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are zooarchaeological indicators of animal domestication? (Select all that apply)",
    "निम्नलिखित में से कौन से पशुपालन के पशु-पुरातात्विक संकेतक हैं? (सभी सही विकल्प चुनें)",
    ["Selective culling of young males while females are preserved", "Smaller body size of bones compared to wild ancestors", "Presence of herding species (cattle/sheep/goat) in high proportion", "Finding of ploughed field marks in associated soil layers"],
    ["मादाओं को संरक्षित करते हुए युवा नरों का चयनात्मक वध", "जंगली पूर्वजों की तुलना में हड्डियों का छोटा आकार", "उच्च अनुपात में पशुपालन प्रजातियों (मवेशी/भेड़/बकरी) की उपस्थिति", "संबंधित मिट्टी की परतों में जुते हुए खेत के निशान मिलना"],
    [0, 1, 2],
    "The first three are zooarchaeological indicators. Ploughed field marks are agricultural Neolithic evidence, not pastoralism evidence.",
    "पहले तीन पशु-पुरातात्विक संकेतक हैं। जुते हुए खेत के निशान कृषि नवपाषाणकालीन साक्ष्य हैं, पशुपालन साक्ष्य नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are correct about the chronology of Bagor (Rajasthan)? (Select all that apply)",
    "निम्नलिखित में से कौन से बागोर (राजस्थान) के कालक्रम के बारे में सही हैं? (सभी सही विकल्प चुनें)",
    ["Phase I shows microliths and animal domestication (c. 5000 BCE)", "Phase II shows coexistence of microliths with early copper tools", "Phase III shows contact with early historical material culture", "All three phases show identical cultural assemblages with no progression"],
    ["प्रथम चरण सूक्ष्म पाषाण और पशुपालन दिखाता है (लगभग 5000 ईसा पूर्व)", "द्वितीय चरण प्रारंभिक तांबे के उपकरणों के साथ सूक्ष्म पाषाणों का सह-अस्तित्व दिखाता है", "तृतीय चरण प्रारंभिक ऐतिहासिक भौतिक संस्कृति के साथ संपर्क दिखाता है", "सभी तीन चरण बिना किसी प्रगति के समान सांस्कृतिक समूह दिखाते हैं"],
    [0, 1, 2],
    "The first three statements correctly describe Bagor's three-phase cultural sequence. Each phase shows progressive cultural change.",
    "पहले तीन कथन बागोर के तीन-चरण सांस्कृतिक अनुक्रम का सही वर्णन करते हैं। प्रत्येक चरण प्रगतिशील सांस्कृतिक परिवर्तन दिखाता है।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are depicted in Bhimbetka Mesolithic rock paintings? (Select all that apply)",
    "निम्नलिखित में से कौन से भीमबेटका मध्यपाषाणकालीन शैल चित्रों में दर्शाए गए हैं? (सभी सही विकल्प चुनें)",
    ["Hunting scenes with bows and arrows", "Honey-gathering from beehives in trees", "Communal dancing figures", "Irrigation canals and paddy fields"],
    ["धनुष और तीर के साथ शिकार के दृश्य", "पेड़ों में छत्तों से शहद इकट्ठा करना", "सामुदायिक नृत्य आकृतियाँ", "सिंचाई नहरें और धान के खेत"],
    [0, 1, 2],
    "Hunting, honey gathering, and dancing are all depicted. Irrigation and paddy fields belong to the agricultural Neolithic, not the Mesolithic.",
    "शिकार, शहद इकट्ठा करना और नृत्य सभी दर्शाए गए हैं। सिंचाई और धान के खेत कृषि नवपाषाण काल के हैं, मध्यपाषाण के नहीं।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following correctly match a Mesolithic site with a distinctive finding? (Select all that apply)",
    "निम्नलिखित में से कौन से एक मध्यपाषाणकालीन स्थल को एक विशिष्ट खोज के साथ सही ढंग से सुमेलित करते हैं? (सभी सही विकल्प चुनें)",
    ["Sarai Nahar Rai : Skeleton with embedded arrowhead (earliest interpersonal conflict)", "Bhimbetka : Largest Mesolithic burial ground in India", "Bagor : Three-phase stratigraphy showing Mesolithic to historical transition", "Damdama : 41 human burials including triple burials"],
    ["सराय नाहर राय : धँसी तीर नोक वाला कंकाल (सबसे पहला व्यक्तिगत संघर्ष)", "भीमबेटका : भारत में सबसे बड़ा मध्यपाषाणकालीन शवाधान स्थल", "बागोर : मध्यपाषाण से ऐतिहासिक संक्रमण दिखाने वाला तीन-चरण स्तरविन्यास", "दमदमा : तिहरी कब्रों सहित 41 मानव कब्रें"],
    [0, 2, 3],
    "Options 1, 3, and 4 are correctly matched. Option 2 is incorrect — Bhimbetka is a rock art site, not a burial ground. Damdama has the largest burial count.",
    "विकल्प 1, 3 और 4 सही ढंग से सुमेलित हैं। विकल्प 2 गलत है — भीमबेटका एक शैल कला स्थल है, शवाधान स्थल नहीं। दमदमा में सबसे अधिक शवाधान संख्या है।"
)

add_multi_mcq(practice_en, practice_hi,
    "Which of the following are true about the ecological context of the transition from Paleolithic to Mesolithic? (Select all that apply)",
    "निम्नलिखित में से कौन से पुरापाषाण से मध्यपाषाण काल में संक्रमण के पारिस्थितिक संदर्भ के बारे में सही हैं? (सभी सही विकल्प चुनें)",
    ["Megafauna (large animals) like mammoths became extinct due to climate change and hunting pressure", "Warmer, wetter climate created new forests and diverse ecological niches", "Decline of large game forced adaptation to smaller, more varied food sources", "Sea levels fell by 120 metres, exposing large tracts of land"],
    ["जलवायु परिवर्तन और शिकार के दबाव से मैमथ जैसे विशाल जीव (बड़े जानवर) विलुप्त हो गए", "गर्म, अधिक आर्द्र जलवायु ने नए जंगल और विविध पारिस्थितिक आले बनाए", "बड़े शिकार की गिरावट ने छोटे, अधिक विविध खाद्य स्रोतों के अनुकूलन को मजबूर किया", "समुद्र का स्तर 120 मीटर गिर गया, जिससे भूमि के बड़े हिस्से उजागर हुए"],
    [0, 1, 2],
    "The first three are correct. Sea level RISE (not fall) occurred during post-glacial warming — the glaciers melted, raising sea levels.",
    "पहले तीन सही हैं। हिमयुगोत्तर ताप के दौरान समुद्र का स्तर बढ़ा (गिरा नहीं) — हिमनद पिघले, समुद्र का स्तर बढ़ा।"
)

# --- Statement-Based (10) ---
add_stmt(practice_en, practice_hi,
    "Consider the following statements about Mesolithic microliths:\n1. They are smaller and more specialised than Paleolithic tools.\n2. They were made exclusively of polished granite.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन सूक्ष्म पाषाणों के बारे में निम्नलिखित कथनों पर विचार करें:\n1. वे पुरापाषाणकालीन उपकरणों की तुलना में छोटे और अधिक विशेष हैं।\n2. वे विशेष रूप से पॉलिश किए गए ग्रेनाइट से बने थे।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — microliths were made from chert, chalcedony, and other fine-grained siliceous stones, not polished granite.",
    "कथन 1 सही है। कथन 2 गलत है — सूक्ष्म पाषाण चर्ट, चाल्सीडोनी और अन्य बारीक दाने वाले सिलिशियस पत्थरों से बने थे, पॉलिश किए गए ग्रेनाइट से नहीं।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about the Mesolithic climate:\n1. The Mesolithic period began with the end of the Last Glacial Maximum.\n2. Warming climate led to the extinction of megafauna and growth of dense forests.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन जलवायु के बारे में निम्नलिखित कथनों पर विचार करें:\n1. मध्यपाषाण काल अंतिम हिमाच्छादन अधिकतम के अंत के साथ शुरू हुआ।\n2. ताप जलवायु ने विशाल जीवों के विलोपन और घने जंगलों के विकास की ओर ले जाया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. The Holocene warming drove both megafauna extinction and new ecological zones.",
    "दोनों कथन सही हैं। होलोसीन ताप ने विशाल जीव विलोपन और नए पारिस्थितिक क्षेत्र दोनों को प्रेरित किया।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about Bhimbetka:\n1. It was discovered by V.S. Wakankar in 1957-58.\n2. It contains rock paintings exclusively from the Mesolithic period.\nWhich of the statements given above is/are correct?",
    "भीमबेटका के बारे में निम्नलिखित कथनों पर विचार करें:\n1. इसकी खोज 1957-58 में वी.एस. वाकणकर ने की थी।\n2. इसमें विशेष रूप से मध्यपाषाण काल की शैल चित्रकारी है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — Bhimbetka has paintings from Paleolithic through to historical periods, not exclusively Mesolithic.",
    "कथन 1 सही है। कथन 2 गलत है — भीमबेटका में पुरापाषाण से ऐतिहासिक काल तक की चित्रकारी है, केवल मध्यपाषाणकालीन नहीं।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following pairs of sites and their locations:\n1. Bagor : Kothari River, Rajasthan\n2. Langhnaj : Narmada River basin, Gujarat\n3. Damdama : Pratapgarh district, Uttar Pradesh\nHow many pairs are correctly matched?",
    "स्थलों और उनके स्थानों के निम्नलिखित युग्मों पर विचार करें:\n1. बागोर : कोठारी नदी, राजस्थान\n2. लांघनाज : नर्मदा नदी बेसिन, गुजरात\n3. दमदमा : प्रतापगढ़ जिला, उत्तर प्रदेश\nकितने युग्म सही सुमेलित हैं?",
    ["Only one", "Only two", "All three", "None"],
    ["केवल एक", "केवल दो", "सभी तीन", "कोई नहीं"],
    1,
    "Pairs 1 and 3 are correct. Pair 2 is incorrect — Langhnaj is in the Sabarmati basin, not the Narmada basin.",
    "युग्म 1 और 3 सही हैं। युग्म 2 गलत है — लांघनाज साबरमती बेसिन में है, नर्मदा बेसिन में नहीं।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about Mesolithic burials:\n1. Grave goods indicate belief in an afterlife.\n2. All Mesolithic graves were identical, showing no social differentiation.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन शवाधान के बारे में निम्नलिखित कथनों पर विचार करें:\n1. कब्र के सामान परलोक में विश्वास को इंगित करते हैं।\n2. सभी मध्यपाषाणकालीन कब्रें समान थीं, जो कोई सामाजिक भेद नहीं दिखाती थीं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — graves varied in richness of grave goods, indicating social differentiation.",
    "कथन 1 सही है। कथन 2 गलत है — कब्रें कब्र के सामान की समृद्धि में भिन्न थीं, जो सामाजिक भेद को इंगित करती हैं।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about animal domestication in India:\n1. The earliest evidence comes from Bagor and Adamgarh, predating the Neolithic phase.\n2. The Mesolithic communities fully abandoned hunting once they began herding animals.\nWhich of the statements given above is/are correct?",
    "भारत में पशुपालन के बारे में निम्नलिखित कथनों पर विचार करें:\n1. सबसे पहला साक्ष्य बागोर और आदमगढ़ से आता है, जो नवपाषाण चरण से पहले है।\n2. मध्यपाषाणकालीन समुदायों ने पशुपालन शुरू करने के बाद शिकार पूरी तरह से छोड़ दिया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — pastoralism supplemented, not replaced, hunting and gathering in the Mesolithic economy.",
    "कथन 1 सही है। कथन 2 गलत है — पशुपालन ने मध्यपाषाणकालीन अर्थव्यवस्था में शिकार और संग्रहण को पूरक बनाया, प्रतिस्थापित नहीं किया।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following pairs:\nTool type : Mesolithic period characteristic\n1. Lunate : Geometric microlith used as arrowhead or blade insert\n2. Handaxe : Iconic Mesolithic tool made by unifacial flaking\n3. Trapeze : Geometric microlith used as transverse arrowhead\nHow many pairs are correctly matched?",
    "निम्नलिखित युग्मों पर विचार करें:\nउपकरण प्रकार : मध्यपाषाण काल की विशेषता\n1. लूनेट : तीर की नोक या ब्लेड इन्सर्ट के रूप में उपयोग किया जाने वाला ज्यामितीय सूक्ष्म पाषाण\n2. हैंड एक्स : एकपक्षीय फ्लेकिंग से बना प्रतिष्ठित मध्यपाषाणकालीन उपकरण\n3. ट्रेपेज़ : अनुप्रस्थ तीर की नोक के रूप में उपयोग किया जाने वाला ज्यामितीय सूक्ष्म पाषाण\nकितने युग्म सही सुमेलित हैं?",
    ["Only one", "Only two", "All three", "None"],
    ["केवल एक", "केवल दो", "सभी तीन", "कोई नहीं"],
    1,
    "Pairs 1 and 3 are correct. Pair 2 is incorrect — handaxes are Paleolithic (Acheulean) tools, not Mesolithic.",
    "युग्म 1 और 3 सही हैं। युग्म 2 गलत है — हैंड एक्स पुरापाषाणकालीन (एशुलियन) उपकरण हैं, मध्यपाषाणकालीन नहीं।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about the Mesolithic burial at Sarai Nahar Rai:\n1. It is the earliest Mesolithic site in the Ganga plains.\n2. A skeleton found here has a microlithic arrowhead embedded in its pelvic bone.\nWhich of the statements given above is/are correct?",
    "सराय नाहर राय में मध्यपाषाणकालीन शवाधान के बारे में निम्नलिखित कथनों पर विचार करें:\n1. यह गंगा के मैदानों में सबसे प्रारंभिक मध्यपाषाणकालीन स्थल है।\n2. यहाँ मिले एक कंकाल के कूल्हे की हड्डी में एक सूक्ष्म पाषाण तीर की नोक धँसी है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Sarai Nahar Rai is the earliest Ganga plain Mesolithic site and has the conflict skeleton.",
    "दोनों कथन सही हैं। सराय नाहर राय गंगा के मैदान का सबसे प्रारंभिक मध्यपाषाणकालीन स्थल है और इसमें संघर्ष कंकाल है।"
)

add_stmt(practice_en, practice_hi,
    "With reference to the Bhimbetka rock art, consider the following statements:\n1. The dominant colour used was red haematite (iron oxide).\n2. The paintings depict exclusively animal figures with no human forms.\nWhich of the statements given above is/are correct?",
    "भीमबेटका शैल कला के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. उपयोग किया गया प्रमुख रंग लाल हेमेटाइट (आयरन ऑक्साइड) था।\n2. चित्रकारी विशेष रूप से जानवरों की आकृतियाँ दर्शाती है जिसमें कोई मानव रूप नहीं है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — Bhimbetka has numerous human figures (hunters, dancers, honey gatherers).",
    "कथन 1 सही है। कथन 2 गलत है — भीमबेटका में कई मानव आकृतियाँ हैं (शिकारी, नृत्यकर्ता, शहद इकट्ठा करने वाले)।"
)

add_stmt(practice_en, practice_hi,
    "Consider the following statements about the Mesolithic economy:\n1. Wild rice was gathered but not cultivated during the Mesolithic.\n2. Animal domestication at Bagor predates the main Neolithic agricultural phase in India.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन अर्थव्यवस्था के बारे में निम्नलिखित कथनों पर विचार करें:\n1. मध्यपाषाण काल के दौरान जंगली चावल इकट्ठा किया जाता था लेकिन उसकी खेती नहीं की जाती थी।\n2. बागोर में पशुपालन भारत में मुख्य नवपाषाणकालीन कृषि चरण से पहले है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Gathering (not cultivation) of wild rice and Mesolithic pastoralism are well-documented.",
    "दोनों कथन सही हैं। जंगली चावल का संग्रह (खेती नहीं) और मध्यपाषाणकालीन पशुपालन अच्छी तरह से दस्तावेजीकृत हैं।"
)

# --- Assertion-Reason (10) ---
add_ar(practice_en, practice_hi,
    "Assertion (A): Microliths replaced large Paleolithic tools during the Mesolithic period.\nReason (R): The extinction of large game and shift to smaller prey made smaller, more precise tools advantageous.",
    "कथन (A): मध्यपाषाण काल के दौरान सूक्ष्म पाषाणों ने बड़े पुरापाषाणकालीन उपकरणों को प्रतिस्थापित किया।\nकारण (R): बड़े शिकार के विलुप्त होने और छोटे शिकार की ओर बदलाव ने छोटे, अधिक सटीक उपकरणों को फायदेमंद बनाया।",
    0,
    "Both A and R are true, and R is the correct ecological explanation for microlith adoption.",
    "A और R दोनों सही हैं, और R सूक्ष्म पाषाण अपनाने की सही पारिस्थितिक व्याख्या है।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): Mesolithic communities lived as fully sedentary farmers in permanent villages.\nReason (R): The development of microliths enabled large-scale grain cultivation.",
    "कथन (A): मध्यपाषाणकालीन समुदाय स्थायी गाँवों में पूरी तरह से स्थायी किसानों के रूप में रहते थे।\nकारण (R): सूक्ष्म पाषाणों के विकास ने बड़े पैमाने पर अनाज की खेती को सक्षम किया।",
    3,
    "Both A and R are false. Mesolithic groups were semi-nomadic forager-pastoralists, not sedentary farmers. Microliths were hunting/gathering tools, not farming tools.",
    "A और R दोनों गलत हैं। मध्यपाषाणकालीन समूह अर्ध-घुमंतू भोजन संग्रहकर्ता-पशुपालक थे, स्थायी किसान नहीं। सूक्ष्म पाषाण शिकार/संग्रह उपकरण थे, कृषि उपकरण नहीं।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): Bagor in Rajasthan provides evidence of early animal domestication predating the Neolithic phase.\nReason (R): Phase I of Bagor shows selective culling of cattle, sheep, and goats, indicating controlled herding by c. 5000 BCE.",
    "कथन (A): राजस्थान में बागोर नवपाषाण चरण से पहले प्रारंभिक पशुपालन का साक्ष्य प्रदान करता है।\nकारण (R): बागोर का प्रथम चरण मवेशियों, भेड़ों और बकरियों का चयनात्मक वध दिखाता है, जो लगभग 5000 ईसा पूर्व तक नियंत्रित पशुपालन को इंगित करता है।",
    0,
    "Both A and R are true, and R is the direct archaeological evidence supporting A.",
    "A और R दोनों सही हैं, और R A का समर्थन करने वाला प्रत्यक्ष पुरातात्विक साक्ष्य है।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): Bhimbetka's rock art has survived for thousands of years due to the protective overhang of sandstone shelters.\nReason (R): The haematite pigment is chemically unstable and would not have survived without shelter.",
    "कथन (A): भीमबेटका की शैल कला बलुआ पत्थर के आश्रयों के सुरक्षात्मक ओवरहैंग के कारण हजारों वर्षों तक जीवित रही है।\nकारण (R): हेमेटाइट रंगद्रव्य रासायनिक रूप से अस्थिर है और आश्रय के बिना नहीं बचता।",
    2,
    "A is true — the overhang did protect the art. R is false — haematite (iron oxide) is chemically STABLE, not unstable. Both the shelter AND pigment stability contribute to preservation.",
    "A सही है — ओवरहैंग ने कला की रक्षा की। R गलत है — हेमेटाइट (आयरन ऑक्साइड) रासायनिक रूप से स्थिर है, अस्थिर नहीं। आश्रय और रंगद्रव्य स्थिरता दोनों संरक्षण में योगदान करते हैं।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): The Mesolithic period is associated with the rise of composite tools where microliths were combined with organic handles.\nReason (R): Composite tools allowed greater functional versatility and efficiency in hunting and food processing.",
    "कथन (A): मध्यपाषाण काल संयुक्त उपकरणों के उदय से जुड़ा है जहाँ सूक्ष्म पाषाणों को जैविक हैंडल के साथ जोड़ा गया था।\nकारण (R): संयुक्त उपकरणों ने शिकार और खाद्य प्रसंस्करण में अधिक कार्यात्मक बहुमुखी प्रतिभा और दक्षता की अनुमति दी।",
    0,
    "Both A and R are true. The functional efficiency of composite tools is what drove their widespread adoption.",
    "A और R दोनों सही हैं। संयुक्त उपकरणों की कार्यात्मक दक्षता ही उनके व्यापक अपनाने का कारण थी।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): Damdama in Uttar Pradesh has the highest number of Mesolithic burials in India.\nReason (R): The oxbow lake ecology of the Ganga plains provided stable resources that encouraged repeated use of the same camps across generations.",
    "कथन (A): उत्तर प्रदेश में दमदमा में भारत में सबसे अधिक मध्यपाषाणकालीन शवाधान हैं।\nकारण (R): गंगा के मैदानों की गोखुर झील पारिस्थितिकी ने स्थिर संसाधन प्रदान किए जिसने पीढ़ियों तक एक ही शिविरों के बार-बार उपयोग को प्रोत्साहित किया।",
    0,
    "Both A and R are true. Ecological stability drove repeated occupation, building up burial density over centuries.",
    "A और R दोनों सही हैं। पारिस्थितिक स्थिरता ने बार-बार बस्ती को प्रेरित किया, सदियों में शवाधान घनत्व का निर्माण किया।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): The Mesolithic period in India is characterised by geometric microliths as the defining tool technology.\nReason (R): Microliths provided greater precision and efficiency in hunting smaller post-glacial fauna compared to large Paleolithic tools.",
    "कथन (A): भारत में मध्यपाषाण काल परिभाषित उपकरण प्रौद्योगिकी के रूप में ज्यामितीय सूक्ष्म पाषाणों द्वारा चित्रित है।\nकारण (R): बड़े पुरापाषाणकालीन उपकरणों की तुलना में सूक्ष्म पाषाणों ने हिमयुगोत्तर छोटे जीवों के शिकार में अधिक सटीकता और दक्षता प्रदान की।",
    0,
    "Both A and R are true, and R provides the adaptive reason for the microlith revolution.",
    "A और R दोनों सही हैं, और R सूक्ष्म पाषाण क्रांति के अनुकूल कारण को प्रदान करता है।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): The honey-gathering scene at Bhimbetka proves that Mesolithic communities practised systematic bee-keeping (apiculture).\nReason (R): Organised bee-keeping requires permanent settlements and does not fit a mobile hunter-gatherer lifestyle.",
    "कथन (A): भीमबेटका में शहद इकट्ठा करने का दृश्य साबित करता है कि मध्यपाषाणकालीन समुदायों ने व्यवस्थित मधुमक्खी पालन (एपिकल्चर) का अभ्यास किया।\nकारण (R): संगठित मधुमक्खी पालन के लिए स्थायी बस्तियों की आवश्यकता होती है और यह एक गतिशील शिकारी-संग्रहकर्ता जीवन शैली के अनुकूल नहीं है।",
    2,
    "A is false — the scene shows opportunistic wild honey gathering, NOT systematic bee-keeping (apiculture). R is true — bee-keeping requires sedentism incompatible with Mesolithic mobility.",
    "A गलत है — दृश्य अवसरवादी जंगली शहद इकट्ठा करना दिखाता है, व्यवस्थित मधुमक्खी पालन (एपिकल्चर) नहीं। R सही है — मधुमक्खी पालन के लिए स्थायित्व की आवश्यकता होती है जो मध्यपाषाणकालीन गतिशीलता के साथ असंगत है।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): V.S. Wakankar's discovery of Bhimbetka proved that prehistoric India had a sophisticated artistic tradition comparable to European Paleolithic cave art.\nReason (R): Before Bhimbetka's discovery, archaeologists had no evidence of prehistoric rock art anywhere in Asia.",
    "कथन (A): वी.एस. वाकणकर की भीमबेटका की खोज ने साबित किया कि प्रागैतिहासिक भारत में यूरोपीय पुरापाषाणकालीन गुफा कला के बराबर एक परिष्कृत कलात्मक परंपरा थी।\nकारण (R): भीमबेटका की खोज से पहले, पुरातत्वविदों के पास एशिया में कहीं भी प्रागैतिहासिक शैल कला का कोई साक्ष्य नहीं था।",
    2,
    "A is true — Bhimbetka established India's prehistoric artistic sophistication. R is false — prehistoric rock art was already known in other parts of Asia (e.g., Altamira in Europe, cave art in Borneo).",
    "A सही है — भीमबेटका ने भारत की प्रागैतिहासिक कलात्मक परिष्कार को स्थापित किया। R गलत है — प्रागैतिहासिक शैल कला पहले से ही एशिया के अन्य हिस्सों में ज्ञात थी।"
)

add_ar(practice_en, practice_hi,
    "Assertion (A): The broad-spectrum foraging strategy of the Mesolithic provided greater food security than exclusive large-game hunting.\nReason (R): Multiple food sources ensure that seasonal failure of any single resource does not lead to starvation.",
    "कथन (A): मध्यपाषाण काल की व्यापक-स्पेक्ट्रम भोजन संग्रह रणनीति ने विशेष बड़े-शिकार शिकार की तुलना में अधिक खाद्य सुरक्षा प्रदान की।\nकारण (R): कई खाद्य स्रोत यह सुनिश्चित करते हैं कि किसी एकल संसाधन की मौसमी विफलता भुखमरी की ओर नहीं ले जाती।",
    0,
    "Both A and R are true, and R is the correct adaptive explanation for the broad-spectrum strategy.",
    "A और R दोनों सही हैं, और R व्यापक-स्पेक्ट्रम रणनीति की सही अनुकूल व्याख्या है।"
)
