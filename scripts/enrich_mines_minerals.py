import os
import re

def build_mines_minerals_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Mineral Classification, Key Districts &amp; Mining Administration in UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के खनिज वर्गीकरण, प्रमुख उत्पादक जिले एवं खनन प्रशासन</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Mines & Minerals of Uttar Pradesh] --> B[Energy & Fuel Minerals]
    A --> C[Metallic Minerals]
    A --> D[Non-Metallic & Industrial]
    A --> E[Refractory & Ceramics]
    A --> F[Building & Dimensional Stones]
    A --> G[Mining Administration & Policy]

    B --> B1[Coal: Singrauli Belt, Sonbhadra | Gondwana Rocks | Rank 8th]
    B --> B2[Uranium: Exclusive to Lalitpur District | Bijawar Rocks]

    C --> C1[Bauxite: Banda, Chitrakoot, Lalitpur, Varanasi | Feeds Hindalco]
    C --> C2[Gold: Son Pahadi & Hardi Sonbhadra | Placer: Sharda & Ramganga]
    C --> C3[Copper: Sonrai Area, Lalitpur]
    C --> C4[Iron Ore: Solda, Lalitpur | PGE Traces: Lalitpur]

    D --> D1[Silica Sand: Shankargarh Prayagraj | Rank 2nd in India]
    D --> D2[Limestone: Gurma, Kanach, Kajrahat Sonbhadra | Churk & Dalla]
    D --> D3[Dolomite: Kajrahat Sonbhadra, Banda | Steel Flux]
    D --> D4[Rock Phosphate: Lalitpur Pisnari & Banda | Fertilizer Input]

    E --> E1[Diaspore: Jhansi, Lalitpur, Hamirpur | Rank 1st in India]
    E --> E2[Pyrophyllite: Jhansi, Hamirpur, Mahoba | Ceramics & Refractory]
    E --> E3[Fire Clay: Bansi Mirzapur, Makrikhoh Sonbhadra]
    E --> E4[China Clay: Sonbhadra & Banda | Khurja Pottery]

    F --> F1[Sandstone: Chunar Mirzapur | Mauryan Pillars to Modern Ghats]
    F --> F2[Granite: Bundelkhand Pink & Grey | Lalitpur, Jhansi, Mahoba]
    F --> F3[Marble: Mirzapur & Sonbhadra | Gypsum: Jhansi & Hamirpur]

    G --> G1[Directorate of Geology & Mining: Est. 1955, Lucknow]
    G --> G2[First Mineral Policy Dec 1998: Declared Minerals as Industry]
    G --> G3[12 Mineral-Rich Districts Notified | Mining Policy 2017 Target 3% GSDP]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के खनिज संसाधन] --> B[ऊर्जा एवं ईंधन खनिज]
    A --> C[धात्विक खनिज]
    A --> D[अधात्विक एवं औद्योगिक खनिज]
    A --> E[रिफ्रैक्टरी एवं सिरेमिक खनिज]
    A --> F[इमारती एवं सजावटी पत्थर]
    A --> G[खनन प्रशासन एवं नीतियां]

    B --> B1[कोयला: सिंगरौली क्षेत्र, सोनभद्र | गोंडवाना शैल | 8वां स्थान]
    B --> B2[यूरेनियम: केवल ललितपुर जिला | बिजावर शैल समूह]

    C --> C1[बॉक्साइट: बांदा, चित्रकूट, ललितपुर, वाराणसी | हिंडाल्को को आपूर्ति]
    C --> C2[स्वर्ण: सोन पहाड़ी व हरदी सोनभद्र | प्लेसर: शारदा व रामगंगा]
    C --> C3[तांबा: सोनराई क्षेत्र, ललितपुर]
    C --> C4[लौह अयस्क: सोल्डा, ललितपुर | प्लेटिनम समूह: ललितपुर]

    D --> D1[सिलिका बालू: शंकरगढ़ प्रयागराज | देश में द्वितीय स्थान]
    D --> D2[चूना पत्थर: गुरमा, कनाच, कजराहट सोनभद्र | चुर्क व डाला]
    D --> D3[डोलोमाइट: कजराहट सोनभद्र, बांदा | इस्पात संयंत्र हेतु फ्लक्स]
    D --> D4[रॉक फास्फेट: ललितपुर पिसनारी व बांदा | उर्वरक उद्योग]

    E --> E1[डायस्पोर: झांसी, ललितपुर, हमीरपुर | देश में प्रथम स्थान]
    E --> E2[पायरोफिलाइट: झांसी, हमीरपुर, महोबा | सिरेमिक व रिफ्रैक्टरी]
    E --> E3[फायर क्ले: बांसी मिर्जापुर, मकरीखोह सोनभद्र]
    E --> E4[चाइना क्ले: सोनभद्र व बांदा | खुर्जा पॉटरी उद्योग]

    F --> F1[बलुआ पत्थर: चुनार मिर्जापुर | मौर्य कालीन स्तंभ से आधुनिक घाट]
    F --> F2[ग्रेनाइट: बुंदेलखंड गुलाबी व धूसर | ललितपुर, झांसी, महोबा]
    F --> F3[संगमरमर: मिर्जापुर व सोनभद्र | जिप्सम: झांसी व हमीरपुर]

    G --> G1[भूतत्व एवं खनिकर्म निदेशालय: स्थापना 1955, लखनऊ]
    G --> G2[प्रथम खनिज नीति दिसंबर 1998: खनिज को उद्योग का दर्जा]
    G --> G3[12 खनिज बाहुल्य जिले घोषित | खनन नीति 2017: GSDP में 3% लक्ष्य]
    </div>
  </div>
</div>

<!-- Card 2: Mining Administration, Legal Framework & Policies -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Mining Administration, Statutory Framework &amp; Mineral Policies of UP</span>
    <span class="lang-hi">1. उत्तर प्रदेश में खनन प्रशासन, विधिक ढांचा एवं खनिज नीतियां</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Directorate of Geology and Mining (भूतत्व एवं खनिकर्म निदेशालय):</strong> Established in <strong>1955</strong> with headquarters at Lucknow; nodal state agency responsible for mineral survey, geo-exploration, regulation of mineral extraction, and revenue collection.</span>
        <span class="lang-hi"><strong>भूतत्व एवं खनिकर्म निदेशालय:</strong> स्थापना <strong>1955</strong> में लखनऊ मुख्यालय के साथ; खनिज सर्वेक्षण, भूगर्भीय पूर्वेक्षण, खनन नियमन एवं राजस्व संग्रहण हेतु उत्तर प्रदेश की नोडल संस्था।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP State Mineral Development Corporation (खनिज विकास निगम):</strong> Formed in <strong>1974</strong> for commercial exploitation and marketing of minerals; officially wound up in 2020 with administrative powers reverted to the Directorate.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश राज्य खनिज विकास निगम:</strong> खनिजों के वाणिज्यिक दोहन एवं विपणन हेतु <strong>1974</strong> में स्थापित; वर्ष 2020 में इसे समाप्त कर इसके दायित्व निदेशालय को सौंपे गए।</span>
      </li>
      <li>
        <span class="lang-en"><strong>First Mineral Policy (प्रथम खनिज नीति - December 1998):</strong> Landmark policy that accorded <strong>'Industry' status (उद्योग का दर्जा)</strong> to mineral development and formally declared <strong>12 mineral-rich districts</strong>.</span>
        <span class="lang-hi"><strong>प्रथम खनिज नीति (दिसंबर 1998):</strong> ऐतिहासिक नीति जिसके द्वारा खनिज विकास को <strong>'उद्योग' का दर्जा</strong> प्रदान किया गया तथा <strong>12 खनिज बाहुल्य जिले</strong> विधिवत अधिसूचित किए गए।</span>
      </li>
      <li>
        <span class="lang-en"><strong>12 Declared Mineral-Rich Districts:</strong> Prayagraj, Kaushambi, Jhansi, Lalitpur, Hamirpur, Mahoba, Banda, Chitrakoot, Mirzapur, Sonbhadra, Chandauli, and Saharanpur (chiefly for boulder/bajri/sand in Shivalik foothills).</span>
        <span class="lang-hi"><strong>12 अधिसूचित खनिज बाहुल्य जिले:</strong> प्रयागराज, कौशाम्बी, झांसी, ललितपुर, हमीरपुर, महोबा, बांदा, चित्रकूट, मिर्जापुर, सोनभद्र, चंदौली, तथा सहारनपुर (शिवालिक तलहटी में बोल्डर/बजरी/रेत हेतु)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Mining Policy 2017 Key Reforms:</strong> Targeted increasing mining sector contribution from 1.5% to <strong>3.0% of GSDP</strong>; introduced mandatory e-auctioning for mining leases, GPS-based vehicle tracking, and <strong>E-MMS (E-Mineral Management System)</strong> transit passes to curb illegal mining.</span>
        <span class="lang-hi"><strong>खनन नीति 2017 के प्रमुख सुधार:</strong> जीएसडीपी में खनन क्षेत्र का योगदान 1.5% से बढ़ाकर <strong>3.0%</strong> करने का लक्ष्य; पट्टों हेतु अनिवार्य ई-नीलामी, जीपीएस वाहन ट्रैकिंग, तथा अवैध खनन रोकने हेतु <strong>E-MMS (ई-परिवहन प्रपत्र)</strong> प्रणाली लागू की गई।</span>
      </li>
      <li>
        <span class="lang-en"><strong>District Mineral Foundation Trust (DMFT / जिला खनिज फाउंडेशन न्यास):</strong> Set up under Section 9B of MMDR Act 2015 in all mining districts; funded by mining royalties to finance drinking water, health, and infrastructure in mining-affected villages.</span>
        <span class="lang-hi"><strong>जिला खनिज फाउंडेशन न्यास (DMFT):</strong> MMDR अधिनियम 2015 की धारा 9B के तहत सभी खनन जिलों में गठित; खनन रॉयल्टी के अंश से खनन प्रभावित गांवों में पेयजल, स्वास्थ्य एवं आधारभूत संरचना का वित्तपोषण।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Major vs Minor Minerals (मुख्य बनाम उपखनिज):</strong> Major minerals (coal, bauxite, limestone, silica sand) governed under Central MMDR Act 1957; Minor minerals (sand, morrum, bajri, kankar, building stone) governed by State under UP Minor Mineral Concession Rules 1963 and generate the bulk of state mining revenue.</span>
        <span class="lang-hi"><strong>मुख्य बनाम उपखनिज:</strong> मुख्य खनिज (कोयला, बॉक्साइट, चूना पत्थर, सिलिका बालू) केंद्रीय MMDR अधिनियम 1957 से शासित; उपखनिज (रेत, मौरंग, बजरी, कंकड़, गिट्टी) यूपी उपखनिज रियायत नियमावली 1963 से शासित हैं तथा राज्य खनन राजस्व का प्रमुख स्रोत हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Energy Minerals: Coal & Radioactive Elements -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Energy Minerals: Coal (Singrauli Belt) &amp; Uranium Deposits</span>
    <span class="lang-hi">2. ऊर्जा खनिज: कोयला (सिंगरौली क्षेत्र) एवं यूरेनियम भंडार</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Coal Reserves &amp; Geological Horizon:</strong> Found exclusively in the <strong>Singrauli coalfield</strong> in <strong>Sonbhadra district</strong>; belongs to the <strong>Lower Gondwana Barakar formation</strong>; estimated reserves ~1,061 million tonnes (~1.06% of national reserves, ranking 8th in India).</span>
        <span class="lang-hi"><strong>कोयला भंडार एवं भूगर्भीय संरचना:</strong> विशेष रूप से <strong>सोनभद्र जिले</strong> के <strong>सिंगरौली कोयला क्षेत्र</strong> में विद्यमान; <strong>निचली गोंडवाना बराकर शैल समूह</strong> से संबंधित; अनुमानित भंडार ~1,061 मिलियन टन (राष्ट्रीय भंडार का ~1.06%, भारत में 8वां स्थान)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Major Coal Mining Blocks:</strong> Kota, Bina, Khadia, Dudhichua, Kakri, and Krishnashila; operated primarily by Northern Coalfields Limited (NCL), a subsidiary of Coal India.</span>
        <span class="lang-hi"><strong>प्रमुख कोयला खनन ब्लॉक:</strong> कोटा, बीना, खड़िया, दुद्धीचुआ, ककरी, तथा कृष्णशिला; इनका संचालन मुख्य रूप से कोल इंडिया की सहायक कंपनी नॉर्दर्न कोलफील्ड्स लिमिटेड (NCL) द्वारा किया जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Power Plant Linkages:</strong> Singrauli coal pithead feeds massive super thermal power stations including <strong>Singrauli Super Thermal (Shaktinagar)</strong>, <strong>Rihand Super Thermal</strong>, <strong>Anpara Thermal</strong>, and <strong>Obra Thermal Power Station</strong>, making Sonbhadra the 'Energy Capital of UP'.</span>
        <span class="lang-hi"><strong>विद्युत संयंत्र लिंकेज:</strong> सिंगरौली कोयला सीधे विशाल थर्मल पावर स्टेशनों जैसे <strong>सिंगरौली सुपर थर्मल (शक्तिनगर)</strong>, <strong>रिहंद सुपर थर्मल</strong>, <strong>अनपरा ताप विद्युत</strong>, और <strong>ओबरा ताप विद्युत केंद्र</strong> को ईंधन देता है, जिससे सोनभद्र को 'यूपी की ऊर्जा राजधानी' कहा जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Uranium (यूरेनियम):</strong> Confined exclusively to <strong>Lalitpur district</strong>; occurs in the bitumenized and sheared quartzite veins of the <strong>Bijawar Group</strong> near Sonrai-Pipra; regulated directly by the Department of Atomic Energy (DAE).</span>
        <span class="lang-hi"><strong>यूरेनियम:</strong> उत्तर प्रदेश में केवल <strong>ललितपुर जिले</strong> में सीमित भंडार; सोनराई-पिपरा के पास <strong>बिजावर समूह</strong> की क्वार्टजाइट शिराओं में पाया जाता है; परमाणु ऊर्जा विभाग (DAE) द्वारा नियंत्रित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Metallic Minerals: Gold, Copper, Bauxite & Iron Ore -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Metallic Minerals: Gold, Bauxite, Copper, Iron Ore &amp; Platinum Group</span>
    <span class="lang-hi">3. धात्विक खनिज: स्वर्ण, बॉक्साइट, तांबा, लौह अयस्क एवं प्लेटिनम समूह</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Gold (स्वर्ण - Sonbhadra &amp; River Placers):</strong>
          <br>&bull; <em>Lode Gold:</em> Major auriferous quartz veins discovered by GSI at <strong>Son Pahadi (सोन पहाड़ी)</strong> and <strong>Hardi (हरदी)</strong> blocks in Sonbhadra district.
          <br>&bull; <em>Placer Gold:</em> Alluvial gold dust panned traditionally from the riverbed sands of <strong>Sharda</strong> (Pilibhit/Lakhimpur) and <strong>Ramganga</strong> rivers.</span>
        <span class="lang-hi"><strong>स्वर्ण (सोनभद्र एवं नदीय प्लेसर):</strong>
          <br>&bull; <em>शिरा स्वर्ण:</em> भारतीय भूवैज्ञानिक सर्वेक्षण (GSI) द्वारा सोनभद्र जिले के <strong>सोन पहाड़ी</strong> एवं <strong>हरदी</strong> ब्लॉकों में स्वर्ण-युक्त क्वार्ट्ज शिराओं की खोज।
          <br>&bull; <em>प्लेसर स्वर्ण:</em> <strong>शारदा</strong> (पीलीभीत/लखीमपुर) और <strong>रामगंगा</strong> नदियों के रेत और बजरी निक्षेपों से पारंपरिक रूप से स्वर्ण कण प्राप्त किए जाते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Bauxite (बॉक्साइट - Aluminium Ore):</strong> Found in the lateritic caps of the Vindhyan plateau in <strong>Banda</strong> (Rajapur, Manikpur, Karwi), <strong>Chitrakoot</strong>, <strong>Lalitpur</strong>, and <strong>Chandauli/Varanasi</strong> (Naugarh area); directly feeds Hindalco's Renukoot aluminum smelter.</span>
        <span class="lang-hi"><strong>बॉक्साइट (एल्युमीनियम अयस्क):</strong> विंध्य पठार के लेटराइट निक्षेपों में <strong>बांदा</strong> (राजापुर, मानिकपुर, कर्वी), <strong>चित्रकूट</strong>, <strong>ललितपुर</strong>, तथा <strong>चंदौली/वाराणसी</strong> (नौगढ़ क्षेत्र) में पाया जाता है; हिंडाल्को के रेणुकूट एल्युमीनियम संयंत्र को आपूर्ति।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Copper (तांबा):</strong> Concentrated in the <strong>Sonrai area of Lalitpur district</strong>; occurs in quartz reefs and basic volcanic rocks of the Bijawar system as chalcopyrite and malachite.</span>
        <span class="lang-hi"><strong>तांबा:</strong> मुख्य रूप से <strong>ललितपुर जिले के सोनराई क्षेत्र</strong> में केंद्रित; बिजावर शैल समूह की क्वार्ट्ज रीफ एवं ज्वालामुखीय चट्टानों में काल्कोप्राइट एवं मैलाकाइट के रूप में विद्यमान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Iron Ore (लौह अयस्क):</strong> Low-to-medium grade hematite and banded iron formation (BIF) located in <strong>Solda area of Lalitpur district</strong>.</span>
        <span class="lang-hi"><strong>लौह अयस्क:</strong> निम्न से मध्यम श्रेणी का हेमेटाइट एवं बैंडेड आयरन फॉर्मेशन (BIF) <strong>ललितपुर जिले के सोल्डा क्षेत्र</strong> में पाया जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Platinum Group of Elements (PGE):</strong> Traces identified in the ultramafic rock complexes of <strong>Lalitpur district</strong> during modern multi-element geochemical mapping.</span>
        <span class="lang-hi"><strong>प्लेटिनम समूह तत्व (PGE):</strong> आधुनिक बहु-तत्व भूरासायनिक मानचित्रण के दौरान <strong>ललितपुर जिले</strong> के अल्ट्रामैफिक शैल समूहों में प्लेटिनम समूह के तत्वों के संकेत मिले हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Non-Metallic & Industrial Minerals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Industrial Minerals: Silica Sand, Limestone, Dolomite &amp; Rock Phosphate</span>
    <span class="lang-hi">4. औद्योगिक खनिज: सिलिका बालू, चूना पत्थर, डोलोमाइट एवं रॉक फास्फेट</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Silica Sand / Glass Sand (सिलिका बालू / कांच बालू):</strong>
          <br>&bull; <em>National Standing:</em> UP ranks <strong>2nd in India</strong> for silica sand production.
          <br>&bull; <em>Primary Hubs:</em> <strong>Shankargarh, Jasra, Lohgarh (Prayagraj district)</strong> produce high-purity glass-grade sand derived from weathering of Vindhyan sandstones (Kaimur series).
          <br>&bull; <em>Other Belts:</em> Bargarh (Banda), Rajapur &amp; Manikpur (Chitrakoot), and riverbed sands of Ganga and Yamuna.
          <br>&bull; <em>Industrial Consumers:</em> Firozabad glassware &amp; bangles cluster, Naini (Prayagraj) glass container units, and solar glass plants.</span>
        <span class="lang-hi"><strong>सिलिका बालू / कांच बालू:</strong>
          <br>&bull; <em>राष्ट्रीय स्थान:</em> उत्तर प्रदेश देश में सिलिका बालू उत्पादन में <strong>द्वितीय स्थान</strong> पर है।
          <br>&bull; <em>प्रमुख केंद्र:</em> <strong>शंकरगढ़, जसरा, लोहगढ़ (प्रयागराज जिला)</strong> विंध्य बलुआ पत्थर (कैमूर श्रृंखला) के अपक्षय से निर्मित उच्च शुद्धता वाली कांच बालू का उत्पादन करते हैं।
          <br>&bull; <em>अन्य क्षेत्र:</em> बरगढ़ (बांदा), राजापुर व मानिकपुर (चित्रकूट), तथा गंगा-यमुना नदी तटीय बालू।
          <br>&bull; <em>उपभोक्ता उद्योग:</em> फिरोजाबाद कांच एवं चूड़ी क्लस्टर, नैनी (प्रयागराज) ग्लास कंटेनर उद्योग, और सोलर ग्लास इकाइयां।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Limestone (चूना पत्थर):</strong>
          <br>&bull; <em>Districts:</em> <strong>Sonbhadra</strong> (Gurma, Kanach, Bapuhari, Kajrahat) and <strong>Mirzapur</strong> (Rohtas formation).
          <br>&bull; <em>Grades:</em> Cement-grade and high-purity Flux-grade (Kajrahat belt).
          <br>&bull; <em>Cement Plants:</em> Supplies raw material to major cement factories at <strong>Churk</strong>, <strong>Dalla</strong> (Sonbhadra), and <strong>Chunar</strong> (Mirzapur).</span>
        <span class="lang-hi"><strong>चूना पत्थर:</strong>
          <br>&bull; <em>जिले:</em> <strong>सोनभद्र</strong> (गुरमा, कनाच, बापुहारी, कजराहट) तथा <strong>मिर्जापुर</strong> (रोहतास शैल समूह)।
          <br>&bull; <em>श्रेणियां:</em> सीमेंट ग्रेड तथा उच्च शुद्धता वाला फ्लक्स-ग्रेड (कजराहट बेल्ट)।
          <br>&bull; <em>सीमेंट उद्योग:</em> <strong>चुर्क</strong>, <strong>डाला</strong> (सोनभद्र), और <strong>चुनार</strong> (मिर्जापुर) के प्रमुख सीमेंट संयंत्रों को कच्चा माल उपलब्ध कराता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Dolomite (डोलोमाइट - CaMg(CO3)2):</strong> Found in high concentration in the <strong>Kajrahat area of Sonbhadra district</strong> and parts of Banda; essential refractory flux material used in blast furnaces of SAIL (Bokaro, Rourkela) iron and steel plants.</span>
        <span class="lang-hi"><strong>डोलोमाइट:</strong> <strong>सोनभद्र जिले के कजराहट क्षेत्र</strong> और बांदा के कुछ हिस्सों में उच्च सांद्रता; सेल (SAIL - बोकारो, राउरकेला) के इस्पात संयंत्रों की ब्लास्ट फर्नेस में फ्लक्स के रूप में अनिवार्य रूप से प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Rock Phosphate / Phosphorite (रॉक फास्फेट):</strong> Deposits located in <strong>Lalitpur district</strong> (Pisnari, Tori) and <strong>Banda</strong>; primary raw material for manufacturing Single Super Phosphate (SSP) fertilizers and soil acidity amendment.</span>
        <span class="lang-hi"><strong>रॉक फास्फेट:</strong> <strong>ललितपुर जिले</strong> (पिसनारी, तोरी) तथा <strong>बांदा</strong> में निक्षेप; सिंगल सुपर फास्फेट (SSP) रासायनिक उर्वरक निर्माण तथा अम्लीय मृदा सुधार हेतु मुख्य कच्चा माल।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Specialty, Refractory & Ceramic Minerals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Specialty, Ceramic &amp; Refractory Minerals: Diaspore, Pyrophyllite, Clays &amp; Gypsum</span>
    <span class="lang-hi">5. विशिष्ट, सिरेमिक एवं रिफ्रैक्टरी खनिज: डायस्पोर, पायरोफिलाइट, क्ले एवं जिप्सम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Diaspore (डायस्पोर - AlO(OH)):</strong> UP is the <strong>Rank 1 producer and reserve holder in India</strong>; co-occurs with pyrophyllite in <strong>Jhansi, Lalitpur, Hamirpur, and Mahoba</strong>; used for high-alumina refractory bricks, spark plug ceramics, and abrasive tools.</span>
        <span class="lang-hi"><strong>डायस्पोर:</strong> उत्तर प्रदेश भारत में डायस्पोर उत्पादन एवं भंडार में <strong>प्रथम स्थान</strong> पर है; यह पायरोफिलाइट के साथ <strong>झांसी, ललितपुर, हमीरपुर और महोबा</strong> में पाया जाता है; उच्च-एल्युमिना रिफ्रैक्टरी ईंटों, स्पार्क प्लग सिरेमिक्स और अपघर्षक उपकरणों में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Pyrophyllite (पायरोफिलाइट):</strong> Major deposits in <strong>Hamirpur (Gorahari belt)</strong>, <strong>Jhansi</strong>, <strong>Lalitpur</strong>, and <strong>Mahoba</strong>; used as high-temperature refractory, pesticide carrier, ceramic glaze, paper coating filler, and cosmetics base.</span>
        <span class="lang-hi"><strong>पायरोफिलाइट:</strong> प्रमुख भंडार <strong>हमीरपुर (गोरहारी क्षेत्र)</strong>, <strong>झांसी</strong>, <strong>ललितपुर</strong>, तथा <strong>महोबा</strong> में; उच्च तापमान रिफ्रैक्टरी, कीटनाशक वाहक, सिरेमिक ग्लेज़, पेपर कोटिंग फिलर एवं सौंदर्य प्रसाधनों में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Fire Clay (फायर क्ले / अग्निसह मिट्टी):</strong> Highly refractory aluminosilicate clay found in <strong>Bansi (Mirzapur)</strong> and <strong>Makrikhoh (Sonbhadra)</strong>; withstands temperatures up to 1600&deg;C; used in blast furnace lining, kilns, and glass crucibles.</span>
        <span class="lang-hi"><strong>फायर क्ले (अग्निसह मिट्टी):</strong> <strong>बांसी (मिर्जापुर)</strong> और <strong>मकरीखोह (सोनभद्र)</strong> में पाई जाने वाली उच्च रिफ्रैक्टरी एल्युमिनोसिलिकेट मिट्टी; 1600&deg;C तक तापमान सहन करने में सक्षम; भट्ठी की आंतरिक परत, ईंट-भट्ठों और कांच की क्रूसिबल में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>China Clay / Kaolin (चाइना क्ले):</strong> Found in <strong>Sonbhadra</strong> and <strong>Banda</strong> districts; provides plastic clay for Khurja pottery, electrical porcelain insulators, and sanitaryware.</span>
        <span class="lang-hi"><strong>चाइना क्ले (केओलिन):</strong> <strong>सोनभद्र</strong> और <strong>बांदा</strong> जिलों में पाया जाता है; खुर्जा पॉटरी, विद्युत पोर्सिलेन इंसुलेटर तथा सेनेटरीवेयर उद्योग हेतु प्लास्टिक क्ले प्रदान करता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Andalusite &amp; Sillimanite:</strong> High-alumina refractory mineral occurrences found in <strong>Sonbhadra (Wyndhamganj area)</strong> and <strong>Mirzapur</strong>.</span>
        <span class="lang-hi"><strong>एन्डालुसाइट एवं सिलीमेनाइट:</strong> उच्च-एल्युमिना रिफ्रैक्टरी खनिज, जो <strong>सोनभद्र (विंढमगंज क्षेत्र)</strong> तथा <strong>मिर्जापुर</strong> में पाए जाते हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Gypsum (जिप्सम - CaSO4.2H2O):</strong> Found in <strong>Jhansi</strong> and <strong>Hamirpur</strong> districts; essential retarder in Portland cement and soil conditioner for reclaiming alkaline (Usar/Reh) soils.</span>
        <span class="lang-hi"><strong>जिप्सम:</strong> <strong>झांसी</strong> और <strong>हमीरपुर</strong> जिलों में पाया जाता है; पोर्टलैंड सीमेंट के जमने की दर नियंत्रित करने (रिटार्डर) तथा क्षारीय/ऊसर भूमि सुधार हेतु अनिवार्य।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Asbestos (एस्बेस्टस):</strong> Occurs in fibrous form in <strong>Mirzapur</strong> and <strong>Jhansi</strong>; used in fireproof fabrics, brake linings, and cement corrugated roofing sheets.</span>
        <span class="lang-hi"><strong>एस्बेस्टस:</strong> रेशेदार रूप में <strong>मिर्जापुर</strong> और <strong>झांसी</strong> में पाया जाता है; अग्निरोधक वस्त्रों, ब्रेक लाइनिंग और सीमेंट की नालीदार छतों के निर्माण में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Ochre / Geru (गेरू):</strong> Red and yellow ochre mined in <strong>Banda district</strong>; traditional natural mineral pigment used in indigenous paints, distempers, and cotton dyeing.</span>
        <span class="lang-hi"><strong>गेरू (ओकर):</strong> लाल और पीला गेरू <strong>बांदा जिले</strong> में खनन किया जाता है; स्वदेशी रंगों, डिस्टेंपर और सूती वस्त्रों की रंगाई में उपयोग होने वाला पारंपरिक प्राकृतिक खनिज वर्णक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Diamond Traces (हीरा):</strong> Minor alluvial and conglomerate occurrences reported in <strong>Banda district</strong> (geological extension of the Panna diamondiferous belt) and parts of <strong>Mirzapur</strong> (Jungle-khas).</span>
        <span class="lang-hi"><strong>हीरा:</strong> <strong>बांदा जिले</strong> (पन्ना हीरा पट्टी का भूगर्भीय विस्तार) तथा <strong>मिर्जापुर</strong> के कुछ हिस्सों (जंगल-खास) में कंकड़-पत्थर निक्षेपों में हीरे के अल्प संकेत मिले हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Building Stones, Dimensional Stones & Minor Minerals -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Building Stones, Dimensional Stones &amp; Minor Minerals</span>
    <span class="lang-hi">6. इमारती पत्थर, सजावटी पत्थर एवं उपखनिज संसाधन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Chunar Sandstone (चुनार बलुआ पत्थर - Mirzapur):</strong> Fine-grained, buff-and-pink Vindhyan sandstone quarried since antiquity; used in Mauryan polished pillars (Ashokan Lion Capital at Sarnath, now National Emblem), Sarnath Stupa, Barabar caves, and modern Varanasi ghats.</span>
        <span class="lang-hi"><strong>चुनार बलुआ पत्थर (मिर्जापुर):</strong> प्राचीन काल से उत्खनित सूक्ष्म कणों वाला गुलाबी एवं बादामी विंध्य बलुआ पत्थर; मौर्यकालीन पॉलिश किए गए स्तंभों (सारनाथ का सिंह शीर्ष - भारत का राष्ट्रीय प्रतीक), सारनाथ स्तूप, बराबर गुफाओं और आधुनिक वाराणसी के घाटों में प्रयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Red Sandstone (लाल बलुआ पत्थर - Agra/Fatehpur Sikri):</strong> Quarried along Rajasthan-UP border tracts; historic stone used in Agra Fort, Fatehpur Sikri, and Jama Masjid.</span>
        <span class="lang-hi"><strong>लाल बलुआ पत्थर (आगरा/फतेहपुर सीकरी):</strong> राजस्थान-यूपी सीमांत क्षेत्रों से प्राप्त; आगरा का किला, फतेहपुर सीकरी और जामा मस्जिद के निर्माण में प्रयुक्त ऐतिहासिक पत्थर।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Bundelkhand Granite (बुंदेलखंड ग्रेनाइट):</strong> High-strength pink and grey granite quarried extensively in <strong>Lalitpur, Jhansi, Mahoba, Banda, and Hamirpur</strong>; processed in modern stone-cutting and polishing units for commercial flooring and monuments.</span>
        <span class="lang-hi"><strong>बुंदेलखंड ग्रेनाइट:</strong> उच्च शक्ति वाला गुलाबी और धूसर ग्रेनाइट <strong>ललितपुर, झांसी, महोबा, बांदा और हमीरपुर</strong> में बड़े पैमाने पर उत्खनित; फर्श टाइल्स और स्मारकों हेतु आधुनिक कटिंग एवं पॉलिशिंग इकाइयों में प्रसंस्कृत।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Marble (संगमरमर):</strong> Crystalline, variegated and calcitic marble occurrences found in <strong>Mirzapur and Sonbhadra</strong> districts.</span>
        <span class="lang-hi"><strong>संगमरमर:</strong> रवेदार, बहुरंगी एवं कैल्साइट युक्त संगमरमर <strong>मिर्जापुर और सोनभद्र</strong> जिलों में पाया जाता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Riverbed Morrum, Sand &amp; Bajri (मौरंग, बालू व बजरी):</strong> Heavy mining across riverbeds of <strong>Ken, Betwa, Yamuna, Chambal, and Dhasan</strong> in Banda, Hamirpur, Jalaun, and Fatehpur; principal aggregate material driving UP's infrastructure and real estate sectors.</span>
        <span class="lang-hi"><strong>नदीय मौरंग, बालू एवं बजरी:</strong> बांदा, हमीरपुर, जालौन और फतेहपुर में <strong>केन, बेतवा, यमुना, चंबल और धसान</strong> नदियों के तलहटी से भारी खनन; यूपी के निर्माण और रियल एस्टेट क्षेत्र की रीढ़।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Kankar Nodules (कंकड़):</strong> Calcareous nodules formed in the subsoil of old alluvial (Bhangar) tracts; widely utilized for rural road sub-base metalling and traditional lime kilns.</span>
        <span class="lang-hi"><strong>कंकड़ ग्रंथियां:</strong> पुरानी जलोढ़ (बांगर) भूमि की उपमृदा में बनने वाली चूनेदार गांठें; ग्रामीण सड़कों की सोलिंग और पारंपरिक चूना भट्टियों में व्यापक उपयोग।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master District-wise Mineral Directory -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master District-wise Mineral Directory of Uttar Pradesh</span>
    <span class="lang-hi">7. उत्तर प्रदेश की जिलावार खनिज संसाधन महा-तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">District</span>
            <span class="lang-hi">जिला</span>
          </th>
          <th>
            <span class="lang-en">Major &amp; Minor Minerals Found</span>
            <span class="lang-hi">पाए जाने वाले प्रमुख एवं उपखनिज</span>
          </th>
          <th>
            <span class="lang-en">Key Mining Belts &amp; Industrial Signatures</span>
            <span class="lang-hi">प्रमुख खनन क्षेत्र एवं औद्योगिक पहचान</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en"><strong>Sonbhadra</strong></span>
            <span class="lang-hi"><strong>सोनभद्र</strong></span>
          </td>
          <td>
            <span class="lang-en">Coal, Limestone, Dolomite, Gold, China Clay, Fire Clay, Andalusite, Marble, Calcite</span>
            <span class="lang-hi">कोयला, चूना पत्थर, डोलोमाइट, स्वर्ण, चाइना क्ले, फायर क्ले, एन्डालुसाइट, संगमरमर, कैल्साइट</span>
          </td>
          <td>
            <span class="lang-en">Singrauli Coalfields (Kota, Bina); Son Pahadi &amp; Hardi (Gold); Kajrahat (Flux Dolomite); Gurma/Kanach (Cement Limestone); Churk &amp; Dalla plants</span>
            <span class="lang-hi">सिंगरौली कोयला क्षेत्र (कोटा, बीना); सोन पहाड़ी व हरदी (स्वर्ण); कजराहट (फ्लक्स डोलोमाइट); गुरमा/कनाच (सीमेंट चूना पत्थर); चुर्क व डाला संयंत्र</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Lalitpur</strong></span>
            <span class="lang-hi"><strong>ललितपुर</strong></span>
          </td>
          <td>
            <span class="lang-en">Uranium, Copper, Rock Phosphate, Diaspore, Pyrophyllite, Iron Ore, Bauxite, Pink Granite, Platinum traces</span>
            <span class="lang-hi">यूरेनियम, तांबा, रॉक फास्फेट, डायस्पोर, पायरोफिलाइट, लौह अयस्क, बॉक्साइट, गुलाबी ग्रेनाइट, प्लेटिनम संकेत</span>
          </td>
          <td>
            <span class="lang-en">Sonrai (Copper &amp; Uranium); Pisnari &amp; Tori (Rock Phosphate); Solda (Iron Ore); Highest diversity of metallic/strategic minerals</span>
            <span class="lang-hi">सोनराई (तांबा व यूरेनियम); पिसनारी व तोरी (रॉक फास्फेट); सोल्डा (लौह अयस्क); धात्विक एवं रणनीतिक खनिजों की सर्वाधिक विविधता</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Prayagraj</strong></span>
            <span class="lang-hi"><strong>प्रयागराज</strong></span>
          </td>
          <td>
            <span class="lang-en">Silica Sand (Glass Sand), Ganga-Yamuna Riverbed Sand</span>
            <span class="lang-hi">सिलिका बालू (कांच बालू), गंगा-यमुना नदीय बालू</span>
          </td>
          <td>
            <span class="lang-en">Shankargarh, Jasra, Lohgarh (Vindhyan Kaimur series); Supplies Firozabad bangles and Naini glass factories; UP Rank 2 nationally</span>
            <span class="lang-hi">शंकरगढ़, जसरा, लोहगढ़ (विंध्य कैमूर श्रृंखला); फिरोजाबाद चूड़ी व नैनी ग्लास उद्योग को आपूर्ति; राष्ट्रीय स्तर पर द्वितीय स्थान</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Mirzapur</strong></span>
            <span class="lang-hi"><strong>मिर्जापुर</strong></span>
          </td>
          <td>
            <span class="lang-en">Sandstone (Chunar stone), Limestone, Fire Clay, Calcite, Asbestos, Marble, Diamond traces</span>
            <span class="lang-hi">बलुआ पत्थर (चुनार स्टोन), चूना पत्थर, फायर क्ले, कैल्साइट, एस्बेस्टस, संगमरमर, हीरा संकेत</span>
          </td>
          <td>
            <span class="lang-en">Chunar (Historic Ashokan pillar sandstone); Rohtas Limestone; Bansi (Fire Clay); Jungle-khas (Diamond indicator); Chunar cement factory</span>
            <span class="lang-hi">चुनार (ऐतिहासिक मौर्य स्तंभ बलुआ पत्थर); रोहतास चूना पत्थर; बांसी (फायर क्ले); जंगल-खास (हीरा संकेत); चुनार सीमेंट संयंत्र</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Banda</strong></span>
            <span class="lang-hi"><strong>बांदा</strong></span>
          </td>
          <td>
            <span class="lang-en">Bauxite, Ochre (Geru), China Clay, Dolomite, Silica Sand, Diamond traces, Ken Morrum</span>
            <span class="lang-hi">बॉक्साइट, गेरू (ओकर), चाइना क्ले, डोलोमाइट, सिलिका बालू, हीरा संकेत, केन मौरंग</span>
          </td>
          <td>
            <span class="lang-en">Rajapur, Manikpur &amp; Karwi plateau (Bauxite for Hindalco); Bargarh (Silica sand); Panna border (Diamonds in conglomerate); Ken red morrum</span>
            <span class="lang-hi">राजापुर, मानिकपुर व कर्वी पठार (हिंडाल्को हेतु बॉक्साइट); बरगढ़ (सिलिका बालू); पन्ना सीमांत (कांग्लोमरेट में हीरा); केन नदी की लाल मौरंग</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Jhansi</strong></span>
            <span class="lang-hi"><strong>झांसी</strong></span>
          </td>
          <td>
            <span class="lang-en">Diaspore, Pyrophyllite, Gypsum, Granite, Asbestos, Feldspar</span>
            <span class="lang-hi">डायस्पोर, पायरोफिलाइट, जिप्सम, ग्रेनाइट, एस्बेस्टस, फेल्डस्पार</span>
          </td>
          <td>
            <span class="lang-en">Rank 1 in Diaspore/Pyrophyllite with Hamirpur; High-alumina spark plug refractory; Bundelkhand dimension granite</span>
            <span class="lang-hi">हमीरपुर के साथ डायस्पोर/पायरोफिलाइट में प्रथम स्थान; स्पार्क प्लग रिफ्रैक्टरी उद्योग; बुंदेलखंड सजावटी ग्रेनाइट</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Hamirpur</strong></span>
            <span class="lang-hi"><strong>हमीरपुर</strong></span>
          </td>
          <td>
            <span class="lang-en">Pyrophyllite, Diaspore, Gypsum, Betwa Red Morrum, Steatite (Soapstone)</span>
            <span class="lang-hi">पायरोफिलाइट, डायस्पोर, जिप्सम, बेतवा लाल मौरंग, सेलखड़ी (सोपस्टोन)</span>
          </td>
          <td>
            <span class="lang-en">Gorahari belt (Pyrophyllite extraction); Highest quality construction morrum from Betwa riverbeds</span>
            <span class="lang-hi">गोरहारी पट्टी (पायरोफिलाइट उत्खनन); बेतवा नदी से सर्वोत्तम गुणवत्ता वाली निर्माण मौरंग</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Mahoba</strong></span>
            <span class="lang-hi"><strong>महोबा</strong></span>
          </td>
          <td>
            <span class="lang-en">Diaspore, Pyrophyllite, Granite Gittie (Crushed Aggregate), Building Stone</span>
            <span class="lang-hi">डायस्पोर, पायरोफिलाइट, ग्रेनाइट गिट्टी, इमारती पत्थर</span>
          </td>
          <td>
            <span class="lang-en">Major stone crushing and dimensional granite hub for road/railway ballast in Central UP</span>
            <span class="lang-hi">मध्य यूपी में सड़क व रेलवे गिट्टी (बैलास्ट) हेतु विशाल स्टोन क्रशिंग व ग्रेनाइट हब</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Chitrakoot</strong></span>
            <span class="lang-hi"><strong>चित्रकूट</strong></span>
          </td>
          <td>
            <span class="lang-en">Silica Sand, Bauxite, Ochre, Limestone</span>
            <span class="lang-hi">सिलिका बालू, बॉक्साइट, गेरू, चूना पत्थर</span>
          </td>
          <td>
            <span class="lang-en">Rajapur &amp; Manikpur (Silica sand and lateritic bauxite)</span>
            <span class="lang-hi">राजापुर एवं मानिकपुर (सिलिका बालू एवं लेटराइट बॉक्साइट)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Chandauli</strong></span>
            <span class="lang-hi"><strong>चंदौली</strong></span>
          </td>
          <td>
            <span class="lang-en">Bauxite, Sandstone, Building Stone</span>
            <span class="lang-hi">बॉक्साइट, बलुआ पत्थर, इमारती पत्थर</span>
          </td>
          <td>
            <span class="lang-en">Chakia &amp; Naugarh ranges (Bauxite laterite caps and sandstone quarries)</span>
            <span class="lang-hi">चकिया एवं नौगढ़ श्रृंखलाएं (बॉक्साइट लेटराइट और बलुआ पत्थर खदानें)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en"><strong>Saharanpur</strong></span>
            <span class="lang-hi"><strong>सहारनपुर</strong></span>
          </td>
          <td>
            <span class="lang-en">Riverbed Boulder, Shingle, Bajri, Coarse Sand</span>
            <span class="lang-hi">नदीय बोल्डर, बजरी, रोड़ी, मोटी रेत</span>
          </td>
          <td>
            <span class="lang-en">Shivalik foothill rivers (Yamuna, Solani, Hindon tributaries); Key building aggregate supplier for Western UP and NCR</span>
            <span class="lang-hi">शिवालिक तलहटी नदियां (यमुना, सोलानी, हिंडन सहायक नदियां); पश्चिमी यूपी व एनसीआर हेतु प्रमुख निर्माण सामग्री प्रदाता</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 9: Rapid Revision Matrix & UPSSSC Exam Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Rapid Revision Matrix: One-Liner Mineral Facts &amp; UPSSSC Exam Traps</span>
    <span class="lang-hi">8. त्वरित पुनरीक्षण सारणी: खनिज तथ्य एवं यूपीएसएसएससी परीक्षा ट्रैप</span>
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
            <span class="lang-en">High-Yield Fact / Correct Rule</span>
            <span class="lang-hi">उच्च अंकदायी तथ्य / सही नियम</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Only District with Coal</span>
            <span class="lang-hi">कोयले वाला एकमात्र जिला</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sonbhadra (Singrauli belt)</strong>; Rank 8th nationally; Gondwana formation. (Trap: Mirzapur does NOT produce coal).</span>
            <span class="lang-hi"><strong>सोनभद्र (सिंगरौली बेल्ट)</strong>; देश में 8वां स्थान; गोंडवाना शैल। (ट्रैप: मिर्जापुर में कोयला नहीं पाया जाता)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Only District with Uranium</span>
            <span class="lang-hi">यूरेनियम वाला एकमात्र जिला</span>
          </td>
          <td>
            <span class="lang-en"><strong>Lalitpur</strong>; occurs in Bijawar formations near Sonrai.</span>
            <span class="lang-hi"><strong>ललितपुर</strong>; सोनराई के निकट बिजावर शैल समूहों में सीमित भंडार।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Only District with Copper</span>
            <span class="lang-hi">तांबे वाला एकमात्र जिला</span>
          </td>
          <td>
            <span class="lang-en"><strong>Lalitpur (Sonrai area)</strong>; found in quartz veins and volcanic rocks.</span>
            <span class="lang-hi"><strong>ललितपुर (सोनराई क्षेत्र)</strong>; क्वार्ट्ज शिराओं एवं ज्वालामुखीय चट्टानों में।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">National Rank 1 Minerals</span>
            <span class="lang-hi">देश में प्रथम स्थान वाले खनिज</span>
          </td>
          <td>
            <span class="lang-en"><strong>Diaspore</strong> and <strong>Pyrophyllite</strong> (Jhansi, Lalitpur, Hamirpur, Mahoba).</span>
            <span class="lang-hi"><strong>डायस्पोर</strong> एवं <strong>पायरोफिलाइट</strong> (झांसी, ललितपुर, हमीरपुर, महोबा)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">National Rank 2 Mineral</span>
            <span class="lang-hi">देश में द्वितीय स्थान वाला खनिज</span>
          </td>
          <td>
            <span class="lang-en"><strong>Silica Sand (Glass Sand)</strong>; highest production centered in Shankargarh (Prayagraj).</span>
            <span class="lang-hi"><strong>सिलिका बालू (कांच बालू)</strong>; सर्वाधिक उत्पादन शंकरगढ़ (प्रयागराज) में केंद्रित।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Gold Exploration Sites</span>
            <span class="lang-hi">स्वर्ण अन्वेषण स्थल</span>
          </td>
          <td>
            <span class="lang-en"><strong>Son Pahadi</strong> and <strong>Hardi</strong> blocks in Sonbhadra; Placer gold in sands of <strong>Sharda &amp; Ramganga</strong> rivers.</span>
            <span class="lang-hi">सोनभद्र के <strong>सोन पहाड़ी</strong> एवं <strong>हरदी</strong> ब्लॉक; <strong>शारदा व रामगंगा</strong> नदियों के रेत में प्लेसर स्वर्ण।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chunar Sandstone Specialty</span>
            <span class="lang-hi">चुनार बलुआ पत्थर विशेषता</span>
          </td>
          <td>
            <span class="lang-en">Quarried in <strong>Mirzapur</strong>; used for Mauryan Ashokan pillars (Sarnath Lion Capital) and Varanasi river ghats.</span>
            <span class="lang-hi"><strong>मिर्जापुर</strong> में उत्खनित; मौर्यकालीन अशोक स्तंभों (सारनाथ सिंह शीर्ष) और वाराणसी घाटों में प्रयुक्त।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Limestone &amp; Cement Hubs</span>
            <span class="lang-hi">चूना पत्थर एवं सीमेंट हब</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sonbhadra</strong> (Gurma, Kanach, Kajrahat) and <strong>Mirzapur</strong>; feeds Churk, Dalla &amp; Chunar cement factories.</span>
            <span class="lang-hi"><strong>सोनभद्र</strong> (गुरमा, कनाच, कजराहट) व <strong>मिर्जापुर</strong>; चुर्क, डाला व चुनार सीमेंट संयंत्रों को कच्चा माल।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Mineral Policy Date</span>
            <span class="lang-hi">प्रथम खनिज नीति वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>December 1998</strong>; declared minerals as an 'Industry' and notified 12 mineral-rich districts.</span>
            <span class="lang-hi"><strong>दिसंबर 1998</strong>; खनिज विकास को 'उद्योग' का दर्जा दिया तथा 12 खनिज बाहुल्य जिले घोषित किए।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Directorate Establishment</span>
            <span class="lang-hi">निदेशालय स्थापना वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>1955</strong>, Directorate of Geology and Mining headquartered at <strong>Lucknow</strong>.</span>
            <span class="lang-hi"><strong>1955</strong>, भूतत्व एवं खनिकर्म निदेशालय, मुख्यालय <strong>लखनऊ</strong>।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "mines-and-minerals", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_mines_minerals_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
