/**
 * webmcp-register.js
 * 
 * WebMCP Browser API Registration Layer for SJMaths CBSE Class 10.
 * Uses navigator.modelContext.registerTool({ name, description, inputSchema, execute })
 * (with window.modelContext / document.modelContext fallbacks for polyfills)
 * 
 * Schema: Universal Schema v4.0.1
 * Coverage: Full CBSE Class 10 Mathematics (14 chapters, 43 topics)
 */

import { createWebMCPTools } from "./webmcp-tools.js";

export const WEBMCP_TOOL_DEFINITIONS = [
  {
    name: "get_curriculum_outline",
    description: "Returns the complete CBSE Class 10 Mathematics curriculum outline with 14 chapters and 43 topics.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false }
  },
  {
    name: "get_chapter_topics",
    description: "Retrieves all topics for a specific chapter with metadata.",
    inputSchema: {
      type: "object",
      properties: { chapter_id: { type: "string", description: "Chapter identifier." } },
      required: ["chapter_id"]
    }
  },
  {
    name: "get_topic_metadata",
    description: "Retrieves metadata for a specific topic including data path and stage count.",
    inputSchema: {
      type: "object",
      properties: { topic_id: { type: "string", description: "Topic identifier." } },
      required: ["topic_id"]
    }
  },
  {
    name: "get_topic_content",
    description: "Retrieves topic content descriptor with configurable answer suppression for assessment mode.",
    inputSchema: {
      type: "object",
      properties: {
        topic_id: { type: "string", description: "Topic identifier." },
        mode: { type: "string", enum: ["assessment", "study"], default: "assessment" }
      },
      required: ["topic_id"]
    }
  },
  {
    name: "get_prerequisite_check",
    description: "Returns prerequisite microlearning modules for foundational mathematical concepts.",
    inputSchema: {
      type: "object",
      properties: { topic_id: { type: "string", description: "Optional topic identifier." } }
    }
  },
  {
    name: "evaluate_practice",
    description: "Evaluates a student answer, tracks attempt history, and triggers remediation on repeated errors.",
    inputSchema: {
      type: "object",
      properties: {
        question_id: { type: "string", description: "Unique question identifier." },
        selected_index: { type: "integer", description: "0-based index of chosen option." },
        topic_id: { type: "string", description: "Optional topic identifier." }
      },
      required: ["question_id", "selected_index"]
    }
  },
  {
    name: "get_hint",
    description: "Delivers progressive 3-tier hints (conceptual, procedural, solution).",
    inputSchema: {
      type: "object",
      properties: {
        question_id: { type: "string", description: "Question identifier." },
        current_level: { type: "integer", description: "Current hint level (0-2).", default: 0 }
      },
      required: ["question_id"]
    }
  },
  {
    name: "get_next_learning_action",
    description: "Recommends optimal next pedagogical action based on student state and error streaks.",
    inputSchema: {
      type: "object",
      properties: { student_state: { type: "object", description: "Optional explicit student state." } }
    }
  },
  {
    name: "start_mastery_exam",
    description: "Initializes the CBSE Class 10 Mathematics mastery exam with solutions suppressed.",
    inputSchema: {
      type: "object",
      properties: { chapter_id: { type: "string", description: "Optional chapter filter." } }
    }
  },
  {
    name: "get_learning_progress",
    description: "Summarizes overall student progress, completed topics, mastered skills, and exam readiness.",
    inputSchema: {
      type: "object",
      properties: { student_state: { type: "object", description: "Optional explicit student state." } }
    }
  }
];

/**
 * Registers all 10 SJMaths tools with the browser WebMCP modelContext interface
 * (navigator.modelContext, with window/document fallbacks).
 */
export async function registerWebMCPTools(curriculumData, customModelContext = null, customStateStore = null) {
  if (!curriculumData) throw new Error("registerWebMCPTools requires curriculumData.");

  const modelContext = customModelContext ||
    (typeof navigator !== "undefined" && navigator.modelContext ? navigator.modelContext : null) ||
    (typeof window !== "undefined" && window.modelContext ? window.modelContext : null) ||
    (typeof document !== "undefined" && document.modelContext ? document.modelContext : null);

  if (!modelContext || typeof modelContext.registerTool !== "function") {
    console.warn("[WebMCP] No WebMCP modelContext (navigator/window/document) supported in this browser.");
    return [];
  }

  const toolsInstance = createWebMCPTools(curriculumData, customStateStore);
  const registered = [];

  for (const def of WEBMCP_TOOL_DEFINITIONS) {
    const executeCallback = async (params) => {
      try {
        const result = toolsInstance.executeTool(def.name, params || {});
        return { content: [{ type: "text", text: typeof result === "string" ? result : JSON.stringify(result, null, 2) }] };
      } catch (err) {
        return { isError: true, content: [{ type: "text", text: `Error executing ${def.name}: ${err.message}` }] };
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

  console.log(`[WebMCP] Successfully registered ${registered.length} tools for SJMaths CBSE Class 10.`);
  return registered;
}

export default { WEBMCP_TOOL_DEFINITIONS, registerWebMCPTools };
