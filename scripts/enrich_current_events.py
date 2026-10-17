import os
import re

def build_current_events_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Contemporary Achievements, Infrastructure &amp; Governance of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की समसामयिक उपलब्धियां, अवसंरचना एवं शासन सुधार</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Current Events & Achievements of UP] --> B[Expressway Capital: 6 Active + 7 Planned]
    A --> C[Aviation Hub: 5 International Airports]
    A --> D[Mega Projects & Defense Corridor]
    A --> E[Urban Transit: Metro & RRTS Namo Bharat]
    A --> F[Governance: EoDB Rank 2 & e-Portals]
    A --> G[Welfare Schemes & Atal Schools]
    A --> H[Sports Milestones & GI Tag Leadership]

    B --> B1[Purvanchal: 341 km | Lucknow to Ghazipur]
    B --> B2[Bundelkhand: 296 km | Chitrakoot to Etawah]
    B --> B3[Ganga Expressway: 594 km | Meerut to Prayagraj]
    B --> B4[Gorakhpur Link: 91 km | Emergency Airstrips]

    C --> C1[Jewar Noida: Asia's Largest Greenfield Airport]
    C --> C2[Ayodhya Dham: Maharishi Valmiki Airport]
    C --> C3[Lucknow, Varanasi & Kushinagar Active]

    D --> D1[Defense Corridor: 6 Nodes - BrahMos Lucknow]
    D --> D2[PM-MITRA Textile Park: Lucknow-Hardoi 1000 Acres]
    D --> D3[Medical Device Park: YEIDA | Bulk Drug: Lalitpur]

    E --> E1[Namo Bharat: India's 1st RRTS Delhi-Meerut 82 km]
    E --> E2[Metro Leader: 5 Cities - Lucknow, Kanpur, Agra, Noida, Gzb]
    E --> E3[NW-1 Ganga: Multimodal Varanasi & MV Ganga Vilas]

    F --> F1[Budget 2024-25: ₹7.36 Lakh Crore Largest Ever]
    F --> F2[Nivesh Mitra: 400+ Online Clearances]
    F --> F3[7 Police Commissionerates: Lucknow, Noida, Vns, Knpr, etc.]

    G --> G1[Atal Residential Schools: 18 Divisional Centers]
    G --> G2[Rank 1 e-Shram Portal: 8.3+ Crore Workers]
    G --> G3[Abhyudaya Free Coaching & Mission Shakti 4.0]

    H --> H1[Major Dhyan Chand Sports Univ: Meerut]
    H --> H2[ODOS Scheme: 75 Districts | Khelo India 2023]
    H --> H3[GI Tag Leader: 75+ Registered Products]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उ.प्र. की समसामयिक उपलब्धियां] --> B[एक्सप्रेसवे प्रदेश: 6 चालू + 7 प्रस्तावित]
    A --> C[नागरिक उड्डयन: 5 अंतरराष्ट्रीय हवाई अड्डे]
    A --> D[मेगा औद्योगिक परियोजनाएं व रक्षा गलियारा]
    A --> E[नगरीय परिवहन: मेट्रो व नमो भारत RRTS]
    A --> F[सुशासन: EoDB रैंक 2 व डिजिटल पोर्टल]
    A --> G[जनकल्याणकारी योजनाएं व अटल विद्यालय]
    A --> H[खेल उपलब्धियां व जीआई टैग में अग्रणी]

    B --> B1[पूर्वांचल: 341 किमी | लखनऊ से गाजीपुर]
    B --> B2[बुंदेलखंड: 296 किमी | चित्रकूट से इटावा]
    B --> B3[गंगा एक्सप्रेसवे: 594 किमी | मेरठ से प्रयागराज]
    B --> B4[गोरखपुर लिंक: 91 किमी | आपातकालीन हवाई पट्टी]

    C --> C1[जेवर नोएडा: एशिया का सबसे बड़ा ग्रीनफील्ड एयरपोर्ट]
    C --> C2[अयोध्या धाम: महर्षि वाल्मीकि अंतरराष्ट्रीय हवाई अड्डा]
    C --> C3[लखनऊ, वाराणसी एवं कुशीनगर पहले से संचालित]

    D --> D1[डिफेंस कॉरिडोर: 6 नोड - ब्रह्मोस विनिर्माण लखनऊ]
    D --> D2[PM-मित्र टेक्सटाइल पार्क: लखनऊ-हरदोई 1000 एकड़]
    D --> D3[मेडिकल डिवाइस पार्क: यीडा | बल्क ड्रग: ललितपुर]

    E --> E1[नमो भारत: देश की पहली RRTS दिल्ली-मेरठ 82 किमी]
    E --> E2[सर्वाधिक मेट्रो शहर: 5 - लखनऊ, कानपुर, आगरा, नोएडा, गाजियाबाद]
    E --> E3[NW-1 गंगा: मल्टीमॉडल टर्मिनल वाराणसी व MV गंगा विलास]

    F --> F1[बजट 2024-25: ₹7.36 लाख करोड़ ऐतिहासिक आकार]
    F --> F2[निवेश मित्र: 400+ ऑनलाइन अनापत्ति सेवाएं]
    F --> F3[7 पुलिस कमिश्नरेट: लखनऊ, नोएडा, वाराणसी, कानपुर आदि]

    G --> G1[अटल आवासीय विद्यालय: सभी 18 मंडलों में संचालित]
    G --> G2[ई-श्रम पोर्टल: 8.3+ करोड़ कामगार पंजीकरण में देश में प्रथम]
    G --> G3[अभ्युदय निःशुल्क कोचिंग व मिशन शक्ति 4.0]

    H --> H1[मेजर ध्यानचंद खेल विश्वविद्यालय: मेरठ]
    H --> H2[ODOS योजना: 75 जिले | खेलो इंडिया विवि खेल 2023]
    H --> H3[जीआई टैग: 75+ विशिष्ट उत्पादों के साथ देश में शीर्ष]
    </div>
  </div>
</div>

<!-- Card 2: Expressway Network & Infrastructure -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Infrastructure Revolution: Expressway Capital of India</span>
    <span class="lang-hi">1. अवसंरचना क्रांति: भारत का 'एक्सप्रेसवे प्रदेश'</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>National Leadership:</strong> Uttar Pradesh is known as the <em>Expressway State of India</em>, possessing the longest network of operational and under-construction expressways in the country (total network exceeding 3,200 km across 13 expressways).</span>
      <span class="lang-hi"><strong>राष्ट्रीय नेतृत्व:</strong> उत्तर प्रदेश को भारत का <em>'एक्सप्रेसवे प्रदेश'</em> कहा जाता है, जहाँ देश का सबसे बड़ा चालू एवं निर्माणाधीन एक्सप्रेसवे नेटवर्क (13 एक्सप्रेसवे के तहत 3,200 किमी से अधिक) स्थित है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Purvanchal Expressway (पूर्वांचल एक्सप्रेसवे):</strong>
        <br/>• <strong>Length &amp; Route:</strong> <strong>340.82 km</strong>; begins at Chand Sarai (Lucknow) and terminates at Haydaria (Ghazipur).
        <br/>• <strong>Districts Traversed (9 districts):</strong> Lucknow, Barabanki, Amethi, Sultanpur, Ayodhya, Ambedkar Nagar, Azamgarh, Mau, and Ghazipur.
        <br/>• <strong>Airstrip:</strong> Features a <strong>3.2 km emergency landing airstrip at Kurebhar (Sultanpur)</strong> for Indian Air Force fighter jets.
        <br/>• <strong>Inauguration:</strong> November 16, 2021, by PM Narendra Modi.
      </span>
      <span class="lang-hi"><strong>पूर्वांचल एक्सप्रेसवे:</strong>
        <br/>• <strong>लंबाई एवं मार्ग:</strong> <strong>340.82 किमी</strong>; चांद सराय (लखनऊ) से प्रारंभ होकर हैदरिया (गाजीपुर) पर समाप्त।
        <br/>• <strong>शामिल 9 जिले:</strong> लखनऊ, बाराबंकी, अमेठी, सुल्तानपुर, अयोध्या, अंबेडकर नगर, आजमगढ़, मऊ तथा गाजीपुर।
        <br/>• <strong>आपातकालीन हवाई पट्टी:</strong> वायुसेना के लड़ाकू विमानों की लैंडिंग हेतु <strong>कुरेभार (सुल्तानपुर) में 3.2 किमी लंबी एयरस्ट्रिप</strong>।
        <br/>• <strong>उद्घाटन:</strong> 16 नवंबर 2021 को प्रधानमंत्री नरेंद्र मोदी द्वारा।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Bundelkhand Expressway (बुंदेलखंड एक्सप्रेसवे):</strong>
        <br/>• <strong>Length &amp; Route:</strong> <strong>296.07 km</strong>; begins at Bharatkoop (Chitrakoot) and merges with the Agra-Lucknow Expressway at Kudrail (Etawah).
        <br/>• <strong>Districts Traversed (7 districts):</strong> Chitrakoot, Banda, Mahoba, Hamirpur, Jalaun, Auraiya, and Etawah.
        <br/>• <strong>Inauguration:</strong> July 16, 2022, by PM Narendra Modi; developed in record 28 months.
      </span>
      <span class="lang-hi"><strong>बुंदेलखंड एक्सप्रेसवे:</strong>
        <br/>• <strong>लंबाई एवं मार्ग:</strong> <strong>296.07 किमी</strong>; भरतकूप (चित्रकूट) से प्रारंभ होकर कुदरैल (इटावा) में आगरा-लखनऊ एक्सप्रेसवे से जुड़ता है।
        <br/>• <strong>शामिल 7 जिले:</strong> चित्रकूट, बांदा, महोबा, हमीरपुर, जालौन, औरैया तथा इटावा।
        <br/>• <strong>उद्घाटन:</strong> 16 जुलाई 2022 को प्रधानमंत्री नरेंद्र मोदी द्वारा; मात्र 28 माह के रिकॉर्ड समय में निर्मित।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Ganga Expressway (गंगा एक्सप्रेसवे) - Under Construction:</strong>
        <br/>• <strong>Length &amp; Route:</strong> <strong>594 km</strong> (6 lanes expandable to 8 lanes); from Bijauli village (Meerut) to Judapur Dandu village (Prayagraj).
        <br/>• <strong>National Distinction:</strong> India's longest access-controlled expressway upon completion; built at an estimated cost of ₹36,230 crore.
        <br/>• <strong>Districts Covered (12 districts):</strong> Meerut, Hapur, Bulandshahr, Amroha, Sambhal, Badaun, Shahjahanpur, Hardoi, Unnao, Rae Bareli, Pratapgarh, and Prayagraj.
        <br/>• <strong>Airstrip:</strong> Features a <strong>3.5 km emergency airstrip at Jalalabad (Shahjahanpur)</strong>.
      </span>
      <span class="lang-hi"><strong>गंगा एक्सप्रेसवे (निर्माणाधीन):</strong>
        <br/>• <strong>लंबाई एवं मार्ग:</strong> <strong>594 किमी</strong> (6 लेन, 8 लेन तक विस्तार योग्य); बिजौली गांव (मेरठ) से जुदापुर दांदू गांव (प्रयागराज) तक।
        <br/>• <strong>राष्ट्रीय महत्व:</strong> पूर्ण होने पर देश का सबसे लंबा एक्सप्रेसवे; अनुमानित लागत ₹36,230 करोड़।
        <br/>• <strong>शामिल 12 जिले:</strong> मेरठ, हापुड़, बुलंदशहर, अमरोहा, संभल, बदायूं, शाहजहांपुर, हरदोई, उन्नाव, रायबरेली, प्रतापगढ़ तथा प्रयागराज।
        <br/>• <strong>हवाई पट्टी:</strong> <strong>जलालाबाद (शाहजहांपुर) में 3.5 किमी लंबी आपातकालीन हवाई पट्टी</strong> का प्रावधान।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Gorakhpur Link Expressway:</strong> <strong>91.35 km</strong> 4-lane expressway connecting Jaitpur (Gorakhpur) to Salarpur (Azamgarh) on the Purvanchal Expressway, passing through Gorakhpur, Sant Kabir Nagar, Ambedkar Nagar, and Azamgarh.</span>
      <span class="lang-hi"><strong>गोरखपुर लिंक एक्सप्रेसवे:</strong> <strong>91.35 किमी</strong> लंबा 4-लेन एक्सप्रेसवे जो जैतपुर (गोरखपुर) को पूर्वांचल एक्सप्रेसवे पर सालारपुर (आजमगढ़) से जोड़ता है (गोरखपुर, संत कबीर नगर, अंबेडकर नगर व आजमगढ़ से होकर)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Agra-Lucknow Expressway:</strong> <strong>302.22 km</strong> 6-lane greenfield expressway with a 3.3 km emergency airstrip in Unnao district.</span>
      <span class="lang-hi"><strong>आगरा-लखनऊ एक्सप्रेसवे:</strong> <strong>302.22 किमी</strong> लंबा 6-लेन एक्सप्रेसवे; उन्नाव जिले में 3.3 किमी लंबी हवाई पट्टी से सुसज्जित।</span>
    </li>
  </ul>
</div>

<!-- Card 3: Civil Aviation & Multi-Modal Transit -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Aviation Leadership &amp; Modern Urban Rapid Transit</span>
    <span class="lang-hi">2. नागरिक उड्डयन में शीर्ष स्थान एवं आधुनिक रैपिड ट्रांजिट</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>5 International Airports Milestone:</strong> UP is the first state in India developing <strong>5 International Airports</strong>:
        <br/>1. <strong>Chaudhary Charan Singh International Airport</strong> (Amausi, Lucknow)
        <br/>2. <strong>Lal Bahadur Shastri International Airport</strong> (Babatpur, Varanasi)
        <br/>3. <strong>Kushinagar International Airport</strong> (Inaugurated October 2021)
        <br/>4. <strong>Maharishi Valmiki International Airport Ayodhya Dham</strong> (Inaugurated December 30, 2023)
        <br/>5. <strong>Noida International Airport (Jewar, Gautam Buddha Nagar):</strong> Developed by Zurich Airport International AG; slated to be Asia's largest greenfield airport with up to 5 runways upon full expansion.
      </span>
      <span class="lang-hi"><strong>5 अंतरराष्ट्रीय हवाई अड्डों का रिकॉर्ड:</strong> उत्तर प्रदेश <strong>5 अंतरराष्ट्रीय हवाई अड्डे</strong> विकसित करने वाला देश का पहला राज्य है:
        <br/>1. <strong>चौधरी चरण सिंह अंतरराष्ट्रीय हवाई अड्डा</strong> (अमौसी, लखनऊ)
        <br/>2. <strong>लाल बहादुर शास्त्री अंतरराष्ट्रीय हवाई अड्डा</strong> (बाबतपुर, वाराणसी)
        <br/>3. <strong>कुशीनगर अंतरराष्ट्रीय हवाई अड्डा</strong> (अक्टूबर 2021 में उद्घाटित)
        <br/>4. <strong>महर्षि वाल्मीकि अंतरराष्ट्रीय हवाई अड्डा अयोध्या धाम</strong> (30 दिसंबर 2023 को उद्घाटित)
        <br/>5. <strong>नोएडा अंतरराष्ट्रीय हवाई अड्डा (जेवर, गौतमबुद्ध नगर):</strong> ज्यूरिख एयरपोर्ट इंटरनेशनल द्वारा विकसित; पूर्ण विस्तार पर 5 रनवे के साथ एशिया का सबसे बड़ा एयरपोर्ट।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Namo Bharat - India's 1st RRTS (Regional Rapid Transit System):</strong>
        <br/>• <strong>Route &amp; Length:</strong> 82.15 km Delhi-Ghaziabad-Meerut corridor; design speed of 180 km/h and operational speed of 160 km/h.
        <br/>• <strong>Priority Section:</strong> 17 km section between Sahibabad and Duhai Depot inaugurated on October 20, 2023, by PM Modi.
      </span>
      <span class="lang-hi"><strong>नमो भारत - देश की पहली RRTS (रीजनल रैपिड ट्रांजिट सिस्टम):</strong>
        <br/>• <strong>मार्ग एवं लंबाई:</strong> 82.15 किमी दिल्ली-गाजियाबाद-मेरठ कॉरिडोर; 180 किमी/घंटा डिजाइन गति व 160 किमी/घंटा परिचालन गति।
        <br/>• <strong>प्राथमिक खंड:</strong> साहिबाबाद से दुहाई डिपो के बीच 17 किमी खंड का उद्घाटन 20 अक्टूबर 2023 को प्रधानमंत्री द्वारा।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Metro Rail Network Leader:</strong> UP has the highest number of cities with operational Metro Rail in India (<strong>5 cities: Lucknow, Kanpur, Agra, Noida, Ghaziabad</strong>). Agra Metro priority corridor (Taj East Gate to Mankameshwar) was inaugurated in March 2024.</span>
      <span class="lang-hi"><strong>मेट्रो रेल नेटवर्क में अग्रणी:</strong> उत्तर प्रदेश में देश में सर्वाधिक शहरों में मेट्रो रेल संचालित है (<strong>5 शहर: लखनऊ, कानपुर, आगरा, नोएडा, गाजियाबाद</strong>)। मार्च 2024 में आगरा मेट्रो के प्राथमिकता खंड का उद्घाटन किया गया।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Inland Waterway &amp; World's Longest River Cruise:</strong>
        <br/>• <strong>National Waterway 1 (NW-1):</strong> 1,620 km along Ganga from Prayagraj to Haldia; Multimodal Terminal established at Ramnagar (Varanasi).
        <br/>• <strong>MV Ganga Vilas:</strong> World's longest river cruise flagged off from Varanasi on January 13, 2023, traveling 3,200 km across 27 river systems to Dibrugarh (Assam) in 51 days.
      </span>
      <span class="lang-hi"><strong>अंतर्देशीय जलमार्ग एवं विश्व का सबसे लंबा रिवर क्रूज:</strong>
        <br/>• <strong>राष्ट्रीय जलमार्ग-1 (NW-1):</strong> प्रयागराज से हल्दिया तक गंगा नदी पर 1,620 किमी; रामनगर (वाराणसी) में मल्टीमॉडल टर्मिनल स्थापित।
        <br/>• <strong>एमवी गंगा विलास:</strong> विश्व का सबसे लंबा रिवर क्रूज, जिसे 13 जनवरी 2023 को वाराणसी से डिब्रूगढ़ (असम) हेतु रवाना किया गया (51 दिनों में 3,200 किमी यात्रा)।
      </span>
    </li>
  </ul>
</div>

<!-- Card 4: Mega Industrial Projects, Defense Corridor & Investment -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Mega Industrial Corridors &amp; Investment Milestones</span>
    <span class="lang-hi">3. मेगा औद्योगिक गलियारे एवं ऐतिहासिक निवेश उपलब्धियां</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>UP Defense Industrial Corridor:</strong>
        <br/>• Comprises <strong>6 Strategic Nodes:</strong> Agra, Aligarh, Chitrakoot, Jhansi, Kanpur, and Lucknow.
        <br/>• <strong>Key Anchors:</strong> BrahMos Aerospace Next-Gen missile manufacturing unit in Lucknow (Bhatgaon, 200 acres); Bharat Dynamics Limited (BDL) propulsion plant in Jhansi.
      </span>
      <span class="lang-hi"><strong>उ.प्र. रक्षा औद्योगिक गलियारा (Defense Corridor):</strong>
        <br/>• <strong>6 रणनीतिक नोड:</strong> आगरा, अलीगढ़, चित्रकूट, झांसी, कानपुर तथा लखनऊ।
        <br/>• <strong>प्रमुख परियोजनाएं:</strong> लखनऊ (भाटगांव) में 200 एकड़ में ब्रह्मोस एयरोस्पेस अगली पीढ़ी मिसाइल विनिर्माण इकाई; झांसी में भारत डायनेमिक्स लिमिटेड (BDL)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>PM-MITRA Mega Integrated Textile Region and Apparel Park:</strong> Approved under Central PM-MITRA scheme; spreading over <strong>1,000 acres at Attari village on the Lucknow-Hardoi border</strong> with an outlay of ₹1,200 crore.</span>
      <span class="lang-hi"><strong>PM-मित्र मेगा टेक्सटाइल पार्क:</strong> केंद्र सरकार की पीएम-मित्र योजना के तहत <strong>लखनऊ-हरदोई सीमा पर अटारी गांव में 1,000 एकड़</strong> में ₹1,200 करोड़ की लागत से स्थापित किया जा रहा है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Medical Device Park &amp; Bulk Drug Park:</strong> North India's first dedicated Medical Device Park spanning 350 acres at Sector 28, YEIDA (Greater Noida); Bulk Drug Park approved in <strong>Lalitpur</strong> (Bundelkhand).</span>
      <span class="lang-hi"><strong>मेडिकल डिवाइस पार्क व बल्क ड्रग पार्क:</strong> उत्तर भारत का पहला मेडिकल डिवाइस पार्क यीडा (ग्रेटर नोएडा) के सेक्टर-28 में 350 एकड़ में; राज्य का बल्क ड्रग पार्क <strong>ललितपुर</strong> (बुंदेलखंड) में स्वीकृत।</span>
    </li>
    <li>
      <span class="lang-en"><strong>UP Global Investors Summit (UP-GIS) 2023:</strong> Held in Lucknow (February 10-12, 2023); secured investment proposals worth over <strong>₹33.50 lakh crore</strong> (revised to ₹40 lakh crore), paving the path to achieve a <strong>$1 Trillion Economy by 2027-28</strong>.</span>
      <span class="lang-hi"><strong>उ.प्र. ग्लोबल इन्वेस्टर्स समिट (UP-GIS) 2023:</strong> 10-12 फरवरी 2023 को लखनऊ में आयोजित; <strong>₹33.50 लाख करोड़</strong> (संशोधित ₹40 लाख करोड़) से अधिक के समझौता ज्ञापनों पर हस्ताक्षर; <strong>2027-28 तक $1 ट्रिलियन अर्थव्यवस्था</strong> का लक्ष्य।</span>
    </li>
  </ul>
</div>

<!-- Card 5: Governance, Law & Order and Ease of Doing Business -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Governance Reforms, Law &amp; Order and Digital Portals</span>
    <span class="lang-hi">4. शासन सुधार, कानून व्यवस्था एवं डिजिटल पोर्टल</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Police Commissionerate System (पुलिस कमिश्नरेट प्रणाली):</strong> Currently operational across <strong>7 major cities</strong> in UP:
        <br/>1. Lucknow (January 2020)
        <br/>2. Gautam Buddha Nagar / Noida (January 2020)
        <br/>3. Kanpur Nagar (March 2021)
        <br/>4. Varanasi (March 2021)
        <br/>5. Agra (November 2022)
        <br/>6. Ghaziabad (November 2022)
        <br/>7. Prayagraj (November 2022)
      </span>
      <span class="lang-hi"><strong>पुलिस कमिश्नरेट प्रणाली:</strong> वर्तमान में उ.प्र. के <strong>7 प्रमुख महानगरों</strong> में लागू:
        <br/>1. लखनऊ (जनवरी 2020)
        <br/>2. गौतमबुद्ध नगर / नोएडा (जनवरी 2020)
        <br/>3. कानपुर नगर (मार्च 2021)
        <br/>4. वाराणसी (मार्च 2021)
        <br/>5. आगरा (नवंबर 2022)
        <br/>6. गाजियाबाद (नवंबर 2022)
        <br/>7. प्रयागराज (नवंबर 2022)
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Ease of Doing Business (EoDB):</strong> UP achieved <strong>2nd Rank nationally</strong> under the Business Reform Action Plan (BRAP) by DPIIT, jumping from 14th rank in 2017.</span>
      <span class="lang-hi"><strong>ईज ऑफ डूइंग बिजनेस (EoDB):</strong> DPIIT की बिजनेस रिफॉर्म एक्शन प्लान रैंकिंग में उ.प्र. ने 2017 के 14वें स्थान से लंबी छलांग लगाकर <strong>राष्ट्रीय स्तर पर दूसरा स्थान</strong> हासिल किया।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Flagship Portals:</strong>
        <br/>• <strong>Nivesh Mitra:</strong> Single Window Clearance Portal providing over 400 online services across 30+ government departments.
        <br/>• <strong>Nivesh Sarathi:</strong> Dedicated portal for end-to-end tracking of MoUs signed during Global Investors Summits.
        <br/>• <strong>e-Prosecution Portal:</strong> UP ranks <strong>1st in India</strong> for highest case disposal and digital hearings on the Inter-operable Criminal Justice System (ICJS).
      </span>
      <span class="lang-hi"><strong>प्रमुख शासन पोर्टल:</strong>
        <br/>• <strong>निवेश मित्र:</strong> सिंगल विंडो पोर्टल जो 30 से अधिक विभागों की 400 से अधिक ऑनलाइन स्वीकृतियां प्रदान करता है।
        <br/>• <strong>निवेश सारथी:</strong> इन्वेस्टर्स समिट में हस्ताक्षरित एमओयू के क्रियान्वयन की निगरानी हेतु पोर्टल।
        <br/>• <strong>ई-प्रॉसिक्यूशन पोर्टल:</strong> ICJS प्लेटफॉर्म पर मामलों के ऑनलाइन निस्तारण में उत्तर प्रदेश <strong>देश में प्रथम स्थान</strong> पर।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>State Budget 2024-25:</strong> Total size of <strong>₹7,36,437 crore</strong> (largest ever in UP's history), with capital outlay of over ₹2.03 lakh crore and fiscal deficit maintained within FRBM limits at 3.46% of GSDP.</span>
      <span class="lang-hi"><strong>राज्य बजट 2024-25:</strong> कुल आकार <strong>₹7,36,437 करोड़</strong> (उ.प्र. के इतिहास का सबसे बड़ा बजट); पूंजीगत व्यय ₹2.03 लाख करोड़ तथा राजकोषीय घाटा GSDP का 3.46% (FRBM सीमा के भीतर)।</span>
    </li>
  </ul>
</div>

<!-- Card 6: Social Welfare, Healthcare & Education Milestones -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Social Welfare, Healthcare &amp; Education Milestones</span>
    <span class="lang-hi">5. सामाजिक कल्याण, स्वास्थ्य सेवा एवं शिक्षा में ऐतिहासिक उपलब्धियां</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Atal Residential Schools (अटल आवासीय विद्यालय):</strong> <strong>18 state-of-the-art CBSE residential schools</strong> established across all 18 Divisional Headquarters of UP, offering free high-quality education and boarding to children of registered construction workers (BOCW Board) and Covid orphans.</span>
      <span class="lang-hi"><strong>अटल आवासीय विद्यालय:</strong> पंजीकृत निर्माण श्रमिकों (BOCW बोर्ड) के बच्चों एवं कोविड अनाथ बच्चों को निःशुल्क गुणवत्तापूर्ण आवासीय शिक्षा प्रदान करने हेतु सभी <strong>18 मंडलों में 18 अटल विद्यालय</strong> स्थापित।</span>
    </li>
    <li>
      <span class="lang-en"><strong>'One District One Medical College' Mission:</strong> Expanded government medical colleges from just 12 in 2017 to over <strong>65 operational colleges</strong>, striving to establish a medical college in every single district.</span>
      <span class="lang-hi"><strong>'एक जिला एक मेडिकल कॉलेज' मिशन:</strong> वर्ष 2017 में मात्र 12 राजकीय मेडिकल कॉलेजों से बढ़ाकर वर्तमान में <strong>65 से अधिक मेडिकल कॉलेज</strong> संचालित; सभी 75 जिलों में मेडिकल कॉलेज स्थापित करने का लक्ष्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Mukhyamantri Abhyudaya Yojana:</strong> Launched on Basant Panchami 2021, providing free high-level coaching, tablets, and mentorship for competitive exams (UPSC, UPPSC, JEE, NEET, NDA, CDS).</span>
      <span class="lang-hi"><strong>मुख्यमंत्री अभ्युदय योजना:</strong> बसंत पंचमी 2021 से प्रारंभ; प्रतियोगी परीक्षाओं (UPSC, UPPSC, JEE, NEET आदि) हेतु निःशुल्क कोचिंग, मार्गदर्शन एवं टैबलेट वितरण।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Mission Shakti 4.0:</strong> Flagship women-safety and self-reliance campaign; established <strong>Pink Booths, Women Help Desks in all 1,535+ police stations</strong>, and expanded 1090 Women Power Line.</span>
      <span class="lang-hi"><strong>मिशन शक्ति 4.0:</strong> महिला सुरक्षा, सम्मान एवं स्वावलंबन हेतु महा-अभियान; सभी 1,535+ थानों में <strong>पिंक बूथ व महिला हेल्प डेस्क</strong> स्थापित तथा 1090 विमेन पावर लाइन का विस्तार।</span>
    </li>
    <li>
      <span class="lang-en"><strong>National Welfare Leadership:</strong>
        <br/>• <strong>e-Shram Registrations:</strong> Rank 1 in India with over <strong>8.3 crore unorganized workers</strong> registered.
        <br/>• <strong>PM-SVANidhi:</strong> Rank 1 in disbursing micro-loans to urban street vendors.
        <br/>• <strong>PMAY (Pradhan Mantri Awas Yojana):</strong> Rank 1 in rural and urban housing construction.
      </span>
      <span class="lang-hi"><strong>राष्ट्रीय जनकल्याण योजनाओं में शीर्ष स्थान:</strong>
        <br/>• <strong>ई-श्रम पंजीकरण:</strong> <strong>8.3 करोड़ से अधिक असंगठित कामगारों</strong> के पंजीकरण के साथ देश में प्रथम।
        <br/>• <strong>पीएम-स्वनिधि:</strong> स्ट्रीट वेंडरों को ऋण वितरण में देश में प्रथम स्थान।
        <br/>• <strong>पीएम आवास योजना:</strong> ग्रामीण एवं शहरी दोनों घटकों के आवास निर्माण में देश में प्रथम स्थान।
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: Sports, GI Tags & Cultural Tourism Records -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Sports Achievements, GI Tags Leadership &amp; Tourism Boom</span>
    <span class="lang-hi">6. खेल उपलब्धियां, जीआई टैग में कीर्तिमान एवं पर्यटन उछाल</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Major Dhyan Chand Sports University:</strong> State's first dedicated sports university established at <strong>Salawa, Sardhana (Meerut)</strong> at an outlay of ₹700 crore.</span>
      <span class="lang-hi"><strong>मेजर ध्यानचंद खेल विश्वविद्यालय:</strong> राज्य का पहला खेल विश्वविद्यालय <strong>सलावा, सरधना (मेरठ)</strong> में ₹700 करोड़ की लागत से स्थापित।</span>
    </li>
    <li>
      <span class="lang-en"><strong>One District One Sport (ODOS) Scheme:</strong> Launched across all 75 districts to identify, train, and promote one specific Olympic/indigenous sport per district (modeled on the success of ODOP).</span>
      <span class="lang-hi"><strong>एक जिला एक खेल (ODOS) योजना:</strong> ओडीओपी की तर्ज पर सभी 75 जिलों में प्रत्येक जिले के लिए एक विशिष्ट खेल को चिन्हित कर खिलाड़ियों को प्रशिक्षित करने हेतु प्रारंभ।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Major Sporting Events Hosted:</strong>
        <br/>• <strong>3rd Khelo India University Games (2023):</strong> Held across 4 cities: Lucknow, Varanasi, Gorakhpur, and Noida; mascot was <em>'Jeetu'</em> (Barasingha - state animal).
        <br/>• <strong>MotoGP Bharat 2023:</strong> India's first premier motorcycle Grand Prix hosted at the <strong>Buddh International Circuit (Greater Noida)</strong> in September 2023.
      </span>
      <span class="lang-hi"><strong>आयोजित प्रमुख खेल आयोजन:</strong>
        <br/>• <strong>तीसरे खेलो इंडिया यूनिवर्सिटी गेम्स (2023):</strong> 4 शहरों (लखनऊ, वाराणसी, गोरखपुर, नोएडा) में आयोजित; शुभंकर <em>'जीतू'</em> (राज्य पशु बारहसिंगा)।
        <br/>• <strong>मोटोजीपी भारत 2023:</strong> भारत की पहली फॉर्मूला बाइक रेस का आयोजन सितंबर 2023 में <strong>बुद्ध इंटरनेशनल सर्किट (ग्रेटर नोएडा)</strong> में किया गया।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>GI Tag Leadership:</strong> UP ranks <strong>1st/2nd in India with over 75 certified GI Products</strong>. Varanasi leads globally as a single region with over 23 GI products (e.g., Banaras Paan, Banaras Langra Mango, Ramnagar Bhanta, Adamchini Rice, Wood Carvings).</span>
      <span class="lang-hi"><strong>जीआई टैग में राष्ट्रीय कीर्तिमान:</strong> उत्तर प्रदेश <strong>75 से अधिक जीआई उत्पादों के साथ देश में शीर्ष स्थान</strong> पर। अकेले वाराणसी क्षेत्र के 23 से अधिक उत्पाद (बनारसी पान, लंगड़ा आम, रामनगर भंटा, आदमचीनी चावल आदि) जीआई टैग प्राप्त कर चुके हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Tourism Superpower:</strong> UP ranks <strong>1st in domestic tourist visits in India</strong>, recording over 48 crore tourists in 2023-24, propelled by the Shri Ram Mandir inauguration in Ayodhya (January 22, 2024), Kashi Vishwanath Dham corridor, and Braj Teerth Vikas Parishad projects.</span>
      <span class="lang-hi"><strong>पर्यटन में देश में प्रथम:</strong> उत्तर प्रदेश <strong>घरेलू पर्यटकों के आगमन में देश में प्रथम स्थान</strong> पर रहा (वर्ष 2023-24 में 48 करोड़ से अधिक पर्यटक), जिसमें अयोध्या धाम श्री राम मंदिर प्राण-प्रतिष्ठा (22 जनवरी 2024), काशी विश्वनाथ धाम व ब्रज तीर्थ विकास परिषद की प्रमुख भूमिका रही।</span>
    </li>
  </ul>
</div>

<!-- Card 8: High-Yield One-Liner Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Rapid Revision Fact Matrix: Current Affairs &amp; Milestones (Direct Exam Points)</span>
    <span class="lang-hi">7. रैपिड रिवीजन तथ्य मैट्रिक्स: समसामयिक घटनाएं एवं उपलब्धियां (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Milestone</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / उपलब्धि</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">What is the total length of the Purvanchal Expressway?</span><span class="lang-hi">पूर्वांचल एक्सप्रेसवे की कुल लंबाई कितनी है?</span></td>
          <td><span class="lang-en"><strong>340.82 km</strong> (from Chand Sarai, Lucknow to Haydaria, Ghazipur)</span><span class="lang-hi"><strong>340.82 किमी</strong> (चांद सराय, लखनऊ से हैदरिया, गाजीपुर तक)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the emergency airstrip located on Purvanchal Expressway?</span><span class="lang-hi">पूर्वांचल एक्सप्रेसवे पर आपातकालीन हवाई पट्टी कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Kurebhar, Sultanpur (3.2 km)</strong></span><span class="lang-hi"><strong>कुरेभार, सुल्तानपुर (3.2 किमी)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the total length of the Bundelkhand Expressway?</span><span class="lang-hi">बुंदेलखंड एक्सप्रेसवे की कुल लंबाई कितनी है?</span></td>
          <td><span class="lang-en"><strong>296.07 km</strong> (from Bharatkoop, Chitrakoot to Kudrail, Etawah)</span><span class="lang-hi"><strong>296.07 किमी</strong> (भरतकूप, चित्रकूट से कुदरैल, इटावा तक)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the total length of the under-construction Ganga Expressway?</span><span class="lang-hi">निर्माणाधीन गंगा एक्सप्रेसवे की कुल लंबाई कितनी है?</span></td>
          <td><span class="lang-en"><strong>594 km</strong> (from Bijauli, Meerut to Judapur Dandu, Prayagraj; 12 districts)</span><span class="lang-hi"><strong>594 किमी</strong> (बिजौली, मेरठ से जुदापुर दांदू, प्रयागराज तक; 12 जिले)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">How many International Airports will Uttar Pradesh possess?</span><span class="lang-hi">उत्तर प्रदेश में कुल कितने अंतरराष्ट्रीय हवाई अड्डे होंगे?</span></td>
          <td><span class="lang-en"><strong>5 International Airports</strong> (Lucknow, Varanasi, Kushinagar, Ayodhya, Jewar)</span><span class="lang-hi"><strong>5 अंतरराष्ट्रीय हवाई अड्डे</strong> (लखनऊ, वाराणसी, कुशीनगर, अयोध्या, जेवर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Major Dhyan Chand Sports University being built?</span><span class="lang-hi">मेजर ध्यानचंद खेल विश्वविद्यालय कहाँ स्थापित किया जा रहा है?</span></td>
          <td><span class="lang-en"><strong>Salawa, Sardhana (Meerut district)</strong></span><span class="lang-hi"><strong>सलावा, सरधना (मेरठ जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the PM-MITRA Mega Textile Park located in UP?</span><span class="lang-hi">उ.प्र. में PM-मित्र मेगा टेक्सटाइल पार्क कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Attari village, Lucknow-Hardoi border (1,000 acres)</strong></span><span class="lang-hi"><strong>अटारी गांव, लखनऊ-हरदोई सीमा (1,000 एकड़)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the BrahMos missile manufacturing facility located in UP?</span><span class="lang-hi">उ.प्र. में ब्रह्मोस मिसाइल विनिर्माण केंद्र कहाँ स्थापित है?</span></td>
          <td><span class="lang-en"><strong>Lucknow (Bhatgaon node, Defense Corridor)</strong></span><span class="lang-hi"><strong>लखनऊ (भाटगांव नोड, रक्षा गलियारा)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In how many cities is the Police Commissionerate system operational?</span><span class="lang-hi">उ.प्र. के कितने शहरों में पुलिस कमिश्नरेट प्रणाली लागू है?</span></td>
          <td><span class="lang-en"><strong>7 Cities</strong> (Lucknow, Noida, Kanpur, Varanasi, Agra, Ghaziabad, Prayagraj)</span><span class="lang-hi"><strong>7 शहर</strong> (लखनऊ, नोएडा, कानपुर, वाराणसी, आगरा, गाजियाबाद, प्रयागराज)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is India's first RRTS train named?</span><span class="lang-hi">भारत की पहली RRTS ट्रेन का नाम क्या रखा गया है?</span></td>
          <td><span class="lang-en"><strong>Namo Bharat (नमो भारत)</strong> (Delhi-Ghaziabad-Meerut corridor)</span><span class="lang-hi"><strong>नमो भारत</strong> (दिल्ली-गाजियाबाद-मेरठ कॉरिडोर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">How many Atal Residential Schools are operational in UP?</span><span class="lang-hi">उ.प्र. में कुल कितने अटल आवासीय विद्यालय संचालित हैं?</span></td>
          <td><span class="lang-en"><strong>18 Schools</strong> (in all 18 Divisional Headquarters)</span><span class="lang-hi"><strong>18 विद्यालय</strong> (सभी 18 मंडल मुख्यालयों में)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What was the mascot for the 3rd Khelo India University Games 2023?</span><span class="lang-hi">तीसरे खेलो इंडिया यूनिवर्सिटी गेम्स 2023 का शुभंकर क्या था?</span></td>
          <td><span class="lang-en"><strong>Jeetu (जीतू)</strong> (representing the Swamp Deer / Barasingha)</span><span class="lang-hi"><strong>जीतू</strong> (राज्य पशु बारहसिंगा का प्रतिनिधित्व)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is UP's rank in e-Shram portal worker registrations?</span><span class="lang-hi">ई-श्रम पोर्टल पर श्रमिक पंजीकरण में उ.प्र. का राष्ट्रीय स्थान क्या है?</span></td>
          <td><span class="lang-en"><strong>1st Rank</strong> (over 8.3 crore unorganized workers registered)</span><span class="lang-hi"><strong>प्रथम स्थान</strong> (8.3 करोड़ से अधिक असंगठित कामगार पंजीकृत)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where was MotoGP Bharat 2023 held?</span><span class="lang-hi">मोटोजीपी भारत 2023 का आयोजन कहाँ किया गया था?</span></td>
          <td><span class="lang-en"><strong>Buddh International Circuit, Greater Noida</strong></span><span class="lang-hi"><strong>बुद्ध इंटरनेशनल सर्किट, ग्रेटर नोएडा</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the target year for UP to achieve a $1 Trillion economy?</span><span class="lang-hi">उ.प्र. को $1 ट्रिलियन अर्थव्यवस्था बनाने का लक्ष्य वर्ष क्या है?</span></td>
          <td><span class="lang-en"><strong>Year 2027-28</strong></span><span class="lang-hi"><strong>वर्ष 2027-28</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "current-events-and-achievements-of-uttar-pradesh-state-in-various-fields-etc", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_current_events_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
