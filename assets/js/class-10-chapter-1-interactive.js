/*---INTERACTIVELOGIC(Class10Chapter1)---*/

document.addEventListener('DOMContentLoaded',()=>{
console.log("InteractiveNotesLoaded");
});

//1.FlipCardToggle
functiontoggleFlip(element){
element.classList.toggle('flipped');
}

//2.ProofStepToggle
functiontoggleProofStep(header){
constcontent=header.nextElementSibling;
consticon=header.querySelector('i');

if(content.style.display==="block"){
content.style.display="none";
icon.className="fasfa-chevron-down";
header.style.background="#f9f9f9";
}else{
content.style.display="block";
icon.className="fasfa-chevron-up";
header.style.background="#e3f2fd";//Slightbluehighlight
}
}

//3.PrimeFactorizationEngine
functioncalcFactorsInteractive(){
letn=parseInt(document.getElementById('factorInput').value);
constdisplay=document.getElementById('factorResult');

if(isNaN(n)||n<2){
display.style.display='block';
display.innerHTML="<spanstyle='color:red'><iclass='fasfa-exclamation-circle'></i>Enteranumber>1</span>";
return;
}

constoriginalN=n;
letfactors=[];
letdivisor=2;

while(n>=2){
if(n%divisor==0){
factors.push(divisor);
n=n/divisor;
}else{
divisor++;
}
}

constcounts={};
factors.forEach(x=>{counts[x]=(counts[x]||0)+1;});

letpowerString=Object.keys(counts).map(key=>`${key}^{${counts[key]}}`).join('\\times');
letlistString=factors.join('×');

display.style.display='block';
display.innerHTML=`
<divstyle="font-size:1rem;color:#666;">Step-by-step:${listString}</div>
<divstyle="font-size:1.4rem;color:var(--primary);margin-top:5px;font-weight:bold;">
$$${originalN}=${powerString}$$
</div>
`;
if(window.MathJax)MathJax.typesetPromise([display]);
}

//4.HCF-LCMVerifier
functioncalcHcfLcmInteractive(){
consta=parseInt(document.getElementById('numA').value);
constb=parseInt(document.getElementById('numB').value);
constres=document.getElementById('hcfResult');

if(isNaN(a)||isNaN(b)){
res.style.display='block';
res.innerHTML="Pleaseentertwovalidnumbers.";
return;
}

constgcd=(x,y)=>(!y?x:gcd(y,x%y));
consthcf=gcd(a,b);
constlcm=(a*b)/hcf;

constprodNum=a*b;
constprodHcfLcm=hcf*lcm;
constverified=prodNum===prodHcfLcm;

res.style.display='block';
res.innerHTML=`
<divstyle="display:grid;grid-template-columns:1fr1fr;gap:10px;margin-bottom:10px;">
<divstyle="background:#e8f5e9;padding:10px;border-radius:8px;">
<strong>HCF:</strong>${hcf}
</div>
<divstyle="background:#e3f2fd;padding:10px;border-radius:8px;">
<strong>LCM:</strong>${lcm}
</div>
</div>
<divstyle="border-top:1pxdashed#ccc;padding-top:10px;">
Product($a\\timesb$)=${prodNum}<br>
HCF$\\times$LCM=${prodHcfLcm}<br>
${verified?'<strongstyle="color:green"><iclass="fasfa-check-circle"></i>RelationshipVerified!</strong>':'<strongstyle="color:red">Mismatch!</strong>'}
</div>
`;
if(window.MathJax)MathJax.typesetPromise([res]);
}

//5.DecimalDetective
functioncheckDecimalInteractive(){
letp=parseInt(document.getElementById('decP').value);
letq=parseInt(document.getElementById('decQ').value);
constres=document.getElementById('decResult');

if(isNaN(p)||isNaN(q)||q===0){
res.innerHTML="Invalidinput(qcannotbe0).";
res.style.display='block';
return;
}

//Simplify
constgcd=(x,y)=>(!y?x:gcd(y,x%y));
constcommon=gcd(p,q);
p/=common;
q/=common;

lettempQ=q;
while(tempQ%2===0)tempQ/=2;
while(tempQ%5===0)tempQ/=5;

letisTerminating=tempQ===1;

res.style.display='block';
res.innerHTML=`
SimplifiedFraction:<strong>${p}/${q}</strong><br>
DenominatorFactors:${isTerminating?'Only2and/or5':'Containsfactorsotherthan2,5'}<br>
<divstyle="margin-top:5px;font-size:1.1rem;font-weight:bold;color:${isTerminating?'green':'red'}">
${isTerminating?'<iclass="fasfa-check"></i>TerminatingDecimal':'<iclass="fasfa-infinity"></i>Non-TerminatingRepeating'}
</div>
`;
}

//6.GamifiedQuiz
functioncheckGamified(btn,isCorrect){
constparent=btn.parentElement;
constoptions=parent.querySelectorAll('.gamified-option');

//Disablealloptions
options.forEach(opt=>{
opt.style.pointerEvents='none';
opt.onclick=null;
});

if(isCorrect){
btn.classList.add('correct');
btn.innerHTML+='<iclass="fasfa-check-circle"></i>';
//Optional:Playsuccesssound
}else{
btn.classList.add('wrong');
btn.innerHTML+='<iclass="fasfa-times-circle"></i>';

//Findandhighlightcorrectanswer
options.forEach(opt=>{
if(opt.dataset.correct==="true"){
opt.classList.add('correct');
opt.innerHTML+='<iclass="fasfa-check"></i>(Correct)';
}
});
}
}
