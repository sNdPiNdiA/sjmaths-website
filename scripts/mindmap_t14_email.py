# Topic 14: E-Mail Creation, Operation & Protocols
mm_t14 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Electronic Mail (E-Mail) Architecture &amp; Operations</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: इलेक्ट्रॉनिक मेल (ई-मेल) वास्तुकला, प्रोटोकॉल एवं सुरक्षा</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Ray Tomlinson 1971 • Protocols (SMTP 25/587, POP3 110, IMAP 143) • Header Anatomy (To, Cc, Bcc) • Folders (Spam/Outbox) • Phishing &amp; SPF/DKIM • NIC Gov Email</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • रे टॉमलिंसन 1971 • प्रोटोकॉल (SMTP, POP3, IMAP) • हेडर (To, Cc, Bcc) • फोल्डर्स (स्पैम/आउटबॉक्स) • फिशिंग व SPF/DKIM • NIC सरकारी ईमेल</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-envelope-open-text"></i>
            <span class="lang-en">Electronic Mail (E-Mail) Communication Ecosystem</span>
            <span class="lang-hi">इलेक्ट्रॉनिक मेल (ई-मेल) संचार पारिस्थितिकी</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: History, Inventors & Address Syntax -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-at" style="color: #059669;"></i>
                    <span class="lang-en">1. History &amp; Address Syntax</span>
                    <span class="lang-hi">1. इतिहास, आविष्कारक एवं पता संरचना</span>
                </h4>
                <span class="mindmap-node-tag">Ray Tomlinson 1971 • @ Sign</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Pioneers &amp; Syntax Structure</span>
                        <span class="lang-hi">अग्रणी व्यक्ति एवं पता संरचना</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Ray Tomlinson</strong> (1971, Father of Email)</span>
                        <span class="mindmap-chip"><strong>@ Symbol</strong> (Separator Choice)</span>
                        <span class="mindmap-chip"><strong>Username</strong> (Local Part, Max 64 Chars)</span>
                        <span class="mindmap-chip"><strong>Domain Name</strong> (Host Server, e.g. nic.in)</span>
                        <span class="mindmap-chip"><strong>Case-Insensitive</strong> (Letters 0-9 . _ -)</span>
                        <span class="mindmap-chip"><strong>Shiva Ayyadurai</strong> (1982 Copyright)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Inventors &amp; Syntactical Rules</span>
                        <span class="lang-hi">आविष्कारक एवं वाक्यविन्यास (Syntax) नियम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ray Tomlinson (1971):</strong> American computer programmer credited as the <strong>Father of Modern Email</strong>. Implemented the first ARPANET network email system (SNDMSG) and chose the <strong>`@` (at sign)</strong> symbol to separate the user mailbox from the host computer name. Sent first test email to himself.</span>
                            <span class="lang-hi"><strong>रे टॉमलिंसन (1971):</strong> आधुनिक ईमेल के जनक। ARPANET पर पहली बार नेटवर्क ईमेल भेजा तथा यूजर और होस्ट सर्वर को अलग करने हेतु <strong>`@` (एट-द-रेट)</strong> चिह्न का चयन किया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Email Address Syntax:</strong> Standard structure: <code>username@domain.extension</code> (e.g. <code>candidate@upsssc.gov.in</code>). <strong>Username (Local-part):</strong> Up to 64 characters, case-insensitive, allows alphanumeric characters and select symbols (<code>.</code>, <code>_</code>, <code>-</code>). <strong>Domain Name:</strong> Identifies the destination mail exchange server. Spaces are strictly prohibited!</span>
                            <span class="lang-hi"><strong>ईमेल पते की संरचना:</strong> <code>username@domain.extension</code>। <strong>यूज़रनेम:</strong> 64 अक्षरों तक, केस-इनसेंसिटिव (अक्षर, अंक, डॉट, अंडरस्कोर)। <strong>@:</strong> विभाजक। <strong>डोमेन:</strong> मेल सर्वर का नाम। ईमेल पते में रिक्त स्थान (स्पेस) पूरी तरह वर्जित है!</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ray Tomlinson invented network email and introduced the @ symbol in 1971; email addresses are case-insensitive and cannot contain spaces!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> रे टॉमलिंसन ने 1971 में ईमेल और @ चिह्न का आविष्कार किया; ईमेल पते में रिक्त स्थान (स्पेस) नहीं हो सकता और यह केस-इनसेंसिटिव होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: The Three Core Email Protocols: SMTP, POP3, IMAP -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-exchange-alt" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Core Protocols: SMTP, POP3, IMAP</span>
                    <span class="lang-hi">2. प्रमुख ईमेल प्रोटोकॉल: SMTP, POP3, IMAP</span>
                </h4>
                <span class="mindmap-node-tag">Push vs Pull • Port 25 • Port 143</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Protocols &amp; Standard Ports</span>
                        <span class="lang-hi">प्रोटोकॉल एवं मानक पोर्ट संख्याएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>SMTP</strong> (Send Outgoing, Push Protocol)</span>
                        <span class="mindmap-chip"><strong>SMTP Ports:</strong> 25 (Plain), 587 (TLS), 465 (SSL)</span>
                        <span class="mindmap-chip"><strong>POP3</strong> (Download/Delete, Pull Protocol)</span>
                        <span class="mindmap-chip"><strong>POP3 Ports:</strong> 110 (Plain), 995 (SSL)</span>
                        <span class="mindmap-chip"><strong>IMAP4</strong> (Sync Multi-Device, Pull Protocol)</span>
                        <span class="mindmap-chip"><strong>IMAP Ports:</strong> 143 (Plain), 993 (SSL)</span>
                        <span class="mindmap-chip"><strong>MIME</strong> (Multimedia Attachments)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Operational Protocol Differences</span>
                        <span class="lang-hi">प्रोटोकॉल कार्यप्रणाली एवं मुख्य अंतर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>SMTP (Simple Mail Transfer Protocol):</strong> Push protocol used to <strong>transmit / send</strong> outgoing emails from a client to a mail server, and between intermediate mail servers. Port <strong>25</strong> (unencrypted), Port <strong>587</strong> (modern client submission with STARTTLS), Port <strong>465</strong> (SMTPS).</span>
                            <span class="lang-hi"><strong>SMTP (सिंपल मेल ट्रांसफर प्रोटोकॉल):</strong> ईमेल <strong>भेजने (Send)</strong> हेतु प्रयुक्त पुश (Push) प्रोटोकॉल। क्लाइंट से सर्वर तक व सर्वरों के मध्य ईमेल भेजता है। पोर्ट <strong>25</strong> (साधारण) व <strong>587</strong> (सुरक्षित TLS)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>POP3 (Post Office Protocol v3):</strong> Pull protocol used to <strong>retrieve / download</strong> emails from server to a single local device. By default, downloads messages to local hard drive and deletes them from server. Port <strong>110</strong> (plain), Port <strong>995</strong> (SSL).</span>
                            <span class="lang-hi"><strong>POP3 (पोस्ट ऑफिस प्रोटोकॉल):</strong> सर्वर से ईमेल <strong>डाउनलोड</strong> करने वाला पुल (Pull) प्रोटोकॉल। ईमेल को स्थानीय कंप्यूटर में डाउनलोड कर सर्वर से हटा देता है (एकल उपकरण मॉडल)। पोर्ट <strong>110</strong> व <strong>995</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>IMAP4 (Internet Message Access Protocol):</strong> Advanced pull protocol for multi-device synchronization. Emails remain stored on remote server; changes (read status, folders) sync seamlessly in real-time across smartphone, tablet, and PC. Port <strong>143</strong> (plain), Port <strong>993</strong> (SSL).</span>
                            <span class="lang-hi"><strong>IMAP4 (इंटरनेट मैसेज एक्सेस प्रोटोकॉल):</strong> आधुनिक मल्टी-डिवाइस सिंक्रोनाइज़ेशन प्रोटोकॉल। ईमेल सर्वर पर ही रहते हैं; फोन, लैपटॉप व ऑफिस PC पर एक साथ रियल-टाइम सिंक। पोर्ट <strong>143</strong> व <strong>993</strong>।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> SMTP is used to SEND emails (Port 25/587); POP3 downloads and deletes from server (Port 110); IMAP keeps emails synced on the server (Port 143/993)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ईमेल भेजने हेतु SMTP (पोर्ट 25) प्रयुक्त होता है; ईमेल डाउनलोड करने हेतु POP3 (पोर्ट 110) व सर्वर पर सिंक रखने हेतु IMAP (पोर्ट 143) प्रयुक्त होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Header Anatomy: To, Cc, Bcc & Subject -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-heading" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Email Header Anatomy</span>
                    <span class="lang-hi">3. ईमेल हेडर संरचना: To, Cc, Bcc</span>
                </h4>
                <span class="mindmap-node-tag">Carbon Copy • Blind Copy • MIME</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Header Fields &amp; Extensions</span>
                        <span class="lang-hi">हेडर फील्ड्स एवं विस्तार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>To:</strong> Primary Target Recipients</span>
                        <span class="mindmap-chip"><strong>Cc:</strong> Carbon Copy (Visible to All)</span>
                        <span class="mindmap-chip"><strong>Bcc:</strong> Blind Carbon Copy (Hidden)</span>
                        <span class="mindmap-chip"><strong>Subject:</strong> Message Summary Line</span>
                        <span class="mindmap-chip"><strong>From &amp; Reply-To:</strong> Sender Identity</span>
                        <span class="mindmap-chip"><strong>MIME:</strong> Non-ASCII Attachments</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Critical Differences: To vs Cc vs Bcc</span>
                        <span class="lang-hi">To, Cc एवं Bcc में महत्वपूर्ण अंतर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>To (Primary Recipient):</strong> Main person(s) for whom message is directly intended and from whom action or response is expected. All recipients can see addresses in To and Cc.</span>
                            <span class="lang-hi"><strong>To (मुख्य प्राप्तकर्ता):</strong> वह व्यक्ति जिससे कार्य या उत्तर अपेक्षित है। To और Cc में मौजूद सभी लोग एक-दूसरे का ईमेल पता देख सकते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cc (Carbon Copy):</strong> Secondary recipients kept informed for courtesy/awareness without expecting direct action. All recipients in To, Cc, and Bcc can see who is in the Cc list.</span>
                            <span class="lang-hi"><strong>Cc (कार्बन कॉपी):</strong> सूचना के उद्देश्य से प्रतिलिपि भेजना। To और Cc में शामिल सभी प्राप्तकर्ताओं को पता होता है कि ईमेल किसे-किसे भेजा गया है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bcc (Blind Carbon Copy):</strong> Discreet recipients whose identity and email addresses are <strong>completely hidden and invisible</strong> from all other recipients in To and Cc. Protects recipient privacy in mass mailings and prevents spam harvester exposure.</span>
                            <span class="lang-hi"><strong>Bcc (ब्लाइंड कार्बन कॉपी):</strong> इसमें दर्ज प्राप्तकर्ताओं के नाम और ईमेल पते <strong>पूरी तरह गोपनीय (अदृश्य)</strong> रहते हैं; To और Cc वाले नहीं जान पाते कि Bcc में कौन है। गोपनीयता बनाए रखने हेतु उपयोगी।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bcc recipients are concealed from everyone else in the email; MIME protocol enables sending attachments (images, PDFs, audio) with emails!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> Bcc में शामिल ईमेल पते अन्य सभी प्राप्तकर्ताओं से छिपे रहते हैं; ईमेल में अटैचमेंट (PDF, चित्र आदि) भेजने हेतु MIME प्रोटोकॉल प्रयुक्त होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Email Folders, Storage & Daily Operations -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-folder-open" style="color: #d97706;"></i>
                    <span class="lang-en">4. Folders &amp; Operations</span>
                    <span class="lang-hi">4. फोल्डर संरचना एवं दैनिक मेल संचालन</span>
                </h4>
                <span class="mindmap-node-tag">Inbox • Outbox • Drafts • Spam</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Standard Mailbox Folders</span>
                        <span class="lang-hi">मानक मेलबॉक्स फोल्डर्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Inbox</strong> (Incoming Received Mails)</span>
                        <span class="mindmap-chip"><strong>Outbox</strong> (Pending Transit Queue)</span>
                        <span class="mindmap-chip"><strong>Sent</strong> (Confirmed Transmitted Mails)</span>
                        <span class="mindmap-chip"><strong>Drafts</strong> (Unsent Composed Mails)</span>
                        <span class="mindmap-chip"><strong>Spam / Junk</strong> (Unsolicited Commercial)</span>
                        <span class="mindmap-chip"><strong>Trash / Bin</strong> (Deleted, Retained 30 Days)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Outbox vs Sent &amp; Trash Retention</span>
                        <span class="lang-hi">आउटबॉक्स बनाम सेंट एवं ट्रैश की अवधि</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Outbox vs Sent Items:</strong> <strong>Outbox:</strong> Temporary holding area for outgoing emails currently waiting to be dispatched (e.g. while network is offline). <strong>Sent Items:</strong> Permanent record of emails that have been successfully transmitted to recipient mail server.</span>
                            <span class="lang-hi"><strong>आउटबॉक्स बनाम सेंट (Sent):</strong> <strong>आउटबॉक्स (Outbox):</strong> कतारबद्ध मेल जो अभी भेजे जाने की प्रक्रिया में हैं (नेटवर्क न होने पर यहाँ रुकते हैं)। <strong>सेंट (Sent):</strong> सफलतापूर्वक भेजे जा चुके ईमेल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Drafts &amp; Trash:</strong> <strong>Drafts:</strong> Partially written or uncompleted emails automatically saved by editor. <strong>Trash/Bin:</strong> Deleted emails kept temporarily (typically for 30 days) before permanent unrecoverable deletion.</span>
                            <span class="lang-hi"><strong>ड्राफ्ट्स एवं ट्रैश:</strong> <strong>ड्राफ्ट्स (Drafts):</strong> अधूरे लिखे गए मेल जो स्वतः संचित हो जाते हैं। <strong>ट्रैश (Trash):</strong> हटाए गए मेल; प्रायः 30 दिनों बाद हमेशा के लिए नष्ट हो जाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Spam / Junk Mail:</strong> Unsolicited bulk commercial emails, marketing blasts, or suspected phishing messages filtered automatically by Bayesian machine learning filters.</span>
                            <span class="lang-hi"><strong>स्पैम (Spam / Junk):</strong> अवांछित बल्क विज्ञापन या संदिग्ध धोखाधड़ी वाले ईमेल, जिन्हें फिल्टर द्वारा अलग फोल्डर में डाल दिया जाता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Outbox holds unsent emails waiting for network connection; Sent folder holds confirmed delivered emails; Trash retains deleted items for 30 days!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> आउटबॉक्स में वे मेल होते हैं जो भेजे जा रहे हैं लेकिन नेटवर्क न होने से अटके हैं; सेंट में भेजे जा चुके मेल होते हैं; ट्रैश में 30 दिन तक डिलीटेड मेल रहते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Email Security, Phishing & SPF/DKIM -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-virus" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Email Security &amp; Phishing</span>
                    <span class="lang-hi">5. ईमेल सुरक्षा, फिशिंग एवं प्रमाणीकरण मानक</span>
                </h4>
                <span class="mindmap-node-tag">Phishing • SPF • DKIM • DMARC</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Threats &amp; Authentication Standards</span>
                        <span class="lang-hi">साइबर खतरे एवं प्रमाणीकरण मानक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Phishing</strong> (Deceptive Credential Theft)</span>
                        <span class="mindmap-chip"><strong>Spear Phishing</strong> (Targeted Individual Attack)</span>
                        <span class="mindmap-chip"><strong>Whaling</strong> (C-Suite / Top Official Target)</span>
                        <span class="mindmap-chip"><strong>Email Spoofing</strong> (Forged From Header)</span>
                        <span class="mindmap-chip"><strong>SPF</strong> (Sender Policy Framework, DNS IP)</span>
                        <span class="mindmap-chip"><strong>DKIM</strong> (Cryptographic Digital Signature)</span>
                        <span class="mindmap-chip"><strong>DMARC</strong> (Policy Enforcement Mechanism)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Attack Vectors &amp; Verification Mechanics</span>
                        <span class="lang-hi">हमलों के प्रकार एवं सत्यापन मानक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Phishing &amp; Social Engineering:</strong> Fraudulent emails masquerading as trusted institutions (banks, government portals, IT admins) containing spoofed links designed to trick users into disclosing passwords, OTPs, or bank details. <strong>Spear Phishing:</strong> Tailored attack on specific individual. <strong>Whaling:</strong> Targeted attack on high-ranking executives.</span>
                            <span class="lang-hi"><strong>फिशिंग (Phishing):</strong> बैंक या सरकारी संस्था का झूठा भेष बनाकर पासवर्ड या बैंक विवरण चुराने वाले फर्जी ईमेल। <strong>स्पीयर फिशिंग:</strong> किसी विशिष्ट व्यक्ति को निशाना बनाना। <strong>व्हेलिंग:</strong> शीर्ष अधिकारियों या मंत्रियों को निशाना बनाना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>SPF, DKIM &amp; DMARC Triple Defense:</strong> <strong>SPF:</strong> DNS record specifying which IP addresses are authorized to send email for a domain. <strong>DKIM:</strong> Affixes cryptographic digital signature in email header to detect in-transit tampering. <strong>DMARC:</strong> Directs receiving mail servers how to reject or quarantine emails failing SPF/DKIM checks.</span>
                            <span class="lang-hi"><strong>SPF, DKIM एवं DMARC सुरक्षा त्रिमूर्ति:</strong> <strong>SPF:</strong> अधिकृत IP पतों की DNS सूची। <strong>DKIM:</strong> ईमेल हेडर में डिजिटल हस्ताक्षर जिससे रास्ते में छेड़छाड़ पकड़ी जा सके। <strong>DMARC:</strong> फर्जी मेल को सीधे ब्लॉक करने की नीति।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Phishing is fraudulent credential theft via deceptive emails; SPF and DKIM verify sender authenticity to prevent email spoofing!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> धोखाधड़ी से पासवर्ड चुराने वाले फर्जी ईमेल को 'फिशिंग' कहते हैं; ईमेल स्पूफिंग रोकने हेतु SPF व DKIM प्रमाणीकरण का प्रयोग होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: NIC Government Email & UP Official Policy -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-university" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Government Email Infrastructure</span>
                    <span class="lang-hi">6. सरकारी ईमेल अवसंरचना (NIC) एवं उप्र नीति</span>
                </h4>
                <span class="mindmap-node-tag">@gov.in • Kavach 2FA • National Policy</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Government Platforms &amp; Security</span>
                        <span class="lang-hi">सरकारी मंच एवं सुरक्षा नीतियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>NIC Email Service</strong> (@gov.in / @nic.in)</span>
                        <span class="mindmap-chip"><strong>National e-Mail Policy</strong> (2014 Mandate)</span>
                        <span class="mindmap-chip"><strong>Kavach Multi-Factor Auth</strong> (OTP Token)</span>
                        <span class="mindmap-chip"><strong>UP State Policy</strong> (Official Use Only)</span>
                        <span class="mindmap-chip"><strong>Sovereign Data Storage</strong> (In-Country DCs)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">National e-Mail Policy &amp; Security Mandates</span>
                        <span class="lang-hi">राष्ट्रीय ईमेल नीति एवं सुरक्षा निर्देश</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National e-Mail Policy (2014):</strong> Mandates that all official communications by central and state government employees in India MUST be conducted exclusively using official government email accounts provided by National Informatics Centre (<code>@gov.in</code> or <code>@nic.in</code>). Prohibits use of public commercial email services (Gmail, Yahoo) for official work.</span>
                            <span class="lang-hi"><strong>राष्ट्रीय ईमेल नीति (2014):</strong> भारत सरकार व राज्य सरकारों के सभी अधिकारियों हेतु आधिकारिक पत्राचार केवल NIC द्वारा प्रदत्त <code>@gov.in</code> या <code>@nic.in</code> ईमेल से करना अनिवार्य है। निजी ईमेल (Gmail, Yahoo) का सरकारी कार्यों में उपयोग प्रतिबंधित है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kavach Multi-Factor Authentication:</strong> Mandatory two-factor authentication (2FA) client application developed by NIC generating time-based one-time passwords (TOTP) and push notifications to protect government email accounts from unauthorized access.</span>
                            <span class="lang-hi"><strong>कवच (Kavach) बहु-चरणीय प्रमाणीकरण:</strong> NIC द्वारा विकसित टू-फैक्टर ऑथेंटिकेशन ऐप जो सरकारी ईमेल लॉगिन पर OTP टोकन उत्पन्न कर साइबर हमलों से सुरक्षा प्रदान करता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Official government emails in India use the @gov.in or @nic.in domain managed by NIC; National e-Mail Policy (2014) prohibits private commercial email for official work!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> भारत में आधिकारिक सरकारी ईमेल @gov.in व @nic.in डोमेन पर NIC द्वारा संचालित होते हैं; 2014 की राष्ट्रीय ईमेल नीति निजी मेल पर रोक लगाती है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
