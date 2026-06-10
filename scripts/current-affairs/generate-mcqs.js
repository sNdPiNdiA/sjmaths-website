const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const MCQS_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'mcqs');

function ensureDir(dirPath) {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
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

// Distractors dictionary to generate options
const DISTRACTORS = {
  science: ['NASA', 'ESA', 'Roscosmos', 'JAXA', 'CNSA', 'ISRO', 'DRDO', 'CSIR'],
  appointments: ['Sanjay Kumar', 'Amitabh Kant', 'Urjit Patel', 'Alok Sharma', 'Rajesh Verma', 'Vinay Mohan Kwatra', 'S. Somanath', 'Samir V. Kamat'],
  awards: ['Padma Vibhushan', 'Bharat Ratna', 'Nobel Prize', 'Abel Prize', 'Booker Prize', 'Pulitzer Prize', 'Khel Ratna', 'Sahitya Akademi Award'],
  sports: ['India', 'Australia', 'England', 'South Africa', 'New Zealand', 'Pakistan', 'Sri Lanka', 'Bangladesh'],
  economy: ['Reserve Bank of India (RBI)', 'Securities and Exchange Board of India (SEBI)', 'NABARD', 'NITI Aayog', 'Ministry of Finance', 'World Bank', 'IMF'],
  schemes: ['PM-KISAN', 'PM-Awas Yojana', 'Ayushman Bharat', 'PM-PRANAM', 'PM-Garib Kalyan', 'Atal Pension Yojana', 'Stand-up India', 'Startup India'],
  environment: ['COP27', 'COP28', 'COP29', 'COP30', 'United Nations Environment Programme (UNEP)', 'Green Climate Fund', 'IPCC', 'IUCN'],
  general: ['Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata', 'Hyderabad', 'Lucknow', 'Ahmedabad']
};

function getRandomItems(arr, count, exclude = []) {
  const filtered = arr.filter(item => !exclude.includes(item));
  const shuffled = [...filtered].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
}

// Build a single MCQ based on news article
function generateMCQ(item, index, dateStr) {
  const title = item.title;
  const desc = item.description || '';
  const primaryCat = item.categories[0] || 'general';
  
  let question = '';
  let options = [];
  let correctAnswerIdx = 0;
  let explanation = '';
  let difficulty = 'easy';

  // Lowercase versions for matching
  const titleLower = title.toLowerCase();
  const descLower = desc.toLowerCase();

  // Rule-based Template matching
  if (item.categories.includes('appointments')) {
    // Look for name who is appointed
    // Standard pattern: "X appointed as Y" or "X takes charge as Y"
    const match = title.match(/([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:appointed|takes charge|assumes charge|sworn in|named)\s+as\s+([^,.]+)/i);
    if (match) {
      const name = match[1];
      const position = match[2];
      question = `Who has been appointed as the ${position.trim()}?`;
      
      const incorrect = getRandomItems(DISTRACTORS.appointments, 3, [name]);
      options = [name, ...incorrect];
      explanation = `${name} has been appointed as the ${position.trim()}. ${desc}`;
      difficulty = 'moderate';
    }
  } 
  
  if (!question && item.categories.includes('awards')) {
    // Award pattern: "X wins Y" or "Y conferred on X"
    const match = title.match(/([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3})\s+(?:wins|conferred|honoured|receives|awarded)\s+([^,.]+)/i);
    if (match) {
      const name = match[1];
      const award = match[2];
      question = `Who was conferred with the ${award.trim()}?`;
      
      const incorrect = getRandomItems(DISTRACTORS.appointments, 3, [name]);
      options = [name, ...incorrect];
      explanation = `${name} received the ${award.trim()}. ${desc}`;
      difficulty = 'moderate';
    }
  }

  if (!question && item.categories.includes('science')) {
    // Science patterns: "ISRO launches X" or "NASA launches X"
    const launchMatch = title.match(/(ISRO|NASA|ESA|DRDO)\s+(?:successfully\s+)?(?:launches|conducts|tests)\s+([^,.]+)/i);
    if (launchMatch) {
      const org = launchMatch[1];
      const project = launchMatch[2];
      question = `Which organization developed or launched the '${project.trim()}'?`;
      
      const incorrect = getRandomItems(DISTRACTORS.science, 3, [org]);
      options = [org, ...incorrect];
      explanation = `${org} conducted/launched ${project.trim()}. ${desc}`;
      difficulty = 'easy';
    }
  }

  if (!question && item.categories.includes('schemes')) {
    // Scheme pattern: "Government launches X scheme"
    const schemeMatch = title.match(/(?:launches|announces|approves)\s+new\s+([^,.]+)\s+scheme/i);
    if (schemeMatch) {
      const scheme = schemeMatch[1];
      question = `Which government program or scheme was recently launched/updated to support its goals?`;
      
      const correct = scheme.includes('PM-') ? scheme : `PM-${scheme}`;
      const incorrect = getRandomItems(DISTRACTORS.schemes, 3, [correct]);
      options = [correct, ...incorrect];
      explanation = `The scheme '${scheme}' was launched. ${desc}`;
      difficulty = 'moderate';
    }
  }

  // Fallback: Default templates for categories if specific regex fails
  if (!question) {
    if (item.categories.includes('sports')) {
      question = `Which country or player won/was associated with the sports event: '${title}'?`;
      const correctOption = title.match(/(India|Australia|England|Yogi Adityanath)/i) ? title.match(/(India|Australia|England)/i)[0] : 'India';
      const incorrect = getRandomItems(DISTRACTORS.sports, 3, [correctOption]);
      options = [correctOption, ...incorrect];
      explanation = `Regarding sports events: ${title}. ${desc}`;
      difficulty = 'easy';
    } else if (item.categories.includes('up_special')) {
      question = `Which state/city is associated with: '${title}'?`;
      const correctOption = titleLower.includes('lucknow') ? 'Lucknow' : titleLower.includes('ayodhya') ? 'Ayodhya' : 'Uttar Pradesh';
      const incorrect = getRandomItems(['Uttar Pradesh', 'Lucknow', 'Ayodhya', 'Prayagraj', 'Varanasi', 'Noida', 'Delhi', 'Bihar'], 3, [correctOption]);
      options = [correctOption, ...incorrect];
      explanation = `This event is associated with Uttar Pradesh: ${desc}`;
      difficulty = 'moderate';
    } else {
      // General news question
      question = `Consider the following news: '${title}'. Which organization, scheme, or focus area is this news related to?`;
      const correctOption = item.source;
      const incorrect = getRandomItems([...DISTRACTORS.science, ...DISTRACTORS.economy], 3, [correctOption]);
      options = [correctOption, ...incorrect];
      explanation = `The news items states: "${title}". Source: ${item.source}. Detail: ${desc}`;
      difficulty = 'moderate';
    }
  }

  // Shuffle options and find new index of correct answer
  const correctOptionText = options[0];
  const shuffledOptions = [...options].sort(() => 0.5 - Math.random());
  correctAnswerIdx = shuffledOptions.indexOf(correctOptionText);

  // If difficulty is high priority, adjust difficulty
  if (item.importance === 'high') {
    difficulty = 'moderate';
  }
  if (item.examTags && item.examTags.includes('upsc')) {
    difficulty = item.importance === 'high' ? 'advanced' : 'moderate';
  }

  return {
    id: `mcq-${dateStr}-${String(index + 1).padStart(3, '0')}`,
    newsId: item.id,
    question,
    options: shuffledOptions,
    correctAnswer: correctAnswerIdx,
    explanation,
    category: primaryCat,
    examTags: item.examTags || [],
    difficulty,
    date: dateStr
  };
}

function main() {
  const todayStr = process.argv[2] || getTodayIST();
  const todayProcessedPath = path.join(PROCESSED_DIR, `${todayStr}.json`);

  ensureDir(MCQS_DIR);
  const outPath = path.join(MCQS_DIR, `${todayStr}.json`);

  if (!fs.existsSync(todayProcessedPath)) {
    console.log(`No processed items file found for today (${todayStr}). Nothing to generate MCQs for.`);
    fs.writeFileSync(outPath, JSON.stringify([], null, 2), 'utf8');
    return;
  }

  let items = [];
  try {
    items = JSON.parse(fs.readFileSync(todayProcessedPath, 'utf8'));
  } catch (err) {
    console.error(`Error reading ${todayProcessedPath}:`, err.message);
    process.exit(1);
  }

  console.log(`Loaded ${items.length} processed items to generate MCQs.`);

  // Generate MCQs for high and medium importance items
  const mcqs = [];
  let index = 0;

  items.forEach(item => {
    // Generate MCQ if high or medium importance
    if (item.importance === 'high' || item.importance === 'medium') {
      const mcq = generateMCQ(item, index, todayStr);
      mcqs.push(mcq);
      index++;
    }
  });

  fs.writeFileSync(outPath, JSON.stringify(mcqs, null, 2), 'utf8');
  console.log(`MCQ generation complete. Generated ${mcqs.length} MCQs. Saved to ${outPath}`);
}

main();
