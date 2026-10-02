#!/usr/bin/env node
/**
 * ============================================================================
 * SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) Sanskrit Language & Literature
 * Complete Sanskrit Language Content Generation Engine
 * Pointwise Concept Notes, Memory Mnemonics, Tips, Tricks, Mindmap, Tables & 10 MCQs
 *
 * Subject: Sanskrit Language & Literature (90 Questions | 270 Marks | -1 Negative Marking)
 * Covers all 31 directories in up-upper-primary-teacher/sanskrit/
 *
 * Uses common CSS: /assets/css/up-upper-primary-topic.min.css?v=20261002_02
 * Uses common JS:  /assets/js/up-upper-primary-topic.min.js?v=20261002_02
 * ============================================================================
 */

import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { jsonrepair } from 'jsonrepair';

const ROOT = process.cwd();
const DOMAIN = 'https://sjmaths.com';
const STATUS_FILE = path.join(ROOT, 'content-generation-status-upper-primary-sanskrit.json');
const OUTPUT_DIR = path.join(ROOT, 'up-upper-primary-teacher', 'sanskrit');

// 1. API Configuration & Key Rotation
const KEY_CONFIGS = [
  { key: process.env.GEMINI_API_KEY_1, name: 'KEY_1', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] },
  { key: process.env.GEMINI_API_KEY_2, name: 'KEY_2', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] },
  { key: process.env.GEMINI_API_KEY,   name: 'KEY_3', models: ['gemini-3.5-flash-lite', 'gemini-3.8-flash', 'gemini-2.5-flash'] }
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
const CONCURRENCY = (() => {
  const idx = args.indexOf('--concurrency');
  return idx !== -1 && args[idx + 1] ? Math.max(1, parseInt(args[idx + 1], 10)) : 2;
})();

// 3. Status Tracking
let statusMap = {};
if (fs.existsSync(STATUS_FILE)) {
  try {
    statusMap = JSON.parse(fs.readFileSync(STATUS_FILE, 'utf8'));
  } catch (e) {
    statusMap = {};
  }
}

function saveStatus() {
  fs.writeFileSync(STATUS_FILE, JSON.stringify(statusMap, null, 2), 'utf8');
}

// 4. Sanskrit Syllabus Catalog (31 Micro-Topics across 3 Modules)
export const SANSKRIT_TOPICS = [
  // ==================== खण्ड 1: संस्कृत व्याकरण एवं माहेश्वर सूत्र (12 Micro + 6 Comprehensive) ====================
  {
    slug: 'maheshwar-sutras',
    numStr: '#1.1',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'माहेश्वर सूत्राणि एवं प्रत्याहार निर्माण विधि (४२/४४ प्रत्याहार)',
    shortTitle: 'माहेश्वर सूत्राणि व प्रत्याहार',
    chkId: 'chk-sanskrit-1-1',
    coreFocus: 'चतुर्दश (14) माहेश्वर सूत्र (अइउण्...हल्), इत्संज्ञा विधायक सूत्र (हलन्त्यम्), तस्य लोपः, प्रत्याहार विधायक सूत्र (आदिरन्त्येन सहेता), 42/44 प्रत्याहार एवं वर्ण गणना।'
  },
  {
    slug: 'varna-vichar',
    numStr: '#1.2',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'वर्ण विचार एवं उच्चारण स्थानानि — स्वर (अच्), व्यञ्जन (हल्) व प्रयत्न',
    shortTitle: 'वर्ण विचार एवं उच्चारण स्थान',
    chkId: 'chk-sanskrit-1-2',
    coreFocus: 'अकुहविसर्जनीयानां कण्ठः, इचुयशानां तालु, उपूपध्मानीयानां ओष्ठौ, लृतुलसानां दन्ताः; आभ्यन्तर प्रयत्न (5) एवं बाह्य प्रयत्न (11) — विवार, संवार, श्वास, नाद, घोष, अघोष, अल्पप्राण, महाप्राण, उदात्त, अनुदात्त, स्वरित।'
  },
  {
    slug: 'sandhi-ach-swar',
    numStr: '#1.3',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'अच् (स्वर) सन्धि — दीर्घ, गुण, वृद्धि, यण् एवं अयादि सन्धि सूत्र व प्रयोग',
    shortTitle: 'अच् (स्वर) सन्धि',
    chkId: 'chk-sanskrit-1-3',
    coreFocus: 'अकः सवर्णे दीर्घः, आद्गुणः, वृद्धिरेचि, इको यणचि, एचोऽयवायावः, एङि पररूपम्, एङः पदान्तादति (पूर्वरूप) सूत्र, उदाहरण एवं अपवाद।'
  },
  {
    slug: 'sandhi-hal-visarga',
    numStr: '#1.4',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'हल् (व्यञ्जन) एवं विसर्ग सन्धि — श्चुत्व, ष्टुत्व, जश्त्व, रुत्व व लोप नियम',
    shortTitle: 'हल् एवं विसर्ग सन्धि',
    chkId: 'chk-sanskrit-1-4',
    coreFocus: 'स्तोः श्चुना श्चुः, ष्टुना ष्टुः, झलां जशोऽन्ते, झलां जश् झशि, खरि च (चर्त्व), विसर्जनीयस्य सः, ससजुषो रुः, अतो रोरप्लुतादप्लुते, हशि च, रो रि (ढ्रलोपे पूर्वस्य दीर्घोऽणः)।'
  },
  {
    slug: 'sandhi',
    numStr: '#1.3-4',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'सन्धि प्रकरणम् (समग्र अध्ययन) — अच् (स्वर), हल् (व्यञ्जन) एवं विसर्ग सन्धि नियम',
    shortTitle: 'सन्धि प्रकरणम् समग्र',
    chkId: 'chk-sanskrit-1-sandhi',
    coreFocus: 'संहितायाम् (परः संनिकर्षः संहिता), स्वर-व्यञ्जन-विसर्ग सन्धि के सभी प्रमुख सूत्र, सन्धि-विच्छेद की सटीक विधियाँ, परीक्षा में सर्वाधिक पूछे जाने वाले 50 संन्धि उदाहरण।'
  },
  {
    slug: 'samasa-avyayibhava-tatpurusha',
    numStr: '#1.5',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'समास प्रकरणम् (भाग 1) — अव्ययीभाव, तत्पुरुष (द्वितीया-सप्तमी) व कर्मधारय',
    shortTitle: 'अव्ययीभाव, तत्पुरुष व कर्मधारय',
    chkId: 'chk-sanskrit-1-5',
    coreFocus: 'समसनं समासः, अव्ययीभाव समास (यथाशक्ति, उपगङ्गम्, प्रतिदिनम्), तत्पुरुष समास के 6 भेद, उपपद तत्पुरुष, अलुक् तत्पुरुष, कर्मधारय (विशेषण-विशेष्य, उपमान-उपमेय)।'
  },
  {
    slug: 'samasa-dvigu-dvandva-bahuvrihi',
    numStr: '#1.6',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'समास प्रकरणम् (भाग 2) — द्विगु, द्वन्द्व (इतरेतर, समाहार) एवं बहुव्रीहि विग्रह',
    shortTitle: 'द्विगु, द्वन्द्व व बहुव्रीहि समास',
    chkId: 'chk-sanskrit-1-6',
    coreFocus: 'संख्यापूर्वो द्विगुः (पञ्चवटी, त्रिभुवनम्), चार्थे द्वन्द्वः (इतरेतर, समाहार, एकशेष), अनेकमन्यपदार्थे बहुव्रीहिः (पीताम्बरः, लम्बोधरः, चन्द्रशेखरः), विग्रह वाक्य रचना।'
  },
  {
    slug: 'samasa',
    numStr: '#1.5-6',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'समास प्रकरणम् (समग्र अध्ययन) — षड् समासाः एवं समास विग्रह (समग्र विश्लेषण)',
    shortTitle: 'समास प्रकरणम् समग्र',
    chkId: 'chk-sanskrit-1-samasa',
    coreFocus: 'समास की परिभाषा, समास के 4/5/6 भेद (सिद्धान्तकौमुदी व लघुसिद्धान्तकौमुदी मत), समस्त पद निर्माण, लौकिक व अलौकिक विग्रह, प्रमुख अपवाद व परीक्षा जाल।'
  },
  {
    slug: 'karaka-prathama-chaturthi',
    numStr: '#1.7',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'कारक एवं विभक्ति (भाग 1) — कर्ता, कर्म, करण एवं सम्प्रदान कारक सूत्र',
    shortTitle: 'कारक भाग 1 (प्रथमा-चतुर्थी)',
    chkId: 'chk-sanskrit-1-7',
    coreFocus: 'प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा, कर्तुरीप्सिततमं कर्म, अकथितं च (16 द्विकर्मक धातुओं की सूची), साधकतमं करणम्, येनाङ्गविकारः, कर्मणा यमभिप्रेति स सम्प्रदानम्, रुच्यर्थानां प्रीयमाणः, नमः स्वस्तिस्वाहास्वधालंवषड्योगाच्च।'
  },
  {
    slug: 'karaka-panchami-saptami',
    numStr: '#1.8',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'कारक एवं उपपद विभक्ति (भाग 2) — अपादान, सम्बन्ध, अधिकरण व उपपद नियम',
    shortTitle: 'कारक भाग 2 (पञ्चमी-सप्तमी)',
    chkId: 'chk-sanskrit-1-8',
    coreFocus: 'ध्रुवमपायेऽपादानम्, भीत्रार्थानां भयहेतुः, आख्यातोपयोगे, जनिकर्तुः प्रकृतिः, षष्ठी शेषे, षष्ठी चानादरे, आधारोऽधिकरणम् (औपश्लेषिक, वैषयिक, अभिव्यापक), यतश्च निर्धारणम्, यस्य च भावेन भावलक्षणम्।'
  },
  {
    slug: 'karaka',
    numStr: '#1.7-8',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'कारक एवं विभक्ति प्रकरणम् (समग्र अध्ययन) — षट् कारकाणि व सप्त विभक्तयः',
    shortTitle: 'कारक प्रकरणम् समग्र',
    chkId: 'chk-sanskrit-1-karaka',
    coreFocus: 'क्रियान्वयित्वं कारकत्वम् (कारक 6 हैं, सम्बन्ध और सम्बोधन कारक नहीं माने जाते), कारक विभक्ति बनाम उपपद विभक्ति की वरीयता (उपपदविभक्तेः कारकविभक्तिर्बलीयसी), 50 मानक वाक्य उदाहरण।'
  },
  {
    slug: 'shabda-rupani',
    numStr: '#1.9',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'शब्द रूपाणि — अजन्त, हलन्त एवं सर्वनाम पद रूपाणि (राम, लता, नदी, फल, सर्व आदि)',
    shortTitle: 'शब्द रूपाणि (अजन्त, हलन्त, सर्वनाम)',
    chkId: 'chk-sanskrit-1-9',
    coreFocus: 'पुल्लिङ्ग: राम, हरि, गुरु, पितृ, राजन्, मरुत्; स्त्रीलिङ्ग: लता, मति, नदी, धेनु, वधू, मातृ; नपुंसकलिङ्ग: फल, वारि, दधि, मधु; सर्वनाम: अस्मद्, युष्मद्, तद्, यद्, किम्, सर्व, इदम्; संख्यावाचक शब्द (1 से 100 तक)।'
  },
  {
    slug: 'dhatu-rupani',
    numStr: '#1.10',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'धातु रूपाणि — पञ्च लकाराः (लट्, लोट्, लङ्, विधिलिङ्, लृट्) परस्मैपद व आत्मनेपद',
    shortTitle: 'धातु रूपाणि (पञ्च लकाराः)',
    chkId: 'chk-sanskrit-1-10',
    coreFocus: 'भू (भव्), पठ्, गम् (गच्छ्), दृश् (पश्य्), पा (पिब्), कृ, ज्ञा, स्था (तिष्ठ्), सेव्, लभ् धातुओं के 5 लकारों में रूप; तिङ् प्रत्यय (18), पुरुष एवं वचन व्यवस्था, आत्मनेपद व परस्मैपद पहचान ट्रिक्स।'
  },
  {
    slug: 'pratyaya',
    numStr: '#1.11',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'प्रत्यय प्रकरणम् — कृत् (क्त्वा, ल्यप्, तुमुन्, क्त), तद्धित एवं स्त्री प्रत्यय (टाप्, ङीप्)',
    shortTitle: 'प्रत्यय प्रकरणम् (कृत्, तद्धित, स्त्री)',
    chkId: 'chk-sanskrit-1-11',
    coreFocus: 'कृत् प्रत्यय: क्त्वा, ल्यप्, तुमुन्, तव्यत्, अनीयर्, शतृ, शानच्, क्त, क्तवतु; तद्धित प्रत्यय: मतुप्, तरप्, तमप्, त्व, तल्, अण्; स्त्री प्रत्यय: अजाद्यतष्टाप् (टाप्), ङीप्, ङीष्, ङीन्, ती; प्रत्ययान्त पदों की पहचान ट्रिक्स।'
  },
  {
    slug: 'avyaya-upasarga-shuddhi',
    numStr: '#1.12',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'अव्यय पदानि, २२ उपसर्गाः, संस्कृत अनुवाद नियम एवं अशुद्धि-संशोधन',
    shortTitle: 'अव्यय, उपसर्ग व अशुद्धि-संशोधन',
    chkId: 'chk-sanskrit-1-12',
    coreFocus: 'सदृशं त्रिषु लिङ्गेषु (अव्यय की परिभाषा), प्रमुख अव्यय (अत्र, तत्र, कुत्र, कदा, यदा, सर्वदा, उच्चैः, नीचैः, सह, विना), 22 उपसर्ग (प्रादयः — प्र, परा, अप, सम्, अनु...), अनुवाद के 9 स्वर्णिम नियम, कारक व लकार आधारित अशुद्धि संशोधन।'
  },
  {
    slug: 'avyaya-upasarga',
    numStr: '#1.12A',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'अव्यय एवं उपसर्ग प्रकरणम् — द्वाविंशति (22) उपसर्गाः एवं प्रमुख अव्यय पद प्रयोग',
    shortTitle: 'अव्यय एवं उपसर्ग समग्र',
    chkId: 'chk-sanskrit-1-avyaya',
    coreFocus: 'उपसर्गेण धात्वर्थो बलादन्यत्र नीयते (हार, प्रहार, आहार, संहार, विहार, परिहार), 22 उपसर्गाः अर्थ एवं उदाहरण, क्रियायोगे प्रादयः उपसर्गाः स्युः, स्वरादिनिपातमव्ययम्।'
  },
  {
    slug: 'shuddhi-sukti',
    numStr: '#1.12B',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'संस्कृत वाक्य रचना, अनुवाद नियम, अशुद्धि-संशोधन एवं सूक्ति संग्रह',
    shortTitle: 'वाक्य रचना व सूक्ति संग्रह',
    chkId: 'chk-sanskrit-1-shuddhi',
    coreFocus: 'कर्ता-क्रिया सामंजस्य, विशेषण-विशेष्य लिंग-वचन एकरूपता, उपपद विभक्ति प्रयोग, परीक्षा में बार-बार पूछे जाने वाले 30 अशुद्ध-शुद्ध वाक्य, अमर नीति सूक्तियां।'
  },
  {
    slug: 'sanskrit-vyakaran-maheshwar-sutras',
    numStr: '#1.0',
    secIdx: 1,
    secTitle: 'संस्कृत व्याकरण एवं माहेश्वर सूत्र',
    title: 'संस्कृत व्याकरण का इतिहास, पाणिनीय परम्परा एवं त्रिमुनि (पाणिनि, कात्यायन, पतञ्जलि)',
    shortTitle: 'संस्कृत व्याकरण परिचय व त्रिमुनि',
    chkId: 'chk-sanskrit-1-vyakaran',
    coreFocus: 'व्याक्रियन्ते व्युत्पाद्यन्ते शब्दा अनेनेति व्याकरणम्, अष्टाध्यायी (पाणिनि), वार्तिक (कात्यायन/वररुचि), महाभाष्य (पतञ्जलि), सिद्धान्तकौमुदी (भट्टोजिदीक्षित), लघुसिद्धान्तकौमुदी (वरदराज)।'
  },

  // ==================== खण्ड 2: संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार (8 Micro + 2 Comprehensive) ====================
  {
    slug: 'vedic-literature-upanishads',
    numStr: '#2.1',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'वैदिक साहित्य — चत्वारः वेदाः, ब्राह्मण, आरण्यक, प्रमुख उपनिषद एवं वेदांग',
    shortTitle: 'वैदिक साहित्य एवं उपनिषद',
    chkId: 'chk-sanskrit-2-1',
    coreFocus: 'ऋग्वेद (10 मण्डल, 1028 सूक्त, गायत्री मन्त्र), यजुर्वेद (शुक्ल व कृष्ण), सामवेद (भारतीय संगीत का मूल), अथर्ववेद (चिकित्सा व जनसाधारण); प्रमुख उपनिषद (ईश, केन, कठ, मुण्डक — सत्यमेव जयते); षड् वेदांग (शिक्षा, कल्प, व्याकरण, निरुक्त, छन्द, ज्योतिष)।'
  },
  {
    slug: 'epics-ramayana-mahabharata',
    numStr: '#2.2',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'संस्कृत आर्ष महाकाव्य — वाल्मीकि रामायण (७ काण्ड) एवं व्यास महाभारत (१८ पर्व)',
    shortTitle: 'रामायण एवं महाभारत आर्ष काव्य',
    chkId: 'chk-sanskrit-2-2',
    coreFocus: 'आदिकवि वाल्मीकि (आदिकाव्य रामायण, 24000 श्लोक — चतुर्विंशतिसाहस्री संहिता, 7 काण्ड, अनुष्टुप् छन्द, करुण रस); वेदव्यास प्रणीत महाभारत (जय, भारत, महाभारत — शतसाहस्री संहिता, 1 लाख श्लोक, 18 पर्व, शान्त रस, भगवद्गीता भीष्मपर्व में 18 अध्याय)।'
  },
  {
    slug: 'sanskrit-mahakavya-tradition',
    numStr: '#2.3',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'शास्त्रीय संस्कृत महाकाव्य परंपरा एवं पञ्चमहाकाव्य (रघुवंश, किरातार्जुनीयम्, नैषध आदि)',
    shortTitle: 'शास्त्रीय पञ्चमहाकाव्य परंपरा',
    chkId: 'chk-sanskrit-2-3',
    coreFocus: 'पञ्चमहाकाव्य: रघुवंशम् (19 सर्ग), कुमारसम्भवम् (17 सर्ग), किरातार्जुनीयम् (18 सर्ग), शिशुपालवधम् (20 सर्ग), नैषधीयचरितम् (22 सर्ग); बृहत्त्रयी (किरातार्जुनीयम्, शिशुपालवधम्, नैषधीयचरितम्); लघुत्रयी (रघुवंशम्, कुमारसम्भवम्, मेघदूतम्); महाकाव्य के शास्त्रीय लक्षण।'
  },
  {
    slug: 'kalidasa-works-dramas',
    numStr: '#2.4',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'महाकवि कालिदास — जीवन वृत्त, सप्त कृतियां (अभिज्ञानशाकुन्तलम्, मेघदूतम्) व काव्य सौंदर्य',
    shortTitle: 'महाकवि कालिदास एवं सप्त कृतियां',
    chkId: 'chk-sanskrit-2-4',
    coreFocus: 'उपमा कालिदासस्य, 7 कालजयी रचनाएँ: 2 महाकाव्य (रघुवंश, कुमारसम्भव), 2 खण्डकाव्य (मेघदूत, ऋतुसंहार), 3 नाटक (अभिज्ञानशाकुन्तलम् - 7 अंक, विक्रमोर्वशीयम्, मालविकाग्निमित्रम्); रीति: वैदर्भी, शकुन्तला के चतुर्थ अंक की 4 प्रसिद्ध सूक्तियां।'
  },
  {
    slug: 'sanskrit-dramatists-bhasa-bhavabhuti',
    numStr: '#2.5',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'प्रमुख संस्कृत नाटककार — भास (१३ नाटक), भवभूति (उत्तररामचरितम्) व शूद्रक',
    shortTitle: 'भास, भवभूति एवं शूद्रक नाटककार',
    chkId: 'chk-sanskrit-2-5',
    coreFocus: 'भासनाटकचक्र (13 नाटक, स्वप्नवासवदत्तम्, प्रतिमानाटकम्, दूतवाक्यम्); भवभूति: कारुण्य रस के प्रतिष्ठाता (एको रसः करुण एव, उत्तररामचरितम्, महावीरचरितम्, मालतीमाधवम्); शूद्रक: मृच्छकटिकम् (10 अंक, रूपक का प्रकरण भेद, चारुदत्त व वसन्तसेना)।'
  },
  {
    slug: 'sanskrit-poets-bharavi-magha',
    numStr: '#2.6',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'प्रमुख संस्कृत कवि — भारवि (किरातार्जुनीयम्), माघ (शिशुपालवधम्) व श्रीहर्ष',
    shortTitle: 'भारवि, माघ एवं श्रीहर्ष (बृहत्त्रयी)',
    chkId: 'chk-sanskrit-2-6',
    coreFocus: 'भारवेरर्थगौरवम् (किरातार्जुनीयम्, प्रथम तीन सर्ग पाषाणत्रय, अर्जुन-शिव किरात युद्ध); माघे सन्ति त्रयो गुणाः (उपमा, अर्थगौरव, पदलालित्य, शिशुपालवधम्); नैषधे पदलालित्यम् (श्रीहर्ष, नैषधीयचरितम्, विद्वदौषधम्); बृहत्त्रयी कवियों की तुलनात्मक सारणी।'
  },
  {
    slug: 'sanskrit-prose-banabhatta-dandin',
    numStr: '#2.7',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'संस्कृत गद्यकार एवं कथा साहित्य — बाणभट्ट (कादम्बरी), दण्डी एवं पञ्चतन्त्रम्',
    shortTitle: 'बाणभट्ट, दण्डी एवं गद्य साहित्य',
    chkId: 'chk-sanskrit-2-7',
    coreFocus: 'बाणोच्छिष्टं जगत्सर्वम् (कादम्बरी - कथा, चन्द्रापीड व पुण्डरीक का त्रिजन्म वर्णन, शुकनासोपदेश; हर्षचरितम् - आख्यायिका); दण्डी: दण्डिनः पदलालित्यम् (दशकुमारचरितम्); सुबन्धु: वासवदत्ता; विष्णुशर्मा: पञ्चतन्त्रम् (मित्रभेद, मित्रलाभ, काकोलूकीय, लब्धप्रणाश, अपरीक्षितकारकम्); नारायण पण्डित: हितोपदेश।'
  },
  {
    slug: 'subhashitani-famous-suktis',
    numStr: '#2.8',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'संस्कृत सूक्तयः, सुभाषितानि, सूक्ति-सुधा एवं नीतिपरक श्लोक संग्रह',
    shortTitle: 'संस्कृत सूक्तयः एवं सुभाषितानि',
    chkId: 'chk-sanskrit-2-8',
    coreFocus: 'भर्तृहरि के तीन शतक (नीतिशतकम्, शृङ्गारशतकम्, वैराग्यशतकम्); प्रसिद्ध सूक्तियां: सर्वे गुणाः काञ्चनमाश्रयन्ति, विद्या ददाति विनयं, न हि सुप्तस्य सिंहस्य प्रविशन्ति मुखे मृगाः, अयम् निजः परो वेति गणना लघुचेतसाम्; श्लोक अन्वय एवं सन्दर्भ।'
  },
  {
    slug: 'pramukh-sanskrit-kavi-natakar',
    numStr: '#2.5A',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'प्रमुख संस्कृत कवि, नाटककार एवं उनकी अमर कृतियां (समग्र सिंहावलोकन)',
    shortTitle: 'प्रमुख संस्कृत कवि व नाटककार',
    chkId: 'chk-sanskrit-2-kavi',
    coreFocus: 'कालिदास, भास, भवभूति, भारवि, माघ, श्रीहर्ष, बाणभट्ट, दण्डी, विशाखदत्त (मुद्राराक्षसम्), भट्टनारायण (वेणीसंहारम्); आश्रयदाता, समय, ग्रन्थ, अंक/सर्ग संख्या एवं प्रमुख नायक-नायिका।'
  },
  {
    slug: 'sanskrit-sahitya-itihas',
    numStr: '#2.0',
    secIdx: 2,
    secTitle: 'संस्कृत साहित्य, प्रमुख महाकाव्य एवं नाटककार',
    title: 'संस्कृत साहित्य का समग्र इतिहास — वैदिक काल, लौकिक काल, महाकाव्य, गद्य व दृश्य काव्य',
    shortTitle: 'संस्कृत साहित्य का समग्र इतिहास',
    chkId: 'chk-sanskrit-2-sahitya',
    coreFocus: 'वैदिक साहित्य से लौकिक साहित्य का संक्रमण, दृश्य काव्य (नाटक) व श्रव्य काव्य (महाकाव्य, खण्डकाव्य, गद्य, चम्पू) का कालक्रम, प्रमुख साहित्यिक संप्रदाय एवं अलंकार शास्त्र।'
  },

  // ==================== खण्ड 3: संस्कृत अपठित बोध (2 Micro + 1 Comprehensive) ====================
  {
    slug: 'sanskrit-apatit-gadyansh',
    numStr: '#3.1',
    secIdx: 3,
    secTitle: 'संस्कृत अपठित बोध',
    title: 'संस्कृत अपठित गद्यांश — गद्यांश बोध, सारांश, शब्दार्थ एवं व्याकरण आधारित प्रश्नोत्तर',
    shortTitle: 'संस्कृत अपठित गद्यांश बोध',
    chkId: 'chk-sanskrit-3-1',
    coreFocus: 'संस्कृत गद्यांश को पढ़कर त्वरित भाव समझना, सन्धि, समास, विभक्ति, प्रत्यय, अव्यय तथा विलोम/समानार्थक पदों की पहचान, शीर्षक चयन की वैज्ञानिक तकनीक एवं 5 आदर्श गद्यांश हल सहित।'
  },
  {
    slug: 'sanskrit-apatit-padyansh',
    numStr: '#3.2',
    secIdx: 3,
    secTitle: 'संस्कृत अपठित बोध',
    title: 'संस्कृत अपठित पद्यांश (श्लोक) — भावार्थ, छन्द, अलंकार एवं रस आधारित प्रश्नोत्तर',
    shortTitle: 'संस्कृत अपठित पद्यांश (श्लोक)',
    chkId: 'chk-sanskrit-3-2',
    coreFocus: 'श्लोकों का अन्वय (पदान्वय), प्रमुख संस्कृत छन्द (अनुष्टुप्, इन्द्रवज्रा, उपेन्द्रवज्रा, वसन्ततिलका, मन्दाक्रान्ता, शिखरिणी, शार्दूलविक्रीडित), अलंकार (अनुप्रास, यमक, उपमा, रूपक, उत्प्रेक्षा) एवं रस निरूपण।'
  },
  {
    slug: 'sanskrit-apatit-gadyansh-padyansh',
    numStr: '#3.0',
    secIdx: 3,
    secTitle: 'संस्कृत अपठित बोध',
    title: 'संस्कृत अपठित गद्यांश एवं पद्यांश (श्लोक) — समग्र विश्लेषण एवं हल प्रश्न संग्रह',
    shortTitle: 'अपठित गद्यांश व पद्यांश समग्र',
    chkId: 'chk-sanskrit-3-apatit',
    coreFocus: 'UP शिक्षक भर्ती परीक्षा के वास्तविक पैटर्न पर आधारित 8 उच्च-स्तरीय गद्यांश व पद्यांश, समय प्रबंधन तकनीक, व्याकरण व भावार्थ प्रश्नों को 100% सटीकता से हल करने के सूत्र।'
  }
];

// 5. High-Yield Prompt Engineering for Sanskrit Content Generation
function buildSanskritPrompt(topic) {
  return `
You are India's foremost Sanskrit scholar, Paninian Grammarian, and UP Upper Primary Assistant Teacher (Super TET Junior) Exam Master Educator.
Create a masterclass, topper-grade, 100% comprehensive study module in PURE HINDI & SANSKRIT for:

TOPIC SLUG: "${topic.slug}"
TOPIC NUMBER: "${topic.numStr}"
SECTION: "${topic.secTitle}"
TOPIC TITLE: "${topic.title}"
CORE SYLLABUS FOCUS: "${topic.coreFocus}"

Target Audience: Aspirants preparing for UP Upper Primary Assistant Teacher (Class 6-8) Recruitment 2026 (संस्कृत भाषा एवं साहित्य - 90 Questions | 270 Marks | -1 Negative Marking).
Every concept must be pointwise, exhaustive, with exact Sanskrit Sutras (पाणिनीय सूत्राणि), accurate Vyakhyas, memory tricks, tips, comparative tables, and 10 exam-accurate practice MCQs.

Respond ONLY with a VALID JSON object adhering to the schema below (NO markdown backticks, no text before or after):
{
  "key_focus_summary": "2-3 concise Hindi sentences on exam importance, question weightage, and high-scoring strategy for this topic.",
  "mindmap": {
    "central_node": "${topic.shortTitle}",
    "branches": [
      {
        "title": "Branch 1 Title in Hindi/Sanskrit",
        "icon": "fas fa-font",
        "nodes": ["Point 1", "Point 2", "Point 3", "Point 4"]
      },
      {
        "title": "Branch 2 Title in Hindi/Sanskrit",
        "icon": "fas fa-book",
        "nodes": ["Point 1", "Point 2", "Point 3", "Point 4"]
      },
      {
        "title": "Branch 3 Title in Hindi/Sanskrit",
        "icon": "fas fa-code-branch",
        "nodes": ["Point 1", "Point 2", "Point 3", "Point 4"]
      },
      {
        "title": "Branch 4 Title in Hindi/Sanskrit",
        "icon": "fas fa-bolt",
        "nodes": ["Point 1", "Point 2", "Point 3", "Point 4"]
      }
    ]
  },
  "concepts": [
    {
      "heading": "1. मुख्य परिचय, पाणिनीय सूत्र एवं आधारभूत नियम",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>मूल सूत्र एवं परिभाषा:</strong> ...सूत्र सहित व्याख्या...</div><div class=\\"point-card\\"><strong>व्युत्पत्ति एवं शास्त्रीय विधान:</strong> ...नियम व उदाहरण...</div></div><div class=\\"tip-box\\"><strong><i class=\\"fas fa-lightbulb\\"></i> परीक्षा टिप:</strong> ...महत्वपूर्ण तथ्य...</div>"
    },
    {
      "heading": "2. प्रमुख भेद, सूत्र विश्लेषण एवं व्यावहारिक उदाहरण",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>प्रमुख भेद व लक्षण:</strong> ...विस्तृत बिंदुवार व्याख्या...</div><div class=\\"point-card\\"><strong>मानक उदाहरण एवं विग्रह:</strong> ...उदाहरणाणि...</div></div><div class=\\"trick-box\\"><strong><i class=\\"fas fa-magic\\"></i> पहचान ट्रिक:</strong> ...शॉर्टकट पहचान नियम...</div>"
    },
    {
      "heading": "3. विशिष्ट अपवाद, वार्तिक नियम एवं सूक्ष्म भेद",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>वार्तिक एवं अपवाद:</strong> ...कात्यायन वार्तिक व अपवाद...</div><div class=\\"point-card\\"><strong>भ्रम निवारण:</strong> ...समान लगने वाले रूपों में अंतर...</div></div><div class=\\"mnemonic-inline-box\\"><strong>स्मरण सूत्र:</strong> <code>...याद रखने का कोड...</code> ...स्पष्टीकरण...</div>"
    },
    {
      "heading": "4. UP शिक्षक भर्ती विगत वर्ष विश्लेषण एवं उच्च अंक सूत्र",
      "html_content": "<div class=\\"point-grid\\"><div class=\\"point-card\\"><strong>PYQ ट्रेंड्स:</strong> ...पिछले वर्षों में पूछे गए प्रश्न प्रारूप...</div><div class=\\"point-card\\"><strong>सटीक समाधान रणनीति:</strong> ...100% एक्यूरेसी के नियम...</div></div>"
    }
  ],
  "comparative_table": {
    "title": "तुलनात्मक सारणी एवं मुख्य परीक्षा भेद",
    "headers": ["क्रम / भेद", "लक्षण / सूत्र", "उदाहरण", "विशेष परीक्षा बिन्दु"],
    "rows": [
      ["1. ...", "...", "...", "..."],
      ["2. ...", "...", "...", "..."],
      ["3. ...", "...", "...", "..."],
      ["4. ...", "...", "...", "..."],
      ["5. ...", "...", "...", "..."]
    ]
  },
  "mcqs": [
    {
      "question": "प्रमाणिक संस्कृत प्रश्न 1 (UP Super TET Junior स्तर का)?",
      "options": [
        "A) विकल्प 1",
        "B) विकल्प 2",
        "C) विकल्प 3",
        "D) विकल्प 4"
      ],
      "correct_index": 0,
      "explanation": "विस्तृत पाणिनीय सूत्र एवं सन्दर्भ सहित व्याख्या, जिससे 3 अन्य प्रश्न भी तैयार हों।"
    }
    // Exactly 10 questions total (index 0 to 9)
  ],
  "revision_facts": [
    "तथ्य 1: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 2: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 3: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 4: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 5: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 6: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 7: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 8: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 9: ...अत्यंत महत्वपूर्ण तथ्य...",
    "तथ्य 10: ...अत्यंत महत्वपूर्ण तथ्य..."
  ],
  "mnemonics": [
    {
      "title": "स्मरण सूत्र 1 (संक्षिप्त mnemonic)",
      "quote": "स्मरण श्लोक / सूत्र / mnemonic",
      "explanation": "इस सूत्र का अर्थ एवं याद रखने की आसान विधि।"
    },
    {
      "title": "स्मरण सूत्र 2 (पहचान ट्रिक)",
      "quote": "पहचान कोड / तुकबंदी",
      "explanation": "परीक्षा कक्ष में 5 सेकंड में उत्तर खोजने का तरीका।"
    },
    {
      "title": "स्मरण सूत्र 3 (अपवाद निवारण)",
      "quote": "अपवाद स्मरण कोड",
      "explanation": "अपवादों को कभी न भूलने का वैज्ञानिक तरीका।"
    }
  ],
  "exam_traps": [
    {
      "title": "परीक्षा जाल 1: सामान्य भ्रम जहाँ 80% छात्र अंक गँवाते हैं",
      "description": "समान दिखने वाले पदों में अन्तर तथा सही उत्तर तक पहुँचने की विधि।"
    },
    {
      "title": "परीक्षा जाल 2: विभक्ति / लकार / प्रत्यय का सूक्ष्म धोखा",
      "description": "मात्रा अथवा इत्संज्ञा लोप से होने वाली भ्रामक गलतियाँ।"
    },
    {
      "title": "परीक्षा जाल 3: प्रश्न में 'न अस्ति' या 'असत्यम्' न पढ़ना",
      "description": "नकारात्मक प्रश्नों में सही विकल्प चुनने की सतर्कता।"
    }
  ],
  "mastery_checklist": [
    "इस विषय से संबंधित सभी पाणिनीय सूत्र, उनके अर्थ और मानक उदाहरण मुझे कंठस्थ हैं।",
    "विगत वर्षों में UP शिक्षक भर्ती व TET में आए इस टॉपिक के सभी प्रश्न मैंने बिना गलती के हल कर लिए हैं।",
    "सभी 10 अभ्यास प्रश्नों के उत्तर एवं व्याख्या को आत्मसात कर लिया है तथा परीक्षा जाल से सतर्क हूँ।"
  ]
}
`.trim();
}

// 6. Page Rendering Engine (Pure Hindi, Common CSS/JS, No Footer, Dark Mode Ready)
function renderSanskritPage(topic, data, prevTopic, nextTopic) {
  const canonicalUrl = `${DOMAIN}/up-upper-primary-teacher/sanskrit/${topic.slug}/`;
  const pageTitle = `${topic.title} नोट्स, ट्रिक्स एवं अभ्यास | UP Junior Super TET Sanskrit | SJMaths`;
  const metaDesc = `UP Upper Primary Assistant Teacher 2026 संस्कृत भाषा एवं साहित्य: ${topic.title} के बिन्दुवार नोट्स, माइंडमैप, तुलनात्मक तालिका, स्मरण सूत्र (Mnemonics), 10 अभ्यास प्रश्न एवं मिनी टेस्ट।`;

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
                        <i class="fas fa-om"></i>
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
  if (data.comparative_table && data.comparative_table.headers && data.comparative_table.rows) {
    const tableData = data.comparative_table;
    const ths = tableData.headers.map(h => `<th>${esc(h)}</th>`).join('');
    const trs = tableData.rows.map(row => {
      const tds = (Array.isArray(row) ? row : Object.values(row)).map(c => `<td>${esc(c)}</td>`).join('');
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
                <span class="mcq-exam-pill"><i class="fas fa-graduation-cap"></i> Super TET Junior संस्कृत</span>
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

  // Render Revision Facts
  let factsHtml = '';
  (data.revision_facts || []).forEach((f, fIdx) => {
    factsHtml += `
            <div class="revision-fact-row">
                <span class="fact-num-badge">#${fIdx + 1}</span>
                <span>${esc(f)}</span>
            </div>`;
  });

  // Render Mnemonics
  let mnemonicsHtml = '';
  (data.mnemonics || []).forEach(m => {
    mnemonicsHtml += `
            <div class="mnemonic-card">
                <h3 style="font-size: 1.05rem; font-weight: 800; color: var(--text-headline); margin: 0 0 0.5rem 0;">
                    <i class="fas fa-lightbulb" style="color: var(--brand-emerald);"></i> ${esc(m.title)}
                </h3>
                <div class="mnemonic-quote-box">${esc(m.quote)}</div>
                <p style="margin: 0; font-size: 0.9rem; color: var(--text-sub); line-height: 1.6;">${esc(m.explanation)}</p>
            </div>`;
  });

  // Render Exam Traps
  let trapsHtml = '';
  (data.exam_traps || []).forEach(tr => {
    trapsHtml += `
            <div class="trap-card-item">
                <i class="fas fa-triangle-exclamation" style="font-size: 1.25rem; flex-shrink: 0; margin-top: 2px;"></i>
                <div>
                    <strong style="display: block; font-size: 0.98rem; margin-bottom: 0.25rem;">${esc(tr.title)}</strong>
                    <span>${esc(tr.description)}</span>
                </div>
            </div>`;
  });

  // Render Self-Assessment Checklist
  let checklistHtml = '';
  (data.mastery_checklist || []).forEach((item, cIdx) => {
    checklistHtml += `
        <label class="mastery-check-item">
            <input type="checkbox" id="chk-mastery-${cIdx}" class="custom-check" onchange="updateMasteryProgress()">
            <span>${esc(item)}</span>
        </label>`;
  });

  // Navigation Links
  const prevLink = prevTopic
    ? `<a href="/up-upper-primary-teacher/sanskrit/${prevTopic.slug}/" class="topic-nav-btn prev-btn"><i class="fas fa-chevron-left"></i> <span>पिछला: ${esc(prevTopic.shortTitle)}</span></a>`
    : `<span class="topic-nav-btn prev-btn disabled"><i class="fas fa-chevron-left"></i> <span>प्रथम अध्याय</span></span>`;

  const nextLink = nextTopic
    ? `<a href="/up-upper-primary-teacher/sanskrit/${nextTopic.slug}/" class="topic-nav-btn next-btn"><span>अगला: ${esc(nextTopic.shortTitle)}</span> <i class="fas fa-chevron-right"></i></a>`
    : `<span class="topic-nav-btn next-btn disabled"><span>अंतिम अध्याय</span> <i class="fas fa-chevron-right"></i></span>`;

  return `<!DOCTYPE html>
<html lang="hi">
<head>
<script async="" crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829"></script>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>${esc(pageTitle)}</title>
<meta content="${esc(topic.title)}, संस्कृत भाषा एवं साहित्य, UP Upper Primary Teacher, Class 6-8 Teacher Syllabus, Super TET Junior Notes, UP Assistant Teacher, SJMaths" name="keywords"/>
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
<meta content="${esc(pageTitle)}" name="twitter:title"/>
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
<link href="/assets/css/up-upper-primary-topic.min.css?v=20261002_02" rel="stylesheet"/>

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
      "name": "Sanskrit",
      "item": "https://sjmaths.com/up-upper-primary-teacher/sanskrit/"
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
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.documentElement.classList.add('dark-mode');
            document.documentElement.setAttribute('data-theme', 'dark');
        } else {
            document.documentElement.classList.remove('dark-mode');
            document.documentElement.setAttribute('data-theme', 'light');
        }
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
    (function () {
        const sjDark = localStorage.getItem('sjmaths-dark');
        const legacyTheme = localStorage.getItem('theme');
        const isDark = sjDark === 'on' || (sjDark === null && legacyTheme === 'dark') || (sjDark === null && legacyTheme === null && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches);
        if (isDark) {
            document.body.classList.add('dark-mode');
        } else {
            document.body.classList.remove('dark-mode');
        }
    })();
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
            <a href="/up-upper-primary-teacher/sanskrit/">संस्कृत पाठ्यक्रम</a>
            <i class="fas fa-chevron-right" style="font-size: 0.7rem;"></i>
            <span>${esc(topic.numStr)}</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.75rem; flex-wrap: wrap;">
            <a href="/up-upper-primary-teacher/sanskrit/" class="back-hub-btn">
                <i class="fas fa-arrow-left"></i>
                <span>मुख्य संस्कृत हब</span>
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
            <span class="subject-tag-pill">खण्ड ${topic.secIdx}: ${esc(topic.secTitle)}</span>
            <span class="subject-tag-pill">कक्षा 6–8 शिक्षक भर्ती</span>
        </div>
        <h1>
            <span>${esc(topic.title)}</span>
        </h1>
        <div class="topic-hero-subtitle">
            <span>UP उच्च प्राथमिक सहायक अध्यापक भर्ती परीक्षा 2026 (Super TET Junior)</span>
        </div>
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
                <strong style="color: var(--text-headline); font-size: 1.05rem;">परीक्षा मानक अभ्यास प्रश्नोत्तरी (10 MCQs)</strong>
                <p style="margin: 3px 0 0 0; font-size: 0.85rem; color: var(--text-muted);">विगत वर्षों के UP शिक्षक भर्ती पैटर्न पर आधारित प्रश्न व्याख्या सहित हल करें।</p>
            </div>
            <div class="practice-score-badge" id="practiceScoreDisplay">स्कोर: 0 / ${data.mcqs.length}</div>
        </div>

        ${mcqsHtml}
    </div>

    <!-- ==================== TAB 3: TIMED MINI TEST ==================== -->
    <div class="study-tab-pane" id="tab-test">
        <div class="prep-card">
            <div id="testIntroScreen" class="mini-test-intro">
                <i class="fas fa-stopwatch" style="font-size: 3rem; color: var(--brand-emerald); margin-bottom: 1rem;"></i>
                <h2 style="justify-content: center; border: none; margin-bottom: 0.5rem;">संस्कृत गति एवं यथार्थता मिनी टेस्ट (Speed &amp; Accuracy Test)</h2>
                <p class="test-desc">यह 5 मिनट का वास्तविक समयबद्ध टेस्ट है जिसमें 10 बहुविकल्पीय प्रश्न हैं। UP Super TET Junior परीक्षा के -1 नकारात्मक अंकन नियम का अभ्यास करें।</p>
                <div class="test-stats-row">
                    <span class="test-stat-chip"><i class="fas fa-question-circle"></i> प्रश्न: 10</span>
                    <span class="test-stat-chip"><i class="fas fa-clock"></i> समय: 5 मिनट (300s)</span>
                    <span class="test-stat-chip"><i class="fas fa-award"></i> पूर्णांक: 30 अंक</span>
                    <span class="test-stat-chip"><i class="fas fa-minus-circle" style="color: #dc2626;"></i> नकारात्मक अंकन: -1</span>
                </div>
                <button type="button" class="start-test-btn" onclick="startMiniTest()">
                    <i class="fas fa-play"></i>
                    <span>टेस्ट प्रारम्भ करें (Start Test)</span>
                </button>
            </div>

            <div id="testActiveScreen" style="display: none;">
                <div class="test-timer-bar">
                    <div>
                        <span style="font-size: 0.85rem; color: var(--text-muted);">अवशिष्ट समय (Time Remaining)</span>
                        <div class="test-countdown" id="testTimerText"><i class="fas fa-clock"></i> 05:00</div>
                    </div>
                    <button type="button" class="test-submit-btn" onclick="submitMiniTest()">
                        <i class="fas fa-paper-plane"></i>
                        <span>टेस्ट जमा करें (Submit Test)</span>
                    </button>
                </div>

                <div id="testQuestionsContainer"></div>

                <div class="test-nav-controls">
                    <button type="button" class="test-btn-nav" id="btnPrevTestQ" onclick="navigateTestQuestion(-1)">
                        <i class="fas fa-chevron-left"></i> पिछला प्रश्न
                    </button>
                    <span id="testQIndexIndicator" style="font-weight: 700; color: var(--text-sub);">1 / 10</span>
                    <button type="button" class="test-btn-nav" id="btnNextTestQ" onclick="navigateTestQuestion(1)">
                        अगला प्रश्न <i class="fas fa-chevron-right"></i>
                    </button>
                </div>
            </div>

            <div id="testResultScreen" style="display: none; text-align: center; padding: 2rem 1rem;">
                <i class="fas fa-trophy" style="font-size: 3.5rem; color: #f59e0b; margin-bottom: 1rem;"></i>
                <h2 style="justify-content: center; border: none; margin-bottom: 0.5rem;">टेस्ट परिणाम पत्रक (Test Scorecard)</h2>
                <div style="font-size: 2.5rem; font-weight: 900; color: var(--brand-emerald); margin-bottom: 0.5rem;" id="finalScoreVal">0 / 30</div>
                <p id="testAccuracySummary" style="font-size: 1rem; color: var(--text-sub); margin-bottom: 1.5rem;"></p>
                <div id="testDetailedBreakdown" style="text-align: left; margin-top: 2rem;"></div>
                <button type="button" class="retry-test-btn" onclick="restartMiniTest()" style="margin-top: 1.5rem;">
                    <i class="fas fa-redo"></i> पुनः टेस्ट दें (Retake Test)
                </button>
            </div>
        </div>
    </div>

    <!-- ==================== TAB 4: REVISION & EXAM TRAPS ==================== -->
    <div class="study-tab-pane" id="tab-revision">
        <div class="prep-card">
            <h2>
                <i class="fas fa-bolt" style="color: #f59e0b;"></i>
                <span>त्वरित परीक्षा तथ्य (10 High-Yield Exam Facts)</span>
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
    const TOPIC_STORAGE_KEY = 'up-upper-primary-teacher-checklist-v2';
    const TOPIC_CHECKBOX_ID = '${topic.chkId}';
    const testData = ${testDataJson};
</script>
<script data-cfasync="false" defer="" src="/assets/js/up-upper-primary-topic.min.js?v=20261002_02"></script>
<script data-cfasync="false" defer="" src="/assets/js/search.min.js?v=a16d370a"></script>
<script data-cfasync="false" defer="" src="/assets/js/main.min.js?v=1594eda0"></script>
<script data-cfasync="false" defer="" src="/assets/js/global-header.min.js?v=d48c181a"></script>
<script src="/assets/js/require-auth.min.js?v=3060658c" type="module"></script>
</body>
</html>
`;
}

// 7. Generation Orchestrator
async function generateSanskritTopicContent(topic) {
  const prompt = buildSanskritPrompt(topic);
  let lastErr = null;

  for (let attempt = 0; attempt < 8; attempt++) {
    const config = getActiveConfig();
    const ai = new GoogleGenAI({ apiKey: config.key });

    for (const model of config.models) {
      try {
        console.log(`    [Attempt ${attempt + 1}] Invoking Gemini API [${config.name} | ${model}] for: ${topic.slug}`);
        const response = await ai.models.generateContent({
          model,
          contents: prompt,
          config: {
            responseMimeType: 'application/json',
            temperature: 0.3
          }
        });

        const rawText = response.text;
        if (!rawText) throw new Error('Empty response received from model');

        let parsed;
        try {
          parsed = JSON.parse(rawText);
        } catch (e) {
          const repaired = jsonrepair(rawText);
          parsed = JSON.parse(repaired);
        }

        // Validate critical keys
        if (!parsed.concepts || !parsed.mcqs || parsed.mcqs.length < 5) {
          throw new Error(`Incomplete JSON payload (concepts: ${parsed.concepts?.length}, mcqs: ${parsed.mcqs?.length})`);
        }

        return parsed;
      } catch (err) {
        lastErr = err;
        console.warn(`    [Warning] ${config.name}/${model} failed on ${topic.slug}: ${err.message}`);
        // If rate limited or unavailable, wait briefly
        await new Promise(r => setTimeout(r, 1500));
      }
    }

    rotateKey();
    await new Promise(r => setTimeout(r, 2000));
  }

  throw new Error(`Exhausted all retries for topic: ${topic.slug}. Last error: ${lastErr?.message}`);
}

async function main() {
  console.log('================================================================');
  console.log('SJ Maths — UP Upper Primary Assistant Teacher (Class 6-8) Sanskrit');
  console.log(`Starting Sanskrit Syllabus Content Generator Engine`);
  console.log(`Total Topics Cataloged: ${SANSKRIT_TOPICS.length}`);
  console.log(`Active API Keys: ${KEY_CONFIGS.length} (${KEY_CONFIGS.map(k => k.name).join(', ')})`);
  console.log('================================================================\n');

  let targets = SANSKRIT_TOPICS;

  if (TARGET_SLUG) {
    targets = SANSKRIT_TOPICS.filter(t => t.slug === TARGET_SLUG);
    if (targets.length === 0) {
      console.error(`ERROR: Target topic slug "${TARGET_SLUG}" not found in catalog.`);
      process.exit(1);
    }
  } else if (LIMIT) {
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
        const data = await generateSanskritTopicContent(topic);
        const html = renderSanskritPage(topic, data, prevTopic, nextTopic);

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
