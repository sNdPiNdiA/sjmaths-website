import os
import re
from bs4 import BeautifulSoup

def build_agriculture_theory_html():
    return """
<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Agriculture of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की कृषि</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Agriculture of UP] --> B[Ranks & Production]
    A --> C[Agro-Climatic Zones - 9]
    A --> D[Major Crops & Districts]
    A --> E[Horticulture & AEZ]
    A --> F[Irrigation Network]
    A --> G[Institutes & Universities]
    A --> H[Livestock & Dairy]
    A --> I[Key Schemes & Reforms]

    B --> B1[Rank 1: Foodgrains, Wheat, Sugarcane, Potato, Milk, Aonla, Guava, Mentha]
    B --> B2[Rank 2: Rice, Total Vegetables]
    B --> B3[Rank 3: Total Pulses]

    C --> C1[Tarai & Western Plains]
    C --> C2[Mid-Western & South-Western Semi-Arid]
    C --> C3[Central & Bundelkhand]
    C --> C4[North-Eastern, Eastern & Vindhyan]

    D --> D1[Wheat: Gorakhpur, Hardoi, Meerut]
    D --> D2[Paddy: Chandauli Rice Bowl, Siddharthnagar Kalanamak]
    D --> D3[Sugarcane: Muzaffarnagar, Meerut, Lakhimpur]
    D --> D4[Potato: Agra Taj Brand, Farrukhabad]
    D --> D5[Pulses: Bundelkhand Chana hub]
    D --> D6[Opium: Ghazipur Factory, Barabanki Cultivation]

    E --> E1[Mango: Malihabad Dussehri, Nawab Brand]
    E --> E2[Aonla: Pratapgarh Capital]
    E --> E3[Guava: Prayagraj Surkha GI]
    E --> E4[3 AEZ: Agra, Lucknow, Saharanpur]

    F --> F1[Tubewells: 73.4% - First Meerut 1930]
    F --> F2[Canals: 15.2% - Sharda Longest 12368 km]
    F --> F3[Ken-Betwa Interlink & Saryu Nahar]

    G --> G1[Central: IISR, CISH, IIVR, IIPR, IVRI, IGFRI]
    G --> G2[4 State SAUs + 1 Central RLBCAU + SHUATS 1910]

    H --> H1[Rank 1 Livestock & Milk]
    H --> H2[First Milk Union: Lucknow 1938]
    H --> H3[Nand Baba Mission & Parag PCDF 1962]

    I --> I1[Chakbandi: 1954 Muzaffarnagar/Sultanpur]
    I --> I2[Kisan Bahi: 1992 | KCC: 1999]
    I --> I3[PM-KISAN: Launched Gorakhpur 2019]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की कृषि] --> B[रैंकिंग एवं उत्पादन]
    A --> C[9 कृषि-जलवायु क्षेत्र]
    A --> D[प्रमुख फसलें एवं जिले]
    A --> E[बागवानी एवं AEZ]
    A --> F[सिंचाई नेटवर्क]
    A --> G[संस्थान एवं विश्वविद्यालय]
    A --> H[पशुपालन एवं दुग्ध विकास]
    A --> I[प्रमुख योजनाएँ एवं सुधार]

    B --> B1[प्रथम: कुल खाद्यान्न, गेहूँ, गन्ना, आलू, दूध, आँवला, अमरूद, मेंथा]
    B --> B2[द्वितीय: धान, कुल सब्जियां]
    B --> B3[तृतीय: कुल दलहन]

    C --> C1[तराई एवं पश्चिमी मैदान]
    C --> C2[मध्य-पश्चिमी एवं दक्षिण-पश्चिमी अर्ध-शुष्क]
    C --> C3[केंद्रीय मैदान एवं बुंदेलखंड]
    C --> C4[उत्तर-पूर्वी, पूर्वी एवं विंध्य क्षेत्र]

    D --> D1[गेहूँ: गोरखपुर, हरदोई, मेरठ]
    D --> D2[धान: चंदौली कटोरा, सिद्धार्थनगर कालानमक]
    D --> D3[गन्ना: मुजफ्फरनगर, मेरठ, लखीमपुर]
    D --> D4[आलू: आगरा ताज ब्रांड, फर्रुखाबाद]
    D --> D5[दलहन: बुंदेलखंड चना हब]
    D --> D6[अफीम: गाजीपुर फैक्ट्री, बाराबंकी खेती]

    E --> E1[आम: मलीहाबाद दशहरी, नवाब ब्रांड]
    E --> E2[आँवला: प्रतापगढ़ राजधानी]
    E --> E3[अमरूद: प्रयागराज सुरखा GI]
    E --> E4[3 AEZ: आगरा, लखनऊ, सहारनपुर]

    F --> F1[नलकूप: 73.4% - प्रथम मेरठ 1930]
    F --> F2[नहरें: 15.2% - शारदा सबसे लंबी 12368 किमी]
    F --> F3[केन-बेतवा लिंक एवं सरयू नहर परियोजना]

    G --> G1[केंद्रीय: IISR, CISH, IIVR, IIPR, IVRI, IGFRI]
    G --> G2[4 राज्य वि.वि. + 1 केंद्रीय RLBCAU + SHUATS 1910]

    H --> H1[प्रथम: कुल पशुधन एवं दुग्ध उत्पादन]
    H --> H2[प्रथम दुग्ध संघ: लखनऊ 1938]
    H --> H3[नंद बाबा मिशन एवं पराग PCDF 1962]

    I --> I1[चकबंदी: 1954 मुजफ्फरनगर/सुल्तानपुर]
    I --> I2[किसान बही: 1992 | KCC: 1999]
    I --> I3[PM-किसान: गोरखपुर से शुभारंभ 2019]
    </div>
  </div>
</div>

<!-- Card 2: National Rankings & Core Agricultural Statistics -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. National Rankings & Land Statistics of UP Agriculture</span>
    <span class="lang-hi">1. उत्तर प्रदेश कृषि की राष्ट्रीय रैंकिंग एवं भूमि उपयोग सांख्यिकी</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Parameter / Crop</span><span class="lang-hi">पैरामीटर / फसल</span></th>
        <th><span class="lang-en">National Rank of UP</span><span class="lang-hi">उ.प्र. का राष्ट्रीय स्थान</span></th>
        <th><span class="lang-en">National Share / Exam Fact</span><span class="lang-hi">राष्ट्रीय हिस्सा / परीक्षा उपयोगी तथ्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Total Foodgrains (कुल खाद्यान्न)</span><span class="lang-hi">कुल खाद्यान्न उत्पादन</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Contributes approx. 18-20% of India's total foodgrain output.</span><span class="lang-hi">भारत के कुल खाद्यान्न उत्पादन में लगभग 18-20% योगदान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Wheat (गेहूँ)</span><span class="lang-hi">गेहूँ</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Produces ~32-34% of India's total wheat; largest cultivated area in state.</span><span class="lang-hi">भारत के कुल गेहूँ का ~32-34% उत्पादन; राज्य में सर्वाधिक बोया जाने वाला क्षेत्रफल।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Sugarcane (गन्ना)</span><span class="lang-hi">गन्ना</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Produces ~45-50% of national sugarcane; primary cash crop of UP.</span><span class="lang-hi">देश के कुल गन्ने का ~45-50% उत्पादन; उत्तर प्रदेश की प्रमुख नकदी फसल।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Potato (आलू)</span><span class="lang-hi">आलू</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Produces ~35% of India's potatoes; exported under "Taj Brand".</span><span class="lang-hi">भारत के कुल आलू का ~35% उत्पादन; "ताज ब्रांड" के नाम से निर्यात।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Milk Production (दुग्ध उत्पादन)</span><span class="lang-hi">दुग्ध उत्पादन</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Produces ~15.5% of national milk; 1st in bovine & buffalo population.</span><span class="lang-hi">राष्ट्रीय दुग्ध उत्पादन में ~15.5% हिस्सा; गोवंशीय व भैंस संख्या में देश में प्रथम।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Horticulture (Mango, Guava, Aonla)</span><span class="lang-hi">बागवानी (आम, अमरूद, आँवला)</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Pratapgarh produces ~80% of UP's Aonla; Malihabad famous for Dussehri mango.</span><span class="lang-hi">प्रतापगढ़ में उ.प्र. का ~80% आँवला; मलीहाबाद दशहरी आम हेतु विश्वप्रसिद्ध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Mentha Oil / Peppermint (मेंथा तेल)</span><span class="lang-hi">मेंथा तेल (पिपरमेंट)</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1st Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">प्रथम स्थान</strong></span></td>
        <td><span class="lang-en">Produces over 80% of India's total mentha oil (Barabanki, Sambhal hub).</span><span class="lang-hi">भारत के कुल मेंथा तेल का 80% से अधिक उत्पादन (बाराबंकी, संभल मुख्य केंद्र)।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Rice / Paddy (चावल/धान)</span><span class="lang-hi">धान / चावल</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">2nd Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">द्वितीय स्थान</strong></span></td>
        <td><span class="lang-en">Ranks 2nd after West Bengal; Chandauli is known as "Rice Bowl of UP".</span><span class="lang-hi">पश्चिम बंगाल के बाद दूसरा स्थान; चंदौली को "उ.प्र. का धान का कटोरा" कहते हैं।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Total Vegetables (कुल सब्जियाँ)</span><span class="lang-hi">कुल सब्जियाँ</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">2nd Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">द्वितीय स्थान</strong></span></td>
        <td><span class="lang-en">Ranks 2nd after West Bengal in total annual production.</span><span class="lang-hi">वार्षिक उत्पादन में पश्चिम बंगाल के बाद देश में द्वितीय स्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Total Pulses (कुल दलहन)</span><span class="lang-hi">कुल दलहन</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">3rd Rank</strong></span><span class="lang-hi"><strong class="theory-highlight">तृतीय स्थान</strong></span></td>
        <td><span class="lang-en">Ranks 3rd after Madhya Pradesh and Rajasthan (Bundelkhand is pulse hub).</span><span class="lang-hi">मध्य प्रदेश एवं राजस्थान के बाद तीसरा स्थान (बुंदेलखंड मुख्य दलहन केंद्र)।</span></td>
      </tr>
    </tbody>
  </table>

  <h3 class="theory-heading">
    <span class="lang-en">Key Land & Operational Holding Facts (परीक्षा उपयोगी भूमि तथ्य)</span>
    <span class="lang-hi">भूमि उपयोग एवं जोत संबंधी मुख्य तथ्य (परीक्षा हेतु महत्वपूर्ण)</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Total Geographical Area:</span> 240.93 lakh hectares (7.33% of India's total area).</span><span class="lang-hi"><span class="theory-highlight">कुल भौगोलिक क्षेत्रफल:</span> 240.93 लाख हेक्टेयर (भारत के कुल क्षेत्रफल का 7.33%)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Net Sown Area (शुद्ध बोया गया क्षेत्रफल):</span> Approx. 165.7 lakh hectares (~68.7% of reporting area).</span><span class="lang-hi"><span class="theory-highlight">शुद्ध बोया गया क्षेत्रफल:</span> लगभग 165.7 लाख हेक्टेयर (कुल रिपोर्टिंग क्षेत्रफल का ~68.7%)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Gross Cropped Area (सकल फसल क्षेत्र):</span> Approx. 260+ lakh hectares.</span><span class="lang-hi"><span class="theory-highlight">सकल फसल क्षेत्र:</span> लगभग 260+ लाख हेक्टेयर।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Cropping Intensity (फसल गहनता):</span> Approx. 162.4% (indicates multi-cropping on irrigated tracts).</span><span class="lang-hi"><span class="theory-highlight">फसल गहनता:</span> लगभग 162.4% (सिंचित भूमि पर एक वर्ष में एक से अधिक फसलें)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Average Size of Landholding (औसत जोत आकार):</span> 0.73 hectare (well below the national average of ~1.08 ha).</span><span class="lang-hi"><span class="theory-highlight">औसत जोत का आकार:</span> 0.73 हेक्टेयर (राष्ट्रीय औसत ~1.08 हेक्टेयर से काफी कम)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Marginal Farmers (&lt; 1 ha):</span> Constitute 79.5% of total operational holdings in UP.</span><span class="lang-hi"><span class="theory-highlight">सीमांत कृषक (&lt; 1 हेक्टेयर):</span> प्रदेश की कुल क्रियाशील जोतों का 79.5% हिस्सा।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Small Farmers (1 to 2 ha):</span> Constitute ~13.0% of total holdings.</span><span class="lang-hi"><span class="theory-highlight">लघु कृषक (1 से 2 हेक्टेयर):</span> कुल जोतों का लगभग 13.0% हिस्सा।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Combined Small &amp; Marginal Farmers:</span> Over 92.5% of farmers in UP own less than 2 hectares of land.</span><span class="lang-hi"><span class="theory-highlight">सीमांत एवं लघु कृषक कुल योग:</span> उ.प्र. के 92.5% से अधिक किसान 2 हेक्टेयर से कम भूमि के स्वामी हैं।</span></li>
  </ul>
</div>

<!-- Card 3: The 9 Agro-Climatic Zones of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The 9 Agro-Climatic Zones of Uttar Pradesh (9 कृषि-जलवायु क्षेत्र)</span>
    <span class="lang-hi">2. उत्तर प्रदेश के 9 कृषि-जलवायु क्षेत्र (विस्तृत जिला एवं फसल सारणी)</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">UP is divided into <span class="theory-highlight">9 Agro-Climatic Zones</span> under the National Agricultural Research Project (NARP/Planning Commission) based on rainfall, soil characteristics, temperature, and topography:</span>
    <span class="lang-hi">उत्तर प्रदेश को वर्षा, मिट्टी, तापमान और स्थलाकृति के आधार पर योजना आयोग/आईसीएआर द्वारा <span class="theory-highlight">9 कृषि-जलवायु क्षेत्रों</span> में वर्गीकृत किया गया है:</span>
  </p>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Agro-Climatic Zone</span><span class="lang-hi">कृषि-जलवायु क्षेत्र</span></th>
        <th><span class="lang-en">Covered Districts</span><span class="lang-hi">शामिल जिले</span></th>
        <th><span class="lang-en">Climatic Features &amp; Major Crops</span><span class="lang-hi">जलवायु विशेषताएँ एवं प्रमुख फसलें</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>1. Tarai Zone (तराई क्षेत्र)</strong></span><span class="lang-hi"><strong>1. तराई क्षेत्र</strong></span></td>
        <td><span class="lang-en">Pilibhit, Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, Siddharthnagar, Maharajganj.</span><span class="lang-hi">पीलीभीत, लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर, सिद्धार्थनगर, महाराजगंज।</span></td>
        <td><span class="lang-en">High rainfall (120-150 cm), marshy fertile alluvial soil. Major crops: Paddy, Sugarcane, Jute, Wheat.</span><span class="lang-hi">सर्वाधिक वर्षा (120-150 सेमी), नमीयुक्त दलदली जलोढ़ मिट्टी। मुख्य फसलें: धान, गन्ना, पटसन, गेहूँ।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>2. Western Plain Zone (पश्चिमी मैदानी क्षेत्र)</strong></span><span class="lang-hi"><strong>2. पश्चिमी मैदानी क्षेत्र</strong></span></td>
        <td><span class="lang-en">Saharanpur, Muzaffarnagar, Shamli, Meerut, Baghpat, Ghaziabad, Hapur, Bulandshahr.</span><span class="lang-hi">सहारनपुर, मुजफ्फरनगर, शामली, मेरठ, बागपत, गाजियाबाद, हापुड़, बुलंदशहर।</span></td>
        <td><span class="lang-en">Highest agricultural productivity, well-irrigated (canals + tubewells). Major crops: Sugarcane, Wheat, Maize, Mustard.</span><span class="lang-hi">प्रदेश में सर्वाधिक कृषि उत्पादकता, उत्कृष्ट सिंचाई। मुख्य फसलें: गन्ना, गेहूँ, मक्का, सरसों।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>3. Mid-Western Plain (मध्य-पश्चिमी मैदान)</strong></span><span class="lang-hi"><strong>3. मध्य-पश्चिमी मैदानी क्षेत्र</strong></span></td>
        <td><span class="lang-en">Bareilly, Badaun, Shahjahanpur, Rampur, Moradabad, Bijnor, Sambhal, Amroha.</span><span class="lang-hi">बरेली, बदायूँ, शाहजहाँपुर, रामपुर, मुरादाबाद, बिजनौर, संभल, अमरोहा।</span></td>
        <td><span class="lang-en">Rohilkhand alluvial plains, moderate rainfall. Major crops: Wheat, Paddy, Sugarcane, Mentha oil, Mustard.</span><span class="lang-hi">रुहेलखंड जलोढ़ मैदान, मध्यम वर्षा। प्रमुख फसलें: गेहूँ, धान, गन्ना, मेंथा ऑयल, सरसों।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>4. South-Western Semi-Arid (दक्षिण-पश्चिमी अर्ध-शुष्क)</strong></span><span class="lang-hi"><strong>4. दक्षिण-पश्चिमी अर्ध-शुष्क क्षेत्र</strong></span></td>
        <td><span class="lang-en">Agra, Mathura, Aligarh, Hathras, Firozabad, Mainpuri, Etah, Kasganj.</span><span class="lang-hi">आगरा, मथुरा, अलीगढ़, हाथरस, फिरोजाबाद, मैनपुरी, एटा, कासगंज।</span></td>
        <td><span class="lang-en">Lowest rainfall (60-75 cm), semi-arid climate, sandy loam. Major crops: Bajra, Mustard, Potato, Wheat, Barley.</span><span class="lang-hi">कम वर्षा (60-75 सेमी), अर्ध-शुष्क, रेतीली दोमट। प्रमुख फसलें: बाजरा, सरसों, आलू, गेहूँ, जौ।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>5. Central Plain Zone (मध्य मैदानी क्षेत्र)</strong></span><span class="lang-hi"><strong>5. मध्य मैदानी क्षेत्र</strong></span></td>
        <td><span class="lang-en">Lucknow, Kanpur Nagar, Kanpur Dehat, Unnao, Rae Bareli, Sitapur, Hardoi, Fatehpur.</span><span class="lang-hi">लखनऊ, कानपुर नगर, कानपुर देहात, उन्नाव, रायबरेली, सीतापुर, हरदोई, फतेहपुर।</span></td>
        <td><span class="lang-en">Ganga-Gomti alluvium, flat plain. Major crops: Wheat, Paddy, Sugarcane, Potato, Mentha, Gram.</span><span class="lang-hi">गंगा-गोमती जलोढ़, समतल मैदान। प्रमुख फसलें: गेहूँ, धान, गन्ना, आलू, मेंथा, चना।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>6. Bundelkhand Zone (बुंदेलखंड क्षेत्र)</strong></span><span class="lang-hi"><strong>6. बुंदेलखंड क्षेत्र</strong></span></td>
        <td><span class="lang-en">Jhansi, Lalitpur, Jalaun, Hamirpur, Mahoba, Banda, Chitrakoot (7 districts).</span><span class="lang-hi">झांसी, ललितपुर, जालौन, हमीरपुर, महोबा, बांदा, चित्रकूट (7 जिले)।</span></td>
        <td><span class="lang-en">Black soils (Mar, Kabar) & red soils (Parwa, Rakar); drought-prone; Pulse Hub of UP: Gram (चना), Arhar, Masoor, Til, Jowar.</span><span class="lang-hi">काली (मार, काबर) व लाल (परवा, राकर) मिट्टियाँ; सूखा-प्रवण; दलहन का कटोरा: चना, अरहर, मसूर, तिल, ज्वार।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>7. North-Eastern Plain (उत्तर-पूर्वी मैदान)</strong></span><span class="lang-hi"><strong>7. उत्तर-पूर्वी मैदानी क्षेत्र</strong></span></td>
        <td><span class="lang-en">Gorakhpur, Deoria, Kushinagar, Maharajganj, Basti, Sant Kabir Nagar, Siddharthnagar, Gonda.</span><span class="lang-hi">गोरखपुर, देवरिया, कुशीनगर, महाराजगंज, बस्ती, संत कबीर नगर, सिद्धार्थनगर, गोंडा।</span></td>
        <td><span class="lang-en">High rainfall, flood-prone (Ghaghara/Rapti). Major crops: Paddy, Wheat, Sugarcane, Maize, Jute.</span><span class="lang-hi">अधिक वर्षा, बाढ़-प्रवण (घाघरा/राप्ती बेसिन)। प्रमुख फसलें: धान, गेहूँ, गन्ना, मक्का, जूट।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>8. Eastern Plain Zone (पूर्वी मैदानी क्षेत्र)</strong></span><span class="lang-hi"><strong>8. पूर्वी मैदानी क्षेत्र</strong></span></td>
        <td><span class="lang-en">Varanasi, Prayagraj, Jaunpur, Ghazipur, Azamgarh, Mau, Ballia, Chandauli, Pratapgarh.</span><span class="lang-hi">वाराणसी, प्रयागराज, जौनपुर, गाजीपुर, आजमगढ़, मऊ, बलिया, चंदौली, प्रतापगढ़।</span></td>
        <td><span class="lang-en">Alluvial soil, high population density, small holdings. Major crops: Paddy, Wheat, Pulses, Guava, Aonla.</span><span class="lang-hi">जलोढ़ दोमट, सघन आबादी, छोटी जोतें। प्रमुख फसलें: धान, गेहूँ, दलहन, अमरूद, आँवला।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>9. Vindhyan Zone (विंध्य क्षेत्र)</strong></span><span class="lang-hi"><strong>9. विंध्य क्षेत्र</strong></span></td>
        <td><span class="lang-en">Mirzapur, Sonbhadra, southern Prayagraj, Chakia tehsil of Chandauli.</span><span class="lang-hi">मिर्जापुर, सोनभद्र, दक्षिणी प्रयागराज, चंदौली की चकिया तहसील।</span></td>
        <td><span class="lang-en">Plateau, rocky red/gravelly soil, rainfed agriculture. Major crops: Minor millets (Kodo/Kutki), Gram, Arhar, Linseed.</span><span class="lang-hi">पठारी चट्टानी, लाल-कंकरीली मिट्टी, असिंचित कृषि। मुख्य फसलें: मोटे अनाज (कोदो, कुटकी), चना, अरहर, अलसी।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 4: Major Crops - District-wise Pointwise Data -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Major Foodgrains & Cash Crops (फसलवार संपूर्ण तथ्य एवं प्रमुख जिले)</span>
    <span class="lang-hi">3. प्रमुख खाद्यान्न एवं नकदी फसलें (फसलवार तथ्य एवं प्रमुख जिले)</span>
  </div>

  <h3 class="theory-heading">
    <span class="lang-en">A. Foodgrains (खाद्यान्न फसलें)</span>
    <span class="lang-hi">क. खाद्यान्न फसलें</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Wheat (गेहूँ):</span> Rabi crop; sown in Oct-Nov, harvested in March-April. Occupies ~24% of UP's gross cropped area. Top producing districts: Gorakhpur, Hardoi, Aligarh, Badaun, Meerut. Highest yield per hectare is in Western UP (Meerut, Muzaffarnagar).</span><span class="lang-hi"><span class="theory-highlight">गेहूँ:</span> रबी फसल; अक्टूबर-नवंबर में बुआई, मार्च-अप्रैल में कटाई। उ.प्र. के सकल फसल क्षेत्र का ~24% हिस्सा। सर्वाधिक उत्पादक जिले: गोरखपुर, हरदोई, अलीगढ़, बदायूँ, मेरठ। प्रति हेक्टेयर सर्वाधिक उत्पादकता पश्चिमी उ.प्र. (मेरठ, मुजफ्फरनगर) में है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Rice / Paddy (धान):</span> Kharif crop; sown in June-July, harvested in Sept-Oct. Requires high moisture and 100+ cm rainfall. Top districts: Shahjahanpur, Bareilly, Pilibhit, Lakhimpur, Gorakhpur. <span class="theory-highlight">Chandauli</span> is officially regarded as the <em>"Rice Bowl of Uttar Pradesh"</em> (धान का कटोरा).</span><span class="lang-hi"><span class="theory-highlight">धान (चावल):</span> खरीफ फसल; जून-जुलाई में बुआई, सितंबर-अक्टूबर में कटाई। उच्च आर्द्रता एवं 100 सेमी+ वर्षा आवश्यक। शीर्ष जिले: शाहजहाँपुर, बरेली, पीलीभीत, लखीमपुर, गोरखपुर। <span class="theory-highlight">चंदौली</span> को <em>"उत्तर प्रदेश का धान का कटोरा"</em> कहा जाता है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Kalanamak Rice (काला नमक चावल):</span> Aromatic, black-husked, iron-rich scented rice with GI Tag. Known as <em>"Buddha's Gift to the World"</em>; centered in Siddharthnagar, Basti, Gorakhpur, Maharajganj, Sant Kabir Nagar.</span><span class="lang-hi"><span class="theory-highlight">काला नमक चावल:</span> सुगंधित, काले छिलके वाला, आयरन एवं जिंक समृद्ध जीआई टैग प्राप्त चावल। इसे <em>"भगवान बुद्ध का महाप्रसाद"</em> कहा जाता है; मुख्य केंद्र: सिद्धार्थनगर, बस्ती, गोरखपुर, महाराजगंज।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Barley (जौ):</span> Rabi crop; tolerant to alkaline and drier soils. Major districts: Azamgarh, Jaunpur, Gorakhpur, Ballia, Varanasi.</span><span class="lang-hi"><span class="theory-highlight">जौ:</span> रबी फसल; लवणीय एवं शुष्क मिट्टी सहिष्णु। प्रमुख जिले: आजमगढ़, जौनपुर, गोरखपुर, बलिया, वाराणसी।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Bajra (बाजरा):</span> Kharif dryland crop grown in sandy-loam soils. Major districts: Agra, Mathura, Aligarh, Firozabad, Budaun.</span><span class="lang-hi"><span class="theory-highlight">बाजरा:</span> खरीफ शुष्क फसल, बलुई दोमट मिट्टी में उपयुक्त। प्रमुख जिले: आगरा, मथुरा, अलीगढ़, फिरोजाबाद, बदायूँ।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Maize (मक्का):</span> Grown in Kharif, Rabi, and Zaid. Major districts: Bahraich, Gonda, Farrukhabad, Jaunpur, Etah, Mainpuri.</span><span class="lang-hi"><span class="theory-highlight">मक्का:</span> खरीफ, रबी और जायद तीनों ऋतुओं में उगाई जाती है। प्रमुख जिले: बहराइच, गोंडा, फर्रुखाबाद, जौनपुर, एटा, मैनपुरी।</span></li>
  </ul>

  <h3 class="theory-heading">
    <span class="lang-en">B. Pulses &amp; Oilseeds (दलहन एवं तिलहन)</span>
    <span class="lang-hi">ख. दलहन एवं तिलहन फसलें</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Gram / Chana (चना):</span> Largest area among all pulses in UP. Bundelkhand region accounts for the majority of production. Key districts: Hamirpur, Banda, Jalaun, Jhansi, Lalitpur, Fatehpur.</span><span class="lang-hi"><span class="theory-highlight">चना:</span> उ.प्र. में दलहनों में सर्वाधिक क्षेत्रफल पर बोई जाने वाली फसल। अधिकांश उत्पादन बुंदेलखंड में होता है। प्रमुख जिले: हमीरपुर, बांदा, जालौन, झांसी, ललितपुर, फतेहपुर।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Arhar / Tur (अरहर/तूर):</span> Major Kharif pulse taking 9-10 months to mature. Key districts: Hamirpur, Fatehpur, Prayagraj, Banda, Chitrakoot.</span><span class="lang-hi"><span class="theory-highlight">अरहर (तूर):</span> प्रमुख खरीफ दलहन, पकने में 9-10 माह लगते हैं। प्रमुख जिले: हमीरपुर, फतेहपुर, प्रयागराज, बांदा, चित्रकूट।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Mustard / Rapeseed (सरसों/राई):</span> Top oilseed of UP; Rabi crop. Key districts: Agra, Mathura, Aligarh, Etah, Firozabad, Kanpur Dehat.</span><span class="lang-hi"><span class="theory-highlight">सरसों / राई:</span> उ.प्र. की प्रमुख तिलहन फसल; रबी मौसम। प्रमुख जिले: आगरा, मथुरा, अलीगढ़, एटा, फिरोजाबाद, कानपुर देहात।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Groundnut (मूंगफली):</span> Kharif crop sown in light sandy loam. Key districts: Mainpuri, Hardoi, Badaun, Etah.</span><span class="lang-hi"><span class="theory-highlight">मूंगफली:</span> खरीफ फसल, हल्की बलुई दोमट मिट्टी में उपयुक्त। प्रमुख जिले: मैनपुरी, हरदोई, बदायूँ, एटा।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Linseed / Alsi (अलसी):</span> Rabi oilseed. Key districts: Mirzapur, Sonbhadra, Hamirpur, Jalaun.</span><span class="lang-hi"><span class="theory-highlight">अलसी:</span> रबी तिलहन। प्रमुख जिले: मिर्जापुर, सोनभद्र, हमीरपुर, जालौन।</span></li>
  </ul>

  <h3 class="theory-heading">
    <span class="lang-en">C. Cash Crops &amp; Specialized Commercial Crops (नकदी एवं विशिष्ट फसलें)</span>
    <span class="lang-hi">ग. नकदी एवं विशिष्ट वाणिज्यिक फसलें</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Sugarcane (गन्ना):</span> Premier cash crop of UP (~13% of gross cropped area). Top belt: Western UP &amp; Tarai (Muzaffarnagar - <em>"Sugar Bowl of UP"</em>, Meerut, Bijnor, Saharanpur, Lakhimpur Kheri). UP Sugar Corporation was established in <strong class="theory-highlight">1971</strong>. UP Sugarcane Research Council is located at <strong class="theory-highlight">Shahjahanpur</strong> (est. 1912).</span><span class="lang-hi"><span class="theory-highlight">गन्ना:</span> प्रदेश की सबसे प्रमुख नकदी फसल (सकल फसल क्षेत्र का ~13%)। मुख्य बेल्ट: पश्चिमी उ.प्र. एवं तराई (मुजफ्फरनगर - <em>"उ.प्र. का चीनी का कटोरा"</em>, मेरठ, बिजनौर, सहारनपुर, लखीमपुर खीरी)। उ.प्र. राज्य चीनी निगम की स्थापना <strong class="theory-highlight">1971</strong> में हुई थी। उ.प्र. गन्ना अनुसंधान परिषद <strong class="theory-highlight">शाहजहाँपुर</strong> (स्थापना 1912) में स्थित है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Potato (आलू):</span> UP produces ~35% of India's total potatoes. Key districts: Agra, Farrukhabad, Firozabad, Hathras, Kannauj. Farrukhabad is called the <em>"Potato Capital of UP"</em>. Exported under the brand name <strong class="theory-highlight">"Taj Brand"</strong>.</span><span class="lang-hi"><span class="theory-highlight">आलू:</span> उ.प्र. देश के कुल आलू का ~35% उत्पादित करता है। प्रमुख जिले: आगरा, फर्रुखाबाद, फिरोजाबाद, हाथरस, कन्नौज। फर्रुखाबाद को <em>"उ.प्र. की आलू राजधानी"</em> कहते हैं। आगरा निर्यात क्षेत्र से आलू <strong class="theory-highlight">"ताज ब्रांड"</strong> के नाम से निर्यात होता है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Mentha Oil / Peppermint (मेंथा तेल):</span> UP accounts for <strong class="theory-highlight">&gt;80%</strong> of India's mentha output. Major districts: Barabanki, Sambhal, Rampur, Badaun, Moradabad, Jalaun.</span><span class="lang-hi"><span class="theory-highlight">मेंथा तेल (पिपरमेंट):</span> भारत के मेंथा तेल उत्पादन में उ.प्र. का हिस्सा <strong class="theory-highlight">80% से अधिक</strong> है। प्रमुख जिले: बाराबंकी, संभल, रामपुर, बदायूँ, मुरादाबाद, जालौन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Opium (अफीम):</span> The only state-owned opium processing factory in UP is the <strong class="theory-highlight">Government Opium and Alkaloid Works, Ghazipur</strong> (established in 1820). The highest licensed opium poppy cultivation area is in <strong class="theory-highlight">Barabanki</strong> district.</span><span class="lang-hi"><span class="theory-highlight">अफीम:</span> प्रदेश में एकमात्र शासकीय अफीम कारखाना <strong class="theory-highlight">गाजीपुर</strong> में स्थित है (स्थापना 1820)। राज्य में अफीम की सर्वाधिक लाइसेंसी खेती <strong class="theory-highlight">बाराबंकी</strong> जिले में होती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Betel Leaf / Pan (पान की खेती):</span> <strong class="theory-highlight">Mahoba</strong> is famous for Desawari Pan. UP's dedicated <em>Pan Experiment and Training Center</em> is situated at <strong class="theory-highlight">Mahoba</strong> (established 1981). Also grown in Barabanki, Unnao, Varanasi.</span><span class="lang-hi"><span class="theory-highlight">पान की खेती:</span> <strong class="theory-highlight">महोबा</strong> देशावरी पान के लिए प्रसिद्ध है। उ.प्र. का <em>पान प्रयोग एवं प्रशिक्षण केंद्र</em> <strong class="theory-highlight">महोबा</strong> (स्थापना 1981) में है। इसके अतिरिक्त बाराबंकी, उन्नाव, वाराणसी में भी पान की खेती होती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Tobacco (तंबाकू):</span> Farrukhabad, Etah, Mainpuri, Ballia.</span><span class="lang-hi"><span class="theory-highlight">तंबाकू:</span> फर्रुखाबाद, एटा, मैनपुरी, बलिया।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Jute / Patson (पटसन/सनई):</span> Deoria, Gorakhpur, Maharajganj (Tarai-moist region).</span><span class="lang-hi"><span class="theory-highlight">पटसन / सनई:</span> देवरिया, गोरखपुर, महाराजगंज (तराई आर्द्र क्षेत्र)।</span></li>
  </ul>
</div>

<!-- Card 5: Horticulture, Fruits, Vegetables & Agri-Export Zones -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Horticulture, Fruits, Vegetables &amp; Agri-Export Zones (AEZ)</span>
    <span class="lang-hi">4. बागवानी, फल, सब्जियाँ एवं कृषि निर्यात क्षेत्र (AEZ)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Fruit / Commodity</span><span class="lang-hi">फल / वस्तु</span></th>
        <th><span class="lang-en">Famous Districts / Centers</span><span class="lang-hi">प्रसिद्ध जिले / मुख्य केंद्र</span></th>
        <th><span class="lang-en">Key Varieties &amp; GI Tag / Exam Notes</span><span class="lang-hi">प्रमुख किस्में, जीआई टैग एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Mango (आम)</strong></span><span class="lang-hi"><strong>आम</strong></span></td>
        <td><span class="lang-en">Malihabad (Lucknow), Saharanpur, Varanasi, Bulandshahr, Baghpat.</span><span class="lang-hi">मलीहाबाद (लखनऊ), सहारनपुर, वाराणसी, बुलंदशहर, बागपत।</span></td>
        <td><span class="lang-en">Dussehri (Malihabad - GI), Chausa (Saharanpur), Langra (Varanasi - GI), Rataul (Baghpat - GI), Gaurjit (Gorakhpur). Export Brand: <strong class="theory-highlight">"Nawab Brand"</strong>.</span><span class="lang-hi">दशहरी (मलीहाबाद - GI), चौसा (सहारनपुर), लंगड़ा (वाराणसी - GI), रटौल (बागपत - GI), गौरजीत (गोरखपुर)। निर्यात ब्रांड: <strong class="theory-highlight">"नवाब ब्रांड"</strong>।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Guava (अमरूद)</strong></span><span class="lang-hi"><strong>अमरूद</strong></span></td>
        <td><span class="lang-en">Prayagraj (Allahabad), Kaushambi, Bareilly, Badaun, Ayodhya.</span><span class="lang-hi">प्रयागराज (इलाहाबाद), कौशांबी, बरेली, बदायूँ, अयोध्या।</span></td>
        <td><span class="lang-en">Allahabad Safeda, Allahabad Surkha (deep pink flesh - GI Tag), Lalit, Shweta. <em>Guava Training and Experiment Center:</em> <strong>Prayagraj (Khusro Bagh)</strong>.</span><span class="lang-hi">इलाहाबादी सफेदा, इलाहाबादी सुरखा (लाल गूदे वाला - GI टैग), ललित, श्वेता। <em>अमरूद प्रशिक्षण एवं प्रयोग केंद्र:</em> <strong>प्रयागराज (खुसरो बाग)</strong>।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Aonla / Gooseberry (आँवला)</strong></span><span class="lang-hi"><strong>आँवला</strong></span></td>
        <td><span class="lang-en"><strong>Pratapgarh</strong> (The Aonla Capital of India).</span><span class="lang-hi"><strong>प्रतापगढ़</strong> (भारत की आँवला राजधानी)।</span></td>
        <td><span class="lang-en">Accounts for ~80% of UP's aonla production. Varieties: Chakaiya, Krishna, Kanchan, NA-7. Heavily processed for murabba, candy, juice under ODOP.</span><span class="lang-hi">उ.प्र. के कुल आँवला उत्पादन का ~80%। किस्में: चकइया, कृष्णा, कंचन, NA-7। ODOP योजना के तहत मुरब्बा, कैंडी, जूस प्रसंस्करण।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Banana (केला)</strong></span><span class="lang-hi"><strong>केला</strong></span></td>
        <td><span class="lang-en">Kaushambi, Gorakhpur, Ayodhya, Kushinagar.</span><span class="lang-hi">कौशांबी, गोरखपुर, अयोध्या, कुशीनगर।</span></td>
        <td><span class="lang-en">Varieties: Grand Naine (G-9), Chini Champa, Basrai, Barwahi. Kaushambi is famous for extensive banana cultivation.</span><span class="lang-hi">किस्में: ग्रैंड नैने (G-9), चीनी चंपा, बसराई, बरवाहि। कौशांबी बड़े पैमाने पर केला उत्पादन हेतु प्रसिद्ध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Citrus &amp; Malta (संतरा, मौसमी, माल्टा)</strong></span><span class="lang-hi"><strong>संतरा, मौसमी, माल्टा</strong></span></td>
        <td><span class="lang-en">Saharanpur, Jhansi, Lalitpur (Bundelkhand).</span><span class="lang-hi">सहारनपुर, झांसी, ललितपुर (बुंदेलखंड)।</span></td>
        <td><span class="lang-en">Saharanpur is the hub of citrus fruits and litchi in UP.</span><span class="lang-hi">सहारनपुर उ.प्र. में खट्टे फलों एवं लीची का प्रमुख उत्पादक केंद्र है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Litchi (लीची)</strong></span><span class="lang-hi"><strong>लीची</strong></span></td>
        <td><span class="lang-en">Saharanpur, Muzaffarnagar, Meerut.</span><span class="lang-hi">सहारनपुर, मुजफ्फरनगर, मेरठ।</span></td>
        <td><span class="lang-en">Dehradun Rose, Shahi litchi grown in sub-Himalayan plains.</span><span class="lang-hi">उप-हिमालयी तराई पट्टी में देहरादून रोज, शाही लीची।</span></td>
      </tr>
    </tbody>
  </table>

  <h3 class="theory-heading">
    <span class="lang-en">The 3 Agri-Export Zones (AEZ) of Uttar Pradesh (3 कृषि निर्यात क्षेत्र)</span>
    <span class="lang-hi">उत्तर प्रदेश के 3 कृषि निर्यात क्षेत्र (AEZ)</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">1. Agra AEZ:</span> Dedicated specifically for <strong class="theory-highlight">Potato (आलू)</strong> export under the "Taj Brand". Covers Agra, Hathras, Farrukhabad, Kannauj, Aligarh, Firozabad.</span><span class="lang-hi"><span class="theory-highlight">1. आगरा कृषि निर्यात क्षेत्र:</span> "ताज ब्रांड" के अंतर्गत विशेष रूप से <strong class="theory-highlight">आलू</strong> के निर्यात हेतु। शामिल जिले: आगरा, हाथरस, फर्रुखाबाद, कन्नौज, अलीगढ़, फिरोजाबाद।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">2. Lucknow AEZ:</span> Dedicated for <strong class="theory-highlight">Mango &amp; Vegetables (आम एवं सब्जियाँ)</strong> export under the "Nawab Brand". Covers Lucknow, Unnao, Barabanki, Sitapur, Hardoi.</span><span class="lang-hi"><span class="theory-highlight">2. लखनऊ कृषि निर्यात क्षेत्र:</span> "नवाब ब्रांड" के अंतर्गत <strong class="theory-highlight">आम एवं सब्जियों</strong> के निर्यात हेतु। शामिल जिले: लखनऊ, उन्नाव, बाराबंकी, सीतापुर, हरदोई।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">3. Saharanpur AEZ:</span> Dedicated specifically for <strong class="theory-highlight">Mango (आम)</strong> export. Covers Saharanpur, Muzaffarnagar, Meerut, Bulandshahr, Baghpat.</span><span class="lang-hi"><span class="theory-highlight">3. सहारनपुर कृषि निर्यात क्षेत्र:</span> विशेष रूप से <strong class="theory-highlight">आम</strong> के निर्यात हेतु। शामिल जिले: सहारनपुर, मुजफ्फरनगर, मेरठ, बुलंदशहर, बागपत।</span></li>
  </ul>
</div>

<!-- Card 6: Irrigation System & Canal Network -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Irrigation Sources &amp; Canal Network of UP (सिंचाई व्यवस्था एवं नहर तंत्र)</span>
    <span class="lang-hi">5. उत्तर प्रदेश में सिंचाई के स्रोत एवं प्रमुख नहर प्रणाली</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Irrigation Source</span><span class="lang-hi">सिंचाई का स्रोत</span></th>
        <th><span class="lang-en">Share of Net Irrigated Area</span><span class="lang-hi">शुद्ध सिंचित क्षेत्र में हिस्सा</span></th>
        <th><span class="lang-en">Exam Facts &amp; Coverage</span><span class="lang-hi">परीक्षा उपयोगी तथ्य एवं विस्तार</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Tubewells (नलकूप)</strong></span><span class="lang-hi"><strong>नलकूप (सरकारी व निजी)</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">~73.4%</strong></span><span class="lang-hi"><strong class="theory-highlight">~73.4%</strong></span></td>
        <td><span class="lang-en">Dominant source of irrigation in UP. First tubewell in UP was dug in <strong class="theory-highlight">1930 at Meerut</strong>. Private tubewells outnumber government tubewells significantly.</span><span class="lang-hi">प्रदेश में सिंचाई का सबसे बड़ा स्रोत। उ.प्र. में पहला नलकूप <strong class="theory-highlight">1930 में मेरठ</strong> में लगाया गया था। निजी नलकूपों की संख्या सर्वाधिक है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Canals (नहरें)</strong></span><span class="lang-hi"><strong>नहरें</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">~15.2%</strong></span><span class="lang-hi"><strong class="theory-highlight">~15.2%</strong></span></td>
        <td><span class="lang-en">UP has the <strong class="theory-highlight">largest canal network in India</strong> (over 75,000 km of canals and distributaries).</span><span class="lang-hi">उत्तर प्रदेश में <strong class="theory-highlight">भारत का सबसे लंबा नहर नेटवर्क</strong> है (कुल 75,000 किमी से अधिक नहरें व वितरण प्रणालियां)।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Traditional Wells (कुएँ)</strong></span><span class="lang-hi"><strong>पारंपरिक कुएँ</strong></span></td>
        <td><span class="lang-en">~8.6%</span><span class="lang-hi">~8.6%</span></td>
        <td><span class="lang-en">Historically dominant in central and eastern UP, now largely replaced by mechanical pumps.</span><span class="lang-hi">ऐतिहासिक रूप से मध्य व पूर्वी उ.प्र. में प्रचलित, अब अधिकांश स्थान पंपसेटों ने ले लिया है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Tanks, Ponds, Lakes (तालाब, पोखर, झीलें)</strong></span><span class="lang-hi"><strong>तालाब, पोखर, झीलें</strong></span></td>
        <td><span class="lang-en">~0.5%</span><span class="lang-hi">~0.5%</span></td>
        <td><span class="lang-en">Common in Bundelkhand (Chandela tanks) and Vindhyan plateau.</span><span class="lang-hi">बुंदेलखंड (चंदेलकालीन तालाब) एवं विंध्य पठारी क्षेत्रों में सिंचाई का पारंपरिक साधन।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Other Sources (अन्य साधन)</strong></span><span class="lang-hi"><strong>अन्य साधन</strong></span></td>
        <td><span class="lang-en">~2.3%</span><span class="lang-hi">~2.3%</span></td>
        <td><span class="lang-en">Direct lifting from rivers, streams, check dams.</span><span class="lang-hi">नदियों, नालों, चेकडैमों से सीधे जल उत्थान द्वारा सिंचाई।</span></td>
      </tr>
    </tbody>
  </table>

  <h3 class="theory-heading">
    <span class="lang-en">Famous Canals of Uttar Pradesh (उत्तर प्रदेश की प्रमुख नहरें)</span>
    <span class="lang-hi">उत्तर प्रदेश की प्रमुख नहरें (परीक्षा उपयोगी तथ्य)</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Eastern Yamuna Canal (पूर्वी यमुना नहर):</span> The <strong class="theory-highlight">oldest canal in Uttar Pradesh</strong>. Originally commissioned in 1830 by the British (conceived during Shah Jahan's reign). Originates from Tajewala Barrage on Yamuna river; irrigates Saharanpur, Shamli, Muzaffarnagar, Meerut, Baghpat, Ghaziabad.</span><span class="lang-hi"><span class="theory-highlight">पूर्वी यमुना नहर:</span> उत्तर प्रदेश की <strong class="theory-highlight">सबसे पुरानी नहर</strong>। मूल रूप से अंग्रेजों द्वारा 1830 में चालू (शाहजहाँ के काल में प्रारंभिक प्रयास)। यमुना पर ताजेवाला बैराज से निकलती है; सहारनपुर, शामली, मुजफ्फरनगर, मेरठ, बागपत, गाजियाबाद को सींचती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Sharda Canal (शारदा नहर):</span> The <strong class="theory-highlight">longest canal network in Uttar Pradesh</strong>. With all branches and distributaries, its total length is approx. <strong class="theory-highlight">12,368 km</strong>. Built in <strong class="theory-highlight">1928</strong>; originates from Sharda Barrage at Banbasa (Nepal border, Pilibhit). Irrigates Pilibhit, Bareilly, Shahjahanpur, Lakhimpur, Hardoi, Sitapur, Lucknow, Unnao, Rae Bareli, Barabanki, Prayagraj.</span><span class="lang-hi"><span class="theory-highlight">शारदा नहर:</span> उत्तर प्रदेश की <strong class="theory-highlight">सबसे लंबी नहर प्रणाली</strong>। शाखाओं-प्रशाखाओं सहित कुल लंबाई लगभग <strong class="theory-highlight">12,368 किमी</strong>। निर्माण वर्ष: <strong class="theory-highlight">1928</strong>; बनबसा (नेपाल सीमा, पीलीभीत) के पास शारदा बैराज से निकलती है। पीलीभीत, बरेली, शाहजहाँपुर, लखीमपुर, हरदोई, सीतापुर, लखनऊ, उन्नाव, रायबरेली, बाराबंकी, प्रयागराज को सिंचित करती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Upper Ganga Canal (ऊपरी गंगा नहर):</span> Constructed between <strong class="theory-highlight">1842-1854</strong> under British engineer Sir Proby Cautley. Originates from Bhimgoda Barrage, Haridwar; irrigates Saharanpur, Muzaffarnagar, Meerut, Bulandshahr, Aligarh, Mathura, Agra, Etawah, Kanpur.</span><span class="lang-hi"><span class="theory-highlight">ऊपरी गंगा नहर:</span> निर्माण: <strong class="theory-highlight">1842-1854</strong> ब्रिटिश इंजीनियर सर प्रोबी कॉटले के निर्देशन में। हरिद्वार के भीमगोड़ा बैराज से निकलती है; सहारनपुर, मुजफ्फरनगर, मेरठ, बुलंदशहर, अलीगढ़, मथुरा, आगरा, इटावा, कानपुर को सींचती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Lower Ganga Canal (निचली गंगा नहर):</span> Constructed in <strong class="theory-highlight">1878</strong>; originates from Narora (Bulandshahr) on Ganga river. Irrigates Bulandshahr, Aligarh, Etah, Mainpuri, Farrukhabad, Fatehpur, Prayagraj.</span><span class="lang-hi"><span class="theory-highlight">निचली गंगा नहर:</span> निर्माण: <strong class="theory-highlight">1878</strong>; गंगा नदी पर नरोरा (बुलंदशहर) से निकलती है। बुलंदशहर, अलीगढ़, एटा, मैनपुरी, फर्रुखाबाद, फतेहपुर, प्रयागराज की सिंचाई करती है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Betwa Canal (बेतवा नहर):</span> Constructed in 1885; originates from Parichha Dam on Betwa river in Jhansi. Crucial lifeline for Bundelkhand (Jhansi, Jalaun, Hamirpur).</span><span class="lang-hi"><span class="theory-highlight">बेतवा नहर:</span> निर्माण: 1885; झांसी में बेतवा नदी पर पारीछा बांध से निकलती है। बुंदेलखंड (झांसी, जालौन, हमीरपुर) की जीवनरेखा।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Ken-Betwa River Interlinking Project:</span> India's first national river interlinking project. Transfers surplus water from Ken river (MP) to Betwa basin (UP) through Daudhan Dam and a 221 km link canal. Irrigates 2.51 lakh hectares in UP's Bundelkhand (Banda, Mahoba, Jhansi, Lalitpur).</span><span class="lang-hi"><span class="theory-highlight">केन-बेतवा नदी जोड़ो परियोजना:</span> देश की पहली राष्ट्रीय नदी जोड़ो परियोजना। दौधन बांध एवं 221 किमी लंबी नहर से केन (म.प्र.) का अधिशेष जल बेतवा (उ.प्र.) बेसिन में हस्तांतरित होगा। उ.प्र. के बुंदेलखंड (बांदा, महोबा, झांसी, ललितपुर) के 2.51 लाख हेक्टेयर क्षेत्र को सिंचाई।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Saryu Canal National Project (सरयू नहर राष्ट्रीय परियोजना):</span> Dedicated to nation in Dec 2021 by PM Modi. Connects 5 rivers (Ghaghara, Saryu, Rapti, Banganga, Rohini) through 6,600 km canal network to irrigate 14+ lakh hectares across 9 eastern districts (Bahraich, Shravasti, Balrampur, Gonda, Siddharthnagar, Basti, Sant Kabir Nagar, Gorakhpur, Maharajganj).</span><span class="lang-hi"><span class="theory-highlight">सरयू नहर राष्ट्रीय परियोजना:</span> दिसंबर 2021 में प्रधानमंत्री द्वारा राष्ट्र को समर्पित। 5 नदियों (घाघरा, सरयू, राप्ती, बाणगंगा, रोहिणी) को जोड़कर 6,600 किमी नहर नेटवर्क से 9 पूर्वी जिलों (बहराइच, श्रावस्ती, बलरामपुर, गोंडा, सिद्धार्थनगर, बस्ती, संत कबीर नगर, गोरखपुर, महाराजगंज) के 14 लाख हेक्टेयर से अधिक क्षेत्र को सिंचाई।</span></li>
  </ul>
</div>

<!-- Card 7: Agricultural Research Institutes & Universities in UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Agricultural Research Institutes &amp; Universities in UP (कृषि अनुसंधान संस्थान एवं विश्वविद्यालय)</span>
    <span class="lang-hi">6. उत्तर प्रदेश के कृषि अनुसंधान संस्थान एवं विश्वविद्यालय (पूर्ण परीक्षा सूची)</span>
  </div>

  <h3 class="theory-heading">
    <span class="lang-en">A. Central ICAR &amp; CSIR Institutes in Uttar Pradesh</span>
    <span class="lang-hi">क. उत्तर प्रदेश में स्थित केंद्रीय (ICAR / CSIR) अनुसंधान संस्थान</span>
  </h3>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Institute Name</span><span class="lang-hi">संस्थान का नाम</span></th>
        <th><span class="lang-en">Location</span><span class="lang-hi">स्थान</span></th>
        <th><span class="lang-en">Key Mandate / Exam Note</span><span class="lang-hi">मुख्य कार्य / परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Indian Institute of Sugarcane Research (IISR)</span><span class="lang-hi">भारतीय गन्ना अनुसंधान संस्थान (IISR)</span></td>
        <td><span class="lang-en"><strong>Lucknow</strong> (est. 1952)</span><span class="lang-hi"><strong>लखनऊ</strong> (स्थापना 1952)</span></td>
        <td><span class="lang-en">Premier national institute for sugarcane agronomy and farm mechanization.</span><span class="lang-hi">गन्ना कृषि विज्ञान एवं यंत्रीकरण हेतु शीर्ष राष्ट्रीय संस्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Institute for Subtropical Horticulture (CISH)</span><span class="lang-hi">केंद्रीय उपोष्ण बागवानी संस्थान (CISH)</span></td>
        <td><span class="lang-en"><strong>Rehmankhera, Lucknow</strong></span><span class="lang-hi"><strong>रहमानखेड़ा, लखनऊ</strong></span></td>
        <td><span class="lang-en">Research on subtropical fruits: Mango, Guava, Papaya, Bael.</span><span class="lang-hi">उपोष्णकटिबंधीय फलों (आम, अमरूद, पपीता, बेल) पर शीर्ष अनुसंधान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Institute of Vegetable Research (IIVR)</span><span class="lang-hi">भारतीय सब्जी अनुसंधान संस्थान (IIVR)</span></td>
        <td><span class="lang-en"><strong>Shahanshahpur, Varanasi</strong></span><span class="lang-hi"><strong>शहंशाहपुर, वाराणसी</strong></span></td>
        <td><span class="lang-en">National center for breeding improved vegetable varieties and hybrid seeds.</span><span class="lang-hi">उन्नत सब्जी प्रजातियों एवं संकर बीजों के विकास हेतु राष्ट्रीय केंद्र।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Institute of Pulses Research (IIPR)</span><span class="lang-hi">भारतीय दलहन अनुसंधान संस्थान (IIPR)</span></td>
        <td><span class="lang-en"><strong>Kalyanpur, Kanpur</strong></span><span class="lang-hi"><strong>कल्याणपुर, कानपुर</strong></span></td>
        <td><span class="lang-en">Apex national institute for basic and applied pulse crop research.</span><span class="lang-hi">दालों (चना, अरहर, मूंग, मसूर) पर बुनियादी व अनुप्रयुक्त अनुसंधान का शीर्ष संस्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Grassland and Fodder Research Institute (IGFRI)</span><span class="lang-hi">भारतीय चारागाह एवं चारा अनुसंधान संस्थान (IGFRI)</span></td>
        <td><span class="lang-en"><strong>Jhansi</strong> (est. 1962)</span><span class="lang-hi"><strong>झांसी</strong> (स्थापना 1962)</span></td>
        <td><span class="lang-en">Dedicated to grassland management, fodder crop production and silvopasture.</span><span class="lang-hi">चारागाह प्रबंधन, चारा फसलों और सिल्वोपाश्चर पर समर्पित शोध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Agroforestry Research Institute (CAFRI)</span><span class="lang-hi">केंद्रीय कृषि वानिकी अनुसंधान संस्थान (CAFRI)</span></td>
        <td><span class="lang-en"><strong>Jhansi</strong> (est. 1988)</span><span class="lang-hi"><strong>झांसी</strong> (स्थापना 1988)</span></td>
        <td><span class="lang-en">National research on integrating trees into agricultural farmlands.</span><span class="lang-hi">कृषि भूमि पर वृक्षारोपण एवं कृषि-वानिकी मॉडल पर राष्ट्रीय संस्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Veterinary Research Institute (IVRI)</span><span class="lang-hi">भारतीय पशु चिकित्सा अनुसंधान संस्थान (IVRI)</span></td>
        <td><span class="lang-en"><strong>Izatnagar, Bareilly</strong> (est. 1889)</span><span class="lang-hi"><strong>इज्जतनगर, बरेली</strong> (स्थापना 1889)</span></td>
        <td><span class="lang-en">One of India's oldest institutes; national deemed university for animal health and vaccines.</span><span class="lang-hi">भारत के सबसे पुराने संस्थानों में से एक; पशु स्वास्थ्य, रोग निदान एवं टीकों हेतु डीम्ड वि.वि.।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Avian Research Institute (CARI)</span><span class="lang-hi">केंद्रीय पक्षी अनुसंधान संस्थान (CARI)</span></td>
        <td><span class="lang-en"><strong>Izatnagar, Bareilly</strong> (est. 1979)</span><span class="lang-hi"><strong>इज्जतनगर, बरेली</strong> (स्थापना 1979)</span></td>
        <td><span class="lang-en">Research on poultry, quail, turkey, duck, and guinea fowl production.</span><span class="lang-hi">मुर्गीपालन, बटेर, टर्की, बत्तख एवं गिनी फाउल उत्पादन पर अनुसंधान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Institute for Research on Goats (CIRG)</span><span class="lang-hi">केंद्रीय बकरी अनुसंधान संस्थान (CIRG)</span></td>
        <td><span class="lang-en"><strong>Makhdoom, Farah, Mathura</strong></span><span class="lang-hi"><strong>मखदूम, फरह, मथुरा</strong></span></td>
        <td><span class="lang-en">Breeding and health management of indigenous goat breeds (Jamunapari, Barbari).</span><span class="lang-hi">देशी बकरी नस्लों (जमुनापारी, बरबरी) के संवर्धन एवं स्वास्थ्य प्रबंधन पर शोध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Institute of Medicinal and Aromatic Plants (CIMAP)</span><span class="lang-hi">केंद्रीय औषधीय एवं सगंध पौधा संस्थान (CIMAP)</span></td>
        <td><span class="lang-en"><strong>Lucknow</strong> (CSIR)</span><span class="lang-hi"><strong>लखनऊ</strong> (CSIR)</span></td>
        <td><span class="lang-en">Pioneered the Mentha revolution and aromatic essential oil varieties in UP.</span><span class="lang-hi">उ.प्र. में मेंथा क्रांति और सगंधीय तेल पौधों की उन्नत किस्मों के विकास का जनक।</span></td>
      </tr>
    </tbody>
  </table>

  <h3 class="theory-heading">
    <span class="lang-en">B. Agricultural Universities in Uttar Pradesh (कुल 6 कृषि विश्वविद्यालय)</span>
    <span class="lang-hi">ख. उत्तर प्रदेश के कृषि विश्वविद्यालय (कुल 6: 4 राज्य, 1 केंद्रीय, 1 डीम्ड)</span>
  </h3>
  <ol class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">1. Chandra Shekhar Azad University of Agriculture &amp; Technology (CSAUAT):</span> Located at <strong class="theory-highlight">Kanpur</strong>. Established in <strong class="theory-highlight">1975</strong> (State SAU).</span><span class="lang-hi"><span class="theory-highlight">1. चन्द्रशेखर आजाद कृषि एवं प्रौद्योगिक विश्वविद्यालय (CSAUAT):</span> <strong class="theory-highlight">कानपुर</strong> में स्थित। स्थापना वर्ष: <strong class="theory-highlight">1975</strong> (राज्य कृषि वि.वि.)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">2. Acharya Narendra Deva University of Agriculture &amp; Technology (ANDUAT):</span> Located at <strong class="theory-highlight">Kumarganj, Ayodhya</strong>. Established in <strong class="theory-highlight">1977</strong> (State SAU).</span><span class="lang-hi"><span class="theory-highlight">2. आचार्य नरेंद्र देव कृषि एवं प्रौद्योगिक विश्वविद्यालय (ANDUAT):</span> <strong class="theory-highlight">कुमारगंज, अयोध्या</strong> में स्थित। स्थापना वर्ष: <strong class="theory-highlight">1977</strong> (राज्य कृषि वि.वि.)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">3. Sardar Vallabhbhai Patel University of Agriculture &amp; Technology (SVPUAT):</span> Located at <strong class="theory-highlight">Modipuram, Meerut</strong>. Established in <strong class="theory-highlight">2000</strong> (State SAU).</span><span class="lang-hi"><span class="theory-highlight">3. सरदार वल्लभभाई पटेल कृषि एवं प्रौद्योगिक विश्वविद्यालय (SVPUAT):</span> <strong class="theory-highlight">मोदीपुरम, मेरठ</strong> में स्थित। स्थापना वर्ष: <strong class="theory-highlight">2000</strong> (राज्य कृषि वि.वि.)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">4. Banda University of Agriculture &amp; Technology (BUAT):</span> Located at <strong class="theory-highlight">Banda</strong>. Established in <strong class="theory-highlight">2010</strong> (State SAU, dedicated to Bundelkhand's dryland agriculture).</span><span class="lang-hi"><span class="theory-highlight">4. बांदा कृषि एवं प्रौद्योगिक विश्वविद्यालय (BUAT):</span> <strong class="theory-highlight">बांदा</strong> में स्थित। स्थापना वर्ष: <strong class="theory-highlight">2010</strong> (बुंदेलखंड की शुष्क कृषि पर केंद्रित राज्य कृषि वि.वि.)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">5. Rani Lakshmi Bai Central Agricultural University (RLBCAU):</span> Located at <strong class="theory-highlight">Jhansi</strong>. Established in <strong class="theory-highlight">2014</strong> by an Act of Parliament (The only <strong class="theory-highlight">Central Agricultural University</strong> in UP).</span><span class="lang-hi"><span class="theory-highlight">5. रानी लक्ष्मीबाई केंद्रीय कृषि विश्वविद्यालय (RLBCAU):</span> <strong class="theory-highlight">झांसी</strong> में स्थित। संसद के अधिनियम द्वारा <strong class="theory-highlight">2014</strong> में स्थापित (उ.प्र. का एकमात्र <strong class="theory-highlight">केंद्रीय कृषि विश्वविद्यालय</strong>)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">6. Sam Higginbottom University of Agriculture, Technology and Sciences (SHUATS):</span> Located at <strong class="theory-highlight">Naini, Prayagraj</strong>. Founded in <strong class="theory-highlight">1910</strong> by Dr. Sam Higginbottom as <em>Allahabad Agricultural Institute</em> (Oldest agricultural school in South Asia; Deemed University).</span><span class="lang-hi"><span class="theory-highlight">6. सैम हिग्गिनबॉटम कृषि, प्रौद्योगिकी एवं विज्ञान विश्वविद्यालय (SHUATS):</span> <strong class="theory-highlight">नैनी, प्रयागराज</strong> में स्थित। डॉ. सैम हिग्गिनबॉटम द्वारा <strong class="theory-highlight">1910</strong> में <em>इलाहाबाद एग्रीकल्चरल इंस्टीट्यूट</em> के रूप में स्थापित (दक्षिण एशिया का सबसे पुराना कृषि संस्थान; डीम्ड वि.वि.)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">UP Council of Agricultural Research (UPCAR):</span> Located at <strong class="theory-highlight">Lucknow</strong>. Established in <strong class="theory-highlight">1989</strong> as the apex body for planning and coordinating state agricultural research.</span><span class="lang-hi"><span class="theory-highlight">उ.प्र. कृषि अनुसंधान परिषद (UPCAR):</span> <strong class="theory-highlight">लखनऊ</strong> में स्थित। स्थापना: <strong class="theory-highlight">1989</strong> में राज्य के कृषि अनुसंधानों के समन्वय व नियोजन हेतु शीर्ष निकाय।</span></li>
  </ol>
</div>

<!-- Card 8: Livestock, Dairy Development & Animal Husbandry -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Livestock Census, Dairy Development &amp; Animal Husbandry</span>
    <span class="lang-hi">7. पशुगणना, दुग्ध विकास एवं पशुपालन (महत्वपूर्ण परीक्षा बिंदु)</span>
  </div>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Rank 1 in Livestock Population:</span> According to the 20th Livestock Census (2019), UP ranks <strong class="theory-highlight">1st in India</strong> with ~67.8 million livestock animals (~13.4% of India's total).</span><span class="lang-hi"><span class="theory-highlight">पशुधन संख्या में प्रथम:</span> 20वीं पशुगणना (2019) के अनुसार, उ.प्र. ~67.8 मिलियन पशुओं के साथ देश में <strong class="theory-highlight">प्रथम स्थान</strong> पर है (देश के कुल पशुधन का ~13.4%)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Rank 1 in Bovine &amp; Buffalo Population:</span> UP possesses the highest buffalo population in India (famous for Murrah and Bhadawari breeds).</span><span class="lang-hi"><span class="theory-highlight">गोवंशीय एवं भैंस संख्या में प्रथम:</span> उ.प्र. में देश की सर्वाधिक भैंसें पाई जाती हैं (मुर्रा एवं भदावरी नस्लें प्रसिद्ध; भदावरी के दूध में सर्वाधिक वसा पाई जाती है)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Rank 1 in Milk Production:</span> UP produces ~33+ million tonnes of milk annually (~15.5% of national milk production).</span><span class="lang-hi"><span class="theory-highlight">दुग्ध उत्पादन में प्रथम स्थान:</span> उ.प्र. वार्षिक 33+ मिलियन टन दुग्ध उत्पादन के साथ देश में <strong class="theory-highlight">नंबर 1</strong> है (राष्ट्रीय उत्पादन का ~15.5%)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">First Cooperative Milk Union in India:</span> The <strong class="theory-highlight">Lucknow Dugdh Utpadak Sahkari Sangh</strong> was established in <strong class="theory-highlight">1938</strong> at Lucknow (India's first registered cooperative dairy union).</span><span class="lang-hi"><span class="theory-highlight">भारत की प्रथम दुग्ध सहकारी समिति:</span> <strong class="theory-highlight">1938 में लखनऊ दुग्ध उत्पादक सहकारी संघ</strong> की स्थापना हुई (भारत का पहला पंजीकृत दुग्ध सहकारी संघ)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Pradeshik Cooperative Dairy Federation (PCDF):</span> Established in <strong class="theory-highlight">1962</strong> to manage the cooperative dairy network under the <strong class="theory-highlight">"Parag" (पराग)</strong> brand.</span><span class="lang-hi"><span class="theory-highlight">प्रादेशिक कोऑपरेटिव डेयरी फेडरेशन (PCDF):</span> स्थापना: <strong class="theory-highlight">1962</strong>; राज्य में <strong class="theory-highlight">"पराग"</strong> ब्रांड के तहत दुग्ध एवं दुग्ध उत्पादों का विपणन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Nand Baba Milk Mission:</span> Launched in <strong class="theory-highlight">June 2023</strong> with an outlay of ₹1,000 crore to organize milk producers into Dairy FPOs and incentivize indigenous cow rearing.</span><span class="lang-hi"><span class="theory-highlight">नंद बाबा दुग्ध मिशन:</span> <strong class="theory-highlight">जून 2023</strong> में ₹1,000 करोड़ के परिव्यय से शुरू; दुग्ध उत्पादकों के FPO गठन एवं देशी गायों के पालन को प्रोत्साहन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Gokul Puraskar (गोकुल पुरस्कार):</span> State award given to the highest milk producer from indigenous cow breeds (Sahiwal, Gir, Tharparkar, Gangatiri).</span><span class="lang-hi"><span class="theory-highlight">गोकुल पुरस्कार:</span> देशी गायों (साहीवाल, गिर, थारपारकर, गंगातीरी) से सर्वाधिक दूध उत्पादन करने वाले गोपालकों को दिया जाने वाला राज्य पुरस्कार।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Veterinary University:</span> UP Pt. Deen Dayal Upadhyaya Pashu Chikitsa Vigyan Vishwavidyalaya Evam Go-Anusandhan Sansthan is located at <strong class="theory-highlight">Mathura</strong> (DUPVASU, est. 2001).</span><span class="lang-hi"><span class="theory-highlight">पशु चिकित्सा विश्वविद्यालय:</span> उ.प्र. पं. दीनदयाल उपाध्याय पशु चिकित्सा विज्ञान वि.वि. एवं गो-अनुसंधान संस्थान <strong class="theory-highlight">मथुरा</strong> (DUPVASU, स्थापना 2001) में स्थित है।</span></li>
  </ul>
</div>

<!-- Card 9: Major State Schemes, Land Reforms & Farmer Welfare -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Agricultural Schemes, Land Reforms &amp; Farmer Welfare (योजनाएँ एवं भूमि सुधार)</span>
    <span class="lang-hi">8. प्रमुख कृषि योजनाएँ, भूमि सुधार एवं किसान कल्याण (वर्षवार तथ्य)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Scheme / Reform</span><span class="lang-hi">योजना / भूमि सुधार</span></th>
        <th><span class="lang-en">Launch Year in UP</span><span class="lang-hi">उ.प्र. में प्रारंभ वर्ष</span></th>
        <th><span class="lang-en">Key Provisions &amp; Exam Facts</span><span class="lang-hi">मुख्य प्रावधान एवं परीक्षा उपयोगी तथ्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Chakbandi Yojana (चकबंदी योजना)</strong></span><span class="lang-hi"><strong>चकबंदी योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1954</strong> (Pilot), <strong>1958</strong> (Statewide)</span><span class="lang-hi"><strong class="theory-highlight">1954</strong> (पायलट), <strong>1958</strong> (संपूर्ण प्रदेश)</span></td>
        <td><span class="lang-en">Started on pilot basis in 1954 from <em>Kairana tehsil (Muzaffarnagar)</em> and <em>Musafirkhana tehsil (Sultanpur)</em>; extended to entire state in 1958 to consolidate fragmented landholdings.</span><span class="lang-hi">1954 में <em>कैराना तहसील (मुजफ्फरनगर)</em> व <em>मुसाफिरखाना (सुल्तानपुर)</em> से पायलट आधार पर प्रारंभ; 1958 में पूरे प्रदेश में विखंडित जोतों के एकीकरण हेतु लागू।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Kisan Bahi Yojana (किसान बही योजना)</strong></span><span class="lang-hi"><strong>किसान बही योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1992</strong></span><span class="lang-hi"><strong class="theory-highlight">1992</strong></span></td>
        <td><span class="lang-en">Official landholding passbook issued to farmers containing complete records of ownership, land classification, and mutation records.</span><span class="lang-hi">किसानों को उनकी जोतों, खतौनी, स्वामित्व एवं भूमि श्रेणी का प्रामाणिक विवरण उपलब्ध कराने वाली पुस्तिका।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Kisan Credit Card (KCC) Scheme</strong></span><span class="lang-hi"><strong>किसान क्रेडिट कार्ड (KCC) योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1999-2000</strong></span><span class="lang-hi"><strong class="theory-highlight">1999-2000</strong></span></td>
        <td><span class="lang-en">Institutional short-term crop credit at subsidized interest rate (4% with prompt repayment incentive).</span><span class="lang-hi">रियायती ब्याज दर (समय पर भुगतान पर 4%) पर संस्थागत अल्पकालिक फसली ऋण की सुविधा।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Kisan Mitra Yojana (किसान मित्र योजना)</strong></span><span class="lang-hi"><strong>किसान मित्र योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">18 June 2001</strong></span><span class="lang-hi"><strong class="theory-highlight">18 जून 2001</strong></span></td>
        <td><span class="lang-en">Deployed trained local agriculture intermediaries in panchayats to disseminate technical farming advice.</span><span class="lang-hi">किसानों को कृषि संबंधी नवीन तकनीकी जानकारी ग्राम पंचायत स्तर पर उपलब्ध कराने हेतु किसान मित्रों की तैनाती।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>PM-KISAN (पीएम-किसान सम्मान निधि)</strong></span><span class="lang-hi"><strong>पीएम-किसान सम्मान निधि</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">24 February 2019</strong></span><span class="lang-hi"><strong class="theory-highlight">24 फरवरी 2019</strong></span></td>
        <td><span class="lang-en">Nationally launched by PM Narendra Modi from <strong class="theory-highlight">Gorakhpur, Uttar Pradesh</strong>; ₹6,000/year in 3 equal installments to eligible farmers.</span><span class="lang-hi">प्रधानमंत्री नरेंद्र मोदी द्वारा <strong class="theory-highlight">गोरखपुर (उत्तर प्रदेश)</strong> से राष्ट्रीय स्तर पर शुभारंभ; ₹6,000 वार्षिक (₹2,000 की 3 समान किस्तों में)।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mukhyamantri Krishak Durghatna Kalyan Yojana</strong></span><span class="lang-hi"><strong>मुख्यमंत्री कृषक दुर्घटना कल्याण योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">Revamped 2020</strong></span><span class="lang-hi"><strong class="theory-highlight">संशोधित 2020</strong></span></td>
        <td><span class="lang-en">Provides up to <strong class="theory-highlight">₹5,00,000</strong> in case of accidental death/permanent disability of a farmer (age 18-70). Crucially extended to <em>sharecroppers (बटाईदार)</em> and landless farm laborers.</span><span class="lang-hi">कृषक (18-70 वर्ष) की दुर्घटनावश मृत्यु/दिव्यांगता पर <strong class="theory-highlight">₹5,00,000</strong> तक की आर्थिक सहायता। महत्वपूर्ण तथ्य: इसमें <em>बटाईदार</em> एवं भूमिहीन खेतिहर मजदूर भी सम्मिलित हैं।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mukhyamantri Khet Suraksha Yojana</strong></span><span class="lang-hi"><strong>मुख्यमंत्री खेत सुरक्षा योजना</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">2023-2024</strong></span><span class="lang-hi"><strong class="theory-highlight">2023-2024</strong></span></td>
        <td><span class="lang-en">Subsidizes solar fencing (low-voltage harmless 12V pulse) to protect crops from stray cattle and wild boars without injuring animals.</span><span class="lang-hi">फसलों को निराश्रित गोवंश व जंगली जानवरों से बिना नुकसान पहुंचाए बचाने हेतु सौर बाड़ (12V करंट झटका) पर अनुदान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mandi Parishad (उ.प्र. राज्य कृषि उत्पादन मंडी परिषद)</strong></span><span class="lang-hi"><strong>उ.प्र. राज्य कृषि उत्पादन मंडी परिषद</strong></span></td>
        <td><span class="lang-en"><strong class="theory-highlight">1973</strong></span><span class="lang-hi"><strong class="theory-highlight">1973</strong></span></td>
        <td><span class="lang-en">Established in 1973; regulates 250+ principal market yards; extensive integration with the national <strong class="theory-highlight">e-NAM</strong> digital auction platform.</span><span class="lang-hi">स्थापना: 1973; 250+ प्रमुख कृषि मंडियों का नियमन; राष्ट्रीय <strong class="theory-highlight">e-NAM</strong> डिजिटल ई-मंडी से व्यापक एकीकरण।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 10: Master One-Liner Quick Revision Table -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">9. One-Liner Quick Revision Matrix (एक नज़र में संपूर्ण कृषि सार)</span>
    <span class="lang-hi">9. एक नज़र में संपूर्ण कृषि सार (त्वरित परीक्षा रिवीजन)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Key Topic / Question</span><span class="lang-hi">प्रमुख विषय / प्रश्न</span></th>
        <th><span class="lang-en">Exact Answer / Fact</span><span class="lang-hi">सटीक उत्तर / तथ्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Number of Agro-Climatic Zones in UP</span><span class="lang-hi">उ.प्र. में कृषि-जलवायु क्षेत्रों की संख्या</span></td>
        <td><span class="lang-en"><strong>9 Zones</strong></span><span class="lang-hi"><strong>9 क्षेत्र</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Largest Canal of Uttar Pradesh</span><span class="lang-hi">उत्तर प्रदेश की सबसे लंबी नहर</span></td>
        <td><span class="lang-en"><strong>Sharda Canal</strong> (~12,368 km network, built 1928)</span><span class="lang-hi"><strong>शारदा नहर</strong> (~12,368 किमी नेटवर्क, 1928 में निर्मित)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Oldest Canal of Uttar Pradesh</span><span class="lang-hi">उत्तर प्रदेश की सबसे पुरानी नहर</span></td>
        <td><span class="lang-en"><strong>Eastern Yamuna Canal</strong> (1830)</span><span class="lang-hi"><strong>पूर्वी यमुना नहर</strong> (1830)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">First Tubewell in UP</span><span class="lang-hi">उ.प्र. में पहला नलकूप कहाँ लगा?</span></td>
        <td><span class="lang-en"><strong>Meerut (1930)</strong></span><span class="lang-hi"><strong>मेरठ (1930)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">District known as "Rice Bowl of UP"</span><span class="lang-hi">"उ.प्र. का धान का कटोरा" किसे कहते हैं?</span></td>
        <td><span class="lang-en"><strong>Chandauli (चंदौली)</strong></span><span class="lang-hi"><strong>चंदौली</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">District known as "Aonla Capital"</span><span class="lang-hi">"आँवला की राजधानी" किस जिले को कहते हैं?</span></td>
        <td><span class="lang-en"><strong>Pratapgarh (प्रतापगढ़)</strong></span><span class="lang-hi"><strong>प्रतापगढ़</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Brand name for UP's Potato export</span><span class="lang-hi">उ.प्र. के आलू निर्यात का ब्रांड नाम</span></td>
        <td><span class="lang-en"><strong>"Taj Brand"</strong> (from Agra AEZ)</span><span class="lang-hi"><strong>"ताज ब्रांड"</strong> (आगरा निर्यात क्षेत्र से)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Brand name for UP's Mango export</span><span class="lang-hi">उ.प्र. के आम निर्यात का ब्रांड नाम</span></td>
        <td><span class="lang-en"><strong>"Nawab Brand"</strong> (from Lucknow/Saharanpur AEZ)</span><span class="lang-hi"><strong>"नवाब ब्रांड"</strong> (लखनऊ/सहारनपुर निर्यात क्षेत्र से)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Only Government Opium Factory in UP</span><span class="lang-hi">उ.प्र. में एकमात्र शासकीय अफीम कारखाना</span></td>
        <td><span class="lang-en"><strong>Ghazipur (1820)</strong></span><span class="lang-hi"><strong>गाजीपुर (1820)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">District with maximum Opium cultivation</span><span class="lang-hi">सर्वाधिक अफीम उत्पादक जिला</span></td>
        <td><span class="lang-en"><strong>Barabanki (बाराबंकी)</strong></span><span class="lang-hi"><strong>बाराबंकी</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Pan Experiment &amp; Training Center</span><span class="lang-hi">पान प्रयोग एवं प्रशिक्षण केंद्र</span></td>
        <td><span class="lang-en"><strong>Mahoba (1981)</strong></span><span class="lang-hi"><strong>महोबा (1981)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Guava Training &amp; Experiment Center</span><span class="lang-hi">अमरूद प्रशिक्षण एवं प्रयोग केंद्र</span></td>
        <td><span class="lang-en"><strong>Prayagraj (Khusro Bagh)</strong></span><span class="lang-hi"><strong>प्रयागराज (खुसरो बाग)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Sugarcane Research Council of UP</span><span class="lang-hi">उ.प्र. गन्ना अनुसंधान परिषद</span></td>
        <td><span class="lang-en"><strong>Shahjahanpur (1912)</strong></span><span class="lang-hi"><strong>शाहजहाँपुर (1912)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Institute of Sugarcane Research (IISR)</span><span class="lang-hi">भारतीय गन्ना अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Lucknow (1952)</strong></span><span class="lang-hi"><strong>लखनऊ (1952)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Institute of Vegetable Research (IIVR)</span><span class="lang-hi">भारतीय सब्जी अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Varanasi</strong></span><span class="lang-hi"><strong>वाराणसी</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Institute of Pulses Research (IIPR)</span><span class="lang-hi">भारतीय दलहन अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Kalyanpur, Kanpur</strong></span><span class="lang-hi"><strong>कल्याणपुर, कानपुर</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Institute for Research on Goats (CIRG)</span><span class="lang-hi">केंद्रीय बकरी अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Makhdoom, Farah, Mathura</strong></span><span class="lang-hi"><strong>मखदूम, फरह, मथुरा</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Central Avian Research Institute (CARI)</span><span class="lang-hi">केंद्रीय पक्षी अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Izatnagar, Bareilly</strong></span><span class="lang-hi"><strong>इज्जतनगर, बरेली</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Indian Grassland and Fodder Research Institute</span><span class="lang-hi">भारतीय चारागाह एवं चारा अनुसंधान संस्थान</span></td>
        <td><span class="lang-en"><strong>Jhansi (1962)</strong></span><span class="lang-hi"><strong>झांसी (1962)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Only Central Agricultural University in UP</span><span class="lang-hi">उ.प्र. का एकमात्र केंद्रीय कृषि विश्वविद्यालय</span></td>
        <td><span class="lang-en"><strong>Rani Lakshmi Bai CAU, Jhansi (2014)</strong></span><span class="lang-hi"><strong>रानी लक्ष्मीबाई केंद्रीय कृषि वि.वि., झांसी (2014)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Oldest Agricultural Institute in South Asia</span><span class="lang-hi">दक्षिण एशिया का सबसे पुराना कृषि संस्थान</span></td>
        <td><span class="lang-en"><strong>SHUATS, Prayagraj (founded 1910 by Sam Higginbottom)</strong></span><span class="lang-hi"><strong>शुआट्स (SHUATS), प्रयागराज (1910 में सैम हिग्गिनबॉटम द्वारा स्थापित)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">First Cooperative Milk Union in India</span><span class="lang-hi">भारत का प्रथम दुग्ध सहकारी संघ</span></td>
        <td><span class="lang-en"><strong>Lucknow Dugdh Utpadak Sahkari Sangh (1938)</strong></span><span class="lang-hi"><strong>लखनऊ दुग्ध उत्पादक सहकारी संघ (1938)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Start of Chakbandi in UP</span><span class="lang-hi">उ.प्र. में चकबंदी का प्रारंभ</span></td>
        <td><span class="lang-en"><strong>1954 (Muzaffarnagar &amp; Sultanpur)</strong></span><span class="lang-hi"><strong>1954 (मुजफ्फरनगर एवं सुल्तानपुर)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Launch of Kisan Bahi Yojana</span><span class="lang-hi">किसान बही योजना का प्रारंभ</span></td>
        <td><span class="lang-en"><strong>1992</strong></span><span class="lang-hi"><strong>1992</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Launch Location of PM-KISAN</span><span class="lang-hi">पीएम-किसान योजना का शुभारंभ स्थल</span></td>
        <td><span class="lang-en"><strong>Gorakhpur, UP (24 Feb 2019)</strong></span><span class="lang-hi"><strong>गोरखपुर, उ.प्र. (24 फरवरी 2019)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Primary Irrigation Source in UP</span><span class="lang-hi">उ.प्र. में सिंचाई का प्राथमिक स्रोत</span></td>
        <td><span class="lang-en"><strong>Tubewells (~73.4% of net irrigated area)</strong></span><span class="lang-hi"><strong>नलकूप (शुद्ध सिंचित क्षेत्र का ~73.4%)</strong></span></td>
      </tr>
    </tbody>
  </table>
</div>

</div>
"""

def main():
    target_file = os.path.join("upsssc-up-gk", "agriculture", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    # Find boundaries of <div class="tab-content" id="tab-theory" ...> ... </div>
    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_agriculture_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
