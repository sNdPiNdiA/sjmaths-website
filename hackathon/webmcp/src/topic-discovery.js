/**
 * topic-discovery.js
 * 
 * Generic topic discovery and loading for WebMCP.
 * Dynamically discovers and loads any topic from the learning/topics directory.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
// Import pure, browser-safe converters (topic-convert.js has no fs/DOM deps)
import { topicToUnit, combineTopicsToChapter } from './topic-convert.js';

// Re-export named converters to preserve the stable public API surface
export { topicToUnit, combineTopicsToChapter };

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Root directory for learning topics (relative to webmcp/src/)
const TOPICS_ROOT = path.join(__dirname, '../../../learning/topics');

/**
 * Discovers all available topics from the learning/topics directory.
 * Returns a structured registry of classes, subjects, chapters, and topics.
 */
export function discoverTopics() {
  const registry = {};

  if (!fs.existsSync(TOPICS_ROOT)) {
    console.warn(`[TopicDiscovery] Topics root not found: ${TOPICS_ROOT}`);
    return registry;
  }

  // Scan for class directories (e.g., class-10, foundations)
  const classDirs = fs.readdirSync(TOPICS_ROOT).filter(dir => {
    return fs.statSync(path.join(TOPICS_ROOT, dir)).isDirectory();
  });

  for (const classDir of classDirs) {
    const classPath = path.join(TOPICS_ROOT, classDir);
    registry[classDir] = {};

    // Scan for subject directories (e.g., mathematics)
    const subjectDirs = fs.readdirSync(classPath).filter(dir => {
      return fs.statSync(path.join(classPath, dir)).isDirectory();
    });

    for (const subjectDir of subjectDirs) {
      const subjectPath = path.join(classPath, subjectDir);
      registry[classDir][subjectDir] = {};

      // Scan for chapter directories (e.g., chapter-1-real-numbers)
      const chapterDirs = fs.readdirSync(subjectPath).filter(dir => {
        return fs.statSync(path.join(subjectPath, dir)).isDirectory();
      });

      for (const chapterDir of chapterDirs) {
        const chapterPath = path.join(subjectPath, chapterDir);
        registry[classDir][subjectDir][chapterDir] = [];

        // Scan for topic directories (e.g., fta, hcf-lcm)
        const topicDirs = fs.readdirSync(chapterPath).filter(dir => {
          return fs.statSync(path.join(chapterPath, dir)).isDirectory();
        });

        for (const topicDir of topicDirs) {
          const topicPath = path.join(chapterPath, topicDir);
          const topicJsonPath = path.join(topicPath, `${topicDir}.json`);

          if (fs.existsSync(topicJsonPath)) {
            try {
              const topicData = JSON.parse(fs.readFileSync(topicJsonPath, 'utf8'));
              registry[classDir][subjectDir][chapterDir].push({
                id: topicData.topic?.id || topicDir,
                title: topicData.topic?.title || topicDir,
                shortTitle: topicData.topic?.short_title || topicDir,
                dir: topicDir,
                path: topicJsonPath,
                data: topicData
              });
            } catch (err) {
              console.warn(`[TopicDiscovery] Failed to load ${topicJsonPath}: ${err.message}`);
            }
          }
        }
      }
    }
  }

  return registry;
}

/**
 * Loads a specific topic by class, subject, chapter, and topic directory name.
 */
export function loadTopic(classDir, subjectDir, chapterDir, topicDir) {
  const topicJsonPath = path.join(TOPICS_ROOT, classDir, subjectDir, chapterDir, topicDir, `${topicDir}.json`);
  
  if (!fs.existsSync(topicJsonPath)) {
    throw new Error(`Topic not found: ${classDir}/${subjectDir}/${chapterDir}/${topicDir}`);
  }

  return JSON.parse(fs.readFileSync(topicJsonPath, 'utf8'));
}

/**
 * Loads all topics for a given chapter.
 */
export function loadChapterTopics(classDir, subjectDir, chapterDir) {
  const chapterPath = path.join(TOPICS_ROOT, classDir, subjectDir, chapterDir);
  
  if (!fs.existsSync(chapterPath)) {
    throw new Error(`Chapter not found: ${classDir}/${subjectDir}/${chapterDir}`);
  }

  const topics = [];
  const topicDirs = fs.readdirSync(chapterPath).filter(dir => {
    return fs.statSync(path.join(chapterPath, dir)).isDirectory();
  });

  for (const topicDir of topicDirs) {
    const topicJsonPath = path.join(chapterPath, topicDir, `${topicDir}.json`);
    
    if (fs.existsSync(topicJsonPath)) {
      try {
        const topicData = JSON.parse(fs.readFileSync(topicJsonPath, 'utf8'));
        topics.push({
          id: topicData.topic?.id || topicDir,
          title: topicData.topic?.title || topicDir,
          shortTitle: topicData.topic?.short_title || topicDir,
          dir: topicDir,
          data: topicData
        });
      } catch (err) {
        console.warn(`[TopicDiscovery] Failed to load ${topicJsonPath}: ${err.message}`);
      }
    }
  }

  return topics;
}
/**
 * Lists all available chapters with their topics.
 */
export function listAvailableChapters() {
  const registry = discoverTopics();
  const chapters = [];

  for (const [classDir, subjects] of Object.entries(registry)) {
    for (const [subjectDir, chapterMap] of Object.entries(subjects)) {
      for (const [chapterDir, topics] of Object.entries(chapterMap)) {
        if (topics.length > 0) {
          chapters.push({
            class: classDir,
            subject: subjectDir,
            chapter: chapterDir,
            topicCount: topics.length,
            topics: topics.map(t => ({ id: t.id, title: t.title }))
          });
        }
      }
    }
  }

  return chapters;
}

export default {
  discoverTopics,
  loadTopic,
  loadChapterTopics,
  topicToUnit,
  combineTopicsToChapter,
  listAvailableChapters
};
