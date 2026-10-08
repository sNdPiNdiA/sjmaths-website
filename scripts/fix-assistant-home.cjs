const fs=require('fs');
const {parse,applyEdits,escapeHtml}=require('./seo-html.cjs');
const home='up-assistant-teacher/index.html';
const source=fs.readFileSync(home,'utf8');
const root=parse(source),edits=[],unmatched=[];
for(const checkbox of root('input.syllabus-checkbox').toArray()){
 const id=root(checkbox).attr('id')||'',match=id.match(/^([a-z0-9-]+)-mt-(\d+)-(\d+)$/);
 if(!match){unmatched.push(id);continue}
 const folder=({eng:'english',sci:'science',math:'mathematics',teach:'teaching-skills',psych:'child-psychology',social:'environmental-social-studies',gk:'gk-current-affairs',reas:'logical-reasoning',it:'information-technology',life:'life-skill-management'})[match[1]]||match[1];
 const hubFile=`up-assistant-teacher/${folder}/index.html`;
 if(!fs.existsSync(hubFile)){unmatched.push(id);continue}
 const hubId=`${folder}-mt-${match[2]}-${match[3]}`;
 const hub=parse(fs.readFileSync(hubFile,'utf8')),sourceBox=hub(`#${hubId}`).first(),sourceLi=sourceBox.closest('li'),sourceLabel=sourceLi.find('.syllabus-text').first(),sourceAnchor=sourceLi.find('a').first(),row=root(checkbox).closest('li'),loc=row[0]?.sourceCodeLocation;
 if(!sourceBox.length||!sourceLabel.length||!sourceAnchor.length||!loc?.startTag||!loc.endTag){unmatched.push(id);continue}
 const boxAttrs=Object.entries(checkbox.attribs).filter(([k])=>k!=='aria-label'&&k!=='aria-labelledby').map(([k,v])=>`${k}="${escapeHtml(v)}"`).join(' ');
 const style=sourceAnchor.attr('style')||'text-decoration:none;color:inherit;flex:1;';
 const labelId=`${id}-label`;
 const content=`<input ${boxAttrs} aria-labelledby="${labelId}"/><a href="${escapeHtml(sourceAnchor.attr('href'))}" style="${escapeHtml(style)}"><span class="syllabus-text" id="${labelId}">${sourceLabel.html()}</span></a>`;
 edits.push({start:loc.startTag.endOffset,end:loc.endTag.startOffset,text:content});
}
let out=applyEdits(source,edits);
out=out.replace(/\.syllabus-checkbox:checked\s*\+\s*\.syllabus-text\s*\{/,'.syllabus-checkbox:checked + a .syllabus-text {').replace(/e\.target\.tagName !== 'A'/g,"!e.target.closest('a')");
fs.writeFileSync(home,out);
console.log(JSON.stringify({rowsSynchronized:edits.length,unmatched:unmatched.slice(0,20),unmatchedCount:unmatched.length},null,2));
