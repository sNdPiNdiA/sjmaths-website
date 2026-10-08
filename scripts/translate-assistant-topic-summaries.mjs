import fs from 'node:fs';
import path from 'node:path';
import 'dotenv/config';
import { GoogleGenAI } from '@google/genai';
import { load } from 'cheerio';
import { parse, applyEdits, escapeHtml } from './seo-html.cjs';

const root = process.cwd();
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY_1 || process.env.GEMINI_API_KEY });
const pages=[];
function walk(dir){for(const entry of fs.readdirSync(dir,{withFileTypes:true})){const file=path.join(dir,entry.name);if(entry.isDirectory())walk(file);else if(entry.name==='index.html')pages.push(file)}}
walk(path.join(root,'up-assistant-teacher'));
const byText=new Map();
for(const file of pages){const $=load(fs.readFileSync(file,'utf8'));$('.topic-desc').each((_,el)=>{const en=$(el).find('.lang-en').first().text().replace(/\s+/g,' ').trim();const hi=$(el).find('.lang-hi').first().text().replace(/\s+/g,' ').trim();if(en&&hi&&(en===hi||!/[\u0900-\u097f]/.test(hi))&&!byText.has(en))byText.set(en,`d${byText.size+1}`)})}
const pairs=[...byText].map(([text,id])=>({id,text}));
if(!pairs.length){console.log('No untranslated topic descriptions found.');process.exit(0)}
console.log(`Translating ${pairs.length} unique topic summaries across ${pages.length} pages.`);
const translations=new Map();
for(let offset=0;offset<pairs.length;offset+=18){
 const batch=pairs.slice(offset,offset+18);
 const prompt='Translate each complete English topic description into clear, natural Hindi suitable for a UP Assistant Teacher exam learning page. Preserve every meaning, qualification, proper name, academic term, acronym, and fact. Do not shorten, add facts, or transliterate English sentences. Return only a JSON array of objects with the same id and a Hindi translation in the `hi` property.\n'+JSON.stringify(batch);
 const response=await ai.models.generateContent({model:'gemini-3.1-flash-lite',contents:prompt,config:{responseMimeType:'application/json',responseSchema:{type:'ARRAY',items:{type:'OBJECT',properties:{id:{type:'STRING'},hi:{type:'STRING'}},required:['id','hi']}}}});
 let output=JSON.parse(response.text||'[]');
 if(!Array.isArray(output)||output.length!==batch.length)throw new Error(`Translation batch ${Math.floor(offset/18)+1} returned ${output.length} rows for ${batch.length} inputs.`);
 for(let i=0;i<batch.length;i++){if(output[i].id!==batch[i].id||!/[\u0900-\u097f]/.test(output[i].hi||''))throw new Error(`Invalid Hindi translation at ${batch[i].id}`);translations.set(batch[i].id,output[i].hi.trim())}
 console.log(`Translated ${translations.size}/${pairs.length}`);
}
const textToHindi=new Map(pairs.map(x=>[x.text,translations.get(x.id)]));let changed=0;
for(const file of pages){const original=fs.readFileSync(file,'utf8'),$=parse(original),edits=[];$('.topic-desc').each((_,el)=>{const en=$(el).find('.lang-en').first().text().replace(/\s+/g,' ').trim();const hiEl=$(el).find('.lang-hi').first();const hi=hiEl.text().replace(/\s+/g,' ').trim();if(!en||!hiEl.length||!textToHindi.has(en)||!(en===hi||!/[\u0900-\u097f]/.test(hi)))return;const loc=hiEl[0].sourceCodeLocation;if(!loc?.startTag||!loc?.endTag)throw new Error(`Missing source location for Hindi topic description: ${file}`);edits.push({start:loc.startTag.endOffset,end:loc.endTag.startOffset,text:escapeHtml(textToHindi.get(en))})});if(edits.length){fs.writeFileSync(file,applyEdits(original,edits));changed+=edits.length}}
console.log(JSON.stringify({translatedDescriptions:changed,uniqueTranslations:translations.size,pages:pages.length},null,2));
