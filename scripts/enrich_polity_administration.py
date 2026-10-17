import os
import re

def build_polity_theory_html():
    return """<div class="tab-content" id="tab-theory" style="display:block">

<!-- Card 1: Mind Map -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">Mind Map: Constitutional Setup &amp; Administrative Machinery of Uttar Pradesh</span>
    <span class="lang-hi">माइंड मैप: उत्तर प्रदेश का संवैधानिक ढांचा एवं प्रशासनिक तंत्र</span>
  </div>
  <div class="lang-en">
    <div class="mermaid">
graph TD
    A[Polity & Administration of UP] --> B[State Legislature]
    A --> C[State Executive]
    A --> D[State Judiciary]
    A --> E[Administrative Hierarchy]
    A --> F[Local Self-Government]
    A --> G[Constitutional & Statutory Bodies]

    B --> B1[Bicameral: Vidhan Sabha 403 Seats | Vidhan Parishad 100 Seats]
    B --> B2[Parliament: Lok Sabha 80 Seats | Rajya Sabha 31 Seats]
    B --> B3[Reservation: VS 84 SC + 2 ST Obra/Duddhi | LS 17 SC]

    C --> C1[Governor: Sarojini Naidu 1st Female | Anandiben Patel Current]
    C --> C2[Chief Minister: Pt. Govind Ballabh Pant 1st | Sucheta Kripalani 1st Woman]
    C --> C3[President's Rule: Imposed 10 Times | 1st in 1968 | Last in 2002]

    D --> D1[Allahabad High Court: Est. 1866 Agra -> 1869 Allahabad]
    D --> D2[Lucknow Bench: Est. 1925 | 160 Sanctioned Judges Largest in India]
    D --> D3[1st CJ: Sir Walter Morgan | 1st Post-Independence: Justice B. Malik]

    E --> E1[18 Divisions: Kanpur, Lucknow, Meerut Largest 6 Dists | Aligarh 18th]
    E --> E2[75 Districts: Lakhimpur Kheri Largest | Hapur Smallest Area]
    E --> E3[Sonbhadra: Borders 4 States MP, CG, JH, BR | Saharanpur 3 States]

    F --> F1[Panchayati Raj 3-Tier: 75 Zilla, 826 Kshetra, 58,189 Gram Panchayats]
    F --> F2[Urban: 17 Municipal Corporations Nagar Nigam | Shahjahanpur 17th]
    F --> F3[Women Reservation: 33% 1/3rd Across All Local Bodies]

    G --> G1[UPPSC: Est. 1937 Prayagraj | State Election Commission: 1994]
    G --> G2[Lokayukta: Act 1975 Est. 1977 | 1st Justice Vishwambhar Dayal]
    G --> G3[State Human Rights Commission: 2002 | RTI Commission: 2005]
    </div>
  </div>
  <div class="lang-hi">
    <div class="mermaid">
graph TD
    A[उत्तर प्रदेश की राजव्यवस्था एवं प्रशासन] --> B[राज्य विधायिका]
    A --> C[राज्य कार्यपालिका]
    A --> D[राज्य न्यायपालिका]
    A --> E[प्रशासनिक संरचना]
    A --> F[स्थानीय स्वशासन]
    A --> G[संवैधानिक एवं सांविधिक निकाय]

    B --> B1[द्विसदनीय: विधानसभा 403 सीटें | विधान परिषद 100 सीटें]
    B --> B2[संसद: लोकसभा 80 सीटें | राज्यसभा 31 सीटें देश में सर्वाधिक]
    B --> B3[आरक्षण: विस 84 SC + 2 ST ओबरा/दुद्धी | लोस 17 SC]

    C --> C1[राज्यपाल: सरोजिनी नायडू प्रथम महिला | आनंदीबेन पटेल वर्तमान]
    C --> C2[मुख्यमंत्री: पं. गोविंद बल्लभ पंत प्रथम | सुचेता कृपलानी प्रथम महिला]
    C --> C3[राष्ट्रपति शासन: कुल 10 बार लागू | प्रथम 1968 | अंतिम 2002]

    D --> D1[इलाहाबाद उच्च न्यायालय: 1866 आगरा में स्थापना -> 1869 इलाहाबाद]
    D --> D2[लखनऊ खंडपीठ: स्थापना 1925 | 160 स्वीकृत न्यायाधीश देश में सबसे बड़ा]
    D --> D3[प्रथम मुख्य न्यायाधीश: सर वाल्टर मॉर्गन | स्वतंत्रता बाद: न्यायमूर्ति बी. मलिक]

    E --> E1[18 मंडल: कानपुर, लखनऊ, मेरठ सर्वाधिक 6 जिले | अलीगढ़ 18वां]
    E --> E2[75 जिले: लखीमपुर खीरी सबसे बड़ा | हापुड़ सबसे छोटा क्षेत्रफल]
    E --> E3[सोनभद्र: 4 राज्यों मप्र, छग, झा, बि से सीमा | सहारनपुर 3 राज्य]

    F --> F1[पंचायती राज 3-स्तरीय: 75 जिला, 826 क्षेत्र, 58,189 ग्राम पंचायतें]
    F --> F2[शहरी: 17 नगर निगम | शाहजहांपुर 17वां नगर निगम]
    F --> F3[महिला आरक्षण: स्थानीय निकायों में 33% 1/3 आरक्षण]

    G --> G1[UPPSC: 1937 प्रयागराज | राज्य निर्वाचन आयोग: 1994]
    G --> G2[लोकायुक्त: अधिनियम 1975 लागू 1977 | प्रथम विश्वंभर दयाल]
    G --> G3[राज्य मानवाधिकार आयोग: 2002 | सूचना आयोग: 2005]
    </div>
  </div>
</div>

<!-- Card 2: State Legislature & Parliamentary Representation -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">1. State Legislature: Vidhan Sabha, Vidhan Parishad &amp; Parliament Seats</span>
    <span class="lang-hi">1. राज्य विधायिका: विधानसभा, विधान परिषद एवं संसदीय प्रतिनिधित्व</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Bicameral System (द्विसदनीय विधायिका):</strong> Established under the <strong>Government of India Act 1935</strong>; Uttar Pradesh is one of only 6 Indian states with a bicameral legislature (UP, Bihar, Maharashtra, Karnataka, Andhra Pradesh, Telangana).</span>
        <span class="lang-hi"><strong>द्विसदनीय व्यवस्था:</strong> <strong>भारत शासन अधिनियम 1935</strong> के तहत स्थापित; उत्तर प्रदेश भारत के उन केवल 6 राज्यों में शामिल है जहां द्विसदनीय विधायिका है (यूपी, बिहार, महाराष्ट्र, कर्नाटक, आंध्र प्रदेश, तेलंगाना)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Legislative Assembly (विधान सभा):</strong>
          <br>&bull; <em>Total Strength:</em> <strong>403 directly elected members</strong> (earlier 404 with 1 nominated Anglo-Indian member, discontinued under 104th Constitutional Amendment Act 2019).
          <br>&bull; <em>Constitutional Quota (Reserved Seats):</em> <strong>86 seats reserved</strong> (84 for Scheduled Castes / SC, and <strong>2 for Scheduled Tribes / ST: Obra and Duddhi in Sonbhadra</strong>).
          <br>&bull; <em>First Speaker (प्रथम विधानसभा अध्यक्ष):</em> <strong>Rajarshi Purushottam Das Tandon</strong> (1937-1950).
          <br>&bull; <em>First Deputy Speaker:</em> Abdul Hakeem.
          <br>&bull; <em>Maximum Times Speaker:</em> Atmaram Govind Kher and Kesari Nath Tripathi (3 times each).
          <br>&bull; <em>Present Speaker:</em> Satish Mahana (18th Assembly).</span>
        <span class="lang-hi"><strong>विधानसभा:</strong>
          <br>&bull; <em>कुल सीटें:</em> <strong>403 प्रत्यक्ष निर्वाचित सदस्य</strong> (पहले 1 मनोनीत एंग्लो-इंडियन सहित 404 थीं, जिसे 104वें संविधान संशोधन 2019 द्वारा समाप्त कर दिया गया)।
          <br>&bull; <em>आरक्षित सीटें:</em> कुल <strong>86 आरक्षित सीटें</strong> (84 अनुसूचित जाति / SC हेतु, तथा <strong>2 अनुसूचित जनजाति / ST हेतु: सोनभद्र के ओबरा एवं दुद्धी</strong>)।
          <br>&bull; <em>प्रथम विधानसभा अध्यक्ष:</em> <strong>राजर्षि पुरुषोत्तम दास टंडन</strong> (1937-1950)।
          <br>&bull; <em>प्रथम उपाध्यक्ष:</em> अब्दुल हकीम।
          <br>&bull; <em>सर्वाधिक बार अध्यक्ष:</em> आत्माराम गोविंद खेर एवं केशरी नाथ त्रिपाठी (3-3 बार)।
          <br>&bull; <em>वर्तमान विधानसभा अध्यक्ष:</em> सतीश महाना (18वीं विधानसभा)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Legislative Council (विधान परिषद):</strong>
          <br>&bull; <em>Strength:</em> <strong>100 members</strong> (Permanent house, not subject to dissolution; 1/3rd members retire every 2 years; 6-year tenure).
          <br>&bull; <em>Composition Breakdown (Article 171):</em>
            - 38 members elected by Members of Legislative Assembly (MLAs).
            - 36 members elected by Local Authorities (Zilla &amp; Kshetra Panchayats, Municipalities).
            - 8 members elected by Graduates' constituencies.
            - 8 members elected by Teachers' constituencies.
            - 10 members nominated by the Governor from literature, science, art, cooperative movement, and social service.
          <br>&bull; <em>First Chairman (Pre-Independence):</em> Sir Dr. Sita Ram.
          <br>&bull; <em>First Chairman (Post-Independence):</em> Chandra Bhal (1949-1958).</span>
        <span class="lang-hi"><strong>विधान परिषद:</strong>
          <br>&bull; <em>सदस्य संख्या:</em> <strong>100 सदस्य</strong> (स्थायी सदन, विघटित नहीं होता; 1/3 सदस्य प्रति 2 वर्ष बाद सेवानिवृत्त; कार्यकाल 6 वर्ष)।
          <br>&bull; <em>निर्वाचन संरचना (अनुच्छेद 171):</em>
            - 38 सदस्य विधानसभा सदस्यों (MLAs) द्वारा निर्वाचित।
            - 36 सदस्य स्थानीय निकायों (जिला/क्षेत्र पंचायत, नगर पालिका) द्वारा निर्वाचित।
            - 8 सदस्य स्नातक निर्वाचन क्षेत्रों द्वारा।
            - 8 सदस्य शिक्षक निर्वाचन क्षेत्रों द्वारा।
            - 10 सदस्य राज्यपाल द्वारा साहित्य, विज्ञान, कला, सहकारिता एवं समाज सेवा से मनोनीत।
          <br>&bull; <em>प्रथम सभापति (स्वतंत्रता पूर्व):</em> सर डॉ. सीता राम।
          <br>&bull; <em>प्रथम सभापति (स्वतंत्रता बाद):</em> चंद्र भाल (1949-1958)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Parliamentary Representation (संसदीय प्रतिनिधित्व):</strong>
          <br>&bull; <em>Lok Sabha (लोक सभा):</em> <strong>80 seats</strong> (highest among all states; 17 reserved for SC, 0 for ST).
          <br>&bull; <em>Rajya Sabha (राज्य सभा):</em> <strong>31 seats</strong> (highest among all states in the Council of States).</span>
        <span class="lang-hi"><strong>संसदीय प्रतिनिधित्व:</strong>
          <br>&bull; <em>लोकसभा:</em> <strong>80 सीटें</strong> (देश के सभी राज्यों में सर्वाधिक; 17 सीटें SC हेतु आरक्षित, ST हेतु 0)।
          <br>&bull; <em>राज्यसभा:</em> <strong>31 सीटें</strong> (देश के सभी राज्यों में सर्वाधिक)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 3: Executive - Governor, Chief Minister & President's Rule -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">2. State Executive: Governor, Chief Minister, Council of Ministers &amp; President's Rule</span>
    <span class="lang-hi">2. राज्य कार्यपालिका: राज्यपाल, मुख्यमंत्री, मंत्रिपरिषद एवं राष्ट्रपति शासन</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Governor of Uttar Pradesh (राज्यपाल - Article 153-161):</strong>
          <br>&bull; <em>Constitutional Head:</em> Constitutional executive head of the state acting on the aid and advice of the Council of Ministers headed by the CM.
          <br>&bull; <em>First Governor (Post-Independence):</em> <strong>Sarojini Naidu</strong> (15 August 1947 to 2 March 1949); <strong>first woman Governor of any Indian state</strong>; died in office at Lucknow.
          <br>&bull; <em>First Governor of United Provinces (1937):</em> Sir Harry Graham Haig.
          <br>&bull; <em>Current Governor:</em> <strong>Anandiben Patel</strong> (since July 2019).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश के राज्यपाल (अनुच्छेद 153-161):</strong>
          <br>&bull; <em>संवैधानिक प्रमुख:</em> मुख्यमंत्री की अध्यक्षता वाली मंत्रिपरिषद की सलाह पर कार्य करने वाले राज्य के संवैधानिक प्रमुख।
          <br>&bull; <em>प्रथम राज्यपाल (स्वतंत्रता बाद):</em> <strong>श्रीमती सरोजिनी नायडू</strong> (15 अगस्त 1947 से 2 मार्च 1949); <strong>भारत के किसी भी राज्य की प्रथम महिला राज्यपाल</strong>; पद पर रहते हुए लखनऊ में निधन।
          <br>&bull; <em>संयुक्त प्रांत के प्रथम राज्यपाल (1937):</em> सर हैरी ग्राहम हेग।
          <br>&bull; <em>वर्तमान राज्यपाल:</em> <strong>श्रीमती आनंदीबेन पटेल</strong> (जुलाई 2019 से)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Chief Minister &amp; Council of Ministers (मुख्यमंत्री एवं मंत्रिपरिषद - Article 163-164):</strong>
          <br>&bull; <em>First Chief Minister:</em> <strong>Pt. Govind Ballabh Pant</strong> (Premier from 1937-1939 &amp; 1946; designated Chief Minister of UP on 26 January 1950 to 1954; awarded Bharat Ratna in 1957).
          <br>&bull; <em>First Woman Chief Minister:</em> <strong>Sucheta Kripalani</strong> (October 1963 to March 1967); <strong>first woman Chief Minister of any Indian state</strong>.
          <br>&bull; <em>Second Woman Chief Minister:</em> <strong>Mayawati</strong> (1st Dalit woman CM in India; served 4 terms: 1995, 1997, 2002, 2007-2012).
          <br>&bull; <em>Maximum Times Chief Minister:</em> <strong>Mayawati (4 times)</strong>.
          <br>&bull; <em>Youngest Chief Minister:</em> <strong>Akhilesh Yadav</strong> (sworn in at age 38 in 2012).
          <br>&bull; <em>UP Chief Ministers who became Prime Ministers of India:</em> <strong>Chaudhary Charan Singh</strong> and <strong>Vishwanath Pratap Singh (V.P. Singh)</strong>.
          <br>&bull; <em>Incumbent Chief Minister:</em> Yogi Adityanath (first CM of UP to complete a continuous 5-year term and return to power with a majority since 1985).</span>
        <span class="lang-hi"><strong>मुख्यमंत्री एवं मंत्रिपरिषद (अनुच्छेद 163-164):</strong>
          <br>&bull; <em>प्रथम मुख्यमंत्री:</em> <strong>पं. गोविंद बल्लभ पंत</strong> (1937-1939 व 1946 में प्रीमियर; 26 जनवरी 1950 को यूपी के प्रथम मुख्यमंत्री बने, 1954 तक रहे; 1957 में भारत रत्न)।
          <br>&bull; <em>प्रथम महिला मुख्यमंत्री:</em> <strong>श्रीमती सुचेता कृपलानी</strong> (अक्टूबर 1963 से मार्च 1967); <strong>भारत के किसी भी राज्य की प्रथम महिला मुख्यमंत्री</strong>।
          <br>&bull; <em>द्वितीय महिला मुख्यमंत्री:</em> <strong>सुश्री मायावती</strong> (भारत की प्रथम दलित महिला मुख्यमंत्री; कुल 4 बार सीएम: 1995, 1997, 2002, 2007-2012)।
          <br>&bull; <em>सर्वाधिक बार मुख्यमंत्री:</em> <strong>सुश्री मायावती (4 बार)</strong>।
          <br>&bull; <em>सबसे युवा मुख्यमंत्री:</em> <strong>अखिलेश यादव</strong> (2012 में 38 वर्ष की आयु में शपथ ली)।
          <br>&bull; <em>यूपी के मुख्यमंत्री जो भारत के प्रधानमंत्री बने:</em> <strong>चौधरी चरण सिंह</strong> एवं <strong>विश्वनाथ प्रताप सिंह (वी.पी. सिंह)</strong>।
          <br>&bull; <em>वर्तमान मुख्यमंत्री:</em> योगी आदित्यनाथ (1985 के बाद लगातार 5 वर्ष का कार्यकाल पूरा कर पुनः बहुमत से सत्ता में लौटने वाले पहले मुख्यमंत्री)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>President's Rule in UP (राष्ट्रपति शासन - Article 356):</strong>
          <br>&bull; <em>Frequency:</em> Imposed <strong>10 times</strong> in Uttar Pradesh.
          <br>&bull; <em>First Imposition:</em> <strong>25 February 1968 to 26 February 1969</strong> (during tenure of Governor B. Gopala Reddi after resignation of Chaudhary Charan Singh).
          <br>&bull; <em>Tenth &amp; Last Imposition:</em> <strong>8 March 2002 to 3 May 2002</strong> (during hung assembly post-2002 elections).
          <br>&bull; <em>Longest Period:</em> 1968-1969 (1 year) and 1992-1993 (post-Babri structure demolition).</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश में राष्ट्रपति शासन (अनुच्छेद 356):</strong>
          <br>&bull; <em>कुल बार:</em> उत्तर प्रदेश में अब तक <strong>10 बार</strong> राष्ट्रपति शासन लगाया जा चुका है।
          <br>&bull; <em>प्रथम बार:</em> <strong>25 फरवरी 1968 से 26 फरवरी 1969</strong> (चौधरी चरण सिंह के इस्तीफे के बाद, राज्यपाल बी. गोपाला रेड्डी के समय)।
          <br>&bull; <em>10वीं एवं अंतिम बार:</em> <strong>8 मार्च 2002 से 3 मई 2002</strong> (त्रिशंकु विधानसभा के दौरान)।
          <br>&bull; <em>सबसे लंबा दौर:</em> 1968-1969 (1 वर्ष) तथा 1992-1993।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 4: Judiciary - Allahabad High Court & Subordinate Courts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">3. State Judiciary: Allahabad High Court &amp; Lucknow Bench</span>
    <span class="lang-hi">3. राज्य न्यायपालिका: इलाहाबाद उच्च न्यायालय एवं लखनऊ खंडपीठ</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Establishment &amp; Historical Trajectory:</strong>
          <br>&bull; <em>Established:</em> Formed under the Indian High Courts Act 1861 on <strong>17 March 1866 at Agra</strong> as the <em>High Court of Judicature for the North-Western Provinces</em>.
          <br>&bull; <em>Shift to Allahabad:</em> Shifted from Agra to <strong>Allahabad in 1869</strong>.
          <br>&bull; <em>Renamed:</em> Formally designated as the <strong>High Court of Judicature at Allahabad</strong> on 11 March 1919.</span>
        <span class="lang-hi"><strong>स्थापना एवं ऐतिहासिक विकास:</strong>
          <br>&bull; <em>स्थापना:</em> भारतीय उच्च न्यायालय अधिनियम 1861 के तहत <strong>17 मार्च 1866 को आगरा</strong> में <em>उत्तर-पश्चिमी प्रांतों हेतु उच्च न्यायालय</em> के रूप में गठित।
          <br>&bull; <em>इलाहाबाद स्थानांतरण:</em> <strong>1869 में आगरा से इलाहाबाद</strong> स्थानांतरित किया गया।
          <br>&bull; <em>नामकरण:</em> 11 मार्च 1919 को औपचारिक रूप से <strong>इलाहाबाद उच्च न्यायालय</strong> नाम दिया गया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Lucknow Bench (लखनऊ खंडपीठ):</strong>
          <br>&bull; <em>Origin:</em> Formerly the Chief Court of Oudh (established under Oudh Courts Act 1925).
          <br>&bull; <em>Amalgamation:</em> United with Allahabad High Court under the <em>United Provinces High Courts (Amalgamation) Order 1948</em> on <strong>26 July 1948</strong>.
          <br>&bull; <em>Jurisdiction:</em> Exercises original and appellate jurisdiction over <strong>12 districts of Awadh</strong>: Lucknow, Ayodhya (Faizabad), Barabanki, Rae Bareli, Sitapur, Lakhimpur Kheri, Unnao, Pratapgarh, Sultanpur, Amethi, Hardoi, and Bahraich.</span>
        <span class="lang-hi"><strong>लखनऊ खंडपीठ:</strong>
          <br>&bull; <em>उत्पत्ति:</em> पूर्व में अवध चीफ कोर्ट (अवध कोर्ट्स एक्ट 1925 के तहत गठित)।
          <br>&bull; <em>विलय:</em> <em>संयुक्त प्रांत उच्च न्यायालय (समामेलन) आदेश 1948</em> के तहत <strong>26 जुलाई 1948</strong> को इलाहाबाद उच्च न्यायालय में समामेलित।
          <br>&bull; <em>क्षेत्राधिकार:</em> अवध क्षेत्र के <strong>12 जिलों</strong> पर अधिकारिता: लखनऊ, अयोध्या, बाराबंकी, रायबरेली, सीतापुर, लखीमपुर खीरी, उन्नाव, प्रतापगढ़, सुल्तानपुर, अमेठी, हरदोई एवं बहराइच।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Sanctioned Strength &amp; Judicial Luminaries:</strong>
          <br>&bull; <em>Sanctioned Judge Strength:</em> <strong>160 Judges</strong> (120 Permanent + 40 Additional) - <strong>largest High Court in India</strong> by judge strength.
          <br>&bull; <em>First Chief Justice (Pre-Independence):</em> <strong>Sir Walter Morgan</strong> (1866-1871).
          <br>&bull; <em>First Indian Chief Justice:</em> <strong>Sir Shah Muhammad Sulaiman</strong> (1932).
          <br>&bull; <em>First Chief Justice Post-Independence:</em> <strong>Justice Bidhubhushan Malik</strong> (1947-1955).</span>
        <span class="lang-hi"><strong>स्वीकृत पद एवं प्रमुख मुख्य न्यायाधीश:</strong>
          <br>&bull; <em>स्वीकृत न्यायाधीश संख्या:</em> <strong>160 न्यायाधीश</strong> (120 स्थायी + 40 अतिरिक्त) - न्यायाधीशों की संख्या में <strong>भारत का सबसे बड़ा उच्च न्यायालय</strong>।
          <br>&bull; <em>प्रथम मुख्य न्यायाधीश (स्वतंत्रता पूर्व):</em> <strong>सर वाल्टर मॉर्गन</strong> (1866-1871)।
          <br>&bull; <em>प्रथम भारतीय मुख्य न्यायाधीश:</em> <strong>सर शाह मुहम्मद सुलेमान</strong> (1932)।
          <br>&bull; <em>स्वतंत्रता बाद प्रथम मुख्य न्यायाधीश:</em> <strong>न्यायमूर्ति बिधुभूषण मलिक</strong> (1947-1955)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 5: Administrative Divisions & Districts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">4. Administrative Divisions, Districts &amp; Revenue Hierarchy</span>
    <span class="lang-hi">4. प्रशासनिक मंडल, जिले एवं राजस्व प्रशासनिक पदानुक्रम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>18 Administrative Divisions (प्रशासनिक मंडल):</strong>
          <br>&bull; Headed by a <strong>Divisional Commissioner (मंडलायुक्त - IAS)</strong> who supervises revenue administration, public grievance redressal, and law and order coordination across districts.
          <br>&bull; <em>Largest Divisions (6 districts each):</em> <strong>Kanpur, Lucknow, and Meerut</strong>.
          <br>&bull; <em>Smallest Divisions (3 districts each):</em> <strong>Mirzapur, Basti, Jhansi, Saharanpur, and Azamgarh</strong>.
          <br>&bull; <em>Newest Division:</em> <strong>Aligarh Division (18th Division)</strong>, carved out in April 2008 comprising Aligarh, Etah, Hathras, and Kasganj.</span>
        <span class="lang-hi"><strong>18 प्रशासनिक मंडल:</strong>
          <br>&bull; प्रत्येक मंडल का प्रमुख <strong>मंडलायुक्त (कमिश्नर - IAS)</strong> होता है, जो मंडल के जिलों के राजस्व प्रशासन और विकास कार्यों का पर्यवेक्षण करता है।
          <br>&bull; <em>सर्वाधिक जिलों वाले मंडल (प्रत्येक में 6 जिले):</em> <strong>कानपुर, लखनऊ एवं मेरठ</strong>।
          <br>&bull; <em>न्यूनतम जिलों वाले मंडल (प्रत्येक में 3 जिले):</em> <strong>मिर्जापुर, बस्ती, झांसी, सहारनपुर एवं आजमगढ़</strong>।
          <br>&bull; <em>नवीनतम मंडल:</em> <strong>अलीगढ़ मंडल (18वां मंडल)</strong>, अप्रैल 2008 में अलीगढ़, एटा, हाथरस और कासगंज को मिलाकर गठित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>75 Districts &amp; Geographical Extremes:</strong>
          <br>&bull; <em>Largest District by Area:</em> <strong>Lakhimpur Kheri (7,680 sq km)</strong>, followed by Sonbhadra (6,788 sq km).
          <br>&bull; <em>Smallest District by Area:</em> <strong>Hapur (660 sq km)</strong>, followed by Bhadohi (1,015 sq km).
          <br>&bull; <em>Four-State Bordering District:</em> <strong>Sonbhadra</strong> is the only district in India bordering <strong>4 states</strong> (Madhya Pradesh, Chhattisgarh, Jharkhand, and Bihar).
          <br>&bull; <em>Three-State Bordering District:</em> <strong>Saharanpur</strong> borders 3 states (Haryana, Himachal Pradesh, and Uttarakhand).
          <br>&bull; <em>Most Populous District (2011 Census):</em> <strong>Prayagraj</strong> (~59.5 lakh).
          <br>&bull; <em>Least Populous District (2011 Census):</em> <strong>Mahoba</strong> (~8.7 lakh).</span>
        <span class="lang-hi"><strong>75 जिले एवं भौगोलिक छोर:</strong>
          <br>&bull; <em>क्षेत्रफल में सबसे बड़ा जिला:</em> <strong>लखीमपुर खीरी (7,680 वर्ग किमी)</strong>, द्वितीय सोनभद्र (6,788 वर्ग किमी)।
          <br>&bull; <em>क्षेत्रफल में सबसे छोटा जिला:</em> <strong>हापुड़ (660 वर्ग किमी)</strong>, द्वितीय भदोही (1,015 वर्ग किमी)।
          <br>&bull; <em>चार राज्यों से सीमा बनाने वाला जिला:</em> <strong>सोनभद्र</strong> भारत का एकमात्र जिला है जो <strong>4 राज्यों</strong> (मध्य प्रदेश, छत्तीसगढ़, झारखंड एवं बिहार) की सीमा को छूता है।
          <br>&bull; <em>तीन राज्यों से सीमा बनाने वाला जिला:</em> <strong>सहारनपुर</strong> (हरियाणा, हिमाचल प्रदेश एवं उत्तराखंड)।
          <br>&bull; <em>सर्वाधिक जनसंख्या वाला जिला (जनगणना 2011):</em> <strong>प्रयागराज</strong> (~59.5 लाख)।
          <br>&bull; <em>न्यूनतम जनसंख्या वाला जिला (जनगणना 2011):</em> <strong>महोबा</strong> (~8.7 लाख)।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Sub-District Administrative Units:</strong>
          <br>&bull; Tehsils: <strong>351 Tehsils</strong> (headed by Sub-Divisional Magistrate / SDM and Tehsildar for revenue adjudication).
          <br>&bull; Development Blocks: <strong>826 Vikas Khand / Blocks</strong> (headed by Block Development Officer / BDO).
          <br>&bull; Gram Panchayats: <strong>58,189 Gram Panchayats</strong>.
          <br>&bull; Revenue Villages: 1,06,774 villages (inhabited: ~97,814).</span>
        <span class="lang-hi"><strong>उप-जिला प्रशासनिक इकाइयां:</strong>
          <br>&bull; तहसीलें: <strong>351 तहसीलें</strong> (उपजिलाधिकारी / SDM तथा तहसीलदार इसके प्रमुख)।
          <br>&bull; विकास खंड (ब्लॉक): <strong>826 विकास खंड</strong> (खंड विकास अधिकारी / BDO प्रमुख)।
          <br>&bull; ग्राम पंचायतें: <strong>58,189 ग्राम पंचायतें</strong>।
          <br>&bull; राजस्व ग्राम: 1,06,774 ग्राम (आबाद ग्राम: ~97,814)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 6: Panchayati Raj & Urban Local Governance -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">5. Local Self-Government: 3-Tier Panchayati Raj &amp; 17 Municipal Corporations</span>
    <span class="lang-hi">5. स्थानीय स्वशासन: त्रि-स्तरीय पंचायती राज एवं 17 नगर निगम</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>Rural Local Self-Government (3-Tier Panchayati Raj):</strong>
          <br>&bull; <em>Statutory Evolution:</em> Governed originally under <strong>UP Panchayati Raj Act 1947</strong> (Gram Panchayats) and <strong>UP Kshetra Panchayats &amp; Zilla Panchayats Act 1961</strong>; modernized via UP Panchayati Raj (Amendment) Act <strong>1994</strong> post-73rd Constitutional Amendment.
          <br>&bull; <em>Apex Tier:</em> <strong>Zilla Panchayat (75 units)</strong>; political head is Zilla Panchayat Adhyaksha (elected indirectly by ward members); Chief Executive Officer is Chief Development Officer (CDO) / Additional CEO (Panchayat).
          <br>&bull; <em>Intermediate Tier:</em> <strong>Kshetra Panchayat (826 units)</strong>; political head is Block Pramukh; Chief Executive Officer is Block Development Officer (BDO).
          <br>&bull; <em>Base Tier:</em> <strong>Gram Panchayat (58,189 units)</strong>; political head is Gram Pradhan (directly elected); administrative secretary is Gram Panchayat Adhikari (VDO).
          <br>&bull; <em>Reservation Structure:</em> <strong>33% (1/3rd) mandatory reservation for women</strong> across all tiers and chairperson posts; constitutional quotas for SC and ST; 27% statutory reservation for OBCs.</span>
        <span class="lang-hi"><strong>ग्रामीण स्थानीय स्वशासन (त्रि-स्तरीय पंचायती राज):</strong>
          <br>&bull; <em>विधिक विकास:</em> मूल रूप से <strong>यूपी पंचायती राज अधिनियम 1947</strong> और <strong>क्षेत्र पंचायत व जिला पंचायत अधिनियम 1961</strong> द्वारा शासित; 73वें संविधान संशोधन के पश्चात <strong>1994</strong> में संशोधन अधिनियम द्वारा लागू।
          <br>&bull; <em>शीर्ष स्तर:</em> <strong>जिला पंचायत (75 इकाइयां)</strong>; राजनीतिक प्रमुख जिला पंचायत अध्यक्ष (वार्ड सदस्यों द्वारा अप्रत्यक्ष निर्वाचित); मुख्य कार्यपालक अधिकारी सीडीओ (CDO) / अपर मुख्य अधिकारी।
          <br>&bull; <em>मध्यवर्ती स्तर:</em> <strong>क्षेत्र पंचायत (826 इकाइयां)</strong>; राजनीतिक प्रमुख ब्लॉक प्रमुख; कार्यपालक अधिकारी बीडीओ (BDO)।
          <br>&bull; <em>ग्राम स्तर:</em> <strong>ग्राम पंचायत (58,189 इकाइयां)</strong>; प्रमुख ग्राम प्रधान (प्रत्यक्ष निर्वाचित); सचिव ग्राम पंचायत अधिकारी (VDO)।
          <br>&bull; <em>आरक्षण व्यवस्था:</em> सभी स्तरों पर महिलाओं हेतु <strong>33% (1/3) अनिवार्य आरक्षण</strong>; एससी एवं एसटी को जनसंख्या अनुपात में तथा ओबीसी को 27% आरक्षण।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Urban Local Governance (74th Amendment Act):</strong>
          <br>&bull; <em>17 Municipal Corporations (नगर निगम):</em> Lucknow, Kanpur, Agra, Varanasi, Prayagraj, Meerut, Bareilly, Aligarh, Moradabad, Gorakhpur, Saharanpur, Firozabad, Jhansi, Ayodhya, Mathura-Vrindavan, Ghaziabad, and <strong>Shahjahanpur (17th Nagar Nigam, formed in 2018)</strong>.
          <br>&bull; <em>Executive Head of Nagar Nigam:</em> Municipal Commissioner (नगर आयुक्त - IAS/PCS officer).
          <br>&bull; <em>Political Head:</em> Mayor (महापौर), directly elected by urban voters.
          <br>&bull; <em>Other Urban Bodies:</em> ~200 Nagar Palika Parishads (for medium towns) and ~545 Nagar Panchayats (for transitional rural-to-urban areas).</span>
        <span class="lang-hi"><strong>शहरी स्थानीय स्वशासन (74वां संविधान संशोधन):</strong>
          <br>&bull; <em>17 नगर निगम:</em> लखनऊ, कानपुर, आगरा, वाराणसी, प्रयागराज, मेरठ, बरेली, अलीगढ़, मुरादाबाद, गोरखपुर, सहारनपुर, फिरोजाबाद, झांसी, अयोध्या, मथुरा-वृंदावन, गाजियाबाद, तथा <strong>शाहजहांपुर (17वां नगर निगम, 2018 में गठित)</strong>।
          <br>&bull; <em>कार्यकारी प्रमुख:</em> नगर आयुक्त (IAS/PCS अधिकारी)।
          <br>&bull; <em>राजनीतिक प्रमुख:</em> महापौर (मेयर), नगर की जनता द्वारा प्रत्यक्ष निर्वाचित।
          <br>&bull; <em>अन्य शहरी निकाय:</em> ~200 नगर पालिका परिषदें (मध्यम शहरों हेतु) तथा ~545 नगर पंचायतें (संक्रमणकालीन कस्बों हेतु)।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 7: Constitutional & Statutory Commissions of UP -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">6. Constitutional &amp; Statutory Commissions of Uttar Pradesh</span>
    <span class="lang-hi">6. उत्तर प्रदेश के संवैधानिक एवं सांविधिक आयोग</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>UP Public Service Commission (UPPSC / उत्तर प्रदेश लोक सेवा आयोग):</strong>
          <br>&bull; <em>Established:</em> <strong>1 April 1937</strong> under Section 264 of Government of India Act 1935 (now Article 315 of Constitution).
          <br>&bull; <em>Headquarters:</em> <strong>Prayagraj (Allahabad)</strong>.
          <br>&bull; <em>First Chairman:</em> Sir D.L. Drake-Brockman.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश लोक सेवा आयोग (UPPSC):</strong>
          <br>&bull; <em>स्थापना:</em> भारत शासन अधिनियम 1935 की धारा 264 के तहत <strong>1 अप्रैल 1937</strong> (वर्तमान में संविधान का अनुच्छेद 315)।
          <br>&bull; <em>मुख्यालय:</em> <strong>प्रयागराज (इलाहाबाद)</strong>।
          <br>&bull; <em>प्रथम अध्यक्ष:</em> सर डी. एल. ड्रेक-ब्रॉकमैन।</span>
      </li>
      <li>
        <span class="lang-en"><strong>State Election Commission (राज्य निर्वाचन आयोग - Article 243K &amp; 243ZA):</strong>
          <br>&bull; <em>Established:</em> <strong>23 April 1994</strong> with headquarters at Lucknow.
          <br>&bull; <em>Mandate:</em> Superintendence, direction, and conduct of all elections to Panchayats and Urban Local Bodies in UP.
          <br>&bull; <em>First State Election Commissioner:</em> Manoj Kumar.</span>
        <span class="lang-hi"><strong>राज्य निर्वाचन आयोग (अनुच्छेद 243K एवं 243ZA):</strong>
          <br>&bull; <em>स्थापना:</em> <strong>23 अप्रैल 1994</strong> को लखनऊ मुख्यालय के साथ।
          <br>&bull; <em>दायित्व:</em> राज्य की त्रि-स्तरीय पंचायतों एवं नगर निकायों के स्वतंत्र एवं निष्पक्ष चुनाव संपन्न कराना।
          <br>&bull; <em>प्रथम राज्य निर्वाचन आयुक्त:</em> मनोज कुमार।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Institution of Lokayukta (लोकायुक्त संस्थान):</strong>
          <br>&bull; <em>Statutory Basis:</em> Established under the <em>UP Lokayukta and Up-Lokayuktas Act 1975</em>.
          <br>&bull; <em>Established:</em> Formed and entered into office on <strong>14 September 1977</strong>.
          <br>&bull; <em>First Lokayukta:</em> <strong>Justice Vishwambhar Dayal</strong> (1977-1982).
          <br>&bull; <em>Tenure:</em> Increased from 6 years to <strong>8 years</strong> by state amendment in 2012.</span>
        <span class="lang-hi"><strong>लोकायुक्त संस्थान:</strong>
          <br>&bull; <em>विधिक आधार:</em> <em>उत्तर प्रदेश लोकायुक्त एवं उप-लोकायुक्त अधिनियम 1975</em> के तहत स्थापित।
          <br>&bull; <em>प्रारंभ:</em> <strong>14 सितंबर 1977</strong> को विधिवत अस्तित्व में आया।
          <br>&bull; <em>प्रथम लोकायुक्त:</em> <strong>न्यायमूर्ति विश्वंभर दयाल</strong> (1977-1982)।
          <br>&bull; <em>कार्यकाल:</em> वर्ष 2012 के संशोधन द्वारा कार्यकाल 6 वर्ष से बढ़ाकर <strong>8 वर्ष</strong> किया गया।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP State Human Rights Commission (राज्य मानवाधिकार आयोग):</strong>
          <br>&bull; <em>Established:</em> Constituted on <strong>7 October 2002</strong> at Lucknow under Protection of Human Rights Act 1993.
          <br>&bull; <em>First Chairman:</em> Justice A.P. Mishra.</span>
        <span class="lang-hi"><strong>राज्य मानवाधिकार आयोग:</strong>
          <br>&bull; <em>स्थापना:</em> मानव अधिकार संरक्षण अधिनियम 1993 के तहत <strong>7 अक्टूबर 2002</strong> को लखनऊ में गठित।
          <br>&bull; <em>प्रथम अध्यक्ष:</em> न्यायमूर्ति ए. पी. मिश्रा।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP State Information Commission (राज्य सूचना आयोग):</strong>
          <br>&bull; <em>Established:</em> Formed in <strong>2005</strong> under the Right to Information Act 2005 at Lucknow.
          <br>&bull; <em>First Chief Information Commissioner:</em> Justice M.A. Khan.</span>
        <span class="lang-hi"><strong>राज्य सूचना आयोग:</strong>
          <br>&bull; <em>स्थापना:</em> सूचना का अधिकार अधिनियम 2005 के तहत <strong>वर्ष 2005</strong> में लखनऊ में गठित।
          <br>&bull; <em>प्रथम मुख्य सूचना आयुक्त:</em> न्यायमूर्ति एम. ए. खान।</span>
      </li>
      <li>
        <span class="lang-en"><strong>UP Subordinate Services Selection Commission (UPSSSC):</strong>
          <br>&bull; <em>Statutory Basis:</em> Established under UP Subordinate Services Selection Commission Act 2014 (UP Act No. 4 of 2014); conducts Group C and Group B (non-gazetted) recruitment; headquarters at Pikup Bhawan, Gomti Nagar, Lucknow.</span>
        <span class="lang-hi"><strong>उत्तर प्रदेश अधीनस्थ सेवा चयन आयोग (UPSSSC):</strong>
          <br>&bull; <em>विधिक आधार:</em> यूपी अधीनस्थ सेवा चयन आयोग अधिनियम 2014 के तहत स्थापित; समूह 'ग' एवं अराजपत्रित पदों की भर्ती हेतु नोडल संस्था; मुख्यालय पिकप भवन, गोमती नगर, लखनऊ।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 8: State Insignia & Official Symbols -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">7. State Insignia, Official Emblem &amp; State Symbols of UP</span>
    <span class="lang-hi">7. उत्तर प्रदेश का राजकीय चिह्न, प्रतीक एवं आधिकारिक भाषाएं</span>
  </div>
  <div class="content-block">
    <ul class="points-list">
      <li>
        <span class="lang-en"><strong>State Emblem / Official Seal (राजकीय चिह्न):</strong>
          <br>&bull; <em>Adopted:</em> Officially adopted in <strong>1938</strong>.
          <br>&bull; <em>Components &amp; Symbolism:</em>
            - <strong>Circular Shield (वृत्ताकार घेरा):</strong> Represents statehood and unity.
            - <strong>Bow and Arrow (धनुष-बाण):</strong> Symbolizes Lord Rama and cultural chivalry of the Awadh region.
            - <strong>Two Fishes (दो मछलियां):</strong> Derived from the historic emblem (Mahi-o-Maratib) of the Nawabs of Awadh, representing prosperity and Ganga-Jamuni Tehzeeb.
            - <strong>Three Wavy Lines (तीन तरंग रेखाएं):</strong> Depicts the holy confluence of River Ganga, River Yamuna, and mythical Saraswati at Prayagraj.</span>
        <span class="lang-hi"><strong>राजकीय चिह्न (आधिकारिक सील):</strong>
          <br>&bull; <em>स्वीकृति:</em> आधिकारिक रूप से <strong>1938</strong> में स्वीकृत किया गया।
          <br>&bull; <em>घटक एवं प्रतीक अर्थ:</em>
            - <strong>वृत्ताकार घेरा:</strong> राज्य की संप्रभुता एवं अखंडता का प्रतीक।
            - <strong>धनुष-बाण:</strong> भगवान श्री राम एवं अवध की सांस्कृतिक वीरता का प्रतीक।
            - <strong>दो मछलियां:</strong> अवध के नवाबों के ऐतिहासिक राजचिह्न (माही-ओ-मरातिब) से ली गई, जो समृद्धि और गंगा-जमुनी तहजीब की प्रतीक हैं।
            - <strong>तीन तरंग रेखाएं:</strong> प्रयागराज में गंगा, यमुना एवं अदृश्य सरस्वती के पावन संगम का द्योतक।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Official Languages (राजभाषाएं):</strong>
          <br>&bull; <em>First Official Language:</em> <strong>Hindi (in Devanagari script)</strong>, declared under the UP Official Language Act <strong>1951</strong>; made mandatory for all official correspondence in <strong>1968</strong>.
          <br>&bull; <em>Second Official Language:</em> <strong>Urdu</strong>, declared through the UP Official Language (Amendment) Act <strong>1989</strong>.</span>
        <span class="lang-hi"><strong>राजभाषाएं:</strong>
          <br>&bull; <em>प्रथम राजभाषा:</em> <strong>हिंदी (देवनागरी लिपि में)</strong>, यूपी राजभाषा अधिनियम <strong>1951</strong> के तहत घोषित; वर्ष <strong>1968</strong> से सभी शासकीय कार्यों में अनिवार्य।
          <br>&bull; <em>द्वितीय राजभाषा:</em> <strong>उर्दू</strong>, यूपी राजभाषा (संशोधन) अधिनियम <strong>1989</strong> द्वारा घोषित।</span>
      </li>
      <li>
        <span class="lang-en"><strong>Official State Natural Symbols:</strong>
          <br>&bull; <em>State Animal:</em> <strong>Barasingha / Swamp Deer (Rucervus duvaucelii)</strong>.
          <br>&bull; <em>State Bird:</em> <strong>Sarus Crane (Grus antigone)</strong>.
          <br>&bull; <em>State Tree:</em> <strong>Ashok (Saraca asoca)</strong>.
          <br>&bull; <em>State Flower:</em> <strong>Palash / Tesu (Butea monosperma)</strong> - declared on 4 January 2011 (replaced Brahmakamal post-Uttarakhand separation).
          <br>&bull; <em>State Aquatic Animal:</em> <strong>Gangetic Dolphin (Platanista gangetica)</strong> - declared in October 2023.</span>
        <span class="lang-hi"><strong>राजकीय प्राकृतिक प्रतीक:</strong>
          <br>&bull; <em>राजकीय पशु:</em> <strong>बारहसिंगा (दलदली हिरण)</strong>।
          <br>&bull; <em>राजकीय पक्षी:</em> <strong>सारस क्रेन (क्रौंच)</strong>।
          <br>&bull; <em>राजकीय वृक्ष:</em> <strong>अशोक</strong>।
          <br>&bull; <em>राजकीय पुष्प:</em> <strong>पलाश / टेसू</strong> - 4 जनवरी 2011 को अधिसूचित (उत्तराखंड विभाजन से पूर्व ब्रह्मकमल था)।
          <br>&bull; <em>राजकीय जलीय जीव:</em> <strong>गंगा डॉल्फिन</strong> - अक्टूबर 2023 में घोषित।</span>
      </li>
    </ul>
  </div>
</div>

<!-- Card 9: Master Directory of Political & Constitutional Firsts -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">8. Master Directory: Constitutional &amp; Administrative Firsts in Uttar Pradesh</span>
    <span class="lang-hi">8. उत्तर प्रदेश में संवैधानिक एवं प्रशासनिक प्रथम हस्तियों की महा-तालिका</span>
  </div>
  <div class="content-block">
    <table class="comparison-table">
      <thead>
        <tr>
          <th>
            <span class="lang-en">Constitutional Post / Office</span>
            <span class="lang-hi">संवैधानिक पद / संस्था</span>
          </th>
          <th>
            <span class="lang-en">First Dignitary</span>
            <span class="lang-hi">प्रथम पदासीन हस्ती</span>
          </th>
          <th>
            <span class="lang-en">Exam Significance &amp; Tenures</span>
            <span class="lang-hi">परीक्षा महत्व एवं कार्यकाल</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Governor (Post-Independence)</span>
            <span class="lang-hi">राज्यपाल (स्वतंत्रता बाद)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sarojini Naidu</strong></span>
            <span class="lang-hi"><strong>श्रीमती सरोजिनी नायडू</strong></span>
          </td>
          <td>
            <span class="lang-en">15 Aug 1947 - 2 Mar 1949; 1st woman Governor of any Indian state</span>
            <span class="lang-hi">15 अगस्त 1947 - 2 मार्च 1949; भारत के किसी भी राज्य की प्रथम महिला राज्यपाल</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chief Minister (1st CM)</span>
            <span class="lang-hi">मुख्यमंत्री (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Pt. Govind Ballabh Pant</strong></span>
            <span class="lang-hi"><strong>पं. गोविंद बल्लभ पंत</strong></span>
          </td>
          <td>
            <span class="lang-en">Premier 1937/1946; 1st CM of UP (26 Jan 1950 - 1954); Bharat Ratna 1957</span>
            <span class="lang-hi">1937/1946 प्रीमियर; यूपी के प्रथम मुख्यमंत्री (1950-1954); भारत रत्न 1957</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Woman Chief Minister (1st Woman CM)</span>
            <span class="lang-hi">महिला मुख्यमंत्री (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sucheta Kripalani</strong></span>
            <span class="lang-hi"><strong>श्रीमती सुचेता कृपलानी</strong></span>
          </td>
          <td>
            <span class="lang-en">1963-1967; 1st woman Chief Minister in Indian history</span>
            <span class="lang-hi">1963-1967; भारतीय इतिहास में किसी भी राज्य की प्रथम महिला मुख्यमंत्री</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Speaker, Legislative Assembly</span>
            <span class="lang-hi">विधानसभा अध्यक्ष (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Rajarshi Purushottam Das Tandon</strong></span>
            <span class="lang-hi"><strong>राजर्षि पुरुषोत्तम दास टंडन</strong></span>
          </td>
          <td>
            <span class="lang-en">1937-1950; Bharat Ratna 1961</span>
            <span class="lang-hi">1937-1950; 1961 में भारत रत्न से सम्मानित</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chairman, Legislative Council</span>
            <span class="lang-hi">विधान परिषद सभापति (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sir Dr. Sita Ram</strong> (Pre-Ind.) / <strong>Chandra Bhal</strong> (Post-Ind.)</span>
            <span class="lang-hi"><strong>सर डॉ. सीता राम</strong> (स्वतंत्रता पूर्व) / <strong>चंद्र भाल</strong> (स्वतंत्रता बाद)</span>
          </td>
          <td>
            <span class="lang-en">Chandra Bhal served 1949-1958</span>
            <span class="lang-hi">चंद्र भाल ने 1949 से 1958 तक सेवा की</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chief Justice, High Court</span>
            <span class="lang-hi">मुख्य न्यायाधीश, उच्च न्यायालय</span>
          </td>
          <td>
            <span class="lang-en"><strong>Sir Walter Morgan</strong> (1866) / <strong>Justice B. Malik</strong> (1947)</span>
            <span class="lang-hi"><strong>सर वाल्टर मॉर्गन</strong> (1866) / <strong>न्यायमूर्ति बिधुभूषण मलिक</strong> (1947)</span>
          </td>
          <td>
            <span class="lang-en">Sir Shah Muhammad Sulaiman was 1st Indian CJ (1932)</span>
            <span class="lang-hi">सर शाह मुहम्मद सुलेमान प्रथम भारतीय मुख्य न्यायाधीश थे (1932)</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Lokayukta of UP</span>
            <span class="lang-hi">उत्तर प्रदेश के लोकायुक्त (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Justice Vishwambhar Dayal</strong></span>
            <span class="lang-hi"><strong>न्यायमूर्ति विश्वंभर दयाल</strong></span>
          </td>
          <td>
            <span class="lang-en">Appointed 1977 under UP Lokayukta Act 1975</span>
            <span class="lang-hi">यूपी लोकायुक्त अधिनियम 1975 के तहत 1977 में नियुक्त</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">State Election Commissioner</span>
            <span class="lang-hi">राज्य निर्वाचन आयुक्त (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Manoj Kumar</strong></span>
            <span class="lang-hi"><strong>मनोज कुमार</strong></span>
          </td>
          <td>
            <span class="lang-en">Appointed upon formation of commission in 1994</span>
            <span class="lang-hi">1994 में आयोग के गठन पर नियुक्त</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Chief Information Commissioner</span>
            <span class="lang-hi">मुख्य सूचना आयुक्त (प्रथम)</span>
          </td>
          <td>
            <span class="lang-en"><strong>Justice M.A. Khan</strong></span>
            <span class="lang-hi"><strong>न्यायमूर्ति एम. ए. खान</strong></span>
          </td>
          <td>
            <span class="lang-en">Appointed under RTI Act 2005</span>
            <span class="lang-hi">सूचना का अधिकार अधिनियम 2005 के तहत नियुक्त</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Card 10: Rapid Revision Matrix & UPSSSC Exam Traps -->
<div class="card-premium">
  <div class="card-title">
    <span class="lang-en">9. Rapid Revision Matrix: One-Liner Exam Facts &amp; UPSSSC Traps</span>
    <span class="lang-hi">9. त्वरित पुनरीक्षण सारणी: परीक्षा उपयोगी तथ्य एवं यूपीएसएसएससी ट्रैप</span>
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
            <span class="lang-en">Correct Concept &amp; Precision Answer</span>
            <span class="lang-hi">सही तथ्य एवं सटीक उत्तर</span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>
            <span class="lang-en">Anglo-Indian Assembly Nomination</span>
            <span class="lang-hi">विधानसभा में एंग्लो-इंडियन मनोनयन</span>
          </td>
          <td>
            <span class="lang-en">Abolished by <strong>104th Constitutional Amendment Act 2019</strong>. Current assembly strength is exactly <strong>403 elected members</strong>.</span>
            <span class="lang-hi"><strong>104वें संविधान संशोधन 2019</strong> द्वारा समाप्त। वर्तमान में सदस्य संख्या ठीक <strong>403 निर्वाचित सदस्य</strong> है।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">ST Reserved Assembly Seats</span>
            <span class="lang-hi">विधानसभा में एसटी आरक्षित सीटें</span>
          </td>
          <td>
            <span class="lang-en">Only <strong>2 seats</strong>: <strong>Obra</strong> and <strong>Duddhi</strong> (both in Sonbhadra district).</span>
            <span class="lang-hi">केवल <strong>2 सीटें</strong>: <strong>ओबरा</strong> एवं <strong>दुद्धी</strong> (दोनों सोनभद्र जिले में)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Lok Sabha ST Reserved Seats</span>
            <span class="lang-hi">लोकसभा में एसटी आरक्षित सीटें</span>
          </td>
          <td>
            <span class="lang-en"><strong>0 seats</strong> in UP (out of 80 seats, 17 are reserved for SC, none for ST).</span>
            <span class="lang-hi">यूपी में <strong>0 सीटें</strong> (80 सीटों में से 17 एससी हेतु हैं, एसटी हेतु शून्य)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Women Reservation in Local Bodies</span>
            <span class="lang-hi">स्थानीय निकायों में महिला आरक्षण</span>
          </td>
          <td>
            <span class="lang-en"><strong>33% (1/3rd)</strong> in UP (Trap: It is NOT 50% in UP, unlike Bihar or MP).</span>
            <span class="lang-hi">यूपी में <strong>33% (1/3)</strong> (ट्रैप: बिहार या मप्र की तरह यूपी में 50% नहीं है)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">17th Municipal Corporation</span>
            <span class="lang-hi">17वां नगर निगम</span>
          </td>
          <td>
            <span class="lang-en"><strong>Shahjahanpur</strong>, constituted in April 2018.</span>
            <span class="lang-hi"><strong>शाहजहांपुर</strong>, अप्रैल 2018 में 17वें नगर निगम के रूप में गठित।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Lokayukta Tenure</span>
            <span class="lang-hi">लोकायुक्त का कार्यकाल</span>
          </td>
          <td>
            <span class="lang-en"><strong>8 years</strong> (amended from 6 years in 2012).</span>
            <span class="lang-hi"><strong>8 वर्ष</strong> (वर्ष 2012 में 6 वर्ष से बढ़ाकर 8 वर्ष किया गया)।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">High Court Origin &amp; Shift</span>
            <span class="lang-hi">उच्च न्यायालय का उद्गम व स्थानांतरण</span>
          </td>
          <td>
            <span class="lang-en">Formed at <strong>Agra on 17 March 1866</strong>; shifted to <strong>Allahabad in 1869</strong>.</span>
            <span class="lang-hi"><strong>17 मार्च 1866 को आगरा</strong> में स्थापना; <strong>1869 में इलाहाबाद</strong> स्थानांतरण।</span>
          </td>
        </tr>
        <tr>
          <td>
            <span class="lang-en">Urdu 2nd Official Language Year</span>
            <span class="lang-hi">उर्दू द्वितीय राजभाषा वर्ष</span>
          </td>
          <td>
            <span class="lang-en"><strong>1989</strong> (UP Official Language Amendment Act 1989).</span>
            <span class="lang-hi"><strong>1989</strong> (यूपी राजभाषा संशोधन अधिनियम 1989)।</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

</div>"""

def main():
    target_file = os.path.join("upsssc-up-gk", "polity-and-administration", "index.html")
    with open(target_file, "r", encoding="utf-8") as f:
        html = f.read()

    pattern = re.compile(r'<div class="tab-content" id="tab-theory"[^>]*>.*?</div>\s*(?=<div class="tab-content" id="tab-practice")', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print("ERROR: Could not locate tab-theory boundary!")
        return

    new_theory = build_polity_theory_html().strip()
    updated_html = html[:match.start()] + new_theory + "\n" + html[match.end():]

    with open(target_file, "w", encoding="utf-8") as f:
        f.write(updated_html)

    print(f"Successfully enriched {target_file} with comprehensive pointwise facts!")

if __name__ == "__main__":
    main()
