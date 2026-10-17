# Topic 16: Information Technology
mm_t16 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Information Technology, Databases &amp; Cyber Security</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: सूचना प्रौद्योगिकी (IT), RDBMS, क्लाउड एवं साइबर सुरक्षा</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • DIKW Pyramid • Relational Model &amp; Codd's Rules • Cloud SPI (IaaS/PaaS/SaaS) • Malware Taxonomy • RSA Cryptography • Helpline 1930</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • DIKW पिरामिड • रिलेशनल मॉडल व कॉड के नियम • क्लाउड SPI • मैलवेयर वर्गीकरण • RSA क्रिप्टोग्राफी • साइबर हेल्पलाइन 1930</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-laptop-code"></i>
            <span class="lang-en">Information Technology &amp; Security Architecture</span>
            <span class="lang-hi">सूचना प्रौद्योगिकी एवं सुरक्षा वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: The DIKW Information Pyramid & Storage Units -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-layer-group" style="color: #059669;"></i>
                    <span class="lang-en">1. DIKW Pyramid &amp; Storage Units</span>
                    <span class="lang-hi">1. DIKW ज्ञान पिरामिड एवं स्टोरेज इकाइयाँ</span>
                </h4>
                <span class="mindmap-node-tag">Data -> Info -> Knowledge -> Wisdom</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">DIKW Hierarchy &amp; Bit Conversions</span>
                        <span class="lang-hi">DIKW पदानुक्रम एवं मेमोरी इकाइयाँ</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Data</strong> (Raw Unprocessed Facts)</span>
                        <span class="mindmap-chip"><strong>2. Information</strong> (Contextualized Data)</span>
                        <span class="mindmap-chip"><strong>3. Knowledge</strong> (Actionable Understanding)</span>
                        <span class="mindmap-chip"><strong>4. Wisdom</strong> (Prudent Ethical Application)</span>
                        <span class="mindmap-chip"><strong>1 Nibble = 4 Bits</strong> (Half Byte)</span>
                        <span class="mindmap-chip"><strong>1 Byte = 8 Bits</strong> (1 Character)</span>
                        <span class="mindmap-chip"><strong>1 KB = 1024 Bytes</strong> (2^10)</span>
                        <span class="mindmap-chip"><strong>PB -> EB -> ZB -> YB</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">DIKW Pipeline &amp; Binary Memory Hierarchy</span>
                        <span class="lang-hi">DIKW विकास क्रम एवं बाइनरी मेमोरी पदानुक्रम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The DIKW Hierarchy:</strong> <strong>Data:</strong> Raw, unorganized facts without context (e.g. <code>98.6</code>). <strong>Information:</strong> Structured, processed data with meaning (e.g. <code>Patient body temperature is 98.6°F</code>). <strong>Knowledge:</strong> Understanding how to apply information (e.g. <code>98.6°F represents normal human body temperature</code>). <strong>Wisdom:</strong> Evaluating long-term ethical and strategic impact.</span>
                            <span class="lang-hi"><strong>DIKW पदानुक्रम:</strong> <strong>डेटा:</strong> असंसाधित कच्चा तथ्य (उदा. 98.6)। <strong>सूचना (Information):</strong> संदर्भयुक्त सार्थक डेटा (शरीर का तापमान 98.6°F है)। <strong>ज्ञान (Knowledge):</strong> समझ कि यह सामान्य तापमान है। <strong>प्रज्ञा (Wisdom):</strong> सही निर्णय लेने की क्षमता।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Memory Units Hierarchy:</strong> Bit (0 or 1) -> <strong>Nibble (4 bits)</strong> -> <strong>Byte (8 bits)</strong> -> KB (1024 B) -> MB (1024 KB) -> GB (1024 MB) -> TB (1024 GB) -> PB (1024 TB) -> EB (1024 PB) -> ZB (1024 EB) -> YB (1024 ZB).</span>
                            <span class="lang-hi"><strong>मेमोरी इकाइयों का क्रम:</strong> 1 निबल = 4 बिट्स; 1 बाइट = 8 बिट्स; 1 KB = 1024 बाइट्स; 1 MB = 1024 KB; 1 GB = 1024 MB; 1 TB = 1024 GB; 1 पेटाबाइट (PB) = 1024 TB; 1 एक्सबाइट (EB) = 1024 PB।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> 1 Nibble is exactly 4 bits (half byte); 1 Byte is 8 bits; the sequence of the DIKW hierarchy is Data -> Information -> Knowledge -> Wisdom!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1 निबल में ठीक 4 बिट्स (आधा बाइट) होते हैं; 1 बाइट में 8 बिट्स होते हैं; DIKW का सही क्रम है: डेटा -> सूचना -> ज्ञान -> प्रज्ञा!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Relational Databases, RDBMS & SQL -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-database" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Relational Databases &amp; SQL</span>
                    <span class="lang-hi">2. रिलेशनल डेटाबेस (RDBMS), कीज़ एवं SQL</span>
                </h4>
                <span class="mindmap-node-tag">E.F. Codd 1970 • Keys • ACID</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">RDBMS Concepts &amp; SQL Sublanguages</span>
                        <span class="lang-hi">RDBMS शब्दावली एवं SQL के प्रकार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Dr. E.F. Codd</strong> (1970, Relational Model)</span>
                        <span class="mindmap-chip"><strong>Tuple</strong> (Row / Record)</span>
                        <span class="mindmap-chip"><strong>Attribute</strong> (Column / Field)</span>
                        <span class="mindmap-chip"><strong>Cardinality</strong> (Number of Rows)</span>
                        <span class="mindmap-chip"><strong>Degree</strong> (Number of Columns)</span>
                        <span class="mindmap-chip"><strong>Primary Key</strong> (Unique &amp; Non-Null)</span>
                        <span class="mindmap-chip"><strong>Foreign Key</strong> (Referential Integrity)</span>
                        <span class="mindmap-chip"><strong>DDL / DML / DCL / TCL</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">RDBMS Terminology &amp; ACID Properties</span>
                        <span class="lang-hi">RDBMS तकनीकी शब्द एवं ACID गुण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>RDBMS Terminology:</strong> Proposed by Dr. Edgar F. Codd (IBM, 1970). <strong>Table</strong> = Relation. <strong>Row</strong> = Tuple. <strong>Column</strong> = Attribute. <strong>Cardinality</strong> = Total count of rows (tuples). <strong>Degree</strong> = Total count of columns (attributes).</span>
                            <span class="lang-hi"><strong>RDBMS शब्दावली (ई.एफ. कॉड 1970):</strong> टेबल = रिलेशन; पंक्ति (Row) = टपल (Tuple); स्तंभ (Column) = एट्रिब्यूट; पंक्तियों की कुल संख्या = <strong>कार्डिनैलिटी</strong>; स्तंभों की कुल संख्या = <strong>डिग्री</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Database Keys:</strong> <strong>Primary Key:</strong> Minimal set of attributes uniquely identifying each tuple; cannot contain NULL. <strong>Foreign Key:</strong> References the Primary Key of another table, enforcing <strong>Referential Integrity</strong>.</span>
                            <span class="lang-hi"><strong>डेटाबेस कीज़ (Keys):</strong> <strong>प्राइमरी की:</strong> विशिष्ट एवं नॉन-नल (Non-Null) पहचानकर्ता। <strong>फॉरेन की:</strong> दूसरी टेबल की प्राइमरी की को संदर्भित करती है और 'रेफरेंशियल इंटीग्रिटी' बनाए रखती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>SQL Commands &amp; ACID:</strong> <strong>DDL:</strong> CREATE, ALTER, DROP, TRUNCATE. <strong>DML:</strong> SELECT, INSERT, UPDATE, DELETE. <strong>ACID:</strong> <strong>A</strong>tomicity (all or nothing), <strong>C</strong>onsistency, <strong>I</strong>solation, <strong>D</strong>urability (permanent committed writes).</span>
                            <span class="lang-hi"><strong>SQL एवं ACID:</strong> DDL (CREATE, DROP, TRUNCATE); DML (SELECT, INSERT, UPDATE); <strong>ACID गुण:</strong> एटॉमीसिटी (पूर्ण या शून्य), कंसिस्टेंसी, आइसोलेशन, ड्यूरेबिलिटी।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> In RDBMS, Cardinality is the number of rows and Degree is the number of columns; Primary Key cannot be NULL; Foreign Key enforces Referential Integrity!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> RDBMS में पंक्तियों की संख्या 'कार्डिनैलिटी' और स्तंभों की संख्या 'डिग्री' कहलाती है; प्राइमरी की कभी शून्य (NULL) नहीं हो सकती!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Cloud Computing Models: IaaS, PaaS, SaaS -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cloud" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Cloud Computing SPI Models</span>
                    <span class="lang-hi">3. क्लाउड कंप्यूटिंग SPI मॉडल एवं परिनियोजन</span>
                </h4>
                <span class="mindmap-node-tag">IaaS • PaaS • SaaS • MeghRaj</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Service &amp; Deployment Models</span>
                        <span class="lang-hi">सेवा मॉडल एवं परिनियोजन श्रेणियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>IaaS</strong> (Infrastructure: AWS EC2, Azure VMs)</span>
                        <span class="mindmap-chip"><strong>PaaS</strong> (Platform: Google App Engine, Heroku)</span>
                        <span class="mindmap-chip"><strong>SaaS</strong> (Software: Gmail, Office 365, Drive)</span>
                        <span class="mindmap-chip"><strong>Public vs Private vs Hybrid Cloud</strong></span>
                        <span class="mindmap-chip"><strong>MeghRaj</strong> (National GI Cloud, NIC)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">SPI Responsibilities &amp; Government Cloud</span>
                        <span class="lang-hi">SPI दायित्व विभाजन एवं सरकारी क्लाउड</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The SPI Delivery Models:</strong> <strong>IaaS (Infrastructure as a Service):</strong> Provides raw compute, storage, virtual machines, and networking; user manages OS, runtime, and apps (AWS EC2). <strong>PaaS (Platform as a Service):</strong> Provides hardware, OS, and runtime environment; developer only writes and deploys application code (Google App Engine). <strong>SaaS (Software as a Service):</strong> Ready-to-use software delivered over web browser; vendor manages everything (Gmail, Office 365, Dropbox).</span>
                            <span class="lang-hi"><strong>SPI सेवा मॉडल:</strong> <strong>IaaS (इन्फ्रास्ट्रक्चर):</strong> वर्चुअल सर्वर व स्टोरेज रेंट पर; यूजर OS व सॉफ्टवेयर खुद डालता है (AWS EC2)। <strong>PaaS (प्लेटफॉर्म):</strong> डेवलपर हेतु रनटाइम व डेटाबेस तैयार; केवल कोड लिखना होता है। <strong>SaaS (सॉफ्टवेयर):</strong> पूर्ण रूप से तैयार सॉफ्टवेयर जो ब्राउज़र से चलता है (Gmail, गूगल ड्राइव)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>MeghRaj (GI Cloud):</strong> Government of India's sovereign cloud computing initiative established by NIC to accelerate delivery of e-services across government departments and optimize ICT spending.</span>
                            <span class="lang-hi"><strong>मेघराज (MeghRaj):</strong> NIC द्वारा संचालित भारत सरकार की संप्रभु क्लाउड पहल, जो सरकारी विभागों को तीव्र, सुरक्षित व सस्ती क्लाउड होस्टिंग प्रदान करती है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Gmail and Google Drive are examples of SaaS; AWS EC2 is IaaS; MeghRaj is the national cloud initiative of Government of India!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> जीमेल (Gmail) और गूगल ड्राइव 'SaaS' के उदाहरण हैं; AWS EC2 'IaaS' है; 'मेघराज' भारत सरकार का राष्ट्रीय क्लाउड है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Cyber Security Threats & Malware Taxonomy -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-bug" style="color: #d97706;"></i>
                    <span class="lang-en">4. Malware Taxonomy &amp; Attacks</span>
                    <span class="lang-hi">4. मैलवेयर का वर्गीकरण एवं साइबर हमले</span>
                </h4>
                <span class="mindmap-node-tag">Virus • Worm • Ransomware</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Malware Categories &amp; Attack Vectors</span>
                        <span class="lang-hi">मैलवेयर की श्रेणियां एवं हमले</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Virus</strong> (Host File Dependent, Human Run)</span>
                        <span class="mindmap-chip"><strong>Worm</strong> (Self-Replicating, Standalone Net)</span>
                        <span class="mindmap-chip"><strong>Trojan Horse</strong> (Disguised Legitimate Software)</span>
                        <span class="mindmap-chip"><strong>Ransomware</strong> (File Encryption Extortion, WannaCry)</span>
                        <span class="mindmap-chip"><strong>Spyware &amp; Keylogger</strong> (Activity Tracking)</span>
                        <span class="mindmap-chip"><strong>Rootkit</strong> (Concealed Kernel Privileges)</span>
                        <span class="mindmap-chip"><strong>DDoS Attack</strong> (Botnet Zombie Flood)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Crucial Differences: Virus vs Worm vs Trojan</span>
                        <span class="lang-hi">वायरस बनाम वॉर्म बनाम ट्रोजन में मुख्य अंतर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Virus vs Worm:</strong> <strong>Computer Virus:</strong> Malicious code that attaches itself to legitimate executable files (.exe, .docm); CANNOT spread without human intervention (user must execute infected file). <strong>Computer Worm:</strong> Standalone self-replicating program that exploits network vulnerabilities to spread automatically from computer to computer without ANY human action, consuming network bandwidth (e.g. Morris Worm 1988).</span>
                            <span class="lang-hi"><strong>वायरस बनाम वॉर्म:</strong> <strong>कंप्यूटर वायरस:</strong> अन्य वैध फाइलों से जुड़ता है; मानव द्वारा फाइल खोलने पर ही फैलता है। <strong>कंप्यूटर वॉर्म:</strong> स्वतंत्र प्रोग्राम जो बिना किसी मानवीय हस्तक्षेप के नेटवर्क के माध्यम से स्वतः फैलता है और बैंडविड्थ चोक कर देता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Trojan Horse &amp; Ransomware:</strong> <strong>Trojan:</strong> Masquerades as useful, safe software (e.g. free game, utility) but contains hidden malicious payload; does not self-replicate. <strong>Ransomware:</strong> Cryptovirological attack that encrypts victim's files and demands ransom in cryptocurrency for decryption key (WannaCry, NotPetya).</span>
                            <span class="lang-hi"><strong>ट्रोजन हॉर्स एवं रैंसमवेयर:</strong> <strong>ट्रोजन:</strong> उपयोगी सॉफ्टवेयर (गेम आदि) का मुखौटा पहनकर कंप्यूटर में घुसता है; स्वयं की प्रति नहीं बनाता। <strong>रैंसमवेयर:</strong> उपयोगकर्ता की फाइलों को लॉक (एन्क्रिप्ट) कर बिटकॉइन में फिरौती मांगता है (WannaCry)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Worms self-replicate without human action; Viruses require human execution; Trojans disguise themselves as legitimate software; WannaCry is Ransomware!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> वॉर्म बिना मानवीय मदद के स्वतः फैलता है; वायरस को मानव द्वारा चलाने की जरूरत होती है; ट्रोजन उपयोगी सॉफ्टवेयर का भेष बनाता है; WannaCry रैंसमवेयर है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Cryptography, Digital Signatures & PKI -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-key" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Cryptography &amp; Signatures</span>
                    <span class="lang-hi">5. क्रिप्टोग्राफी, डिजिटल हस्ताक्षर एवं PKI</span>
                </h4>
                <span class="mindmap-node-tag">Symmetric vs Asymmetric • RSA</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Encryption Types &amp; Standards</span>
                        <span class="lang-hi">एन्क्रिप्शन के प्रकार एवं मानक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Symmetric Key</strong> (1 Shared Secret Key, AES/DES)</span>
                        <span class="mindmap-chip"><strong>Asymmetric Key</strong> (Key Pair: Public &amp; Private)</span>
                        <span class="mindmap-chip"><strong>RSA Algorithm</strong> (Rivest, Shamir, Adleman 1977)</span>
                        <span class="mindmap-chip"><strong>Digital Signature</strong> (Sender's Private Key)</span>
                        <span class="mindmap-chip"><strong>Hash Functions</strong> (SHA-256, One-Way Digest)</span>
                        <span class="mindmap-chip"><strong>PKI &amp; CCA</strong> (Section 17 IT Act, 2000)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Asymmetric Mechanics &amp; Digital Signatures</span>
                        <span class="lang-hi">असममित एन्क्रिप्शन एवं डिजिटल हस्ताक्षर कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Symmetric vs Asymmetric Encryption:</strong> <strong>Symmetric:</strong> Single shared secret key used for both encryption and decryption (AES, DES); ultra-fast but risky key exchange. <strong>Asymmetric (Public Key):</strong> Uses mathematically linked pair of keys: <strong>Public Key</strong> (freely distributed to encrypt messages) and <strong>Private Key</strong> (kept strictly secret by owner to decrypt messages). Examples: RSA, ECC.</span>
                            <span class="lang-hi"><strong>सममित बनाम असममित एन्क्रिप्शन:</strong> <strong>सममित (Symmetric):</strong> एक ही गुप्त कुंजी से एन्क्रिप्शन और डिक्रिप्शन (AES)। <strong>असममित (Asymmetric):</strong> दो कुंजियों का जोड़ा; <strong>पब्लिक की</strong> से संदेश लॉक किया जाता है और केवल प्राप्तकर्ता की <strong>प्राइवेट की</strong> से ही खुलता है (RSA)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Digital Signature Mechanics:</strong> Provides Authentication, Integrity, and Non-Repudiation. Created by taking cryptographic hash (SHA-256) of document and encrypting it with the <strong>Sender's Private Key</strong>. Verified by recipient using sender's Public Key.</span>
                            <span class="lang-hi"><strong>डिजिटल हस्ताक्षर कार्यप्रणाली:</strong> प्रेषक के <strong>प्राइवेट की</strong> द्वारा संदेश के हैश को एन्क्रिप्ट कर बनता है; प्राप्तकर्ता प्रेषक की <strong>पब्लिक की</strong> से इसकी प्रामाणिकता जांचता है। कानूनी रूप से मान्य।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Asymmetric encryption uses two keys (Public &amp; Private); Digital Signature is created using sender's Private Key and verified with their Public Key!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> असममित एन्क्रिप्शन में दो कुंजियां (पब्लिक व प्राइवेट) होती हैं; डिजिटल हस्ताक्षर प्रेषक की 'प्राइवेट की' से बनता है और 'पब्लिक की' से जांचा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Cyber Crime Reporting, CERT-In & Helpline 1930 -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-alt" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Cyber Laws, CERT-In &amp; 1930</span>
                    <span class="lang-hi">6. साइबर कानून, CERT-In एवं हेल्पलाइन 1930</span>
                </h4>
                <span class="mindmap-node-tag">CERT-In • Helpline 1930 • UP Grid</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Agencies &amp; Emergency Helplines</span>
                        <span class="lang-hi">सुरक्षा एजेंसियां एवं आपातकालीन हेल्पलाइन</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>IT Act, 2000</strong> (Enacted 17 Oct 2000)</span>
                        <span class="mindmap-chip"><strong>CERT-In</strong> (National Response, Sec 70B)</span>
                        <span class="mindmap-chip"><strong>NCIIPC</strong> (Critical Infrastructure, Sec 70)</span>
                        <span class="mindmap-chip"><strong>Cyber Helpline 1930</strong> (Financial Fraud, CFCFRMS)</span>
                        <span class="mindmap-chip"><strong>cybercrime.gov.in</strong> (National Portal)</span>
                        <span class="mindmap-chip"><strong>UP Cyber Thanas</strong> (All 75 UP Districts)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">National Agencies &amp; Golden Hour Intervention</span>
                        <span class="lang-hi">राष्ट्रीय एजेंसियां एवं गोल्डन ऑवर वित्तीय सुरक्षा</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>CERT-In &amp; NCIIPC:</strong> <strong>CERT-In:</strong> National nodal agency under Section 70B of IT Act for computer security incident response. <strong>NCIIPC:</strong> Protects Critical Information Infrastructure (power, banking, telecom) under Section 70.</span>
                            <span class="lang-hi"><strong>CERT-In एवं NCIIPC:</strong> CERT-In साइबर हमलों से निपटने वाली राष्ट्रीय नोडल एजेंसी है (धारा 70B)। NCIIPC देश के महत्वपूर्ण बुनियादी ढांचे (पावर ग्रिड, बैंक) की रक्षा करता है (धारा 70)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Cyber Helpline 1930 (Golden Hour):</strong> Citizen Financial Cyber Fraud Reporting and Management System (CFCFRMS). Dialing <strong>1930</strong> immediately after financial cyber fraud alerts banks to freeze siphoned funds within the critical "Golden Hour".</span>
                            <span class="lang-hi"><strong>साइबर वित्तीय हेल्पलाइन 1930:</strong> ऑनलाइन बैंकिंग धोखाधड़ी होने पर तत्काल <strong>1930</strong> डायल करने पर 'गोल्डन ऑवर' के भीतर बैंकों से संपर्क कर ठगी की रकम को तत्काल फ्रीज करवा दिया जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Uttar Pradesh Cyber Thana Grid:</strong> Uttar Pradesh established dedicated Cyber Crime Police Stations across all 18 police ranges and 75 districts equipped with digital forensics labs to prosecute cyber criminals.</span>
                            <span class="lang-hi"><strong>उप्र साइबर थाना ग्रिड:</strong> उत्तर प्रदेश के सभी 75 जिलों और 18 पुलिस परिक्षेत्रों में साइबर अपराध थानों की स्थापना की गई है, जो डिजिटल फोरेंसिक लैब से सुसज्जित हैं।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> National Cyber Fraud Helpline number is 1930; CERT-In is established under Section 70B of IT Act 2000; NCIIPC protects Critical Infrastructure under Section 70!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> साइबर वित्तीय धोखाधड़ी हेल्पलाइन नंबर '1930' है; CERT-In आईटी एक्ट की धारा 70B के तहत कार्य करता है; NCIIPC धारा 70 के तहत महत्वपूर्ण ढांचों की रक्षा करता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
