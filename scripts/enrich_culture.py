import os
import re

def build_culture_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Cultural Heritage &amp; Traditional Ecosystem of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की सांस्कृतिक विरासत एवं परंपरा परिदृश्य</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Culture of Uttar Pradesh] --> B[Composite Ganga-Jamuni Tehzeeb]
    A --> C[Regional Cultural Zones: 5 Hubs]
    A --> D[Fairs & Melas: Highest in India ~2250]
    A --> E[Theatrical Traditions: Ramlila & Nautanki]
    A --> F[Music & Dance: Kathak & Classical Gharanas]
    A --> G[Tribal Culture & Traditions]
    A --> H[Cultural Academies & UNESCO Recognitions]

    B --> B1[Synthesis of Hindu-Islamic Traditions]
    B --> B2[Sufi-Bhakti Saints: Kabir, Tulsidas, Amir Khusro]

    C --> C1[Braj: Krishna Bhakti, Charkula, Rasiya, Lathmar Holi]
    C --> C2[Awadh: Nawabi Sophistication, Kathak, Thumri, Sohar]
    C --> C3[Bundelkhand: Chhatrasal Valor, Alha Ballad, Rai Dance]
    C --> C4[Purvanchal: Bhojpuri Heritage, Birha, Kajari, Dhobiya]
    C --> C5[Rohilkhand: Urdu Poetry, Woodcraft, Qawwali]

    D --> D1[Kumbh & Mahakumbh Prayagraj: UNESCO 2017]
    D --> D2[Bateshwar Agra & Dadhri Ballia: Cattle Fairs]
    D --> D3[Nauchandi Meerut & Deva Sharif Barabanki: Harmony]
    D --> D4[District Rank: Mathura 86 Max | Pilibhit Least]

    E --> E1[Ramlila: Ramnagar Varanasi 31-Day UNESCO Heritage]
    E --> E2[Nautanki: Hathras Doha School & Kanpur Social Drama]
    E --> E3[Raslila Braj & Swang Operatic Folk Theater]

    F --> F1[Kathak: Only Classical Dance of North India]
    F --> F2[Lucknow Gharana: Wajid Ali Shah, Birju Maharaj]
    F --> F3[Banaras Gharana: Girija Devi, Bismillah Khan]

    G --> G1[Tharu: Largest Tribe, Diwali as Shok Parv, Terai]
    G --> G2[Sonbhadra: Highest ST Population & 10+ Tribes]
    G --> G3[Sahariya: Lalitpur | Buksa/Bhoksa: Bijnor]

    H --> H1[UNESCO Sites: Taj Mahal, Agra Fort, Fatehpur Sikri]
    H --> H2[UNESCO Intangible: Ramlila 2008 & Kumbh Mela 2017]
    H --> H3[Institutes: Bhatkhande 1926, Lalit Kala 1962, BNA 1975]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की संस्कृति] --> B[गंगा-जमुनी साझी तहज़ीब]
    A --> C[क्षेत्रीय सांस्कृतिक अंचल: 5 प्रमुख क्षेत्र]
    A --> D[मेले एवं उत्सव: देश में सर्वाधिक ~2250]
    A --> E[पारंपरिक लोक रंगमंच: रामलीला एवं नौटंकी]
    A --> F[संगीत एवं नृत्य: कथक एवं शास्त्रीय घराने]
    A --> G[जनजातीय संस्कृति एवं लोक जीवन]
    A --> H[सांस्कृतिक संस्थाएं एवं यूनेस्को धरोहर]

    B --> B1[हिंदू-मुस्लिम सांस्कृतिक समन्वय]
    B --> B2[भक्ति-सूफी संत परंपरा: कबीर, तुलसीदास, अमीर खुसरो]

    C --> C1[ब्रज: कृष्ण भक्ति, चरकुला, रसिया, लठमार होली]
    C --> C2[अवध: नफासत, कथक, ठुमरी, सोहर, वाजिद अली शाह]
    C --> C3[बुंदेलखंड: शौर्य गाथाएं, आल्हा, राई नृत्य, पाई-डंडा]
    C --> C4[पूर्वांचल: भोजपुरी संस्कृति, बिरहा, कजरी, धोबिया]
    C --> C5[रोहिलखंड: उर्दू शायरी, काष्ठ शिल्प, कव्वाली]

    D --> D1[कुंभ व महाकुंभ प्रयागराज: यूनेस्को अमूर्त धरोहर 2017]
    D --> D2[बटेश्वर आगरा व ददरी बलिया: विशाल पशु मेले]
    D --> D3[नौचंदी मेरठ व देवा शरीफ बाराबंकी: कौमी एकता]
    D --> D4[जिला रैंकिंग: मथुरा सर्वाधिक 86 | पीलीभीत न्यूनतम]

    E --> E1[रामलीला: रामनगर वाराणसी 31-दिवसीय यूनेस्को धरोहर]
    E --> E2[नौटंकी: हाथरस दोहा-चौबोला व कानपुर सामाजिक शैली]
    E --> E3[रासलीला ब्रज एवं स्वांग लोक नाट्य]

    F --> F1[कथक: उत्तर भारत का एकमात्र शास्त्रीय नृत्य]
    F --> F2[लखनऊ घराना: नवाब वाजिद अली शाह, बिरजू महाराज]
    F --> F3[बनारस घराना: गिरिजा देवी, बिस्मिल्लाह खां]

    G --> G1[थारू: सबसे बड़ी जनजाति, दीपावली शोक पर्व, तराई]
    G --> G2[सोनभद्र: सर्वाधिक जनजाति जनसंख्या एवं विविधता]
    G --> G3[सहरिया: ललितपुर | बुक्सा/भोक्सा: बिजनौर]

    H --> H1[यूनेस्को स्थल: ताजमहल, आगरा किला, फतेहपुर सीकरी]
    H --> H2[यूनेस्को अमूर्त धरोहर: रामलीला 2008 एवं कुंभ 2017]
    H --> H3[प्रमुख संस्थान: भातखंडे 1926, ललित कला 1962, BNA 1975]
    </div>
  </div>
</div>

<!-- Card 2: Composite Culture & Regional Cultural Zones -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Ganga-Jamuni Tehzeeb &amp; Regional Cultural Distinctiveness</span>
    <span class="lang-hi">1. गंगा-जमुनी तहज़ीब एवं क्षेत्रीय सांस्कृतिक विशिष्टता</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Ganga-Jamuni Tehzeeb (गंगा-जमुनी तहज़ीब):</strong> The syncretic cultural ethos of Uttar Pradesh, symbolizing the peaceful coexistence, linguistic blending, and mutual enrichment of Hindu and Islamic traditions along the fertile alluvial plains of the Ganga and Yamuna.</span>
      <span class="lang-hi"><strong>गंगा-जमुनी तहज़ीब:</strong> उत्तर प्रदेश का संश्लिष्ट सांस्कृतिक लोकाचार, जो गंगा और यमुना के उर्वर मैदानी भाग में हिंदू और इस्लामी परंपराओं के शांतिपूर्ण सह-अस्तित्व, भाषाई समन्वय और पारस्परिक सांस्कृतिक आदान-प्रदान का प्रतीक है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Braj Cultural Zone (Mathura, Agra, Aligarh, Hathras):</strong> Centered around Lord Krishna's childhood lore (Leelas), Surdas's poetry, Haveli Sangeet, Dhrupad, Brajbhasha literature, and folk expressions like Charkula and Rasiya.</span>
      <span class="lang-hi"><strong>ब्रज सांस्कृतिक क्षेत्र (मथुरा, आगरा, अलीगढ़, हाथरस):</strong> भगवान श्री कृष्ण की बाल-लीलाओं, सूरदास के पदों, हवेली संगीत, ध्रुपद, ब्रजभाषा साहित्य तथा चरकुला व रसिया जैसी लोक कलाओं पर केंद्रित।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Awadh Cultural Zone (Lucknow, Ayodhya, Barabanki, Rae Bareli):</strong> Famous for its sophisticated etiquette (Adab-o-Tahzeeb), Tulsidas's Ramcharitmanas, Nawabi court patronage of Kathak, Thumri, Gazal, Marsiya, Dastangoi, and culinary arts (Dum-pukht cuisine).</span>
      <span class="lang-hi"><strong>अवध सांस्कृतिक क्षेत्र (लखनऊ, अयोध्या, बाराबंकी, रायबरेली):</strong> अपनी विशिष्ट नफासत और नजाकत (अदब-ओ-तहज़ीब), तुलसीदास कृत रामचरितमानस, कथक, ठुमरी, गजल, मरसिया, दास्तानगोई तथा लखनवी दस्तरख्वान (दमपुख्त भोजन) हेतु प्रख्यात।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Bundelkhand Cultural Zone (Jhansi, Mahoba, Banda, Chitrakoot):</strong> Characterized by martial chivalry, heroic folklore of Alha-Udal, Raja Chhatrasal's resistance, Bundeli language, and energetic folk dances like Rai, Pai-Danda, and Diwari.</span>
      <span class="lang-hi"><strong>बुंदेलखंड सांस्कृतिक क्षेत्र (झांसी, महोबा, बांदा, चित्रकूट):</strong> अदम्य शौर्य, आल्हा-ऊदल की वीर गाथाओं, महाराजा छत्रसाल के स्वाभिमान, बुंदेली भाषा तथा राई, पाई-डंडा व दीवारी जैसे ऊर्जावान लोक नृत्यों से युक्त।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Purvanchal &amp; Bhojpuri Zone (Varanasi, Gorakhpur, Ballia, Ghazipur):</strong> Spiritual heartland of India (Kashi), Kabir's Nirguna philosophy, Buddhist monastic roots (Sarnath, Kushinagar), and soulful folk songs (Birha, Kajari, Sohar).</span>
      <span class="lang-hi"><strong>पूर्वांचल एवं भोजपुरी क्षेत्र (वाराणसी, गोरखपुर, बलिया, गाजीपुर):</strong> भारत की आध्यात्मिक राजधानी (काशी), कबीर की निर्गुण परंपरा, बौद्ध तीर्थ (सारनाथ, कुशीनगर) तथा बिरहा, कजरी व सोहर जैसे मर्मस्पर्शी लोक गीतों का केंद्र।</span>
    </li>
  </ul>
</div>

<!-- Card 3: Major Fairs (Melas) & Festivals of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Major Fairs (मेले) &amp; Traditional Festivals of Uttar Pradesh</span>
    <span class="lang-hi">2. उत्तर प्रदेश के प्रमुख मेले एवं पारंपरिक उत्सव</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Fairs Capital of India:</strong> Uttar Pradesh hosts the largest number of annual fairs in India—approximately <strong>2,250 fairs</strong> are organized every year across its 75 districts.</span>
      <span class="lang-hi"><strong>मेलों का अग्रणी राज्य:</strong> उत्तर प्रदेश में देश में सर्वाधिक मेले आयोजित होते हैं—राज्य के 75 जिलों में प्रतिवर्ष लगभग <strong>2,250 मेले</strong> आयोजित किए जाते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>District Fairs Ranking:</strong>
        <br/>• <strong>Highest Number of Fairs:</strong> <strong>Mathura (86 fairs)</strong>, followed by Kanpur (80), Hamirpur (79), Jhansi (78), Agra (72), and Fatehpur (70).
        <br/>• <strong>Lowest Number of Fairs:</strong> <strong>Pilibhit (least, only 2-3 fairs)</strong>.
      </span>
      <span class="lang-hi"><strong>जिलों की मेला रैंकिंग:</strong>
        <br/>• <strong>सर्वाधिक मेले:</strong> <strong>मथुरा (86 मेले)</strong>, इसके बाद कानपुर (80), हमीरपुर (79), झांसी (78), आगरा (72) तथा फतेहपुर (70)।
        <br/>• <strong>न्यूनतम मेले:</strong> <strong>पीलीभीत (सबसे कम, मात्र 2-3 मेले)</strong>।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Kumbh &amp; Mahakumbh Mela (Prayagraj):</strong> Held at the sacred Triveni Sangam (Ganga, Yamuna, mythical Saraswati). Mahakumbh every 12 years; Kumbh (Ardh Kumbh) every 6 years; Magh Mela organized annually in Jan-Feb. Inscribed on <strong>UNESCO's Representative List of Intangible Cultural Heritage of Humanity in 2017</strong>.</span>
      <span class="lang-hi"><strong>कुंभ एवं महाकुंभ मेला (प्रयागराज):</strong> पावन त्रिवेणी संगम (गंगा, यमुना व सरस्वती) पर आयोजित। महाकुंभ प्रत्येक 12 वर्ष पर, अर्धकुंभ प्रत्येक 6 वर्ष पर तथा माघ मेला प्रतिवर्ष जनवरी-फरवरी में। वर्ष <strong>2017 में यूनेस्को की अमूर्त सांस्कृतिक विरासत सूची</strong> में शामिल।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Bateshwar Mela (Agra):</strong> Organized on the banks of Yamuna in Kartik month; dedicated to Lord Shiva (101 Shiva temples complex) and renowned as UP's largest <strong>Cattle and Camel Fair (पशु मेला)</strong>.</span>
      <span class="lang-hi"><strong>बटेश्वर मेला (आगरा):</strong> कार्तिक माह में यमुना तट पर 101 शिव मंदिर परिसर में आयोजित; उत्तर प्रदेश का सबसे बड़ा <strong>ऊंट एवं पशु मेला</strong>।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Dadhri Mela (Ballia):</strong> Organized on Kartik Purnima in memory of sage Bhrigu's disciple Dardar Muni; second-largest cattle fair in Uttar Pradesh.</span>
      <span class="lang-hi"><strong>ददरी मेला (बलिया):</strong> महर्षि भृगु के शिष्य दर्दर मुनि के सम्मान में कार्तिक पूर्णिमा को आयोजित; उत्तर प्रदेश का दूसरा सबसे बड़ा पशु मेला।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Nauchandi Mela (Meerut):</strong> Starts on the second Sunday after Holi; historic symbol of Hindu-Muslim communal harmony where Navchandi Devi temple and Dargah of Hazrat Bale Mian stand face-to-face.</span>
      <span class="lang-hi"><strong>नौचंदी मेला (मेरठ):</strong> होली के दूसरे रविवार से प्रारंभ; हिंदू-मुस्लिम सांप्रदायिक सौहार्द का ऐतिहासिक प्रतीक जहां नवचंदी देवी मंदिर और बाले मियां की दरगाह आमने-सामने स्थित हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Deva Sharif Mela (Barabanki):</strong> Annual Urs organized in Kartik month at the shrine of celebrated Sufi saint <strong>Haji Waris Ali Shah</strong>, spreading the universal message of <em>"Jo Rab Hai Wahi Ram Hai"</em>.</span>
      <span class="lang-hi"><strong>देवा शरीफ मेला (बाराबंकी):</strong> प्रसिद्ध सूफी संत <strong>हाजी वारिस अली शाह</strong> की मजार पर कार्तिक माह में वार्षिक उर्स; सर्वधर्म समभाव ("जो रब है वही राम है") का प्रतीक।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Syed Salar Masud Ghazi Mela (Bahraich):</strong> Massive annual fair held in Jyeshtha month at the Dargah of warrior-saint Syed Salar Masud Ghazi.</span>
      <span class="lang-hi"><strong>सैयद सालार मसूद गाजी मेला (बहराइच):</strong> ज्येष्ठ माह के प्रथम रविवार को गाजी मियां की दरगाह पर आयोजित विशाल मेला।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Govind Saheb Mela (Ambedkar Nagar):</strong> Held at the Samadhi of Mahatma Govind Saheb on Margashirsha (Agahan) Shukla Dashami; famous for cattle and indigenous trade.</span>
      <span class="lang-hi"><strong>गोविंद साहब मेला (अंबेडकर नगर):</strong> अगहन शुक्ल दशमी को महात्मा गोविंद साहब की समाधि पर आयोजित; पशु व खादी व्यापार हेतु विख्यात।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Khichdi Mela (Gorakhpur):</strong> Celebrated every year on Makar Sankranti (14-15 January) at the historic Gorakhnath Temple of the Nath sect.</span>
      <span class="lang-hi"><strong>खिचड़ी मेला (गोरखपुर):</strong> नाथ संप्रदाय के विश्वप्रसिद्ध गोरखनाथ मंदिर में मकर संक्रांति (14-15 जनवरी) पर आयोजित ऐतिहासिक मेला।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Shakumbhari Devi Mela (Saharanpur):</strong> Organized twice a year during Navratri at the foothills of Shivalik mountains.</span>
      <span class="lang-hi"><strong>शाकंभरी देवी मेला (सहारनपुर):</strong> शिवालिक पहाड़ियों की तलहटी में स्थित शाकंभरी देवी शक्तिपीठ पर नवरात्रि में आयोजित मेला।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Soron Mela (Kasganj):</strong> Held on Margashirsha Ekadashi at Soron Shukar Kshetra on the banks of Ganga, venerated as the Varaha Avatar site.</span>
      <span class="lang-hi"><strong>सोरो मेला (कासगंज):</strong> मार्गशीर्ष एकादशी को गंगा तट स्थित शूकर क्षेत्र (वराह अवतार स्थल) पर आयोजित।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kampil Mela (Farrukhabad):</strong> Renowned cultural gathering dedicated to Jain Tirthankaras and ancient Mahajanapada heritage (Panchala capital).</span>
      <span class="lang-hi"><strong>काम्पिल मेला (फर्रुखाबाद):</strong> प्राचीन पांचाल राजधानी कांपिल्य में जैन तीर्थंकरों (विमलनाथ) के सम्मान में आयोजित जैन संस्कृति मेला।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Unique Holi Celebrations of UP:</strong>
        <br/>• <strong>Lathmar Holi (Barsana &amp; Nandgaon, Mathura):</strong> Celebrated on Phalgun Shukla Navami and Dashami; women playfully beat men shield-bearers with wooden sticks.
        <br/>• <strong>Huranga (Dauji Temple, Baldeo, Mathura):</strong> Held the day after Holi; devar-bhabhi playful tearing of clothes dipped in natural dyes.
        <br/>• <strong>Chhadimar Holi (Gokul):</strong> Women strike with small sticks (Chhadis) instead of heavy lathis to protect child Krishna.
        <br/>• <strong>Chita Bhasma Holi (Masane Ki Holi, Manikarnika Ghat, Varanasi):</strong> Played with pyre ash on Rangbhari Ekadashi in honor of Lord Shiva.
      </span>
      <span class="lang-hi"><strong>उ.प्र. की विशिष्ट होली परंपराएं:</strong>
        <br/>• <strong>लठमार होली (बरसाना व नंदगांव, मथुरा):</strong> फाल्गुन शुक्ल नवमी व दशमी को; गोपियां (हुरियारिनें) ढाल लिए पुरुषों (हुरियारों) पर लाठियां बरसाती हैं।
        <br/>• <strong>हुरंगा (दाऊजी मंदिर, बलदेव, मथुरा):</strong> होली के अगले दिन आयोजित; देवर-भाभी का पारंपरिक रंगोत्सव जिसमें कपड़े फाड़कर रंग में डुबोए जाते हैं।
        <br/>• <strong>छड़ीमार होली (गोकुल):</strong> भगवान कृष्ण के बाल स्वरूप के कारण लाठी के स्थान पर छोटी छड़ियों से खेली जाती है।
        <br/>• <strong>मसाने की होली / चिता भस्म होली (मणिकर्णिका घाट, काशी):</strong> रंगभरी एकादशी के अगले दिन भगवान शिव के गणों द्वारा चिता भस्म से खेली जाने वाली अनोखी होली।
      </span>
    </li>
  </ul>
</div>

<!-- Card 4: Folk Theatre & Performing Traditions -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Traditional Folk Theater: Ramlila, Nautanki &amp; Raslila</span>
    <span class="lang-hi">3. पारंपरिक लोक रंगमंच: रामलीला, नौटंकी एवं रासलीला</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Ramlila of Ramnagar (Varanasi):</strong> World-renowned 31-day open-air theatrical enactment established in the 1830s under Maharaja Udit Narayan Singh. Inscribed by <strong>UNESCO as an Intangible Cultural Heritage of Humanity in 2008</strong>. The entire town serves as a moving stage without modern microphones or electric lighting.</span>
      <span class="lang-hi"><strong>रामनगर (वाराणसी) की रामलीला:</strong> 1830 के दशक में महाराजा उदित नारायण सिंह द्वारा स्थापित 31-दिवसीय खुला मंचन। वर्ष <strong>2008 में यूनेस्को द्वारा मानवता की अमूर्त सांस्कृतिक धरोहर</strong> घोषित। पूरा कस्बा बिना किसी माइक या कृत्रिम प्रकाश के विशाल रंगमंच में बदल जाता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Nautanki (नौटंकी):</strong> The most popular operatic folk theater of North India, deriving from medieval ballads, Swang, and Bhagat traditions. Employs musical instruments like the <strong>Nakkara (नगाड़ा), Dholak, and Harmonium</strong>.</span>
      <span class="lang-hi"><strong>नौटंकी:</strong> उत्तर भारत का सर्वाधिक लोकप्रिय गीति-नाट्य (लोक रंगमंच), जिसकी जड़ें मध्यकालीन स्वांग एवं भगत परंपरा में हैं। इसमें <strong>नगाड़ा, ढोलक एवं हारमोनियम</strong> प्रमुख वाद्ययंत्र होते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Two Historic Schools (Gharanas) of Nautanki:</strong>
        <br/>• <strong>Hathras School (हाथरस शैली):</strong> Founded by <strong>Indraman</strong> and Pandit Natharam Sharma Gour. Characterized by classical raga bases, high-pitch operatic singing, and poetic meters (Doha, Chaubola, Chhand, Bahr-e-Taweel).
        <br/>• <strong>Kanpur School (कानपुर शैली):</strong> Founded by <strong>Shrikrishna Pahalwan</strong>. Emphasizes modern prose dialogues, social and patriotic realism, theatrical melodrama, and accessible popular tunes.
      </span>
      <span class="lang-hi"><strong>नौटंकी की दो ऐतिहासिक शैलियां (घराने):</strong>
        <br/>• <strong>हाथरस शैली:</strong> प्रवर्तक <strong>इंद्रमन</strong> एवं पंडित नथाराम शर्मा गौड़। शास्त्रीय रागों, उच्च स्वर गायकी तथा दोहा, चौबोला, छंद व बहरे-तवील छंदों पर आधारित।
        <br/>• <strong>कानपुर शैली:</strong> प्रवर्तक <strong>श्रीकृष्ण पहलवान</strong>। गद्य संवादों, सामाजिक एवं देशभक्ति नाटकों, रंगमंचीय अभिनय तथा जनसुलभ धुनों पर आधारित।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Raslila (रासलीला):</strong> Devotional dance-drama of the Braj region (Mathura-Vrindavan), originally formulated by Swami Haridas and Vallabhacharya's disciples, depicting Radha-Krishna's eternal divine play.</span>
      <span class="lang-hi"><strong>रासलीला:</strong> ब्रज क्षेत्र (मथुरा-वृंदावन) का भक्ति प्रधान नृत्य-नाट्य, जिसे स्वामी हरिदास एवं वल्लभाचार्य के अष्टछाप कवियों ने स्वरूप प्रदान किया; राधा-कृष्ण की नित्य लीलाओं का चित्रण।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Swang &amp; Bhagat:</strong> Older operatic folk theater forms prevailing in Western UP (Meerut, Aligarh, Agra) that laid the foundation for modern Nautanki.</span>
      <span class="lang-hi"><strong>स्वांग एवं भगत:</strong> पश्चिमी उत्तर प्रदेश (मेरठ, अलीगढ़, आगरा) के प्राचीन खुले लोक नाट्य, जिन्होंने आधुनिक नौटंकी की आधारशिला रखी।</span>
    </li>
  </ul>
</div>

<!-- Card 5: Classical & Folk Performing Arts (Kathak, Gharanas, Folk Music) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Classical Dance (Kathak), Music Gharanas &amp; Folk Songs</span>
    <span class="lang-hi">4. शास्त्रीय नृत्य (कथक), संगीत घराने एवं प्रमुख लोक गीत</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Kathak (कथक) - Only Classical Dance of North India:</strong>
        <br/>• Originated from temple storytellers ('Katha Kahe So Kathak Kahave').
        <br/>• Attained classical refinement under the patronage of Awadh's last Nawab, <strong>Wajid Ali Shah</strong> (who danced under the pen-name <em>Akhtar Piya</em> in Rahas plays).
        <br/>• <strong>Lucknow Gharana Pioneers:</strong> Founded by <strong>Thakur Prasad</strong>; elevated by Maharaj brothers (Kalka Prasad and Bindadin Maharaj). Modern legends include <strong>Pt. Birju Maharaj</strong>, Lachhu Maharaj, and Shambhu Maharaj.
        <br/>• <strong>Banaras Kathak Gharana:</strong> Founded by Janaki Prasad; characterized by pure Natwari Bols and strong footwork. Queen of Kathak: <strong>Sitara Devi</strong>.
      </span>
      <span class="lang-hi"><strong>कथक - उत्तर भारत का एकमात्र शास्त्रीय नृत्य:</strong>
        <br/>• उत्पत्ति मंदिर कथाकारों से ('कथा कहे सो कथक कहावे')।
        <br/>• अवध के अंतिम नवाब <strong>वाजिद अली शाह</strong> (जो 'अख्तर पिया' उपनाम से रहस्य नृत्य करते थे) के संरक्षण में शास्त्रीय उत्कृष्टता प्राप्त की।
        <br/>• <strong>लखनऊ घराना प्रवर्तक:</strong> <strong>ठाकुर प्रसाद</strong> द्वारा स्थापित; कालका-बिंदादीन महाराज ने समृद्ध किया। आधुनिक दिग्गजों में <strong>पंडित बिरजू महाराज</strong>, लच्छू महाराज व शंभू महाराज शामिल हैं।
        <br/>• <strong>बनारस कथक घराना:</strong> जानकी प्रसाद द्वारा प्रवर्तित; नटवरी बोलों व कठिन पद-संचालन हेतु विख्यात। प्रख्यात नृत्यांगना: <strong>सितारा देवी</strong>।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Major Musical Gharanas:</strong>
        <br/>• <strong>Banaras Gharana:</strong> Famous for Thumri, Dadra, Chaiti, Shehnai (Ustad Bismillah Khan - Bharat Ratna 2001), Sitar (Pt. Ravi Shankar - Bharat Ratna 1999), Thumri Queen (Girija Devi), Tabla (Pt. Kishan Maharaj, Pt. Samta Prasad 'Gudai Maharaj').
        <br/>• <strong>Kirana Gharana (Kairana, Shamli):</strong> Founded by Ustad Abdul Karim Khan &amp; Abdul Wahid Khan; renowned for slow Khayal elaboration and emotive Swara purity. Legend: Pt. Bhimsen Joshi (Bharat Ratna 2008), Gangubai Hangal.
        <br/>• <strong>Agra Gharana:</strong> Known as 'Rangeela Gharana'; synthesis of Dhrupad-Dhamar and Khayal. Master: Ustad Faiyaz Khan (honored as <em>Aftab-e-Mousiqui</em>).
        <br/>• <strong>Fatehpur Sikri Gharana:</strong> Celebrated for Dhrupad exponents; founded by Zainu Khan and Zorawar Khan during Akbar's reign.
      </span>
      <span class="lang-hi"><strong>प्रमुख संगीत घराने:</strong>
        <br/>• <strong>बनारस घराना:</strong> ठुमरी, दादरा, चैती, शहनाई (उस्ताद बिस्मिल्लाह खां - भारत रत्न 2001), सितार (पं. रवि शंकर - भारत रत्न 1999), ठुमरी साम्राज्ञी (गिरिजा देवी), तबला (पं. किशन महाराज, पं. सामता प्रसाद 'गुदई महाराज')।
        <br/>• <strong>किराना घराना (कैराना, शामली):</strong> संस्थापक उस्ताद अब्दुल करीम खां व अब्दुल वाहिद खां; विलंबित ख्याल व स्वर-शुद्धता हेतु विख्यात। दिग्गज: पं. भीमसेन जोशी (भारत रत्न 2008), गंगूबाई हंगल।
        <br/>• <strong>आगरा घराना:</strong> 'रंगीला घराना' के नाम से प्रसिद्ध; ध्रुपद-धमार व ख्याल का समन्वय। प्रमुख गायक: उस्ताद फैयाज खां (उपाधि: <em>आफताब-ए-मौसिकी</em>)।
        <br/>• <strong>फतेहपुर सीकरी घराना:</strong> ध्रुपद गायन हेतु प्रसिद्ध; अकबर के काल में जैनू खां व जोरावर खां द्वारा स्थापित।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Regional Folk Music Traditions:</strong>
        <br/>• <strong>Alha (आल्हा):</strong> Heroic ballad of Bundelkhand (Mahoba), composed by Jagnik in <em>Alha-Khand</em>, recounting 52 battles of warrior brothers Alha and Udal.
        <br/>• <strong>Birha (बिरहा):</strong> Most popular folk singing tradition of Purvanchal and Bhojpuri belt, recounting socio-political narratives and historical events.
        <br/>• <strong>Kajari (कजरी):</strong> Monsoon folk song originating in Mirzapur and Varanasi, sung during Teej and Shravan, expressing longing and rain devotion.
        <br/>• <strong>Rasiya &amp; Hori (रसिया व होरी):</strong> Braj region romantic songs celebrating Radha-Krishna's divine love and Holi.
        <br/>• <strong>Sohar (सोहर):</strong> Auspicious songs sung during childbirth and baptism ceremonies across Awadh and Purvanchal.
        <br/>• <strong>Chaiti (चैती):</strong> Classical semi-folk music sung during Chaitra month in eastern UP.
      </span>
      <span class="lang-hi"><strong>क्षेत्रीय लोक संगीत परंपराएं:</strong>
        <br/>• <strong>आल्हा:</strong> बुंदेलखंड (महोबा) का वीर रस लोक गायन; जगनिक रचित <em>आल्हा-खंड</em> पर आधारित, जिसमें आल्हा-ऊदल के 52 युद्धों का वर्णन है।
        <br/>• <strong>बिरहा:</strong> पूर्वांचल एवं भोजपुरी क्षेत्र का सर्वाधिक लोकप्रिय कथात्मक लोक गायन, जिसमें सामाजिक-ऐतिहासिक गाथाएं गाई जाती हैं।
        <br/>• <strong>कजरी:</strong> मिर्जापुर एवं वाराणसी में उत्पन्न वर्षा ऋतु का लोक गीत; सावन व कजरी तीज पर विरह एवं प्रकृति उल्लास का चित्रण।
        <br/>• <strong>रसिया व होरी:</strong> ब्रज क्षेत्र का लोक संगीत जो राधा-कृष्ण की प्रेम लीलाओं एवं होली पर गाया जाता है।
        <br/>• <strong>सोहर:</strong> अवध एवं पूर्वांचल में संतान जन्म (संस्कार गीत) के अवसर पर गाया जाने वाला मांगलिक लोक गीत।
        <br/>• <strong>चैती:</strong> चैत्र माह में रामनवमी के आसपास गाया जाने वाला अर्ध-शास्त्रीय लोक संगीत।
      </span>
    </li>
  </ul>
</div>

<!-- Card 6: Tribal Culture & Indigenous Heritage -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Tribal Culture, Demographics &amp; Customs of Uttar Pradesh</span>
    <span class="lang-hi">5. उत्तर प्रदेश की जनजातीय संस्कृति, जनसांख्यिकी एवं परंपराएं</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Tribal Population Demographics (Census 2011):</strong> Scheduled Tribes (ST) constitute <strong>0.57% of UP's total population</strong> (approx. 11.34 lakh persons). 15 tribes are notified across the state.</span>
      <span class="lang-hi"><strong>जनजातीय जनसांख्यिकी (जनगणना 2011):</strong> अनुसूचित जनजाति (ST) राज्य की कुल जनसंख्या का <strong>0.57%</strong> (लगभग 11.34 लाख) है। राज्य में कुल 15 जनजातियां अधिसूचित हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>District ST Extremes:</strong>
        <br/>• <strong>Highest ST Population &amp; Percentage:</strong> <strong>Sonbhadra</strong> (3.85 lakh ST population; ~20.7% of district population).
        <br/>• <strong>Lowest ST Population:</strong> <strong>Baghpat</strong> (only 14 persons), followed by Kannauj and Badaun.
        <br/>• <strong>Districts with Zero ST Notified Population:</strong> Ayodhya and Jalaun recorded negligible/zero rural ST groups.
      </span>
      <span class="lang-hi"><strong>जिलों में जनजातीय चरम आंकड़े:</strong>
        <br/>• <strong>सर्वाधिक ST जनसंख्या व प्रतिशत वाला जिला:</strong> <strong>सोनभद्र</strong> (3.85 लाख ST जनसंख्या; जिले का ~20.7%)।
        <br/>• <strong>न्यूनतम ST जनसंख्या वाला जिला:</strong> <strong>बागपत</strong> (मात्र 14 व्यक्ति), इसके बाद कन्नौज व बदायूं।
        <br/>• <strong>शून्य/नगण्य ST अधिसूचित जिले:</strong> अयोध्या और जालौन में ग्रामीण जनजातीय जनसंख्या नगण्य दर्ज की गई।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Tharu Tribe (थारू जनजाति) - Largest Tribe of UP:</strong>
        <br/>• <strong>Habitat:</strong> Terai region across Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, and Maharajganj (region called <em>Taruhat</em>).
        <br/>• <strong>Racial Stock:</strong> Mongoloid stock with high cheekbones and yellowish complexion.
        <br/>• <strong>Unique Custom:</strong> Celebrate <strong>Deepawali as a Day of Mourning (शोक पर्व)</strong>, offering 'Bhet' to dead ancestors.
        <br/>• <strong>Social Structure:</strong> Matriarchal influence (women hold superior domestic status); practice Badla Vivah (exchange marriage) and Bajhar festival.
        <br/>• <strong>Development:</strong> Dedicated Tharu Vikas Pariyojana launched in 1980; Eklavya Model Residential Schools established in Lakhimpur Kheri.
      </span>
      <span class="lang-hi"><strong>थारू जनजाति - उ.प्र. की सबसे बड़ी जनजाति:</strong>
        <br/>• <strong>निवास क्षेत्र:</strong> तराई बेल्ट (लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर, महराजगंज; क्षेत्र को <em>तरुहट</em> कहते हैं)।
        <br/>• <strong>प्रजातीय समूह:</strong> मंगोलॉयड प्रजाति की विशेषताएं (चपटी नाक, उभरी गाल की हड्डियां)।
        <br/>• <strong>अनोखी प्रथा:</strong> <strong>दीपावली को 'शोक पर्व'</strong> के रूप में मनाते हैं तथा पूर्वजों को पुतला बनाकर 'भेंट' अर्पित करते हैं।
        <br/>• <strong>सामाजिक व्यवस्था:</strong> मातृसत्तात्मक प्रभाव (महिलाओं को परिवार में उच्च स्थान); 'बदला विवाह' तथा 'बझहर' त्योहार प्रसिद्ध।
        <br/>• <strong>विकास पहल:</strong> 1980 में थारू विकास परियोजना प्रारंभ; लखीमपुर खीरी में एकलव्य मॉडल आवासीय विद्यालय संचालित।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Buksa / Bhoksa Tribe (बुक्सा / भोक्सा जनजाति):</strong>
        <br/>• Concentrated primarily in <strong>Bijnor</strong> district (small groups in Pauri Garhwal border).
        <br/>• Claim lineage from the <strong>Patwar Rajputs</strong> of Rajasthan.
        <br/>• Worship <strong>Chamunda Devi</strong> as their supreme patron deity; village council headed by 'Takht'.
      </span>
      <span class="lang-hi"><strong>बुक्सा / भोक्सा जनजाति:</strong>
        <br/>• मुख्य रूप से <strong>बिजनौर</strong> जिले में केंद्रित।
        <br/>• स्वयं को चित्तौड़गढ़ के <strong>पटवार राजपूतों</strong> का वंशज मानते हैं।
        <br/>• <strong>चामुंडा देवी</strong> की अनन्य उपासना करते हैं; इनकी ग्राम पंचायत का प्रधान 'तख्त' कहलाता है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Other Prominent Tribes of UP:</strong>
        <br/>• <strong>Sahariya (सहरिया):</strong> Found exclusively in <strong>Lalitpur</strong> district.
        <br/>• <strong>Agariya, Baiga, Chero, Panika, Parhaiya, Pathari, Kharwar:</strong> Inhabit the rocky forests of <strong>Sonbhadra</strong> district.
        <br/>• <strong>Jaunsari &amp; Bhotia:</strong> Historically in Uttarakhand hills, minor trans-border presence in Saharanpur.
      </span>
      <span class="lang-hi"><strong>अन्य प्रमुख जनजातियां:</strong>
        <br/>• <strong>सहरिया:</strong> मात्र <strong>ललितपुर</strong> जिले में पाई जाती है।
        <br/>• <strong>अगरिया, बैगा, चेरो, पनिका, परहिया, पठारी, खरवार:</strong> मुख्य रूप से <strong>सोनभद्र</strong> के वनांचल में निवास करते हैं।
        <br/>• <strong>जौनसारी व भोटिया:</strong> ऐतिहासिक रूप से उत्तराखंड व सहारनपुर सीमांत क्षेत्र।
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: Cultural Institutions & Academies of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Premier Cultural Institutions, Academies &amp; Museums</span>
    <span class="lang-hi">6. प्रमुख सांस्कृतिक संस्थान, अकादमियाँ एवं संग्रहालय</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Cultural Institution / Academy</span><span class="lang-hi">सांस्कृतिक संस्थान / अकादमी</span></th>
          <th><span class="lang-en">Headquarters</span><span class="lang-hi">मुख्यालय</span></th>
          <th><span class="lang-en">Year Est.</span><span class="lang-hi">स्थापना वर्ष</span></th>
          <th><span class="lang-en">Key Role &amp; Exam Relevance</span><span class="lang-hi">मुख्य भूमिका एवं परीक्षा तथ्य</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Department of Culture (संस्कृति विभाग)</span><span class="lang-hi">संस्कृति विभाग, उत्तर प्रदेश</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1957</strong></span><span class="lang-hi"><strong>1957</strong></span></td>
          <td><span class="lang-en">Apex nodal department coordinating all cultural preservation in UP</span><span class="lang-hi">राज्य में कला, संस्कृति एवं विरासत संरक्षण का शीर्ष नोडल विभाग</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Bhatkhande Sanskriti Vishwavidyalaya</span><span class="lang-hi">भातखंडे संस्कृति विश्वविद्यालय</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1926</strong></span><span class="lang-hi"><strong>1926</strong></span></td>
          <td><span class="lang-en">Founded by Pt. V.N. Bhatkhande as Marris College of Music; Deemed Univ 2000; State Univ 2022</span><span class="lang-hi">पं. विष्णु नारायण भातखंडे द्वारा 'मैरिस कॉलेज ऑफ म्यूजिक' के रूप में स्थापित; 2022 में राज्य सांस्कृतिक विश्वविद्यालय</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">State Lalit Kala Academy (राज्य ललित कला अकादमी)</span><span class="lang-hi">राज्य ललित कला अकादमी</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1962</strong></span><span class="lang-hi"><strong>1962</strong></span></td>
          <td><span class="lang-en">Promotes visual arts, painting, sculpture, and exhibitions</span><span class="lang-hi">दृश्य कला, चित्रकला, मूर्तिकला एवं कला प्रदर्शनियों का संवर्धन</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Uttar Pradesh Sangeet Natak Academy</span><span class="lang-hi">उत्तर प्रदेश संगीत नाटक अकादमी</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1963</strong></span><span class="lang-hi"><strong>1963</strong></span></td>
          <td><span class="lang-en">Promotes performing arts, music, dance, and folk drama</span><span class="lang-hi">संगीत, नृत्य, लोकनाट्य एवं प्रदर्शनकारी कलाओं का संरक्षण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Bharatendu Natya Academy (BNA)</span><span class="lang-hi">भारतेन्दु नाट्य अकादमी</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1975</strong></span><span class="lang-hi"><strong>1975</strong></span></td>
          <td><span class="lang-en">Premier professional dramatic training institute (formerly Drama Division 1975)</span><span class="lang-hi">उत्तर भारत का शीर्ष नाट्य प्रशिक्षण संस्थान (1975 में स्थापित)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">National Kathak Institute (राष्ट्रीय कथक संस्थान)</span><span class="lang-hi">राष्ट्रीय कथक संस्थान</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1988-89</strong></span><span class="lang-hi"><strong>1988-89</strong></span></td>
          <td><span class="lang-en">Apex body for research, training, and documentation of Kathak classical dance</span><span class="lang-hi">कथक नृत्य के शोध, प्रशिक्षण एवं दस्तावेजीकरण का शीर्ष संस्थान</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Ayodhya Shodh Sansthan (अयोध्या शोध संस्थान)</span><span class="lang-hi">अयोध्या शोध संस्थान</span></td>
          <td><span class="lang-en">Ayodhya</span><span class="lang-hi">अयोध्या</span></td>
          <td><span class="lang-en"><strong>1986</strong></span><span class="lang-hi"><strong>1986</strong></span></td>
          <td><span class="lang-en">Research and preservation of Ramayana culture and global Ramlila traditions</span><span class="lang-hi">रामायण कालीन संस्कृति एवं वैश्विक रामलीला परंपराओं पर शोध</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Tribal &amp; Folk Art Culture Sansthan</span><span class="lang-hi">जनजातीय एवं लोक कला संस्कृति संस्थान</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1996</strong></span><span class="lang-hi"><strong>1996</strong></span></td>
          <td><span class="lang-en">Preservation of tribal rituals, songs, and indigenous crafts</span><span class="lang-hi">जनजातीय रीति-रिवाजों, लोकगीतों व देशज शिल्पों का संरक्षण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Uttar Pradesh Jain Vidya Sansthan</span><span class="lang-hi">उत्तर प्रदेश जैन विद्या संस्थान</span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en"><strong>1990</strong></span><span class="lang-hi"><strong>1990</strong></span></td>
          <td><span class="lang-en">Promotes research and preservation of Jain literature and heritage in UP</span><span class="lang-hi">राज्य में जैन धर्म, साहित्य एवं दर्शन पर शोध व संवर्धन</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">State Museum Lucknow (राज्य संग्रहालय)</span><span class="lang-hi">राज्य संग्रहालय, लखनऊ</span></td>
          <td><span class="lang-en">Lucknow (Zoo campus)</span><span class="lang-hi">लखनऊ (चिड़ियाघर परिसर)</span></td>
          <td><span class="lang-en"><strong>1863</strong></span><span class="lang-hi"><strong>1863</strong></span></td>
          <td><span class="lang-en">Oldest multi-purpose museum in UP; houses Egyptian mummy &amp; Kushan sculptures</span><span class="lang-hi">उ.प्र. का सबसे पुराना बहुउद्देश्यीय संग्रहालय; मिस्र की ममी व कुषाण मूर्तियां</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Government Museum Mathura (राजकीय संग्रहालय)</span><span class="lang-hi">राजकीय संग्रहालय, मथुरा</span></td>
          <td><span class="lang-en">Mathura</span><span class="lang-hi">मथुरा</span></td>
          <td><span class="lang-en"><strong>1874</strong></span><span class="lang-hi"><strong>1874</strong></span></td>
          <td><span class="lang-en">World's premier collection of Kushana-era Red Sandstone Buddhist &amp; Jain sculptures</span><span class="lang-hi">कुषाण युगीन लाल बलुआ पत्थर की मूर्तियों का विश्व प्रसिद्ध संग्रह</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 8: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Rapid Revision Fact Matrix: UP Culture (Direct Exam Points)</span>
    <span class="lang-hi">7. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. की संस्कृति (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Topic</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / विषय</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Which district hosts the maximum number of fairs in UP?</span><span class="lang-hi">उ.प्र. में सर्वाधिक मेलों का आयोजन किस जिले में होता है?</span></td>
          <td><span class="lang-en"><strong>Mathura (86 fairs)</strong> (followed by Kanpur 80, Hamirpur 79)</span><span class="lang-hi"><strong>मथुरा (86 मेले)</strong> (इसके बाद कानपुर 80, हमीरपुर 79)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district hosts the minimum number of fairs in UP?</span><span class="lang-hi">उ.प्र. में सबसे कम मेलों का आयोजन किस जिले में होता है?</span></td>
          <td><span class="lang-en"><strong>Pilibhit</strong> (only 2-3 fairs annually)</span><span class="lang-hi"><strong>पीलीभीत</strong> (प्रतिवर्ष मात्र 2-3 मेले)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">When was Kumbh Mela inscribed on UNESCO's Intangible Heritage list?</span><span class="lang-hi">कुंभ मेले को यूनेस्को की अमूर्त धरोहर सूची में कब शामिल किया गया?</span></td>
          <td><span class="lang-en"><strong>Year 2017</strong> (at Jeju, South Korea session)</span><span class="lang-hi"><strong>वर्ष 2017</strong> (जेजू, दक्षिण कोरिया सत्र में)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">When was Ramlila inscribed on UNESCO's Intangible Heritage list?</span><span class="lang-hi">रामलीला को यूनेस्को की अमूर्त सांस्कृतिक धरोहर में कब शामिल किया गया?</span></td>
          <td><span class="lang-en"><strong>Year 2008</strong> (Ramnagar, Varanasi tradition)</span><span class="lang-hi"><strong>वर्ष 2008</strong> (रामनगर, वाराणसी परंपरा)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the only classical dance originating from North India?</span><span class="lang-hi">उत्तर भारत से उत्पन्न एकमात्र शास्त्रीय नृत्य कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Kathak (कथक)</strong> (Lucknow and Banaras Gharanas)</span><span class="lang-hi"><strong>कथक</strong> (लखनऊ एवं बनारस घराना)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which Awadh Nawab was a great patron of Kathak and Thumri?</span><span class="lang-hi">अवध का कौन सा नवाब कथक एवं ठुमरी का महान संरक्षक था?</span></td>
          <td><span class="lang-en"><strong>Nawab Wajid Ali Shah</strong> (pen-name 'Akhtar Piya')</span><span class="lang-hi"><strong>नवाब वाजिद अली शाह</strong> (उपनाम 'अख्तर पिया')</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What are the two prominent schools (gharanas) of Nautanki?</span><span class="lang-hi">नौटंकी की दो प्रमुख शैलियां (घराने) कौन सी हैं?</span></td>
          <td><span class="lang-en"><strong>Hathras School</strong> (operatic) &amp; <strong>Kanpur School</strong> (dramatic prose)</span><span class="lang-hi"><strong>हाथरस शैली</strong> (गायन प्रधान) एवं <strong>कानपुर शैली</strong> (नाट्य/संवाद प्रधान)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which fair in UP is celebrated as a symbol of Hindu-Muslim unity?</span><span class="lang-hi">उ.प्र. का कौन सा मेला हिंदू-मुस्लिम एकता के प्रतीक के रूप में प्रसिद्ध है?</span></td>
          <td><span class="lang-en"><strong>Nauchandi Mela (Meerut)</strong> &amp; <strong>Sulah-kul Utsav (Agra)</strong></span><span class="lang-hi"><strong>नौचंदी मेला (मेरठ)</strong> एवं <strong>सुलह-कुल उत्सव (आगरा)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the largest camel/cattle animal fair held in UP?</span><span class="lang-hi">उ.प्र. में सबसे बड़ा ऊंट/पशु मेला कहाँ आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Bateshwar Mela (Agra)</strong> on the banks of Yamuna</span><span class="lang-hi"><strong>बटेश्वर मेला (आगरा)</strong> यमुना तट पर</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the famous Deva Sharif Mela organized?</span><span class="lang-hi">प्रसिद्ध देवा शरीफ मेला कहाँ आयोजित किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Barabanki</strong> (Shrine of Sufi saint Waris Ali Shah)</span><span class="lang-hi"><strong>बाराबंकी</strong> (सूफी संत हाजी वारिस अली शाह की दरगाह)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is Lathmar Holi traditionally celebrated?</span><span class="lang-hi">लठमार होली पारंपरिक रूप से कहाँ खेली जाती है?</span></td>
          <td><span class="lang-en"><strong>Barsana and Nandgaon</strong> (Mathura district)</span><span class="lang-hi"><strong>बरसाना एवं नंदगांव</strong> (मथुरा)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which is the largest Scheduled Tribe in Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश की सबसे बड़ी अनुसूचित जनजाति कौन सी है?</span></td>
          <td><span class="lang-en"><strong>Tharu Tribe (थारू जनजाति)</strong> (residing in Terai belt)</span><span class="lang-hi"><strong>थारू जनजाति</strong> (तराई क्षेत्र में निवास)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which tribe in UP observes Deepawali as a day of mourning?</span><span class="lang-hi">उ.प्र. की कौन सी जनजाति दीपावली को शोक पर्व के रूप में मनाती है?</span></td>
          <td><span class="lang-en"><strong>Tharu Tribe</strong> (थारू जनजाति)</span><span class="lang-hi"><strong>थारू जनजाति</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the highest tribal population in UP?</span><span class="lang-hi">उ.प्र. में सर्वाधिक जनजाति जनसंख्या वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Sonbhadra</strong> (3.85 lakh ST population; ~20.7%)</span><span class="lang-hi"><strong>सोनभद्र</strong> (3.85 लाख ST जनसंख्या; ~20.7%)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which district is the Sahariya tribe exclusively found?</span><span class="lang-hi">सहरिया जनजाति विशेष रूप से किस जिले में पाई जाती है?</span></td>
          <td><span class="lang-en"><strong>Lalitpur district</strong> (ललितपुर)</span><span class="lang-hi"><strong>ललितपुर जिला</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the oldest museum in Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश का सबसे पुराना संग्रहालय कौन सा है?</span></td>
          <td><span class="lang-en"><strong>State Museum Lucknow (राजकीय संग्रहालय, 1863)</strong></span><span class="lang-hi"><strong>राज्य संग्रहालय, लखनऊ (स्थापना 1863)</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "culture", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_culture_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
