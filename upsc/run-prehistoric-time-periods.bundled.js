var __create = Object.create;
var __defProp = Object.defineProperty;
var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
var __getOwnPropNames = Object.getOwnPropertyNames;
var __getProtoOf = Object.getPrototypeOf;
var __hasOwnProp = Object.prototype.hasOwnProperty;
var __copyProps = (to, from, except, desc) => {
  if (from && typeof from === "object" || typeof from === "function") {
    for (let key of __getOwnPropNames(from))
      if (!__hasOwnProp.call(to, key) && key !== except)
        __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
  }
  return to;
};
var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
  // If the importer is in node compatibility mode or this is not an ESM
  // file that has been converted to a CommonJS file using a Babel-
  // compatible transform (i.e. "__esModule" has not been set), then set
  // "default" to the CommonJS "module.exports" for node compatibility.
  isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
  mod
));

// upsc/run-prehistoric-time-periods.js
var import_fs = __toESM(require("fs"));
var import_path = __toESM(require("path"));

// upsc/upsc-microtopic-template.js
var VERSION = {
  generator: "v5",
  prompt: "4.0",
  translator: "2.0",
  normalizer: "1.0",
  scorer: "1.5",
  manifest: "1.0"
};
var SUBJECT_CONFIGS = {
  "ancient-history": {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "match"]
  },
  "medieval-history": {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "match"]
  },
  "modern-history": {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "assertion", "advanced"]
  },
  "polity": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "assertion", "advanced"]
  },
  "geography": {
    supportsTimeline: false,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "match"]
  },
  "economy": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "advanced"]
  },
  "environment": {
    supportsTimeline: false,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "match"]
  },
  "science-and-tech": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: false,
    defaultPracticeTypes: ["basic", "conceptual", "statement"]
  },
  "art-and-culture": {
    supportsTimeline: true,
    supportsMaps: true,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "match"]
  },
  "social-issues": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "advanced"]
  },
  "ethics": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ["conceptual", "statement", "advanced"]
  },
  "csat": {
    supportsTimeline: false,
    supportsMaps: false,
    supportsMains: false,
    defaultPracticeTypes: ["basic", "conceptual", "advanced"]
  }
};
function getSubjectConfig(subjectDir) {
  return SUBJECT_CONFIGS[subjectDir] || {
    supportsTimeline: true,
    supportsMaps: false,
    supportsMains: true,
    defaultPracticeTypes: ["basic", "conceptual", "statement", "assertion", "match", "advanced"]
  };
}
function validateMetadata(meta2) {
  const errors = [];
  const warnings = [];
  if (!meta2) {
    errors.push("Metadata is null/undefined");
    return { passed: false, errors, warnings };
  }
  const required = ["name", "hindiName", "dir", "subject", "subjectDir", "canonicalUrl", "description", "topicId"];
  for (const field of required) {
    if (!meta2[field]) {
      errors.push(`Missing required field: ${field}`);
    }
  }
  if (meta2.name && meta2.name.length < 3) {
    errors.push(`Name too short: "${meta2.name}" (min 3 chars)`);
  }
  if (meta2.name && meta2.name.length > 100) {
    errors.push(`Name too long: "${meta2.name}" (max 100 chars)`);
  }
  if (meta2.hindiName && meta2.hindiName.length < 3) {
    warnings.push(`hindiName seems too short: "${meta2.hindiName}"`);
  }
  if (meta2.description) {
    if (meta2.description.length < 50) {
      warnings.push(`SEO description too short (${meta2.description.length} chars, min 50)`);
    }
    if (meta2.description.length > 160) {
      warnings.push(`SEO description too long (${meta2.description.length} chars, max 160)`);
    }
  }
  if (meta2.canonicalUrl) {
    if (!meta2.canonicalUrl.startsWith("https://sjmaths.com/")) {
      warnings.push(`canonicalUrl should start with https://sjmaths.com/: ${meta2.canonicalUrl}`);
    }
    if (!meta2.canonicalUrl.endsWith("/")) {
      warnings.push(`canonicalUrl should end with /: ${meta2.canonicalUrl}`);
    }
  }
  if (meta2.topicId && !/^[a-z0-9.-]+$/.test(meta2.topicId)) {
    warnings.push(`topicId should be lowercase alphanumeric with dots/hyphens: ${meta2.topicId}`);
  }
  if (meta2.previousTopic && !meta2.previousDir) {
    warnings.push("previousTopic exists but previousDir is missing");
  }
  if (meta2.nextTopic && !meta2.nextDir) {
    warnings.push("nextTopic exists but nextDir is missing");
  }
  if (meta2.scope) {
    if (!meta2.scope.mustExplain || meta2.scope.mustExplain.length === 0) {
      warnings.push("scope.mustExplain is empty \u2014 add at least one concept");
    }
    if (!meta2.scope.neverExplain || meta2.scope.neverExplain.length === 0) {
      warnings.push("scope.neverExplain is empty \u2014 add at least one forbidden topic");
    }
    if (!meta2.scope.keywords || meta2.scope.keywords.length < 3) {
      warnings.push("scope.keywords has fewer than 3 entries");
    }
  } else {
    warnings.push("scope is missing \u2014 strongly recommended for content boundary enforcement");
  }
  const validDifficulties = ["easy", "medium", "hard"];
  if (meta2.difficulty && !validDifficulties.includes(meta2.difficulty)) {
    errors.push(`Invalid difficulty: "${meta2.difficulty}". Must be one of: ${validDifficulties.join(", ")}`);
  }
  if (meta2.studyTime) {
    if (typeof meta2.studyTime.concepts !== "number" || meta2.studyTime.concepts < 1) {
      warnings.push("studyTime.concepts should be a positive number");
    }
    if (typeof meta2.studyTime.practice !== "number" || meta2.studyTime.practice < 1) {
      warnings.push("studyTime.practice should be a positive number");
    }
  }
  const validTypes = ["basic", "conceptual", "statement", "assertion", "match", "advanced"];
  if (meta2.practiceTypes) {
    for (const type of meta2.practiceTypes) {
      if (!validTypes.includes(type)) {
        warnings.push(`Invalid practiceType: "${type}". Valid: ${validTypes.join(", ")}`);
      }
    }
  }
  if (meta2.learningObjectives && meta2.learningObjectives.length < 2) {
    warnings.push("learningObjectives should have at least 2 entries");
  }
  if (meta2.subjectDir && !SUBJECT_CONFIGS[meta2.subjectDir]) {
    warnings.push(`Unknown subjectDir: "${meta2.subjectDir}". Add config to SUBJECT_CONFIGS or expect defaults`);
  }
  return {
    passed: errors.length === 0,
    errors,
    warnings
  };
}
var DEFAULT_GLOSSARY = {
  // Prehistory
  "Paleolithic": "\u092A\u0941\u0930\u093E\u092A\u093E\u0937\u093E\u0923 \u0915\u093E\u0932",
  "Mesolithic": "\u092E\u0927\u094D\u092F\u092A\u093E\u0937\u093E\u0923 \u0915\u093E\u0932",
  "Neolithic": "\u0928\u0935\u092A\u093E\u0937\u093E\u0923 \u0915\u093E\u0932",
  "Chalcolithic": "\u0924\u093E\u092E\u094D\u0930\u092A\u093E\u0937\u093E\u0923 \u0915\u093E\u0932",
  "Acheulian": "\u090F\u0936\u094D\u092F\u0942\u0932\u093F\u092F\u0928",
  "Soanian": "\u0938\u094B\u0906\u0928\u093F\u092F\u0928",
  "Nevasan": "\u0928\u0947\u0935\u093E\u0938\u0928",
  "Handaxe": "\u0939\u0938\u094D\u0924 \u0915\u0941\u0920\u093E\u0930",
  "Cleaver": "\u0915\u094D\u0932\u0940\u0935\u0930",
  "Blade": "\u092B\u0932\u0915",
  "Burin": "\u092C\u094D\u092F\u0942\u0930\u093F\u0928",
  "Scraper": "\u0916\u0941\u0930\u091A\u0928\u0940",
  "Borers": "\u092C\u0947\u0927\u0928\u0940",
  "Hominin": "\u0939\u094B\u092E\u093F\u0928\u093F\u0928",
  "Pleistocene": "\u092A\u094D\u0932\u0940\u0938\u094D\u091F\u094B\u0938\u0940\u0928",
  "Holocene": "\u0939\u094B\u0932\u094B\u0938\u0940\u0928",
  // Polity
  "Doctrine of Eclipse": "\u0917\u094D\u0930\u0939\u0923 \u0915\u093E \u0938\u093F\u0926\u094D\u0927\u093E\u0902\u0924",
  "Doctrine of Severability": "\u092A\u0943\u0925\u0915\u094D\u0915\u0930\u0923\u0940\u092F\u0924\u093E \u0915\u093E \u0938\u093F\u0926\u094D\u0927\u093E\u0902\u0924",
  "Doctrine of Basic Structure": "\u092E\u0942\u0932 \u0938\u0902\u0930\u091A\u0928\u093E \u0915\u093E \u0938\u093F\u0926\u094D\u0927\u093E\u0902\u0924",
  "Judicial Review": "\u0928\u094D\u092F\u093E\u092F\u093F\u0915 \u092A\u0941\u0928\u0930\u093E\u0935\u0932\u094B\u0915\u0928",
  "Writ": "\u0930\u093F\u091F",
  "Habeas Corpus": "\u092C\u0902\u0926\u0940 \u092A\u094D\u0930\u0924\u094D\u092F\u0915\u094D\u0937\u0940\u0915\u0930\u0923",
  "Mandamus": "\u092A\u0930\u092E\u093E\u0926\u0947\u0936",
  "Certiorari": "\u0909\u0924\u094D\u092A\u094D\u0930\u0947\u0937\u0923",
  "Prohibition": "\u0928\u093F\u0937\u0947\u0927",
  "Quo Warranto": "\u0905\u0927\u093F\u0915\u093E\u0930 \u092A\u0943\u091A\u094D\u091B\u093E",
  // Geography
  "Ecotone": "\u0907\u0915\u094B\u091F\u094B\u0928",
  "Continental Drift": "\u092E\u0939\u093E\u0926\u094D\u0935\u0940\u092A\u0940\u092F \u0935\u093F\u0938\u094D\u0925\u093E\u092A\u0928",
  "Plate Tectonics": "\u092A\u094D\u0932\u0947\u091F \u0935\u093F\u0935\u0930\u094D\u0924\u0928\u093F\u0915\u0940",
  "Monsoon": "\u092E\u093E\u0928\u0938\u0942\u0928",
  "Western Ghats": "\u092A\u0936\u094D\u091A\u093F\u092E\u0940 \u0918\u093E\u091F",
  "Eastern Ghats": "\u092A\u0942\u0930\u094D\u0935\u0940 \u0918\u093E\u091F",
  "Himalayas": "\u0939\u093F\u092E\u093E\u0932\u092F",
  "Indo-Gangetic Plain": "\u0938\u093F\u0902\u0927\u0941-\u0917\u0902\u0917\u093E \u0915\u093E \u092E\u0948\u0926\u093E\u0928",
  "Deccan Plateau": "\u0926\u0915\u094D\u0915\u0928 \u0915\u093E \u092A\u0920\u093E\u0930",
  "Thar Desert": "\u0925\u093E\u0930 \u092E\u0930\u0941\u0938\u094D\u0925\u0932",
  // Environment
  "Biodiversity": "\u091C\u0948\u0935 \u0935\u093F\u0935\u093F\u0927\u0924\u093E",
  "Ecosystem": "\u092A\u093E\u0930\u093F\u0938\u094D\u0925\u093F\u0924\u093F\u0915\u0940 \u0924\u0902\u0924\u094D\u0930",
  "Biosphere": "\u091C\u0940\u0935\u092E\u0902\u0921\u0932",
  "Food Chain": "\u0916\u093E\u0926\u094D\u092F \u0936\u094D\u0930\u0943\u0902\u0916\u0932\u093E",
  "Food Web": "\u0916\u093E\u0926\u094D\u092F \u091C\u093E\u0932",
  "Trophic Level": "\u092A\u094B\u0937\u0940 \u0938\u094D\u0924\u0930",
  "Ecological Pyramid": "\u092A\u093E\u0930\u093F\u0938\u094D\u0925\u093F\u0924\u093F\u0915 \u092A\u093F\u0930\u093E\u092E\u093F\u0921",
  "Biome": "\u091C\u0948\u0935\u092D\u0942\u092E\u093F",
  "Conservation": "\u0938\u0902\u0930\u0915\u094D\u0937\u0923",
  "Endemic Species": "\u0938\u094D\u0925\u093E\u0928\u093F\u0915 \u092A\u094D\u0930\u091C\u093E\u0924\u093F",
  "Endangered": "\u0932\u0941\u092A\u094D\u0924\u092A\u094D\u0930\u093E\u092F",
  "Vulnerable": "\u0905\u0938\u0941\u0930\u0915\u094D\u0937\u093F\u0924",
  "Critically Endangered": "\u0917\u0902\u092D\u0940\u0930 \u0930\u0942\u092A \u0938\u0947 \u0932\u0941\u092A\u094D\u0924\u092A\u094D\u0930\u093E\u092F",
  // Economy
  "GDP": "\u0938\u0915\u0932 \u0918\u0930\u0947\u0932\u0942 \u0909\u0924\u094D\u092A\u093E\u0926",
  "GNP": "\u0938\u0915\u0932 \u0930\u093E\u0937\u094D\u091F\u094D\u0930\u0940\u092F \u0909\u0924\u094D\u092A\u093E\u0926",
  "Inflation": "\u092E\u0941\u0926\u094D\u0930\u093E\u0938\u094D\u092B\u0940\u0924\u093F",
  "Deflation": "\u0905\u092A\u0938\u094D\u092B\u0940\u0924\u093F",
  "Fiscal Policy": "\u0930\u093E\u091C\u0915\u094B\u0937\u0940\u092F \u0928\u0940\u0924\u093F",
  "Monetary Policy": "\u092E\u094C\u0926\u094D\u0930\u093F\u0915 \u0928\u0940\u0924\u093F",
  "Repo Rate": "\u0930\u0947\u092A\u094B \u0926\u0930",
  "Reverse Repo Rate": "\u0930\u093F\u0935\u0930\u094D\u0938 \u0930\u0947\u092A\u094B \u0926\u0930",
  "CRR": "\u0928\u0915\u0926 \u0906\u0930\u0915\u094D\u0937\u093F\u0924 \u0905\u0928\u0941\u092A\u093E\u0924",
  "SLR": "\u0935\u0948\u0927\u093E\u0928\u093F\u0915 \u0924\u0930\u0932\u0924\u093E \u0905\u0928\u0941\u092A\u093E\u0924",
  "Budget": "\u092C\u091C\u091F",
  "Subsidy": "\u0938\u092C\u094D\u0938\u093F\u0921\u0940",
  "Tax": "\u0915\u0930",
  "Direct Tax": "\u092A\u094D\u0930\u0924\u094D\u092F\u0915\u094D\u0937 \u0915\u0930",
  "Indirect Tax": "\u0905\u092A\u094D\u0930\u0924\u094D\u092F\u0915\u094D\u0937 \u0915\u0930",
  "GST": "\u0935\u0938\u094D\u0924\u0941 \u090F\u0935\u0902 \u0938\u0947\u0935\u093E \u0915\u0930",
  // Science & Tech
  "DNA": "\u0921\u0940\u090F\u0928\u090F",
  "RNA": "\u0906\u0930\u090F\u0928\u090F",
  "Gene": "\u091C\u0940\u0928",
  "Chromosome": "\u0917\u0941\u0923\u0938\u0942\u0924\u094D\u0930",
  "Mutation": "\u0909\u0924\u094D\u092A\u0930\u093F\u0935\u0930\u094D\u0924\u0928",
  "Photosynthesis": "\u092A\u094D\u0930\u0915\u093E\u0936 \u0938\u0902\u0936\u094D\u0932\u0947\u0937\u0923",
  "Respiration": "\u0936\u094D\u0935\u0938\u0928",
  "Mitosis": "\u0938\u092E\u0938\u0942\u0924\u094D\u0930\u0940 \u0935\u093F\u092D\u093E\u091C\u0928",
  "Meiosis": "\u0905\u0930\u094D\u0927\u0938\u0942\u0924\u094D\u0930\u0940 \u0935\u093F\u092D\u093E\u091C\u0928",
  "Antibody": "\u092A\u094D\u0930\u0924\u093F\u0930\u0915\u094D\u0937\u0940",
  "Antigen": "\u092A\u094D\u0930\u0924\u093F\u091C\u0928",
  "Vaccine": "\u091F\u0940\u0915\u093E",
  "Satellite": "\u0909\u092A\u0917\u094D\u0930\u0939",
  "Orbit": "\u0915\u0915\u094D\u0937\u093E",
  "Rocket": "\u0930\u0949\u0915\u0947\u091F",
  "Nuclear Fission": "\u0928\u093E\u092D\u093F\u0915\u0940\u092F \u0935\u093F\u0916\u0902\u0921\u0928",
  "Nuclear Fusion": "\u0928\u093E\u092D\u093F\u0915\u0940\u092F \u0938\u0902\u0932\u092F\u0928",
  // Art & Culture
  "Temple Architecture": "\u092E\u0902\u0926\u093F\u0930 \u0935\u093E\u0938\u094D\u0924\u0941\u0915\u0932\u093E",
  "Nagara Style": "\u0928\u093E\u0917\u0930 \u0936\u0948\u0932\u0940",
  "Dravida Style": "\u0926\u094D\u0930\u0935\u093F\u0921\u093C \u0936\u0948\u0932\u0940",
  "Vesara Style": "\u0935\u0947\u0938\u0930 \u0936\u0948\u0932\u0940",
  "Rock Cut": "\u0936\u0948\u0932 \u0915\u093E\u091F",
  "Stupa": "\u0938\u094D\u0924\u0942\u092A",
  "Vihara": "\u0935\u093F\u0939\u093E\u0930",
  "Chaitya": "\u091A\u0948\u0924\u094D\u092F",
  "Mural": "\u092D\u093F\u0924\u094D\u0924\u093F\u091A\u093F\u0924\u094D\u0930",
  "Miniature": "\u0932\u0918\u0941\u091A\u093F\u0924\u094D\u0930",
  "Raga": "\u0930\u093E\u0917",
  "Tala": "\u0924\u093E\u0932",
  "Mudra": "\u092E\u0941\u0926\u094D\u0930\u093E",
  // Modern History
  "Revolt of 1857": "1857 \u0915\u093E \u0935\u093F\u0926\u094D\u0930\u094B\u0939",
  "Indian National Congress": "\u092D\u093E\u0930\u0924\u0940\u092F \u0930\u093E\u0937\u094D\u091F\u094D\u0930\u0940\u092F \u0915\u093E\u0902\u0917\u094D\u0930\u0947\u0938",
  "Partition of Bengal": "\u092C\u0902\u0917\u093E\u0932 \u0915\u093E \u0935\u093F\u092D\u093E\u091C\u0928",
  "Swadeshi Movement": "\u0938\u094D\u0935\u0926\u0947\u0936\u0940 \u0906\u0902\u0926\u094B\u0932\u0928",
  "Non-Cooperation Movement": "\u0905\u0938\u0939\u092F\u094B\u0917 \u0906\u0902\u0926\u094B\u0932\u0928",
  "Civil Disobedience Movement": "\u0938\u0935\u093F\u0928\u092F \u0905\u0935\u091C\u094D\u091E\u093E \u0906\u0902\u0926\u094B\u0932\u0928",
  "Quit India Movement": "\u092D\u093E\u0930\u0924 \u091B\u094B\u0921\u093C\u094B \u0906\u0902\u0926\u094B\u0932\u0928",
  "Simon Commission": "\u0938\u093E\u0907\u092E\u0928 \u0915\u092E\u0940\u0936\u0928",
  "Government of India Act": "\u092D\u093E\u0930\u0924 \u0938\u0930\u0915\u093E\u0930 \u0905\u0927\u093F\u0928\u093F\u092F\u092E",
  "Cabinet Mission": "\u0915\u0948\u092C\u093F\u0928\u0947\u091F \u092E\u093F\u0936\u0928",
  "Mountbatten Plan": "\u092E\u093E\u0909\u0902\u091F\u092C\u0947\u091F\u0928 \u092F\u094B\u091C\u0928\u093E",
  "Indian Independence Act": "\u092D\u093E\u0930\u0924\u0940\u092F \u0938\u094D\u0935\u0924\u0902\u0924\u094D\u0930\u0924\u093E \u0905\u0927\u093F\u0928\u093F\u092F\u092E"
};
var PROSE_KEYS = /* @__PURE__ */ new Set([
  "content",
  "definition",
  "explanation",
  "importanceInUpsc",
  "introduction",
  "body",
  "conclusion",
  "clarification",
  "relationship",
  "description"
]);
function normalizeContent(data) {
  function normalize(obj, key = "") {
    if (typeof obj === "string") {
      let text = obj;
      text = text.trim();
      text = text.replace(/  +/g, " ");
      text = text.split("\n").map((line) => line.trimEnd()).join("\n");
      text = text.replace(/^[-*→]\s/gm, "\u2022 ");
      if (PROSE_KEYS.has(key) && text.length > 20 && !text.endsWith(".") && !text.endsWith("?") && !text.endsWith("!") && !text.endsWith(":") && !text.endsWith("\n")) {
        text += ".";
      }
      const monthAbbr = /(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})/g;
      const monthFull = {
        Jan: "January",
        Feb: "February",
        Mar: "March",
        Apr: "April",
        May: "May",
        Jun: "June",
        Jul: "July",
        Aug: "August",
        Sep: "September",
        Oct: "October",
        Nov: "November",
        Dec: "December"
      };
      text = text.replace(monthAbbr, (match, m, y) => `${monthFull[m] || m} ${y}`);
      text = text.replace(/(\d+)-(\d+)/g, "$1\u2013$2");
      text = text.replace(/\.  +/g, ". ");
      return text;
    }
    if (Array.isArray(obj)) {
      return obj.map((item, i) => normalize(item, key));
    }
    if (typeof obj === "object" && obj !== null) {
      const result = {};
      for (const [k, value] of Object.entries(obj)) {
        result[k] = normalize(value, k);
      }
      return result;
    }
    return obj;
  }
  return normalize(data);
}
var STRUCTURAL_KEYS = /* @__PURE__ */ new Set([
  "id",
  "letter",
  "correct",
  "correctAnswer",
  "correctMapping",
  "left",
  "right",
  "type",
  "marks",
  "number",
  "icon",
  "difficulty",
  "estimatedReadingTime"
]);
async function translateToBilingual(englishJson, translateFn, glossary = {}) {
  if (!englishJson) return null;
  const mergedGlossary = { ...DEFAULT_GLOSSARY, ...glossary };
  function applyGlossary2(text) {
    let result = text;
    for (const [en, hi] of Object.entries(mergedGlossary)) {
      const escaped = en.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      const regex = new RegExp(`\\b${escaped}\\b`, "gi");
      result = result.replace(regex, hi);
    }
    return result;
  }
  async function translate(obj, key = "") {
    if (STRUCTURAL_KEYS.has(key)) {
      return obj;
    }
    if (typeof obj === "string") {
      const glossaryApplied = applyGlossary2(obj);
      const hi = await translateFn(glossaryApplied, "hi");
      return { en: obj, hi };
    }
    if (Array.isArray(obj)) {
      return await Promise.all(obj.map((item, i) => translate(item, key)));
    }
    if (typeof obj === "object" && obj !== null) {
      const result = {};
      for (const [k, value] of Object.entries(obj)) {
        result[k] = await translate(value, k);
      }
      return result;
    }
    return obj;
  }
  return await translate(englishJson);
}
async function generateContentHash(data) {
  return await generateSha256Hash(data);
}
var PageScorer = class {
  constructor(meta2) {
    this.meta = meta2;
    this.scores = {};
  }
  score(tabName, data) {
    const scores = {
      seo: this.scoreSeo(),
      coverage: this.scoreCoverage(tabName, data),
      duplication: this.scoreDuplication(data),
      readability: this.scoreReadability(data),
      upscQuality: this.scoreUpscQuality(tabName, data),
      hallucinationRisk: this.scoreHallucinationRisk(data)
    };
    const weights = {
      seo: 0.1,
      coverage: 0.25,
      duplication: 0.15,
      readability: 0.15,
      upscQuality: 0.25,
      hallucinationRisk: 0.1
    };
    let overall = 0;
    for (const [dim, score] of Object.entries(scores)) {
      overall += score * (weights[dim] || 0);
    }
    return {
      dimensions: scores,
      overall: Math.round(overall),
      passed: overall >= 90,
      tabName,
      timestamp: (/* @__PURE__ */ new Date()).toISOString()
    };
  }
  scoreSeo() {
    let score = 100;
    const desc = this.meta.description || "";
    if (desc.length < 50) score -= 20;
    if (desc.length > 160) score -= 10;
    if (!this.meta.canonicalUrl) score -= 15;
    if (!this.meta.topicId) score -= 10;
    const title = `${this.meta.name} | UPSC ${this.meta.category} | SJMaths`;
    if (title.length > 70) score -= 10;
    return Math.max(0, score);
  }
  scoreCoverage(tabName, data) {
    if (!data) return 0;
    let score = 100;
    const wordCount = this.countWords(data);
    const minWords = {
      overview: 50,
      concepts: 200,
      visual: 50,
      comparisons: 100,
      practice: 200,
      mains: 100,
      revision: 50,
      test: 200
    };
    if (wordCount < (minWords[tabName] || 50)) {
      score -= 30;
    }
    const hasEmpty = this.hasEmptyArrays(data);
    if (hasEmpty) score -= 20;
    return Math.max(0, score);
  }
  scoreDuplication(data) {
    if (!data) return 50;
    const strings = [];
    const collect = (obj) => {
      if (typeof obj === "string") strings.push(obj);
      if (Array.isArray(obj)) obj.forEach(collect);
      if (typeof obj === "object" && obj !== null) {
        Object.values(obj).forEach(collect);
      }
    };
    collect(data);
    if (strings.length === 0) return 50;
    const unique = new Set(strings);
    const ratio = unique.size / strings.length;
    return Math.round(ratio * 100);
  }
  scoreReadability(data) {
    if (!data) return 50;
    const text = JSON.stringify(data);
    const sentences = text.split(/[.!?]+/).filter((s) => s.trim().length > 0);
    if (sentences.length === 0) return 50;
    const avgLength = sentences.reduce((sum, s) => sum + s.split(/\s+/).length, 0) / sentences.length;
    if (avgLength < 10) return 60;
    if (avgLength > 40) return 60;
    if (avgLength >= 15 && avgLength <= 25) return 100;
    return 80;
  }
  scoreUpscQuality(tabName, data) {
    if (!data) return 0;
    let score = 70;
    const text = JSON.stringify(data).toLowerCase();
    const upscKeywords = ["prelims", "mains", "upsc", "exam", "pyq", "previous year"];
    const hasUpscKeywords = upscKeywords.some((k) => text.includes(k));
    if (hasUpscKeywords) score += 10;
    if (tabName === "concepts" && text.includes("trap")) score += 10;
    if (tabName === "concepts" && text.includes("common mistake")) score += 10;
    if (tabName === "revision" && text.includes("mnemonic")) score += 10;
    return Math.min(100, score);
  }
  scoreHallucinationRisk(data) {
    if (!data || !this.meta.scope?.neverExplain) return 100;
    const text = JSON.stringify(data).toLowerCase();
    const forbidden = this.meta.scope.neverExplain.map((t) => t.toLowerCase());
    let risk = 0;
    for (const topic of forbidden) {
      if (text.includes(topic)) {
        risk += 20;
      }
    }
    return Math.max(0, 100 - risk);
  }
  countWords(obj) {
    if (typeof obj === "string") return obj.split(/\s+/).length;
    if (Array.isArray(obj)) return obj.reduce((sum, item) => sum + this.countWords(item), 0);
    if (typeof obj === "object" && obj !== null) {
      return Object.values(obj).reduce((sum, val) => sum + this.countWords(val), 0);
    }
    return 0;
  }
  hasEmptyArrays(obj) {
    if (Array.isArray(obj) && obj.length === 0) return true;
    if (typeof obj === "object" && obj !== null) {
      return Object.values(obj).some((v) => this.hasEmptyArrays(v));
    }
    return false;
  }
};
var QualityControl = class {
  constructor(meta2) {
    this.meta = meta2;
    this.errors = [];
    this.warnings = [];
  }
  validate(tabName, data) {
    this.errors = [];
    this.warnings = [];
    if (!data) {
      this.errors.push(`[${tabName}] No data generated`);
      return this.result();
    }
    if (data === null || data === void 0) {
      this.errors.push(`[${tabName}] Data is null/undefined`);
      return this.result();
    }
    const wordCount = this.countWords(data);
    const limits = { overview: 250, concepts: 2e3, visual: 500, comparisons: 1e3, revision: 400 };
    if (limits[tabName] && wordCount > limits[tabName]) {
      this.warnings.push(`[${tabName}] Word count ${wordCount} exceeds limit ${limits[tabName]}`);
    }
    this.checkEmpty(data, tabName);
    this.checkDuplicates(data, tabName);
    if (this.meta.scope?.neverExplain) {
      this.checkForbiddenTopics(data, tabName);
    }
    this.checkRequiredSections(tabName, data);
    return this.result();
  }
  countWords(obj) {
    if (typeof obj === "string") return obj.split(/\s+/).length;
    if (Array.isArray(obj)) return obj.reduce((sum, item) => sum + this.countWords(item), 0);
    if (typeof obj === "object" && obj !== null) {
      return Object.values(obj).reduce((sum, val) => sum + this.countWords(val), 0);
    }
    return 0;
  }
  checkEmpty(obj, path2) {
    if (Array.isArray(obj) && obj.length === 0) {
      this.warnings.push(`[${path2}] Empty array`);
    }
    if (typeof obj === "object" && obj !== null) {
      for (const [key, value] of Object.entries(obj)) {
        this.checkEmpty(value, `${path2}.${key}`);
      }
    }
  }
  checkDuplicates(obj, path2) {
    const strings = [];
    const collect = (o, p) => {
      if (typeof o === "string") {
        if (strings.includes(o)) {
          this.warnings.push(`[${p}] Duplicate text found`);
        }
        strings.push(o);
      }
      if (Array.isArray(o)) o.forEach((item, i) => collect(item, `${p}[${i}]`));
      if (typeof o === "object" && o !== null) {
        for (const [k, v] of Object.entries(o)) collect(v, `${p}.${k}`);
      }
    };
    collect(obj, path2);
  }
  checkForbiddenTopics(obj, path2) {
    const forbidden = this.meta.scope.neverExplain.map((t) => t.toLowerCase());
    const text = JSON.stringify(obj).toLowerCase();
    for (const topic of forbidden) {
      if (text.includes(topic)) {
        this.warnings.push(`[${path2}] Contains forbidden topic: "${topic}"`);
      }
    }
  }
  checkRequiredSections(tabName, data) {
    const required = {
      overview: ["title", "definition", "importanceInUpsc", "learningOutcomes"],
      concepts: ["sections", "keyTakeaways"],
      visual: ["visualBlocks"],
      comparisons: ["differenceTables"],
      practice: ["levels"],
      mains: ["questions"],
      revision: ["onePageNotes", "examDaySheet"],
      test: ["mcq", "statementBased"]
    };
    const sections = required[tabName] || [];
    for (const section of sections) {
      if (!data[section]) {
        this.errors.push(`[${tabName}] Missing required section: "${section}"`);
      }
    }
  }
  result() {
    return {
      passed: this.errors.length === 0,
      errors: this.errors,
      warnings: this.warnings
    };
  }
};
function generateFaqSchema(meta2, overviewData) {
  const faqs = [];
  if (overviewData?.definition) {
    faqs.push({
      "@type": "Question",
      name: `What is ${meta2.name}?`,
      acceptedAnswer: {
        "@type": "Answer",
        text: typeof overviewData.definition === "string" ? overviewData.definition : overviewData.definition.en || ""
      }
    });
  }
  if (overviewData?.importanceInUpsc) {
    faqs.push({
      "@type": "Question",
      name: `Why is ${meta2.name} important for UPSC?`,
      acceptedAnswer: {
        "@type": "Answer",
        text: typeof overviewData.importanceInUpsc === "string" ? overviewData.importanceInUpsc : overviewData.importanceInUpsc.en || ""
      }
    });
  }
  if (meta2.scope?.mustExplain && meta2.scope.mustExplain.length > 0) {
    faqs.push({
      "@type": "Question",
      name: `What are the key topics in ${meta2.name}?`,
      acceptedAnswer: {
        "@type": "Answer",
        text: `The key topics include: ${meta2.scope.mustExplain.join(", ")}.`
      }
    });
  }
  if (meta2.studyTime) {
    const totalTime = Object.values(meta2.studyTime).reduce((a, b) => a + b, 0);
    faqs.push({
      "@type": "Question",
      name: `How much time should I spend on ${meta2.name} for UPSC?`,
      acceptedAnswer: {
        "@type": "Answer",
        text: `You should spend approximately ${totalTime} minutes: ${meta2.studyTime.concepts || 0} minutes on concepts, ${meta2.studyTime.practice || 0} minutes on practice, and ${meta2.studyTime.revision || 0} minutes on revision.`
      }
    });
  }
  if (meta2.difficulty) {
    const difficultyMap = {
      easy: "Easy \u2014 suitable for beginners",
      medium: "Medium \u2014 requires conceptual understanding",
      hard: "Hard \u2014 requires in-depth analysis and practice"
    };
    faqs.push({
      "@type": "Question",
      name: `What is the difficulty level of ${meta2.name}?`,
      acceptedAnswer: {
        "@type": "Answer",
        text: difficultyMap[meta2.difficulty] || meta2.difficulty
      }
    });
  }
  if (faqs.length === 0) return null;
  return {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    mainEntity: faqs
  };
}
function promptOverview(meta2) {
  return `You are a UPSC faculty member. Write a brief overview for the microtopic "${meta2.name}".

TOPIC CONTEXT:
- Subject: ${meta2.subject}
- Parent Topic: ${meta2.parentTopic}
- Category: ${meta2.category}
- Difficulty: ${meta2.difficulty || "medium"}

SCOPE (stay within these boundaries):
- Must explain: ${(meta2.scope?.mustExplain || []).join(", ")}
- May mention: ${(meta2.scope?.mayMention || []).join(", ")}
- NEVER explain: ${(meta2.scope?.neverExplain || []).join(", ")}

RULES:
- Max 250 words total
- Do NOT explain concepts (that's Tab 2)
- Do NOT compare with other topics (that's Tab 4)
- Output ONLY valid JSON

Output this exact JSON:
{
  "title": "Topic Name",
  "definition": "One sentence definition.",
  "importanceInUpsc": "2-3 sentences on why this matters for UPSC Prelims/Mains.",
  "learningOutcomes": ["Outcome 1", "Outcome 2", "Outcome 3"],
  "prerequisites": ["Prerequisite Topic 1", "Prerequisite Topic 2"],
  "estimatedReadingTime": 15
}`;
}
function promptConcepts(meta2) {
  return `You are a UPSC faculty member. Write detailed concept notes for "${meta2.name}".

TOPIC CONTEXT:
- Subject: ${meta2.subject}
- Parent Topic: ${meta2.parentTopic}
- Category: ${meta2.category}
- Difficulty: ${meta2.difficulty || "medium"}

SCOPE (CRITICAL \u2014 stay within these boundaries):
- Must explain thoroughly: ${(meta2.scope?.mustExplain || []).join(", ")}
- May mention briefly: ${(meta2.scope?.mayMention || []).join(", ")}
- NEVER explain (belong to other topics): ${(meta2.scope?.neverExplain || []).join(", ")}

RULES:
- Max 2000 words
- Explain ONLY concepts that belong to this microtopic
- NEVER explain sibling microtopics
- NEVER compare with other topics (that's Tab 4)
- Output ONLY valid JSON

Output this JSON:
{
  "sections": [
    {
      "title": "Section Title",
      "type": "paragraph",
      "content": "Full explanation with key terms in **bold**."
    },
    {
      "title": "Classification Table",
      "type": "table",
      "headers": ["Column 1", "Column 2", "Column 3"],
      "rows": [
        ["Row 1 Col 1", "Row 1 Col 2", "Row 1 Col 3"],
        ["Row 2 Col 1", "Row 2 Col 2", "Row 2 Col 3"]
      ]
    },
    {
      "title": "Key Characteristics",
      "type": "list",
      "items": [
        { "term": "Characteristic 1", "definition": "Explanation." },
        { "term": "Characteristic 2", "definition": "Explanation." }
      ]
    },
    {
      "title": "Sub-concepts",
      "type": "subcards",
      "items": [
        { "title": "Sub-concept 1", "content": "Explanation." },
        { "title": "Sub-concept 2", "content": "Explanation." }
      ]
    }
  ],
  "upscNotes": [
    { "type": "trap", "content": "Common mistake students make." },
    { "type": "tip", "content": "Exam-specific insight." },
    { "type": "fact", "content": "High-yield fact for Prelims." }
  ],
  "keyTakeaways": [
    "Takeaway 1",
    "Takeaway 2",
    "Takeaway 3"
  ]
}`;
}
function promptVisual(meta2) {
  return `You are a UPSC faculty member. Create visual learning aids for "${meta2.name}".

SCOPE:
- Must explain: ${(meta2.scope?.mustExplain || []).join(", ")}
- NEVER explain: ${(meta2.scope?.neverExplain || []).join(", ")}

RULES:
- Max 500 words total (mostly labels)
- No paragraphs \u2014 only visual structures
- No SVG, no HTML
- Output ONLY valid JSON

Output this JSON using the generic visualBlocks array:
{
  "visualBlocks": [
    {
      "type": "timeline",
      "title": "Chronological Development",
      "data": [
        { "label": "Period 1", "description": "Key event" },
        { "label": "Period 2", "description": "Key event" },
        { "label": "Period 3", "description": "Key event" }
      ]
    },
    {
      "type": "flow",
      "title": "Process Flow",
      "data": ["Step 1", "Step 2", "Step 3", "Step 4"]
    },
    {
      "type": "tree",
      "title": "Classification Hierarchy",
      "data": {
        "root": "Central Concept",
        "branches": [
          { "label": "Branch 1", "children": ["Sub 1a", "Sub 1b"] },
          { "label": "Branch 2", "children": ["Sub 2a", "Sub 2b"] }
        ]
      }
    },
    {
      "type": "table",
      "title": "Data Summary",
      "headers": ["Header 1", "Header 2"],
      "rows": [["Value 1", "Value 2"], ["Value 3", "Value 4"]]
    }
  ]
}

Use only the types you need. You can include 0-4 blocks.`;
}
function promptComparisons(meta2) {
  return `You are a UPSC faculty member. Create comparison tables for "${meta2.name}".

This is the ONLY section where you may discuss other microtopics.

SCOPE:
- Current topic: ${meta2.name}
- Related topics (may reference): ${(meta2.scope?.relatedTopics || []).join(", ")}
- May mention: ${(meta2.scope?.mayMention || []).join(", ")}
- NEVER explain fully: ${(meta2.scope?.neverExplain || []).join(", ")}

RULES:
- Max 1000 words
- Only tables and brief connections \u2014 no detailed explanations
- Output ONLY valid JSON

Output this JSON:
{
  "differenceTables": [
    {
      "title": "${meta2.name} vs [Related Topic]",
      "headers": ["Aspect", "${meta2.name}", "[Related Topic]"],
      "rows": [
        ["Aspect 1", "Value for current", "Value for related"],
        ["Aspect 2", "Value for current", "Value for related"]
      ]
    }
  ],
  "similarityTables": [
    {
      "title": "Similarities",
      "headers": ["Shared Aspect", "Description"],
      "rows": [["Aspect 1", "How they are similar"]]
    }
  ],
  "evolution": {
    "title": "Evolutionary Progression",
    "steps": ["Previous Stage", "${meta2.name}", "Next Stage"]
  },
  "frequentlyConfused": [
    {
      "topicA": "${meta2.name}",
      "topicB": "[Confused Topic]",
      "clarification": "1-2 sentence clarification."
    }
  ],
  "conceptConnections": [
    {
      "from": "Concept A within this topic",
      "to": "Concept B within this topic",
      "relationship": "How they connect."
    }
  ]
}`;
}
function promptPractice(meta2) {
  const types = meta2.practiceTypes || ["basic", "conceptual", "statement", "assertion", "match", "advanced"];
  const typeDescriptions = {
    basic: `"basic": [
      { "id": 1, "question": "Simple recall question?", "options": [
        {"letter":"A","text":"Option 1","correct":false},
        {"letter":"B","text":"Option 2","correct":true},
        {"letter":"C","text":"Option 3","correct":false},
        {"letter":"D","text":"Option 4","correct":false}
      ], "explanation": "Why this is correct." }
    ]`,
    conceptual: `"conceptual": [ /* same structure as basic */ ]`,
    statement: `"statementBased": [
      { "id": 11, "question": "Consider the following statements:", "statements": [
        {"number":1,"text":"Statement 1","correct":true},
        {"number":2,"text":"Statement 2","correct":false},
        {"number":3,"text":"Statement 3","correct":true}
      ], "options": [
        {"letter":"A","text":"1 and 2 only","correct":false},
        {"letter":"B","text":"2 and 3 only","correct":false},
        {"letter":"C","text":"1 and 3 only","correct":true},
        {"letter":"D","text":"1, 2 and 3","correct":false}
      ], "explanation": "Explanation." }
    ]`,
    assertion: `"assertionReason": [
      { "id": 16, "assertion": "Assertion statement.", "reason": "Reason statement.", "options": [
        {"letter":"A","text":"Both A and R are true and R is the correct explanation of A","correct":true},
        {"letter":"B","text":"Both A and R are true but R is NOT the correct explanation of A","correct":false},
        {"letter":"C","text":"A is true but R is false","correct":false},
        {"letter":"D","text":"A is false but R is true","correct":false}
      ], "explanation": "Explanation." }
    ]`,
    match: `"match": [
      { "id": 19, "question": "Match List I with List II:", "pairs": [
        {"left":"A","right":"1"},
        {"left":"B","right":"2"},
        {"left":"C","right":"3"}
      ], "correctMapping": "A-1, B-2, C-3", "explanation": "Explanation." }
    ]`,
    advanced: `"advanced": [ /* same structure as basic */ ]`
  };
  const typeSection = types.map((t) => typeDescriptions[t] || "").filter(Boolean).join(",\n");
  return `You are a UPSC faculty member. Create practice questions for "${meta2.name}".

SCOPE:
- Must test: ${(meta2.scope?.mustExplain || []).join(", ")}
- Keywords: ${(meta2.scope?.keywords || []).join(", ")}

RULES:
- Max 30 questions total across all types
- Every question MUST have an explanation
- Questions must be relevant to UPSC exam pattern
- Output ONLY valid JSON

Output this JSON (only include the question types listed):
{
  "levels": {
    ${typeSection}
  }
}`;
}
function promptMains(meta2) {
  return `You are a UPSC faculty member. Create mains answer writing content for "${meta2.name}".

SCOPE:
- Must explain: ${(meta2.scope?.mustExplain || []).join(", ")}
- Keywords: ${(meta2.scope?.keywords || []).join(", ")}

RULES:
- Max 3 questions (one per mark type)
- Output ONLY valid JSON

Output this JSON:
{
  "questions": [
    {
      "marks": 10,
      "question": "10-mark question?",
      "structure": ["Intro point", "Body point 1", "Body point 2", "Conclusion"],
      "keywords": ["keyword1", "keyword2"],
      "modelAnswer": {
        "introduction": "2-3 sentence intro.",
        "body": "Key arguments and evidence.",
        "conclusion": "1-2 sentence conclusion."
      },
      "valueAddition": ["Relevant fact or data point"],
      "diagram": {
        "type": "flow",
        "data": ["Step 1", "Step 2", "Step 3"]
      }
    }
  ]
}`;
}
function promptRevision(meta2) {
  return `You are a UPSC faculty member. Create ultra-condensed revision notes for "${meta2.name}".

SCOPE:
- Must explain: ${(meta2.scope?.mustExplain || []).join(", ")}
- May mention: ${(meta2.scope?.mayMention || []).join(", ")}
- NEVER explain: ${(meta2.scope?.neverExplain || []).join(", ")}

RULES:
- Max 400 words total
- 95% current topic, 5% related topics only
- No detailed explanations
- Output ONLY valid JSON

Output this JSON:
{
  "onePageNotes": {
    "columns": [
      {
        "title": "Section 1",
        "points": ["Point 1", "Point 2", "Point 3"]
      },
      {
        "title": "Section 2",
        "points": ["Point 1", "Point 2"]
      }
    ]
  },
  "mnemonics": [
    {
      "phrase": "Acronym or phrase",
      "meaning": "What it helps remember",
      "explanation": "How to use it."
    }
  ],
  "flashcards": [
    { "question": "Question?", "answer": "Answer." }
  ],
  "frequentlyConfusedFacts": [
    { "misconception": "Wrong belief", "correction": "Correct fact." }
  ],
  "examDaySheet": {
    "fiveFacts": ["Fact 1", "Fact 2", "Fact 3", "Fact 4", "Fact 5"],
    "threeTraps": ["Trap 1", "Trap 2", "Trap 3"],
    "oneMnemonic": { "phrase": "Quick mnemonic", "meaning": "What it helps remember" }
  }
}`;
}
function promptTest(meta2) {
  return `You are a UPSC faculty member. Create a test for "${meta2.name}".

SCOPE:
- Must test: ${(meta2.scope?.mustExplain || []).join(", ")}
- Keywords: ${(meta2.scope?.keywords || []).join(", ")}

RULES:
- 15 MCQs + 3 Statement Based + 2 Match + 1 Mains = 21 total
- Every question MUST have an explanation
- Output ONLY valid JSON

Output this JSON:
{
  "mcq": [
    {
      "id": 1,
      "question": "Question?",
      "options": [
        {"letter":"A","text":"Option 1"},
        {"letter":"B","text":"Option 2"},
        {"letter":"C","text":"Option 3"},
        {"letter":"D","text":"Option 4"}
      ],
      "correctAnswer": "B",
      "explanation": "Explanation."
    }
  ],
  "statementBased": [
    {
      "id": 16,
      "question": "Consider the following statements:",
      "statements": [
        {"number":1,"text":"Statement 1","correct":true},
        {"number":2,"text":"Statement 2","correct":false},
        {"number":3,"text":"Statement 3","correct":true}
      ],
      "options": [
        {"letter":"A","text":"1 and 2 only","correct":false},
        {"letter":"B","text":"2 and 3 only","correct":false},
        {"letter":"C","text":"1 and 3 only","correct":true},
        {"letter":"D","text":"1, 2 and 3","correct":false}
      ],
      "explanation": "Explanation."
    }
  ],
  "match": [
    {
      "id": 19,
      "question": "Match List I with List II:",
      "pairs": [
        {"left":"A","right":"1"},
        {"left":"B","right":"2"},
        {"left":"C","right":"3"}
      ],
      "correctMapping": "A-1, B-2, C-3",
      "explanation": "Explanation."
    }
  ],
  "mains": {
    "id": 21,
    "question": "Mains question?",
    "marks": 10,
    "modelAnswer": "Brief outline."
  }
}`;
}
var PROMPT_GENERATORS = {
  overview: promptOverview,
  concepts: promptConcepts,
  visual: promptVisual,
  comparisons: promptComparisons,
  practice: promptPractice,
  mains: promptMains,
  revision: promptRevision,
  test: promptTest
};
function generatePrompt(tabName, meta2) {
  const generator = PROMPT_GENERATORS[tabName];
  if (!generator) throw new Error(`Unknown tab: ${tabName}`);
  return generator(meta2);
}
function parseResponse(raw) {
  let cleaned = raw.trim();
  if (cleaned.startsWith("```json")) {
    cleaned = cleaned.replace(/^```json\s*/, "").replace(/\s*```$/, "");
  } else if (cleaned.startsWith("```")) {
    cleaned = cleaned.replace(/^```\s*/, "").replace(/\s*```$/, "");
  }
  try {
    return JSON.parse(cleaned);
  } catch (e) {
    const jsonMatch = cleaned.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      try {
        return JSON.parse(jsonMatch[0]);
      } catch (e2) {
        throw new Error(`Failed to parse JSON: ${e2.message}`);
      }
    }
    throw new Error(`No JSON found in response: ${e.message}`);
  }
}
var RELATED_TOPICS_CARD = `
  <div class="related-topics-card">
    <h2 class="card-title">
      <i class="fas fa-sitemap"></i>
      <span class="lang-en">Related Topics</span>
      <span class="lang-hi">\u0938\u0902\u092C\u0902\u0927\u093F\u0924 \u0935\u093F\u0937\u092F</span>
    </h2>
    <div class="related-topics-grid">
      <div class="related-topic-group">
        <h3><span class="lang-en">Previous Topic</span><span class="lang-hi">\u092A\u093F\u091B\u0932\u093E \u0935\u093F\u0937\u092F</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[PREVIOUS_DIR]/" class="related-topic-link">
          <i class="fas fa-arrow-left"></i>
          <span class="lang-en">[PREVIOUS_TOPIC]</span>
          <span class="lang-hi">[PREVIOUS_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Current Topic</span><span class="lang-hi">\u0935\u0930\u094D\u0924\u092E\u093E\u0928 \u0935\u093F\u0937\u092F</span></h3>
        <span class="related-topic-current">
          <i class="fas fa-circle"></i>
          <span class="lang-en">[TOPIC_NAME]</span>
          <span class="lang-hi">[HINDI_NAME]</span>
        </span>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Next Topic</span><span class="lang-hi">\u0905\u0917\u0932\u093E \u0935\u093F\u0937\u092F</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[NEXT_DIR]/" class="related-topic-link">
          <i class="fas fa-arrow-right"></i>
          <span class="lang-en">[NEXT_TOPIC]</span>
          <span class="lang-hi">[NEXT_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Parent Topic</span><span class="lang-hi">\u092E\u0942\u0932 \u0935\u093F\u0937\u092F</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/" class="related-topic-link">
          <i class="fas fa-level-up-alt"></i>
          <span class="lang-en">[PARENT_TOPIC]</span>
          <span class="lang-hi">[PARENT_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Child Topics</span><span class="lang-hi">\u0909\u092A-\u0935\u093F\u0937\u092F</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[CHILD_DIR]/" class="related-topic-link">
          <span class="lang-en">[CHILD_TOPIC]</span>
          <span class="lang-hi">[CHILD_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Similar Topics</span><span class="lang-hi">\u0938\u092E\u093E\u0928 \u0935\u093F\u0937\u092F</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[SIMILAR_DIR]/" class="related-topic-link">
          <span class="lang-en">[SIMILAR_TOPIC]</span>
          <span class="lang-hi">[SIMILAR_TOPIC_HI]</span>
        </a>
      </div>
      <div class="related-topic-group">
        <h3><span class="lang-en">Frequently Confused With</span><span class="lang-hi">\u0905\u0915\u094D\u0938\u0930 \u092D\u094D\u0930\u092E\u093F\u0924</span></h3>
        <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/[CONFUSED_DIR]/" class="related-topic-link confused">
          <i class="fas fa-question-circle"></i>
          <span class="lang-en">[CONFUSED_TOPIC]</span>
          <span class="lang-hi">[CONFUSED_TOPIC_HI]</span>
        </a>
      </div>
    </div>
  </div>
`;
var PAGE_TEMPLATE = `<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7924751316191829" crossorigin="anonymous"></script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[SEO_TITLE]</title>
    <meta name="description" content="[SEO_DESCRIPTION]">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <link rel="canonical" href="[CANONICAL_URL]">
    <meta name="keywords" content="[SEO_KEYWORDS]">
    <meta name="author" content="SJMaths">
    <link rel="icon" type="image/png" href="/favicon.png">

    <!-- Fonts and Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    <link rel="preload" as="style" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c" onload="this.onload=null;this.rel='stylesheet'" crossorigin="anonymous">
    <noscript><link rel="stylesheet" href="/assets/vendor/fontawesome/css/all.min.css?v=7441465c"></noscript>

    <!-- Stylesheets -->
    <link rel="stylesheet" href="/assets/css/main.min.css?v=4ba21ce7">
    <link rel="stylesheet" href="/assets/css/layout.min.css?v=e4922b08">
    <link rel="stylesheet" href="/assets/css/component.min.css?v=8c99f11f">
    <link rel="stylesheet" href="/assets/css/improved-ui.min.css?v=86f5556a">
    <link rel="stylesheet" href="/assets/css/pages.min.css?v=9e3bd560">
    <link rel="stylesheet" href="/assets/css/competitive-exam-guide.min.css?v=bcdc8e39">

    <!-- Open Graph -->
    <meta property="og:title" content="[OG_TITLE]">
    <meta property="og:description" content="[OG_DESCRIPTION]">
    <meta property="og:type" content="article">
    <meta property="og:url" content="[CANONICAL_URL]">
    <meta property="og:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="[OG_TITLE]">
    <meta name="twitter:description" content="[OG_DESCRIPTION]">
    <meta name="twitter:image" content="https://sjmaths.com/assets/icons/icon-512x512.png">

    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "BreadcrumbList",
          "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://sjmaths.com/" },
            { "@type": "ListItem", "position": 2, "name": "UPSC IAS Prep", "item": "https://sjmaths.com/upsc/" },
            { "@type": "ListItem", "position": 3, "name": "[SUBJECT]", "item": "https://sjmaths.com/upsc/[SUBJECT_DIR]/" },
            { "@type": "ListItem", "position": 4, "name": "[PARENT_TOPIC]", "item": "https://sjmaths.com/upsc/[SUBJECT_DIR]/[PARENT_DIR]/" },
            { "@type": "ListItem", "position": 5, "name": "[TOPIC_NAME]", "item": "[CANONICAL_URL]" }
          ]
        },
        {
          "@type": "LearningResource",
          "name": "[TOPIC_NAME]",
          "description": "[SEO_DESCRIPTION]",
          "learningResourceType": "Study Notes",
          "educationalLevel": "UPSC Civil Services / IAS",
          "url": "[CANONICAL_URL]"
        }
      ]
    }
    </script>

    <!-- FAQ Schema (auto-generated) -->
    <script type="application/ld+json">[FAQ_SCHEMA]</script>
</head>
<body>
    <div id="header-container"></div>

    <main class="topic-container" id="main-content">
        <div class="breadcrumbs">
            <div class="breadcrumbs-path">
                <a href="/">Home</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/">UPSC</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/[SUBJECT_DIR]/">[SUBJECT]</a>
                <i class="fas fa-chevron-right"></i>
                <a href="/upsc/[SUBJECT_DIR]/[PARENT_DIR]/">[PARENT_TOPIC]</a>
                <i class="fas fa-chevron-right"></i>
                <span class="lang-en">[TOPIC_NAME]</span>
                <span class="lang-hi">[HINDI_NAME]</span>
            </div>
        </div>

        <div class="topic-header">
            <h1>
                <span class="lang-en">[TOPIC_NAME]</span>
                <span class="lang-hi">[HINDI_NAME]</span>
            </h1>
            <p class="topic-desc">
                <span class="lang-en">[SEO_DESCRIPTION]</span>
                <span class="lang-hi">[HINDI_DESCRIPTION]</span>
            </p>
            <div class="topic-meta-bar">
                <span class="topic-difficulty [DIFFICULTY_CLASS]">
                    <i class="fas fa-signal"></i>
                    <span class="lang-en">[DIFFICULTY_LABEL]</span>
                    <span class="lang-hi">[DIFFICULTY_LABEL_HI]</span>
                </span>
                <span class="topic-study-time">
                    <i class="fas fa-clock"></i>
                    <span class="lang-en">[STUDY_TIME_LABEL]</span>
                    <span class="lang-hi">[STUDY_TIME_LABEL_HI]</span>
                </span>
            </div>
        </div>

        <!-- 10-Tab Navigation -->
        <div class="study-tabs" role="tablist" aria-label="Topic resources">
            <button class="tab-btn active" data-tab="tab-overview" role="tab" aria-selected="true">
                <i class="fas fa-compass"></i> <span class="lang-en">1. Overview</span><span class="lang-hi">1. \u0905\u0935\u0932\u094B\u0915\u0928</span>
            </button>
            <button class="tab-btn" data-tab="tab-concepts" role="tab" aria-selected="false">
                <i class="fas fa-book-open"></i> <span class="lang-en">2. Concepts</span><span class="lang-hi">2. \u0905\u0935\u0927\u093E\u0930\u0923\u093E\u090F\u0901</span>
            </button>
            <button class="tab-btn" data-tab="tab-visual" role="tab" aria-selected="false">
                <i class="fas fa-diagram-project"></i> <span class="lang-en">3. Visual</span><span class="lang-hi">3. \u0926\u0943\u0936\u094D\u092F</span>
            </button>
            <button class="tab-btn" data-tab="tab-comparisons" role="tab" aria-selected="false">
                <i class="fas fa-scale-balanced"></i> <span class="lang-en">4. Comparisons</span><span class="lang-hi">4. \u0924\u0941\u0932\u0928\u093E</span>
            </button>
            <button class="tab-btn" data-tab="tab-current-affairs" role="tab" aria-selected="false">
                <i class="fas fa-newspaper"></i> <span class="lang-en">5. Current Affairs</span><span class="lang-hi">5. \u0938\u092E\u0938\u093E\u092E\u092F\u093F\u0915</span>
            </button>
            <button class="tab-btn" data-tab="tab-pyqs" role="tab" aria-selected="false">
                <i class="fas fa-clock-rotate-left"></i> <span class="lang-en">6. PYQs</span><span class="lang-hi">6. PYQs</span>
            </button>
            <button class="tab-btn" data-tab="tab-practice" role="tab" aria-selected="false">
                <i class="fas fa-list-check"></i> <span class="lang-en">7. Practice</span><span class="lang-hi">7. \u0905\u092D\u094D\u092F\u093E\u0938</span>
            </button>
            <button class="tab-btn" data-tab="tab-mains" role="tab" aria-selected="false" id="mains-tab-btn" style="display:none">
                <i class="fas fa-pen-fancy"></i> <span class="lang-en">8. Mains</span><span class="lang-hi">8. \u092E\u0947\u0902\u0938</span>
            </button>
            <button class="tab-btn" data-tab="tab-revision" role="tab" aria-selected="false">
                <i class="fas fa-rotate"></i> <span class="lang-en">9. Revision</span><span class="lang-hi">9. \u092A\u0941\u0928\u0930\u093E\u0935\u0943\u0924\u094D\u0924\u093F</span>
            </button>
            <button class="tab-btn" data-tab="tab-test" role="tab" aria-selected="false">
                <i class="fas fa-graduation-cap"></i> <span class="lang-en">10. Test</span><span class="lang-hi">10. \u091F\u0947\u0938\u094D\u091F</span>
            </button>
        </div>

        <!-- Tab Content -->
        <div class="topic-content" id="topic-content"></div>

        <!-- Related Topics Card -->
        [RELATED_TOPICS_HTML]
    </main>

    <!-- Page data as JSON -->
    <script id="upsc-page-data" type="application/json">
    {
        "topicId": "[TOPIC_ID]",
        "topicName": "[TOPIC_NAME]",
        "hindiName": "[HINDI_NAME]",
        "subject": "[SUBJECT]",
        "subjectDir": "[SUBJECT_DIR]",
        "parentTopic": "[PARENT_TOPIC]",
        "parentDir": "[PARENT_DIR]",
        "previousTopic": "[PREVIOUS_TOPIC]",
        "previousDir": "[PREVIOUS_DIR]",
        "nextTopic": "[NEXT_TOPIC]",
        "nextDir": "[NEXT_DIR]",
        "difficulty": "[DIFFICULTY]",
        "studyTime": [STUDY_TIME_JSON],
        "learningObjectives": [LEARNING_OBJECTIVES_JSON],
        "supportsMains": [SUPPORTS_MAINS],
        "overview": [OVERVIEW_JSON],
        "concepts": [CONCEPTS_JSON],
        "visual": [VISUAL_JSON],
        "comparisons": [COMPARISONS_JSON],
        "practice": [PRACTICE_JSON],
        "mains": [MAINS_JSON],
        "revision": [REVISION_JSON],
        "version": {
            "generator": "[GENERATOR_VERSION]",
            "prompt": "[PROMPT_VERSION]",
            "translator": "[TRANSLATOR_VERSION]",
            "normalizer": "[NORMALIZER_VERSION]"
        },
        "contentHash": "[CONTENT_HASH]",
        "generatedAt": "[GENERATED_AT]"
    }
    </script>

    <!-- Reusable renderers -->
    <script src="/assets/js/upsc-renderer.min.js" defer></script>
    <script src="/assets/js/upsc-test.min.js" defer></script>
    <script src="/assets/js/upsc-current-affairs.min.js" defer></script>
    <script src="/assets/js/upsc-pyq-loader.min.js" defer></script>

    <script src="/assets/js/search.min.js?v=68a0a505" defer data-cfasync="false"></script>
    <script src="/assets/js/main.min.js?v=10f0770d" defer data-cfasync="false"></script>
    <script src="/assets/js/global-header.min.js?v=d6ad26b3" defer data-cfasync="false"></script>
    <script src="/assets/js/global-footer.min.js?v=c641c625" defer data-cfasync="false"></script>
</body>
</html>`;
function assemblePage(meta2, bilingualData, score) {
  let html = PAGE_TEMPLATE;
  const difficultyLabels = {
    easy: { en: "Easy", hi: "\u0938\u0930\u0932" },
    medium: { en: "Medium", hi: "\u092E\u0927\u094D\u092F\u092E" },
    hard: { en: "Hard", hi: "\u0915\u0920\u093F\u0928" }
  };
  const diff = difficultyLabels[meta2.difficulty] || difficultyLabels.medium;
  const studyTime = meta2.studyTime || { concepts: 15, practice: 10, revision: 5 };
  const totalTime = Object.values(studyTime).reduce((a, b) => a + b, 0);
  const objectives = meta2.learningObjectives || [];
  const contentHash = generateContentHash(bilingualData);
  const faqSchema = generateFaqSchema(meta2, bilingualData.overview);
  const replacements = {
    "[SEO_TITLE]": `${meta2.name} | UPSC ${meta2.category} | SJMaths`,
    "[SEO_DESCRIPTION]": meta2.description,
    "[SEO_KEYWORDS]": `UPSC ${meta2.name}, ${meta2.subject} ${meta2.name}, UPSC ${meta2.category} ${meta2.name}`,
    "[CANONICAL_URL]": meta2.canonicalUrl,
    "[OG_TITLE]": `${meta2.name} - UPSC ${meta2.category} | SJMaths`,
    "[OG_DESCRIPTION]": meta2.description,
    "[TOPIC_NAME]": meta2.name,
    "[HINDI_NAME]": meta2.hindiName,
    "[HINDI_DESCRIPTION]": meta2.hindiDescription || meta2.description,
    "[SUBJECT]": meta2.subject,
    "[SUBJECT_DIR]": meta2.subjectDir,
    "[PARENT_TOPIC]": meta2.parentTopic,
    "[PARENT_DIR]": meta2.parentDir,
    "[TOPIC_ID]": meta2.topicId || `${meta2.subjectDir}.${meta2.parentDir}.${meta2.dir}`,
    "[SUPPORTS_MAINS]": meta2.supportsMains ? "true" : "false",
    "[PREVIOUS_TOPIC]": meta2.previousTopic || "",
    "[PREVIOUS_DIR]": meta2.previousDir || "",
    "[NEXT_TOPIC]": meta2.nextTopic || "",
    "[NEXT_DIR]": meta2.nextDir || "",
    "[DIFFICULTY]": meta2.difficulty || "medium",
    "[DIFFICULTY_CLASS]": `difficulty-${meta2.difficulty || "medium"}`,
    "[DIFFICULTY_LABEL]": diff.en,
    "[DIFFICULTY_LABEL_HI]": diff.hi,
    "[STUDY_TIME_LABEL]": `${totalTime} min total (Concepts: ${studyTime.concepts || 0}m, Practice: ${studyTime.practice || 0}m, Revision: ${studyTime.revision || 0}m)`,
    "[STUDY_TIME_LABEL_HI]": `\u0915\u0941\u0932 ${totalTime} \u092E\u093F\u0928\u091F (\u0905\u0935\u0927\u093E\u0930\u0923\u093E\u090F\u0901: ${studyTime.concepts || 0}\u092E\u093F, \u0905\u092D\u094D\u092F\u093E\u0938: ${studyTime.practice || 0}\u092E\u093F, \u092A\u0941\u0928\u0930\u093E\u0935\u0943\u0924\u094D\u0924\u093F: ${studyTime.revision || 0}\u092E\u093F)`,
    "[GENERATOR_VERSION]": VERSION.generator,
    "[PROMPT_VERSION]": VERSION.prompt,
    "[TRANSLATOR_VERSION]": VERSION.translator,
    "[NORMALIZER_VERSION]": VERSION.normalizer,
    "[CONTENT_HASH]": contentHash,
    "[GENERATED_AT]": (/* @__PURE__ */ new Date()).toISOString(),
    "[FAQ_SCHEMA]": JSON.stringify(faqSchema || {})
  };
  for (const [key, value] of Object.entries(replacements)) {
    html = html.replace(new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g"), value);
  }
  html = html.replace("[OVERVIEW_JSON]", JSON.stringify(bilingualData.overview));
  html = html.replace("[CONCEPTS_JSON]", JSON.stringify(bilingualData.concepts));
  html = html.replace("[VISUAL_JSON]", JSON.stringify(bilingualData.visual));
  html = html.replace("[COMPARISONS_JSON]", JSON.stringify(bilingualData.comparisons));
  html = html.replace("[PRACTICE_JSON]", JSON.stringify(bilingualData.practice));
  html = html.replace("[MAINS_JSON]", JSON.stringify(bilingualData.mains));
  html = html.replace("[REVISION_JSON]", JSON.stringify(bilingualData.revision));
  html = html.replace("[STUDY_TIME_JSON]", JSON.stringify(studyTime));
  html = html.replace("[LEARNING_OBJECTIVES_JSON]", JSON.stringify(objectives));
  const buildLinks = (names, dirs, namesHi) => {
    if (!names || names.length === 0) return "";
    return names.map((name, i) => {
      const dir = dirs && dirs[i] ? dirs[i] : name.toLowerCase().replace(/\s+/g, "-");
      const hi = namesHi && namesHi[i] ? namesHi[i] : name;
      return `<a href="/upsc/${meta2.subjectDir}/${meta2.parentDir}/${dir}/" class="related-topic-link">${name}</a>`;
    }).join("\n              ");
  };
  let relatedCard = RELATED_TOPICS_CARD;
  const relatedReplacements = {
    "[TOPIC_NAME]": meta2.name,
    "[HINDI_NAME]": meta2.hindiName,
    "[SUBJECT_DIR]": meta2.subjectDir,
    "[PARENT_DIR]": meta2.parentDir,
    "[PREVIOUS_DIR]": meta2.previousDir || "",
    "[NEXT_DIR]": meta2.nextDir || "",
    "[PREVIOUS_TOPIC]": meta2.previousTopic || "",
    "[PREVIOUS_TOPIC_HI]": meta2.previousTopicHi || meta2.previousTopic || "",
    "[NEXT_TOPIC]": meta2.nextTopic || "",
    "[NEXT_TOPIC_HI]": meta2.nextTopicHi || meta2.nextTopic || "",
    "[PARENT_TOPIC]": meta2.parentTopic || "",
    "[PARENT_TOPIC_HI]": meta2.parentTopicHi || meta2.parentTopic || "",
    "[CHILD_TOPIC]": buildLinks(meta2.childTopics, meta2.childDirs, meta2.childTopicsHi),
    "[SIMILAR_TOPIC]": buildLinks(meta2.similarTopics, meta2.similarDirs, meta2.similarTopicsHi),
    "[CONFUSED_TOPIC]": buildLinks(meta2.confusedTopics, meta2.confusedDirs, meta2.confusedTopicsHi)
  };
  for (const [key, value] of Object.entries(relatedReplacements)) {
    relatedCard = relatedCard.replace(new RegExp(key.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g"), value);
  }
  html = html.replace("[RELATED_TOPICS_HTML]", relatedCard);
  return html;
}
async function generateSha256Hash(data) {
  const json = typeof data === "string" ? data : JSON.stringify(data);
  const encoder = new TextEncoder();
  const bytes = encoder.encode(json);
  if (typeof crypto !== "undefined" && crypto.subtle) {
    const hashBuffer = await crypto.subtle.digest("SHA-256", bytes);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return "sha256-" + hashArray.map((b) => b.toString(16).padStart(2, "0")).join("");
  }
  try {
    const nodeCrypto = require("crypto");
    return "sha256-" + nodeCrypto.createHash("sha256").update(json).digest("hex");
  } catch (e) {
    let hash = 0;
    for (let i = 0; i < json.length; i++) {
      hash = (hash << 5) - hash + json.charCodeAt(i);
      hash = hash & hash;
    }
    return "simple-" + Math.abs(hash).toString(16).padStart(8, "0");
  }
}
function getFocusedRetryPrompt(tabName, score, originalJson) {
  const dims = score.dimensions;
  const issues = [];
  const scope = originalJson.scope || {};
  if (dims.readability < 80) {
    issues.push(`READABILITY: Sentences are too long/short. Rewrite to use 15-25 words per sentence. Break long sentences into shorter ones. Current avg: ${JSON.stringify(originalJson).split(/[.!?]+/).length > 0 ? "needs improvement" : "unknown"}`);
  }
  if (dims.duplication < 80) {
    issues.push(`DUPLICATION: Some text appears multiple times. Remove duplicate sentences and rephrase repeated ideas.`);
  }
  if (dims.coverage < 80) {
    issues.push(`COVERAGE: Some sections are too short. Ensure each subsection has adequate content.`);
  }
  if (dims.upscQuality < 80) {
    issues.push(`UPSC QUALITY: Add more UPSC-specific content: exam tips, trap warnings, common mistakes, high-yield facts.`);
  }
  if (dims.hallucinationRisk < 80) {
    issues.push(`HALLUCINATION RISK: Remove content that explains topics outside this microtopic's scope. Stick to: ${JSON.stringify(scope.mustExplain || [])}`);
  }
  if (issues.length === 0) return null;
  return `You previously generated content for a UPSC microtopic, but it needs improvement in these areas:
${issues.map((i) => `- ${i}`).join("\n")}

KEEP all existing correct content. Only fix the issues listed above.
Output ONLY valid JSON with the same structure as before.`;
}
function createManifest(meta2, tabResults) {
  const tabs = {};
  for (const [tabName, result] of Object.entries(tabResults)) {
    if (result) {
      tabs[tabName] = {
        hash: result.contentHash || "unknown",
        score: result.score?.overall || 0,
        promptVersion: VERSION.prompt,
        attempts: result.attempt || 1
      };
    }
  }
  const allScores = Object.values(tabs).map((t) => t.score);
  const avgScore = allScores.length > 0 ? Math.round(allScores.reduce((a, b) => a + b, 0) / allScores.length) : 0;
  return {
    topicId: meta2.topicId,
    topicName: meta2.name,
    subject: meta2.subject,
    subjectDir: meta2.subjectDir,
    parentTopic: meta2.parentTopic,
    parentDir: meta2.parentDir,
    createdAt: (/* @__PURE__ */ new Date()).toISOString(),
    updatedAt: (/* @__PURE__ */ new Date()).toISOString(),
    generatorVersion: VERSION.generator,
    translatorVersion: VERSION.translator,
    scorerVersion: VERSION.scorer,
    manifestVersion: VERSION.manifest,
    globalScore: avgScore,
    tabs
  };
}
var logCounter = 0;
function createLogEntry(event, details = {}) {
  const entry = {
    id: `gen-${Date.now()}-${++logCounter}`,
    timestamp: (/* @__PURE__ */ new Date()).toISOString(),
    event,
    ...details
  };
  if (typeof console !== "undefined") {
    const prefix = `[Pipeline:${entry.id}]`;
    if (event === "error") {
      console.error(prefix, JSON.stringify(entry, null, 2));
    } else if (event === "warning") {
      console.warn(prefix, JSON.stringify(entry, null, 2));
    } else {
      console.log(prefix, JSON.stringify(entry, null, 2));
    }
  }
  return entry;
}
var GeminiClient = class _GeminiClient {
  constructor(apiKey, options = {}) {
    this.apiKey = apiKey;
    this.model = options.model || "gemini-2.0-flash-lite";
    this.temperature = options.temperature ?? 0.1;
    this.maxRetries = options.maxRetries || 5;
    this.REQUEST_DELAY = options.requestDelay || 13e3;
    this.lastRequestTime = 0;
  }
  /**
   * Gets or creates the singleton instance.
   */
  static getInstance(apiKey, options = {}) {
    if (!_GeminiClient._instance || _GeminiClient._instance.apiKey !== apiKey) {
      _GeminiClient._instance = new _GeminiClient(apiKey, options);
    }
    return _GeminiClient._instance;
  }
  /**
   * Generates content via the Gemini API with:
   *   - Automatic rate limiting (13s delay between requests)
   *   - Exponential backoff on 429 rate limits
   *   - Retry logic (5 attempts by default)
   *   - Structured logging
   * 
   * @param {string} prompt - The prompt text
   * @returns {Promise<string>} The raw response text
   */
  async generate(prompt) {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${this.model}:generateContent?key=${this.apiKey}`;
    for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
      try {
        const elapsed = Date.now() - this.lastRequestTime;
        if (elapsed < this.REQUEST_DELAY) {
          const wait = this.REQUEST_DELAY - elapsed;
          await new Promise((r) => setTimeout(r, wait));
        }
        const startTime = Date.now();
        const res = await fetch(url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            contents: [{ parts: [{ text: prompt }] }],
            generationConfig: { temperature: this.temperature }
          })
        });
        const data = await res.json();
        const duration = Date.now() - startTime;
        this.lastRequestTime = Date.now();
        if (data.error) {
          if (data.error.code === 429) {
            const wait = Math.min(15e3 * Math.pow(2, attempt - 1), 6e4);
            createLogEntry("warning", {
              message: `Rate limited (429) on attempt ${attempt}`,
              wait,
              duration
            });
            await new Promise((r) => setTimeout(r, wait));
            continue;
          }
          throw new Error(`Gemini API error: ${data.error.message}`);
        }
        if (!data.candidates || !data.candidates[0]) {
          throw new Error(`No candidates in response: ${JSON.stringify(data)}`);
        }
        const text = data.candidates[0].content.parts[0].text;
        createLogEntry("success", {
          tabName: "api",
          attempt,
          duration,
          responseLength: text.length
        });
        return text;
      } catch (err) {
        createLogEntry("error", {
          message: err.message,
          attempt,
          maxRetries: this.maxRetries
        });
        if (attempt >= this.maxRetries) throw err;
        await new Promise((r) => setTimeout(r, 5e3 * attempt));
      }
    }
  }
  sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
};

// upsc/run-prehistoric-time-periods.js
if (import_fs.default.existsSync(".env")) {
  const envConfig = import_fs.default.readFileSync(".env", "utf8");
  envConfig.split("\n").forEach((line) => {
    const [key, value] = line.split("=");
    if (key && value) {
      process.env[key.trim()] = value.trim();
    }
  });
}
var meta = {
  name: "Prehistoric Time Periods",
  hindiName: "\u092A\u094D\u0930\u093E\u0910\u0930\u093F\u0936\u093F\u092F\u0928 \u0938\u092E\u092F \u0905\u0935\u0927\u093E\u0930\u0923\u093E\u090F\u0901",
  dir: "Prehistoric-Time-Periods",
  subject: "Ancient History",
  subjectDir: "ancient-history",
  parentTopic: "Prehistory",
  parentDir: "Prehistory",
  previousTopic: "Sources of Information of Pre-History",
  previousDir: "Sources-of-Information-of-Pre-History",
  previousTopicHi: "\u092A\u094D\u0930\u093E\u0910\u0930\u093F\u0936\u093F\u092F\u0928 \u0907\u0924\u093F\u0939\u093E\u0938 \u0915\u0947 \u0938\u094D\u0930\u094B\u0924",
  nextTopic: "History of Paleolithic or Old Stone Age",
  nextDir: "History-of-Paleolithic-or-Old-Stone-Age",
  nextTopicHi: "\u092A\u0941\u0930\u093E\u092A\u093E\u0937\u093E\u0923 \u092F\u093E \u092A\u0941\u0930\u093E\u0928\u093E \u092A\u0924\u094D\u0925\u0930 \u0915\u093E\u0932 \u0915\u093E \u0907\u0924\u093F\u0939\u093E\u0938",
  parentTopicHi: "\u092A\u094D\u0930\u093E\u0910\u0930\u093F\u0936\u093F\u092F\u0928",
  childTopics: [],
  childDirs: [],
  childTopicsHi: [],
  similarTopics: [],
  similarDirs: [],
  similarTopicsHi: [],
  confusedTopics: [],
  confusedDirs: [],
  confusedTopicsHi: [],
  canonicalUrl: "https://sjmaths.com/upsc/ancient-history/Prehistory/Prehistoric-Time-Periods/",
  description: "Comprehensive UPSC GS-1 guide on Prehistoric Time Periods. Study notes, tool typology, timeline, practice questions, and mock tests covering Paleolithic, Mesolithic, Neolithic, and Chalcolithic ages.",
  category: "GS-1",
  supportsMains: true,
  topicId: "ancient-history.prehistory.prehistoric-time-periods",
  practiceTypes: ["basic", "conceptual", "statement", "match"],
  difficulty: "medium",
  studyTime: { concepts: 20, practice: 15, revision: 8 },
  learningObjectives: [
    "Explain the four major prehistoric time periods and their characteristics",
    "Compare tool technologies across Paleolithic, Mesolithic, Neolithic, and Chalcolithic ages",
    "Identify key archaeological sites and their significance in Indian prehistory"
  ],
  scope: {
    mustExplain: [
      "Paleolithic Age characteristics and tool traditions",
      "Mesolithic Age and microlith technology",
      "Neolithic Age and agricultural revolution",
      "Chalcolithic Age and copper metallurgy",
      "Chronological framework of prehistoric periods",
      "Tool typology evolution"
    ],
    mayMention: [
      "Archaeological dating methods",
      "Major prehistoric sites in India",
      "Rock art and cave paintings"
    ],
    neverExplain: [
      "Indus Valley Civilization",
      "Vedic period",
      "Mauryan Empire",
      "Gupta Empire"
    ],
    relatedTopics: [
      "Paleolithic Age",
      "Mesolithic Age",
      "Neolithic Age",
      "Chalcolithic Age"
    ],
    keywords: [
      "prehistory",
      "stone age",
      "paleolithic",
      "mesolithic",
      "neolithic",
      "chalcolithic",
      "microliths",
      "handaxes",
      "agriculture",
      "domestication",
      "archaeology",
      "tool technology",
      "chronological framework"
    ]
  },
  related: {
    prerequisite: ["Sources of Information of Pre-History"],
    recommendedNext: ["History of Paleolithic or Old Stone Age"],
    advancedTopics: ["Bhimbetka Rock Paintings", "Prehistoric Sites of India"]
  },
  hindiDescription: "\u092A\u094D\u0930\u093E\u0910\u0930\u093F\u0936\u093F\u092F\u0928 \u0938\u092E\u092F \u0905\u0935\u0927\u093E\u0930\u0923\u093E\u0913\u0902 \u092A\u0930 UPSC GS-1 \u0915\u0940 \u0935\u094D\u092F\u093E\u092A\u0915 \u0917\u093E\u0907\u0921\u0964 \u0905\u0927\u094D\u092F\u092F\u0928 \u0928\u094B\u091F\u094D\u0938, \u0909\u092A\u0915\u0930\u0923 \u0924\u0915\u0928\u0940\u0915, \u0930\u0947\u0916\u093E\u0902\u0915\u0930\u0923, \u0905\u092D\u094D\u092F\u093E\u0938 \u092A\u094D\u0930\u0936\u094D\u0928 \u0914\u0930 \u092E\u0949\u0915 \u091F\u0947\u0938\u094D\u091F \u091C\u094B \u092A\u0941\u0930\u093E\u092A\u093E\u0937\u093E\u0923, \u092E\u0927\u094D\u092F\u092A\u093E\u0937\u093E\u0923, \u0928\u0935\u092A\u093E\u0937\u093E\u0923 \u0914\u0930 \u0924\u093E\u092E\u094D\u0930\u092A\u093E\u0937\u093E\u0923 \u092F\u0941\u0917\u094B\u0902 \u0915\u094B \u0915\u0935\u0930 \u0915\u0930\u0924\u0947 \u0939\u0948\u0902\u0964"
};
function collectStrings(obj, strings = /* @__PURE__ */ new Set()) {
  if (typeof obj === "string") {
    strings.add(obj);
  } else if (Array.isArray(obj)) {
    obj.forEach((item) => collectStrings(item, strings));
  } else if (typeof obj === "object" && obj !== null) {
    Object.values(obj).forEach((v) => collectStrings(v, strings));
  }
  return strings;
}
function applyGlossary(text, glossary) {
  let result = text;
  for (const [en, hi] of Object.entries(glossary)) {
    const escaped = en.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const regex = new RegExp(`\\b${escaped}\\b`, "gi");
    result = result.replace(regex, hi);
  }
  return result;
}
async function batchTranslate(strings, client, batchSize = 20) {
  const translations = /* @__PURE__ */ new Map();
  const stringArray = Array.from(strings);
  const totalBatches = Math.ceil(stringArray.length / batchSize);
  for (let i = 0; i < stringArray.length; i += batchSize) {
    const batch = stringArray.slice(i, i + batchSize);
    const batchNum = Math.floor(i / batchSize) + 1;
    const prompt = `Translate the following English text items to Hindi. Keep technical terms, names, and formatting intact. Return ONLY the translations, one per line, in the same order as the input.

${batch.map((s, idx) => `${idx + 1}. ${s}`).join("\n")}

Translations:`;
    try {
      const result = await client.generate(prompt);
      const lines = result.trim().split("\n");
      for (let j = 0; j < batch.length && j < lines.length; j++) {
        translations.set(batch[j], lines[j].trim());
      }
      console.log(`  Translated batch ${batchNum}/${totalBatches} (${batch.length} strings)`);
    } catch (err) {
      console.warn(`  Batch ${batchNum} failed: ${err.message}. Using fallback.`);
      for (let j = 0; j < batch.length; j++) {
        translations.set(batch[j], batch[j]);
      }
    }
  }
  return translations;
}
async function generateTabWithBatchTranslation(tabName, meta2, contentClient, translationClient, glossary) {
  const log = (event, details) => createLogEntry(event, { tabName, ...details });
  const maxRetries = 3;
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const startTime = Date.now();
    try {
      const prompt = generatePrompt(tabName, meta2);
      const raw = await contentClient.generate(prompt);
      const englishJson = parseResponse(raw);
      const qc = new QualityControl(meta2);
      const validation = qc.validate(tabName, englishJson);
      if (!validation.passed) {
        log("validation-failed", { errors: validation.errors, attempt });
        if (attempt >= maxRetries) {
          throw new Error(`[${tabName}] Quality gate: validation failed after ${maxRetries} attempts. Errors: ${validation.errors.join("; ")}`);
        }
        continue;
      }
      const normalized = normalizeContent(englishJson, glossary);
      const scorer = new PageScorer(meta2);
      const score = scorer.score(tabName, normalized);
      if (!score.passed) {
        if (attempt >= maxRetries) {
          console.warn(`[${tabName}] Score ${score.overall} < 90 after ${maxRetries} attempts. Using generated content.`);
        } else {
          const focusedPrompt = getFocusedRetryPrompt(tabName, score, normalized);
          if (focusedPrompt) {
            log("smart-retry", { score: score.overall, dimensions: score.dimensions });
            console.warn(`[${tabName}] Score ${score.overall} < 90. Attempting focused retry.`);
          }
        }
      }
      const allStrings = collectStrings(normalized);
      const mergedGlossary = { ...DEFAULT_GLOSSARY, ...glossary };
      const glossaryAppliedStrings = /* @__PURE__ */ new Set();
      for (const str of allStrings) {
        glossaryAppliedStrings.add(applyGlossary(str, mergedGlossary));
      }
      const translations = await batchTranslate(glossaryAppliedStrings, translationClient);
      const translateFn = (text, targetLang) => {
        if (targetLang !== "hi") return text;
        return translations.get(text) || text;
      };
      const bilingual = await translateToBilingual(normalized, translateFn, glossary);
      const contentHash = await generateSha256Hash(bilingual);
      const duration = Date.now() - startTime;
      log("success", {
        attempt,
        duration,
        score: score.overall,
        contentHash,
        uniqueStrings: allStrings.size
      });
      return {
        data: bilingual,
        score,
        validation,
        version: VERSION,
        contentHash,
        attempt,
        duration
      };
    } catch (err) {
      log("error", { message: err.message, attempt });
      if (attempt >= maxRetries) throw err;
      console.log(`[${tabName}] Attempt ${attempt} failed, retrying...`);
    }
  }
}
async function main() {
  console.log("\u2554\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2557");
  console.log("\u2551 UPSC Microtopic Generator v5 \u2014 Runner                  \u2551");
  console.log("\u2551 Topic: Prehistoric Time Periods                        \u2551");
  console.log("\u2551 Path: /upsc/ancient-history/Prehistory/                \u2551");
  console.log("\u2551       Prehistoric-Time-Periods/                        \u2551");
  console.log("\u255A\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u2550\u255D");
  console.log("");
  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    console.error("\u274C GEMINI_API_KEY not found in environment variables.");
    process.exit(1);
  }
  console.log(`\u2705 API key loaded (length: ${apiKey.length})`);
  console.log("\n\u{1F4CB} Validating topic metadata...");
  const validation = validateMetadata(meta);
  if (!validation.passed) {
    console.error("\u274C Metadata validation failed:");
    validation.errors.forEach((e) => console.error(`   - ${e}`));
    process.exit(1);
  }
  console.log("\u2705 Metadata validation passed.");
  if (validation.warnings.length > 0) {
    console.warn(`\u26A0\uFE0F  ${validation.warnings.length} warnings:`);
    validation.warnings.forEach((w) => console.warn(`   - ${w}`));
  }
  const subjectConfig = getSubjectConfig(meta.subjectDir);
  console.log(`
\u{1F4DA} Subject config: supportsTimeline=${subjectConfig.supportsTimeline}, supportsMaps=${subjectConfig.supportsMaps}, supportsMains=${subjectConfig.supportsMains}`);
  const contentClient = new GeminiClient(apiKey, {
    model: "gemini-3.5-flash-lite",
    temperature: 0.1,
    maxRetries: 5,
    requestDelay: 13e3
  });
  const translationClient = new GeminiClient(apiKey, {
    model: "gemini-3.5-flash-lite",
    temperature: 0.1,
    maxRetries: 5,
    requestDelay: 13e3
  });
  console.log("\u2705 Gemini clients initialized.");
  const tabs = ["overview", "concepts", "visual", "comparisons", "practice", "mains", "revision", "test"];
  const tabResults = {};
  for (const tabName of tabs) {
    console.log(`
${"=".repeat(60)}`);
    console.log(`\u{1F4DD} Generating tab: ${tabName}`);
    console.log(`   Prompt: ${generatePrompt(tabName, meta).substring(0, 100)}...`);
    console.log(`   Estimated time: ~30-60s (content + translation)`);
    console.log(`${"=".repeat(60)}`);
    try {
      const result = await generateTabWithBatchTranslation(
        tabName,
        meta,
        contentClient,
        translationClient,
        {}
      );
      tabResults[tabName] = result;
      console.log(`\u2705 Tab "${tabName}" generated successfully!`);
      console.log(`   Score: ${result.score?.overall || "N/A"}/100`);
      console.log(`   Duration: ${(result.duration / 1e3).toFixed(1)}s`);
      console.log(`   Content hash: ${result.contentHash?.substring(0, 20)}...`);
    } catch (err) {
      console.error(`\u274C Failed to generate tab "${tabName}": ${err.message}`);
      tabResults[tabName] = null;
    }
  }
  console.log(`
${"=".repeat(60)}`);
  console.log("\u{1F528} Assembling HTML page...");
  console.log(`${"=".repeat(60)}`);
  const bilingualData = {};
  for (const tabName of tabs) {
    if (tabResults[tabName]) {
      bilingualData[tabName] = tabResults[tabName].data;
    }
  }
  const overallScore = Math.round(
    Object.values(tabResults).filter((r) => r).reduce((sum, r) => sum + (r.score?.overall || 0), 0) / Object.values(tabResults).filter((r) => r).length
  );
  const html = assemblePage(meta, bilingualData, { overall: overallScore });
  const outputDir = import_path.default.join(process.cwd(), "upsc", meta.subjectDir, meta.parentDir, meta.dir);
  import_fs.default.mkdirSync(outputDir, { recursive: true });
  const htmlPath = import_path.default.join(outputDir, "index.html");
  import_fs.default.writeFileSync(htmlPath, html, "utf8");
  console.log(`\u2705 HTML page written to: ${htmlPath}`);
  console.log(`   File size: ${(html.length / 1024).toFixed(1)} KB`);
  const manifest = createManifest(meta, tabResults);
  const manifestPath = import_path.default.join(outputDir, "page.manifest.json");
  import_fs.default.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2), "utf8");
  console.log(`\u2705 Manifest written to: ${manifestPath}`);
  const tabsDir = import_path.default.join(outputDir, "tabs");
  import_fs.default.mkdirSync(tabsDir, { recursive: true });
  for (const tabName of tabs) {
    if (tabResults[tabName]) {
      const tabPath = import_path.default.join(tabsDir, `${tabName}.json`);
      import_fs.default.writeFileSync(tabPath, JSON.stringify(tabResults[tabName].data, null, 2), "utf8");
    }
  }
  console.log(`\u2705 Tab JSON files written to: ${tabsDir}/`);
  console.log(`
${"=".repeat(60)}`);
  console.log("\u{1F4CA} Generation Summary");
  console.log(`${"=".repeat(60)}`);
  console.log(`Topic: ${meta.name}`);
  console.log(`URL: ${meta.canonicalUrl}`);
  console.log(`Overall score: ${overallScore}/100`);
  console.log(`Tabs generated: ${Object.values(tabResults).filter((r) => r).length}/${tabs.length}`);
  for (const tabName of tabs) {
    const result = tabResults[tabName];
    if (result) {
      console.log(`  \u2705 ${tabName}: ${result.score?.overall || "N/A"}/100 (${(result.duration / 1e3).toFixed(1)}s)`);
    } else {
      console.log(`  \u274C ${tabName}: FAILED`);
    }
  }
  console.log(`${"=".repeat(60)}`);
  console.log("\u{1F389} Done!");
}
main().catch((err) => {
  console.error("\n\u274C Fatal error:", err);
  process.exit(1);
});
