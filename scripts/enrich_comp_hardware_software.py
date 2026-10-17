import os
import re

def build_hardware_software_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Computer Hardware, Software &amp; Memory Hierarchy</span>
    <span class="lang-hi">माइंड मैप: कंप्यूटर हार्डवेयर, सॉफ्टवेयर एवं मेमोरी पदानुक्रम</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Computer System Architecture] --> B[Hardware Physical Components]
    A --> C[Software Logical Instructions]
    A --> D[Memory Hierarchy & Storage]

    B --> B1[CPU: ALU, Control Unit, Registers, Internal Bus]
    B --> B2[Motherboard: Chipset Northbridge/Southbridge, CMOS, BIOS/UEFI]
    B --> B3[System Bus: Data Bus Bi, Address Bus Uni, Control Bus]
    B --> B4[Ports & Expansion: USB, HDMI, PCIe, SATA]

    C --> C1[System Software: OS, Device Drivers]
    C --> C2[Language Translators: Assembler, Compiler, Interpreter, Linker, Loader]
    C --> C3[Application Software: General Word/Excel vs Specific ERP/Billing]
    C --> C4[Utility Software: Antivirus, Disk Defrag, File Compression]
    C --> C5[License Models: Open Source, Proprietary, Freeware, Shareware, Firmware]

    D --> D1[Level 0 Registers: In-CPU, Fastest, Smallest]
    D --> D2[Level 1 Cache L1, L2, L3: SRAM, High Speed Buffer]
    D --> D3[Level 2 Primary Memory: RAM SRAM/DRAM, ROM PROM/EPROM/EEPROM]
    D --> D4[Level 3 Secondary Storage: Magnetic HDD, Optical CD/DVD, Flash SSD]
    D --> D5[Virtual Memory: Paging, Swap Space on Disk]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[कंप्यूटर सिस्टम वास्तुकला] --> B[हार्डवेयर भौतिक घटक]
    A --> C[सॉफ्टवेयर तार्किक निर्देश]
    A --> D[मेमोरी पदानुक्रम एवं स्टोरेज]

    B --> B1[सीपीयू: ALU, कंट्रोल यूनिट, रजिस्टर्स, आंतरिक बस]
    B --> B2[मदरबोर्ड: चिपसेट नॉर्थब्रिज/साउथब्रिज, CMOS, BIOS/UEFI]
    B --> B3[सिस्टम बस: डेटा बस द्विदिशी, एड्रेस बस एकदिशी, कंट्रोल बस]
    B --> B4[पोर्ट्स व स्लॉट्स: USB, HDMI, PCIe, SATA]

    C --> C1[सिस्टम सॉफ्टवेयर: ऑपरेटिंग सिस्टम, डिवाइस ड्राइवर्स]
    C --> C2[भाषा अनुवादक: असेंबलर, कंपाइलर, इंटरप्रेटर, लिंकर, लोडर]
    C --> C3[एप्लीकेशन सॉफ्टवेयर: सामान्य वर्ड/एक्सेल बनाम विशिष्ट ERP/बिलिंग]
    C --> C4[यूटिलिटी सॉफ्टवेयर: एंटीवायरस, डिस्क डिफ्रैग्मेंटर, कम्प्रेशन]
    C --> C5[लाइसेंस प्रकार: ओपन सोर्स, प्रोप्राइटरी, फ्रीवेयर, शेयरवेयर, फर्मवेयर]

    D --> D1[लेवल 0 रजिस्टर्स: सीपीयू के अंदर, तीव्रतम, न्यूनतम क्षमता]
    D --> D2[लेवल 1 कैश मेमोरी L1, L2, L3: SRAM, तीव्र बफर]
    D --> D3[लेवल 2 प्राथमिक मेमोरी: रैम SRAM/DRAM, रोम PROM/EPROM/EEPROM]
    D --> D4[लेवल 3 द्वितीयक स्टोरेज: मैग्नेटिक HDD, ऑप्टिकल CD/DVD, सॉलिड स्टेट SSD]
    D --> D5[वर्चुअल मेमोरी: पेजिंग, डिस्क पर स्वैप स्पेस]
    </div>
  </div>
</div>

<!-- Card 2: Hardware Core Components -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Computer Hardware Architecture: CPU, Motherboard &amp; System Bus</span>
    <span class="lang-hi">1. कंप्यूटर हार्डवेयर वास्तुकला: सीपीयू, मदरबोर्ड एवं सिस्टम बस</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Central Processing Unit (CPU / Microprocessor):</strong>
          <br>&bull; Termed the <strong>"Brain of the Computer"</strong>. Responsible for fetching, decoding, executing, and storing instructions.
          <br>&bull; <em>Arithmetic Logic Unit (ALU):</em> Performs fundamental arithmetic (+, -, *, /) and logical decisions (AND, OR, NOT, comparisons &gt;, &lt;, =).
          <br>&bull; <em>Control Unit (CU):</em> The <strong>"Nerve Center / Traffic Cop"</strong> of the CPU; coordinates operations of all hardware units by issuing electrical timing signals; contains the <strong>Instruction Decoder</strong>.
          <br>&bull; <em>Internal Registers:</em> High-speed micro-storage locations inside the CPU:
            <br>&nbsp;&nbsp;&bull; <strong>Program Counter (PC):</strong> Holds the memory address of the <em>next</em> instruction to be fetched and executed.
            <br>&nbsp;&nbsp;&bull; <strong>Instruction Register (IR):</strong> Holds the current instruction being decoded and executed.
            <br>&nbsp;&nbsp;&bull; <strong>Memory Address Register (MAR):</strong> Holds the memory address currently being read from or written to.
            <br>&nbsp;&nbsp;&bull; <strong>Memory Buffer / Data Register (MBR / MDR):</strong> Holds the actual data contents read from or to be written to memory.
            <br>&nbsp;&nbsp;&bull; <strong>Accumulator (AC):</strong> Directly stores intermediate arithmetic and logical results.
          <br>&bull; <em>Machine Cycle (मशीन चक्र):</em> Four fundamental steps: <strong>Fetch &rarr; Decode &rarr; Execute &rarr; Store</strong>. Instruction Fetch + Decode = <em>I-Time</em>; Execute + Store = <em>E-Time</em>.
          <br>&bull; <em>Clock Speed (क्लॉक स्पीड):</em> Internal crystal oscillator generating pulses per second; measured in <strong>Megahertz (MHz)</strong> and <strong>Gigahertz (GHz)</strong> (1 GHz = 10^9 clock cycles/sec).</span>
        <span class="lang-hi"><strong>सेंट्रल प्रोसेसिंग यूनिट (CPU / माइक्रोप्रोसेसर):</strong>
          <br>&bull; इसे <strong>"कंप्यूटर का मस्तिष्क"</strong> कहा जाता है। यह निर्देशों को प्राप्त (Fetch), व्याख्या (Decode), निष्पादित (Execute) और सुरक्षित (Store) करता है।
          <br>&bull; <em>अंकगणितीय एवं तार्किक इकाई (ALU):</em> सभी गणितीय संक्रियाएं (+, -, *, /) एवं तार्किक निर्णय (AND, OR, NOT, तुलना &gt;, &lt;, =) करता है।
          <br>&bull; <em>कंट्रोल यूनिट (CU):</em> CPU का <strong>"तंत्रिका तंत्र / ट्रैफिक पुलिस"</strong>; हार्डवेयर घटकों के कार्यों का समन्वय करता है; इसमें इंस्ट्रक्शन डिकोडर होता है।
          <br>&bull; <em>आंतरिक रजिस्टर्स (Internal Registers):</em> सीपीयू के भीतर स्थित तीव्रतम मेमोरी सेल:
            <br>&nbsp;&nbsp;&bull; <strong>प्रोग्राम काउंटर (PC):</strong> निष्पादित होने वाले <em>अगले</em> निर्देश का मेमोरी पता सुरक्षित रखता है।
            <br>&nbsp;&nbsp;&bull; <strong>इंस्ट्रक्शन रजिस्टर (IR):</strong> वर्तमान में निष्पादित हो रहे निर्देश को रखता है।
            <br>&nbsp;&nbsp;&bull; <strong>मेमोरी एड्रेस रजिस्टर (MAR):</strong> उस मेमोरी लोकेशन का पता रखता है जिसे पढ़ा या लिखा जाना है।
            <br>&nbsp;&nbsp;&bull; <strong>मेमोरी डेटा रजिस्टर (MDR / MBR):</strong> मेमोरी से पढ़े गए अथवा लिखे जाने वाले वास्तविक डेटा को रखता है।
            <br>&nbsp;&nbsp;&bull; <strong>एक्युमुलेटर (AC):</strong> ALU के मध्यवर्ती गणना परिणामों को संग्रहीत करता है।
          <br>&bull; <em>मशीन साइकिल (Machine Cycle):</em> चार चरण: <strong>फेच (Fetch) &rarr; डिकोड (Decode) &rarr; एग्जीक्यूट (Execute) &rarr; स्टोर (Store)</strong>।
          <br>&bull; <em>क्लॉक स्पीड:</em> सीपीयू की गति का मापक; <strong>गीगाहर्ट्ज (GHz)</strong> और मेगाहर्ट्ज (MHz) में मापा जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Motherboard &amp; Chipset Architecture:</strong>
          <br>&bull; <em>Motherboard (Mainboard / System Board):</em> Main printed circuit board (PCB) connecting all components.
          <br>&bull; <em>Chipset:</em> Micro-controller hub managing communication:
            <br>&nbsp;&nbsp;&bull; <strong>Northbridge (Host Bridge):</strong> Connects high-speed components: CPU, Main RAM, and high-speed PCIe graphics cards. (In modern CPUs, Northbridge functions are integrated directly into the processor die).
            <br>&nbsp;&nbsp;&bull; <strong>Southbridge (I/O Controller Hub):</strong> Connects slower peripheral buses: SATA drives, USB ports, BIOS, Audio, PCI slots, Ethernet.
          <br>&bull; <em>BIOS &amp; UEFI:</em> <strong>BIOS (Basic Input/Output System)</strong> is firmware stored in ROM/EEPROM on motherboard; modern systems use <strong>UEFI (Unified Extensible Firmware Interface)</strong> supporting GUID Partition Table (GPT) and drives &gt;2 TB.
          <br>&bull; <em>POST (Power-On Self-Test):</em> Diagnostic routine executed by BIOS upon startup to test hardware components (RAM, keyboard, drives). Single short beep indicates successful test.
          <br>&bull; <em>CMOS (Complementary Metal-Oxide Semiconductor) &amp; Battery:</em> Volatile memory chip powered by a small coin-cell lithium battery (CR2032); retains system time, date, and hardware configuration when the computer is turned off.
          <br>&bull; <em>Booting Process:</em>
            <br>&nbsp;&nbsp;&bull; <strong>Cold Booting (Hard Boot):</strong> Turning on the computer from a completely powered-off state using the physical power switch.
            <br>&nbsp;&nbsp;&bull; <strong>Warm Booting (Soft Boot):</strong> Restarting an already running computer without turning off main power (via OS Restart or shortcut <strong>Ctrl + Alt + Delete</strong>).</span>
        <span class="lang-hi"><strong>मदरबोर्ड एवं चिपसेट वास्तुकला:</strong>
          <br>&bull; <em>मदरबोर्ड (सिस्टम बोर्ड):</em> कंप्यूटर का मुख्य सर्किट बोर्ड, जो सभी आंतरिक व बाह्य घटकों को आपस में जोड़ता है।
          <br>&bull; <em>चिपसेट:</em> डेटा प्रवाह का नियंत्रण केंद्र:
            <br>&nbsp;&nbsp;&bull; <strong>नॉर्थब्रिज (Northbridge):</strong> उच्च-गति घटकों (CPU, RAM, PCIe ग्राफिक्स कार्ड) के बीच तीव्र संचार संभालता है।
            <br>&nbsp;&nbsp;&bull; <strong>साउथब्रिज (Southbridge):</strong> अपेक्षाकृत धीमी परिधीय युक्तियों (SATA हार्ड ड्राइव, USB पोर्ट, ऑडियो, BIOS चिप) को जोड़ता है।
          <br>&bull; <em>BIOS एवं UEFI:</em> <strong>BIOS (बेसिक इनपुट/आउटपुट सिस्टम)</strong> मदरबोर्ड की ROM/EEPROM चिप में स्थायी रूप से लिखा फर्मवेयर है; आधुनिक सिस्टम <strong>UEFI</strong> का प्रयोग करते हैं जो 2 TB से बड़े डिस्क को बूट कर सकता है।
          <br>&bull; <em>POST (पावर-ऑन सेल्फ-टेस्ट):</em> कंप्यूटर ऑन होते ही BIOS द्वारा हार्डवेयर (रैम, कीबोर्ड आदि) की कार्यक्षमता जांचने वाला डायग्नोस्टिक परीक्षण।
          <br>&bull; <em>CMOS एवं बैटरी:</em> मदरबोर्ड पर CR2032 लिथियम सेल द्वारा संचालित छोटी मेमोरी, जो कंप्यूटर बंद रहने पर भी वास्तविक समय, दिनांक व BIOS सेटिंग्स सुरक्षित रखती है।
          <br>&bull; <em>बूटिंग (Booting):</em>
            <br>&nbsp;&nbsp;&bull; <strong>कोल्ड बूट (Cold Boot):</strong> पावर स्विच दबाकर पूर्णतः बंद कंप्यूटर को चालू करना।
            <br>&nbsp;&nbsp;&bull; <strong>वार्म बूट (Warm Boot):</strong> पहले से चालू कंप्यूटर को बिना मुख्य पावर काटे रीस्टार्ट करना (शॉर्टकट: <strong>Ctrl + Alt + Delete</strong>)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>System Bus (सिस्टम बस):</strong>
          <br>&bull; <em>Data Bus (द्विदिशी / Bidirectional):</em> Transfers actual binary data between CPU, memory, and devices. Bus width (e.g., 32-bit, 64-bit) determines data throughput per cycle.
          <br>&bull; <em>Address Bus (एकदिशी / Unidirectional):</em> Carries memory addresses generated solely by the CPU to identify target locations. A 32-bit address bus can access 2^32 bytes = <strong>4 Gigabytes (GB)</strong> of RAM. A 64-bit bus can access 16 Exabytes.
          <br>&bull; <em>Control Bus (नियंत्रण बस):</em> Carries read/write, interrupt, acknowledge, and synchronization clock signals.</span>
        <span class="lang-hi"><strong>सिस्टम बस (System Bus):</strong>
          <br>&bull; <em>डेटा बस (द्विदिशी):</em> सीपीयू, मेमोरी और इनपुट/आउटपुट के बीच वास्तविक डेटा का आदान-प्रदान करती है (चौड़ाई: 32-बिट या 64-बिट)।
          <br>&bull; <em>एड्रेस बस (एकदिशी):</em> केवल सीपीयू द्वारा उत्पन्न मेमोरी पते को मेमोरी या पोर्ट्स तक ले जाती है (32-बिट एड्रेस बस अधिकतम <strong>4 GB</strong> रैम को एड्रेस कर सकती है)।
          <br>&bull; <em>कंट्रोल बस:</em> रीड, राइट, इंटरप्ट एवं क्लॉक सिग्नल प्रसारित करती है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Memory Hierarchy Deep Dive -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Memory Hierarchy: Registers, Cache, RAM, ROM &amp; Secondary Storage</span>
    <span class="lang-hi">2. मेमोरी पदानुक्रम: रजिस्टर्स, कैश, रैम, रोम एवं द्वितीयक स्टोरेज</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Memory Hierarchy Principles:</strong>
          <br>&bull; As we move from top (Registers) to bottom (Secondary Storage): <strong>Speed decreases, Capacity increases, and Cost per bit decreases</strong>.
          <br>&bull; Hierarchy Order: <strong>CPU Registers &gt; Cache Memory (L1 &gt; L2 &gt; L3) &gt; Primary RAM &gt; SSD &gt; HDD &gt; Optical / Tape Storage</strong>.</span>
        <span class="lang-hi"><strong>मेमोरी पदानुक्रम के नियम:</strong>
          <br>&bull; शीर्ष (रजिस्टर) से तल (सेकेंडरी स्टोरेज) की ओर जाने पर: <strong>गति घटती है, भंडारण क्षमता बढ़ती है, तथा प्रति बिट लागत घटती है</strong>।
          <br>&bull; गति का घटता क्रम: <strong>रजिस्टर्स &gt; कैश मेमोरी (L1 &gt; L2 &gt; L3) &gt; प्राथमिक रैम (RAM) &gt; सॉलिड स्टेट ड्राइव (SSD) &gt; हार्ड डिस्क (HDD) &gt; ऑप्टिकल डिस्क/टेप</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Primary / Main Memory (प्राथमिक मेमोरी):</strong>
          <br>&bull; <em>Random Access Memory (RAM):</em> <strong>Volatile (अस्थायी)</strong>; loses all data immediately when power is turned off; read/write accessible.
            <br>&nbsp;&nbsp;&bull; <strong>SRAM (Static RAM):</strong> Uses 4 to 6 flip-flop transistors per cell; faster, requires no periodic refreshing; highly expensive; used in <strong>Cache Memory</strong>.
            <br>&nbsp;&nbsp;&bull; <strong>DRAM (Dynamic RAM):</strong> Uses 1 transistor and 1 capacitor per cell; capacitor leaks charge and requires continuous electrical <strong>refreshing</strong> thousands of times per second; cheaper, high density; used in <strong>Main System RAM</strong> (DDR4, DDR5).
          <br>&bull; <em>Read Only Memory (ROM):</em> <strong>Non-Volatile (स्थायी)</strong>; retains firmware/BIOS instructions even when power is turned off; primarily read-only.
            <br>&nbsp;&nbsp;&bull; <strong>PROM (Programmable ROM):</strong> Manufactured blank; can be programmed by the user only once using a PROM burner (fuse burning).
            <br>&nbsp;&nbsp;&bull; <strong>EPROM (Erasable Programmable ROM):</strong> Can be erased by exposing the quartz window to intense <strong>Ultraviolet (UV) light</strong> for 20-30 minutes, then reprogrammed.
            <br>&nbsp;&nbsp;&bull; <strong>EEPROM (Electrically Erasable Programmable ROM):</strong> Can be erased and rewritten electrically byte-by-byte without removing it from the motherboard; foundation of modern <strong>Flash Memory</strong>.</span>
        <span class="lang-hi"><strong>प्राथमिक / मुख्य मेमोरी (Primary Memory):</strong>
          <br>&bull; <em>रैम (RAM - रैंडम एक्सेस मेमोरी):</em> <strong>परिवर्तनशील / अस्थायी (Volatile)</strong>; बिजली जाते ही सारा डेटा नष्ट हो जाता है; पढ़ने व लिखने दोनों योग्य।
            <br>&nbsp;&nbsp;&bull; <strong>SRAM (स्टैटिक रैम):</strong> फ्लिप-फ्लॉप ट्रांजिस्टरों से निर्मित; अत्यधिक तीव्र, इसे बार-बार रिफ्रेश करने की आवश्यकता नहीं होती; <strong>कैश मेमोरी</strong> में प्रयुक्त।
            <br>&nbsp;&nbsp;&bull; <strong>DRAM (डायनामिक रैम):</strong> कैपेसिटर व ट्रांजिस्टर पर आधारित; कैपेसिटर डिस्चार्ज होता है अतः इसे प्रति सेकंड हजारों बार <strong>रिफ्रेश (Refresh)</strong> करना पड़ता है; मुख्य कंप्यूटर रैम में प्रयुक्त।
          <br>&bull; <em>रोम (ROM - रीड ओनली मेमोरी):</em> <strong>अपरिवर्तनशील / स्थायी (Non-Volatile)</strong>; बिजली कटने पर भी डेटा सुरक्षित रहता है; BIOS प्रोग्राम रखने हेतु प्रयुक्त।
            <br>&nbsp;&nbsp;&bull; <strong>PROM:</strong> केवल एक बार प्रोग्राम किया जा सकता है।
            <br>&nbsp;&nbsp;&bull; <strong>EPROM:</strong> पराबैंगनी किरणों (UV Light) के संपर्क में रखकर डेटा मिटाया और पुनः लिखा जा सकता है।
            <br>&nbsp;&nbsp;&bull; <strong>EEPROM:</strong> विद्युत पल्स द्वारा बाइट-दर-बाइट मिटाया और पुनः लिखा जा सकता है; पेन ड्राइव एवं फ्लैश मेमोरी का आधार।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Cache Memory &amp; Virtual Memory:</strong>
          <br>&bull; <em>Cache Memory:</em> Extremely high-speed buffer memory placed between CPU and Main RAM to bridge the speed mismatch; holds frequently and recently used instructions.
            <br>&nbsp;&nbsp;&bull; <strong>L1 Cache:</strong> Smallest (32-128 KB), fastest, built directly into the CPU core.
            <br>&nbsp;&nbsp;&bull; <strong>L2 Cache:</strong> Medium size (256 KB - 1 MB), dedicated to each core.
            <br>&nbsp;&nbsp;&bull; <strong>L3 Cache:</strong> Largest (8 - 64+ MB), shared among all CPU cores.
          <br>&bull; <em>Virtual Memory:</em> An OS memory management illusion where a section of Secondary Storage (HDD/SSD) is utilized as an extension of physical RAM. Managed via <strong>Paging</strong> (fixed-size blocks). When requested data is missing in physical RAM, a <strong>Page Fault</strong> occurs, causing the OS to swap pages between RAM and disk.</span>
        <span class="lang-hi"><strong>कैश मेमोरी एवं वर्चुअल मेमोरी:</strong>
          <br>&bull; <em>कैश मेमोरी:</em> सीपीयू और मुख्य रैम के बीच गति के अंतर को पाटने हेतु प्रयुक्त तीव्रतम बफर मेमोरी; बार-बार प्रयुक्त निर्देशों को रखती है। L1 (कोर में), L2 (प्रति कोर), और L3 (साझा) कैश।
          <br>&bull; <em>वर्चुअल मेमोरी (Virtual Memory):</em> ऑपरेटिंग सिस्टम की एक तकनीक जिसके द्वारा हार्ड डिस्क या एसएसडी के एक भाग को अस्थायी रैम की तरह प्रयुक्त किया जाता है, जिससे भौतिक रैम से बड़े प्रोग्राम भी चल सकते हैं। इसे <strong>पेजिंग (Paging)</strong> द्वारा प्रबंधित किया जाता है; जब मांगा गया पेज रैम में नहीं होता, तो उसे <strong>पेज फॉल्ट (Page Fault)</strong> कहते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Secondary Storage Technologies:</strong>
          <br>&bull; <em>Magnetic Storage:</em> Hard Disk Drive (HDD - tracks, sectors, cylinders, read/write head, speed measured in RPM: 5400/7200 RPM), Magnetic Tape (sequential access).
          <br>&bull; <em>Optical Storage:</em> Read/written using laser beams:
            <br>&nbsp;&nbsp;&bull; <strong>Compact Disc (CD):</strong> 700 MB capacity (Red laser 780 nm).
            <br>&nbsp;&nbsp;&bull; <strong>Digital Versatile Disc (DVD):</strong> 4.7 GB (single-layer) to 8.5 GB (dual-layer) (Red laser 650 nm).
            <br>&nbsp;&nbsp;&bull; <strong>Blu-ray Disc (BD):</strong> 25 GB (single-layer) to 50 GB (dual-layer) (Blue-violet laser 405 nm).
          <br>&bull; <em>Solid State Storage:</em> Solid State Drive (SSD), USB Flash Drive, MicroSD cards (use NAND Flash EEPROM memory; no moving mechanical parts, shock resistant, 5-10x faster than HDD).</span>
        <span class="lang-hi"><strong>द्वितीयक स्टोरेज प्रौद्योगिकियां:</strong>
          <br>&bull; <em>मैग्नेटिक स्टोरेज:</em> हार्ड डिस्क ड्राइव (HDD - ट्रैक्स, सेक्टर्स और सिलिंडर्स में विभाजित; घूर्णन गति 5400/7200 RPM में मापी जाती है), मैग्नेटिक टेप (सीक्वेंशियल एक्सेस)।
          <br>&bull; <em>ऑप्टिकल स्टोरेज (लेजर आधारित):</em>
            <br>&nbsp;&nbsp;&bull; <strong>सीडी (CD):</strong> 700 MB क्षमता (लाल लेजर 780 nm)।
            <br>&nbsp;&nbsp;&bull; <strong>डीवीडी (DVD):</strong> 4.7 GB (सिंगल लेयर) से 8.5 GB (ड्यूल लेयर) (लाल लेजर 650 nm)।
            <br>&nbsp;&nbsp;&bull; <strong>ब्लू-रे डिस्क (Blu-ray):</strong> 25 GB से 50 GB क्षमता (नीली-बैंगनी लेजर 405 nm)।
          <br>&bull; <em>सॉलिड स्टेट स्टोरेज (SSD / पेन ड्राइव):</em> NAND फ्लैश मेमोरी आधारित; कोई चलायमान यांत्रिक पुर्जा नहीं होता, अत्यधिक तीव्र और टिकाऊ।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Software Classification & Ecosystem -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Software Classification: System, Application, Utility &amp; Licensing</span>
    <span class="lang-hi">3. सॉफ्टवेयर वर्गीकरण: सिस्टम, एप्लीकेशन, यूटिलिटी एवं लाइसेंसिंग</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. System Software (सिस्टम सॉफ्टवेयर):</strong>
          <br>&bull; Low-level software that manages computer hardware, resources, and provides a platform for application software.
          <br>&bull; <em>Operating System (OS):</em> Resource manager (CPU, memory, files, I/O); e.g., Windows, Linux, macOS, Android.
          <br>&bull; <em>Device Drivers:</em> Specialized software modules that enable the OS to communicate with physical peripheral hardware (printer drivers, graphics drivers).
          <br>&bull; <em>Language Translators:</em> Compilers, Interpreters, Assemblers.
          <br>&bull; <em>Linker &amp; Loader:</em> System utilities essential for program execution.</span>
        <span class="lang-hi"><strong>1. सिस्टम सॉफ्टवेयर:</strong>
          <br>&bull; कंप्यूटर के हार्डवेयर और आंतरिक संसाधनों का प्रबंधन करने वाला तथा एप्लीकेशन सॉफ्टवेयर को मंच प्रदान करने वाला सॉफ्टवेयर।
          <br>&bull; <em>ऑपरेटिंग सिस्टम (OS):</em> विंडोज, लिनक्स, यूनिक्स, मैकओएस, एंड्रॉइड।
          <br>&bull; <em>डिवाइस ड्राइवर्स:</em> प्रिंटर, साउंड कार्ड, ग्राफिक्स कार्ड जैसे हार्डवेयर को ऑपरेटिंग सिस्टम से जोड़ने वाले सॉफ्टवेयर।
          <br>&bull; <em>भाषा अनुवादक:</em> कंपाइलर, इंटरप्रेटर, असेंबलर।
          <br>&bull; <em>लिंकर एवं लोडर:</em> प्रोग्राम निष्पादन हेतु आवश्यक सिस्टम प्रोग्राम।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Application Software (एप्लीकेशन सॉफ्टवेयर):</strong>
          <br>&bull; End-user software designed to perform specific user-oriented tasks.
          <br>&bull; <em>General Purpose:</em> MS Office / LibreOffice (Word, Excel, PowerPoint), Web Browsers (Chrome, Firefox), Media Players (VLC), Graphics (Photoshop).
          <br>&bull; <em>Specialized / Customized:</em> Railway Reservation System (CRIS), Hospital Management ERP, Banking Software (Finacle), Tally ERP for accounting.</span>
        <span class="lang-hi"><strong>2. एप्लीकेशन सॉफ्टवेयर:</strong>
          <br>&bull; उपयोगकर्ताओं द्वारा अपनी विशिष्ट आवश्यकताओं को पूरा करने हेतु उपयोग किए जाने वाले प्रोग्राम।
          <br>&bull; <em>सामान्य उद्देशीय:</em> एमएस ऑफिस (वर्ड, एक्सेल, पावरपॉइंट), वेब ब्राउज़र (क्रोम, एज), वीएलसी मीडिया प्लेयर।
          <br>&bull; <em>विशिष्ट / कस्टमाइज्ड:</em> रेलवे आरक्षण प्रणाली, बैंक कोर सॉफ्टवेयर (Finacle), टैली (Tally ERP), स्कूल प्रबंधन सॉफ्टवेयर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>3. Utility Software (यूटिलिटी सॉफ्टवेयर / सर्विस प्रोग्राम):</strong>
          <br>&bull; Routine housekeeping software that optimizes, maintains, and protects computer performance.
          <br>&bull; <em>Antivirus &amp; Anti-malware:</em> Windows Defender, Quick Heal, Kaspersky, Norton.
          <br>&bull; <em>Disk Defragmenter:</em> Reorganizes fragmented non-contiguous file clusters on HDDs to contiguous spaces, speeding up disk read times.
          <br>&bull; <em>Disk Cleanup:</em> Scans and removes temporary files, cache, and recycle bin junk.
          <br>&bull; <em>File Compression Utilities:</em> WinRAR, WinZip, 7-Zip (uses lossless compression algorithms like DEFLATE).
          <br>&bull; <em>Backup &amp; Recovery:</em> System Restore, Acronis True Image.</span>
        <span class="lang-hi"><strong>3. यूटिलिटी सॉफ्टवेयर (रखरखाव प्रोग्राम):</strong>
          <br>&bull; कंप्यूटर की कार्यक्षमता को सुरक्षित, सुव्यवस्थित और अनुकूलित रखने वाले सहायक सॉफ्टवेयर।
          <br>&bull; <em>एंटीवायरस:</em> विंडोज डिफेंडर, क्विक हील, नॉर्टन (मैलवेयर से सुरक्षा)।
          <br>&bull; <em>डिस्क डिफ्रैग्मेंटर (Disk Defragmenter):</em> बिखरी हुई फाइलों के टुकड़ों को हार्ड डिस्क पर एक साथ व्यवस्थित कर पढ़ने की गति बढ़ाता है।
          <br>&bull; <em>डिस्क क्लीनअप:</em> अस्थायी फाइलों, कैश एवं ट्रैश को हटाकर डिस्क स्पेस खाली करता है।
          <br>&bull; <em>फाइल कम्प्रेशन:</em> 7-Zip, WinRAR, WinZip (फाइल का आकार छोटा करना)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>4. Classification by Distribution &amp; Licensing:</strong>
          <br>&bull; <em>Open Source Software (OSS):</em> Source code is freely accessible, modifiable, and redistributable. Examples: Linux kernel, Apache HTTP server, Python, LibreOffice, Mozilla Firefox, Android (AOSP).
          <br>&bull; <em>Proprietary / Closed Source:</em> Source code is private intellectual property; requires paid license; reverse engineering prohibited. Examples: MS Windows, MS Office, Adobe Photoshop, macOS.
          <br>&bull; <em>Freeware:</em> Available free of cost for indefinite use, but source code is NOT provided (closed-source). Examples: Adobe Acrobat Reader, Skype, Google Chrome.
          <br>&bull; <em>Shareware:</em> Distributed free on a trial basis for evaluation (e.g., 30 days trial); requires payment for continued full functionality. Examples: WinRAR.
          <br>&bull; <em>Firmware:</em> Software permanently embedded into hardware ROM/EEPROM chips. Examples: BIOS/UEFI, Microwave control software, Router firmware.</span>
        <span class="lang-hi"><strong>4. वितरण एवं लाइसेंसिंग के आधार पर वर्गीकरण:</strong>
          <br>&bull; <em>ओपन सोर्स सॉफ्टवेयर (OSS):</em> जिसका सोर्स कोड सभी के लिए निःशुल्क उपलब्ध, संपादन योग्य और पुनर्वितरित करने योग्य होता है। उदाहरण: लिनक्स (Linux), अपाचे, पायथन, लिब्रे ऑफिस, मोज़िला फ़ायरफ़ॉक्स।
          <br>&bull; <em>प्रोप्राइटरी (Proprietary / क्लोज्ड सोर्स):</em> कॉपीराइट सुरक्षित सॉफ्टवेयर जिसका सोर्स कोड गुप्त होता है और उपयोग हेतु लाइसेंस खरीदना पड़ता है। उदाहरण: MS विंडोज, MS ऑफिस, फोटोशॉप।
          <br>&bull; <em>फ्रीवेयर (Freeware):</em> निःशुल्क उपलब्ध सॉफ्टवेयर, परंतु इसका सोर्स कोड नहीं दिया जाता। उदाहरण: एडोब एक्रोबैट रीडर, गूगल क्रोम।
          <br>&bull; <em>शेयरवेयर (Shareware):</em> परीक्षण हेतु सीमित अवधि (जैसे 30 दिन का ट्रायल) के लिए निःशुल्क मिलने वाला सॉफ्टवेयर (उदा. WinRAR)।
          <br>&bull; <em>फर्मवेयर (Firmware):</em> हार्डवेयर (ROM चिप) में स्थायी रूप से संचित सॉफ्टवेयर (जैसे BIOS)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Language Translators Deep Dive -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Language Translators: Assembler, Compiler, Interpreter, Linker &amp; Loader</span>
    <span class="lang-hi">4. भाषा अनुवादक: असेंबलर, कंपाइलर, इंटरप्रेटर, लिंकर एवं लोडर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Assembler (असेंबलर):</strong>
          <br>&bull; System software that translates low-level <strong>Assembly Language mnemonic instructions</strong> (such as MOV, ADD, SUB, JMP) directly into binary <strong>Machine Code (0 and 1)</strong>.</span>
        <span class="lang-hi"><strong>असेंबलर (Assembler):</strong>
          <br>&bull; वह भाषा अनुवादक जो निम्न-स्तरीय <strong>असेंबली भाषा के निमोनिक कोड (जैसे ADD, SUB, MOV)</strong> को सीधे बाइनरी <strong>मशीन भाषा (0 और 1)</strong> में परिवर्तित करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Compiler (कंपाइलर):</strong>
          <br>&bull; Translates the <strong>entire source program</strong> written in High-Level Language (HLL) into target Machine/Object code (.obj) <strong>all at once in a single pass</strong>.
          <br>&bull; Detects syntax errors and displays a complete list of errors after scanning the whole file.
          <br>&bull; Execution speed of compiled code is extremely fast. Languages: C, C++, COBOL, Pascal, Go, Rust.</span>
        <span class="lang-hi"><strong>कंपाइलर (Compiler):</strong>
          <br>&bull; उच्च-स्तरीय भाषा (HLL) में लिखे <strong>संपूर्ण प्रोग्राम को एक ही बार में</strong> मशीन / ऑब्जेक्ट कोड में अनुवादित करता है।
          <br>&bull; संपूर्ण प्रोग्राम को पढ़ने के पश्चात सभी सिंटैक्स त्रुटियों की सूची एक साथ प्रदर्शित करता है।
          <br>&bull; प्रोग्राम का निष्पादन अत्यंत तीव्र होता है। उदाहरण: C, C++, फोरट्रान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Interpreter (इंटरप्रेटर):</strong>
          <br>&bull; Translates and executes high-level source code <strong>line-by-line sequentially</strong>.
          <br>&bull; If an error occurs on any line, execution <strong>immediately halts</strong>, making debugging very easy.
          <br>&bull; Does NOT generate a separate standalone object file (.obj); execution is slower as translation repeats each run. Languages: Python, JavaScript, Ruby, PHP, BASIC.</span>
        <span class="lang-hi"><strong>इंटरप्रेटर (Interpreter):</strong>
          <br>&bull; उच्च-स्तरीय भाषा के सोर्स कोड को <strong>एक-एक पंक्ति करके (लाइन-बाय-लाइन)</strong> पढ़ता और तुरंत निष्पादित करता है।
          <br>&bull; किसी पंक्ति में त्रुटि मिलते ही निष्पादन <strong>तुरंत रुक जाता है</strong>, जिससे डिबगिंग सरल होती है।
          <br>&bull; यह कोई स्थायी ऑब्जेक्ट कोड फाइल नहीं बनाता; गति अपेक्षाकृत धीमी होती है। उदाहरण: पायथन, जावास्क्रिप्ट, बेसिक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Linker and Loader (लिंकर एवं लोडर):</strong>
          <br>&bull; <em>Linker (लिंकर):</em> Takes one or more object code files (.obj) generated by compiler/assembler, links required system library functions, and combines them into a single executable file (<strong>.exe</strong> in Windows).
          <br>&bull; <em>Loader (लोडर):</em> System utility that copies the executable program from secondary storage (HDD/SSD) into main RAM, allocates memory addresses, and hands over control to the CPU for execution.</span>
        <span class="lang-hi"><strong>लिंकर एवं लोडर (Linker &amp; Loader):</strong>
          <br>&bull; <em>लिंकर:</em> कंपाइलर द्वारा निर्मित विभिन्न ऑब्जेक्ट फाइलों (.obj) तथा सिस्टम लाइब्रेरी कोड को आपस में जोड़कर एक स्वतंत्र निष्पादन योग्य फाइल (<strong>.exe</strong>) बनाता है।
          <br>&bull; <em>लोडर:</em> निष्पादन योग्य प्रोग्राम को सेकेंडरी डिस्क से उठाकर मुख्य मेमोरी (RAM) में लोड करता है और सीपीयू को निष्पादन हेतु सौंपता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Memory Units & Storage Capacity Table -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Memory Measurement Units &amp; Binary Conversion Matrix</span>
    <span class="lang-hi">5. कंप्यूटर मेमोरी मापन इकाइयां एवं बाइनरी रूपांतरण सारणी</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Unit Name</span>
            <span class="lang-hi">इकाई का नाम</span>
          </th>
          <th>
            <span class="lang-en">Short Form</span>
            <span class="lang-hi">संक्षिप्त रूप</span>
          </th>
          <th>
            <span class="lang-en">Equivalent Capacity</span>
            <span class="lang-hi">समतुल्य क्षमता</span>
          </th>
          <th>
            <span class="lang-en">Power of 2 / Bits</span>
            <span class="lang-hi">2 की घात / बिट्स</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Binary Digit</span>
            <span class="lang-hi">बाइनरी डिजिट</span>
          </td>
          <td>Bit (b)</td>
          <td>
            <span class="lang-en">Smallest storage unit (0 or 1)</span>
            <span class="lang-hi">सबसे छोटी इकाई (0 या 1)</span>
          </td>
          <td>1 bit</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Nibble</span>
            <span class="lang-hi">निब्बल</span>
          </td>
          <td>Nibble</td>
          <td>
            <span class="lang-en">4 Bits (Half a Byte)</span>
            <span class="lang-hi">4 बिट्स (आधा बाइट)</span>
          </td>
          <td>4 bits</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Byte</span>
            <span class="lang-hi">बाइट</span>
          </td>
          <td>Byte (B)</td>
          <td>
            <span class="lang-en">8 Bits (Stores 1 ASCII character)</span>
            <span class="lang-hi">8 बिट्स (1 अक्षर सुरक्षित करने हेतु)</span>
          </td>
          <td>8 bits = 2^3 bits</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Kilobyte</span>
            <span class="lang-hi">किलोबाइट</span>
          </td>
          <td>KB</td>
          <td>
            <span class="lang-en">1,024 Bytes</span>
            <span class="lang-hi">1,024 बाइट्स</span>
          </td>
          <td>2^10 Bytes</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Megabyte</span>
            <span class="lang-hi">मेगाबाइट</span>
          </td>
          <td>MB</td>
          <td>
            <span class="lang-en">1,024 Kilobytes (KB)</span>
            <span class="lang-hi">1,024 KB</span>
          </td>
          <td>2^20 Bytes (~1 Million B)</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Gigabyte</span>
            <span class="lang-hi">गीगाबाइट</span>
          </td>
          <td>GB</td>
          <td>
            <span class="lang-en">1,024 Megabytes (MB)</span>
            <span class="lang-hi">1,024 MB</span>
          </td>
          <td>2^30 Bytes (~1 Billion B)</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Terabyte</span>
            <span class="lang-hi">टेराबाइट</span>
          </td>
          <td>TB</td>
          <td>
            <span class="lang-en">1,024 Gigabytes (GB)</span>
            <span class="lang-hi">1,024 GB</span>
          </td>
          <td>2^40 Bytes (~1 Trillion B)</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Petabyte</span>
            <span class="lang-hi">पेटाबाइट</span>
          </td>
          <td>PB</td>
          <td>
            <span class="lang-en">1,024 Terabytes (TB)</span>
            <span class="lang-hi">1,024 TB</span>
          </td>
          <td>2^50 Bytes</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Exabyte</span>
            <span class="lang-hi">एक्सोबाइट</span>
          </td>
          <td>EB</td>
          <td>
            <span class="lang-en">1,024 Petabytes (PB)</span>
            <span class="lang-hi">1,024 PB</span>
          </td>
          <td>2^60 Bytes</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Zettabyte</span>
            <span class="lang-hi">जेटाबाइट</span>
          </td>
          <td>ZB</td>
          <td>
            <span class="lang-en">1,024 Exabytes (EB)</span>
            <span class="lang-hi">1,024 EB</span>
          </td>
          <td>2^70 Bytes</td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Yottabyte</span>
            <span class="lang-hi">योटाबाइट</span>
          </td>
          <td>YB</td>
          <td>
            <span class="lang-en">1,024 Zettabytes (ZB)</span>
            <span class="lang-hi">1,024 ZB</span>
          </td>
          <td>2^80 Bytes</td>
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
            <span class="lang-en">Key Concept / Question</span>
            <span class="lang-hi">प्रमुख संकल्पना / परीक्षा प्रश्न</span>
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
            <span class="lang-en">Fastest Memory in Computer System</span>
            <span class="lang-hi">कंप्यूटर सिस्टम में सबसे तीव्र मेमोरी</span>
          </td>
          <td>
            <span class="lang-en"><strong>CPU Registers</strong> (followed by L1 Cache).</span>
            <span class="lang-hi"><strong>सीपीयू रजिस्टर्स</strong> (इसके पश्चात L1 कैश)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Difference between 1 Byte and 1 Nibble</span>
            <span class="lang-hi">1 बाइट और 1 निब्बल में अंतर</span>
          </td>
          <td>
            <span class="lang-en"><strong>1 Byte = 8 Bits = 2 Nibbles</strong>; <strong>1 Nibble = 4 Bits</strong>.</span>
            <span class="lang-hi"><strong>1 बाइट = 8 बिट्स = 2 निब्बल</strong>; <strong>1 निब्बल = 4 बिट्स</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Nature of RAM vs ROM</span>
            <span class="lang-hi">रैम और रोम की प्रकृति (Volatile vs Non-Volatile)</span>
          </td>
          <td>
            <span class="lang-en"><strong>RAM is Volatile</strong> (temporary); <strong>ROM is Non-Volatile</strong> (permanent).</span>
            <span class="lang-hi"><strong>रैम अस्थायी (Volatile)</strong> है; <strong>रोम स्थायी (Non-Volatile)</strong> है।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Which RAM requires continuous refreshing?</span>
            <span class="lang-hi">किस रैम को निरंतर रिफ्रेश करने की आवश्यकता होती है?</span>
          </td>
          <td>
            <span class="lang-en"><strong>DRAM (Dynamic RAM)</strong> (due to capacitor discharge).</span>
            <span class="lang-hi"><strong>DRAM (डायनामिक रैम)</strong> (कैपेसिटर चार्ज रिसाव के कारण)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Which memory chip stores the BIOS program?</span>
            <span class="lang-hi">BIOS प्रोग्राम किस चिप में सुरक्षित रहता है?</span>
          </td>
          <td>
            <span class="lang-en"><strong>ROM / EEPROM</strong> (Flash ROM on motherboard).</span>
            <span class="lang-hi"><strong>ROM / EEPROM</strong> (मदरबोर्ड पर फ्लैश रोम चिप)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Hardware self-test executed during boot</span>
            <span class="lang-hi">बूटिंग के समय चलने वाला हार्डवेयर परीक्षण</span>
          </td>
          <td>
            <span class="lang-en"><strong>POST (Power-On Self-Test)</strong>.</span>
            <span class="lang-hi"><strong>POST (पावर-ऑन सेल्फ-टेस्ट)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Battery used to retain CMOS settings</span>
            <span class="lang-hi">CMOS सेटिंग्स सुरक्षित रखने वाला सेल</span>
          </td>
          <td>
            <span class="lang-en"><strong>CR2032 Lithium Coin Cell (3V)</strong>.</span>
            <span class="lang-hi"><strong>CR2032 लिथियम कॉइन सेल (3V)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Translator that converts line-by-line</span>
            <span class="lang-hi">वह अनुवादक जो पंक्ति-दर-पंक्ति अनुवाद करता है</span>
          </td>
          <td>
            <span class="lang-en"><strong>Interpreter</strong> (e.g. in Python). Compiler converts whole file.</span>
            <span class="lang-hi"><strong>इंटरप्रेटर</strong> (उदा. पायथन)। कंपाइलर एक साथ पूरा अनुवाद करता है।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Program that combines object modules into .exe</span>
            <span class="lang-hi">ऑब्जेक्ट कोड को जोड़कर .exe बनाने वाला प्रोग्राम</span>
          </td>
          <td>
            <span class="lang-en"><strong>Linker</strong>.</span>
            <span class="lang-hi"><strong>लिंकर (Linker)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Storage capacity of standard CD vs DVD</span>
            <span class="lang-hi">मानक CD और DVD की भंडारण क्षमता</span>
          </td>
          <td>
            <span class="lang-en"><strong>CD = 700 MB</strong>; <strong>Single-layer DVD = 4.7 GB</strong>; <strong>Blu-ray = 25 GB</strong>.</span>
            <span class="lang-hi"><strong>CD = 700 MB</strong>; <strong>DVD = 4.7 GB</strong>; <strong>ब्लू-रे = 25 GB</strong>।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-computer", "hardware-and-software", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_hardware_software_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
