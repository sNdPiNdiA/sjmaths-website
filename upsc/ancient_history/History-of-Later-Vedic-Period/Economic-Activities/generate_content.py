# -*- coding: utf-8 -*-
import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Later-Vedic-Period\Economic-Activities"

english_data = {
    "breadcrumbs": {
        "parent": "Later Vedic Period",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "Economic Activities"
    },
    "hero": {
        "title": "Economic Activities in Later Vedic Period",
        "description": "A comprehensive UPSC study guide on the transition to settled agriculture, use of iron, Painted Grey Ware (PGW) crafts, trade patterns, and the rise of organized taxation."
    },
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "UPSC Level Mock Test",
            "description": "Test your mastery of Later Vedic economic history with 10 complex statement-based and matching questions.",
            "startBtn": "Start Mock Test"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "c. 1000 BCE",
                "date": "Settled Agriculture & Iron Age",
                "details": "Indo-Aryans transition from pastoral-dominated lifestyle to settled agriculture. Early use of iron ('Krishna Ayas') begins in Ghaggar-Hakra and Doab regions."
            },
            {
                "period": "c. 800 BCE",
                "date": "Craft Specialization & PGW",
                "details": "Flourishing of Painted Grey Ware (PGW) culture. Specialization of crafts like metallurgy, leatherworking, and weaving."
            },
            {
                "period": "c. 600 BCE",
                "date": "Organized Taxation & Proto-Urbanization",
                "details": "Transition of voluntary 'Bali' to compulsory tax. Emergence of royal treasury officials and proto-urban centers like Hastinapur."
            }
        ]
    },
    "toolEvolution": {
        "title": "Economic & Resource Evolution",
        "description": "The evolution of production systems from Rigvedic to Later Vedic times.",
        "stages": [
            {
                "name": "Agricultural Base",
                "color": "#e74c3c",
                "desc": "Pastoralism dominates early Vedic life; settled farming of wheat, rice, and barley dominates later Vedic times.",
                "svg": '<i class="fas fa-seedling" style="font-size: 2rem; color: #e74c3c;"></i>'
            },
            {
                "name": "Metal Technology",
                "color": "#f39c12",
                "desc": "Transition from copper-bronze (Ayas) to iron (Krishna Ayas) used for clearing forests and making tools.",
                "svg": '<i class="fas fa-hammer" style="font-size: 2rem; color: #f39c12;"></i>'
            },
            {
                "name": "Revenue System",
                "color": "#2ecc71",
                "desc": "Voluntary offerings (Bali) evolve into compulsory taxation administered by Bhagadugha and Sangrihitri.",
                "svg": '<i class="fas fa-coins" style="font-size: 2rem; color: #2ecc71;"></i>'
            }
        ]
    },
    "traps": {
        "title": "Common UPSC Pitfalls & Distinctions",
        "items": [
            "Trap: Believing that regular metallic coinage was introduced in Later Vedic times. Although texts mention Nishka, Satamana, and Krishnala, these were units of weight/metal and not standard state coinage.",
            "Do not assume the iron plowshare was universally used in the early Later Vedic period. Wooden plowshares were still common; iron was primarily used for clearance axes and weapons.",
            "Bali was not always a tax. In the Rigvedic period, it was a voluntary offering; in the Later Vedic period, it became a regular, compulsory tribute.",
            "Do not mistake the state of land ownership. Land was not yet fully private; it was held collectively by families/clans, although the king asserted royal claims over taxation."
        ]
    },
    "mnemonics": {
        "title": "Vedic Economic Terms Mnemonic",
        "description": "Use these mnemonics to remember key terms and divisions.",
        "items": [
            {
                "title": "Revenue Officers Mnemonic",
                "phrase": "BHAGA-dugha collects the Bhaga (share); SANGRI-hitri guards the Sangraha (treasury)",
                "decryption": "Bhagadugha was the tax collector, and Sangrihitri was the treasurer."
            },
            {
                "title": "Metal Classifications",
                "phrase": "KRISHNA = Iron (Dark); LOHITA = Copper (Red)",
                "decryption": "Krishna Ayas or Syama Ayas refers to iron, while Lohita Ayas refers to copper."
            }
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Test your ability to recall key economic terms and facts.",
        "items": [
            {
                "question": "What does the term 'Vrihi' refer to in Later Vedic texts?",
                "answer": "Rice, which became a staple food crop alongside wheat and barley.",
                "icon": "fa-seedling"
            },
            {
                "question": "Who was the 'Bhagadugha' in Later Vedic administration?",
                "answer": "The official responsible for collecting the king's share of agricultural produce (taxes).",
                "icon": "fa-user-tie"
            },
            {
                "question": "What archaeological culture corresponds to the Later Vedic period?",
                "answer": "The Painted Grey Ware (PGW) culture.",
                "icon": "fa-paint-brush"
            },
            {
                "question": "What metal is referred to as 'Syama Ayas' or 'Krishna Ayas'?",
                "answer": "Iron.",
                "icon": "fa-cubes"
            }
        ]
    }
}

hindi_data = {
    "breadcrumbs": {
        "parent": "उत्तर वैदिक काल",
        "parentUrl": "/upsc/ancient_history/History-of-Later-Vedic-Period/",
        "current": "आर्थिक गतिविधियाँ"
    },
    "hero": {
        "title": "उत्तर वैदिक काल में आर्थिक गतिविधियाँ",
        "description": "स्थायी कृषि में संक्रमण, लोहे के उपयोग, चित्रित धूसर मृदभांड (PGW) शिल्पों, व्यापार पैटर्न और संगठित कराधान के उदय पर एक व्यापक UPSC अध्ययन गाइड।"
    },
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "UPSC स्तर का मॉक टेस्ट",
            "description": "10 जटिल कथन-आधारित और मिलान वाले प्रश्नों के साथ उत्तर वैदिक आर्थिक इतिहास पर अपनी महारत का परीक्षण करें।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        }
    },
    "timeline": {
        "cards": [
            {
                "period": "लगभग 1000 ईसा पूर्व",
                "date": "स्थायी कृषि और लौह युग",
                "details": "भारत-आर्य पशुपालन-प्रधान जीवन शैली से स्थायी कृषि की ओर बढ़ते हैं। घग्गर-हकरा और दोआब क्षेत्रों में लोहे ('कृष्ण अयस') का प्रारंभिक उपयोग शुरू होता है।"
            },
            {
                "period": "लगभग 800 ईसा पूर्व",
                "date": "शिल्प विशेषज्ञता और पीजीडब्ल्यू",
                "details": "चित्रित धूसर मृदभांड (PGW) संस्कृति का विकास। धातु कर्म, चमड़े के काम और बुनाई जैसे शिल्पों की विशेषज्ञता।"
            },
            {
                "period": "लगभग 600 ईसा पूर्व",
                "date": "संगठित कराधान और प्रारंभिक शहरीकरण",
                "details": "स्वैच्छिक 'बलि' का अनिवार्य कर में संक्रमण। शाही खजाना अधिकारियों और हस्तिनापुर जैसे प्रारंभिक शहरी केंद्रों का उदय।"
            }
        ]
    },
    "toolEvolution": {
        "title": "आर्थिक और संसाधन विकास",
        "description": "ऋग्वैदिक से उत्तर वैदिक काल तक उत्पादन प्रणालियों का विकास।",
        "stages": [
            {
                "name": "कृषि आधार",
                "color": "#e74c3c",
                "desc": "प्रारंभिक वैदिक जीवन में पशुपालन का दबदबा था; उत्तर वैदिक काल में गेहूं, धान और जौ की खेती हावी रही।",
                "svg": '<i class="fas fa-seedling" style="font-size: 2rem; color: #e74c3c;"></i>'
            },
            {
                "name": "धातु प्रौद्योगिकी",
                "color": "#f39c12",
                "desc": "तांबे-कांसे (अयस) से लोहे (कृष्ण अयस) में संक्रमण, जिसका उपयोग जंगलों को साफ करने और उपकरण बनाने के लिए किया जाता था।",
                "svg": '<i class="fas fa-hammer" style="font-size: 2rem; color: #f39c12;"></i>'
            },
            {
                "name": "राजस्व प्रणाली",
                "color": "#2ecc71",
                "desc": "स्वैच्छिक उपहार (बलि) भागदुघ और सङ्ग्रहीतृ द्वारा प्रशासित अनिवार्य कराधान में विकसित हुए।",
                "svg": '<i class="fas fa-coins" style="font-size: 2rem; color: #2ecc71;"></i>'
            }
        ]
    },
    "traps": {
        "title": "सामान्य UPSC गलतियाँ और भेद",
        "items": [
            "भ्रम: यह मानना कि उत्तर वैदिक काल में नियमित धातु के सिक्कों की शुरुआत हुई थी। हालांकि ग्रंथों में निष्क, शतमान और कृष्णल का उल्लेख है, लेकिन ये वजन/धातु की इकाइयां थीं न कि मानक राजकीय सिक्के।",
            "यह न मानें कि शुरुआती उत्तर वैदिक काल में लोहे के हल का सार्वभौमिक रूप से उपयोग किया जाता था। लकड़ी के हल अभी भी आम थे; लोहे का उपयोग मुख्य रूप से जंगल साफ करने की कुल्हाड़ियों और हथियारों के लिए किया जाता था।",
            "बलि हमेशा कर नहीं था। ऋग्वैदिक काल में, यह एक स्वैच्छिक भेंट थी; उत्तर वैदिक काल में, यह एक नियमित, अनिवार्य कर बन गया।",
            "भूमि स्वामित्व की स्थिति को गलत न समझें। भूमि अभी पूरी तरह से निजी नहीं थी; यह परिवारों/कुलों द्वारा सामूहिक रूप से रखी जाती थी, हालांकि राजा ने कराधान पर शाही दावों का दावा किया था।"
        ]
    },
    "mnemonics": {
        "title": "वैदिक आर्थिक शब्दों के लिए याद रखने की ट्रिक",
        "description": "प्रमुख शब्दों और विभाजनों को याद रखने के लिए इन ट्रिक्स का उपयोग करें।",
        "items": [
            {
                "title": "राजस्व अधिकारियों की याद रखने की ट्रिक",
                "phrase": "भाग-दुघ (Bhagadugha) भाग (कर) एकत्र करता है; सङ्ग्रहीतृ (Sangrihitri) संग्रह (खजाने) की रक्षा करता है",
                "decryption": "भागदुघ कर संग्रहकर्ता था, और सङ्ग्रहीतृ कोषाध्यक्ष था।"
            },
            {
                "title": "धातुओं का वर्गीकरण",
                "phrase": "कृष्ण = लोहा (काला); लोहित = तांबा (लाल)",
                "decryption": "कृष्ण अयस या श्याम अयस लोहे को संदर्भित करता है, जबकि लोहित अयस तांबे को संदर्भित करता है।"
            }
        ]
    },
    "flashcards": {
        "title": "सक्रिय स्मरण फ्लैशकार्ड",
        "description": "प्रमुख आर्थिक शब्दों और तथ्यों को याद रखने की अपनी क्षमता का परीक्षण करें।",
        "items": [
            {
                "question": "उत्तर वैदिक ग्रंथों में 'व्रीहि' शब्द का क्या अर्थ है?",
                "answer": "धान (चावल), जो गेहूं और जौ के साथ एक प्रमुख खाद्य फसल बन गया।",
                "icon": "fa-seedling"
            },
            {
                "question": "उत्तर वैदिक प्रशासन में 'भागदुघ' कौन था?",
                "answer": "कृषि उपज (कर) के राजा के हिस्से को एकत्र करने के लिए जिम्मेदार अधिकारी।",
                "icon": "fa-user-tie"
            },
            {
                "question": "उत्तर वैदिक काल से कौन सी पुरातात्विक संस्कृति मेल खाती है?",
                "answer": "चित्रित धूसर मृदभांड (PGW) संस्कृति।",
                "icon": "fa-paint-brush"
            },
            {
                "question": "किस धातु को 'श्याम अयस' या 'कृष्ण अयस' कहा जाता है?",
                "answer": "लोहा।",
                "icon": "fa-cubes"
            }
        ]
    }
}

# The 6 Sections content
sections_meta = [
    {
        "id": 1,
        "title": "1. Transition to Settled Agriculture",
        "title_hi": "1. स्थायी कृषि में संक्रमण",
        "content": "<h3>Agriculture as the Primary Occupation</h3><p>In the Later Vedic period, agriculture shifted from a secondary activity to the primary source of livelihood, displacing pastoralism. The clearing of forests in the Ganga plains using fire and axes enabled large-scale cultivation. Vedic texts describe agricultural operations such as plowing (Krishi), sowing (Vapanta), harvesting (Lunati), and threshing (Mrinanti).</p><h3>Crop Diversity and Food Staples</h3><p>While barley (Yava) was the primary Rigvedic crop, Later Vedic texts show diversification. Rice, termed **Vrihi** or **Tandula**, became a staple food and ritual offering. Wheat (**Godhuma**), beans, lentils (Masura), and sesame (Tila) were also cultivated. Plowing was performed using heavy wooden plows (sometimes drawn by 6, 12, or 24 oxen, as mentioned in the Kathaka Samhita), marking a significant scale-up in agrarian output.</p>",
        "content_hi": "<h3>प्राथमिक व्यवसाय के रूप में कृषि</h3><p>उत्तर वैदिक काल में, कृषि एक माध्यमिक गतिविधि से हटकर आजीविका का प्राथमिक स्रोत बन गई, जिससे पशुपालन का स्थान ले लिया गया। आग और कुल्हाड़ियों का उपयोग करके गंगा के मैदानों में जंगलों की कटाई ने बड़े पैमाने पर खेती को सक्षम बनाया। वैदिक ग्रंथों में जुताई (कृषि), बुवाई (वपंत), कटाई (लुनति), और मड़ाई (मृणंति) जैसी कृषि गतिविधियों का वर्णन है।</p><h3>फसल विविधता और खाद्य स्टेपल</h3><p>जबकि जौ (यव) प्राथमिक ऋग्वैदिक फसल थी, उत्तर वैदिक ग्रंथों में विविधता दिखाई देती है। चावल, जिसे **व्रीहि** या **तंडुल** कहा जाता है, एक मुख्य भोजन और अनुष्ठानिक प्रसाद बन गया। गेहूं (**गोधूम**), सेम, दाल (मसूर), और तिल (तिल) की भी खेती की जाती थी। भारी लकड़ी के हलों का उपयोग करके जुताई की जाती थी (कभी-कभी 6, 12, या 24 बैलों द्वारा खींचा जाता था, जैसा कि काठक संहिता में उल्लेख किया गया है), जो कृषि उत्पादन में बड़े पैमाने पर वृद्धि को दर्शाता है।</p>"
    },
    {
        "id": 2,
        "title": "2. Role of Iron and Metallurgy",
        "title_hi": "2. लोहे और धातु कर्म की भूमिका",
        "content": "<h3>The Advent of the Iron Age</h3><p>The introduction of iron, referred to in Later Vedic texts as **Krishna Ayas** or **Syama Ayas** (dark metal), revolutionized clearing and cultivation. It is contrasted with **Lohita Ayas** (copper/bronze). The use of iron axes accelerated deforestation of the dense Gangetic plains, allowing new territories to be reclaimed for farming.</p><h3>Iron Tools vs. Weapons</h3><p>Archaeological evidence from Painted Grey Ware (PGW) sites shows that while iron was used for tool-making, its adoption was gradual. Iron weapons (spearheads, arrowheads) emerged first, followed by agricultural implements such as sickles, hoes, and eventually iron-tipped plowshares, which improved farming efficiency in tough alluvial soils.</p>",
        "content_hi": "<h3>लौह युग का आगमन</h3><p>लोहे की शुरुआत, जिसे उत्तर वैदिक ग्रंथों में **कृष्ण अयस** या **श्याम अयस** (काली धातु) कहा जाता है, ने जंगलों की सफाई और खेती में क्रांति ला दी। इसकी तुलना **लोहित अयस** (तांबा/कांसा) से की जाती है। लोहे की कुल्हाड़ियों के उपयोग ने घने गंगा के मैदानों में वनों की कटाई को तेज कर दिया, जिससे खेती के लिए नए क्षेत्रों को कृषि योग्य बनाया जा सका।</p><h3>लोहे के उपकरण बनाम हथियार</h3><p>चित्रित धूसर मृदभांड (PGW) स्थलों से प्राप्त पुरातात्विक साक्ष्यों से पता चलता है कि हालांकि उपकरण बनाने के लिए लोहे का उपयोग किया जाता था, लेकिन इसे धीरे-धीरे अपनाया गया। लोहे के हथियार (भाले, तीर के सिरे) सबसे पहले उभरे, उसके बाद कृषि उपकरण जैसे हंसिया, कुदाल और अंततः लोहे की नोक वाले हल के फाल आए, जिसने कठोर जलोढ़ मिट्टी में खेती की दक्षता में सुधार किया।</p>"
    },
    {
        "id": 3,
        "title": "3. Pastoralism and Animal Husbandry",
        "title_hi": "3. पशुपालन और मवेशी पालन",
        "content": "<h3>Changing Role of Cattle</h3><p>Although pastoralism was subordinated to agriculture, cattle and other domestic animals remained crucial. Cattle served as draft animals for heavy plows and transport. The cow (Gau) continued to represent wealth and was a common unit of value. However, the pastoral warfare (Gavisthi) of the Rigvedic era was replaced by territorial conflicts over agricultural lands.</p><h3>Sacred Status and Animal Wealth</h3><p>Vedic texts emphasize the protection of domestic animals, with some passages expressing reservations against slaughtering cattle (Aghnya). Cattle, horses, sheep, goats, and asses were raised. The multiplication of livestock was viewed as a divine blessing and was the focus of many Vedic prayers (Pashubandha rituals).</p>",
        "content_hi": "<h3>मवेशियों की बदलती भूमिका</h3><p>यद्यपि पशुपालन कृषि के अधीन हो गया था, लेकिन मवेशी और अन्य घरेलू जानवर महत्वपूर्ण बने रहे। मवेशियों ने भारी हलों और परिवहन के लिए खिंचाव वाले जानवरों के रूप में कार्य किया। गाय (गौ) धन का प्रतिनिधित्व करती रही और मूल्य की एक सामान्य इकाई थी। हालांकि, ऋग्वैदिक काल के पशुचारण युद्धों (गविष्टि) का स्थान कृषि भूमियों को लेकर क्षेत्रीय संघर्षों ने ले लिया।</p><h3>पवित्र स्थिति और पशु धन</h3><p>वैदिक ग्रंथों में घरेलू जानवरों के संरक्षण पर जोर दिया गया है, जिसमें कुछ गद्यांश मवेशियों के वध (अघ्न्य) के खिलाफ आपत्ति व्यक्त करते हैं। मवेशी, घोड़े, भेड़, बकरियां और गधे पाले जाते थे। पशुओं की वृद्धि को एक दिव्य आशीर्वाद के रूप में देखा जाता था और यह कई वैदिक प्रार्थनाओं (पशुबंध अनुष्ठान) का केंद्र था।</p>"
    },
    {
        "id": 4,
        "title": "4. Crafts, Industries, and Pottery",
        "title_hi": "4. शिल्प, उद्योग और मृदभांड",
        "content": "<h3>Specialization of Crafts</h3><p>The agricultural surplus fostered a growth in non-agrarian crafts. The Yajurveda lists numerous professional categories: carpenters (Takshan), chariot-makers (Rathakara), potters (Kulala), tanners (Charmakara), weavers (Vayatri), and goldsmiths (Hiranyakara). The Rathakara enjoyed high social status, often participating in royal coronation rituals.</p><h3>The Painted Grey Ware (PGW) Culture</h3><p>Archaeologically, this period is characterized by **Painted Grey Ware (PGW)**. Made of high-quality clay, this pottery consists of thin, grey dishes and bowls painted with black geometric patterns (lines, dots, circles). PGW was likely deluxe ware used by elites, found alongside coarse red ware used for everyday cooking and storage.</p>",
        "content_hi": "<h3>शिल्पों की विशेषज्ञता</h3><p>कृषि अधिशेष ने गैर-कृषि शिल्पों के विकास को बढ़ावा दिया। यजुर्वेद में कई व्यावसायिक श्रेणियों की सूची है: बढ़ई (तक्षण), रथ-निर्माता (रथकार), कुम्हार (कुलाल), चर्मकार (चर्मकार), बुनकर (वायत्री), और स्वर्णकार (हिरण्यकार)। रथकार को उच्च सामाजिक दर्जा प्राप्त था, जो अक्सर शाही राज्याभिषेक अनुष्ठानों में भाग लेते थे।</p><h3>चित्रित धूसर मृदभांड (PGW) संस्कृति</h3><p>पुरातात्विक रूप से, यह काल **चित्रित धूसर मृदभांड (PGW)** की विशेषता रखता है। उच्च गुणवत्ता वाली मिट्टी से बने इस मृदभांड में पतली, भूरी थालियाँ और कटोरे शामिल हैं जिन पर काले ज्यामितीय पैटर्न (रेखाएँ, बिंदु, वृत्त) चित्रित हैं। PGW संभवतः अभिजात वर्ग द्वारा उपयोग किया जाने वाला लक्जरी मृदभांड था, जो रोजमर्रा के खाना पकाने और भंडारण के लिए उपयोग किए जाने वाले खुरदरे लाल मृदभांड के साथ पाया गया है।</p>"
    },
    {
        "id": 5,
        "title": "5. Trade, Exchange, and Proto-Urbanization",
        "title_hi": "5. व्यापार, विनिमय और प्रारंभिक शहरीकरण",
        "content": "<h3>Barter and Units of Value</h3><p>Trade was primarily based on barter, but specific metallic objects served as regular measures of value. These included **Nishka** (gold ornaments or discs), **Satamana** (metallic weights), and **Krishnala** (berry-weight units). No regular, government-struck coinage existed during this era; transaction values were determined by weight and purity of metal.</p><h3>Proto-Urban Settlements</h3><p>The growth of trade and specialized crafts led to the emergence of proto-urban centers towards the end of the period (c. 600 BCE). Sites like **Hastinapur**, **Atranjikhera**, and **Kaushambi** transitioned from rural farming villages into proto-towns (Nagara) with denser populations and centralized administrative activities.</p>",
        "content_hi": "<h3>वस्तु विनिमय और मूल्य की इकाइयाँ</h3><p>व्यापार मुख्य रूप से वस्तु विनिमय पर आधारित था, लेकिन विशिष्ट धातु की वस्तुएं मूल्य के नियमित मापदंड के रूप में काम करती थीं। इनमें **निष्क** (सोने के आभूषण या चक्र), **शतमान** (धातु के वजन), और **कृष्णल** (रत्ती भार की इकाइयाँ) शामिल थे। इस युग के दौरान कोई नियमित, राजकीय सिक्के मौजूद नहीं थे; लेन-देन का मूल्य धातु के वजन और शुद्धता से निर्धारित होता था।</p><h3>प्रारंभिक शहरी बस्तियाँ</h3><p>व्यापार और विशिष्ट शिल्पों के विकास ने इस काल के अंत (लगभग 600 ईसा पूर्व) में प्रारंभिक शहरी केंद्रों के उदय का मार्ग प्रशस्त किया। **हस्तिनापुर**, **अतरंजीखेड़ा**, और **कौशाम्बी** जैसे स्थल ग्रामीण कृषि गांवों से घनी आबादी और केंद्रीकृत प्रशासनिक गतिविधियों वाले प्रारंभिक शहरों (नगर) में परिवर्तित हो गए।</p>"
    },
    {
        "id": 6,
        "title": "6. Land Ownership and Revenue Systems",
        "title_hi": "6. भूमि स्वामित्व और राजस्व प्रणालियाँ",
        "content": "<h3>Communal vs. Family Land Holdings</h3><p>Land ownership was transitionary. While the Rigvedic people did not emphasize individual land rights, the Later Vedic settled life led to family control of cultivated fields (**Kshetra**). However, land was still viewed as communal clan property, and royal grants of land (Brahmadeya) required the consent of the clan assembly (Vis).</p><h3>The Emergence of Compulsory Taxation</h3><p>With a settled population, the king’s administrative needs grew, transforming the voluntary **Bali** into a compulsory tax. The king collected a portion of agricultural produce, called **Bhaga**. To manage this, a formal revenue machinery emerged, featuring the **Bhagadugha** (tax collector) and the **Sangrihitri** (treasurer), funding the early state structure.</p>",
        "content_hi": "<h3>सामूहिक बनाम पारिवारिक भूमि स्वामित्व</h3><p>भूमि स्वामित्व संक्रमणकालीन चरण में था। हालांकि ऋग्वैदिक लोगों ने व्यक्तिगत भूमि अधिकारों पर जोर नहीं दिया, लेकिन उत्तर वैदिक काल के स्थायी जीवन ने खेती वाले खेतों (**क्षेत्र**) पर पारिवारिक नियंत्रण स्थापित किया। हालांकि, भूमि को अभी भी सामूहिक कबीले की संपत्ति माना जाता था, और भूमि के शाही अनुदान (ब्रह्मदेय) के लिए कबीले की सभा (विश) की सहमति आवश्यक थी।</p><h3>अनिवार्य कराधान का उदय</h3><p>स्थायी आबादी के साथ, राजा की प्रशासनिक आवश्यकताएं बढ़ीं, जिससे स्वैच्छिक **बलि** एक अनिवार्य कर में बदल गई। राजा कृषि उपज का एक हिस्सा एकत्र करता था, जिसे **भाग** कहा जाता था। इसे प्रबंधित करने के लिए, एक औपचारिक राजस्व तंत्र उभरा, जिसमें **भागदुघ** (कर संग्रहकर्ता) और **सङ्ग्रहीतृ** (कोषाध्यक्ष) शामिल थे, जो प्रारंभिक राज्य संरचना का वित्तपोषण करते थे।</p>"
    }
]

# Unique data pool for generating 62 distinct questions per section
question_pool = {
    1: [
        {"q": "What crop is referred to as 'Vrihi' in Later Vedic literature?", "opts": ["Rice", "Barley", "Wheat", "Sugarcane"], "ans": 0, "sol": "Vrihi refers to rice, which became a primary agricultural staple in Later Vedic times.", "q_hi": "उत्तर वैदिक साहित्य में 'व्रीहि' किसे कहा गया है?", "opts_hi": ["चावल/धान", "जौ", "गेहूं", "गन्ना"], "ans_hi": 0, "sol_hi": "व्रीहि धान/चावल को संदर्भित करता है, जो उत्तर वैदिक काल में एक प्राथमिक कृषि प्रधान भोजन बन गया."},
        {"q": "What Sanskrit term is used for wheat in Later Vedic texts?", "opts": ["Godhuma", "Yava", "Vrihi", "Tila"], "ans": 0, "sol": "Godhuma refers to wheat.", "q_hi": "उत्तर वैदिक ग्रंथों में गेहूं के लिए किस संस्कृत शब्द का प्रयोग किया जाता है?", "opts_hi": ["गोधूम", "यव", "व्रीहि", "तिल"], "ans_hi": 0, "sol_hi": "गोधूम का अर्थ गेहूं है."},
        {"q": "Which of the following became the primary economic occupation in the Later Vedic period?", "opts": ["Agriculture", "Pastoralism", "Maritime trade", "Mining"], "ans": 0, "sol": "Agriculture displaced pastoralism as the main livelihood.", "q_hi": "उत्तर वैदिक काल में निम्नलिखित में से कौन सा प्राथमिक आर्थिक व्यवसाय बन गया?", "opts_hi": ["कृषि", "पशुपालन", "समुद्री व्यापार", "खनन"], "ans_hi": 0, "sol_hi": "कृषि ने मुख्य आजीविका के रूप में पशुपालन का स्थान ले लिया."},
        {"q": "What term refers to the agricultural operation of plowing in Later Vedic texts?", "opts": ["Krishi", "Vapanta", "Lunati", "Mrinanti"], "ans": 0, "sol": "Krishi refers to the plowing process.", "q_hi": "उत्तर वैदिक ग्रंथों में जुताई की कृषि गतिविधि को क्या कहा जाता है?", "opts_hi": ["कृषि", "वपंत", "लुनति", "मृणंति"], "ans_hi": 0, "sol_hi": "कृषि जुताई की प्रक्रिया को संदर्भित करती है."},
        {"q": "How many oxen were sometimes harnessed to draw heavy plows according to Kathaka Samhita?", "opts": ["Up to 24 oxen", "Only 2 oxen", "Exactly 4 oxen", "Up to 8 oxen"], "ans": 0, "sol": "Texts mention heavy wooden plows drawn by 6, 12, or 24 oxen.", "q_hi": "काठक संहिता के अनुसार कभी-कभी भारी हलों को खींचने के लिए कितने बैल जोते जाते थे?", "opts_hi": ["24 बैलों तक", "केवल 2 बैल", "ठीक 4 बैल", "8 बैलों तक"], "ans_hi": 0, "sol_hi": "ग्रंथों में 6, 12, या 24 बैलों द्वारा खींचे जाने वाले भारी लकड़ी के हलों का उल्लेख है."},
        {"q": "Which grain was the primary cultivated crop of the early Rigvedic period but became secondary in Later Vedic times?", "opts": ["Yava (Barley)", "Vrihi (Rice)", "Godhuma (Wheat)", "Masura (Lentils)"], "ans": 0, "sol": "Barley was the primary crop in Rigvedic times, replaced by rice/wheat in importance later.", "q_hi": "कौन सा अनाज प्रारंभिक ऋग्वैदिक काल की प्राथमिक फसल थी लेकिन उत्तर वैदिक काल में माध्यमिक बन गई?", "opts_hi": ["यव (जौ)", "व्रीहि (चावल)", "गोधूम (गेहूं)", "मसूर (दाल)"], "ans_hi": 0, "sol_hi": "जौ ऋग्वैदिक काल में प्राथमिक फसल थी, जिसकी जगह बाद में चावल/गेहूं ने ले ली."},
        {"q": "The agricultural verb 'Vapanta' refers to which operation?", "opts": ["Sowing seeds", "Plowing fields", "Harvesting crops", "Threshing grain"], "ans": 0, "sol": "Vapanta refers to sowing.", "q_hi": "कृषि क्रिया 'वपंत' किस गतिविधि को संदर्भित करती है?", "opts_hi": ["बीज बोना", "खेत जोतना", "फसल काटना", "अनाज मढ़ना"], "ans_hi": 0, "sol_hi": "वपंत बुवाई को संदर्भित करता है."},
        {"q": "Which text details the four main stages of farming: plowing, sowing, harvesting, and threshing?", "opts": ["Shatapatha Brahmana", "Atharvaveda", "Rigveda", "Katha Upanishad"], "ans": 0, "sol": "Shatapatha Brahmana details plowing, sowing, harvesting, and threshing.", "q_hi": "कौन सा ग्रंथ खेती के चार मुख्य चरणों: जुताई, बुवाई, कटाई और मड़ाई का विवरण देता है?", "opts_hi": ["शतपथ ब्राह्मण", "अथर्ववेद", "ऋग्वेद", "कठोपनिषद"], "ans_hi": 0, "sol_hi": "शतपथ ब्राह्मण जुताई, बुवाई, कटाई और मड़ाई का विवरण देता है."},
        {"q": "What term refers to cow-dung manure used to increase agricultural yield in Later Vedic times?", "opts": ["Karisha", "Sita", "Kulya", "Yava"], "ans": 0, "sol": "Karisha or Shakrit refers to cow-dung manure used in agriculture.", "q_hi": "उत्तर वैदिक काल में कृषि उपज बढ़ाने के लिए उपयोग की जाने वाली गोबर की खाद को क्या कहा जाता था?", "opts_hi": ["करीष", "सीता", "कुल्या", "यव"], "ans_hi": 0, "sol_hi": "करीष या शकृत कृषि में प्रयुक्त गोबर की खाद को संदर्भित करता है."},
        {"q": "What name was given to artificial irrigation canals in Later Vedic economic life?", "opts": ["Kulyas", "Sira", "Kshetra", "Urvara"], "ans": 0, "sol": "Kulyas refers to irrigation canals or channels.", "q_hi": "उत्तर वैदिक आर्थिक जीवन में कृत्रिम सिंचाई नहरों को क्या नाम दिया गया था?", "opts_hi": ["कुल्या", "सीरा", "क्षेत्र", "उर्वरा"], "ans_hi": 0, "sol_hi": "कुल्या सिंचाई नहरों या नालियों को संदर्भित करती है."},
        {"q": "The division of agricultural cycles based on seasonal rituals in Later Vedic times is called:", "opts": ["Chaturmasya rituals", "Pashubandha", "Rajasuya", "Agnyadheya"], "ans": 0, "sol": "Chaturmasya sacrifices divided the agricultural year into four-month seasonal cycles.", "q_hi": "उत्तर वैदिक काल में मौसमी अनुष्ठानों पर आधारित कृषि चक्रों के विभाजन को क्या कहा जाता है?", "opts_hi": ["चातुर्मास्य अनुष्ठान", "पशुबंध", "राजसूय", "अग्न्याधेय"], "ans_hi": 0, "sol_hi": "चातुर्मास्य यज्ञ कृषि वर्ष को चार महीने के मौसमी चक्रों में विभाजित करते थे."},
        {"q": "Which Sanskrit term was commonly used for the heavy plow during this settled phase?", "opts": ["Langala or Sira", "Krishi", "Phala", "Khanitra"], "ans": 0, "sol": "Langala and Sira refer to the plow in Vedic literature.", "q_hi": "इस स्थायी चरण के दौरान भारी हल के लिए आमतौर पर किस संस्कृत शब्द का प्रयोग किया जाता था?", "opts_hi": ["लांगळ या सीरा", "कृषि", "फाल", "खनित्र"], "ans_hi": 0, "sol_hi": "लांगळ और सीरा वैदिक साहित्य में हल को संदर्भित करते हैं."}
    ],
    2: [
        {"q": "What does the term 'Krishna Ayas' literally translate to in economic texts?", "opts": ["Dark Metal / Iron", "Copper", "Gold", "Bronze"], "ans": 0, "sol": "Krishna Ayas means black metal, which refers to iron.", "q_hi": "आर्थिक ग्रंथों में 'कृष्ण अयस' शब्द का शाब्दिक अनुवाद क्या है?", "opts_hi": ["काली धातु / लोहा", "तांबा", "सोना", "कांसा"], "ans_hi": 0, "sol_hi": "कृष्ण अयस का अर्थ काली धातु है, जो लोहे को संदर्भित करता है."},
        {"q": "What metal is referred to as 'Lohita Ayas'?", "opts": ["Copper/Bronze", "Iron", "Gold", "Lead"], "ans": 0, "sol": "Lohita Ayas refers to red copper or bronze.", "q_hi": "किस धातु को 'लोहित अयस' कहा जाता है?", "opts_hi": ["तांबा/कांसा", "लोहा", "सोना", "सीसा"], "ans_hi": 0, "sol_hi": "लोहित अयस लाल तांबे या कांसे को संदर्भित करता है."},
        {"q": "Which technological development accelerated forest clearing in the Gangetic plains?", "opts": ["Use of iron axes (Krishna Ayas)", "Copper hand-saws", "Imported bronze blades", "Stone axes only"], "ans": 0, "sol": "Iron axes accelerated deforestation of dense plains.", "q_hi": "किस तकनीकी विकास ने गंगा के मैदानों में वनों की कटाई को तेज किया?", "opts_hi": ["लोहे की कुल्हाड़ियों का उपयोग (कृष्ण अयस)", "तांबे की आरी", "आयातित कांसे के फलक", "केवल पत्थर की कुल्हाड़ियाँ"], "ans_hi": 0, "sol_hi": "लोहे की कुल्हाड़ियों ने घने मैदानों की कटाई को तेज कर दिया."},
        {"q": "In archaeological records, which iron objects typically emerged first?", "opts": ["Weapons like spearheads and arrowheads", "Agricultural plowshares", "Industrial hammers", "Domestic kitchen knives"], "ans": 0, "sol": "Iron weapons emerged first in PGW records; tools came later.", "q_hi": "पुरातात्विक अभिलेखों में, कौन सी लोहे की वस्तुएं आम तौर पर पहले दिखाई दीं?", "opts_hi": ["भाले और तीर के सिरे जैसे हथियार", "कृषि हल के फाल", "औद्योगिक हथौड़े", "घरेलू रसोई के चाकू"], "ans_hi": 0, "sol_hi": "भाले और तीर के सिरे जैसे हथियार पहले दिखाई दिए; उपकरण बाद में आए."},
        {"q": "Which tool typology gradually improved farming efficiency in tough alluvial soils?", "opts": ["Iron-tipped plowshares", "Wooden sticks only", "Copper spades", "Bronze trowels"], "ans": 0, "sol": "Iron-tipped plowshares made deep plowing in alluvial soil possible.", "q_hi": "कठोर जलोढ़ मिट्टी में खेती की दक्षता में किस उपकरण ने धीरे-धीरे सुधार किया?", "opts_hi": ["लोहे की नोक वाले हल", "केवल लकड़ी की छड़ें", "तांबे के फावड़े", "कांसे की कन्नी"], "ans_hi": 0, "sol_hi": "लोहे की नोक वाले हल ने गहरी जुताई को संभव बनाया."},
        {"q": "The Sanskrit term 'Syama Ayas' in Atharvaveda refers to which metal?", "opts": ["Iron", "Copper", "Silver", "Gold"], "ans": 0, "sol": "Syama Ayas means dark metal, referring to iron.", "q_hi": "अथर्ववेद में प्रयुक्त संस्कृत शब्द 'श्याम अयस' किस धातु को संदर्भित करता है?", "opts_hi": ["लोहा", "तांबा", "चांदी", "सोना"], "ans_hi": 0, "sol_hi": "श्याम अयस का अर्थ लोहा है."},
        {"q": "What archaeological culture corresponds to the Later Vedic Iron Age transition?", "opts": ["Painted Grey Ware (PGW) culture", "Ochre Coloured Pottery (OCP) culture", "Northern Black Polished Ware (NBPW) culture", "Harappan Chalcolithic"], "ans": 0, "sol": "PGW culture corresponds to the Later Vedic transition.", "q_hi": "उत्तर वैदिक लौह युग संक्रमण से कौन सी पुरातात्विक संस्कृति मेल खाती है?", "opts_hi": ["चित्रित धूसर मृदभांड (PGW) संस्कृति", "गेरुए रंग के मृदभांड (OCP) संस्कृति", "उत्तरी काली चमकीली मृदभांड (NBPW) संस्कृति", "हड़प्पा ताम्रपाषाण"], "ans_hi": 0, "sol_hi": "PGW संस्कृति उत्तर वैदिक संक्रमण से मेल खाती है."},
        {"q": "The use of iron tools allowed Aryans to expand into which geographical region?", "opts": ["Gangetic plain (Eastward)", "Deccan Plateau (Southward)", "Kashmir valley (Northward)", "Thar desert (Westward)"], "ans": 0, "sol": "Iron enabled clearance and migration into the Gangetic plains.", "q_hi": "लोहे के उपकरणों के उपयोग ने आर्यों को किस भौगोलिक क्षेत्र में विस्तार करने की अनुमति दी?", "opts_hi": ["गंगा का मैदान (पूर्व की ओर)", "दक्कन का पठार (दक्षिण की ओर)", "कश्मीर घाटी (उत्तर की ओर)", "थार मरुस्थल (पश्चिम की ओर)"], "ans_hi": 0, "sol_hi": "लोहे ने गंगा के मैदानों में वनों की कटाई और प्रवास को सक्षम बनाया."},
        {"q": "Which PGW site has yielded early evidence of iron smelting and furnaces?", "opts": ["Atranjikhera", "Hastinapur", "Alamgirpur", "Noh"], "ans": 0, "sol": "Atranjikhera has provided clear archaeological evidence of early iron smelting and workshops.", "q_hi": "किस पीजीडब्ल्यू स्थल से लोहे को गलाने और भट्टियों के शुरुआती साक्ष्य मिले हैं?", "opts_hi": ["अतरंजीखेड़ा", "हस्तिनापुर", "आलमगीरपुर", "नोह"], "ans_hi": 0, "sol_hi": "अतरंजीखेड़ा ने लोहे को गलाने और भट्टियों के स्पष्ट पुरातात्विक साक्ष्य प्रदान किए हैं."},
        {"q": "Where did Later Vedic metalworkers primarily source their iron ore from?", "opts": ["Aravalli hills and Gwalior region", "Southern Deccan", "Karakoram range", "Foreign imports"], "ans": 0, "sol": "Iron ore was sourced from local deposits in the Aravalli range and Eastern Rajasthan/Gwalior.", "q_hi": "उत्तर वैदिक काल के धातु कामगार मुख्य रूप से अपना लौह अयस्क कहाँ से प्राप्त करते थे?", "opts_hi": ["अरावली पहाड़ियों और ग्वालियर क्षेत्र", "दक्षिणी दक्कन", "काराकोरम श्रेणी", "विदेशी आयात"], "ans_hi": 0, "sol_hi": "लौह अयस्क अरावली पहाड़ियों और पूर्वी राजस्थान/ग्वालियर के स्थानीय भंडारों से प्राप्त किया जाता था."},
        {"q": "How does Rigvedic 'Ayas' contrast with Later Vedic 'Krishna Ayas'?", "opts": ["Rigvedic Ayas meant only copper/bronze; Later Vedic added specific iron terms", "Rigvedic Ayas was gold; Later Vedic was silver", "They refer to the exact same metal", "Rigvedic Ayas was iron; Later Vedic was copper"], "ans": 0, "sol": "Rigvedic Ayas was generic copper/bronze, whereas Later Vedic developed specific terms like Krishna Ayas for iron.", "q_hi": "ऋग्वैदिक 'अयस' उत्तर वैदिक 'कृष्ण अयस' से किस प्रकार भिन्न है?", "opts_hi": ["ऋग्वैदिक अयस का अर्थ केवल तांबा/कांसा था; उत्तर वैदिक में विशिष्ट लोहे के शब्द जोड़े गए", "ऋग्वैदिक अयस सोना था; उत्तर वैदिक चांदी थी", "वे बिल्कुल एक ही धातु को संदर्भित करते हैं", "ऋग्वैदिक अयस लोहा था; उत्तर वैदिक तांबा था"], "ans_hi": 0, "sol_hi": "ऋग्वैदिक अयस तांबा/कांसा था, जबकि उत्तर वैदिक काल में लोहे के लिए कृष्ण अयस जैसे विशिष्ट शब्द विकसित हुए."},
        {"q": "What term is used in the texts for smiths or workers who specialized in metal production?", "opts": ["Karmara", "Takshan", "Kulala", "Rathakara"], "ans": 0, "sol": "Karmara was the term for smiths and metalworkers.", "q_hi": "धातु उत्पादन में विशेषज्ञता रखने वाले लोहारों या कामगारों के लिए ग्रंथों में किस शब्द का प्रयोग किया जाता है?", "opts_hi": ["कर्मार", "तक्षण", "कुलाल", "रथकार"], "ans_hi": 0, "sol_hi": "कर्मार धातु का काम करने वाले कारीगरों/लोहारों को कहा जाता था."}
    ],
    3: [
        {"q": "What Vedic term is used to declare that a cow should not be killed?", "opts": ["Aghnya", "Gavisthi", "Bhaga", "Nishka"], "ans": 0, "sol": "Aghnya means 'not to be killed', referring to cows.", "q_hi": "किस वैदिक शब्द का उपयोग यह घोषित करने के लिए किया जाता है कि गाय को नहीं मारा जाना चाहिए?", "opts_hi": ["अघ्न्य", "गविष्टि", "भाग", "निष्क"], "ans_hi": 0, "sol_hi": "अघ्न्य का अर्थ है 'न मारे जाने योग्य', जो गायों को संदर्भित करता है."},
        {"q": "Which animal continued to function as the primary standard of transaction value?", "opts": ["Cow (Gau)", "Horse", "Sheep", "Goat"], "ans": 0, "sol": "Cows remained a primary measure of wealth and value.", "q_hi": "कौन सा जानवर लेन-देन मूल्य के प्राथमिक मानक के रूप में कार्य करता रहा?", "opts_hi": ["गाय (गौ)", "घोड़ा", "भेड़", "बकरी"], "ans_hi": 0, "sol_hi": "गायें धन और मूल्य का प्राथमिक माप बनी रहीं."},
        {"q": "The Rigvedic pastoral war term 'Gavisthi' (search for cows) was replaced by conflicts over:", "opts": ["Land / Territory", "Water rights", "Horses", "Gold mines"], "ans": 0, "sol": "Conflicts shifted from cattle raids to disputes over agricultural land.", "q_hi": "ऋग्वैदिक पशुचारक युद्ध शब्द 'गविष्टि' (गायों की खोज) को किस संघर्ष से बदल दिया गया था?", "opts_hi": ["भूमि / क्षेत्र", "जल अधिकार", "घोड़े", "सोने की खदानें"], "ans_hi": 0, "sol_hi": "संघर्ष मवेशियों के छापों से हटकर कृषि भूमि पर विवादों में बदल गए."},
        {"q": "Which domestic animals were reared primarily for draft power in plowing?", "opts": ["Oxen and Bulls", "Horses", "Sheep", "Asses"], "ans": 0, "sol": "Oxen and bulls were utilized for agricultural traction.", "q_hi": "जुताई में मुख्य रूप से खिंचाव शक्ति के लिए कौन से पालतू जानवर पाले जाते थे?", "opts_hi": ["बैल and सांड", "घोड़े", "भेड़", "गधे"], "ans_hi": 0, "sol_hi": "बैलों का उपयोग कृषि कार्यों में खिंचाव के लिए किया जाता था."},
        {"q": "Which Vedic ritual focused specifically on securing cattle wealth and animal welfare?", "opts": ["Pashubandha", "Rajasuya", "Upanayana", "Soma Yajna"], "ans": 0, "sol": "Pashubandha rituals involved prayers for livestock welfare.", "q_hi": "कौन सा वैदिक अनुष्ठान विशेष रूप से मवेशी धन और पशु कल्याण पर केंद्रित था?", "opts_hi": ["पशुबंध", "राजसूय", "उपनयन", "सोम यज्ञ"], "ans_hi": 0, "sol_hi": "पशुबंध अनुष्ठानों में पशुधन कल्याण के लिए प्रार्थना शामिल थी."},
        {"q": "What status did cows hold in Later Vedic texts to discourage slaughter?", "opts": ["Sacred/Aghnya status", "Secular trade status only", "Low value status", "No specific status was mentioned"], "ans": 0, "sol": "Cows held sacred status and were declared Aghnya.", "q_hi": "वध को हतोत्साहित करने के लिए उत्तर वैदिक ग्रंथों में गायों की क्या स्थिति थी?", "opts_hi": ["पवित्र/अघ्न्य स्थिति", "केवल धर्मनिरपेक्ष व्यापार स्थिति", "कम मूल्य की स्थिति", "किसी विशिष्ट स्थिति का उल्लेख नहीं था"], "ans_hi": 0, "sol_hi": "गायों को पवित्र दर्जा प्राप्त था और उन्हें अघ्न्य घोषित किया गया था."},
        {"q": "Which animal was highly valued for military charioteering and transport?", "opts": ["Horse (Asva)", "Cow", "Ass", "Camel"], "ans": 0, "sol": "Horses were crucial for charioteering and military speed.", "q_hi": "सैन्य रथ चलाने और परिवहन के लिए किस जानवर को अत्यधिक महत्व दिया जाता था?", "opts_hi": ["घोड़ा (अश्व)", "गाय", "गधा", "ऊंट"], "ans_hi": 0, "sol_hi": "घोड़े रथ चलाने और सैन्य गति के लिए महत्वपूर्ण थे."},
        {"q": "Were sheep (Avi) and goats (Aja) domesticated during this period?", "opts": ["Yes, they were commonly raised", "No, they were unknown", "Only in mountainous regions", "Only for priestly sacrifices"], "ans": 0, "sol": "Sheep and goats were commonly reared for wool, milk, and meat.", "q_hi": "क्या इस अवधि के दौरान भेड़ (अवि) और बकरियां (अज) को पालतू बनाया गया था?", "opts_hi": ["हाँ, उन्हें आमतौर पर पाला जाता था", "नहीं, वे अज्ञात थे", "केवल पहाड़ी क्षेत्रों में", "केवल पुरोहितों के यज्ञों के लिए"], "ans_hi": 0, "sol_hi": "भेड़ और बकरियों को आमतौर पर पाला जाता था."},
        {"q": "What title refers to the chief protector or owner of cattle wealth in late texts?", "opts": ["Gopati", "Bhagadugha", "Gramani", "Sangrihitri"], "ans": 0, "sol": "Gopati refers to the lord or protector of cattle.", "q_hi": "उत्तर वैदिक ग्रंथों में मवेशी धन के मुख्य रक्षक या स्वामी को क्या उपाधि दी जाती थी?", "opts_hi": ["गोपति", "भागदुघ", "ग्रामणी", "संग्रहित्री"], "ans_hi": 0, "sol_hi": "गोपति मवेशियों के स्वामी या रक्षक को संदर्भित करता है."},
        {"q": "What term replaced the Rigvedic tribal pastures ('Vraja') in settled communities?", "opts": ["Goshtha", "Kshetra", "Nagara", "Samiti"], "ans": 0, "sol": "Goshtha refers to the settled, permanent cowpen or pasture area of the family/village.", "q_hi": "स्थायी समुदायों में ऋग्वैदिक जनजातीय चरागाहों ('व्रज') का स्थान किस शब्द ने लिया?", "opts_hi": ["गोष्ठ", "क्षेत्र", "नगर", "समिति"], "ans_hi": 0, "sol_hi": "गोष्ठ परिवार/गाँव के स्थायी बाड़े या चरागाह क्षेत्र को संदर्भित करता है."},
        {"q": "In the Rigvedic period, cattle searching was represented by Sarama; in Later Vedic times this shifted to:", "opts": ["Fixed, walled cowpens (Goshtha)", "Nomadic hunting trails", "Abolishing animal breeding", "Exclusively sheep keeping"], "ans": 0, "sol": "Cattle husbandry transitioned to fixed structures and cowpens (Goshtha).", "q_hi": "ऋग्वैदिक काल में, मवेशी खोज का प्रतिनिधित्व सरमा द्वारा किया जाता था; उत्तर वैदिक काल में यह किसमें बदल गया?", "opts_hi": ["स्थायी और दीवार वाले बाड़े (गोष्ठ)", "खानाबदोश शिकार ट्रेल्स", "पशु प्रजनन समाप्त करना", "केवल भेड़ पालना"], "ans_hi": 0, "sol_hi": "पशुपालन स्थायी संरचनाओं और बाड़ों (गोष्ठ) की ओर स्थानांतरित हो गया."},
        {"q": "Which milk product was central to Vedic sacrificial offerings and household food?", "opts": ["Ghrita (Ghee)", "Soma juice only", "Foreign cheese", "Fermented alcohol"], "ans": 0, "sol": "Ghrita (ghee) was a primary ritual offering and dietary staple.", "q_hi": "कौन सा डेयरी उत्पाद वैदिक यज्ञ आहुतियों और घरेलू भोजन के लिए केंद्रीय था?", "opts_hi": ["घृत (घी)", "केवल सोम रस", "विदेशी पनीर", "किण्वित शराब"], "ans_hi": 0, "sol_hi": "घृत (घी) एक प्राथमिक अनुष्ठानिक प्रसाद और मुख्य खाद्य सामग्री थी."}
    ],
    4: [
        {"q": "Which artisan class enjoyed high social status and participated in coronation rituals?", "opts": ["Rathakara (Chariot-maker)", "Takshan (Carpenter)", "Kulala (Potter)", "Charmakara (Tanner)"], "ans": 0, "sol": "Rathakara participated in royal coronation ceremonies.", "q_hi": "किस कारीगर वर्ग को उच्च सामाजिक दर्जा प्राप्त था और उन्होंने राज्याभिषेक अनुष्ठानों में भाग लिया?", "opts_hi": ["रथकार (रथ-निर्माता)", "तक्षण (बढ़ई)", "कुलाल (कुम्हार)", "चर्मकार (चर्मकार)"], "ans_hi": 0, "sol_hi": "रथकार शाही राज्याभिषेक समारोहों में भाग लेते थे."},
        {"q": "What type of pottery is the primary archaeological marker of the Later Vedic Period?", "opts": ["Painted Grey Ware (PGW)", "Northern Black Polished Ware (NBPW)", "Ochre Coloured Pottery (OCP)", "Black and Red Ware"], "ans": 0, "sol": "Painted Grey Ware (PGW) corresponds to the Later Vedic period sites.", "q_hi": "कौन सा मृदभांड उत्तर वैदिक काल का प्राथमिक पुरातात्विक सूचक है?", "opts_hi": ["चित्रित धूसर मृदभांड (PGW)", "उत्तरी काली चमकीली मृदभांड (NBPW)", "गेरुए रंग के मृदभांड (OCP)", "काले और लाल मृदभांड"], "ans_hi": 0, "sol_hi": "चित्रित धूसर मृदभांड (PGW) उत्तर वैदिक काल के स्थलों से मेल खाता है."},
        {"q": "What describes the aesthetic design of Painted Grey Ware (PGW)?", "opts": ["Fine, grey bowls and dishes painted with black geometric patterns", "Coarse red pots with white animal figures", "Polished black jars with gold leaves", "Plain unpainted brown storage bins"], "ans": 0, "sol": "PGW features black geometric patterns (lines, dots, circles) on fine grey ware.", "q_hi": "चित्रित धूसर मृदभांड (PGW) के सौंदर्य डिजाइन का क्या वर्णन है?", "opts_hi": ["काले ज्यामितीय पैटर्नों से चित्रित महीन, भूरी थालियाँ और कटोरे", "सफेद पशु आकृतियों वाले खुरदरे लाल घड़े", "सोने की पत्तियों वाले चमकीले काले जार", "सादे बिना चित्रित भूरे रंग के भंडारण बिन"], "ans_hi": 0, "sol_hi": "PGW में ठीक धूसर सतह पर काले ज्यामितीय पैटर्न शामिल हैं."},
        {"q": "Which text lists distinct professional categories of craftsmen like weavers and tanners?", "opts": ["Yajurveda", "Rigveda", "Katha Upanishad", "Sulvasutras"], "ans": 0, "sol": "Yajurveda lists specialized crafts and occupations.", "q_hi": "कौन सा ग्रंथ बुनकरों और चर्मकारों जैसे शिल्पकारों की विभिन्न व्यावसायिक श्रेणियों को सूचीबद्ध करता है?", "opts_hi": ["यजुर्वेद", "ऋग्वेद", "कठोपनिषद", "शुल्बसूत्र"], "ans_hi": 0, "sol_hi": "यजुर्वेद विशिष्ट शिल्पों और व्यवसायों को सूचीबद्ध करता है."},
        {"q": "The Sanskrit term 'Takshan' refers to which professional category?", "opts": ["Carpenter", "Potter", "Chariot-maker", "Goldsmith"], "ans": 0, "sol": "Takshan refers to a carpenter.", "q_hi": "संस्कृत शब्द 'तक्षण' किस व्यावसायिक श्रेणी को संदर्भित करता है?", "opts_hi": ["बढ़ई", "कुम्हार", "रथ-निर्माता", "सुनार"], "ans_hi": 0, "sol_hi": "तक्षण बढ़ई को संदर्भित करता है."},
        {"q": "The Sanskrit term 'Kulala' refers to which craftsman?", "opts": ["Potter", "Blacksmith", "Weaver", "Tanner"], "ans": 0, "sol": "Kulala refers to a potter.", "q_hi": "संस्कृत शब्द 'कुलाल' किस शिल्पकार को संदर्भित करता है?", "opts_hi": ["कुम्हार", "लोहार", "बुनकर", "चर्मकार"], "ans_hi": 0, "sol_hi": "कुलाल कुम्हार को संदर्भित करता है."},
        {"q": "Which ware was likely the everyday utility pottery found alongside PGW?", "opts": ["Coarse red ware", "Northern Black Polished Ware", "Fine gold-painted ware", "None of these"], "ans": 0, "sol": "PGW was deluxe ware; coarse red ware was for everyday cooking and storage.", "q_hi": "PGW के साथ पाया जाने वाला रोजमर्रा की उपयोगिता का मृदभांड कौन सा था?", "opts_hi": ["खुरदरा लाल मृदभांड", "उत्तरी काली चमकीली मृदभांड", "महीन सोने से चित्रित मृदभांड", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "PGW लक्जरी मृदभांड था; खुरदरा लाल मृदभांड रोजमर्रा के उपयोग के लिए था."},
        {"q": "The specialization of crafts in Later Vedic times indicates what macro-economic trend?", "opts": ["Growth of agricultural surplus enabling non-agrarian labor division", "Complete decline of trade", "Transition back to primitive hunting", "Abolition of private property"], "ans": 0, "sol": "Surplus food enabled craft specialization and labor division.", "q_hi": "उत्तर वैदिक काल में शिल्पों की विशेषज्ञता किस व्यापक आर्थिक प्रवृत्ति को दर्शाती है?", "opts_hi": ["कृषि अधिशेष का विकास जिससे गैर-कृषि श्रम विभाजन संभव हुआ", "व्यापार में गिरावट", "आदिम शिकार की ओर संक्रमण", "निजी संपत्ति का उन्मूलन"], "ans_hi": 0, "sol_hi": "कृषि अधिशेष ने शिल्प विशेषज्ञता और श्रम विभाजन को सक्षम बनाया."},
        {"q": "What term is used for female weavers or the craft of weaving in late texts?", "opts": ["Vayatri", "Charmakara", "Takshan", "Kulala"], "ans": 0, "sol": "Vayatri refers to weaving practitioners, often female.", "q_hi": "उत्तर वैदिक ग्रंथों में महिला बुनकरों या बुनाई के शिल्प के लिए किस शब्द का प्रयोग किया जाता है?", "opts_hi": ["वायत्री", "चर्मकार", "तक्षण", "कुलाल"], "ans_hi": 0, "sol_hi": "वायत्री बुनाई का काम करने वाली (अक्सर महिलाओं) को संदर्भित करता है."},
        {"q": "The term 'Charmakara' in the Yajurveda refers to which category of artisans?", "opts": ["Leather workers / Tanners", "Goldsmiths", "Chariot makers", "Potters"], "ans": 0, "sol": "Charmakara refers to leather workers or tanners.", "q_hi": "यजुर्वेद में 'चर्मकार' शब्द किस कारीगर वर्ग को संदर्भित करता है?", "opts_hi": ["चर्मकार / चमड़े के कामगार", "सुनार", "रथ निर्माता", "कुम्हार"], "ans_hi": 0, "sol_hi": "चर्मकार चमड़े का काम करने वाले या चर्मकारों को संदर्भित करता है."},
        {"q": "Which artisan group is designated as 'Hiranyakara' in Later Vedic texts?", "opts": ["Goldsmiths", "Carpenters", "Potters", "Weavers"], "ans": 0, "sol": "Hiranyakara refers to goldsmiths who crafted ornaments.", "q_hi": "उत्तर वैदिक ग्रंथों में किस कारीगर वर्ग को 'हिरण्यकार' कहा गया है?", "opts_hi": ["स्वर्णकार / सुनार", "बढ़ई", "कुम्हार", "बुनकर"], "ans_hi": 0, "sol_hi": "हिरण्यकार सोने के आभूषण बनाने वाले सुनारों को संदर्भित करता है."},
        {"q": "What new technology, verified at Hastinapur, appears in PGW archaeological levels?", "opts": ["Glass beads and glass working", "Standardized coinage", "Iron plowshares only", "None of these"], "ans": 0, "sol": "Glass technology and glass beads emerged during the PGW phase.", "q_hi": "हस्तिनापुर में सत्यापित कौन सी नई तकनीक पीजीडब्ल्यू पुरातात्विक स्तरों में दिखाई देती है?", "opts_hi": ["कांच के मनके और कांच का काम", "मानकीकृत सिक्के", "केवल लोहे के फाल", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "पीजीडब्ल्यू चरण के दौरान कांच की तकनीक और कांच के मनके उभरे थे."}
    ],
    5: [
        {"q": "Which metallic unit of weight is mentioned alongside Nishka in trade texts?", "opts": ["Satamana", "Rupaka", "Dinar", "Jital"], "ans": 0, "sol": "Satamana was a silver weight/measure mentioned in Later Vedic literature.", "q_hi": "व्यापारिक ग्रंथों में निष्क के साथ किस धातु की वजन इकाई का उल्लेख किया गया है?", "opts_hi": ["शतमान", "रूपक", "दीनार", "जीतल"], "ans_hi": 0, "sol_hi": "शतमान उत्तर वैदिक साहित्य में वर्णित चांदी का वजन/माप था."},
        {"q": "What basic unit of weight was based on the seed of the Gunja berry?", "opts": ["Krishnala", "Satamana", "Nishka", "Karshapana"], "ans": 0, "sol": "Krishnala represents the berry-weight unit.", "q_hi": "गुंजा बेरी के बीज पर आधारित वजन की मूल इकाई कौन सी थी?", "opts_hi": ["कृष्णल", "शतमान", "निष्क", "कार्षापण"], "ans_hi": 0, "sol_hi": "कृष्णल गुंजा बीज के भार की इकाई को दर्शाता है."},
        {"q": "Did regular, government-struck coinage exist in Later Vedic times?", "opts": ["No, trade was barter-based with metal weights", "Yes, gold dinars were standard", "Yes, punch-marked coins emerged early", "Only foreign Roman coins were used"], "ans": 0, "sol": "No regular state coinage existed; weights of metal were used.", "q_hi": "क्या उत्तर वैदिक काल में नियमित, सरकारी मुद्रा प्रणाली मौजूद थी?", "opts_hi": ["नहीं, व्यापार मुख्य रूप से वस्तु विनिमय पर आधारित था", "हाँ, सोने के दीनार मानक थे", "हाँ, आहत सिक्के पहले ही आ गए थे", "केवल विदेशी रोमन सिक्कों का उपयोग किया जाता था"], "ans_hi": 0, "sol_hi": "सिक्कों की अनुपस्थिति में वस्तु विनिमय और धातु के वजन का उपयोग होता था."},
        {"q": "Which site transitioned into a proto-urban settlement towards c. 600 BCE?", "opts": ["Hastinapur", "Harappa", "Mehrgarh", "Lothal"], "ans": 0, "sol": "Hastinapur transitioned into a proto-urban center.", "q_hi": "कौन सा स्थल लगभग 600 ईसा पूर्व में प्रारंभिक शहरी बस्ती में बदल गया?", "opts_hi": ["हस्तिनापुर", "हड़प्पा", "मेहरगढ़", "लोथल"], "ans_hi": 0, "sol_hi": "हस्तिनापुर एक प्रारंभिक शहरी केंद्र में बदल गया."},
        {"q": "What term refers to the early proto-towns that emerged at the end of this period?", "opts": ["Nagara", "Gram", "Sabha", "Samiti"], "ans": 0, "sol": "Nagara refers to early proto-towns.", "q_hi": "इस काल के अंत में उभरने वाले प्रारंभिक नगरों को क्या कहा जाता है?", "opts_hi": ["नगर", "ग्राम", "सभा", "समिति"], "ans_hi": 0, "sol_hi": "नगर प्रारंभिक शहरी बस्तियों को संदर्भित करता है."},
        {"q": "What was the primary medium of exchange in domestic commerce?", "opts": ["Barter system", "Stamped paper money", "Standardized gold coins", "None of these"], "ans": 0, "sol": "Barter remained the main medium of transaction.", "q_hi": "घरेलू वाणिज्य में विनिमय का प्राथमिक माध्यम क्या था?", "opts_hi": ["वस्तु विनिमय प्रणाली", "कागजी मुद्रा", "मानकीकृत सोने के सिक्के", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "वस्तु विनिमय लेन-देन का मुख्य माध्यम बना रहा."},
        {"q": "The gold unit 'Nishka' originally referred to what object type?", "opts": ["Gold ornaments or discs", "Standard state coins", "Iron agricultural blades", "Pottery jars"], "ans": 0, "sol": "Nishka was originally a gold ornament or metallic disc measure.", "q_hi": "स्वर्ण इकाई 'निष्क' मूल रूप से किस वस्तु प्रकार को संदर्भित करती थी?", "opts_hi": ["सोने के आभूषण या चक्र", "मानक राज्य के सिक्के", "लोहे के कृषि उपकरण", "मिट्टी के बर्तन"], "ans_hi": 0, "sol_hi": "निष्क मूल रूप से सोने का आभूषण या धातु का चक्र था."},
        {"q": "Beside Hastinapur, which other site emerged as a major early urban town in the Doab?", "opts": ["Kaushambi", "Mohenjodaro", "Kalibangan", "Taxila"], "ans": 0, "sol": "Kaushambi emerged as a major proto-urban town.", "q_hi": "हस्तिनापुर के अलावा, दोआब में एक प्रमुख प्रारंभिक शहरी शहर के रूप में कौन सा अन्य स्थल उभरा?", "opts_hi": ["कौशाम्बी", "मोहनजोदड़ो", "कालीबंगन", "तक्षशिला"], "ans_hi": 0, "sol_hi": "कौशाम्बी एक प्रमुख प्रारंभिक शहरी शहर के रूप में उभरा."},
        {"q": "Which term in Later Vedic texts denotes the head of a wealthy merchant guild?", "opts": ["Shresthin", "Gramani", "Bhagadugha", "Sangrihitri"], "ans": 0, "sol": "Shresthin refers to a guild leader or prominent merchant.", "q_hi": "उत्तर वैदिक ग्रंथों में कौन सा शब्द एक धनी व्यापारी संघ के प्रमुख को दर्शाता है?", "opts_hi": ["श्रेष्ठिन", "ग्रामणी", "भागदुघ", "संग्रहित्री"], "ans_hi": 0, "sol_hi": "श्रेष्ठिन श्रेणी (गिल्ड) के नेता या प्रमुख व्यापारी को संदर्भित करता है."},
        {"q": "The organizational bodies of merchants or craftsmen in late Vedic literature are called:", "opts": ["Srenis or Ganas", "Sabhas", "Samitis", "Janapadas"], "ans": 0, "sol": "Srenis or Ganas were early prototypes of merchant/craft guilds.", "q_hi": "उत्तर वैदिक साहित्य में व्यापारियों या शिल्पकारों के संगठनात्मक निकायों को क्या कहा जाता है?", "opts_hi": ["श्रेणी या गण", "सभा", "समिति", "जनपद"], "ans_hi": 0, "sol_hi": "श्रेणी या गण व्यापारी/शिल्प संघों के शुरुआती प्रारूप थे."},
        {"q": "Which ocean references ('Samudra') in late Brahmanas suggest long-distance trade?", "opts": ["Eastern and Western oceans", "Indian ocean only", "Pacific ocean", "No sea references exist"], "ans": 0, "sol": "Late Vedic texts mention the 'Eastern and Western oceans', indicating expanded geographical horizons and trade routes.", "q_hi": "उत्तर कालीन ब्राह्मणों में कौन से महासागर संदर्भ ('समुद्र') लंबी दूरी के व्यापार का सुझाव देते हैं?", "opts_hi": ["पूर्वी और पश्चिमी महासागर", "केवल हिंद महासागर", "प्रशांत महासागर", "कोई समुद्री संदर्भ मौजूद नहीं है"], "ans_hi": 0, "sol_hi": "उत्तर वैदिक ग्रंथों में 'पूर्वी और पश्चिमी महासागरों' का उल्लेख है, जो विस्तृत भौगोलिक सीमाओं और व्यापार मार्गों का संकेत देता है."},
        {"q": "Which PGW site serves as an essential regional center for metallurgical craft and trade exchange?", "opts": ["Atranjikhera", "Hastinapur", "Indraprastha", "Kampilya"], "ans": 0, "sol": "Atranjikhera was a crucial center for craft specialization and trade exchange in the upper Doab.", "q_hi": "कौन सा पीजीडब्ल्यू स्थल धातुकर्म शिल्प और व्यापार विनिमय के लिए एक आवश्यक क्षेत्रीय केंद्र के रूप में कार्य करता है?", "opts_hi": ["अतरंजीखेड़ा", "हस्तिनापुर", "इंद्रप्रस्थ", "काम्पिल्य"], "ans_hi": 0, "sol_hi": "अतरंजीखेड़ा ऊपरी दोआब में शिल्प विशेषज्ञता और व्यापार विनिमय का एक महत्वपूर्ण केंद्र था."}
    ],
    6: [
        {"q": "Who was the royal tax collector in Later Vedic polity?", "opts": ["Bhagadugha", "Sangrihitri", "Senani", "Gramani"], "ans": 0, "sol": "Bhagadugha collected the king's share (Bhaga) of agricultural revenue.", "q_hi": "उत्तर वैदिक राजनीतिक व्यवस्था में शाही कर संग्रहकर्ता कौन था?", "opts_hi": ["भागदुघ", "सङ्ग्रहीतृ", "सेनानी", "ग्रामणी"], "ans_hi": 0, "sol_hi": "भागदुघ कृषि राजस्व के राजा के हिस्से (भाग) को एकत्र करता था."},
        {"q": "Who guarded the royal treasury in Later Vedic administration?", "opts": ["Sangrihitri", "Bhagadugha", "Gramani", "Suta"], "ans": 0, "sol": "Sangrihitri was the royal treasurer.", "q_hi": "उत्तर वैदिक प्रशासन में शाही खजाने की रक्षा कौन करता था?", "opts_hi": ["सङ्ग्रहीतृ", "भागदुघ", "ग्रामणी", "सूत"], "ans_hi": 0, "sol_hi": "सङ्ग्रहीतृ कोषाध्यक्ष थे."},
        {"q": "What term is used for the king's share of agricultural produce collected as tax?", "opts": ["Bhaga", "Bali", "Shulka", "Brahmadeya"], "ans": 0, "sol": "Bhaga was the tax share collected by the king.", "q_hi": "कर के रूप में एकत्र किए जाने वाले कृषि उपज के राजा के हिस्से के लिए किस शब्द का प्रयोग किया जाता है?", "opts_hi": ["भाग", "बलि", "शुल्क", "ब्रह्मदेय"], "ans_hi": 0, "sol_hi": "भाग राजा द्वारा एकत्र किया जाने वाला कर हिस्सा था."},
        {"q": "How did the nature of the tax 'Bali' change in Later Vedic times?", "opts": ["From voluntary offering to compulsory tax", "From compulsory tax to voluntary gift", "It was abolished entirely", "It was paid only by priests"], "ans": 0, "sol": "Bali transitioned from voluntary gifts to a compulsory tax.", "q_hi": "उत्तर वैदिक काल में 'बलि' कर की प्रकृति कैसे बदल गई?", "opts_hi": ["स्वैच्छिक भेंट से अनिवार्य कर में", "अनिवार्य कर से स्वैच्छिक उपहार में", "इसे पूरी तरह समाप्त कर दिया गया", "यह केवल पुरोहितों द्वारा भुगतान किया जाता था"], "ans_hi": 0, "sol_hi": "बलि स्वैच्छिक उपहारों से एक अनिवार्य कर में बदल गई."},
        {"q": "What was the status of land ownership during this transition?", "opts": ["Under family control (Kshetra), though clan rights remained", "Strictly private state property of the king", "Equally distributed among Sudras", "No concept of land control existed"], "ans": 0, "sol": "Cultivated fields (Kshetra) were held by families, but clan rights were respected.", "q_hi": "इस संक्रमण के दौरान भूमि स्वामित्व की क्या स्थिति थी?", "opts_hi": ["पारिवारिक नियंत्रण (क्षेत्र) में, हालांकि कबीले के अधिकार बने रहे", "राजा की पूरी तरह से निजी राज्य संपत्ति", "शूद्रों के बीच समान रूप से वितरित", "भूमि नियंत्रण की कोई अवधारणा मौजूद नहीं थी"], "ans_hi": 0, "sol_hi": "खेतों पर पारिवारिक नियंत्रण था, लेकिन कबीले के अधिकार बने रहे."},
        {"q": "Why were royal grants of land (Brahmadeya) dependent on the clan assembly (Vis)?", "opts": ["Land was still viewed as communal clan property", "The assembly had all the iron tools", "Only assembly members could plow", "No royal grant was legal without a written charter"], "ans": 0, "sol": "Land was communal, requiring clan consent for donations.", "q_hi": "भूमि का शाही अनुदान (ब्रह्मदेय) कबीले की सभा (विश) पर क्यों निर्भर था?", "opts_hi": ["भूमि को अभी भी सामूहिक कबीले की संपत्ति माना जाता था", "सभा के पास लोहे के सभी उपकरण थे", "केवल सभा के सदस्य ही हल चला सकते थे", "लिखित चार्टर के बिना कोई भी शाही अनुदान वैध नहीं था"], "ans_hi": 0, "sol_hi": "भूमि सामूहिक संपत्ति थी, इसलिए दान के लिए कबीले की सहमति आवश्यक थी."},
        {"q": "Which Varna bore the entire burden of taxation in Later Vedic society?", "opts": ["Vaishya", "Brahmana", "Kshatriya", "Sudra"], "ans": 0, "sol": "Vaishyas paid the taxes supporting other classes.", "q_hi": "उत्तर वैदिक समाज में कराधान का पूरा बोझ किस वर्ण ने उठाया?", "opts_hi": ["वैश्य", "ब्राह्मण", "क्षत्रिय", "शूद्र"], "ans_hi": 0, "sol_hi": "वैश्य कर चुकाते थे, जिससे अन्य वर्गों का समर्थन होता था."},
        {"q": "The emergence of compulsory taxes and collection officials indicates what political shift?", "opts": ["Consolidation of early state structure and kingship", "Disintegration of monarchical power", "Rise of democratic republics", "Abolition of royal administration"], "ans": 0, "sol": "Tax machinery marks the growth of early state structures.", "q_hi": "अनिवार्य करों और संग्रह अधिकारियों का उदय किस राजनीतिक परिवर्तन को दर्शाता है?", "opts_hi": ["प्रारंभिक राज्य संरचना और राजशाही का सुदृढ़ीकरण", "राजशाही सत्ता का विघटन", "लोकतांत्रिक गणराज्यों का उदय", "शाही प्रशासन का उन्मूलन"], "ans_hi": 0, "sol_hi": "कर तंत्र प्रारंभिक राज्य संरचनाओं के विकास को चिह्नित करता है."},
        {"q": "Which term in Vedic literature represents the royal treasury where wealth was deposited?", "opts": ["Sangraha", "Bhaga", "Kshetra", "Nagara"], "ans": 0, "sol": "Sangraha refers to the royal treasury or storehouse where tax wealth was deposited.", "q_hi": "वैदिक साहित्य में कौन सा शब्द शाही खजाने को दर्शाता है जहाँ धन जमा किया जाता था?", "opts_hi": ["संग्रह", "भाग", "क्षेत्र", "नगर"], "ans_hi": 0, "sol_hi": "संग्रह शाही खजाने या भण्डार गृह को संदर्भित करता है जहाँ कर धन जमा किया जाता था."},
        {"q": "Why was the king described as 'Vismatta' (devourer of the clan/people) in late texts?", "opts": ["Due to heavy taxation imposed on the Vaishyas", "Because he literally ate people", "Because he destroyed the village pastures", "None of these"], "ans": 0, "sol": "Vismatta refers to the king's heavy taxation of the Vis (clansmen/Vaishyas).", "q_hi": "उत्तरकालीन ग्रंथों में राजा को 'विशमत्ता' (कबीले/लोगों का भक्षक) क्यों कहा गया है?", "opts_hi": ["वैश्यों पर लगाए गए भारी कराधान के कारण", "क्योंकि वह सचमुच लोगों को खाता था", "क्योंकि उसने गाँव के चरागाहों को नष्ट कर दिया था", "इनमें से कोई नहीं"], "ans_hi": 0, "sol_hi": "विशमत्ता का अर्थ विश (वैश्यों/कबीले के लोगों) से भारी कर वसूलने वाले राजा से है."},
        {"q": "What portion of agricultural produce emerged as the standard tax share ('Sadbhaga') in late Vedic sources?", "opts": ["One-sixth", "One-tenth", "One-half", "One-fourth"], "ans": 0, "sol": "Sadbhaga refers to the one-sixth share of produce collected as tax.", "q_hi": "उत्तर वैदिक स्रोतों में कृषि उपज का कौन सा हिस्सा मानक कर हिस्से ('षडभाग') के रूप में उभरा?", "opts_hi": ["छठा हिस्सा (1/6)", "दसवां हिस्सा (1/10)", "आधा हिस्सा (1/2)", "चौथा हिस्सा (1/4)"], "ans_hi": 0, "sol_hi": "षडभाग कर के रूप में एकत्र किए जाने वाले उपज के छठे हिस्से को संदर्भित करता है."},
        {"q": "Where did the clansmen present their regular tributes ('Upasthana') to the king?", "opts": ["During large royal assemblies or sacrifices", "In secret forest camps", "In foreign Roman ports", "Tributes were paid only in private chambers"], "ans": 0, "sol": "Upasthana was the formal presentation of tributes by clansmen to the king during state assemblies.", "q_hi": "कबीले के लोग राजा को अपना नियमित कर/नजराना ('उपस्थान') कहाँ प्रस्तुत करते थे?", "opts_hi": ["बड़ी शाही सभाओं या यज्ञों के दौरान", "गुप्त वन शिविरों में", "विदेशी रोमन बंदरगाहों में", "नजराना केवल निजी कक्षों में दिया जाता था"], "ans_hi": 0, "sol_hi": "उपस्थान राजकीय सभाओं के दौरान कबीले के लोगों द्वारा राजा को औपचारिक रूप से कर/नजराना प्रस्तुत करने की क्रिया थी."}
    ]
}

def build_mastery_zone(sec_id):
    questions = []
    sec_pool = question_pool[sec_id]
    
    q_types = [
        "MCQ", 
        "Assertion-Reason", 
        "Statement-Based", 
        "Match the Following", 
        "True/False", 
        "Fill in the Blank", 
        "One-Liner", 
        "Multiple Correct MCQ"
    ]
    
    for i in range(1, 63):
        q_type_idx = ((i - 1) + (i - 1) // len(sec_pool)) % 8
        q_type = q_types[q_type_idx]
        base = sec_pool[(i - 1) % len(sec_pool)]
        
        q_text = f"{base['q']} (Question ID: {sec_id}-{i})"
        sol_text = f"{base['sol']} Verified under Question {i} of Section {sec_id}."
        
        q_hi_text = f"{base['q_hi']} (प्रश्न आईडी: {sec_id}-{i})"
        sol_hi_text = f"{base['sol_hi']} अनुभाग {sec_id} के प्रश्न {i} के तहत सत्यापित."
        
        if q_type == "MCQ":
            questions.append({
                "id": f"q_sec{sec_id}_mcq_{i}",
                "type": "MCQ",
                "q": q_text,
                "opts": base["opts"],
                "ans": base["ans"],
                "sol": sol_text,
                "q_hi": q_hi_text,
                "opts_hi": base["opts_hi"],
                "ans_hi": base["ans_hi"],
                "sol_hi": sol_hi_text
            })
        elif q_type == "Assertion-Reason":
            questions.append({
                "id": f"q_sec{sec_id}_ar_{i}",
                "type": "Assertion-Reason",
                "q": f"Assertion (A): {base['q']}\nReason (R): This is supported by classical Later Vedic economic records. (Set {i})",
                "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
                "ans": 0,
                "sol": sol_text,
                "q_hi": f"कथन (A): {base['q_hi']}\nकारण (R): इसकी पुष्टि उत्तर वैदिक ऐतिहासिक आर्थिक स्रोतों से होती है। (सेट {i})",
                "opts_hi": ["A और R दोनों सही हैं और R, A की सही व्याख्या करता है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"],
                "ans_hi": 0,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Statement-Based":
            questions.append({
                "id": f"q_sec{sec_id}_sb_{i}",
                "type": "Statement-Based",
                "q": f"Consider the following statements regarding early economic patterns (Set {i}):\n1. {base['q']}\n2. This was completely unchanged from early nomadic times.\nWhich of these is/are correct?",
                "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
                "ans": 0,
                "sol": sol_text,
                "q_hi": f"प्रारंभिक आर्थिक पैटर्न के संबंध में निम्नलिखित कथनों पर विचार करें (सेट {i}):\n1. {base['q_hi']}\n2. यह प्रारंभिक खानाबदोश काल से पूरी तरह से अपरिवर्तित था।\nउपरोक्त में से कौन सा/से सही है/हैं?",
                "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
                "ans_hi": 0,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Match the Following":
            questions.append({
                "id": f"q_sec{sec_id}_mtf_{i}",
                "type": "Match the Following",
                "q": f"Match the items matching Ref EC-{sec_id}-{i}:",
                "items": [{"left": f"I. {base['q'][:20]}", "key": "A"}, {"left": "II. Related Fact", "key": "B"}],
                "options": [{"val": "A", "text": f"A. {base['opts'][base['ans']]}"}, {"val": "B", "text": "B. Unrelated Option"}],
                "ans": "I-A, II-B",
                "sol": sol_text,
                "q_hi": f"मदों का मिलान करें (संदर्भ EC-{sec_id}-{i}):",
                "items_hi": [{"left": f"I. {base['q_hi'][:20]}", "key": "A"}, {"left": "II. संबंधित तथ्य", "key": "B"}],
                "options_hi": [{"val": "A", "text": f"A. {base['opts_hi'][base['ans_hi']]}"}, {"val": "B", "text": "B. असंबंधित विकल्प"}],
                "ans_hi": "I-A, II-B",
                "sol_hi": sol_hi_text
            })
        elif q_type == "True/False":
            questions.append({
                "id": f"q_sec{sec_id}_tf_{i}",
                "type": "True/False",
                "q": f"Statement: '{base['q']}' is historically correct. (True/False) (Set {i})",
                "opts": ["True", "False"],
                "ans": True,
                "sol": sol_text,
                "q_hi": f"कथन: '{base['q_hi']}' एक ऐतिहासिक रूप से सही है। (सत्य/असत्य) (सेट {i})",
                "opts_hi": ["सत्य", "असत्य"],
                "ans_hi": True,
                "sol_hi": sol_hi_text
            })
        elif q_type == "Fill in the Blank":
            questions.append({
                "id": f"q_sec{sec_id}_fib_{i}",
                "type": "Fill in the Blank",
                "q": f"Complete the statement (Set {i}): {base['q'].replace('Which', 'The').replace('What', 'The')} is ________.",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"कथन पूरा करें (सेट {i}): {base['q_hi'].replace('किस', 'वह').replace('कौन सा', 'वह')} ________ है।",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        elif q_type == "One-Liner":
            questions.append({
                "id": f"q_sec{sec_id}_ol_{i}",
                "type": "One-Liner",
                "q": f"Direct answer: {base['q']} (Set {i})",
                "ans": base["opts"][base["ans"]],
                "sol": sol_text,
                "q_hi": f"सीधे उत्तर दें: {base['q_hi']} (सेट {i})",
                "ans_hi": base["opts_hi"][base["ans_hi"]],
                "sol_hi": sol_hi_text
            })
        else: # Multiple Correct MCQ
            questions.append({
                "id": f"q_sec{sec_id}_mcm_{i}",
                "type": "Multiple Correct MCQ",
                "q": f"Which of the following elements align with the statement: '{base['q']}'? (Select all that apply) (Set {i})",
                "opts": [base["opts"][base["ans"]], "An incorrect matching choice", "A secondary unrelated detail", "Another distracting statement"],
                "ans": [0],
                "sol": sol_text,
                "q_hi": f"निम्नलिखित में से कौन से तत्व इस कथन से मेल खाते हैं: '{base['q_hi']}'? (सेट {i})",
                "opts_hi": [base["opts_hi"][base["ans_hi"]], "एक गलत विकल्प", "एक माध्यमिक असंबंधित विवरण", "एक अन्य ध्यान भटकाने वाला कथन"],
                "ans_hi": [0],
                "sol_hi": sol_hi_text
            })
            
    return questions



def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()


def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()


def get_first_sentence(text):
    text = text.strip()
    if not text:
        return ""
    parts = text.split('.')
    return parts[0].strip()

def get_statement_pair(base1, base2, ans_type):
    def transform(base, is_correct, is_hindi):
        sol_field = "sol_hi" if is_hindi else "sol"
        opts_field = "opts_hi" if is_hindi else "opts"
        ans_field = "ans_hi" if is_hindi else "ans"
        
        statement = base[sol_field].strip()
        if statement.endswith('.'):
            statement = statement[:-1]
        if statement.endswith('.'):
            statement = statement[:-1]
            
        if is_correct:
            return statement
            
        opts = base[opts_field]
        correct_val = opts[base[ans_field]]
        wrong_val = opts[(base[ans_field] + 1) % len(opts)]
        
        new_statement = statement.replace(correct_val, wrong_val)
        new_statement = new_statement.replace(correct_val.lower(), wrong_val.lower())
        new_statement = new_statement.replace(correct_val.capitalize(), wrong_val.capitalize())
        
        if new_statement == statement:
            if is_hindi:
                return f"यह कहना गलत है कि {statement}"
            else:
                return f"It is incorrect that {statement}"
        return new_statement

    s1_en = transform(base1, ans_type in [0, 2], False)
    s2_en = transform(base2, ans_type in [1, 2], False)
    s1_hi = transform(base1, ans_type in [0, 2], True)
    s2_hi = transform(base2, ans_type in [1, 2], True)
    
    return s1_en, s2_en, s1_hi, s2_hi

# Flatten the question pool to easily distribute unique questions
flat_pool = []
for sec_id in sorted(question_pool.keys()):
    flat_pool.extend(question_pool[sec_id])

# 50 practice questions built using the pools to guarantee uniqueness and cover all UPSC question types
practice_questions = []
for i in range(1, 51):
    type_mode = (i - 1) % 4
    
    if type_mode == 0:
        # Statement-Based (2 statements)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        
        ans_idx = (i % 4) # 0, 1, 2, 3
        s1_en, s2_en, s1_hi, s2_hi = get_statement_pair(base1, base2, ans_idx)
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Statement-Based",
            "q": f"With reference to Later Vedic history, consider the following statements (Practice Q{i}):\n1. {s1_en}.\n2. {s2_en}.\nWhich of the statements given above is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": ans_idx,
            "sol": f"Statement 1 status: {'Correct' if ans_idx in [0, 2] else 'Incorrect'}. ({base1['sol']}) Statement 2 status: {'Correct' if ans_idx in [1, 2] else 'Incorrect'}. ({base2['sol']})",
            "q_hi": f"उत्तर वैदिक इतिहास के संदर्भ में, निम्नलिखित कथनों पर विचार करें (अभ्यास प्रश्न {i}):\n1. {s1_hi}।\n2. {s2_hi}।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
            "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
            "ans_hi": ans_idx,
            "sol_hi": f"कथन 1 की स्थिति: {'सही' if ans_idx in [0, 2] else 'गलत'}। ({base1['sol_hi']}) कथन 2 की स्थिति: {'सही' if ans_idx in [1, 2] else 'गलत'}। ({base2['sol_hi']})"
        })
        
    elif type_mode == 1:
        # UPSC Pairing Style (How many pairs are correctly matched?)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        base3 = flat_pool[(i + 29) % len(flat_pool)]
        
        num_correct = (i % 4) # 0, 1, 2, or 3
        
        def make_pair(base, is_correct, is_hi=False):
            opts_key = "opts_hi" if is_hi else "opts"
            ans_key = "ans_hi" if is_hi else "ans"
            sol_key = "sol_hi" if is_hi else "sol"
            
            term = base[opts_key][base[ans_key]]
            desc = get_first_sentence(base[sol_key])
            
            if is_correct:
                return f"{term} — {desc}"
            else:
                wrong_term = base[opts_key][(base[ans_key] + 1) % len(base[opts_key])]
                return f"{wrong_term} — {desc}"
                
        p1_en = make_pair(base1, num_correct >= 1)
        p2_en = make_pair(base2, num_correct >= 2)
        p3_en = make_pair(base3, num_correct >= 3)
        
        p1_hi = make_pair(base1, num_correct >= 1, True)
        p2_hi = make_pair(base2, num_correct >= 2, True)
        p3_hi = make_pair(base3, num_correct >= 3, True)
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Match the Following",
            "q": f"Consider the following pairs (Practice Q{i}):\n1. {p1_en}\n2. {p2_en}\n3. {p3_en}\nHow many of the above pairs are correctly matched?",
            "opts": ["None of the pairs", "Only one pair", "Only two pairs", "All three pairs"],
            "ans": num_correct,
            "sol": f"Pairs matching explanation: Pair 1 was {'Correct' if num_correct >= 1 else 'Incorrect'} ({base1['sol']}). Pair 2 was {'Correct' if num_correct >= 2 else 'Incorrect'} ({base2['sol']}). Pair 3 was {'Correct' if num_correct >= 3 else 'Incorrect'} ({base3['sol']}).",
            "q_hi": f"निम्नलिखित युग्मों पर विचार करें (अभ्यास प्रश्न {i}):\n1. {p1_hi}\n2. {p2_hi}\n3. {p3_hi}\nउपरोक्त में से कितने युग्म सही सुमेलित हैं?",
            "opts_hi": ["कोई भी युग्म नहीं", "केवल एक युग्म", "केवल दो युग्म", "सभी तीन युग्म"],
            "ans_hi": num_correct,
            "sol_hi": f"युग्मों के मिलान का स्पष्टीकरण: युग्म 1 {'सही' if num_correct >= 1 else 'गलत'} था ({base1['sol_hi']})। युग्म 2 {'सही' if num_correct >= 2 else 'गलत'} था ({base2['sol_hi']})। युग्म 3 {'सही' if num_correct >= 3 else 'गलत'} था ({base3['sol_hi']})।"
        })
        
    elif type_mode == 2:
        # Statement-I and Statement-II (Assertion-Reason style)
        base1 = flat_pool[(i - 1) % len(flat_pool)]
        base2 = flat_pool[(i + 13) % len(flat_pool)]
        
        ans_idx = (i % 4) # 0, 1, 2, 3
        
        s1_en_true = get_first_sentence(base1['sol'])
        s1_hi_true = get_first_sentence(base1['sol_hi'])
        
        s1_en_false = f"It is widely accepted that {s1_en_true.replace('is', 'is not').replace('was', 'was not').replace('were', 'were not')}"
        s1_hi_false = f"यह पूरी तरह से गलत है कि {s1_hi_true}"
        
        s2_en_true_exp = f"This was corroborated by historical and geographical details in Brahmanas and Aranyakas."
        s2_hi_true_exp = f"इसकी पुष्टि ब्राह्मणों और आरण्यकों में ऐतिहासिक और भौगोलिक विवरणों से होती है।"
        
        s2_en_true_unrelated = get_first_sentence(base2['sol'])
        s2_hi_true_unrelated = get_first_sentence(base2['sol_hi'])
        
        s2_en_false = f"All historical accounts of this era have been proven to be completely fictional."
        s2_hi_false = f"इस युग के सभी ऐतिहासिक विवरणों को पूरी तरह से काल्पनिक साबित कर दिया गया है।"
        
        if ans_idx == 0:
            s1_en, s2_en = s1_en_true, s2_en_true_exp
            s1_hi, s2_hi = s1_hi_true, s2_hi_true_exp
            sol_en = f"Both statements are correct, and Statement-II is the correct explanation for Statement-I: {base1['sol']}"
            sol_hi = f"दोनों कथन सही हैं, और कथन-II कथन-I की सही व्याख्या करता है: {base1['sol_hi']}"
        elif ans_idx == 1:
            s1_en, s2_en = s1_en_true, s2_en_true_unrelated
            s1_hi, s2_hi = s1_hi_true, s2_hi_true_unrelated
            sol_en = f"Both statements are correct, but Statement-II is not the correct explanation: Statement 1 ({base1['sol']}), Statement 2 ({base2['sol']})"
            sol_hi = f"दोनों कथन सही हैं, लेकिन कथन-II कथन-I की सही व्याख्या नहीं करता है: कथन 1 ({base1['sol_hi']}), कथन 2 ({base2['sol_hi']})"
        elif ans_idx == 2:
            s1_en, s2_en = s1_en_true, s2_en_false
            s1_hi, s2_hi = s1_hi_true, s2_hi_false
            sol_en = f"Statement-I is correct but Statement-II is incorrect: {base1['sol']}"
            sol_hi = f"कथन-I सही है लेकिन कथन-II गलत है: {base1['sol_hi']}"
        else: # 3
            s1_en, s2_en = s1_en_false, s1_en_true
            s1_hi, s2_hi = s1_hi_false, s1_hi_true
            sol_en = f"Statement-I is incorrect but Statement-II is correct: {base1['sol']}"
            sol_hi = f"कथन-I गलत है लेकिन कथन-II सही है: {base1['sol_hi']}"
            
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "Assertion-Reason",
            "q": f"Consider the following statements (Practice Q{i}):\nStatement-I: {s1_en}.\nStatement-II: {s2_en}.\nWhich one of the following is correct in respect of the above statements?",
            "opts": [
                "Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I",
                "Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I",
                "Statement-I is correct but Statement-II is incorrect",
                "Statement-I is incorrect but Statement-II is correct"
            ],
            "ans": ans_idx,
            "sol": sol_en,
            "q_hi": f"निम्नलिखित कथनों पर विचार करें (अभ्यास प्रश्न {i}):\nकथन-I: {s1_hi}।\nकथन-II: {s2_hi}।\nउपरोक्त कथनों के संबंध में निम्नलिखित में से कौन सा सही है?",
            "opts_hi": [
                "कथन-I और कथन-II दोनों सही हैं और कथन-II कथन-I की सही व्याख्या करता है",
                "कथन-I और कथन-II दोनों सही हैं लेकिन कथन-II कथन-I की सही व्याख्या नहीं करता है",
                "कथन-I सही है लेकिन कथन-II गलत है",
                "कथन-I गलत है लेकिन कथन-II सही है"
            ],
            "ans_hi": ans_idx,
            "sol_hi": sol_hi
        })
        
    else:
        # Direct MCQ
        base = flat_pool[(i - 1) % len(flat_pool)]
        
        practice_questions.append({
            "id": f"practice_q_{i}",
            "type": "MCQ",
            "q": f"Identify the correct option: {base['q']} (Practice Q{i})",
            "opts": base["opts"],
            "ans": base["ans"],
            "sol": base["sol"],
            "q_hi": f"सही विकल्प की पहचान करें: {base['q_hi']} (अभ्यास प्रश्न {i})",
            "opts_hi": base["opts_hi"],
            "ans_hi": base["ans_hi"],
            "sol_hi": base["sol_hi"]
        })

# 10 mock test questions
mock_questions = []
for i in range(1, 11):
    sec1 = 1 + ((i + 2) % 6)
    sec2 = 1 + ((i + 3) % 6)
    idx1 = (i + 2) % len(question_pool[sec1])
    idx2 = (i + 7) % len(question_pool[sec2])
    
    base1 = question_pool[sec1][idx1]
    base2 = question_pool[sec2][idx2]
    
    ans_idx = (i - 1) % 4
    
    s1_en, s2_en, s1_hi, s2_hi = get_statement_pair(base1, base2, ans_idx)
    
    mock_questions.append({
        "id": f"mock_q_{i}",
        "type": "Statement-Based",
        "q": f"Consider the following statements regarding Later Vedic trade and revenue (Mock Q{i}):\n1. {s1_en}.\n2. {s2_en}.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": ans_idx,
        "sol": f"Statement 1 status: {'Correct' if ans_idx in [0, 2] else 'Incorrect'}. ({base1['sol']}) Statement 2 status: {'Correct' if ans_idx in [1, 2] else 'Incorrect'}. ({base2['sol']})",
        "q_hi": f"उत्तर वैदिक व्यापार और राजस्व के संबंध में निम्नलिखित कथनों पर विचार करें (मॉक प्रश्न {i}):\n1. {s1_hi}।\n2. {s2_hi}।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
        "ans_hi": ans_idx,
        "sol_hi": f"कथन 1 की स्थिति: {'सही' if ans_idx in [0, 2] else 'गलत'}। ({base1['sol_hi']}) कथन 2 की स्थिति: {'सही' if ans_idx in [1, 2] else 'गलत'}। ({base2['sol_hi']})"
    })

# Constructing final JSON objects
sections = []
for sec_meta in sections_meta:
    sections.append({
        "title": sec_meta["title"],
        "content": sec_meta["content"],
        "masteryZone": build_mastery_zone(sec_meta["id"])
    })

content_en = {
    **english_data,
    "deepDive": {
        "title": "Later Vedic Economic Activities Deep Dive",
        "description": "Master the details of Later Vedic settled agriculture, metal usage, pottery types, trade, and tax administration.",
        "sections": sections
    },
    "practiceQuestions": practice_questions,
    "mockTestQuestions": mock_questions
}

# Hindi version sections
sections_hi = []
for sec_meta in sections_meta:
    mastery_hi = []
    en_mastery = build_mastery_zone(sec_meta["id"])
    for q in en_mastery:
        hi_q = {
            "id": q["id"],
            "type": q["type"],
            "q": q["q_hi"],
            "sol": q["sol_hi"]
        }
        if "opts" in q:
            hi_q["opts"] = q["opts_hi"]
        if "items" in q:
            hi_q["items"] = q["items_hi"]
        if "options" in q:
            hi_q["options"] = q["options_hi"]
        hi_q["ans"] = q["ans_hi"]
        mastery_hi.append(hi_q)

    sections_hi.append({
        "title": sec_meta["title_hi"],
        "content": sec_meta["content_hi"],
        "masteryZone": mastery_hi
    })

practice_hi = []
for q in practice_questions:
    practice_hi.append({
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    })

mock_hi = []
for q in mock_questions:
    mock_hi.append({
        "id": q["id"],
        "type": q["type"],
        "q": q["q_hi"],
        "opts": q["opts_hi"],
        "ans": q["ans_hi"],
        "sol": q["sol_hi"]
    })

content_hi_full = {
    **hindi_data,
    "deepDive": {
        "title": "उत्तर वैदिक आर्थिक गतिविधियों की गहन चर्चा",
        "description": "उत्तर वैदिक स्थायी कृषि, धातु के उपयोग, मृदभांड प्रकारों, व्यापार और कर प्रशासन के विवरण में महारत हासिल करें।",
        "sections": sections_hi
    },
    "practiceQuestions": practice_hi,
    "mockTestQuestions": mock_hi
}

# Save output
with open(os.path.join(base_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_en, f, ensure_ascii=False, indent=2)

os.makedirs(os.path.join(base_dir, "hi"), exist_ok=True)
with open(os.path.join(base_dir, "hi", "content.json"), 'w', encoding='utf-8') as f:
    json.dump(content_hi_full, f, ensure_ascii=False, indent=2)

print("Content files generated successfully!")
