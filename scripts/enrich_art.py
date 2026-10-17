import os
import re

def build_art_theory_html():
    return """
<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Arts, Crafts &amp; Cultural Heritage of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश की कला, शिल्प एवं सांस्कृतिक विरासत</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Art Heritage of UP] --> B[Painting Traditions]
    A --> C[Traditional Handicrafts & GI Tags]
    A --> D[Classical Music & Vocal Gharanas]
    A --> E[Kathak Classical Dance]
    A --> F[Key Cultural Academies]

    B --> B1[Prehistoric: Mirzapur Rock Art 1880 Carlleyle]
    B --> B2[Mughal: Humayun, Akbar Hamzanama, Jahangir Golden Age]
    B --> B3[Mathura & Awadh Wash Style: Asit Kumar Haldar 1925]

    C --> C1[Textiles: Lucknow Chikan/Zardozi, Varanasi Silk Brocade]
    C --> C2[Carpets: Bhadohi Carpet City, Mirzapur Dari]
    C --> C3[Metals: Moradabad Peetal Nagari, Aligarh Locks]
    C --> C4[Pottery: Khurja Ceramic, Nizamabad Black Clay, Gorakhpur Terracotta]
    C --> C5[Wood & Glass: Saharanpur Woodcraft, Firozabad Glass Bangles]
    C --> C6[Perfumery: Kannauj Attar Perfume Capital Deg-Bhapka]

    D --> D1[Banaras Gharana: Bismillah Khan, Ravi Shankar, Girija Devi]
    D --> D2[Kirana Gharana Shamli: Abdul Karim Khan, Bhimsen Joshi]
    D --> D3[Agra Gharana: Faiyaz Khan Aftab-e-Mousiqui]

    E --> E1[Only Classical Dance of North India]
    E --> E2[Lucknow Gharana: Wajid Ali Shah, Kalka-Bindadin, Birju Maharaj]
    E --> E3[Banaras Gharana: Janaki Prasad Natwari Bol]

    F --> F1[Bhatkhande Sangeet Sansthan 1926 Marris College]
    F --> F2[State Lalit Kala Akademi 1962 Lucknow]
    F --> F3[UP Sangeet Natak Akademi 1963 & Bhartendu Natya 1975]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की कला विरासत] --> B[चित्रकला परंपराएं]
    A --> C[पारंपरिक हस्तशिल्प एवं GI टैग]
    A --> D[शास्त्रीय संगीत घराने]
    A --> E[कथक शास्त्रीय नृत्य]
    A --> F[प्रमुख सांस्कृतिक अकादमियाँ]

    B --> B1[प्रागैतिहासिक: मिर्जापुर शैलचित्र 1880 कार्लाइल]
    B --> B2[मुगल: हुमायूँ, अकबर हम्ज़ानामा, जहांगीर स्वर्णकाल]
    B --> B3[मथुरा व अवध वॉश शैली: असित कुमार हलदार 1925]

    C --> C1[वस्त्र: लखनऊ चिकनकारी-जरदोजी, बनारसी सिल्क साड़ी]
    C --> C2[कालीन: भदोही कालीन नगरी, मिर्जापुर दरी]
    C --> C3[धातु: मुरादाबाद पीतल नगरी, अलीगढ़ ताला नगरी]
    C --> C4[मृद्भांड: खुर्जा चीनी मिट्टी, निजामाबाद काली मिट्टी, गोरखपुर टेराकोटा]
    C --> C5[काष्ठ व कांच: सहारनपुर नक्काशी, फिरोजाबाद कांच चूड़ियां]
    C --> C6[इत्र: कन्नौज इत्र राजधानी देग-भपका पद्धति]

    D --> D1[बनारस घराना: बिस्मिल्लाह खां, रवि शंकर, गिरिजा देवी]
    D --> D2[किराना घराना शामली: अब्दुल करीम खां, भीमसेन जोशी]
    D --> D3[आगरा घराना: फैयाज खां आफताब-ए-मौसकी]

    E --> E1[उत्तर भारत का एकमात्र शास्त्रीय नृत्य]
    E --> E2[लखनऊ घराना: वाजिद अली शाह, कालका-बिंदादीन, बिरजू महाराज]
    E --> E3[बनारस घराना: जानकी प्रसाद नटवरी बोल]

    F --> F1[भातखंडे संगीत संस्थान 1926 मैरिस कॉलेज]
    F --> F2[राज्य ललित कला अकादमी 1962 लखनऊ]
    F --> F3[उ.प्र. संगीत नाटक अकादमी 1963 व भारतेन्दु नाट्य 1975]
    </div>
  </div>
</div>

<!-- Card 2: Painting Traditions of Uttar Pradesh -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Painting Traditions of UP: From Prehistoric Caves to Modern Wash Art</span>
    <span class="lang-hi">1. उत्तर प्रदेश की चित्रकला: प्रागैतिहासिक गुफाओं से आधुनिक वॉश कला तक</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Painting Era / School</span><span class="lang-hi">चित्रकला शैली / काल</span></th>
        <th><span class="lang-en">Key Centers in UP</span><span class="lang-hi">उ.प्र. में मुख्य केंद्र</span></th>
        <th><span class="lang-en">Prominent Features &amp; Exam Facts</span><span class="lang-hi">प्रमुख विशेषताएँ एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Pre-historic Rock Art (प्रागैतिहासिक शैलचित्र)</strong></span><span class="lang-hi"><strong>प्रागैतिहासिक शैलचित्र</strong></span></td>
        <td><span class="lang-en"><strong>Mirzapur</strong> (Lekhania, Vijaygarh, Morhana Pahar, Bhaldaria, Kandakot), <strong>Manikpur</strong> (Banda).</span><span class="lang-hi"><strong>मिर्जापुर</strong> (लिखुनिया, विजयगढ़, मोरहना पहाड़, भलडरिया, कंडाकोट), <strong>मानिकपुर</strong> (बांदा)।</span></td>
        <td><span class="lang-en">First discovered in 1880 by Archibald Carlleyle and Cockburn (pre-dating Spain's Altamira cave discoveries). Painted in red ochre (Geru); famous scenes: wounded wild boar hunt (घायल सुअर का शिकार), rhinoceros hunt, deer herds, dance poses.</span><span class="lang-hi">1880 में आर्किबाल्ड कार्लाइल एवं कॉकबर्न द्वारा खोजी गईं (स्पेन की अल्तामीरा गुफाओं से भी पहले)। गेरू एवं कोयले से चित्रित; प्रसिद्ध दृश्य: घायल सूअर का शिकार, गैंडे का शिकार, हिरणों के झुंड एवं सामूहिक नृत्य।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mughal School of Painting (मुगल चित्रकला)</strong></span><span class="lang-hi"><strong>मुगल चित्रकला शैली</strong></span></td>
        <td><span class="lang-en">Agra, Fatehpur Sikri.</span><span class="lang-hi">आगरा, फतेहपुर सीकरी।</span></td>
        <td><span class="lang-en">Humayun brought Persian masters Mir Sayyid Ali and Abdus Samad. Akbar established the Imperial Tasvirkhana; 1400 folios of <em>Hamzanama (दास्तान-ए-अमीर हम्ज़ा)</em> painted on cloth. Jahangir's reign was the <strong class="theory-highlight">Golden Age of Mughal Painting</strong>; court masters: Ustad Mansur (specialist in flora/fauna - Siberian Crane, Dodo), Bishandas (portrait maestro), Abul Hasan.</span><span class="lang-hi">हुमायूँ ने फारसी चित्रकारों मीर सैय्यद अली व अब्बुस समद को आमंत्रित किया। अकबर ने शाही तस्वीरखाना स्थापित किया; सूती वस्त्र पर 1400 चित्रों का <em>हम्ज़ानामा</em> तैयार हुआ। जहांगीर का काल <strong class="theory-highlight">मुगल चित्रकला का स्वर्णकाल</strong> था; दरबारी उस्ताद: उस्ताद मंसूर (पशु-पक्षी विशेषज्ञ - साइबेरियाई सारस), बिशनदास (व्यक्ति चित्र/शबीह विशेषज्ञ), अबुल हसन।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Mathura &amp; Braj Sanjhi Art (सांझी कला)</strong></span><span class="lang-hi"><strong>सांझी कला (ब्रज-मथुरा)</strong></span></td>
        <td><span class="lang-en">Mathura, Vrindavan.</span><span class="lang-hi">मथुरा, वृंदावन।</span></td>
        <td><span class="lang-en">Intricate paper stenciling and dry color powdered art practiced by priests to decorate temple floors depicting Krishna's divine sports (Raas Leela).</span><span class="lang-hi">कागज की महीन कटाई (स्टेंसिल) द्वारा सूखे प्राकृतिक रंगों से मंदिरों के फर्श एवं जल पर बनाई जाने वाली राधा-कृष्ण लीलाओं की पारंपरिक लोककला।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Modern Wash Style &amp; Lucknow Arts College</strong></span><span class="lang-hi"><strong>लखनऊ वॉश शैली एवं कला महाविद्यालय</strong></span></td>
        <td><span class="lang-en">Lucknow Arts College (est. 1911).</span><span class="lang-hi">राजकीय कला एवं शिल्प महाविद्यालय, लखनऊ (1911)।</span></td>
        <td><span class="lang-en"><strong class="theory-highlight">Asit Kumar Haldar</strong> became the first Indian Principal in 1925, pioneering the *Lucknow Wash Technique* (blending Bengal wash with Persian lyricism). Notable UP artists: Ranvir Singh Bisht (famous <em>Blue Series</em> and <em>Hilly Village</em>), Bireswar Sen, Lalit Mohan Sen, Chaman Lal Thapar.</span><span class="lang-hi"><strong class="theory-highlight">असित कुमार हलदार</strong> 1925 में पहले भारतीय प्रधानाचार्य बने और <em>'लखनऊ वॉश शैली'</em> की नींव रखी। प्रमुख कलाकार: रणवीर सिंह बिष्ट (प्रसिद्ध <em>ब्लू सीरीज</em>), वीरेश्वर सेन, ललित मोहन सेन, चमन लाल थापर।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 3: Traditional Handicrafts, Textiles & GI Tags of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Traditional Handicrafts, Textiles &amp; GI Tags (हस्तशिल्प, वस्त्र एवं जीआई टैग)</span>
    <span class="lang-hi">2. उत्तर प्रदेश के प्रमुख हस्तशिल्प, वस्त्र उद्योग एवं जीआई टैग (जिलावार सूची)</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Handicraft / Industry</span><span class="lang-hi">हस्तशिल्प / कुटीर उद्योग</span></th>
        <th><span class="lang-en">Prominent City / District</span><span class="lang-hi">प्रमुख जिला / शहर</span></th>
        <th><span class="lang-en">Key Features &amp; Exam Highlights</span><span class="lang-hi">मुख्य विशेषताएँ एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Chikan Embroidery (चिकनकारी)</strong></span><span class="lang-hi"><strong>चिकनकारी हस्तशिल्प</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow</strong> (GI Tag)</span><span class="lang-hi"><strong>लखनऊ</strong> (GI टैग प्राप्त)</span></td>
        <td><span class="lang-en">Traditional delicate white-thread shadow work on muslin and cotton fabrics. Patronized by Noor Jahan and Awadh Nawabs. Features 32 distinct stitches: <em>Bakhiya, Tepchi, Phanda, Murri, Jali, Hathkathi</em>.</span><span class="lang-hi">मलमल व सूती वस्त्रों पर सफेद धागे से की जाने वाली छायाकारी कढ़ाई। नूरजहाँ व अवध के नवाबों का संरक्षण। प्रमुख 32 प्रकार के टांके: <em>बखिया, तेपची, फंदा, मुर्री, जाली, हाथकटी</em>।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Zari &amp; Zardozi (जरी-जरदोजी)</strong></span><span class="lang-hi"><strong>जरी-जरदोजी</strong></span></td>
        <td><span class="lang-en">Varanasi, Bareilly, Badaun, Shahjahanpur, Lucknow.</span><span class="lang-hi">वाराणसी, बरेली, बदायूँ, शाहजहाँपुर, लखनऊ।</span></td>
        <td><span class="lang-en">Heavy metallic embroidery using gold and silver threads, sequins (Salma-Sitara) on velvet and silk.</span><span class="lang-hi">मखमल व रेशम पर सोने-चांदी के तारों, सलमा-सितारों द्वारा की जाने वाली भारी नक्काशीदार कढ़ाई।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Banarasi Silk Brocade (बनारसी साड़ी)</strong></span><span class="lang-hi"><strong>बनारसी रेशमी साड़ी एवं ब्रोकेड</strong></span></td>
        <td><span class="lang-en"><strong>Varanasi</strong> (GI Tag)</span><span class="lang-hi"><strong>वाराणसी</strong> (GI टैग प्राप्त)</span></td>
        <td><span class="lang-en">World-renowned for gold/silver brocade (Zari), fine silk weave, compact weaving, floral and foliate motifs (Kalga and Bel), Jhallar borders. Varieties: Katan, Kora, Tanchoi, Jangla.</span><span class="lang-hi">सोने-चांदी की जरी के काम, महीन रेशम बुनाई, कलगा-बेल व बूटी डिजाइन हेतु विश्वप्रसिद्ध। प्रमुख प्रकार: कटान, कोरा, तंचोई, जंगला।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Hand-Knotted Carpets (कालीन उद्योग)</strong></span><span class="lang-hi"><strong>हस्तनिर्मित कालीन एवं दरी</strong></span></td>
        <td><span class="lang-en"><strong>Bhadohi</strong> (Carpet City / कालीन नगरी - GI Tag), <strong>Mirzapur</strong> (GI Tag).</span><span class="lang-hi"><strong>भदोही</strong> (कालीन नगरी - GI टैग), <strong>मिर्जापुर</strong> (GI टैग)।</span></td>
        <td><span class="lang-en">Bhadohi is the largest hand-knotted carpet weaving hub in South Asia, accounting for ~60% of India's carpet exports. Originated under Akbar's royal patronage.</span><span class="lang-hi">भदोही दक्षिण एशिया का सबसे बड़ा हस्तनिर्मित कालीन केंद्र है, जो भारत के कुल कालीन निर्यात का ~60% हिस्सा संभालता है। अकबर कालीन संरक्षण से प्रारंभ।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Brassware / Metal Handicrafts (पीतल उद्योग)</strong></span><span class="lang-hi"><strong>पीतल के बर्तन एवं हस्तशिल्प</strong></span></td>
        <td><span class="lang-en"><strong>Moradabad</strong> (Peetal Nagari - GI Tag).</span><span class="lang-hi"><strong>मुरादाबाद</strong> (पीतल नगरी - GI टैग)।</span></td>
        <td><span class="lang-en">Accounts for massive exports of engraved brass utensils, ornamental vases, artifacts, and idols. Famous for fine chisel engraving (*Naqqashi*).</span><span class="lang-hi">उत्कृष्ट नक्काशीदार पीतल के बर्तनों, फूलदानों व कलाकृतियों का भारी निर्यात केंद्र। 'पीतल नगरी' के उपनाम से प्रसिद्ध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Locks &amp; Hardware (ताला उद्योग)</strong></span><span class="lang-hi"><strong>ताला एवं हार्डवेयर उद्योग</strong></span></td>
        <td><span class="lang-en"><strong>Aligarh</strong> (Tala Nagari - GI Tag).</span><span class="lang-hi"><strong>अलीगढ़</strong> (ताला नगरी - GI टैग)।</span></td>
        <td><span class="lang-en">Supplies over 70% of India's brass, iron, and electronic locks and padlocks.</span><span class="lang-hi">भारत के 70% से अधिक तालों, पैडलॉक एवं हार्डवेयर का निर्माण केंद्र।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Glassware &amp; Bangles (कांच व चूड़ी उद्योग)</strong></span><span class="lang-hi"><strong>कांच के उत्पाद एवं चूड़ियाँ</strong></span></td>
        <td><span class="lang-en"><strong>Firozabad</strong> (Suhag Nagari - GI Tag).</span><span class="lang-hi"><strong>फिरोजाबाद</strong> (सुहाग नगरी / कांच नगरी - GI टैग)।</span></td>
        <td><span class="lang-en">Undisputed center of glass bangles, chandeliers, glassware, and laboratory apparatus in India.</span><span class="lang-hi">भारत में कांच की चूड़ियों, झूमरों, सजावटी सामान एवं कांच उद्योग का निर्विवाद केंद्र।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Ceramic Pottery (चीनी मिट्टी के बर्तन)</strong></span><span class="lang-hi"><strong>चीनी मिट्टी के बर्तन (सिरेमिक्स)</strong></span></td>
        <td><span class="lang-en"><strong>Khurja</strong> (Bulandshahr - GI Tag).</span><span class="lang-hi"><strong>खुर्जा</strong> (बुलंदशहर - GI टैग)।</span></td>
        <td><span class="lang-en">Known as the <em>"Ceramic City of India"</em>; famous for glazed artistic ceramic tableware, vases, and sanitary-ware.</span><span class="lang-hi"><em>'भारत का सिरेमिक नगर'</em>; कलात्मक चीनी मिट्टी के बर्तनों, फूलदानों व टाइलों के लिए प्रसिद्ध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Black Clay Pottery (काली मिट्टी के बर्तन)</strong></span><span class="lang-hi"><strong>काली मिट्टी के बर्तन</strong></span></td>
        <td><span class="lang-en"><strong>Nizamabad</strong> (Azamgarh - GI Tag).</span><span class="lang-hi"><strong>निजामाबाद</strong> (आजमगढ़ - GI टैग)।</span></td>
        <td><span class="lang-en">World-unique luster-black terracotta finished with kabiz slip and engraved with silvery zinc-lead alloy floral lines.</span><span class="lang-hi">विशिष्ट चमकदार काले मृद्भांड जिन पर जस्ता-पारे के लेप से चमकदार चांदी जैसी नक्काशी की जाती है।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Terracotta Craft (टेराकोटा शिल्प)</strong></span><span class="lang-hi"><strong>टेराकोटा शिल्प</strong></span></td>
        <td><span class="lang-en"><strong>Gorakhpur</strong> (GI Tag).</span><span class="lang-hi"><strong>गोरखपुर</strong> (GI टैग प्राप्त)।</span></td>
        <td><span class="lang-en">Artistic handcrafted baked-clay elephants, horses, Ganesha, and garden lamps without molds.</span><span class="lang-hi">बिना सांचे के हाथों से तैयार किए जाने वाले मिट्टी के हाथी, घोड़े, दीये, झूमर व मूर्तियां।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Wood Carving (काष्ठ नक्काशी)</strong></span><span class="lang-hi"><strong>काष्ठ नक्काशी हस्तशिल्प</strong></span></td>
        <td><span class="lang-en"><strong>Saharanpur</strong> (GI Tag), <strong>Nagina</strong> (Bijnor).</span><span class="lang-hi"><strong>सहारनपुर</strong> (GI टैग), <strong>नगीना</strong> (बिजनौर)।</span></td>
        <td><span class="lang-en">Saharanpur is world-famous for Sheesham wood screens, tables, and openwork carving. Nagina is renowned for ebony woodwork.</span><span class="lang-hi">सहारनपुर शीशम की लकड़ी की नक्काशीदार जाली, मेज व फर्नीचर हेतु विश्वविख्यात। नगीना आबनूस की लकड़ी के काम हेतु प्रसिद्ध।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Perfumery / Attar (इत्र उद्योग)</strong></span><span class="lang-hi"><strong>पारंपरिक इत्र (अत्तर) उद्योग</strong></span></td>
        <td><span class="lang-en"><strong>Kannauj</strong> (Perfume Capital - GI Tag).</span><span class="lang-hi"><strong>कन्नौज</strong> (इत्र नगरी / खुशबुओं का शहर - GI टैग)।</span></td>
        <td><span class="lang-en">Practicing ancient <em>Deg-Bhapka</em> hydro-distillation using copper stills on sandalwood base. Famous for <em>Mitti Attar</em> (scent of baked earth during first rain), Gulab, Shamama, Khas.</span><span class="lang-hi">प्राचीन <em>देग-भपका</em> आसवन पद्धति द्वारा चंदन तेल के आधार पर इत्र निर्माण। प्रसिद्ध: <em>मिट्टी का अत्तर</em> (सोंधी मिट्टी की खुशबू), गुलाब, शमामा, खस।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 4: Classical Music & Vocal Gharanas of Uttar Pradesh -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Classical Music Gharanas &amp; Maestro Traditions of UP</span>
    <span class="lang-hi">3. उत्तर प्रदेश के शास्त्रीय संगीत घराने एवं प्रमुख संगीतज्ञ (विस्तृत विवरण)</span>
  </div>

  <h3 class="theory-heading">
    <span class="lang-en">A. Banaras Gharana (बनारस संगीत घराना)</span>
    <span class="lang-hi">क. बनारस संगीत घराना</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Origin &amp; Founder:</span> Founded by <strong class="theory-highlight">Pandit Ram Sahai</strong> (1780-1826) who developed the Banaras Baaj (table style) suited for both accompaniment and solo performance.</span><span class="lang-hi"><span class="theory-highlight">उत्पत्ति एवं संस्थापक:</span> <strong class="theory-highlight">पंडित राम सहाय</strong> (1780-1826) द्वारा स्थापित, जिन्होंने संगत व स्वतंत्र वादन दोनों के अनुकूल बनारस बाज का विकास किया।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Thumri &amp; Semi-Classical Vocalists:</span> Banaras is the world capital of <strong class="theory-highlight">Purab Ang Thumri, Dadra, Chaiti, Kajari, and Tappa</strong>. Legendary maestros: <strong class="theory-highlight">Girija Devi</strong> (honored as <em>"Queen of Thumri" / थुमरी की रानी</em>, Padma Vibhushan), Rasoolan Bai, Siddheshwari Devi, Badi Moti Bai.</span><span class="lang-hi"><span class="theory-highlight">ठुमरी एवं उप-शास्त्रीय गायन:</span> बनारस <strong class="theory-highlight">पूरब अंग की ठुमरी, दादरा, चैती, कजरी एवं टप्पा</strong> का विश्व केंद्र है। विदुषी गायिकाएं: <strong class="theory-highlight">गिरिजा देवी</strong> (<em>"ठुमरी की मलिका"</em>, पद्म विभूषण), रसूलन बाई, सिद्धेश्वरी देवी, बड़ी मोती बाई।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Instrumental Maestros (वादक):</span></span><span class="lang-hi"><span class="theory-highlight">प्रमुख वाद्य संगीतज्ञ:</span></span>
      <ul class="theory-para">
        <li><span class="lang-en"><strong>Shehnai:</strong> <strong class="theory-highlight">Ustad Bismillah Khan</strong> (awarded Bharat Ratna in 2001; took Shehnai from temple courtyards to world concert stages).</span><span class="lang-hi"><strong>शहनाई:</strong> <strong class="theory-highlight">उस्ताद बिस्मिल्लाह खां</strong> (2001 में 'भारत रत्न'; शहनाई को मंदिर प्रांगण से विश्व मंच तक पहुंचाया)।</span></li>
        <li><span class="lang-en"><strong>Sitar:</strong> <strong class="theory-highlight">Pandit Ravi Shankar</strong> (awarded Bharat Ratna in 1999; disciple of Ustad Allauddin Khan).</span><span class="lang-hi"><strong>सितार:</strong> <strong class="theory-highlight">पंडित रवि शंकर</strong> (1999 में 'भारत रत्न'; बाबा अलाउद्दीन खां के शिष्य)।</span></li>
        <li><span class="lang-en"><strong>Tabla:</strong> Pandit Samta Prasad (Gudai Maharaj), Pandit Kishan Maharaj (Padma Vibhushan), Pandit Kanthe Maharaj.</span><span class="lang-hi"><strong>तबला:</strong> पंडित सामता प्रसाद (गुदई महाराज), पंडित किशन महाराज (पद्म विभूषण), पंडित कंठे महाराज।</span></li>
        <li><span class="lang-en"><strong>Sarangi:</strong> Pandit Gopal Mishra, Pandit Hanuman Prasad Mishra, Santosh Mishra.</span><span class="lang-hi"><strong>सारंगी:</strong> पंडित गोपाल मिश्र, पंडित हनुमान प्रसाद मिश्र, संतोष मिश्र।</span></li>
      </ul>
    </li>
  </ul>

  <h3 class="theory-heading">
    <span class="lang-en">B. Kirana Gharana (किराना घराना - शामली/मुजफ्फरनगर)</span>
    <span class="lang-hi">ख. किराना घराना (शामली/मुजफ्फरनगर)</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Origin:</span> Founded in the town of <strong class="theory-highlight">Kairana</strong> (now in Shamli district) by legendary Sarangi and Been master <strong class="theory-highlight">Ustad Abdul Karim Khan</strong> and <strong class="theory-highlight">Ustad Abdul Wahid Khan</strong>.</span><span class="lang-hi"><span class="theory-highlight">उत्पत्ति:</span> <strong class="theory-highlight">कैराना</strong> (वर्तमान शामली जिला) में सारंगी व बीन उस्ताद <strong class="theory-highlight">अब्दुल करीम खां</strong> तथा <strong class="theory-highlight">अब्दुल वाहिद खां</strong> द्वारा स्थापित।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Style:</span> Known for microtonal precision of Swaras (Swar Sadhana), emotional depth, and slow, meditative *Vilambit Khayal* development.</span><span class="lang-hi"><span class="theory-highlight">गायन शैली:</span> स्वरों की सूक्ष्म शुद्धता (स्वर साधना), भावात्मक गहराई एवं अत्यंत मंद गति में विलंबित ख्याल गायन।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Doyen Maestros:</span> <strong class="theory-highlight">Pandit Bhimsen Joshi</strong> (awarded Bharat Ratna in 2008), Gangubai Hangal, Sawai Gandharva, Prabha Atre.</span><span class="lang-hi"><span class="theory-highlight">शीर्ष गायक:</span> <strong class="theory-highlight">पंडित भीमसेन जोशी</strong> (2008 में 'भारत रत्न'), गंगूबाई हंगल, सवाई गंधर्व, प्रभा अत्रे।</span></li>
  </ul>

  <h3 class="theory-heading">
    <span class="lang-en">C. Agra Gharana &amp; Other Key Vocal Schools (आगरा घराना एवं अन्य घराने)</span>
    <span class="lang-hi">ग. आगरा घराना एवं अन्य प्रमुख संगीत घराने</span>
  </h3>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Agra Gharana (रंगीला घराना):</span> Traces origin to Haji Sujan Khan (contemporary of Tansen). Revolutionized by <strong class="theory-highlight">Ustad Faiyaz Khan</strong> (awarded title <em>"Aftab-e-Mousiqui" / संगीत का सूर्य</em>). Characterized by open-throated, powerful voice projection (*Bol-Taans*, *Nom-Tom Alap*), blending Dhrupad and Khayal.</span><span class="lang-hi"><span class="theory-highlight">आगरा घराना (रंगीला घराना):</span> हाजी सुजान खां (तानसेन के समकालीन) से प्रारंभ। <strong class="theory-highlight">उस्ताद फैयाज खां</strong> (उपाधि: <em>'आफताब-ए-मौसकी'</em>) द्वारा चरमोत्कर्ष। खुले गले का जोरदार गायन, बोल-तान, नोम-तोम आलाप, ध्रुपद-धमार एवं ख्याल का अद्वितीय संगम।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Atrauli Gharana (अतरौली घराना, अलीगढ़):</span> Founded by Ustad Alladiya Khan; associated with intricate rhythmic structures.</span><span class="lang-hi"><span class="theory-highlight">अतरौली घराना (अलीगढ़):</span> उस्ताद अल्लादिया खां द्वारा स्थापित; जटिल रागों व लयकारी हेतु प्रसिद्ध।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">Shahjahanpur Sarod Gharana:</span> Key center for Sarod mastery (Ustad Enayat Ali Khan).</span><span class="lang-hi"><span class="theory-highlight">शाहजहाँपुर सरोद घराना:</span> सरोद वादन का ऐतिहासिक केंद्र (उस्ताद इनायत अली खां)।</span></li>
  </ul>
</div>

<!-- Card 5: Kathak Classical Dance & The Lucknow Gharana -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Kathak Classical Dance of Uttar Pradesh (कथक शास्त्रीय नृत्य एवं लखनऊ घराना)</span>
    <span class="lang-hi">4. कथक शास्त्रीय नृत्य एवं लखनऊ घराना (उत्तर भारत का एकमात्र शास्त्रीय नृत्य)</span>
  </div>
  <p class="theory-para">
    <span class="lang-en"><strong class="theory-highlight">Kathak</strong> is the <strong class="theory-highlight">only classical dance style native to North India / Uttar Pradesh</strong>. Derived from the Sanskrit word <em>'Katha'</em> (story), its ancient exponents were traveling temple storytellers (*Kathakas*) who enacted epics with mime, hand gestures, and dance:</span>
    <span class="lang-hi"><strong class="theory-highlight">कथक</strong> उत्तर भारत / उत्तर प्रदेश का <strong class="theory-highlight">एकमात्र शास्त्रीय नृत्य</strong> है। 'कथा' शब्द से व्युत्पन्न, इसकी प्राचीन परंपरा मंदिर के कथाकारों (कथक) से जुड़ी है: <em>"कथा कहे सो कथक कहावे"</em>:</span>
  </p>
  <ul class="theory-para">
    <li><span class="lang-en"><span class="theory-highlight">Royal Patronage of Awadh:</span> Reached its artistic zenith in Lucknow under the passionate patronage of <strong class="theory-highlight">Nawab Wajid Ali Shah</strong> (pen name <em>'Akhtar Piya'</em>). The Nawab himself trained in Kathak, composed Thumris (e.g. <em>"Babul Mora Naihar Chhooto Jaye"</em>), and institutionalized the dance in his court (*Parikhana*).</span><span class="lang-hi"><span class="theory-highlight">अवध का शाही संरक्षण:</span> लखनऊ में नवाब <strong class="theory-highlight">वाजिद अली शाह</strong> (उपनाम <em>'अख्तर पिया'</em>) के काल में कथक को अभूतपूर्व संरक्षण मिला। नवाब ने स्वयं कथक सीखा, प्रसिद्ध ठुमरी <em>"बाबुल मोरा नैहर छूटो जाय"</em> रची, और 'परीखाना' में नृत्यांगनाओं को प्रशिक्षण दिलाया।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">The Legendary Kalka-Bindadin Dynasty:</span> Founded in the Lucknow court by brothers <strong class="theory-highlight">Pandit Kalka Prasad</strong> and <strong class="theory-highlight">Pandit Bindadin Maharaj</strong> (Thakur Prasad's sons). Bindadin composed thousands of Thumris and Bhajans tailored for *Bhava* (emotional expression).</span><span class="lang-hi"><span class="theory-highlight">कालका-बिंदादीन परंपरा:</span> लखनऊ घराने को विश्व पटल पर स्थापित करने का श्रेय सगे भाइयों <strong class="theory-highlight">पंडित कालका प्रसाद</strong> एवं <strong class="theory-highlight">पंडित बिंदादीन महाराज</strong> को है। बिंदादीन ने भाव प्रदर्शन हेतु हजारों ठुमरियों व पदों की रचना की।</span></li>
    <li><span class="lang-en"><span class="theory-highlight">The Maharaj Maestros:</span></span><span class="lang-hi"><span class="theory-highlight">महाराज बंधु एवं वंश परंपरा:</span></span>
      <ul class="theory-para">
        <li><span class="lang-en"><strong>Achchan Maharaj:</strong> Eldest son of Kalka Prasad; master of complex *Tala* (rhythm) and *Bhava*.</span><span class="lang-hi"><strong>अच्छन महाराज:</strong> कालका प्रसाद के ज्येष्ठ पुत्र; भाव एवं लय के अद्वितीय सम्राट।</span></li>
        <li><span class="lang-en"><strong>Lachhu Maharaj:</strong> Renowned choreographer for Bollywood classics (*Mughal-e-Azam*, *Pakeezah*).</span><span class="lang-hi"><strong>लच्छू महाराज:</strong> प्रसिद्ध नृत्याचार्य, फिल्मों (मुगल-ए-आजम, पाकीजा) में कालजयी कथक नृत्य निर्देशन।</span></li>
        <li><span class="lang-en"><strong>Shambhu Maharaj:</strong> Sangeet Natak Akademi Fellow; undisputed master of seated Thumri Abhinaya.</span><span class="lang-hi"><strong>शंभू महाराज:</strong> संगीत नाटक अकादमी रत्न; बैठकर गाई जाने वाली ठुमरी पर भाव अभिनय के बेजोड़ उस्ताद।</span></li>
        <li><span class="lang-en"><strong>Pandit Birju Maharaj (1938-2022):</strong> Son of Achchan Maharaj; awarded <strong class="theory-highlight">Padma Vibhushan (1986)</strong>. Elevated Kathak to international acclaim; legendary choreographer, poet, singer, and percussionist.</span><span class="lang-hi"><strong>पंडित बिरजू महाराज (1938-2022):</strong> अच्छन महाराज के पुत्र; <strong class="theory-highlight">पद्म विभूषण (1986)</strong>। कथक को वैश्विक पहचान दिलाने वाले युगद्रष्टा; नृत्य गुरु, कवि, गायक एवं तबला वादक।</span></li>
      </ul>
    </li>
    <li><span class="lang-en"><span class="theory-highlight">Banaras Kathak Gharana:</span> Founded by <strong class="theory-highlight">Janaki Prasad</strong>. Emphasizes clean *Natwari Bol* (syllables imitating nature and Krishna's dance) rather than Pakhawaj/Tabla bols, robust footwork (*Tatkar*), and Chakkar (spins) executed from both sides. Prominent exponents: Sitara Devi (hailed by Rabindranath Tagore as <em>"Kathak Queen" / नृत्य सम्राज्ञी</em>).</span><span class="lang-hi"><span class="theory-highlight">बनारस कथक घराना:</span> <strong class="theory-highlight">जानकी प्रसाद</strong> द्वारा स्थापित। तबले के बोलों के बजाय शुद्ध <em>नटवरी बोलों</em> पर आधारित, जोरदार पद संचालन (तत्कार) तथा दोनों ओर से चक्कर। शीर्ष नृत्यांगना: <strong class="theory-highlight">सितारा देवी</strong> (रवींद्रनाथ टैगोर ने इन्हें <em>"नृत्य सम्राज्ञी"</em> की उपाधि दी थी)।</span></li>
  </ul>
</div>

<!-- Card 6: Cultural Institutions, Academies & Museums of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. State Cultural Academies, Institutes &amp; Museums in UP</span>
    <span class="lang-hi">5. उत्तर प्रदेश की प्रमुख सांस्कृतिक अकादमियाँ, संस्थान एवं संग्रहालय</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Institution / Academy</span><span class="lang-hi">संस्थान / अकादमी</span></th>
        <th><span class="lang-en">Location &amp; Est. Year</span><span class="lang-hi">स्थान एवं स्थापना वर्ष</span></th>
        <th><span class="lang-en">Key Mandate &amp; Exam Highlights</span><span class="lang-hi">मुख्य कार्य एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en"><strong>Bhatkhande Sanskriti Vishwavidyalaya</strong></span><span class="lang-hi"><strong>भातखंडे संस्कृति विश्वविद्यालय</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (1926)</strong></span><span class="lang-hi"><strong>लखनऊ (1926)</strong></span></td>
        <td><span class="lang-en">Founded in 1926 by Pt. Vishnu Narayan Bhatkhande as <em>Marris College of Hindustani Music</em>. Renamed Bhatkhande Music Institute; upgraded to a full-fledged <strong>State Cultural University in 2022</strong>. Premier classical music university.</span><span class="lang-hi">पं. विष्णु नारायण भातखंडे द्वारा 1926 में <em>'मैरिस कॉलेज'</em> के रूप में स्थापित। 1966 में भातखंडे संगीत संस्थान बना; <strong class="theory-highlight">2022 में राज्य संस्कृति विश्वविद्यालय</strong> का दर्जा दिया गया।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>State Lalit Kala Akademi (राज्य ललित कला अकादमी)</strong></span><span class="lang-hi"><strong>राज्य ललित कला अकादमी</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (8 Feb 1962)</strong></span><span class="lang-hi"><strong>लखनऊ (8 फरवरी 1962)</strong></span></td>
        <td><span class="lang-en">Autonomous body promoting fine arts, paintings, sculptures, and art exhibitions across UP.</span><span class="lang-hi">उत्तर प्रदेश में दृश्य कलाओं, चित्रकला, मूर्तिकला एवं कला प्रदर्शनियों को बढ़ावा देने वाली स्वायत्त संस्था।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>UP Sangeet Natak Akademi (संगीत नाटक अकादमी)</strong></span><span class="lang-hi"><strong>उ.प्र. संगीत नाटक अकादमी</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (13 Nov 1963)</strong></span><span class="lang-hi"><strong>लखनऊ (13 नवंबर 1963)</strong></span></td>
        <td><span class="lang-en">Apex state body preserving and promoting classical music, folk music, classical and folk dance, and theater traditions.</span><span class="lang-hi">शास्त्रीय संगीत, लोक संगीत, लोक नृत्य एवं रंगमंच के संरक्षण व संवर्धन हेतु राज्य की शीर्ष संस्था।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Bhartendu Natya Akademi (भारतेन्दु नाट्य अकादमी)</strong></span><span class="lang-hi"><strong>भारतेन्दु नाट्य अकादमी (BNA)</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (Aug 1975)</strong></span><span class="lang-hi"><strong>लखनऊ (अगस्त 1975)</strong></span></td>
        <td><span class="lang-en">Dedicated professional drama and theater training academy; modeled after the National School of Drama (NSD).</span><span class="lang-hi">राष्ट्रीय नाट्य विद्यालय (NSD) की तर्ज पर स्थापित नाट्य कला एवं रंगमंच प्रशिक्षण संस्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>National Kathak Sansthan (राष्ट्रीय कथक संस्थान)</strong></span><span class="lang-hi"><strong>राष्ट्रीय कथक संस्थान</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (1989)</strong></span><span class="lang-hi"><strong>लखनऊ (1989)</strong></span></td>
        <td><span class="lang-en">Autonomous institute dedicated to teaching, research, and documentation of Kathak classical dance traditions.</span><span class="lang-hi">कथक शास्त्रीय नृत्य के शिक्षण, शोध, दस्तावेजीकरण एवं प्रसार हेतु समर्पित स्वायत्त संस्थान।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>State Museum, Lucknow (राज्य संग्रहालय, लखनऊ)</strong></span><span class="lang-hi"><strong>राज्य संग्रहालय, लखनऊ</strong></span></td>
        <td><span class="lang-en"><strong>Lucknow (1863)</strong></span><span class="lang-hi"><strong>लखनऊ (1863)</strong></span></td>
        <td><span class="lang-en">Oldest and largest multi-disciplinary museum in UP (located in Banarasi Bagh / Zoo). Famous for Gupta sculptures, Mathura art, Egyptian mummy, and rare coin hoards.</span><span class="lang-hi">उ.प्र. का सबसे पुराना एवं विशालतम बहु-विषयक संग्रहालय (बनारसी बाग में स्थित)। गुप्त मूर्तियों, कुषाण कला, मिस्र की ममी एवं प्राचीन सिक्कों का खजाना।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Government Museum, Mathura (राजकीय संग्रहालय)</strong></span><span class="lang-hi"><strong>राजकीय संग्रहालय, मथुरा</strong></span></td>
        <td><span class="lang-en"><strong>Mathura (1874)</strong></span><span class="lang-hi"><strong>मथुरा (1874)</strong></span></td>
        <td><span class="lang-en">World's richest repository of Kushana and Gupta red sandstone sculptures, Buddhist icons, and Jain Ayagapatas. Founded by collector F.S. Growse.</span><span class="lang-hi">कुषाण एवं गुप्तकालीन लाल बलुआ पत्थर की मूर्तियों व बौद्ध-जैन कलाकृतियों का विश्व का सबसे समृद्ध संग्रहालय।</span></td>
      </tr>
      <tr>
        <td><span class="lang-en"><strong>Bharat Kala Bhavan (भारत कला भवन)</strong></span><span class="lang-hi"><strong>भारत कला भवन (BHU)</strong></span></td>
        <td><span class="lang-en"><strong>BHU, Varanasi (1920)</strong></span><span class="lang-hi"><strong>बीएचयू, वाराणसी (1920)</strong></span></td>
        <td><span class="lang-en">Famous university museum established by Rai Krishnadasa; houses exquisite Mughal miniatures, textiles, and historical manuscripts.</span><span class="lang-hi">राय कृष्णदास द्वारा स्थापित विख्यात कला संग्रहालय; मुगल लघुचित्रों, बनारसी वस्त्रों व दुर्लभ पांडुलिपियों का अनूठा संग्रह।</span></td>
      </tr>
    </tbody>
  </table>
</div>

<!-- Card 7: Master One-Liner Art Quick Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Master Art &amp; Craft One-Liner Quick Revision Matrix</span>
    <span class="lang-hi">6. उत्तर प्रदेश की कला एवं शिल्प: एक नज़र में त्वरित परीक्षा सार</span>
  </div>
  <table class="theory-overflow-mb">
    <thead>
      <tr>
        <th><span class="lang-en">Craft / Art Fact Question</span><span class="lang-hi">कला / हस्तशिल्प संबंधी प्रश्न</span></th>
        <th><span class="lang-en">Exact Answer &amp; Key Exam Fact</span><span class="lang-hi">सटीक उत्तर एवं परीक्षा बिंदु</span></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><span class="lang-en">Prehistoric rock paintings discovery in UP</span><span class="lang-hi">उ.प्र. में प्रागैतिहासिक शैलचित्रों की खोज</span></td>
        <td><span class="lang-en"><strong>Mirzapur (discovered 1880 by Carlleyle &amp; Cockburn)</strong></span><span class="lang-hi"><strong>मिर्जापुर (1880 में कार्लाइल एवं कॉकबर्न द्वारा)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Only Classical Dance of North India / UP</span><span class="lang-hi">उत्तर भारत / उत्तर प्रदेश का एकमात्र शास्त्रीय नृत्य</span></td>
        <td><span class="lang-en"><strong>Kathak (कथक)</strong></span><span class="lang-hi"><strong>कथक</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Nawab who patronized Kathak &amp; composed Thumri</span><span class="lang-hi">कथक को संरक्षण देने वाले व ठुमरी रचयिता नवाब</span></td>
        <td><span class="lang-en"><strong>Nawab Wajid Ali Shah (pen name: Akhtar Piya)</strong></span><span class="lang-hi"><strong>नवाब वाजिद अली शाह (उपनाम: अख्तर पिया)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Famous Kathak maestro awarded Padma Vibhushan (1986)</span><span class="lang-hi">पद्म विभूषण (1986) से सम्मानित महान कथक नर्तक</span></td>
        <td><span class="lang-en"><strong>Pandit Birju Maharaj</strong> (Lucknow Kalka-Bindadin Gharana)</span><span class="lang-hi"><strong>पंडित बिरजू महाराज</strong> (लखनऊ कालका-बिंदादीन घराना)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Dancer titled "Kathak Samragyi" by Tagore</span><span class="lang-hi">टैगोर द्वारा "कथक सम्राज्ञी" की उपाधि पाने वाली नर्तकी</span></td>
        <td><span class="lang-en"><strong>Sitara Devi (Banaras Gharana)</strong></span><span class="lang-hi"><strong>सितारा देवी (बनारस घराना)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">City known as "Peetal Nagari" (Brass City)</span><span class="lang-hi">"पीतल नगरी" के नाम से प्रसिद्ध शहर</span></td>
        <td><span class="lang-en"><strong>Moradabad (मुरादाबाद - GI Tag)</strong></span><span class="lang-hi"><strong>मुरादाबाद</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">City known as "Suhag Nagari" (Glass City)</span><span class="lang-hi">"सुहाग नगरी" / "कांच नगरी" उपनाम से प्रसिद्ध जिला</span></td>
        <td><span class="lang-en"><strong>Firozabad (फिरोजाबाद - GI Tag)</strong></span><span class="lang-hi"><strong>फिरोजाबाद</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">City known as "Carpet City" of South Asia</span><span class="lang-hi">दक्षिण एशिया की "कालीन नगरी" किसे कहते हैं?</span></td>
        <td><span class="lang-en"><strong>Bhadohi (भदोही - GI Tag)</strong></span><span class="lang-hi"><strong>भदोही</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">City known as "Perfume Capital" (इत्र नगरी)</span><span class="lang-hi">"इत्र नगरी" / खुशबुओं का शहर</span></td>
        <td><span class="lang-en"><strong>Kannauj (कन्नौज - GI Tag)</strong></span><span class="lang-hi"><strong>कन्नौज</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Black Clay Pottery GI Tag district</span><span class="lang-hi">काली मिट्टी के बर्तनों (ब्लैक पॉटरी) का जीआई टैग जिला</span></td>
        <td><span class="lang-en"><strong>Nizamabad, Azamgarh (निजामाबाद, आजमगढ़)</strong></span><span class="lang-hi"><strong>निजामाबाद, आजमगढ़</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Ceramic Pottery GI Tag town</span><span class="lang-hi">चीनी मिट्टी के बर्तनों (सिरेमिक्स) हेतु प्रसिद्ध</span></td>
        <td><span class="lang-en"><strong>Khurja, Bulandshahr (खुर्जा, बुलंदशहर)</strong></span><span class="lang-hi"><strong>खुर्जा, बुलंदशहर</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Wood Carving GI Tag district</span><span class="lang-hi">काष्ठ नक्काशी शिल्प का जीआई टैग जिला</span></td>
        <td><span class="lang-en"><strong>Saharanpur (सहारनपुर)</strong></span><span class="lang-hi"><strong>सहारनपुर</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Terracotta Craft GI Tag center</span><span class="lang-hi">टेराकोटा शिल्प का जीआई टैग केंद्र</span></td>
        <td><span class="lang-en"><strong>Gorakhpur (गोरखपुर)</strong></span><span class="lang-hi"><strong>गोरखपुर</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Shehnai maestro awarded Bharat Ratna (2001)</span><span class="lang-hi">भारत रत्न (2001) से सम्मानित शहनाई वादक</span></td>
        <td><span class="lang-en"><strong>Ustad Bismillah Khan (Banaras)</strong></span><span class="lang-hi"><strong>उस्ताद बिस्मिल्लाह खां (बनारस)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Sitar maestro awarded Bharat Ratna (1999)</span><span class="lang-hi">भारत रत्न (1999) से सम्मानित सितार वादक</span></td>
        <td><span class="lang-en"><strong>Pandit Ravi Shankar (Banaras Gharana)</strong></span><span class="lang-hi"><strong>पंडित रवि शंकर (बनारस घराना)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Vocalist hailed as "Queen of Thumri" (ठुमरी की रानी)</span><span class="lang-hi">"ठुमरी की रानी" उपनाम से विख्यात शास्त्रीय गायिका</span></td>
        <td><span class="lang-en"><strong>Girija Devi (बनारस घराना)</strong></span><span class="lang-hi"><strong>गिरिजा देवी (बनारस घराना)</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Kirana Gharana founded in which district</span><span class="lang-hi">किराना घराने की स्थापना किस जिले में हुई?</span></td>
        <td><span class="lang-en"><strong>Kairana, Shamli district</strong> (by Ustad Abdul Karim Khan)</span><span class="lang-hi"><strong>कैराना, शामली जिला</strong> (उस्ताद अब्दुल करीम खां द्वारा)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Year of establishment of Marris College / Bhatkhande</span><span class="lang-hi">मैरिस कॉलेज / भातखंडे संगीत संस्थान की स्थापना वर्ष</span></td>
        <td><span class="lang-en"><strong>1926</strong> (by Pt. V.N. Bhatkhande at Lucknow; State University in 2022)</span><span class="lang-hi"><strong>1926</strong> (पं. वी.एन. भातखंडे द्वारा लखनऊ में; 2022 में राज्य वि.वि.)</span></td>
      </tr>
      <tr>
        <td><span class="lang-en">State Lalit Kala Akademi established in</span><span class="lang-hi">राज्य ललित कला अकादमी की स्थापना कब और कहाँ हुई?</span></td>
        <td><span class="lang-en"><strong>1962, Lucknow</strong></span><span class="lang-hi"><strong>1962, लखनऊ</strong></span></td>
      </tr>
      <tr>
        <td><span class="lang-en">Bhartendu Natya Akademi established in</span><span class="lang-hi">भारतेन्दु नाट्य अकादमी की स्थापना वर्ष</span></td>
        <td><span class="lang-en"><strong>1975, Lucknow</strong></span><span class="lang-hi"><strong>1975, लखनऊ</strong></span></td>
      </tr>
    </tbody>
  </table>
</div>

</div>
"""

def main():
    target_file = os.path.join("upsssc-up-gk", "art", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_art_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
