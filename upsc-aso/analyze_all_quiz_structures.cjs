const fs = require('fs');
const path = require('path');

async function main() {
  const genModule = await import('./generate_gemini_study_page.mjs');
  const allDays = genModule.parseAllDays();
  const existingDays = allDays.filter(d => fs.existsSync(d.outputPath));

  console.log(`Analyzing quiz structures across ${existingDays.length} existing study modules...\n`);

  const categories = {
    dynamicQuizData: [], // Uses window.quizData / quizData array and renders via JS
    staticOptionItem: [], // Uses .option-item with selectOption(...)
    staticQuizOptBtn: [], // Uses .quiz-opt-btn with selectQuizOpt(...)
    staticRadios: [], // Uses static input[type="radio"]
    other: []
  };

  const testStructures = {
    dynamicLevelData: [], // Uses level1Data / level2Data
    dynamicQuestionsData: [], // Uses level1QuestionsData / level2QuestionsData
    dynamicLevelQuestions: [], // Uses level1Questions / level2Questions
    other: []
  };

  for (const d of existingDays) {
    const html = fs.readFileSync(d.outputPath, 'utf8');

    // Tab 2 Quiz check
    if (html.includes('quizData') && (html.includes('renderQuiz') || html.includes('buildQuiz'))) {
      categories.dynamicQuizData.push(d.day);
    } else if (html.includes('selectOption(this')) {
      categories.staticOptionItem.push(d.day);
    } else if (html.includes('selectQuizOpt(')) {
      categories.staticQuizOptBtn.push(d.day);
    } else if (html.includes('input type="radio"') && (html.includes('tab-2') || html.includes('tab-quiz'))) {
      categories.staticRadios.push(d.day);
    } else {
      categories.other.push(d.day);
    }

    // Tab 5 Tests check
    if (html.includes('level1Data') || html.includes('level2Data')) {
      testStructures.dynamicLevelData.push(d.day);
    } else if (html.includes('level1QuestionsData') || html.includes('level2QuestionsData')) {
      testStructures.dynamicQuestionsData.push(d.day);
    } else if (html.includes('level1Questions') || html.includes('level2Questions')) {
      testStructures.dynamicLevelQuestions.push(d.day);
    } else {
      testStructures.other.push(d.day);
    }
  }

  console.log('--- Tab 2 Quiz Categories ---');
  console.log(`Dynamic quizData (${categories.dynamicQuizData.length} days):`, categories.dynamicQuizData.join(', '));
  console.log(`Static with selectOption (${categories.staticOptionItem.length} days):`, categories.staticOptionItem.join(', '));
  console.log(`Static with selectQuizOpt (${categories.staticQuizOptBtn.length} days):`, categories.staticQuizOptBtn.join(', '));
  console.log(`Static with Radios (${categories.staticRadios.length} days):`, categories.staticRadios.join(', '));
  console.log(`Other (${categories.other.length} days):`, categories.other.join(', '));

  console.log('\n--- Tab 5 Test Categories ---');
  console.log(`level1Data / level2Data (${testStructures.dynamicLevelData.length} days):`, testStructures.dynamicLevelData.join(', '));
  console.log(`level1QuestionsData / level2QuestionsData (${testStructures.dynamicQuestionsData.length} days):`, testStructures.dynamicQuestionsData.join(', '));
  console.log(`level1Questions / level2Questions (${testStructures.dynamicLevelQuestions.length} days):`, testStructures.dynamicLevelQuestions.join(', '));
  console.log(`Other (${testStructures.other.length} days):`, testStructures.other.join(', '));
}

main().catch(console.error);
