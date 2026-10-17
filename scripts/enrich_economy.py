import os
import re

def build_economy_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Macroeconomic Structure, Budget &amp; Regional Growth of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का व्यापक आर्थिक ढांचा, बजट एवं क्षेत्रीय विकास</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Economy of Uttar Pradesh] --> B[GSDP & Macro Dimensions]
    A --> C[Sectoral Share in GSVA]
    A --> D[State Budget 2024-25 Architecture]
    A --> E[Regional Economic Disparities]
    A --> F[Power & Energy Infrastructure]
    A --> G[Investment, FDI & Trade Hubs]

    B --> B1[2nd Largest Economy in India ~9.2% of GDP]
    B --> B2[$1 Trillion Target by 2027-28 Deloitte]
    B --> B3[Workforce: 59.3% Agriculture, 32.9% WPR]
    B --> B4[Unemployment Rate down to 2.4-2.6%]

    C --> C1[Primary Sector: 23-25% | Agri, Milk, Sugarcane]
    C --> C2[Secondary Sector: 24-26% | MSMEs & Mfg]
    C --> C3[Tertiary Sector: 49-51% Dominant | Services]

    D --> D1[Budget Size: ₹7.36 Lakh Crore Largest Ever]
    D --> D2[Revenue Surplus: ₹74,147 Crore]
    D --> D3[Fiscal Deficit: 3.46% GSDP FRBM Compliant]
    D --> D4[Tax Revenue: SGST 40% + State Excise + Stamp]

    E --> E1[Western Region: 50% Output, Noida Highest PCI]
    E --> E2[Central Region: Kanpur Industrial, Lucknow Service]
    E --> E3[Eastern Region: Purvanchal, Agrarian, High Density]
    E --> E4[Bundelkhand: Drought Prone, Lowest Density]

    F --> F1[Narora Bulandshahr: Only Nuclear Plant 440 MW]
    F --> F2[Thermal: Obra, Anpara Sonbhadra, Harduaganj Aligarh]
    F --> F3[Hydro: Rihand Dam 300 MW | Solar City: Ayodhya]

    G --> G1[MSME Leader: 90+ Lakh Units 14% of India]
    G --> G2[UP-GIS 2023: 33.5 Lakh Crore MoUs]
    G --> G3[Ease of Doing Business: 2nd Rank Nationally]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की अर्थव्यवस्था] --> B[GSDP एवं व्यापक आर्थिक आधार]
    A --> C[GSVA में क्षेत्रीय हिस्सेदारी]
    A --> D[राज्य बजट 2024-25 संरचना]
    A --> E[क्षेत्रीय आर्थिक विषमताएं: 4 क्षेत्र]
    A --> F[ऊर्जा एवं विद्युत अवसंरचना]
    A --> G[निवेश, एफडीआई एवं व्यापार हब]

    B --> B1[देश की दूसरी सबसे बड़ी अर्थव्यवस्था ~9.2%]
    B --> B2[$1 ट्रिलियन अर्थव्यवस्था लक्ष्य 2027-28 डेलॉयट]
    B --> B3[कार्यबल: 59.3% कृषि निर्भर, 32.9% WPR]
    B --> B4[बेरोजगारी दर घटकर 2.4-2.6%]

    C --> C1[प्राथमिक क्षेत्र: 23-25% | कृषि, दुग्ध, गन्ना]
    C --> C2[द्वितीयक क्षेत्र: 24-26% | MSME व विनिर्माण]
    C --> C3[तृतीयक क्षेत्र: 49-51% सर्वाधिक | सेवा क्षेत्र]

    D --> D1[बजट आकार: ₹7.36 लाख करोड़ ऐतिहासिक आकार]
    D --> D2[राजस्व अधिशेष: ₹74,147 करोड़]
    D --> D3[राजकोषीय घाटा: 3.46% GSDP (FRBM सीमा में)]
    D --> D4[कर राजस्व: SGST ~40% + आबकारी + स्टाम्प]

    E --> E1[पश्चिमी क्षेत्र: 50% उत्पादन, नोएडा शीर्ष प्रति व्यक्ति आय]
    E --> E2[केंद्रीय क्षेत्र: कानपुर औद्योगिक, लखनऊ सेवा हब]
    E --> E3[पूर्वी क्षेत्र: पूर्वांचल, कृषि प्रधान, सघन जनसंख्या]
    E --> E4[बुंदेलखंड: सूखा प्रवृत्त, सबसे कम घनत्व]

    F --> F1[नरोरा बुलंदशहर: एकमात्र परमाणु संयंत्र 440 MW]
    F --> F2[ताप विद्युत: ओबरा, अनपरा सोनभद्र, हरदुआगंज अलीगढ़]
    F --> F3[जल विद्युत: रिहंद बांध 300 MW | सोलर सिटी: अयोध्या]

    G --> G1[MSME राजधानी: 90+ लाख इकाइयाँ देश का 14%]
    G --> G2[UP-GIS 2023: 33.5 लाख करोड़ के निवेश प्रस्ताव]
    G --> G3[ईज ऑफ डूइंग बिजनेस: देश में द्वितीय स्थान]
    </div>
  </div>
</div>

<!-- Card 2: Macroeconomic Dimensions & Target -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Macroeconomic Profile &amp; The $1 Trillion Roadmap</span>
    <span class="lang-hi">1. व्यापक आर्थिक परिदृश्य एवं $1 ट्रिलियन अर्थव्यवस्था रोडमैप</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>National GSDP Contribution:</strong> Uttar Pradesh possesses the <strong>2nd largest economy in India</strong> (behind Maharashtra), contributing approximately <strong>9.2% to India's national GDP</strong>.</span>
      <span class="lang-hi"><strong>राष्ट्रीय GSDP में स्थान:</strong> उत्तर प्रदेश महाराष्ट्र के बाद <strong>भारत की दूसरी सबसे बड़ी अर्थव्यवस्था</strong> है, जो देश के कुल सकल घरेलू उत्पाद में लगभग <strong>9.2% का योगदान</strong> देता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Current GSDP Size:</strong> The Gross State Domestic Product (GSDP) at current prices for 2024-25 is estimated at over <strong>₹27.50 lakh crore (approx. $330 Billion)</strong>, growing at 5.73% higher than the national average.</span>
      <span class="lang-hi"><strong>वर्तमान GSDP आकार:</strong> वर्ष 2024-25 हेतु वर्तमान मूल्यों पर उ.प्र. का सकल राज्य घरेलू उत्पाद (GSDP) <strong>₹27.50 लाख करोड़ (लगभग $330 बिलियन)</strong> से अधिक अनुमानित है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>$1 Trillion Economy Target:</strong> The state government has set an ambitious target to make Uttar Pradesh a <strong>$1 Trillion economy by the fiscal year 2027-28</strong>. Global consultancy firm <strong>Deloitte Touche Tohmatsu India</strong> was appointed as the consultant to frame this structural roadmap.</span>
      <span class="lang-hi"><strong>$1 ट्रिलियन अर्थव्यवस्था का लक्ष्य:</strong> राज्य सरकार ने वित्तीय वर्ष <strong>2027-28 तक उ.प्र. को $1 ट्रिलियन (1 लाख करोड़ डॉलर) की अर्थव्यवस्था</strong> बनाने का लक्ष्य रखा है। इस रोडमैप को तैयार करने हेतु <strong>डेलॉयट इंडिया</strong> को सलाहकार नियुक्त किया गया है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Per Capita Income Trend:</strong> The state's Per Capita Income has doubled from ₹43,000 in 2016-17 to approximately <strong>₹83,000 to ₹90,000</strong> (at current prices in 2023-24). However, it remains below the national average (~₹1.72 lakh).</span>
      <span class="lang-hi"><strong>प्रति व्यक्ति आय की प्रवृत्ति:</strong> राज्य की प्रति व्यक्ति आय 2016-17 के ₹43,000 से बढ़कर वर्तमान में लगभग <strong>₹83,000 से ₹90,000</strong> (वर्तमान मूल्यों पर) हो चुकी है, यद्यपि यह अभी भी राष्ट्रीय औसत (~₹1.72 लाख) से कम है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Workforce &amp; Employment Profile (Census 2011 &amp; PLFS):</strong>
        <br/>• <strong>Agriculture Workers:</strong> <strong>59.3% of the total workforce</strong> depends directly on agriculture (29.03% Cultivators + 30.3% Agricultural Laborers).
        <br/>• <strong>Worker Population Ratio (WPR):</strong> 32.9% according to Census 2011.
        <br/>• <strong>Unemployment Rate (PLFS):</strong> Dropped drastically from over 17.5% in 2017 to <strong>2.4% - 2.6% in 2023-24</strong>.
      </span>
      <span class="lang-hi"><strong>कार्यबल एवं रोजगार संरचना:</strong>
        <br/>• <strong>कृषि पर निर्भर कार्यबल:</strong> कुल कार्यबल का <strong>59.3% भाग</strong> प्रत्यक्ष रूप से कृषि पर निर्भर है (29.03% कृषक + 30.3% कृषि मजदूर)।
        <br/>• <strong>श्रमिक जनसंख्या अनुपात (WPR):</strong> जनगणना 2011 के अनुसार 32.9%।
        <br/>• <strong>बेरोजगारी दर:</strong> 2017 के 17.5% से घटकर 2023-24 में मात्र <strong>2.4% से 2.6%</strong> रह गई है।
      </span>
    </li>
  </ul>
</div>

<!-- Card 3: Sectoral Composition (GSVA Shares) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Sectoral Composition of State Economy (GSVA Analysis)</span>
    <span class="lang-hi">2. राज्य अर्थव्यवस्था की क्षेत्रीय संरचना (GSVA विश्लेषण)</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Structural Transition:</strong> Similar to the national economic shift, UP's Gross State Value Added (GSVA) has transitioned from an agrarian dominance toward a services-led economy, though agriculture still anchors rural livelihood security.</span>
      <span class="lang-hi"><strong>संरचनात्मक बदलाव:</strong> राष्ट्रीय अर्थव्यवस्था की भांति उ.प्र. का सकल राज्य मूल्यवर्धन (GSVA) कृषि प्रधानता से सेवा प्रधान अर्थव्यवस्था की ओर स्थानांतरित हुआ है, यद्यपि ग्रामीण आजीविका में कृषि आज भी सर्वाधिक महत्वपूर्ण है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Primary Sector (प्राथमिक क्षेत्र: 23% - 25% of GSVA):</strong>
        <br/>• Includes Agriculture, Animal Husbandry, Forestry, Fishing, and Mining &amp; Quarrying.
        <br/>• UP ranks <strong>1st in total Foodgrain production (~19% of India)</strong>, 1st in Wheat, 1st in Sugarcane, 1st in Potato, and 1st in Milk.
        <br/>• Provides subsistence to nearly 60% of the state's workforce despite a declining share in state GDP.
      </span>
      <span class="lang-hi"><strong>प्राथमिक क्षेत्र (GSVA का 23% - 25%):</strong>
        <br/>• इसमें कृषि, पशुपालन, वानिकी, मत्स्य पालन तथा खनन व उत्खनन शामिल हैं।
        <br/>• उ.प्र. कुल खाद्यान्न उत्पादन (देश का ~19%), गेहूं, गन्ना, आलू तथा दुग्ध उत्पादन में <strong>देश में प्रथम स्थान</strong> पर है।
        <br/>• GDP में हिस्सा घटने के बावजूद यह राज्य के लगभग 60% कार्यबल को आजीविका प्रदान करता है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Secondary Sector (द्वितीयक क्षेत्र: 24% - 26% of GSVA):</strong>
        <br/>• Includes Manufacturing (Registered &amp; Unregistered), Construction, Electricity, Gas, and Water Supply.
        <br/>• Powered by over <strong>90 lakh MSME units (Rank 1 in India, ~14% share)</strong>, the One District One Product (ODOP) ecosystem, and the Defense Industrial Corridor.
        <br/>• Construction and agro-processing are the fastest-growing secondary sub-sectors.
      </span>
      <span class="lang-hi"><strong>द्वितीयक क्षेत्र (GSVA का 24% - 26%):</strong>
        <br/>• इसमें विनिर्माण (पंजीकृत व अपंजीकृत), निर्माण, विद्युत, गैस एवं जल आपूर्ति शामिल हैं।
        <br/>• <strong>90 लाख से अधिक MSME इकाइयों (देश में प्रथम, ~14% हिस्सेदारी)</strong>, ODOP योजना तथा डिफेंस कॉरिडोर द्वारा संचालित।
        <br/>• निर्माण क्षेत्र एवं कृषि-प्रसंस्करण सबसे तीव्र गति से बढ़ते उप-क्षेत्र हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Tertiary Sector (तृतीयक / सेवा क्षेत्र: 49% - 51% of GSVA):</strong>
        <br/>• The largest contributor to UP's economy.
        <br/>• Encompasses Trade, Hotels &amp; Restaurants, Transport &amp; Storage, Communication, Real Estate &amp; Professional Services, Banking, and Public Administration.
        <br/>• Driven by booming <strong>Spiritual and Heritage Tourism (Rank 1 in domestic tourists)</strong>, IT/ITeS hub in Noida-Greater Noida, and financial intermediation.
      </span>
      <span class="lang-hi"><strong>तृतीयक / सेवा क्षेत्र (GSVA का 49% - 51%):</strong>
        <br/>• उ.प्र. की अर्थव्यवस्था में <strong>सर्वाधिक योगदान देने वाला क्षेत्र</strong>।
        <br/>• इसमें व्यापार, होटल व रेस्टोरेंट, परिवहन व भंडारण, संचार, रियल एस्टेट, बैंकिंग तथा लोक प्रशासन शामिल हैं।
        <br/>• <strong>धार्मिक एवं विरासत पर्यटन (घरेलू पर्यटकों में देश में प्रथम)</strong>, नोएडा-ग्रेटर नोएडा के आईटी हब तथा बैंकिंग सेवाओं द्वारा संचालित।
      </span>
    </li>
  </ul>
</div>

<!-- Card 4: State Budget Architecture & Public Finance -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. State Budget 2024-25 Architecture &amp; Tax Revenue Breakdown</span>
    <span class="lang-hi">3. राज्य बजट 2024-25 संरचना एवं कर राजस्व का विश्लेषण</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Historic Budget Outlay:</strong> Finance Minister Suresh Kumar Khanna presented a budget of <strong>₹7,36,437.71 crore for FY 2024-25</strong>, marking the largest annual financial statement in Uttar Pradesh's history.</span>
      <span class="lang-hi"><strong>ऐतिहासिक बजट आकार:</strong> वित्त मंत्री सुरेश कुमार खन्ना ने वित्तीय वर्ष 2024-25 हेतु <strong>₹7,36,437.71 करोड़ का बजट</strong> पेश किया, जो राज्य के इतिहास का सबसे बड़ा बजट है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Key Budgetary Parameters (2024-25):</strong>
        <br/>• <strong>Total Revenue Receipts:</strong> ₹6,06,802.40 crore (State's Own Tax Revenue ₹2,70,086 crore + Central Tax devolution + non-tax).
        <br/>• <strong>Total Revenue Expenditure:</strong> ₹5,32,655.33 crore.
        <br/>• <strong>Revenue Surplus (राजस्व अधिशेष):</strong> <strong>₹74,147.07 crore</strong> (demonstrating fiscal strength).
        <br/>• <strong>Capital Outlay / Expenditure:</strong> <strong>₹2,03,782.38 crore</strong> (directed towards expressways, airports, and urban metro lines).
        <br/>• <strong>Fiscal Deficit (राजकोषीय घाटा):</strong> <strong>₹86,530.51 crore (3.46% of estimated GSDP)</strong>, strictly complying with the 3.5% ceiling mandated by the Fiscal Responsibility and Budget Management (FRBM) Act.
      </span>
      <span class="lang-hi"><strong>प्रमुख बजटीय आंकड़े (2024-25):</strong>
        <br/>• <strong>कुल राजस्व प्राप्तियां:</strong> ₹6,06,802.40 करोड़ (स्वयं का कर राजस्व ₹2,70,086 करोड़)।
        <br/>• <strong>कुल राजस्व व्यय:</strong> ₹5,32,655.33 करोड़।
        <br/>• <strong>राजस्व अधिशेष (Revenue Surplus):</strong> <strong>₹74,147.07 करोड़</strong> (वित्तीय मजबूती का प्रमाण)।
        <br/>• <strong>पूंजीगत परिव्यय / व्यय:</strong> <strong>₹2,03,782.38 करोड़</strong> (एक्सप्रेसवे, एयरपोर्ट व मेट्रो परियोजनाओं में)।
        <br/>• <strong>राजकोषीय घाटा:</strong> <strong>₹86,530.51 करोड़ (GSDP का 3.46%)</strong>, जो FRBM अधिनियम की 3.5% की सीमा के पूर्णतः अनुकूल है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Composition of State's Own Tax Revenue (SOTR):</strong>
        <br/>1. <strong>State GST (SGST):</strong> Largest individual contributor (~40% of own tax revenue).
        <br/>2. <strong>State Excise Duty (राज्य आबकारी शुल्क):</strong> ~20% - 22% (liquor &amp; alcohol manufacture).
        <br/>3. <strong>Stamp &amp; Registration Fees (स्टाम्प एवं पंजीकरण):</strong> ~13% - 15% (land, property registry).
        <br/>4. <strong>Taxes on Sales / VAT:</strong> Petroleum products and non-GST items.
        <br/>5. <strong>Taxes on Motor Vehicles (वाहन कर):</strong> Transport department road tax.
      </span>
      <span class="lang-hi"><strong>राज्य के स्वयं के कर राजस्व (SOTR) के प्रमुख स्रोत:</strong>
        <br/>1. <strong>राज्य माल एवं सेवा कर (SGST):</strong> सर्वाधिक हिस्सेदारी (~40%)।
        <br/>2. <strong>राज्य आबकारी शुल्क:</strong> ~20% से 22% (मदिरा व स्पिरिट पर कर)।
        <br/>3. <strong>स्टाम्प एवं पंजीकरण शुल्क:</strong> ~13% से 15% (भूमि व अचल संपत्ति रजिस्ट्री)।
        <br/>4. <strong>बिक्री कर / वैट:</strong> पेट्रोलियम उत्पाद एवं गैर-जीएसटी वस्तुएं।
        <br/>5. <strong>वाहन कर (Motor Vehicle Tax):</strong> परिवहन विभाग से प्राप्त पथकर।
      </span>
    </li>
  </ul>
</div>

<!-- Card 5: Regional Economic Disparities -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Regional Economic Disparities: 4 Economic Regions Analysis</span>
    <span class="lang-hi">4. क्षेत्रीय आर्थिक विषमताएं: 4 आर्थिक संभागों का तुलनात्मक विश्लेषण</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Economic Region</span><span class="lang-hi">आर्थिक क्षेत्र</span></th>
          <th><span class="lang-en">Districts Covered</span><span class="lang-hi">शामिल जिले</span></th>
          <th><span class="lang-en">Economic Characteristics</span><span class="lang-hi">आर्थिक विशेषताएं</span></th>
          <th><span class="lang-en">Per Capita &amp; Industrial Status</span><span class="lang-hi">प्रति व्यक्ति आय व औद्योगिक स्थिति</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Western Region (पश्चिमी क्षेत्र)</strong></span><span class="lang-hi"><strong>पश्चिमी क्षेत्र (Western)</strong></span></td>
          <td><span class="lang-en">30 Districts (Meerut, Noida, Agra, Bareilly, Moradabad, Aligarh divisions)</span><span class="lang-hi">30 जिले (मेरठ, नोएडा, आगरा, बरेली, मुरादाबाद, अलीगढ़ मंडल)</span></td>
          <td><span class="lang-en">Most prosperous region; high agricultural productivity (Green Revolution hub), dense tube-well irrigation, proximity to NCR market</span><span class="lang-hi">सर्वाधिक समृद्ध क्षेत्र; उच्च कृषि उत्पादकता (हरित क्रांति बेल्ट), सघन नलकूप सिंचाई, एनसीआर बाजार की निकटता</span></td>
          <td><span class="lang-en">Contributes ~50% to state industrial output; <strong>Gautam Buddha Nagar (Noida) has highest Per Capita Income</strong> in UP</span><span class="lang-hi">राज्य के औद्योगिक उत्पादन का ~50% हिस्सा; <strong>गौतमबुद्ध नगर (नोएडा) राज्य में सर्वोच्च प्रति व्यक्ति आय</strong> वाला जिला</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Central Region (केंद्रीय क्षेत्र)</strong></span><span class="lang-hi"><strong>केंद्रीय क्षेत्र (Central)</strong></span></td>
          <td><span class="lang-en">10 Districts (Lucknow, Kanpur Nagar, Kanpur Dehat, Unnao, Sitapur, Hardoi, etc.)</span><span class="lang-hi">10 जिले (लखनऊ, कानपुर नगर, कानपुर देहात, उन्नाव, सीतापुर, हरदोई आदि)</span></td>
          <td><span class="lang-en">Transitional economy; balanced agricultural and industrial mix; administrative capital (Lucknow) and historical textile/leather base (Kanpur)</span><span class="lang-hi">संक्रमणकालीन अर्थव्यवस्था; कृषि व उद्योग का संतुलित मिश्रण; प्रशासनिक राजधानी (लखनऊ) व ऐतिहासिक चमड़ा/वस्त्र केंद्र (कानपुर)</span></td>
          <td><span class="lang-en">Moderate per capita income; service sector dominance in Lucknow and manufacturing in Kanpur cluster</span><span class="lang-hi">मध्यम प्रति व्यक्ति आय; लखनऊ में सेवा क्षेत्र तथा कानपुर में विनिर्माण क्लस्टर का प्रभुत्व</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Eastern Region / Purvanchal (पूर्वी क्षेत्र)</strong></span><span class="lang-hi"><strong>पूर्वी क्षेत्र / पूर्वांचल</strong></span></td>
          <td><span class="lang-en">28 Districts (Varanasi, Gorakhpur, Prayagraj, Ayodhya, Azamgarh, Mirzapur, Basti)</span><span class="lang-hi">28 जिले (वाराणसी, गोरखपुर, प्रयागराज, अयोध्या, आजमगढ़, मिर्जापुर, बस्ती आदि)</span></td>
          <td><span class="lang-en">Agrarian distress, high population density, small &amp; fragmented landholdings, annual floods (Ghaghara, Rapti), remittance economy</span><span class="lang-hi">कृषि निर्भरता, अत्यधिक जनसंख्या घनत्व, खंडित जोतें, वार्षिक बाढ़ की विभीषिका, प्रवासी धन (Remittance) पर निर्भरता</span></td>
          <td><span class="lang-en">Lower per capita income; <strong>Balrampur, Shravasti, Bahraich have lowest Per Capita Incomes</strong>; now transforming via Purvanchal Expressway</span><span class="lang-hi">निम्न प्रति व्यक्ति आय; <strong>बलरामपुर, श्रावस्ती, बहराइच सबसे कम प्रति व्यक्ति आय</strong> वाले जिले; पूर्वांचल एक्सप्रेसवे से रूपांतरण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Bundelkhand Region (बुंदेलखंड क्षेत्र)</strong></span><span class="lang-hi"><strong>बुंदेलखंड क्षेत्र</strong></span></td>
          <td><span class="lang-en">7 Districts (Jhansi, Lalitpur, Jalaun, Hamirpur, Mahoba, Banda, Chitrakoot)</span><span class="lang-hi">7 जिले (झांसी, ललितपुर, जालौन, हमीरपुर, महोबा, बांदा, चित्रकूट)</span></td>
          <td><span class="lang-en">Drought-prone, rocky unfertile soil, lowest population density, water scarcity, high seasonal outward labor migration</span><span class="lang-hi">बारंबार सूखा, पथरीली अनुपजाऊ भूमि, सबसे कम जनसंख्या घनत्व, जल संकट, अत्यधिक मौसमी पलायन</span></td>
          <td><span class="lang-en">Historically lowest economic base; now designated for Defense Corridor (Jhansi node) &amp; Bundelkhand Expressway</span><span class="lang-hi">ऐतिहासिक रूप से पिछड़ा; अब बुंदेलखंड एक्सप्रेसवे एवं डिफेंस कॉरिडोर (झांसी नोड) से गतिमान</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 6: Power, Energy & Minerals Infrastructure -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Energy, Power Infrastructure &amp; Mineral Endowments</span>
    <span class="lang-hi">5. ऊर्जा, विद्युत अवसंरचना एवं खनिज संपदा</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Narora Atomic Power Station (NAPS, Bulandshahr):</strong>
        <br/>• The <strong>only nuclear power plant in Uttar Pradesh</strong>.
        <br/>• Located at Narora on the banks of Ganga; operates two Pressurized Heavy Water Reactor (PHWR) units of <strong>220 MW each (Total 440 MW)</strong>, commissioned in 1991 and 1992.
      </span>
      <span class="lang-hi"><strong>नरोरा परमाणु ऊर्जा संयंत्र (NAPS, बुलंदशहर):</strong>
        <br/>• उत्तर प्रदेश का <strong>एकमात्र परमाणु विद्युत गृह</strong>।
        <br/>• गंगा तट पर स्थित; 220-220 मेगावाट की दो दाबित भारी जल रिएक्टर (PHWR) इकाइयाँ (<strong>कुल 440 MW</strong>); 1991 व 1992 में चालू।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Major Thermal Power Plants (ताप विद्युत संयंत्र):</strong>
        <br/>• <strong>Harduaganj (Aligarh):</strong> The <strong>oldest thermal power plant in UP</strong> (established in 1942).
        <br/>• <strong>Obra &amp; Anpara (Sonbhadra):</strong> Mega thermal power stations using Singrauli coal basin.
        <br/>• <strong>Parichha (Jhansi):</strong> Key thermal plant serving Bundelkhand.
        <br/>• <strong>Panki (Kanpur):</strong> Historic thermal station modernized with a 660 MW super-critical unit.
        <br/>• <strong>NTPC Plants in UP:</strong> Singrauli (Shaktinagar), Rihand, Unchahar (Rae Bareli), Tanda (Ambedkar Nagar), Dadri (Gautam Buddha Nagar - gas/coal).
      </span>
      <span class="lang-hi"><strong>प्रमुख ताप विद्युत संयंत्र:</strong>
        <br/>• <strong>हरदुआगंज (अलीगढ़):</strong> उ.प्र. का <strong>सबसे पुराना ताप विद्युत गृह</strong> (1942 में स्थापित)।
        <br/>• <strong>ओबरा एवं अनपरा (सोनभद्र):</strong> सिंगरौली कोयला क्षेत्र पर आधारित विशाल ताप विद्युत स्टेशन।
        <br/>• <strong>परीछा (झांसी):</strong> बुंदेलखंड को विद्युत आपूर्ति करने वाला प्रमुख संयंत्र।
        <br/>• <strong>पनकी (कानपुर):</strong> 660 MW सुपरक्रिटिकल इकाई से सुसज्जित आधुनिक ताप विद्युत स्टेशन।
        <br/>• <strong>उ.प्र. में NTPC संयंत्र:</strong> सिंगरौली (शक्तिनगर), रिहंद, ऊंचाहार (रायबरेली), टांडा (अंबेडकर नगर), दादरी (गौतमबुद्ध नगर)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Hydroelectric Power Plants (जल विद्युत संयंत्र):</strong>
        <br/>• <strong>Rihand Dam / Govind Ballabh Pant Sagar (Pipri, Sonbhadra):</strong> <strong>300 MW (6 x 50 MW)</strong>, built on Rihand river.
        <br/>• <strong>Obra Hydroelectric:</strong> 99 MW on Rihand downstream.
        <br/>• <strong>Matatila Hydroelectric:</strong> 30 MW (3 x 10 MW) on Betwa river in Lalitpur district (joint venture with MP).
        <br/>• <strong>Sharda Hydroelectric:</strong> 41.4 MW at Khatima/Banbasa on Sharda river.
      </span>
      <span class="lang-hi"><strong>प्रमुख जल विद्युत परियोजनाएं:</strong>
        <br/>• <strong>रिहंद बांध / गोविंद बल्लभ पंत सागर (पिपरी, सोनभद्र):</strong> रिहंद नदी पर <strong>300 MW (6 x 50 MW)</strong>।
        <br/>• <strong>ओबरा जल विद्युत:</strong> रिहंद के निचले प्रवाह पर 99 MW।
        <br/>• <strong>माताटीला जल विद्युत:</strong> ललितपुर जिले में बेतवा नदी पर 30 MW (उ.प्र. व म.प्र. की संयुक्त परियोजना)।
        <br/>• <strong>शारदा जल विद्युत:</strong> पीलीभीत सीमांत शारदा नदी पर 41.4 MW।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Renewable Energy &amp; Solar Policy 2022:</strong> Target to generate <strong>22,000 MW solar power by 2026-27</strong>. <strong>Ayodhya</strong> is being developed as the state's <strong>First Model Solar City</strong>; 150 MW floating solar project commissioned at Rihand reservoir.</span>
      <span class="lang-hi"><strong>नवीकरणीय ऊर्जा एवं सौर नीति 2022:</strong> वर्ष 2026-27 तक <strong>22,000 MW सौर ऊर्जा</strong> उत्पादन का लक्ष्य। <strong>अयोध्या को प्रथम मॉडल सोलर सिटी</strong> के रूप में विकसित किया जा रहा है; रिहंद जलाशय पर 150 MW फ्लोटिंग सोलर प्लांट स्थापित।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Mineral Resources Endowment:</strong> UP is a mineral-deficient state, but southern Vindhyan-Bundelkhand hills yield crucial minerals:
        <br/>• <strong>Coal:</strong> Found exclusively in <strong>Singrauli coalfield (Sonbhadra)</strong>.
        <br/>• <strong>Limestone (चूना पत्थर):</strong> Guruma, Kanach, Basuhari in <strong>Sonbhadra &amp; Mirzapur</strong> (supplies cement plants at Churk and Dalla).
        <br/>• <strong>Glass Sand (कांच बालू / सिलिका सैंड):</strong> Shankargarh (Prayagraj) - ranks 1st in India.
        <br/>• <strong>Uranium:</strong> Minor reserves found exclusively in <strong>Lalitpur district</strong>.
        <br/>• <strong>Bauxite (एल्युमिनियम अयस्क):</strong> Banda, Varanasi, and Lalitpur (supplies Hindalco Renukoot aluminum plant).
      </span>
      <span class="lang-hi"><strong>खनिज संसाधन संपदा:</strong> उ.प्र. खनिज संपदा की दृष्टि से मध्यम-निम्न श्रेणी का राज्य है, किंतु दक्षिणी पठारी जिले महत्वपूर्ण खनिज प्रदान करते हैं:
        <br/>• <strong>कोयला:</strong> केवल <strong>सिंगरौली कोयला क्षेत्र (सोनभद्र)</strong> में पाया जाता है।
        <br/>• <strong>चूना पत्थर:</strong> <strong>सोनभद्र व मिर्जापुर</strong> के कजराहट, गुरमा व बासुहारी (चुर्क व डाला सीमेंट कारखानों को आपूर्ति)।
        <br/>• <strong>कांच बालू (सिलिका सैंड):</strong> शंकरगढ़ (प्रयागराज) - उत्पादन में देश में अग्रणी।
        <br/>• <strong>यूरेनियम:</strong> सीमित भंडार केवल <strong>ललितपुर जिले</strong> में पाए जाते हैं।
        <br/>• <strong>बॉक्साइट:</strong> बांदा, वाराणसी व ललितपुर (हिंडाल्को रेनूकूट एल्युमिनियम संयंत्र को आपूर्ति)।
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Fact Matrix: UP Economy (Direct Exam Points)</span>
    <span class="lang-hi">6. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. की अर्थव्यवस्था (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Economic Indicator</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / आर्थिक संकेतक</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">What is the national ranking of UP in terms of GSDP size?</span><span class="lang-hi">GSDP के आकार की दृष्टि से देश में उ.प्र. का कौन सा स्थान है?</span></td>
          <td><span class="lang-en"><strong>2nd Largest Economy</strong> (contributing ~9.2% to India's GDP)</span><span class="lang-hi"><strong>दूसरा सबसे बड़ा राज्य</strong> (राष्ट्रीय GDP में ~9.2% हिस्सा)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the target year for UP to achieve a $1 Trillion economy?</span><span class="lang-hi">उ.प्र. को $1 ट्रिलियन अर्थव्यवस्था बनाने का लक्ष्य वर्ष क्या है?</span></td>
          <td><span class="lang-en"><strong>Fiscal Year 2027-28</strong> (Consultant: Deloitte India)</span><span class="lang-hi"><strong>वित्तीय वर्ष 2027-28</strong> (सलाहकार: डेलॉयट इंडिया)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which sector contributes the maximum share to UP's GSVA?</span><span class="lang-hi">उ.प्र. के GSVA में सर्वाधिक हिस्सेदारी किस क्षेत्र की है?</span></td>
          <td><span class="lang-en"><strong>Tertiary / Services Sector (49% - 51%)</strong></span><span class="lang-hi"><strong>तृतीयक / सेवा क्षेत्र (49% से 51%)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What percentage of UP's total workforce depends on agriculture?</span><span class="lang-hi">उ.प्र. के कुल कार्यबल का कितने प्रतिशत भाग कृषि पर निर्भर है?</span></td>
          <td><span class="lang-en"><strong>59.3%</strong> (29.03% Cultivators + 30.3% Agri Laborers)</span><span class="lang-hi"><strong>59.3%</strong> (29.03% कृषक + 30.3% कृषि मजदूर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What was the total outlay of UP State Budget for 2024-25?</span><span class="lang-hi">वित्तीय वर्ष 2024-25 हेतु उ.प्र. बजट का कुल आकार कितना था?</span></td>
          <td><span class="lang-en"><strong>₹7,36,437.71 crore</strong> (Largest in state's history)</span><span class="lang-hi"><strong>₹7,36,437.71 करोड़</strong> (राज्य इतिहास का सबसे बड़ा बजट)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the estimated Fiscal Deficit percentage in Budget 2024-25?</span><span class="lang-hi">बजट 2024-25 में राजकोषीय घाटा GSDP का कितना प्रतिशत अनुमानित है?</span></td>
          <td><span class="lang-en"><strong>3.46% of GSDP</strong> (within the 3.5% FRBM ceiling)</span><span class="lang-hi"><strong>GSDP का 3.46%</strong> (3.5% की FRBM सीमा के भीतर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which tax yields the highest revenue to the UP government?</span><span class="lang-hi">उ.प्र. सरकार को सर्वाधिक कर राजस्व किस मद से प्राप्त होता है?</span></td>
          <td><span class="lang-en"><strong>State GST (SGST)</strong> (followed by State Excise Duty)</span><span class="lang-hi"><strong>राज्य माल एवं सेवा कर (SGST)</strong> (इसके बाद राज्य आबकारी)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the highest Per Capita Income in UP?</span><span class="lang-hi">उ.प्र. में सर्वाधिक प्रति व्यक्ति आय वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Gautam Buddha Nagar (Noida)</strong></span><span class="lang-hi"><strong>गौतमबुद्ध नगर (नोएडा)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the lowest Per Capita Income in UP?</span><span class="lang-hi">उ.प्र. में न्यूनतम प्रति व्यक्ति आय वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Balrampur / Shravasti</strong></span><span class="lang-hi"><strong>बलरामपुर / श्रावस्ती</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the only nuclear power plant located in UP?</span><span class="lang-hi">उत्तर प्रदेश का एकमात्र परमाणु ऊर्जा संयंत्र कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Narora (Bulandshahr district)</strong> (440 MW PHWR)</span><span class="lang-hi"><strong>नरोरा (बुलंदशहर)</strong> (440 MW PHWR)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the oldest thermal power station in Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश का सबसे पुराना ताप विद्युत गृह कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Harduaganj Thermal Power Plant (Aligarh, est. 1942)</strong></span><span class="lang-hi"><strong>हरदुआगंज ताप विद्युत गृह (अलीगढ़, स्थापना 1942)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which district are coal reserves found in Uttar Pradesh?</span><span class="lang-hi">उ.प्र. के किस जिले में कोयले के भंडार पाए जाते हैं?</span></td>
          <td><span class="lang-en"><strong>Sonbhadra district (Singrauli coalfield)</strong></span><span class="lang-hi"><strong>सोनभद्र जिला (सिंगरौली कोयला क्षेत्र)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which district are Uranium reserves exclusively found in UP?</span><span class="lang-hi">उ.प्र. में यूरेनियम के भंडार विशेष रूप से किस जिले में पाए जाते हैं?</span></td>
          <td><span class="lang-en"><strong>Lalitpur district</strong> (ललितपुर)</span><span class="lang-hi"><strong>ललितपुर जिला</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the largest silica / glass-sand mining area in UP?</span><span class="lang-hi">उ.प्र. में कांच बालू (सिलिका सैंड) का प्रमुख खनन क्षेत्र कहाँ है?</span></td>
          <td><span class="lang-en"><strong>Shankargarh (Prayagraj district)</strong></span><span class="lang-hi"><strong>शंकरगढ़ (प्रयागराज जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city is being developed as UP's first Model Solar City?</span><span class="lang-hi">उ.प्र. की पहली मॉडल सोलर सिटी के रूप में किसे विकसित किया जा रहा है?</span></td>
          <td><span class="lang-en"><strong>Ayodhya (अयोध्या)</strong></span><span class="lang-hi"><strong>अयोध्या</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "economy", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_economy_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
