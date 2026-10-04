document.addEventListener('DOMContentLoaded',()=>{const esc=v=>String(v??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');const bilingualDataElement=document.getElementById('bilingual-data');const bilingualData=JSON.parse(bilingualDataElement?.textContent||'{}');const pageLanguage=localStorage.getItem('sjmaths_language')==='en'?'en':bilingualDataElement?'hi':'en';const quiz=pageLanguage==='hi'&&bilingualData.quiz?.length?bilingualData.quiz:JSON.parse(document.getElementById('quiz-data').textContent||'[]');const test=pageLanguage==='hi'&&bilingualData.test?.length?bilingualData.test:JSON.parse(document.getElementById('test-data').textContent||'[]');let quizScore=0;const answered=new Set();const feedback=(ok,text)=>'<div class="quiz-feedback '+(ok?'correct':'incorrect')+'"><strong>'+(ok?(pageLanguage==='hi'?'✓ सही':'✓ Correct'):(pageLanguage==='hi'?'✗ पुनः देखें':'✗ Review'))+'</strong><p>'+esc(text)+'</p></div>';function markQuiz(i,ok,text){if(answered.has(i))return;answered.add(i);if(ok)quizScore++;const card=document.getElementById('quiz-card-'+i);card.dataset.answered='true';card.querySelectorAll('button').forEach(b=>b.disabled=true);document.getElementById('quiz-feedback-'+i).innerHTML=feedback(ok,text);document.getElementById('quiz-score').textContent='Score: '+quizScore+' / '+quiz.length;}document.querySelectorAll('[data-quiz]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.quiz),o=Number(btn.dataset.option),q=quiz[i];document.querySelectorAll('#quiz-card-'+i+' [data-option]').forEach((b,n)=>{b.disabled=true;if(n===q.correct_index)b.classList.add('correct');if(n===o&&o!==q.correct_index)b.classList.add('incorrect');});markQuiz(i,o===q.correct_index,q.explanation);}));document.querySelectorAll('[data-fill]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.fill),q=quiz[i],v=document.getElementById('quiz-input-'+i).value.trim().toLowerCase();markQuiz(i,(q.accepted_answers||[]).some(a=>v===String(a).trim().toLowerCase()),(pageLanguage==='hi'?'स्वीकृत उत्तर: ':'Accepted answer(s): ')+(q.accepted_answers||[]).join(', ')+' — '+q.explanation);}));document.querySelectorAll('[data-short]').forEach(btn=>btn.addEventListener('click',()=>{const i=Number(btn.dataset.short),q=quiz[i];markQuiz(i,false,(pageLanguage==='hi'?'अपेक्षित उत्तर: ':'Expected answer: ')+(q.expected_answer||'See the explanation')+' — '+q.explanation);}));document.getElementById('btn-reset-quiz').addEventListener('click',()=>location.reload());const chosen={};let submitted=false;document.querySelectorAll('[data-test]').forEach(btn=>btn.addEventListener('click',()=>{if(submitted)return;const i=Number(btn.dataset.test);chosen[i]=Number(btn.dataset.option);document.querySelectorAll('#test-card-'+i+' [data-option]').forEach(b=>b.classList.remove('selected'));btn.classList.add('selected');}));function submitTest(){if(submitted)return;submitted=true;let score=0;test.forEach((q,i)=>{const answer=chosen[i];if(answer===q.correct_index)score++;document.querySelectorAll('#test-card-'+i+' [data-option]').forEach((b,n)=>{b.disabled=true;if(n===q.correct_index)b.classList.add('correct');if(n===answer&&answer!==q.correct_index)b.classList.add('incorrect');});document.getElementById('test-feedback-'+i).innerHTML=feedback(answer===q.correct_index,q.explanation);});document.getElementById('test-score').textContent=score;document.getElementById('test-result').classList.remove('hidden');document.getElementById('btn-submit-test').classList.add('hidden');}document.getElementById('btn-submit-test').addEventListener('click',submitTest);document.getElementById('btn-retake-test').addEventListener('click',()=>location.reload());let timer=null,remaining=600;function startTimer(){if(timer||submitted)return;timer=setInterval(()=>{remaining--;document.getElementById('test-timer').textContent=String(Math.floor(remaining/60)).padStart(2,'0')+':'+String(remaining%60).padStart(2,'0');if(remaining<=0){clearInterval(timer);submitTest();}},1000);}const tabs=document.querySelectorAll('.tab-btn'),panels=document.querySelectorAll('.tab-panel');tabs.forEach(btn=>btn.addEventListener('click',()=>{tabs.forEach(b=>{b.classList.remove('active');b.setAttribute('aria-selected','false');});panels.forEach(p=>{p.classList.remove('active');p.classList.add('hidden');});btn.classList.add('active');btn.setAttribute('aria-selected','true');document.getElementById(btn.dataset.tab).classList.remove('hidden');document.getElementById(btn.dataset.tab).classList.add('active');if(btn.dataset.tab==='tab-test')startTimer();window.scrollTo({top:document.querySelector('.study-tabs-sticky-wrapper').offsetTop-15,behavior:'smooth'});}));const theme=document.getElementById('btn-theme-toggle');
const themePreferenceKey='sjmaths.theme.preference';
const isDarkPreference=preference=>preference==='dark'||(preference==='system'&&window.matchMedia('(prefers-color-scheme: dark)').matches);
const updateThemeToggle=isDark=>{
  document.documentElement.dataset.theme=isDark?'dark':'light';
  document.documentElement.dataset.themePreference=themePreference;
  document.documentElement.style.colorScheme=isDark?'dark':'light';
  document.documentElement.classList.toggle('dark-mode',isDark);
  document.documentElement.classList.toggle('dark',isDark);
  document.body.classList.toggle('dark-mode',isDark);
  if(!theme)return;
  theme.textContent=pageLanguage==='hi'?(isDark?'लाइट मोड (Light Mode)':'डार्क मोड (Dark Mode)'):(isDark?'Light Mode':'Dark Mode');
  theme.setAttribute('aria-label',isDark?'Switch to light mode':'Switch to dark mode');
  theme.setAttribute('aria-pressed',String(isDark));
};
const applyLocalTheme=(preference,persist=true)=>{
  if(!['system','light','dark'].includes(preference))return;
  themePreference=preference;
  const isDark=isDarkPreference(preference);
  updateThemeToggle(isDark);
  if(persist){try{localStorage.setItem(themePreferenceKey,preference);}catch(error){}}
  window.dispatchEvent(new CustomEvent('sjmaths:themechange',{detail:{preference,theme:isDark?'dark':'light',isDark}}));
  window.dispatchEvent(new CustomEvent('themeChanged',{detail:{isDark}}));
};
let themePreference='system';
if(window.SJMathsTheme){
  themePreference=window.SJMathsTheme.getPreference();
  updateThemeToggle(isDarkPreference(themePreference));
  window.addEventListener('sjmaths:themechange',event=>updateThemeToggle(event.detail?.theme==='dark'));
  window.addEventListener('themeChanged',event=>updateThemeToggle(Boolean(event.detail?.isDark)));
}else{
  try{
    const saved=localStorage.getItem(themePreferenceKey);
    if(['system','light','dark'].includes(saved))themePreference=saved;
    else{
      const legacy=[['sjmaths-dark',{on:'dark',off:'light'}],['sjmaths_theme',{dark:'dark',light:'light'}],['sj_theme',{dark:'dark',light:'light'}],['theme',{dark:'dark',light:'light'}],['sjmaths-test-dark',{true:'dark',false:'light'}],['sjmaths-theme',{dark:'dark',light:'light'}]];
      for(const[key,values]of legacy){const migrated=values[localStorage.getItem(key)];if(!migrated)continue;themePreference=migrated;localStorage.setItem(themePreferenceKey,migrated);break;}
    }
  }catch(error){}
  applyLocalTheme(themePreference,false);
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener?.('change',()=>{if(themePreference==='system')applyLocalTheme('system',false);});
  window.addEventListener('storage',event=>{if(event.key===themePreferenceKey)applyLocalTheme(['system','light','dark'].includes(event.newValue)?event.newValue:'system',false);});
}
if(theme)theme.addEventListener('click',event=>{
  event.preventDefault();
  const next=isDarkPreference(themePreference)?'light':'dark';
  if(window.SJMathsTheme)window.SJMathsTheme.setPreference(next);
  else applyLocalTheme(next);
});
});
