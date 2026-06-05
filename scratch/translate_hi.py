# -*- coding: utf-8 -*-
import json
import re

target_file = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\Prehistory\Prehistoric-Time-Periods\hi\index.html"

# Read the file
with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace general headers and titles
html = html.replace('<html lang="en">', '<html lang="hi">')
html = html.replace('<title>Prehistoric Time Periods - UPSC Ancient Indian History Study Guide | SJMaths</title>', '<title>प्रागैतिहासिक काल (Prehistoric Time Periods) - UPSC प्राचीन इतिहास गाइड | SJMaths</title>')
html = html.replace('<meta name="description" content="Comprehensive UPSC GS-1 guide on Prehistoric Time Periods. Notes, mnemonics, tool typology, 50 interactive practice questions, and 10 UPSC-style mock test questions.">', '<meta name="description" content="UPSC GS-1 के लिए प्रागैतिहासिक काल का व्यापक अध्ययन मार्गदर्शिका। नोट्स, स्मृति संकेत (mnemonics), उपकरण विकास, 50 अभ्यास प्रश्न, और 10 UPSC शैली मॉक टेस्ट।">')

# Breadcrumbs
html = html.replace('<span>Prehistoric Time Periods</span>', '<span>प्रागैतिहासिक काल (Prehistoric Time Periods)</span>')

# Hero copy
html = html.replace('<h1>Prehistoric Time Periods</h1>', '<h1>प्रागैतिहासिक काल (Prehistoric Time Periods)</h1>')
html = html.replace('<p>A comprehensive study guide featuring memory-assisting mnemonics, visual tools evolution, 50 practice questions, and a 10-question live mock exam.</p>', '<p>UPSC सिविल सेवा परीक्षा (GS-1) के लिए एक व्यापक, शैक्षणिक मार्गदर्शिका। इसमें स्मृति-सहायक सूत्र (Mnemonics), पाषाण उपकरणों के विकास का ग्राफ़िक, 50 बहुविकल्पीय अभ्यास प्रश्न और 10 बहु-कथनीय UPSC शैली मॉक टेस्ट शामिल हैं।</p>')
html = html.replace('<i class="fas fa-arrow-down"></i> Start Reading', '<i class="fas fa-arrow-down"></i> पढ़ना शुरू करें')

# Tabs
html = html.replace('<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. Study Notes</button>', '<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. अध्ययन नोट्स (Study Notes)</button>')
html = html.replace('<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. Practice Zone (50 Qs)</button>', '<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. अभ्यास क्षेत्र (50 प्रश्न)</button>')
html = html.replace('<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. Live UPSC Mock Test</button>', '<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. लाइव UPSC मॉक टेस्ट</button>')

# Tab 1: Study Notes - Chronological Framework
html = html.replace('<h2 class="card-title"><i class="fas fa-history"></i> The Chronological Framework</h2>', '<h2 class="card-title"><i class="fas fa-history"></i> कालानुक्रमिक ढांचा (The Chronological Framework)</h2>')
html = html.replace('<p>Click on any period card below to view its key archaeological characteristics, tool types, and major Indian sites.</p>', '<p>प्रत्येक प्रागैतिहासिक काल की मुख्य पुरातात्विक विशेषताओं, उपकरण प्रकारों और प्रमुख भारतीय स्थलों को देखने के लिए नीचे दिए गए कार्डों पर क्लिक करें।</p>')

# Card Click Instruction
html = html.replace('<div class="click-instruction"><i class="fas fa-hand-pointer"></i> Click to expand</div>', '<div class="click-instruction"><i class="fas fa-hand-pointer"></i> विवरण देखने के लिए क्लिक करें</div>')

# Timeline Cards - Paleolithic
html = html.replace('<div class="timeline-period">Paleolithic Age</div>', '<div class="timeline-period">पुरापाषाण काल (Paleolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 2.6 MYA – 10,000 BCE</div>', '<div class="timeline-date">लगभग 2.6 MYA – 10,000 BCE</div>')
paleo_details_en = """                            <strong>Old Stone Age:</strong> Longest prehistoric phase (99% of human history).<br>
                            &bull; <strong>Tools:</strong> Hand-axes, cleavers, choppers (crude/heavy). Made of Quartzite.<br>
                            &bull; <strong>Livelihood:</strong> Hunting-gathering, nomadic, caves/shelters. Fire discovered.<br>
                            &bull; <strong>Key Sites:</strong> Soan Valley (Pakistan), Attirampakkam (TN), Bhimbetka (MP)."""
paleo_details_hi = """                            <strong>पुरापाषाण काल (Old Stone Age):</strong> सबसे लंबी प्रागैतिहासिक अवधि (मानव इतिहास का 99%)।<br>
                            &bull; <strong>उपकरण:</strong> हस्त-कुठार (Hand-axes), विदारणी (Cleavers), गंडासा (Choppers) (कच्चे/भारी)। ये मुख्यतः क्वार्ट्जाइट पत्थर से बने थे, इसलिए आदिमानव को 'क्वार्ट्जाइट मैन' भी कहा जाता था।<br>
                            &bull; <strong>जीवनशैली:</strong> शिकारी-संग्रहकर्ता, खानाबदोश, गुफाओं और चट्टानी आश्रयों में निवास। आग की खोज हुई।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> सोअन घाटी (पाकिस्तान), अतिरामपक्कम (तमिलनाडु), भीमबेटका (मध्य प्रदेश)।"""
html = html.replace(paleo_details_en, paleo_details_hi)

# Timeline Cards - Mesolithic
html = html.replace('<div class="timeline-period">Mesolithic Age</div>', '<div class="timeline-period">मध्यपाषाण काल (Mesolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 10,000 – 8,000 BCE</div>', '<div class="timeline-date">लगभग 10,000 – 8,000 BCE</div>')
meso_details_en = """                            <strong>Middle Stone Age:</strong> Transitional period marking climate warming (Holocene).<br>
                            &bull; <strong>Tools:</strong> Microliths (1-5 cm tiny geometric blades).<br>
                            &bull; <strong>Livelihood:</strong> Incipient domestication of animals begins, fishing, rock art.<br>
                            &bull; <strong>Key Sites:</strong> Bagor (Rajasthan), Adamgarh (MP), Langhnaj (Gujarat)."""
meso_details_hi = """                            <strong>मध्यपाषाण काल (Middle Stone Age):</strong> संक्रमण काल जो जलवायु के गर्म होने (होलोसीन युग) को दर्शाता है।<br>
                            &bull; <strong>उपकरण:</strong> माइक्रोलिथ (1-5 सेमी के छोटे ज्यामितीय ब्लेड, त्रिकोण, अर्धचंद्र)।<br>
                            &bull; <strong>जीवनशैली:</strong> पशुपालन की शुरुआत, शिकार, मछली पकड़ना, शैल चित्र (rock art) का विकास।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> बागोर (राजस्थान - सबसे बड़ा मेसोलिथिक स्थल), अदमगढ़ (मध्य प्रदेश - पशुपालन के सबसे पुराने साक्ष्य), लघनाज (गुजरात)।"""
html = html.replace(meso_details_en, meso_details_hi)

# Timeline Cards - Neolithic
html = html.replace('<div class="timeline-period">Neolithic Age</div>', '<div class="timeline-period">नवपाषाण काल (Neolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 8,000 – 2,000 BCE</div>', '<div class="timeline-date">लगभग 8,000 – 2,000 BCE</div>')
neo_details_en = """                            <strong>Neolithic Revolution:</strong> Shift from food-gathering to food-producing.<br>
                            &bull; <strong>Tools:</strong> Polished stone tools, ground axes, celts.<br>
                            &bull; <strong>Livelihood:</strong> Agriculture (wheat, barley, rice), settled village life, wheel-made pottery.<br>
                            &bull; <strong>Key Sites:</strong> Mehrgarh (Balochistan), Burzahom (J&K), Koldihwa (UP)."""
neo_details_hi = """                            <strong>नवपाषाण क्रांति (Neolithic Revolution):</strong> भोजन-संग्रहक से भोजन-उत्पादक (कृषि) बनने का युग।<br>
                            &bull; <strong>उपकरण:</strong> पॉलिशदार पत्थर के उपकरण, घिसे हुए सेल्ट (Celts) और कुल्हाड़ियाँ।<br>
                            &bull; <strong>जीवनशैली:</strong> व्यवस्थित ग्राम जीवन, कृषि (गेहूं, जौ, धान), चाक पर बने मिट्टी के बर्तन, पहिये का आविष्कार।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> मेहरगढ़ (बलूचिस्तान - प्राचीनतम कृषि साक्ष्य), बुर्जहोम (कश्मीर - गर्त-आवास या pit-dwellings और मालिक के साथ कुत्ता दफनाने की प्रथा), कोलडिहवा (उत्तर प्रदेश - प्राचीनतम चावल)।"""
html = html.replace(neo_details_en, neo_details_hi)

# Timeline Cards - Chalcolithic
html = html.replace('<div class="timeline-period">Chalcolithic Age</div>', '<div class="timeline-period">ताम्रपाषाण काल (Chalcolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 2,000 – 1,500 BCE</div>', '<div class="timeline-date">लगभग 2,000 – 1,500 BCE</div>')
chalco_details_en = """                            <strong>Copper-Stone Age:</strong> First use of metals (copper) alongside stone tools.<br>
                            &bull; <strong>Pottery:</strong> Black & Red Ware (BRW) pottery.<br>
                            &bull; <strong>Livelihood:</strong> Agricultural village economies (non-urban, non-Harappan).<br>
                            &bull; <strong>Key Sites:</strong> Inamgaon & Daimabad (Maharashtra), Ahar (Rajasthan)."""
chalco_details_hi = """                            <strong>ताम्र-पाषाण युग (Copper-Stone Age):</strong> पत्थर के साथ-साथ धातु (तांबा) का पहला प्रयोग।<br>
                            &bull; <strong>मृदभांड:</strong> काले और लाल मृदभांड (Black and Red Ware - BRW)।<br>
                            &bull; <strong>जीवनशैली:</strong> कृषि ग्रामीण संस्कृतियाँ (गैर-शहरी)।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> जोरवे संस्कृति (इनामगांव और दैमाबाद, महाराष्ट्र), आहार-बनास संस्कृति (आहार और गिलुंड, राजस्थान)।"""
html = html.replace(chalco_details_en, chalco_details_hi)

# Timeline Cards - Iron Age
html = html.replace('<div class="timeline-period">Iron Age</div>', '<div class="timeline-period">लौह युग (Iron Age)</div>')
html = html.replace('<div class="timeline-date">c. 1,500 BCE onward</div>', '<div class="timeline-date">लगभग 1,500 BCE से आगे</div>')
iron_details_en = """                            <strong>Early Iron Age:</strong> Use of iron tools leading to agricultural surplus.<br>
                            &bull; <strong>Burials:</strong> Megaliths (dolmens, menhirs) in South India.<br>
                            &bull; <strong>Pottery:</strong> Painted Grey Ware (PGW) and NBPW.<br>
                            &bull; <strong>Impact:</strong> Laid base for Second Urbanisation (600 BCE)."""
iron_details_hi = """                            <strong>प्रारंभिक लौह युग:</strong> लोहे के औजारों का उपयोग जिससे कृषि अधिशेष और आर्थिक विकास हुआ।<br>
                            &bull; <strong>समाधियाँ:</strong> दक्षिण भारत में महापाषाण (Megaliths - डोलमेंस, मेनहिर) समाधियाँ।<br>
                            &bull; <strong>मृदभांड:</strong> चित्रित धूसर मृदभांड (PGW) और उत्तरी काले चमकीले मृदभांड (NBPW)।<br>
                            &bull; <strong>प्रभाव:</strong> गंगा घाटी में द्वितीय नगरीकरण (600 BCE - महाजनपद काल) का मार्ग प्रशस्त हुआ।"""
html = html.replace(iron_details_en, iron_details_hi)

# Mnemonics & Memory Hacks
html = html.replace('<h2 class="card-title"><i class="fas fa-lightbulb"></i> Mnemonics & Memory Palace Hooks</h2>', '<h2 class="card-title"><i class="fas fa-lightbulb"></i> स्मृति सहायक सूत्र (Mnemonics & Memory Hooks)</h2>')
html = html.replace('<p>Use these structured mnemonic associations to remember sequence, tools, and sites forever.</p>', '<p>कालक्रम, खोजों और प्रमुख स्थलों को हमेशा के लिए याद रखने के लिए इन तीन स्मृति सूत्रों का उपयोग करें।</p>')
html = html.replace('<div class="mnemonic-title">Mnemonic 1: Chronological Sequence</div>', '<div class="mnemonic-title">स्मृति सूत्र 1: कालानुक्रमिक क्रम</div>')
html = html.replace('<div class="mnemonic-title">Mnemonic 2: Earliest Domestication and Sites</div>', '<div class="mnemonic-title">स्मृति सूत्र 2: पशुपालन की शुरुआत और प्रमुख स्थल</div>')
html = html.replace('<div class="mnemonic-title">Mnemonic 3: Neolithic Major Discoveries</div>', '<div class="mnemonic-title">स्मृति सूत्र 3: नवपाषाण कालीन प्रमुख खोजें/स्थल</div>')

# Evolution of Prehistoric Tool Typology
html = html.replace('<h2 class="card-title"><i class="fas fa-hammer"></i> Evolution of Prehistoric Tool Typology</h2>', '<h2 class="card-title"><i class="fas fa-hammer"></i> प्रागैतिहासिक उपकरणों के प्रकारों का विकास</h2>')
html = html.replace('<p>Observe the progressive reduction in tool size and increase in technological precision over time:</p>', '<p>समय के साथ उपकरण के आकार में कमी और तकनीकी सटीकता में वृद्धि का विश्लेषण करें:</p>')
html = html.replace('<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Crude Bifaces, Handaxes, Choppers (Quartzite)</p>', '<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">कच्चे हस्त-कुठार, गंडासा (क्वार्ट्जाइट पत्थर)</p>')
html = html.replace('<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Microliths (1-5 cm tiny Lunates, Triangles)</p>', '<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">माइक्रोलिथ (1-5 सेमी के छोटे ब्लेड, त्रिकोण, अर्धचंद्र)</p>')
html = html.replace('<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Polished Celts, Polished Ground Axes</p>', '<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">पॉलिशदार पत्थर के उपकरण, घिसे हुए सेल्ट और कुल्हाड़ियाँ</p>')
html = html.replace('<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Copper Axes, Bronze chisels alongside chert flakes</p>', '<p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">तांबे की कुल्हाड़ियाँ और कांस्य छैनी, पत्थर के साथ</p>')

# Common Traps
html = html.replace('<h2 class="card-title" style="color: #e74c3c;"><i class="fas fa-triangle-exclamation"></i> UPSC Common Exam Traps</h2>', '<h2 class="card-title" style="color: #e74c3c;"><i class="fas fa-triangle-exclamation"></i> UPSC सामान्य परीक्षा ट्रैप (भ्रम)</h2>')
html = html.replace('<strong>Trap 1: Domestication vs. Agriculture:</strong> Domestication of animals began in the <em>Mesolithic</em> period (earliest evidence: Adamgarh & Bagor). Agriculture, however, became a mainstream practice only during the <em>Neolithic</em> period. Do not confuse the two!', '<strong>भ्रम 1: पशुपालन बनाम कृषि:</strong> पशुपालन की शुरुआत <em>मध्यपाषाण (Mesolithic)</em> काल में हुई थी (सबसे पुराना साक्ष्य: अदमगढ़ और बागोर)। जबकि कृषि का विकास मुख्य रूप से <em>नवपाषाण (Neolithic)</em> काल में हुआ। दोनों में भ्रमित न हों!')
html = html.replace('<strong>Trap 2: Megaliths Geography:</strong> Although Megaliths (large stone graves) are widely associated with South Indian Iron Age cultures, they are also found in Central India, Maharashtra, and Kashmir (e.g. Burzahom).', '<strong>भ्रम 2: महापाषाण (Megaliths) का भूगोल:</strong> यद्यपि महापाषाण समाधियां मुख्य रूप से दक्षिण भारत के लौह युग से जुड़ी हैं, वे मध्य भारत, महाराष्ट्र और कश्मीर (जैसे बुर्जहोम) में भी पाई गई हैं।')
html = html.replace('<strong>Trap 3: Harappan overlap:</strong> Most Chalcolithic cultures (Jorwe, Malwa, Banas) were rural, farming villages and flourished <em>after</em> or during the decline of the urban Indus Valley Civilization (post-2000 BCE). They were not precursors to Harappa, except Kot Diji or Amri.', '<strong>भ्रम 3: हड़प्पा ओवरलैप:</strong> अधिकांश ताम्रपाषाण कालीन संस्कृतियां (जोरवे, मालवा, बनास) ग्रामीण थीं और शहरी सिंधु घाटी सभ्यता के पतन के <em>बाद</em> या उसके दौरान (2000 ईपू के बाद) विकसित हुईं। ये हड़प्पा से पहले की संस्कृतियां नहीं थीं (कोट दीजी या आमरी को छोड़कर)।')

# Practice Zone text
html = html.replace('<h2 class="card-title"><i class="fas fa-list-check"></i> Practice Zone: 50 Questions</h2>', '<h2 class="card-title"><i class="fas fa-list-check"></i> अभ्यास क्षेत्र: 50 प्रश्न</h2>')
html = html.replace('<p>Click on the options to check your answer instantly. Click "Show Explanation" to read step-by-step solutions.</p>', '<p>उत्तरों की तुरंत जांच करने के लिए विकल्पों पर क्लिक करें। विस्तृत समाधान पढ़ने के लिए "व्याख्या देखें" पर क्लिक करें।</p>')
html = html.replace("card.innerHTML = `\\n                    <div class=\\\"q-header\\\">\\n                        <span class=\\\"q-badge\\\">Q ${globalIdx + 1}</span>\\n                        <div>${q.q}</div>\\n                    </div>\\n                    <ul class=\\\"options-list\\\">${optsHtml}</ul>\\n                    <button class=\\\"sol-btn\\\" onclick=\\\"toggleExplanation(${globalIdx})\\\">Show Explanation</button>\\n                    <div class=\\\"explanation-box\\\" id=\\\"exp-${globalIdx}\\\">\\n                        <strong>Explanation:</strong> ${q.sol}\\n                    </div>\\n                `;", "card.innerHTML = `\n                    <div class=\"q-header\">\n                        <span class=\"q-badge\">Q ${globalIdx + 1}</span>\n                        <div>${q.q}</div>\n                    </div>\n                    <ul class=\"options-list\">${optsHtml}</ul>\n                    <button class=\"sol-btn\" onclick=\"toggleExplanation(${globalIdx})\">व्याख्या देखें</button>\n                    <div class=\"explanation-box\" id=\"exp-${globalIdx}\">\n                        <strong>व्याख्या:</strong> ${q.sol}\n                    </div>\n                `;")

# Test Zone text
html = html.replace('<h2>UPSC-Style Prehistory Mock Test</h2>', '<h2>UPSC शैली प्रागैतिहासिक मॉक टेस्ट</h2>')
html = html.replace('<p style="color: var(--text-light); margin: 0.5rem 0 1.5rem;">Contains 10 multi-statement questions testing conceptual understanding and site locations. 1/3 negative marking applies.</p>', '<p style="color: var(--text-light); margin: 0.5rem 0 1.5rem;">अवधारणात्मक समझ और स्थलों की स्थिति का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।</p>')
html = html.replace('<button class="btn-action btn-next" onclick="startTest()">Start Live Test</button>', '<button class="btn-action btn-next" onclick="startTest()">लाइव टेस्ट शुरू करें</button>')
html = html.replace('Time: 00:00', 'समय: 00:00')
html = html.replace('Time:', 'समय:')
html = html.replace('Question 1 of 10', 'प्रश्न 1 of 10')
html = html.replace('document.getElementById(\'testProgress\').textContent = `Question ${currentTestIdx + 1} of ${testQuestions.length}`;', 'document.getElementById(\'testProgress\').textContent = `प्रश्न ${currentTestIdx + 1} of ${testQuestions.length}`;')
html = html.replace('Question ${currentTestIdx + 1}', 'प्रश्न ${currentTestIdx + 1}')
html = html.replace("container.innerHTML = `\\n                <div class=\\\"test-q-num\\\">Question ${currentTestIdx + 1}</div>\\n                <div class=\\\"test-q-text\\\">${q.q.replace(/\\\\n/g, '<br>')}</div>\\n                <div class=\\\"test-options\\\">${optionsHtml}</div>\\n            `;", "container.innerHTML = `\n                <div class=\"test-q-num\">प्रश्न ${currentTestIdx + 1}</div>\n                <div class=\"test-q-text\">${q.q.replace(/\\n/g, '<br>')}</div>\n                <div class=\"test-options\">${optionsHtml}</div>\n            `;")
html = html.replace("nextBtn.textContent = 'Submit Test';", "nextBtn.textContent = 'टेस्ट जमा करें';")
html = html.replace("nextBtn.textContent = 'Next';", "nextBtn.textContent = 'आगे बढ़ें';")
html = html.replace("Previous", "पीछे जाएं")

# Test results panel
html = html.replace('<h2 style="font-family: \'Outfit\', sans-serif; margin-bottom: 0.5rem;">Test Complete!</h2>', '<h2 style="font-family: \'Outfit\', sans-serif; margin-bottom: 0.5rem;">टेस्ट समाप्त!</h2>')
html = html.replace('<button class="btn-action btn-next" onclick="restartTest()">Restart Test</button>', '<button class="btn-action btn-next" onclick="restartTest()">टेस्ट दोबारा शुरू करें</button>')
html = html.replace('<h3 style="border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem; margin-bottom: 1rem;"><i class="fas fa-square-poll-vertical"></i> Question Review</h3>', '<h3 style="border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem; margin-bottom: 1rem;"><i class="fas fa-square-poll-vertical"></i> प्रश्नों की समीक्षा</h3>')

# Result review rendering JS
review_item_html_en = """                    <div class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                        ${isCorrect ? '<i class="fas fa-check"></i> Correct' : '<i class="fas fa-xmark"></i> Incorrect / Unanswered'}
                    </div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem;">Q${idx + 1}. ${q.q.replace(/\\n/g, '<br>')}</div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Your Answer:</strong> ${userAnswers[idx] !== null ? q.opts[userAnswers[idx]] : '<span style="color:#e74c3c">Not Answered</span>'}
                    </div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Correct Answer:</strong> ${q.opts[q.ans]}
                    </div>
                    <div style="background: rgba(0,0,0,0.02); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem; margin-top: 0.5rem;">
                        <strong>Explanation:</strong> ${q.sol}
                    </div>"""

review_item_html_hi = """                    <div class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                        ${isCorrect ? '<i class="fas fa-check"></i> सही' : '<i class="fas fa-xmark"></i> गलत / अनुत्तरित'}
                    </div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem;">Q${idx + 1}. ${q.q.replace(/\\n/g, '<br>')}</div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>आपका उत्तर:</strong> ${userAnswers[idx] !== null ? q.opts[userAnswers[idx]] : '<span style="color:#e74c3c">अनुत्तरित</span>'}
                    </div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>सही उत्तर:</strong> ${q.opts[q.ans]}
                    </div>
                    <div style="background: rgba(0,0,0,0.02); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem; margin-top: 0.5rem;">
                        <strong>व्याख्या:</strong> ${q.sol}
                    </div>"""

html = html.replace(review_item_html_en, review_item_html_hi)

# Summary text logic
html = html.replace("document.getElementById('resultSummaryText').textContent = `You answered ${correctCount} questions correctly out of ${testQuestions.length} in ${Math.floor(testSeconds / 60)} minutes and ${testSeconds % 60} seconds.`;", "const incorrectCount = testQuestions.length - correctCount - userAnswers.filter(a => a === null).length; const totalScore = (correctCount * 2) - (incorrectCount * (2/3)); document.getElementById('resultSummaryText').textContent = `आपने ${Math.floor(testSeconds / 60)} मिनट ${testSeconds % 60} सेकंड में ${correctCount} सही, ${incorrectCount} गलत और ${userAnswers.filter(a => a === null).length} अनुत्तरित प्रश्न किए। UPSC प्राप्तांक (UPSC Score): ${totalScore.toFixed(2)} / 20.00`;")

# -*- coding: utf-8 -*-
import json
import re

target_file = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\Prehistory\Prehistoric-Time-Periods\hi\index.html"

# Read the file
with open(target_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace general headers and titles
html = html.replace('<html lang="en">', '<html lang="hi">')
html = html.replace('<title>Prehistoric Time Periods - UPSC Ancient Indian History Study Guide | SJMaths</title>', '<title>प्रागैतिहासिक काल (Prehistoric Time Periods) - UPSC प्राचीन इतिहास गाइड | SJMaths</title>')
html = html.replace('<meta name="description" content="Comprehensive UPSC GS-1 guide on Prehistoric Time Periods. Notes, mnemonics, tool typology, 50 interactive practice questions, and 10 UPSC-style mock test questions.">', '<meta name="description" content="UPSC GS-1 के लिए प्रागैतिहासिक काल का व्यापक अध्ययन मार्गदर्शिका। नोट्स, स्मृति संकेत (mnemonics), उपकरण विकास, 50 अभ्यास प्रश्न, और 10 UPSC शैली मॉक टेस्ट।">')

# Breadcrumbs
html = html.replace('<span>Prehistoric Time Periods</span>', '<span>प्रागैतिहासिक काल (Prehistoric Time Periods)</span>')

# Hero copy
html = html.replace('<h1>Prehistoric Time Periods</h1>', '<h1>प्रागैतिहासिक काल (Prehistoric Time Periods)</h1>')
html = html.replace('<p>A comprehensive study guide featuring memory-assisting mnemonics, visual tools evolution, 50 practice questions, and a 10-question live mock exam.</p>', '<p>UPSC सिविल सेवा परीक्षा (GS-1) के लिए एक व्यापक, शैक्षणिक मार्गदर्शिका। इसमें स्मृति-सहायक सूत्र (Mnemonics), पाषाण उपकरणों के विकास का ग्राफ़िक, 50 बहुविकल्पीय अभ्यास प्रश्न और 10 बहु-कथनीय UPSC शैली मॉक टेस्ट शामिल हैं।</p>')
html = html.replace('<i class="fas fa-arrow-down"></i> Start Reading', '<i class="fas fa-arrow-down"></i> पढ़ना शुरू करें')

# Tabs
html = html.replace('<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. Study Notes</button>', '<button class="tab-btn active" data-tab="notes-panel" role="tab" aria-selected="true" aria-controls="notes-panel"><i class="fas fa-book-open"></i> 1. अध्ययन नोट्स (Study Notes)</button>')
html = html.replace('<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. Practice Zone (50 Qs)</button>', '<button class="tab-btn" data-tab="practice-panel" role="tab" aria-selected="false" aria-controls="practice-panel"><i class="fas fa-list-check"></i> 2. अभ्यास क्षेत्र (50 प्रश्न)</button>')
html = html.replace('<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. Live UPSC Mock Test</button>', '<button class="tab-btn" data-tab="test-panel" role="tab" aria-selected="false" aria-controls="test-panel"><i class="fas fa-graduation-cap"></i> 3. लाइव UPSC मॉक टेस्ट</button>')

# Tab 1: Study Notes - Chronological Framework
html = html.replace('<h2 class="card-title"><i class="fas fa-history"></i> The Chronological Framework</h2>', '<h2 class="card-title"><i class="fas fa-history"></i> कालानुक्रमिक ढांचा (The Chronological Framework)</h2>')
html = html.replace('<p>Click on any period card below to view its key archaeological characteristics, tool types, and major Indian sites.</p>', '<p>प्रत्येक प्रागैतिहासिक काल की मुख्य पुरातात्विक विशेषताओं, उपकरण प्रकारों और प्रमुख भारतीय स्थलों को देखने के लिए नीचे दिए गए कार्डों पर क्लिक करें।</p>')

# Card Click Instruction
html = html.replace('<div class="click-instruction"><i class="fas fa-hand-pointer"></i> Click to expand</div>', '<div class="click-instruction"><i class="fas fa-hand-pointer"></i> विवरण देखने के लिए क्लिक करें</div>')

# Timeline Cards - Paleolithic
html = html.replace('<div class="timeline-period">Paleolithic Age</div>', '<div class="timeline-period">पुरापाषाण काल (Paleolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 2.6 MYA – 10,000 BCE</div>', '<div class="timeline-date">लगभग 2.6 MYA – 10,000 BCE</div>')
paleo_details_en = """                            <strong>Old Stone Age:</strong> Longest prehistoric phase (99% of human history).<br>
                            &bull; <strong>Tools:</strong> Hand-axes, cleavers, choppers (crude/heavy). Made of Quartzite.<br>
                            &bull; <strong>Livelihood:</strong> Hunting-gathering, nomadic, caves/shelters. Fire discovered.<br>
                            &bull; <strong>Key Sites:</strong> Soan Valley (Pakistan), Attirampakkam (TN), Bhimbetka (MP)."""
paleo_details_hi = """                            <strong>पुरापाषाण काल (Old Stone Age):</strong> सबसे लंबी प्रागैतिहासिक अवधि (मानव इतिहास का 99%)।<br>
                            &bull; <strong>उपकरण:</strong> हस्त-कुठार (Hand-axes), विदारणी (Cleavers), गंडासा (Choppers) (कच्चे/भारी)। ये मुख्यतः क्वार्ट्जाइट पत्थर से बने थे, इसलिए आदिमानव को 'क्वार्ट्जाइट मैन' भी कहा जाता था।<br>
                            &bull; <strong>जीवनशैली:</strong> शिकारी-संग्रहकर्ता, खानाबदोश, गुफाओं और चट्टानी आश्रयों में निवास। आग की खोज हुई।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> सोअन घाटी (पाकिस्तान), अतिरामपक्कम (तमिलनाडु), भीमबेटका (मध्य प्रदेश)।"""
html = html.replace(paleo_details_en, paleo_details_hi)

# Timeline Cards - Mesolithic
html = html.replace('<div class="timeline-period">Mesolithic Age</div>', '<div class="timeline-period">मध्यपाषाण काल (Mesolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 10,000 – 8,000 BCE</div>', '<div class="timeline-date">लगभग 10,000 – 8,000 BCE</div>')
meso_details_en = """                            <strong>Middle Stone Age:</strong> Transitional period marking climate warming (Holocene).<br>
                            &bull; <strong>Tools:</strong> Microliths (1-5 cm tiny geometric blades).<br>
                            &bull; <strong>Livelihood:</strong> Incipient domestication of animals begins, fishing, rock art.<br>
                            &bull; <strong>Key Sites:</strong> Bagor (Rajasthan), Adamgarh (MP), Langhnaj (Gujarat)."""
meso_details_hi = """                            <strong>मध्यपाषाण काल (Middle Stone Age):</strong> संक्रमण काल जो जलवायु के गर्म होने (होलोसीन युग) को दर्शाता है।<br>
                            &bull; <strong>उपकरण:</strong> माइक्रोलिथ (1-5 सेमी के छोटे ज्यामितीय ब्लेड, त्रिकोण, अर्धचंद्र)।<br>
                            &bull; <strong>जीवनशैली:</strong> पशुपालन की शुरुआत, शिकार, मछली पकड़ना, शैल चित्र (rock art) का विकास।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> बागोर (राजस्थान - सबसे बड़ा मेसोलिथिक स्थल), अदमगढ़ (मध्य प्रदेश - पशुपालन के सबसे पुराने साक्ष्य), लघनाज (गुजरात)।"""
html = html.replace(meso_details_en, meso_details_hi)

# Timeline Cards - Neolithic
html = html.replace('<div class="timeline-period">Neolithic Age</div>', '<div class="timeline-period">नवपाषाण काल (Neolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 8,000 – 2,000 BCE</div>', '<div class="timeline-date">लगभग 8,000 – 2,000 BCE</div>')
neo_details_en = """                            <strong>Neolithic Revolution:</strong> Shift from food-gathering to food-producing.<br>
                            &bull; <strong>Tools:</strong> Polished stone tools, ground axes, celts.<br>
                            &bull; <strong>Livelihood:</strong> Agriculture (wheat, barley, rice), settled village life, wheel-made pottery.<br>
                            &bull; <strong>Key Sites:</strong> Mehrgarh (Balochistan), Burzahom (J&K), Koldihwa (UP)."""
neo_details_hi = """                            <strong>नवपाषाण क्रांति (Neolithic Revolution):</strong> भोजन-संग्रहक से भोजन-उत्पादक (कृषि) बनने का युग।<br>
                            &bull; <strong>उपकरण:</strong> पॉलिशदार पत्थर के उपकरण, घिसे हुए सेल्ट (Celts) और कुल्हाड़ियाँ।<br>
                            &bull; <strong>जीवनशैली:</strong> व्यवस्थित ग्राम जीवन, कृषि (गेहूं, जौ, धान), चाक पर बने मिट्टी के बर्तन, पहिये का आविष्कार।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> मेहरगढ़ (बलूचिस्तान - प्राचीनतम कृषि साक्ष्य), बुर्जहोम (कश्मीर - गर्त-आवास या pit-dwellings और मालिक के साथ कुत्ता दफनाने की प्रथा), कोलडिहवा (उत्तर प्रदेश - प्राचीनतम चावल)।"""
html = html.replace(neo_details_en, neo_details_hi)

# Timeline Cards - Chalcolithic
html = html.replace('<div class="timeline-period">Chalcolithic Age</div>', '<div class="timeline-period">ताम्रपाषाण काल (Chalcolithic Age)</div>')
html = html.replace('<div class="timeline-date">c. 2,000 – 1,500 BCE</div>', '<div class="timeline-date">लगभग 2,000 – 1,500 BCE</div>')
chalco_details_en = """                            <strong>Copper-Stone Age:</strong> First use of metals (copper) alongside stone tools.<br>
                            &bull; <strong>Pottery:</strong> Black & Red Ware (BRW) pottery.<br>
                            &bull; <strong>Livelihood:</strong> Agricultural village economies (non-urban, non-Harappan).<br>
                            &bull; <strong>Key Sites:</strong> Inamgaon & Daimabad (Maharashtra), Ahar (Rajasthan)."""
chalco_details_hi = """                            <strong>ताम्र-पाषाण युग (Copper-Stone Age):</strong> पत्थर के साथ-साथ धातु (तांबा) का पहला प्रयोग।<br>
                            &bull; <strong>मृदभांड:</strong> काले और लाल मृदभांड (Black and Red Ware - BRW)।<br>
                            &bull; <strong>जीवनशैली:</strong> कृषि ग्रामीण संस्कृतियाँ (गैर-शहरी)।<br>
                            &bull; <strong>प्रमुख स्थल:</strong> जोरवे संस्कृति (इनामगांव और दैमाबाद, महाराष्ट्र), आहार-बनास संस्कृति (आहार और गिलुंड, राजस्थान)।"""
html = html.replace(chalco_details_en, chalco_details_hi)

# Timeline Cards - Iron Age
html = html.replace('<div class="timeline-period">Iron Age</div>', '<div class="timeline-period">लौह युग (Iron Age)</div>')
html = html.replace('<div class="timeline-date">c. 1,500 BCE onward</div>', '<div class="timeline-date">लगभग 1,500 BCE से आगे</div>')
iron_details_en = """                            <strong>Early Iron Age:</strong> Use of iron tools leading to agricultural surplus.<br>
                            &bull; <strong>Burials:</strong> Megaliths (dolmens, menhirs) in South India.<br>
                            &bull; <strong>Pottery:</strong> Painted Grey Ware (PGW) and NBPW.<br>
                            &bull; <strong>Impact:</strong> Laid base for Second Urbanisation (600 BCE)."""
iron_details_hi = """                            <strong>प्रारंभिक लौह युग:</strong> लोहे के औजारों का उपयोग जिससे कृषि अधिशेष और आर्थिक विकास हुआ।<br>
                            &bull; <strong>समाधियाँ:</strong> दक्षिण भारत में महापाषाण (Megaliths - डोलमेंस, मेनहिर) समाधियाँ।<br>
                            &bull; <strong>मृदभांड:</strong> चित्रित धूसर मृदभांड (PGW) और उत्तरी काले चमकीले मृदभांड (NBPW)।<br>
                            &bull; <strong>प्रभाव:</strong> गंगा घाटी में द्वितीय नगरीकरण (600 BCE - महाजनपद काल) का मार्ग प्रशस्त हुआ।"""
html = html.replace(iron_details_en, iron_details_hi)

# Mnemonics & Memory Hacks
html = html.replace('<h2 class="card-title"><i class="fas fa-lightbulb"></i> Mnemonics & Memory Palace Hooks</h2>', '<h2 class="card-title"><i class="fas fa-lightbulb"></i> स्मृति सहायक सूत्र (Mnemonics & Memory Hooks)</h2>')
html = html.replace('<p>Use these structured mnemonic associations to remember sequence, tools, and sites forever.</p>', '<p>कालक्रम, खोजों और प्रमुख स्थलों को हमेशा के लिए याद रखने के लिए इन तीन स्मृति सूत्रों का उपयोग करें।</p>')
html = html.replace('<div class="mnemonic-title">Mnemonic 1: Chronological Sequence</div>', '<div class="mnemonic-title">स्मृति सूत्र 1: कालानुक्रमिक क्रम</div>')
html = html.replace('<div class="mnemonic-phrase">"People Make New Copper Instruments"</div>', '<div class="mnemonic-phrase">"People Make New Copper Instruments"</div>')
html = html.replace('<strong>P</strong>eople (<strong>P</strong>aleolithic) &rarr;\n                        <strong>M</strong>ake (<strong>M</strong>esolithic) &rarr;\n                        <strong>N</strong>ew (<strong>N</strong>eolithic) &rarr;\n                        <strong>C</strong>opper (<strong>C</strong>halcolithic) &rarr;\n                        <strong>I</strong>nstruments (<strong>I</strong>ron Age)', '<strong>P</strong>eople (<strong>P</strong>aleolithic - पुरापाषाण) &rarr;\n                        <strong>M</strong>ake (<strong>M</strong>esolithic - मध्यपाषाण) &rarr;\n                        <strong>N</strong>ew (<strong>N</strong>eolithic - नवपाषाण) &rarr;\n                        <strong>C</strong>opper (<strong>C</strong>halcolithic - ताम्रपाषाण) &rarr;\n                        <strong>I</strong>nstruments (<strong>I</strong>ron Age - लौह युग)')

html = html.replace('<div class="mnemonic-title">Mnemonic 2: Earliest Domestication and Sites</div>', '<div class="mnemonic-title">स्मृति सूत्र 2: पशुपालन की शुरुआत और प्रमुख स्थल</div>')
html = html.replace('<div class="mnemonic-phrase">"Adam Domestication, Bagor Biggest"</div>', '<div class="mnemonic-phrase">"Adam Domestication, Bagor Biggest"</div>')
html = html.replace('&bull; <strong>Adam</strong>garh (MP) &rarr; Earliest evidence of animal <strong>Domestication</strong>.<br>\n                        &bull; <strong>Bagor</strong> (Rajasthan) &rarr; <strong>Biggest</strong> (Largest) Mesolithic site in India.', '&bull; <strong>Adam</strong>garh (मप्र) &rarr; पशु <strong>Domestication (पालन)</strong> के सबसे पहले साक्ष्य।<br>\n                        &bull; <strong>Bagor</strong> (राजस्थान) &rarr; भारत का सबसे बड़ा <strong>Biggest (विशालतम)</strong> मध्यपाषाण कालीन स्थल।')

html = html.replace('<div class="mnemonic-title">Mnemonic 3: Neolithic Major Discoveries</div>', '<div class="mnemonic-title">स्मृति सूत्र 3: नवपाषाण कालीन प्रमुख खोजें/स्थल</div>')
html = html.replace('<div class="mnemonic-phrase">"My Best Goat Keeps Chewing Rice"</div>', '<div class="mnemonic-phrase">"My Best Goat Keeps Chewing Rice"</div>')
html = html.replace('&bull; <strong>M</strong>y (<strong>M</strong>ehrgarh &rarr; Earliest agriculture, Balochistan)<br>\n                        &bull; <strong>B</strong>est (<strong>B</strong>urzahom &rarr; Pit-dwellings & Dog burials, J&K)<br>\n                        &bull; <strong>G</strong>oat (<strong>G</strong>ufkral &rarr; Pit-dwellings & Pastoralism, J&K)<br>\n                        &bull; <strong>K</strong>eeps (<strong>K</strong>oldihwa &rarr; Earliest rice evidence, UP)<br>\n                        &bull; <strong>C</strong>hewing (<strong>C</strong>hirand &rarr; Bone tools, Bihar)', '&bull; <strong>M</strong>y (<strong>M</strong>ehrgarh &rarr; प्राचीनतम कृषि, बलूचिस्तान)<br>\n                        &bull; <strong>B</strong>est (<strong>B</strong>urzahom &rarr; गर्त-आवास (Pit-dwellings) और कुत्ता दफनाने की प्रथा, जम्मू-कश्मीर)<br>\n                        &bull; <strong>G</strong>oat (<strong>G</strong>ufkral &rarr; गर्त-आवास और पशुपालन, जम्मू-कश्मीर)<br>\n                        &bull; <strong>K</strong>eeps (<strong>K</strong>oldihwa &rarr; प्राचीनतम चावल के साक्ष्य, उत्तर प्रदेश)<br>\n                        &bull; <strong>C</strong>hewing (<strong>C</strong>hirand &rarr; हिरण के सींग से बने हड्डी के औजार, बिहार)')

# Evolution of Prehistoric Tool Typology
html = html.replace('<h2 class="card-title"><i class="fas fa-hammer"></i> Evolution of Prehistoric Tool Typology</h2>', '<h2 class="card-title"><i class="fas fa-hammer"></i> प्रागैतिहासिक उपकरणों के प्रकारों का विकास</h2>')
html = html.replace('<p>Observe the progressive reduction in tool size and increase in technological precision over time:</p>', '<p>समय के साथ उपकरण के आकार में कमी और तकनीकी सटीकता में वृद्धि का विश्लेषण करें:</p>')
html = html.replace('<strong style="color: #8e44ad;">Paleolithic</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Crude Bifaces, Handaxes, Choppers (Quartzite)</p>', '<strong style="color: #8e44ad;">पुरापाषाण (Paleolithic)</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">कच्चे हस्त-कुठार, गंडासा (क्वार्ट्जाइट पत्थर)</p>')
html = html.replace('<strong style="color: #2980b9;">Mesolithic</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Microliths (1-5 cm tiny Lunates, Triangles)</p>', '<strong style="color: #2980b9;">मध्यपाषाण (Mesolithic)</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">माइक्रोलिथ (1-5 सेमी के छोटे ब्लेड, त्रिकोण, अर्धचंद्र)</p>')
html = html.replace('<strong style="color: #27ae60;">Neolithic</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Polished Celts, Polished Ground Axes</p>', '<strong style="color: #27ae60;">नवपाषाण (Neolithic)</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">पॉलिशदार पत्थर के उपकरण, घिसे हुए सेल्ट और कुल्हाड़ियाँ</p>')
html = html.replace('<strong style="color: #f39c12;">Chalcolithic</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">Copper Axes, Bronze chisels alongside chert flakes</p>', '<strong style="color: #f39c12;">ताम्रपाषाण (Chalcolithic)</strong>\n                        <p style="font-size: 0.78rem; color: var(--text-light); margin-top: 0.25rem;">तांबे की कुल्हाड़ियाँ और कांस्य छैनी, पत्थर के साथ</p>')

# Common Traps
html = html.replace('<h2 class="card-title" style="color: #e74c3c;"><i class="fas fa-triangle-exclamation"></i> UPSC Common Exam Traps</h2>', '<h2 class="card-title" style="color: #e74c3c;"><i class="fas fa-triangle-exclamation"></i> UPSC सामान्य परीक्षा ट्रैप (भ्रम)</h2>')
html = html.replace('<strong>Trap 1: Domestication vs. Agriculture:</strong> Domestication of animals began in the <em>Mesolithic</em> period (earliest evidence: Adamgarh & Bagor). Agriculture, however, became a mainstream practice only during the <em>Neolithic</em> period. Do not confuse the two!', '<strong>भ्रम 1: पशुपालन बनाम कृषि:</strong> मवेशियों/पशुओं का पालन <em>मध्यपाषाण (Mesolithic)</em> काल में शुरू हुआ (सबसे पुराना साक्ष्य: अदमगढ़ और बागोर)। जबकि कृषि का विकास मुख्य रूप से <em>नवपाषाण (Neolithic)</em> काल में भोजन-उत्पादन क्रांति के रूप में हुआ।')
html = html.replace('<strong>Trap 2: Megaliths Geography:</strong> Although Megaliths (large stone graves) are widely associated with South Indian Iron Age cultures, they are also found in Central India, Maharashtra, and Kashmir (e.g. Burzahom).', '<strong>भ्रम 2: महापाषाण (Megaliths) का भूगोल:</strong> यद्यपि महापाषाण समाधियां मुख्य रूप से दक्षिण भारत के लौह युग से जुड़ी हैं, वे मध्य भारत, महाराष्ट्र और कश्मीर (जैसे बुर्जहोम) में भी पाई गई हैं।')
html = html.replace('<strong>Trap 3: Harappan overlap:</strong> Most Chalcolithic cultures (Jorwe, Malwa, Banas) were rural, farming villages and flourished <em>after</em> or during the decline of the urban Indus Valley Civilization (post-2000 BCE). They were not precursors to Harappa, except Kot Diji or Amri.', '<strong>भ्रम 3: हड़प्पा ओवरलैप:</strong> अधिकांश ताम्रपाषाण कालीन संस्कृतियां (जोरवे, मालवा, बनास) ग्रामीण बस्तियां थीं और शहरी सिंधु घाटी सभ्यता के पतन के <em>बाद</em> या उसके अंतिम चरण में (2000 ईपू के बाद) विकसित हुईं। ये हड़प्पा से पहले की संस्कृतियां नहीं थीं (कोट दीजी या आमरी को छोड़कर)।')

# Practice Zone text
html = html.replace('<h2 class="card-title"><i class="fas fa-list-check"></i> Practice Zone: 50 Questions</h2>', '<h2 class="card-title"><i class="fas fa-list-check"></i> अभ्यास क्षेत्र: 50 प्रश्न</h2>')
html = html.replace('<p>Click on the options to check your answer instantly. Click "Show Explanation" to read step-by-step solutions.</p>', '<p>उत्तरों की तुरंत जांच करने के लिए विकल्पों पर क्लिक करें। विस्तृत समाधान पढ़ने के लिए "व्याख्या देखें" पर क्लिक करें।</p>')
html = html.replace('Show Explanation', 'व्याख्या देखें')
html = html.replace('<strong>Explanation:</strong>', '<strong>व्याख्या:</strong>')

# Test Zone text
html = html.replace('<h2>UPSC-Style Prehistory Mock Test</h2>', '<h2>UPSC शैली प्रागैतिहासिक मॉक टेस्ट</h2>')
html = html.replace('<p style="color: var(--text-light); margin: 0.5rem 0 1.5rem;">Contains 10 multi-statement questions testing conceptual understanding and site locations. 1/3 negative marking applies.</p>', '<p style="color: var(--text-light); margin: 0.5rem 0 1.5rem;">अवधारणात्मक समझ और स्थलों की स्थिति का परीक्षण करने वाले 10 बहु-कथनीय प्रश्न शामिल हैं। 1/3 नकारात्मक अंकन प्रणाली लागू है।</p>')
html = html.replace('<button class="btn-action btn-next" onclick="startTest()">Start Live Test</button>', '<button class="btn-action btn-next" onclick="startTest()">लाइव टेस्ट शुरू करें</button>')
html = html.replace('Time: 00:00', 'समय: 00:00')
html = html.replace('`Time: ${mins}:${secs}`', '`समय: ${mins}:${secs}`')
html = html.replace('`Question ${currentTestIdx + 1} of ${testQuestions.length}`', '`प्रश्न ${currentTestIdx + 1} of ${testQuestions.length}`')
html = html.replace('Question 1 of 10', 'प्रश्न 1 of 10')
html = html.replace("nextBtn.textContent = 'Submit Test';", "nextBtn.textContent = 'टेस्ट जमा करें';")
html = html.replace("nextBtn.textContent = 'Next';", "nextBtn.textContent = 'आगे बढ़ें';")
html = html.replace("Previous", "पीछे जाएं")

# Test results panel
html = html.replace('<h2 style="font-family: \'Outfit\', sans-serif; margin-bottom: 0.5rem;">Test Complete!</h2>', '<h2 style="font-family: \'Outfit\', sans-serif; margin-bottom: 0.5rem;">टेस्ट समाप्त!</h2>')
html = html.replace('<button class="btn-action btn-next" onclick="restartTest()">Restart Test</button>', '<button class="btn-action btn-next" onclick="restartTest()">टेस्ट दोबारा शुरू करें</button>')
html = html.replace('<h3 style="border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem; margin-bottom: 1rem;"><i class="fas fa-square-poll-vertical"></i> Question Review</h3>', '<h3 style="border-bottom: 2px solid #d4af37; padding-bottom: 0.5rem; margin-bottom: 1rem;"><i class="fas fa-square-poll-vertical"></i> प्रश्नों की समीक्षा</h3>')

# Result review rendering JS
review_item_html_en = """                    <div class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                        ${isCorrect ? '<i class="fas fa-check"></i> Correct' : '<i class="fas fa-xmark"></i> Incorrect / Unanswered'}
                    </div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem;">Q${idx + 1}. ${q.q.replace(/\\n/g, '<br>')}</div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Your Answer:</strong> ${userAnswers[idx] !== null ? q.opts[userAnswers[idx]] : '<span style="color:#e74c3c">Not Answered</span>'}
                    </div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>Correct Answer:</strong> ${q.opts[q.ans]}
                    </div>
                    <div style="background: rgba(0,0,0,0.02); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem; margin-top: 0.5rem;">
                        <strong>Explanation:</strong> ${q.sol}
                    </div>"""

review_item_html_hi = """                    <div class="review-badge ${isCorrect ? 'correct' : 'incorrect'}">
                        ${isCorrect ? '<i class="fas fa-check"></i> सही' : '<i class="fas fa-xmark"></i> गलत / अनुत्तरित'}
                    </div>
                    <div style="font-weight: 600; margin-bottom: 0.5rem;">Q${idx + 1}. ${q.q.replace(/\\n/g, '<br>')}</div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>आपका उत्तर:</strong> ${userAnswers[idx] !== null ? q.opts[userAnswers[idx]] : '<span style="color:#e74c3c">अनुत्तरित</span>'}
                    </div>
                    <div style="font-size: 0.88rem; margin-bottom: 0.4rem;">
                        <strong>सही उत्तर:</strong> ${q.opts[q.ans]}
                    </div>
                    <div style="background: rgba(0,0,0,0.02); padding: 0.75rem; border-radius: 6px; font-size: 0.85rem; margin-top: 0.5rem;">
                        <strong>व्याख्या:</strong> ${q.sol}
                    </div>"""

html = html.replace(review_item_html_en, review_item_html_hi)

# Summary text logic
html = html.replace("document.getElementById('resultSummaryText').textContent = `You answered ${correctCount} questions correctly out of ${testQuestions.length} in ${Math.floor(testSeconds / 60)} minutes and ${testSeconds % 60} seconds.`;", "const incorrectCount = testQuestions.length - correctCount - userAnswers.filter(a => a === null).length; const totalScore = (correctCount * 2) - (incorrectCount * (2/3)); document.getElementById('resultSummaryText').textContent = `आपने ${Math.floor(testSeconds / 60)} मिनट ${testSeconds % 60} सेकंड में ${correctCount} सही, ${incorrectCount} गलत और ${userAnswers.filter(a => a === null).length} अनुत्तरित प्रश्न किए। UPSC प्राप्तांक (UPSC Score): ${totalScore.toFixed(2)} / 20.00`;")

# Now translate the JS arrays: pQuestions and testQuestions
# We will define a python function or mapping to swap them out in the html string
# Let's read the pre-translated Hindi questions database
# (Translated from English to standard Hindi)
hi_pQuestions = [
    {
        "q": "किस भू-वैज्ञानिक ने 1863 में भारत में पहले पुरापाषाण कालीन पत्थर के उपकरण (हस्त-कुठार / handaxe) की खोज की थी?",
        "opts": ["रॉबर्ट ब्रूस फूट (Robert Bruce Foote)", "अलेक्जेंडर कनिंघम (Alexander Cunningham)", "एच.डी. सांकलिया (H.D. Sankalia)", "मोर्टिमर व्हीलर (Mortimer Wheeler)"],
        "ans": 0,
        "sol": "रॉबर्ट ब्रूस फूट ने मई 1863 में पल्लवरम (चेन्नई के पास) में भारत के पहले प्रागैतिहासिक उपकरण (एक एशुलेयिन हस्त-कुठार) की खोज की थी। उन्हें भारतीय प्रागैतिहास का जनक (Father of Indian Prehistory) कहा जाता है।"
    },
    {
        "q": "इतिहास में 'क्वार्ट्जाइट मैन' (Quartzite Man) शब्द भारत के किस प्रागैतिहासिक काल से जुड़ा है?",
        "opts": ["मध्यपाषाण काल (Mesolithic Period)", "पुरापाषाण काल (Paleolithic Period)", "नवपाषाण काल (Neolithic Period)", "ताम्रपाषाण काल (Chalcolithic Period)"],
        "ans": 1,
        "sol": "भारत में पुरापाषाण कालीन मानव अपने भारी पत्थर के औजार बनाने के लिए मुख्य रूप से क्वार्ट्जाइट (एक कठोर कायांतरित चट्टान) का उपयोग करते थे, जिससे पुरातत्वविदों ने उन्हें 'क्वार्ट्जाइट मैन' कहा।"
    },
    {
        "q": "निम्नलिखित में से भारत में उत्खनित सबसे बड़ा मध्यपाषाण कालीन (Mesolithic) स्थल कौन सा है?",
        "opts": ["अदमगढ़ (मप्र)", "बागोर (राजस्थान)", "लघनाज (गुजरात)", "सराय नाहर राय (उप्र)"],
        "ans": 1,
        "sol": "राजस्थान में कोठारी नदी पर स्थित बागोर भारत का सबसे बड़ा मध्यपाषाण कालीन स्थल है। यहाँ से भारी मात्रा में माइक्रोलिथ (सूक्ष्म पाषाण उपकरण) और पशुपालन के शुरुआती साक्ष्य मिले हैं।"
    },
    {
        "q": "निम्नलिखित में से किस मध्यपाषाण कालीन स्थल से हमें भारत में पशुपालन के सबसे पुराने साक्ष्य मिले हैं?",
        "opts": ["लघनाज (गुजरात)", "अदमगढ़ (मप्र)", "सराय नाहर राय (उप्र)", "बीरभानपुर (पश्चिम बंगाल)"],
        "ans": 1,
        "sol": "पशुपालन के सबसे पुराने साक्ष्य (लगभग 5000 ईपू) मध्य प्रदेश के अदमगढ़ और राजस्थान के बागोर से प्राप्त हुए हैं।"
    },
    {
        "q": "कौन सा प्रागैतिहासिक स्थल निम्न पुरापाषाण काल (Lower Paleolithic) से लेकर नवपाषाण काल (Neolithic) तक के निरंतर स्तरित अनुक्रम (stratographic sequence) के लिए प्रसिद्ध है?",
        "opts": ["सोअन घाटी (पाकिस्तान)", "भीमबेटका (मप्र)", "बेलन घाटी (उप्र)", "अतिरामपक्कम (तमिलनाडु)"],
        "ans": 2,
        "sol": "उत्तर प्रदेश में स्थित बेलन घाटी में पुरापाषाण, मध्यपाषाण से नवपाषाण काल तक के विकास को दर्शाने वाला एक निरंतर भू-पुरातात्विक स्तरित अनुक्रम मौजूद है।"
    },
    {
        "q": "खेती की ओर बदलाव (खाद्य उत्पादक बनने) को दर्शाने के लिए 'नवपाषाण क्रांति' (Neolithic Revolution) शब्द किसने गढ़ा था?",
        "opts": ["वी. गॉर्डन चाइल्ड (V. Gordon Childe)", "जॉन लुबॉक (John Lubbock)", "मोर्टिमर व्हीलर (Mortimer Wheeler)", "रॉबर्ट ब्रूस फूट (Robert Bruce Foote)"],
        "ans": 0,
        "sol": "वी. गॉर्डन चाइल्ड ने 1936 में 'नवपाषाण क्रांति' शब्द गढ़ा था ताकि उस गहन सामाजिक-आर्थिक बदलाव को रेखांकित किया जा सके जब मानव खाद्य-संग्रहक से खाद्य-उत्पादक (कृषि और पशुपालन) की ओर बढ़ा।"
    },
    {
        "q": "मेहरगढ़, भारतीय उपमहाद्वीप में सबसे पुराना नवपाषाण कालीन कृषि स्थल, किस नदी के तट पर स्थित है?",
        "opts": ["सिंधु नदी", "सोअन नदी", "बोलन नदी", "घग्गर नदी"],
        "ans": 2,
        "sol": "मेहरगढ़ बलूचिस्तान (पाकिस्तान) में बोलन दर्रे के पास, बोलन नदी के तट पर स्थित है। यह स्थल लगभग 7000 ईपू का है।"
    },
    {
        "q": "गर्त-आवास (pit-dwellings) और कब्रों में इंसानी कंकालों के साथ पालतू कुत्तों को दफनाने की प्रथा किस नवपाषाण स्थल की अनूठी विशेषताएँ हैं?",
        "opts": ["मेहरगढ़", "बुर्जहोम", "गुफक्राल", "चिरण्ड"],
        "ans": 1,
        "sol": "जम्मू-कश्मीर में स्थित बुर्जहोम (जिसका अर्थ 'भूर्ज वृक्ष का स्थान' है) अपने भूमिगत गर्त-आवासों और कब्रों में स्वामियों के साथ उनके पालतू कुत्तों को दफनाने की अनूठी प्रथा के लिए प्रसिद्ध है।"
    },
    {
        "q": "गंगा के मैदानों पर स्थित किस नवपाषाण कालीन स्थल से हिरण के सींगों (antlers) से बने बड़ी संख्या में हड्डी के उपकरण मिले हैं?",
        "opts": ["कोलडिहवा", "चिरण्ड", "महागरा", "सेनुआर"],
        "ans": 1,
        "sol": "चिरण्ड (सारण जिला, बिहार) गंगा नदी के उत्तरी तट पर स्थित एक प्रमुख नवपाषाण स्थल है, जो हिरण के सींगों से बने हड्डी के औजारों के व्यापक संग्रह के लिए जाना जाता है।"
    },
    {
        "q": "किस नवपाषाण स्थल से दुनिया में धान (चावल) की खेती के सबसे पुराने साक्ष्य (लगभग 6000 ईपू) मिले हैं?",
        "opts": ["मेहरगढ़ (बलूचिस्तान)", "कोलडिहवा (उप्र)", "चिरण्ड (बिहार)", "हल्लूर (कर्नाटक)"],
        "ans": 1,
        "sol": "बेलन घाटी (उत्तर प्रदेश) में स्थित कोलडिहवा से मिट्टी के बर्तनों के गारे में लिपटे धान की भूसी के सबसे पुराने साक्ष्य मिले हैं, जो लगभग 6000 ईपू के हैं।"
    },
    {
        "q": "भारतीय उपमहाद्वीप में मानव द्वारा प्रयोग की जाने वाली पहली धातु कौन सी थी?",
        "opts": ["लोहा", "कांसा", "तांबा", "सोना"],
        "ans": 2,
        "sol": "ताम्रपाषाण (तांबा-पत्थर) काल के दौरान प्रागैतिहासिक मानव द्वारा सबसे पहले तांबे (Copper) को गलाकर उपयोग में लाया गया था।"
    },
    {
        "q": "दैमाबाद से प्राप्त प्रसिद्ध कांस्य मूर्तियाँ (जिसमें रथ, हाथी, और गेंडा शामिल हैं) किस सांस्कृतिक चरण से संबंधित हैं?",
        "opts": ["नवपाषाण काल", "जोरवे ताम्रपाषाण संस्कृति", "लौह युग पीजीडब्ल्यू संस्कृति", "मध्यपाषाण काल"],
        "ans": 1,
        "sol": "महाराष्ट्र के दैमाबाद से कांसे की चार मूर्तियां (मनुष्य द्वारा चलाया जाने वाला रथ, हाथी, गेंडा और भैंसा) मिली हैं, जो जोरवे/देर-हड़प्पा ताम्रपाषाण कालीन चरण से संबंधित हैं।"
    },
    {
        "q": "भारत में सबसे व्यापक रूप से उत्खनित ताम्रपाषाण कालीन (Chalcolithic) स्थल कौन सा है?",
        "opts": ["नवदाटोली", "इनामगांव", "कायथा", "आहार"],
        "ans": 1,
        "sol": "महाराष्ट्र में स्थित इनामगांव (जोरवे संस्कृति का स्थल) भारत में सबसे व्यापक और व्यवस्थित रूप से उत्खनित ताम्रपाषाण कालीन स्थल है, जिसका उत्खनन एच.डी. सांकलिया और अन्यों द्वारा किया गया था।"
    },
    {
        "q": "कौन सी ताम्रपाषाण कालीन संस्कृति सफेद रंग से चित्रित अपने विशिष्ट काले और लाल मृदभांड (Black and Red Ware) के लिए जानी जाती है?",
        "opts": ["जोरवे संस्कृति", "आहार-बनास संस्कृति", "मालवा संस्कृति", "कायथा संस्कृति"],
        "ans": 1,
        "sol": "राजस्थान की आहार-बनास संस्कृति की मुख्य विशेषता सफेद रंग से चित्रित काले और लाल मृदभांड (BRW) हैं। आहार को तांबे की प्रचुरता के कारण 'ताम्बवती' भी कहा जाता था।"
    },
    {
        "q": "किस प्रकार की महापाषाण (Megalithic) समाधि में खड़े पत्थरों के स्लैब के ऊपर एक आड़ा स्लैब मेज की तरह रखा जाता है?",
        "opts": ["मेनहिर (Menhir)", "डोलमेन (Dolmen)", "शिलावृत्त (Stone Circle)", "केर्न वृत्त (Cairn Circle)"],
        "ans": 1,
        "sol": "डोलमेन (Dolmen) एक महापाषाण समाधि है जिसमें दो या दो से अधिक खड़े पत्थरों के ऊपर एक बड़ा चपटा आड़ा पत्थर टिकाया जाता है।"
    },
    {
        "q": "उत्तर प्रदेश के किस स्थल से भारत में लौह प्रगलन (iron smelting) के प्राचीनतम साक्ष्य (लगभग 1800 ईपू) मिले हैं?",
        "opts": ["अतरंजीखेड़ा", "मल्हार", "हस्तिनापुर", "जखेड़ा"],
        "ans": 1,
        "sol": "उत्तर प्रदेश के चंदौली जिले में मल्हार नामक स्थल के उत्खनन से लोहे के प्रयोग की प्राचीनता लगभग 1800 ईपू तक चली जाती है, जो मध्य गंगा के मैदानों में स्वतंत्र लौह तकनीक के विकास को दर्शाती है।"
    },
    {
        "q": "चित्रित धूसर मृदभांड (PGW) पॉटरी मुख्य रूप से किस काल से जुड़ी है?",
        "opts": ["सिंधु घाटी सभ्यता", "प्रारंभिक लौह युग / उत्तर वैदिक काल", "मध्यपाषाण काल", "मौर्य काल"],
        "ans": 1,
        "sol": "चित्रित धूसर मृदभांड (PGW) एक महीन धूसर पॉटरी है जिस पर काले ज्यामितीय चित्र बने होते हैं। यह लगभग 1100 से 600 ईपू की है, जो वैदिक ग्रंथों में वर्णित लौह युगीन स्थलों (जैसे हस्तिनापुर) से जुड़ी है।"
    },
    {
        "q": "दक्षिण भारत के राख के टीले (Ash Mounds - जैसे उतनूर और कुपगल) किस प्रागैतिहासिक काल से संबंधित हैं?",
        "opts": ["उच्च पुरापाषाण काल", "मध्यपाषाण काल", "नवपाषाण पशुपालक चरण", "ताम्रपाषाण काल"],
        "ans": 2,
        "sol": "कर्नाटक और आंध्र प्रदेश में पाए जाने वाले राख के टीले मवेशियों के बाड़ों में जमा गोबर को समय-समय पर जलाने से बने थे, जो दक्षिण भारत में नवपाषाण समुदायों की पशुपालन गतिविधियों को साबित करते हैं।"
    },
    {
        "q": "किस स्थल से भारत में सबसे प्राचीन एशुलेयिन (Acheulian) हस्त-कुठार मिले हैं, जो लगभग 15 लाख वर्ष पुराने हैं?",
        "opts": ["सोअन घाटी (पाकिस्तान)", "अतिरामपक्कम (तमिलनाडु)", "भीमबेटका (मप्र)", "हुंसगी (कर्नाटक)"],
        "ans": 1,
        "sol": "तमिलनाडु के अतिरामपक्कम को कॉस्मोस न्यूक्लाइड बरियल डेटिंग से लगभग 15 लाख वर्ष पुराना आंका गया है, जो अफ्रीका से बाहर सबसे पुराने हस्त-कुठार परंपराओं में से एक है।"
    },
    {
        "q": "भारत में शुतुरमुर्ग के अंडों के छिलकों के मनके और नक्काशीदार टुकड़े किस प्रागैतिहासिक चरण में खोजे गए हैं?",
        "opts": ["निम्न पुरापाषाण काल", "मध्य पुरापाषाण काल", "उच्च पुरापाषाण काल", "नवपाषाण काल"],
        "ans": 2,
        "sol": "महाराष्ट्र के पाटने (Patne) जैसे उच्च पुरापाषाण कालीन स्थलों से शुतुरमुर्ग के अंडों के छिलकों के अलंकृत टुकड़े और मनके मिले हैं, जो होमो सेपियंस की प्रारंभिक कलात्मक क्षमताओं को दर्शाते हैं।"
    },
    {
        "q": "कश्मीर के किस स्थल से नवपाषाण कालीन गर्त-आवास, हड्डी के हार्पून और पॉलिशदार पत्थर की कुल्हाड़ियाँ मिली हैं?",
        "opts": ["मेहरगढ़", "गुफक्राल", "चिरण्ड", "बुर्जहोम"],
        "ans": 3,
        "sol": "बुर्जहोम कश्मीर का मुख्य नवपाषाण स्थल है, जहाँ सर्दियों से बचने के लिए गर्त-आवासों का निर्माण, हड्डी के औजार और विशिष्ट दफन प्रथाएँ पाई जाती थीं।"
    },
    {
        "q": "कांस्य मूर्तियों के लिए प्रसिद्ध दैमाबाद किस ताम्रपाषाण कालीन संस्कृति के अंतर्गत आता है?",
        "opts": ["मालवा संस्कृति", "जोरवे संस्कृति", "कायथा संस्कृति", "बनास संस्कृति"],
        "ans": 1,
        "sol": "दैमाबाद महाराष्ट्र के अहमदनगर जिले में प्रवरा नदी के तट पर स्थित जोरवे संस्कृति का एक प्रमुख स्थल है।"
    },
    {
        "q": "भारत में मध्य और उच्च पुरापाषाण काल में उपकरण निर्माण के लिए मुख्य रूप से किस सामग्री का उपयोग किया जाता था?",
        "opts": ["चर्ट और जैस्पर", "क्वार्ट्जाइट", "फ्लिंट (चकमक पत्थर)", "तांबा"],
        "ans": 0,
        "sol": "मध्य और उच्च पुरापाषाण काल में मानव क्वार्ट्जाइट के स्थान पर बारीक कणों वाले सिलिका-युक्त पत्थरों जैसे चर्ट, जैस्पर, कैल्सेडोनी और अकीक का उपयोग करने लगा था।"
    },
    {
        "q": "प्लीस्टोसीन (हिमयुग) से होलोसीन (गर्म और आर्द्र) भू-वैज्ञानिक युग में परिवर्तन किस प्रागैतिहासिक काल से मेल खाता है?",
        "opts": ["पुरापाषाण काल", "मध्यपाषाण काल", "नवपाषाण काल", "लौह युग"],
        "ans": 1,
        "sol": "मध्यपाषाण काल की शुरुआत लगभग 10,000 ईपू में होलोसीन युग के प्रारंभ से होती है। गर्म जलवायु के कारण वनस्पतियों और जीवों का विकास हुआ, जिससे सूक्ष्म उपकरणों (माइक्रोलिथ) का उपयोग शुरू हुआ।"
    },
    {
        "q": "राजस्थान की बनास घाटी में तांबा गलाने के सबसे पुराने साक्ष्य किस ताम्रपाषाण कालीन स्थल से मिले हैं?",
        "opts": ["गिलुंड", "आहार", "कायथा", "एरन"],
        "ans": 1,
        "sol": "आहार (प्राचीन नाम ताम्बवती यानी तांबे का स्थान) आहार-बनास संस्कृति का प्रमुख स्थल है, जहाँ तांबा गलाने के अवशेष और भट्टियाँ मिली हैं।"
    },
    {
        "q": "असम के किस नवपाषाण स्थल से कंधे वाली कुल्हाड़ियाँ (shouldered axes) और रस्सी की छाप वाले मृदभांड (cord-impressed pottery) मिले हैं?",
        "opts": ["कुचाई", "दोजाली हडिंग", "सरुतरु", "चिरण्ड"],
        "ans": 1,
        "sol": "असम की उत्तर कछार पहाड़ियों में स्थित दोजाली हडिंग से कंधे वाली कुल्हाड़ियाँ, जीवाश्म लकड़ी के औजार और रस्सी की छाप वाले मिट्टी के बर्तन मिले हैं, जो दक्षिण-पूर्व एशिया से संबंध दर्शाते हैं।"
    },
    {
        "q": "मानव इतिहास में दांतों में ड्रिलिंग/छेद करने का सबसे पुराना साक्ष्य (लगभग 7000 ईपू) किस नवपाषाण स्थल से प्राप्त हुआ है?",
        "opts": ["बुर्जहोम", "मेहरगढ़", "गुफक्राल", "इनामगांव"],
        "ans": 1,
        "sol": "मेहरगढ़ से नौ ऐसे मानव कंकाल मिले हैं जिनके दांतों में सूक्ष्म चकमक पत्थर (flint) के यंत्रों से छेद किए जाने के साक्ष्य मिले हैं, जो दंत चिकित्सा के इतिहास का प्राचीनतम उदाहरण है।"
    },
    {
        "q": "द्वितीय नगरीकरण (लगभग 600 ईपू) के समृद्ध नगरों से कौन सी मृदभांड परंपरा जुड़ी हुई है?",
        "opts": ["गेरूए रंग के मृदभांड (OCP)", "चित्रित धूसर मृदभांड (PGW)", "उत्तरी काले चमकीले मृदभांड (NBPW)", "काले और लाल मृदभांड (BRW)"],
        "ans": 2,
        "sol": "उत्तरी काले चमकीले मृदभांड (NBPW) एक अत्यंत चमकदार, दर्पण जैसी पॉलिश वाली ब्लैक स्लिप्ड पॉटरी है जो महाजनपदों और नगरीकरण के उदय से जुड़ी है।"
    },
    {
        "q": "उत्तर प्रदेश का सराय नाहर राय ऐतिहासिक रूप से किस प्रागैतिहासिक काल से जुड़ा है?",
        "opts": ["निम्न पुरापाषाण काल", "मध्य पुरापाषाण काल", "मध्यपाषाण काल", "नवपाषाण काल"],
        "ans": 2,
        "sol": "सराय नाहर राय (प्रतापगढ़, उप्र) एक मध्यपाषाण कालीन स्थल है जहाँ से माइक्रोलिथ, चूल्हे (hearths) और पश्चिम-पूर्व दिशा में दफनाए गए मानव कंकाल मिले हैं।"
    },
    {
        "q": "दक्षिण भारत का कौन सा स्थल सबसे प्रसिद्ध और शुरुआती महापाषाण (Megalithic) कलश शवाधान (urn burial) स्थल के रूप में जाना जाता है?",
        "opts": ["आदिचनल्लूर", "ब्रह्मागिरी", "मास्की", "हल्लूर"],
        "ans": 0,
        "sol": "तमिलनाडु के थूथुकुडी जिले में स्थित आदिचनल्लूर एक प्रसिद्ध महापाषाण/लौह युगीन स्थल है जहाँ हजारों कलश कब्रें मिली हैं, जिनमें लोहे के हथियार और मिट्टी के बर्तन रखे जाते थे।"
    },
    {
        "q": "50,000 वर्ष पुराने हड्डी और कोयले जैसे जैविक अवशेषों की आयु निर्धारित करने के लिए आमतौर पर किस विधि का उपयोग किया जाता है?",
        "opts": ["पोटेशियम-ऑर्गन डेटिंग", "रेडियोकार्बन (C-14) डेटिंग", "थर्मोल्यूमिनेसेंस", "डेंड्रोक्रोनोलॉजी"],
        "ans": 1,
        "sol": "रेडियोकार्बन (C-14) डेटिंग विधि जैविक अवशेषों (लकड़ी, कोयला, हड्डियों) में कार्बन-14 समस्थानिक के क्षय को मापती है। यह लगभग 50,000 वर्ष तक की आयु के लिए सटीक है।"
    },
    {
        "q": "यूनेस्को द्वारा विश्व धरोहर घोषित भीमबेटका रॉक शेल्टर्स भारत के किस राज्य में स्थित हैं?",
        "opts": ["महाराष्ट्र", "मध्य प्रदेश", "उत्तर प्रदेश", "राजस्थान"],
        "ans": 1,
        "sol": "भीमबेटका मध्य प्रदेश के रायसेन जिले में विंध्य पर्वत श्रृंखलाओं में स्थित है। यहाँ पुरापाषाण काल से लेकर ऐतिहासिक काल तक की गुफा चित्रकारी देखी जा सकती है।"
    },
    {
        "q": "भारत में मध्य पुरापाषाण काल (Middle Paleolithic) के उपकरणों की मुख्य विशेषता क्या थी?",
        "opts": ["भारी हस्त-कुठार (Handaxes)", "पॉलिशदार सेल्ट (Celts)", "शल्क उपकरण (Flake tools - खुरचनी, वेधक)", "सूक्ष्म पाषाण उपकरण (Microliths)"],
        "ans": 2,
        "sol": "मध्य पुरापाषाण उद्योग मुख्य रूप से शल्क उपकरणों (flake tools) जैसे खुरचनी (scrapers), वेधक (borers) और वेधनी (points) द्वारा चिह्नित है, जो बड़े पत्थरों से तोड़कर बनाए जाते थे।"
    },
    {
        "q": "दक्षिण भारत के किस स्थल से इस क्षेत्र में लोहे के उपयोग का सबसे पहला साक्ष्य (लगभग 1000 ईपू) मिला है?",
        "opts": ["हल्लूर", "ब्रह्मागिरी", "मास्की", "पिकलीहल"],
        "ans": 0,
        "sol": "कर्नाटक के हावेरी जिले में स्थित हल्लूर से दक्षिण भारत में लोहे के उपयोग के सबसे पुराने रेडियोकार्बन साक्ष्य (लगभग 1000 ईपू) मिले हैं।"
    },
    {
        "q": "गेरूए रंग के मृदभांड (OCP) आमतौर पर किस पुरातात्विक चरण से जुड़े हैं?",
        "opts": ["उत्तर नवपाषाण काल", "उत्तर हड़प्पा और ताम्र संचय संस्कृतियाँ", "मौर्य साम्राज्य", "द्वितीय नगरीकरण"],
        "ans": 1,
        "sol": "गेरूए रंग के मृदभांड (OCP) लगभग 2000-1500 ईपू के हैं, जो गंगा-यमुना दोआब के ताम्र संचय (Copper Hoards) से जुड़े हैं।"
    },
    {
        "q": "पुरापाषाण कालीन समुदायों के भोजन का मुख्य स्रोत क्या था?",
        "opts": ["पशुपालन और डेयरी", "कृषि", "शिकार और जंगली कंदमूल संग्रह", "मछली पालन"],
        "ans": 2,
        "sol": "पुरापाषाण काल के मानव घुमंतू शिकारी-संग्रहकर्ता थे। वे कृषि या पशुपालन नहीं जानते थे।"
    },
    {
        "q": "दक्कन में राख के टीलों (जैसे कुपगल) की खोज से नवपाषाण कालीन जीवनशैली की क्या जानकारी मिलती है?",
        "opts": ["स्थायी गेहूं की खेती", "पशुचारण और मवेशी पालन गतिविधियाँ", "तांबा पिघलाने की भट्टी", "महापाषाण काल की तैयारी"],
        "ans": 1,
        "sol": "राख के टीले मवेशियों के बाड़ों में गोबर के जमाव को जलाने से बने थे, जो नवपाषाण कालीन चरवाहा अर्थव्यवस्था को दर्शाते हैं।"
    },
    {
        "q": "राजस्थान का कौन सा ताम्रपाषाण कालीन स्थल अपनी पक्की ईंटों की सुरक्षा दीवार के साक्ष्य के लिए जाना जाता है?",
        "opts": ["आहार", "गिलुंड", "बालाथल", "डीड़वाना"],
        "ans": 1,
        "sol": "राजस्थान के उदयपुर जिले में स्थित गिलुंड एक प्रमुख बनास संस्कृति स्थल है, जहाँ से पक्की ईंटों की सुरक्षा दीवार के साक्ष्य मिले हैं।"
    },
    {
        "q": "महाराष्ट्र के पाटने (Patne) स्थल से कौन सी महत्वपूर्ण प्रागैतिहासिक खोज हुई है?",
        "opts": ["सबसे पुराना नवपाषाण ग्राम", "उच्च पुरापाषाण कालीन शुतुरमुर्ग के अंडे के छिलके", "दैमाबाद की कांस्य मूर्तियां", "मध्यपाषाण कालीन पशु कब्रें"],
        "ans": 1,
        "sol": "पाटने से उच्च पुरापाषाण काल के शुतुरमुर्ग के अंडों के छिलके के टुकड़े मिले हैं, जिन पर बारीक नक्काशी की गई है और मनके बनाए गए हैं।"
    },
    {
        "q": "एक पोर्ट-होल (circular opening) किस प्रकार की कब्रों/समाधियों की मुख्य विशेषता है?",
        "opts": ["उच्च पुरापाषाण गुफाएं", "नवपाषाण गर्त-आवास", "महापाषाण कालीन सिस्ट (Cist) कब्रें", "जोरवे कलश शवाधान"],
        "ans": 2,
        "sol": "दक्षिण भारत की महापाषाण कालीन सिस्ट कब्रों (पत्थर की बक्सेनुमा समाधि) के पूर्वी हिस्से में एक गोलाकार छेद (पोर्ट-होल) होता था, माना जाता है कि यह बाद के शवों या उपहारों के लिए प्रवेश द्वार था।"
    },
    {
        "q": "भारतीय उपमहाद्वीप में गेहूं और जौ की खेती के प्राचीनतम साक्ष्य किस स्थल से प्राप्त हुए हैं?",
        "opts": ["मेहरगढ़", "कोलडिहवा", "बुर्जहोम", "चिरण्ड"],
        "ans": 0,
        "sol": "मेहरगढ़ (लगभग 7000 ईपू, बलूचिस्तान) से उपमहाद्वीप में गेहूं और जौ की खेती के सबसे प्राचीन साक्ष्य मिले हैं।"
    },
    {
        "q": "ताम्रपाषाण काल की किस क्षेत्रीय संस्कृति में एरन (Eran) स्थित है?",
        "opts": ["जोरवे संस्कृति", "मालवा संस्कृति", "आहार संस्कृति", "प्रभास संस्कृति"],
        "ans": 1,
        "sol": "मध्य प्रदेश में स्थित एरन मालवा ताम्रपाषाण संस्कृति का एक प्रमुख स्थल है, जो अपनी सुरक्षात्मक मिट्टी की प्राचीर के लिए जाना जाता है।"
    },
    {
        "q": "1861 में भारतीय पुरातत्व सर्वेक्षण (ASI) के पहले महानिदेशक के रूप में किसे नियुक्त किया गया था?",
        "opts": ["अलेक्जेंडर कनिंघम (Alexander Cunningham)", "जॉन मार्शल (John Marshall)", "मोर्टिमर व्हीलर (Mortimer Wheeler)", "जेम्स प्रिंसिप (James Prinsep)"],
        "ans": 0,
        "sol": "अलेक्जेंडर कनिंघम को 1861 में भारत के पहले पुरातात्विक सर्वेक्षक के रूप में नियुक्त किया गया था। उन्हें ASI का संस्थापक माना जाता है।"
    },
    {
        "q": "कौन सा स्थल प्रागैतिहासिक गुफा चित्रों के लिए प्रसिद्ध है, जिसमें गतिशील सामूहिक शिकार के दृश्य दिखाए गए हैं?",
        "opts": ["अतिरामपक्कम", "हुंसगी", "भीमबेटका", "मेहरगढ़"],
        "ans": 2,
        "sol": "भीमबेटका के शैलचित्रों में मध्यपाषाण कालीन मानवों द्वारा जानवरों का शिकार करने, नृत्य करने और अनुष्ठानों के गतिशील दृश्य चित्रित हैं।"
    },
    {
        "q": "नवपाषाण कालीन स्थल गुफक्राल (जिसका अर्थ 'कुम्हार की गुफा' है) किस क्षेत्र में स्थित है?",
        "opts": ["हिमाचल प्रदेश", "जम्मू-कश्मीर", "लद्दाख", "उत्तराखंड"],
        "ans": 1,
        "sol": "गुफक्राल जम्मू-कश्मीर के पुलवामा जिले में स्थित है, जहाँ से गर्त-आवास, कृषि और पशुपालन के साक्ष्य मिले हैं।"
    },
    {
        "q": "प्रागैतिहासिक मृदभांड (पॉटरी) संस्कृतियों का सही कालानुक्रमिक क्रम क्या है?",
        "opts": ["PGW &rarr; BRW &rarr; NBPW", "BRW &rarr; PGW &rarr; NBPW", "NBPW &rarr; PGW &rarr; BRW", "PGW &rarr; NBPW &rarr; BRW"],
        "ans": 1,
        "sol": "सही अनुक्रम है: काले और लाल मृदभांड (BRW - ताम्रपाषाण काल) &rarr; चित्रित धूसर मृदभांड (PGW - लौह युग) &rarr; उत्तरी काले चमकीले मृदभांड (NBPW - महाजनपद काल)।"
    },
    {
        "q": "उच्च पुरापाषाण काल के संदर्भ में हड्डी की बनी सुई (bone needle) का प्राचीनतम साक्ष्य किस घाटी से मिला है?",
        "opts": ["भीमबेटका", "बेलन घाटी", "कुरनूल गुफाएं", "नेवासा"],
        "ans": 1,
        "sol": "उत्तर प्रदेश की बेलन घाटी के लोहंदा नाला क्षेत्र से हड्डी की बनी सुई (या कुछ विद्वानों के अनुसार मातृदेवी की मूर्ति) मिली है, जो उच्च पुरापाषाण काल की है।"
    },
    {
        "q": "दक्षिण भारत में महापाषाण स्मारकों के रूप में खड़े किए गए एकल विशाल पत्थरों को क्या कहा जाता है?",
        "opts": ["डोलमेन (Dolmen)", "मेनहिर (Menhir)", "केर्न (Cairn)", "सिस्ट (Cist)"],
        "ans": 1,
        "sol": "मेनहिर (Menhir) महापाषाण लौह युग के दौरान स्मारक के रूप में जमीन में गाड़ा गया एक अकेला सीधा खड़ा पत्थर होता था।"
    },
    {
        "q": "मध्य भारत और गंगा-यमुना दोआब के 'ताम्र संचय' (Copper Hoards) आमतौर पर किससे जुड़े हैं?",
        "opts": ["सिंधु घाटी सभ्यता", "गेरूए रंग के मृदभांड (OCP) चरण", "महापाषाण कालीन शवाधान", "NBPW संस्कृति"],
        "ans": 1,
        "sol": "गंगा-यमुना दोआब में पाए जाने वाले ताम्र संचय (Copper Hoards, लगभग 2000-1500 ईपू) पुरातात्विक रूप से गेरूए रंग के मृदभांड (OCP) संस्कृति से संबंधित हैं।"
    },
    {
        "q": "कौन सा भू-वैज्ञानिक युग पुरापाषाण काल (Paleolithic Age) से मेल खाता है, जो बार-बार हिमयुग के आगमन से चिह्नित था?",
        "opts": ["होलोसीन (Holocene)", "प्लीस्टोसीन (Pleistocene)", "प्लायोसीन (Pliocene)", "मायोसीन (Miocene)"],
        "ans": 1,
        "sol": "प्लीस्टोसीन युग (Pleistocene epoch / हिमयुग), जो लगभग 26 लाख वर्ष पहले शुरू हुआ और 11,700 वर्ष पहले समाप्त हुआ, पुरापाषाण काल के समकालीन था।"
    }
]

hi_testQuestions = [
    {
        "q": "भारत में पुरापाषाण (Paleolithic) काल के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. पाकिस्तान में सोअन घाटी को उपमहाद्वीप में सबसे पुराना पुरापाषाण स्थल माना जाता है।\n2. भारत में अधिकांश पुरापाषाण कालीन उपकरण क्वार्ट्जाइट से बने थे, जिसके कारण यहाँ के पुरापाषाण मनुष्यों को 'क्वार्ट्जाइट मैन' कहा गया।\n3. भेड़ और बकरी को पालतू बनाने की प्रथा सबसे पहले निम्न पुरापाषाण काल में शुरू की गई थी।",
        "statements": [],
        "opts": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। पशुपालन पुरापाषाण काल में नहीं, बल्कि मध्यपाषाण (Mesolithic) काल में शुरू हुआ था।"
    },
    {
        "q": "भारत में मध्यपाषाण (Mesolithic) काल के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. राजस्थान में स्थित बागोर भारत का सबसे बड़ा उत्खनित मध्यपाषाण कालीन स्थल है।\n2. उत्तर प्रदेश के सराय नाहर राय से पश्चिम-पूर्व दिशा में दफनाए गए मानव कंकाल मिले हैं।\n3. होलोसीन (Holocene) युग की शुरुआत से होने वाले जलवायु परिवर्तनों ने सूक्ष्म पाषाण उपकरणों (microliths) के उपयोग को समाप्त कर दिया।",
        "statements": [],
        "opts": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 and 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। होलोसीन के कारण उत्पन्न जलवायु परिवर्तन से माइक्रोलिथ का उपयोग समाप्त नहीं हुआ, बल्कि यह मध्यपाषाण काल का मुख्य आधार बन गया।"
    },
    {
        "q": "निम्नलिखित में से कौन सा/से नवपाषाण (Neolithic) स्थल और उनकी प्रमुख विशेषताओं का युग्म सही सुमेलित है/हैं?\n1. बुर्जहोम &mdash; गर्त-आवास (pit dwellings) और कुत्ते दफनाने की प्रथा\n2. मेहरगढ़ &mdash; विश्व में सबसे प्राचीन चावल की खेती के साक्ष्य\n3. चिरण्ड &mdash; हिरण के सींग से बने हड्डी के उपकरणों का विशाल संग्रह",
        "statements": [],
        "opts": ["केवल 1 और 3", "केवल 2 और 3", "केवल 1 और 2", "1, 2 और 3"],
        "ans": 0,
        "sol": "युग्म 1 और 3 सही सुमेलित हैं। मेहरगढ़ गेहूं/जौ की प्राचीनतम खेती के लिए प्रसिद्ध है, जबकि सबसे प्राचीन चावल के साक्ष्य उत्तर प्रदेश के कोलडिहवा से मिले हैं।"
    },
    {
        "q": "बुर्जहोम (Burzahom) नवपाषाण कालीन स्थल के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. अत्यधिक ठंड से बचने के लिए भूमिगत गर्त-आवासों (pit-dwellings) का निर्माण किया गया था।\n2. यहाँ से प्राप्त मिट्टी के बर्तन मुख्य रूप से उत्कृष्ट पहिये से बने उत्तरी काले चमकीले मृदभांड (NBPW) हैं।\n3. लोग कब्रों में अपने पालतू कुत्तों को स्वामियों के साथ दफनाते थे।",
        "statements": [],
        "opts": ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 3 सही हैं। बुर्जहोम के बर्तन खुरदुरे धूसर/काले चमकीले प्रकार के थे। NBPW बहुत बाद के द्वितीय नगरीकरण/लौह युग से संबंधित है।"
    },
    {
        "q": "भारत में ताम्रपाषाण (Chalcolithic) संस्कृतियों के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. महाराष्ट्र की जोरवे संस्कृति मुख्य रूप से ग्रामीण थी, लेकिन इसमें दैमाबाद और इनामगांव जैसे बड़े अर्ध-शहरी केंद्र शामिल थे।\n2. राजस्थान की आहार संस्कृति में पत्थर के सूक्ष्म उपकरणों (microliths) का पूर्ण अभाव पाया जाता है, यहाँ केवल तांबे का उपयोग होता था।\n3. सफेद रंग से चित्रित काले और लाल मृदभांड (BRW) मालवा संस्कृति की विशिष्ट पहचान हैं।",
        "statements": [],
        "opts": ["केवल 1 और 2", "केवल 1 और 3", "केवल 2 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। आहार संस्कृति में सूक्ष्म पाषाण उपकरणों का पूर्ण अभाव है, यहाँ तांबे का उपयोग होता था। सफेद रंग से चित्रित BRW बर्तनों का संबंध बनास (आहार) संस्कृति से है।"
    },
    {
        "q": "प्राचीन भारत में महापाषाण (Megaliths) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. महापाषाण पत्थर की बड़ी समाधियों को संदर्भित करते हैं, जिनका निर्माण मुख्यतः लौह युग में हुआ था।\n2. ये कब्रें केवल दक्कन और दक्षिण भारत में ही पाई जाती हैं।\n3. महापाषाण कब्रों से बड़ी संख्या में लोहे के कृषि उपकरण और हथियार प्राप्त होते हैं।",
        "statements": [],
        "opts": ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 3 सही हैं। महापाषाण कब्रें केवल दक्षिण भारत में नहीं, बल्कि कश्मीर, राजस्थान, और उत्तर प्रदेश में भी पाई गई हैं।"
    },
    {
        "q": "भारतीय उपमहाद्वीप में लोहे की प्राचीनता के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. भारत में लौह प्रगलन का प्राचीनतम साक्ष्य उत्तर प्रदेश के मल्हार (Malhar) से मिला है, जो लगभग 1800 ईपू का है।\n2. दक्षिण भारत में प्रारंभिक लोहे के साक्ष्य कर्नाटक के हल्लूर (Hallur) से मिले हैं।\n3. लौह तकनीक के विकास के कारण ही सिंधु घाटी में प्रथम नगरीकरण हुआ।",
        "statements": [],
        "opts": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। लौह तकनीक के कारण द्वितीय नगरीकरण (लगभग 600 ईपू) हुआ था। सिंधु घाटी सभ्यता एक कांस्य युगीन सभ्यता थी।"
    },
    {
        "q": "निम्नलिखित में से कौन सा/से कथन प्रागैतिहासिक मृदभांड (pottery) परंपराओं के बारे में सही है/हैं?\n1. गेरूए रंग के मृदभांड (OCP) प्रारंभिक वैदिक बस्तियों से जुड़े हैं।\n2. चित्रित धूसर मृदभांड (PGW) उत्तर वैदिक काल की लौह युगीन संस्कृति का प्रतिनिधित्व करते हैं।\n3. उत्तरी काले चमकीले मृदभांड (NBPW) महाजनपदों के समृद्ध और लक्जरी बर्तनों का प्रतिनिधित्व करते हैं।",
        "statements": [],
        "opts": ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 2 और 3 सही हैं। OCP बर्तनों का संबंध उत्तर हड़प्पा और ताम्र संचय (Copper Hoard) संस्कृतियों (लगभग 2000-1500 ईपू) से है।"
    },
    {
        "q": "दक्षिण भारत में पाए जाने वाले 'राख के टीलों' (Ash Mounds) के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. ये टीले मवेशियों के बाड़ों में एकत्रित किए गए गोबर को जलाने से बने थे।\n2. ये कर्नाटक और आंध्र प्रदेश के नवपाषाण कालीन चरवाहा (pastoral) समुदायों से संबंधित हैं।\n3. ये ताम्रपाषाण काल के तांबा प्रगलन भट्टी (copper smelting furnaces) के अवशेष हैं।",
        "statements": [],
        "opts": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans": 0,
        "sol": "कथन 1 और 2 सही हैं। राख के टीले गोबर जलाने से बने हैं, न कि तांबा गलाने की भट्टियों के अवशेष हैं।"
    },
    {
        "q": "भू-वैज्ञानिक समयरेखा और प्रागैतिहास के संदर्भ में निम्नलिखित कथनों पर विचार कीजिए:\n1. पुरापाषाण (Paleolithic) काल भू-वैज्ञानिक प्लीस्टोसीन युग (हिमयुग) से मेल खाता है।\n2. होलोसीन (Holocene) युग हिमयुग के बाद की गर्म जलवायु से संबंधित है, जिसमें मध्यपाषाण और नवपाषाण संस्कृतियां विकसित हुईं।\n3. अतिरामपक्कम में मिले एशुलेयिन (Acheulian) उपकरणों को लगभग 15 लाख वर्ष पुराना आंका गया है।",
        "statements": [],
        "opts": ["1, 2 और 3", "केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3"],
        "ans": 0,
        "sol": "सभी कथन सही हैं। अतिरामपक्कम 1.5 MYA पुराना है, प्लीस्टोसीन पुरापाषाण से मेल खाता है, और होलोसीन गर्म काल का प्रतिनिधित्व करता है।"
    }
]

# We will serialize these lists to JSON and replace the English questions in the file
pQs_json = json.dumps(hi_pQuestions, ensure_ascii=False, indent=12)
tQs_json = json.dumps(hi_testQuestions, ensure_ascii=False, indent=12)

# Find the pQuestions array in the html and replace it
# Use regex to find pQuestions = [ ... ];
html = re.sub(r'const pQuestions\s*=\s*\[[\s\S]*?\];', lambda m: f'const pQuestions = {pQs_json};', html)

# Find the testQuestions array in the html and replace it
# Use regex to find testQuestions = [ ... ];
html = re.sub(r'const testQuestions\s*=\s*\[[\s\S]*?\];', lambda m: f'const testQuestions = {tQs_json};', html)

# Write the updated html back to the file
with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Successfully translated hi/index.html to Hindi!")

