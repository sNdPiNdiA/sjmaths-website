(function(){
  'use strict';

  function snapOffset(){
    var bar=document.querySelector('.tabs');
    return bar?bar.getBoundingClientRect().bottom:0;
  }
  /* Only scroll when the target would otherwise open underneath the sticky toolbar. */
  function reveal(target){
    if(!target)return;
    if(target.getBoundingClientRect().top<snapOffset()-1){
      target.scrollIntoView({block:'start',behavior:'smooth'});
    }
  }
  function panelFor(button){return document.getElementById('p-'+button.dataset.t)}

  var tabs=document.querySelectorAll('.tabbtn');
  function activateTab(button,moveFocus){
    tabs.forEach(function(item){
      var active=item===button;
      item.classList.toggle('on',active);
      if(active)item.setAttribute('aria-current','location');
      else item.removeAttribute('aria-current');
    });
    if(moveFocus)button.focus();
    var target=panelFor(button);
    if(target){
      if(window.history&&window.history.replaceState)window.history.replaceState(null,'',button.getAttribute('href'));
      target.scrollIntoView({block:'start',behavior:'smooth'});
    }
  }
  tabs.forEach(function(button,index){
    if(button.classList.contains('on'))button.setAttribute('aria-current','location');
    button.addEventListener('click',function(event){event.preventDefault();activateTab(button,false)});
    button.addEventListener('keydown',function(event){
      var next;
      if(event.key==='ArrowRight')next=tabs[(index+1)%tabs.length];
      if(event.key==='ArrowLeft')next=tabs[(index+tabs.length-1)%tabs.length];
      if(event.key==='Home')next=tabs[0];
      if(event.key==='End')next=tabs[tabs.length-1];
      if(next){event.preventDefault();activateTab(next,true);}
    });
  });

  document.querySelectorAll('.subtabs').forEach(function(group){
    var buttons=group.querySelectorAll('.subtab');
    function activate(button,moveFocus){
      buttons.forEach(function(item){
        var active=item===button;
        item.classList.toggle('on',active);
        if(active)item.setAttribute('aria-current','location');
        else item.removeAttribute('aria-current');
      });
      if(moveFocus)button.focus();
      var target=document.getElementById(button.dataset.st);
      if(target){
        if(window.history&&window.history.replaceState)window.history.replaceState(null,'',button.getAttribute('href'));
        target.scrollIntoView({block:'start',behavior:'smooth'});
      }
    }
    buttons.forEach(function(button,index){
      if(button.classList.contains('on'))button.setAttribute('aria-current','location');
      button.addEventListener('click',function(event){event.preventDefault();activate(button,false)});
      button.addEventListener('keydown',function(event){
        var next;
        if(event.key==='ArrowRight')next=buttons[(index+1)%buttons.length];
        if(event.key==='ArrowLeft')next=buttons[(index+buttons.length-1)%buttons.length];
        if(event.key==='Home')next=buttons[0];
        if(event.key==='End')next=buttons[buttons.length-1];
        if(next){event.preventDefault();activate(next,true);}
      });
    });
  });

  function openExerciseTarget(targetId){
    var target=document.getElementById(targetId);
    if(!target)return;
    if(window.history&&window.history.replaceState)window.history.replaceState(null,'','#'+targetId);
    window.setTimeout(function(){target.scrollIntoView({block:'start',behavior:'smooth'});},0);
  }
  document.querySelectorAll('[data-exercise-link]').forEach(function(link){
    link.addEventListener('click',function(event){
      event.preventDefault();
      openExerciseTarget(link.dataset.exerciseLink);
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
