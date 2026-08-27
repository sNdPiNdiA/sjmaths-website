/**
 * topic-loader.js
 * 
 * Topic Loader & Registry service for the generic SJMaths mastery-learning system.
 * Dynamically resolves topic identifiers to data paths or remote endpoints.
 */

// Registry of known learning topics across classes and subjects
export const TOPIC_REGISTRY = Object.freeze({
  // Class 10 Real Numbers
  'cbse10-real-numbers-fta': '../../data/class-10/mathematics/chapter-1-real-numbers/fta.json',
  'class-10-maths-chapter-1-fta': '../../data/class-10/mathematics/chapter-1-real-numbers/fta.json',
  'fta': '../../data/class-10/mathematics/chapter-1-real-numbers/fta.json',

  'cbse10-real-numbers-hcf-lcm': '../../data/class-10/mathematics/chapter-1-real-numbers/hcf-lcm.json',
  'class-10-maths-chapter-1-hcf-lcm': '../../data/class-10/mathematics/chapter-1-real-numbers/hcf-lcm.json',
  'hcf-lcm': '../../data/class-10/mathematics/chapter-1-real-numbers/hcf-lcm.json',

  'cbse10-real-numbers-irrationality': '../../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json',
  'class-10-maths-chapter-1-irrationality': '../../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json',
  'proof-of-irrationality': '../../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json',
  'irrationality': '../../data/class-10/mathematics/chapter-1-real-numbers/proof-of-irrationality.json'
});

/**
 * Extracts the requested topic identifier from URL search parameters or hash.
 * 
 * @param {string} [urlString] - Optional URL string (defaults to window.location.href in browser)
 * @returns {string|null} Topic identifier if found
 */
export function getRequestedTopicId(urlString = null) {
  try {
    const url = urlString ? new URL(urlString, 'http://localhost') : (typeof window !== 'undefined' ? window.location : null);
    if (!url) return null;
    const params = new URLSearchParams(url.search);
    return params.get('topic') || params.get('topic_id') || params.get('id') || null;
  } catch (err) {
    return null;
  }
}

/**
 * Resolves a topic ID to its corresponding JSON data path.
 * 
 * @param {string} topicId 
 * @returns {string|null} Relative or absolute JSON URL
 */
export function resolveTopicDataPath(topicId) {
  if (!topicId || typeof topicId !== 'string') return null;
  const normalizedId = topicId.trim().toLowerCase();

  if (TOPIC_REGISTRY[normalizedId]) {
    return TOPIC_REGISTRY[normalizedId];
  }

  // Support direct relative/absolute path passed as topic parameter (for dev/synthetic tests)
  if (normalizedId.endsWith('.json')) {
    return normalizedId;
  }

  return null;
}

/**
 * Loads and validates a Learning-Topic JSON.
 * 
 * @param {string} topicId
 * @param {Object} [options]
 * @param {Function} [options.fetchFn] - Custom fetch implementation
 * @returns {Promise<Object>} Loaded topic dataset
 */
export async function loadTopicData(topicId, { fetchFn = (typeof fetch !== 'undefined' ? fetch : null) } = {}) {
  if (!topicId) {
    throw new Error('No topic ID provided. Please specify ?topic=<topic_id> in the URL.');
  }

  const dataPath = resolveTopicDataPath(topicId);
  if (!dataPath) {
    throw new Error(`Learning topic "${topicId}" is not registered.`);
  }

  if (!fetchFn) {
    throw new Error('No fetch implementation available to load topic data.');
  }

  const res = await fetchFn(dataPath);
  if (!res.ok) {
    throw new Error(`Failed to load topic dataset (${res.status} ${res.statusText}).`);
  }

  const data = await res.json();
  if (!data || typeof data !== 'object' || !data.topic) {
    throw new Error('Malformed topic data: Missing required topic metadata object.');
  }

  return data;
}
