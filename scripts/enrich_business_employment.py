import os
import re

def build_business_employment_theory_html():
    return """
<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Business, Industry &amp; Employment Ecosystem of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का व्यवसाय, उद्योग एवं रोजगार परिदृश्य</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Business & Employment in UP] --> B[Macro Economy & Workforce]
    A --> C[MSME Capital: Rank 1]
    A --> D[ODOP Scheme: 75 Districts]
    A --> E[Self-Employment & Skill Missions]
    A --> F[Ease of Doing Business & Portals]
    A --> G[Defense Corridor & Industrial Nodes]
    A --> H[Labor Welfare & Atal Schools]

    B --> B1[$1 Trillion Economy Goal by 2027]
    B --> B2[GSDP: 2nd Largest in India ~9.2%]
    B --> B3[Workforce: 59.3% Agri, 32.9% WPR]

    C --> C1[90+ Lakh Units: 14% of India]
    C --> C2[60% Industrial Jobs & 70% Exports]
    C --> C3[MSME Policy 2022 Subsidies]

    D --> D1[Launched 24 Jan 2018 UP Diwas]
    D --> D2[75 Districts Specific Products]
    D --> D3[Financial, Skill & Tool-kit Support]

    E --> E1[Mukhyamantri Yuva Swarojgar: Up to 25 Lakh]
    E --> E2[Vishwakarma Shram Samman: 2019 Artisans]
    E --> E3[UPSDM: 1st Skill Mission in India 2013]
    E --> E4[Rozgar Sangam: Job Fairs & Apprenticeship]

    F --> F1[Nivesh Mitra: 400+ Single Window Clearances]
    F --> F2[Nivesh Sarathi: MoU & Investor Tracking]
    F --> F3[UP-GIS 2023: 33+ Lakh Crore MoUs]

    G --> G1[Defense Corridor: 6 Nodes - Agra, Aligarh, Chitrakoot, Jhansi, Kanpur, Lucknow]
    G --> G2[BrahMos Lucknow, PM-MITRA Textile Park Lucknow-Hardoi]

    H --> H1[Atal Residential Schools: 18 Divisions]
    H --> H2[Rank 1 e-Shram Portal Registrations]
    H --> H3[BOCW Board & Kanya Vivah Yojana]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उ.प्र. में व्यवसाय एवं रोजगार] --> B[अर्थव्यवस्था एवं कार्यबल]
    A --> C[MSME राजधानी: देश में प्रथम]
    A --> D[ODOP योजना: 75 जिले]
    A --> E[स्वरोजगार एवं कौशल विकास]
    A --> F[ईज ऑफ डूइंग बिजनेस एवं पोर्टल]
    A --> G[रक्षा गलियारा एवं औद्योगिक नोड]
    A --> H[श्रम कल्याण एवं अटल आवासीय विद्यालय]

    B --> B1[$1 ट्रिलियन अर्थव्यवस्था लक्ष्य 2027]
    B --> B2[GSDP: देश में दूसरी सबसे बड़ी ~9.2%]
    B --> B3[कार्यबल: 59.3% कृषि, 32.9% WPR]

    C --> C1[90+ लाख इकाइयाँ: देश का 14%]
    C --> C2[60% औद्योगिक रोजगार व 70% निर्यात]
    C --> C3[MSME नीति 2022 पूंजीगत अनुदान]

    D --> D1[24 जनवरी 2018 उ.प्र. दिवस पर शुभारंभ]
    D --> D2[75 जिलों के विशिष्ट उत्पाद]
    D --> D3[मार्जिन मनी, कौशल व टूल-किट सहायता]

    E --> E1[मुख्यमंत्री युवा स्वरोजगार: 25 लाख तक]
    E --> E2[विश्वकर्मा श्रम सम्मान: 2019 शिल्पकार]
    E --> E3[UPSDM: देश का पहला कौशल मिशन 2013]
    E --> E4[रोजगार संगम: रोजगार मेले व अप्रेंटिसशिप]

    F --> F1[निवेश मित्र: 400+ ऑनलाइन एकल खिड़की सेवाएं]
    F --> F2[निवेश सारथी: MoU व निवेशक ट्रैकिंग]
    F --> F3[UP-GIS 2023: 33+ लाख करोड़ के प्रस्ताव]

    G --> G1[डिफेंस कॉरिडोर: 6 नोड - आगरा, अलीगढ़, चित्रकूट, झांसी, कानपुर, लखनऊ]
    G --> G2[ब्रह्मोस लखनऊ, PM-मित्र टेक्सटाइल पार्क लखनऊ-हरदोई]

    H --> H1[अटल आवासीय विद्यालय: सभी 18 मंडल]
    H --> H2[ई-श्रम पोर्टल पंजीकरण में देश में प्रथम]
    H --> H3[BOCW बोर्ड व कन्या विवाह सहायता]
    </div>
  </div>
</div>

<!-- Card 2: Macroeconomic Indicators & Workforce Profile -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Macroeconomic Profile &amp; Workforce Demographics of UP</span>
    <span class="lang-hi">1. उत्तर प्रदेश का व्यापक आर्थिक परिदृश्य एवं कार्यबल सांख्यिकी</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Economic Indicator / Metric</span><span class="lang-hi">आर्थिक संकेतक / सांख्यिकी</span></th>
        <th><span class="lang-en">Current Value / Status</span><span class="lang-hi">वर्तमान मान / स्थिति</span></th>
        <th><span class="lang-en">Exam Significance &amp; Target</span><span class="lang-hi">परीक्षा महत्व एवं लक्ष्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Target Economy Size (अर्थव्यवस्था का लक्ष्य)</span><span class="lang-hi">अर्थव्यवस्था का आकार लक्ष्य</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">$1 Trillion Economy</strong></span><span class="lang-hi"><strong class="theory-highlight">$1 ट्रिलियन डॉलर अर्थव्यवस्था</strong></span></td>
        <td><span class="lang-en">Target deadline set by State Government for achievement by <strong>2027-28</strong>.</span><span class="lang-hi">राज्य सरकार द्वारा <strong>2027-28</strong> तक $1 ट्रिलियन अर्थव्यवस्था बनने का महत्वाकांक्षी लक्ष्य।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">National GSDP Contribution</span><span class="lang-hi">राष्ट्रीय जीडीपी में योगदान</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">2nd Largest Economy</strong></span><span class="lang-hi"><strong class="theory-highlight">दूसरी सबसे बड़ी अर्थव्यवस्था</strong></span></td>
        <td><span class="lang-en">Contributes approx. 9.2% to India's Gross Domestic Product (GDP), trailing only Maharashtra.</span><span class="lang-hi">महाराष्ट्र के बाद भारत के सकल घरेलू उत्पाद में लगभग 9.2% योगदान के साथ दूसरे स्थान पर।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Sectoral GSDP Composition</span><span class="lang-hi">सकल राज्य मूल्य संवर्धन (GSVA) हिस्सा</span></td>
        <td><span class="lang-en">Primary: ~23.5% | Secondary: ~26.8% | Tertiary: ~49.7%</span><span class="lang-hi">प्राथमिक: ~23.5% | द्वितीयक: ~26.8% | तृतीयक (सेवा): ~49.7%</span></td>
        <td><span class="lang-en">Service sector dominates GSDP, while agriculture absorbs majority of the labor force.</span><span class="lang-hi">सेवा क्षेत्र राज्य जीडीपी में सबसे बड़ा योगदानकर्ता है, जबकि कृषि सर्वाधिक कार्यबल को समाहित करती है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Workforce in Agriculture (Census 2011)</span><span class="lang-hi">कृषि पर निर्भर कार्यबल</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">59.3% of total workers</strong></span><span class="lang-hi"><strong class="theory-highlight">कुल श्रमिकों का 59.3%</strong></span></td>
        <td><span class="lang-en">Comprises Cultivators (29.0%) and Agricultural Laborers (30.3%).</span><span class="lang-hi">कृषक (काश्तकार - 29.0%) तथा खेतिहर मजदूर (30.3%) का सम्मिलित योग।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Household Industry Workers</span><span class="lang-hi">पारिवारिक उद्योग श्रमिक</span></td>
        <td><span class="lang-en">5.9%</span><span class="lang-hi">5.9%</span></td>
        <td><span class="lang-en">Includes traditional weaving, pottery, blacksmithy, and handicrafts.</span><span class="lang-hi">पारंपरिक बुनाई, कुम्हारी, लोहारी एवं कुटीर हस्तशिल्प कार्य।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Other Workers (Non-Agri/Services)</span><span class="lang-hi">अन्य श्रमिक (सेवा एवं व्यापार)</span></td>
        <td><span class="lang-en">34.8%</span><span class="lang-hi">34.8%</span></td>
        <td><span class="lang-en">Manufacturing, construction, IT, logistics, trade, and commercial services.</span><span class="lang-hi">विनिर्माण, निर्माण कार्य, आईटी, परिवहन, व्यापार एवं वाणिज्यिक सेवाएँ।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Work Participation Rate (WPR)</span><span class="lang-hi">श्रमिक सहभागिता दर (WPR)</span></td>
        <td><span class="lang-en">Overall: 32.9% (Male: 49.8%, Female: 15.2%)</span><span class="lang-hi">कुल: 32.9% (पुरुष: 49.8%, महिला: 15.2%)</span></td>
        <td><span class="lang-en">According to Census 2011; female work participation is highest in Bundelkhand tribal areas.</span><span class="lang-hi">2011 की जनगणना अनुसार; महिला श्रमिक सहभागिता बुंदेलखंड व आदिवासी क्षेत्रों में अपेक्षाकृत अधिक।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 3: MSME Sector - The Growth Engine -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The MSME Sector: Backbone of Employment in UP</span>
    <span class="lang-hi">2. सूक्ष्म, लघु एवं मध्यम उद्यम (MSME): उत्तर प्रदेश में रोजगार की रीढ़</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">Uttar Pradesh is universally recognized as the <strong class="theory-highlight">MSME Capital of India</strong>, hosting the maximum concentration of traditional and modern micro and small enterprises in the country:</span>
    <span class="lang-hi">उत्तर प्रदेश को निर्विवाद रूप से <strong class="theory-highlight">भारत की MSME राजधानी</strong> माना जाता है, जहाँ देश में सूक्ष्म, लघु और मध्यम उद्यमों का सबसे बड़ा संकेंद्रण है:</span>
  </p>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Rank 1 in India:</span> UP is home to over <strong class="theory-highlight">90 lakh (9 million) MSME units</strong>, accounting for approx. <strong class="theory-highlight">14% of India's total MSME base</strong> (highest among all states).</span><span class="lang-hi"><span class="theory-highlight">देश में प्रथम स्थान:</span> उ.प्र. में <strong class="theory-highlight">90 लाख से अधिक MSME इकाइयाँ</strong> कार्यरत हैं, जो भारत के कुल MSME का लगभग <strong class="theory-highlight">14%</strong> है (सभी राज्यों में सर्वाधिक)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Employment Generation:</span> MSMEs provide employment to over <strong class="theory-highlight">1.6 crore (16 million) persons</strong>, generating approx. 60% of total industrial employment outside agriculture.</span><span class="lang-hi"><span class="theory-highlight">रोजगार सृजन:</span> MSME क्षेत्र राज्य में <strong class="theory-highlight">1.6 करोड़ से अधिक व्यक्तियों</strong> को आजीविका प्रदान करता है, जो गैर-कृषि औद्योगिक रोजगार का लगभग 60% है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Export Share:</span> Over <strong class="theory-highlight">70% of total merchandise exports</strong> from Uttar Pradesh originate from the MSME and traditional handicraft clusters.</span><span class="lang-hi"><span class="theory-highlight">निर्यात में योगदान:</span> उत्तर प्रदेश से होने वाले कुल व्यापारिक निर्यातों का <strong class="theory-highlight">70% से अधिक</strong> हिस्सा MSME एवं पारंपरिक हस्तशिल्प क्लस्टरों से आता है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">UP Micro, Small &amp; Medium Enterprises Promotion Policy 2022:</span></span><span class="lang-hi"><span class="theory-highlight">उ.प्र. सूक्ष्म, लघु एवं मध्यम उद्यम प्रोत्साहन नीति 2022:</span></span>
      <ul class="theory-para">
        <li><span class="lang-en">Capital investment subsidy up to 25% for Micro, 20% for Small, and 15% for Medium enterprises.</span><span class="lang-hi">माइक्रो इकाइयों को 25%, लघु को 20% तथा मध्यम इकाइयों को 15% तक पूंजीगत उपादान (सब्सिडी)।</span></li>
        <li><span class="lang-en"><strong>100% exemption on stamp duty</strong> for setting up MSME units in Bundelkhand and Purvanchal regions (75% in Madhyanchal and Paschimanchal).</span><span class="lang-hi">बुंदेलखंड एवं पूर्वांचल में MSME इकाइयाँ स्थापित करने पर <strong class="theory-highlight">स्टाम्प शुल्क में 100% छूट</strong> (मध्यांचल व पश्चिमांचल में 75% छूट)।</span></li>
        <li><span class="lang-en">Financial assistance for patent registration (100% up to ₹5 lakh) and clean green technology adoption.</span><span class="lang-hi">पेटेंट पंजीकरण हेतु 100% वित्तीय सहायता (अधिकतम ₹5 लाख) एवं हरित स्वच्छ तकनीक अपनाने पर अनुदान।</span></li>
      </ul>
    </li>
  </ul>
</div>

<!-- Card 4: One District One Product (ODOP) Scheme -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. One District One Product (ODOP) Scheme (एक जिला एक उत्पाद योजना)</span>
    <span class="lang-hi">3. एक जिला एक उत्पाद (ODOP) योजना: विस्तृत रूपरेखा एवं लाभ</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">The pioneering <strong class="theory-highlight">One District One Product (ODOP)</strong> scheme of Uttar Pradesh was formally inaugurated on <strong class="theory-highlight">24 January 2018 (UP Foundation Day / उत्तर प्रदेश दिवस)</strong> by Hon'ble President Ram Nath Kovind and Chief Minister Yogi Adityanath. It became a benchmark model later adopted nationwide by the Central Government:</span>
    <span class="lang-hi">उत्तर प्रदेश की महत्वाकांक्षी <strong class="theory-highlight">एक जिला एक उत्पाद (ODOP)</strong> योजना का औपचारिक शुभारंभ <strong class="theory-highlight">24 जनवरी 2018 (उत्तर प्रदेश दिवस)</strong> को तत्कालीन राष्ट्रपति रामनाथ कोविंद एवं मुख्यमंत्री योगी आदित्यनाथ द्वारा किया गया। बाद में इसे केंद्र सरकार द्वारा पूरे देश में अपनाया गया:</span>
  </p>

  <h3 class="theory-heading">
    <span class="lang-en">Core Components &amp; Financial Support Mechanisms</span>
    <span class="lang-hi">मुख्य घटक एवं वित्तीय सहायता तंत्र</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">1. ODOP Margin Money Scheme (मार्जिन मनी योजना):</span> Provides financial subsidies on bank loans for setting up or modernizing project units:</span><span class="lang-hi"><span class="theory-highlight">1. ODOP मार्जिन मनी योजना:</span> नई इकाइयां स्थापित करने अथवा आधुनिकीकरण हेतु बैंक ऋण पर पूंजीगत उपादान:</span>
      <ul class="theory-para">
        <li><span class="lang-en">Projects up to ₹25 lakh: Margin money subsidy of <strong class="theory-highlight">25% of project cost</strong> (max ₹6.25 lakh).</span><span class="lang-hi">₹25 लाख तक की परियोजना लागत पर: <strong class="theory-highlight">25% मार्जिन मनी सब्सिडी</strong> (अधिकतम ₹6.25 लाख)।</span></li>
        <li><span class="lang-en">Projects from ₹25 lakh to ₹50 lakh: Subsidy of <strong class="theory-highlight">20%</strong> or ₹6.25 lakh (whichever is higher, max ₹10 lakh).</span><span class="lang-hi">₹25 लाख से ₹50 लाख तक: <strong class="theory-highlight">20%</strong> अथवा ₹6.25 लाख जो अधिक हो (अधिकतम ₹10 लाख)।</span></li>
        <li><span class="lang-en">Projects above ₹50 lakh to ₹1.5 crore: Subsidy of <strong class="theory-highlight">10%</strong> (max ₹20 lakh).</span><span class="lang-hi">₹50 लाख से ₹1.5 करोड़ तक: <strong class="theory-highlight">10%</strong> (अधिकतम ₹20 लाख)।</span></li>
      </ul>
    </li>
    <li><span class="lang-en"><span class="theory-highlight">2. Skill Development &amp; Tool-Kit Distribution:</span> Free 10-day certified technical training provided to artisans, followed by the free distribution of modern electrical/mechanical tool-kits.</span><span class="lang-hi"><span class="theory-highlight">2. कौशल विकास एवं टूल-किट वितरण:</span> पारंपरिक कारीगरों को 10 दिवसीय निःशुल्क तकनीकी प्रशिक्षण तथा प्रशिक्षणोपरांत आधुनिक टूल-किट का निःशुल्क वितरण।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">3. Market Development Assistance (MDA):</span> Financial assistance to participate in national/international fairs, buyer-seller meets, and online marketplaces (Amazon, Flipkart, GeM portal integration).</span><span class="lang-hi"><span class="theory-highlight">3. विपणन सहायता योजना (MDA):</span> राष्ट्रीय एवं अंतर्राष्ट्रीय मेलों, प्रदर्शनियों में भाग लेने पर यात्रा-किराया व स्टॉल शुल्क में 75% तक की प्रतिपूर्ति।</span></li>
  </ul>
</div>

<!-- Card 5: Self-Employment, Skill Missions & Labor Welfare Schemes -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Flagship Employment, Entrepreneurship &amp; Labor Welfare Schemes</span>
    <span class="lang-hi">4. स्वरोजगार, कौशल विकास एवं श्रम कल्याण योजनाएँ (परीक्षा उपयोगी सारणी)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Scheme Name</span><span class="lang-hi">योजना का नाम</span></th>
        <th><span class="lang-en">Target Beneficiary</span><span class="lang-hi">लक्षित लाभार्थी</span></th>
        <th><span class="lang-en">Financial Assistance / Key Provisions</span><span class="lang-hi">वित्तीय सहायता एवं मुख्य प्रावधान</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Mukhyamantri Yuva Swarojgar Yojana</strong></span><span class="lang-hi"><strong>मुख्यमंत्री युवा स्वरोजगार योजना</strong></span></td>
        <td><span class="lang-en">Educated unemployed youth (18-40 yrs, min 10th pass).</span><span class="lang-hi">शिक्षित बेरोजगार युवा (18-40 वर्ष, न्यूनतम 10वीं पास)।</span></td>
        <td><span class="lang-en">Bank loan up to <strong class="theory-highlight">₹25 lakh</strong> for Industrial/Manufacturing unit; up to <strong class="theory-highlight">₹10 lakh</strong> for Service sector. State government provides <strong>25% margin money subsidy</strong> (max ₹6.25 lakh for industry, ₹2.5 lakh for service).</span><span class="lang-hi">उद्योग (विनिर्माण) हेतु <strong class="theory-highlight">₹25 लाख</strong> तक तथा सेवा क्षेत्र हेतु <strong class="theory-highlight">₹10 लाख</strong> तक बैंक ऋण। <strong>25% मार्जिन मनी अनुदान</strong> (उद्योग हेतु अधिकतम ₹6.25 लाख, सेवा हेतु ₹2.5 लाख)।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Vishwakarma Shram Samman Yojana (VSSY)</strong></span><span class="lang-hi"><strong>विश्वकर्मा श्रम सम्मान योजना</strong></span></td>
        <td><span class="lang-en">Traditional village artisans (carpenters, potters, cobblers, tailors, blacksmiths, barbers, goldsmiths).</span><span class="lang-hi">पारंपरिक ग्रामीण दस्तकार (बढ़ई, कुम्हार, मोची, दर्जी, लोहार, नाई, सोनार)।</span></td>
        <td><span class="lang-en">Launched in <strong class="theory-highlight">2019</strong>. 6-day free advanced training, free distribution of modern advanced tool-kits, and collateral-free bank loans from ₹10,000 to ₹10 lakh with interest subsidies.</span><span class="lang-hi">प्रारंभ वर्ष: <strong class="theory-highlight">2019</strong>। 6 दिवसीय निःशुल्क प्रशिक्षण, निःशुल्क आधुनिक टूल-किट वितरण, तथा बिना गारंटी ₹10,000 से ₹10 लाख तक का रियायती बैंक ऋण।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>UP Skill Development Mission (UPSDM)</strong></span><span class="lang-hi"><strong>उ.प्र. कौशल विकास मिशन (UPSDM)</strong></span></td>
        <td><span class="lang-en">Youth aged 14 to 35 years.</span><span class="lang-hi">14 से 35 वर्ष के युवा।</span></td>
        <td><span class="lang-en">Launched in <strong class="theory-highlight">2013</strong> (UP was the <strong class="theory-highlight">first state in India</strong> to establish a dedicated unified Skill Mission). Integrates technical courses across 30+ sectors with direct industrial employment linkage.</span><span class="lang-hi"><strong class="theory-highlight">2013</strong> में प्रारंभ (समर्पित कौशल विकास मिशन स्थापित करने वाला <strong class="theory-highlight">देश का पहला राज्य</strong>)। 30+ क्षेत्रों में निःशुल्क प्रमाणिक कौशल प्रशिक्षण एवं रोजगार लिंकेज।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Rozgar Sangam Portal &amp; Rojgar Melas</strong></span><span class="lang-hi"><strong>रोजगार संगम पोर्टल एवं रोजगार मेले</strong></span></td>
        <td><span class="lang-en">Job seekers and registered employers.</span><span class="lang-hi">नौकरी चाहने वाले युवा एवं नियोक्ता कंपनियां।</span></td>
        <td><span class="lang-en">Unified single digital portal for employment exchange registration, organizing block-level and district-level Rojgar Melas, and national apprenticeship schemes.</span><span class="lang-hi">रोजगार कार्यालय पंजीकरण, जिला व ब्लॉक स्तरीय रोजगार मेलों के आयोजन तथा अप्रेंटिसशिप प्रोत्साहन हेतु एकल डिजिटल मंच।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Atal Residential Schools (अटल आवासीय विद्यालय)</strong></span><span class="lang-hi"><strong>अटल आवासीय विद्यालय योजना</strong></span></td>
        <td><span class="lang-en">Children of registered construction workers (BOCW) and COVID-orphaned children.</span><span class="lang-hi">पंजीकृत निर्माण श्रमिकों (BOCW) के बच्चे एवं कोविड-अनाथ बालक/बालिकाएं।</span></td>
        <td><span class="lang-en">Established in all <strong class="theory-highlight">18 administrative divisional headquarters</strong> of UP. Modeled on Navodaya Vidyalayas, providing 100% free quality boarding education (Classes 6 to 12) under CBSE curriculum.</span><span class="lang-hi">उ.प्र. के सभी <strong class="theory-highlight">18 मंडल मुख्यालयों</strong> में स्थापित। नवोदय विद्यालय की तर्ज पर कक्षा 6 से 12 तक निःशुल्क आवासीय सीबीएसई शिक्षा, भोजन, वस्त्र एवं खेलकूद सुविधाएं।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>BOCW Board Schemes (श्रम कल्याण बोर्ड)</strong></span><span class="lang-hi"><strong>भवन एवं सन्निर्माण कर्मकार कल्याण बोर्ड</strong></span></td>
        <td><span class="lang-en">Registered daily wage construction workers.</span><span class="lang-hi">पंजीकृत भवन एवं निर्माण श्रमिक।</span></td>
        <td><span class="lang-en"><em>Kanya Vivah Sahayata:</em> ₹55,000 for daughter's marriage (₹65,000 in mass marriages); <em>Shishu Hitlabh:</em> ₹20,000 lump-sum on birth of boy, ₹25,000 for girl child; death and accident insurance.</span><span class="lang-hi"><em>कन्या विवाह सहायता:</em> ₹55,000 (सामूहिक विवाह में ₹65,000); <em>शिशु हितलाभ:</em> पुत्र जन्म पर ₹20,000, पुत्री पर ₹25,000 एकमुश्त; मृत्यु एवं दुर्घटना राहत।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>e-Shram Portal Registration</strong></span><span class="lang-hi"><strong>ई-श्रम पोर्टल पंजीकरण</strong></span></td>
        <td><span class="lang-en">Unorganized sector workers (कृषि मजदूर, रेहड़ी-पटरी, गिग वर्कर्स).</span><span class="lang-hi">असंगठित क्षेत्र के श्रमिक (कृषि मजदूर, रेहड़ी-पटरी, गिग वर्कर्स)।</span></td>
        <td><span class="lang-en">Uttar Pradesh ranks <strong class="theory-highlight">1st in India</strong> with over 8.3 crore unorganized workers registered on the national e-Shram portal, providing accidental insurance and direct benefit transfers.</span><span class="lang-hi">उत्तर प्रदेश 8.3 करोड़ से अधिक असंगठित कामगारों के पंजीकरण के साथ देश में <strong class="theory-highlight">नंबर 1</strong> स्थान पर है; ₹2 लाख दुर्घटना बीमा एवं भरण-पोषण भत्ता।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 6: Industrial Corridors & Ease of Doing Business -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Defense Industrial Corridor, Mega Parks &amp; Ease of Doing Business</span>
    <span class="lang-hi">5. उत्तर प्रदेश रक्षा गलियारा, मेगा पार्क एवं ईज ऑफ डूइंग बिजनेस</span>
  </div>

  <h3 class="theory-heading">
    <span class="lang-en">The UP Defense Industrial Corridor (UPDIC - 6 Nodes)</span>
    <span class="lang-hi">उत्तर प्रदेश रक्षा औद्योगिक गलियारा (6 प्रमुख नोड्स)</span>
  </h3>
  <p class="theory-para">
    <span class="lang-en">Announced by the Prime Minister in 2018 during the UP Investors Summit to reduce foreign defense imports and make UP an aerospace hub. Developed along <strong class="theory-highlight">6 designated nodes</strong>:</span>
    <span class="lang-hi">प्रधानमंत्री द्वारा 2018 के इनवेस्टर समिट में विदेशी रक्षा आयातों को कम करने एवं उ.प्र. को एयरोस्पेस हब बनाने हेतु घोषित। यह <strong class="theory-highlight">6 नोड्स</strong> में विकसित किया जा रहा है:</span>
  </p>
  <ol class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">1. Lucknow Node:</span> Manufacturing unit of <strong class="theory-highlight">BrahMos Supersonic Cruise Missiles</strong> (BrahMos Aerospace) and titanium castings.</span><span class="lang-hi"><span class="theory-highlight">1. लखनऊ नोड:</span> <strong class="theory-highlight">ब्रह्मोस सुपरसोनिक क्रूज मिसाइल</strong> निर्माण इकाई (ब्रह्मोस एयरोस्पेस) एवं टाइटेनियम कास्टिंग।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">2. Kanpur Node:</span> Defense testing infrastructure, ordnance manufacture, small arms and artillery production.</span><span class="lang-hi"><span class="theory-highlight">2. कानपुर नोड:</span> रक्षा परीक्षण अवसंरचना, आयुध निर्माण, छोटे हथियार व तोपखाना उत्पादन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">3. Jhansi Node:</span> Heavy combat vehicle testing, propulsion systems, and Bharat Dynamics Limited (BDL) missile manufacturing.</span><span class="lang-hi"><span class="theory-highlight">3. झांसी नोड:</span> लड़ाकू वाहन परीक्षण, प्रणोदन प्रणाली, एवं भारत डायनेमिक्स लिमिटेड (BDL) मिसाइल निर्माण इकाई।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">4. Aligarh Node:</span> Precision components, defense metal hardware, arms parts, and drone manufacturing.</span><span class="lang-hi"><span class="theory-highlight">4. अलीगढ़ नोड:</span> प्रिसिजन कंपोनेंट्स, रक्षा धातु हार्डवेयर, हथियार पुर्जे एवं ड्रोन निर्माण क्लस्टर।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">5. Agra Node:</span> Defense electronics, aeronautical subsystems, and military logistics equipment.</span><span class="lang-hi"><span class="theory-highlight">5. आगरा नोड:</span> डिफेंस इलेक्ट्रॉनिक्स, वैमानिकी सब-सिस्टम एवं सैन्य लॉजिस्टिक्स उपकरण।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">6. Chitrakoot Node:</span> Special focus on defense manufacturing in Bundelkhand along the Bundelkhand Expressway.</span><span class="lang-hi"><span class="theory-highlight">6. चित्रकूट नोड:</span> बुंदेलखंड एक्सप्रेसवे के समीप रक्षा उपकरण एवं उपकरण विनिर्माण क्लस्टर।</span></li>
  </ol>

  <h3 class="theory-heading">
    <span class="lang-en">Ease of Doing Business &amp; Key Digital Portals</span>
    <span class="lang-hi">ईज ऑफ डूइंग बिजनेस एवं प्रमुख डिजिटल पोर्टल</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Nivesh Mitra (निवेश मित्र):</span> UP's flagship online Single Window Clearance System, offering 400+ clearances, licenses, and permits across 30+ government departments without physical human touchpoints.</span><span class="lang-hi"><span class="theory-highlight">निवेश मित्र:</span> उ.प्र. का प्रतिष्ठित ऑनलाइन सिंगल विंडो क्लीयरेंस पोर्टल; 30+ विभागों की 400+ व्यावसायिक एनओसी, लाइसेंस व स्वीकृतियां बिना कार्यालय चक्कर काटे ऑनलाइन उपलब्ध।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Nivesh Sarathi (निवेश सारथी):</span> Dedicated monitoring portal to track investor MoUs, land allotment, incentive disbursement, and resolve industrial grievances.</span><span class="lang-hi"><span class="theory-highlight">निवेश सारथी:</span> निवेशकों के एमओयू, भूमि आवंटन, प्रोत्साहन वितरण व शिकायतों के समाधान की पारदर्शी निगरानी हेतु पोर्टल।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">PM-MITRA Mega Textile Park:</span> 1,000-acre world-class integrated textile and apparel park approved on the <strong class="theory-highlight">Lucknow-Hardoi border</strong> (Attari village) under PM-MITRA scheme.</span><span class="lang-hi"><span class="theory-highlight">PM-मित्र मेगा टेक्सटाइल पार्क:</span> पीएम-मित्र योजना के तहत <strong class="theory-highlight">लखनऊ-हरदोई सीमा</strong> (अटारी गांव) पर 1,000 एकड़ में विश्वस्तरीय एकीकृत टेक्सटाइल एवं अपैरल पार्क।</span></li>
  </ul>
</div>

<!-- Card 7: Master One-Liner Business & Employment Quick Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Master Business &amp; Employment One-Liner Quick Revision Matrix</span>
    <span class="lang-hi">6. उत्तर प्रदेश व्यवसाय एवं रोजगार: एक नज़र में त्वरित परीक्षा सार</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Key Topic / Question</span><span class="lang-hi">प्रमुख विषय / प्रश्न</span></th>
        <th><span class="lang-en">Exact Answer &amp; Key Fact</span><span class="lang-hi">सटीक उत्तर एवं मुख्य तथ्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Launch Date of ODOP Scheme in UP</span><span class="lang-hi">उ.प्र. में ODOP योजना का शुभारंभ कब हुआ?</span></td>
        <td><span class="lang-en"><strong>24 January 2018 (UP Foundation Day)</strong></span><span class="lang-hi"><strong>24 जनवरी 2018 (उत्तर प्रदेश दिवस)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">State target for $1 Trillion Economy deadline</span><span class="lang-hi">उ.प्र. को $1 ट्रिलियन अर्थव्यवस्था बनाने का लक्ष्य वर्ष</span></td>
        <td><span class="lang-en"><strong>2027-28</strong></span><span class="lang-hi"><strong>2027-28</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Rank of UP in India for total MSME units</span><span class="lang-hi">कुल MSME इकाइयों की संख्या में उ.प्र. का देश में स्थान</span></td>
        <td><span class="lang-en"><strong>1st Rank (~90+ lakh units, ~14% of India)</strong></span><span class="lang-hi"><strong>प्रथम स्थान (~90 लाख से अधिक इकाइयाँ, देश का ~14%)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Workforce percentage employed in Agriculture (Census 2011)</span><span class="lang-hi">2011 जनगणना अनुसार उ.प्र. का कृषि पर निर्भर कार्यबल</span></td>
        <td><span class="lang-en"><strong>59.3%</strong> (29.0% Cultivators + 30.3% Agri Laborers)</span><span class="lang-hi"><strong>59.3%</strong> (29.0% काश्तकार + 30.3% खेतिहर मजदूर)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Maximum loan under Mukhyamantri Yuva Swarojgar (Industry)</span><span class="lang-hi">मुख्यमंत्री युवा स्वरोजगार में उद्योग हेतु अधिकतम ऋण</span></td>
        <td><span class="lang-en"><strong>₹25 Lakh</strong> (with 25% margin money subsidy)</span><span class="lang-hi"><strong>₹25 लाख</strong> (25% मार्जिन मनी अनुदान सहित)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Maximum loan under Mukhyamantri Yuva Swarojgar (Service)</span><span class="lang-hi">मुख्यमंत्री युवा स्वरोजगार में सेवा क्षेत्र हेतु अधिकतम ऋण</span></td>
        <td><span class="lang-en"><strong>₹10 Lakh</strong></span><span class="lang-hi"><strong>₹10 लाख</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Vishwakarma Shram Samman Yojana launch year</span><span class="lang-hi">विश्वकर्मा श्रम सम्मान योजना किस वर्ष शुरू हुई?</span></td>
        <td><span class="lang-en"><strong>2019</strong> (for traditional village artisans &amp; craftsmen)</span><span class="lang-hi"><strong>2019</strong> (पारंपरिक ग्रामीण दस्तकारों व कारीगरों हेतु)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">First State in India to set up Skill Development Mission</span><span class="lang-hi">कौशल विकास मिशन गठित करने वाला भारत का पहला राज्य</span></td>
        <td><span class="lang-en"><strong>Uttar Pradesh (UPSDM - 2013)</strong></span><span class="lang-hi"><strong>उत्तर प्रदेश (UPSDM - 2013)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Number of Nodes in UP Defense Industrial Corridor</span><span class="lang-hi">उ.प्र. डिफेंस इंडस्ट्रियल कॉरिडोर में कुल नोड्स की संख्या</span></td>
        <td><span class="lang-en"><strong>6 Nodes</strong> (Agra, Aligarh, Chitrakoot, Jhansi, Kanpur, Lucknow)</span><span class="lang-hi"><strong>6 नोड</strong> (आगरा, अलीगढ़, चित्रकूट, झांसी, कानपुर, लखनऊ)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Location of BrahMos Missile manufacturing unit</span><span class="lang-hi">ब्रह्मोस मिसाइल निर्माण इकाई कहाँ स्थापित की गई है?</span></td>
        <td><span class="lang-en"><strong>Lucknow Node</strong> (Bhatgaon, Lucknow)</span><span class="lang-hi"><strong>लखनऊ नोड</strong> (भटगांव, लखनऊ)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Flagship Single-Window Clearance Portal of UP</span><span class="lang-hi">उ.प्र. का प्रतिष्ठित एकल खिड़की क्लीयरेंस पोर्टल</span></td>
        <td><span class="lang-en"><strong>Nivesh Mitra (निवेश मित्र)</strong></span><span class="lang-hi"><strong>निवेश मित्र</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Location of PM-MITRA Mega Textile Park</span><span class="lang-hi">PM-मित्र मेगा टेक्सटाइल पार्क कहाँ स्थापित किया जा रहा है?</span></td>
        <td><span class="lang-en"><strong>Lucknow-Hardoi border (Attari village, 1,000 acres)</strong></span><span class="lang-hi"><strong>लखनऊ-हरदोई सीमा (अटारी गांव, 1000 एकड़)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Number of Atal Residential Schools in UP</span><span class="lang-hi">उ.प्र. में कुल कितने अटल आवासीय विद्यालय स्थापित हैं?</span></td>
        <td><span class="lang-en"><strong>18 Schools</strong> (in all 18 Divisional Headquarters)</span><span class="lang-hi"><strong>18 विद्यालय</strong> (सभी 18 मंडल मुख्यालयों में)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Rank of UP in e-Shram Portal worker registrations</span><span class="lang-hi">ई-श्रम पोर्टल पर श्रमिक पंजीकरण में उ.प्र. का राष्ट्रीय स्थान</span></td>
        <td><span class="lang-en"><strong>1st Rank</strong> (over 8.3 crore unorganized workers registered)</span><span class="lang-hi"><strong>प्रथम स्थान</strong> (8.3 करोड़ से अधिक असंगठित कामगार पंजीकृत)</span></td>
      </tr>
    </tbody>
  </table>
</div>

</div>
"""

def main():
    target_file = os.path.join("upsssc-up-gk", "business-and-employment", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_business_employment_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
