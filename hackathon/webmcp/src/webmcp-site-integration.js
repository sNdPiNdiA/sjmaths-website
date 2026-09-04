/**
 * SJMaths WebMCP Site-Wide Integration Script
 * Bridges W3C WebMCP & OpenAI ChatGPT Desktop App Site Tools
 * Supports:
 *  - Native document.modelContext / navigator.modelContext preservation
 *  - Full 13 CBSE Class 10 Mathematics WebMCP tools
 *  - Declarative HTML forms (<form toolname="..." tooldescription="...">)
 *  - High-performance client-side tool execution with zero network roundtrips
 */
(function () {
  'use strict';

  // 1. Tool Schemas
  var TOOL_SCHEMAS = [
    {
      name: 'get_curriculum_outline',
      description: 'Get the full CBSE Class 10 Mathematics curriculum outline with all chapters, topics and skill counts.',
      inputSchema: { type: 'object', properties: {} }
    },
    {
      name: 'get_chapter_topics',
      description: 'List all topics inside a chapter with their ids, titles and stage counts.',
      inputSchema: {
        type: 'object',
        properties: { chapter_id: { type: 'string', description: 'Chapter id, e.g. chapter-4-quadratic-equations' } },
        required: ['chapter_id']
      }
    },
    {
      name: 'get_topic_metadata',
      description: 'Get lightweight metadata for a topic without full content.',
      inputSchema: {
        type: 'object',
        properties: { topic_id: { type: 'string', description: 'Topic ID or topic name' } },
        required: ['topic_id']
      }
    },
    {
      name: 'get_prerequisite_check',
      description: 'Check whether the student has mastered prerequisite skills for a topic.',
      inputSchema: {
        type: 'object',
        properties: { topic_id: { type: 'string', description: 'Topic ID or topic name' } },
        required: ['topic_id']
      }
    },
    {
      name: 'get_topic_concepts',
      description: 'Get core conceptual explanations, key formulas, diagrams, and trap warnings.',
      inputSchema: {
        type: 'object',
        properties: { topic_id: { type: 'string', description: 'Topic ID or topic name' } },
        required: ['topic_id']
      }
    },
    {
      name: 'get_worked_examples',
      description: 'Get step-by-step solved model problems with mathematical reasoning.',
      inputSchema: {
        type: 'object',
        properties: { topic_id: { type: 'string', description: 'Topic ID or topic name' } },
        required: ['topic_id']
      }
    },
    {
      name: 'get_practice_questions',
      description: 'Get practice questions for a topic across cognitive typology (answers stripped in assessment mode).',
      inputSchema: {
        type: 'object',
        properties: {
          topic_id: { type: 'string', description: 'Topic ID or topic name' },
          mode: { type: 'string', enum: ['assessment', 'study'], description: 'Access mode' }
        },
        required: ['topic_id']
      }
    },
    {
      name: 'evaluate_practice',
      description: 'Evaluate a student answer attempt against real answer keys.',
      inputSchema: {
        type: 'object',
        properties: {
          question_id: { type: 'string', description: 'Question ID, e.g. t1_p1' },
          selected_index: { type: 'integer', description: 'Option index chosen (0, 1, 2, 3)' },
          topic_id: { type: 'string', description: 'Topic ID or topic name' }
        },
        required: ['question_id', 'selected_index', 'topic_id']
      }
    },
    {
      name: 'get_hint',
      description: 'Get next progressive hint (levels 1-3) without disclosing final solution.',
      inputSchema: {
        type: 'object',
        properties: {
          question_id: { type: 'string', description: 'Question ID, e.g. t1_p1' },
          current_level: { type: 'integer', description: 'Current hint level (0, 1, 2)' },
          topic_id: { type: 'string', description: 'Topic ID or topic name' }
        },
        required: ['question_id']
      }
    },
    {
      name: 'get_topic_content',
      description: 'Get full topic content bundle across 5 stages.',
      inputSchema: {
        type: 'object',
        properties: {
          topic_id: { type: 'string', description: 'Topic ID or topic name' },
          mode: { type: 'string', enum: ['assessment', 'study'], description: 'Access mode' }
        },
        required: ['topic_id']
      }
    },
    {
      name: 'get_next_learning_action',
      description: 'Platform recommended next pedagogical step based on live mastery state.',
      inputSchema: {
        type: 'object',
        properties: { topic_id: { type: 'string', description: 'Topic ID or topic name' } }
      }
    },
    {
      name: 'start_mastery_exam',
      description: 'Initiate a 10-question timed cumulative mastery test.',
      inputSchema: { type: 'object', properties: {} }
    },
    {
      name: 'get_learning_progress',
      description: 'Get global CBSE curriculum progress and mastery percentages.',
      inputSchema: {
        type: 'object',
        properties: { curriculum_id: { type: 'string', description: 'Curriculum ID' } }
      }
    }
  ];

  window.WEBMCP_TOOL_SCHEMAS = TOOL_SCHEMAS;

  // 2. Execution Engine Resolver
  var _toolsEnginePromise = null;
  function getToolsEngine() {
    if (!_toolsEnginePromise) {
      _toolsEnginePromise = (async function () {
        if (window._webmcpToolsInstance) return window._webmcpToolsInstance;
        if (window._curriculumReadyPromise) {
          await window._curriculumReadyPromise;
          if (window._webmcpToolsInstance) return window._webmcpToolsInstance;
        }
        try {
          var isDemo = window.location.pathname.includes('/hackathon/webmcp/');
          var basePath = isDemo ? '../' : '/hackathon/webmcp/';
          var dataUrl = basePath + 'data/class-10/mathematics/cbse-class-10-mathematics.json';
          var toolsUrl = basePath + 'src/webmcp-tools.js';
          var r = await fetch(dataUrl);
          var curriculumData = await r.json();
          var mod = await import(toolsUrl);
          var factory = mod.createWebMCPTools || (mod.default && mod.default.createWebMCPTools);
          var inst = factory(curriculumData);
          window._webmcpToolsInstance = inst;
          return inst;
        } catch (err) {
          console.error('[WebMCP] Failed to initialize tools engine:', err);
          throw err;
        }
      })();
    }
    return _toolsEnginePromise;
  }

  async function executeWebMCPTool(nameOrObj, params, options) {
    var toolName = nameOrObj;
    var toolParams = params || {};
    if (typeof nameOrObj === 'object' && nameOrObj !== null) {
      toolName = nameOrObj.name || nameOrObj.tool || nameOrObj.tool_name || nameOrObj.toolName;
      toolParams = nameOrObj.parameters || nameOrObj.params || nameOrObj.arguments || nameOrObj.input || params || {};
    }
    if (!toolName || typeof toolName !== 'string') {
      throw new Error('Tool name must be a non-empty string.');
    }
    if (typeof toolParams === 'string') {
      try { toolParams = JSON.parse(toolParams); } catch (e) { toolParams = {}; }
    }
    if (typeof window._executeWebMCPToolImpl === 'function') {
      return window._executeWebMCPToolImpl(toolName, toolParams, options || {});
    }
    var engine = await getToolsEngine();
    return engine.executeTool(toolName, toolParams);
  }

  window._executeWebMCPTool = executeWebMCPTool;

  // 3. W3C ModelContext Polyfill Class
  class WebMCPModelContext extends EventTarget {
    constructor(toolsList) {
      super();
      this._toolsMap = new Map();
      this.ontoolchange = null;
      var self = this;
      if (Array.isArray(toolsList)) {
        for (var i = 0; i < toolsList.length; i++) {
          var t = toolsList[i];
          (function (def) {
            self._toolsMap.set(def.name, {
              name: def.name,
              description: def.description,
              inputSchema: def.inputSchema,
              annotations: {
                readOnlyHint: def.name !== 'start_mastery_exam',
                untrustedContentHint: false
              },
              execute: function (p) { return self.executeTool(def.name, p); }
            });
          })(t);
        }
      }
    }

    get tools() {
      return Array.from(this._toolsMap.values());
    }

    async getTools() {
      var list = Array.from(this._toolsMap.values());
      list.tools = list;
      return list;
    }

    async listTools() {
      var list = Array.from(this._toolsMap.values());
      list.tools = list;
      return list;
    }

    async registerTool(toolDef) {
      if (!toolDef || !toolDef.name) throw new Error('Tool definition requires a name.');
      var self = this;
      var reg = {
        name: toolDef.name,
        description: toolDef.description || '',
        inputSchema: toolDef.inputSchema || { type: 'object', properties: {} },
        annotations: toolDef.annotations || {
          readOnlyHint: toolDef.name !== 'start_mastery_exam',
          untrustedContentHint: false
        },
        execute: toolDef.execute || (function (p) { return self.executeTool(toolDef.name, p); })
      };
      this._toolsMap.set(toolDef.name, reg);
      var ev = new CustomEvent('toolchange', { detail: { action: 'register', tool: reg } });
      if (typeof this.dispatchEvent === 'function') this.dispatchEvent(ev);
      if (typeof this.ontoolchange === 'function') this.ontoolchange(ev);
      return reg;
    }

    async unregisterTool(name) {
      if (this._toolsMap.delete(name)) {
        var ev = new CustomEvent('toolchange', { detail: { action: 'unregister', name: name } });
        if (typeof this.dispatchEvent === 'function') this.dispatchEvent(ev);
        if (typeof this.ontoolchange === 'function') this.ontoolchange(ev);
        return true;
      }
      return false;
    }

    async executeTool(toolOrName, inputObject, options) {
      return executeWebMCPTool(toolOrName, inputObject, options);
    }

    async codexExecuteTool(toolOrName, inputObject, options) {
      return this.executeTool(toolOrName, inputObject, options);
    }
  }

  window.WebMCPModelContext = WebMCPModelContext;

  // 4. Preserve Native Host document.modelContext or Install Fallback
  var nativeMC = (typeof document !== 'undefined' && document.modelContext && typeof document.modelContext.registerTool === 'function')
    ? document.modelContext
    : (typeof navigator !== 'undefined' && navigator.modelContext && typeof navigator.modelContext.registerTool === 'function')
      ? navigator.modelContext
      : null;

  var polyfillMC = new WebMCPModelContext(TOOL_SCHEMAS);
  var activeMC = nativeMC || polyfillMC;

  if (!nativeMC) {
    try {
      if (!document.modelContext) {
        Object.defineProperty(document, 'modelContext', {
          value: polyfillMC,
          writable: true,
          configurable: true
        });
      }
    } catch (e) {
      try { document.modelContext = polyfillMC; } catch (err) {}
    }
    try {
      if (!navigator.modelContext) {
        Object.defineProperty(navigator, 'modelContext', {
          value: polyfillMC,
          writable: true,
          configurable: true
        });
      }
    } catch (e) {
      try { navigator.modelContext = polyfillMC; } catch (err) {}
    }
  }

  window.modelContext = activeMC;
  window.sjmathsWebMCP = activeMC;
  window.webmcp = activeMC;

  // 5. Register All 13 Tools on Active Context
  var registeredTools = new Set();
  async function registerAllTools(target) {
    if (!target || typeof target.registerTool !== 'function') return false;
    var existing = [];
    try {
      if (typeof target.getTools === 'function') {
        var tList = await target.getTools();
        existing = Array.isArray(tList) ? tList : (tList && tList.tools ? tList.tools : []);
      }
    } catch (e) {}
    var existingNames = new Set((existing || []).map(function (t) { return t.name; }));

    for (var i = 0; i < TOOL_SCHEMAS.length; i++) {
      var schema = TOOL_SCHEMAS[i];
      if (existingNames.has(schema.name)) continue;
      (function (def) {
        try {
          var p = target.registerTool({
            name: def.name,
            description: def.description,
            inputSchema: def.inputSchema,
            annotations: {
              readOnlyHint: def.name !== 'start_mastery_exam',
              untrustedContentHint: false
            },
            execute: async function (params) {
              var raw = await executeWebMCPTool(def.name, params);
              var text = typeof raw === 'string' ? raw : JSON.stringify(raw, null, 2);
              return {
                content: [{ type: 'text', text: text }],
                result: raw,
                ...(typeof raw === 'object' && raw !== null ? raw : {})
              };
            }
          });
          if (p && typeof p.catch === 'function') {
            p.catch(function (e) {});
          }
          registeredTools.add(def.name);
        } catch (err) {}
      })(schema);
    }
    try {
      var readyEv = new CustomEvent('modelcontextready', { detail: { modelContext: target } });
      if (typeof document !== 'undefined' && typeof document.dispatchEvent === 'function') document.dispatchEvent(readyEv);
      if (typeof window !== 'undefined' && typeof window.dispatchEvent === 'function') window.dispatchEvent(readyEv);
      var toolEv = new CustomEvent('toolchange', { detail: { tools: TOOL_SCHEMAS } });
      if (typeof document !== 'undefined' && typeof document.dispatchEvent === 'function') document.dispatchEvent(toolEv);
      if (typeof window !== 'undefined' && typeof window.dispatchEvent === 'function') window.dispatchEvent(toolEv);
    } catch (e) {}
    return true;
  }

  registerAllTools(activeMC);

  // 6. Watch for Host Preload Injections
  function checkHostContext() {
    var lateCtx = (typeof document !== 'undefined' && document.modelContext && typeof document.modelContext.registerTool === 'function' && document.modelContext !== activeMC)
      ? document.modelContext
      : (typeof navigator !== 'undefined' && navigator.modelContext && typeof navigator.modelContext.registerTool === 'function' && navigator.modelContext !== activeMC)
        ? navigator.modelContext
        : null;
    if (lateCtx) {
      activeMC = lateCtx;
      window.modelContext = lateCtx;
      registerAllTools(lateCtx);
    }
  }

  if (typeof document !== 'undefined' && typeof document.addEventListener === 'function') {
    document.addEventListener('DOMContentLoaded', checkHostContext);
  }
  if (typeof window !== 'undefined') {
    if (typeof window.addEventListener === 'function') {
      window.addEventListener('load', checkHostContext);
    }
    setTimeout(checkHostContext, 100);
    setTimeout(checkHostContext, 500);
    setTimeout(checkHostContext, 2000);
  }

  // 7. Global Interfaces for LLM Agents (ChatGPT Luna/Sol/Terra, Claude, DevTools)
  var getToolList = function () {
    var list = Array.from(activeMC.tools || TOOL_SCHEMAS);
    list.tools = list;
    return list;
  };

  window.fetchTools = getToolList;
  document.fetchTools = getToolList;
  try { navigator.fetchTools = getToolList; } catch (e) {}

  window.webmcp_list_tools = getToolList;
  document.webmcp_list_tools = getToolList;

  window.webmcp_call_tool = function (n, p) { return executeWebMCPTool(n, p); };
  window.webmcp_execute_tool = window.webmcp_call_tool;
  document.webmcp_call_tool = window.webmcp_call_tool;
  document.webmcp_execute_tool = window.webmcp_call_tool;

  window.getTools = function () { return (activeMC.getTools ? activeMC.getTools() : getToolList()); };
  window.listTools = function () { return (activeMC.listTools ? activeMC.listTools() : getToolList()); };

  window.executeTool = function (t, i, o) { return executeWebMCPTool(t, i, o); };
  document.executeTool = window.executeTool;
  try { navigator.executeTool = window.executeTool; } catch (e) {}

  window.callTool = window.executeTool;
  document.callTool = window.executeTool;
  window.call_tool = window.executeTool;
  window.execute_tool = window.executeTool;
  window.registerTool = function (t, o) { return activeMC.registerTool(t, o); };

  // 8. Declarative WebMCP Form Bridge
  if (typeof document !== 'undefined') {
    document.addEventListener('submit', async function (e) {
      var form = e.target;
      if (!form || !form.getAttribute) return;
      var toolName = form.getAttribute('data-toolname') || form.getAttribute('toolname') || form.getAttribute('tool');
      if (!toolName) return;
      e.preventDefault();
      var formData = new FormData(form);
      var params = {};
      formData.forEach(function (val, key) {
        params[key] = val;
      });
      try {
        var res = await executeWebMCPTool(toolName, params);
        if (typeof e.respondWith === 'function') {
          e.respondWith(Promise.resolve(res));
        }
      } catch (err) {
        if (typeof e.respondWith === 'function') {
          e.respondWith(Promise.reject(err));
        }
      }
    });
  }

  console.log('[WebMCP] SJMaths WebMCP active & site tools ready (13 tools registered).');
})();
