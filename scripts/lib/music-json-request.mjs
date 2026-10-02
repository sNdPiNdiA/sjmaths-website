// Existing Music generator retry policy; dependencies are injectable for offline tests.
export async function generateMusicJson(prompt, ai, validator, label, { model: MODEL, parseJson, maxAttempts = 3, warn = console.warn, sleep = ms => new Promise(resolve => setTimeout(resolve, ms)), emptyResponseMessage = 'Gemini returned an empty response' }) {
  let activePrompt = prompt; let lastError; let lastData;
  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      const response = await ai.models.generateContent({ model: MODEL, contents: activePrompt, config: { temperature: 0.25, responseMimeType: 'application/json' } });
      if (!response?.text) throw new Error(emptyResponseMessage);
      const data = parseJson(response.text);
      lastData = data;
      try {
        validator(data);
        return data;
      } catch (validationError) {
        const error = new Error(`${label} validation failed: ${validationError.message}`);
        error.isValidationError = true;
        error.partialData = data;
        throw error;
      }
    } catch (error) {
      lastError = error;
      const status = Number(error?.status || error?.code || error?.error?.code || error?.response?.status) || null;
      const quotaError = status === 429 || String(error?.message || '').includes('RESOURCE_EXHAUSTED');
      if ([400, 401, 403].includes(status) || quotaError) throw error;

      if (error.isValidationError === true) {
        if (attempt === maxAttempts) {
          warn(`${label} final attempt failed validation; saving the last generated response and continuing.`);
          return error.partialData || lastData;
        }
        activePrompt = `${prompt}\n\nThe previous JSON failed validation: ${error.message}\nReturn corrected complete JSON. Preserve every required field and minimum point count.`;
      }

      if (attempt < maxAttempts) {
        const waitMs = error.isValidationError === true
          ? Math.min(8000, attempt * 2000)
          : Math.min(60000, 8000 * (2 ** (attempt - 1)));
        warn(`${label} attempt ${attempt} failed (${status || error.message}); retrying in ${Math.round(waitMs / 1000)}s.`);
        await sleep(waitMs);
      }
    }
  }
  throw lastError;
}
