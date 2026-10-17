import os
import re

def build_heritage_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Archaeological, Architectural &amp; Cultural Heritage of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की पुरातात्विक, स्थापत्य एवं सांस्कृतिक धरोहर</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Heritage of Uttar Pradesh] --> B[UNESCO World Heritage Sites]
    A --> C[UNESCO Intangible Heritage]
    A --> D[Buddhist Circuit Heritage]
    A --> E[Ancient & Harappan Roots]
    A --> F[Medieval Awadh & Sharqi Splendors]
    A --> G[Bundelkhand Forts & Gupta Temples]
    A --> H[Heritage Arc & Institutions]

    B --> B1[Taj Mahal 1983: Shah Jahan & Lahauri]
    B --> B2[Agra Fort 1983: Akbar Red Sandstone 1565]
    B --> B3[Fatehpur Sikri 1986: Buland Darwaza 1601]

    C --> C1[Ramlila 2008: Ramnagar Varanasi Tradition]
    C --> C2[Vedic Chanting 2008: Oral Preservation]
    C --> C3[Kumbh Mela 2017: Triveni Sangam Prayagraj]

    D --> D1[Sarnath: 1st Sermon, Dhamekh & Ashoka Capital]
    D --> D2[Kushinagar: Mahaparinirvana 6.1m Statue]
    D --> D3[Shravasti: Jetavana | Sankisa: Elephant Capital]
    D --> D4[Piprahwa: Relic Casket | Kaushambi: Ghoshitarama]

    E --> E1[Alamgirpur: Meerut Easternmost Harappan]
    E --> E2[Sinauli: Baghpat Copper Chariots 2000 BCE]

    F --> F1[Awadh: Bara Imambara 1784 & Rumi Darwaza]
    F --> F2[Chhota Imambara 1838 & Clock Tower 221 ft]
    F --> F3[Sharqi Jaunpur: Atala Masjid 1408 & Shahi Pul]

    G --> G1[Kalinjar Banda: Neelkanth & Sher Shah 1545]
    G --> G2[Jhansi Fort: Bir Singh Deo & Rani Laxmi Bai]
    G --> G3[Deogarh Lalitpur: Dashavatara 1st Shikhara]

    H --> H1[Heritage Arc: Agra - Lucknow - Varanasi]
    H --> H2[State Archaeology Directorate 1951]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की ऐतिहासिक धरोहर] --> B[यूनेस्को विश्व धरोहर स्थल]
    A --> C[यूनेस्को अमूर्त सांस्कृतिक धरोहर]
    A --> D[बौद्ध सर्किट एवं प्रमुख स्तूप]
    A --> E[प्राचीन एवं हड़प्पा कालीन सभ्यता]
    A --> F[मध्यकालीन अवध एवं शर्की स्थापत्य]
    A --> G[बुंदेलखंड के दुर्ग एवं गुप्तकालीन मंदिर]
    A --> H[हेरिटेज आर्क एवं पुरातत्व निदेशालय]

    B --> B1[ताजमहल 1983: शाहजहाँ एवं उस्ताद लाहौरी]
    B --> B2[आगरा किला 1983: अकबर का लाल बलुआ पत्थर 1565]
    B --> B3[फतेहपुर सीकरी 1986: बुलंद दरवाजा 1601]

    C --> C1[रामलीला 2008: रामनगर वाराणसी परंपरा]
    C --> C2[वैदिक जप 2008: प्राचीन मौखिक परंपरा]
    C --> C3[कुंभ मेला 2017: त्रिवेणी संगम प्रयागराज]

    D --> D1[सारनाथ: प्रथम उपदेश, धमेख व सिंह शीर्ष]
    D --> D2[कुशीनगर: महापरिनिर्वाण 6.1 मी शयन प्रतिमा]
    D --> D3[श्रावस्ती: जेतवन | संकिसा: गज शीर्ष]
    D --> D4[पिपरहवा: अस्थि कलश | कौशाम्बी: घोषिताराम]

    E --> E1[आलमगीरपुर: मेरठ पूर्वी हड़प्पा स्थल]
    E --> E2[सिनौली: बागपत ताम्र रथ व योद्धा समाधियां]

    F --> F1[अवध: बड़ा इमामबाड़ा 1784 व रूमी दरवाजा]
    F --> F2[छोटा इमामबाड़ा 1838 व क्लॉक टॉवर 221 फीट]
    F --> F3[शर्की जौनपुर: अटाला मस्जिद 1408 व शाही पुल]

    G --> G1[कालिंजर बांदा: नीलकंठ व शेरशाह मृत्यु 1545]
    G --> G2[झांसी दुर्ग: बीर सिंह देव व रानी लक्ष्मीबाई]
    G --> G3[देवगढ़ ललितपुर: दशावतार प्रथम शिखर मंदिर]

    H --> H1[हेरिटेज आर्क: आगरा - लखनऊ - वाराणसी]
    H --> H2[राज्य पुरातत्व निदेशालय 1951]
    </div>
  </div>
</div>

<!-- Card 2: UNESCO Tangible & Intangible Heritage -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. UNESCO World Heritage Sites (Tangible &amp; Intangible)</span>
    <span class="lang-hi">1. यूनेस्को विश्व धरोहर स्थल (मूर्त एवं अमूर्त सांस्कृतिक विरासत)</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Three UNESCO Tangible Cultural Heritage Sites in UP:</strong>
        <br/>• <strong>1. Taj Mahal, Agra (Inscribed 1983):</strong> Commissioned in 1631 by Mughal Emperor Shah Jahan in memory of Mumtaz Mahal; completed in 1648/1653. Chief architect was <strong>Ustad Ahmad Lahauri</strong>. Built of pristine white Makrana marble on a raised sandstone plinth along the Yamuna river, featuring exquisite <strong>Pietra Dura (Parchin Kari)</strong> floral inlay work.
        <br/>• <strong>2. Agra Fort, Agra (Inscribed 1983):</strong> Constructed by Emperor <strong>Akbar between 1565 and 1573</strong> in red sandstone on the ruins of the ancient Lodi/Badalgarh fort. Later adorned with white marble pavilions by Shah Jahan. Houses architectural gems: Jahangiri Mahal, Diwan-i-Aam, Diwan-i-Khas, Moti Masjid, Sheesh Mahal, and Musamman Burj (where Shah Jahan was held captive).
        <br/>• <strong>3. Fatehpur Sikri, Agra (Inscribed 1986):</strong> Founded in <strong>1571 by Akbar</strong> as the imperial capital in honor of Sufi saint Sheikh Salim Chishti. Encompasses the monumental <strong>Buland Darwaza (54 meters high, built in 1601 to commemorate the conquest of Gujarat)</strong>, the white-marble Tomb of Salim Chishti (famous for mother-of-pearl jali screens), Panch Mahal (5-storey pyramidal pavilion), Jodha Bai's Palace, Ibadat Khana (1575), and Jama Masjid.
      </span>
      <span class="lang-hi"><strong>उ.प्र. के तीन यूनेस्को मूर्त विश्व धरोहर स्थल:</strong>
        <br/>• <strong>1. ताजमहल, आगरा (1983 में शामिल):</strong> मुगल सम्राट शाहजहाँ द्वारा मुमताज महल की स्मृति में 1631 में प्रारंभ तथा 1648/1653 में पूर्ण। मुख्य वास्तुकार: <strong>उस्ताद अहमद लाहौरी</strong>। मकराना के श्वेत संगमरमर से निर्मित एवं <strong>पिएत्रा ड्यूरा (पच्चीकारी)</strong> से सुसज्जित।
        <br/>• <strong>2. आगरा का किला (1983 में शामिल):</strong> सम्राट <strong>अकबर द्वारा 1565 से 1573 के मध्य</strong> लाल बलुआ पत्थर से प्राचीन बादलगढ़ के स्थान पर निर्मित। जहांगीरी महल, दीवान-ए-आम, दीवान-ए-खास, मोती मस्जिद, शीश महल तथा मुसम्मन बुर्ज (जहाँ शाहजहाँ को नजरबंद रखा गया था) प्रमुख आकर्षण हैं।
        <br/>• <strong>3. फतेहपुर सीकरी (1986 में शामिल):</strong> सूफी संत शेख सलीम चिश्ती के सम्मान में <strong>अकबर द्वारा 1571 में बसाई गई राजधानी</strong>। इसमें <strong>बुलंद दरवाजा (54 मीटर ऊंचा, 1601 में गुजरात विजय के उपलक्ष्य में निर्मित)</strong>, सलीम चिश्ती का मकबरा (संगमरमर की बारीक जालियां), पंचमहल (5 मंजिला पिरामिड नुमा हवा महल), जोधाबाई महल, इबादत खाना व जामा मस्जिद स्थित हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>UNESCO Intangible Cultural Heritage of Humanity (ICH):</strong>
        <br/>• <strong>1. Ramlila of Ramnagar, Varanasi (Inscribed 2008):</strong> World-renowned 31-day cyclical open-air enactment of the Ramcharitmanas without microphones, utilizing an entire town as an active stage.
        <br/>• <strong>2. Tradition of Vedic Chanting (Inscribed 2008):</strong> Ancient unbroken oral transmission of the four Vedas, rigorously preserved by Vedic schools (Gurukuls) across Varanasi.
        <br/>• <strong>3. Kumbh Mela, Prayagraj (Inscribed 2017):</strong> World's largest peaceful religious gathering celebrated at the Triveni Sangam, exemplifying universal brotherhood and spiritual purification.
      </span>
      <span class="lang-hi"><strong>यूनेस्को की मानवता की अमूर्त सांस्कृतिक विरासत (ICH):</strong>
        <br/>• <strong>1. रामनगर (वाराणसी) की रामलीला (2008):</strong> संपूर्ण नगर को खुले रंगमंच में बदलकर 31 दिनों तक बिना माइक के होने वाला ऐतिहासिक रामकथा मंचन।
        <br/>• <strong>2. वैदिक जप की परंपरा (2008):</strong> वेदों की प्राचीन मौखिक गायन परंपरा, जिसे वाराणसी के वेद विद्यालयों ने अक्षुण्ण रखा है।
        <br/>• <strong>3. कुंभ मेला, प्रयागराज (2017):</strong> त्रिवेणी संगम पर आयोजित विश्व का सबसे बड़ा शांतिपूर्ण जन समागम, जो आत्म-शुद्धि व समरसता का प्रतीक है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>UNESCO Tentative List from UP:</strong> Includes the <em>Ghats of Varanasi</em> (84 riverfront stone ghats along the Ganga) and the <em>Iconic Monuments of Sarnath</em> (Dhamekh &amp; Chaukhandi Stupas).</span>
      <span class="lang-hi"><strong>यूनेस्को की संभावित (Tentative) सूची में शामिल स्थल:</strong> <em>वाराणसी के गंगा घाट</em> (84 पक्के घाट) तथा <em>सारनाथ के बौद्ध स्मारक</em> (धमेख व चौखंडी स्तूप)।</span>
    </li>
  </ul>
</div>

<!-- Card 3: Buddhist Circuit Heritage Sites -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. The Buddhist Circuit: Sacred Stupas &amp; Monastic Heritage</span>
    <span class="lang-hi">2. बौद्ध सर्किट: पावन स्तूप, विहार एवं महापरिनिर्वाण विरासत</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Sarnath (Isipatana / Mrigadava, Varanasi):</strong>
        <br/>• <strong>Dharmachakrapravartana:</strong> Site where Gautama Buddha delivered his <strong>First Sermon (धम्मचक्कपवत्तन)</strong> to five ascetic companions (Kaundinya and group) after enlightenment.
        <br/>• <strong>Dhamekh Stupa:</strong> Massive cylindrical brick stupa (height 43.6 meters, diameter 28 meters) built in 500 CE during the Gupta era over an earlier Ashokan foundation; adorned with intricate Gupta geometric and floral carvings.
        <br/>• <strong>Chaukhandi Stupa:</strong> Terraced brick monument marking the spot where Buddha met his 5 disciples; features an octagonal Islamic tower erected by Govardhan in 1588 to commemorate Mughal Emperor Humayun's visit.
        <br/>• <strong>Ashoka Lion Capital:</strong> Polished Chunar sandstone pillar erected by Emperor Ashoka (250 BCE); features four Asiatic lions standing back-to-back, adopted on <strong>January 26, 1950, as India's National Emblem</strong>.
      </span>
      <span class="lang-hi"><strong>सारनाथ (ऋषिपतन / मृगदाव, वाराणसी):</strong>
        <br/>• <strong>धर्मचक्रप्रवर्तन:</strong> ज्ञान प्राप्ति के पश्चात भगवान बुद्ध द्वारा पांच शिष्यों (पंचवर्गीय भिक्षुओं) को दिया गया <strong>प्रथम उपदेश स्थल</strong>।
        <br/>• <strong>धमेख स्तूप:</strong> 500 ई. में गुप्त काल में निर्मित विशाल बेलनाकार ईंट स्तूप (ऊंचाई 43.6 मीटर); गुप्तकालीन नक्काशीदार ज्यामितीय व पुष्प आकृतियों से सुसज्जित।
        <br/>• <strong>चौखंडी स्तूप:</strong> वह स्थान जहाँ बुद्ध अपने पांच शिष्यों से मिले थे; इसके शीर्ष पर 1588 में गोवर्धन द्वारा मुगल बादशाह हुमायूं की यात्रा की स्मृति में एक अष्टकोणीय बुर्ज बनाया गया।
        <br/>• <strong>अशोक का सिंह शीर्ष स्तंभ:</strong> चुनार के बलुआ पत्थर पर उत्कीर्ण; <strong>26 जनवरी 1950 को भारत के राष्ट्रीय प्रतीक</strong> के रूप में अंगीकृत।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Kushinagar (Kusinara):</strong>
        <br/>• <strong>Mahaparinirvana:</strong> Site where Lord Buddha attained final salvation (Mahaparinirvana) in 483 BCE at the age of 80 under twin Sal trees on the banks of Hiranyavati river.
        <br/>• <strong>Mahaparinirvana Temple:</strong> Houses a monolithic <strong>6.1-meter-long reclining red-sandstone Buddha statue</strong> in dying posture, excavated by Carlleyle in 1876 (dating to Gupta era 5th century CE, carved by Dinna of Mathura).
        <br/>• <strong>Ramabhar Stupa (Mukutabandhana Chaitya):</strong> Massive brick stupa marking the holy spot of Buddha's cremation and division of sacred bone relics among 8 clans.
      </span>
      <span class="lang-hi"><strong>कुशीनगर (कुशीनारा):</strong>
        <br/>• <strong>महापरिनिर्वाण:</strong> हिरण्यवती नदी तट पर शाल वृक्षों के नीचे 80 वर्ष की आयु में 483 ई.पू. में बुद्ध का देहत्याग (महापरिनिर्वाण)।
        <br/>• <strong>महापरिनिर्वाण मंदिर:</strong> 5वीं सदी (गुप्त काल) की <strong>6.1 मीटर लंबी लेटी हुई लाल बलुआ पत्थर की बुद्ध प्रतिमा</strong> (मथुरा के मूर्तिकार दिन्ना द्वारा निर्मित, 1876 में कार्लाईल द्वारा खोजी गई)।
        <br/>• <strong>रामाभार स्तूप (मुकुटबंधन चैत्य):</strong> वह पावन स्थान जहाँ भगवान बुद्ध का अंतिम संस्कार हुआ था तथा उनकी अस्थि धातुओं का 8 गणराज्यों में विभाजन हुआ था।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Shravasti (Sahet-Mahet):</strong> Capital of ancient Kosala Mahajanapada; Buddha spent <strong>24 monsoon retreats (Varshavas)</strong> here. Features the <strong>Jetavana Monastery</strong> (donated by merchant Anathapindika), Anandabodhi Tree, and Angulimala's Stupa.</span>
      <span class="lang-hi"><strong>श्रावस्ती (सहेत-महेत):</strong> प्राचीन कोशल महाजनपद की राजधानी; बुद्ध ने अपने जीवन के <strong>सर्वाधिक 24 वर्षावास</strong> यहीं व्यतीत किए। श्रेष्ठी अनाथपिंडक द्वारा समर्पित <strong>जेतवन विहार</strong>, आनंदबोधि वृक्ष तथा अंगुलिमाल स्तूप।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Piprahwa / Ganwaria (Siddharthnagar):</strong> Identified as ancient <strong>Kapilavastu</strong>, the capital of the Shakya republic where Prince Siddhartha spent his youth. Famous for the 1898 excavation of the <strong>Piprahwa inscribed soapstone casket</strong> containing authentic Buddha bone relics.</span>
      <span class="lang-hi"><strong>पिपरहवा / गनवरिया (सिद्धार्थनगर):</strong> प्राचीन <strong>कपिलवस्तु</strong> के रूप में चिन्हित; शाक्य गणराज्य की राजधानी जहाँ सिद्धार्थ का बाल्यकाल बीता। 1898 में यहां से बुद्ध की मूल अस्थि धातुओं से युक्त अभिलेखित प्रस्तर मंजूषा प्राप्त हुई।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Sankisa (Farrukhabad):</strong> Venerated as the site where Buddha miraculously descended from Trayastrimsa Heaven back to earth accompanied by Brahma and Indra; marked by an Ashokan polished stone <strong>Elephant Capital (गज शीर्ष)</strong>.</span>
      <span class="lang-hi"><strong>संकिसा (फर्रुखाबाद):</strong> पौराणिक मान्यतानुसार भगवान बुद्ध का देवलोक (त्रायस्त्रिंश स्वर्ग) से पृथ्वी पर अवतरण स्थल; सम्राट अशोक का चुनार बलुआ पत्थर से निर्मित <strong>हाथी शीर्ष (गज स्तंभ)</strong> यहाँ स्थापित है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kaushambi (Kosam):</strong> Capital of ancient Vatsa Mahajanapada under King Udayana; home to the historic <strong>Ghoshitarama Monastery</strong> where Buddha stayed and preached.</span>
      <span class="lang-hi"><strong>कौशाम्बी (कोसम):</strong> राजा उदयन के वत्स महाजनपद की राजधानी; प्रसिद्ध <strong>घोषिताराम विहार</strong> जहाँ बुद्ध ने कई प्रवचन दिए।</span>
    </li>
  </ul>
</div>

<!-- Card 4: Ancient Harappan & Classical Gupta Temple Heritage -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Harappan Horizons &amp; Classical Gupta Temple Architecture</span>
    <span class="lang-hi">3. सिंधु-हड़प्पा सभ्यता एवं शास्त्रीय गुप्तकालीन मंदिर स्थापत्य</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Eastern Harappan Frontiers:</strong>
        <br/>• <strong>Alamgirpur (Meerut):</strong> Located along the Hindon River; represents the <strong>easternmost boundary of the Mature Indus Valley Civilization</strong>, excavated by Y.D. Sharma in 1958.
        <br/>• <strong>Sinauli (Baghpat):</strong> Globally celebrated necropolis dating to 2000-1800 BCE (Late Harappan / Copper Hoard transition); yielded <strong>India's first solid-disk copper chariots</strong>, copper antenna swords, warrior helmets, and royal anthropomorphic coffins.
        <br/>• <strong>Hulas (Saharanpur) &amp; Mandi (Muzaffarnagar):</strong> Crucial proto-historic settlements revealing Harappan pottery and gold treasure hoards.
      </span>
      <span class="lang-hi"><strong>हड़प्पा सभ्यता के पूर्वी सीमांत:</strong>
        <br/>• <strong>आलमगीरपुर (मेरठ):</strong> हिंडन नदी तट पर स्थित; <strong>हड़प्पा सभ्यता का सबसे पूर्वी स्थल</strong> (1958 में वाई.डी. शर्मा द्वारा उत्खनित)।
        <br/>• <strong>सिनौली (बागपत):</strong> 2000-1800 ई.पू. का ऐतिहासिक शवाधान स्थल; यहाँ से <strong>भारत के प्रथम तांबे से मढ़े ठोस पहियों वाले रथ</strong>, तांबे की तलवारें, योद्धा शिरस्त्राण (हेलमेट) तथा शाही ताबूत प्राप्त हुए।
        <br/>• <strong>हुलास (सहारनपुर) व मांडी (मुजफ्फरनगर):</strong> उत्तर-हड़प्पा कालीन बस्तियां एवं स्वर्ण मुद्रा भंडार।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Gupta Golden Age Temples (5th-6th Century CE):</strong>
        <br/>• <strong>Dashavatara Temple, Deogarh (Lalitpur):</strong> The <strong>earliest surviving temple in India featuring a stone Shikhara (spire)</strong> and a formal <em>Panchayatana layout</em> (central sanctum surrounded by four subsidiary shrines). Celebrated for its masterly high-relief sculpted panels of <strong>Sheshashayi Vishnu (Narayana reclining on Ananta Shesha)</strong>, Gajendramoksha, and Nara-Narayana.
        <br/>• <strong>Bhitargaon Temple (Kanpur Nagar):</strong> The <strong>oldest surviving complete Terracotta &amp; Brick temple in India</strong> (5th century CE). Features a stepped pyramidal shikhara and the earliest true structural arch (Voli) in Indian temple architecture.
        <br/>• <strong>Bhitari Monolithic Pillar (Ghazipur):</strong> Commemorates Gupta Emperor Skandagupta's historic military triumph repelling the ferocious Huna invasions.
      </span>
      <span class="lang-hi"><strong>गुप्तकालीन स्वर्णिम मंदिर (5वीं-6वीं सदी):</strong>
        <br/>• <strong>दशावतार मंदिर, देवगढ़ (ललितपुर):</strong> भारत का <strong>पहला पत्थर का शिखरयुक्त मंदिर</strong> तथा प्रथम <em>पंचायतन शैली</em> का मंदिर। शेषशायी विष्णु (अनंतनाग पर शयन), गजेंद्रमोक्ष व नर-नारायण के अद्वितीय मूर्तिकला पैनल।
        <br/>• <strong>भीतरगांव मंदिर (कानपुर नगर):</strong> भारत में ईंटों व पकी मिट्टी (टेराकोटा) से निर्मित <strong>सबसे प्राचीन जीवित हिंदू मंदिर</strong> (5वीं सदी); इसमें भारतीय स्थापत्य में पहली बार यथार्थ मेहराब (True Arch) का प्रयोग मिलता है।
        <br/>• <strong>भीतरी स्तंभ लेख (गाजीपुर):</strong> गुप्त सम्राट स्कंदगुप्त द्वारा बर्बर हूण आक्रमणकारियों को पराजित करने का ऐतिहासिक अभिलेख।
      </span>
    </li>
  </ul>
</div>

<!-- Card 5: Medieval Architectural Splendors: Sharqi & Awadh Nawabi -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Medieval Splendors: Sharqi Architecture &amp; Awadh Nawabi Heritage</span>
    <span class="lang-hi">4. मध्यकालीन वैभव: जौनपुर शर्की शैली एवं अवध नवाबी स्थापत्य</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Jaunpur Sharqi Architecture ('Shiraz-e-Hind'):</strong>
        <br/>• Founded in 1359 by Feroz Shah Tughlaq in memory of his cousin Muhammad bin Tughlaq (Jauna Khan). Later blossomed into the independent Sharqi Sultanate (1394-1479).
        <br/>• <strong>Atala Masjid, Jaunpur (Completed 1408):</strong> Built by Sultan Ibrahim Shah Sharqi on the foundations of an ancient temple; pioneering monument of Sharqi style characterized by <strong>monumental battered pylons (propylons), imposing arched screens, and complete absence of traditional slender minarets</strong>.
        <br/>• <strong>Shahi Pul (Akbar's Bridge):</strong> Iconic 16-arch stone bridge spanning the Gomti river, built in 1568 by Afghan architect Afzal Ali under the patronage of Mughal governor Munim Khan.
      </span>
      <span class="lang-hi"><strong>जौनपुर की शर्की स्थापत्य शैली ('शीराज-ए-हिंद'):</strong>
        <br/>• 1359 में फिरोज शाह तुगलक द्वारा जौना खां (मुहम्मद बिन तुगलक) की याद में बसाया गया।
        <br/>• <strong>अटाला मस्जिद, जौनपुर (1408 में पूर्ण):</strong> सुल्तान इब्राहिम शाह शर्की द्वारा निर्मित; शर्की शैली का उत्कृष्ट नमूना जिसमें <strong>विशाल तोरण द्वार (प्रोपिलॉन), मेहराबी स्क्रीन तथा मीनारों का पूर्ण अभाव</strong> प्रमुख विशेषता है।
        <br/>• <strong>शाही पुल:</strong> गोमती नदी पर 16 मेहराबों वाला पत्थर का ऐतिहासिक पुल, जिसे 1568 में अकबर के सूबेदार मुनीम खां ने अफगान वास्तुकार अफजल अली से बनवाया था।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Awadh Nawabi Architecture (Lucknow):</strong>
        <br/>• <strong>Bara Imambara (Asafi Imambara, 1784):</strong> Commissioned by Nawab Asaf-ud-Daula as a famine relief project; designed by architect <strong>Kifayatullah</strong>. Features the world's largest vaulted central hall (50m x 16m x 15m) constructed without a single interior pillar or wooden beam. Houses the complex multi-level labyrinth <strong>Bhul-Bhulaiya</strong> and a five-storey Shahi Baoli (stepwell).
        <br/>• <strong>Rumi Darwaza (1784):</strong> 60-foot monumental portal standing adjacent to Bara Imambara; modeled upon the ancient Sub-lime Porte of Constantinople (Istanbul), often lauded as the <em>Turkish Gate</em> of Lucknow.
        <br/>• <strong>Chhota Imambara (Husainabad Imambara, 1838):</strong> Built by Nawab Muhammad Ali Shah; famed as the <em>Palace of Lights</em> for its Belgian chandeliers, gilded dome, and calligraphic relief.
        <br/>• <strong>Husainabad Clock Tower (1881):</strong> 221-foot Victorian Gothic clock tower; the <strong>tallest clock tower in India</strong>, designed by Roskell Payne.
      </span>
      <span class="lang-hi"><strong>अवध का नवाबी स्थापत्य (लखनऊ):</strong>
        <br/>• <strong>बड़ा इमामबाड़ा (आसफी इमामबाड़ा, 1784):</strong> नवाब आसफ-उद-दौला द्वारा अकाल राहत कार्य के रूप में निर्मित; वास्तुकार <strong>किफायतउल्लाह</strong>। बिना किसी खंभे या गर्डर के 50 मीटर लंबा विश्व का सबसे बड़ा मेहराबदार हॉल। इसमें प्रसिद्ध <strong>भूल-भुलैया</strong> तथा पंचमंजिला शाही बावली स्थित है।
        <br/>• <strong>रूमी दरवाजा (1784):</strong> 60 फीट ऊंचा भव्य मेहराबी प्रवेश द्वार; तुर्की के इस्तांबुल (कांस्टेंटिनोपल) के प्रवेश द्वार की तर्ज पर निर्मित होने के कारण इसे 'तुर्किश गेट' भी कहते हैं।
        <br/>• <strong>छोटा इमामबाड़ा (हुसैनाबाद इमामबाड़ा, 1838):</strong> नवाब मुहम्मद अली शाह द्वारा निर्मित; बेल्जियम के झूमरों व सोने के पानी चढ़े गुंबद के कारण <em>'पैलेस ऑफ लाइट्स'</em> कहलाता है।
        <br/>• <strong>हुसैनाबाद क्लॉक टॉवर (1881):</strong> 221 फीट ऊंचा विक्टोरियन गोथिक घंटाघर; <strong>भारत का सबसे ऊंचा क्लॉक टॉवर</strong>।
      </span>
    </li>
  </ul>
</div>

<!-- Card 6: Bundelkhand Forts & Ancient Hill Fortresses -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Fortresses of Valor: Kalinjar &amp; Jhansi</span>
    <span class="lang-hi">5. शौर्य के दुर्ग: कालिंजर एवं झांसी के ऐतिहासिक किले</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Kalinjar Fort (Banda District):</strong>
        <br/>• Perched on an isolated Vindhyan hill at 1,203 feet; historically celebrated as one of India's most impregnable fortresses, held successively by Chandela kings and Bundela warriors.
        <br/>• <strong>Historical Event:</strong> Afghan monarch <strong>Sher Shah Suri met his death here in May 1545</strong> due to an accidental explosion of a gunpowder shell ('Ukka') during the siege of Kalinjar.
        <br/>• <strong>Neelkanth Mahadev Temple:</strong> Ancient cave temple inside the fort where Lord Shiva is believed to have rested after consuming the poison (Halahala) during Samudra Manthan; features an 18-armed colossal Bhairava relief sculpture.
      </span>
      <span class="lang-hi"><strong>कालिंजर दुर्ग (बांदा जिला):</strong>
        <br/>• विंध्य पर्वतमाला पर 1,203 फीट की ऊंचाई पर स्थित; भारत के सबसे अभेद्य किलों में से एक, जिस पर चंदेलों और बुंदेलों का आधिपत्य रहा।
        <br/>• <strong>ऐतिहासिक घटना:</strong> मई 1545 में कालिंजर घेराबंदी के दौरान तोप का गोला ('उक्का') फटने से अफगान सुल्तान <strong>शेरशाह सूरी की मृत्यु</strong> इसी दुर्ग की दीवारों के समक्ष हुई थी।
        <br/>• <strong>नीलकंठ महादेव मंदिर:</strong> दुर्ग के भीतर स्थित प्राचीन गुफा मंदिर जहाँ समुद्र मंथन का विषपान करने के बाद शिव ने विश्राम किया था; यहाँ 18 भुजाओं वाली विशाल काल-भैरव प्रतिमा स्थित है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Jhansi Fort (Jhansi District):</strong>
        <br/>• Erected atop Bangira Hill in <strong>1613 by Orchha ruler Raja Bir Singh Ju Deo</strong>.
        <br/>• Symbol of 1857 First War of Independence under the valiant leadership of <strong>Rani Lakshmibai</strong>.
        <br/>• Houses the historic <strong>Kadak Bijli and Bhavani Shankar cannons</strong>, Ganesh Mandir, and the steep ramparts from which Rani Lakshmibai leaped with her adopted son Damodar Rao on horseback (Badal).
      </span>
      <span class="lang-hi"><strong>झांसी का किला (झांसी जिला):</strong>
        <br/>• <strong>1613 में ओरछा शासक राजा बीर सिंह जू देव</strong> द्वारा बंगिरा पहाड़ी पर निर्मित।
        <br/>• 1857 के प्रथम स्वतंत्रता संग्राम में <strong>रानी लक्ष्मीबाई</strong> की अदम्य वीरता का अमर प्रतीक।
        <br/>• किले में ऐतिहासिक <strong>कड़क बिजली एवं भवानी शंकर तोपें</strong>, गणेश मंदिर तथा वह बुर्ज स्थित है जहां से रानी अपने दत्तक पुत्र दामोदर राव को पीठ पर बांधकर घोड़े (बादल) सहित कूदी थीं।
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Fact Matrix: UP Heritage (Direct Exam Points)</span>
    <span class="lang-hi">6. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. की धरोहर (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Heritage Site</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / धरोहर स्थल</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">How many tangible UNESCO World Heritage Sites are there in UP?</span><span class="lang-hi">उत्तर प्रदेश में कुल कितने मूर्त यूनेस्को विश्व धरोहर स्थल हैं?</span></td>
          <td><span class="lang-en"><strong>3 Sites:</strong> Taj Mahal (1983), Agra Fort (1983), Fatehpur Sikri (1986)</span><span class="lang-hi"><strong>3 स्थल:</strong> ताजमहल (1983), आगरा किला (1983), फतेहपुर सीकरी (1986)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which elements from UP are in UNESCO's Intangible Heritage list?</span><span class="lang-hi">उ.प्र. की कौन सी परंपराएं यूनेस्को अमूर्त सांस्कृतिक धरोहर में शामिल हैं?</span></td>
          <td><span class="lang-en"><strong>Ramlila (2008), Vedic Chanting (2008), and Kumbh Mela (2017)</strong></span><span class="lang-hi"><strong>रामलीला (2008), वैदिक जप (2008) एवं कुंभ मेला (2017)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Who was the chief architect of the Taj Mahal?</span><span class="lang-hi">ताजमहल का मुख्य वास्तुकार कौन था?</span></td>
          <td><span class="lang-en"><strong>Ustad Ahmad Lahauri</strong> (उस्ताद अहमद लाहौरी)</span><span class="lang-hi"><strong>उस्ताद अहमद लाहौरी</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which year was Buland Darwaza built and to commemorate what?</span><span class="lang-hi">बुलंद दरवाजा किस वर्ष और किस विजय के उपलक्ष्य में बनाया गया था?</span></td>
          <td><span class="lang-en"><strong>1601 CE</strong>, to commemorate Akbar's conquest of <strong>Gujarat</strong></span><span class="lang-hi"><strong>1601 ई.</strong>, अकबर की <strong>गुजरात विजय</strong> के उपलक्ष्य में</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where did Gautama Buddha deliver his First Sermon (Dharmachakrapravartana)?</span><span class="lang-hi">भगवान बुद्ध ने अपना प्रथम उपदेश (धर्मचक्रप्रवर्तन) कहाँ दिया था?</span></td>
          <td><span class="lang-en"><strong>Sarnath (Isipatana/Mrigadava, Varanasi)</strong></span><span class="lang-hi"><strong>सारनाथ (ऋषिपतन/मृगदाव, वाराणसी)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Dhamekh Stupa located?</span><span class="lang-hi">धमेख स्तूप कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Sarnath, Varanasi</strong> (built during Gupta era, 500 CE)</span><span class="lang-hi"><strong>सारनाथ, वाराणसी</strong> (गुप्त काल 500 ई. में निर्मित)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where did Lord Buddha attain Mahaparinirvana?</span><span class="lang-hi">भगवान बुद्ध को महापरिनिर्वाण कहाँ प्राप्त हुआ था?</span></td>
          <td><span class="lang-en"><strong>Kushinagar (Kusinara)</strong> on the banks of Hiranyavati river</span><span class="lang-hi"><strong>कुशीनगर</strong>, हिरण्यवती नदी तट पर (483 ई.पू.)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where was the easternmost boundary of the Harappan Civilization located?</span><span class="lang-hi">हड़प्पा सभ्यता का सबसे पूर्वी सीमांत स्थल कहाँ स्थित था?</span></td>
          <td><span class="lang-en"><strong>Alamgirpur (Meerut district)</strong> along Hindon river</span><span class="lang-hi"><strong>आलमगीरपुर (मेरठ)</strong> हिंडन नदी तट पर</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where were ancient copper chariots of warrior civilization discovered in UP?</span><span class="lang-hi">उ.प्र. में प्राचीन ताम्र रथ एवं योद्धा समाधियां कहाँ खोजी गईं?</span></td>
          <td><span class="lang-en"><strong>Sinauli (Baghpat district)</strong></span><span class="lang-hi"><strong>सिनौली (बागपत जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which is the earliest temple in India with a stone Shikhara?</span><span class="lang-hi">भारत में पत्थर के शिखर से युक्त पहला मंदिर कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Dashavatara Temple, Deogarh (Lalitpur district)</strong></span><span class="lang-hi"><strong>दशावतार मंदिर, देवगढ़ (ललितपुर जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the oldest surviving complete brick &amp; terracotta temple in India?</span><span class="lang-hi">भारत में ईंटों व टेराकोटा से बना सबसे प्राचीन मंदिर कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Bhitargaon Temple (Kanpur Nagar)</strong> (5th century Gupta era)</span><span class="lang-hi"><strong>भीतरगांव मंदिर (कानपुर नगर)</strong> (5वीं सदी गुप्त काल)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">When and by whom was the Bara Imambara in Lucknow built?</span><span class="lang-hi">लखनऊ का बड़ा इमामबाड़ा कब और किसके द्वारा बनवाया गया था?</span></td>
          <td><span class="lang-en"><strong>1784 CE by Nawab Asaf-ud-Daula</strong> (Architect: Kifayatullah)</span><span class="lang-hi"><strong>1784 ई. में नवाब आसफ-उद-दौला द्वारा</strong> (वास्तुकार: किफायतउल्लाह)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the height of Rumi Darwaza in Lucknow?</span><span class="lang-hi">लखनऊ के रूमी दरवाजे की ऊंचाई कितनी है?</span></td>
          <td><span class="lang-en"><strong>60 feet</strong> (Turkish Gate, modeled on Constantinople gate)</span><span class="lang-hi"><strong>60 फीट</strong> (कांस्टेंटिनोपल के प्रवेश द्वार की तर्ज पर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the tallest clock tower in India located?</span><span class="lang-hi">भारत का सबसे ऊंचा क्लॉक टॉवर कहाँ स्थित है?</span></td>
          <td><span class="lang-en"><strong>Husainabad Clock Tower, Lucknow (221 feet, built 1881)</strong></span><span class="lang-hi"><strong>हुसैनाबाद क्लॉक टॉवर, लखनऊ (221 फीट, 1881)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">At which fort did Sher Shah Suri die in 1545?</span><span class="lang-hi">1545 में शेरशाह सूरी की मृत्यु किस दुर्ग की घेराबंदी में हुई थी?</span></td>
          <td><span class="lang-en"><strong>Kalinjar Fort (Banda district)</strong></span><span class="lang-hi"><strong>कालिंजर दुर्ग (बांदा जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city was renowned as 'Shiraz-e-Hind' for its Sharqi architecture?</span><span class="lang-hi">शर्की स्थापत्य एवं विद्या हेतु किस नगर को 'शीराज-ए-हिंद' कहा जाता था?</span></td>
          <td><span class="lang-en"><strong>Jaunpur (जौनपुर)</strong> (famous for Atala Masjid)</span><span class="lang-hi"><strong>जौनपुर</strong> (अटाला मस्जिद हेतु विख्यात)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "heritage", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_heritage_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
