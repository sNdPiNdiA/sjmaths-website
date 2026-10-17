import os
import re

def build_regional_languages_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Linguistic Spectrum, Dialect Zones &amp; Literary Sansthans of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का भाषाई परिदृश्य, बोली क्षेत्र एवं भाषा संस्थान</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Languages & Dialects of Uttar Pradesh] --> B[Official State Languages]
    A --> C[Western Hindi Shauraseni]
    A --> D[Eastern Hindi Ardhamagadhi]
    A --> E[Bihari Hindi Magadhi]
    A --> F[Urdu & Ganga-Jamuni Tehzeeb]
    A --> G[Language Sansthans & Academies]

    B --> B1[1st Official: Hindi Devanagari 1951 | Mandatory 1968]
    B --> B2[2nd Official: Urdu 1989 Amendment Act]

    C --> C1[Khari Boli Kauravi: Meerut, Saharanpur, Bijnor | Modern Hindi Base]
    C --> C2[Braj Bhasha: Mathura, Agra, Aligarh | Surdas & Raskhan]
    C --> C3[Kannauji: Kannauj, Farrukhabad, Etawah | O-karanta Endings]
    C --> C4[Bundeli: Jhansi, Lalitpur, Banda, Mahoba | Alha-Udal & Isuri]

    D --> D1[Awadhi: Ayodhya, Lucknow, Prayagraj | Tulsidas & Jayasi]
    D --> D2[Bagheli: Mirzapur, Sonbhadra, Trans-Yamuna Prayagraj]

    E --> E1[Bhojpuri: Varanasi, Gorakhpur, Ballia, Ghazipur | Largest Spoken]
    E --> E2[Folk Icon: Bhikhari Thakur Shakespeare of Bhojpuri | Bidesiya]

    F --> F1[Dabistan-e-Lucknow: Mir Anees, Dabeer, Atish, Nasikh]
    F --> F2[Luminaries: Ghalib Agra 1797, Firaq Gorakhpur Jnanpith 1969]

    G --> G1[UP Hindi Sansthan: 1976 Lucknow | Bharat Bharati Award]
    G --> G2[UP Sanskrit Sansthan: 1976 | Vishwabharati Award]
    G --> G3[Nagari Pracharini Sabha: 1893 Kashi | Hindustani Academy: 1927]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की भाषाएं एवं बोलियां] --> B[राजकीय भाषाएं]
    A --> C[पश्चिमी हिंदी शौरसेनी अपभ्रंश]
    A --> D[पूर्वी हिंदी अर्धमागधी अपभ्रंश]
    A --> E[बिहारी हिंदी मागधी अपभ्रंश]
    A --> F[उर्दू एवं गंगा-जमुनी तहजीब]
    A --> G[भाषा अकादमी एवं संस्थान]

    B --> B1[प्रथम राजभाषा: हिंदी देवनागरी 1951 | अनिवार्य 1968]
    B --> B2[द्वितीय राजभाषा: उर्दू 1989 संशोधन अधिनियम]

    C --> C1[खड़ी बोली कौरवी: मेरठ, सहारनपुर, बिजनौर | मानक हिंदी का आधार]
    C --> C2[ब्रजभाषा: मथुरा, आगरा, अलीगढ़ | सूरदास व रसखान]
    C --> C3[कन्नौजी: कन्नौज, फर्रुखाबाद, इटावा | ओ-कारान्त ध्वनियां]
    C --> C4[बुंदेली: झांसी, ललितपुर, बांदा, महोबा | आल्हा-ऊदल व ईसुरी]

    D --> D1[अवधी: अयोध्या, लखनऊ, प्रयागराज | तुलसीदास व जायसी]
    D --> D2[बघेली: मिर्जापुर, सोनभद्र, यमुनापार प्रयागराज]

    E --> E1[भोजपुरी: वाराणसी, गोरखपुर, बलिया, गाजीपुर | सर्वाधिक बोली जाने वाली]
    E --> E2[लोक नायक: भिखारी ठाकुर भोजपुरी के शेक्सपियर | बिदेसिया]

    F --> F1[दबिस्तान-ए-लखनऊ: मीर अनीस, दबीर, आतिश, नासिख]
    F --> F2[महान शायर: गालिब आगरा 1797, फिराक गोरखपुर ज्ञानपीठ 1969]

    G --> G1[यूपी हिंदी संस्थान: 1976 लखनऊ | भारत भारती पुरस्कार]
    G --> G2[यूपी संस्कृत संस्थान: 1976 | विश्वभारती पुरस्कार]
    G --> G3[नागरी प्रचारिणी सभा: 1893 काशी | हिंदुस्तानी एकेडमी: 1927]
    </div>
  </div>
</div>

<!-- Card 2: Official Languages & Statutory Framework -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Official Languages of Uttar Pradesh &amp; Constitutional Status</span>
    <span class="lang-hi">1. उत्तर प्रदेश की राजभाषाएं एवं संवैधानिक स्थिति</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Constitutional Enactment (Article 345 &amp; 347):</strong> Under Article 345, the state legislature has constitutional authority to adopt one or more languages in use in the state for official government transactions.</span>
        <span class="lang-hi"><strong>संवैधानिक प्रावधान (अनुच्छेद 345 एवं 347):</strong> संविधान के अनुच्छेद 345 के तहत राज्य विधानमंडल को राज्य में प्रयुक्त होने वाली भाषाओं में से किसी एक या अधिक को आधिकारिक कार्यों हेतु अपनाने का अधिकार है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>First Official Language - Hindi (प्रथम राजभाषा - हिंदी):</strong>
          <br>&bull; <em>Statutory Enactment:</em> Adopted as the official language of the state under the <strong>UP Official Language Act 1951 (उत्तर प्रदेश राजभाषा अधिनियम 1951)</strong> in Devanagari script.
          <br>&bull; <em>Mandatory Implementation:</em> On <strong>26 January 1968</strong>, the Government of UP issued a statutory notification making the use of Hindi completely <strong>mandatory for all official government transactions, gazette notifications, and administrative correspondence</strong>.</span>
        <span class="lang-hi"><strong>प्रथम राजभाषा - हिंदी:</strong>
          <br>&bull; <em>विधिक अंगीकार:</em> <strong>उत्तर प्रदेश राजभाषा अधिनियम 1951</strong> के तहत देवनागरी लिपि में हिंदी को राज्य की आधिकारिक भाषा घोषित किया गया।
          <br>&bull; <em>अनिवार्य क्रियान्वयन:</em> <strong>26 जनवरी 1968</strong> को एक शासकीय अधिसूचना द्वारा सभी सरकारी कार्यालयों, राजपत्रों और प्रशासनिक पत्राचार में हिंदी का प्रयोग <strong>पूर्णतः अनिवार्य</strong> कर दिया गया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Second Official Language - Urdu (द्वितीय राजभाषा - उर्दू):</strong>
          <br>&bull; <em>Statutory Amendment:</em> Declared as the <strong>second official language of Uttar Pradesh</strong> through the <strong>UP Official Language (Amendment) Act 1989</strong> (promulgated in October 1989 during the tenure of Chief Minister N.D. Tiwari).
          <br>&bull; <em>Permitted Official Uses:</em> Receiving petitions and memorandums in Urdu, publishing significant state laws, rules, and government orders in Urdu, publishing electoral rolls, and registration of documents.</span>
        <span class="lang-hi"><strong>द्वितीय राजभाषा - उर्दू:</strong>
          <br>&bull; <em>विधिक संशोधन:</em> <strong>उत्तर प्रदेश राजभाषा (संशोधन) अधिनियम 1989</strong> के माध्यम से उर्दू को राज्य की <strong>द्वितीय राजभाषा</strong> घोषित किया गया (अक्टूबर 1989 में मुख्यमंत्री नारायण दत्त तिवारी के कार्यकाल में)।
          <br>&bull; <em>अनुमन्य आधिकारिक उपयोग:</em> उर्दू में आवेदन-पत्र प्राप्त करना, महत्वपूर्ण सरकारी नियमों, अधिनियमों व शासनादेशों का उर्दू में प्रकाशन, मतदाता सूचियों का प्रकाशन तथा दस्तावेजों का निबंधन।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Western Hindi Branch (Shauraseni Apabhramsha) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Western Hindi Branch (Shauraseni Apabhramsha): Khari Boli, Braj, Kannauji &amp; Bundeli</span>
    <span class="lang-hi">2. पश्चिमी हिंदी शाखा (शौरसेनी अपभ्रंश): खड़ी बोली, ब्रजभाषा, कन्नौजी एवं बुंदेली</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. Khari Boli / Kauravi (खड़ी बोली / कौरवी):</strong>
          <br>&bull; <em>Nomenclature &amp; Origin:</em> Term 'Kauravi' was coined by <strong>Mahapandit Rahul Sankrityayan</strong> after the ancient Kuru kingdom; developed from northern Shauraseni Apabhramsha.
          <br>&bull; <em>National Importance:</em> Forms the grammatical base and phonetic foundation of <strong>Modern Standard Hindi (मानक हिंदी)</strong> and Urdu.
          <br>&bull; <em>Districts:</em> Meerut, Saharanpur, Muzaffarnagar, Shamli, Baghpat, Ghaziabad, Hapur, Gautam Buddha Nagar, Bulandshahr, Bijnor, Moradabad, Amroha, and Rampur.
          <br>&bull; <em>Pioneer Poet:</em> <strong>Amir Khusro (1253-1325)</strong>, born in <strong>Patiyali (Kasganj district)</strong>, was the first poet to deliberately compose poetry, riddles (Pahelis), and songs (Mukaris) in Khari Boli / Hindavi.</span>
        <span class="lang-hi"><strong>1. खड़ी बोली / कौरवी:</strong>
          <br>&bull; <em>नामकरण व उद्गम:</em> प्राचीन कुरु जनपद के आधार पर 'कौरवी' नाम <strong>महापंडित राहुल सांकृत्यायन</strong> ने दिया; उत्तरी शौरसेनी अपभ्रंश से विकसित।
          <br>&bull; <em>राष्ट्रीय महत्व:</em> यह <strong>आधुनिक मानक हिंदी</strong> तथा उर्दू की व्याकरणिक व ध्वन्यात्मक रीढ़ है।
          <br>&bull; <em>विस्तार जिले:</em> मेरठ, सहारनपुर, मुजफ्फरनगर, शामली, बागपत, गाजियाबाद, हापुड़, गौतमबुद्ध नगर, बुलंदशहर, बिजनौर, मुरादाबाद, अमरोहा एवं रामपुर।
          <br>&bull; <em>प्रथम प्रयोक्ता:</em> <strong>अमीर खुसरो (1253-1325)</strong>, जिनका जन्म <strong>पटियाली (कासगंज जिला)</strong> में हुआ था; उन्होंने सर्वप्रथम खड़ी बोली (हिंदवी) में पहेलियां, मुकरियां और दोहे रचे।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Braj Bhasha (ब्रजभाषा):</strong>
          <br>&bull; <em>Origin &amp; Nature:</em> Developed from central Shauraseni Apabhramsha; predominant literary vehicle of medieval India from 15th to late 19th century.
          <br>&bull; <em>Districts:</em> Mathura, Agra, Aligarh, Hathras, Firozabad, Etah, Kasganj, Mainpuri, and parts of Budaun and Bareilly.
          <br>&bull; <em>Great Literati:</em> <strong>Surdas</strong> (Sur Sagar, Sur Saravali, Sahitya Lahari), <strong>Raskhan</strong> (Sujan Raskhan, Prem Vatika), <strong>Bihari</strong> (Bihari Satsai - 719 couplets), Nanddas, Kumbhandas, and Amir Khusro's Braj songs.</span>
        <span class="lang-hi"><strong>2. ब्रजभाषा:</strong>
          <br>&bull; <em>उद्गम व स्वरूप:</em> मध्य शौरसेनी अपभ्रंश से विकसित; 15वीं से 19वीं सदी के उत्तरार्ध तक मध्यकालीन भारतीय साहित्य की निर्विवाद मुख्य साहित्यिक भाषा।
          <br>&bull; <em>विस्तार जिले:</em> मथुरा, आगरा, अलीगढ़, हाथरस, फिरोजाबाद, एटा, कासगंज, मैनपुरी, तथा बदायूं और बरेली के कुछ भाग।
          <br>&bull; <em>प्रमुख साहित्यकार:</em> <strong>सूरदास</strong> (सूर सागर, सूर सारावली, साहित्य लहरी), <strong>रसखान</strong> (सुजान रसखान, प्रेम वाटिका), <strong>बिहारी लाल</strong> (बिहारी सतसई - 719 दोहे), नंददास, कुंभनदास आदि।</span>
      </li>
      <li>
        <span class="lang-en"><strong>3. Kannauji (कन्नौजी):</strong>
          <br>&bull; <em>Characteristics:</em> Closely related to Braj Bhasha, distinguished by strong <strong>'O-karanta' (ओ-कारान्त) noun and verb inflections</strong> (e.g., 'Aao' -> 'Aayo', 'Ghar' -> 'Gharau').
          <br>&bull; <em>Districts:</em> Kannauj, Farrukhabad, Etawah, Auraiya, Kanpur Dehat, Kanpur Nagar, Hardoi, Shahjahanpur, and Pilibhit.
          <br>&bull; <em>Folk Literature:</em> Vibrant folk songs, seasonal barahmasa, and heroic Alha recitations.</span>
        <span class="lang-hi"><strong>3. कन्नौजी:</strong>
          <br>&bull; <em>विशेषताएं:</em> ब्रजभाषा से अत्यधिक साम्य, किंतु संज्ञा एवं क्रिया रूपों में प्रमुखता से <strong>'ओ-कारान्त' ध्वनियों</strong> का प्रयोग (जैसे 'आयो', 'गयो', 'घरौ')।
          <br>&bull; <em>विस्तार जिले:</em> कन्नौज, फर्रुखाबाद, इटावा, औरैया, कानपुर देहात, कानपुर नगर, हरदोई, शाहजहांपुर एवं पीलीभीत।
          <br>&bull; <em>लोक साहित्य:</em> लोकगीत, बारहमासा तथा स्थानीय आल्हा गायन।</span>
      </li>
      <li>
        <span class="lang-en"><strong>4. Bundeli / Bundelkhandi (बुंदेली):</strong>
          <br>&bull; <em>Origin &amp; Geography:</em> Evolved from southwestern Shauraseni Apabhramsha; spoken across all <strong>7 districts of Bundelkhand</strong>: Jhansi, Lalitpur, Jalaun (Orai), Hamirpur, Mahoba, Banda, and Chitrakoot.
          <br>&bull; <em>Sub-Dialects:</em> Banafri, Pawari, Lodhanti, Khatola.
          <br>&bull; <em>Epic Ballad of Bravery:</em> <strong>Alha-Khand (आल्हा-खंड)</strong> composed by Chandela court poet <strong>Jagnik (जगनिक)</strong> in the 12th century celebrating the 52 battles of warrior brothers Alha and Udal.
          <br>&bull; <em>Folk Poetry Genius:</em> <strong>Isuri (ईसुरी)</strong>, the master creator of Bundeli four-line folk couplets known as <strong>'Isuri Ki Phag' (ईसुरी की फागें)</strong>.</span>
        <span class="lang-hi"><strong>4. बुंदेली / बुंदेलखंडी:</strong>
          <br>&bull; <em>उद्गम व भूगोल:</em> दक्षिण-पश्चिमी शौरसेनी अपभ्रंश से विकसित; बुंदेलखंड के सभी <strong>7 जिलों</strong> में बोली जाती है: झांसी, ललितपुर, जालौन (उरई), हमीरपुर, महोबा, बांदा एवं चित्रकूट।
          <br>&bull; <em>उप-बोलियां:</em> बनाफरी, पवारी, लोधांती, खटोला।
          <br>&bull; <em>वीरगाथा महाकाव्य:</em> 12वीं सदी में चंदेल दरबारी कवि <strong>जगनिक</strong> द्वारा रचित <strong>आल्हा-खंड</strong>, जिसमें वीर आल्हा और ऊदल के 52 युद्धों का ओजस्वी वर्णन है (बनाफरी बोली में)।
          <br>&bull; <em>लोक कवि:</em> <strong>ईसुरी</strong>, जिनकी बुंदेली चौपहिया फागें <strong>'ईसुरी की फाग'</strong> के नाम से अमर हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Eastern Hindi Branch (Ardhamagadhi Apabhramsha) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Eastern Hindi Branch (Ardhamagadhi Apabhramsha): Awadhi &amp; Bagheli</span>
    <span class="lang-hi">3. पूर्वी हिंदी शाखा (अर्धमागधी अपभ्रंश): अवधी एवं बघेली</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. Awadhi (अवधी):</strong>
          <br>&bull; <em>Origin &amp; Prestige:</em> Directly derived from <strong>Ardhamagadhi Apabhramsha</strong>; immortalized as the greatest devotional and narrative poetic language of Northern India.
          <br>&bull; <em>Districts:</em> Ayodhya, Lucknow, Barabanki, Rae Bareli, Sitapur, Lakhimpur Kheri, Unnao, Hardoi (eastern parts), Pratapgarh, Sultanpur, Amethi, Gonda, Bahraich, Shravasti, Balrampur, Fatehpur, Kaushambi, and Prayagraj.
          <br>&bull; <em>Two Immortal Literary Traditions:</em>
            - <strong>Ram-Bhakti Tradition (राम-भक्ति धारा):</strong> <strong>Goswami Tulsidas</strong> composed the world-renowned epic <em>Ramcharitmanas</em> (started in Ayodhya in 1574 CE), <em>Kavitavali</em>, <em>Dohavali</em>, <em>Gitavali</em>, and <em>Vinaya Patrika</em>.
            - <strong>Sufi Premakhyan Tradition (सूफी प्रेमाख्यान धारा):</strong> <strong>Malik Muhammad Jayasi</strong> composed the magnum opus <em>Padmavat</em> (1540 CE at Jais, Amethi), <em>Akharavat</em>, and <em>Akhiri Kalam</em>. Earlier masterworks include <strong>Mulla Daud's</strong> <em>Chandayan</em> (1379 CE - first Sufi romance in Awadhi), <strong>Qutban's</strong> <em>Mrigavati</em>, and <strong>Manjhan's</strong> <em>Madhumalti</em>.</span>
        <span class="lang-hi"><strong>1. अवधी:</strong>
          <br>&bull; <em>उद्गम व प्रतिष्ठा:</em> <strong>अर्धमागधी अपभ्रंश</strong> से प्रत्यक्ष उत्पन्न; उत्तर भारत की महानतम भक्ति एवं आख्यान काव्य भाषा के रूप में प्रतिष्ठित।
          <br>&bull; <em>विस्तार जिले:</em> अयोध्या, लखनऊ, बाराबंकी, रायबरेली, सीतापुर, लखीमपुर खीरी, उन्नाव, हरदोई (पूर्वी भाग), प्रतापगढ़, सुल्तानपुर, अमेठी, गोंडा, बहराइच, श्रावस्ती, बलरामपुर, फतेहपुर, कौशाम्बी तथा प्रयागराज।
          <br>&bull; <em>दो अमर साहित्यिक परंपराएं:</em>
            - <strong>राम-भक्ति काव्यधारा:</strong> <strong>गोस्वामी तुलसीदास</strong> ने 1574 ई. में अयोध्या में विश्वप्रसिद्ध महाकाव्य <em>रामचरितमानस</em>, तथा <em>कवितावली</em>, <em>दोहावली</em> व <em>गीतावली</em> की रचना अवधी में की।
            - <strong>सूफी प्रेमाख्यानक काव्यधारा:</strong> जायस (अमेठी) के <strong>मलिक मोहम्मद जायसी</strong> ने 1540 ई. में अमर कृति <em>पद्मावत</em>, <em>अखरावट</em> व <em>आखिरी कलाम</em> की रचना की। <strong>मुल्ला दाऊद</strong> कृत <em>चंदायन</em> (1379 ई. - अवधी का प्रथम सूफी प्रेमाख्यान), <strong>कुतुबन</strong> कृत <em>मृगावती</em> तथा <strong>मंझन</strong> कृत <em>मधुमालती</em> भी अवधी में हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Bagheli (बघेली):</strong>
          <br>&bull; <em>Origin &amp; Characteristics:</em> Also derived from Ardhamagadhi Apabhramsha; closely related cousin of Awadhi; sometimes classified as South-Eastern Awadhi.
          <br>&bull; <em>Districts:</em> Spoken in the southern plateaus of <strong>Mirzapur, Sonbhadra</strong>, and southern trans-Yamuna tracts of <strong>Prayagraj</strong> along the Madhya Pradesh border.</span>
        <span class="lang-hi"><strong>2. बघेली:</strong>
          <br>&bull; <em>उद्गम व स्वरूप:</em> अर्धमागधी अपभ्रंश से उत्पन्न; अवधी की सहोदरा बोली, जिसे कई भाषाविद 'दक्षिणी अवधी' भी मानते हैं।
          <br>&bull; <em>विस्तार जिले:</em> मध्य प्रदेश सीमा से सटे <strong>मिर्जापुर, सोनभद्र</strong> के पठारी क्षेत्रों तथा <strong>प्रयागराज</strong> के दक्षिणी यमुनापार क्षेत्र में प्रयुक्त।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Bihari Hindi Branch - Bhojpuri (Magadhi Apabhramsha) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Bihari Hindi Branch (Magadhi Apabhramsha): Bhojpuri in Purvanchal</span>
    <span class="lang-hi">4. बिहारी हिंदी शाखा (मागधी अपभ्रंश): पूर्वांचल में भोजपुरी</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Origin &amp; Demographic Stature:</strong> Derived from <strong>Magadhi Apabhramsha</strong>; named after the ancient town of Bhojpur; <strong>most widely spoken regional dialect in Uttar Pradesh</strong> by population size.</span>
        <span class="lang-hi"><strong>उद्गम एवं जनसांख्यिकीय स्थिति:</strong> <strong>मागधी अपभ्रंश</strong> से विकसित; प्राचीन भोजपुर नगर के आधार पर नामकरण; जनसंख्या के आधार पर <strong>उत्तर प्रदेश में सर्वाधिक बोली जाने वाली बोली</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Districts Covered (Purvanchal Heartland):</strong> Varanasi, Gorakhpur, Deoria, Ballia, Ghazipur, Azamgarh, Mau, Jaunpur, Chandauli, Kushinagar, Maharajganj, Siddharthnagar, Basti, Sant Kabir Nagar, Mirzapur, and Sonbhadra.</span>
        <span class="lang-hi"><strong>विस्तार जिले (पूर्वांचल का हृदय स्थल):</strong> वाराणसी, गोरखपुर, देवरिया, बलिया, गाजीपुर, आजमगढ़, मऊ, जौनपुर, चंदौली, कुशीनगर, महाराजगंज, सिद्धार्थनगर, बस्ती, संत कबीर नगर, मिर्जापुर एवं सोनभद्र।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Cultural &amp; Theatrical Legend - Bhikhari Thakur (भिखारी ठाकुर):</strong>
          <br>&bull; Revered as the <strong>'Shakespeare of Bhojpuri' (भोजपुरी के शेक्सपियर)</strong> and 'Rai Bahadur of folk theatre'.
          <br>&bull; Immortalized folk plays addressing social reality and migration: <em>Bidesiya (बिदेसिया)</em>, <em>Gabarghichor</em>, <em>Beti-Vechwa</em>, and <em>Bhai-Birodh</em>.</span>
        <span class="lang-hi"><strong>सांस्कृतिक एवं रंगमंच के महानायक - भिखारी ठाकुर:</strong>
          <br>&bull; <strong>'भोजपुरी के शेक्सपियर'</strong> एवं 'लोक रंगमंच के राय बहादुर' के रूप में विख्यात।
          <br>&bull; पलायन और सामाजिक विसंगतियों पर आधारित कालजयी लोक नाटकों की रचना: <em>बिदेसिया</em>, <em>गबरघिचोर</em>, <em>बेटी-बेचवा</em>, तथा <em>भाई-बिरोध</em>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Folk Music &amp; Poetic Genres:</strong> World-famous genres include <strong>Biraha (बिरहा)</strong>, <strong>Kajari (कजरी)</strong> (centered in Mirzapur/Varanasi), <strong>Chaiti</strong>, <strong>Sohar</strong> (birth songs), and <strong>Pachara</strong> (Devi songs).</span>
        <span class="lang-hi"><strong>लोक संगीत एवं काव्य विधाएं:</strong> विश्वविख्यात लोक विधाओं में <strong>बिरहा</strong>, <strong>कजरी</strong> (मिर्जापुर/वाराणसी केंद्र), <strong>चैती</strong>, <strong>सोहर</strong> (पुत्र जन्मोत्सव गीत) तथा <strong>पचरा</strong> (देवी गीत) सम्मिलित हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Urdu Literature & Ganga-Jamuni Tehzeeb -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Urdu Language &amp; Literary Heritage: Dabistan-e-Lucknow &amp; UP Maestros</span>
    <span class="lang-hi">5. उर्दू भाषा एवं साहित्यिक धरोहर: दबिस्तान-ए-लखनऊ एवं यूपी के महान शायर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Historical Cradle of Northern Urdu:</strong> Uttar Pradesh evolved as the supreme center of refined Urdu prose and poetry, characterized by the composite <em>Ganga-Jamuni Tehzeeb</em>.</span>
        <span class="lang-hi"><strong>उत्तरी उर्दू का ऐतिहासिक पालना:</strong> उत्तर प्रदेश परिष्कृत उर्दू गद्य और पद्य का शीर्ष केंद्र बनकर उभरा, जिसने <em>गंगा-जमुनी तहजीब</em> को जन्म दिया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Lucknow School of Urdu Poetry (दबिस्तान-ए-लखनऊ):</strong>
          <br>&bull; Emerged during the Nawabi era when poets migrated from Delhi to Lucknow.
          <br>&bull; Known for artistic sophistication, delicate verbal ornament (Rai-o-Raiyayi), and emotional elegance.
          <br>&bull; <em>Marsiya Immortals:</em> <strong>Mir Babar Ali Anees</strong> (मीर अनीस) and <strong>Mirza Salamat Ali Dabeer</strong> (मिर्जा दबीर) elevated the Marsiya (elegiac poetry on Karbala) to sublime literary heights.
          <br>&bull; <em>Ghazal Masters:</em> <strong>Khwaja Haidar Ali Atish</strong> (आतिश लखनवी), <strong>Imam Bakhsh Nasikh</strong> (नासिख), and <strong>Pandit Daya Shankar Kaul 'Naseem'</strong> (author of the masterpiece masnavi <em>Gulzar-e-Naseem</em>).</span>
        <span class="lang-hi"><strong>उर्दू शायरी का लखनऊ स्कूल (दबिस्तान-ए-लखनऊ):</strong>
          <br>&bull; नवाबी दौर में दिल्ली से कवियों के लखनऊ आगमन के साथ विकसित।
          <br>&bull; भाषाई नजाकत, बाह्य सौंदर्य, अलंकरण एवं मुहावरों के सटीक प्रयोग हेतु प्रसिद्ध।
          <br>&bull; <em>मर्सिया के अमर कवि:</em> <strong>मीर बबर अली अनीस</strong> एवं <strong>मिर्जा सलामत अली दबीर</strong> ने कर्बला की शहादत पर आधारित मर्सिया को विश्व साहित्य की ऊंचाइयों पर पहुंचाया।
          <br>&bull; <em>गजल व मसनवी के उस्ताद:</em> <strong>ख्वाजा हैदर अली आतिश</strong>, <strong>शेख इमाम बख्श नासिख</strong>, तथा <strong>पंडित दयाशंकर कौल 'नसीम'</strong> (मसनवी <em>गुलजार-ए-नसीम</em> के रचयिता)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Legendary UP-Born Urdu Luminaries:</strong>
          <br>&bull; <em>Mirza Ghalib (1797-1869):</em> Born in <strong>Kala Mahal, Agra</strong>; greatest Urdu-Persian poet.
          <br>&bull; <em>Firaq Gorakhpuri (Raghupati Sahay, 1896-1982):</em> Born in <strong>Gorakhpur</strong>; awarded the prestigious <strong>Jnanpith Award (1969)</strong> for his collection <em>Gul-e-Naghma</em> (first Jnanpith in Urdu).
          <br>&bull; <em>Josh Malihabadi (1898-1982):</em> Born in <strong>Malihabad (Lucknow)</strong>; renowned as 'Shair-e-Inqilab' (Poet of the Revolution).
          <br>&bull; <em>Asrar-ul-Haq 'Majaz' (1911-1955):</em> Born in <strong>Rudauli (Ayodhya)</strong>; penned the iconic anthem of Aligarh Muslim University (<em>Tarana-e-Aligarh</em>).
          <br>&bull; <em>Akbar Allahabadi (1846-1921):</em> Born in <strong>Prayagraj</strong>; father of modern Urdu satirical and humorous poetry.</span>
        <span class="lang-hi"><strong>यूपी में जन्मे अमर उर्दू हस्ताक्षर:</strong>
          <br>&bull; <em>मिर्जा गालिब (1797-1869):</em> जन्म <strong>काला महल, आगरा</strong>; उर्दू और फारसी के महानतम शायर।
          <br>&bull; <em>फिराक गोरखपुरी (रघुपति सहाय, 1896-1982):</em> जन्म <strong>गोरखपुर</strong>; कृति <em>गुल-ए-नगमा</em> हेतु <strong>ज्ञानपीठ पुरस्कार (1969)</strong> से सम्मानित (उर्दू साहित्य का प्रथम ज्ञानपीठ)।
          <br>&bull; <em>जोश मलीहाबादी (1898-1982):</em> जन्म <strong>मलीहाबाद (लखनऊ)</strong>; 'शायर-ए-इंकलाब' के रूप में प्रसिद्ध।
          <br>&bull; <em>असरार-उल-हक 'मजाज' (1911-1955):</em> जन्म <strong>रदौली (अयोध्या)</strong>; अलीगढ़ मुस्लिम विश्वविद्यालय का तराना लिखा।
          <br>&bull; <em>अकबर इलाहाबादी (1846-1921):</em> जन्म <strong>प्रयागराज</strong>; आधुनिक उर्दू व्यंग्य एवं हास्य शायरी के जनक।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Language Promotion Academies & Research Sansthans -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Language Promotion Academies &amp; Literary Sansthans of UP</span>
    <span class="lang-hi">6. उत्तर प्रदेश के भाषा संवर्धन संस्थान एवं साहित्यिक अकादमियां</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Uttar Pradesh Hindi Sansthan (उत्तर प्रदेश हिंदी संस्थान, लखनऊ):</strong>
          <br>&bull; <em>Established:</em> Formed on <strong>30 December 1976</strong> by amalgamating the Hindi Samiti, Hindi Granth Academy, and Bhasha Vibhag; headquartered at Hazratganj, Lucknow.
          <br>&bull; <em>Highest State Literary Honor:</em> <strong>Bharat Bharati Samman (भारत भारती सम्मान)</strong> - highest state award for Hindi literature, carrying a cash prize of ₹8 lakh, citation, and Angavastram.
          <br>&bull; <em>Other Major Honors:</em> Lohia Sahitya Samman, Hindi Gaurav Samman, Mahatma Gandhi Sahitya Samman.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश हिंदी संस्थान (लखनऊ):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>30 दिसंबर 1976</strong> को हिंदी समिति, हिंदी ग्रंथ अकादमी और भाषा विभाग को मिलाकर गठित; मुख्यालय हजरतगंज, लखनऊ।
          <br>&bull; <em>सर्वोच्च राज्य साहित्यिक पुरस्कार:</em> <strong>भारत भारती सम्मान</strong> - हिंदी साहित्य के क्षेत्र में राज्य का सर्वोच्च सम्मान, ₹8 लाख की नकद राशि, प्रशस्ति-पत्र व अंगवस्त्रम।
          <br>&bull; <em>अन्य प्रमुख सम्मान:</em> लोहिया साहित्य सम्मान, हिंदी गौरव सम्मान, महात्मा गांधी साहित्य सम्मान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Uttar Pradesh Sanskrit Sansthan (उत्तर प्रदेश संस्कृत संस्थान, लखनऊ):</strong>
          <br>&bull; <em>Established:</em> Formed on <strong>31 December 1976</strong> at Lucknow for revitalization and scholarship of Sanskrit language, Vedas, and Jyotish.
          <br>&bull; <em>Highest State Award:</em> <strong>Vishwabharati Samman (विश्वभारती सम्मान)</strong> - carrying cash award of ₹5 lakh.
          <br>&bull; <em>Other Awards:</em> Maharshi Valmiki Samman, Maharshi Vyas Samman.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश संस्कृत संस्थान (लखनऊ):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>31 दिसंबर 1976</strong> को संस्कृत, वेद एवं ज्योतिष के संवर्धन हेतु लखनऊ में गठित।
          <br>&bull; <em>सर्वोच्च सम्मान:</em> <strong>विश्वभारती सम्मान</strong> - ₹5 लाख की पुरस्कार राशि।
          <br>&bull; <em>अन्य प्रमुख सम्मान:</em> महर्षि वाल्मीकि सम्मान, महर्षि व्यास सम्मान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Uttar Pradesh Urdu Academy (उत्तर प्रदेश उर्दू अकादमी, लखनऊ):</strong>
          <br>&bull; <em>Established:</em> Set up in <strong>January 1972</strong> for the promotion, research, translation, and publication of Urdu literary treasures.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश उर्दू अकादमी (लखनऊ):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>जनवरी 1972</strong> में उर्दू साहित्य के संरक्षण, शोध, अनुवाद एवं प्रकाशन हेतु लखनऊ में स्थापित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Hindustani Academy (हिंदुस्तानी एकेडमी, प्रयागराज):</strong>
          <br>&bull; <em>Established:</em> Founded on <strong>22 January 1927</strong> at Prayagraj under the initiative of Sir William Marris; publishes academic quarterly journal <em>Hindustani</em>; dedicated to composite Hindi-Urdu linguistic scholarship.</span>
        <span class="lang-hi"><strong>हिंदुस्तानी एकेडमी (प्रयागराज):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>22 जनवरी 1927</strong> को सर विलियम मॉरिस की पहल पर प्रयागराज में स्थापित; त्रैमासिक शोध पत्रिका <em>हिंदुस्तानी</em> का प्रकाशन; हिंदी-उर्दू साझी विरासत का प्रमुख संस्थान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Nagari Pracharini Sabha (काशी नागरी प्रचारिणी सभा, वाराणसी):</strong>
          <br>&bull; <em>Established:</em> Founded on <strong>16 July 1893</strong> at Varanasi by Babu Shyam Sundar Das, Pandit Ramnarayan Mishra, and Thakur Shivkumar Singh.
          <br>&bull; <em>Historic Contributions:</em> Championed the adoption of Devanagari script in courts (achieved in 1900 under Sir Antony MacDonnell); published the first authoritative Hindi dictionary <em>Hindi Shabdsagar</em> and edited critical editions of Prithviraj Raso and Kabir Granthavali.</span>
        <span class="lang-hi"><strong>काशी नागरी प्रचारिणी सभा (वाराणसी):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>16 जुलाई 1893</strong> को वाराणसी में बाबू श्याम सुंदर दास, पंडित रामनारायण मिश्र एवं ठाकुर शिवकुमार सिंह द्वारा स्थापित।
          <br>&bull; <em>ऐतिहासिक योगदान:</em> 1900 में अदालतों में देवनागरी लिपि की मान्यता दिलाने में प्रमुख भूमिका; प्रथम प्रामाणिक वृहद <em>हिंदी शब्दसागर</em> का निर्माण तथा पृथ्वीराज रासो व कबीर ग्रंथावली का संपादन।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Other Language Sansthans:</strong> UP Punjabi Academy (1998, Lucknow), UP Sindhi Academy (1996, Lucknow), and UP Bhasha Sansthan (1994, Lucknow).</span>
        <span class="lang-hi"><strong>अन्य भाषा संस्थान:</strong> यूपी पंजाबी अकादमी (1998, लखनऊ), यूपी सिंधी अकादमी (1996, लखनऊ), तथा यूपी भाषा संस्थान (1994, लखनऊ)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master Comparison Table of Regional Dialects -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Comparison Table: Regional Dialects of Uttar Pradesh</span>
    <span class="lang-hi">7. उत्तर प्रदेश की क्षेत्रीय बोलियों की महा-तुलना तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Dialect &amp; Apabhramsha Origin</span>
            <span class="lang-hi">बोली एवं अपभ्रंश उद्गम</span>
          </th>
          <th>
            <span class="lang-en">Primary Districts in UP</span>
            <span class="lang-hi">उत्तर प्रदेश के प्रमुख जिले</span>
          </th>
          <th>
            <span class="lang-en">Linguistic Feature &amp; Key Literary Works</span>
            <span class="lang-hi">भाषाई लक्षण एवं प्रमुख कृतियां</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en"><strong>Khari Boli (कौरवी)</strong><br>Northern Shauraseni</span>
            <span class="lang-hi"><strong>खड़ी बोली (कौरवी)</strong><br>उत्तरी शौरसेनी</span>
          </td>
          <td>
            <span class="lang-en">Meerut, Saharanpur, Muzaffarnagar, Shamli, Baghpat, Bijnor, Moradabad, Rampur</span>
            <span class="lang-hi">मेरठ, सहारनपुर, मुजफ्फरनगर, शामली, बागपत, बिजनौर, मुरादाबाद, रामपुर</span>
          </td>
          <td>
            <span class="lang-en">Standard Hindi foundation; Amir Khusro's Pahelis/Mukaris; Bharatendu, Premchand, Jayashankar Prasad</span>
            <span class="lang-hi">मानक हिंदी का आधार; अमीर खुसरो की पहेलियां/मुकरियां; भारतेंदु, प्रेमचंद, जयशंकर प्रसाद</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Braj Bhasha (ब्रजभाषा)</strong><br>Central Shauraseni</span>
            <span class="lang-hi"><strong>ब्रजभाषा</strong><br>मध्य शौरसेनी</span>
          </td>
          <td>
            <span class="lang-en">Mathura, Agra, Aligarh, Hathras, Firozabad, Etah, Mainpuri, Kasganj</span>
            <span class="lang-hi">मथुरा, आगरा, अलीगढ़, हाथरस, फिरोजाबाद, एटा, मैनपुरी, कासगंज</span>
          </td>
          <td>
            <span class="lang-en">Dominant medieval literary vehicle; Surdas (<em>Sur Sagar</em>), Raskhan (<em>Prem Vatika</em>), Bihari (<em>Satsai</em>)</span>
            <span class="lang-hi">मध्यकालीन प्रमुख साहित्यिक भाषा; सूरदास (<em>सूर सागर</em>), रसखान (<em>प्रेम वाटिका</em>), बिहारी (<em>सतसई</em>)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Kannauji (कन्नौजी)</strong><br>Shauraseni</span>
            <span class="lang-hi"><strong>कन्नौजी</strong><br>शौरसेनी</span>
          </td>
          <td>
            <span class="lang-en">Kannauj, Farrukhabad, Etawah, Auraiya, Kanpur Dehat, Hardoi, Shahjahanpur</span>
            <span class="lang-hi">कन्नौज, फर्रुखाबाद, इटावा, औरैया, कानपुर देहात, हरदोई, शाहजहांपुर</span>
          </td>
          <td>
            <span class="lang-en">Distinct 'O-karanta' endings; folk songs, local Alha singing traditions</span>
            <span class="lang-hi">'ओ-कारान्त' ध्वनियां; लोकगीत एवं स्थानीय आल्हा गायन परंपरा</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Bundeli (बुंदेली)</strong><br>Southwestern Shauraseni</span>
            <span class="lang-hi"><strong>बुंदेली</strong><br>दक्षिण-पश्चिमी शौरसेनी</span>
          </td>
          <td>
            <span class="lang-en">Jhansi, Lalitpur, Jalaun (Orai), Hamirpur, Mahoba, Banda, Chitrakoot</span>
            <span class="lang-hi">झांसी, ललितपुर, जालौन (उरई), हमीरपुर, महोबा, बांदा, चित्रकूट</span>
          </td>
          <td>
            <span class="lang-en">Warrior culture; Jagnik's <em>Alha-Khand</em> (Banafri dialect); Isuri's four-line Phag couplets</span>
            <span class="lang-hi">वीर रस प्रधान; जगनिक रचित <em>आल्हा-खंड</em> (बनाफरी बोली); ईसुरी की फागें</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Awadhi (अवधी)</strong><br>Ardhamagadhi</span>
            <span class="lang-hi"><strong>अवधी</strong><br>अर्धमागधी</span>
          </td>
          <td>
            <span class="lang-en">Ayodhya, Lucknow, Barabanki, Rae Bareli, Sitapur, Lakhimpur, Pratapgarh, Sultanpur, Gonda</span>
            <span class="lang-hi">अयोध्या, लखनऊ, बाराबंकी, रायबरेली, सीतापुर, लखीमपुर, प्रतापगढ़, सुल्तानपुर, गोंडा</span>
          </td>
          <td>
            <span class="lang-en">Epic devotional &amp; Sufi literature; Tulsidas (<em>Ramcharitmanas</em>), Jayasi (<em>Padmavat</em>), Mulla Daud</span>
            <span class="lang-hi">महाकाव्यात्मक भक्ति व सूफी काव्य; तुलसीदास (<em>रामचरितमानस</em>), जायसी (<em>पद्मावत</em>), मुल्ला दाऊद</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Bagheli (बघेली)</strong><br>Ardhamagadhi</span>
            <span class="lang-hi"><strong>बघेली</strong><br>अर्धमागधी</span>
          </td>
          <td>
            <span class="lang-en">Mirzapur, Sonbhadra, and Trans-Yamuna Prayagraj</span>
            <span class="lang-hi">मिर्जापुर, सोनभद्र, एवं यमुनापार प्रयागराज</span>
          </td>
          <td>
            <span class="lang-en">Close sister dialect of Awadhi; plateau folk traditions</span>
            <span class="lang-hi">अवधी की सहोदरा बोली; पठारी लोक परंपराएं</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Bhojpuri (भोजपुरी)</strong><br>Magadhi</span>
            <span class="lang-hi"><strong>भोजपुरी</strong><br>मागधी</span>
          </td>
          <td>
            <span class="lang-en">Varanasi, Gorakhpur, Ghazipur, Ballia, Deoria, Azamgarh, Mau, Jaunpur, Chandauli, Kushinagar</span>
            <span class="lang-hi">वाराणसी, गोरखपुर, गाजीपुर, बलिया, देवरिया, आजमगढ़, मऊ, जौनपुर, चंदौली, कुशीनगर</span>
          </td>
          <td>
            <span class="lang-en">Most populous dialect of UP; Bhikhari Thakur (<em>Bidesiya</em>); Biraha, Kajari, Chaiti music</span>
            <span class="lang-hi">यूपी में सर्वाधिक बोली जाने वाली बोली; भिखारी ठाकुर (<em>बिदेसिया</em>); बिरहा, कजरी, चैती संगीत</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 9: Rapid Revision Matrix & UPSSSC Exam Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">8. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Exam Topic / Trap</span>
            <span class="lang-hi">परीक्षा विषय / ट्रैप</span>
          </th>
          <th>
            <span class="lang-en">Precision Answer &amp; Conceptual Truth</span>
            <span class="lang-hi">सटीक उत्तर एवं संकल्पनात्मक तथ्य</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Father of Khari Boli / Hindavi</span>
            <span class="lang-hi">खड़ी बोली / हिंदवी के आदि कवि</span>
          </td>
          <td>
            <span class="lang-en"><strong>Amir Khusro</strong>; born in Patiyali (Kasganj district).</span>
            <span class="lang-hi"><strong>अमीर खुसरो</strong>; जन्म पटियाली (कासगंज जिला)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Father of Modern Hindi Prose</span>
            <span class="lang-hi">आधुनिक हिंदी गद्य के जनक</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bhartendu Harishchandra (1850-1885)</strong>; born in Kashi (Varanasi).</span>
            <span class="lang-hi"><strong>भारतेंदु हरिश्चंद्र (1850-1885)</strong>; जन्म काशी (वाराणसी)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Most Widely Spoken Dialect in UP</span>
            <span class="lang-hi">यूपी में सर्वाधिक बोली जाने वाली बोली</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bhojpuri</strong>; spoken across entire Purvanchal (Eastern UP).</span>
            <span class="lang-hi"><strong>भोजपुरी</strong>; संपूर्ण पूर्वांचल में सर्वाधिक आबादी द्वारा प्रयुक्त।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Kauravi Dialect Coined by</span>
            <span class="lang-hi">कौरवी नामकरण किसके द्वारा</span>
          </td>
          <td>
            <span class="lang-en"><strong>Rahul Sankrityayan</strong> (for Khari Boli of Meerut-Saharanpur).</span>
            <span class="lang-hi"><strong>राहुल सांकृत्यायन</strong> (मेरठ-सहारनपुर की खड़ी बोली हेतु)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Shakespeare of Bhojpuri</span>
            <span class="lang-hi">भोजपुरी के शेक्सपियर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bhikhari Thakur</strong> (author of <em>Bidesiya</em>).</span>
            <span class="lang-hi"><strong>भिखारी ठाकुर</strong> (<em>बिदेसिया</em> नाटक के रचयिता)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Jnanpith Award in Urdu</span>
            <span class="lang-hi">उर्दू में प्रथम ज्ञानपीठ पुरस्कार</span>
          </td>
          <td>
            <span class="lang-en"><strong>Firaq Gorakhpuri (1969)</strong> for <em>Gul-e-Naghma</em> (born in Gorakhpur).</span>
            <span class="lang-hi"><strong>फिराक गोरखपुरी (1969)</strong>, कृति <em>गुल-ए-नगमा</em> हेतु (जन्म गोरखपुर)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Highest Award of UP Hindi Sansthan</span>
            <span class="lang-hi">यूपी हिंदी संस्थान का सर्वोच्च सम्मान</span>
          </td>
          <td>
            <span class="lang-en"><strong>Bharat Bharati Samman</strong> (₹8 lakh prize).</span>
            <span class="lang-hi"><strong>भारत भारती सम्मान</strong> (₹8 लाख पुरस्कार राशि)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Highest Award of UP Sanskrit Sansthan</span>
            <span class="lang-hi">यूपी संस्कृत संस्थान का सर्वोच्च सम्मान</span>
          </td>
          <td>
            <span class="lang-en"><strong>Vishwabharati Samman</strong> (₹5 lakh prize).</span>
            <span class="lang-hi"><strong>विश्वभारती सम्मान</strong> (₹5 लाख पुरस्कार राशि)।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "regional-languages", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_regional_languages_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
