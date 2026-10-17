import os
import re

def build_climate_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Climate Systems &amp; Weather Dynamics of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की जलवायु प्रणाली एवं मौसमी गतिकी</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Climate of Uttar Pradesh] --> B[Classification: Koeppen Cwg]
    A --> C[Three Distinct Seasons]
    A --> D[Rainfall Dynamics & Distribution]
    A --> E[Agro-Climatic Zones: 9 Zones]
    A --> F[Extreme Records & Anomalies]

    B --> B1[Subtropical Humid / Tropical Monsoon]
    B --> B2[Cwg: Warm Temperate with Dry Winter & Hot Summer]
    B --> B3[Thornthwaite: CB'w | Trewartha: CAw]

    C --> C1[Summer: March-mid June | Loo & Heatwaves | Jhansi/Agra 48°C+]
    C --> C2[Rainy: mid June-Oct | 80-85% Rain | Bay of Bengal Purva]
    C --> C3[Winter: Oct-Feb | Jan Coldest Bareilly | Western Disturbances]

    D --> D1[Average Annual Rain: ~94.8 cm]
    D --> D2[Decreasing Gradient: East to West & North to South]
    D --> D3[Monsoon Purva Winds: 80-85% total precipitation]
    D --> D4[Winter Showers: Western Disturbances for Rabi Wheat]

    E --> E1[Bhabhar-Terai & Vindhyan]
    E --> E2[Western, Mid-Western & South-Western Semi-Arid]
    E --> E3[Central, Bundelkhand, North-Eastern & Eastern Plains]

    F --> F1[Highest Rain: Gorakhpur 184.7 cm / 56 rainy days]
    F --> F2[Lowest Rain: Mathura 54.4 cm / 32 rainy days]
    F --> F3[Hottest Districts: Agra & Jhansi]
    F --> F4[Coldest Plains: Bareilly]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की जलवायु] --> B[वैज्ञानिक वर्गीकरण: कोपेन Cwg]
    A --> C[तीन प्रमुख ऋतुएँ]
    A --> D[वर्षा प्रणाली एवं वितरण]
    A --> E[कृषि-जलवायु क्षेत्र: कुल 9]
    A --> F[चरम मौसम रिकॉर्ड एवं तथ्य]

    B --> B1[उपोष्ण आर्द्र / उष्णकटिबंधीय मानसूनी जलवायु]
    B --> B2[Cwg: शुष्क शीत ऋतु व गर्म ग्रीष्म ऋतु वाला गंगा तुल्य प्रदेश]
    B --> B3[थार्नथ्वेट: CB'w | त्रिवार्था: CAw]

    C --> C1[ग्रीष्म ऋतु: मार्च-मध्य जून | लू एवं धूल भरी आंधी | झांसी/आगरा 48°C+]
    C --> C2[वर्षा ऋतु: मध्य जून-अक्टूबर | 80-85% वर्षा | बंगाल खाड़ी पूर्वा]
    C --> C3[शीत ऋतु: अक्टूबर-फरवरी | जनवरी सबसे ठंडा बरेली | पश्चिमी विक्षोभ]

    D --> D1[राज्य की औसत वार्षिक वर्षा: ~94.8 सेमी]
    D --> D2[घटती वर्षा प्रवणता: पूर्व से पश्चिम एवं उत्तर से दक्षिण]
    D --> D3[मानसूनी पूर्वा हवाएं: 80-85% वर्षा हेतु उत्तरदायी]
    D --> D4[शीतकालीन वर्षा: पश्चिमी विक्षोभ / मावठ रबी गेहूं हेतु वरदान]

    E --> E1[भाबर-तराई एवं विंध्य क्षेत्र]
    E --> E2[पश्चिमी, मध्य-पश्चिमी एवं दक्षिण-पश्चिमी अर्ध-शुष्क]
    E --> E3[केंद्रीय, बुंदेलखंड, उत्तर-पूर्वी एवं पूर्वी मैदानी क्षेत्र]

    F --> F1[सर्वाधिक वर्षा: गोरखपुर 184.7 सेमी / 56 वर्षा दिन]
    F --> F2[न्यूनतम वर्षा: मथुरा 54.4 सेमी / 32 वर्षा दिन]
    F --> F3[सर्वाधिक गर्म जिले: आगरा एवं झांसी]
    F --> F4[सर्वाधिक ठंडा मैदानी जिला: बरेली]
    </div>
  </div>
</div>

<!-- Card 2: Scientific Classification & Climatic Characteristics -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Scientific Climatic Classification &amp; Regional Nomenclature</span>
    <span class="lang-hi">1. वैज्ञानिक जलवायु वर्गीकरण एवं क्षेत्रीय नामकरण</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>General Nature:</strong> Uttar Pradesh is characterized by a <strong>Subtropical Humid Monsoon Climate</strong> (उपोष्ण मानसूनी जलवायु) with extreme seasonal variations due to its continental interior location.</span>
      <span class="lang-hi"><strong>सामान्य स्वरूप:</strong> समुद्र से दूरी (महाद्वीपीय स्थिति) के कारण उत्तर प्रदेश की जलवायु <strong>उष्णकटिबंधीय / उपोष्ण मानसूनी</strong> है, जिसमें तीव्र मौसमी विषमताएं पाई जाती हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Vladimir Koeppen's Classification:</strong> Most of UP falls under the <strong>Cwg</strong> climatic type (Mesothermal Humid with Dry Winter and Hot Summer / Gangetic type climate). The southern fringes of Bundelkhand and Mirzapur plateau approach <strong>Aw</strong> (Tropical Savanna with dry winter).</span>
      <span class="lang-hi"><strong>व्लादिमीर कोपेन का वर्गीकरण:</strong> राज्य का अधिकांश मैदानी भाग <strong>Cwg</strong> (शुष्क शीत ऋतु युक्त मानसूनी गंगा-तुल्य जलवायु) के अंतर्गत आता है। दक्षिणी बुंदेलखंड एवं विंध्य पठारी सीमांत <strong>Aw</strong> (उष्णकटिबंधीय सवाना) प्रकार के निकट हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>C.W. Thornthwaite's Classification:</strong> Classifies UP primarily as <strong>CB'w</strong> (Sub-humid Mesothermal with winter rainfall deficiency).</span>
      <span class="lang-hi"><strong>सी.डब्ल्यू. थार्नथ्वेट का वर्गीकरण:</strong> उ.प्र. को मुख्य रूप से <strong>CB'w</strong> (उपोष्ण अर्ध-आर्द्र जलवायु, जहां शीतकाल में वर्षा की कमी होती है) के रूप में वर्गीकृत किया गया है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Glenn T. Trewartha's Classification:</strong> Places the state under the <strong>CAw</strong> (Subtropical Semi-arid to Sub-humid Monsoon) category.</span>
      <span class="lang-hi"><strong>ग्लेन टी. त्रिवार्था का वर्गीकरण:</strong> राज्य को <strong>CAw</strong> (उपोष्ण मानसूनी जलवायु क्षेत्र) के अंतर्गत रखा गया है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Major Climatic Regions (Prof. Stamp &amp; Stamp-Saxena):</strong> Divided into two primary zones: (i) <em>Humid &amp; Sub-humid Region</em> (तराई एवं पूर्वी मैदान, 100-150 cm rain) and (ii) <em>Moderately Dry / Semi-Arid Region</em> (मध्य एवं पश्चिमी मैदान व बुंदेलखंड, 50-80 cm rain).</span>
      <span class="lang-hi"><strong>प्रमुख प्राकृतिक जलवायु प्रदेश (प्रो. स्टाम्प व सक्सेना):</strong> दो मुख्य प्रदेशों में विभक्त: (i) <em>आर्द्र एवं उप-आर्द्र क्षेत्र</em> (तराई व पूर्वी मैदान, 100-150 सेमी वर्षा) तथा (ii) <em>मध्यम शुष्क / अर्ध-शुष्क क्षेत्र</em> (मध्य, पश्चिमी मैदान व बुंदेलखंड, 50-80 सेमी वर्षा)।</span>
    </li>
  </ul>
</div>

<!-- Card 3: Summer Season (Greeshma Ritu) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Summer Season (ग्रीष्म ऋतु): March to Mid-June</span>
    <span class="lang-hi">2. ग्रीष्म ऋतु (Summer Season): मार्च से मध्य-जून</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Solar Declination &amp; Pressure Shift:</strong> With the northward apparent movement of the Sun toward the Tropic of Cancer (23.5° N), temperature steadily rises across UP starting in March, peaking in late May and June.</span>
      <span class="lang-hi"><strong>सूर्य का उत्तरायण:</strong> मार्च में सूर्य के कर्क रेखा की ओर बढ़ने से राज्य में तापमान तेजी से बढ़ता है और मई-जून में चरम पर पहुंच जाता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Hottest Districts:</strong> <strong>Agra and Jhansi</strong> record the highest average maximum temperatures (often crossing <strong>48°C to 49°C</strong>), followed closely by Banda, Jalaun, and Hamirpur.</span>
      <span class="lang-hi"><strong>सर्वाधिक गर्म जिले:</strong> <strong>आगरा एवं झांसी</strong> में सर्वाधिक औसत अधिकतम तापमान (प्रायः <strong>48°C से 49°C</strong> तक) दर्ज किया जाता है, जिसके बाद बांदा, जालौन व हमीरपुर आते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Causes of Extreme Heat in South-West:</strong> Proximity to the arid Thar Desert of Rajasthan, rocky Bundelkhand gneiss/granite bedrock absorbing intense insolation, and absence of tree cover.</span>
      <span class="lang-hi"><strong>दक्षिण-पश्चिम में भीषण गर्मी के कारण:</strong> राजस्थान के थार मरुस्थल की निकटता, बुंदेलखंड के नीस/ग्रेनाइट चट्टानी धरातल द्वारा अत्यधिक ताप अवशोषण तथा वन आवरण की कमी।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Coldest / Mildest Summer District:</strong> <strong>Bareilly</strong> and adjacent Himalayan foothills (Terai) record the lowest summer temperatures due to proximity to mountains.</span>
      <span class="lang-hi"><strong>ग्रीष्मकाल में न्यूनतम तापमान:</strong> हिमालय की तलहटी से निकटता के कारण <strong>बरेली</strong> और आसपास के तराई जिलों में ग्रीष्मकालीन तापमान राज्य में सबसे कम रहता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>The 'Loo' Phenomenon:</strong> Intense, gusty, searing hot and bone-dry westerly winds that blow continuously from 10 AM to 5 PM across May and June, causing severe heat stroke.</span>
      <span class="lang-hi"><strong>'लू' (Loo) परिघटना:</strong> मई और जून में पश्चिम दिशा (राजस्थान) से बहने वाली अत्यंत शुष्क एवं धूल भरी गर्म हवाएं जो दिन में 10 बजे से शाम 5 बजे तक चलती हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Dust Storms (आंधी):</strong> Periodic convectional dust storms with wind speeds between 50-80 km/h occur in late afternoon, temporarily lowering temperatures by 3-5°C.</span>
      <span class="lang-hi"><strong>धूल भरी आंधियां:</strong> दोपहर बाद संवहनीय धाराओं द्वारा 50-80 किमी/घंटा की गति से धूल भरी आंधियां चलती हैं, जो क्षणिक रूप से तापमान में 3-5°C की गिरावट लाती हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Diurnal Temperature Range:</strong> The diurnal range (day vs. night temperature difference) is highest in the <strong>Bundelkhand Plateau</strong> region (14°C to 18°C).</span>
      <span class="lang-hi"><strong>दैनिक तापांतर:</strong> दिन और रात के तापमान का अंतर (दैनिक तापांतर) सर्वाधिक <strong>बुंदेलखंड पठारी क्षेत्र</strong> (14°C से 18°C) में पाया जाता है।</span>
    </li>
  </ul>
</div>

<!-- Card 4: Rainy Season (Varsha Ritu) & Monsoon Mechanics -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Rainy Season (वर्षा ऋतु): Mid-June to October &amp; Rainfall Distribution</span>
    <span class="lang-hi">3. वर्षा ऋतु (Rainy Season): मध्य-जून से अक्टूबर एवं वर्षा वितरण</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Monsoon Onset:</strong> The South-West Monsoon officially enters eastern Uttar Pradesh during the <strong>third or fourth week of June</strong> (approx. June 20-25) via the Bihar plains.</span>
      <span class="lang-hi"><strong>मानसून का आगमन:</strong> दक्षिण-पश्चिम मानसून राज्य के पूर्वी भाग (पूर्वांचल) में सामान्यतः <strong>जून के तीसरे या चौथे सप्ताह</strong> (20-25 जून के आसपास) में बिहार के रास्ते प्रवेश करता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Primary Source - Bay of Bengal Branch ('Purva'):</strong> Nearly <strong>80% to 85% of UP's annual rainfall</strong> is contributed by the Bay of Bengal branch of the SW monsoon. These moist easterly winds are locally termed <strong>'Purva' (पूर्वा / पुरवैया)</strong>.</span>
      <span class="lang-hi"><strong>मुख्य स्रोत - बंगाल की खाड़ी शाखा ('पूर्वा'):</strong> उ.प्र. की कुल वार्षिक वर्षा का लगभग <strong>80% से 85% भाग</strong> बंगाल की खाड़ी शाखा से प्राप्त होता है। इन मानसूनी हवाओं को स्थानीय रूप से <strong>'पूर्वा' या 'पुरवैया'</strong> कहा जाता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Arabian Sea Branch:</strong> The Arabian Sea branch advances through the Narmada-Tapti graben and affects southern UP (Bundelkhand and Mirzapur). In the plains, it converges with the Bay of Bengal branch.</span>
      <span class="lang-hi"><strong>अरब सागर शाखा:</strong> अरब सागर शाखा नर्मदा-ताप्ती घाटी से होकर दक्षिण उ.प्र. (बुंदेलखंड एवं विंध्य) में वर्षा करती है तथा उत्तरी मैदानी भाग में बंगाल की खाड़ी शाखा से मिल जाती है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>State Annual Average Rainfall:</strong> Approximately <strong>94.8 cm</strong> (normal range varies from 90 cm to 105 cm across standard meteorological cycles).</span>
      <span class="lang-hi"><strong>राज्य की औसत वार्षिक वर्षा:</strong> लगभग <strong>94.8 सेमी</strong> (विभिन्न वर्षों के चक्र में 90 सेमी से 105 सेमी के मध्य)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Highest Rainfall District:</strong> <strong>Gorakhpur</strong> records the state's highest average rainfall at <strong>184.7 cm</strong> (experiencing approximately <strong>56 rainy days</strong> per year).</span>
      <span class="lang-hi"><strong>सर्वाधिक वर्षा वाला जिला:</strong> <strong>गोरखपुर</strong> राज्य में सर्वाधिक औसत वर्षा दर्ज करता है - <strong>184.7 सेमी</strong> (वर्ष में लगभग <strong>56 वर्षा दिवस</strong>)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Lowest Rainfall District:</strong> <strong>Mathura</strong> records the lowest average rainfall at <strong>54.4 cm</strong> (with only about <strong>32 rainy days</strong> per year).</span>
      <span class="lang-hi"><strong>न्यूनतम वर्षा वाला जिला:</strong> <strong>मथुरा</strong> राज्य में सबसे कम वर्षा दर्ज करता है - मात्र <strong>54.4 सेमी</strong> (वर्ष में केवल लगभग <strong>32 वर्षा दिवस</strong>)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Natural Zone Rainfall Gradient:</strong>
        <br/>• <strong>Bhabhar-Terai Belt:</strong> 120 cm - 150 cm (Highest among natural physiographic zones)
        <br/>• <strong>Eastern Plains:</strong> 100 cm - 120 cm
        <br/>• <strong>Central Plains:</strong> 80 cm - 100 cm
        <br/>• <strong>Western Plains:</strong> 60 cm - 80 cm
        <br/>• <strong>South-Western / Bundelkhand:</strong> 50 cm - 70 cm (Drought-prone)
      </span>
      <span class="lang-hi"><strong>भौतिक प्रदेशीय वर्षा प्रवणता:</strong>
        <br/>• <strong>भाबर एवं तराई क्षेत्र:</strong> 120 से 150 सेमी (भौगोलिक क्षेत्रों में सर्वाधिक)
        <br/>• <strong>पूर्वी मैदानी भाग:</strong> 100 से 120 सेमी
        <br/>• <strong>मध्य मैदानी भाग:</strong> 80 से 100 सेमी
        <br/>• <strong>पश्चिमी मैदानी भाग:</strong> 60 से 80 सेमी
        <br/>• <strong>दक्षिण-पश्चिमी / बुंदेलखंड:</strong> 50 से 70 सेमी (सूखा प्रवृत्त क्षेत्र)
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Dual Gradient Rule:</strong> Rainfall consistently decreases from <strong>East to West</strong> (due to progressive loss of moisture in Purva winds) and from <strong>North to South</strong> (distance from Himalayan orographic barrier).</span>
      <span class="lang-hi"><strong>द्वि-दिशा प्रवणता नियम:</strong> उ.प्र. में वर्षा की मात्रा <strong>पूर्व से पश्चिम</strong> (पूर्वा हवाओं में आर्द्रता क्षीण होने के कारण) तथा <strong>उत्तर से दक्षिण</strong> (हिमालयी अवरोध से दूरी बढ़ने के कारण) लगातार घटती जाती है।</span>
    </li>
  </ul>
</div>

<!-- Card 5: Winter Season (Sheet Ritu) & Western Disturbances -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Winter Season (शीत ऋतु): October to February &amp; Western Disturbances</span>
    <span class="lang-hi">4. शीत ऋतु (Winter Season): अक्टूबर से फरवरी एवं पश्चिमी विक्षोभ</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Retreating Monsoon &amp; Transition:</strong> October and November mark the transition period (शरत ऋतु) characterized by clear skies, dropping humidity, and pleasant daytime weather ('October Heat' subsides by mid-November).</span>
      <span class="lang-hi"><strong>मानसून का निवर्तन एवं संक्रमण काल:</strong> अक्टूबर-नवंबर संक्रमण काल होता है जिसमें आकाश स्वच्छ रहता है, आर्द्रता घटती है और मौसम सुहावना होने लगता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Coldest Month:</strong> <strong>January</strong> is universally the coldest month across Uttar Pradesh, with average minimum temperatures ranging from 3°C to 10°C.</span>
      <span class="lang-hi"><strong>सर्वाधिक ठंडा महीना:</strong> <strong>जनवरी</strong> पूरे उत्तर प्रदेश में सबसे ठंडा महीना होता है, जिसमें औसत न्यूनतम तापमान 3°C से 10°C के मध्य रहता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Coldest Plain District:</strong> <strong>Bareilly</strong> and plains of Western UP record the lowest temperatures during peak winter spells (occasionally dropping to 1°C - 2°C).</span>
      <span class="lang-hi"><strong>सर्वाधिक ठंडा मैदानी जिला:</strong> शीत ऋतु के चरम में <strong>बरेली</strong> और पश्चिमी उ.प्र. के मैदानी जिलों में सबसे कम तापमान (कभी-कभी 1°C - 2°C तक) दर्ज किया जाता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Winter Temperature Gradient:</strong> Unlike summer, in winter the temperature <strong>increases from North to South</strong>. The southern Bundelkhand plateau remains comparatively warmer due to lower latitude and sun angle.</span>
      <span class="lang-hi"><strong>शीतकालीन तापमान प्रवणता:</strong> ग्रीष्म ऋतु के विपरीत, शीतकाल में तापमान <strong>उत्तर से दक्षिण की ओर बढ़ता है</strong>। दक्षिणी बुंदेलखंड पठार कम अक्षांश होने के कारण उत्तर की तुलना में अपेक्षाकृत गर्म रहता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Western Disturbances (पश्चिमी विक्षोभ):</strong> Temperate extra-tropical cyclones originating over the <strong>Mediterranean Sea and Caspian Sea</strong>, steered into North-West India by the Subtropical Westerly Jet Stream.</span>
      <span class="lang-hi"><strong>पश्चिमी विक्षोभ (Western Disturbances):</strong> <strong>भूमध्य सागर एवं कैस्पियन सागर</strong> से उत्पन्न होने वाले शीतोष्ण कटिबंधीय चक्रवात, जिन्हें उपोष्ण पछुआ जेट स्ट्रीम उत्तर-पश्चिम भारत की ओर ले आती है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Winter Rainfall ('Mahawat'):</strong> Western disturbances bring light to moderate showers (accounting for <strong>3% to 5% of UP's annual rain</strong>, ~10 cm in Western UP). Locally called <strong>'Mahawat' (मावठ)</strong>.</span>
      <span class="lang-hi"><strong>शीतकालीन वर्षा ('मावठ'):</strong> पश्चिमी विक्षोभ के कारण उत्तर-पश्चिमी उ.प्र. में हल्की से मध्यम वर्षा (वार्षिक वर्षा का <strong>3% से 5%</strong>, लगभग 10 सेमी) होती है, जिसे स्थानीय भाषा में <strong>'मावठ'</strong> कहते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Agricultural Significance:</strong> Winter rain acts as <em>liquid gold</em> for <strong>Rabi crops</strong>, crucially boosting the yield of <strong>Wheat (गेहूं), Barley (जौ), Mustard (सरसों), and Gram (चना)</strong>.</span>
      <span class="lang-hi"><strong>कृषि महत्व:</strong> यह शीतकालीन वर्षा <strong>रबी फसलों</strong> के लिए अमृत तुल्य होती है, जो विशेषकर <strong>गेहूं, जौ, सरसों व चना</strong> के दानों के विकास में अत्यंत सहायक सिद्ध होती है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Cold Waves &amp; Radiation Fog:</strong> Dense radiation fog (कोहरा) blankets the Indo-Gangetic plains during December-January, causing ground frost (पाला) that damages potato and mustard crops.</span>
      <span class="lang-hi"><strong>शीतलहर एवं घना कोहरा:</strong> दिसंबर-जनवरी में शांत हवाओं के कारण घना विकिरण कोहरा छाया रहता है, जिससे कभी-कभी 'पाला' (Frost) पड़ता है जो आलू और सरसों की फसल को हानि पहुंचाता है।</span>
    </li>
  </ul>
</div>

<!-- Card 6: Comprehensive 9 Agro-Climatic Zones Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. The 9 Agro-Climatic Zones of UP: Climate, Rainfall &amp; District Matrix</span>
    <span class="lang-hi">5. उ.प्र. के 9 कृषि-जलवायु क्षेत्र: जलवायु, वर्षा एवं जिला मैट्रिक्स</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Agro-Climatic Zone</span><span class="lang-hi">कृषि-जलवायु क्षेत्र</span></th>
          <th><span class="lang-en">Key Districts Included</span><span class="lang-hi">शामिल प्रमुख जिले</span></th>
          <th><span class="lang-en">Annual Rainfall</span><span class="lang-hi">वार्षिक वर्षा</span></th>
          <th><span class="lang-en">Climatic Characteristics</span><span class="lang-hi">जलवायु संबंधी विशेषताएं</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>1. Bhabhar &amp; Terai Zone</strong></span><span class="lang-hi"><strong>1. भाबर एवं तराई क्षेत्र</strong></span></td>
          <td><span class="lang-en">Saharanpur, Bijnor, Rampur, Bareilly, Pilibhit, Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, Siddharthnagar, Maharajganj, Kushinagar</span><span class="lang-hi">सहारनपुर, बिजनौर, रामपुर, बरेली, पीलीभीत, लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर, सिद्धार्थनगर, महराजगंज, कुशीनगर</span></td>
          <td><span class="lang-en">120 - 150 cm</span><span class="lang-hi">120 - 150 सेमी</span></td>
          <td><span class="lang-en">Heavy rainfall, high humidity, tall reed grasses, marshy terrain, moisture retention</span><span class="lang-hi">भारी वर्षा, अत्यधिक आर्द्रता, दलदली भूमि, सघन नमी, घने वन क्षेत्र</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>2. Western Plain Zone</strong></span><span class="lang-hi"><strong>2. पश्चिमी मैदानी क्षेत्र</strong></span></td>
          <td><span class="lang-en">Meerut, Bulandshahr, Ghaziabad, Gautam Buddha Nagar, Baghpat, Hapur, Muzaffarnagar</span><span class="lang-hi">मेरठ, बुलंदशहर, गाजियाबाद, गौतमबुद्ध नगर, बागपत, हापुड़, मुजफ्फरनगर</span></td>
          <td><span class="lang-en">65 - 80 cm</span><span class="lang-hi">65 - 80 सेमी</span></td>
          <td><span class="lang-en">Semi-humid to dry, severe hot summers, high tube-well irrigation density, sugarcane hub</span><span class="lang-hi">अर्ध-आर्द्र से शुष्क, गर्म ग्रीष्म, नलकूप सिंचाई की सघनता, गन्ना उत्पादक बेल्ट</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>3. Mid-Western Plain Zone</strong></span><span class="lang-hi"><strong>3. मध्य-पश्चिमी मैदानी क्षेत्र</strong></span></td>
          <td><span class="lang-en">Moradabad, Sambhal, Amroha, Badaun, Shahjahanpur</span><span class="lang-hi">मुरादाबाद, संभल, अमरोहा, बदायूं, शाहजहांपुर</span></td>
          <td><span class="lang-en">80 - 100 cm</span><span class="lang-hi">80 - 100 सेमी</span></td>
          <td><span class="lang-en">Transitional climate, fertile alluvial loam, moderate rainfall, winter frost spells</span><span class="lang-hi">संक्रमणकालीन जलवायु, उपजाऊ जलोढ़ दोमट, मध्यम वर्षा, शीतकालीन कोहरा</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>4. South-Western Semi-Arid Zone</strong></span><span class="lang-hi"><strong>4. दक्षिण-पश्चिमी अर्ध-शुष्क क्षेत्र</strong></span></td>
          <td><span class="lang-en">Agra, Mathura, Firozabad, Mainpuri, Etah, Aligarh, Hathras, Kasganj</span><span class="lang-hi">आगरा, मथुरा, फिरोजाबाद, मैनपुरी, एटा, अलीगढ़, हाथरस, कासगंज</span></td>
          <td><span class="lang-en">50 - 70 cm</span><span class="lang-hi">50 - 70 सेमी</span></td>
          <td><span class="lang-en">Lowest rainfall in state (Mathura 54.4 cm), intense summer heat (Agra 48°C+), ravines of Chambal</span><span class="lang-hi">राज्य में न्यूनतम वर्षा (मथुरा 54.4 सेमी), भीषण ग्रीष्म (आगरा 48°C+), चंबल के बीहड़, अर्ध-शुष्क परिस्थितियां</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>5. Central Plain Zone</strong></span><span class="lang-hi"><strong>5. मध्य मैदानी क्षेत्र</strong></span></td>
          <td><span class="lang-en">Lucknow, Kanpur Nagar, Kanpur Dehat, Unnao, Rae Bareli, Fatehpur, Sitapur, Hardoi</span><span class="lang-hi">लखनऊ, कानपुर नगर, कानपुर देहात, उन्नाव, रायबरेली, फतेहपुर, सीतापुर, हरदोई</span></td>
          <td><span class="lang-en">80 - 95 cm</span><span class="lang-hi">80 - 95 सेमी</span></td>
          <td><span class="lang-en">Representative Gangetic climate (Cwg), alkaline/usar soil patches, balanced agrarian regime</span><span class="lang-hi">विशिष्ट गंगा-तुल्य जलवायु (Cwg), ऊसर/रेह भूमि के चकत्ते, संतुलित कृषि प्रणाली</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>6. Bundelkhand Zone</strong></span><span class="lang-hi"><strong>6. बुंदेलखंड क्षेत्र</strong></span></td>
          <td><span class="lang-en">Jhansi, Lalitpur, Jalaun, Hamirpur, Mahoba, Banda, Chitrakoot (7 districts)</span><span class="lang-hi">झांसी, ललितपुर, जालौन, हमीरपुर, महोबा, बांदा, चित्रकूट (7 जिले)</span></td>
          <td><span class="lang-en">70 - 90 cm</span><span class="lang-hi">70 - 90 सेमी</span></td>
          <td><span class="lang-en">Extreme continental heat, high diurnal range, erratic rainfall, frequent drought cycles, black soil (Mar/Kabar)</span><span class="lang-hi">अत्यधिक ग्रीष्म ताप, उच्च दैनिक तापांतर, अनिश्चित वर्षा, बारंबार सूखा, काली मिट्टी (मार/काबर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>7. North-Eastern Plain Zone</strong></span><span class="lang-hi"><strong>7. उत्तर-पूर्वी मैदानी क्षेत्र</strong></span></td>
          <td><span class="lang-en">Gorakhpur, Deoria, Kushinagar, Maharajganj, Basti, Sant Kabir Nagar, Gonda</span><span class="lang-hi">गोरखपुर, देवरिया, कुशीनगर, महराजगंज, बस्ती, संत कबीर नगर, गोंडा</span></td>
          <td><span class="lang-en">100 - 130 cm</span><span class="lang-hi">100 - 130 सेमी</span></td>
          <td><span class="lang-en">Heavy monsoon rains (Gorakhpur 184.7 cm), riverine flooding (Ghaghara, Rapti, Gandak), sub-humid</span><span class="lang-hi">सघन मानसूनी वर्षा (गोरखपुर 184.7 सेमी), नदियों की बाढ़ (घाघरा, राप्ती, गंडक), उप-आर्द्र दशाएं</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>8. Eastern Plain Zone</strong></span><span class="lang-hi"><strong>8. पूर्वी मैदानी क्षेत्र</strong></span></td>
          <td><span class="lang-en">Varanasi, Jaunpur, Ghazipur, Azamgarh, Mau, Ballia, Ayodhya, Sultanpur, Ambedkar Nagar</span><span class="lang-hi">वाराणसी, जौनपुर, गाजीपुर, आजमगढ़, मऊ, बलिया, अयोध्या, सुल्तानपुर, अंबेडकर नगर</span></td>
          <td><span class="lang-en">95 - 115 cm</span><span class="lang-hi">95 - 115 सेमी</span></td>
          <td><span class="lang-en">High humidity, alluvial Khadar inundation, intensive multi-cropping, paddy dominance</span><span class="lang-hi">उच्च आर्द्रता, खादर बाढ़ कछार, सघन बहु-फसली कृषि, धान की प्रधानता</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>9. Vindhyan Zone</strong></span><span class="lang-hi"><strong>9. विंध्य क्षेत्र</strong></span></td>
          <td><span class="lang-en">Mirzapur, Sonbhadra, Southern Prayagraj (Trans-Yamuna plateau)</span><span class="lang-hi">मिर्जापुर, सोनभद्र, दक्षिणी प्रयागराज (यमुनापार पठारी भाग)</span></td>
          <td><span class="lang-en">100 - 115 cm</span><span class="lang-hi">100 - 115 सेमी</span></td>
          <td><span class="lang-en">Rocky plateau terrain, red gravelly soils, forested tracts, localized orographic rain, hot summers</span><span class="lang-hi">पहाड़ी-पठारी धरातल, लाल बजरीयुक्त मिट्टी, वनाच्छादित क्षेत्र, स्थानीय पर्वतीय वर्षा, गर्म ग्रीष्म</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 7: Seasonal Comparison Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Comparative Analysis of the Three Primary Seasons</span>
    <span class="lang-hi">6. तीनों प्रमुख ऋतुओं का तुलनात्मक विश्लेषण</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Meteorological Parameter</span><span class="lang-hi">मौसम संबंधी मानक</span></th>
          <th><span class="lang-en">Summer (ग्रीष्म ऋतु)</span><span class="lang-hi">ग्रीष्म ऋतु (Summer)</span></th>
          <th><span class="lang-en">Rainy (वर्षा ऋतु)</span><span class="lang-hi">वर्षा ऋतु (Monsoon)</span></th>
          <th><span class="lang-en">Winter (शीत ऋतु)</span><span class="lang-hi">शीत ऋतु (Winter)</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Active Duration</span><span class="lang-hi">सक्रिय अवधि</span></td>
          <td><span class="lang-en">March to Mid-June</span><span class="lang-hi">मार्च से मध्य-जून</span></td>
          <td><span class="lang-en">Mid-June to October</span><span class="lang-hi">मध्य-जून से अक्टूबर</span></td>
          <td><span class="lang-en">October to February</span><span class="lang-hi">अक्टूबर से फरवरी</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Average Max / Min Temp</span><span class="lang-hi">औसत अधिकतम / न्यूनतम ताप</span></td>
          <td><span class="lang-en">36°C - 39°C / 21°C - 23°C (Peak 48°C)</span><span class="lang-hi">36°C - 39°C / 21°C - 23°C (चरम 48°C)</span></td>
          <td><span class="lang-en">32°C - 34°C / 24°C - 26°C</span><span class="lang-hi">32°C - 34°C / 24°C - 26°C</span></td>
          <td><span class="lang-en">22°C - 28°C / 8°C - 10°C (Lowest 1-3°C)</span><span class="lang-hi">22°C - 28°C / 8°C - 10°C (न्यूनतम 1-3°C)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Prevailing Wind Direction</span><span class="lang-hi">हवाओं की मुख्य दिशा</span></td>
          <td><span class="lang-en">Westerly &amp; North-Westerly (Dry)</span><span class="lang-hi">पछुआ एवं उत्तर-पछुआ (शुष्क)</span></td>
          <td><span class="lang-en">Easterly &amp; South-Easterly ('Purva')</span><span class="lang-hi">पुरवैया (पूर्व एवं दक्षिण-पूर्व)</span></td>
          <td><span class="lang-en">North-Westerly (Cold &amp; Calm)</span><span class="lang-hi">उत्तर-पछुआ (शीतल एवं शांत)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Precipitation Share</span><span class="lang-hi">कुल वर्षा में हिस्सा</span></td>
          <td><span class="lang-en">Negligible (~1-2% Convectional showers)</span><span class="lang-hi">नगण्य (~1-2% संवहनीय बौछारें)</span></td>
          <td><span class="lang-en"><strong>80% - 85%</strong> (Primary Monsoon)</span><span class="lang-hi"><strong>80% - 85%</strong> (मुख्य मानसून)</span></td>
          <td><span class="lang-en"><strong>3% - 5%</strong> (Western Disturbances)</span><span class="lang-hi"><strong>3% - 5%</strong> (पश्चिमी विक्षोभ)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Defining Weather Phenomena</span><span class="lang-hi">विशिष्ट मौसमी घटनाएं</span></td>
          <td><span class="lang-en">Loo, Heatwaves, Dust Storms (आंधी)</span><span class="lang-hi">लू (Loo), लू के थपेड़े, धूल भरी आंधियां</span></td>
          <td><span class="lang-en">Monsoon Bursts, River Inundation, High Relative Humidity (&gt;75%)</span><span class="lang-hi">मानसूनी प्रस्फोट, नदीय बाढ़, उच्च सापेक्षिक आर्द्रता (&gt;75%)</span></td>
          <td><span class="lang-en">Radiation Fog, Cold Wave (Sheetlahar), Frost (पाला), Mahawat</span><span class="lang-hi">घना कोहरा, शीतलहर, पाला (Ground Frost), मावठ</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Beneficiary Crop Season</span><span class="lang-hi">लाभान्वित फसल चक्र</span></td>
          <td><span class="lang-en">Zaid crops (Watermelon, Cucumber, Fodder)</span><span class="lang-hi">जायद फसलें (तरबूज, खीरा, ककड़ी, चारा)</span></td>
          <td><span class="lang-en">Kharif crops (Paddy, Maize, Jowar, Bajra)</span><span class="lang-hi">खरीफ फसलें (धान, मक्का, ज्वार, बाजरा)</span></td>
          <td><span class="lang-en">Rabi crops (Wheat, Mustard, Barley, Gram)</span><span class="lang-hi">रबी फसलें (गेहूं, सरसों, जौ, चना)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 8: High-Yield One-Liner Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Rapid Revision Fact Matrix: UP Climate (Direct Exam Points)</span>
    <span class="lang-hi">7. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. की जलवायु (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Parameter</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / मानक</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">What is the broad climatic type of Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश की सामान्य जलवायु का प्रकार क्या है?</span></td>
          <td><span class="lang-en"><strong>Subtropical Humid Monsoon Climate (उष्णकटिबंधीय / उपोष्ण मानसूनी)</strong></span><span class="lang-hi"><strong>उपोष्ण मानसूनी / उष्णकटिबंधीय मानसूनी जलवायु</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which Koeppen climatic symbol represents Uttar Pradesh?</span><span class="lang-hi">कोपेन के अनुसार उ.प्र. किस जलवायु संकेत के अंतर्गत आता है?</span></td>
          <td><span class="lang-en"><strong>Cwg</strong> (Warm Temperate with Dry Winter and Hot Summer)</span><span class="lang-hi"><strong>Cwg</strong> (शुष्क शीत ऋतु युक्त गंगा-तुल्य जलवायु)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district receives the highest annual rainfall in UP?</span><span class="lang-hi">उ.प्र. में सर्वाधिक वार्षिक वर्षा किस जिले में होती है?</span></td>
          <td><span class="lang-en"><strong>Gorakhpur (184.7 cm)</strong> (approx. 56 rainy days)</span><span class="lang-hi"><strong>गोरखपुर (184.7 सेमी)</strong> (लगभग 56 वर्षा दिवस)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district receives the lowest annual rainfall in UP?</span><span class="lang-hi">उ.प्र. में न्यूनतम वार्षिक वर्षा किस जिले में होती है?</span></td>
          <td><span class="lang-en"><strong>Mathura (54.4 cm)</strong> (approx. 32 rainy days)</span><span class="lang-hi"><strong>मथुरा (54.4 सेमी)</strong> (लगभग 32 वर्षा दिवस)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which physical natural zone receives the highest rainfall?</span><span class="lang-hi">उ.प्र. का कौन सा प्राकृतिक भौतिक भाग सर्वाधिक वर्षा प्राप्त करता है?</span></td>
          <td><span class="lang-en"><strong>Bhabhar and Terai belt (120 cm - 150 cm)</strong></span><span class="lang-hi"><strong>भाबर एवं तराई क्षेत्र (120 से 150 सेमी)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which districts record the highest summer temperatures?</span><span class="lang-hi">ग्रीष्म ऋतु में सर्वाधिक तापमान किन जिलों में दर्ज होता है?</span></td>
          <td><span class="lang-en"><strong>Agra and Jhansi</strong> (crossing 48°C - 49°C)</span><span class="lang-hi"><strong>आगरा एवं झांसी</strong> (48°C से 49°C तक)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district records the lowest temperature in summer?</span><span class="lang-hi">ग्रीष्म ऋतु में सबसे कम तापमान किस जिले में रहता है?</span></td>
          <td><span class="lang-en"><strong>Bareilly</strong> (due to proximity to Himalayas)</span><span class="lang-hi"><strong>बरेली</strong> (हिमालय की तलहटी से निकटता के कारण)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which month is the coldest in Uttar Pradesh?</span><span class="lang-hi">उ.प्र. में वर्ष का सबसे ठंडा महीना कौन सा होता है?</span></td>
          <td><span class="lang-en"><strong>January</strong> (औसत न्यूनतम तापमान 3°C - 10°C)</span><span class="lang-hi"><strong>जनवरी</strong> (औसत न्यूनतम तापमान 3°C - 10°C)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the local name for the Bay of Bengal monsoon winds in UP?</span><span class="lang-hi">बंगाल की खाड़ी से आने वाली मानसूनी पवनों को उ.प्र. में क्या कहते हैं?</span></td>
          <td><span class="lang-en"><strong>Purva (पूर्वा / पुरवैया)</strong></span><span class="lang-hi"><strong>पूर्वा (पुरवैया)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What percentage of UP's rainfall is received during the Monsoon?</span><span class="lang-hi">उ.प्र. की कुल वर्षा का कितना प्रतिशत दक्षिण-पश्चिम मानसून से मिलता है?</span></td>
          <td><span class="lang-en"><strong>80% to 85%</strong> (July - September)</span><span class="lang-hi"><strong>80% से 85%</strong> (जुलाई - सितंबर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What causes winter rainfall in North-Western Uttar Pradesh?</span><span class="lang-hi">उत्तर-पश्चिमी उ.प्र. में शीतकालीन वर्षा का मुख्य कारण क्या है?</span></td>
          <td><span class="lang-en"><strong>Western Disturbances (पश्चिमी विक्षोभ)</strong> originating from Mediterranean Sea</span><span class="lang-hi">भूमध्य सागर से आने वाले <strong>पश्चिमी विक्षोभ</strong> (मावठ)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Winter rain in UP is exceptionally beneficial for which crop?</span><span class="lang-hi">शीतकालीन वर्षा उ.प्र. में किस फसल के लिए अमृत मानी जाती है?</span></td>
          <td><span class="lang-en"><strong>Rabi crops (particularly Wheat / गेहूं)</strong></span><span class="lang-hi"><strong>रबी फसल (विशेषकर गेहूं)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which directions does rainfall decrease across the state?</span><span class="lang-hi">राज्य में वर्षा की मात्रा किन दिशाओं में घटती है?</span></td>
          <td><span class="lang-en"><strong>From East to West</strong> and <strong>From North to South</strong></span><span class="lang-hi"><strong>पूर्व से पश्चिम</strong> की ओर तथा <strong>उत्तर से दक्षिण</strong> की ओर</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">How many Agro-Climatic Zones are demarcated in UP?</span><span class="lang-hi">उत्तर प्रदेश को कुल कितने कृषि-जलवायु क्षेत्रों में बांटा गया है?</span></td>
          <td><span class="lang-en"><strong>9 Agro-Climatic Zones (9 कृषि-जलवायु क्षेत्र)</strong></span><span class="lang-hi"><strong>9 कृषि-जलवायु क्षेत्र</strong> (योजना आयोग द्वारा संस्तुत)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which region records the highest diurnal temperature range?</span><span class="lang-hi">उ.प्र. के किस क्षेत्र में सर्वाधिक दैनिक तापांतर पाया जाता है?</span></td>
          <td><span class="lang-en"><strong>Bundelkhand Plateau region</strong> (14°C - 18°C)</span><span class="lang-hi"><strong>बुंदेलखंड पठारी क्षेत्र</strong> (14°C - 18°C)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "climate", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_climate_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
