import os
import re

def build_forests_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Forest Cover, Forest Types &amp; Forestry Resources of UP</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का वन आवरण, वन प्रकार एवं वानिकी संसाधन</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Forests of Uttar Pradesh] --> B[ISFR 2021 Forest Statistics]
    A --> C[District Forest Extremes]
    A --> D[Three Major Forest Types]
    A --> E[Forest Products & Industries]
    A --> F[Forest Policy & Historical Milestones]
    A --> G[State Natural Symbols]

    B --> B1[Total Forest Cover: 14,817.89 sq km 6.15%]
    B --> B2[Tree Cover: 7,421 sq km 3.08%]
    B --> B3[Combined Green Cover: 22,238.89 sq km 9.23%]
    B --> B4[Density: VDF 1.09%, MDF 1.67%, Open 3.39%]

    C --> C1[Max Area: Sonbhadra 2539 sq km | Kheri 1272 sq km]
    C --> C2[Max Percent: Sonbhadra 36.79% | Chandauli 22.25%]
    C --> C3[Min Area: Bhadohi 3.71 sq km | Mau 11 sq km]
    C --> C4[Min Percent: Bhadohi 0.37% | Mainpuri 0.49%]

    D --> D1[Moist Deciduous: Terai-Bhabar | Sal, Teak, Semal]
    D --> D2[Dry Deciduous: Plains | Sal, Palash, Neem, Mahua]
    D --> D3[Thorn Forests: Bundelkhand & SW | Babul, Khair, Ber]

    E --> E1[Tendu Leaves: Bidi Industry Bundelkhand & Mirzapur]
    E --> E2[Kattha: Khair Tree Bareilly & Gonda]
    E --> E3[Resin & Turpentine Bareilly | Matchbox Bareilly]
    E --> E4[Wood Carving: Saharanpur GI & Nagina Bijnor]

    F --> F1[Forest Dept: 1855 | Forest Corporation: 1974]
    F --> F2[Social Forestry 1976 World Bank | Operation Green 2001]
    F --> F3[State Forest Policy 1998 | Target 15% Green Cover]

    G --> G1[State Tree: Ashok | State Flower: Palash 2011]
    G --> G2[State Bird: Sarus Crane | State Animal: Barasingha]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के वन संसाधन] --> B[ISFR 2021 वन स्थिति आंकड़े]
    A --> C[जिलों में वन आवरण के चरम आंकड़े]
    A --> D[तीन मुख्य प्राकृतिक वन प्रकार]
    A --> E[वन उत्पाद एवं वन-आधारित उद्योग]
    A --> F[वन नीति एवं ऐतिहासिक संस्थाएं]
    A --> G[राज्य के राजकीय प्राकृतिक प्रतीक]

    B --> B1[कुल वन आवरण: 14,817.89 वर्ग किमी 6.15%]
    B --> B2[कुल वृक्ष आवरण: 7,421 वर्ग किमी 3.08%]
    B --> B3[कुल हरित आवरण: 22,238.89 वर्ग किमी 9.23%]
    B --> B4[घनत्व: अति सघन 1.09%, मध्यम 1.67%, खुला 3.39%]

    C --> C1[सर्वाधिक क्षेत्रफल: सोनभद्र 2539 वर्ग किमी | खीरी 1272]
    C --> C2[सर्वाधिक प्रतिशत: सोनभद्र 36.79% | चंदौली 22.25%]
    C --> C3[न्यूनतम क्षेत्रफल: भदोही 3.71 वर्ग किमी | मऊ 11]
    C --> C4[न्यूनतम प्रतिशत: भदोही 0.37% | मैनपुरी 0.49%]

    D --> D1[उष्णकटिबंधीय नम पर्णपाती: तराई-भाबर | साल, सागौन, सेमल]
    D --> D2[उष्णकटिबंधीय शुष्क पर्णपाती: मैदान | साल, पलाश, महुआ]
    D --> D3[कंटीले वन: बुंदेलखंड व दक्षिण-पश्चिम | बबूल, खैर, बेर]

    E --> E1[तेंदू पत्ता: बीड़ी उद्योग बुंदेलखंड व मिर्जापुर]
    E --> E2[कत्था: खैर वृक्ष से निष्कर्षण बरेली व गोंडा]
    E --> E3[बिरोजा व तारपीन बरेली | दियासलाई बरेली]
    E --> E4[काष्ठ नक्काशी: सहारनपुर जीआई व नगीना बिजनौर]

    F --> F1[वन विभाग: 1855 | उ.प्र. वन निगम: 1974]
    F --> F2[सामाजिक वानिकी 1976 विश्व बैंक | ऑपरेशन ग्रीन 2001]
    F --> F3[राज्य वन नीति 1998 | 15% हरित आवरण लक्ष्य]

    G --> G1[राजकीय वृक्ष: अशोक | राजकीय पुष्प: पलाश 2011]
    G --> G2[राजकीय पक्षी: सारस (क्रौंच) | राजकीय पशु: बारहसिंगा]
    </div>
  </div>
</div>

<!-- Card 2: ISFR 2021 Definitive Forest Statistics -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Forest &amp; Tree Cover Statistics (ISFR 2021 Benchmark)</span>
    <span class="lang-hi">1. वन एवं वृक्ष आवरण सांख्यिकी (ISFR 2021 आधिकारिक आंकड़े)</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Biennial Assessment:</strong> The India State of Forest Report (ISFR) is published biennially by the <strong>Forest Survey of India (FSI, Dehradun)</strong> under the Ministry of Environment, Forest and Climate Change. The 17th assessment (ISFR 2021) provides the definitive exam benchmarks.</span>
      <span class="lang-hi"><strong>द्विवार्षिक मूल्यांकन:</strong> <strong>भारतीय वन सर्वेक्षण (FSI, देहरादून)</strong> द्वारा प्रत्येक दो वर्ष में भारत वन स्थिति रिपोर्ट (ISFR) प्रकाशित की जाती है। 17वीं रिपोर्ट (ISFR 2021) परीक्षा हेतु आधिकारिक मानक है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Total Forest Cover (वनावरण):</strong> <strong>14,817.89 sq km</strong>, which is <strong>6.15% of the total geographical area</strong> of Uttar Pradesh (2,40,928 sq km).</span>
      <span class="lang-hi"><strong>कुल वन आवरण (वनावरण):</strong> <strong>14,817.89 वर्ग किमी</strong>, जो उ.प्र. के कुल भौगोलिक क्षेत्रफल (2,40,928 वर्ग किमी) का <strong>6.15%</strong> है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Canopy Density Breakdown:</strong>
        <br/>• <strong>Very Dense Forest (VDF - अति सघन वन):</strong> Canopy density &gt;70% = <strong>2,626.65 sq km (1.09%)</strong>.
        <br/>• <strong>Moderately Dense Forest (MDF - मध्यम सघन वन):</strong> Canopy density 40% to 70% = <strong>4,029.37 sq km (1.67%)</strong>.
        <br/>• <strong>Open Forest (OF - खुला वन):</strong> Canopy density 10% to 40% = <strong>8,161.87 sq km (3.39%)</strong>.
        <br/>• <strong>Scrub (झाड़ियां):</strong> Canopy density &lt;10% = <strong>563.38 sq km (0.23%)</strong> (non-forest category).
      </span>
      <span class="lang-hi"><strong>छत्र घनत्व के आधार पर वर्गीकरण:</strong>
        <br/>• <strong>अति सघन वन (VDF):</strong> 70% से अधिक घनत्व = <strong>2,626.65 वर्ग किमी (1.09%)</strong>।
        <br/>• <strong>मध्यम सघन वन (MDF):</strong> 40% से 70% घनत्व = <strong>4,029.37 वर्ग किमी (1.67%)</strong>।
        <br/>• <strong>खुला वन (OF):</strong> 10% से 40% घनत्व = <strong>8,161.87 वर्ग किमी (3.39%)</strong>।
        <br/>• <strong>झाड़ियां (Scrub):</strong> 10% से कम घनत्व = <strong>563.38 वर्ग किमी (0.23%)</strong>।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Tree Cover (वृक्षावरण):</strong> <strong>7,421 sq km</strong>, constituting <strong>3.08% of total geographical area</strong> (recorded patches &lt;1 hectare outside recorded forest area).</span>
      <span class="lang-hi"><strong>वृक्ष आवरण (वृक्षावरण):</strong> <strong>7,421 वर्ग किमी</strong>, जो राज्य के कुल भौगोलिक क्षेत्रफल का <strong>3.08%</strong> है (1 हेक्टेयर से छोटे वृक्ष समूह)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Total Green Cover (वनावरण + वृक्षावरण):</strong> <strong>22,238.89 sq km</strong>, which equals <strong>9.23% of UP's total geographical area</strong>.</span>
      <span class="lang-hi"><strong>कुल हरित आवरण (वनावरण + वृक्षावरण):</strong> <strong>22,238.89 वर्ग किमी</strong>, जो राज्य के कुल भौगोलिक क्षेत्रफल का <strong>9.23%</strong> है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Net Change over ISFR 2019:</strong> Total forest cover increased by <strong>12.24 sq km</strong>. Highest increase was registered in <strong>Saharanpur district (+49.92 sq km)</strong>, while Chitrakoot district recorded the highest loss (-4.81 sq km).</span>
      <span class="lang-hi"><strong>ISFR 2019 की तुलना में परिवर्तन:</strong> राज्य के वनावरण में <strong>12.24 वर्ग किमी की शुद्ध वृद्धि</strong> हुई। सर्वाधिक वृद्धि <strong>सहारनपुर जिले (+49.92 वर्ग किमी)</strong> में दर्ज की गई, जबकि सर्वाधिक कमी चित्रकूट जिले (-4.81 वर्ग किमी) में हुई।</span>
    </li>
  </ul>
</div>

<!-- Card 3: District Rankings by Forest Cover -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. District-Wise Forest Cover Rankings (Area &amp; Percentage Extremes)</span>
    <span class="lang-hi">2. जिला-वार वन आवरण रैंकिंग (क्षेत्रफल एवं प्रतिशत चरम आंकड़े)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Category / Ranking</span><span class="lang-hi">श्रेणी / रैंकिंग</span></th>
          <th><span class="lang-en">Top Districts (Highest)</span><span class="lang-hi">शीर्ष जिले (सर्वाधिक वन)</span></th>
          <th><span class="lang-en">Bottom Districts (Lowest)</span><span class="lang-hi">न्यूनतम जिले (सबसे कम वन)</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en"><strong>Area-Wise Forest Cover (क्षेत्रफल के आधार पर)</strong></span><span class="lang-hi"><strong>क्षेत्रफल के आधार पर वन आवरण</strong></span></td>
          <td>
            <span class="lang-en">
              1. <strong>Sonbhadra:</strong> 2,539.25 sq km<br/>
              2. <strong>Lakhimpur Kheri:</strong> 1,272.56 sq km<br/>
              3. <strong>Mirzapur:</strong> 803.73 sq km<br/>
              4. <strong>Pilibhit:</strong> 687.11 sq km<br/>
              5. <strong>Chitrakoot:</strong> 631.13 sq km
            </span>
            <span class="lang-hi">
              1. <strong>सोनभद्र:</strong> 2,539.25 वर्ग किमी<br/>
              2. <strong>लखीमपुर खीरी:</strong> 1,272.56 वर्ग किमी<br/>
              3. <strong>मिर्जापुर:</strong> 803.73 वर्ग किमी<br/>
              4. <strong>पीलीभीत:</strong> 687.11 वर्ग किमी<br/>
              5. <strong>चित्रकूट:</strong> 631.13 वर्ग किमी
            </span>
          </td>
          <td>
            <span class="lang-en">
              1. <strong>Bhadohi (Sant Ravidas Nagar):</strong> 3.71 sq km (Lowest)<br/>
              2. <strong>Mau:</strong> 11.00 sq km<br/>
              3. <strong>Mainpuri:</strong> 13.64 sq km<br/>
              4. <strong>Sant Kabir Nagar:</strong> 14.28 sq km<br/>
              5. <strong>Deoria:</strong> 15.21 sq km
            </span>
            <span class="lang-hi">
              1. <strong>भदोही (संत रविदास नगर):</strong> 3.71 वर्ग किमी (न्यूनतम)<br/>
              2. <strong>मऊ:</strong> 11.00 वर्ग किमी<br/>
              3. <strong>मैनपुरी:</strong> 13.64 वर्ग किमी<br/>
              4. <strong>संत कबीर नगर:</strong> 14.28 वर्ग किमी<br/>
              5. <strong>देवरिया:</strong> 15.21 वर्ग किमी
            </span>
          </td>
        </tr>
        <tr>
          <td><span class="lang-en"><strong>Percentage-Wise Forest Cover (प्रतिशत के आधार पर)</strong></span><span class="lang-hi"><strong>प्रतिशत के आधार पर वन आवरण</strong></span></td>
          <td>
            <span class="lang-en">
              1. <strong>Sonbhadra:</strong> 36.79% (Highest)<br/>
              2. <strong>Chandauli:</strong> 22.25%<br/>
              3. <strong>Chitrakoot:</strong> 19.64%<br/>
              4. <strong>Pilibhit:</strong> 18.60%<br/>
              5. <strong>Mirzapur:</strong> 18.25%
            </span>
            <span class="lang-hi">
              1. <strong>सोनभद्र:</strong> 36.79% (सर्वाधिक)<br/>
              2. <strong>चंदौली:</strong> 22.25%<br/>
              3. <strong>चित्रकूट:</strong> 19.64%<br/>
              4. <strong>पीलीभीत:</strong> 18.60%<br/>
              5. <strong>मिर्जापुर:</strong> 18.25%
            </span>
          </td>
          <td>
            <span class="lang-en">
              1. <strong>Bhadohi (Sant Ravidas Nagar):</strong> 0.37% (Lowest in state)<br/>
              2. <strong>Mainpuri:</strong> 0.49%<br/>
              3. <strong>Deoria:</strong> 0.60%<br/>
              4. <strong>Badaun:</strong> 0.62%<br/>
              5. <strong>Mau:</strong> 0.64%
            </span>
            <span class="lang-hi">
              1. <strong>भदोही (संत रविदास नगर):</strong> 0.37% (राज्य में सबसे कम)<br/>
              2. <strong>मैनपुरी:</strong> 0.49%<br/>
              3. <strong>देवरिया:</strong> 0.60%<br/>
              4. <strong>बदायूं:</strong> 0.62%<br/>
              5. <strong>मऊ:</strong> 0.64%
            </span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 4: Three Major Forest Types of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Ecological Classification: Three Natural Forest Types of UP</span>
    <span class="lang-hi">3. पारिस्थितिक वर्गीकरण: उत्तर प्रदेश के तीन मुख्य प्राकृतिक वन प्रकार</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>1. Tropical Moist Deciduous Forests (उष्णकटिबंधीय नम पर्णपाती वन):</strong>
        <br/>• <strong>Rainfall Regime:</strong> 100 cm to 150 cm annual precipitation.
        <br/>• <strong>Geographical Tract:</strong> Bhabhar and Terai belt in northern UP (Pilibhit, Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, Siddharthnagar, Maharajganj, Kushinagar).
        <br/>• <strong>Dominant Tree Flora:</strong> <strong>Sal (Shorea robusta - dominant timber)</strong>, Teak (सागौन), Semal, Mahua, Shisham, Haldu, Bahera, Jamun, Aonla, Dhak, and tall reed grasses (Elephant grass, Kans, Munj).
        <br/>• <strong>Ecology:</strong> Dense multi-storey canopy; trees shed leaves for a brief 6-8 week spell in spring.
      </span>
      <span class="lang-hi"><strong>1. उष्णकटिबंधीय नम पर्णपाती वन:</strong>
        <br/>• <strong>वार्षिक वर्षा:</strong> 100 सेमी से 150 सेमी।
        <br/>• <strong>भौगोलिक विस्तार:</strong> भाबर एवं तराई पट्टी (पीलीभीत, लखीमपुर खीरी, बहराइच, श्रावस्ती, बलरामपुर, सिद्धार्थनगर, महराजगंज, कुशीनगर)।
        <br/>• <strong>प्रमुख वनस्पति:</strong> <strong>साल (साखू - प्रमुख प्रकाष्ठ)</strong>, सागौन, सेमल, महुआ, शीशम, हल्दू, बहेड़ा, जामुन, आंवला, ढाक तथा विशाल घासें (हाथी घास, कांस, मूंज)।
        <br/>• <strong>पारिस्थितिकी:</strong> घने बहुस्तरीय वन; वसंत ऋतु में 6-8 सप्ताह के लिए पत्तियां गिराते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>2. Tropical Dry Deciduous Forests (उष्णकटिबंधीय शुष्क पर्णपाती वन):</strong>
        <br/>• <strong>Rainfall Regime:</strong> 50 cm to 100 cm annual precipitation.
        <br/>• <strong>Geographical Tract:</strong> Covers the largest land area across UP; extensive in the Central, Eastern, and Western Gangetic plains.
        <br/>• <strong>Dominant Tree Flora:</strong> Sal, <strong>Palash (Dhak / Tesu - Butea monosperma, State Flower)</strong>, Neem, Peepal, Banyan, Bel, Amaltas, Mahua, Khair, Shisham, and Tendu.
        <br/>• <strong>Ecology:</strong> Trees shed leaves for an extended 2-3 month period in early summer to curb transpirational water loss.
      </span>
      <span class="lang-hi"><strong>2. उष्णकटिबंधीय शुष्क पर्णपाती वन:</strong>
        <br/>• <strong>वार्षिक वर्षा:</strong> 50 सेमी से 100 सेमी।
        <br/>• <strong>भौगोलिक विस्तार:</strong> राज्य के सबसे बड़े मैदानी भाग पर विस्तृत; मध्य, पूर्वी एवं पश्चिमी गंगा के मैदान।
        <br/>• <strong>प्रमुख वनस्पति:</strong> साल, <strong>पलाश (ढाक / टेसू - राजकीय पुष्प)</strong>, नीम, पीपल, बरगद, बेल, अमलतास, महुआ, खैर, शीशम तथा तेंदू।
        <br/>• <strong>पारिस्थितिकी:</strong> जल संरक्षण हेतु ग्रीष्मकाल के प्रारंभ में 2-3 माह के लिए पूर्णतः पर्णपाती हो जाते हैं।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>3. Tropical Thorn Forests (उष्णकटिबंधीय कंटीले वन):</strong>
        <br/>• <strong>Rainfall Regime:</strong> Less than 50 cm to 70 cm annual precipitation.
        <br/>• <strong>Geographical Tract:</strong> Semi-arid South-Western UP (Agra, Mathura, Firozabad) and the Bundelkhand plateau (Jhansi, Lalitpur, Banda, Hamirpur, Jalaun).
        <br/>• <strong>Dominant Tree Flora:</strong> <strong>Babul (Acacia nilotica)</strong>, Kikar, Khair, Thor, Date Palm (Khajur), Ber, Reunjha, and Neem.
        <br/>• <strong>Ecology:</strong> Xerophytic adaptations with deep taproots, stunted stature, small waxy leaves, and sharp thorns to prevent grazing and moisture loss.
      </span>
      <span class="lang-hi"><strong>3. उष्णकटिबंधीय कंटीले वन:</strong>
        <br/>• <strong>वार्षिक वर्षा:</strong> 50 सेमी से 70 सेमी से कम।
        <br/>• <strong>भौगोलिक विस्तार:</strong> दक्षिण-पश्चिमी अर्ध-शुष्क भाग (आगरा, मथुरा) तथा बुंदेलखंड पठार (झांसी, ललितपुर, बांदा, हमीरपुर, जालौन)।
        <br/>• <strong>प्रमुख वनस्पति:</strong> <strong>बबूल (अकेशिया)</strong>, कीकर, खैर, थोर (कैक्टस), खजूर, बेर, रौंझ तथा नीम।
        <br/>• <strong>पारिस्थितिकी:</strong> मरुद्भिद (Xerophytic) लक्षण; गहरी जड़ें, छोटी पत्तियां एवं नुकीले कांटे।
      </span>
    </li>
  </ul>
</div>

<!-- Card 5: Forest Products & Associated Industries -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Minor Forest Products (MFP) &amp; Forest-Based Industrial Hubs</span>
    <span class="lang-hi">4. लघु वन उत्पाद (MFP) एवं वन-आधारित प्रमुख औद्योगिक केंद्र</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Tendu Leaves (तेंदू पत्ता):</strong> Collected extensively in the forests of Bundelkhand (Jhansi, Lalitpur, Banda) and Mirzapur/Sonbhadra. Used as wrappers for the rural <strong>Bidi industry</strong>. Managed directly by the UP Forest Corporation.</span>
      <span class="lang-hi"><strong>तेंदू पत्ता:</strong> बुंदेलखंड (झांसी, ललितपुर, बांदा) तथा मिर्जापुर-सोनभद्र के वनों से भारी मात्रा में एकत्र; <strong>बीड़ी निर्माण उद्योग</strong> का मुख्य कच्चा माल। उ.प्र. वन निगम द्वारा विपणन।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Kattha (कत्था):</strong> Extracted by boiling the heartwood of the <strong>Khair tree (Acacia catechu)</strong>. Major processing factories located in <strong>Bareilly, Gonda, and Aligarh</strong>.</span>
      <span class="lang-hi"><strong>कत्था:</strong> <strong>खैर के वृक्ष (Acacia catechu)</strong> की लकड़ी को उबालकर निकाला जाता है। प्रमुख कारखाने <strong>बरेली, गोंडा एवं अलीगढ़</strong> में स्थित हैं।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Resin &amp; Turpentine Oil (बिरोजा एवं तारपीन का तेल):</strong> Extracted from Chir pine (चीड़) trees; <strong>Bareilly</strong> is the largest historic processing center in Uttar Pradesh.</span>
      <span class="lang-hi"><strong>बिरोजा एवं तारपीन का तेल:</strong> चीड़ के पेड़ों से प्राप्त लीसा (राल) से तैयार किया जाता है; <strong>बरेली</strong> इसका प्रमुख शोधन व विनिर्माण केंद्र है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Matchbox Industry (दियासलाई उद्योग):</strong> Uses Semal (Bombax ceiba) and Guttel softwoods. <strong>Bareilly is the primary matchbox manufacturing hub</strong> of UP, along with Saharanpur and Meerut.</span>
      <span class="lang-hi"><strong>दियासलाई (माचिस) उद्योग:</strong> सेमल व गुटेल की मुलायम लकड़ी का उपयोग; <strong>बरेली उ.प्र. का प्रमुख दियासलाई उद्योग केंद्र</strong> है (सहारनपुर व मेरठ में भी इकाइयां)।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Wood Carving (काष्ठ नक्काशी):</strong>
        <br/>• <strong>Saharanpur:</strong> World-famous for intricate Sheesham and Teak wood carvings and decorative screens (GI Tagged).
        <br/>• <strong>Nagina (Bijnor):</strong> Famous for exquisite ebony and rosewood carvings on combs, walking sticks, and boxes.
      </span>
      <span class="lang-hi"><strong>काष्ठ नक्काशी व शिल्प:</strong>
        <br/>• <strong>सहारनपुर:</strong> शीशम व सागौन की बारीक नक्काशी, जालीदार स्क्रीन व फर्नीचर हेतु विश्व विख्यात (GI टैग प्राप्त)।
        <br/>• <strong>नगीना (बिजनौर):</strong> आबनूस की लकड़ी पर सुंदर नक्काशीदार कंघी, छड़ी व कलात्मक डिब्बों हेतु प्रसिद्ध।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Cane &amp; Bamboo Furniture:</strong> Centered in <strong>Bareilly (famed as 'Bans-Bareilly')</strong> for cane handicrafts and bamboo furniture.</span>
      <span class="lang-hi"><strong>बेंत एवं बांस फर्नीचर:</strong> <strong>बरेली ('बांस-बरेली')</strong> बेंत की कुर्सियों व कलात्मक फर्नीचर निर्माण का ऐतिहासिक केंद्र है।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Paper &amp; Pulp Mills:</strong> Major paper mill located in <strong>Saharanpur (Star Paper Mills)</strong> utilizing eucalyptus, bamboo, and agricultural bagasse.</span>
      <span class="lang-hi"><strong>कागज एवं लुगदी उद्योग:</strong> <strong>सहारनपुर (स्टार पेपर मिल)</strong> यूकेलिप्टस, बांस व खोई पर आधारित प्रमुख कागज उत्पादक केंद्र।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Sports Goods (खेल का सामान):</strong> <strong>Meerut</strong> is the national capital for sports goods, crafting high-grade cricket bats from English and Kashmir willow (Salix) and hockey sticks from mulberry wood.</span>
      <span class="lang-hi"><strong>खेल का सामान:</strong> <strong>मेरठ</strong> खेल उपकरण निर्माण का राष्ट्रीय केंद्र है, जहाँ विलो (विलो वृक्ष) की लकड़ी से क्रिकेट बैट तथा शहतूत की लकड़ी से हॉकी स्टिक बनाई जाती हैं।</span>
    </li>
  </ul>
</div>

<!-- Card 6: Forest Policy, Institutions & State Symbols -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Forest Policies, Institutions &amp; State Natural Symbols</span>
    <span class="lang-hi">5. वन नीतियां, प्रमुख संस्थाएं एवं राजकीय प्राकृतिक प्रतीक</span>
  </div>
  <ul class="bullet-list">
    <li>
      <span class="lang-en"><strong>Institutional History:</strong>
        <br/>• <strong>UP Forest Department:</strong> Established in <strong>1855</strong>, ranking among the earliest organized forestry departments in British India.
        <br/>• <strong>Uttar Pradesh Forest Corporation (उ.प्र. वन निगम):</strong> Established on <strong>November 25, 1974</strong>, under the UP Forest Corporation Act, 1974, to systematize timber trade and eliminate exploitative middleman contractors.
      </span>
      <span class="lang-hi"><strong>संस्थागत इतिहास:</strong>
        <br/>• <strong>उ.प्र. वन विभाग:</strong> स्थापना <strong>1855 में</strong>; भारत के सबसे पुराने संगठित वन विभागों में से एक।
        <br/>• <strong>उत्तर प्रदेश वन निगम:</strong> स्थापना <strong>25 नवंबर 1974</strong> को उ.प्र. वन निगम अधिनियम 1974 के तहत; वनोपज के वैज्ञानिक दोहन व ठेकेदारों के शोषण को समाप्त करने हेतु।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>Social Forestry Scheme (सामाजिक वानिकी योजना, 1976):</strong>
        <br/>• Launched in 1976 with <strong>World Bank financial assistance</strong> to plant trees on panchayat lands, canal banks, roadsides, and railway tracks.
        <br/>• The term <em>'Social Forestry'</em> was first coined by Westoby (1968).
        <br/>• Widespread planting of <strong>Eucalyptus (सफेदा)</strong> occurred, though later criticized as an <em>'ecological terrorist'</em> for excessively depleting groundwater.
      </span>
      <span class="lang-hi"><strong>सामाजिक वानिकी योजना (1976):</strong>
        <br/>• <strong>विश्व बैंक की वित्तीय सहायता</strong> से 1976 में प्रारंभ; सड़कों, नहरों, रेल पटरियों व बंजर भूमि पर वृक्षारोपण।
        <br/>• 'सोशल फॉरेस्ट्री' शब्द सर्वप्रथम वेस्टोबी (1968) द्वारा प्रयुक्त।
        <br/>• इस योजना में बड़े पैमाने पर <strong>यूकेलिप्टस (सफेदा)</strong> लगाया गया, जिसे भूजल अत्यधिक सोखने के कारण बाद में <em>'पारिस्थितिक आतंकवादी'</em> कहा गया।
      </span>
    </li>
    <li>
      <span class="lang-en"><strong>State Forest Policy 1998:</strong> First dedicated state policy aiming to expand forest and tree cover to 15% by 2001 and 20% by 2011. Present target under Mission Green UP is achieving <strong>15% green cover by 2026-27</strong>.</span>
      <span class="lang-hi"><strong>राज्य वन नीति 1998:</strong> राज्य की प्रथम स्वतंत्र वन नीति; 2001 तक 15% व 2011 तक 20% वनाच्छादन का लक्ष्य। वर्तमान में मिशन ग्रीन उ.प्र. के तहत <strong>2026-27 तक 15% हरित आवरण</strong> का लक्ष्य।</span>
    </li>
    <li>
      <span class="lang-en"><strong>Official Natural Symbols of Uttar Pradesh:</strong>
        <br/>• <strong>State Tree:</strong> <strong>Ashok / Sita Ashok</strong> (<em>Saraca asoca</em>)
        <br/>• <strong>State Flower:</strong> <strong>Palash / Tesu / Dhak</strong> (<em>Butea monosperma</em>) - Notified on January 4, 2011 (replaces Brahmakamal post-Uttarakhand separation).
        <br/>• <strong>State Bird:</strong> <strong>Sarus Crane / Kraunch</strong> (<em>Grus antigone</em>) - World's tallest flying bird; largest population resides in UP's wetland belt (Mainpuri, Etawah).
        <br/>• <strong>State Animal:</strong> <strong>Barasingha / Swamp Deer</strong> (<em>Rucervus duvaucelii</em>) - Thrives in Dudhwa National Park wetlands.
        <br/>• <strong>State Aquatic Animal:</strong> <strong>Gangetic Dolphin / Susu</strong> (<em>Platanista gangetica</em>) - Declared state aquatic animal in October 2023.
        <br/>• <strong>State Fish:</strong> <strong>Chital / Chitala</strong> (<em>Chitala chitala</em>)
      </span>
      <span class="lang-hi"><strong>उत्तर प्रदेश के राजकीय प्राकृतिक प्रतीक:</strong>
        <br/>• <strong>राजकीय वृक्ष:</strong> <strong>अशोक / सीता अशोक</strong> (<em>Saraca asoca</em>)
        <br/>• <strong>राजकीय पुष्प:</strong> <strong>पलाश / टेसू / ढाक</strong> (<em>Butea monosperma</em>) - 4 जनवरी 2011 को अधिसूचित।
        <br/>• <strong>राजकीय पक्षी:</strong> <strong>सारस (क्रौंच)</strong> (<em>Grus antigone</em>) - विश्व का सबसे विशाल उड़ने वाला पक्षी; सर्वाधिक संख्या मैनपुरी व इटावा वेटलैंड्स में।
        <br/>• <strong>राजकीय पशु:</strong> <strong>बारहसिंगा (स्वांप डियर)</strong> (<em>Rucervus duvaucelii</em>) - दुधवा राष्ट्रीय उद्यान में संरक्षित।
        <br/>• <strong>राजकीय जलीय जीव:</strong> <strong>गंगा डॉल्फिन (सूंस)</strong> (<em>Platanista gangetica</em>) - अक्टूबर 2023 में घोषित।
        <br/>• <strong>राजकीय मछली:</strong> <strong>चीतल / मोय</strong> (<em>Chitala chitala</em>)
      </span>
    </li>
  </ul>
</div>

<!-- Card 7: High-Yield Rapid Revision Matrix -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Rapid Revision Fact Matrix: UP Forests (Direct Exam Points)</span>
    <span class="lang-hi">6. रैपिड रिवीजन तथ्य मैट्रिक्स: उ.प्र. के वन (सीधे परीक्षा हेतु तथ्य)</span>
  </div>
  <div class="theory-overflow-mb">
    <table border="1">
      <thead>
        <tr>
          <th><span class="lang-en">Examinable Question / Forestry Benchmark</span><span class="lang-hi">परीक्षोपयोगी प्रश्न / वानिकी मानक</span></th>
          <th><span class="lang-en">Definitive Exam Fact / Figure</span><span class="lang-hi">सटीक परीक्षा तथ्य / उत्तर</span></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="lang-en">What is the total Forest Cover of UP as per ISFR 2021?</span><span class="lang-hi">ISFR 2021 के अनुसार उ.प्र. का कुल वनावरण कितना है?</span></td>
          <td><span class="lang-en"><strong>14,817.89 sq km (6.15% of total area)</strong></span><span class="lang-hi"><strong>14,817.89 वर्ग किमी (कुल क्षेत्रफल का 6.15%)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the total Tree Cover of UP as per ISFR 2021?</span><span class="lang-hi">ISFR 2021 के अनुसार उ.प्र. का कुल वृक्षावरण कितना है?</span></td>
          <td><span class="lang-en"><strong>7,421 sq km (3.08% of total area)</strong></span><span class="lang-hi"><strong>7,421 वर्ग किमी (कुल क्षेत्रफल का 3.08%)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the combined Forest &amp; Tree Cover of UP?</span><span class="lang-hi">उ.प्र. का कुल वनावरण एवं वृक्षावरण प्रतिशत कितना है?</span></td>
          <td><span class="lang-en"><strong>22,238.89 sq km (9.23% of total area)</strong></span><span class="lang-hi"><strong>22,238.89 वर्ग किमी (कुल क्षेत्रफल का 9.23%)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the highest forest cover by area?</span><span class="lang-hi">क्षेत्रफल की दृष्टि से सर्वाधिक वनावरण वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Sonbhadra (2,539.25 sq km)</strong> (followed by Lakhimpur Kheri)</span><span class="lang-hi"><strong>सोनभद्र (2,539.25 वर्ग किमी)</strong> (इसके बाद लखीमपुर खीरी)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the highest forest cover by percentage?</span><span class="lang-hi">प्रतिशत की दृष्टि से सर्वाधिक वनावरण वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Sonbhadra (36.79%)</strong> (followed by Chandauli 22.25%)</span><span class="lang-hi"><strong>सोनभद्र (36.79%)</strong> (इसके बाद चंदौली 22.25%)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which district has the lowest forest cover by area and percentage?</span><span class="lang-hi">क्षेत्रफल एवं प्रतिशत दोनों में न्यूनतम वनावरण वाला जिला कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Bhadohi / Sant Ravidas Nagar (3.71 sq km / 0.37%)</strong></span><span class="lang-hi"><strong>भदोही / संत रविदास नगर (3.71 वर्ग किमी / 0.37%)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">When was the Uttar Pradesh Forest Corporation established?</span><span class="lang-hi">उत्तर प्रदेश वन निगम की स्थापना कब हुई थी?</span></td>
          <td><span class="lang-en"><strong>November 25, 1974</strong></span><span class="lang-hi"><strong>25 नवंबर 1974</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">In which year was the Social Forestry Scheme launched in UP?</span><span class="lang-hi">उ.प्र. में सामाजिक वानिकी योजना किस वर्ष प्रारंभ की गई थी?</span></td>
          <td><span class="lang-en"><strong>Year 1976</strong> (with World Bank financial assistance)</span><span class="lang-hi"><strong>वर्ष 1976</strong> (विश्व बैंक की सहायता से)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">From which tree species is Kattha extracted in UP?</span><span class="lang-hi">उ.प्र. में कत्था किस वृक्ष की लकड़ी से निकाला जाता है?</span></td>
          <td><span class="lang-en"><strong>Khair tree (Acacia catechu)</strong> (Processed in Bareilly)</span><span class="lang-hi"><strong>खैर का वृक्ष (Acacia catechu)</strong> (बरेली में प्रसंस्कृत)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which tree leaves are used in the Bidi manufacturing industry?</span><span class="lang-hi">बीड़ी निर्माण में किस वृक्ष के पत्तों का उपयोग होता है?</span></td>
          <td><span class="lang-en"><strong>Tendu leaves (तेंदू पत्ता)</strong> (from Bundelkhand &amp; Mirzapur)</span><span class="lang-hi"><strong>तेंदू पत्ता</strong> (बुंदेलखंड व मिर्जापुर से)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city is the premier hub for the matchbox industry in UP?</span><span class="lang-hi">उ.प्र. में दियासलाई (माचिस) उद्योग का प्रमुख केंद्र कौन सा शहर है?</span></td>
          <td><span class="lang-en"><strong>Bareilly (बरेली)</strong></span><span class="lang-hi"><strong>बरेली</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">Which city is internationally famous for wood carving?</span><span class="lang-hi">काष्ठ नक्काशी (Wood Carving) हेतु कौन सा शहर प्रसिद्ध है?</span></td>
          <td><span class="lang-en"><strong>Saharanpur (सहारनपुर)</strong> (GI tagged) &amp; Nagina (Bijnor)</span><span class="lang-hi"><strong>सहारनपुर</strong> (GI टैग प्राप्त) एवं नगीना (बिजनौर)</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the State Flower of Uttar Pradesh and when was it notified?</span><span class="lang-hi">उ.प्र. का राजकीय पुष्प क्या है और इसे कब अधिसूचित किया गया?</span></td>
          <td><span class="lang-en"><strong>Palash / Tesu (Butea monosperma)</strong> - Notified <strong>4 January 2011</strong></span><span class="lang-hi"><strong>पलाश / टेसू</strong> - <strong>4 जनवरी 2011</strong> को अधिसूचित</span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the State Tree of Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश का राजकीय वृक्ष कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Ashok / Sita Ashok (Saraca asoca)</strong></span><span class="lang-hi"><strong>अशोक / सीता अशोक (Saraca asoca)</strong></span></td>
        </tr>
        <tr>
          <td><span class="lang-en">What is the State Bird of Uttar Pradesh?</span><span class="lang-hi">उत्तर प्रदेश का राजकीय पक्षी कौन सा है?</span></td>
          <td><span class="lang-en"><strong>Sarus Crane / Kraunch (Grus antigone)</strong></span><span class="lang-hi"><strong>सारस / क्रौंच (Grus antigone)</strong></span></td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "forests", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_forests_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
