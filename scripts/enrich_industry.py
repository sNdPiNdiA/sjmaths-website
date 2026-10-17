import os
import re

def build_industry_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Industrial Sectors, Manufacturing Hubs &amp; Industrial Authorities of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के औद्योगिक क्षेत्र, विनिर्माण हब एवं औद्योगिक विकास प्राधिकरण</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Industries of Uttar Pradesh] --> B[Agro-Based Industries]
    A --> C[Heavy Industries & PSUs]
    A --> D[Mineral & Chemical Manufacturing]
    A --> E[Traditional Handicrafts & GI Clusters]
    A --> F[High-Tech Electronics & IT Hubs]
    A --> G[Defense Corridor & Industrial Authorities]

    B --> B1[Sugar: 1st Mill Pratappur 1903 Deoria | NSI Kanpur]
    B --> B2[Textiles: Kanpur Manchester of North | PM-MITRA]
    B --> B3[Leather: Kanpur Saddlery & Agra Footwear Hub]

    C --> C1[Locomotives: BLW Varanasi & Modern Coach Raebareli]
    C --> C2[Aviation & Defense: HAL Kanpur & Lucknow | AK-203 Korwa]
    C --> C3[BHEL Jhansi & Jagdishpur | ITI Naini & Mankapur]
    C --> C4[Mathura Refinery: IOCL 1982 | Opium Factory: Ghazipur 1820]

    D --> D1[Aluminum: Hindalco Renukoot Sonbhadra]
    D --> D2[Cement: Churk & Dalla Sonbhadra, Kajrahat]
    D --> D3[Fertilizers: IFFCO Phulpur & HURL Gorakhpur]

    E --> E1[Moradabad Brassware | Firozabad Suhag Nagri Glass]
    E --> E2[Khurja Ceramics | Kannauj Attar Perfumes]
    E --> E3[Bhadohi Carpets | Saharanpur Wood Carving]

    F --> F1[Noida: World's Largest Samsung Mobile Plant]
    F --> F2[YEIDA: Medical Device Park & Toy Park]
    F --> F3[Data Center Parks: Yotta D1 Greater Noida]

    G --> G1[Defense Corridor: 6 Nodes | BrahMos Lucknow]
    G --> G2[Authorities: UPSIDA Kanpur 1958, NOIDA 1976, BIDA Jhansi 2023]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के उद्योग] --> B[कृषि आधारित उद्योग]
    A --> C[भारी उद्योग एवं केंद्रीय उपक्रम (PSUs)]
    A --> D[खनिज एवं रसायन आधारित उद्योग]
    A --> E[पारंपरिक हस्तशिल्प एवं जीआई क्लस्टर]
    A --> F[हाई-टेक इलेक्ट्रॉनिक्स एवं आईटी हब]
    A --> G[रक्षा गलियारा एवं औद्योगिक प्राधिकरण]

    B --> B1[चीनी: प्रथम मिल प्रतापपुर 1903 देवरिया | NSI कानपुर]
    B --> B2[वस्त्र: कानपुर उत्तर का मैनचेस्टर | PM-मित्र पार्क]
    B --> B3[चमड़ा: कानपुर सैडलरी व आगरा जूता निर्यात हब]

    C --> C1[रेलवे इंजन: BLW वाराणसी व मॉडर्न कोच रायबरेली]
    C --> C2[विमानन व रक्षा: HAL कानपुर व लखनऊ | AK-203 कोरवा]
    C --> C3[BHEL झांसी व जगदीशपुर | ITI नैनी व मनकापुर]
    C --> C4[मथुरा रिफाइनरी: IOCL 1982 | अफीम कारखाना: गाजीपुर 1820]

    D --> D1[एल्युमीनियम: हिंडाल्को रेणुकूट सोनभद्र]
    D --> D2[सीमेंट: चुर्क व डाला सोनभद्र, कजराहट]
    D --> D3[उर्वरक: इफ्को फूलपुर व HURL गोरखपुर]

    E --> E1[मुरादाबाद पीतल नगरी | फिरोजाबाद सुहाग नगरी कांच]
    E --> E2[खुर्जा सिरेमिक्स | कन्नौज इत्र राजधानी]
    E --> E3[भदोही कालीन | सहारनपुर काष्ठ नक्काशी]

    F --> F1[नोएडा: सैमसंग की सबसे बड़ी मोबाइल विनिर्माण इकाई]
    F --> F2[यीडा: मेडिकल डिवाइस पार्क व टॉय पार्क]
    F --> F3[डेटा सेंटर पार्क: योट्टा D1 ग्रेटर नोएडा]

    G --> G1[डिफेंस कॉरिडोर: 6 नोड | ब्रह्मोस विनिर्माण लखनऊ]
    G --> G2[प्राधिकरण: UPSIDA कानपुर 1958, NOIDA 1976, BIDA झांसी 2023]
    </div>
  </div>
</div>

<!-- Card 2: Traditional Agro-Based Industries -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Agro-Based Industries: Sugar, Cotton Textiles &amp; Leather</span>
    <span class="lang-hi">1. कृषि-आधारित उद्योग: चीनी, सूती वस्त्र एवं चमड़ा उद्योग</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Sugar Industry (चीनी उद्योग) - Crown Agro-Industry:</strong>
        <br/>• <strong>Historic Inception:</strong> India and UP's <strong>first modern sugar mill was established in 1903 at Pratappur (Deoria district)</strong>.
        <br/>• <strong>National Status:</strong> UP is the leading sugarcane and sugar-producing state, known as the <em>'Sugar Bowl of India'</em>, operating over 120 sugar mills.
        <br/>• <strong>Geographical Belt:</strong> Concentrated in the upper Ganga-Yamuna Doab (Meerut, Muzaffarnagar, Saharanpur, Baghpat) and the Terai belt (Lakhimpur Kheri, Gonda, Basti, Deoria).
        <br/>• <strong>Premier Apex Institutes:</strong>
        <br/>  - <em>National Sugar Institute (NSI):</em> Kalyanpur, Kanpur (est. 1936).
        <br/>  - <em>Indian Institute of Sugarcane Research (IISR):</em> Dilkusha, Lucknow (est. 1952).
        <br/>  - <em>UP Sugarcane Research Council:</em> Shahjahanpur (est. 1912).
      </span>
      <span class="lang-hi"><strong>चीनी उद्योग - उ.प्र. का शीर्ष कृषि उद्योग:</strong>
        <br/>• <strong>ऐतिहासिक प्रारंभ:</strong> भारत तथा उत्तर प्रदेश की <strong>प्रथम आधुनिक चीनी मिल 1903 में प्रतापपुर (देवरिया जिला)</strong> में स्थापित की गई थी।
        <br/>• <strong>राष्ट्रीय स्थिति:</strong> उ.प्र. देश का सबसे बड़ा गन्ना एवं चीनी उत्पादक राज्य है ('भारत का चीनी का कटोरा'); यहाँ 120 से अधिक चीनी मिलें कार्यरत हैं।
        <br/>• <strong>प्रमुख भौगोलिक बेल्ट:</strong> ऊपरी गंगा-यमुना दोआब (मेरठ, मुजफ्फरनगर, सहारनपुर, बागपत) तथा तराई पट्टी (लखीमपुर खीरी, गोंडा, बस्ती, देवरिया)।
        <br/>• <strong>शीर्ष अनुसंधान संस्थान:</strong>
        <br/>  - <em>राष्ट्रीय शर्करा संस्थान (NSI):</em> कल्याणपुर, कानपुर (स्थापना 1936)।
        <br/>  - <em>भारतीय गन्ना अनुसंधान संस्थान (IISR):</em> दिलकुशा, लखनऊ (स्थापना 1952)।
        <br/>  - <em>उ.प्र. गन्ना शोध परिषद:</em> शाहजहांपुर (स्थापना 1912)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Cotton Textile Industry (सूती वस्त्र उद्योग):</strong>
        <br/>• <strong>Manchester of North India:</strong> <strong>Kanpur</strong> is historically renowned as the <em>'Manchester of North India' (उत्तर भारत का मैनचेस्टर)</em>, pioneered by the establishment of <em>Elgin Mills (1862)</em> and <em>Muir Mills (1874)</em>.
        <br/>• <strong>Government Central Textile Institute (UPTTI):</strong> Located at Kanpur.
        <br/>• <strong>Handloom &amp; Weaving Clusters:</strong> Varanasi (world-famous Banarasi Silk Sarees &amp; Zari brocades, GI Tagged), Mau (powerloom and cotton hub of Purvanchal), Mubarakpur (Azamgarh - silk weaving), Tanda (Ambedkar Nagar - Tericot &amp; Jamdani), Pilkhuwa (Hapur - handblock printing), and Sikandrabad (Bulandshahr).
        <br/>• <strong>PM-MITRA Mega Textile Park:</strong> 1,000-acre world-class integrated textile hub sanctioned at <strong>Attari village (Lucknow-Hardoi border)</strong>.
      </span>
      <span class="lang-hi"><strong>सूती वस्त्र उद्योग:</strong>
        <br/>• <strong>उत्तर भारत का मैनचेस्टर:</strong> <strong>कानपुर</strong> को सूती वस्त्र मिलों की सघनता के कारण <em>'उत्तर भारत का मैनचेस्टर'</em> कहा जाता है; <em>एल्गिन मिल्स (1862)</em> तथा <em>म्योर मिल्स (1874)</em> द्वारा औद्योगिक आधार स्थापित।
        <br/>• <strong>राजकीय वस्त्र प्रौद्योगिकी संस्थान:</strong> कानपुर में स्थित।
        <br/>• <strong>हथकरघा एवं बुनाई केंद्र:</strong> वाराणसी (विश्व प्रसिद्ध बनारसी रेशमी साड़ियां व जरी ब्रोकेड, GI टैग), मऊ (पूर्वांचल का पावरलूम हब), मुबारकपुर (आजमगढ़ - रेशम बुनाई), टांडा (अंबेडकर नगर - टेरीकॉट व जामदानी), पिलखुवा (हापुड़ - स्क्रीन प्रिंटिंग व चादरें)।
        <br/>• <strong>PM-मित्र मेगा टेक्सटाइल पार्क:</strong> <strong>अटारी गांव (लखनऊ-हरदोई सीमा)</strong> पर 1,000 एकड़ में ₹1,200 करोड़ की लागत से स्वीकृत।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Leather &amp; Footwear Industry (चमड़ा एवं फुटवियर उद्योग):</strong>
        <br/>• <strong>Kanpur:</strong> The premier global center for industrial leather, hides, animal saddlery (घोड़े की काठी), harnesses, and army footwear; regional center of Central Leather Research Institute (CLRI) located here.
        <br/>• <strong>Agra:</strong> India's largest footwear manufacturing and export cluster, accounting for over <strong>65% of domestic shoe production and ~28% of national footwear exports</strong>.
        <br/>• <strong>Mega Leather Park:</strong> Sanctioned at <strong>Ramaipur (Kanpur Nagar)</strong> over 235 acres under the Mega Investment Textile Parks/Leather scheme.
      </span>
      <span class="lang-hi"><strong>चमड़ा एवं फुटवियर उद्योग:</strong>
        <br/>• <strong>कानपुर:</strong> औद्योगिक चमड़ा, टैनरी, पशु काठी (सैडलरी), हार्नेस तथा रक्षा जूतों का विश्व प्रसिद्ध केंद्र; केंद्रीय चर्म अनुसंधान संस्थान (CLRI) की शाखा स्थापित।
        <br/>• <strong>आगरा:</strong> भारत का शीर्ष जूता निर्माण एवं निर्यात हब; देश के कुल घरेलू जूता उत्पादन का <strong>65% तथा राष्ट्रीय फुटवियर निर्यात का ~28% हिस्सा</strong> अकेले आगरा से आता है।
        <br/>• <strong>मेगा लेदर पार्क:</strong> <strong>रमैईपुर (कानपुर नगर)</strong> में 235 एकड़ में ₹5,850 करोड़ के निवेश वाला अत्याधुनिक लेदर क्लस्टर स्थापित।
      </span>
    </li>
  </ul>
</div>

<!-- Card 3: Heavy Public Sector Undertakings & Defense Industry -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Central PSUs, Heavy Engineering &amp; Strategic Defense Facilities</span>
    <span class="lang-hi">2. केंद्रीय सार्वजनिक उपक्रम (PSUs), भारी इंजीनियरिंग एवं रक्षा विनिर्माण</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Railways &amp; Heavy Transport Engineering:</strong>
        <br/>• <strong>Banaras Locomotive Works (BLW, Varanasi):</strong> Formerly Diesel Locomotive Works (DLW, est. 1961); manufactures state-of-the-art heavy freight and passenger electric/diesel locomotive engines.
        <br/>• <strong>Modern Coach Factory (MCF, Lalganj, Raebareli):</strong> India's ultra-modern passenger rail coach factory (est. 2012); manufactures stainless steel LHB and Vande Bharat train coaches.
        <br/>• <strong>BHEL (Bharat Heavy Electricals Ltd):</strong> Units operating in <strong>Jhansi</strong> (locomotives and transformers), <strong>Jagdishpur</strong> (Amethi - industrial turbines), and <strong>Varanasi</strong> (heavy electricals).
      </span>
      <span class="lang-hi"><strong>रेलवे एवं भारी परिवहन इंजीनियरिंग:</strong>
        <br/>• <strong>बनारस लोकोमोटिव वर्क्स (BLW, वाराणसी):</strong> पूर्व में डीजल रेल इंजन कारखाना (DLW, 1961); अत्याधुनिक विद्युत एवं डीजल रेल इंजनों का निर्माण।
        <br/>• <strong>मॉडर्न कोच फैक्ट्री (MCF, लालगंज, रायबरेली):</strong> देश का तीसरा अत्याधुनिक रेल डिब्बा कारखाना (2012); एलएचबी व वंदे भारत डिब्बों का निर्माण।
        <br/>• <strong>भारत हेवी इलेक्ट्रिकल्स लिमिटेड (BHEL):</strong> <strong>झांसी</strong> (विद्युत ट्रांसफार्मर व लोकोमोटिव), <strong>जगदीशपुर</strong> (अमेठी) तथा <strong>वाराणसी</strong> में इकाइयाँ।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Aeronautics &amp; Strategic Defense Manufacturing:</strong>
        <br/>• <strong>Hindustan Aeronautics Limited (HAL):</strong>
        <br/>  - <em>Kanpur Division:</em> Manufactures Transport Aircraft (Dornier 228, Avro HS-748).
        <br/>  - <em>Lucknow Division:</em> Manufactures advanced aircraft accessories, hydraulics, and avionics.
        <br/>  - <em>Korwa Division (Amethi):</em> Manufactures advanced navigation systems.
        <br/>• <strong>Ordnance Factories:</strong> Small Arms Factory (SAF, Kanpur), Field Gun Factory (Kanpur), Ordnance Clothing Factory (Shahjahanpur), Ordnance Equipment Factory (OEF, Hazratpur, Firozabad &amp; Kanpur), and Ordnance Factory Muradnagar (Ghaziabad - metallurgical steel).
        <br/>• <strong>Indo-Russian Rifles Private Limited (IRRPL):</strong> State-of-the-art plant at <strong>Korwa (Amethi)</strong> manufacturing <strong>AK-203 assault rifles</strong> for the Indian Armed Forces.
        <br/>• <strong>BrahMos Aerospace:</strong> 200-acre Next-Gen missile manufacturing plant at <strong>Bhatgaon node (Lucknow)</strong> of the UP Defense Industrial Corridor.
      </span>
      <span class="lang-hi"><strong>वैमानिकी एवं रणनीतिक रक्षा विनिर्माण:</strong>
        <br/>• <strong>हिंदुस्तान एयरोनॉटिक्स लिमिटेड (HAL):</strong>
        <br/>  - <em>कानपुर प्रभाग:</em> परिवहन विमानों (डोर्नियर 228, एवरो) का निर्माण।
        <br/>  - <em>लखनऊ प्रभाग:</em> विमान सहायक उपकरण, हाइड्रोलिक्स एवं एवियोनिक्स का निर्माण।
        <br/>  - <em>कोरवा प्रभाग (अमेठी):</em> आधुनिक नेविगेशन प्रणाली का निर्माण।
        <br/>• <strong>आयुध कारखाने (Ordnance Factories):</strong> लघु शस्त्र निर्माणी (SAF, कानपुर), फील्ड गन फैक्ट्री (कानपुर), आयुध वस्त्र निर्माणी (शाहजहांपुर), आयुध उपस्कर निर्माणी (हजरतपुर, फिरोजाबाद व कानपुर), तथा आयुध निर्माणी मुरादनगर (गाजियाबाद)।
        <br/>• <strong>इंडो-रशियन राइफल्स (IRRPL):</strong> <strong>कोरवा (अमेठी)</strong> में भारतीय सेना हेतु <strong>AK-203 असॉल्ट राइफल</strong> विनिर्माण इकाई।
        <br/>• <strong>ब्रह्मोस एयरोस्पेस:</strong> उ.प्र. रक्षा औद्योगिक गलियारे के तहत <strong>भाटगांव (लखनऊ)</strong> में 200 एकड़ में अत्याधुनिक ब्रह्मोस नेक्स्ट-जेन मिसाइल विनिर्माण इकाई।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Petroleum, Telecommunications &amp; Opium:</strong>
        <br/>• <strong>Mathura Refinery (IOCL):</strong> Established in <strong>1982</strong> with an initial capacity of 6.0 MMTPA (expanded to 8.0 MMTPA); only oil refinery in Uttar Pradesh.
        <br/>• <strong>Indian Telephone Industries (ITI):</strong> Telecommunication hardware plants at <strong>Naini (Prayagraj)</strong>, <strong>Raebareli</strong>, and <strong>Mankapur (Gonda)</strong>.
        <br/>• <strong>Government Opium and Alkaloid Works, Ghazipur:</strong> Established by the British in <strong>1820</strong> on the banks of Ganga; the <strong>oldest and largest legal government opium manufacturing factory in India</strong>.
      </span>
      <span class="lang-hi"><strong>पेट्रोलियम, दूरसंचार एवं अफीम कारखाना:</strong>
        <br/>• <strong>मथुरा तेल शोधक कारखाना (IOCL):</strong> स्थापना <strong>1982</strong>; उत्तर प्रदेश की एकमात्र तेल रिफाइनरी (क्षमता 8.0 MMTPA)।
        <br/>• <strong>इंडियन टेलीफोन इंडस्ट्रीज (ITI):</strong> <strong>नैनी (प्रयागराज)</strong>, <strong>रायबरेली</strong> तथा <strong>मनकापुर (गोंडा)</strong> में दूरसंचार उपकरण इकाइयां।
        <br/>• <strong>शासकीय अफीम एवं क्षारोद कारखाना, गाजीपुर:</strong> अंग्रेजों द्वारा <strong>1820 में स्थापित</strong>; भारत का <strong>सबसे पुराना व सबसे बड़ा सरकारी अफीम कारखाना</strong>।
      </span>
    </li>
  </ul>
</div>

<!-- Card 4: Mineral & Chemical-Based Industries -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Mineral-Based &amp; Chemical Industries (Cement, Aluminum &amp; Fertilizer)</span>
    <span class="lang-hi">3. खनिज एवं रसायन-आधारित उद्योग (सीमेंट, एल्युमीनियम एवं उर्वरक)</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Aluminum Industry - Hindalco (Renukoot, Sonbhadra):</strong>
        <br/>• Established in 1962 by the Aditya Birla Group at Renukoot; one of Asia's largest integrated aluminum smelters.
        <br/>• Raw Material: Bauxite sourced from Lohardaga (Jharkhand), Banda, and MP.
        <br/>• Power: Captive hydro-power from the adjoining <strong>Rihand Dam (Govind Ballabh Pant Sagar)</strong>.
      </span>
      <span class="lang-hi"><strong>एल्युमीनियम उद्योग - हिंडाल्को (रेणुकूट, सोनभद्र):</strong>
        <br/>• आदित्य बिड़ला समूह द्वारा 1962 में रेणुकूट में स्थापित; एशिया का प्रमुख एकीकृत एल्युमीनियम संयंत्र।
        <br/>• कच्चा माल: बॉक्साइट (बांदा, लोहरदगा व म.प्र. से)।
        <br/>• ऊर्जा स्रोत: समीपवर्ती <strong>रिहंद बांध (गोविंद बल्लभ पंत सागर)</strong> से जल विद्युत।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Cement Industry (सीमेंट उद्योग):</strong>
        <br/>• Primary limestone-belt plants located in <strong>Churk, Dalla, and Kajrahat (Sonbhadra district)</strong>, historically set up under the UP State Cement Corporation.
        <br/>• Clinker grinding units: Sikandrabad (Bulandshahr), Jhansi (Diamond Cement), Aligarh, and Tanda (Ambedkar Nagar).
      </span>
      <span class="lang-hi"><strong>सीमेंट उद्योग:</strong>
        <br/>• विंध्य चूना पत्थर बेल्ट पर आधारित प्रमुख संयंत्र: <strong>चुर्क, डाला तथा कजराहट (सोनभद्र जिला)</strong>।
        <br/>• क्लिंकर ग्राइंडिंग इकाइयां: सिकंदराबाद (बुलंदशहर), झांसी, अलीगढ़ तथा टांडा (अंबेडकर नगर)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Chemical Fertilizer Plants (रासायनिक उर्वरक उद्योग):</strong>
        <br/>• <strong>IFFCO Phulpur (Prayagraj):</strong> Massive gas-based urea manufacturing complex; world's first commercial Nano Urea liquid plant operational here.
        <br/>• <strong>IFFCO Aonla (Bareilly):</strong> Major gas-based nitrogenous fertilizer complex along HBJ pipeline.
        <br/>• <strong>HURL Gorakhpur:</strong> Modernized urea complex with a landmark 149.2-meter natural draft prilling tower.
        <br/>• <strong>Duncans Fertilizers (Kanpur):</strong> Manufactures urea under the popular 'Chandachap' brand.
      </span>
      <span class="lang-hi"><strong>रासायनिक उर्वरक संयंत्र:</strong>
        <br/>• <strong>इफ्को फूलपुर (प्रयागराज):</strong> प्राकृतिक गैस आधारित विशाल यूरिया संयंत्र; विश्व का प्रथम व्यावसायिक नैनो यूरिया प्लांट यहीं स्थापित।
        <br/>• <strong>इफ्को आंवला (बरेली):</strong> HBJ गैस पाइपलाइन पर आधारित विशाल यूरिया उत्पादक संयंत्र।
        <br/>• <strong>HURL गोरखपुर:</strong> 149.2 मीटर ऊंचे प्रिलिंग टॉवर से युक्त पुनर्जीवित यूरिया खाद कारखाना।
        <br/>• <strong>डंकन फर्टिलाइजर्स (कानपुर):</strong> 'चांद छाप' ब्रांड यूरिया का विनिर्माण।
      </span>
    </li>
  </ul>
</div>

<!-- Card 5: Specialized Handicrafts & GI Tag Industrial Clusters -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Traditional Cottage Handicrafts &amp; GI Product Clusters</span>
    <span class="lang-hi">4. पारंपरिक कुटीर हस्तशिल्प एवं जीआई उत्पाद औद्योगिक क्लस्टर</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Industrial Cluster / Product</span><span class="lang-hi">औद्योगिक क्लस्टर / उत्पाद</span></th>
          <th><span class="lang-en">Key District / Hub</span><span class="lang-hi">प्रमुख जिला / केंद्र</span></th>
          <th><span class="lang-en">Popular Epithet / Distinction</span><span class="lang-hi">प्रसिद्ध उपनाम / विशिष्टता</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Brassware &amp; Metal Artware</strong></span><span class="lang-hi"><strong>पीतल के बर्तन एवं धातु हस्तशिल्प</strong></span></td>
          <td><span class="lang-en">Moradabad</span><span class="lang-hi">मुरादाबाद</span></td>
          <td><span class="lang-en"><em>'Peetal Nagari'</em> (Brass City) - accounts for 40%+ of India's handicraft exports</span><span class="lang-hi"><em>'पीतल नगरी'</em> - देश के कुल हस्तशिल्प निर्यात का 40% से अधिक हिस्सा</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Glass Bangles &amp; Glassware</strong></span><span class="lang-hi"><strong>कांच की चूड़ियां एवं कांच उत्पाद</strong></span></td>
          <td><span class="lang-en">Firozabad</span><span class="lang-hi">फिरोजाबाद</span></td>
          <td><span class="lang-en"><em>'Suhag Nagri'</em> / City of Bangles - dominant glass manufacturing cluster of India</span><span class="lang-hi"><em>'सुहाग नगरी'</em> - कांच की चूड़ियों एवं कलात्मक झूमरों का राष्ट्रीय केंद्र</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Ceramics &amp; Glazed Pottery</strong></span><span class="lang-hi"><strong>सिरेमिक्स एवं चीनी मिट्टी बर्तन</strong></span></td>
          <td><span class="lang-en">Khurja (Bulandshahr)</span><span class="lang-hi">खुर्जा (बुलंदशहर)</span></td>
          <td><span class="lang-en"><em>'Ceramic City'</em> - Central Glass &amp; Ceramic Research Institute (CGCRI) centre</span><span class="lang-hi"><em>'सिरेमिक सिटी'</em> - केंद्रीय कांच एवं सिरेमिक अनुसंधान संस्थान का केंद्र</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Black Clay Pottery</strong></span><span class="lang-hi"><strong>काली मिट्टी के बर्तन (ब्लैक पॉटरी)</strong></span></td>
          <td><span class="lang-en">Nizamabad (Azamgarh)</span><span class="lang-hi">निजामाबाद (आजमगढ़)</span></td>
          <td><span class="lang-en">Unique silver inlay on smoke-treated black clay pottery (GI Tagged)</span><span class="lang-hi">काले बर्तन पर चांदी जैसी नक्काशी (GI टैग प्राप्त)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Terracotta Crafts</strong></span><span class="lang-hi"><strong>टेराकोटा शिल्प</strong></span></td>
          <td><span class="lang-en">Gorakhpur (Gulriha, Bhathat)</span><span class="lang-hi">गोरखपुर (गुलरिहा)</span></td>
          <td><span class="lang-en">Natural clay elephant figurines and temple sculptures (GI Tagged / ODOP)</span><span class="lang-hi">हाथी, घोड़े व मूर्तिकला के मिट्टी शिल्प (GI टैग व ODOP उत्पाद)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Locks &amp; Hardware</strong></span><span class="lang-hi"><strong>ताले एवं हार्डवेयर उद्योग</strong></span></td>
          <td><span class="lang-en">Aligarh</span><span class="lang-hi">अलीगढ़</span></td>
          <td><span class="lang-en"><em>'Taala Nagri'</em> (City of Locks) - over 75% of Indian manual/brass locks</span><span class="lang-hi"><em>'ताला नगरी'</em> - देश के 75% से अधिक तालों का विनिर्माण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Handmade Knotted Carpets</strong></span><span class="lang-hi"><strong>हाथ से बुने कालीन (कार्पेट)</strong></span></td>
          <td><span class="lang-en">Bhadohi &amp; Mirzapur</span><span class="lang-hi">भदोही एवं मिर्जापुर</span></td>
          <td><span class="lang-en"><em>'Carpet City of South Asia'</em> - Indian Institute of Carpet Technology (IICT) Bhadohi</span><span class="lang-hi"><em>'कालीन नगरी'</em> - भारतीय कालीन प्रौद्योगिकी संस्थान (IICT) भदोही</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Wood Carving (काष्ठ नक्काशी)</strong></span><span class="lang-hi"><strong>काष्ठ नक्काशी एवं फर्नीचर</strong></span></td>
          <td><span class="lang-en">Saharanpur &amp; Nagina (Bijnor)</span><span class="lang-hi">सहारनपुर व नगीना (बिजनौर)</span></td>
          <td><span class="lang-en">Intricate Sheesham open-work screens, brass inlay furniture (GI Tagged)</span><span class="lang-hi">शीशम की लकड़ी पर बारीक नक्काशी व पीतल जड़ाई (GI टैग प्राप्त)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Natural Attar &amp; Perfumes</strong></span><span class="lang-hi"><strong>प्राकृतिक इत्र एवं सुगंध तेल</strong></span></td>
          <td><span class="lang-en">Kannauj</span><span class="lang-hi">कन्नौज</span></td>
          <td><span class="lang-en"><em>'Perfume Capital of India'</em> - traditional hydro-distillation Deg-Bhapka attar</span><span class="lang-hi"><em>'इत्र नगरी'</em> - प्राचीन देग-भपका आसवन विधि से गुलाब व खस इत्र निर्माण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Handmade Paper (हस्तनिर्मित कागज)</strong></span><span class="lang-hi"><strong>हस्तनिर्मित कागज</strong></span></td>
          <td><span class="lang-en">Kalpi (Jalaun)</span><span class="lang-hi">कालपी (जालौन)</span></td>
          <td><span class="lang-en">Centuries-old handmade paper crafted from waste cotton rags (ODOP / GI Tag)</span><span class="lang-hi">कपास की कतरन से हस्तनिर्मित पर्यावरण अनुकूल कागज (GI टैग)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 6: Industrial Development Authorities of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Industrial Development Authorities &amp; Defense Corridor Nodes</span>
    <span class="lang-hi">5. उत्तर प्रदेश के औद्योगिक विकास प्राधिकरण एवं डिफेंस कॉरिडोर नोड</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Statutory Industrial Development Authorities:</strong>
        <br/>• <strong>UPSIDA (UP State Industrial Development Authority):</strong> Headquartered at <strong>Kanpur</strong> (established in 1958 as UPSIDC; apex body managing 150+ industrial areas across UP).
        <br/>• <strong>NOIDA (New Okhla Industrial Development Authority):</strong> Constituted on <strong>April 17, 1976</strong>, under the UP Industrial Area Development Act, 1976.
        <br/>• <strong>GNIDA (Greater Noida Industrial Development Authority):</strong> Established in <strong>January 1991</strong>.
        <br/>• <strong>YEIDA (Yamuna Expressway Industrial Development Authority):</strong> Established in <strong>April 2001</strong>; developing Noida International Airport, Medical Device Park, and Data Centers.
        <br/>• <strong>GIDA (Gorakhpur Industrial Development Authority):</strong> Established in <strong>1989</strong> for industrialization of Eastern UP.
        <br/>• <strong>SIDA (Satharia Industrial Development Authority):</strong> Established in <strong>1989 at Jaunpur</strong>.
        <br/>• <strong>BIDA (Bundelkhand Industrial Development Authority):</strong> Newly notified in <strong>2023 at Jhansi</strong> (spanning 35,000+ acres along the lines of Noida to transform Bundelkhand).
      </span>
      <span class="lang-hi"><strong>वैधानिक औद्योगिक विकास प्राधिकरण:</strong>
        <br/>• <strong>UPSIDA (उ.प्र. राज्य औद्योगिक विकास प्राधिकरण):</strong> मुख्यालय <strong>कानपुर</strong> (स्थापना 1958; राज्य के 150+ औद्योगिक क्षेत्रों का प्रबंधन करने वाली शीर्ष संस्था)।
        <br/>• <strong>NOIDA (नवीन ओखला औद्योगिक विकास प्राधिकरण):</strong> स्थापना <strong>17 अप्रैल 1976</strong>।
        <br/>• <strong>GNIDA (ग्रेटर नोएडा औद्योगिक विकास प्राधिकरण):</strong> स्थापना <strong>जनवरी 1991</strong>।
        <br/>• <strong>YEIDA (यमुना एक्सप्रेसवे औद्योगिक विकास प्राधिकरण):</strong> स्थापना <strong>अप्रैल 2001</strong>; जेवर एयरपोर्ट, मेडिकल डिवाइस पार्क का विकास।
        <br/>• <strong>GIDA (गीडा - गोरखपुर औद्योगिक विकास प्राधिकरण):</strong> स्थापना <strong>1989</strong>; पूर्वांचल के औद्योगीकरण हेतु।
        <br/>• <strong>SIDA (सीडा - सतहरिया औद्योगिक विकास प्राधिकरण):</strong> स्थापना <strong>1989 (जौनपुर)</strong>।
        <br/>• <strong>BIDA (बीडा - बुंदेलखंड औद्योगिक विकास प्राधिकरण):</strong> <strong>2023 में झांसी में अधिसूचित</strong> (नोएडा की तर्ज पर 35,000 एकड़ में विकसित नया औद्योगिक शहर)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>UP Defense Industrial Corridor (6 Strategic Nodes):</strong>
        <br/>• <strong>Nodes:</strong> 1. Agra, 2. Aligarh, 3. Chitrakoot, 4. Jhansi, 5. Kanpur, 6. Lucknow.
        <br/>• <strong>BrahMos Aerospace Unit:</strong> Located at <strong>Bhatgaon node, Lucknow</strong>.
        <br/>• <strong>Bharat Dynamics Limited (BDL):</strong> Propulsion system unit at <strong>Jhansi node</strong>.
        <br/>• <strong>Small Arms &amp; Drones:</strong> Kanpur and Aligarh nodes.
      </span>
      <span class="lang-hi"><strong>उ.प्र. रक्षा औद्योगिक गलियारा (6 रणनीतिक नोड):</strong>
        <br/>• <strong>6 नोड:</strong> 1. आगरा, 2. अलीगढ़, 3. चित्रकूट, 4. झांसी, 5. कानपुर, 6. लखनऊ।
        <br/>• <strong>ब्रह्मोस एयरोस्पेस:</strong> <strong>भाटगांव (लखनऊ नोड)</strong> में नेक्स्ट-जेन मिसाइल विनिर्माण।
        <br/>• <strong>भारत डायनेमिक्स लिमिटेड (BDL):</strong> <strong>झांसी नोड</strong> में प्रणोदन प्रणाली विनिर्माण।
        <br/>• <strong>लघु अस्त्र एवं ड्रोन हब:</strong> कानपुर एवं अलीगढ़ नोड।
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Fact Matrix: UP Industries (Direct Exam Points)</span>
    <span class="lang-hi">6. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. के उद्योग (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Industrial Fact</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / औद्योगिक तथ्य</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Where was the first sugar mill in India and UP established?</span><span class="lang-hi">भारत एवं उ.प्र. की प्रथम चीनी मिल कहाँ स्थापित की गई थी?</span></td>
          <td><span class="lang-en"><strong>Pratappur (Deoria district) in 1903</strong></span><span class="lang-hi"><strong>प्रतापपुर (देवरिया जिला) में वर्ष 1903 में</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city is known as the 'Manchester of North India'?</span><span class="lang-hi">किस नगर को 'उत्तर भारत का मैनचेस्टर' कहा जाता है?</span></td>
          <td><span class="lang-en"><strong>Kanpur (कानपुर)</strong></span><span class="lang-hi"><strong>कानपुर</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the National Sugar Institute (NSI) located?</span><span class="lang-hi">राष्ट्रीय शर्करा संस्थान (NSI) कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Kanpur (Kalyanpur)</strong> (established in 1936)</span><span class="lang-hi"><strong>कानपुर (कल्याणपुर)</strong> (स्थापना 1936)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Indian Institute of Sugarcane Research (IISR) located?</span><span class="lang-hi">भारतीय गन्ना अनुसंधान संस्थान (IISR) कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Lucknow (Dilkusha)</strong> (established in 1952)</span><span class="lang-hi"><strong>लखनऊ (दिलकुशा)</strong> (स्थापना 1952)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city in UP is world-famous as 'Peetal Nagari' (Brass City)?</span><span class="lang-hi">उ.प्र. का कौन सा शहर 'पीतल नगरी' के रूप में विश्व विख्यात है?</span></td>
          <td><span class="lang-en"><strong>Moradabad (मुरादाबाद)</strong></span><span class="lang-hi"><strong>मुरादाबाद</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city is renowned as 'Suhag Nagri' for its glass bangles?</span><span class="lang-hi">कांच की चूड़ियों के लिए कौन सा शहर 'सुहाग नगरी' कहलाता है?</span></td>
          <td><span class="lang-en"><strong>Firozabad (फिरोजाबाद)</strong></span><span class="lang-hi"><strong>फिरोजाबाद</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which town is known as the 'Ceramic City' of Uttar Pradesh?</span><span class="lang-hi">उ.प्र. का कौन सा कस्बा 'सिरेमिक सिटी' कहलाता है?</span></td>
          <td><span class="lang-en"><strong>Khurja (Bulandshahr district)</strong></span><span class="lang-hi"><strong>खुर्जा (बुलंदशहर जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Hindalco aluminum plant located in UP?</span><span class="lang-hi">उ.प्र. में हिंडाल्को एल्युमीनियम संयंत्र कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Renukoot (Sonbhadra district)</strong></span><span class="lang-hi"><strong>रेणुकूट (सोनभद्र जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the only oil refinery in Uttar Pradesh located?</span><span class="lang-hi">उत्तर प्रदेश की एकमात्र तेल रिफाइनरी कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Mathura Refinery (IOCL, established 1982)</strong></span><span class="lang-hi"><strong>मथुरा तेल शोधनशाला (IOCL, स्थापना 1982)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the oldest legal Government Opium Factory in India located?</span><span class="lang-hi">भारत का सबसे पुराना सरकारी अफीम कारखाना कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Ghazipur (गाजीपुर)</strong> (established in 1820)</span><span class="lang-hi"><strong>गाजीपुर</strong> (स्थापना 1820)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Modern Coach Factory (MCF) of Indian Railways located?</span><span class="lang-hi">भारतीय रेलवे की मॉडर्न कोच फैक्ट्री कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Lalganj, Raebareli</strong></span><span class="lang-hi"><strong>लालगंज, रायबरेली</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where are AK-203 assault rifles manufactured in UP?</span><span class="lang-hi">उ.प्र. में AK-203 असॉल्ट राइफलों का निर्माण कहाँ होता है?</span></td>
          <td><span class="lang-en"><strong>Korwa (Amethi district)</strong> by IRRPL</span><span class="lang-hi"><strong>कोरवा (अमेठी जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Indian Institute of Carpet Technology (IICT) located?</span><span class="lang-hi">भारतीय कालीन प्रौद्योगिकी संस्थान (IICT) कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Bhadohi (भदोही)</strong></span><span class="lang-hi"><strong>भदोही</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city in UP is famous as the 'Perfume Capital' (इत्र नगरी)?</span><span class="lang-hi">उत्तर प्रदेश की 'इत्र नगरी' के नाम से कौन सा शहर प्रसिद्ध है?</span></td>
          <td><span class="lang-en"><strong>Kannauj (कन्नौज)</strong></span><span class="lang-hi"><strong>कन्नौज</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the headquarters of UPSIDA located?</span><span class="lang-hi">UPSIDA का मुख्यालय कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Kanpur (established in 1958)</strong></span><span class="lang-hi"><strong>कानपुर (स्थापना 1958)</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "industry", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_industry_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
