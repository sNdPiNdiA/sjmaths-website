import 'dotenv/config';
import { createHash } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { copyFile, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

const audioDir = path.resolve('class-10-maths/video-notes/chapter-13-statistics/mean/audio');
const model = 'gemini-3.8-flash-tts';
const voice = 'Sulafat';
const voiceStyle = [
  'Warm, clear, natural Indian classroom teacher speaking conversational Hinglish to Class 10 students.',
  'Use a friendly North Indian Hindi accent with natural English mathematics terms, a medium-slow pace,',
  'clear enunciation, short thoughtful pauses around equations, and light energy without sounding theatrical.',
  'Read the transcript exactly; do not add an introduction, conclusion, or extra words.'
].join(' ');

const narration = [
  'Chaliye, ek real-life situation se shuru karte hain. Sochiye, class ke students roz kitne minutes padhte hain, uska record rakhna hai. Har student ka alag time likhne ke bajay, hum data ko intervals mein group karte hain, aur har interval ke saath frequency likhte hain. Ab in observations ko ek representative number mein summarize karna hai. Grouped data ka mean yahi representative average deta hai. Aaj hum class mark se shuru karke ise teen board methods se nikaalenge.',
  'Individual observations mein mean hota hai, sab values ka sum divided by unki total count. Frequency table mein koi value jitni baar aati hai, use utni baar count karna zaroori hai. Isliye frequency ek weight ki tarah kaam karti hai. Grouped data mein har interval ke liye uska class mark representative value hota hai. Formula hai: x bar equals sum of f i into x i, divided by sum of f i. Mean ki unit original data jaisi hi rehti hai.',
  'Har class interval ka midpoint uska class mark hota hai. Lower limit aur upper limit ko add karke two se divide kijiye. Isse x i milta hai. f i us class ki frequency hai, N total frequency yani sum of f i hai, aur x bar mean ko show karta hai. Jaise ten se twenty ka midpoint fifteen hai, isliye us class ka class mark fifteen hoga.',
  'Calculation se pehle class intervals check kijiye. Zero se ten aur ten se twenty jaise continuous intervals mein common boundary clear hoti hai. Lekin inclusive classes ten se nineteen aur twenty se twenty-nine ke beech gap one hai. Half-gap zero point five hota hai. Lower side se point five ghata kar aur upper side mein point five jod kar classes nine point five se nineteen point five, aur nineteen point five se twenty-nine point five banengi. Ab boundaries ka midpoint class mark hoga.',
  'Direct method mein pehle har interval ka class mark x i nikaaliye. Phir frequency f i se multiply karke f i x i banaiye. Saare products add karke total frequency se divide kijiye. Yani x bar equals sum of f i x i, divided by sum of f i. Jab class marks aur products manageable hon, direct method sabse seedha rehta hai. Board answer mein f i, x i aur f i x i ke columns saaf dikhaiye.',
  'Ab opening table solve karte hain. Intervals zero to ten, ten to twenty, twenty to thirty, aur thirty to forty hain. Inke class marks five, fifteen, twenty-five, thirty-five hain. Frequencies three, five, seven, five hain. Total frequency twenty, aur f i x i ka total four hundred forty aata hai. Direct formula se mean four hundred forty divided by twenty, yani twenty-two minutes. Grouped data mein yeh class marks se mila estimated mean hai.',
  'Assumed mean method mein beech ke paas koi convenient class mark a choose kijiye. Har class mark se a ghata kar signed deviation d i milta hai. Phir frequency se multiply karke weighted deviations add karte hain. Formula hai: x bar equals a plus sum of f i d i divided by N. Central value chunne se deviations chhote rehte hain. Sign bilkul mat hataiye: a se neeche ka class mark negative deviation deta hai.',
  'Reading-time example mein assumed mean twenty-five lete hain. Class marks five, fifteen, twenty-five, thirty-five hain; deviations minus twenty, minus ten, zero, ten milte hain. Inhe frequencies se multiply karne par total weighted deviation minus sixty aata hai. Ab twenty-five plus minus sixty divided by twenty equals twenty-two minutes. Negative correction ka matlab hai ki actual grouped mean assumed mean se neeche hai. Yeh direct method wale answer se match karta hai.',
  'Agar sabhi class intervals ki width same ho, step-deviation method calculation ko aur chhota kar deta hai. Pehle d i equals x i minus a nikaaliye, phir common class width h se divide karke u i paaiye. Mean ka formula hai: x bar equals a plus h times sum of f i u i divided by N. Dhyaan rahe, correction ko end mein h se multiply karna hota hai. Unequal widths ke liye yeh shortcut use na karein.',
  'Yahan assumed mean a twenty-five aur class width h ten hai. Deviations minus twenty, minus ten, zero, ten ko ten se divide karne par step values minus two, minus one, zero, one milti hain. Frequency-weighted total minus six hai. Formula mein values rakhne par twenty-five plus ten times minus six divided by twenty equals twenty-two minutes. Dekhiye, direct, assumed mean aur step-deviation, teeno methods ne wahi mean diya.',
  'Method chunne ka simple rule yaad rakhiye. Class marks aur products chhote hon, toh direct method. Class marks bade hon par central assumed mean se deviations chhote hon, toh assumed mean method. Sab intervals ki width equal ho, toh step-deviation fast rehta hai. Teeno ka final mean same hona chahiye. Agar question mein koi method specifically maanga ho, toh wahi method use karke poora working dikhaiye.',
  'Board exam mein ek missing frequency m ho, toh use total frequency aur weighted sum, dono mein include kijiye. Is example mein class marks five, fifteen, twenty-five, thirty-five hain; frequencies four, six, m, five aur mean twenty-two diya hai. Isliye N equals fifteen plus m, aur sum of f i x i equals two hundred eighty-five plus twenty-five m. Mean condition lagane par m fifteen milta hai. End mein check kijiye: total thirty, weighted sum six hundred sixty, aur mean twenty-two.',
  'Do missing frequencies p aur q hon, toh mean ke saath total frequency ki condition bhi chahiye. Yahan total thirty diya hai, isliye p plus q equals twenty-one. Mean twenty-two hone par weighted sum six hundred sixty hona chahiye. Known classes hataane ke baad fifteen p plus twenty-five q equals four hundred sixty-five milta hai. Dono equations solve karne par p six aur q fifteen aate hain. Ek equation se do unknowns alag-alag determine nahi hote.',
  'Board-ready answer mein pehle class marks likhiye, phir required product ya deviation columns banaiye. N equals sum of f i aur zaroori weighted sum clearly show kijiye. Sahi formula mein values substitute karke signs aur units ke saath final answer dijiye. Step-deviation mein h se multiply karna na bhoolein. Ek quick check: mean class marks ki range mein hona chahiye. Class limits ko class marks samajhna, classes ki count se divide karna, aur missing frequency ko kisi total se chhod dena common mistakes hain.',
  'Quick revision: class mark equals lower limit plus upper limit, divided by two. Direct method mein x bar equals sum of f i x i divided by N. Assumed mean mein d i equals x i minus a, phir a plus weighted deviation over N. Equal class widths ke liye u i equals x i minus a over h, aur correction ko h se multiply karte hain. Aakhri check: N forty hai aur sum of f i x i nine hundred twenty. Mean kya hoga? Nine hundred twenty divided by forty, yani twenty-three.'
];

function requireTool(command, args, label) {
  const result = spawnSync(command, args, { encoding: 'utf8', windowsHide: true });
  if (result.error || result.status !== 0) {
    const detail = (result.stderr || result.error?.message || '').trim().slice(0, 500);
    throw new Error(`${label} failed${detail ? `: ${detail}` : '.'}`);
  }
  return result.stdout.trim();
}

function getAudioData(payload) {
  if (payload.output_audio?.data) return payload.output_audio.data;
  const outputs = (payload.steps || []).filter(step => step.type === 'model_output').flatMap(step => step.content || []);
  return outputs.find(part => part.type === 'audio' && part.data)?.data;
}

async function generateClip(apiKey, text, index) {
  const response = await fetch('https://generativelanguage.googleapis.com/v1beta/interactions', {
    method: 'POST',
    headers: { 'x-goog-api-key': apiKey, 'content-type': 'application/json' },
    body: JSON.stringify({
      model,
      input: [{
        type: 'user_input',
        content: [{
          type: 'text',
          text,
          annotations: [{ type: 'speech_metadata', style: voiceStyle }]
        }]
      }],
      response_format: { type: 'audio' },
      generation_config: { speech_config: [{ voice }] }
    }),
    signal: AbortSignal.timeout(120000)
  });
  const raw = await response.text();
  if (!response.ok) {
    const safeDetails = raw.replaceAll(apiKey, '[redacted]').slice(0, 500);
    throw new Error(`Gemini TTS failed for slide ${index + 1} with HTTP ${response.status}: ${safeDetails}`);
  }
  const audio = getAudioData(JSON.parse(raw));
  if (!audio) throw new Error(`Gemini TTS returned no audio for slide ${index + 1}.`);
  return Buffer.from(audio, 'base64');
}

const apiKey = process.env.GEMINI_API_KEY || process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY_2;
if (!apiKey) throw new Error('Set GEMINI_API_KEY in the local .env file before running this script.');
if (narration.length !== 15) throw new Error('Expected exactly 15 slide scripts.');

// Keep validated clips across runs so a quota limit can be resumed later.
const stageKey = createHash('sha256')
  .update(JSON.stringify({ model, voice, voiceStyle, narration }))
  .digest('hex')
  .slice(0, 12);
const stageRoot = path.join(os.tmpdir(), 'sjmaths-class10-statistics-mean-voiceover', stageKey);
const stagedDir = path.join(stageRoot, 'new');
const backupDir = path.join(stageRoot, 'old');
await mkdir(stagedDir, { recursive: true });

for (let index = 0; index < narration.length; index += 1) {
  const fileNo = String(index + 1).padStart(2, '0');
  const wavPath = path.join(stagedDir, `slide-${fileNo}.wav`);
  const mp3Path = path.join(stagedDir, `slide-${fileNo}.mp3`);

  let stagedIsValid = false;
  try {
    const stagedAudio = await readFile(mp3Path);
    if (stagedAudio.length > 1000) {
      const stagedSeconds = Number(requireTool('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', mp3Path], `MP3 validation for slide ${index + 1}`));
      stagedIsValid = Number.isFinite(stagedSeconds) && stagedSeconds >= 5;
      if (stagedIsValid) process.stdout.write(`Reusing staged slide ${fileNo} (${stagedSeconds.toFixed(1)} s)\n`);
    }
  } catch {
    stagedIsValid = false;
  }
  if (stagedIsValid) continue;
  await rm(mp3Path, { force: true });

  let wav;
  try {
    wav = await generateClip(apiKey, narration[index], index);
  } catch (error) {
    process.stderr.write(`Generation paused at slide ${fileNo}. Valid staged clips are kept; rerun this script later to resume.\n`);
    throw error;
  }
  if (wav.subarray(0, 4).toString('ascii') !== 'RIFF' || wav.subarray(8, 12).toString('ascii') !== 'WAVE') {
    throw new Error(`Gemini returned an invalid WAV file for slide ${index + 1}.`);
  }
  await writeFile(wavPath, wav);

  try {
    requireTool('ffmpeg', ['-hide_banner', '-loglevel', 'error', '-y', '-i', wavPath, '-codec:a', 'libmp3lame', '-b:a', '96k', '-ar', '24000', '-ac', '1', mp3Path], `MP3 conversion for slide ${index + 1}`);
    const seconds = Number(requireTool('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', mp3Path], `MP3 validation for slide ${index + 1}`));
    if (!Number.isFinite(seconds) || seconds < 5) throw new Error(`Generated slide ${index + 1} audio is unexpectedly short.`);
    process.stdout.write(`Generated slide ${fileNo} (${seconds.toFixed(1)} s)\n`);
  } catch (error) {
    await rm(mp3Path, { force: true });
    throw error;
  } finally {
    await rm(wavPath, { force: true });
  }
}

await rm(backupDir, { recursive: true, force: true });
await mkdir(backupDir, { recursive: true });
for (let index = 1; index <= narration.length; index += 1) {
  const fileNo = String(index).padStart(2, '0');
  await copyFile(path.join(audioDir, `slide-${fileNo}.mp3`), path.join(backupDir, `slide-${fileNo}.mp3`));
}

try {
  for (let index = 1; index <= narration.length; index += 1) {
    const fileNo = String(index).padStart(2, '0');
    await copyFile(path.join(stagedDir, `slide-${fileNo}.mp3`), path.join(audioDir, `slide-${fileNo}.mp3`));
  }

  process.stdout.write(`Installed ${narration.length} new Hinglish voice clips using ${model} (${voice}).\n`);
  await rm(stageRoot, { recursive: true, force: true });
} catch (error) {
  for (let index = 1; index <= narration.length; index += 1) {
    const fileNo = String(index).padStart(2, '0');
    await copyFile(path.join(backupDir, `slide-${fileNo}.mp3`), path.join(audioDir, `slide-${fileNo}.mp3`));
  }
  throw error;
}
