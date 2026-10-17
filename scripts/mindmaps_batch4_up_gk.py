# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 13: Heritage of Uttar Pradesh
# ==============================================================================
mm_heritage = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Heritage of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की ऐतिहासिक एवं सांस्कृतिक धरोहर</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • UNESCO Tangible &amp; Intangible World Heritage • Buddhist Circuit Holy Sites • Harappan &amp; Classical Gupta Temples • Jaunpur Sharqi Architecture • Awadh Nawabi Heritage • Bundelkhand Forts</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • यूनेस्को मूर्त व अमूर्त विश्व धरोहर • बौद्ध सर्किट के पावन स्थल • हड़प्पा व गुप्तकालीन मंदिर • जौनपुर शर्की स्थापत्य • अवध नवाबी धरोहर • बुंदेलखंड के ऐतिहासिक दुर्ग</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-landmark-dome"></i>
            <span class="lang-en">World Heritage Treasures &amp; Monumental Splendors of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की विश्व धरोहर, पुरातात्विक वैभव एवं ऐतिहासिक स्मारक</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: UNESCO Tangible & Intangible Heritage -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-award" style="color: #059669;"></i>
                    <span class="lang-en">1. UNESCO World Heritage</span>
                    <span class="lang-hi">1. यूनेस्को विश्व धरोहर स्थल</span>
                </h4>
                <span class="mindmap-node-tag">3 Tangible • 2 Intangible • 1 Creative City</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-monument"></i>
                        <span class="lang-en">3 Tangible World Heritage Sites (Agra District)</span>
                        <span class="lang-hi">3 मूर्त विश्व धरोहर स्थल (आगरा जिला)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1. Taj Mahal (1983):</strong> Ivory-white marble mausoleum on Yamuna bank built by Shah Jahan (1631–1648); chief architect Ustad Ahmad Lahori.</span>
                            <span class="lang-hi"><strong>1. ताजमहल (1983):</strong> यमुना तट पर शाहजहाँ द्वारा निर्मित श्वेत संगमरमर का मकबरा (1631-1648); मुख्य वास्तुकार उस्ताद अहमद लाहौरी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2. Agra Fort (1983):</strong> Massive red sandstone fortress built by Akbar (1565); contains Jahangiri Mahal, Moti Masjid, and Musamman Burj.</span>
                            <span class="lang-hi"><strong>2. आगरा किला (1983):</strong> अकबर द्वारा 1565 में निर्मित विशाल लाल बलुआ पत्थर दुर्ग; जहांगीरी महल व मुसम्मन बुर्ज युक्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3. Fatehpur Sikri (1986):</strong> Imperial city founded by Akbar (1571); features Buland Darwaza (53.5m), Salim Chishti Tomb, and Panch Mahal.</span>
                            <span class="lang-hi"><strong>3. फतेहपुर सीकरी (1986):</strong> अकबर द्वारा 1571 में बसाई गई राजधानी; बुलंद दरवाजा, सलीम चिश्ती की दरगाह व पंचमहल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hands-holding-circle"></i>
                        <span class="lang-en">Intangible Heritage &amp; Creative City</span>
                        <span class="lang-hi">अमूर्त सांस्कृतिक धरोहर एवं क्रिएटिव सिटी</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Ramlila of Ramnagar:</strong> Inscribed 2008 (Oldest environmental theatre)</span>
                        <span class="mindmap-chip"><strong>Kumbh Mela (Prayagraj):</strong> Inscribed 2017 (World's largest gathering)</span>
                        <span class="mindmap-chip"><strong>Varanasi:</strong> UNESCO Creative City of Music (2015)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 3 UNESCO Tangible Sites (Taj Mahal 1983, Agra Fort 1983, Fatehpur Sikri 1986) all in Agra! Kumbh Mela was inscribed in 2017.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र के तीनों मूर्त यूनेस्को स्थल (ताजमहल 1983, आगरा किला 1983, फतेहपुर सीकरी 1986) आगरा में हैं! कुंभ मेला 2017 में अमूर्त धरोहर बना।</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Buddhist Circuit Heritage Sites -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-dharmachakra" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Buddhist Circuit Heritage</span>
                    <span class="lang-hi">2. बौद्ध सर्किट के पावन स्थल</span>
                </h4>
                <span class="mindmap-node-tag">Cradle of Buddhism (बौद्ध धर्म का पालना)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-place-of-worship"></i>
                        <span class="lang-en">The 6 Major Sacred Buddhist Centers</span>
                        <span class="lang-hi">6 प्रमुख पावन बौद्ध तीर्थ केंद्र</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Sarnath (Varanasi):</strong> First Sermon (Dharmachakra Pravartana) &amp; Ashoka Lion Capital</span>
                        <span class="mindmap-chip"><strong>2. Shravasti:</strong> Max 24 Varshavasa (Rainy Retreats), Jetavana Vihara, Sahet-Mahet</span>
                        <span class="mindmap-chip"><strong>3. Kushinagar:</strong> Mahaparinirvana (483 BCE), Ramabhar Stupa, Reclining Buddha</span>
                        <span class="mindmap-chip"><strong>4. Kapilavastu (Piprahwa):</strong> Childhood palace home; Buddha bone relic caskets</span>
                        <span class="mindmap-chip"><strong>5. Sankisa (Farrukhabad):</strong> Heavenly descent from Tavatimsa; Ashokan Elephant capital</span>
                        <span class="mindmap-chip"><strong>6. Kaushambi:</strong> Ghoshitarama Monastery; visited in 6th &amp; 9th years</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-landmark"></i>
                        <span class="lang-en">Sarnath &amp; Kushinagar Iconic Monuments</span>
                        <span class="lang-hi">सारनाथ एवं कुशीनगर के विशिष्ट स्मारक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sarnath Lion Capital:</strong> Carved from Chunar sandstone; features 4 back-to-back Asiatic lions, 24-spoke Dharma Chakra, horse, bull, elephant, lion. Adopted as India's National Emblem on <strong>26 Jan 1950</strong>.</span>
                            <span class="lang-hi"><strong>सारनाथ सिंह शीर्ष:</strong> चुनार बलुआ पत्थर पर उत्कीर्ण 4 सिंह, 24 तीलियों वाला धर्मचक्र; 26 जनवरी 1950 को राष्ट्रीय प्रतीक अंगीकृत।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Gautama Buddha preached his first sermon at Sarnath (Rishipattana), spent the maximum 24 rainy seasons at Shravasti, and attained Mahaparinirvana at Kushinagar!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> गौतम बुद्ध ने प्रथम उपदेश सारनाथ में दिया, सर्वाधिक 24 वर्षावास श्रावस्ती में बिताए, और महापरिनिर्वाण कुशीनगर में प्राप्त किया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Ancient Harappan & Classical Gupta Temple Heritage -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gopuram" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Ancient &amp; Gupta Temples</span>
                    <span class="lang-hi">3. हड़प्पा सभ्यता एवं गुप्तकालीन मंदिर धरोहर</span>
                </h4>
                <span class="mindmap-node-tag">Alamgirpur • Deogarh • Bhitargaon</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-archaeology"></i>
                        <span class="lang-en">Archaeological Milestones</span>
                        <span class="lang-hi">पुरातात्विक स्थल एवं खोजें</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Alamgirpur &amp; Sinauli:</strong> <em>Alamgirpur (Meerut - Hindon River)</em> is the easternmost outpost of Indus Valley Civilization. <em>Sinauli (Baghpat)</em> revealed Copper Age royal burials, solid-wheel war chariots, and copper antennae swords.</span>
                            <span class="lang-hi"><strong>आलमगीरपुर व सिनौली:</strong> <em>आलमगीरपुर (मेरठ - हिंडन नदी)</em> हड़प्पा सभ्यता का सबसे पूर्वी स्थल है। <em>सिनौली (बागपत)</em> में ताम्रपाषाण कालीन युद्ध रथ व शाही ताबूत मिले।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dashavatara Temple (Deogarh, Lalitpur):</strong> North India's earliest surviving Panchayatana stone temple (~500 CE). First curvilinear Shikhara in Indian architecture; famous for <em>Sheshashayi Vishnu</em> and <em>Gajendra Moksha</em> panels.</span>
                            <span class="lang-hi"><strong>दशावतार मंदिर (देवगढ़, ललितपुर):</strong> उत्तर भारत का प्राचीनतम सुरक्षित पंचायतन प्रस्तर मंदिर (~500 ई.); शिखर का प्रथम प्रयोग; शेषशायी विष्णु फलक।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bhitargaon Temple (Kanpur):</strong> India's oldest surviving complete all-brick temple (5th century CE) featuring a true semicircular arch and terracotta relief carvings.</span>
                            <span class="lang-hi"><strong>भीतरगांव मंदिर (कानपुर):</strong> भारत का सबसे प्राचीन सुरक्षित संपूर्ण ईंट मंदिर (5वीं सदी); मेहराब व टेराकोटा शिल्प युक्त।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Alamgirpur (Hindon) is IVC's eastern boundary. Deogarh is the oldest stone Panchayatana temple and Bhitargaon is the oldest brick temple!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> आलमगीरपुर (हिंडन) हड़प्पा की पूर्वी सीमा है। देवगढ़ प्राचीनतम प्रस्तर पंचायतन मंदिर व भीतरगांव प्राचीनतम ईंट मंदिर है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Medieval Sharqi Architectural Splendors (Jaunpur) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-archway" style="color: #d97706;"></i>
                    <span class="lang-en">4. Jaunpur Sharqi Heritage</span>
                    <span class="lang-hi">4. जौनपुर शर्की वास्तुकला ('शीराज़-ए-हिन्द')</span>
                </h4>
                <span class="mindmap-node-tag">Atala Masjid • Propylon Gate</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-mosque"></i>
                        <span class="lang-en">Key Sharqi Monuments</span>
                        <span class="lang-hi">प्रमुख शर्की स्मारक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Atala Masjid (1408):</strong> Built by Sultan Ibrahim Shah Sharqi on foundation laid by Firuz Shah Tughlaq. Masterpiece of the Jaunpur style; features a monumental sloping propylon gateway that hides the central dome; completely devoid of minarets.</span>
                            <span class="lang-hi"><strong>अटाला मस्जिद (1408):</strong> सुल्तान इब्राहिम शाह शर्की द्वारा निर्मित; विशाल ढलवां तोरण द्वार (प्रोपाइलॉन); पारंपरिक मीनारों का पूर्ण अभाव।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jhanjhari, Lal Darwaza &amp; Shahi Bridge:</strong> <em>Jhanjhari Masjid (1430)</em>; <em>Lal Darwaza (1450, Queen Bibi Raji)</em>; <em>Shahi Pul (Akbari Bridge, 1568)</em> built by Munim Khan across Gomti with 16 stone arches and pavilions.</span>
                            <span class="lang-hi"><strong>झंझरी, लाल दरवाजा व शाही पुल:</strong> <em>झंझरी मस्जिद</em>; <em>लाल दरवाजा</em> (रानी बीबी राजी); <em>शाही पुल (1568)</em> गोमती नदी पर 16 मेहराबों वाला पत्थर का ऐतिहासिक पुल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Atala Masjid in Jaunpur has no minarets and is celebrated for its sloping propylon screen. Jaunpur was called <em>'Shiraz-e-Hind'</em>!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> जौनपुर की अटाला मस्जिद मीनारविहीन है। शर्की काल में विद्या व कला के केंद्र होने के कारण जौनपुर को <em>'शीराज़-ए-हिन्द'</em> कहा गया!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Awadh Nawabi Heritage (Lucknow) -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-building-columns" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Awadh Nawabi Heritage</span>
                    <span class="lang-hi">5. अवध नवाबी धरोहर (लखनऊ)</span>
                </h4>
                <span class="mindmap-node-tag">Bara Imambara • Rumi Darwaza</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-landmark"></i>
                        <span class="lang-en">Nawabi Architectural Landmarks</span>
                        <span class="lang-hi">नवाबी काल के प्रमुख स्मारक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bara Imambara (Asafi Imambara, 1784):</strong> Built by Nawab Asaf-ud-Daula as a famine relief project; designed by architect <strong>Kifayatullah</strong>. The central vaulted hall (50m long) is built of Lakhori bricks without any pillars or steel beams. Houses the famous <strong>Bhulbhulaiya</strong> (labyrinth).</span>
                            <span class="lang-hi"><strong>बड़ा इमामबाड़ा (आसफी इमामबाड़ा, 1784):</strong> नवाब आसफउद्दौला द्वारा अकाल राहत हेतु निर्मित; वास्तुकार <strong>किफायतउल्लाह</strong>। केंद्रीय हॉल (50 मी.) बिना किसी खंभे के टिका है; ऊपरी तल पर <strong>भूलभुलैया</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rumi Darwaza (1784):</strong> 60-ft high ornamental gateway modeled on the <em>Sublime Porte</em> of Constantinople (Istanbul); adorned with Awadh's twin fish emblem.</span>
                            <span class="lang-hi"><strong>रूमी दरवाजा (1784):</strong> 60 फीट ऊंचा विशाल प्रवेश द्वार; इस्तांबुल के 'बाब-ए-हुमायूँ' की तर्ज पर निर्मित; अवध के मछली राजचिह्न से अलंकृत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chhota Imambara &amp; British Residency:</strong> <em>Chhota Imambara (1838, Muhammad Ali Shah)</em> famous for golden dome and chandeliers; <em>British Residency</em>, epicenter of the heroic 1857 Siege of Lucknow.</span>
                            <span class="lang-hi"><strong>छोटा इमामबाड़ा व रेजीडेंसी:</strong> <em>छोटा इमामबाड़ा (1838)</em> सुनहरे गुंबद व झूमरों युक्त; <em>ब्रिटिश रेजीडेंसी</em> 1857 की क्रांति का प्रमुख युद्ध स्थल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bara Imambara was designed by Kifayatullah in 1784 without pillars using Lakhori bricks. Rumi Darwaza stands 60 feet tall!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बड़ा इमामबाड़ा 1784 में किफायतीउल्लाह द्वारा बिना खंभों के बनाया गया। रूमी दरवाजा 60 फीट ऊंचा है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Bundelkhand Forts & Ancient Hill Fortresses -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-chess-rook" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Bundelkhand Fortresses</span>
                    <span class="lang-hi">6. बुंदेलखंड के ऐतिहासिक गिरि दुर्ग</span>
                </h4>
                <span class="mindmap-node-tag">Kalinjar • Jhansi • Chunar</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield"></i>
                        <span class="lang-en">Impregnable Citadels of UP</span>
                        <span class="lang-hi">अभेद्य ऐतिहासिक किले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kalinjar Fort (Banda):</strong> Perched on an isolated Vindhyan hill; built by Chandela rulers; houses the 7th-century rock-cut <strong>Nilkanth Mahadev Temple</strong>. Afghan emperor <strong>Sher Shah Suri died here in 1545</strong> when a cannon shell rebounded during his siege.</span>
                            <span class="lang-hi"><strong>कालिंजर दुर्ग (बांदा):</strong> चंदेल शासकों द्वारा निर्मित अजेय दुर्ग; शैलकृत <strong>नीलकंठ महादेव मंदिर</strong>। 1545 में शेरशाह सूरी की मृत्यु इसी दुर्ग के घेरे में उक्का तोप का गोला फटने से हुई।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jhansi Fort (1613):</strong> Built on Bangira hill by Orchha ruler <strong>Bir Singh Deo</strong>; contains Karak Bijli cannon, Shiva temple, and the high rampart from which Rani Lakshmibai made her legendary horse leap during the 1858 siege.</span>
                            <span class="lang-hi"><strong>झांसी का किला (1613):</strong> ओरछा नरेश <strong>वीर सिंह देव</strong> द्वारा बंगिरा पहाड़ी पर निर्मित; कड़क बिजली तोप तथा रानी लक्ष्मीबाई के अदम्य शौर्य का गवाह।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chunar Fort (Mirzapur):</strong> Overlooking Ganga river cliff; linked to King Vikramaditya, Bhartrihari samadhi, Babur, Sher Shah Suri, and Warren Hastings.</span>
                            <span class="lang-hi"><strong>चुनार दुर्ग (मिर्जापुर):</strong> गंगा तट पर स्थित; विक्रमादित्य, राजा भर्तृहरि, शेरशाह सूरी व वारेन हेस्टिंग्स से संबंधित।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sher Shah Suri died at Kalinjar Fort (Banda) in 1545. Jhansi Fort was constructed by Bir Singh Deo in 1613!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> 1545 में शेरशाह सूरी की मृत्यु कालिंजर दुर्ग (बांदा) में हुई थी। झांसी किले का निर्माण 1613 में वीर सिंह देव ने कराया था!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 14: Industry of Uttar Pradesh
# ==============================================================================
mm_industry = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Industry of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के उद्योग एवं विनिर्माण क्षेत्र</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Traditional Agro-Industries (Sugar 1903, Cotton/Kanpur) • Central PSUs &amp; Defense Hubs • Mineral &amp; Chemical Industries (Cement, Glass, HINDALCO) • Specialized Craft Clusters &amp; GI Tags • Industrial Development Authorities • Investment Parks</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • पारंपरिक कृषि उद्योग (चीनी 1903, सूती वस्त्र/कानपुर) • केंद्रीय उपक्रम व रक्षा इकाइयां • खनिज व रसायन उद्योग (सीमेंट, कांच, हिंडाल्को) • विशिष्ट शिल्प क्लस्टर व जीआई टैग • औद्योगिक विकास प्राधिकरण • मेगा निवेश पार्क</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-industry"></i>
            <span class="lang-en">Manufacturing Powerhouse, Industrial Clusters &amp; Public Undertakings</span>
            <span class="lang-hi">उत्तर प्रदेश का विनिर्माण परिदृश्य, औद्योगिक क्लस्टर एवं प्रमुख उद्यम</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Traditional Agro-Based Industries -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-wheat-awn" style="color: #059669;"></i>
                    <span class="lang-en">1. Agro-Based Industries</span>
                    <span class="lang-hi">1. प्रमुख कृषि-आधारित उद्योग</span>
                </h4>
                <span class="mindmap-node-tag">Sugar (1903 Pratappur) • Cotton Textile</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cubes-stacked"></i>
                        <span class="lang-en">Sugar Industry (चीनी उद्योग)</span>
                        <span class="lang-hi">चीनी उद्योग एवं ऐतिहासिक पृष्ठभूमि</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Modern Sugar Mill:</strong> India's first modern sugar mill was established in <strong>1903 at Pratappur (Deoria)</strong>, Uttar Pradesh.</span>
                            <span class="lang-hi"><strong>प्रथम आधुनिक चीनी मिल:</strong> भारत की पहली आधुनिक चीनी मिल <strong>1903 में प्रतापपुर (देवरिया)</strong> में स्थापित की गई थी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sugar Bowl &amp; Production:</strong> UP is the leading sugar producing state; Muzaffarnagar is known as the <em>'Sugar Bowl'</em> with Asia's largest jaggery (Gur) trading market. Over 120 sugar mills operate across Meerut, Muzaffarnagar, Bijnor, and Lakhimpur Kheri.</span>
                            <span class="lang-hi"><strong>चीनी का कटोरा:</strong> उप्र देश का शीर्ष चीनी उत्पादक है; मुजफ्फरनगर को 'चीनी का कटोरा' कहा जाता है (एशिया की सबसे बड़ी गुड़ मंडी)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shirt"></i>
                        <span class="lang-en">Cotton Textile Industry (सूती वस्त्र उद्योग)</span>
                        <span class="lang-hi">सूती वस्त्र उद्योग एवं 'उत्तर भारत का मैनचेस्टर'</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Manchester of North India:</strong> <strong>Kanpur</strong> is universally hailed as the <em>'Manchester of North India' (उत्तर भारत का मैनचेस्टर)</em>; first mill (Elgin Mills) established in 1862. Other textile centers: Varanasi, Mau, Meerut, Tanda.</span>
                            <span class="lang-hi"><strong>उत्तर भारत का मैनचेस्टर:</strong> <strong>कानपुर</strong> को 'उत्तर भारत का मैनचेस्टर' कहा जाता है (प्रथम मिल एल्गिन मिल्स 1862)। अन्य केंद्र: वाराणसी, मऊ, मेरठ, टांडा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> India's first sugar mill was set up at Pratappur (Deoria) in 1903. Kanpur is called the 'Manchester of North India'!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> भारत की पहली चीनी मिल 1903 में प्रतापपुर (देवरिया) में स्थापित हुई थी। कानपुर को 'उत्तर भारत का मैनचेस्टर' कहा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Heavy Public Sector Undertakings & Defense Units -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gear" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Heavy PSUs &amp; Defense Hubs</span>
                    <span class="lang-hi">2. केंद्रीय सार्वजनिक उपक्रम एवं रक्षा उद्योग</span>
                </h4>
                <span class="mindmap-node-tag">BHEL • HAL • BLW • HURL • IOCL</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building"></i>
                        <span class="lang-en">Premier Central Public Sector Undertakings</span>
                        <span class="lang-hi">प्रमुख केंद्रीय सार्वजनिक उपक्रम इकाइयाँ</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>BHEL:</strong> Jagdishpur (Amethi) &amp; Jhansi (Transformers)</span>
                        <span class="mindmap-chip"><strong>HAL:</strong> Lucknow (Avionics), Kanpur (Aircraft), Korwa (Amethi)</span>
                        <span class="mindmap-chip"><strong>BLW / DLW:</strong> Banaras Locomotive Works, Varanasi (Locomotives)</span>
                        <span class="mindmap-chip"><strong>MCF:</strong> Modern Coach Factory, Lalganj (Raebareli - Vande Bharat)</span>
                        <span class="mindmap-chip"><strong>ITI:</strong> Indian Telephone Industries, Naini (Prayagraj) &amp; Mankapur</span>
                        <span class="mindmap-chip"><strong>BEL:</strong> Bharat Electronics Limited, Ghaziabad</span>
                        <span class="mindmap-chip"><strong>IOCL Oil Refinery:</strong> Mathura (1982 - only refinery in UP)</span>
                        <span class="mindmap-chip"><strong>IFFCO Fertilizers:</strong> Phulpur (Prayagraj) &amp; Aonla (Bareilly)</span>
                        <span class="mindmap-chip"><strong>HURL Fertilizer:</strong> Gorakhpur (149.5m world's tallest prilling tower)</span>
                        <span class="mindmap-chip"><strong>AK-203 Rifles:</strong> Indo-Russian Rifles Ltd, Korwa (Amethi)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> BLW is in Varanasi, Modern Coach Factory is in Lalganj (Raebareli), and UP's only oil refinery is at Mathura (IOCL)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बीएलडब्ल्यू वाराणसी में, मॉडर्न कोच फैक्ट्री लालगंज (रायबरेली) में, और उप्र की एकमात्र तेल रिफाइनरी मथुरा (IOCL) में है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Mineral & Chemical-Based Industries -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-flask" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Mineral &amp; Chemical Industries</span>
                    <span class="lang-hi">3. खनिज एवं रसायन आधारित भारी उद्योग</span>
                </h4>
                <span class="mindmap-node-tag">Cement • HINDALCO • Glass • Leather</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trowel-bricks"></i>
                        <span class="lang-en">Cement, Aluminum &amp; Chemical Hubs</span>
                        <span class="lang-hi">सीमेंट, एल्युमीनियम एवं कांच उद्योग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Cement Industry (सीमेंट):</strong> Major clusters in Sonbhadra (Churk, Dalla, Kajrahat using local limestone), Sikandrabad (Bulandshahr), and Jhansi.</span>
                            <span class="lang-hi"><strong>सीमेंट उद्योग:</strong> सोनभद्र (चुर्क, डाला, कजराहाट - स्थानीय चूना पत्थर पर आधारित), सिकंदराबाद (बुलंदशहर) व झांसी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Aluminum Smelter (HINDALCO):</strong> Located at <strong>Renukoot (Sonbhadra)</strong>; utilizes bauxite from Amarkantak/Banda and cheap hydel power from Rihand Dam (Govind Ballabh Pant Sagar).</span>
                            <span class="lang-hi"><strong>हिंडाल्को एल्युमीनियम संयंत्र:</strong> <strong>रेणुकूट (सोनभद्र)</strong> में स्थापित; रिहंद बांध की सस्ती जलविद्युत व अमरकंटक/बांदा के बॉक्साइट पर निर्भर।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Glass &amp; Leather:</strong> <strong>Firozabad ('Suhag Nagari')</strong> is India's bangle &amp; glassware capital; <strong>Kanpur &amp; Agra</strong> form India's premier leather tanning and footwear export hubs.</span>
                            <span class="lang-hi"><strong>कांच व चमड़ा उद्योग:</strong> <strong>फिरोजाबाद ('सुहाग नगरी')</strong> कांच की चूड़ियों का विश्व केंद्र; <strong>कानपुर व आगरा</strong> देश के प्रमुख चमड़ा शोधन व जूता निर्यात केंद्र हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> HINDALCO aluminum plant is at Renukoot (Sonbhadra). Churk and Dalla are famous for cement, and Firozabad for glass bangles!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> हिंडाल्को एल्युमीनियम संयंत्र रेणुकूट (सोनभद्र) में है। चुर्क व डाला सीमेंट हेतु तथा फिरोजाबाद कांच की चूड़ियों हेतु प्रसिद्ध हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Specialized Craft Clusters & GI Tags -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tags" style="color: #d97706;"></i>
                    <span class="lang-en">4. Specialized Craft Clusters</span>
                    <span class="lang-hi">4. विशिष्ट हस्तशिल्प क्लस्टर एवं जीआई टैग</span>
                </h4>
                <span class="mindmap-node-tag">Peetal • Carpet • Attar • Locks</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-scissors"></i>
                        <span class="lang-en">Famous Industrial City Epithets &amp; Products</span>
                        <span class="lang-hi">प्रसिद्ध औद्योगिक उपनाम एवं उत्पाद</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Moradabad:</strong> Brassware &amp; Metalcraft ('Peetal Nagari')</span>
                        <span class="mindmap-chip"><strong>Bhadohi:</strong> Hand-Knotted Woolen Carpets ('Carpet City')</span>
                        <span class="mindmap-chip"><strong>Kannauj:</strong> Natural Perfumes &amp; Rose Water ('Attar Nagari')</span>
                        <span class="mindmap-chip"><strong>Aligarh:</strong> Locks &amp; Brass Hardware ('Tala Nagari')</span>
                        <span class="mindmap-chip"><strong>Meerut:</strong> Sports Goods &amp; Scissors ('Sports City' / कैंची नगर)</span>
                        <span class="mindmap-chip"><strong>Khurja (Bulandshahr):</strong> Ceramic Pottery ('Ceramic City')</span>
                        <span class="mindmap-chip"><strong>Saharanpur:</strong> Carved Wooden Furniture &amp; Screens</span>
                        <span class="mindmap-chip"><strong>Varanasi:</strong> Banarasi Zari Silk Sarees &amp; Wooden Lacquer Toys</span>
                        <span class="mindmap-chip"><strong>Lucknow:</strong> Chikankari &amp; Zardozi Needlework</span>
                        <span class="mindmap-chip"><strong>Gorakhpur:</strong> Terracotta Clay Craft (टेराकोटा)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Moradabad is Brass City, Bhadohi is Carpet City, Kannauj is Perfume City, Aligarh is Lock City, and Meerut is Sports City!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> मुरादाबाद पीतल नगरी, भदोही कालीन नगरी, कन्नौज इत्र नगरी, अलीगढ़ ताला नगरी, और मेरठ कैंची/खेल नगरी है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Industrial Development Authorities (UPSIDA, NOIDA & UPEIDA) -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-city" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Industrial Authorities</span>
                    <span class="lang-hi">5. औद्योगिक विकास प्राधिकरण एवं निगम</span>
                </h4>
                <span class="mindmap-node-tag">UPSIDA (Kanpur) • NOIDA 1976</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building-flag"></i>
                        <span class="lang-en">Statutory Industrial Development Authorities</span>
                        <span class="lang-hi">वैधानिक औद्योगिक विकास प्राधिकरण</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>UPSIDA:</strong> UP State Industrial Dev. Authority (Kanpur HQ)</span>
                        <span class="mindmap-chip"><strong>NOIDA:</strong> New Okhla Industrial Dev. Authority (1976)</span>
                        <span class="mindmap-chip"><strong>Greater Noida:</strong> Greater Noida Industrial Dev. Authority (1991)</span>
                        <span class="mindmap-chip"><strong>GIDA:</strong> Gorakhpur Industrial Development Authority (1989)</span>
                        <span class="mindmap-chip"><strong>SIDA:</strong> Satharia Industrial Dev. Authority (Jaunpur, 1989)</span>
                        <span class="mindmap-chip"><strong>BIDA:</strong> Bundelkhand Industrial Dev. Authority (Jhansi, 2023)</span>
                        <span class="mindmap-chip"><strong>YEIDA:</strong> Yamuna Expressway Industrial Dev. Authority (2001)</span>
                        <span class="mindmap-chip"><strong>UPEIDA:</strong> UP Expressways Industrial Dev. Authority (2007)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> NOIDA was established in 1976. UPSIDA is headquartered in Kanpur. BIDA was established in Jhansi in 2023!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नोएडा 1976 में स्थापित हुआ। यूपीसीडा (UPSIDA) का मुख्यालय कानपुर में है। बीडा (BIDA) 2023 में झांसी में स्थापित हुआ!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Mega Industrial Parks & Electronics Clusters -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-microchip" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Mega Industrial Parks</span>
                    <span class="lang-hi">6. मेगा औद्योगिक पार्क एवं इलेक्ट्रॉनिक्स क्लस्टर</span>
                </h4>
                <span class="mindmap-node-tag">PM MITRA • Mobile Manufacturing Hub</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-microchip"></i>
                        <span class="lang-en">Next-Gen Industrial Megaprojects</span>
                        <span class="lang-hi">आधुनिक औद्योगिक मेगा परियोजनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Noida-Greater Noida Electronics Hub:</strong> Manufactures over 60% of all mobile phones in India (Samsung World's largest mobile factory in Noida, Dixon, Oppo).</span>
                            <span class="lang-hi"><strong>नोएडा इलेक्ट्रॉनिक्स हब:</strong> भारत के 60% से अधिक मोबाइल फोन का विनिर्माण (सैमसंग की विश्व की सबसे बड़ी मोबाइल फैक्ट्री नोएडा में)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>PM MITRA Textile Park:</strong> 1,000-acre mega integrated textile and apparel park spanning Lucknow and Hardoi districts.</span>
                            <span class="lang-hi"><strong>पीएम मित्र टेक्सटाइल पार्क:</strong> लखनऊ-हरदोई में 1,000 एकड़ में फैला एकीकृत मेगा वस्त्र पार्क।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mega Leather Park:</strong> Set up at Ramaipur (Kanpur) across 235 acres with modern zero-liquid-discharge CETP facilities.</span>
                            <span class="lang-hi"><strong>मेगा लेदर पार्क:</strong> रमईपुर (कानपुर) में 235 एकड़ में स्थापित आधुनिक चमड़ा क्लस्टर।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Samsung's largest mobile manufacturing unit is located in Noida. The PM MITRA Mega Textile Park spans across Lucknow and Hardoi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सैमसंग की सबसे बड़ी मोबाइल विनिर्माण इकाई नोएडा में है। पीएम मित्र मेगा टेक्सटाइल पार्क लखनऊ व हरदोई में स्थित है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 15: Literature of Uttar Pradesh
# ==============================================================================
mm_literature = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Literature of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश का साहित्य, कालजयी रचनाकार एवं संस्थाएं</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Ancient Sanskrit Epics (Valmiki &amp; Vyasa) • Medieval Bhakti Confluence (Kabir, Tulsi, Sur, Jayasi) • Father of Modern Hindi (Bharatendu) • Upanyas Samrat Premchand &amp; Chhayavad • Urdu Ghazal Masters • Literary Academies</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • प्राचीन संस्कृत महाकाव्य (वाल्मीकि व व्यास) • मध्यकालीन भक्ति संगम (कबीर, तुलसी, सूर, जायसी) • आधुनिक हिंदी के जनक (भारतेन्दु) • उपन्यास सम्राट प्रेमचंद व छायावाद • उर्दू गजल उस्ताद • प्रमुख साहित्यिक संस्थाएं</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-book-open"></i>
            <span class="lang-en">Literary Cradle of Hindi, Sanskrit &amp; Urdu in Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश: संस्कृत, हिंदी एवं उर्दू साहित्य की उद्गम स्थली</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Ancient & Classical Sanskrit Heritage -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-scroll" style="color: #059669;"></i>
                    <span class="lang-en">1. Ancient Sanskrit Heritage</span>
                    <span class="lang-hi">1. प्राचीन संस्कृत महाकाव्य एवं ऋषि परंपरा</span>
                </h4>
                <span class="mindmap-node-tag">Valmiki • Vyasa • Patanjali • Banabhatta</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-feather-pointed"></i>
                        <span class="lang-en">Epic Sages &amp; Sacred Writing Grounds</span>
                        <span class="lang-hi">महाकाव्यकार ऋषि एवं पावन रचना स्थल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Maharishi Valmiki (Adi Kavi):</strong> Authored the original Sanskrit <strong>Ramayana</strong> at his hermitage in <strong>Brahmavarta (Bithoor, Kanpur)</strong> on the bank of River Ganga; ashram where Sita gave birth to Luv and Kush.</span>
                            <span class="lang-hi"><strong>महर्षि वाल्मीकि (आदि कवि):</strong> गंगा तट पर <strong>ब्रह्मावर्त (बिठूर, कानपुर)</strong> स्थित आश्रम में संस्कृत <strong>रामायण</strong> की रचना की; लव-कुश की जन्मस्थली।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Maharishi Ved Vyasa:</strong> Compiled the four Vedas and authored the <strong>Mahabharata</strong> and 18 Puranas in Uttar Pradesh (sacred land of Naimisharanya, Sitapur).</span>
                            <span class="lang-hi"><strong>महर्षि वेदव्यास:</strong> वेदों का संकलन तथा <strong>महाभारत</strong> व 18 पुराणों की रचना उप्र की पावन भूमि (नैमिषारण्य) पर की।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sage Patanjali &amp; Banabhatta:</strong> <em>Patanjali</em> (born in Gonarda/Gonda) authored <em>Mahabhashya</em> (Sanskrit grammar) and <em>Yoga Sutras</em>. <em>Banabhatta</em> (court of King Harshavardhana in Kannauj) composed <em>Harshacharita</em> and <em>Kadambari</em> (world's earliest novel).</span>
                            <span class="lang-hi"><strong>पतंजलि व बाणभट्ट:</strong> <em>पतंजलि</em> (जन्म: गोनार्द/गोंडा) ने <em>महाभाष्य</em> व <em>योगसूत्र</em> रचे। <em>बाणभट्ट</em> (हर्षवर्धन के दरबारी, कन्नौज) ने <em>हर्षचरित</em> व <em>कादंबरी</em> (विश्व का प्रथम उपन्यास) की रचना की।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Maharishi Valmiki composed Ramayana at Bithoor (Kanpur). Sage Patanjali belonged to Gonda (Gonarda), and Banabhatta authored Kadambari at Kannauj!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> महर्षि वाल्मीकि ने बिठूर (कानपुर) में रामायण की रचना की। पतंजलि गोंडा से संबंधित थे तथा बाणभट्ट ने कन्नौज में कादंबरी लिखी!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Medieval Bhakti & Sufi Literature -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hands-praying" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Medieval Bhakti &amp; Sufi Lore</span>
                    <span class="lang-hi">2. मध्यकालीन भक्ति एवं सूफी साहित्य</span>
                </h4>
                <span class="mindmap-node-tag">Kabir • Tulsi • Sur • Jayasi • Khusrau</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-book-bookmark"></i>
                        <span class="lang-en">Immortal Poets &amp; Masterpieces</span>
                        <span class="lang-hi">कालजयी संत कवि एवं रचनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sant Kabir Das (1398–1518):</strong> Born at Lahartara (Varanasi), died at Maghar (Sant Kabir Nagar). Wrote in <em>Sadhukkadi / Panchmel Khichdi</em>; verses collected in <strong>Bijak</strong> (comprising Sakhi, Sabad, Ramaini).</span>
                            <span class="lang-hi"><strong>संत कबीरदास:</strong> जन्म लहरतारा (वाराणसी), महाप्रयाण मगहर (संत कबीर नगर)। सधुक्कड़ी भाषा; रचना संकलन <strong>बीजक</strong> (साखी, सबद, रमैनी)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Goswami Tulsidas (1532–1623):</strong> Born at Rajapur (Chitrakoot); composed the monumental epic <strong>Ramcharitmanas</strong> (in Awadhi in 1574 CE), <em>Vinaya Patrika</em>, <em>Kavitavali</em>, <em>Dohavali</em>, <em>Gitavali</em>, and <em>Hanuman Chalisa</em>.</span>
                            <span class="lang-hi"><strong>गोस्वामी तुलसीदास:</strong> जन्म राजापुर (चित्रकूट); अवधी भाषा में अमर महाकाव्य <strong>रामचरितमानस</strong> (1574 ई.), <em>विनय पत्रिका</em>, <em>कवितावली</em>, <em>दोहावली</em> व <em>हनुमान चालीसा</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Surdas (Brajbhasha):</strong> Born at Sihi/Runkata (Agra/Mathura); disciple of Vallabhacharya; composed <strong>Sursagar</strong>, <em>Sur Saravali</em>, and <em>Sahitya Lahari</em>.</span>
                            <span class="lang-hi"><strong>सूरदास:</strong> जन्म सीही/रुनकता (आगरा/मथुरा); वल्लभाचार्य के शिष्य; ब्रजभाषा में <strong>सूरसागर</strong>, <em>सूर सारावली</em> व <em>साहित्य लहरी</em> रची।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jayasi &amp; Amir Khusrau:</strong> <em>Malik Muhammad Jayasi</em> (Jayas, Amethi) wrote the Sufi epic <strong>Padmavat</strong> (1540 CE in Awadhi). <em>Amir Khusrau</em> (Patiali, Kasganj) pioneered Khari Boli, Pahelis, Mukarnis, and Qawwali.</span>
                            <span class="lang-hi"><strong>जायसी व अमीर खुसरो:</strong> <em>मलिक मुहम्मद जायसी</em> (जायस, अमेठी) ने अवधी में <strong>पद्मावत</strong> (1540 ई.) रचा। <em>अमीर खुसरो</em> (पटियाली, कासगंज) खड़ी बोली व पहेलियों के जनक।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Tulsidas was born in Rajapur (Chitrakoot) and wrote Ramcharitmanas in Awadhi. Kabir died at Maghar. Jayasi wrote Padmavat in 1540 CE!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> तुलसीदास का जन्म राजापुर (चित्रकूट) में हुआ (अवधी में रामचरितमानस)। कबीर का निर्वाण मगहर में हुआ। जायसी ने 1540 में पद्मावत की रचना की!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Modern Hindi Renaissance: Bharatendu Era -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-pen-nib" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Bharatendu &amp; Hindi Renaissance</span>
                    <span class="lang-hi">3. भारतेन्दु युग एवं आधुनिक हिंदी नवजागरण</span>
                </h4>
                <span class="mindmap-node-tag">Father of Modern Hindi Literature</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-newspaper"></i>
                        <span class="lang-en">Bharatendu Harishchandra (1850–1885, Varanasi)</span>
                        <span class="lang-hi">भारतेन्दु हरिश्चंद्र एवं आधुनिक गद्य का सूत्रपात</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Father of Modern Hindi:</strong> Revolutionized Hindi by establishing Khari Boli as standard literary prose. Proclaimed: <em>'Nij bhasha unnati ahe, sab unnati ko mool'</em>.</span>
                            <span class="lang-hi"><strong>आधुनिक हिंदी के पितामह:</strong> खड़ी बोली को आधुनिक गद्य की भाषा बनाया। उद्घोष: <em>'निज भाषा उन्नति अहै, सब उन्नति को मूल'</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Masterpiece Plays &amp; Journals:</strong> Authored political satire plays <em>Bharat Durdasha</em> (1880), <em>Andher Nagari</em> (1881), <em>Satya Harishchandra</em>. Founded landmark literary magazines: <strong>Kavi Vachan Sudha</strong> (1868) and <em>Harishchandra Magazine</em>.</span>
                            <span class="lang-hi"><strong>प्रमुख नाटक व पत्रिकाएं:</strong> अमर व्यंग्य नाटक <em>भारत दुर्दशा</em> (1880), <em>अंधेर नगरी</em> (1881), <em>सत्य हरिश्चंद्र</em>। प्रसिद्ध पत्रिकाएं: <strong>कवि वचन सुधा</strong> (1868) व <em>हरिश्चंद्र मैगजीन</em>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bharatendu Harishchandra was born in Varanasi and is hailed as the Father of Modern Hindi Prose. Kavi Vachan Sudha was launched in 1868!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> भारतेन्दु हरिश्चंद्र (वाराणसी) को आधुनिक हिंदी गद्य का जनक कहा जाता है। कवि वचन सुधा पत्रिका 1868 में निकली!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Upanyas Samrat Premchand & Chhayavad Era -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-book" style="color: #d97706;"></i>
                    <span class="lang-en">4. Premchand &amp; Chhayavad</span>
                    <span class="lang-hi">4. उपन्यास सम्राट प्रेमचंद एवं छायावाद युग</span>
                </h4>
                <span class="mindmap-node-tag">Godan • Kamayani • Yama</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-book-open-reader"></i>
                        <span class="lang-en">Munshi Premchand (1880–1936, Lamhi, Varanasi)</span>
                        <span class="lang-hi">मुंशी प्रेमचंद (उपन्यास सम्राट)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Novels &amp; Social Realism:</strong> Real name Dhanpat Rai (wrote in Urdu as Nawab Rai). Monumental novels: <strong>Godan</strong> (1936 - epic of Indian peasantry), <em>Gaban</em>, <em>Sevasadan</em>, <em>Karmabhumi</em>, <em>Rangbhumi</em>, <em>Nirmala</em>. Short stories: <em>Kafan</em>, <em>Poos ki Raat</em>, <em>Idgah</em>, <em>Panch Parmeshwar</em>. Founded magazine <strong>Hans (हंस)</strong>.</span>
                            <span class="lang-hi"><strong>अमर उपन्यास व कहानियां:</strong> मूल नाम धनपत राय (उर्दू में नवाब राय)। <strong>गोदान</strong> (1936 - भारतीय कृषक जीवन का महाकाव्य), <em>गबन</em>, <em>सेवासदन</em>, <em>निर्मला</em>। कहानियां: <em>कफन</em>, <em>पूस की रात</em>, <em>ईदगाह</em>। <strong>हंस</strong> पत्रिका निकाली।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cloud-sun"></i>
                        <span class="lang-en">Chhayavad Four Pillars in UP</span>
                        <span class="lang-hi">छायावाद के चार स्तंभ (उप्र केंद्र)</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Jaishankar Prasad (Varanasi):</strong> Kamayani (1936 epic), Skandagupta, Dhruvasvamini</span>
                        <span class="mindmap-chip"><strong>Mahadevi Varma (Farrukhabad/Prayagraj):</strong> 'Modern Meera', Yama (Jnanpith 1982), Nihar</span>
                        <span class="mindmap-chip"><strong>Suryakant Tripathi 'Nirala' (Prayagraj):</strong> Ram ki Shakti Puja, Saroj Smriti, Parimal</span>
                        <span class="mindmap-chip"><strong>Sumitranandan Pant (Prayagraj):</strong> Chidambara (First Hindi Jnanpith Award 1968)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Premchand was born in Lamhi (Varanasi). Sumitranandan Pant won the 1st Hindi Jnanpith for Chidambara (1968). Mahadevi Varma won Jnanpith for Yama (1982)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> प्रेमचंद का जन्म लमही (वाराणसी) में हुआ। सुमित्रानंदन पंत को चिदंबरा (1968) पर प्रथम हिंदी ज्ञानपीठ तथा महादेवी वर्मा को यामा (1982) पर ज्ञानपीठ मिला!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Urdu Literature & Ganga-Jamuni Poetry -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-feather" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Urdu Poetry &amp; Ghazal Masters</span>
                    <span class="lang-hi">5. उर्दू शायरी एवं कालजयी गजलकार</span>
                </h4>
                <span class="mindmap-node-tag">Mirza Ghalib • Firaq Gorakhpuri</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-quote-left"></i>
                        <span class="lang-en">Legends Born and Nurtured in UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के महान उर्दू शायर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mirza Asadullah Khan 'Ghalib' (1797–1869):</strong> Born at <strong>Kala Mahal in Agra</strong>; greatest Urdu-Persian poet of all time; redefined the Urdu Ghazal.</span>
                            <span class="lang-hi"><strong>मिर्जा असदुल्लाह खां 'गालिब':</strong> जन्म <strong>काला महल, आगरा</strong> में हुआ (1797); उर्दू-फारसी शायरी के अमर हस्ताक्षर जिन्होंने गजल को दर्शन दिया।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mir Taqi Mir &amp; Josh Malihabadi:</strong> <em>Mir Taqi Mir</em> born in Agra ('Khuda-e-Sukhan'); <em>Josh Malihabadi</em> (Shabbir Hasan Khan, born Malihabad, Lucknow) hailed as 'Shair-e-Inquilab'.</span>
                            <span class="lang-hi"><strong>मीर तकी मीर व जोश मलीहाबादी:</strong> <em>मीर तकी मीर</em> (जन्म: आगरा, 'खुदा-ए-सुखन'); <em>जोश मलीहाबादी</em> (मलीहाबाद, लखनऊ, 'शायर-ए-इंकलाब')।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Firaq Gorakhpuri (Raghupati Sahay, 1896–1982):</strong> Born in Gorakhpur, taught English at Allahabad University; received the <strong>first Jnanpith Award for Urdu (1969)</strong> for his poetry collection <strong>Gul-e-Naghma (गुल-ए-नग़्मा)</strong>.</span>
                            <span class="lang-hi"><strong>फिराक गोरखपुरी (रघुपति सहाय):</strong> जन्म गोरखपुर; इलाहाबाद वि.वि. में प्रोफेसर; 1969 में काव्य संग्रह <strong>गुल-ए-नग़्मा</strong> हेतु उर्दू का <strong>प्रथम ज्ञानपीठ पुरस्कार</strong> प्राप्त किया।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Mirza Ghalib was born in Agra. Firaq Gorakhpuri received the first Jnanpith Award for Urdu literature in 1969 for Gul-e-Naghma!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> मिर्जा गालिब का जन्म आगरा में हुआ था। फिराक गोरखपुरी को 1969 में गुल-ए-नग़्मा हेतु उर्दू का प्रथम ज्ञानपीठ पुरस्कार मिला था!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Literary Institutions & Academies of UP -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-building-columns" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Literary Academies &amp; Sansthans</span>
                    <span class="lang-hi">6. प्रमुख साहित्यिक संस्थाएं एवं अकादमी</span>
                </h4>
                <span class="mindmap-node-tag">Nagari Pracharini 1893 • Hindi Sansthan</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-university"></i>
                        <span class="lang-en">Key Institutions &amp; Headquarters</span>
                        <span class="lang-hi">प्रमुख साहित्यिक संस्थान एवं स्थापना वर्ष</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Nagari Pracharini Sabha:</strong> Varanasi (Established 1893 by Babu Shyam Sundar Das)</span>
                        <span class="mindmap-chip"><strong>Hindi Sahitya Sammelan:</strong> Prayagraj (1910, 1st President Purushottam Das Tandon)</span>
                        <span class="mindmap-chip"><strong>Hindustani Academy:</strong> Prayagraj (Established 1927)</span>
                        <span class="mindmap-chip"><strong>UP Hindi Sansthan:</strong> Lucknow (Est. 1976 - confers Bharat Bharati Samman)</span>
                        <span class="mindmap-chip"><strong>UP Sanskrit Sansthan:</strong> Lucknow (Est. 1976 - confers Vishwabharti Samman)</span>
                        <span class="mindmap-chip"><strong>UP Urdu Akademi:</strong> Lucknow (Established 1972)</span>
                        <span class="mindmap-chip"><strong>UP Sindhi &amp; Punjabi Akademi:</strong> Lucknow</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Nagari Pracharini Sabha was established in 1893 in Varanasi. Hindi Sahitya Sammelan was founded in 1910 in Prayagraj!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नागरी प्रचारिणी सभा की स्थापना 1893 में वाराणसी में हुई थी। हिंदी साहित्य सम्मेलन 1910 में प्रयागराज में स्थापित हुआ!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 16: Mines and Minerals of Uttar Pradesh
# ==============================================================================
mm_mines = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Mines &amp; Minerals of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के खनिज संसाधन, खनन नीति एवं प्रमुख खदानें</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Mineral Policy 1998 &amp; 12 Mineral Districts • Energy Minerals (Coal/Singrauli, Uranium/Lalitpur) • Metallic Minerals (Gold, Copper, Bauxite) • Glass Sand &amp; Limestone Wealth • National Diaspore Rank 1 • Mine Mitra &amp; Green Mining</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • प्रथम खनन नीति 1998 व 12 खनिज जिले • ऊर्जा खनिज (कोयला/सिंगरौली, यूरेनियम/ललितपुर) • धात्विक खनिज (सोना, तांबा, बॉक्साइट) • कांच बालू व चूना पत्थर • डायस्पोर में देश में प्रथम • माइन मित्र व पर्यावरण संरक्षण</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-gem"></i>
            <span class="lang-en">Mineral Distribution, Southern Plateaus &amp; Mining Framework of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की खनिज संपदा, दक्षिणी पठारी क्षेत्र एवं खनन प्रशासन</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Mining Administration, Legal Framework & Policies -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-scale-balanced" style="color: #059669;"></i>
                    <span class="lang-en">1. Mining Policy &amp; 12 Districts</span>
                    <span class="lang-hi">1. खनन नीति एवं 12 खनिज बाहुल्य जिले</span>
                </h4>
                <span class="mindmap-node-tag">First Policy: Dec 1998 • Industry Status</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-file-contract"></i>
                        <span class="lang-en">State Policy &amp; Administrative Setup</span>
                        <span class="lang-hi">राज्य खनन नीति एवं प्रशासनिक ढांचा</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Directorate of Geology &amp; Mining:</strong> Established in <strong>1955 at Lucknow</strong> for mineral survey, exploration, and lease administration. UP State Mineral Development Corporation (UPSMDC) set up in 1974.</span>
                            <span class="lang-hi"><strong>भूतत्व एवं खनिकर्म निदेशालय:</strong> खनिज सर्वेक्षण व पट्टा प्रबंधन हेतु <strong>1955 में लखनऊ</strong> में स्थापित। उप्र राज्य खनिज विकास निगम 1974 में बना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>First Mineral Policy (December 1998):</strong> Declared mining as an <strong>'Industry'</strong>; identified <strong>12 districts as 'Mineral Rich Districts'</strong> located across Bundelkhand, Vindhyan plateaus, and northern hills.</span>
                            <span class="lang-hi"><strong>प्रथम खनन नीति (दिसंबर 1998):</strong> खनन को <strong>उद्योग का दर्जा</strong> दिया गया तथा <strong>12 जिलों को खनिज बाहुल्य क्षेत्र</strong> घोषित किया गया।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-map-pin"></i>
                        <span class="lang-en">The 12 Mineral Rich Districts of UP</span>
                        <span class="lang-hi">12 खनिज बाहुल्य जिले</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip">1. Sonbhadra (सोनभद्र)</span>
                        <span class="mindmap-chip">2. Mirzapur (मिर्जापुर)</span>
                        <span class="mindmap-chip">3. Prayagraj (प्रयागराज)</span>
                        <span class="mindmap-chip">4. Banda (बांदा)</span>
                        <span class="mindmap-chip">5. Hamirpur (हमीरपुर)</span>
                        <span class="mindmap-chip">6. Mahoba (महोबा)</span>
                        <span class="mindmap-chip">7. Jalaun (जालौन)</span>
                        <span class="mindmap-chip">8. Jhansi (झांसी)</span>
                        <span class="mindmap-chip">9. Lalitpur (ललितपुर)</span>
                        <span class="mindmap-chip">10. Chitrakoot (चित्रकूट)</span>
                        <span class="mindmap-chip">11. Kaushambi (कौशाम्बी)</span>
                        <span class="mindmap-chip">12. Saharanpur (सहारनपुर)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP declared its First Mineral Policy in December 1998 giving mining industry status and notifying 12 mineral-rich districts!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र की प्रथम खनिज नीति दिसंबर 1998 में घोषित हुई, जिसमें खनन को उद्योग का दर्जा देकर 12 खनिज बाहुल्य जिले घोषित किए गए!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Energy Minerals: Coal & Uranium -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-fire-flame-simple" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Energy Minerals: Coal &amp; Uranium</span>
                    <span class="lang-hi">2. ऊर्जा खनिज: कोयला एवं यूरेनियम</span>
                </h4>
                <span class="mindmap-node-tag">Coal: Sonbhadra • Uranium: Lalitpur</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-gem"></i>
                        <span class="lang-en">Singrauli Coalfield &amp; Power Pit-Heads</span>
                        <span class="lang-hi">सिंगरौली कोयला क्षेत्र एवं ऊर्जा राजधानी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Coal (Singrauli, Sonbhadra):</strong> Mined from Gondwana rock strata in Singrauli (Sonbhadra) by Northern Coalfields Limited (NCL); directly feeds giant pit-head thermal stations (Singrauli Super Thermal, Obra, Anpara), earning Sonbhadra the title <strong>'Energy Capital of India'</strong>.</span>
                            <span class="lang-hi"><strong>कोयला (सिंगरौली, सोनभद्र):</strong> सोनभद्र की गोंडवाना चट्टानों से NCL द्वारा खनन; यह ओबरा, अनपरा व सिंगरौली ताप विद्युत गृहों को ईंधन देता है, जिससे सोनभद्र <strong>'ऊर्जा राजधानी'</strong> कहलाता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-atom"></i>
                        <span class="lang-en">Radioactive Minerals (Uranium)</span>
                        <span class="lang-hi">रेडियोधर्मी खनिज (यूरेनियम)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Uranium (Lalitpur District):</strong> Found exclusively in <strong>Lalitpur district</strong> in limited veins within granitic pegmatites. Highly strategic atomic mineral.</span>
                            <span class="lang-hi"><strong>यूरेनियम (ललितपुर जिला):</strong> उप्र में यूरेनियम के सीमित भंडार केवल और केवल <strong>ललितपुर जिले</strong> में पाए जाते हैं (अत्यंत महत्वपूर्ण परमाणु खनिज)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Coal is found only in Singrauli (Sonbhadra), and Uranium is found exclusively in Lalitpur district. Absolute top-frequency questions!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में कोयला केवल सिंगरौली (सोनभद्र) में और यूरेनियम केवल ललितपुर जिले में मिलता है। परीक्षा का अनिवार्य प्रश्न!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Metallic Minerals: Gold, Copper, Bauxite & Iron Ore -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-coins" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Metallic Minerals</span>
                    <span class="lang-hi">3. धात्विक खनिज: सोना, तांबा, बॉक्साइट व लोहा</span>
                </h4>
                <span class="mindmap-node-tag">Sonbhadra Gold • Sonrai Copper</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-ring"></i>
                        <span class="lang-en">Precious &amp; Base Metals Distribution</span>
                        <span class="lang-hi">कीमती एवं औद्योगिक धातुओं का वितरण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Gold (सोना):</strong> Primary gold reserves discovered in <strong>Sonbhadra</strong> (Sonpahadi and Hardi areas); alluvial placer gold particles also panned from sands of <strong>Sharda and Ramganga rivers</strong>.</span>
                            <span class="lang-hi"><strong>सोना:</strong> प्राथमिक भंडार <strong>सोनभद्र</strong> (सोनपहाड़ी व हरदी क्षेत्र) तथा ललितपुर (विक्रमपुर); इसके अतिरिक्त <strong>शारदा व रामगंगा नदियों की बालू</strong> में प्लेसर गोल्ड कण पाए जाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Copper (तांबा):</strong> Concentrated in <strong>Sonrai area of Lalitpur district</strong> within Bijawar sedimentary formations.</span>
                            <span class="lang-hi"><strong>तांबा:</strong> <strong>ललितपुर जिले के सोनराई क्षेत्र</strong> की बिजावर चट्टानों में तांबे के भंडार पाए जाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bauxite (बॉक्साइट - Aluminum Ore):</strong> Mined in <strong>Banda (Rajapur)</strong>, <strong>Chitrakoot</strong>, and Chandauli; feeds HINDALCO aluminum smelter at Renukoot.</span>
                            <span class="lang-hi"><strong>बॉक्साइट (एल्युमीनियम अयस्क):</strong> <strong>बांदा (राजापुर)</strong>, <strong>चित्रकूट</strong> व चंदौली में खनन; रेणुकूट के हिंडाल्को संयंत्र को आपूर्ति।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Iron Ore (लौह अयस्क):</strong> Low-grade hematite deposits found in <strong>Lalitpur district</strong>.</span>
                            <span class="lang-hi"><strong>लौह अयस्क:</strong> हेमेटाइट श्रेणी के लौह भंडार <strong>ललितपुर जिले</strong> में पाए जाते हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Copper is found in Sonrai (Lalitpur). Gold reserves are in Sonpahadi (Sonbhadra). Bauxite is mined in Banda and Chitrakoot!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> तांबा सोनराई (ललितपुर) में मिलता है। सोना सोनपहाड़ी (सोनभद्र) में तथा बॉक्साइट बांदा व चित्रकूट में पाया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Non-Metallic & Industrial Minerals: Glass Sand & Limestone -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cubes" style="color: #d97706;"></i>
                    <span class="lang-en">4. Glass Sand &amp; Limestone</span>
                    <span class="lang-hi">4. कांच बालू, चूना पत्थर एवं डोलोमाइट</span>
                </h4>
                <span class="mindmap-node-tag">Glass Sand Rank 2 • Sonbhadra Lime</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-volcano"></i>
                        <span class="lang-en">Glass Sand / Silica Sand (कांच बालू)</span>
                        <span class="lang-hi">कांच बालू (सिलिका सैंड)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Standing:</strong> UP ranks <strong>#2 in India</strong> for glass sand production; high-purity silica sand quarried from Vindhyan quartzite in <strong>Shankargarh &amp; Lohgara (Prayagraj)</strong>, <strong>Bargadh (Chitrakoot)</strong>, and riverbeds of Ganga &amp; Yamuna; supplies Firozabad glass industry and Naini glass works.</span>
                            <span class="lang-hi"><strong>राष्ट्रीय स्थान:</strong> कांच बालू उत्पादन में उप्र का देश में <strong>दूसरा स्थान</strong>; <strong>शंकरगढ़ व लोहगरा (प्रयागराज)</strong> तथा <strong>बरगढ़ (चित्रकूट)</strong> मुख्य स्रोत; फिरोजाबाद व नैनी के कांच उद्योगों की जीवनरेखा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trowel-bricks"></i>
                        <span class="lang-en">Limestone &amp; Dolomite (चूना पत्थर व डोलोमाइट)</span>
                        <span class="lang-hi">चूना पत्थर एवं डोलोमाइट</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Limestone (Sonbhadra &amp; Mirzapur):</strong> High-grade flux and cement grade limestone mined at <strong>Gurma, Kanach, Kajrahat, and Bapuhari (Sonbhadra)</strong>; directly feeds Churk and Dalla cement plants.</span>
                            <span class="lang-hi"><strong>चूना पत्थर (सोनभद्र व मिर्जापुर):</strong> <strong>गुरमा, कनाच, कजराहाट व बापुहारी (सोनभद्र)</strong> में सीमेंट व इस्पात ग्रेड चूना पत्थर; चुर्क व डाला सीमेंट कारखानों को आपूर्ति।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dolomite (Kajrahat, Sonbhadra):</strong> Used in steel blast furnace lining and refractory bricks; quarried in Kajrahat (Sonbhadra) and Banda.</span>
                            <span class="lang-hi"><strong>डोलोमाइट:</strong> इस्पात कारखानों की भट्ठियों हेतु <strong>कजराहाट (सोनभद्र)</strong> व बांदा में खनन।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Shankargarh (Prayagraj) is India's leading glass sand hub. Gurma and Kajrahat (Sonbhadra) are famous for limestone and dolomite!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> शंकरगढ़ (प्रयागराज) कांच बालू का प्रमुख केंद्र है। गुरमा व कजराहाट (सोनभद्र) चूना पत्थर व डोलोमाइट हेतु प्रसिद्ध हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Specialty Minerals: Diaspore & Pyrophyllite (Rank 1) -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-trophy" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Diaspore Rank 1 &amp; Bundelkhand</span>
                    <span class="lang-hi">5. डायस्पोर (देश में प्रथम) एवं विशिष्ट खनिज</span>
                </h4>
                <span class="mindmap-node-tag">National Leader in Diaspore</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-medal"></i>
                        <span class="lang-en">Diaspore &amp; Pyrophyllite Dominance</span>
                        <span class="lang-hi">डायस्पोर एवं पायरोफिलाइट में एकाधिकार</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Diaspore (Rank 1 in India):</strong> UP holds over <strong>80% of India's total Diaspore reserves</strong>, concentrated in <strong>Jhansi, Lalitpur, Mahoba, and Hamirpur</strong>; vital raw material for high-alumina refractory bricks, ceramics, and spark plugs.</span>
                            <span class="lang-hi"><strong>डायस्पोर (देश में प्रथम):</strong> देश के <strong>80% से अधिक भंडार उप्र में</strong>; <strong>झांसी, ललितपुर, महोबा व हमीरपुर</strong> में स्थित; उच्च तापरोधी ईंटों व स्पार्क प्लग निर्माण में प्रयुक्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Pyrophyllite &amp; Gypsum:</strong> Mined in Jhansi and Hamirpur (used in ceramics, insecticides, talc powder, and slate pencils); Gypsum found in Jhansi and Hamirpur.</span>
                            <span class="lang-hi"><strong>पायरोफिलाइट व जिप्सम:</strong> झांसी व हमीरपुर (कीटनाशक, सिरेमिक व टेलकम पाउडर); जिप्सम भी झांसी व हमीरपुर में।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rock Phosphate:</strong> Found in <strong>Lalitpur district</strong>; essential for phosphatic fertilizer manufacturing.</span>
                            <span class="lang-hi"><strong>रॉक फॉस्फेट:</strong> <strong>ललितपुर जिले</strong> में भंडार; रासायनिक उर्वरक उद्योग हेतु कच्चा माल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Uttar Pradesh ranks #1 in India in Diaspore reserves (Jhansi, Lalitpur, Mahoba). Rock Phosphate is mined in Lalitpur!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> डायस्पोर के उत्पादन/भंडार में उप्र देश में प्रथम (झांसी, ललितपुर, महोबा) है। रॉक फॉस्फेट ललितपुर में मिलता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Minor Minerals, Dimensional Stones & Mine Mitra -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-laptop-medical" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Dimensional Stone &amp; Mine Mitra</span>
                    <span class="lang-hi">6. इमारती पत्थर एवं 'माइन मित्र' पोर्टल</span>
                </h4>
                <span class="mindmap-node-tag">Chunar Sandstone • Digital Mining</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-monument"></i>
                        <span class="lang-en">Building Stones &amp; River Sand</span>
                        <span class="lang-hi">इमारती पत्थर एवं नदी बालू/मौरंग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chunar Sandstone (Mirzapur):</strong> Buff and mottled pink sandstone used from Ashokan pillars and Sarnath lion capital to Agra monuments and modern grand memorials. Holds GI tag (Chunar Glazed Pottery &amp; Sandstone).</span>
                            <span class="lang-hi"><strong>चुनार बलुआ पत्थर (मिर्जापुर):</strong> मौर्यकालीन अशोक स्तंभों से लेकर आधुनिक स्मारकों तक प्रयुक्त गुलाबी व चित्तीदार बलुआ पत्थर। जीआई टैग प्राप्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Granite (Dimensional Stone):</strong> Red, pink and black granite dimensional blocks quarried in Jhansi, Lalitpur, Banda, and Mahoba.</span>
                            <span class="lang-hi"><strong>ग्रेनाइट:</strong> झांसी, ललितपुर, बांदा व महोबा से इमारती लाल व काला ग्रेनाइट।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-computer"></i>
                        <span class="lang-en">Mine Mitra Digital Platform</span>
                        <span class="lang-hi">'माइन मित्र' डिजिटल प्रणाली</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Mine Mitra Portal:</strong> e-transit pass (ISTP) &amp; e-rawanna system</span>
                        <span class="mindmap-chip"><strong>Mining Surveillance:</strong> AI-enabled drone surveillance to curb illegal sand mining</span>
                        <span class="mindmap-chip"><strong>DMF (District Mineral Foundation):</strong> High welfare spending in mining regions</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Chunar (Mirzapur) sandstone has been the building block of Indian monuments since Mauryan times. Mine Mitra is UP's mining portal!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> चुनार (मिर्जापुर) का बलुआ पत्थर मौर्य काल से स्मारकों का आधार रहा है। 'माइन मित्र' उप्र का डिजिटल खनन पोर्टल है!</span>
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
    inject_mindmap('heritage', mm_heritage)
    inject_mindmap('industry', mm_industry)
    inject_mindmap('literature', mm_literature)
    inject_mindmap('mines-and-minerals', mm_mines)
