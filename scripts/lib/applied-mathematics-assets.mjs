import fs from 'node:fs';

const cssUrl = new URL('../../assets/css/applied-mathematics-topic.css', import.meta.url);
const jsUrl = new URL('../../assets/js/applied-mathematics-topic.js', import.meta.url);

export const appliedMathematicsTopicCss = fs.readFileSync(cssUrl, 'utf8').trim();
export const appliedMathematicsTopicJs = fs.readFileSync(jsUrl, 'utf8').trim();

export const appliedMathematicsTopicStyleLink = '<link rel="stylesheet" href="/assets/css/applied-mathematics-topic.min.css?v=f2e3598b" data-applied-maths-style="monolith">';
export const appliedMathematicsTopicScriptTag = '<script src="/assets/js/applied-mathematics-topic.min.js?v=cbbe6612" data-applied-maths-script="tabs" defer></script>';

const normalize = text => text.replace(/\r\n/g, '\n').trim();

export function externalizeAppliedMathematicsStyles(html) {
  return html.replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gi, (tag, css) => {
    return normalize(css) === normalize(appliedMathematicsTopicCss) ? appliedMathematicsTopicStyleLink : tag;
  });
}

export function hydrateAppliedMathematicsStyles(html) {
  return html.replace(/<link\b[^>]*data-applied-maths-style="monolith"[^>]*>/gi, () => {
    return `<style>\n${appliedMathematicsTopicCss}\n    </style>`;
  });
}

export function externalizeAppliedMathematicsScript(html) {
  return html.replace(/<script\b(?![^>]*\bsrc=)[^>]*>([\s\S]*?)<\/script>/gi, (tag, js) => {
    return normalize(js) === normalize(appliedMathematicsTopicJs) ? appliedMathematicsTopicScriptTag : tag;
  });
}

export function hydrateAppliedMathematicsScript(html) {
  return html.replace(/<script\b[^>]*data-applied-maths-script="tabs"[^>]*><\/script>/gi, () => {
    return `<script>\n        ${appliedMathematicsTopicJs}\n    </script>`;
  });
}

export function externalizeAppliedMathematicsAssets(html) {
  return externalizeAppliedMathematicsScript(externalizeAppliedMathematicsStyles(html));
}

export function hydrateAppliedMathematicsAssets(html) {
  return hydrateAppliedMathematicsScript(hydrateAppliedMathematicsStyles(html));
}
