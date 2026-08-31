/**
 * webmcp-tools.js
 * 
 * Thin WebMCP Adapter over the generic LearningEngine for SJMaths.
 * Browser-safe Vanilla JavaScript implementation of the 8 WebMCP tools.
 * 
 * Architecture:
 *   WebMCP Tool Request -> webmcp-tools.js (Adapter) -> learning-engine.js (Generic Engine) -> Topic Data + State
 * 
 * Now fully generic - works with ANY valid Learning-Topic JSON specification.
 */

import { StateStore } from './state-store.js';
import { createLearningEngine } from './learning-engine.js';

export function createWebMCPTools(topicData, customStateStore = null) {
  if (!topicData || typeof topicData !== 'object') {
    throw new Error('WebMCP Tools require a valid topic data object.');
  }

  const defaultStore = customStateStore || new StateStore({ topicId: topicData.topic?.id });

  // Instantiate the generic, topic-agnostic learning engine
  const engine = createLearningEngine({
    topicData: topicData,
    stateStore: defaultStore
  });

  // Tool wrapper handlers delegating directly to generic engine
  function getTopicOutline(params = {}) {
    return engine.getTopicOutline(params);
  }

  function getUnitContent(params = {}) {
    return engine.getUnitContent(params);
  }

  function getPrerequisiteCheck(params = {}) {
    return engine.getPrerequisiteCheck(params);
  }

  function evaluateUnitPractice(params = {}, store = defaultStore) {
    return engine.evaluatePractice(params, store);
  }

  function getHint(params = {}, store = defaultStore) {
    return engine.getHint(params, store);
  }

  function getNextLearningAction(params = {}, store = defaultStore) {
    return engine.getNextLearningAction(params, store);
  }

  function startMasteryExam(params = {}) {
    return engine.startMasteryExam(params);
  }

  function getLearningProgress(params = {}, store = defaultStore) {
    return engine.getLearningProgress(params, store);
  }

  // Internal Tool Registry
  const TOOLS = {
    'get_topic_outline': getTopicOutline,
    'get_unit_content': getUnitContent,
    'get_prerequisite_check': getPrerequisiteCheck,
    'evaluate_unit_practice': evaluateUnitPractice,
    'get_hint': getHint,
    'get_next_learning_action': getNextLearningAction,
    'start_mastery_exam': startMasteryExam,
    'get_learning_progress': getLearningProgress
  };

  function executeTool(toolName, params = {}, customStore = defaultStore) {
    if (!toolName || typeof toolName !== 'string') {
      throw new Error('toolName must be a non-empty string.');
    }
    const handler = TOOLS[toolName];
    if (!handler) {
      throw new Error(`Unknown WebMCP tool: "${toolName}". Available tools: ${Object.keys(TOOLS).join(', ')}`);
    }
    return handler(params, customStore);
  }

  return {
    engine,
    TOOLS,
    executeTool,
    getTopicOutline,
    getUnitContent,
    getPrerequisiteCheck,
    evaluateUnitPractice,
    getHint,
    getNextLearningAction,
    startMasteryExam,
    getLearningProgress
  };
}

export default {
  createWebMCPTools
};
