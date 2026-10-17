# Topic 11: Internet and Computer Networks
mm_t11 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Computer Networks, OSI Model &amp; The Internet</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: कंप्यूटर नेटवर्क, OSI मॉडल, टोपोलॉजी एवं इंटरनेट</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • ARPANET to VSNL 1995 • LAN/MAN/WAN • Topologies (Star/Mesh/Bus) • 7-Layer OSI Architecture • Connecting Hardware (Switches/Routers) • BharatNet</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • ARPANET से VSNL 1995 • LAN/MAN/WAN • टोपोलॉजी (स्टार/मेश) • 7-स्तरीय OSI मॉडल • नेटवर्क उपकरण (स्विच/राउटर) • भारतनेट</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-globe"></i>
            <span class="lang-en">Computer Networking &amp; Internet Architecture</span>
            <span class="lang-hi">कंप्यूटर नेटवर्किंग एवं इंटरनेट वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Evolution & Pioneers of the Internet -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-history" style="color: #059669;"></i>
                    <span class="lang-en">1. Network Evolution &amp; Pioneers</span>
                    <span class="lang-hi">1. नेटवर्क का क्रमिक विकास एवं जनक</span>
                </h4>
                <span class="mindmap-node-tag">ARPANET 1969 • VSNL 1995</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Milestones &amp; Key Pioneers</span>
                        <span class="lang-hi">मील के पत्थर एवं प्रमुख व्यक्ति</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>ARPANET</strong> (1969, US DoD 4 Nodes)</span>
                        <span class="mindmap-chip"><strong>Vint Cerf &amp; Bob Kahn</strong> (Fathers of Internet)</span>
                        <span class="mindmap-chip"><strong>TCP/IP Protocol</strong> (1974 Design, Jan 1 1983)</span>
                        <span class="mindmap-chip"><strong>Packet Switching</strong> (Paul Baran &amp; Donald Davies)</span>
                        <span class="mindmap-chip"><strong>ERNET</strong> (1986, India Academic Net)</span>
                        <span class="mindmap-chip"><strong>VSNL</strong> (15 Aug 1995, Public Internet in India)</span>
                        <span class="mindmap-chip"><strong>B.K. Syngal</strong> (Father of Indian Internet)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Global &amp; Indian Historic Breakthroughs</span>
                        <span class="lang-hi">वैश्विक एवं भारतीय ऐतिहासिक उपलब्धियां</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ARPANET (1969):</strong> Advanced Research Projects Agency Network funded by US Department of Defense; world's first operational packet-switching network. First 4 nodes connected: UCLA, Stanford Research Institute (SRI), UC Santa Barbara, and University of Utah. First message "LO" sent on 29 Oct 1969.</span>
                            <span class="lang-hi"><strong>ARPANET (1969):</strong> अमेरिकी रक्षा विभाग द्वारा वित्तपोषित विश्व का प्रथम पैकेट-स्विचिंग नेटवर्क। प्रारंभिक 4 नोड्स: UCLA, स्टैनफोर्ड, सांता बारबरा व यूटा विश्वविद्यालय। 29 अक्टूबर 1969 को पहला संदेश "LO" भेजा गया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Vint Cerf &amp; Bob Kahn:</strong> Co-designed TCP/IP protocols (1973-1974); recognized worldwide as the <strong>"Fathers of the Internet"</strong>. On <strong>1 January 1983</strong> (Flag Day), ARPANET officially standardized on TCP/IP, marking the true birth of modern Internet.</span>
                            <span class="lang-hi"><strong>विंट सर्फ एवं बॉब कान:</strong> TCP/IP प्रोटोकॉल के सह-निर्माता; <strong>"इंटरनेट के पिता"</strong> कहलाते हैं। <strong>1 जनवरी 1983</strong> को ARPANET ने पूर्णतः TCP/IP अपनाया, जिसे इंटरनेट का औपचारिक जन्मदिवस माना जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Internet in India (15 August 1995):</strong> Public commercial Internet launched in India on Independence Day, 15 August 1995 by Videsh Sanchar Nigam Limited (VSNL) led by Chairman B.K. Syngal (Father of Indian Internet). Prior to this, ERNET (1986) linked academic institutions.</span>
                            <span class="lang-hi"><strong>भारत में इंटरनेट का आगमन (15 अगस्त 1995):</strong> स्वतंत्रता दिवस पर विदेश संचार निगम लिमिटेड (VSNL) द्वारा सार्वजनिक इंटरनेट सेवा शुरू की गई; तत्कालीन VSNL प्रमुख बी.के. सिंघल को <em>"भारतीय इंटरनेट का जनक"</em> कहा जाता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Vint Cerf &amp; Bob Kahn are Fathers of the Internet; public Internet in India was launched on 15 August 1995 by VSNL; B.K. Syngal is the Father of Indian Internet!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> विंट सर्फ व बॉब कान इंटरनेट के पिता हैं; भारत में सार्वजनिक इंटरनेट 15 अगस्त 1995 को VSNL द्वारा शुरू हुआ; बी.के. सिंघल भारतीय इंटरनेट के जनक हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Classification by Scale: PAN, LAN, MAN, WAN -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-network-wired" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Geographic Network Scales</span>
                    <span class="lang-hi">2. भौगोलिक विस्तार के आधार पर नेटवर्क</span>
                </h4>
                <span class="mindmap-node-tag">PAN • LAN • MAN • WAN • VPN</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Network Scales &amp; Coverage</span>
                        <span class="lang-hi">नेटवर्क के स्तर एवं प्रसार सीमा</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>PAN</strong> (1-10 meters, Bluetooth 802.15)</span>
                        <span class="mindmap-chip"><strong>LAN</strong> (Up to 1 km, Ethernet 802.3, Wi-Fi)</span>
                        <span class="mindmap-chip"><strong>CAN</strong> (Campus Area, University/Base)</span>
                        <span class="mindmap-chip"><strong>MAN</strong> (Up to 50 km, City Cable/Wi-Fi)</span>
                        <span class="mindmap-chip"><strong>WAN</strong> (Global/Country, The Internet)</span>
                        <span class="mindmap-chip"><strong>VPN</strong> (Virtual Private Encrypted Tunnel)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Technical Characteristics &amp; IEEE Standards</span>
                        <span class="lang-hi">तकनीकी विशेषताएं एवं IEEE मानक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>PAN (Personal Area Network):</strong> Covers small workspace around a single person (1 to 10 meters). Technologies: Bluetooth (IEEE 802.15.1, 2.4 GHz), Zigbee, Wireless USB, connecting smartphone to wireless earbuds or smartwatch.</span>
                            <span class="lang-hi"><strong>PAN (पर्सनल एरिया नेटवर्क):</strong> एकल व्यक्ति के आस-पास का व्यक्तिगत दायरा (1 से 10 मीटर)। ब्लूटूथ (IEEE 802.15.1), स्मार्टवॉच, वायरलेस ईयरबड्स।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>LAN &amp; MAN:</strong> <strong>LAN (Local Area Network):</strong> Covers single room, office floor, or building (up to 1 km); high data rate (100 Mbps - 10 Gbps), low error rate; uses Ethernet cables (IEEE 802.3, Robert Metcalfe 1973) or Wi-Fi (IEEE 802.11). <strong>MAN:</strong> Spans an entire city or metropolitan town (up to 50 km); cable TV distribution or municipal broadband networks.</span>
                            <span class="lang-hi"><strong>LAN एवं MAN:</strong> <strong>LAN:</strong> कमरा, कार्यालय या भवन (1 किमी तक); ईथरनेट (IEEE 802.3) या वाई-फाई (IEEE 802.11); तीव्र गति, निम्न त्रुटि। <strong>MAN:</strong> संपूर्ण शहर (50 किमी तक); केबल टीवी नेटवर्क।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>WAN (Wide Area Network):</strong> Spans countries, continents, or the entire globe; uses telephone lines, fiber-optic submarine cables, and satellite communication links. The Internet is the world's largest public WAN.</span>
                            <span class="lang-hi"><strong>WAN (वाइड एरिया नेटवर्क):</strong> देशों, महाद्वीपों या संपूर्ण विश्व में फैला विशाल नेटवर्क; उपग्रह व समुद्र के नीचे बिछे ऑप्टिकल फाइबर केबल्स पर आधारित। इंटरनेट विश्व का सबसे बड़ा WAN है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ethernet standard is IEEE 802.3; Wi-Fi standard is IEEE 802.11; Bluetooth is IEEE 802.15.1; the Internet is the world's largest WAN!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ईथरनेट का मानक IEEE 802.3 है; वाई-फाई IEEE 802.11 है; ब्लूटूथ IEEE 802.15.1 है; इंटरनेट विश्व का सबसे बड़ा WAN है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Network Topologies & Architectures -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-project-diagram" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Network Topologies</span>
                    <span class="lang-hi">3. नेटवर्क टोपोलॉजी एवं ज्यामितीय विन्यास</span>
                </h4>
                <span class="mindmap-node-tag">Bus • Star • Ring • Mesh</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Topology Types &amp; Fault Tolerance</span>
                        <span class="lang-hi">टोपोलॉजी के प्रकार एवं विश्वसनीयता</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Bus</strong> (Backbone Cable &amp; Terminators)</span>
                        <span class="mindmap-chip"><strong>Star</strong> (Central Hub/Switch, Most Popular)</span>
                        <span class="mindmap-chip"><strong>Ring</strong> (Token Passing, Unidirectional)</span>
                        <span class="mindmap-chip"><strong>Mesh</strong> (Point-to-Point, n(n-1)/2 Links)</span>
                        <span class="mindmap-chip"><strong>Tree</strong> (Hierarchical Star-Bus Combo)</span>
                        <span class="mindmap-chip"><strong>Hybrid</strong> (Combination of 2+ Types)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Topological Comparisons &amp; Formulas</span>
                        <span class="lang-hi">टोपोलॉजी तुलना एवं गणितीय सूत्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bus Topology:</strong> Nodes share a single linear backbone cable with terminators at both ends to absorb signals. Inexpensive and simple, but if central backbone cable snaps, the ENTIRE network collapses.</span>
                            <span class="lang-hi"><strong>बस टोपोलॉजी:</strong> एक मुख्य बैकबोन केबल से सभी नोड्स जुड़े होते हैं तथा दोनों सिरों पर टर्मिनेटर लगे होते हैं। यदि मुख्य बैकबोन तार टूट जाए तो पूरा नेटवर्क ठप हो जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Star Topology:</strong> All network nodes connect directly to a central Hub or Switch via dedicated cables. Most widely deployed LAN topology. If one node's cable fails, others remain unaffected; if the central switch fails, the entire network goes down.</span>
                            <span class="lang-hi"><strong>स्टार टोपोलॉजी:</strong> सभी कंप्यूटर एक केंद्रीय हब या स्विच से जुड़े होते हैं। सर्वाधिक प्रयुक्त। यदि किसी एक कंप्यूटर का तार टूटे तो बाकी चलते रहते हैं; किंतु केंद्रीय स्विच खराब होने पर पूरा नेटवर्क बंद।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mesh Topology (Full Mesh):</strong> Every node connects directly to every other node via dedicated point-to-point physical links. Total physical links required for $n$ nodes = $\frac{n(n-1)}{2}$. Offers absolute maximum fault tolerance, zero traffic collision, but highest cabling cost and port complexity.</span>
                            <span class="lang-hi"><strong>मेश टोपोलॉजी (पूर्ण मेश):</strong> प्रत्येक नोड हर दूसरे नोड से समर्पित तार द्वारा जुड़ा होता है। $n$ नोड्स हेतु आवश्यक तारों की संख्या: $\frac{n(n-1)}{2}$। अत्यधिक विश्वसनीय, ट्रैफिक जाम मुक्त, किंतु सबसे महंगी।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Number of physical links in a Full Mesh network with n nodes is n(n-1)/2; Star topology uses a central Hub/Switch; Bus topology uses Terminators!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> $n$ नोड्स वाली पूर्ण मेश टोपोलॉजी में कुल तारों की संख्या $n(n-1)/2$ होती है; स्टार टोपोलॉजी केंद्रीय हब/स्विच का उपयोग करती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Connecting Hardware & Transmission Media -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-server" style="color: #d97706;"></i>
                    <span class="lang-en">4. Network Hardware &amp; Media</span>
                    <span class="lang-hi">4. नेटवर्क उपकरण एवं संचरण माध्यम</span>
                </h4>
                <span class="mindmap-node-tag">Switch • Router • Fiber TIR</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Hardware Devices &amp; Media Types</span>
                        <span class="lang-hi">हार्डवेयर उपकरण एवं मीडिया प्रकार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Twisted Pair</strong> (Cat6, RJ-45, 100m)</span>
                        <span class="mindmap-chip"><strong>Coaxial Cable</strong> (BNC, Shielded)</span>
                        <span class="mindmap-chip"><strong>Optical Fiber</strong> (TIR, Glass Core)</span>
                        <span class="mindmap-chip"><strong>Repeater</strong> (Layer 1 Signal Regenerator)</span>
                        <span class="mindmap-chip"><strong>Hub</strong> (Layer 1 Broadcast Device)</span>
                        <span class="mindmap-chip"><strong>Switch</strong> (Layer 2 Intelligent Unicast)</span>
                        <span class="mindmap-chip"><strong>Router</strong> (Layer 3 Logical IP Routing)</span>
                        <span class="mindmap-chip"><strong>Gateway</strong> (Protocol Translator)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Device Differences &amp; Fiber Physics</span>
                        <span class="lang-hi">उपकरणों में अंतर एवं ऑप्टिकल फाइबर भौतिकी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Optical Fiber Physics:</strong> Transmits data as pulses of light through a silica glass/plastic core surrounded by cladding with lower refractive index; operates on the principle of <strong>Total Internal Reflection (TIR)</strong>. Provides highest bandwidth, lowest attenuation, and total immunity to Electromagnetic Interference (EMI).</span>
                            <span class="lang-hi"><strong>ऑप्टिकल फाइबर भौतिकी:</strong> डेटा को प्रकाश तरंगों के रूप में भेजता है; <strong>पूर्ण आंतरिक परावर्तन (TIR)</strong> के सिद्धांत पर कार्य करता है। कांच का कोर व क्लैडिंग; विद्युत-चुंबकीय हस्तक्षेप (EMI) से पूर्णतः सुरक्षित व उच्चतम बैंडविड्थ।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hub vs Switch vs Router:</strong> <strong>Hub (Layer 1):</strong> Dumb broadcast device; copies incoming packet to ALL ports indiscriminately; shared collision domain. <strong>Switch (Layer 2):</strong> Intelligent device; inspects destination hardware MAC address and forwards packets ONLY to designated port (Unicast); maintains CAM table. <strong>Router (Layer 3):</strong> Connects different logical networks; forwards packets using IP addresses and routing protocols (OSPF, BGP).</span>
                            <span class="lang-hi"><strong>हब बनाम स्विच बनाम राउटर:</strong> <strong>हब (लेयर 1):</strong> डंब ब्रॉडकास्ट उपकरण; डेटा सभी पोर्ट्स पर अंधाधुंध भेजता है। <strong>स्विच (लेयर 2):</strong> बुद्धिमान उपकरण; MAC पते की जांच कर केवल लक्षित पोर्ट पर डेटा भेजता है (यूनिकास्ट)। <strong>राउटर (लेयर 3):</strong> IP पते के आधार पर विभिन्न नेटवर्कों के बीच पैकेट रूट करता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Optical fiber operates on Total Internal Reflection (TIR); Hub operates at Layer 1 (broadcast); Switch operates at Layer 2 (MAC address unicast); Router operates at Layer 3 (IP address routing)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ऑप्टिकल फाइबर पूर्ण आंतरिक परावर्तन (TIR) पर कार्य करता है; हब लेयर 1 पर; स्विच लेयर 2 (MAC पता) पर; तथा राउटर लेयर 3 (IP पता) पर कार्य करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: The 7-Layer OSI Reference Model -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-layer-group" style="color: #dc2626;"></i>
                    <span class="lang-en">5. The 7-Layer OSI Model</span>
                    <span class="lang-hi">5. 7-स्तरीय OSI संदर्भ मॉडल</span>
                </h4>
                <span class="mindmap-node-tag">ISO 1984 • 7 Layers • PDU</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">The 7 Layers &amp; Data Units (PDUs)</span>
                        <span class="lang-hi">7 परतें एवं डेटा इकाइयाँ (PDU)</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Layer 7: Application</strong> (HTTP, DNS, SMTP)</span>
                        <span class="mindmap-chip"><strong>Layer 6: Presentation</strong> (Encryption, JPEG)</span>
                        <span class="mindmap-chip"><strong>Layer 5: Session</strong> (Dialogue, Checkpoints)</span>
                        <span class="mindmap-chip"><strong>Layer 4: Transport</strong> (TCP/UDP, Segments)</span>
                        <span class="mindmap-chip"><strong>Layer 3: Network</strong> (IP, Routing, Packets)</span>
                        <span class="mindmap-chip"><strong>Layer 2: Data Link</strong> (MAC, Frames, Switch)</span>
                        <span class="mindmap-chip"><strong>Layer 1: Physical</strong> (Bits, Cables, Volts, Hub)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Layer Functions &amp; Data Encapsulation</span>
                        <span class="lang-hi">परतों के कार्य एवं डेटा कैप्सुलेशन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>OSI History &amp; Mnemonic (ISO, 1984):</strong> Open Systems Interconnection model conceptualizes network communication into 7 distinct layers. Mnemonic from Layer 7 to 1: <em>"All People Seem To Need Data Processing"</em>.</span>
                            <span class="lang-hi"><strong>OSI मॉडल (ISO 1984):</strong> नेटवर्किंग को 7 तार्किक परतों में विभाजित करता है। लेयर 7 से 1 याद रखने का सूत्र: <em>"All People Seem To Need Data Processing"</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Data Units (PDUs) per Layer:</strong> Physical Layer handles raw <strong>Bits</strong> -> Data Link Layer organizes bits into <strong>Frames</strong> -> Network Layer routes <strong>Packets</strong> -> Transport Layer segments data into <strong>Segments (TCP)</strong> or <strong>Datagrams (UDP)</strong> -> Upper layers handle user <strong>Data</strong>.</span>
                            <span class="lang-hi"><strong>परतवार डेटा इकाइयाँ (PDU):</strong> फिजिकल लेयर पर <strong>बिट्स (Bits)</strong> -> डेटा लिंक पर <strong>फ्रेम्स (Frames)</strong> -> नेटवर्क पर <strong>पैकेट्स (Packets)</strong> -> ट्रांसपोर्ट पर <strong>सेगमेंट्स (Segments)</strong> -> ऊपरी परतों पर <strong>डेटा</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Core Responsibilities:</strong> <strong>Presentation (Layer 6):</strong> Data translation, compression, and encryption/decryption (SSL/TLS). <strong>Session (Layer 5):</strong> Dialogue control, simplex/duplex management, synchronization checkpoints. <strong>Transport (Layer 4):</strong> End-to-end flow control, error recovery, port addressing.</span>
                            <span class="lang-hi"><strong>मुख्य दायित्व:</strong> <strong>प्रेजेंटेशन (लेयर 6):</strong> डेटा अनुवाद, संपीड़न व एन्क्रिप्शन (SSL/TLS)। <strong>सेशन (लेयर 5):</strong> संवाद नियंत्रण व चेकपॉइंट्स। <strong>ट्रांसपोर्ट (लेयर 4):</strong> एंड-टू-एंड प्रवाह नियंत्रण, त्रुटि सुधार, पोर्ट नंबर।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> OSI has 7 layers; Data Link PDU is Frame; Network PDU is Packet; Transport PDU is Segment; Encryption and compression occur at Layer 6 (Presentation)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> OSI में 7 परतें होती हैं; डेटा लिंक पर PDU 'फ्रेम' तथा नेटवर्क पर 'पैकेट' होता है; एन्क्रिप्शन व कम्प्रेशन लेयर 6 (प्रेजेंटेशन) पर होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: TCP/IP Model & Indian Broadband Initiatives -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-flag" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. TCP/IP &amp; India Broadband</span>
                    <span class="lang-hi">6. TCP/IP मॉडल एवं भारत में ब्रॉडबैंड पहल</span>
                </h4>
                <span class="mindmap-node-tag">4 Layers • BharatNet • NKN</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Model Layers &amp; National Infrastructure</span>
                        <span class="lang-hi">मॉडल की परतें एवं राष्ट्रीय अवसंरचना</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Application Layer</strong> (HTTP, SMTP, DNS)</span>
                        <span class="mindmap-chip"><strong>Transport Layer</strong> (TCP, UDP)</span>
                        <span class="mindmap-chip"><strong>Internet Layer</strong> (IP, ICMP, ARP)</span>
                        <span class="mindmap-chip"><strong>Network Access Layer</strong> (Ethernet, Wi-Fi)</span>
                        <span class="mindmap-chip"><strong>BharatNet</strong> (2.5 Lakh Gram Panchayats)</span>
                        <span class="mindmap-chip"><strong>NKN</strong> (National Knowledge Network)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">TCP/IP Mapping &amp; Rural Optical Fiber Grid</span>
                        <span class="lang-hi">TCP/IP मैपिंग एवं ग्रामीण ऑप्टिकल फाइबर ग्रिड</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>TCP/IP 4-Layer Architecture:</strong> Practical architectural model powering the Internet. Maps to OSI as: Application Layer (OSI 5, 6, 7) -> Transport Layer (OSI 4) -> Internet Layer (OSI 3) -> Network Access / Link Layer (OSI 1, 2).</span>
                            <span class="lang-hi"><strong>TCP/IP 4-स्तरीय वास्तुकला:</strong> इंटरनेट का व्यावहारिक मॉडल। OSI से मैपिंग: एप्लिकेशन लेयर (OSI 5, 6, 7) -> ट्रांसपोर्ट लेयर (OSI 4) -> इंटरनेट लेयर (OSI 3) -> नेटवर्क एक्सेस लेयर (OSI 1, 2)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>BharatNet Project:</strong> World's largest rural optical fiber network initiative, connecting all 2.5 lakh Gram Panchayats in India with high-speed broadband to empower rural e-governance, digital schools, and primary health centers across Uttar Pradesh.</span>
                            <span class="lang-hi"><strong>भारतनेट परियोजना:</strong> देश की 2.5 लाख ग्राम पंचायतों को हाई-स्पीड ऑप्टिकल फाइबर से जोड़ने वाला विश्व का सबसे बड़ा ग्रामीण ब्रॉडबैंड अभियान; उप्र के गांवों में डिजिटल क्रांति का आधार।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Knowledge Network (NKN):</strong> Multi-gigabit pan-India secure optical network connecting over 1,500 research and educational institutions (IIT Kanpur, IIT BHU, Lucknow University) for collaborative research and e-learning.</span>
                            <span class="lang-hi"><strong>राष्ट्रीय ज्ञान नेटवर्क (NKN):</strong> देश के 1,500+ शीर्ष उच्च शिक्षण व अनुसंधान संस्थानों (IIT कानपुर, IIT BHU आदि) को जोड़ने वाला बहु-गीगाबिट क्षमता का हाई-स्पीड नेटवर्क।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> TCP/IP model has 4 layers; BharatNet connects 2.5 lakh Gram Panchayats via optical fiber; NKN connects universities and scientific laboratories!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> TCP/IP मॉडल में 4 परतें होती हैं; भारतनेट 2.5 लाख ग्राम पंचायतों को ऑप्टिकल फाइबर से जोड़ता है; NKN विश्वविद्यालयों को आपस में जोड़ता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
