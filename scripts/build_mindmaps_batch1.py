import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# Ensure we have all 5 topics in one self-contained runner
pattern = re.compile(r'(<!--\s*Card 1:.*?-->.*?)(?=<!--\s*Card 2:)', re.DOTALL)

# ==========================================
# Topic 1: History, Introduction & Classification
# ==========================================
mm_t1 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: History, Evolution &amp; Classification of Computers</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: कंप्यूटर का इतिहास, क्रमिक विकास, पीढ़ियाँ एवं वर्गीकरण</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Ancient Calculating Devices • Five Generations • von Neumann Architecture • Supercomputing &amp; UP Milestones</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • प्राचीन गणना यंत्र • 5 पीढ़ियाँ • वॉन न्यूमैन वास्तुकला • सुपरकंप्यूटिंग व उप्र मील के पत्थर</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-desktop"></i>
            <span class="lang-en">Computer Architecture, Evolution &amp; Generations</span>
            <span class="lang-hi">कंप्यूटर वास्तुकला, ऐतिहासिक विकास एवं पीढ़ियाँ</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Pre-Electronic & Mechanical Era -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-history" style="color: #059669;"></i>
                    <span class="lang-en">1. Manual &amp; Mechanical Era</span>
                    <span class="lang-hi">1. हस्तचालित एवं यांत्रिक गणना युग</span>
                </h4>
                <span class="mindmap-node-tag">~3000 BCE – 1890 CE</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Pioneering Devices &amp; Inventors</span>
                        <span class="lang-hi">अग्रणी यंत्र एवं उनके आविष्कारक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Abacus</strong> (China, ~3000 BCE)</span>
                        <span class="mindmap-chip"><strong>Napier's Bones</strong> (1617, John Napier)</span>
                        <span class="mindmap-chip"><strong>Pascaline</strong> (1642, Blaise Pascal)</span>
                        <span class="mindmap-chip"><strong>Stepped Reckoner</strong> (1673, Leibniz)</span>
                        <span class="mindmap-chip"><strong>Jacquard Loom</strong> (1804, Punched Cards)</span>
                        <span class="mindmap-chip"><strong>Difference Engine</strong> (1822, Babbage)</span>
                        <span class="mindmap-chip"><strong>Analytical Engine</strong> (1837, Babbage)</span>
                        <span class="mindmap-chip"><strong>Tabulating Machine</strong> (1890, Hollerith)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Milestones &amp; Architectural Concepts</span>
                        <span class="lang-hi">प्रमुख मील के पत्थर एवं वैचारिक सिद्धांत</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Abacus:</strong> Earliest mechanical device for bead-based arithmetic calculation (Heaven and Earth beads on rods).</span>
                            <span class="lang-hi"><strong>अबेकस:</strong> मोतियों और छड़ों पर आधारित विश्व का प्राचीनतम यांत्रिक गणना यंत्र (स्वर्ग और पृथ्वी मोती)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Napier's Bones (1617):</strong> Invented by John Napier using carved ivory rods; used for multiplication and division using rabdology. Also invented logarithms.</span>
                            <span class="lang-hi"><strong>नेपियर्स बोन्स (1617):</strong> जॉन नेपियर द्वारा हाथीदांत की छड़ों से निर्मित; गुणन व भाग हेतु प्रयुक्त (रैब्डोलॉजी सिद्धांत)। इन्होंने लघुगणक (लॉग) का भी आविष्कार किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Pascaline (1642):</strong> Blaise Pascal created the first mechanical adding machine using geared toothed wheels; performed addition and subtraction (odometer principle).</span>
                            <span class="lang-hi"><strong>पास्कलाइन (1642):</strong> ब्लेज़ पास्कल द्वारा निर्मित विश्व का पहला यांत्रिक कैलकुलेटर; दांतेदार पहियों और गियर्स पर आधारित, जोड़ व घटाव में सक्षम।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Leibniz Stepped Reckoner (1673):</strong> Gottfried Wilhelm Leibniz extended Pascal's machine to multiply, divide, and extract square roots; promoted binary numbering.</span>
                            <span class="lang-hi"><strong>लाइबनिट्ज़ रेकनर (1673):</strong> गॉटफ्रीड लाइबनिट्ज़ द्वारा निर्मित; जोड़-घटाव के साथ गुणन, भाग व वर्गमूल निकालने में सक्षम; द्विआधारी (बाइनरी) पद्धति के समर्थक।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Charles Babbage (Father of Computer):</strong> Designed Difference Engine (1822) for polynomial tables, and Analytical Engine (1837) with input, store (memory), mill (CPU), and output.</span>
                            <span class="lang-hi"><strong>चार्ल्स बैबेज (कंप्यूटर के जनक):</strong> 1822 में डिफरेंस इंजन तथा 1837 में एनालिटिकल इंजन की रूपरेखा बनाई जिसमें इनपुट, स्टोर (मेमोरी), मिल (CPU) और आउटपुट की आधुनिक संरचना थी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lady Ada Lovelace:</strong> World's first computer programmer; wrote algorithm for Analytical Engine to compute Bernoulli numbers.</span>
                            <span class="lang-hi"><strong>लेडी एडा लवलेस:</strong> विश्व की प्रथम कंप्यूटर प्रोग्रामर; एनालिटिकल इंजन हेतु बर्नौली संख्याओं की गणना करने वाला पहला एल्गोरिदम लिखा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Herman Hollerith:</strong> Developed punched-card Tabulating Machine for 1890 US Census; founded Tabulating Machine Co. (renamed IBM in 1924).</span>
                            <span class="lang-hi"><strong>हर्मन होलेरिथ:</strong> 1890 की अमेरिकी जनगणना हेतु पंचकार्ड-आधारित टैबुलेटिंग मशीन बनाई; टैबुलेटिंग मशीन कंपनी की स्थापना की (जो 1924 में IBM बनी)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Charles Babbage is "Father of Computer"; Ada Lovelace is "First Programmer"; Hollerith punched cards were 80-column standard.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> चार्ल्स बैबेज को "कंप्यूटर का पिता" तथा एडा लवलेस को "प्रथम प्रोग्रामर" कहा जाता है; होलेरिथ के पंचकार्ड 80-कॉलम मानक के थे।</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Electronic Dawn & von Neumann Architecture -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microchip" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Electronic Pioneers &amp; Architecture</span>
                    <span class="lang-hi">2. इलेक्ट्रॉनिक कंप्यूटर का उदय व वास्तुकला</span>
                </h4>
                <span class="mindmap-node-tag">1940 – 1952</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Early Electronic Computers</span>
                        <span class="lang-hi">प्रारंभिक इलेक्ट्रॉनिक कंप्यूटर</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Z3</strong> (1941, Konrad Zuse)</span>
                        <span class="mindmap-chip"><strong>ABC</strong> (1942, Atanasoff-Berry)</span>
                        <span class="mindmap-chip"><strong>Colossus</strong> (1943, Bletchley Park)</span>
                        <span class="mindmap-chip"><strong>ENIAC</strong> (1946, Mauchly &amp; Eckert)</span>
                        <span class="mindmap-chip"><strong>EDVAC</strong> (1949, von Neumann)</span>
                        <span class="mindmap-chip"><strong>EDSAC</strong> (1949, Maurice Wilkes)</span>
                        <span class="mindmap-chip"><strong>UNIVAC I</strong> (1951, 1st Commercial)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Milestones &amp; Architectural Breakthroughs</span>
                        <span class="lang-hi">प्रमुख मील के पत्थर एवं तकनीकी सफलताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ABC (1942):</strong> Atanasoff-Berry Computer was first electronic digital calculating device, using vacuum tubes and regenerative capacitor drum memory.</span>
                            <span class="lang-hi"><strong>ABC (1942):</strong> अटानासॉफ-बेरी कंप्यूटर पहला स्वचालित इलेक्ट्रॉनिक डिजिटल उपकरण था, जिसमें वैक्यूम ट्यूब और कैपेसिटर ड्रम मेमोरी का प्रयोग हुआ।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ENIAC (1946):</strong> First general-purpose electronic digital computer by J. Presper Eckert &amp; John Mauchly at Univ. of Pennsylvania; contained ~18,000 vacuum tubes, weighed 30 tons, used decimal arithmetic.</span>
                            <span class="lang-hi"><strong>ENIAC (1946):</strong> एकर्ट एवं मॉचली द्वारा निर्मित पहला पूर्ण इलेक्ट्रॉनिक सामान्य-उद्देश्यीय डिजिटल कंप्यूटर; 18,000 वैक्यूम ट्यूब, 30 टन वजन, दशमलव प्रणाली पर आधारित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>John von Neumann Architecture (1945):</strong> Stored-program concept where data and program instructions share same physical memory. Core components: CPU (ALU + Control Unit + Registers), Memory, Input/Output, System Bus.</span>
                            <span class="lang-hi"><strong>वॉन न्यूमैन वास्तुकला (1945):</strong> स्टोर्ड-प्रोग्राम सिद्धांत जिसमें डेटा और प्रोग्राम निर्देश एक ही मेमोरी में संग्रहीत होते हैं। घटक: CPU (ALU + CU + रजिस्टर्स), मेमोरी, I/O एवं सिस्टम बस।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>EDSAC &amp; EDVAC (1949):</strong> EDSAC (Maurice Wilkes, Cambridge) was the first practical stored-program computer. EDVAC introduced binary representation for stored programs.</span>
                            <span class="lang-hi"><strong>EDSAC व EDVAC (1949):</strong> EDSAC (कैम्ब्रिज वि.वि.) पहला व्यावहारिक स्टोर्ड-प्रोग्राम कंप्यूटर था। EDVAC ने द्विआधारी (बाइनरी) स्टोर्ड-प्रोग्राम को पूर्णतः लागू किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UNIVAC I (1951):</strong> Universal Automatic Computer was first commercially available general-purpose computer, built for US Census Bureau by Remington Rand.</span>
                            <span class="lang-hi"><strong>UNIVAC I (1951):</strong> प्रथम व्यावसायिक रूप से उपलब्ध सामान्य-उद्देश्यीय कंप्यूटर; रेमिंगटन रैंड द्वारा अमेरिकी जनगणना ब्यूरो हेतु निर्मित।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> ENIAC used decimal; EDVAC introduced binary stored program; von Neumann architecture is the foundation of all modern computers.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ENIAC दशमलव प्रणाली पर आधारित था; EDVAC ने बाइनरी स्टोर्ड-प्रोग्राम दिया; आधुनिक कंप्यूटर वॉन न्यूमैन मॉडल पर ही कार्य करते हैं।</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: The Five Computer Generations -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-sitemap" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Five Computer Generations</span>
                    <span class="lang-hi">3. कंप्यूटर की पाँच पीढ़ियाँ</span>
                </h4>
                <span class="mindmap-node-tag">1940 – Present &amp; Future</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Hardware Technology Matrix</span>
                        <span class="lang-hi">मुख्य हार्डवेयर तकनीक मैट्रिक्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1st Gen:</strong> Vacuum Tubes</span>
                        <span class="mindmap-chip"><strong>2nd Gen:</strong> Transistors</span>
                        <span class="mindmap-chip"><strong>3rd Gen:</strong> IC (SSI / MSI)</span>
                        <span class="mindmap-chip"><strong>4th Gen:</strong> VLSI Microprocessor</span>
                        <span class="mindmap-chip"><strong>5th Gen:</strong> ULSI, AI &amp; Quantum</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Generation Breakdown &amp; Defining Features</span>
                        <span class="lang-hi">पीढ़ीवार विभाजन एवं प्रमुख विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1st Gen (1940-1956):</strong> Vacuum Tubes (Thermionic valves), Magnetic drums for memory; Machine Language (0/1); massive size, enormous power &amp; heat. Examples: ENIAC, EDVAC, UNIVAC I, IBM 701.</span>
                            <span class="lang-hi"><strong>प्रथम पीढ़ी (1940-1956):</strong> वैक्यूम ट्यूब (थर्मिओनिक वाल्व), मैग्नेटिक ड्रम मेमोरी; मशीनी भाषा (0/1); भारी आकार, अत्यधिक विद्युत व ऊष्मा उत्सर्जन। उदाहरण: ENIAC, UNIVAC I, IBM 701।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2nd Gen (1956-1963):</strong> Transistors (invented 1947 by Bardeen, Brattain, Shockley at Bell Labs); Magnetic core memory; Assembly language &amp; early HLLs (FORTRAN 1957 by John Backus, COBOL 1959 by Grace Hopper). Examples: IBM 1401, CDC 1604.</span>
                            <span class="lang-hi"><strong>द्वितीय पीढ़ी (1956-1963):</strong> ट्रांजिस्टर (1947, बेल लैब्स); मैग्नेटिक कोर मेमोरी; असेंबली भाषा एवं प्रारंभिक उच्चस्तरीय भाषाएं (FORTRAN 1957, COBOL 1959)। उदाहरण: IBM 1401, CDC 1604।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3rd Gen (1964-1971):</strong> Integrated Circuits (IC - Jack Kilby 1958 &amp; Robert Noyce 1959); SSI &amp; MSI silicon chips; Time-sharing OS, monitors and keyboards replace punched cards; BASIC (1964), PASCAL. Examples: IBM System/360, PDP-8.</span>
                            <span class="lang-hi"><strong>तृतीय पीढ़ी (1964-1971):</strong> एकीकृत परिपथ (IC - जैक किल्बी 1958 व रॉबर्ट नॉयस); सिलिकॉन चिप्स (SSI/MSI); टाइम-शेयरिंग OS, मॉनिटर व कीबोर्ड का आगमन; BASIC, PASCAL। उदाहरण: IBM System/360, PDP-8।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>4th Gen (1971-Present):</strong> VLSI / LSI Microprocessors (Intel 4004 in 1971 - 4-bit, Ted Hoff); Semiconductor RAM/ROM; Personal Computers (Altair 8800, Apple II, IBM PC 1981); GUI, C language (1972, Dennis Ritchie), Internet.</span>
                            <span class="lang-hi"><strong>चतुर्थ पीढ़ी (1971-वर्तमान):</strong> VLSI माइक्रोप्रोसेसर (इंटेल 4004 - 1971, टेड हॉफ); सेमीकंडक्टर रैम/रोम; पर्सनल कंप्यूटर (IBM PC 1981, Apple II); GUI, सी भाषा (1972, डेनिस रिची), इंटरनेट क्रांति।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>5th Gen (Present &amp; Future):</strong> ULSI (Ultra Large Scale Integration), Multi-core parallel processors, Artificial Intelligence (AI), Machine Learning, Natural Language Processing (NLP), Quantum Computing, Superconductors.</span>
                            <span class="lang-hi"><strong>पंचम पीढ़ी (वर्तमान व भविष्य):</strong> ULSI तकनीक, समानांतर प्रोसेसिंग, कृत्रिम बुद्धिमत्ता (AI), मशीन लर्निंग, नेचुरल लैंग्वेज प्रोसेसिंग (NLP), क्वांटम कंप्यूटिंग एवं सुपरकंडक्टर्स।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Transistor inventor: Shockley, Bardeen, Brattain (Nobel 1956). IC inventor: Jack Kilby (Nobel 2000). First Microprocessor: Intel 4004 (1971).</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ट्रांजिस्टर खोज: शॉकले, बारडीन, ब्रैटन (1956 नोबेल)। IC खोज: जैक किल्बी (2000 नोबेल)। विश्व का पहला माइक्रोप्रोसेसर: इंटेल 4004 (1971)।</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Classification by Size, Purpose & Signal -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cubes" style="color: #d97706;"></i>
                    <span class="lang-en">4. Classification of Computers</span>
                    <span class="lang-hi">4. कंप्यूटरों का संपूर्ण वर्गीकरण</span>
                </h4>
                <span class="mindmap-node-tag">3 Dimensions</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Categories &amp; Taxonomies</span>
                        <span class="lang-hi">प्रमुख श्रेणियां एवं वर्गीकरण आधार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>By Signal:</strong> Analog, Digital, Hybrid</span>
                        <span class="mindmap-chip"><strong>By Size:</strong> Micro, Mini, Mainframe, Super</span>
                        <span class="mindmap-chip"><strong>By Purpose:</strong> General, Special / Embedded</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Detailed Functional Differences</span>
                        <span class="lang-hi">विस्तृत कार्यात्मक अंतर एवं अनुप्रयोग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Analog Computers:</strong> Process continuous physical data (voltage, pressure, temperature, speed) without discrete conversion. Examples: Speedometer, traditional thermometer, slide rule.</span>
                            <span class="lang-hi"><strong>एनालॉग कंप्यूटर:</strong> भौतिक राशियों (दाब, तापमान, वोल्टेज, गति) के सतत प्रवाह को मापते हैं। उदाहरण: स्पीडोमीटर, पारे का थर्मामीटर, वोल्टमीटर।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Digital Computers:</strong> Process discrete binary digits (0 and 1); highly accurate, flexible, and programmable. Used for mathematical, business, and general computation.</span>
                            <span class="lang-hi"><strong>डिजिटल कंप्यूटर:</strong> असतत द्विआधारी अंकों (0 और 1) पर कार्य करते हैं; उच्च परिशुद्धता, तीव्र गति तथा बहुउद्देशीय। आधुनिक PC, लैपटॉप, स्मार्टफोन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hybrid Computers:</strong> Combines best features of analog (speed) and digital (precision); accepts continuous analog input, converts to digital for processing. Examples: Intensive Care Unit (ICU) patient monitors, ECG machines, petrol pump meters.</span>
                            <span class="lang-hi"><strong>हाइब्रिड कंप्यूटर:</strong> एनालॉग (तीव्र गति) और डिजिटल (परिशुद्धता) का समन्वय; एनालॉग इनपुट को डिजिटल में बदलकर प्रोसेस करता है। उदाहरण: ICU मॉनिटर, ईसीजी (ECG) मशीन, पेट्रोल पंप मीटर।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Microcomputers:</strong> Single microprocessor chip CPU; personal computers, laptops, notebooks, tablets, smartphones, workstations.</span>
                            <span class="lang-hi"><strong>माइक्रोकंप्यूटर:</strong> एकल माइक्रोप्रोसेसर चिप पर आधारित; डेस्कटॉप PC, लैपटॉप, टैबलेट, स्मार्टफोन, वर्कस्टेशन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Minicomputers:</strong> Mid-sized multi-user systems supporting 4 to 200 users simultaneously; PDP-11, VAX, IBM AS/400.</span>
                            <span class="lang-hi"><strong>मिनीकंप्यूटर:</strong> मध्यम आकार के कंप्यूटर जो एक साथ 4 से 200 उपयोगकर्ताओं को सपोर्ट करते हैं; PDP-11, VAX, IBM AS/400।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mainframe Computers:</strong> Massive multi-processor systems with massive I/O bandwidth, fault tolerance, transaction processing in banking, insurance, railways; IBM Z-Series.</span>
                            <span class="lang-hi"><strong>मेनफ्रेम कंप्यूटर:</strong> अत्यधिक शक्तिशाली, विशाल I/O क्षमता; बैंकिंग, रेलवे आरक्षण, बीमा में लाखों लेनदेन संभालने वाले बहु-उपयोगकर्ता सर्वर; IBM Z-सीरीज।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> ICU monitors and petrol dispensing pumps are classic examples of Hybrid Computers frequently asked in UP exams!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> पेट्रोल पंप मशीन एवं अस्पताल का ICU मॉनिटर हाइब्रिड कंप्यूटर के सबसे लोकप्रिय परीक्षा उदाहरण हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Supercomputing Milestones & India -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-bolt" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Supercomputing &amp; India</span>
                    <span class="lang-hi">5. सुपरकंप्यूटिंग एवं भारत की उपलब्धियां</span>
                </h4>
                <span class="mindmap-node-tag">FLOPS &amp; NSM</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Key Supercomputing Names</span>
                        <span class="lang-hi">प्रमुख सुपरकंप्यूटर एवं व्यक्तित्व</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>CDC 6600</strong> (1964, Seymour Cray)</span>
                        <span class="mindmap-chip"><strong>CRAY-1</strong> (1976, Vector Arch)</span>
                        <span class="mindmap-chip"><strong>Frontier</strong> (USA, Exascale)</span>
                        <span class="mindmap-chip"><strong>PARAM 8000</strong> (1991, C-DAC)</span>
                        <span class="mindmap-chip"><strong>Dr. Vijay Bhatkar</strong> (Father in India)</span>
                        <span class="mindmap-chip"><strong>AIRAWAT</strong> (C-DAC Pune, AI)</span>
                        <span class="mindmap-chip"><strong>PARAM Shivay</strong> (IIT BHU, UP)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Milestones &amp; Speed Metrics</span>
                        <span class="lang-hi">प्रमुख मील के पत्थर एवं गति मापन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Supercomputer Definition &amp; Metric:</strong> Extremely fast parallel computing system designed for complex simulations; performance measured in FLOPS (Floating Point Operations Per Second - TeraFLOPS, PetaFLOPS, ExaFLOPS).</span>
                            <span class="lang-hi"><strong>सुपरकंप्यूटर परिभाषा व मापन:</strong> समानांतर प्रोसेसिंग पर आधारित जटिल वैज्ञानिक गणना प्रणाली; गति FLOPS (फ्लोटिंग प्वाइंट ऑपरेशंस पर सेकंड) में मापी जाती है (टेराफ्लॉप्स, पेटाफ्लॉप्स, एक्सफ्लॉप्स)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Seymour Cray (Father of Supercomputing):</strong> Designed CDC 6600 (1964, first commercial supercomputer) and CRAY-1 (1976, vector processor architecture).</span>
                            <span class="lang-hi"><strong>सीमोर क्रे (सुपरकंप्यूटिंग के पिता):</strong> 1964 में CDC 6600 (विश्व का पहला सुपरकंप्यूटर) तथा 1976 में वेक्टर आर्किटेक्चर वाला प्रसिद्ध CRAY-1 डिजाइन किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>India's Supercomputing Genesis (PARAM 8000):</strong> Developed in 1991 by C-DAC (Centre for Development of Advanced Computing, Pune) led by Dr. Vijay Bhatkar after USA denied Cray X-MP export to India.</span>
                            <span class="lang-hi"><strong>भारत में सुपरकंप्यूटिंग (परम 8000):</strong> अमेरिका द्वारा क्रे X-MP देने से इनकार के बाद डॉ. विजय भटकर के नेतृत्व में C-DAC पुणे ने 1991 में स्वदेशी 'परम 8000' विकसित किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Supercomputing Mission (NSM):</strong> Launched in 2015 jointly by DST &amp; MeitY, implemented by C-DAC &amp; IISc Bangalore to build national supercomputing grid of 70+ high-performance systems.</span>
                            <span class="lang-hi"><strong>राष्ट्रीय सुपरकंप्यूटिंग मिशन (NSM):</strong> 2015 में DST और MeitY द्वारा शुरू; C-DAC एवं IISc बैंगलोर द्वारा क्रियान्वित; देश भर में 70+ सुपरकंप्यूटरों का ग्रिड स्थापित करना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Notable Indian Supercomputers:</strong> AIRAWAT (C-DAC Pune, AI supercomputer ranked in global Top500), Pratyush (IITM Pune, weather), Mihir (NCMRWF Noida, weather), PARAM Siddhi-AI, PARAM Pravega (IISc).</span>
                            <span class="lang-hi"><strong>भारत के प्रमुख सुपरकंप्यूटर:</strong> ऐरावत (C-DAC पुणे, AI आधारित Top500 में शामिल), प्रत्यूष (IITM पुणे), मिहिर (NCMRWF नोएडा), परम सिद्धि-AI, परम प्रवेगा (IISc बैंगलोर)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Dr. Vijay Bhatkar is "Father of Indian Supercomputing"; PARAM 8000 was launched in 1991; PARAM Shivay was installed at IIT BHU (Varanasi, UP) under NSM!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> डॉ. विजय भटकर "भारतीय सुपरकंप्यूटिंग के पिता" हैं; 'परम 8000' 1991 में बना; NSM के तहत पहला सुपरकंप्यूटर 'परम शिवाय' IIT BHU (वाराणसी, उप्र) में स्थापित हुआ!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Architecture, Ecosystem & UP State Context -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-network-wired" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Architecture &amp; UP Applications</span>
                    <span class="lang-hi">6. वास्तुकला, अनुप्रयोग एवं उप्र संदर्भ</span>
                </h4>
                <span class="mindmap-node-tag">E-Governance &amp; IT</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Architectural Blocks</span>
                        <span class="lang-hi">वास्तुकला के मूल घटक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>CPU</strong> (ALU + CU + Registers)</span>
                        <span class="mindmap-chip"><strong>Memory</strong> (Primary RAM/ROM &amp; Cache)</span>
                        <span class="mindmap-chip"><strong>System Bus</strong> (Data, Address, Control)</span>
                        <span class="mindmap-chip"><strong>I/O Units</strong> (Peripherals)</span>
                        <span class="mindmap-chip"><strong>IPOS Cycle</strong> (Input-Process-Output-Store)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Application Domains &amp; UP State Initiatives</span>
                        <span class="lang-hi">अनुप्रयोग क्षेत्र एवं उत्तर प्रदेश की पहल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Basic Computer Operations (IPOS):</strong> Input (accepts raw data) -> Process (manipulates data via ALU/CU) -> Output (presents meaningful information) -> Storage (retains data in memory/disk).</span>
                            <span class="lang-hi"><strong>बुनियादी कंप्यूटर चक्र (IPOS):</strong> इनपुट (कच्चा डेटा ग्रहण) -> प्रोसेसिंग (ALU/CU द्वारा गणना) -> आउटपुट (सूचना प्रदर्शन) -> स्टोरेज (मेमोरी/डिस्क में संचयन)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>System Bus Functions:</strong> Address Bus (unidirectional, specifies memory location), Data Bus (bidirectional, carries data words), Control Bus (carries read/write and timing pulses).</span>
                            <span class="lang-hi"><strong>सिस्टम बस के कार्य:</strong> एड्रेस बस (एकदिशीय, मेमोरी पता ले जाती है), डेटा बस (द्विदिशीय, डेटा स्थानांतरित करती है), कंट्रोल बस (नियंत्रण व टाइमिंग संकेत)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP e-District &amp; Citizen Services:</strong> Computerized delivery of caste, income, domicile, and birth certificates across all 75 districts via Common Service Centres (CSCs).</span>
                            <span class="lang-hi"><strong>उप्र ई-डिस्ट्रिक्ट एवं नागरिक सेवाएं:</strong> जन सेवा केंद्रों (CSC) के माध्यम से राज्य के सभी 75 जिलों में जाति, आय, निवास व जन्म प्रमाण पत्र का कंप्यूटरीकृत वितरण।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Bhulekh (Land Records):</strong> Complete computerization and online access of Khatauni/Khasra to eliminate rural land disputes and corruption.</span>
                            <span class="lang-hi"><strong>उप्र भूलेख (खतौनी डिजिटलीकरण):</strong> भूमि विवादों एवं भ्रष्टाचार के खात्मे हेतु राज्य के सभी खसरा/खतौनी भू-अभिलेखों का पूर्ण कंप्यूटरीकरण व ऑनलाइन उपलब्धता।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow AI City &amp; IT Parks:</strong> Uttar Pradesh developing India's first designated AI City in Lucknow (Nadarganj) and IT Parks across Tier-2 cities (Kanpur, Gorakhpur, Varanasi, Meerut, Bareilly, Agra).</span>
                            <span class="lang-hi"><strong>लखनऊ AI सिटी एवं IT पार्क:</strong> लखनऊ के नादरगंज में भारत की पहली AI सिटी तथा कानपुर, गोरखपुर, वाराणसी, मेरठ, बरेली व आगरा में IT पार्कों का विकास।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IPOS stands for Input-Process-Output-Storage; Address Bus is unidirectional; Data Bus is bidirectional; UP Bhulekh digitized state land records.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> IPOS का अर्थ Input-Process-Output-Storage है; एड्रेस बस एकदिशीय तथा डेटा बस द्विदिशीय होती है; उप्र भूलेख ने भूमि अभिलेखों का पूर्ण डिजिटलीकरण किया।</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''

# ==========================================
# Topic 2: Hardware and Software
# ==========================================
mm_t2 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Computer Hardware &amp; Software Architecture</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: कंप्यूटर हार्डवेयर एवं सॉफ्टवेयर वास्तुकला</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Architectural Flow • CPU Internal Units • Motherboard &amp; BIOS/UEFI • Memory Hierarchy (SRAM/DRAM/ROM) • Secondary Storage • System &amp; Application Software</span>
            <span class="lang-hi">समग्र वास्तुकला संकल्पना प्रवाह • CPU आंतरिक इकाइयाँ • मदरबोर्ड एवं BIOS/UEFI • मेमोरी पदानुक्रम • द्वितीयक स्टोरेज • सिस्टम एवं एप्लिकेशन सॉफ्टवेयर</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-server"></i>
            <span class="lang-en">Computer Hardware, Software &amp; Memory Ecosystem</span>
            <span class="lang-hi">कंप्यूटर हार्डवेयर, सॉफ्टवेयर एवं मेमोरी पारिस्थितिकी</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: CPU Architecture & Registers -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microchip" style="color: #059669;"></i>
                    <span class="lang-en">1. CPU Architecture &amp; Execution</span>
                    <span class="lang-hi">1. CPU वास्तुकला, घटक एवं रजिस्टर्स</span>
                </h4>
                <span class="mindmap-node-tag">ALU • CU • Registers</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Internal CPU Elements</span>
                        <span class="lang-hi">CPU के मुख्य आंतरिक घटक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>ALU</strong> (Arithmetic &amp; Logic)</span>
                        <span class="mindmap-chip"><strong>CU</strong> (Control Unit / Traffic Cop)</span>
                        <span class="mindmap-chip"><strong>PC</strong> (Program Counter)</span>
                        <span class="mindmap-chip"><strong>IR</strong> (Instruction Register)</span>
                        <span class="mindmap-chip"><strong>AC</strong> (Accumulator)</span>
                        <span class="mindmap-chip"><strong>MAR &amp; MDR</strong> (Memory Registers)</span>
                        <span class="mindmap-chip"><strong>Clock Speed</strong> (GHz / MHz)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Functional Operations &amp; Machine Cycle</span>
                        <span class="lang-hi">कार्यात्मक संचालन एवं मशीन चक्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Arithmetic Logic Unit (ALU):</strong> Performs fundamental arithmetic (+, -, *, /) and logical comparisons (AND, OR, NOT, =, &lt;, &gt;); results stored in Accumulator.</span>
                            <span class="lang-hi"><strong>अंकगणितीय एवं तार्किक इकाई (ALU):</strong> मूलभूत अंकगणित (+, -, *, /) तथा तार्किक तुलनाएं (AND, OR, NOT, =, &lt;, &gt;) निष्पादित करती है; परिणाम एक्युमुलेटर में जाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Control Unit (CU - "Brain/Supervisor"):</strong> Directs the entire computer operation, fetches instructions, decodes opcodes, generates control signals, and manages timing.</span>
                            <span class="lang-hi"><strong>कंट्रोल यूनिट (CU - "कंप्यूटर का प्रबंधक"):</strong> कंप्यूटर के समस्त कार्यों का समन्वय करती है; निर्देशों को फेच करना, डिकोड करना तथा कंट्रोल सिग्नल जारी करना इसका कार्य है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>CPU Registers (Fastest Memory):</strong> High-speed temporary memory inside the CPU. <strong>Program Counter (PC):</strong> holds memory address of the NEXT instruction to execute. <strong>Instruction Register (IR):</strong> holds current instruction being decoded. <strong>MAR:</strong> holds memory address to read/write. <strong>MDR/MBR:</strong> holds actual data word read from/written to memory.</span>
                            <span class="lang-hi"><strong>CPU रजिस्टर्स (तीव्रतम मेमोरी):</strong> CPU के भीतर अति-उच्च गति की अस्थायी मेमोरी। <strong>PC:</strong> निष्पादित होने वाले अगले निर्देश का पता रखता है। <strong>IR:</strong> वर्तमान निर्देश को रखता है। <strong>MAR:</strong> मेमोरी पता तथा <strong>MDR:</strong> मेमोरी से पढ़ा या लिखा जाने वाला वास्तविक डेटा रखता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Machine Cycle (Instruction Cycle):</strong> Fetch (from RAM to CPU) -> Decode (by CU) -> Execute (by ALU) -> Store (result written to register/RAM). Controlled by system clock.</span>
                            <span class="lang-hi"><strong>मशीन चक्र (निर्देश चक्र):</strong> फेच (मेमोरी से निर्देश लाना) -> डिकोड (CU द्वारा अर्थ समझना) -> एक्ज़ीक्यूट (ALU द्वारा निष्पादन) -> स्टोर (परिणाम संचयन)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Program Counter (PC) stores the address of the NEXT instruction to be executed; registers are the fastest memory in a computer system!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> प्रोग्राम काउंटर (PC) निष्पादित होने वाले अगले निर्देश का पता रखता है; कंप्यूटर में सबसे तेज गति वाली मेमोरी 'रजिस्टर्स' होती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Motherboard, System Bus & Firmware -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-project-diagram" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Motherboard, Buses &amp; Firmware</span>
                    <span class="lang-hi">2. मदरबोर्ड, सिस्टम बस एवं फर्मवेयर</span>
                </h4>
                <span class="mindmap-node-tag">BIOS • UEFI • CMOS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Components &amp; Bus Architecture</span>
                        <span class="lang-hi">प्रमुख घटक एवं बस वास्तुकला</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Address Bus</strong> (Unidirectional)</span>
                        <span class="mindmap-chip"><strong>Data Bus</strong> (Bidirectional)</span>
                        <span class="mindmap-chip"><strong>Control Bus</strong> (Control &amp; Timing)</span>
                        <span class="mindmap-chip"><strong>Northbridge</strong> (RAM &amp; PCIe GPU)</span>
                        <span class="mindmap-chip"><strong>Southbridge</strong> (SATA, USB, Audio)</span>
                        <span class="mindmap-chip"><strong>BIOS / POST</strong> (Firmware)</span>
                        <span class="mindmap-chip"><strong>UEFI / GPT</strong> (Modern Standard)</span>
                        <span class="mindmap-chip"><strong>CMOS RAM</strong> (CR2032 Battery)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Operations &amp; Standards</span>
                        <span class="lang-hi">प्रमुख प्रक्रियाएं एवं मानक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>System Bus:</strong> Group of parallel electronic pathways. <strong>Address Bus:</strong> Unidirectional from CPU to memory/IO; bus width determines max memory capacity (e.g. 32-bit = 2^32 = 4 GB, 64-bit = 16 Exabytes). <strong>Data Bus:</strong> Bidirectional; width defines word length (32-bit, 64-bit). <strong>Control Bus:</strong> Coordinates read/write pulses and interrupts.</span>
                            <span class="lang-hi"><strong>सिस्टम बस:</strong> समानांतर विद्युत पथों का समूह। <strong>एड्रेस बस:</strong> CPU से मेमोरी की ओर एकदिशीय; चौड़ाई अधिकतम मेमोरी क्षमता तय करती है (32-बिट = 4 GB, 64-बिट = 16 EB)। <strong>डेटा बस:</strong> द्विदिशीय, डेटा ले जाती है। <strong>कंट्रोल बस:</strong> रीड/राइट व इंटरप्ट सिग्नल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>BIOS &amp; POST:</strong> Basic Input/Output System stored in ROM/EEPROM; executes POST (Power-On Self-Test) upon boot to verify keyboard, RAM, and storage; invokes bootstrap loader to load OS kernel into RAM.</span>
                            <span class="lang-hi"><strong>BIOS एवं POST:</strong> ROM में स्थायी फर्मवेयर; कंप्यूटर ऑन होते ही POST (पावर-ऑन सेल्फ-टेस्ट) चलाकर हार्डवेयर जांचता है और बूटस्ट्रैप लोडर द्वारा OS को रैम में लोड कराता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>BIOS vs UEFI:</strong> Legacy BIOS uses 16-bit real mode and MBR partition scheme (max 2 TB drive, max 4 primary partitions). Modern UEFI uses 32/64-bit code, graphical interface, Secure Boot, and GPT partition scheme (&gt;2 TB drives, up to 128 partitions).</span>
                            <span class="lang-hi"><strong>BIOS बनाम UEFI:</strong> पुराना BIOS 16-बिट तथा MBR (अधिकतम 2 TB, 4 पार्टिशन) का उपयोग करता है। आधुनिक UEFI 64-बिट, सुरक्षित बूट (Secure Boot) तथा GPT (&gt;2 TB, 128 पार्टिशन) सपोर्ट करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>CMOS Chip:</strong> Low-power volatile RAM powered by a coin-cell battery (CR2032) that keeps track of real-time clock (RTC), date, time, and custom hardware boot configuration when PC is powered off.</span>
                            <span class="lang-hi"><strong>CMOS चिप:</strong> CR2032 सेल बैटरी द्वारा संचालित वोलेटाइल रैम, जो कंप्यूटर बंद होने पर भी सिस्टम की तारीख, समय व बायोस सेटिंग्स को सुरक्षित रखती है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> POST is performed by BIOS; Address Bus is unidirectional while Data Bus is bidirectional; CR2032 battery powers the CMOS chip.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> POST परीक्षण BIOS द्वारा किया जाता है; एड्रेस बस एकदिशीय व डेटा बस द्विदिशीय होती है; CMOS चिप को CR2032 बैटरी से ऊर्जा मिलती है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Primary Memory & Cache -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-memory" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Primary Memory &amp; Cache</span>
                    <span class="lang-hi">3. प्राथमिक मेमोरी (रैम/रोम) एवं कैश</span>
                </h4>
                <span class="mindmap-node-tag">SRAM • DRAM • ROM</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Memory Types &amp; Classifications</span>
                        <span class="lang-hi">मेमोरी के प्रकार एवं श्रेणियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>RAM</strong> (Volatile Read/Write)</span>
                        <span class="mindmap-chip"><strong>SRAM</strong> (Flip-Flop / No Refresh)</span>
                        <span class="mindmap-chip"><strong>DRAM</strong> (Capacitor / Needs Refresh)</span>
                        <span class="mindmap-chip"><strong>Cache</strong> (L1, L2, L3)</span>
                        <span class="mindmap-chip"><strong>ROM</strong> (Non-Volatile Permanent)</span>
                        <span class="mindmap-chip"><strong>PROM / EPROM / EEPROM</strong></span>
                        <span class="mindmap-chip"><strong>Flash Memory</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Structural &amp; Operational Contrasts</span>
                        <span class="lang-hi">संरचनात्मक एवं कार्यात्मक विभेद</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>RAM (Random Access Memory):</strong> Primary working memory of computer; volatile (loses data when power is turned off); allows both read and write operations directly to any memory cell in constant time.</span>
                            <span class="lang-hi"><strong>रैम (RAM):</strong> कंप्यूटर की मुख्य कार्यशील मेमोरी; वोलेटाइल (विद्युत जाते ही डेटा नष्ट); इसमें किसी भी सेल से समान समय में डेटा पढ़ा व लिखा जा सकता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>SRAM vs DRAM:</strong> <strong>SRAM (Static RAM):</strong> Uses 4-6 transistors/flip-flops per bit; very fast (1-10 ns), does NOT require periodic electric refreshing, expensive; used for CPU Cache (L1, L2, L3). <strong>DRAM (Dynamic RAM):</strong> Uses 1 transistor + 1 capacitor per bit; charge leaks and REQUIRES periodic refreshing thousands of times per second; slower (50-70 ns), cheaper, high density; used for Main System RAM (DDR4, DDR5).</span>
                            <span class="lang-hi"><strong>SRAM बनाम DRAM:</strong> <strong>SRAM:</strong> फ्लिप-फ्लॉप पर आधारित, रीफ्रेश करने की आवश्यकता नहीं, अति-तीव्र, महंगी; CPU कैश में प्रयुक्त। <strong>DRAM:</strong> कैपेसिटर पर आधारित, लगातार रीफ्रेशिंग अनिवार्य, सस्ती, सघन; मुख्य सिस्टम रैम में प्रयुक्त (DDR4, DDR5)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cache Memory:</strong> Small, high-speed buffer located between CPU and RAM to bridge speed mismatch. L1 Cache (fastest, smallest, inside core), L2 Cache (larger, per-core), L3 Cache (shared across all cores). Principle of Locality: Temporal &amp; Spatial.</span>
                            <span class="lang-hi"><strong>कैश मेमोरी:</strong> CPU और रैम के बीच गति असंतुलन दूर करने वाली तीव्र बफर मेमोरी। L1 (तीव्रतम, कोर के भीतर), L2 (प्रत्येक कोर हेतु), L3 (सभी कोर द्वारा साझा)। लोकैलिटी सिद्धांत पर कार्य।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ROM (Read Only Memory):</strong> Non-volatile permanent memory; retains data without power. Types: <strong>PROM:</strong> Programmable once using PROM burner. <strong>EPROM:</strong> Erased by Ultraviolet (UV) light exposure through quartz window. <strong>EEPROM:</strong> Erased and rewritten electrically byte-by-byte (used in modern flash BIOS chips).</span>
                            <span class="lang-hi"><strong>रोम (ROM):</strong> गैर-वाष्पशील (स्थायी) मेमोरी; बिजली जाने पर डेटा सुरक्षित रहता है। <strong>PROM:</strong> केवल एक बार प्रोग्राम करने योग्य। <strong>EPROM:</strong> पराबैंगनी (UV) किरणों द्वारा मिटाई जाने वाली। <strong>EEPROM:</strong> विद्युत पल्स द्वारा बाइट-दर-बाइट मिटाई और पुनर्लिखित होने वाली।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> DRAM requires periodic refreshing; SRAM does not; EPROM is erased by UV light; Cache memory sits directly between CPU and RAM!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> DRAM को निरंतर रीफ्रेश करने की आवश्यकता होती है; EPROM को पराबैंगनी (UV) किरणों से मिटाया जाता है; कैश मेमोरी CPU और RAM के मध्य स्थित होती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Secondary & External Storage -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hdd" style="color: #d97706;"></i>
                    <span class="lang-en">4. Secondary &amp; Tertiary Storage</span>
                    <span class="lang-hi">4. द्वितीयक एवं बाह्य स्टोरेज उपकरण</span>
                </h4>
                <span class="mindmap-node-tag">HDD • SSD • Optical • Tape</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Storage Media &amp; Capacities</span>
                        <span class="lang-hi">स्टोरेज माध्यम एवं उनकी क्षमताएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>HDD</strong> (Magnetic Platter, RPM)</span>
                        <span class="mindmap-chip"><strong>SSD</strong> (NAND Flash, NVMe/SATA)</span>
                        <span class="mindmap-chip"><strong>CD-ROM</strong> (700 MB, Infrared 780nm)</span>
                        <span class="mindmap-chip"><strong>DVD</strong> (4.7 GB / 8.5 GB, Red 650nm)</span>
                        <span class="mindmap-chip"><strong>Blu-ray</strong> (25 GB / 50 GB, Blue 405nm)</span>
                        <span class="mindmap-chip"><strong>Floppy Disk</strong> (1.44 MB, 3.5-inch)</span>
                        <span class="mindmap-chip"><strong>Magnetic Tape</strong> (Sequential Access)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Mechanics &amp; Speed Comparisons</span>
                        <span class="lang-hi">प्रमुख यांत्रिकी एवं गति तुलना</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hard Disk Drive (HDD):</strong> Magnetic storage using spinning platters coated with magnetic material. Data organized into concentric <strong>Tracks</strong>, divided into <strong>Sectors</strong> (512 bytes or 4KB Advanced Format), aligned vertically across platters as <strong>Cylinders</strong>. Speed measured in RPM (5400/7200 RPM); Access Time = Seek Time (head positioning) + Rotational Latency (platter spin) + Transfer Rate.</span>
                            <span class="lang-hi"><strong>हार्ड डिस्क ड्राइव (HDD):</strong> चुंबकीय स्टोरेज; डेटा संकेंद्रित <strong>ट्रैक्स (Tracks)</strong> एवं <strong>सेक्टर्स (Sectors - 512B/4KB)</strong> में विभाजित होता है; सभी प्लेटर्स के समान ट्रैक मिलकर <strong>सिलेंडर (Cylinder)</strong> बनाते हैं। स्पिंडल गति 5400/7200 RPM।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Solid-State Drive (SSD):</strong> Non-volatile NAND flash memory with no moving parts; shock resistant, silent, consumes less power. SATA SSD (max ~550 MB/s) vs NVMe M.2 PCIe SSD (up to 7000+ MB/s, directly connects to PCIe bus).</span>
                            <span class="lang-hi"><strong>सॉलिड-स्टेट ड्राइव (SSD):</strong> बिना किसी यांत्रिक गतिमान भाग वाली NAND फ्लैश मेमोरी; शांत, शॉक-प्रूफ व तीव्र। SATA SSD (~550 MB/s) की तुलना में NVMe M.2 SSD (7000+ MB/s) अत्यधिक तेज है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Optical Storage Comparison:</strong> <strong>CD:</strong> 700 MB, 780 nm infrared laser. <strong>DVD:</strong> 4.7 GB (single-layer) / 8.5 GB (dual-layer), 650 nm red laser. <strong>Blu-ray Disc (BD):</strong> 25 GB (single-layer) / 50 GB (dual-layer) up to 100 GB (BD-XL), 405 nm blue-violet laser (shorter wavelength allows tighter pits).</span>
                            <span class="lang-hi"><strong>ऑप्टिकल स्टोरेज तुलना:</strong> <strong>CD:</strong> 700 MB (780 nm इंफ्रारेड लेजर)। <strong>DVD:</strong> 4.7 GB / 8.5 GB (650 nm लाल लेजर)। <strong>ब्लू-रे डिस्क:</strong> 25 GB / 50 GB (405 nm नीली-बैंगनी लेजर, छोटी तरंगदैर्ध्य से अधिक डेटा घनत्व)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Direct vs Sequential Access:</strong> Magnetic Tape is <strong>Sequential Access</strong> (must wind past earlier records; ideal for low-cost enterprise archival). HDD, SSD, and Optical discs are <strong>Direct/Random Access</strong> (can jump directly to any address).</span>
                            <span class="lang-hi"><strong>प्रत्यक्ष बनाम क्रमिक एक्सेस:</strong> मैग्नेटिक टेप <strong>क्रमिक एक्सेस (Sequential Access)</strong> माध्यम है (डेटा तक पहुँचने हेतु आगे की टेप घुमानी पड़ती है; दीर्घकालिक बैकअप हेतु उपयोगी)। HDD और SSD <strong>डायरेक्ट/रैंडम एक्सेस</strong> माध्यम हैं।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Standard 3.5-inch floppy capacity is 1.44 MB; standard CD capacity is 700 MB; standard single-layer DVD is 4.7 GB; Blu-ray uses 405 nm blue-violet laser!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 3.5 इंच फ्लॉपी डिस्क क्षमता 1.44 MB; CD की 700 MB; सिंगल-लेयर DVD की 4.7 GB; तथा ब्लू-रे में 405 nm नीली-बैंगनी लेजर प्रयुक्त होती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Software Classification & Translators -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-code" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Software Classification &amp; Translators</span>
                    <span class="lang-hi">5. सॉफ्टवेयर वर्गीकरण एवं भाषा अनुवादक</span>
                </h4>
                <span class="mindmap-node-tag">System • App • Compilers</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Software Categories &amp; Utilities</span>
                        <span class="lang-hi">सॉफ्टवेयर की श्रेणियां एवं यूटिलिटीज</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>System Software</strong> (OS &amp; Drivers)</span>
                        <span class="mindmap-chip"><strong>Application Software</strong> (End-User)</span>
                        <span class="mindmap-chip"><strong>Utility Software</strong> (Antivirus, Defrag)</span>
                        <span class="mindmap-chip"><strong>Assembler</strong> (Assembly to Machine)</span>
                        <span class="mindmap-chip"><strong>Compiler</strong> (Entire Code to Object)</span>
                        <span class="mindmap-chip"><strong>Interpreter</strong> (Line-by-Line Execution)</span>
                        <span class="mindmap-chip"><strong>Linker &amp; Loader</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Translator Mechanics &amp; Differences</span>
                        <span class="lang-hi">अनुवादक प्रक्रिया एवं मुख्य अंतर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>System vs Application Software:</strong> System Software manages computer hardware and system resources (OS, Device Drivers, Utilities). Application Software solves specific user tasks (MS Word, Excel, VLC player, Photoshop).</span>
                            <span class="lang-hi"><strong>सिस्टम बनाम एप्लिकेशन सॉफ्टवेयर:</strong> सिस्टम सॉफ्टवेयर हार्डवेयर और आंतरिक संसाधनों का प्रबंधन करता है (OS, ड्राइवर, यूटिलिटीज)। एप्लिकेशन सॉफ्टवेयर उपयोगकर्ता के विशिष्ट कार्य करता है (वर्ड, एक्सेल, ब्राउज़र)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Assembler:</strong> Translates low-level Assembly Language mnemonic instructions (ADD, SUB, MOV) into machine code (binary 0 and 1).</span>
                            <span class="lang-hi"><strong>असेंबलर:</strong> निम्नस्तरीय असेंबली भाषा के निमोनिक कोड (ADD, MOV, SUB) को मशीनी भाषा (बाइनरी 0 व 1) में परिवर्तित करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Compiler:</strong> Translates entire High-Level Language program at once into machine code (object module); creates standalone executable (.exe); execution is very fast; displays all syntax errors together at the end. Examples: C, C++, Rust.</span>
                            <span class="lang-hi"><strong>कंपाइलर:</strong> संपूर्ण उच्चस्तरीय प्रोग्राम का एक ही बार में मशीनी कोड (ऑब्जेक्ट कोड) में अनुवाद करता है; स्वतंत्र .exe फाइल बनाता है; तीव्र निष्पादन; अंत में सभी त्रुटियां एक साथ दिखाता है (C, C++)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Interpreter:</strong> Translates and executes High-Level code line-by-line; stops immediately on encountering first error; slower execution; requires interpreter during every run. Examples: Python, JavaScript, Ruby.</span>
                            <span class="lang-hi"><strong>इंटरप्रेटर:</strong> उच्चस्तरीय प्रोग्राम का पंक्ति-दर-पंक्ति (लाइन-बाय-लाइन) अनुवाद व निष्पादन करता है; पहली त्रुटि पर रुक जाता है; निष्पादन धीमा; प्रत्येक बार अनुवादक की आवश्यकता (Python, JavaScript)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Linker &amp; Loader:</strong> <strong>Linker:</strong> Combines multiple compiled object files and external system libraries into a single executable (.exe). <strong>Loader:</strong> Loads the executable from secondary storage into main RAM and initializes CPU registers for execution.</span>
                            <span class="lang-hi"><strong>लिंकर एवं लोडर:</strong> <strong>लिंकर:</strong> विभिन्न कंपाइल किए गए ऑब्जेक्ट मॉड्यूल्स व लाइब्रेरी फाइलों को जोड़कर एक निष्पादन योग्य (.exe) फाइल बनाता है। <strong>लोडर:</strong> उस .exe फाइल को सेकेंडरी स्टोरेज से RAM में लोड कर निष्पादन शुरू कराता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Compiler translates entire source code at once; Interpreter translates line-by-line; Linker combines object modules into executable; Loader puts program into RAM!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कंपाइलर पूरे प्रोग्राम को एक साथ अनुवादित करता है; इंटरप्रेटर लाइन-बाय-लाइन करता है; लिंकर ऑब्जेक्ट फाइलों को जोड़ता है तथा लोडर प्रोग्राम को RAM में लोड करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Open Source, Licensing & Firmware -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-balance-scale" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Software Licensing &amp; Ecosystem</span>
                    <span class="lang-hi">6. सॉफ्टवेयर लाइसेंसिंग एवं कानूनी अधिकार</span>
                </h4>
                <span class="mindmap-node-tag">FOSS • Proprietary • Freeware</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Licensing Models &amp; Legal Types</span>
                        <span class="lang-hi">लाइसेंस मॉडल एवं विधिक प्रकार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Proprietary</strong> (Closed Source, Paid)</span>
                        <span class="mindmap-chip"><strong>Open Source</strong> (FOSS, Free Access)</span>
                        <span class="mindmap-chip"><strong>GNU GPL</strong> (Copyleft License)</span>
                        <span class="mindmap-chip"><strong>Freeware</strong> (Free Cost, Closed Code)</span>
                        <span class="mindmap-chip"><strong>Shareware</strong> (Trialware e.g. 30 days)</span>
                        <span class="mindmap-chip"><strong>Public Domain</strong> (No Copyright)</span>
                        <span class="mindmap-chip"><strong>Firmware</strong> (Hardcoded in ROM)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Licensing Details &amp; Government Policies</span>
                        <span class="lang-hi">लाइसेंस विवरण एवं सरकारी नीतियां</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Proprietary / Closed Source:</strong> Source code is protected under copyright and kept secret by vendor; user only buys a license to use the compiled software. Examples: Microsoft Windows, MS Office, Adobe Photoshop.</span>
                            <span class="lang-hi"><strong>प्रोप्राइटरी (क्लोज्ड सोर्स):</strong> स्रोत कोड (Source Code) गोपनीय व कॉपीराइट सुरक्षित होता है; उपयोगकर्ता केवल उपयोग का लाइसेंस खरीदता है। उदाहरण: Windows, MS Office, Photoshop।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Free and Open Source Software (FOSS):</strong> Source code is freely accessible, inspectable, modifiable, and redistributable. Initiated by Richard Stallman (GNU Project, 1983) and Linus Torvalds (Linux, 1991). Licenses: GNU GPL, MIT, Apache 2.0. Examples: Linux, Apache HTTP Server, LibreOffice, Python, VLC.</span>
                            <span class="lang-hi"><strong>ओपन सोर्स (FOSS):</strong> सोर्स कोड सभी हेतु निःशुल्क उपलब्ध, संपादन योग्य व पुनर्वितरित करने की स्वतंत्रता। रिचर्ड स्टॉलमैन (GNU) एवं लिनुस टोरवाल्ड्स (Linux) द्वारा प्रवर्तित। उदाहरण: Linux, LibreOffice, Python, VLC।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Freeware vs Shareware:</strong> <strong>Freeware:</strong> Distributed free of financial charge, but source code is NOT provided and modification is prohibited (e.g. Adobe Acrobat Reader, Skype). <strong>Shareware:</strong> Distributed free on a trial basis for limited time/features (e.g. WinRAR 40-day trial).</span>
                            <span class="lang-hi"><strong>फ्रीवेयर बनाम शेयरवेयर:</strong> <strong>फ्रीवेयर:</strong> बिना शुल्क के उपलब्ध, किंतु सोर्स कोड बंद रहता है (Adobe Reader)। <strong>शेयरवेयर:</strong> परीक्षण अवधि (ट्रायल) हेतु सीमित समय या सुविधाओं के साथ निःशुल्क (WinRAR)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>India &amp; UP Open Source Policy:</strong> Government of India Policy on Adoption of Open Source Software (2015) mandates preferential adoption of FOSS in all e-governance systems to ensure data sovereignty, vendor independence, and cost efficiency.</span>
                            <span class="lang-hi"><strong>भारत व उप्र ओपन सोर्स नीति (2015):</strong> भारत सरकार ने सभी ई-गवर्नेंस परियोजनाओं में विदेशी सॉफ्टवेयर निर्भरता समाप्त करने हेतु ओपन सोर्स सॉफ्टवेयर (FOSS) को प्राथमिकता देना अनिवार्य किया है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Linux and LibreOffice are Open Source (FOSS); WinRAR is Shareware; Adobe Reader is Freeware; Firmware is stored in ROM/EEPROM!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> Linux और LibreOffice ओपन सोर्स (FOSS) हैं; WinRAR शेयरवेयर है; एडोब रीडर फ्रीवेयर है; तथा फर्मवेयर ROM में स्थायी रहता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''

from t3_data import mindmap_topic3 as mm_t3


# ==========================================
# Topic 4: Operating System, Social Networking & E-Governance
# ==========================================
mm_t4 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Operating Systems, Social Media &amp; E-Governance</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: ऑपरेटिंग सिस्टम, सोशल मीडिया नेटवर्क एवं ई-गवर्नेंस</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Kernel &amp; Scheduling • Deadlock &amp; Memory Management • Social Media Platforms • Cyber Law (IT Act 2000) • National &amp; UP E-Governance Portals</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • कर्नल व शेड्यूलिंग • डेडलॉक व मेमोरी प्रबंधन • सोशल मीडिया • आईटी अधिनियम 2000 • राष्ट्रीय व उप्र ई-गवर्नेंस पोर्टल</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-cogs"></i>
            <span class="lang-en">OS Architecture, Social Networking &amp; Digital Governance</span>
            <span class="lang-hi">OS वास्तुकला, सोशल नेटवर्किंग एवं डिजिटल सुशासन</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: OS Types & Kernel Architecture -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-window-restore" style="color: #059669;"></i>
                    <span class="lang-en">1. OS Architecture &amp; Types</span>
                    <span class="lang-hi">1. OS वास्तुकला एवं प्रकार</span>
                </h4>
                <span class="mindmap-node-tag">Kernel • Monolithic • RTOS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">OS Types &amp; Architectures</span>
                        <span class="lang-hi">ऑपरेटिंग सिस्टम प्रकार एवं संरचना</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Batch OS</strong> (No Interaction)</span>
                        <span class="mindmap-chip"><strong>Time-Sharing</strong> (Time Quantum)</span>
                        <span class="mindmap-chip"><strong>Multiprogramming</strong> (CPU Busy)</span>
                        <span class="mindmap-chip"><strong>Real-Time OS (RTOS)</strong> (Deadlines)</span>
                        <span class="mindmap-chip"><strong>Monolithic Kernel</strong> (Linux)</span>
                        <span class="mindmap-chip"><strong>Microkernel</strong> (Minix / QNX)</span>
                        <span class="mindmap-chip"><strong>Unix</strong> (1969, Ritchie &amp; Thompson)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Core Principles &amp; Differences</span>
                        <span class="lang-hi">मूलभूत सिद्धांत एवं मुख्य अंतर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Operating System Role:</strong> System software acting as intermediary between computer hardware and user applications. Allocates CPU time, main memory, storage, and I/O devices.</span>
                            <span class="lang-hi"><strong>OS की भूमिका:</strong> हार्डवेयर और उपयोगकर्ता/एप्लिकेशन के मध्य मध्यस्थ प्रणाली सॉफ्टवेयर। CPU समय, मुख्य मेमोरी, स्टोरेज और I/O का प्रबंधन करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Real-Time Operating System (RTOS):</strong> Strict time-bound processing. <strong>Hard RTOS:</strong> Missing deadline causes catastrophic system failure (e.g. missile guidance, nuclear plant, airbag, pacemaker). <strong>Soft RTOS:</strong> Missed deadline degrades quality of service without total crash (e.g. live video streaming, online gaming).</span>
                            <span class="lang-hi"><strong>रीयल-टाइम OS (RTOS):</strong> कठोर समय-सीमा। <strong>हार्ड RTOS:</strong> समय सीमा चूकने पर विनाशकारी विफलता (मिसाइल नियंत्रण, पेसमेकर, एयरबैग)। <strong>सॉफ्ट RTOS:</strong> समय चूकने पर गुणवत्ता में कमी किंतु विनाश नहीं (वीडियो स्ट्रीमिंग, ऑनलाइन गेमिंग)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kernel Architecture:</strong> Kernel is core of OS. <strong>Monolithic Kernel:</strong> All OS services (VFS, IPC, drivers, memory) run in single kernel space address (faster, but driver bug can crash system - Linux). <strong>Microkernel:</strong> Only bare essentials (IPC, scheduling, basic memory) run in kernel space; drivers and file systems run as user-space servers (highly stable - Minix, QNX).</span>
                            <span class="lang-hi"><strong>कर्नल वास्तुकला:</strong> कर्नल OS का हृदय है। <strong>मोनोलिथिक कर्नल:</strong> सभी सेवाएं कर्नल स्पेस में चलती हैं (अति तीव्र, किंतु ड्राइवर में बग से पूरा सिस्टम क्रैश - Linux)। <strong>माइक्रोकर्नल:</strong> केवल अनिवार्य सेवाएं कर्नल में, शेष यूजर स्पेस में (अत्यंत सुरक्षित - Minix, QNX)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Hard RTOS is used in missile systems and airbags; Linux uses a Monolithic kernel; Unix was developed at Bell Labs in 1969!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> मिसाइल प्रणाली व एयरबैग में 'हार्ड RTOS' का उपयोग होता है; Linux में मोनोलिथिक कर्नल होता है; Unix का विकास 1969 में बेल लैब्स में हुआ था!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Process Scheduling, Deadlock & Memory -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tasks" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Process, Memory &amp; Deadlocks</span>
                    <span class="lang-hi">2. प्रोसेस शेड्यूलिंग, डेडलॉक एवं मेमोरी</span>
                </h4>
                <span class="mindmap-node-tag">FCFS • Round Robin • Banker's</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Algorithms &amp; Management</span>
                        <span class="lang-hi">एल्गोरिदम एवं संसाधन प्रबंधन</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>PCB</strong> (Process Control Block)</span>
                        <span class="mindmap-chip"><strong>FCFS</strong> (Convoy Effect)</span>
                        <span class="mindmap-chip"><strong>SJF</strong> (Shortest Job First)</span>
                        <span class="mindmap-chip"><strong>Round Robin</strong> (Time Quantum)</span>
                        <span class="mindmap-chip"><strong>Coffman Conditions</strong> (4 Criteria)</span>
                        <span class="mindmap-chip"><strong>Banker's Algorithm</strong> (Avoidance)</span>
                        <span class="mindmap-chip"><strong>Paging &amp; Virtual Memory</strong></span>
                        <span class="mindmap-chip"><strong>Thrashing</strong> (Page Faults)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Mechanics &amp; Deadlock Conditions</span>
                        <span class="lang-hi">प्रमुख यांत्रिकी एवं डेडलॉक की शर्तें</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Process States &amp; Scheduling:</strong> Process transitions through: New -> Ready -> Running -> Waiting/Blocked -> Terminated. Scheduling: <strong>FCFS:</strong> Non-preemptive, suffers convoy effect. <strong>SJF:</strong> Minimizes average waiting time; risks starvation. <strong>Round Robin:</strong> Preemptive time-slicing using fixed time quantum; optimal for time-sharing.</span>
                            <span class="lang-hi"><strong>प्रोसेस अवस्थाएं व शेड्यूलिंग:</strong> प्रोसेस अवस्थाएं: न्यू -> रेडी -> रनिंग -> वेटिंग -> टर्मिनेटेड। <strong>FCFS:</strong> पहले आओ पहले पाओ (कॉनवॉय प्रभाव)। <strong>SJF:</strong> सबसे छोटे कार्य को पहले (औसत प्रतीक्षा समय न्यूनतम)। <strong>राउंड रॉबिन:</strong> निश्चित टाइम क्वांटम पर आधारित प्रीमेप्टिव शेड्यूलिंग।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Deadlock &amp; 4 Coffman Conditions:</strong> Deadlock occurs when set of processes are blocked waiting for resources held by each other. ALL 4 conditions must hold simultaneously: 1. Mutual Exclusion, 2. Hold and Wait, 3. No Preemption, 4. Circular Wait. <strong>Banker's Algorithm (Dijkstra):</strong> Resource allocation algorithm used for deadlock avoidance by verifying safe state.</span>
                            <span class="lang-hi"><strong>डेडलॉक एवं 4 कॉफमैन शर्तें:</strong> जब प्रोसेस एक-दूसरे के संसाधनों की प्रतीक्षा में हमेशा के लिए अटक जाएं। सभी 4 शर्तें एक साथ होना अनिवार्य: 1. म्यूचुअल एक्सक्लूजन, 2. होल्ड एंड वेट, 3. नो प्रीएम्पशन, 4. सर्कुलर वेट। <strong>बैंकर्स एल्गोरिदम:</strong> डेडलॉक से बचाव (Safe State) हेतु प्रयुक्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Virtual Memory &amp; Thrashing:</strong> Extends physical RAM using secondary storage (swap space). Uses Paging (fixed-size blocks). <strong>Page Fault:</strong> CPU accesses page not present in RAM; OS fetches it from disk. <strong>Thrashing:</strong> State where system spends more time swapping pages than executing instructions, dropping CPU utilization to near zero.</span>
                            <span class="lang-hi"><strong>वर्चुअल मेमोरी व थ्रैशिंग:</strong> हार्ड डिस्क के स्पेस को अतिरिक्त रैम (स्वैप स्पेस) के रूप में प्रयुक्त करना। <strong>पेज फॉल्ट:</strong> जब मांगा गया पेज रैम में न मिले। <strong>थ्रैशिंग:</strong> जब CPU वास्तविक निष्पादन छोड़कर केवल पेज की अदला-बदली (स्वैपिंग) में फंसा रह जाए और गति शून्य हो जाए।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Banker's algorithm is used for Deadlock Avoidance; Thrashing occurs due to excessive page faults; Round Robin uses Time Quantum!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बैंकर्स एल्गोरिदम डेडलॉक से बचाव हेतु प्रयुक्त होता है; अत्यधिक पेज फॉल्ट्स से थ्रैशिंग होती है; राउंड रॉबिन में टाइम क्वांटम का उपयोग होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Social Networking Platforms -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-users" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Social Networking Ecosystem</span>
                    <span class="lang-hi">3. सोशल नेटवर्किंग मंच एवं उद्भव</span>
                </h4>
                <span class="mindmap-node-tag">Founders • Evolution • Metrics</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Platforms &amp; Founders</span>
                        <span class="lang-hi">प्रमुख मंच एवं संस्थापक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>SixDegrees</strong> (1997, 1st Social Site)</span>
                        <span class="mindmap-chip"><strong>LinkedIn</strong> (2003, Reid Hoffman)</span>
                        <span class="mindmap-chip"><strong>Facebook</strong> (2004, Mark Zuckerberg)</span>
                        <span class="mindmap-chip"><strong>YouTube</strong> (2005, Hurley, Chen, Karim)</span>
                        <span class="mindmap-chip"><strong>X / Twitter</strong> (2006, Jack Dorsey)</span>
                        <span class="mindmap-chip"><strong>WhatsApp</strong> (2009, Koum &amp; Acton)</span>
                        <span class="mindmap-chip"><strong>Instagram</strong> (2010, Systrom &amp; Krieger)</span>
                        <span class="mindmap-chip"><strong>Sandes &amp; Koo</strong> (Indigenous)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Pioneering Milestones &amp; Architecture</span>
                        <span class="lang-hi">ऐतिहासिक मील के पत्थर एवं वास्तुकला</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chronological Evolution:</strong> SixDegrees.com (1997) was the first recognized social networking platform with user profiles and friend lists. Friendster (2002), Myspace (2003), Facebook (launched Feb 2004 at Harvard).</span>
                            <span class="lang-hi"><strong>कालक्रमानुसार विकास:</strong> सिक्सडिग्रीज़.कॉम (1997) प्रोफाइल और फ्रेंड लिस्ट वाला पहला सोशल नेटवर्क था। इसके बाद फ्रेंडस्टर (2002), माइस्पेस (2003) तथा फेसबुक (फरवरी 2004, मार्क जुकरबर्ग)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Microblogging &amp; Video:</strong> Twitter/X (launched 2006 by Jack Dorsey, Biz Stone, Evan Williams; character limit expanded from 140 to 280). YouTube (launched 2005 by Steve Chen, Chad Hurley, Jawed Karim; acquired by Google in 2006; first video: "Me at the zoo").</span>
                            <span class="lang-hi"><strong>माइक्रोब्लॉगिंग व वीडियो:</strong> ट्विटर/X (2006, जैक डोर्सी; 140 से 280 अक्षर सीमा)। यूट्यूब (2005, स्टीव चेन, चाड हर्ले, जावेद करीम; 2006 में गूगल द्वारा अधिगृहीत; पहला वीडियो "Me at the zoo")।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Indian Messaging Apps:</strong> Sandes (Government Instant Messaging System - GIMS developed by NIC for official secure government communications) and Koo (multi-lingual microblogging platform).</span>
                            <span class="lang-hi"><strong>भारतीय मैसेजिंग मंच:</strong> संदेश (Sandes - NIC द्वारा सरकारी कर्मचारियों के सुरक्षित संवाद हेतु विकसित ऐप) तथा कू (Koo - भारतीय बहुभाषी माइक्रोब्लॉगिंग ऐप)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> SixDegrees.com (1997) was the first modern social network; Sandes is the government instant messaging app built by NIC!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सिक्सडिग्रीज़ (1997) पहला सोशल नेटवर्किंग प्लेटफॉर्म था; 'संदेश' (Sandes) NIC द्वारा निर्मित सरकारी मैसेजिंग ऐप है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Cyber Law & IT Act 2000 -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gavel" style="color: #d97706;"></i>
                    <span class="lang-en">4. Cyber Laws &amp; IT Act 2000</span>
                    <span class="lang-hi">4. साइबर कानून एवं आईटी अधिनियम 2000</span>
                </h4>
                <span class="mindmap-node-tag">Oct 17, 2000 • Section 66</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Crucial Legal Sections</span>
                        <span class="lang-hi">प्रमुख कानूनी धाराएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>IT Act, 2000</strong> (Effective 17 Oct 2000)</span>
                        <span class="mindmap-chip"><strong>Section 43</strong> (System Damage)</span>
                        <span class="mindmap-chip"><strong>Section 65</strong> (Source Code Tampering)</span>
                        <span class="mindmap-chip"><strong>Section 66</strong> (Computer Hacking)</span>
                        <span class="mindmap-chip"><strong>Section 66C</strong> (Identity Theft)</span>
                        <span class="mindmap-chip"><strong>Section 66D</strong> (Cheating by Personation)</span>
                        <span class="mindmap-chip"><strong>Section 66E</strong> (Privacy Violation)</span>
                        <span class="mindmap-chip"><strong>Section 66F</strong> (Cyber Terrorism - Life)</span>
                        <span class="mindmap-chip"><strong>Section 67</strong> (Obscene Content)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Legal Provisions &amp; Landmark Judgments</span>
                        <span class="lang-hi">कानूनी प्रावधान एवं ऐतिहासिक निर्णय</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Enactment of IT Act 2000:</strong> Passed by Indian Parliament based on UNCITRAL Model Law on Electronic Commerce (1996); notified and enacted on <strong>17 October 2000</strong>. Provides legal recognition to electronic records and digital signatures.</span>
                            <span class="lang-hi"><strong>आईटी अधिनियम 2000 का गठन:</strong> संयुक्त राष्ट्र के UNCITRAL मॉडल कानून (1996) पर आधारित; भारत में <strong>17 अक्टूबर 2000</strong> को लागू। इलेक्ट्रॉनिक दस्तावेजों व डिजिटल हस्ताक्षरों को कानूनी मान्यता प्रदान करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Section 66A &amp; Shreya Singhal Case (2015):</strong> Section 66A penalized sending offensive messages via communication services. Struck down as unconstitutional by Supreme Court of India in <em>Shreya Singhal v. Union of India (2015)</em> for violating Article 19(1)(a) freedom of speech.</span>
                            <span class="lang-hi"><strong>धारा 66A एवं श्रेया सिंघल वाद (2015):</strong> आपत्तिजनक संदेश भेजने पर दंड का प्रावधान था। सुप्रीम कोर्ट ने <em>श्रेया सिंघल बनाम भारत संघ (2015)</em> में इसे अभिव्यक्ति की स्वतंत्रता (अनुच्छेद 19(1)(a)) का हनन मानकर असंवैधानिक घोषित कर रद्द किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Penal Provisions:</strong> <strong>Section 66C:</strong> Identity theft (stolen password/digital signature) - up to 3 yrs imprisonment. <strong>Section 66D:</strong> Cheating by personation using computer resource. <strong>Section 66F:</strong> Cyber Terrorism (attacking critical national infrastructure) - punishable with imprisonment for life!</span>
                            <span class="lang-hi"><strong>प्रमुख दंडात्मक धाराएं:</strong> <strong>धारा 66C:</strong> पहचान की चोरी (पासवर्ड/हस्ताक्षर चुराना) - 3 वर्ष तक जेल। <strong>धारा 66D:</strong> प्रतिरूपण (छद्म भेष) द्वारा धोखाधड़ी। <strong>धारा 66F:</strong> साइबर आतंकवाद (राष्ट्रीय सुरक्षा पर साइबर हमला) - <strong>आजीवन कारावास</strong> तक का दंड!</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IT Act was enacted on 17 October 2000; Section 66F prescribes Life Imprisonment for Cyber Terrorism; Section 66A was struck down in Shreya Singhal case!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> आईटी एक्ट 17 अक्टूबर 2000 को लागू हुआ; धारा 66F में साइबर आतंकवाद हेतु आजीवन कारावास का प्रावधान है; धारा 66A श्रेया सिंघल वाद में निरस्त हुई!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: E-Governance Models & National Initiatives -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-landmark" style="color: #dc2626;"></i>
                    <span class="lang-en">5. E-Governance &amp; Digital India</span>
                    <span class="lang-hi">5. ई-गवर्नेंस मॉडल एवं डिजिटल इंडिया</span>
                </h4>
                <span class="mindmap-node-tag">G2C • G2B • DigiLocker</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Interaction Models &amp; Flagship Portals</span>
                        <span class="lang-hi">संवाद मॉडल एवं प्रमुख राष्ट्रीय पोर्टल</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>G2C</strong> (Govt to Citizen)</span>
                        <span class="mindmap-chip"><strong>G2B</strong> (Govt to Business)</span>
                        <span class="mindmap-chip"><strong>G2G</strong> (Govt to Govt)</span>
                        <span class="mindmap-chip"><strong>G2E</strong> (Govt to Employee)</span>
                        <span class="mindmap-chip"><strong>DigiLocker</strong> (Rule 9A Legal Parity)</span>
                        <span class="mindmap-chip"><strong>UMANG</strong> (Unified Mobile App)</span>
                        <span class="mindmap-chip"><strong>GeM</strong> (Govt e-Marketplace)</span>
                        <span class="mindmap-chip"><strong>BharatNet</strong> (Optical Fiber)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">National Programs &amp; Legal Parity</span>
                        <span class="lang-hi">राष्ट्रीय कार्यक्रम एवं विधिक स्थिति</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Four E-Governance Interaction Models:</strong> <strong>G2C:</strong> Aadhaar, DigiLocker, Passport Seva. <strong>G2B:</strong> GeM (Government e-Marketplace procurement), MCA21 corporate filings, GSTN. <strong>G2G:</strong> e-Office, PRAGATI portal. <strong>G2E:</strong> SARATHI, PFMS, e-HRMS.</span>
                            <span class="lang-hi"><strong>ई-गवर्नेंस के 4 संवाद मॉडल:</strong> <strong>G2C:</strong> आधार, डिजिलॉकर, पासपोर्ट सेवा। <strong>G2B:</strong> सरकारी ई-मार्केटप्लेस (GeM), MCA21, GSTN। <strong>G2G:</strong> ई-ऑफिस, प्रगति पोर्टल। <strong>G2E:</strong> PFMS पेंशन व वेतन, ई-HRMS।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>DigiLocker Legal Validity:</strong> Flagship platform under Digital India for issuing and verifying digital certificates. Rule 9A of Information Technology (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules, 2016 gives DigiLocker issued documents equal legal validity to physical documents.</span>
                            <span class="lang-hi"><strong>डिजिलॉकर की कानूनी वैधता:</strong> डिजिटल इंडिया का प्रमुख मंच; आईटी नियमावली 2016 के <strong>नियम 9A</strong> के तहत डिजिलॉकर में उपलब्ध डिजिटल दस्तावेज भौतिक मूल दस्तावेजों के समान ही वैध माने जाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UMANG Platform:</strong> Unified Mobile Application for New-age Governance launched in Nov 2017; provides single unified master platform for 1,200+ Central and State government services in 13 Indian languages.</span>
                            <span class="lang-hi"><strong>उमंग (UMANG):</strong> नवंबर 2017 में लॉन्च; 13 भारतीय भाषाओं में केंद्र व राज्यों की 1200+ नागरिक सेवाओं को एक ही मोबाइल ऐप पर उपलब्ध कराता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Rule 9A of IT Rules 2016 equates DigiLocker documents with physical originals; GeM portal is for government procurement (G2B); UMANG supports 13 languages!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> आईटी नियम 2016 का नियम 9A डिजिलॉकर दस्तावेजों को मूल के बराबर मान्यता देता है; GeM पोर्टल G2B का उदाहरण है; उमंग 13 भाषाओं में उपलब्ध है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Uttar Pradesh E-Governance Portals -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-map-marked-alt" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Uttar Pradesh E-Governance</span>
                    <span class="lang-hi">6. उत्तर प्रदेश राज्य ई-गवर्नेंस पहल</span>
                </h4>
                <span class="mindmap-node-tag">UP e-District • IGRS 1076</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">State Portals &amp; Helpline Systems</span>
                        <span class="lang-hi">राज्य पोर्टल एवं हेल्पलाइन प्रणालियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>UP e-District</strong> (Caste/Income/Domicile)</span>
                        <span class="mindmap-chip"><strong>IGRS / Jan-Sunwai</strong> (CM Helpline 1076)</span>
                        <span class="mindmap-chip"><strong>Nivesh Mitra</strong> (Single Window G2B)</span>
                        <span class="mindmap-chip"><strong>Bhulekh UP</strong> (Land Khatauni ROR)</span>
                        <span class="mindmap-chip"><strong>Kanya Sumangala</strong> (mksy.up.gov.in)</span>
                        <span class="mindmap-chip"><strong>Abhyuday Yojana</strong> (Free Coaching)</span>
                        <span class="mindmap-chip"><strong>Paradarshi Kisan</strong> (Farmer DBT)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Key Features &amp; Citizen Impact</span>
                        <span class="lang-hi">मुख्य विशेषताएं एवं नागरिक प्रभाव</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP e-District Portal:</strong> edistrict.up.gov.in delivers computerized government certificates (Caste, Income, Domicile, Birth, Death) and revenue court services through Citizen Service Centers (CSCs) across all 75 districts.</span>
                            <span class="lang-hi"><strong>उप्र ई-डिस्ट्रिक्ट पोर्टल:</strong> जन सेवा केंद्रों के माध्यम से 75 जिलों में जाति, आय, निवास, जन्म/मृत्यु प्रमाण पत्र व राजस्व न्यायालय सेवाएं ऑनलाइन प्रदान करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IGRS / Jan-Sunwai Portal:</strong> Integrated Grievance Redressal System (jansunwai.up.nic.in) directly monitored by CM's Secretariat; integrated with <strong>CM Helpline 1076</strong> for phone-based grievance registration and resolution.</span>
                            <span class="lang-hi"><strong>IGRS / जनसुनवाई पोर्टल:</strong> मुख्यमंत्री कार्यालय द्वारा सीधे मॉनिटर की जाने वाली जन शिकायत निवारण प्रणाली; <strong>मुख्यमंत्री हेल्पलाइन 1076</strong> के साथ एकीकृत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nivesh Mitra:</strong> Dedicated single-window clearance portal (niveshmitra.up.gov.in) for investors and businesses in Uttar Pradesh, providing 350+ online government clearances without physical visits.</span>
                            <span class="lang-hi"><strong>निवेश मित्र (Nivesh Mitra):</strong> उप्र में उद्यमियों व उद्योगपतियों हेतु एकल खिड़की (Single Window) पोर्टल, जहाँ 350 से अधिक सरकारी स्वीकृतियां ऑनलाइन मिलती हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Bhulekh Portal:</strong> Digitized land registry portal (upbhulekh.gov.in) offering online computerized Record of Rights (RoR - Khatauni), preventing fraudulent land registry and rural disputes.</span>
                            <span class="lang-hi"><strong>उप्र भूलेख पोर्टल:</strong> राज्य भर की खतौनी और भूमि अभिलेखों का कंप्यूटरीकृत रिकॉर्ड; घर बैठे खतौनी नकल देखने व डाउनलोड करने की सुविधा।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP CM Helpline number is 1076; Nivesh Mitra is UP's single window business portal; Jan-Sunwai portal handles citizen grievances!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र मुख्यमंत्री हेल्पलाइन नंबर 1076 है; 'निवेश मित्र' उप्र का सिंगल विंडो बिजनेस पोर्टल है; 'जनसुनवाई' नागरिक शिकायतों का निवारण करता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''

# ==========================================
# Topic 5: Operation of Printer, Tablet and Mobile
# ==========================================
mm_t5 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Printers, Tablets &amp; Smartphone Ecosystem</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: प्रिंटर, टैबलेट एवं मोबाइल उपकरण पारिस्थितिकी</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Device Flow • 6 Pillars • Laser Printing (6 Steps) • Inkjet &amp; Thermal • Tablet/Mobile SoC Architecture • Touchscreens • NavIC &amp; Cellular (1G to 5G) • UP Tablet Scheme</span>
            <span class="lang-hi">समग्र उपकरण संकल्पना प्रवाह • 6 प्रमुख स्तंभ • लेजर प्रिंटिंग (6 चरण) • इंकजेट व थर्मल • मोबाइल SoC • टचस्क्रीन • नाविक व 1G-5G नेटवर्क • उप्र टैबलेट योजना</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-mobile-alt"></i>
            <span class="lang-en">Printers, Tablets &amp; Smartphone Hardware Architecture</span>
            <span class="lang-hi">प्रिंटर, टैबलेट एवं स्मार्टफोन हार्डवेयर वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Printer Mechanics & Laser Printing Process -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-print" style="color: #059669;"></i>
                    <span class="lang-en">1. Printer Mechanics &amp; Laser Cycle</span>
                    <span class="lang-hi">1. प्रिंटर यांत्रिकी एवं लेजर प्रिंटिंग प्रक्रिया</span>
                </h4>
                <span class="mindmap-node-tag">6-Step Xerography • Toner</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Laser Printing 6-Step Cycle</span>
                        <span class="lang-hi">लेजर प्रिंटिंग के 6 चरण</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Cleaning</strong> (Scraper Blade)</span>
                        <span class="mindmap-chip"><strong>2. Conditioning</strong> (Corona -600V)</span>
                        <span class="mindmap-chip"><strong>3. Writing</strong> (Laser Discharge -100V)</span>
                        <span class="mindmap-chip"><strong>4. Developing</strong> (Toner Attraction)</span>
                        <span class="mindmap-chip"><strong>5. Transferring</strong> (+Charge Paper)</span>
                        <span class="mindmap-chip"><strong>6. Fusing</strong> (Heat ~200°C &amp; Pressure)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Detailed Electrophotographic Process</span>
                        <span class="lang-hi">विस्तृत इलेक्ट्रोफोटोग्राफिक कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cleaning &amp; Conditioning:</strong> Physical blade removes residual toner into waste hopper; primary corona wire or charge roller applies uniform high negative electrostatic charge (-600V) over rotating photosensitive drum.</span>
                            <span class="lang-hi"><strong>सफाई एवं चार्जिंग:</strong> वाइपर ब्लेड बचे हुए टोनर को साफ करता है; प्राइमरी चार्ज रोलर या कोरोना वायर पूरे फोटोसेंसिटिव ड्रम पर -600V का एकसमान नकारात्मक चार्ज चढ़ाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Writing (Exposing) &amp; Developing:</strong> Laser beam scans drum via polygonal mirror, neutralizing charge in image areas to -100V (latent electrostatic image). Developing roller coats negatively charged dry toner powder onto the discharged image areas.</span>
                            <span class="lang-hi"><strong>राइटिंग (एक्सपोजिंग) एवं डेवलपिंग:</strong> लेजर बीम अक्षरों के स्थान पर ड्रम को डिस्चार्ज (-100V) कर अदृश्य छवि बनाती है। डेवलपिंग रोलर से नकारात्मक चार्ज वाला सूखा टोनर डिस्चार्ज भाग पर चिपक जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Transferring &amp; Fusing:</strong> Transfer roller puts strong positive charge on back of paper, pulling negative toner from drum onto paper. Fuser assembly uses heated roller (~200°C) and pressure roller to permanently melt toner resin into paper fibers.</span>
                            <span class="lang-hi"><strong>ट्रांसफर एवं फ्यूजिंग:</strong> ट्रांसफर रोलर कागज पर सकारात्मक चार्ज देकर टोनर को ड्रम से कागज पर खींचता है। फ्यूजर रोलर लगभग 200°C तापमान व दबाव देकर टोनर को कागज के रेशों में स्थायी रूप से पिघला देता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Fuser unit permanently bonds toner using heat (~200°C) and pressure; the 6 steps of laser printing are: Clean -> Charge -> Write -> Develop -> Transfer -> Fuse!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> फ्यूजर असेंबली ऊष्मा (~200°C) व दबाव से टोनर को कागज पर चिपकाती है; लेजर प्रिंटिंग के 6 चरण: क्लीन -> चार्ज -> राइट -> डेवलप -> ट्रांसफर -> फ्यूज!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Inkjet, Thermal, Plotters & Print Spooler -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tint" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Inkjet, Thermal &amp; Print Spooler</span>
                    <span class="lang-hi">2. इंकजेट, थर्मल प्रिंटर एवं प्रिंट स्पूलर</span>
                </h4>
                <span class="mindmap-node-tag">CMYK • Piezo • Spooler</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Technologies &amp; Components</span>
                        <span class="lang-hi">प्रमुख तकनीक एवं घटक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>CMYK</strong> (Cyan, Magenta, Yellow, blacK)</span>
                        <span class="mindmap-chip"><strong>Thermal Bubble</strong> (Canon / HP)</span>
                        <span class="mindmap-chip"><strong>Piezoelectric</strong> (Epson Crystal)</span>
                        <span class="mindmap-chip"><strong>Direct Thermal</strong> (ATM / POS Receipts)</span>
                        <span class="mindmap-chip"><strong>Thermal Transfer</strong> (Ribbon, Barcodes)</span>
                        <span class="mindmap-chip"><strong>Print Spooler</strong> (spoolsv.exe)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Inkjet Mechanics &amp; Print Spooling</span>
                        <span class="lang-hi">इंकजेट कार्यप्रणाली एवं प्रिंट स्पूलिंग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Inkjet Spray Technologies:</strong> <strong>Thermal Bubble:</strong> Tiny heating resistor boils ink vapor bubble, ejecting droplet onto paper. <strong>Piezoelectric:</strong> Piezo crystal flexes under electric voltage to force ink droplets through nozzle with high precision.</span>
                            <span class="lang-hi"><strong>इंकजेट स्याही तकनीक:</strong> <strong>थर्मल बबल:</strong> हीटिंग तत्व स्याही को उबालकर बुलबुला बनाता है जिससे बूंद निकलती है। <strong>पीजोइलेक्ट्रिक:</strong> विद्युत संकेत से पीजो क्रिस्टल मुड़ता है और नोजल से स्याही की सूक्ष्म बूंदें निकालता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Direct Thermal vs Thermal Transfer:</strong> Direct thermal uses heat-sensitive paper that turns black on heated pin contact (ATM receipts, fades over time). Thermal transfer melts wax/resin ribbon onto labels for permanent durable barcodes.</span>
                            <span class="lang-hi"><strong>डायरेक्ट थर्मल बनाम थर्मल ट्रांसफर:</strong> डायरेक्ट थर्मल में गर्मी संवेदी कागज काला पड़ता है (ATM व POS पर्ची, समय के साथ फीकी पड़ जाती है)। थर्मल ट्रांसफर रिबन को पिघलाकर बारकोड लेबल पर पक्की छपाई करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Print Spooler (spoolsv.exe):</strong> Background operating system service that temporarily intercepts print jobs from high-speed CPU and queues them in secondary disk buffer (spool folder), releasing CPU immediately while slowly sending data to the printer.</span>
                            <span class="lang-hi"><strong>प्रिंट स्पूलर (spoolsv.exe):</strong> पृष्ठभूमि OS सेवा जो CPU से प्रिंट जॉब ग्रहण कर डिस्क बफर में कतारबद्ध करती है, जिससे CPU तुरंत मुक्त हो जाता है और प्रिंटर अपनी गति से प्रिंट करता रहता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> CMYK stands for Cyan, Magenta, Yellow, blacK; Print Spooler buffers jobs in storage to resolve speed mismatch between CPU and printer!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> CMYK का अर्थ Cyan, Magenta, Yellow, blacK (काला) है; प्रिंट स्पूलर CPU व प्रिंटर के मध्य गति अंतर को बफरिंग द्वारा संतुलित करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Tablet & Mobile Hardware Architecture (SoC) -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microchip" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Tablet &amp; Mobile Hardware (SoC)</span>
                    <span class="lang-hi">3. टैबलेट एवं स्मार्टफोन हार्डवेयर वास्तुकला (SoC)</span>
                </h4>
                <span class="mindmap-node-tag">ARM • GPU • NPU • UFS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">System-on-Chip (SoC) Elements</span>
                        <span class="lang-hi">सिस्टम-ऑन-चिप (SoC) के आंतरिक घटक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>ARM CPU</strong> (big.LITTLE Architecture)</span>
                        <span class="mindmap-chip"><strong>GPU</strong> (Adreno / Mali Graphics)</span>
                        <span class="mindmap-chip"><strong>NPU</strong> (Neural Processing for AI)</span>
                        <span class="mindmap-chip"><strong>ISP</strong> (Image Signal Processor)</span>
                        <span class="mindmap-chip"><strong>Baseband Modem</strong> (5G / 4G LTE)</span>
                        <span class="mindmap-chip"><strong>UFS 3.1 / 4.0</strong> vs <strong>eMMC</strong></span>
                        <span class="mindmap-chip"><strong>LPDDR5 RAM</strong> (Low-Power)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Mobile Architecture &amp; Touchscreens</span>
                        <span class="lang-hi">मोबाइल संरचना एवं टचस्क्रीन तकनीक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>System-on-Chip (SoC):</strong> Consolidates CPU, GPU, NPU, ISP (camera processing), audio DAC, and 4G/5G cellular modem onto a single silicon die; consumes minimal battery power compared to desktop motherboards.</span>
                            <span class="lang-hi"><strong>सिस्टम-ऑन-चिप (SoC):</strong> CPU, ग्राफिक्स (GPU), AI (NPU), कैमरा प्रोसेसर (ISP) तथा 5G मॉडेम को एक ही सिलिकॉन चिप पर समाहित करता है; न्यूनतम बैटरी खपत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ARM big.LITTLE Architecture:</strong> Combines high-performance CPU cores (for heavy tasks like gaming) with energy-efficient CPU cores (for idle background tasks), maximizing smartphone battery endurance.</span>
                            <span class="lang-hi"><strong>ARM big.LITTLE वास्तुकला:</strong> भारी कार्यों (गेमिंग) हेतु उच्च प्रदर्शन कोर तथा पृष्ठभूमि कार्यों हेतु ऊर्जा-कुशल कोर का संयोजन; बैटरी जीवन में भारी वृद्धि।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Capacitive vs Resistive Touchscreen:</strong> Modern tablets and mobiles use <strong>Capacitive Touchscreens</strong> that detect minute electrostatic changes caused by conductive human fingertips; supports multi-touch gestures (pinch, zoom, rotate). Resistive screens rely on mechanical pressure between two flexible layers (single-touch only).</span>
                            <span class="lang-hi"><strong>कैपेसिटिव बनाम रेसिस्टिव टचस्क्रीन:</strong> आधुनिक स्मार्टफोन <strong>कैपेसिटिव टचस्क्रीन</strong> का उपयोग करते हैं जो मानव उंगली की विद्युत चालकता पहचानती है (मल्टी-टच जेस्चर)। रेसिस्टिव स्क्रीन केवल यांत्रिक दबाव पर कार्य करती है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Smartphones use System on Chip (SoC) based on ARM architecture; capacitive touchscreens enable multi-touch pinch-to-zoom!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> स्मार्टफोन ARM वास्तुकला पर आधारित SoC चिप का प्रयोग करते हैं; मल्टी-टच जेस्चर हेतु 'कैपेसिटिव टचस्क्रीन' का उपयोग होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Mobile Operating Systems & Runtimes -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cogs" style="color: #d97706;"></i>
                    <span class="lang-en">4. Mobile Operating Systems</span>
                    <span class="lang-hi">4. मोबाइल ऑपरेटिंग सिस्टम एवं प्लेटफॉर्म</span>
                </h4>
                <span class="mindmap-node-tag">Android • iOS • ART</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Major Platforms &amp; Runtimes</span>
                        <span class="lang-hi">प्रमुख प्लेटफॉर्म एवं रनटाइम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Android</strong> (Modified Linux Kernel)</span>
                        <span class="mindmap-chip"><strong>Andy Rubin</strong> (Android Inc, 2003)</span>
                        <span class="mindmap-chip"><strong>ART</strong> (Android Runtime, AOT)</span>
                        <span class="mindmap-chip"><strong>APK / AAB</strong> (App Packaging)</span>
                        <span class="mindmap-chip"><strong>Apple iOS</strong> (Darwin / Mach Unix)</span>
                        <span class="mindmap-chip"><strong>Steve Jobs</strong> (iPhone, 2007)</span>
                        <span class="mindmap-chip"><strong>KaiOS &amp; BharOS</strong> (Indigenous)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Architectural Contrasts &amp; Package Formats</span>
                        <span class="lang-hi">वास्तुकला तुलना एवं पैकेज प्रारूप</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Android Architecture:</strong> Founded by Andy Rubin (2003), acquired by Google in 2005; open-source (AOSP) based on modified Linux kernel. Uses <strong>Android Runtime (ART)</strong> with Ahead-of-Time (AOT) and JIT compilation to execute DEX bytecode. App packages distributed as <strong>APK</strong> (Android Package) or <strong>AAB</strong> (Android App Bundle).</span>
                            <span class="lang-hi"><strong>एंड्रॉइड वास्तुकला:</strong> एंडी रुबिन (2003), 2005 में गूगल द्वारा अधिगृहीत; लिनक्स कर्नल पर आधारित ओपन-सोर्स (AOSP)। DEX बाइटकोड चलाने हेतु <strong>ART (एंड्रॉइड रनटाइम)</strong> का प्रयोग। ऐप पैकेज <strong>APK</strong> या <strong>AAB</strong> प्रारूप में होते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Apple iOS Architecture:</strong> Closed-source proprietary OS developed by Apple Inc. for iPhone (introduced Jan 2007 by Steve Jobs). Derived from macOS (Darwin Unix microkernel). Apps run in tight sandbox environments for security; packaged as <strong>IPA</strong> files.</span>
                            <span class="lang-hi"><strong>ऐप्पल iOS वास्तुकला:</strong> एप्पल द्वारा iPhone हेतु विकसित क्लोज्ड-सोर्स प्रोप्राइटरी OS (2007, स्टीव जॉब्स)। डार्विन यूनिक्स कर्नल पर आधारित। ऐप्स सैंडबॉक्स सुरक्षा में चलते हैं; <strong>IPA</strong> पैकेज प्रारूप।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>BharOS (India's Indigenous Mobile OS):</strong> Developed by JandK Operations Pvt Ltd (incubated at IIT Madras) as a secure indigenous Linux-based mobile operating system with No Default Apps (NDA) for enhanced user privacy and national security.</span>
                            <span class="lang-hi"><strong>BharOS (भारत का स्वदेशी मोबाइल OS):</strong> IIT मद्रास द्वारा समर्थित स्टार्टअप द्वारा विकसित स्वदेशी सुरक्षित मोबाइल OS; इसमें कोई डिफॉल्ट ऐप नहीं होती (NDA), जिससे डेटा गोपनीयता बनी रहती है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Android is based on modified Linux kernel; Android founder was Andy Rubin; BharOS is India's indigenous mobile OS developed by IIT Madras!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> एंड्रॉइड लिनक्स कर्नल पर आधारित है; एंड्रॉइड के संस्थापक एंडी रुबिन थे; BharOS भारत का स्वदेशी मोबाइल OS है जिसे IIT मद्रास ने विकसित किया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Mobile Sensors, Navigation & Cellular Standards -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-satellite" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Sensors, NavIC &amp; Cellular Tech</span>
                    <span class="lang-hi">5. मोबाइल सेंसर्स, नाविक एवं सेलुलर नेटवर्क</span>
                </h4>
                <span class="mindmap-node-tag">NavIC • Gyro • 1G to 5G</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Sensors &amp; Satellite Constellations</span>
                        <span class="lang-hi">सेंसर्स एवं उपग्रह नेविगेशन प्रणालियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Accelerometer</strong> (Linear Motion)</span>
                        <span class="mindmap-chip"><strong>Gyroscope</strong> (Angular Rotation)</span>
                        <span class="mindmap-chip"><strong>Proximity Sensor</strong> (Ear Detection)</span>
                        <span class="mindmap-chip"><strong>GPS</strong> (USA, 31 Satellites)</span>
                        <span class="mindmap-chip"><strong>NavIC / IRNSS</strong> (ISRO, 7 Satellites)</span>
                        <span class="mindmap-chip"><strong>GLONASS</strong> (Russia)</span>
                        <span class="mindmap-chip"><strong>NFC</strong> (13.56 MHz Tap-to-Pay)</span>
                        <span class="mindmap-chip"><strong>OTG</strong> (On-The-Go Host)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Navigation Systems &amp; Cellular Generations</span>
                        <span class="lang-hi">नेविगेशन प्रणालियां एवं सेलुलर पीढ़ियाँ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Smartphone Sensors:</strong> <strong>Accelerometer:</strong> Detects linear tilt and step count. <strong>Gyroscope:</strong> Measures 3-axis rotational velocity (essential for 360° AR/VR, camera stabilization). <strong>Proximity Sensor:</strong> Infrared emitter/detector that turns off screen display during calls when brought near ear.</span>
                            <span class="lang-hi"><strong>स्मार्टफोन सेंसर्स:</strong> <strong>एक्सेलेरोमीटर:</strong> फोन का झुकाव व कदम गिनता है। <strong>जाइरोस्कोप:</strong> 3-अक्षीय कोणीय घूर्णन मापता है (कैमरा स्थिरीकरण व गेमिंग हेतु अनिवार्य)। <strong>प्रॉक्सिमिटी सेंसर:</strong> कॉल के दौरान फोन कान के पास आते ही स्क्रीन ऑफ करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>NavIC (Navigation with Indian Constellation):</strong> Indigenous regional satellite navigation system developed by ISRO (formerly IRNSS). Constellation of 7 satellites in Geostationary (GEO) and Geosynchronous (GSO) orbits; covers India and 1,500 km beyond national borders; dual frequency (L5 and S-band).</span>
                            <span class="lang-hi"><strong>नाविक (NavIC / IRNSS):</strong> ISRO द्वारा विकसित भारत की स्वतंत्र क्षेत्रीय उपग्रह नेविगेशन प्रणाली। 7 उपग्रहों का समूह (भू-स्थिर व भू-तुल्यकालिक कक्षा में); भारत व उसकी सीमाओं से 1,500 किमी तक सटीक स्थिति; दोहरी आवृत्ति (L5 व S-बैंड)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cellular Network Generations:</strong> <strong>1G:</strong> Analog voice (AMPS). <strong>2G:</strong> Digital voice, SMS, GPRS/EDGE data (GSM/CDMA). <strong>3G:</strong> Mobile broadband, video calls (UMTS/WCDMA). <strong>4G LTE:</strong> All-IP packet switched network, VoLTE HD calling, up to 1 Gbps. <strong>5G:</strong> Massive MIMO, sub-6GHz &amp; mmWave, latency &lt;1 ms, network slicing.</span>
                            <span class="lang-hi"><strong>सेलुलर पीढ़ियाँ:</strong> <strong>1G:</strong> एनालॉग वॉयस। <strong>2G:</strong> डिजिटल वॉयस, SMS (GSM/CDMA)। <strong>3G:</strong> मोबाइल इंटरनेट, वीडियो कॉल (UMTS)। <strong>4G LTE:</strong> पूर्ण IP पैकेट-स्विच्ड, VoLTE एचडी कॉलिंग। <strong>5G:</strong> अल्ट्रा-लो लेटेंसी (&lt;1 ms), मैसिव MIMO, नेटवर्क स्लाइसिंग।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> NavIC is developed by ISRO using 7 satellites covering India + 1500 km; Proximity sensor turns display off during calls; Gyroscope detects 3D rotational motion!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नाविक (NavIC) ISRO द्वारा 7 उपग्रहों से निर्मित है (भारत + 1500 किमी क्षेत्र); प्रॉक्सिमिटी सेंसर कान के पास स्क्रीन ऑफ करता है; जाइरोस्कोप घूर्णन गति मापता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Mobile Security, IMEI & UP Tablet Scheme -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-alt" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Mobile Security &amp; UP Schemes</span>
                    <span class="lang-hi">6. मोबाइल सुरक्षा, IMEI एवं उप्र टैबलेट वितरण</span>
                </h4>
                <span class="mindmap-node-tag">IMEI (*#06#) • SAR • DigiShakti</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Security Identifiers &amp; UP Portals</span>
                        <span class="lang-hi">सुरक्षा मानक एवं उत्तर प्रदेश पोर्टल</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>IMEI</strong> (15-Digit Identifier)</span>
                        <span class="mindmap-chip"><strong>Check Code:</strong> *#06#</span>
                        <span class="mindmap-chip"><strong>SAR Limit:</strong> 1.6 W/kg (1g tissue)</span>
                        <span class="mindmap-chip"><strong>Sanchar Saathi</strong> (CEIR Portal)</span>
                        <span class="mindmap-chip"><strong>DigiShakti Portal</strong> (digishakti.up.gov.in)</span>
                        <span class="mindmap-chip"><strong>Swami Vivekananda Scheme</strong> (UP Youth)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Security Standards &amp; UP Government Initiatives</span>
                        <span class="lang-hi">सुरक्षा मानक एवं उप्र सरकार की योजनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IMEI Number (15 Digits):</strong> International Mobile Equipment Identity is a unique 15-digit serial number assigned to every GSM SIM slot; checked by dialing <code>*#06#</code>. Used by telecom operators and police to blacklist and track stolen handsets on CEIR (Central Equipment Identity Register via <em>sancharsaathi.gov.in</em>).</span>
                            <span class="lang-hi"><strong>IMEI नंबर (15 अंक):</strong> प्रत्येक मोबाइल फोन के सिम स्लॉट का विशिष्ट 15-अंकीय पहचान नंबर; <code>*#06#</code> डायल कर ज्ञात किया जाता है। चोरी हुए फोन को संचार साथी (CEIR) पोर्टल पर ब्लॉक व ट्रैक करने हेतु प्रयुक्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>SAR Value (Specific Absorption Rate):</strong> Measures rate of radio frequency electromagnetic energy absorption by human body. Regulatory limit in India is <strong>1.6 W/kg</strong> averaged over 1 gram of human tissue (dial <code>*#07#</code> to check).</span>
                            <span class="lang-hi"><strong>SAR मान:</strong> मानव शरीर द्वारा मोबाइल विकिरण अवशोषण की दर। भारत में कानूनी सीमा <strong>1.6 W/kg</strong> (1 ग्राम मानव ऊतक पर) निर्धारित है; जांच हेतु <code>*#07#</code> डायल करें।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Free Smartphone &amp; Tablet Scheme:</strong> Swami Vivekananda Yuva Sashaktikaran Yojana distributes free smartphones and tablets to youth enrolled in higher education, ITI, polytechnic, and skill programs across Uttar Pradesh. Managed end-to-end via the <strong>DigiShakti Portal</strong> (digishakti.up.gov.in).</span>
                            <span class="lang-hi"><strong>उप्र स्वामी विवेकानंद युवा सशक्तिकरण योजना:</strong> उत्तर प्रदेश सरकार द्वारा उच्च शिक्षा, ITI, पॉलिटेक्निक व कौशल विकास के युवाओं को निःशुल्क स्मार्टफोन व टैबलेट वितरण। संपूर्ण प्रबंधन <strong>डिजीशक्ति पोर्टल</strong> (digishakti.up.gov.in) द्वारा।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IMEI number has 15 digits (dial *#06#); India SAR limit is 1.6 W/kg; DigiShakti portal manages UP free tablet distribution!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> IMEI 15 अंकों का होता है (*#06#); भारत में SAR सीमा 1.6 W/kg है; उप्र में टैबलेट वितरण 'डिजीशक्ति पोर्टल' द्वारा प्रबंधित होता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''

# Process Batch 1 replacements
batch1_map = {
    'history-introduction-and-application-of-computer': mm_t1,
    'hardware-and-software': mm_t2,
    'input-and-output': mm_t3,
    'operating-system-social-networking-e-governance': mm_t4,
    'operation-of-printer-tablet-and-mobile': mm_t5
}

print("Starting Batch 1 replacements...")
for topic, new_mm in batch1_map.items():
    file_path = os.path.join('upsssc-computer', topic, 'index.html')
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    m = pattern.search(content)
    if not m:
        print(f"ERROR: Could not find Card 1 pattern in {topic}")
        continue
    
    updated_content = pattern.sub(new_mm + "\n\n", content, count=1)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f"SUCCESS: Replaced Card 1 in {topic}")

print("Batch 1 completed successfully!")
