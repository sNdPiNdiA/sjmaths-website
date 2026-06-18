const fs = require('fs');
const path = require('path');

const RAW_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'raw');
const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const KEYWORDS_PATH = path.join(__dirname, 'config', 'category-keywords.json');

// Helper to match a keyword with safety for short words, acronyms, and Devanagari boundary awareness
function matchKeyword(text, keyword, originalText) {
  // If the keyword is written in ALL CAPS (like "WHO" or "UP"), perform case-sensitive matching on originalText
  const isAllCaps = /^[A-Z0-9\s]+$/.test(keyword) && keyword.length >= 2;

  const kw = isAllCaps ? keyword : keyword.toLowerCase();
  const txt = isAllCaps ? (originalText || '') : text.toLowerCase();

  const isEnglish = /^[a-zA-Z0-9\s]+$/.test(kw);
  if (isEnglish) {
    const escaped = kw.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    // Match strict word boundaries, allowing optional plural 's' or 'es'
    const regex = new RegExp('\\b' + escaped + '(?:s|es)?\\b', isAllCaps ? '' : 'i');
    return regex.test(txt);
  }

  // Devanagari Smart Matching
  const kwLower = kw.toLowerCase();
  const txtLower = txt.toLowerCase();
  if (kwLower === 'पहल') {
    return /पहल(?![ेाीु])/.test(txtLower);
  }

  if (kwLower === 'देश') {
    return /(?:^|[^\u0900-\u097F\w])देश/.test(txtLower);
  }

  if (kwLower.length <= 3) {
    const escaped = kwLower.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp('(?:^|[^\u0900-\u097F\w])' + escaped + '(?:$|[^\u0900-\u097F\w])', 'i');
    return regex.test(txtLower);
  }

  return txtLower.includes(kwLower);
}

// Helper to check negative keywords using word boundaries to avoid substring false matches
function matchNegativeKeyword(text, keyword) {
  const kw = keyword.toLowerCase();
  const txt = text.toLowerCase();

  // If Devanagari, enforce boundary checking to avoid false positives (e.g. "पति" matching "राष्ट्रपति")
  const isDevanagari = /[\u0900-\u097F]/.test(kw);
  if (isDevanagari) {
    const escaped = kw.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp('(?:^|[^\u0900-\u097F\w])' + escaped + '(?:$|[^\u0900-\u097F\w])', 'i');
    return regex.test(txt);
  }

  // Enforce word boundaries for English keywords/phrases (e.g. to prevent "reactor" from matching "actor")
  const isEnglish = /^[a-z0-9\s\-]+$/i.test(kw);
  if (isEnglish) {
    const escaped = kw.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
    const regex = new RegExp('\\b' + escaped + '(?:s|es)?\\b', 'i');
    return regex.test(txt);
  }

  return txt.includes(kw);
}

// Helper to get current date in YYYY-MM-DD IST
function getTodayIST() {
  const formatter = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'Asia/Kolkata',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
  return formatter.format(new Date());
}

function categorize() {
  const todayStr = process.argv[2] || getTodayIST();
  const todayDedupPath = path.join(RAW_DIR, `${todayStr}-deduped.json`);

  if (!fs.existsSync(PROCESSED_DIR)) {
    fs.mkdirSync(PROCESSED_DIR, { recursive: true });
  }
  const tempProcessedPath = path.join(PROCESSED_DIR, `${todayStr}-temp.json`);

  if (!fs.existsSync(todayDedupPath)) {
    console.log(`No deduped file found for today (${todayStr}). Nothing to categorize.`);
    fs.writeFileSync(tempProcessedPath, JSON.stringify([], null, 2), 'utf8');
    return;
  }

  let items = [];
  try {
    items = JSON.parse(fs.readFileSync(todayDedupPath, 'utf8'));
  } catch (err) {
    console.error(`Error reading ${todayDedupPath}:`, err.message);
    process.exit(1);
  }

  if (!fs.existsSync(KEYWORDS_PATH)) {
    console.error('Category keywords file not found at:', KEYWORDS_PATH);
    process.exit(1);
  }

  let keywordsConfig = {};
  try {
    keywordsConfig = JSON.parse(fs.readFileSync(KEYWORDS_PATH, 'utf8'));
  } catch (err) {
    console.error(`Error reading keywords config:`, err.message);
    process.exit(1);
  }

  console.log(`Loaded ${items.length} items to categorize.`);
  const categorizedItems = [];

  for (const item of items) {
    const titleLower = item.title.toLowerCase();
    const descLower = (item.description || '').toLowerCase();

    // Clean press conference terms to avoid false "वार्ता" international matches
    const titleCleaned = titleLower.replace(/प्रेसवार्ता/g, 'प्रेस_कांफ्रेंस').replace(/प्रेस वार्ता/g, 'प्रेस_कांफ्रेंस');
    const descCleaned = descLower.replace(/प्रेसवार्ता/g, 'प्रेस_कांफ्रेंस').replace(/प्रेस वार्ता/g, 'प्रेस_कांफ्रेंस');

    const sebiJunkPatterns = [
      'certificate no', 'certificate no.', 'order no', 'order no.', 'show cause notice', 'final order',
      'adjudication order', 'settlement order', 'recovery certificate', 'notice of demand', 'consent order',
      'enforcement order', 'penalty on', 'order in the matter of', 'appeal no', 'appeal no.', 'release order', 'corrigendum to order', 'illiquid stock'
    ];

    if (item.sourceId === 'sebi_notifications') {
      const fullText = `${titleCleaned} ${descCleaned}`;
      if (sebiJunkPatterns.some(pattern => fullText.includes(pattern))) {
        console.log(`Skipping SEBI notification junk item: "${item.title}"`);
        continue;
      }
    }

    // For priority 3 (newspapers), only scan title to prevent description boilerplate false matches
    const textToScan = item.priority === 3 ? titleCleaned : `${titleCleaned} ${descCleaned}`;
    const originalTextToScan = item.priority === 3 ? item.title : `${item.title} ${(item.description || '')}`;

    // Negative keyword filtering for exam relevance
    const negativeKeywords = [
      // SEBI / Adjudication / Individual Regulatory Actions
      "order under section", "final order", "settlement order", "show cause notice", "recovery certificate",
      "remittance advice", "notice of demand", "adjudication order", "inspection of", "consent order",
      "enforcement order", "penalty on", "compounding of", "order in the matter of",

      // Crime / Violence / Law & Order (Individual Incidents)
      "suicide", "murder", "accident", "minor injury", "collision", "arrested for", "stolen", "theft",
      "robbery", "contraband", "ganja seized", "smuggling", "caught with", "kills", "killed", "kidnap",
      "assault", "rape", "molestation", "firing", "police encounter", "gangster", "forgery", "cheat",
      "arrest", "jail", "extortion", "cyber fraud", "illegal liquor", "smuggler",
      "गिरफ्तार", "हादसा", "दुर्घटना", "हत्या", "कत्ल", "चोरी", "लूट", "बदमाश", "तस्करी", "जब्त किया", "अवैध शराब",
      "गिरफ्तारी", "मारी गई", "मारा गया", "मौत", "मृत्यु", "अपहरण", "लाश", "शव बरामद", "खूनी संघर्ष", "पीट-पीटकर",
      "फायर", "हमला", "अवैध", "दरिंदगी", "कुकृत्य", "दुष्कर्म", "बलात्कार", "गैंगरेप", "छेड़खानी", "पिस्तौल", "तमंचा", "कारतूस",
      "एनकाउंटर", "जेल भेजा", "धोखाधड़ी", "जालसाजी", "गैंगस्तर", "रिश्वत", "भ्रष्टाचार", "पकड़ा गया", "पकड़े गए",

      // Tabloid / Local political bickering / Protests / Small-scale disputes
      "सपा", "भाजपा", "कांग्रेस", "बसपा", "आरजेडी", "अखिलेश यादव", "राहुल गांधी", "मायावती", "प्रियंका गांधी", "तेजस्वी यादव",
      "हल्लाबोल", "धरना", "प्रदर्शन", "पुतला दहन", "भड़के", "फटकार", "ड्रामा", "टावर पर चढ़ा", "जबरन", "जमकर हंगामा", "बवाल",
      "विवाद", "बिकरी", "बिक्री", "अतिक्रमण", "ढाया", "सील्ड", "सील किया", "ठगी", "धोखाधड़ी", "रिश्वत", "भ्रष्टाचार",
      "जनता दर्शन", "जनता दरबार", "शिकायत", "पति", "पत्नी", "प्रेमी", "प्रेमिका", "ससुर", "सास", "बहू", "बॉयफ्रेंड", "गर्लफ्रेंड",
      "शादी", "निकाह", "तलाक", "divorce", "lok adalat", "लोक अदालत", "जिहादी", "बकरीद", "शंकराचार्य", "अविमुक्तेश्वरानंद",
      "जगद्गुरु", "साधु", "संत", "मस्जिद", "मंदिर", "मजहब", "मजहबी",

      // Weather forecasts (Routine/Local)
      "आज का मौसम", "मौसम विभाग", "बारिश के आसार", "येलो अलर्ट", "ऑरेंज अलर्ट", "रेड अलर्ट", "झमाझम बारिश",
      "weather forecast", "rain alert", "heat wave", "heatwave", "cold wave", "heavy rain", "thunderstorm",
      "weather update", "तापमान", "गर्मी", "आंधी", "तूफान", "ओले", "बारिश की चेतावनी", "बारिश का अलर्ट", "मौसम का तांडव",
      "मौसम का मिजाज", "मौसम का हाल", "मौसम अपडेट", "weather report", "तापमान में", "गर्मी से राहत", "गर्मी का सितम",
      "मौसम विभाग का अलर्ट", "मौसम विभाग की चेतावनी", "तापमान का",

      // Exam notifications / Admission / Results (Admin stuff, not GA content)
      "admit card", "result date", "answer key", "registration date", "exam date", "how to download",
      "city slip", "hall ticket", "counseling", "admission cut-off", "exam analysis", "cutoff",
      "एडमिट कार्ड", "रिजल्ट कब", "उत्तर कुंजी", "आंसर की", "रजिस्ट्रेशन", "परीक्षा तिथि", "कैसे डाउनलोड",
      "सिटी स्लिप", "प्रवेश परीक्षा", "कटऑफ", "काउंसिलिंग", "कैसा था पेपर", "पेपर का लेवल", "कैसा रहा पेपर",

      // Other minor local news indicators
      "यात्री जान लें", "टोल प्लाजा", "स्पीड निर्धारित", "टोल टैक्स", "रोडवेज bus", "बिजली गायब", "बिजली संकट",
      "news live", "news today live", "breaking news", "live news", "live updates", "live blog", "live update",
      "ताजा समाचार", "मुख्य समाचार", "ब्रेकिंग न्यूज़", "लाइव अपडेट", "लाइव ब्लॉग", "लाइव खबरें", "बड़ी खबरें",
      "मुख्य खबरें", "डीएम को दिया पत्र", "जांच की मांग", "व्यवधान डालने", "medhavi award", "medhavi awards",

      // Sports entertainment (non-policy)
      "ipl", "rcb", "csk", "kkr", "mi ", "srh", "dc ", "pbks", "gt ", "lsg",
      "fifa world cup 2026", "fifa world cup", "premier league", "bundesliga",
      "knee ligament", "weekend sports", "desk jobs to weekend",

      // Consumer product launches
      "launched:", "what changes in price", "range and features",
      "price starts at", "bookings open", "ex-showroom",

      // Daily forex/market micro-moves  
      "rupee falls", "rupee rises", "paise to close", "paise in early trade",
      "rupee in early trade", "sensex falls", "nifty falls", "sensex rises", "nifty rises",
      "market today", "stock market today",

      // Political party infighting / cabinet shuffles (no national policy)
      "cabinet expansion", "mlas take oath", "mlas sworn", "oath as ministers",
      "swearing-in ceremony", "meet party high command", "party high command",
      "organisational appointments", "bjp rejig", "congress rejig",
      "expels two mlas", "expels mla", "anti-party activities",
      "attack on abhishek", "abhishek banerjee", "victim of state-sponsored",
      "tmc workers hold protest", "tmc expels",

      // Personal health/lifestyle advice
      "knock knees", "postpartum preeclampsia", "inflammatory bowel",
      "home loan benefits for women", "how inflammatory bowel",
      "baby may be out", "risks might remain", "what mothers should know",
      "eco-anxiety", "emotional fatigue", "climate change is affecting mental health",
      "painting your home white", "what role does your money",
      "from desk jobs to weekend", "rise in knee",

      // Clickbait/emotional Artemis crew personal stories  
      "tears in space", "gets emotional", "surreal and profound",
      "shed light on space health", "astronauts describe their lunar",
      "gives scare moment", "breaks apollo 13", "crew reaches the moon as",
      "crew gets emotional", "howl at the moon",

      // Foreign domestic politics (not IR)
      "pro-trump candidate", "colombia presidential", "dhs green card",
      "u.s. takes step to halt nvidia", "eu wants to break up with u.s. tech",
      "after the ai binge", "companies balk at soaring bills",
      "nvidia launches windows laptop",

      // Wildlife sightings (not conservation policy)
      "cheetahs spotted near", "glimpses from kuno", "solar-driven water lift helps kuno",
      "kuno cheetahs spotted", "female cheetah dies of injuries",
      "zimbabwe to cull", "ban predatory pet fish",
      "elephants from mexico flee", "animals from mexico flee",
      "red panda cubs born",

      // MyGov contest announcements (not policy)
      "winner announcement", "photo contest", "selfie", "mini vlog contest",
      "logo design competition", "video storytelling contest",
      "through your selfie", "tell the story of",

      // Psychology/soft news masquerading as science
      "psychology says people who", "makes world a better place",
      "guntur residents leave their old clothes",
      "science snapshots",

      // Climate-anxiety/lifestyle
      "eco-anxiety to emotional", "affecting mental health",
      "precious metals in may", "mixed bag for precious metals",

      // Health individual conditions
      "veracyte genomic test", "breast cancer patients who can skip",
      "adolescent sexuality", "towards a dialogue on",

      // Non-exam/junk news added in refinement check
      "quote of the day", "proverb of the day", "quote of the Day",
      "easy breakfast recipes", "recipes to support", "recipes to weight-loss", "recipe of the day", "breakfast recipe",
      "tiffany trump",
      "dry days", "liquor shops to be closed",
      "champions league", "premier league", "arsenal fans", "barcelona",
      "eviction notice to", "eviction notice", "nitish kumar should be vacated", "rabri devi",
      "kapil sibal",
      "palaniswami",
      "suvendu adhikari", "abhishek banerjee", "tmc", "trinamool congress",
      "derivatives of", "adjudication order", "settlement order",
      "dermatologists warn", "salon botox", "botox",
      "science quiz", "holiday spots for the",
      "trauma survivor", "how to heal",
      "compensation rises", "ceo's compensation",
      "tesla launches", "model y", "humanoid robot optimus",
      "musk says", "spacex agreed only",
      "cockroach janta party", "cockroach janta",
      "appeal no.", "appeal no", "filed by",
      "layoff", "reddit", "looking for job", "resume was enough", "ex-employee", "job market", "looking for a job",
      "treasury bills", "treasury bill", "t-bill", "t-bills", "money market operations", "dated security", "dated securities",
      "sovereign gold bond", "redemption price", "redemption under sovereign", "auction of", "state government securities",
      "weekly statistical supplement", "bulletin weekly statistical", "limited departmental", "departmental competitive",
      "departmental exam", "summer internship", "internship programme", "internship program", "assesses mobile network",
      "quality of service", "network quality", "fuel, lpg supply", "stable in", "adequate fuel", "rozgar mela",
      "inaugurates seed godown", "visits fc", "visits club", "establishment day",
      "mrna vaccine", "mrna vaccines", "mcrna covid", "mcrna vaccine", "dr mccullough", "vaccine side effects", "blood clots surge", "hantavirus", " Tenerife ",
      "hostage", "hostages", "civilians held", "captors",
      "service centre for defence", "pensioners inaugurated", "defence pensioners", "sparsh service centre",
      "this startup was already", "investors bet on a", "venture capital funding", "series a funding",
      "ministerial berths", "berth", "seat sharing", "seat-sharing", "mlas demand", "ministerial berth",
      "to amend the constitution to remove", "impeachment", "impeach", " xinhua ", " xinhua reporter ",
      "building collapse", "sealing drive", "seal illegal structures", "illegal structures", "demolition drive",
      "supreme court notice to", "hc notice to", "high court notice to", "issued notice to", "seeks response from",
      "political suppression of",
      "ineligible for", "financial crisis", "irregularities in", "congress expresses concern", "slams dharmendra", "busy in jod-tod",
      "municipal corporation polls", "municipal corporation elections", "local body polls", "himachal municipal",
      "the hindu huddle", "huddle panel", "panel to throw light",
      "labour party wins", "malta", "parliamentary election in",
      "champions league", "premier league", "match updates", "batsman", "bowler", "wicket",
      "niveshak shivir", "investor camp",
      "a giant lake vanished", "octopuses tend to explore", "how to use 8 arms", "koalas from chlamydia", "chlamydia",
      "district collector", "collector promotes", "riding electric bike", "rides electric bike",
      "school reopens", "back to school", "school challenge", "welcomes students",
      "mango and jackfruit", "mela in", "jackfruit", "mango festival",
      "appoints new coach", "football club", "visits fc", "grassroots talent",
      "temple from", "brahmotsavam",
      "fire breaks out", "fire in building", "fire in office", "first respondents", "head constables", "constables reached", "fire: locals",
      "asks rabri devi", " bungalow", " bungalow ",
      "fake accounts", "fake account",
      "ott releases", "new movies and shows", "netflix", "k-dramas", "k-drama", "watch in", "ending explained",
      "google keyword ads",
      "pancreatic cancer", "pancreatic cancer drug",
      "supriya sule", "arun lakhani", "supriya sule's daughter",
      "t-hub", "innovation challenge", "humans are still evolving", "lead to casualties", "senate testimony",
      "hails pm modi", "bjp delhi chief", "hails pm", "condolence", "condolences", "passing of", "निधन", "शोक व्यक्त",
      "subhashit", "subhashitam", "सुभाषित", "collector", "जिलाधिकारी", "डीएम", "dm visit", "dm inspects",

      // Additional state-level politics & local elections (no exam relevance)
      "state assembly", "assembly polls", "assembly election", "state election", "vidhan sabha",
      "municipal corporation", "municipal body", "zilla parishad", "panchayat", "local body", "local elections",
      "mayor elected", "mayor resigned", "mla elected", "mla resigned", "cm sworn in", "cm meets",
      "rajya sabh seat", "rajya sabha seat", "seat distribution", "seat allocation", "seat sharing",
      "विधानसभा चुनाव", "स्थानीय चुनाव", "पंचायत चुनाव", "नगर निकाय", "सीएम की", "मुख्यमंत्री ने", "विधायक ने",
      "राज्य सरकार", "राज्य स्तर", "स्थानीय स्तर", "जिला स्तर", "तहसील", "प्रशासनिक व्यवस्था",

      // Entertainment & celebrity news (not policy)
      "bollywood", "hollywood", "movie release", "film release", "actor", "actress", "singer", "director",
      "divorce", "breakup", "dating", "relationship", "marriage", "wedding", "engagement",
      "reality show", "reality tv", "celebrity gossip", "celebrity news", "celebrity interview",
      "award show", "award ceremony", "award night", "winners list", "nominations",
      "film festival", "movie premiere", "box office", "box office collections",
      "राज्य पुरस्कार", "राज्य सम्मान", "फिल्म", "गीत", "गायक", "अभिनेता", "अभिनेत्री",

      // Sports (non-policy, entertainment focus)
      "cricket match", "football match", "tennis match", "rugby", "hockey match",
      "player interview", "player injured", "player suspended", "coach fired",
      "world cup qualifier", "tournament", "championship", "league match",
      "और जीते", "और हारे", "स्कोर है", "रन बनाए", "विकेट गिरे",

      // Personal legal/family matters (non-policy)
      "divorce settlement", "custody battle", "child support", "alimony",
      "civil suit", "property dispute", "inheritance", "will reading",
      "family feud", "family dispute", "property fight", "boundary dispute",

      // Micro-local infrastructure (not policy)
      "road pothole", "pothole", "streetlight broken", "sewer overflow",
      "garbage pile", "waste management issue", "water supply problem",
      "traffic jam", "traffic congestion", "commute issues",
      "सड़क खराब", "बिजली कटौती", "पानी की कमी", "सीवर साफ", "कचरा", "ट्रैफिक",

      // Personal finance/consumer complaints (not policy)
      "cheated by bank", "atm fraud", "credit card fraud", "loan scam",
      "fake ids sold", "counterfeit currency", "investment scam",
      "शिकार", "ठग", "धोखे", "अपराध", "अवैध",

      // Industry-specific layoffs and micro-stories (not macro policy)
      "company layoffs", "job cuts", "staff reduction", "workforce reduction",
      "startup shutdown", "startup closure", "company failure",
      "कंपनी ने निकाला", "नौकरी से निकाले", "निकले हुए", "बंद किया", "असफल",

      // Personality-driven news (not policy)
      "entrepreneur interview", "startup founder", "business tycoon", "industrialist says",
      "tech billionaire", "richest person", "wealth ranking",

      // Quasi-judicial/administrative orders about individuals (not policy)
      "ias officer", "ips officer", "suspended", "transferred", "posted to",
      "deputation", "secondment", "leave", "retirement", "pension",
      "आईएएस", "आईपीएस", "निलंबित", "स्थानांतरित", "सेवा निवृत्ति",

      // Real estate & property (not policy)
      "property price up", "property price down", "realty news", "real estate news",
      "housing market", "apartment", "residential project", "commercial space",
      "land deal", "land acquisition", "land grab",
      "संपत्ति", "प्रॉपर्टी", "जमीन", "मकान", "आवास",

      // Niche academic/research without policy impact
      "researcher finds", "study shows", "survey reveals", "research reveals",
      "university study", "college research", "academic findings",
      "खोज", "अनुसंधान", "शोध", "विश्वविद्यालय",

      // Tourism & travel (not policy)
      "tourist destination", "travel guide", "travel tips", "vacation spot",
      "hotel review", "restaurant review", "travel review",
      "यात्रा", "पर्यटन", "होटल", "रेस्तरां", "अवकाश",

      // Lottery results, prize announcements (not exam-relevant)
      "lottery result", "lottery results", "prize winning number", "lottery prize",
      "karunya plus", "karunya lottery", "winning number", "lottery today",
      "लॉटरी", "लॉटरी रिजल्ट", "पुरस्कार संख्या", "लकी ड्रॉ",
      "₹1 crore prize", "rs 1 crore prize", "cash reward", "winning ticket"
    ];

    let hasNegativeKeyword = false;
    for (const neg of negativeKeywords) {
      if (matchNegativeKeyword(textToScan, neg)) {
        hasNegativeKeyword = true;
        break;
      }
    }

    if (hasNegativeKeyword) {
      console.log(`Skipping non-exam-related item (negative keyword matched): "${item.title}"`);
      continue;
    }

    // For Priority 2 and 3 items, check for at least one exam relevance keyword
    if (item.priority > 1) {
      const examRelevanceKeywords = [
        "policy", "scheme", "yojana", "yojna", "mission", "summit", "conclave", "bilateral", "agreement", "mou", "fta", "pact", "treaty", "alliance",
        "launch", "satellite", "spacecraft", "isro", "drdo", "missile", "military exercise", "joint exercise", "exercise", "appoint", "sworn",
        "chairman", "ceo", "cmd", "governor", "chief justice", "judge", "award", "prize", "nobel", "padma", "ratna", "index", "ranking",
        "report", "survey", "budget", "gdp", "gst", "inflation", "deficit", "fiscal", "parliament", "bill", "act", "law", "commission",
        "supreme court", "high court", "constitutional", "amendment", "brics", "g20", "asean", "un ", "who", "unesco", "imf", "world bank",
        "cop28", "cop29", "cop30", "conservation", "wetland", "reserve", "sanctuary", "national park", "biodiversity", "climate", "emissions",
        "inaugurate", "commissioned", "criticality", "reactor", "supercomputer", "quantum", "vaccine", "outbreak", "eliminate", "declaration",
        "dialogue", "forum", "phf", "nfhs", "cpi", "iip", "wpi", "repo rate", "monetary policy",

        "योजना", "नीति", "अभियान", "पहल", "मिशन", "शिखर सम्मेलन", "द्विपक्षीय", "समझौता", "संधि", "एमओयू", "सहमति", "लॉन्च", "उपग्रह", "सैटेलाइट",
        "इसरो", "डीआरडीओ", "मिसाइल", "सैन्य अभ्यास", "नियुक्त", "अध्यक्ष", "निदेशक", "राज्यपाल", "मुख्य न्यायाधीश", "न्यायाधीश", "शपथ",
        "पुरस्कार", "सम्मान", "नोबेल", "पद्म", "रत्न", "विजेता", "सूचकांक", "इंडेक्स", "रैंकिंग", "रिपोर्ट", "सर्वेक्षण", "बजट", "जीडीपी",
        "जीएसटी", "मुद्रास्फीति", "घाटा", "राजकोषीय", "संसद", "विधेयक", "कानून", "आयोग", "सर्वोच्च न्यायालय", "सुप्रीम कोर्ट", "उच्च न्यायालय",
        "संवैधानिक", "संशोधन", "संयुक्त राष्ट्र", "डब्ल्यूएचओ", "यूनेस्को", "विश्व बैंक", "आईएमएफ", "संरक्षण", "अभयारण्य", "राष्ट्रीय उद्यान",
        "जलवायु", "उत्सर्जन", "उद्घाटन", "शुरू", "वैश्विक", "घोषणा", "वार्ता", "मंच", "परियोजना", "स्थापना दिवस"
      ];

      let relevanceKeywordCount = 0;
      for (const kw of examRelevanceKeywords) {
        if (matchKeyword(textToScan, kw, originalTextToScan)) {
          relevanceKeywordCount++;
        }
      }

      if (relevanceKeywordCount < 1) {
        console.log(`Skipping non-exam-related item (no exam relevance keyword found): "${item.title}"`);
        continue;
      }
    }

    const matchedCategories = [];
    let totalPrimaryMatches = 0;
    let totalSecondaryMatches = 0;

    for (const [catName, config] of Object.entries(keywordsConfig)) {
      let isMatched = false;
      let primaryMatches = 0;
      let secondaryMatches = 0;

      // 1. Check source hints (support prefix/infix match like "who_english" matching "who")
      const isSourceHint = config.source_hints && config.source_hints.some(hint =>
        item.sourceId === hint ||
        item.sourceId.startsWith(hint + '_') ||
        item.sourceId.includes('_' + hint)
      );
      if (isSourceHint) {
        isMatched = true;
      }

      // 2. Check primary keywords
      if (config.primary) {
        for (const word of config.primary) {
          if (matchKeyword(textToScan, word, originalTextToScan)) {
            primaryMatches++;
            totalPrimaryMatches++;
          }
        }
      }

      // 3. Check secondary keywords
      if (config.secondary) {
        for (const word of config.secondary) {
          if (matchKeyword(textToScan, word, originalTextToScan)) {
            secondaryMatches++;
            totalSecondaryMatches++;
          }
        }
      }

      // Categorization criteria:
      // - Source hint match, OR
      // - At least one primary keyword match, OR
      // - At least two secondary keyword matches
      if (isMatched || primaryMatches > 0 || secondaryMatches >= 2) {
        matchedCategories.push(catName);
      }
    }

    // Skip if no category matched (helps filter out junk local news/non-exam material)
    if (matchedCategories.length === 0) {
      console.log(`Skipping non-exam-related item (no categories matched): "${item.title}"`);
      continue;
    }

    // Compute Importance Score
    // - "high" if:
    //   - item matches multiple primary keywords, OR
    //   - item's source is high priority (1) AND matches at least one primary keyword
    // - "medium" if:
    //   - matches at least one primary keyword, OR
    //   - matches multiple secondary keywords (>= 3)
    // - "low" otherwise
    let importance = 'low';
    if (totalPrimaryMatches >= 2 || (item.priority === 1 && totalPrimaryMatches >= 1)) {
      importance = 'high';
    } else if (totalPrimaryMatches >= 1 || totalSecondaryMatches >= 3) {
      importance = 'medium';
    }

    // Extract matched keywords for metadata
    const keywordsFound = [];
    for (const [catName, config] of Object.entries(keywordsConfig)) {
      if (matchedCategories.includes(catName)) {
        if (config.primary) {
          config.primary.forEach(word => {
            if (matchKeyword(textToScan, word, originalTextToScan) && !keywordsFound.includes(word)) {
              keywordsFound.push(word);
            }
          });
        }
      }
    }

    categorizedItems.push({
      ...item,
      categories: matchedCategories,
      importance,
      keywords: keywordsFound.slice(0, 8) // Limit to top 8 keywords
    });
  }

  fs.writeFileSync(tempProcessedPath, JSON.stringify(categorizedItems, null, 2), 'utf8');
  console.log(`Categorization complete. Saved ${categorizedItems.length} items with temporary tags to ${tempProcessedPath}`);
}

categorize();

