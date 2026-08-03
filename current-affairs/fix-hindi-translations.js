/**
 * Fix Hindi translations by replacing English content with proper Hindi translations
 * Maps each topic title to its complete Hindi translation
 */
const fs = require('fs');
const path = require('path');

const DIR = path.join(__dirname, 'data', 'weekly', '2026', '06');
const files = fs.readdirSync(DIR).filter(f => f.endsWith('.json'));

// Complete Hindi translations for all topics
const hindiTranslations = {
    'World Brain Tumour Day Observed': {
        detail: 'विश्व ब्रेन ट्यूमर दिवस ब्रेन ट्यूमर के बारे में जागरूकता बढ़ाता है और मरीजों का समर्थन करता है।',
        exam: 'दिवस-तिथि वन-लाइनर।',
        remember: 'विश्व ब्रेन ट्यूमर दिवस: 8 जून।',
        facts: ['8 जून', 'ब्रेन ट्यूमर जागरूकता', 'स्वास्थ्य पालन']
    },
    'World Oceans Day 2026 Observed': {
        detail: 'विश्व महासागर दिवस ने "रीइमैजिन: बियॉनड द वर्ल्ड वी नो" थीम के तहत समुद्री पारिस्थितिकी संरक्षण को बढ़ावा दिया।',
        exam: 'दिवस-थीम प्रश्नों के लिए महत्वपूर्ण।',
        remember: 'विश्व महासागर दिवस 2026: रीइमैजिन थीम।',
        facts: ['8 जून', 'थीम: रीइमैजिन - बियॉनड द वर्ल्ड वी नो...', 'समुद्री पारिस्थितिकी संरक्षण', 'संयुक्त राष्ट्र']
    },
    'World Day Against Child Labour Observed': {
        detail: 'बाल श्रम के विरुद्ध विश्व दिवस ने "रेड कार्ड टू चाइल्ड लेबर" स्लोगन के तहत वैश्विक सुरक्षात्मक प्रवर्तन को आगे बढ़ाया।',
        exam: 'दिवस-स्लोगन मिलान के लिए महत्वपूर्ण।',
        remember: 'बाल श्रम दिवस: 12 जून, रेड कार्ड स्लोगन।',
        facts: ['12 जून', 'स्लोगन: रेड कार्ड टू चाइल्ड लेबर...', 'आईएलओ']
    },
    'International Albinism Awareness Day Observed': {
        detail: 'अंतर्राष्ट्रीय ऐल्बिनिज़म जागरूकता दिवस ऐल्बिनिज़म से पीड़ित व्यक्तियों के अधिकारों को आगे बढ़ाता है।',
        exam: 'दिवस-तिथि वन-लाइनर।',
        remember: 'ऐल्बिनिज़म जागरूकता दिवस: 13 जून।',
        facts: ['13 जून', 'संयुक्त राष्ट्र पालन']
    },
    'Supreme Court: Trauma Care Part of Right to Life': {
        detail: 'सुप्रीम कोर्ट ने घोषणा की कि आघात देखभाल तक पहुँच संविधान के अनुच्छेद 21 के तहत जीवन के अधिकार का अभिन्न हिस्सा है।',
        exam: 'संवैधानिक अधिकारों और ऐतिहासिक निर्णयों के लिए महत्वपूर्ण।',
        remember: 'आघात देखभाल: अनुच्छेद 21 जीवन के अधिकार का हिस्सा।',
        facts: ['अनुच्छेद 21', 'जीवन का अधिकार', 'आघात देखभाल तक पहुँच', 'सुप्रीम कोर्ट']
    },
    'World Environment Day 2026 Observed': {
        detail: 'विश्व पर्यावरण दिवस 2026 ने #NowForClimate थीम के तहत बाकू, अज़रबैजान में जलवायु पहल पर ध्यान केंद्रित किया।',
        exam: 'दिवस-थीम-मेज़बान देश प्रश्नों के लिए महत्वपूर्ण।',
        remember: 'डब्ल्यूईडी 2026: #NowForClimate, बाकू में आयोजित।',
        facts: ['5 जून', 'थीम: #NowForClimate', 'बाकू, अज़रबैजान में आयोजित', 'यूएनईपी']
    },
    'World Food Safety Day Observed': {
        detail: 'विश्व खाद्य सुरक्षा दिवस ने सुरक्षित खाद्य प्रथाओं और मानकों के प्रति जागरूकता बढ़ाई।',
        exam: 'दिवस-संगठन मिलान।',
        remember: 'विश्व खाद्य सुरक्षा दिवस: 7 जून।',
        facts: ['7 जून', 'डब्ल्यूएचओ और एफएओ', 'खाद्य सुरक्षा मानक']
    },
    'World Bicycle Day Observed': {
        detail: 'विश्व साइकिल दिवस साइकिल को एक सरल, किफायती और टिकाऊ परिवहन के साधन के रूप में बढ़ावा देता है।',
        exam: 'दिवस-तिथि वन-लाइनर।',
        remember: 'विश्व साइकिल दिवस: 3 जून।',
        facts: ['3 जून', 'संयुक्त राष्ट्र', 'टिकाऊ गतिशीलता']
    },
    'International Day of Innocent Children Victims of Aggression': {
        detail: 'यह दिवस आक्रामकता और हिंसा से प्रभावित बच्चों के अधिकारों की रक्षा के प्रति प्रतिबद्धता की पुष्टि करता है।',
        exam: 'दिवस-तिथि वन-लाइनर।',
        remember: 'आक्रामकता के निर्दोष बाल पीड़ितों का दिवस: 4 जून।',
        facts: ['4 जून', 'संयुक्त राष्ट्र पालन']
    }
};

// Common translations for facts
const factTranslations = {
    'June 8': '8 जून', 'June 12': '12 जून', 'June 13': '13 जून', 'June 15': '15 जून',
    'June 17': '17 जून', 'June 19': '19 जून', 'June 18': '18 जून', 'June 20': '20 जून',
    'June 21': '21 जून', 'June 22': '22 जून', 'June 23': '23 जून', 'June 24': '24 जून',
    'June 25': '25 जून', 'June 26': '26 जून', 'June 27': '27 जून', 'June 28': '28 जून',
    'June 29': '29 जून', 'June 30': '30 जून', 'June 1': '1 जून', 'June 2': '2 जून',
    'June 3': '3 जून', 'June 4': '4 जून', 'June 5': '5 जून', 'June 6': '6 जून',
    'June 7': '7 जून', 'June 9': '9 जून', 'June 10': '10 जून', 'June 11': '11 जून',
    'June 14': '14 जून', 'June 16': '16 जून',
    'Brain tumour awareness': 'ब्रेन ट्यूमर जागरूकता',
    'Health observance': 'स्वास्थ्य पालन',
    'Marine ecosystem conservation': 'समुद्री पारिस्थितिकी संरक्षण',
    'UN': 'संयुक्त राष्ट्र',
    'Land Degradation Neutrality': 'भूमि क्षरण उदासीनता',
    'UNCCD': 'यूएनसीसीडी',
    'Crocodile habitat protection': 'मगरमच्छ आवास संरक्षण',
    'Sickle cell awareness': 'सिकल सेल जागरूकता',
    'Renewable transition': 'नवीकरणीय संक्रमण',
    'Theme: Our wind, our community': 'थीम: हमारा पवन, हमारा समुदाय',
    'Important Days': 'महत्वपूर्ण दिवस',
    'Annual observance': 'वार्षिक पालन',
    'Theme-based observance': 'थीम-आधारित पालन',
    'Health observance': 'स्वास्थ्य पालन',
    'Environment observance': 'पर्यावरण पालन',
    'Social observance': 'सामाजिक पालन',
    'UN observance': 'संयुक्त राष्ट्र पालन',
    'Drought and Desertification': 'सूखा और मरुभूमिकरण'
};

let totalFixed = 0;

for (const file of files) {
    const filePath = path.join(DIR, file);
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    if (!data.topics || !Array.isArray(data.topics)) continue;

    let fileFixed = 0;

    for (const topic of data.topics) {
        if (!topic.hi || typeof topic.hi !== 'object') continue;

        // Check if we have a complete translation for this topic
        if (hindiTranslations[topic.title]) {
            const hi = hindiTranslations[topic.title];
            if (hi.detail) topic.hi.detail = hi.detail;
            if (hi.exam) topic.hi.exam = hi.exam;
            if (hi.remember) topic.hi.remember = hi.remember;
            if (hi.facts) topic.hi.facts = hi.facts;
            fileFixed++;
        } else {
            // For topics without complete translations, clean up the detail/remember fields
            // Remove English text patterns that shouldn't be there
            if (topic.hi.detail && topic.hi.detail.includes(' यह ')) {
                // Keep only the Hindi part before the English text
                const hindiPart = topic.hi.detail.split('।')[0];
                if (hindiPart && hindiPart.length > 10) {
                    topic.hi.detail = hindiPart + '।';
                    fileFixed++;
                }
            }

            if (topic.hi.remember && topic.hi.remember.includes('W')) {
                // Replace with a clean Hindi version
                topic.hi.remember = `याद रखें: ${topic.title}: ${topic.date}.`;
                fileFixed++;
            }

            // Fix facts array - translate any remaining English facts
            if (Array.isArray(topic.hi.facts)) {
                let factsChanged = false;
                topic.hi.facts = topic.hi.facts.map(f => {
                    const translated = factTranslations[f] || f;
                    if (translated !== f) factsChanged = true;
                    return translated;
                });
                if (factsChanged) fileFixed++;
            }
        }
    }

    if (fileFixed > 0) {
        fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf8');
        console.log(`✓ ${file}: ${fileFixed} topics fixed`);
        totalFixed += fileFixed;
    }
}

console.log(`\nTotal topics fixed: ${totalFixed}`);
console.log('Hindi translation cleanup completed!');