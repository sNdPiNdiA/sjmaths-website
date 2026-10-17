import os
import re

def build_comp_history_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Evolution, Generations &amp; Classification of Computers</span>
    <span class="lang-hi">माइंड मैप: कंप्यूटर का विकास, पीढ़ियां एवं वर्गीकरण</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Computer Fundamentals & History] --> B[Chronological Evolution]
    A --> C[Computer Generations]
    A --> D[Classification of Computers]
    A --> E[Architecture & Applications]

    B --> B1[Manual Era: Abacus, Napier Bones, Pascaline, Leibniz Wheel]
    B --> B2[Mechanical Era: Babbage Difference & Analytical Engine | Ada Lovelace]
    B --> B3[Electro-Mechanical Era: Hollerith Tabulator | Punch Cards | Mark I]
    B --> B4[Electronic Era: ABC, ENIAC, EDVAC, EDSAC, UNIVAC-I]

    C --> C1[1st Gen 1940-56: Vacuum Tubes | Machine/Assembly | Milliseconds | ENIAC, UNIVAC]
    C --> C2[2nd Gen 1956-63: Transistors | FORTRAN, COBOL | Microseconds | IBM 1401]
    C --> C3[3rd Gen 1964-71: Integrated Circuits SSI/MSI | Time-sharing OS | Nanoseconds | IBM 360]
    C --> C4[4th Gen 1971-Present: Microprocessors VLSI/ULSI | C, C++, GUI | Picoseconds | PCs]
    C --> C5[5th Gen Present-Future: Ultra Large Scale ULSI | AI, Quantum, Parallel Processing]

    D --> D1[By Mechanism: Analog, Digital, Hybrid]
    D --> D2[By Size & Speed: Micro, Mini, Mainframe, Supercomputer]
    D --> D3[By Purpose: General Purpose vs Special Purpose]

    E --> E1[Von Neumann Architecture: CPU ALU+CU, Registers, Memory, Bus]
    E --> E2[Modern Applications: E-Governance, Defense, Weather, AI, Education]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[कंप्यूटर मूल बातें एवं इतिहास] --> B[कालक्रमानुसार ऐतिहासिक विकास]
    A --> C[कंप्यूटर की पीढ़ियां]
    A --> D[कंप्यूटरों का वर्गीकरण]
    A --> E[वास्तुकला एवं आधुनिक अनुप्रयोग]

    B --> B1[मैनुअल युग: अबेकस, नेपियर्स बोन्स, पास्कलाइन, लाइबनिज चक्र]
    B --> B2[यांत्रिक युग: बैबेज का डिफरेंस व एनालिटिकल इंजन | एडा लवलेस]
    B --> B3[विद्युत-यांत्रिक युग: हॉलेरिथ टैबुलेटर | पंच कार्ड | मार्क-1]
    B --> B4[इलेक्ट्रॉनिक युग: ABC, ENIAC, EDVAC, EDSAC, UNIVAC-I]

    C --> C1[प्रथम पीढ़ी 1940-56: वैक्यूम ट्यूब | मशीन/असेंबली | मिलीसेकंड | ENIAC, UNIVAC]
    C --> C2[द्वितीय पीढ़ी 1956-63: ट्रांजिस्टर | फोरट्रान, कोबोल | माइक्रोसेकंड | IBM 1401]
    C --> C3[तृतीय पीढ़ी 1964-71: एकीकृत परिपथ IC | टाइम-शेयरिंग OS | नैनोसेकंड | IBM 360]
    C --> C4[चतुर्थ पीढ़ी 1971-वर्तमान: माइक्रोप्रोसेसर VLSI/ULSI | C, C++, GUI | पिकोसेकंड | PC]
    C --> C5[पंचम पीढ़ी वर्तमान-भविष्य: ULSI/AI | क्वांटम कंप्यूटिंग | समानांतर प्रसंस्करण]

    D --> D1[कार्यप्रणाली आधार: एनालॉग, डिजिटल, हाइब्रिड]
    D --> D2[आकार व गति आधार: माइक्रो, मिनी, मेनफ्रेम, सुपरकंप्यूटर]
    D --> D3[उद्देश्य आधार: सामान्य उद्देशीय एवं विशिष्ट उद्देशीय]

    E --> E1[वॉन न्यूमैन आर्किटेक्चर: CPU ALU+CU, रजिस्टर्स, मेमोरी, बस प्रणाली]
    E --> E2[आधुनिक अनुप्रयोग: ई-गवर्नेंस, रक्षा, मौसम पूर्वानुमान, AI, शिक्षा]
    </div>
  </div>
</div>

<!-- Card 2: Chronological Evolution of Computing Devices -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Chronological Evolution of Computing Devices: Manual to Electronic Era</span>
    <span class="lang-hi">1. कंप्यूटर का कालक्रमानुसार ऐतिहासिक विकास: मैनुअल से इलेक्ट्रॉनिक युग</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Abacus (अबेकस - ~3000 BCE, Babylonia/China):</strong>
          <br>&bull; World's first mechanical calculating aid; consisted of wooden frame with beads sliding on parallel wires.
          <br>&bull; Performed addition and subtraction; Upper deck beads called <em>Heaven</em> (value 5) and lower deck called <em>Earth</em> (value 1).</span>
        <span class="lang-hi"><strong>अबेकस (~3000 ई.पू., बेबीलोनिया/चीन):</strong>
          <br>&bull; विश्व का प्रथम यांत्रिक गणना यंत्र; समानांतर तारों पर मोतियों (Beads) के सहारे गणना की जाती थी।
          <br>&bull; जोड़ एवं घटाव हेतु प्रयुक्त; ऊपरी भाग को <em>हेवन</em> (मान 5) एवं निचले भाग को <em>अर्थ</em> (मान 1) कहा जाता था।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Napier's Bones (1617 - John Napier, Scotland):</strong>
          <br>&bull; Invented by the Scottish mathematician who introduced <em>Logarithms</em>.
          <br>&bull; Consisted of numbered rods carved from animal bones used for fast multiplication and division.</span>
        <span class="lang-hi"><strong>नेपियर्स बोन्स (1617 - जॉन नेपियर, स्कॉटलैंड):</strong>
          <br>&bull; लघुगणक (Logarithms) के आविष्कारक जॉन नेपियर द्वारा विकसित।
          <br>&bull; जानवरों की हड्डियों पर 0 से 9 तक के पहाड़े अंकित छड़ों द्वारा तीव्र गुणा एवं भाग करने वाला यंत्र।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Pascaline / Arithmetic Machine (1642 - Blaise Pascal, France):</strong>
          <br>&bull; <strong>World's first mechanical adding machine</strong> (mechanical calculator).
          <br>&bull; Operated on toothed wheels and gears with automatic carry-over mechanism (odometer principle); could perform addition and subtraction only.</span>
        <span class="lang-hi"><strong>पास्कलाइन (1642 - ब्लेज पास्कल, फ्रांस):</strong>
          <br>&bull; <strong>विश्व का प्रथम यांत्रिक गणना कैलकुलेटर (Adding Machine)</strong>।
          <br>&bull; दांतेदार पहियों (Gears) और चक्रों पर आधारित, जिसमें कैरी-ओवर तंत्र था; केवल जोड़ और घटाव करने में सक्षम।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Step Reckoner / Leibniz Calculator (1671 - Gottfried Wilhelm Leibniz, Germany):</strong>
          <br>&bull; Extended Pascal's design using stepped cylinders (stepped drum / Leibniz wheel).
          <br>&bull; First mechanical calculator capable of all four fundamental arithmetic operations: addition, subtraction, multiplication, and division, plus square roots.
          <br>&bull; Leibniz also developed the modern <strong>Binary Number System (0 and 1)</strong>.</span>
        <span class="lang-hi"><strong>स्टेप रेकनर / लाइबनिज कैलकुलेटर (1671 - गॉटफ्रीड विल्हेम लाइबनिज, जर्मनी):</strong>
          <br>&bull; पास्कल के यंत्र में सुधार कर 'स्टेप्ड ड्रम' (लाइबनिज व्हील) का प्रयोग किया गया।
          <br>&bull; चारों बुनियादी गणितीय संक्रियाएं (जोड़, घटाव, गुणा, भाग) तथा वर्गमूल निकालने वाला पहला यंत्र।
          <br>&bull; लाइबनिज ने ही आधुनिक <strong>बाइनरी संख्या प्रणाली (0 और 1)</strong> का प्रतिपादन किया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Jacquard's Loom (1804 - Joseph Marie Jacquard, France):</strong>
          <br>&bull; First machine to use <strong>punched cards</strong> with holes to control weaving patterns automatically; laid the conceptual foundation for binary data storage.</span>
        <span class="lang-hi"><strong>जैकवार्ड लूम (1804 - जोसेफ मैरी जैकवार्ड, फ्रांस):</strong>
          <br>&bull; बुनाई के पैटर्न को स्वचालित रूप से नियंत्रित करने हेतु <strong>पंच कार्ड (Punched Cards)</strong> का प्रयोग करने वाली पहली मशीन; बाइनरी डेटा भंडारण की आधारशिला।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Charles Babbage's Engines (England - "Father of Modern Computer"):</strong>
          <br>&bull; <em>Difference Engine (1822):</em> Steam-powered mechanical calculator designed to tabulate mathematical polynomial functions up to 20 decimal places.
          <br>&bull; <em>Analytical Engine (1833):</em> <strong>First general-purpose mechanical computer design</strong>. Incorporated the 5 modern computer components: Store (Memory), Mill (ALU/CPU), Control (CU), Input (Punch cards), and Output (Printer/Bell).
          <br>&bull; <strong>Lady Ada Lovelace (Augusta Ada Byron):</strong> World's first computer programmer; wrote the first algorithm (calculating Bernoulli numbers) for Babbage's Analytical Engine; introduced concepts of loops and subroutines.</span>
        <span class="lang-hi"><strong>चार्ल्स बैबेज के इंजन (इंग्लैंड - "कंप्यूटर के जनक"):</strong>
          <br>&bull; <em>डिफरेंस इंजन (1822):</em> भाप से चलने वाला यांत्रिक कैलकुलेटर, जो 20 दशमलव स्थानों तक बहुपदीय फलनों की गणना कर सकता था।
          <br>&bull; <em>एनालिटिकल इंजन (1833):</em> <strong>विश्व का प्रथम सामान्य उद्देशीय यांत्रिक कंप्यूटर डिजाइन</strong>। इसमें आधुनिक कंप्यूटर के 5 मूलभूत अंग थे: स्टोर (मेमोरी), मिल (CPU/ALU), कंट्रोल (CU), इनपुट (पंच कार्ड) तथा आउटपुट।
          <br>&bull; <strong>लेडी एडा लवलेस:</strong> विश्व की <strong>प्रथम कंप्यूटर प्रोग्रामर</strong>; उन्होंने एनालिटिकल इंजन हेतु पहला प्रोग्राम (बरनौली संख्याओं की गणना) लिखा; लूप एवं सबरूटीन की जनक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Hollerith Tabulating Machine (1890 - Herman Hollerith, USA):</strong>
          <br>&bull; Electro-mechanical machine using punched cards to process the 1890 US Census data in 2.5 years (down from 8 years).
          <br>&bull; Hollerith founded the <em>Tabulating Machine Company (1896)</em>, which merged in 1911 and was renamed in 1924 as <strong>IBM (International Business Machines)</strong>.</span>
        <span class="lang-hi"><strong>हॉलेरिथ टैबुलेटिंग मशीन (1890 - हरमन हॉलेरिथ, अमेरिका):</strong>
          <br>&bull; 1890 की अमेरिकी जनगणना को मात्र 2.5 वर्षों में संसाधित करने वाली विद्युत-यांत्रिक मशीन।
          <br>&bull; हॉलेरिथ ने 1896 में 'टैबुलेटिंग मशीन कंपनी' बनाई, जो 1924 में <strong>IBM (इंटरनेशनल बिजनेस मशीन्स)</strong> बनी।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Mark-I (1944 - Howard Aiken, Harvard &amp; IBM):</strong>
          <br>&bull; <strong>First fully automatic electromechanical computer</strong> (ASCC - Automatic Sequence Controlled Calculator); 51 feet long, 5 tons weight, used 750,000 components and relays.</span>
        <span class="lang-hi"><strong>मार्क-1 (1944 - हॉवर्ड आइकन, हार्वर्ड एवं IBM):</strong>
          <br>&bull; <strong>विश्व का प्रथम पूर्णतः स्वचालित विद्युत-यांत्रिक कंप्यूटर</strong> (ASCC); 51 फीट लंबा, 5 टन वजनी, 7.5 लाख पुर्जों व रिले से निर्मित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>First Electronic Computers Milestone:</strong>
          <br>&bull; <em>ABC (Atanasoff-Berry Computer, 1939-42):</em> First electronic digital computing device (used vacuum tubes, binary math, regenerative capacitor memory).
          <br>&bull; <em>ENIAC (1946 - J. Presper Eckert &amp; John Mauchly, Univ. of Pennsylvania):</em> <strong>First general-purpose electronic digital computer</strong>; used 18,000 vacuum tubes, weighed 30 tons, consumed 150 kW power.
          <br>&bull; <em>EDSAC (1949 - Maurice Wilkes, Cambridge Univ.):</em> <strong>First practical stored-program computer</strong>.
          <br>&bull; <em>EDVAC (1950 - Eckert, Mauchly &amp; John von Neumann):</em> Implemented complete stored-program binary architecture.
          <br>&bull; <em>UNIVAC-I (Universal Automatic Computer, 1951):</em> <strong>First commercially available general-purpose computer</strong> produced for business and census.</span>
        <span class="lang-hi"><strong>प्रारंभिक इलेक्ट्रॉनिक कंप्यूटरों के मील के पत्थर:</strong>
          <br>&bull; <em>ABC (अटानासॉफ-बेरी कंप्यूटर, 1939-42):</em> प्रथम इलेक्ट्रॉनिक डिजिटल कंप्यूटिंग डिवाइस (वैक्यूम ट्यूब व बाइनरी अंकगणित पर आधारित)।
          <br>&bull; <em>ENIAC (1946 - जे. प्रेस्पर एकर्ट एवं जॉन मौचली):</em> <strong>विश्व का प्रथम सामान्य उद्देशीय पूर्णतः इलेक्ट्रॉनिक डिजिटल कंप्यूटर</strong>; 18,000 वैक्यूम ट्यूब, 30 टन वजन, 150 kW बिजली खपत।
          <br>&bull; <em>EDSAC (1949 - मॉरिस विल्क्स, कैम्ब्रिज):</em> <strong>संग्रहीत प्रोग्राम (Stored Program) पर चलने वाला प्रथम व्यावहारिक कंप्यूटर</strong>।
          <br>&bull; <em>EDVAC (1950):</em> वॉन न्यूमैन की बाइनरी संग्रहीत प्रोग्राम वास्तुकला पर निर्मित कंप्यूटर।
          <br>&bull; <em>UNIVAC-I (1951):</em> <strong>व्यावसायिक उपयोग हेतु निर्मित प्रथम इलेक्ट्रॉनिक कंप्यूटर</strong> (जनगणना ब्यूरो हेतु उपलब्ध कराया गया)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Five Generations of Computers Deep Comparison -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Five Generations of Computers: Deep Technical Comparison</span>
    <span class="lang-hi">2. कंप्यूटर की पांच पीढ़ियां: गहन तकनीकी तुलना</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>First Generation (1940 - 1956):</strong>
          <br>&bull; <em>Core Electronic Component:</em> <strong>Vacuum Tubes (Thermionic Valves)</strong> invented by Lee de Forest (1906).
          <br>&bull; <em>Primary Memory:</em> Magnetic Drums and Delay Lines; Secondary Storage: Punched cards and paper tapes.
          <br>&bull; <em>Programming Languages:</em> Machine Language (Binary 0 and 1) and primitive Assembly Language.
          <br>&bull; <em>Processing Speed:</em> Measured in <strong>Milliseconds (10^-3 seconds)</strong>.
          <br>&bull; <em>Characteristics:</em> Immense physical size (room-sized), heavy heat generation, frequent hardware failures (burnouts), batch processing.
          <br>&bull; <em>Examples:</em> ENIAC, EDVAC, EDSAC, UNIVAC-I, IBM 701, IBM 650.</span>
        <span class="lang-hi"><strong>प्रथम पीढ़ी (1940 - 1956):</strong>
          <br>&bull; <em>मुख्य इलेक्ट्रॉनिक घटक:</em> <strong>वैक्यूम ट्यूब (निर्वात नली / थर्मिओनिक वाल्व)</strong> (ली डी फॉरेस्ट द्वारा 1906 में आविष्कृत)।
          <br>&bull; <em>प्राथमिक मेमोरी:</em> मैग्नेटिक ड्रम; द्वितीयक मेमोरी: पंच कार्ड एवं पेपर टेप।
          <br>&bull; <em>प्रोग्रामिंग भाषा:</em> मशीन भाषा (बाइनरी 0 और 1) एवं प्रारंभिक असेंबली भाषा।
          <br>&bull; <em>गति मापन:</em> <strong>मिलीसेकंड (10^-3 सेकंड)</strong>।
          <br>&bull; <em>विशेषताएं:</em> विशाल आकार (कमरे के बराबर), अत्यधिक ऊष्मा उत्सर्जन, बार-बार खराबी, बैच प्रोसेसिंग ऑपरेटिंग सिस्टम।
          <br>&bull; <em>प्रमुख उदाहरण:</em> ENIAC, EDVAC, EDSAC, UNIVAC-I, IBM 701, IBM 650।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Second Generation (1956 - 1963):</strong>
          <br>&bull; <em>Core Electronic Component:</em> <strong>Transistors</strong> invented at Bell Labs in 1947 by John Bardeen, Walter Brattain, and William Shockley (Nobel Prize 1956).
          <br>&bull; <em>Primary Memory:</em> <strong>Magnetic Core Memory</strong>; Secondary: Magnetic Tape and Magnetic Disks.
          <br>&bull; <em>Programming Languages:</em> Early High-Level Languages: <strong>FORTRAN (1957, John Backus - Formula Translation)</strong>, <strong>COBOL (1959, Grace Hopper - Common Business Oriented Language)</strong>, and ALGOL.
          <br>&bull; <em>Processing Speed:</em> Measured in <strong>Microseconds (10^-6 seconds)</strong>.
          <br>&bull; <em>Characteristics:</em> 10x smaller, faster, more reliable, and consumed drastically less electricity than 1st generation.
          <br>&bull; <em>Examples:</em> IBM 1401, IBM 1620, CDC 1604, PDP-1, UNIVAC 1108.</span>
        <span class="lang-hi"><strong>द्वितीय पीढ़ी (1956 - 1963):</strong>
          <br>&bull; <em>मुख्य इलेक्ट्रॉनिक घटक:</em> <strong>ट्रांजिस्टर</strong> (1947 में बेल लैब्स में जॉन बार्डीन, वाल्टर ब्रैटन और विलियम शॉकले द्वारा आविष्कृत; 1956 का नोबेल पुरस्कार)।
          <br>&bull; <em>प्राथमिक मेमोरी:</em> <strong>चुंबकीय कोर मेमोरी (Magnetic Core Memory)</strong>; द्वितीयक: चुंबकीय टेप एवं डिस्क।
          <br>&bull; <em>प्रोग्रामिंग भाषा:</em> उच्च स्तरीय भाषाएं (HLL): <strong>FORTRAN (1957 - जॉन बैकस)</strong>, <strong>COBOL (1959 - ग्रेस हॉपर)</strong> तथा ALGOL।
          <br>&bull; <em>गति मापन:</em> <strong>माइक्रोसेकंड (10^-6 सेकंड)</strong>।
          <br>&bull; <em>विशेषताएं:</em> वैक्यूम ट्यूब से 10 गुना छोटे, तेज, कम बिजली खपत और अधिक विश्वसनीय।
          <br>&bull; <em>प्रमुख उदाहरण:</em> IBM 1401, IBM 1620, CDC 1604, PDP-1।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Third Generation (1964 - 1971):</strong>
          <br>&bull; <em>Core Electronic Component:</em> <strong>Integrated Circuits (IC / Silicon Chips)</strong> invented by Jack Kilby (Texas Instruments, 1958) and Robert Noyce (Fairchild, 1959).
          <br>&bull; <em>Scale of Integration:</em> SSI (Small Scale Integration - up to 10 transistors per chip) and MSI (Medium Scale Integration - 100 to 1,000 transistors).
          <br>&bull; <em>Primary Memory:</em> Semiconductor memory (early RAM); Secondary: Magnetic hard disks.
          <br>&bull; <em>Operating Systems &amp; Languages:</em> <strong>Time-sharing and Multiprogramming Operating Systems</strong>; High-Level Languages: BASIC (1964 - Kemeny &amp; Kurtz), Pascal, PL/1.
          <br>&bull; <em>Processing Speed:</em> Measured in <strong>Nanoseconds (10^-9 seconds)</strong>.
          <br>&bull; <em>Human Interface:</em> Introduction of Monitors (CRTs) and Keyboards replacing punched cards.
          <br>&bull; <em>Examples:</em> IBM System/360, PDP-8, PDP-11, ICL 2900, TDC-316 (India).</span>
        <span class="lang-hi"><strong>तृतीय पीढ़ी (1964 - 1971):</strong>
          <br>&bull; <em>मुख्य इलेक्ट्रॉनिक घटक:</em> <strong>एकीकृत परिपथ (IC चिप / सेमीकंडक्टर)</strong> (1958 में जैक किल्बी एवं रॉबर्ट नॉयस द्वारा आविष्कृत)।
          <br>&bull; <em>एकीकरण स्तर:</em> SSI (स्मॉल स्केल इंटीग्रेशन - चिप पर 10 ट्रांजिस्टर) एवं MSI (मीडियम स्केल इंटीग्रेशन - 100 से 1000 ट्रांजिस्टर)।
          <br>&bull; <em>प्राथमिक मेमोरी:</em> सेमीकंडक्टर रैम (RAM); द्वितीयक: मैग्नेटिक हार्ड डिस्क।
          <br>&bull; <em>ऑपरेटिंग सिस्टम व भाषा:</em> <strong>टाइम-शेयरिंग एवं मल्टीप्रोग्रामिंग OS</strong>; भाषाएँ: BASIC (1964), पास्कल।
          <br>&bull; <em>गति मापन:</em> <strong>नैनोसेकंड (10^-9 सेकंड)</strong>।
          <br>&bull; <em>उपयोगकर्ता इंटरफ़ेस:</em> पंच कार्ड के स्थान पर <strong>कीबोर्ड एवं मॉनिटर</strong> का उपयोग प्रारंभ।
          <br>&bull; <em>प्रमुख उदाहरण:</em> IBM System/360, PDP-8, ICL 2900।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Fourth Generation (1971 - Present):</strong>
          <br>&bull; <em>Core Electronic Component:</em> <strong>Microprocessor</strong> built with <strong>VLSI (Very Large Scale Integration)</strong> and <strong>VLSIC</strong> holding hundreds of thousands of transistors on a single chip.
          <br>&bull; <em>Pioneering Microprocessor:</em> <strong>Intel 4004 (1971)</strong> - 4-bit microprocessor designed by Ted Hoff, Federico Faggin, and Stanley Mazor.
          <br>&bull; <em>Memory &amp; Storage:</em> Semiconductor Dynamic RAM, ROM, Optical Disks (CD/DVD), Flash Drives, Solid State Drives (SSD).
          <br>&bull; <em>Software &amp; OS:</em> Graphical User Interface (GUI), MS-DOS, MS Windows, UNIX, Linux, Apple macOS; Languages: C, C++, Java, Python, SQL.
          <br>&bull; <em>Processing Speed:</em> Measured in <strong>Picoseconds (10^-12 seconds)</strong> to Gigahertz (GHz).
          <br>&bull; <em>Birth of Personal Computers (PC):</em> Altair 8800 (1975), Apple-I &amp; Apple-II (1976-77 - Steve Wozniak &amp; Steve Jobs), IBM PC 5150 (1981).</span>
        <span class="lang-hi"><strong>चतुर्थ पीढ़ी (1971 - वर्तमान):</strong>
          <br>&bull; <em>मुख्य इलेक्ट्रॉनिक घटक:</em> <strong>माइक्रोप्रोसेसर</strong>, जो <strong>VLSI (वेरी लार्ज स्केल इंटीग्रेशन)</strong> तकनीक द्वारा एक छोटी सिलिकॉन चिप पर लाखों ट्रांजिस्टर समाहित करता है।
          <br>&bull; <em>प्रथम माइक्रोप्रोसेसर:</em> <strong>Intel 4004 (1971)</strong> - 4-बिट प्रोसेसर (टेड हॉफ और फेडेरिको फैगिन द्वारा विकसित)।
          <br>&bull; <em>मेमोरी एवं स्टोरेज:</em> सेमीकंडक्टर DRAM, SRAM, ऑप्टिकल डिस्क (CD/DVD), पेन ड्राइव, SSD।
          <br>&bull; <em>सॉफ्टवेयर व OS:</em> ग्राफिकल यूजर इंटरफेस (GUI), MS-DOS, विंडोज, यूनिक्स, लिनक्स; भाषाएं: C, C++, जावा, पायथन।
          <br>&bull; <em>गति मापन:</em> <strong>पिकोसेकंड (10^-12 सेकंड)</strong> तथा गीगाहर्ट्ज (GHz)।
          <br>&bull; <em>पर्सनल कंप्यूटर (PC) का उदय:</em> अल्टेयर 8800 (1975), एप्पल-II (1977), IBM PC (1981)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Fifth Generation (Present &amp; Beyond):</strong>
          <br>&bull; <em>Core Technology:</em> <strong>ULSI (Ultra Large Scale Integration)</strong> packing billions of transistors, Artificial Intelligence (AI), Machine Learning, and Parallel Processing.
          <br>&bull; <em>Frontier Hardware:</em> Quantum Computing (Qubits / Superposition), Optical Computing, Nanotechnology, and Bio-chips.
          <br>&bull; <em>Key Features:</em> Natural Language Processing (NLP), Voice Recognition, Autonomous Robotics, High-Performance Computing (HPC).</span>
        <span class="lang-hi"><strong>पंचम पीढ़ी (वर्तमान एवं भविष्य):</strong>
          <br>&bull; <em>मुख्य तकनीक:</em> <strong>ULSI (अल्ट्रा लार्ज स्केल इंटीग्रेशन)</strong>, कृत्रिम बुद्धिमत्ता (AI), मशीन लर्निंग, तथा समानांतर प्रसंस्करण (Parallel Processing)।
          <br>&bull; <em>अत्याधुनिक हार्डवेयर:</em> क्वांटम कंप्यूटिंग (क्यूबिट्स / सुपरपोजिशन), नैनो-प्रौद्योगिकी एवं बायो-चिप्स।
          <br>&bull; <em>विशेषताएं:</em> प्राकृतिक भाषा प्रसंस्करण (NLP), वॉयस रिकग्निशन, रोबोटिक्स एवं सुपरकंप्यूटिंग।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Classification of Computers -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Classification of Computers by Mechanism, Size &amp; Purpose</span>
    <span class="lang-hi">3. कार्यप्रणाली, आकार एवं उद्देश्य के आधार पर कंप्यूटरों का वर्गीकरण</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. Classification by Mechanism / Technology (तकनीक आधारित):</strong>
          <br>&bull; <em>Analog Computers (एनालॉग कंप्यूटर):</em> Process continuous physical quantities (voltage, current, pressure, temperature, speed); measurements are plotted on dials/scales rather than discrete counts. Examples: Speedometer, Voltmeter, Mercury Thermometer, Seismograph.
          <br>&bull; <em>Digital Computers (डिजिटल कंप्यूटर):</em> Process discrete binary data (0s and 1s); perform high-precision arithmetic and logical operations. Examples: Desktops, Laptops, Calculators, Digital Watches.
          <br>&bull; <em>Hybrid Computers (हाइब्रिड कंप्यूटर):</em> Combine the speed of analog signal measurement with the high precision of digital calculation. Examples: Intensive Care Unit (ICU) patient monitors (measures heartbeat/blood pressure analogously, converts to digital numbers), Petrol Pump dispensers, Flight Simulators.</span>
        <span class="lang-hi"><strong>1. कार्यप्रणाली / तकनीक के आधार पर वर्गीकरण:</strong>
          <br>&bull; <em>एनालॉग कंप्यूटर:</em> भौतिक मात्राओं (तापमान, दाब, गति, वोल्टेज) के निरंतर परिवर्तनों को मापते हैं। उदाहरण: स्पीडोमीटर, साधारण थर्मामीटर, सिस्मोग्राफ।
          <br>&bull; <em>डिजिटल कंप्यूटर:</em> बाइनरी अंकों (0 और 1) पर कार्य करते हैं तथा गणितीय व तार्किक गणनाएं करते हैं। उदाहरण: डेस्कटॉप, लैपटॉप, स्मार्टफोन।
          <br>&bull; <em>हाइब्रिड कंप्यूटर:</em> एनालॉग और डिजिटल दोनों तकनीकों का मिश्रण; गति एनालॉग जैसी और सटीकता डिजिटल जैसी। उदाहरण: अस्पताल के ICU मॉनिटर (रक्तचाप/धड़कन एनालॉग में मापकर स्क्रीन पर डिजिटल संख्या में दिखाना), पेट्रोल पंप की मशीन।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Classification by Size, Speed &amp; Capacity (आकार व क्षमता आधारित):</strong>
          <br>&bull; <em>Microcomputer (माइक्रोकंप्यूटर):</em> Built around a single microprocessor chip; designed for individual single-user operation. Examples: PC, Desktop, Laptop, Tablet, Smartphone, Workstation.
          <br>&bull; <em>Minicomputer (मिनीकंप्यूटर):</em> Mid-sized multi-user systems supporting 4 to 200 simultaneous users; introduced in the 1960s (DEC PDP-8 was the 1st successful commercial minicomputer); used in university labs and mid-sized factories.
          <br>&bull; <em>Mainframe Computer (मेनफ्रेम कंप्यूटर):</em> Large-scale, highly reliable computers with massive I/O bandwidth capable of supporting thousands of simultaneous users and petabytes of transactional data. Examples: IBM zSeries, IBM System z16; used by Indian Railways IRCTC, Banking core systems, Airline reservations.
          <br>&bull; <em>Supercomputer (सुपरकंप्यूटर):</em> The fastest and most expensive computers on Earth designed for massive parallel numerical simulations. Performance measured in <strong>FLOPS (Floating Point Operations Per Second)</strong>.</span>
        <span class="lang-hi"><strong>2. आकार, गति एवं क्षमता के आधार पर वर्गीकरण:</strong>
          <br>&bull; <em>माइक्रोकंप्यूटर:</em> एकल माइक्रोप्रोसेसर पर आधारित एकल-उपयोगकर्ता (Single-user) सिस्टम। उदाहरण: PC, लैपटॉप, स्मार्टफोन, टैबलेट।
          <br>&bull; <em>मिनीकंप्यूटर:</em> मध्यम आकार के मल्टी-यूजर कंप्यूटर, जो एक साथ 4 से 200 उपयोगकर्ताओं को संभाल सकते हैं (DEC PDP-8 प्रथम सफल मिनीकंप्यूटर था)।
          <br>&bull; <em>मेनफ्रेम कंप्यूटर:</em> अत्यधिक शक्तिशाली, उच्च मेमोरी एवं I/O क्षमता वाले कंप्यूटर, जो एक साथ हजारों उपयोगकर्ताओं के भारी डेटा लेनदेन को संभालते हैं। उदाहरण: IBM zSeries (रेलवे आरक्षण, बैंकिंग, बीमा क्षेत्र)।
          <br>&bull; <em>सुपरकंप्यूटर:</em> विश्व में सर्वाधिक तेज गति, विशाल मेमोरी और समानांतर प्रसंस्करण क्षमता वाले कंप्यूटर; गति मापन: <strong>FLOPS (फ्लोटिंग प्वाइंट ऑपरेशंस प्रति सेकंड)</strong> में।</span>
      </li>
      <li>
        <span class="lang-en"><strong>3. Classification by Purpose (उद्देश्य आधारित):</strong>
          <br>&bull; <em>General Purpose Computers:</em> Designed to perform a wide variety of tasks (word processing, web browsing, gaming, accounting) by loading different application software.
          <br>&bull; <em>Special Purpose Computers:</em> Hardwired and programmed to perform a specific dedicated task (traffic light controllers, missile guidance systems, washing machine microcontrollers, MRI machines).</span>
        <span class="lang-hi"><strong>3. उद्देश्य के आधार पर वर्गीकरण:</strong>
          <br>&bull; <em>सामान्य उद्देशीय (General Purpose):</em> विभिन्न प्रकार के कार्यों (दस्तावेज़ निर्माण, वेब सर्फिंग, हिसाब-किताब) हेतु अनुकूलित कंप्यूटर।
          <br>&bull; <em>विशिष्ट उद्देशीय (Special Purpose):</em> किसी एक निश्चित कार्य हेतु समर्पित सिस्टम (मिसाइल नियंत्रण प्रणाली, मौसम राडार, वाशिंग मशीन या कार इंजन कंट्रोल यूनिट)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Supercomputing Architecture & Indian Supercomputers -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Supercomputing Architecture &amp; India's Supercomputing Odyssey</span>
    <span class="lang-hi">4. सुपरकंप्यूटिंग वास्तुकला एवं भारत का सुपरकंप्यूटर इतिहास</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Global Supercomputing Pioneers:</strong>
          <br>&bull; <strong>Seymour Cray:</strong> Renowned globally as the <strong>"Father of Supercomputing"</strong>.
          <br>&bull; <em>CDC 6600 (1964):</em> Recognized as the world's first successful supercomputer (designed by Seymour Cray at Control Data Corporation).
          <br>&bull; <em>Cray-1 (1976):</em> First commercially successful vector-processor supercomputer (distinctive C-shaped bench design).
          <br>&bull; <em>Frontier (USA - Oak Ridge National Lab):</em> World's first true <strong>Exascale Supercomputer</strong> (>1.1 ExaFLOPS), based on AMD EPYC processors.</span>
        <span class="lang-hi"><strong>वैश्विक सुपरकंप्यूटिंग के अग्रदूत:</strong>
          <br>&bull; <strong>सीमोर क्रे (Seymour Cray):</strong> <strong>"सुपरकंप्यूटर के पितामह"</strong> के रूप में विख्यात।
          <br>&bull; <em>CDC 6600 (1964):</em> विश्व का प्रथम सफल सुपरकंप्यूटर (कंट्रोल डेटा कॉर्पोरेशन में सीमोर क्रे द्वारा विकसित)।
          <br>&bull; <em>Cray-1 (1976):</em> प्रथम व्यावसायिक वेक्टर-प्रोसेसर सुपरकंप्यूटर (विशिष्ट C-आकार की बनावट)।
          <br>&bull; <em>फ्रंटियर (Frontier - अमेरिका):</em> विश्व का प्रथम <strong>एक्सास्केल (Exascale)</strong> सुपरकंप्यूटर (>1.1 एक्साफ्लॉप्स क्षमता)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>India's Supercomputing Milestones (C-DAC &amp; PARAM Series):</strong>
          <br>&bull; <strong>Birth of C-DAC (1988):</strong> When the US denied India the Cray X-MP supercomputer in 1987 under technology denial sanctions, the Government of India established <strong>C-DAC (Centre for Development of Advanced Computing)</strong> in Pune under the visionary leadership of <strong>Dr. Vijay P. Bhatkar ("Father of Indian Supercomputing")</strong>.
          <br>&bull; <strong>PARAM 8000 (1991):</strong> <strong>India's first indigenous supercomputer</strong> (built using parallel computing architecture with transputers, speed ~1 GFLOPS).
          <br>&bull; <strong>PARAM 10000 (1998):</strong> Scaled Indian supercomputing to 100 GigaFLOPS.
          <br>&bull; <strong>PARAM Yuva &amp; PARAM Yuva-II (2013):</strong> First Indian system to exceed 500 TeraFLOPS.</span>
        <span class="lang-hi"><strong>भारत के सुपरकंप्यूटर मील के पत्थर:</strong>
          <br>&bull; <strong>सी-डैक (C-DAC) की स्थापना (1988):</strong> जब 1987 में अमेरिका ने भारत को मौसम पूर्वानुमान हेतु 'क्रे एक्स-एमपी' सुपरकंप्यूटर देने से मना कर दिया, तब पुणे में C-DAC की स्थापना हुई, जिसके संस्थापक निदेशक <strong>डॉ. विजय पांडुरंग भटकर ("भारतीय सुपरकंप्यूटिंग के जनक")</strong> बने।
          <br>&bull; <strong>परम 8000 (PARAM 8000 - 1991):</strong> <strong>भारत का प्रथम स्वदेशी सुपरकंप्यूटर</strong> (गति: लगभग 1 गीगाफ्लॉप्स)।
          <br>&bull; <strong>परम 10000 (1998):</strong> 100 गीगाफ्लॉप्स क्षमता का विस्तार।
          <br>&bull; <strong>परम युवा-II (2013):</strong> 500 से अधिक टेराफ्लॉप्स क्षमता वाला भारतीय सुपरकंप्यूटर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>National Supercomputing Mission (NSM - 2015):</strong>
          <br>&bull; Jointly steered by DST (Department of Science &amp; Technology) and MeitY, implemented by C-DAC and IISc Bengaluru.
          <br>&bull; <strong>PARAM Shivay:</strong> First supercomputer assembled indigenously under NSM, inaugurated in 2019 at <strong>IIT (BHU) Varanasi, Uttar Pradesh</strong> (833 TeraFLOPS).
          <br>&bull; <strong>AIRAWAT (AI Research Analytics &amp; Knowledge Dissemination Platform):</strong> Installed at C-DAC Pune; ranked in the Global TOP500 supercomputers list as India's premier AI computing facility.
          <br>&bull; <strong>Pratyush (IITM Pune, 4.0 PetaFLOPS) &amp; Mihir (NCMRWF Noida, 2.8 PetaFLOPS):</strong> Dedicated weather and climate modeling supercomputers under the Ministry of Earth Sciences (MoES).</span>
        <span class="lang-hi"><strong>राष्ट्रीय सुपरकंप्यूटिंग मिशन (NSM - 2015):</strong>
          <br>&bull; विज्ञान और प्रौद्योगिकी विभाग (DST) तथा इलेक्ट्रॉनिक्स व आईटी मंत्रालय (MeitY) द्वारा संयुक्त रूप से संचालित; C-DAC एवं IISc द्वारा क्रियान्वित।
          <br>&bull; <strong>परम शिवाय (PARAM Shivay):</strong> NSM के तहत निर्मित प्रथम स्वदेशी सुपरकंप्यूटर, जिसका उद्घाटन 2019 में <strong>आईआईटी (बीएचयू) वाराणसी, उत्तर प्रदेश</strong> में किया गया (833 टेराफ्लॉप्स)।
          <br>&bull; <strong>ऐरावत (AIRAWAT):</strong> C-DAC पुणे में स्थापित भारत का सबसे तेज एआई (AI) सुपरकंप्यूटर; वैश्विक TOP500 सूची में शामिल।
          <br>&bull; <strong>प्रत्युष (IITM पुणे) एवं मिहिर (NCMRWF नोएडा, यूपी):</strong> पृथ्वी विज्ञान मंत्रालय के तहत समर्पित मौसम पूर्वानुमान सुपरकंप्यूटर।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Von Neumann Architecture & Stored Program Concept -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Von Neumann Architecture &amp; Stored-Program Concept</span>
    <span class="lang-hi">5. वॉन न्यूमैन वास्तुकला एवं संग्रहित प्रोग्राम संकल्पना</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>The Stored-Program Principle (1945 - John von Neumann):</strong>
          <br>&bull; Before von Neumann, computers were reprogrammed by physically rewiring cables and switches.
          <br>&bull; Von Neumann proposed that <strong>data and instructions (programs) share the same sequential memory space</strong> in binary form.</span>
        <span class="lang-hi"><strong>संग्रहित प्रोग्राम सिद्धांत (1945 - जॉन वॉन न्यूमैन):</strong>
          <br>&bull; वॉन न्यूमैन से पूर्व कंप्यूटरों को नया कार्य देने हेतु तारों और स्विचों को भौतिक रूप से बदलना पड़ता था।
          <br>&bull; वॉन न्यूमैन ने प्रतिपादित किया कि <strong>निर्देश (प्रोग्राम) एवं डेटा दोनों एक ही प्राथमिक मेमोरी में बाइनरी रूप में संग्रहित होने चाहिए</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Core Architectural Subsystems:</strong>
          <br>&bull; <em>1. Central Processing Unit (CPU):</em> The brain of the computer containing:
            <br>&nbsp;&nbsp;&bull; <strong>Arithmetic Logic Unit (ALU):</strong> Performs fundamental mathematical (+, -, *, /) and logical (AND, OR, NOT, comparisons) operations.
            <br>&nbsp;&nbsp;&bull; <strong>Control Unit (CU):</strong> Acts as the traffic cop; fetches instructions from memory, decodes them, and coordinates the flow of signals across all hardware.
            <br>&nbsp;&nbsp;&bull; <strong>Registers:</strong> High-speed temporary internal storage cells (PC - Program Counter, IR - Instruction Register, MAR, MDR, Accumulator).
          <br>&bull; <em>2. Main Memory (RAM):</em> Random-access linear sequence of addressable storage locations holding active instructions and operands.
          <br>&bull; <em>3. System Bus:</em> Set of parallel electrical wires connecting CPU, Memory, and I/O:
            <br>&nbsp;&nbsp;&bull; <strong>Data Bus (द्विदिशी / Bidirectional):</strong> Transports actual data bits between CPU, memory, and devices.
            <br>&nbsp;&nbsp;&bull; <strong>Address Bus (एकदिशी / Unidirectional):</strong> Carries memory/port addresses specified by CPU (width determines maximum RAM addressable: e.g., 32-bit bus = 2^32 = 4 GB RAM).
            <br>&nbsp;&nbsp;&bull; <strong>Control Bus (द्विदिशी / Bidirectional):</strong> Carries read/write timing and handshake control signals.</span>
        <span class="lang-hi"><strong>प्रमुख वास्तुकला घटक:</strong>
          <br>&bull; <em>1. सेंट्रल प्रोसेसिंग यूनिट (CPU):</em> कंप्यूटर का मस्तिष्क, जिसमें सम्मिलित हैं:
            <br>&nbsp;&nbsp;&bull; <strong>अंकगणितीय एवं तार्किक इकाई (ALU):</strong> सभी गणितीय एवं तार्किक गणनाएं निष्पादित करता है।
            <br>&nbsp;&nbsp;&bull; <strong>कंट्रोल यूनिट (CU):</strong> कंप्यूटर का तंत्रिका तंत्र; मेमोरी से निर्देश फेच करना, डिकोड करना तथा संकेतों का समन्वय करना।
            <br>&nbsp;&nbsp;&bull; <strong>रजिस्टर्स:</strong> CPU के अंदर स्थित तीव्रतम अल्पकालिक मेमोरी (प्रोग्राम काउंटर PC, एक्युमुलेटर, IR, MAR)।
          <br>&bull; <em>2. मुख्य मेमोरी (RAM):</em> एड्रेस योग्य बाइनरी मेमोरी, जहां सक्रिय प्रोग्राम और डेटा रखे जाते हैं।
          <br>&bull; <em>3. सिस्टम बस (System Bus):</em> सीपीयू, मेमोरी और इनपुट/आउटपुट को जोड़ने वाले तारों का समूह:
            <br>&nbsp;&nbsp;&bull; <strong>डेटा बस (द्विदिशी - Bidirectional):</strong> वास्तविक डेटा का आदान-प्रदान करता है।
            <br>&nbsp;&nbsp;&bull; <strong>एड्रेस बस (एकदिशी - Unidirectional):</strong> मेमोरी लोकेशन का पता सीपीयू से मेमोरी तक ले जाता है।
            <br>&nbsp;&nbsp;&bull; <strong>कंट्रोल बस:</strong> रीड/राइट एवं क्लॉक सिग्नलों का समन्वय करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Von Neumann Bottleneck:</strong>
          <br>&bull; Throughput restriction caused because the CPU and memory share a single common bus; CPU is forced to wait for sequential instruction and data fetches. Modern systems mitigate this using <strong>Cache Memory (L1, L2, L3)</strong>.</span>
        <span class="lang-hi"><strong>वॉन न्यूमैन बॉटलनेक:</strong>
          <br>&bull; डेटा और निर्देशों हेतु एक ही साझा बस होने के कारण सीपीयू को डेटा स्थानांतरण की प्रतीक्षा करनी पड़ती है, जिससे गति सीमित हो जाती है। इसे दूर करने हेतु आधुनिक कंप्यूटरों में <strong>कैश मेमोरी (L1, L2, L3)</strong> का प्रयोग किया जाता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Modern Applications & Digital Frameworks -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Modern Applications &amp; Digital Governance Frameworks</span>
    <span class="lang-hi">6. कंप्यूटर के आधुनिक अनुप्रयोग एवं डिजिटल गवर्नेंस प्रारूप</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Key Application Sectors:</strong>
          <br>&bull; <em>E-Governance:</em> Citizen-centric digital service delivery (e-District, DigiLocker, UMANG portal, Jan Samarth).
          <br>&bull; <em>Banking &amp; FinTech:</em> Core Banking Solutions (CBS), Automated Teller Machines (ATM), Real Time Gross Settlement (RTGS), National Electronic Funds Transfer (NEFT), Unified Payments Interface (UPI).
          <br>&bull; <em>Defense &amp; Space Research:</em> Radar tracking, ballistic missile trajectory calculations, satellite telemetry (ISRO Telemetry Tracking and Command Network - ISTRAC), drone autonomy.
          <br>&bull; <em>Healthcare &amp; Telemedicine:</em> Electronic Health Records (EHR), CT-Scan and MRI image reconstruction, robotic surgery, e-Sanjeevani portal.
          <br>&bull; <em>Weather &amp; Disaster Simulation:</em> Monsoon tracking, cyclone path prediction using numerical weather models on supercomputers (Pratyush/Mihir).</span>
        <span class="lang-hi"><strong>प्रमुख अनुप्रयोग क्षेत्र:</strong>
          <br>&bull; <em>ई-गवर्नेंस:</em> नागरिकों को पारदर्शी डिजिटल सेवाएं (ई-डिस्ट्रिक्ट पोर्टल, डिजिलॉकर, उमंग, जन समर्थ पोर्टल)।
          <br>&bull; <em>बैंकिंग एवं फिनटेक:</em> कोर बैंकिंग सॉल्यूशन (CBS), एटीएम, आरटीजीएस (RTGS), एनईएफटी (NEFT), यूपीआई (UPI)।
          <br>&bull; <em>रक्षा एवं अंतरिक्ष अनुसंधान:</em> मिसाइल मार्गदर्शन प्रणाली, रडार, उपग्रह टेलीमेट्री (इसरो ISTRAC), ड्रोन तकनीक।
          <br>&bull; <em>चिकित्सा एवं टेलीमेडिसिन:</em> सीटी स्कैन एवं एमआरआई इमेजिंग, रोबोटिक सर्जरी, ई-संजीवनी टेली-परामर्श।
          <br>&bull; <em>मौसम एवं आपदा प्रबंधन:</em> सुपरकंप्यूटरों (प्रत्युष व मिहिर) द्वारा चक्रवात एवं मानसूनी वर्षा का सटीक संख्यात्मक पूर्वानुमान।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master Comparison Table -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Comparison Matrix: Computer Generations at a Glance</span>
    <span class="lang-hi">7. कंप्यूटर पीढ़ियों की संपूर्ण तुलनात्मक सारणी</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Generation</span>
            <span class="lang-hi">पीढ़ी</span>
          </th>
          <th>
            <span class="lang-en">Switching Device</span>
            <span class="lang-hi">मुख्य घटक</span>
          </th>
          <th>
            <span class="lang-en">Primary Memory</span>
            <span class="lang-hi">प्राथमिक मेमोरी</span>
          </th>
          <th>
            <span class="lang-en">Languages &amp; OS</span>
            <span class="lang-hi">भाषा एवं OS</span>
          </th>
          <th>
            <span class="lang-en">Speed &amp; Hallmarks</span>
            <span class="lang-hi">गति एवं प्रमुख लक्षण</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en"><strong>1st Gen</strong> (1940-56)</span>
            <span class="lang-hi"><strong>प्रथम पीढ़ी</strong></span>
          </td>
          <td>
            <span class="lang-en">Vacuum Tubes</span>
            <span class="lang-hi">वैक्यूम ट्यूब</span>
          </td>
          <td>
            <span class="lang-en">Magnetic Drum</span>
            <span class="lang-hi">मैग्नेटिक ड्रम</span>
          </td>
          <td>
            <span class="lang-en">Machine &amp; Assembly; Batch OS</span>
            <span class="lang-hi">मशीन व असेंबली; बैच OS</span>
          </td>
          <td>
            <span class="lang-en">Milliseconds (10^-3 s); ENIAC, UNIVAC</span>
            <span class="lang-hi">मिलीसेकंड; ENIAC, UNIVAC</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>2nd Gen</strong> (1956-63)</span>
            <span class="lang-hi"><strong>द्वितीय पीढ़ी</strong></span>
          </td>
          <td>
            <span class="lang-en">Transistors</span>
            <span class="lang-hi">ट्रांजिस्टर</span>
          </td>
          <td>
            <span class="lang-en">Magnetic Core</span>
            <span class="lang-hi">मैग्नेटिक कोर</span>
          </td>
          <td>
            <span class="lang-en">FORTRAN, COBOL; Multiprogramming</span>
            <span class="lang-hi">फोरट्रान, कोबोल; मल्टीप्रोग्रामिंग</span>
          </td>
          <td>
            <span class="lang-en">Microseconds (10^-6 s); IBM 1401</span>
            <span class="lang-hi">माइक्रोसेकंड; IBM 1401</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>3rd Gen</strong> (1964-71)</span>
            <span class="lang-hi"><strong>तृतीय पीढ़ी</strong></span>
          </td>
          <td>
            <span class="lang-en">Integrated Circuits (SSI/MSI)</span>
            <span class="lang-hi">एकीकृत परिपथ (IC चिप)</span>
          </td>
          <td>
            <span class="lang-en">Semiconductor RAM</span>
            <span class="lang-hi">सेमीकंडक्टर रैम</span>
          </td>
          <td>
            <span class="lang-en">BASIC, Pascal; Time-sharing OS</span>
            <span class="lang-hi">बेसिक, पास्कल; टाइम शेयरिंग OS</span>
          </td>
          <td>
            <span class="lang-en">Nanoseconds (10^-9 s); Keyboards/Monitors</span>
            <span class="lang-hi">नैनोसेकंड; कीबोर्ड व मॉनिटर का आगमन</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>4th Gen</strong> (1971-Pres)</span>
            <span class="lang-hi"><strong>चतुर्थ पीढ़ी</strong></span>
          </td>
          <td>
            <span class="lang-en">Microprocessor (VLSI/ULSI)</span>
            <span class="lang-hi">माइक्रोप्रोसेसर (VLSI)</span>
          </td>
          <td>
            <span class="lang-en">DRAM, SRAM, SSD</span>
            <span class="lang-hi">DRAM, SRAM, SSD</span>
          </td>
          <td>
            <span class="lang-en">C, C++, Java, Python; GUI Windows, Linux</span>
            <span class="lang-hi">C, C++, जावा; GUI विंडोज, लिनक्स</span>
          </td>
          <td>
            <span class="lang-en">Picoseconds (10^-12 s); PCs, Laptops</span>
            <span class="lang-hi">पिकोसेकंड; पर्सनल कंप्यूटर (PC) क्रांति</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>5th Gen</strong> (Present-Fut)</span>
            <span class="lang-hi"><strong>पंचम पीढ़ी</strong></span>
          </td>
          <td>
            <span class="lang-en">ULSI, Bio-chips, Quantum</span>
            <span class="lang-hi">ULSI, क्वांटम, बायो-चिप्स</span>
          </td>
          <td>
            <span class="lang-en">Optical &amp; Cloud Storage</span>
            <span class="lang-hi">ऑप्टिकल एवं क्लाउड स्टोरेज</span>
          </td>
          <td>
            <span class="lang-en">Natural Language (AI/NLP); Neural Nets</span>
            <span class="lang-hi">प्राकृतिक भाषा (AI), न्यूरल नेटवर्क</span>
          </td>
          <td>
            <span class="lang-en">ExaFLOPS; Robotics, Quantum Computing</span>
            <span class="lang-hi">एक्साफ्लॉप्स; रोबोटिक्स, क्वांटम कंप्यूटिंग</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 9: Rapid Revision Matrix & UPSSSC Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">8. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Exam Question / Concept</span>
            <span class="lang-hi">परीक्षा प्रश्न / संकल्पना</span>
          </th>
          <th>
            <span class="lang-en">Exact Answer &amp; UPSSSC Exam Fact</span>
            <span class="lang-hi">सटीक उत्तर एवं महत्वपूर्ण तथ्य</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Father of Computer</span>
            <span class="lang-hi">कंप्यूटर के जनक (Father of Computer)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Charles Babbage</strong> (for Analytical Engine concept).</span>
            <span class="lang-hi"><strong>चार्ल्स बैबेज</strong> (एनालिटिकल इंजन की संकल्पना हेतु)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Computer Programmer</span>
            <span class="lang-hi">विश्व की प्रथम प्रोग्रामर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Lady Ada Lovelace</strong> (Augusta Ada Byron).</span>
            <span class="lang-hi"><strong>लेडी एडा लवलेस</strong> (अगस्टा एडा बायरन)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Stored-Program Concept Originator</span>
            <span class="lang-hi">संग्रहीत प्रोग्राम संकल्पना के प्रणेता</span>
          </td>
          <td>
            <span class="lang-en"><strong>John von Neumann</strong> (1945).</span>
            <span class="lang-hi"><strong>जॉन वॉन न्यूमैन</strong> (1945)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Electronic Digital Computer</span>
            <span class="lang-hi">प्रथम सामान्य उद्देशीय इलेक्ट्रॉनिक डिजिटल कंप्यूटर</span>
          </td>
          <td>
            <span class="lang-en"><strong>ENIAC</strong> (Eckert &amp; Mauchly, 1946).</span>
            <span class="lang-hi"><strong>ENIAC</strong> (एकर्ट एवं मौचली, 1946)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Commercial Computer</span>
            <span class="lang-hi">प्रथम व्यावसायिक कंप्यूटर</span>
          </td>
          <td>
            <span class="lang-en"><strong>UNIVAC-I</strong> (1951).</span>
            <span class="lang-hi"><strong>UNIVAC-I</strong> (1951)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Microprocessor in the World</span>
            <span class="lang-hi">विश्व का प्रथम माइक्रोप्रोसेसर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Intel 4004</strong> (1971, 4-bit).</span>
            <span class="lang-hi"><strong>इंटेल 4004</strong> (1971, 4-बिट)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Inventor of Integrated Circuit (IC)</span>
            <span class="lang-hi">इंटीग्रेटेड सर्किट (IC) के आविष्कारक</span>
          </td>
          <td>
            <span class="lang-en"><strong>Jack Kilby</strong> and <strong>Robert Noyce</strong> (1958-59).</span>
            <span class="lang-hi"><strong>जैक किल्बी</strong> एवं <strong>रॉबर्ट नॉयस</strong> (1958-59)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Father of Indian Supercomputing</span>
            <span class="lang-hi">भारतीय सुपरकंप्यूटिंग के जनक</span>
          </td>
          <td>
            <span class="lang-en"><strong>Dr. Vijay P. Bhatkar</strong> (developed PARAM 8000 in 1991).</span>
            <span class="lang-hi"><strong>डॉ. विजय पांडुरंग भटकर</strong> (1991 में परम 8000 का निर्माण)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Supercomputer Assembled under NSM</span>
            <span class="lang-hi">NSM के तहत स्थापित प्रथम सुपरकंप्यूटर</span>
          </td>
          <td>
            <span class="lang-en"><strong>PARAM Shivay</strong> at <strong>IIT (BHU) Varanasi, UP</strong> (2019).</span>
            <span class="lang-hi"><strong>परम शिवाय</strong>, <strong>IIT (BHU) वाराणसी, उप्र</strong> (2019)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Speed of Supercomputer Measured in</span>
            <span class="lang-hi">सुपरकंप्यूटर की गति का मापक</span>
          </td>
          <td>
            <span class="lang-en"><strong>FLOPS</strong> (Floating Point Operations Per Second).</span>
            <span class="lang-hi"><strong>FLOPS</strong> (फ्लोटिंग प्वाइंट ऑपरेशंस प्रति सेकंड)।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-computer", "history-introduction-and-application-of-computer", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_comp_history_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
