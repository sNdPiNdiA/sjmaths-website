import os
import re

def build_os_egov_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Operating Systems, Social Networks &amp; E-Governance</span>
    <span class="lang-hi">माइंड मैप: ऑपरेटिंग सिस्टम, सोशल नेटवर्किंग एवं ई-गवर्नेंस</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[OS, Social Media & E-Governance] --> B[Operating System Architecture]
    A --> C[Core OS Functions & Scheduling]
    A --> D[Social Networking Ecosystem]
    A --> E[E-Governance Models & Initiatives]

    B --> B1[Types: Batch, Time-sharing, Real-time RTOS, Distributed]
    B --> B2[Kernel: Monolithic Linux vs Microkernel Minix/QNX]
    B --> B3[Dual Mode: User Mode Ring 3 vs Kernel Mode Ring 0]

    C --> C1[CPU Scheduling: FCFS, SJF, Round Robin Quantum, Priority]
    C --> C2[Memory: Virtual Memory, Paging, Page Fault, Thrashing]
    C --> C3[File Systems: FAT32, NTFS Windows, ext4 Linux]

    D --> D1[Platforms: X 2006 280 chars, FB 2004, LinkedIn 2002, WA 2009]
    D --> D2[Indian Apps: Koo Microblogging, Sandes, ShareChat]
    D --> D3[Features: Hashtags 2007 Messina, Cloud Storage, P2P Messaging]

    E --> E1[Models: G2C Citizen, G2B Business, G2G Gov, G2E Employee]
    E --> E2[National: Digital India 2015 9 Pillars, DigiLocker 1GB, UMANG, GeM]
    E --> E3[UP State: e-District, IGRS Jansunwai, Bhulekh UP, Nivesh Mitra]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[ओएस, सोशल मीडिया एवं ई-गवर्नेंस] --> B[ऑपरेटिंग सिस्टम वास्तुकला]
    A --> C[ओएस के मुख्य कार्य एवं शेड्यूलिंग]
    A --> D[सोशल नेटवर्किंग इकोसिस्टम]
    A --> E[ई-गवर्नेंस मॉडल एवं प्रमुख पहलें]

    B --> B1[प्रकार: बैच, टाइम-शेयरिंग, रियल-टाइम RTOS, वितरित]
    B --> B2[कर्नल: मोनोलिथिक लिनक्स बनाम माइक्रोकर्नल Minix]
    B --> B3[ड्यूल मोड: यूजर मोड रिंग 3 बनाम कर्नल मोड रिंग 0]

    C --> C1[सीपीयू शेड्यूलिंग: FCFS, SJF, राउंड रॉबिन क्वांटम]
    C --> C2[मेमोरी: वर्चुअल मेमोरी, पेजिंग, पेज फॉल्ट, थ्रैशिंग]
    C --> C3[फाइल सिस्टम: FAT32, NTFS विंडोज, ext4 लिनक्स]

    D --> D1[प्लेटफॉर्म: X 2006, फेसबुक 2004, लिंक्डइन 2002, व्हाट्सएप]
    D --> D2[भारतीय ऐप्स: कू (Koo), संदेश (Sandes), शेयरचैट]
    D --> D3[विशेषताएं: हैशटैग 2007, क्लाउड स्टोरेज, P2P मैसेजिंग]

    E --> E1[मॉडल: G2C नागरिक, G2B व्यापार, G2G अंतर-सरकारी, G2E]
    E --> E2[राष्ट्रीय: डिजिटल इंडिया 2015, डिजिलॉकर 1GB, उमंग, GeM]
    E --> E3[यूपी राज्य: ई-डिस्ट्रिक्ट, आईजीआरएस जनसुनवाई, भूलेख, निवेश मित्र]
    </div>
  </div>
</div>

<!-- Card 2: Operating System Architecture & Types -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Operating System: Architecture, Kernel &amp; OS Classifications</span>
    <span class="lang-hi">1. ऑपरेटिंग सिस्टम: वास्तुकला, कर्नल एवं ओएस का वर्गीकरण</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Definition &amp; Dual-Mode Operation:</strong>
          <br>&bull; An <strong>Operating System (OS)</strong> is foundational system software that manages computer hardware resources (CPU, RAM, storage, I/O) and provides a secure execution environment for applications.
          <br>&bull; <em>Dual Mode Operation:</em> To prevent rogue user programs from crashing the system, the CPU executes in two distinct modes:
            <br>&nbsp;&nbsp;&bull; <strong>User Mode (Non-privileged / Ring 3):</strong> User applications run here with restricted hardware access.
            <br>&nbsp;&nbsp;&bull; <strong>Kernel / Supervisor Mode (Privileged / Ring 0):</strong> The core OS kernel executes here with direct, unrestricted hardware execution rights. Transitions occur via <strong>System Calls (Syscalls)</strong>.</span>
        <span class="lang-hi"><strong>परिभाषा एवं डुअल-मोड संचालन:</strong>
          <br>&bull; <strong>ऑपरेटिंग सिस्टम (OS)</strong> एक आधारभूत सिस्टम सॉफ्टवेयर है जो कंप्यूटर हार्डवेयर (सीपीयू, रैम, स्टोरेज, इनपुट/आउटपुट) का प्रबंधन करता है एवं यूजर और हार्डवेयर के मध्य इंटरफेस प्रदान करता है।
          <br>&bull; <em>ड्यूल मोड संचालन:</em> सिस्टम सुरक्षा हेतु सीपीयू दो स्तरों पर कार्य करता है:
            <br>&nbsp;&nbsp;&bull; <strong>यूज़र मोड (Ring 3):</strong> यूजर प्रोग्राम इस गैर-विशेषाधिकार प्राप्त मोड में चलते हैं।
            <br>&nbsp;&nbsp;&bull; <strong>कर्नल / सुपरवाइज़र मोड (Ring 0):</strong> ओएस का मुख्य कर्नल इस विशेषाधिकार प्राप्त मोड में सीधे हार्डवेयर को नियंत्रित करता है; यूज़र प्रोग्राम <strong>सिस्टम कॉल (System Call)</strong> के माध्यम से कर्नल से सेवा मांगते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Kernel Types:</strong>
          <br>&bull; <strong>Kernel:</strong> The central core component of an OS loaded into memory during booting; remains in RAM throughout system uptime.
          <br>&bull; <em>Monolithic Kernel:</em> All OS services (process management, memory, file system, device drivers) run inside a single large kernel space in Ring 0 (e.g., <strong>Linux, Unix, MS-DOS</strong>). Faster execution, but a bug in any driver can crash the entire system.
          <br>&bull; <em>Microkernel:</em> Only essential mechanisms (IPC, basic scheduling, memory mapping) reside in kernel space; drivers and file systems run in user space (e.g., <strong>Minix, QNX</strong>). Highly stable and crash-resistant, but slower IPC.</span>
        <span class="lang-hi"><strong>कर्नल के प्रकार:</strong>
          <br>&bull; <strong>कर्नल (Kernel):</strong> ऑपरेटिंग सिस्टम का केंद्रीय हृदय (Core); बूटिंग के समय रैम में लोड होता है और कंप्यूटर बंद होने तक रैम में बना रहता है।
          <br>&bull; <em>मोनोलिथिक कर्नल:</em> सभी सेवाएं (मेमोरी, डिवाइस ड्राइवर, फाइल सिस्टम) एक ही कर्नल स्पेस में चलती हैं (उदा: <strong>लिनक्स, यूनिक्स, डॉस</strong>); तीव्र गति, किंतु ड्राइवर क्रैश होने पर पूरा सिस्टम क्रैश हो सकता है।
          <br>&bull; <em>माइक्रोकर्नल:</em> केवल न्यूनतम आवश्यक सेवाएं कर्नल में रहती हैं, बाकी यूजर स्पेस में चलती हैं (उदा: <strong>Minix, QNX</strong>); अत्यधिक स्थिर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Classification of Operating Systems:</strong>
          <br>&bull; <em>Batch Operating System:</em> Similar jobs are grouped into batches and processed sequentially without human user intervention (e.g., early IBM mainframes).
          <br>&bull; <em>Multiprogramming OS:</em> Keeps multiple programs in main memory simultaneously; when one program waits for I/O, the CPU switches to another program, maximizing CPU utilization.
          <br>&bull; <em>Time-Sharing / Multitasking OS:</em> CPU switches between active processes so rapidly using small time slices (Time Quanta) that users perceive concurrent execution (e.g., <strong>Windows, Linux, macOS</strong>).
          <br>&bull; <em>Real-Time Operating System (RTOS):</em> Guaranteed completion of tasks within strict deterministic deadlines (hard real-time vs soft real-time); used in <strong>missile guidance, industrial robots, pacemaker medical implants, automotive ABS</strong> (e.g., <strong>VxWorks, RTLinux, QNX</strong>).
          <br>&bull; <em>Distributed OS:</em> Manages a collection of independent networked computers appearing to the user as a single coherent system.</span>
        <span class="lang-hi"><strong>ऑपरेटिंग सिस्टम का वर्गीकरण:</strong>
          <br>&bull; <em>बैच ऑपरेटिंग सिस्टम:</em> एक जैसे कार्यों को बैच में समूहीकृत कर बिना मानवीय हस्तक्षेप के क्रमानुसार प्रोसेस किया जाता है।
          <br>&bull; <em>मल्टीप्रोग्रामिंग ओएस:</em> मुख्य मेमोरी में एक साथ कई प्रोग्राम रखे जाते हैं; एक प्रोग्राम द्वारा I/O प्रतीक्षा करने पर सीपीयू दूसरे प्रोग्राम पर स्विच कर सीपीयू दक्षता बढ़ाता है।
          <br>&bull; <em>टाइम-शेयरिंग / मल्टीटास्किंग:</em> सीपीयू समय को छोटे-छोटे टुकड़ों (टाइम स्लाइस/क्वांटम) में विभाजित कर कई प्रोग्रामों को लगभग एक साथ चलाता है (उदा: <strong>विंडोज, लिनक्स, मैकओएस</strong>)।
          <br>&bull; <em>रियल-टाइम ऑपरेटिंग सिस्टम (RTOS):</em> कार्यों को पूर्व-निर्धारित अत्यंत सख्त समय-सीमा (Deadlines) में पूरा करता है; <strong>मिसाइल गाइडेंस, रोबोटिक्स, सैटेलाइट, मेडिकल वेंटिलेटर</strong> में प्रयुक्त (उदा: <strong>VxWorks, RTLinux</strong>)।
          <br>&bull; <em>डिस्ट्रिब्यूटेड ओएस:</em> कई स्वतंत्र नेटवर्क कंप्यूटरों को एकल सिस्टम के रूप में प्रबंधित करता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Process Scheduling, Virtual Memory & File Systems -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Process Scheduling, Virtual Memory &amp; File Systems</span>
    <span class="lang-hi">2. प्रोसेस शेड्यूलिंग, वर्चुअल मेमोरी एवं फाइल सिस्टम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Process States &amp; CPU Scheduling Algorithms:</strong>
          <br>&bull; <em>Process Lifecycle States:</em> <strong>New &rarr; Ready &rarr; Running &rarr; Waiting (Blocked) &rarr; Terminated</strong>.
          <br>&bull; <em>FCFS (First-Come, First-Served):</em> Non-preemptive; processes executed in arrival order; suffers from the <strong>Convoy Effect</strong> (short processes stuck behind long CPU-bound jobs).
          <br>&bull; <em>SJF (Shortest Job First):</em> Selects process with smallest CPU burst time; optimal average waiting time; risk of <strong>Starvation</strong> for longer jobs.
          <br>&bull; <em>Round Robin (RR):</em> Preemptive; cyclic allocation using a fixed <strong>Time Quantum</strong>; universally used in time-sharing interactive OS.
          <br>&bull; <em>Deadlock (गतिरोध):</em> A condition where two or more processes are permanently blocked, each holding a resource and waiting for another resource held by the other. Coffman's 4 conditions: Mutual Exclusion, Hold &amp; Wait, No Preemption, Circular Wait.</span>
        <span class="lang-hi"><strong>प्रोसेस अवस्थाएं एवं शेड्यूलिंग एल्गोरिदम:</strong>
          <br>&bull; <em>प्रोसेस के 5 जीवन चक्र:</em> <strong>New (नई) &rarr; Ready (तैयार) &rarr; Running (सक्रिय) &rarr; Waiting/Blocked (प्रतीक्षारत) &rarr; Terminated (समाप्त)</strong>।
          <br>&bull; <em>FCFS (पहले आओ, पहले पाओ):</em> आगमन क्रम में निष्पादन; कॉन्वॉय प्रभाव (Convoy Effect) से ग्रसित।
          <br>&bull; <em>SJF (शॉर्टेस्ट जॉब फर्स्ट):</em> सबसे छोटे कार्य को पहले चुनता है; न्यूनतम औसत प्रतीक्षा समय।
          <br>&bull; <em>राउंड रॉबिन (Round Robin):</em> प्रत्येक प्रोसेस को एक निश्चित <strong>टाइम क्वांटम (Time Quantum)</strong> आवंटित किया जाता है; टाइम-शेयरिंग सिस्टम का मुख्य आधार।
          <br>&bull; <em>डेडलॉक (Deadlock):</em> ऐसी स्थिति जब दो या दो से अधिक प्रक्रियाएं एक-दूसरे द्वारा रोके गए संसाधनों की प्रतीक्षा में सदैव के लिए अटक जाती हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Virtual Memory &amp; Paging:</strong>
          <br>&bull; <em>Virtual Memory:</em> An OS memory management technique that creates an illusion of a large contiguous physical memory space by mapping virtual addresses to physical RAM and secondary hard disk space (<strong>Swap Space / Pagefile.sys</strong>).
          <br>&bull; <em>Paging:</em> Memory divided into fixed-size blocks: physical memory blocks are called <strong>Frames</strong>; logical memory blocks are called <strong>Pages</strong> (typically 4 KB).
          <br>&bull; <em>Page Fault:</em> An interrupt generated when an active program requests a page that is not currently loaded into physical RAM.
          <br>&bull; <em>Thrashing (थ्रैशिंग):</em> A catastrophic system degradation state where the CPU spends more time swapping pages back and forth between RAM and disk than executing actual instructions.</span>
        <span class="lang-hi"><strong>वर्चुअल मेमोरी एवं पेजिंग:</strong>
          <br>&bull; <em>वर्चुअल मेमोरी:</em> भौतिक रैम (RAM) की सीमा से बड़े प्रोग्रामों को चलाने हेतु हार्ड डिस्क के एक हिस्से को अस्थायी मेमोरी (<strong>Swap Space</strong>) के रूप में प्रयोग करने की तकनीक।
          <br>&bull; <em>पेजिंग (Paging):</em> लॉजिकल मेमोरी को निश्चित आकार के ब्लॉकों (<strong>Pages</strong>) में और फिजिकल रैम को (<strong>Frames</strong>) में विभाजित करना।
          <br>&bull; <em>पेज फॉल्ट (Page Fault):</em> जब प्रोग्राम किसी ऐसे पेज की मांग करता है जो वर्तमान में रैम में मौजूद नहीं है, तब पेज फॉल्ट उत्पन्न होता है।
          <br>&bull; <em>थ्रैशिंग (Thrashing):</em> अत्यधिक पेज फॉल्ट के कारण सीपीयू द्वारा वास्तविक निष्पादन करने के बजाय अधिकांश समय हार्ड डिस्क और रैम के बीच पेजों की अदला-बदली (Swapping) में बर्बाद करने की स्थिति।</span>
      </li>
      <li>
        <span class="lang-en"><strong>File Systems Architecture:</strong>
          <br>&bull; <strong>FAT32 (File Allocation Table):</strong> Legacy file system supported across all OS; max single file size limit is <strong>4 GB</strong>; max partition size 2 TB.
          <br>&bull; <strong>NTFS (New Technology File System):</strong> Modern default Windows file system; supports journaling, file encryption (EFS), compression, access permissions (ACL), and massive files up to 16 TB+.
          <br>&bull; <strong>ext4 (Fourth Extended Filesystem):</strong> Standard default journaling file system for Linux distributions.
          <br>&bull; <strong>APFS (Apple File System):</strong> Optimized for flash SSD storage on macOS and iOS.</span>
        <span class="lang-hi"><strong>फाइल सिस्टम वास्तुकला:</strong>
          <br>&bull; <strong>FAT32:</strong> पुराना फाइल सिस्टम; किसी एकल फाइल का अधिकतम आकार केवल <strong>4 GB</strong> हो सकता है।
          <br>&bull; <strong>NTFS (विंडोज):</strong> आधुनिक विंडोज का मानक फाइल सिस्टम; जर्नलिंग, फाइल एन्क्रिप्शन, एक्सेस अनुमतियां और विशाल फाइल आकार का समर्थन।
          <br>&bull; <strong>ext4:</strong> लिनक्स ऑपरेटिंग सिस्टम का मानक डिफॉल्ट फाइल सिस्टम।
          <br>&bull; <strong>APFS:</strong> ऐप्पल मैकओएस एवं आईओएस का आधुनिक सॉलिड-स्टेट फाइल सिस्टम।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Social Networking Platforms -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Social Networking Platforms: Origins, Mechanics &amp; Indian Ecosystem</span>
    <span class="lang-hi">3. सोशल नेटवर्किंग प्लेटफॉर्म: उद्भव, कार्यप्रणाली एवं भारतीय इकोसिस्टम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Global Social Platforms Fact Sheet:</strong>
          <br>&bull; <em>Facebook:</em> Founded in <strong>2004</strong> by <strong>Mark Zuckerberg</strong> at Harvard University; parent company rebranded as <strong>Meta</strong> (2021).
          <br>&bull; <em>X (formerly Twitter):</em> Founded in <strong>2006</strong> by <strong>Jack Dorsey, Biz Stone, and Evan Williams</strong>; microblogging platform; character limit expanded from 140 to <strong>280 characters</strong>; acquired by Elon Musk (2022).
          <br>&bull; <em>Hashtag (#):</em> First proposed for categorizing social media posts by <strong>Chris Messina</strong> on Twitter on August 23, 2007.
          <br>&bull; <em>Instagram:</em> Founded in <strong>2010</strong> by Kevin Systrom and Mike Krieger; photo and video sharing platform; acquired by Facebook (2012).
          <br>&bull; <em>LinkedIn:</em> Founded in <strong>2002</strong> by <strong>Reid Hoffman</strong>; premier professional networking and career development portal; acquired by Microsoft (2016).
          <br>&bull; <em>YouTube:</em> Video sharing platform created in <strong>February 2005</strong> by Chad Hurley, Steve Chen, and Jawed Karim; first video uploaded was 'Me at the zoo'; acquired by Google (2006).
          <br>&bull; <em>WhatsApp:</em> Instant messaging application founded in <strong>2009</strong> by Jan Koum and Brian Acton; end-to-end encryption; acquired by Facebook (2014).</span>
        <span class="lang-hi"><strong>वैश्विक सोशल मीडिया प्लेटफॉर्म तथ्य:</strong>
          <br>&bull; <em>फेसबुक (Facebook):</em> स्थापना <strong>2004</strong> में <strong>मार्क जुकरबर्ग</strong> द्वारा; मूल कंपनी का नाम 2021 में बदलकर <strong>मेटा (Meta)</strong> किया गया।
          <br>&bull; <em>X (पूर्व में ट्विटर):</em> स्थापना <strong>2006</strong> में <strong>जैक डॉर्सी</strong> द्वारा; माइक्रोब्लॉगिंग प्लेटफॉर्म; मानक शब्द सीमा <strong>280 कैरेक्टर</strong>।
          <br>&bull; <em>हैशटैग (#):</em> सोशल मीडिया पर पोस्ट वर्गीकरण हेतु हैशटैग का सर्वप्रथम सुझाव <strong>क्रिस मेसिना</strong> (2007) द्वारा ट्विटर पर दिया गया था।
          <br>&bull; <em>इंस्टाग्राम:</em> स्थापना <strong>2010</strong> में केविन सिस्ट्रॉम और माइक क्राइगर द्वारा; 2012 में मेटा द्वारा अधिग्रहीत।
          <br>&bull; <em>लिंक्डइन (LinkedIn):</em> स्थापना <strong>2002</strong> में <strong>रीड हॉफमैन</strong> द्वारा; पेशेवर नेटवर्किंग एवं रोजगार पोर्टल; माइक्रोसॉफ्ट द्वारा 2016 में अधिग्रहीत।
          <br>&bull; <em>यूट्यूब (YouTube):</em> स्थापना <strong>2005</strong> में चाड हर्ले, स्टीव चेन एवं जावेद करीम द्वारा; पहला वीडियो 'Me at the zoo'; 2006 में गूगल द्वारा अधिग्रहीत।
          <br>&bull; <em>व्हाट्सएप (WhatsApp):</em> <strong>2009</strong> में ब्रायन एक्टन व जान कौम द्वारा निर्मित; एंड-टू-एंड एन्क्रिप्टेड मैसेजिंग; 2014 में मेटा द्वारा अधिग्रहीत।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Indian Indigenous Platforms &amp; Apps:</strong>
          <br>&bull; <em>Sandes:</em> Indigenous instant messaging platform developed by the <strong>National Informatics Centre (NIC)</strong> for secure government official and citizen communications.
          <br>&bull; <em>Koo:</em> Indian multi-lingual microblogging platform launched by Aprameya Radhakrishna and Mayank Bidawatka (2020) supporting regional Indian languages with a yellow bird icon.
          <br>&bull; <em>ShareChat:</em> Indian social media and regional language networking platform founded by Mohit Saxena, Farid Ahsan, and Ankush Sachdeva.</span>
        <span class="lang-hi"><strong>भारतीय स्वदेशी प्लेटफॉर्म एवं ऐप्स:</strong>
          <br>&bull; <em>संदेश ऐप (Sandes):</em> <strong>राष्ट्रीय सूचना विज्ञान केंद्र (NIC)</strong> द्वारा सरकारी और नागरिक संचार हेतु विकसित सुरक्षित स्वदेशी इंस्टेंट मैसेजिंग ऐप।
          <br>&bull; <em>कू (Koo):</em> भारतीय भाषाओं में उपलब्ध स्वदेशी माइक्रोब्लॉगिंग प्लेटफॉर्म (पीली चिड़िया प्रतीक)।
          <br>&bull; <em>शेयरचैट (ShareChat):</em> भारतीय क्षेत्रीय भाषाओं का सोशल नेटवर्किंग प्लेटफॉर्म।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: E-Governance Models & National Initiatives -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. E-Governance: 4 Interaction Models &amp; National Digital Initiatives</span>
    <span class="lang-hi">4. ई-गवर्नेंस: 4 संपर्क मॉडल एवं प्रमुख राष्ट्रीय डिजिटल पहलें</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>The 4 E-Governance Interaction Models:</strong>
          <br>&bull; <strong>G2C (Government-to-Citizen):</strong> Direct delivery of public services to citizens (e.g., Aadhaar portal, DigiLocker, passport online seva, electricity bill payment, e-District services).
          <br>&bull; <strong>G2B (Government-to-Business):</strong> Electronic interfaces between government and commercial business enterprises (e.g., GSTN portal, MCA21 corporate filings, GeM e-bidding, trade licenses).
          <br>&bull; <strong>G2G (Government-to-Government):</strong> Seamless electronic information sharing between central, state, and local administrative bodies (e.g., Smart Governance intranets, PRAGATI, CCTNS crime tracking network).
          <br>&bull; <strong>G2E (Government-to-Employee):</strong> Internal administrative automation for government personnel (e.g., online GPF, SPARROW appraisal system, e-Office, pension tracking).</span>
        <span class="lang-hi"><strong>ई-गवर्नेंस के 4 प्रमुख संपर्क मॉडल:</strong>
          <br>&bull; <strong>G2C (सरकार-से-नागरिक):</strong> नागरिकों को सीधे सरकारी सेवाओं का वितरण (उदा: आधार, डिजिलॉकर, ऑनलाइन पासपोर्ट सेवा, ई-डिस्ट्रिक्ट)।
          <br>&bull; <strong>G2B (सरकार-से-व्यापार):</strong> सरकार और व्यावसायिक उद्यमों के मध्य डिजिटल सेवाएं (उदा: जीएसटी पोर्टल, एमसीए21 कंपनी पंजीकरण, GeM टेंडर)।
          <br>&bull; <strong>G2G (सरकार-से-सरकार):</strong> विभिन्न सरकारी विभागों, केंद्र एवं राज्य सरकारों के मध्य डेटा साझाकरण (उदा: PRAGATI समीक्षा प्रणाली, CCTNS पुलिस नेटवर्क)।
          <br>&bull; <strong>G2E (सरकार-से-कर्मचारी):</strong> सरकारी कर्मचारियों हेतु आंतरिक डिजिटल सेवाएं (उदा: ई-ऑफिस, ऑनलाइन पीएफ व पेंशन पोर्टल, स्पैरो ACR)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>National Digital Flagship Initiatives:</strong>
          <br>&bull; <em>National e-Governance Plan (NeGP):</em> Formulated in <strong>May 2006</strong> comprising 31 Mission Mode Projects (MMPs) implemented across Central, State, and Integrated levels.
          <br>&bull; <em>Digital India Programme:</em> Launched on <strong>1 July 2015</strong> by Prime Minister Narendra Modi based on <strong>9 Pillars</strong> (Broadband Highways, Universal Mobile Access, Public Internet Access, e-Governance, e-Kranti, Information for All, Electronics Manufacturing, IT for Jobs, Early Harvest Programmes).
          <br>&bull; <em>DigiLocker:</em> Flagship cloud storage initiative under Digital India launched in <strong>2015</strong>. Provides every Aadhaar-linked citizen with <strong>1 GB free secure cloud storage</strong>. Issued electronic documents in DigiLocker carry legal parity with physical originals under <strong>Rule 9A of Information Technology (Preservation and Retention of Information) Rules, 2016</strong>.
          <br>&bull; <em>UMANG (Unified Mobile Application for New-age Governance):</em> Launched in <strong>November 2017</strong>; multi-lingual unified mobile gateway providing single-app access to over 1,500+ Central and State government services (EPFO, PAN, Aadhaar, DigiLocker, Gas booking).
          <br>&bull; <em>GeM (Government e-Marketplace):</em> Online public procurement portal launched in <strong>August 2016</strong> by Ministry of Commerce and Industry to facilitate transparent, contactless procurement of goods and services by all government ministries, departments, and PSUs.
          <br>&bull; <em>PRAGATI:</em> <strong>Pro-Active Governance and Timely Implementation</strong> launched in 2015; multi-modal platform chaired by the Prime Minister integrating video conferencing, cloud, and GIS to review mega infrastructure projects.
          <br>&bull; <em>BharatNet:</em> World's largest rural broadband project aiming to connect all <strong>2.5 lakh Gram Panchayats</strong> across India via high-speed optical fiber cable (OFC) network.</span>
        <span class="lang-hi"><strong>राष्ट्रीय डिजिटल पहलें एवं महत्वपूर्ण कार्यक्रम:</strong>
          <br>&bull; <em>राष्ट्रीय ई-गवर्नेंस योजना (NeGP):</em> <strong>मई 2006</strong> में 31 मिशन मोड प्रोजेक्ट्स (MMPs) के साथ स्वीकृत।
          <br>&bull; <em>डिजिटल इंडिया कार्यक्रम:</em> <strong>1 जुलाई 2015</strong> को प्रधानमंत्री नरेंद्र मोदी द्वारा प्रारंभ; <strong>9 स्तंभों (Pillars)</strong> पर आधारित।
          <br>&bull; <em>डिजिलॉकर (DigiLocker):</em> 2015 में प्रारंभ; प्रत्येक आधार-सत्यापित नागरिक को <strong>1 GB का निःशुल्क सुरक्षित क्लाउड स्पेस</strong> प्रदान करता है। सूचना प्रौद्योगिकी अधिनियम के नियम 9A के तहत डिजिलॉकर में उपलब्ध डिजिटल दस्तावेज मूल भौतिक दस्तावेजों के समान कानूनी मान्यता रखते हैं।
          <br>&bull; <em>उमंग (UMANG):</em> <strong>Unified Mobile Application for New-age Governance</strong>; <strong>नवंबर 2017</strong> में लॉन्च; 1500+ केंद्रीय व राज्य सरकारी सेवाओं (EPFO, पैन, आधार आदि) हेतु एकीकृत एकल मोबाइल ऐप।
          <br>&bull; <em>GeM (गवर्नमेंट ई-मार्केटप्लेस):</em> सरकारी विभागों द्वारा वस्तुओं और सेवाओं की पारदर्शी ऑनलाइन खरीद हेतु <strong>अगस्त 2016</strong> में स्थापित पोर्टल।
          <br>&bull; <em>PRAGATI:</em> <strong>Pro-Active Governance and Timely Implementation</strong> (2015); पीएम की अध्यक्षता में मेगा परियोजनाओं की ऑनलाइन समीक्षा प्रणाली।
          <br>&bull; <em>भारतनेट (BharatNet):</em> देश की सभी <strong>2.5 लाख ग्राम पंचायतों</strong> को ऑप्टिकल फाइबर केबल (OFC) से जोड़कर ग्रामीण ब्रॉडबैंड प्रदान करने की परियोजना।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: UP State Specific E-Governance Portals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Uttar Pradesh State-Specific E-Governance Portals &amp; Citizen Platforms</span>
    <span class="lang-hi">5. उत्तर प्रदेश राज्य-विशिष्ट ई-गवर्नेंस पोर्टल एवं नागरिक मंच</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>UP State E-Governance Portals Fact Sheet:</strong>
          <br>&bull; <em>e-District UP (edistrict.up.gov.in):</em> Centralized district-level delivery platform for 250+ citizen services including digitally signed <strong>Caste Certificate (जाति प्रमाण पत्र), Income Certificate (आय प्रमाण पत्र), Domicile/Residence Certificate (निवास प्रमाण पत्र), and Khatauni land records</strong>.
          <br>&bull; <em>Jansunwai / IGRS UP (Integrated Grievance Redressal System):</em> Flagship citizen grievance redressal portal (jansunwai.up.nic.in) and mobile app; directly monitored by the Chief Minister's Office; facilitates time-bound resolution and escalation of public complaints against administrative departments.
          <br>&bull; <em>e-Sathi UP (esathi.up.gov.in):</em> Direct citizen access portal allowing individuals to apply for government certificates, social welfare schemes, revenue records, and ration cards without visiting CSCs (Common Service Centres).
          <br>&bull; <em>Bhulekh UP (upbhulekh.gov.in):</em> Comprehensive digitized portal for Uttar Pradesh land records; provides real-time access to <strong>Khasra, Khatauni (ROR - Record of Rights), land ownership maps (Bhudnaksha), and digitized 16-digit Unique Land Parcel Identification Number (ULPIN)</strong>.
          <br>&bull; <em>Nivesh Mitra (niveshmitra.up.nic.in):</em> UP's premier <strong>Single Window Clearance System</strong> for industrial entrepreneurs; provides online clearance of over 450+ licenses and NOCs across 35+ departments to boost Ease of Doing Business.
          <br>&bull; <em>Parivahan Sewa (Sarathi &amp; Vahan):</em>
            <br>&nbsp;&nbsp;&bull; <strong>SARATHI:</strong> Citizen portal for online Driving License (DL) applications, learner permits, and driving school records.
            <br>&nbsp;&nbsp;&bull; <strong>VAHAN:</strong> Centralized vehicle registration, road tax payment, and fitness certificate database.
          <br>&bull; <em>UP Abhyudaya Portal:</em> Digital platform delivering free competitive exam coaching (UPSC, UPPSC, UPSSSC, NEET, JEE) to meritorious underprivileged students across all 75 UP districts.
          <br>&bull; <em>UPCOP Citizen Mobile App:</em> Developed by UP Police; enables citizens to lodge online e-FIRs for lost articles, request tenant/servant verifications, event permissions, and report cybercrimes digitally.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश ई-गवर्नेंस पोर्टल महत्वपूर्ण तथ्य:</strong>
          <br>&bull; <em>ई-डिस्ट्रिक्ट यूपी (e-District UP):</em> 250 से अधिक नागरिक सेवाओं का ऑनलाइन वितरण; इसके माध्यम से डिजिटल हस्ताक्षरित <strong>जाति प्रमाण पत्र, आय प्रमाण पत्र, निवास प्रमाण पत्र, एवं खतौनी नकल</strong> जारी किए जाते हैं।
          <br>&bull; <em>जनसुनवाई / आईजीआरएस (IGRS UP):</em> नागरिकों की जन शिकायतों के समयबद्ध निस्तारण हेतु मुख्यमंत्री कार्यालय द्वारा सीधे मॉनिटर किया जाने वाला एकीकृत शिकायत निवारण पोर्टल (jansunwai.up.nic.in)।
          <br>&bull; <em>ई-साथी यूपी (e-Sathi UP):</em> नागरिकों को घर बैठे विभिन्न सरकारी प्रमाण पत्रों एवं समाज कल्याण योजनाओं के लिए सीधे आवेदन करने की सुविधा।
          <br>&bull; <em>भूलेख यूपी (Bhulekh UP):</em> उत्तर प्रदेश का भू-अभिलेख पोर्टल; भूमि का <strong>खसरा, खतौनी (अधिकार अभिलेख), भू-नक्शा और 16 अंकों का यूनिक लैंड कोड (गाटा संख्या)</strong> ऑनलाइन देखने की सुविधा।
          <br>&bull; <em>निवेश मित्र (Nivesh Mitra):</em> यूपी का <strong>सिंगल विंडो क्लीयरेंस सिस्टम</strong>; उद्योगों को 35 से अधिक विभागों से 450+ अनुमतियां व एनओसी एक ही स्थान पर ऑनलाइन प्रदान करने वाला पोर्टल।
          <br>&bull; <em>सारथी एवं वाहन पोर्टल (Parivahan):</em>
            <br>&nbsp;&nbsp;&bull; <strong>सारथी (SARATHI):</strong> ड्राइविंग लाइसेंस (DL) एवं लर्नर लाइसेंस संबंधी सेवाओं का पोर्टल।
            <br>&nbsp;&nbsp;&bull; <strong>वाहन (VAHAN):</strong> मोटर वाहन पंजीकरण (RC), टैक्स एवं फिटनेस प्रमाण पत्र का पोर्टल।
          <br>&bull; <em>मुख्यमंत्री अभ्युदय पोर्टल:</em> राज्य के 75 जनपदों में प्रतियोगी परीक्षाओं (UPSC, UPPSC, UPSSSC आदि) की निःशुल्क कोचिंग हेतु डिजिटल पोर्टल।
          <br>&bull; <em>UPCOP ऐप:</em> उत्तर प्रदेश पुलिस का नागरिक ऐप; खोई वस्तुओं की ई-एफआईआर, किरायेदार सत्यापन एवं चरित्र प्रमाण पत्र हेतु।</span>
      </li>
    </ul>
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
            <span class="lang-en">The core and heart of an Operating System</span>
            <span class="lang-hi">ऑपरेटिंग सिस्टम का मुख्य हृदय / केंद्रीय भाग</span>
          </td>
          <td>
            <span class="lang-en"><strong>Kernel</strong> (remains in RAM during system operation).</span>
            <span class="lang-hi"><strong>कर्नल (Kernel)</strong> (सिस्टम चालू रहने तक रैम में रहता है)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Operating system used for strict real-time deadlines</span>
            <span class="lang-hi">सख्त समय-सीमा पर कार्य करने वाला ऑपरेटिंग सिस्टम</span>
          </td>
          <td>
            <span class="lang-en"><strong>RTOS (Real-Time Operating System)</strong> e.g., VxWorks, RTLinux.</span>
            <span class="lang-hi"><strong>RTOS (रियल-टाइम ओएस)</strong> जैसे VxWorks, RTLinux।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Condition where CPU is trapped in excessive page swapping</span>
            <span class="lang-hi">जब सीपीयू वास्तविक कार्य करने के बजाय केवल पेज बदलने में उलझ जाता है</span>
          </td>
          <td>
            <span class="lang-en"><strong>Thrashing (थ्रैशिंग)</strong>.</span>
            <span class="lang-hi"><strong>थ्रैशिंग (Thrashing)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Maximum single file size limit in FAT32 file system</span>
            <span class="lang-hi">FAT32 फाइल सिस्टम में एकल फाइल का अधिकतम आकार</span>
          </td>
          <td>
            <span class="lang-en"><strong>4 Gigabytes (4 GB)</strong>.</span>
            <span class="lang-hi"><strong>4 GB (गीगाबाइट)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Free cloud storage space allocated per citizen in DigiLocker</span>
            <span class="lang-hi">डिजिलॉकर में प्रत्येक नागरिक को मिलने वाला निःशुल्क क्लाउड स्पेस</span>
          </td>
          <td>
            <span class="lang-en"><strong>1 GB (Gigabyte)</strong>.</span>
            <span class="lang-hi"><strong>1 GB (गीगाबाइट)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Launch date of Digital India Programme</span>
            <span class="lang-hi">डिजिटल इंडिया कार्यक्रम प्रारंभ होने की तिथि</span>
          </td>
          <td>
            <span class="lang-en"><strong>1 July 2015</strong> (based on 9 key pillars).</span>
            <span class="lang-hi"><strong>1 जुलाई 2015</strong> (9 मुख्य स्तंभों पर आधारित)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Full form of UMANG e-governance mobile app</span>
            <span class="lang-hi">उमंग (UMANG) मोबाइल ऐप का पूरा नाम</span>
          </td>
          <td>
            <span class="lang-en"><strong>Unified Mobile Application for New-age Governance</strong> (2017).</span>
            <span class="lang-hi"><strong>Unified Mobile Application for New-age Governance</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Uttar Pradesh single window clearance portal for industries</span>
            <span class="lang-hi">उत्तर प्रदेश में उद्योगों हेतु सिंगल विंडो क्लीयरेंस पोर्टल</span>
          </td>
          <td>
            <span class="lang-en"><strong>Nivesh Mitra (निवेश मित्र)</strong>.</span>
            <span class="lang-hi"><strong>निवेश मित्र (Nivesh Mitra)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Digitized land records portal of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश का ऑनलाइन भू-अभिलेख पोर्टल</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bhulekh UP (upbhulekh.gov.in)</strong>.</span>
            <span class="lang-hi"><strong>भूलेख यूपी (Bhulekh UP)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Standard character limit of posts on X (formerly Twitter)</span>
            <span class="lang-hi">एक्स (ट्विटर) पर सामान्य पोस्ट की अधिकतम कैरेक्टर सीमा</span>
          </td>
          <td>
            <span class="lang-en"><strong>280 characters</strong> (expanded from original 140 in 2017).</span>
            <span class="lang-hi"><strong>280 कैरेक्टर</strong> (2017 में 140 से बढ़ाकर 280 किया गया)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Founder and year of launch for LinkedIn</span>
            <span class="lang-hi">लिंक्डइन के संस्थापक एवं इसकी शुरुआत का वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>Reid Hoffman</strong> (launched in <strong>2002</strong>, professional networking).</span>
            <span class="lang-hi"><strong>रीड हॉफमैन</strong> (वर्ष <strong>2002</strong>, पेशेवर नेटवर्किंग)।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-computer", "operating-system-social-networking-e-governance", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_os_egov_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
