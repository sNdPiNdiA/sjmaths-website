import os
import re

def build_internet_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Internet History, Network Topologies &amp; Architecture</span>
    <span class="lang-hi">माइंड मैप: इंटरनेट का इतिहास, नेटवर्क टोपोलॉजी एवं वास्तुकला</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[The Internet & Computer Networks] --> B[Evolution & Milestones]
    A --> C[Network Classification by Scale]
    A --> D[Network Topologies]
    A --> E[Network Connecting Hardware]
    A --> F[OSI vs TCP/IP Reference Models]

    B --> B1[ARPANET 1969: First packet switching network DoD]
    B --> B2[Birth of Internet: Jan 1 1983 TCP/IP adoption]
    B --> B3[Fathers of Internet: Vinton Cerf & Bob Kahn]
    B --> B4[India Launch: Aug 15 1995 VSNL by B.K. Syngal]

    C --> C1[PAN: Personal Bluetooth/NFC ~10 meters]
    C --> C2[LAN: Local Ethernet/Wi-Fi single building]
    C --> C3[MAN: Metropolitan Cable TV/City-wide ~50 km]
    C --> C4[WAN: Wide Area Internet/Global fiber & satellite]

    D --> D1[Star: Central Switch/Hub most common in LAN]
    D --> D2[Bus: Single backbone cable with terminators]
    D --> D3[Ring: Token passing unidirectional/FDDI]
    D --> D4[Mesh: Full mesh n n-1 / 2 links max reliability]

    E --> E1[Layer 1: Repeater signal boost, Hub broadcast]
    E --> E2[Layer 2: Switch intelligent MAC, Bridge LAN segment]
    E --> E3[Layer 3: Router packet routing via IP tables]
    E --> E4[Gateway: Protocol translation between dissimilar networks]

    F --> F1[OSI 7 Layers: Physical, DataLink, Network, Transport, Session, Presentation, Application]
    F --> F2[TCP/IP 4 Layers: Network Access, Internet IP, Transport TCP/UDP, Application]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[इंटरनेट एवं कंप्यूटर नेटवर्क] --> B[ऐतिहासिक विकास एवं मील के पत्थर]
    A --> C[भौगोलिक दूरी के आधार पर नेटवर्क]
    A --> D[नेटवर्क टोपोलॉजी संरचनाएं]
    A --> E[नेटवर्किंग हार्डवेयर उपकरण]
    A --> F[OSI एवं TCP/IP संदर्भ मॉडल]

    B --> B1[ARPANET 1969: अमेरिकी रक्षा विभाग का प्रथम पैकेट स्विचिंग]
    B --> B2[इंटरनेट का जन्म: 1 जनवरी 1983 TCP/IP मानक]
    B --> B3[इंटरनेट के जनक: विंटन सर्फ एवं बॉब कान]
    B --> B4[भारत में शुरुआत: 15 अगस्त 1995 VSNL बी.के. सिंघल]

    C --> C1[PAN: व्यक्तिगत ब्लूटूथ/NFC ~10 मीटर दायरा]
    C --> C2[LAN: स्थानीय ईथरनेट/वाई-फाई एक कमरा या भवन]
    C --> C3[MAN: महानगरीय केबल टीवी/शहर व्यापी ~50 किमी]
    C --> C4[WAN: विस्तृत क्षेत्र इंटरनेट/वैश्विक ऑप्टिकल फाइबर]

    D --> D1[स्टार: केंद्रीय स्विच/हब सर्वाधिक लोकप्रिय]
    D --> D2[बस: एकल बैकबोन केबल दोनों सिरों पर टर्मिनेटर]
    D --> D3[रिंग: टोकन पासिंग एकल दिशा/FDDI रिंग]
    D --> D4[मेश: पूर्ण मेश n n-1 / 2 लिंक अधिकतम विश्वसनीयता]

    E --> E1[लेयर 1: रिपीटर सिग्नल प्रवर्धन, हब ब्रॉडकास्ट]
    E --> E2[लेयर 2: स्विच बुद्धिमान MAC टेबल, ब्रिज लैन विभाजन]
    E --> E3[लेयर 3: राउटर IP आधारित सर्वश्रेष्ठ मार्ग चयन]
    E --> E4[गेटवे: भिन्न प्रोटोकॉल नेटवर्क के मध्य अनुवादक]

    F --> F1[OSI 7 परतें: फिजिकल, डेटा लिंक, नेटवर्क, ट्रांसपोर्ट, सेशन, प्रेजेंटेशन, एप्लीकेशन]
    F --> F2[TCP/IP 4 परतें: नेटवर्क एक्सेस, इंटरनेट IP, ट्रांसपोर्ट TCP/UDP, एप्लीकेशन]
    </div>
  </div>
</div>

<!-- Card 2: History & Launch of Internet -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. History, Evolution &amp; Launch of the Internet (Global &amp; India)</span>
    <span class="lang-hi">1. इंटरनेट का इतिहास, क्रमिक विकास एवं भारत में आगमन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>ARPANET (Advanced Research Projects Agency Network):</strong>
          <br>&bull; Commissioned in <strong>1969</strong> by the United States Department of Defense (DoD).
          <br>&bull; The world's first operational network to implement <strong>Packet Switching</strong> technology (invented by Paul Baran and Donald Davies), transmitting data in discrete packets rather than continuous telephone circuits.
          <br>&bull; The first message sent over ARPANET was <em>"LO"</em> (attempting to type "LOGIN" before the system crashed) on October 29, 1969 between UCLA and Stanford University.</span>
        <span class="lang-hi"><strong>ARPANET (अर्पानेट):</strong>
          <br>&bull; वर्ष <strong>1969</strong> में अमेरिकी रक्षा विभाग (DoD) की एजेंसी DARPA द्वारा प्रारंभ।
          <br>&bull; विश्व का प्रथम कार्यरत नेटवर्क जिसमें <strong>पैकेट स्विचिंग (Packet Switching)</strong> तकनीक का प्रयोग किया गया।
          <br>&bull; 29 अक्टूबर 1969 को UCLA और स्टैनफोर्ड के बीच पहला संदेश <em>"LO"</em> भेजा गया था (सिस्टम क्रैश होने से पहले "LOGIN" लिखा जा रहा था)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Official Birth of the Internet &amp; Fathers of Internet:</strong>
          <br>&bull; <strong>January 1, 1983:</strong> Known as the official birth date of the Internet, when ARPANET permanently adopted the <strong>TCP/IP</strong> (Transmission Control Protocol / Internet Protocol) networking standard.
          <br>&bull; <strong>Fathers of the Internet:</strong> <strong>Vinton Gray Cerf</strong> and <strong>Robert Elliot Kahn (Bob Kahn)</strong>, who co-designed the TCP/IP architecture.</span>
        <span class="lang-hi"><strong>इंटरनेट का आधिकारिक जन्म एवं जनक:</strong>
          <br>&bull; <strong>1 जनवरी 1983:</strong> इंटरनेट का आधिकारिक जन्म दिवस माना जाता है, जब ARPANET ने पुराने NCP को त्यागकर <strong>TCP/IP प्रोटोकॉल</strong> को पूर्ण रूप से अपनाया।
          <br>&bull; <strong>इंटरनेट के जनक:</strong> <strong>विंटन जी. सर्फ (Vint Cerf)</strong> एवं <strong>रॉबर्ट ई. कान (Bob Kahn)</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Launch of Public Internet in India:</strong>
          <br>&bull; Public internet services were formally launched in India on <strong>August 15, 1995</strong> by <strong>VSNL (Videsh Sanchar Nigam Limited)</strong> through dial-up gateway services.
          <br>&bull; <strong>Brijendra K. Syngal (B.K. Syngal)</strong>, then chairman of VSNL, is universally recognized as the <strong>"Father of the Internet in India"</strong>.
          <br>&bull; <strong>ERNET (Education and Research Network):</strong> Established in 1986 by the Department of Electronics for academic research institutions (IITs, IISc) prior to commercial launch.</span>
        <span class="lang-hi"><strong>भारत में इंटरनेट का आगमन:</strong>
          <br>&bull; भारत में सार्वजनिक इंटरनेट सेवा का शुभारंभ <strong>15 अगस्त 1995</strong> को <strong>विदेश संचार निगम लिमिटेड (VSNL)</strong> द्वारा 'गेटवे इंटरनेट एक्सेस सर्विस' (GIAS) के रूप में किया गया।
          <br>&bull; VSNL के तत्कालीन अध्यक्ष <strong>बृजेंद्र कुमार सिंघल (बी.के. सिंघल)</strong> को <strong>"भारत में इंटरनेट के जनक"</strong> के रूप में जाना जाता है।
          <br>&bull; भारत में शैक्षणिक व शोध संस्थानों हेतु 1986 में <strong>ERNET</strong> की स्थापना की गई थी।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Network Classifications & Topologies -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Computer Networks: Classification by Scale &amp; Physical Topologies</span>
    <span class="lang-hi">2. कंप्यूटर नेटवर्क: भौगोलिक विस्तार के आधार पर वर्गीकरण एवं टोपोलॉजी</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Network Type</span><span class="lang-hi">नेटवर्क प्रकार</span></th>
          <th><span class="lang-en">Full Form</span><span class="lang-hi">पूर्ण रूप</span></th>
          <th><span class="lang-en">Geographic Coverage</span><span class="lang-hi">भौगोलिक दायरा</span></th>
          <th><span class="lang-en">Speed &amp; Technology</span><span class="lang-hi">गति एवं तकनीक</span></th>
          <th><span class="lang-en">Typical Example</span><span class="lang-hi">विशिष्ट उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>PAN</strong></td>
          <td>Personal Area Network</td>
          <td>Up to 10 meters (Personal workspace)</td>
          <td>Moderate speed, Low power (Bluetooth IEEE 802.15.1, Zigbee, NFC)</td>
          <td>Connecting smartphone to wireless earbuds, smartwatch, or portable speaker</td>
        </tr>
        <tr>
          <td><strong>LAN</strong></td>
          <td>Local Area Network</td>
          <td>Within a single room, office, or building (Up to 1 km)</td>
          <td>Very high speed (100 Mbps to 10 Gbps), High security (Ethernet 802.3, Wi-Fi 802.11)</td>
          <td>Computer lab in college, office local file sharing network</td>
        </tr>
        <tr>
          <td><strong>MAN</strong></td>
          <td>Metropolitan Area Network</td>
          <td>Across an entire city or large town (Up to 50 km)</td>
          <td>High speed, Optical fiber backbone / Coaxial / Microwave links</td>
          <td>City cable TV network, municipal corporation surveillance camera network</td>
        </tr>
        <tr>
          <td><strong>WAN</strong></td>
          <td>Wide Area Network</td>
          <td>Across countries, continents, or the entire globe (Unlimited)</td>
          <td>Variable speed, complex routing (Subsea fiber optic cables, Satellite communication)</td>
          <td>The global <strong>Internet</strong>, Banking ATM inter-bank network</td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Physical Network Topologies (नेटवर्क टोपोलॉजी):</span>
      <span class="lang-hi">नेटवर्क टोपोलॉजी (कंप्यूटरों के जुड़ने की ज्यामितीय व्यवस्था):</span>
    </h4>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Topology</span><span class="lang-hi">टोपोलॉजी</span></th>
          <th><span class="lang-en">Physical Layout</span><span class="lang-hi">भौतिक संरचना</span></th>
          <th><span class="lang-en">Key Advantages</span><span class="lang-hi">प्रमुख लाभ</span></th>
          <th><span class="lang-en">Key Limitations / Formula</span><span class="lang-hi">सीमाएं / सूत्र</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Star Topology</strong></td>
          <td><span class="lang-en">All nodes individually connect to a central hub or switch like spokes on a wheel.</span><span class="lang-hi">सभी कंप्यूटर एक केंद्रीय स्विच या हब से अलग-अलग जुड़े होते हैं।</span></td>
          <td><span class="lang-en">Easy to install and troubleshoot; failure of one cable/node does not affect other nodes. <strong>Most common in modern LANs.</strong></span><span class="lang-hi">आसान स्थापना; एक कंप्यूटर खराब होने पर बाकी नेटवर्क चालू रहता है। वर्तमान लैन में सर्वाधिक लोकप्रिय।</span></td>
          <td><span class="lang-en">If central hub/switch fails, entire network crashes (Single point of failure).</span><span class="lang-hi">यदि केंद्रीय स्विच/हब खराब हो जाए तो पूरा नेटवर्क ठप हो जाता है।</span></td>
        </tr>
        <tr>
          <td><strong>Bus Topology</strong></td>
          <td><span class="lang-en">All devices connect to a single central coaxial cable called the <em>backbone</em> with terminators at both ends.</span><span class="lang-hi">सभी नोड्स एक मुख्य बैकबोन केबल से जुड़े होते हैं; दोनों सिरों पर टर्मिनेटर लगे होते हैं।</span></td>
          <td><span class="lang-en">Requires minimum cable length; low cost; simple for small networks.</span><span class="lang-hi">कम केबल की आवश्यकता; कम लागत; छोटे नेटवर्कों हेतु सरल।</span></td>
          <td><span class="lang-en">Break in main backbone brings entire network down; packet collisions (CSMA/CD).</span><span class="lang-hi">मुख्य केबल कटने पर पूरा नेटवर्क बंद; डेटा टकराव (Collisions)।</span></td>
        </tr>
        <tr>
          <td><strong>Ring Topology</strong></td>
          <td><span class="lang-en">Every device has exactly two neighbors, forming a closed continuous circular loop.</span><span class="lang-hi">प्रत्येक कंप्यूटर अपने दोनों ओर के दो नोड्स से जुड़कर एक बंद गोलाकार लूप बनाता है।</span></td>
          <td><span class="lang-en">No packet collisions because data travels in one direction using an electronic <em>Token</em> (Token Ring IEEE 802.5).</span><span class="lang-hi">टोकन पासिंग के कारण डेटा टकराव नहीं होता; समान अवसर मिलता है।</span></td>
          <td><span class="lang-en">Failure of any single workstation breaks the entire ring (unless dual ring like FDDI is used).</span><span class="lang-hi">किसी एक नोड के खराब होने पर पूरा लूप टूट जाता है।</span></td>
        </tr>
        <tr>
          <td><strong>Mesh Topology</strong></td>
          <td><span class="lang-en">Every node has a dedicated point-to-point link to every other node in the network (Full Mesh).</span><span class="lang-hi">नेटवर्क का प्रत्येक कंप्यूटर अन्य सभी कंप्यूटरों से सीधे जुड़ा होता है।</span></td>
          <td><span class="lang-en"><strong>Highest reliability and fault tolerance</strong>; no traffic congestion; robust privacy and security.</span><span class="lang-hi"><strong>सर्वोच्च विश्वसनीयता व सुरक्षा</strong>; कोई नोड खराब होने पर भी वैकल्पिक मार्ग उपलब्ध।</span></td>
          <td><span class="lang-en">Extremely expensive and complex cabling. Total links required: $\frac{n(n-1)}{2}$ links for $n$ nodes. Total I/O ports per device = $n-1$.</span><span class="lang-hi">अत्यधिक महंगा; $n$ नोड्स हेतु $\frac{n(n-1)}{2}$ केबलों की आवश्यकता होती है।</span></td>
        </tr>
        <tr>
          <td><strong>Tree / Hybrid</strong></td>
          <td><span class="lang-en">Tree is hierarchical star networks connected to a bus backbone; Hybrid combines two or more topologies.</span><span class="lang-hi">ट्री में कई स्टार नेटवर्क एक बस बैकबोन से जुड़े होते हैं; हाइब्रिड दो या अधिक का मिश्रण है।</span></td>
          <td><span class="lang-en">Scalable; widely used in large university campuses and corporate enterprises.</span><span class="lang-hi">आसानी से विस्तार योग्य; बड़े परिसरों में प्रयुक्त।</span></td>
          <td><span class="lang-en">Complex maintenance and costly installation.</span><span class="lang-hi">रखरखाव कठिन एवं महंगा।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Network Hardware & OSI Reference Model -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Network Hardware Devices &amp; The 7 Layers of OSI Model</span>
    <span class="lang-hi">3. नेटवर्किंग हार्डवेयर उपकरण एवं OSI मॉडल की 7 परतें</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Network Hardware Hierarchy:</strong>
          <br>&bull; <strong>Repeater (Physical Layer 1):</strong> Electronic device that receives a weak/attenuated signal, cleans and regenerates it at full strength over long distances.
          <br>&bull; <strong>Hub (Physical Layer 1):</strong> Multiport repeater. Non-intelligent device that simply broadcasts incoming packets to <em>all connected ports</em> (broadcast storm, half-duplex).
          <br>&bull; <strong>Bridge (Data Link Layer 2):</strong> Connects and filters traffic between two separate LAN segments based on <strong>MAC addresses</strong>.
          <br>&bull; <strong>Switch (Data Link Layer 2):</strong> Intelligent multiport bridge. Maintains a dynamic <strong>MAC Address Table (CAM Table)</strong> to forward packets exclusively to the intended destination port (unicast, full-duplex, no collisions).
          <br>&bull; <strong>Router (Network Layer 3):</strong> Intelligent device that connects multiple different networks (e.g., LAN to WAN). Operates on <strong>IP addresses</strong> and uses routing algorithms (OSPF, BGP) to find the fastest path for packets.
          <br>&bull; <strong>Gateway (All Layers 1-7):</strong> Protocol converter that connects two fundamentally dissimilar networks (e.g., AppleTalk to TCP/IP, or internal legacy mainframe to Internet).
          <br>&bull; <strong>Modem (Modulator-Demodulator):</strong> Converts digital signals of a computer into analog signals for transmission across telephone/coaxial lines (Modulation) and vice versa (Demodulation).</span>
        <span class="lang-hi"><strong>नेटवर्किंग हार्डवेयर उपकरणों का वर्गीकरण:</strong>
          <br>&bull; <strong>रिपीटर (लेयर 1):</strong> कमजोर पड़ चुके सिग्नलों को पुनः प्रवर्धित (Regenerate) कर दूरी बढ़ाता है।
          <br>&bull; <strong>हब (लेयर 1):</strong> डंब/अज्ञानी उपकरण; आने वाले डेटा को सभी जुड़े हुए कंप्यूटरों पर <em>ब्रॉडकास्ट</em> कर देता है।
          <br>&bull; <strong>ब्रिज (लेयर 2):</strong> दो लैन खंडों को जोड़ता है और <strong>MAC पते</strong> के आधार पर डेटा को फिल्टर करता है।
          <br>&bull; <strong>स्विच (लेयर 2):</strong> बुद्धिमान उपकरण; <strong>MAC एड्रेस टेबल</strong> रखता है और डेटा को केवल लक्षित कंप्यूटर (यूनिकास्ट) तक भेजता है।
          <br>&bull; <strong>राउटर (लेयर 3):</strong> दो भिन्न नेटवर्कों (जैसे LAN और WAN) को जोड़ता है; <strong>IP पते</strong> के आधार पर पैकेट का सर्वोत्तम मार्ग तय करता है।
          <br>&bull; <strong>गेटवे:</strong> दो बिल्कुल भिन्न प्रोटोकॉल वाले नेटवर्कों के मध्य अनुवादक (Translator) का कार्य करता है।
          <br>&bull; <strong>मॉडेम:</strong> डिजिटल सिग्नल को एनालॉग (मॉड्यूलेशन) एवं एनालॉग को डिजिटल (डिमॉड्यूलेशन) में परिवर्तित करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>OSI 7-Layer Reference Model (Open Systems Interconnection - ISO, 1984):</strong>
          <br>&bull; Mnemonic from top to bottom: <strong>A</strong>ll <strong>P</strong>eople <strong>S</strong>eem <strong>T</strong>o <strong>N</strong>eed <strong>D</strong>ata <strong>P</strong>rocessing
          <br>&nbsp;&nbsp;<strong>Layer 7: Application Layer</strong> &rarr; User interface, HTTP, FTP, SMTP, DNS, Telnet.
          <br>&nbsp;&nbsp;<strong>Layer 6: Presentation Layer</strong> &rarr; Data translation, Encryption/Decryption (SSL), Compression (JPEG, MP3).
          <br>&nbsp;&nbsp;<strong>Layer 5: Session Layer</strong> &rarr; Dialogue control, session establishment, checkpoints, RPC.
          <br>&nbsp;&nbsp;<strong>Layer 4: Transport Layer</strong> &rarr; End-to-end reliability, Flow &amp; Error control, Port numbers (TCP, UDP). Data unit: <em>Segment</em>.
          <br>&nbsp;&nbsp;<strong>Layer 3: Network Layer</strong> &rarr; Logical routing, Path determination, IP addresses (IPv4, IPv6, ICMP). Data unit: <em>Packet</em>.
          <br>&nbsp;&nbsp;<strong>Layer 2: Data Link Layer</strong> &rarr; Physical framing, MAC addressing, Error detection (CRC), Switch, NIC. Data unit: <em>Frame</em>.
          <br>&nbsp;&nbsp;<strong>Layer 1: Physical Layer</strong> &rarr; Transmission of raw bits over physical media (cables, radio waves, voltage). Data unit: <em>Bit</em>.</span>
        <span class="lang-hi"><strong>OSI मॉडल की 7 परतें (ISO द्वारा 1984 में विकसित):</strong>
          <br>&bull; नीचे से ऊपर की ओर क्रम: 1. फिजिकल &rarr; 2. डेटा लिंक &rarr; 3. नेटवर्क &rarr; 4. ट्रांसपोर्ट &rarr; 5. सेशन &rarr; 6. प्रेजेंटेशन &rarr; 7. एप्लीकेशन।
          <br>&bull; <strong>लेयर 7 (एप्लीकेशन):</strong> उपयोगकर्ता इंटरफेस (HTTP, FTP, SMTP, DNS)।
          <br>&bull; <strong>लेयर 6 (प्रेजेंटेशन):</strong> डेटा अनुवाद, एन्क्रिप्शन (SSL), कम्प्रेशन।
          <br>&bull; <strong>लेयर 5 (सेशन):</strong> संचार सत्र की स्थापना, प्रबंधन व समाप्ति।
          <br>&bull; <strong>लेयर 4 (ट्रांसपोर्ट):</strong> एंड-टू-एंड डेटा ट्रांसफर, पोर्ट एड्रेसिंग (TCP, UDP) [इकाई: सेगमेंट]।
          <br>&bull; <strong>लेयर 3 (नेटवर्क):</strong> लॉजिकल एड्रेसिंग, रूटिंग (IP, राउटर) [इकाई: पैकेट]।
          <br>&bull; <strong>लेयर 2 (डेटा लिंक):</strong> फिजिकल एड्रेसिंग (MAC), स्विच, ब्रिज [इकाई: फ्रेम]।
          <br>&bull; <strong>लेयर 1 (फिजिकल):</strong> कच्चे बिट्स (0 और 1) का भौतिक तारों/तरंगों में संचरण [इकाई: बिट]।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Father of the Internet</span><span class="lang-hi">इंटरनेट के जनक</span></td>
          <td><span class="lang-en"><strong>Vinton G. Cerf</strong> and <strong>Robert E. Kahn</strong> (co-designers of TCP/IP).</span><span class="lang-hi"><strong>विंटन सर्फ</strong> एवं <strong>बॉब कान</strong> (TCP/IP के निर्माता)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Date of commercial internet launch in India</span><span class="lang-hi">भारत में सार्वजनिक इंटरनेट प्रारंभ होने की तिथि</span></td>
          <td><span class="lang-en"><strong>15 August 1995</strong> by VSNL (headed by B.K. Syngal).</span><span class="lang-hi"><strong>15 अगस्त 1995</strong> (VSNL द्वारा, बी.के. सिंघल के नेतृत्व में)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First computer network in the world</span><span class="lang-hi">विश्व का प्रथम कंप्यूटर नेटवर्क</span></td>
          <td><span class="lang-en"><strong>ARPANET</strong> (1969, US Department of Defense).</span><span class="lang-hi"><strong>ARPANET</strong> (1969, अमेरिकी रक्षा विभाग)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Number of cables needed in a Full Mesh topology of $n$ nodes</span><span class="lang-hi">$n$ नोड्स वाले पूर्ण मेश नेटवर्क में केबलों की संख्या</span></td>
          <td><span class="lang-en">$\frac{n(n-1)}{2}$ dedicated physical links.</span><span class="lang-hi">$\frac{n(n-1)}{2}$ लिंक (सर्वोच्च विश्वसनीयता)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Network topology where all nodes connect to a single central switch</span><span class="lang-hi">सभी कंप्यूटर केंद्रीय स्विच से जुड़े होने वाली टोपोलॉजी</span></td>
          <td><span class="lang-en"><strong>Star Topology</strong> (most commonly deployed in modern LANs).</span><span class="lang-hi"><strong>स्टार टोपोलॉजी</strong> (सर्वाधिक प्रचलित लैन टोपोलॉजी)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Layer of OSI model responsible for routing and logical addressing</span><span class="lang-hi">राउटिंग और लॉजिकल एड्रेसिंग हेतु उत्तरदायी OSI परत</span></td>
          <td><span class="lang-en"><strong>Layer 3 - Network Layer</strong> (uses IP packets).</span><span class="lang-hi"><strong>लेयर 3 - नेटवर्क लेयर</strong> (IP पैकेट आधारित)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Data unit name at the Transport Layer of OSI model</span><span class="lang-hi">OSI की ट्रांसपोर्ट लेयर पर डेटा इकाई का नाम</span></td>
          <td><span class="lang-en"><strong>Segment</strong> (TCP) or <strong>Datagram</strong> (UDP).</span><span class="lang-hi"><strong>सेगमेंट (Segment)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Intelligent device operating at Data Link Layer using MAC addresses</span><span class="lang-hi">डेटा लिंक लेयर पर MAC पते पर कार्य करने वाला उपकरण</span></td>
          <td><span class="lang-en"><strong>Network Switch</strong>.</span><span class="lang-hi"><strong>स्विच (Switch)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Device used to connect two fundamentally dissimilar network protocols</span><span class="lang-hi">दो भिन्न प्रोटोकॉल नेटवर्कों को जोड़ने वाला उपकरण</span></td>
          <td><span class="lang-en"><strong>Gateway</strong> (प्रोटोकॉल कनवर्टर).</span><span class="lang-hi"><strong>गेटवे (Gateway)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Standard protocol suite powering the global internet</span><span class="lang-hi">वैश्विक इंटरनेट को संचालित करने वाला मुख्य प्रोटोकॉल सूट</span></td>
          <td><span class="lang-en"><strong>TCP/IP</strong> (Transmission Control Protocol / Internet Protocol).</span><span class="lang-hi"><strong>TCP/IP</strong> (ट्रांसमिशन कंट्रोल प्रोटोकॉल / इंटरनेट प्रोटोकॉल)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_www_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: World Wide Web Architecture, Protocols &amp; Web Technologies</span>
    <span class="lang-hi">माइंड मैप: वर्ल्ड वाइड वेब वास्तुकला, प्रोटोकॉल एवं वेब प्रौद्योगिकियां</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[World Wide Web WWW] --> B[Origins & Pioneers]
    A --> C[Three Pillars of WWW]
    A --> D[URL Structure & Addressing]
    A --> E[HTTP/HTTPS & Status Codes]
    A --> F[Browsers vs Search Engines]
    A --> G[Web 1.0 to Web 3.0 Evolution]

    B --> B1[Inventor: Tim Berners-Lee March 1989 CERN]
    B --> B2[First Web Browser: WorldWideWeb / Nexus 1990]
    B --> B3[First Website: info.cern.ch August 6 1991]
    B --> B4[W3C: World Wide Web Consortium founded 1994]

    C --> C1[HTML: HyperText Markup Language Content Structure]
    C --> C2[HTTP: HyperText Transfer Protocol Communication]
    C --> C3[URL: Uniform Resource Locator Global Addressing]

    D --> D1[Protocol: http://, https:// Port 80/443]
    D --> D2[Domain & TLD: Subdomain, Second Level, Top Level .com, .in]
    D --> D3[Path, Query & Anchor: Directory path, Parameters, Hash tag]

    E --> E1[HTTP Methods: GET retrieve, POST submit, PUT, DELETE]
    E --> E2[Status Codes: 200 OK, 301 Redirect, 404 Not Found, 500 Server Error]
    E --> E3[HTTPS: SSL/TLS Encrypted handshake, port 443]

    F --> F1[Browsers: Mosaic 1993, Netscape, Chrome V8, Firefox, Safari]
    F --> F2[Components: Rendering Engine Blink/Gecko, Cache, Cookies]
    F --> F3[Search Engines: Archie 1990 first, Google 1998 PageRank, Bing]

    G --> G1[Web 1.0 1990s: Static, Read-Only, Personal homepages]
    G --> G2[Web 2.0 2004+: Dynamic, Read-Write, Social, AJAX, User Content]
    G --> G3[Web 3.0 Present: Semantic Web, Decentralized, Blockchain, AI]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[वर्ल्ड वाइड वेब WWW] --> B[उत्पत्ति एवं आविष्कारक]
    A --> C[WWW के तीन आधार स्तंभ]
    A --> D[URL संरचना एवं वेब एड्रेसिंग]
    A --> E[HTTP/HTTPS एवं स्टेटस कोड]
    A --> F[वेब ब्राउज़र बनाम सर्च इंजन]
    A --> G[Web 1.0 से Web 3.0 का विकास]

    B --> B1[आविष्कारक: टिम बर्नर्स-ली मार्च 1989 CERN स्विट्जरलैंड]
    B --> B2[पहला वेब ब्राउज़र: WorldWideWeb / नेक्सस 1990]
    B --> B3[पहली वेबसाइट: info.cern.ch 6 अगस्त 1991]
    B --> B4[W3C: वर्ल्ड वाइड वेब कंसोर्टियम स्थापना 1994]

    C --> C1[HTML: हाइपरटेक्स्ट मार्कअप लैंग्वेज संरचना हेतु]
    C --> C2[HTTP: हाइपरटेक्स्ट ट्रांसफर प्रोटोकॉल संचार हेतु]
    C --> C3[URL: यूनिफॉर्म रिसोर्स लोकेटर वैश्विक पते हेतु]

    D --> D1[प्रोटोकॉल: http://, https:// पोर्ट 80/443]
    D --> D2[डोमेन एवं TLD: सबडोमेन, मुख्य डोमेन, टॉप लेवल .com, .in]
    D --> D3[पाथ, क्वेरी व एंकर: फाइल पाथ, पैरामीटर्स, हैश टैग]

    E --> E1[HTTP विधियाँ: GET डेटा प्राप्ति, POST डेटा जमा, PUT, DELETE]
    E --> E2[स्टेटस कोड: 200 सफल, 301 स्थायी पुनर्निर्देशन, 404 अनुपलब्ध, 500 एरर]
    E --> E3[HTTPS: SSL/TLS एन्क्रिप्टेड सुरक्षित संचार पोर्ट 443]

    F --> F1[ब्राउज़र: मोज़ेक 1993, नेटस्केप, क्रोम V8, फ़ायरफ़ॉक्स, सफ़ारी]
    F --> F2[घटक: रेंडरिंग इंजन, कुकीज सत्र डेटा, कैश मेमोरी]
    F --> F3[सर्च इंजन: आर्ची 1990 प्रथम, गूगल 1998 पेजरैंक, बिंग]

    G --> G1[Web 1.0 1990 का दशक: स्थिर (Static), केवल पठनीय (Read-Only)]
    G --> G2[Web 2.0 2004+: गतिशील (Dynamic), सोशल मीडिया, उपयोगकर्ता सामग्री]
    G --> G3[Web 3.0 वर्तमान: सिमेंटिक वेब, विकेंद्रीकृत, ब्लॉकचेन, AI]
    </div>
  </div>
</div>

<!-- Card 2: Invention & Foundational Pillars -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Origins of WWW &amp; Difference Between Internet and Web</span>
    <span class="lang-hi">1. WWW का उद्भव एवं इंटरनेट और वेब के बीच अंतर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Invention of the World Wide Web:</strong>
          <br>&bull; Invented in <strong>March 1989</strong> by British scientist <strong>Sir Timothy John Berners-Lee (Tim Berners-Lee)</strong> while working at <strong>CERN</strong> (European Organization for Nuclear Research in Geneva, Switzerland).
          <br>&bull; Designed to allow scientists around the world to easily share automated research papers via hyperlinked documents.
          <br>&bull; Developed the first web browser &amp; editor named <strong>WorldWideWeb</strong> (later renamed <em>Nexus</em> to avoid confusion with the web itself) on a <strong>NeXT Computer</strong> workstation in 1990.
          <br>&bull; <strong>First Website:</strong> <code>http://info.cern.ch</code> went live publicly on <strong>August 6, 1991</strong>.
          <br>&bull; <strong>W3C (World Wide Web Consortium):</strong> Founded in <strong>1994</strong> by Tim Berners-Lee at MIT to maintain open standards for the Web.</span>
        <span class="lang-hi"><strong>वर्ल्ड वाइड वेब का आविष्कार:</strong>
          <br>&bull; <strong>मार्च 1989</strong> में ब्रिटिश वैज्ञानिक <strong>सर टिम बर्नर्स-ली</strong> द्वारा <strong>CERN</strong> (जिनेवा, स्विट्जरलैंड) में आविष्कार किया गया।
          <br>&bull; उद्देश्य: विश्व भर के वैज्ञानिकों के बीच हाइपरलिंक्ड दस्तावेजों द्वारा शोध पत्रों का आदान-प्रदान सरल बनाना।
          <br>&bull; उन्होंने 1990 में <em>NeXT कंप्यूटर</em> पर पहला वेब ब्राउज़र व संपादक <strong>WorldWideWeb</strong> (बाद में नाम <em>Nexus</em>) बनाया।
          <br>&bull; <strong>विश्व की पहली वेबसाइट:</strong> <code>http://info.cern.ch</code> <strong>6 अगस्त 1991</strong> को लाइव हुई थी।
          <br>&bull; <strong>W3C (वर्ल्ड वाइड वेब कंसोर्टियम):</strong> वेब मानकों के नियमन हेतु 1994 में टिम बर्नर्स-ली द्वारा स्थापित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Internet vs World Wide Web (Critical Distinction):</strong>
          <br>&bull; <strong>The Internet:</strong> The physical, worldwide global network of computers, servers, cables, and routers connected via the TCP/IP protocol (the physical highway).
          <br>&bull; <strong>The World Wide Web (WWW):</strong> An information service and collection of multimedia webpages running <em>on top of the Internet</em> using the HTTP protocol (the traffic and cars traveling on the highway).
          <br>&bull; Other services running on the Internet besides WWW include Email (SMTP/IMAP), File Transfer (FTP), Remote Access (SSH/Telnet), and VoIP.</span>
        <span class="lang-hi"><strong>इंटरनेट बनाम वर्ल्ड वाइड वेब (महत्वपूर्ण अंतर):</strong>
          <br>&bull; <strong>इंटरनेट:</strong> दुनिया भर के कंप्यूटरों, तारों, सबमरीन केबलों और राउटर्स का विशाल <em>भौतिक ढांचा (हार्डवेयर नेटवर्क)</em> है (मानो एक राष्ट्रीय राजमार्ग)।
          <br>&bull; <strong>वर्ल्ड वाइड वेब (WWW):</strong> इंटरनेट के ऊपर चलने वाली एक <em>सूचना प्रणाली (सर्विस)</em> है, जिसमें हाइपरलिंक्ड वेब पेज होते हैं (मानो राजमार्ग पर चलने वाले वाहन)।
          <br>&bull; इंटरनेट पर WWW के अलावा ईमेल (SMTP), फाइल ट्रांसफर (FTP), ऑनलाइन गेमिंग आदि सेवाएं भी चलती हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>The Three Core Architectural Pillars of the Web:</strong>
          <br>&bull; <strong>1. HTML (HyperText Markup Language):</strong> The standard markup language used to structure web pages and their content (text, images, hyperlinks).
          <br>&bull; <strong>2. HTTP/HTTPS (HyperText Transfer Protocol):</strong> The application-layer communication protocol used to transfer HTML documents and media between client browsers and web servers.
          <br>&bull; <strong>3. URL (Uniform Resource Locator):</strong> The unique global address used to locate any resource on the Internet.</span>
        <span class="lang-hi"><strong>वेब के तीन आधार स्तंभ:</strong>
          <br>&bull; <strong>1. HTML (हाइपरटेक्स्ट मार्कअप लैंग्वेज):</strong> वेब पेजों की संरचना और सामग्री (टेक्स्ट, चित्र, लिंक) तैयार करने वाली भाषा।
          <br>&bull; <strong>2. HTTP/HTTPS:</strong> क्लाइंट (ब्राउज़र) और वेब सर्वर के बीच वेब पेजों के आदान-प्रदान का संचार प्रोटोकॉल।
          <br>&bull; <strong>3. URL (यूनिफॉर्म रिसोर्स लोकेटर):</strong> इंटरनेट पर किसी भी वेब पेज या फाइल का विशिष्ट वैश्विक पता।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: URL Structure & Anatomy -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. URL Structure, Domain Names &amp; TLDs</span>
    <span class="lang-hi">2. URL संरचना, डोमेन नेम प्रणाली एवं टॉप लेवल डोमेन (TLD)</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en">Anatomy of a complete URL: <code>https://www.sjmaths.com:443/upsssc-computer/index.html?topic=ai#theory</code></span>
      <span class="lang-hi">एक संपूर्ण URL की विस्तृत संरचना: <code>https://www.sjmaths.com:443/upsssc-computer/index.html?topic=ai#theory</code></span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">URL Component</span><span class="lang-hi">URL घटक</span></th>
          <th><span class="lang-en">Example Value</span><span class="lang-hi">उदाहरण मान</span></th>
          <th><span class="lang-en">Technical Role &amp; Purpose</span><span class="lang-hi">तकनीकी कार्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Protocol / Scheme</strong></td>
          <td><code>https://</code></td>
          <td><span class="lang-en">Specifies how data is transferred. <code>http://</code> (port 80) or <code>https://</code> (encrypted port 443).</span><span class="lang-hi">संचार का नियम; HTTPS में SSL/TLS एन्क्रिप्शन होता है।</span></td>
        </tr>
        <tr>
          <td><strong>Subdomain</strong></td>
          <td><code>www.</code></td>
          <td><span class="lang-en">Sub-division of the domain indicating the service (e.g., <code>www</code>, <code>mail</code>, <code>blog</code>).</span><span class="lang-hi">मुख्य डोमेन का उप-भाग जो विशिष्ट सर्वर या सेवा इंगित करता है।</span></td>
        </tr>
        <tr>
          <td><strong>Domain Name</strong></td>
          <td><code>sjmaths</code></td>
          <td><span class="lang-en">Human-friendly Second-Level Domain (SLD) registered with a domain registrar.</span><span class="lang-hi">वेबसाइट का मुख्य पहचान नाम।</span></td>
        </tr>
        <tr>
          <td><strong>Top-Level Domain (TLD)</strong></td>
          <td><code>.com</code></td>
          <td><span class="lang-en">The extension following the domain. Categories: Generic TLDs (gTLD) and Country-Code TLDs (ccTLD).</span><span class="lang-hi">डोमेन के अंत में लगा प्रत्यय (.com, .org, .gov, .in)।</span></td>
        </tr>
        <tr>
          <td><strong>Port Number</strong></td>
          <td><code>:443</code></td>
          <td><span class="lang-en">Virtual port endpoint. Defaults to 80 for HTTP and 443 for HTTPS (usually omitted in browser).</span><span class="lang-hi">वर्चुअल पोर्ट संख्या (HTTP हेतु 80, HTTPS हेतु 443)।</span></td>
        </tr>
        <tr>
          <td><strong>Path</strong></td>
          <td><code>/upsssc-computer/index.html</code></td>
          <td><span class="lang-en">Exact folder directory path and filename on the web server.</span><span class="lang-hi">सर्वर पर फाइल या फोल्डर का वास्तविक मार्ग।</span></td>
        </tr>
        <tr>
          <td><strong>Query String</strong></td>
          <td><code>?topic=ai</code></td>
          <td><span class="lang-en">Parameters passed to the server, introduced by a question mark <code>?</code> with key-value pairs.</span><span class="lang-hi">सर्वर को भेजे जाने वाले चर मान (Key-Value पेयर)।</span></td>
        </tr>
        <tr>
          <td><strong>Anchor / Fragment</strong></td>
          <td><code>#theory</code></td>
          <td><span class="lang-en">Jumps directly to a specific HTML bookmark/element ID on the page, prefixed by <code>#</code>.</span><span class="lang-hi">पेज के किसी विशेष भाग या हेडिंग पर सीधे ले जाने वाला एंकर।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:16px 0 8px; color:var(--primary-dark);">
      <span class="lang-en">Common Top-Level Domains (TLDs):</span>
      <span class="lang-hi">प्रमुख टॉप लेवल डोमेन (TLD):</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Generic TLDs (gTLD):</strong> <code>.com</code> (Commercial), <code>.org</code> (Non-profit Organization), <code>.net</code> (Network infrastructure), <code>.edu</code> (Educational institutions), <code>.gov</code> (Government entities), <code>.mil</code> (US Military).</span>
        <span class="lang-hi"><strong>जेनेरिक TLD:</strong> <code>.com</code> (व्यावसायिक), <code>.org</code> (गैर-लाभकारी संस्था), <code>.edu</code> (शैक्षणिक), <code>.gov</code> (सरकारी संस्थाएं), <code>.net</code> (नेटवर्क)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Country-Code TLDs (ccTLD):</strong> Two-letter country identifiers: <code>.in</code> (India), <code>.us</code> (United States), <code>.uk</code> (United Kingdom), <code>.ca</code> (Canada), <code>.au</code> (Australia).
          <br>&bull; Indian second-level domains: <code>.gov.in</code> (Government of India), <code>.nic.in</code> (National Informatics Centre), <code>.edu.in</code> (Indian universities), <code>.res.in</code> (Research).</span>
        <span class="lang-hi"><strong>कंट्री कोड TLD (ccTLD):</strong> देशों के दो-अक्षरीय कोड: <code>.in</code> (भारत), <code>.uk</code> (ब्रिटेन), <code>.us</code> (अमेरिका)।
          <br>&bull; भारतीय सरकारी डोमेन: <code>.gov.in</code> (भारत सरकार), <code>.nic.in</code> (राष्ट्रीय सूचना विज्ञान केंद्र), <code>.ac.in</code> (अकादमिक संस्थान)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: HTTP/HTTPS & Status Codes -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. HTTP vs HTTPS &amp; Important HTTP Status Codes</span>
    <span class="lang-hi">3. HTTP बनाम HTTPS एवं महत्वपूर्ण HTTP स्टेटस कोड</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Feature</span><span class="lang-hi">विशेषता</span></th>
          <th><span class="lang-en">HTTP</span><span class="lang-hi">HTTP</span></th>
          <th><span class="lang-en">HTTPS</span><span class="lang-hi">HTTPS</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Full Form</span><span class="lang-hi">पूर्ण रूप</span></td>
          <td>HyperText Transfer Protocol</td>
          <td>HyperText Transfer Protocol Secure</td>
        </tr>
        <tr>
          <td><span class="lang-en">Default Port</span><span class="lang-hi">डिफ़ॉल्ट पोर्ट</span></td>
          <td><strong>Port 80</strong></td>
          <td><strong>Port 443</strong></td>
        </tr>
        <tr>
          <td><span class="lang-en">Security / Encryption</span><span class="lang-hi">सुरक्षा व एन्क्रिप्शन</span></td>
          <td><span class="lang-en">Plain text (unencrypted); vulnerable to eavesdropping and Man-in-the-Middle (MitM) attacks.</span><span class="lang-hi">प्लेन टेक्स्ट (असुरक्षित); डेटा को हैक किया जा सकता है।</span></td>
          <td><span class="lang-en">Encrypted with <strong>SSL/TLS</strong> (Secure Sockets Layer / Transport Layer Security); secure padlock icon in address bar.</span><span class="lang-hi"><strong>SSL/TLS</strong> द्वारा एन्क्रिप्टेड; ब्राउज़र में पैडलॉक (ताला) चिन्ह दिखता है।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Essential HTTP Status Codes (Frequently Tested in UPSSSC):</span>
      <span class="lang-hi">प्रमुख HTTP स्टेटस कोड (UPSSSC परीक्षाओं में बार-बार पूछे जाने वाले):</span>
    </h4>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Class &amp; Range</span><span class="lang-hi">श्रेणी एवं परास</span></th>
          <th><span class="lang-en">Status Code</span><span class="lang-hi">कोड</span></th>
          <th><span class="lang-en">Standard Meaning</span><span class="lang-hi">मानक अर्थ</span></th>
          <th><span class="lang-en">Exam Explanation</span><span class="lang-hi">परीक्षा विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1xx (Informational)</strong></td>
          <td>100 Continue</td>
          <td>Informational</td>
          <td><span class="lang-en">Request received and continuing.</span><span class="lang-hi">अनुरोध प्राप्त हुआ, प्रक्रिया जारी है।</span></td>
        </tr>
        <tr>
          <td rowspan="2"><strong>2xx (Success)</strong></td>
          <td><strong>200 OK</strong></td>
          <td>Success</td>
          <td><span class="lang-en">Standard response for successful HTTP requests; webpage delivered correctly.</span><span class="lang-hi">अनुरोध पूरी तरह सफल रहा और वेबपेज लोड हो गया।</span></td>
        </tr>
        <tr>
          <td>201 Created</td>
          <td>Resource Created</td>
          <td><span class="lang-en">New resource successfully created (common after POST).</span><span class="lang-hi">नया संसाधन सफलतापूर्वक सर्वर पर बन गया।</span></td>
        </tr>
        <tr>
          <td rowspan="2"><strong>3xx (Redirection)</strong></td>
          <td><strong>301 Moved Permanently</strong></td>
          <td>Permanent Redirect</td>
          <td><span class="lang-en">Requested URL permanently moved to a new URL; search engines transfer SEO rank.</span><span class="lang-hi">वेब पेज स्थायी रूप से नए URL पर स्थानांतरित हो गया है।</span></td>
        </tr>
        <tr>
          <td>302 Found</td>
          <td>Temporary Redirect</td>
          <td><span class="lang-en">Page temporarily located at a different URL.</span><span class="lang-hi">पेज अस्थायी रूप से किसी अन्य पते पर भेजा गया।</span></td>
        </tr>
        <tr>
          <td rowspan="4"><strong>4xx (Client Error)</strong></td>
          <td><strong>400 Bad Request</strong></td>
          <td>Bad Request</td>
          <td><span class="lang-en">Server cannot process request due to client syntax error.</span><span class="lang-hi">क्लाइंट की ओर से गलत सिंटैक्स या अमान्य अनुरोध।</span></td>
        </tr>
        <tr>
          <td><strong>401 Unauthorized</strong></td>
          <td>Unauthorized</td>
          <td><span class="lang-en">Authentication required (valid login/password missing).</span><span class="lang-hi">प्रमाणीकरण आवश्यक है (लॉगिन/पासवर्ड नहीं दिया गया)।</span></td>
        </tr>
        <tr>
          <td><strong>403 Forbidden</strong></td>
          <td>Forbidden</td>
          <td><span class="lang-en">Client is authenticated but lacks access permissions to the requested resource.</span><span class="lang-hi">उपयोगकर्ता को उस पेज को देखने की अनुमति नहीं है।</span></td>
        </tr>
        <tr>
          <td><strong>404 Not Found</strong></td>
          <td>Not Found</td>
          <td><span class="lang-en"><strong>Most common web error:</strong> Requested webpage or file does not exist on the server.</span><span class="lang-hi"><strong>सर्वाधिक ज्ञात एरर:</strong> अनुरोधित वेब पेज सर्वर पर मौजूद नहीं है।</span></td>
        </tr>
        <tr>
          <td rowspan="3"><strong>5xx (Server Error)</strong></td>
          <td><strong>500 Internal Server Error</strong></td>
          <td>Server Error</td>
          <td><span class="lang-en">Generic error indicating server-side application crashed or encountered an unexpected condition.</span><span class="lang-hi">वेब सर्वर के आंतरिक कोड में अप्रत्याशित खराबी।</span></td>
        </tr>
        <tr>
          <td>502 Bad Gateway</td>
          <td>Bad Gateway</td>
          <td><span class="lang-en">Server acting as gateway received an invalid response from upstream server.</span><span class="lang-hi">गेटवे सर्वर को मुख्य सर्वर से अमान्य उत्तर मिला।</span></td>
        </tr>
        <tr>
          <td><strong>503 Service Unavailable</strong></td>
          <td>Service Unavailable</td>
          <td><span class="lang-en">Server currently unable to handle request due to temporary overloading or maintenance.</span><span class="lang-hi">सर्वर अत्यधिक लोड या मेंटेनेंस के कारण अस्थायी रूप से बंद है।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 5: Web Browsers, Search Engines & Evolution -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Web Browsers, Search Engines &amp; Web 1.0 to Web 3.0</span>
    <span class="lang-hi">4. वेब ब्राउज़र, सर्च इंजन एवं Web 1.0 से Web 3.0 का विकास</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Web Browsers:</strong>
          <br>&bull; Software application used to access, retrieve, and display content from the World Wide Web.
          <br>&bull; <strong>Historic Browsers:</strong> <em>WorldWideWeb</em> (1990, first browser), <em>Mosaic</em> (1993, developed by Marc Andreessen at NCSA; first popular graphical browser that displayed images inline with text), <em>Netscape Navigator</em> (1994), <em>Internet Explorer</em> (1995, Microsoft - officially retired in 2022).
          <br>&bull; <strong>Modern Browsers &amp; Engines:</strong> Google Chrome (Chromium, Blink engine, V8 JS engine), Mozilla Firefox (Gecko engine), Apple Safari (WebKit engine), Microsoft Edge (Chromium based).
          <br>&bull; <strong>Browser Features:</strong>
            <br>&nbsp;&nbsp;&bull; <strong>Cookies:</strong> Small text files created by a web server and stored by browser on user's machine to remember login sessions, shopping carts, and preferences (invented by Lou Montulli in 1994).
            <br>&nbsp;&nbsp;&bull; <strong>Cache:</strong> Temporary storage of web files (HTML, CSS, images) so repeat visits load instantly without redownloading.
            <br>&nbsp;&nbsp;&bull; <strong>Incognito / Private Browsing:</strong> Prevents browser from saving history, cookies, and form data locally, but does NOT make user invisible to ISP or network administrators.</span>
        <span class="lang-hi"><strong>वेब ब्राउज़र:</strong>
          <br>&bull; वर्ल्ड वाइड वेब से सामग्री प्राप्त करने और प्रदर्शित करने वाला एप्लीकेशन सॉफ्टवेयर।
          <br>&bull; <strong>ऐतिहासिक ब्राउज़र:</strong> <em>मोज़ेक (Mosaic - 1993)</em>: मार्क एंड्रीसन द्वारा विकसित पहला लोकप्रिय ग्राफिकल वेब ब्राउज़र जिसमें टेक्स्ट के साथ चित्र दिखते थे।
          <br>&bull; <strong>आधुनिक ब्राउज़र:</strong> गूगल क्रोम (ब्लिंक इंजन, V8 जावास्क्रिप्ट इंजन), मोज़िला फ़ायरफ़ॉक्स (गेको), एप्पल सफारी (वेबकिट), माइक्रोसॉफ्ट एज।
          <br>&bull; <strong>कुकीज़ (Cookies):</strong> सर्वर द्वारा उपयोगकर्ता के कंप्यूटर पर सहेजी जाने वाली छोटी टेक्स्ट फाइलें, जो लॉगिन सत्र व प्राथमिकताएं याद रखती हैं (आविष्कारक: लू मोंटुली, 1994)।
          <br>&bull; <strong>कैश (Cache):</strong> छवियों व फाइलों को स्थानीय रूप से सहेजता है ताकि दोबारा पेज तुरंत खुले।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Search Engines:</strong>
          <br>&bull; Software program that searches for information on the World Wide Web using keywords.
          <br>&bull; <strong>First Search Engine:</strong> <strong>Archie</strong> (created in 1990 by Alan Emtage at McGill University for indexing FTP archives).
          <br>&bull; <strong>Google:</strong> Founded in <strong>1998</strong> by <strong>Larry Page</strong> and <strong>Sergey Brin</strong> at Stanford University; revolutionized search using the <strong>PageRank</strong> algorithm which ranks pages based on number and quality of inbound links.
          <br>&bull; <strong>Three Components of a Search Engine:</strong>
            <br>&nbsp;&nbsp;1. <strong>Web Crawler / Spider (Googlebot):</strong> Automatically traverses links across the web to discover pages.
            <br>&nbsp;&nbsp;2. <strong>Indexer:</strong> Organizes, parses, and catalogs tokens/words into a colossal search database.
            <br>&nbsp;&nbsp;3. <strong>Query Processor / Ranking Algorithm:</strong> Matches user queries to indexed documents and ranks them by relevance.</span>
        <span class="lang-hi"><strong>सर्च इंजन:</strong>
          <br>&bull; कीवर्ड के आधार पर वेब पर सूचनाएं खोजने वाला सॉफ्टवेयर।
          <br>&bull; <strong>पहला सर्च इंजन:</strong> <strong>आर्ची (Archie - 1990)</strong>, जिसे एलन एमटेज ने विकसित किया था।
          <br>&bull; <strong>गूगल (1998):</strong> लैरी पेज और सर्गेई ब्रिन द्वारा स्थापित; <strong>पेजरैंक (PageRank)</strong> एल्गोरिदम पर आधारित।
          <br>&bull; <strong>सर्च इंजन के तीन घटक:</strong>
            <br>&nbsp;&nbsp;1. <strong>वेब क्रॉलर/स्पाइडर (Googlebot):</strong> कड़ियों (Links) का अनुसरण कर नए वेबपेज ढूंढता है।
            <br>&nbsp;&nbsp;2. <strong>इंडेक्सर:</strong> पृष्ठों के शब्दों की एक विशाल अनुक्रमणिका (कैटलॉग) बनाता है।
            <br>&nbsp;&nbsp;3. <strong>रैंकिंग एल्गोरिदम:</strong> प्रासंगिकता के आधार पर परिणाम प्रदर्शित करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Evolution: Web 1.0 vs Web 2.0 vs Web 3.0:</strong>
          <br>&bull; <strong>Web 1.0 (1991 - 2004):</strong> <em>Read-Only Web</em>. Static HTML pages, centralized servers, personal homepages, one-way communication (user was merely a consumer).
          <br>&bull; <strong>Web 2.0 (2004 - Present):</strong> <em>Read-Write / Social Web</em>. Dynamic webpages, user-generated content, blogs, wikis, social media (YouTube, Facebook, Twitter/X), AJAX and mobile apps. Coined by Tim O'Reilly.
          <br>&bull; <strong>Web 3.0 (Future / Emerging):</strong> <em>Read-Write-Execute / Semantic Web</em>. Decentralized web powered by blockchain, smart contracts, decentralized identity (DID), peer-to-peer storage (IPFS), and artificial intelligence.</span>
        <span class="lang-hi"><strong>वेब का विकास: Web 1.0, 2.0 एवं 3.0:</strong>
          <br>&bull; <strong>Web 1.0 (1991-2004):</strong> <em>केवल पठनीय (Read-Only)</em>। स्थिर HTML पेज; उपयोगकर्ता केवल सामग्री पढ़ सकता था।
          <br>&bull; <strong>Web 2.0 (2004 से वर्तमान):</strong> <em>पठन-लेखन/सोशल वेब (Read-Write)</em>। उपयोगकर्ता स्वयं सामग्री बनाता है (यूट्यूब, विकिपीडिया, ब्लॉग, फेसबुक)। टिम ओ'रेली द्वारा प्रचारित।
          <br>&bull; <strong>Web 3.0 (उभरता हुआ):</strong> <em>सिमेंटिक व विकेंद्रीकृत वेब</em>। ब्लॉकचेन, स्मार्ट कॉन्ट्रैक्ट्स, क्रिप्टो, AI और विकेंद्रीकृत डेटा स्वामित्व पर आधारित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Inventor of the World Wide Web (WWW)</span><span class="lang-hi">वर्ल्ड वाइड वेब (WWW) के आविष्कारक</span></td>
          <td><span class="lang-en"><strong>Tim Berners-Lee</strong> (March 1989 at CERN, Switzerland).</span><span class="lang-hi"><strong>टिम बर्नर्स-ली</strong> (मार्च 1989, CERN स्विट्जरलैंड)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First popular graphical web browser</span><span class="lang-hi">पहला लोकप्रिय ग्राफिकल वेब ब्राउज़र</span></td>
          <td><span class="lang-en"><strong>NCSA Mosaic</strong> (developed in 1993 by Marc Andreessen).</span><span class="lang-hi"><strong>मोज़ेक (Mosaic)</strong> (1993, मार्क एंड्रीसन द्वारा)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First internet search engine in history</span><span class="lang-hi">इतिहास का पहला इंटरनेट सर्च इंजन</span></td>
          <td><span class="lang-en"><strong>Archie</strong> (created in 1990 by Alan Emtage).</span><span class="lang-hi"><strong>आर्ची (Archie)</strong> (1990, एलन एमटेज)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default port number for HTTPS secure web traffic</span><span class="lang-hi">सुरक्षित HTTPS संचार का मानक पोर्ट नंबर</span></td>
          <td><span class="lang-en"><strong>Port 443</strong> (HTTP uses Port 80).</span><span class="lang-hi"><strong>पोर्ट 443</strong> (HTTP पोर्ट 80 का उपयोग करता है)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">HTTP status code indicating 'Page Not Found'</span><span class="lang-hi">'पेज नहीं मिला' दर्शाने वाला HTTP स्टेटस कोड</span></td>
          <td><span class="lang-en"><strong>404 Not Found</strong>.</span><span class="lang-hi"><strong>404 Not Found</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">HTTP status code indicating successful request</span><span class="lang-hi">सफल अनुरोध दर्शाने वाला कोड</span></td>
          <td><span class="lang-en"><strong>200 OK</strong>.</span><span class="lang-hi"><strong>200 OK</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Software stored on user machine to remember session state and preferences</span><span class="lang-hi">ब्राउज़र में सत्र व प्राथमिकताएं सहेजने वाली फाइल</span></td>
          <td><span class="lang-en"><strong>Cookies</strong> (invented by Lou Montulli in 1994).</span><span class="lang-hi"><strong>कुकीज़ (Cookies)</strong> (आविष्कारक: लू मोंटुली)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Full form of URL</span><span class="lang-hi">URL का पूर्ण रूप</span></td>
          <td><span class="lang-en"><strong>Uniform Resource Locator</strong>.</span><span class="lang-hi"><strong>यूनिफॉर्म रिसोर्स लोकेटर</strong> (Uniform Resource Locator)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Algorithm developed by Larry Page and Sergey Brin for ranking pages</span><span class="lang-hi">गूगल द्वारा वेब पेजों की रैंकिंग हेतु विकसित एल्गोरिदम</span></td>
          <td><span class="lang-en"><strong>PageRank</strong> Algorithm.</span><span class="lang-hi"><strong>पेजरैंक (PageRank)</strong> एल्गोरिदम।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Organization responsible for maintaining official Web standards</span><span class="lang-hi">वेब मानकों का नियमन करने वाली आधिकारिक संस्था</span></td>
          <td><span class="lang-en"><strong>W3C</strong> (World Wide Web Consortium, founded in 1994).</span><span class="lang-hi"><strong>W3C</strong> (वर्ल्ड वाइड वेब कंसोर्टियम)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_ip_address_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Internet Protocol, IP Addressing (IPv4 vs IPv6) &amp; Supporting Protocols</span>
    <span class="lang-hi">माइंड मैप: इंटरनेट प्रोटोकॉल, IP एड्रेसिंग (IPv4 बनाम IPv6) एवं सहायक प्रोटोकॉल</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[IP Addressing & Protocols] --> B[IPv4 Architecture]
    A --> C[IPv6 Architecture]
    A --> D[Public vs Private vs Special IPs]
    A --> E[Network Protocols: DHCP, DNS, ARP, NAT]
    A --> F[Logical IP vs Physical MAC Address]

    B --> B1[32-bit Address: 4 Octets separated by dots 0-255]
    B --> B2[Total Capacity: 2^32 approx 4.29 billion addresses]
    B --> B3[Classes A to E: Class A /8, Class B /16, Class C /24, D Multicast, E Experimental]

    C --> C1[128-bit Address: 8 groups of 4 hexadecimal digits]
    C --> C2[Total Capacity: 2^128 approx 3.4 x 10^38 undecillion]
    C --> C3[Features: No broadcasts Unicast/Multicast/Anycast, Built-in IPSec, Zero Compression]

    D --> D1[Private RFC 1918: Class A 10.x, Class B 172.16-31.x, Class C 192.168.x]
    D --> D2[Special: Loopback 127.0.0.1 localhost, APIPA 169.254.x.x]

    E --> E1[DHCP DORA: Discover, Offer, Request, Acknowledge port 67/68]
    E --> E2[DNS Port 53: Translates domain name to IP]
    E --> E3[ARP: Resolves IP address to physical MAC address]
    E --> E4[NAT: Translates private LAN IPs to public WAN IP]

    F --> F1[IP Address: 32/128-bit Logical, Network Layer 3, Software configurable]
    F --> F2[MAC Address: 48-bit 6-byte Physical, Data Link Layer 2, Burned in NIC ROM]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[IP एड्रेसिंग एवं प्रोटोकॉल] --> B[IPv4 वास्तुकला]
    A --> C[IPv6 वास्तुकला]
    A --> D[पब्लिक, प्राइवेट एवं विशेष IP पते]
    A --> E[सहायक प्रोटोकॉल: DHCP, DNS, ARP, NAT]
    A --> F[लॉजिकल IP बनाम भौतिक MAC एड्रेस]

    B --> B1[32-बिट एड्रेस: 4 ऑक्टेट डॉट्स द्वारा अलग 0 से 255]
    B --> B2[कुल क्षमता: 2^32 लगभग 4.29 अरब पते]
    B --> B3[क्लास A से E: क्लास A बड़े नेटवर्क, B मध्यम, C छोटे नेटवर्क, D मल्टीकास्ट, E शोध]

    C --> C1[128-बिट एड्रेस: 8 समूह 4 हेक्साडेसिमल अंक कोलन द्वारा अलग]
    C --> C2[कुल क्षमता: 2^128 लगभग 3.4 x 10^38 असीम पते]
    C --> C3[विशेषताएं: ब्रॉडकास्ट समाप्त, इनबिल्ट IPSec सुरक्षा, शून्य संपीड़न नियम]

    D --> D1[प्राइवेट पते: क्लास A 10.x, क्लास B 172.16-31.x, क्लास C 192.168.x]
    D --> D2[विशेष पते: लूपबैक 127.0.0.1 लोकलहोस्ट, APIPA 169.254.x.x]

    E --> E1[DHCP DORA प्रक्रिया: डिस्कवर, ऑफर, रिक्वेस्ट, एक्नॉलेज]
    E --> E2[DNS पोर्ट 53: डोमेन नेम को IP पते में बदलना]
    E --> E3[ARP: IP पते से भौतिक MAC पता खोजना]
    E --> E4[NAT: निजी प्राइवेट IP को सार्वजनिक IP में बदलना]

    F --> F1[IP एड्रेस: 32/128 बिट लॉजिकल, नेटवर्क लेयर 3, विन्यास योग्य]
    F --> F2[MAC एड्रेस: 48 बिट 6 बाइट भौतिक, डेटा लिंक लेयर 2, NIC ROM में दर्ज]
    </div>
  </div>
</div>

<!-- Card 2: IPv4 vs IPv6 Comprehensive Architecture -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. IPv4 vs IPv6 Architecture &amp; Comparative Analysis</span>
    <span class="lang-hi">1. IPv4 बनाम IPv6 वास्तुकला एवं तुलनात्मक विश्लेषण</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en">An <strong>IP Address (Internet Protocol Address)</strong> is a unique numerical label assigned to every device connected to a computer network that uses the Internet Protocol for communication.</span>
      <span class="lang-hi"><strong>IP एड्रेस (इंटरनेट प्रोटोकॉल एड्रेस)</strong> कंप्यूटर नेटवर्क से जुड़े प्रत्येक उपकरण को दिया जाने वाला एक विशिष्ट तार्किक (Logical) संख्यात्मक पता है।</span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Feature</span><span class="lang-hi">विशेषता</span></th>
          <th><span class="lang-en">IPv4 (IP version 4)</span><span class="lang-hi">IPv4</span></th>
          <th><span class="lang-en">IPv6 (IP version 6)</span><span class="lang-hi">IPv6</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Address Size &amp; Bits</span><span class="lang-hi">पते का आकार एवं बिट्स</span></td>
          <td><strong>32 bits</strong> (4 bytes)</td>
          <td><strong>128 bits</strong> (16 bytes)</td>
        </tr>
        <tr>
          <td><span class="lang-en">Format &amp; Notation</span><span class="lang-hi">प्रारूप एवं अंकन</span></td>
          <td><span class="lang-en"><strong>Dotted Decimal notation:</strong> 4 octets (8 bits each) separated by dots. Range: <code>0.0.0.0</code> to <code>255.255.255.255</code>.<br>Example: <code>192.168.1.100</code></span><span class="lang-hi"><strong>डॉटेड डेसिमल:</strong> डॉट्स द्वारा अलग 4 ऑक्टेट (प्रत्येक 8 बिट, मान 0-255)।<br>उदा: <code>192.168.1.100</code></span></td>
          <td><span class="lang-en"><strong>Hexadecimal notation:</strong> 8 groups of 4 hexadecimal digits separated by colons. Range: 0-9 and a-f.<br>Example: <code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code></span><span class="lang-hi"><strong>हेक्साडेसिमल:</strong> कोलन द्वारा अलग 8 समूह (प्रत्येक 16 बिट)।<br>उदा: <code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Total Address Space</span><span class="lang-hi">कुल पतों की संख्या</span></td>
          <td>$2^{32} \approx 4,294,967,296$ (Approx <strong>4.29 billion</strong> addresses - exhausted)</td>
          <td>$2^{128} \approx 3.4 \times 10^{38}$ (Virtually inexhaustible undecillion addresses)</td>
        </tr>
        <tr>
          <td><span class="lang-en">Loopback Address</span><span class="lang-hi">लूपबैक पता</span></td>
          <td><code>127.0.0.1</code> (or entire <code>127.0.0.0/8</code> block)</td>
          <td><code>::1</code> (or <code>0:0:0:0:0:0:0:1</code>)</td>
        </tr>
        <tr>
          <td><span class="lang-en">Communication Types</span><span class="lang-hi">संचार के प्रकार</span></td>
          <td>Unicast, Multicast, <strong>Broadcast</strong></td>
          <td>Unicast, Multicast, <strong>Anycast</strong> (<strong>No Broadcast</strong> in IPv6)</td>
        </tr>
        <tr>
          <td><span class="lang-en">Security</span><span class="lang-hi">सुरक्षा</span></td>
          <td>IPSec is optional / add-on</td>
          <td><strong>IPSec is built-in</strong> and mandatory by design</td>
        </tr>
        <tr>
          <td><span class="lang-en">Zero Compression Rule</span><span class="lang-hi">शून्य संपीड़न नियम</span></td>
          <td>Not applicable</td>
          <td>Consecutive blocks of zeros can be compressed once using double colon <code>::</code> (e.g., <code>2001:db8::1</code>). Leading zeros in a block can be dropped.</td>
        </tr>
        <tr>
          <td><span class="lang-en">Header Size</span><span class="lang-hi">हेडर का आकार</span></td>
          <td>Variable size: 20 to 60 bytes (includes Options)</td>
          <td>Fixed size: <strong>40 bytes</strong> (speeds up routing)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 3: IPv4 Classes & Private Addressing -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. IPv4 Classes, Default Subnet Masks &amp; Private IP Ranges</span>
    <span class="lang-hi">2. IPv4 की क्लास संरचना, डिफ़ॉल्ट सबनेट मास्क एवं प्राइवेट IP परास</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Class</span><span class="lang-hi">क्लास</span></th>
          <th><span class="lang-en">Leading Bits</span><span class="lang-hi">प्रारंभिक बिट्स</span></th>
          <th><span class="lang-en">First Octet Range</span><span class="lang-hi">प्रथम ऑक्टेट परास</span></th>
          <th><span class="lang-en">Default Subnet Mask</span><span class="lang-hi">डिफ़ॉल्ट सबनेट मास्क</span></th>
          <th><span class="lang-en">Target Deployment</span><span class="lang-hi">उपयोग का उद्देश्य</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Class A</strong></td>
          <td><code>0</code></td>
          <td>1 – 126 (127 reserved for loopback)</td>
          <td><code>255.0.0.0</code> (/8)</td>
          <td><span class="lang-en">Very large networks ($2^7 = 126$ networks, ~16.7 million hosts each).</span><span class="lang-hi">अत्यंत बड़े नेटवर्क (सरकारें, विशाल दूरसंचार कंपनियां)।</span></td>
        </tr>
        <tr>
          <td><strong>Class B</strong></td>
          <td><code>10</code></td>
          <td>128 – 191</td>
          <td><code>255.255.0.0</code> (/16)</td>
          <td><span class="lang-en">Medium-sized networks (16,384 networks, 65,534 hosts each).</span><span class="lang-hi">मध्यम आकार के नेटवर्क (विश्वविद्यालय, बड़े उद्यम)।</span></td>
        </tr>
        <tr>
          <td><strong>Class C</strong></td>
          <td><code>110</code></td>
          <td>192 – 223</td>
          <td><code>255.255.255.0</code> (/24)</td>
          <td><span class="lang-en">Small networks (~2.09 million networks, 254 hosts each). <strong>Most common for home/small office LANs.</strong></span><span class="lang-hi">छोटे नेटवर्क (होम वाई-फाई, छोटे कार्यालय; 254 होस्ट प्रति नेटवर्क)।</span></td>
        </tr>
        <tr>
          <td><strong>Class D</strong></td>
          <td><code>1110</code></td>
          <td>224 – 239</td>
          <td>No Subnet Mask</td>
          <td><span class="lang-en">Reserved for <strong>Multicasting</strong> (sending packets to a group of hosts).</span><span class="lang-hi"><strong>मल्टीकास्टिंग</strong> (वीडियो कॉन्फ्रेंसिंग, स्ट्रीमिंग) हेतु आरक्षित।</span></td>
        </tr>
        <tr>
          <td><strong>Class E</strong></td>
          <td><code>1111</code></td>
          <td>240 – 255</td>
          <td>No Subnet Mask</td>
          <td><span class="lang-en">Reserved for <strong>Experimental &amp; Research</strong> purposes.</span><span class="lang-hi"><strong>प्रायोगिक एवं भविष्य के अनुसंधान</strong> हेतु आरक्षित।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Private IP Address Ranges (RFC 1918 - Non-routable on Public Internet):</span>
      <span class="lang-hi">प्राइवेट IP पते (RFC 1918 - इंटरनेट पर सीधे नहीं दिखते):</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Class A Private Range:</strong> <code>10.0.0.0</code> to <code>10.255.255.255</code> (Total $16,777,216$ addresses, CIDR prefix <code>10.0.0.0/8</code>).</span>
        <span class="lang-hi"><strong>क्लास A प्राइवेट परास:</strong> <code>10.0.0.0</code> से <code>10.255.255.255</code> (विशाल कॉर्पोरेट नेटवर्क)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Class B Private Range:</strong> <code>172.16.0.0</code> to <code>172.31.255.255</code> (16 contiguous /16 blocks, CIDR prefix <code>172.16.0.0/12</code>).</span>
        <span class="lang-hi"><strong>क्लास B प्राइवेट परास:</strong> <code>172.16.0.0</code> से <code>172.31.255.255</code> (मध्यम स्तरीय नेटवर्क)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Class C Private Range:</strong> <code>192.168.0.0</code> to <code>192.168.255.255</code> (256 contiguous /24 blocks, CIDR prefix <code>192.168.0.0/16</code>). <strong>Default IP on home Wi-Fi routers (e.g. 192.168.1.1).</strong></span>
        <span class="lang-hi"><strong>क्लास C प्राइवेट परास:</strong> <code>192.168.0.0</code> से <code>192.168.255.255</code> (घरेलू वाई-फाई राउटर का डिफ़ॉल्ट पता जैसे 192.168.1.1)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>APIPA (Automatic Private IP Addressing):</strong> <code>169.254.0.1</code> to <code>169.254.255.254</code> (Subnet mask <code>255.255.0.0</code>). Automatically self-assigned by Windows client when a DHCP server is unreachable.</span>
        <span class="lang-hi"><strong>APIPA (ऑटोमैटिक प्राइवेट IP एड्रेसिंग):</strong> <code>169.254.x.x</code>; जब कंप्यूटर को DHCP सर्वर से IP नहीं मिल पाता, तो विंडोज स्वतः यह पता सेट कर लेता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Essential Supporting Protocols & MAC Address -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Essential Supporting Protocols (DHCP, DNS, ARP, NAT) &amp; MAC Address</span>
    <span class="lang-hi">3. आवश्यक सहायक प्रोटोकॉल (DHCP, DNS, ARP, NAT) एवं MAC एड्रेस</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>DHCP (Dynamic Host Configuration Protocol - Port 67 Server, Port 68 Client):</strong>
          <br>&bull; Automatically assigns dynamic IP addresses, subnet masks, default gateways, and DNS server IPs to devices joining a network.
          <br>&bull; <strong>DORA Process:</strong>
            <br>&nbsp;&nbsp;1. <strong>D - Discover:</strong> Client broadcasts looking for a DHCP server.
            <br>&nbsp;&nbsp;2. <strong>O - Offer:</strong> Server broadcasts offering an available IP address.
            <br>&nbsp;&nbsp;3. <strong>R - Request:</strong> Client formally requests to lease the offered IP.
            <br>&nbsp;&nbsp;4. <strong>A - Acknowledge:</strong> Server acknowledges and confirms the lease duration.</span>
        <span class="lang-hi"><strong>DHCP (डायनेमिक होस्ट कॉन्फ़िगरेशन प्रोटोकॉल):</strong>
          <br>&bull; नेटवर्क से जुड़ने वाले नए कंप्यूटरों को स्वतः डायनेमिक IP पता, सबनेट मास्क व गेटवे प्रदान करता है।
          <br>&bull; <strong>DORA प्रक्रिया:</strong> 1. Discover (खोजना) &rarr; 2. Offer (प्रस्ताव) &rarr; 3. Request (अनुरोध) &rarr; 4. Acknowledge (स्वीकृति)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>DNS (Domain Name System - Port 53 UDP/TCP):</strong>
          <br>&bull; The "Phonebook of the Internet". Translates human-friendly domain names (e.g., <code>sjmaths.com</code>) into machine-readable IP addresses (e.g., <code>104.21.55.12</code>).</span>
        <span class="lang-hi"><strong>DNS (डोमेन नेम सिस्टम):</strong>
          <br>&bull; इंटरनेट की "फोन डायरेक्टरी"। मानव द्वारा पढ़े जाने वाले वेब पते (sjmaths.com) को संख्यात्मक IP पते में बदलता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>ARP (Address Resolution Protocol) &amp; RARP:</strong>
          <br>&bull; <strong>ARP (Layer 2/3):</strong> Resolves a known logical 32-bit IP address into a physical 48-bit <strong>MAC address</strong> so frames can be delivered across a local network.
          <br>&bull; <strong>RARP (Reverse ARP):</strong> Resolves a physical MAC address to obtain an IP address (mostly replaced by DHCP).</span>
        <span class="lang-hi"><strong>ARP (एड्रेस रेजोल्यूशन प्रोटोकॉल) एवं RARP:</strong>
          <br>&bull; <strong>ARP:</strong> ज्ञात IP पते के संगत भौतिक <strong>MAC एड्रेस</strong> का पता लगाता है।
          <br>&bull; <strong>RARP:</strong> भौतिक MAC पते से संबंधित IP पते का पता लगाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>NAT (Network Address Translation):</strong>
          <br>&bull; Implemented on routers and firewalls. Translates multiple private, non-routable IP addresses on a local LAN into a single public, globally routable IP address when sending traffic to the Internet.
          <br>&bull; Major technology that prevented early exhaustion of IPv4 addresses.</span>
        <span class="lang-hi"><strong>NAT (नेटवर्क एड्रेस ट्रांसलेशन):</strong>
          <br>&bull; स्थानीय नेटवर्क (LAN) के कई प्राइवेट IP पतों को इंटरनेट पर केवल एक पब्लिक IP पते के माध्यम से जोड़ता है।
          <br>&bull; इसने IPv4 पतों की कमी को दूर करने में क्रांतिकारी भूमिका निभाई।</span>
      </li>
      <li>
        <span class="lang-en"><strong>IP Address vs MAC Address (Physical vs Logical):</strong>
          <br>&bull; <strong>MAC Address (Media Access Control):</strong> 48-bit (6 bytes) permanent hardware address burned into the Network Interface Card (NIC) ROM. Formatted as 12 hexadecimal digits (e.g., <code>00:1A:2B:3C:4D:5E</code>). First 24 bits are the <em>OUI (Organizationally Unique Identifier)</em> identifying the manufacturer; last 24 bits are device serial.
          <br>&bull; <strong>IP Address:</strong> Logical software address assigned dynamically or statically, changing when moving to different networks.</span>
        <span class="lang-hi"><strong>IP एड्रेस बनाम MAC एड्रेस:</strong>
          <br>&bull; <strong>MAC एड्रेस:</strong> 48-बिट (6 बाइट) का स्थायी भौतिक पता जो नेटवर्क कार्ड (NIC) की ROM में दर्ज होता है (उदा. <code>00:1A:2B:3C:4D:5E</code>)। प्रथम 24 बिट निर्माता कंपनी (OUI) की पहचान होती है।
          <br>&bull; <strong>IP एड्रेस:</strong> लॉजिकल सॉफ्टवेयर पता जो नेटवर्क बदलने पर बदल जाता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Total length of IPv4 address in bits and bytes</span><span class="lang-hi">IPv4 पते की कुल लंबाई (बिट्स एवं बाइट्स)</span></td>
          <td><span class="lang-en"><strong>32 bits</strong> (4 bytes, 4 octets).</span><span class="lang-hi"><strong>32 बिट्स</strong> (4 बाइट्स, 4 ऑक्टेट)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Total length of IPv6 address in bits and bytes</span><span class="lang-hi">IPv6 पते की कुल लंबाई</span></td>
          <td><span class="lang-en"><strong>128 bits</strong> (16 bytes, 8 hexadecimal blocks).</span><span class="lang-hi"><strong>128 बिट्स</strong> (16 बाइट्स)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Reserved loopback testing IP address in IPv4</span><span class="lang-hi">IPv4 में लूपबैक परीक्षण हेतु आरक्षित पता</span></td>
          <td><span class="lang-en"><strong>127.0.0.1</strong> (Localhost).</span><span class="lang-hi"><strong>127.0.0.1</strong> (लोकलहोस्ट)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Loopback address representation in IPv6</span><span class="lang-hi">IPv6 में लूपबैक पते का अंकन</span></td>
          <td><span class="lang-en"><code>::1</code>.</span><span class="lang-hi"><code>::1</code>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Length of a physical hardware MAC address</span><span class="lang-hi">भौतिक MAC एड्रेस की लंबाई</span></td>
          <td><span class="lang-en"><strong>48 bits</strong> (6 bytes, written in 12 hexadecimal characters).</span><span class="lang-hi"><strong>48 बिट्स</strong> (6 बाइट्स, हेक्साडेसिमल में लिखित)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Class of IPv4 used for Multicast streaming</span><span class="lang-hi">मल्टीकास्टिंग हेतु प्रयुक्त IPv4 क्लास</span></td>
          <td><span class="lang-en"><strong>Class D</strong> (Range 224.0.0.0 to 239.255.255.255).</span><span class="lang-hi"><strong>क्लास D</strong> (224 से 239)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol used to automatically lease IP addresses to client devices</span><span class="lang-hi">कंप्यूटर को स्वतः IP पता देने वाला प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>DHCP</strong> (uses 4-step DORA process: Discover, Offer, Request, Acknowledge).</span><span class="lang-hi"><strong>DHCP</strong> (DORA प्रक्रिया द्वारा)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol used to find MAC address from a known IP address</span><span class="lang-hi">IP पते से MAC पता ज्ञात करने वाला प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>ARP</strong> (Address Resolution Protocol).</span><span class="lang-hi"><strong>ARP</strong> (एड्रेस रेजोल्यूशन प्रोटोकॉल)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol used to translate domain names to IP addresses</span><span class="lang-hi">डोमेन नाम को IP पते में अनुवादित करने वाला प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>DNS</strong> (Domain Name System, Port 53).</span><span class="lang-hi"><strong>DNS</strong> (डोमेन नेम सिस्टम, पोर्ट 53)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Type of transmission removed in IPv6</span><span class="lang-hi">IPv6 से हटाई गई ट्रांसमिशन विधि</span></td>
          <td><span class="lang-en"><strong>Broadcast</strong> (IPv6 uses Unicast, Multicast, and Anycast only).</span><span class="lang-hi"><strong>ब्रॉडकास्ट (Broadcast)</strong> (IPv6 में ब्रॉडकास्ट नहीं होता)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_email_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Electronic Mail (E-Mail) Architecture, Protocols &amp; Security</span>
    <span class="lang-hi">माइंड मैप: इलेक्ट्रॉनिक मेल (ईमेल) वास्तुकला, प्रोटोकॉल एवं सुरक्षा</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Electronic Mail E-Mail] --> B[History & Syntax]
    A --> C[Three Core Email Protocols]
    A --> D[Header Fields & Structure]
    A --> E[Operations & Storage Folders]
    A --> F[Government Email & Cyber Security]

    B --> B1[Ray Tomlinson 1971: First ARPANET email & @ symbol]
    B --> B2[Address Syntax: username@domain.extension Case-insensitive]
    B --> B3[Shiva Ayyadurai 1978: Copyrighted EMAIL software]

    C --> C1[SMTP Port 25/465/587: Simple Mail Transfer Pushing/Sending]
    C --> C2[POP3 Port 110/995: Post Office Protocol Downloading Local]
    C --> C3[IMAP4 Port 143/993: Internet Message Access Two-way Sync Server]
    C --> C4[MIME: Multipurpose Internet Mail Extensions Non-text files]

    D --> D1[To: Primary recipients visible to all]
    D --> D2[CC Carbon Copy: Secondary recipients visible to all]
    D --> D3[BCC Blind Carbon Copy: Secret recipients hidden from all]
    D --> D4[Subject, Date, Message-ID, Attachments 25MB limit]

    E --> E1[Inbox: Incoming received messages]
    E --> E2[Drafts: Incomplete auto-saved messages]
    E --> E3[Spam/Junk: Filtered unsolicited commercial bulk mail]
    E --> E4[Trash/Bin: Deleted mail auto-purged after 30 days]

    F --> F1[National: NIC Email @gov.in / @nic.in with Kavach 2FA OTP]
    F --> F2[Threats: Phishing, Email Spoofing, Malicious attachments]
    F --> F3[Defense: SPF, DKIM, DMARC, PGP Encryption]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[इलेक्ट्रॉनिक मेल E-Mail] --> B[इतिहास एवं ईमेल सिंटैक्स]
    A --> C[तीन मुख्य ईमेल प्रोटोकॉल]
    A --> D[ईमेल हेडर फील्ड्स एवं संरचना]
    A --> E[ईमेल संचालन एवं फोल्डर]
    A --> F[सरकारी ईमेल एवं साइबर सुरक्षा]

    B --> B1[रे टॉमलिंसन 1971: पहला अर्पानेट ईमेल एवं @ प्रतीक]
    B --> B2[एड्रेस सिंटैक्स: उपयोगकर्ता_नाम@डोमेन.विस्तार केस-असंवेदनशील]
    B --> B3[शिवा अय्यादुरई 1978: ईमेल सॉफ्टवेयर का कॉपीराइट]

    C --> C1[SMTP पोर्ट 25/465: भेजने हेतु पुश प्रोटोकॉल]
    C --> C2[POP3 पोर्ट 110/995: डाउनलोड कर स्थानीय रूप से सहेजना]
    C --> C3[IMAP4 पोर्ट 143/993: सर्वर पर दो-तरफा सिंक सभी डिवाइस पर]
    C --> C4[MIME: मल्टीमीडिया अटैचमेंट (चित्र, पीडीएफ) भेजने का मानक]

    D --> D1[To: मुख्य प्राप्तकर्ता (सभी को दिखाई देता है)]
    D --> D2[CC कार्बन कॉपी: द्वितीयक प्राप्तकर्ता (सभी को दृश्य)]
    D --> D3[BCC ब्लाइंड कार्बन कॉपी: गुप्त प्राप्तकर्ता (किसी को नहीं दिखता)]
    D --> D4[सब्जेक्ट, अटैचमेंट सीमा 25 MB]

    E --> E1[इनबॉक्स: प्राप्त संदेशों का भंडार]
    E --> E2[ड्राफ्ट: अधूरे स्वतः सहेजे गए संदेश]
    E --> E3[स्पैम: अवांछित बल्क व विज्ञापन मेल]
    E --> E4[ट्रैश: हटाए गए मेल 30 दिन में स्वतः नष्ट]

    F --> F1[सरकारी: NIC ईमेल @gov.in, कवच 2FA OTP सुरक्षा]
    F --> F2[खतरे: फ़िशिंग, स्पूफिंग, फर्जी अटैचमेंट]
    F --> F3[सुरक्षा: SPF, DKIM, DMARC डिजिटल हस्ताक्षर]
    </div>
  </div>
</div>

<!-- Card 2: History & Address Syntax -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. History of Email &amp; Syntax of an Email Address</span>
    <span class="lang-hi">1. ईमेल का इतिहास एवं ईमेल पते की संरचना (Syntax)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Invention of Email:</strong>
          <br>&bull; In <strong>1971</strong>, American computer programmer <strong>Ray Tomlinson</strong> sent the world's first network email over ARPANET between two side-by-side PDP-10 computers.
          <br>&bull; Tomlinson introduced the <strong>"@" (at the rate) symbol</strong> to separate the recipient's user name from the host machine name (e.g., <code>tomlinson@bbn-tenexa</code>).
          <br>&bull; Indian-American <strong>V.A. Shiva Ayyadurai</strong> created an electronic interoffice mail system called "EMAIL" in 1978 and obtained the US copyright for it in 1982.</span>
        <span class="lang-hi"><strong>ईमेल का आविष्कार:</strong>
          <br>&bull; वर्ष <strong>1971</strong> में अमेरिकी प्रोग्रामर <strong>रे टॉमलिंसन (Ray Tomlinson)</strong> ने ARPANET पर पहला नेटवर्क ईमेल भेजा।
          <br>&bull; उन्होंने उपयोगकर्ता के नाम और होस्ट कंप्यूटर के नाम को अलग करने के लिए <strong>"@" (एट द रेट) चिन्ह</strong> का चयन किया। इन्हें <strong>"ईमेल का जनक"</strong> माना जाता है।
          <br>&bull; भारतीय मूल के <strong>वी.ए. शिवा अय्यादुरई</strong> ने 1978 में कार्यालयी संचार हेतु 'EMAIL' सॉफ्टवेयर विकसित कर 1982 में कॉपीराइट प्राप्त किया था।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Standard Email Address Anatomy:</strong>
          <br>&bull; General format: <code>username@domain.extension</code> (e.g., <code>sjmaths.help@gmail.com</code>).
          <br>&bull; <strong>1. Username (Local Part):</strong> Identifies the specific user mailbox on the mail server. Maximum 64 characters. Can contain letters, digits, and specific symbols (<code>.</code>, <code>_</code>, <code>-</code>).
          <br>&bull; <strong>2. "@" Separator:</strong> Mandatory delimiter separating username and domain. An email address must contain exactly one "@" symbol.
          <br>&bull; <strong>3. Domain Name:</strong> The web address of the mail service provider (e.g., <code>gmail.com</code>, <code>outlook.com</code>, <code>gov.in</code>).
          <br>&bull; <strong>Critical Rules:</strong> Email addresses are <strong>case-insensitive</strong> (<code>User@domain.com</code> is identical to <code>user@domain.com</code>). Email addresses <strong>cannot contain spaces</strong>.</span>
        <span class="lang-hi"><strong>ईमेल पते की प्रामाणिक संरचना:</strong>
          <br>&bull; सामान्य प्रारूप: <code>उपयोगकर्ता_नाम@डोमेन_नाम.विस्तार</code> (जैसे <code>candidate@gmail.com</code>)।
          <br>&bull; <strong>1. यूजरनेम (स्थानीय भाग):</strong> मेल सर्वर पर उपयोगकर्ता के इनबॉक्स की पहचान।
          <br>&bull; <strong>2. "@" विभाजक:</strong> यूजरनेम और डोमेन को अलग करने वाला अनिवार्य चिन्ह (पूरे पते में ठीक एक '@' होना चाहिए)।
          <br>&bull; <strong>3. डोमेन नेम:</strong> सेवा प्रदाता कंपनी का नाम (जैसे gmail, yahoo, outlook, nic)।
          <br>&bull; <strong>नियम:</strong> ईमेल पते <strong>केस-असंवेदनशील (Case-insensitive)</strong> होते हैं (बड़े या छोटे अक्षरों का भेद नहीं होता)। ईमेल पते में <strong>खाली स्थान (Space) की अनुमति नहीं होती</strong>।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: The Three Core Email Protocols -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The Three Core Email Protocols: SMTP, POP3 &amp; IMAP4</span>
    <span class="lang-hi">2. तीन मुख्य ईमेल प्रोटोकॉल: SMTP, POP3 एवं IMAP4</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Protocol</span><span class="lang-hi">प्रोटोकॉल</span></th>
          <th><span class="lang-en">Full Form</span><span class="lang-hi">पूर्ण रूप</span></th>
          <th><span class="lang-en">Standard Ports</span><span class="lang-hi">मानक पोर्ट्स</span></th>
          <th><span class="lang-en">Role &amp; Operation</span><span class="lang-hi">कार्य एवं संचालन</span></th>
          <th><span class="lang-en">Multi-Device Sync</span><span class="lang-hi">मल्टी-डिवाइस सिंक</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>SMTP</strong></td>
          <td>Simple Mail Transfer Protocol</td>
          <td><strong>Port 25</strong> (unencrypted), <strong>Port 465</strong> (SSL/TLS), <strong>Port 587</strong> (modern submission)</td>
          <td><span class="lang-en"><strong>Push Protocol:</strong> Used exclusively for <strong>sending/uploading</strong> emails from client to server and between mail transfer agents (MTAs).</span><span class="lang-hi"><strong>पुश प्रोटोकॉल:</strong> केवल ईमेल <strong>भेजने (Send करने)</strong> के लिए प्रयुक्त होता है (क्लाइंट से सर्वर तथा सर्वर से सर्वर)।</span></td>
          <td>N/A (Sending only)</td>
        </tr>
        <tr>
          <td><strong>POP3</strong></td>
          <td>Post Office Protocol version 3</td>
          <td><strong>Port 110</strong> (unencrypted), <strong>Port 995</strong> (SSL/TLS)</td>
          <td><span class="lang-en"><strong>Pull/Download Protocol:</strong> Downloads emails from the mail server to the local computer client and by default <strong>deletes them from the server</strong>. Designed for single-device offline reading.</span><span class="lang-hi"><strong>डाउनलोड प्रोटोकॉल:</strong> सर्वर से ईमेल को स्थानीय कंप्यूटर पर डाउनलोड करता है और डिफ़ॉल्ट रूप से <strong>सर्वर से डिलीट कर देता है</strong> (ऑफ़लाइन पढ़ने हेतु)।</span></td>
          <td><span class="lang-en">No (Single device only)</span><span class="lang-hi">नहीं (केवल एक डिवाइस)</span></td>
        </tr>
        <tr>
          <td><strong>IMAP4</strong></td>
          <td>Internet Message Access Protocol version 4</td>
          <td><strong>Port 143</strong> (unencrypted), <strong>Port 993</strong> (SSL/TLS)</td>
          <td><span class="lang-en"><strong>Two-way Synchronization Protocol:</strong> Keeps emails stored permanently on the cloud mail server. Any action (read, delete, move to folder) is <strong>synchronized instantaneously across all connected devices</strong> (phone, tablet, PC).</span><span class="lang-hi"><strong>दो-तरफा सिंक्रोनाइज़ेशन:</strong> ईमेल सर्वर पर सुरक्षित रहते हैं। किसी भी डिवाइस पर किया गया बदलाव (पढ़ना, डिलीट करना) <strong>सभी डिवाइसों पर स्वतः अपडेट</strong> हो जाता है।</span></td>
          <td><span class="lang-en"><strong>Yes</strong> (Full multi-device cloud sync)</span><span class="lang-hi"><strong>हाँ</strong> (आधुनिक ईमेल का मानक)</span></td>
        </tr>
      </tbody>
    </table>
    <div style="margin-top:16px; padding:12px 16px; background:var(--primary-light); border-left:4px solid var(--primary); border-radius:6px;">
      <span class="lang-en"><strong>MIME (Multipurpose Internet Mail Extensions):</strong> Original SMTP was strictly limited to 7-bit ASCII plain English text. MIME extends email capability to support non-ASCII text, international languages (Hindi Devanagari), and multimedia file attachments (images, audio, video, PDFs, DOCX).</span>
      <span class="lang-hi"><strong>MIME (मल्टीपर्पस इंटरनेट मेल एक्सटेंशन):</strong> मूल SMTP केवल साधारण अंग्रेजी टेक्स्ट (7-बिट ASCII) भेज सकता था। MIME तकनीक ने ईमेल में भारतीय भाषाओं, चित्रों, ऑडियो, वीडियो और फाइलों (PDF आदि) को अटैचमेंट के रूप में भेजने को संभव बनाया।</span>
    </div>
  </div>
</div>

<!-- Card 4: Email Fields, Structure & Operations -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Email Header Fields (To, CC, BCC) &amp; Storage Folders</span>
    <span class="lang-hi">3. ईमेल हेडर फील्ड्स (To, CC, BCC) एवं स्टोरेज फोल्डर</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Header Field</span><span class="lang-hi">फील्ड</span></th>
          <th><span class="lang-en">Full Form &amp; Meaning</span><span class="lang-hi">पूर्ण रूप एवं अर्थ</span></th>
          <th><span class="lang-en">Recipient Visibility</span><span class="lang-hi">दृश्यता (Visibility)</span></th>
          <th><span class="lang-en">Exam Tested Purpose</span><span class="lang-hi">परीक्षा उपयोगी उद्देश्य</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>To</strong></td>
          <td>Primary Recipient</td>
          <td><span class="lang-en">Visible to <strong>ALL</strong> recipients.</span><span class="lang-hi"><strong>सभी</strong> प्राप्तकर्ताओं को दिखाई देता है।</span></td>
          <td><span class="lang-en">The person(s) directly expected to read and take action on the message.</span><span class="lang-hi">वह मुख्य व्यक्ति जिससे उत्तर या कार्रवाई अपेक्षित है।</span></td>
        </tr>
        <tr>
          <td><strong>CC</strong></td>
          <td><strong>Carbon Copy</strong></td>
          <td><span class="lang-en">Visible to <strong>ALL</strong> recipients (To, other CCs, and BCCs).</span><span class="lang-hi"><strong>सभी</strong> को दिखाई देता है।</span></td>
          <td><span class="lang-en">Secondary recipients kept informed for reference (FYI - For Your Information).</span><span class="lang-hi">सूचना हेतु शामिल किए गए अन्य लोग (कार्बन कॉपी)।</span></td>
        </tr>
        <tr>
          <td><strong>BCC</strong></td>
          <td><strong>Blind Carbon Copy</strong></td>
          <td><span class="lang-en"><strong>COMPLETELY HIDDEN</strong> from To, CC, and other BCC recipients. Only sender knows who was BCC'd.</span><span class="lang-hi"><strong>पूरी तरह गुप्त</strong>; To, CC या अन्य किसी BCC प्राप्तकर्ता को नहीं दिखता।</span></td>
          <td><span class="lang-en">Used to protect recipient privacy in mass mailings and prevent spam harvesting.</span><span class="lang-hi">गोपनीयता बनाए रखने तथा सैकड़ों लोगों को एक साथ बिना पहचान उजागर किए मेल भेजने हेतु।</span></td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">Standard Email Storage Folders &amp; Attachment Rules:</span>
      <span class="lang-hi">मानक ईमेल फोल्डर एवं अटैचमेंट नियम:</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Inbox (इनबॉक्स):</strong> Default repository for all newly received incoming emails.</span>
        <span class="lang-hi"><strong>इनबॉक्स:</strong> आने वाले सभी नए ईमेल संदेशों का मुख्य संग्रह फोल्डर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Drafts (ड्राफ्ट):</strong> Automatically stores unfinished or composed emails that have not yet been sent.</span>
        <span class="lang-hi"><strong>ड्राफ्ट:</strong> वे संदेश जो लिखे गए हैं परंतु अभी भेजे नहीं गए हैं (स्वतः सहेजे जाते हैं)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Spam / Junk (स्पैम):</strong> Repository for unsolicited bulk commercial messages, suspicious emails, or phishing attempts automatically filtered by security heuristics.</span>
        <span class="lang-hi"><strong>स्पैम / जंक:</strong> अवांछित, फर्जी या विज्ञापन वाले मेल जिन्हें फिल्टर द्वारा अलग कर दिया जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Trash / Bin (ट्रैश / बिन):</strong> Holds deleted emails. In modern webmail services like Gmail, deleted emails are automatically and permanently purged after <strong>30 days</strong>.</span>
        <span class="lang-hi"><strong>ट्रैश / रीसायकल बिन:</strong> हटाए गए ईमेल; अधिकांश सेवाओं (जैसे जीमेल) में <strong>30 दिन बाद</strong> स्वतः हमेशा के लिए नष्ट हो जाते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Attachment Limits:</strong> Standard webmail services (Gmail, Outlook) enforce an attachment limit of <strong>25 MB</strong> per email. Files exceeding this size must be shared via cloud links (Google Drive, OneDrive). Executable files (<code>.exe</code>, <code>.bat</code>, <code>.vbs</code>) are blocked for security.</span>
        <span class="lang-hi"><strong>अटैचमेंट सीमा:</strong> जीमेल पर एक बार में अधिकतम <strong>25 MB</strong> की फाइल अटैच की जा सकती है। इससे बड़ी फाइलें गूगल ड्राइव लिंक द्वारा भेजी जाती हैं। सुरक्षा कारणों से <code>.exe</code> फाइलें प्रतिबंधित होती हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Government Email & Cyber Threats -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Government Email System (NIC) &amp; Email Cyber Threats</span>
    <span class="lang-hi">4. सरकारी ईमेल प्रणाली (NIC) एवं ईमेल साइबर सुरक्षा खतरे</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>National Informatics Centre (NIC) Government Email:</strong>
          <br>&bull; Official secure messaging service provided to Indian central and state government officials with domain extensions <code>@gov.in</code> and <code>@nic.in</code>.
          <br>&bull; <strong>Kavach App:</strong> Mandatory Two-Factor Authentication (2FA) application providing time-based one-time passwords (TOTP) to prevent unauthorized access.
          <br>&bull; Hosted in secured National Data Centres (NDCs) located at Delhi, Pune, Bhubaneswar, and Hyderabad.</span>
        <span class="lang-hi"><strong>राष्ट्रीय सूचना विज्ञान केंद्र (NIC) सरकारी ईमेल:</strong>
          <br>&bull; भारत सरकार एवं राज्य सरकारों (उत्तर प्रदेश सहित) के अधिकारियों हेतु आधिकारिक सुरक्षित ईमेल (डोमेन: <code>@gov.in</code> एवं <code>@nic.in</code>)।
          <br>&bull; <strong>कवच (Kavach) ऐप:</strong> दो-चरणीय प्रमाणीकरण (2FA) सुरक्षा ऐप, जो लॉगिन के समय सुरक्षित OTP प्रदान करता है।
          <br>&bull; राष्ट्रीय डेटा केंद्रों (दिल्ली, पुणे, भुवनेश्वर, हैदराबाद) में होस्टेड।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Major Email Security Threats:</strong>
          <br>&bull; <strong>Phishing (फिशिंग):</strong> Fraudulent emails masquerading as reputable institutions (banks, government portals) to trick users into revealing sensitive data like passwords and credit card numbers.
          <br>&bull; <strong>Email Spoofing (स्पूफिंग):</strong> Forging the email header 'From' address so that the email appears to originate from someone other than the actual source.
          <br>&bull; <strong>Email Security Protocols:</strong> <strong>SPF</strong> (Sender Policy Framework), <strong>DKIM</strong> (DomainKeys Identified Mail - cryptographic signature), and <strong>DMARC</strong> work together to block spoofed and phishing emails.</span>
        <span class="lang-hi"><strong>ईमेल सुरक्षा के प्रमुख खतरे:</strong>
          <br>&bull; <strong>फ़िशिंग (Phishing):</strong> बैंकों या सरकारी संस्थाओं के नाम से फर्जी मेल भेजकर पासवर्ड या ओटीपी चुराना।
          <br>&bull; <strong>ईमेल स्पूफिंग (Spoofing):</strong> सेंडर (From) पते को फर्जी बनाकर ऐसा दिखाना कि मेल किसी विश्वस्त अधिकारी ने भेजा है।
          <br>&bull; <strong>सुरक्षा मानक:</strong> <strong>SPF</strong>, <strong>DKIM</strong> और <strong>DMARC</strong> तकनीकें फर्जी मेल की रोकथाम करती हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: One-Liner Exam Facts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Key One-Liner Exam Facts (UPSSSC Computer Special)</span>
    <span class="lang-hi">महत्वपूर्ण वन-लाइनर परीक्षा तथ्य (UPSSSC कंप्यूटर विशेष)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Exam Question Topic</span><span class="lang-hi">परीक्षा प्रश्न विषय</span></th>
          <th><span class="lang-en">Core Exam Fact &amp; Details</span><span class="lang-hi">महत्वपूर्ण तथ्य एवं विवरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Father of Email and originator of the '@' symbol</span><span class="lang-hi">ईमेल के जनक एवं '@' चिन्ह के प्रणेता</span></td>
          <td><span class="lang-en"><strong>Ray Tomlinson</strong> (1971, over ARPANET).</span><span class="lang-hi"><strong>रे टॉमलिंसन</strong> (1971, ARPANET पर)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol used specifically for sending/transferring outgoing emails</span><span class="lang-hi">ईमेल भेजने (Send) हेतु प्रयुक्त प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>SMTP</strong> (Simple Mail Transfer Protocol, Port 25/465/587).</span><span class="lang-hi"><strong>SMTP</strong> (सिंपल मेल ट्रांसफर प्रोटोकॉल)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol that downloads emails to PC and deletes from server</span><span class="lang-hi">सर्वर से मेल डाउनलोड कर डिलीट करने वाला प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>POP3</strong> (Post Office Protocol version 3, Port 110/995).</span><span class="lang-hi"><strong>POP3</strong> (पोस्ट ऑफिस प्रोटोकॉल)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol that enables real-time synchronization across all devices</span><span class="lang-hi">सभी डिवाइसों पर रीयल-टाइम मेल सिंक करने वाला प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>IMAP4</strong> (Internet Message Access Protocol, Port 143/993).</span><span class="lang-hi"><strong>IMAP4</strong> (इंटरनेट मैसेज एक्सेस प्रोटोकॉल)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Header field used to hide recipient email addresses from others</span><span class="lang-hi">अन्य प्राप्तकर्ताओं से पते छिपाने वाली हेडर फील्ड</span></td>
          <td><span class="lang-en"><strong>BCC</strong> (Blind Carbon Copy).</span><span class="lang-hi"><strong>BCC</strong> (ब्लाइंड कार्बन कॉपी)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Standard attachment file size limit in Gmail</span><span class="lang-hi">जीमेल में अटैचमेंट की अधिकतम फाइल सीमा</span></td>
          <td><span class="lang-en"><strong>25 MB</strong>.</span><span class="lang-hi"><strong>25 MB</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Number of days deleted emails remain in Trash before permanent purge</span><span class="lang-hi">ट्रैश में हटाए गए मेल कितने दिन तक सुरक्षित रहते हैं</span></td>
          <td><span class="lang-en"><strong>30 days</strong>.</span><span class="lang-hi"><strong>30 दिन</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Protocol standard that enables non-text multimedia email attachments</span><span class="lang-hi">मल्टीमीडिया फाइल अटैचमेंट को संभव बनाने वाला मानक</span></td>
          <td><span class="lang-en"><strong>MIME</strong> (Multipurpose Internet Mail Extensions).</span><span class="lang-hi"><strong>MIME</strong> (मल्टीपर्पस इंटरनेट मेल एक्सटेंशन)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Authentication mobile app mandated for accessing NIC government emails</span><span class="lang-hi">NIC सरकारी ईमेल लॉगिन हेतु अनिवार्य 2FA ऐप</span></td>
          <td><span class="lang-en"><strong>Kavach</strong> (कवच ऐप).</span><span class="lang-hi"><strong>कवच (Kavach)</strong> ऐप।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Term for fraudulent emails attempting to steal passwords and financial data</span><span class="lang-hi">पासवर्ड चुराने हेतु भेजे जाने वाले फर्जी मेल</span></td>
          <td><span class="lang-en"><strong>Phishing</strong> (फिशिंग).</span><span class="lang-hi"><strong>फिशिंग (Phishing)</strong>।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def enrich_file(rel_path, theory_html):
    target_file = os.path.join("upsssc-computer", rel_path, "index.html")
    if not os.path.exists(target_file):
        print(f"Error: {target_file} not found")
        return False

    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print(f"ERROR: Could not locate tab-theory boundary in {target_file}!")
        return False

    updated_html = html[:match.start()] + theory_html.strip() + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file}")
    return True

def main():
    enrich_file("internet", build_internet_theory_html())
    enrich_file("world-wide-web-www", build_www_theory_html())
    enrich_file("internet-protocol-ip-address", build_ip_address_theory_html())
    enrich_file("creation-of-e-mail-id-and-use-operation-of-e-mail", build_email_theory_html())

if __name__ == "__main__":
    main()
