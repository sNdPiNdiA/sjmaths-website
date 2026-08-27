/**
 * webmcp-register.js
 * 
 * WebMCP Browser API Registration Layer for SJMaths Chapter 4.
 * Uses the current `document.modelContext.registerTool({ name, description, inputSchema, execute })`
 * asynchronous API with injected tool implementation.
 */

import { createWebMCPTools } from './webmcp-tools.js';

export const WEBMCP_TOOL_DEFINITIONS = [
  {
    name: 'get_topic_outline',
    description: 'Returns the high-level curriculum outline, units, and skill list for Class 10 Quadratic Equations.',
    inputSchema: {
      type: 'object',
      properties: {},
      additionalProperties: false
    }
  },
  {
    name: 'get_unit_content',
    description: 'Retrieves instructional content, core concepts, formulas, callouts, and practice items for a specific learning unit. In assessment mode, answers and solutions are suppressed.',
    inputSchema: {
      type: 'object',
      properties: {
        unit_id: {
          type: 'string',
          description: 'The unit identifier.',
          enum: [
            'unit-1-standard-form-factorisation',
            'unit-2-quadratic-formula',
            'unit-3-nature-of-roots',
            'unit-4-situational-word-problems'
          ]
        },
        include_practice: {
          type: 'boolean',
          description: 'Whether to include practice and board transfer questions.',
          default: false
        },
        mode: {
          type: 'string',
          description: 'Access mode ("assessment" suppresses solutions; "study" includes full derivations).',
          enum: ['assessment', 'study'],
          default: 'assessment'
        }
      },
      required: ['unit_id']
    }
  },
  {
    name: 'get_prerequisite_check',
    description: 'Retrieves the diagnostic precheck question for a specific unit to test prerequisite readiness before starting instruction.',
    inputSchema: {
      type: 'object',
      properties: {
        unit_id: {
          type: 'string',
          description: 'The unit identifier to retrieve diagnostic check for.',
          enum: [
            'unit-1-standard-form-factorisation',
            'unit-2-quadratic-formula',
            'unit-3-nature-of-roots',
            'unit-4-situational-word-problems'
          ]
        }
      },
      required: ['unit_id']
    }
  },
  {
    name: 'evaluate_unit_practice',
    description: 'Evaluates a student submitted answer, tracks attempt history and error streaks, and triggers remediation rules when repeated mistakes occur.',
    inputSchema: {
      type: 'object',
      properties: {
        question_id: {
          type: 'string',
          description: 'The unique question identifier (e.g. u1-p-1, u1-pyq-2, u1-precheck).'
        },
        selected_index: {
          type: 'integer',
          description: 'The 0-based index of the chosen option.'
        },
        prior_attempt_count: {
          type: 'integer',
          description: 'Optional prior attempt counter if operating statelessly.',
          default: 0
        }
      },
      required: ['question_id', 'selected_index']
    }
  },
  {
    name: 'get_hint',
    description: 'Delivers progressive, multi-tier hints without prematurely revealing the final answer (Level 1: Conceptual cue, Level 2: Procedural intermediate step, Level 3: Full solution derivation).',
    inputSchema: {
      type: 'object',
      properties: {
        question_id: {
          type: 'string',
          description: 'The question identifier.'
        },
        hint_level: {
          type: 'integer',
          description: 'The requested scaffolding level (1, 2, or 3).',
          enum: [1, 2, 3],
          default: 1
        }
      },
      required: ['question_id', 'hint_level']
    }
  },
  {
    name: 'get_next_learning_action',
    description: 'Inspects student progress, recent error streaks, and unit milestones to recommend the optimal next pedagogical learning action.',
    inputSchema: {
      type: 'object',
      properties: {
        current_unit_id: {
          type: 'string',
          description: 'Optional current unit identifier.'
        },
        completed_question_ids: {
          type: 'array',
          items: { type: 'string' },
          description: 'List of completed question IDs.'
        },
        recent_error_streak: {
          type: 'integer',
          description: 'Current count of consecutive incorrect answers.',
          default: 0
        }
      }
    }
  },
  {
    name: 'start_mastery_exam',
    description: 'Initializes the proctored Chapter 4 Mastery Exam with all answer keys and solution derivations strictly suppressed.',
    inputSchema: {
      type: 'object',
      properties: {},
      additionalProperties: false
    }
  },
  {
    name: 'get_learning_progress',
    description: 'Summarizes overall student learning progress, completed units, mastered skills, and mastery exam readiness.',
    inputSchema: {
      type: 'object',
      properties: {
        student_state: {
          type: 'object',
          description: 'Optional explicit student state object if querying externally.'
        }
      }
    }
  }
];

/**
 * Registers all 8 SJMaths tools with the browser's `document.modelContext` interface.
 * Uses the modern object signature: document.modelContext.registerTool({ name, description, inputSchema, execute })
 * 
 * @param {object} chapterData - Injected chapter-4-data-v2 JSON object (loaded via fetch() in browser).
 * @param {object} [customModelContext] - Optional mock/custom modelContext for testing.
 * @param {object} [customStateStore] - Optional StateStore instance.
 * @returns {Promise<Array<string>>} Promise resolving to the list of successfully registered tool names.
 */
export async function registerWebMCPTools(chapterData, customModelContext = null, customStateStore = null) {
  if (!chapterData) {
    throw new Error('registerWebMCPTools requires chapterData.');
  }

  const modelContext = customModelContext || 
    (typeof document !== 'undefined' && document.modelContext ? document.modelContext : null);

  if (!modelContext || typeof modelContext.registerTool !== 'function') {
    console.warn('[WebMCP] document.modelContext is not supported or not enabled in this browser.');
    return [];
  }

  const toolsInstance = createWebMCPTools(chapterData, customStateStore);
  const registered = [];

  for (const def of WEBMCP_TOOL_DEFINITIONS) {
    const executeCallback = async (params) => {
      try {
        const result = toolsInstance.executeTool(def.name, params || {});
        return {
          content: [
            {
              type: 'text',
              text: typeof result === 'string' ? result : JSON.stringify(result, null, 2)
            }
          ]
        };
      } catch (err) {
        return {
          isError: true,
          content: [
            {
              type: 'text',
              text: `Error executing ${def.name}: ${err.message}`
            }
          ]
        };
      }
    };

    try {
      await modelContext.registerTool({
        name: def.name,
        description: def.description,
        inputSchema: def.inputSchema,
        execute: executeCallback
      });
      registered.push(def.name);
    } catch (regError) {
      console.error(`[WebMCP] Failed to register tool "${def.name}":`, regError);
    }
  }

  console.log(`[WebMCP] Successfully registered ${registered.length} tools for SJMaths Chapter 4.`);
  return registered;
}

export default {
  WEBMCP_TOOL_DEFINITIONS,
  registerWebMCPTools
};
