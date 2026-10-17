import os
import re

def build_wildlife_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Protected Areas Network &amp; Wildlife Hierarchy of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का संरक्षित क्षेत्र नेटवर्क एवं वन्यजीव संरचना</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Wildlife & Protected Areas of UP] --> B[1 National Park]
    A --> C[4 Tiger Reserves]
    A --> D[11 Wildlife Sanctuaries]
    A --> E[14 Bird Sanctuaries]
    A --> F[10 Ramsar Wetlands]
    A --> G[Special Wildlife Projects & Safaris]

    B --> B1[Dudhwa National Park: Lakhimpur Kheri 1977 | 490 sq km | Barasingha, Tiger, Rhino]

    C --> C1[1. Dudhwa TR: Lakhimpur Kheri 1987]
    C --> C2[2. Amangarh TR: Bijnor 2012 | Corbett Buffer]
    C --> C3[3. Pilibhit TR: Pilibhit 2014 | TX2 Global Award]
    C --> C4[4. Ranipur TR: Chitrakoot 2022 | 53rd in India, 4th in UP]

    D --> D1[Oldest: Chandraprabha Chandauli 1957]
    D --> D2[Largest: Hastinapur 2073 sq km 1986]
    D --> D3[Smallest: Mahavir Swami Lalitpur 5.4 sq km 1977]
    D --> D4[Specialized: National Chambal Agra/Etawah Gharials | Katarniaghat | Kaimur]

    E --> E1[Oldest: Nawabganj Shahid Chandra Shekhar Azad Unnao 1984]
    E --> E2[Largest: Lakh Bahosi Kannauj 80.24 sq km 1988]
    E --> E3[Smallest: Shekha Jheel Aligarh 0.25 sq km / Patna Etah 1.11 sq km]

    F --> F1[1st: Upper Ganga River Brijghat-Narora 2005]
    F --> F2[Others: Nawabganj, Samaspur, Sandi, Saman, Parvati Arga, Sarsai Nawar, Sur Sarovar, Haiderpur, Bakhira]

    G --> G1[2 Elephant Reserves: UP Elephant Reserve 2009 & Terai Elephant Reserve 2022]
    G --> G2[Safaris: Etawah Lion Safari & Lucknow Kukrail Night Safari]
    G --> G3[Vulture Conservation: Jatayu Center Farenda, Maharajganj]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के वन्यजीव एवं संरक्षित क्षेत्र] --> B[1 राष्ट्रीय उद्यान]
    A --> C[4 टाइगर रिजर्व]
    A --> D[11 वन्यजीव अभयारण्य]
    A --> E[14 पक्षी अभयारण्य]
    A --> F[10 रामसर आर्द्रभूमि स्थल]
    A --> G[विशेष वन्यजीव परियोजनाएं एवं सफारी]

    B --> B1[दुधवा राष्ट्रीय उद्यान: लखीमपुर खीरी 1977 | 490 वर्ग किमी | बारहसिंगा, बाघ, गैंडा]

    C --> C1[1. दुधवा टाइगर रिजर्व: लखीमपुर खीरी 1987]
    C --> C2[2. अमानगढ़ टाइगर रिजर्व: बिजनौर 2012 | कॉर्बेट बफर]
    C --> C3[3. पीलीभीत टाइगर रिजर्व: पीलीभीत 2014 | TX2 वैश्विक पुरस्कार]
    C --> C4[4. रानीपुर टाइगर रिजर्व: चित्रकूट 2022 | भारत का 53वां, यूपी का चौथा]

    D --> D1[सबसे पुराना: चन्द्रप्रभा चंदौली 1957]
    D --> D2[सबसे बड़ा: हस्तिनापुर 2073 वर्ग किमी 1986]
    D --> D3[सबसे छोटा: महावीर स्वामी ललितपुर 5.4 वर्ग किमी 1977]
    D --> D4[विशिष्ट: राष्ट्रीय चंबल घड़ियाल | कतर्नियाघाट | कैमूर]

    E --> E1[प्रथम/पुराना: नवाबगंज चंद्रशेखर आजाद उन्नाव 1984]
    E --> E2[सबसे बड़ा: लाख बहोसी कन्नौज 80.24 वर्ग किमी 1988]
    E --> E3[सबसे छोटा: शेखा झील अलीगढ़ 0.25 वर्ग किमी / पटना एटा 1.11 वर्ग किमी]

    F --> F1[प्रथम: ऊपरी गंगा नदी ब्रजघाट-नरौरा 2005]
    F --> F2[अन्य: नवाबगंज, समसपुर, सांडी, समन, पार्वती अरगा, सरसई नावर, सूर सरोवर, हैदरपुर, बखिरा]

    G --> G1[2 हाथी रिजर्व: यूपी एलीफेंट रिजर्व 2009 एवं तराई एलीफेंट रिजर्व 2022]
    G --> G2[सफारी: इटावा लायन सफारी एवं लखनऊ कुकरैल नाइट सफारी]
    G --> G3[गिद्ध संरक्षण: जटायु संरक्षण केंद्र फरेंदा, महाराजगंज]
    </div>
  </div>
</div>

<!-- Card 2: Dudhwa National Park Profile -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Dudhwa National Park: Profile &amp; Ecological Stature</span>
    <span class="lang-hi">1. दुधवा राष्ट्रीय उद्यान: परिचय एवं पारिस्थितिक महत्व</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Sole National Park of UP:</strong> Dudhwa is the <strong>only National Park in the state of Uttar Pradesh</strong>, situated in the Terai alluvial belt along the Indo-Nepal international border in <strong>Lakhimpur Kheri district</strong>.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश का एकमात्र राष्ट्रीय उद्यान:</strong> दुधवा <strong>उत्तर प्रदेश का एकमात्र राष्ट्रीय उद्यान</strong> है, जो <strong>लखीमपुर खीरी जिले</strong> में भारत-नेपाल अंतरराष्ट्रीय सीमा के तराई क्षेत्र में स्थित है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Historical Evolution &amp; Dates:</strong>
          <br>&bull; <em>1958:</em> Initially established as <strong>Sonaripur Wildlife Sanctuary</strong> to protect swamp deer.
          <br>&bull; <em>1968:</em> Expanded and renamed as <strong>Dudhwa Wildlife Sanctuary</strong>.
          <br>&bull; <em>1 February 1977:</em> Upgraded and notified as <strong>Dudhwa National Park</strong> (area: <strong>490 sq km</strong>) largely through the untiring conservation efforts of legendary naturalist 'Billy' Arjan Singh.
          <br>&bull; <em>1987-88:</em> Integrated into <strong>Project Tiger</strong> to form the <strong>Dudhwa Tiger Reserve</strong> by merging Dudhwa National Park with Kishanpur Wildlife Sanctuary (204 sq km) and later Katarniaghat Wildlife Sanctuary (400 sq km) in 2000.</span>
        <span class="lang-hi"><strong>ऐतिहासिक विकास एवं महत्वपूर्ण वर्ष:</strong>
          <br>&bull; <em>1958:</em> प्रारंभ में बारहसिंगा के संरक्षण हेतु <strong>सोनारीपुर वन्यजीव अभयारण्य</strong> के रूप में स्थापित।
          <br>&bull; <em>1968:</em> क्षेत्र विस्तार कर <strong>दुधवा वन्यजीव अभयारण्य</strong> नाम दिया गया।
          <br>&bull; <em>1 फरवरी 1977:</em> प्रसिद्ध वन्यजीव प्रेमी 'बिली' अर्जुन सिंह के प्रयासों से इसे <strong>दुधवा राष्ट्रीय उद्यान</strong> (क्षेत्रफल: <strong>490 वर्ग किमी</strong>) का दर्जा प्रदान किया गया।
          <br>&bull; <em>1987-88:</em> प्रोजेक्ट टाइगर के अंतर्गत दुधवा राष्ट्रीय उद्यान तथा किशनपुर अभयारण्य (204 वर्ग किमी) को मिलाकर <strong>दुधवा टाइगर रिजर्व</strong> बनाया गया (वर्ष 2000 में कतर्नियाघाट अभयारण्य भी इसमें शामिल किया गया)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Keystone Species &amp; Conservation Success:</strong>
          <br>&bull; <em>Swamp Deer (बारहसिंगा - Rucervus duvaucelii):</em> State animal of UP; Dudhwa shelters the largest surviving population of the endangered northern subspecies in the world.
          <br>&bull; <em>One-horned Rhinoceros (एक सींग वाला गैंडा):</em> Reintroduced successfully in Dudhwa in <strong>1984</strong> from Kaziranga (Assam) and Pobitora under the Rhino Reintroduction Project.
          <br>&bull; <em>Bengal Tiger &amp; Leopard:</em> Thriving apex predators in the Terai dense Sal and riverine grasslands.
          <br>&bull; <em>Hispid Hare &amp; Bengal Florican:</em> Critically rare grassland species protected in Dudhwa grasslands.</span>
        <span class="lang-hi"><strong>प्रमुख वन्यजीव एवं संरक्षण उपलब्धियां:</strong>
          <br>&bull; <em>बारहसिंगा (दलदली हिरण):</em> उत्तर प्रदेश का राजकीय पशु; विश्व में उत्तरी उप-प्रजाति की सर्वाधिक आबादी दुधवा के विशाल घास के मैदानों में निवास करती है।
          <br>&bull; <em>एक सींग वाला भारतीय गैंडा:</em> वर्ष <strong>1984</strong> में काजीरंगा (असम) एवं पोबितोरा से लाकर दुधवा में 'गेंडा पुनर्वास परियोजना' के तहत सफलतापूर्वक पुनर्वासित किया गया।
          <br>&bull; <em>रॉयल बंगाल टाइगर एवं तेंदुआ:</em> तराई के घने साल वनों एवं आर्द्रभूमि में शीर्ष शिकारी।
          <br>&bull; <em>हिसपिड खरगोश एवं बंगाल फ्लोरिकन:</em> दुधवा के घास के मैदानों में संरक्षित अत्यंत दुर्लभ प्रजातियां।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: 4 Tiger Reserves & 2 Elephant Reserves -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Four Tiger Reserves &amp; Two Elephant Reserves of Uttar Pradesh</span>
    <span class="lang-hi">2. उत्तर प्रदेश के चार टाइगर रिजर्व एवं दो हाथी रिजर्व</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Four Tiger Reserves of UP (चार टाइगर रिजर्व):</strong>
          <br>1. <strong>Dudhwa Tiger Reserve (1987):</strong> Located in <strong>Lakhimpur Kheri</strong> district; comprises Dudhwa National Park, Kishanpur Sanctuary, and Katarniaghat Sanctuary.
          <br>2. <strong>Amangarh Tiger Reserve (2012):</strong> Located in <strong>Bijnor</strong> district; declared as a dedicated buffer zone of Uttarakhand's Jim Corbett National Park after the bifurcation of Uttar Pradesh.
          <br>3. <strong>Pilibhit Tiger Reserve (2014):</strong> Located in <strong>Pilibhit</strong> district; recognized internationally with the prestigious <strong>TX2 Global Award (2020)</strong> for doubling its wild tiger population in just four years ahead of the 10-year target.
          <br>4. <strong>Ranipur Tiger Reserve (2022):</strong> Located in <strong>Chitrakoot</strong> district in Bundelkhand; declared as the <strong>53rd Tiger Reserve of India</strong> and the <strong>4th Tiger Reserve of Uttar Pradesh</strong> (notified on 19 October 2022, area ~529.89 sq km); does not possess its own resident tigers but serves as an active wildlife corridor for tigers from Panna Tiger Reserve (MP).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के चार टाइगर रिजर्व:</strong>
          <br>1. <strong>दुधवा टाइगर रिजर्व (1987):</strong> <strong>लखीमपुर खीरी</strong> जिला; इसमें दुधवा राष्ट्रीय उद्यान, किशनपुर एवं कतर्नियाघाट अभयारण्य शामिल हैं।
          <br>2. <strong>अमानगढ़ टाइगर रिजर्व (2012):</strong> <strong>बिजनौर</strong> जिला; उत्तराखंड विभाजन के उपरांत जिम कॉर्बेट नेशनल पार्क के बफर जोन के रूप में इसे अलग टाइगर रिजर्व घोषित किया गया।
          <br>3. <strong>पीलीभीत टाइगर रिजर्व (2014):</strong> <strong>पीलीभीत</strong> जिला; 10 वर्ष के लक्ष्य के सापेक्ष मात्र 4 वर्षों में बाघों की संख्या दोगुनी करने हेतु वैश्विक <strong>TX2 अवार्ड (2020)</strong> से सम्मानित।
          <br>4. <strong>रानीपुर टाइगर रिजर्व (2022):</strong> बुंदेलखंड के <strong>चित्रकूट</strong> जिले में स्थित; <strong>भारत का 53वां</strong> तथा <strong>उत्तर प्रदेश का चौथा टाइगर रिजर्व</strong> (19 अक्टूबर 2022 को अधिसूचित, क्षेत्रफल ~529.89 वर्ग किमी); यह मध्य प्रदेश के पन्ना टाइगर रिजर्व के बाघों हेतु एक सक्रिय प्राकृतिक गलियारा है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Tiger Population (All India Tiger Estimation 2022):</strong> Uttar Pradesh recorded a significant rise in wild tigers to <strong>205 tigers</strong> (up from 173 in 2018, and 117 in 2014).</span>
        <span class="lang-hi"><strong>बाघ गणना 2022 के आंकड़े:</strong> अखिल भारतीय बाघ आकलन 2022 के अनुसार उत्तर प्रदेश में बाघों की संख्या बढ़कर <strong>205</strong> हो गई है (2018 में 173 तथा 2014 में 117 थी)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Two Elephant Reserves of UP (दो हाथी रिजर्व):</strong>
          <br>&bull; <em>1. Uttar Pradesh Elephant Reserve (UPER, 2009):</em> Notified in September 2009 across <strong>Saharanpur and Bijnor</strong> districts (covering 744 sq km foothills and Shivalik corridors).
          <br>&bull; <em>2. Terai Elephant Reserve (TER, 2022):</em> Formally approved by MoEFCC in October 2022 across <strong>Lakhimpur Kheri and Pilibhit</strong> districts (covering <strong>3,049 sq km</strong>); recognized as the <strong>33rd Elephant Reserve of India</strong> and the 2nd Elephant Reserve of UP, protecting wild Asian Elephants and Indian Rhinos under Project Elephant (launched 1992).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के दो हाथी रिजर्व:</strong>
          <br>&bull; <em>1. उत्तर प्रदेश हाथी रिजर्व (2009):</em> सितंबर 2009 में <strong>सहारनपुर एवं बिजनौर</strong> जिलों में शिवालिक तलहटी (744 वर्ग किमी) में अधिसूचित।
          <br>&bull; <em>2. तराई हाथी रिजर्व (TER, 2022):</em> अक्टूबर 2022 में केंद्रीय पर्यावरण मंत्रालय द्वारा <strong>लखीमपुर खीरी एवं पीलीभीत</strong> में <strong>3,049 वर्ग किमी</strong> क्षेत्र में अधिसूचित; यह <strong>भारत का 33वां</strong> तथा उत्तर प्रदेश का दूसरा हाथी रिजर्व है (प्रोजेक्ट एलीफेंट 1992 के अंतर्गत)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Complete Directory of 11 Wildlife Sanctuaries -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Complete Directory of 11 Wildlife Sanctuaries (वन्यजीव अभयारण्य) of UP</span>
    <span class="lang-hi">3. उत्तर प्रदेश के 11 वन्यजीव अभयारण्यों की संपूर्ण निर्देशिका</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. Chandraprabha Wildlife Sanctuary (चंदौली - 1957):</strong>
          <br>&bull; <em>Historical Status:</em> <strong>Oldest Wildlife Sanctuary in Uttar Pradesh</strong> (established in 1957, area: 78 sq km).
          <br>&bull; <em>Legacy:</em> Experimental site for Asiatic Lion reintroduction in 1957; famous for Rajdari and Devdari waterfalls.</span>
        <span class="lang-hi"><strong>1. चन्द्रप्रभा वन्यजीव अभयारण्य (चंदौली - 1957):</strong>
          <br>&bull; <em>ऐतिहासिक स्थिति:</em> <strong>उत्तर प्रदेश का सबसे पहला/पुराना वन्यजीव अभयारण्य</strong> (स्थापना 1957, क्षेत्रफल 78 वर्ग किमी)।
          <br>&bull; <em>महत्व:</em> 1957 में एशियाई शेरों के पुनर्वास का प्रयोग; राजदारी एवं देवदारी जलप्रपातों हेतु प्रसिद्ध।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Hastinapur Wildlife Sanctuary (मेरठ/मुजफ्फरनगर/हापुड़/बिजनौर/अमरोहा - 1986):</strong>
          <br>&bull; <em>Size Status:</em> <strong>Largest Wildlife Sanctuary in Uttar Pradesh</strong> (spread across <strong>2,073 sq km</strong> over 5 districts).
          <br>&bull; <em>Fauna:</em> Swamp Deer, Nilgai, Leopard, and rich Gangetic aquatic life.</span>
        <span class="lang-hi"><strong>2. हस्तिनापुर वन्यजीव अभयारण्य (मेरठ/मुजफ्फरनगर/हापुड़/बिजनौर/अमरोहा - 1986):</strong>
          <br>&bull; <em>आकार:</em> <strong>उत्तर प्रदेश का सबसे बड़ा वन्यजीव अभयारण्य</strong> (5 जिलों में <strong>2,073 वर्ग किमी</strong> में विस्तृत)।
          <br>&bull; <em>वन्यजीव:</em> बारहसिंगा, नीलगाय, तेंदुआ तथा गंगा नदी की समृद्ध जैव विविधता।</span>
      </li>
      <li>
        <span class="lang-en"><strong>3. Mahavir Swami Wildlife Sanctuary (ललितपुर - 1977):</strong>
          <br>&bull; <em>Size Status:</em> <strong>Smallest Wildlife Sanctuary in Uttar Pradesh</strong> (area: only <strong>5.4 sq km</strong>).
          <br>&bull; <em>Fauna:</em> Leopards, jackals, langurs, and scrub plateau wildlife.</span>
        <span class="lang-hi"><strong>3. महावीर स्वामी वन्यजीव अभयारण्य (ललितपुर - 1977):</strong>
          <br>&bull; <em>आकार:</em> <strong>उत्तर प्रदेश का सबसे छोटा वन्यजीव अभयारण्य</strong> (क्षेत्रफल: मात्र <strong>5.4 वर्ग किमी</strong>)।
          <br>&bull; <em>वन्यजीव:</em> तेंदुआ, सियार, लंगूर एवं पठारी वन्यजीव।</span>
      </li>
      <li>
        <span class="lang-en"><strong>4. National Chambal Wildlife Sanctuary (आगरा एवं इटावा - 1979):</strong>
          <br>&bull; <em>Status:</em> Tri-state sanctuary (UP, MP, Rajasthan); established to protect the critically endangered <strong>Gharial (Gavialis gangeticus)</strong>, Mugger Crocodile, <strong>Gangetic River Dolphin</strong>, and Indian Skimmer.</span>
        <span class="lang-hi"><strong>4. राष्ट्रीय चंबल वन्यजीव अभयारण्य (आगरा एवं इटावा - 1979):</strong>
          <br>&bull; <em>विशेष स्थिति:</em> तीन राज्यों (यूपी, एमपी, राजस्थान) का संयुक्त अभयारण्य; <strong>घड़ियाल</strong>, मगरमच्छ, <strong>गंगा डॉल्फिन</strong> एवं इंडियन स्किमर के संरक्षण हेतु स्थापित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Other Major Sanctuaries:</strong>
          <br>&bull; <em>5. Katarniaghat Wildlife Sanctuary (Bahraich, 1976 - 400 sq km):</em> High tiger density, Gangetic dolphin, swamp deer, and gharials.
          <br>&bull; <em>6. Kishanpur Wildlife Sanctuary (Lakhimpur Kheri, 1972 - 204 sq km):</em> Core tiger and swamp deer habitat (Jhadi Tal).
          <br>&bull; <em>7. Kaimur Wildlife Sanctuary (Mirzapur &amp; Sonbhadra, 1982 - 501 sq km):</em> Blackbuck, chinkara, leopard, and rock art.
          <br>&bull; <em>8. Ranipur Wildlife Sanctuary (Chitrakoot, 1977 - 230 sq km):</em> Now part of Ranipur Tiger Reserve.
          <br>&bull; <em>9. Suhelwa Wildlife Sanctuary (Balrampur &amp; Shravasti, 1988 - 452 sq km):</em> Terai forest tiger/leopard corridor.
          <br>&bull; <em>10. Sohagibarwa Wildlife Sanctuary (Maharajganj, 1987 - 428 sq km):</em> Gandak basin tiger/leopard sanctuary.
          <br>&bull; <em>11. Turtle Wildlife Sanctuary / Kachhua Sanctuary:</em> Shifted from Varanasi (Ganga stretch) to Bhadohi/Mirzapur/Prayagraj stretch in 2020.</span>
        <span class="lang-hi"><strong>अन्य प्रमुख अभयारण्य:</strong>
          <br>&bull; <em>5. कतर्नियाघाट वन्यजीव अभयारण्य (बहराइच, 1976 - 400 वर्ग किमी):</em> उच्च बाघ घनत्व, गंगा डॉल्फिन, बारहसिंगा व घड़ियाल।
          <br>&bull; <em>6. किशनपुर वन्यजीव अभयारण्य (लखीमपुर खीरी, 1972 - 204 वर्ग किमी):</em> बाघ एवं बारहसिंगा का मुख्य आवास (झाड़ी ताल)।
          <br>&bull; <em>7. कैमूर वन्यजीव अभयारण्य (मिर्जापुर एवं सोनभद्र, 1982 - 501 वर्ग किमी):</em> कृष्णमृग (काला हिरण), चिंकारा, तेंदुआ।
          <br>&bull; <em>8. रानीपुर वन्यजीव अभयारण्य (चित्रकूट, 1977 - 230 वर्ग किमी):</em> अब रानीपुर टाइगर रिजर्व का भाग।
          <br>&bull; <em>9. सुहेलवा वन्यजीव अभयारण्य (बलरामपुर एवं श्रावस्ती, 1988 - 452 वर्ग किमी):</em> तराई वन बाघ गलियारा।
          <br>&bull; <em>10. सोहागीबरवा वन्यजीव अभयारण्य (महाराजगंज, 1987 - 428 वर्ग किमी):</em> गंडक घाटी में तेंदुआ व बाघ।
          <br>&bull; <em>11. कछुआ वन्यजीव अभयारण्य:</em> 2020 में वाराणसी से भदोही/मिर्जापुर/प्रयागराज गंगा क्षेत्र में स्थानांतरित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Complete Directory of 14 Bird Sanctuaries -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Complete Directory of 14 Bird Sanctuaries (पक्षी विहार) of UP</span>
    <span class="lang-hi">4. उत्तर प्रदेश के 14 पक्षी अभयारण्यों (पक्षी विहार) की संपूर्ण निर्देशिका</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>1. Nawabganj Bird Sanctuary (उन्नाव - 1984):</strong>
          <br>&bull; <strong>First / Oldest Bird Sanctuary in Uttar Pradesh</strong> (area: 2.25 sq km); renamed in 2015 as <strong>Shahid Chandra Shekhar Azad Bird Sanctuary</strong>. Ramsar site since 2019.</span>
        <span class="lang-hi"><strong>1. नवाबगंज पक्षी विहार (उन्नाव - 1984):</strong>
          <br>&bull; <strong>उत्तर प्रदेश का प्रथम / सबसे पुराना पक्षी अभयारण्य</strong> (क्षेत्रफल: 2.25 वर्ग किमी); 2015 में <strong>शहीद चंद्रशेखर आजाद पक्षी अभयारण्य</strong> नामकरण। 2019 से रामसर स्थल।</span>
      </li>
      <li>
        <span class="lang-en"><strong>2. Lakh Bahosi Bird Sanctuary (कन्नौज - 1988):</strong>
          <br>&bull; <strong>Largest Bird Sanctuary in Uttar Pradesh</strong> (spread over <strong>80.24 sq km</strong>); hosts massive flocks of migratory waterfowl, bar-headed geese, and pintails across Lakh and Bahosi lakes.</span>
        <span class="lang-hi"><strong>2. लाख बहोसी पक्षी विहार (कन्नौज - 1988):</strong>
          <br>&bull; <strong>उत्तर प्रदेश का सबसे बड़ा पक्षी अभयारण्य</strong> (क्षेत्रफल: <strong>80.24 वर्ग किमी</strong>); लाख एवं बहोसी झीलों पर साइबेरियाई व मध्य एशियाई प्रवासी पक्षियों का बसेरा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>3. Shekha Jheel Bird Sanctuary (अलीगढ़):</strong>
          <br>&bull; <strong>Smallest Bird Sanctuary in Uttar Pradesh</strong> by water body footprint (approx. <strong>0.25 sq km / 25 hectares</strong>).
          <br>&bull; <em>Note on Patna Bird Sanctuary (एटा - 1991):</em> Spread over <strong>1.11 sq km</strong>, widely asked in UPSSSC exams as the smallest full-fledged forest bird sanctuary; famed for wintering water birds.</span>
        <span class="lang-hi"><strong>3. शेखा झील पक्षी विहार (अलीगढ़):</strong>
          <br>&bull; आर्द्रभूमि क्षेत्र के आधार पर <strong>उत्तर प्रदेश का सबसे छोटा पक्षी विहार</strong> (लगभग <strong>0.25 वर्ग किमी / 25 हेक्टेयर</strong>)।
          <br>&bull; <em>पटना पक्षी विहार (एटा - 1991):</em> क्षेत्रफल <strong>1.11 वर्ग किमी</strong>; यूपीएसएसएससी परीक्षाओं में प्रायः इसे सबसे छोटे अधिसूचित पक्षी विहार के रूप में पूछा जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Directory of Other 11 Bird Sanctuaries:</strong>
          <br>&bull; <em>4. Samaspur Bird Sanctuary (Rae Bareli, 1987 - 7.99 sq km):</em> Ramsar site.
          <br>&bull; <em>5. Sandi Bird Sanctuary (Hardoi, 1990 - 3.09 sq km):</em> Ramsar site (Dahar lake).
          <br>&bull; <em>6. Bakhira Bird Sanctuary (Sant Kabir Nagar, 1990 - 28.94 sq km):</em> Largest natural freshwater lake in Eastern UP, Ramsar site 2022.
          <br>&bull; <em>7. Okhla Bird Sanctuary (Gautam Buddha Nagar, 1990 - 4.00 sq km):</em> Yamuna barrage wetland.
          <br>&bull; <em>8. Saman Bird Sanctuary (Mainpuri, 1990 - 5.25 sq km):</em> Sarus crane stronghold, Ramsar site.
          <br>&bull; <em>9. Parvati Arga Bird Sanctuary (Gonda, 1990 - 10.84 sq km):</em> Oxbow lakes, Ramsar site.
          <br>&bull; <em>10. Vijay Sagar Bird Sanctuary (Mahoba, 1990 - 2.62 sq km):</em> Bundelkhand lake.
          <br>&bull; <em>11. Sur Sarovar Bird Sanctuary / Keetham Lake (Agra, 1991 - 4.03 sq km):</em> Ramsar site, houses Bear Rescue Facility.
          <br>&bull; <em>12. Surha Tal Bird Sanctuary / Loknayak Jai Prakash Narayan (Ballia, 1991 - 34.32 sq km).</em>
          <br>&bull; <em>13. Dr. Bhimrao Ambedkar Bird Sanctuary / Behti Lake (Pratapgarh, 2003 - 4.27 sq km).</em></span>
        <span class="lang-hi"><strong>अन्य 11 पक्षी विहारों की निर्देशिका:</strong>
          <br>&bull; <em>4. समसपुर पक्षी विहार (रायबरेली, 1987 - 7.99 वर्ग किमी):</em> रामसर स्थल।
          <br>&bull; <em>5. सांडी पक्षी विहार (हरदोई, 1990 - 3.09 वर्ग किमी):</em> रामसर स्थल (दहर झील)।
          <br>&bull; <em>6. बखिरा पक्षी विहार (संत कबीर नगर, 1990 - 28.94 वर्ग किमी):</em> पूर्वी यूपी की सबसे बड़ी प्राकृतिक मीठे पानी की झील, रामसर स्थल 2022।
          <br>&bull; <em>7. ओखला पक्षी विहार (गौतमबुद्ध नगर, 1990 - 4.00 वर्ग किमी):</em> यमुना बैराज आर्द्रभूमि।
          <br>&bull; <em>8. समन पक्षी विहार (मैनपुरी, 1990 - 5.25 वर्ग किमी):</em> सारस क्रेन का प्रमुख केंद्र, रामसर स्थल।
          <br>&bull; <em>9. पार्वती अरगा पक्षी विहार (गोंडा, 1990 - 10.84 वर्ग किमी):</em> गोखुर झीलें, रामसर स्थल।
          <br>&bull; <em>10. विजय सागर पक्षी विहार (महोबा, 1990 - 2.62 वर्ग किमी):</em> बुंदेलखंड झील।
          <br>&bull; <em>11. सूर सरोवर पक्षी विहार / कीठम झील (आगरा, 1991 - 4.03 वर्ग किमी):</em> रामसर स्थल, भालू संरक्षण केंद्र स्थित।
          <br>&bull; <em>12. सुरहा ताल पक्षी विहार / लोकनायक जयप्रकाश नारायण (बलिया, 1991 - 34.32 वर्ग किमी)।</em>
          <br>&bull; <em>13. डॉ. भीमराव अंबेडकर पक्षी विहार / बेती झील (प्रतापगढ़, 2003 - 4.27 वर्ग किमी)।</em></span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: 10 Ramsar Wetland Sites of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Ten Ramsar Wetland Sites of International Importance in UP</span>
    <span class="lang-hi">5. उत्तर प्रदेश के 10 अंतरराष्ट्रीय महत्व के रामसर आर्द्रभूमि स्थल</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>National Standing:</strong> With <strong>10 Ramsar Sites</strong>, Uttar Pradesh has the <strong>second-highest number of Ramsar wetlands in India</strong> (after Tamil Nadu with 16).</span>
        <span class="lang-hi"><strong>राष्ट्रीय स्थिति:</strong> <strong>10 रामसर स्थलों</strong> के साथ उत्तर प्रदेश भारत में (तमिलनाडु के 16 स्थलों के बाद) <strong>द्वितीय सर्वाधिक रामसर आर्द्रभूमि वाला राज्य</strong> है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Chronological List of UP's 10 Ramsar Sites:</strong>
          <br>1. <strong>Upper Ganga River (ब्रजघाट से नरौरा खिंचाव):</strong> Designated in <strong>2005</strong> (first Ramsar site in UP); 82 km stretch of river Ganga harboring Gangetic Dolphins, Gharials, and Otters.
          <br>2. <strong>Nawabganj Bird Sanctuary (उन्नाव):</strong> Designated in <strong>2019</strong>.
          <br>3. <strong>Parvati Arga Bird Sanctuary (गोंडा):</strong> Designated in <strong>2019</strong>.
          <br>4. <strong>Saman Bird Sanctuary (मैनपुरी):</strong> Designated in <strong>2019</strong>.
          <br>5. <strong>Samaspur Bird Sanctuary (रायबरेली):</strong> Designated in <strong>2019</strong>.
          <br>6. <strong>Sandi Bird Sanctuary (हरदोई):</strong> Designated in <strong>2019</strong>.
          <br>7. <strong>Sarsai Nawar Jheel (इटावा):</strong> Designated in <strong>2019</strong>; vital breeding ground for the Sarus Crane.
          <br>8. <strong>Sur Sarovar / Keetham Lake (आगरा):</strong> Designated in <strong>November 2020</strong>.
          <br>9. <strong>Haiderpur Wetland (बिजनौर / मुजफ्फरनगर):</strong> Designated in <strong>December 2021</strong>; human-made wetland formed by the Madhya Ganga Canal barrage in Hastinapur WLS.
          <br>10. <strong>Bakhira Wildlife Sanctuary (संत कबीर नगर):</strong> Designated on World Wetlands Day, <strong>February 2022</strong>.</span>
        <span class="lang-hi"><strong>यूपी के 10 रामसर स्थलों की कालक्रमानुसार सूची:</strong>
          <br>1. <strong>ऊपरी गंगा नदी (ब्रजघाट से नरौरा):</strong> वर्ष <strong>2005</strong> में घोषित (यूपी का प्रथम रामसर स्थल); 82 किमी लंबा गंगा प्रवाह क्षेत्र जो डॉल्फिन, घड़ियाल और ऊदबिलाव का प्राकृतिक वास है।
          <br>2. <strong>नवाबगंज पक्षी अभयारण्य (उन्नाव):</strong> वर्ष <strong>2019</strong> में घोषित।
          <br>3. <strong>पार्वती अरगा पक्षी अभयारण्य (गोंडा):</strong> वर्ष <strong>2019</strong> में घोषित।
          <br>4. <strong>समन पक्षी अभयारण्य (मैनपुरी):</strong> वर्ष <strong>2019</strong> में घोषित।
          <br>5. <strong>समसपुर पक्षी अभयारण्य (रायबरेली):</strong> वर्ष <strong>2019</strong> में घोषित।
          <br>6. <strong>सांडी पक्षी अभयारण्य (हरदोई):</strong> वर्ष <strong>2019</strong> में घोषित।
          <br>7. <strong>सरसई नावर झील (इटावा):</strong> वर्ष <strong>2019</strong> में घोषित; सारस क्रेन का मुख्य प्रजनन क्षेत्र।
          <br>8. <strong>सूर सरोवर / कीठम झील (आगरा):</strong> <strong>नवंबर 2020</strong> में घोषित।
          <br>9. <strong>हैदरपुर आर्द्रभूमि (बिजनौर / मुजफ्फरनगर):</strong> <strong>दिसंबर 2021</strong> में घोषित; मध्य गंगा नहर बैराज द्वारा निर्मित मानव-निर्मित आर्द्रभूमि।
          <br>10. <strong>बखिरा वन्यजीव अभयारण्य (संत कबीर नगर):</strong> <strong>फरवरी 2022</strong> (विश्व आर्द्रभूमि दिवस) में घोषित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Special Wildlife Projects, Safaris & State Symbols -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Special Wildlife Projects, Safaris &amp; State Natural Symbols</span>
    <span class="lang-hi">6. विशेष वन्यजीव परियोजनाएं, सफारी एवं राजकीय प्राकृतिक प्रतीक</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Safaris &amp; Rescue Centers of UP:</strong>
          <br>&bull; <em>Etawah Safari Park (इटावा सफारी पार्क):</em> Located in Fisher Forest, Etawah; features specialized Lion Safari, Deer Safari, Bear Safari, and Leopard Safari; Asiatic Lion captive breeding center.
          <br>&bull; <em>Kukrail Forest Reserve &amp; Night Safari (लखनऊ):</em> World-renowned captive breeding center for <strong>Gharials and freshwater turtles</strong> established in 1975; currently developing <strong>India's first Night Safari</strong> over 350 acres on the Singapore model.
          <br>&bull; <em>Jatayu Conservation &amp; Breeding Center (महाराजगंज):</em> World's first conservation center dedicated to Asian King Vulture (Red-headed Vulture), established at Farenda, Maharajganj.
          <br>&bull; <em>Sur Sarovar Bear Rescue Facility (आगरा):</em> Largest sloth bear rehabilitation facility in India.</span>
        <span class="lang-hi"><strong>सफारी एवं बचाव केंद्र:</strong>
          <br>&bull; <em>इटावा सफारी पार्क:</em> फिशर वन, इटावा में स्थित; लायन सफारी, डियर सफारी, भालू सफारी एवं तेंदुआ सफारी; एशियाई शेरों का प्रजनन केंद्र।
          <br>&bull; <em>कुकरैल वन एवं नाइट सफारी (लखनऊ):</em> 1975 में स्थापित विश्वप्रसिद्ध <strong>घड़ियाल एवं कछुआ प्रजनन केंद्र</strong>; सिंगापुर की तर्ज पर 350 एकड़ में <strong>भारत की प्रथम नाइट सफारी</strong> विकसित की जा रही है।
          <br>&bull; <em>जटायु गिद्ध संरक्षण एवं प्रजनन केंद्र (महाराजगंज):</em> महाराजगंज के फरेंदा में एशियाई राजा गिद्ध (लाल सिर वाले गिद्ध) हेतु स्थापित विश्व का प्रथम समर्पित केंद्र।
          <br>&bull; <em>सूर सरोवर भालू संरक्षण केंद्र (कीठम, आगरा):</em> भारत का सबसे बड़ा स्लॉथ बीयर पुनर्वास केंद्र।</span>
      </li>
      <li>
        <span class="lang-en"><strong>State Aquatic Animal Declaration:</strong>
          <br>&bull; On <strong>October 2023</strong>, Uttar Pradesh officially declared the <strong>Gangetic River Dolphin (Platanista gangetica - सोंस / सूंस)</strong> as the <strong>State Aquatic Animal of Uttar Pradesh</strong> (it has been India's National Aquatic Animal since 2009).</span>
        <span class="lang-hi"><strong>राजकीय जलीय जीव की घोषणा:</strong>
          <br>&bull; <strong>अक्टूबर 2023</strong> में उत्तर प्रदेश सरकार ने <strong>गंगा डॉल्फिन (सोंस / सूंस)</strong> को उत्तर प्रदेश का <strong>राजकीय जलीय जीव</strong> घोषित किया (यह 2009 से भारत का राष्ट्रीय जलीय जीव है)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Complete State Natural Symbols of Uttar Pradesh:</strong>
          <br>&bull; <em>State Animal:</em> <strong>Swamp Deer (बारहसिंगा)</strong> (Rucervus duvaucelii).
          <br>&bull; <em>State Bird:</em> <strong>Sarus Crane (सारस / क्रौंच)</strong> (Grus antigone - world's tallest flying bird; UP hosts ~70% of India's Sarus population).
          <br>&bull; <em>State Tree:</em> <strong>Ashok (अशोक)</strong> (Saraca asoca).
          <br>&bull; <em>State Flower:</em> <strong>Palash / Tesu / Flame of the Forest (पलाश / टेसू)</strong> (Butea monosperma - declared on <strong>4 January 2011</strong>, replacing Brahma Kamal).
          <br>&bull; <em>State Fish:</em> <strong>Chital / Moh (चीतल)</strong> (Chitala chitala).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के संपूर्ण राजकीय प्राकृतिक प्रतीक:</strong>
          <br>&bull; <em>राजकीय पशु:</em> <strong>बारहसिंगा (दलदली हिरण)</strong>।
          <br>&bull; <em>राजकीय पक्षी:</em> <strong>सारस / क्रौंच</strong> (विश्व का सबसे ऊंचा उड़ने वाला पक्षी; भारत के ~70% सारस यूपी में पाए जाते हैं)।
          <br>&bull; <em>राजकीय वृक्ष:</em> <strong>अशोक</strong>।
          <br>&bull; <em>राजकीय पुष्प:</em> <strong>पलाश / टेसू</strong> (4 जनवरी 2011 को ब्रह्मकमल के स्थान पर घोषित)।
          <br>&bull; <em>राजकीय मछली:</em> <strong>चीतल / मोह</strong>।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master Tabular Directory of Protected Areas -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Comparison Directory: Wildlife &amp; Bird Sanctuaries of UP</span>
    <span class="lang-hi">7. उत्तर प्रदेश के वन्यजीव एवं पक्षी अभयारण्यों की महा-निर्देशिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Sanctuary Name</span>
            <span class="lang-hi">अभयारण्य का नाम</span>
          </th>
          <th>
            <span class="lang-en">District</span>
            <span class="lang-hi">जिला</span>
          </th>
          <th>
            <span class="lang-en">Year &amp; Area</span>
            <span class="lang-hi">स्थापना वर्ष एवं क्षेत्रफल</span>
          </th>
          <th>
            <span class="lang-en">Special Distinction</span>
            <span class="lang-hi">विशिष्ट पहचान</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Dudhwa National Park</span>
            <span class="lang-hi">दुधवा राष्ट्रीय उद्यान</span>
          </td>
          <td>
            <span class="lang-en">Lakhimpur Kheri</span>
            <span class="lang-hi">लखीमपुर खीरी</span>
          </td>
          <td>
            <span class="lang-en">1977 | 490 sq km</span>
            <span class="lang-hi">1977 | 490 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Only National Park of UP; Swamp Deer &amp; Rhino reintroduction (1984)</span>
            <span class="lang-hi">यूपी का एकमात्र राष्ट्रीय उद्यान; बारहसिंगा एवं गेंडा पुनर्वास</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chandraprabha WLS</span>
            <span class="lang-hi">चन्द्रप्रभा WLS</span>
          </td>
          <td>
            <span class="lang-en">Chandauli</span>
            <span class="lang-hi">चंदौली</span>
          </td>
          <td>
            <span class="lang-en">1957 | 78 sq km</span>
            <span class="lang-hi">1957 | 78 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Oldest Wildlife Sanctuary of UP; Rajdari waterfalls</span>
            <span class="lang-hi">यूपी का सबसे पहला वन्यजीव अभयारण्य; राजदारी जलप्रपात</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Hastinapur WLS</span>
            <span class="lang-hi">हस्तिनापुर WLS</span>
          </td>
          <td>
            <span class="lang-en">Meerut, MZN, Hapur, Bijnor, Amroha</span>
            <span class="lang-hi">मेरठ, मुजफ्फरनगर, हापुड़, बिजनौर, अमरोहा</span>
          </td>
          <td>
            <span class="lang-en">1986 | 2,073 sq km</span>
            <span class="lang-hi">1986 | 2,073 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Largest Wildlife Sanctuary of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का सबसे बड़ा वन्यजीव अभयारण्य</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Mahavir Swami WLS</span>
            <span class="lang-hi">महावीर स्वामी WLS</span>
          </td>
          <td>
            <span class="lang-en">Lalitpur</span>
            <span class="lang-hi">ललितपुर</span>
          </td>
          <td>
            <span class="lang-en">1977 | 5.4 sq km</span>
            <span class="lang-hi">1977 | 5.4 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Smallest Wildlife Sanctuary of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का सबसे छोटा वन्यजीव अभयारण्य</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Nawabganj Bird Sanctuary</span>
            <span class="lang-hi">नवाबगंज पक्षी विहार</span>
          </td>
          <td>
            <span class="lang-en">Unnao</span>
            <span class="lang-hi">उन्नाव</span>
          </td>
          <td>
            <span class="lang-en">1984 | 2.25 sq km</span>
            <span class="lang-hi">1984 | 2.25 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Oldest Bird Sanctuary of UP; Shahid Chandra Shekhar Azad; Ramsar</span>
            <span class="lang-hi">यूपी का सबसे पहला पक्षी विहार; शहीद चंद्रशेखर आजाद; रामसर</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Lakh Bahosi Bird Sanctuary</span>
            <span class="lang-hi">लाख बहोसी पक्षी विहार</span>
          </td>
          <td>
            <span class="lang-en">Kannauj</span>
            <span class="lang-hi">कन्नौज</span>
          </td>
          <td>
            <span class="lang-en">1988 | 80.24 sq km</span>
            <span class="lang-hi">1988 | 80.24 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Largest Bird Sanctuary of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का सबसे बड़ा पक्षी अभयारण्य</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Patna Bird Sanctuary</span>
            <span class="lang-hi">पटना पक्षी विहार</span>
          </td>
          <td>
            <span class="lang-en">Etah</span>
            <span class="lang-hi">एटा</span>
          </td>
          <td>
            <span class="lang-en">1991 | 1.11 sq km</span>
            <span class="lang-hi">1991 | 1.11 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">Smallest Bird Sanctuary by notified forest area</span>
            <span class="lang-hi">अधिसूचित वन क्षेत्र में सबसे छोटा पक्षी विहार</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Ranipur Tiger Reserve</span>
            <span class="lang-hi">रानीपुर टाइगर रिजर्व</span>
          </td>
          <td>
            <span class="lang-en">Chitrakoot</span>
            <span class="lang-hi">चित्रकूट</span>
          </td>
          <td>
            <span class="lang-en">2022 | 529.89 sq km</span>
            <span class="lang-hi">2022 | 529.89 वर्ग किमी</span>
          </td>
          <td>
            <span class="lang-en">53rd Tiger Reserve of India / 4th of UP</span>
            <span class="lang-hi">भारत का 53वां एवं यूपी का चौथा टाइगर रिजर्व</span>
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
            <span class="lang-en">First Wildlife Sanctuary in UP</span>
            <span class="lang-hi">उत्तर प्रदेश का प्रथम वन्यजीव अभयारण्य</span>
          </td>
          <td>
            <span class="lang-en"><strong>Chandraprabha WLS (Chandauli, 1957)</strong>.</span>
            <span class="lang-hi"><strong>चन्द्रप्रभा (चंदौली, 1957)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Bird Sanctuary in UP</span>
            <span class="lang-hi">उत्तर प्रदेश का प्रथम पक्षी विहार</span>
          </td>
          <td>
            <span class="lang-en"><strong>Nawabganj (Unnao, 1984)</strong> (Shahid Chandra Shekhar Azad).</span>
            <span class="lang-hi"><strong>नवाबगंज (उन्नाव, 1984)</strong> (शहीद चंद्रशेखर आजाद)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Largest Bird Sanctuary in UP</span>
            <span class="lang-hi">उत्तर प्रदेश का सबसे बड़ा पक्षी विहार</span>
          </td>
          <td>
            <span class="lang-en"><strong>Lakh Bahosi (Kannauj, 80.24 sq km)</strong>.</span>
            <span class="lang-hi"><strong>लाख बहोसी (कन्नौज, 80.24 वर्ग किमी)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Smallest Wildlife Sanctuary in UP</span>
            <span class="lang-hi">उत्तर प्रदेश का सबसे छोटा वन्यजीव अभयारण्य</span>
          </td>
          <td>
            <span class="lang-en"><strong>Mahavir Swami WLS (Lalitpur, 5.4 sq km)</strong>.</span>
            <span class="lang-hi"><strong>महावीर स्वामी (ललितपुर, 5.4 वर्ग किमी)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">4th Tiger Reserve of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का चौथा टाइगर रिजर्व</span>
          </td>
          <td>
            <span class="lang-en"><strong>Ranipur Tiger Reserve (Chitrakoot, 2022)</strong> (53rd in India).</span>
            <span class="lang-hi"><strong>रानीपुर टाइगर रिजर्व (चित्रकूट, 2022)</strong> (भारत का 53वां)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">TX2 Global Award Winner</span>
            <span class="lang-hi">TX2 अंतरराष्ट्रीय पुरस्कार विजेता</span>
          </td>
          <td>
            <span class="lang-en"><strong>Pilibhit Tiger Reserve (2020)</strong>.</span>
            <span class="lang-hi"><strong>पीलीभीत टाइगर रिजर्व (2020)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Total Ramsar Wetland Sites in UP</span>
            <span class="lang-hi">उत्तर प्रदेश में कुल रामसर स्थल</span>
          </td>
          <td>
            <span class="lang-en"><strong>10 Sites</strong> (2nd highest in India after Tamil Nadu).</span>
            <span class="lang-hi"><strong>10 स्थल</strong> (तमिलनाडु के बाद भारत में दूसरा स्थान)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Ramsar Site of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का प्रथम रामसर स्थल</span>
          </td>
          <td>
            <span class="lang-en"><strong>Upper Ganga River (Brijghat to Narora, 2005)</strong>.</span>
            <span class="lang-hi"><strong>ऊपरी गंगा नदी (ब्रजघाट से नरौरा, 2005)</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">State Aquatic Animal of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का राजकीय जलीय जीव</span>
          </td>
          <td>
            <span class="lang-en"><strong>Gangetic River Dolphin (Platanista gangetica)</strong> (declared Oct 2023).</span>
            <span class="lang-hi"><strong>गंगा डॉल्फिन</strong> (अक्टूबर 2023 में घोषित)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Asian King Vulture Conservation Center</span>
            <span class="lang-hi">एशियाई राजा गिद्ध (जटायु) संरक्षण केंद्र</span>
          </td>
          <td>
            <span class="lang-en"><strong>Farenda (Maharajganj district)</strong>.</span>
            <span class="lang-hi"><strong>फरेंदा (महाराजगंज जिला)</strong>।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "wildlife", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_wildlife_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
