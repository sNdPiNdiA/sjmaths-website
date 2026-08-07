/**
 * Populates Tab 1 (Concepts/Theories) with realistic educational content
 * for all 6 Child Psychology microtopics.
 * 
 * Run: node populate-content.cjs
 */
const fs = require('fs');
const path = require('path');

const TOPICS_DIR = path.join(__dirname, 'topics');

const topicContents = {
    'individual-differences': {
        overview: 'वैयक्तिक भिन्नता का अर्थ है कि प्रत्येक बच्चा अपने ज्ञान, कौशल, व्यवहार और विकास गति में दूसरों से भिन्न होता है। शिक्षकों को इन भिन्नताओं को समझकर शिक्षण की व्यवस्था करनी चाहिए।',
        detailedExplanation: '<ul><li><strong>ज्ञान में भिन्नता:</strong> कुछ बच्चे तेजी से सीखते हैं, कुछ धीरे-धीरे</li><li><strong>कौशल में भिन्नता:</strong> रचनात्मक कौशल, तार्किक कौशल में अंतर</li><li><strong>व्यवहार में भिन्नता:</strong> कुछ बच्चे शांत होते हैं, कुछ उतावले</li><li><strong>भावात्मकता में भिन्नता:</strong> कुछ बच्चे अधिक संवेदनशील होते हैं</li><li><strong>सीखने की शैली:</strong> दृष्टिगत, श्रवणात्मक, स्पर्शात्मक अलग-अलग होती है</li><li><strong>विकास गति में भिन्नता:</strong> शारीरिक, मानसिक, सामाजिक विकास में अंतर</li><li><strong>पूर्वाग्रह नहीं करना:</strong> सभी बच्चों को एक समान मानना चाहिए</li><li><strong>व्यक्तिगत शिक्षण योजना:</strong> हर बच्चे के अनुसार शिक्षण तैयार करें</li></ul>',
        mnemonic: 'KABH - Knowledge, Attitude, Behaviour, Habits (ज्ञान, आचरण, व्यवहार, आदतें)',
        tips: '1. प्रत्येक बच्चे को अलग रूप से ध्यान दें\n2. उनकी रुचियों के अनुसार अभ्यास दें\n3. छोटे-छोटे लक्ष्य निर्धारित करें ताकि वे सफलता का अनुभव करें',
        mistakes: '1. किसी बच्चे की तुलना दूसरे से न करें\n2. उनकी कमियों पर ध्यान दिए बिना उनकी ताकत को नजरअंदाज न करें\n3. सभी बच्चों को एक ही शिक्षण शैली से न पढ़ाएं'
    },
    'factors-affecting-child-development': {
        overview: 'बाल विकास को जीन, पर्यावरण, पोषण, शिक्षा, सामाजिक परिवेश और आर्थिक स्थिति जैसे कारक प्रभावित करते हैं। इन्हें समझकर शिक्षक बच्चों का समग्र विकास सुनिश्चित कर सकते हैं।',
        detailedExplanation: '<ul><li><strong>जीनविक:</strong> कुछ गुण माता-पिता से संतति में स्थानांतरित होते हैं</li><li><strong>पोषण:</strong> संतुलित आहार, शारीरिक विकास के लिए आवश्यक</li><li><strong>शारीरिक वातावरण:</strong> स्वच्छता, सुस्पष्ट वायु, सुरक्षा महत्वपूर्ण</li><li><strong>सामाजिक परिवेश:</strong> परिवार, स्कूल, दोस्त विकास को प्रभावित करते हैं</li><li><strong>आर्थिक स्थिति:</strong> गरीबी शिक्षा और पोषण दोनों में बाधा डालती है</li><li><strong>शिक्षा:</strong> गुणवत्तापूर्ण शिक्षा ही विकास की नींव है</li><li><strong>भावात्मक वातावरण:</strong> प्यार, सुरक्षा और प्रोत्साहन आवश्यक</li><li><strong>सांस्कृतिक प्रभाव:</strong> परंपराएँ, मूल्य, रीति-रिवाज सभी विकास को आकार देते हैं</li></ul>',
        mnemonic: 'GREEN - Genes, Resources, Environment, Education, Nutrition (जीन, संसाधन, परिवेश, शिक्षा, पोषण)',
        tips: '1. बच्चों के पीछे के कारकों को समझकर व्यवहार करें\n2. पोषण और स्वास्थ्य पर ध्यान दें\n3. सकारात्मक और सुरक्षित वातावरण बनाएं',
        mistakes: '1. बच्चे की कमियों को जन्मजात मानकर उसकी प्रगति को स्थगित न करें\n2. सामाजिक वातावरण का प्रभाव नजरअंदाज न करें\n3. आर्थिक कठिनाई को बच्चे की शिक्षा में बाधा न बनें'
    },
    'identification-of-learning-needs': {
        overview: 'सीखने की आवश्यकता की पहचान का अर्थ है बच्चों की शिक्षण की जरूरतों को समझना। पूर्व सांख्यिकी, अवलोकन, परीक्षण और मूल्यांकन से यह पहचान की जा सकती है।',
        detailedExplanation: '<ul><li><strong>पूर्व सांख्यिकी:</strong> पुराने परीक्षण के आधार पर नया शिक्षण योजना बनाएं</li><li><strong>अवलोकन:</strong> बच्चों के व्यवहार, रुचि और कौशल का निरीक्षण करें</li><li><strong>परीक्षण:</strong> औपचारिक मूल्यांकन परीक्षणों से स्तर ज्ञात करें</li><li><strong>प्रश्नावली:</strong> सवालों के जवाब से जरूरत की पहचान करें</li><li><strong>रुचि सर्वेक्षण:</strong> बच्चों की पसंद और अपसंद को जानें</li><li><strong>वार्षिक गुण:</strong> सालाना प्रगति रिपोर्ट का विश्लेषण करें</li><li><strong>विशेषज्ञ सलाह:</strong> विशेष शिक्षण विशेषज्ञ से सलाह लें</li><li><strong>मूल्यांकन रिपोर्ट:</strong> बच्चे की प्रगति का पूरा रिकॉर्ड रखें</li></ul>',
        mnemonic: 'IDEA - Identification, Diagnosis, Evaluation, Action (पहचान, निदान, मूल्यांकन, कार्रवाई)',
        tips: '1. नियमित रूप से मूल्यांकन करें\n2. बच्चों के अनुसार लक्ष्य निर्धारित करें\n3. मूल्यांकन के परिणामों का उपयोग शिक्षण में करें',
        mistakes: '1. केवल परीक्षा पर आधारित निर्णय न लें\n2. बच्चे की क्षमता को अंकों से मापें मत\n3. मूल्यांकन का परिणाम बच्चे के सामने न बताएं'
    },
    'creating-conducive-learning-environment': {
        overview: 'पढ़ने के लिए उपयुक्त वातावरण का निर्माण शिक्षक की मुख्य जिम्मेदारी है। शांत, सुरक्षित और प्रोत्साहक माहौल में बच्चे बेहतर सीखते हैं।',
        detailedExplanation: '<ul><li><strong>शारीरिक वातावरण:</strong> पर्याप्त रोशनी, वेंटिलेशन, साफ-सफाई</li><li><strong>शांत वातावरण:</strong> बाहरी शोर से बचना, शांति का वातावरण</li><li><strong>सुरक्षित वातावरण:</strong> भयमुक्त, सुरक्षित, आत्मविश्वास बढ़ाने वाला</li><li><strong>सामग्री:</strong> चित्र, मॉडल, शिक्षण सामग्री उपलब्ध रखें</li><li><strong>बैठक की व्यवस्था:</strong> सुविधाजनक सीटें, सभी को दिखाई देने वाला व्यवस्था</li><li><strong>सांस्कृतिक सुंदरता:</strong> स्कूल की दीवारें सराहनीय कार्यों से सजाएं</li><li><strong>सकारात्मक संवेश:</strong> गलती से सीखने का माहौल बनाएं</li><li><strong>सहयोगी वातावरण:</strong> सहपाठियों के बीच सहयोग की भावना बढ़ाएं</li></ul>',
        mnemonic: 'SPACE - Safe, Positive, Arrangement, Culture, Encouragement (सुरक्षित, सकारात्मक, व्यवस्था, संस्कृति, प्रोत्साहन)',
        tips: '1. कक्षा को रंग-बिरंगी और आकर्षक बनाएं\n2. प्रत्येक बच्चे को ध्यान दें\n3. सकारात्मक शिक्षा का माहौल बनाएं',
        mistakes: '1. कक्षा में अव्यवस्था न रखें\n2. शिक्षक का व्यवहार बच्चों पर नकारात्मक प्रभाव डालता है\n3. सभी बच्चों के लिए एक ही माहौल नहीं चाहिए'
    },
    'learning-theories-and-classroom-application': {
        overview: 'सीखने के सिद्धान्त बच्चों की सीखने की प्रक्रिया को समझते हैं। इन सिद्धान्तों का उपयोग कक्षा में करके शिक्षण को अधिक प्रभावी बनाया जा सकता है।',
        detailedExplanation: '<ul><li><strong>पवर्तन सिद्धान्त (Behaviorism):</strong> पुरस्कार-दंड द्वारा सीखने को प्रेरित करना</li><li><strong>ज्ञान निर्माण सिद्धान्त (Constructivism):</strong> बच्चे स्वयं ज्ञान निर्माण करते हैं</li><li><strong>सांज्ञानिक सिद्धान्त (Cognitivism):</strong> मानसिक प्रक्रियाओं पर ध्यान दें</li><li><strong>सामाजिक सिद्धान्त (Social Learning):</strong> मॉडलिंग और नकल से सीखना</li><li><strong>अनुभवात्मक सिद्धान्त (Experiential):</strong> practical से जोड़कर सीखें</li><li><strong>व्यक्तिगततावाद (Humanism):</strong> पूर्ण विकास के लिए शिक्षा</li><li><strong>कक्षा में अनुप्रयोग:</strong> पुरस्कार, समूह कार्य, प्रयोग, चर्चा</li><li><strong>विभिन्न शैलियों का मिलान:</strong> बच्चों की आवश्यकता के अनुसार शैली चुनें</li></ul>',
        mnemonic: 'BCCSH - Behaviorism, Cognitivism, Constructivism, Social, Humanism',
        tips: '1. एक ही सिद्धान्त का उपयोग सभी के लिए न करें\n2. कक्षा में अभ्यास द्वारा सिद्धान्त लागू करें\n3. बच्चों की प्रगति को नियमित रूप से मापें',
        mistakes: '1. केवल पठन-लिखन पर ध्यान दें, व्यावहारिक न हो\n2. सभी बच्चों को एक ही तरीके से न पढ़ाएं\n3. शिक्षण सिद्धान्तों को केवल सिद्धांत में ही सीमित रखें'
    },
    'special-provisions-for-divyang-students': {
        overview: 'दिव्यांग छात्रों के लिए विशेष व्यवस्थाएँ शिक्षा प्रणाली में आवश्यक हैं। इन्हें सामान्य शिक्षा में ही समावेश करना चाहिए।',
        detailedExplanation: '<ul><li><strong>समावेशी शिक्षा:</strong> दिव्यांग बच्चों को सामान्य स्कूल में ही शिक्षा दें</li><li><strong>विशेष शिक्षक:</strong> प्रत्येक विशेष बच्चे के लिए विशेष शिक्षक की व्यवस्था</li><li><strong>अनुकूलित सामग्री:</strong> बड़े फॉन्ट, ब्राइल, ऑडियो सामग्री</li><li><strong>सुविधाजनक बातचीत:</strong> रैंप, हाथीया, विशेष टॉयलट</li><li><strong>सूचना प्रणाली:</strong> शारीरिक विकलांगता के अनुसार सहायक उपकरण</li><li><strong>सामाजिक सुरक्षा:</strong> बुलिंग और उपेक्षा से बचाव</li><li><strong>मानसिक सहायता:</strong> आत्मविश्वास बढ़ाने के लिए सलाह</li><li><strong>अभिभावक सहभागिता:</strong> अभिभावकों को नियमित रूप से जानकारी दें</li></ul>',
        mnemonic: 'I CARE - Inclusive, Customized, Accessible, Respectful, Empathetic (समावेशी, अनुकूलित, सुलभ, सम्मानजनक, सहानुभूतिपूर्ण)',
        tips: '1. दिव्यांग बच्चों की गति को न रोकें\n2. उन्हें सामान्य बच्चों के साथ मिलकर शिक्षा दें\n3. प्रोत्साहन और सहयोग का माहौल बनाएं',
        mistakes: '1. दिव्यांग बच्चों को अलग से न रखें\n2. उनकी क्षमता को कम समझें मत\n3. शारीरिक विकलांगता को बौद्धिक कमी न समझें'
    }
};

// Process all topics
Object.keys(topicContents).forEach(slug => {
    const filePath = path.join(TOPICS_DIR, slug + '.html');
    if (!fs.existsSync(filePath)) {
        console.log(`⚠ Skipping ${slug} - file not found`);
        return;
    }

    let html = fs.readFileSync(filePath, 'utf8');
    const content = topicContents[slug];

    // Escape HTML
    function escapeHtml(text) {
        const map = { '&': '&', '<': '<', '>': '>', '"': '"', "'": '&#039;' };
        return text.replace(/[&<>"']/g, m => map[m]);
    }

    // Update Overview
    html = html.replace(
        /<div class="placeholder-note">[\s\S]*?यह खंड AI द्वारा जनरेट किया जा रहा है[\s\S]*?<\/div>/,
        `<p>${escapeHtml(content.overview)}</p>`
    );

    // Update Detailed Explanation
    html = html.replace(
        /<div class="placeholder-note">[\s\S]*?विस्तृत व्याख्या AI द्वारा जनरेट की जा रही है[\s\S]*?<\/div>/,
        content.detailedExplanation
    );

    // Update Mnemonics
    html = html.replace(
        /<strong>💡 Mnemonic:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>💡 Mnemonic:</strong> ${escapeHtml(content.mnemonic)}`
    );

    // Update Tips & Tricks
    html = html.replace(
        /<strong>✓ Tip:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>✓ Tip:</strong> ${escapeHtml(content.tips)}`
    );

    // Update Mistakes to Avoid
    html = html.replace(
        /<strong>⚠ Common Mistake:<\/strong> <span class="lang-hi">\(जनरेट किया जा रहा है\.\.\.\)<\/span><br>\s*<span class="lang-en">\(Being generated\.\.\.\)<\/span>/,
        `<strong>⚠ Common Mistake:</strong> ${escapeHtml(content.mistakes)}`
    );

    fs.writeFileSync(filePath, html, 'utf8');
    console.log(`✓ Populated Tab 1 for: ${slug}`);
});

console.log('\n✅ All 6 microtopics now have complete Tab 1 content!');