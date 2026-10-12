from pathlib import Path
import re, html, json
from bs4 import BeautifulSoup
ROOT=Path('ib/dp-mathematics')
MARK='<!-- sjmaths:preserve-expanded-lesson -->'
def card(title,items):
 return '<article class="concept-card"><div class="concept-header"><h2 class="concept-title">'+title+'</h2></div><ul class="concept-notes">'+''.join('<li>'+i+'</li>' for i in items)+'</ul></article>\n'
def practice(n,q,a):
 return f'<div class="practice-item"><div class="practice-header"><strong>Exercise {n}</strong></div><p>{q}</p><button class="solution-toggle-btn" type="button" aria-expanded="false" onclick="toggleSolution(this)">Show Solution <i class="fa-solid fa-chevron-down" aria-hidden="true"></i></button><div class="solution-content"><p>{a}</p></div></div>\n'
def checkpoint(q,a):
 return f'<article class="concept-card"><h3>Independent checkpoint</h3><p>{q}</p><details><summary>Solution and reasoning</summary><p>{a}</p></details></article>\n'
def quiz(n,q,choices,key,why):
 options=''.join(f'<label style="display:block;padding:0.5rem"><input type="radio" name="q{n}" value="{k}"> {k}) {v}</label>' for k,v in zip('ABCD',choices))
 return f'<div class="quiz-question" style="margin-bottom:1.5rem"><p><strong>{n}. {q}</strong></p><div class="quiz-options" data-correct="{key}" data-explanation="{html.escape(why,quote=True)}">{options}</div><div class="quiz-feedback" style="display:none"></div></div>\n'
def append_panel(s,panel,addition):
 pat=r'(<section\b[^>]*\bid="'+panel+r'"[^>]*>)(.*?)(</section>)'
 s,n=re.subn(pat,lambda m:m[1]+m[2]+addition+m[3],s,count=1,flags=re.S);assert n==1,panel;return s
def expand(rel,notes='',problems=(),quizzes=()):
 p=ROOT/rel/'index.html';s=p.read_text(encoding='utf-8');soup=BeautifulSoup(s,'html.parser')
 if MARK not in s:s=s.replace('<head>','<head>\n'+MARK,1)
 if notes:s=append_panel(s,'tab-notes',notes)
 old=len(soup.select('#tab-practice .exercise-item, #tab-practice .practice-item'))
 if problems:s=append_panel(s,'tab-practice',''.join(practice(old+i,q,a) for i,(q,a) in enumerate(problems,1)))
 oldq=len(soup.select('.quiz-question'))
 if quizzes:
  anchor='<button type="button" onclick="gradeQuiz()"'
  assert anchor in s
  s=s.replace(anchor,''.join(quiz(oldq+i,*q) for i,q in enumerate(quizzes,1))+anchor,1)
 # Accurate counts, without changing original educational questions.
 count=old+len(problems)
 if count:
  s=re.sub(r'(Practice Exercises \()\d+(\))',lambda m:m[1]+str(count)+m[2],s)
  s=re.sub(r'<h2>10 Progressive Practice Exercises</h2>',f'<h2>{count} Practice Exercises</h2>',s)
 s=re.sub(r'<p>Carefully calibrated.*?</p>','<p>Attempt each problem before opening the solution.</p>',s)
 s=re.sub(r'<p>Worked examples calibrated.*?</p>','<p>Attempt each problem before opening the solution.</p>',s)
 p.write_text(s,encoding='utf-8',newline='\n');print(rel,'expanded')
def create(rel,title,course,section,description,concepts,problems,quizzes):
 p=ROOT/rel/'index.html';assert not p.exists(),p
 template=ROOT/'applications-and-interpretation-sl/geometry-and-trigonometry/3d-geometry-and-trigonometry/index.html'
 s=BeautifulSoup(template.read_text(encoding='utf-8'),'html.parser')
 url='https://sjmaths.com/ib/dp-mathematics/'+rel+'/'
 s.title.string=title+' | IB Math '+course+' | SJMaths'
 for name,value in [('description',description),('keywords',title+', IB Mathematics '+course)]:s.find('meta',attrs={'name':name})['content']=value
 for key,value in [('og:title',s.title.string),('og:description',description),('og:url',url)]:s.find('meta',attrs={'property':key})['content']=value
 for key,value in [('twitter:title',s.title.string),('twitter:description',description)]:s.find('meta',attrs={'name':key})['content']=value
 s.find('link',rel='canonical')['href']=url
 s.select_one('h1').string=title;s.select_one('.ib-hero-desc').string=description
 s.select_one('.guide-kicker').string=course+' · '+section+' · Current course (first assessment 2021)'
 pills=s.select_one('.meta-pills');pills.clear();pills.append(BeautifulSoup('<span class="meta-pill">'+course+'</span><span class="meta-pill">Notes · worked examples · independent practice</span>','html.parser'))
 course_rel=rel.split('/')[0];parent='/'.join(rel.split('/')[:-1])
 crumbs=[('Home','https://sjmaths.com/'),('IB Mathematics','https://sjmaths.com/ib/'),('DP Mathematics','https://sjmaths.com/ib/dp-mathematics/'),(course,'https://sjmaths.com/ib/dp-mathematics/'+course_rel+'/')]
 if parent!=course_rel:crumbs.append((section,'https://sjmaths.com/ib/dp-mathematics/'+parent+'/'))
 crumbs.append((title,url));nav=s.select_one('.breadcrumb-nav');nav.clear()
 for i,(label,href) in enumerate(crumbs):
  node=s.new_tag('span' if i==len(crumbs)-1 else 'a');node.string=label
  if node.name=='a':node['href']=href
  else:node['aria-current']='page'
  nav.append(node)
  if i<len(crumbs)-1:
   sep=s.new_tag('span');sep['class']='breadcrumb-separator';sep['aria-hidden']='true';sep.string=' › ';nav.append(sep)
 schema={'@context':'https://schema.org','@graph':[{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':i,'name':label,'item':href} for i,(label,href) in enumerate(crumbs,1)]},{'@type':'Article','headline':title,'description':description,'url':url,'dateModified':'2026-10-11','inLanguage':'en','author':{'@type':'Person','name':'Sandeep Jaiswal'}}]}
 s.find('script',type='application/ld+json').string=json.dumps(schema,ensure_ascii=False)
 values={'tab-notes':''.join(card(t,items) for t,items in concepts),'tab-practice':'<h2>Independent practice</h2><p>Attempt each question before opening its solution.</p>'+''.join(practice(n,q,a) for n,(q,a) in enumerate(problems,1)),'tab-formulas':card('Method and answer checklist',['Choose the method from the assumptions, not from a keyword.','Record variable definitions, domain restrictions and units.','Keep exact or unrounded intermediate values; check each result against the original question.','Use the notes above for formulas and conditions; distinguish an algebraic result from a justified contextual conclusion.']),'tab-test':'<h2>Diagnostic check</h2><p id="quiz-score-badge" aria-live="polite">Score: 0 / '+str(len(quizzes))+'</p>'+''.join(quiz(n,*q) for n,q in enumerate(quizzes,1))+'<button type="button" onclick="gradeQuiz()">Check answers</button>'}
 for panel,markup in values.items():
  el=s.select_one('#'+panel);el.clear();el.append(BeautifulSoup(markup,'html.parser'))
 s.select_one('#tab-btn-practice').string='2. Practice ('+str(len(problems))+')'
 s.select_one('#tab-btn-test').string='4. Diagnostic ('+str(len(quizzes))+')'
 s.select_one('.ib-footer p').string='© 2026 SJMaths · IB DP Mathematics '+course+' · Sandeep Jaiswal'
 # Retain established tab, theme and mobile-dock scripts. Remove template-only stray text.
 output=str(s).replace('">>','">').replace('<head>','<head>\n'+MARK,1)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(output,encoding='utf-8',newline='\n');print(rel,'created')
