const DATA_ROOT = new URL('../data/quantitative-aptitude/', import.meta.url);
const TOPIC_ID_PATTERN = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

async function fetchJson(relativePath, signal) {
  const response = await fetch(new URL(relativePath, DATA_ROOT), { signal });
  if (!response.ok) {
    throw new Error(`Could not load quantitative aptitude data (${response.status} ${response.statusText}).`);
  }
  return response.json();
}

export async function loadQuantitativeAptitudeManifest({ signal } = {}) {
  const manifest = await fetchJson('manifest.json', signal);
  if (manifest.schemaVersion !== 1 || !Array.isArray(manifest.topics)) {
    throw new Error('Unsupported quantitative aptitude manifest format.');
  }
  return manifest;
}

export async function loadQuantitativeAptitudeCatalog({ signal } = {}) {
  const catalog = await fetchJson('catalog.json', signal);
  if (catalog.schemaVersion !== 1 || !Array.isArray(catalog.groups)) {
    throw new Error('Unsupported quantitative aptitude catalog format.');
  }
  return catalog;
}

export async function loadQuantitativeAptitudeTopic(topicId, { examId = null, signal } = {}) {
  if (typeof topicId !== 'string' || !TOPIC_ID_PATTERN.test(topicId)) {
    throw new TypeError('A lowercase topic id is required to load quantitative aptitude data.');
  }

  const catalog = await loadQuantitativeAptitudeCatalog({ signal });
  const catalogTopic = catalog.groups
    .flatMap(group => group.topics)
    .find(item => item.id === topicId);
  if (catalogTopic && !catalogTopic.dataFile) {
    throw new Error(`Shared lesson content is not available yet for "${topicId}".`);
  }

  const dataFile = catalogTopic?.dataFile ?? `${topicId}.json`;
  const expectedDataId = dataFile.slice(0, -'.json'.length);
  const topic = await fetchJson(dataFile, signal);
  if (topic.schemaVersion !== 1 || topic.id !== expectedDataId || !Array.isArray(topic.sections)) {
    throw new Error(`Unsupported quantitative aptitude topic format for "${topicId}".`);
  }

  return {
    ...topic,
    ...(catalogTopic ? { requestedTopicId: topicId, catalogTopic } : {}),
    sections: topic.sections.filter(section => !section.examId || section.examId === examId),
  };
}
