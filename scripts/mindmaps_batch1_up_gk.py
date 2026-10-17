# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 1: Agriculture
# ==============================================================================
mm_agriculture = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Agriculture of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की कृषि एवं संबद्ध क्षेत्र</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • National Rankings &amp; Production • 9 Agro-Climatic Zones • Irrigation Network • Crops &amp; Districts • Research Institutes • Schemes &amp; Reforms</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • राष्ट्रीय रैंकिंग व उत्पादन • 9 कृषि-जलवायु क्षेत्र • सिंचाई तंत्र • प्रमुख फसलें व जिले • अनुसंधान संस्थान • कृषि योजनाएं व सुधार</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-seedling"></i>
            <span class="lang-en">Agrarian Economy &amp; Rural Wealth of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश की कृषि अर्थव्यवस्था एवं ग्रामीण समृद्धि</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: National Rankings & Production -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-trophy" style="color: #059669;"></i>
                    <span class="lang-en">1. National Rankings &amp; Output</span>
                    <span class="lang-hi">1. राष्ट्रीय रैंकिंग एवं प्रमुख उत्पादन</span>
                </h4>
                <span class="mindmap-node-tag">Rank 1 in 8+ Commodities</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-medal"></i>
                        <span class="lang-en">Rank 1 Commodities in India</span>
                        <span class="lang-hi">भारत में प्रथम स्थान वाले उत्पाद</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Total Foodgrains</strong> (कुल खाद्यान्न ~19%)</span>
                        <span class="mindmap-chip"><strong>Wheat</strong> (~32% national share)</span>
                        <span class="mindmap-chip"><strong>Sugarcane</strong> (गन्ना ~45% share)</span>
                        <span class="mindmap-chip"><strong>Potato</strong> (आलू ~35% share)</span>
                        <span class="mindmap-chip"><strong>Milk</strong> (दूध उत्पादन ~15.7%)</span>
                        <span class="mindmap-chip"><strong>Aonla</strong> (आँवला - Pratapgarh)</span>
                        <span class="mindmap-chip"><strong>Guava</strong> (अमरूद - Prayagraj Surkha)</span>
                        <span class="mindmap-chip"><strong>Mentha Oil</strong> (मेंथा ~80% share)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Rank 2 &amp; Rank 3 Categories</span>
                        <span class="lang-hi">द्वितीय एवं तृतीय स्थान वाले उत्पाद</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rank 2 (Rice / Paddy):</strong> Second largest producer after West Bengal. Chandauli is hailed as the <em>'Rice Bowl of UP' (धान का कटोरा)</em>. Siddharthnagar's fragrant <strong>Kalanamak Rice</strong> (Buddha Rice) holds a GI tag.</span>
                            <span class="lang-hi"><strong>द्वितीय स्थान (चावल):</strong> पश्चिम बंगाल के बाद देश में दूसरा सबसे बड़ा उत्पादक। चंदौली को <em>'उप्र का धान का कटोरा'</em> कहा जाता है। सिद्धार्थनगर का सुगंधित <strong>कालानमक चावल</strong> (बुद्ध चावल) जीआई टैग प्राप्त है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rank 2 (Vegetables) &amp; Rank 3 (Pulses):</strong> Second in total vegetables after West Bengal. Third in total pulses; Bundelkhand is the core pulse-producing belt (Gram/Chana).</span>
                            <span class="lang-hi"><strong>सब्जी (द्वितीय) व दलहन (तृतीय):</strong> कुल सब्जी उत्पादन में पश्चिम बंगाल के बाद दूसरा स्थान। कुल दलहन उत्पादन में तीसरा स्थान (बुंदेलखंड चना व अरहर का मुख्य केंद्र)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP produces ~19% of India's foodgrains and ~32% of total wheat! Barabanki is India's largest mentha oil production hub.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र देश के कुल खाद्यान्न का लगभग 19% और कुल गेहूं का 32% उत्पादित करता है! बाराबंकी देश का सबसे बड़ा मेंथा तेल उत्पादक जिला है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: The 9 Agro-Climatic Zones -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-globe-asia" style="color: #0284c7;"></i>
                    <span class="lang-en">2. The 9 Agro-Climatic Zones</span>
                    <span class="lang-hi">2. उत्तर प्रदेश के 9 कृषि-जलवायु क्षेत्र</span>
                </h4>
                <span class="mindmap-node-tag">Planning Commission Matrix</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-map"></i>
                        <span class="lang-en">Zonal Classification &amp; Key Districts</span>
                        <span class="lang-hi">क्षेत्रीय वर्गीकरण एवं प्रमुख जिले</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Tarai Zone:</strong> High rainfall, Sugarcane &amp; Paddy</span>
                        <span class="mindmap-chip"><strong>2. Western Plain:</strong> Meerut, Highest productivity</span>
                        <span class="mindmap-chip"><strong>3. Mid-Western Plain:</strong> Bareilly, Moradabad</span>
                        <span class="mindmap-chip"><strong>4. SW Semi-Arid:</strong> Agra, Mathura, Bajra &amp; Mustard</span>
                        <span class="mindmap-chip"><strong>5. Central Plain:</strong> Kanpur, Lucknow, Alluvial</span>
                        <span class="mindmap-chip"><strong>6. Bundelkhand:</strong> Jhansi, Drought-prone, Pulses</span>
                        <span class="mindmap-chip"><strong>7. North-Eastern:</strong> Gorakhpur, Flood-prone, Rice</span>
                        <span class="mindmap-chip"><strong>8. Eastern Plain:</strong> Varanasi, Ayodhya, Mixed crops</span>
                        <span class="mindmap-chip"><strong>9. Vindhyan Zone:</strong> Mirzapur, Sonbhadra, Plateau</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cloud-sun-rain"></i>
                        <span class="lang-en">Rainfall &amp; Productivity Dynamics</span>
                        <span class="lang-hi">वर्षा एवं उत्पादकता प्रतिमान</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Highest Rainfall:</strong> Gorakhpur in North-Eastern Plain receives the state's highest rainfall (~184.7 cm). Tarai and North-Eastern plains are flood-prone.</span>
                            <span class="lang-hi"><strong>सर्वाधिक वर्षा:</strong> उत्तर-पूर्वी मैदानी क्षेत्र का गोरखपुर जिला राज्य में सर्वाधिक वर्षा (~184.7 सेमी) प्राप्त करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lowest Rainfall &amp; Highest Productivity:</strong> Mathura receives the lowest rainfall (~54.4 cm). Western plain zone exhibits the highest agricultural mechanization and crop yield.</span>
                            <span class="lang-hi"><strong>न्यूनतम वर्षा व उच्चतम उत्पादकता:</strong> मथुरा में सबसे कम वर्षा (~54.4 सेमी) होती है। पश्चिमी मैदान में कृषि उत्पादकता व यंत्रीकरण सर्वाधिक है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Uttar Pradesh is divided into exactly <strong>9 Agro-Climatic Zones</strong> by the Planning Commission (repeated question in UP PCS / UPSSSC)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> योजना आयोग के अनुसार उत्तर प्रदेश को <strong>9 कृषि-जलवायु क्षेत्रों</strong> में विभाजित किया गया है (बार-बार पूछा जाने वाला तथ्य)!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Major Crops & District Hubs -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-wheat-awn" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Major Crops &amp; District Hubs</span>
                    <span class="lang-hi">3. प्रमुख फसलें एवं जिलावार वितरण</span>
                </h4>
                <span class="mindmap-node-tag">Rabi • Kharif • Zaid</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-tractor"></i>
                        <span class="lang-en">Cash Crops &amp; Commercial Agriculture</span>
                        <span class="lang-hi">नगदी फसलें एवं व्यावसायिक कृषि</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sugarcane (गन्ना):</strong> State's foremost commercial cash crop. Core belt: Muzaffarnagar (Sugar bowl), Meerut, Lakhimpur Kheri, Bijnor. Muzaffarnagar is the largest jaggery (Gur) trading market in Asia.</span>
                            <span class="lang-hi"><strong>गन्ना:</strong> राज्य की प्रमुख नकदी फसल। मुख्य बेल्ट: मुजफ्फरनगर (चीनी का कटोरा), मेरठ, लखीमपुर खीरी, बिजनौर। मुजफ्फरनगर एशिया की सबसे बड़ी गुड़ मंडी है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Potato (आलू) &amp; Agra Taj Brand:</strong> Farrukhabad, Agra, Firozabad, Kannauj lead production. UP potatoes exported under the brand name <strong>'Taj' (ताज ब्रांड)</strong>. Central Potato Research Station at Modipuram (Meerut).</span>
                            <span class="lang-hi"><strong>आलू एवं 'ताज' ब्रांड:</strong> फर्रुखाबाद, आगरा, फिरोजाबाद अग्रणी जिले हैं। उप्र के आलू का निर्यात <strong>'ताज' ब्रांड</strong> के नाम से किया जाता है। केंद्रीय आलू अनुसंधान केंद्र मोदीपुरम (मेरठ) में है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Opium (अफीम):</strong> Ghazipur houses the nation's only historic Govt Opium &amp; Alkaloid Works (1820). Barabanki records the highest acreage of legal opium poppy cultivation.</span>
                            <span class="lang-hi"><strong>अफीम:</strong> गाजीपुर में देश की एकमात्र सरकारी अफीम फैक्ट्री (1820) स्थित है। सर्वाधिक अफीम की खेती बाराबंकी जिले में होती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-apple-whole"></i>
                        <span class="lang-en">Horticulture &amp; Fruits Footprint</span>
                        <span class="lang-hi">बागवानी एवं फल उत्पादन</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Mango (Dussehri):</strong> Malihabad (Lucknow)</span>
                        <span class="mindmap-chip"><strong>Mango (Chausa/Langra):</strong> Saharanpur / Varanasi</span>
                        <span class="mindmap-chip"><strong>Mango Export Brand:</strong> 'Nawab' (नवाब ब्रांड)</span>
                        <span class="mindmap-chip"><strong>Aonla Capital:</strong> Pratapgarh (प्रतापगढ़)</span>
                        <span class="mindmap-chip"><strong>Guava (Surkha):</strong> Prayagraj (प्रयागराज सुर्खा)</span>
                        <span class="mindmap-chip"><strong>Betel Leaf (Paan):</strong> Mahoba (महोबा - पान अनुसंधान केंद्र)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP mangoes are exported under <strong>'Nawab'</strong> brand and potatoes under <strong>'Taj'</strong> brand! Mahoba is world-famous for its Deshwari Paan.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र के आम <strong>'नवाब' ब्रांड</strong> और आलू <strong>'ताज' ब्रांड</strong> से निर्यात होते हैं! महोबा देशवारी पान की खेती के लिए प्रसिद्ध है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Irrigation Network & Sources -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-water" style="color: #d97706;"></i>
                    <span class="lang-en">4. Irrigation Network &amp; Sources</span>
                    <span class="lang-hi">4. सिंचाई तंत्र एवं स्रोतवार वितरण</span>
                </h4>
                <span class="mindmap-node-tag">Tubewells: 73.4% • Canals: 15.2%</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-chart-pie"></i>
                        <span class="lang-en">Net Irrigated Area by Sources</span>
                        <span class="lang-hi">सिंचाई के प्रमुख स्रोत एवं हिस्सेदारी</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Tubewells (नलकूप):</strong> ~73.4% (Rank 1 Source)</span>
                        <span class="mindmap-chip"><strong>Canals (नहरें):</strong> ~15.2% (Rank 2 Source)</span>
                        <span class="mindmap-chip"><strong>Wells (कुएँ):</strong> ~8.8% (Rank 3 Source)</span>
                        <span class="mindmap-chip"><strong>Tanks &amp; Lakes (तालाब/झीलें):</strong> ~0.5%</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-route"></i>
                        <span class="lang-en">Major Historic Canals &amp; Projects</span>
                        <span class="lang-hi">प्रमुख ऐतिहासिक नहरें एवं परियोजनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Tubewell:</strong> First tubewell in Uttar Pradesh was bored in <strong>Meerut (1930)</strong>.</span>
                            <span class="lang-hi"><strong>प्रथम नलकूप:</strong> उत्तर प्रदेश में पहला नलकूप <strong>1930 में मेरठ</strong> में लगाया गया था।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Longest Canal Network:</strong> <strong>Sharda Canal (शारदा नहर)</strong> is the longest canal system in UP (total length ~12,368 km with branches; constructed 1928 from Banbasa on Sharda river).</span>
                            <span class="lang-hi"><strong>सर्वाधिक लंबी नहर:</strong> <strong>शारदा नहर</strong> उप्र की सबसे लंबी नहर प्रणाली है (शाखाओं सहित कुल लंबाई ~12,368 किमी; 1928 में निर्मित)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Oldest Canals:</strong> <em>Eastern Yamuna Canal (1830)</em> is the oldest operational canal; <em>Upper Ganga Canal (1854)</em> originated at Haridwar (engineered by Col. Proby Cautley).</span>
                            <span class="lang-hi"><strong>प्राचीनतम नहरें:</strong> <em>पूर्वी यमुना नहर (1830)</em> उप्र की सबसे पुरानी चालू नहर है; <em>ऊपरी गंगा नहर (1854)</em> हरिद्वार से निकलती है (निर्माता पी.बी. कॉटले)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Highest irrigated source is Tubewells (73.4%). Saryu Nahar National Project (inaugurated 2021) links 5 rivers (Ghaghara, Saryu, Rapti, Banganga, Rohini) benefiting 9 districts!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सिंचाई का सबसे बड़ा स्रोत नलकूप (73.4%) है। सरयू नहर राष्ट्रीय परियोजना (2021) 5 नदियों को जोड़कर 9 पूर्वी जिलों को सिंचित करती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Institutes & SAUs -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-university" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Institutes &amp; SAUs</span>
                    <span class="lang-hi">5. राष्ट्रीय अनुसंधान संस्थान एवं कृषि वि.वि.</span>
                </h4>
                <span class="mindmap-node-tag">ICAR Institutes • 4 SAUs + 1 CAU</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-flask"></i>
                        <span class="lang-en">Premier Central Research Institutes (ICAR)</span>
                        <span class="lang-hi">प्रमुख केंद्रीय अनुसंधान संस्थान (ICAR)</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>IISR:</strong> Indian Inst. of Sugarcane Research (Lucknow)</span>
                        <span class="mindmap-chip"><strong>CISH:</strong> Subtropical Horticulture (Rahman Khera, Lko)</span>
                        <span class="mindmap-chip"><strong>IIVR:</strong> Indian Inst. of Vegetable Research (Varanasi)</span>
                        <span class="mindmap-chip"><strong>IIPR:</strong> Indian Inst. of Pulses Research (Kalyanpur, Kanpur)</span>
                        <span class="mindmap-chip"><strong>IVRI:</strong> Indian Veterinary Research Inst. (Izzatnagar, Bareilly)</span>
                        <span class="mindmap-chip"><strong>CARI:</strong> Central Avian Research Inst. (Izzatnagar, Bareilly)</span>
                        <span class="mindmap-chip"><strong>CIRG:</strong> Research on Goats (Makhdoom, Mathura)</span>
                        <span class="mindmap-chip"><strong>IGFRI:</strong> Grassland &amp; Fodder Research (Jhansi)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-graduation-cap"></i>
                        <span class="lang-en">State &amp; Central Agricultural Universities</span>
                        <span class="lang-hi">राज्य एवं केंद्रीय कृषि विश्वविद्यालय</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>4 State Agricultural Universities (SAUs):</strong> 1. CSA Univ of Agriculture &amp; Tech (Kanpur); 2. Acharya Narendra Deva Univ (Kumarganj, Ayodhya); 3. Sardar Vallabhbhai Patel Univ (Modipuram, Meerut); 4. Banda Univ of Agriculture &amp; Tech (Banda).</span>
                            <span class="lang-hi"><strong>4 राज्य कृषि विश्वविद्यालय:</strong> 1. चंद्रशेखर आजाद कृषि वि.वि. (कानपुर); 2. आचार्य नरेंद्र देव कृषि वि.वि. (कुमारगंज, अयोध्या); 3. सरदार वल्लभभाई पटेल कृषि वि.वि. (मोदीपुरम, मेरठ); 4. बांदा कृषि एवं प्रौद्योगिकी वि.वि. (बांदा)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Central &amp; Deemed Agri Universities:</strong> <em>Rani Lakshmi Bai Central Agricultural University (RLBCAU)</em> at Jhansi (Central Univ); <em>SHUATS (Sam Higginbottom Univ)</em> at Naini, Prayagraj (founded 1910 - India's earliest agricultural institute).</span>
                            <span class="lang-hi"><strong>केंद्रीय व मानित कृषि वि.वि.:</strong> <em>रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय</em> (झांसी); <em>शुआट्स (SHUATS)</em> नैनी, प्रयागराज (1910 में स्थापित - देश का प्रथम कृषि संस्थान)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> IIVR is in Varanasi, IIPR in Kanpur, IISR &amp; CISH in Lucknow, and IVRI in Bareilly. These match-the-column questions appear in every UP exam!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सब्जी अनुसंधान (IIVR) वाराणसी में, दलहन (IIPR) कानपुर में, गन्ना (IISR) लखनऊ में, और पशु चिकित्सा (IVRI) बरेली में है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Reforms, Dairy & Schemes -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hand-holding-dollar" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Reforms, Dairy &amp; Schemes</span>
                    <span class="lang-hi">6. भूमि सुधार, दुग्ध विकास एवं किसान योजनाएं</span>
                </h4>
                <span class="mindmap-node-tag">Chakbandi 1954 • PM-KISAN 2019</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-file-contract"></i>
                        <span class="lang-en">Land Reforms &amp; Peasant Welfare Milestones</span>
                        <span class="lang-hi">भूमि सुधार एवं किसान कल्याण के मील के पत्थर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Zamindari Abolition Act 1950:</strong> UP Zamindari Abolition &amp; Land Reforms Act 1950 came into force on <strong>1 July 1952</strong>.</span>
                            <span class="lang-hi"><strong>जमींदारी उन्मूलन अधिनियम:</strong> उप्र जमींदारी विनाश एवं भूमि व्यवस्था अधिनियम 1950, <strong>1 जुलाई 1952</strong> से प्रभावी हुआ।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chakbandi Scheme (1954):</strong> Consolidation of land holdings launched in <strong>1954</strong> as a pilot in Kairana (Muzaffarnagar) and Musafirkhana (Sultanpur); made statewide in 1958.</span>
                            <span class="lang-hi"><strong>चकबंदी योजना (1954):</strong> 1954 में कैराना (मुजफ्फरनगर) व मुसाफिरखाना (सुल्तानपुर) तहसील से शुरू; 1958 से पूरे प्रदेश में लागू।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kisan Bahi &amp; KCC:</strong> <em>Kisan Bahi Scheme</em> launched in <strong>1992</strong>; <em>Kisan Credit Card (KCC)</em> introduced in <strong>1998-99</strong>; <em>Kisan Mitra</em> started on 18 June 2001.</span>
                            <span class="lang-hi"><strong>किसान बही व KCC:</strong> <em>किसान बही योजना</em> <strong>1992</strong> में; <em>किसान क्रेडिट कार्ड (KCC)</em> <strong>1998-99</strong> में; <em>किसान मित्र योजना</em> 18 जून 2001 से लागू हुई।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cow"></i>
                        <span class="lang-en">Dairy Development &amp; National Launches</span>
                        <span class="lang-hi">श्वेत क्रांति, दुग्ध विकास व राष्ट्रीय योजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>First Milk Union:</strong> Lucknow (1938)</span>
                        <span class="mindmap-chip"><strong>PCDF / Parag Brand:</strong> Established 1962</span>
                        <span class="mindmap-chip"><strong>Nand Baba Milk Mission:</strong> ₹1000 Cr outlay</span>
                        <span class="mindmap-chip"><strong>Gokul &amp; Nandbaba Awards:</strong> Top indigenous dairy producers</span>
                        <span class="mindmap-chip"><strong>PM-KISAN Launch:</strong> 24 Feb 2019 (Gorakhpur by PM Modi)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> PM-KISAN (₹6000/yr) was nationally inaugurated from Gorakhpur on 24 Feb 2019. Chakbandi started in 1954 and Kisan Bahi in 1992!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> पीएम-किसान योजना का देशव्यापी शुभारंभ 24 फरवरी 2019 को गोरखपुर से हुआ था। चकबंदी 1954 तथा किसान बही 1992 में शुरू हुई!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 2: Architecture
# ==============================================================================
mm_architecture = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Architecture of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की स्थापत्य कला एवं स्मारक</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Ancient Stupas &amp; Buddhist Viharas • Gupta Shikhara &amp; Brick Temples • Jaunpur Sharqi Style • Mughal Splendors (Agra &amp; Fatehpur Sikri) • Awadh Nawabi Architecture • Bundelkhand Hill Forts</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • प्राचीन बौद्ध स्तूप व विहार • गुप्तकालीन शिखर व ईंट मंदिर • जौनपुर शर्की शैली • मुग़ल स्थापत्य (आगरा व फतेहपुर सीकरी) • अवध की नवाबी वास्तुकला • बुंदेलखंड के गिरि दुर्ग</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-monument"></i>
            <span class="lang-en">Architectural Heritage of Uttar Pradesh (Ancient to Nawabi Era)</span>
            <span class="lang-hi">उत्तर प्रदेश की स्थापत्य धरोहर (प्राचीन काल से नवाबी युग तक)</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Ancient Buddhist Stupas & Viharas -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-dharmachakra" style="color: #059669;"></i>
                    <span class="lang-en">1. Ancient Stupas &amp; Buddhist Viharas</span>
                    <span class="lang-hi">1. प्राचीन बौद्ध स्तूप एवं संघाराम</span>
                </h4>
                <span class="mindmap-node-tag">Mauryan to Gupta Era</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-place-of-worship"></i>
                        <span class="lang-en">Iconic Stupas &amp; Relic Sites</span>
                        <span class="lang-hi">प्रमुख स्तूप एवं पवित्र अस्थि धातु स्थल</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Dhamekh Stupa:</strong> Sarnath (Dharmachakra Pravartana)</span>
                        <span class="mindmap-chip"><strong>Chaukhandi Stupa:</strong> Sarnath (Octagonal Humayun tower)</span>
                        <span class="mindmap-chip"><strong>Ramabhar Stupa:</strong> Kushinagar (Mukutbandhana Chaitya)</span>
                        <span class="mindmap-chip"><strong>Piprahwa Stupa:</strong> Siddharthnagar (Kapilavastu relics)</span>
                        <span class="mindmap-chip"><strong>Ghoshitarama Vihara:</strong> Kaushambi (Yamuna bank)</span>
                        <span class="mindmap-chip"><strong>Jetavana Monastery:</strong> Shravasti (Anathapindika donation)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Architectural Highlights</span>
                        <span class="lang-hi">स्थापत्य विशेषताएं एवं साक्ष्य</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dhamekh Stupa (Sarnath):</strong> Massive cylindrical brick &amp; stone stupa built during Gupta era replacing Ashokan structure; exhibits delicate geometric &amp; floral carvings with swastika patterns.</span>
                            <span class="lang-hi"><strong>धमेख स्तूप (सारनाथ):</strong> गुप्तकालीन विशाल बेलनाकार ईंट-पत्थर स्तूप; अशोक के मूल स्तूप पर निर्मित; स्वास्तिक, ज्यामितीय व पुष्प आकृतियों की बारीक नक्काशी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Piprahwa &amp; Ramabhar:</strong> Piprahwa casket bore the earliest Mauryan Brahmi inscription confirming Buddha's corporeal relics; Ramabhar marks the holy cremation ground of Buddha.</span>
                            <span class="lang-hi"><strong>पिपरहवा व रामाभार:</strong> पिपरहवा मंजूषा पर सबसे प्राचीन ब्राह्मी लेख मिला जो बुद्ध की अस्थियों की पुष्टि करता है; रामाभार स्तूप बुद्ध का पावन अंत्येष्टि स्थल है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Chaukhandi Stupa at Sarnath has an octagonal brick tower erected by Govardhan (son of Todar Mal) to commemorate Humayun's visit in 1588!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सारनाथ के चौखंडी स्तूप पर अष्टकोणीय बुर्ज हुमायूँ के आगमन की स्मृति में 1588 में गोवर्धन (टोडरमल के पुत्र) ने बनवाया था!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Classical Gupta Temples & Terracotta -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gopuram" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Gupta Temples &amp; Terracotta</span>
                    <span class="lang-hi">2. गुप्तकालीन शिखर मंदिर एवं टेराकोटा</span>
                </h4>
                <span class="mindmap-node-tag">5th–6th Century CE</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-landmark"></i>
                        <span class="lang-en">Architectural Milestones of North India</span>
                        <span class="lang-hi">उत्तर भारतीय मंदिर स्थापत्य के मील के पत्थर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dashavatara Temple (Deogarh, Lalitpur):</strong> North India's earliest surviving Panchayatana stone temple (~500 CE). First appearance of a curvilinear Shikhara (tower); world-famous high-relief panels: <em>Sheshashayi Vishnu</em>, <em>Gajendra Moksha</em>, and <em>Nara-Narayana</em>.</span>
                            <span class="lang-hi"><strong>दशावतार मंदिर (देवगढ़, ललितपुर):</strong> उत्तर भारत का प्राचीनतम सुरक्षित पंचायतन शैली का पत्थर मंदिर (~500 ई.)। शिखर का प्रथम प्रयोग; <em>शेषशायी विष्णु</em>, <em>गजेंद्र मोक्ष</em> व <em>नर-नारायण</em> के विश्वप्रसिद्ध शिल्प फलक।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bhitargaon Temple (Kanpur):</strong> India's earliest surviving complete all-brick Hindu temple (5th century CE). Features a stepped curvilinear shikhara, semicircular <strong>true arch</strong>, and exquisite terracotta panels depicting Shiva-Parvati and Ganas.</span>
                            <span class="lang-hi"><strong>भीतरगांव मंदिर (कानपुर):</strong> भारत का प्राचीनतम सुरक्षित संपूर्ण ईंट-निर्मित हिंदू मंदिर (5वीं सदी)। सोपानी शिखर, अर्धवृत्ताकार <strong>यथार्थ मेहराब</strong> तथा शिव-पार्वती व गणों के सुंदर टेराकोटा फलक।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bhitari Pillar &amp; Temple (Ghazipur):</strong> Monolithic sandstone pillar with Skandagupta's inscription recording triumph over Hunas; brick temple ruins of Vishnu.</span>
                            <span class="lang-hi"><strong>भीतरी स्तंभ व मंदिर (गाजीपुर):</strong> स्कंदगुप्त का एकाश्म बलुआ पत्थर स्तंभ लेख (हूणों पर विजय); भगवान विष्णु के प्राचीन ईंट मंदिर के अवशेष।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Deogarh (stone Panchayatana with Shikhara) &amp; Bhitargaon (brick with true arch) are the two foundational monuments of Hindu temple architecture!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> देवगढ़ (शिखर युक्त पंचायतन प्रस्तर मंदिर) और भीतरगांव (मेहराब युक्त ईंट मंदिर) हिंदू मंदिर स्थापत्य के दो आधार स्तंभ हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Jaunpur Sharqi Sultanate Style -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-archway" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Jaunpur Sharqi Architecture</span>
                    <span class="lang-hi">3. जौनपुर की शर्की स्थापत्य शैली</span>
                </h4>
                <span class="mindmap-node-tag">1394–1479 CE • Shiraz-e-Hind</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-mosque"></i>
                        <span class="lang-en">Distinctive Style: Propylon Gateway &amp; No Minarets</span>
                        <span class="lang-hi">विशिष्ट शैली: विशाल तोरण द्वार एवं मीनारविहीन रूप</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Atala Masjid (Jaunpur, 1408):</strong> Masterpiece of Sharqi architecture commissioned by Sultan Ibrahim Shah Sharqi. Unique characteristics: Massive sloping pylons (propylon screen) hiding the dome; completely devoid of traditional minarets; exquisite stone lattice screens.</span>
                            <span class="lang-hi"><strong>अटाला मस्जिद (1408):</strong> सुल्तान इब्राहिम शाह शर्की द्वारा निर्मित शर्की स्थापत्य का मुकुटमणि। मुख्य विशेषता: गुंबद को ढकने वाला विशाल ढलवां तोरण (प्रोपाइलॉन); पारंपरिक मीनारों का पूर्ण अभाव; बारीक पत्थर की जालियां।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jhanjhari, Lal Darwaza &amp; Jama Masjid:</strong> <em>Jhanjhari Masjid (1430)</em> famous for screen work; <em>Lal Darwaza (1450)</em> built by Queen Bibi Raji; <em>Jama Masjid Jaunpur (1478)</em> built by Husain Shah Sharqi on a 20-ft high plinth.</span>
                            <span class="lang-hi"><strong>झंझरी, लाल दरवाजा व जामा मस्जिद:</strong> <em>झंझरी मस्जिद (1430)</em> बारीक नक्काशी हेतु प्रसिद्ध; <em>लाल दरवाजा (1450)</em> रानी बीबी राजी द्वारा निर्मित; <em>जामा मस्जिद जौनपुर (1478)</em> हुसैन शाह द्वारा 20 फीट ऊंचे चबूतरे पर निर्मित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Shahi Bridge (Akbari Pul, Jaunpur):</strong> Built across Gomti River in <strong>1568</strong> by Mughal governor Munim Khan; designed by Afghan architect Afzal Ali; features 16 stone arches and roofed kiosks (gumtis).</span>
                            <span class="lang-hi"><strong>शाही पुल (अकबरी पुल, जौनपुर):</strong> गोमती नदी पर <strong>1568</strong> में मुनीम खां द्वारा निर्मित; वास्तुकार अफजल अली; 16 मेहराबों व सुंदर छतरियों से सुसज्जित।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Atala Masjid has no minarets and uses a massive central pylon (propylon). Jaunpur was hailed as <em>'Shiraz-e-Hind'</em> during the Sharqi reign!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> अटाला मस्जिद मीनारविहीन है और इसमें विशाल तोरण द्वार है। शर्की काल में जौनपुर को <em>'शीराज़-ए-हिन्द'</em> कहा गया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Mughal Architecture Peak (Agra & Fatehpur Sikri) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-crown" style="color: #d97706;"></i>
                    <span class="lang-en">4. Mughal Architectural Splendors</span>
                    <span class="lang-hi">4. मुग़ल स्थापत्य कला के शिखर</span>
                </h4>
                <span class="mindmap-node-tag">Agra &amp; Fatehpur Sikri • UNESCO</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-gem"></i>
                        <span class="lang-en">Red Sandstone to White Marble &amp; Pietra Dura</span>
                        <span class="lang-hi">लाल बलुआ पत्थर से श्वेत संगमरमर व पच्चीकारी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Agra Fort (1565–1573, Akbar):</strong> Built with red sandstone on Yamuna bank. Contains Jahangiri Mahal (Akbar's Hindu-Islamic synthesis), Diwan-i-Aam, Diwan-i-Khas, Moti Masjid (white marble by Shah Jahan), and Musamman Burj. UNESCO World Heritage 1983.</span>
                            <span class="lang-hi"><strong>आगरा किला (1565):</strong> लाल बलुआ पत्थर से निर्मित। जहांगीरी महल (हिंदू-इस्लामी समन्वय), मोती मस्जिद (शाहजहाँ द्वारा संगमरमर से निर्मित), तथा मुसम्मन बुर्ज (जहाँ शाहजहाँ को बंदी रखा गया)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Fatehpur Sikri (1571, Akbar):</strong> <em>Buland Darwaza</em> (53.5 m high gateway commemorating Gujarat victory 1572/1601); <em>Tomb of Salim Chishti</em> (pure white marble, jali screens); <em>Panch Mahal</em> (5-tier columnar pyramid based on Buddhist vihara); <em>Ibadat Khana</em> (1575); <em>Birbal Bhawan</em>. UNESCO 1986.</span>
                            <span class="lang-hi"><strong>फतेहपुर सीकरी (1571):</strong> <em>बुलंद दरवाजा</em> (53.5 मी. ऊँचा, गुजरात विजय की स्मृति में); <em>शेख सलीम चिश्ती की दरगाह</em> (श्वेत संगमरमर व जालीदार नक्काशी); <em>पंचमहल</em> (बौद्ध विहार शैली पर आधारित 5 मंजिला स्तंभ महल); <em>इबादतखाना</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tomb of Itimad-ud-Daulah (Agra, 1622–1628):</strong> Built by Empress Nur Jahan for her father Mirza Ghiyas Beg. First complete building in India constructed entirely of white marble; pioneered <strong>Pietra Dura (Parchin Kari)</strong> floral stone inlay; hailed as the <em>'Baby Taj'</em>.</span>
                            <span class="lang-hi"><strong>एतमादुद्दौला का मकबरा (1622-28):</strong> नूरजहाँ द्वारा पिता मिर्जा गयास बेग हेतु निर्मित। भारत की पहली इमारत जो पूर्णतः श्वेत संगमरमर से बनी; इसमें पहली बार <strong>पित्रा ड्यूरा (पच्चीकारी)</strong> का प्रयोग हुआ; इसे <em>'बेबी ताज'</em> कहा जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Taj Mahal (Agra, 1631–1648):</strong> Built by Shah Jahan for Mumtaz Mahal. Chief architect: <strong>Ustad Ahmad Lahori</strong>; Calligrapher: Amanat Khan Shirazi. Features Makrana marble, bulbous dome, Charbagh garden, and optical symmetry. UNESCO 1983.</span>
                            <span class="lang-hi"><strong>ताजमहल (1631-1648):</strong> शाहजहाँ द्वारा मुमताज महल की स्मृति में निर्मित। मुख्य वास्तुकार: <strong>उस्ताद अहमद लाहौरी</strong>; कैलीग्राफर: अमानत खां शीराजी। मकराना संगमरमर, चारबाग शैली व समरूपता का प्रतीक।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Pietra Dura was first used in Itimad-ud-Daulah's tomb (Nur Jahan). Taj Mahal architect was Ustad Ahmad Lahori. Buland Darwaza is the world's highest gateway (53.5m)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> पित्रा ड्यूरा का पहला प्रयोग एतमादुद्दौला के मकबरे में हुआ। ताजमहल के वास्तुकार उस्ताद अहमद लाहौरी थे। बुलंद दरवाजा विश्व का सबसे ऊंचा प्रवेश द्वार है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Awadh Nawabi Architecture (Lucknow Style) -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-building-columns" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Awadh Nawabi Architecture</span>
                    <span class="lang-hi">5. अवध की नवाबी स्थापत्य कला (लखनऊ)</span>
                </h4>
                <span class="mindmap-node-tag">Brick &amp; Stucco • Lakhori Bricks</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-city"></i>
                        <span class="lang-en">Imambaras, Gateways &amp; Palaces</span>
                        <span class="lang-hi">इमामबाड़े, तोरण द्वार एवं महल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bara Imambara (Asafi Imambara, 1784):</strong> Built by Nawab Asaf-ud-Daula as a famine relief project; designed by architect <strong>Kifayatullah</strong>. The central vaulted hall (50m x 16m x 15m) is one of the world's largest unsupported vaults (built of Lakhori brick &amp; lime mortar without wood, iron or pillars). Houses the intricate <strong>Bhulbhulaiya</strong> (labyrinth) on upper floors.</span>
                            <span class="lang-hi"><strong>बड़ा इमामबाड़ा (आसफी इमामबाड़ा, 1784):</strong> नवाब आसफउद्दौला द्वारा अकाल राहत कार्य के रूप में निर्मित; वास्तुकार <strong>किफायतउल्लाह</strong>। केंद्रीय मेहराबदार हॉल (50 मी. लंबा) बिना किसी खंभे या गर्डर के टिका है (लखौरी ईंट व चूने से निर्मित)। ऊपरी तल पर प्रसिद्ध <strong>भूलभुलैया</strong> स्थित है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rumi Darwaza (Turkish Gate, 1784):</strong> 60-ft high monumental gate built adjacent to Bara Imambara. Modeled on the <em>Sublime Porte</em> of Constantinople (Istanbul); decorated with fish motifs (emblem of Awadh).</span>
                            <span class="lang-hi"><strong>रूमी दरवाजा (1784):</strong> 60 फीट ऊंचा विशाल द्वार; बड़ा इमामबाड़ा के सामने स्थित। यह कांस्टेंटिनोपल (इस्तांबुल) के 'बाब-ए-हुमायूँ' की तर्ज पर निर्मित है; अवध के राजचिह्न मछली से अलंकृत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chhota Imambara, Residency &amp; Chattar Manzil:</strong> <em>Chhota Imambara (1838, Muhammad Ali Shah)</em> famous for golden dome, calligraphic texts &amp; chandeliers; <em>British Residency</em> (focal point of 1857 siege); <em>Chattar Manzil</em> &amp; <em>Dilkusha Kothi</em> (Indo-European hybrid).</span>
                            <span class="lang-hi"><strong>छोटा इमामबाड़ा, रेजीडेंसी व छतर मंजिल:</strong> <em>छोटा इमामबाड़ा (1838)</em> सुनहरे गुंबद व झूमरों हेतु प्रसिद्ध; <em>ब्रिटिश रेजीडेंसी</em> 1857 की क्रांति का प्रमुख केंद्र; <em>छतर मंजिल</em> इंडो-यूरोपीय शैली का सुंदर उदाहरण।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bara Imambara's central hall is built completely without pillars or iron beams using Lakhori bricks. Rumi Darwaza is 60 feet high and modeled on Constantinople's gateway!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बड़ा इमामबाड़ा बिना किसी खंभे के लखौरी ईंटों से बना है। रूमी दरवाजा 60 फीट ऊंचा है तथा इस्तांबुल के प्रवेश द्वार की तर्ज पर बना है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Bundelkhand Forts & Ancient Hill Fortresses -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-chess-rook" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Bundelkhand Fortresses</span>
                    <span class="lang-hi">6. बुंदेलखंड के गिरि दुर्ग एवं प्राचीन किले</span>
                </h4>
                <span class="mindmap-node-tag">Kalinjar • Jhansi • Chunar • Ramnagar</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield-halved"></i>
                        <span class="lang-en">Strategic Fortresses &amp; Historical Battles</span>
                        <span class="lang-hi">सामरिक दुर्ग एवं ऐतिहासिक संघर्ष</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kalinjar Fort (Banda):</strong> Legendary hill fort on Vindhyan range built by Chandela rulers. Houses the historic rock-cut <strong>Nilkanth Mahadev Temple</strong> with eighteen-armed Shiva sculpture and Mrigdhara. Afghan ruler <strong>Sher Shah Suri died here in 1545</strong> when a gunpowder blast rebounded during his siege.</span>
                            <span class="lang-hi"><strong>कालिंजर दुर्ग (बांदा):</strong> चंदेल शासकों द्वारा विंध्य पर्वत पर निर्मित अजेय दुर्ग। इसमें शैलकृत <strong>नीलकंठ महादेव मंदिर</strong> व अष्टदशभुजी शिव प्रतिमा स्थित है। <strong>1545 में शेरशाह सूरी की मृत्यु</strong> इसी दुर्ग के घेरे में उक्का तोप का गोला फटने से हुई थी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jhansi Fort (1613):</strong> Built by Orchha King <strong>Bir Singh Deo</strong> on Bangira hill. Key sites: Panch Mahal, Shiva temple, Kadak Bijli cannon, and the legendary rampart from which Rani Lakshmibai leaped on horseback in 1858.</span>
                            <span class="lang-hi"><strong>झांसी का किला (1613):</strong> ओरछा के राजा <strong>वीर सिंह देव</strong> द्वारा बंगिरा पहाड़ी पर निर्मित। प्रमुख स्थल: कड़क बिजली तोप, पंचमहल, तथा वह परकोटा जहाँ से रानी लक्ष्मीबाई ने घोड़े सहित छलांग लगाई थी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chunar Fort &amp; Ramnagar Fort:</strong> <em>Chunar Fort (Mirzapur)</em> on Ganga cliff, associated with King Vikramaditya, Babur, Sher Shah and Warren Hastings; <em>Ramnagar Fort (Varanasi)</em> built 18th century by Kashi Naresh Balwant Singh on eastern bank of Ganga (famous for 200-year-old Ramlila).</span>
                            <span class="lang-hi"><strong>चुनार व रामनगर किला:</strong> <em>चुनार दुर्ग (मिर्जापुर)</em> गंगा तट पर स्थित; विक्रमादित्य, शेरशाह व वारेन हेस्टिंग्स से संबंधित; <em>रामनगर किला (वाराणसी)</em> काशी नरेश बलवंत सिंह द्वारा निर्मित (प्रसिद्ध 200 वर्षीय रामलीला स्थल)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sher Shah Suri died during the siege of Kalinjar Fort (Banda) in 1545. Jhansi Fort was founded by Bir Singh Deo in 1613!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> शेरशाह सूरी की मृत्यु 1545 में कालिंजर दुर्ग (बांदा) के घेरे में हुई थी। झांसी किले का निर्माण 1613 में वीर सिंह देव ने कराया था!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 3: Art (Painting, Music, Handicrafts & Gharanas)
# ==============================================================================
mm_art = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Art &amp; Culture of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की कला, संगीत एवं हस्तशिल्प</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Prehistoric to Mughal Painting • Traditional Handicrafts &amp; GI Tags • Classical Kathak Heritage • Banaras &amp; Lucknow Musical Gharanas • Kirana &amp; Agra Vocal Styles • Folk Theatres (Nautanki &amp; Ramlila)</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • प्रागैतिहासिक से मुग़ल चित्रकला • पारंपरिक हस्तशिल्प व जीआई टैग • शास्त्रीय कत्थक परंपरा • बनारस व लखनऊ संगीत घराने • किराना व आगरा गायन शैलियां • लोक नाट्य (नौटंकी व रामलीला)</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-palette"></i>
            <span class="lang-en">Artistic, Musical &amp; Craft Traditions of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश की चित्रकला, शास्त्रीय संगीत एवं शिल्प परंपरा</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Painting Traditions: Prehistoric to Modern -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-paint-brush" style="color: #059669;"></i>
                    <span class="lang-en">1. Painting Traditions &amp; Rock Art</span>
                    <span class="lang-hi">1. चित्रकला परंपरा एवं शैलचित्र</span>
                </h4>
                <span class="mindmap-node-tag">Mirzapur Caves • Mughal Court</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-mountain"></i>
                        <span class="lang-en">Prehistoric Rock Art in Vindhyas</span>
                        <span class="lang-hi">विंध्य क्षेत्र के प्रागैतिहासिक शैलचित्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mirzapur &amp; Sonbhadra Rock Shelters:</strong> Lakhaniya Dari, Vijaygarh, Kohbar, and Kandakot feature Upper Paleolithic and Mesolithic rock paintings drawn in red ochre (Geru); depict hunting scenes, animal figures, and group dances.</span>
                            <span class="lang-hi"><strong>मिर्जापुर व सोनभद्र की गुफाएं:</strong> लखनिया दरी, विजयगढ़, कोहबर व कंडाकोट में गेरू रंग से चित्रित शिकार, पशु व सामूहिक नृत्य के प्राचीन शैलचित्र।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crown"></i>
                        <span class="lang-en">Mughal &amp; Awadh Court Painting</span>
                        <span class="lang-hi">मुग़ल एवं अवध दरबारी चित्रकला</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mughal Atelier (Akbar &amp; Jahangir):</strong> Akbar founded imperial karkhana (Hamzanama, Tutinama); master artists Mir Sayyid Ali, Abdus Samad, Daswanth, Basawan. Jahangir's reign was the golden era (portraiture &amp; nature): <strong>Ustad Mansur</strong> (animal/bird specialist, painted Siberian Crane &amp; Dodo), Bishandas, Abul Hasan.</span>
                            <span class="lang-hi"><strong>मुग़ल कारखाना:</strong> अकबर कालीन हम्ज़ानामा; मीर सैयद अली, दसवंत व बसावन। जहांगीर का काल स्वर्ण युग: <strong>उस्ताद मंसूर</strong> (प्रकृति व पक्षी विशेषज्ञ, साइबेरियन सारस चित्र), बिशनदास व अबुल हसन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Modern Era (Lucknow Art College):</strong> <strong>Asit Kumar Haldar</strong> appointed first Indian Principal of Govt College of Arts &amp; Crafts, Lucknow (1925); pioneered the Indian wash technique in UP.</span>
                            <span class="lang-hi"><strong>आधुनिक काल (लखनऊ कला महाविद्यालय):</strong> <strong>असित कुमार हलदार</strong> 1925 में लखनऊ कला महाविद्यालय के प्रथम भारतीय प्राचार्य बने; उप्र में 'वॉश तकनीक' के प्रवर्तक।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ustad Mansur was Jahangir's court specialist for birds/animals. Asit Kumar Haldar was the first Indian principal of Lucknow Arts College in 1925!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उस्ताद मंसूर जहांगीर के दरबारी पक्षी चित्रकार थे। असित कुमार हलदार 1925 में लखनऊ कला महाविद्यालय के पहले भारतीय प्राचार्य बने!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Traditional Handicrafts & GI Tags -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-scissors" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Handicrafts &amp; GI Tags</span>
                    <span class="lang-hi">2. पारंपरिक हस्तशिल्प एवं जीआई टैग</span>
                </h4>
                <span class="mindmap-node-tag">ODOP Hubs • 45+ GI Tags</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-tags"></i>
                        <span class="lang-en">Geographical Indication (GI) Products of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के प्रमुख जीआई उत्पाद</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Chikankari:</strong> Lucknow (32 hand stitches)</span>
                        <span class="mindmap-chip"><strong>Zardozi:</strong> Lucknow, Bareilly, Varanasi</span>
                        <span class="mindmap-chip"><strong>Banarasi Brocade &amp; Sarees:</strong> Varanasi (Kinkhab)</span>
                        <span class="mindmap-chip"><strong>Brassware:</strong> Moradabad ('Peetal Nagari')</span>
                        <span class="mindmap-chip"><strong>Wood Carving:</strong> Saharanpur (Sheesham wood)</span>
                        <span class="mindmap-chip"><strong>Black Pottery:</strong> Nizamabad (Azamgarh)</span>
                        <span class="mindmap-chip"><strong>Terracotta:</strong> Gorakhpur (clay horses &amp; bells)</span>
                        <span class="mindmap-chip"><strong>Glassware / Bangles:</strong> Firozabad ('Suhag Nagari')</span>
                        <span class="mindmap-chip"><strong>Handmade Carpets:</strong> Bhadohi ('Carpet City') &amp; Mirzapur</span>
                        <span class="mindmap-chip"><strong>Attar / Perfume:</strong> Kannauj (Deg-Bhapka distillation)</span>
                        <span class="mindmap-chip"><strong>Leathercraft:</strong> Kanpur &amp; Agra</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hand-sparkles"></i>
                        <span class="lang-en">Techniques &amp; Cultural Roots</span>
                        <span class="lang-hi">शिल्प तकनीक एवं सांस्कृतिक संदर्भ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chikankari (Lucknow):</strong> Delicate shadow white-on-white needle embroidery popularized by Empress Nur Jahan; involves 32 stitches including <em>Bakhiya</em>, <em>Phanda</em>, <em>Tepchi</em>, <em>Murri</em>, and <em>Jaali</em>.</span>
                            <span class="lang-hi"><strong>चिकनकारी (लखनऊ):</strong> नूरजहाँ द्वारा संपोषित सफेद धागे की महीन कशीदाकारी; इसमें 32 प्रकार के टांके (बखिया, फंदा, तेपची, मुर्री, जाली) प्रयुक्त होते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nizamabad Black Pottery:</strong> Earthenware fired in enclosed smoke kilns using mustard oil wash, followed by rubbing zinc-mercury/lead silver-colored powder into engraved patterns.</span>
                            <span class="lang-hi"><strong>निजामाबाद की काली मिट्टी के बर्तन (आजमगढ़):</strong> धुएं में पकाए गए काले बर्तनों पर जस्ते व पारे के लेप से चांदी जैसी चमकीली नक्काशी की जाती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP ranks among India's top states with 45+ GI Tags! Moradabad is Peetal Nagari, Firozabad is Suhag Nagari, and Bhadohi is Carpet City.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र 45+ जीआई टैग्स के साथ देश में अग्रणी है! मुरादाबाद पीतल नगरी, फिरोजाबाद सुहाग नगरी, और भदोही कालीन नगरी के रूप में प्रसिद्ध हैं।</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Classical Kathak & Lucknow Gharana -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-person-walking"></i>
                    <span class="lang-en">3. Classical Kathak Heritage</span>
                    <span class="lang-hi">3. शास्त्रीय कत्थक एवं लखनऊ घराना</span>
                </h4>
                <span class="mindmap-node-tag">Only Classical Dance of North India</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-drum"></i>
                        <span class="lang-en">Evolution &amp; Royal Patronage</span>
                        <span class="lang-hi">विकास क्रम एवं शाही संरक्षण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Roots &amp; Wajid Ali Shah:</strong> Originated from temple storytellers (<em>'Katha kahe so Kathak kahave'</em>). Reached artistic zenith under <strong>Nawab Wajid Ali Shah ('Akhtarpiya')</strong> of Awadh, who staged the first Rahas (dance-drama) as Lord Krishna at Parikhana.</span>
                            <span class="lang-hi"><strong>उत्पत्ति व वाजिद अली शाह:</strong> मंदिर कथाकारों से उत्पत्ति (<em>'कथा कहे सो कथक कहावे'</em>)। अवध के अंतिम नवाब <strong>वाजिद अली शाह ('अख्तरपिया')</strong> के दरबार में स्वर्ण काल; उन्होंने परीखाना में 'रहस' नृत्य नाटिका रची।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow Kathak Gharana Stalwarts:</strong> Founded by Ishwari Prasad. Great masters: Thakur Prasad, Kalka-Bindadin Maharaj, Achchan Maharaj, Shambhu Maharaj, Lachhu Maharaj, and legendary <strong>Pandit Birju Maharaj</strong> (Padma Vibhushan). Focuses on <em>Nazakat</em> (grace), <em>Bhav</em> (expression), and subtle Thumri abhinaya.</span>
                            <span class="lang-hi"><strong>लखनऊ घराने के दिग्गज:</strong> ईश्वरी प्रसाद द्वारा संस्थापित। कालका-बिंदादीन महाराज, अच्छन महाराज, शंभू महाराज, लच्छू महाराज, व पद्म विभूषण <strong>पं. बिरजू महाराज</strong>। नफासत, नजाकत व भाव-अभिनय पर विशेष बल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kathak is the sole classical dance originating in Uttar Pradesh/North India. Nawab Wajid Ali Shah wrote under the pen-name 'Akhtarpiya'!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कत्थक उत्तर प्रदेश/उत्तर भारत का एकमात्र शास्त्रीय नृत्य है। नवाब वाजिद अली शाह 'अख्तरपिया' उपनाम से बंदिशें लिखते थे!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Banaras Gharana (Tabla, Shehnai & Vocal) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-music" style="color: #d97706;"></i>
                    <span class="lang-en">4. Banaras Musical Gharana</span>
                    <span class="lang-hi">4. बनारस संगीत घराना (शहनाई, तबला व गायन)</span>
                </h4>
                <span class="mindmap-node-tag">UNESCO City of Music (Varanasi)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-guitar"></i>
                        <span class="lang-en">Maestros &amp; Sacred Classical Tradition</span>
                        <span class="lang-hi">महान संगीत साधक एवं परंपरा</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Shehnai:</strong> Ustad Bismillah Khan (Bharat Ratna 2001)</span>
                        <span class="mindmap-chip"><strong>Tabla Founder:</strong> Pandit Ram Sahai</span>
                        <span class="mindmap-chip"><strong>Tabla Legends:</strong> Samta Prasad (Gudai Maharaj) &amp; Kishen Maharaj</span>
                        <span class="mindmap-chip"><strong>Queen of Thumri:</strong> Girija Devi (पद्म विभूषण)</span>
                        <span class="mindmap-chip"><strong>Vocal Maestros:</strong> Siddheshwari Devi &amp; Rasoolan Bai</span>
                        <span class="mindmap-chip"><strong>Khayal Duet:</strong> Pt. Rajan &amp; Sajan Mishra</span>
                        <span class="mindmap-chip"><strong>Sitar Legend:</strong> Pt. Ravi Shankar (Bharat Ratna 1999)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-record-vinyl"></i>
                        <span class="lang-en">Banaras Semi-Classical Vocal Forms</span>
                        <span class="lang-hi">बनारस के उप-शास्त्रीय गायन रूप</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Semi-Classical Genres:</strong> Banaras is the capital of <strong>Thumri</strong>, <strong>Dadra</strong>, <strong>Chaiti</strong>, <strong>Kajri</strong>, and <strong>Tappa</strong>. Varanasi is declared a <em>UNESCO City of Music</em> under Creative Cities Network.</span>
                            <span class="lang-hi"><strong>उप-शास्त्रीय विधाएं:</strong> बनारस <strong>ठुमरी</strong>, <strong>दादरा</strong>, <strong>चैती</strong>, <strong>कजरी</strong> व <strong>टप्पा</strong> का विश्व केंद्र है। वाराणसी को यूनेस्को द्वारा 'संगीत का शहर' घोषित किया गया है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ustad Bismillah Khan received Bharat Ratna in 2001. Pt. Ravi Shankar (born in Varanasi) received Bharat Ratna in 1999. Girija Devi is renowned as the 'Queen of Thumri'!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उस्ताद बिस्मिल्लाह खान को 2001 में और पं. रविशंकर को 1999 में भारत रत्न मिला। गिरिजा देवी को 'ठुमरी की साम्राज्ञी' कहा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Vocal Gharanas: Kirana, Agra & Atrauli -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microphone-lines" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Vocal Gharanas of UP</span>
                    <span class="lang-hi">5. उप्र के प्रमुख गायन घराने</span>
                </h4>
                <span class="mindmap-node-tag">Kirana • Agra • Atrauli</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-users-line"></i>
                        <span class="lang-en">Founders &amp; Classical Lineages</span>
                        <span class="lang-hi">संस्थापक एवं शास्त्रीय परंपराएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kirana Gharana (Muzaffarnagar):</strong> Founded by <strong>Ustad Abdul Karim Khan</strong> and <strong>Abdul Wahid Khan</strong> at village Kairana (Shamli/Muzaffarnagar). Renowned for emotional Swara delineation and slow Vilambit Khayal. Stalwarts: <em>Pandit Bhimsen Joshi</em> (Bharat Ratna 2008) and <em>Gangubai Hangal</em>.</span>
                            <span class="lang-hi"><strong>किराना घराना (मुजफ्फरनगर/शामली):</strong> <strong>उस्ताद अब्दुल करीम खां</strong> व <strong>अब्दुल वाहिद खां</strong> द्वारा कैराना गांव में स्थापित। सुर लगाव व विलंबित खयाल गायकी हेतु प्रसिद्ध। प्रमुख गायक: <em>पं. भीमसेन जोशी</em> (भारत रत्न 2008) व <em>गंगूबाई हंगल</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Agra Gharana ('Rangila' Gharana):</strong> Founded by Haji Sujan Khan (court of Akbar) and revitalized by <strong>Ustad Faiyaz Khan ('Prempiya')</strong>. Blends Dhrupad-Dhamar vigor with Khayal improvisation; emphasizes Nom-Tom alap.</span>
                            <span class="lang-hi"><strong>आगरा घराना ('रंगीला' घराना):</strong> हाजी सुजान खां द्वारा प्रवर्तित, <strong>उस्ताद फैयाज खां ('प्रेमपिया')</strong> द्वारा पुनर्जीवित। ध्रुपद-धमार के ओज व खयाल गायकी का अद्भुत संगम; नोम-तोम आलाप की प्रधानता।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Atrauli Gharana (Aligarh):</strong> Founded by Ustad Alladiya Khan; famous for intricate bandishes and rare ragas (Anvat Ragas).</span>
                            <span class="lang-hi"><strong>अतरौली घराना (अलीगढ़):</strong> उस्ताद अल्लादिया खां द्वारा स्थापित; जटिल बंदिशों व अप्रचलित रागों की गायकी हेतु प्रसिद्ध।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kirana Gharana originated in Kairana (UP) founded by Abdul Karim Khan. Pt. Bhimsen Joshi (Bharat Ratna) belonged to Kirana Gharana!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> किराना घराना कैराना (उप्र) में अब्दुल करीम खां द्वारा स्थापित हुआ। पं. भीमसेन जोशी (भारत रत्न) किराना घराने से संबंधित थे!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Folk Theatres & Living Art Forms -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-masks-theater" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Folk Theatre &amp; Performing Arts</span>
                    <span class="lang-hi">6. लोक नाट्य एवं पारंपरिक प्रदर्शन कलाएँ</span>
                </h4>
                <span class="mindmap-node-tag">Nautanki • Ramlila (UNESCO) • Raslila</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-theater-masks"></i>
                        <span class="lang-en">Major Folk Drama Forms</span>
                        <span class="lang-hi">प्रमुख लोक नाट्य रूप</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nautanki (नौटंकी):</strong> Secular musical street theatre featuring rhymed dialogue in Doha, Chaubola, and Lavani set to Nagada and Dholak rhythms. Two major schools: <strong>Hathras School</strong> (operatic singing, classical ragas) and <strong>Kanpur School</strong> (theatrical dialogues and social themes).</span>
                            <span class="lang-hi"><strong>नौटंकी:</strong> नगाड़ा व ढोलक की थाप पर दोहा, चौबोला व लावणी में प्रस्तुत लोकप्रिय संगीतमय लोकनाट्य। दो प्रमुख शैलियां: <strong>हाथरस शैली</strong> (गायन प्रधान, शास्त्रीय राग) तथा <strong>कानपुर शैली</strong> (अभिनय व संवाद प्रधान)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ramnagar Ramlila (Varanasi):</strong> World's oldest environmental theatre founded by Maharaja Udit Narayan Singh (~1830). Performed over 31 days with whole town as stage; inscribed on <strong>UNESCO Intangible Cultural Heritage List (2008)</strong>.</span>
                            <span class="lang-hi"><strong>रामनगर की रामलीला (वाराणसी):</strong> काशी नरेश उदित नारायण सिंह द्वारा ~1830 में प्रारंभ। 31 दिनों तक पूरे नगर में मंचित; <strong>2008 में यूनेस्को की अमूर्त सांस्कृतिक धरोहर</strong> में शामिल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Raslila &amp; Amir Khusrau's Legacy:</strong> <em>Raslila</em> of Braj depicts divine playful love of Radha-Krishna (founded by Swami Harivansh); <em>Amir Khusrau</em> (born at Patiali, Kasganj in 1253 CE) invented Khayal singing, Qawwali, Sitar and Tabla.</span>
                            <span class="lang-hi"><strong>रासलीला व अमीर खुसरो:</strong> ब्रज की <em>रासलीला</em> राधा-कृष्ण की लीलाओं पर आधारित; <em>अमीर खुसरो</em> (पटियाली, कासगंज में 1253 में जन्मे) ने खयाल गायन, कव्वाली, सितार व तबले का आविष्कार किया।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Amir Khusrau (born in Patiali, Kasganj) is the father of Qawwali, Khayal, Sitar and Hindustani Tabla. Ramnagar Ramlila holds UNESCO Intangible Heritage status!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> अमीर खुसरो (जन्म: पटियाली, कासगंज) को कव्वाली, खयाल, सितार व तबले का जनक माना जाता है। रामनगर रामलीला यूनेस्को की अमूर्त धरोहर है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 4: Business and Employment
# ==============================================================================
mm_business = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Business &amp; Employment in Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश में व्यापार, उद्योग एवं रोजगार</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • $1 Trillion Economy Vision • MSME Leader (90 Lakh Units) • ODOP Flagship Architecture • Industrial Expressways &amp; Freight Corridors • Defense Industrial Corridor • Skill Missions &amp; Job Portals</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • $1 ट्रिलियन अर्थव्यवस्था का लक्ष्य • MSME में देश में प्रथम (90 लाख इकाइयाँ) • ODOP योजना वास्तुकला • औद्योगिक एक्सप्रेसवे व फ्रेट कॉरिडोर • रक्षा औद्योगिक गलियारा • कौशल विकास मिशन व रोजगार पोर्टल</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-briefcase"></i>
            <span class="lang-en">Business Ecosystem, Investment &amp; Employment Engines of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का व्यावसायिक तंत्र, निवेश एवं रोजगार के प्रमुख इंजन</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Macroeconomy & $1 Trillion Vision -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-chart-line" style="color: #059669;"></i>
                    <span class="lang-en">1. Macroeconomy &amp; $1T Target</span>
                    <span class="lang-hi">1. अर्थव्यवस्था एवं $1 ट्रिलियन का लक्ष्य</span>
                </h4>
                <span class="mindmap-node-tag">2nd Largest State Economy</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-coins"></i>
                        <span class="lang-en">Macroeconomic Fundamentals</span>
                        <span class="lang-hi">मैक्रोइकॉनॉमिक संकेतक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Rank 2:</strong> Largest State Economy in India (~9.2% share)</span>
                        <span class="mindmap-chip"><strong>GSDP:</strong> Exceeding ₹25+ Lakh Crore (~$300B+)</span>
                        <span class="mindmap-chip"><strong>Vision 2027-28:</strong> $1 Trillion Economy Target</span>
                        <span class="mindmap-chip"><strong>Workforce:</strong> ~6.6 Crore Total Workers</span>
                        <span class="mindmap-chip"><strong>Agri Employment:</strong> ~59.3% of workforce</span>
                        <span class="mindmap-chip"><strong>Services &amp; Industry:</strong> Rapidly expanding share</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-bullseye"></i>
                        <span class="lang-en">Growth Drivers &amp; Fiscal Strength</span>
                        <span class="lang-hi">विकास चालक एवं वित्तीय सुदृढ़ता</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Revenue Surplus &amp; Capex:</strong> UP consistently maintains a revenue surplus while channeling over 20% of its budget into capital expenditure (infrastructure creation).</span>
                            <span class="lang-hi"><strong>राजस्व अधिशेष व पूंजीगत व्यय:</strong> उप्र लगातार राजस्व अधिशेष बनाए रखते हुए अपने बजट का 20% से अधिक बुनियादी ढांचे के विकास पर खर्च कर रहा है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has set a formal target to transform into a <strong>$1 Trillion Economy by 2027-28</strong>. It is currently India's second largest state economy!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र ने <strong>2027-28 तक $1 ट्रिलियन अर्थव्यवस्था</strong> बनने का औपचारिक लक्ष्य रखा है। यह वर्तमान में देश की दूसरी सबसे बड़ी राज्य अर्थव्यवस्था है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: MSME Sector: The Growth Engine -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-industry" style="color: #0284c7;"></i>
                    <span class="lang-en">2. MSME Powerhouse (Rank 1)</span>
                    <span class="lang-hi">2. MSME का पावरहाउस (देश में प्रथम)</span>
                </h4>
                <span class="mindmap-node-tag">90 Lakh+ Units • 14% of India</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-boxes-stacked"></i>
                        <span class="lang-en">MSME Scale &amp; State Schemes</span>
                        <span class="lang-hi">MSME का आकार एवं प्रमुख राज्य योजनाएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Total Units:</strong> Over 90 Lakh (9 million) MSMEs</span>
                        <span class="mindmap-chip"><strong>National Share:</strong> ~14% of all Indian MSMEs (Rank 1)</span>
                        <span class="mindmap-chip"><strong>MSME Policy 2022:</strong> Capital subsidy &amp; plug-and-play estates</span>
                        <span class="mindmap-chip"><strong>Pledge Park Scheme:</strong> Private industrial park subsidies</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-user-gear"></i>
                        <span class="lang-en">Self-Employment &amp; Artisan Schemes</span>
                        <span class="lang-hi">स्वरोजगार एवं पारंपरिक कारीगर योजनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mukhyamantri Yuva Swarojgar Yojana (MYSY):</strong> Provides bank loans with margin money subsidy up to <strong>₹25 Lakh</strong> for setting up industrial ventures and <strong>₹10 Lakh</strong> for service enterprises.</span>
                            <span class="lang-hi"><strong>मुख्यमंत्री युवा स्वरोजगार योजना:</strong> उद्योग स्थापित करने हेतु <strong>₹25 लाख</strong> तथा सेवा क्षेत्र हेतु <strong>₹10 लाख</strong> तक के ऋण पर मार्जिन मनी सब्सिडी प्रदान की जाती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Vishwakarma Shram Samman Yojana (VSSY):</strong> Imparts 6-day free advanced skill training, modern toolkits, and subsidized loan linkages to traditional rural artisans (blacksmiths, potters, carpenters, cobblers, tailors, barbers).</span>
                            <span class="lang-hi"><strong>विश्वकर्मा श्रम सम्मान योजना:</strong> 14 पारंपरिक ग्रामीण दस्तकारों (बढ़ई, लोहार, कुम्हार, मोची, दर्जी आदि) को 6 दिवसीय निःशुल्क प्रशिक्षण, टूलकिट व ऋण सुविधा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Uttar Pradesh ranks #1 in India with over 90 lakh MSME units. MYSY offers loan subsidy up to ₹25 lakh for industry!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र 90 लाख से अधिक MSME इकाइयों के साथ देश में प्रथम स्थान पर है। युवा स्वरोजगार योजना में उद्योग हेतु ₹25 लाख तक सहायता मिलती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: One District One Product (ODOP) Scheme -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gift" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. One District One Product (ODOP)</span>
                    <span class="lang-hi">3. एक जिला एक उत्पाद (ODOP) योजना</span>
                </h4>
                <span class="mindmap-node-tag">Launched 24 Jan 2018 • 75 Districts</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-calendar-check"></i>
                        <span class="lang-en">Scheme Architecture &amp; National Benchmark</span>
                        <span class="lang-hi">योजना का स्वरूप एवं राष्ट्रीय विस्तार</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Launch &amp; Vision:</strong> Launched on <strong>24 January 2018 (UP Diwas)</strong> by Chief Minister Yogi Adityanath. Aims to revitalize specialized indigenous traditional crafts/products across all 75 districts. Its remarkable success led the Central Government to adopt ODOP nationwide.</span>
                            <span class="lang-hi"><strong>शुभारंभ:</strong> <strong>24 जनवरी 2018 (उप्र दिवस)</strong> को मुख्यमंत्री योगी आदित्यनाथ द्वारा प्रारंभ। सभी 75 जिलों के विशिष्ट पारंपरिक उत्पादों को बढ़ावा देना। केंद्र सरकार ने इसे पूरे देश में लागू किया।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-list-check"></i>
                        <span class="lang-en">Key District-Product Pairings</span>
                        <span class="lang-hi">प्रमुख जिले एवं उनके विशिष्ट उत्पाद</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Lucknow:</strong> Chikankari &amp; Zari Zardozi</span>
                        <span class="mindmap-chip"><strong>Varanasi:</strong> Banarasi Silk Sarees &amp; Zari</span>
                        <span class="mindmap-chip"><strong>Moradabad:</strong> Metal Craft &amp; Brassware</span>
                        <span class="mindmap-chip"><strong>Firozabad:</strong> Glassware &amp; Bangles</span>
                        <span class="mindmap-chip"><strong>Kannauj:</strong> Attar &amp; Perfumery</span>
                        <span class="mindmap-chip"><strong>Bhadohi:</strong> Hand-Knotted Carpet (कालीन)</span>
                        <span class="mindmap-chip"><strong>Aligarh:</strong> Locks &amp; Hardware (ताले)</span>
                        <span class="mindmap-chip"><strong>Meerut:</strong> Sports Goods (खेल का सामान)</span>
                        <span class="mindmap-chip"><strong>Gorakhpur:</strong> Terracotta Art (टेराकोटा)</span>
                        <span class="mindmap-chip"><strong>Agra / Kanpur:</strong> Leather Products (चमड़ा उत्पाद)</span>
                        <span class="mindmap-chip"><strong>Saharanpur:</strong> Wooden Carving (काष्ठ शिल्प)</span>
                        <span class="mindmap-chip"><strong>Pratapgarh:</strong> Aonla Processing (आँवला)</span>
                        <span class="mindmap-chip"><strong>Siddharthnagar:</strong> Kalanamak Rice (कालानमक चावल)</span>
                        <span class="mindmap-chip"><strong>Muzaffarnagar:</strong> Jaggery (गुड़ उत्पाद)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> ODOP was launched on UP Diwas (24 Jan 2018). Match-the-column questions for ODOP products and districts are asked in virtually every exam!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ODOP का शुभारंभ उप्र दिवस (24 जनवरी 2018) को हुआ। जिले व उनके ODOP उत्पाद का मिलान परीक्षा में अनिवार्य रूप से पूछा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Expressways & Industrial Corridors -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-road" style="color: #d97706;"></i>
                    <span class="lang-en">4. Expressways &amp; Freight Corridors</span>
                    <span class="lang-hi">4. एक्सप्रेसवे नेटवर्क एवं फ्रेट कॉरिडोर</span>
                </h4>
                <span class="mindmap-node-tag">Expressway Capital of India</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-highway"></i>
                        <span class="lang-en">World-Class Expressway Network</span>
                        <span class="lang-hi">विश्वस्तरीय एक्सप्रेसवे तंत्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Purvanchal Expressway (341 km):</strong> Connects Chand Sarai (Lucknow) to Haidaria (Ghazipur); passes through 9 districts; features a 3.2 km emergency airstrip at Kurebhar (Sultanpur).</span>
                            <span class="lang-hi"><strong>पूर्वांचल एक्सप्रेसवे (341 किमी):</strong> चांद सराय (लखनऊ) से हैदरिया (गाजीपुर); 9 जिलों से गुजरता है; सुल्तानपुर के कूड़ेभार में 3.2 किमी की एयरस्ट्रिप।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bundelkhand Expressway (296 km):</strong> Connects Bharatkoop (Chitrakoot) to Kudrail (Etawah) joining Agra-Lucknow Expressway; passes through 7 districts.</span>
                            <span class="lang-hi"><strong>बुंदेलखंड एक्सप्रेसवे (296 किमी):</strong> भरतकूप (चित्रकूट) से कुदरैल (इटावा); 7 जिलों को जोड़ते हुए आगरा-लखनऊ एक्सप्रेसवे से मिलता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ganga Expressway (594 km - Under Construction):</strong> UP's longest upcoming expressway from Bijauli (Meerut) to Judapur Dandu (Prayagraj); connects 12 districts with airstrip at Jalalabad (Shahjahanpur).</span>
                            <span class="lang-hi"><strong>गंगा एक्सप्रेसवे (594 किमी):</strong> मेरठ के बिजौली से प्रयागराज के जुदापुर दांदू तक; 12 जिलों से गुजरने वाला उप्र का सबसे लंबा एक्सप्रेसवे (शाहजहाँपुर में एयरस्ट्रिप)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-train-subway"></i>
                        <span class="lang-en">Dedicated Freight Corridors (DFC) Junction</span>
                        <span class="lang-hi">समर्पित माल ढुलाई गलियारा (DFC) संगम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Dadri (Greater Noida):</strong> Intersection of EDFC &amp; WDFC</span>
                        <span class="mindmap-chip"><strong>EDFC (Eastern Corridor):</strong> Ludhiana to Dankuni (passes through UP)</span>
                        <span class="mindmap-chip"><strong>WDFC (Western Corridor):</strong> Dadri to JNPT Mumbai</span>
                        <span class="mindmap-chip"><strong>Multi-Modal Logistics Hub:</strong> Dadri and Boraki</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Dadri is the junction of both Eastern and Western Dedicated Freight Corridors. Purvanchal is 341 km, Bundelkhand is 296 km, and Ganga is 594 km!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> दादरी पूर्वी व पश्चिमी दोनों फ्रेट कॉरिडोर का संगम है। पूर्वांचल एक्सप्रेसवे 341 किमी, बुंदेलखंड 296 किमी व गंगा 594 किमी लंबा है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Defense Corridor & Investment Summits -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Defense Corridor &amp; Investment</span>
                    <span class="lang-hi">5. रक्षा गलियारा एवं वैश्विक निवेश</span>
                </h4>
                <span class="mindmap-node-tag">6 Defense Nodes • GIS ₹33.5T</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crosshairs"></i>
                        <span class="lang-en">UP Defense Industrial Corridor (UPDIC)</span>
                        <span class="lang-hi">उत्तर प्रदेश रक्षा औद्योगिक गलियारा</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Node 1:</strong> Lucknow (BrahMos Aerospace missile unit)</span>
                        <span class="mindmap-chip"><strong>Node 2:</strong> Kanpur (Ordnance, Small arms &amp; Drones)</span>
                        <span class="mindmap-chip"><strong>Node 3:</strong> Jhansi (Bharat Dynamics missile propulsion)</span>
                        <span class="mindmap-chip"><strong>Node 4:</strong> Agra (Military logistics &amp; footwear)</span>
                        <span class="mindmap-chip"><strong>Node 5:</strong> Aligarh (Precision metal components &amp; locks)</span>
                        <span class="mindmap-chip"><strong>Node 6:</strong> Chitrakoot (Specialized defense support)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-handshake"></i>
                        <span class="lang-en">Global Investors Summit (GIS) &amp; Ease of Doing Business</span>
                        <span class="lang-hi">ग्लोबल इन्वेस्टर्स समिट एवं ईज ऑफ डूइंग बिजनेस</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP GIS 2023:</strong> Held in Lucknow in February 2023; generated investment intent of over <strong>₹33.5 Lakh Crore</strong> across renewable energy, manufacturing, data centers, and electronics.</span>
                            <span class="lang-hi"><strong>यूपी जीआईएस 2023:</strong> लखनऊ में आयोजित; <strong>₹33.5 लाख करोड़</strong> से अधिक के निवेश प्रस्ताव प्राप्त हुए।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nivesh Mitra Portal:</strong> Single window clearance portal integrating 400+ online citizen and investor services; transformed UP into an Achiever state in Business Reforms Action Plan (BRAP).</span>
                            <span class="lang-hi"><strong>निवेश मित्र पोर्टल:</strong> 400 से अधिक ऑनलाइन सेवाओं वाला सिंगल विंडो क्लीयरेंस पोर्टल; ईज ऑफ डूइंग बिजनेस में उप्र 'अचीवर' राज्य बना।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> The 6 nodes of UP Defense Industrial Corridor are Lucknow, Kanpur, Agra, Aligarh, Jhansi, and Chitrakoot! BrahMos missiles are manufactured in Lucknow.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> रक्षा गलियारे के 6 नोड हैं: लखनऊ, कानपुर, आगरा, अलीगढ़, झांसी और चित्रकूट! ब्रह्मोस मिसाइल निर्माण केंद्र लखनऊ में है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Skill Ecosystem & Employment Missions -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-graduation-cap" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Skill Missions &amp; Employment</span>
                    <span class="lang-hi">6. कौशल विकास मिशन एवं रोजगार अभियान</span>
                </h4>
                <span class="mindmap-node-tag">UPSDM 2013 • Rojgar Sangam</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-briefcase"></i>
                        <span class="lang-en">Employment Portals &amp; Mega Industrial Parks</span>
                        <span class="lang-hi">रोजगार पोर्टल एवं मेगा औद्योगिक पार्क</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Skill Development Mission (UPSDM):</strong> Launched in <strong>2013</strong>; UP became the first state in India to establish a unified right-to-skill mission for youth aged 14–35 years.</span>
                            <span class="lang-hi"><strong>उप्र कौशल विकास मिशन (UPSDM):</strong> <strong>2013</strong> में स्थापित; युवाओं को कौशल प्रशिक्षण का अधिकार देने वाला देश का पहला राज्य बना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rojgar Sangam Portal:</strong> Unified digital placement portal connecting unemployed youth with private employers, tracking mega job fairs (Rojgar Melas) across all 75 districts.</span>
                            <span class="lang-hi"><strong>रोजगार संगम पोर्टल:</strong> 75 जिलों में आयोजित रोजगार मेलों व निजी कंपनियों में युवाओं की सीधी भर्ती हेतु राज्य का एकीकृत पोर्टल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mega Parks &amp; IT Clusters:</strong> <em>PM MITRA Mega Textile Park</em> (1000 acres across Lucknow-Hardoi); <em>Mega Leather Park</em> at Ramaipur (Kanpur); <em>Noida/Greater Noida</em> as India's leading mobile manufacturing &amp; electronics cluster.</span>
                            <span class="lang-hi"><strong>मेगा पार्क व आईटी क्लस्टर:</strong> <em>पीएम मित्र टेक्सटाइल पार्क</em> (लखनऊ-हरदोई में 1000 एकड़); <em>मेगा लेदर पार्क</em> रमईपुर (कानपुर); <em>नोएडा-ग्रेटर नोएडा</em> देश का प्रमुख मोबाइल व इलेक्ट्रॉनिक्स विनिर्माण केंद्र।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP was the first state in India to establish a Skill Development Mission (2013). PM MITRA Mega Textile Park is situated across Lucknow &amp; Hardoi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कौशल विकास मिशन स्थापित करने वाला पहला राज्य उप्र (2013) था। पीएम मित्र टेक्सटाइल पार्क लखनऊ व हरदोई में स्थित है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Helper to inject and clean mermaid
# ==============================================================================
def inject_mindmap(topic_dir, mindmap_content):
    path = os.path.join('upsssc-up-gk', topic_dir, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match Card 1
    m1 = re.search(r'(<!--\s*Card 1:\s*Mind Map\s*-->.*?)(<!--\s*Card 2:)', content, re.DOTALL)
    m2 = re.search(r'(<div class="card-premium">.*?Mindmap.*?)(<div class="card-premium")', content, re.DOTALL | re.IGNORECASE)

    if m1:
        target = m1.group(1)
        content = content.replace(target, mindmap_content + '\n\n')
    elif m2:
        target = m2.group(1)
        content = content.replace(target, mindmap_content + '\n\n')
    else:
        print(f"ERROR: Could not match mindmap section in {topic_dir}")
        return False

    # Remove mermaid scripts
    content = re.sub(r'<script\s+src="https://cdn\.jsdelivr\.net/npm/mermaid/dist/mermaid\.min\.js"></script>\s*', '', content)
    content = re.sub(r'<script>mermaid\.initialize\(\{startOnLoad:true,\s*theme:\s*\'default\'\}\);</script>\s*', '', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated: {topic_dir}")
    return True

if __name__ == '__main__':
    inject_mindmap('agriculture', mm_agriculture)
    inject_mindmap('architecture', mm_architecture)
    inject_mindmap('art', mm_art)
    inject_mindmap('business-and-employment', mm_business)
