from .helpers import add_mcq, add_multi_mcq, add_tf, add_blank, add_match, add_oneliner, add_ar, add_stmt, add_open

sec3_en = []
sec3_hi = []

# --- 1. MCQ (5 Questions) ---
add_mcq(sec3_en, sec3_hi,
    "Which site is considered the largest Mesolithic site in India?",
    "निम्नलिखित में से कौन सा स्थल भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल माना जाता है?",
    ["Langhnaj", "Bagor", "Sarai Nahar Rai", "Adamgarh"],
    ["लांघनाज", "बागोर", "सराय नाहर राय", "आदमगढ़"],
    1,
    "Bagor on the Kothari River in Rajasthan is the largest Mesolithic site in India, spanning over 2500 square metres with a thick cultural deposit.",
    "राजस्थान में कोठारी नदी पर स्थित बागोर भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है, जो 2500 वर्ग मीटर से अधिक क्षेत्रफल में फैला हुआ है।"
)

add_mcq(sec3_en, sec3_hi,
    "H.D. Sankalia excavated which major sand-dune Mesolithic site in Gujarat?",
    "एच.डी. सांकलिया ने गुजरात के किस प्रमुख रेत के टीले वाले मध्यपाषाणकालीन स्थल का उत्खनन किया था?",
    ["Bagor", "Langhnaj", "Mahadaha", "Adamgarh"],
    ["बागोर", "लांघनाज", "महदहा", "आदमगढ़"],
    1,
    "H.D. Sankalia of Deccan College excavated the Langhnaj dune site in the Sabarmati River basin of Gujarat.",
    "डेक्कन कॉलेज के एच.डी. सांकलिया ने गुजरात में साबरमती नदी बेसिन में लांघनाज रेत के टीले के स्थल का उत्खनन किया था।"
)

add_mcq(sec3_en, sec3_hi,
    "Sarai Nahar Rai, the earliest known Mesolithic site in the Ganga plains, is located in which state?",
    "सराय नाहर राय, गंगा के मैदानों में सबसे प्रारंभिक ज्ञात मध्यपाषाणकालीन स्थल, किस राज्य में स्थित है?",
    ["Bihar", "Madhya Pradesh", "Uttar Pradesh", "Rajasthan"],
    ["बिहार", "मध्य प्रदेश", "उत्तर प्रदेश", "राजस्थान"],
    2,
    "Sarai Nahar Rai is located in Pratapgarh district, Uttar Pradesh, on the banks of a tributary of the Sai River.",
    "सराय नाहर राय उत्तर प्रदेश के प्रतापगढ़ जिले में साई नदी की एक सहायक नदी के किनारे स्थित है।"
)

add_mcq(sec3_en, sec3_hi,
    "The Mesolithic site of Damdama in Uttar Pradesh is famous for yielding the largest number of human burials at any single site. Approximately how many burials were found?",
    "उत्तर प्रदेश में मध्यपाषाणकालीन स्थल दमदमा किसी एकल स्थल पर सबसे अधिक मानव कब्रों के लिए प्रसिद्ध है। वहाँ लगभग कितनी कब्रें मिली थीं?",
    ["10", "41", "120", "5"],
    ["10", "41", "120", "5"],
    1,
    "Damdama yielded 41 human burials, including triple burials, making it the richest burial site in Indian prehistory.",
    "दमदमा से 41 मानव कब्रें मिली हैं, जिनमें तिहरी कब्र (triple burials) भी शामिल हैं, जो इसे भारतीय प्रागैतिहास में सबसे समृद्ध शवाधान स्थल बनाती हैं।"
)

add_mcq(sec3_en, sec3_hi,
    "Adamgarh in Madhya Pradesh is located near which major Indian river?",
    "मध्य प्रदेश में आदमगढ़ किस प्रमुख भारतीय नदी के पास स्थित है?",
    ["Godavari River", "Narmada River", "Tapti River", "Chambal River"],
    ["गोदावरी नदी", "नर्मदा नदी", "तापी नदी", "चंबल नदी"],
    1,
    "Adamgarh is situated in Hoshangabad district near the Narmada River in Madhya Pradesh.",
    "आदमगढ़ मध्य प्रदेश में नर्मदा नदी के पास होशंगाबाद जिले में स्थित है।"
)

# --- 2. Multiple Correct MCQ (5 Questions) ---
add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following are Mesolithic sites located in the Ganga River plains of Uttar Pradesh? (Select all that apply)",
    "निम्नलिखित में से कौन से मध्यपाषाणकालीन स्थल उत्तर प्रदेश के गंगा नदी मैदानों में स्थित हैं? (सभी सही विकल्प चुनें)",
    ["Sarai Nahar Rai", "Mahadaha", "Damdama", "Langhnaj"],
    ["सराय नाहर राय", "महदहा", "दमदमा", "लांघनाज"],
    [0, 1, 2],
    "Sarai Nahar Rai, Mahadaha, and Damdama are all in Pratapgarh district, UP. Langhnaj is in Gujarat.",
    "सराय नाहर राय, महदहा और दमदमा सभी उत्तर प्रदेश के प्रतापगढ़ जिले में हैं। लांघनाज गुजरात में है।"
)

add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following correctly describe the Mesolithic site of Bagor in Rajasthan? (Select all that apply)",
    "निम्नलिखित में से कौन से राजस्थान में मध्यपाषाणकालीन स्थल बागोर का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Located on the Kothari River", "Largest Mesolithic site in India", "Yields evidence of early animal domestication", "Located in the Sabarmati River basin"],
    ["कोठारी नदी पर स्थित", "भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल", "प्रारंभिक पशुपालन का साक्ष्य देता है", "साबरमती नदी बेसिन में स्थित"],
    [0, 1, 2],
    "Bagor is on the Kothari River, is the largest Mesolithic site in India, and shows animal domestication. It is not in the Sabarmati basin (that is Langhnaj).",
    "बागोर कोठारी नदी पर है, भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है, और पशुपालन के साक्ष्य दिखाता है। यह साबरमती बेसिन में नहीं है (वह लांघनाज है)।"
)

add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following correctly describe the Mesolithic burials at Mahadaha (Uttar Pradesh)? (Select all that apply)",
    "निम्नलिखित में से कौन से उत्तर प्रदेश के महदहा में मध्यपाषाणकालीन शवाधान का सही वर्णन करते हैं? (सभी सही विकल्प चुनें)",
    ["Double burials were found", "Bone ornaments (necklaces) were grave goods", "Bodies were cremated with ashes", "Fire pits were associated with the graves"],
    ["दोहरी कब्रें मिली थीं", "हड्डी के आभूषण (हार) कब्र का सामान थे", "शवों को राख के साथ जलाया जाता था", "कब्रों के पास चूल्हे थे"],
    [0, 1, 3],
    "Mahadaha shows double burials, bone ornaments as grave goods, and fire pits. There is no evidence of cremation; bodies were directly inhumed.",
    "महदहा में दोहरी कब्रें, हड्डी के आभूषण कब्र के सामान के रूप में, और चूल्हे दिखाई देते हैं। दाह-संस्कार का कोई सबूत नहीं है; शवों को सीधे दफनाया जाता था।"
)

add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following features make Sarai Nahar Rai historically significant? (Select all that apply)",
    "निम्नलिखित में से कौन सी विशेषताएं सराय नाहर राय को ऐतिहासिक रूप से महत्वपूर्ण बनाती हैं? (सभी सही विकल्प चुनें)",
    ["Earliest Mesolithic site in the Ganga plains", "Evidence of a skeleton with embedded arrow-point", "Contains 41 systematic human burials", "Hearths associated with human occupation"],
    ["गंगा के मैदानों में सबसे प्रारंभिक मध्यपाषाणकालीन स्थल", "एक कंकाल में धँसी तीर की नोक का साक्ष्य", "41 व्यवस्थित मानव कब्रें", "मानव बस्ती से जुड़े चूल्हे"],
    [0, 1, 3],
    "Sarai Nahar Rai is the earliest Ganga plain site, shows the conflict skeleton, and has hearths. The 41 burials belong to Damdama, not Sarai Nahar Rai.",
    "सराय नाहर राय सबसे प्रारंभिक गंगा मैदान स्थल है, संघर्ष कंकाल दिखाता है, और चूल्हे हैं। 41 कब्रें दमदमा की हैं, सराय नाहर राय की नहीं।"
)

add_multi_mcq(sec3_en, sec3_hi,
    "Which of the following descriptions correctly characterise the Mesolithic rock shelter site of Adamgarh (MP)? (Select all that apply)",
    "निम्नलिखित में से कौन से विवरण मध्य प्रदेश के मध्यपाषाणकालीन शैल आश्रय स्थल आदमगढ़ की सही विशेषताएं बताते हैं? (सभी सही विकल्प चुनें)",
    ["Located in rock shelters near the Narmada", "Contains rich assemblages of microliths", "Yields earliest evidence of animal domestication in the rock shelter context", "Located in sand dunes near the Sabarmati"],
    ["नर्मदा के पास शैल आश्रयों में स्थित", "सूक्ष्म पाषाणों का समृद्ध भंडार है", "शैल आश्रय संदर्भ में पशुपालन का सबसे प्रारंभिक प्रमाण है", "साबरमती के पास रेत के टीलों में स्थित"],
    [0, 1, 2],
    "Adamgarh is in Narmada valley rock shelters with microliths and animal domestication evidence. It is not on sand dunes or the Sabarmati.",
    "आदमगढ़ नर्मदा घाटी के शैल आश्रयों में है जहाँ सूक्ष्म पाषाण और पशुपालन के साक्ष्य हैं। यह रेत के टीलों या साबरमती पर नहीं है।"
)

# --- 3. True/False (8 Questions) ---
add_tf(sec3_en, sec3_hi,
    "Bagor is the largest Mesolithic site in India, located on the Kothari River in Rajasthan.",
    "बागोर भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है, जो राजस्थान में कोठारी नदी पर स्थित है।",
    True,
    "Bagor on the Kothari River is indeed the largest single Mesolithic site documented in India.",
    "कोठारी नदी पर बागोर वास्तव में भारत में दस्तावेजीकृत सबसे बड़ा एकल मध्यपाषाणकालीन स्थल है।"
)

add_tf(sec3_en, sec3_hi,
    "Langhnaj is situated on a sand dune in the Narmada River basin of Gujarat.",
    "लांघनाज गुजरात में नर्मदा नदी बेसिन में एक रेत के टीले पर स्थित है।",
    False,
    "Langhnaj is in the Sabarmati River basin, not the Narmada basin.",
    "लांघनाज नर्मदा बेसिन में नहीं, बल्कि साबरमती नदी बेसिन में है।"
)

add_tf(sec3_en, sec3_hi,
    "Damdama in Uttar Pradesh yielded 41 human burials, including triple burials.",
    "उत्तर प्रदेश में दमदमा से 41 मानव कब्रें मिली हैं, जिनमें तिहरी (triple) कब्रें भी शामिल हैं।",
    True,
    "Damdama has the highest number of Mesolithic burials in India, including some rare triple burials.",
    "भारत में मध्यपाषाणकालीन कब्रों की सबसे अधिक संख्या दमदमा में है, जिसमें कुछ दुर्लभ तिहरी कब्रें भी शामिल हैं।"
)

add_tf(sec3_en, sec3_hi,
    "A skeleton at Sarai Nahar Rai shows evidence of being killed by a microlithic arrowhead embedded in its pelvic bone.",
    "सराय नाहर राय में एक कंकाल के पेल्विक बोन (कूल्हे की हड्डी) में धँसी सूक्ष्म पाषाण तीर की नोक का साक्ष्य मिलता है।",
    True,
    "This is the earliest evidence of interpersonal conflict/warfare in prehistoric India.",
    "यह प्रागैतिहासिक भारत में व्यक्तिगत संघर्ष/युद्ध का सबसे पहला प्रमाण है।"
)

add_tf(sec3_en, sec3_hi,
    "Mahadaha is a Mesolithic site in Gujarat famous for its triple burials.",
    "महदहा गुजरात में एक मध्यपाषाणकालीन स्थल है जो अपनी तिहरी कब्रों के लिए प्रसिद्ध है।",
    False,
    "Mahadaha is in Uttar Pradesh. Damdama in UP is famous for triple burials, while Mahadaha shows double burials and bone ornaments.",
    "महदहा उत्तर प्रदेश में है। उत्तर प्रदेश में दमदमा तिहरी कब्रों के लिए प्रसिद्ध है, जबकि महदहा में दोहरी कब्रें और हड्डी के आभूषण हैं।"
)

add_tf(sec3_en, sec3_hi,
    "Langhnaj yielded human skeletons along with stone microliths and animal bones.",
    "लांघनाज से पत्थर के सूक्ष्म पाषाण और जानवरों की हड्डियों के साथ मानव कंकाल मिले हैं।",
    True,
    "Sankalia's excavation of Langhnaj revealed all three — microliths, animal bones, and human skeletal remains.",
    "लांघनाज के सांकलिया के उत्खनन में तीनों — सूक्ष्म पाषाण, जानवरों की हड्डियाँ और मानव कंकाल अवशेष — सामने आए।"
)

add_tf(sec3_en, sec3_hi,
    "Adamgarh rock shelters are located in the Eastern Ghats near Vishakhapatnam.",
    "आदमगढ़ के शैल आश्रय पूर्वी घाट में विशाखापत्तनम के पास स्थित हैं।",
    False,
    "Adamgarh is in Hoshangabad district, Madhya Pradesh, in the Central Indian highlands near the Narmada River.",
    "आदमगढ़ मध्य प्रदेश के होशंगाबाद जिले में नर्मदा नदी के पास मध्य भारतीय उच्च भूमि में स्थित है।"
)

add_tf(sec3_en, sec3_hi,
    "The Mesolithic sites of Sarai Nahar Rai, Mahadaha, and Damdama all lie in Pratapgarh district of Uttar Pradesh.",
    "सराय नाहर राय, महदहा और दमदमा के मध्यपाषाणकालीन स्थल सभी उत्तर प्रदेश के प्रतापगढ़ जिले में हैं।",
    True,
    "All three Ganga valley Mesolithic sites are clustered together in Pratapgarh district, UP.",
    "तीनों गंगा घाटी मध्यपाषाणकालीन स्थल उत्तर प्रदेश के प्रतापगढ़ जिले में एक साथ स्थित हैं।"
)

# --- 4. Fill in the Blank (8 Questions) ---
add_blank(sec3_en, sec3_hi,
    "The largest Mesolithic site in India is ________, located on the Kothari River.",
    "भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल ________ है, जो कोठारी नदी पर स्थित है।",
    "Bagor", "बागोर",
    "Bagor in Rajasthan is documented as the largest and most extensively excavated Mesolithic site.",
    "राजस्थान में बागोर को सबसे बड़े और सबसे व्यापक रूप से उत्खनित मध्यपाषाणकालीन स्थल के रूप में दर्ज किया गया है।"
)

add_blank(sec3_en, sec3_hi,
    "The sand-dune Mesolithic site of Langhnaj was excavated by ________ of Deccan College.",
    "लांघनाज के रेत के टीले वाले मध्यपाषाणकालीन स्थल का उत्खनन डेक्कन कॉलेज के ________ ने किया था।",
    "H.D. Sankalia", "एच.डी. सांकलिया",
    "H.D. Sankalia led the systematic excavation of Langhnaj, which is one of the landmark sites of Indian Mesolithic studies.",
    "एच.डी. सांकलिया ने लांघनाज के व्यवस्थित उत्खनन का नेतृत्व किया, जो भारतीय मध्यपाषाण अध्ययन के ऐतिहासिक स्थलों में से एक है।"
)

add_blank(sec3_en, sec3_hi,
    "Sarai Nahar Rai, the earliest Mesolithic site in the Ganga plains, is in ________ district.",
    "सराय नाहर राय, गंगा के मैदानों में सबसे प्रारंभिक मध्यपाषाणकालीन स्थल, ________ जिले में है।",
    "Pratapgarh", "प्रतापगढ़",
    "All three major UP Mesolithic sites — Sarai Nahar Rai, Mahadaha, and Damdama — are in Pratapgarh.",
    "तीनों प्रमुख उत्तर प्रदेश मध्यपाषाणकालीन स्थल — सराय नाहर राय, महदहा और दमदमा — प्रतापगढ़ में हैं।"
)

add_blank(sec3_en, sec3_hi,
    "The site that yielded 41 human burials including triple burials is ________.",
    "41 मानव कब्रें जिनमें तिहरी कब्रें भी शामिल हैं, वे ________ से मिली हैं।",
    "Damdama", "दमदमा",
    "Damdama has the highest number of Mesolithic burials at a single site in India.",
    "दमदमा में भारत के किसी एकल स्थल पर मध्यपाषाणकालीन कब्रों की सबसे अधिक संख्या है।"
)

add_blank(sec3_en, sec3_hi,
    "Langhnaj is located in the ________ river basin of Gujarat.",
    "लांघनाज गुजरात में ________ नदी बेसिन में स्थित है।",
    "Sabarmati", "साबरमती",
    "Langhnaj lies on the banks of a tributary within the Sabarmati River basin, north of Ahmedabad.",
    "लांघनाज अहमदाबाद के उत्तर में साबरमती नदी बेसिन के भीतर एक सहायक नदी के किनारे है।"
)

add_blank(sec3_en, sec3_hi,
    "The Mesolithic rock shelter site of Adamgarh is situated near the ________ River.",
    "आदमगढ़ का मध्यपाषाणकालीन शैल आश्रय स्थल ________ नदी के पास स्थित है।",
    "Narmada", "नर्मदा",
    "Adamgarh is in Hoshangabad district, close to the Narmada River.",
    "आदमगढ़ होशंगाबाद जिले में नर्मदा नदी के पास है।"
)

add_blank(sec3_en, sec3_hi,
    "The Mesolithic site at Mahadaha is known for ________ burials and bone ornaments.",
    "महदहा का मध्यपाषाणकालीन स्थल ________ कब्रों और हड्डी के आभूषणों के लिए जाना जाता है।",
    "double", "दोहरी",
    "Mahadaha is famous for double burials with bone necklaces placed with the dead.",
    "महदहा मृतकों के साथ रखे गए हड्डी के हारों के साथ दोहरी कब्रों के लिए प्रसिद्ध है।"
)

add_blank(sec3_en, sec3_hi,
    "The earliest evidence of interpersonal conflict in India is found at ________ where a skeleton was discovered with an arrowhead embedded in its pelvis.",
    "भारत में व्यक्तिगत संघर्ष का सबसे पहला प्रमाण ________ में मिलता है जहाँ एक कंकाल की श्रोणि में एक तीर की नोक धँसी हुई पाई गई थी।",
    "Sarai Nahar Rai", "सराय नाहर राय",
    "The embedded arrowhead in the pelvic bone at Sarai Nahar Rai is the oldest archaeological evidence of lethal conflict in India.",
    "सराय नाहर राय में कूल्हे की हड्डी में धँसी तीर की नोक भारत में घातक संघर्ष का सबसे पुराना पुरातात्विक प्रमाण है।"
)

# --- 5. Match the Following (3 Questions) ---
add_match(sec3_en, sec3_hi,
    "Match the Mesolithic site with its river/geographical location:",
    "मध्यपाषाणकालीन स्थल को उसकी नदी/भौगोलिक स्थिति से सुमेलित करें:",
    ["1. Bagor", "2. Langhnaj", "3. Adamgarh"],
    ["1. बागोर", "2. लांघनाज", "3. आदमगढ़"],
    ["A. Kothari River, Rajasthan", "B. Sabarmati basin, Gujarat", "C. Near Narmada, Madhya Pradesh"],
    ["A. कोठारी नदी, राजस्थान", "B. साबरमती बेसिन, गुजरात", "C. नर्मदा के पास, मध्य प्रदेश"],
    "1-A, 2-B, 3-C. Bagor is on the Kothari; Langhnaj is in Sabarmati basin; Adamgarh is near the Narmada.",
    "1-A, 2-B, 3-C. बागोर कोठारी पर है; लांघनाज साबरमती बेसिन में है; आदमगढ़ नर्मदा के पास है।"
)

add_match(sec3_en, sec3_hi,
    "Match the Ganga Valley site with its key archaeological finding:",
    "गंगा घाटी के स्थल को उसकी प्रमुख पुरातात्विक खोज से सुमेलित करें:",
    ["1. Sarai Nahar Rai", "2. Mahadaha", "3. Damdama"],
    ["1. सराय नाहर राय", "2. महदहा", "3. दमदमा"],
    ["A. Skeleton with embedded arrowhead (earliest conflict)", "B. Double burials with bone ornaments and fire pits", "C. 41 burials including triple burials"],
    ["A. धँसी तीर नोक वाला कंकाल (सबसे पहला संघर्ष)", "B. हड्डी के आभूषणों और चूल्हों के साथ दोहरी कब्रें", "C. तिहरी कब्रों सहित 41 कब्रें"],
    "1-A, 2-B, 3-C.",
    "1-A, 2-B, 3-C."
)

add_match(sec3_en, sec3_hi,
    "Match the scholar with their excavated Mesolithic site:",
    "विद्वान को उनके उत्खनित मध्यपाषाणकालीन स्थल से सुमेलित करें:",
    ["1. H.D. Sankalia", "2. V.N. Misra", "3. G.R. Sharma"],
    ["1. एच.डी. सांकलिया", "2. वी.एन. मिश्रा", "3. जी.आर. शर्मा"],
    ["A. Langhnaj (Gujarat)", "B. Bagor (Rajasthan)", "C. Sarai Nahar Rai, Mahadaha, Damdama (UP)"],
    ["A. लांघनाज (गुजरात)", "B. बागोर (राजस्थान)", "C. सराय नाहर राय, महदहा, दमदमा (उत्तर प्रदेश)"],
    "1-A, 2-B, 3-C. Sankalia excavated Langhnaj; V.N. Misra excavated Bagor; G.R. Sharma excavated the Ganga valley sites.",
    "1-A, 2-B, 3-C. सांकलिया ने लांघनाज, वी.एन. मिश्रा ने बागोर, और जी.आर. शर्मा ने गंगा घाटी स्थलों का उत्खनन किया।"
)

# --- 6. One-Liner (8 Questions) ---
add_oneliner(sec3_en, sec3_hi,
    "Which river does the largest Mesolithic site in India, Bagor, lie on?",
    "भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल बागोर किस नदी पर स्थित है?",
    "The Kothari River in Rajasthan.",
    "राजस्थान में कोठारी नदी पर।"
)

add_oneliner(sec3_en, sec3_hi,
    "Who excavated the sand-dune Mesolithic site of Langhnaj in Gujarat?",
    "गुजरात में लांघनाज के रेत के टीले वाले मध्यपाषाणकालीन स्थल का उत्खनन किसने किया था?",
    "H.D. Sankalia of Deccan College, Pune.",
    "पुणे के डेक्कन कॉलेज के एच.डी. सांकलिया।"
)

add_oneliner(sec3_en, sec3_hi,
    "What is the historical significance of the skeleton found at Sarai Nahar Rai?",
    "सराय नाहर राय में मिले कंकाल का ऐतिहासिक महत्व क्या है?",
    "It has a microlithic arrowhead embedded in its pelvic bone — earliest evidence of interpersonal conflict in India.",
    "इसके कूल्हे की हड्डी में एक सूक्ष्म पाषाण तीर की नोक धँसी है — यह भारत में व्यक्तिगत संघर्ष का सबसे पहला प्रमाण है।"
)

add_oneliner(sec3_en, sec3_hi,
    "How many human burials have been found at Damdama?",
    "दमदमा में कितनी मानव कब्रें मिली हैं?",
    "41 burials, including triple burials.",
    "41 कब्रें, जिनमें तिहरी कब्रें भी शामिल हैं।"
)

add_oneliner(sec3_en, sec3_hi,
    "In which state is Adamgarh, the Mesolithic rock shelter site, located?",
    "मध्यपाषाणकालीन शैल आश्रय स्थल आदमगढ़ किस राज्य में स्थित है?",
    "Madhya Pradesh (Hoshangabad district, near Narmada River).",
    "मध्य प्रदेश (होशंगाबाद जिला, नर्मदा नदी के पास)।"
)

add_oneliner(sec3_en, sec3_hi,
    "What type of ornaments were found as grave goods at Mahadaha?",
    "महदहा में कब्र के सामान (grave goods) के रूप में किस प्रकार के आभूषण मिले थे?",
    "Bone ornaments — necklaces and earrings made of bone beads.",
    "हड्डी के आभूषण — हड्डी के मोतियों से बने हार और झुमके।"
)

add_oneliner(sec3_en, sec3_hi,
    "Sarai Nahar Rai, Mahadaha, and Damdama all lie in which district of Uttar Pradesh?",
    "सराय नाहर राय, महदहा और दमदमा उत्तर प्रदेश के किस जिले में हैं?",
    "Pratapgarh district.",
    "प्रतापगढ़ जिला।"
)

add_oneliner(sec3_en, sec3_hi,
    "Which Rajasthan Mesolithic site shows distinct phases of microliths followed by early metal contact?",
    "कौन सा राजस्थान मध्यपाषाणकालीन स्थल सूक्ष्म पाषाणों के अलग-अलग चरणों और उसके बाद प्रारंभिक धातु संपर्क दिखाता है?",
    "Bagor — Phase I (microliths + animal domestication) and Phase II (copper implements appear).",
    "बागोर — प्रथम चरण (सूक्ष्म पाषाण + पशुपालन) और द्वितीय चरण (तांबे के उपकरण दिखाई देते हैं)।"
)

# --- 7. Assertion-Reason (8 Questions) ---
add_ar(sec3_en, sec3_hi,
    "Assertion (A): Bagor in Rajasthan is the largest Mesolithic site in India.\nReason (R): It is located at the confluence of the Kothari River, providing stable water supply and attracting high-density occupation.",
    "कथन (A): राजस्थान में बागोर भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है।\nकारण (R): यह कोठारी नदी के संगम पर स्थित है, जो स्थिर जल आपूर्ति और उच्च घनत्व वाली बस्ती को आकर्षित करती है।",
    0,
    "Both A and R are true, and R explains why the site became so large due to riparian resource stability.",
    "A और R दोनों सही हैं, और R स्पष्ट करता है कि नदी संसाधन स्थिरता के कारण स्थल इतना बड़ा क्यों बन गया।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): Langhnaj is situated in the Narmada River valley of Gujarat.\nReason (R): The Narmada basin provided the most favorable ecological conditions for Mesolithic occupation in Western India.",
    "कथन (A): लांघनाज गुजरात में नर्मदा नदी घाटी में स्थित है।\nकारण (R): नर्मदा बेसिन ने पश्चिमी भारत में मध्यपाषाणकालीन बस्ती के लिए सबसे अनुकूल पारिस्थितिक परिस्थितियां प्रदान कीं।",
    3,
    "A is false: Langhnaj is in the Sabarmati basin. R is false: the Sabarmati dune belt, not Narmada, supported Gujarat Mesolithic occupation.",
    "A गलत है: लांघनाज साबरमती बेसिन में है। R गलत है: साबरमती टीला बेल्ट, न कि नर्मदा, ने गुजरात मध्यपाषाण बस्ती का समर्थन किया।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): The arrowhead embedded in the skeleton at Sarai Nahar Rai is the earliest evidence of interpersonal violence in Indian prehistory.\nReason (R): No other Mesolithic site in India has yielded skeletal trauma injuries from projectile weapons.",
    "कथन (A): सराय नाहर राय में कंकाल में धँसी तीर की नोक भारतीय प्रागैतिहास में व्यक्तिगत हिंसा का सबसे पहला प्रमाण है।\nकारण (R): भारत में कोई अन्य मध्यपाषाणकालीन स्थल प्रक्षेपास्त्र हथियारों से होने वाली कंकाल की चोटों का साक्ष्य नहीं देता है।",
    1,
    "A is true. R is partially incorrect — the statement that NO other site shows such evidence is overly absolute; but A remains the earliest confirmed example.",
    "A सही है। R आंशिक रूप से गलत है — यह कथन कि कोई अन्य स्थल ऐसा साक्ष्य नहीं दिखाता, अत्यधिक निश्चितता से कहा गया है; लेकिन A सबसे पहला पुष्ट उदाहरण बना हुआ है।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): Mahadaha in UP shows double burials with bone ornaments as grave goods.\nReason (R): The presence of grave goods suggests the Mesolithic community believed in an afterlife and recognized social differentiation.",
    "कथन (A): उत्तर प्रदेश में महदहा हड्डी के आभूषणों के साथ दोहरी कब्रें दिखाता है।\nकारण (R): कब्र के सामान की उपस्थिति सुझाती है कि मध्यपाषाणकालीन समुदाय परलोक में विश्वास करता था और सामाजिक भेद को मान्यता देता था।",
    0,
    "Both A and R are true. Grave goods are globally interpreted as evidence of afterlife beliefs and social complexity.",
    "A और R दोनों सही हैं। कब्र के सामान को विश्व स्तर पर परलोक की मान्यता और सामाजिक जटिलता के साक्ष्य के रूप में व्याख्यायित किया जाता है।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): Damdama has the highest number of Mesolithic burials found at any single site in India.\nReason (R): It shows 41 burials, including rare triple burials, indicating a highly organised burial community.",
    "कथन (A): दमदमा में भारत के किसी एकल स्थल पर सबसे अधिक मध्यपाषाणकालीन कब्रें मिली हैं।\nकारण (R): इसमें दुर्लभ तिहरी कब्रों सहित 41 कब्रें हैं, जो एक अत्यधिक संगठित शवाधान समुदाय को इंगित करती हैं।",
    0,
    "Both A and R are true, and R correctly elaborates on why Damdama holds this distinction.",
    "A और R दोनों सही हैं, और R सही ढंग से बताता है कि दमदमा यह विशेषता क्यों रखता है।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): Adamgarh rock shelters contain evidence of both early microliths and some of the earliest domesticated animal remains in India.\nReason (R): Rock shelters provided permanent, all-weather habitations that allowed communities to maintain herds nearby.",
    "कथन (A): आदमगढ़ शैल आश्रयों में प्रारंभिक सूक्ष्म पाषाण और भारत में सबसे प्रारंभिक पालतू पशुओं के कुछ अवशेष दोनों के साक्ष्य हैं।\nकारण (R): शैल आश्रयों ने स्थायी, सभी मौसमों में उपयोग योग्य आवास प्रदान किए जिससे समुदाय पास में पशुओं को रख सकते थे।",
    0,
    "Both A and R are true. Rock shelter stability allowed semi-permanent occupation and early pastoralism.",
    "A और R दोनों सही हैं। शैल आश्रय की स्थिरता ने अर्ध-स्थायी बस्ती और प्रारंभिक पशुपालन की अनुमति दी।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): The Ganga valley Mesolithic sites are devoid of any stone tool remains due to their deep alluvial soil.\nReason (R): Alluvial soils rapidly dissolve silica-based stones.",
    "कथन (A): गंगा घाटी के मध्यपाषाणकालीन स्थल अपनी गहरी जलोढ़ मिट्टी के कारण किसी भी पत्थर के उपकरण के अवशेष से रहित हैं।\nकारण (R): जलोढ़ मिट्टी सिलिका-आधारित पत्थरों को तेजी से घोल देती है।",
    3,
    "A is false — thousands of microliths were found at these sites. R is also false — silica stones (chert, chalcedony) are chemically resistant to alluvial soil dissolution.",
    "A गलत है — इन स्थलों पर हजारों सूक्ष्म पाषाण मिले हैं। R भी गलत है — सिलिका पत्थर (चर्ट, चाल्सीडोनी) जलोढ़ मिट्टी में रासायनिक रूप से घुलनशील नहीं होते।"
)

add_ar(sec3_en, sec3_hi,
    "Assertion (A): The Ganga plain Mesolithic sites show no evidence of permanent structures or built houses.\nReason (R): Mesolithic communities were semi-nomadic hunter-gatherers who built temporary shelters from organic materials.",
    "कथन (A): गंगा के मैदान के मध्यपाषाणकालीन स्थल स्थायी संरचनाओं या बने हुए घरों का कोई साक्ष्य नहीं दिखाते हैं।\nकारण (R): मध्यपाषाणकालीन समुदाय अर्ध-घुमंतू शिकारी-संग्रहकर्ता थे जो जैविक सामग्री से अस्थायी आश्रय बनाते थे।",
    0,
    "Both A and R are true. The absence of stone foundations or permanent mud-brick walls confirms the temporary nature of Mesolithic habitation.",
    "A और R दोनों सही हैं। पत्थर की नींव या स्थायी मिट्टी की दीवारों की अनुपस्थिति मध्यपाषाणकालीन बस्ती की अस्थायी प्रकृति की पुष्टि करती है।"
)

# --- 8. Statement-Based (5 Questions) ---
add_stmt(sec3_en, sec3_hi,
    "Consider the following statements regarding the Mesolithic site of Bagor:\n1. It is located on the Kothari River in Rajasthan.\n2. It is the largest Mesolithic site in India and shows evidence of animal domestication.\nWhich of the statements given above is/are correct?",
    "मध्यपाषाणकालीन स्थल बागोर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह राजस्थान में कोठारी नदी पर स्थित है।\n2. यह भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है और पशुपालन के साक्ष्य दिखाता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct — Bagor is on the Kothari River and is India's largest Mesolithic site with animal domestication evidence.",
    "दोनों कथन सही हैं — बागोर कोठारी नदी पर है और पशुपालन साक्ष्य के साथ भारत का सबसे बड़ा मध्यपाषाणकालीन स्थल है।"
)

add_stmt(sec3_en, sec3_hi,
    "With reference to Ganga valley Mesolithic sites, consider the following statements:\n1. Damdama has the highest number of human burials at a single site, including triple burials.\n2. The skeleton at Mahadaha shows an embedded arrowhead, proving prehistoric conflict.\nWhich of the statements given above is/are correct?",
    "गंगा घाटी मध्यपाषाणकालीन स्थलों के संदर्भ में, निम्नलिखित कथनों पर विचार करें:\n1. दमदमा में तिहरी कब्रों सहित किसी एकल स्थल पर मानव कब्रों की सबसे अधिक संख्या है।\n2. महदहा के कंकाल में एक धँसी तीर की नोक दिखाई देती है, जो प्रागैतिहासिक संघर्ष को साबित करती है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct (Damdama has 41 burials). Statement 2 is incorrect — the embedded arrowhead skeleton is at Sarai Nahar Rai, not Mahadaha.",
    "कथन 1 सही है (दमदमा में 41 कब्रें हैं)। कथन 2 गलत है — धँसी तीर की नोक वाला कंकाल सराय नाहर राय में है, महदहा में नहीं।"
)

add_stmt(sec3_en, sec3_hi,
    "Consider the following statements about Langhnaj:\n1. Langhnaj was excavated by H.D. Sankalia and is located in the Sabarmati basin of Gujarat.\n2. Human skeletons, animal bones, and microliths were found together at the site.\nWhich of the statements given above is/are correct?",
    "लांघनाज के बारे में निम्नलिखित कथनों पर विचार करें:\n1. लांघनाज का उत्खनन एच.डी. सांकलिया ने किया था और यह गुजरात के साबरमती बेसिन में स्थित है।\n2. स्थल पर मानव कंकाल, जानवरों की हड्डियाँ और सूक्ष्म पाषाण एक साथ पाए गए थे।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    2,
    "Both statements are correct. Sankalia excavated Langhnaj, which is in the Sabarmati basin, and yielded all three categories of remains.",
    "दोनों कथन सही हैं। सांकलिया ने लांघनाज का उत्खनन किया, जो साबरमती बेसिन में है, और तीनों श्रेणियों के अवशेष प्राप्त हुए।"
)

add_stmt(sec3_en, sec3_hi,
    "Consider the following pairs of Mesolithic sites and their key features:\n1. Sarai Nahar Rai : Earliest Mesolithic site in the Ganga plains with conflict skeleton\n2. Mahadaha : 41 burials including triple burials\nHow many of the pairs given above are correctly matched?",
    "मध्यपाषाणकालीन स्थलों और उनकी प्रमुख विशेषताओं के निम्नलिखित युग्मों पर विचार करें:\n1. सराय नाहर राय : गंगा के मैदानों में सबसे प्रारंभिक मध्यपाषाणकालीन स्थल जहाँ संघर्ष कंकाल है\n2. महदहा : तिहरी कब्रों सहित 41 कब्रें\nऊपर दिए गए कितने युग्म सही सुमेलित हैं?",
    ["Only one pair", "Both pairs", "Neither pair", "Cannot be determined"],
    ["केवल एक युग्म", "दोनों युग्म", "कोई भी युग्म नहीं", "निर्धारित नहीं किया जा सकता"],
    0,
    "Only Pair 1 is correct. Pair 2 is incorrect — 41 burials (including triple burials) belong to Damdama, not Mahadaha. Mahadaha is known for double burials.",
    "केवल युग्म 1 सही है। युग्म 2 गलत है — 41 कब्रें (तिहरी कब्रों सहित) दमदमा की हैं, महदहा की नहीं। महदहा दोहरी कब्रों के लिए जाना जाता है।"
)

add_stmt(sec3_en, sec3_hi,
    "Consider the following statements about Adamgarh:\n1. It is a rock shelter site in Madhya Pradesh near the Narmada River.\n2. It is the largest sand-dune Mesolithic site in India.\nWhich of the statements given above is/are correct?",
    "आदमगढ़ के बारे में निम्नलिखित कथनों पर विचार करें:\n1. यह मध्य प्रदेश में नर्मदा नदी के पास एक शैल आश्रय स्थल है।\n2. यह भारत का सबसे बड़ा रेत के टीले वाला मध्यपाषाणकालीन स्थल है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?",
    ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
    ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    0,
    "Statement 1 is correct. Statement 2 is incorrect — Adamgarh is a rock shelter site, not a sand dune site. Langhnaj (Gujarat) is the sand dune site; Bagor (Rajasthan) is the largest Mesolithic site.",
    "कथन 1 सही है। कथन 2 गलत है — आदमगढ़ एक शैल आश्रय स्थल है, रेत के टीले का स्थल नहीं। लांघनाज (गुजरात) रेत का टीला है; बागोर (राजस्थान) सबसे बड़ा मध्यपाषाणकालीन स्थल है।"
)

# --- 9. Why (3 Questions) ---
add_open(sec3_en, sec3_hi, "Why",
    "Why is Bagor considered the most important Mesolithic site in India?",
    "बागोर को भारत का सबसे महत्वपूर्ण मध्यपाषाणकालीन स्थल क्यों माना जाता है?",
    "Bagor is the largest (2500+ sq m) and most extensively excavated Mesolithic site. It provides the most complete chronological sequence showing three distinct phases: Phase I (microliths + animal domestication, c. 5000 BCE), Phase II (copper tool integration, c. 2800 BCE), and Phase III (historic contact). No other Indian site records such a continuous Mesolithic-to-early-historical transition.",
    "बागोर सबसे बड़ा (2500+ वर्ग मीटर) और सबसे व्यापक रूप से उत्खनित मध्यपाषाणकालीन स्थल है। यह तीन अलग-अलग चरणों को दिखाने वाला सबसे पूर्ण कालानुक्रमिक अनुक्रम प्रदान करता है: प्रथम चरण (सूक्ष्म पाषाण + पशुपालन, लगभग 5000 ईसा पूर्व), द्वितीय चरण (तांबे के उपकरण, लगभग 2800 ईसा पूर्व), और तृतीय चरण (ऐतिहासिक संपर्क)।"
)

add_open(sec3_en, sec3_hi, "Why",
    "Why do Ganga valley Mesolithic sites (Sarai Nahar Rai, Mahadaha, Damdama) show such high-density burials?",
    "गंगा घाटी मध्यपाषाणकालीन स्थल (सराय नाहर राय, महदहा, दमदमा) इतनी अधिक घनत्व वाली कब्रें क्यों दिखाते हैं?",
    "Oxbow lake ecology provided stable, year-round resources, encouraging repeated seasonal returns by the same bands. Over many generations, the same camps were reused, and deceased community members were buried in the same habitation zone. Social cohesion and resource stability drove the accumulation of burial densities.",
    "गोखुर झील पारिस्थितिकी ने स्थिर, साल भर के संसाधन प्रदान किए, जिससे एक ही समूह के बार-बार मौसमी वापसी को प्रोत्साहन मिला। कई पीढ़ियों तक एक ही शिविरों का पुनः उपयोग किया गया, और मृत सदस्यों को उसी बस्ती क्षेत्र में दफनाया गया। सामाजिक एकजुटता और संसाधन स्थिरता ने कब्र घनत्व संचय को प्रेरित किया।"
)

add_open(sec3_en, sec3_hi, "Why",
    "Why is the embedded arrowhead at Sarai Nahar Rai archaeologically significant?",
    "सराय नाहर राय में धँसी तीर की नोक पुरातात्विक रूप से महत्वपूर्ण क्यों है?",
    "The embedded stone point in the pelvic bone is the oldest material evidence of intentional lethal conflict between humans in India, predating all historical war records by thousands of years. It proves that inter-group warfare or interpersonal violence was a social reality even among Mesolithic foraging bands.",
    "कूल्हे की हड्डी में धँसी पत्थर की नोक भारत में मनुष्यों के बीच जानबूझकर किए गए घातक संघर्ष का सबसे पुराना भौतिक साक्ष्य है, जो सभी ऐतिहासिक युद्ध अभिलेखों से हजारों वर्ष पहले का है। यह साबित करता है कि मध्यपाषाणकालीन शिकारी समूहों के बीच भी समूहों के बीच युद्ध एक सामाजिक वास्तविकता थी।"
)

# --- 10. How (3 Questions) ---
add_open(sec3_en, sec3_hi, "How",
    "How does the three-phase stratigraphy of Bagor reveal the progression from Mesolithic to early historical periods?",
    "बागोर की तीन-चरण स्तरविन्यास (stratigraphy) मध्यपाषाण से प्रारंभिक ऐतिहासिक काल तक की प्रगति को कैसे प्रकट करती है?",
    "Phase I (lowest layer): Pure Mesolithic microliths with animal bones of domesticated species. Phase II (middle layer): Microliths coexist with early copper spear tips and hand-made pottery, indicating Chalcolithic contact. Phase III (top layer): Iron tools and NBP pottery appear, linking the site to the early historical period.",
    "प्रथम चरण (सबसे निचली परत): पालतू प्रजातियों की हड्डियों के साथ शुद्ध मध्यपाषाण सूक्ष्म पाषाण। द्वितीय चरण (मध्य परत): सूक्ष्म पाषाण प्रारंभिक तांबे की भाला की नोक और हस्तनिर्मित बर्तनों के साथ सह-अस्तित्व में, जो ताम्रपाषाण संपर्क दर्शाता है। तृतीय चरण (ऊपरी परत): लोहे के उपकरण और NBP मिट्टी के बर्तन दिखाई देते हैं।"
)

add_open(sec3_en, sec3_hi, "How",
    "How does the burial evidence at Mahadaha and Damdama reveal emerging social complexity in the Mesolithic?",
    "महदहा और दमदमा में शवाधान साक्ष्य मध्यपाषाण काल में उभरती सामाजिक जटिलता को कैसे प्रकट करता है?",
    "Single and double burials with elaborate bone ornaments, shells, and food offerings suggest individual social identities and ranks. Triple burials might indicate family units or community leadership. The systematic orientation of bodies (east-west) implies shared spiritual beliefs across a community, marking the rise of organised social and ritual life.",
    "हड्डी के आभूषणों, शंखों और भोजन चढ़ावे के साथ एकल और दोहरी कब्रें व्यक्तिगत सामाजिक पहचान और रैंक का सुझाव देती हैं। तिहरी कब्रें पारिवारिक इकाइयों या सामुदायिक नेतृत्व को इंगित कर सकती हैं। शवों का व्यवस्थित अभिविन्यास (पूर्व-पश्चिम) एक समुदाय में साझा आध्यात्मिक विश्वासों का संकेत देता है।"
)

add_open(sec3_en, sec3_hi, "How",
    "How did the ecological setting of sand dunes near seasonal lakes support Mesolithic occupation at Langhnaj?",
    "मौसमी झीलों के पास रेत के टीलों की पारिस्थितिक स्थापना ने लांघनाज में मध्यपाषाणकालीन बस्तियों का समर्थन कैसे किया?",
    "Stabilised sand dunes at Langhnaj provided dry, elevated ground safe from seasonal flooding. The adjacent rain-fed playas (seasonal lakes) provided freshwater, fish, mollusks, waterfowl, and drinking water. The dune surface served as the camp, while the lake margin served as the food source — creating an ideal hunter-gatherer habitat.",
    "लांघनाज में स्थिर रेत के टीलों ने मौसमी बाढ़ से सुरक्षित सूखी, ऊंची जमीन प्रदान की। पड़ोसी वर्षा-पोषित झीलों ने ताजे पानी, मछली, घोंघे, जलीय पक्षी और पीने का पानी प्रदान किया। टीले की सतह शिविर का काम करती थी, जबकि झील का किनारा खाद्य स्रोत था।"
)

# --- 11. Case Study (3 Questions) ---
add_open(sec3_en, sec3_hi, "Case Study",
    "Case Study: V.N. Misra's excavation of Bagor.\nDescribe how the evidence of animal domestication was identified at this Rajasthan Mesolithic site.",
    "मामला अध्ययन: वी.एन. मिश्रा द्वारा बागोर का उत्खनन।\nवर्णन करें कि इस राजस्थान मध्यपाषाणकालीन स्थल पर पशुपालन के साक्ष्य की पहचान कैसे की गई।",
    "V.N. Misra recovered animal bones from the Phase I layers (c. 5000 BCE) at Bagor. Zooarchaeologists analyzed the age and size profiles of cattle, sheep, and goat bones. Domesticated animals show a deliberate culling pattern — young males are killed for meat while breeding females are preserved. This selective slaughter profile, combined with small body size (indicating selective breeding generations), proved controlled husbandry, not wild hunting.",
    "वी.एन. मिश्रा ने बागोर में प्रथम चरण की परतों (लगभग 5000 ईसा पूर्व) से जानवरों की हड्डियाँ बरामद कीं। पशु-पुरातत्वविदों ने मवेशियों, भेड़ों और बकरियों की हड्डियों की आयु और आकार प्रोफाइल का विश्लेषण किया। पालतू जानवरों में मांस के लिए जानबूझकर युवा नरों को मारा जाता था जबकि प्रजनन करने वाली मादाओं को जीवित रखा जाता था। यह चयनात्मक वध पैटर्न, छोटे शरीर के आकार के साथ, नियंत्रित पशुपालन साबित करता है।"
)

add_open(sec3_en, sec3_hi, "Case Study",
    "Case Study: G.R. Sharma's excavation of the Pratapgarh Cluster (Sarai Nahar Rai, Mahadaha, Damdama).\nExplain how burial evidence reconstructs social life in the Ganga valley Mesolithic.",
    "मामला अध्ययन: जी.आर. शर्मा द्वारा प्रतापगढ़ समूह (सराय नाहर राय, महदहा, दमदमा) का उत्खनन।\nस्पष्ट करें कि शवाधान साक्ष्य गंगा घाटी के मध्यपाषाण काल में सामाजिक जीवन का पुनर्निर्माण कैसे करता है।",
    "G.R. Sharma excavated all three sites. At Sarai Nahar Rai, hearths and the conflict skeleton reveal hunting disputes and communal cooking. At Mahadaha, double burials with bone necklaces and earrings reveal family units and personal identity. At Damdama, 41 burials including triples show elaborate rituals. Together, these sites trace a community cycling seasonally among three oxbow lake camps.",
    "जी.आर. शर्मा ने तीनों स्थलों का उत्खनन किया। सराय नाहर राय में, चूल्हे और संघर्ष कंकाल शिकार विवादों और सामुदायिक खाना पकाने को प्रकट करते हैं। महदहा में, हड्डी के हार और झुमकों के साथ दोहरी कब्रें पारिवारिक इकाइयों और व्यक्तिगत पहचान को प्रकट करती हैं। दमदमा में, तिहरी कब्रों सहित 41 कब्रें विस्तृत अनुष्ठानों को दर्शाती हैं।"
)

add_open(sec3_en, sec3_hi, "Case Study",
    "Case Study: Langhnaj Sand Dune Stratigraphy.\nExplain how Sankalia's stratigraphic analysis at Langhnaj revealed the long time-span of Mesolithic occupation in Gujarat.",
    "मामला अध्ययन: लांघनाज रेत के टीले का स्तरविन्यास।\nस्पष्ट करें कि लांघनाज में सांकलिया के स्तरविन्यासात्मक विश्लेषण ने गुजरात में मध्यपाषाणकालीन बस्ती के लंबे समय के विस्तार को कैसे प्रकट किया।",
    "Sankalia found a layered profile at Langhnaj: the lower sterile yellow sand layers (no human activity) overlay the transition zone where the first microliths appear. Above this are thick cultural layers with microliths, hearths, animal bones, and human skeletons. The uppermost layers show hand-made pottery interspersed with microliths, proving continuous occupation from c. 5000 BCE to c. 2000 BCE.",
    "सांकलिया ने लांघनाज में एक स्तरित प्रोफाइल पाया: निचली बंजर पीली रेत की परतें (कोई मानव गतिविधि नहीं) संक्रमण क्षेत्र के ऊपर हैं जहाँ पहले सूक्ष्म पाषाण दिखाई देते हैं। इसके ऊपर सूक्ष्म पाषाण, चूल्हे, जानवरों की हड्डियाँ और मानव कंकाल के साथ मोटी सांस्कृतिक परतें हैं। सबसे ऊपरी परतें सूक्ष्म पाषाणों के साथ हस्तनिर्मित बर्तन दिखाती हैं।"
)

# --- 12. Teach the Concept (3 Questions) ---
add_open(sec3_en, sec3_hi, "Teach the Concept",
    "Teach the Concept: Explain why Bagor is more important than Langhnaj for understanding Indian Mesolithic chronology.",
    "अवधारणा समझाएं: समझाएं कि भारतीय मध्यपाषाण कालक्रम को समझने के लिए बागोर लांघनाज से अधिक महत्वपूर्ण क्यों है।",
    "Langhnaj is a rich site but shows mostly a single-phase occupation with microliths and burials. Bagor has three distinct stratigraphic phases showing cultural evolution over several thousand years — from a pure Mesolithic foraging camp (Phase I) to a site with early copper tools and pottery (Phase II) to historic contact layers (Phase III). This multi-phase record makes Bagor uniquely valuable for tracing the entire transition.",
    "लांघनाज एक समृद्ध स्थल है लेकिन ज्यादातर एकल-चरण बस्ती दिखाता है। बागोर में तीन अलग-अलग स्तरविन्यासात्मक चरण हैं जो कई हजार वर्षों में सांस्कृतिक विकास दिखाते हैं — एक शुद्ध मध्यपाषाण शिकार शिविर से तांबे के उपकरण और बर्तनों वाले स्थल तक। यह बहु-चरण रिकॉर्ड बागोर को पूरे संक्रमण को ट्रेस करने के लिए अद्वितीय रूप से मूल्यवान बनाता है।"
)

add_open(sec3_en, sec3_hi, "Teach the Concept",
    "Teach the Concept: Explain the significance of grave goods (burial offerings) in reconstructing Mesolithic social systems.",
    "अवधारणा समझाएं: मध्यपाषाणकालीन सामाजिक प्रणालियों के पुनर्निर्माण में कब्र के सामान (शवाधान अर्पण) के महत्व को समझाएं।",
    "When we find bones buried with necklaces, tools, and food pots, we learn something profound. The objects placed with the dead were valuable goods the community decided to 'give away' forever. This means: (1) people believed in an afterlife where the dead might use these items; (2) some people received more grave goods than others — showing rank and status emerged. Without written records, grave goods are archaeology's main window into social structure.",
    "जब हम हार, उपकरणों और भोजन के बर्तनों के साथ दफनाई गई हड्डियाँ पाते हैं, तो हम कुछ गहरा सीखते हैं। मृतकों के साथ रखी गई वस्तुएं मूल्यवान थीं जिन्हें समुदाय ने हमेशा के लिए 'दे देने' का फैसला किया। इसका मतलब है: (1) लोगों का परलोक में विश्वास था; (2) कुछ लोगों को अधिक सामान मिला — सामाजिक रैंक और स्थिति का उदय दर्शाता है।"
)

add_open(sec3_en, sec3_hi, "Teach the Concept",
    "Teach the Concept: Use a simple analogy to explain why the Ganga Plain Mesolithic sites (like Mahadaha) have no stone naturally nearby, yet contain thousands of microliths.",
    "अवधारणा समझाएं: एक सरल सादृश्य का उपयोग करके समझाएं कि गंगा के मैदान के मध्यपाषाणकालीन स्थलों (जैसे महदहा) के पास कोई प्राकृतिक पत्थर नहीं है, फिर भी हजारों सूक्ष्म पाषाण क्यों हैं।",
    "Imagine a campsite in a dense forest where no grocery store exists. Yet the campers have food, utensils, and tools — because they brought supplies from towns far away. Similarly, the Ganga plains have no stone outcrops. Yet Mahadaha has thousands of chert/chalcedony tools. The Mesolithic people must have collected raw stones from the Vindhyan hills (80-100 km away) during seasonal migrations and carried them as portable tool kits.",
    "एक घने जंगल में एक शिविर की कल्पना करें जहाँ कोई किराने की दुकान नहीं है। फिर भी शिविरार्थियों के पास भोजन, बर्तन और उपकरण हैं — क्योंकि वे दूर के शहरों से आपूर्ति लाए थे। इसी तरह, गंगा के मैदानों में कोई पत्थर नहीं है। फिर भी महदहा में हजारों चर्ट/चाल्सीडोनी उपकरण हैं। मध्यपाषाणकालीन लोग मौसमी प्रवास के दौरान विंध्यन पहाड़ियों से कच्चे पत्थर ले आते थे।"
)
