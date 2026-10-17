import os
import re

def build_input_output_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Input, Output &amp; Interface Ports Architecture</span>
    <span class="lang-hi">माइंड मैप: इनपुट, आउटपुट एवं इंटरफेस पोर्ट्स वास्तुकला</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Computer Peripherals Interface] --> B[Input Devices]
    A --> C[Output Devices]
    A --> D[Dual I/O Devices]
    A --> E[Hardware Ports & Interfaces]

    B --> B1[Text & Keystroke: QWERTY Keyboard, Keypad]
    B --> B2[Pointing: Mouse, Trackball, Touchpad, Light Pen, Stylus]
    B --> B3[Optical & Scanning: OMR, OCR, MICR, Barcode, QR Code]
    B --> B4[Audio/Visual: Microphone, Webcam, Biometric Scanners]

    C --> C1[Soft Copy: Monitors CRT, LCD, LED, OLED, Projectors]
    C --> C2[Audio: Speakers, Headphones, DAC Sound Card]
    C --> C3[Hard Copy: Printers & Plotters Note: Detailed in Printers Topic]

    D --> D1[Touchscreens, Multi-Function Devices MFD]
    D --> D2[Modems, Network Interface Cards NIC]
    D --> D3[VR Headsets, Smart Interactive Boards]

    E --> E1[Legacy: Serial RS-232, Parallel DB-25, PS/2 Purple/Green]
    E --> E2[Modern: USB Type-A/B/C, HDMI Audio+Video, DisplayPort, VGA 15-pin]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[कंप्यूटर परिधीय इंटरफेस] --> B[इनपुट उपकरण]
    A --> C[आउटपुट उपकरण]
    A --> D[उभयनिष्ठ इनपुट/आउटपुट युक्तियां]
    A --> E[हार्डवेयर पोर्ट्स एवं इंटरफेस]

    B --> B1[टेक्स्ट/कुंजी: QWERTY कीबोर्ड, कीपैड]
    B --> B2[पॉइंटिंग: माउस, ट्रैकबॉल, टचपैड, लाइट पेन, डिजिटाइज़र स्टायलस]
    B --> B3[ऑप्टिकल व स्कैनर: OMR, OCR, MICR, बारकोड, QR कोड स्कैनर]
    B --> B4[ध्वनि/दृश्य: माइक्रोफोन, वेबकैम, बायोमेट्रिक स्कैनर]

    C --> C1[सॉफ्ट कॉपी: मॉनिटर्स CRT, LCD, LED, OLED, प्रोजेक्टर]
    C --> C2[ध्वनि आउटपुट: स्पीकर्स, हेडफ़ोन, DAC साउंड कार्ड]
    C --> C3[हार्ड कॉपी: प्रिंटर्स एवं प्लॉटर्स]

    D --> D1[टचस्क्रीन, मल्टी-फंक्शन प्रिंटर MFD]
    D --> D2[मॉडेम, नेटवर्क कार्ड NIC]
    D --> D3[वीआर हेडसेट, इंटरैक्टिव स्मार्ट बोर्ड]

    E --> E1[पुरातन पोर्ट: सीरियल RS-232, पैरेलल DB-25, PS/2 बैंगनी/हरा]
    E --> E2[आधुनिक पोर्ट: USB Type-A/B/C, HDMI ऑडियो+वीडियो, डिस्प्लेपोर्ट, VGA 15-पिन]
    </div>
  </div>
</div>

<!-- Card 2: Input Devices Deep-Dive -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Input Devices Deep-Dive: Keyboard, Pointing &amp; Scanning Hardware</span>
    <span class="lang-hi">1. इनपुट उपकरण गहन विश्लेषण: कीबोर्ड, पॉइंटिंग एवं स्कैनिंग हार्डवेयर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Computer Keyboard (कीबोर्ड):</strong>
          <br>&bull; Most primary text input device; invented in its modern layout by <strong>Christopher Latham Sholes</strong> (1868).
          <br>&bull; <em>Standard Layouts:</em> <strong>QWERTY</strong> (standard 101 to 104 keys); alternate layouts include DVORAK and AZERTY (used in France).
          <br>&bull; <em>Key Classifications:</em>
            <br>&nbsp;&nbsp;&bull; <strong>Alphanumeric Keys:</strong> Letters (A-Z) and numbers (0-9).
            <br>&nbsp;&nbsp;&bull; <strong>Function Keys (F1 to F12):</strong> Positioned on top row; execute specific dedicated operating system and application shortcuts.
            <br>&nbsp;&nbsp;&bull; <strong>Toggle Keys (टॉगल कुंजियां):</strong> Keys that switch between two states (ON / OFF): <strong>Caps Lock</strong>, <strong>Num Lock</strong>, and <strong>Scroll Lock</strong>.
            <br>&nbsp;&nbsp;&bull; <strong>Modifier Keys (संशोधक कुंजियां):</strong> Keys that do nothing alone but modify the action of another key when pressed simultaneously: <strong>Shift</strong>, <strong>Ctrl (Control)</strong>, and <strong>Alt (Alternate)</strong>.
            <br>&nbsp;&nbsp;&bull; <strong>Navigation Keys:</strong> Arrow keys, Home (start of line), End (end of line), Page Up, Page Down, Insert, Delete.
            <br>&nbsp;&nbsp;&bull; <strong>Special Keys:</strong> Esc (Escape - cancels current task/dialog), Spacebar (longest key on keyboard), Enter/Return (executes command/new line), Backspace (erases character to the <em>left</em> of cursor), Delete (erases character to the <em>right</em> of cursor).</span>
        <span class="lang-hi"><strong>कंप्यूटर कीबोर्ड:</strong>
          <br>&bull; सर्वाधिक प्रयुक्त प्राथमिक इनपुट डिवाइस; आधुनिक लेआउट के आविष्कारक <strong>क्रिस्टोफर लैथम शोल्स</strong> (1868) थे।
          <br>&bull; <em>मानक लेआउट:</em> <strong>QWERTY</strong> (मानक 101 से 104 कुंजियां); अन्य लेआउट: DVORAK और AZERTY।
          <br>&bull; <em>कुंजियों का वर्गीकरण:</em>
            <br>&nbsp;&nbsp;&bull; <strong>अल्फान्यूमेरिक कुंजियां:</strong> अक्षर (A-Z) एवं अंक (0-9)।
            <br>&nbsp;&nbsp;&bull; <strong>फंक्शन कुंजियां (F1 से F12):</strong> शीर्ष पंक्ति पर स्थित; विशेष कार्यों हेतु शॉर्टकट।
            <br>&nbsp;&nbsp;&bull; <strong>टॉगल कुंजियां (Toggle Keys):</strong> जो दबाने पर दो अवस्थाओं (चालू/बंद) के बीच बदलती हैं: <strong>Caps Lock</strong>, <strong>Num Lock</strong>, एवं <strong>Scroll Lock</strong>।
            <br>&nbsp;&nbsp;&bull; <strong>मॉडिफायर कुंजियां (Modifier Keys):</strong> जो अकेले कार्य नहीं करतीं बल्कि किसी अन्य कुंजी के साथ मिलकर कार्य करती हैं: <strong>Shift</strong>, <strong>Ctrl</strong>, एवं <strong>Alt</strong>।
            <br>&nbsp;&nbsp;&bull; <strong>नेविगेशन कुंजियां:</strong> Arrow keys, Home (पंक्ति के प्रारंभ में), End (पंक्ति के अंत में), Page Up, Page Down।
            <br>&nbsp;&nbsp;&bull; <strong>Backspace vs Delete:</strong> <em>Backspace</em> कर्सर के <strong>बाईं ओर (Left)</strong> के अक्षर को मिटाता है; <em>Delete</em> कर्सर के <strong>दायीं ओर (Right)</strong> के अक्षर को मिटाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Pointing Devices (पॉइंटिंग युक्तियां):</strong>
          <br>&bull; <em>Mouse (माउस):</em> Invented by <strong>Douglas Engelbart</strong> in 1964 (initially wooden with two metal wheels). Modern variants: Mechanical (trackball inside), Optical (LED sensor), Laser (high precision). Standard actions: Left click (select), Right click (context menu), Double click (open), Drag and Drop.
          <br>&bull; <em>Trackball:</em> Inverted mouse where the user rolls a stationary exposed ball with fingers/thumb; used in CAD, air traffic control, radar stations, and ultrasound consoles where desk space is restricted.
          <br>&bull; <em>Touchpad / Trackpad:</em> Flat capacitive touch-sensitive surface common on laptops; translates finger motion to screen coordinates.
          <br>&bull; <em>Pointing Stick (TrackPoint):</em> Small isometric rubber joystick embedded between the 'G', 'H', and 'B' keys on laptop keyboards (popularized by IBM ThinkPad).
          <br>&bull; <em>Light Pen:</em> Photosensitive electro-optical wand used to draw or point directly on CRT phosphor screens.
          <br>&bull; <em>Digitizing Tablet / Graphic Tablet:</em> Electronic pressure-sensitive flat pad with a cordless <strong>Stylus</strong>; used by architects, digital artists, and cartographers for CAD and vector drawing.</span>
        <span class="lang-hi"><strong>पॉइंटिंग युक्तियां (Pointing Devices):</strong>
          <br>&bull; <em>माउस:</em> आविष्कार <strong>डगलस एंजेलबर्ट</strong> द्वारा 1964 में लकड़ी के ब्लॉक से किया गया था। प्रकार: मैकेनिकल, ऑप्टिकल (एलईडी), और लेजर माउस।
          <br>&bull; <em>ट्रैकबॉल (Trackball):</em> माउस का उल्टा रूप जिसमें गेंद ऊपर स्थिर रहती है और अंगुली से घुमाई जाती है; एयर ट्रैफिक कंट्रोल, रडार एवं कैड (CAD) वर्कस्टेशन में प्रयुक्त।
          <br>&bull; <em>टचपैड (Touchpad):</em> लैपटॉप में प्रयुक्त सपाट कैपेसिटिव सतह।
          <br>&bull; <em>पॉइंटिंग स्टिक (TrackPoint):</em> लैपटॉप कीबोर्ड पर 'G', 'H', 'B' कुंजियों के बीच स्थित छोटी लाल रबर जैसी बटन।
          <br>&bull; <em>लाइट पेन (Light Pen):</em> प्रकाश-संवेदनशील पेन जो CRT स्क्रीन पर सीधे लिखने/चित्र बनाने के काम आता है।
          <br>&bull; <em>ग्राफिक टैबलेट / डिजिटाइज़र:</em> कॉर्डलेस <strong>स्टायलस</strong> के साथ प्रयुक्त पैड; सीएडी (CAD) डिजाइनिंग एवं डिजिटल चित्रकारी हेतु।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Optical &amp; Recognition Scanning Devices (पहचान एवं स्कैनिंग उपकरण):</strong>
          <br>&bull; <em>Optical Mark Reader (OMR):</em> Evaluates darkened pencil or pen marks on pre-printed forms by measuring reflected light intensity; universally used for competitive exam answer sheets.
          <br>&bull; <em>Optical Character Recognition (OCR):</em> Scans printed or handwritten documents and converts optical pixel images of letters into editable ASCII/Unicode text.
          <br>&bull; <em>Magnetic Ink Character Recognition (MICR):</em> Reads characters printed with magnetic iron-oxide ink (E-13B font) on the bottom band of bank cheques. Contains a <strong>9-digit routing code</strong>:
            <br>&nbsp;&nbsp;&bull; <strong>First 3 digits:</strong> City Code (corresponds to PIN code).
            <br>&nbsp;&nbsp;&bull; <strong>Middle 3 digits:</strong> Bank Code.
            <br>&nbsp;&nbsp;&bull; <strong>Last 3 digits:</strong> Branch Code.
          <br>&bull; <em>Barcode Reader (BCR):</em> Handheld optical scanner reading 1D black-and-white parallel stripes of varying widths representing <strong>Universal Product Code (UPC)</strong> or EAN-13.
          <br>&bull; <em>QR Code (Quick Response Code) Reader:</em> 2D matrix barcode invented in 1994 by <strong>Denso Wave</strong> (Japan); stores up to 7,089 numeric or 4,296 alphanumeric characters; features 3 large positioning squares at corners; readable omnidirectionally.
          <br>&bull; <em>Biometric Sensors:</em> Captures biological characteristics for identity authentication: Fingerprint scanner, Iris/Retina scanner, Facial recognition, Voice recognition.</span>
        <span class="lang-hi"><strong>ऑप्टिकल एवं पहचान स्कैनिंग उपकरण:</strong>
          <br>&bull; <em>OMR (ऑप्टिकल मार्क रीडर):</em> परीक्षा उत्तर-पुस्तिकाओं (OMR शीट) पर पेंसिल या पेन के गोलों की उपस्थिति व अनुपस्थिति को परावर्तित प्रकाश द्वारा जांचता है।
          <br>&bull; <em>OCR (ऑप्टिकल कैरेक्टर रिकॉग्निशन):</em> मुद्रित अथवा हस्तलिखित पृष्ठ की छवि को संपादन योग्य डिजिटल टेक्स्ट (ASCII) में परिवर्तित करता है।
          <br>&bull; <em>MICR (मैग्नेटिक इंक कैरेक्टर रिकॉग्निशन):</em> बैंक चेकों के नीचे विशेष चुंबकीय आयरन ऑक्साइड स्याही से छपे <strong>9 अंकों के कोड</strong> को पढ़ता है:
            <br>&nbsp;&nbsp;&bull; <strong>प्रथम 3 अंक:</strong> शहर कोड (City Code)।
            <br>&nbsp;&nbsp;&bull; <strong>मध्य 3 अंक:</strong> बैंक कोड (Bank Code)।
            <br>&nbsp;&nbsp;&bull; <strong>अंतिम 3 अंक:</strong> शाखा कोड (Branch Code)।
          <br>&bull; <em>बारकोड रीडर (BCR):</em> उत्पादों पर छपी काली-सफेद 1D पट्टियों (UPC कोड) को लेजर बीम द्वारा पढ़ता है।
          <br>&bull; <em>QR कोड (क्विक रिस्पांस कोड):</em> 1994 में <strong>डेंसो वेव (जापान)</strong> द्वारा आविष्कृत 2D मैट्रिक्स बारकोड; 7,089 अंकों तक डेटा रख सकता है; कोनों पर 3 पहचान वर्ग होते हैं।
          <br>&bull; <em>बायोमेट्रिक स्कैनर:</em> उंगलियों के निशान (फिंगरप्रिंट), आंख की पुतली (आइरिस/रेटिना) व चेहरे की पहचान हेतु प्रयुक्त।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Output Devices Deep-Dive -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Output Devices Deep-Dive: Monitors, Audio &amp; Hard Copy Displays</span>
    <span class="lang-hi">2. आउटपुट उपकरण गहन विश्लेषण: मॉनिटर्स, ऑडियो एवं हार्ड कॉपी डिस्प्ले</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Soft Copy vs Hard Copy Output:</strong>
          <br>&bull; <em>Soft Copy:</em> Intangible, electronic output displayed on screens or heard through speakers; temporary, modifiable, requires electrical power to view.
          <br>&bull; <em>Hard Copy:</em> Permanent tangible physical output printed on paper, film, or flex boards (via Printers and Plotters).</span>
        <span class="lang-hi"><strong>सॉफ्ट कॉपी बनाम हार्ड कॉपी आउटपुट:</strong>
          <br>&bull; <em>सॉफ्ट कॉपी (Soft Copy):</em> इलेक्ट्रॉनिक रूप से स्क्रीन पर दिखाई देने वाला अथवा स्पीकर से सुनाई देने वाला अस्थायी आउटपुट; बिजली बंद होने पर नष्ट हो जाता है।
          <br>&bull; <em>हार्ड कॉपी (Hard Copy):</em> कागज या भौतिक माध्यम पर मुद्रित स्थायी आउटपुट (प्रिंटर और प्लॉटर द्वारा)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Monitors &amp; Visual Display Units (VDU):</strong>
          <br>&bull; <em>CRT (Cathode Ray Tube):</em> Bulky older technology; uses an electron gun firing beams through magnetic deflection coils onto an inner phosphor-coated screen.
          <br>&bull; <em>LCD (Liquid Crystal Display):</em> Thin display using liquid crystals sandwiched between polarizing filters; does not emit light directly, relies on cold cathode fluorescent lamps (<strong>CCFL</strong>) for backlighting.
          <br>&bull; <em>LED (Light Emitting Diode):</em> LCD screen backlit by an array of energy-efficient semiconductor LEDs; produces brighter images and consumes 40% less power than CCFL LCDs.
          <br>&bull; <em>OLED (Organic LED) &amp; AMOLED:</em> Emissive display where each organic carbon-based pixel emits its own light; requires no backlight; delivers true deep blacks, infinite contrast ratio, and wide viewing angles.
          <br>&bull; <em>Key Monitor Performance Specifications:</em>
            <br>&nbsp;&nbsp;&bull; <strong>Pixel (Picture Element):</strong> The smallest addressable illumination point on a display screen.
            <br>&nbsp;&nbsp;&bull; <strong>Resolution (रिजॉल्यूशन):</strong> Total number of distinct pixels displayed horizontally and vertically (e.g., Full HD = 1920 &times; 1080; 4K UHD = 3840 &times; 2160). Higher resolution = sharper image.
            <br>&nbsp;&nbsp;&bull; <strong>Dot Pitch / Pixel Pitch:</strong> The diagonal distance between two adjacent phosphor dots/pixels of the same color (measured in millimeters); <em>smaller dot pitch yields sharper images</em> (&le; 0.28 mm is desirable).
            <br>&nbsp;&nbsp;&bull; <strong>Refresh Rate (रिफ्रेश रेट):</strong> Number of times the screen image is redrawn per second; measured in <strong>Hertz (Hz)</strong> (standard 60 Hz; gaming monitors 144 Hz - 240 Hz).
            <br>&nbsp;&nbsp;&bull; <strong>Aspect Ratio:</strong> Ratio of screen width to height (e.g., 4:3 for CRT, 16:9 for modern widescreen displays).</span>
        <span class="lang-hi"><strong>मॉनिटर्स एवं विज़ुअल डिस्प्ले यूनिट (VDU):</strong>
          <br>&bull; <em>CRT (कैथोड रे ट्यूब):</em> इलेक्ट्रॉन गन द्वारा फॉस्फोर लेपित स्क्रीन पर बीम डालकर चित्र बनाने वाली पुरातन तकनीक।
          <br>&bull; <em>LCD (लिक्विड क्रिस्टल डिस्प्ले):</em> पोलराइज़्ड परतों के बीच तरल क्रिस्टल युक्त फ्लैट पैनल; पीछे से CCFL ट्यूब की रोशनी (बैकलाइट) की आवश्यकता होती है।
          <br>&bull; <em>LED (लाइट एमिटिंग डायोड):</em> बैकलाइट के रूप में एलईडी डायोड का प्रयोग करने वाला उन्नत एलसीडी मॉनिटर; कम बिजली खपत।
          <br>&bull; <em>OLED (ऑर्गेनिक एलईडी):</em> प्रत्येक कार्बनिक पिक्सेल स्वयं प्रकाश उत्सर्जित करता है; किसी बैकलाइट की आवश्यकता नहीं; सर्वोत्तम कंट्रास्ट एवं शुद्ध काला रंग।
          <br>&bull; <em>मॉनिटर के प्रमुख तकनीकी मापदंड:</em>
            <br>&nbsp;&nbsp;&bull; <strong>पिक्सेल (Pixel):</strong> स्क्रीन पर चित्र की सबसे छोटी इकाई।
            <br>&nbsp;&nbsp;&bull; <strong>रिजॉल्यूशन:</strong> स्क्रीन पर क्षैतिज व लंबवत पिक्सेल की कुल संख्या (Full HD = 1920 &times; 1080; 4K = 3840 &times; 2160)।
            <br>&nbsp;&nbsp;&bull; <strong>डॉट पिच (Dot Pitch):</strong> दो समान रंग के निकटवर्ती पिक्सेल के बीच की दूरी (मिलीमीटर में); <em>डॉट पिच जितनी कम होगी, चित्र उतना ही स्पष्ट होगा</em>।
            <br>&nbsp;&nbsp;&bull; <strong>रिफ्रेश रेट:</strong> स्क्रीन द्वारा प्रति सेकंड चित्र को पुनः बनाए जाने की दर; <strong>हर्ट्ज़ (Hz)</strong> में मापी जाती है।
            <br>&nbsp;&nbsp;&bull; <strong>पहलू अनुपात (Aspect Ratio):</strong> स्क्रीन की चौड़ाई व ऊंचाई का अनुपात (मानक: 16:9)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Audio Output Hardware:</strong>
          <br>&bull; <em>Sound Card (ध्वनि कार्ड):</em> Internal expansion card containing a <strong>DAC (Digital to Analog Converter)</strong> that transforms digital binary sound files into continuous electrical analog sound waves transmitted to speakers or headphones.</span>
        <span class="lang-hi"><strong>ऑडियो आउटपुट हार्डवेयर:</strong>
          <br>&bull; <em>साउंड कार्ड:</em> इसमें <strong>DAC (डिजिटल-टू-एनालॉग कनवर्टर)</strong> चिप होती है जो डिजिटल बाइनरी ऑडियो डेटा को एनालॉग ध्वनि तरंगों में बदलकर स्पीकर अथवा हेडफ़ोन को भेजती है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Dual Input/Output & Hybrid Peripherals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Dual Input/Output Devices (Both Input &amp; Output)</span>
    <span class="lang-hi">3. उभयनिष्ठ इनपुट/आउटपुट उपकरण (इनपुट एवं आउटपुट दोनों)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Touchscreen (टचस्क्रीन):</strong>
          <br>&bull; Acts as an <strong>Input Device</strong> via finger touch/stylus sensors (resistive or capacitive grid) and simultaneously as an <strong>Output Device</strong> displaying the visual interface. Common in smartphones, ATMs, POS kiosks, and tablets.</span>
        <span class="lang-hi"><strong>टचस्क्रीन:</strong>
          <br>&bull; स्पर्श सेंसर द्वारा <strong>इनपुट</strong> लेता है तथा उसी डिस्प्ले स्क्रीन पर विज़ुअल परिणाम दिखाकर <strong>आउटपुट</strong> देता है (स्मार्टफोन, एटीएम, टैबलेट)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Modem (मॉडेम - Modulator / Demodulator):</strong>
          <br>&bull; Performs modulation (converting computer digital signals into analog signals for transmission over phone lines) &rarr; <em>Output function</em>.
          <br>&bull; Performs demodulation (converting received analog signals back into digital data for computer processing) &rarr; <em>Input function</em>.</span>
        <span class="lang-hi"><strong>मॉडेम (मॉड्यूलेटर/डीमॉड्यूलेटर):</strong>
          <br>&bull; डिजिटल सिग्नलों को एनालॉग सिग्नलों में बदलता है (मॉड्यूलेशन - आउटपुट) और आने वाले एनालॉग सिग्नलों को डिजिटल में बदलता है (डीमॉड्यूलेशन - इनपुट)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Multi-Function Printer / Peripheral (MFD / All-in-One):</strong>
          <br>&bull; Combines scanner (Input), printer (Output), photocopier (Both), and fax machine (Both) into a single desktop unit.</span>
        <span class="lang-hi"><strong>मल्टी-फंक्शन डिवाइस (MFD / All-in-One):</strong>
          <br>&bull; स्कैनर (इनपुट) एवं प्रिंटर (आउटपुट) दोनों को एक ही उपकरण में समाहित करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Network Interface Card (NIC / LAN Card) &amp; VR Headsets:</strong>
          <br>&bull; <em>NIC:</em> Transmits outgoing network data packets (Output) and receives incoming data packets (Input). Possesses a unique physical 48-bit <strong>MAC Address</strong>.
          <br>&bull; <em>Virtual Reality (VR) Headset:</em> Gyroscopes and accelerometers track head movement (Input), while dual OLED lenses render immersive 3D virtual worlds (Output).</span>
        <span class="lang-hi"><strong>नेटवर्क इंटरफेस कार्ड (NIC) एवं वीआर हेडसेट:</strong>
          <br>&bull; <em>NIC (नेटवर्क कार्ड):</em> नेटवर्क पर डेटा भेजता (आउटपुट) और प्राप्त (इनपुट) करता है; इसमें 48-बिट का स्थायी <strong>MAC पता</strong> होता है।
          <br>&bull; <em>VR हेडसेट:</em> सिर के घुमाव को सेंसर द्वारा ट्रैक करता है (इनपुट) और आंखों के सामने 3D दृश्य प्रदर्शित करता है (आउटपुट)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Ports, Connectors & Interfaces -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Hardware Ports, Busses &amp; Physical Interface Connectors</span>
    <span class="lang-hi">4. हार्डवेयर पोर्ट्स, बसेस एवं भौतिक इंटरफेस कनेक्टर्स</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Serial vs Parallel Ports:</strong>
          <br>&bull; <em>Serial Port (RS-232 / COM Port):</em> Transmits data sequentially <strong>one bit at a time</strong> over a single wire. Typically 9-pin (DB-9) or 25-pin (DB-25 male); used for external dial-up modems and legacy serial mice.
          <br>&bull; <em>Parallel Port (Centronics / LPT Port / IEEE 1284):</em> Transmits <strong>8 bits (1 byte) simultaneously</strong> over 8 parallel wires. 25-pin female connector (DB-25); historically used to connect legacy printers and scanners. Faster over short distances than serial, but prone to crosstalk skew over long cables.</span>
        <span class="lang-hi"><strong>सीरियल बनाम पैरेलल पोर्ट्स:</strong>
          <br>&bull; <em>सीरियल पोर्ट (RS-232 / COM):</em> एक समय में एक तार पर <strong>एक-एक बिट</strong> करके डेटा भेजता है (9-पिन या 25-पिन); पुराने मॉडेम जोड़ने हेतु प्रयुक्त।
          <br>&bull; <em>पैरेलल पोर्ट (LPT पोर्ट / IEEE 1284):</em> एक साथ 8 तारों पर <strong>8 बिट्स (1 बाइट) एक साथ</strong> भेजता है (25-पिन DB-25 फीमेल); पुराने प्रिंटर जोड़ने में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>PS/2 &amp; USB Ports:</strong>
          <br>&bull; <em>PS/2 Port:</em> 6-pin Mini-DIN connector introduced by IBM in 1987. Color coded: <strong>Purple for Keyboard</strong>, <strong>Green for Mouse</strong>. Not hot-swappable (requires computer reboot if unplugged).
          <br>&bull; <em>Universal Serial Bus (USB):</em> Standardized hot-swappable plug-and-play serial bus interface developed by an industry consortium (Intel, Microsoft, etc., led by Ajay Bhatt):
            <br>&nbsp;&nbsp;&bull; <strong>USB 1.1:</strong> 12 Mbps (Full Speed).
            <br>&nbsp;&nbsp;&bull; <strong>USB 2.0:</strong> 480 Mbps (High Speed - standard black connector).
            <br>&nbsp;&nbsp;&bull; <strong>USB 3.0 / 3.1 Gen 1:</strong> 5 Gbps (SuperSpeed - identified by distinct <strong>Blue connector</strong>).
            <br>&nbsp;&nbsp;&bull; <strong>USB Type-C:</strong> 24-pin reversible symmetrical connector supporting data up to 40 Gbps (USB4 / Thunderbolt 4) and Power Delivery up to 240W.</span>
        <span class="lang-hi"><strong>PS/2 एवं USB पोर्ट्स:</strong>
          <br>&bull; <em>PS/2 पोर्ट:</em> 6-पिन मिनी-डिन कनेक्टर; आईबीएम द्वारा विकसित। रंग कोड: <strong>बैंगनी (Purple) = कीबोर्ड</strong>, <strong>हरा (Green) = माउस</strong>।
          <br>&bull; <em>USB (यूनिवर्सल सीरियल बस):</em> प्लग-एंड-प्ले एवं हॉट-स्वैपेबल पोर्ट (भारतीय मूल के <strong>अजय भट्ट</strong> के नेतृत्व में विकसित):
            <br>&nbsp;&nbsp;&bull; <strong>USB 2.0:</strong> 480 Mbps गति (काला कनेक्टर)।
            <br>&nbsp;&nbsp;&bull; <strong>USB 3.0:</strong> 5 Gbps गति (पहचान: <strong>नीला कनेक्टर / Blue Port</strong>)।
            <br>&nbsp;&nbsp;&bull; <strong>USB Type-C:</strong> 24-पिन सममित (उल्टा-सीधा दोनों तरफ से लगने वाला) तीव्रतम पोर्ट।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Display Video Ports:</strong>
          <br>&bull; <em>VGA (Video Graphics Array):</em> 15-pin (3 rows of 5 pins) analog video connector (usually blue); carries analog video only (no audio).
          <br>&bull; <em>HDMI (High-Definition Multimedia Interface):</em> 19-pin uncompressed all-digital interface; carries <strong>both digital video AND multi-channel digital audio</strong> over a single cable.
          <br>&bull; <em>DisplayPort (DP):</em> Digital display interface with 20 pins; supports multiple daisy-chained monitors.</span>
        <span class="lang-hi"><strong>डिस्प्ले वीडियो पोर्ट्स:</strong>
          <br>&bull; <em>VGA (वीडियो ग्राफिक्स ऐरे):</em> 15-पिन (3 पंक्तियों में 5-5 पिन) एनालॉग वीडियो पोर्ट (नीले रंग का); केवल वीडियो सिग्नल ले जाता है (ऑडियो नहीं)।
          <br>&bull; <em>HDMI (हाई-डेफिनिशन मल्टीमीडिया इंटरफेस):</em> 19-पिन डिजिटल पोर्ट; एक ही केबल से <strong>डिजिटल वीडियो एवं डिजिटल ऑडियो दोनों</strong> का संचरण करता है।
          <br>&bull; <em>डिस्प्लेपोर्ट (DP):</em> 20-पिन उच्च बैंडविड्थ डिजिटल वीडियो पोर्ट।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Function Keys Reference Table -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Master Reference: Function Keys (F1 to F12) Functions</span>
    <span class="lang-hi">5. मास्टर संदर्भ: फंक्शन कुंजियों (F1 से F12) के कार्य</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Function Key</span>
            <span class="lang-hi">फंक्शन कुंजी</span>
          </th>
          <th>
            <span class="lang-en">Standard Windows / MS Office Action</span>
            <span class="lang-hi">मानक विंडोज / एमएस ऑफिस कार्य</span>
          </th>
          <th>
            <span class="lang-en">Key Exam Combination</span>
            <span class="lang-hi">महत्वपूर्ण परीक्षा शॉर्टकट</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>F1</strong></td>
          <td>
            <span class="lang-en">Universal <strong>Help</strong> screen in almost every software.</span>
            <span class="lang-hi">लगभग सभी प्रोग्रामों में सार्वभौमिक <strong>सहायता (Help)</strong> विंडो खोलना।</span>
          </td>
          <td>Ctrl + F1 (Ribbon Hide/Show)</td>
        </tr>
        <tr>
          <td><strong>F2</strong></td>
          <td>
            <span class="lang-en"><strong>Rename</strong> selected file/folder in Windows; Edit active cell in MS Excel.</span>
            <span class="lang-hi">फाइल/फोल्डर का <strong>नाम बदलना (Rename)</strong>; एक्सेल में सेल संपादन।</span>
          </td>
          <td>Ctrl + F2 (Print Preview in Word)</td>
        </tr>
        <tr>
          <td><strong>F3</strong></td>
          <td>
            <span class="lang-en">Open <strong>Search</strong> file/folder feature in File Explorer and browsers.</span>
            <span class="lang-hi">विंडोज और ब्राउज़र में <strong>खोज (Search)</strong> सुविधा खोलना।</span>
          </td>
          <td>Shift + F3 (Change Case in Word)</td>
        </tr>
        <tr>
          <td><strong>F4</strong></td>
          <td>
            <span class="lang-en">Repeat last action in MS Office; Focus Address Bar in File Explorer.</span>
            <span class="lang-hi">अंतिम कार्य दोहराना; फाइल एक्सप्लोरर में एड्रेस बार सक्रिय करना।</span>
          </td>
          <td>Alt + F4 (Close active window / Shut Down)</td>
        </tr>
        <tr>
          <td><strong>F5</strong></td>
          <td>
            <span class="lang-en"><strong>Refresh</strong> active webpage or desktop; Start Slide Show from beginning in PowerPoint.</span>
            <span class="lang-hi">सक्रिय विंडो/पेज <strong>रिफ्रेश (Refresh)</strong> करना; पावरपॉइंट में स्लाइड शो शुरू करना।</span>
          </td>
          <td>Shift + F5 (Slide show from current slide)</td>
        </tr>
        <tr>
          <td><strong>F6</strong></td>
          <td>
            <span class="lang-en">Cycle through screen elements; Move cursor to URL address bar in web browsers.</span>
            <span class="lang-hi">ब्राउज़र में कर्सर को सीधे URL एड्रेस बार पर ले जाना।</span>
          </td>
          <td>Ctrl + Shift + F6 (Switch docs)</td>
        </tr>
        <tr>
          <td><strong>F7</strong></td>
          <td>
            <span class="lang-en">Launch <strong>Spelling &amp; Grammar Check</strong> in MS Word/Excel.</span>
            <span class="lang-hi">एमएस वर्ड में <strong>स्पेलिंग एवं ग्रामर (वर्तनी व व्याकरण)</strong> जांच शुरू करना।</span>
          </td>
          <td>Shift + F7 (Thesaurus / पर्यायवाची शब्द)</td>
        </tr>
        <tr>
          <td><strong>F8</strong></td>
          <td>
            <span class="lang-en">Enter Windows <strong>Safe Mode</strong> during booting; Extend Selection in MS Word.</span>
            <span class="lang-hi">बूटिंग के समय विंडोज <strong>सेफ मोड (Safe Mode)</strong> में जाना।</span>
          </td>
          <td>Triple F8 (Select entire sentence in Word)</td>
        </tr>
        <tr>
          <td><strong>F9</strong></td>
          <td>
            <span class="lang-en">Refresh document in MS Word; Recalculate all workbooks in MS Excel.</span>
            <span class="lang-hi">वर्ड डॉक्यूमेंट रिफ्रेश करना; एक्सेल में सभी फॉर्मूलों की पुनः गणना।</span>
          </td>
          <td>Ctrl + F9 (Insert blank field)</td>
        </tr>
        <tr>
          <td><strong>F10</strong></td>
          <td>
            <span class="lang-en">Activate menu bar / ribbon key tips in applications.</span>
            <span class="lang-hi">प्रोग्राम की मेन्यू बार या रिबन शॉर्टकट को सक्रिय करना।</span>
          </td>
          <td>Shift + F10 (Right Click context menu)</td>
        </tr>
        <tr>
          <td><strong>F11</strong></td>
          <td>
            <span class="lang-en">Toggle <strong>Full Screen mode</strong> in web browsers and File Explorer; Create Chart in Excel.</span>
            <span class="lang-hi">वेब ब्राउज़र में <strong>फुल स्क्रीन मोड (Full Screen)</strong> चालू/बंद करना।</span>
          </td>
          <td>Alt + F11 (Open VBA Editor)</td>
        </tr>
        <tr>
          <td><strong>F12</strong></td>
          <td>
            <span class="lang-en">Open <strong>Save As</strong> dialog box in MS Word and Excel.</span>
            <span class="lang-hi">एमएस वर्ड एवं एक्सेल में <strong>सेव ऐज़ (Save As)</strong> डायलॉग बॉक्स खोलना।</span>
          </td>
          <td>Ctrl + F12 (Open document)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 7: Rapid Revision Matrix & UPSSSC Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">6. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
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
            <span class="lang-en">Inventor of Computer Mouse</span>
            <span class="lang-hi">कंप्यूटर माउस के आविष्कारक</span>
          </td>
          <td>
            <span class="lang-en"><strong>Douglas Engelbart</strong> (1964 at Stanford Research Institute).</span>
            <span class="lang-hi"><strong>डगलस एंजेलबर्ट</strong> (1964, स्टैनफोर्ड)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Which keys are called Toggle Keys?</span>
            <span class="lang-hi">किन कुंजियों को टॉगल कुंजियां कहा जाता है?</span>
          </td>
          <td>
            <span class="lang-en"><strong>Caps Lock, Num Lock, and Scroll Lock</strong> (switch states ON/OFF).</span>
            <span class="lang-hi"><strong>Caps Lock, Num Lock, एवं Scroll Lock</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Which keys are called Modifier Keys?</span>
            <span class="lang-hi">किन कुंजियों को मॉडिफायर कुंजियां कहा जाता है?</span>
          </td>
          <td>
            <span class="lang-en"><strong>Shift, Ctrl, and Alt</strong> (operate in combination with other keys).</span>
            <span class="lang-hi"><strong>Shift, Ctrl, एवं Alt</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Number of digits in bank cheque MICR code</span>
            <span class="lang-hi">बैंक चेक के MICR कोड में कुल कितने अंक होते हैं?</span>
          </td>
          <td>
            <span class="lang-en"><strong>9 digits</strong> (Format: 3 City + 3 Bank + 3 Branch).</span>
            <span class="lang-hi"><strong>9 अंक</strong> (संरचना: 3 शहर + 3 बैंक + 3 शाखा)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Device used to check OMR answer sheets</span>
            <span class="lang-hi">प्रतियोगी परीक्षाओं की उत्तर-पुस्तिका जांचने वाली युक्ति</span>
          </td>
          <td>
            <span class="lang-en"><strong>Optical Mark Reader (OMR)</strong>.</span>
            <span class="lang-hi"><strong>ऑप्टिकल मार्क रीडर (OMR)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Port that carries both digital video and audio</span>
            <span class="lang-hi">वह पोर्ट जो डिजिटल वीडियो और ऑडियो दोनों का संचरण करता है</span>
          </td>
          <td>
            <span class="lang-en"><strong>HDMI (High-Definition Multimedia Interface)</strong>. VGA carries video only.</span>
            <span class="lang-hi"><strong>HDMI</strong> (VGA केवल एनालॉग वीडियो भेजता है)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Color of USB 3.0 connector</span>
            <span class="lang-hi">USB 3.0 पोर्ट कनेक्टर का आंतरिक रंग</span>
          </td>
          <td>
            <span class="lang-en"><strong>Blue (नीला)</strong>. (USB 2.0 is Black, USB 3.1 Gen 2 is Teal/Red).</span>
            <span class="lang-hi"><strong>नीला (Blue)</strong>। (USB 2.0 काला होता है)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Shortcut key to open 'Save As' dialog</span>
            <span class="lang-hi">'सेव ऐज़' (Save As) डायलॉग बॉक्स की शॉर्टकट कुंजी</span>
          </td>
          <td>
            <span class="lang-en"><strong>F12</strong> (in MS Word &amp; Excel).</span>
            <span class="lang-hi"><strong>F12</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Shortcut key for Spelling &amp; Grammar check</span>
            <span class="lang-hi">स्पेलिंग एवं ग्रामर जांच की शॉर्टकट कुंजी</span>
          </td>
          <td>
            <span class="lang-en"><strong>F7</strong> (Thesaurus is <strong>Shift + F7</strong>).</span>
            <span class="lang-hi"><strong>F7</strong> (समानार्थी शब्द हेतु <strong>Shift + F7</strong>)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Difference between Backspace and Delete keys</span>
            <span class="lang-hi">Backspace और Delete कुंजियों में अंतर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Backspace</strong> erases to the <strong>Left</strong>; <strong>Delete</strong> erases to the <strong>Right</strong> of cursor.</span>
            <span class="lang-hi"><strong>Backspace</strong> कर्सर के <strong>बाईं ओर</strong>; <strong>Delete</strong> <strong>दायीं ओर</strong> के अक्षर को मिटाता है।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-computer", "input-and-output", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_input_output_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
