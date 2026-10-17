# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 17: Natural Resources of Uttar Pradesh
# ==============================================================================
mm_natural_resources = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Natural Resources of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के प्राकृतिक संसाधन, जल संपदा एवं आर्द्रभूमियाँ</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • River Drainage &amp; Ganga-Yamuna Basins • Canal Networks (Sharda 12,368 km &amp; Saryu Nahar) • Major Multi-Purpose Dams (Rihand / Govind Ballabh Pant Sagar) • Groundwater Dynamics &amp; Tubewell Overdraft • Natural Lakes &amp; 10 Ramsar Wetlands • Agro-Ecological Wealth</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • गंगा-यमुना अपवाह तंत्र • नहर नेटवर्क (शारदा 12,368 किमी व सरयू नहर) • बहुउद्देशीय बांध (रिहंद / गोविद वल्लभ पंत सागर) • भूजल गतिकी व नलकूप दोहन • प्राकृतिक झीलें व 10 रामसर स्थल • कृषि-पारिस्थितिक संसाधन</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-water"></i>
            <span class="lang-en">Hydrological, Wetland &amp; Natural Resource Endowment of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की जल संपदा, नदी घाटियां, आर्द्रभूमियाँ एवं प्राकृतिक संपदा</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Water Resources & Major River Basins -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-route" style="color: #059669;"></i>
                    <span class="lang-en">1. River Systems &amp; Basins</span>
                    <span class="lang-hi">1. नदी तंत्र एवं प्रमुख जल ग्रहण क्षेत्र</span>
                </h4>
                <span class="mindmap-node-tag">Ganga Basin covers ~85% of UP</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water"></i>
                        <span class="lang-en">Major River Trajectories in UP</span>
                        <span class="lang-hi">प्रमुख नदियों का प्रवाह क्षेत्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ganga River (गंगा नदी):</strong> Longest and holiest river of UP; enters the state at <strong>Bijnor</strong>, flows through <strong>28 districts</strong> over 1,450 km, and exits at <strong>Ballia</strong> into Bihar. Major tributaries: Yamuna, Ramganga, Gomti, Ghaghara, Tons.</span>
                            <span class="lang-hi"><strong>गंगा नदी:</strong> उप्र की सबसे लंबी नदी; <strong>बिजनौर</strong> से प्रवेश, <strong>28 जिलों</strong> में 1,450 किमी प्रवाह, और <strong>बलिया</strong> से बिहार में निकास। प्रमुख सहायक: यमुना, रामगंगा, गोमती, घाघरा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Yamuna River (यमुना नदी):</strong> Enters at <strong>Saharanpur</strong> (Faizabad village); traverses 19 districts forming boundary with Haryana; merges with Ganga at <strong>Prayagraj Sangam</strong>. Major tributaries: Chambal, Betwa, Ken, Hindon.</span>
                            <span class="lang-hi"><strong>यमुना नदी:</strong> <strong>सहारनपुर</strong> से प्रवेश; 19 जिलों में प्रवाह; <strong>प्रयागराज संगम</strong> पर गंगा में विलय। सहायक नदियां: चंबल, बेतवा, केन, हिंडन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Gomti River (गोमती नदी):</strong> Unique plains-origin river arising from <strong>Fulhar Jheel (Gomat Tal) in Pilibhit</strong>; flows through Lucknow, Sultanpur, Jaunpur, and meets Ganga at Kaithi (Ghazipur).</span>
                            <span class="lang-hi"><strong>गोमती नदी:</strong> <strong>पीलीभीत की फुलहर झील (गोमत ताल)</strong> से निकलने वाली मैदानी नदी; लखनऊ, सुल्तानपुर, जौनपुर होते हुए गाजीपुर के कैथी में गंगा से संगम।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ganga enters at Bijnor and leaves at Ballia (flows through 28 districts). Gomti is the only major river originating in the plains from Fulhar Lake (Pilibhit)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> गंगा बिजनौर से प्रवेश कर बलिया से निकलती है (28 जिले)। गोमती मैदानी भाग में फुलहर झील (पीलीभीत) से निकलने वाली प्रमुख नदी है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Canal Irrigation Network & Interlinking Projects -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-diagram-project" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Canal Irrigation Network</span>
                    <span class="lang-hi">2. नहर सिंचाई तंत्र एवं नदी जोड़ो परियोजनाएं</span>
                </h4>
                <span class="mindmap-node-tag">Sharda 12,368 km • Ken-Betwa</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-network-wired"></i>
                        <span class="lang-en">State's Premier Canal Systems</span>
                        <span class="lang-hi">प्रमुख नहर प्रणालियाँ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sharda Canal (शारदा नहर):</strong> Longest canal network in UP (total length ~<strong>12,368 km</strong> including branches); constructed in <strong>1928</strong> from Banbasa on Sharda river.</span>
                            <span class="lang-hi"><strong>शारदा नहर:</strong> उप्र की सबसे लंबी नहर प्रणाली (शाखाओं सहित कुल ~<strong>12,368 किमी</strong>); <strong>1928</strong> में बनबासा (शारदा नदी) से निर्मित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Eastern Yamuna &amp; Upper Ganga Canals:</strong> <em>Eastern Yamuna Canal (1830)</em> is UP's oldest operational canal; <em>Upper Ganga Canal (1854)</em> drawn from Haridwar (engineered by Col. Proby Cautley); <em>Lower Ganga Canal (1878)</em> drawn from Narora.</span>
                            <span class="lang-hi"><strong>पूर्वी यमुना व ऊपरी गंगा नहर:</strong> <em>पूर्वी यमुना नहर (1830)</em> सबसे पुरानी चालू नहर; <em>ऊपरी गंगा नहर (1854)</em> हरिद्वार से (पी.बी. कॉटले); <em>निचली गंगा नहर (1878)</em> नरौरा से।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Saryu Nahar &amp; Ken-Betwa Link:</strong> <em>Saryu Nahar National Project (2021)</em> interlinks 5 rivers (Ghaghara, Saryu, Rapti, Banganga, Rohini) irrigating 14 lakh hectares in 9 eastern districts; <em>Ken-Betwa Project</em> is India's first national river interlink.</span>
                            <span class="lang-hi"><strong>सरयू नहर व केन-बेतवा लिंक:</strong> <em>सरयू नहर राष्ट्रीय परियोजना (2021)</em> 5 नदियों को जोड़कर 9 जिलों के 14 लाख हेक्टेयर सिंचित करती है; <em>केन-बेतवा</em> देश की पहली नदी जोड़ो परियोजना।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sharda Canal is the longest canal network (12,368 km). Eastern Yamuna Canal (1830) is the oldest. Ken-Betwa is India's first river link project!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> शारदा नहर उप्र की सबसे लंबी नहर (12,368 किमी) है। पूर्वी यमुना नहर (1830) सबसे पुरानी है। केन-बेतवा देश का पहला रिवर लिंक प्रोजेक्ट है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Major Multi-Purpose Dams & Reservoirs -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gem" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Major Dams &amp; Reservoirs</span>
                    <span class="lang-hi">3. प्रमुख बहुउद्देशीय बांध एवं जलाशय</span>
                </h4>
                <span class="mindmap-node-tag">Rihand • Matatila • Rajghat</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water-ladder"></i>
                        <span class="lang-en">Iconic Dams and River Projects</span>
                        <span class="lang-hi">प्रमुख बांध एवं उनकी नदियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Rihand Dam:</strong> Rihand River, Pipri (Sonbhadra) - Govind Ballabh Pant Sagar</span>
                        <span class="mindmap-chip"><strong>Matatila Dam:</strong> Betwa River (Lalitpur/Jhansi, built 1958)</span>
                        <span class="mindmap-chip"><strong>Rajghat Dam (Rani Lakshmibai):</strong> Betwa River (Lalitpur - joint UP &amp; MP)</span>
                        <span class="mindmap-chip"><strong>Parichha Dam:</strong> Betwa River (Jhansi - feeds thermal plant)</span>
                        <span class="mindmap-chip"><strong>Sukma-Dukma Dam:</strong> Betwa River (Jhansi)</span>
                        <span class="mindmap-chip"><strong>Bansagar Dam:</strong> Son River (Shahdol, MP - joint UP, MP &amp; Bihar)</span>
                        <span class="mindmap-chip"><strong>Meja Reservoir:</strong> Belan River (Prayagraj/Mirzapur)</span>
                        <span class="mindmap-chip"><strong>Jirgo &amp; Sirsi Dams:</strong> Mirzapur</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-lake"></i>
                        <span class="lang-en">Govind Ballabh Pant Sagar Milestone</span>
                        <span class="lang-hi">गोविंद वल्लभ पंत सागर की महत्ता</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Largest Artificial Reservoir:</strong> Govind Ballabh Pant Sagar behind Rihand Dam (Pipri, Sonbhadra) is India's largest artificial man-made lake by volume (~300 sq km area); powers HINDALCO aluminum smelter and regional grid.</span>
                            <span class="lang-hi"><strong>भारत की सबसे बड़ी कृत्रिम झील:</strong> रिहंद बांध (पिपरी, सोनभद्र) के पीछे स्थित गोविंद वल्लभ पंत सागर जल आयतन की दृष्टि से भारत की सबसे बड़ी मानव निर्मित कृत्रिम झील है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Govind Ballabh Pant Sagar (Rihand Dam, Sonbhadra) is India's largest artificial reservoir. Matatila and Rajghat dams are on Betwa River!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> गोविंद वल्लभ पंत सागर (रिहंद बांध, सोनभद्र) भारत का सबसे बड़ा मानव निर्मित जलाशय है। माताटीला व राजघाट बांध बेतवा नदी पर हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Groundwater Dynamics & Management -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-bore-hole" style="color: #d97706;"></i>
                    <span class="lang-en">4. Groundwater Dynamics</span>
                    <span class="lang-hi">4. भूजल गतिकी एवं जल संरक्षण योजनाएं</span>
                </h4>
                <span class="mindmap-node-tag">Tubewells: 73.4% • Atal Bhujal</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hand-holding-droplet"></i>
                        <span class="lang-en">Extraction &amp; Overdraft Issues</span>
                        <span class="lang-hi">भूजल दोहन एवं अति-शोषित विकास खंड</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tubewell Dominance:</strong> Tubewells account for <strong>73.4% of total irrigation</strong> in UP (first tubewell bored at Meerut in 1930). Intense extraction has pushed numerous western UP blocks into the <em>'Over-Exploited'</em> category.</span>
                            <span class="lang-hi"><strong>नलकूपों की प्रधानता:</strong> सिंचाई में नलकूपों की हिस्सेदारी <strong>73.4%</strong> है (पहला नलकूप 1930 मेरठ में)। अत्यधिक दोहन से पश्चिमी उप्र के कई ब्लॉक 'अति-शोषित' श्रेणी में पहुंचे हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Atal Bhujal &amp; Khet Talab Yojana:</strong> <em>Atal Bhujal Yojana</em> drives community groundwater recharge in Bundelkhand; <em>Khet Talab Yojana</em> provides 50% subsidy to farmers for digging farm ponds to harvest rainwater.</span>
                            <span class="lang-hi"><strong>अटल भूजल व खेत तालाब योजना:</strong> बुंदेलखंड में सामुदायिक भूजल पुनर्भरण हेतु <em>अटल भूजल योजना</em> तथा खेत में वर्षा जल संचयन हेतु 50% अनुदान पर <em>खेत तालाब योजना</em>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Tubewells are the #1 source of irrigation in UP (73.4%). First tubewell was bored in Meerut in 1930!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सिंचाई का सबसे बड़ा साधन नलकूप (73.4%) है। राज्य का पहला नलकूप 1930 में मेरठ में खोदा गया था!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Natural Lakes, Tals & 10 Ramsar Wetlands -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-water-ladder" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Lakes &amp; 10 Ramsar Wetlands</span>
                    <span class="lang-hi">5. प्राकृतिक झीलें, ताल एवं 10 रामसर स्थल</span>
                </h4>
                <span class="mindmap-node-tag">Upper Ganga (1st) • Bakhira (10th)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-dove"></i>
                        <span class="lang-en">The 10 Ramsar Wetlands of International Importance</span>
                        <span class="lang-hi">10 अंतरराष्ट्रीय महत्व के रामसर आर्द्रभूमि स्थल</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Upper Ganga River:</strong> Brijghat to Narora (First in UP, 2005)</span>
                        <span class="mindmap-chip"><strong>2. Nawabganj Bird Sanctuary:</strong> Unnao (Pt. Deen Dayal Upadhyay)</span>
                        <span class="mindmap-chip"><strong>3. Samaspur Bird Sanctuary:</strong> Raebareli</span>
                        <span class="mindmap-chip"><strong>4. Sandi Bird Sanctuary:</strong> Hardoi</span>
                        <span class="mindmap-chip"><strong>5. Parvati Arga Sanctuary:</strong> Gonda</span>
                        <span class="mindmap-chip"><strong>6. Saman Bird Sanctuary:</strong> Mainpuri</span>
                        <span class="mindmap-chip"><strong>7. Sarsai Nawar Jheel:</strong> Etawah</span>
                        <span class="mindmap-chip"><strong>8. Sur Sarovar (Keetham Lake):</strong> Agra</span>
                        <span class="mindmap-chip"><strong>9. Haiderpur Wetland:</strong> Bijnor/Muzaffarnagar (2021)</span>
                        <span class="mindmap-chip"><strong>10. Bakhira Wildlife Sanctuary:</strong> Sant Kabir Nagar (Notified 2022)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-fish"></i>
                        <span class="lang-en">Famous Historic Lakes &amp; Tals Directory</span>
                        <span class="lang-hi">प्रमुख ऐतिहासिक झीलें एवं ताल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Suraha Tal:</strong> Ballia (famous oxbow lake &amp; bird sanctuary); <strong>Ramgarh Tal:</strong> Gorakhpur; <strong>Moti &amp; Bhakt Jheel:</strong> Kanpur; <strong>Bara Tal:</strong> Shahjahanpur; <strong>Karela Jheel:</strong> Lucknow; <strong>Naujheel:</strong> Mathura.</span>
                            <span class="lang-hi"><strong>सुरहा ताल:</strong> बलिया (गोखुर झील); <strong>रामगढ़ ताल:</strong> गोरखपुर; <strong>मोती झील:</strong> कानपुर; <strong>बड़ा ताल:</strong> शाहजहाँपुर; <strong>करेला झील:</strong> लखनऊ; <strong>नौझील:</strong> मथुरा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 10 Ramsar sites. Upper Ganga River was the 1st (2005) and Bakhira (Sant Kabir Nagar) is the 10th (2022). Keetham Lake is in Agra!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में 10 रामसर स्थल हैं। ऊपरी गंगा प्रथम (2005) और बखिरा (संत कबीर नगर) 10वां स्थल है। कीठम झील आगरा में है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Land, Soil & Agro-Ecological Wealth -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-seedling" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Land &amp; Soil Wealth</span>
                    <span class="lang-hi">6. भूमि, मृदा एवं कृषि-पारिस्थितिक संसाधन</span>
                </h4>
                <span class="mindmap-node-tag">Khadar • Bhangar • Mar • Kabar</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Core Soil Belts of Uttar Pradesh</span>
                        <span class="lang-hi">उप्र के प्रमुख मृदा कटिबंध</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Alluvial Soils (जलोढ़ मृदा):</strong> Covers ~70% of state. <em>Khadar</em> (new flood alluvium, fertile, light colored) vs <em>Bhangar</em> (older elevated alluvium, rich in calcareous nodules / Kankar).</span>
                            <span class="lang-hi"><strong>जलोढ़ मृदा:</strong> राज्य का ~70% भाग। <em>खादर</em> (नवीन जलोढ़, उपजाऊ) तथा <em>बांगर</em> (पुरातन जलोढ़, कंकड़ युक्त)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bundelkhand Black Soils (काली मृदा):</strong> Locally called <strong>Mar (माड़)</strong> and <strong>Kabar (काबर)</strong>; highly clayey, self-ploughing black cotton soils (Regur).</span>
                            <span class="lang-hi"><strong>बुंदेलखंड की काली मिट्टी:</strong> स्थानीय नाम <strong>माड़</strong> और <strong>काबर</strong>; अत्यधिक चीका युक्त, स्वतः जुताई वाली कपास मृदा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Red Soils of Bundelkhand &amp; Vindhyas:</strong> Known as <strong>Parwa (पड़वा)</strong> and <strong>Rakar (रांकड़)</strong>; rich in iron oxide, suitable for pulses, gram and oilseeds.</span>
                            <span class="lang-hi"><strong>लाल मिट्टियाँ:</strong> <strong>पड़वा</strong> एवं <strong>रांकड़</strong>; आयरन ऑक्साइड की अधिकता, दलहन (चना) व तिलहन हेतु उपयुक्त।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Mar and Kabar are local names for Black soils in Bundelkhand, while Parwa and Rakar are Red soils!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बुंदेलखंड में काली मिट्टी को माड़ व काबर तथा लाल मिट्टी को पड़वा व रांकड़ कहा जाता है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 18: Polity and Administration of Uttar Pradesh
# ==============================================================================
mm_polity = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Polity &amp; Administration of UP</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की राजव्यवस्था, शासन एवं प्रशासनिक ढांचा</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Bicameral Legislature (403 Assembly + 100 Council) • Parliamentary Hegemony (80 Lok Sabha + 31 Rajya Sabha) • Executive (Governor &amp; CM Milestones) • Allahabad High Court (160 Judges) • 18 Divisions &amp; 75 Districts • 3-Tier Panchayati Raj</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • द्विसदनीय विधानमंडल (403 वि.स. + 100 वि.प.) • संसदीय प्रतिनिधित्व (80 लो.स. + 31 रा.स.) • कार्यपालिका (राज्यपाल व सीएम मील के पत्थर) • इलाहाबाद उच्च न्यायालय (160 न्यायाधीश) • 18 मण्डल व 75 जिले • 3-स्तरीय पंचायती राज</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-landmark"></i>
            <span class="lang-en">Constitutional Architecture, Executive &amp; Judiciary of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश की संवैधानिक संरचना, कार्यपालिका, न्यायपालिका एवं स्थानीय स्वशासन</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: State Legislature (Bicameral: 403 + 100 Seats) -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-landmark-dome" style="color: #059669;"></i>
                    <span class="lang-en">1. Bicameral Legislature</span>
                    <span class="lang-hi">1. द्विसदनीय राज्य विधानमंडल</span>
                </h4>
                <span class="mindmap-node-tag">403 Assembly • 100 Council</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-users"></i>
                        <span class="lang-en">Legislative Assembly (Vidhan Sabha - विधानसभा)</span>
                        <span class="lang-hi">विधानसभा की संरचना एवं आरक्षण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Total Strength:</strong> <strong>403 directly elected MLAs</strong> (largest Assembly in India; Anglo-Indian nomination discontinued by 104th CAA 2019).</span>
                            <span class="lang-hi"><strong>कुल सदस्य संख्या:</strong> <strong>403 प्रत्यक्ष निर्वाचित सदस्य</strong> (देश की सबसे बड़ी विधानसभा; 104वें संविधान संशोधन द्वारा आंग्ल-भारतीय मनोनयन समाप्त)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Reserved Seats:</strong> Total 86 reserved seats: <strong>84 for Scheduled Castes (SC)</strong> and <strong>2 for Scheduled Tribes (ST)</strong>. Both ST seats (Obra and Duddhi) are in <strong>Sonbhadra district</strong>.</span>
                            <span class="lang-hi"><strong>आरक्षित सीटें:</strong> कुल 86 सीटें; <strong>84 अनुसूचित जाति (SC)</strong> तथा <strong>2 अनुसूचित जनजाति (ST)</strong> हेतु आरक्षित। दोनों ST सीटें (ओबरा व दुद्धी) <strong>सोनभद्र जिले</strong> में हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building-user"></i>
                        <span class="lang-en">Legislative Council (Vidhan Parishad - विधान परिषद)</span>
                        <span class="lang-hi">विधान परिषद की संरचना</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>100 Seats (Permanent House):</strong> Largest Upper House in India. Composition: 38 elected by MLAs, 36 by Local Bodies, 8 by Teachers, 8 by Graduates, and 10 nominated by the Governor.</span>
                            <span class="lang-hi"><strong>100 सीटें (स्थायी सदन):</strong> देश की सबसे बड़ी विधान परिषद; 38 विधायकों द्वारा, 36 स्थानीय निकायों द्वारा, 8 शिक्षकों द्वारा, 8 स्नातकों द्वारा निर्वाचित तथा 10 राज्यपाल द्वारा मनोनीत।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP Vidhan Sabha has 403 seats (84 SC + 2 ST in Sonbhadra). Vidhan Parishad has 100 seats. Both are the largest in India!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र विधानसभा में 403 सीटें (84 SC + 2 ST सोनभद्र में) तथा विधान परिषद में 100 सीटें हैं। दोनों देश में सर्वाधिक हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Parliamentary Representation (80 Lok Sabha + 31 Rajya Sabha) -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-handshake" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Parliamentary Hegemony</span>
                    <span class="lang-hi">2. संसद में प्रतिनिधित्व (80 लो.स. + 31 रा.स.)</span>
                </h4>
                <span class="mindmap-node-tag">80 Lok Sabha • 31 Rajya Sabha</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-check-to-slot"></i>
                        <span class="lang-en">Lok Sabha &amp; Rajya Sabha Strength</span>
                        <span class="lang-hi">लोकसभा एवं राज्यसभा की सीटें</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Lok Sabha Seats:</strong> 80 Seats (Rank 1 in India)</span>
                        <span class="mindmap-chip"><strong>SC Reserved in Lok Sabha:</strong> 17 Seats</span>
                        <span class="mindmap-chip"><strong>ST Reserved in Lok Sabha:</strong> 0 Seats (None)</span>
                        <span class="mindmap-chip"><strong>Rajya Sabha Seats:</strong> 31 Seats (Rank 1 in India)</span>
                        <span class="mindmap-chip"><strong>Prime Ministers from UP:</strong> 9 Indian Prime Ministers</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-scale-unbalanced-flip"></i>
                        <span class="lang-en">Political Hegemony ('Pathway to Delhi')</span>
                        <span class="lang-hi">राष्ट्रीय राजनीति की धुरी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Influence:</strong> UP sends 80 MPs to Lok Sabha (~14.7% of total House) and 31 MPs to Rajya Sabha. Produced 9 PMs: Nehru, Shastri, Indira Gandhi, Charan Singh, Rajiv Gandhi, V.P. Singh, Chandra Shekhar, Atal Bihari Vajpayee, and Narendra Modi (Varanasi MP).</span>
                            <span class="lang-hi"><strong>राष्ट्रीय प्रभाव:</strong> उप्र लोकसभा में 80 सांसद (~14.7%) तथा राज्यसभा में 31 सांसद भेजता है। देश को 9 प्रधानमंत्री दिए (नेहरू, शास्त्री, इंदिरा, चरण सिंह, अटल, मोदी आदि)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 80 Lok Sabha seats (17 reserved for SC, 0 for ST) and 31 Rajya Sabha seats, the highest in the country!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में 80 लोकसभा सीटें (17 SC आरक्षित, 0 ST आरक्षित) तथा 31 राज्यसभा सीटें हैं, जो देश में सर्वाधिक हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Executive Architecture: Governor, CM & President's Rule -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-user-tie" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Executive Leadership</span>
                    <span class="lang-hi">3. राज्य कार्यपालिका: राज्यपाल एवं मुख्यमंत्री</span>
                </h4>
                <span class="mindmap-node-tag">First Woman Governor &amp; CM</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crown"></i>
                        <span class="lang-en">Governors of Uttar Pradesh (Article 153–161)</span>
                        <span class="lang-hi">उत्तर प्रदेश के राज्यपाल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Governor (Post-Independence):</strong> <strong>Sarojini Naidu</strong> (15 Aug 1947 – 2 Mar 1949) — also the <strong>first woman Governor of any Indian state</strong>.</span>
                            <span class="lang-hi"><strong>प्रथम राज्यपाल:</strong> <strong>सरोजिनी नायडू</strong> (15 अगस्त 1947 - 2 मार्च 1949) — भारत के किसी भी राज्य की <strong>पहली महिला राज्यपाल</strong> भी थीं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Governor of Renamed UP:</strong> <strong>Hormasji Peroshaw Mody (H.P. Mody)</strong> was Governor when the state was officially renamed Uttar Pradesh on 24 Jan 1950.</span>
                            <span class="lang-hi"><strong>'उत्तर प्रदेश' नामकरण समय राज्यपाल:</strong> 24 जनवरी 1950 को जब नाम उत्तर प्रदेश हुआ, तब <strong>एच.पी. मोदी</strong> राज्यपाल थे।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-user-gear"></i>
                        <span class="lang-en">Chief Ministers of Uttar Pradesh (Article 163–167)</span>
                        <span class="lang-hi">उत्तर प्रदेश के मुख्यमंत्री</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Chief Minister:</strong> <strong>Pt. Govind Ballabh Pant</strong> (1946–1954; recipient of Bharat Ratna 1957).</span>
                            <span class="lang-hi"><strong>प्रथम मुख्यमंत्री:</strong> <strong>पं. गोविंद वल्लभ पंत</strong> (1946–1954; 1957 में भारत रत्न से सम्मानित)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Woman Chief Minister:</strong> <strong>Sucheta Kripalani</strong> (1963–1967) — also the <strong>first woman Chief Minister in India</strong>! Mayawati has served maximum times (4 times).</span>
                            <span class="lang-hi"><strong>प्रथम महिला मुख्यमंत्री:</strong> <strong>सुचेता कृपलानी</strong> (1963–1967) — भारत के किसी भी राज्य की <strong>पहली महिला मुख्यमंत्री</strong>! सुश्री मायावती 4 बार मुख्यमंत्री रहीं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>President's Rule (Article 356):</strong> Imposed <strong>10 times</strong> in UP (first imposed on 25 Feb 1968, last in 2002).</span>
                            <span class="lang-hi"><strong>राष्ट्रपति शासन (अनुच्छेद 356):</strong> उप्र में अब तक <strong>10 बार</strong> लगाया जा चुका है (पहली बार 1968, अंतिम बार 2002)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sarojini Naidu was India's 1st female Governor, and Sucheta Kripalani was India's 1st female Chief Minister! President's Rule imposed 10 times.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सरोजिनी नायडू देश की पहली महिला राज्यपाल तथा सुचेता कृपलानी देश की पहली महिला मुख्यमंत्री थीं! राष्ट्रपति शासन 10 बार लगा।</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Judiciary: Allahabad High Court (Sanctioned Strength: 160) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gavel" style="color: #d97706;"></i>
                    <span class="lang-en">4. Allahabad High Court</span>
                    <span class="lang-hi">4. न्यायपालिका: इलाहाबाद उच्च न्यायालय</span>
                </h4>
                <span class="mindmap-node-tag">Est. 1866 • 160 Judges (Max in India)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-scale-balanced"></i>
                        <span class="lang-en">Origins, Bench &amp; Judge Strength</span>
                        <span class="lang-hi">स्थापना, लखनऊ खंडपीठ एवं न्यायाधीश संख्या</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Establishment &amp; Relocation:</strong> Established on <strong>17 March 1866 at Agra</strong> under Indian High Courts Act 1861; shifted to <strong>Allahabad (Prayagraj) in 1869</strong>. Permanent Lucknow Bench created in 1948 by amalgamating Chief Court of Oudh.</span>
                            <span class="lang-hi"><strong>स्थापना व स्थानांतरण:</strong> <strong>17 मार्च 1866 को आगरा</strong> में स्थापना; <strong>1869 में इलाहाबाद</strong> स्थानांतरित। 1948 में लखनऊ स्थायी खंडपीठ का गठन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sanctioned Strength:</strong> <strong>160 Judges</strong> (120 permanent + 40 additional) — the largest High Court in India.</span>
                            <span class="lang-hi"><strong>स्वीकृत पद:</strong> <strong>160 न्यायाधीश</strong> (120 स्थायी + 40 अतिरिक्त) — भारत का सबसे बड़ा उच्च न्यायालय।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Chief Justices:</strong> First Chief Justice: <strong>Sir Walter Morgan</strong> (1866). First Indian Chief Justice: <strong>Shah Muhammad Sulaiman</strong> (1932). First Chief Justice of Independent India: <strong>Bidhu Bhushan Malik (B.B. Malik)</strong>.</span>
                            <span class="lang-hi"><strong>प्रथम मुख्य न्यायाधीश:</strong> प्रथम मुख्य न्यायाधीश <strong>सर वाल्टर मॉर्गन</strong> (1866)। प्रथम भारतीय मुख्य न्यायाधीश <strong>शाह मुहम्मद सुलेमान</strong> (1932)। स्वतंत्र भारत में प्रथम <strong>बी.बी. मलिक</strong>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Allahabad High Court was established at Agra in 1866 and shifted to Allahabad in 1869. Sanctioned judge strength is 160!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उच्च न्यायालय की स्थापना 1866 में आगरा में हुई व 1869 में इलाहाबाद आया। स्वीकृत न्यायाधीशों की संख्या 160 है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Administrative Structure: 18 Divisions & 75 Districts -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-sitemap" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Administrative Divisions</span>
                    <span class="lang-hi">5. प्रशासनिक संरचना: 18 मण्डल व 75 जनपद</span>
                </h4>
                <span class="mindmap-node-tag">18 Divisions • 75 Districts • 351 Tehsils</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-city"></i>
                        <span class="lang-en">18 Administrative Divisions (मण्डल)</span>
                        <span class="lang-hi">18 प्रशासनिक मण्डल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Largest Divisions (6 districts each):</strong> <strong>Lucknow</strong>, <strong>Kanpur</strong>, and <strong>Meerut</strong>.</span>
                            <span class="lang-hi"><strong>सबसे बड़े मण्डल (6-6 जिले):</strong> <strong>लखनऊ</strong>, <strong>कानपुर</strong> और <strong>मेरठ</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Smallest Divisions (3 districts each):</strong> Mirzapur, Basti, Jhansi, Saharanpur, and Azamgarh. 18th division created was <strong>Aligarh (2008)</strong>.</span>
                            <span class="lang-hi"><strong>सबसे छोटे मण्डल (3-3 जिले):</strong> मिर्जापुर, बस्ती, झांसी, सहारनपुर, आजमगढ़। 18वां मण्डल <strong>अलीगढ़ (2008)</strong> बना।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-map"></i>
                        <span class="lang-en">Extreme District Facts (75 Districts)</span>
                        <span class="lang-hi">75 जनपदों के प्रमुख तथ्य</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Largest by Area:</strong> Lakhimpur Kheri (7,680 sq km)</span>
                        <span class="mindmap-chip"><strong>Smallest by Area:</strong> Hapur (660 sq km)</span>
                        <span class="mindmap-chip"><strong>Most Populated District:</strong> Prayagraj (~59.5 Lakh)</span>
                        <span class="mindmap-chip"><strong>Least Populated District:</strong> Mahoba (~8.7 Lakh)</span>
                        <span class="mindmap-chip"><strong>Highest Literacy:</strong> Gautam Buddha Nagar (80.12%)</span>
                        <span class="mindmap-chip"><strong>Lowest Literacy:</strong> Shravasti (46.74%)</span>
                        <span class="mindmap-chip"><strong>Highest Sex Ratio:</strong> Jaunpur (1024 females / 1000 males)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Lakhimpur Kheri is largest by area and Hapur is smallest. Prayagraj is most populated, Mahoba least populated. Jaunpur has highest sex ratio (1024)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> लखीमपुर खीरी क्षेत्रफल में सबसे बड़ा व हापुड़ सबसे छोटा है। प्रयागराज सर्वाधिक आबादी व महोबा न्यूनतम आबादी वाला जिला है। जौनपुर में लिंगानुपात (1024) सर्वाधिक है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Panchayati Raj & Urban Local Governance -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-users-gear" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Panchayati Raj &amp; Urban Local</span>
                    <span class="lang-hi">6. पंचायती राज एवं नगरीय स्थानीय स्वशासन</span>
                </h4>
                <span class="mindmap-node-tag">3-Tier PRIs • 17 Nagar Nigams</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-people-roof"></i>
                        <span class="lang-en">3-Tier Panchayati Raj Structure</span>
                        <span class="lang-hi">त्रि-स्तरीय पंचायती राज ढांचा</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Statutory Evolution:</strong> UP Panchayati Raj Act 1947 enacted on 15 Aug 1949. Post-73rd CAA 1992, UP enacted the UP Panchayat Laws (Amendment) Act <strong>1994</strong> instituting 3 tiers: 1. Zila Panchayat (75); 2. Kshetra Panchayat / Block (826); 3. Gram Panchayat (~58,189). <strong>33% women reservation</strong>.</span>
                            <span class="lang-hi"><strong>त्रि-स्तरीय व्यवस्था:</strong> 1994 के संशोधन अधिनियम द्वारा लागू: 1. जिला पंचायत (75); 2. क्षेत्र पंचायत (826); 3. ग्राम पंचायत (~58,189)। महिलाओं हेतु <strong>33% आरक्षण</strong>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building-columns"></i>
                        <span class="lang-en">17 Municipal Corporations (नगर निगम)</span>
                        <span class="lang-hi">17 नगर निगम</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip">1. Lucknow</span>
                        <span class="mindmap-chip">2. Kanpur</span>
                        <span class="mindmap-chip">3. Agra</span>
                        <span class="mindmap-chip">4. Varanasi</span>
                        <span class="mindmap-chip">5. Prayagraj</span>
                        <span class="mindmap-chip">6. Meerut</span>
                        <span class="mindmap-chip">7. Bareilly</span>
                        <span class="mindmap-chip">8. Aligarh</span>
                        <span class="mindmap-chip">9. Moradabad</span>
                        <span class="mindmap-chip">10. Gorakhpur</span>
                        <span class="mindmap-chip">11. Ghaziabad</span>
                        <span class="mindmap-chip">12. Saharanpur</span>
                        <span class="mindmap-chip">13. Jhansi</span>
                        <span class="mindmap-chip">14. Firozabad</span>
                        <span class="mindmap-chip">15. Ayodhya</span>
                        <span class="mindmap-chip">16. Mathura-Vrindavan</span>
                        <span class="mindmap-chip">17. Shahjahanpur (17th, formed 2018)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 17 Municipal Corporations (Nagar Nigams); Shahjahanpur was created as the 17th in 2018. Women reservation in Panchayats is 33%!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में 17 नगर निगम हैं (17वां शाहजहाँपुर 2018 में बना)। पंचायतों में महिलाओं को 33% आरक्षण प्राप्त है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 19: Regional Languages of Uttar Pradesh
# ==============================================================================
mm_regional_languages = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Regional Languages &amp; Dialects of UP</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की भाषाएं, बोलियाँ एवं भाषाई भूगोल</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Official Languages (Hindi 1951 &amp; Urdu 1989) • Western Hindi Branch (Brajbhasha &amp; Khari Boli) • Kannauji &amp; Bundeli Dialects • Eastern Hindi Branch (Awadhi &amp; Bagheli) • Bihari Hindi Branch (Bhojpuri Dominance) • Language Academies</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • राजभाषाएं (हिंदी 1951 व उर्दू 1989) • पश्चिमी हिंदी उपशाखा (ब्रजभाषा व खड़ी बोली) • कन्नौजी व बुंदेली बोलियाँ • पूर्वी हिंदी उपशाखा (अवधी व बघेली) • बिहारी हिंदी (भोजपुरी का विशाल क्षेत्र) • राज्य भाषा संस्थान</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-language"></i>
            <span class="lang-en">Linguistic Matrix, Regional Dialects &amp; Official Languages of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का भाषाई स्वरूप, आंचलिक बोलियाँ एवं राजभाषा संरचना</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Official Languages & Statutory Framework -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-scale-balanced" style="color: #059669;"></i>
                    <span class="lang-en">1. Official Languages Status</span>
                    <span class="lang-hi">1. राजभाषा एवं वैधानिक ढांचा</span>
                </h4>
                <span class="mindmap-node-tag">Hindi 1951 • Urdu 1989</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-file-signature"></i>
                        <span class="lang-en">The Two Official Languages of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश की दो आधिकारिक भाषाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Official Language (Hindi):</strong> Declared the official language of Uttar Pradesh in <strong>October 1947</strong>; statutory backing via <em>UP Official Language Act 1951</em>. In <strong>1968</strong>, use of Hindi in Devanagari script was made mandatory for all official government transactions.</span>
                            <span class="lang-hi"><strong>प्रथम राजभाषा (हिंदी):</strong> अक्टूबर 1947 में घोषित; <em>उप्र राजभाषा अधिनियम 1951</em> द्वारा वैधानिक दर्जा। <strong>1968</strong> से सभी सरकारी कामकाज हेतु देवनागरी लिपि में हिंदी अनिवार्य।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Second Official Language (Urdu):</strong> <strong>Urdu</strong> was declared the second official language of UP in <strong>1989</strong> through the <em>UP Official Language (Amendment) Act 1989</em>.</span>
                            <span class="lang-hi"><strong>द्वितीय राजभाषा (उर्दू):</strong> <strong>1989</strong> में उप्र राजभाषा (संशोधन) अधिनियम द्वारा <strong>उर्दू</strong> को राज्य की द्वितीय आधिकारिक भाषा घोषित किया गया।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Hindi became mandatory for official business in 1968. Urdu was notified as the 2nd official language in 1989!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1968 में हिंदी को सभी सरकारी कार्यों हेतु अनिवार्य किया गया। उर्दू को 1989 में द्वितीय राजभाषा घोषित किया गया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Western Hindi Branch (Shauraseni Apabhramsha): Braj & Khari Boli -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-book" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Western Hindi: Braj &amp; Khari Boli</span>
                    <span class="lang-hi">2. पश्चिमी हिंदी: ब्रजभाषा एवं खड़ी बोली</span>
                </h4>
                <span class="mindmap-node-tag">Shauraseni Apabhramsha Origin</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-feather"></i>
                        <span class="lang-en">Brajbhasha (ब्रजभाषा) &amp; Khari Boli (कौरवी)</span>
                        <span class="lang-hi">ब्रजभाषा एवं खड़ी बोली का विस्तार</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Brajbhasha (ब्रजभाषा):</strong> Derived from Shauraseni Apabhramsha. Core districts: Mathura, Agra, Aligarh, Hathras, Firozabad, Etah, Mainpuri, Bareilly, Badaun. The glorious medium of Krishna Bhakti literature (Surdas, Raskhan, Bihari Lal).</span>
                            <span class="lang-hi"><strong>ब्रजभाषा:</strong> शौरसेनी अपभ्रंश से विकसित। क्षेत्र: मथुरा, आगरा, अलीगढ़, हाथरस, फिरोजाबाद, एटा, मैनपुरी, बरेली, बदायूं। सूरदास, रसखान, बिहारी की कालजयी काव्य भाषा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Khari Boli / Kauravi (खड़ी बोली):</strong> Spoken in Meerut, Saharanpur, Muzaffarnagar, Shamli, Baghpat, Ghaziabad. Progenitor of Modern Standard Hindi and Urdu; pioneered in verse by <strong>Amir Khusrau</strong> and in prose by <strong>Bharatendu Harishchandra</strong>.</span>
                            <span class="lang-hi"><strong>खड़ी बोली (कौरवी):</strong> मेरठ, सहारनपुर, मुजफ्फरनगर, शामली, बागपत, गाजियाबाद। आधुनिक मानक हिंदी व उर्दू की जननी; अमीर खुसरो व भारतेन्दु द्वारा समृद्ध।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Brajbhasha and Khari Boli (Kauravi) both originate from Shauraseni Apabhramsha. Meerut is the heartland of standard Khari Boli!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ब्रजभाषा और खड़ी बोली दोनों का विकास शौरसेनी अपभ्रंश से हुआ है। मेरठ मानक खड़ी बोली का केंद्र है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Western Hindi Branch: Kannauji & Bundeli Dialects -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-halved" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Kannauji &amp; Bundeli</span>
                    <span class="lang-hi">3. पश्चिमी हिंदी: कन्नौजी एवं बुंदेली</span>
                </h4>
                <span class="mindmap-node-tag">Shauraseni Apabhramsha</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-map-pin"></i>
                        <span class="lang-en">Kannauji (कन्नौजी) &amp; Bundeli (बुंदेली)</span>
                        <span class="lang-hi">कन्नौजी एवं बुंदेली का भाषाई भूगोल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kannauji (कन्नौजी):</strong> Spoken in Kannauj, Farrukhabad, Etawah, Auraiya, Kanpur Dehat, and Hardoi; transitional dialect between Braj and Awadhi.</span>
                            <span class="lang-hi"><strong>कन्नौजी:</strong> कन्नौज, फर्रुखाबाद, इटावा, औरैया, कानपुर देहात व हरदोई; ब्रजभाषा व अवधी की संक्रमणकालीन बोली।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bundeli (बुंदेली):</strong> Spoken across Bundelkhand: Jhansi, Jalaun, Lalitpur, Hamirpur, Mahoba, Banda, and Chitrakoot. Rich in heroic folk poetry, immortalized by <strong>Jagnik's Alha-Khand</strong> and poet Isuri's Phag.</span>
                            <span class="lang-hi"><strong>बुंदेली:</strong> बुंदेलखंड के 7 जिलों (झांसी, जालौन, ललितपुर, हमीरपुर, महोबा, बांदा, चित्रकूट) में बोली जाती है। <strong>जगनिक के आल्हा-खंड</strong> व ईसुरी की फाग की भाषा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kannauji is spoken in Farrukhabad and Kannauj. Bundeli is the dialect of Jhansi and Banda, famous for Alha-Khand!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कन्नौजी फर्रुखाबाद व कन्नौज में बोली जाती है। बुंदेली झांसी व बांदा की बोली है, जो आल्हा-खंड हेतु प्रसिद्ध है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Eastern Hindi Branch (Ardhamagadhi Apabhramsha): Awadhi & Bagheli -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-feather-pointed" style="color: #d97706;"></i>
                    <span class="lang-en">4. Eastern Hindi: Awadhi &amp; Bagheli</span>
                    <span class="lang-hi">4. पूर्वी हिंदी: अवधी एवं बघेली</span>
                </h4>
                <span class="mindmap-node-tag">Ardhamagadhi Apabhramsha</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-book-open"></i>
                        <span class="lang-en">Awadhi (अवधी) Geographical &amp; Literary Domain</span>
                        <span class="lang-hi">अवधी का क्षेत्र एवं साहित्यिक वैभव</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Awadhi Extent:</strong> Originates from Ardhamagadhi Apabhramsha. Spoken across Central &amp; East-Central UP: <strong>Ayodhya, Lucknow, Prayagraj, Pratapgarh, Sultanpur, Raebareli, Barabanki, Unnao, Fatehpur, Bahraich, Gonda, Shravasti, Amethi</strong>.</span>
                            <span class="lang-hi"><strong>अवधी का विस्तार:</strong> अर्धमागधी अपभ्रंश से उद्भव। क्षेत्र: <strong>अयोध्या, लखनऊ, प्रयागराज, प्रतापगढ़, सुल्तानपुर, रायबरेली, बाराबंकी, उन्नाव, फतेहपुर, बहराइच, गोंडा, श्रावस्ती, अमेठी</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Monumental Epics in Awadhi:</strong> <em>Ramcharitmanas</em> (Goswami Tulsidas, 1574 CE), <em>Padmavat</em> (Malik Muhammad Jayasi, 1540 CE), <em>Chandayan</em> (Mulla Daud, 1379 CE - first Awadhi Sufi poem), <em>Mrigavati</em> (Kutuban).</span>
                            <span class="lang-hi"><strong>अवधी के अमर महाकाव्य:</strong> <em>रामचरितमानस</em> (तुलसीदास, 1574 ई.), <em>पद्मावत</em> (मलिक मुहम्मद जायसी, 1540 ई.), <em>चंदायन</em> (मुल्ला दाऊद, 1379 ई. - प्रथम अवधी सूफी काव्य)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bagheli (बघेली):</strong> Spoken along southern border districts of Mirzapur, Sonbhadra, and southern Prayagraj touching MP.</span>
                            <span class="lang-hi"><strong>बघेली:</strong> मिर्जापुर, सोनभद्र व दक्षिणी प्रयागराज के मध्य प्रदेश सीमावर्ती क्षेत्रों में बोली जाती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Awadhi originates from Ardhamagadhi Apabhramsha. Tulsidas wrote Ramcharitmanas and Jayasi wrote Padmavat in Awadhi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> अवधी अर्धमागधी अपभ्रंश से विकसित हुई है। तुलसीदास ने रामचरितमानस और जायसी ने पद्मावत अवधी में ही रचा!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Bihari Hindi Branch (Magadhi Apabhramsha): Bhojpuri Dominance -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-people-group" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Bhojpuri (Bihari Hindi)</span>
                    <span class="lang-hi">5. भोजपुरी (बिहारी हिंदी उपशाखा)</span>
                </h4>
                <span class="mindmap-node-tag">Magadhi Apabhramsha • Most Spoken</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-earth-asia"></i>
                        <span class="lang-en">Bhojpuri Region &amp; Cultural Stature</span>
                        <span class="lang-hi">भोजपुरी का विशाल विस्तार एवं लोक साहित्य</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Origin &amp; Districts:</strong> Derived from Magadhi Apabhramsha. Spoken by the <strong>largest population</strong> among all regional tongues in UP: <strong>Varanasi, Gorakhpur, Ballia, Ghazipur, Deoria, Azamgarh, Mau, Jaunpur, Chandauli, Kushinagar, Maharajganj, Sant Kabir Nagar</strong>.</span>
                            <span class="lang-hi"><strong>उद्भव एवं विस्तार:</strong> मागधी अपभ्रंश से विकसित। उप्र में <strong>सर्वाधिक लोगों द्वारा बोली जाने वाली बोली</strong>: <strong>वाराणसी, गोरखपुर, बलिया, गाजीपुर, देवरिया, आजमगढ़, मऊ, जौनपुर, चंदौली, कुशीनगर, महाराजगंज</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Shakespeare of Bhojpuri:</strong> <strong>Bhikhari Thakur</strong> (creator of <em>Bidesiya</em>, <em>Gabarghichor</em>, <em>Beti Viyog</em>) is revered as the 'Shakespeare of Bhojpuri' and 'Rai Bahadur of folk theatre'.</span>
                            <span class="lang-hi"><strong>भोजपुरी के शेक्सपियर:</strong> <strong>भिखारी ठाकुर</strong> (प्रसिद्ध नाटक <em>बिदेसिया</em>, <em>गबरघिचोर</em>, <em>बेटी वियोग</em> के रचयिता) को 'भोजपुरी का शेक्सपियर' कहा जाता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bhojpuri is spoken by the largest number of people in UP. Bhikhari Thakur (Bidesiya) is hailed as the 'Shakespeare of Bhojpuri'!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सर्वाधिक जनसंख्या द्वारा बोली जाने वाली बोली भोजपुरी है। भिखारी ठाकुर (बिदेसिया नाटक) को 'भोजपुरी का शेक्सपियर' कहा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Language Institutions & Promotional Academies -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-building-columns" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Language Sansthans &amp; Academies</span>
                    <span class="lang-hi">6. राज्य भाषा संस्थान एवं अकादमियां</span>
                </h4>
                <span class="mindmap-node-tag">Hindi • Sanskrit • Urdu • Punjabi</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-university"></i>
                        <span class="lang-en">State Language Academies in Lucknow</span>
                        <span class="lang-hi">लखनऊ स्थित प्रमुख राज्य भाषा अकादमियां</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>UP Hindi Sansthan:</strong> Lucknow (Established 1976 - confers 'Bharat Bharati' Award)</span>
                        <span class="mindmap-chip"><strong>UP Sanskrit Sansthan:</strong> Lucknow (Established 1976 - confers 'Vishwabharti' Award)</span>
                        <span class="mindmap-chip"><strong>UP Urdu Akademi:</strong> Lucknow (Established 1972)</span>
                        <span class="mindmap-chip"><strong>UP Punjabi Akademi:</strong> Lucknow (Established 1999)</span>
                        <span class="mindmap-chip"><strong>UP Sindhi Akademi:</strong> Lucknow (Established 1996)</span>
                        <span class="mindmap-chip"><strong>UP Bhasha Sansthan:</strong> Lucknow (Promotes all Indian languages)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP Hindi Sansthan and UP Sanskrit Sansthan were both established in 1976 in Lucknow. UP Urdu Akademi was set up in 1972!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र हिंदी संस्थान व उप्र संस्कृत संस्थान दोनों 1976 में लखनऊ में स्थापित हुए। उप्र उर्दू अकादमी 1972 में स्थापित हुई!</span>
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
    inject_mindmap('natural-resources', mm_natural_resources)
    inject_mindmap('polity-and-administration', mm_polity)
    inject_mindmap('regional-languages', mm_regional_languages)
