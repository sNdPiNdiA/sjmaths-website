import os
import re

def build_natural_resources_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Natural Resources Spectrum of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश के प्राकृतिक संसाधनों का समग्र वर्गीकरण</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Natural Resources of Uttar Pradesh] --> B[Water & River Basins]
    A --> C[Canal Networks & Major Dams]
    A --> D[Groundwater Wealth & Aquifers]
    A --> E[Lakes, Tals & Ramsar Wetlands]
    A --> F[Land, Soil & Agro-Physiography]
    A --> G[Forest & Biotic Resources]

    B --> B1[Ganga Basin: Encompasses >90% of UP Area]
    B --> B2[Himalayan Rivers: Ganga 1450 km in UP, Yamuna, Ghaghara, Sharda]
    B --> B3[Peninsular Rivers: Chambal, Betwa, Ken, Son, Tons, Rihand]
    B --> B4[Plain-Origin Rivers: Gomti Fulhar Jheel, Sai, Varuna]

    C --> C1[Canals: Sharda 12,368 km Longest | Upper Ganga 1854 | Eastern Yamuna 1830]
    C --> C2[Interlinking: Ken-Betwa Link | Daudhan Dam | 2.51 L ha Irrigation]
    C --> C3[Dams: Rihand Govind Ballabh Pant Sagar | Matatila & Rajghat Betwa]

    D --> D1[Alluvial Aquifers: Gangetic Plains Multi-layered & Highly Productive]
    D --> D2[Hard Rock Aquifers: Bundelkhand Fractured Granite & Limited Yield]
    D --> D3[Schemes: Atal Bhujal Yojana & Khet Talab Farm Ponds]

    E --> E1[10 Ramsar Sites: Upper Ganga 1st 2005, Bakhira, Haiderpur 2021]
    E --> E2[Historic Lakes: Fulhar Gomti Origin, Keetham, Samaspur, Bela Sagar]

    F --> F1[Net Sown Area: 165.7 L ha | ~68.5% of Total Land | Rank 1 India]
    F --> F2[3 Divisions: Bhabhar-Terai, Gangetic Alluvium, Bundelkhand Plateau]

    G --> G1[ISFR 2021: Forest Cover 6.15% | Tree Cover 3.08% | Total 9.23%]
    G --> G2[MFP: Tendu Leaves, Mahua, Sal Seeds, Kattha, Resin]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश के प्राकृतिक संसाधन] --> B[जल संसाधन एवं नदी बेसिन]
    A --> C[नहर नेटवर्क एवं प्रमुख बांध]
    A --> D[भूजल भंडार एवं एक्विफर]
    A --> E[झीलें, ताल एवं रामसर आर्द्रभूमियां]
    A --> F[भूमि, मृदा एवं कृषि-भूआकृति]
    A --> G[वन एवं जैविक संपदा]

    B --> B1[गंगा बेसिन: राज्य के 90% से अधिक क्षेत्रफल पर विस्तृत]
    B --> B2[हिमालयी नदियां: गंगा 1450 किमी यूपी में, यमुना, घाघरा, शारदा]
    B --> B3[प्रायद्वीपीय नदियां: चंबल, बेतवा, केन, सोन, टोंस, रिहंद]
    B --> B4[मैदानी नदियां: गोमती फुल्हर झील, सई, वरुणा]

    C --> C1[नहरें: शारदा 12,368 किमी सबसे लंबी | ऊपरी गंगा 1854 | पूर्वी यमुना 1830]
    C --> C2[नदी जोड़ो: केन-बेतवा लिंक | दौधन बांध | 2.51 लाख हे. सिंचाई]
    C --> C3[बांध: रिहंद गोविंद बल्लभ पंत सागर | माताटीला व राजघाट बेतवा]

    D --> D1[जलोढ़ एक्विफर: गंगा मैदान बहु-स्तरीय एवं अत्यधिक समृद्ध जलभृत]
    D --> D2[कठोर शैल एक्विफर: बुंदेलखंड खंडित ग्रेनाइट व सीमित भूजल]
    D --> D3[योजनाएं: अटल भूजल योजना एवं खेत तालाब योजना]

    E --> E1[10 रामसर स्थल: ऊपरी गंगा प्रथम 2005, बखिरा, हैदरपुर 2021]
    E --> E2[प्रमुख झीलें: फुल्हर गोमती उद्गम, कीठम, समसपुर, बेला सागर]

    F --> F1[शुद्ध बोया गया क्षेत्र: 165.7 लाख हे. | कुल भूमि का ~68.5% | भारत में प्रथम]
    F --> F2[3 प्राकृतिक विभाजन: भाभर-तराई, गंगा जलोढ़ मैदान, बुंदेलखंड पठार]

    G --> G1[ISFR 2021: वनावरण 6.15% | वृक्षावरण 3.08% | कुल हरित आवरण 9.23%]
    G --> G2[गौण वनोपज: तेंदू पत्ता, महुआ, साल बीज, कत्था, लीसा]
    </div>
  </div>
</div>

<!-- Card 2: Water Resources & Major River Basins -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. Water Resources &amp; Threefold River Systems of Uttar Pradesh</span>
    <span class="lang-hi">1. उत्तर प्रदेश के जल संसाधन एवं त्रिविध नदी तंत्र</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Basin Dominance:</strong> Entire Uttar Pradesh falls within the <strong>Ganga River Basin</strong>, the largest and most populated river basin in the country, endowed with perennial Himalayan flows and extensive monsoon discharge.</span>
        <span class="lang-hi"><strong>बेसिन का विस्तार:</strong> संपूर्ण उत्तर प्रदेश <strong>गंगा नदी बेसिन</strong> के अंतर्गत आता है, जो बारहमासी हिमालयी जलप्रवाह एवं मानसूनी जल से समृद्ध देश का सबसे बड़ा नदी बेसिन है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Himalayan Perennial Rivers (हिमालयी बारहमासी नदियां):</strong>
          <br>&bull; <em>Ganga (गंगा):</em> Enters UP at <strong>Bijnor</strong> district; flows through 28 districts for approximately <strong>1,450 km</strong> before exiting at <strong>Ballia</strong> into Bihar; longest river in the state; joined by Yamuna, Ramganga, Gomti, Ghaghara, Tons.
          <br>&bull; <em>Yamuna (यमुना):</em> Enters at <strong>Saharanpur (Faizabad village)</strong>; flows through 19 districts along UP-Haryana border and Doab; length ~1,376 km; merges with Ganga at the historic <strong>Triveni Sangam (Prayagraj)</strong>.
          <br>&bull; <em>Ghaghara / Sarayu (घाघरा / सरयू):</em> Originates near Lake Mansarovar (Mapchachungo glacier); enters UP at Lakhimpur/Bahraich border; passes Ayodhya as 'Sarayu'; largest river of UP in terms of water volume/discharge; merges with Ganga at Revelganj (Chhapra).
          <br>&bull; <em>Sharda / Kali (शारदा / काली):</em> Enters plains at Banbasa (Pilibhit border); joins Ghaghara at Bahramghat (Barabanki).
          <br>&bull; <em>Ramganga (रामगंगा):</em> Enters plains at Kalagarh (Bijnor); joins Ganga near Kannauj.
          <br>&bull; <em>Gandak (गंडक / नारायणी):</em> Flows along the northeastern border of Maharajganj and Kushinagar districts.</span>
        <span class="lang-hi"><strong>हिमालयी बारहमासी नदियां:</strong>
          <br>&bull; <em>गंगा:</em> उत्तर प्रदेश में <strong>बिजनौर</strong> जिले से प्रवेश करती है; 28 जिलों से होते हुए लगभग <strong>1,450 किमी</strong> बहकर <strong>बलिया</strong> से बिहार में प्रवेश करती है; राज्य की सबसे लंबी नदी।
          <br>&bull; <em>यमुना:</em> <strong>सहारनपुर (फैजाबाद गांव)</strong> से प्रवेश; 19 जिलों से प्रवाहित होकर <strong>त्रिवेणी संगम (प्रयागराज)</strong> में गंगा में विलीन होती है।
          <br>&bull; <em>घाघरा / सरयू:</em> मानसरोवर के निकट मापचाचुंगो हिमनद से उद्गम; लखीमपुर/बहराइच से प्रवेश; अयोध्या में सरयू कहलाती है; जल प्रवाह (डिस्चार्ज) की दृष्टि से यूपी की सबसे बड़ी नदी; छपरा में गंगा से संगम।
          <br>&bull; <em>शारदा / काली:</em> बनबसा (पीलीभीत) से मैदान में प्रवेश; बहरामघाट (बाराबंकी) में घाघरा से मिलती है।
          <br>&bull; <em>रामगंगा:</em> कालागढ़ (बिजनौर) से मैदान में प्रवेश; कन्नौज के निकट गंगा में संगम।
          <br>&bull; <em>गंडक (नारायणी):</em> महाराजगंज और कुशीनगर जिलों की उत्तर-पूर्वी सीमा पर प्रवाहित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Peninsular / Plateau Rivers (प्रायद्वीपीय पठारी नदियां - Non-Perennial):</strong>
          <br>&bull; <em>Chambal (चंबल):</em> Originates from Janapav hills (Mhow, MP); forms southern boundary; joins Yamuna at <strong>Panchnada (Etawah/Auraiya border)</strong>; famous for ravines/badlands and gharial sanctuary.
          <br>&bull; <em>Betwa (बेतवा / वेत्रवती):</em> Originates in Raisen (MP); enters UP in Lalitpur; passes Jhansi and Jalaun; merges into Yamuna at <strong>Hamirpur</strong>.
          <br>&bull; <em>Ken (केन / कर्णावती):</em> Originates in Kaimur hills (MP); passes Banda; merges into Yamuna at <strong>Chilla (Banda)</strong>.
          <br>&bull; <em>Son (सोन):</em> Originates from Amarkantak (MP); flows across southern <strong>Sonbhadra</strong> district before joining Ganga near Patna.
          <br>&bull; <em>Tons / Tamasa (टोंस):</em> Merges with Ganga at <strong>Sirsa (Prayagraj)</strong>.
          <br>&bull; <em>Rihand (रिहंद):</em> Tributary of Son river; site of Govind Ballabh Pant Sagar reservoir at Pipri (Sonbhadra).</span>
        <span class="lang-hi"><strong>प्रायद्वीपीय पठारी नदियां (गैर-बारहमासी):</strong>
          <br>&bull; <em>चंबल:</em> जनापाव पहाड़ी (महू, मप्र) से उद्गम; <strong>पंचनद (इटावा/औरैया सीमा)</strong> पर यमुना में मिलती है; बीहड़ों एवं घड़ियाल अभयारण्य हेतु प्रसिद्ध।
          <br>&bull; <em>बेतवा (वेत्रवती):</em> रायसेन (मप्र) से उद्गम; ललितपुर से प्रवेश कर झांसी व जालौन होते हुए <strong>हमीरपुर</strong> के निकट यमुना में संगम।
          <br>&bull; <em>केन (कर्णावती):</em> कैमूर पहाड़ी (मप्र) से उद्गम; बांदा में <strong>चिल्ला</strong> के निकट यमुना में संगम।
          <br>&bull; <em>सोन:</em> अमरकंटक से उद्गम; दक्षिणी <strong>सोनभद्र</strong> जिले से बहते हुए पटना के पास गंगा में मिलती है।
          <br>&bull; <em>टोंस (तमसा):</em> <strong>सिरसा (प्रयागराज)</strong> के पास गंगा में संगम।
          <br>&bull; <em>रिहंद:</em> सोन की प्रमुख सहायक नदी; पिपरी (सोनभद्र) में गोविंद बल्लभ पंत सागर बांध इसी पर स्थित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Plain-Origin / Groundwater-Fed Rivers (मैदानी उद्गम की नदियां):</strong>
          <br>&bull; <em>Gomti (गोमती):</em> Originates from <strong>Fulhar Jheel / Gomat Taal in Madhotanda (Pilibhit)</strong>; length ~960 km; flows through Lucknow, Sultanpur, Jaunpur; merges with Ganga at <strong>Kaithi (Ghazipur/Varanasi border)</strong>.
          <br>&bull; <em>Sai River (सई):</em> Originates from Bijwan Jheel (Hardoi); joins Gomti at Rajepur (Jaunpur).
          <br>&bull; <em>Varuna &amp; Assi:</em> Streams of Varanasi plain joining Ganga (giving Varanasi its name).</span>
        <span class="lang-hi"><strong>मैदानी उद्गम की नदियां (भूजल पोषित):</strong>
          <br>&bull; <em>गोमती:</em> <strong>माधोटांडा (पीलीभीत) स्थित फुल्हर झील / गोमत ताल</strong> से उद्गम; लंबाई ~960 किमी; लखनऊ, सुल्तानपुर, जौनपुर से बहते हुए <strong>कैथी (गाजीपुर/वाराणसी सीमा)</strong> पर गंगा में संगम।
          <br>&bull; <em>सई नदी:</em> भिजवान झील (हरदोई) से उद्गम; राजेपुर (जौनपुर) में गोमती से मिलती है।
          <br>&bull; <em>वरुणा एवं अस्सी:</em> वाराणसी के मैदानी नाले जो गंगा में मिलते हैं (जिनसे वाराणसी नामकरण हुआ)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Canal Irrigation Network & Major Dams -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. Canal Irrigation Systems, Multi-Purpose Dams &amp; River Interlinking</span>
    <span class="lang-hi">2. नहर सिंचाई प्रणालियां, बहुउद्देशीय बांध एवं नदी जोड़ो परियोजना</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Sharda Canal System (शारदा नहर तंत्र):</strong>
          <br>&bull; <em>Status:</em> <strong>Longest canal network in Uttar Pradesh</strong> with total system length (including branches and distributaries) of approximately <strong>12,368 km</strong>.
          <br>&bull; <em>Headworks:</em> Constructed at Banbasa on Sharda river (Pilibhit/Champawat border).
          <br>&bull; <em>Commissioned:</em> Completed and opened for irrigation in <strong>1928</strong>.
          <br>&bull; <em>Beneficiary Districts:</em> Pilibhit, Lakhimpur Kheri, Shahjahanpur, Hardoi, Sitapur, Lucknow, Unnao, Rae Bareli, Barabanki, Ayodhya, and Prayagraj.</span>
        <span class="lang-hi"><strong>शारदा नहर तंत्र:</strong>
          <br>&bull; <em>स्थिति:</em> शाखाओं-प्रशाखाओं सहित कुल <strong>12,368 किमी</strong> लंबाई के साथ <strong>उत्तर प्रदेश का सबसे लंबा नहर नेटवर्क</strong>।
          <br>&bull; <em>उद्गम स्थल:</em> शारदा नदी पर बनबसा (पीलीभीत/चंपावत सीमा) बैराज से निकाली गई।
          <br>&bull; <em>शुरुआत:</em> <strong>1928</strong> में निर्माण पूर्ण होकर चालू की गई।
          <br>&bull; <em>लाभान्वित जिले:</em> पीलीभीत, लखीमपुर खीरी, शाहजहांपुर, हरदोई, सीतापुर, लखनऊ, उन्नाव, रायबरेली, बाराबंकी, अयोध्या एवं प्रयागराज।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Upper Ganga Canal (ऊपरी गंगा नहर):</strong>
          <br>&bull; <em>Engineer &amp; Construction:</em> Designed and constructed under <strong>Sir Proby Cautley</strong> between <strong>1842 and 1854</strong>.
          <br>&bull; <em>Headworks:</em> Originates from Bhimgoda Barrage at Haridwar.
          <br>&bull; <em>Command Area:</em> Irrigates Western UP Doab districts including Saharanpur, Muzaffarnagar, Meerut, Ghaziabad, Bulandshahr, and Aligarh; terminates near Mainpuri.</span>
        <span class="lang-hi"><strong>ऊपरी गंगा नहर:</strong>
          <br>&bull; <em>निर्माण व अभियंता:</em> <strong>सर प्रोबी काटले</strong> के निर्देशन में <strong>1842 से 1854</strong> के मध्य निर्मित।
          <br>&bull; <em>उद्गम:</em> हरिद्वार स्थित भीमगोड़ा बैराज से निकाली गई।
          <br>&bull; <em>सिंचाई क्षेत्र:</em> पश्चिमी यूपी के दोआब जिले (सहारनपुर, मुजफ्फरनगर, मेरठ, गाजियाबाद, बुलंदशहर, अलीगढ़); मैनपुरी के निकट समाप्त होती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Lower Ganga Canal (निचली गंगा नहर):</strong>
          <br>&bull; Originates from <strong>Narora Barrage (Bulandshahr)</strong> on Ganga; commissioned in <strong>1878</strong>; irrigates Bulandshahr, Aligarh, Mathura, Agra, Etah, Mainpuri, Farrukhabad, and Kanpur.</span>
        <span class="lang-hi"><strong>निचली गंगा नहर:</strong>
          <br>&bull; गंगा नदी पर <strong>नरौरा बैराज (बुलंदशहर)</strong> से निकाली गई; <strong>1878</strong> में चालू हुई; बुलंदशहर, अलीगढ़, मथुरा, आगरा, एटा, मैनपुरी, फर्रुखाबाद और कानपुर को सिंचित करती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Eastern Yamuna Canal (पूर्वी यमुना नहर):</strong>
          <br>&bull; <strong>Oldest canal in Uttar Pradesh</strong>; originally excavated during Mughal Emperor Shah Jahan's reign (1631); remodeled and reopened by British in <strong>1830</strong>; originates from Faizabad (Saharanpur) on left bank of Yamuna; irrigates Saharanpur, Shamli, Muzaffarnagar, Meerut, and Baghpat.</span>
        <span class="lang-hi"><strong>पूर्वी यमुना नहर:</strong>
          <br>&bull; <strong>उत्तर प्रदेश की सबसे पुरानी नहर</strong>; मूल रूप से मुगल बादशाह शाहजहां के शासनकाल (1631) में खोदी गई; अंग्रेजों द्वारा <strong>1830</strong> में पुनर्गठित; यमुना के बाएं किनारे फैजाबाद (सहारनपुर) से निकाली गई।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Agra Canal (आगरा नहर):</strong>
          <br>&bull; Originates from <strong>Okhla Barrage</strong> on Yamuna; commissioned in <strong>1874</strong>; provides irrigation to Mathura, Agra, and border areas of Rajasthan and Haryana.</span>
        <span class="lang-hi"><strong>आगरा नहर:</strong>
          <br>&bull; यमुना नदी पर <strong>ओखला बैराज</strong> से निकाली गई; <strong>1874</strong> में चालू; मथुरा, आगरा तथा राजस्थान और हरियाणा के सीमावर्ती क्षेत्रों को जल उपलब्ध कराती है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Ken-Betwa River Interlinking Project (केन-बेतवा लिंक परियोजना):</strong>
          <br>&bull; <em>National Milestone:</em> <strong>India's first river interlinking project</strong> under National Perspective Plan.
          <br>&bull; <em>Structure:</em> Construction of <strong>Daudhan Dam</strong> on Ken river in Chhatarpur (MP) and a 221 km link canal to transfer surplus water to Betwa basin.
          <br>&bull; <em>Benefit to UP:</em> Direct annual irrigation to <strong>2.51 lakh hectares</strong> across water-starved Bundelkhand districts (Banda, Mahoba, Jhansi, Lalitpur) and drinking water to 21 lakh people.</span>
        <span class="lang-hi"><strong>केन-बेतवा लिंक परियोजना:</strong>
          <br>&bull; <em>राष्ट्रीय मील का पत्थर:</em> राष्ट्रीय परिप्रेक्ष्य योजना के तहत <strong>भारत की पहली नदी जोड़ो परियोजना</strong>।
          <br>&bull; <em>संरचना:</em> छतरपुर (मप्र) में केन नदी पर <strong>दौधन बांध</strong> एवं 221 किमी लंबी लिंक नहर द्वारा अतिरिक्त जल बेतवा बेसिन में स्थानांतरित करना।
          <br>&bull; <em>यूपी को लाभ:</em> सूखाग्रस्त बुंदेलखंड के जिलों (बांदा, महोबा, झांसी, ललितपुर) में <strong>2.51 लाख हेक्टेयर</strong> भूमि पर वार्षिक सिंचाई तथा 21 लाख लोगों को पेयजल।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Major Multi-Purpose Dams &amp; Reservoirs:</strong>
          <br>&bull; <em>Govind Ballabh Pant Sagar (Rihand Dam):</em> Concrete gravity dam on Rihand river at Pipri (Sonbhadra); <strong>India's largest artificial/man-made reservoir</strong> (~466 sq km storage area); 300 MW hydel capacity.
          <br>&bull; <em>Matatila Dam (माताटीला बांध):</em> Built in 1958 on Betwa river in Lalitpur; also known as 'Rani Laxmibai Dam'; irrigates Jhansi, Jalaun, Hamirpur.
          <br>&bull; <em>Rajghat Dam (राजघाट बांध):</em> Inter-state joint venture of UP and MP on Betwa river in Lalitpur district.
          <br>&bull; <em>Parichha Dam:</em> Betwa river near Jhansi; supplies water to Parichha Thermal Power Plant.
          <br>&bull; <em>Bansagar Dam:</em> Joint project of UP, MP, and Bihar on Son river; canal network feeds Mirzapur and Prayagraj.</span>
        <span class="lang-hi"><strong>प्रमुख बहुउद्देशीय बांध एवं जलाशय:</strong>
          <br>&bull; <em>गोविंद बल्लभ पंत सागर (रिहंद बांध):</em> पिपरी (सोनभद्र) में रिहंद नदी पर कंक्रीट ग्रेविटी बांध; <strong>भारत का सबसे बड़ा कृत्रिम जलाशय</strong> (~466 वर्ग किमी फैलाव); 300 मेगावाट जलविद्युत क्षमता।
          <br>&bull; <em>माताटीला बांध:</em> 1958 में बेतवा नदी (ललितपुर) पर निर्मित; इसे 'रानी लक्ष्मीबाई बांध' भी कहते हैं; झांसी, जालौन, हमीरपुर को सिंचित करता है।
          <br>&bull; <em>राजघाट बांध:</em> ललितपुर में बेतवा नदी पर यूपी और एमपी की संयुक्त अंतरराज्यीय परियोजना।
          <br>&bull; <em>परीछा बांध:</em> झांसी के निकट बेतवा नदी पर; परीछा ताप विद्युत गृह को जल आपूर्ति।
          <br>&bull; <em>बाणसागर बांध:</em> सोन नदी पर यूपी, एमपी और बिहार की संयुक्त परियोजना; नहरें मिर्जापुर व प्रयागराज को जल देती हैं।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Groundwater Dynamics & Management -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. Groundwater Wealth, Aquifer Zones &amp; Water Conservation Programs</span>
    <span class="lang-hi">3. भूजल संपदा, जलभृत क्षेत्र एवं जल संरक्षण कार्यक्रम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Primary Source of Irrigation:</strong> Tubewells (नलकूप) account for approximately <strong>73.4% of net irrigated area</strong> in UP, making groundwater the bedrock of the state's agrarian economy.</span>
        <span class="lang-hi"><strong>सिंचाई का मुख्य साधन:</strong> उत्तर प्रदेश में शुद्ध सिंचित क्षेत्र का लगभग <strong>73.4% नलकूपों</strong> द्वारा सिंचित होता है, जिससे भूजल राज्य की कृषि अर्थव्यवस्था का आधार है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Two Hydrogeological Provinces:</strong>
          <br>&bull; <em>Gangetic Alluvial Tract (गंगा जलोढ़ क्षेत्र):</em> Unconsolidated quaternary sand, gravel, and clay layers reaching depths of up to 1,000-2,000 meters; high porosity, prolific yield, dynamic recharge via monsoon and river seepage.
          <br>&bull; <em>Southern Marginal Hard-Rock Tract (बुंदेलखंड-विंध्य कठोर शैल):</em> Granite, gneiss, sandstones; poor secondary porosity (confined to fissures/fractures); water table drops severely in summer.</span>
        <span class="lang-hi"><strong>दो प्रमुख जल-भूवैज्ञानिक प्रभाग:</strong>
          <br>&bull; <em>गंगा जलोढ़ क्षेत्र:</em> चतुर्थक रेत, बजरी और दोमट मिट्टी की 1,000-2,000 मीटर तक गहरी परतें; उच्च जलभंडारण क्षमता एवं मानसूनी रिसाव से निरंतर पुनर्भरण।
          <br>&bull; <em>दक्षिणी सीमांत कठोर शैल क्षेत्र (बुंदेलखंड-विंध्य):</em> ग्रेनाइट, नीस, बलुआ पत्थर; केवल दरारों व संधियों तक सीमित भूजल; गर्मियों में जलस्तर अत्यधिक नीचे गिरता है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Groundwater Stress &amp; Over-Exploitation:</strong>
          <br>&bull; Overall state groundwater development stage is ~70-72% (categorized as 'Safe' at macro level).
          <br>&bull; However, severe groundwater depletion occurs in Western UP (Meerut, Muzaffarnagar, Saharanpur, Aligarh) driven by water-intensive paddy-sugarcane cropping, and in Bundelkhand due to low geological storage.</span>
        <span class="lang-hi"><strong>भूजल संकट एवं अति-दोहन:</strong>
          <br>&bull; राज्य का समग्र भूजल दोहन स्तर ~70-72% है (मैक्रो स्तर पर 'सुरक्षित' श्रेणी)।
          <br>&bull; किंतु पश्चिमी यूपी में अत्यधिक जल-खपत वाली धान-गन्ना फसलों के कारण और बुंदेलखंड में कठोर शैल संरचना के कारण कई ब्लॉक 'अति-दोहित' (Over-Exploited) घोषित हैं।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Water Conservation Schemes:</strong>
          <br>&bull; <em>Atal Bhujal Yojana (अटल भूजल योजना):</em> Implemented across water-stressed gram panchayats in Bundelkhand and Western UP with World Bank assistance; community-led water security plans.
          <br>&bull; <em>Khet Talab Yojana (खेत तालाब योजना):</em> 50% subsidy to farmers in Bundelkhand and drought-prone districts to construct farm ponds for rainwater harvesting.
          <br>&bull; <em>Amrit Sarovar Mission:</em> UP ranked <strong>Rank 1 in India</strong> in constructing and rejuvenating village ponds (Amrit Sarovars) to recharge local aquifers.</span>
        <span class="lang-hi"><strong>जल संरक्षण योजनाएं:</strong>
          <br>&bull; <em>अटल भूजल योजना:</em> विश्व बैंक की सहायता से बुंदेलखंड और पश्चिमी यूपी की जल संकटग्रस्त ग्राम पंचायतों में सामुदायिक जल सुरक्षा योजना।
          <br>&bull; <em>खेत तालाब योजना:</em> वर्षा जल संचयन हेतु बुंदेलखंड के किसानों को खेत तालाब निर्माण पर 50% अनुदान।
          <br>&bull; <em>अमृत सरोवर मिशन:</em> स्थानीय जलभृतों के पुनर्भरण हेतु ग्राम तालाबों के कायाकल्प में उत्तर प्रदेश <strong>देश में प्रथम स्थान</strong> पर रहा।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Natural Lakes, Tals & Ramsar Wetlands -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Natural Lakes, Historic Tals &amp; 10 Ramsar Wetlands of UP</span>
    <span class="lang-hi">4. प्राकृतिक झीलें, ऐतिहासिक ताल एवं उत्तर प्रदेश के 10 रामसर आर्द्रभूमि स्थल</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>10 Ramsar Wetland Sites of Uttar Pradesh:</strong>
          <br>1. <strong>Upper Ganga River (Brijghat to Narora):</strong> <em>Designated in 2005 (1st Ramsar site of UP)</em>; 82 km stretch; critical habitat of endangered Gangetic Dolphin, gharials, and otters.
          <br>2. <strong>Nawabganj Bird Sanctuary (Unnao):</strong> Renamed <em>Shahid Chandra Shekhar Azad Bird Sanctuary</em>; designated 2019.
          <br>3. <strong>Parvati Arga Bird Sanctuary (Gonda):</strong> Permanent oxbow lake wetland; designated 2019.
          <br>4. <strong>Saman Bird Sanctuary (Mainpuri):</strong> Seasonal wetland on Ganga-Yamuna floodplain; designated 2019.
          <br>5. <strong>Samaspur Bird Sanctuary (Rae Bareli):</strong> Perennial wetland lake system; designated 2019.
          <br>6. <strong>Sandi Bird Sanctuary (Hardoi):</strong> Natural freshwater marsh fed by Garra river; designated 2019.
          <br>7. <strong>Sarsai Nawar (Etawah):</strong> Permanent marsh; prime nesting ground of Sarus Crane; designated 2019.
          <br>8. <strong>Sur Sarovar / Keetham Lake (Agra):</strong> Artificial man-made lake on Yamuna canal; bears sanctuary; designated 2020.
          <br>9. <strong>Haiderpur Wetland (Muzaffarnagar/Bijnor):</strong> Formed on Madhya Ganga Canal; rich biodiversity; designated <strong>2021 (47th in India)</strong>.
          <br>10. <strong>Bakhira Wildlife Sanctuary (Sant Kabir Nagar):</strong> Largest natural floodplain lake in Eastern UP; designated <strong>2022 (49th in India)</strong>.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के 10 रामसर आर्द्रभूमि स्थल:</strong>
          <br>1. <strong>ऊपरी गंगा नदी (ब्रजघाट से नरौरा):</strong> <em>2005 में घोषित (यूपी का प्रथम रामसर स्थल)</em>; 82 किमी विस्तार; गंगा डॉल्फिन, घड़ियाल और ऊदबिलाव का वास।
          <br>2. <strong>नवाबगंज पक्षी अभयारण्य (उन्नाव):</strong> नया नाम <em>शहीद चंद्रशेखर आजाद पक्षी अभयारण्य</em>; 2019 में घोषित।
          <br>3. <strong>पार्वती अरगा पक्षी अभयारण्य (गोंडा):</strong> गोखुर (Oxbow) झील आधारित आर्द्रभूमि; 2019 में घोषित।
          <br>4. <strong>समन पक्षी अभयारण्य (मैनपुरी):</strong> गंगा-यमुना बाढ़ के मैदान पर मौसमी आर्द्रभूमि; 2019 में घोषित।
          <br>5. <strong>समसपुर पक्षी अभयारण्य (रायबरेली):</strong> बारहमासी झील आर्द्रभूमि; 2019 में घोषित।
          <br>6. <strong>सांडी पक्षी अभयारण्य (हरदोई):</strong> गर्रा नदी के निकट प्राकृतिक दलदल; 2019 में घोषित।
          <br>7. <strong>सरसई नावर (इटावा):</strong> सारस क्रेन का प्रमुख प्रजनन स्थल; 2019 में घोषित।
          <br>8. <strong>सूर सरोवर / कीठम झील (आगरा):</strong> यमुना नहर से जुड़ी झील; भालू संरक्षण केंद्र; 2020 में घोषित।
          <br>9. <strong>हैदरपुर वेटलैंड (मुजफ्फरनगर/बिजनौर):</strong> मध्य गंगा बैराज पर निर्मित; <strong>2021 में घोषित (देश का 47वां)</strong>।
          <br>10. <strong>बखिरा वन्यजीव अभयारण्य (संत कबीर नगर):</strong> पूर्वी यूपी की सबसे बड़ी प्राकृतिक मीठे पानी की झील; <strong>2022 में घोषित (देश का 49वां)</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Directory of Famous Historic Lakes &amp; Tals:</strong>
          <br>&bull; <em>Fulhar Jheel / Gomat Taal (Pilibhit):</em> Origin of Gomti river.
          <br>&bull; <em>Bela Sagar &amp; Madan Sagar (Mahoba):</em> Historic Chandela-built lakes.
          <br>&bull; <em>Barua Sagar (Jhansi):</em> Large artificial lake built by Orchha Bundela rulers.
          <br>&bull; <em>Surha Tal / Loknayak Tal (Ballia):</em> Large oxbow lake on Ganga-Ghaghara interfluve.
          <br>&bull; <em>Ramgarh Tal (Gorakhpur):</em> Massive urban natural lake developed as tourism waterfront.
          <br>&bull; <em>Karela &amp; Itauja Jheel (Lucknow):</em> Historic freshwater lakes.
          <br>&bull; <em>Chittaura Jheel (Bahraich):</em> Site of Maharaja Suheldev battle monument.
          <br>&bull; <em>Gaur Jheel &amp; Moti Jheel (Rampur / Kanpur):</em> Scenic urban water bodies.</span>
        <span class="lang-hi"><strong>प्रमुख ऐतिहासिक झीलों एवं तालों की सूची:</strong>
          <br>&bull; <em>फुल्हर झील / गोमत ताल (पीलीभीत):</em> गोमती नदी का उद्गम स्थल।
          <br>&bull; <em>बेला सागर एवं मदन सागर (महोबा):</em> चंदेल शासकों द्वारा निर्मित ऐतिहासिक झीलें।
          <br>&bull; <em>बरुआ सागर (झांसी):</em> ओरछा के बुंदेला राजाओं द्वारा निर्मित विशाल झील।
          <br>&bull; <em>सुरहा ताल / लोकनायक ताल (बलिया):</em> गंगा-घाघरा दोआब पर विशाल गोखुर झील।
          <br>&bull; <em>रामगढ़ ताल (गोरखपुर):</em> प्राकृतिक विशाल झील, जिसे पर्यटन स्थल के रूप में विकसित किया गया।
          <br>&bull; <em>करेला एवं इटौंजा झील (लखनऊ):</em> ऐतिहासिक मीठे पानी की झीलें।
          <br>&bull; <em>चित्तौरा झील (बहराइच):</em> महाराजा सुहेलदेव स्मारक स्थल।
          <br>&bull; <em>गौर झील व मोती झील (रामपुर / कानपुर):</em> प्रमुख जलाशय।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Land, Soil & Agro-Ecological Wealth -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Land Endowment, Agro-Physiography &amp; Soil Wealth</span>
    <span class="lang-hi">5. भूमि संपदा, कृषि-भूआकृति एवं मृदा संसाधन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Agricultural Land Extent:</strong> Total geographical area of UP is <strong>240.93 lakh hectares</strong> (7.33% of India); <strong>Net Sown Area is ~165.7 lakh hectares (~68.5%)</strong>, the highest cultivated land base among all Indian states; Gross Cropped Area ~260 lakh hectares; Cropping intensity ~162%.</span>
        <span class="lang-hi"><strong>कृषि भूमि का विस्तार:</strong> उत्तर प्रदेश का कुल भौगोलिक क्षेत्रफल <strong>240.93 लाख हेक्टेयर</strong> (देश का 7.33%) है; <strong>शुद्ध बोया गया क्षेत्र ~165.7 लाख हेक्टेयर (~68.5%)</strong> है, जो भारत के सभी राज्यों में सर्वाधिक है; फसल सघनता ~162% है।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Three Major Physiographic Resource Zones:</strong>
          <br>&bull; <em>Bhabhar &amp; Terai Belt (उत्तरी भाभर एवं तराई):</em> Foothill gravelly pebble tract (Bhabhar where mountain streams vanish underground) transitioning into marshy, water-saturated, tall-grass alluvial plain (Terai) rich in nitrogen and organic matter; suited for sugarcane and paddy.
          <br>&bull; <em>Gangetic Alluvial Plain (गंगा का विशाल मैदान):</em> Flat, deep alluvium divided into <strong>Khadar (नवीन जलोढ़ - floodplains, fertile, sandy-silt)</strong> and <strong>Bhangar (पुरातन जलोढ़ - higher interfluves, clayey loam with calcareous Kankar nodules)</strong>; breadbasket of India.
          <br>&bull; <em>Southern Plateau &amp; Upland (दक्षिणी पठारी भाग - Bundelkhand &amp; Vindhyan):</em> Old crystalline granites, gneisses, and sandstones; thin, gravelly soils (Rakar, Parwa) and black soils (Marr, Kabar); prone to drought; suited for pulses, oilseeds, and coarse cereals.</span>
        <span class="lang-hi"><strong>तीन प्रमुख भू-आकृतिक संसाधन क्षेत्र:</strong>
          <br>&bull; <em>भाभर एवं तराई पट्टी:</em> शिवालिक तलहटी का कंकड़-पत्थर वाला क्षेत्र (भाभर, जहां नदियां लुप्त हो जाती हैं) जो आगे दलदली, अत्यधिक नम तराई मैदान में बदलता है; नाइट्रोजन व जीवांश से भरपूर; गन्ना व धान हेतु आदर्श।
          <br>&bull; <em>गंगा का विशाल मैदान:</em> गहरा जलोढ़ मैदान, जो <strong>खादर (नवीन जलोढ़ - बाढ़ क्षेत्र, उपजाऊ गाद)</strong> तथा <strong>बांगर (पुरातन जलोढ़ - कंकड़ ग्रंथियों युक्त दोमट)</strong> में विभाजित है; भारत का अन्न भंडार।
          <br>&bull; <em>दक्षिणी पठारी भाग (बुंदेलखंड व विंध्याचल):</em> प्राचीन ग्रेनाइट, नीस व बलुआ पत्थर; उथली लाल मृदाएं (राकर, परवा) तथा काली मृदाएं (मार, काबर); दलहन, तिलहन व मोटे अनाजों हेतु उपयुक्त।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Reclamation of Usar/Alkaline Soils (ऊसर भूमि सुधार):</strong> Approximately 10-12 lakh hectares in Mainpuri, Aligarh, Rae Bareli, Sultanpur, and Pratapgarh affected by salinity/alkalinity (Reh/Kallar); reclaimed through gypsum application, green manuring (Dhaincha), and UP Bhumi Sudhar Nigam projects.</span>
        <span class="lang-hi"><strong>ऊसर/क्षारीय भूमि सुधार:</strong> मैनपुरी, अलीगढ़, रायबरेली, सुल्तानपुर और प्रतापगढ़ में लगभग 10-12 लाख हेक्टेयर भूमि लवणीय/क्षारीय (रेह/कल्लर) से प्रभावित; जिप्सम, ढैंचा की हरी खाद और यूपी भूमि सुधार निगम की परियोजनाओं द्वारा सुधारी जा रही है।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Forest & Biotic Wealth Synthesis -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Forest Resources, Minor Forest Produce &amp; State Natural Symbols</span>
    <span class="lang-hi">6. वन संसाधन, गौण वनोपज एवं राज्य के प्राकृतिक प्रतीक</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>ISFR 2021 Forest Metrics:</strong>
          <br>&bull; Forest Cover: <strong>14,817.89 sq km (6.15% of geographic area)</strong>.
          <br>&bull; Tree Cover: <strong>7,421 sq km (3.08%)</strong>.
          <br>&bull; Total Green Cover: <strong>22,238.89 sq km (9.23%)</strong>.
          <br>&bull; Highest Forest Area &amp; Percent: <strong>Sonbhadra (2,539 sq km / 36.79%)</strong>.
          <br>&bull; Lowest Forest Area &amp; Percent: <strong>Bhadohi (3.71 sq km / 0.37%)</strong>.</span>
        <span class="lang-hi"><strong>ISFR 2021 वन सांख्यिकी:</strong>
          <br>&bull; वनावरण: <strong>14,817.89 वर्ग किमी (कुल क्षेत्रफल का 6.15%)</strong>।
          <br>&bull; वृक्षावरण: <strong>7,421 वर्ग किमी (3.08%)</strong>।
          <br>&bull; कुल हरित आवरण: <strong>22,238.89 वर्ग किमी (9.23%)</strong>।
          <br>&bull; सर्वाधिक वन क्षेत्रफल व प्रतिशत: <strong>सोनभद्र (2,539 वर्ग किमी / 36.79%)</strong>।
          <br>&bull; न्यूनतम वन क्षेत्रफल व प्रतिशत: <strong>भदोही (3.71 वर्ग किमी / 0.37%)</strong>।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Minor Forest Produce (MFP / गौण वनोपज):</strong>
          <br>&bull; <em>Tendu Leaves (Diospyros melanoxylon):</em> Mined in Sonbhadra, Mirzapur, Bundelkhand; collected under UP Forest Corporation for bidi manufacturing.
          <br>&bull; <em>Mahua (Madhuca longifolia):</em> Flowers and seeds used for indigenous nutrition, oil extraction, and local brewing.
          <br>&bull; <em>Kattha (Acacia catechu):</em> Extracted from Khair wood; Bareilly is the historic industrial center.
          <br>&bull; <em>Resin (लीसा):</em> Extracted from Chir pine in Saharanpur Shivaliks; used for turpentine and varnishes.
          <br>&bull; <em>Cane &amp; Bamboo (बेंत एवं बांस):</em> Bareilly furniture industry and paper pulp mills.</span>
        <span class="lang-hi"><strong>गौण वनोपज (MFP):</strong>
          <br>&bull; <em>तेंदू पत्ता:</em> सोनभद्र, मिर्जापुर और बुंदेलखंड में संग्रहण; यूपी वन निगम द्वारा बीड़ी निर्माण हेतु विपणन।
          <br>&bull; <em>महुआ:</em> फूल व बीज खाद्य पोषण, तेल निष्कर्षण और पारंपरिक मदिरा हेतु प्रयुक्त।
          <br>&bull; <em>कत्था:</em> खैर की लकड़ी से निष्कर्षित; बरेली इसका ऐतिहासिक विनिर्माण केंद्र है।
          <br>&bull; <em>लीसा (रेजिन):</em> सहारनपुर शिवालिक के चीड़ वनों से प्राप्त; तारपीन तेल और वार्निश में प्रयुक्त।
          <br>&bull; <em>बेंत व बांस:</em> बरेली का फर्नीचर उद्योग तथा कागज मिलों हेतु कच्चा माल।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Official State Natural Symbols:</strong>
          <br>&bull; State Tree: <strong>Ashok (Saraca asoca)</strong>.
          <br>&bull; State Flower: <strong>Palash / Tesu (Butea monosperma)</strong> - declared 2011.
          <br>&bull; State Bird: <strong>Sarus Crane (Grus antigone)</strong>.
          <br>&bull; State Animal: <strong>Swamp Deer / Barasingha (Rucervus duvaucelii)</strong>.
          <br>&bull; State Aquatic Animal: <strong>Gangetic Dolphin (Platanista gangetica)</strong> - declared in 2023.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के आधिकारिक प्राकृतिक प्रतीक:</strong>
          <br>&bull; राज्य वृक्ष: <strong>अशोक (Saraca asoca)</strong>।
          <br>&bull; राज्य पुष्प: <strong>पलाश / टेसू (Butea monosperma)</strong> - वर्ष 2011 में अधिसूचित।
          <br>&bull; राज्य पक्षी: <strong>सारस क्रेन (Grus antigone)</strong>।
          <br>&bull; राज्य पशु: <strong>बारहसिंगा (Rucervus duvaucelii)</strong>।
          <br>&bull; राज्य जलीय जीव: <strong>गंगा डॉल्फिन (Platanista gangetica)</strong> - वर्ष 2023 में घोषित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: Master Comparison Table of Natural Resources -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. Master Comparison Table: Natural Resources of Uttar Pradesh</span>
    <span class="lang-hi">7. उत्तर प्रदेश के प्राकृतिक संसाधनों की महा-तुलना तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Resource Category</span>
            <span class="lang-hi">संसाधन श्रेणी</span>
          </th>
          <th>
            <span class="lang-en">Key Centers / Geographical Distribution</span>
            <span class="lang-hi">प्रमुख केंद्र / भौगोलिक वितरण</span>
          </th>
          <th>
            <span class="lang-en">Statistical Metric &amp; Exam Significance</span>
            <span class="lang-hi">सांख्यिकी एवं परीक्षा दृष्टि से महत्व</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Longest Canal System</span>
            <span class="lang-hi">सबसे लंबी नहर प्रणाली</span>
          </td>
          <td>
            <span class="lang-en">Sharda Canal (Banbasa, Pilibhit border to Central/Eastern UP)</span>
            <span class="lang-hi">शारदा नहर (बनबसा, पीलीभीत से मध्य/पूर्वी यूपी)</span>
          </td>
          <td>
            <span class="lang-en">~12,368 km total system length; commissioned 1928</span>
            <span class="lang-hi">कुल लंबाई ~12,368 किमी; 1928 में चालू</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Oldest Canal System</span>
            <span class="lang-hi">सबसे पुरानी नहर प्रणाली</span>
          </td>
          <td>
            <span class="lang-en">Eastern Yamuna Canal (Faizabad, Saharanpur to Western Doab)</span>
            <span class="lang-hi">पूर्वी यमुना नहर (फैजाबाद, सहारनपुर से पश्चिमी दोआब)</span>
          </td>
          <td>
            <span class="lang-en">Originally 1631 (Shah Jahan); remodeled 1830 by British</span>
            <span class="lang-hi">मूल रूप से 1631 (शाहजहां); 1830 में ब्रिटिश द्वारा पुनर्गठित</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Largest Artificial Reservoir</span>
            <span class="lang-hi">सबसे बड़ा कृत्रिम जलाशय</span>
          </td>
          <td>
            <span class="lang-en">Govind Ballabh Pant Sagar (Rihand Dam, Pipri, Sonbhadra)</span>
            <span class="lang-hi">गोविंद बल्लभ पंत सागर (रिहंद बांध, पिपरी, सोनभद्र)</span>
          </td>
          <td>
            <span class="lang-en">~466 sq km storage area; largest man-made lake in India; 300 MW hydel</span>
            <span class="lang-hi">~466 वर्ग किमी फैलाव; भारत की सबसे बड़ी मानव निर्मित झील; 300 MW</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">1st River Interlinking Project</span>
            <span class="lang-hi">प्रथम नदी जोड़ो परियोजना</span>
          </td>
          <td>
            <span class="lang-en">Ken-Betwa Link (Daudhan Dam MP to Betwa, UP Bundelkhand)</span>
            <span class="lang-hi">केन-बेतवा लिंक (दौधन बांध मप्र से बेतवा, यूपी बुंदेलखंड)</span>
          </td>
          <td>
            <span class="lang-en">2.51 lakh ha irrigation for Banda, Mahoba, Jhansi, Lalitpur</span>
            <span class="lang-hi">बांदा, महोबा, झांसी, ललितपुर हेतु 2.51 लाख हे. सिंचाई</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Primary Irrigation Source</span>
            <span class="lang-hi">प्राथमिक सिंचाई साधन</span>
          </td>
          <td>
            <span class="lang-en">Tubewells (नलकूप) across Gangetic plain</span>
            <span class="lang-hi">गंगा मैदान में नलकूप (सरकारी व निजी)</span>
          </td>
          <td>
            <span class="lang-en"><strong>73.4%</strong> of net irrigated area (Canals: ~15.2%)</span>
            <span class="lang-hi">शुद्ध सिंचित क्षेत्र का <strong>73.4%</strong> (नहरें: ~15.2%)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">First Ramsar Wetland</span>
            <span class="lang-hi">प्रथम रामसर आर्द्रभूमि</span>
          </td>
          <td>
            <span class="lang-en">Upper Ganga River (Brijghat to Narora, 82 km stretch)</span>
            <span class="lang-hi">ऊपरी गंगा नदी (ब्रजघाट से नरौरा, 82 किमी खंड)</span>
          </td>
          <td>
            <span class="lang-en">Designated in 2005; Gangetic Dolphin and gharial habitat</span>
            <span class="lang-hi">2005 में अधिसूचित; गंगा डॉल्फिन और घड़ियाल आवास</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Gomti River Origin</span>
            <span class="lang-hi">गोमती नदी उद्गम</span>
          </td>
          <td>
            <span class="lang-en">Fulhar Jheel / Gomat Taal (Madhotanda, Pilibhit)</span>
            <span class="lang-hi">फुल्हर झील / गोमत ताल (माधोटांडा, पीलीभीत)</span>
          </td>
          <td>
            <span class="lang-en">Groundwater-fed plain-origin river; length ~960 km; joins Ganga at Kaithi</span>
            <span class="lang-hi">मैदानी उद्गम की भूजल-पोषित नदी; लंबाई ~960 किमी; कैथी में संगम</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Cultivated Land Share</span>
            <span class="lang-hi">कृषि योग्य भूमि हिस्सा</span>
          </td>
          <td>
            <span class="lang-en">Net Sown Area: ~165.7 lakh hectares</span>
            <span class="lang-hi">शुद्ध बोया गया क्षेत्र: ~165.7 लाख हेक्टेयर</span>
          </td>
          <td>
            <span class="lang-en">~68.5% of total state land; Rank 1 in India</span>
            <span class="lang-hi">राज्य के कुल क्षेत्रफल का ~68.5%; भारत में प्रथम स्थान</span>
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
            <span class="lang-en">High-Yield Answer &amp; Conceptual Clarity</span>
            <span class="lang-hi">उच्च अंकदायी उत्तर एवं स्पष्टीकरण</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Longest River within UP</span>
            <span class="lang-hi">यूपी में सर्वाधिक लंबी नदी</span>
          </td>
          <td>
            <span class="lang-en"><strong>Ganga (~1,450 km)</strong>; enters Bijnor, exits Ballia; passes 28 districts.</span>
            <span class="lang-hi"><strong>गंगा (~1,450 किमी)</strong>; बिजनौर से प्रवेश, बलिया से निकास; 28 जिलों से गुजरती है।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">River with Maximum Water Volume</span>
            <span class="lang-hi">सर्वाधिक जल प्रवाह (डिस्चार्ज) वाली नदी</span>
          </td>
          <td>
            <span class="lang-en"><strong>Ghaghara (Sarayu)</strong>; brings highest water discharge in UP plains.</span>
            <span class="lang-hi"><strong>घाघरा (सरयू)</strong>; यूपी के मैदानों में सर्वाधिक जल आयतन लाती है।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Panchnada Confluence</span>
            <span class="lang-hi">पंचनद संगम</span>
          </td>
          <td>
            <span class="lang-en">Confluence of 5 rivers near Etawah/Auraiya: <strong>Yamuna, Chambal, Kwari, Sindh, and Pahuj</strong>.</span>
            <span class="lang-hi">इटावा/औरैया सीमा पर 5 नदियों का संगम: <strong>यमुना, चंबल, क्वारी, सिंध और पहुज</strong>।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Rani Laxmibai Dam Location</span>
            <span class="lang-hi">रानी लक्ष्मीबाई बांध अवस्थिति</span>
          </td>
          <td>
            <span class="lang-en">Built on <strong>Betwa river in Lalitpur</strong> district (also called Matatila Dam).</span>
            <span class="lang-hi"><strong>ललितपुर जिले में बेतवा नदी</strong> पर निर्मित (माताटीला बांध)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Upper Ganga Canal Architect</span>
            <span class="lang-hi">ऊपरी गंगा नहर के वास्तुकार</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sir Proby Cautley (1842-1854)</strong>; originates at Haridwar.</span>
            <span class="lang-hi"><strong>सर प्रोबी काटले (1842-1854)</strong>; हरिद्वार से निकाली गई।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Total Ramsar Sites in UP</span>
            <span class="lang-hi">यूपी में कुल रामसर स्थल</span>
          </td>
          <td>
            <span class="lang-en"><strong>10 Ramsar Sites</strong> (2nd highest in India after Tamil Nadu).</span>
            <span class="lang-hi"><strong>10 रामसर स्थल</strong> (तमिलनाडु के बाद देश में दूसरा सर्वाधिक)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">State Aquatic Animal</span>
            <span class="lang-hi">राज्य जलीय जीव</span>
          </td>
          <td>
            <span class="lang-en"><strong>Gangetic Dolphin (Platanista gangetica)</strong>; declared in October 2023.</span>
            <span class="lang-hi"><strong>गंगा डॉल्फिन</strong>; अक्टूबर 2023 में आधिकारिक रूप से घोषित।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "natural-resources", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_natural_resources_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
