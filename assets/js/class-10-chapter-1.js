/**


*Class10Chapter1-RealNumbers


*SpecificLogicforCalculators,Proofs,andQuizzes


*/





//---1.PRIMEFACTORIZATIONENGINE---


window.calcFactors = function () {


    letn = parseInt(document.getElementById('factorInput').value);


    constdisplay = document.getElementById('factorResult');





    if (isNaN(n) || n < 2) {


        display.style.display = 'block';


        display.innerHTML = "<spanstyle='color:var(--danger)'>Pleaseenteranumber>1</span>";


        return;


    }





    constoriginalN = n;


    letfactors = [];


    letdivisor = 2;





    while (n >= 2) {


        if (n % divisor == 0) {


            factors.push(divisor);


            n = n / divisor;


        } else {


            divisor++;


        }


    }





    //Groupingforpowers(e.g.2^2)


    constcounts = {};


    factors.forEach(function (x) { counts[x] = (counts[x] || 0) + 1; });





    letpowerString = Object.keys(counts).map(key => `${key}^{${counts[key]}}`).join('\\times');


    letlistString = factors.join('×');





    display.style.display = 'block';


    display.innerHTML = `


<divstyle="font-size:1.1rem;margin-bottom:5px;"><strong>Factors:</strong>${listString}</div>


<divstyle="font-size:1.3rem;color:var(--primary);">$$${originalN}=${powerString}$$</div>


`;


    //TriggerMathJaxre-render


    if (window.MathJax) MathJax.typesetPromise();


};





//---2.HCFLCMCALCULATOR---


function gcd(a, b) {


    returnb == 0 ? a : gcd(b, a % b);


}





window.calcHcfLcm = function () {


    consta = parseInt(document.getElementById('numA').value);


    constb = parseInt(document.getElementById('numB').value);


    constres = document.getElementById('hcfResult');





    if (isNaN(a) || isNaN(b)) {


        res.style.display = 'block';


        res.innerHTML = "Pleaseentertwonumbers.";


        return;


    }





    consthcf = gcd(a, b);


    constlcm = (a * b) / hcf;


    constproduct = a * b;


    constproductHcfLcm = hcf * lcm;





    letverification = (product === productHcfLcm)


        ? "<spanstyle='color:var(--success)'><iclass='fasfa-check-circle'></i>Verified!</span>"


        : "<spanstyle='color:var(--danger)'>Mismatch!</span>";





    res.style.display = 'block';


    res.innerHTML = `


<p><strong>HCF(${a},${b})</strong>=${hcf}</p>


<p><strong>LCM(${a},${b})</strong>=${lcm}</p>


<hrstyle="margin:10px0;border-top:1pxdashed#ccc;">


<p>ProductofNumbers=${a}×${b}=<strong>${product}</strong></p>


<p>HCF×LCM=${hcf}×${lcm}=<strong>${productHcfLcm}</strong></p>


<pstyle="margin-top:5px;font-size:1.1rem;">${verification}</p>


`;


};





//---3.DECIMALDETECTIVE---


window.checkDecimal = function () {


    letp = parseInt(document.getElementById('decP').value);


    letq = parseInt(document.getElementById('decQ').value);


    constres = document.getElementById('decResult');





    if (isNaN(p) || isNaN(q) || q === 0) {


        res.style.display = 'block';


        res.innerHTML = "Invalidinput(qcannotbe0).";


        return;


    }





    //Simplifyfractionfirst


    constcommon = gcd(p, q);


    p = p / common;


    q = q / common;





    //Analyzeqforfactorsotherthan2and5


    lettempQ = q;


    while (tempQ % 2 === 0) tempQ /= 2;


    while (tempQ % 5 === 0) tempQ /= 5;





    letmsg = "";


    letcolor = "";





    if (tempQ === 1) {


        msg = `<strong>TerminatingDecimal</strong><br>Denominator${q}hasonlyfactorsof2and5.`;


        color = "var(--success)";


    } else {


        msg = `<strong>Non-TerminatingRecurring</strong><br>Denominator${q}hasfactorsotherthan2and5(residue:${tempQ}).`;


        color = "var(--danger)";


    }





    res.style.display = 'block';


    res.innerHTML = `<spanstyle="color:${color};font-size:1.1rem;">${msg}</span><br><small>SimplifiedFraction:${p}/${q}</small>`;


};





//---4.PROOFTOGGLE---


window.toggleProof = function (element) {


    constcontent = element.querySelector('.proof-content');


    if (content.style.display === "none") {


        content.style.display = "block";


        element.style.background = "var(--primary-fade,#f3e5f5)";//Fallbackcolor


    } else {


        content.style.display = "none";


        element.style.background = "";//Removehighlight


    }


};





//---5.CASESTUDYTOGGLE---


window.toggleCaseStudy = function () {


    constsol = document.getElementById('caseStudySol');


    sol.style.display = (sol.style.display === 'none') ? 'block' : 'none';


};





//---6.QUIZLOGIC---


window.checkQuiz = function (element, isCorrect) {


    constparent = element.parentElement;


    constoptions = parent.querySelectorAll('.quiz-option');





    //Disableclicksonalloptions


    options.forEach(opt => {


        opt.style.pointerEvents = 'none';


        opt.onclick = null;//Removehandlerjustincase


    });





    if (isCorrect) {


        element.classList.add('correct');


        element.innerHTML += '<iclass="fasfa-check"></i>';


    } else {


        element.classList.add('wrong');


        element.innerHTML += '<iclass="fasfa-times"></i>';





        //Findandhighlightthecorrectanswer(ifwecouldidentifyit)


        //SincethecurrentlogicpassesisCorrectbooleaninonclick,


        //weneedtofindtheelementthathasonclick="checkQuiz(this,true)"intheHTML


        //Thisisabittrickywith`onclick`attributes.


        //Abetterwayforfuturerefactoringisdataattributes.


        //Fornow,let'strytomatchbysearchingthesiblings.





        //Thispartisanenhancement:


        options.forEach(opt => {


            //Wechecktheonclickattributestring


            constattr = opt.getAttribute('onclick');


            if (attr && attr.includes('true')) {


                opt.classList.add('correct');


                opt.innerHTML += '<iclass="fasfa-check"></i>(CorrectAnswer)';


            }


        });


    }


};





//---7.FLIPCARDTOGGLE(Mobile/ClickSupport)---


window.toggleFlip = function (element) {


    element.classList.toggle('flipped');


};


