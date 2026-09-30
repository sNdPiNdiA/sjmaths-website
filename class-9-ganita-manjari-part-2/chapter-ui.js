(function(){
  'use strict';

  function panelFor(button){return document.getElementById('p-'+button.dataset.t)}
  function setActive(items,active,className){
    items.forEach(function(item){
      var selected=item===active;
      item.classList.toggle(className,selected);
      if(selected)item.setAttribute('aria-current','location');
      else item.removeAttribute('aria-current');
    });
  }
  var tabs=document.querySelectorAll('.tabbtn');
  function updateAddress(link){
    if(window.history&&window.history.replaceState)window.history.replaceState(null,'',link.getAttribute('href'));
  }
  function activateTab(button,options){
    options=options||{};
    setActive(tabs,button,'on');
    var target=panelFor(button);
    if(target){
      setActive(document.querySelectorAll('.panel'),target,'on');
      if(options.updateAddress)updateAddress(button);
      if(options.scroll)target.scrollIntoView({block:'start',behavior:'smooth'});
    }
    return target;
  }
  function subtabsFor(panel){return panel?panel.querySelectorAll('.subtab'):[]}
  function activateSubtab(button,options){
    options=options||{};
    var group=button.closest('.subtabs');
    var buttons=group?group.querySelectorAll('.subtab'):[];
    setActive(buttons,button,'on');
    var target=document.getElementById(button.dataset.st);
    if(target){
      setActive(group.parentElement.querySelectorAll('.subpanel'),target,'on');
      var exerciseTab=document.querySelector('.tabbtn[data-t="exercises"]');
      if(exerciseTab)activateTab(exerciseTab,{updateAddress:false,scroll:false});
      if(options.updateAddress)updateAddress(button);
      if(options.scroll)target.scrollIntoView({block:'start',behavior:'smooth'});
      if(options.focus){target.setAttribute('tabindex','-1');target.focus({preventScroll:true});}
    }
    return target;
  }
  function buildExerciseSteppers(){
    document.querySelectorAll('.subtabs').forEach(function(group){
      var buttons=group.querySelectorAll('.subtab');
      buttons.forEach(function(button,index){
        var panel=document.getElementById(button.dataset.st);
        if(!panel||panel.querySelector('.exercise-stepper'))return;
        var nav=document.createElement('nav');
        nav.className='exercise-stepper';
        nav.setAttribute('aria-label','Exercise navigation');
        var previous=document.createElement('button');
        previous.type='button';
        previous.className='exercise-stepper-button';
        previous.textContent='Previous';
        previous.disabled=index===0;
        previous.addEventListener('click',function(){
          if(index>0)activateSubtab(buttons[index-1],{updateAddress:true,scroll:true,focus:true});
        });
        var position=document.createElement('span');
        position.className='exercise-stepper-position';
        position.textContent='Section '+(index+1)+' of '+buttons.length;
        var next=document.createElement('button');
        next.type='button';
        next.className='exercise-stepper-button exercise-stepper-next';
        next.textContent=index===buttons.length-1?'End of exercises':'Next exercise';
        next.disabled=index===buttons.length-1;
        next.addEventListener('click',function(){
          if(index<buttons.length-1)activateSubtab(buttons[index+1],{updateAddress:true,scroll:true,focus:true});
        });
        nav.appendChild(previous);
        nav.appendChild(position);
        nav.appendChild(next);
        panel.appendChild(nav);
      });
    });
  }
  tabs.forEach(function(button,index){
    if(button.classList.contains('on'))button.setAttribute('aria-current','location');
    button.addEventListener('click',function(event){event.preventDefault();activateTab(button,{updateAddress:true,scroll:true})});
    button.addEventListener('keydown',function(event){
      var next;
      if(event.key==='ArrowRight')next=tabs[(index+1)%tabs.length];
      if(event.key==='ArrowLeft')next=tabs[(index+tabs.length-1)%tabs.length];
      if(event.key==='Home')next=tabs[0];
      if(event.key==='End')next=tabs[tabs.length-1];
      if(next){event.preventDefault();activateTab(next,{updateAddress:true,scroll:true});next.focus();}
    });
  });
  document.querySelectorAll('.subtabs').forEach(function(group){
    var buttons=group.querySelectorAll('.subtab');
    buttons.forEach(function(button,index){
      if(button.classList.contains('on'))button.setAttribute('aria-current','location');
      button.addEventListener('click',function(event){event.preventDefault();activateSubtab(button,{updateAddress:true,scroll:true})});
      button.addEventListener('keydown',function(event){
        var next;
        if(event.key==='ArrowRight')next=buttons[(index+1)%buttons.length];
        if(event.key==='ArrowLeft')next=buttons[(index+buttons.length-1)%buttons.length];
        if(event.key==='Home')next=buttons[0];
        if(event.key==='End')next=buttons[buttons.length-1];
        if(next){event.preventDefault();activateSubtab(next,{updateAddress:true,scroll:true});next.focus();}
      });
    });
  });
  buildExerciseSteppers();

  function activateFromAddress(){
    var id=window.location.hash.slice(1);
    try{id=decodeURIComponent(id);}catch(error){return;}
    if(!id)return;
    var target=document.getElementById(id);
    if(target&&target.classList.contains('subpanel')){
      var button=Array.from(document.querySelectorAll('.subtab')).find(function(item){return item.dataset.st===id});
      if(button)activateSubtab(button,{scroll:false});
      return;
    }
    var panel=target&&target.classList.contains('panel')?target:null;
    if(panel&&panel.classList.contains('panel')){
      var tab=Array.from(tabs).find(function(item){return item.getAttribute('href')==='#'+panel.id});
      if(tab)activateTab(tab,{scroll:false});
    }
  }
  activateFromAddress();
  window.addEventListener('hashchange',activateFromAddress);
  /* The source HTML stays complete for crawlers and no-JS readers. Only after
     the controls are ready do we turn the in-page links into exclusive tabs. */
  document.documentElement.classList.add('chapter-tabs-ready');
  document.querySelectorAll('[data-exercise-link]').forEach(function(link){
    link.addEventListener('click',function(event){
      event.preventDefault();
      var button=Array.from(document.querySelectorAll('.subtab')).find(function(item){return item.dataset.st===link.dataset.exerciseLink});
      if(button)activateSubtab(button,{updateAddress:true,scroll:true});
    });
  });

  document.querySelectorAll('.ws .wh').forEach(function(header){
    header.setAttribute('role','button');
    header.setAttribute('tabindex','0');
    header.setAttribute('aria-expanded',header.parentElement.classList.contains('opn')?'true':'false');
    function toggle(){
      var open=header.parentElement.classList.toggle('opn');
      header.setAttribute('aria-expanded',open?'true':'false');
    }
    header.addEventListener('click',toggle);
    header.addEventListener('keydown',function(event){
      if(event.key==='Enter'||event.key===' '){event.preventDefault();toggle();}
    });
  });

  function injectExerciseAnswers(){
    var answerData=document.getElementById('exercise-answers');
    var exerciseDetails=document.querySelectorAll('#p-exercises details');
    if(!answerData||!exerciseDetails.length)return;
    var answers=JSON.parse(answerData.textContent||'[]');
    exerciseDetails.forEach(function(detail,index){
      // Current pages ship the full answer as HTML; only enhance it once.
      if(detail.querySelector('.answer-box'))return;
      var answer=answers[index]&&answers[index].answer;
      if(!answer)return;
      var body=detail.querySelector(':scope > .db');
      if(!body){body=document.createElement('div');body.className='db';detail.appendChild(body);}
      var controls=document.createElement('div');
      controls.className='answer-controls';
      var label=document.createElement('span');
      label.className='answer-kicker';
      label.textContent='Answer / method';
      var button=document.createElement('button');
      button.type='button';
      button.className='btng btn tog';
      button.textContent='Show Answer';
      controls.appendChild(label);
      controls.appendChild(button);
      var content=document.createElement('div');
      content.className='an answer-text';
      content.textContent=answer;
      var answerBox=document.createElement('div');
      answerBox.className='answer-box';
      answerBox.appendChild(controls);
      answerBox.appendChild(content);
      body.appendChild(answerBox);
    });
  }
  injectExerciseAnswers();
  function setAnswerState(answerBox,visible){
    if(!answerBox)return;
    answerBox.classList.toggle('sh',visible);
    var button=answerBox.querySelector('.tog');
    if(button){
      button.textContent=visible?'Hide Answer':'Show Answer';
      button.setAttribute('aria-expanded',visible?'true':'false');
    }
  }
  document.querySelectorAll('.tog').forEach(function(button){
    var answerBox=button.closest('.answer-box')||button.parentElement;
    button.setAttribute('aria-expanded',answerBox.classList.contains('sh')?'true':'false');
    button.addEventListener('click',function(){
      setAnswerState(answerBox,!answerBox.classList.contains('sh'));
    });
    answerBox.classList.add('answer-ready');
  });

  /* A long notes panel needs a way in. Built from the section headings. */
  function buildChapterMap(){
    var notes=document.getElementById('p-notes');
    if(!notes)return;
    var headings=notes.querySelectorAll('.card > h2');
    if(headings.length<3)return;
    var list=document.createElement('ul');
    list.className='toc-list';
    headings.forEach(function(heading,index){
      var numberNode=heading.querySelector('.section-no');
      var label=heading.textContent.trim();
      if(!heading.id)heading.id='section-'+(index+1);
      var item=document.createElement('li');
      var link=document.createElement('a');
      link.href='#'+heading.id;
      if(numberNode){
        var mark=document.createElement('span');
        mark.className='toc-n';
        mark.textContent=numberNode.textContent;
        link.appendChild(mark);
        label=heading.textContent.replace(numberNode.textContent,'').trim();
      }
      link.appendChild(document.createTextNode(label));
      item.appendChild(link);
      list.appendChild(item);
    });
    var detailsNode=document.createElement('details');
    detailsNode.className='toc';
    if(window.matchMedia('(min-width:560px)').matches)detailsNode.open=true;
    var summaryNode=document.createElement('summary');
    var title=document.createElement('span');
    title.textContent='Chapter map';
    var count=document.createElement('span');
    count.className='toc-count';
    count.textContent=headings.length+' sections';
    summaryNode.appendChild(title);
    summaryNode.appendChild(count);
    detailsNode.appendChild(summaryNode);
    detailsNode.appendChild(list);
    var anchor=notes.querySelector('.card');
    if(anchor)anchor.appendChild(detailsNode);else notes.insertBefore(detailsNode,notes.firstChild);
  }
  buildChapterMap();

  var quizBox=document.getElementById('quiz');
  var quizData=document.getElementById('quiz-data');
  if(!quizBox||!quizData)return;
  var questions=JSON.parse(quizData.textContent||'[]'),score=0,done={};
  var scoreNode=document.getElementById('score');
  var bar=document.getElementById('tbar');
  if(bar){
    bar.parentElement.setAttribute('role','progressbar');
    bar.parentElement.setAttribute('aria-label','Test progress');
    bar.parentElement.setAttribute('aria-valuemin','0');
    bar.parentElement.setAttribute('aria-valuemax',String(questions.length));
    bar.parentElement.setAttribute('aria-valuenow','0');
  }
  if(scoreNode)scoreNode.setAttribute('aria-live','polite');
  function updateProgress(){
    var answered=Object.keys(done).length;
    if(scoreNode)scoreNode.textContent='Score: '+score+' / '+questions.length;
    if(!bar)return;
    bar.style.width=(answered/questions.length*100)+'%';
    bar.parentElement.setAttribute('aria-valuenow',String(answered));
  }
  function lockItem(item,index){
    item.querySelectorAll('.op')[questions[index].a].classList.add('ok');
    item.querySelectorAll('.op').forEach(function(choice){choice.disabled=true;});
  }
  function renderQuiz(){
    quizBox.innerHTML='';
    questions.forEach(function(question,index){
      var item=document.createElement('div');
      item.className='mc';
      var title=document.createElement('h4');
      title.textContent='Q'+(index+1)+'. '+question.q;
      item.appendChild(title);
      question.o.forEach(function(option,optionIndex){
        var button=document.createElement('button');
        button.className='op';
        button.type='button';
        button.textContent=option;
        button.addEventListener('click',function(){
          if(done[index])return;
          done[index]=true;
          if(optionIndex===question.a)button.classList.add('ok');
          else button.classList.add('no');
          if(optionIndex!==question.a)item.querySelectorAll('.op')[question.a].classList.add('ok');
          else score++;
          lockItem(item,index);
          updateProgress();
        });
        item.appendChild(button);
      });
      quizBox.appendChild(item);
    });
  }
  renderQuiz();
  var retry=document.getElementById('retry');
  if(retry)retry.addEventListener('click',function(){
    score=0;done={};
    updateProgress();
    renderQuiz();
  });
  var showAll=document.getElementById('showall');
  if(showAll)showAll.addEventListener('click',function(){
    quizBox.querySelectorAll('.mc').forEach(function(item,index){
      if(done[index])return;
      done[index]=true;
      lockItem(item,index);
    });
    updateProgress();
  });
})();
