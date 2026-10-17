import os
import re

def build_festivals_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Fairs, Festivals &amp; Cultural Celebrations of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के मेले, त्यौहार एवं सांस्कृतिक उत्सव</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Festivals & Fairs of UP] --> B[Spiritual & Kumbh Heritage]
    A --> C[Braj Holi Festivities]
    A --> D[Cultural Tourism Mahotsavs]
    A --> E[Major Historical Fairs: ~2250 Annually]
    A --> F[Sufi Urs & Communal Harmony]
    A --> G[Tribal & Folk Observances]

    B --> B1[Kumbh Mela Prayagraj: UNESCO 2017]
    B --> B2[Dev Deepawali Varanasi: Kartik Purnima]
    B --> B3[Deepotsav Ayodhya: World Record Diyas]
    B --> B4[Maha Shivratri: Kashi & Lodheshwar]

    C --> C1[Barsana & Nandgaon: Lathmar Holi]
    C --> C2[Vrindavan: Phoolon Ki Holi & Banke Bihari]
    C --> C3[Dauji Baldeo: Huranga | Gokul: Chhadimar]
    C --> C4[Varanasi: Masane Ki Chita Bhasma Holi]

    D --> D1[Taj Mahotsav: Agra Shilpgram 18-27 Feb]
    D --> D2[Lucknow Mahotsav: Awadhi Crafts & Food]
    D --> D3[Sulah-kul Utsav: Agra Hindu-Muslim Unity]
    D --> D4[Kabir Utsav Maghar & Ramayan Mela]

    E --> E1[Bateshwar Agra & Dadhri Ballia: Cattle Fairs]
    E --> E2[Nauchandi Meerut: 2nd Sunday after Holi]
    E --> E3[Shakumbhari Saharanpur & Khichdi Gorakhpur]
    E --> E4[Fairs Rank: Mathura 86 Max | Pilibhit Least]

    F --> F1[Deva Sharif Barabanki: Waris Ali Shah]
    F --> F2[Syed Salar Masud Ghazi: Bahraich]
    F --> F3[Makhanpur Kanpur: Zinda Shah Madar]

    G --> G1[Tharu: Bajhar Festival & Diwali as Shok Parv]
    G --> G2[Kharwar & Baiga: Karma Festival Sonbhadra]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उ.प्र. के मेले एवं त्यौहार] --> B[आध्यात्मिक एवं कुंभ परंपरा]
    A --> C[ब्रज की विशिष्ट होली परंपराएं]
    A --> D[सांस्कृतिक पर्यटन महोत्सव]
    A --> E[प्रमुख ऐतिहासिक मेले: प्रतिवर्ष ~2250]
    A --> F[सूफी उर्स एवं कौमी एकता]
    A --> G[जनजातीय एवं लोक उत्सव]

    B --> B1[कुंभ मेला प्रयागराज: यूनेस्को धरोहर 2017]
    B --> B2[देव दीपावली वाराणसी: कार्तिक पूर्णिमा]
    B --> B3[दीपोत्सव अयोध्या: सरयू तट पर विश्व रिकॉर्ड]
    B --> B4[महाशिवरात्रि: काशी विश्वनाथ व लोधेश्वर]

    C --> C1[बरसाना व नंदगांव: लठमार होली]
    C --> C2[वृंदावन: फूलों की होली व बांके बिहारी]
    C --> C3[दाऊजी बलदेव: हुरंगा | गोकुल: छड़ीमार]
    C --> C4[वाराणसी: मणिकर्णिका चिता भस्म की होली]

    D --> D1[ताज महोत्सव: आगरा शिल्पग्राम 18-27 फरवरी]
    D --> D2[लखनऊ महोत्सव: अवधी शिल्प, कथक व व्यंजन]
    D --> D3[सुलह-कुल उत्सव: आगरा हिंदू-मुस्लिम एकता]
    D --> D4[कबीर उत्सव मगहर व रामायण मेला चित्रकूट]

    E --> E1[बटेश्वर आगरा व ददरी बलिया: विशाल पशु मेले]
    E --> E2[नौचंदी मेरठ: होली के दूसरे रविवार से]
    E --> E3[शाकंभरी सहारनपुर व खिचड़ी गोरखनाथ]
    E --> E4[मेला रैंकिंग: मथुरा सर्वाधिक 86 | पीलीभीत न्यूनतम]

    F --> F1[देवा शरीफ बाराबंकी: वारिस अली शाह उर्स]
    F --> F2[सैयद सालार मसूद गाजी: बहराइच जेठ मेला]
    F --> F3[मकनपुर कानपुर: मदार शाह का उर्स]

    G --> G1[थारू: बझहर पर्व व दीपावली शोक पर्व]
    G --> G2[खरवार व बैगा: कर्मा पर्व सोनभद्र]
    </div>
  </div>
</div>

<!-- Card 2: Overview & District Rankings of Fairs -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Fairs Landscape of UP: Statistics &amp; District Rankings</span>
    <span class="lang-hi">1. उ.प्र. में मेलों का परिदृश्य: सांख्यिकी एवं जिला रैंकिंग</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Fairs Capital of India:</strong> Uttar Pradesh organizes the highest number of annual fairs in the country—approximately <strong>2,250 fairs</strong> take place across the state every year.</span>
      <span class="lang-hi"><strong>मेलों का अग्रणी राज्य:</strong> उत्तर प्रदेश में देश में सर्वाधिक मेले आयोजित होते हैं—राज्य के विभिन्न जनपदों में प्रतिवर्ष लगभग <strong>2,250 मेले</strong> लगते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>District Ranking by Number of Fairs:</strong>
        <br/>• <strong>Rank 1 (Highest):</strong> <strong>Mathura (86 fairs)</strong> - due to extensive Krishna Leela and Braj circuit pilgrimage points.
        <br/>• <strong>Rank 2:</strong> <strong>Kanpur (80 fairs)</strong>
        <br/>• <strong>Rank 3:</strong> <strong>Hamirpur (79 fairs)</strong>
        <br/>• <strong>Rank 4:</strong> <strong>Jhansi (78 fairs)</strong>
        <br/>• <strong>Rank 5:</strong> <strong>Agra (72 fairs)</strong>
        <br/>• <strong>Rank 6:</strong> <strong>Fatehpur (70 fairs)</strong>
        <br/>• <strong>Lowest Number of Fairs:</strong> <strong>Pilibhit (least, only 2 to 3 fairs annually)</strong>.
      </span>
      <span class="lang-hi"><strong>मेलों की संख्या के आधार पर जिलों की रैंकिंग:</strong>
        <br/>• <strong>प्रथम स्थान (सर्वाधिक):</strong> <strong>मथुरा (86 मेले)</strong> - कृष्ण भक्ति एवं ब्रज चौरासी कोस परिक्रमा के कारण।
        <br/>• <strong>द्वितीय स्थान:</strong> <strong>कानपुर (80 मेले)</strong>
        <br/>• <strong>तृतीय स्थान:</strong> <strong>हमीरपुर (79 मेले)</strong>
        <br/>• <strong>चतुर्थ स्थान:</strong> <strong>झांसी (78 मेले)</strong>
        <br/>• <strong>पंचम स्थान:</strong> <strong>आगरा (72 मेले)</strong>
        <br/>• <strong>षष्ठम स्थान:</strong> <strong>फतेहपुर (70 मेले)</strong>
        <br/>• <strong>न्यूनतम मेले:</strong> <strong>पीलीभीत (सबसे कम, प्रतिवर्ष मात्र 2 से 3 मेले)</strong>।
      </span>
    </li>
  </ul>
</div>

<!-- Card 3: Spiritual Peaks: Kumbh, Dev Deepawali & Deepotsav -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Grand Spiritual Gatherings: Kumbh Mela, Dev Deepawali &amp; Deepotsav</span>
    <span class="lang-hi">2. भव्य आध्यात्मिक उत्सव: कुंभ मेला, देव दीपावली एवं दीपोत्सव</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Kumbh Mela (Prayagraj):</strong>
        <br/>• <strong>Location:</strong> Triveni Sangam (confluence of Ganga, Yamuna, and subterranean Saraswati).
        <br/>• <strong>Cycles:</strong> <em>Maha Kumbh</em> held every 12 years; <em>Kumbh / Ardh Kumbh</em> held every 6 years; <em>Magh Mela</em> held annually in Magh month (Jan-Feb) for Kalpavasis.
        <br/>• <strong>Global Honor:</strong> Inscribed on <strong>UNESCO's Representative List of Intangible Cultural Heritage of Humanity in 2017</strong>.
        <br/>• <strong>Astrological Basis:</strong> Occurs when Jupiter enters Taurus/Aries and Sun and Moon enter Capricorn on Amavasya (Mauni Amavasya royal bath / Shahi Snan).
      </span>
      <span class="lang-hi"><strong>कुंभ मेला (प्रयागराज):</strong>
        <br/>• <strong>स्थल:</strong> त्रिवेणी संगम (गंगा, यमुना एवं अदृश्य सरस्वती का मिलन स्थल)।
        <br/>• <strong>आयोजन चक्र:</strong> <em>महाकुंभ</em> प्रत्येक 12 वर्ष पर; <em>कुंभ / अर्धकुंभ</em> प्रत्येक 6 वर्ष पर; <em>माघ मेला</em> प्रतिवर्ष माघ माह (जनवरी-फरवरी) में कल्पवासियों हेतु।
        <br/>• <strong>वैश्विक सम्मान:</strong> वर्ष <strong>2017 में यूनेस्को की मानवता की अमूर्त सांस्कृतिक विरासत</strong> सूची में सम्मिलित।
        <br/>• <strong>ज्योतिषीय आधार:</strong> जब बृहस्पति मेष/वृष राशि में तथा सूर्य व चंद्रमा मकर राशि में प्रवेश करते हैं (मौनी अमावस्या का शाही स्नान)।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Dev Deepawali (Varanasi):</strong>
        <br/>• Celebrated on <strong>Kartik Purnima</strong> (fifteen days after Diwali) along all 84 Ghats of Varanasi.
        <br/>• <strong>Mythological Significance:</strong> Commemorates Lord Shiva's victory over the demon Tripurasura (also called <em>Tripurotsav</em>); belief that Gods descend to bathe in the Ganga.
        <br/>• Over 12-15 lakh earthen diyas illuminated simultaneously, attracting millions of international travelers.
      </span>
      <span class="lang-hi"><strong>देव दीपावली (वाराणसी):</strong>
        <br/>• <strong>कार्तिक पूर्णिमा</strong> (दीपावली के 15 दिन बाद) को काशी के सभी 84 घाटों पर भव्य रूप से आयोजित।
        <br/>• <strong>पौराणिक मान्यता:</strong> भगवान शिव द्वारा त्रिपुरासुर राक्षस के वध (त्रिपुरोत्सव) के उपलक्ष्य में देवताओं द्वारा गंगा तट पर दीप प्रज्वलित करने की मान्यता।
        <br/>• एक साथ 12 से 15 लाख मिट्टी के दीयों से घाटों का जगमगाना तथा भव्य महाआरती।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Ayodhya Deepotsav (दीपोत्सव, अयोध्या धाम):</strong>
        <br/>• Initiated in 2017; celebrated on <strong>Chhoti Diwali (Kartik Krishna Chaturdashi)</strong> on the banks of Saryu River (Ram Ki Paidi).
        <br/>• Consistently enters the <strong>Guinness World Records</strong> (lighting over 22+ lakh indigenous earthen lamps simultaneously in recent editions).
      </span>
      <span class="lang-hi"><strong>अयोध्या दीपोत्सव (दीपोत्सव, अयोध्या धाम):</strong>
        <br/>• वर्ष 2017 से प्रारंभ; प्रतिवर्ष <strong>छोटी दीपावली (नरक चतुर्दशी)</strong> पर सरयू तट (राम की पैड़ी) पर आयोजित।
        <br/>• एक साथ 22 लाख से अधिक मिट्टी के दीये जलाकर लगातार <strong>गिनीज वर्ल्ड रिकॉर्ड्स</strong> में दर्ज।
      </span>
    </li>
  </ul>
</div>

<!-- Card 4: Unique Holi Celebrations of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Unique Holi Traditions Across Uttar Pradesh</span>
    <span class="lang-hi">3. उत्तर प्रदेश की अनूठी एवं विश्वप्रसिद्ध होली परंपराएं</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Lathmar Holi (Barsana &amp; Nandgaon, Mathura):</strong>
        <br/>• <strong>Barsana (Phalgun Shukla Navami):</strong> Men from Nandgaon (Huriyaras) visit Barsana; women (Huriyarins) strike their shields playfully with wooden staffs (Lathis).
        <br/>• <strong>Nandgaon (Phalgun Shukla Dashami):</strong> Men of Barsana visit Nandgaon the next day for reciprocating celebrations.
      </span>
      <span class="lang-hi"><strong>लठमार होली (बरसाना एवं नंदगांव, मथुरा):</strong>
        <br/>• <strong>बरसाना (फाल्गुन शुक्ल नवमी):</strong> नंदगांव के पुरुष (हुरियारे) बरसाना आते हैं; बरसाना की महिलाएं (हुरियारिनें) उन पर लाठियां बरसाती हैं और पुरुष ढाल से बचाव करते हैं।
        <br/>• <strong>नंदगांव (फाल्गुन शुक्ल दशमी):</strong> अगले दिन बरसाना के पुरुष नंदगांव जाकर होली खेलते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Phoolon Ki Holi (फूलों की होली, Vrindavan):</strong> Celebrated at the historic <strong>Banke Bihari Temple</strong> on Amalaki Ekadashi; priests shower flower petals (rose, marigold) and perfumed gulal on devotees.</span>
      <span class="lang-hi"><strong>फूलों की होली (वृंदावन):</strong> आमलकी एकादशी को प्रसिद्ध <strong>बांके बिहारी मंदिर</strong> में आयोजित; श्रद्धालु एवं पुजारी एक-दूसरे पर गुलाब व गेंदे की पंखुड़ियां व अबीर बरसाते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Chhadi-mar Holi (छड़ीमार होली, Gokul):</strong> Women play with small sticks (Chhadis) instead of heavy lathis to protect child Krishna (Bal Gopal) from injury.</span>
      <span class="lang-hi"><strong>छड़ीमार होली (गोकुल):</strong> भगवान कृष्ण के बाल स्वरूप को चोट न पहुंचे, इसलिए गोपियां लाठी के स्थान पर छोटी छड़ियों से होली खेलती हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Huranga (हुरंगा, Dauji Temple, Baldeo, Mathura):</strong> Organized the day after main Holi at the temple of Krishna's elder brother, Balram (Dauji). Women tear men's upper clothes, soak them in turmeric and tesu dye, and playfully whip them.</span>
      <span class="lang-hi"><strong>हुरंगा (दाऊजी मंदिर, बलदेव, मथुरा):</strong> होली के अगले दिन बलराम जी (दाऊजी) के मंदिर में आयोजित; देवर-भाभी का पारंपरिक उत्सव जिसमें कपड़े फाड़कर रंग में डुबोकर कोड़े मारे जाते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Chita Bhasma Holi / Masane Ki Holi (मणिकर्णिका घाट, Varanasi):</strong> Played on the day after Rangbhari Ekadashi with pyre ashes (Chita Bhasma) and gulal at the cremation ground in reverence to Mahadev Shiva.</span>
      <span class="lang-hi"><strong>चिता भस्म की होली / मसाने की होली (मणिकर्णिका घाट, काशी):</strong> रंगभरी एकादशी के अगले दिन श्मशान घाट पर भगवान शिव के गणों द्वारा चिता की भस्म और अबीर-गुलाल से खेली जाने वाली अद्वितीय होली।</span>
    </li>
  </ul>
</div>

<!-- Card 5: Major State Tourism Mahotsavs -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Cultural &amp; Tourism Mahotsavs Organized by UP Government</span>
    <span class="lang-hi">4. उ.प्र. पर्यटन एवं संस्कृति विभाग द्वारा आयोजित प्रमुख महोत्सव</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Mahotsav / Festival</span><span class="lang-hi">महोत्सव / उत्सव</span></th>
          <th><span class="lang-en">Venue / District</span><span class="lang-hi">स्थान / जिला</span></th>
          <th><span class="lang-en">Month / Timing</span><span class="lang-hi">माह / समय</span></th>
          <th><span class="lang-en">Cultural Significance</span><span class="lang-hi">सांस्कृतिक महत्व</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Taj Mahotsav (ताज महोत्सव)</strong></span><span class="lang-hi"><strong>ताज महोत्सव</strong></span></td>
          <td><span class="lang-en">Shilpgram, Agra</span><span class="lang-hi">शिल्पग्राम, आगरा</span></td>
          <td><span class="lang-en">18 - 27 February (Annual)</span><span class="lang-hi">18 से 27 फरवरी (प्रतिवर्ष)</span></td>
          <td><span class="lang-en">10-day celebration of Mughal heritage, Indian handicrafts, culinary arts, and folk dance</span><span class="lang-hi">मुगलकालीन वैभव, भारतीय हस्तशिल्प, व्यंजन और लोक नृत्यों का 10-दिवसीय संगम</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Lucknow Mahotsav (लखनऊ महोत्सव)</strong></span><span class="lang-hi"><strong>लखनऊ महोत्सव</strong></span></td>
          <td><span class="lang-en">Lucknow</span><span class="lang-hi">लखनऊ</span></td>
          <td><span class="lang-en">November - December</span><span class="lang-hi">नवंबर - दिसंबर</span></td>
          <td><span class="lang-en">Showcases Awadhi Tehzeeb, Chikan embroidery, Kathak dance, and traditional cuisine</span><span class="lang-hi">अवध की नफासत, चिकनकारी, कथक, गजल एवं लखनवी खान-पान का प्रदर्शन</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Sulah-kul Utsav (सुलह-कुल उत्सव)</strong></span><span class="lang-hi"><strong>सुलह-कुल उत्सव</strong></span></td>
          <td><span class="lang-en">Agra</span><span class="lang-hi">आगरा</span></td>
          <td><span class="lang-en">October / Annual</span><span class="lang-hi">अक्टूबर / प्रतिवर्ष</span></td>
          <td><span class="lang-en">Established on Akbar's philosophy of universal religious peace and Hindu-Muslim harmony</span><span class="lang-hi">अकबर की सर्वधर्म समभाव नीति पर आधारित हिंदू-मुस्लिम सांप्रदायिक एकता का प्रतीक</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Ganga Mahotsav (गंगा महोत्सव)</strong></span><span class="lang-hi"><strong>गंगा महोत्सव</strong></span></td>
          <td><span class="lang-en">Varanasi (Rajghat / Dashashwamedh)</span><span class="lang-hi">वाराणसी (राजघाट/दशाश्वमेध)</span></td>
          <td><span class="lang-en">Kartik Purnima (Oct-Nov)</span><span class="lang-hi">कार्तिक पूर्णिमा (अक्टूबर-नवंबर)</span></td>
          <td><span class="lang-en">Classical Hindustani vocal &amp; instrumental recitals, boat races, culminates in Dev Deepawali</span><span class="lang-hi">शास्त्रीय संगीत व नृत्य की प्रस्तुतियां, नौकायन प्रतियोगिता, देव दीपावली पर समापन</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Jhansi Mahotsav / Ayurveda Utsav</strong></span><span class="lang-hi"><strong>झांसी महोत्सव / आयुर्वेद पर्व</strong></span></td>
          <td><span class="lang-en">Jhansi Fort complex</span><span class="lang-hi">झांसी दुर्ग परिसर</span></td>
          <td><span class="lang-en">February / November</span><span class="lang-hi">फरवरी / नवंबर</span></td>
          <td><span class="lang-en">Bundelkhandi martial arts, Rai dance, folk sangeet, and promotion of Ayurvedic medicinal herbs</span><span class="lang-hi">बुंदेलखंडी शौर्य, राई नृत्य, आल्हा गायन तथा औषधीय जड़ी-बूटी प्रदर्शनी</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kabir Utsav (कबीर उत्सव)</strong></span><span class="lang-hi"><strong>कबीर उत्सव</strong></span></td>
          <td><span class="lang-en">Maghar (Sant Kabir Nagar)</span><span class="lang-hi">मगहर (संत कबीर नगर)</span></td>
          <td><span class="lang-en">January</span><span class="lang-hi">जनवरी</span></td>
          <td><span class="lang-en">Celebrates Sant Kabir's egalitarian philosophy at his Nirvana / Samadhi site</span><span class="lang-hi">संत कबीर दास के निर्वाण स्थल पर उनकी निर्गुण वाणी एवं सामाजिक समरसता का उत्सव</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Ramayan Mela (रामायण मेला)</strong></span><span class="lang-hi"><strong>रामायण मेला</strong></span></td>
          <td><span class="lang-en">Ayodhya &amp; Chitrakoot</span><span class="lang-hi">अयोध्या एवं चित्रकूट</span></td>
          <td><span class="lang-en">Annual (started 1973)</span><span class="lang-hi">प्रतिवर्ष (प्रारंभ 1973)</span></td>
          <td><span class="lang-en">Founded by Dr. Ram Manohar Lohia in 1973; scholarly discourses on Ramcharitmanas</span><span class="lang-hi">डॉ. राम मनोहर लोहिया के प्रयासों से 1973 में प्रारंभ; रामकथा एवं सांस्कृतिक संवाद</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kampil Mahotsav (काम्पिल महोत्सव)</strong></span><span class="lang-hi"><strong>काम्पिल महोत्सव</strong></span></td>
          <td><span class="lang-en">Kampil (Farrukhabad)</span><span class="lang-hi">काम्पिल (फर्रुखाबाद)</span></td>
          <td><span class="lang-en">March</span><span class="lang-hi">मार्च</span></td>
          <td><span class="lang-en">Celebration of Jain Tirthankara Vimalnath's birthplace and ancient Panchala kingdom</span><span class="lang-hi">13वें जैन तीर्थंकर विमलनाथ की जन्मस्थली एवं प्राचीन पांचाल संस्कृति का उत्सव</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kajari Mahotsav (कजरी महोत्सव)</strong></span><span class="lang-hi"><strong>कजरी महोत्सव</strong></span></td>
          <td><span class="lang-en">Mirzapur</span><span class="lang-hi">मिर्जापुर</span></td>
          <td><span class="lang-en">Shravan / Bhadrapada (Monsoon)</span><span class="lang-hi">सावन / भाद्रपद (वर्षा ऋतु)</span></td>
          <td><span class="lang-en">Traditional monsoon folk singing competition celebrating folk goddess Kajali</span><span class="lang-hi">वर्षा ऋतु में लोक देवी कजली के सम्मान में कजरी गायन की ऐतिहासिक प्रतियोगिताएं</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kannauj Mahotsav (कन्नौज महोत्सव)</strong></span><span class="lang-hi"><strong>कन्नौज महोत्सव</strong></span></td>
          <td><span class="lang-en">Kannauj ('Attar Nagari')</span><span class="lang-hi">कन्नौज ('इत्र नगरी')</span></td>
          <td><span class="lang-en">Winter</span><span class="lang-hi">शीतकाल</span></td>
          <td><span class="lang-en">Promotion of indigenous floral distillation (Deg-Bhapka attar) and Harshavardhana legacy</span><span class="lang-hi">पारंपरिक देग-भपका इत्र उद्योग एवं सम्राट हर्षवर्धन की ऐतिहासिक विरासत का उत्सव</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 6: Comprehensive Major Fairs (Melas) Directory -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Comprehensive Directory of Historic Fairs &amp; Urs in UP</span>
    <span class="lang-hi">5. उत्तर प्रदेश के प्रमुख ऐतिहासिक मेलों एवं उर्स की विस्तृत सूची</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Name of Fair / Mela</span><span class="lang-hi">मेले / उत्सव का नाम</span></th>
          <th><span class="lang-en">District / Location</span><span class="lang-hi">जिला / स्थल</span></th>
          <th><span class="lang-en">Timing / Occasion</span><span class="lang-hi">अवसर / समय</span></th>
          <th><span class="lang-en">Core Feature &amp; Exam Relevance</span><span class="lang-hi">मुख्य विशेषता एवं परीक्षा तथ्य</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Bateshwar Mela (बटेश्वर मेला)</strong></span><span class="lang-hi"><strong>बटेश्वर मेला</strong></span></td>
          <td><span class="lang-en">Agra (Yamuna banks)</span><span class="lang-hi">आगरा (यमुना तट)</span></td>
          <td><span class="lang-en">Kartik Shukla Pratipada</span><span class="lang-hi">कार्तिक शुक्ल प्रतिपदा</span></td>
          <td><span class="lang-en">Largest camel, horse &amp; cattle fair in UP; dedicated to Lord Bateshwar Nath (101 Shiva temples)</span><span class="lang-hi">उ.प्र. का सबसे बड़ा ऊंट व पशु मेला; 101 शिव मंदिरों की श्रृंखला</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Dadhri Mela (ददरी मेला)</strong></span><span class="lang-hi"><strong>ददरी मेला</strong></span></td>
          <td><span class="lang-en">Ballia</span><span class="lang-hi">बलिया</span></td>
          <td><span class="lang-en">Kartik Purnima</span><span class="lang-hi">कार्तिक पूर्णिमा</span></td>
          <td><span class="lang-en">Second-largest cattle fair in UP; held in memory of sage Bhrigu's disciple Dardar Muni</span><span class="lang-hi">उ.प्र. का दूसरा सबसे बड़ा पशु मेला; महर्षि भृगु के शिष्य दर्दर मुनि की स्मृति में</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Nauchandi Mela (नौचंदी मेला)</strong></span><span class="lang-hi"><strong>नौचंदी मेला</strong></span></td>
          <td><span class="lang-en">Meerut</span><span class="lang-hi">मेरठ</span></td>
          <td><span class="lang-en">2nd Sunday after Holi (lasts 1 month)</span><span class="lang-hi">होली के दूसरे रविवार से (1 माह तक)</span></td>
          <td><span class="lang-en">Historic symbol of Hindu-Muslim unity (Navchandi Devi Temple &amp; Bale Mian Dargah face each other)</span><span class="lang-hi">सांप्रदायिक सौहार्द का प्रतीक; नवचंदी देवी मंदिर व बाले मियां की दरगाह आमने-सामने</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Deva Sharif Mela (देवा शरीफ मेला)</strong></span><span class="lang-hi"><strong>देवा शरीफ मेला</strong></span></td>
          <td><span class="lang-en">Barabanki</span><span class="lang-hi">बाराबंकी</span></td>
          <td><span class="lang-en">Kartik month (Oct-Nov)</span><span class="lang-hi">कार्तिक माह (अक्टूबर-नवंबर)</span></td>
          <td><span class="lang-en">Annual Urs at shrine of Sufi Saint Haji Waris Ali Shah (famous for universal love message)</span><span class="lang-hi">सूफी संत हाजी वारिस अली शाह की दरगाह पर वार्षिक उर्स; सर्वधर्म समभाव का संदेश</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Shakumbhari Devi Mela</strong></span><span class="lang-hi"><strong>शाकंभरी देवी मेला</strong></span></td>
          <td><span class="lang-en">Saharanpur (Shivalik hills)</span><span class="lang-hi">सहारनपुर (शिवालिक तलहटी)</span></td>
          <td><span class="lang-en">Chaitra &amp; Ashwin Navratri</span><span class="lang-hi">चैत्र व अश्विन नवरात्रि</span></td>
          <td><span class="lang-en">Ancient Shakumbhari Shaktipeeth; massive footfall from Western UP, Haryana, and Punjab</span><span class="lang-hi">प्राचीन शाकंभरी देवी शक्तिपीठ; पश्चिमी उ.प्र., हरियाणा व पंजाब के श्रद्धालुओं का केंद्र</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Govind Saheb Mela</strong></span><span class="lang-hi"><strong>गोविंद साहब मेला</strong></span></td>
          <td><span class="lang-en">Ambedkar Nagar (Atrariya)</span><span class="lang-hi">अंबेडकर नगर (अतरौलिया सीमा)</span></td>
          <td><span class="lang-en">Margashirsha (Agahan) Dashami</span><span class="lang-hi">अगहन शुक्ल दशमी</span></td>
          <td><span class="lang-en">Dedicated to Mahatma Govind Saheb; month-long fair known for livestock and handloom trade</span><span class="lang-hi">महात्मा गोविंद साहब की समाधि पर आयोजित; पशु व खादी हथकरघा व्यापार हेतु विख्यात</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Khichdi Mela (खिचड़ी मेला)</strong></span><span class="lang-hi"><strong>खिचड़ी मेला</strong></span></td>
          <td><span class="lang-en">Gorakhpur</span><span class="lang-hi">गोरखपुर</span></td>
          <td><span class="lang-en">Makar Sankranti (14-15 Jan)</span><span class="lang-hi">मकर संक्रांति (14-15 जनवरी)</span></td>
          <td><span class="lang-en">Historic Nath sect celebration at Gorakhnath Temple; devotees offer raw grains/khichdi</span><span class="lang-hi">गोरखनाथ मंदिर में नाथ संप्रदाय का ऐतिहासिक मेला; बाबा गोरखनाथ को खिचड़ी अर्पण</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Syed Salar Masud Ghazi Mela</strong></span><span class="lang-hi"><strong>सैयद सालार मेला</strong></span></td>
          <td><span class="lang-en">Bahraich</span><span class="lang-hi">बहराइच</span></td>
          <td><span class="lang-en">First Sunday of Jyeshtha</span><span class="lang-hi">ज्येष्ठ माह का प्रथम रविवार</span></td>
          <td><span class="lang-en">Held at Dargah of Ghazi Mian; attracts pilgrims across faiths offering ceremonial Nishans</span><span class="lang-hi">गाजी मियां की मजार पर आयोजित; श्रद्धालु गाजे-बाजे के साथ 'निशान' चढ़ाते हैं</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Soron Mela (सोरो मेला)</strong></span><span class="lang-hi"><strong>सोरो मेला</strong></span></td>
          <td><span class="lang-en">Kasganj (Shukar Kshetra)</span><span class="lang-hi">कासगंज (शूकर क्षेत्र)</span></td>
          <td><span class="lang-en">Margashirsha Ekadashi</span><span class="lang-hi">मार्गशीर्ष एकादशी</span></td>
          <td><span class="lang-en">Celebrated on banks of Ganga at site venerated for Lord Vishnu's Varaha (boar) avatar</span><span class="lang-hi">गंगा तट पर भगवान विष्णु के वराह अवतार स्थल के रूप में पूजित शूकर क्षेत्र</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Devi Patan Mela (देवी पाटन मेला)</strong></span><span class="lang-hi"><strong>देवी पाटन मेला</strong></span></td>
          <td><span class="lang-en">Tulsipur (Balrampur)</span><span class="lang-hi">तुलसीपुर (बलरामपुर)</span></td>
          <td><span class="lang-en">Chaitra Navratri</span><span class="lang-hi">चैत्र नवरात्रि</span></td>
          <td><span class="lang-en">Famous Shaktipeeth where Maa Sati's left shoulder (pat) fell; Indo-Nepal cross-border devotees</span><span class="lang-hi">सती का वाम स्कंध गिरने से स्थापित शक्तिपीठ; भारत-नेपाल मैत्री का प्रतीक</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Parikrama Mela (परिक्रमा मेला)</strong></span><span class="lang-hi"><strong>परिक्रमा मेला</strong></span></td>
          <td><span class="lang-en">Naimisharanya (Sitapur) &amp; Ayodhya</span><span class="lang-hi">नैमिषारण्य (सीतापुर) व अयोध्या</span></td>
          <td><span class="lang-en">Phalgun &amp; Kartik months</span><span class="lang-hi">फाल्गुन एवं कार्तिक माह</span></td>
          <td><span class="lang-en">84 Kosi Parikrama in Naimisharanya (land of 88,000 Rishis) and 14/5 Kosi in Ayodhya</span><span class="lang-hi">नैमिषारण्य में 84 कोसी परिक्रमा तथा अयोध्या धाम में 14 कोसी व 5 कोसी परिक्रमा</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kalinjar Mela (कालिंजर मेला)</strong></span><span class="lang-hi"><strong>कालिंजर मेला</strong></span></td>
          <td><span class="lang-en">Banda (Kalinjar Fort)</span><span class="lang-hi">बांदा (कालिंजर दुर्ग)</span></td>
          <td><span class="lang-en">Kartik Purnima</span><span class="lang-hi">कार्तिक पूर्णिमा</span></td>
          <td><span class="lang-en">Organized at historic Neelkanth Mahadev temple inside the impregnable Kalinjar fort</span><span class="lang-hi">कालिंजर दुर्ग स्थित नीलकंठ महादेव मंदिर परिसर में आयोजित ऐतिहासिक मेला</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Gola Gokaran Nath Mela</strong></span><span class="lang-hi"><strong>गोला गोकर्ण नाथ मेला</strong></span></td>
          <td><span class="lang-en">Lakhimpur Kheri</span><span class="lang-hi">लखीमपुर खीरी</span></td>
          <td><span class="lang-en">Maha Shivratri &amp; Chaitra</span><span class="lang-hi">महाशिवरात्रि एवं चैत्र माह</span></td>
          <td><span class="lang-en">Celebrated at Shiva temple known as 'Chhoti Kashi'; Ravana established lingam here</span><span class="lang-hi">'छोटी काशी' नाम से प्रसिद्ध प्राचीन शिव मंदिर में चैती मेले का आयोजन</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Belasundari Devi Mela</strong></span><span class="lang-hi"><strong>बेलासंदरी देवी मेला</strong></span></td>
          <td><span class="lang-en">Sambhal</span><span class="lang-hi">संभल</span></td>
          <td><span class="lang-en">Chaitra Navratri</span><span class="lang-hi">चैत्र नवरात्रि</span></td>
          <td><span class="lang-en">Celebrated at the ancient temple of Belasundari Devi</span><span class="lang-hi">प्राचीन बेलासंदरी देवी मंदिर में आयोजित पारंपरिक मेला</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Makhanpur Mela (मकनपुर मेला)</strong></span><span class="lang-hi"><strong>मकनपुर मेला</strong></span></td>
          <td><span class="lang-en">Kanpur Nagar (Bilhaur)</span><span class="lang-hi">कानपुर नगर (बिल्हौर)</span></td>
          <td><span class="lang-en">Magh month</span><span class="lang-hi">माघ माह</span></td>
          <td><span class="lang-en">Annual Urs at shrine of Sufi saint Badiuddin Zinda Shah Madar; horse and animal trading</span><span class="lang-hi">सूफी संत बदीउद्दीन जिंदा शाह मदार की दरगाह पर आयोजित; घोड़ों व पशुओं का व्यापार</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 7: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Fact Matrix: UP Festivals &amp; Fairs (Direct Exam Points)</span>
    <span class="lang-hi">6. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. के मेले व त्यौहार (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Festival Fact</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / त्योहार तथ्य</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">Which district hosts the highest number of fairs in UP?</span><span class="lang-hi">उ.प्र. में सर्वाधिक मेलों का आयोजन किस जिले में होता है?</span></td>
          <td><span class="lang-en"><strong>Mathura (86 fairs)</strong> (followed by Kanpur 80, Hamirpur 79)</span><span class="lang-hi"><strong>मथुरा (86 मेले)</strong> (इसके बाद कानपुर 80, हमीरपुर 79)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district hosts the lowest number of fairs in UP?</span><span class="lang-hi">उ.प्र. में न्यूनतम मेलों का आयोजन किस जिले में होता है?</span></td>
          <td><span class="lang-en"><strong>Pilibhit</strong> (least, only 2-3 fairs annually)</span><span class="lang-hi"><strong>पीलीभीत</strong> (प्रतिवर्ष मात्र 2-3 मेले)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the largest camel/cattle animal fair held in UP?</span><span class="lang-hi">उ.प्र. में सबसे बड़ा ऊंट/पशु मेला कहाँ लगता है?</span></td>
          <td><span class="lang-en"><strong>Bateshwar Mela (Agra)</strong> on the banks of Yamuna</span><span class="lang-hi"><strong>बटेश्वर मेला (आगरा)</strong> यमुना तट पर</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the second largest cattle fair organized in UP?</span><span class="lang-hi">उ.प्र. में दूसरा सबसे बड़ा पशु मेला कहाँ आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Dadhri Mela (Ballia)</strong> on Kartik Purnima</span><span class="lang-hi"><strong>ददरी मेला (बलिया)</strong> कार्तिक पूर्णिमा पर</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which fair in UP is celebrated as a symbol of Hindu-Muslim harmony?</span><span class="lang-hi">उ.प्र. का कौन सा मेला हिंदू-मुस्लिम सांप्रदायिक एकता का प्रतीक है?</span></td>
          <td><span class="lang-en"><strong>Nauchandi Mela (Meerut)</strong> &amp; <strong>Sulah-kul Utsav (Agra)</strong></span><span class="lang-hi"><strong>नौचंदी मेला (मेरठ)</strong> एवं <strong>सुलह-कुल उत्सव (आगरा)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">When and where is the Taj Mahotsav organized every year?</span><span class="lang-hi">प्रत्येक वर्ष ताज महोत्सव कहाँ और कब आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Agra (Shilpgram), 18 to 27 February</strong></span><span class="lang-hi"><strong>आगरा (शिल्पग्राम), 18 से 27 फरवरी</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is Lathmar Holi traditionally played?</span><span class="lang-hi">लठमार होली मुख्य रूप से कहाँ खेली जाती है?</span></td>
          <td><span class="lang-en"><strong>Barsana and Nandgaon (Mathura district)</strong></span><span class="lang-hi"><strong>बरसाना एवं नंदगांव (मथुरा जिला)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is Huranga celebrated the day after Holi?</span><span class="lang-hi">होली के अगले दिन 'हुरंगा' कहाँ मनाया जाता है?</span></td>
          <td><span class="lang-en"><strong>Dauji Temple, Baldeo (Mathura)</strong></span><span class="lang-hi"><strong>दाऊजी मंदिर, बलदेव (मथुरा)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is 'Chita Bhasma Holi' (Masane Ki Holi) celebrated?</span><span class="lang-hi">'चिता भस्म की होली' (मसाने की होली) कहाँ खेली जाती है?</span></td>
          <td><span class="lang-en"><strong>Manikarnika Ghat, Varanasi (Rangbhari Ekadashi)</strong></span><span class="lang-hi"><strong>मणिकर्णिका घाट, वाराणसी (रंगभरी एकादशी)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the famous Deva Sharif Mela organized?</span><span class="lang-hi">प्रसिद्ध देवा शरीफ मेला कहाँ आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Barabanki</strong> (Shrine of Sufi saint Haji Waris Ali Shah)</span><span class="lang-hi"><strong>बाराबंकी</strong> (सूफी संत हाजी वारिस अली शाह की दरगाह)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Syed Salar Masud Ghazi fair held?</span><span class="lang-hi">सैयद सालार मसूद गाजी मेला कहाँ लगता है?</span></td>
          <td><span class="lang-en"><strong>Bahraich</strong> (in Jyeshtha month)</span><span class="lang-hi"><strong>बहराइच</strong> (ज्येष्ठ माह में)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Khichdi Mela held on Makar Sankranti?</span><span class="lang-hi">मकर संक्रांति पर खिचड़ी मेला कहाँ आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Gorakhpur (Gorakhnath Temple)</strong></span><span class="lang-hi"><strong>गोरखपुर (गोरखनाथ मंदिर)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Shakumbhari Devi Mela held?</span><span class="lang-hi">शाकंभरी देवी मेला कहाँ आयोजित होता है?</span></td>
          <td><span class="lang-en"><strong>Saharanpur</strong> (during Navratri)</span><span class="lang-hi"><strong>सहारनपुर</strong> (नवरात्रि के दौरान)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which tribe celebrates Deepawali as a day of mourning (Shok Parv)?</span><span class="lang-hi">उ.प्र. की कौन सी जनजाति दीपावली को शोक पर्व के रूप में मनाती है?</span></td>
          <td><span class="lang-en"><strong>Tharu Tribe (थारू जनजाति)</strong></span><span class="lang-hi"><strong>थारू जनजाति</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Where is the Ramayan Mela annually organized?</span><span class="lang-hi">रामायण मेले का आयोजन प्रतिवर्ष कहाँ किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Ayodhya and Chitrakoot</strong> (started in 1973 by Dr. Lohia)</span><span class="lang-hi"><strong>अयोध्या एवं चित्रकूट</strong> (1973 में डॉ. लोहिया द्वारा प्रारंभ)</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "festivals", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_festivals_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
