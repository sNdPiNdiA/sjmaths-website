import json
import os
import sys

# Append questions_data directory to search path
sys.path.append(os.path.join(os.path.dirname(__file__), 'questions_data'))

# Import all modular sections and questions
from section1 import section1_en, section1_hi
from section2 import section2_en, section2_hi
from section3 import section3_en, section3_hi
from section4 import section4_en, section4_hi
from section5 import section5_en, section5_hi
from practice import practice_en, practice_hi
from mock import mock_en, mock_hi

# Base English Database
en_data = {
  "breadcrumbs": {
    "parent": "UPSC Syllabus",
    "parentUrl": "/upsc/",
    "description": "Master Pedro Álvares Cabral's 1500 CE expedition, the discovery of Brazil, the conflicts in Calicut, the first factory in Cochin, and the foundations of the Portuguese trade monopoly."
  },
  "timeline": {
    "title": "Pedro Álvares Cabral's Expedition & Impact",
    "description": "Click on each card to follow the chronological milestones of Cabral's historic voyage to India and the discovery of Brazil.",
    "cards": [
      {
        "period": "Lisbon Departure",
        "date": "March 1500 CE",
        "details": "Cabral departs from Lisbon with 13 ships, carrying 1,200 to 1,500 men, sponsored by King Manuel I to establish stable trade relations in India."
      },
      {
        "period": "Discovery of Brazil",
        "date": "April 1500 CE",
        "details": "Swinging far west to catch favorable winds (Volta do Mar), Cabral discovers Brazil, claims it for Portugal, and sends Gaspar de Lemos back with the news."
      },
      {
        "period": "Arrival at Calicut",
        "date": "September 1500 CE",
        "details": "After losing 4 ships in a storm (including Bartolomeu Dias's vessel), Cabral arrives in Calicut. He sets up the first factory under Aires Correia."
      },
      {
        "period": "Factory Massacre & Retaliation",
        "date": "December 1500 CE",
        "details": "Arab merchants attack the factory, killing Aires Correia and 50 men. Cabral retaliates by bombarding Calicut and capturing 10 Arab vessels."
      },
      {
        "period": "Cochin & Kannur Alliances",
        "date": "Dec 1500 – Jan 1501 CE",
        "details": "Cabral allies with Cochin's ruler (Trimumpara Raja) and Kannur's Kolathiri. He loads spices and sails back before the Zamorin's fleet attacks."
      },
      {
        "period": "Return to Lisbon",
        "date": "July 1501 CE",
        "details": "Cabral returns to Lisbon with only 6 of the original 13 ships, but the spice cargo fully covers the costs and generates significant profits."
      }
    ]
  },
  "mnemonics": {
    "title": "Mnemonics & Memory Hacks",
    "description": "Memory triggers to quickly recall details of Cabral's voyages.",
    "items": [
      {
        "title": "Mnemonic 1: The Three Malabar Ports",
        "phrase": "\"C-C-K\" — Calicut, Cochin, Kannur",
        "decryption": "The order of ports visited by Cabral in India: **Calicut** (conflict), **Cochin** (alliance & factory), and **Kannur** (loading spices & alliance)."
      },
      {
        "title": "Mnemonic 2: Crucial Losses and Discoveries",
        "phrase": "\"B-B-D\" — Brazil, Bombardment, Dias",
        "decryption": "Cabral's voyage is famous for discovering **Brazil**, the **Bombardment** of Calicut, and the drowning of Bartolomeu **Dias**."
      }
    ]
  },
  "traps": {
    "title": "UPSC Common Exam Traps",
    "items": [
      "<strong>Trap 1: The Discovery of Brazil:</strong> UPSC might suggest that the discovery of Brazil was a planned expedition. In reality, it was an accidental/divergent landing caused by swinging southwest to catch trade winds (Volta do Mar), though some historians argue secret crown knowledge existed.",
      "<strong>Trap 2: The First Factory:</strong> Do not confuse Vasco da Gama's alliances with Cabral's achievements. Vasco da Gama secured trade permissions, but **Pedro Álvares Cabral** established the first physical warehouse/factory in Calicut, and later Cochin.",
      "<strong>Trap 3: The Viceroy Title:</strong> Cabral was a nobleman and captain-major, but he was never appointed Governor or Viceroy of India. Francisco de Almeida was the first Governor/Viceroy in 1505."
    ]
  },
  "deepDive": {
    "title": "Syllabus Core Study Notes (Deep-Dive)",
    "description": "Master Pedro Álvares Cabral's voyages, route details, conflicts, and historical legacy in India.",
    "sections": [
      {
        "title": "1. Fleet Preparation & Brazil Discovery (March - April 1500)",
        "content": "<p>Following Vasco da Gama's return in 1499, King Manuel I commissioned a massive, highly militarized armada to establish permanent trade relations with India and secure a royal monopoly. Commanded by the nobleman <strong>Pedro Álvares Cabral</strong>, the fleet consisted of 13 ships (including heavy carracks/naus and fast caravels) carrying 1,200 to 1,500 soldiers, sailors, and merchants. Among the captains was the veteran explorer Bartolomeu Dias.</p><p>To avoid the adverse currents and doldrums of the Gulf of Guinea along the West African coast, the fleet sailed in a wide southwesterly loop into the open Atlantic, a navigation maneuver known as the <strong>Volta do Mar</strong>. This strategic detour led to the accidental/divergent sighting of the Brazilian coast. On April 22, 1500, the fleet sighted a mountain they named <strong>Monte Pascoal</strong> and anchored at a safe harbor named <strong>Porto Seguro</strong>. Cabral claimed the land for Portugal under the terms of the <strong>Treaty of Tordesillas (1494)</strong>, naming it <strong>Ilha de Vera Cruz</strong> (Island of the True Cross). The fleet's official scribe, <strong>Pero Vaz de Caminha</strong>, wrote a detailed letter reporting the discovery to King Manuel I, which was sent back to Lisbon aboard a supply ship commanded by <strong>Gaspar de Lemos</strong>, before the rest of the fleet continued to India.</p>"
      },
      {
        "title": "2. Voyage across the Indian Ocean & Arrival at Calicut",
        "content": "<p>In May 1500, Cabral's remaining 12 ships departed Brazil to cross the southern Atlantic towards Africa. Near the <strong>Cape of Good Hope</strong>, the fleet encountered a sudden, violent tempest that sank four ships, drowning all crews, including the legendary pioneer <strong>Bartolomeu Dias</strong>. Another ship, commanded by his brother Diogo Dias, was separated from the fleet and sailed east, eventually discovering the island of <strong>Madagascar</strong>, which he named <em>São Lourenço</em>.</p><p>The remaining ships regrouped and made stopovers along the East African Swahili coast. They explored <strong>Sofala</strong> to assess its gold trade potential, bypassed hostile Mombasa, and found a cooperative ally in the Sultan of <strong>Malindi</strong>. The Sultan provided the Portuguese with an experienced Gujarati/Arab pilot who guided the fleet across the Arabian Sea using the southwest summer monsoon winds. On <strong>September 13, 1500</strong>, Cabral's remaining ships anchored at Calicut. The Hindu ruler, the <strong>Zamorin (Samudiri)</strong>, received Cabral warmly, granted him an audience, and signed a commercial treaty permitting the Portuguese to establish a trading post.</p>"
      },
      {
        "title": "3. Aires Correia & The Calicut Factory Massacre",
        "content": "<p>Under the terms of the treaty, the Portuguese established a physical trading post and warehouse, known as a <strong>feitoria</strong> (factory), in Calicut, managed by the chief factor (feitor) <strong>Aires Correia</strong>. The objective was to purchase and store black pepper and ginger directly from local merchants for shipment to Lisbon. However, this direct crown trading bypassed the traditional networks controlled by Arab and Muslim merchant guilds, who held a centuries-old monopoly on spice exports in Calicut.</p><p>Tensions escalated as Arab merchants systematically bought up available pepper supplies, causing long delays for the Portuguese. Friction reached a boiling point when the Zamorin granted the Portuguese permission to search Arab vessels suspected of hoarding spices. In December 1500, a large mob, instigated by Arab traders, launched a violent assault on the feitoria. Chief factor Aires Correia, three Franciscan missionary friars, and around 50 Portuguese men were killed, and the warehouse was destroyed. Cabral retaliated fiercely: he seized 10 Arab merchant vessels in the harbor, confiscated their spice cargoes, executed their crews (~600 men), and ordered a devastating 24-hour naval bombardment of Calicut, killing an estimated 600 citizens and destroying harbor structures before sailing south.</p>"
      },
      {
        "title": "4. Alliances with Cochin & Kannur",
        "content": "<p>Departing Calicut, Cabral strategically capitalized on pre-existing political rivalries along the Malabar Coast. He sailed to <strong>Cochin (Kochi)</strong>, whose ruler, <strong>Unni Goda Varma</strong> (the Trimumpara Raja), was a subordinate vassal of the Zamorin and eagerly sought military assistance to break Calicut's dominance. The Raja signed a commercial treaty with Cabral, allowed the establishment of a factory, and assisted the Portuguese in rapidly loading their ships with black pepper and ginger. The chief factor <strong>Gonçalo Gil Barbosa</strong> was left behind with a small garrison to manage the warehouse.</p><p>Cabral also established friendly trade relations with the Kolathiri Raja of <strong>Kannur</strong> (Cannanore) further north, loading additional spices. In January 1501, the Zamorin dispatched a massive war fleet of around 80 ships to attack the Portuguese at Cochin. Warned of the threat, Cabral hastily sailed away, leaving behind his factors under the protection of the Cochin ruler, who refused to surrender them to the Zamorin's forces. This alliance laid the geopolitical foundation for Cochin to serve as the first Portuguese headquarters in India.</p>"
      },
      {
        "title": "5. Return to Lisbon & Geopolitical Legacy",
        "content": "<p>Cabral's fleet sailed across the Indian Ocean and around the Cape of Good Hope, arriving back in Lisbon in <strong>July 1501 CE</strong>. Out of the 13 ships that had departed in March 1500, only 6 returned safely. Despite the loss of 7 ships and hundreds of lives, the spice cargo brought back by the surviving vessels was so large and valuable that its sale generated immense profits, fully covering the costs of the entire expedition and the lost ships.</p><p>The voyage verified the immense commercial viability of the Cape Route. In Lisbon, the crown expanded the state department <strong>Casa da Índia</strong> to regulate import monopolies, and institutionalized the annual spice fleet system known as the <strong>Carreira da Índia</strong>. Geopolitically, the diversion of trade from the Red Sea route broke the Venetian spice distribution monopoly and severely weakened the <strong>Mamluk Sultanate of Egypt</strong>, facilitating its conquest by the Ottoman Empire in 1517. Despite his success, Cabral fell out of favor with King Manuel I due to command disputes for the 1502 armada (which was given to Vasco da Gama) and the high rate of ship losses. Cabral retired to his estates in <strong>Santarém</strong>, where he died in 1520, leaving behind the framework of the Portuguese trade monopoly.</p>"
      }
    ]
  }
}

# Base Hindi Database
hi_data = {
  "breadcrumbs": {
    "parent": "यूपीएससी पाठ्यक्रम",
    "parentUrl": "/upsc/",
    "current": "पुर्तगाली: पेड्रो अल्वारेज़ कैब्राल"
  },
  "hero": {
    "title": "पुर्तगाली: पेड्रो अल्वारेज़ कैब्राल",
    "description": "पेड्रो अल्वारेज़ कैब्राल के 1500 ईस्वी के अभियान, ब्राजील की खोज, कालीकट में संघर्ष, कोचीन में पहली फैक्ट्री और पुर्तगाली व्यापारिक एकाधिकार की नींव पर महारत हासिल करें।"
  },
  "timeline": {
    "title": "पेड्रो अल्वारेज़ कैब्राल का अभियान और प्रभाव",
    "description": "भारत में पुर्तगाली उपस्थिति स्थापित करने और ब्राजील की खोज में पेड्रो अल्वारेज़ कैब्राल की ऐतिहासिक यात्रा के मील के पत्थर का पता लगाने के लिए प्रत्येक कार्ड पर क्लिक करें।",
    "cards": [
      {
        "period": "लिस्बन प्रस्थान",
        "date": "मार्च 1500 ईस्वी",
        "details": "कैब्राल भारत में स्थिर व्यापार संबंध स्थापित करने के लिए राजा मैनुअल प्रथम द्वारा प्रायोजित 13 जहाजों और लगभग 1,200 से 1,500 पुरुषों के साथ लिस्बन से रवाना हुए।"
      },
      {
        "period": "ब्राजील की खोज",
        "date": "अप्रैल 1500 ईस्वी",
        "details": "अनुकूल हवाओं को पकड़ने के लिए अटलांटिक में काफी पश्चिम की ओर घूमकर (वोल्टा डो मार), कैब्राल ने ब्राजील की खोज की, उस पर पुर्तगाल का दावा किया और समाचार के साथ गास्पर डी लेमोस को वापस भेजा।"
      },
      {
        "period": "कालीकट आगमन",
        "date": "सितंबर 1500 ईस्वी",
        "details": "केप ऑफ गुड होप के पास एक तूफान में 4 जहाजों (बार्टोलोम्यू डियास के जहाज सहित) को खोने के बाद, कैब्राल कालीकट पहुंचे। उन्होंने ऐरेस कोरिया के तहत पहली फैक्ट्री स्थापित की।"
      },
      {
        "period": "फैक्ट्री नरसंहार और जवाबी कार्रवाई",
        "date": "दिसंबर 1500 ईस्वी",
        "details": "अरब व्यापारियों ने फैक्ट्री पर हमला किया, जिसमें ऐरेस कोरिया और 50 पुर्तगाली मारे गए। कैब्राल ने कालीकट पर बमबारी करके और 10 अरब जहाजों को जब्त करके जवाबी कार्रवाई की।"
      },
      {
        "period": "कोचीन और कन्नूर गठबंधन",
        "date": "दिसंबर 1500 - जनवरी 1501 ईस्वी",
        "details": "कैब्राल ने कोचीन के शासक (त्रिमुम्पारा राजा) और कन्नूर के कोलाथिरी के साथ गठबंधन किया। ज़मोरिन के बेड़े के हमले से पहले उन्होंने मसाले लोड किए और वापस रवाना हो गए।"
      }
    ]
  },
  "mnemonics": {
    "title": "स्मरणोदहार और मेमोरी ट्रिक्स",
    "description": "कैब्राल की यात्राओं के विवरणों को जल्दी से याद रखने के लिए मेमोरी ट्रिक्स।",
    "items": [
      {
        "title": "ट्रिक 1: तीन मालाबार बंदरगाह",
        "phrase": "\"C-C-K\" — कालीकट, कोचीन, कन्नूर",
        "decryption": "भारत में कैब्राल द्वारा दौरा किए गए बंदरगाहों का क्रम: कालीकट (संघर्ष), कोचीन (गठबंधन और फैक्ट्री), और कन्नूर (मसाले लोड करना और गठबंधन)।"
      },
      {
        "title": "ट्रिक 2: महत्वपूर्ण नुकसान और खोजें",
        "phrase": "\"B-B-D\" — ब्राजील, बमबारी, डियास",
        "decryption": "कैब्राल की यात्रा ब्राजील की खोज, कालीकट पर बमबारी, और बार्टोलोम्यू डियास के डूबने के लिए प्रसिद्ध है।"
      }
    ]
  },
  "traps": {
    "title": "यूपीएससी परीक्षा के सामान्य जाल",
    "items": [
      "<strong>जाल 1: ब्राजील की खोज:</strong> यूपीएससी संकेत दे सकता है कि ब्राजील की खोज एक योजनाबद्ध अभियान थी। वास्तव में, यह व्यापारिक हवाओं (वोल्टा डो मार) को पकड़ने के लिए दक्षिण-पश्चिम में घूमने के कारण एक आकस्मिक लैंडिंग थी, हालांकि कुछ इतिहासकारों का तर्क है कि क्राउन को पहले से गुप्त जानकारी थी।",
      "<strong>जाल 2: पहली फैक्ट्री:</strong> वास्को डी गामा के गठबंधनों को कैब्राल की उपलब्धियों के साथ न मिलाएं। वास्को डी गामा ने व्यापारिक अनुमति सुरक्षित की थी, लेकिन **पेड्रो अल्वारेज़ कैब्राल** ने कालीकट और बाद में कोचीन में पहला गोदाम/फैक्ट्री स्थापित की थी।",
      "<strong>जाल 3: वायसराय की उपाधि:</strong> कैब्राल एक रईस और कैप्टन-मेजर थे, लेकिन उन्हें कभी भी भारत का गवर्नर या वायसराय नियुक्त नहीं किया गया था। फ्रांसिस्को डी अल्मेडा 1505 में पहले गवर्नर/वायसराय बने थे।"
    ]
  },
  "deepDive": {
    "title": "पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)",
    "description": "पेड्रो अल्वारेज़ कैब्राल की यात्राओं, उनके मार्ग विवरण, संघर्षों और भारत में ऐतिहासिक विरासत पर महारत हासिल करें।",
    "sections": [
      {
        "title": "1. बेड़ा तैयारी और ब्राजील की खोज (मार्च - अप्रैल 1500)",
        "content": "<p>वास्को डी गामा की 1499 में सफल वापसी के बाद, पुर्तगाली राजा मैनुअल प्रथम ने भारत के साथ सीधे व्यापारिक संबंध स्थापित करने और शाही एकाधिकार सुनिश्चित करने के लिए एक विशाल और अत्यधिक सैन्यीकृत बेड़े का गठन किया। इस दूसरे अभियान की कमान पुर्तगाली रईस <strong>पेड्रो अल्वारेज़ कैब्राल</strong> को सौंपी गई। इस बेड़े में 13 जहाज (जिसमें भारी नाउ और तेज चलने वाली कारवेल शामिल थीं) शामिल थीं, जिन पर लगभग 1,200 से 1,500 सैनिक, नाविक और व्यापारी सवार थे। बेड़े के कप्तानों में अनुभवी खोजकर्ता बार्टोलोम्यू डियास भी शामिल थे।</p><p>पश्चिम अफ्रीकी तट (गिनी की खाड़ी) की प्रतिकूल हवाओं और धाराओं से बचने के लिए, कैब्राल ने अटलांटिक महासागर में दक्षिण-पश्चिम की ओर एक विस्तृत मोड़ लिया। इस नौसैनिक रणनीति को <strong>वोल्टा डो मार</strong> कहा जाता था। इसी मोड़ के दौरान अप्रत्याशित रूप से 22 अप्रैल 1500 को उन्हें ब्राजील का तट दिखाई दिया। उन्होंने वहां दिखाई देने वाले पहले पर्वत का नाम <strong>मोंटे पास्कोआल</strong> रखा और एक सुरक्षित बंदरगाह <strong>पोर्टो सेगुइरो</strong> में लंगर डाला। कैब्राल ने <strong>1494 की टॉर्डेसिलस की संधि</strong> के तहत पुर्तगाल के लिए इस भूमि पर दावा किया और इसका नाम <strong>इल्हा दे वेरा क्रूज़</strong> (सच्चे क्रॉस का द्वीप) रखा। पेरो वाज़ दे कामिन्हा ने इस खोज की विस्तृत रिपोर्ट तैयार की, जिसे आपूर्ति जहाज के कप्तान गास्पर डी लेमोस के माध्यम से तुरंत लिस्बन भेजा गया, जिसके बाद बेड़ा भारत के लिए आगे बढ़ा।</p>"
      },
      {
        "title": "2. हिंद महासागर में यात्रा और कालीकट आगमन",
        "content": "<p>मई 1500 में, कैब्राल के शेष 12 जहाज ब्राजील से विदा होकर अफ्रीका की ओर बढ़े। <strong>केप ऑफ गुड होप</strong> के पास बेड़े को एक विनाशकारी समुद्री तूफान का सामना करना पड़ा। इस तूफान में बार्टोलोम्यू डियास के जहाज सहित 4 जहाज डूब गए और सभी नाविक मारे गए। डियास वही खोजकर्ता थे जिन्होंने 1488 में पहली बार केप मार्ग की खोज की थी। बार्टोलोम्यू के भाई डिओगो डियास का जहाज भी इस तूफान के दौरान मुख्य बेड़े से अलग हो गया और बहुत पूर्व की ओर चला गया, जिससे उन्होंने <strong>मेडागास्कर</strong> द्वीप की खोज की, जिसका नाम उन्होंने <em>साओ लॉरेंको</em> रखा।</p><p>शेष जहाज पूर्वी अफ्रीका के स्वाहिली तट पर एकत्र हुए। उन्होंने सोने के व्यापार की खोज के लिए <strong>सोफाला</strong> का दौरा किया, शत्रुतापूर्ण मोम्बासा को छोड़ दिया और <strong>मालिंदी</strong> के सुल्तान के साथ एक वफादार गठबंधन किया। मालिंदी के सुल्तान ने पुर्तगालियों को एक कुशल गुजराती/अरब पायलट प्रदान किया, जिसने दक्षिण-पश्चिमी ग्रीष्मकालीन मानसून हवाओं का उपयोग करके बेड़े को अरब सागर पार करवाया। <strong>13 सितंबर 1500</strong> को कैब्राल का शेष बेड़ा कालीकट पहुंचा। कालीकट के हिंदू राजा <strong>ज़मोरिन (सामुदिरी)</strong> ने कैब्राल का गर्मजोशी से स्वागत किया और उन्हें एक व्यापारिक फैक्ट्री (गोदाम) स्थापित करने की अनुमति दी।</p>"
      },
      {
        "title": "3. ऐरेस कोरिया और कालीकट फैक्ट्री नरसंहार",
        "content": "<p>ज़मोरिन के साथ हुई संधि के अनुसार, पुर्तगालियों ने कालीकट में मसाले खरीदने और संग्रहीत करने के लिए एक गोदाम स्थापित किया, जिसे <strong>feitoria</strong> (फैक्ट्री) कहा गया। इसका प्रबंधन मुख्य प्रतिनिधि <strong>ऐरेस कोरिया</strong> को सौंपा गया। इसका उद्देश्य सीधे स्थानीय उत्पादकों से काली मिर्च और अदरक खरीदना था। हालांकि, पुर्तगाल क्राउन का यह सीधा व्यापार सदियों से कालीकट के मसाला निर्यात पर नियंत्रण रखने वाले अरब और मुस्लिम व्यापारियों के एकाधिकार के खिलाफ था।</p><p>अरब व्यापारियों ने जानबूझकर काली मिर्च की कीमतों को बढ़ाया और जमाखोरी की, जिससे पुर्तगाली जहाजों को लोडिंग में भारी देरी होने लगी। तनाव तब बढ़ गया जब ज़मोरिन ने पुर्तगालियों को मसाले छिपाने के संदेह में अरब जहाजों की तलाशी लेने का अधिकार दे दिया। दिसंबर 1500 में, अरब व्यापारियों द्वारा भड़काई गई एक बड़ी भीड़ ने पुर्तगाली फैक्ट्री पर हमला कर दिया। इस हमले में मुख्य प्रतिनिधि ऐरेस कोरिया, तीन फ्रांसिस्कन मिशनरी और लगभग 50 पुर्तगाली मारे गए तथा गोदाम को नष्ट कर दिया गया। इसके जवाब में कैब्राल ने बंदरगाह में खड़े 10 अरब जहाजों को जब्त कर लिया, उनके मसाले के कार्गो को छीन लिया, उनके नाविकों (~600 पुरुष) को मार डाला और कालीकट शहर पर 24 घंटे तक तोपों से भीषण बमबारी की। इस हमले में लगभग 600 नागरिक मारे गए और बंदरगाह पूरी तरह तबाह हो गया।</p>"
      },
      {
        "title": "4. कोचीन और कन्नूर के साथ गठबंधन",
        "content": "<p>कालीकट से हटने के बाद, कैब्राल ने मालाबार तट की स्थानीय राजनीतिक प्रतिद्वंद्विता का चतुर उपयोग किया। वे दक्षिण में <strong>कोचीन (कोच्चि)</strong> पहुंचे, जिसके राजा <strong>उन्नी गोदा वर्मा</strong> (त्रिम्मुम्पारा राजा) कालीकट के ज़मोरिन के एक जागीरदार थे और अपनी स्वतंत्रता के लिए पुर्तगाली तोपों का सहयोग चाहते थे। राजा ने पुर्तगालियों के साथ एक व्यापारिक संधि पर हस्ताक्षर किए, उन्हें वहां फैक्ट्री बनाने की अनुमति दी और जहाजों पर तेजी से काली मिर्च और अदरक लोड करवाया। कैब्राल ने <strong>गोन्सालो गिल बारबोसा</strong> को एक छोटे दस्ते के साथ कोचीन फैक्ट्री के प्रभारी के रूप में पीछे छोड़ दिया।</p><p>कैब्राल ने उत्तर में <strong>कन्नूर</strong> के कोलाथिरी राजा के साथ भी मैत्रीपूर्ण संबंध स्थापित किए और मसाले लोड किए। जनवरी 1501 में, ज़मोरिन ने पुर्तगालियों को नष्ट करने के लिए 80 जहाजों का एक विशाल युद्ध बेड़ा भेजा। खतरे की सूचना मिलते ही कैब्राल अपने जहाजों के साथ वहां से निकल गए, लेकिन उन्होंने अपने प्रतिनिधियों को कोचीन के राजा के संरक्षण में ही छोड़ दिया। कोचीन के राजा ने ज़मोरिन के भारी दबाव के बावजूद पुर्तगालियों को सौंपने से इनकार कर दिया। इस गठबंधन ने कोचीन को भारत में पुर्तगालियों का पहला स्थायी मुख्यालय बनाने का मार्ग प्रशस्त किया।</p>"
      },
      {
        "title": "5. लिस्बन वापसी और भू-राजनीतिक विरासत",
        "content": "<p>कैब्राल का बेड़ा हिंद महासागर को पार करके और केप ऑफ गुड होप का चक्कर लगाकर <strong>जुलाई 1501 ईस्वी</strong> में लिस्बन लौटा। मार्च 1500 में रवाना हुए 13 जहाजों में से केवल 6 जहाज ही सुरक्षित वापस आ पाए थे। हालांकि, 7 जहाजों और सैकड़ों नाविकों के भारी नुकसान के बावजूद, बचे हुए जहाजों द्वारा लाया गया मसाला कार्गो इतना समृद्ध था कि उसने पूरी यात्रा और नष्ट हुए जहाजों की लागत को कवर करके शाही खजाने को भारी मुनाफा दिया।</p><p>इस यात्रा ने केप मार्ग की भारी व्यावसायिक व्यवहार्यता को साबित कर दिया। लिस्बन में मसाला व्यापार पर नियंत्रण के लिए <strong>कासा दा इंडिया</strong> विभाग का विस्तार किया गया और वार्षिक बेड़े की प्रणाली को <strong>कैरियर दा इंडिया</strong> के रूप में संस्थागत बनाया गया। भू-राजनीतिक रूप से, इस व्यापार मार्ग के कारण मिस्र के <strong>ममलुक सल्तनत</strong> को भारी कर राजस्व का नुकसान हुआ, जिससे वह कमजोर हो गया और 1517 में ऑटोमन्स ने उस पर विजय प्राप्त कर ली। यूरोप में वेनिस के मसाला एकाधिकार का भी पतन हो गया। सफलता के बावजूद, 1502 की अगली यात्रा की कमान संरचना पर विवाद और भारी जहाजों के नुकसान से राजा मैनुअल प्रथम अप्रसन्न थे, जिसके कारण उन्होंने कमान वास्को डी गामा को दे दी। कैब्राल <strong>संतरम</strong> में अपनी जागीर में सेवानिवृत्त हो गए, जहां 1520 में उनका निधन हो गया।</p>"
      }
    ]
  }
}

# Merge Mastery Zones
en_data['deepDive']['sections'][0]['masteryZone'] = section1_en
en_data['deepDive']['sections'][1]['masteryZone'] = section2_en
en_data['deepDive']['sections'][2]['masteryZone'] = section3_en
en_data['deepDive']['sections'][3]['masteryZone'] = section4_en
en_data['deepDive']['sections'][4]['masteryZone'] = section5_en

en_data['practiceQuestions'] = practice_en
en_data['mockTestQuestions'] = mock_en

# Ensure labels object exists
if 'labels' not in en_data:
    en_data['labels'] = {}
if 'tabs' not in en_data['labels']:
    en_data['labels']['tabs'] = {}
if 'practiceZoneHeader' not in en_data['labels']:
    en_data['labels']['practiceZoneHeader'] = {}
if 'mockIntro' not in en_data['labels']:
    en_data['labels']['mockIntro'] = {}
if 'mockPlay' not in en_data['labels']:
    en_data['labels']['mockPlay'] = {
        "prevBtn": "Previous",
        "nextBtn": "Next",
        "submitBtn": "Submit Test"
    }

en_data['labels']['tabs']['practice'] = "2. Practice Zone (50 Qs)"
en_data['labels']['practiceZoneHeader']['title'] = "Practice Zone: 50 Questions"
en_data['labels']['mockIntro']['title'] = "UPSC Prelims Mock Exam"
en_data['labels']['mockIntro']['description'] = "Contains 10 multi-statement questions testing conceptual understanding of Pedro Álvares Cabral's voyages, Brazil discovery, conflicts, and geopolitical impact. 1/3 negative marking applies."
en_data['labels']['mockIntro']['startBtn'] = "Start Mock Exam"
en_data['labels']['clickToExpand'] = "Click to Expand"

# Save English content.json
with open('content.json', 'w', encoding='utf-8') as f:
    json.dump(en_data, f, ensure_ascii=False, indent=2)

# Merge Hindi Mastery Zones
hi_data['deepDive']['sections'][0]['masteryZone'] = section1_hi
hi_data['deepDive']['sections'][1]['masteryZone'] = section2_hi
hi_data['deepDive']['sections'][2]['masteryZone'] = section3_hi
hi_data['deepDive']['sections'][3]['masteryZone'] = section4_hi
hi_data['deepDive']['sections'][4]['masteryZone'] = section5_hi

hi_data['practiceQuestions'] = practice_hi
hi_data['mockTestQuestions'] = mock_hi

# Ensure labels object exists
if 'labels' not in hi_data:
    hi_data['labels'] = {}
if 'tabs' not in hi_data['labels']:
    hi_data['labels']['tabs'] = {}
if 'practiceZoneHeader' not in hi_data['labels']:
    hi_data['labels']['practiceZoneHeader'] = {}
if 'mockIntro' not in hi_data['labels']:
    hi_data['labels']['mockIntro'] = {}
if 'mockPlay' not in hi_data['labels']:
    hi_data['labels']['mockPlay'] = {
        "prevBtn": "पिछला",
        "nextBtn": "अगला",
        "submitBtn": "टेस्ट सबमिट करें"
    }

hi_data['labels']['tabs']['practice'] = "2. अभ्यास क्षेत्र (50 प्रश्न)"
hi_data['labels']['practiceZoneHeader']['title'] = "अभ्यास क्षेत्र: 50 प्रश्न"
hi_data['labels']['mockIntro']['title'] = "यूपीएससी प्रीलिम्स मॉक परीक्षा"
hi_data['labels']['mockIntro']['description'] = "पेड्रो अल्वारेज़ कैब्राल की यात्रा, ब्राजील की खोज, संघर्ष और उनके भू-राजनीतिक प्रभाव की वैचारिक समझ का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।"
hi_data['labels']['mockIntro']['startBtn'] = "मॉक टेस्ट शुरू करें"
hi_data['labels']['clickToExpand'] = "विस्तार करने के लिए क्लिक करें"

# Save Hindi content.json
with open('hi/content.json', 'w', encoding='utf-8') as f:
    json.dump(hi_data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Merged and compiled all Cabral sections, practice, and mock questions into English and Hindi content.json.")
