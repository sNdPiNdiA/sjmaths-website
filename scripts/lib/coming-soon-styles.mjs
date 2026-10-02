import crypto from 'node:crypto';

export const COMING_SOON_STYLE_SHA256 = '9bf425aaab6df9db4891c3acd20d368d0a8fa56fe80741dd1921f5dd2101788b';
export const COMING_SOON_STYLESHEET_HREF = '/assets/css/coming-soon-page.css';

export function externalizeComingSoonStyle(html) {
  const styleTags = [...html.matchAll(/<style\b[^>]*>[\s\S]*?<\/style\s*>/gi)];
  const matchingTags = styleTags.filter(([tag]) => {
    const css = tag.replace(/^<style\b[^>]*>/i, '').replace(/<\/style\s*>$/i, '').trim();
    return crypto.createHash('sha256').update(css).digest('hex') === COMING_SOON_STYLE_SHA256;
  });

  if (matchingTags.length === 0) return html;
  if (matchingTags.length !== 1 || styleTags.length !== 1) {
    throw new Error('Expected exactly one inline coming-soon stylesheet.');
  }
  if (new RegExp(`<link\\b(?=[^>]*\\bhref=["']${COMING_SOON_STYLESHEET_HREF.replaceAll('/', '\\/')}["'])`, 'i').test(html)) {
    throw new Error('Page already links the coming-soon stylesheet while retaining its inline copy.');
  }

  return html.replace(matchingTags[0][0], `<link rel="stylesheet" href="${COMING_SOON_STYLESHEET_HREF}">`);
}
