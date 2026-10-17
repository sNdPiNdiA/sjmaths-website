import os
import re

def build_architecture_theory_html():
    return """
<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Architectural Heritage of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की स्थापत्य एवं वास्तुकला विरासत</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Architecture of UP] --> B[Ancient & Buddhist]
    A --> C[Gupta Golden Age]
    A --> D[Sharqi Style Jaunpur]
    A --> E[Mughal Imperial Architecture]
    A --> F[Awadh Nawabi Architecture]
    A --> G[Colonial & Indo-Saracenic]
    A --> H[Modern & Nagara Style]

    B --> B1[Sarnath: Dhamekh & Chaukhandi Stupa]
    B --> B2[Kushinagar: Parinirvana Stupa]
    B --> B3[Piprahwa: Relic Casket of Buddha]
    B --> B4[Ashokan Lion Capital: Sarnath Emblem]
    B --> B5[Mathura School: Spotted Red Sandstone]

    C --> C1[Deogarh Dashavatara: First Shikhara & Panchayatana]
    C --> C2[Bhitargaon Kanpur: Oldest Brick/Terracotta Temple]
    C --> C3[Bhitari Pillar: Skandagupta Huna Victory]

    D --> D1[Jaunpur Shiraz of East: No minarets, Massive Propylons]
    D --> D2[Atala Masjid 1408 Ibrahim Sharqi]
    D --> D3[Jama Masjid, Lal Darwaza, Shahi Pul 1568]

    E --> E1[Babur: Aram Bagh Agra 1526 Charbagh]
    E --> E2[Akbar: Agra Fort 1565 & Fatehpur Sikri 1569]
    E --> E3[Sikri: Buland Darwaza 1601, Panch Mahal, Salim Chishti Tomb]
    E --> E4[Jahangir: Akbar Tomb Sikandra & Itimad-ud-Daula 1622 Pietra Dura]
    E --> E5[Shah Jahan: Taj Mahal 1631-1653 Lahauri & Moti Masjid]

    F --> F1[Lakhauri Bricks & Lime Stucco & Fish Motifs]
    F --> F2[Bara Imambara 1784: Pillarless Asafi Vault & Bhul-Bhulaiya]
    F --> F3[Rumi Darwaza: 60 ft Turkish Gate of Constantinople]
    F --> F4[Chhota Imambara, Chattar Manzil, Qaiserbagh]

    G --> G1[Indo-Saracenic: Charbagh Station 1914 Chessboard]
    G --> G2[Gothic: All Saints Cathedral Prayagraj William Emerson]
    G --> G3[Allahabad High Court 1916 & Lucknow Residency]

    H --> H1[Vidhan Sabha 1928 Classic-Awadhi]
    H --> H2[Ram Mandir Ayodhya: Nagara Style Sompura Bansi Paharpur]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की वास्तुकला] --> B[प्राचीन एवं बौद्ध काल]
    A --> C[गुप्त काल का स्वर्ण युग]
    A --> D[शर्की शैली जौनपुर]
    A --> E[मुगल शाही वास्तुकला]
    A --> F[अवध की नवाबी वास्तुकला]
    A --> G[औपनिवेशिक एवं इंडो-सारसेनिक]
    A --> H[आधुनिक एवं नागर शैली]

    B --> B1[सारनाथ: धमेख एवं चौखंडी स्तूप]
    B --> B2[कुशीनगर: परिनिर्वाण स्तूप]
    B --> B3[पिपरहवा: बुद्ध अस्थि मंजूषा स्तूप]
    B --> B4[अशोक सिंह शीर्ष: सारनाथ राष्ट्रीय प्रतीक]
    B --> B5[मथुरा कला: लाल चित्तीदार बलुआ पत्थर]

    C --> C1[देवगढ़ दशावतार: प्रथम शिखर व पंचायतन]
    C --> C2[भीतरगाँव कानपुर: प्राचीनतम ईंट-टेराकोटा मंदिर]
    C --> C3[भीतरी स्तंभ: स्कंदगुप्त हूण विजय]

    D --> D1[जौनपुर शिराज-ए-हिंद: मीनारविहीन, विशाल तोरणद्वार]
    D --> D2[अटाला मस्जिद 1408 इब्राहिम शर्की]
    D --> D3[जामा मस्जिद, लाल दरवाजा, शाही पुल 1568]

    E --> E1[बाबर: आराम बाग आगरा 1526 चारबाग]
    E --> E2[अकबर: आगरा किला 1565 व फतेहपुर सीकरी 1569]
    E --> E3[सीकरी: बुलंद दरवाजा 1601, पंचमहल, सलीम चिश्ती दरगाह]
    E --> E4[जहांगीर: अकबर मकबरा सिकंदरा व एतमादुद्दौला 1622 पितरा दुरा]
    E --> E5[शाहजहाँ: ताजमहल 1631-1653 लाहौरी व मोती मस्जिद]

    F --> F1[लखौरी ईंटें, चूना प्लास्टर एवं मछली प्रतीक]
    F --> F2[बड़ा इमामबाड़ा 1784: बिना खंभे का हॉल व भूल-भुलैया]
    F --> F3[रूमी दरवाजा: 60 फीट कांस्टेंटिनोपल तुर्की द्वार]
    F --> F4[छोटा इमामबाड़ा, छत्तर मंजिल, कैसरबाग]

    G --> G1[इंडो-सारसेनिक: चारबाग स्टेशन 1914 शतरंज दृश्य]
    G --> G2[गोथिक: ऑल सेंट्स कैथेड्रल प्रयागराज विलियम एमर्सन]
    G --> G3[इलाहाबाद हाईकोर्ट 1916 व लखनऊ रेजिडेंसी]

    H --> H1[विधानसभा भवन 1928 यूरोपीय-अवधी]
    H --> H2[राम मंदिर अयोध्या: नागर शैली सोमपुरा बंसी पहाड़पुर]
    </div>
  </div>
</div>

<!-- Card 2: Ancient, Harappan & Buddhist Stupa Architecture in UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Ancient, Harappan &amp; Buddhist Architecture in UP</span>
    <span class="lang-hi">1. उत्तर प्रदेश की प्राचीन, हड़प्पा एवं बौद्ध स्थापत्य कला</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Monument / Site</span><span class="lang-hi">स्मारक / स्थल</span></th>
        <th><span class="lang-en">Location (District)</span><span class="lang-hi">स्थान (जिला)</span></th>
        <th><span class="lang-en">Architectural Features &amp; Exam Facts</span><span class="lang-hi">स्थापत्य विशेषताएँ एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Alamgirpur &amp; Sinauli</strong></span><span class="lang-hi"><strong>आलमगीरपुर एवं सनौली</strong></span></td>
        <td><span class="lang-en">Alamgirpur (Meerut), Sinauli (Baghpat), Hulas (Saharanpur).</span><span class="lang-hi">आलमगीरपुर (मेरठ), सनौली (बागपत), हुलास (सहारनपुर)।</span></td>
        <td><span class="lang-en">Alamgirpur on Hindon river is the easternmost Indus Valley site. Sinauli revealed India's first Bronze Age war chariots, anthropomorphic coffins, and copper swords (2000-1800 BCE).</span><span class="lang-hi">हिंडन नदी तट पर आलमगीरपुर हड़प्पा सभ्यता का सबसे पूर्वी स्थल है। सनौली से कांस्य युगीन युद्ध रथ, मानव रूपी ताबूत एवं तांबे की तलवारें (2000-1800 ई.पू.) प्राप्त हुईं।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Dhamekh Stupa (धमेख स्तूप)</strong></span><span class="lang-hi"><strong>धमेख स्तूप</strong></span></td>
        <td><span class="lang-en"><strong>Sarnath (Varanasi)</strong></span><span class="lang-hi"><strong>सारनाथ (वाराणसी)</strong></span></td>
        <td><span class="lang-en">Marks the spot of Buddha's first sermon (Dharmachakrapravartana). Solid cylindrical tower of Chunar sandstone and bricks (height 43.6 m, diameter 28 m); intricately carved with Gupta geometric and floral swags.</span><span class="lang-hi">भगवान बुद्ध के प्रथम उपदेश (धर्मचक्रप्रवर्तन) स्थल का प्रतीक। चुनार बलुआ पत्थर व ईंटों से निर्मित ठोस बेलनाकार स्तूप (ऊंचाई 43.6 मी, व्यास 28 मी); गुप्तकालीन ज्यामितीय व स्वस्तिक नक्काशी।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Chaukhandi Stupa (चौखंडी स्तूप)</strong></span><span class="lang-hi"><strong>चौखंडी स्तूप</strong></span></td>
        <td><span class="lang-en"><strong>Sarnath (Varanasi)</strong></span><span class="lang-hi"><strong>सारनाथ (वाराणसी)</strong></span></td>
        <td><span class="lang-en">Marks where Buddha met his first five disciples. High terraced brick mound crowned with an <em>octagonal Mughal tower</em> built in 1588 by Govardhan (son of Raja Todar Mal) to commemorate Emperor Humayun's visit.</span><span class="lang-hi">बुद्ध द्वारा अपने पांच प्रथम शिष्यों से मिलन स्थल। ईंटों की सीढ़ीदार संरचना; शीर्ष पर 1588 में राजा टोडरमल के पुत्र गोवर्धन द्वारा हुमायूँ के आगमन की स्मृति में अष्टकोणीय मुगल मीनार बनाई गई।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Ashoka Lion Capital (सिंह शीर्ष)</strong></span><span class="lang-hi"><strong>अशोक का सिंह शीर्ष</strong></span></td>
        <td><span class="lang-en"><strong>Sarnath (Varanasi)</strong></span><span class="lang-hi"><strong>सारनाथ (वाराणसी)</strong></span></td>
        <td><span class="lang-en">Carved from a single block of polished Chunar sandstone (3rd century BCE). Features four back-to-back Asiatic lions, circular abacus with 4 animals (elephant, galloping horse, bull, lion) separated by 24-spoke Dharmachakras. Adopted as India's National Emblem on <strong>26 January 1950</strong>.</span><span class="lang-hi">चुनार के पॉलिशदार बलुआ पत्थर से एकाश्मक नक्काशी (तीसरी शताब्दी ई.पू.)। चार पीठ सटाए सिंह, 24 तीलियों वाले धर्मचक्रों से विभाजित 4 पशु (हाथी, घोड़ा, बैल, सिंह)। <strong class="theory-highlight">26 जनवरी 1950</strong> को भारत का राष्ट्रीय प्रतीक स्वीकृत।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Parinirvana Stupa &amp; Temple</strong></span><span class="lang-hi"><strong>महापरिनिर्वाण स्तूप एवं मंदिर</strong></span></td>
        <td><span class="lang-en"><strong>Kushinagar</strong></span><span class="lang-hi"><strong>कुशीनगर</strong></span></td>
        <td><span class="lang-en">Site of Buddha's death (Mahaparinirvana) in 483 BCE. Houses a 6.1-meter-long monolith red sandstone reclining statue of Buddha in dying posture. Nearby Ramabhar Stupa is Buddha's cremation mound.</span><span class="lang-hi">483 ई.पू. में बुद्ध के महापरिनिर्वाण का स्थल। मंदिर में 6.1 मीटर लंबी लाल बलुआ पत्थर की लेटी हुई बुद्ध प्रतिमा। निकटवर्ती रामाभार स्तूप बुद्ध का अंतिम संस्कार स्थल है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Piprahwa Stupa (पिपरहवा स्तूप)</strong></span><span class="lang-hi"><strong>पिपरहवा स्तूप</strong></span></td>
        <td><span class="lang-en"><strong>Siddharthnagar</strong></span><span class="lang-hi"><strong>सिद्धार्थनगर</strong></span></td>
        <td><span class="lang-en">Identified with historical Kapilavastu. Excavations yielded inscribed steatite urns containing genuine bone relics of Gautama Buddha donated by the Sakya clan.</span><span class="lang-hi">ऐतिहासिक कपिलवस्तु के रूप में चिन्हित। शाक्यों द्वारा स्थापित बुद्ध के वास्तविक अस्थि अवशेष युक्त नक्काशीदार प्रस्तर मंजूषाएं उत्खनन से प्राप्त।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mathura School of Art (मथुरा कला शैली)</strong></span><span class="lang-hi"><strong>मथुरा मूर्तिकला एवं स्थापत्य</strong></span></td>
        <td><span class="lang-en"><strong>Mathura &amp; Sonkh</strong></span><span class="lang-hi"><strong>मथुरा एवं सोंख</strong></span></td>
        <td><span class="lang-en">Flourished under Kushana emperors (1st-3rd century CE). Carved exclusively from <em>spotted red sandstone</em> (लाल चित्तीदार बलुआ पत्थर). First to carve human images of Buddha, Jain Tirthankara Ayagapatas (Kankali Tila), and Hindu deities (Vishnu, Shiva, Kartikeya).</span><span class="lang-hi">कुषाण काल (प्रथम-तृतीय शताब्दी ई.) में चरमोत्कर्ष। <em>लाल चित्तीदार बलुआ पत्थर</em> का विशेष प्रयोग। बुद्ध की प्रथम मानवीय प्रतिमाएं, जैन तीर्थंकर आयागपट्ट (कंकाली टीला) और हिंदू देवताओं की प्रारंभिक मूर्तियां।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 3: Gupta Architecture - The Birth of Shikhara & Brick Temples -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Gupta Period Architecture: The Golden Age of Temples</span>
    <span class="lang-hi">2. गुप्तकालीन वास्तुकला: मंदिर स्थापत्य का स्वर्ण युग (शिखर व ईंट मंदिर)</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">The Gupta period (4th-6th Century CE) represents the structural genesis of classical Hindu temple architecture in North India:</span>
    <span class="lang-hi">गुप्त काल (4थी-6ठी शताब्दी ईस्वी) उत्तर भारत में शास्त्रीय हिंदू मंदिर स्थापत्य के विकास का प्रारंभिक एवं सबसे महत्वपूर्ण चरण है:</span>
  </p>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Dashavatara Temple, Deogarh (दशावतार मंदिर, देवगढ़):</span> Located in <strong class="theory-highlight">Lalitpur district</strong> on Betwa river bank. Built in early 6th century CE. It is the <strong class="theory-highlight">first surviving North Indian temple with a Shikhara (spire)</strong>. Follows the classical <strong class="theory-highlight">Panchayatana style</strong> (main central shrine on a raised plinth flanked by 4 corner shrines). Famous for masterpiece relief sculptures: <em>Sheshashayi Vishnu</em> (विष्णु अनंतशयन मुद्रा में), <em>Gajendramoksha</em>, and <em>Nara-Narayana</em>. River goddesses Ganga and Yamuna are carved on the doorways.</span><span class="lang-hi"><span class="theory-highlight">दशावतार मंदिर, देवगढ़:</span> <strong class="theory-highlight">ललितपुर जिले</strong> में बेतवा नदी के तट पर स्थित। 6ठी शताब्दी ई. की शुरुआत में निर्मित। यह उत्तर भारत का <strong class="theory-highlight">पहला शिखरयुक्त मंदिर</strong> है। <strong class="theory-highlight">पंचायतन शैली</strong> में निर्मित (मुख्य मंदिर के चारों कोनों पर चार लघु मंदिर)। प्रसिद्ध नक्काशी: <em>शेषशायी विष्णु</em>, <em>गजेंद्रमोक्ष</em>, एवं <em>नर-नारायण तपस्या</em>। गर्भगृह के प्रवेश द्वार पर गंगा एवं यमुना की मूर्तियाँ उत्कीर्ण हैं।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Bhitargaon Brick Temple (भीतरगाँव ईंट मंदिर):</span> Located in <strong class="theory-highlight">Kanpur Nagar district</strong>. 5th century Gupta era. It is the <strong class="theory-highlight">oldest surviving complete brick and terracotta temple in India</strong>. Features a square sanctum, a stepped pyramidal shikhara (height ~21 meters), and rare true arches (*voussoir arch system*). Wall niches contain terracotta panels of Shiva, Parvati, Ganesha, and Durga slaying Mahishasura.</span><span class="lang-hi"><span class="theory-highlight">भीतरगाँव का ईंट मंदिर:</span> <strong class="theory-highlight">कानपुर नगर जिले</strong> में स्थित। 5वीं शताब्दी गुप्त काल। यह भारत में <strong class="theory-highlight">ईंटों तथा टेराकोटा से बना सबसे प्राचीन जीवित मंदिर</strong> है। इसमें वर्गाकार गर्भगृह, ऊंचा सीढ़ीदार पिरामिडीय शिखर (ऊंचाई ~21 मीटर) और वास्तविक मेहराब प्रणाली पाई जाती है। बाहरी दीवारों पर शिव, पार्वती, गणेश एवं महिषासुरमर्दिनी की टेराकोटा पट्टिकाएँ लगी हैं।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Bhitari Pillar &amp; Temple Complex (भीतरी स्तंभ):</span> Located in <strong class="theory-highlight">Saidpur tehsil, Ghazipur district</strong>. Monolithic red sandstone pillar erected by Gupta Emperor <strong class="theory-highlight">Skandagupta</strong>. The Sanskrit inscription details his heroic victory over the fierce Huna invaders, saving the Gupta Empire.</span><span class="lang-hi"><span class="theory-highlight">भीतरी स्तंभ एवं मंदिर परिसर:</span> <strong class="theory-highlight">सैदपुर तहसील, गाजीपुर जिले</strong> में स्थित। गुप्त सम्राट <strong class="theory-highlight">स्कंदगुप्त</strong> द्वारा स्थापित एकाश्मक चुनार प्रस्तर स्तंभ। संस्कृत अभिलेख में हूण आक्रमणकारियों पर स्कंदगुप्त की ऐतिहासिक विजय का विस्तृत वर्णन है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Garhwa Fort &amp; Temple Complex (गढ़वा किला एवं मंदिर):</span> Located at Shankargarh, <strong class="theory-highlight">Prayagraj district</strong>. Contains Gupta period stone temples, Vishnu statues, and inscriptions of Chandragupta II and Kumaragupta I.</span><span class="lang-hi"><span class="theory-highlight">गढ़वा किला एवं मंदिर परिसर:</span> शंकरगढ़, <strong class="theory-highlight">प्रयागराज जिले</strong> में स्थित। गुप्तकालीन प्रस्तर मंदिर, विष्णु प्रतिमाएँ तथा चंद्रगुप्त द्वितीय व कुमारगुप्त प्रथम के अभिलेख मौजूद हैं।</span></li>
  </ul>
</div>

<!-- Card 4: Medieval Architecture - Sharqi Style of Jaunpur -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Medieval Sultanate Architecture: The Sharqi Style of Jaunpur</span>
    <span class="lang-hi">3. मध्यकालीन सल्तनत वास्तुकला: जौनपुर की शर्की स्थापत्य शैली ("पूर्व का शिराज")</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">Jaunpur was founded in 1359 by Sultan Firoz Shah Tughlaq in memory of his cousin Muhammad bin Tughlaq (Jauna Khan). It earned the prestigious title <span class="theory-highlight">"Shiraz-e-Hind" (पूर्व का शिराज)</span> for its flourishing Islamic learning and distinct regional architecture under the Sharqi rulers (1394-1479):</span>
    <span class="lang-hi">जौनपुर की स्थापना 1359 में फिरोज शाह तुगलक ने अपने चचेरे भाई मुहम्मद बिन तुगलक (जौना खां) की स्मृति में की थी। शर्की सुल्तानों (1394-1479) के संरक्षण में शिक्षा एवं विशिष्ट वास्तुकला के कारण इसे <span class="theory-highlight">"शीराज-ए-हिंद"</span> कहा गया:</span>
  </p>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Key Characteristics of Sharqi Architecture:</span> Total <strong class="theory-highlight">absence of slender minarets</strong>, presence of gigantic battered gate screens called <strong class="theory-highlight">Propylons</strong> (विशाल ढलवां तोरणद्वार), arched cloisters with heavy stone beams and brackets, and perforated stone lattice (Jali) windows.</span><span class="lang-hi"><span class="theory-highlight">शर्की शैली की प्रमुख विशेषताएँ:</span> पतली <strong class="theory-highlight">मीनारों का पूर्ण अभाव</strong>, मस्जिदों के अग्रभाग में विशाल ढलवां तोरणद्वार (<strong class="theory-highlight">प्रोपिलोन</strong>), भारी प्रस्तर बीम व कोष्ठक, तथा सुंदर पत्थर की जालीदार खिड़कियाँ।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Atala Masjid, Jaunpur (अटाला मस्जिद):</span> Completed in <strong class="theory-highlight">1408</strong> by Sultan <strong class="theory-highlight">Ibrahim Shah Sharqi</strong>. The most iconic masterpiece of Sharqi architecture. The central entrance pylon rises to 75 feet with fine relief arches, completely concealing the dome behind it.</span><span class="lang-hi"><span class="theory-highlight">अटाला मस्जिद, जौनपुर:</span> सुल्तान <strong class="theory-highlight">इब्राहिम शाह शर्की</strong> द्वारा <strong class="theory-highlight">1408</strong> में पूर्ण। शर्की शैली का सर्वश्रेष्ठ नमूना। इसका केंद्रीय तोरणद्वार (प्रोपिलोन) 75 फीट ऊंचा है जो पीछे के मुख्य गुंबद को पूरी तरह छिपा लेता है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Jama Masjid / Bari Masjid, Jaunpur (जामा मस्जिद):</span> Built by Sultan <strong class="theory-highlight">Hussain Shah Sharqi</strong> in <strong class="theory-highlight">1470</strong>. Built on a 20-foot high raised terrace, it is the largest mosque in Jaunpur.</span><span class="lang-hi"><span class="theory-highlight">बड़ी जामी मस्जिद, जौनपुर:</span> सुल्तान <strong class="theory-highlight">हुसैन शाह शर्की</strong> द्वारा <strong class="theory-highlight">1470</strong> में निर्मित। 20 फीट ऊंचे चबूतरे पर स्थित जौनपुर की सबसे विशाल मस्जिद।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Lal Darwaza Masjid (लाल दरवाजा मस्जिद):</span> Built in <strong class="theory-highlight">1450</strong> by Bibi Raji, queen of Sultan Mahmud Shah Sharqi; famous for its distinctive red gate.</span><span class="lang-hi"><span class="theory-highlight">लाल दरवाजा मस्जिद:</span> सुल्तान महमूद शाह शर्की की बेगम बीबी राजी द्वारा <strong class="theory-highlight">1450</strong> में निर्मित; अपने लाल द्वार के लिए प्रसिद्ध।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Jhanjhari Masjid (झांझरी मस्जिद):</span> Built by Ibrahim Shah Sharqi in 1430; known for its delicate fine-cut stone tracery screens.</span><span class="lang-hi"><span class="theory-highlight">झांझरी मस्जिद:</span> इब्राहिम शाह शर्की द्वारा 1430 में निर्मित; बारीक जालीदार प्रस्तर नक्काशी हेतु विख्यात।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Shahi Pul / Munim Khan Bridge (शाही पुल, जौनपुर):</span> Built across Gomti river between <strong class="theory-highlight">1564-1568</strong> during Akbar's reign by governor Munim Khan. Designed by Afghan architect Afzal Ali; unique bridge featuring pillared kiosks (Gumtis) on both sides where merchants ran shops.</span><span class="lang-hi"><span class="theory-highlight">शाही पुल (मुनीम खां पुल, जौनपुर):</span> अकबर के काल में गवर्नर मुनीम खां द्वारा <strong class="theory-highlight">1564-1568</strong> में गोमती नदी पर निर्मित। अफगान वास्तुकार अफजल अली द्वारा डिजाइन; पुल के दोनों किनारों पर छतरियां (गुमटियां) बनी हैं जहां पहले दुकानें सजती थीं।</span></li>
  </ul>
</div>

<!-- Card 5: Mughal Imperial Architecture - Agra & Fatehpur Sikri -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Mughal Imperial Architecture: Agra &amp; Fatehpur Sikri</span>
    <span class="lang-hi">4. मुगल शाही वास्तुकला: आगरा एवं फतेहपुर सीकरी (UNESCO विश्व धरोहर स्थल)</span>
  </div>

  <h3 class="theory-heading">
    <span class="lang-en">A. Babur &amp; Akbar's Eras (बाबर एवं अकबर कालीन स्थापत्य)</span>
    <span class="lang-hi">क. बाबर एवं अकबर कालीन स्थापत्य</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Aram Bagh / Ram Bagh, Agra:</span> Built by Babur in <strong class="theory-highlight">1526</strong>. The <strong class="theory-highlight">oldest Mughal garden in India</strong>, laid out in the classical Persian *Charbagh* geometric quadrilateral water-channel pattern.</span><span class="lang-hi"><span class="theory-highlight">आराम बाग (राम बाग), आगरा:</span> बाबर द्वारा <strong class="theory-highlight">1526</strong> में निर्मित। भारत का <strong class="theory-highlight">सबसे पुराना जीवित मुगल उद्यान</strong>, जो चारबाग ज्यामितीय जलधारा पद्धति पर आधारित है।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Agra Fort (आगरा का किला):</span> Begun in <strong class="theory-highlight">1565</strong> by Akbar on the banks of Yamuna, built in massive red sandstone. UNESCO World Heritage Site (1983). Key structures inside: Jahangiri Mahal (Akbar's Hindu-Rajput style palace with Gujarati brackets), Akbari Mahal, Delhi Gate, Amar Singh Gate.</span><span class="lang-hi"><span class="theory-highlight">आगरा का किला:</span> अकबर द्वारा <strong class="theory-highlight">1565</strong> में यमुना किनारे लाल बलुआ पत्थर से निर्मित। 1983 में यूनेस्को विश्व धरोहर घोषित। प्रमुख महल: जहांगीरी महल (हिंदू-राजपूत शैली व गुजराती कोष्ठकों से युक्त), अकबरी महल, दिल्ली दरवाजा, अमर सिंह दरवाजा।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Fatehpur Sikri (फतेहपुर सीकरी):</span> Imperial capital planned and built by Akbar between <strong class="theory-highlight">1569-1585</strong> in red sandstone. UNESCO World Heritage Site (1986). Chief architect: Bahauddin.</span><span class="lang-hi"><span class="theory-highlight">फतेहपुर सीकरी:</span> अकबर द्वारा <strong class="theory-highlight">1569-1585</strong> के मध्य बसाई गई लाल बलुआ पत्थर की शाही राजधानी। 1986 में यूनेस्को विश्व धरोहर घोषित। प्रधान वास्तुकार: बहाउद्दीन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Buland Darwaza (बुलंद दरवाजा):</span> Rising to <strong class="theory-highlight">176 feet (53.5 m)</strong>, it is the <strong class="theory-highlight">highest gateway in the world</strong>. Erected by Akbar in <strong class="theory-highlight">1601-1602</strong> to commemorate his historic victory over <strong class="theory-highlight">Gujarat</strong>. Carries the famous Persian inscription quoting Jesus Christ: <em>"The world is a bridge, pass over it, but build no house upon it."</em></span><span class="lang-hi"><span class="theory-highlight">बुलंद दरवाजा:</span> <strong class="theory-highlight">176 फीट (53.5 मी)</strong> ऊंचा, <strong class="theory-highlight">विश्व का सबसे ऊंचा प्रवेश द्वार</strong>। अकबर द्वारा <strong class="theory-highlight">1601-1602</strong> में अपनी <strong class="theory-highlight">गुजरात विजय</strong> के उपलक्ष्य में निर्मित। इस पर ईसा मसीह का प्रसिद्ध कथन अंकित है: <em>"यह संसार एक पुल के समान है, इस पर से गुजरो परंतु इस पर घर मत बनाओ।"</em></span></li>
    <li><span class="lang-en"><span class="theory-highlight">Panch Mahal (पंचमहल, सीकरी):</span> 5-storey pyramidal pavilion resting on 176 intricately carved stone pillars (54 on ground floor decreasing to 4 on top). Designed on the lines of a Buddhist Vihara or Persian wind-tower (Badgir) for royal ladies.</span><span class="lang-hi"><span class="theory-highlight">पंचमहल, फतेहपुर सीकरी:</span> 5 मंजिला पिरामिडीय हवा महल जो 176 नक्काशीदार खंभों पर टिका है (भूतल पर 54, शीर्ष पर 4)। बौद्ध विहार की तर्ज पर रानियों के लिए ग्रीष्मकालीन विश्राम हेतु निर्मित।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Salim Chishti's Tomb (शेख सलीम चिश्ती की दरगाह):</span> Located in Jama Masjid courtyard, Sikri. Commissioned by Akbar in white marble; renowned for its hypnotic serpentine brackets and delicate perforated marble Jali screens.</span><span class="lang-hi"><span class="theory-highlight">शेख सलीम चिश्ती का मकबरा:</span> जामा मस्जिद प्रांगण, सीकरी। सफेद संगमरमर से निर्मित; बारीक संगमरमरी जालीदार खिड़कियों व सर्पिलाकार कोष्ठकों हेतु प्रसिद्ध।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Diwan-i-Khas &amp; Central Pillar (दीवान-ए-खास):</span> Features a world-famous single central pillar supporting a circular platform with 36 multi-tiered serpentine brackets resembling a blooming lotus flower.</span><span class="lang-hi"><span class="theory-highlight">दीवान-ए-खास का केंद्रीय स्तंभ:</span> 36 घुमावदार कोष्ठकों पर आधारित कमल के फूल सदृश अद्वितीय केंद्रीय प्रस्तर स्तंभ जिस पर बैठकर अकबर मंत्रियों से परामर्श करता था।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Allahabad Fort (प्रयागराज का किला):</span> Built by Akbar in <strong class="theory-highlight">1583</strong> at the confluence of Ganga, Yamuna, and Saraswati. Largest fort built by Akbar. Contains the Ashoka Pillar, Patalpuri underground temple, and the sacred <em>Akshaya Vat</em> (अक्षयवट tree).</span><span class="lang-hi"><span class="theory-highlight">प्रयागराज का किला:</span> अकबर द्वारा <strong class="theory-highlight">1583</strong> में संगम तट पर निर्मित। अकबर द्वारा निर्मित सबसे विशाल दुर्ग। इसमें अशोक स्तंभ, पातालपुरी मंदिर एवं अमर <em>अक्षयवट</em> स्थित है।</span></li>
  </ul>

  <h3 class="theory-heading">
    <span class="lang-en">B. Jahangir &amp; Shah Jahan's Masterpieces (ताजमहल एवं पितरा दुरा)</span>
    <span class="lang-hi">ख. जहांगीर व शाहजहाँ कालीन स्थापत्य: ताजमहल एवं पितरा दुरा</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Akbar's Tomb, Sikandra (Agra):</span> Begun by Akbar and completed by Jahangir in <strong class="theory-highlight">1613</strong>. 5 tiers combining red sandstone and marble; notable for the complete <strong class="theory-highlight">absence of a central dome</strong> (flat open-terrace design).</span><span class="lang-hi"><span class="theory-highlight">अकबर का मकबरा, सिकंदरा (आगरा):</span> निर्माण अकबर द्वारा शुरू, जहांगीर द्वारा <strong class="theory-highlight">1613</strong> में पूर्ण। 5 मंजिला संरचना; मुख्य विशेषता: <strong class="theory-highlight">गुंबद का पूर्ण अभाव</strong> (खुली सपाट संगमरमरी छत)।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Tomb of Itimad-ud-Daulah, Agra (एतमादुद्दौला का मकबरा):</span> Built between <strong class="theory-highlight">1622-1628</strong> by Empress <strong class="theory-highlight">Nur Jahan</strong> for her father Mirza Ghiyas Beg. Nicknamed <strong class="theory-highlight">"Baby Taj"</strong> and <strong class="theory-highlight">"Jewel Box"</strong>. It is the <strong class="theory-highlight">first Mughal building built entirely of white marble</strong> and marks the <strong class="theory-highlight">first extensive use of Pietra Dura (पितरा दुरा)</strong>—the inlay technique of inserting semi-precious colored gems into marble.</span><span class="lang-hi"><span class="theory-highlight">एतमादुद्दौला का मकबरा, आगरा:</span> नूरजहाँ द्वारा अपने पिता मिर्जा गियास बेग की स्मृति में <strong class="theory-highlight">1622-1628</strong> में निर्मित। इसे <strong class="theory-highlight">"बेबी ताज"</strong> या <strong class="theory-highlight">"श्रृंगारदान"</strong> कहते हैं। यह <strong class="theory-highlight">पूर्णतः सफेद संगमरमर से निर्मित पहली मुगल इमारत</strong> है तथा इसमें पहली बार व्यापक स्तर पर <strong class="theory-highlight">पितरा दुरा (Pietra Dura - पच्चीकारी)</strong> का प्रयोग किया गया।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">The Taj Mahal, Agra (ताजमहल):</span> Built by Emperor <strong class="theory-highlight">Shah Jahan</strong> between <strong class="theory-highlight">1631-1648</strong> (complex finished 1653) in memory of his beloved wife <strong class="theory-highlight">Mumtaz Mahal</strong> (Arjumand Banu Begum). UNESCO World Heritage Site (1983). Chief Architect: <strong class="theory-highlight">Ustad Ahmad Lahauri</strong> (conferred title <em>Nadir-ul-Asr</em>); Dome Designer: Ismail Khan; Chief Calligrapher: Amanat Khan Shirazi. Built of pristine Makrana white marble on a high riverfront plinth. Features 4 minarets tilted slightly outward (to prevent damage to dome in earthquakes), bulbous double dome, perfect bilateral symmetry, and exquisite pietra dura inlay.</span><span class="lang-hi"><span class="theory-highlight">ताजमहल, आगरा:</span> सम्राट <strong class="theory-highlight">शाहजहाँ</strong> द्वारा अपनी बेगम <strong class="theory-highlight">मुमताज महल</strong> की याद में <strong class="theory-highlight">1631-1648</strong> (परिसर पूर्ण 1653) में निर्मित। 1983 में यूनेस्को विश्व धरोहर। मुख्य वास्तुकार: <strong class="theory-highlight">उस्ताद अहमद लाहौरी</strong> (उपाधि: <em>नादिर-उल-अस्र</em>); गुंबद निर्माता: इस्माइल खां; सुलेखक: अमानत खां शिराजी। मकराना संगमरमर, चारों कोनों पर बाहर की ओर झुकी 4 मीनारें (भूकंप से मुख्य गुंबद की सुरक्षा हेतु), पूर्ण द्विपक्षीय सममिति एवं अद्भुत पितरा दुरा पच्चीकारी।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Moti Masjid (Agra Fort):</span> Built by Shah Jahan inside Agra Fort entirely of pure white marble; resembles a radiant pearl.</span><span class="lang-hi"><span class="theory-highlight">मोती मस्जिद (आगरा किला):</span> शाहजहाँ द्वारा आगरा किले में शुद्ध सफेद संगमरमर से निर्मित; चमकते मोती सदृश।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Jama Masjid, Agra:</span> Built in <strong class="theory-highlight">1648</strong> by Shah Jahan's eldest daughter <strong class="theory-highlight">Jahanara Begum</strong>.</span><span class="lang-hi"><span class="theory-highlight">जामा मस्जिद, आगरा:</span> शाहजहाँ की विदुषी पुत्री <strong class="theory-highlight">जहाँआरा बेगम</strong> द्वारा <strong class="theory-highlight">1648</strong> में निर्मित।</span></li>
  </ul>
</div>

<!-- Card 6: Awadh / Nawabi Architecture of Lucknow -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Awadh (Nawabi) Architecture of Lucknow (अवध की नवाबी स्थापत्य शैली)</span>
    <span class="lang-hi">5. अवध की नवाबी स्थापत्य कला (लखनऊ के ऐतिहासिक स्मारक)</span>
  </div>
  <p class="theory-para">
    <span class="lang-en">When Nawab Asaf-ud-Daula shifted the Awadh capital from Faizabad to Lucknow in 1775, a unique regional style developed. Due to a scarcity of local sandstone, Nawabi architecture used thin <strong class="theory-highlight">Lakhauri Bricks (लखौरी ईंटें)</strong> coated with fine lime-shell mortar stucco, decorated with relief scrollwork and the royal emblem of twin fish (<strong class="theory-highlight">Mahi-Maratib</strong>):</span>
    <span class="lang-hi">1775 में नवाब आसफउद्दौला द्वारा अवध की राजधानी फैजाबाद से लखनऊ स्थानांतरित करने के बाद नवाबी शैली का चरमोत्कर्ष हुआ। पत्थर की कमी के कारण इमारतों में पतली <strong class="theory-highlight">लखौरी ईंटों</strong>, सीप-चूने के प्लास्टर (स्टुको) और शाही प्रतीक <strong class="theory-highlight">मछली के जोड़े (माही मरातिब)</strong> का बहुतायत से प्रयोग हुआ:</span>
  </p>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Monument</span><span class="lang-hi">स्मारक</span></th>
        <th><span class="lang-en">Builder &amp; Year</span><span class="lang-hi">निर्माता एवं वर्ष</span></th>
        <th><span class="lang-en">Architectural Significance &amp; Exam Facts</span><span class="lang-hi">स्थापत्य महत्व एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Bara Imambara (बड़ा इमामबाड़ा / आसफी इमामबाड़ा)</strong></span><span class="lang-hi"><strong>बड़ा इमामबाड़ा (आसफी इमामबाड़ा)</strong></span></td>
        <td><span class="lang-en">Nawab <strong>Asaf-ud-Daula (1784)</strong>; Architect: <strong>Kifayatullah</strong>.</span><span class="lang-hi">नवाब <strong>आसफ-उद-दौला (1784)</strong>; वास्तुकार: <strong>किफायतउल्लाह</strong>।</span></td>
        <td><span class="lang-en">Built as famine relief work. Its central Asafi Hall (162 ft x 53 ft x 49 ft) is the <strong class="theory-highlight">largest vaulted hall in the world without any pillar or iron girder support</strong>. Contains the world-famous <strong class="theory-highlight">Bhul-Bhulaiya (भूल-भुलैया)</strong>—a 3D labyrinth of 489 identical doorways.</span><span class="lang-hi">अकाल राहत कार्य के रूप में निर्मित। इसका केंद्रीय हॉल <strong class="theory-highlight">बिना किसी खंभे या गर्डर के टिका विश्व का सबसे बड़ा हॉल</strong> है। छत के ऊपर प्रसिद्ध <strong class="theory-highlight">भूल-भुलैया</strong> (489 समान द्वारों का जटिल चक्रव्यूह) स्थित है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Rumi Darwaza (रूमी दरवाजा)</strong></span><span class="lang-hi"><strong>रूमी दरवाजा</strong></span></td>
        <td><span class="lang-en">Nawab <strong>Asaf-ud-Daula (1784)</strong>.</span><span class="lang-hi">नवाब <strong>आसफ-उद-दौला (1784)</strong>।</span></td>
        <td><span class="lang-en">Soaring <strong class="theory-highlight">60 feet high</strong> gateway. Modeled on the <em>Sublime Porte (Bab-i-Humayun)</em> of Constantinople (Istanbul, ancient Rome/Byzantium), hence named 'Rumi'. Known as the <em>Turkish Gate of Lucknow</em>.</span><span class="lang-hi">लगभग <strong class="theory-highlight">60 फीट ऊंचा</strong> भव्य प्रवेश द्वार। तुर्की (कांस्टेंटिनोपल/इस्तांबुल) के शाही प्रवेश द्वार की तर्ज पर निर्मित होने से 'रूमी' कहलाया। इसे <em>तुर्की गेट</em> भी कहते हैं।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Chhota Imambara (छोटा इमामबाड़ा / हुसैनाबाद)</strong></span><span class="lang-hi"><strong>छोटा इमामबाड़ा (हुसैनाबाद)</strong></span></td>
        <td><span class="lang-en">Nawab <strong>Muhammad Ali Shah (1838)</strong>.</span><span class="lang-hi">नवाब <strong>मुहम्मद अली शाह (1838)</strong>।</span></td>
        <td><span class="lang-en">Also called <em>Palace of Lights</em>. Gilded golden dome, ornate Arabic calligraphy, and magnificent Belgian glass chandeliers. Contains the tombs of Muhammad Ali Shah and his mother.</span><span class="lang-hi">इसे <em>रोशनी का महल</em> भी कहा जाता है। सोने का पानी चढ़ा गुंबद, सुंदर अरबी सुलेख और बेल्जियम के कांच के झूमर। इसमें मुहम्मद अली शाह का मकबरा है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Husainabad Clock Tower (घंटाघर, लखनऊ)</strong></span><span class="lang-hi"><strong>हुसैनाबाद घंटाघर (लखनऊ)</strong></span></td>
        <td><span class="lang-en">Built in <strong>1881</strong>; Designed by Roskell Payne.</span><span class="lang-hi">निर्माण: <strong>1881</strong>; वास्तुकार: रोस्केल पायने।</span></td>
        <td><span class="lang-en">Standing <strong class="theory-highlight">221 feet (67 meters)</strong>, it is the <strong class="theory-highlight">tallest clock tower in India</strong>. Built to mark the arrival of Sir George Couper, 1st Lt. Governor of United Provinces.</span><span class="lang-hi"><strong class="theory-highlight">221 फीट (67 मी)</strong> ऊंचा, यह <strong class="theory-highlight">भारत का सबसे ऊंचा घंटाघर</strong> है। संयुक्त प्रांत के पहले लेफ्टिनेंट गवर्नर जॉर्ज कूपर के आगमन पर निर्मित।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Chattar Manzil (छत्तर मंजिल)</strong></span><span class="lang-hi"><strong>छत्तर मंजिल</strong></span></td>
        <td><span class="lang-en">Begun by Saadat Ali Khan, finished by Nasir-ud-din Haider.</span><span class="lang-hi">सआदत अली खां द्वारा प्रारंभ, नसीरुद्दीन हैदर द्वारा पूर्ण।</span></td>
        <td><span class="lang-en">Named after the large gilded umbrella (Chattar) crowning the dome. Blend of Indo-Italian architecture on Gomti bank (housed CDRI for decades).</span><span class="lang-hi">गुंबद पर छत्र (अम्ब्रेला) लगा होने के कारण 'छत्तर मंजिल' नाम। गोमती तट पर इंडो-इटैलियन शैली का उत्कृष्ट महल (दशकों तक CDRI का मुख्यालय रहा)।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Qaiserbagh Palace Complex (कैसरबाग महल)</strong></span><span class="lang-hi"><strong>कैसरबाग महल परिसर</strong></span></td>
        <td><span class="lang-en">Nawab <strong>Wajid Ali Shah (1848-1852)</strong>.</span><span class="lang-hi">नवाब <strong>वाजिद अली शाह (1848-1852)</strong>।</span></td>
        <td><span class="lang-en">Grand quadrangle palace with white pavilions, Lakhi Phatak, and the Baradari where Wajid Ali Shah staged his famous Raas dances and musical soirees.</span><span class="lang-hi">सफेद संगमरमरी बारादरी, लखी फाटक युक्त विशाल महल जहां नवाब वाजिद अली शाह रासलीला व कथक नृत्यों का आयोजन करते थे।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 7: Colonial, Indo-Saracenic & Modern Architecture -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Colonial, Indo-Saracenic &amp; Modern Landmarks of UP</span>
    <span class="lang-hi">6. औपनिवेशिक, इंडो-सारसेनिक एवं आधुनिक वास्तुकला (ऐतिहासिक इमारतें)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Building / Landmark</span><span class="lang-hi">इमारत / ऐतिहासिक स्थल</span></th>
        <th><span class="lang-en">City &amp; Year</span><span class="lang-hi">शहर एवं वर्ष</span></th>
        <th><span class="lang-en">Architect &amp; Style</span><span class="lang-hi">वास्तुकार एवं शैली</span></th>
        <th><span class="lang-en">Key Exam Facts</span><span class="lang-hi">प्रमुख परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Charbagh Railway Station</strong></span><span class="lang-hi"><strong>चारबाग रेलवे स्टेशन</strong></span></td>
        <td><span class="lang-en">Lucknow (1914-1926)</span><span class="lang-hi">लखनऊ (1914-1926)</span></td>
        <td><span class="lang-en">J.H. Horniman; Indo-Saracenic.</span><span class="lang-hi">जे.एच. हॉर्नीमैन; इंडो-सारसेनिक।</span></td>
        <td><span class="lang-en">Aerial view resembles a <strong class="theory-highlight">Chessboard</strong> with turrets and domes appearing like chess pieces. Gandhiji and Jawaharlal Nehru met here for the first time on 26 Dec 1916.</span><span class="lang-hi">ऊपर (हवाई दृश्य) से देखने पर <strong class="theory-highlight">शतरंज के बोर्ड</strong> जैसा दिखता है। 26 दिसंबर 1916 को महात्मा गांधी व जवाहरलाल नेहरू की पहली मुलाकात इसी स्टेशन पर हुई थी।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>All Saints Cathedral (Patthar Girja)</strong></span><span class="lang-hi"><strong>ऑल सेंट्स कैथेड्रल (पत्थर गिरजा)</strong></span></td>
        <td><span class="lang-en">Prayagraj (1871-1887)</span><span class="lang-hi">प्रयागराज (1871-1887)</span></td>
        <td><span class="lang-en">Sir William Emerson; 13th Century Gothic Revival.</span><span class="lang-hi">सर विलियम एमर्सन; 13वीं सदी की गोथिक शैली।</span></td>
        <td><span class="lang-en">Designed by the architect of Kolkata's Victoria Memorial. Built of fine cream sandstone and red marble; stained glass rose windows.</span><span class="lang-hi">कोलकाता विक्टोरिया मेमोरियल के वास्तुकार विलियम एमर्सन द्वारा डिजाइन। लाल-क्रीम बलुआ पत्थर व रंगीन कांच की खिड़कियों से निर्मित।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Allahabad High Court Building</strong></span><span class="lang-hi"><strong>इलाहाबाद उच्च न्यायालय भवन</strong></span></td>
        <td><span class="lang-en">Prayagraj (1916)</span><span class="lang-hi">प्रयागराज (1916)</span></td>
        <td><span class="lang-en">Frank Lishman; Indo-Saracenic Classical.</span><span class="lang-hi">फ्रैंक लिशमैन; इंडो-सारसेनिक शास्त्रीय।</span></td>
        <td><span class="lang-en">Foundation laid in 1911 by Lord Minto, opened by Viceroy Lord Chelmsford in 1916. Features sweeping colonnades and sandstone portico.</span><span class="lang-hi">1911 में लॉर्ड मिंटो द्वारा शिलान्यास, 1916 में लॉर्ड चेम्सफोर्ड द्वारा उद्घाटन। भव्य प्रस्तर स्तंभों व बरामदों से सुसज्जित।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>The British Residency</strong></span><span class="lang-hi"><strong>ब्रिटिश रेजिडेंसी (लखनऊ)</strong></span></td>
        <td><span class="lang-en">Lucknow (1800)</span><span class="lang-hi">लखनऊ (1800)</span></td>
        <td><span class="lang-en">Nawab Saadat Ali Khan II; Colonial brick.</span><span class="lang-hi">नवाब सआदत अली खां द्वितीय; औपनिवेशिक ईंट।</span></td>
        <td><span class="lang-en">Epicenter of the 1857 Siege of Lucknow. Preserved exactly in its battle-scarred ruined state by ASI; national memorial of 1857 War of Independence.</span><span class="lang-hi">1857 के प्रथम स्वतंत्रता संग्राम में ऐतिहासिक घेराबंदी का केंद्र। तोपों के गोलों के निशानों सहित भग्नावशेष रूप में सुरक्षित राष्ट्रीय स्मारक।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Vidhan Sabha Building</strong></span><span class="lang-hi"><strong>उत्तर प्रदेश विधानसभा भवन</strong></span></td>
        <td><span class="lang-en">Lucknow (1922-1928)</span><span class="lang-hi">लखनऊ (1922-1928)</span></td>
        <td><span class="lang-en">Sir Swinton Jacob &amp; Heera Singh; Neo-Classical Awadhi.</span><span class="lang-hi">सर स्विंटन जैकब व हीरा सिंह; नव-शास्त्रीय अवधी।</span></td>
        <td><span class="lang-en">Inaugurated on 21 Feb 1928 by Governor Sir William Marris. Semi-circular building of Chunar sandstone crowned with a majestic central dome.</span><span class="lang-hi">21 फरवरी 1928 को गवर्नर सर विलियम मैरिस द्वारा उद्घाटित। चुनार बलुआ पत्थर से निर्मित अर्धवृत्ताकार भव्य गुंबददार भवन।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Shri Ram Janmabhoomi Mandir</strong></span><span class="lang-hi"><strong>श्री राम जन्मभूमि मंदिर (अयोध्या)</strong></span></td>
        <td><span class="lang-en">Ayodhya (Consecrated 22 Jan 2024)</span><span class="lang-hi">अयोध्या (प्राण प्रतिष्ठा 22 जनवरी 2024)</span></td>
        <td><span class="lang-en">Chandrakant Sompura; Traditional <strong class="theory-highlight">Nagara Style</strong>.</span><span class="lang-hi">चंद्रकांत सोमपुरा; पारंपरिक <strong class="theory-highlight">नागर शैली</strong>।</span></td>
        <td><span class="lang-en">3 storeys (height 161 feet), 392 pillars, 44 doors, 5 mandapas (Nritya, Rang, Sabha, Prarthana, Kirtan). Built entirely without iron or steel using carved pink sandstone from Bansi Paharpur (Rajasthan).</span><span class="lang-hi">3 मंजिला (ऊंचाई 161 फीट), 392 स्तंभ, 44 द्वार, 5 मंडप (नृत्य, रंग, सभा, प्रार्थना, कीर्तन)। बिना लोहे/स्टील के बंसी पहाड़पुर (राजस्थान) के नक्काशीदार गुलाबी पत्थरों से निर्मित।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 8: One-Liner Architecture Quick Revision Table -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Architecture One-Liner Quick Revision Matrix</span>
    <span class="lang-hi">7. उत्तर प्रदेश स्थापत्य कला: एक नज़र में त्वरित परीक्षा सार</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Historical Landmark / Architectural Question</span><span class="lang-hi">ऐतिहासिक स्मारक / स्थापत्य संबंधी प्रश्न</span></th>
        <th><span class="lang-en">Exact Answer &amp; Key Fact</span><span class="lang-hi">सटीक उत्तर एवं मुख्य तथ्य</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">First temple with a Shikhara in North India</span><span class="lang-hi">उत्तर भारत का पहला शिखरयुक्त मंदिर कौन सा है?</span></td>
        <td><span class="lang-en"><strong>Dashavatara Temple, Deogarh (Lalitpur)</strong></span><span class="lang-hi"><strong>दशावतार मंदिर, देवगढ़ (ललितपुर)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Oldest surviving brick and terracotta temple in India</span><span class="lang-hi">भारत का सबसे पुराना जीवित ईंट व टेराकोटा मंदिर</span></td>
        <td><span class="lang-en"><strong>Bhitargaon Temple, Kanpur Nagar (5th Century Gupta era)</strong></span><span class="lang-hi"><strong>भीतरगाँव मंदिर, कानपुर नगर (5वीं सदी गुप्त काल)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Site of Buddha's First Sermon Stupa</span><span class="lang-hi">भगवान बुद्ध के प्रथम उपदेश स्थल का स्तूप</span></td>
        <td><span class="lang-en"><strong>Dhamekh Stupa, Sarnath (Varanasi)</strong></span><span class="lang-hi"><strong>धमेख स्तूप, सारनाथ (वाराणसी)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Octagonal tower atop Chaukhandi Stupa commemorates</span><span class="lang-hi">चौखंडी स्तूप की अष्टकोणीय मीनार किसकी स्मृति में बनी?</span></td>
        <td><span class="lang-en"><strong>Visit of Mughal Emperor Humayun</strong> (built by Govardhan in 1588)</span><span class="lang-hi"><strong>मुगल सम्राट हुमायूँ के आगमन की स्मृति में</strong> (1588 में गोवर्धन द्वारा निर्मित)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Adoption date of Sarnath Lion Capital as National Emblem</span><span class="lang-hi">सारनाथ सिंह शीर्ष को राष्ट्रीय प्रतीक के रूप में कब अपनाया गया?</span></td>
        <td><span class="lang-en"><strong>26 January 1950</strong></span><span class="lang-hi"><strong>26 जनवरी 1950</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">City titled "Shiraz-e-Hind" (पूर्व का शिराज)</span><span class="lang-hi">"शीराज-ए-हिंद" की उपाधि किस शहर को प्राप्त थी?</span></td>
        <td><span class="lang-en"><strong>Jaunpur (जौनपुर)</strong></span><span class="lang-hi"><strong>जौनपुर</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Architectural hallmark of Sharqi style of Jaunpur</span><span class="lang-hi">जौनपुर की शर्की शैली की मुख्य पहचान</span></td>
        <td><span class="lang-en"><strong>Absence of minarets &amp; massive Propylons (sloping pylons)</strong></span><span class="lang-hi"><strong>मीनारों का अभाव एवं विशाल तोरणद्वार (प्रोपिलोन)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Builder and year of Atala Masjid, Jaunpur</span><span class="lang-hi">अटाला मस्जिद (जौनपुर) के निर्माता एवं वर्ष</span></td>
        <td><span class="lang-en"><strong>Sultan Ibrahim Shah Sharqi (1408)</strong></span><span class="lang-hi"><strong>सुल्तान इब्राहिम शाह शर्की (1408)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Oldest Mughal garden in India</span><span class="lang-hi">भारत का सबसे पुराना मुगल उद्यान</span></td>
        <td><span class="lang-en"><strong>Aram Bagh (Ram Bagh), Agra</strong> (built by Babur in 1526)</span><span class="lang-hi"><strong>आराम बाग (राम बाग), आगरा</strong> (बाबर द्वारा 1526 में निर्मित)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Buland Darwaza was built to commemorate victory over</span><span class="lang-hi">बुलंद दरवाजा किस विजय के उपलक्ष्य में बनाया गया?</span></td>
        <td><span class="lang-en"><strong>Akbar's Conquest of Gujarat (built 1601-1602, height 176 ft)</strong></span><span class="lang-hi"><strong>अकबर की गुजरात विजय</strong> (1601-1602 में निर्मित, ऊंचाई 176 फीट)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Panch Mahal at Fatehpur Sikri is inspired by</span><span class="lang-hi">फतेहपुर सीकरी का पंचमहल किस शैली से प्रेरित है?</span></td>
        <td><span class="lang-en"><strong>Buddhist Vihara design (5 storeys, 176 pillars)</strong></span><span class="lang-hi"><strong>बौद्ध विहार संरचना</strong> (5 मंजिला, 176 खंभे)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Mughal building lacking a dome</span><span class="lang-hi">कौन सा मुगल मकबरा बिना गुंबद का है?</span></td>
        <td><span class="lang-en"><strong>Akbar's Tomb at Sikandra, Agra (1613)</strong></span><span class="lang-hi"><strong>अकबर का मकबरा, सिकंदरा (आगरा)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">First Mughal building in pure white marble with Pietra Dura</span><span class="lang-hi">पितरा दुरा पच्चीकारी युक्त पूर्ण संगमरमरी पहली मुगल इमारत</span></td>
        <td><span class="lang-en"><strong>Tomb of Itimad-ud-Daulah, Agra</strong> (built by Nur Jahan, 1628)</span><span class="lang-hi"><strong>एतमादुद्दौला का मकबरा, आगरा</strong> (नूरजहाँ द्वारा 1628 में निर्मित)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Chief architect of the Taj Mahal</span><span class="lang-hi">ताजमहल के मुख्य वास्तुकार कौन थे?</span></td>
        <td><span class="lang-en"><strong>Ustad Ahmad Lahauri</strong> (title: Nadir-ul-Asr)</span><span class="lang-hi"><strong>उस्ताद अहमद लाहौरी</strong> (उपाधि: नादिर-उल-अस्र)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Builder and architect of Bara Imambara, Lucknow</span><span class="lang-hi">बड़ा इमामबाड़ा (लखनऊ) के निर्माता एवं वास्तुकार</span></td>
        <td><span class="lang-en"><strong>Nawab Asaf-ud-Daula (1784)</strong>; Architect: <strong>Kifayatullah</strong></span><span class="lang-hi"><strong>नवाब आसफ-उद-दौला (1784)</strong>; वास्तुकार: <strong>किफायतउल्लाह</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Rumi Darwaza model inspiration</span><span class="lang-hi">रूमी दरवाजा किस ऐतिहासिक द्वार से प्रेरित है?</span></td>
        <td><span class="lang-en"><strong>Sublime Porte (Bab-i-Humayun) of Constantinople (Istanbul)</strong></span><span class="lang-hi"><strong>कांस्टेंटिनोपल (इस्तांबुल) का सबलाइम पोर्टे (तुर्की द्वार)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Tallest clock tower in India</span><span class="lang-hi">भारत का सबसे ऊंचा घंटाघर</span></td>
        <td><span class="lang-en"><strong>Husainabad Clock Tower, Lucknow (221 feet / 67 meters)</strong></span><span class="lang-hi"><strong>हुसैनाबाद घंटाघर, लखनऊ (221 फीट / 67 मीटर)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Railway station resembling a chessboard from the air</span><span class="lang-hi">हवाई दृश्य से शतरंज सदृश दिखने वाला रेलवे स्टेशन</span></td>
        <td><span class="lang-en"><strong>Charbagh Railway Station, Lucknow</strong> (designed by J.H. Horniman)</span><span class="lang-hi"><strong>चारबाग रेलवे स्टेशन, लखनऊ</strong> (वास्तुकार: जे.एच. हॉर्नीमैन)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Architectural style of Ram Mandir, Ayodhya</span><span class="lang-hi">राम मंदिर (अयोध्या) की स्थापत्य शैली</span></td>
        <td><span class="lang-en"><strong>Traditional Nagara Style</strong> (Chief Architect: Chandrakant Sompura)</span><span class="lang-hi"><strong>पारंपरिक नागर शैली</strong> (मुख्य वास्तुकार: चंद्रकांत सोमपुरा)</span></td>
      </tr>
    </tbody>
  </table>
</div>

</div>
"""

def main():
    target_file = os.path.join("upsssc-up-gk", "architecture", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_architecture_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
