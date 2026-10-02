import { jsonrepair } from 'jsonrepair';

// Exact existing Music response parser, independent of API and page persistence.
export function parseMusicJson(raw) {
  const cleaned = String(raw || '').trim().replace(/^```(?:json)?\s*/i, '').replace(/\s*```$/i, '').trim();
  try { return JSON.parse(cleaned); }
  catch (error) { try { return JSON.parse(jsonrepair(cleaned)); } catch { throw new Error(`Gemini JSON parse failed: ${error.message}`); } }
}
