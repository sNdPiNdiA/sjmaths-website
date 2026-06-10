const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const EXAM_MAP_PATH = path.join(__dirname, 'config', 'exam-mapping.json');

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

function tagExams() {
  const todayStr = process.argv[2] || getTodayIST();
  const tempProcessedPath = path.join(PROCESSED_DIR, `${todayStr}-temp.json`);
  const finalProcessedPath = path.join(PROCESSED_DIR, `${todayStr}.json`);

  if (!fs.existsSync(tempProcessedPath)) {
    console.log(`No temporary categorized file found for today (${todayStr}). Nothing to tag.`);
    fs.writeFileSync(finalProcessedPath, JSON.stringify([], null, 2), 'utf8');
    return;
  }

  let items = [];
  try {
    items = JSON.parse(fs.readFileSync(tempProcessedPath, 'utf8'));
  } catch (err) {
    console.error(`Error reading ${tempProcessedPath}:`, err.message);
    process.exit(1);
  }

  if (!fs.existsSync(EXAM_MAP_PATH)) {
    console.error('Exam mapping file not found at:', EXAM_MAP_PATH);
    process.exit(1);
  }

  let examConfig = {};
  try {
    examConfig = JSON.parse(fs.readFileSync(EXAM_MAP_PATH, 'utf8'));
  } catch (err) {
    console.error(`Error reading exam mapping config:`, err.message);
    process.exit(1);
  }

  const exams = examConfig.exams || [];
  console.log(`Loaded ${items.length} items to tag for ${exams.length} exams.`);

  const finalItems = items.map(item => {
    const examTags = [];

    // For each exam, check if there's any intersection of categories
    for (const exam of exams) {
      const intersection = item.categories.filter(cat => exam.categories.includes(cat));
      if (intersection.length > 0) {
        examTags.push(exam.id);
      }
    }

    return {
      id: item.id,
      title: item.title,
      source: item.source,
      sourceUrl: item.sourceUrl,
      pubDate: item.pubDate,
      description: item.description,
      categories: item.categories,
      examTags: examTags,
      importance: item.importance,
      keywords: item.keywords,
      imageUrl: item.imageUrl
    };
  });

  fs.writeFileSync(finalProcessedPath, JSON.stringify(finalItems, null, 2), 'utf8');
  console.log(`Exam tagging complete. Saved final processed items to: ${finalProcessedPath}`);

  // Clean up the temporary file
  try {
    fs.unlinkSync(tempProcessedPath);
    console.log(`Cleaned up temporary file: ${tempProcessedPath}`);
  } catch (err) {
    console.error(`Error deleting temporary file ${tempProcessedPath}:`, err.message);
  }
}

tagExams();
