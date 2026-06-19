import json
import os

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Early-VedicRigvedic-Period\Sources-for-Information-about-Vedic-Society-and-Culture"
hi_dir = os.path.join(base_dir, "hi")
os.makedirs(hi_dir, exist_ok=True)

# 1. Generate hi/index.html by translating index.html
english_index_path = os.path.join(base_dir, "index.html")
hindi_index_path = os.path.join(hi_dir, "index.html")

with open(english_index_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Substitutions for Hindi HTML
html = html.replace('<html lang="en">', '<html lang="hi">')
html = html.replace(
    '<title>Sources for Information about Vedic Society and Culture - UPSC Civil Services Study Guide | SJMaths</title>',
    '<title>वैदिक समाज और संस्कृति के बारे में जानकारी के स्रोत - UPSC सिविल सेवा अध्ययन गाइड | SJMaths</title>'
)
html = html.replace(
    '<meta name="description" content="Comprehensive UPSC study guide on Sources for Information about Vedic Society and Culture. Explore the Rigveda, other Vedic texts, archaeological evidence, and linguistic sources. Includes notes, flashcards, 50 practice questions, and a timed mock test.">',
    '<meta name="description" content="वैदिक समाज और संस्कृति के बारे में जानकारी के स्रोतों पर व्यापक UPSC अध्ययन गाइड। ऋग्वेद, अन्य वैदिक ग्रंथों, पुरातात्विक साक्ष्यों और भाषाई स्रोतों का अन्वेषण करें। नोट्स, फ्लैशकार्ड, 50 अभ्यास प्रश्न और एक समयबद्ध मॉक टेस्ट शामिल हैं।">'
)
html = html.replace(
    '<link rel="canonical" href="https://sjmaths.com/upsc/ancient_history/History-of-Early-VedicRigvedic-Period/Sources-for-Information-about-Vedic-Society-and-Culture/">',
    '<link rel="canonical" href="https://sjmaths.com/upsc/ancient_history/History-of-Early-VedicRigvedic-Period/Sources-for-Information-about-Vedic-Society-and-Culture/hi/">'
)
html = html.replace(
    '',
    ''
)
html = html.replace(
    '<a href="hi/">Hindi Version</a>',
    '<a href="../">English Version</a>'
)
html = html.replace(
    '<a href="hi/" class="mobile-lang-toggle"><i class="fas fa-globe"></i> हिन्दी</a>',
    '<a href="../" class="mobile-lang-toggle"><i class="fas fa-globe"></i> English</a>'
)
html = html.replace(
    '<nav role="navigation" aria-label="Main Navigation">\n            <a href="/">Home</a>\n            <a href="hi/">Hindi Version</a>\n            <a href="/upsc/">UPSC Dashboard</a>\n        </nav>',
    '<nav role="navigation" aria-label="Main Navigation">\n            <a href="/">होम</a>\n            <a href="../">English Version</a>\n            <a href="/upsc/">UPSC डैशबोर्ड</a>\n        </nav>'
)
html = html.replace(
    '<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. Study Notes</button>',
    '<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. अध्ययन नोट्स</button>'
)
html = html.replace(
    '<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. Practice Zone (50 Qs)</button>',
    '<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. अभ्यास क्षेत्र (50 प्रश्न)</button>'
)
html = html.replace(
    '<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. Live UPSC Mock Test</button>',
    '<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. लाइव UPSC मॉक टेस्ट</button>'
)
html = html.replace(
    'Next: Practice Zone',
    'आगे बढ़ें: अभ्यास क्षेत्र'
)
html = html.replace(
    'Next: Mock Test',
    'आगे बढ़ें: मॉक टेस्ट'
)
html = html.replace(
    'Click on the options to check your answer instantly. Click "Show Explanation" to read step-by-step solutions.',
    'उत्तरों की तुरंत जांच करने के लिए विकल्पों पर क्लिक करें। विस्तृत समाधान पढ़ने के लिए "व्याख्या देखें" पर क्लिक करें।'
)

with open(hindi_index_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: hi/index.html generated.")

# 2. Generate hi/content.json by loading content.json and translating fields to Hindi
with open(os.path.join(base_dir, "content.json"), 'r', encoding='utf-8') as f:
    eng_data = json.load(f)

# Translate root metadata
hi_data = {
    "breadcrumbs": {
        "parent": "UPSC पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "वैदिक समाज और संस्कृति के बारे में जानकारी के स्रोत"
    },
    "hero": {
        "title": "वैदिक समाज और संस्कृति के बारे में जानकारी के स्रोत",
        "description": "UPSC GS-1 के लिए वैदिक सभ्यता के साहित्यिक, पुरातात्विक और भाषाई स्रोतों पर महारत हासिल करें। ऋग्वेद की प्रधानता, वैदिक साहित्य की संरचना, पुरातात्विक साक्ष्य और मुख्य इतिहास लेखन वाद-विवाद को समझें।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव UPSC मॉक टेस्ट",
            "description": "वैदिक समाज और संस्कृति के स्रोतों पर अपने ज्ञान का परीक्षण करें। इस समयबद्ध परीक्षा में 10 उच्च-गुणवत्ता वाले, परीक्षा-मानक प्रश्न शामिल हैं। प्रारंभिक परीक्षा से पहले आत्म-मूल्यांकन के लिए सर्वोत्तम।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "टेस्ट सबमिट करें"
        }
    },
    "timeline": {
        "title": "वैदिक साहित्यिक परंपरा — कालानुक्रमिक अवलोकन",
        "description": "वैदिक समाज के पुनर्निर्माण के लिए प्रमुख ग्रंथों, उनकी रचना समयसीमा और ऐतिहासिक स्रोतों के रूप में उनके महत्व का पता लगाने के लिए नीचे प्रत्येक कार्ड पर क्लिक करें।",
        "cards": [
            {
                "period": "ऋग्वेद — सबसे पुराना स्रोत",
                "date": "लगभग 1500 ईसा पूर्व – 1000 ईसा पूर्व",
                "details": "<strong>प्रारंभिक वैदिक काल का प्राथमिक स्रोत:</strong> ऋग्वेद वैदिक संस्कृत में रचित 10 पुस्तकों (मंडलों) में 1,028 सूक्तों का संग्रह है। यह दुनिया का सबसे पुराना धार्मिक पाठ है जो अभी भी प्रचलन में है।<br><br><strong>ऐतिहासिक महत्व:</strong> मंडल II-VII ('पारिवारिक पुस्तकें') सबसे पुराने हैं, जो विशिष्ट पुरोहित परिवारों (गोत्रों) द्वारा रचित हैं। मंडल I, VIII, IX और X बाद के संकलन हैं। यह उत्तर-पश्चिम भारत के भूगोल, जनजातीय राजनीति (जन), सामाजिक संरचना (वर्ण), अर्थव्यवस्था (गोवंश, कृषि), धर्म (बहुदेववाद) और सरस्वती जैसी नदियों की भूमिका के बारे में जानकारी प्रदान करता है।"
            },
            {
                "period": "उत्तर वैदिक संहिताएं",
                "date": "लगभग 1000 ईसा पूर्व – 600 ईसा पूर्व",
                "details": "<strong>तीन उत्तर वैदिक संहिताएं:</strong> सामवेद (यज्ञों के लिए धुनें), यजुर्वेद (अनुष्ठानों के लिए गद्य सूत्र — कृष्ण/शुक्ल यजुर्वेद), और अथर्ववेद (मंत्र, जादुई आकर्षण, लोकप्रिय विश्वास) ऋग्वेद के साथ मिलकर चार वेद (चतुर्वेद) बनाते हैं।<br><br><strong>ऐतिहासिक मूल्य:</strong> अथर्ववेद सामाजिक इतिहास के लिए विशेष रूप से महत्वपूर्ण है क्योंकि इसमें चिकित्सा, लोकप्रिय धर्म, वर्ग तनाव, व्यापार और पुरोहित दृष्टिकोण से परे रोजमर्रा की जिंदगी के संदर्भ शामिल हैं। यजुर्वेद उत्तर वैदिक कृषि अर्थव्यवस्था से जुड़े जटिल अनुष्ठानों के विस्तार को दर्शाता है।"
            },
            {
                "period": "ब्राह्मण, आरण्यक और उपनिषद",
                "date": "लगभग 900 ईसा पूर्व – 500 ईसा पूर्व",
                "details": "<strong>गद्यात्मक व्याख्यात्मक साहित्य:</strong> ब्राह्मण विस्तृत गद्य टिप्पणियां हैं जो वैदिक अनुष्ठानों के अर्थ और प्रक्रिया की व्याख्या करती हैं। मुख्य ग्रंथों में ऐतरेय ब्राह्मण (ऋग्वेद), शतपथ ब्राह्मण (यजुर्वेद — सबसे बड़ा और सबसे महत्वपूर्ण), और तैत्तिरीय ब्राह्मण (यजुर्वेद) शामिल हैं।<br><br><strong>आरण्यक</strong> ('वन पुस्तकें') संक्रमणकालीन ग्रंथ हैं जो अनुष्ठानों का प्रतीकात्मक रूपक बनाते हैं। <strong>उपनिषद</strong> (कुल 108; 10-12 मुख्य) वैदिक विचार की दार्शनिक पराकाष्ठा का प्रतिनिधित्व करते हैं, जो ब्रह्म और आत्मन पर चर्चा करते हैं। वे सामाजिक प्रश्नकाल और बौद्ध व जैन जैसी सुधारवादी विचारधाराओं के उदय की अवधि को दर्शाते हैं।"
            },
            {
                "period": "वेदांग और सहायक साहित्य",
                "date": "लगभग 800 ईसा पूर्व – 200 ईसा पूर्व",
                "details": "<strong>छह वेदांग (वेद के अंग):</strong> शिक्षा (ध्वन्यात्मकता), कल्प (अनुष्ठान), व्याकरण (व्याकरण — पाणिनी की अष्टाध्यायी), निरुक्त (व्युत्पत्तिशास्त्र — यास्क द्वारा), छंद (छंद शास्त्र), और ज्योतिष (खगोल विज्ञान)।<br><br><strong>ऐतिहासिक महत्व:</strong> पाणिनी की अष्टाध्यायी (लगभग चौथी शताब्दी ईसा पूर्व) प्राचीन काल का सबसे व्यवस्थित व्याकरण है और वैदिक/उत्तर-वैदिक काल की सामाजिक संरचना, व्यापार, राजनीति और भूगोल के बारे में महत्वपूर्ण जानकारी प्रदान करता है। यास्क का निरुक्त भारतीय भाषा विज्ञान और व्युत्पत्ति का सबसे पुराना जीवित कार्य है।"
            },
            {
                "period": "पुरातात्विक और पुरालेखीय साक्ष्य",
                "date": "लगभग 1500 ईसा पूर्व – 500 ईसा पूर्व (आधुनिक काल में उत्खनन)",
                "details": "<strong>चित्रित धूसर मृदभांड (PGW) संस्कृति:</strong> उत्तर वैदिक समुदायों से जुड़ी पुरातात्विक संस्कृति, जो हस्तिनापुर, कुरुक्षेत्र, अहिच्छत्र और अतरंजीखेड़ा जैसे स्थलों पर पाई गई है। कालखंड लगभग 1100-600 ईसा पूर्व है। इस संस्कृति में लोहे के प्रगलन के साक्ष्य उत्तर वैदिक लोहे के उपयोग की पुष्टि करते हैं।<br><br><strong>गेरुए रंग के मृदभांड (OCP):</strong> संभवतः प्रारंभिक आर्य प्रवासियों या उत्तर-हड़प्पा आबादी से जुड़े हैं। ऊपरी गंगा-यमुना दोआब में पाए गए हैं।<br><br><strong>वैदिक शिलालेख और बाहरी स्रोत:</strong> सीरिया से मिले मितानी शिलालेख (लगभग 1400 ईसा पूर्व) में वैदिक देवताओं मित्र, वरुण, इंद्र और नासत्य का उल्लेख है, जो प्रोटो-इन्डो-ईरानी संस्कृति के प्रसार की पुष्टि करते हैं; ऋग्वैदिक सूक्तों की संरचना प्राचीन ईरान के अवेस्ता ग्रंथों से मेल खाती है।"
            },
            {
                "period": "भाषाई और तुलनात्मक स्रोत",
                "date": "19वीं–21वीं सदी ईस्वी (आधुनिक वैज्ञानिक विश्लेषण)",
                "details": "<strong>तुलनात्मक भाषाशास्त्र:</strong> मैक्स मूलर और अन्य 19वीं सदी के भाषाविदों ने संस्कृत के ग्रीक, लैटिन, फारसी और अन्य भारत-यूरोपीय भाषाओं के साथ संबंधों के अध्ययन का नेतृत्व किया। इसने भारत-आर्य भाषाई परिवार को स्थापित किया और आर्य प्रवास सिद्धांत को समझने में मदद की।<br><br><strong>आंतरिक आलोचना और वाद-विवाद:</strong> रोमिला थापर, आर.एस. शर्मा और डी.डी. कोसांबी जैसे आधुनिक इतिहासकार विशुद्ध धार्मिक पाठ के बजाय वैदिक ग्रंथों के सामाजिक-आर्थिक व्याख्या पर जोर देते हैं। आर्य आक्रमण बनाम आर्य प्रवास बनाम स्वदेशी मूल सिद्धांत (OIT) का विवाद UPSC के लिए एक प्रमुख वाद-विवाद है।"
            }
        ]
    },
    "mnemonics": {
        "title": "स्मृति सूत्र और त्वरित याद रखने की तकनीक",
        "description": "UPSC सिविल सेवा परीक्षा के लिए वैदिक स्रोतों के वर्गीकरण और महत्वपूर्ण तथ्यों को तुरंत याद रखने के लिए इन स्मृति सूत्रों का उपयोग करें।",
        "items": [
            {
                "title": "स्मृति सूत्र 1: चार वेद",
                "phrase": "\"RSYA — ऋग, साम, यजु, अथर्व\"",
                "decryption": "**R**igveda (ऋग्वेद - सूक्त), **S**amaveda (सामवेद - धुनें), **Y**ajurveda (यजुर्वेद - अनुष्ठान), **A**tharvaveda (अथर्ववेद - जादू/चिकित्सा)। याद रखें: 'RSY A' — सबसे पुराना ऋग्वेद है, सामाजिक इतिहास के लिए सबसे महत्वपूर्ण अथर्ववेद है।"
            },
            {
                "title": "स्मृति सूत्र 2: छह वेदांग",
                "phrase": "\"S-K-V-N-C-J (शिक्षा, कल्प, व्याकरण, निरुक्त, छंद, ज्योतिष)\"",
                "decryption": "**S**hiksha (शिक्षा), **K**alpa (कल्प), **V**yakarana (व्याकरण), **N**irukta (निरुक्त), **C**hhanda (छंद), **J**yotisha (ज्योतिष) — ये वेद के छह अंग हैं।"
            },
            {
                "title": "स्मृति सूत्र 3: ऋग्वेद की पारिवारिक पुस्तकें",
                "phrase": "\"2 से 7 — परिवार जीवित!\"",
                "decryption": "ऋग्वेद के मंडल **2 से 7** को 'पारिवारिक पुस्तकें' कहा जाता है — ये सबसे पुराने और प्रामाणिक हैं, जो भारद्वाज, विश्वामित्र, वशिष्ठ, अत्रि, कश्यप और अंगिरस जैसे विशिष्ट पुरोहित परिवारों (गोत्रों) द्वारा रचित हैं।"
            },
            {
                "title": "स्मृति सूत्र 4: चित्रित धूसर मृदभांड (PGW) स्थल",
                "phrase": "\"हाथी कुछ और अतरंजीखेड़ा खाते हैं (HKAAK)\"",
                "decryption": "**H**astinapura (हस्तिनापुर), **K**urukshetra (कुरुक्षेत्र), **A**hichhatra (अहिच्छत्र), **A**tranjikhera (अतरंजीखेड़ा), **K**aushambi (कौशांबी) — उत्तर वैदिक पुरातात्विक संस्कृति से जुड़े प्रमुख चित्रित धूसर मृदभांड (PGW) स्थल।"
            }
        ]
    },
    "traps": {
        "title": "UPSC परीक्षा के सामान्य भ्रम (Traps) जिनसे बचें",
        "items": [
            "<strong>भ्रम 1: संहिता और ब्राह्मण में भ्रम:</strong> UPSC विकल्पों में अक्सर इन्हें मिला दिया जाता है। एक <strong>संहिता</strong> सूक्तों/मंत्रों का संग्रह है (जैसे ऋग्वेद संहिता)। जबकि <strong>ब्राह्मण</strong> एक संहिता के अनुष्ठानों की व्याख्या करने वाला गद्य ग्रंथ है। दोनों अलग ग्रंथ हैं, हालांकि दोनों 'श्रुति' का हिस्सा हैं।",
            "<strong>भ्रम 2: अथर्ववेद तीसरा वेद नहीं है:</strong> अथर्ववेद <strong>चौथा वेद</strong> है। इसका क्रम ऋग्वेद → सामवेद → यजुर्वेद → अथर्ववेद है। मूल तीन वेदों (त्रयी विद्या) में ऋग, साम और यजुस शामिल थे। अथर्ववेद को बाद में शामिल किया गया।",
            "<strong>भ्रम 3: PGW ≠ हड़प्पा:</strong> चित्रित धूसर मृदभांड (PGW) संस्कृति पुरातात्विक रूप से <strong>उत्तर वैदिक काल</strong> से संबंधित है, न कि हड़प्पा या प्रारंभिक वैदिक काल से। गेरुए रंग के मृदभांड (OCP) का प्रारंभिक वैदिक काल से संबंध हो सकता है, लेकिन यह PGW के समान नहीं है।",
            "<strong>भ्रम 4: पाणिनी की अष्टाध्यायी स्वयं वेदांग नहीं है:</strong> यद्यपि व्याकरण एक वेदांग है, पाणिनी की अष्टाध्यायी बाद की शास्त्रीय रचना (लगभग चौथी शताब्दी ईसा पूर्व) है। यह वैदिक समाज के बारे में जानकारी का एक ऐतिहासिक स्रोत है, लेकिन यह स्वयं वैदिक संहिता नहीं है।",
            "<strong>भ्रम 5: 'श्रुति' बनाम 'स्मृति' भ्रम:</strong> चारों वेद, ब्राह्मण, आरण्यक और उपनिषद <strong>श्रुति</strong> (प्रकट/सुना हुआ) कहलाते हैं। जबकि महाकाव्य (रामायण, महाभारत), पुराण, धर्मसूत्र और धर्मशास्त्र <strong>स्मृति</strong> (स्मरण किया हुआ/परंपरा) कहलाते हैं। यह अंतर UPSC में बार-बार पूछा जाता।",
            "<strong>भ्रम 6: उपनिषद कोई अलग श्रेणी नहीं हैं:</strong> उपनिषद वैदिक साहित्य का अंतिम भाग हैं (वेदांत = वेदों का अंत)। वे अलग ग्रंथ नहीं हैं बल्कि प्रत्येक वेद की दार्शनिक शाखाओं के निष्कर्ष हैं। कुल 108 उपनिषद हैं लेकिन केवल 10-12 को मुख्य माना जाता है।"
        ]
    },
    "deepDive": {
        "title": "पाठ्यक्रम कोर अध्ययन नोट्स (Deep-Dive)",
        "description": "UPSC GS-I के लिए वैदिक समाज और संस्कृति के साहित्यिक, पुरातात्विक और भाषाई स्रोतों का एक व्यापक विश्लेषण।",
        "sections": []
    }
}

# Translate sections into Hindi while keeping the structure of 62 questions in each section's mastery zone
# We will write a lightweight translation function in Python to map the questions to Hindi or output them directly
# Let's run a translation parser for the deep-dive notes and questions to make them Hindi standard

hi_sections = []
for idx, sec in enumerate(eng_data["deepDive"]["sections"]):
    title = sec["title"]
    # Simple titles translation
    titles_map = {
        "1. The Rigveda — The Premier Source": "1. ऋग्वेद — प्राथमिक स्रोत (The Rigveda — The Premier Source)",
        "2. The Later Vedic Samhitas — Samaveda, Yajurveda & Atharvaveda": "2. उत्तर वैदिक संहिताएं — सामवेद, यजुर्वेद और अथर्ववेद",
        "3. Brahmanas, Aranyakas, and Upanishads": "3. ब्राह्मण, आरण्यक और उपनिषद",
        "4. Vedangas — The Six Auxiliary Sciences": "4. वेदांग — छह सहायक विज्ञान",
        "5. Archaeological & External Sources": "5. पुरातात्विक और बाहरी स्रोत",
        "6. Historiographical Debates — Aryan Origins & Methodological Issues": "6. इतिहास लेखन वाद-विवाद — आर्यों का मूल और पद्धति संबंधी मुद्दे"
    }
    hi_title = titles_map.get(title, title)
    
    # We will translate the content body to Hindi
    # Let's map each section content body to its Hindi equivalent (rich HTML)
    content_map = [
        # Section 1
        """<p><strong>ऋग्वेद</strong> प्रारंभिक वैदिक (ऋग्वैदिक) काल के लिए सबसे पुराना और सबसे महत्वपूर्ण स्रोत है। इसमें <strong>1,028 सूक्त</strong> शामिल हैं जो <strong>10 मंडलों (पुस्तकों)</strong> में व्यवस्थित हैं। इसे <strong>ऋग्वेद संहिता</strong> भी कहा जाता है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-book"></i> ऋग्वेद की संरचना</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>10,600 मंत्र (ऋचाएं)</strong> 10 मंडलों में फैले हुए हैं।</li>
      <li><strong>मंडल II–VII</strong>: पारिवारिक पुस्तकें — सबसे पुरानी, गोत्रों द्वारा रचित।</li>
      <li><strong>मंडल IX</strong>: पूरी तरह से सोम (अनुष्ठानिक पौधे) को समर्पित।</li>
      <li><strong>मंडल X</strong>: नवीनतम संकलन; इसमें <em>पुरुष सूक्त</em> (वर्णों की उत्पत्ति) और <em>नासदीय सूक्त</em> (सृष्टि सूक्त) शामिल हैं।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-landmark"></i> प्राप्त ऐतिहासिक जानकारी</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>भूगोल:</strong> सिंधु, सरस्वती (सबसे पवित्र नदी), गंगा (केवल एक बार उल्लेख), और सप्त-सिंधु क्षेत्र।</li>
      <li><strong>राजनीति:</strong> जनजातीय संगठन — सभा, समिति, गण, विधात विधानसभाएं; राजा का पद वंशानुगत नहीं था।</li>
      <li><strong>अर्थव्यवस्था:</strong> गोवंश-आधारित पशुपालक अर्थव्यवस्था; युद्ध को 'गविष्टि' (गायों की खोज) कहा गया है।</li>
      <li><strong>समाज:</strong> व्यवसाय पर आधारित लचीली वर्ण व्यवस्था।</li>
    </ul>
  </div>
</div>""",
        # Section 2
        """<p>ऋग्वेद के बाद रचित तीन बाद के वेद, मिलकर <strong>चतुर्वेद</strong> (चार वेद) कहलाते हैं। वे प्रारंभिक से उत्तर वैदिक काल तक सामाजिक संरचना और अर्थव्यवस्था के विकास को समझने के लिए महत्वपूर्ण स्रोत हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-music"></i> सामवेद</div>
    <p style="font-size: 0.88rem; line-height: 1.5; margin-top: 0.5rem;">सामवेद 'धुनों का वेद' है। इसके लगभग सभी 1,549 श्लोक ऋग्वेद से लिए गए हैं। इन्हें सोम यज्ञ के दौरान उद्गाता पुरोहित द्वारा गाने के लिए संगीतबद्ध किया गया था।</p>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-fire"></i> यजुर्वेद</div>
    <p style="font-size: 0.88rem; line-height: 1.5; margin-top: 0.5rem;">यजुर्वेद 'यज्ञीय सूत्रों का वेद' है। यह दो संस्करणों में मौजूद है — <strong>कृष्ण यजुर्वेद</strong> (तैत्तिरीय संहिता) और <strong>शुक्ल यजुर्वेद</strong> (वाजसनेयी संहिता)। इसका पाठ अध्वर्यु पुरोहित द्वारा किया जाता था।</p>
  </div>
</div>
<div class="info-subcard" style="margin-top: 1rem;">
  <div class="subcard-header"><i class="fas fa-star"></i> अथर्ववेद — सामाजिक इतिहास के लिए अद्वितीय मूल्य</div>
  <p style="font-size: 0.88rem; line-height: 1.5; margin-top: 0.5rem;">अथर्ववेद 'जादू-टोने और तंत्र-मंत्र का वेद' है। इसमें 20 अध्यायों में 731 सूक्त शामिल हैं। यह बीमारी के इलाज के मंत्र, प्राकृतिक आपदाओं से बचाव और आम जनता के लोक विश्वासों को दर्शाता है। इसमें लोहे ('श्याम अयस') के संदर्भ शामिल हैं, जो उत्तर वैदिक काल की पुष्टि करते हैं।</p>
</div>""",
        # Section 3
        """<p>ये ग्रंथ वैदिक संहिताओं की गद्यात्मक व्याख्या और दार्शनिक निष्कर्ष हैं, जिन्हें <strong>श्रुति</strong> के रूप में वर्गीकृत किया गया है।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-scroll"></i> ब्राह्मण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>ऐतरेय ब्राह्मण:</strong> राज्याभिषेक अनुष्ठानों का विवरण।</li>
      <li><strong>शतपथ ब्राह्मण:</strong> सबसे बड़ा ब्राह्मण; विदेघ माथव और अग्नि वैश्वानर द्वारा गंगा की ओर प्रसार का विवरण।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-tree"></i> आरण्यक और उपनिषद</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>आरण्यक:</strong> वन पुस्तकें जो अनुष्ठान का प्रतीकात्मक चित्रण करती हैं।</li>
      <li><strong>उपनिषद:</strong> आत्मा और ब्रह्म पर गहन दार्शनिक संवाद; यज्ञीय अनुष्ठानों की आलोचना।</li>
    </ul>
  </div>
</div>""",
        # Section 4
        """<p>वेदों के सही उच्चारण, अनुष्ठान और पाठ को समझने में सहायता के लिए छह <strong>वेदांगों</strong> का विकास किया गया।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-language"></i> वेदांगों का विवरण</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>शिक्षा:</strong> ध्वन्यात्मकता (pronunciation)।</li>
      <li><strong>व्याकरण:</strong> पाणिनी की अष्टाध्यायी।</li>
      <li><strong>निरुक्त:</strong> यास्क द्वारा रचित व्युत्पत्तिशास्त्र (etymology)।</li>
      <li><strong>कल्प:</strong> अनुष्ठान नियम (धर्मसूत्र, गृह्यसूत्र, श्रौतसूत्र, शुल्बसूत्र)।</li>
      <li><strong>छंद:</strong> काव्य छंद।</li>
      <li><strong>ज्योतिष:</strong> खगोल विज्ञान (लगध का वेदांग ज्योतिष)।</li>
    </ul>
  </div>
</div>""",
        # Section 5
        """<p>आर्थिक और सामाजिक परिवर्तनों की पुष्टि साहित्यिक स्रोतों के साथ पुरातात्विक और विदेशी पुरालेख साक्ष्य भी करते हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-shovel"></i> चित्रित धूसर मृदभांड (PGW)</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li>कालखंड लगभग 1100-600 ईसा पूर्व — उत्तर वैदिक काल का प्रतिनिधि।</li>
      <li>हस्तिनापुर, अतरंजीखेड़ा, और कुरुक्षेत्र में पाया गया।</li>
      <li>लोहे के औजारों की उपस्थिति कृषि और वन सफाई की पुष्टि करती है।</li>
    </ul>
  </div>
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-globe-asia"></i> विदेशी साक्ष्य</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>बोगाजकोई शिलालेख (c. 1400 BCE):</strong> तुर्की से मिला, इंद्र, मित्र, वरुण, नासत्य देवों का उल्लेख।</li>
      <li><strong>अवेस्ता:</strong> ईरानी धर्मग्रंथ जो ऋग्वेद के साथ भाषाई समानता साझा करता है।</li>
    </ul>
  </div>
</div>""",
        # Section 6
        """<p>वैदिक ग्रंथों की व्याख्या में विभिन्न इतिहासकारों के दृष्टिकोण और मतभेद शामिल हैं।</p>
<div class="deep-dive-grid">
  <div class="info-subcard">
    <div class="subcard-header"><i class="fas fa-microscope"></i> वाद-विवाद</div>
    <ul style="margin-top: 0.5rem; padding-left: 1.1rem; font-size: 0.88rem; line-height: 1.5;">
      <li><strong>आर्य आक्रमण सिद्धांत:</strong> मैक्स मूलर द्वारा प्रस्तावित, अब खारिज।</li>
      <li><strong>आर्य प्रवास सिद्धांत:</strong> स्टेपी क्षेत्र से क्रमिक आगमन, आनुवंशिक (DNA) अध्ययन द्वारा समर्थित।</li>
      <li><strong>स्वदेशी मूल सिद्धांत (OIT):</strong> आर्यों को भारत का मूल निवासी बताना।</li>
      <li><strong>संयुक्त पद्धति:</strong> डी.डी. कोसांबी द्वारा ग्रंथों, सिक्कों और पुरातत्व का एक साथ उपयोग।</li>
    </ul>
  </div>
</div>"""
    ]
    hi_content = content_map[idx]
    
    # We also need to map the masteryZone questions to Hindi
    # We will build a structured translation mapping dictionary to cover all 6 sections
    
    # 1. Translation Maps for Programmatic / Loop questions
    terms_map = {
        # Section 1
        "Rita": "ऋत (Rita)", "Jana": "जन (Jana)", "Vis": "विश (Vis)", "Gramani": "ग्रामणी (Gramani)", 
        "Niyoga": "नियोग (Niyoga)", "Gavishti": "गविष्टि (Gavishti)", "Soma": "सोम (Soma)", "Upasaka": "उपासक (Upasaka)",
        # Section 2
        "Bali": "बलि (Bali)", "Bhaga": "भाग (Bhaga)", "Sangrahitri": "संग्रहीत्री (Sangrahitri)", "Suta": "सूत (Suta)", 
        "Akshavapa": "अक्षावाप (Akshavapa)", "Adhyaksha": "अध्यक्ष (Adhyaksha)", "Gahapati": "गृहपति (Gahapati)", "Sena": "सेना (Sena)",
        # Section 3
        "Atman": "आत्मन (Atman)", "Brahman": "ब्रह्म (Brahman)", "Samsara": "संसार (Samsara)", "Moksha": "मोक्ष (Moksha)", 
        "Pancha-agni": "पंचाग्नि (Pancha-agni)", "Videha": "विदेह (Videha)", "Pravahana Jaivali": "प्रवाहण जैवलि (Pravahana Jaivali)", "Janaka": "जनक (Janaka)",
        # Section 4
        "Shiksha": "शिक्षा (Shiksha)", "Vyakarana": "व्याकरण (Vyakarana)", "Nirukta": "निरुक्त (Nirukta)", "Chhanda": "छंद (Chhanda)", 
        "Jyotisha": "ज्योतिष (Jyotisha)", "Shulba Sutras": "शुल्ब सूत्र (Shulba Sutras)", "Dharma Sutras": "धर्म सूत्र (Dharma Sutras)", "Griha Sutras": "गृह्य सूत्र (Griha Sutras)",
        # Section 5
        "Hastinapura": "हस्तिनापुर (Hastinapura)", "Atranjikhera": "अतरंजीखेड़ा (Atranjikhera)", "Jakhera": "जखेड़ा (Jakhera)", 
        "Noh": "नोह (Noh)", "Allahpura": "अल्लाहपुरा (Allahpura)", "Bhagwanpura": "भगवानपुरा (Bhagwanpura)", "Boghazkoi": "बोगजकोई (Boghazkoi)", "Majiayuan": "माजियायुआन (Majiayuan)",
        # Section 6
        "Aryan Invasion Theory": "आर्य आक्रमण सिद्धांत (Aryan Invasion Theory)", "Aryan Migration Theory": "आर्य प्रवास सिद्धांत (Aryan Migration Theory)", 
        "Out of India Theory": "आउट ऑफ इंडिया थ्योरी (OIT)", "Combined Method": "संयुक्त पद्धति (Combined Method)", 
        "Rakhigarhi DNA": "राखीगढ़ी डीएनए (Rakhigarhi DNA)", "Sarasvati Hydrology": "सरस्वती जल विज्ञान (Sarasvati Hydrology)", 
        "Steppe Ancestry": "स्टेपी आनुवंशिकी (Steppe Ancestry)", "Indigenous Origin": "स्वदेशी मूल (Indigenous Origin)"
    }

    # 2. Main translation dictionary for all MCQ, True/False, Fill, Match, Why, How, Case Study, and Teach questions
    q_dict = {
        # --- Section 1: Rigveda ---
        "Which Mandala of the Rigveda contains the Purusha Sukta, introducing the fourfold social order?": {
            "q": "ऋग्वेद के किस मंडल में पुरुष सूक्त शामिल है, जो चतुष्कोणीय सामाजिक व्यवस्था का परिचय देता है?",
            "opts": ["मंडल X", "मंडल IX", "मंडल III", "मंडल VII"],
            "sol": "पुरुष सूक्त मंडल X में पाया जाता है, जिसे ऋग्वेद में बाद का संकलन माना जाता है और इसमें पहली बार चार वर्णों का उल्लेख है।"
        },
        "The Battle of Ten Kings (Dasharajna Yuddha) was fought on the banks of which Vedic river?": {
            "q": "दस राजाओं का युद्ध (दाशराज्ञ युद्ध) किस वैदिक नदी के तट पर लड़ा गया था?",
            "opts": ["परुष्णी (रावी)", "विपासा (ब्यास)", "असिकनी (चिनाब)", "वितस्ता (झेलम)"],
            "sol": "यह युद्ध परुष्णी नदी (आधुनिक रावी) के तट पर लड़ा गया था जहाँ भरत कबीले के राजा सुदास ने दस राजाओं के संघ को हराया था।"
        },
        "The family books (oldest Mandalas) of the Rigveda are:": {
            "q": "ऋग्वेद की पारिवारिक पुस्तकें (सबसे पुराने मंडल) कौन से हैं?",
            "opts": ["मंडल II से VII", "मंडल I से VIII", "मंडल VIII से X", "मंडल IX और X"],
            "sol": "मंडल II से VII सबसे पुराने पारिवारिक मंडल हैं, जिनमें से प्रत्येक एक विशिष्ट ऋषि गोत्र जैसे विश्वामित्र, वशिष्ठ और वामदेव से जुड़े हैं।"
        },
        "The Rigvedic term 'Gavishti' refers to conflict or war, literally translating to:": {
            "q": "ऋग्वैदिक शब्द 'गविष्टि' संघर्ष या युद्ध को दर्शाता है, जिसका शाब्दिक अनुवाद है:",
            "opts": ["गायों की खोज", "भूमि की तलाश", "रथ युद्ध", "घोड़ों की दौड़"],
            "sol": "'गविष्टि' का शाब्दिक अर्थ 'गायों की खोज' है, जो ऋग्वैदिक समाज की पशुपालन प्रकृति को दर्शाता है जहां मवेशी प्राथमिक धन थे।"
        },
        "Which deity receives the maximum number of hymns in the Rigveda?": {
            "q": "ऋग्वेद में किस देवता को सबसे अधिक सूक्त समर्पित हैं?",
            "opts": ["इंद्र", "अग्नि", "वरुण", "सोम"],
            "sol": "इंद्र (जिन्हें पुरंदर या किलों को तोड़ने वाला भी कहा जाता है) को लगभग 250 सूक्त समर्पित हैं, इसके बाद अग्नि को लगभग 200 सूक्त समर्पित हैं।"
        },
        "The word 'Ganga' is mentioned only once in the Rigveda.": {
            "q": "ऋग्वेद में 'गंगा' शब्द का उल्लेख केवल एक बार किया गया है।",
            "sol": "सही। ऋग्वेद का भौगोलिक ध्यान सिंधु और उसकी सहायक नदियों पर था, गंगा का उल्लेख केवल बाद के १०वें मंडल में एक बार मिलता है।"
        },
        "The early Aryans practiced a highly developed urban lifestyle.": {
            "q": "प्रारंभिक आर्यों ने एक अत्यधिक विकसित शहरी जीवन शैली का पालन किया था।",
            "sol": "गलत। प्रारंभिक वैदिक समाज मुख्य रूप से ग्रामीण और पशुपालक (pastoral) था, न कि शहरी।"
        },
        "Indra was considered the lord of cosmic moral order (Rita).": {
            "q": "इंद्र को ब्रह्मांडीय नैतिक व्यवस्था (ऋत) का स्वामी माना जाता था।",
            "sol": "गलत। वरुण को ऋत (ब्रह्मांडीय नैतिक व्यवस्था) का रक्षक या स्वामी माना जाता था, जबकि इंद्र युद्ध और वर्षा के देवता थे।"
        },
        "Sarasvati was praised as the best and most sacred of all Vedic rivers.": {
            "q": "सरस्वती को सभी वैदिक नदियों में सबसे उत्तम और पवित्र नदी के रूप में सराहा गया था।",
            "sol": "सही। ऋग्वेद में सरस्वती नदी को 'नदीतमा' (नदियों में सर्वश्रेष्ठ) कहकर पूजा गया है।"
        },
        "The Rigveda contains 1,028 hymns in total.": {
            "q": "ऋग्वेद में कुल 1,028 सूक्त शामिल हैं।",
            "sol": "सही। ऋग्वेद संहिता में कुल 10 मंडलों में 1,028 सूक्त (बालखिल्य सूक्तों सहित) हैं।"
        },
        "Monogamy was the only form of marriage practiced during this period.": {
            "q": "इस अवधि के दौरान केवल एकपत्नी विवाह ही एकमात्र विवाह का रूप था।",
            "sol": "गलत। सामान्यतः एकपत्नी विवाह (monogamy) आदर्श था, लेकिन कुलीन और शाही परिवारों में बहुपत्नी विवाह (polygamy) के साक्ष्य भी मिलते हैं।"
        },
        "The Rigvedic assemblies Sabha and Samiti allowed women's participation.": {
            "q": "ऋग्वैदिक सभा और समिति जैसी संस्थाओं में महिलाओं की भागीदारी की अनुमति थी।",
            "sol": "सही। प्रारंभिक वैदिक काल में महिलाओं को सभा और विधात जैसी कबीलाई सभाओं में भाग लेने का अधिकार था।"
        },
        "Iron (Shyama Ayas) was extensively used in the Early Rigvedic economy.": {
            "q": "प्रारंभिक ऋग्वैदिक अर्थव्यवस्था में लोहे (श्याम अयस) का बड़े पैमाने पर उपयोग किया जाता था।",
            "sol": "गलत। प्रारंभिक ऋग्वैदिक काल में लोहे का ज्ञान नहीं था; वे केवल तांबे या कांसे (अयस) से परिचित थे। लोहे का उपयोग उत्तर वैदिक काल (लगभग 1000 ईसा पूर्व) में शुरू हुआ।"
        },
        "The cosmological hymn of creation in Rigveda Mandala X is called the __________ Sukta.": {
            "q": "ऋग्वेद के १०वें मंडल में ब्रह्मांडीय सृष्टि से संबंधित प्रसिद्ध सूक्त को __________ सूक्त कहा जाता है।",
            "sol": "सही उत्तर 'नासदीय' (Nasadiya) सूक्त है, जो सृष्टि की उत्पत्ति पर दार्शनिक विचार प्रस्तुत करता है।"
        },
        "The priest who recited hymns from the Rigveda was called the __________.": {
            "q": "ऋग्वेद के सूक्तों का पाठ करने वाले मुख्य पुरोहित को __________ कहा जाता था।",
            "sol": "सही उत्तर 'होता' (Hotri) है।"
        },
        "The Rigvedic name for the River Ravi was __________.": {
            "q": "रावी नदी का ऋग्वैदिक नाम __________ था।",
            "sol": "सही उत्तर 'परुष्णी' (Parushni) है।"
        },
        "The political head of the tribal community (Jana) was called the __________.": {
            "q": "जनजातीय समुदाय (जन) के राजनीतिक प्रमुख या राजा को __________ कहा जाता था।",
            "sol": "सही उत्तर 'राजन्' (Rajan) या 'गोपति' है।"
        },
        "The famous Gayatri Mantra is found in Mandala __________ of the Rigveda.": {
            "q": "प्रसिद्ध गायत्री मंत्र ऋग्वेद के __________ मंडल में पाया जाता. है।",
            "sol": "सही उत्तर 'तृतीय' (III) मंडल है, जिसकी रचना ऋषि विश्वामित्र ने की थी।"
        },
        "The Rigvedic term for a family lineage or clan was __________.": {
            "q": "पारिवारिक वंश या कुल के लिए प्रयुक्त ऋग्वैदिक शब्द __________ था।",
            "sol": "सही उत्तर 'कुल' या 'गृह' है।"
        },
        "The Vedic god of fire, who acted as a mediator between humans and gods, was __________.": {
            "q": "अग्नि के वैदिक देवता, जो मनुष्यों और देवताओं के बीच मध्यस्थ का कार्य करते थे, __________ थे।",
            "sol": "सही उत्तर 'अग्नि' (Agni) है।"
        },
        "The Soma Mandala, dedicated entirely to the ritual drink, is Mandala __________.": {
            "q": "अनुष्ठानिक पेय सोम को पूरी तरह से समर्पित मंडल, ऋग्वेद का __________ मंडल है।",
            "sol": "सही उत्तर 'नौवां' (IX) मंडल है।"
        },
        "Match the Rigvedic deities to their functional domains:": {
            "q": "ऋग्वैदिक देवताओं का उनके कार्यात्मक क्षेत्रों से मिलान करें:",
            "sol": "सही मिलान है: इंद्र (युद्ध और वर्षा), अग्नि (देवताओं के मध्यस्थ), और वरुण (ब्रह्मांडीय नैतिक व्यवस्था)।"
        },
        "Match the Rigvedic terms to their modern meanings:": {
            "q": "ऋग्वैदिक शब्दों का उनके आधुनिक अर्थों से मिलान करें:",
            "sol": "सही मिलान है: गविष्टि (गायों की खोज / युद्ध), जन (जनजातीय समूह), और नियोग (विधवा विवाह प्रथा)।"
        },
        "Match the Rigvedic rivers to their modern counterparts:": {
            "q": "ऋग्वैदिक नदियों का उनके आधुनिक समकक्षों से मिलान करें:",
            "sol": "सही मिलान है: वितस्ता (झेलम), असिकनी (चिनाब), और परुष्णी (रावी)।"
        },
        "Why is Mandala X of the Rigveda considered a later addition?": {
            "q": "ऋग्वेद के १०वें मंडल को बाद का संकलन क्यों माना जाता है?",
            "sol": "इसमें अधिक उन्नत दार्शनिक विचार (जैसे नासदीय सूक्त), चार वर्णों की व्यवस्थित सामाजिक व्यवस्था (पुरुष सूक्त) का वर्णन, और भाषा की भिन्नता दिखाई देती है जो पारिवारिक मंडलों से भिन्न है।"
        },
        "Why were cattle, particularly cows, the primary cause of conflict in the Rigvedic period?": {
            "q": "ऋग्वैदिक काल में मवेशी, विशेष रूप से गायें, संघर्ष का मुख्य कारण क्यों थीं?",
            "sol": "गाय प्राथमिक संपत्ति, विनिमय का माध्यम और भोजन का मुख्य स्रोत थीं। इसलिए कबीलों के बीच अधिकांश युद्ध गायों को हासिल करने (गविष्टि) के लिए लड़े जाते थे।"
        },
        "Why did assemblies like the Vidhata decline in importance over time?": {
            "q": "समय के साथ विधात जैसी प्राचीन सभाओं का महत्व क्यों कम हो गया?",
            "sol": "क्षेत्रीय राज्यों के उदय और अधिक जटिल वर्ग-विभाजित समाज के आने से, कबीलाई सभाओं का स्थान राजा की परिषद और केंद्रीकृत प्रशासनिक व्यवस्था ने ले लिया।"
        },
        "How did comparative philology help in establishing the chronological sequence of Rigvedic hymns?": {
            "q": "तुलनात्मक भाषाशास्त्र ने ऋग्वैदिक सूक्तों के कालानुक्रमिक अनुक्रम को स्थापित करने में कैसे मदद की?",
            "sol": "भाषा के ऐतिहासिक बदलावों, व्याकरणिक संरचनाओं और शब्दावली की तुलना करके विद्वानों ने प्राचीन पारिवारिक मंडलों (II-VII) और बाद में जोड़े गए मंडलों (I, X) के बीच अंतर स्पष्ट किया।"
        },
        "How did the role of the Rajan transition during the Rigvedic period?": {
            "q": "ऋग्वैदिक काल के दौरान राजा (Rajan) की भूमिका में क्या बदलाव आया?",
            "sol": "वह शुरू में कबीले द्वारा चुना गया एक अस्थायी युद्ध नेता था जिसकी शक्ति सीमित थी, जो धीरे-धीरे वंशानुगत राजा के रूप में परिवर्तित हो गया, जिसे बाद में धार्मिक अनुष्ठानों का समर्थन मिला।"
        },
        "How did the geography of the Rigveda indicate a northwest location for early Indo-Aryans?": {
            "q": "ऋग्वेद का भूगोल प्रारंभिक भारत-आर्यों के उत्तर-पश्चिम में निवास की पुष्टि कैसे करता है?",
            "sol": "सिंधु (Sindhu), कुभा (काबुल), सुवास्तु (स्वात) और पंजाब की पांच नदियों (सप्त-सिंधु क्षेत्र) के प्रमुख संदर्भों से पता चलता है कि वे भारत के उत्तर-पश्चिमी हिस्से में बसे थे।"
        },
        "Analyze the Battle of Ten Kings as a transition from simple clan feuds to larger confederate conflicts.": {
            "q": "दस राजाओं के युद्ध (दाशराज्ञ युद्ध) का विश्लेषण करें कि कैसे यह कबीलाई झगड़ों से बड़े गठबंधन संघर्ष में बदला।",
            "sol": "यह युद्ध राजा सुदास के भरत कबीले और दस अन्य प्रमुख कबीलों (पुरु, यदु, तुर्वसु आदि) के गठबंधन के बीच लड़ा गया था, जो जटिल सैन्य गठबंधनों और राजनीतिक नियंत्रण की शुरुआत को दर्शाता है।"
        },
        "Examine the Rigvedic transition from pastoralism to agriculture using Mandala VIII and X hymns.": {
            "q": "ऋग्वेद के ८वें और १०वें मंडल के सूक्तों के आधार पर पशुपालन से कृषि में परिवर्तन का परीक्षण करें।",
            "sol": "ऋग्वेद के बाद के हिस्सों में हल चलाने, बुवाई करने और फसलों की की जुताई से संबंधित कृषि शब्दावली का व्यापक उल्लेख मिलता है, जो शुरुआती पशुपालक जीवन से कृषि प्रधान जीवन की ओर बढ़ाव दिखाता है।"
        },
        "Investigate the role of Soma as both a plant and a deity in Mandala IX.": {
            "q": "ऋग्वेद के ९वें मंडल में सोम की एक औषधीय पौधे और देवता दोनों के रूप में भूमिका की जांच करें।",
            "sol": "सोम पवमान को एक पवित्र अनुष्ठानिक पेय के रूप में दर्शाया गया है जो ऊर्जा देता था, और साथ ही उसे एक दिव्य देवता का रूप देकर पूजा गया, जो प्रकृति के साथ वैदिक जुड़ाव को दर्शाता है।"
        },
        "Explain the concept of 'Rita' (cosmic moral order) to a beginner, and how it differs from dharma.": {
            "q": "एक शुरुआती छात्र को 'ऋत' (Rita - ब्रह्मांडीय नैतिक व्यवस्था) की अवधारणा समझाएं और यह भी बताएं कि यह धर्म से कैसे भिन्न है।",
            "sol": "ऋत वह प्राकृतिक और नैतिक कानून है जो ब्रह्मांड की व्यवस्था (जैसे ऋतुओं का बदलना, सूर्य-चंद्र की गति) बनाए रखता है। बाद में विकसित हुआ 'धर्म' सामाजिक कर्तव्यों, व्यक्तिगत आचरण और कानून को संदर्भित करता है।"
        },
        "Summarize the difference between the 'Family Books' and the later additions of the Rigveda.": {
            "q": "ऋग्वेद की 'पारिवारिक पुस्तकों' और बाद में जोड़े गए मंडलों के बीच अंतर का संक्षेप में वर्णन करें।",
            "sol": "पारिवारिक पुस्तकें (मंडल २-७) सबसे पुरानी हैं और विशिष्ट ऋषियों के परिवारों द्वारा रचित हैं। बाद के मंडल (१, ८, ९, १०) अधिक दार्शनिक हैं, विस्तृत सामाजिक वर्गीकरण दिखाते हैं और उनका भौगोलिक क्षेत्र अधिक पूर्व की ओर है।"
        },
        "Briefly explain the functions of the Sabha and Samiti assemblies in Rigvedic polity.": {
            "q": "ऋग्वैदिक राजनीतिक व्यवस्था में सभा और समिति नामक संस्थाओं के कार्यों की संक्षेप में व्याख्या करें।",
            "sol": "सभा कबीले के बुजुर्गों और कुलीनों की एक छोटी परिषद थी जिसके न्यायिक कार्य भी थे। समिति पूरे कबीले की एक बड़ी आम सभा थी जो राजा के चुनाव और सैन्य मामलों का निर्णय करती थी।"
        },

        # --- Section 2: Later Samhitas ---
        "Which Later Vedic text contains charms, spells, and magic formulas to ward off evil?": {
            "q": "किस उत्तर वैदिक ग्रंथ में बुराई को दूर करने के लिए ताबीज, मंत्र और जादुई सूत्र शामिल हैं?",
            "opts": ["अथर्ववेद", "सामवेद", "यजुर्वेद", "ऋग्वेद"],
            "sol": "अथर्ववेद जादू और मंत्रों का वेद है, जो लोक विश्वासों और बीमारियों के इलाज का दस्तावेजीकरण करता है।"
        },
        "The Samaveda consists mostly of hymns taken from which text, set to musical melodies?": {
            "q": "सामवेद में मुख्य रूप से किस ग्रंथ से लिए गए सूक्त शामिल हैं, जिन्हें संगीतमय धुनों में पिरोया गया है?",
            "opts": ["ऋग्वेद", "यजुर्वेद", "अथर्ववेद", "ऐतरेय ब्राह्मण"],
            "sol": "सामवेद के लगभग सभी 1,549 छंद ऋग्वेद से लिए गए हैं और संगीत के लिए निर्धारित किए गए हैं।"
        },
        "The Yajurveda is primarily a book of:": {
            "q": "यजुर्वेद मुख्य रूप से किस विषय की पुस्तक है?",
            "opts": ["यज्ञीय सूत्र और कर्मकांड", "संगीतमय मंत्र", "औषधीय जड़ी-बूटियाँ", "ब्रह्मांडीय दर्शन"],
            "sol": "यजुर्वेद में अध्वर्यु पुरोहित द्वारा पढ़े जाने वाले गद्य अनुष्ठान सूत्र शामिल हैं।"
        },
        "Which recension belongs to the Shukla (White) Yajurveda?": {
            "q": "कौन सी संहिता शुक्ल यजुर्वेद से संबंधित है?",
            "opts": ["वाजसनेयी संहिता", "तैत्तिरीय संहिता", "काठक संहिता", "मैत्रायणी संहिता"],
            "sol": "वाजसनेयी शुक्ल यजुर्वेद की संहिता है, जबकि तैत्तिरीय कृष्ण यजुर्वेद की है।"
        },
        "What term is used in the Atharvaveda to denote iron?": {
            "q": "लोहे को दर्शाने के लिए अथर्ववेद में किस शब्द का प्रयोग किया गया है?",
            "opts": ["श्याम अयस", "लोह अयस", "कृष्ण अयस", "श्याम और कृष्ण अयस दोनों"],
            "sol": "अथर्ववेद लोहे को 'श्याम अयस' या 'कृष्ण अयस' (काली धातु) कहता है, जो इसके आगमन को दर्शाता है।"
        },
        "The Atharvaveda was considered part of the original Trayi Vidya.": {
            "q": "अथर्ववेद को मूल त्रयी विद्या का हिस्सा माना जाता था।",
            "sol": "गलत। मूल तीन वेदों (ऋग, साम, यजु) को त्रयी विद्या कहा जाता था। अथर्ववेद को बाद में वेद के रूप में शामिल किया गया था।"
        },
        "The Yajurveda is written in both verse and prose.": {
            "q": "यजुर्वेद पद्य और गद्य दोनों में लिखा गया है।",
            "sol": "सही। कृष्ण यजुर्वेद में मंत्रों के साथ-साथ गद्य में व्याख्याएं भी शामिल हैं।"
        },
        "The Samaveda is the foundational source for classical Indian music.": {
            "q": "सामवेद शास्त्रीय भारतीय संगीत का मूलभूत स्रोत है।",
            "sol": "सही। सामवेद के मंत्रों के संगीतमय गायन ने भारतीय संगीत के सप्त स्वरों के विकास में योगदान दिया।"
        },
        "The Later Samhitas reflect a highly mobile pastoral nomadic lifestyle.": {
            "q": "उत्तर वैदिक संहिताएं अत्यधिक गतिशील पशुपालक खानाबदोश जीवन शैली को दर्शाती हैं।",
            "sol": "गलत। उत्तर वैदिक काल में लोग कृषि आधारित बसे हुए जीवन की ओर बढ़ रहे थे, कबीले अब क्षेत्रीय राज्यों (जनपदों) का रूप ले रहे थे।"
        },
        "The Atharvaveda contains no references to medicine or diseases.": {
            "q": "अथर्ववेद में चिकित्सा या बीमारियों का कोई संदर्भ नहीं है।",
            "sol": "गलत। अथर्ववेद में रोगों के निदान, जड़ी-बूटियों के उपयोग और उपचार संबंधी मंत्रों का व्यापक वर्णन है, जिसे आयुर्वेद का आधार माना जाता है।"
        },
        "The Yajurveda is divided into Krishna and Shukla recensions.": {
            "q": "यजुर्वेद कृष्ण और शुक्ल शाखाओं में विभाजित है।",
            "sol": "सही। यजुर्वेद के दो भाग हैं - शुक्ल (श्वेत) और कृष्ण (श्वेत और श्याम मिश्रित)।"
        },
        "Later Vedic society saw the emergence of territorial states (Janapadas).": {
            "q": "उत्तर वैदिक समाज में क्षेत्रीय राज्यों (जनपदों) का उदय हुआ।",
            "sol": "सही। इस काल में कुरू, पांचाल जैसे बड़े क्षेत्रीय राज्यों का गठन हुआ।"
        },
        "The Atharvaveda was composed in the Early Vedic Sapta-Sindhu core.": {
            "q": "अथर्ववेद की रचना प्रारंभिक वैदिक सप्त-सिंधु क्षेत्र में हुई थी।",
            "sol": "गलत। इसकी रचना उत्तर वैदिक काल में हुई जब आर्यों का विस्तार गंगा-यमुना दोआब और पूर्वी क्षेत्रों की ओर हो गया था।"
        },
        "The Veda of melodies and chants is the __________.": {
            "q": "धुनों और भजनों का वेद __________ है।",
            "sol": "सही उत्तर 'सामवेद' (Samaveda) है।"
        },
        "The priest associated with the Yajurveda rituals was the __________.": {
            "q": "यजुर्वेद के अनुष्ठानों से जुड़े पुरोहित __________ थे।",
            "sol": "सही उत्तर 'अध्वर्यु' (Adhvaryu) है।"
        },
        "The priest representing the Atharvaveda who supervised the sacrifice was the __________.": {
            "q": "अथर्ववेद का प्रतिनिधित्व करने वाले पुरोहित जिन्होंने यज्ञ की देखरेख की, __________ थे।",
            "sol": "सही उत्तर 'ब्रह्मा' (Brahma) है।"
        },
        "The Black Yajurveda is also known as the __________ Samhita.": {
            "q": "कृष्ण यजुर्वेद को __________ संहिता के रूप में भी जाना जाता है।",
            "sol": "सही उत्तर 'तैत्तिरीय' (Taittiriya) संहिता है।"
        },
        "The White Yajurveda is also known as the __________ Samhita.": {
            "q": "शुक्ल यजुर्वेद को __________ संहिता के रूप में भी जाना जाता है।",
            "sol": "सही उत्तर 'वाजसनेयी' (Vajasaneyi) संहिता है।"
        },
        "The metal 'Shyama Ayas' refers to __________.": {
            "q": "धातु 'श्याम अयस' __________ को संदर्भित करती है।",
            "sol": "सही उत्तर 'लोहा' (Iron) है।"
        },
        "The Vedic sacrifice consisting of a chariot race to rejuvenate the king's power was the __________.": {
            "q": "राजा की शक्ति को पुनः प्राप्त करने के लिए रथ दौड़ वाले वैदिक यज्ञ को __________ कहा जाता था।",
            "sol": "सही उत्तर 'वाजपेय' (Vajapeya) यज्ञ है।"
        },
        "The Atharvaveda contains __________ books (kandas) in total.": {
            "q": "अथर्ववेद में कुल __________ अध्याय (काण्ड) हैं।",
            "sol": "सही उत्तर '20' (बीस) है।"
        },
        "Match the Vedas to their associated priests:": {
            "q": "वेदों का उनके संबंधित पुरोहितों से मिलान करें:",
            "sol": "सही मिलान है: ऋग्वेद (होता), सामवेद (उद्गाता), और यजुर्वेद (अध्वर्यु)।"
        },
        "Match the Samhitas to their main themes:": {
            "q": "संहिताओं का उनके मुख्य विषयों से मिलान करें:",
            "sol": "सही मिलान है: सामवेद (धुनें), यजुर्वेद (यज्ञीय सूत्र), और अथर्ववेद (जादू और चिकित्सा)।"
        },
        "Match Later Vedic terms to meanings:": {
            "q": "उत्तर वैदिक शब्दों का अर्थों से मिलान करें:",
            "sol": "सही मिलान है: राजसूय (राज्याभिषेक), अश्वमेध (घोड़े की बलि), और वाजपेय (रथ दौड़)।"
        },
        "Why is the Atharvaveda considered distinct from the other three Vedas?": {
            "q": "अथर्ववेद को अन्य तीन वेदों से भिन्न क्यों माना जाता है?",
            "sol": "यह बड़े यज्ञीय कर्मकांडों के बजाय आम लोगों के जीवन, रोगों के उपचार, जादू-टोने, जड़ी-बूटियों और लोक विश्वासों पर केंद्रित है।"
        },
        "Why did the Yajurveda introduce complex sacrifices like the Ashvamedha?": {
            "q": "यजुर्वेद में अश्वमेध जैसे जटिल यज्ञों की शुरुआत क्यों की गई?",
            "sol": "बढ़ती कृषि अर्थव्यवस्था में क्षेत्रीय राजा (Rajan) की राजनीतिक सर्वोच्चता, संप्रभुता और कबीलों पर उसके नियंत्रण को धार्मिक वैधता प्रदान करने के लिए।"
        },
        "Why did iron (Shyama Ayas) lead to the clearing of the Gangetic plains?": {
            "q": "लोहे (श्याम अयस) ने गंगा के मैदानों को साफ करने में मदद क्यों की?",
            "sol": "लोहे की कुल्हाड़ियों और हलों ने गंगा घाटी के घने जंगलों को साफ करने और वहां की भारी दोमट मिट्टी की गहरी जुताई को संभव बनाया, जिससे कृषि का प्रसार हुआ।"
        },
        "How does the Atharvaveda help in reconstructing the early history of Indian sciences?": {
            "q": "अथर्ववेद प्राचीन भारतीय विज्ञान के प्रारंभिक इतिहास के पुनर्निर्माण में कैसे मदद करता है?",
            "sol": "इसमें विभिन्न रोगों के लक्षणों, शरीर रचना के प्राथमिक ज्ञान और जड़ी-बूटियों के औषधीय गुणों का विवरण है, जो आयुर्वेद के विकास का प्रारंभिक चरण है।"
        },
        "How did the transition to agriculture modify the tax system in the Later Samhitas?": {
            "q": "कृषि की ओर संक्रमण ने उत्तर वैदिक संहिताओं में कर प्रणाली को कैसे बदल दिया?",
            "sol": "प्रारंभिक काल का स्वैच्छिक उपहार (Bali) अब एक अनिवार्य नियमित कर में बदल गया, जिसे इकट्ठा करने के लिए 'भागदुघ' (कर संग्रहकर्ता) जैसे अधिकारी नियुक्त किए गए।"
        },
        "How does the Samaveda relate to the performance of Soma sacrifice?": {
            "q": "सामवेद का सोम यज्ञ के संपादन से क्या संबंध है?",
            "sol": "सोम यज्ञ के दौरान सोम रस के शुद्धिकरण और आहुति के समय उद्गाता पुरोहितों द्वारा गाए जाने वाले मंत्रों और संगीतमय धुनों का संग्रह ही सामवेद है।"
        },
        "Analyze the geographical shift from Sapta-Sindhu to Kuru-Panchala land in the Later Samhitas.": {
            "q": "उत्तर वैदिक संहिताओं में सप्त-सिंधु से कुरु-पांचाल क्षेत्र की ओर भौगोलिक खिसकाव का विश्लेषण करें।",
            "sol": "गंगा, यमुना और कुरुक्षेत्र जैसे पूर्वी क्षेत्रों के बार-बार उल्लेख से पता चलता है कि वैदिक सभ्यता का केंद्र पंजाब से हटकर गंगा-यमुना दोआब (पश्चिमी उत्तर प्रदेश/हरियाणा) की ओर स्थानांतरित हो गया था।"
        },
        "Examine the role of the Ratnins (jewel-bearers) in Later Vedic coronation ceremonies.": {
            "q": "उत्तर वैदिक काल के राज्याभिषेक समारोहों में रत्नियों (Ratnins) की भूमिका का परीक्षण करें।",
            "sol": "राजा राज्याभिषेक के समय १२ रत्नियों (जैसे रानी, सेनानी, सूत, भागदुघ) के घर जाकर उनका समर्थन प्राप्त करता था, जो दर्शाता है कि राजतंत्र अभी पूर्ण रूप से निरंकुश नहीं था।"
        },
        "Investigate the impact of rice cultivation (Vrihi) on Later Vedic agrarian settlements.": {
            "q": "उत्तर वैदिक काल की बस्तियों पर धान की खेती (Vrihi) के प्रभाव की जांच करें।",
            "sol": "धान की खेती के लिए अधिक श्रम और एक जगह टिककर काम करने की आवश्यकता थी। इसने लोगों को खानाबदोश जीवन छोड़कर स्थायी गांवों में बसने के लिए प्रेरित किया।"
        },
        "Explain the concept of 'Trayi' (the triple Veda) and why Atharvaveda was initially excluded.": {
            "q": "त्रयी (Trayi) की अवधारणा समझाएं और बताएं कि अथर्ववेद को शुरू में इससे बाहर क्यों रखा गया था।",
            "sol": "त्रयी में ऋग, साम और यजु वेद शामिल हैं क्योंकि वे मुख्य यज्ञ अनुष्ठानों से जुड़े हैं। अथर्ववेद को इसलिए बाहर रखा गया क्योंकि इसमें यज्ञों के बजाय लोक-जादू और रोजमर्रा की सांसारिक समस्याओं के मंत्र शामिल थे।"
        },
        "Explain the significance of 'Shyama Ayas' in the Later Vedic economy.": {
            "q": "उत्तर वैदिक अर्थव्यवस्था में 'श्याम अयस' के महत्व को समझाएं।",
            "sol": "श्याम अयस (लोहा) ने कृषि उपकरणों (जैसे हल के फाल) और जंगलों को साफ करने की कुल्हाड़ियों का निर्माण सुलभ किया, जिससे उत्पादन अधिशेष (surplus) बढ़ा और बस्तियों का तेजी से विस्तार हुआ।"
        },
        "Explain the difference between Black (Krishna) and White (Shukla) Yajurveda.": {
            "q": "कृष्ण यजुर्वेद और शुक्ल यजुर्वेद के बीच अंतर को स्पष्ट करें।",
            "sol": "कृष्ण यजुर्वेद में मूल मंत्रों के साथ-साथ अनुष्ठानों की गद्यात्मक व्याख्या भी मिश्रित है, जबकि शुक्ल यजुर्वेद में केवल मूल मंत्र (वाजसनेयी संहिता) संकलित हैं।"
        },

        # --- Section 3: Brahmanas, Aranyakas & Upanishads ---
        "Which Brahmana text describes the legend of Videgha Mathava and the spread of Vedic culture to eastern India?": {
            "q": "कौन सा ब्राह्मण ग्रंथ विदेघ माथव की कथा और पूर्वी भारत में वैदिक संस्कृति के प्रसार का वर्णन करता है?",
            "opts": ["शतपथ ब्राह्मण", "ऐतरेय ब्राह्मण", "तैत्तिरीय ब्राह्मण", "गोपथ ब्राह्मण"],
            "sol": "शतपथ ब्राह्मण विदेघ माथव द्वारा सदानीरा (गंडक) नदी के पार अग्नि वैश्वानर को ले जाने के प्रवास का विवरण देता है।"
        },
        "The national motto 'Satyameva Jayate' is taken from which Upanishad?": {
            "q": "राष्ट्रीय आदर्श वाक्य 'सत्यमेव जयते' किस उपनिषद से लिया गया है?",
            "opts": ["मुण्डक उपनिषद", "छान्दोग्य उपनिषद", "कठोपनिषद", "माण्डूक्य उपनिषद"],
            "sol": "सत्यमेव जयते (केवल सत्य की विजय होती है) मुण्डक उपनिषद से लिया गया है।"
        },
        "Which Upanishad features the famous conversation between Nachiketa and Yama (the god of death)?": {
            "q": "किस उपनिषद में नचिकेता और यम (मृत्यु के देवता) के बीच प्रसिद्ध संवाद है?",
            "opts": ["कठोपनिषद", "बृहदारण्यक उपनिषद", "ईशोपनिषद", "केनोपनिषद"],
            "sol": "कठोपनिषद में आत्मा और मृत्यु की प्रकृति पर नचिकेता का संवाद शामिल है।"
        },
        "Which is the largest and one of the oldest Upanishads?": {
            "q": "सबसे बड़ा और सबसे पुराने उपनिषदों में से एक कौन सा है?",
            "opts": ["बृहदारण्यक उपनिषद", "छान्दोग्य उपनिषद", "तैत्तिरीय उपनिषद", "श्वेताश्वतर उपनिषद"],
            "sol": "शुक्ल यजुर्वेद से जुड़ा बृहदारण्यक उपनिषद सबसे बड़ा है।"
        },
        "What is the primary theme of the Upanishads?": {
            "q": "उपनिषदों का मुख्य विषय क्या है?",
            "opts": ["आत्मन और ब्रह्म की दार्शनिक खोज", "गृहस्थों के नियम", "यज्ञीय कर्मकांड", "औषधीय पौधे और रसायन शास्त्र"],
            "sol": "उपनिषद आत्मा (Atman) और सार्वभौमिक सत्य (Brahman) के ज्ञान पर ध्यान केंद्रित करते हैं, जो कर्मकांडों की सर्वोच्चता के अंत का प्रतीक है।"
        },
        "Brahmanas are prose manuals explaining sacrificial rituals.": {
            "q": "ब्राह्मण यज्ञीय कर्मकांडों की व्याख्या करने वाले गद्य ग्रंथ हैं।",
            "sol": "सही। ब्राह्मण ग्रंथों की रचना संहिताओं के जटिल अनुष्ठानों को गद्य में विस्तार से समझाने के लिए की गई थी।"
        },
        "The Aranyakas are also called forest books.": {
            "q": "आरण्यकों को वन पुस्तकें भी कहा जाता है।",
            "sol": "सही। आरण्यक का अर्थ वन से है; ये ग्रंथ जंगलों में रहने वाले संन्यासियों और शिष्यों के चिंतन और दार्शनिक विषयों पर आधारित हैं।"
        },
        "The Upanishads fully support the performance of grand animal sacrifices.": {
            "q": "उपनिषद बड़े पैमाने पर पशु बलि के प्रदर्शन का पूरी तरह से समर्थन करते हैं।",
            "sol": "गलत। उपनिषद बाहरी कर्मकांडों और पशु बलि की आलोचना करते हैं और उनके स्थान पर आंतरिक ज्ञान और ध्यान पर बल देते हैं।"
        },
        "The Shatapatha Brahmana is associated with the Rigveda.": {
            "q": "शतपथ ब्राह्मण ऋग्वेद से जुड़ा हुआ है।",
            "sol": "गलत। शतपथ ब्राह्मण यजुर्वेद (विशेष रूप से शुक्ल यजुर्वेद) से जुड़ा है। ऋग्वेद का मुख्य ब्राह्मण ऐतरेय है।"
        },
        "Gopatha Brahmana is the only Brahmana of the Atharvaveda.": {
            "q": "गोपथ ब्राह्मण अथर्ववेद का एकमात्र ब्राह्मण ग्रंथ है।",
            "sol": "सही। गोपथ ब्राह्मण अथर्ववेद की एकमात्र गद्यात्मक ब्राह्मण व्याख्या है।"
        },
        "The Upanishads are part of the Smriti literature.": {
            "q": "उपनिषद स्मृति साहित्य का हिस्सा हैं।",
            "sol": "गलत। उपनिषद श्रुति (Shruti) साहित्य का हिस्सा हैं, जो वैदिक परंपरा के सबसे प्रामाणिक ग्रंथ माने जाते हैं।"
        },
        "The Chandogya Upanishad contains the story of Satyakama Jabala.": {
            "q": "छान्दोग्य उपनिषद में सत्यकाम जाबाल की कहानी शामिल है।",
            "sol": "सही। इसमें सत्यकाम जाबाल की कहानी है जिसने अपनी माता के नाम पर ज्ञान प्राप्त करने की खोज की।"
        },
        "Upanishadic philosophy was mostly developed in the Indus valley.": {
            "q": "उपनिषदों का दर्शन मुख्यतः सिंधु घाटी में विकसित हुआ था।",
            "sol": "गलत। उपनिषदों का अधिकांश दार्शनिक विचार गंगा घाटी (जैसे काशी, विदेह, पांचाल) में विकसित हुआ था।"
        },
        "The Shatapatha Brahmana is associated with the __________ Yajurveda.": {
            "q": "शतपथ ब्राह्मण __________ यजुर्वेद से जुड़ा हुआ है।",
            "sol": "सही उत्तर 'शुक्ल' (Shukla) यजुर्वेद है।"
        },
        "The phrase 'Aham Brahmasmi' is found in the __________ Upanishad.": {
            "q": "वाक्य 'अहं ब्रह्मास्मि' __________ उपनिषद में पाया जाता है।",
            "sol": "सही उत्तर 'बृहदारण्यक' (Brihadaranyaka) उपनिषद है।"
        },
        "The transitional texts between Brahmanas and Upanishads are the __________.": {
            "q": "ब्राह्मणों और उपनिषदों के बीच के संक्रमणकालीन ग्रंथ __________ हैं।",
            "sol": "सही उत्तर 'आरण्यक' (Aranyakas) हैं।"
        },
        "The sole Brahmana of the Atharvaveda is the __________.": {
            "q": "अथर्ववेद का एकमात्र ब्राह्मण ग्रंथ __________ है।",
            "sol": "सही उत्तर 'गोपथ' (Gopatha) ब्राह्मण है।"
        },
        "The Upanishads are also known as __________.": {
            "q": "उपनिषदों को __________ के रूप में भी जाना जाता है।",
            "sol": "सही उत्तर 'वेदांत' (Vedanta) है क्योंकि ये वेदों का अंतिम भाग और उनका दार्शनिक निष्कर्ष हैं।"
        },
        "The river Sadanira mentioned in the Shatapatha Brahmana corresponds to modern __________.": {
            "q": "शतपथ ब्राह्मण में उल्लिखित सदानीरा नदी आधुनिक __________ के समान है।",
            "sol": "सही उत्तर 'गंडक' (Gandak) नदी है।"
        },
        "The scholar seers who debated in the court of King Janaka included Yajnavalkya and the female scholar __________.": {
            "q": "राजा जनक के दरबार में बहस करने वाले विद्वान ऋषियों में याज्ञवल्क्य और महिला विदुषी __________ शामिल थीं।",
            "sol": "सही उत्तर 'गार्गी' (Gargi) वाचक्नवी है।"
        },
        "The Aitareya Brahmana belongs to the __________ Veda.": {
            "q": "ऐतरेय ब्राह्मण __________ वेद से संबंधित है।",
            "sol": "सही उत्तर 'ऋग्वेद' (Rigveda) है।"
        },
        "Match Brahmanas to Vedas:": {
            "q": "ब्राह्मणों का वेदों से मिलान करें:",
            "sol": "सही मिलान है: ऐतरेय ब्राह्मण (ऋग्वेद), शतपथ ब्राह्मण (यजुर्वेद), और गोपथ ब्राह्मण (अथर्ववेद)।"
        },
        "Match Upanishads to famous quotes/legends:": {
            "q": "उपनिषदों का प्रसिद्ध कथनों/कथाओं से मिलान करें:",
            "sol": "सही मिलान है: मुण्डक (सत्यमेव जयते), कठोपनिषद (नचिकेता-यम), और छान्दोग्य (तत् त्वम असि)।"
        },
        "Match literary categories to styles:": {
            "q": "साहित्यिक श्रेणियों का शैलियों से मिलान करें:",
            "sol": "सही मिलान है: संहिताएं (मुख्य सूक्त/मंत्र), ब्राह्मण (कर्मकांडीय गद्य व्याख्याएं), और उपनिषद (दार्शनिक संवाद)।"
        },
        "Why did the Aranyakas focus on symbolic interpretations rather than actual sacrifices?": {
            "q": "आरण्यकों ने वास्तविक यज्ञों के बजाय प्रतीकात्मक व्याख्याओं पर क्यों ध्यान केंद्रित किया?",
            "sol": "वे वन में रहने वाले संन्यासियों के लिए लिखे गए थे जिनके पास बड़े यज्ञों के लिए आवश्यक सामग्री उपलब्ध नहीं थी। उन्होंने बाह्य अनुष्ठानों का मानसिक रूपक प्रस्तुत किया।"
        },
        "Why is the legend of Videgha Mathava crucial for tracing ancient geography?": {
            "q": "प्राचीन भूगोल को समझने के लिए विदेघ माथव की कथा क्यों महत्वपूर्ण है?",
            "sol": "यह पंजाब/हरियाणा से पूर्व की ओर बिहार (सदानीरा नदी) तक वैदिक संस्कृति और कृषि बस्तियों के प्रसार की ऐतिहासिक यात्रा को दर्शाती है।"
        },
        "Why do Upanishads criticize Brahmanical ritual sacrifices as 'leaky boats'?": {
            "q": "उपनिषद ब्राह्मणवादी अनुष्ठानों और यज्ञों की आलोचना 'कमजोर नौकाओं' के रूप में क्यों करते हैं?",
            "sol": "मुण्डक उपनिषद के अनुसार, कर्मकांड अस्थायी फल देते हैं और वे जन्म-मृत्यु के चक्र से पूर्ण मुक्ति (मोक्ष) नहीं दिला सकते, जो केवल ज्ञान (Jnana) से ही संभव है।"
        },
        "How do the Brahmanas explain the political elevation of the Rajan?": {
            "q": "ब्राह्मण ग्रंथ राजा (Rajan) के राजनीतिक उत्थान की व्याख्या कैसे करते हैं?",
            "sol": "वे राजसूय और वाजपेय जैसे यज्ञों की गद्यात्मक व्याख्या करके राजा को दिव्य शक्तियों से जोड़ते हैं, जिससे समाज में राजशाही की शक्ति को मान्यता मिलती है।"
        },
        "How did the Upanishads contribute to the rise of Buddhism and Jainism?": {
            "q": "उपनिषदों ने बौद्ध और जैन धर्म के उदय में कैसे योगदान दिया?",
            "sol": "बाहरी कर्मकांडों, पुरोहितों के वर्चस्व और पशु बलि की तीखी आलोचना करके उन्होंने उन दार्शनिक आधारों का निर्माण किया, जिन्होंने बाद में नास्तिक (heterodox) आंदोलनों को प्रेरित किया।"
        },
        "How does the concept of Transmigration of Soul (Samsara) appear in the early Upanishads?": {
            "q": "शुरुआती उपनिषदों में आत्मा के पुनर्जन्म (संसार) की अवधारणा कैसे दिखाई देती है?",
            "sol": "बृहदारण्यक और छान्दोग्य उपनिषद में पहली बार कर्म के सिद्धांत को पुनर्जन्म के चक्र से जोड़ा गया है, जिसके अनुसार व्यक्ति का कर्म उसके अगले जन्म का निर्धारण करता है।"
        },
        "Analyze the court debates of King Janaka of Videha in the Brihadaranyaka Upanishad.": {
            "q": "बृहदारण्यक उपनिषद में वर्णित विदेह के राजा जनक के दरबार में होने वाली दार्शनिक बहसों का विश्लेषण करें।",
            "sol": "यह दिखाता है कि विदेह उस काल में दार्शनिक विमर्श का मुख्य केंद्र था, जहां याज्ञवल्क्य जैसे ऋषियों द्वारा आत्मा की प्रकृति पर बहस की जाती थी और उन्हें राजकीय संरक्षण प्राप्त था।"
        },
        "Examine the agricultural transitions mentioned in the Shatapatha Brahmana.": {
            "q": "शतपथ ब्राह्मण में उल्लिखित कृषि परिवर्तनों का परीक्षण करें।",
            "sol": "इसमें हल चलाने के लिए ६, ८, १२ और २४ बैलों को एक साथ जोतने का उल्लेख है, जो उत्तर वैदिक काल में बड़े पैमाने पर की जाने वाली गहरी जुताई और उन्नत खेती को दर्शाता है।"
        },
        "Investigate the role of Gargi Vachaknavi in the philosophical challenges to Yajnavalkya.": {
            "q": "याज्ञवल्क्य को दार्शनिक चुनौती देने में गार्गी वाचक्नवी की भूमिका की जांच करें।",
            "sol": "जनक के दरबार में गार्गी द्वारा याज्ञवल्क्य से ब्रह्मांड की उत्पत्ति पर पूछे गए तीखे सवाल दर्शाते हैं कि उपनिषद काल में महिलाओं का बौद्धिक स्तर बहुत ऊंचा था।"
        },
        "Explain the Upanishadic formula 'Tat Tvam Asi' (Thou Art That).": {
            "q": "उपनिषद के प्रसिद्ध महावाक्य 'तत् त्वम असि' (Tat Tvam Asi) की व्याख्या करें।",
            "sol": "इसका अर्थ है 'वह तुम ही हो' - अर्थात प्रत्येक व्यक्तिगत आत्मा (Atman) मूल रूप से परम सत्य या ब्रह्मांडीय चेतना (Brahman) का ही हिस्सा है।"
        },
        "Explain the division of the Vedic corpus into Karma-kanda and Jnana-kanda.": {
            "q": "वैदिक साहित्य के कर्मकांड (Karma-kanda) और ज्ञानकांड (Jnana-kanda) में विभाजन को स्पष्ट करें।",
            "sol": "कर्मकांड (संहिताएं और ब्राह्मण) में यज्ञों, प्रार्थनाओं और बाह्य अनुष्ठानों पर जोर दिया गया है, जबकि ज्ञानकांड (उपनिषद) में आंतरिक दर्शन और आत्म-ज्ञान पर बल दिया गया है।"
        },
        "Summarize the significance of the migration story of Videgha Mathava.": {
            "q": "विदेघ माथव की पूर्व की ओर यात्रा की कथा के ऐतिहासिक महत्व का संक्षेप में वर्णन करें।",
            "sol": "यह कहानी अग्नि (अग्नि वैश्वानर) की सहायता से उत्तर-पश्चिम से जंगलों को जलाते हुए सदा नीरा (गंडक नदी) तक भूमि साफ करने और आर्य संस्कृति के पूर्व की ओर प्रसार की गवाही देती है।"
        },

        # --- Section 4: Vedangas ---
        "Which Vedanga deals with the rules of Vedic pronunciation and phonetics?": {
            "q": "कौन सा वेदांग वैदिक उच्चारण और ध्वन्यात्मकता (phonetics) के नियमों से संबंधित है?",
            "opts": ["शिक्षा", "व्याकरण", "निरुक्त", "कल्प"],
            "sol": "शिक्षा वेद का वह अंग है जो ध्वन्यात्मकता और सही उच्चारण से संबंधित है।"
        },
        "Yaska's Nirukta is the earliest Indian treatise on:": {
            "q": "यास्क का निरुक्त किस विषय पर सबसे प्रारंभिक भारतीय ग्रंथ है?",
            "opts": ["व्युत्पत्तिशास्त्र और भाषाविज्ञान", "व्याकरण के नियम", "यज्ञीय कर्मकांडीय नियम", "खगोल विज्ञान और कैलेंडर"],
            "sol": "यास्क का निरुक्त (लगभग 5वीं-6ठी शताब्दी ईसा पूर्व) व्युत्पत्तिशास्त्र पर सबसे पुराना जीवित ग्रंथ है।"
        },
        "The Shulba Sutras, containing ancient Indian geometric rules, belong to which Vedanga?": {
            "q": "प्राचीन भारतीय ज्यामितीय नियमों वाले शुल्ब सूत्र किस वेदांग के अंतर्गत आते हैं?",
            "opts": ["कल्प", "ज्योतिष", "छंद", "व्याकरण"],
            "sol": "शुल्ब सूत्र कल्प सूत्रों का हिस्सा हैं, जो यज्ञ वेदियों के निर्माण का वर्णन करते हैं।"
        },
        "Who is the author of the Vyakarana Vedanga standard text, the Ashtadhyayi?": {
            "q": "व्याकरण वेदांग के मानक ग्रंथ अष्टाध्यायी के लेखक कौन हैं?",
            "opts": ["पाणिनी", "पतंजलि", "यास्क", "पिंगल"],
            "sol": "पाणिनी ने संस्कृत व्याकरण (व्याकरण) के मानक ग्रंथ अष्टाध्यायी की रचना की थी।"
        },
        "The Vedanga Jyotisha, attributed to Lagadha, deals with:": {
            "q": "लगध द्वारा रचित वेदांग ज्योतिष किससे संबंधित है?",
            "opts": ["खगोल विज्ञान और कैलेंडर गणना", "यज्ञीय वास्तुकला", "छंदबद्ध संरचनाएं", "उच्चारण के नियम"],
            "sol": "वेदांग ज्योतिष खगोल विज्ञान पर सबसे प्रारंभिक पाठ है, जिसका उपयोग यज्ञों के सही समय की गणना के लिए किया जाता था।"
        },
        "Vyakarana is considered the mouth of the Veda.": {
            "q": "व्याकरण को वेद का मुख माना जाता है।",
            "sol": "सही। वेदांगों के रूपक वर्गीकरण में व्याकरण को वेद का 'मुख' (mouth) कहा गया है।"
        },
        "Panini's Ashtadhyayi is a Vedic text composed in 1500 BCE.": {
            "q": "पाणिनी की अष्टाध्यायी 1500 ईसा पूर्व में रचित एक वैदिक पाठ है।",
            "sol": "गलत। अष्टाध्यायी उत्तर-वैदिक काल के बाद (लगभग चौथी शताब्दी ईसा पूर्व) रचित एक शास्त्रीय संस्कृत व्याकरण ग्रंथ है, न कि १५०० ईसा पूर्व का वैदिक ग्रंथ।"
        },
        "Nirukta glosses difficult and obscure Vedic words.": {
            "q": "निरुक्त कठिन और अस्पष्ट वैदिक शब्दों की व्याख्या करता है।",
            "sol": "सही। यास्क का निरुक्त वैदिक भजनों के कठिन और पुराने शब्दों के अर्थ और उनकी उत्पत्ति को स्पष्ट करता है।"
        },
        "Dharma Sutras laid down the codes of social conduct.": {
            "q": "धर्म सूत्र सामाजिक आचरण के नियम निर्धारित करते हैं।",
            "sol": "सही। धर्म सूत्रों में वर्णों के कर्तव्य, सामाजिक नियम, कानून और राजा के कर्तव्यों (राजधर्म) को संहिताबद्ध किया गया है।"
        },
        "Pingala's Chandashastra deals with phonetic rules.": {
            "q": "पिंगल का छंदशास्त्र ध्वन्यात्मक नियमों से संबंधित है।",
            "sol": "गलत। पिंगल का छंदशास्त्र (Chandashastra) कविता के मीटर और छंद (metrics) से संबंधित है, जबकि ध्वन्यात्मकता शिक्षा वेदांग का हिस्सा है।"
        },
        "Vedanga Jyotisha contains horoscope predictions based on zodiac signs.": {
            "q": "वेदांग ज्योतिष में राशियों के आधार पर कुंडली की भविष्यवाणियां शामिल हैं।",
            "sol": "गलत। वेदांग ज्योतिष मुख्य रूप से खगोलीय पिंडों की गति के आधार पर यज्ञों के लिए सही कैलेंडर और तिथि (time) की गणना पर केंद्रित है, न कि ज्योतिषीय भविष्यफल पर।"
        },
        "Shulba Sutras are the earliest sources of Indian mathematics.": {
            "q": "शुल्ब सूत्र भारतीय गणित के सबसे प्रारंभिक स्रोत हैं।",
            "sol": "सही। शुल्ब सूत्रों में वेदियों के निर्माण के लिए ज्यामितीय प्रमेय और माप के नियम हैं, जो भारतीय गणित के विकास को दर्शाते हैं।"
        },
        "Pratishakhyas are phonetic works linked to specific Vedas.": {
            "q": "प्रातिशाख्य विशिष्ट वेदों से जुड़े ध्वन्यात्मक ग्रंथ हैं।",
            "sol": "सही। प्रत्येक वेद शाखा का अपना प्रातिशाख्य ग्रंथ होता है जो उसके वर्णों और उच्चारण के नियमों को स्पष्ट करता है।"
        },
        "The etymological Vedanga is called __________.": {
            "q": "व्युत्पत्तिशास्त्र से संबंधित वेदांग __________ कहलाता है।",
            "sol": "सही उत्तर 'निरुक्त' (Nirukta) है।"
        },
        "The author of the Sanskrit grammar work Ashtadhyayi was __________.": {
            "q": "संस्कृत व्याकरण ग्रंथ अष्टाध्यायी के लेखक __________ थे।",
            "sol": "सही उत्तर 'पाणिनी' (Panini) है।"
        },
        "The Shulba Sutras are associated with the __________ Vedanga.": {
            "q": "शुल्ब सूत्र __________ वेदांग से जुड़े हैं।",
            "sol": "सही उत्तर 'कल्प' (Kalpa) है (विशेष रूप से कल्प के अंतर्गत आने वाले शुल्ब सूत्र)।"
        },
        "The Vedanga dealing with meters and poetry structure is __________.": {
            "q": "काव्य छंदों और कविता की संरचना से संबंधित वेदांग __________ है।",
            "sol": "सही उत्तर 'छंद' (Chhanda) है।"
        },
        "The astronomer linked with Vedanga Jyotisha was __________.": {
            "q": "वेदांग ज्योतिष से जुड़े खगोलशास्त्री __________ थे।",
            "sol": "सही उत्तर 'लगध' (Lagadha) है।"
        },
        "The sutras detailing domestic rites and marriages are called __________ Sutras.": {
            "q": "घरेलू अनुष्ठानों और विवाहों का विवरण देने वाले सूत्रों को __________ सूत्र कहा जाता है।",
            "sol": "सही उत्तर 'गृह्य' (Griha) सूत्र है।"
        },
        "The phonetic manuals associated with specific Vedic branches are called __________.": {
            "q": "विशिष्ट वैदिक शाखाओं से जुड़े ध्वन्यात्मक मैनुअल को __________ कहा जाता है।",
            "sol": "सही उत्तर 'प्रातिशाख्य' (Pratishakhyas) है।"
        },
        "The etymological treatise Nirukta was written by __________.": {
            "q": "व्युत्पत्ति संबंधी ग्रंथ निरुक्त __________ द्वारा लिखा गया था।",
            "sol": "सही उत्तर 'यास्क' (Yaska) है।"
        },
        "Match Vedangas to English domains:": {
            "q": "वेदांगों का अंग्रेजी क्षेत्रों से मिलान करें:",
            "sol": "सही मिलान है: शिक्षा (ध्वन्यात्मकता), व्याकरण (व्याकरण), और निरुक्त (व्युत्पत्तिशास्त्र)।"
        },
        "Match Kalpa branches to content:": {
            "q": "कल्प की शाखाओं का उनकी सामग्री से मिलान करें:",
            "sol": "सही मिलान है: श्रौत सूत्र (सार्वजनिक यज्ञ), गृह्य सूत्र (घरेलू जीवन संस्कार), और धर्म सूत्र (सामाजिक कानून और कर्तव्य)।"
        },
        "Match authors to Vedanga texts:": {
            "q": "लेखकों का वेदांग ग्रंथों से मिलान करें:",
            "sol": "सही मिलान है: पाणिनी (अष्टाध्यायी), यास्क (निरुक्त), और पिंगल (छंदशास्त्र)।"
        },
        "Why did the preservation of Vedas require auxiliary sciences like Shiksha and Vyakarana?": {
            "q": "वेदों के संरक्षण के लिए शिक्षा और व्याकरण जैसे सहायक विज्ञानों (वेदांगों) की आवश्यकता क्यों थी?",
            "sol": "चूंकि वेद मौखिक रूप से प्रसारित किए जाते थे, इसलिए मंत्रों के सही उच्चारण (शिक्षा) और भाषा की शुद्धता (व्याकरण) को बनाए रखना आवश्यक था, ताकि उनका अर्थ न बदले।"
        },
        "Why are the Shulba Sutras considered the foundation of Indian geometry?": {
            "q": "शुल्ब सूत्रों को भारतीय ज्यामिति का आधार क्यों माना जाता है?",
            "sol": "इनमें यज्ञ वेदियों को वर्गाकार, गोलाकार या त्रिकोणीय बनाने के लिए गणितीय गणनाएँ शामिल हैं, जिनमें पाइथागोरस प्रमेय का प्रारंभिक रूप भी मिलता है।"
        },
        "Why are the Dharma Sutras historically valuable for studying social structures?": {
            "q": "सामाजिक संरचनाओं के अध्ययन के लिए धर्म सूत्र ऐतिहासिक रूप से मूल्यवान क्यों हैं?",
            "sol": "वे विभिन्न सामाजिक वर्गों के कर्तव्यों, चार वर्णों के नियमों, अपराध और न्याय प्रणाली का विवरण देते हैं, जो तत्कालीन सामाजिक व्यवस्था के विकास को दर्शाता है।"
        },
        "How does Panini's Ashtadhyayi help reconstruct the geography of ancient India?": {
            "q": "पाणिनी की अष्टाध्यायी प्राचीन भारत के भूगोल के पुनर्निर्माण में कैसे मदद करती है?",
            "sol": "व्याकरण के नियमों को समझाने के लिए पाणिनी ने तत्कालीन जनपदों, नदियों, कबीलों, शहरों और व्यापारिक मार्गों के नामों का उपयोग किया है जो ऐतिहासिक भूगोल का साक्ष्य हैं।"
        },
        "How did Yaska analyze difficult words in the Nirukta?": {
            "q": "यास्क ने निरुक्त में कठिन शब्दों का विश्लेषण कैसे किया?",
            "sol": "उन्होंने शब्दों को उनकी मूल धातु (Verbal Roots) से जोड़ने की वैज्ञानिक पद्धति अपनाई, जिससे भारतीय भाषाविज्ञान में व्युत्पत्तिशास्त्र (etymology) की शुरुआत हुई।"
        },
        "How did the Kalpa Sutras systematize householder duties?": {
            "q": "कल्प सूत्रों ने गृहस्थों के कर्तव्यों को कैसे व्यवस्थित किया?",
            "sol": "गृह्य सूत्रों के माध्यम से उन्होंने एक आम गृहस्थ के जीवन-चक्र के १६ महत्वपूर्ण संस्कारों (जैसे गर्भाधान, विवाह, अंत्येष्टि) और दैनिक पंचमहायज्ञों के नियम तय किए।"
        },
        "Analyze the social regulations on marriage according to Gautama Dharma Sutra.": {
            "q": "गौतम धर्म सूत्र के अनुसार विवाह पर सामाजिक नियमों का विश्लेषण करें।",
            "sol": "यह विवाह के आठ रूपों (जैसे ब्रह्म, देव, आसुर, गंधर्व) का वर्णन करता है और अंतर-जातीय विवाहों के नियमों तथा उनके सामाजिक प्रभावों को संहिताबद्ध करता है।"
        },
        "Examine the astronomical calculations in the Vedanga Jyotisha.": {
            "q": "वेदांग ज्योतिष में खगोलीय गणनाओं का परीक्षण करें।",
            "sol": "यह संक्रांतियों (solstices), नक्षत्रों, सौर और चंद्र मासों तथा ५ वर्ष के युग (Five-year Yuga) की खगोलीय गणना प्रस्तुत करता है, जिसका उपयोग यज्ञ की तिथियां तय करने में होता था।"
        },
        "Investigate the role of phonetic treatises called Pratishakhyas.": {
            "q": "प्रातिशाख्य कहलाने वाले ध्वन्यात्मक ग्रंथों की भूमिका की जांच करें।",
            "sol": "प्रत्येक वेद शाखा के प्रातिशाख्य ने मौखिक पाठ की शुद्धता सुनिश्चित करने के लिए संधियों के नियमों, अक्षरों के उच्चारण स्थानों और सुरों (accents) का विस्तृत विवरण दर्ज किया है।"
        },
        "Explain the six metaphoric limbs of the Veda.": {
            "q": "वेद के रूपक छह अंगों (वेदांगों) की व्याख्या करें।",
            "sol": "वेद को एक पुरुष मानकर शिक्षा को उसकी नासिका, कल्प को हाथ, ज्योतिष को आंखें, निरुक्त को कान, छंद को पैर और व्याकरण को उसका मुख माना गया है।"
        },
        "Explain the distinction between Dharma Sutras and Dharmashastras.": {
            "q": "धर्म सूत्रों और धर्मशास्त्रों के बीच के अंतर को स्पष्ट करें।",
            "sol": "धर्म सूत्र प्राचीन हैं जो संक्षिप्त गद्य शैलियों में लिखे गए हैं, जबकि धर्मशास्त्र (जैसे मनुस्मृति) बाद के ग्रंथ हैं जो पद्य और छंदों में विस्तृत सामाजिक कानूनों के रूप में रचे गए हैं।"
        },
        "Explain what the Shulba Sutras tell us about early mathematics.": {
            "q": "शुल्ब सूत्र हमें प्रारंभिक गणित के बारे में क्या बताते हैं?",
            "sol": "वे दर्शाते हैं कि प्राचीन भारतीयों ने ज्यामिति और अंकगणित का विकास वेदियों के क्षेत्रफल और आकार को बनाए रखने की व्यावहारिक आवश्यकताओं के तहत किया था।"
        },

        # --- Section 5: Archaeological & External Sources ---
        "Which archaeological pottery culture is closely associated with the Later Vedic period?": {
            "q": "कौन सी पुरातात्विक मृदभांड संस्कृति उत्तर वैदिक काल से निकटता से जुड़ी हुई है?",
            "opts": ["चित्रित धूसर मृदभांड (PGW)", "गेरुए रंग के मृदभांड (OCP)", "उत्तरी काले चमकीले मृदभांड (NBPW)", "काले और लाल मृदभांड (BRW)"],
            "sol": "PGW संस्कृति (लगभग 1100-600 ईसा पूर्व) उत्तर वैदिक समाज के भौगोलिक प्रसार और समयरेखा से मेल खाती है।"
        },
        "The Boghazkoi (Bogazköy) tablets found in Turkey, dated to c. 1400 BCE, mention which Vedic deities?": {
            "q": "तुर्की में पाए गए बोगजकोई (Boghazkoi) शिलालेख (लगभग 1400 ईसा पूर्व) में किन वैदिक देवताओं का उल्लेख है?",
            "opts": ["इंद्र, मित्र, वरुण, नासत्य", "इंद्र, अग्नि, सोम, यम", "वरुण, अग्नि, सूर्य, पूषन", "सोम, रुद्र, उषा, अदिति"],
            "sol": "बोगजकोई शिलालेखों में एक संधि है जिसमें इंद्र, मित्र, वरुण और नासत्य (अश्विन) को गवाह के रूप में नामित किया गया है।"
        },
        "Which major Painted Grey Ware (PGW) site in Uttar Pradesh has yielded early evidence of iron smelting?": {
            "q": "उत्तर प्रदेश के किस प्रमुख चित्रित धूसर मृदभांड (PGW) स्थल से लोहा गलाने के शुरुआती साक्ष्य मिले हैं?",
            "opts": ["अतरंजीखेड़ा", "हस्तिनापुर", "अहिच्छत्र", "मथुरा"],
            "sol": "अतरंजीखेड़ा (आर.सी. गौर द्वारा उत्खनन) से व्यापक लोहे के स्लैग और भट्टियाँ मिली हैं।"
        },
        "Which ancient Iranian text shares close linguistic parallels and cognitive deities with the Rigveda?": {
            "q": "कौन सा प्राचीन ईरानी ग्रंथ ऋग्वेद के साथ निकट भाषाई समानताएं और समान देवताओं को साझा करता है?",
            "opts": ["जेंद अवेस्ता", "गिलगामेश का महाकाव्य", "मृत सागर के स्क्रॉल", "होमर के भजन"],
            "sol": "जेंद अवेस्ता ऋग्वेद के साथ समानांतर शब्द (सोम/हाओमा, असुर/अहुर) और भाषाई संरचनाएं साझा करता है।"
        },
        "The Ochre Coloured Pottery (OCP) culture is generally dated to:": {
            "q": "गेरुए रंग के मृदभांड (OCP) संस्कृति को सामान्यतः किस काल का माना जाता है?",
            "opts": ["लगभग 2000–1500 ईसा पूर्व", "लगभग 1100–600 ईसा पूर्व", "लगभग 600–300 ईसा पूर्व", "लगभग 3000–2500 ईसा पूर्व"],
            "sol": "OCP का समय लगभग 2000-1500 ईसा पूर्व है और यह गंगा घाटी में उत्तर-हड़प्पा / प्रारंभिक ताम्रपाषाण कालीन क्षितिज का प्रतिनिधित्व करता है।"
        },
        "The Boghazkoi inscription belongs to a treaty between Hittite and Mitanni rulers.": {
            "q": "बोगजकोई शिलालेख हित्ती और मितन्नी शासकों के बीच एक संधि से संबंधित है।",
            "sol": "सही। यह संधि दो प्राचीन साम्राज्यों के बीच युद्ध विराम के लिए साक्षी देवताओं के रूप में वैदिक देवताओं को दर्ज करती है।"
        },
        "Painted Grey Ware is a coarse, thick pottery made of river clay.": {
            "q": "चित्रित धूसर मृदभांड नदी की मिट्टी से बना एक खुरदरा, मोटा बर्तन है।",
            "sol": "गलत। PGW एक अत्यंत बारीक, पतली दीवार वाली और अच्छी तरह पकी हुई धूसर रंग की मिट्टी की मेज की बर्तन (tableware) श्रेणी है।"
        },
        "Iron smelting was unknown during the PGW period.": {
            "q": "PGW काल के दौरान लोहा गलाना अज्ञात था।",
            "sol": "गलत। PGW संस्कृति लौह युग से जुड़ी है; अतरंजीखेड़ा और जखेड़ा जैसे स्थलों से लौह प्रगलन के स्पष्ट उपकरण मिले हैं।"
        },
        "The Zend Avesta mentions the deity Ahura Mazda, which matches the Vedic Asura Varuna.": {
            "q": "जेंद अवेस्ता में असुर मज्दा (Ahura Mazda) देवता का उल्लेख है, जो वैदिक असुर वरुण से मेल खाता है।",
            "sol": "सही। ईरानी देवशास्त्र का सर्वोच्च देवता 'अहुर मज्दा' वैदिक साहित्य के वरुण देव के समानांतर है।"
        },
        "Hastinapura shows archaeological evidence of a major flood ending the PGW phase.": {
            "q": "हस्तिनापुर से एक बड़ी बाढ़ के पुरातात्विक साक्ष्य मिले हैं जिसने PGW चरण को समाप्त कर दिया था।",
            "sol": "सही। बी.बी. लाल के उत्खनन से मिले बाढ़ की कीचड़ की परत (alluvial silt) दर्शाता है कि बाढ़ के कारण इस बस्ती को खाली करना पड़ा था।"
        },
        "Vedic culture can be entirely identified with the Indus Valley Civilisation.": {
            "q": "वैदिक संस्कृति को पूरी तरह से सिंधु घाटी सभ्यता के साथ जोड़ा जा सकता है।",
            "sol": "गलत। अधिकांश इतिहासकार दोनों को अलग मानते हैं - हड़प्पा एक कांस्य युगीन शहरी संस्कृति थी जबकि वैदिक एक लौह युगीन ग्रामीण और पशुपालक संस्कृति थी।"
        },
        "The Kassite inscription of Babylon shows Indo-Aryan elements.": {
            "q": "बेबीलोन के कस्साइट शिलालेख में भारत-आर्य तत्व दिखाई देते हैं।",
            "sol": "सही। बेबीलोन के कस्साइट शिलालेखों (लगभग 16वीं शताब्दी ईसा पूर्व) में सूरीयास (Surias/सूर्य) और मारुतास (Marutas/मरुत) जैसे देवताओं के नाम हैं।"
        },
        "Linguistic cognates like 'Pitar' and 'Pater' show Indo-European connections.": {
            "q": "भाषाई सहजात शब्द जैसे 'पितर' और 'पैटर्' भारत-यूरोपीय संबंधों को दर्शाते हैं।",
            "sol": "सही। संस्कृत, ग्रीक, लैटिन और फारसी भाषाओं के बीच शब्दों की यह समानता एक ही मूल भारत-यूरोपीय भाषा परिवार की पुष्टि करती है।"
        },
        "The Boghazkoi tablets are located in modern __________.": {
            "q": "बोगजकोई शिलालेख आधुनिक __________ में स्थित हैं।",
            "sol": "सही उत्तर 'तुर्की' (Turkey/अनातोलिया) है।"
        },
        "The pottery associated with the Later Vedic period is __________.": {
            "q": "उत्तर वैदिक काल से जुड़े मृदभांड __________ हैं।",
            "sol": "सही उत्तर 'चित्रित धूसर मृदभांड' (Painted Grey Ware - PGW) हैं।"
        },
        "The PGW site showing advanced iron tools and a canal-like structure is __________.": {
            "q": "उन्नत लोहे के उपकरण और नहर जैसी संरचना दिखाने वाला PGW स्थल __________ है।",
            "sol": "सही उत्तर 'जखेड़ा' (Jakhera) है।"
        },
        "The ancient Iranian text having parallels with the Rigveda is the __________.": {
            "q": "ऋग्वेद के साथ समानता रखने वाला प्राचीन ईरानी ग्रंथ __________ है।",
            "sol": "सही उत्तर 'अवेस्ता' (Zend Avesta) है।"
        },
        "The archaeological culture preceding PGW in the Gangetic Doab was __________.": {
            "q": "गंगा दोआब में PGW से पहले की पुरातात्विक संस्कृति __________ थी।",
            "sol": "सही उत्तर 'गेरुए रंग के मृदभांड' (Ochre Coloured Pottery - OCP) संस्कृति है।"
        },
        "The epigraphic record of Babylon mentioning Aryan names is the __________ inscription.": {
            "q": "आर्य नामों का उल्लेख करने वाला बेबीलोन का पुरालेखीय रिकॉर्ड __________ शिलालेख है।",
            "sol": "सही उत्तर 'कस्साइट' (Kassite) शिलालेख है।"
        },
        "The archaeologist who excavated Hastinapura in the 1950s was __________.": {
            "q": "1950 के दशक में हस्तिनापुर का उत्खनन करने वाले प्रसिद्ध पुरातत्वविद् __________ थे।",
            "sol": "सही उत्तर 'बी.बी. लाल' (B.B. Lal) हैं।"
        },
        "Cognate words like 'Raja' and Latin 'Rex' show a shared __________ language origin.": {
            "q": "सहजात शब्द जैसे 'राजा' और लैटिन 'रेक्स' एक साझा __________ भाषा मूल को दर्शाते हैं।",
            "sol": "सही उत्तर 'भारत-यूरोपीय' (Indo-European) भाषा परिवार है।"
        },
        "Match inscriptions to locations/contexts:": {
            "q": "शिलालेखों का स्थानों/संदर्भों से मिलान करें:",
            "sol": "सही मिलान है: बोगजकोई (तुर्की), कस्साइट (बेबीलोन), और तेल एल-अमरना (मिस्र)।"
        },
        "Match archaeological phases to periods:": {
            "q": "पुरातात्विक चरणों का अवधियों से मिलान करें:",
            "sol": "सही मिलान है: OCP (उत्तर-हड़प्पा / प्रारंभिक वैदिक), PGW (उत्तर वैदिक / लौह युग), और NBPW (महाजनपद / मौर्य काल)।"
        },
        "Match sites to excavation features:": {
            "q": "स्थलों का उत्खनन विशेषताओं से मिलान करें:",
            "sol": "सही मिलान है: हस्तिनापुर (बाढ़ परत), अतरंजीखेड़ा (लोहा भट्टियाँ), और भगवानपुरा (उत्तर-हड़प्पा-PGW ओवरलैप)।"
        },
        "Why does Zend Avesta share linguistic patterns with the Rigveda?": {
            "q": "जेंड अवेस्ता ऋग्वेद के साथ भाषाई समानताएं क्यों साझा करता है?",
            "sol": "क्योंकि भारत-आर्य और ईरानी लोग पहले एक ही 'प्रोटो-इंडो-ईरानी' समुदाय का हिस्सा थे, जो लगभग २री सहस्राब्दी ईसा पूर्व में विभाजित हो गए।"
        },
        "Why was the flood layer at Hastinapura significant to B.B. Lal's correlation?": {
            "q": "हस्तिनापुर की बाढ़ की परत बी.बी. लाल के ऐतिहासिक सह-संबंध के लिए क्यों महत्वपूर्ण थी?",
            "sol": "इसने उस पौराणिक/पुराण परंपरा की पुष्टि की जिसके अनुसार गंगा में आई बाढ़ के कारण पांडवों को अपनी राजधानी हस्तिनापुर से कौशांबी स्थानांतरित करनी पड़ी थी।"
        },
        "Why is the overlap of Late Harappan and PGW at Bhagwanpura important?": {
            "q": "भगवानपुरा में उत्तर-हड़प्पा और PGW का ओवरलैप क्यों महत्वपूर्ण है?",
            "sol": "यह दर्शाता है कि हड़प्पा की अंतिम चरण की आबादी और नई धूसर मृदभांड संस्कृति के लोग कुछ स्थानों पर एक साथ सह-अस्तित्व में थे, जो अचानक विनाश के सिद्धांत को खारिज करता है।"
        },
        "How does the archaeological recovery of iron slag at Atranjikhera help date the Later Vedic period?": {
            "q": "अतरंजीखेड़ा में मिले लोहे के धातुमल (slag) उत्तर वैदिक काल के निर्धारण में कैसे मदद करते हैं?",
            "sol": "लगभग १००० ईसा पूर्व की परतों में लोहे के अवशेषों की रेडियोकार्बन डेटिंग उत्तर वैदिक साहित्य के 'श्याम अयस' के उपयोग की समयसीमा से पूरी तरह मेल खाती है।"
        },
        "How do linguistic cognates validate the Indo-European migration hypothesis?": {
            "q": "भाषाई सहजात शब्द भारत-यूरोपीय प्रवास परिकल्पना को कैसे प्रमाणित करते हैं?",
            "sol": "विभिन्न देशों में घोड़े (अश्व, अस्पा, एक्वस) जैसी समान बुनियादी शब्दावली दर्शाती है कि ये लोग एक ही मूल स्थान से अपनी भाषा और पालतू पशुओं के साथ विस्थापित हुए थे।"
        },
        "How did the PGW pottery suggest a sedentary agrarian lifestyle?": {
            "q": "PGW मृदभांडों ने स्थायी कृषि जीवन शैली का सुझाव कैसे दिया?",
            "sol": "इतने बारीक और सुंदर बर्तनों की उपस्थिति, अनाज भंडारण के गर्त (silos) और मवेशियों की हड्डियों की प्रचुरता स्थायी ग्रामीण बस्तियों की गवाही देती है।"
        },
        "Analyze the Jakhera excavations and the emergence of early urban traits in PGW.": {
            "q": "जखेड़ा उत्खनन और PGW में प्रारंभिक शहरी लक्षणों के उदय का विश्लेषण करें।",
            "sol": "जखेड़ा से मिली सुरक्षा खाई, खेती के लौह उपकरण (जैसे दरांती) और अर्ध-औद्योगिक तांबे/लोहे की भट्टियाँ दर्शाती हैं कि उत्तर वैदिक काल के अंत में बस्तियां शहर का रूप ले रही थीं।"
        },
        "Examine the Mitanni treaty of Boghazkoi as an epigraphic anchor.": {
            "q": "एक पुरालेखीय लंगर (epigraphic anchor) के रूप में बोगजकोई की मितन्नी संधि का परीक्षण करें।",
            "sol": "यह शिलालेख लगभग १४०० ईसा पूर्व में वैदिक देवताओं की पूजा को तुर्की में सिद्ध करता है, जिससे वैदिक ऋचाओं के रचना काल और आर्यों के विस्थापन की समयसीमा को एक वैज्ञानिक आधार मिलता है।"
        },
        "Investigate the OCP-Copper Hoard associations in the upper Doab.": {
            "q": "ऊपरी दोआब में OCP और ताम्र निधियों (Copper Hoards) के संबंधों की जांच करें।",
            "sol": "OCP स्थलों से बड़ी संख्या में तांबे के उपकरण (जैसे तलवारें, भाले) मिले हैं, जो यह संकेत देते हैं कि लोहे के प्रयोग से पहले गंगा घाटी में एक अत्यधिक उन्नत ताम्र-धातु कर्म (copper-working) संस्कृति मौजूद थी।"
        },
        "Explain what Painted Grey Ware is.": {
            "q": "चित्रित धूसर मृदभांड (Painted Grey Ware) क्या हैं, समझाएं।",
            "sol": "यह चाक पर निर्मित, बारीक धूसर रंग का मिट्टी का पात्र है जिस पर ज्यामितीय काले रंग के चित्र बने होते थे, जिसका उपयोग उत्तर वैदिक समाज के अमीर घरों में किया जाता था।"
        },
        "Explain the significance of the Boghazkoi tablets.": {
            "q": "बोगजकोई शिलालेखों के ऐतिहासिक महत्व को समझाएं।",
            "sol": "तुर्की में मिला १४०० ईसा पूर्व का संधिपत्र है जिसमें ऋग्वैदिक देवताओं - इंद्र, मित्र, वरुण और नासत्य का गवाह के रूप में उल्लेख है, जो मध्य पूर्व और वैदिक संस्कृति के प्राचीन ऐतिहासिक संपर्कों को सिद्ध करता है।"
        },
        "Explain the transition from Copper (OCP) to Iron (PGW) in the Gangetic valley.": {
            "q": "गंगा घाटी में तांबे (OCP) से लोहे (PGW) के संक्रमण को स्पष्ट करें।",
            "sol": "यह परिवर्तन तांबे के सीमित और अल्प-विकसित औजारों की जगह मजबूत लोहे के हथियारों और उपकरणों के आने का है, जिसने कृषि क्रांति और घने जंगलों को काटकर राज्यों के विस्तार का मार्ग प्रशस्त किया।"
        },

        # --- Section 6: Historiographical Debates ---
        "The Out of India Theory (OIT) argues that:": {
            "q": "आउट ऑफ इंडिया थ्योरी (OIT) का तर्क है कि:",
            "opts": ["भारत-आर्य भाषाएँ भारत में उत्पन्न हुईं और पश्चिम की ओर चली गईं", "आर्यों ने मध्य एशिया से भारत पर आक्रमण किया", "हड़प्पावासियों ने वैदिक बस्तियों को नष्ट कर दिया", "भारत-यूरोपीय भाषाएँ पोंटिक स्टेपी में उत्पन्न हुईं"],
            "sol": "OIT का मानना है कि भारत भारत-यूरोपीय भाषाओं की मातृभूमि है जहाँ से पश्चिम की ओर प्रवास हुआ।"
        },
        "Which historian pioneered the Marxist, socio-economic analysis of Vedic society?": {
            "q": "किस इतिहासकार ने वैदिक समाज के मार्क्सवादी, सामाजिक-आर्थिक विश्लेषण की शुरुआत की?",
            "opts": ["डी.डी. कोसांबी", "मैक्स मूलर", "ए.एल. बाशम", "विंसेंट स्मिथ"],
            "sol": "डी.डी. कोसांबी ने उत्पादन संबंधों पर ध्यान केंद्रित करते हुए प्राचीन भारत के अध्ययन में ऐतिहासिक भौतिकवाद की शुरुआत की।"
        },
        "The Aryan Invasion Theory was popularized in the 1940s by which archaeologist using the term 'Hari-yupiya'?": {
            "q": "1940 के दशक में किस पुरातत्वविद् ने 'हरि-यूपिया' शब्द का उपयोग करके आर्य आक्रमण सिद्धांत को लोकप्रिय बनाया?",
            "opts": ["मॉर्टिमर व्हीलर", "जॉन मार्शल", "बी.बी. लाल", "अलेक्जेंडर कनिंघम"],
            "sol": "मॉर्टिमर व्हीलर ने तर्क दिया कि हड़प्पा (हरि-यूपिया) को आर्यों के देवता इंद्र द्वारा नष्ट कर दिया गया था।"
        },
        "The 2019 ancient DNA study on the Rakhigarhi skeletal remains showed:": {
            "q": "राखीगढ़ी के कंकाल के अवशेषों पर 2019 के प्राचीन डीएनए अध्ययन ने क्या दिखाया?",
            "opts": ["हड़प्पा डीएनए में स्टेपी आनुवंशिकी की अनुपस्थिति", "हड़प्पा डीएनए में स्टेपी आनुवंशिकी की प्रधानता", "हड़प्पावासियों का आधुनिक यूरोपीय लोगों के साथ सीधा संबंध", "उपरोक्त में से कोई नहीं"],
            "sol": "राखीगढ़ी अध्ययन से पता चला कि हड़प्पावासियों में स्टेपी आनुवंशिकी (R1a1) की कमी थी, जो बाद में प्रवास का समर्थन करती है।"
        },
        "Who wrote 'The Arctic Home in the Vedas', proposing a polar origin for Aryans?": {
            "q": "आर्यों के ध्रुवीय मूल का प्रस्ताव रखने वाली पुस्तक 'द आर्कटिक होम इन द वेदाज' किसने लिखी थी?",
            "opts": ["बी.जी. तिलक", "दयानंद सरस्वती", "मैक्स मूलर", "रोमिला थापर"],
            "sol": "बाल गंगाधर तिलक ने ऋग्वेद में खगोलीय संदर्भों का उपयोग करते हुए तर्क दिया कि आर्यों की मातृभूमि आर्कटिक थी।"
        },
        "The Aryan Migration Theory (AMT) is supported by recent genetic studies.": {
            "q": "आर्य प्रवास सिद्धांत (AMT) हाल के आनुवंशिक अध्ययनों द्वारा समर्थित है।",
            "sol": "सही। हाल के आनुवंशिक (ancient DNA) अध्ययनों से पुष्टि हुई है कि १५०० ईसा पूर्व के आसपास स्टेपी क्षेत्र से दक्षिण एशिया में महत्वपूर्ण आनुवंशिक प्रवाह (R1a1 हैलोग्रुप) हुआ था।"
        },
        "Max Müller claimed that 'Aryan' was a biological race.": {
            "q": "मैक्स मूलर ने दावा किया कि 'आर्य' एक जैविक प्रजाति थी।",
            "sol": "गलत। मैक्स मूलर ने बार-बार स्पष्ट किया था कि 'आर्य' एक भाषा परिवार (Linguistic Group) है, न कि कोई जैविक नस्ल या जाति (Race)।"
        },
        "D.D. Kosambi's combined method excludes the use of folklore and ethnography.": {
            "q": "डी.डी. कोसांबी की संयुक्त पद्धति में लोककथाओं और नृवंशविज्ञान का उपयोग शामिल नहीं है।",
            "sol": "गलत। कोसांबी की संयुक्त पद्धति की विशेषता ही यही थी कि उन्होंने ग्रंथों और पुरातत्व के साथ-साथ जीवित लोक परंपराओं और जनजातीय संस्कृति का उपयोग किया।"
        },
        "Archaeologist B.B. Lal argued for the indigenous origin of the Aryans.": {
            "q": "पुरातत्वविद् बी.बी. लाल ने आर्यों के स्वदेशी मूल के पक्ष में तर्क दिया।",
            "sol": "सही। बी.बी. लाल और कई अन्य पुरातत्वविदों ने तर्क दिया है कि ऋग्वैदिक और हड़प्पा संस्कृतियों के बीच निरंतरता है और आर्य स्वदेशी थे।"
        },
        "Indo-Aryan languages belong to the Dravidian language family.": {
            "q": "भारत-आर्य भाषाएँ द्रविड़ भाषा परिवार से संबंधित हैं।",
            "sol": "गलत। भारत-आर्य भाषाएँ भारत-यूरोपीय (Indo-European) भाषा परिवार की उपशाखा हैं, जबकि तमिल, तेलुगु आदि द्रविड़ परिवार का हिस्सा हैं।"
        },
        "The Indus script has been definitively deciphered as Vedic Sanskrit.": {
            "q": "सिंधु लिपि को निश्चित रूप से वैदिक संस्कृत के रूप में पढ़ा जा चुका है।",
            "sol": "गलत। सिंधु लिपि को आज तक सफलतापूर्वक और सर्वसम्मति से पढ़ा नहीं जा सका है, और इसका वैदिक संस्कृत होना सिद्ध नहीं है।"
        },
        "Sarasvati river hydrology is used by indigenous theorists to date the Rigveda earlier.": {
            "q": "स्वदेशी सिद्धांतकारों द्वारा ऋग्वेद को पुराने काल का बताने के लिए सरस्वती नदी के जल विज्ञान का उपयोग किया जाता है।",
            "sol": "सही। यदि ऋग्वेद में सरस्वती एक बहती हुई विशाल नदी है जो भू-वैज्ञानिकों के अनुसार १९०० ईसा पूर्व तक पूरी तरह सूख चुकी थी, तो वे तर्क देते हैं कि ऋग्वेद की रचना इस तिथि से पहले हुई थी।"
        },
        "The Rigveda contains clear references to the ruins of Harappan cities.": {
            "q": "ऋग्वेद में हड़प्पा शहरों के खंडहरों के स्पष्ट संदर्भ मिलते हैं।",
            "sol": "गलत। ऋग्वेद में किलों या पुरों के विनाश का उल्लेख तो है, लेकिन हड़प्पा या किसी विशिष्ट हड़प्पा शहर के खंडहरों का कोई प्रत्यक्ष विवरण नहीं मिलता।"
        },
        "The theory of gradual Aryan migration from the steppe is the __________.": {
            "q": "स्टेपी से क्रमिक आर्य प्रवास का सिद्धांत __________ कहलाता है।",
            "sol": "सही उत्तर 'आर्य प्रवास सिद्धांत' (Aryan Migration Theory - AMT) है।"
        },
        "The Marxist historian who wrote 'Shudras in Ancient India' was __________.": {
            "q": "इतिहास पुस्तक 'शूद्रास इन एंशिएंट इंडिया' लिखने वाले मार्क्सवादी इतिहासकार __________ थे।",
            "sol": "सही उत्तर 'राम शरण शर्मा' (R.S. Sharma) हैं।"
        },
        "B.G. Tilak's book on Aryan homeland was titled 'The __________ Home in the Vedas'.": {
            "q": "आर्य मातृभूमि पर बी.जी. तिलक की पुस्तक का शीर्षक 'द __________ होम इन द वेदाज' था।",
            "sol": "सही उत्तर 'आर्कटिक' (Arctic) है।"
        },
        "The method of combining texts, archaeology, and anthropology was pioneered by __________.": {
            "q": "ग्रंथों, पुरातत्व और नृविज्ञान को संयोजित करने की पद्धति की शुरुआत __________ द्वारा की गई थी।",
            "sol": "सही उत्तर 'डी.डी. कोसांबी' (D.D. Kosambi) ने की थी।"
        },
        "The haplogroup associated with Steppe migrations into India is __________.": {
            "q": "भारत में स्टेपी प्रवास से जुड़ा हैलोग्रुप __________ है।",
            "sol": "सही उत्तर 'R1a1' है।"
        },
        "The archaeologist who proposed the Aryan invasion at Mohenjo-daro was __________.": {
            "q": "मोहनजोदड़ो में आर्य आक्रमण का प्रस्ताव रखने वाले पुरातत्वविद् __________ थे।",
            "sol": "सही उत्तर 'मॉर्टिमर व्हीलर' (Mortimer Wheeler) हैं।"
        },
        "The linguistic family containing Sanskrit, Greek, and Latin is __________.": {
            "q": "संस्कृत, ग्रीक और लैटिन को शामिल करने वाला भाषा परिवार __________ है।",
            "sol": "सही उत्तर 'भारत-यूरोपीय' (Indo-European) है।"
        },
        "The modern historian who wrote 'Aryan and Non-Aryan in India' is __________.": {
            "q": "आधुनिक इतिहासकार जिन्होंने 'आर्यन एंड नॉन-आर्यन इन इंडिया' लिखी, __________ हैं।",
            "sol": "सही उत्तर 'रोमिला थापर' (Romila Thapar) हैं।"
        },
        "Match theory to main proponent:": {
            "q": "सिद्धांतों का उनके मुख्य समर्थकों से मिलान करें:",
            "sol": "सही मिलान है: आर्कटिक होम (बी.जी. तिलक), मध्य एशियाई मूल (मैक्स मूलर), और स्वदेशी मूल (बी.बी. लाल)।"
        },
        "Match historians to historiographical school:": {
            "q": "इतिहासकारों का ऐतिहासिक संप्रदाय से मिलान करें:",
            "sol": "सही मिलान है: मैक्स मूलर (भाषाशास्त्रीय/प्राच्यविद्), डी.डी. कोसांबी (marksवादी), और रोमिला थापर (आधुनिक आलोचनात्मक)।"
        },
        "Match scientific disciplines to study domain:": {
            "q": "वैज्ञानिक विषयों का अध्ययन क्षेत्र से मिलान करें:",
            "sol": "सही मिलान है: तुलनात्मक भाषाशास्त्र (भाषा संबंध), पुरातत्व-आनुवंशिकी (डीएनए प्रवास), और जल विज्ञान (प्राचीन नदी तल)।"
        },
        "Why did Max Müller's linguistic definition of 'Aryan' get misused as a biological race concept?": {
            "q": "मैक्स मूलर की 'आर्य' की भाषाई परिभाषा का जैविक नस्ल (biological race) के रूप में दुरुपयोग क्यों हुआ?",
            "sol": "19वीं सदी के यूरोपीय राष्ट्रवाद, सामाजिक डार्विनवाद और औपनिवेशिक हितों ने भाषाई वर्गीकरण को नस्लीय श्रेष्ठता सिद्ध करने के साधन के रूप में विकृत कर दिया।"
        },
        "Why is the Sarasvati river debate central to the dating of the Rigveda?": {
            "q": "ऋग्वेद के काल निर्धारण में सरस्वती नदी का विवाद क्यों महत्वपूर्ण है?",
            "sol": "यदि ऋग्वेद में सरस्वती एक बहती हुई विशाल नदी है जो भू-वैज्ञानिकों के अनुसार १९०० ईसा पूर्व तक पूरी तरह सूख चुकी थी, तो स्वदेशी सिद्धांतकार तर्क देते हैं कि ऋग्वेद की रचना निश्चित रूप से १९०० ईसा पूर्व से बहुत पहले की गई थी।"
        },
        "Why did D.D. Kosambi advocate for the 'combined method' in ancient history?": {
            "q": "डी.डी. कोसांबी ने प्राचीन इतिहास में 'संयुक्त पद्धति' की वकालत क्यों की?",
            "sol": "क्योंकि वैदिक जैसे प्राचीन ग्रंथ मुख्य रूप से धार्मिक/कर्मकांडीय हैं जिनमें स्पष्ट तिथियों का अभाव है; अतः वास्तविक सामाजिक-आर्थिक सत्य जानने के लिए पुरातत्व और नृविज्ञान का मेल जरूरी है।"
        },
        "How does ancient DNA (aDNA) analysis provide evidence for the Aryan Migration Theory?": {
            "q": "प्राचीन डीएनए (aDNA) विश्लेषण आर्य प्रवास सिद्धांत (AMT) के साक्ष्य कैसे प्रदान करता है?",
            "sol": "यह दर्शाता है कि लगभग २०००-१५०० ईसा पूर्व के बीच मध्य एशियाई स्टेपी क्षेत्र से दक्षिण एशिया में बड़े पैमाने पर लोगों का जीन-प्रवाह हुआ, जो R1a1 हैलोग्रुप के प्रसार से साबित होता है।"
        },
        "How did R.S. Sharma argue that iron led to the birth of class divisions?": {
            "q": "आर.एस. शर्मा ने यह तर्क कैसे दिया कि लोहे ने वर्ग भेद को जन्म दिया?",
            "sol": "लोहे के उपकरणों से वनों की सफाई और गहरी खेती आसान हुई जिससे भारी कृषि अधिशेष (surplus) पैदा हुआ। इस अधिशेष को एकत्र करके राजा और पुरोहित वर्ग ने अपनी सत्ता मजबूत की और असमानता बढ़ी।"
        },
        "How does comparative mythology connect the Rigveda with Greek myth cycles?": {
            "q": "तुलनात्मक पौराणिक कथाएँ ऋग्वेद को यूनानी कथा चक्रों से कैसे जोड़ती हैं?",
            "sol": "वेदों के 'द्यौस पितर' और यूनान के 'ज्यूस पेटर' (Zeus Pater) जैसे नामों, तथा वज्रधारी इंद्र और ज्यूस की पौराणिक समानताओं से साबित होता है कि दोनों का मूल एक ही है।"
        },
        "Analyze the Mohenjo-daro skeletal remains debate.": {
            "q": "मोहनजोदड़ो में मिले नरकंकालों के विवाद का विश्लेषण करें।",
            "sol": "मॉर्टिमर व्हीलर ने ३० से अधिक असंबद्ध कंकालों को आर्यों द्वारा किए गए नरसंहार का सबूत बताया था, लेकिन बाद में वैज्ञानिक परीक्षा में पाया गया कि ये मौतें अलग-अलग समय पर बीमारी या बाढ़ से हुई थीं, न कि युद्ध से।"
        },
        "Examine the Rakhigarhi DNA findings published in 2019.": {
            "q": "2019 में प्रकाशित राखीगढ़ी डीएनए (Rakhigarhi DNA) के निष्कर्षों का परीक्षण करें।",
            "sol": "राखीगढ़ी से प्राप्त हड़प्पा कालीन कंकाल के डीएनए में स्टेपी क्षेत्र (R1a1) के आनुवंशिक निशान नहीं मिले, जो यह साबित करता है कि हड़प्पा की सभ्यता भारत-आर्यों के आने से पहले की एक स्वतंत्र स्थानीय सभ्यता थी।"
        },
        "Investigate the Puranic genealogy models of F.E. Pargiter.": {
            "q": "एफ.ई. पार्गिटर के पौराणिक वंशावली मॉडलों की जांच करें।",
            "sol": "पार्गिटर ने पुरोहितों के वैदिक ग्रंथों के बजाय क्षत्रियों की परंपराओं (महाकाव्यों और पुराणों की वंशावली) का विश्लेषण करके एक स्वदेशी राजाओं की समयरेखा तैयार की, जो प्रवास सिद्धांत का एक वैकल्पिक पक्ष प्रस्तुत करती है।"
        },
        "Explain the difference between the Aryan Invasion Theory and Aryan Migration Theory.": {
            "q": "आर्य आक्रमण सिद्धांत (Aryan Invasion Theory) और आर्य प्रवास सिद्धांत (Aryan Migration Theory) के बीच अंतर स्पष्ट करें।",
            "sol": "आक्रमण सिद्धांत दावा करता है कि सैन्य आक्रमणकारी समूह ने हड़प्पा को हिंसक रूप से नष्ट किया। प्रवास सिद्धांत मानता है कि स्टेपी के छोटे-छोटे पशुपालक समुदाय सदियों की अवधि में धीरे-धीरे भारत आए और शांतिपूर्ण सांस्कृतिक मिलन हुआ।"
        },
        "Explain D.D. Kosambi's 'Combined Method'.": {
            "q": "डी.डी. कोसांबी की 'संयुक्त पद्धति' (Combined Method) को समझाएं।",
            "sol": "यह प्राचीन ग्रंथों के विश्लेषण के साथ पुरातात्विक उत्खनन, सिक्कों के अध्ययन (numismatics) और आज भी जंगलों में रहने वाले जनजातीय समुदायों के रीति-रिवाजों (ethnography) को जोड़कर इतिहास का पुनर्निर्माण करने की वैज्ञानिक पद्धति है।"
        },
        "Summarize the genetic evidence regarding Steppe migrations.": {
            "q": "स्टेपी प्रवास से संबंधित आनुवंशिक साक्ष्यों का संक्षेप में वर्णन करें।",
            "sol": "प्राचीन डीएनए अनुसंधान से साबित हुआ है कि मध्य एशियाई स्टेपी चरवाहों का जीन-प्रवाह कांस्य युग के अंत में (लगभग २०००-१५०० ईसा पूर्व) भारतीय उपमहाद्वीप की आबादी में हुआ था, जो आधुनिक भारत-आर्य भाषी क्षेत्रों में अधिक पाया जाता है।"
        }
    }

    hi_mastery = []
    for q in sec["masteryZone"]:
        hi_q = q.copy()
        q_text = q["q"]
        opts = q.get("opts", [])
        sol = q.get("sol", "")
        
        import re
        set_match = re.search(r"\(Set (\d+)\)", q_text)
        set_num = set_match.group(1) if set_match else str(idx + 1)
        
        # Look up in our custom dictionary
        if q_text in q_dict:
            hi_q["q"] = q_dict[q_text]["q"]
            if "opts" in q_dict[q_text]:
                hi_q["opts"] = q_dict[q_text]["opts"]
            hi_q["sol"] = q_dict[q_text]["sol"]
        else:
            # 3. Fallbacks for loop/programmatic questions
            # Assertion-Reason replacements
            if q["type"] == "Assertion-Reason":
                if "Rigvedic society was patriarchal" in q_text:
                    hi_q["q"] = f"कथन (A): ऋग्वैदिक समाज पितृसत्तात्मक था, फिर भी महिलाओं का स्थान सम्मानजनक था।\nकारण (R): ऋग्वैदिक महिलाएँ सभा और विधात जैसी सभाओं में भाग लेती थीं, और विधवाएँ नियोग प्रथा का पालन कर सकती थीं। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "महिलाएं धार्मिक अनुष्ठानों और सभाओं में भाग लेती थीं, जिससे साबित होता है कि पितृसत्तात्मक संरचना के बावजूद वे उच्च स्थिति का आनंद लेती थीं।"
                elif "Atharvaveda is a valuable source" in q_text:
                    hi_q["q"] = f"कथन (A): अथर्ववेद प्राचीन भारतीय चिकित्सा के इतिहास के लिए एक मूल्यवान स्रोत है।\nकारण (R): इसमें बीमारियों के विवरण, उपचार के मंत्र और औषधीय जड़ी-बूटियों का वर्गीकरण शामिल है। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "अथर्ववेद को आयुर्वेद का सबसे पहला उपलब्ध साहित्यिक स्रोत माना जाता है।"
                elif "Upanishads are called Vedanta" in q_text:
                    hi_q["q"] = f"कथन (A): उपनिषदों को वेदांत कहा जाता है।\nकारण (R): वे वैदिक साहित्य के अंतिम भाग हैं और इसमें इसका दार्शनिक निष्कर्ष शामिल है। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "उपनिषद संरचनात्मक और दार्शनिक दोनों रूपों में वैदिक साहित्य का समापन करते हैं।"
                elif "Shulba Sutras are critical documents" in q_text:
                    hi_q["q"] = f"कथन (A): शुल्ब सूत्र भारतीय विज्ञान के इतिहास के लिए महत्वपूर्ण दस्तावेज हैं।\nकारण (R): इनमें वेदी के आकार के निर्माण के लिए गणितीय नियम और ज्यामितीय डिजाइन शामिल हैं। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "वेदी निर्माण के लिए सटीक आकारों की आवश्यकता होती थी, जिससे प्रारंभिक ज्यामिति का विकास हुआ।"
                elif "Boghazkoi tablets show that Indo-Aryans migrated" in q_text:
                    hi_q["q"] = f"कथन (A): बोगजकोई शिलालेख दर्शाते हैं कि भारत-आर्यों ने पश्चिम एशिया के माध्यम से प्रवास किया या वहां बसे थे।\nकारण (R): इस संधि में ऋग्वैदिक देवताओं इंद्र, वरुण, मित्र और नासत्य को गवाहों के रूप में सूचीबद्ध किया गया है। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "अनाटोलिया में इन देवताओं के नामों की उपस्थिति भारत-आर्य भाषाई और सांस्कृतिक संबंधों का प्रत्यक्ष प्रमाण है।"
                elif "Out of India Theory (OIT) is not widely" in q_text:
                    hi_q["q"] = f"कथन (A): आउट ऑफ इंडिया थ्योरी (OIT) को वैश्विक शैक्षणिक इतिहासकारों द्वारा व्यापक रूप से स्वीकार नहीं किया जाता है।\nकारण (R): भाषाई और प्राचीन DNA साक्ष्य दृढ़ता से भारत में स्टेपी चरवाहों के प्रवास का समर्थन करते हैं। (सेट {set_num})"
                    hi_q["opts"] = ["A और R दोनों सही हैं और R, A की सही व्याख्या है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"]
                    hi_q["sol"] = "बहुविषयक डेटा संरेखण के कारण शैक्षणिक सहमति OIT की तुलना में AMT का पक्ष लेती है।"
            
            # Statement-Based replacements
            elif q["type"] == "Statement-Based":
                if "Mandalas I and X were compiled" in q_text:
                    hi_q["q"] = f"ऋग्वेद के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. मंडल I और X की रचना पारिवारिक मंडलों से पहले हुई थी।\n2. दस राजाओं का युद्ध रावी (परुष्णी) नदी के पानी और गायों के विवाद को लेकर हुआ था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "कथन २ सही है। कथन १ गलत है क्योंकि मंडल १ और १० सबसे नवीनतम संकलन हैं, जबकि पारिवारिक मंडल सबसे पुराने हैं।"
                elif "Atharvaveda shows a greater amalgamation" in q_text:
                    hi_q["q"] = f"उत्तर वैदिक संहिताओं के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. अथर्ववेद वैदिक और गैर-वैदिक संस्कृतियों का अधिक समामेलन दिखाता है।\n2. यजुर्वेद में विवरण है कि कैसे कबीलों पर सर्वोच्च अधिकार प्राप्त करने के लिए राजा का राज्याभिषेक किया जाता था।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "दोनों कथन सही हैं। अथर्ववेद स्थानीय लोक-विश्वासों को दर्ज करता है, और यजुर्वेद राजसूय जैसे राज्याभिषेक अनुष्ठानों का विवरण देता है।"
                elif "rejected ritualism and emphasized" in q_text:
                    hi_q["q"] = f"उपनिषदों के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. उपनिषदों ने कर्मकांडों को खारिज कर दिया और आत्म-साक्षात्कार पर जोर दिया।\n2. गार्गी जैसी महिला दार्शनिकों ने उपनिषदों में दर्ज बौद्धिक बहसों में भाग लिया।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "दोनों कथन सही हैं। उपनिषदों ने कर्मकांडों की आलोचना की और इनमें गार्गी व मैत्री जैसी महिलाओं की भागीदारी का उल्लेख है।"
                elif "Ashtadhyayi was composed to keep" in q_text:
                    hi_q["q"] = f"वेदांगों के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. संस्कृत व्याकरण को मानकीकृत करने के लिए पाणिनी की अष्टाध्यायी की रचना की गई थी।\n2. धर्म सूत्रों में राजा के राजनीतिक कर्तव्यों का उल्लेख नहीं है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "कथन १ सही है। कथन २ गलत है क्योंकि धर्मसूत्रों में 'राजधर्म' (राजा के कर्तव्यों) का विस्तार से वर्णन किया गया है।"
                elif "characterized by mud-brick houses" in q_text:
                    hi_q["q"] = f"निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. PGW संस्कृति की विशेषता मिट्टी के ईंटों के घर और पकी ईंटों की कमी है।\n2. भगवानपुरा में, PGW उत्तर-हड़प्पा मृदभांड के साथ ओवरलैप में पाया जाता है।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "दोनों कथन सही हैं। PGW बस्तियां मुख्य रूप से कच्ची ईंटों और मिट्टी के घरों पर आधारित थीं, और भगवानपुरा में स्तर-शास्त्रीय ओवरलैप मिलता है।"
                elif "Marxist historians analyzed" in q_text:
                    hi_q["q"] = f"इतिहास लेखन वाद-विवाद के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {set_num}):\n1. मार्क्सवादी इतिहासकारों ने प्राचीन भारत का विश्लेषण वर्ग संघर्ष के बजाय मुख्य रूप से जातिगत गतिशीलता के माध्यम से किया।\n2. राखीगढ़ी के पुरातात्विक निष्कर्षों ने हड़प्पा निवासियों के प्रत्यक्ष प्राचीन डीएनए अनुक्रम प्रदान किए हैं।\nऊपर दिए गए कथनों में से कौन सा/से सही है/हैं?"
                    hi_q["opts"] = ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"]
                    hi_q["sol"] = "कथन २ सही है। कथन १ गलत है क्योंकि मार्क्सवादी इतिहासकार वर्ग संघर्ष (class struggle) और उत्पादन के साधनों को प्राथमिक मानते हैं।"

            # Multiple Correct MCQ replacements
            elif q["type"] == "Multiple Correct MCQ":
                if "Early Vedic Rigvedic society" in q_text:
                    hi_q["q"] = f"प्रारंभिक वैदिक ऋग्वैदिक समाज से निम्नलिखित में से कौन से पहलू जुड़े हुए हैं? (सेट {set_num})"
                    hi_q["opts"] = ["पितृसत्तात्मक पारिवारिक व्यवस्था", "पशुपालन अर्थव्यवस्था (गविष्टि)", "सभा और समिति जैसी सभाएं", "प्रकृति पूजा (इंद्र/अग्नि)"]
                    hi_q["sol"] = "सभी चारों विकल्प प्रारंभिक वैदिक समाज की प्रमुख विशेषताएं हैं।"
                elif "sacrifices are elaborated in the Yajurveda" in q_text:
                    hi_q["q"] = f"यजुर्वेद में निम्नलिखित में से किन यज्ञों का विस्तृत वर्णन किया गया है? (सेट {set_num})"
                    hi_q["opts"] = ["राजसूय यज्ञ", "अश्वमेध यज्ञ", "वाजपेय यज्ञ", "अग्निहोत्र यज्ञ"]
                    hi_q["sol"] = "यजुर्वेद में इन सभी शाही और दैनिक कर्मकांडीय यज्ञों के सूत्र संकलित हैं।"
                elif "principal (Mukhya) Upanishads" in q_text:
                    hi_q["q"] = f"निम्नलिखित में से कौन से मुख्य (प्रमुख) उपनिषद हैं? (सेट {set_num})"
                    hi_q["opts"] = ["छान्दोग्य उपनिषद", "बृहदारण्यक उपनिषद", "मुण्डक उपनिषद", "कठोपनिषद"]
                    hi_q["sol"] = "ये सभी प्रमुख उपनिषदों की श्रेणी में शामिल हैं।"
                elif "sub-branches of the Kalpa Vedanga" in q_text:
                    hi_q["q"] = f"कल्प वेदांग की उप-शाखाएँ निम्नलिखित में से कौन सी हैं? (सेट {set_num})"
                    hi_q["opts"] = ["श्रौत सूत्र", "गृह्य सूत्र", "धर्म सूत्र", "शुल्ब सूत्र"]
                    hi_q["sol"] = "ये सभी कल्प सूत्र की प्रमुख चार शाखाएं हैं।"
                elif "associated with the PGW culture" in q_text:
                    hi_q["q"] = f"निम्नलिखित में से कौन से पुरातात्विक स्थल PGW (चित्रित धूसर मृदभांड) संस्कृति से जुड़े हैं? (सेट {set_num})"
                    hi_q["opts"] = ["हस्तिनापुर", "अतरंजीखेड़ा", "जखेड़ा", "कुरुक्षेत्र"]
                    hi_q["sol"] = "ये सभी प्रसिद्ध PGW पुरातात्विक स्थल हैं जहाँ लोहे और चित्रित बर्तनों के साक्ष्य मिले हैं।"
                elif "Aryan origins debate" in q_text:
                    hi_q["q"] = f"आर्यों के मूल के संबंध में वाद-विवाद में साक्ष्य की निम्नलिखित में से किन श्रेणियों का उपयोग किया जाता है? (सेट {set_num})"
                    hi_q["opts"] = ["तुलनात्मक भाषाशास्त्र", "पुरातात्विक डेटा (PGW/OCP)", "प्राचीन डीएनए विश्लेषण", "खगोलीय गणना"]
                    hi_q["sol"] = "इतिहासकार इस जटिल वाद-विवाद को सुलझाने के लिए इन सभी वैज्ञानिक और साहित्यिक विषयों का सहारा लेते हैं।"

            # One-Liner replacements
            elif q["type"] == "One-Liner":
                term_match = None
                for eng_term, hi_term in terms_map.items():
                    if f"'{eng_term}'" in q_text or f" {eng_term} " in q_text:
                        term_match = hi_term
                        break
                
                if term_match:
                    if idx == 0:
                        hi_q["q"] = f"एक पंक्ति में '{term_match}' की ऋग्वैदिक अवधारणा को परिभाषित करें।"
                    elif idx == 1:
                        hi_q["q"] = f"उत्तर वैदिक संहिताओं में उल्लिखित '{term_match}' की अवधारणा को एक पंक्ति में परिभाषित करें।"
                    elif idx == 2:
                        hi_q["q"] = f"उपनिषदों से '{term_match}' की दार्शनिक अवधारणा को स्पष्ट करें।"
                    elif idx == 3:
                        hi_q["q"] = f"सहायक विषय (वेदांग) के रूप में '{term_match}' की भूमिका स्पष्ट करें।"
                    elif idx == 4:
                        hi_q["q"] = f"पुरातात्विक स्थल '{term_match}' के ऐतिहासिक महत्व को एक पंक्ति में स्पष्ट करें।"
                    else:
                        hi_q["q"] = f"आर्यों के मूल के संदर्भ में '{term_match}' की अवधारणा को स्पष्ट करें।"
                    hi_q["sol"] = f"इतिहास ग्रंथों के अनुसार '{term_match}' की एक पंक्ति में सटीक ऐतिहासिक परिभाषा और इसकी प्रासंगिकता।"

            # Match replacements
            elif q["type"] == "Match the Following":
                # Fallback to copy the translated values
                hi_q["q"] = q_text.replace("Match the columns representing", "स्तंभों का मिलान करें").replace("Match the Rigvedic", "ऋग्वैदिक मिलान करें").replace("Match", "मिलान करें")
                hi_q["sol"] = sol.replace("Rigveda", "ऋग्वेद").replace("Samaveda", "सामवेद").replace("Yajurveda", "यजुर्वेद")

        hi_mastery.append(hi_q)
        
    hi_sections.append({
        "title": hi_title,
        "content": hi_content,
        "masteryZone": hi_mastery
    })

hi_data["deepDive"]["sections"] = hi_sections

# Map Practice Questions to Hindi
hi_practice = []
for q in eng_data["practiceQuestions"]:
    hi_practice.append({
        "q": q["hi_q"],
        "opts": q["hi_opts"],
        "sol": q["hi_sol"]
    })

# Map Mock Test Questions to Hindi
hi_mock = []

# Question 1
hi_mock.append({
    "q": "अनातोलिया (तुर्की) से प्राप्त बोगजकोई (Boghazkoi) शिलालेख (लगभग 1400 ईसा पूर्व) वैदिक इतिहास के लिए क्यों महत्वपूर्ण हैं?",
    "opts": [
        "एक राजनीतिक संधि में वैदिक देवताओं मित्र, वरुण, इंद्र और नासत्य के नाम मिलते हैं",
        "इनमें भारत-आर्यों के सैन्य प्रवास मार्गों का वर्णन है",
        "इनमें अग्नि को समर्पित सबसे पहले ज्ञात भजनों का रिकॉर्ड है",
        "इनमें ऋग्वैदिक गोत्रों से मेल खाती वंशावली सूचियाँ हैं"
    ],
    "ans": 0,
    "sol": "मितन्नी-हित्ती संधि के बोगजकोई शिलालेख में चार वैदिक देवताओं (मित्र, वरुण, इंद्र, नासत्य) को गवाह या रक्षक के रूप में बुलाया गया है, जो लगभग 1400 ईसा पूर्व पश्चिम एशिया में उनके सम्मान को दर्शाता है।"
})

# Question 2
hi_mock.append({
    "q": "ऋग्वेद में उल्लिखित जनजातीय सभाओं के संबंध में निम्नलिखित कथनों पर विचार कीजिए:\n1. विधात सबसे पुरानी सभा थी जिसमें धर्मनिरपेक्ष और धार्मिक दोनों कार्य होते थे।\n2. महिलाओं को सभा और समिति में भाग लेने से पूरी तरह से बाहर रखा गया था।\nउपर्युक्त कथनों में से कौन सा/से सही है/हैं?",
    "opts": ["1 केवल", "2 केवल", "1 और 2 दोनों", "न तो 1 और न ही 2"],
    "ans": 0,
    "sol": "कथन 1 सही है। कथन 2 गलत है क्योंकि ऋग्वैदिक काल में महिलाएं सभा और विधात सभाओं में सक्रिय रूप से भाग लेती थीं।"
})

# Question 3
hi_mock.append({
    "q": "सदानीरा नदी के पार वैदिक संस्कृति के पूर्व की ओर विस्तार का वर्णन करने वाली विदेघ माथव और अग्नि वैश्वानर की कथा किस ग्रंथ में दर्ज है?",
    "opts": ["शतपथ ब्राह्मण", "ऐतरेय ब्राह्मण", "छान्दोग्य उपनिषद", "गोपथ ब्राह्मण"],
    "ans": 0,
    "sol": "शतपथ ब्राह्मण (यजुर्वेद) में विदेघ माथव की कथा दर्ज है जो गंगा के मैदानों को बसाने के लिए यज्ञ की अग्नि को पूर्व की ओर ले गए थे।"
})

# Question 4
hi_mock.append({
    "q": "उत्तर वैदिक काल से जुड़ी चित्रित धूसर मृदभांड (PGW) संस्कृति की प्रमुख विशेषताएं निम्नलिखित में से कौन सी हैं/हैं?\n1. कृषि और युद्ध के लिए लोहे के उपकरणों का व्यापक उपयोग।\n2. घोड़ों को पालतू बनाना और लोहे के पहियों वाले रथों का उपयोग।\n3. भगवानपुरा जैसे स्थलों पर उत्तर-हड़प्पा स्तरों के साथ स्तर-शास्त्रीय (stratigraphic) ओवरलैप।\nनीचे दिए गए कूट का उपयोग करके सही उत्तर चुनिए:",
    "opts": ["1 और 2 केवल", "1 और 3 केवल", "2 और 3 केवल", "1, 2 और 3"],
    "ans": 1,
    "sol": "कथन 1 और 3 सही हैं। PGW में रथों में लोहे की तीलियों (iron-spoked) वाले पहिये नहीं थे (वे लकड़ी के थे, और लोहे की तीलियाँ बाद की तकनीक है)।"
})

# Question 5
hi_mock.append({
    "q": "उपनिषदों के संदर्भ में, निम्नलिखित कथनों पर विचार कीजिए:\n1. वे कर्मकांडीय क्रिया से आध्यात्मिक ज्ञान की ओर संक्रमण का प्रतिनिधित्व करते हैं।\n2. मुण्डक उपनिषद कर्मकांडों की तुलना अस्थिर जर्जर नौकाओं से करता है।\n3. सबसे शुरुआती उपनिषद शास्त्रीय संस्कृत छंद (Classical Sanskrit verse) में लिखे गए हैं।\nउपर्युक्त कथनों में से कौन सा/से सही है/हैं?",
    "opts": ["1 और 2 केवल", "2 और 3 केवल", "1 और 3 केवल", "1, 2 और 3"],
    "ans": 0,
    "sol": "कथन 1 और 2 सही हैं। सबसे पुराने उपनिषद (बृहदारण्यक, छान्दोग्य) गद्य में लिखे गए हैं, न कि शास्त्रीय संस्कृत छंदों में।"
})

# Question 6
hi_mock.append({
    "q": "निम्नलिखित वैदिक नदियों का उनके आधुनिक समकक्षों से मिलान कीजिए:\nI. वितस्ता - A. झेलम\nII. असिकनी - B. चिनाब\nIII. परुष्णी - C. रावी\nIV. विपासा - D. ब्यास\nसही कूट चुनिए:",
    "opts": [
        "I-A, II-B, III-C, IV-D",
        "I-B, II-A, III-C, IV-D",
        "I-A, II-B, III-D, IV-C",
        "I-D, II-C, III-B, IV-A"
    ],
    "ans": 0,
    "sol": "सही मिलान हैं: वितस्ता (झेलम), असिकनी (चिनाब), परुष्णी (रावी), और विपासा (ब्यास)।"
})

# Question 7
hi_mock.append({
    "q": "निम्नलिखित में से कौन सा विकल्प अथर्ववेद के चरित्र का सही वर्णन करता है?",
    "opts": [
        "यह लोकप्रिय वैदिक जीवन का प्रतिनिधित्व करने वाले लोक जादू, टोने और चिकित्सा का संकलन है",
        "इसमें केवल यज्ञों के लिए कर्मकांडीय निर्देश शामिल हैं",
        "यह पूरी तरह से सोम और अग्नि की स्तुति के लिए समर्पित है",
        "इसकी रचना ऋग्वेद संहिता से पहले की गई थी"
    ],
    "ans": 0,
    "sol": "अथर्ववेद अद्वितीय है क्योंकि यह गैर-पुरोहित वर्गों के लोकप्रिय धर्म, उपचार के मंत्रों और रोजमर्रा की सामाजिक स्थितियों को दर्शाता है।"
})

# Question 8
hi_mock.append({
    "q": "वेदांग वेद के सहायक विज्ञान हैं। निम्नलिखित में से कौन सा सही सुमेलित नहीं है?",
    "opts": ["शिक्षा — निरुक्त/व्युत्पत्तिशास्त्र", "व्याकरण — व्याकरण", "कल्प — कर्मकांड प्रक्रिया", "ज्योतिष — खगोल विज्ञान"],
    "ans": 0,
    "sol": "शिक्षा का अर्थ ध्वन्यात्मकता/उच्चारण है (वेद की नासिका)। व्युत्पत्तिशास्त्र निरुक्त कहलाता है।"
})

# Question 9
hi_mock.append({
    "q": "प्राचीन भारत के ऐतिहासिक पुनर्निर्माण के लिए ग्रंथों, पुरातत्व और नृवंशविज्ञान को जोड़ने वाली 'संयुक्त पद्धति' (combined method) की शुरुआत किसने की थी?",
    "opts": ["डी.डी. कोसांबी", "रोमिला थापर", "मैक्स मूलर", "आर.एस. शर्मा"],
    "ans": 0,
    "sol": "डी.डी. कोसांबी ने प्राचीन भारत के अध्ययन में ग्रंथों, भौतिक संस्कृति और नृवंशविज्ञान को एकीकृत करते हुए संयुक्त पद्धति की शुरुआत की थी।"
})

# Question 10
hi_mock.append({
    "q": "प्रारंभिक वैदिक काल से उत्तर वैदिक काल में संक्रमण के दौरान, अर्थव्यवस्था में कौन सा महत्वपूर्ण बदलाव आया?",
    "opts": [
        "पशुपालक घुमंतू मवेशी-पालन से लोहे की सहायता से स्थायी कृषि की ओर बदलाव",
        "शहरी व्यापार-आधारित शिल्पकला से ग्रामीण कृषि की ओर बदलाव",
        "गेहूं उत्पादक खेतों से पशुपालक वन संपदा की ओर बदलाव",
        "लोहा गलाने वाले केंद्रों से कांस्य धातु कर्म की प्रधानता की ओर बदलाव"
    ],
    "ans": 0,
    "sol": "प्रारंभिक वैदिक काल मुख्य रूप से खानाबदोश पशुपालन (गायों) पर आधारित था, जो उत्तर वैदिक युग में लोहे की मदद से जंगल साफ कर बसे हुए कृषि जीवन (धान, गेहूं) में परिवर्तित हो गया।"
})

hi_data["mockTestQuestions"] = hi_mock

# Save hi/content.json
with open(os.path.join(hi_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, indent=2, ensure_ascii=False)

print("SUCCESS: hi/content.json generated.")
