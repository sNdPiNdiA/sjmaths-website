import os
import re

def build_social_customs_tourism_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Social Customs Spectrum &amp; Tourism Circuits of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के सामाजिक रीति-रिवाज एवं पर्यटन परिपथ (सर्किट)</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Social Customs & Tourism of UP] --> B[16 Samskaras & Life-Cycle Customs]
    A --> C[Regional Folk & Tribal Customs]
    A --> D[UP Tourism Policy 2022 & Footfall]
    A --> E[Heritage Arc & Mega Circuits]
    A --> F[Specialized Cultural Circuits]
    A --> G[UNESCO Heritage & Tourism Infrastructure]

    B --> B1[Birth: Jatakarma, Namakarana, Nishkramana, Annaprashana, Chudakarana/Mundan]
    B --> B2[Initiation: Upanayana/Janeu & Vedarambha]
    B --> B3[Marriage: Vivaha Kanyadan, Dwar-Pooja, Saptapadi, Kohbar, Bidaai]
    B --> B4[Death: Antyeshti, Pind Daan Gaya/Kashi/Prayagraj, Terahvi]

    C --> C1[Purvanchal & Awadh: Sohar Birth Songs, Nakta, Chowk Poorana]
    C --> C2[Braj: Charkula, Lathmar Holi, Dauji Huranga]
    C --> C3[Tribal: Tharu Joint Families, Badwa Elders, Diwali Mourning, Jhitiya]

    D --> D1[Footfall Rank: Rank 1 in Domestic Tourists >32 Cr Annual Visitors]
    D --> D2[Policy 2022: ₹20,000 Cr Investment Target | 12 Thematic Circuits]
    D --> D3[Schemes: Bed & Breakfast, Homestays, Caravan Tourism, Agri-Tourism]

    E --> E1[Heritage Arc: Agra - Lucknow - Varanasi Golden Triangle]
    E --> E2[Ramayana Circuit: Ayodhya, Chitrakoot, Shringverpur, Bithoor]
    E --> E3[Krishna Circuit: Mathura, Vrindavan, Barsana, Govardhan, Gokul]
    E --> E4[Buddhist Circuit: Sarnath, Kushinagar, Shravasti, Kapilvastu, Sankisa, Kaushambi]

    F --> F1[Bundelkhand: Jhansi, Kalinjar Banda, Deogarh Lalitpur, Mahoba]
    F --> F2[Sufi Circuit: Salim Chishti Sikri, Dewa Sharif, Syed Salar Bahraich]
    F --> F3[Jain Circuit: Ayodhya 5 Tirthankaras, Kashi, Kaushambi, Deogarh]

    G --> G1[UNESCO Tangible: Taj Mahal 1983, Agra Fort 1983, Fatehpur Sikri 1986]
    G --> G2[UNESCO Intangible: Ramlila 2008, Vedic Chanting 2008, Kumbh Mela 2017]
    G --> G3[UPSTDC: Established 1974 | Rahi Tourist Bungalows]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के रीति-रिवाज एवं पर्यटन] --> B[षोडश संस्कार एवं जीवन-चक्र रीति]
    A --> C[क्षेत्रीय लोक एवं जनजातीय प्रथाएं]
    A --> D[पर्यटन नीति 2022 एवं पर्यटक आगमन]
    A --> E[हेरिटेज आर्क एवं प्रमुख सर्किट]
    A --> F[विशिष्ट सांस्कृतिक परिपथ]
    A --> G[यूनेस्को धरोहर एवं पर्यटन अवसंरचना]

    B --> B1[जन्म: जातकर्म, नामकरण, निष्क्रमण, अन्नप्राशन, चूड़ाकर्म/मुंडन]
    B --> B2[दीक्षा: उपनयन/जनेऊ एवं वेदारंभ]
    B --> B3[विवाह: कन्यादान, द्वारपूजा, सप्तपदी, कोहबर, विदाई]
    B --> B4[मृत्यु: अंत्येष्टि, पिंडदान प्रयागराज/काशी, तेरहवीं]

    C --> C1[पूर्वांचल व अवध: सोहर जन्मोत्सव, नकटा, चौक पूरना]
    C --> C2[ब्रज: चरकुला, लठमार होली, दाऊजी हुरंगा]
    C --> C3[जनजातीय: थारू संयुक्त परिवार, बड़वा मुखिया, दीपावली शोक पर्व, झितीया]

    D --> D1[पर्यटक आगमन: घरेलू पर्यटन में देश में प्रथम स्थान >32 करोड़]
    D --> D2[पर्यटन नीति 2022: ₹20,000 करोड़ निवेश लक्ष्य | 12 थीम आधारित सर्किट]
    D --> D3[योजनाएं: बेड एंड ब्रेकफास्ट, होमस्टे, कारवां पर्यटन, कृषि-पर्यटन]

    E --> E1[हेरिटेज आर्क: आगरा - लखनऊ - वाराणसी स्वर्णिम त्रिकोण]
    E --> E2[रामायण सर्किट: अयोध्या, चित्रकूट, श्रृंगवेरपुर, बिठूर]
    E --> E3[कृष्ण सर्किट: मथुरा, वृंदावन, बरसाना, गोवर्धन, गोकुल]
    E --> E4[बौद्ध सर्किट: सारनाथ, कुशीनगर, श्रावस्ती, कपिलवस्तु, संकिसा, कौशाम्बी]

    F --> F1[बुंदेलखंड सर्किट: झांसी, कालिंजर बांदा, देवगढ़ ललितपुर, महोबा]
    F --> F2[सूफी सर्किट: सलीम चिश्ती सीकरी, देवा शरीफ, सैयद सालार बहराइच]
    F --> F3[जैन सर्किट: अयोध्या 5 तीर्थंकर जन्मभूमि, काशी, कौशाम्बी, देवगढ़]

    G --> G1[यूनेस्को मूर्त: ताजमहल 1983, आगरा किला 1983, फतेहपुर सीकरी 1986]
    G --> G2[यूनेस्को अमूर्त: रामलीला 2008, वैदिक मंत्रोच्चार 2008, कुंभ मेला 2017]
    G --> G3[UPSTDC: स्थापना 1974 | राही पर्यटक आवास]
    </div>
  </div>
</div>

<!-- Card 2: 16 Samskaras & Life-Cycle Customs in UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Sixteen Samskaras (षोडश संस्कार) &amp; Traditional Life-Cycle Rituals</span>
    <span class="lang-hi">1. षोडश (16) संस्कार एवं पारंपरिक जीवन-चक्र रीति-रिवाज</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Cosmological Significance:</strong> The traditional social fabric of Uttar Pradesh is deeply anchored in the ancient <strong>16 Samskaras (षोडश संस्कार)</strong> prescribed in the Grihya Sutras, sanctifying individual milestones from conception to departure.</span>
        <span class="lang-hi"><strong>वैदिक एवं सामाजिक महत्व:</strong> उत्तर प्रदेश का पारंपरिक समाज गृह्यसूत्रों में वर्णित <strong>षोडश (16) संस्कारों</strong> पर आधारित है, जो गर्भाधान से लेकर मृत्यु पर्यंत जीवन के प्रत्येक चरण को पवित्र एवं अनुशासित करते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Prenatal &amp; Childhood Samskaras (जन्म पूर्व एवं बाल संस्कार):</strong>
          <br>&bull; <em>Garbhadhana (गर्भाधान):</em> Conception prayer for healthy progeny.
          <br>&bull; <em>Pumsavana &amp; Simantonnayana (पुंसवन व सीमंतोन्नयन):</em> Fetal protection and mother's psychological well-being (Godh Bharai ritual).
          <br>&bull; <em>Jatakarma (जातकर्म):</em> Birth ceremony; father licks honey and ghee to the newborn before umbilical cord separation.
          <br>&bull; <em>Namakarana (नामकरण):</em> Naming on the 10th or 11th day; accompanied by chanting and family feasting.
          <br>&bull; <em>Nishkramana (निष्क्रमण):</em> First outdoor outing of the child to gaze at the Sun and Moon (4th month).
          <br>&bull; <em>Annaprashana (अन्नप्राशन):</em> First feeding of solid food / rice-kheer (6th month).
          <br>&bull; <em>Chudakarana / Mundan (चूड़ाकर्म / मुंडन):</em> First tonsure of hair (1st or 3rd year), frequently performed at holy riverbanks (Ganga at Prayagraj, Kashi, or Garhmukteshwar).
          <br>&bull; <em>Karnavedha (कर्णवेध):</em> Piercing of ear lobes for health and acupuncture benefits.</span>
        <span class="lang-hi"><strong>जन्म पूर्व एवं बाल संस्कार:</strong>
          <br>&bull; <em>गर्भाधान:</em> श्रेष्ठ संतति हेतु प्रथम संस्कार।
          <br>&bull; <em>पुंसवन एवं सीमंतोन्नयन:</em> गर्भस्थ शिशु की सुरक्षा एवं माता के मानसिक स्वास्थ्य हेतु (गोद भराई की रस्म)।
          <br>&bull; <em>जातकर्म:</em> जन्मोपरांत शिशु को शहद व घृत चटाना तथा नाल छेदन।
          <br>&bull; <em>नामकरण:</em> जन्म के 10वें या 11वें दिन कुल पुरोहित द्वारा नामकरण संस्कार।
          <br>&bull; <em>निष्क्रमण:</em> चौथे माह में शिशु को प्रथम बार घर से बाहर सूर्य व चंद्र दर्शन कराना।
          <br>&bull; <em>अन्नप्राशन:</em> छठे माह में शिशु को प्रथम बार ठोस अन्न (खीर) खिलाना।
          <br>&bull; <em>चूड़ाकर्म / मुंडन:</em> प्रथम या तृतीय वर्ष में बच्चे के सिर के बाल मुंडवाना, जो प्रायः तीर्थस्थलों (प्रयागराज, काशी, गढ़मुक्तेश्वर) पर संपन्न होता है।
          <br>&bull; <em>कर्णवेध:</em> स्वास्थ्य व एक्यूपंक्चर लाभ हेतु कान छिदवाना।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Educational &amp; Initiatory Samskaras (विद्या एवं दीक्षा संस्कार):</strong>
          <br>&bull; <em>Vidyarambha (विद्यारंभ / पाटी पूजन):</em> Commencement of learning alphabet on Akshaya Tritiya or Vasant Panchami.
          <br>&bull; <em>Upanayana / Janeu (उपनयन / यज्ञोपवीत):</em> Sacred thread investiture symbolizing spiritual rebirth (Dvija); chanting of Gayatri Mantra.
          <br>&bull; <em>Vedarambha, Keshanta (Godana), &amp; Samavartana (स्नान / समावर्तन):</em> Formal completion of Gurukula education and return home for Grihastha Ashrama.</span>
        <span class="lang-hi"><strong>विद्या एवं दीक्षा संस्कार:</strong>
          <br>&bull; <em>विद्यारंभ (पाटी पूजन):</em> अक्षर ज्ञान की शुरुआत (अक्षय तृतीया या वसंत पंचमी पर)।
          <br>&bull; <em>उपनयन / यज्ञोपवीत (जनेऊ):</em> पवित्र सूत का त्रिगुण धागा धारण कर द्विजत्व प्राप्त करना एवं गायत्री मंत्र दीक्षा।
          <br>&bull; <em>वेदारंभ, केशांत (गोदान) एवं समावर्तन (स्नान):</em> गुरुकुल शिक्षा पूर्ण कर गृहस्थ आश्रम में प्रवेश हेतु दीक्षांत समारोह।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Vivaha &amp; Antyeshti (विवाह एवं अंत्येष्टि संस्कार):</strong>
          <br>&bull; <em>Vivaha (विवाह संस्कार):</em> Grihastha foundation; comprises <strong>Tilak/Bariksha, Dwar-Pooja, Jayamala, Kanyadan, Pani-Grahana, Saptapadi (सात फेरे around sacred Agni), Kohbar (bridal chamber art), and Sindoor-Daan</strong>.
          <br>&bull; <em>Antyeshti (अंत्येष्टि संस्कार):</em> Final rites; cremation with Agni Sanskar, Kapala Kriya; Asthi Visarjan at Sangam (Prayagraj) or Manikarnika Ghat (Varanasi); followed by Terahvi (13th day community feast) and annual Shradh (Pind Daan).</span>
        <span class="lang-hi"><strong>विवाह एवं अंत्येष्टि संस्कार:</strong>
          <br>&bull; <em>विवाह संस्कार:</em> गृहस्थ जीवन का आधार; <strong>तिलक/बरीक्षा, द्वारपूजा, जयमाला, कन्यादान, पाणिग्रहण, सप्तपदी (अग्नि के समक्ष सात फेरे), कोहबर पूजन एवं सिंदूरदान</strong>।
          <br>&bull; <em>अंत्येष्टि संस्कार:</em> 16वां व अंतिम संस्कार; अग्नि संस्कार, कपाल क्रिया; प्रयागराज संगम या काशी मणिकर्णिका पर अस्थि विसर्जन; 13वें दिन तेरहवीं तथा प्रतिवर्ष पितृपक्ष में पिंडदान (श्राद्ध)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Regional Folk Customs & Tribal Traditions -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Regional Folk Customs, Ritual Art &amp; Tribal Traditions of UP</span>
    <span class="lang-hi">2. उत्तर प्रदेश के क्षेत्रीय लोक रीति-रिवाज, मांगलिक कला एवं जनजातीय परंपराएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Folk Celebrations of Life &amp; Ritual Art:</strong>
          <br>&bull; <em>Sohar (सोहर):</em> Auspicious folk songs sung by women on the birth of a child across Awadh and Purvanchal (immortalized in Goswami Tulsidas's <em>Ram Lala Nahachhu</em>).
          <br>&bull; <em>Chowk Poorana (चौक पूरना):</em> Traditional floor art created with wheat flour, turmeric, and dry colors at the threshold during all auspicious rituals.
          <br>&bull; <em>Kohbar Art (कोहबर कला):</em> Symbolic ritual wall mural painted in the nuptial chamber depicting fertility symbols (lotus, bamboo clump, fish, turtle, sun, and moon).
          <br>&bull; <em>Nakta / Domkach (नकटा / डोमकच):</em> Women-only humorous folk theatre performed in the groom's house through the wedding night after the Barat departs.</span>
        <span class="lang-hi"><strong>मांगलिक लोक परंपराएं एवं अनुष्ठान कला:</strong>
          <br>&bull; <em>सोहर:</em> अवध और पूर्वांचल में शिशु जन्मोत्सव पर महिलाओं द्वारा गाए जाने वाले मंगल गीत (गोस्वामी तुलसीदास कृत <em>रामलला नहछू</em> में वर्णित)।
          <br>&bull; <em>चौक पूरना:</em> मांगलिक अवसरों पर घर के आंगन व देहरी पर आटे, हल्दी व सूखे रंगों से बनाई जाने वाली पारंपरिक मांडणा कला।
          <br>&bull; <em>कोहबर कला:</em> विवाह के समय नवदंपति के कक्ष की दीवार पर उर्वरता व वंश-वृद्धि के प्रतीकों (कमल, बांस, मछली, कछुआ, सूर्य-चंद्र) का मांगलिक भित्ति-चित्रण।
          <br>&bull; <em>नकटा / डोमकच:</em> बारात विदा होने के बाद वर-पक्ष के घर में महिलाओं द्वारा रात्रिभर किया जाने वाला स्वांग व हास्य लोक नाटक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Tribal Customs &amp; Social Practices (जनजातीय रीति-रिवाज):</strong>
          <br>&bull; <em>Tharu Tribe (थारू जनजाति - Terai Belt):</em>
            - Joint Family System (संयुक्त परिवार प्रथा): Headed by the eldest male known as <em>Badwa (बड़वा)</em>; matriarch is <em>Badi Badi (बड़ी बड्डी)</em>.
            - Mourning on Diwali (दीपावली को शोक पर्व के रूप में): Tharus observe Diwali as a day of ancestor remembrance, performing the <em>Bhent / Jhitiya</em> ritual.
            - Badla Marriage (बदला विवाह): Traditional reciprocal cross-cousin marriages (now declining).
            - Local Beverage: <em>Jaand (जांड़)</em> - traditional fermented rice beer.
          <br>&bull; <em>Buxa Tribe (बुक्सा जनजाति - Bijnor):</em>
            - Social organization: Governed by local caste panchayats headed by <em>Takhat (तखत)</em>, followed by Munsif and Daroga.
            - Worship: Reverence for Kashipur Chamunda Devi and local forest deities.
          <br>&bull; <em>Agariya &amp; Kharwar Tribes (Sonbhadra):</em>
            - Agariyas practice ancient black iron smelting rituals with Lohasur worship; Kharwars celebrate Karma tree rituals.</span>
        <span class="lang-hi"><strong>जनजातीय रीति-रिवाज एवं सामाजिक प्रथाएं:</strong>
          <br>&bull; <em>थारू जनजाति (तराई क्षेत्र - लखीमपुर, बहराइच, बलरामपुर):</em>
            - संयुक्त परिवार प्रणाली: परिवार का वयोवृद्ध मुखिया <em>बड़वा</em> तथा वृद्ध महिला <em>बड़ी बड्डी</em> कहलाती है।
            - दीपावली पर शोक पर्व: थारू लोग दीपावली को अपने पूर्वजों की याद में शोक पर्व के रूप में मनाते हैं और 'भेंट/पुतला' विसर्जित करते हैं।
            - बदला विवाह: बहन-विनिमय पर आधारित पारंपरिक विवाह प्रथा (अब लुप्तप्राय)।
            - पारंपरिक पेय: चावल से निर्मित मदिरा <em>जांड़</em>।
          <br>&bull; <em>बुक्सा जनजाति (बिजनौर):</em>
            - सामाजिक न्याय व्यवस्था: बिरादरी पंचायत द्वारा शासित, जिसका सर्वोच्च अधिकारी <em>तखत</em> होता है (उसके बाद मुंसिफ व दारोगा)।
            - इष्टदेवी: काशीपुर की चामुंडा देवी की विशेष पूजा।
            - पितृसत्तात्मक परिवार और अनुलोम-प्रतिलोम विवाह।
          <br>&bull; <em>अगरिया एवं खरवार जनजाति (सोनभद्र):</em>
            - अगरिया जनजाति लौह-गलाने के पारंपरिक अनुष्ठान व 'लोहासुर' की पूजा करती है; खरवार जनजाति कर्म वृक्ष (कर्मा पूजा) की आराधना करती है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Tourism Policy 2022 & Footfall Dominance -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Uttar Pradesh Tourism Policy 2022 &amp; Historic Footfall Leadership</span>
    <span class="lang-hi">3. उत्तर प्रदेश पर्यटन नीति 2022 एवं ऐतिहासिक पर्यटक आगमन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>National Tourism Footfall Leadership:</strong> Uttar Pradesh ranks <strong>Rank 1 in India in Domestic Tourist Visits</strong>, recording over <strong>32+ crore domestic tourists</strong> annually following the rejuvenation of the Kashi Vishwanath Dham Corridor (Varanasi), the consecration of the Shri Ram Janmabhoomi Mandir (Ayodhya), and Braj Teerth Vikas projects.</span>
        <span class="lang-hi"><strong>घरेलू पर्यटन में देश में प्रथम स्थान:</strong> काशी विश्वनाथ धाम कॉरिडोर (वाराणसी), श्रीराम जन्मभूमि मंदिर (अयोध्या) तथा ब्रज तीर्थ विकास परियोजनाओं के फलस्वरूप उत्तर प्रदेश <strong>घरेलू पर्यटकों के आगमन में भारत में प्रथम स्थान</strong> पर है, जहां प्रतिवर्ष <strong>32 करोड़ से अधिक घरेलू पर्यटक</strong> आते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP Tourism Policy 2022 Highlights:</strong>
          <br>&bull; <em>Investment Target:</em> Attract <strong>₹20,000 crore investment</strong> in tourism infrastructure and generate 10 lakh jobs over 5 years.
          <br>&bull; <em>Subsidies:</em> Capital investment subsidies (up to 25%), interest subsidies (up to 5%), stamp duty exemption (100%), and SGST reimbursement for new hotels and wellness resorts.
          <br>&bull; <em>Homestay &amp; Bed &amp; Breakfast Scheme:</em> Promotes rural homestays and heritage stay networks in pilgrim centers with financial incentives to local house owners.
          <br>&bull; <em>Caravan Tourism &amp; Wellness Tourism:</em> Establishment of designated Caravan parks, Ayurvedic and Naturopathy wellness retreats.</span>
        <span class="lang-hi"><strong>यूपी पर्यटन नीति 2022 की मुख्य विशेषताएं:</strong>
          <br>&bull; <em>निवेश लक्ष्य:</em> पर्यटन अवसंरचना में <strong>₹20,000 करोड़ का निवेश</strong> आकर्षित करना एवं 5 वर्षों में 10 लाख रोजगार सृजित करना।
          <br>&bull; <em>वित्तीय प्रोत्साहन:</em> नए होटलों व रिसॉर्ट्स को 25% तक पूंजी निवेश सब्सिडी, 5% ब्याज सब्सिडी, 100% स्टांप शुल्क छूट तथा एसजीएसटी प्रतिपूर्ति।
          <br>&bull; <em>होमस्टे एवं बेड एंड ब्रेकफास्ट योजना:</em> तीर्थस्थलों व ग्रामीण अंचलों में स्थानीय गृहस्वामियों को वित्तीय प्रोत्साहन देकर होमस्टे नेटवर्क का विस्तार।
          <br>&bull; <em>कारवां एवं वेलनेस पर्यटन:</em> समर्पित कारवां पार्कों की स्थापना तथा आयुर्वेदिक/प्राकृतिक चिकित्सा केंद्रों को उद्योग का दर्जा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP State Tourism Development Corporation (UPSTDC):</strong> Established in <strong>1974</strong>; operates the famous <em>'Rahi' (राही)</em> chain of tourist bungalows, hotels, and conducts curated package tours across the state.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश राज्य पर्यटन विकास निगम (UPSTDC):</strong> स्थापना <strong>1974</strong> में; राज्यभर में <em>'राही'</em> पर्यटक आवासों व होटलों का संचालन तथा टूरिस्ट पैकेज का प्रबंधन करता है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Comprehensive Tourism Circuits: Heritage Arc, Ramayana, Krishna & Buddhist -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Mega Tourism Circuits: Heritage Arc, Ramayana, Krishna &amp; Buddhist Circuits</span>
    <span class="lang-hi">4. प्रमुख पर्यटन परिपथ: हेरिटेज आर्क, रामायण, कृष्ण एवं बौद्ध सर्किट</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Heritage Arc (हेरिटेज आर्क - Golden Triangle of UP Tourism):</strong>
          <br>&bull; <em>Agra Node:</em> Mughal glory, UNESCO sites (Taj Mahal, Agra Fort, Fatehpur Sikri), Sikandra (Akbar's tomb), Itmad-ud-Daulah.
          <br>&bull; <em>Lucknow Node:</em> Nawabi architecture and culture, Bara Imambara (Bhool Bhulaiya), Chhota Imambara, Rumi Darwaza, British Residency, Chattar Manzil.
          <br>&bull; <em>Varanasi Node:</em> Spiritual capital of India, Kashi Vishwanath Temple &amp; Corridor, 84 historic Ghats (Dashashwamedh Ganga Aarti, Assi, Manikarnika), Sarnath.</span>
        <span class="lang-hi"><strong>हेरिटेज आर्क (उत्तर प्रदेश पर्यटन का स्वर्णिम त्रिकोण):</strong>
          <br>&bull; <em>आगरा केंद्र:</em> मुगल वास्तुकला, यूनेस्को धरोहरें (ताजमहल, आगरा किला, फतेहपुर सीकरी), सिकंदरा (अकबर का मकबरा), एत्मादुद्दौला।
          <br>&bull; <em>लखनऊ केंद्र:</em> नवाबी तहजीब व स्थापत्य, बड़ा इमामबाड़ा (भूलभुलैया), छोटा इमामबाड़ा, रूमी दरवाजा, ब्रिटिश रेजिडेंसी, छतर मंजिल।
          <br>&bull; <em>वाराणसी केंद्र:</em> भारत की आध्यात्मिक राजधानी, काशी विश्वनाथ धाम कॉरिडोर, 84 गंगा घाट (दशाश्वमेध महाआरती, अस्सी, मणिकर्णिका), सारनाथ।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Ramayana Circuit (रामायण सर्किट):</strong>
          <br>&bull; <em>Ayodhya:</em> Birthplace of Lord Rama, grand Shri Ram Janmabhoomi Mandir, Kanak Bhawan, Hanuman Garhi, Saryu Ghats (Ram Ki Paidi).
          <br>&bull; <em>Chitrakoot:</em> Site of 11.5 years of Lord Rama's exile, Kamadgiri Parikrama, Ramghat on Mandakini river, Bharat Milap, Gupt Godavari, Sati Anusuya Ashram.
          <br>&bull; <em>Shringverpur (Prayagraj):</em> Historic spot where Nishadraj Kevat washed Lord Rama's feet and ferried Him across Ganga.
          <br>&bull; <em>Bithoor (Kanpur):</em> Valmiki Ashram where Mata Sita resided and Luv-Kush were born; Brahmavarta Ghat.</span>
        <span class="lang-hi"><strong>रामायण सर्किट:</strong>
          <br>&bull; <em>अयोध्या:</em> भगवान श्री राम की जन्मस्थली, भव्य श्रीराम जन्मभूमि मंदिर, कनक भवन, हनुमान गढ़ी, सरयू तट (राम की पैड़ी)।
          <br>&bull; <em>चित्रकूट:</em> भगवान राम के 11.5 वर्ष वनवास का स्थल, कामदगिरि परिक्रमा, मंदाकिनी तट पर रामघाट, भरत मिलाप, गुप्त गोदावरी, सती अनुसूया आश्रम।
          <br>&bull; <em>श्रृंगवेरपुर (प्रयागराज):</em> निषादराज केवट द्वारा भगवान राम के चरण पखारने और गंगा पार कराने का ऐतिहासिक स्थल।
          <br>&bull; <em>बिठूर (कानपुर):</em> महर्षि वाल्मीकि आश्रम जहां माता सीता ने निवास किया व लव-कुश का जन्म हुआ; ब्रह्मावर्त घाट।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Krishna / Braj Circuit (कृष्ण / ब्रज सर्किट):</strong>
          <br>&bull; <em>Mathura:</em> Shri Krishna Janmasthan, Vishram Ghat, Dwarkadhish Temple.
          <br>&bull; <em>Vrindavan:</em> Bankey Bihari Temple, Prem Mandir, ISKCON Krishna Balaram Temple, Nidhivan, Radha Raman Temple.
          <br>&bull; <em>Barsana:</em> Shri Radha Rani Temple (Ladli Ji), epicenter of world-famous Lathmar Holi.
          <br>&bull; <em>Govardhan:</em> Sacred Govardhan Hill (21 km Parikrama), Mansi Ganga, Radha Kund, Shyam Kund.
          <br>&bull; <em>Gokul &amp; Nandgaon:</em> Chhadimar Holi, Raman Reti, 84 Khamba Temple.</span>
        <span class="lang-hi"><strong>कृष्ण / ब्रज सर्किट:</strong>
          <br>&bull; <em>मथुरा:</em> श्रीकृष्ण जन्मस्थान, विश्राम घाट, द्वारकाधीश मंदिर।
          <br>&bull; <em>वृंदावन:</em> बांके बिहारी मंदिर, प्रेम मंदिर, इस्कॉन मंदिर, निधिवन, राधा रमण मंदिर।
          <br>&bull; <em>बरसाना:</em> श्री राधा रानी मंदिर (लाडली जी), विश्वप्रसिद्ध लठमार होली का केंद्र।
          <br>&bull; <em>गोवर्धन:</em> पावन गोवर्धन पर्वत (21 किमी परिक्रमा), मानसी गंगा, राधा कुंड, श्याम कुंड।
          <br>&bull; <em>गोकुल व नंदगांव:</em> छड़ीमार होली, रमण रेती, 84 खंभा मंदिर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Buddhist Circuit (बौद्ध सर्किट):</strong>
          <br>&bull; <em>Sarnath (Varanasi):</em> <strong>Dhammacakkappavattana</strong> (First Sermon); Dhamekh Stupa, Chaukhandi Stupa, Ashoka Lion Capital (National Emblem).
          <br>&bull; <em>Kushinagar:</em> <strong>Mahaparinirvana</strong> of Lord Buddha; Mahaparinirvana Stupa (6.1 meter reclining Buddha statue), Ramabhar Stupa (cremation site).
          <br>&bull; <em>Shravasti:</em> Jetavana Monastery; site where Buddha spent 24 monsoon retreats (Vassavasa) and performed greatest miracles (Yamaka-Patihāriya); Angulimala Stupa.
          <br>&bull; <em>Kapilvastu (Piprahwa, Siddharthnagar):</em> Royal childhood capital of Prince Siddhartha; archaeological discovery of Buddha relic caskets.
          <br>&bull; <em>Sankisa (Farrukhabad):</em> Legend of Buddha's descent from Trayastrimsa Heaven; Asokan Elephant Capital.
          <br>&bull; <em>Kaushambi:</em> Ghositarama Monastery visited by Buddha; capital of ancient Vatsa Mahajanapada.</span>
        <span class="lang-hi"><strong>बौद्ध सर्किट:</strong>
          <br>&bull; <em>सारनाथ (वाराणसी):</em> <strong>धर्मचक्रप्रवर्तन</strong> (प्रथम उपदेश); धमेख स्तूप, चौखंडी स्तूप, अशोक का सिंह शीर्ष स्तंभ (हमारा राष्ट्रीय प्रतीक)।
          <br>&bull; <em>कुशीनगर:</em> भगवान बुद्ध का <strong>महापरिनिर्वाण</strong>; महापरिनिर्वाण मंदिर (6.1 मीटर लेटी हुई बुद्ध प्रतिमा), रामाभार स्तूप (अंतिम संस्कार स्थल)।
          <br>&bull; <em>श्रावस्ती:</em> जेतवन महाविहार; जहां बुद्ध ने सर्वाधिक 24 वर्षावास (वर्षावास) बिताए एवं यमक-प्रातिहार्य चमत्कार दिखाए; अंगुलिमाल स्तूप।
          <br>&bull; <em>कपिलवस्तु (पिपरहवा, सिद्धार्थनगर):</em> राजकुमार सिद्धार्थ का बाल्यकाल राजप्रसाद; शाक्य बुद्ध धातु-मंजूषा की खोज।
          <br>&bull; <em>संकिसा (फर्रुखाबाद):</em> बुद्ध के त्रयस्त्रिंश स्वर्ग से पृथ्वी पर अवतरण की मान्यता; अशोक का गज (हाथी) शीर्ष स्तंभ।
          <br>&bull; <em>कौशाम्बी:</em> घोषिताराम विहार जहां बुद्ध ने उपदेश दिए; प्राचीन वत्स महाजनपद की राजधानी।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Specialized Circuits: Bundelkhand, Sufi, Jain, Eco-Tourism & Craft -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Specialized Cultural Circuits: Bundelkhand, Sufi, Jain &amp; Eco-Tourism</span>
    <span class="lang-hi">5. विशिष्ट सांस्कृतिक परिपथ: बुंदेलखंड, सूफी, जैन एवं ईको-पर्यटन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Bundelkhand Circuit (बुंदेलखंड सर्किट):</strong>
          <br>&bull; <em>Jhansi:</em> Historic Jhansi Fort (built 1613 by Raja Bir Singh Deo), Rani Mahal (mural paintings), Government Museum.
          <br>&bull; <em>Kalinjar Fort (Banda):</em> Ancient impregnable hill fort on Vindhyan range; Neelkanth Temple, site of Sher Shah Suri's fatal blast in 1545.
          <br>&bull; <em>Deogarh (Lalitpur):</em> Gupta-era Dashavatara Temple (earliest North Indian temple with a shikhara and Panchayatana plan); 31 Jain temples inside the fort.
          <br>&bull; <em>Mahoba:</em> Historic Chandela capital, Sun Temple of Rahila, Vijay Sagar lake, shrines of Alha and Udal.</span>
        <span class="lang-hi"><strong>बुंदेलखंड सर्किट:</strong>
          <br>&bull; <em>झांसी:</em> ऐतिहासिक झांसी किला (1613 में राजा बीर सिंह देव द्वारा निर्मित), रानी महल (भित्ति चित्र), राजकीय संग्रहालय।
          <br>&bull; <em>कालिंजर किला (बांदा):</em> विंध्य पर्वतमाला पर स्थित अजेय दुर्ग; नीलकंठ महादेव मंदिर, 1545 में शेरशाह सूरी की मृत्यु का स्थल।
          <br>&bull; <em>देवगढ़ (ललितपुर):</em> गुप्तकालीन दशावतार मंदिर (शिखर युक्त एवं पंचायतन शैली का भारत का सबसे प्राचीन मंदिर); किले में 31 जैन मंदिर।
          <br>&bull; <em>महोबा:</em> चंदेलों की राजधानी, राहिला सूर्य मंदिर, विजय सागर झील, आल्हा-ऊदल के स्मारक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Sufi Circuit (सूफी सर्किट):</strong>
          <br>&bull; <em>Fatehpur Sikri (Agra):</em> Dargah of Sufi Saint <strong>Sheikh Salim Chishti</strong> (built in pure white marble by Akbar).
          <br>&bull; <em>Dewa Sharif (Barabanki):</em> Shrine of <strong>Haji Waris Ali Shah</strong>, venue of the world-famous annual Dewa Mela celebrating universal brotherhood ("Jo Rab Hai Wahi Ram Hai").
          <br>&bull; <em>Dargah Syed Salar Masud Ghazi (Bahraich):</em> Historic shrine attracting millions during Jyeshtha fair.
          <br>&bull; <em>Kichhauchha Sharif (Ambedkar Nagar):</em> Dargah of Makhdoom Ashraf Jahangir Semnani.
          <br>&bull; <em>Khanqah-e-Karamia (Salon, Rae Bareli) &amp; Shafi Lakhi Dargah.</em></span>
        <span class="lang-hi"><strong>सूफी सर्किट:</strong>
          <br>&bull; <em>फतेहपुर सीकरी (आगरा):</em> सूफी संत <strong>शेख सलीम चिश्ती</strong> की संगमरमरी दरगाह (अकबर द्वारा निर्मित)।
          <br>&bull; <em>देवा शरीफ (बाराबंकी):</em> <strong>हाजी वारिस अली शाह</strong> की मजार, जहां प्रतिवर्ष विश्वप्रसिद्ध देवा मेला लगता है ("जो रब है वही राम है" का संदेश)।
          <br>&bull; <em>सैयद सालार मसूद गाजी दरगाह (बहराइच):</em> ऐतिहासिक मजार जहां ज्येष्ठ मास में विशाल मेला लगता है।
          <br>&bull; <em>किछौछा शरीफ (अंबेडकर नगर):</em> मखदूम अशरफ जहांगीर समनानी की दरगाह।
          <br>&bull; <em>खानकाह-ए-करमिया (सलोन, रायबरेली)।</em></span>
      </li>
      <li>
        <span class="lang-en"><strong>Jain Circuit (जैन सर्किट):</strong>
          <br>&bull; <em>Ayodhya:</em> Holiest Jain pilgrimage as the <strong>birthplace of 5 Tirthankaras</strong>: Rishabhdev (Adinath - 1st), Ajitnath (2nd), Abhinandannath (4th), Sumatinath (5th), and Anantnath (14th).
          <br>&bull; <em>Kashi (Varanasi):</em> Birthplace of <strong>Suparshvanath (7th)</strong> and <strong>Parshvanath (23rd Tirthankara)</strong>.
          <br>&bull; <em>Kaushambi:</em> Birthplace of <strong>Padmaprabhu (6th Tirthankara)</strong> (Prabhas Giri).
          <br>&bull; <em>Shravasti:</em> Birthplace of <strong>Sambhavnath (3rd Tirthankara)</strong>.
          <br>&bull; <em>Deogarh &amp; Hastinapur:</em> Shantinath (16th), Kunthunath (17th), and Aranatha (18th) associated with Hastinapur (Meerut).</span>
        <span class="lang-hi"><strong>जैन सर्किट:</strong>
          <br>&bull; <em>अयोध्या:</em> <strong>5 तीर्थंकरों की जन्मभूमि</strong> होने के कारण परम पावन जैन तीर्थ: ऋषभदेव (आदिनाथ - प्रथम), अजितनाथ (द्वितीय), अभिनंदननाथ (चतुर्थ), सुमतिनाथ (पंचम) एवं अनंतनाथ (14वें)।
          <br>&bull; <em>काशी (वाराणसी):</em> <strong>सुपार्श्वनाथ (7वें)</strong> एवं <strong>पार्श्वनाथ (23वें तीर्थंकर)</strong> की जन्मस्थली।
          <br>&bull; <em>कौशाम्बी:</em> <strong>पद्मप्रभु (6वें तीर्थंकर)</strong> की जन्मस्थली (प्रभास गिरि)।
          <br>&bull; <em>श्रावस्ती:</em> <strong>संभवनाथ (तीसरे तीर्थंकर)</strong> की जन्मस्थली (शोभनाथ मंदिर)।
          <br>&bull; <em>हस्तिनापुर (मेरठ):</em> शांतिनाथ (16वें), कुंथुनाथ (17वें) एवं अरनाथ (18वें) तीर्थंकरों से संबंधित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Eco-Tourism &amp; Wildlife Circuit (ईको-पर्यटन सर्किट):</strong>
          <br>&bull; Dudhwa National Park (Lakhimpur Kheri) &amp; Kishanpur Sanctuary (tiger, rhino, swamp deer).
          <br>&bull; Pilibhit Tiger Reserve (TX2 award for doubling tigers).
          <br>&bull; Katarniaghat Wildlife Sanctuary (Bahraich - Gangetic dolphins, gharials).
          <br>&bull; National Chambal Sanctuary (Etawah/Agra - gharials and skimmers).
          <br>&bull; Chandraprabha Wildlife Sanctuary &amp; Rajdari-Devdari Waterfalls (Chandauli).</span>
        <span class="lang-hi"><strong>ईको-पर्यटन एवं वन्यजीव परिपथ:</strong>
          <br>&bull; दुधवा राष्ट्रीय उद्यान (लखीमपुर खीरी) एवं किशनपुर (बाघ, गैंडा, बारहसिंगा)।
          <br>&bull; पीलीभीत टाइगर रिजर्व (बाघों की संख्या दोगुनी करने हेतु वैश्विक TX2 पुरस्कार)।
          <br>&bull; कतर्नियाघाट वन्यजीव अभयारण्य (बहराइच - गंगा डॉल्फिन, घड़ियाल)।
          <br>&bull; राष्ट्रीय चंबल अभयारण्य (इटावा/आगरा - घड़ियाल एवं प्रवासी पक्षी)।
          <br>&bull; चंद्रप्रभा वन्यजीव अभयारण्य तथा राजदारी-देवदारी जलप्रपात (चंदौली)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: UNESCO World Heritage Sites of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. UNESCO World Heritage Sites &amp; Intangible Cultural Heritage of UP</span>
    <span class="lang-hi">6. उत्तर प्रदेश के यूनेस्को विश्व धरोहर स्थल एवं अमूर्त सांस्कृतिक धरोहर</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Three Tangible UNESCO World Heritage Sites (तीन मूर्त यूनेस्को स्थल):</strong>
          <br>1. <strong>Taj Mahal (Agra):</strong> Inscribed in <strong>1983</strong>; built between 1631-1648 by Mughal Emperor Shah Jahan for Mumtaz Mahal; Chief Architect was Ustad Ahmad Lahauri; masterpiece of white Makrana marble and Pietra Dura inlay.
          <br>2. <strong>Agra Fort (Agra):</strong> Inscribed in <strong>1983</strong>; red sandstone fortress constructed under Akbar (1565-1573); houses Jahangiri Mahal, Diwan-e-Aam, Diwan-e-Khas, Khas Mahal, Sheesh Mahal, and Musamman Burj.
          <br>3. <strong>Fatehpur Sikri (Agra):</strong> Inscribed in <strong>1986</strong>; royal capital built by Akbar (1571-1585); features <strong>Buland Darwaza (1601 - 54 meters tall, highest gateway in the world)</strong>, Jama Masjid, Salim Chishti Tomb, Panch Mahal, and Ibadat Khana.</span>
        <span class="lang-hi"><strong>तीन मूर्त यूनेस्को विश्व धरोहर स्थल:</strong>
          <br>1. <strong>ताजमहल (आगरा):</strong> <strong>1983</strong> में inscribed; 1631-1648 के मध्य शाहजहां द्वारा मुमताज महल की स्मृति में निर्मित; मुख्य वास्तुकार उस्ताद अहमद लाहौरी; सफेद मकराना संगमरमर एवं पच्चीकारी (पिएट्रा ड्यूरा) का उत्कृष्ट नमूना।
          <br>2. <strong>आगरा का किला:</strong> <strong>1983</strong> में inscribed; अकबर द्वारा 1565-1573 में निर्मित लाल बलुआ पत्थर का दुर्ग; जहांगीरी महल, दीवान-ए-आम, दीवान-ए-खास, शीश महल एवं मुसम्मन बुर्ज इसमें स्थित हैं।
          <br>3. <strong>फतेहपुर सीकरी:</strong> <strong>1986</strong> में inscribed; अकबर द्वारा 1571-1585 के मध्य बसाई गई राजधानी; <strong>बुलंद दरवाजा (1601 - 54 मीटर ऊंचा, विश्व का सबसे ऊंचा प्रवेश द्वार)</strong>, जामा मस्जिद, सलीम चिश्ती दरगाह, पंचमहल व इबादतखाना।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Three Intangible Cultural Heritage (ICH) Elements (तीन अमूर्त यूनेस्को धरोहरें):</strong>
          <br>1. <strong>Ramlila (रामलीला):</strong> Inscribed in <strong>2008</strong>; traditional folk enactment of Ramayana across Ramnagar (Varanasi), Ayodhya, and Chitrakoot.
          <br>2. <strong>Tradition of Vedic Chanting (वैदिक मंत्रोच्चार):</strong> Inscribed in <strong>2008</strong>; preserved meticulously by the traditional Vedic scholars of Kashi (Varanasi).
          <br>3. <strong>Kumbh Mela (कुंभ मेला, प्रयागराज):</strong> Inscribed in <strong>2017</strong>; recognized as the world's largest peaceful congregation of pilgrims on Earth at the Triveni Sangam.</span>
        <span class="lang-hi"><strong>तीन अमूर्त यूनेस्को सांस्कृतिक धरोहरें (ICH):</strong>
          <br>1. <strong>रामलीला:</strong> <strong>2008</strong> में अमूर्त धरोहर सूची में सम्मिलित; रामनगर (वाराणसी), अयोध्या एवं चित्रकूट की ऐतिहासिक रामलीला परंपरा।
          <br>2. <strong>वैदिक मंत्रोच्चार की परंपरा:</strong> <strong>2008</strong> में सम्मिलित; काशी के वैदिक विद्वानों द्वारा सहेजी गई मौखिक वेद पाठ की प्राचीन परंपरा।
          <br>3. <strong>कुंभ मेला (प्रयागराज):</strong> <strong>2017</strong> में सम्मिलित; त्रिवेणी संगम पर जुटने वाला मानवता का सबसे बड़ा शांतिपूर्ण जन-समागम।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master Comparison Table of Tourism Circuits -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Comparison Table: Tourism Circuits of Uttar Pradesh</span>
    <span class="lang-hi">7. उत्तर प्रदेश के पर्यटन परिपथों की महा-तुलना तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Circuit Name</span>
            <span class="lang-hi">परिपथ का नाम</span>
          </th>
          <th>
            <span class="lang-en">Primary Destinations / Nodes</span>
            <span class="lang-hi">प्रमुख गंतव्य / नोड्स</span>
          </th>
          <th>
            <span class="lang-en">Thematic Core &amp; Architectural Focus</span>
            <span class="lang-hi">विषय वस्तु एवं स्थापत्य महत्व</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Heritage Arc</span>
            <span class="lang-hi">हेरिटेज आर्क</span>
          </td>
          <td>
            <span class="lang-en">Agra - Lucknow - Varanasi</span>
            <span class="lang-hi">आगरा - लखनऊ - वाराणसी</span>
          </td>
          <td>
            <span class="lang-en">Golden triangle connecting Mughal grandeur, Nawabi sophistication, and ancient spiritual Varanasi</span>
            <span class="lang-hi">मुगल स्थापत्य, नवाबी नजाकत एवं प्राचीन काशी के संगम का स्वर्णिम त्रिकोण</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Ramayana Circuit</span>
            <span class="lang-hi">रामायण सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Ayodhya, Chitrakoot, Shringverpur, Bithoor</span>
            <span class="lang-hi">अयोध्या, चित्रकूट, श्रृंगवेरपुर, बिठूर</span>
          </td>
          <td>
            <span class="lang-en">Life journey of Lord Rama: Birthplace, exile hermitage, boat crossing, and Valmiki Ashram</span>
            <span class="lang-hi">श्रीराम का जीवन चरित: जन्मस्थली, वनवास स्थली, केवट मिलन एवं वाल्मीकि आश्रम</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Krishna Circuit</span>
            <span class="lang-hi">कृष्ण सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Mathura, Vrindavan, Barsana, Govardhan, Gokul, Nandgaon</span>
            <span class="lang-hi">मथुरा, वृंदावन, बरसाना, गोवर्धन, गोकुल, नंदगांव</span>
          </td>
          <td>
            <span class="lang-en">Leelas of Lord Krishna and Radha Rani; 84 Kos Parikrama; Lathmar Holi</span>
            <span class="lang-hi">श्रीकृष्ण एवं श्री राधा रानी की लीला भूमियां; 84 कोस परिक्रमा; लठमार होली</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Buddhist Circuit</span>
            <span class="lang-hi">बौद्ध सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Sarnath, Kushinagar, Shravasti, Kapilvastu, Sankisa, Kaushambi</span>
            <span class="lang-hi">सारनाथ, कुशीनगर, श्रावस्ती, कपिलवस्तु, संकिसा, कौशाम्बी</span>
          </td>
          <td>
            <span class="lang-en">First Sermon (Sarnath), Mahaparinirvana (Kushinagar), 24 Vassavasas (Shravasti)</span>
            <span class="lang-hi">प्रथम उपदेश (सारनाथ), महापरिनिर्वाण (कुशीनगर), 24 वर्षावास (श्रावस्ती)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Bundelkhand Circuit</span>
            <span class="lang-hi">बुंदेलखंड सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Jhansi, Kalinjar (Banda), Deogarh (Lalitpur), Mahoba</span>
            <span class="lang-hi">झांसी, कालिंजर (बांदा), देवगढ़ (ललितपुर), महोबा</span>
          </td>
          <td>
            <span class="lang-en">Chivalric hill forts, Gupta Dashavatara temple, Chandela lakes, and Rani Lakshmibai heritage</span>
            <span class="lang-hi">वीर गाथाओं के दुर्ग, गुप्तकालीन दशावतार मंदिर, चंदेल झीलें व रानी लक्ष्मीबाई स्मृति</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Sufi Circuit</span>
            <span class="lang-hi">सूफी सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Fatehpur Sikri, Dewa Sharif (Barabanki), Bahraich, Kichhauchha</span>
            <span class="lang-hi">फतेहपुर सीकरी, देवा शरीफ (बाराबंकी), बहराइच, किछौछा</span>
          </td>
          <td>
            <span class="lang-en">Shrines of Salim Chishti, Waris Ali Shah, Salar Masud; Ganga-Jamuni composite mysticism</span>
            <span class="lang-hi">सलीम चिश्ती, वारिस अली शाह, सालार मसूद की दरगाहें; साझी गंगा-जमुनी सूफी परंपरा</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Jain Circuit</span>
            <span class="lang-hi">जैन सर्किट</span>
          </td>
          <td>
            <span class="lang-en">Ayodhya (5 Tirthankaras), Kashi, Kaushambi, Shravasti, Deogarh, Hastinapur</span>
            <span class="lang-hi">अयोध्या (5 तीर्थंकर), काशी, कौशाम्बी, श्रावस्ती, देवगढ़, हस्तिनापुर</span>
          </td>
          <td>
            <span class="lang-en">Birthplaces and penance sites of 24 Jain Tirthankaras</span>
            <span class="lang-hi">जैन तीर्थंकरों की जन्म एवं तपस्या भूमियां</span>
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
            <span class="lang-en">Exam Question / Trap</span>
            <span class="lang-hi">परीक्षा प्रश्न / ट्रैप</span>
          </th>
          <th>
            <span class="lang-en">Precision Answer &amp; Strategic Fact</span>
            <span class="lang-hi">सटीक उत्तर एवं महत्वपूर्ण तथ्य</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">UP Rank in Domestic Tourists</span>
            <span class="lang-hi">घरेलू पर्यटकों में यूपी का स्थान</span>
          </td>
          <td>
            <span class="lang-en"><strong>Rank 1 in India</strong> (>32 crore domestic tourists annually).</span>
            <span class="lang-hi"><strong>भारत में प्रथम स्थान</strong> (वार्षिक 32 करोड़ से अधिक घरेलू पर्यटक)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Tirthankaras Born in Ayodhya</span>
            <span class="lang-hi">अयोध्या में जन्मे तीर्थंकर</span>
          </td>
          <td>
            <span class="lang-en"><strong>5 Tirthankaras</strong>: Rishabhdev, Ajitnath, Abhinandannath, Sumatinath, and Anantnath.</span>
            <span class="lang-hi"><strong>5 तीर्थंकर</strong>: ऋषभदेव, अजितनाथ, अभिनंदननाथ, सुमतिनाथ एवं अनंतनाथ।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Earliest Temple with Shikhara</span>
            <span class="lang-hi">शिखर युक्त सबसे प्राचीन मंदिर</span>
          </td>
          <td>
            <span class="lang-en"><strong>Dashavatara Temple, Deogarh (Lalitpur)</strong>; Gupta period; Panchayatana style.</span>
            <span class="lang-hi"><strong>दशावतार मंदिर, देवगढ़ (ललितपुर)</strong>; गुप्तकालीन; पंचायतन शैली।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Buddha Preached Maximum Sermons at</span>
            <span class="lang-hi">बुद्ध ने सर्वाधिक उपदेश कहां दिए</span>
          </td>
          <td>
            <span class="lang-en"><strong>Shravasti (Jetavana Monastery)</strong>; spent 24 monsoon retreats (Vassavasas).</span>
            <span class="lang-hi"><strong>श्रावस्ती (जेतवन विहार)</strong>; सर्वाधिक 24 वर्षावास बिताए।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Kumbh Mela UNESCO Year</span>
            <span class="lang-hi">कुंभ मेला यूनेस्को अमूर्त धरोहर वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>2017</strong> (Ramlila &amp; Vedic Chanting were inscribed in <strong>2008</strong>).</span>
            <span class="lang-hi"><strong>2017</strong> (रामलीला एवं वैदिक मंत्रोच्चार <strong>2008</strong> में शामिल किए गए)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Tribe Observing Mourning on Diwali</span>
            <span class="lang-hi">दीपावली को शोक पर्व के रूप में मनाने वाली जनजाति</span>
          </td>
          <td>
            <span class="lang-en"><strong>Tharu Tribe</strong> (perform ancestor remembrance ritual).</span>
            <span class="lang-hi"><strong>थारू जनजाति</strong> (पूर्वज स्मरण / भेंट पूजा)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">UPSTDC Establishment Year</span>
            <span class="lang-hi">UPSTDC स्थापना वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>1974</strong> (Uttar Pradesh State Tourism Development Corporation).</span>
            <span class="lang-hi"><strong>1974</strong> (उत्तर प्रदेश राज्य पर्यटन विकास निगम)।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "social-customs-and-tourism", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_social_customs_tourism_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
