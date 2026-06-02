const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const MCQS_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'mcqs');
const OLLAMA_URL = 'http://localhost:11434/api/generate';

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

async function checkOllama() {
  try {
    const res = await fetch('http://localhost:11434/', { method: 'GET' });
    return res.ok;
  } catch (e) {
    return false;
  }
}

async function enhanceWithOllama(item) {
  const prompt = `
You are a subject matter expert preparing MCQs for competitive government exams in India (UPSC, SSC, Railways).
Create a high-quality MCQ based on the following news article:

Title: ${item.title}
Source: ${item.source}
Details: ${item.description}

Requirements:
1. Provide a clear, unambiguous question.
2. Provide exactly 4 options.
3. Identify the correct answer (0-3 index).
4. Provide a detailed, educational explanation of the answer.
5. Rate difficulty: "easy", "moderate", or "advanced".

Respond ONLY with a valid JSON object matching this schema (do not wrap in markdown codeblocks):
{
  "question": "question string",
  "options": ["option A", "option B", "option C", "option D"],
  "correctAnswer": 0,
  "explanation": "detailed explanation of why the correct answer is right and why other options are wrong",
  "difficulty": "easy|moderate|advanced"
}
`;

  try {
    const response = await fetch(OLLAMA_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama3.2', // default fast model, user can change
        prompt: prompt,
        stream: false,
        format: 'json'
      })
    });

    if (!response.ok) {
      throw new Error(`Ollama HTTP status ${response.status}`);
    }

    const result = await response.json();
    const parsed = JSON.parse(result.response);
    return parsed;
  } catch (err) {
    console.error(`Ollama failed for "${item.title}":`, err.message);
    return null;
  }
}

async function main() {
  console.log('Checking for local Ollama service...');
  const isAvailable = await checkOllama();
  
  if (!isAvailable) {
    console.log('⚠️  Ollama is not running on http://localhost:11434.');
    console.log('Ensure Ollama is installed and run "ollama serve" before running this script.');
    console.log('Skipping AI enhancement. Standard template-based MCQs will be used.');
    return;
  }

  console.log('✅ Ollama is available! Starting AI enhancement...');
  const todayStr = getTodayIST();
  const todayProcessedPath = path.join(PROCESSED_DIR, `${todayStr}.json`);
  const mcqsPath = path.join(MCQS_DIR, `${todayStr}.json`);

  if (!fs.existsSync(todayProcessedPath) || !fs.existsSync(mcqsPath)) {
    console.log('Processed news or MCQ file not found for today. Run ca:process and ca:mcq first.');
    return;
  }

  const items = JSON.parse(fs.readFileSync(todayProcessedPath, 'utf8'));
  const mcqs = JSON.parse(fs.readFileSync(mcqsPath, 'utf8'));

  console.log(`Loaded ${items.length} news items. Rewriting high-importance MCQs...`);

  for (let i = 0; i < mcqs.length; i++) {
    const mcq = mcqs[i];
    const newsItem = items.find(item => item.id === mcq.newsId);
    
    if (newsItem && newsItem.importance === 'high') {
      console.log(`Enhancing MCQ ${i + 1} for: "${newsItem.title}"`);
      const enhanced = await enhanceWithOllama(newsItem);
      
      if (enhanced) {
        mcqs[i] = {
          ...mcq,
          question: enhanced.question,
          options: enhanced.options,
          correctAnswer: enhanced.correctAnswer,
          explanation: enhanced.explanation,
          difficulty: enhanced.difficulty
        };
        console.log('  -> MCQ enhanced successfully!');
      }
    }
  }

  fs.writeFileSync(mcqsPath, JSON.stringify(mcqs, null, 2), 'utf8');
  console.log(`AI enhancement completed. Updated MCQs written back to ${mcqsPath}`);
}

main().catch(err => {
  console.error('Fatal AI enhancement error:', err);
});
