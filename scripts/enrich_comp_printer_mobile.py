import os
import re

def build_printer_mobile_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Printers, Mobile Architecture &amp; Tablet Computing</span>
    <span class="lang-hi">माइंड मैप: प्रिंटर, मोबाइल वास्तुकला एवं टैबलेट कंप्यूटिंग</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Hard Copy Devices & Mobile Ecosystem] --> B[Printers & Plotters]
    A --> C[Tablet & Mobile Hardware Architecture]
    A --> D[Mobile Operating Systems & Platforms]
    A --> E[Sensors, Connectivity & Protocols]

    B --> B1[Impact: Dot Matrix CPS, Daisy Wheel, Line Drum/Chain LPM]
    B --> B2[Non-Impact: Laser Toner PPM, Inkjet CMYK, Thermal POS]
    B --> B3[Vector Output: Plotters Flatbed/Drum for CAD Blueprints]
    B --> B4[Metrics: Resolution DPI, Speed CPS/LPM/PPM, Print Spooler]

    C --> C1[System on Chip SoC: Snapdragon, Apple A-Series, MediaTek]
    C --> C2[Displays: Capacitive Multi-touch, IPS LCD, AMOLED]
    C --> C3[Identity: IMEI 15-digit, Nano-SIM, Embedded eSIM]

    D --> D1[Android Linux-based Open Source Google, APK/AAB]
    D --> D2[iOS Unix-based Apple Proprietary, Swift/IPA]
    D --> D3[BharOS Indigenous IIT Madras Incubated, Privacy-first]

    E --> E1[Sensors: Accelerometer, Gyroscope, Proximity, Light Sensor]
    E --> E2[Wireless: NFC 13.56 MHz, Bluetooth 802.15.1, Wi-Fi 802.11, OTG]
    E --> E3[Cellular: 2G/3G/4G VoLTE/5G NR, IMEI Tracking]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[हार्ड कॉपी उपकरण एवं मोबाइल इकोसिस्टम] --> B[प्रिंटर्स एवं प्लॉटर्स]
    A --> C[टैबलेट एवं मोबाइल हार्डवेयर वास्तुकला]
    A --> D[मोबाइल ऑपरेटिंग सिस्टम]
    A --> E[सेंसर, कनेक्टिविटी एवं प्रोटोकॉल]

    B --> B1[इम्पैक्ट: डॉट मैट्रिक्स CPS, डेज़ी व्हील, लाइन प्रिंटर LPM]
    B --> B2[नॉन-इम्पैक्ट: लेज़र टोनर PPM, इंकजेट CMYK, थर्मल POS]
    B --> B3[वेक्टर आउटपुट: कैड नक्शों हेतु प्लॉटर]
    B --> B4[मापक: रिजॉल्यूशन DPI, गति CPS/LPM/PPM, प्रिंट स्पूलर]

    C --> C1[सिस्टम ऑन चिप SoC: स्नैपड्रैगन, ऐप्पल ए-सीरीज़, मीडियाटेक]
    C --> C2[डिस्प्ले: कैपेसिटिव टचस्क्रीन, IPS LCD, AMOLED]
    C --> C3[पहचान: 15 अंकों का IMEI, नैनो-सिम, एम्बेडेड eSIM]

    D --> D1[एंड्रॉयड: लिनक्स आधारित ओपन-सोर्स गूगल]
    D --> D2[iOS: यूनिक्स आधारित ऐप्पल प्रोप्राइटरी]
    D --> D3[BharOS: स्वदेशी भारतीय ओएस IIT मद्रास विकसित]

    E --> E1[सेंसर: एक्सेलेरोमीटर, जाइरोस्कोप, प्रॉक्सिमिटी, लाइट सेंसर]
    E --> E2[वायरलेस: NFC 13.56 MHz, ब्लूटूथ 802.15.1, वाई-फाई, OTG]
    E --> E3[सेलुलर: 2G/3G/4G VoLTE/5G, IMEI ट्रैकिंग]
    </div>
  </div>
</div>

<!-- Card 2: Printer Classification & Technology -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Printer Classification: Impact vs Non-Impact Technologies</span>
    <span class="lang-hi">1. प्रिंटर वर्गीकरण: इम्पैक्ट बनाम नॉन-इम्पैक्ट तकनीक</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Core Classification Principle:</strong>
          <br>&bull; Printers are primary <strong>hard-copy output devices</strong> classified fundamentally into two operating mechanisms: <strong>Impact Printers</strong> and <strong>Non-Impact Printers</strong>.</span>
        <span class="lang-hi"><strong>मूल वर्गीकरण सिद्धांत:</strong>
          <br>&bull; प्रिंटर प्राथमिक <strong>हार्ड-कॉपी आउटपुट डिवाइस</strong> हैं जिन्हें दो प्रमुख श्रेणियों में बांटा गया है: <strong>इम्पैक्ट प्रिंटर</strong> एवं <strong>नॉन-इम्पैक्ट प्रिंटर</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Impact Printers (यांत्रिक आघात प्रिंटर):</strong>
          <br>&bull; <em>Mechanism:</em> Forms characters by mechanical physical striking of hammer/pins against an inked ribbon onto paper. Noisy in operation; capable of generating <strong>carbon copies</strong> (multipart paper forms).
          <br>&bull; <em>Dot Matrix Printer (DMP):</em>
            <br>&nbsp;&nbsp;&bull; Uses a print head containing a vertical matrix of <strong>9 or 24 pins</strong>. Pins strike the inked ribbon to create patterns of tiny dots.
            <br>&nbsp;&nbsp;&bull; Speed is measured in <strong>CPS (Characters Per Second)</strong>, typically ranging from 50 to 500 CPS.
            <br>&nbsp;&nbsp;&bull; Highly economical; widely used in railways ticketing, bank statement passes, and government billing.
          <br>&bull; <em>Daisy Wheel Printer:</em>
            <br>&nbsp;&nbsp;&bull; Uses a rotating plastic or metal wheel with petals resembling a daisy flower, with embossed solid fonts on each petal.
            <br>&nbsp;&nbsp;&bull; Produces letter-quality (LQ) crisp text like a typewriter, but <strong>cannot print graphics or images</strong>; speed measured in CPS.
          <br>&bull; <em>Line Printers (लाइन प्रिंटर):</em>
            <br>&nbsp;&nbsp;&bull; Prints an entire line of text at once; speed is measured in <strong>LPM (Lines Per Minute)</strong> (typically 300 to 3000 LPM).
            <br>&nbsp;&nbsp;&bull; <em>Drum Printer:</em> Solid cylindrical drum with raised characters engraved in circular bands; hammers strike the ribbon from behind.
            <br>&nbsp;&nbsp;&bull; <em>Chain / Train Printer:</em> High-speed characters connected on a horizontal rotating metallic chain.</span>
        <span class="lang-hi"><strong>इम्पैक्ट प्रिंटर्स (Impact Printers):</strong>
          <br>&bull; <em>कार्यप्रणाली:</em> रिबन पर पिन या हैमर (हथौड़े) के भौतिक आघात द्वारा छपाई; कार्य करते समय तीव्र आवाज करते हैं; <strong>कार्बन कॉपी</strong> बनाने में सक्षम।
          <br>&bull; <em>डॉट मैट्रिक्स प्रिंटर (DMP):</em>
            <br>&nbsp;&nbsp;&bull; इसके प्रिंट हेड में <strong>9 या 24 पिनों</strong> का मैट्रिक्स होता है जो स्याही लगे रिबन पर प्रहार कर डॉट्स से अक्षर बनाता है।
            <br>&nbsp;&nbsp;&bull; गति का मापन <strong>CPS (कैरेक्टर प्रति सेकंड)</strong> में किया जाता है (50 से 500 CPS)।
            <br>&nbsp;&nbsp;&bull; सस्ता एवं टिकाऊ; रेलवे टिकट व बैंक पासबुक छपाई में प्रयुक्त।
          <br>&bull; <em>डेज़ी व्हील प्रिंटर:</em>
            <br>&nbsp;&nbsp;&bull; चक्राकार पहिए की पंखुड़ियों पर उभरे हुए अक्षर होते हैं; टाइपराइटर जैसी उच्च गुणवत्ता (लेटर क्वालिटी) टेक्स्ट छापता है; <strong>ग्राफिक्स या चित्र नहीं छाप सकता</strong>।
          <br>&bull; <em>लाइन प्रिंटर:</em>
            <br>&nbsp;&nbsp;&bull; एक समय में एक पूरी पंक्ति छापता है; गति <strong>LPM (लाइन प्रति मिनट)</strong> में मापी जाती है।
            <br>&nbsp;&nbsp;&bull; प्रमुख प्रकार: <em>ड्रम प्रिंटर</em> एवं <em>चेन प्रिंटर</em>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Non-Impact Printers (शांत/गैर-आघात प्रिंटर):</strong>
          <br>&bull; <em>Mechanism:</em> Forms images without physical impact on paper using laser light, electrostatic charges, heat, or spraying liquid ink droplets. Completely silent in operation, high resolution, but <strong>cannot produce carbon copies</strong>.
          <br>&bull; <em>Laser Printer (लेज़र प्रिंटर):</em>
            <br>&nbsp;&nbsp;&bull; Invented by <strong>Gary Starkweather</strong> at Xerox (1969).
            <br>&nbsp;&nbsp;&bull; Page Printer (prints an entire page at a time); uses semiconductor laser beam, rotating mirror, photosensitive drum, and dry powdered <strong>Toner</strong> (carbon powder + polymer plastic). Heat fuser rollers melt toner onto paper.
            <br>&nbsp;&nbsp;&bull; Fastest and highest quality text printing; speed measured in <strong>PPM (Pages Per Minute)</strong> (15 to 100+ PPM).
          <br>&bull; <em>Inkjet Printer (इंकजेट प्रिंटर):</em>
            <br>&nbsp;&nbsp;&bull; Sprays tiny microscopic droplets of electrically charged liquid ink through microscopic nozzles onto paper (thermal bubble or piezoelectric actuators).
            <br>&nbsp;&nbsp;&bull; Uses <strong>CMYK Color Model</strong>: <strong>Cyan</strong> (blue-green), <strong>Magenta</strong> (purplish-red), <strong>Yellow</strong>, and <strong>Key (Black)</strong>.
            <br>&nbsp;&nbsp;&bull; Best for high-resolution color photographs and personal home use.
          <br>&bull; <em>Thermal Printer (थर्मल प्रिंटर):</em>
            <br>&nbsp;&nbsp;&bull; Uses a thermal print head with heated pins applied to specialized chemically treated <strong>thermochromic paper</strong> that turns dark when heated.
            <br>&nbsp;&nbsp;&bull; Requires no ink cartridge or ribbon; extremely fast, compact, and silent.
            <br>&nbsp;&nbsp;&bull; Universally used in <strong>ATM receipt dispensers, POS card swipe terminals, bus ticket machines, and supermarket billing counters</strong>.
          <br>&bull; <em>Plotters (प्लॉटर्स):</em>
            <br>&nbsp;&nbsp;&bull; Specialized vector output device that uses automated mechanical pens or ink jets to draw continuous, high-precision lines on oversized paper sheets.
            <br>&nbsp;&nbsp;&bull; Used by engineers, architects, and cartographers for <strong>CAD blueprints, circuit schematics, topographic maps, and giant hoarding flex banners</strong>. Types: Flatbed Plotter and Drum Plotter.</span>
        <span class="lang-hi"><strong>नॉन-इम्पैक्ट प्रिंटर्स (Non-Impact Printers):</strong>
          <br>&bull; <em>कार्यप्रणाली:</em> बिना किसी आघात के लेज़र बीम, रासायनिक स्याही के फुहार अथवा ताप द्वारा छपाई; बिल्कुल शांत, उच्च गुणवत्ता, परंतु <strong>कार्बन कॉपी बनाने में असमर्थ</strong>।
          <br>&bull; <em>लेज़र प्रिंटर (Laser Printer):</em>
            <br>&nbsp;&nbsp;&bull; आविष्कार <strong>गैरी स्टार्कवेदर</strong> (ज़ेरॉक्स, 1969) द्वारा।
            <br>&nbsp;&nbsp;&bull; यह एक <strong>पेज प्रिंटर</strong> है; इसमें लेज़र बीम, फोटोसेंसिटिव ड्रम और सूखे पाउडर वाली स्याही (<strong>टोनर - Toner</strong>) का प्रयोग होता है।
            <br>&nbsp;&nbsp;&bull; गति <strong>PPM (पेज प्रति मिनट)</strong> में मापी जाती है; सर्वाधिक तीव्र एवं उच्च गुणवत्ता।
          <br>&bull; <em>इंकजेट प्रिंटर (Inkjet Printer):</em>
            <br>&nbsp;&nbsp;&bull; स्याही के सूक्ष्म नोजल से तरल स्याही की बूंदों का छिड़काव करता है।
            <br>&nbsp;&nbsp;&bull; इसमें <strong>CMYK रंग मॉडल</strong> प्रयुक्त होता है: <strong>C = सायन (नीला)</strong>, <strong>M = मैजेंटा (गुलाबी/लाल)</strong>, <strong>Y = पीला</strong>, <strong>K = काला (Black)</strong>।
          <br>&bull; <em>थर्मल प्रिंटर (Thermal Printer):</em>
            <br>&nbsp;&nbsp;&bull; इसमें किसी रिबन या स्याही की आवश्यकता नहीं होती; विशेष रासायनिक <strong>थर्मोसेंसिटिव कागज</strong> पर ऊष्मा (Heat) द्वारा अक्षर उभारे जाते हैं।
            <br>&nbsp;&nbsp;&bull; <strong>एटीएम (ATM) रसीद, पीओएस (POS) मशीन, बस टिकट एवं बिलिंग काउंटरों</strong> पर व्यापक रूप से प्रयुक्त।
          <br>&bull; <em>प्लॉटर (Plotters):</em>
            <br>&nbsp;&nbsp;&bull; बड़े आकार के <strong>वेक्टर ग्राफिक्स, सीएडी (CAD) ब्लूप्रिंट, वास्तुशिल्प के नक्शे और बड़े बैनर</strong> तैयार करने हेतु प्रयुक्त विशेष आउटपुट डिवाइस।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Printer Performance Metrics & Spooling -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Printer Performance Metrics, Resolution &amp; Print Spooling</span>
    <span class="lang-hi">2. प्रिंटर निष्पादन मापदंड, रिजॉल्यूशन एवं प्रिंट स्पूलिंग</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Print Resolution (DPI):</strong>
          <br>&bull; Print quality and sharpness is quantified in <strong>DPI (Dots Per Inch)</strong>.
          <br>&bull; Measures the number of individual ink dots placed within a linear span of one inch. Standard office laser printing uses 600 to 1200 DPI; fine photo printing uses 2400 to 4800 DPI. Higher DPI = sharper printout.</span>
        <span class="lang-hi"><strong>प्रिंट रिजॉल्यूशन (DPI):</strong>
          <br>&bull; मुद्रण की गुणवत्ता और स्पष्टता को <strong>DPI (डॉट्स प्रति इंच)</strong> में मापा जाता है।
          <br>&bull; एक रैखिक इंच में स्थित स्याही के डॉट्स की संख्या; DPI जितना अधिक होगा, प्रिंट उतना ही स्पष्ट व बारीक होगा (मानक: 600 से 1200 DPI)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Printer Speed Measurement Units:</strong>
          <br>&bull; <strong>CPS (Characters Per Second):</strong> Used for Character printers (Dot Matrix, Daisy Wheel).
          <br>&bull; <strong>LPM (Lines Per Minute):</strong> Used for Line printers (Drum, Chain printers).
          <br>&bull; <strong>PPM (Pages Per Minute):</strong> Used for Page printers (Laser printers, modern office Inkjet printers).</span>
        <span class="lang-hi"><strong>प्रिंटर गति मापन इकाइयां:</strong>
          <br>&bull; <strong>CPS (कैरेक्टर प्रति सेकंड):</strong> कैरेक्टर प्रिंटर (डॉट मैट्रिक्स, डेज़ी व्हील)।
          <br>&bull; <strong>LPM (लाइन्स प्रति मिनट):</strong> लाइन प्रिंटर (ड्रम, चेन प्रिंटर)।
          <br>&bull; <strong>PPM (पेज प्रति मिनट):</strong> पेज प्रिंटर (लेज़र प्रिंटर, इंकजेट प्रिंटर)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Print Spooling (SPOOL):</strong>
          <br>&bull; <em>Full Form:</em> <strong>Simultaneous Peripheral Operations On-Line</strong>.
          <br>&bull; <em>Working:</em> A software buffer process that intercepts print jobs dispatched by the CPU and queues them in system RAM or on the hard drive.
          <br>&bull; <em>Core Advantage:</em> Because the CPU operates at gigahertz speeds while mechanical printers operate at slow millisecond rates, spooling frees up the CPU and user applications immediately without forcing the system to wait for physical printing to finish.</span>
        <span class="lang-hi"><strong>प्रिंट स्पूलिंग (SPOOL):</strong>
          <br>&bull; <em>पूर्ण रूप:</em> <strong>Simultaneous Peripheral Operations On-Line</strong>।
          <br>&bull; <em>कार्यप्रणाली:</em> सीपीयू द्वारा भेजे गए प्रिंट कार्यों को एक अस्थायी बफर (रैम या हार्ड डिस्क) में कतारबद्ध (Queue) करता है।
          <br>&bull; <em>महत्व:</em> चूंकि प्रिंटर की गति सीपीयू की तुलना में अत्यंत धीमी होती है, स्पूलिंग के कारण सीपीयू प्रिंटर के खाली होने की प्रतीक्षा किए बिना तुरंत अन्य कार्यों हेतु मुक्त हो जाता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Mobile & Tablet Hardware Architecture -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Mobile &amp; Tablet Architecture: SoC, Displays &amp; Sensors</span>
    <span class="lang-hi">3. मोबाइल एवं टैबलेट वास्तुकला: SoC, डिस्प्ले एवं अंतर्निहित सेंसर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>System on Chip (SoC):</strong>
          <br>&bull; Unlike desktop computers with separate motherboards, CPUs, and GPUs, mobile devices integrate all core functional subsystems onto a single integrated silicon chip called <strong>SoC</strong>.
          <br>&bull; <em>Integrated Components:</em> Multicore CPU (ARM RISC architecture), GPU (graphics), DSP (digital signal processor), Cellular Modem (5G/4G), ISP (Image Signal Processor for camera), and NPU (Neural Processing Unit for on-device AI).
          <br>&bull; <em>Leading SoC Platforms:</em> Qualcomm Snapdragon, Apple A-series (Bionic)/M-series, MediaTek Dimensity, Samsung Exynos, Google Tensor.</span>
        <span class="lang-hi"><strong>सिस्टम ऑन चिप (SoC):</strong>
          <br>&bull; डेस्कटॉप के विपरीत, मोबाइल और टैबलेट में अलग-अलग घटकों के बजाय एक ही सिलिकॉन चिप पर सभी मुख्य घटक समाहित होते हैं, जिसे <strong>SoC</strong> कहते हैं।
          <br>&bull; <em>समाहित घटक:</em> CPU (ARM आधारित), GPU (ग्राफिक्स), मॉडेम (5G/4G), ISP (कैमरा इमेज प्रोसेसर), और NPU (AI प्रोसेसर)।
          <br>&bull; <em>प्रमुख प्रोसेसर:</em> क्वालकॉम स्नैपड्रैगन, ऐप्पल ए-सीरीज़, मीडियाटेक डाइमेंसिटी, सैमसंग एक्सीनॉस, गूगल टेंसर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Touchscreen Display Technologies:</strong>
          <br>&bull; <em>Capacitive Touchscreen:</em> Coated with a transparent conductive indium tin oxide (ITO) layer. Detects touches via electrical conductivity changes when human fingers touch the glass. Supports multi-touch gestures (pinch-to-zoom). Does not respond to ordinary non-conductive plastic pens.
          <br>&bull; <em>Resistive Touchscreen (Older):</em> Uses two flexible conductive sheets separated by microscopic spacer dots; requires physical mechanical pressure; supports single touch only.</span>
        <span class="lang-hi"><strong>टचस्क्रीन तकनीक:</strong>
          <br>&bull; <em>कैपेसिटिव टचस्क्रीन:</em> आधुनिक स्मार्टफोन और टैबलेट में प्रयुक्त; मानव शरीर की प्राकृतिक विद्युत चालकता से स्पर्श को पहचानती है; मल्टी-टच (पिंच ज़ूम) समर्थित करती है।
          <br>&bull; <em>रेसिस्टिव टचस्क्रीन:</em> पुरानी तकनीक जो स्क्रीन पर भौतिक दबाव डालने पर काम करती थी; केवल सिंगल टच समर्थित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Built-in Mobile Sensors (मोबाइल के अंतर्निहित सेंसर):</strong>
          <br>&bull; <em>Accelerometer:</em> Detects linear acceleration forces along 3 axes; automatically switches screen orientation between <strong>Portrait (Vertical)</strong> and <strong>Landscape (Horizontal)</strong>; counts steps in fitness apps.
          <br>&bull; <em>Gyroscope:</em> Measures angular rotational velocity and orientation in 3D space; provides ultra-smooth motion control in mobile gaming and optical image stabilization (OIS).
          <br>&bull; <em>Proximity Sensor:</em> Infrared LED sensor located near the top earpiece; <strong>automatically switches off the display and touch screen when the phone is held close to the ear</strong> during a call to prevent accidental face touches.
          <br>&bull; <em>Ambient Light Sensor:</em> Measures external room light intensity; automatically adjusts screen brightness to conserve battery power.
          <br>&bull; <em>Magnetometer:</em> Solid-state electronic Hall-effect compass detecting Earth's magnetic field; powers navigation and Google Maps direction pointer.</span>
        <span class="lang-hi"><strong>मोबाइल के प्रमुख अंतर्निहित सेंसर:</strong>
          <br>&bull; <em>एक्सेलेरोमीटर (Accelerometer):</em> रैखिक गति मापता है; स्क्रीन को <strong>पोर्ट्रेट (लंबवत) एवं लैंडस्केप (क्षैतिज)</strong> मोड में स्वतः घुमाता है; स्टेप्स गिनता है।
          <br>&bull; <em>जाइरोस्कोप (Gyroscope):</em> 3D स्पेस में फोन के कोणीय घुमाव (रोटेशन) को मापता है; मोबाइल गेमिंग व कैमरा स्थिरीकरण (OIS) में प्रयुक्त।
          <br>&bull; <em>प्रॉक्सिमिटी सेंसर (Proximity Sensor):</em> कॉल के दौरान जब फोन कान के पास लाया जाता है, तो यह <strong>स्क्रीन की लाइट और टच को स्वतः बंद कर देता है</strong> ताकि अनपेक्षित टच न हो।
          <br>&bull; <em>एम्बिएंट लाइट सेंसर:</em> कमरे की रोशनी के अनुसार स्क्रीन की चमक (Brightness) को स्वतः नियंत्रित करता है।
          <br>&bull; <em>मैग्नेटोमीटर:</em> डिजिटल कंपास जो पृथ्वी के चुंबकीय उत्तर को पहचानकर मैप्स में दिशा दिखाता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Mobile OS & Communication Standards -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Mobile Operating Systems, Cellular Generations &amp; Connectivity</span>
    <span class="lang-hi">4. मोबाइल ऑपरेटिंग सिस्टम, सेलुलर पीढ़ियां एवं कनेक्टिविटी</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Mobile Operating Systems:</strong>
          <br>&bull; <em>Android:</em> Open-source mobile OS based on a modified <strong>Linux kernel</strong>; originally founded by Andy Rubin (2003) and acquired by Google (2005). Uses <strong>APK (Android Package)</strong> / AAB installation files. Governed by the Open Handset Alliance (OHA).
          <br>&bull; <em>iOS:</em> Proprietary closed-source Unix-based mobile OS developed exclusively by Apple Inc. for the iPhone; uses <strong>IPA</strong> app installation archives.
          <br>&bull; <em>BharOS:</em> Indigenous Indian mobile operating system incubated at <strong>IIT Madras</strong> (JandK Operations); built on AOSP (Android Open Source Project) with 'No Default Apps' (NDA) for enhanced user privacy and national cybersecurity.</span>
        <span class="lang-hi"><strong>मोबाइल ऑपरेटिंग सिस्टम:</strong>
          <br>&bull; <em>एंड्रॉयड (Android):</em> <strong>लिनक्स कर्नल</strong> पर आधारित ओपन-सोर्स ओएस; गूगल द्वारा 2005 में अधिग्रहीत। इसके इंस्टॉलेशन पैकेज का एक्सटेंशन <strong>.apk</strong> (Android Package) होता है।
          <br>&bull; <em>iOS:</em> ऐप्पल (Apple) द्वारा केवल iPhone हेतु विकसित प्रोप्राइटरी क्लोज्ड-सोर्स यूनिक्स-आधारित ओएस।
          <br>&bull; <em>BharOS (भारओएस):</em> भारत का स्वदेशी मोबाइल ऑपरेटिंग सिस्टम; <strong>IIT मद्रास</strong> के इनक्यूबेटेड स्टार्टअप (JandKops) द्वारा विकसित; डेटा सुरक्षा व गोपनीयता हेतु 'नो डिफॉल्ट ऐप्स' (NDA) नीति।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Mobile Identifiers: IMEI &amp; SIM:</strong>
          <br>&bull; <em>IMEI (International Mobile Station Equipment Identity):</em> A globally unique <strong>15-digit number</strong> assigned to every cellular mobile phone hardware. Dual-SIM phones possess two distinct IMEI numbers. Dialing <strong>*#06#</strong> on any mobile handset displays its IMEI. Used by law enforcement and telecom operators to blacklist and block stolen phones.
          <br>&bull; <em>SIM (Subscriber Identity Module):</em> An integrated circuit chip securely storing the IMSI (International Mobile Subscriber Identity) and cryptographic keys to authenticate the phone on cellular carrier networks. Evolutions: Standard SIM &rarr; Micro SIM &rarr; Nano SIM &rarr; <strong>eSIM</strong> (permanently embedded virtual SIM soldered directly onto the motherboard).</span>
        <span class="lang-hi"><strong>मोबाइल पहचानकर्ता: IMEI एवं SIM:</strong>
          <br>&bull; <em>IMEI (इंटरनेशनल मोबाइल स्टेशन इक्विपमेंट आइडेंटिटी):</em> प्रत्येक मोबाइल फोन का अद्वितीय <strong>15 अंकों का हार्डवेयर नंबर</strong>; फोन पर <strong>*#06#</strong> डायल करके देखा जा सकता है; चोरी हुए फोन को ब्लॉक करने में प्रयुक्त।
          <br>&bull; <em>SIM (सब्सक्राइबर आइडेंटिटी मॉड्यूल):</em> उपयोगकर्ता की पहचान और नेटवर्क प्रमाणीकरण चिप; आधुनिक रूप: <strong>eSIM (एम्बेडेड सिम)</strong> जो फोन में पहले से स्थाई रूप से जुड़ी होती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Short-Range Mobile Connectivity:</strong>
          <br>&bull; <em>Bluetooth:</em> Short-range radio frequency standard (IEEE 802.15.1) operating on the unlicensed <strong>2.4 GHz ISM band</strong>; range ~10 meters; creates a PAN (Personal Area Network) or Piconet.
          <br>&bull; <em>NFC (Near Field Communication):</em> Ultra-short-range wireless communication based on RFID (13.56 MHz frequency); operating distance <strong>&le; 4 cm</strong>; powers contactless tap-and-pay card payments, e-ticketing, and secure access tags.
          <br>&bull; <em>USB OTG (On-The-Go):</em> Hardware standard allowing mobile devices to switch from USB peripheral mode to <strong>USB Host mode</strong>, allowing direct connection of pendrives, keyboards, mice, and game controllers.</span>
        <span class="lang-hi"><strong>अल्प-दूरी वायरलेस कनेक्टिविटी:</strong>
          <br>&bull; <em>ब्लूटूथ (Bluetooth):</em> 2.4 GHz ISM बैंड पर कार्य करने वाली अल्प-दूरी रेडियो तकनीक (IEEE 802.15.1); सीमा लगभग 10 मीटर; पैन (PAN) नेटवर्क बनाती है।
          <br>&bull; <em>NFC (नियर फील्ड कम्युनिकेशन):</em> <strong>4 सेमी से कम दूरी</strong> पर कार्य करने वाली वायरलेस तकनीक (13.56 MHz); कॉन्टैक्टलेस पेमेंट (Tap &amp; Pay) एवं मेट्रो कार्ड में प्रयुक्त।
          <br>&bull; <em>USB OTG (ऑन-द-गो):</em> मोबाइल फोन को होस्ट बनाकर पेनड्राइव, माउस या कीबोर्ड को सीधे फोन से जोड़ने की सुविधा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Cellular Generations (1G to 5G):</strong>
          <br>&bull; <em>1G:</em> Analog voice only (AMPS).
          <br>&bull; <em>2G:</em> Digital voice and SMS (GSM, CDMA); GPRS introduced packet data (up to 56 kbps).
          <br>&bull; <em>3G:</em> High-speed mobile broadband (UMTS, WCDMA, HSPA); video calling and web browsing.
          <br>&bull; <em>4G LTE &amp; VoLTE:</em> Pure IP packet-switched architecture; <strong>VoLTE (Voice over LTE)</strong> routes high-definition voice calls over 4G data networks without falling back to 2G/3G.
          <br>&bull; <em>5G NR (New Radio):</em> Speeds up to 10-20 Gbps; ultra-low latency (&lt; 1 ms); supports massive IoT (mMTC) and smart autonomous systems.</span>
        <span class="lang-hi"><strong>सेलुलर पीढ़ियां (1G से 5G):</strong>
          <br>&bull; <em>1G:</em> एनालॉग वॉयस कॉलिंग।
          <br>&bull; <em>2G:</em> डिजिटल वॉयस एवं एसएमएस (GSM/CDMA); GPRS डेटा की शुरुआत।
          <br>&bull; <em>3G:</em> मोबाइल ब्रॉडबैंड इंटरनेट एवं वीडियो कॉलिंग (UMTS/HSPA)।
          <br>&bull; <em>4G LTE एवं VoLTE:</em> ऑल-आईपी पैकेट स्विचिंग नेटवर्क; <strong>VoLTE</strong> के माध्यम से 4G डेटा पर हाई-डेफिनिशन वॉयस कॉलिंग।
          <br>&bull; <em>5G:</em> 10-20 Gbps तक तीव्र गति, 1 मिलीसेकंड से कम लेटेंसी एवं विशाल IoT नेटवर्किंग।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Rapid Revision Matrix & UPSSSC Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">5. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Exam Question / Core Concept</span>
            <span class="lang-hi">परीक्षा प्रश्न / मुख्य संकल्पना</span>
          </th>
          <th>
            <span class="lang-en">Exact Answer &amp; UPSSSC Fact</span>
            <span class="lang-hi">सटीक उत्तर एवं महत्वपूर्ण तथ्य</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Unit of measurement for printer resolution</span>
            <span class="lang-hi">प्रिंटर के रिजॉल्यूशन को मापने की इकाई</span>
          </td>
          <td>
            <span class="lang-en"><strong>DPI (Dots Per Inch)</strong>.</span>
            <span class="lang-hi"><strong>DPI (डॉट्स प्रति इंच)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Speed measurement unit for Laser Printers</span>
            <span class="lang-hi">लेज़र प्रिंटर की गति मापने की इकाई</span>
          </td>
          <td>
            <span class="lang-en"><strong>PPM (Pages Per Minute)</strong>.</span>
            <span class="lang-hi"><strong>PPM (पेज प्रति मिनट)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Printer that can produce carbon copies</span>
            <span class="lang-hi">कार्बन कॉपी निकालने में सक्षम प्रिंटर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Impact Printers (Dot Matrix, Daisy Wheel)</strong>. Non-impact cannot.</span>
            <span class="lang-hi"><strong>इम्पैक्ट प्रिंटर (डॉट मैट्रिक्स प्रिंटर)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Printer universally used in ATM and POS machines</span>
            <span class="lang-hi">एटीएम एवं पीओएस स्वाइप मशीनों में प्रयुक्त प्रिंटर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Thermal Printer</strong> (uses heat-sensitive thermochromic paper).</span>
            <span class="lang-hi"><strong>थर्मल प्रिंटर</strong> (ऊष्मा-संवेदनशील रासायनिक कागज पर)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Color components in Inkjet Printer (CMYK)</span>
            <span class="lang-hi">इंकजेट प्रिंटर में CMYK के चार घटक रंग</span>
          </td>
          <td>
            <span class="lang-en"><strong>Cyan, Magenta, Yellow, and Key (Black)</strong>.</span>
            <span class="lang-hi"><strong>सायन, मैजेंटा, पीला, एवं काला (Black)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Temporary holding buffer for print tasks</span>
            <span class="lang-hi">प्रिंट कार्यों को कतार में रखने वाला बफर सॉफ्टवेयर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Print Spooler (SPOOL)</strong>: Simultaneous Peripheral Operations On-Line.</span>
            <span class="lang-hi"><strong>प्रिंट स्पूलर (SPOOL)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Number of digits in mobile IMEI number</span>
            <span class="lang-hi">मोबाइल के IMEI नंबर में कुल कितने अंक होते हैं?</span>
          </td>
          <td>
            <span class="lang-en"><strong>15 digits</strong> (Check hardware code via <strong>*#06#</strong>).</span>
            <span class="lang-hi"><strong>15 अंक</strong> (जांच कोड: <strong>*#06#</strong>)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Sensor that switches off screen during phone call</span>
            <span class="lang-hi">फोन कॉल के दौरान कान के पास ले जाने पर स्क्रीन बंद करने वाला सेंसर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Proximity Sensor</strong>.</span>
            <span class="lang-hi"><strong>प्रॉक्सिमिटी सेंसर (Proximity Sensor)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Operating system kernel that Android is built upon</span>
            <span class="lang-hi">एंड्रॉयड ऑपरेटिंग सिस्टम किस कर्नल पर आधारित है?</span>
          </td>
          <td>
            <span class="lang-en"><strong>Linux Kernel</strong>.</span>
            <span class="lang-hi"><strong>लिनक्स कर्नल (Linux Kernel)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">India's indigenous mobile OS developed by IIT Madras</span>
            <span class="lang-hi">आईआईटी मद्रास द्वारा विकसित भारत का स्वदेशी मोबाइल ओएस</span>
          </td>
          <td>
            <span class="lang-en"><strong>BharOS</strong> (developed by JandK Operations).</span>
            <span class="lang-hi"><strong>भारओएस (BharOS)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Short-range wireless technology for contactless Tap-to-Pay</span>
            <span class="lang-hi">कॉन्टैक्टलेस टैप-टू-पे भुगतान हेतु प्रयुक्त अल्प-दूरी तकनीक</span>
          </td>
          <td>
            <span class="lang-en"><strong>NFC (Near Field Communication)</strong> - operational distance &lt; 4 cm.</span>
            <span class="lang-hi"><strong>NFC (नियर फील्ड कम्युनिकेशन)</strong> - दूरी &lt; 4 सेमी।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-computer", "operation-of-printer-tablet-and-mobile", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_printer_mobile_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
