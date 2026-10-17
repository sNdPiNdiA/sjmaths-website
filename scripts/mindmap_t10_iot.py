# Topic 10: Internet of Things
mm_t10 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Internet of Things (IoT) Architecture &amp; Protocols</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: इंटरनेट ऑफ थिंग्स (IoT) 4-स्तरीय वास्तुकला एवं प्रोटोकॉल</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Kevin Ashton 1999 • 4-Layer Architecture • Sensors &amp; Actuators • MQTT &amp; CoAP Protocols • LoRaWAN &amp; FASTag RFID • UP Smart Cities ICCC</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • केविन एश्टन 1999 • 4-स्तरीय वास्तुकला • सेंसर्स व एक्ट्यूएटर्स • MQTT व CoAP • LoRaWAN व फास्टैग RFID • उप्र स्मार्ट सिटीज ICCC</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-network-wired"></i>
            <span class="lang-en">Internet of Things (IoT) Architectural Hierarchy</span>
            <span class="lang-hi">इंटरनेट ऑफ थिंग्स (IoT) पदानुक्रमित वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: Origins & 4-Layer IoT Architecture -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-layer-group" style="color: #059669;"></i>
                    <span class="lang-en">1. Concept &amp; 4-Layer Architecture</span>
                    <span class="lang-hi">1. उद्भव एवं 4-स्तरीय IoT वास्तुकला</span>
                </h4>
                <span class="mindmap-node-tag">Kevin Ashton 1999 • 4 Layers</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Founders &amp; The 4 Layers</span>
                        <span class="lang-hi">संस्थापक एवं 4 प्रमुख परतें</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Kevin Ashton</strong> (1999, P&amp;G / MIT)</span>
                        <span class="mindmap-chip"><strong>1. Perception Layer</strong> (Sensors/Actuators)</span>
                        <span class="mindmap-chip"><strong>2. Network Layer</strong> (Wi-Fi, 5G, Zigbee)</span>
                        <span class="mindmap-chip"><strong>3. Processing Layer</strong> (Edge, Fog, Cloud)</span>
                        <span class="mindmap-chip"><strong>4. Application Layer</strong> (Smart Home/City)</span>
                        <span class="mindmap-chip"><strong>M2M</strong> (Machine-to-Machine)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Core Principles &amp; Layer Responsibilities</span>
                        <span class="lang-hi">मूलभूत सिद्धांत एवं परतों के दायित्व</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kevin Ashton &amp; IoT Genesis (1999):</strong> Coined the phrase <em>"Internet of Things"</em> in a presentation for Procter &amp; Gamble (P&amp;G) linking RFID supply chains to the Internet. Defined as a network of uniquely identifiable physical objects that collect and exchange data autonomously.</span>
                            <span class="lang-hi"><strong>केविन एश्टन एवं IoT का जन्म (1999):</strong> P&amp;G में RFID आपूर्ति श्रृंखला को इंटरनेट से जोड़ते हुए <em>"इंटरनेट ऑफ थिंग्स"</em> शब्द गढ़ा। भौतिक उपकरणों का ऐसा जाल जो बिना मानवीय हस्तक्षेप के डेटा का आदान-प्रदान करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The 4 Architectural Layers:</strong> <strong>1. Perception/Sensing Layer:</strong> Physical hardware (sensors, RFID tags) collecting environmental parameters. <strong>2. Network/Transport Layer:</strong> Securely transmits telemetry data via wireless/cellular protocols. <strong>3. Processing/Middleware Layer:</strong> Analyzes, filters, and stores sensor data (Cloud/Edge). <strong>4. Application Layer:</strong> Delivers actionable smart services to end-users (Smart Cities, Healthcare, Agriculture).</span>
                            <span class="lang-hi"><strong>4-स्तरीय वास्तुकला:</strong> <strong>1. परसेप्शन (संवेदी) परत:</strong> सेंसर्स व RFID द्वारा भौतिक डेटा संग्रह। <strong>2. नेटवर्क परत:</strong> 5G/Wi-Fi/ब्लूटूथ द्वारा डेटा ट्रांसमिशन। <strong>3. प्रोसेसिंग परत:</strong> क्लाउड या एज पर डेटा विश्लेषण। <strong>4. एप्लिकेशन परत:</strong> उपयोगकर्ता सेवाएं (स्मार्ट होम, स्मार्ट सिटी, कृषि)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kevin Ashton coined "Internet of Things" in 1999; Perception Layer is the bottom-most layer containing sensors and actuators!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1999 में केविन एश्टन ने 'इंटरनेट ऑफ थिंग्स' शब्द दिया; परसेप्शन लेयर सबसे निचली परत है जिसमें सेंसर्स व एक्ट्यूएटर्स होते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Sensors, Actuators & Embedded Hardware -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microchip" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Sensors, Actuators &amp; Boards</span>
                    <span class="lang-hi">2. सेंसर्स, एक्ट्यूएटर्स एवं माइक्रोकंट्रोलर</span>
                </h4>
                <span class="mindmap-node-tag">Arduino • Raspberry Pi • ESP32</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Hardware Elements &amp; Sensors</span>
                        <span class="lang-hi">हार्डवेयर उपकरण एवं सेंसर्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Sensors</strong> (Input: DHT11, PIR, Gas)</span>
                        <span class="mindmap-chip"><strong>Actuators</strong> (Output: Servos, Relays)</span>
                        <span class="mindmap-chip"><strong>Arduino Uno</strong> (ATmega328P, 2005)</span>
                        <span class="mindmap-chip"><strong>Raspberry Pi</strong> (Eben Upton 2012, Linux SBC)</span>
                        <span class="mindmap-chip"><strong>ESP8266 &amp; ESP32</strong> (Built-in Wi-Fi/BLE)</span>
                        <span class="mindmap-chip"><strong>Transducer Principle</strong> (Energy Conversion)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Sensors vs Actuators &amp; Development Boards</span>
                        <span class="lang-hi">सेंसर्स बनाम एक्ट्यूएटर्स एवं डेवलपमेंट बोर्ड्स</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sensors vs Actuators:</strong> <strong>Sensor (Input):</strong> Transducer that measures a physical quantity (temperature, humidity DHT11, motion PIR, light LDR, smoke MQ-2) and converts it into an electrical signal. <strong>Actuator (Output):</strong> Transducer that takes electrical commands and converts them into physical motion, force, or mechanical action (motors, servos, solenoid water valves, electrical relays).</span>
                            <span class="lang-hi"><strong>सेंसर बनाम एक्ट्यूएटर:</strong> <strong>सेंसर (इनपुट):</strong> भौतिक राशि (तापમાન DHT11, गति PIR, धुआं MQ-2) को विद्युत संकेत में बदलता है। <strong>एक्ट्यूएटर (आउटपुट):</strong> विद्युत संकेत को यांत्रिक गति या कार्य में बदलता है (सर्वो मोटर, रिले, वाल्व)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Arduino vs Raspberry Pi:</strong> <strong>Arduino:</strong> Open-source Microcontroller board (ATmega328P) executing a single repetitive C/C++ control loop; ultra-low power, ideal for direct sensor reading. <strong>Raspberry Pi:</strong> Complete Single-Board Computer (SBC) running a full Linux OS with HDMI, USB, and high-performance Broadcom ARM processor; ideal for edge computing and computer vision.</span>
                            <span class="lang-hi"><strong>आर्डुइनो बनाम रास्पबेरी पाई:</strong> <strong>आर्डुइनो (Arduino):</strong> एकल C/C++ लूप पर चलने वाला माइक्रोकंट्रोलर; कम बिजली खपत, सेंसर्स हेतु श्रेष्ठ। <strong>रास्पबेरी पाई (Raspberry Pi):</strong> पूर्ण लिनक्स OS चलाने वाला क्रेडिट-कार्ड आकार का कंप्यूटर; एज AI हेतु श्रेष्ठ।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sensors convert physical quantities into electrical signals (Input); Actuators convert electrical signals into physical action (Output); Arduino is a microcontroller while Raspberry Pi is a single-board computer!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सेंसर भौतिक राशि को विद्युत संकेत में बदलता है (इनपुट); एक्ट्यूएटर विद्युत संकेत को यांत्रिक कार्य में बदलता है (आउटपुट); आर्डुइनो माइक्रोकंट्रोलर है जबकि रास्पबेरी पाई एक पूर्ण कंप्यूटर है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Specialized IoT Protocols: MQTT & CoAP -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-satellite-dish" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. IoT Protocols: MQTT &amp; CoAP</span>
                    <span class="lang-hi">3. विशिष्ट IoT संचार प्रोटोकॉल: MQTT एवं CoAP</span>
                </h4>
                <span class="mindmap-node-tag">Pub/Sub • 2-Byte Header • Port 1883</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Protocols &amp; QoS Levels</span>
                        <span class="lang-hi">प्रोटोकॉल एवं QoS स्तर</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>MQTT</strong> (Stanford-Clark 1999, IBM)</span>
                        <span class="mindmap-chip"><strong>Pub/Sub Architecture</strong> (Publisher, Broker, Subscriber)</span>
                        <span class="mindmap-chip"><strong>2-Byte Fixed Header</strong> (Ultra-Lightweight)</span>
                        <span class="mindmap-chip"><strong>MQTT Port</strong> (1883 TCP / 8883 TLS)</span>
                        <span class="mindmap-chip"><strong>QoS 0, 1, 2</strong> (At most / At least / Exactly once)</span>
                        <span class="mindmap-chip"><strong>CoAP</strong> (Constrained Application Protocol, UDP)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">MQTT Mechanics &amp; Comparison with HTTP</span>
                        <span class="lang-hi">MQTT कार्यप्रणाली एवं HTTP से तुलना</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>MQTT (Message Queuing Telemetry Transport):</strong> Created by Andy Stanford-Clark &amp; Arlen Nipper in 1999 for satellite oil pipeline telemetry. Lightweight <strong>Publish/Subscribe</strong> messaging protocol over TCP/IP. Minimal <strong>2-byte header</strong> (compared to HTTP's thousands of bytes), making it ideal for battery-powered remote sensors over flaky networks.</span>
                            <span class="lang-hi"><strong>MQTT (मैसेज क्यूइंग टेलीमेट्री ट्रांसपोर्ट - 1999):</strong> कम बैंडविड्थ और रिमोट सेंसर्स हेतु निर्मित पब्लिश/सब्सक्राइब (Pub/Sub) प्रोटोकॉल। इसमें केवल <strong>2-बाइट का हेडर</strong> होता है (HTTP की तुलना में बहुत हल्का)। डिफॉल्ट पोर्ट: 1883 (TCP)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>MQTT Architecture &amp; QoS Levels:</strong> <strong>Publisher</strong> sends sensor data to central <strong>Broker</strong> on specific Topic; Broker forwards to all subscribed <strong>Subscribers</strong>. Quality of Service (QoS): <strong>QoS 0:</strong> At most once (no ack). <strong>QoS 1:</strong> At least once (acknowledged, duplicate possible). <strong>QoS 2:</strong> Exactly once (4-step handshake, highest reliability).</span>
                            <span class="lang-hi"><strong>MQTT संरचना व QoS स्तर:</strong> पब्लिशर -> ब्रोकर (केंद्रीकृत सर्वर) -> सब्सक्राइबर। <strong>QoS 0:</strong> अधिकतम एक बार। <strong>QoS 1:</strong> कम से कम एक बार (स्वीकृति सहित)। <strong>QoS 2:</strong> बिल्कुल एक बार (सटीकतम, 4-चरणीय हैंडशेक)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>CoAP (Constrained Application Protocol):</strong> Specialized web transfer protocol for constrained nodes; follows REST model (GET, POST, PUT, DELETE) but runs over lightweight <strong>UDP</strong> on port 5683 with minimal header overhead.</span>
                            <span class="lang-hi"><strong>CoAP प्रोटोकॉल:</strong> सीमित क्षमता वाले IoT उपकरणों हेतु REST आधारित वेब प्रोटोकॉल; HTTP के समान किंतु <strong>UDP</strong> पर संचालित (पोर्ट 5683)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> MQTT uses a Publish/Subscribe model with a tiny 2-byte header over TCP port 1883; CoAP runs over UDP on port 5683!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> MQTT पब्लिश-सब्सक्राइब मॉडल और 2-बाइट हेडर पर TCP पोर्ट 1883 पर चलता है; CoAP पोर्ट 5683 पर UDP का उपयोग करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Wireless Communication & LPWAN Standards -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-wifi" style="color: #d97706;"></i>
                    <span class="lang-en">4. Wireless Standards &amp; LPWAN</span>
                    <span class="lang-hi">4. वायरलेस कनेक्टिविटी एवं LPWAN मानक</span>
                </h4>
                <span class="mindmap-node-tag">RFID FASTag • LoRaWAN • Zigbee</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Standards &amp; Frequency Bands</span>
                        <span class="lang-hi">मानक एवं आवृत्ति बैंड</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>RFID</strong> (Passive vs Active Tags)</span>
                        <span class="mindmap-chip"><strong>FASTag</strong> (UHF 865-868 MHz)</span>
                        <span class="mindmap-chip"><strong>Zigbee</strong> (IEEE 802.15.4, 2.4 GHz Mesh)</span>
                        <span class="mindmap-chip"><strong>BLE</strong> (Bluetooth Low Energy, Wearables)</span>
                        <span class="mindmap-chip"><strong>LoRaWAN</strong> (10-15 km, 10-Yr Battery)</span>
                        <span class="mindmap-chip"><strong>NB-IoT</strong> (Narrowband IoT, Cellular 3GPP)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Short-Range vs Long-Range LPWAN</span>
                        <span class="lang-hi">लघु दूरी बनाम दीर्घ दूरी (LPWAN) तकनीक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>RFID &amp; FASTag Mechanics:</strong> Radio Frequency Identification. <strong>Passive RFID Tags:</strong> Have no internal battery; powered wirelessly by reader's electromagnetic interrogation signal. <strong>FASTag:</strong> Electronic toll collection system across Indian highways utilizing passive UHF RFID (865-868 MHz) affixed on vehicle windshields; managed by NPCI and NHAI.</span>
                            <span class="lang-hi"><strong>RFID एवं फास्टैग (FASTag):</strong> <strong>पैसिव RFID:</strong> इसमें कोई बैटरी नहीं होती; स्कैनर के इलेक्ट्रोमैग्नेटिक क्षेत्र से ऊर्जा प्राप्त करता है। <strong>फास्टैग:</strong> भारतीय राष्ट्रीय राजमार्गों पर वाहनों की विंडशील्ड पर लगा पैसिव UHF RFID टैग (865-868 MHz); NHAI व NPCI द्वारा प्रबंधित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Short-Range Standards (Zigbee &amp; BLE):</strong> <strong>Zigbee (IEEE 802.15.4):</strong> Low-power mesh networking standard operating at 2.4 GHz; devices relay messages through neighbors (smart home bulbs, smart switches). <strong>BLE:</strong> Operates at 2.4 GHz ISM band; ultra-low power consumption for fitness bands and smartwatches.</span>
                            <span class="lang-hi"><strong>शॉर्ट-रेंज मानक (जिगबी व BLE):</strong> <strong>जिगबी (Zigbee - 802.15.4):</strong> मेश नेटवर्क आधारित घरेलू स्वचालन मानक। <strong>BLE (ब्लूटूथ लो एनर्जी):</strong> फिटनेस बैंड व घड़ियों में प्रयुक्त अति-अल्प ऊर्जा खपत मानक।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>LPWAN (LoRaWAN &amp; NB-IoT):</strong> Low-Power Wide-Area Networks transmit small packets over 10-15 km with battery life extending up to 10 years. <strong>LoRaWAN:</strong> Uses chirp spread spectrum on unlicensed sub-GHz bands (865-867 MHz in India). <strong>NB-IoT:</strong> Operates on licensed cellular frequencies managed by telecom operators.</span>
                            <span class="lang-hi"><strong>LPWAN (LoRaWAN व NB-IoT):</strong> 10-15 किमी दूर तक डेटा भेजने वाली कम ऊर्जा तकनीक (10 वर्ष तक बैटरी लाइफ)। स्मार्ट पानी/बिजली मीटरों व कृषि में प्रयुक्त।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> FASTag operates on Passive UHF RFID technology at 865-868 MHz; Zigbee uses IEEE 802.15.4; LoRaWAN provides 10-15 km range with 10-year battery life!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> फास्टैग 865-868 MHz पर पैसिव UHF RFID तकनीक से कार्य करता है; जिगबी का मानक IEEE 802.15.4 है; LoRaWAN 10-15 किमी तक रेंज देता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Edge, Fog & Cloud Computing Paradigm -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cloud" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Edge, Fog &amp; Cloud Computing</span>
                    <span class="lang-hi">5. एज, फॉग एवं क्लाउड कंप्यूटिंग प्रतिमान</span>
                </h4>
                <span class="mindmap-node-tag">Cisco Fog • Zero Latency</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Computing Tiers &amp; Twins</span>
                        <span class="lang-hi">कंप्यूटिंग स्तर एवं डिजिटल ट्विन</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Cloud Computing</strong> (Centralized Data Centers)</span>
                        <span class="mindmap-chip"><strong>Fog Computing</strong> (Cisco 2012, Gateway Level)</span>
                        <span class="mindmap-chip"><strong>Edge Computing</strong> (On-Device Local AI)</span>
                        <span class="mindmap-chip"><strong>Zero-Latency</strong> (Real-Time Safety Action)</span>
                        <span class="mindmap-chip"><strong>Digital Twin</strong> (Virtual Asset Mirror)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Tier Comparison &amp; Digital Twin Concepts</span>
                        <span class="lang-hi">कंप्यूटिंग स्तर तुलना एवं डिजिटल ट्विन सिद्धांत</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cloud vs Fog vs Edge:</strong> <strong>Cloud Computing:</strong> Centralized distant data centers; infinite storage and compute; high latency and bandwidth cost. <strong>Fog Computing (Cisco, 2012):</strong> Decentralized intermediate layer on local LAN gateways and routers. <strong>Edge Computing:</strong> Data processed right on the physical device or sensor (microcontroller, smart camera); delivers near-zero latency, operates offline, preserves privacy.</span>
                            <span class="lang-hi"><strong>क्लाउड बनाम फॉग बनाम एज कंप्यूटिंग:</strong> <strong>क्लाउड:</strong> दूर स्थित विशाल सर्वर (अधिक लेटेंसी)। <strong>फॉग कंप्यूटिंग (सिस्को 2012):</strong> स्थानीय नेटवर्क गेटवे पर प्रोसेसिंग। <strong>एज कंप्यूटिंग:</strong> डेटा का सीधे उपकरण/कैमरे पर ही विश्लेषण (शून्य लेटेंसी, बिना इंटरनेट त्वरित निर्णय)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Digital Twin Technology:</strong> Exact virtual software clone of a physical device, machine, or smart city updated in real-time from continuous IoT sensor telemetry. Enables engineers to simulate stresses, predict breakdowns, and optimize performance before physical changes.</span>
                            <span class="lang-hi"><strong>डिजिटल ट्विन (Digital Twin):</strong> किसी भौतिक मशीन, पुल या स्मार्ट शहर का डिजिटल सॉफ्टवेयर मॉडल; लाइव IoT डेटा से अपडेट रहकर संभावित खराबियों और रखरखाव का अग्रिम अनुमान लगाता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Fog Computing was introduced by Cisco in 2012; Edge Computing executes processing directly on the sensor/device to eliminate network latency!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> फॉग कंप्यूटिंग शब्द 2012 में सिस्को (Cisco) ने दिया; एज कंप्यूटिंग लेटेंसी मिटाने हेतु सीधे उपकरण पर डेटा प्रोसेस करती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Uttar Pradesh Smart Cities & ICCC Projects -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-city" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. UP Smart Cities &amp; Governance</span>
                    <span class="lang-hi">6. उत्तर प्रदेश में IoT: स्मार्ट सिटीज एवं ICCC</span>
                </h4>
                <span class="mindmap-node-tag">10 Smart Cities • ICCC Centers</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">UP IoT Megaprojects</span>
                        <span class="lang-hi">उत्तर प्रदेश में IoT की प्रमुख परियोजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>10 UP Smart Cities</strong> (National Mission)</span>
                        <span class="mindmap-chip"><strong>ICCC Centers</strong> (Integrated Command Control)</span>
                        <span class="mindmap-chip"><strong>Smart Water Telemetry</strong> (Jal Jeevan Mission)</span>
                        <span class="mindmap-chip"><strong>Smart Solid Waste</strong> (GPS &amp; RFID Bins)</span>
                        <span class="mindmap-chip"><strong>Bundelkhand Agri IoT</strong> (Soil Moisture Drip)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Real-World Deployments in Uttar Pradesh</span>
                        <span class="lang-hi">उत्तर प्रदेश में वास्तविक धरातलीय क्रियान्वयन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>10 UP Smart Cities &amp; ICCC:</strong> 10 cities selected under National Smart Cities Mission in UP: Lucknow, Kanpur, Prayagraj, Varanasi, Agra, Aligarh, Jhansi, Moradabad, Bareilly, Saharanpur. All equipped with <strong>Integrated Command and Control Centers (ICCC)</strong> acting as city's digital brain, aggregating feeds from thousands of CCTV cameras, environmental air quality sensors, and traffic lights.</span>
                            <span class="lang-hi"><strong>उप्र के 10 स्मार्ट शहर एवं ICCC:</strong> राष्ट्रीय स्मार्ट सिटी मिशन के तहत चयनित: लखनऊ, कानपुर, प्रयागराज, वाराणसी, आगरा, अलीगढ़, झांसी, मुरादाबाद, बरेली व सहारनपुर। सभी शहरों में <strong>ICCC केंद्र</strong> स्थापित हैं जो वायु गुणवत्ता, सीसीटीवी कैमरों व ट्रैफिक सेंसर्स की एकीकृत निगरानी करते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jal Jeevan Mission Rural Telemetry:</strong> Water flow sensors and residual chlorine analyzers deployed across rural UP piped drinking water networks, streaming continuous telemetry to ensure safe, regular water supply.</span>
                            <span class="lang-hi"><strong>जल जीवन मिशन ग्रामीण टेलीमेट्री:</strong> उप्र के ग्रामीण इलाकों में नल-से-जल आपूर्ति में जल प्रवाह व क्लोरीन स्तर मापने हेतु IoT सेंसर्स द्वारा लाइव निगरानी।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> 10 cities in Uttar Pradesh were selected under the National Smart Cities Mission, all connected via Integrated Command and Control Centers (ICCC)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> राष्ट्रीय स्मार्ट सिटी मिशन के तहत उत्तर प्रदेश के 10 शहर चयनित हुए, जो ICCC (इंटीग्रेटेड कमांड एंड कंट्रोल सेंटर) द्वारा संचालित हैं!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
