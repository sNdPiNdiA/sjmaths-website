import os
import re

def build_folk_dances_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Classical &amp; Regional Folk Dances of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के शास्त्रीय एवं क्षेत्रीय लोक नृत्य</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Folk & Classical Dances of UP] --> B[Classical: Kathak]
    A --> C[Braj Region Dances]
    A --> D[Bundelkhand Region Dances]
    A --> E[Purvanchal Region Dances]
    A --> F[Awadh Region Dances]
    A --> G[Tribal Belt: Sonbhadra & Mirzapur]

    B --> B1[Only Classical Dance of North India]
    B --> B2[Lucknow Gharana: Wajid Ali Shah & Birju Maharaj]
    B --> B3[Banaras Gharana: Natwari Bols & Sitara Devi]

    C --> C1[Charkula: 108 Lamps Pyramid on Head]
    C --> C2[Raas & Mayur Nritya: Peacock Feathers]
    C --> C3[Ghada & Jhula Nritya]

    D --> D1[Rai Dance: Ahir Women Janmashtami Peacock]
    D --> D2[Pai-Danda & Diwari: Stick Dance like Dandiya]
    D --> D3[Shaira / Saura: Harvest Sticks Dance]
    D --> D4[Khyal: Son Birth | Dhuriya: Kumhar Women Attire]

    E --> E1[Dhobiya: Dhobi Community Donkey Acrobatics]
    E --> E2[Natwari: Ahir Community Physical Feats]
    E --> E3[Chaurasiya: Kahar Community of Jaunpur]
    E --> E4[Kathghorwa: Wooden Dummy Horse]

    F --> F1[Jogini: Ram Navami Cross-Dressing Men]
    F --> F2[Kala Bazi: Kachhi Ghodi Acrobatic Stunts]

    G --> G1[Karma: Kharwar & Baiga Tree Worship]
    G --> G2[Thadiya: Childbirth Blessing | Shila Dance]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उ.प्र. के शास्त्रीय एवं लोक नृत्य] --> B[शास्त्रीय नृत्य: कथक]
    A --> C[ब्रज क्षेत्र के लोक नृत्य]
    A --> D[बुंदेलखंड के लोक नृत्य]
    A --> E[पूर्वांचल के लोक नृत्य]
    A --> F[अवध क्षेत्र के लोक नृत्य]
    A --> G[जनजातीय नृत्य: सोनभद्र व मिर्जापुर]

    B --> B1[उत्तर भारत का एकमात्र शास्त्रीय नृत्य]
    B --> B2[लखनऊ घराना: वाजिद अली शाह व बिरजू महाराज]
    B --> B3[बनारस घराना: नटवरी बोल व सितारा देवी]

    C --> C1[चरकुला: सिर पर 108 दीपकों का पिरामिड]
    C --> C2[रास एवं मयूर नृत्य: मोर पंख परिधान]
    C --> C3[घड़ा एवं झूला नृत्य]

    D --> D1[राई नृत्य: अहीर महिलाएं मयूर चाल]
    D --> D2[पाई-डंडा एवं दीवारी: डांडिया समतुल्य लाठी नृत्य]
    D --> D3[शहरा / सौरा: फसल कटाई पर डंडा नृत्य]
    D --> D4[ख्याल: पुत्र जन्मोत्सव | धुरिया: कुम्हार स्त्री वेश]

    E --> E1[धोबिया: धोबी समुदाय व गधे का स्वांग]
    E --> E2[नटवारी: अहीर समुदाय के शारीरिक करतब]
    E --> E3[चौरसिया: जौनपुर का कहार समुदाय]
    E --> E4[काठघोड़वा: लकड़ी का कृत्रिम घोड़ा]

    F --> F1[जोगिनी: रामनवमी पर स्त्री वेश में पुरुष]
    F --> F2[कलाबाजी: कच्ची घोड़ी व करतब]

    G --> G1[कर्मा: खरवार व बैगा करम वृक्ष पूजा]
    G --> G2[ठड़िया: संतान कामना | शीला नृत्य]
    </div>
  </div>
</div>

<!-- Card 2: Classical Kathak Heritage -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Classical Kathak: Origins, Anatomy &amp; Gharanas</span>
    <span class="lang-hi">1. शास्त्रीय कथक: उत्पत्ति, व्याकरण एवं प्रमुख घराने</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Sole Classical Dance of North India:</strong> Kathak is the only classical dance form originating from North India, having its foundational roots in the ancient temple storytellers ('Kathakars') of the Indo-Gangetic plains.</span>
      <span class="lang-hi"><strong>उत्तर भारत का एकमात्र शास्त्रीय नृत्य:</strong> कथक उत्तर भारत से उत्पन्न होने वाला एकमात्र शास्त्रीय नृत्य है, जिसकी जड़ें गंगा के मैदानों के प्राचीन मंदिर कथाकारों ('कथा कहे सो कथक कहावे') में हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Eight Key Structural Components:</strong>
        <br/>1. <strong>Vandana (वंदना):</strong> Devotional invocation to Lord Ganesha or Saraswati.
        <br/>2. <strong>Amad (आमाद):</strong> Formal entry onto the stage with rhythmic bols.
        <br/>3. <strong>Thaat (ठाठ):</strong> Elegant, poised posture with subtle eyebrow and neck movements.
        <br/>4. <strong>Tukra / Toda (टुकड़ा/तोड़ा):</strong> Crisp compositions set to complex rhythmic beats.
        <br/>5. <strong>Parhant (पढ़ंत):</strong> Vocal recitation of rhythmic syllables with hand claps before execution.
        <br/>6. <strong>Tatkar (तत्कार):</strong> Intricate, rapid footwork synchronized with ankle-bell sounds (Ghungroos).
        <br/>7. <strong>Chakradar (चक्करदार):</strong> Rapid pirouettes/spins ending precisely on the 'Sam' (first beat).
        <br/>8. <strong>Bhav (भाव / अभिनय):</strong> Subtle, emotive expression of devotional or romantic poetry (Thumri/Dadra).
      </span>
      <span class="lang-hi"><strong>कथक के 8 प्रमुख संरचनात्मक अंग:</strong>
        <br/>1. <strong>वंदना:</strong> गणेश या सरस्वती की मंगलाचरण स्तुति।
        <br/>2. <strong>आमाद:</strong> बोलों के साथ मंच पर नर्तक का औपचारिक प्रवेश।
        <br/>3. <strong>ठाठ:</strong> ग्रेसफुल मुद्रा जिसमें भौंहों व ग्रीवा का सूक्ष्म संचालन होता है।
        <br/>4. <strong>टुकड़ा / तोड़ा:</strong> निश्चित ताल में बद्ध लघु व तीव्र नृत्य रचना।
        <br/>5. <strong>पढ़ंत:</strong> ताल के बोलों को हाथ की ताली पर बोलकर प्रस्तुत करना।
        <br/>6. <strong>तत्कार:</strong> घुंघरुओं की झंकार के साथ पैरों का द्रुत व लयबद्ध संचालन (पद-ताल)।
        <br/>7. <strong>चक्करदार:</strong> तीव्र गति से चक्कर लेकर सटीक 'सम' पर रुकना।
        <br/>8. <strong>भाव / अभिनय:</strong> ठुमरी या दादरा के पदों पर सूक्ष्म आंगिक व सात्विक भावाभिव्यक्ति।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Lucknow Kathak Gharana:</strong>
        <br/>• Founded under the royal patronage of Awadh's last Nawab, <strong>Wajid Ali Shah</strong> (who performed in <em>Rahas</em> under the pen-name <strong>Akhtar Piya</strong>).
        <br/>• Initiated by <strong>Thakur Prasad</strong>; flourished through Maharaj brothers <strong>Kalka Prasad and Bindadin Maharaj</strong>.
        <br/>• Elevated globally by <strong>Pandit Birju Maharaj</strong>, Lachhu Maharaj, and Shambhu Maharaj. Celebrated for grace, Nazakat, and delicate Thumri abhinaya.
      </span>
      <span class="lang-hi"><strong>लखनऊ कथक घराना:</strong>
        <br/>• अवध के अंतिम नवाब <strong>वाजिद अली शाह</strong> ('अख्तर पिया') के संरक्षण में विकसित।
        <br/>• प्रवर्तक: <strong>ठाकुर प्रसाद</strong>; कालका प्रसाद व बिंदादीन महाराज ने इसे समृद्ध किया।
        <br/>• विश्व स्तर पर प्रतिष्ठित: <strong>पंडित बिरजू महाराज</strong>, लच्छू महाराज व शंभू महाराज। नजाकत, नफासत व ठुमरी पर भाव प्रदर्शन हेतु विख्यात।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Banaras Kathak Gharana:</strong>
        <br/>• Founded by <strong>Janaki Prasad</strong>; distinguished by pure <strong>Natwari Bols</strong> (syllables of Krishna's dance on Kaliya serpent) rather than Pakhawaj/Tabla bols.
        <br/>• Renowned exponent: <strong>Sitara Devi</strong> (lauded by Rabindranath Tagore as the <em>Nritya Samragni / Queen of Dance</em>).
      </span>
      <span class="lang-hi"><strong>बनारस कथक घराना:</strong>
        <br/>• संस्थापक: <strong>जानकी प्रसाद</strong>; पखावज के स्थान पर शुद्ध <strong>नटवरी बोलों</strong> (कालिया नाग पर कृष्ण के नृत्य के बोल) हेतु प्रसिद्ध।
        <br/>• शीर्ष नृत्यांगना: <strong>सितारा देवी</strong> (जिन्हें रवींद्रनाथ टैगोर ने <em>'नृत्य साम्राज्ञी'</em> की उपाधि दी थी)।
      </span>
    </li>
  </ul>
</div>

<!-- Card 3: Braj Region Folk Dances -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Folk Dances of the Braj Region (Mathura-Vrindavan)</span>
    <span class="lang-hi">2. ब्रज क्षेत्र (मथुरा-वृंदावन) के प्रसिद्ध लोक नृत्य</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Charkula Dance (चरकुला नृत्य):</strong>
        <br/>• Most famous folk dance of Braj, performed on <strong>Radhashtami (and the 3rd day after Holi)</strong> to celebrate Radha's birth.
        <br/>• Female dancers balance a multi-tiered wooden pyramid/wheel (called <em>Charkula</em>) containing <strong>108 illuminated oil lamps</strong> on their veiled heads, dancing gracefully to the beats of <em>Hurduk</em> and <em>Rasiya</em>.
      </span>
      <span class="lang-hi"><strong>चरकुला नृत्य:</strong>
        <br/>• ब्रज का सर्वाधिक प्रसिद्ध लोक नृत्य, जो <strong>राधाष्टमी (तथा होली के तीसरे दिन)</strong> पर राधा जी के जन्म के उल्लास में किया जाता है।
        <br/>• महिलाएं घूंघट काढ़े अपने सिर पर <strong>108 जलते हुए दीपकों वाला 4-5 मंजिला लकड़ी का पिरामिड (चरकुला)</strong> संतुलित कर <em>हुरदुक</em> व <em>रसिया</em> की धुन पर नृत्य करती हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Mayur Dance (मयूर नृत्य):</strong> Dancers don garments adorned with peacock feathers, reenacting the lore where Lord Krishna danced as a peacock in the groves of Barsana to enchant Radha.</span>
      <span class="lang-hi"><strong>मयूर नृत्य:</strong> नर्तक मोर पंखों से बने वस्त्र धारण कर मोर का रूप धरते हैं; भगवान कृष्ण द्वारा बरसाना में राधा को रिझाने हेतु मोर बनकर नृत्य करने की लीला का मंचन।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Raas Nritya (रास नृत्य):</strong> The devotional group circle-dance performed during Raslila, recreating the Maharaas of Krishna and the Gopis on Sharad Purnima in Vrindavan.</span>
      <span class="lang-hi"><strong>रास नृत्य:</strong> रासलीला के अवसर पर किया जाने वाला भक्ति नृत्य; शरद पूर्णिमा पर वृंदावन में भगवान कृष्ण और गोपियों के महारास का अभिनय।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Ghada Dance (घड़ा नृत्य):</strong> Women balance multiple earthen pots (Ghada) stacked vertically on their heads with a burning lamp on the topmost pot while executing circular foot movements.</span>
      <span class="lang-hi"><strong>घड़ा नृत्य:</strong> सिर पर एक के ऊपर एक कई मिट्टी के घड़े रखकर तथा सबसे ऊपर दीपक जलाकर रथ के पहिए पर संतुलित होकर किया जाने वाला नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Jhula Dance (झूला नृत्य):</strong> Performed during the monsoon month of Shravan in the temples of Mathura, Vrindavan, and Gokul accompanying devotional swings.</span>
      <span class="lang-hi"><strong>झूला नृत्य:</strong> सावन माह में ब्रज के मंदिरों में भगवान के हिंडोले (झूला) के समक्ष भक्ति पदों के साथ किया जाने वाला उल्लास नृत्य।</span>
    </li>
  </ul>
</div>

<!-- Card 4: Bundelkhand Region Folk Dances -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Folk Dances of Bundelkhand (Martial &amp; Agrarian)</span>
    <span class="lang-hi">3. बुंदेलखंड क्षेत्र के लोक नृत्य (शौर्य एवं कृषि आधारित)</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Rai Dance (राई नृत्य):</strong>
        <br/>• Performed by women (traditional Bedni dancers) during Janmashtami, festivals, and weddings across Bundelkhand.
        <br/>• Also known as the <strong>Peacock Dance of Bundelkhand (मयूर चाल)</strong> because the dancer mimics the swirling movements of a courting peacock to the fast beats of the <em>Mridang</em>.
      </span>
      <span class="lang-hi"><strong>राई नृत्य:</strong>
        <br/>• बुंदेलखंड में जन्माष्टमी, शुभ अवसरों व विवाह पर महिलाओं (पारंपरिक बेड़नी) द्वारा किया जाने वाला प्रमुख नृत्य।
        <br/>• इसे <strong>बुंदेलखंड का मयूर नृत्य</strong> भी कहते हैं क्योंकि नर्तकी मृदंग की तीव्र थाप पर मोर की भांति द्रुत गति से चक्कर लेती है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Pai-Danda &amp; Diwari Dance (पाई-डंडा एवं दीवारी नृत्य):</strong>
        <br/>• Performed by the <strong>Ahir / Yadav community</strong> of Bundelkhand during Diwali.
        <br/>• Known as the <strong>Dandiya of Bundelkhand / UP</strong>; men carry small polished lathis (sticks) and strike them rhythmically in circles, showcasing martial defense skills.
      </span>
      <span class="lang-hi"><strong>पाई-डंडा एवं दीवारी नृत्य:</strong>
        <br/>• बुंदेलखंड के <strong>अहीर/यादव समुदाय</strong> द्वारा दीपावली के अवसर पर किया जाने वाला नृत्य।
        <br/>• इसे <strong>बुंदेलखंड का डांडिया</strong> कहा जाता है; पुरुष लाठियों को आपस में टकराते हुए वीरतापूर्ण युद्ध कौशल का प्रदर्शन करते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Shaira / Saura / Suwa Dance (शैरा / सौरा नृत्य):</strong> Performed by young boys and girls during harvest season (Bhadrapada) carrying green corn stalks; invokes rain gods and celebrates agricultural bounty using sticks.</span>
      <span class="lang-hi"><strong>शैरा / सौरा नृत्य:</strong> भाद्रपद में फसल कटाई के उल्लास में युवा लड़के-लड़कियों द्वारा हाथों में ज्वार की हरी बालियां व डंडे लेकर वर्षा देव इंद्र की स्तुति में किया जाने वाला नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Khyal Dance (ख्याल नृत्य):</strong> Performed exclusively on the <strong>birth of a male child (पुत्र जन्मोत्सव)</strong>; dancers balance a multi-colored paper and bamboo temple structure (Khyal) on their heads.</span>
      <span class="lang-hi"><strong>ख्याल नृत्य:</strong> <strong>पुत्र रत्न की प्राप्ति</strong> के अवसर पर किया जाता है; रंगीन कागजों व बांस की खपच्चियों से बने मंदिर (ख्याल) को सिर पर रखकर नृत्य किया जाता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Dhuriya Dance (धुरिया नृत्य):</strong> Performed by the <strong>Prajapati (Kumhar / Potter) community</strong> of Bundelkhand, where male dancers dress entirely in female attire to invoke ancestral spirits.</span>
      <span class="lang-hi"><strong>धुरिया नृत्य:</strong> बुंदेलखंड के <strong>कुम्हार (प्रजापति) समुदाय</strong> के पुरुषों द्वारा स्त्री वेश धारण करके किया जाने वाला पारंपरिक अनुष्ठानिक नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Ghodi Dance (घोड़ी नृत्य):</strong> A dummy horse dance performed during marriage processions (Barat) to the accompaniment of Shehnai and Nagara.</span>
      <span class="lang-hi"><strong>घोड़ी नृत्य:</strong> बुंदेलखंड में विवाह बारात के समय नर्तक द्वारा नकली लकड़ी की घोड़ी में बैठकर बाजों की धुन पर किया जाने वाला नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kartik Dance (कार्तिक नृत्य):</strong> Performed throughout the month of Kartik; dancers portray Radha-Krishna and Gopis to the beats of earthen pots.</span>
      <span class="lang-hi"><strong>कार्तिक नृत्य:</strong> कार्तिक माह में गोपी-कृष्ण बनकर बुंदेलखंड के ग्रामीणों द्वारा किया जाने वाला भक्ति नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kaanra Dance (कानरा नृत्य):</strong> Performed by the Dhobi community of Bundelkhand during weddings, singing devotional songs with Sarangi.</span>
      <span class="lang-hi"><strong>कानरा नृत्य:</strong> बुंदेलखंड के धोबी समाज द्वारा विवाह उत्सव पर सारंगी व ढोलक की धुन पर किया जाने वाला नृत्य।</span>
    </li>
  </ul>
</div>

<!-- Card 5: Purvanchal & Awadh Folk Dances -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Folk Dances of Purvanchal (Eastern UP) &amp; Awadh</span>
    <span class="lang-hi">4. पूर्वांचल एवं अवध क्षेत्र के विशिष्ट लोक नृत्य</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Dhobiya Dance (धोबिया नृत्य, Purvanchal):</strong>
        <br/>• Performed exclusively by the <strong>Dhobi (washermen) community</strong> during marriages, child-naming, and festive celebrations.
        <br/>• Enacts the humorous, affectionate relationship between the washerman and his loyal donkey (one dancer plays the donkey with a dummy skin/costume).
      </span>
      <span class="lang-hi"><strong>धोबिया नृत्य (पूर्वांचल):</strong>
        <br/>• पूर्वांचल के <strong>धोबी समुदाय</strong> द्वारा मांगलिक अवसरों (विवाह व जन्मोत्सव) पर किया जाने वाला सर्वाधिक लोकप्रिय लोक नृत्य।
        <br/>• इसमें एक नर्तक गधा बनता है और दूसरा धोबी; दोनों के बीच परस्पर आत्मीय एवं हास्य संवाद व तीव्र शारीरिक उछल-कूद होती है।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Natwari Dance (नटवारी नृत्य, Purvanchal):</strong>
        <br/>• Performed by the <strong>Ahir / Yadav community</strong> on Janmashtami and Holi.
        <br/>• Dedicated to Lord Krishna as <em>Natwar</em> (the divine dancer); dancers execute rhythmic martial jumps, acrobatics, and wrestling maneuvers to the beats of Nakkaara and Dholak.
      </span>
      <span class="lang-hi"><strong>नटवारी नृत्य (पूर्वांचल):</strong>
        <br/>• पूर्वांचल के <strong>अहीर समुदाय</strong> द्वारा जन्माष्टमी व होली पर किया जाने वाला ओजस्वी नृत्य।
        <br/>• भगवान कृष्ण के 'नटवर' स्वरूप को समर्पित; इसमें नगाड़े व ढोलक की ताल पर कुश्ती के पैंतरे, ऊंची छलांगें व शारीरिक करतब दिखाए जाते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Chaurasiya Dance (चौरसिया नृत्य, Purvanchal):</strong> Performed exclusively by the <strong>Kahar (water-carrier/palanquin) community of Jaunpur</strong> district during celebratory feasts.</span>
      <span class="lang-hi"><strong>चौरसिया नृत्य (पूर्वांचल):</strong> <strong>जौनपुर जिले के कहार समुदाय</strong> द्वारा मांगलिक अवसरों पर किया जाने वाला विशिष्ट लोक नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kathghorwa Dance (काठघोड़वा नृत्य, Purvanchal):</strong> A dancer mounts a hollow wooden horse strapped to his waist and dances energetically surrounded by other musicians playing Jhanjh and Mridang.</span>
      <span class="lang-hi"><strong>काठघोड़वा नृत्य (पूर्वांचल):</strong> नर्तक अपनी कमर में लकड़ी का बना कृत्रिम घोड़ा बांधकर झांझ और मृदंग की तेज लय पर तीव्र गति से नृत्य करता है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Jogini Dance (जोगिनी नृत्य, Awadh):</strong> Performed in the Awadh region (Ayodhya, Lucknow) during <strong>Ram Navami</strong>; male dancers dress in feminine attire as wandering female ascetics (Joginis) and perform ecstatic dances in temple courtyards.</span>
      <span class="lang-hi"><strong>जोगिनी नृत्य (अवध):</strong> अवध क्षेत्र (अयोध्या) में <strong>रामनवमी</strong> के अवसर पर पुरुषों द्वारा स्त्री (जोगिनी) का वेश धारण कर मंदिरों में साध्वी भाव से किया जाने वाला भक्ति नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kala Bazi (कलाबाजी नृत्य, Awadh):</strong> Dancers ride a bamboo dummy horse (Kachhi Ghodi) and showcase daring acrobatics, balancing brass plates on sticks to the rhythm of 'Nakkara'.</span>
      <span class="lang-hi"><strong>कलाबाजी नृत्य (अवध):</strong> नर्तक कच्ची घोड़ी पर सवार होकर नगाड़े की थाप पर अद्भुत संतुलन, थाली घुमाने व कलाबाजियों का प्रदर्शन करते हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Dediya Dance (डेडिया नृत्य, Duab region):</strong> Women dance balancing clay pots (having holes with burning lamps inside) on their heads during Navratri in the Ganga-Yamuna Doab.</span>
      <span class="lang-hi"><strong>डेडिया नृत्य (दोआब क्षेत्र):</strong> गंगा-यमुना दोआब में नवरात्रि पर महिलाएं सिर पर छिद्रयुक्त मिट्टी के घड़े (जिसमें दीपक जलता है) रखकर देवी स्तुति में नृत्य करती हैं।</span>
    </li>
  </ul>
</div>

<!-- Card 6: Tribal Dances (Sonbhadra & Mirzapur) -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Tribal Dances of Sonbhadra &amp; Mirzapur Belt</span>
    <span class="lang-hi">5. सोनभद्र एवं मिर्जापुर अंचल के जनजातीय लोक नृत्य</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Karma Dance (कर्मा नृत्य) - Most Famous Tribal Dance of UP:</strong>
        <br/>• Performed by the <strong>Kharwar, Baiga, Kol, and Gond tribes</strong> in Sonbhadra and Mirzapur districts.
        <br/>• Performed on <strong>Karma Ekadashi (Bhadrapada month)</strong> around the sacred <em>Karam (Adina cordifolia) tree</em>, symbolizing environmental worship, agricultural prosperity, and human karma.
        <br/>• Men and women form intertwining rows, singing call-and-response verses to the rhythm of the <em>Mandar</em> drum.
      </span>
      <span class="lang-hi"><strong>कर्मा नृत्य - उ.प्र. का शीर्ष जनजातीय नृत्य:</strong>
        <br/>• सोनभद्र एवं मिर्जापुर जिलों में <strong>खरवार, बैगा, कोल एवं गोंड जनजातियों</strong> द्वारा प्रस्तुत।
        <br/>• भाद्रपद माह की <strong>कर्मा एकादशी</strong> पर पवित्र <em>करम वृक्ष</em> की शाखा की प्रतिष्ठा कर प्रकृति व कृषि समृद्धि हेतु आयोजित।
        <br/>• पुरुष व महिलाएं पंक्तिबद्ध होकर मांदर की गूंजती थाप पर एक-दूसरे की कमर में हाथ डालकर आगे-पीछे झुकते हुए नृत्य करते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Thadiya Dance (ठड़िया नृत्य):</strong> An indigenous tribal dance performed in the forested valleys of Sonbhadra for invoking ancestral deities and seeking divine blessings for childbirth (संतान कामना).</span>
      <span class="lang-hi"><strong>ठड़िया नृत्य:</strong> सोनभद्र के वनांचल में जनजातियों द्वारा कुलदेवता की प्रसन्नता एवं संतान प्राप्ति के आशीर्वाद हेतु किया जाने वाला अनुष्ठानिक नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Shila Dance (शीला नृत्य):</strong> A rhythmic wooden stick dance performed by tribal youth during festive village gatherings in Mirzapur and Sonbhadra.</span>
      <span class="lang-hi"><strong>शीला नृत्य:</strong> मिर्जापुर-सोनभद्र में जनजातीय युवाओं द्वारा डंडों की लयबद्ध थाप पर किया जाने वाला सामूहिक नृत्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Cholari Dance (चोलरी नृत्य):</strong> Performed by Mirzapur tribals during harvest and wedding ceremonies to invoke prosperity.</span>
      <span class="lang-hi"><strong>चोलरी नृत्य:</strong> मिर्जापुर के वनांचल में अच्छी फसल व वैवाहिक अवसरों पर संपन्न होने वाला लोक नृत्य।</span>
    </li>
  </ul>
</div>

<!-- Card 7: Master Comparison Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Master Matrix: UP Folk Dances, Regions, Communities &amp; Key Props</span>
    <span class="lang-hi">6. मास्टर मैट्रिक्स: उ.प्र. के लोक नृत्य, क्षेत्र, समुदाय एवं मुख्य वाद्य/उपकरण</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Folk Dance</span><span class="lang-hi">लोक नृत्य</span></th>
          <th><span class="lang-en">Primary Region</span><span class="lang-hi">प्रमुख क्षेत्र</span></th>
          <th><span class="lang-en">Associated Community</span><span class="lang-hi">संबद्ध समुदाय</span></th>
          <th><span class="lang-en">Core Prop / Defining Feature</span><span class="lang-hi">मुख्य उपकरण / विशिष्ट पहचान</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Charkula (चरकुला)</strong></span><span class="lang-hi"><strong>चरकुला</strong></span></td>
          <td><span class="lang-en">Braj (Mathura)</span><span class="lang-hi">ब्रज (मथुरा)</span></td>
          <td><span class="lang-en">Braj women</span><span class="lang-hi">ब्रज की महिलाएं</span></td>
          <td><span class="lang-en">108 oil lamps on a multi-tier wooden pyramid on head</span><span class="lang-hi">सिर पर 108 दीपकों का बहुमंजिला पिरामिड</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Pai-Danda (पाई-डंडा)</strong></span><span class="lang-hi"><strong>पाई-डंडा</strong></span></td>
          <td><span class="lang-en">Bundelkhand</span><span class="lang-hi">बुंदेलखंड</span></td>
          <td><span class="lang-en">Ahir / Yadav</span><span class="lang-hi">अहीर / यादव</span></td>
          <td><span class="lang-en">Short lathis struck together; Dandiya of Bundelkhand</span><span class="lang-hi">लाठियों की थाप; बुंदेलखंड का डांडिया</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Rai Dance (राई नृत्य)</strong></span><span class="lang-hi"><strong>राई नृत्य</strong></span></td>
          <td><span class="lang-en">Bundelkhand</span><span class="lang-hi">बुंदेलखंड</span></td>
          <td><span class="lang-en">Bedni / Ahir women</span><span class="lang-hi">बेड़नी / अहीर महिलाएं</span></td>
          <td><span class="lang-en">Peacock-like fast swirling movements to Mridang</span><span class="lang-hi">मृदंग पर मयूर जैसी द्रुत चाल (मयूर नृत्य)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Shaira / Saura (सौरा)</strong></span><span class="lang-hi"><strong>शैरा / सौरा</strong></span></td>
          <td><span class="lang-en">Bundelkhand</span><span class="lang-hi">बुंदेलखंड</span></td>
          <td><span class="lang-en">Agrarian youth</span><span class="lang-hi">कृषक युवा</span></td>
          <td><span class="lang-en">Sticks and green corn stalks at harvest</span><span class="lang-hi">फसल कटाई पर डंडे व ज्वार की हरी बालियां</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Khyal Dance (ख्याल)</strong></span><span class="lang-hi"><strong>ख्याल नृत्य</strong></span></td>
          <td><span class="lang-en">Bundelkhand</span><span class="lang-hi">बुंदेलखंड</span></td>
          <td><span class="lang-en">Bundelkhand families</span><span class="lang-hi">बुंदेलखंडी परिवार</span></td>
          <td><span class="lang-en">Paper-bamboo temple structure balanced on son's birth</span><span class="lang-hi">पुत्र जन्मोत्सव पर सिर पर रंगीन मंदिर की संरचना</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Dhuriya Dance (धुरिया)</strong></span><span class="lang-hi"><strong>धुरिया नृत्य</strong></span></td>
          <td><span class="lang-en">Bundelkhand</span><span class="lang-hi">बुंदेलखंड</span></td>
          <td><span class="lang-en">Prajapati (Kumhar)</span><span class="lang-hi">प्रजापति (कुम्हार)</span></td>
          <td><span class="lang-en">Men perform in female clothes and makeup</span><span class="lang-hi">पुरुषों द्वारा स्त्री वेश धारण करके नृत्य</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Dhobiya Dance (धोबिया)</strong></span><span class="lang-hi"><strong>धोबिया नृत्य</strong></span></td>
          <td><span class="lang-en">Purvanchal</span><span class="lang-hi">पूर्वांचल</span></td>
          <td><span class="lang-en">Dhobi community</span><span class="lang-hi">धोबी समुदाय</span></td>
          <td><span class="lang-en">Washerman and donkey comedic acrobatics</span><span class="lang-hi">धोबी व गधे का हास्य स्वांग व करतब</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Natwari Dance (नटवारी)</strong></span><span class="lang-hi"><strong>नटवारी नृत्य</strong></span></td>
          <td><span class="lang-en">Purvanchal</span><span class="lang-hi">पूर्वांचल</span></td>
          <td><span class="lang-en">Ahir community</span><span class="lang-hi">अहीर समुदाय</span></td>
          <td><span class="lang-en">Martial jumps, acrobatics dedicated to Lord Krishna</span><span class="lang-hi">नगाड़े पर कुश्ती पैंतरे व कृष्ण वंदना</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Chaurasiya (चौरसिया)</strong></span><span class="lang-hi"><strong>चौरसिया</strong></span></td>
          <td><span class="lang-en">Purvanchal (Jaunpur)</span><span class="lang-hi">पूर्वांचल (जौनपुर)</span></td>
          <td><span class="lang-en">Kahar community</span><span class="lang-hi">कहार समुदाय</span></td>
          <td><span class="lang-en">Graceful palanquin-carrier community celebrations</span><span class="lang-hi">कहारों का पारंपरिक मांगलिक नृत्य</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Jogini Dance (जोगिनी)</strong></span><span class="lang-hi"><strong>जोगिनी नृत्य</strong></span></td>
          <td><span class="lang-en">Awadh (Ayodhya)</span><span class="lang-hi">अवध (अयोध्या)</span></td>
          <td><span class="lang-en">Devotees</span><span class="lang-hi">श्रद्धालु</span></td>
          <td><span class="lang-en">Men cross-dress as female ascetics on Ram Navami</span><span class="lang-hi">रामनवमी पर पुरुषों द्वारा साध्वी वेश में नृत्य</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Kala Bazi (कलाबाजी)</strong></span><span class="lang-hi"><strong>कलाबाजी</strong></span></td>
          <td><span class="lang-en">Awadh</span><span class="lang-hi">अवध</span></td>
          <td><span class="lang-en">Folk performers</span><span class="lang-hi">लोक कलाकार</span></td>
          <td><span class="lang-en">Acrobatics on Kachhi Ghodi (dummy horse) to Nakkara</span><span class="lang-hi">कच्ची घोड़ी पर संतुलन व करतब</span></td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Karma Dance (कर्मा)</strong></span><span class="lang-hi"><strong>कर्मा नृत्य</strong></span></td>
          <td><span class="lang-en">Sonbhadra &amp; Mirzapur</span><span class="lang-hi">सोनभद्र एवं मिर्जापुर</span></td>
          <td><span class="lang-en">Kharwar, Baiga, Kol</span><span class="lang-hi">खरवार, बैगा, कोल जनजाति</span></td>
          <td><span class="lang-en">Nature/tree worship around Karam branch with Mandar</span><span class="lang-hi">करम वृक्ष पूजा, मांदर की थाप पर सामूहिक नृत्य</span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 8: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Rapid Revision Fact Matrix: UP Folk Dances (Direct Exam Points)</span>
    <span class="lang-hi">7. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. के लोक नृत्य (सीधे परीक्षा हेतु तथ्य)</span>
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
          <td><span class="lang-en">What is the sole classical dance of North India?</span><span class="lang-hi">उत्तर भारत का एकमात्र शास्त्रीय नृत्य कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Kathak (कथक)</strong> (Lucknow and Banaras Gharanas)</span><span class="lang-hi"><strong>कथक</strong> (लखनऊ एवं बनारस घराना)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which dance features 108 oil lamps balanced on a wooden pyramid?</span><span class="lang-hi">108 दीपकों का पिरामिड सिर पर रखकर कौन सा नृत्य किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Charkula Dance (चरकुला नृत्य)</strong> of Braj region</span><span class="lang-hi">ब्रज क्षेत्र का <strong>चरकुला नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which dance of Bundelkhand is identical to Gujarat's Dandiya?</span><span class="lang-hi">बुंदेलखंड का कौन सा नृत्य गुजरात के डांडिया के समान है?</span></td>
          <td><span class="lang-en"><strong>Pai-Danda / Diwari Dance (पाई-डंडा / दीवारी)</strong></span><span class="lang-hi"><strong>पाई-डंडा / दीवारी नृत्य</strong> (अहीर समुदाय द्वारा)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which folk dance is known as the 'Peacock Dance of Bundelkhand'?</span><span class="lang-hi">बुंदेलखंड का कौन सा लोक नृत्य 'मयूर नृत्य' कहलाता है?</span></td>
          <td><span class="lang-en"><strong>Rai Dance (राई नृत्य)</strong></span><span class="lang-hi"><strong>राई नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which Bundelkhand dance is performed on the birth of a son?</span><span class="lang-hi">पुत्र जन्म के उत्सव पर बुंदेलखंड में कौन सा नृत्य किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Khyal Dance (ख्याल नृत्य)</strong></span><span class="lang-hi"><strong>ख्याल नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which dance do Kumhar men perform dressed in female clothes?</span><span class="lang-hi">कुम्हार पुरुष स्त्री वेश धारण करके कौन सा नृत्य करते हैं?</span></td>
          <td><span class="lang-en"><strong>Dhuriya Dance (धुरिया नृत्य)</strong> in Bundelkhand</span><span class="lang-hi">बुंदेलखंड का <strong>धुरिया नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which community performs the famous Dhobiya dance of Purvanchal?</span><span class="lang-hi">पूर्वांचल का प्रसिद्ध धोबिया नृत्य किस समुदाय द्वारा किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Dhobi (washermen) community</strong> (धोबी समाज)</span><span class="lang-hi"><strong>धोबी समुदाय</strong> द्वारा</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which martial acrobatic dance is performed by Ahirs in Purvanchal?</span><span class="lang-hi">पूर्वांचल में अहीरों द्वारा नगाड़े पर कौन सा कलाबाजी नृत्य किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Natwari Dance (नटवारी नृत्य)</strong></span><span class="lang-hi"><strong>नटवारी नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which district is the Chaurasiya dance traditionally performed?</span><span class="lang-hi">चौरसिया नृत्य मुख्य रूप से किस जिले में कहारों द्वारा किया जाता है?</span></td>
          <td><span class="lang-en"><strong>Jaunpur district (जौनपुर जिला)</strong></span><span class="lang-hi"><strong>जौनपुर जिला</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which dance is performed during Ram Navami by cross-dressing men in Awadh?</span><span class="lang-hi">अवध में रामनवमी पर पुरुष स्त्री वेश धरकर कौन सा नृत्य करते हैं?</span></td>
          <td><span class="lang-en"><strong>Jogini Dance (जोगिनी नृत्य)</strong></span><span class="lang-hi"><strong>जोगिनी नृत्य</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which is the most prominent tribal folk dance of Sonbhadra/Mirzapur?</span><span class="lang-hi">सोनभद्र/मिर्जापुर का सबसे प्रमुख जनजातीय लोक नृत्य कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Karma Dance (कर्मा नृत्य)</strong> (Kharwar, Baiga, Kol tribes)</span><span class="lang-hi"><strong>कर्मा नृत्य</strong> (खरवार, बैगा व कोल जनजाति)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which dance is performed in Bundelkhand by youth at harvest with sticks?</span><span class="lang-hi">बुंदेलखंड में फसल कटाई पर युवाओं द्वारा डंडों से कौन सा नृत्य होता है?</span></td>
          <td><span class="lang-en"><strong>Shaira / Saura Dance (शैरा / सौरा नृत्य)</strong></span><span class="lang-hi"><strong>शैरा / सौरा नृत्य</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "folk-dances", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_folk_dances_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
