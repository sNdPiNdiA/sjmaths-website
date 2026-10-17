# Topic 9: Big Data Processing
mm_t9 = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Big Data Architecture, Hadoop, Spark &amp; NoSQL</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: बिग डेटा प्रोसेसिंग, हडूप पारिस्थितिकी, स्पार्क एवं NoSQL</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • The 5 V's of Big Data • Hadoop (HDFS, YARN, MapReduce) • Apache Spark In-Memory • NoSQL &amp; CAP Theorem • UP State Analytics</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • बिग डेटा के 5 V's • हडूप (HDFS, YARN, मैप-रिड्यूस) • अपाचे स्पार्क इन-मेमोरी • NoSQL एवं CAP प्रमेय • उप्र शासन डेटा एनालिटिक्स</span>
        </p>
    </div>

    <!-- Central Hub -->
    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-database"></i>
            <span class="lang-en">Big Data Distributed Computing Architecture</span>
            <span class="lang-hi">बिग डेटा वितरित कंप्यूटिंग वास्तुकला</span>
        </div>
    </div>

    <!-- 6 Branch Nodes Grid -->
    <div class="mindmap-grid">

        <!-- Branch 1: The 5 V's & Definition -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cubes" style="color: #059669;"></i>
                    <span class="lang-en">1. Definition &amp; The 5 V's</span>
                    <span class="lang-hi">1. बिग डेटा परिभाषा एवं 5 V's</span>
                </h4>
                <span class="mindmap-node-tag">Doug Laney 2001 • 5 V's</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">The 5 V's Dimensions</span>
                        <span class="lang-hi">बिग डेटा के 5 प्रमुख आयाम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Volume</strong> (Terabytes to Zettabytes)</span>
                        <span class="mindmap-chip"><strong>Velocity</strong> (Real-Time Streams)</span>
                        <span class="mindmap-chip"><strong>Variety</strong> (Structured / Semi / Unstructured)</span>
                        <span class="mindmap-chip"><strong>Veracity</strong> (Trustworthiness &amp; Noise)</span>
                        <span class="mindmap-chip"><strong>Value</strong> (Actionable Business ROI)</span>
                        <span class="mindmap-chip"><strong>Doug Laney</strong> (Original 3 V's, 2001)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Detailed Meaning of Each Dimension</span>
                        <span class="lang-hi">प्रत्येक आयाम का विस्तृत अर्थ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Big Data Definition:</strong> Massive, complex datasets that exceed processing capacity of conventional Relational Database Management Systems (RDBMS). Doug Laney introduced original 3 V's (Volume, Velocity, Variety) in 2001 at META Group/Gartner.</span>
                            <span class="lang-hi"><strong>बिग डेटा परिभाषा:</strong> इतना विशाल व जटिल डेटा जिसे पारंपरिक रिलेशनल डेटाबेस (RDBMS) द्वारा प्रोसेस नहीं किया जा सकता। डग लैनी ने 2001 में मूल 3 V's (वॉल्यूम, वेलोसिटी, वैरायटी) प्रस्तुत किए।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Volume, Velocity &amp; Variety:</strong> <strong>Volume:</strong> Sheer scale of data generated (PB, EB, ZB). <strong>Velocity:</strong> Speed at which data arrives and must be processed (batch vs real-time IoT feeds). <strong>Variety:</strong> Diverse types (text, clickstreams, images, audio, video).</span>
                            <span class="lang-hi"><strong>वॉल्यूम, वेलोसिटी एवं वैरायटी:</strong> <strong>वॉल्यूम:</strong> डेटा का विशाल परिमाण (पेटाबाइट, जेटाबाइट)। <strong>वेलोसिटी:</strong> डेटा उत्पादन व प्रवाह की तीव्र गति (रियल-टाइम)। <strong>वैरायटी:</strong> डेटा के विभिन्न प्रकार (ऑडियो, वीडियो, टेक्स्ट, लॉग्स)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Veracity &amp; Value:</strong> <strong>Veracity:</strong> Cleanliness, reliability, and accuracy of data (handling noise, bias, anomalies). <strong>Value:</strong> Ultimate business or governance outcome extracted from analyzing raw data.</span>
                            <span class="lang-hi"><strong>वेरासिटी एवं वैल्यू:</strong> <strong>वेरासिटी (सत्यता):</strong> डेटा की प्रामाणिकता, शुद्धता और विश्वसनीयता (शोर व गलतियों की छंटनी)। <strong>वैल्यू (मूल्य):</strong> विश्लेषण के पश्चात प्राप्त उपयोगी परिणाम व निर्णय शक्ति।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Doug Laney introduced the original 3 V's in 2001; the expanded 5 V's are Volume, Velocity, Variety, Veracity, and Value!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> डग लैनी ने 2001 में मूल 3 V's दिए थे; बिग डेटा के 5 V's हैं: वॉल्यूम, वेलोसिटी, वैरायटी, वेरासिटी और वैल्यू!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Data Classification & File Formats -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-file-alt" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Data Types &amp; Formats</span>
                    <span class="lang-hi">2. डेटा प्रारूप एवं स्टोरेज फॉर्मेट्स</span>
                </h4>
                <span class="mindmap-node-tag">Structured • Parquet • ORC</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Classifications &amp; Formats</span>
                        <span class="lang-hi">डेटा श्रेणियां एवं स्टोरेज प्रारूप</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Structured</strong> (RDBMS Tables, SQL)</span>
                        <span class="mindmap-chip"><strong>Semi-Structured</strong> (JSON, XML, YAML)</span>
                        <span class="mindmap-chip"><strong>Unstructured</strong> (80% Data, Video/Audio/PDF)</span>
                        <span class="mindmap-chip"><strong>Apache Parquet</strong> (Columnar, Fast Analytics)</span>
                        <span class="mindmap-chip"><strong>Apache ORC</strong> (Optimized Row Columnar)</span>
                        <span class="mindmap-chip"><strong>Apache Avro</strong> (Row-based, Schema Evolution)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Characteristics &amp; Columnar Storage</span>
                        <span class="lang-hi">विशेषताएं एवं कॉलमनर स्टोरेज का महत्व</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Three Data Formats:</strong> <strong>Structured Data:</strong> Predefined schema, tabular rows and columns (e.g. MySQL, Oracle, bank ledgers). <strong>Semi-Structured:</strong> Self-describing schema with hierarchical tags (JSON, XML, CSV). <strong>Unstructured Data:</strong> No predefined data model (~80-90% of all data; text emails, PDF contracts, CCTV video, social media posts).</span>
                            <span class="lang-hi"><strong>डेटा के तीन रूप:</strong> <strong>संरचित (Structured):</strong> निश्चित स्कीमा, पंक्ति-स्तंभ युक्त टेबल (SQL डेटाबेस)। <strong>अर्ध-संरचित (Semi-Structured):</strong> टैग्स व की-वैल्यू पर आधारित (JSON, XML)। <strong>असंरचित (Unstructured):</strong> बिना किसी पूर्व-निर्धारित संरचना वाला ~80% डेटा (वीडियो, ऑडियो, ईमेल, PDF)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Columnar Storage (Parquet / ORC):</strong> Unlike row-oriented formats (CSV, Avro), Columnar storage groups data by column. When querying specific columns (e.g. <code>SELECT AVG(salary)</code>), it only reads relevant disk blocks, reducing disk I/O by 90%+ and enabling extreme data compression (Snappy).</span>
                            <span class="lang-hi"><strong>कॉलमनर स्टोरेज (Parquet / ORC):</strong> डेटा को पंक्तियों के बजाय स्तंभों में संग्रहीत करता है; जब केवल कुछ स्तंभ पढ़ने हों तो पूरे डेटा को पढ़ने की आवश्यकता नहीं होती, जिससे 90%+ डिस्क I/O बचता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> ~80-90% of enterprise data is Unstructured; Apache Parquet is a columnar storage file format optimized for fast analytical queries!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> विश्व का लगभग 80-90% डेटा 'असंरचित' (Unstructured) है; अपाचे पारकेट (Parquet) कॉलमनर स्टोरेज प्रारूप है जो तेज एनालिटिक्स देता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Apache Hadoop Ecosystem (HDFS, YARN, MapReduce) -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-elephant" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Apache Hadoop Ecosystem</span>
                    <span class="lang-hi">3. अपाचे हडूप वितरित पारिस्थितिकी</span>
                </h4>
                <span class="mindmap-node-tag">Doug Cutting 2006 • HDFS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Hadoop Components &amp; Architecture</span>
                        <span class="lang-hi">हडूप के घटक एवं वास्तुकला</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Doug Cutting &amp; Mike Cafarella</strong> (2006)</span>
                        <span class="mindmap-chip"><strong>HDFS</strong> (NameNode Master, DataNode Worker)</span>
                        <span class="mindmap-chip"><strong>Block Size</strong> (Default 128 MB)</span>
                        <span class="mindmap-chip"><strong>Replication Factor</strong> (Default 3 Copies)</span>
                        <span class="mindmap-chip"><strong>YARN</strong> (Yet Another Resource Negotiator)</span>
                        <span class="mindmap-chip"><strong>MapReduce</strong> (Map -> Shuffle &amp; Sort -> Reduce)</span>
                        <span class="mindmap-chip"><strong>Hive &amp; Pig</strong> (SQL &amp; Scripting)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">HDFS &amp; MapReduce Mechanics</span>
                        <span class="lang-hi">HDFS एवं मैप-रिड्यूस कार्यप्रणाली</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hadoop Origins (2006):</strong> Created by Doug Cutting &amp; Mike Cafarella based on Google's GFS (2003) and MapReduce (2004) whitepapers; named after toy yellow elephant. Open-source framework for distributed storage and processing across clusters of commodity hardware.</span>
                            <span class="lang-hi"><strong>हडूप का उद्भव (2006):</strong> डग कटिंग व माइक कैफेरेला द्वारा गूगल के शोधपत्रों पर आधारित; सामान्य हार्डवेयर क्लस्टर पर विशाल डेटा संचयन व प्रोसेसिंग का ओपन-सोर्स ढांचा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>HDFS Master-Worker Architecture:</strong> <strong>NameNode (Master):</strong> Manages filesystem namespace, metadata, and maps data blocks to DataNodes. <strong>DataNode (Worker):</strong> Stores actual data blocks on local disks. Default block size is <strong>128 MB</strong>; default replication factor is <strong>3</strong> (rack awareness prevents data loss).</span>
                            <span class="lang-hi"><strong>HDFS मास्टर-वर्कर वास्तुकला:</strong> <strong>नेमनोड (NameNode - मास्टर):</strong> मेटाडेटा और फाइल डायरेक्टरी रखता है। <strong>डेटानेम (DataNode - वर्कर):</strong> वास्तविक डेटा ब्लॉक्स सुरक्षित रखता है। डिफॉल्ट ब्लॉक आकार <strong>128 MB</strong> तथा डिफॉल्ट प्रतिकृति (Replication Factor) <strong>3</strong> है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>MapReduce Computation:</strong> <strong>Map:</strong> Takes input chunks, applies user function, outputs key-value pairs <code>(K1, V1) -> list(K2, V2)</code>. <strong>Shuffle &amp; Sort:</strong> Groups all values sharing identical key. <strong>Reduce:</strong> Aggregates intermediate values for each key <code>(K2, list(V2)) -> list(K3, V3)</code>.</span>
                            <span class="lang-hi"><strong>मैप-रिड्यूस प्रोसेसिंग:</strong> <strong>मैप:</strong> इनपुट डेटा को की-वैल्यू पेयर में तोड़ता है। <strong>शफल व सॉर्ट:</strong> समान की (Keys) वाले डेटा को एक साथ समूहीकृत करता है। <strong>रिड्यूस:</strong> एकत्रित डेटा का योग या गणना कर अंतिम परिणाम देता है।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> HDFS default block size is 128 MB; default replication factor is 3; NameNode is the Master storing metadata while DataNode stores actual data!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> HDFS में डिफॉल्ट ब्लॉक आकार 128 MB और रेप्लिकेशन फैक्टर 3 होता है; नेमनोड मेटाडेटा का मास्टर है तथा डेटानेम वास्तविक डेटा रखता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Apache Spark & In-Memory Distributed Computing -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-bolt" style="color: #d97706;"></i>
                    <span class="lang-en">4. Apache Spark &amp; In-Memory</span>
                    <span class="lang-hi">4. अपाचे स्पार्क एवं इन-मेमोरी कंप्यूटिंग</span>
                </h4>
                <span class="mindmap-node-tag">100x Faster • RDD • DAG</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Spark Core &amp; Ecosystem</span>
                        <span class="lang-hi">स्पार्क के घटक एवं अमूर्त संरचनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Matei Zaharia</strong> (UC Berkeley AMPLab 2009)</span>
                        <span class="mindmap-chip"><strong>100x Speed</strong> (In-Memory Processing)</span>
                        <span class="mindmap-chip"><strong>RDD</strong> (Resilient Distributed Dataset)</span>
                        <span class="mindmap-chip"><strong>DAG Engine</strong> (Directed Acyclic Graph)</span>
                        <span class="mindmap-chip"><strong>Lazy Evaluation</strong> (Transformations vs Actions)</span>
                        <span class="mindmap-chip"><strong>Spark SQL &amp; DataFrames</strong></span>
                        <span class="mindmap-chip"><strong>Spark Streaming &amp; MLlib</strong></span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Spark In-Memory Architecture vs MapReduce</span>
                        <span class="lang-hi">स्पार्क इन-मेमोरी बनाम हडूप मैप-रिड्यूस</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Why Spark is 100x Faster:</strong> MapReduce writes intermediate state back to slow physical disks between every map and reduce phase. Apache Spark keeps intermediate computation in cluster RAM (In-Memory Computing), performing iterative algorithms up to 100x faster than MapReduce.</span>
                            <span class="lang-hi"><strong>स्पार्क 100 गुना तेज क्यों है:</strong> मैप-रिड्यूस प्रत्येक चरण के बाद डेटा को धीमी हार्ड डिस्क पर लिखता है। स्पार्क मध्यवर्ती गणनाओं को सीधे क्लस्टर की रैम (इन-मेमोरी) में रखता है, जिससे चक्रीय एल्गोरिदम 100 गुना तेज चलते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>RDD (Resilient Distributed Dataset):</strong> Fundamental data structure of Spark. Immutable, fault-tolerant collection of elements partitioned across cluster nodes. Fault tolerance achieved via <strong>Lineage Graph</strong> (re-computes lost partitions without data replication).</span>
                            <span class="lang-hi"><strong>RDD (रेज़िलिएंट डिस्ट्रीब्यूटेड डेटासेट):</strong> स्पार्क की मूल संरचना। अपरिवर्तनीय, फॉल्ट-टॉलरेंट डेटा समूह। यदि कोई नोड क्रैश हो जाए तो लीनिएज ग्राफ खोए हुए हिस्से को मेमोरी में पुनः बना लेता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Transformations vs Actions:</strong> <strong>Transformations:</strong> Create new RDD from existing RDD (e.g. <code>map()</code>, <code>filter()</code>); evaluated lazily (computation NOT executed until action called). <strong>Actions:</strong> Trigger actual computation and return value to driver (e.g. <code>count()</code>, <code>collect()</code>, <code>save()</code>).</span>
                            <span class="lang-hi"><strong>ट्रांसफॉर्मेशन बनाम एक्शन:</strong> <strong>ट्रांसफॉर्मेशन:</strong> नया RDD बनाते हैं (map, filter); लेज़ी इवैल्यूएशन (तुरंत निष्पादित नहीं होते)। <strong>एक्शन:</strong> वास्तविक गणना शुरू कराते हैं (count, collect, save)।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Spark is up to 100x faster than MapReduce due to in-memory processing; RDD is the core abstraction; Spark uses Lazy Evaluation!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> इन-मेमोरी प्रोसेसिंग के कारण स्पार्क मैप-रिड्यूस से 100 गुना तेज है; RDD स्पार्क की मुख्य इकाई है; स्पार्क लेज़ी इवैल्यूएशन पर कार्य करता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: NoSQL Databases & The CAP Theorem -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-th-list" style="color: #dc2626;"></i>
                    <span class="lang-en">5. NoSQL &amp; The CAP Theorem</span>
                    <span class="lang-hi">5. NoSQL डेटाबेस एवं CAP प्रमेय</span>
                </h4>
                <span class="mindmap-node-tag">Not Only SQL • Brewer 2000</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">NoSQL Models &amp; CAP Constraints</span>
                        <span class="lang-hi">NoSQL प्रकार एवं CAP सिद्धांत</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Document Store</strong> (MongoDB, JSON/BSON)</span>
                        <span class="mindmap-chip"><strong>Key-Value Store</strong> (Redis, Fast Cache)</span>
                        <span class="mindmap-chip"><strong>Column-Family</strong> (Cassandra, HBase)</span>
                        <span class="mindmap-chip"><strong>Graph Database</strong> (Neo4j, Nodes &amp; Edges)</span>
                        <span class="mindmap-chip"><strong>CAP Theorem</strong> (Consistency, Availability, Partition)</span>
                        <span class="mindmap-chip"><strong>BASE Properties</strong> (Eventual Consistency)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">NoSQL Paradigms &amp; CAP Proof</span>
                        <span class="lang-hi">NoSQL प्रकार एवं CAP प्रमेय की शर्तें</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Four NoSQL Database Categories:</strong> <strong>1. Document Store:</strong> Stores semi-structured JSON/BSON documents with flexible schema (MongoDB, CouchDB). <strong>2. Key-Value:</strong> Ultra-fast hash table lookups (Redis, DynamoDB). <strong>3. Wide-Column:</strong> Massive write throughput partitioned across rows and dynamic columns (Cassandra, HBase). <strong>4. Graph:</strong> Models interconnected nodes and relationships (Neo4j).</span>
                            <span class="lang-hi"><strong>NoSQL के 4 प्रमुख प्रकार:</strong> <strong>1. डॉक्यूमेंट स्टोर:</strong> JSON/BSON में लचीला डेटा संचयन (MongoDB)। <strong>2. की-वैल्यू:</strong> अति-तीव्र हैश टेबल (Redis)। <strong>3. वाइड-कॉलम:</strong> भारी राइट क्षमता (Cassandra, HBase)। <strong>4. ग्राफ डेटाबेस:</strong> संबंधों और नेटवर्कों का विश्लेषण (Neo4j)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Eric Brewer's CAP Theorem (2000):</strong> Any distributed data store can guarantee at most TWO of three properties simultaneously: <strong>Consistency (C):</strong> Every read receives most recent write. <strong>Availability (A):</strong> Every non-failing node returns response. <strong>Partition Tolerance (P):</strong> System operates despite network dropped messages. Distributed systems must pick <strong>CP</strong> (MongoDB, HBase) or <strong>AP</strong> (Cassandra, CouchDB).</span>
                            <span class="lang-hi"><strong>एरिक ब्रेवर का CAP प्रमेय (2000):</strong> किसी वितरित डेटाबेस में तीन में से केवल दो गुण ही एक साथ संभव हैं: <strong>कंसिस्टेंसी (C):</strong> हर बार नवीनतम डेटा मिलना। <strong>अवेलेबिलिटी (A):</strong> सिस्टम का सदैव उत्तर देना। <strong>पार्टिशन टॉलरेंस (P):</strong> नेटवर्क टूटने पर भी चलते रहना। वितरित प्रणालियां CP या AP चुनती हैं।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> CAP Theorem states a distributed database can only achieve 2 of C, A, and P; MongoDB is a Document-based NoSQL database; Redis is Key-Value!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> CAP प्रमेय के अनुसार वितरित डेटाबेस C, A और P में से केवल 2 चुन सकता है; MongoDB डॉक्यूमेंट-आधारित तथा Redis की-वैल्यू डेटाबेस है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Big Data Governance in India & Uttar Pradesh -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-landmark" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Big Data in India &amp; UP State</span>
                    <span class="lang-hi">6. भारत एवं उत्तर प्रदेश में बिग डेटा गवर्नेंस</span>
                </h4>
                <span class="mindmap-node-tag">Aadhaar • GSTN • UP HMIS</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">National Systems &amp; UP Megaprojects</span>
                        <span class="lang-hi">राष्ट्रीय प्रणालियां एवं उप्र मेगाप्रोजेक्ट्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>UIDAI Aadhaar</strong> (1.4+ Billion Biometrics)</span>
                        <span class="mindmap-chip"><strong>GSTN System</strong> (Billions of Invoices)</span>
                        <span class="mindmap-chip"><strong>UPI Mega-Engine</strong> (10+ Billion Tx/Month)</span>
                        <span class="mindmap-chip"><strong>UP Health MIS</strong> (HMIS District Health)</span>
                        <span class="mindmap-chip"><strong>UP CCTNS</strong> (Police Crime Network)</span>
                        <span class="mindmap-chip"><strong>UP CM Dashboard</strong> (darpan.up.gov.in)</span>
                    </div>
                </div>

                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-circle"></i>
                        <span class="lang-en">Mega-Scale Data Architecture &amp; UP Portals</span>
                        <span class="lang-hi">विशाल डेटा वास्तुकला एवं उप्र पोर्टल प्रभाव</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UIDAI Aadhaar Architecture:</strong> World's largest biometric identity database storing multimodal biometrics (fingerprints, iris, photo) of 1.4+ billion residents; processes millions of daily e-KYC authentications using massive Hadoop and NoSQL distributed clusters.</span>
                            <span class="lang-hi"><strong>UIDAI आधार वास्तुकला:</strong> 1.4 अरब से अधिक नागरिकों के फिंगरप्रिंट व आइरिस बायोमेट्रिक वाला विश्व का सबसे बड़ा डेटाबेस; हडूप व NoSQL क्लस्टर द्वारा दैनिक करोड़ों ई-KYC प्रमाणीकरण।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP CM Dashboard (Darpan Portal):</strong> Real-time big data analytical portal (darpan.up.gov.in) monitoring performance, KPI scores, fund utilization, and flagship public schemes across all 75 districts and 18 divisions of Uttar Pradesh.</span>
                            <span class="lang-hi"><strong>उप्र सीएम डैशबोर्ड (दर्पण पोर्टल):</strong> राज्य के 75 जिलों और 18 मंडलों में सरकारी योजनाओं, फंड उपयोग व विकास कार्यों की रियल-टाइम बिग डेटा मॉनिटरिंग प्रणाली।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP CCTNS Police Network:</strong> Crime and Criminal Tracking Network &amp; Systems integrates 1,500+ police stations across Uttar Pradesh into a centralized big data store for criminal record analytics and instant inter-district lookups.</span>
                            <span class="lang-hi"><strong>उप्र CCTNS पुलिस नेटवर्क:</strong> उत्तर प्रदेश के 1,500 से अधिक थानों को केंद्रीकृत बिग डेटा नेटवर्क से जोड़कर अपराध व अपराधियों के रिकॉर्ड का त्वरित विश्लेषण।</span>
                        </li>
                    </ul>
                </div>

                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UIDAI Aadhaar is the world's largest biometric database powered by Big Data; UP CM Dashboard monitors all 75 districts using real-time KPI data analytics!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> UIDAI आधार बिग डेटा पर संचालित विश्व का सबसे बड़ा बायोमेट्रिक डेटाबेस है; उप्र सीएम डैशबोर्ड राज्य के सभी 75 जिलों की रियल-टाइम मॉनिटरिंग करता है!</span>
                </div>
            </div>
        </div>

    </div>
</div>
'''
