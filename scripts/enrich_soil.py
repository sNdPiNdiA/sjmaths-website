import os
import re

def build_soil_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Comprehensive Soil Classification &amp; Geomorphic Zones of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की मिट्टियों का संपूर्ण वर्गीकरण एवं भू-आकृतिक क्षेत्र</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Soils of Uttar Pradesh] --> B[Bhabhar & Terai Zone]
    A --> C[Gangetic Alluvial Plain Soils]
    A --> D[Bundelkhand Black Soils]
    A --> E[Bundelkhand & Vindhyan Red Soils]
    A --> F[Problem Soils & Erosion Zones]

    B --> B1[Bhabhar: Coarse Pebbles, Gravel, High Porosity | Rivers Disappear]
    B --> B2[Terai: Marshy Silt Clay, Rich in Humus/N, Deficient in Zinc/P | Sugarcane, Paddy]

    C --> C1[Khadar: New Alluvium, Annual Floods, High Fertility, No Kankar]
    C --> C2[Bhangar: Old Alluvium, Calcareous Kankar Nodules, Uphar/Matiyar]
    C --> C3[Bhur: Sandy Wind-blown Ridges along River Terraces | Groundnut]

    D --> D1[Mar Soil: Deep Black Clay 60%+ Clay, High Moisture, Deep Cracks | Cotton, Wheat]
    D --> D2[Kabar Soil: Coarser Greyish-Black, Hardens like Brick when Dry | Gram, Oilseeds]

    E --> E1[Parwa/Padwa: Light Reddish Sandy-Loam, Fertile with Irrigation]
    E --> E2[Rakar: Sloping Gravelly Red Soil, Highly Eroded | Kodon, Kutki, Til]
    E --> E3[Bonta/Vindhyan: Weathered Granite-Sandstone | Mirzapur, Sonbhadra]

    F --> F1[Usar/Reh: Saline-Alkaline Soils ~10% Area | Reclaimed by Gypsum/Pyrite]
    F --> F2[Gully Erosion: Chambal & Yamuna Ravines | Etawah Worst Affected]
    F --> F3[Sheet Erosion: Silent Killer of Farming | Water & Wind Erosion]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की मृदा संपदा] --> B[भाबर एवं तराई क्षेत्र की मृदा]
    A --> C[गंगा के मैदानी जलोढ़ मृदा]
    A --> D[बुंदेलखंड की काली मृदा]
    A --> E[बुंदेलखंड व विंध्य की लाल मृदा]
    A --> F[समस्याग्रस्त मृदा एवं अपरदन]

    B --> B1[भाबर: कंकड़-पत्थर, बजरी, अत्यधिक छिद्रयुक्त | नदियां विलुप्त]
    B --> B2[तराई: दलदली बारीक गाद, ह्यूमस/नाइट्रोजन प्रचुर, जिंक/फास्फेट न्यून | गन्ना, धान]

    C --> C1[खादर: नवीन जलोढ़, बाढ़ द्वारा नवीनीकृत, अत्यधिक उपजाऊ, कंकड़ रहित]
    C --> C2[बांगर: पुरातन जलोढ़, चूनायुक्त कंकड़ ग्रंथियां, उपहार/मटियार दुमट]
    C --> C3[भूर: बलुई टीले, गंगा-यमुना तटवर्ती टीले | मूंगफली, बाजरा]

    D --> D1[मार मृदा: गहरी काली मृदा 60%+ क्ले, नमी सोखने वाली, गहरी दरारें | कपास, गेहूं]
    D --> D2[काबर मृदा: दानेदार धूसर-काली, सूखने पर ईंट जैसी कठोर | चना, तिलहन]

    E --> E1[परवा/पड़वा: हल्की लाल बलुई दोमट, सिंचाई से उपजाऊ | गेहूं, चना]
    E --> E2[राकर: ढालू कंकरीली लाल मृदा, क्षरणग्रस्त | कोदों, कुटकी, तिल]
    E --> E3[बोंटा/विंध्य: ग्रेनाइट-बलुआ पत्थर से निर्मित | मिर्जापुर, सोनभद्र]

    F --> F1[ऊसर/रेह: क्षारीय-लवणीय मृदा ~10% क्षेत्रफल | जिप्सम/पाइराइट से सुधार]
    F --> F2[अवनालिका अपरदन: चंबल व यमुना के बीहड़ | इटावा सर्वाधिक प्रभावित]
    F --> F3[परत अपरदन: किसान की मौत (धीमा जहर) | जल एवं वायु अपरदन]
    </div>
  </div>
</div>

<!-- Card 2: Bhabhar & Terai Soils -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Soils of the Northern Sub-Himalayan Belt: Bhabhar &amp; Terai Formations</span>
    <span class="lang-hi">1. उत्तरी उप-हिमालयी पट्टी की मृदा: भाबर एवं तराई संरचना</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Bhabhar Soil Belt (भाबर मृदा पेटी):</strong>
          <br>&bull; <em>Geomorphic Position:</em> Narrow strip (approx. 34 km wide in the west, tapering eastwards) running along the foothills of the Shivalik Himalayas.
          <br>&bull; <em>Texture &amp; Genesis:</em> Formed by alluvial fans of heavy boulders, pebbles, gravel, and coarse scree brought down by fast mountain streams.
          <br>&bull; <em>Subterranean Drainage:</em> Extremely porous and permeable; smaller mountain rivers and rivulets sink subterraneanly below the gravel beds and disappear from the surface.
          <br>&bull; <em>Agricultural Value:</em> Completely unsuitable for normal crop farming due to lack of fine topsoil; supports dense natural forests (Sal, Sheesham, Khair).
          <br>&bull; <em>Districts:</em> Northern fringes of Saharanpur, Bijnor, Lakhimpur Kheri, and Pilibhit.</span>
        <span class="lang-hi"><strong>भाबर मृदा पेटी:</strong>
          <br>&bull; <em>भू-आकृतिक स्थिति:</em> शिवालिक हिमालय की तलहटी के समानांतर पश्चिम से पूर्व की ओर फैली संकरी पट्टी (पश्चिम में ~34 किमी चौड़ी, पूर्व की ओर संकरी)।
          <br>&bull; <em>संरचना एवं उद्गम:</em> तीव्र वेग वाली पर्वतीय नदियों द्वारा निक्षेपित कंकड़-पत्थर, बजरी और मोटे बालू के जलोढ़ पंखों से निर्मित।
          <br>&bull; <em>भूमिगत जलप्रवाह:</em> अत्यधिक सरंध्रता (porosity) के कारण छोटी नदियां कंकड़ों के नीचे विलुप्त होकर भूगर्भ में बहती हैं।
          <br>&bull; <em>कृषि उपयोग:</em> बारीक उपजाऊ मृदा के अभाव के कारण सामान्य कृषि हेतु अनुपयुक्त; प्राकृतिक साल, शीशम एवं खैर के वनों से आच्छादित।
          <br>&bull; <em>विस्तार जिले:</em> सहारनपुर, बिजनौर, लखीमपुर खीरी एवं पीलीभीत के उत्तरी सीमांत भाग।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Terai Soil Belt (तराई मृदा पेटी):</strong>
          <br>&bull; <em>Geomorphic Position:</em> Lies immediately south of the Bhabhar belt; where subterranean streams re-emerge at the surface, creating marshy, poorly-drained swampy flood conditions.
          <br>&bull; <em>Texture &amp; Chemistry:</em> Rich, dark, fine silty-clay loam with heavy organic matter (humus) and high nitrogen content; <strong>deficient in phosphate (P) and zinc (Zn)</strong>.
          <br>&bull; <em>Agricultural Dominance:</em> Following post-independence reclamation (drainage of swamps), Terai has become one of the most productive agricultural belts of India, ideal for water-loving crops: <strong>Sugarcane (गन्ना), Paddy (धान), and Jute</strong>.
          <br>&bull; <em>Districts:</em> Pilibhit, Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, Siddharthnagar, Maharajganj, and Kushinagar.</span>
        <span class="lang-hi"><strong>तराई मृदा पेटी:</strong>
          <br>&bull; <em>भू-आकृतिक स्थिति:</em> भाबर के ठीक दक्षिण में स्थित; जहां भूमिगत हुई नदियां पुनः सतह पर प्रकट होती हैं, जिससे दलदली एवं जलभराव वाली नम भूमि बनती है।
          <br>&bull; <em>रासायनिक संगठन:</em> बारीक गाद एवं क्ले युक्त गहरी दोमट मृदा; ह्यूमस (जीवांश) एवं नाइट्रोजन की प्रचुरता; <strong>फास्फेट एवं जिंक की भारी कमी</strong>।
          <br>&bull; <em>कृषि महत्व:</em> स्वतंत्रता उपरांत दलदलों को सुखाकर इसे देश की सबसे उर्वर कृषि पट्टी में बदला गया; अत्यधिक जल चाहने वाली फसलों हेतु आदर्श: <strong>गन्ना, धान (चावल) तथा जूट</strong>।
          <br>&bull; <em>विस्तार जिले:</em> पीलीभीत, लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर, सिद्धार्थनगर, महाराजगंज एवं कुशीनगर।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Gangetic Plain Alluvial Soils - Khadar vs Bhangar -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Gangetic Alluvial Soils: Khadar (New Alluvium) vs Bhangar (Old Alluvium)</span>
    <span class="lang-hi">2. गंगा के मैदानी जलोढ़ मृदा: खादर (नवीन जलोढ़) बनाम बांगर (पुरातन जलोढ़)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Alluvial Stature:</strong> Alluvial soils cover approximately <strong>75% to 80% of the geographical area of Uttar Pradesh</strong>, deposited over millennia by the Ganga, Yamuna, Ghaghara, Saryu, Gandak, and Gomti river systems.</span>
        <span class="lang-hi"><strong>जलोढ़ मृदा का विस्तार:</strong> गंगा, यमुना, घाघरा, सरयू, गंडक एवं गोमती नदी प्रणालियों द्वारा निक्षेपित जलोढ़ मृदा उत्तर प्रदेश के लगभग <strong>75% से 80% भूभाग</strong> को आच्छादित करती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Khadar Soil (नवीन जलोढ़ / कछार):</strong>
          <br>&bull; <em>Location:</em> Low-lying active floodplains adjacent to river channels subject to recurring inundation during monsoon floods.
          <br>&bull; <em>Renewal Cycle:</em> Annually renewed by fresh deposits of silt and clay, requiring negligible artificial fertilizers.
          <br>&bull; <em>Texture &amp; Color:</em> Light-colored, porous, sandy-silt loam with superb aeration and high moisture-retention capacity.
          <br>&bull; <em>Chemical Nature:</em> Rich in potash, lime, and magnesium; lacks calcareous Kankar nodules.
          <br>&bull; <em>Local Names:</em> Kachhar (कछार), Bet (बेत), Naven (नवीन जलोढ़).</span>
        <span class="lang-hi"><strong>खादर मृदा (नवीन जलोढ़):</strong>
          <br>&bull; <em>स्थिति:</em> नदियों के निचले बाढ़ के मैदान जो प्रतिवर्ष मानसूनी बाढ़ द्वारा जलमग्न होते हैं।
          <br>&bull; <em>नवीनीकरण:</em> प्रतिवर्ष नदियों द्वारा लाई गई नवीन उपजाऊ गाद की परत जमती है, जिससे उर्वरता स्वतः बनी रहती है।
          <br>&bull; <em>संरचना व रंग:</em> हल्के रंग की, सरंध्र, बलुई गाद युक्त दोमट; उच्च जलधारण क्षमता एवं उत्कृष्ट वायु-संचार।
          <br>&bull; <em>रासायनिक तत्व:</em> पोटाश, चूना व मैग्नीशियम से युक्त; इसमें कंकड़ ग्रंथियां (Kankar nodules) नहीं पाई जातीं।
          <br>&bull; <em>स्थानीय नाम:</em> कछार, बेत, खादर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Bhangar Soil (पुरातन जलोढ़ / उपहार):</strong>
          <br>&bull; <em>Location:</em> Higher alluvial terraces situated above the modern flood levels where floodwaters never reach.
          <br>&bull; <em>Texture &amp; Color:</em> Darker, heavier clayey loam or clayey texture, often compacted in the subsoil layers.
          <br>&bull; <em>Diagnostic Marker:</em> Characterized by hard calcareous concretions of calcium carbonate called <strong>Kankar (कंकड़)</strong> formed in the subsoil profile.
          <br>&bull; <em>Chemical Nature:</em> Deficient in nitrogen, phosphorus, and organic matter; requires intensive irrigation and synthetic fertilizers (NPK) for high productivity.
          <br>&bull; <em>Local Names:</em> Uphar मृदा (उपहार), Matiyar (मटियार), Dumat (दुमट).</span>
        <span class="lang-hi"><strong>बांगर मृदा (पुरातन जलोढ़):</strong>
          <br>&bull; <em>स्थिति:</em> नदी घाटियों के ऊंचे चबूतरे जहां नदियों की वर्तमान बाढ़ का पानी कभी नहीं पहुंच पाता।
          <br>&bull; <em>संरचना व रंग:</em> गहरे पीले-भूरे रंग की, भारी मटियार दोमट या क्ले संरचना।
          <br>&bull; <em>पहचान लक्षण:</em> उप-सतह में कैल्शियम कार्बोनेट के जमाव से बनी कठोर ग्रंथियां, जिन्हें <strong>कंकड़</strong> कहा जाता है।
          <br>&bull; <em>रासायनिक स्थिति:</em> नाइट्रोजन, फास्फोरस एवं जीवांश की न्यूनता; उच्च पैदावार हेतु निरंतर सिंचाई एवं रासायनिक उर्वरकों (NPK) की आवश्यकता।
          <br>&bull; <em>स्थानीय नाम:</em> उपहार मृदा, मटियार, दोमट।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Problem Soils: Usar, Reh, Kallar & Reclamation -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Saline &amp; Alkaline Problem Soils: Reh, Usar, Kallar &amp; Reclamation</span>
    <span class="lang-hi">3. समस्याग्रस्त लवणीय एवं क्षारीय मृदा: रेह, ऊसर, कल्लर एवं भूमि सुधार</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Genesis &amp; Capillary Action (ऊसर मृदा का उद्भव):</strong>
          <br>&bull; In the semi-arid, flat terrain of Western and Central UP, excessive canal irrigation coupled with poor sub-soil drainage and high summer evaporation causes waterlogging.
          <br>&bull; Dissolved soluble salts of Sodium (Sodium carbonate Na2CO3, Sodium chloride NaCl, Sodium sulphate Na2SO4) are drawn to the surface via <strong>capillary action</strong>, leaving a glistening white powdery salt efflorescence called <strong>Reh (रेह)</strong>.
          <br>&bull; The soil becomes highly alkaline (pH > 8.5 to 10.0), impermeable, and biologically sterile.</span>
        <span class="lang-hi"><strong>उद्भव एवं केशिकत्व क्रिया (ऊसर का निर्माण):</strong>
          <br>&bull; पश्चिमी एवं मध्य उत्तर प्रदेश के समतल क्षेत्रों में अनियंत्रित नहरी सिंचाई, जल निकासी का अभाव एवं ग्रीष्म ऋतु में तीव्र वाष्पीकरण के कारण जलभराव होता है।
          <br>&bull; <strong>केशिकत्व क्रिया (Capillary action)</strong> द्वारा भूगर्भ के घुलनशील सोडियम लवण (सोडियम कार्बोनेट, क्लोराइड व सल्फेट) सतह पर आ जाते हैं, जिससे सफेद रंग की लवण परत जम जाती है जिसे <strong>रेह</strong> कहते हैं।
          <br>&bull; मृदा का पीएच (pH) मान 8.5 से 10.0 से अधिक हो जाता है, जिससे मिट्टी अनुपजाऊ व बंजर हो जाती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Spatial Extent &amp; Worst Affected Districts:</strong>
          <br>&bull; Approximately <strong>10% of UP's total agricultural area (~1.2 to 1.3 million hectares)</strong> is afflicted by salinity/alkalinity - the largest salt-affected area of any Indian state.
          <br>&bull; <em>Worst Afflicted Belt:</em> Aligarh, Mainpuri, Kanpur Nagar, Kanpur Dehat, Etawah, Auraiya, Unnao, Rae Bareli, Pratapgarh, Azamgarh, and Jaunpur.</span>
        <span class="lang-hi"><strong>विस्तार एवं सर्वाधिक प्रभावित जिले:</strong>
          <br>&bull; उत्तर प्रदेश के कुल कृषि क्षेत्रफल का लगभग <strong>10% भाग (~12 से 13 लाख हेक्टेयर)</strong> लवणीय-क्षारीय समस्या से ग्रस्त है - देश में सर्वाधिक ऊसर भूमि उत्तर प्रदेश में है।
          <br>&bull; <em>सर्वाधिक प्रभावित पट्टी:</em> अलीगढ़, मैनपुरी, कानपुर नगर, कानपुर देहात, इटावा, औरैया, उन्नाव, रायबरेली, प्रतापगढ़, आजमगढ़ एवं जौनपुर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Scientific Reclamation Measures (ऊसर सुधार के उपाय):</strong>
          <br>&bull; <em>Chemical Amendment:</em> Application of <strong>Gypsum (Calcium Sulphate - CaSO4·2H2O)</strong> to replace exchangeable sodium ions with calcium ions.
          <br>&bull; <em>Iron Pyrites (FeS2):</em> Mined in Sonbhadra/Mirzapur, pyrites form sulphuric acid in wet soil, neutralizing alkalinity.
          <br>&bull; <em>Green Manuring:</em> Cultivation and plowing of <strong>Dhaincha (Sesbania aculeata)</strong> and Sanai to restore organic humus and lower pH.
          <br>&bull; <em>Flushing &amp; Leaching (निक्षालन):</em> Flooding the field with fresh water and draining out saline dissolved surface runoff.</span>
        <span class="lang-hi"><strong>वैज्ञानिक सुधार के उपाय:</strong>
          <br>&bull; <em>रासायनिक सुधारक:</em> <strong>जिप्सम (कैल्शियम सल्फेट)</strong> का प्रयोग, जो मृदा के विनिमेय सोडियम को कैल्शियम से प्रतिस्थापित करता है।
          <br>&bull; <em>आयरन पाइराइट्स (FeS2):</em> सोनभद्र व मिर्जापुर से प्राप्त पाइराइट्स गीली मिट्टी में सल्फ्यूरिक अम्ल बनाकर क्षारीयता को उदासीन करता है।
          <br>&bull; <em>हरी खाद:</em> <strong>ढैंचा (सेसबेनिया)</strong> एवं सनई की बुवाई कर खेत में पलटना, जिससे जीवांश बढ़ता है और पीएच मान घटता है।
          <br>&bull; <em>निक्षालन (Leaching):</em> खेतों में पानी भरकर घुलनशील लवणों को जल निकासी नालियों द्वारा बाहर बहाना।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Bundelkhand Black Soils - Mar & Kabar -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Bundelkhand Black Soils: Mar &amp; Kabar Formations</span>
    <span class="lang-hi">4. बुंदेलखंड की काली मृदा: मार एवं काबर संरचनाएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Genesis:</strong> Derived from the weathering of ancient Deccan Trap volcanic basalts and iron-rich crystalline rocks extending into southern UP; locally known as <em>Kapas / Regur</em> soil.</span>
        <span class="lang-hi"><strong>उद्गम:</strong> दक्षिणी उत्तर प्रदेश में दक्कन ट्रैप की प्राचीन बेसाल्टिक ज्वालामुखीय चट्टानों के अपक्षय से विकसित; स्थानीय रूप से <em>कपास / रेगुर</em> मृदा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Mar Soil (मार / मांड मृदा):</strong>
          <br>&bull; <em>Texture:</em> Deep black, fine-grained heavy clay containing <strong>60% or more pure clay content</strong>.
          <br>&bull; <em>Signature Behavior:</em> Highly cohesive and sticky when wet; undergoes severe shrinkage upon drying, forming wide and deep polygonal fissures/cracks (self-ploughing soil).
          <br>&bull; <em>Moisture Capacity:</em> Outstanding water-holding capacity, allowing rabi crops to survive winter drought.
          <br>&bull; <em>Crops:</em> Highly suitable for Wheat (गेहूं), Gram (चना), Cotton (कपास), and Oilseeds.
          <br>&bull; <em>Districts:</em> Jalaun, Jhansi, Hamirpur, Mahoba, and Banda.</span>
        <span class="lang-hi"><strong>मार मृदा (मांड):</strong>
          <br>&bull; <em>संरचना:</em> गहरी काली, अत्यंत बारीक कणों वाली भारी क्ले मृदा, जिसमें <strong>60% से अधिक विशुद्ध क्ले</strong> होता है।
          <br>&bull; <em>पहचान लक्षण:</em> गीली होने पर अत्यधिक चिपचिपी; सूखने पर सिकुड़ कर इसमें चौड़ी व गहरी दरारें पड़ जाती हैं (स्वयं-जुताई वाली मिट्टी)।
          <br>&bull; <em>जलधारण:</em> असाधारण नमी संरक्षण क्षमता, जिससे बिना सिंचाई के भी शीतकालीन रबी फसलें तैयार हो जाती हैं।
          <br>&bull; <em>फसलें:</em> गेहूं, चना, कपास तथा तिलहन हेतु अत्यधिक उर्वर।
          <br>&bull; <em>विस्तार जिले:</em> जालौन, झांसी, हमीरपुर, महोबा एवं बांदा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Kabar Soil (काबर मृदा):</strong>
          <br>&bull; <em>Texture:</em> Coarser, dark grey to blackish clay-loam with less clay than Mar soil.
          <br>&bull; <em>Tillage Challenge:</em> Extremely temperamental; if ploughed too wet, it turns into unmanageable mud; if ploughed dry, it hardens into brick-like lumps.
          <br>&bull; <em>Crops:</em> Gram, Mustard, Jowar, Bajra, and Pulses.</span>
        <span class="lang-hi"><strong>काबर मृदा:</strong>
          <br>&bull; <em>संरचना:</em> मार की तुलना में कम क्ले युक्त, धूसर से गहरे काले रंग की खुरदरी दोमट-क्ले मृदा।
          <br>&bull; <em>जुताई की चुनौती:</em> अत्यंत संवेदनशील; अधिक नमी में दलदली हो जाती है और सूखने पर ईंट जैसी कठोर हो जाती है, अतः अनुकूल नमी में ही जुताई संभव।
          <br>&bull; <em>फसलें:</em> चना, सरसों, ज्वार, बाजरा एवं दलहन।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Bundelkhand & Vindhyan Red Soils - Parwa, Rakar & Bonta -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Bundelkhand &amp; Vindhyan Red Soils: Parwa, Rakar &amp; Bonta</span>
    <span class="lang-hi">5. बुंदेलखंड एवं विंध्य की लाल मृदा: परवा, राकर एवं बोंटा</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Genesis &amp; Chemical Core:</strong> Formed by the prolonged weathering and leaching of Archean granite and gneiss rocks; the distinctive reddish to yellowish-red coloration is caused by wide dissemination of <strong>Ferric Iron Oxides (Fe2O3)</strong>. Deficient in nitrogen, phosphorus, humus, and lime.</span>
        <span class="lang-hi"><strong>उद्गम एवं रासायनिक आधार:</strong> आर्कियन युगीन ग्रेनाइट एवं नीस चट्टानों के अपक्षय से निर्मित; मृदा का लाल रंग <strong>फेरिक आयरन ऑक्साइड (लौह तत्व)</strong> के व्यापक प्रसार के कारण होता है। इसमें नाइट्रोजन, फास्फोरस, ह्यूमस एवं चूने की न्यूनता होती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Parwa / Padwa Soil (परवा / पड़वा मृदा):</strong>
          <br>&bull; <em>Texture:</em> Light reddish-brown sandy loam or fine sandy silt; porous, friable, and well-drained.
          <br>&bull; <em>Fertility:</em> Possesses moderate fertility; produces excellent yields of Wheat, Gram, Mustard, and Jowar when supported by assured tubewell or canal irrigation.
          <br>&bull; <em>Districts:</em> Hamirpur, Jalaun (especially along the Yamuna and Betwa belts), and northern Jhansi.</span>
        <span class="lang-hi"><strong>परवा / पड़वा मृदा:</strong>
          <br>&bull; <em>संरचना:</em> हल्के लाल-भूरे रंग की बलुई दोमट या बारीक रेतीली गाद; सरंध्र, भुरभुरी एवं उत्तम जल निकासी युक्त।
          <br>&bull; <em>उर्वरता:</em> मध्यम उर्वरता; यदि नलकूप या नहर द्वारा सिंचाई उपलब्ध हो तो गेहूं, चना, सरसों एवं ज्वार की उत्तम पैदावार देती है।
          <br>&bull; <em>विस्तार जिले:</em> हमीरपुर, जालौन (विशेषकर यमुना व बेतवा नदी तटवर्ती क्षेत्र) एवं उत्तरी झांसी।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Rakar Soil (राकर मृदा):</strong>
          <br>&bull; <em>Characteristics:</em> Extremely coarse, gravelly red soil found on undulating hill slopes, barren ridges, and denuded plateau scarps.
          <br>&bull; <em>Variants:</em> Moti Rakar (stony, uncultivable) and Patli Rakar (shallow gravelly).
          <br>&bull; <em>Agricultural Utility:</em> Highly prone to sheet wash erosion with virtually zero water retention; cultivable only during the monsoon for hardy drought-resistant coarse millets: <strong>Kodon, Kutki, Til (Sesame), and Jowar</strong>.
          <br>&bull; <em>Districts:</em> Southern parts of Jhansi, Lalitpur, Banda, and Chitrakoot.</span>
        <span class="lang-hi"><strong>राकर मृदा:</strong>
          <br>&bull; <em>विशेषताएं:</em> उबड़-खाबड़ पहाड़ी ढलानों, टीलों और पठारी कगारों पर पाई जाने वाली अत्यंत खुरदरी, कंकरीली लाल मृदा।
          <br>&bull; <em>प्रकार:</em> मोटी राकर (पत्थरीली, बंजर) एवं पतली राकर (छिछली कंकरीली)।
          <br>&bull; <em>कृषि उपयोग:</em> तीव्र जल क्षरण और शून्य जलधारण क्षमता; केवल मानसूनी वर्षा में कम पानी चाहने वाले मोटे अनाजों हेतु प्रयुक्त: <strong>कोदों, कुटकी, तिल एवं ज्वार</strong>।
          <br>&bull; <em>विस्तार जिले:</em> झांसी, ललितपुर, बांदा एवं चित्रकूट के दक्षिणी पहाड़ी भाग।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Bonta &amp; Vindhyan Soils (बोंटा एवं विंध्य मृदा):</strong>
          <br>&bull; <em>Occurrence:</em> Spread across the Vindhyan escarpments of <strong>Mirzapur, Sonbhadra, and southern Chandauli</strong>.
          <br>&bull; <em>Characteristics:</em> Shallow reddish-yellow stony soils deficient in nutrients, supporting scrub vegetation and rainfed subsistence cultivation.</span>
        <span class="lang-hi"><strong>बोंटा एवं विंध्य मृदा:</strong>
          <br>&bull; <em>विस्तार:</em> <strong>मिर्जापुर, सोनभद्र एवं दक्षिणी चंदौली</strong> के विंध्य पर्वतीय कगारों पर विस्तृत।
          <br>&bull; <em>विशेषताएं:</em> पोषक तत्वों से विहीन, छिछली लाल-पीली पथरीली मिट्टी, जहां कंटीली झाड़ियां एवं मानसूनी मोटे अनाज उगाए जाते हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Specialized Soils: Bhur & Ravine Badlands -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Specialized Soils: Bhur Sand Ridges &amp; Chambal Ravine Badlands</span>
    <span class="lang-hi">6. विशिष्ट मृदाएं: भूर (रेतीले टीले) एवं चंबल के बीहड़ (अवनालिका क्षरण)</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Bhur Soils (भूर मृदा):</strong>
          <br>&bull; <em>Formation:</em> Elevated undulating sandy mounds (10 to 20 feet high) created by wind action and abandoned river meanders along the flood terraces of the Ganga and its tributaries during the Holocene epoch.
          <br>&bull; <em>Soil Quality:</em> 80% to 90% coarse sand; very low nutrient content and deficient moisture retention.
          <br>&bull; <em>Crops:</em> Groundnut (मूंगफली), Bajra, Watermelon, and Muskmelon.
          <br>&bull; <em>Districts:</em> Moradabad, Bijnor, Sambhal, Amroha, Budaun, Shahjahanpur, and Farrukhabad.</span>
        <span class="lang-hi"><strong>भूर मृदा:</strong>
          <br>&bull; <em>उद्भव:</em> गंगा एवं उसकी सहायक नदियों के पुराने प्रवाह मार्गों व तटवर्ती चबूतरों पर वायु द्वारा निर्मित 10 से 20 फीट ऊंचे रेतीले टीले।
          <br>&bull; <em>मृदा गुण:</em> 80% से 90% तक बालू; न्यूनतम पोषक तत्व एवं नगण्य जलधारण क्षमता।
          <br>&bull; <em>फसलें:</em> मूंगफली, बाजरा, तरबूज, खरबूजा एवं खीरा।
          <br>&bull; <em>विस्तार जिले:</em> मुरादाबाद, बिजनौर, संभल, अमरोहा, बदायूं, शाहजहांपुर एवं फर्रुखाबाद।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Chambal &amp; Yamuna Ravine Badlands (बीहड़ / खड्ड मृदा):</strong>
          <br>&bull; <em>Gully Erosion Phenomenon:</em> Caused by violent torrential monsoon runoff cutting deep, vertical chasm-like ravines into soft alluvial soil along the Chambal, Yamuna, Betwa, and Ken river valleys.
          <br>&bull; <em>Worst Affected District:</em> <strong>Etawah</strong> (epicenter of gully erosion in UP), followed by Agra, Auraiya, and Jalaun.
          <br>&bull; <em>Remediation:</em> Afforestation under social forestry schemes, construction of earthen check dams, and contour bunding.</span>
        <span class="lang-hi"><strong>चंबल एवं यमुना के बीहड़ (अवनालिका क्षरण):</strong>
          <br>&bull; <em>अवनालिका अपरदन:</em> चंबल, यमुना, बेतवा व केन नदियों के किनारों पर तीव्र मानसूनी बहाव द्वारा गहरी, खड़ी घाटियों और बीहड़ों का निर्माण।
          <br>&bull; <em>सर्वाधिक प्रभावित जिला:</em> <strong>इटावा</strong> (उत्तर प्रदेश में अवनालिका अपरदन का मुख्य केंद्र), तत्पश्चात आगरा, औरैया एवं जालौन।
          <br>&bull; <em>उपचार:</em> सामाजिक वानिकी, चेक डैम निर्माण, समोच्च मेड़बंदी एवं बबूल-शीशम का वृक्षारोपण।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Soil Erosion, Degradation & Reclamation Programs -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Soil Erosion Dynamics, Degradation &amp; Conservation Programs in UP</span>
    <span class="lang-hi">7. उत्तर प्रदेश में मृदा अपरदन, क्षरण एवं संरक्षण कार्यक्रम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Types of Soil Erosion in UP:</strong>
          <br>&bull; <em>Sheet Erosion (परत अपरदन - 'Scourge of the Farmer' / 'किसान की मौत'):</em> Gradual, invisible removal of the nutrient-rich topsoil layer across vast Gangetic plains by rainwater runoff; termed "silent theft of fertility".
          <br>&bull; <em>Gully Erosion (अवनालिका अपरदन):</em> Deep incision of drainage channels leading to barren badlands in the Chambal and Yamuna basins (Etawah, Agra).
          <br>&bull; <em>Wind Erosion (वायु अपरदन):</em> High wind-blown sand movement during hot summer Loo months in arid Western UP (Agra, Mathura, Firozabad).</span>
        <span class="lang-hi"><strong>मृदा अपरदन के प्रमुख प्रकार:</strong>
          <br>&bull; <em>परत अपरदन ('किसान की मौत' / धीमा जहर):</em> मानसूनी वर्षा जल द्वारा गंगा के समतल मैदानों की ऊपरी अत्यंत उपजाऊ बारीक परत का धीरे-धीरे बह जाना; इसे 'अदृश्य अपरदन' भी कहा जाता है।
          <br>&bull; <em>अवनालिका अपरदन:</em> चंबल व यमुना घाटियों (इटावा, आगरा) में गहरी खाइयों व बीहड़ों का बनना।
          <br>&bull; <em>वायु अपरदन:</em> ग्रीष्म ऋतु में 'लू' पवनों द्वारा पश्चिमी उत्तर प्रदेश (आगरा, मथुरा) की बलुई मृदा का उड़ना।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Major State Conservation Schemes:</strong>
          <br>&bull; <em>Soil Health Card Scheme (मृदा स्वास्थ्य कार्ड):</em> Evaluates 12 soil parameters (N, P, K, S, Zn, Fe, Cu, Mn, Bo, pH, EC, OC) to prevent fertilizer over-application.
          <br>&bull; <em>UP Bhumi Sudhar Nigam (उत्तर प्रदेश भूमि सुधार निगम):</em> Established in <strong>1978</strong>; successfully reclaimed over 5 lakh hectares of sodic and Usar land under World Bank-assisted Sodic Lands Reclamation Projects.
          <br>&bull; <em>Dhaincha Seed Subsidy Scheme:</em> Promotes biological green manuring across salt-affected blocks of UP.</span>
        <span class="lang-hi"><strong>प्रमुख राज्य संरक्षण एवं सुधार योजनाएं:</strong>
          <br>&bull; <em>मृदा स्वास्थ्य कार्ड योजना:</em> रासायनिक उर्वरकों के अंधाधुंध प्रयोग को रोकने हेतु 12 पोषक मापदंडों का मृदा परीक्षण।
          <br>&bull; <em>उत्तर प्रदेश भूमि सुधार निगम:</em> स्थापना <strong>1978</strong>; विश्व बैंक पोषित ऊसर सुधार परियोजनाओं के तहत 5 लाख हेक्टेयर से अधिक बंजर/क्षारीय भूमि का सफल उपचार।
          <br>&bull; <em>ढैंचा बीज अनुदान योजना:</em> क्षारीयता प्रभावित विकास खंडों में जैविक हरी खाद हेतु 90% तक अनुदान।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 9: Master Comparison Table of UP Soil Types -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Master Comparison Table: Soil Classification of Uttar Pradesh</span>
    <span class="lang-hi">8. उत्तर प्रदेश की मिट्टियों की संपूर्ण तुलना तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Soil Type</span>
            <span class="lang-hi">मिट्टी का प्रकार</span>
          </th>
          <th>
            <span class="lang-en">Geographic Belt / Districts</span>
            <span class="lang-hi">भौगोलिक पट्टी / जिले</span>
          </th>
          <th>
            <span class="lang-en">Physical &amp; Chemical Attributes</span>
            <span class="lang-hi">भौतिक व रासायनिक विशेषताएं</span>
          </th>
          <th>
            <span class="lang-en">Prime Crops &amp; Local Names</span>
            <span class="lang-hi">प्रमुख फसलें एवं स्थानीय नाम</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en"><strong>Bhabhar</strong> (भाबर)</span>
            <span class="lang-hi"><strong>भाबर</strong></span>
          </td>
          <td>
            <span class="lang-en">Saharanpur, Bijnor, Lakhimpur, Pilibhit</span>
            <span class="lang-hi">सहारनपुर, बिजनौर, लखीमपुर, पीलीभीत</span>
          </td>
          <td>
            <span class="lang-en">Boulders, coarse pebbles, dry surface; subterranean streams</span>
            <span class="lang-hi">कंकड़-पत्थर, बजरी; भूमिगत नदी प्रवाह; शुष्क ऊपरी सतह</span>
          </td>
          <td>
            <span class="lang-en">Unfit for farming; Sal &amp; Sheesham forests</span>
            <span class="lang-hi">कृषि अनुपयुक्त; साल व शीशम के सघन वन</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Terai</strong> (तराई)</span>
            <span class="lang-hi"><strong>तराई</strong></span>
          </td>
          <td>
            <span class="lang-en">Pilibhit, Lakhimpur, Bahraich, Siddharthnagar, Maharajganj</span>
            <span class="lang-hi">पीलीभीत, लखीमपुर, बहराइच, सिद्धार्थनगर, महाराजगंज</span>
          </td>
          <td>
            <span class="lang-en">Marshy silt clay, rich humus &amp; N; deficient in Zinc &amp; P</span>
            <span class="lang-hi">दलदली गाद क्ले, ह्यूमस व N प्रचुर; जिंक व फास्फेट न्यून</span>
          </td>
          <td>
            <span class="lang-en">Sugarcane, Paddy, Jute</span>
            <span class="lang-hi">गन्ना, धान (चावल), जूट</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Khadar</strong> (नवीन जलोढ़)</span>
            <span class="lang-hi"><strong>खादर</strong></span>
          </td>
          <td>
            <span class="lang-en">Low-lying active floodplains of Ganga, Yamuna, Ghaghara</span>
            <span class="lang-hi">गंगा, यमुना, घाघरा के निचले बाढ़ के मैदान</span>
          </td>
          <td>
            <span class="lang-en">Annually renewed fertile silt; no Kankar nodules; high moisture</span>
            <span class="lang-hi">प्रतिवर्ष नवीनीकृत गाद; कंकड़ रहित; उच्च जलधारण</span>
          </td>
          <td>
            <span class="lang-en">Vegetables, Pulses, Wheat, Maize (Kachhar/Bet)</span>
            <span class="lang-hi">सब्जियां, दलहन, गेहूं, मक्का (कछार/बेत)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Bhangar</strong> (पुरातन जलोढ़)</span>
            <span class="lang-hi"><strong>बांगर</strong></span>
          </td>
          <td>
            <span class="lang-en">Upper upland terraces of Gangetic Plain</span>
            <span class="lang-hi">गंगा के मैदान के ऊंचे चबूतरे</span>
          </td>
          <td>
            <span class="lang-en">Clayey loam; calcareous Kankar concretions; needs NPK</span>
            <span class="lang-hi">मटियार दोमट; चूनेदार कंकड़ ग्रंथियां; NPK उर्वरक आवश्यक</span>
          </td>
          <td>
            <span class="lang-en">Wheat, Sugarcane, Pulses (Uphar/Dumat)</span>
            <span class="lang-hi">गेहूं, गन्ना, दलहन (उपहार/दोमट)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Usar / Reh</strong> (ऊसर)</span>
            <span class="lang-hi"><strong>ऊसर / रेह</strong></span>
          </td>
          <td>
            <span class="lang-en">Aligarh, Mainpuri, Kanpur, Unnao, Etawah, Rae Bareli</span>
            <span class="lang-hi">अलीगढ़, मैनपुरी, कानपुर, उन्नाव, इटावा, रायबरेली</span>
          </td>
          <td>
            <span class="lang-en">Alkaline white salt crust (pH 8.5-10); capillary action</span>
            <span class="lang-hi">सफेद क्षारीय लवण परत (pH 8.5-10); केशिकत्व क्रिया</span>
          </td>
          <td>
            <span class="lang-en">Barren until reclaimed by Gypsum/Pyrite (Kallar/Reh)</span>
            <span class="lang-hi">बंजर; जिप्सम/पाइराइट से सुधार उपरांत धान (कल्लर)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Mar</strong> (मार / मांड)</span>
            <span class="lang-hi"><strong>मार</strong></span>
          </td>
          <td>
            <span class="lang-en">Jalaun, Jhansi, Hamirpur, Mahoba, Banda</span>
            <span class="lang-hi">जालौन, झांसी, हमीरपुर, महोबा, बांदा</span>
          </td>
          <td>
            <span class="lang-en">Deep black clay (60%+ clay); sticky wet, deep cracks dry</span>
            <span class="lang-hi">गहरी काली क्ले (60%+ क्ले); गीली में चिपचिपी, सूखने पर दरारें</span>
          </td>
          <td>
            <span class="lang-en">Cotton, Gram, Wheat, Oilseeds (Regur)</span>
            <span class="lang-hi">कपास, चना, गेहूं, तिलहन (रेगुर)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Kabar</strong> (काबर)</span>
            <span class="lang-hi"><strong>काबर</strong></span>
          </td>
          <td>
            <span class="lang-en">Bundelkhand plateau tract</span>
            <span class="lang-hi">बुंदेलखंड पठारी क्षेत्र</span>
          </td>
          <td>
            <span class="lang-en">Dark grey clay-loam; hardens like brick upon drying</span>
            <span class="lang-hi">धूसर-काली दोमट-क्ले; सूखने पर ईंट समान कठोर</span>
          </td>
          <td>
            <span class="lang-en">Gram, Mustard, Jowar</span>
            <span class="lang-hi">चना, सरसों, ज्वार</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Parwa</strong> (परवा / पड़वा)</span>
            <span class="lang-hi"><strong>परवा</strong></span>
          </td>
          <td>
            <span class="lang-en">Hamirpur, Jalaun, northern Jhansi</span>
            <span class="lang-hi">हमीरपुर, जालौन, उत्तरी झांसी</span>
          </td>
          <td>
            <span class="lang-en">Light reddish sandy loam; friable, well-aerated</span>
            <span class="lang-hi">हल्की लाल बलुई दोमट; भुरभुरी, हवादार</span>
          </td>
          <td>
            <span class="lang-en">Wheat, Gram, Mustard with irrigation</span>
            <span class="lang-hi">सिंचाई द्वारा गेहूं, चना, सरसों</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Rakar</strong> (राकर)</span>
            <span class="lang-hi"><strong>राकर</strong></span>
          </td>
          <td>
            <span class="lang-en">Southern Jhansi, Lalitpur, Banda, Chitrakoot</span>
            <span class="lang-hi">दक्षिणी झांसी, ललितपुर, बांदा, चित्रकूट</span>
          </td>
          <td>
            <span class="lang-en">Coarse gravelly red soil on hill slopes; zero moisture</span>
            <span class="lang-hi">पहाड़ी ढलानों पर कंकरीली लाल मृदा; शून्य जलधारण</span>
          </td>
          <td>
            <span class="lang-en">Kodon, Kutki, Til, Jowar</span>
            <span class="lang-hi">कोदों, कुटकी, तिल, ज्वार</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 10: Rapid Revision Matrix & UPSSSC Exam Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">9. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">9. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Exam Question / Trap</span>
            <span class="lang-hi">परीक्षा प्रश्न / ट्रैप</span>
          </th>
          <th>
            <span class="lang-en">Precision Answer &amp; Strategic Fact</span>
            <span class="lang-hi">सटीक उत्तर एवं महत्वपूर्ण तथ्य</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Kankar Nodules Found in</span>
            <span class="lang-hi">कंकड़ ग्रंथियां किसमें पाई जाती हैं</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bhangar Soil (Old Alluvium)</strong> (Trap: Never in Khadar).</span>
            <span class="lang-hi"><strong>बांगर मृदा (पुरातन जलोढ़)</strong> (ट्रैप: खादर में कभी नहीं)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">District with Most Gully Erosion</span>
            <span class="lang-hi">सर्वाधिक अवनालिका अपरदन वाला जिला</span>
          </td>
          <td>
            <span class="lang-en"><strong>Etawah</strong> (along Chambal and Yamuna river valleys).</span>
            <span class="lang-hi"><strong>इटावा</strong> (चंबल एवं यमुना नदी घाटियों में)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Soil Termed "Death of the Farmer"</span>
            <span class="lang-hi">'किसान की मौत' कहा जाने वाला अपरदन</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sheet Erosion (परत अपरदन)</strong> (silent removal of fertile topsoil).</span>
            <span class="lang-hi"><strong>परत अपरदन</strong> (उपजाऊ ऊपरी परत का धीमा अदृश्य क्षरण)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chemical Used for Usar Reclamation</span>
            <span class="lang-hi">ऊसर सुधार हेतु प्रयुक्त रसायन</span>
          </td>
          <td>
            <span class="lang-en"><strong>Gypsum (CaSO4·2H2O)</strong> and <strong>Iron Pyrites (FeS2)</strong>.</span>
            <span class="lang-hi"><strong>जिप्सम (कैल्शियम सल्फेट)</strong> तथा <strong>आयरन पाइराइट्स</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">State with Most Salt-Affected Soil</span>
            <span class="lang-hi">सर्वाधिक लवणीय-क्षारीय मृदा वाला राज्य</span>
          </td>
          <td>
            <span class="lang-en"><strong>Uttar Pradesh</strong> (~1.2 to 1.3 million hectares, ~10% area).</span>
            <span class="lang-hi"><strong>उत्तर प्रदेश</strong> (~12 से 13 लाख हेक्टेयर, ~10% कृषि क्षेत्र)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Terai Soils are Deficient in</span>
            <span class="lang-hi">तराई मृदा में किसकी कमी होती है</span>
          </td>
          <td>
            <span class="lang-en"><strong>Phosphate (P) and Zinc (Zn)</strong> (while rich in Nitrogen and Humus).</span>
            <span class="lang-hi"><strong>फास्फेट एवं जिंक</strong> (जबकि नाइट्रोजन एवं ह्यूमस प्रचुर हैं)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Red Color of Bundelkhand Soils Due to</span>
            <span class="lang-hi">बुंदेलखंड की लाल मृदा का रंग किसके कारण</span>
          </td>
          <td>
            <span class="lang-en">Diffusion of <strong>Ferric Iron Oxides (Fe2O3)</strong>.</span>
            <span class="lang-hi"><strong>फेरिक आयरन ऑक्साइड (लौह ऑक्साइड)</strong> के प्रसार के कारण।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">UP Bhumi Sudhar Nigam Est. Year</span>
            <span class="lang-hi">यूपी भूमि सुधार निगम स्थापना वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>1978</strong>.</span>
            <span class="lang-hi"><strong>1978</strong>.</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "soil", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_soil_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
