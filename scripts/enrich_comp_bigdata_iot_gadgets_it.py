import os
import re

def build_big_data_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Big Data Characteristics (5 V's), Hadoop Ecosystem &amp; NoSQL</span>
    <span class="lang-hi">माइंड मैप: बिग डेटा के 5 V's लक्षण, हडूप इकोसिस्टम एवं NoSQL डेटाबेस</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Big Data Processing] --> B[5 V's Characteristics]
    A --> C[Data Classification & Formats]
    A --> D[Hadoop Distributed Ecosystem]
    A --> E[Apache Spark & In-Memory]
    A --> F[NoSQL Databases & CAP Theorem]
    A --> G[Real-World Governance in UP & India]

    B --> B1[Volume: Petabytes, Exabytes, Zettabytes]
    B --> B2[Velocity: Real-time streams, IoT, UPI, Sensor feeds]
    B --> B3[Variety: Structured, Semi-structured JSON, Unstructured video]
    B --> B4[Veracity: Trustworthiness, noise, data cleansing]
    B --> B5[Value: Business & governance actionable insights]

    C --> C1[Structured: Relational RDBMS SQL rows & columns]
    C --> C2[Semi-Structured: JSON, XML, NoSQL documents]
    C --> C3[Unstructured: CCTV footage, audio, social media posts, PDFs]

    D --> D1[HDFS: NameNode Master + DataNodes Slaves 128MB block]
    D --> D2[MapReduce: Map key-value pairs + Reduce aggregation]
    D --> D3[YARN: Resource Manager & Node Managers]

    E --> E1[Apache Spark: 100x faster in-memory processing]
    E --> E2[Core Abstraction: RDD Resilient Distributed Datasets]

    F --> F1[NoSQL: Document MongoDB, Column Cassandra, Key-Value Redis, Graph Neo4j]
    F --> F2[CAP Theorem: Consistency, Availability, Partition Tolerance]

    G --> G1[National: Aadhaar Biometric, GSTN Real-time, DigiLocker]
    G --> G2[Uttar Pradesh: Smart City ICCC Lucknow/Varanasi, CCTNS Crime Analytics]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[बिग डेटा प्रोसेसिंग] --> B[बिग डेटा के 5 V's लक्षण]
    A --> C[डेटा का वर्गीकरण एवं प्रारूप]
    A --> D[हडूप वितरित इकोसिस्टम]
    A --> E[अपाचे स्पार्क एवं इन-मेमोरी कंप्यूटिंग]
    A --> F[NoSQL डेटाबेस एवं CAP प्रमेय]
    A --> G[भारत व उत्तर प्रदेश में ई-गवर्नेंस अनुप्रयोग]

    B --> B1[वॉल्यूम Volume: पेटाबाइट, एक्साबाइट, जेटाबाइट आकार]
    B --> B2[वेलोसिटी Velocity: रीयल-टाइम प्रवाह, UPI, सेंसर डेटा]
    B --> B3[वैरायटी Variety: संरचित, अर्ध-संरचित JSON, असंरचित वीडियो]
    B --> B4[वेरासिटी Veracity: डेटा की सत्यता एवं शुद्धता]
    B --> B5[वैल्यू Value: विश्लेषण से उपयोगी निष्कर्ष]

    C --> C1[संरचित: रिलेशनल SQL टेबल पंक्तियाँ व कॉलम]
    C --> C2[अर्ध-संरचित: JSON, XML, NoSQL दस्तावेज]
    C --> C3[असंरचित: सीसीटीवी वीडियो, ऑडियो, सोशल मीडिया पोस्ट]

    D --> D1[HDFS: नेम-नोड मास्टर + डेटा-नोड्स 128 MB ब्लॉक]
    D --> D2[मैपरिड्यूस: मैप की-वैल्यू + रिड्यूस संक्षेपण]
    D --> D3[YARN: संसाधन प्रबंधन तंत्र]

    E --> E1[अपाचे स्पार्क: 100 गुना तीव्र इन-मेमोरी प्रोसेसिंग]
    E --> E2[मूल संरचना: RDD रेजिलिएंट डिस्ट्रीब्यूटेड डेटासेट]

    F --> F1[NoSQL: डॉक्यूमेंट मोंगोDB, कॉलम कैसेंड्रा, की-वैल्यू रेडिस, ग्राफ नियो4j]
    F --> F2[CAP प्रमेय: निरंतरता, उपलब्धता, विभाजन सहिष्णुता]

    G --> G1[राष्ट्रीय: आधार बायोमेट्रिक, GSTN पोर्टल, डिजिलॉकर]
    G --> G2[उत्तर प्रदेश: स्मार्ट सिटी ICCC लखनऊ/वाराणसी, CCTNS पुलिसिंग]
    </div>
  </div>
</div>

<!-- Card 2: 5 V's & Data Types -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Definition, 5 V's Characteristics &amp; Types of Big Data</span>
    <span class="lang-hi">1. बिग डेटा की परिभाषा, 5 V's लक्षण एवं डेटा के प्रकार</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Definition of Big Data:</strong>
          <br>&bull; Extremely large, complex, and rapidly growing datasets that cannot be captured, stored, managed, or analyzed using traditional Relational Database Management Systems (RDBMS).
          <br>&bull; Term popularized in the late 1990s by John Mashey (SGI); formal framework of 3 V's defined by analyst <strong>Doug Laney (2001)</strong> at Gartner, later expanded to the <strong>5 V's</strong>.</span>
        <span class="lang-hi"><strong>बिग डेटा की परिभाषा:</strong>
          <br>&bull; डेटा का वह अत्यंत विशाल, तीव्र गति से बढ़ने वाला और विविधतापूर्ण संग्रह, जिसे पारंपरिक रिलेशनल डेटाबेस (RDBMS जैसे SQL Server, Oracle) द्वारा संग्रहीत, प्रबंधित या विश्लेषित नहीं किया जा सकता।
          <br>&bull; 2001 में गार्टनर के विश्लेषक <strong>डग लेसी (Doug Laney)</strong> ने इसके 3 V's मॉडल को प्रतिपादित किया था, जो बाद में <strong>5 V's</strong> के रूप में प्रसिद्ध हुआ।</span>
      </li>
    </ul>

    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">The 5 V's</span><span class="lang-hi">5 V's लक्षण</span></th>
          <th><span class="lang-en">Core Definition</span><span class="lang-hi">मूल परिभाषा</span></th>
          <th><span class="lang-en">Practical Examples</span><span class="lang-hi">व्यावहारिक उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>1. Volume (विशालता)</strong></td>
          <td><span class="lang-en">The astronomical quantity of generated and stored data, scaling from Terabytes (TB) &rarr; Petabytes (PB) &rarr; Exabytes (EB) &rarr; Zettabytes (ZB).</span><span class="lang-hi">डेटा का अभूतपूर्व आकार; टेराबाइट से बढ़कर पेटाबाइट, एक्साबाइट और जेटाबाइट में पहुंचना।</span></td>
          <td>Aadhaar biometric database (1.4+ billion records), Walmart transactions, YouTube video archives</td>
        </tr>
        <tr>
          <td><strong>2. Velocity (गति)</strong></td>
          <td><span class="lang-en">The astonishing speed at which new data is generated, transmitted, and needs to be processed in real-time or near real-time.</span><span class="lang-hi">डेटा उत्पन्न होने और उसके विश्लेषण की तीव्र गति (मिलीसेकंड में निर्णय)।</span></td>
          <td>UPI payments, stock exchange trading feeds, Formula 1 telemetry, Twitter/X posts feed</td>
        </tr>
        <tr>
          <td><strong>3. Variety (विविधता)</strong></td>
          <td><span class="lang-en">The diverse forms and formats of incoming data: Structured (tables), Semi-structured (JSON, XML), and Unstructured (video, audio).</span><span class="lang-hi">डेटा के विविध प्रारूप: संरचित (तालिकाएं), अर्ध-संरचित (JSON/XML), एवं असंरचित (वीडियो, चित्र, पीडीएफ)।</span></td>
          <td>Emails, WhatsApp voice notes, CCTV surveillance video, IoT sensor telemetry, hospital MRI scans</td>
        </tr>
        <tr>
          <td><strong>4. Veracity (सत्यता / गुणवत्ता)</strong></td>
          <td><span class="lang-en">The trustworthiness, quality, accuracy, and reliability of the data. Dirty, duplicate, or noisy data requires scrubbing.</span><span class="lang-hi">डेटा की विश्वसनीयता और प्रामाणिकता। अपूर्ण, फर्जी या त्रुटिपूर्ण डेटा को साफ (Cleaning) करना।</span></td>
          <td>Spam social reviews, incomplete GPS breadcrumbs, sensor signal noise filtering</td>
        </tr>
        <tr>
          <td><strong>5. Value (मूल्य / उपयोगिता)</strong></td>
          <td><span class="lang-en"><strong>The ultimate objective:</strong> The actionable business insights, predictive capability, or governance policy derived from analyzing Big Data.</span><span class="lang-hi"><strong>अंतिम उद्देश्य:</strong> भारी डेटा के विश्लेषण से निकलने वाले उपयोगी निष्कर्ष, जिससे नीतियां या निर्णय लिए जा सकें।</span></td>
          <td>Predicting disease outbreaks, detecting financial tax evasion (GSTN), reducing traffic congestion</td>
        </tr>
      </tbody>
    </table>

    <h4 style="margin:20px 0 10px; color:var(--primary-dark);">
      <span class="lang-en">The Three Data Structures (Structured vs Semi-Structured vs Unstructured):</span>
      <span class="lang-hi">डेटा के तीन मुख्य प्रारूप (संरचित, अर्ध-संरचित एवं असंरचित):</span>
    </h4>
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Structured Data (संरचित डेटा ~20% of data):</strong> Organized into fixed, predefined schemas with strict rows and columns. Easily searchable using SQL. Examples: RDBMS tables (MySQL, Oracle, PostgreSQL), Excel spreadsheets, bank account transaction tables.</span>
        <span class="lang-hi"><strong>संरचित डेटा (~20%):</strong> निश्चित स्कीमा, पंक्तियों और कॉलमों में व्यवस्थित। SQL द्वारा आसानी से खोजा जा सकता है (जैसे बैंक लेजर, छात्र अंक तालिका)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Semi-Structured Data (अर्ध-संरचित डेटा):</strong> Does not conform to rigid tabular schemas, but contains internal markers, tags, or hierarchies to separate data elements. Examples: <strong>JSON (JavaScript Object Notation)</strong>, <strong>XML</strong>, HTML files, NoSQL document stores.</span>
        <span class="lang-hi"><strong>अर्ध-संरचित डेटा:</strong> कठोर टेबल में नहीं होता, परंतु इसमें डेटा तत्वों को अलग करने हेतु टैग्स या की-वैल्यू पेयर होते हैं (जैसे JSON, XML, NoSQL)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Unstructured Data (असंरचित डेटा ~80% of all data):</strong> Has no predefined conceptual structure, model, or schema. Heavily text, audio, or video based. Examples: CCTV footage, audio recordings, scanned PDFs, social media posts, satellite imagery.</span>
        <span class="lang-hi"><strong>असंरचित डेटा (~80%):</strong> कोई पूर्व-निर्धारित संरचना या मॉडल नहीं होता। वीडियो, ऑडियो, सीसीटीवी फुटेज, सोशल मीडिया पोस्ट, उपग्रह चित्र।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Hadoop Ecosystem & Architecture -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The Apache Hadoop Ecosystem &amp; Storage Architecture (HDFS &amp; MapReduce)</span>
    <span class="lang-hi">2. अपाचे हडूप इकोसिस्टम एवं स्टोरेज वास्तुकला (HDFS एवं मैपरिड्यूस)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>What is Apache Hadoop?</strong>
          <br>&bull; An open-source software framework created in <strong>2006</strong> by <strong>Doug Cutting</strong> and <strong>Mike Cafarella</strong> (originally inspired by Google's GFS and MapReduce white papers; named after Cutting's son's yellow toy elephant).
          <br>&bull; Enables distributed storage and distributed processing of very large datasets across clusters of commodity hardware using simple programming models.
          <br>&bull; Highly fault-tolerant with automatic data replication across nodes.</span>
        <span class="lang-hi"><strong>अपाचे हडूप (Apache Hadoop) क्या है?</strong>
          <br>&bull; वर्ष <strong>2006</strong> में <strong>डग कटिंग (Doug Cutting)</strong> और <strong>माइक कैफेरेला</strong> द्वारा विकसित ओपन-सोर्स फ्रेमवर्क (गूगल के GFS और MapReduce पेपर से प्रेरित; नाम डग कटिंग के बेटे के खिलौना हाथी पर रखा गया)।
          <br>&bull; सामान्य सस्ते कंप्यूटरों (Commodity Hardware) के क्लस्टर पर भारी डेटा को समानांतर रूप से संग्रहीत और संसाधित करने में सक्षम।</span>
      </li>
      <li>
        <span class="lang-en"><strong>HDFS (Hadoop Distributed File System) Architecture:</strong>
          <br>&bull; Operates on a <strong>Master-Slave Architecture</strong>:
            <br>&nbsp;&nbsp;&bull; <strong>NameNode (Master):</strong> High-performance server that manages the file system namespace, maintains directory tree, and tracks the location of data blocks across the cluster (stores metadata in <em>fsimage</em> and <em>edits</em> log in RAM).
            <br>&nbsp;&nbsp;&bull; <strong>DataNodes (Slaves/Workers):</strong> Standard worker servers that physically store and retrieve the actual data blocks as instructed by the NameNode; send periodic <em>Heartbeat</em> signals (every 3 seconds) to verify health.
          <br>&bull; <strong>Block Size:</strong> Files are split into large blocks (default <strong>128 MB</strong> in Hadoop 2.x/3.x, compared to 4 KB in OS).
          <br>&bull; <strong>Replication Factor:</strong> By default, each block is replicated <strong>3 times</strong> across different racks/nodes for fault tolerance.</span>
        <span class="lang-hi"><strong>HDFS वास्तुकला (मास्टर-स्लेव मॉडल):</strong>
          <br>&bull; <strong>नेम-नोड (NameNode - मास्टर):</strong> केंद्रीय सर्वर जो पूरे फाइल सिस्टम का मेटाडेटा (Metadata - फाइलें किस नोड पर हैं) रखता है।
          <br>&bull; <strong>डेटा-नोड्स (DataNodes - स्लेव):</strong> वे कंप्यूटर जहां वास्तविक डेटा के ब्लॉक संग्रहीत होते हैं। ये हर 3 सेकंड में नेम-नोड को <em>हार्टबीट</em> सिग्नल भेजते हैं।
          <br>&bull; <strong>डिफ़ॉल्ट ब्लॉक साइज:</strong> हडूप 2.x/3.x में <strong>128 MB</strong> (पारंपरिक OS के 4 KB की तुलना में बहुत बड़ा)।
          <br>&bull; <strong>प्रतिकृति कारक (Replication Factor):</strong> डिफ़ॉल्ट रूप से प्रत्येक ब्लॉक की <strong>3 प्रतियां (Copies)</strong> अलग-अलग नोड्स पर बनाई जाती हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>MapReduce Distributed Processing:</strong>
          <br>&bull; Software programming model for processing massive datasets in parallel across two primary phases:
            <br>&nbsp;&nbsp;1. <strong>Map Phase:</strong> Master node takes input, partitions it, and applies worker tasks to filter and transform raw data into intermediate <code>&lt;key, value&gt;</code> pairs.
            <br>&nbsp;&nbsp;2. <strong>Shuffle &amp; Sort:</strong> Gathers all intermediate values sharing the same key.
            <br>&nbsp;&nbsp;3. <strong>Reduce Phase:</strong> Aggregates and combines the sorted values to produce the final output.</span>
        <span class="lang-hi"><strong>मैपरिड्यूस (MapReduce) प्रोसेसिंग मॉडल:</strong>
          <br>&bull; विशाल डेटा को समानांतर रूप से प्रोसेस करने का गणितीय मॉडल:
            <br>&nbsp;&nbsp;1. <strong>मैप चरण (Map):</strong> इनपुट डेटा को विभाजित कर की-वैल्यू <code>&lt;Key, Value&gt;</code> युग्मों में बदलता है।
            <br>&nbsp;&nbsp;2. <strong>शफल एवं सॉर्ट:</strong> समान 'Key' वाले डेटा को एक साथ समूहीकृत करता है।
            <br>&nbsp;&nbsp;3. <strong>रिड्यूस चरण (Reduce):</strong> समूहीकृत डेटा पर गणना (जैसे योग, औसत) कर अंतिम परिणाम देता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>YARN (Yet Another Resource Negotiator - Hadoop 2.x+):</strong>
          <br>&bull; Decoupled resource management from processing. Manages CPU, memory, and disk resources across the cluster via <em>ResourceManager</em> (cluster-level) and <em>NodeManagers</em> (per-machine).</span>
        <span class="lang-hi"><strong>YARN:</strong> हडूप क्लस्टर में CPU और RAM जैसे संसाधनों का प्रबंधन करने वाला तंत्र।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Apache Spark & NoSQL Databases -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Apache Spark, In-Memory Analytics &amp; NoSQL Databases</span>
    <span class="lang-hi">3. अपाचे स्पार्क (इन-मेमोरी कंप्यूटिंग) एवं NoSQL डेटाबेस प्रणालियाँ</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Technology</span><span class="lang-hi">तकनीक</span></th>
          <th><span class="lang-en">Core Architecture</span><span class="lang-hi">मूल संरचना</span></th>
          <th><span class="lang-en">Speed Advantage</span><span class="lang-hi">गति एवं लाभ</span></th>
          <th><span class="lang-en">Key Components / Examples</span><span class="lang-hi">घटक / उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Apache Spark</strong></td>
          <td><span class="lang-en"><strong>In-Memory Distributed Engine:</strong> Processes data in RAM rather than writing intermediate steps back to hard disks (unlike Hadoop MapReduce).</span><span class="lang-hi"><strong>इन-मेमोरी प्रोसेसिंग:</strong> डेटा को हार्ड डिस्क के बजाय सीधे RAM में रखकर प्रोसेस करता है।</span></td>
          <td><span class="lang-en">Up to <strong>100x faster</strong> than Hadoop MapReduce for iterative workloads (machine learning).</span><span class="lang-hi">हडूप मैपरिड्यूस से <strong>100 गुना अधिक तीव्र</strong>।</span></td>
          <td><span class="lang-en"><strong>RDD</strong> (Resilient Distributed Datasets), Spark SQL, Spark Streaming, MLlib (Machine Learning), GraphX.</span><span class="lang-hi"><strong>RDD</strong> (रेजिलिएंट डिस्ट्रीब्यूटेड डेटासेट), स्पार्क स्ट्रीमिंग, MLlib।</span></td>
        </tr>
        <tr>
          <td><strong>NoSQL Databases (Not Only SQL)</strong></td>
          <td><span class="lang-en">Non-relational, schema-less/flexible databases designed for horizontal scaling (scale-out across hundreds of servers) with high availability.</span><span class="lang-hi">गैर-रिलेशनल, बिना निश्चित स्कीमा वाले डेटाबेस जो सैकड़ों सर्वरों पर क्षैतिज रूप से फैल सकते हैं।</span></td>
          <td><span class="lang-en">Massive read/write throughput for unstructured and semi-structured big data.</span><span class="lang-hi">विशाल डेटा हेतु तीव्र पठन/लेखन गति।</span></td>
          <td><span class="lang-en"><strong>Document:</strong> MongoDB, CouchDB<br><strong>Column:</strong> Apache Cassandra, HBase<br><strong>Key-Value:</strong> Redis, DynamoDB<br><strong>Graph:</strong> Neo4j</span><span class="lang-hi"><strong>दस्तावेज:</strong> मोंगोDB<br><strong>कॉलम:</strong> कैसेंड्रा, HBase<br><strong>की-वैल्यू:</strong> रेडिस<br><strong>ग्राफ:</strong> नियो4j</span></td>
        </tr>
      </tbody>
    </table>

    <div style="margin-top:16px; padding:12px 16px; background:var(--primary-light); border-left:4px solid var(--primary); border-radius:6px;">
      <span class="lang-en"><strong>The CAP Theorem (Brewer's Theorem, 2000):</strong> States that a distributed data store can simultaneously provide at most <strong>two out of three</strong> guarantees:
        <br>&bull; <strong>C - Consistency:</strong> Every read receives the most recent write or an error.
        <br>&bull; <strong>A - Availability:</strong> Every request receives a non-error response (without guarantee of latest write).
        <br>&bull; <strong>P - Partition Tolerance:</strong> The system continues to operate despite network partitions/dropped messages. (In real-world networks, $P$ is mandatory, forcing a choice between $CP$ or $AP$).</span>
      <span class="lang-hi"><strong>CAP प्रमेय (ब्रूअर का प्रमेय):</strong> किसी भी वितरित डेटाबेस में एक समय में केवल दो गुण ही संभव हैं:
        <br>&bull; <strong>C (निरंतरता - Consistency):</strong> हर नोड पर एकदम अद्यतन डेटा मिले।
        <br>&bull; <strong>A (उपलब्धता - Availability):</strong> नेटवर्क हर अनुरोध पर उत्तर अवश्य दे।
        <br>&bull; <strong>P (विभाजन सहिष्णुता - Partition Tolerance):</strong> नेटवर्क कनेक्शन टूटने पर भी सिस्टम चलता रहे।</span>
    </div>
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
          <td><span class="lang-en">The 5 V's of Big Data</span><span class="lang-hi">बिग डेटा के 5 V's लक्षण</span></td>
          <td><span class="lang-en"><strong>Volume, Velocity, Variety, Veracity, Value</strong>.</span><span class="lang-hi"><strong>Volume, Velocity, Variety, Veracity, Value</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Co-creators of Apache Hadoop</span><span class="lang-hi">अपाचे हडूप के सह-निर्माता</span></td>
          <td><span class="lang-en"><strong>Doug Cutting</strong> and <strong>Mike Cafarella</strong> (2006).</span><span class="lang-hi"><strong>डग कटिंग</strong> एवं <strong>माइक कैफेरेला</strong> (2006)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default block size in Hadoop 2.x and 3.x HDFS</span><span class="lang-hi">HDFS में डिफ़ॉल्ट डेटा ब्लॉक आकार</span></td>
          <td><span class="lang-en"><strong>128 MB</strong> (Hadoop 1.x used 64 MB).</span><span class="lang-hi"><strong>128 MB</strong> (हडूप 1.x में 64 MB था)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Default data replication factor in HDFS</span><span class="lang-hi">HDFS में डिफ़ॉल्ट प्रतिकृति कारक (प्रतियों की संख्या)</span></td>
          <td><span class="lang-en"><strong>3</strong> (Three copies stored across cluster nodes).</span><span class="lang-hi"><strong>3 प्रतियां</strong> (विश्वसनीयता हेतु)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Master node in HDFS architecture storing file metadata</span><span class="lang-hi">HDFS में मेटाडेटा रखने वाला मास्टर नोड</span></td>
          <td><span class="lang-en"><strong>NameNode</strong> (DataNodes act as workers/slaves).</span><span class="lang-hi"><strong>नेम-नोड (NameNode)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Distributed computing framework operating in-memory (RAM)</span><span class="lang-hi">RAM में इन-मेमोरी कार्य करने वाला तीव्र फ्रेमवर्क</span></td>
          <td><span class="lang-en"><strong>Apache Spark</strong> (uses RDD - Resilient Distributed Datasets).</span><span class="lang-hi"><strong>अपाचे स्पार्क (Apache Spark)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Full form of NoSQL</span><span class="lang-hi">NoSQL का पूर्ण रूप</span></td>
          <td><span class="lang-en"><strong>Not Only SQL</strong>.</span><span class="lang-hi"><strong>Not Only SQL</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Prominent Document-oriented NoSQL database</span><span class="lang-hi">प्रमुख डॉक्यूमेंट-आधारित NoSQL डेटाबेस</span></td>
          <td><span class="lang-en"><strong>MongoDB</strong> (stores data in JSON/BSON format).</span><span class="lang-hi"><strong>मोंगोDB (MongoDB)</strong> (JSON प्रारूप)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Three guarantees of the CAP Theorem</span><span class="lang-hi">CAP प्रमेय के तीन घटक</span></td>
          <td><span class="lang-en"><strong>Consistency, Availability, Partition Tolerance</strong> (Brewer's Theorem).</span><span class="lang-hi"><strong>Consistency, Availability, Partition Tolerance</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">National tax platform processing Big Data invoices in India</span><span class="lang-hi">भारत में बिग डेटा पर आधारित राष्ट्रीय कर प्रणाली</span></td>
          <td><span class="lang-en"><strong>GSTN</strong> (Goods and Services Tax Network).</span><span class="lang-hi"><strong>GSTN</strong> (वस्तु एवं सेवा कर नेटवर्क)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_iot_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Internet of Things (IoT) Architecture, Protocols &amp; Applications</span>
    <span class="lang-hi">माइंड मैप: इंटरनेट ऑफ थिंग्स (IoT) वास्तुकला, प्रोटोकॉल एवं अनुप्रयोग</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Internet of Things IoT] --> B[Origins & Concept]
    A --> C[Four-Layer IoT Architecture]
    A --> D[Sensors & Actuators Hardware]
    A --> E[Specialized IoT Communication Protocols]
    A --> F[Edge vs Fog vs Cloud Computing]
    A --> G[Real-World Applications in UP & India]

    B --> B1[Term Origin: Kevin Ashton 1999 MIT Auto-ID Center]
    B --> B2[Concept: Physical objects embedded with sensors & network]
    B --> B3[Communication: M2M Machine to Machine without human input]

    C --> C1[Perception Layer: Sensors, RFID, Actuators physical touch]
    C --> C2[Network Layer: Wi-Fi, BLE, Zigbee, LoRaWAN, Cellular 5G]
    C --> C3[Middleware Layer: Data aggregation, filtering & storage]
    C --> C4[Application Layer: Smart Home, Smart City, Smart Agriculture]

    D --> D1[Sensors: Temperature, Humidity, Ultrasonic, PIR Motion, Gyro]
    D --> D2[Actuators: Relays, Servomotors, Solenoid valves physical action]

    E --> E1[MQTT Port 1883: Publish/Subscribe lightweight low-bandwidth]
    E --> E2[CoAP Port 5683: RESTful over UDP constrained nodes]
    E --> E3[6LoWPAN: IPv6 over low-power IEEE 802.15.4]

    F --> F1[Edge Computing: Processing directly on device microsecond latency]
    F --> F2[Fog Computing: Processing at local gateway/router]
    F --> F3[Cloud Computing: Centralized deep analytics & massive storage]

    G --> G1[UP Power: UPPCL Smart Prepaid electricity meters]
    G --> G2[UP Jal Jeevan: IoT monitoring of tap water in rural villages]
    G --> G3[Smart Traffic: ITMS in Lucknow, Noida, Varanasi, Kanpur]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[इंटरनेट ऑफ थिंग्स IoT] --> B[उद्भव एवं मूल अवधारणा]
    A --> C[चार-स्तरीय IoT वास्तुकला]
    A --> D[सेंसर एवं एक्चुएटर हार्डवेयर]
    A --> E[विशिष्ट IoT संचार प्रोटोकॉल]
    A --> F[एज बनाम फॉग बनाम क्लाउड कंप्यूटिंग]
    A --> G[भारत व उत्तर प्रदेश में व्यावहारिक अनुप्रयोग]

    B --> B1[शब्द के जनक: केविन एश्टन 1999 MIT ऑटो-ID सेंटर]
    B --> B2[अवधारणा: भौतिक वस्तुओं में सेंसर व नेटवर्क कनेक्टिविटी]
    B --> B3[संचार: M2M मशीन-से-मशीन बिना मानवीय हस्तक्षेप]

    C --> C1[प्रत्यक्षीकरण परत: सेंसर, RFID, एक्चुएटर भौतिक डेटा]
    C --> C2[नेटवर्क परत: वाई-फाई, ब्लूटूथ BLE, जिगबी, LoRaWAN, 5G]
    C --> C3[मिडलवेयर परत: डेटा एकत्रीकरण एवं शुद्धिकरण]
    C --> C4[एप्लीकेशन परत: स्मार्ट होम, स्मार्ट सिटी, स्मार्ट कृषि]

    D --> D1[सेंसर: तापमान, आर्द्रता, अल्ट्रासोनिक, PIR गति, जायरो]
    D --> D2[एक्चुएटर: रिले, मोटर, वॉल्व भौतिक कार्य निष्पादन]

    E --> E1[MQTT पोर्ट 1883: पब्लिश/सब्सक्राइब हल्का व तेज प्रोटोकॉल]
    E --> E2[CoAP पोर्ट 5683: UDP पर RESTful मॉडल]
    E --> E3[6LoWPAN: कम ऊर्जा वाले वायरलेस पर IPv6 एड्रेसिंग]

    F --> F1[एज कंप्यूटिंग: सीधे उपकरण पर त्वरित प्रोसेसिंग]
    F --> F2[फॉग कंप्यूटिंग: स्थानीय गेटवे/राउटर स्तर पर प्रोसेसिंग]
    F --> F3[क्लाउड कंप्यूटिंग: केंद्रीय सर्वर पर वृहद विश्लेषण]

    G --> G1[यूपी पावर: UPPCL स्मार्ट प्रीपेड बिजली मीटर]
    G --> G2[जल जीवन मिशन: उप्र के गांवों में नल जल की IoT निगरानी]
    G --> G3[स्मार्ट ट्रैफिक: लखनऊ, नोएडा, वाराणसी में ITMS नियंत्रण]
    </div>
  </div>
</div>

<!-- Card 2: Origins & Concept -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Origins, Definition &amp; Core Concept of IoT</span>
    <span class="lang-hi">1. IoT का उद्भव, परिभाषा एवं मूल कार्यप्रणाली</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Origin of the Term 'Internet of Things':</strong>
          <br>&bull; Coined in <strong>1999</strong> by British technology pioneer <strong>Kevin Ashton</strong> during a presentation at Procter &amp; Gamble (P&amp;G) while working with the <strong>MIT Auto-ID Center</strong>.
          <br>&bull; Ashton proposed using <strong>Radio Frequency Identification (RFID)</strong> tags to let computers track physical products without human intervention.
          <br>&bull; The first unofficial connected IoT device was a modified <strong>Coca-Cola vending machine</strong> at Carnegie Mellon University in 1982 that reported its inventory and temperature over the ARPANET.</span>
        <span class="lang-hi"><strong>'इंटरनेट ऑफ थिंग्स' शब्द की उत्पत्ति:</strong>
          <br>&bull; <strong>1999</strong> में ब्रिटिश प्रौद्योगिकी विशेषज्ञ <strong>केविन एश्टन (Kevin Ashton)</strong> द्वारा प्रॉक्टर एंड गैंबल (P&amp;G) में प्रस्तुति के दौरान MIT ऑटो-ID केंद्र के संदर्भ में गढ़ा गया।
          <br>&bull; इन्होंने आरएफआईडी (RFID) चिप्स के माध्यम से वस्तुओं को इंटरनेट से जोड़ने का प्रस्ताव रखा था।
          <br>&bull; इतिहास का पहला अनाधिकारिक IoT उपकरण 1982 में कार्नेगी मेलन यूनिवर्सिटी की एक <em>कोका-कोला वेंडिंग मशीन</em> थी, जो नेटवर्क पर अपनी इन्वेंट्री और तापमान बताती थी।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Definition &amp; M2M Communication:</strong>
          <br>&bull; <strong>IoT Definition:</strong> A vast interconnected network of physical objects ("things") embedded with sensors, software, actuators, and network connectivity that enables them to collect, exchange, and act upon data over the Internet.
          <br>&bull; <strong>M2M (Machine-to-Machine):</strong> Autonomous communication between physical devices without manual human-to-human or human-to-computer intervention.</span>
        <span class="lang-hi"><strong>IoT की परिभाषा एवं M2M संचार:</strong>
          <br>&bull; भौतिक वस्तुओं ("Things") का ऐसा विशाल नेटवर्क जिसमें सेंसर, सॉफ्टवेयर, एक्चुएटर और नेटवर्क कनेक्टिविटी अंतर्निहित होती है, जो उन्हें मानवीय हस्तक्षेप के बिना डेटा एकत्र करने और आदान-प्रदान करने में सक्षम बनाती है।
          <br>&bull; <strong>M2M (मशीन-से-मशीन):</strong> दो मशीनों के बीच बिना किसी मानवीय दखल के स्वतः होने वाला डिजिटल संचार।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: 4-Layer Architecture of IoT -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The Four-Layer Architecture of IoT Systems</span>
    <span class="lang-hi">2. IoT प्रणालियों की चार-स्तरीय वास्तुकला (4-Layer Architecture)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Layer</span><span class="lang-hi">परत</span></th>
          <th><span class="lang-en">Layer Name</span><span class="lang-hi">परत का नाम</span></th>
          <th><span class="lang-en">Core Function</span><span class="lang-hi">मुख्य कार्य</span></th>
          <th><span class="lang-en">Hardware &amp; Protocols Used</span><span class="lang-hi">हार्डवेयर एवं प्रोटोकॉल</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Layer 1</strong></td>
          <td><strong>Perception / Sensing Layer (प्रत्यक्षीकरण परत)</strong></td>
          <td><span class="lang-en">Physical interface interacting with real world; collects physical signals (heat, pressure, light) and converts to electrical signals.</span><span class="lang-hi">भौतिक जगत से डेटा एकत्र करना (ताप, दबाव, प्रकाश) तथा एक्चुएटर द्वारा भौतिक कार्य करना।</span></td>
          <td>Sensors (DHT11, PIR, LDR, Ultrasonic, GPS, Gyroscope), RFID tags, QR codes, Actuators (Relays, Solenoids, Motors)</td>
        </tr>
        <tr>
          <td><strong>Layer 2</strong></td>
          <td><strong>Network / Transmission Layer (नेटवर्क परत)</strong></td>
          <td><span class="lang-en">Transmits collected sensor data securely to gateways, servers, or cloud platforms.</span><span class="lang-hi">सेंसर डेटा को सुरक्षित रूप से सर्वर या क्लाउड तक पहुंचाना।</span></td>
          <td>Wi-Fi (802.11), Bluetooth Low Energy (BLE), <strong>Zigbee (IEEE 802.15.4)</strong>, <strong>LoRaWAN</strong>, Cellular NB-IoT, 5G</td>
        </tr>
        <tr>
          <td><strong>Layer 3</strong></td>
          <td><strong>Middleware / Data Processing Layer (मिडलवेयर परत)</strong></td>
          <td><span class="lang-en">Aggregates, filters, stores, and performs computing on massive streams of incoming telemetry data.</span><span class="lang-hi">डेटा का भंडारण, शुद्धिकरण, एकत्रीकरण एवं गणना करना।</span></td>
          <td>Edge computing gateways, Fog nodes, Cloud platforms (AWS IoT Core, Azure IoT, Google Cloud IoT)</td>
        </tr>
        <tr>
          <td><strong>Layer 4</strong></td>
          <td><strong>Application Layer (एप्लीकेशन परत)</strong></td>
          <td><span class="lang-en">Delivers user-facing services and domain-specific smart dashboards to end consumers and enterprises.</span><span class="lang-hi">उपयोगकर्ता को अंतिम सेवाएं एवं डैशबोर्ड प्रदान करना।</span></td>
          <td>Smart Homes (smart plugs, thermostats), Smart Agriculture (soil moisture monitoring), Smart Cities, Connected Healthcare</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Specialized IoT Protocols -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Specialized IoT Communication Protocols (MQTT, CoAP &amp; Zigbee)</span>
    <span class="lang-hi">3. विशिष्ट IoT संचार प्रोटोकॉल (MQTT, CoAP एवं जिगबी)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Protocol</span><span class="lang-hi">प्रोटोकॉल</span></th>
          <th><span class="lang-en">Full Form</span><span class="lang-hi">पूर्ण रूप</span></th>
          <th><span class="lang-en">Transport &amp; Port</span><span class="lang-hi">ट्रांसपोर्ट व पोर्ट</span></th>
          <th><span class="lang-en">Messaging Architecture</span><span class="lang-hi">मैसेजिंग मॉडल</span></th>
          <th><span class="lang-en">Key Features &amp; Best Use</span><span class="lang-hi">विशेषताएं एवं उपयोग</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>MQTT</strong></td>
          <td>Message Queuing Telemetry Transport</td>
          <td><strong>TCP</strong> (Port 1883 plain, Port 8883 SSL/TLS)</td>
          <td><strong>Publish / Subscribe (Pub-Sub)</strong> via central Broker</td>
          <td><span class="lang-en">Extremely lightweight, minimal 2-byte header, designed by IBM (Andy Stanford-Clark) for low-bandwidth, high-latency remote monitoring. <strong>De-facto IoT standard.</strong></span><span class="lang-hi">अत्यंत हल्का (2-बाइट हेडर), कम बैंडविड्थ और खराब नेटवर्क में भी तीव्र। IoT का सर्वाधिक लोकप्रिय प्रोटोकॉल।</span></td>
        </tr>
        <tr>
          <td><strong>CoAP</strong></td>
          <td>Constrained Application Protocol</td>
          <td><strong>UDP</strong> (Port 5683 unencrypted, Port 5684 DTLS)</td>
          <td><strong>Request / Response</strong> (RESTful)</td>
          <td><span class="lang-en">Web-like REST protocol (GET, POST, PUT) designed specifically for resource-constrained 8-bit microcontrollers over UDP.</span><span class="lang-hi">सीमित क्षमता वाले 8-बिट माइक्रोकंट्रोलर्स हेतु UDP पर आधारित RESTful मॉडल।</span></td>
        </tr>
        <tr>
          <td><strong>Zigbee</strong></td>
          <td>IEEE 802.15.4 standard</td>
          <td>Radio Frequency (2.4 GHz)</td>
          <td><strong>Mesh Networking</strong></td>
          <td><span class="lang-en">Low-power, low data rate (250 kbps), short range (10-100m). Capable of connecting up to 65,000 devices in a robust self-healing mesh.</span><span class="lang-hi">कम ऊर्जा खपत, 10-100 मीटर दायरा; स्मार्ट होम ऑटोमेशन में बल्ब, सेंसर जोड़ने हेतु।</span></td>
        </tr>
        <tr>
          <td><strong>LoRaWAN</strong></td>
          <td>Long Range Wide Area Network</td>
          <td>Sub-GHz ISM bands (865-867 MHz in India)</td>
          <td>Star-of-Stars</td>
          <td><span class="lang-en">Long-range wireless communication (up to 10-15 km in rural areas) with 10-year battery life for remote sensors.</span><span class="lang-hi">10 से 15 किमी लंबी दूरी तक कम ऊर्जा में डेटा भेजना (स्मार्ट खेती, रिमोट मीटरिंग)।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 5: Edge vs Fog vs Cloud & UP Applications -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Edge vs Fog vs Cloud &amp; Real-World IoT in Uttar Pradesh</span>
    <span class="lang-hi">4. एज बनाम फॉग बनाम क्लाउड कंप्यूटिंग एवं उत्तर प्रदेश में IoT अनुप्रयोग</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Computing Paradigms in IoT:</strong>
          <br>&bull; <strong>Edge Computing:</strong> Data is processed locally right on the sensor or device micro-controller itself. Minimal latency (microseconds); critical for autonomous braking or industrial safety shutdowns.
          <br>&bull; <strong>Fog Computing:</strong> Processing happens at local network gateway routers or edge servers located close to the devices rather than across the Internet.
          <br>&bull; <strong>Cloud Computing:</strong> Massive centralized data centers (AWS, Microsoft Azure, Google Cloud) handling petabyte-scale long-term historical analytics, machine learning training, and global dashboards.</span>
        <span class="lang-hi"><strong>IoT में कंप्यूटिंग के तीन स्तर:</strong>
          <br>&bull; <strong>एज कंप्यूटिंग (Edge):</strong> डेटा प्रोसेसिंग सीधे सेंसर या उपकरण पर ही होती है (अत्यंत तीव्र, बिना इंटरनेट विलंबता के, जैसे कार का इमरजेंसी ब्रेक)।
          <br>&bull; <strong>फॉग कंप्यूटिंग (Fog):</strong> डेटा का विश्लेषण स्थानीय नेटवर्क गेटवे/राउटर स्तर पर होता है।
          <br>&bull; <strong>क्लाउड कंप्यूटिंग (Cloud):</strong> केंद्रीय रिमोट सर्वरों पर भारी विश्लेषण और दीर्घकालिक रिकॉर्ड सहेजना।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Real-World IoT Initiatives in Uttar Pradesh:</strong>
          <br>&bull; <strong>UPPCL Smart Metering:</strong> Uttar Pradesh Power Corporation Limited has installed millions of smart electric prepaid meters that communicate consumption data to billing servers via cellular IoT without physical meter readers.
          <br>&bull; <strong>Jal Jeevan Mission IoT Monitoring:</strong> Over 100,000 villages in UP are equipped with IoT sensors on rural tap water pipelines measuring water flow, pressure, and chlorine levels transmitted in real time to the State Water Dashboard.
          <br>&bull; <strong>ITMS (Integrated Traffic Management System):</strong> Deployed in cities like Lucknow, Varanasi, Noida, and Kanpur; uses IoT camera sensors to automatically detect red-light violations and issue e-challans.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश में IoT के प्रमुख व्यावहारिक उदाहरण:</strong>
          <br>&bull; <strong>स्मार्ट बिजली मीटर (UPPCL):</strong> उत्तर प्रदेश में लाखों स्मार्ट प्रीपेड मीटर लगाए गए हैं, जो स्वचालित रूप से बिजली खपत का डेटा सर्वर पर भेजते हैं।
          <br>&bull; <strong>जल जीवन मिशन में IoT:</strong> उप्र के गांवों में पेयजल की आपूर्ति, दबाव और क्लोरीन स्तर की निगरानी हेतु पाइपलाइनों में IoT सेंसर लगाए गए हैं।
          <br>&bull; <strong>एकीकृत यातायात प्रबंधन प्रणाली (ITMS):</strong> लखनऊ, नोएडा, कानपुर और वाराणसी में रेड-लाइट उल्लंघन पकड़ने और ई-चालान काटने हेतु स्मार्ट कैमरे व सेंसर।</span>
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
          <td><span class="lang-en">Who coined the term 'Internet of Things' (IoT)?</span><span class="lang-hi">'इंटरनेट ऑफ थिंग्स' (IoT) शब्द किसने गढ़ा?</span></td>
          <td><span class="lang-en"><strong>Kevin Ashton</strong> in <strong>1999</strong> at MIT Auto-ID Center.</span><span class="lang-hi"><strong>केविन एश्टन</strong> (1999 में, MIT)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First unofficial IoT connected device in history</span><span class="lang-hi">इतिहास का पहला इंटरनेट से जुड़ा उपकरण</span></td>
          <td><span class="lang-en">A <strong>Coca-Cola Vending Machine</strong> at Carnegie Mellon University (1982).</span><span class="lang-hi">कार्नेगी मेलन यूनिवर्सिटी की <strong>कोका-कोला वेंडिंग मशीन</strong> (1982)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Lightweight Publish/Subscribe messaging protocol widely used in IoT</span><span class="lang-hi">IoT में सर्वाधिक प्रयुक्त हल्का पब्लिश/सब्सक्राइब प्रोटोकॉल</span></td>
          <td><span class="lang-en"><strong>MQTT</strong> (Message Queuing Telemetry Transport, Port 1883).</span><span class="lang-hi"><strong>MQTT</strong> (पोर्ट 1883)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Component in IoT that converts electrical commands into physical motion</span><span class="lang-hi">विद्युत सिग्नल को भौतिक गति में बदलने वाला उपकरण</span></td>
          <td><span class="lang-en"><strong>Actuator</strong> (e.g., relay, motor, valve).</span><span class="lang-hi"><strong>एक्चुएटर (Actuator)</strong> (जैसे मोटर, रिले)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Component in IoT that measures physical environmental attributes</span><span class="lang-hi">पर्यावरणीय भौतिक मानों को मापने वाला उपकरण</span></td>
          <td><span class="lang-en"><strong>Sensor</strong> (e.g., temperature, light, motion).</span><span class="lang-hi"><strong>सेंसर (Sensor)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Short-range mesh networking wireless standard IEEE 802.15.4</span><span class="lang-hi">स्मार्ट होम मेश नेटवर्किंग का IEEE 802.15.4 मानक</span></td>
          <td><span class="lang-en"><strong>Zigbee</strong>.</span><span class="lang-hi"><strong>जिगबी (Zigbee)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Computing paradigm where data is processed directly on the IoT device</span><span class="lang-hi">सीधे उपकरण पर डेटा प्रोसेस करने वाली कंप्यूटिंग</span></td>
          <td><span class="lang-en"><strong>Edge Computing</strong> (न्यूनतम विलंबता).</span><span class="lang-hi"><strong>एज कंप्यूटिंग (Edge Computing)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Long-range, low-power wireless technology covering up to 15 km</span><span class="lang-hi">10-15 किमी लंबी दूरी तक कम ऊर्जा में डेटा भेजने की तकनीक</span></td>
          <td><span class="lang-en"><strong>LoRaWAN</strong> (Long Range WAN).</span><span class="lang-hi"><strong>LoRaWAN</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Layer of IoT architecture containing physical sensors and RFID</span><span class="lang-hi">भौतिक सेंसर और RFID वाली IoT परत</span></td>
          <td><span class="lang-en"><strong>Perception / Sensing Layer</strong> (प्रत्यक्षीकरण परत).</span><span class="lang-hi"><strong>प्रत्यक्षीकरण परत (Perception Layer)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Massive botnet that infected IoT devices with default passwords in 2016</span><span class="lang-hi">2016 में कमजोर पासवर्ड वाले IoT उपकरणों को हैक करने वाला बॉटनेत</span></td>
          <td><span class="lang-en"><strong>Mirai Botnet</strong>.</span><span class="lang-hi"><strong>मिराई बॉटनेत (Mirai Botnet)</strong>।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_it_gadgets_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: IT Gadgets, Smart Devices, Wearables &amp; Applications</span>
    <span class="lang-hi">माइंड मैप: IT गैजेट्स, स्मार्ट उपकरण, वियरेबल्स एवं अनुप्रयोग</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[IT Gadgets & Applications] --> B[Smart Mobile Devices]
    A --> C[Wearables & Health Tech]
    A --> D[Multimedia & Audio Gadgets]
    A --> E[Drones & Robotics UAVs]
    A --> F[Navigation & Peripherals]
    A --> G[Battery & Charging Tech]

    B --> B1[Smartphones: SoC Snapdragon, Apple A-Series, MediaTek]
    B --> B2[Tablets & Phablets: Large touch screens, stylus support]
    B --> B3[E-Readers: Amazon Kindle, E-Ink electronic paper zero eye strain]

    C --> C1[Smartwatches & Fitness Bands: Optical PPG heart rate, SpO2]
    C --> C2[Smart Glasses: Augmented Reality AR heads-up display]
    C --> C3[Medical Wearables: Continuous Glucose Monitors CGM, portable ECG]

    D --> D1[TWS Earbuds: Bluetooth 5.x, Active Noise Cancellation ANC]
    D --> D2[Smart Speakers: Amazon Alexa, Google Assistant, Siri]
    D --> D3[Streaming Dongles: Chromecast, Fire TV Stick HDMI]

    E --> E1[UAV Drones: Quadcopters, GPS waypoint navigation, LiDAR]
    E --> E2[UP Scheme: SVAMITVA village property mapping Gharauni]
    E --> E3[Kisan Drones: Precision fertilizer & pesticide spraying]

    F --> F1[Navigation: GPS USA vs NavIC India ISRO 7 satellites]
    F --> F2[Biometric Scanners: Aadhaar AePS fingerprint & iris STQC]
    F --> F3[Barcode 1D vs QR Code 2D Denso Wave 1994]

    G --> G1[Batteries: Li-ion vs Li-Polymer thin lightweight]
    G --> G2[Charging: USB Power Delivery USB-PD, Qi Wireless induction]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[IT गैजेट्स एवं अनुप्रयोग] --> B[स्मार्ट मोबाइल उपकरण]
    A --> C[वियरेबल्स एवं स्वास्थ्य तकनीक]
    A --> D[मल्टीमीडिया एवं ध्वनि गैजेट्स]
    A --> E[ड्रोन एवं रोबोटिक्स UAV]
    A --> F[नेविगेशन एवं परिधीय उपकरण]
    A --> G[बैटरी एवं चार्जिंग तकनीक]

    B --> B1[स्मार्टफोन: SoC स्नैपड्रैगन, एप्पल बायोनिक, मीडियाटेक]
    B --> B2[टैबलेट: बड़ी टच स्क्रीन, स्टायलस पेन समर्थन]
    B --> B3[ई-रीडर: अमेज़न किंडल, ई-इंक इलेक्ट्रॉनिक पेपर आँखों पर शून्य तनाव]

    C --> C1[स्मार्टवॉच व फिटनेस बैंड: PPG हृदय गति, SpO2 ऑक्सीजन]
    C --> C2[स्मार्ट चश्मा: ऑगमेंटेड रियलिटी AR डिजिटल डिस्प्ले]
    C --> C3[चिकित्सा उपकरण: पोर्टेबल ईसीजी, ग्लूकोज मॉनिटर]

    D --> D1[TWS ईयरबड्स: ब्लूटूथ 5.x, एक्टिव नॉइज़ कैंसिलेशन ANC]
    D --> D2[स्मार्ट स्पीकर: अमेज़न अलेक्सा, गूगल असिस्टेंट]
    D --> D3[स्ट्रीमिंग डोंगल: क्रोमकास्ट, फायर टीवी स्टिक HDMI]

    E --> E1[UAV ड्रोन: क्वाडकॉप्टर, जीपीएस नेविगेशन, LiDAR]
    E --> E2[उप्र योजना: स्वामित्व योजना ग्रामीण भूमि पैमाइश घरौनी]
    E --> E3[किसान ड्रोन: कीटनाशक एवं यूरिया का छिड़काव]

    F --> F1[नेविगेशन: GPS अमेरिका बनाम NavIC भारत इसरो 7 उपग्रह]
    F --> F2[बायोमेट्रिक स्कैनर: आधार AePS फिंगरप्रिंट व आईरिस]
    F --> F3[बारकोड 1D बनाम QR कोड 2D डेंसो वेव 1994]

    G --> G1[बैटरी: लिथियम-आयन बनाम लिथियम-पॉलिमर पतली व सुरक्षित]
    G --> G2[चार्जिंग: USB पावर डिलीवरी USB-PD, Qi वायरलेस चार्जिंग]
    </div>
  </div>
</div>

<!-- Card 2: Mobile Smart Devices & E-Readers -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Smart Mobile Devices &amp; E-Book Readers</span>
    <span class="lang-hi">1. स्मार्ट मोबाइल उपकरण एवं ई-बुक रीडर तकनीक</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>What is an IT Gadget?</strong>
          <br>&bull; A specialized electronic device or appliance designed with computing, network connectivity, and compact form factor to perform specific utility functions and improve productivity.
          <br>&bull; Powered by miniaturized embedded microprocessors or <strong>SoC (System-on-Chip)</strong> architectures that integrate CPU, GPU, memory controller, modem, and AI neural engines onto a single silicon chip (e.g., Qualcomm Snapdragon, Apple A-series/M-series, MediaTek Dimensity).</span>
        <span class="lang-hi"><strong>IT गैजेट क्या है?</strong>
          <br>&bull; एक विशिष्ट कॉम्पैक्ट इलेक्ट्रॉनिक उपकरण जिसमें कंप्यूटिंग क्षमता और नेटवर्क कनेक्टिविटी होती है, जो विशिष्ट कार्य करने व दैनिक जीवन को सुगम बनाने हेतु डिज़ाइन किया गया हो।
          <br>&bull; यह <strong>SoC (सिस्टम-ऑन-चिप)</strong> पर आधारित होता है, जिसमें CPU, GPU, मॉडम और AI न्यूरल इंजन एक ही छोटी चिप पर समाहित होते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>E-Book Readers &amp; E-Ink Technology:</strong>
          <br>&bull; Devices like <strong>Amazon Kindle</strong> and Kobo designed dedicatedly for reading digital books.
          <br>&bull; <strong>E-Ink (Electronic Paper Display):</strong> Uses millions of microscopic microcapsules filled with clear fluid containing charged black (negative) and white (positive) pigment particles. When an electric field is applied, the appropriate particles float to the surface.
          <br>&bull; <strong>Advantages over LCD/OLED:</strong> <strong>Zero backlight glare</strong> (reads like real printed paper in bright sunlight), <strong>zero eye strain</strong>, and consumes battery <em>only when turning pages</em> (battery lasts for weeks rather than hours).</span>
        <span class="lang-hi"><strong>ई-बुक रीडर एवं ई-इंक (E-Ink) तकनीक:</strong>
          <br>&bull; अमेज़न किंडल (Amazon Kindle) जैसे उपकरण जो केवल डिजिटल पुस्तकें पढ़ने हेतु बनाए गए हैं।
          <br>&bull; <strong>ई-इंक (इलेक्ट्रॉनिक पेपर):</strong> इसमें सूक्ष्म कैप्सूल होते हैं जिनमें काले और सफेद कण विद्युत आवेश द्वारा सतह पर आते हैं।
          <br>&bull; <strong>LCD स्क्रीन की तुलना में लाभ:</strong> धूप में भी स्पष्ट पठनीयता, <strong>आँखों पर शून्य तनाव</strong>, और बिजली की खपत केवल पेज पलटते समय होती है (बैटरी हफ्तों तक चलती है)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Wearables & Audio Gadgets -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Wearable Technology &amp; Audio Gadgets (ANC &amp; Sensors)</span>
    <span class="lang-hi">2. वियरेबल तकनीक एवं ऑडियो गैजेट्स (ANC एवं स्वास्थ्य सेंसर)</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Gadget Category</span><span class="lang-hi">गैजेट श्रेणी</span></th>
          <th><span class="lang-en">Key Sensor / Tech</span><span class="lang-hi">प्रमुख सेंसर / तकनीक</span></th>
          <th><span class="lang-en">Scientific Working Principle</span><span class="lang-hi">वैज्ञानिक कार्यप्रणाली</span></th>
          <th><span class="lang-en">Typical Health / Utility Use</span><span class="lang-hi">उपयोग</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Smartwatches &amp; Fitness Bands</strong></td>
          <td><strong>PPG Sensor</strong> (Photoplethysmography) &amp; <strong>SpO2</strong></td>
          <td><span class="lang-en">Emits green LED light into skin; photodiode measures light absorption changes caused by pulsing blood volume to calculate <strong>Heart Rate</strong>. Red/Infrared light calculates <strong>Blood Oxygen (SpO2)</strong> saturation.</span><span class="lang-hi">त्वचा पर हरी रोशनी डालकर रक्त प्रवाह के आधार पर <strong>हृदय गति</strong> मापना। लाल/अवरक्त प्रकाश द्वारा रक्त में <strong>ऑक्सीजन (SpO2)</strong> का स्तर मापना।</span></td>
          <td>24x7 pulse tracking, sleep staging, stress monitoring, pedometer step counter (accelerometer)</td>
        </tr>
        <tr>
          <td><strong>TWS Earbuds</strong></td>
          <td><strong>ANC</strong> (Active Noise Cancellation)</td>
          <td><span class="lang-en">External microphones detect ambient noise; internal DSP processor instantly creates an inverted <strong>anti-phase soundwave (destructive interference)</strong> to neutralize background noise before it hits the eardrum.</span><span class="lang-hi">बाहरी शोर को माइक द्वारा पकड़कर, विपरीत तरंग (Anti-phase wave / विनाशी व्यतिकरण) उत्पन्न कर बाहरी शोर को शून्य कर देना।</span></td>
          <td>Crystal clear calling in noisy metro, flight travel, immersive audio listening</td>
        </tr>
        <tr>
          <td><strong>Smart Speakers</strong></td>
          <td>Far-Field Mics &amp; Natural Language Processing (NLP)</td>
          <td><span class="lang-en">Constantly listens for localized <strong>wake-words</strong> ("Alexa", "Hey Google"); streams voice query to cloud AI server for natural language comprehension and home automation command execution.</span><span class="lang-hi">वेक-वर्ड ("अलेक्सा", "हे गूगल") सुनते ही सक्रिय होना; आवाज को टेक्स्ट में बदलकर घरेलू उपकरणों को नियंत्रित करना।</span></td>
          <td>Smart home automation (lights, AC), playing news/music, set timers and reminders</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Drones, Navigation & Peripherals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Drones (UAVs), Navigation Systems (GPS vs NavIC) &amp; Barcode/QR</span>
    <span class="lang-hi">3. ड्रोन (UAV), नेविगेशन प्रणालियाँ (GPS बनाम NavIC) एवं बारकोड/QR कोड</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Drones (Unmanned Aerial Vehicles - UAV):</strong>
          <br>&bull; Aircraft operated without a human pilot onboard, controlled either autonomously by onboard computers or via remote control.
          <br>&bull; <strong>SVAMITVA Scheme in Uttar Pradesh:</strong> The Ministry of Panchayati Raj uses survey-grade camera drones across UP villages to map rural abadi (inhabited) lands with centimeter accuracy, providing villagers with legal ownership property cards called <strong>"Gharauni" (घरौनी)</strong>.
          <br>&bull; <strong>Kisan Drones:</strong> Used in precision agriculture for spraying liquid nano-urea and pesticides across large farms in minutes, saving water and chemical runoff.</span>
        <span class="lang-hi"><strong>ड्रोन (मानव रहित हवाई वाहन - UAV):</strong>
          <br>&bull; बिना पायलट के उड़ने वाला विमान, जिसे रिमोट कंट्रोल या कंप्यूटर द्वारा स्वचालित रूप से उड़ाया जाता है।
          <br>&bull; <strong>उत्तर प्रदेश में 'स्वामित्व' योजना (SVAMITVA):</strong> पंचायती राज मंत्रालय द्वारा उप्र के गांवों में ड्रोन से भूमि की सटीक पैमाइश कर ग्रामीणों को कानूनी संपत्ति दस्तावेज <strong>"घरौनी"</strong> प्रदान किए जा रहे हैं।
          <br>&bull; <strong>किसान ड्रोन:</strong> खेतों में तरल नैनो-यूरिया और कीटनाशकों के त्वरित व सुरक्षित छिड़काव हेतु।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Satellite Navigation: GPS (USA) vs NavIC (India):</strong>
          <br>&bull; <strong>GPS (Global Positioning System):</strong> Owned by the US Government; constellation of 24+ operational satellites providing global positioning.
          <br>&bull; <strong>NavIC (Navigation with Indian Constellation / IRNSS):</strong> Developed independently by <strong>ISRO</strong> (Indian Space Research Organisation).
          <br>&bull; Consists of a constellation of <strong>7 satellites</strong> (3 geostationary + 4 geosynchronous). Covers entire Indian landmass and extends up to <strong>1,500 km</strong> beyond Indian borders with civilian accuracy &lt; 10 meters.</span>
        <span class="lang-hi"><strong>उपग्रह नेविगेशन: GPS (अमेरिका) बनाम NavIC (भारत):</strong>
          <br>&bull; <strong>GPS:</strong> अमेरिकी सरकार का वैश्विक उपग्रह नेविगेशन सिस्टम (24+ उपग्रह)।
          <br>&bull; <strong>NavIC (नाविक / IRNSS):</strong> <strong>इसरो (ISRO)</strong> द्वारा विकसित भारत का स्वदेशी उपग्रह नेविगेशन सिस्टम।
          <br>&bull; इसमें <strong>7 उपग्रहों</strong> का समूह है (3 भू-स्थिर एवं 4 भू-तुल्यकालिक)। यह पूरे भारत तथा सीमाओं से <strong>1,500 किमी बाहर तक</strong> 10 मीटर से बेहतर सटीकता प्रदान करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Barcode (1D) vs QR Code (2D):</strong>
          <br>&bull; <strong>Barcode (1D):</strong> Linear representation of data using parallel lines of varying widths and spacings. Read horizontally by laser scanners (UPC, EAN-13 codes on grocery items). Stores only ~20 alphanumeric characters.
          <br>&bull; <strong>QR Code (Quick Response - 2D Matrix):</strong> Invented in <strong>1994</strong> by <strong>Masahiro Hara</strong> at Denso Wave (Japan) to track automobile parts.
          <br>&bull; Two-dimensional matrix of black squares on a white background with 3 distinct square position detection patterns in corners.
          <br>&bull; Stores significantly more data: up to <strong>7,089 numeric</strong> or <strong>4,296 alphanumeric characters</strong>. Features built-in <em>Reed-Solomon error correction</em> (readable even if up to 30% damaged). Powers India's UPI payment scanning.</span>
        <span class="lang-hi"><strong>बारकोड (1D) बनाम QR कोड (2D):</strong>
          <br>&bull; <strong>बारकोड (1D):</strong> विभिन्न चौड़ाई की समानांतर काली पट्टियों की रैखिक व्यवस्था; केवल क्षैतिज रूप से पढ़ा जा सकता है (~20 अक्षर)।
          <br>&bull; <strong>QR कोड (2D):</strong> <strong>1994</strong> में जापानी कंपनी डेंसो वेव के <strong>मासाहिरो हारा</strong> द्वारा विकसित।
          <br>&bull; तीन कोनों में बड़े चौकोर पहचान चिन्ह होते हैं; इसमें <strong>7,089 अंक</strong> या <strong>4,296 अक्षर</strong> समा सकते हैं।
          <br>&bull; 30% तक कटे-फटे होने पर भी पढ़ा जा सकता है (रीड-सोलोमन एरर करेक्शन)। भारत में UPI भुगतान (फोनपे, गूगल पे, पेटीएम) का आधार।</span>
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
          <td><span class="lang-en">Display technology used in Amazon Kindle e-readers</span><span class="lang-hi">किंडल ई-रीडर में प्रयुक्त डिस्प्ले तकनीक</span></td>
          <td><span class="lang-en"><strong>E-Ink (Electronic Paper Display)</strong> (zero glare, weeks of battery life).</span><span class="lang-hi"><strong>ई-इंक (E-Ink / इलेक्ट्रॉनिक पेपर)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Inventor and year of 2D Quick Response (QR) Code</span><span class="lang-hi">QR कोड के आविष्कारक एवं वर्ष</span></td>
          <td><span class="lang-en"><strong>Masahiro Hara</strong> at <strong>Denso Wave</strong> in <strong>1994</strong> (Japan).</span><span class="lang-hi"><strong>मासाहिरो हारा</strong> (डेंसो वेव, <strong>1994</strong>)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">India's indigenous satellite navigation system developed by ISRO</span><span class="lang-hi">इसरो द्वारा विकसित भारत का स्वदेशी उपग्रह नेविगेशन सिस्टम</span></td>
          <td><span class="lang-en"><strong>NavIC</strong> (Navigation with Indian Constellation / IRNSS - 7 satellites).</span><span class="lang-hi"><strong>NavIC (नाविक)</strong> (7 उपग्रहों का समूह)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Technology used in smartwatches to measure heart rate via green LEDs</span><span class="lang-hi">स्मार्टवॉच में हृदय गति मापने वाला ऑप्टिकल सेंसर</span></td>
          <td><span class="lang-en"><strong>PPG Sensor</strong> (Photoplethysmography).</span><span class="lang-hi"><strong>PPG सेंसर</strong> (फोटोप्लेथिस्मोग्राफी)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Acoustic principle used in Active Noise Cancellation (ANC) earbuds</span><span class="lang-hi">ANC ईयरबड्स में प्रयुक्त ध्वनि तरंग सिद्धांत</span></td>
          <td><span class="lang-en"><strong>Destructive Interference</strong> (generating inverted anti-phase soundwaves).</span><span class="lang-hi"><strong>विनाशी व्यतिकरण (Destructive Interference)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Central rural land mapping drone scheme operating in Uttar Pradesh</span><span class="lang-hi">उप्र में ग्रामीण भूमि पैमाइश हेतु ड्रोन योजना</span></td>
          <td><span class="lang-en"><strong>SVAMITVA Scheme</strong> (issues 'Gharauni' legal ownership cards).</span><span class="lang-hi"><strong>स्वामित्व योजना (SVAMITVA)</strong> ('घरौनी' प्रमाण पत्र)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Global industry standard for wireless inductive device charging</span><span class="lang-hi">वायरलेस चार्जिंग का वैश्विक मानक</span></td>
          <td><span class="lang-en"><strong>Qi Standard</strong> (Wireless Power Consortium).</span><span class="lang-hi"><strong>Qi (ची) मानक</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Single silicon chip integrating CPU, GPU, memory, and modems in phones</span><span class="lang-hi">स्मार्टफोन में सभी चिप घटकों को समाहित करने वाली चिप</span></td>
          <td><span class="lang-en"><strong>SoC</strong> (System-on-Chip).</span><span class="lang-hi"><strong>SoC</strong> (सिस्टम-ऑन-चिप)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Government certification standard required for Aadhaar biometric scanners</span><span class="lang-hi">आधार बायोमेट्रिक स्कैनर हेतु अनिवार्य सरकारी प्रमाणन</span></td>
          <td><span class="lang-en"><strong>STQC Certification</strong> (Standardisation Testing and Quality Certification).</span><span class="lang-hi"><strong>STQC प्रमाणन</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Battery chemistry offering thinner and flexible form factors in gadgets</span><span class="lang-hi">गैजेट्स में प्रयुक्त पतली व लचीली बैटरी तकनीक</span></td>
          <td><span class="lang-en"><strong>Li-Po</strong> (Lithium-ion Polymer battery).</span><span class="lang-hi"><strong>लिथियम-पॉलिमर (Li-Po)</strong>।</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def build_information_technology_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Information Technology Foundations, DBMS, Cloud &amp; Cyber Laws</span>
    <span class="lang-hi">माइंड मैप: सूचना प्रौद्योगिकी मूल बातें, DBMS, क्लाउड एवं IT कानून</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Information Technology IT] --> B[The DIKW Information Pyramid]
    A --> C[Relational Databases RDBMS & SQL]
    A --> D[Cloud Computing Service Models]
    A --> E[Cyber Security & Threat Landscape]
    A --> F[Information Technology Act 2000]

    B --> B1[Data: Raw unprocessed facts without context]
    B --> B2[Information: Processed structured data with meaning]
    B --> B3[Knowledge: Synthesized understanding actionable]
    B --> B4[Wisdom: Strategic evaluated judgment]

    C --> C1[E.F. Codd 1970: Relational Model Tables/Tuples/Attributes]
    C --> C2[Keys: Primary unique not null, Foreign references parent, Candidate]
    C --> C3[SQL Commands: DDL Create/Alter, DML Select/Insert, DCL Grant, TCL Commit]
    C --> C4[ACID Properties: Atomicity, Consistency, Isolation, Durability]

    D --> D1[IaaS: Infrastructure virtual hardware AWS EC2, Azure VMs]
    D --> D2[PaaS: Platform runtime environment Google App Engine]
    D --> D3[SaaS: Ready software over web Google Docs, MS 365]

    E --> E1[Malware: Virus host file, Worm standalone self-replicating, Trojan backdoor]
    E --> E2[Attacks: Phishing credentials, Ransomware encryption, DDoS botnet]

    F --> F1[Enacted: Oct 17 2000 based on UNCITRAL model]
    F --> F2[Sections: Sec 43 Damage, Sec 65 Source code, Sec 66 Hacking, Sec 66C Identity theft, Sec 66F Cyber terrorism]
    F --> F3[CERT-In: National nodal agency for cyber incidents]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[सूचना प्रौद्योगिकी IT] --> B[DIKW सूचना पिरामिड]
    A --> C[रिलेशनल डेटाबेस RDBMS एवं SQL]
    A --> D[क्लाउड कंप्यूटिंग सेवा मॉडल]
    A --> E[साइबर सुरक्षा एवं खतरे]
    A --> F[सूचना प्रौद्योगिकी अधिनियम 2000]

    B --> B1[डेटा: कच्चे असंसाधित तथ्य बिना संदर्भ]
    B --> B2[सूचना: प्रसंस्कृत अर्थपूर्ण डेटा]
    B --> B3[ज्ञान: समझ व अनुभव पर आधारित कार्यान्वयन]
    B --> B4[प्रज्ञा: रणनीतिक व विवेकपूर्ण निर्णय]

    C --> C1[ई.एफ. कॉड 1970: रिलेशनल मॉडल टेबल/पंक्ति/कॉलम]
    C --> C2[कुंजियाँ: प्राइमरी की अद्वितीय, फॉरेन की संदर्भ, कैंडिडेट]
    C --> C3[SQL कमांड्स: DDL संरचना, DML डेटा संपादन, DCL अनुमति, TCL संव्यवहार]
    C --> C4[ACID गुण: Atomicity, Consistency, Isolation, Durability]

    D --> D1[IaaS: बुनियादी ढांचा वर्चुअल मशीन AWS EC2, Azure]
    D --> D2[PaaS: प्लेटफॉर्म रनटाइम गूगल ऐप इंजन]
    D --> D3[SaaS: तैयार सॉफ्टवेयर गूगल डॉक्स, माइक्रोसॉफ्ट 365]

    E --> E1[मैलवेयर: वायरस होस्ट फाइल, वॉर्म स्वतः प्रतिकृति, ट्रोजन बैकडोर]
    E --> E2[हमले: फ़िशिंग पासवर्ड चोरी, रैनसमवेयर फिरौती, DDoS हमला]

    F --> F1[लागू: 17 अक्टूबर 2000 UNCITRAL मॉडल पर आधारित]
    F --> F2[धाराएं: धारा 43 क्षतिपूर्ति, 65 स्रोत कोड, 66 हैकिंग, 66C पहचान चोरी, 66F साइबर आतंकवाद]
    F --> F3[CERT-In: साइबर घटनाओं की राष्ट्रीय नोडल एजेंसी]
    </div>
  </div>
</div>

<!-- Card 2: DIKW Pyramid & RDBMS SQL -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. The DIKW Information Pyramid &amp; Relational Databases (RDBMS/SQL)</span>
    <span class="lang-hi">1. DIKW सूचना पिरामिड एवं रिलेशनल डेटाबेस (RDBMS / SQL)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>The DIKW Hierarchy (Data, Information, Knowledge, Wisdom):</strong>
          <br>&bull; <strong>Data (कच्चा डेटा):</strong> Unprocessed, unorganized raw facts, figures, or symbols lacking context (e.g., <code>"38.5"</code>).
          <br>&bull; <strong>Information (सूचना):</strong> Data that has been processed, structured, and presented within context to give it meaning (e.g., <code>"Patient's body temperature is 38.5°C, indicating a fever"</code>).
          <br>&bull; <strong>Knowledge (ज्ञान):</strong> Information that has been comprehended, internalized, and combined with experience to enable action (e.g., <code>"Knowing which medication and cooling procedures to administer for 38.5°C fever"</code>).
          <br>&bull; <strong>Wisdom (प्रज्ञा / विवेक):</strong> The highest level involving evaluated understanding and ethical judgment to make optimal long-term decisions.</span>
        <span class="lang-hi"><strong>DIKW पदानुक्रम (डेटा, सूचना, ज्ञान, प्रज्ञा):</strong>
          <br>&bull; <strong>डेटा:</strong> असंसाधित, असंगठित कच्चे तथ्य या आंकड़े जिनका कोई संदर्भ नहीं होता (जैसे: <code>"38.5"</code>)।
          <br>&bull; <strong>सूचना:</strong> प्रसंस्कृत डेटा जिसे संदर्भ मिलने पर अर्थ प्राप्त होता है (जैसे: <code>"रोगी का तापमान 38.5°C है, यानी बुखार है"</code>)।
          <br>&bull; <strong>ज्ञान:</strong> सूचना का समझ और अनुभव के साथ समन्वय, जिससे निर्णय लिया जा सके (जैसे: <code>"बुखार उतारने हेतु कौन सी दवा देनी है"</code>)।
          <br>&bull; <strong>प्रज्ञा (Wisdom):</strong> दीर्घकालिक और विवेकपूर्ण निर्णय लेने की उच्चतम बौद्धिक क्षमता।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Relational Database Management Systems (RDBMS):</strong>
          <br>&bull; Proposed in <strong>1970</strong> by British computer scientist <strong>Dr. Edgar Frank Codd (E.F. Codd)</strong> at IBM in his paper defining the Relational Model (12 Codd's Rules).
          <br>&bull; Data is stored in two-dimensional tables called <strong>Relations</strong>, composed of horizontal rows called <strong>Tuples / Records</strong> and vertical columns called <strong>Attributes / Fields</strong>.
          <br>&bull; <strong>Keys in Relational Databases:</strong>
            <br>&nbsp;&nbsp;&bull; <strong>Primary Key:</strong> An attribute (or set of attributes) that uniquely identifies each record in a table. It cannot contain NULL values and must be strictly unique.
            <br>&nbsp;&nbsp;&bull; <strong>Foreign Key:</strong> A field in one table that references the Primary Key of another table, enforcing <em>Referential Integrity</em> between related tables.
            <br>&nbsp;&nbsp;&bull; <strong>Candidate Key:</strong> Any attribute that has the potential to become the Primary Key.</span>
        <span class="lang-hi"><strong>रिलेशनल डेटाबेस (RDBMS):</strong>
          <br>&bull; <strong>1970</strong> में IBM के <strong>डॉ. ई.एफ. कॉड (E.F. Codd)</strong> द्वारा प्रतिपादित (कॉड के 12 नियम)।
          <br>&bull; डेटा को 2-विमीय तालिकाओं (Relations) में रखा जाता है। पंक्तियों को <strong>टुपल्स (Tuples / Records)</strong> और कॉलमों को <strong>एट्रीब्यूट्स (Attributes / Fields)</strong> कहते हैं।
          <br>&bull; <strong>डेटाबेस कुंजियाँ (Keys):</strong>
            <br>&nbsp;&nbsp;&bull; <strong>प्राइमरी की (Primary Key):</strong> तालिका में प्रत्येक रिकॉर्ड की विशिष्ट पहचान; इसमें कभी भी NULL (खाली) मान नहीं हो सकता।
            <br>&nbsp;&nbsp;&bull; <strong>फॉरेन की (Foreign Key):</strong> दूसरी तालिका की प्राइमरी की को संदर्भित कर दोनों तालिकाओं में संबंध बनाती है (Referential Integrity)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>SQL (Structured Query Language) Command Categories:</strong>
          <br>&bull; <strong>DDL (Data Definition Language):</strong> Defines database schema structure: <code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code>, <code>RENAME</code>.
          <br>&bull; <strong>DML (Data Manipulation Language):</strong> Modifies and queries data: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>.
          <br>&bull; <strong>DCL (Data Control Language):</strong> Manages user permissions: <code>GRANT</code>, <code>REVOKE</code>.
          <br>&bull; <strong>TCL (Transaction Control Language):</strong> Manages database transactions: <code>COMMIT</code> (permanently save), <code>ROLLBACK</code> (undo uncommitted changes), <code>SAVEPOINT</code>.
          <br>&bull; <strong>ACID Properties:</strong> <strong>A</strong>tomicity (all operations succeed or all fail), <strong>C</strong>onsistency (valid states maintained), <strong>I</strong>solation (transactions do not interfere), <strong>D</strong>urability (committed data survives system crashes).</span>
        <span class="lang-hi"><strong>SQL कमांड्स का वर्गीकरण:</strong>
          <br>&bull; <strong>DDL (डेटा डेफिनिशन):</strong> डेटाबेस का ढांचा तैयार करना: <code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code>।
          <br>&bull; <strong>DML (डेटा मैनिपुलेशन):</strong> डेटा देखना व बदलना: <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>।
          <br>&bull; <strong>DCL (डेटा कंट्रोल):</strong> अधिकार देना/हटाना: <code>GRANT</code>, <code>REVOKE</code>।
          <br>&bull; <strong>TCL (ट्रांजेक्शन कंट्रोल):</strong> <code>COMMIT</code> (स्थायी रूप से सहेजना), <code>ROLLBACK</code> (पूर्ववत करना)।
          <br>&bull; <strong>ACID गुण:</strong> Atomicity (पूर्ण या शून्य), Consistency (नियमों की संगति), Isolation (अलगाव), Durability (स्थायित्व)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Cloud Computing Models -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Cloud Computing Service &amp; Deployment Models</span>
    <span class="lang-hi">2. क्लाउड कंप्यूटिंग सेवा एवं परिनियोजन मॉडल</span>
  </div>
  <div class="content-block">
    <p>
      <span class="lang-en"><strong>Cloud Computing</strong> is the on-demand delivery of computing services—including servers, storage, databases, networking, software, and analytics—over the Internet ("the cloud") with pay-as-you-go pricing.</span>
      <span class="lang-hi"><strong>क्लाउड कंप्यूटिंग</strong> इंटरनेट के माध्यम से मांग पर कंप्यूटिंग सेवाएं—जैसे सर्वर, स्टोरेज, डेटाबेस, नेटवर्किंग और सॉफ्टवेयर—उपलब्ध कराने की प्रणाली है।</span>
    </p>
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Service Model</span><span class="lang-hi">सेवा मॉडल</span></th>
          <th><span class="lang-en">Full Form</span><span class="lang-hi">पूर्ण रूप</span></th>
          <th><span class="lang-en">User Manages</span><span class="lang-hi">उपयोगकर्ता प्रबंधन</span></th>
          <th><span class="lang-en">Vendor Manages</span><span class="lang-hi">कंपनी प्रबंधन</span></th>
          <th><span class="lang-en">Popular Industry Examples</span><span class="lang-hi">प्रमुख उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>IaaS</strong></td>
          <td>Infrastructure as a Service</td>
          <td><span class="lang-en">Operating System, Applications, Middleware, Runtime, Data</span><span class="lang-hi">OS, सॉफ्टवेयर, डेटा</span></td>
          <td><span class="lang-en">Virtualization, Physical Servers, Storage, Networking hardware</span><span class="lang-hi">भौतिक सर्वर, स्टोरेज, हार्डवेयर</span></td>
          <td>Amazon Web Services (AWS EC2), Microsoft Azure Virtual Machines, Google Compute Engine (GCE)</td>
        </tr>
        <tr>
          <td><strong>PaaS</strong></td>
          <td>Platform as a Service</td>
          <td><span class="lang-en">Applications and Data code only</span><span class="lang-hi">केवल एप्लीकेशन कोड और डेटा</span></td>
          <td><span class="lang-en">Operating System, Runtime environment, Database engine, Hardware</span><span class="lang-hi">OS, रनटाइम, डेटाबेस, हार्डवेयर</span></td>
          <td>Google App Engine, AWS Elastic Beanstalk, Heroku</td>
        </tr>
        <tr>
          <td><strong>SaaS</strong></td>
          <td>Software as a Service</td>
          <td><span class="lang-en">None (User just uses the software via web browser)</span><span class="lang-hi">कुछ नहीं (केवल ब्राउज़र में सॉफ्टवेयर चलाना)</span></td>
          <td><span class="lang-en">Everything (Application, Data, OS, Servers, Security, Upgrades)</span><span class="lang-hi">सब कुछ क्लाउड प्रदाता संभालता है</span></td>
          <td>Google Docs / Gmail, Microsoft 365, Dropbox, Salesforce, Zoom</td>
        </tr>
      </tbody>
    </table>
    <div style="margin-top:16px; padding:12px 16px; background:var(--primary-light); border-left:4px solid var(--primary); border-radius:6px;">
      <span class="lang-en"><strong>MeghRaj (GI Cloud):</strong> Government of India's sovereign cloud initiative implemented by NIC to accelerate delivery of e-services across states and central departments with high security.</span>
      <span class="lang-hi"><strong>मेघराज (GI Cloud):</strong> भारत सरकार की राष्ट्रीय क्लाउड पहल, जिसे NIC द्वारा संचालित किया जाता है ताकि सरकारी ई-सेवाओं को सुरक्षित और तीव्र गति से चलाया जा सके।</span>
    </div>
  </div>
</div>

<!-- Card 4: Cyber Security Threats & Attacks -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Cyber Security Threats, Malware Classification &amp; Cyber Attacks</span>
    <span class="lang-hi">3. साइबर सुरक्षा खतरे, मैलवेयर का वर्गीकरण एवं साइबर हमले</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Malware Type</span><span class="lang-hi">मैलवेयर प्रकार</span></th>
          <th><span class="lang-en">Propagation Mechanism</span><span class="lang-hi">फैलने की कार्यप्रणाली</span></th>
          <th><span class="lang-en">Host File / Human Needed?</span><span class="lang-hi">होस्ट फाइल की आवश्यकता?</span></th>
          <th><span class="lang-en">Destructive Action &amp; Examples</span><span class="lang-hi">हानि एवं ऐतिहासिक उदाहरण</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Computer Virus</strong></td>
          <td><span class="lang-en">Attaches itself to an executable program (<code>.exe</code>, <code>.docx</code>) and replicates when the infected host program is executed by a user.</span><span class="lang-hi">किसी अन्य वैध फाइल (.exe आदि) से चिपकता है और जब यूजर उसे चलाता है तब फैलता है।</span></td>
          <td><span class="lang-en"><strong>YES</strong> (Requires host file and user action)</span><span class="lang-hi"><strong>हाँ</strong> (होस्ट फाइल अनिवार्य)</span></td>
          <td>Corrupts files, deletes data. First PC virus: <strong>Brain</strong> (1986, boot sector virus by Alvi brothers, Pakistan); Creeper (1971, ARPANET).</td>
        </tr>
        <tr>
          <td><strong>Computer Worm</strong></td>
          <td><span class="lang-en">Standalone software that self-replicates across computer networks automatically through vulnerabilities without needing a host file or human intervention.</span><span class="lang-hi">स्वतंत्र प्रोग्राम जो बिना किसी मानवीय हस्तक्षेप के नेटवर्क की कमियों से स्वतः फैलता है।</span></td>
          <td><span class="lang-en"><strong>NO</strong> (Independent standalone program)</span><span class="lang-hi"><strong>नहीं</strong> (स्वतंत्र प्रोग्राम)</span></td>
          <td>Consumes network bandwidth, crashes servers. Examples: Morris Worm (1988, Robert Morris), ILOVEYOU (2000), Code Red.</td>
        </tr>
        <tr>
          <td><strong>Trojan Horse</strong></td>
          <td><span class="lang-en">Disguised as useful, legitimate software (e.g., game, utility) to trick user into downloading; opens covert backdoor for hackers.</span><span class="lang-hi">दिखने में उपयोगी सॉफ्टवेयर जैसा लगता है, परंतु कंप्यूटर में हैकर्स के लिए गुप्त चोर-दरवाजा (Backdoor) खोल देता है।</span></td>
          <td><span class="lang-en">Does <strong>NOT replicate</strong> itself</span><span class="lang-hi">यह अपनी प्रतियां <strong>नहीं बनाता</strong></span></td>
          <td>Steals passwords, financial credentials, logs keystrokes. Example: Zeus Trojan, Netbus.</td>
        </tr>
        <tr>
          <td><strong>Ransomware</strong></td>
          <td><span class="lang-en">Malicious software that encrypts user files with uncrackable cryptography (AES/RSA) and displays a ransom demand (usually in Bitcoin) to decrypt them.</span><span class="lang-hi">उपयोगकर्ता की फाइलों को जटिल पासवर्ड से लॉक (एन्क्रिप्ट) कर देता है और खोलने के बदले फिरौती (Ransom) मांगता है।</span></td>
          <td>Standalone or Trojan delivery</td>
          <td>Paralyzes hospitals, banks, and pipelines. Examples: <strong>WannaCry</strong> (2017), Petya, Locky.</td>
        </tr>
        <tr>
          <td><strong>Spyware / Keylogger</strong></td>
          <td><span class="lang-en">Secretly monitors and logs user keystrokes, browsing history, webcam, and audio without user consent.</span><span class="lang-hi">उपयोगकर्ता की जासूसी करता है और कीबोर्ड पर दबाए गए पासवर्ड रिकॉर्ड करता है।</span></td>
          <td>Stealth background installation</td>
          <td>Identity theft, corporate espionage. Example: <strong>Pegasus Spyware</strong>.</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 5: Information Technology Act 2000 -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. The Information Technology Act, 2000 (IT Act 2000) - Core Sections</span>
    <span class="lang-hi">4. सूचना प्रौद्योगिकी अधिनियम, 2000 (IT Act 2000) - महत्वपूर्ण धाराएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Overview of the IT Act 2000:</strong>
          <br>&bull; Enacted by the Indian Parliament and notified on <strong>October 17, 2000</strong> based on the United Nations Commission on International Trade Law (UNCITRAL) Model Law on Electronic Commerce (1996).
          <br>&bull; Provides legal recognition to electronic transactions, digital signatures, and electronic records.
          <br>&bull; Extends to the whole of India and applies to any cyber offense committed outside India if it involves a computer resource located in India. Major amendments made in <strong>2008</strong> (IT Amendment Act 2008).</span>
        <span class="lang-hi"><strong>सूचना प्रौद्योगिकी अधिनियम, 2000 का संक्षिप्त परिचय:</strong>
          <br>&bull; भारतीय संसद द्वारा पारित होकर <strong>17 अक्टूबर 2000</strong> को लागू हुआ (संयुक्त राष्ट्र के UNCITRAL मॉडल लॉ पर आधारित)।
          <br>&bull; इलेक्ट्रॉनिक लेन-देन, डिजिटल हस्ताक्षर और इलेक्ट्रॉनिक दस्तावेजों को कानूनी मान्यता प्रदान करता है।
          <br>&bull; यह संपूर्ण भारत में तथा भारत से बाहर किए गए उन सभी अपराधों पर भी लागू होता है जिनका संबंध भारत स्थित कंप्यूटर से हो। वर्ष 2008 में इसमें बड़ा संशोधन किया गया था।</span>
      </li>
    </ul>

    <table class="comparison-table">
      <thead>
        <tr>
          <th><span class="lang-en">Section</span><span class="lang-hi">धारा</span></th>
          <th><span class="lang-en">Offense / Provision</span><span class="lang-hi">अपराध / प्रावधान</span></th>
          <th><span class="lang-en">Prescribed Legal Penalty</span><span class="lang-hi">कानूनी दंड</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Section 43</strong></td>
          <td><span class="lang-en">Penalty for damage to computer systems, unauthorized downloading, virus insertion, or data extraction.</span><span class="lang-hi">कंप्यूटर को नुकसान पहुंचाना, वायरस डालना, अनधिकृत डेटा कॉपी करना।</span></td>
          <td><span class="lang-en">Civil compensation up to <strong>₹1 Crore</strong> to the affected person.</span><span class="lang-hi">पीड़ित को <strong>1 करोड़ रुपये तक</strong> का हर्जाना।</span></td>
        </tr>
        <tr>
          <td><strong>Section 65</strong></td>
          <td><span class="lang-en">Tampering with computer source documents (programming source code).</span><span class="lang-hi">कंप्यूटर सोर्स कोड (दस्तावेजों) से छेड़छाड़ करना।</span></td>
          <td><span class="lang-en">Imprisonment up to <strong>3 years</strong>, or fine up to <strong>₹2 Lakh</strong>, or both.</span><span class="lang-hi"><strong>3 वर्ष तक कारावास</strong>, या <strong>₹2 लाख तक जुर्माना</strong>, या दोनों।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66</strong></td>
          <td><span class="lang-en">Computer-related offenses (Hacking, unauthorized access with fraudulent intent).</span><span class="lang-hi">कंप्यूटर संबंधी अपराध (हैकिंग, अनधिकृत डेटा चोरी)।</span></td>
          <td><span class="lang-en">Imprisonment up to <strong>3 years</strong>, or fine up to <strong>₹5 Lakh</strong>, or both.</span><span class="lang-hi"><strong>3 वर्ष तक जेल</strong>, या <strong>₹5 लाख तक जुर्माना</strong>।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66B</strong></td>
          <td><span class="lang-en">Dishonestly receiving stolen computer resource or communication device.</span><span class="lang-hi">चोरी का कंप्यूटर या मोबाइल फोन बेईमानी से प्राप्त करना।</span></td>
          <td><span class="lang-en">Imprisonment up to 3 years, or fine up to ₹1 Lakh, or both.</span><span class="lang-hi">3 वर्ष तक जेल, या ₹1 लाख जुर्माना।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66C</strong></td>
          <td><span class="lang-en"><strong>Identity Theft:</strong> Fraudulent use of another person's electronic signature, password, or biometric.</span><span class="lang-hi"><strong>पहचान की चोरी:</strong> दूसरे के पासवर्ड, डिजिटल हस्ताक्षर या बायोमेट्रिक का दुरुपयोग।</span></td>
          <td><span class="lang-en">Imprisonment up to 3 years and fine up to ₹1 Lakh.</span><span class="lang-hi">3 वर्ष तक जेल एवं ₹1 लाख जुर्माना।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66D</strong></td>
          <td><span class="lang-en"><strong>Cheating by Impersonation:</strong> Using a computer resource to impersonate someone else fraudulently.</span><span class="lang-hi"><strong>प्रतिरूपण द्वारा धोखाधड़ी:</strong> कंप्यूटर से किसी अन्य व्यक्ति का रूप धारण कर ठगी करना।</span></td>
          <td><span class="lang-en">Imprisonment up to 3 years and fine up to ₹1 Lakh.</span><span class="lang-hi">3 वर्ष तक जेल एवं ₹1 लाख जुर्माना।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66E</strong></td>
          <td><span class="lang-en"><strong>Violation of Privacy:</strong> Capturing, publishing, or transmitting images of private area of a person without consent.</span><span class="lang-hi"><strong>निजता का उल्लंघन:</strong> बिना सहमति किसी व्यक्ति के निजी अंगों की तस्वीरें खींचना या प्रसारित करना।</span></td>
          <td><span class="lang-en">Imprisonment up to 3 years, or fine up to ₹2 Lakh, or both.</span><span class="lang-hi">3 वर्ष तक जेल, या ₹2 लाख तक जुर्माना।</span></td>
        </tr>
        <tr>
          <td><strong>Section 66F</strong></td>
          <td><span class="lang-en"><strong>Cyber Terrorism:</strong> Acts threatening unity, integrity, security or sovereignty of India via cyber means.</span><span class="lang-hi"><strong>साइबर आतंकवाद:</strong> भारत की संप्रभुता, एकता व सुरक्षा को साइबर माध्यम से खतरा पहुंचाना।</span></td>
          <td><span class="lang-en"><strong>Imprisonment for LIFE</strong> (आजीवन कारावास).</span><span class="lang-hi"><strong>आजीवन कारावास (Life Imprisonment)</strong>।</span></td>
        </tr>
        <tr>
          <td><strong>Section 67</strong></td>
          <td><span class="lang-en">Publishing or transmitting obscene material in electronic form.</span><span class="lang-hi">इलेक्ट्रॉनिक रूप में अश्लील सामग्री का प्रकाशन या प्रसारण।</span></td>
          <td><span class="lang-en">First conviction: Up to 3 years jail + ₹5 Lakh fine. Subsequent: Up to 5 years + ₹10 Lakh.</span><span class="lang-hi">प्रथम बार: 3 वर्ष जेल + ₹5 लाख जुर्माना; दोबारा: 5 वर्ष जेल।</span></td>
        </tr>
      </tbody>
    </table>
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
          <td><span class="lang-en">Date on which the Information Technology Act 2000 came into force in India</span><span class="lang-hi">भारत में IT Act 2000 लागू होने की तिथि</span></td>
          <td><span class="lang-en"><strong>17 October 2000</strong>.</span><span class="lang-hi"><strong>17 अक्टूबर 2000</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Section of IT Act 2000 penalizing Cyber Terrorism with life imprisonment</span><span class="lang-hi">साइबर आतंकवाद हेतु आजीवन कारावास का प्रावधान करने वाली धारा</span></td>
          <td><span class="lang-en"><strong>Section 66F</strong>.</span><span class="lang-hi"><strong>धारा 66F</strong> (आजीवन कारावास)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Section of IT Act 2000 penalizing tampering with computer source code</span><span class="lang-hi">कंप्यूटर सोर्स कोड से छेड़छाड़ पर दंड की धारा</span></td>
          <td><span class="lang-en"><strong>Section 65</strong> (Up to 3 years imprisonment or ₹2 Lakh fine).</span><span class="lang-hi"><strong>धारा 65</strong> (3 वर्ष जेल या ₹2 लाख जुर्माना)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">India's national agency for responding to cybersecurity incidents</span><span class="lang-hi">साइबर सुरक्षा घटनाओं की जांच हेतु भारत की नोडल एजेंसी</span></td>
          <td><span class="lang-en"><strong>CERT-In</strong> (Indian Computer Emergency Response Team, under MeitY).</span><span class="lang-hi"><strong>CERT-In</strong> (इलेक्ट्रॉनिक्स व आईटी मंत्रालय)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Father of Relational Database Management Systems (RDBMS)</span><span class="lang-hi">रिलेशनल डेटाबेस (RDBMS) के जनक</span></td>
          <td><span class="lang-en"><strong>Dr. E.F. Codd</strong> (proposed 12 Codd's Rules in 1970).</span><span class="lang-hi"><strong>डॉ. ई.एफ. कॉड (E.F. Codd)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Database key that uniquely identifies records and cannot contain NULL values</span><span class="lang-hi">रिकॉर्ड को विशिष्ट पहचान देने वाली कुंजी जिसमें NULL मान नहीं हो सकता</span></td>
          <td><span class="lang-en"><strong>Primary Key</strong>.</span><span class="lang-hi"><strong>प्राइमरी की (Primary Key)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">SQL command used to permanently save all changes made in a transaction</span><span class="lang-hi">लेन-देन के सभी बदलावों को स्थायी रूप से सहेजने वाली SQL कमांड</span></td>
          <td><span class="lang-en"><strong>COMMIT</strong> (TCL command).</span><span class="lang-hi"><strong>COMMIT</strong> (TCL कमांड)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Cloud service model where user accesses ready software over web browser</span><span class="lang-hi">ब्राउज़र में सीधे सॉफ्टवेयर उपलब्ध कराने वाला क्लाउड मॉडल</span></td>
          <td><span class="lang-en"><strong>SaaS</strong> (Software as a Service, e.g., Google Docs, Microsoft 365).</span><span class="lang-hi"><strong>SaaS</strong> (सॉफ्टवेयर ऐज ए सर्विस)।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Self-replicating malware that spreads across networks without a host file</span><span class="lang-hi">बिना किसी होस्ट फाइल के नेटवर्क पर स्वतः फैलने वाला मैलवेयर</span></td>
          <td><span class="lang-en"><strong>Computer Worm</strong>.</span><span class="lang-hi"><strong>कंप्यूटर वॉर्म (Worm)</strong>।</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">First IBM PC computer virus in history</span><span class="lang-hi">इतिहास का पहला IBM PC कंप्यूटर वायरस</span></td>
          <td><span class="lang-en"><strong>Brain Virus</strong> (1986, boot sector virus created by Alvi brothers).</span><span class="lang-hi"><strong>ब्रेन (Brain Virus - 1986)</strong>।</span></td>
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
    enrich_file("big-data-processing", build_big_data_theory_html())
    enrich_file("internet-of-things", build_iot_theory_html())
    enrich_file("it-gadgets-and-their-applications", build_it_gadgets_theory_html())
    enrich_file("information-technology", build_information_technology_theory_html())

if __name__ == "__main__":
    main()
