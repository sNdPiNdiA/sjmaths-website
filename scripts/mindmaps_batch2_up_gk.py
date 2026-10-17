# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 5: Climate of Uttar Pradesh
# ==============================================================================
mm_climate = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Climate &amp; Weather of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की जलवायु, ऋतु चक्र एवं मानसूनी प्रतिमान</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Köppen Classification (Cwg) • Summer Dynamics &amp; Loo • SW Monsoon &amp; Bay of Bengal Branch • Extreme Rainfall Disparities • Winter Mechanics &amp; Western Disturbances • 9 Climatic Sub-Zones</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • कोपेन वर्गीकरण (Cwg) • ग्रीष्म ऋतु एवं 'लू' • द.-प. मानसून व बंगाल की खाड़ी शाखा • वर्षा की चरम विषमताएं • शीत ऋतु एवं पश्चिमी विक्षोभ • 9 जलवायु उप-क्षेत्र</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-cloud-sun-rain"></i>
            <span class="lang-en">Subtropical Monsoon Climate &amp; Seasonal Cycles of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की उपोष्णकटिबंधीय मानसूनी जलवायु एवं मौसमी चक्र</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Scientific Classification & General Characteristics -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-temperature-half" style="color: #059669;"></i>
                    <span class="lang-en">1. Scientific Classification</span>
                    <span class="lang-hi">1. जलवायु का वैज्ञानिक वर्गीकरण</span>
                </h4>
                <span class="mindmap-node-tag">Köppen Cwg • Subtropical Monsoon</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-compass"></i>
                        <span class="lang-en">Typological Classifications</span>
                        <span class="lang-hi">प्रमुख वैज्ञानिक वर्गीकरण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Köppen System (Cwg):</strong> Predominant climate is <strong>Cwg</strong> (Humid Subtropical with dry winter and hot summer). Southern Bundelkhand and Vindhyan plateaus touch <em>Aw</em> (Tropical Savanna with dry winter).</span>
                            <span class="lang-hi"><strong>कोपेन प्रणाली (Cwg):</strong> प्रमुख रूप से <strong>Cwg</strong> (शुष्क शीत ऋतु वाली मानसूनी उपोष्ण जलवायु)। दक्षिणी बुंदेलखंड व विंध्य क्षेत्र <em>Aw</em> (उष्णकटिबंधीय सवाना) को छूता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Thornthwaite System:</strong> Classified as <em>CB'w</em> (Sub-humid Subtropical with dry winter). General nature: Continental inland climate marked by extreme seasonality (hot summers, chilly winters).</span>
                            <span class="lang-hi"><strong>थॉर्नथवेट प्रणाली:</strong> उप-आर्द्र उपोष्ण कटिबंधीय जलवायु (<em>CB'w</em>)। महाद्वीपीय अंतर्देशीय स्थिति के कारण ग्रीष्म व शीत ऋतु के तापमान में भारी अंतर।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Under Köppen's classification, the climate of the Gangetic plain of Uttar Pradesh is designated as <strong>Cwg</strong>!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कोपेन के जलवायु वर्गीकरण के अनुसार उत्तर प्रदेश के मैदानी भाग की जलवायु को <strong>Cwg</strong> कोड से दर्शाया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Summer Season (Greeshma Ritu) & Heat Dynamics -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-sun" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Summer Season (Greeshma)</span>
                    <span class="lang-hi">2. ग्रीष्म ऋतु एवं तापमान प्रतिमान</span>
                </h4>
                <span class="mindmap-node-tag">March to June • 'Loo' Winds</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-fire-flame-curved"></i>
                        <span class="lang-en">Temperature Extremes &amp; Hottest Districts</span>
                        <span class="lang-hi">चरम तापमान एवं सर्वाधिक गर्म जिले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hottest Month:</strong> May and June record the highest temperatures, frequently soaring between 45°C and 48°C.</span>
                            <span class="lang-hi"><strong>सर्वाधिक गर्म माह:</strong> मई और जून सबसे गर्म महीने होते हैं; पारा 45°C से 48°C तक पहुँच जाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Hottest &amp; Coolest Districts:</strong> <strong>Agra and Jhansi</strong> record the highest average summer temperatures due to proximity to Thar Desert and black soil plateau. <strong>Bareilly</strong> records the lowest average summer temperatures in the plains.</span>
                            <span class="lang-hi"><strong>सर्वाधिक गर्म व ठंडा जिला:</strong> <strong>आगरा और झांसी</strong> में ग्रीष्म ऋतु में सर्वाधिक औसत तापमान रहता है। मैदानी भागों में <strong>बरेली</strong> में सबसे कम औसत तापमान रहता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>'Loo' Phenomena:</strong> Extremely hot, desiccating westerly winds blowing across the plains during May-June with speeds of 30-40 km/h, causing severe heatwaves and dust storms (Andhi).</span>
                            <span class="lang-hi"><strong>'लू' पवनें:</strong> मई-जून में पश्चिम दिशा से चलने वाली अत्यंत शुष्क एवं गर्म हवाएं जो भीषण लू व धूल भरी आंधियां लाती हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Agra and Jhansi record the highest summer temperatures in UP, while Bareilly experiences the lowest summer temperatures!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में ग्रीष्म ऋतु में सर्वाधिक औसत तापमान आगरा व झांसी में, जबकि सबसे कम औसत तापमान बरेली में दर्ज किया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Rainy Season (Varsha Ritu) & Monsoon Mechanics -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-cloud-showers-heavy" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Rainy Season &amp; Monsoon</span>
                    <span class="lang-hi">3. वर्षा ऋतु एवं मानसूनी क्रियाविधि</span>
                </h4>
                <span class="mindmap-node-tag">Mid-June to Oct • 85-90% Annual Rain</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-wind"></i>
                        <span class="lang-en">Monsoon Origin &amp; The 'Purva' Current</span>
                        <span class="lang-hi">मानसून की उत्पत्ति एवं 'पुरवा' धारा</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bay of Bengal Branch (Purva):</strong> Enters UP from the east/southeast through Bihar around 15–20 June. Known locally as <strong>'Purva' (पुरवा)</strong>; delivers ~85% to 90% of the state's total annual precipitation.</span>
                            <span class="lang-hi"><strong>बंगाल की खाड़ी शाखा ('पुरवा'):</strong> 15-20 जून के आसपास बिहार के रास्ते पूर्वी उप्र में प्रवेश करती है; इसे स्थानीय भाषा में <strong>'पुरवा'</strong> कहते हैं; यह राज्य की 85-90% वर्षा कराती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Arabian Sea Branch:</strong> Contributes only ~10-15% of rainfall, mostly active in southern Bundelkhand and western borders.</span>
                            <span class="lang-hi"><strong>अरब सागर शाखा:</strong> केवल 10-15% वर्षा प्रदान करती है, जिसका प्रभाव मुख्यतः दक्षिणी बुंदेलखंड व पश्चिमी सीमा पर होता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-chart-line-down"></i>
                        <span class="lang-en">Spatial Rainfall Gradient</span>
                        <span class="lang-hi">वर्षा का स्थानिक ढाल</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>East to West Decrease:</strong> Rainfall progressively decreases from East to West and from North (Tarai) to South (Plain/Plateau). Eastern UP averages ~112 cm, whereas Western UP receives only ~65 cm.</span>
                            <span class="lang-hi"><strong>पूर्व से पश्चिम की ओर ह्रास:</strong> पूर्व से पश्चिम तथा उत्तर (तराई) से दक्षिण की ओर जाने पर वर्षा की मात्रा लगातार घटती जाती है (पूर्वी उप्र: ~112 सेमी, पश्चिमी उप्र: ~65 सेमी)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> The Bay of Bengal branch of the SW monsoon is called 'Purva' in UP. Over 85% of state rainfall occurs between July and September!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> द.-प. मानसून की बंगाल की खाड़ी शाखा को उप्र में 'पुरवा' कहा जाता है। 85% से अधिक वर्षा जुलाई से सितंबर के बीच होती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Extreme Rainfall Disparities: Gorakhpur vs Mathura -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-droplet" style="color: #d97706;"></i>
                    <span class="lang-en">4. Rainfall Extremes</span>
                    <span class="lang-hi">4. वर्षा की चरम विषमता: गोरखपुर बनाम मथुरा</span>
                </h4>
                <span class="mindmap-node-tag">Highest: 184.7 cm • Lowest: 54.4 cm</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-scale-unbalanced"></i>
                        <span class="lang-en">Extreme Rainfall Contrast</span>
                        <span class="lang-hi">चरम वर्षा तुलना</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Highest Rainfall District:</strong> Gorakhpur (184.7 cm)</span>
                        <span class="mindmap-chip"><strong>Rainiest Days:</strong> Gorakhpur (~56 rainy days)</span>
                        <span class="mindmap-chip"><strong>Lowest Rainfall District:</strong> Mathura (54.4 cm)</span>
                        <span class="mindmap-chip"><strong>Fewest Rainy Days:</strong> Mathura (~32 rainy days)</span>
                        <span class="mindmap-chip"><strong>State Average Rainfall:</strong> ~95 cm to 102 cm</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-triangle-exclamation"></i>
                        <span class="lang-en">Hydrological Consequences</span>
                        <span class="lang-hi">जलवैज्ञानिक परिणाम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tarai &amp; Eastern Floods:</strong> Heavy orographic precipitation along Himalayan foothills makes Gorakhpur, Deoria, Kushinagar, and Siddharthnagar prone to catastrophic seasonal floods (Rapti &amp; Ghaghara rivers).</span>
                            <span class="lang-hi"><strong>तराई व पूर्वी बाढ़:</strong> हिमालय की तलहटी में भारी वर्षा से गोरखपुर, देवरिया व कुशीनगर राप्ती व घाघरा की विनाशकारी बाढ़ से प्रभावित होते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>South-Western Droughts:</strong> Mathura, Agra, and Bundelkhand suffer acute soil moisture deficits and frequent droughts requiring artificial tube-well and canal networks.</span>
                            <span class="lang-hi"><strong>दक्षिण-पश्चिमी सूखा:</strong> मथुरा, आगरा व बुंदेलखंड में अल्प वर्षा से सूखे की स्थिति बनती है जहाँ नलकूप व नहरें जीवनरेखा हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Gorakhpur receives the highest rainfall (184.7 cm, 56 days) and Mathura receives the lowest (54.4 cm, 32 days). Absolute exam essential!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सर्वाधिक वर्षा गोरखपुर (184.7 सेमी, 56 दिन) में और न्यूनतम वर्षा मथुरा (54.4 सेमी, 32 दिन) में होती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Winter Season (Sheet Ritu) & Western Disturbances -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-snowflake" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Winter &amp; Western Disturbances</span>
                    <span class="lang-hi">5. शीत ऋतु एवं पश्चिमी विक्षोभ</span>
                </h4>
                <span class="mindmap-node-tag">November to February • Rabi Rain</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-icicles"></i>
                        <span class="lang-en">Thermal Profile &amp; Cold Wave</span>
                        <span class="lang-hi">तापमान एवं शीत लहर</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Coldest Month:</strong> <strong>January</strong> is the coldest month across UP. Mean minimum temperatures range from 3°C to 10°C. Temperature drops sharply from South to North.</span>
                            <span class="lang-hi"><strong>सर्वाधिक ठंडा माह:</strong> <strong>जनवरी</strong> सबसे ठंडा महीना है। न्यूनतम तापमान 3°C से 10°C तक गिर जाता है। दक्षिण से उत्तर की ओर तापमान घटता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dense Fog (Khora) &amp; Frost (Pala):</strong> Severe radiation fog engulfs Indo-Gangetic plains in Dec-Jan, severely impacting transport and triggering frost damage to mustard and potato crops.</span>
                            <span class="lang-hi"><strong>कोहरा व पाला:</strong> दिसंबर-जनवरी में घना कोहरा छाया रहता है; कभी-कभी पाला (पाला/तुषार) पड़ने से आलू व सरसों की फसल को नुकसान होता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cloud-bolt"></i>
                        <span class="lang-en">Western Disturbances (पश्चिमी विक्षोभ)</span>
                        <span class="lang-hi">पश्चिमी विक्षोभ एवं रबी वर्षा</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mediterranean Origin:</strong> Extratropical cyclones originating over the Mediterranean Sea are steered into North India by the Subtropical Westerly Jet Stream during winter.</span>
                            <span class="lang-hi"><strong>भूमध्यसागरीय उत्पत्ति:</strong> भूमध्य सागर से उठने वाले शीतोष्ण चक्रवात पछुआ जेट स्ट्रीम द्वारा उत्तर भारत में आते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Crucial Rabi Boon:</strong> Delivers 10 cm to 15 cm of light cyclonic showers (known as <em>Mahawat</em> in western UP) in Dec-Jan; acts as a golden boon for standing wheat, gram, and mustard crops.</span>
                            <span class="lang-hi"><strong>रबी हेतु वरदान:</strong> दिसंबर-जनवरी में 10-15 सेमी हल्की वर्षा (माहवट) कराता है; यह गेहूं व सरसों की फसलों के लिए अमृत समान लाभकारी होती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Winter rainfall in UP is caused by Western Disturbances originating from the Mediterranean Sea, highly beneficial for Rabi crops!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में शीतकालीन वर्षा भूमध्य सागर से उत्पन्न होने वाले पश्चिमी विक्षोभों के कारण होती है, जो रबी फसलों (गेहूं) के लिए वरदान है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Comprehensive 9 Agro-Climatic Zones Matrix -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-mountain-sun" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Climatic Zonal Matrix</span>
                    <span class="lang-hi">6. जलवायु उप-क्षेत्र एवं परिस्थितिकी</span>
                </h4>
                <span class="mindmap-node-tag">Tarai • Plains • Plateau</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">3 Broad Natural Climatic Divisions</span>
                        <span class="lang-hi">3 वृहद प्राकृतिक जलवायु विभाजन</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1. Humid &amp; Sub-Humid Tarai Belt:</strong> High humidity, marshy soil, dense forests, 120-180 cm annual rainfall, prone to malaria and floods.</span>
                            <span class="lang-hi"><strong>1. आर्द्र व उप-आर्द्र तराई क्षेत्र:</strong> उच्च आर्द्रता, दलदली मिट्टी, 120-180 सेमी वर्षा, बाढ़ व मलेरिया प्रवण क्षेत्र।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2. Sub-Humid Gangetic Plain:</strong> Transitional climate; Eastern plain receives 100-120 cm rain, Western plain receives 60-80 cm rain with high diurnal thermal range.</span>
                            <span class="lang-hi"><strong>2. उप-आर्द्र मध्य मैदानी क्षेत्र:</strong> संक्रमणकालीन जलवायु; पूर्वी भाग में 100-120 सेमी और पश्चिमी भाग में 60-80 सेमी वर्षा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3. Semi-Arid Bundelkhand &amp; Vindhyan:</strong> High summer heat (often >47°C), low rainfall (70-90 cm), low groundwater table, rocky plateau, severe dry season droughts.</span>
                            <span class="lang-hi"><strong>3. अर्ध-शुष्क बुंदेलखंड व विंध्य पठार:</strong> ग्रीष्म ऋतु में अत्यधिक गर्मी (>47°C), कम वर्षा (70-90 सेमी), निम्न भूजल स्तर व गंभीर सूखा प्रवणता।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP's climate transitions from humid sub-tropical in Tarai to semi-arid in Bundelkhand. Average annual temperature of UP is 25°C to 26°C!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र की जलवायु तराई के आर्द्र उपोष्ण से बुंदेलखंड के अर्ध-शुष्क रूप में बदलती है। राज्य का वार्षिक औसत तापमान 25°C से 26°C है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 6: Culture of Uttar Pradesh
# ==============================================================================
mm_culture = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Culture of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की समग्र संस्कृति एवं विरासत</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Ganga-Jamuni Composite Culture • 5 Cultural Regional Zones • Major Fairs &amp; Spiritual Peaks • Folk Theatre &amp; Performing Arts • Classical Music &amp; Dance Legacy • Tribal Heritage &amp; Traditions</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • गंगा-जमुनी साझा संस्कृति • 5 सांस्कृतिक आंचलिक क्षेत्र • प्रमुख मेले व आध्यात्मिक उत्सव • लोक नाट्य व प्रदर्शन कलाएं • शास्त्रीय संगीत व नृत्य परंपरा • जनजातीय संस्कृति व रीति-रिवाज</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-om"></i>
            <span class="lang-en">Composite Culture &amp; Living Heritage of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश की सामासिक संस्कृति एवं जीवंत सांस्कृतिक धरोहर</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Ganga-Jamuni Tehzeeb & Composite Culture -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hands-praying" style="color: #059669;"></i>
                    <span class="lang-en">1. Ganga-Jamuni Tehzeeb</span>
                    <span class="lang-hi">1. गंगा-जमुनी तहज़ीब एवं सामासिक संस्कृति</span>
                </h4>
                <span class="mindmap-node-tag">Syncretism • Pluralistic Harmony</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-peace"></i>
                        <span class="lang-en">Philosophical Roots &amp; Cultural Confluence</span>
                        <span class="lang-hi">दार्शनिक आधार एवं सांस्कृतिक समन्वय</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ganga-Jamuni Ethos:</strong> Refers to the harmonious blending of Hindu and Islamic cultures nurtured in the fertile plains of Ganga and Yamuna, especially in Awadh, Braj, and Varanasi.</span>
                            <span class="lang-hi"><strong>गंगा-जमुनी संस्कृति:</strong> गंगा और यमुना के दोआब में विकसित हिंदू-मुस्लिम समन्वय; विशेषकर अवध, ब्रज व बनारस की साझा तहज़ीब।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bhakti &amp; Sufi Synthesis:</strong> Cradle of the Bhakti movement (Kabir, Tulsidas, Surdas, Ravidas, Ramananda) and Chishti Sufism (Nizamuddin Auliya born Badaun; Salim Chishti at Sikri; Waris Ali Shah at Deva Sharif).</span>
                            <span class="lang-hi"><strong>भक्ति एवं सूफी समन्वय:</strong> कबीर, तुलसी, सूर, रैदास व रामानंद की भक्ति धारा तथा निजामुद्दीन औलिया (बदायूं), शेख सलीम चिश्ती व वारिस अली शाह की सूफी परंपरा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Hazrat Nizamuddin Auliya was born in Badaun (UP). Amir Khusrau was his foremost disciple and pioneer of Hindavi and Qawwali!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> हजरत निजामुद्दीन औलिया का जन्म बदायूं (उप्र) में हुआ था। अमीर खुसरो उनके प्रिय शिष्य और हिन्दवी व कव्वाली के जनक थे!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: 5 Regional Cultural Zones -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-map-location-dot" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Five Regional Cultural Zones</span>
                    <span class="lang-hi">2. पांच आंचलिक सांस्कृतिक क्षेत्र</span>
                </h4>
                <span class="mindmap-node-tag">Braj • Awadh • Bundelkhand • Purvanchal • Rohilkhand</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cubes"></i>
                        <span class="lang-en">Zonal Characteristics &amp; Dialects</span>
                        <span class="lang-hi">आंचलिक विशेषताएं एवं बोलियाँ</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Braj Region:</strong> Mathura/Agra, Krishna Bhakti, Brajbhasha, Raslila</span>
                        <span class="mindmap-chip"><strong>2. Awadh Region:</strong> Lucknow/Ayodhya, Ram tradition, Awadhi, Nawabi adab</span>
                        <span class="mindmap-chip"><strong>3. Bundelkhand:</strong> Jhansi/Banda, Martial valor, Alha-Udal, Bundeli</span>
                        <span class="mindmap-chip"><strong>4. Purvanchal:</strong> Varanasi/Gorakhpur, Shiva cult, Bhojpuri, Birha &amp; Kajri</span>
                        <span class="mindmap-chip"><strong>5. Rohilkhand &amp; Paschim:</strong> Bareilly/Meerut, Khari Boli, Kauravi</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-masks-theater"></i>
                        <span class="lang-en">Distinct Folk Literature &amp; Folklore</span>
                        <span class="lang-hi">विशिष्ट लोक साहित्य एवं गाथाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Alha-Khand (Bundelkhand):</strong> Composed by court poet <strong>Jagnik</strong> (Mahoba); recounts 52 heroic battles fought by warrior brothers Alha and Udal against Prithviraj Chauhan. Sung in monsoon season in Veera Rasa.</span>
                            <span class="lang-hi"><strong>आल्हा-खंड (बुंदेलखंड):</strong> जगनिक (महोबा) द्वारा रचित; आल्हा-ऊदल के 52 युद्धों का वीर रसपूर्ण वर्णन; वर्षा ऋतु में गाया जाने वाला लोकप्रिय लोककाव्य।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Alha is the most popular heroic folk ballad of Bundelkhand (composed by Jagnik in Mahoba), sung especially during the rainy season!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> आल्हा बुंदेलखंड का सर्वाधिक लोकप्रिय वीर रस का लोकगीत है (रचनाकार: जगनिक, महोबा), जो वर्षा ऋतु में गाया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Major Fairs (Melas) & Festivals Directory -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tent" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Major Fairs &amp; Spiritual Peaks</span>
                    <span class="lang-hi">3. प्रमुख मेले एवं आध्यात्मिक उत्सव</span>
                </h4>
                <span class="mindmap-node-tag">2,250+ Fairs Annually • Mathura #1</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trophy"></i>
                        <span class="lang-en">District Rankings by Number of Fairs</span>
                        <span class="lang-hi">मेलों की संख्या में जिलावार रैंकिंग</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Max Fairs:</strong> Mathura (86 Fairs - Rank 1)</span>
                        <span class="mindmap-chip"><strong>Rank 2:</strong> Kanpur (80 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 3:</strong> Hamirpur (79 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 4:</strong> Jhansi (78 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 5:</strong> Prayagraj (77 Fairs)</span>
                        <span class="mindmap-chip"><strong>Lowest Fairs:</strong> Pilibhit (पीलीभीत - न्यूनतम मेले)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-calendar-star"></i>
                        <span class="lang-en">Iconic Fairs Across UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के विश्वप्रसिद्ध मेले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kumbh &amp; Magh Mela:</strong> Maha Kumbh held every 12 years and Ardha Kumbh every 6 years at Prayagraj Sangam. UNESCO Intangible Cultural Heritage 2017. Annual Magh Mela held in Jan-Feb.</span>
                            <span class="lang-hi"><strong>कुंभ व माघ मेला:</strong> प्रयागराज संगम पर हर 12 वर्ष में महाकुंभ और 6 वर्ष में अर्धकुंभ; 2017 में यूनेस्को अमूर्त सांस्कृतिक धरोहर घोषित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bateshwar Mela (Agra):</strong> Huge animal/camel fair held on Yamuna bank at Bateshwar (101 Shiva temples), revered as 'Mini Pushkar of UP'.</span>
                            <span class="lang-hi"><strong>बटेश्वर मेला (आगरा):</strong> यमुना तट पर 101 शिव मंदिरों वाले बटेश्वर में लगने वाला प्रसिद्ध ऊंट व पशु मेला; 'उप्र का मिनी पुष्कर'।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nauchandi Mela (Meerut):</strong> Communal harmony fair held after Holi; devotees visit Nauchandi Devi temple and Bale Mian Dargah together.</span>
                            <span class="lang-hi"><strong>नौचंदी मेला (मेरठ):</strong> होली के बाद लगने वाला सांप्रदायिक सौहार्द का मेला; नवचंडी देवी मंदिर व बाले मियां की दरगाह पर एक साथ मत्था टेकते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Other Essential Fairs:</strong> <em>Deva Sharif</em> (Barabanki - Waris Ali Shah); <em>Syed Salar</em> (Bahraich); <em>Khichdi Mela</em> (Gorakhpur - Gorakhnath temple); <em>Govind Sahib</em> (Ambedkar Nagar); <em>Shakumbhari Devi</em> (Saharanpur); <em>Dadhikandho</em> (Prayagraj).</span>
                            <span class="lang-hi"><strong>अन्य अनिवार्य मेले:</strong> <em>देवा शरीफ</em> (बाराबंकी); <em>सैयद सालार मसूद गाजी</em> (बहराइच); <em>खिचड़ी मेला</em> (गोरखपुर); <em>गोविंद साहब</em> (अंबेडकर नगर); <em>शाकुंभरी देवी</em> (सहारनपुर)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Mathura hosts the maximum number of fairs (86), while Pilibhit hosts the lowest. Bateshwar (Agra) is the prime cattle fair!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सर्वाधिक मेले मथुरा (86) में और सबसे कम पीलीभीत में लगते हैं। बटेश्वर मेला (आगरा) प्रमुख पशु मेला है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Folk Theatre & Performing Traditions -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-theater-masks" style="color: #d97706;"></i>
                    <span class="lang-en">4. Folk Theatres &amp; Dramas</span>
                    <span class="lang-hi">4. लोक नाट्य एवं अभिनय शैलियाँ</span>
                </h4>
                <span class="mindmap-node-tag">Nautanki • Ramnagar Ramlila</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-drum"></i>
                        <span class="lang-en">Nautanki, Swang &amp; Bhagat</span>
                        <span class="lang-hi">नौटंकी, स्वांग एवं भगत</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nautanki Schools:</strong> <em>Hathras School</em> (initiated by Indraman, classical music dominance, Doha-Chaubola) and <em>Kanpur School</em> (founded by Shri Krishna Pahalwan, dialogue, acting, social themes).</span>
                            <span class="lang-hi"><strong>नौटंकी की शैलियां:</strong> <em>हाथरस शैली</em> (पंडित इंद्रमन द्वारा प्रवर्तित, गायन व शास्त्रीय राग प्रधान) तथा <em>कानपुर शैली</em> (श्रीकृष्ण पहलवान, अभिनय व सामाजिक संवाद प्रधान)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Swang &amp; Bhagat:</strong> Ancient musical open-air folk theatre of Western UP (Agra, Mathura, Aligarh); Bhagat dates back 400+ years.</span>
                            <span class="lang-hi"><strong>स्वांग व भगत:</strong> पश्चिमी उप्र (आगरा, मथुरा) की 400 वर्ष पुरानी संगीतमय नाट्य परंपरा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Hathras School and Kanpur School are the two primary styles of Nautanki in Uttar Pradesh!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> हाथरस और कानपुर शैलियां उत्तर प्रदेश के नौटंकी लोकनाट्य के दो मुख्य घराने/स्कूल हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Classical & Folk Performing Arts -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-guitar" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Classical &amp; Folk Music</span>
                    <span class="lang-hi">5. शास्त्रीय एवं लोक संगीत परंपरा</span>
                </h4>
                <span class="mindmap-node-tag">Kathak • Birha • Kajri • Rasiya</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-music"></i>
                        <span class="lang-en">Regional Folk Songs Matrix</span>
                        <span class="lang-hi">क्षेत्रीय लोकगीतों का वर्गीकरण</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Braj:</strong> Rasiya (रसिया), Hori, Phag, Charkula</span>
                        <span class="mindmap-chip"><strong>Awadh:</strong> Sohar (पुत्र जन्मोत्सव), Nakta, Kawwali</span>
                        <span class="mindmap-chip"><strong>Purvanchal:</strong> Birha (बिरहा - Yadav community), Kajri (Mirzapur monsoon)</span>
                        <span class="mindmap-chip"><strong>Bundelkhand:</strong> Alha (आल्हा), Isuri Faag, Hardaul Geet</span>
                        <span class="mindmap-chip"><strong>Rohilkhand:</strong> Lavani, Ragini (रागिनी)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cloud-rain"></i>
                        <span class="lang-en">Kajri &amp; Birha Distinctive Features</span>
                        <span class="lang-hi">कजरी एवं बिरहा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kajri (Mirzapur/Varanasi):</strong> Female monsoon folk song dedicated to Goddess Vindhyavasini, expressing longing of the separated bride in rainy season.</span>
                            <span class="lang-hi"><strong>कजरी (मिर्जापुर/वाराणसी):</strong> वर्षा ऋतु में गाया जाने वाला विरह व श्रृंगार प्रधान लोकगीत; मां विंध्यवासिनी के जन्मोत्सव से जुड़ा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Birha (Purvanchal):</strong> Most popular Bhojpuri folk genre narrating valorous events, social stories, and heroic sagas.</span>
                            <span class="lang-hi"><strong>बिरहा (पूर्वांचल):</strong> वीर, ऐतिहासिक व समसामयिक घटनाओं पर आधारित पूर्वांचल का सर्वाधिक लोकप्रिय लोकगीत।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kajri originated in Mirzapur, Rasiya belongs to Braj, Birha to Purvanchal, and Sohar is sung on childbirth in Awadh!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कजरी की उत्पत्ति मिर्जापुर में हुई, रसिया ब्रज का, बिरहा पूर्वांचल का, और सोहर अवध में संतान जन्म पर गाया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Tribal Culture & Indigenous Heritage -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-people-group" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Tribal Culture &amp; Heritage</span>
                    <span class="lang-hi">6. जनजातीय संस्कृति एवं लोक परंपरा</span>
                </h4>
                <span class="mindmap-node-tag">Tharu • Buksa • Sahariya • Agariya</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-campground"></i>
                        <span class="lang-en">Major Scheduled Tribes of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश की प्रमुख अनुसूचित जनजातियाँ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tharu Tribe (तराई क्षेत्र):</strong> Largest tribal community of UP (Lakhimpur Kheri, Bahraich, Shravasti, Balrampur). Claim Kirat descent; practice joint family system; observe <strong>Diwali as a day of mourning (शोक पर्व)</strong> offering 'Putla' to ancestors; brew rice beer called <em>Jad (जाड़)</em>; celebrate <em>Bajhar</em> festival.</span>
                            <span class="lang-hi"><strong>थारू जनजाति:</strong> उप्र की सबसे बड़ी जनजाति (लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर)। किरात वंशीय; संयुक्त परिवार प्रथा; <strong>दीपावली को शोक पर्व</strong> के रूप में मनाते हैं; चावल की मदिरा <em>'जाड़'</em> पीते हैं; <em>बझहर</em> त्यौहार मनाते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Buksa / Bhoksa (Bijnor):</strong> Claim Rajput descent (Pawar Rajputs of Patan); worship Chamunda Devi; practice Anuloma/Pratiloma marriages; have their own tribal panchayat headed by a <em>Takht</em>.</span>
                            <span class="lang-hi"><strong>बुक्सा / भोक्सा (बिजनौर):</strong> पटवार राजपूत वंशज मानते हैं; चामुंडा देवी की पूजा करते हैं; इनकी बिरादरी पंचायत का सर्वोच्च अधिकारी <em>'तख्त'</em> कहलाता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sonbhadra &amp; Lalitpur Tribes:</strong> <strong>Sonbhadra</strong> has the highest tribal population (Gond, Kharwar, Baiga, Panika, Agariya - traditional iron smelters, Chero, Parahiya). <strong>Sahariya</strong> tribe resides exclusively in <strong>Lalitpur</strong>.</span>
                            <span class="lang-hi"><strong>सोनभद्र व ललितपुर की जनजातियाँ:</strong> <strong>सोनभद्र</strong> सर्वाधिक जनजाति आबादी वाला जिला (गोंड, खरवार, बैगा, पनिका, अगरिया - लौह प्रगालक, चेरो)। <strong>सहरिया</strong> जनजाति केवल <strong>ललितपुर</strong> जिले में पाई जाती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Tharu tribe celebrates Diwali as a festival of mourning (शोक पर्व). Sahariya tribe is found in Lalitpur. Sonbhadra has the highest tribal population in UP!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> थारू जनजाति दीपावली को शोक पर्व के रूप में मनाती है। सहरिया जनजाति ललितपुर में पाई जाती है। सोनभद्र में सर्वाधिक जनजाति जनसंख्या है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 7: Current Events & Achievements of Uttar Pradesh
# ==============================================================================
mm_current_events = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Current Events &amp; Achievements of UP</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की समसामयिक घटनाएं, उपलब्धियां एवं मेगा प्रोजेक्ट्स</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Expressway Capital of India • Civil Aviation &amp; 5 International Airports • Namo Bharat RRTS &amp; Metro Systems • Defense Corridor &amp; BrahMos • Digital Governance &amp; GIS 2023 • National Welfare Rankings</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • देश का एक्सप्रेसवे प्रदेश • नागरिक उड्डयन व 5 अंतरराष्ट्रीय हवाई अड्डे • नमो भारत RRTS व मेट्रो तंत्र • रक्षा गलियारा व ब्रह्मोस • डिजिटल गवर्नेंस व जीआईएस 2023 • राष्ट्रीय योजनाओं में प्रथम स्थान</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-rocket"></i>
            <span class="lang-en">Transformational Governance &amp; Infrastructure Milestones of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का बुनियादी ढांचा, सुशासन एवं विकास के ऐतिहासिक मील के पत्थर</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Expressway Network: Capital of Expressways -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-road" style="color: #059669;"></i>
                    <span class="lang-en">1. Expressway Super-Network</span>
                    <span class="lang-hi">1. देश का एक्सप्रेसवे प्रदेश</span>
                </h4>
                <span class="mindmap-node-tag">6 Operational • 7 Upcoming</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-route"></i>
                        <span class="lang-en">Operational &amp; Under-Construction Expressways</span>
                        <span class="lang-hi">संचालित एवं निर्माणाधीन एक्सप्रेसवे</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Purvanchal Expressway (341 km):</strong> Inaugurated Nov 2021; connects Lucknow (Chand Sarai) to Ghazipur (Haidaria); traverses 9 districts; has a 3.2 km fighter airstrip at Kurebhar (Sultanpur).</span>
                            <span class="lang-hi"><strong>पूर्वांचल एक्सप्रेसवे (341 किमी):</strong> लखनऊ से गाजीपुर; 9 जिलों से गुजरता है; सुल्तानपुर के कूड़ेभार में 3.2 किमी की फाइटर एयरस्ट्रिप।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bundelkhand Expressway (296 km):</strong> Inaugurated July 2022; links Chitrakoot (Bharatkoop) to Etawah (Kudrail); connects 7 districts; provides direct link to Agra-Lucknow Expressway.</span>
                            <span class="lang-hi"><strong>बुंदेलखंड एक्सप्रेसवे (296 किमी):</strong> चित्रकूट से इटावा; 7 बुंदेलखंड जिलों को जोड़ते हुए आगरा-लखनऊ एक्सप्रेसवे से जोड़ता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ganga Expressway (594 km):</strong> UP's longest expressway under construction; stretches from Bijauli (Meerut) to Judapur Dandu (Prayagraj); connects 12 districts; airstrip at Shahjahanpur.</span>
                            <span class="lang-hi"><strong>गंगा एक्सप्रेसवे (594 किमी):</strong> मेरठ से प्रयागराज; 12 जिलों को जोड़ने वाला उप्र का सबसे लंबा एक्सप्रेसवे (शाहजहाँपुर में आपातकालीन एयरस्ट्रिप)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Other Key Arteries:</strong> <em>Agra-Lucknow Expressway (302 km)</em>; <em>Yamuna Expressway (165 km)</em>; <em>Gorakhpur Link Expressway (91 km)</em> connecting Gorakhpur to Purvanchal Expressway.</span>
                            <span class="lang-hi"><strong>अन्य एक्सप्रेसवे:</strong> <em>आगरा-लखनऊ (302 किमी)</em>; <em>यमुना (165 किमी)</em>; <em>गोरखपुर लिंक (91 किमी)</em> जो गोरखपुर को पूर्वांचल एक्सप्रेसवे से जोड़ता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP holds over 50% of India's total expressway network. Ganga Expressway is 594 km (12 districts) and Purvanchal is 341 km (9 districts)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> देश के कुल एक्सप्रेसवे नेटवर्क का 50% से अधिक उप्र में है। गंगा एक्सप्रेसवे 594 किमी (12 जिले) व पूर्वांचल 341 किमी (9 जिले) लंबा है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Civil Aviation Revolution & 5 International Airports -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-plane-departure" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Aviation &amp; 5 Int'l Airports</span>
                    <span class="lang-hi">2. नागरिक उड्डयन एवं 5 अंतरराष्ट्रीय हवाई अड्डे</span>
                </h4>
                <span class="mindmap-node-tag">21 Airports • Only State with 5 Int'l</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-plane"></i>
                        <span class="lang-en">The 5 International Airports of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के 5 अंतरराष्ट्रीय हवाई अड्डे</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Lucknow:</strong> Chaudhary Charan Singh Int'l Airport (Amausi)</span>
                        <span class="mindmap-chip"><strong>2. Varanasi:</strong> Lal Bahadur Shastri Int'l Airport (Babatpur)</span>
                        <span class="mindmap-chip"><strong>3. Kushinagar:</strong> Kushinagar Int'l Airport (Buddhist Circuit hub)</span>
                        <span class="mindmap-chip"><strong>4. Ayodhya:</strong> Maharishi Valmiki Int'l Airport (Ayodhya Dham)</span>
                        <span class="mindmap-chip"><strong>5. Noida (Jewar):</strong> Noida Int'l Airport (Asia's largest upon completion)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-tower-control"></i>
                        <span class="lang-en">Regional Domestic Connectivity (UDAN)</span>
                        <span class="lang-hi">क्षेत्रीय संपर्क एवं उड़ान योजना</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>21 Airport Target:</strong> UP expanded from 4 operational airports in 2017 to over 16 operational airports (including Bareilly, Prayagraj, Hindon-Ghaziabad, Aligarh, Azamgarh, Chitrakoot, Moradabad, Shravasti).</span>
                            <span class="lang-hi"><strong>21 हवाई अड्डों का नेटवर्क:</strong> 2017 के 4 हवाई अड्डों से बढ़कर अब 16+ चालू (बरेली, प्रयागराज, हिंडन, अलीगढ़, आजमगढ़, चित्रकूट, मुरादाबाद, श्रावस्ती आदि)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP is the first and only state in India with 5 International Airports! Jewar (Noida International Airport) will be the largest airport in Asia.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र देश का पहला और एकमात्र राज्य है जहाँ 5 अंतरराष्ट्रीय हवाई अड्डे हैं! जेवर (नोएडा) एशिया का सबसे बड़ा हवाई अड्डा बन रहा है।</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Rapid Rail (RRTS) & Urban Metro Networks -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-train-subway" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Namo Bharat RRTS &amp; Metros</span>
                    <span class="lang-hi">3. नमो भारत RRTS एवं मेट्रो नेटवर्क</span>
                </h4>
                <span class="mindmap-node-tag">180 kmph RRTS • 6 Metro Cities</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-bolt"></i>
                        <span class="lang-en">India's First RapidX / RRTS (Namo Bharat)</span>
                        <span class="lang-hi">भारत की प्रथम रैपिड रेल (नमो भारत)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Delhi-Ghaziabad-Meerut Corridor (82.15 km):</strong> India's first Regional Rapid Transit System. Design speed: <strong>180 km/h</strong>, operational speed: 160 km/h. Priority section (Sahibabad to Duhai Depot, 17 km) inaugurated by PM Modi on <strong>20 Oct 2023</strong> flagging off 'Namo Bharat'.</span>
                            <span class="lang-hi"><strong>दिल्ली-गाजियाबाद-मेरठ कॉरिडोर (82.15 किमी):</strong> भारत की पहली रीजनल रैपिड रेल; डिजाइन गति <strong>180 किमी/घंटा</strong>; 20 अक्टूबर 2023 को साहिबाबाद से दुहाई डिपो (17 किमी) के बीच देश की पहली 'नमो भारत' ट्रेन शुरू।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-train"></i>
                        <span class="lang-en">Metro Rail Leadership in India</span>
                        <span class="lang-hi">मेट्रो रेल संचालन में देश में अग्रणी</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Lucknow Metro:</strong> Amausi Airport to Munshipulia</span>
                        <span class="mindmap-chip"><strong>2. Noida Metro:</strong> Aqua Line (Noida to Greater Noida)</span>
                        <span class="mindmap-chip"><strong>3. Kanpur Metro:</strong> IIT Kanpur to Moti Jheel operational</span>
                        <span class="mindmap-chip"><strong>4. Agra Metro:</strong> Taj East Gate to Jama Masjid / Mankameshwar</span>
                        <span class="mindmap-chip"><strong>5. Ghaziabad &amp; Meerut:</strong> Integrated with NCR &amp; RRTS</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> India's first RRTS 'Namo Bharat' train operates between Delhi-Ghaziabad-Meerut (180 km/h design speed). UP has 6 cities with operational metro rail!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> देश की पहली रैपिड रेल 'नमो भारत' दिल्ली-गाजियाबाद-मेरठ के बीच शुरू हुई। उप्र देश में सर्वाधिक 6 शहरों में मेट्रो संचालित करने वाला राज्य है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Defense Corridor & Strategic Manufacturing -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-halved" style="color: #d97706;"></i>
                    <span class="lang-en">4. Defense Corridor &amp; BrahMos</span>
                    <span class="lang-hi">4. रक्षा औद्योगिक गलियारा एवं ब्रह्मोस</span>
                </h4>
                <span class="mindmap-node-tag">6 Defense Nodes • Atmanirbhar Bharat</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crosshairs"></i>
                        <span class="lang-en">The 6 Nodes of UP Defense Industrial Corridor</span>
                        <span class="lang-hi">रक्षा गलियारे के 6 प्रमुख नोड्स</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Lucknow:</strong> BrahMos Aerospace Next-Gen (NG) Cruise Missiles</span>
                        <span class="mindmap-chip"><strong>Kanpur:</strong> Ordnance Factory Board, Small Arms, Adani Ammo Park</span>
                        <span class="mindmap-chip"><strong>Jhansi:</strong> Bharat Dynamics Limited (BDL) missile propulsion unit</span>
                        <span class="mindmap-chip"><strong>Aligarh:</strong> Precision engineering, UAV components &amp; locks</span>
                        <span class="mindmap-chip"><strong>Agra:</strong> Aerospace components, ballistic armors &amp; leathergear</span>
                        <span class="mindmap-chip"><strong>Chitrakoot:</strong> Specialized defense logistics &amp; assembly</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-rocket"></i>
                        <span class="lang-en">BrahMos Aerospace Manufacturing Unit</span>
                        <span class="lang-hi">ब्रह्मोस एयरोस्पेस विनिर्माण केंद्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow BrahMos Unit:</strong> 200-acre state-of-the-art facility at Bhatgaon (Lucknow); produces 80 to 100 BrahMos-NG supersonic cruise missiles annually for Indian Armed Forces and friendly export nations.</span>
                            <span class="lang-hi"><strong>लखनऊ ब्रह्मोस यूनिट:</strong> भटगांव (लखनऊ) में 200 एकड़ में स्थापित; प्रतिवर्ष 80-100 ब्रह्मोस-NG सुपरसोनिक क्रूज मिसाइलों का उत्पादन।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP Defense Corridor has 6 nodes: Lucknow, Kanpur, Jhansi, Aligarh, Agra, and Chitrakoot. BrahMos missiles are produced in Lucknow!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र रक्षा गलियारे के 6 नोड हैं: लखनऊ, कानपुर, झांसी, अलीगढ़, आगरा और चित्रकूट। ब्रह्मोस मिसाइल निर्माण केंद्र लखनऊ में है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Digital Governance & Investment Summits -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-laptop-code" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Digital Governance &amp; GIS 2023</span>
                    <span class="lang-hi">5. डिजिटल सुशासन एवं वैश्विक निवेश</span>
                </h4>
                <span class="mindmap-node-tag">₹33.5 Lakh Cr MoUs • Nivesh Mitra</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-chart-pie"></i>
                        <span class="lang-en">Global Investors Summit (GIS) 2023</span>
                        <span class="lang-hi">ग्लोबल इन्वेस्टर्स समिट 2023</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Record Investment Inflow:</strong> UP GIS held 10–12 Feb 2023 in Lucknow; bagged <strong>₹33.5 Lakh Crore</strong> in investment proposals across 20,000+ MoUs. Ground Breaking Ceremony (GBC-IV) in Feb 2024 operationalized projects worth over ₹10 Lakh Crore.</span>
                            <span class="lang-hi"><strong>ऐतिहासिक निवेश:</strong> फरवरी 2023 में आयोजित जीआईएस में <strong>₹33.5 लाख करोड़</strong> के एमओयू; फरवरी 2024 के चौथे ग्राउंड ब्रेकिंग समारोह में ₹10 लाख करोड़ से अधिक की परियोजनाएं धरातल पर उतरीं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-network-wired"></i>
                        <span class="lang-en">Pioneering Digital Portals</span>
                        <span class="lang-hi">अग्रणी डिजिटल पोर्टल एवं सुधार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Nivesh Mitra:</strong> 400+ online clearance services</span>
                        <span class="mindmap-chip"><strong>Nivesh Sarathi:</strong> Digital MoU tracking portal</span>
                        <span class="mindmap-chip"><strong>e-FIR &amp; UP 112:</strong> Fastest emergency response in India</span>
                        <span class="mindmap-chip"><strong>Mine Mitra:</strong> Mining surveillance &amp; e-permits</span>
                        <span class="mindmap-chip"><strong>e-Abkari &amp; e-Prosecution:</strong> Rank 1 in national disposal</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP ranks #1 in India for inter-operable criminal justice system (e-Prosecution portal) and achieved an 'Achiever' grade in Ease of Doing Business (BRAP)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र ई-प्रॉसीक्यूशन पोर्टल के माध्यम से मामलों के निस्तारण में देश में प्रथम स्थान पर है तथा ईज ऑफ डूइंग बिजनेस में 'अचीवर' राज्य है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: National Welfare Leadership & National Ranks -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-medal" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. National Welfare Leadership</span>
                    <span class="lang-hi">6. राष्ट्रीय जनकल्याणकारी योजनाओं में प्रथम स्थान</span>
                </h4>
                <span class="mindmap-node-tag">Rank 1 in 10+ Central Schemes</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hand-holding-heart"></i>
                        <span class="lang-en">Schemes where UP Ranks #1 in India</span>
                        <span class="lang-hi">जिन योजनाओं में उप्र देश में प्रथम स्थान पर है</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>PM-KISAN:</strong> Over 2.6 Crore beneficiary farmers</span>
                        <span class="mindmap-chip"><strong>PMAY (Gramin &amp; Urban):</strong> Over 47 Lakh pucca houses built</span>
                        <span class="mindmap-chip"><strong>PM SVANidhi:</strong> Over 15 Lakh street vendor micro-loans</span>
                        <span class="mindmap-chip"><strong>Swachh Bharat:</strong> Highest individual toilets constructed</span>
                        <span class="mindmap-chip"><strong>PM Ujjwala Yojana:</strong> Over 1.75 Crore free LPG connections</span>
                        <span class="mindmap-chip"><strong>PM Saubhagya:</strong> Highest rural household electrifications</span>
                        <span class="mindmap-chip"><strong>Ayushman Bharat:</strong> Over 5 Crore golden cards issued</span>
                        <span class="mindmap-chip"><strong>Jal Jeevan Mission:</strong> Highest tap water connections issued</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Uttar Pradesh ranks #1 in India in PM-KISAN, PM Awas Yojana, PM SVANidhi, Ujjwala Yojana, and Ayushman Bharat Card generation!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उत्तर प्रदेश पीएम-किसान, पीएम आवास योजना, पीएम स्वनिधि, उज्ज्वला योजना, और आयुष्मान भारत कार्ड बनाने में देश में प्रथम स्थान पर है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 8: Economy of Uttar Pradesh
# ==============================================================================
mm_economy = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Economy of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की समग्र अर्थव्यवस्था एवं सार्वजनिक वित्त</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Macroeconomic Dimensions &amp; $1T Target • Sectoral Composition (GSVA Shares) • State Budget Architecture &amp; Public Finance • Regional Disparities • Power &amp; Energy Infrastructure • Economic Development Authorities</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • मैक्रोइकॉनॉमिक आयाम व $1 ट्रिलियन लक्ष्य • क्षेत्रीय संरचना (GSVA हिस्सेदारी) • राज्य बजट वास्तुकला व लोक वित्त • क्षेत्रीय विषमताएं • विद्युत व ऊर्जा ढांचा • औद्योगिक विकास प्राधिकरण</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-vault"></i>
            <span class="lang-en">State Macroeconomics, Fiscal Architecture &amp; Growth Engine of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की राज्य अर्थव्यवस्था, राजकोषीय संरचना एवं विकास के चालक</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Macroeconomic Dimensions & Target -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-chart-line" style="color: #059669;"></i>
                    <span class="lang-en">1. Macroeconomic Dimensions</span>
                    <span class="lang-hi">1. वृहद आर्थिक आयाम एवं लक्ष्य</span>
                </h4>
                <span class="mindmap-node-tag">2nd Largest GSDP • $1 Trillion Goal</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-landmark"></i>
                        <span class="lang-en">Core Economic Metrics</span>
                        <span class="lang-hi">प्रमुख आर्थिक संकेतक</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>National Standing:</strong> UP is India's <strong>second largest state economy</strong>, contributing approximately <strong>9.2%</strong> of India's national GDP (trailing only Maharashtra).</span>
                            <span class="lang-hi"><strong>राष्ट्रीय स्थिति:</strong> उप्र महाराष्ट्र के बाद भारत की <strong>दूसरी सबसे बड़ी राज्य अर्थव्यवस्था</strong> है, जो देश की कुल जीडीपी में लगभग <strong>9.2%</strong> का योगदान देती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>GSDP Milestones:</strong> Gross State Domestic Product (GSDP) crossed <strong>₹25.48 Lakh Crore</strong> in 2023-24 (nominal growth rate ~19.2%). Target: <strong>$1 Trillion Economy by 2027-28</strong>.</span>
                            <span class="lang-hi"><strong>GSDP आंकड़े:</strong> 2023-24 में सकल राज्य घरेलू उत्पाद <strong>₹25.48 लाख करोड़</strong> पार कर गया (वृद्धि दर ~19.2%)। लक्ष्य: <strong>2027-28 तक $1 ट्रिलियन अर्थव्यवस्था</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Per Capita Income (PCI):</strong> Per capita income at current prices stands at ~₹83,000–₹86,000 (has doubled in the last 6 years, steadily closing the gap with national average).</span>
                            <span class="lang-hi"><strong>प्रति व्यक्ति आय:</strong> वर्तमान मूल्यों पर प्रति व्यक्ति आय ~₹83,000-₹86,000 है (पिछले 6 वर्षों में दोगुनी हुई है)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP is India's 2nd largest state economy (~9.2% share) and aims to reach $1 Trillion by 2027-28!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र देश की दूसरी सबसे बड़ी अर्थव्यवस्था (~9.2% हिस्सेदारी) है तथा 2027-28 तक $1 ट्रिलियन का लक्ष्य रखा गया है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Sectoral Composition (GSVA Shares) -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-pie-chart" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Sectoral Structure (GSVA)</span>
                    <span class="lang-hi">2. क्षेत्रीय संरचना (GSVA हिस्सेदारी)</span>
                </h4>
                <span class="mindmap-node-tag">Primary • Secondary • Tertiary</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Share in Gross State Value Added (GSVA)</span>
                        <span class="lang-hi">सकल राज्य मूल्य संवर्धन में हिस्सेदारी</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Primary Sector (प्राथमिक):</strong> ~26.1% (Agri, Dairy, Forestry)</span>
                        <span class="mindmap-chip"><strong>Secondary Sector (द्वितीयक):</strong> ~24.3% (Manufacturing, Power)</span>
                        <span class="mindmap-chip"><strong>Tertiary Sector (तृतीयक):</strong> ~49.6% (Services, Trade, Real Estate)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-arrows-split-up-and-left"></i>
                        <span class="lang-en">Structural Economic Shifts</span>
                        <span class="lang-hi">संरचनात्मक आर्थिक बदलाव</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Services Dominance:</strong> Tertiary (services) sector contributes nearly half of the economy (~50%), driven by IT/ITeS in Noida, trade, financial services, logistics, and tourism.</span>
                            <span class="lang-hi"><strong>सेवा क्षेत्र का प्रभुत्व:</strong> तृतीयक क्षेत्र का योगदान लगभग आधा (~50%) है, जिसका मुख्य आधार नोएडा का आईटी हब, व्यापार, परिवहन व पर्यटन है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Workforce Asymmetry:</strong> While Primary sector generates ~26% of GSVA, it still engages ~59.3% of the total working population, highlighting the imperative of shifting labor to industry and services.</span>
                            <span class="lang-hi"><strong>श्रम असंतुलन:</strong> प्राथमिक क्षेत्र जहां 26% आय देता है, वहीं 59.3% कार्यबल को रोजगार देता है; अतः उद्योगों व सेवाओं में रोजगार बढ़ाना अनिवार्य है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Tertiary (Services) sector is the largest contributor to UP's economy (~50%), followed by Primary (~26%) and Secondary (~24%)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र की अर्थव्यवस्था में सर्वाधिक योगदान तृतीयक/सेवा क्षेत्र (~50%) का है, इसके बाद प्राथमिक (~26%) और द्वितीयक (~24%) हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: State Budget Architecture & Public Finance -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-money-bill-transfer" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. State Budget &amp; Public Finance</span>
                    <span class="lang-hi">3. राज्य बजट वास्तुकला एवं लोक वित्त</span>
                </h4>
                <span class="mindmap-node-tag">₹7.36+ Lakh Crore Budget • Revenue Surplus</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-scale-balanced"></i>
                        <span class="lang-en">Fiscal Discipline &amp; Revenue Sources</span>
                        <span class="lang-hi">राजकोषीय अनुशासन एवं आय के स्रोत</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Historic Budget Size:</strong> State Budget for 2024-25 stood at a historic <strong>₹7,36,437 Crore</strong> (largest ever in UP history, up from ~₹3.8 Lakh Cr in 2017).</span>
                            <span class="lang-hi"><strong>ऐतिहासिक बजट आकार:</strong> 2024-25 का बजट <strong>₹7,36,437 करोड़</strong> का रहा (उप्र के इतिहास का सबसे बड़ा बजट)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Own Tax Revenue (OTR):</strong> State's Own Tax Revenue is dominated by <strong>State GST (SGST)</strong>, followed by <strong>State Excise (आबकारी शुल्क)</strong>, <strong>Stamp &amp; Registration Fees</strong>, and <strong>Taxes on Vehicles</strong>.</span>
                            <span class="lang-hi"><strong>स्वयं का कर राजस्व:</strong> उप्र के स्वयं के कर राजस्व में सबसे बड़ा हिस्सा <strong>SGST</strong> का है, जिसके बाद <strong>राज्य आबकारी</strong>, <strong>स्टांप व पंजीकरण</strong> तथा <strong>वाहन कर</strong> आते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>FRBM Act Compliance:</strong> Fiscal deficit is maintained strictly within the prescribed limit of <strong>under 3.5% of GSDP</strong> (budgeted at ~3.46%), while maintaining a healthy <strong>Revenue Surplus</strong> (~₹74,000+ Cr).</span>
                            <span class="lang-hi"><strong>FRBM अनुपालन:</strong> राजकोषीय घाटा GSDP के 3.5% की सीमा के भीतर (लगभग 3.46%) नियंत्रित है तथा लगातार <strong>राजस्व अधिशेष</strong> बना हुआ है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> State GST (SGST) is the largest single source of Own Tax Revenue in Uttar Pradesh, followed by State Excise!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र के स्वयं के कर राजस्व में सबसे बड़ा एकल स्रोत राज्य जीएसटी (SGST) है, जिसके बाद राज्य आबकारी शुल्क का स्थान है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Regional Economic Disparities (4 Economic Regions) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-globe" style="color: #d97706;"></i>
                    <span class="lang-en">4. Regional Disparities</span>
                    <span class="lang-hi">4. 4 आर्थिक क्षेत्र एवं क्षेत्रीय विषमताएं</span>
                </h4>
                <span class="mindmap-node-tag">Western • Central • Eastern • Bundelkhand</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-chart-column"></i>
                        <span class="lang-en">Economic Contribution by Region</span>
                        <span class="lang-hi">क्षेत्रवार आर्थिक योगदान</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Western UP (पश्चिमी):</strong> ~50% of GSDP (Industrial engine &amp; high yield agri)</span>
                        <span class="mindmap-chip"><strong>Eastern UP (पूर्वी / पूर्वांचल):</strong> ~26% of GSDP (High population, 28 districts)</span>
                        <span class="mindmap-chip"><strong>Central UP (मध्य):</strong> ~18% of GSDP (Kanpur, Lucknow)</span>
                        <span class="mindmap-chip"><strong>Bundelkhand (बुंदेलखंड):</strong> ~6% of GSDP (7 districts, plateau, minerals)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-bridge"></i>
                        <span class="lang-en">Bridging the Gap via Expressways</span>
                        <span class="lang-hi">बुनियादी ढांचे द्वारा असंतुलन पाटना</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Noida / Gautam Buddha Nagar:</strong> Highest per capita income and industrial output district in UP (generates over 10% of total state revenue).</span>
                            <span class="lang-hi"><strong>गौतम बुद्ध नगर (नोएडा):</strong> राज्य में सर्वाधिक प्रति व्यक्ति आय और औद्योगिक उत्पादन वाला जिला।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Purvanchal &amp; Bundelkhand Revival:</strong> Massive infrastructure injection via Purvanchal &amp; Bundelkhand Expressways, Defense Corridor nodes (Jhansi/Chitrakoot), and Ken-Betwa link.</span>
                            <span class="lang-hi"><strong>पूर्वांचल व बुंदेलखंड उत्थान:</strong> एक्सप्रेसवे नेटवर्क, रक्षा गलियारे के नोड्स (झांसी/चित्रकूट) तथा केन-बेतवा लिंक से क्षेत्रीय विकास।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Western UP contributes nearly 50% of the state's total GSDP. Gautam Buddha Nagar has the highest per capita income in UP!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> पश्चिमी उप्र राज्य के सकल घरेलू उत्पाद में लगभग 50% का योगदान देता है। गौतमबुद्ध नगर में प्रति व्यक्ति आय सर्वाधिक है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Power & Energy Infrastructure -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-bolt-lightning" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Power &amp; Energy Infrastructure</span>
                    <span class="lang-hi">5. विद्युत, ऊर्जा ढांचा एवं परमाणु केंद्र</span>
                </h4>
                <span class="mindmap-node-tag">Narora Atomic • Thermal Giants • Solar</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-atom"></i>
                        <span class="lang-en">Nuclear Power Station of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश का एकमात्र परमाणु ऊर्जा संयंत्र</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Narora Atomic Power Station (NAPS, Bulandshahr):</strong> State's only nuclear power facility on the bank of River Ganga; operates two Pressurized Heavy Water Reactors (PHWR) of 220 MWe each (Unit-1 1991, Unit-2 1992).</span>
                            <span class="lang-hi"><strong>नरौरा परमाणु संयंत्र (बुलंदशहर):</strong> गंगा तट पर स्थित उप्र का एकमात्र परमाणु ऊर्जा केंद्र; 220 मेगावाट की 2 PHWR इकाइयाँ (1991 व 1992 में चालू)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-smog"></i>
                        <span class="lang-en">Major Thermal Power Plants</span>
                        <span class="lang-hi">प्रमुख ताप विद्युत संयंत्र</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Singrauli Super Thermal (NTPC):</strong> Shaktinagar, Sonbhadra (first NTPC plant)</span>
                        <span class="mindmap-chip"><strong>Rihand Super Thermal (NTPC):</strong> Rihand Nagar, Sonbhadra</span>
                        <span class="mindmap-chip"><strong>Obra &amp; Anpara Thermal:</strong> Sonbhadra (UPRVUNL)</span>
                        <span class="mindmap-chip"><strong>Harduaganj Thermal:</strong> Aligarh (Oldest power plant in UP, 1942)</span>
                        <span class="mindmap-chip"><strong>Parichha Thermal:</strong> Jhansi (Betwa river bank)</span>
                        <span class="mindmap-chip"><strong>Tanda Thermal:</strong> Ambedkar Nagar (NTPC)</span>
                        <span class="mindmap-chip"><strong>Rosa Thermal:</strong> Shahjahanpur (Reliance Power)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Narora (Bulandshahr) is UP's sole atomic power station. Sonbhadra is hailed as the <em>'Energy Capital of India' (ऊर्जा राजधानी)</em> due to thermal clusters!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नरौरा (बुलंदशहर) उप्र का एकमात्र परमाणु संयंत्र है। सोनभद्र को भारी विद्युत उत्पादन के कारण <em>'भारत की ऊर्जा राजधानी'</em> कहा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Industrial Development Authorities (UPSIDA, NOIDA & UPEIDA) -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-building" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Industrial Authorities</span>
                    <span class="lang-hi">6. औद्योगिक विकास प्राधिकरण एवं संस्थान</span>
                </h4>
                <span class="mindmap-node-tag">NOIDA • YEIDA • UPSIDA • UPEIDA</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-city"></i>
                        <span class="lang-en">Key Industrial Authorities of UP</span>
                        <span class="lang-hi">प्रमुख औद्योगिक विकास प्राधिकरण</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>NOIDA:</strong> New Okhla Industrial Dev. Authority (Est. 1976)</span>
                        <span class="mindmap-chip"><strong>GIDA:</strong> Gorakhpur Industrial Development Authority (1989)</span>
                        <span class="mindmap-chip"><strong>SIDA:</strong> Satharia Industrial Dev. Authority (Jaunpur, 1989)</span>
                        <span class="mindmap-chip"><strong>YEIDA:</strong> Yamuna Expressway Industrial Dev. Authority (2001)</span>
                        <span class="mindmap-chip"><strong>UPEIDA:</strong> UP Expressways Industrial Dev. Authority (2007)</span>
                        <span class="mindmap-chip"><strong>UPSIDA:</strong> UP State Industrial Dev. Authority (HQ: Kanpur)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building-ngo"></i>
                        <span class="lang-en">State Financial &amp; Industrial Corporations</span>
                        <span class="lang-hi">राज्य वित्तीय एवं औद्योगिक निगम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UPFC (UP Financial Corporation):</strong> Established in <strong>1954</strong> at Kanpur to provide medium and long-term credit to industrial enterprises.</span>
                            <span class="lang-hi"><strong>उप्र वित्तीय निगम (UPFC):</strong> <strong>1954 में कानपुर</strong> में स्थापित; उद्योगों को मध्यम व दीर्घकालिक वित्तीय ऋण सहायता प्रदान करता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> NOIDA was formed under UP Industrial Development Act 1976. UPSIDA and UP Financial Corporation (1954) are headquartered in Kanpur!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नोएडा की स्थापना 1976 में हुई थी। यूपीसीडा (UPSIDA) और उप्र वित्तीय निगम (1954) का मुख्यालय कानपुर में स्थित है!</span>
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
    inject_mindmap('climate', mm_climate)
    inject_mindmap('culture', mm_culture)
    inject_mindmap('current-events-and-achievements-of-uttar-pradesh-state-in-various-fields-etc', mm_current_events)
    inject_mindmap('economy', mm_economy)
