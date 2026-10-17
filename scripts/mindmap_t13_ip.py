# Topic 13: Internet Protocol & IP Address
mm_t13 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: IP Addressing, Protocols &amp; IPv4 vs IPv6</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: आईपी एड्रेसिंग, सबनेटिंग, नेटवर्क प्रोटोकॉल एवं IPv4 बनाम IPv6</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • IPv4 Classes &amp; Ranges • Private IP &amp; NAT • CIDR &amp; Subnetting Math • 128-bit IPv6 Architecture • Core Protocols (DHCP, DNS, ARP) • Logical IP vs MAC</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • IPv4 वर्ग व रेंज • प्राइवेट IP व NAT • CIDR व सबनेटिंग गणना • 128-बिट IPv6 वास्तुकला • मुख्य प्रोटोकॉल (DHCP, DNS, ARP) • लॉजिकल IP बनाम MAC</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-map-signs"></i>
            <span class="lang-en">IP Addressing &amp; Internet Protocols Hierarchy</span>
            <span class="lang-hi">आईपी एड्रेसिंग एवं इंटरनेट प्रोटोकॉल पदानुक्रम</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: IPv4 Architecture & The 5 Classes -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-network-wired" style="color: #059669;"></i>
                    <span class="lang-en">1. IPv4 Architecture &amp; Classes</span>
                    <span class="lang-hi">1. IPv4 संरचना एवं 5 वर्ग (Classes)</span>
                </h4>
                <span class="mindmap-node-tag">32-Bit • 4 Octets • 4.3 Billion</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">IPv4 Classes &amp; Ranges</span>
                        <span class="lang-hi">IPv4 के वर्ग एवं उनकी रेंज</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>32-Bit Address</strong> (4 Octets, Dotted Decimal)</span>
                        <span class="mindmap-chip"><strong>Class A: 1 – 126</strong> (Mask 255.0.0.0, Very Large)</span>
                        <span class="mindmap-chip"><strong>Loopback: 127.0.0.1</strong> (Internal Self-Test)</span>
                        <span class="mindmap-chip"><strong>Class B: 128 – 191</strong> (Mask 255.255.0.0, Medium)</span>
                        <span class="mindmap-chip"><strong>Class C: 192 – 223</strong> (Mask 255.255.255.0, Small)</span>
                        <span class="mindmap-chip"><strong>Class D: 224 – 239</strong> (Multicast Groups)</span>
                        <span class="mindmap-chip"><strong>Class E: 240 – 255</strong> (Experimental/Research)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Class Breakdown &amp; Octet Mechanics</span>
                        <span class="lang-hi">वर्ग विभाजन एवं ऑक्टेट कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IPv4 Address Structure:</strong> 32-bit binary number expressed as 4 decimal octets separated by dots (0-255 each, e.g. <code>192.168.1.1</code>). Total theoretical address space: $2^{32} \approx 4,294,967,296$ (~4.29 billion addresses).</span>
                            <span class="lang-hi"><strong>IPv4 संरचना:</strong> 32-बिट बाइनरी संख्या जिसे 4 दशमलव ऑक्टेट्स में बिंदुओं द्वारा लिखा जाता है (0 से 255 प्रत्येक, उदा. <code>192.168.1.1</code>)। कुल सैद्धांतिक क्षमता: $2^{32} \approx 4.29$ अरब पते।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Classful IP Allocation:</strong> <strong>Class A (1-126):</strong> Leading bit `0`; 126 networks, 16.7 million hosts each. <strong>Loopback (127.x.x.x):</strong> <code>127.0.0.1</code> reserved for localhost internal diagnostics. <strong>Class B (128-191):</strong> Leading bits `10`; 65,534 hosts each. <strong>Class C (192-223):</strong> Leading bits `110`; 254 hosts each. <strong>Class D (224-239):</strong> Multicasting (no subnet mask). <strong>Class E (240-255):</strong> Research/Experimental.</span>
                            <span class="lang-hi"><strong>वर्गवार विभाजन:</strong> <strong>क्लास A (1-126):</strong> अति विशाल नेटवर्क। <strong>लूपबैक (127.0.0.1):</strong> कंप्यूटर की स्वयं की जांच हेतु आरक्षित। <strong>क्लास B (128-191):</strong> मध्यम नेटवर्क (65,534 होस्ट)। <strong>क्लास C (192-223):</strong> छोटे नेटवर्क (254 होस्ट)। <strong>क्लास D (224-239):</strong> मल्टीकास्टिंग। <strong>क्लास E (240-255):</strong> अनुसंधान हेतु।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IPv4 has 32 bits divided into 4 octets; Class D is reserved for Multicasting; 127.0.0.1 is the Loopback/localhost address!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> IPv4 में 32 बिट्स होते हैं जो 4 ऑक्टेट्स में बंटे होते हैं; क्लास D 'मल्टीकास्टिंग' हेतु आरक्षित है; 127.0.0.1 लूपबैक (Localhost) पता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Public vs Private IP Addresses & NAT -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-user-shield" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Private IPs, Public IPs &amp; NAT</span>
                    <span class="lang-hi">2. प्राइवेट IP, पब्लिक IP एवं NAT प्रणाली</span>
                </h4>
                <span class="mindmap-node-tag">RFC 1918 • 192.168.x.x • NAT</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Private Ranges (RFC 1918)</span>
                        <span class="lang-hi">प्राइवेट IP रेंज (RFC 1918)</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Class A Private:</strong> 10.0.0.0 – 10.255.255.255 (/8)</span>
                        <span class="mindmap-chip"><strong>Class B Private:</strong> 172.16.0.0 – 172.31.255.255 (/12)</span>
                        <span class="mindmap-chip"><strong>Class C Private:</strong> 192.168.0.0 – 192.168.255.255 (/16)</span>
                        <span class="mindmap-chip"><strong>APIPA Range:</strong> 169.254.0.0 – 169.254.255.255 (/16)</span>
                        <span class="mindmap-chip"><strong>NAT:</strong> Network Address Translation</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Public vs Private Mechanics &amp; Address Translation</span>
                        <span class="lang-hi">पब्लिक बनाम प्राइवेट कार्यप्रणाली एवं NAT</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Public vs Private IP Addresses:</strong> <strong>Public IPs:</strong> Globally unique, assigned by ISP/IANA, directly routable across the worldwide Internet. <strong>Private IPs (RFC 1918):</strong> Reserved for internal local home/office LANs; non-routable on the public Internet; reusable across billions of private networks without conflict.</span>
                            <span class="lang-hi"><strong>पब्लिक बनाम प्राइवेट IP:</strong> <strong>पब्लिक IP:</strong> विश्व में अद्वितीय, ISP द्वारा प्रदत्त, इंटरनेट पर सीधे खोजने योग्य। <strong>प्राइवेट IP (RFC 1918):</strong> घरेलू व कार्यालयी LAN हेतु आरक्षित; इंटरनेट पर सीधे नहीं जा सकते; अरबों नेटवर्कों में पुनः उपयोग संभव।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Network Address Translation (NAT):</strong> Router technology that maps hundreds of internal private IP devices onto a single external public IP using unique port numbers (Port Address Translation / PAT), conserving scarce IPv4 addresses.</span>
                            <span class="lang-hi"><strong>नेटवर्क एड्रेस ट्रांसलेशन (NAT):</strong> घर के दर्जनों उपकरणों के प्राइवेट IP पतों को राउटर पर केवल एक पब्लिक IP पते में बदलता है, जिससे करोड़ों IPv4 पतों की बचत होती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>APIPA (Automatic Private IP Addressing):</strong> Automatically self-assigned by Windows client (<code>169.254.x.x</code>) when DHCP server fails to respond, allowing local subnet communication without Internet access.</span>
                            <span class="lang-hi"><strong>APIPA (169.254.x.x):</strong> जब कंप्यूटर को नेटवर्क पर DHCP सर्वर से IP नहीं मिल पाता, तो विंडोज स्वतः 169.254.x.x रेंज का IP चुन लेता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> 192.168.x.x and 10.x.x.x are Private IP addresses; APIPA assigns 169.254.x.x when DHCP is unavailable; NAT maps private IPs to a public IP!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 192.168.x.x व 10.x.x.x प्राइवेट IP पते हैं; DHCP न मिलने पर APIPA द्वारा 169.254.x.x मिलता है; NAT प्राइवेट को पब्लिक IP में बदलता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: CIDR Subnetting & Network Calculation -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-calculator" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. CIDR &amp; Subnetting Math</span>
                    <span class="lang-hi">3. CIDR सबनेटिंग एवं होस्ट गणना</span>
                </h4>
                <span class="mindmap-node-tag">Slash /24 • 2^h - 2 Formula</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">CIDR Prefixes &amp; Usable Hosts</span>
                        <span class="lang-hi">CIDR प्रीफिक्स एवं प्रयोग योग्य होस्ट</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>CIDR</strong> (Classless Inter-Domain Routing, 1993)</span>
                        <span class="mindmap-chip"><strong>/24 Prefix:</strong> 254 Hosts (Mask 255.255.255.0)</span>
                        <span class="mindmap-chip"><strong>/25 Prefix:</strong> 126 Hosts (Mask 255.255.255.128)</span>
                        <span class="mindmap-chip"><strong>/26 Prefix:</strong> 62 Hosts (Mask 255.255.255.192)</span>
                        <span class="mindmap-chip"><strong>/28 Prefix:</strong> 14 Hosts (Mask 255.255.255.240)</span>
                        <span class="mindmap-chip"><strong>/30 Prefix:</strong> 2 Hosts (Point-to-Point Routers)</span>
                        <span class="mindmap-chip"><strong>Formula:</strong> 2^h - 2 Usable Hosts</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Subnet Mask Logic &amp; Host Calculation Formula</span>
                        <span class="lang-hi">सबनेट मास्क तर्क एवं होस्ट गणना सूत्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>CIDR Notation (RFC 1519, 1993):</strong> Replaced rigid classful boundaries with variable prefix length notation (e.g. <code>192.168.1.0/24</code> where <code>/24</code> specifies that the first 24 bits are Network portion, leaving 8 bits for Hosts).</span>
                            <span class="lang-hi"><strong>CIDR पद्धति (1993):</strong> क्लास आधारित सीमाओं को समाप्त कर स्लैश नोटेशन (उदा. <code>/24</code>) दिया, जहाँ /24 का अर्थ है कि पहले 24 बिट्स नेटवर्क के हैं और शेष 8 बिट्स होस्ट के।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mathematical Host Formula ($2^h - 2$):</strong> In any subnet with $h$ host bits, the total usable host IP addresses is strictly $2^h - 2$. Two addresses are deducted because: <strong>1. First address</strong> (all host bits 0) is the <strong>Network ID</strong>. <strong>2. Last address</strong> (all host bits 1) is the <strong>Broadcast Address</strong>. Example for /24: $2^8 - 2 = 256 - 2 = 254$ usable hosts.</span>
                            <span class="lang-hi"><strong>होस्ट गणना का सूत्र ($2^h - 2$):</strong> $h$ होस्ट बिट्स वाले सबनेट में कुल प्रयोग योग्य कंप्यूटरों की संख्या $2^h - 2$ होती है। 2 घटाने का कारण: <strong>पहला पता</strong> (सभी 0) = <strong>नेटवर्क ID</strong>; <strong>अंतिम पता</strong> (सभी 1) = <strong>ब्रॉडकास्ट पता</strong>। /24 हेतु: $2^8 - 2 = 254$ होस्ट।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> In a /24 subnet, total usable host addresses is 254 (formula: 2^h - 2); the first address is Network ID and the last address is Broadcast ID!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> /24 सबनेट में प्रयोग योग्य होस्ट की संख्या 254 होती है ($2^h - 2$ सूत्र); पहला पता नेटवर्क ID और अंतिम पता ब्रॉडकास्ट ID होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: IPv6 Architecture & Notation -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-infinity" style="color: #d97706;"></i>
                    <span class="lang-en">4. IPv6 Architecture &amp; Notation</span>
                    <span class="lang-hi">4. IPv6 वास्तुकला एवं हेक्साडेसिमल संकेतन</span>
                </h4>
                <span class="mindmap-node-tag">128-Bit • 8 Quartets • 3.4x10^38</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">IPv6 Specs &amp; Compression Rules</span>
                        <span class="lang-hi">IPv6 विनिर्देश एवं संपीड़न नियम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>128-Bit Length</strong> (4x Longer than IPv4)</span>
                        <span class="mindmap-chip"><strong>8 Hex Quartets</strong> (Colon Separated)</span>
                        <span class="mindmap-chip"><strong>3.4 x 10^38 Addresses</strong> (Undecillion)</span>
                        <span class="mindmap-chip"><strong>Omit Leading Zeros</strong> (:0042: -> :42:)</span>
                        <span class="mindmap-chip"><strong>Double Colon (::)</strong> (Compress Zeros Once)</span>
                        <span class="mindmap-chip"><strong>Loopback: ::1</strong> (IPv6 Localhost)</span>
                        <span class="mindmap-chip"><strong>Built-in IPsec</strong> (Network Layer Security)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">IPv6 Advantages &amp; Zero Compression</span>
                        <span class="lang-hi">IPv6 के लाभ एवं शून्य संपीड़न के नियम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IPv6 Specifications:</strong> 128-bit address represented as 8 quartets of 4 hexadecimal digits separated by colons (e.g. <code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code>). Total addresses = $2^{128} \approx 3.4 \times 10^{38}$. Solves IPv4 exhaustion forever.</span>
                            <span class="lang-hi"><strong>IPv6 विनिर्देश:</strong> 128-बिट पता जो 8 हेक्साडेसिमल खंडों में कोलन (:) द्वारा अलग किया जाता है (उदा. <code>2001:0db8:...</code>)। कुल पते = $2^{128} \approx 3.4 \times 10^{38}$। IPv4 की कमी को सदा हेतु समाप्त करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Compression Rules:</strong> <strong>Rule 1:</strong> Leading zeros in any quartet can be omitted (<code>:0db8:</code> becomes <code>:db8:</code>). <strong>Rule 2:</strong> One contiguous run of consecutive all-zero quartets can be replaced by double colon <code>::</code> (e.g. <code>2001:db8::8a2e:370:7334</code>). <code>::</code> can appear only ONCE in an address!</span>
                            <span class="lang-hi"><strong>संपीड़न (छोटा करने) के नियम:</strong> <strong>नियम 1:</strong> प्रत्येक खंड के शुरुआती शून्य हटाए जा सकते हैं (:0042: का :42:)। <strong>नियम 2:</strong> लगातार शून्य वाले खंडों को डबल कोलन <code>::</code> द्वारा केवल एक बार संक्षिप्त किया जा सकता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Architectural Advantages:</strong> Eliminates need for NAT, provides native end-to-end IPsec encryption, simplified fixed 40-byte base header, eliminates broadcasts (uses multicast/anycast), and supports Stateless Address Autoconfiguration (SLAAC).</span>
                            <span class="lang-hi"><strong>वास्तुकला लाभ:</strong> NAT की आवश्यकता समाप्त, इन-बिल्ट IPsec सुरक्षा, निश्चित 40-बाइट हेडर, ब्रॉडकास्ट के स्थान पर मल्टीकास्ट व एनीकास्ट, तथा स्वतः कॉन्फ़िगरेशन (SLAAC)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IPv6 has 128 bits (16 bytes); loopback address in IPv6 is ::1; double colon (::) can only be used once in an IPv6 address!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> IPv6 में 128 बिट्स (16 बाइट्स) होते हैं; IPv6 में लूपबैक पता '::1' है; डबल कोलन (::) का प्रयोग पते में केवल एक बार हो सकता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Supporting Protocols: DHCP, DNS, ARP & ICMP -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-exchange-alt" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Supporting Network Protocols</span>
                    <span class="lang-hi">5. सहायक नेटवर्क प्रोटोकॉल: DHCP, DNS, ARP</span>
                </h4>
                <span class="mindmap-node-tag">DORA • DNS Port 53 • ARP MAC</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Protocols &amp; Port Numbers</span>
                        <span class="lang-hi">प्रोटोकॉल एवं पोर्ट नंबर</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>DHCP</strong> (DORA Process, UDP 67/68)</span>
                        <span class="mindmap-chip"><strong>DNS</strong> (Domain to IP, Port 53)</span>
                        <span class="mindmap-chip"><strong>ARP</strong> (Logical IP -> Physical MAC)</span>
                        <span class="mindmap-chip"><strong>RARP</strong> (Physical MAC -> Logical IP)</span>
                        <span class="mindmap-chip"><strong>ICMP</strong> (Ping &amp; Traceroute Diagnostics)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Protocol Mechanics: DORA &amp; Name Resolution</span>
                        <span class="lang-hi">प्रोटोकॉल कार्यप्रणाली: DORA एवं नाम समाधान</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>DHCP &amp; DORA Process:</strong> Dynamic Host Configuration Protocol automatically assigns IP address, subnet mask, default gateway, and DNS servers to client devices. 4-Step DORA Handshake: <strong>D</strong>iscover (broadcast) -> <strong>O</strong>ffer (from server) -> <strong>R</strong>equest (from client) -> <strong>A</strong>cknowledge (confirmation). Operates over UDP ports 67 (server) and 68 (client).</span>
                            <span class="lang-hi"><strong>DHCP एवं DORA प्रक्रिया:</strong> कंप्यूटर को स्वतः IP पता देने वाली सेवा। DORA के 4 चरण: <strong>D</strong>iscover (खोज) -> <strong>O</strong>ffer (प्रस्ताव) -> <strong>R</strong>equest (अनुरोध) -> <strong>A</strong>cknowledge (स्वीकृति)। UDP पोर्ट 67 व 68।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>DNS (Domain Name System, Port 53):</strong> Known as the "Phonebook of the Internet" (Paul Mockapetris, 1983). Translates user-friendly domain names (e.g. <code>upsssc.gov.in</code>) into numerical IP addresses. Common records: <strong>A</strong> (IPv4 address), <strong>AAAA</strong> (IPv6 address), <strong>CNAME</strong> (canonical alias), <strong>MX</strong> (mail server).</span>
                            <span class="lang-hi"><strong>DNS (डोमेन नेम सिस्टम - पोर्ट 53):</strong> इंटरनेट की फोनबुक (पॉल मोकापेट्रिस 1983); डोमेन नामों (upsssc.gov.in) को संख्यात्मक IP पते में बदलता है। A रिकॉर्ड = IPv4, AAAA रिकॉर्ड = IPv6।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>ARP vs ICMP:</strong> <strong>ARP (Address Resolution Protocol):</strong> Resolves known Logical IP address into unknown 48-bit physical hardware MAC address on local network broadcast. <strong>ICMP:</strong> Reports network delivery errors and provides network diagnostics (powers <code>ping</code> and <code>traceroute</code>).</span>
                            <span class="lang-hi"><strong>ARP बनाम ICMP:</strong> <strong>ARP:</strong> ज्ञात IP पते से उपकरण का भौतिक MAC पता खोजता है। <strong>ICMP:</strong> नेटवर्क कनेक्टिविटी जांचने (Ping व Traceroute कमांड) हेतु प्रयुक्त।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> DHCP assigns IP addresses using the DORA process; DNS resolves domain names to IP over port 53; ARP translates IP addresses to MAC addresses!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> DHCP DORA प्रक्रिया द्वारा IP पता देता है; DNS पोर्ट 53 पर डोमेन नाम को IP में बदलता है; ARP IP पते को MAC पते में परिवर्तित करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Logical IP vs Physical MAC & India IPv6 Leadership -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-id-card" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. IP vs MAC &amp; India IPv6 Rank</span>
                    <span class="lang-hi">6. लॉजिकल IP बनाम MAC एवं भारत में IPv6</span>
                </h4>
                <span class="mindmap-node-tag">48-Bit MAC • #1 Global IPv6</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Hardware vs Software Addressing</span>
                        <span class="lang-hi">हार्डवेयर बनाम सॉफ्टवेयर एड्रेसिंग</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>MAC Address</strong> (48-Bit / 6 Octets / 12 Hex)</span>
                        <span class="mindmap-chip"><strong>OUI Prefix</strong> (First 24 Bits, Manufacturer)</span>
                        <span class="mindmap-chip"><strong>NIC Specific</strong> (Last 24 Bits, Serial No)</span>
                        <span class="mindmap-chip"><strong>Physical vs Logical</strong> (Permanent vs Configurable)</span>
                        <span class="mindmap-chip"><strong>India Global Rank #1</strong> (&gt;80% IPv6 Adoption)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">MAC Address Anatomy &amp; India's Global IPv6 Rank</span>
                        <span class="lang-hi">MAC पता संरचना एवं भारत की वैश्विक IPv6 स्थिति</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>MAC Address Architecture:</strong> 48-bit (6 bytes / 12 hex digits) hardware address burned permanently into ROM of Network Interface Card (NIC). Format: <code>00:1A:2B:3C:4D:5E</code>. <strong>First 24 bits (3 bytes):</strong> Organizationally Unique Identifier (OUI) assigned to manufacturer by IEEE. <strong>Last 24 bits (3 bytes):</strong> Unique device serial number.</span>
                            <span class="lang-hi"><strong>MAC पते की संरचना:</strong> 48-बिट (6 बाइट्स / 12 हेक्साडेसिमल अंक) भौतिक पता जो NIC कार्ड के ROM में स्थायी रूप से दर्ज होता है। <strong>प्रथम 24 बिट्स:</strong> निर्माता कंपनी का OUI कोड। <strong>अंतिम 24 बिट्स:</strong> विशिष्ट उपकरण सीरियल नंबर।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Logical IP vs Physical MAC:</strong> IP Address (Layer 3) is logical, software-configurable, and changes with geographic network location. MAC Address (Layer 2) is physical, immutable, and remains constant regardless of which network the device joins.</span>
                            <span class="lang-hi"><strong>IP बनाम MAC तुलना:</strong> IP पता (लेयर 3) सॉफ्टवेयर आधारित व परिवर्तनीय है (स्थान बदलने पर बदल जाता है)। MAC पता (लेयर 2) हार्डवेयर आधारित व स्थायी है (कभी नहीं बदलता)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>India's Global IPv6 Leadership:</strong> India ranks <strong>#1 in the world</strong> in IPv6 adoption (over 80% user adoption rate tracked by Google and APNIC), driven by Reliance Jio 4G/5G, Digital India initiatives, and National IPv6 Deployment Roadmaps by DoT.</span>
                            <span class="lang-hi"><strong>भारत की वैश्विक IPv6 में प्रथम रैंक:</strong> 80% से अधिक IPv6 अंगीकरण के साथ भारत विश्व में <strong>पहले स्थान</strong> पर है (रिलायंस जियो व डिजिटल इंडिया की महत्वपूर्ण भूमिका)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> MAC Address has 48 bits (6 bytes) in hexadecimal; the first 24 bits represent the OUI; India ranks #1 globally in IPv6 adoption!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> MAC पते में 48 बिट्स (6 बाइट्स) हेक्साडेसिमल में होते हैं; प्रथम 24 बिट्स OUI दर्शाते हैं; IPv6 अपनाने में भारत विश्व में प्रथम स्थान पर है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
