#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) Hindi Language & Literature
 * Complete Hindi Language Content Generation Engine
 * Pointwise Concept Notes, Memory Mnemonics, Tips, Tricks, Mindmap, Tables & 10 MCQs
 *
 * Subject: Hindi Language & Literature (90 Questions | 270 Marks | -1 Negative Marking)
 * Covers all 34 directories in up-upper-primary-teacher/hindi/
 *
 * Uses common CSS: /assets/css/up-upper-primary-topic.min.css?v=20261006_04
 * Uses common JS:  /assets/js/up-upper-primary-topic.min.js
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import { compactUpUpperPrimaryModuleLabel } from './lib/up-upper-primary-heading.mjs';
import { upUpperPrimaryHeadThemeBootstrap, upUpperPrimaryBodyThemeBootstrap } from './lib/up-upper-primary-theme-bootstrap.mjs';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-hindi.json');
const OUTPUT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'hindi');

// 1. API Configuration & Key Rotation
const KEY_CONFIGS = [
  { key: process.env.GEMINI_API_KEY_1, name: 'KEY_1', models: ['gemini-3.5-flash-lite', 'gemini-2.5-flash'] },
  { key: process.env.GEMINI_API_KEY_2, name: 'KEY_2', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash'] },
  { key: process.env.GEMINI_API_KEY,   name: 'KEY_3', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash'] }
].filter(c => Boolean(c.key));

if (KEY_CONFIGS.length === 0) {
  console.error('ERROR: No valid GEMINI_API_KEY found in environment.');
  process.exit(1);
}

let keyIndex = 0;
function getActiveConfig() {
  return KEY_CONFIGS[keyIndex % KEY_CONFIGS.length];
}

function rotateKey() {
  keyIndex++;
  const next = getActiveConfig();
  console.log(`  [Key Rotation] Rotating to next API key (${next.name})...`);
}

// 2. Command Line Arguments
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const ALL = args.includes('--all');
const LIMIT = (() => {
  const idx = args.indexOf('--limit');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : null;
})();
const TARGET_SLUG = (() => {
  const idx = args.indexOf('--topic');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : null;
})();
const MODEL_NAME = (() => {
  const idx = args.indexOf('--model');
  return idx !== -1 && args[idx + 1] ? args[idx + 1] : 'gemini-2.5-flash';
})();
const CONCURRENCY = (() => {
  const idx = args.indexOf('--concurrency');
  return idx !== -1 && args[idx + 1] ? parseInt(args[idx + 1], 10) : 3;
})();

// 3. Status Tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch {
    statusMap = {};
  }
}
function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 4. Topic Directory Manifest (All 34 Topics)
export const HINDI_TOPICS = [
  // Section 1: Literature History (1.1 - 1.6)
  {
    slug: 'aadikaal',
    numStr: '#1.1',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'आदिकाल (वीरगाथा काल) — रासो काव्य परंपरा, सिद्ध-नाथ साहित्य, प्रवृत्तियां व प्रमुख रचनाएं',
    shortTitle: 'आदिकाल (वीरगाथा काल)',
    chkId: 'chk-hindi-1-1',
    coreFocus: 'अपभ्रंश एवं देशभाषा काव्य, पृथ्वीराज रासो (चंदबरदाई), बीसलदेव रासो, सरहपा, गोरखनाथ, अमीर खुसरो, विद्यापति एवं चारण काव्य परंपरा।'
  },
  {
    slug: 'bhaktikaal-nirgun-dhara',
    numStr: '#1.2',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'भक्तिकाल (निर्गुण काव्य धारा) — ज्ञानाश्रयी शाखा (संत कबीर) एवं प्रेमाश्रयी शाखा (मलिक मोहम्मद जायसी)',
    shortTitle: 'भक्तिकाल: निर्गुण काव्य धारा',
    chkId: 'chk-hindi-1-2',
    coreFocus: 'ज्ञानाश्रयी शाखा: कबीरदास (बीजक: साखी, सबद, रमैनी), रैदास, नानक। प्रेमाश्रयी (सूफी) शाखा: जायसी (पद्मावत, अखरावट), कुतुबन, मंझन।'
  },
  {
    slug: 'bhaktikaal-sagun-dhara',
    numStr: '#1.3',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'भक्तिकाल (सगुण काव्य धारा) — कृष्ण भक्ति शाखा (सूरदास, मीराबाई) एवं राम भक्ति शाखा (तुलसीदास)',
    shortTitle: 'भक्तिकाल: सगुण काव्य धारा',
    chkId: 'chk-hindi-1-3',
    coreFocus: 'रामभक्ति शाखा: गोस्वामी तुलसीदास (रामचरितमानस, विनयपत्रिका, कवितावली)। कृष्णभक्ति शाखा: अष्टछाप कवि, सूरदास (सूरसागर, साहित्य लहरी), मीराबाई, रसखान।'
  },
  {
    slug: 'reetikaal',
    numStr: '#1.4',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'रीतिकाल — रीतिबद्ध (केशवदास, चिंतामणि), रीतिसिद्ध (बिहारी) एवं रीतिमुक्त (घनानंद) काव्य',
    shortTitle: 'रीतिकाल: रीतिबद्ध, सिद्ध व मुक्त',
    chkId: 'chk-hindi-1-4',
    coreFocus: 'रीतिकाल की प्रमुख प्रवृत्तियां (शृंगारिकता, लक्षण-ग्रंथ), रीतिबद्ध: केशवदास (कविप्रिया), चिंतामणि; रीतिसिद्ध: बिहारी (बिहारी सतसई); रीतिमुक्त: घनानंद, बोधा, आलम, ठाकुर।'
  },
  {
    slug: 'aadhunik-kaal-bharatendu-dwivedi',
    numStr: '#1.5',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'आधुनिक काल (प्रथम चरण) — भारतेन्दु युग (गद्य का सूत्रपात) एवं द्विवेदी युग (खड़ी बोली आंदोलन)',
    shortTitle: 'आधुनिक काल: भारतेन्दु व द्विवेदी युग',
    chkId: 'chk-hindi-1-5',
    coreFocus: 'भारतेन्दु हरिश्चंद्र, नागरी प्रचारिणी सभा, महावीर प्रसाद द्विवेदी एवं सरस्वती पत्रिका (1903), मैथिलीशरण गुप्त (साकेत), अयोध्यासिंह उपाध्याय हरिऔध (प्रियप्रवास)।'
  },
  {
    slug: 'chhayavad-pragativad-prayogvad',
    numStr: '#1.6',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'आधुनिक काल (द्वितीय चरण) — छायावाद (प्रसाद, निराला, पन्त, महादेवी), प्रगतिवाद एवं प्रयोगवाद',
    shortTitle: 'छायावाद, प्रगतिवाद, प्रयोगवाद व नई कविता',
    chkId: 'chk-hindi-1-6',
    coreFocus: 'छायावाद की प्रवृत्तियां, प्रगतिशील लेखक संघ (1936), नागार्जुन, केदारनाथ अग्रवाल; प्रयोगवाद: अज्ञेय (तार सप्तक 1943), गजानन माधव मुक्तिबोध, नई कविता एवं समकालीन काव्य।'
  },

  // Section 2: Authors & Masterpieces (2.1 - 2.6)
  {
    slug: 'kavi-bhakti-reetikaal',
    numStr: '#2.1',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'भक्ति एवं रीतिकाल के प्रमुख कवि — कबीर (बीजक), सूरदास, तुलसीदास (रामचरितमानस), जायसी व बिहारी',
    shortTitle: 'भक्ति एवं रीतिकाल के प्रमुख कवि',
    chkId: 'chk-hindi-2-1',
    coreFocus: 'कबीर (बीजक, रहस्यवाद), सूरदास (वात्सल्य सम्राट), तुलसीदास (समन्वय की चेष्टा, 12 प्रामाणिक ग्रंथ), जायसी (मसनवी शैली), बिहारीलाल (गागर में सागर)।'
  },
  {
    slug: 'sahityakar-dwivedi-yug',
    numStr: '#2.2',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'द्विवेदी युग के प्रमुख साहित्यकार — महावीर प्रसाद द्विवेदी, मैथिलीशरण गुप्त (साकेत, भारत-भारती) व हरिऔध',
    shortTitle: 'द्विवेदी युग के प्रमुख साहित्यकार',
    chkId: 'chk-hindi-2-2',
    coreFocus: 'आचार्य महावीर प्रसाद द्विवेदी (भाषा संस्कार), राष्ट्रकवि मैथिलीशरण गुप्त (साकेत, यशोधरा, भारत-भारती), अयोध्यासिंह उपाध्याय हरिऔध (प्रियप्रवास, वैदेही वनवास)।'
  },
  {
    slug: 'chhayavad-char-stambh',
    numStr: '#2.3',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'छायावाद के चार स्तम्भ — जयशंकर प्रसाद (कामायनी), निराला (राम की शक्तिपूजा), पन्त व महादेवी वर्मा',
    shortTitle: 'छायावाद के चार स्तम्भ',
    chkId: 'chk-hindi-2-3',
    coreFocus: 'जयशंकर प्रसाद (कामायनी, चंद्रगुप्त), सूर्यकांत त्रिपाठी निराला (सरोज स्मृति, राम की शक्तिपूजा), सुमित्रानंदन पन्त (प्रकृति के सुकुमार कवि, चिदम्बरा), महादेवी वर्मा (यामा, नीहार)।'
  },
  {
    slug: 'munshi-premchand-works',
    numStr: '#2.4',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'उपन्यास सम्राट मुंशी प्रेमचंद — गोदान, गबन, सेवासदन, रंगभूमि, मानसरोवर कहानियां व यथार्थवाद',
    shortTitle: 'उपन्यास सम्राट मुंशी प्रेमचंद',
    chkId: 'chk-hindi-2-4',
    coreFocus: 'मुंशी प्रेमचंद: जीवन परिचय, उपन्यास (गोदान, गबन, निर्मला, रंगभूमि), मानसरोवर (कफन, पूस की रात, पंच परमेश्वर, ईदगाह) एवं आदर्शोन्मुख यथार्थवाद।'
  },
  {
    slug: 'kavi-dinkar-bachchan-agyeya',
    numStr: '#2.5',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'आधुनिक राष्ट्रकवि एवं नवलेखन — रामधारी सिंह दिनकर (उर्वशी, रश्मिरथी), हरिवंश राय बच्चन व अज्ञेय',
    shortTitle: 'दिनकर, बच्चन, अज्ञेय व नवलेखन',
    chkId: 'chk-hindi-2-5',
    coreFocus: 'रामधारी सिंह दिनकर (ओज व पौरुष, कुरुक्षेत्र, रश्मिरथी, उर्वशी), हरिवंश राय बच्चन (हालावाद, मधुशाला, क्या भूलूँ क्या याद करूँ), सच्चिदानंद हीरानंद वात्स्यायन अज्ञेय (आंगन के पार द्वार)।'
  },
  {
    slug: 'hindi-gadya-shukla-dwivedi',
    numStr: '#2.6',
    secIdx: 2,
    secTitle: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां',
    title: 'हिन्दी गद्य, निबन्ध एवं आलोचना — आचार्य रामचंद्र शुक्ल (चिंतामणि), हजारी प्रसाद द्विवेदी व भारती',
    shortTitle: 'हिन्दी गद्य, निबन्ध एवं आलोचना',
    chkId: 'chk-hindi-2-6',
    coreFocus: 'आचार्य रामचंद्र शुक्ल (हिन्दी साहित्य का इतिहास, चिंतामणि भाग 1-2, मनोविकार सम्बन्धी निबन्ध), आचार्य हजारी प्रसाद द्विवेदी (बाणभट्ट की आत्मकथा, अशोक के फूल), धर्मवीर भारती (अंधा युग)।'
  },

  // Section 3: Hindi Grammar (3.1 - 3.12)
  {
    slug: 'varnamala',
    numStr: '#3.1',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'हिन्दी वर्णमाला — स्वर, व्यञ्जन, उच्चारण स्थान, अल्पप्राण-महाप्राण एवं अघोष-सघोष वर्ण',
    shortTitle: 'वर्णमाला एवं उच्चारण स्थान',
    chkId: 'chk-hindi-3-1',
    coreFocus: 'स्वर (ह्रस्व, दीर्घ, प्लुत), व्यञ्जन (स्पर्श, अंतःस्थ, ऊष्म, संयुक्त), अल्पप्राण-महाप्राण, घोष-अघोष, कंठ्य, तालव्य, मूर्धन्य, दन्त्य, ओष्ठ्य उच्चारण स्थान तालिका।'
  },
  {
    slug: 'sandhi-swar',
    numStr: '#3.2',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'स्वर सन्धि (५ भेद) — दीर्घ, गुण, वृद्धि, यण् एवं अयादि सन्धि के नियम व विच्छेद',
    shortTitle: 'स्वर सन्धि (५ भेद)',
    chkId: 'chk-hindi-3-2',
    coreFocus: 'दीर्घ सन्धि (अकः सवर्णे दीर्घः), गुण सन्धि (आद्गुणः), वृद्धि सन्धि (वृद्धिरेचि), यण् सन्धि (इको यणचि), अयादि सन्धि (एचोऽयवायावः), पहचान के अचूक सूत्र व उदाहरण।'
  },
  {
    slug: 'sandhi-vyanjan-visarga',
    numStr: '#3.3',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'व्यञ्जन सन्धि एवं विसर्ग सन्धि — प्रमुख परिवर्तन नियम, अपवाद एवं सन्धि विच्छेद',
    shortTitle: 'व्यञ्जन एवं विसर्ग सन्धि',
    chkId: 'chk-hindi-3-3',
    coreFocus: 'व्यञ्जन सन्धि के प्रमुख नियम (प्रथम वर्ण का तृतीय वर्ण में परिवर्तन, अनुनासिक परिवर्तन, त् सम्बन्धी नियम), विसर्ग सन्धि (विसर्ग का ओ, र्, श्, ष्, स् में परिवर्तन व लोप)।'
  },
  {
    slug: 'samas',
    numStr: '#3.4',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'समास प्रकरणम् — अव्ययीभाव, तत्पुरुष, कर्मधारय, द्विगु, द्वन्द्व एवं बहुव्रीहि समास विग्रह',
    shortTitle: 'समास प्रकरणम् (६ भेद)',
    chkId: 'chk-hindi-3-4',
    coreFocus: 'समास के ६ भेद: अव्ययीभाव (पूर्वपद प्रधान), तत्पुरुष (उत्तरपद प्रधान व कारक भेद), कर्मधारय (विशेषण-विशेष्य), द्विगु (संख्यावाची पूर्वपद), द्वन्द्व (उभयपद प्रधान), बहुव्रीहि (अन्यपद प्रधान)।'
  },
  {
    slug: 'shabd-bhed-vikari',
    numStr: '#3.5',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'विकारी शब्द — संज्ञा (५ भेद), सर्वनाम (६ भेद), विशेषण (४ भेद) एवं क्रिया (सकर्मक-अकर्मक)',
    shortTitle: 'विकारी शब्द (संज्ञा, सर्वनाम, विशेषण, क्रिया)',
    chkId: 'chk-hindi-3-5',
    coreFocus: 'संज्ञा (व्यक्ति, जाति, भाव, समूह, द्रव्य), सर्वनाम (पुरुष, निश्चय, अनिश्चय, संबंध, प्रश्न, निज), विशेषण (गुण, संख्या, परिमाण, सार्वनामिक), क्रिया (सकर्मक, अकर्मक, प्रेरणार्थक, द्विकर्मक)।'
  },
  {
    slug: 'shabd-bhed-avikari',
    numStr: '#3.6',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'अविकारी शब्द (अव्यय) — क्रिया-विशेषण, संबंधबोधक, समुच्चयबोधक एवं विस्मयादिबोधक',
    shortTitle: 'अविकारी शब्द (अव्यय)',
    chkId: 'chk-hindi-3-6',
    coreFocus: 'क्रियाविशेषण (स्थान, काल, रीति, परिमाणवाचक), संबंधबोधक अव्यय, समुच्चयबोधक (समानाधिकरण, व्यधिकरण), विस्मयादिबोधक, निपात (ही, भी, तो, मात्र) का सूक्ष्म प्रयोग।'
  },
  {
    slug: 'karak',
    numStr: '#3.7',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'कारक एवं विभक्ति चिह्न — ८ कारक (कर्ता से संबोधन तक), परसर्ग एवं सटीक प्रयोग',
    shortTitle: 'कारक एवं विभक्ति चिह्न',
    chkId: 'chk-hindi-3-7',
    coreFocus: '८ कारक: कर्ता (ने), कर्म (को), करण (से/द्वारा), संप्रदान (को/के लिए), अपादान (से पृथक्), संबंध (का/की/के), अधिकरण (में/पर), संबोधन (हे/अरे) एवं परसर्ग रहित प्रयोग।'
  },
  {
    slug: 'upsarg-pratyay',
    numStr: '#3.8',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'उपसर्ग एवं प्रत्यय — संस्कृत, हिन्दी व आगत उपसर्ग, कृत् व तद्धित प्रत्यय तथा शब्द निर्माण',
    shortTitle: 'उपसर्ग एवं प्रत्यय',
    chkId: 'chk-hindi-3-8',
    coreFocus: 'उपसर्ग के भेद (संस्कृत के २२ उपसर्ग, हिन्दी उपसर्ग, उर्दू-फ़ारसी उपसर्ग), प्रत्यय के भेद (कृदन्त/कृत् प्रत्यय — क्रिया मूल, तद्धित प्रत्यय — संज्ञा/सर्वनाम मूल), शब्द रचना के नियम।'
  },
  {
    slug: 'vakya-bhed',
    numStr: '#3.9',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'वाक्य रचना एवं वाक्य शुद्धि — सरल, संयुक्त व मिश्र वाक्य तथा लिंग-वचन-कारक संबंधी अशुद्धियां',
    shortTitle: 'वाक्य रचना एवं वाक्य शुद्धि',
    chkId: 'chk-hindi-3-9',
    coreFocus: 'रचना के आधार पर वाक्य भेद (सरल, संयुक्त, मिश्र — प्रधान व आश्रित उपवाक्य), अर्थ के आधार पर ८ भेद, वाक्य शुद्धि (लिंग, वचन, कारक, पदक्रम, पुनरुक्ति दोष निवारण)।'
  },
  {
    slug: 'muhavare',
    numStr: '#3.10',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'मुहावरे एवं लोकोक्तियाँ — लोकप्रिय कहावतें, विशिष्ट लाक्षणिक अर्थ एवं परीक्षा उपयोगी प्रयोग',
    shortTitle: 'मुहावरे एवं लोकोक्तियाँ',
    chkId: 'chk-hindi-3-10',
    coreFocus: 'मुहावरा (वाक्यांश, लाक्षणिक अर्थ) एवं लोकोक्ति (पूर्ण वाक्य, सामाजिक अनुभव) में अंतर, परीक्षा में बार-बार पूछे जाने वाले ५०+ अतिमहत्वपूर्ण मुहावरे व लोकोक्तियां।'
  },
  {
    slug: 'shabd-bhandar',
    numStr: '#3.11',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'शब्द भण्डार — विलोम, पर्यायवाची, अनेकार्थी, वाक्यांश के लिए एक शब्द, तत्सम-तद्भव',
    shortTitle: 'शब्द भण्डार (तत्सम, पर्यायवाची, विलोम)',
    chkId: 'chk-hindi-3-11',
    coreFocus: 'उत्पत्ति के आधार पर (तत्सम, तद्भव, देशज, विदेशज, संकर), अर्थ के आधार पर (पर्यायवाची, विलोम, समश्रुत भिन्नार्थक, अनेकार्थी, वाक्यांश के लिए एक शब्द)।'
  },
  {
    slug: 'ras-chhand-alankar',
    numStr: '#3.12',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'काव्यशास्त्र — रस (स्थायी भाव व ९ रस), छन्द (दोहा, चौपाई, सोरठा) एवं अलंकार (शब्द व अर्थ)',
    shortTitle: 'काव्यशास्त्र: रस, छन्द एवं अलंकार',
    chkId: 'chk-hindi-3-12',
    coreFocus: 'रस के ४ अंग (स्थायी भाव, विभाव, अनुभाव, संचारी भाव), ९ रस + वात्सल्य/भक्ति; छन्द: मात्रिक छन्द (दोहा, सोरठा, चौपाई, रोला, कुण्डलिया); अलंकार: शब्दालंकार (अनुप्रास, यमक, श्लेष), अर्थालंकार (उपमा, रूपक, उत्प्रेक्षा, अतिशयोक्ति, भ्रान्तिमान)।'
  },

  // Section 4: Comprehension (4.1 - 4.2)
  {
    slug: 'hindi-apatit-gadyansh',
    numStr: '#4.1',
    secIdx: 4,
    secTitle: 'अपठित बोध',
    title: 'अपठित गद्यांश — गद्यांश बोध, केंद्रीय विचार, शीर्षक निर्धारण एवं व्याकरण आधारित प्रश्नोत्तर',
    shortTitle: 'अपठित गद्यांश बोध',
    chkId: 'chk-hindi-4-1',
    coreFocus: 'अपठित गद्यांश को हल करने की वैज्ञानिक तकनीक, मूल भाव ग्रहण, सटीक शीर्षक चयन, रेखांकित अंशों की व्याख्या, गद्यांश से व्याकरण आधारित प्रश्नों (सन्धि, समास, प्रत्यय) का समाधान।'
  },
  {
    slug: 'hindi-apatit-padyansh',
    numStr: '#4.2',
    secIdx: 4,
    secTitle: 'अपठित बोध',
    title: 'अपठित पद्यांश — काव्यांश भाव-सौंदर्य, शिल्प-सौंदर्य, रस, छन्द, अलंकार एवं काव्य बोध प्रश्नोत्तर',
    shortTitle: 'अपठित पद्यांश एवं काव्यांश बोध',
    chkId: 'chk-hindi-4-2',
    coreFocus: 'काव्यांश का भाव-सौंदर्य (केंद्रीय भाव, संवेदना, रस निष्पत्ति), शिल्प-सौंदर्य (भाषा, छन्द, अलंकार, शब्द-शक्ति), काव्यांश पर आधारित सटीक वस्तुनिष्ठ प्रश्नों का समाधान।'
  },

  // 8 Master Combined / Parent Topics
  {
    slug: 'aadhunik-kaal',
    numStr: '#Master-1',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'आधुनिक काल समग्र — भारतेन्दु युग, द्विवेदी युग, छायावाद, प्रगतिवाद, प्रयोगवाद एवं नई कविता',
    shortTitle: 'आधुनिक काल सम्पूर्ण महा-अध्याय',
    chkId: 'chk-hindi-m1',
    coreFocus: 'आधुनिक काल का सम्पूर्ण कालक्रम (1850 से अद्यतन), गद्य का विकास, खड़ी बोली काव्य आंदोलन, छायावाद के चार स्तम्भ, प्रगतिवाद, तार सप्तक एवं साठोत्तरी हिन्दी कविता।'
  },
  {
    slug: 'bhaktikaal',
    numStr: '#Master-2',
    secIdx: 1,
    secTitle: 'हिन्दी साहित्य का इतिहास एवं प्रमुख काल',
    title: 'भक्तिकाल समग्र (स्वर्णयुग) — निर्गुण एवं सगुण काव्य धारा, चारों प्रमुख शाखाएं व प्रतिनिधि कवि',
    shortTitle: 'भक्तिकाल सम्पूर्ण महा-अध्याय (स्वर्णयुग)',
    chkId: 'chk-hindi-m2',
    coreFocus: 'हिन्दी साहित्य का स्वर्ण युग (जॉर्ज ग्रियर्सन), निर्गुण धारा (ज्ञानाश्रयी — कबीर, प्रेमाश्रयी — जायसी) एवं सगुण धारा (रामभक्ति — तुलसीदास, कृष्णभक्ति — सूरदास, मीराबाई)।'
  },
  {
    slug: 'sandhi',
    numStr: '#Master-3',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'सन्धि प्रकरणम् समग्र — स्वर सन्धि, व्यञ्जन सन्धि एवं विसर्ग सन्धि के समस्त नियम व अपवाद',
    shortTitle: 'सन्धि प्रकरणम् सम्पूर्ण महा-अध्याय',
    chkId: 'chk-hindi-m3',
    coreFocus: 'दो समीपवर्ती वर्णों के मेल से होने वाला विकार, स्वर सन्धि (५ भेद), व्यञ्जन सन्धि (१२ प्रमुख परिवर्तन नियम) एवं विसर्ग सन्धि के अचूक पहचान सूत्र व अपवाद।'
  },
  {
    slug: 'shabd-bhed',
    numStr: '#Master-4',
    secIdx: 3,
    secTitle: 'हिन्दी व्याकरण समग्र',
    title: 'पद भेद समग्र — विकारी (संज्ञा, सर्वनाम, विशेषण, क्रिया) एवं अविकारी (अव्यय व निपात) शब्द विचार',
    shortTitle: 'पद भेद सम्पूर्ण महा-अध्याय (विकारी-अविकारी)',
    chkId: 'chk-hindi-m4',
    coreFocus: 'व्याकरणिक कोटियाँ एवं पद परिचय: संज्ञा, सर्वनाम, विशेषण, क्रिया, काल, वाच्य, लिंग, वचन, कारक तथा चारों अव्यय भेद एवं निपात का गहन व्यावहारिक विश्लेषण।'
  },
  {
    slug: 'apatit-gadyansh-padyansh',
    numStr: '#Master-5',
    secIdx: 4,
    secTitle: 'अपठित बोध',
    title: 'अपठित बोध समग्र — अपठित गद्यांश एवं पद्यांश विश्लेषण, भाव-शिल्प सौंदर्य एवं हल करने की रणनीतियां',
    shortTitle: 'अपठित बोध सम्पूर्ण महा-अध्याय (गद्य-पद्य)',
    chkId: 'chk-hindi-m5',
    coreFocus: 'गद्यांश एवं पद्यांश पर आधारित प्रश्नों को हल करने का टाइम-मैनेजमेंट फॉर्मूला, शीर्षक चयन विधि, लाक्षणिक अर्थ ग्रहण, व्याकरणिक प्रश्नों का त्वरित समाधान।'
  },
  {
    slug: 'hindi-sahitya-itihas',
    numStr: '#Sec-1',
    secIdx: 1,
    secTitle: 'खण्ड 1 हब',
    title: 'हिन्दी साहित्य का इतिहास समग्र — काल विभाजन, नामकरण, प्रमुख प्रवृत्तियां एवं युग प्रवर्तक साहित्यकार',
    shortTitle: 'हिन्दी साहित्य का इतिहास सम्पूर्ण काल विभाजन',
    chkId: 'chk-hindi-sec1',
    coreFocus: 'आचार्य रामचंद्र शुक्ल, डॉ. रामकुमार वर्मा, हजारी प्रसाद द्विवेदी द्वारा काल विभाजन व नामकरण; आदिकाल, भक्तिकाल, रीतिकाल एवं आधुनिक काल की समग्र तुलना।'
  },
  {
    slug: 'pramukh-lekhak-kavi-kritiyan',
    numStr: '#Sec-2',
    secIdx: 2,
    secTitle: 'खण्ड 2 हब',
    title: 'प्रमुख लेखक, कवि एवं उनकी कालजयी कृतियां समग्र — प्राचीन से आधुनिक काल के शीर्ष रचनाकार व पुरस्कार',
    shortTitle: 'प्रमुख साहित्यकार, कृतियां एवं पुरस्कार',
    chkId: 'chk-hindi-sec2',
    coreFocus: 'कबीर, सूर, तुलसी, जायसी, बिहारी, भारतेन्दु, द्विवेदी, गुप्त, प्रसाद, निराला, पन्त, महादेवी, प्रेमचंद, दिनकर, अज्ञेय की प्रमुख रचनाएं, ज्ञानपीठ एवं साहित्य अकादमी पुरस्कार।'
  },
  {
    slug: 'hindi-vyakaran-samagra',
    numStr: '#Sec-3',
    secIdx: 3,
    secTitle: 'खण्ड 3 हब',
    title: 'हिन्दी व्याकरण समग्र — वर्ण विचार, शब्द रचना, पद भेद, वाक्य विचार एवं सम्पूर्ण काव्यशास्त्र',
    shortTitle: 'हिन्दी व्याकरण सम्पूर्ण महा-मार्गदर्शिका',
    chkId: 'chk-hindi-sec3',
    coreFocus: 'UP शिक्षक भर्ती के लिए सम्पूर्ण मानक व्याकरण: वर्णमाला, सन्धि, समास, कारक, उपसर्ग-प्रत्यय, वाक्य शुद्धि, शब्द भण्डार, मुहावरे तथा रस, छन्द, अलंकार का महा-संग्रह।'
  }
];

// 5. Prompt Builder (Pure High-Academic Hindi)
function buildHindiPrompt(topic) {
  return `आप उत्तर प्रदेश बेसिक शिक्षा परिषद (SCERT UP) एवं उच्च प्राथमिक शिक्षक भर्ती परीक्षा (Super TET Junior — Class 6-8 हिन्दी भाषा एवं साहित्य: 90 प्रश्न | 270 अंक | -1 नकारात्मक अंकन) के मुख्य पाठ्यक्रम विशेषज्ञ व वरिष्ठ प्रश्नपत्र निर्माता हैं।

इस विषय के लिए परीक्षार्थी को परीक्षा में शत-प्रतिशत अंक (Top Rank) दिलाने योग्य, अत्यंत उच्च स्तरीय, प्रामाणिक एवं विस्तृत अध्ययन सामग्री केवल और केवल शुद्ध हिन्दी भाषा (देवनागरी लिपि) में तैयार करें:

विषय विवरण:
- परीक्षा: UP Upper Primary Assistant Teacher Recruitment (Class 6-8) 2026
- विषय: हिन्दी भाषा एवं साहित्य (खण्ड ${topic.secIdx}: ${topic.secTitle})
- टॉपिक कोड: ${topic.numStr}
- टॉपिक शीर्षक: ${topic.title}
- मुख्य अध्ययन बिंदु: ${topic.coreFocus}

कड़े शैक्षणिक एवं संरचनात्मक नियम (अनिवार्य पालन):
1. पूर्णतः बिन्दुवार (STRICTLY POINTWISE ARCHITECTURE):
   - कोई लंबा या उबाऊ पैराग्राफ नहीं होना चाहिए।
   - प्रत्येक अवधारणा को <div class="point-grid"><div class="point-card"><strong>[प्रमुख पद / नियम / रचनाकार / सूत्र]:</strong> [गहन, प्रामाणिक, विस्तृत तथ्यात्मक विवरण]</div>...</div> में प्रस्तुत करें।
   - कक्षा 6-8 SCERT UP पाठ्यपुस्तकें ("मंजरी", "हिन्दी व्याकरण एवं रचना") एवं प्रामाणिक मानक ग्रन्थों (कामताप्रसाद गुरु, डॉ. वासुदेव नंदन प्रसाद, आचार्य रामचंद्र शुक्ल) पर आधारित तथ्य।

2. चार मुख्य संकल्पना भाग (4 Comprehensive Concepts):
   - भाग 1 (मूल अवधारणा, परिभाषाएं एवं मुख्य सिद्धांत):
     कम से कम 4-5 विस्तृत point-card + 1 <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>परीक्षा उपयोगी सूत्र (Pro-Tip):</strong> ...</div> + 1 <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>याद रखने का अचूक सूत्र (Mnemonic):</strong> <code>सूत्र</code> — विस्तार...</div>।
   - भाग 2 (वर्गीकरण, संरचना एवं सूक्ष्म नियम):
     1 तुलनात्मक उप-तालिका <div class="topic-subtable-wrapper"><table class="topic-subtable"><thead><tr><th>वर्गीकरण / भेद</th><th>पहचान व मुख्य नियम</th><th>परीक्षा उपयोगी सटीक उदाहरण</th></tr></thead><tbody><tr><td>...</td><td>...</td><td>...</td></tr></tbody></table></div> + 3-4 point-card + 1 <div class="trick-box"><i class="fas fa-bolt"></i> <strong>पहचानने की शॉर्टकट ट्रिक:</strong> ...</div>।
   - भाग 3 (उत्तर प्रदेश शिक्षक भर्ती विशिष्ट परिप्रेक्ष्य व उदाहरण):
     UP-TET / Super TET में बार-बार पूछे जाने वाले विशिष्ट उदाहरण, काव्य पंक्तियाँ, उत्तर प्रदेश के प्रमुख साहित्यकार / रचनाएं, क्षेत्रीय बोलियाँ + 1 <div class="tip-box"><i class="fas fa-lightbulb"></i> <strong>UP परीक्षा विशेष टिप:</strong> ...</div>।
   - भाग 4 (अपवाद, सूक्ष्म भेद एवं परीक्षार्थी भ्रम निवारण):
     समान दिखने वाले नियमों में अंतर, भ्रामक उदाहरण, अपवाद + 1 <div class="trick-box"><i class="fas fa-bolt"></i> <strong>भ्रम निवारण ट्रिक:</strong> ...</div> + 1 <div class="mnemonic-inline-box"><i class="fas fa-brain"></i> <strong>स्मरण सूत्र:</strong> <code>KEY</code> — ...</div>।

3. माइंडमैप संरचना (Mindmap Data):
   - एक मुख्य केंद्रीय नोड (central_node)
   - 4 से 5 मुख्य शाखाएं (branches), प्रत्येक शाखा में शीर्षक (title), आइकन (icon जैसे 'fas fa-book', 'fas fa-feather', 'fas fa-spell-check', 'fas fa-list-ol') और 3-4 संक्षिप्त उप-बिंदु (nodes) जो पूरे पाठ का विहंगम दृश्य प्रस्तुत करें।

4. विस्तृत तुलनात्मक तालिका (Comprehensive Comparative Table):
   - शीर्षक, 4 कॉलम हेडर्स, और कम से कम 4-5 पंक्तियाँ जो महत्वपूर्ण भेदों को स्पष्ट करें।

5. 10 उच्च-स्तरीय बहुविकल्पीय प्रश्न (10 Practice MCQs):
   - Super TET Junior के 270 अंकों के वास्तविक परीक्षा स्तर के प्रश्न।
   - 4 विकल्प (बिना A/B/C/D उपसर्ग के)।
   - सही विकल्प का 0-आधारित सूचकांक (correct_index: 0, 1, 2, या 3)।
   - विस्तृत व्याख्या (explanation) जिसमें सही उत्तर का कारण और अन्य विकल्पों के गलत होने का कारण स्पष्ट हो।

6. त्वरित पुनरीक्षण एवं परीक्षा जाल (Revision Vault):
   - revision_facts: 8 अतिमहत्वपूर्ण, परीक्षा-केंद्रित तीव्र पुनरीक्षण तथ्य।
   - mnemonics: 2 स्मरण सूत्र (title, acronym, expansion)।
   - exam_traps: 4 नकारात्मक अंकन जाल (-1 अंक काटने से बचाने वाली सावधानियां)।
   - checklist_items: 4 स्व-मूल्यांकन चेकलिस्ट बिंदु।

नीचे दिए गए JSON प्रारूप में ही उत्तर दें (RAW JSON ONLY, कोई अतिरिक्त मार्कडाउन या टेक्स्ट नहीं):
{
  "key_focus_summary": "इस अध्याय का 2-3 वाक्यों में सारगर्भित परीक्षा सारांश और अंक भार...",
  "mindmap": {
    "central_node": "अध्याय का केंद्रीय शीर्षक",
    "branches": [
      {
        "title": "प्रथम शाखा",
        "icon": "fas fa-book-open",
        "nodes": ["बिंदु 1", "बिंदु 2", "बिंदु 3"]
      },
      {
        "title": "द्वितीय शाखा",
        "icon": "fas fa-diagram-project",
        "nodes": ["बिंदु 1", "बिंदु 2", "बिंदु 3"]
      },
      {
        "title": "तृतीय शाखा",
        "icon": "fas fa-star",
        "nodes": ["बिंदु 1", "बिंदु 2", "बिंदु 3"]
      },
      {
        "title": "चतुर्थ शाखा",
        "icon": "fas fa-shield-halved",
        "nodes": ["बिंदु 1", "बिंदु 2", "बिंदु 3"]
      }
    ]
  },
  "concepts": [
    {
      "heading": "1. मूल अवधारणा, परिभाषाएं एवं मुख्य सिद्धांत",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>...:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>परीक्षा उपयोगी सूत्र:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>याद रखने का अचूक सूत्र:</strong> <code>...</code> — ...</div>"
    },
    {
      "heading": "2. वर्गीकरण, संरचना एवं सूक्ष्म नियम",
      "html_content": "<div class=\"topic-subtable-wrapper\"><table class=\"topic-subtable\"><thead><tr><th>वर्गीकरण / भेद</th><th>पहचान व मुख्य नियम</th><th>परीक्षा उपयोगी सटीक उदाहरण</th></tr></thead><tbody><tr><td><strong>...</strong></td><td>...</td><td>...</td></tr></tbody></table></div><div class=\"point-grid\"><div class=\"point-card\"><strong>...:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>पहचानने की शॉर्टकट ट्रिक:</strong> ...</div>"
    },
    {
      "heading": "3. उत्तर प्रदेश शिक्षक भर्ती विशिष्ट परिप्रेक्ष्य व उदाहरण",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>...:</strong> ...</div></div><div class=\"tip-box\"><i class=\"fas fa-lightbulb\"></i> <strong>UP परीक्षा विशेष टिप:</strong> ...</div>"
    },
    {
      "heading": "4. अपवाद, सूक्ष्म भेद एवं परीक्षार्थी भ्रम निवारण",
      "html_content": "<div class=\"point-grid\"><div class=\"point-card\"><strong>...:</strong> ...</div></div><div class=\"trick-box\"><i class=\"fas fa-bolt\"></i> <strong>भ्रम निवारण ट्रिक:</strong> ...</div><div class=\"mnemonic-inline-box\"><i class=\"fas fa-brain\"></i> <strong>स्मरण सूत्र:</strong> <code>...</code> — ...</div>"
    }
  ],
  "comparative_table": {
    "title": "तुलनात्मक विश्लेषण एवं मुख्य परीक्षा भेद",
    "headers": ["तुलना के आधार / बिन्दु", "वर्ग / रूप A", "वर्ग / रूप B", "परीक्षा हेतु महत्त्वपूर्ण तथ्य"],
    "rows": [
      ["बिन्दु 1", "विवरण A", "विवरण B", "महत्वपूर्ण निष्कर्ष"],
      ["बिन्दु 2", "विवरण A", "विवरण B", "महत्वपूर्ण निष्कर्ष"],
      ["बिन्दु 3", "विवरण A", "विवरण B", "महत्वपूर्ण निष्कर्ष"],
      ["बिन्दु 4", "विवरण A", "विवरण B", "महत्वपूर्ण निष्कर्ष"]
    ]
  },
  "mcqs": [
    {
      "question": "परीक्षा उपयोगी उच्च स्तरीय प्रश्न?",
      "options": ["पहला विकल्प", "दूसरा विकल्प", "तीसरा विकल्प", "चौथा विकल्प"],
      "correct_index": 0,
      "explanation": "विस्तृत व्याख्या जिसमें सही उत्तर की पुष्टि और अन्य विकल्पों का विश्लेषण हो।"
    }
  ],
  "revision_facts": [
    "तीव्र पुनरीक्षण तथ्य 1",
    "तीव्र पुनरीक्षण तथ्य 2",
    "तीव्र पुनरीक्षण तथ्य 3",
    "तीव्र पुनरीक्षण तथ्य 4",
    "तीव्र पुनरीक्षण तथ्य 5",
    "तीव्र पुनरीक्षण तथ्य 6",
    "तीव्र पुनरीक्षण तथ्य 7",
    "तीव्र पुनरीक्षण तथ्य 8"
  ],
  "mnemonics": [
    {
      "title": "पहला स्मरण सूत्र",
      "acronym": "सूत्र",
      "expansion": "विस्तार"
    },
    {
      "title": "दूसरा स्मरण सूत्र",
      "acronym": "ट्रिक",
      "expansion": "विस्तार"
    }
  ],
  "exam_traps": [
    "नकारात्मक अंकन जाल 1: ...",
    "नकारात्मक अंकन जाल 2: ...",
    "नकारात्मक अंकन जाल 3: ...",
    "नकारात्मक अंकन जाल 4: ..."
  ],
  "checklist_items": [
    "मूल परिभाषाएं, वर्गीकरण एवं प्रमुख सूत्र भली-भाँति कंठस्थ हैं।",
    "उत्तर प्रदेश शिक्षक भर्ती के विगत वर्षों में पूछे गए उदाहरण हल कर लिए हैं।",
    "सभी 10 अभ्यास प्रश्नों को विस्तृत व्याख्या सहित समझ लिया है।",
    "5 मिनट के समयबद्ध मिनी टेस्ट में 20+ अंक अर्जित कर लिए हैं।"
  ]
}`;
}

// 6. HTML Page Renderer (Using Common CSS & Common JS)
function renderHindiPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}/up-upper-primary-teacher/hindi/${topic.slug}/`;
  const pageTitle = `${topic.title} नोट्स, ट्रिक्स एवं अभ्यास | UP Junior Super TET Hindi | SJMaths`;
  const metaDesc = `UP Upper Primary Assistant Teacher 2026 हिन्दी भाषा एवं साहित्य: ${topic.title} के बिन्दुवार नोट्स, माइंडमैप, तुलनात्मक तालिका, स्मरण सूत्र (Mnemonics), 10 अभ्यास प्रश्न एवं मिनी टेस्ट।`;

  const esc = (s) => String(s || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

  function cleanOptionText(opt) {
    if (!opt) return '';
    return String(opt).replace(/^(\([A-D]\)|\[[A-D]\]|[A-D][\).:-]|[A-D]\s*[-–—]\s*|[A-D]\s+)\s*/i, '').trim();
  }

  // Render Mindmap
  let mindmapHtml = '';
  if (data.mindmap && data.mindmap.branches && data.mindmap.branches.length > 0) {
    let branchesHtml = '';
    data.mindmap.branches.forEach((b) => {
      let subnodesHtml = (b.nodes || []).map(n => `<li class="mindmap-subnode-item"><i class="fas fa-angle-right" style="color: var(--brand-emerald); margin-right: 0.35rem;"></i>${esc(n)}</li>`).join('');
      branchesHtml += `
            <div class="mindmap-branch-card">
                <div class="mindmap-branch-title">
                    <i class="${esc(b.icon || 'fas fa-circle-dot')}" style="color: var(--brand-emerald);"></i>
                    <span>${esc(b.title)}</span>
                </div>
                <ul class="mindmap-subnodes">
                    ${subnodesHtml}
                </ul>
            </div>`;
    });

    mindmapHtml = `
        <div class="prep-card">
            <h2>
                <i class="fas fa-sitemap" style="color: var(--brand-emerald);"></i>
                <span>माइंडमैप (Mindmap — समग्र संकल्पना प्रवाह)</span>
            </h2>
            <div class="mindmap-wrapper">
                <div class="mindmap-root-node">
                    <span class="mindmap-root-badge">
                        <i class="fas fa-brain"></i>
                        <span>${esc(data.mindmap.central_node || topic.shortTitle)}</span>
                    </span>
                </div>
                <div class="mindmap-branches">
                    ${branchesHtml}
                </div>
            </div>
        </div>`;
  }

  // Render Concepts
  let conceptsHtml = '';
  (data.concepts || []).forEach(c => {
    conceptsHtml += `
        <div class="prep-card">
            <h2>
                <i class="fas fa-bookmark" style="color: var(--brand-emerald);"></i>
                <span>${esc(c.heading)}</span>
            </h2>
            <div class="topic-content-body">
                ${c.html_content || ''}
            </div>
        </div>`;
  });

  // Render Comparative Table
  let compTableHtml = '';
  const tableData = data.comparative_table;
  if (tableData && tableData.headers && tableData.rows) {
    let ths = tableData.headers.map(h => `<th>${esc(h)}</th>`).join('');
    let trs = tableData.rows.map(row => {
      let tds = row.map((cell, idx) => {
        if (idx === 0) return `<td><strong>${esc(cell)}</strong></td>`;
        return `<td>${esc(cell)}</td>`;
      }).join('');
      return `<tr>${tds}</tr>`;
    }).join('');

    compTableHtml = `
        <div class="prep-card">
            <h2>
                <i class="fas fa-table-columns" style="color: var(--brand-emerald);"></i>
                <span>${esc(tableData.title || 'तुलनात्मक विश्लेषण एवं मुख्य परीक्षा भेद')}</span>
            </h2>
            <div class="table-scroll-wrapper">
                <table class="prep-table">
                    <thead>
                        <tr>${ths}</tr>
                    </thead>
                    <tbody>
                        ${trs}
                    </tbody>
                </table>
            </div>
        </div>`;
  }

  // Render Practice Questions (10 MCQs)
  let mcqsHtml = '';
  (data.mcqs || []).forEach((q, idx) => {
    let optionsListHtml = '';
    (q.options || []).forEach((opt, optIdx) => {
      const letter = ['A', 'B', 'C', 'D'][optIdx];
      const isCorrect = optIdx === q.correct_index;
      const cleaned = cleanOptionText(opt);
      optionsListHtml += `
            <button type="button" class="mcq-option-btn" data-correct="${isCorrect ? 'true' : 'false'}" onclick="handleMcqOptionClick(this, ${idx})">
                <span class="opt-label">${letter}</span>
                <span>${esc(cleaned)}</span>
            </button>`;
    });

    mcqsHtml += `
        <div class="mcq-item-card" id="mcq-card-${idx}">
            <div class="mcq-header-meta">
                <span class="mcq-q-pill">प्रश्न ${idx + 1} / ${data.mcqs.length}</span>
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior हिन्दी</span>
            </div>
            <div class="mcq-question-text">${esc(q.question)}</div>
            <div class="mcq-options-group">
                ${optionsListHtml}
            </div>
            <div class="mcq-explanation-box" id="mcq-exp-${idx}">
                <div class="exp-badge" style="color: var(--brand-emerald);"><i class="fas fa-check-circle"></i> सटीक व्याख्या एवं विश्लेषण:</div>
                <div style="font-size: 0.95rem; line-height: 1.65; color: var(--text-sub);">${esc(q.explanation)}</div>
            </div>
        </div>`;
  });

  // Prepare testData for interactive mini test
  const testDataJson = JSON.stringify((data.mcqs || []).map(q => ({
    question: q.question,
    question_hi: q.question,
    options: (q.options || []).map(cleanOptionText),
    options_hi: (q.options || []).map(cleanOptionText),
    correct_index: q.correct_index,
    explanation: q.explanation,
    explanation_hi: q.explanation
  })));

  // Render Rapid Recall Facts
  let factsHtml = '';
  (data.revision_facts || []).forEach((fact, fIdx) => {
    factsHtml += `
        <div class="revision-fact-row">
            <span class="fact-num-badge">#${fIdx + 1}</span>
            <div>${esc(fact)}</div>
        </div>`;
  });

  // Render Mnemonics
  let mnemonicsHtml = '';
  (data.mnemonics || []).forEach(m => {
    mnemonicsHtml += `
        <div class="mnemonic-card">
            <div style="font-weight: 700; font-family: 'Outfit', sans-serif; font-size: 1.05rem; color: var(--brand-indigo); margin-bottom: 0.5rem;">
                <i class="fas fa-key"></i> ${esc(m.title)}
            </div>
            <div class="mnemonic-quote-box">
                <strong style="color: var(--brand-emerald-dark); font-family: 'Outfit', monospace; font-size: 1.15rem; letter-spacing: 1px;">${esc(m.acronym)}</strong> — ${esc(m.expansion)}
            </div>
        </div>`;
  });

  // Render Traps
  let trapsHtml = '';
  (data.exam_traps || []).forEach((trap, tIdx) => {
    trapsHtml += `
        <div class="trap-card-item">
            <i class="fas fa-triangle-exclamation" style="color: #dc2626; font-size: 1.15rem; margin-top: 2px;"></i>
            <div>
                <strong>नकारात्मक अंकन चेतावनी #${tIdx + 1}:</strong>
                <p style="margin: 0.25rem 0 0 0;">${esc(trap)}</p>
            </div>
        </div>`;
  });

  // Render Checklist
  let checklistHtml = '';
  (data.checklist_items || []).forEach((item, cIdx) => {
    checklistHtml += `
        <label class="mastery-check-item">
            <input type="checkbox" id="chk-mastery-${cIdx}" class="custom-check" onchange="updateMasteryProgress()">
            <span>${esc(item)}</span>
        </label>`;
  });

  // Navigation Links
  const prevLink = prevTopic
    ? `<a href="/up-upper-primary-teacher/hindi/${prevTopic.slug}/" class="topic-nav-btn prev-btn"><i class="fas fa-chevron-left"></i> <span>पिछला: ${esc(prevTopic.shortTitle)}</span></a>`
    : `<span class="topic-nav-btn prev-btn disabled"><i class="fas fa-chevron-left"></i> <span>प्रथम अध्याय</span></span>`;

  const nextLink = nextTopic
    ? `<a href="/up-upper-primary-teacher/hindi/${nextTopic.slug}/" class="topic-nav-btn next-btn"><span>अगला: ${esc(nextTopic.shortTitle)}</span> <i class="fas fa-chevron-right"></i></a>`
    : `<span class="topic-nav-btn next-btn disabled"><span>अंतिम अध्याय</span> <i class="fas fa-chevron-right"></i></span>`;

  return `<!DOCTYPE html>
<html lang="hi">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${esc(pageTitle)}</title>
<meta content="${esc(topic.title)}, हिन्दी भाषा एवं साहित्य, UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
<meta content="SJMaths" name="author"/>
<meta content="${esc(metaDesc)}" name="description"/>
<meta content="index, follow, max-image-preview:large" name="robots"/>
<link href="${canonicalUrl}" rel="canonical"/>
<link href="/favicon.png" rel="icon" type="image/png"/>

<!-- Open Graph -->
<meta property="og:title" content="${esc(pageTitle)}"/>
<meta content="${esc(metaDesc)}" property="og:description"/>
<meta content="article" property="og:type"/>
<meta content="${canonicalUrl}" property="og:url"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" property="og:image"/>

<!-- Twitter Card -->
<meta content="summary_large_image" name="twitter:card"/>
<meta name="twitter:title" content="${esc(pageTitle)}"/>
<meta content="${esc(metaDesc)}" name="twitter:description"/>
<meta content="https://sjmaths.com/assets/icons/icon-512x512.png" name="twitter:image"/>

<!-- Fonts and Icons -->
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet"/>
<link as="style" crossorigin="anonymous" href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" onload="this.onload=null;this.rel='stylesheet'" rel="preload"/>
<noscript>
<link href="/assets/vendor/fontawesome/css/all.min.css?v=db73e473" rel="stylesheet"/>
</noscript>

<!-- Stylesheets (Common Asset Architecture) -->
<link href="/assets/css/main.min.css?v=a3faaea0" rel="stylesheet"/>
<link href="/assets/css/layout.min.css?v=e4922b08" rel="stylesheet"/>
<link href="/assets/css/component.min.css?v=3fce8e36" rel="stylesheet"/>
<link href="/assets/css/improved-ui.min.css?v=dd2cffe9" rel="stylesheet"/>
<link href="/assets/css/pages.min.css?v=9e3bd560" rel="stylesheet"/>
<link href="/assets/css/up-upper-primary-topic.min.css?v=20261006_04" rel="stylesheet"/>

<!-- Language Mode Enforcement: Hindi Only -->
<style>
    .lang-hi { display: inline !important; }
    .lang-en { display: none !important; }
</style>

<!-- Breadcrumb Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://sjmaths.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "UP Upper Primary Teacher",
      "item": "https://sjmaths.com/up-upper-primary-teacher/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Hindi",
      "item": "https://sjmaths.com/up-upper-primary-teacher/hindi/"
    },
    {
      "@type": "ListItem",
      "position": 4,
      "name": "${esc(topic.shortTitle)}",
      "item": "${canonicalUrl}"
    }
  ]
}
</script>

<!-- Theme & Palette Sync Script (Light / Dark Mode Persistence matching Homepage) -->
<script>
    (function () {
        ${upUpperPrimaryHeadThemeBootstrap}
        const savedTheme = localStorage.getItem('sjmaths-theme');
        const themePalettes = {
            green: { primary: '#059669', 'primary-dark': '#047857', 'primary-light': '#ecfdf5' },
            blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#eff6ff' },
            purple: { primary: '#7c3aed', 'primary-dark': '#6d28d9', 'primary-light': '#f5f3ff' },
            orange: { primary: '#ea580c', 'primary-dark': '#c2410c', 'primary-light': '#fff7ed' }
        };
        if (savedTheme && themePalettes[savedTheme]) {
            Object.entries(themePalettes[savedTheme]).forEach(([k, v]) => {
                document.documentElement.style.setProperty('--brand-' + k, v);
            });
        }
    })();
</script>
</head>

<body class="lang-mode-hi">
<script>
    ${upUpperPrimaryBodyThemeBootstrap}
</script>
<div id="header-container"></div>

<main class="topic-page-container">

    <!-- Top Action Bar -->
    <div class="top-action-bar">
        <div class="breadcrumb-trail">
            <a href="/"><i class="fas fa-home"></i> होम</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/">UP शिक्षक भर्ती</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <a href="/up-upper-primary-teacher/hindi/">हिन्दी पाठ्यक्रम</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${esc(topic.numStr)}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
            <a href="/up-upper-primary-teacher/hindi/" class="back-hub-btn">
                <i class="fas fa-arrow-left"></i>
                <span>मुख्य हिन्दी हब</span>
            </a>
            <a href="/up-upper-primary-teacher/" class="back-hub-btn">
                <i class="fas fa-th-large"></i>
                <span>सम्पूर्ण सिलेबस</span>
            </a>
        </div>
    </div>

    <!-- Topic Hero Panel -->
    <div class="topic-hero-panel">
        <div class="topic-meta-row">
            <span class="topic-badge-pill">${esc(topic.numStr)} अनिवार्य</span>
            <span class="subject-tag-pill">${esc(compactUpUpperPrimaryModuleLabel(topic.secTitle))}</span>
            <span class="subject-tag-pill">कक्षा 6–8 शिक्षक भर्ती</span>
        </div>
        <h1>
            <span>${esc(topic.shortTitle || topic.title)}</span>
        </h1>
        <p class="lead-desc">
            <span>${esc(data.key_focus_summary || topic.coreFocus)}</span>
        </p>
    </div>

    <!-- Live Completion Toggle -->
    <div class="completion-card">
        <div class="completion-card-left">
            <i class="fas fa-tasks" style="font-size: 1.5rem; color: var(--brand-emerald);"></i>
            <div>
                <strong style="font-size: 1rem; color: var(--text-headline);">
                    <span>तैयारी की स्थिति (Preparation Status)</span>
                </strong>
                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: var(--text-muted);" id="statusDesc">
                    <span>अध्ययन पूरा होने पर पूर्ण चिह्नित करें। प्रगति मुख्य पाठ्यक्रम हब के साथ स्वतः सिंक होती है।</span>
                </p>
            </div>
        </div>
        <button id="topicCompletionBtn" class="toggle-topic-btn" onclick="toggleTopicStatus()">
            <i class="fas fa-check-circle"></i>
            <span id="completionBtnText">पूर्ण चिह्नित करें (Mark Complete)</span>
        </button>
    </div>

    <!-- Study Tabs Strip -->
    <div class="study-tabs-strip" role="tablist">
        <button class="study-tab-btn active" data-tab="concepts">
            <i class="fas fa-book-open"></i>
            <span>1. संकल्पना एवं नियम</span>
        </button>
        <button class="study-tab-btn" data-tab="practice">
            <i class="fas fa-list-check"></i>
            <span>2. अभ्यास प्रश्न (10 MCQs)</span>
        </button>
        <button class="study-tab-btn" data-tab="test">
            <i class="fas fa-stopwatch"></i>
            <span>3. मिनी टेस्ट (5 मिनट)</span>
        </button>
        <button class="study-tab-btn" data-tab="revision">
            <i class="fas fa-redo"></i>
            <span>4. क्विक रिवीजन एवं परीक्षा जाल</span>
        </button>
    </div>

    <!-- ==================== TAB 1: CONCEPTS & THEORY ==================== -->
    <div class="study-tab-pane active" id="tab-concepts">
        <div class="strategy-banner-box">
            <p style="margin: 0; font-size: 0.95rem; color: var(--text-headline); line-height: 1.6;">
                <i class="fas fa-compass" style="color: var(--brand-emerald); margin-right: 0.4rem;"></i>
                <strong>पाठ्यक्रम फोकस एवं उच्च अंक रणनीति:</strong>
                <span>${esc(topic.coreFocus)}</span>
            </p>
        </div>

        <!-- Mindmap Component -->
        ${mindmapHtml}

        <!-- 4 Core Concepts -->
        ${conceptsHtml}

        <!-- Comparative Matrix Table -->
        ${compTableHtml}
    </div>

    <!-- ==================== TAB 2: PRACTICE QUESTIONS ==================== -->
    <div class="study-tab-pane" id="tab-practice">
        <div class="practice-summary-bar">
            <div>
                <strong style="color: var(--text-headline); font-size: 1.05rem;">परीक्षा अभ्यास प्रश्नोत्तरी (10 MCQs)</strong>
                <p style="margin: 2px 0 0 0; font-size: 0.85rem; color: var(--text-muted);" id="practiceProgressText">0 of ${data.mcqs.length} Answered</p>
            </div>
            <span class="practice-score-badge" id="practiceScoreBadge">Score: 0 / ${data.mcqs.length}</span>
        </div>

        ${mcqsHtml}
    </div>

    <!-- ==================== TAB 3: TIMED MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="prep-card">
            <div id="miniTestIntro" class="mini-test-intro">
                <h2><i class="fas fa-stopwatch" style="color: var(--brand-emerald);"></i> <span>समयबद्ध मिनी टेस्ट (Timed Mini Test)</span></h2>
                <p class="test-desc">यह 10 प्रश्नों का वास्तविक परीक्षा अनुरूप टेस्ट है। प्रत्येक सही उत्तर के लिए +3 अंक तथा प्रत्येक गलत उत्तर के लिए -1 अंक की नकारात्मक कटौती होगी। कुल समय: 5 मिनट।</p>
                <div class="test-stats-row">
                    <span class="test-stat-chip"><i class="fas fa-question-circle"></i> 10 प्रश्न</span>
                    <span class="test-stat-chip"><i class="fas fa-clock"></i> 5:00 मिनट</span>
                    <span class="test-stat-chip"><i class="fas fa-trophy"></i> 30 अधिकतम अंक</span>
                    <span class="test-stat-chip" style="color: #dc2626;"><i class="fas fa-minus-circle"></i> -1 नकारात्मक अंकन</span>
                </div>
                <button type="button" class="start-test-btn" onclick="startMiniTest()">
                    <i class="fas fa-play"></i> <span>टेस्ट प्रारंभ करें (Start Test)</span>
                </button>
            </div>

            <div id="miniTestActive" style="display: none;">
                <div class="test-timer-bar">
                    <div>
                        <span style="font-weight: 700; color: var(--text-headline);">प्रश्न संख्या:</span>
                        <span id="testCurrentQ" style="font-weight: 800; color: var(--brand-emerald);">1</span> / 10
                    </div>
                    <div class="test-countdown">
                        <i class="fas fa-stopwatch"></i>
                        <span id="timerDisplay">05:00</span>
                    </div>
                </div>

                <div id="testQuestionContainer"></div>

                <div class="test-nav-controls">
                    <button type="button" class="test-btn-nav" id="testPrevBtn" onclick="navTest(-1)"><i class="fas fa-chevron-left"></i> पिछला</button>
                    <button type="button" class="test-btn-nav" id="testNextBtn" onclick="navTest(1)">अगला <i class="fas fa-chevron-right"></i></button>
                    <button type="button" class="test-submit-btn" id="testSubmitBtn" style="display: none;" onclick="submitMiniTest()">टेस्ट सबमिट करें <i class="fas fa-check-double"></i></button>
                </div>
            </div>

            <div id="miniTestResult" style="display: none; text-align: center; padding: 2rem 1rem;">
                <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.8rem; font-weight: 800; color: var(--text-headline); margin-bottom: 0.5rem;">टेस्ट परिणाम</h3>
                <div id="testScoreDisplay" style="font-family: 'Outfit', sans-serif; font-size: 2.5rem; font-weight: 900; color: var(--brand-emerald); margin-bottom: 1rem;"></div>
                <div id="testBreakdownDisplay" style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1.5rem; flex-wrap: wrap;"></div>
                <p id="testFeedbackMsg" style="font-size: 1.05rem; color: var(--text-sub); max-width: 600px; margin: 0 auto 2rem; line-height: 1.6;"></p>
                <button type="button" class="retry-test-btn" onclick="startMiniTest()"><i class="fas fa-redo"></i> पुनः टेस्ट दें</button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: QUICK REVISION & TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #f59e0b;"></i>
                <span>त्वरित स्मरणीय मुख्य तथ्य (8 Rapid Recall Facts)</span>
            </h2>
            <div class="revision-facts-grid">
                ${factsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-brain" style="color: var(--brand-indigo);"></i>
                <span>अचूक स्मरण सूत्र (Memory Mnemonics Vault)</span>
            </h2>
            ${mnemonicsHtml}
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-triangle-exclamation" style="color: #dc2626;"></i>
                <span>परीक्षा के जाल एवं नकारात्मक अंकन से बचाव (-1 Penalty Traps)</span>
            </h2>
            <div class="traps-container">
                ${trapsHtml}
            </div>
        </div>

        <div class="prep-card">
            <h2>
                <i class="fas fa-circle-check" style="color: var(--brand-emerald);"></i>
                <span>स्व-मूल्यांकन चेकलिस्ट (Self-Assessment Checklist)</span>
            </h2>
            <div class="topic-mastery-checklist">
                ${checklistHtml}
            </div>
        </div>
    </div>

    <!-- Bottom Sequential Navigation -->
    <div class="bottom-topic-nav">
        ${prevLink}
        ${nextLink}
    </div>

</main>

<button aria-label="Back to Top" class="back-to-top-btn" id="backToTopBtn">
    <i class="fas fa-arrow-up"></i>
</button>

<!-- Interactive Logic & Shared Runtime Engine -->
<script>
    window.TOPIC_STORAGE_KEY = 'up-upper-primary-teacher-checklist-v2';
    window.TOPIC_CHECKBOX_ID = '${topic.chkId}';
    window.testData = ${testDataJson};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js?v=20261002_02"></script>
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=c0d93c8c"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=d48c181a"></script>
<script src="/assets/js/require-auth.min.js?v=3060658c" type="module"></script>
</body>
</html>
`;
}

// 7. Generation Orchestrator
async function generateTopicContent(topic) {
  const prompt = buildHindiPrompt(topic);
  const maxRetries = 4;

  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const active = getActiveConfig();
    const modelToUse = active.models[(attempt - 1) % active.models.length] || MODEL_NAME;
    console.log(`  [Calling API] ${topic.slug} (Attempt ${attempt}/${maxRetries} via ${active.name} / ${modelToUse})...`);

    try {
      const ai = new GoogleGenAI({ apiKey: active.key });
      const response = await ai.models.generateContent({
        model: modelToUse,
        contents: prompt,
        config: {
          temperature: 0.2,
          responseMimeType: 'application/json'
        }
      });

      const rawText = response.text || '';
      let cleanedText = rawText.trim();
      if (cleanedText.startsWith('```json')) cleanedText = cleanedText.slice(7);
      if (cleanedText.startsWith('```')) cleanedText = cleanedText.slice(3);
      if (cleanedText.endsWith('```')) cleanedText = cleanedText.slice(0, -3);
      cleanedText = cleanedText.trim();

      let parsed;
      try {
        parsed = JSON.parse(cleanedText);
      } catch {
        parsed = JSON.parse(jsonrepair(cleanedText));
      }

      // Basic validation
      if (!parsed.concepts || parsed.concepts.length < 3 || !parsed.mcqs || parsed.mcqs.length < 8) {
        throw new Error(`Incomplete payload: concepts=${parsed.concepts?.length}, mcqs=${parsed.mcqs?.length}`);
      }

      return parsed;
    } catch (err) {
      console.warn(`  [Warning] Attempt ${attempt} failed: ${err.message}`);
      rotateKey();
      const delay = Math.min(attempt * 2000, 8000);
      await new Promise(r => setTimeout(r, delay));
    }
  }

  throw new Error(`Failed to generate topic content for ${topic.slug} after ${maxRetries} attempts.`);
}

async function main() {
  console.log(`================================================================`);
  console.log(`SJMaths — UP Upper Primary Teacher (Class 6-8) Hindi Generator`);
  console.log(`Pure Hindi Pointwise Notes, Mnemonics, Mindmap, Tables & MCQs`);
  console.log(`Total Topics in Manifest: ${HINDI_TOPICS.length}`);
  console.log(`================================================================\n`);

  let targets = HINDI_TOPICS;
  if (TARGET_SLUG) {
    targets = HINDI_TOPICS.filter(t => t.slug === TARGET_SLUG);
    if (targets.length === 0) {
      console.error(`ERROR: Target topic '${TARGET_SLUG}' not found in manifest.`);
      process.exit(1);
    }
  }

  if (LIMIT && LIMIT > 0) {
    targets = targets.slice(0, LIMIT);
  }

  let generatedCount = 0;
  let skippedCount = 0;

  const pendingTasks = [];
  for (let i = 0; i < targets.length; i++) {
    const topic = targets[i];
    const prevTopic = i > 0 ? targets[i - 1] : null;
    const nextTopic = i < targets.length - 1 ? targets[i + 1] : null;

    const topicDir = path.join(OUTPUT_DIR, topic.slug);
    const topicFile = path.join(topicDir, 'index.html');

    if (!FORCE && statusMap[topic.slug] && statusMap[topic.slug].status === 'completed' && fs.existsSync(topicFile)) {
      console.log(`[SKIP] Already completed: ${topic.slug}`);
      skippedCount++;
      continue;
    }

    pendingTasks.push({ topic, prevTopic, nextTopic, index: i, total: targets.length });
  }

  console.log(`\nPending to generate: ${pendingTasks.length} topics (Concurrency: ${CONCURRENCY})\n`);

  if (DRY_RUN) {
    pendingTasks.forEach(t => console.log(`  [DRY-RUN] Would generate: ${t.topic.slug}`));
    return;
  }

  let taskPointer = 0;
  async function worker(workerId) {
    while (taskPointer < pendingTasks.length) {
      const currentTask = pendingTasks[taskPointer++];
      const { topic, prevTopic, nextTopic, index, total } = currentTask;
      const topicDir = path.join(OUTPUT_DIR, topic.slug);
      const topicFile = path.join(topicDir, 'index.html');

      console.log(`[Worker ${workerId}][${index + 1}/${total}] Starting: ${topic.slug} (${topic.title.slice(0, 50)}...)`);

      try {
        const data = await generateTopicContent(topic);
        const html = renderHindiPage(topic, data, prevTopic, nextTopic);

        if (!fs.existsSync(topicDir)) {
          fs.mkdirSync(topicDir, { recursive: true });
        }

        fs.writeFileSync(topicFile, html, 'utf8');

        statusMap[topic.slug] = {
          status: 'completed',
          timestamp: new Date().toISOString(),
          sizeBytes: html.length,
          title: topic.title,
          secIdx: topic.secIdx,
          chkId: topic.chkId
        };
        saveStatus();

        generatedCount++;
        console.log(`[Worker ${workerId}]  ✓ SUCCESS: Generated ${topic.slug} (${Math.round(html.length / 1024)} KB)`);

        await new Promise(r => setTimeout(r, 1000));
      } catch (err) {
        console.error(`[Worker ${workerId}]  ✗ FAILED: ${topic.slug} -> ${err.message}`);
        statusMap[topic.slug] = {
          status: 'failed',
          timestamp: new Date().toISOString(),
          error: err.message
        };
        saveStatus();
      }
    }
  }

  const pool = Array.from({ length: Math.min(CONCURRENCY, pendingTasks.length) }, (_, id) => worker(id + 1));
  await Promise.all(pool);

  console.log(`\n================================================================`);
  console.log(`Batch Summary:`);
  console.log(`  - Successfully Generated: ${generatedCount}`);
  console.log(`  - Skipped (Existing):     ${skippedCount}`);
  console.log(`  - Total Processed:        ${targets.length}`);
  console.log(`================================================================`);
}

main().catch(err => {
  console.error('Fatal execution error:', err);
  process.exit(1);
});
