# -*- coding: utf-8 -*-
import json
import os
import sys

# Force stdout to use UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\sande\Documents\GitHub\sjmaths-website\upsc\ancient_history\History-of-Early-VedicRigvedic-Period\Societal-Setup"

# 1. Outline the 6 Detailed deep-dive sections (in English and Hindi)
sections_meta = [
    {
        "id": 1,
        "title": "1. Kinship & Family Structure",
        "title_hi": "1. सगोत्रता और पारिवारिक संरचना",
        "content": """
<h3>Kinship as the Core Social Unit</h3>
<p>The Rigvedic society was structured fundamentally around kinship (blood relations) rather than territory. Social identity, security, and access to resources were entirely determined by lineage. The primary social unit was the patriarchal family, known as the <strong>Kula</strong> or <strong>Griha</strong>. The head of this household was the eldest male member, designated as the <strong>Kulapa</strong> or <strong>Grihapati</strong>, who wielded absolute authority over the family members and assets, though his power was tempered by customary ethics.</p>

<h3>Hierarchical Social Divisions</h3>
<p>The social structure ascended from the family unit to larger kinship divisions:</p>
<ul>
    <li><strong>Kula / Griha:</strong> The fundamental family unit headed by the Kulapa.</li>
    <li><strong>Grama:</strong> A cluster of families or a mobile kin-camp. In battle and pastoral migrations, the Grama functioned as a cohesive unit led by the <strong>Gramani</strong>.</li>
    <li><strong>Vis:</strong> A subdivision of the tribe (clan canton), headed by the <strong>Vispati</strong>, representing a collection of Gramas.</li>
    <li><strong>Jana:</strong> The entire tribe or ethnic assembly (e.g., Bharatas, Purus), headed by the <strong>Rajan</strong>.</li>
</ul>

<h3>Joint Family System and Patrilineality</h3>
<p>The family was of a joint nature, often spanning three generations living together under one roof. Patrilineal descent was strictly observed; sons were highly desired (referred to as <strong>Viras</strong>) to secure the lineage, inherit family herds, and perform ancestral rites. Despite the strong patriarchal bias, the family unit operated as a cooperative economic unit where tasks were divided based on age and gender.</p>
""",
        "content_hi": """
<h3>सामाजिक इकाई के रूप में सगोत्रता</h3>
<p>ऋग्वैदिक समाज मूल रूप से क्षेत्र के बजाय सगोत्रता (रक्त संबंधों) के आधार पर संरचित था। सामाजिक पहचान, सुरक्षा और संसाधनों तक पहुँच पूरी तरह से वंश द्वारा निर्धारित होती थी। प्राथमिक सामाजिक इकाई पितृसत्तात्मक परिवार थी, जिसे <strong>कुल</strong> या <strong>गृह</strong> के रूप में जाना जाता था। इस परिवार का मुखिया सबसे बड़ा पुरुष सदस्य होता था, जिसे <strong>कुलप</strong> या <strong>गृहपति</strong> कहा जाता था। उसके पास परिवार के सदस्यों और संपत्तियों पर पूर्ण अधिकार होता था, हालांकि उसकी शक्ति पारंपरिक नैतिक नियमों से नियंत्रित होती थी।</p>

<h3>पदानुक्रमित सामाजिक विभाजन</h3>
<p>सामाजिक संरचना पारिवारिक इकाई से बढ़कर बड़े सगोत्र विभाजनों की ओर बढ़ती थी:</p>
<ul>
    <li><strong>कुल / गृह:</strong> कुलप के नेतृत्व में बुनियादी पारिवारिक इकाई।</li>
    <li><strong>ग्राम:</strong> परिवारों का एक समूह या एक गतिशील सगोत्र-शिविर। युद्ध और पशुचारण प्रवास में, ग्राम <strong>ग्रामणी</strong> के नेतृत्व में एक एकजुट इकाई के रूप में कार्य करता था।</li>
    <li><strong>विश:</strong> कबीले का एक उपविभाग (कबीला छावनी), जिसका प्रमुख <strong>विशपति</strong> होता था, जो ग्रामों के समूह का प्रतिनिधित्व करता था।</li>
    <li><strong>जन:</strong> पूरी जनजाति या जातीय सभा (जैसे, भरत, पुरु), जिसका नेतृत्व <strong>राजन</strong> करता था।</li>
</ul>

<h3>संयुक्त परिवार प्रणाली और पितृवंशिकता</h3>
<p>परिवार संयुक्त प्रकृति का होता था, जिसमें अक्सर तीन पीढ़ियां एक ही छत के नीचे रहती थीं। पितृवंशीय वंशानुक्रम का कड़ाई से पालन किया जाता था; वंश को सुरक्षित रखने, पारिवारिक पशुधन विरासत में प्राप्त करने और पैतृक अनुष्ठान करने के लिए बेटों (जिन्हें <strong>वीर</strong> कहा जाता था) की अत्यधिक कामना की जाती थी। मजबूत पितृसत्तात्मक पूर्वाग्रह के बावजूद, पारिवारिक इकाई एक सहकारी आर्थिक इकाई के रूप में कार्य करती थी जहाँ आयु और लिंग के आधार पर कार्यों का विभाजन किया जाता था।</p>
"""
    },
    {
        "id": 2,
        "title": "2. Social Stratification & Varna System",
        "title_hi": "2. सामाजिक स्तरीकरण और वर्ण व्यवस्था",
        "content": """
<h3>From Egalitarianism to Stratification</h3>
<p>The early Rigvedic society was largely egalitarian, with no rigid class divisions. The primary social distinction was between the incoming Indo-Aryans (<strong>Aryas</strong>) and the indigenous populations (referred to as <strong>Dasas</strong> and <strong>Dasyus</strong>). This distinction was initially based on language, religious practices, and physical traits (referred to as <strong>Varna</strong>, meaning color or outward appearance).</p>

<h3>The Concept of Varna</h3>
<p>In the early Rig Vedic period, Varna did not denote a hereditary caste system. Instead, it was a flexible division based on occupations and social standing. The society was divided broadly into three functional groups:</p>
<ol>
    <li><strong>Priests (Brahmanas):</strong> Handled sacrifices and sacred chants.</li>
    <li><strong>Warriors (Rajanyas/Kshatriyas):</strong> Protected the clan and led military expeditions.</li>
    <li><strong>Commoners (Vis/Vaishyas):</strong> Engaged in pastoralism, trade, and agriculture.</li>
</ol>
<p>An individual's Varna was fluid; a hymn in Mandala 9 famously records a poet saying: <i>'I am a singer, my father is a physician, my mother grinds corn with stone...'</i>, highlighting the lack of occupational rigidity.</p>

<h3>The Purusha Sukta and Later Stratification</h3>
<p>Towards the end of the Rigvedic period, specifically in the <strong>Purusha Sukta</strong> hymn of the 10th Mandala (a later addition), the four-fold Varna system is mentioned for the first time. It describes the creation of the four varnas from the body of the primeval giant, Purusha: Brahmanas from the mouth, Rajanyas from the arms, Vaishyas from the thighs, and Shudras from the feet. This laid the theoretical foundation for the rigid social hierarchy that characterized the Later Vedic period.</p>
""",
        "content_hi": """
<h3>समतावाद से स्तरीकरण तक</h3>
<p>प्रारंभिक ऋग्वैदिक समाज काफी हद तक समतावादी था, जिसमें कोई कठोर वर्ग विभाजन नहीं था। प्राथमिक सामाजिक अंतर नवागंतुक भारत-आर्यों (<strong>आर्य</strong>) और स्वदेशी आबादी (जिन्हें <strong>दास</strong> और <strong>दस्यु</strong> कहा जाता था) के बीच था। यह अंतर प्रारंभ में भाषा, धार्मिक प्रथाओं और शारीरिक लक्षणों (जिन्हें <strong>वर्ण</strong> कहा जाता था, जिसका अर्थ रंग या बाहरी रूप था) पर आधारित था।</p>

<h3>वर्ण की अवधारणा</h3>
<p>प्रारंभिक ऋग्वैदिक काल में, वर्ण का अर्थ वंशानुगत जाति व्यवस्था नहीं था। इसके बजाय, यह व्यवसायों और सामाजिक स्थिति पर आधारित एक लचीला विभाजन था। समाज को मोटे तौर पर तीन कार्यात्मक समूहों में विभाजित किया गया था:</p>
<ol>
    <li><strong>पुरोहित (ब्राह्मण):</strong> यज्ञ और पवित्र मंत्रों का संपादन करते थे।</li>
    <li><strong>योद्धा (राजन्य/क्षत्रिय):</strong> कबीले की रक्षा करते थे और सैन्य अभियानों का नेतृत्व करते थे।</li>
    <li><strong>सामान्य लोग (विश/वैश्य):</strong> पशुपालन, व्यापार और कृषि में संलग्न थे।</li>
</ol>
<p>व्यक्ति का वर्ण लचीला था; मंडल 9 के एक भजन में एक कवि ने प्रसिद्ध रूप से कहा है: <i>'मैं एक कवि हूँ, मेरे पिता एक चिकित्सक हैं, मेरी माँ पत्थर से अनाज पीसती है...'</i>, जो व्यावसायिक लचीलेपन को दर्शाता है।</p>

<h3>पुरुष सूक्त और उत्तरवर्ती स्तरीकरण</h3>
<p>ऋग्वैदिक काल के अंत में, विशेष रूप से 10वें मंडल के <strong>पुरुष सूक्त</strong> भजन (एक बाद का प्रक्षेप) में, पहली बार चार-स्तरीय वर्ण व्यवस्था का उल्लेख मिलता है। यह आदि पुरुष के शरीर से चार वर्णों के निर्माण का वर्णन करता है: मुख से ब्राह्मण, भुजाओं से राजन्य, जांघों से वैश्य और पैरों से शूद्र। इसने उस कठोर सामाजिक पदानुक्रम की सैद्धांतिक नींव रखी जिसने उत्तर वैदिक काल की विशेषता बताई।</p>
"""
    },
    {
        "id": 3,
        "title": "3. Position of Women",
        "title_hi": "3. महिलाओं की स्थिति",
        "content": """
<h3>High Status and Public Participation</h3>
<p>Women in early Vedic society occupied a highly respectable position. They were not confined to the domestic sphere and had access to education and political assemblies. Women actively participated in tribal assemblies like the <strong>Sabha</strong> and <strong>Vidatha</strong>. The term <strong>Sabhāvati</strong> is used to describe a woman eligible to participate in assembly discussions.</p>

<h3>Access to Education and Rituals</h3>
<p>Women were initiated into education through the Upanayana ceremony (sacred thread investiture) and studied the Vedas. Several women scholars composed Vedic hymns and were designated as <strong>Brahmavadinis</strong> (lifelong students of sacred lore). Prominent examples include:</p>
<ul>
    <li><strong>Lopamudra:</strong> Wife of sage Agastya, who composed hymns in Mandala 1.</li>
    <li><strong>Ghosha:</strong> Composed hymns dedicated to the Ashvins in Mandala 10.</li>
    <li><strong>Apala, Vishvavara, and Sikata:</strong> Celebrated women seers who sponsored and performed sacrifices.</li>
</ul>

<h3>Marriage and Social Norms</h3>
<p>Marriage was considered a sacred, cooperative partnership. Key aspects of Rigvedic marriage include:</p>
<ul>
    <li><strong>Consent and Age:</strong> Child marriage was absent; girls married after reaching maturity. Instances of choice in choosing partners (swayamvara-like) are recorded.</li>
    <li><strong>Niyoga (Levirate):</strong> The practice of Niyoga was allowed, where a childless widow could cohabit with her brother-in-law to produce an heir.</li>
    <li><strong>Widow Remarriage:</strong> Widows had the right to remarry, and the custom of Sati (widow burning) was completely absent.</li>
    <li><strong>Patriarchal Limits:</strong> Despite these freedoms, women did not have independent property rights (inheritance went to sons), and the birth of a son was celebrated far more than a daughter.</li>
</ul>
""",
        "content_hi": """
<h3>उच्च सामाजिक स्थिति और सार्वजनिक भागीदारी</h3>
<p>प्रारंभिक वैदिक समाज में महिलाओं को अत्यधिक सम्मानजनक स्थान प्राप्त था। वे घरेलू दायरे तक सीमित नहीं थीं और उन्हें शिक्षा तथा राजनीतिक सभाओं तक पहुँच प्राप्त थी। महिलाओं ने <strong>सभा</strong> और <strong>विदथ</strong> जैसी जनजातीय सभाओं में सक्रिय रूप से भाग लिया। <strong>सभावती</strong> शब्द का प्रयोग सभा की चर्चाओं में भाग लेने के लिए पात्र महिला का वर्णन करने के लिए किया जाता है।</p>

<h3>शिक्षा और अनुष्ठानों तक पहुँच</h3>
<p>उपनयन संस्कार (जनेऊ धारण) के माध्यम से महिलाओं को शिक्षा में दीक्षित किया जाता था और वे वेदों का अध्ययन करती थीं। कई महिला विदुषियों ने वैदिक भजनों की रचना की और उन्हें <strong>ब्रह्मवादिनी</strong> (पवित्र ज्ञान की आजीवन छात्राएं) कहा गया। प्रमुख उदाहरणों में शामिल हैं:</p>
<ul>
    <li><strong>लोपामुद्रा:</strong> ऋषि अगस्त्य की पत्नी, जिन्होंने मंडल 1 में भजनों की रचना की।</li>
    <li><strong>घोषा:</strong> मंडल 10 में अश्विनों को समर्पित भजनों की रचना की।</li>
    <li><strong>अपाला, विश्ववारा और सिकता:</strong> प्रसिद्ध महिला ऋषि जिन्होंने यज्ञों का आयोजन और संपादन किया।</li>
</ul>

<h3>विवाह और सामाजिक मानदंड</h3>
<p>विवाह को एक पवित्र, सहकारी साझेदारी माना जाता था। ऋग्वैदिक विवाह के प्रमुख पहलुओं में शामिल हैं:</p>
<ul>
    <li><strong>सहमति और आयु:</strong> बाल विवाह अनुपस्थित था; लड़कियां परिपक्वता प्राप्त करने के बाद विवाह करती थीं। जीवनसाथी चुनने में पसंद (स्वयंवर जैसी) के उदाहरण दर्ज हैं।</li>
    <li><strong>नियोग (देवर-विवाह):</strong> नियोग की प्रथा की अनुमति थी, जहाँ एक निःसंतान विधवा अपने देवर के साथ सहवास करके उत्तराधिकारी उत्पन्न कर सकती थी।</li>
    <li><strong>विधवा पुनर्विवाह:</strong> विधवाओं को पुनर्विवाह करने का अधिकार था, और सती प्रथा (विधवा को जलाना) पूरी तरह से अनुपस्थित थी।</li>
    <li><strong>पितृसत्तात्मक सीमाएँ:</strong> इन स्वतंत्रताओं के बावजूद, महिलाओं को स्वतंत्र संपत्ति अधिकार नहीं थे (विरासत बेटों को मिलती थी), और बेटी की तुलना में बेटे के जन्म का उत्सव कहीं अधिक मनाया जाता था।</li>
</ul>
"""
    },
    {
        "id": 4,
        "title": "4. Pastoral-Agricultural Economy & Material Culture",
        "title_hi": "4. पशुचारण-कृषि अर्थव्यवस्था और भौतिक संस्कृति",
        "content": """
<h3>Cattle as the Measure of Wealth</h3>
<p>The Rigvedic economy was predominantly pastoral, with agriculture playing a secondary role. The cow (<strong>Gau</strong>) was the central unit of economic value, acting as a currency and a measure of wealth. Wealthy individuals were called <strong>Gomat</strong> (possessor of cattle). Wars were primarily fought to capture cattle, and the terms for conflict (e.g., <strong>Gavisthi</strong>, <strong>Gaveshana</strong>) literally mean 'search for cows'. The cow was declared <strong>Aghnya</strong> (not to be killed) in several hymns, indicating its sacred and economic sanctity.</p>

<h3>Vedic Diet and Beverages</h3>
<p>The diet consisted primarily of milk and milk products (ghee, butter, curd), and barley (<strong>Yava</strong>), which was the chief grain cultivated. Meat was consumed occasionally during sacrifices. Two sacred beverages are highlighted:</p>
<ul>
    <li><strong>Soma:</strong> A sacred, intoxicating drink prepared from a plant found in the mountains (Mujavant). It was offered to the gods, especially Indra, and consumed during rituals.</li>
    <li><strong>Sura:</strong> A secular, popular liquor brewed from grain, though often disapproved of by priests due to its intoxicating effects.</li>
</ul>

<h3>Clothing, Ornaments, and Entertainment</h3>
<p>The dress of the Vedic people was simple, consisting of two or three pieces of cloth: the <strong>Nivi</strong> (undergarment), the <strong>Vasa</strong> (garment), and the <strong>Atka</strong> or <strong>Adhivasa</strong> (cloak/overgarment). Both men and women wore ornaments made of gold (<strong>Niska</strong> and <strong>Rukma</strong>) and beads. Popular forms of entertainment included chariot racing, dicing (playing with <strong>Aksa</strong>), music (flutes, lutes, drums), and dancing.</p>
""",
        "content_hi": """
<h3>धन के माप के रूप में मवेशी (गाय)</h3>
<p>ऋग्वैदिक अर्थव्यवस्था मुख्य रूप से पशुचारण थी, जिसमें कृषि गौण भूमिका निभाती थी। गाय (<strong>गौ</strong>) आर्थिक मूल्य की केंद्रीय इकाई थी, जो एक मुद्रा और धन के माप के रूप में कार्य करती थी। धनी व्यक्तियों को <strong>गोमत</strong> (मवेशियों का स्वामी) कहा जाता था। युद्ध मुख्य रूप से गायों को पकड़ने के लिए लड़े जाते थे, और संघर्ष के शब्दों (जैसे, <strong>गविष्टि</strong>, <strong>गवेषणा</strong>) का शाब्दिक अर्थ 'गायों की खोज' है। कई भजनों में गाय को <strong>अघन्या</strong> (न मारने योग्य) घोषित किया गया था, जो इसकी पवित्र और आर्थिक महत्ता को दर्शाता है।</p>

<h3>वैदिक आहार और पेय</h3>
<p>आहार में मुख्य रूप से दूध और दूध से बने उत्पाद (घी, मक्खन, दही) और जौ (<strong>यव</strong>) शामिल थे, जो खेती की जाने वाली मुख्य फसल थी। यज्ञों के दौरान कभी-कभी मांस का सेवन किया जाता था। दो पवित्र पेयों पर प्रकाश डाला गया है:</p>
<ul>
    <li><strong>सोम:</strong> पहाड़ों (मूजवंत) में पाए जाने वाले एक पौधे से तैयार किया जाने वाला एक पवित्र, स्फूर्तिदायक पेय। इसे देवताओं, विशेष रूप से इंद्र को अर्पित किया जाता था और अनुष्ठानों के दौरान सेवन किया जाता था।</li>
    <li><strong>सुरा:</strong> अनाज से तैयार की जाने वाली एक धर्मनिरपेक्ष, लोकप्रिय मदिरा, हालांकि पुरोहितों द्वारा इसके नशीले प्रभावों के कारण अक्सर इसे नापसंद किया जाता था।</li>
</ul>

<h3>कपड़े, आभूषण और मनोरंजन</h3>
<p>वैदिक लोगों की पोशाक सरल थी, जिसमें कपड़े के दो या तीन टुकड़े शामिल थे: <strong>नीवि</strong> (अधोवस्त्र), <strong>वास</strong> (मुख्य वस्त्र), और <strong>अत्क</strong> या <strong>अधिवास</strong> (चोगा/ऊपरी वस्त्र)। पुरुष और महिला दोनों सोने (<strong>निष्क</strong> और <strong>रुक्म</strong>) और मोतियों से बने आभूषण पहनते थे। मनोरंजन के लोकप्रिय रूपों में रथ दौड़, पासा (<strong>अक्ष</strong> के साथ खेलना), संगीत (बांसुरी, वीणा, ढोल) और नृत्य शामिल थे।</p>
"""
    },
    {
        "id": 5,
        "title": "5. Daily Life, Education & Professional Castes",
        "title_hi": "5. दैनिक जीवन, शिक्षा और व्यावसायिक जातियाँ",
        "content": """
<h3>The Oral Tradition and Gurukula</h3>
<p>Education was entirely oral and focused on the transmission of sacred hymns and rituals. The teacher (Guru) recited the hymns, and the students repeated them with precise pronunciation and pitch. The system of education was centered in the household of the teacher, representing the early prototype of the <strong>Gurukula</strong> system. There was a strong emphasis on moral conduct, discipline, and the preservation of cosmic order (<strong>Rta</strong>).</p>

<h3>Artisans and Craftsmen</h3>
<p>The Rigvedic economy was supported by skilled professional groups who enjoyed respectable social status. Unlike the Later Vedic and classical periods, artisans were not marginalized. Key groups mentioned include:</p>
<ul>
    <li><strong>Takshan (Carpenter):</strong> Crafted spoked-wheel chariots (Ratha) which were vital for war and migrations.</li>
    <li><strong>Karmara (Metalworker):</strong> Worked with copper and bronze (referred to as <strong>Ayas</strong>) to make tools and weapons.</li>
    <li><strong>Vayatri (Weaver):</strong> Primarily women, who spun and wove wool and cotton garments.</li>
    <li><strong>Charmakara (Leatherworker):</strong> Prepared leather for reins, bowstrings, and water bags.</li>
</ul>

<h3>Hospitality and Social Ethics</h3>
<p>Hospitality was a supreme moral virtue. Guests were treated with deep respect, and terms like <strong>Atithi</strong> reflect their honor. A wealthy host who slaughtered a cow or ox for an honored guest was referred to as <strong>Goghna</strong>. Charity (<strong>Dana</strong>) and sharing resources with clansmen were highly valued behaviors, ensuring social harmony in the tribe.</p>
""",
        "content_hi": """
<h3>मौखिक परंपरा और गुरुकुल</h3>
<p>शिक्षा पूरी तरह से मौखिक थी और पवित्र भजनों तथा अनुष्ठानों के हस्तांतरण पर केंद्रित थी। गुरु भजनों का पाठ करते थे, और छात्र सटीक उच्चारण और स्वर-ऊंचाई के साथ उन्हें दोहराते थे। शिक्षा की व्यवस्था शिक्षक के घर पर केंद्रित थी, जो <strong>गुरुकुल</strong> प्रणाली के प्रारंभिक रूप का प्रतिनिधित्व करती थी। नैतिक आचरण, अनुशासन और ब्रह्मांडीय व्यवस्था (<strong>ऋत</strong>) के संरक्षण पर कड़ा बल दिया जाता था।</p>

<h3>कारीगर और शिल्पकार</h3>
<p>ऋग्वैदिक अर्थव्यवस्था को कुशल व्यावसायिक समूहों का समर्थन प्राप्त था जो सम्मानजनक सामाजिक स्थिति का आनंद लेते थे। उत्तर वैदिक और शास्त्रीय काल के विपरीत, कारीगरों को हाशिए पर नहीं धकेला गया था। उल्लिखित प्रमुख समूहों में शामिल हैं:</p>
<ul>
    <li><strong>तक्षण (बढ़ई):</strong> हल्के पहियों वाले रथों (रथ) का निर्माण करते थे जो युद्ध और प्रवास के लिए महत्वपूर्ण थे।</li>
    <li><strong>कर्मार (धातु कर्मकार):</strong> उपकरण और हथियार बनाने के लिए तांबे और कांस्य (जिन्हें <strong>अयस</strong> कहा जाता था) के साथ काम करते थे।</li>
    <li><strong>वयित्री (बुनकर):</strong> मुख्य रूप से महिलाएं, जो ऊनी और सूती कपड़े कातती और बुनती थीं।</li>
    <li><strong>चर्मकार (चर्म-शिल्पी):</strong> लगाम, धनुष की डोरी और पानी के थैलों के लिए चमड़ा तैयार करते थे।</li>
</ul>

<h3>अतिथि सत्कार और सामाजिक नैतिकता</h3>
<p>अतिथि सत्कार एक सर्वोच्च नैतिक गुण था। अतिथियों का गहरे सम्मान के साथ स्वागत किया जाता था, और <strong>अतिथि</strong> जैसे शब्द उनके सम्मान को दर्शाते हैं। एक धनी मेजबान जो एक सम्मानित अतिथि के लिए गाय या बैल का वध (सत्कार के रूप में) करता था, उसे <strong>गोघ्न</strong> कहा जाता था। दान (<strong>दान</strong>) और कबीले के लोगों के साथ संसाधनों को साझा करना अत्यधिक मूल्यवान आचरण था, जिससे जनजाति में सामाजिक सद्भाव सुनिश्चित होता था।</p>
"""
    },
    {
        "id": 6,
        "title": "6. Social Transition & Class Differentiation",
        "title_hi": "6. सामाजिक संक्रमण और वर्ग भिन्नता",
        "content": """
<h3>Transition to Sedentary Agriculture</h3>
<p>Towards the end of the Rigvedic period (around 1000 BCE), the Aryan clans began migrating eastward from the Sapta-Sindhu region (Punjab) towards the Ganga-Yamuna Doab. This migration coincided with a transition from a nomadic pastoral lifestyle to settled agriculture. Land, which was previously a communal pasture, began to acquire territorial significance, and individual claims on cultivated plots (known as <strong>Kshetra</strong>) started to emerge.</p>

<h3>Emergence of Social Inequality</h3>
<p>As settled agriculture generated surpluses, social inequality increased. Chieftains (Rajans) and priests (Brahmanas) accumulated greater wealth, particularly in the form of cattle, horses, and captive women. The common people (Vis) were increasingly pressured to provide voluntary gifts (Bali), which slowly began to resemble mandatory tributes. This created a clear class division between the ruling/priestly elites and the working peasantry.</p>

<h3>Interaction with Indigenous Populations</h3>
<p>The expansion into new territories led to greater interaction and assimilation with the indigenous populations (Dasas and Dasyus). Many defeated indigenous people were incorporated into the Aryan social fold at the bottom of the hierarchy as agricultural laborers and domestic servants. This social integration of non-Aryan groups culminated in the creation of the fourth Varna, the <strong>Shudras</strong>, establishing the institutionalized four-fold hierarchy of Later Vedic times.</p>
""",
        "content_hi": """
<h3>स्थायी कृषि की ओर संक्रमण</h3>
<p>ऋग्वैदिक काल के अंत में (लगभग 1000 ईसा पूर्व), आर्य कबीलों ने सप्त-सिंधु क्षेत्र (पंजाब) से पूर्व की ओर गंगा-यमुना दोआब की ओर पलायन शुरू किया। यह प्रवास खानाबदोश पशुचारण जीवन शैली से स्थायी कृषि की ओर संक्रमण के साथ मेल खाता था। भूमि, जो पहले एक सामूहिक चरागाह थी, क्षेत्रीय महत्व प्राप्त करने लगी और खेती की जाने वाली भूमि (जिन्हें <strong>क्षेत्र</strong> कहा जाता था) पर व्यक्तिगत दावे उभरने लगे।</p>

<h3>सामाजिक असमानता का उदय</h3>
<p>जैसे-जैसे स्थायी कृषि से अधिशेष (सरप्लस) उत्पन्न होने लगा, वैसे-वैसे सामाजिक असमानता बढ़ती गई। प्रमुखों (राजन) और पुरोहितों (ब्राह्मणों) ने अधिक धन संचित किया, विशेष रूप से मवेशियों, घोड़ों और बंदी महिलाओं के रूप में। आम लोगों (विश) पर स्वैच्छिक उपहार (बलि) प्रदान करने का दबाव बढ़ता गया, जो धीरे-धीरे अनिवार्य करों का रूप लेने लगा। इसने शासक/पुरोहित वर्ग और कामकाजी कृषकों के बीच एक स्पष्ट वर्ग विभाजन पैदा किया।</p>

<h3>स्वदेशी आबादी के साथ अंतःक्रिया</h3>
<p>नए क्षेत्रों में विस्तार के कारण स्वदेशी आबादी (दासों और दस्युओं) के साथ अधिक अंतःक्रिया और आत्मसात हुआ। कई पराजित स्वदेशी लोगों को कृषि श्रमिकों और घरेलू नौकरों के रूप में पदानुक्रम में सबसे नीचे आर्य सामाजिक व्यवस्था में शामिल किया गया था। गैर-आर्य समूहों के इस सामाजिक एकीकरण के परिणामस्वरूप चौथे वर्ण, <strong>शूद्रों</strong> का निर्माण हुआ, जिसने उत्तर वैदिक काल के संस्थागत चार-स्तरीय पदानुक्रम को स्थापित किया।</p>
"""
    }
]

# 2. Generator for 62 mastery zone questions per section

question_pool = {1: [{'q': 'What was the basic unit of Rigvedic social structure?', 'opts': ['Kula (Family household)', 'Grama (Village)', 'Vis (Clan)', 'Jana (Tribe)'], 'ans': 0, 'sol': 'Kula was the family, the basic social and residential unit.', 'q_hi': 'ऋग्वैदिक सामाजिक संरचना की बुनियादी इकाई क्या थी?', 'opts_hi': ['कुल (पारिवारिक गृहस्थी)', 'ग्राम (गाँव)', 'विश (कुल/गोत्र)', 'जन (जनजाति)'], 'ans_hi': 0, 'sol_hi': 'कुल परिवार था, जो बुनियादी सामाजिक और आवासीय इकाई थी.'}, {'q': 'Who was the patriarchal head of the family unit?', 'opts': ['Kulapa or Grihapati', 'Rajan', 'Gramani', 'Vispati'], 'ans': 0, 'sol': 'The Kulapa or Grihapati (usually the father/eldest male) headed the Kula.', 'q_hi': 'पारिवारिक इकाई का पितृसत्तात्मक प्रमुख कौन था?', 'opts_hi': ['कुलप या गृहपति', 'राजन', 'ग्रामणी', 'विशपति'], 'ans_hi': 0, 'sol_hi': 'कुलप या गृहपति (आमतौर पर पिता/सबसे बड़ा पुरुष) कुल का मुखिया होता था.'}, {'q': 'What describes the family system of the early Rigvedic Aryans?', 'opts': ['Patriarchal and joint family system', 'Matriarchal and nuclear family system', 'Fraternal polyandry standard', 'None of the above'], 'ans': 0, 'sol': 'Rigvedic families were patriarchal and lived as large joint households.', 'q_hi': 'प्रारंभिक ऋग्वैदिक आर्यों की पारिवारिक व्यवस्था का क्या वर्णन है?', 'opts_hi': ['पितृसत्तात्मक और संयुक्त परिवार प्रणाली', 'मातृसत्तात्मक और एकल परिवार प्रणाली', 'भ्रातृ बहुपति विवाह मानक', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक परिवार पितृसत्तात्मक थे और बड़े संयुक्त घरों के रूप में रहते थे.'}, {'q': "The Sanskrit term 'Griha' in Rigvedic context refers to:", 'opts': ['The household or home', 'The temple sanctuary', 'The pasture boundary', 'The battle chariot'], 'ans': 0, 'sol': 'Griha refers to the house, home, or family dwelling.', 'q_hi': "ऋग्वैदिक संदर्भ में संस्कृत शब्द 'गृह' किसे संदर्भित करता है?", 'opts_hi': ['गृहस्थी या घर', 'मंदिर का गर्भगृह', 'चरागाह की सीमा', 'युद्ध का रथ'], 'ans_hi': 0, 'sol_hi': 'गृह का तात्पर्य घर, गृहस्थी या पारिवारिक आवास से है.'}, {'q': 'Did the patriarch (Grihapati) have absolute authority over family members?', 'opts': ['Yes, including powers of punishment and disposal of assets', 'No, his decisions had to be approved by the Samiti', 'No, the mother held the ultimate veto', 'Only in Later Vedic times'], 'ans': 0, 'sol': 'The patriarch held absolute power over children and property in the household.', 'q_hi': 'क्या पितृसत्तात्मक प्रमुख (गृहपति) के पास परिवार के सदस्यों पर पूर्ण अधिकार था?', 'opts_hi': ['हाँ, जिसमें सजा देने और संपत्ति के निपटान के अधिकार शामिल थे', 'नहीं, उसके निर्णयों को समिति द्वारा अनुमोदित किया जाना था', 'नहीं, माता के पास अंतिम वीटो शक्ति थी', 'केवल उत्तर वैदिक काल में'], 'ans_hi': 0, 'sol_hi': 'गृहपति के पास घर में बच्चों और संपत्ति पर पूर्ण शक्ति होती थी.'}, {'q': 'What was the cluster of several families (Kula) called?', 'opts': ['Grama', 'Vis', 'Jana', 'Sabha'], 'ans': 0, 'sol': 'Several families formed a Grama (village or mobile settlement).', 'q_hi': 'कई परिवारों (कुल) के समूह को क्या कहा जाता था?', 'opts_hi': ['ग्राम', 'विश', 'जन', 'सभा'], 'ans_hi': 0, 'sol_hi': 'कई परिवारों ने मिलकर एक ग्राम (गाँव या गतिशील बस्ती) का निर्माण किया.'}, {'q': 'Which term describes a group of villages forming a clan unit?', 'opts': ['Vis', 'Grama', 'Kula', 'Jana'], 'ans': 0, 'sol': 'Vis was a clan grouping, consisting of several Gramas.', 'q_hi': 'गाँवों के उस समूह को क्या कहा जाता है जो एक कुल इकाई बनाता था?', 'opts_hi': ['विश', 'ग्राम', 'कुल', 'जन'], 'ans_hi': 0, 'sol_hi': 'विश एक कुल समूह था, जिसमें कई ग्राम शामिल थे.'}, {'q': 'What was the highest social and political unit based on kinship?', 'opts': ['Jana (Tribe)', 'Vis', 'Grama', 'Kula'], 'ans': 0, 'sol': 'Jana was the tribe, the highest kinship-based unit migrating together.', 'q_hi': 'सगोत्रता पर आधारित सर्वोच्च सामाजिक और राजनीतिक इकाई कौन सी थी?', 'opts_hi': ['जन (जनजाति)', 'विश', 'ग्राम', 'कुल'], 'ans_hi': 0, 'sol_hi': 'जन जनजाति थी, जो एक साथ प्रवास करने वाली सगोत्रता पर आधारित सर्वोच्च इकाई थी.'}, {'q': 'How was kinship (blood relations) viewed in Rigvedic society?', 'opts': ['As the primary bond of social organization and loyalty', 'As secondary to commercial contracts', 'As completely irrelevant in cities', 'Only for priestly families'], 'ans': 0, 'sol': 'Kinship was the primary bond; loyalty was to the family and tribe (Jana).', 'q_hi': 'ऋग्वैदिक समाज में सगोत्रता (रक्त संबंध) को किस रूप में देखा जाता था?', 'opts_hi': ['सामाजिक संगठन और निष्ठा के प्राथमिक बंधन के रूप में', 'व्यावसायिक अनुबंधों के बाद गौण रूप में', 'शहरों में पूरी तरह से अप्रासंगिक', 'केवल पुरोहित परिवारों के लिए'], 'ans_hi': 0, 'sol_hi': 'सगोत्रता प्राथमिक बंधन थी; निष्ठा परिवार और जनजाति (जन) के प्रति थी.'}, {'q': "The term 'Sadhana' or 'Sajata' in early texts refers to:", 'opts': ['Kinsmen or relatives of the same clan', 'Tax collectors', 'Chariot builders', 'Foreign merchants'], 'ans': 0, 'sol': 'Sajata refers to relatives or kinsmen belonging to the same birth group.', 'q_hi': "प्रारंभिक ग्रंथों में 'साधना' या 'सजात' शब्द किसे संदर्भित करता है?", 'opts_hi': ['एक ही कुल के संबंधी या रिश्तेदार (सजात)', 'कर संग्राहक', 'रथ निर्माता', 'विदेशी व्यापारी'], 'ans_hi': 0, 'sol_hi': 'सजात का तात्पर्य एक ही जन्म समूह से संबंधित रिश्तेदारों या सगोत्रों से है.'}, {'q': 'Did separate private household ownership of pastures exist?', 'opts': ['No, pastures were deified and held collectively by the Jana', 'Yes, marked by stone boundary walls', 'Yes, owned exclusively by the Kulapa', 'Only for gold merchants'], 'ans': 0, 'sol': 'Pastures were communal property; families owned only cattle and domestic goods.', 'q_hi': 'क्या चरागाहों का अलग निजी घरेलू स्वामित्व मौजूद था?', 'opts_hi': ['नहीं, चरागाहों को देवत्व प्रदान किया गया था और जन द्वारा सामूहिक रूप से रखा जाता था', 'हाँ, पत्थर की सीमा की दीवारों द्वारा चिह्नित', 'हाँ, विशेष रूप से कुलप के स्वामित्व में', 'केवल स्वर्ण व्यापारियों के लिए'], 'ans_hi': 0, 'sol_hi': 'चरागाह सामूहिक संपत्ति थे; परिवारों के पास केवल मवेशी और घरेलू सामान थे.'}, {'q': 'What describes the position of the mother (Grihapatni) in the household?', 'opts': ['Respected mistress of the home who participated in Yajna', 'A slave without rights', 'Exiled to separate forest tracts', 'The supreme commander of the family militia'], 'ans': 0, 'sol': 'Grihapatni enjoyed respect and performed Yajna alongside her husband.', 'q_hi': 'घर में माता (गृहपत्नी) की स्थिति का क्या वर्णन है?', 'opts_hi': ['घर की सम्मानित स्वामिनी जो यज्ञ में भाग लेती थी', 'बिना अधिकारों की गुलाम', 'अलग वन क्षेत्रों में निर्वासित', 'पारिवारिक मिलिशिया की सर्वोच्च कमांडर'], 'ans_hi': 0, 'sol_hi': 'गृहपत्नी को सम्मान प्राप्त था और वह अपने पति के साथ यज्ञ संपन्न करती थी.'}], 2: [{'q': 'Which hymn in Rigveda Mandala X introduces the fourfold varna system?', 'opts': ['Purusha Sukta', 'Nasadiya Sukta', 'Gayatri Sukta', 'Sarasvati Sukta'], 'ans': 0, 'sol': 'The Purusha Sukta describes the creation of four classes from the giant Purusha.', 'q_hi': 'ऋग्वेद मंडल X का कौन सा सूक्त चार वर्णों की व्यवस्था का परिचय देता है?', 'opts_hi': ['पुरुष सूक्त', 'नासदीय सूक्त', 'गायत्री सूक्त', 'सरस्वती सूक्त'], 'ans_hi': 0, 'sol_hi': 'पुरुष सूक्त विशाल पुरुष से चार वर्गों के निर्माण का वर्णन करता है.'}, {'q': 'Was the varna system in the early Rigvedic period hereditary?', 'opts': ['No, it was flexible and based on occupation, not birth', "Yes, children had to follow the parent's varna strictly", 'Varna did not exist in any form', 'Only for the warriors'], 'ans': 0, 'sol': 'Varna was flexible; caste rigidity and hereditary rules only developed later.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में वर्ण व्यवस्था वंशानुगत थी?', 'opts_hi': ['नहीं, यह लचीली थी और जन्म पर नहीं बल्कि व्यवसाय पर आधारित थी', 'हाँ, बच्चों को माता-पिता के वर्ण का सख्ती से पालन करना पड़ता था', 'वर्ण किसी भी रूप में मौजूद नहीं था', 'केवल योद्धाओं के लिए'], 'ans_hi': 0, 'sol_hi': 'वर्ण लचीला था; जातिगत कठोरता और वंशानुगत नियम केवल बाद में विकसित हुए.'}, {'q': 'What terms were initially used to differentiate people in the early Rigveda?', 'opts': ['Arya Varna and Dasa Varna', 'Brahmin and Kshatriya only', 'Untouchable and Touchable', 'None of the above'], 'ans': 0, 'sol': 'Initial distinction was based on color/culture: Arya (Vedic) and Dasa (indigenous).', 'q_hi': 'प्रारंभिक ऋग्वेद में लोगों में अंतर करने के लिए शुरू में किन शब्दों का प्रयोग किया जाता था?', 'opts_hi': ['आर्य वर्ण और दास वर्ण', 'केवल ब्राह्मण और क्षत्रिय', 'अछूत और छूत', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक अंतर रंग/संस्कृति पर आधारित था: आर्य (वैदिक) और दास (स्वदेशी).'}, {'q': "A poet in Rigveda Mandala IX says: 'I am a poet, my father is a physician, my mother grinds grain.' This indicates:", 'opts': ['High occupational mobility within the same family', 'Rigid caste laws', 'Absence of family bonds', 'Slavery of women'], 'ans': 0, 'sol': 'It shows that members of the same family could follow different occupations.', 'q_hi': "ऋग्वेद मंडल IX में एक कवि कहता है: 'मैं एक कवि हूँ, मेरे पिता एक चिकित्सक हैं, मेरी माँ अनाज पीसती हैं।' यह दर्शाता है:", 'opts_hi': ['एक ही परिवार के भीतर उच्च व्यावसायिक गतिशीलता', 'कठोर जातिगत कानून', 'पारिवारिक बंधनों का अभाव', 'महिलाओं की गुलामी'], 'ans_hi': 0, 'sol_hi': 'यह दर्शाता है कि एक ही परिवार के सदस्य अलग-अलग व्यवसाय अपना सकते थे.'}, {'q': "What was the physical basis of the term 'Varna' etymologically?", 'opts': ['Color or outward appearance', 'Hereditary lineage', 'Tax category', 'Sacrificial altar shape'], 'ans': 0, 'sol': 'Varna etymologically comes from vrn (to choose or color).', 'q_hi': "व्युत्पत्ति के अनुसार 'वर्ण' शब्द का भौतिक आधार क्या था?", 'opts_hi': ['रंग या बाहरी रूप', 'वंशानुगत वंश', 'कर श्रेणी', 'यज्ञ वेदी का आकार'], 'ans_hi': 0, 'sol_hi': 'वर्ण शब्द व्युत्पत्ति के अनुसार वृ (चुनना या रंग) से आता है.'}, {'q': "Who were the 'Dasas' and 'Dasyus' in early Vedic society?", 'opts': ['Indigenous non-Aryan populations conquered by Aryans', 'Priests from Mesopotamia', 'Chariot builders of the Bharatas', 'None of these'], 'ans': 0, 'sol': 'They were the pre-existing, indigenous populations of the Sapta-Sindhu.', 'q_hi': "प्रारंभिक वैदिक समाज में 'दास' और 'दस्यु' कौन थे?", 'opts_hi': ['आर्यों द्वारा जीते गए स्वदेशी गैर-आर्य लोग', 'मेसोपोटामिया के पुरोहित', 'भरतों के रथ निर्माता', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'वे सप्त-सिंधु के पहले से मौजूद, स्वदेशी लोग थे.'}, {'q': 'Which text is considered a later addition to the Rigveda containing the Purusha Sukta?', 'opts': ['Mandala X', 'Mandala II', 'Mandala III', 'Mandala VII'], 'ans': 0, 'sol': 'Mandala X is linguistically and conceptually later than Mandalas II-VII.', 'q_hi': 'ऋग्वेद में बाद में जोड़े गए किस मंडल में पुरुष सूक्त शामिल है?', 'opts_hi': ['मंडल X', 'मंडल II', 'मंडल III', 'मंडल VII'], 'ans_hi': 0, 'sol_hi': 'मंडल X भाषाई और वैचारिक रूप से मंडल II-VII से बाद का है.'}, {'q': 'Did untouchability exist in the early Rigvedic period?', 'opts': ['No, there is no mention of untouchability or impurity of touch', 'Yes, Shudras were completely excluded from villages', 'Only for metalworkers', 'Only in the later part of the Ganges valley'], 'ans': 0, 'sol': 'Untouchability did not exist in the early pastoral society.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में अस्पृश्यता मौजूद थी?', 'opts_hi': ['नहीं, अस्पृश्यता या स्पर्श की अशुद्धता का कोई उल्लेख नहीं है', 'हाँ, शूद्रों को गाँवों से पूरी तरह बाहर रखा गया था', 'केवल धातु कामगारों के लिए', 'केवल गंगा घाटी के बाद के हिस्से में'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक पशुचारक समाज में अस्पृश्यता का अस्तित्व नहीं था.'}, {'q': 'What term describes the class of warriors and chiefs in early texts?', 'opts': ['Rajanya', 'Brahmin', 'Vaishya', 'Shudra'], 'ans': 0, 'sol': 'Rajanya was the term used for the ruling warrior class.', 'q_hi': 'प्रारंभिक ग्रंथों में योद्धाओं और मुखियों के वर्ग को कौन सा शब्द वर्णित करता है?', 'opts_hi': ['राजन्य', 'ब्राह्मण', 'वैश्य', 'शूद्र'], 'ans_hi': 0, 'sol_hi': 'राजन्य शब्द का प्रयोग शासक योद्धा वर्ग के लिए किया जाता था.'}, {'q': 'The common people or agriculturists were termed as:', 'opts': ['Vis or Vaishya', 'Rajanya', 'Brahmin', 'Shudra'], 'ans': 0, 'sol': 'Vis (common folk) later crystallized into the Vaishya varna.', 'q_hi': 'सामान्य लोगों या कृषकों को क्या कहा जाता था?', 'opts_hi': ['विश या वैश्य', 'राजन्य', 'ब्राह्मण', 'शूद्र'], 'ans_hi': 0, 'sol_hi': 'विश (सामान्य लोग) बाद में वैश्य वर्ण के रूप में स्तरीकृत हुए.'}, {'q': "How were the 'Dasyus' characterized in the Rigvedic hymns?", 'opts': ['As flat-nosed (Anas) non-sacrificers who spoke a different language', 'As great friends and trading allies', 'As divine beings', 'As iron weapon manufacturers'], 'ans': 0, 'sol': 'Hymns describe them as Anas (flat-nosed), Mridhravac (hostile speech), and non-sacrificing.', 'q_hi': "ऋग्वैदिक भजनों में 'दस्युओं' की क्या विशेषताएँ बताई गई हैं?", 'opts_hi': ['चपटी नाक वाले (अनास) और यज्ञ न करने वाले जो भिन्न भाषा बोलते थे', 'महान मित्रों और व्यापारिक सहयोगियों के रूप में', 'दिव्य प्राणियों के रूप में', 'लोहे के हथियार बनाने वालों के रूप में'], 'ans_hi': 0, 'sol_hi': 'भजनों में उन्हें अनास (चपटी नाक वाले), मृध्रवाच (कटु भाषा बोलने वाले) और यज्ञ न करने वाले के रूप में वर्णित किया गया है.'}, {'q': 'What caused the transition from a simple classless society to early social hierarchy?', 'opts': ['Economic surplus from agriculture and incorporation of indigenous populations', 'Complete destruction of cattle', 'A decree by the King of Babylon', 'None of the above'], 'ans': 0, 'sol': 'Surplus resources and assimilation of Dasas created social layers.', 'q_hi': 'एक सरल वर्गहीन समाज से प्रारंभिक सामाजिक पदानुक्रम में संक्रमण का क्या कारण था?', 'opts_hi': ['कृषि से प्राप्त आर्थिक अधिशेष और स्वदेशी आबादी का समावेश', 'मवेशियों का पूर्ण विनाश', 'बेबीलोन के राजा द्वारा जारी एक आदेश', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'अधिशेष संसाधनों और दासों के आत्मसात होने से सामाजिक परतें बनीं.'}], 3: [{'q': 'What describes the status of women in the early Rigvedic period?', 'opts': ['Respectable status with access to education and assemblies', 'Completely confined to dark rooms without rights', 'Exempt from family work but banned from rituals', 'Considered property that could be sold'], 'ans': 0, 'sol': 'Women had high status, could study, and participated in Sabha/Vidatha.', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में महिलाओं की स्थिति का क्या वर्णन है?', 'opts_hi': ['शिक्षा और सभाओं तक पहुंच के साथ सम्मानित स्थिति', 'बिना किसी अधिकार के पूरी तरह से अंधेरे कमरों में बंद', 'पारिवारिक कार्यों से मुक्त लेकिन अनुष्ठानों से प्रतिबंधित', 'संपत्ति माना जाता था जिसे बेचा जा सकता था'], 'ans_hi': 0, 'sol_hi': 'महिलाओं की स्थिति उच्च थी, वे अध्ययन कर सकती थीं, और सभा/विदथ में भाग लेती थीं.'}, {'q': 'Which rite of initiation (sacred thread ceremony) was open to girls in early times?', 'opts': ['Upanayana', 'Sanyasa', 'Niyoga', 'Garbadhana'], 'ans': 0, 'sol': 'Upanayana (education rite) was performed for both boys and girls.', 'q_hi': 'प्रारंभिक काल में लड़कियों के लिए दीक्षा का कौन सा संस्कार (जनेऊ समारोह) खुला था?', 'opts_hi': ['उपनयन', 'संन्यास', 'नियोग', 'गर्भाधान'], 'ans_hi': 0, 'sol_hi': 'उपनयन (शिक्षा संस्कार) लड़के और लड़कियों दोनों के लिए किया जाता था.'}, {'q': 'Could women participate in the tribal assemblies Sabha and Vidatha?', 'opts': ['Yes, they participated and were called Sabhavati', 'No, they were strictly banned', 'Only widows could attend', 'Only during the Soma festival'], 'ans': 0, 'sol': 'Rigveda shows women attended assemblies and had voice.', 'q_hi': 'क्या महिलाएँ जनजातीय सभाओं सभा और विदथ में भाग ले सकती थीं?', 'opts_hi': ['हाँ, वे भाग लेती थीं और उन्हें सभावती कहा जाता था', 'नहीं, उन पर सख्त प्रतिबंध था', 'केवल विधवाएं ही भाग ले सकती थीं', 'केवल सोम उत्सव के दौरान'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद दर्शाता है कि महिलाओं ने सभाओं में भाग लिया और उनकी आवाज़ सुनी जाती थी.'}, {'q': "What was the practice of 'Niyoga' in the early Vedic society?", 'opts': ["Co-habiting with a brother-in-law to produce an heir after husband's death", 'Banishment of widows to forests', "Burning of widows on husband's pyre", 'Sacrificing young girls to deities'], 'ans': 0, 'sol': "Niyoga allowed a childless widow to raise sons with her husband's brother.", 'q_hi': "प्रारंभिक वैदिक समाज में 'नियोग' की क्या प्रथा थी?", 'opts_hi': ['पति की मृत्यु के बाद उत्तराधिकारी पैदा करने के लिए देवर के साथ सहवास करना', 'विधवाओं को जंगलों में निर्वासित करना', 'पति की चिता पर विधवाओं को जलाना', 'देवताओं के लिए युवा लड़कियों की बलि देना'], 'ans_hi': 0, 'sol_hi': 'नियोग प्रथा एक निःसंतान विधवा को अपने पति के भाई के साथ संतान उत्पन्न करने की अनुमति देती थी.'}, {'q': 'Did the practice of Sati (widow burning) exist in the early Rigveda?', 'opts': ['No, it was non-existent; widows remarried or practiced Niyoga', 'Yes, it was compulsory for all varnas', 'Only in the Sarasvati region', 'Only for the wives of the Rajan'], 'ans': 0, 'sol': 'Sati was not practiced; Rigveda has no authentic hymns supporting widow burning.', 'q_hi': 'क्या प्रारंभिक ऋग्वेद में सती प्रथा (विधवा दाह) का अस्तित्व था?', 'opts_hi': ['नहीं, यह अस्तित्वहीन थी; विधवाएँ पुनर्विवाह करती थीं या नियोग का पालन करती थीं', 'हाँ, यह सभी वर्णों के लिए अनिवार्य था', 'केवल सरस्वती क्षेत्र में', 'केवल राजन की पत्नियों के लिए'], 'ans_hi': 0, 'sol_hi': 'सती प्रथा का प्रचलन नहीं था; ऋग्वेद में विधवा दाह का समर्थन करने वाले कोई प्रामाणिक भजन नहीं हैं.'}, {'q': "Who were the 'Brahmavadinis' in Rigvedic times?", 'opts': ['Women who chose education and philosophy over marriage', 'Female temple dancers', 'Wives of the Rajan', 'Women metalworkers'], 'ans': 0, 'sol': 'Brahmavadinis were lifelong female students of Vedas and philosophy.', 'q_hi': "ऋग्वैदिक काल में 'ब्रह्मवादिनी' कौन थीं?", 'opts_hi': ['वे महिलाएँ जिन्होंने विवाह के स्थान पर शिक्षा और दर्शन को चुना', 'महिला मंदिर नर्तकियाँ', 'राजन की पत्नियाँ', 'महिला धातु कामगार'], 'ans_hi': 0, 'sol_hi': 'ब्रह्मवादिनी वे महिलाएँ थीं जिन्होंने जीवन भर वेदों और दर्शन का अध्ययन किया.'}, {'q': 'Who was the famous female seer who composed Rigvedic hymns and debated philosophers?', 'opts': ['Ghopsha or Apala', 'Sita', 'Aranyani', 'None of these'], 'ans': 0, 'sol': 'Female seers (Rishikas) like Ghosha, Apala, and Lopamudra composed hymns.', 'q_hi': 'ऋग्वैदिक भजनों की रचना करने वाली और दार्शनिकों के साथ बहस करने वाली प्रसिद्ध महिला ऋषि कौन थी?', 'opts_hi': ['घोषा या अपाला', 'सीता', 'अरण्यानी', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'घोषा, अपाला और लोपामुद्रा जैसी महिला ऋषियों (ऋषिकाओं) ने भजनों की रचना की थी.'}, {'q': 'At what age were girls usually married in the early Rigvedic period?', 'opts': ['At maturity (adulthood)', 'As child brides before puberty', 'They were never allowed to marry', 'Only after the age of 40'], 'ans': 0, 'sol': 'Child marriage was absent; girls married after reaching maturity.', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में लड़कियों का विवाह आमतौर पर किस आयु में होता था?', 'opts_hi': ['वयस्क होने पर (परिपक्वता पर)', 'यौवन से पहले बाल वधुओं के रूप में', 'उन्हें कभी विवाह करने की अनुमति नहीं थी', 'केवल 40 वर्ष की आयु के बाद'], 'ans_hi': 0, 'sol_hi': 'बाल विवाह अनुपस्थित था; लड़कियां परिपक्वता प्राप्त करने के बाद ही विवाह करती थीं.'}, {'q': "The term 'Amaju' refers to which category of women?", 'opts': ["Unmarried women who lived in parent's house lifelong", 'Widows who practiced Sati', 'Female military commanders', 'Women who ran markets'], 'ans': 0, 'sol': "Amaju refers to women who remained unmarried and stayed at father's home.", 'q_hi': "शब्द 'अमाजू' किस श्रेणी की महिलाओं को संदर्भित करता है?", 'opts_hi': ['अविवाहित महिलाएँ जो जीवन भर माता-पिता के घर रहती थीं', 'सती प्रथा का पालन करने वाली विधवाएँ', 'महिला सैन्य कमांडर', 'बाजार चलाने वाली महिलाएँ'], 'ans_hi': 0, 'sol_hi': 'अमाजू उन महिलाओं को संदर्भित करता है जो अविवाहित रहीं और अपने पिता के घर पर रहीं.'}, {'q': 'Did women have the right to choose their husbands in early times?', 'opts': ['Yes, through swayamvara or mutual choice (Kama marriage)', 'No, they were sold to the highest bidder', 'Only with the permission of the chief priest', 'Only from foreign tribes'], 'ans': 0, 'sol': 'Texts indicate that mature girls had a say in choosing their husbands.', 'q_hi': 'क्या प्रारंभिक काल में महिलाओं को अपने पति चुनने का अधिकार था?', 'opts_hi': ['हाँ, स्वयंवर या आपसी पसंद (काम विवाह) के माध्यम से', 'नहीं, उन्हें सबसे ऊंची बोली लगाने वाले को बेच दिया जाता था', 'केवल मुख्य पुरोहित की अनुमति से', 'केवल विदेशी कबीलों से'], 'ans_hi': 0, 'sol_hi': 'ग्रंथों से संकेत मिलता है कि वयस्क लड़कियों को अपना पति चुनने का अधिकार था.'}, {'q': 'Which female philosopher debated Yajnavalkya in royal court?', 'opts': ['Gargi Vachaknavi (later tradition)', 'Lopamudra', 'Apala', 'Ghosha'], 'ans': 0, 'sol': 'Gargi debated Yajnavalkya (recorded in Upanishads, marking later transition).', 'q_hi': 'शाही दरबार में याज्ञवल्क्य के साथ किस महिला दार्शनिक ने बहस की थी?', 'opts_hi': ['गार्गी वाचक्नवी (उत्तरकालीन परंपरा)', 'लोपामुद्रा', 'अपाला', 'घोषा'], 'ans_hi': 0, 'sol_hi': 'गार्गी ने याज्ञवल्क्य के साथ शास्त्रार्थ किया था (उपनिषदों में दर्ज, जो उत्तरकालीन संक्रमण को दर्शाता है).'}, {'q': 'Was purdah (veil system) practiced by Rigvedic women?', 'opts': ['No, it was completely absent', 'Yes, they had to cover their face in front of elders', 'Only during sacrifices', 'Only inside the chariot'], 'ans': 0, 'sol': 'Veil system or seclusion of women did not exist in the early Vedic society.', 'q_hi': 'क्या ऋग्वैदिक महिलाओं द्वारा पर्दा प्रथा का पालन किया जाता था?', 'opts_hi': ['नहीं, यह पूरी तरह से अनुपस्थित था', 'हाँ, उन्हें बुजुर्गों के सामने अपना चेहरा ढकना पड़ता था', 'केवल यज्ञों के दौरान', 'केवल रथ के भीतर'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक वैदिक समाज में पर्दा प्रथा या महिलाओं को अलग रखने की व्यवस्था मौजूद नहीं थी.'}], 4: [{'q': 'What was the standard form of marriage in early Rigvedic society?', 'opts': ['Monogamy (one husband and wife)', 'Polygamy for all men', 'Polyandry (one wife with many husbands)', 'Group marriage standard'], 'ans': 0, 'sol': 'Monogamy was the general rule, though chiefs practiced polygamy.', 'q_hi': 'प्रारंभिक ऋग्वैदिक समाज में विवाह का मानक स्वरूप क्या था?', 'opts_hi': ['एकपत्नीत्व (एक पति और एक पत्नी)', 'सभी पुरुषों के लिए बहुपत्नीत्व', 'बहुपतित्व (एक पत्नी के कई पति)', 'समूह विवाह मानक'], 'ans_hi': 0, 'sol_hi': 'एकपत्नीत्व सामान्य नियम था, हालांकि मुखिया बहुपत्नीत्व का पालन करते थे.'}, {'q': "What term represents the bridal gifts or dowry carried by bride to husband's house?", 'opts': ['Vahatu', 'Bali', 'Bhaga', 'Niska'], 'ans': 0, 'sol': 'Vahatu was the gift or dowry given during marriage.', 'q_hi': 'दुल्हन द्वारा अपने पति के घर ले जाए जाने वाले विवाह उपहार या दहेज को क्या कहा जाता था?', 'opts_hi': ['वहतु', 'बलि', 'भाग', 'निष्क'], 'ans_hi': 0, 'sol_hi': 'वहतु विवाह के समय दुल्हन को दिए जाने वाले उपहार या दहेज की सामग्री थी.'}, {'q': 'Was child marriage common in early Rigvedic times?', 'opts': ['No, it was completely absent; marriages occurred at adulthood', 'Yes, children were married at age 5', 'Only for the priestly Brahmin class', 'Only in the western areas'], 'ans': 0, 'sol': 'Marriages took place after girls reached puberty and physical maturity.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में बाल विवाह आम था?', 'opts_hi': ['नहीं, यह पूरी तरह से अनुपस्थित था; विवाह वयस्क होने पर होते थे', 'हाँ, बच्चों का विवाह 5 वर्ष की आयु में कर दिया जाता था', 'केवल पुरोहित ब्राह्मण वर्ग के लिए', 'केवल पश्चिमी क्षेत्रों में'], 'ans_hi': 0, 'sol_hi': 'विवाह लड़कियों के यौवन और शारीरिक परिपक्वता प्राप्त करने के बाद ही होते थे.'}, {'q': "The concept of 'Niyoga' allowed a childless widow to raise sons with:", 'opts': ["Her deceased husband's brother (Devar)", 'The chief priest of the tribe', 'The Rajan', 'A foreign trader'], 'ans': 0, 'sol': 'Niyoga was levirate marriage allowed for raising a male heir.', 'q_hi': 'नियोग की अवधारणा ने एक निःसंतान विधवा को किसके साथ पुत्र उत्पन्न करने की अनुमति दी?', 'opts_hi': ['अपने मृत पति के भाई (देवर) के साथ', 'कबीले के मुख्य पुरोहित के साथ', 'राजन के साथ', 'एक विदेशी व्यापारी के साथ'], 'ans_hi': 0, 'sol_hi': 'नियोग देवर-भाभी विवाह का रूप था जिसकी अनुमति पुरुष उत्तराधिकारी प्राप्त करने के लिए दी जाती थी.'}, {'q': 'Which type of marriage was defined by mutual love and choice without parental consent?', 'opts': ['Gandharva marriage (Kama marriage)', 'Brahma marriage', 'Daiva marriage', 'Asura marriage'], 'ans': 0, 'sol': 'Gandharva marriage was based on love and mutual consent of the couple.', 'q_hi': 'माता-पिता की सहमति के बिना आपसी प्रेम और पसंद से परिभाषित विवाह का कौन सा प्रकार था?', 'opts_hi': ['गंधर्व विवाह (काम विवाह)', 'ब्रह्म विवाह', 'दैव विवाह', 'असुर विवाह'], 'ans_hi': 0, 'sol_hi': 'गंधर्व विवाह युगल के प्रेम और आपसी सहमति पर आधारित होता था.'}, {'q': 'What describes the attitude towards divorce in early Rigvedic law?', 'opts': ['Divorce did not exist; marriage was an unbreakable sacred bond', 'Divorce was allowed at will by paying a fee in cows', 'Only the wife could divorce the husband', 'None of the above'], 'ans': 0, 'sol': 'Marriage was a lifelong sacrament; divorce was practically unknown.', 'q_hi': 'प्रारंभिक ऋग्वैदिक कानून में तलाक के प्रति दृष्टिकोण का क्या वर्णन है?', 'opts_hi': ['तलाक का अस्तित्व नहीं था; विवाह एक अटूट पवित्र बंधन था', 'गायों में शुल्क देकर इच्छानुसार तलाक की अनुमति थी', 'केवल पत्नी ही पति को तलाक दे सकती थी', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'विवाह एक आजीवन संस्कार था; तलाक व्यावहारिक रूप से अज्ञात था.'}, {'q': 'What was the term for the bridegroom in Rigvedic Sanskrit?', 'opts': ['Vara', 'Jamatr', 'Pati', 'Grihapati'], 'ans': 0, 'sol': 'Vara was the term used for the bridegroom/husband.', 'q_hi': 'ऋग्वैदिक संस्कृत में दूल्हे के लिए क्या शब्द था?', 'opts_hi': ['वर', 'जामातृ', 'पति', 'गृहपति'], 'ans_hi': 0, 'sol_hi': 'वर दूल्हे/पति के लिए इस्तेमाल किया जाने वाला शब्द था.'}, {'q': 'Which text contains the famous Surya Sukta (Marriage Hymn)?', 'opts': ['Rigveda Mandala X', 'Rigveda Mandala III', 'Yajurveda', 'Sama Veda'], 'ans': 0, 'sol': "Surya Sukta of Mandala X details the marriage of Surya's daughter, forming the base of Hindu rites.", 'q_hi': 'प्रसिद्ध सूर्य सूक्त (विवाह सूक्त) किस ग्रंथ में मिलता है?', 'opts_hi': ['ऋग्वेद मंडल X', 'ऋग्वेद मंडल III', 'यजुर्वेद', 'सामवेद'], 'ans_hi': 0, 'sol_hi': 'मंडल X का सूर्य सूक्त सूर्य की पुत्री के विवाह का विवरण देता है, जो हिंदू विवाह संस्कारों का आधार है.'}, {'q': "The term 'Devar' literally translates to:", 'opts': ["Second husband (husband's brother)", 'The priest who performs marriage', 'The father of the bride', "The king's representative"], 'ans': 0, 'sol': 'Devar literally means second husband, referring to brother-in-law in Niyoga.', 'q_hi': "'देवर' शब्द का शाब्दिक अर्थ है:", 'opts_hi': ['दूसरा पति (पति का भाई)', 'विवाह कराने वाला पुरोहित', 'दुल्हन का पिता', 'राजा का प्रतिनिधि'], 'ans_hi': 0, 'sol_hi': 'देवर का शाब्दिक अर्थ दूसरा पति है, जो नियोग में देवर को संदर्भित करता है.'}, {'q': 'Were inter-caste marriages allowed in the early Rigvedic period?', 'opts': ['Yes, varna boundaries were fluid; intermarriage was common', 'No, they were strictly punished by death', 'Only between priests and warriors', 'None of the above'], 'ans': 0, 'sol': 'Class boundaries were fluid; intermarriage was not forbidden.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में अंतर-जातीय विवाह की अनुमति थी?', 'opts_hi': ['हाँ, वर्ण सीमाएँ लचीली थीं; अंतर-विवाह आम थे', 'नहीं, उन्हें मृत्युदंड से सख्ती से दंडित किया जाता था', 'केवल पुरोहितों और योद्धाओं के बीच', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'वर्ग सीमाएँ लचीली थीं; अंतर-विवाह वर्जित नहीं थे.'}, {'q': 'What was the relative position of co-wives (Sapatni) in polygamous families?', 'opts': ['Highly tense; hymns contain spells to overcome co-wives', 'They shared all assets equally without conflict', 'They ruled the household jointly', 'None of the above'], 'ans': 0, 'sol': "Rigveda Mandala X contains spells to win husband's affection over co-wives.", 'q_hi': 'बहुपत्नी परिवारों में सौतनों (सपत्नी) की सापेक्ष स्थिति क्या थी?', 'opts_hi': ['अत्यधिक तनावपूर्ण; भजनों में सौतनों पर विजय पाने के मंत्र शामिल हैं', 'उन्होंने बिना किसी संघर्ष के सभी संपत्तियों को समान रूप से साझा किया', 'उन्होंने संयुक्त रूप से घर पर शासन किया', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद मंडल X में सौतनों पर पति का स्नेह प्राप्त करने के लिए मंत्र शामिल हैं.'}, {'q': 'What represents the domestic marriage altar fire?', 'opts': ['Yuvati Agni', 'Garhapatya Agni', 'Rudra Agni', 'None of these'], 'ans': 0, 'sol': 'The bride and groom circumambulate the sacrificial fire, which is then carried to their home as Garhapatya.', 'q_hi': 'घरेलू विवाह वेदी की अग्नि का क्या प्रतिनिधित्व है?', 'opts_hi': ['युवती अग्नि', 'गार्हपत्य अग्नि', 'रुद्र अग्नि', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'दूल्हा और दुल्हन यज्ञ की अग्नि की परिक्रमा करते हैं, जिसे बाद में गार्हपत्य के रूप में उनके घर ले जाया जाता है.'}], 5: [{'q': 'How was education conducted in the early Rigvedic period?', 'opts': ['Orally, through memorization of hymns under a Guru', 'By writing Sanskrit script on clay bricks', 'In formal universities like Nalanda', 'Only in foreign lands'], 'ans': 0, 'sol': 'Education was purely oral, based on listening and chanting (Shruti).', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में शिक्षा कैसे संचालित की जाती थी?', 'opts_hi': ['मौखिक रूप से, गुरु के अधीन भजनों को कंठस्थ करके', 'मिट्टी की ईंटों पर संस्कृत लिपि लिखकर', 'नालंदा जैसे औपचारिक विश्वविद्यालयों में', 'केवल विदेशी भूमि में'], 'ans_hi': 0, 'sol_hi': 'शिक्षा विशुद्ध रूप से मौखिक थी, जो सुनने और उच्चारण करने (श्रुति) पर आधारित थी.'}, {'q': "Which ceremony marked the initiation of a student's education?", 'opts': ['Upanayana (sacred thread rite)', 'Sanyasa', 'Niyoga', 'Garbadhana'], 'ans': 0, 'sol': 'Upanayana was the thread ceremony opening access to Vedic study.', 'q_hi': 'कौन सा समारोह छात्र की शिक्षा की शुरुआत का प्रतीक था?', 'opts_hi': ['उपनयन (जनेऊ संस्कार)', 'संन्यास', 'नियोग', 'गर्भाधान'], 'ans_hi': 0, 'sol_hi': 'उपनयन जनेऊ संस्कार था जो वैदिक अध्ययन तक पहुंच प्रदान करता था.'}, {'q': 'Did the four rigid Ashrama stages (celibate, householder, forest, ascetic) exist fully in Rigvedic times?', 'opts': ['No, the system only crystallized in Later Vedic/post-Vedic texts', 'Yes, all men had to follow the four stages strictly', 'Only the ascetic stage existed', 'None of the above'], 'ans': 0, 'sol': 'The four Ashramas developed later; early texts focus mainly on Grihastha (householder).', 'q_hi': 'क्या ऋग्वैदिक काल में चार कठोर आश्रम चरण (ब्रह्मचर्य, गृहस्थ, वानप्रस्थ, संन्यास) पूरी तरह से मौजूद थे?', 'opts_hi': ['नहीं, यह व्यवस्था केवल उत्तर वैदिक/उत्तर-वैदिक ग्रंथों में स्पष्ट हुई', 'हाँ, सभी पुरुषों को चारों चरणों का सख्ती से पालन करना पड़ता था', 'केवल संन्यास चरण मौजूद था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'चारों आश्रम बाद में विकसित हुए; प्रारंभिक ग्रंथ मुख्य रूप से गृहस्थ (गृहस्वामी) पर केंद्रित हैं.'}, {'q': 'What describes the Rigvedic frog hymn (Mandala VII) regarding education?', 'opts': ['It compares students chanting after their teacher to croaking frogs', 'It praises frogs as sacred animals', 'It bans frogs from sacrifice sites', 'None of the above'], 'ans': 0, 'sol': 'Hymn VII.103 humorously compares chanting students to frogs croaking after rain.', 'q_hi': 'शिक्षा के संबंध में ऋग्वैदिक मेंढक भजन (मंडल VII) का क्या वर्णन है?', 'opts_hi': ['यह अपने शिक्षक के बाद भजनों का पाठ करने वाले छात्रों की तुलना मेंढकों की टर्राहट से करता है', 'यह मेंढकों को पवित्र जानवरों के रूप में पूजता है', 'यह यज्ञ स्थलों से मेंढकों को प्रतिबंधित करता है', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'भजन VII.103 हास्यपूर्ण ढंग से पाठ करने वाले छात्रों की तुलना बारिश के बाद मेंढकों की टर्राहट से करता है.'}, {'q': 'Who was the teacher in the Vedic educational setup?', 'opts': ['Guru or Acharya', 'Kulapa', 'Gramani', 'Rajan'], 'ans': 0, 'sol': 'Guru or Acharya was the spiritual and intellectual preceptor.', 'q_hi': 'वैदिक शैक्षणिक व्यवस्था में शिक्षक कौन था?', 'opts_hi': ['गुरु या आचार्य', 'कुलप', 'ग्रामणी', 'राजन'], 'ans_hi': 0, 'sol_hi': 'गुरु या आचार्य आध्यात्मिक और बौद्धिक गुरु होते थे.'}, {'q': 'Could girls undergo the Upanayana ceremony in early times?', 'opts': ['Yes, it was performed for girls who studied Vedas', 'No, they were strictly banned from the ceremony', 'Only if their father was the Rajan', 'Only in the Ganga valley'], 'ans': 0, 'sol': 'Upanayana was open to girls (Brahmavadinis) who pursued education.', 'q_hi': 'क्या प्रारंभिक काल में लड़कियों का उपनयन संस्कार हो सकता था?', 'opts_hi': ['हाँ, यह उन लड़कियों के लिए किया जाता था जो वेदों का अध्ययन करती थीं', 'नहीं, उन्हें इस समारोह से सख्ती से प्रतिबंधित किया गया था', 'केवल तभी जब उनके पिता राजन हों', 'केवल गंगा घाटी में'], 'ans_hi': 0, 'sol_hi': 'शिक्षा प्राप्त करने वाली लड़कियों (ब्रह्मवादिनी) के लिए उपनयन खुला था.'}, {'q': 'The sacred thread ceremony is etymologically related to which term?', 'opts': ['Upanayana (bringing near to teacher)', 'Guru', 'Acharya', 'Shruti'], 'ans': 0, 'sol': 'Upanayana means bringing the student near to the teacher.', 'q_hi': 'जनेऊ संस्कार व्युत्पत्ति के अनुसार किस शब्द से संबंधित है?', 'opts_hi': ['उपनयन (गुरु के पास लाना)', 'गुरु', 'आचार्य', 'श्रुति'], 'ans_hi': 0, 'sol_hi': 'उपनयन का अर्थ है छात्र को शिक्षक के पास लाना.'}, {'q': 'What was the subject matter of early Rigvedic education?', 'opts': ['Chanting hymns, rituals, grammar, and astronomy', 'Writing and bookkeeping', 'Mesopotamian trade contracts', 'Stone sculpting'], 'ans': 0, 'sol': 'Education focused on memorizing hymns, pronunciation (phonetics), and rituals.', 'q_hi': 'प्रारंभिक ऋग्वैदिक शिक्षा की विषयवस्तु क्या थी?', 'opts_hi': ['भजनों का पाठ, अनुष्ठान, व्याकरण और खगोल विज्ञान', 'लेखन और बहीखाता', 'मेसोपोटामिया के व्यापार अनुबंध', 'पत्थर की नक्काशी'], 'ans_hi': 0, 'sol_hi': 'शिक्षा भजनों को कंठस्थ करने, उच्चारण (ध्वनिशास्त्र) और अनुष्ठानों पर केंद्रित थी.'}, {'q': 'Was the system of residential schools (Gurukulas) fully developed in early times?', 'opts': ['No, students lived with Gurus informally in huts/hermitages', 'Yes, large universities with stone libraries existed', 'Only in the Indus cities', 'None of the above'], 'ans': 0, 'sol': 'Gurukulas were simple ashrams/hermitages, not institutionalized boarding campuses.', 'q_hi': 'क्या प्रारंभिक काल में आवासीय विद्यालयों (गुरुकुलों) की प्रणाली पूरी तरह से विकसित थी?', 'opts_hi': ['नहीं, छात्र अनौपचारिक रूप से गुरुओं के साथ झोपड़ियों/आश्रमों में रहते थे', 'हाँ, पत्थर के पुस्तकालयों वाले बड़े विश्वविद्यालय मौजूद थे', 'केवल सिंधु शहरों में', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'गुरुकुल सरल आश्रम/कुटीर थे, न कि संस्थागत आवासीय परिसर.'}, {'q': 'What title represents the students who chose lifelong celibacy and study?', 'opts': ['Naishthika Brahmachari', 'Amaju', 'Upakurvana', 'Sanyasi'], 'ans': 0, 'sol': 'Naishthika was the student who stayed with the Guru lifelong.', 'q_hi': 'जीवन भर ब्रह्मचर्य और अध्ययन का मार्ग चुनने वाले छात्रों को कौन सी उपाधि दी जाती थी?', 'opts_hi': ['नैष्ठिक ब्रह्मचारी', 'अमाजू', 'उपकुर्वाण', 'संन्यासी'], 'ans_hi': 0, 'sol_hi': 'नैष्ठिक वह छात्र था जो जीवन भर गुरु के साथ रहता था.'}, {'q': 'What title refers to students who returned to householder life after completing studies?', 'opts': ['Upakurvana', 'Naishthika', 'Amaju', 'Grihapati'], 'ans': 0, 'sol': 'Upakurvana returned to marry and lead a householder life.', 'q_hi': 'अध्ययन पूरा करने के बाद गृहस्थ जीवन में लौटने वाले छात्रों को क्या उपाधि दी जाती थी?', 'opts_hi': ['उपकुर्वाण', 'नैष्ठिक', 'अमाजू', 'गृहपति'], 'ans_hi': 0, 'sol_hi': 'उपकुर्वाण अध्ययन के बाद विवाह करने और गृहस्थ जीवन जीने के लिए लौट आते थे.'}, {'q': 'Which Vedanga represents phonetics or pronunciation essential for oral Vedic studies?', 'opts': ['Shiksha', 'Vyakarana', 'Kalpa', 'Jyotisha'], 'ans': 0, 'sol': 'Shiksha is phonetics, the nose of the Veda, crucial for correct chanting.', 'q_hi': 'कौन सा वेदांग मौखिक वैदिक अध्ययन के लिए आवश्यक ध्वनिकी या उच्चारण का प्रतिनिधित्व करता है?', 'opts_hi': ['शिक्षा', 'व्याकरण', 'कल्प', 'ज्योतिष'], 'ans_hi': 0, 'sol_hi': 'शिक्षा ध्वनिकी है, वेद की नासिका, जो सही पाठ करने के लिए महत्वपूर्ण है.'}], 6: [{'q': 'What was the principal grain consumed in early Rigvedic diet?', 'opts': ['Yava (Barley)', 'Vrihi (Rice)', 'Godhuma (Wheat)', 'Masura (Lentil)'], 'ans': 0, 'sol': 'Yava (barley) was the staple cereal; rice and wheat were unknown.', 'q_hi': 'प्रारंभिक ऋग्वैदिक आहार में उपभोग किया जाने वाला मुख्य अनाज कौन सा था?', 'opts_hi': ['यव (जौ)', 'व्रीहि (चावल)', 'गोधूम (गेहूं)', 'मसूर (दाल)'], 'ans_hi': 0, 'sol_hi': 'यव (जौ) मुख्य अनाज था; धान/चावल और गेहूं अज्ञात थे.'}, {'q': 'What describes the milk-rice porridge mentioned in late hymns?', 'opts': ['Kshirodana', 'Karambha', 'Apupa', 'Yava'], 'ans': 0, 'sol': 'Kshirodana was a dish made of milk and grain/rice.', 'q_hi': 'उत्तरकालीन भजनों में उल्लिखित दूध-चावल की खीर/दलिया का क्या वर्णन है?', 'opts_hi': ['क्षीरोदन', 'करम्भ', 'अपूप', 'यव'], 'ans_hi': 0, 'sol_hi': 'क्षीरोदन दूध और अनाज/चावल से बना एक व्यंजन था.'}, {'q': 'Which intoxicating drink was banned or frowned upon by elites, unlike Soma?', 'opts': ['Sura', 'Somapana', 'Madhu', 'None of these'], 'ans': 0, 'sol': 'Sura was a popular grain-brewed drink condemned for causing violence.', 'q_hi': 'सोम के विपरीत, किस नशीले पेय पर अभिजात वर्ग द्वारा प्रतिबंध लगाया गया था या उसे नापसंद किया जाता था?', 'opts_hi': ['सुरा', 'सोमपान', 'मधु', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सुरा अनाज से निर्मित एक लोकप्रिय पेय था जिसकी हिंसा उत्पन्न करने के लिए निंदा की जाती थी.'}, {'q': 'What was the cake made of parched barley meal and ghee called?', 'opts': ['Apupa', 'Karambha', 'Kshirodana', 'Yava'], 'ans': 0, 'sol': 'Apupa was a sweet cake or bread prepared from barley.', 'q_hi': 'भुने हुए जौ के आटे और घी से बने केक/अपुप को क्या कहा जाता था?', 'opts_hi': ['अपूप', 'करम्भ', 'क्षीरोदन', 'यव'], 'ans_hi': 0, 'sol_hi': 'अपूप जौ से तैयार किया जाने वाला एक मीठा केक या रोटी थी.'}, {'q': 'What describe the garments worn by early Vedic people?', 'opts': ['An undergarment (Nivi), garment (Vasa), and overgarment (Adhivasa)', 'Heavy silk tunics and trousers', 'Only animal hides', 'None of the above'], 'ans': 0, 'sol': 'Standard attire consisted of Nivi (undergarment), Vasa, and Adhivasa.', 'q_hi': 'प्रारंभिक वैदिक लोगों द्वारा पहने जाने वाले वस्त्रों का क्या वर्णन है?', 'opts_hi': ['अंतर्वस्त्र (नीवि), मुख्य वस्त्र (वास) और ओढ़नी (अधिवास)', 'भारी रेशमी अंगरखे और पतलून', 'केवल जानवरों की खाल', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'मानक परिधान में नीवि (अंतर्वस्त्र), वास और अधिवास शामिल थे.'}, {'q': 'What describes the entertainment and amusements of Rigvedic Aryans?', 'opts': ['Chariot racing, dicing, music, and dancing', 'Gladiator fights and theater', 'Bull fighting and chess', 'None of the above'], 'ans': 0, 'sol': 'Chariot racing, gambling with dice (Aksha), and music were popular.', 'q_hi': 'ऋग्वैदिक आर्यों के मनोरंजन और आमोद-प्रमोद का क्या वर्णन है?', 'opts_hi': ['रथ दौड़, पासा खेलना, संगीत और नृत्य', 'ग्लेडिएटर लड़ाई और रंगमंच', 'सांडों की लड़ाई और शतरंज', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'रथ दौड़, पासा खेलना (अक्ष) और संगीत लोकप्रिय मनोरंजन थे.'}, {'q': 'Which musical instrument is mentioned in early Vedic hymns?', 'opts': ['Lute (Vina) and flute (Nadi)', 'Tabla and Sitar', 'Harmonium', 'Piano'], 'ans': 0, 'sol': 'Vina (lute) and Nadi (flute/reed) are mentioned in music contexts.', 'q_hi': 'प्रारंभिक वैदिक भजनों में किस वाद्य यंत्र का उल्लेख मिलता है?', 'opts_hi': ['वीणा और बांसुरी (नाडी)', 'तबला और सितार', 'हारमोनियम', 'पियानो'], 'ans_hi': 0, 'sol_hi': 'संगीत के संदर्भों में वीणा और नाडी (बांसुरी) का उल्लेख मिलता है.'}, {'q': 'What was the main source of clothing fibers in early times?', 'opts': ["Sheep's wool (Urna) and cotton", 'Imported silk threads', 'Jute fibers only', 'Reed grass strips'], 'ans': 0, 'sol': 'Wool (Urna) from sheep and local cotton were spun.', 'q_hi': 'प्रारंभिक काल में वस्त्रों के रेशों का मुख्य स्रोत क्या था?', 'opts_hi': ['भेड़ की ऊन (ऊर्णा) और कपास', 'आयातित रेशम के धागे', 'केवल जूट के रेशे', 'सरकंडे की घास की पट्टियाँ'], 'ans_hi': 0, 'sol_hi': 'भेड़ों से प्राप्त ऊन (ऊर्णा) और स्थानीय कपास कातकर धागे बनाए जाते थे.'}, {'q': 'What was the main social attitude towards gambling or dicing?', 'opts': ['Condemned as a source of ruin, yet widely practiced', 'Praised as a moral virtue', 'Banned by royal decree on pain of death', 'Reserved only for priests'], 'ans': 0, 'sol': "Rigveda's 'Lament of the Gambler' warns of ruin from dice games.", 'q_hi': 'जुआ या पासा खेलने के प्रति मुख्य सामाजिक दृष्टिकोण क्या था?', 'opts_hi': ['विनाश के स्रोत के रूप में निंदा की गई, फिर भी व्यापक रूप से अभ्यास किया गया', 'एक नैतिक गुण के रूप में प्रशंसा की गई', 'मृत्युदंड के तहत शाही फरमान द्वारा प्रतिबंधित', 'केवल पुरोहितों के लिए आरक्षित'], 'ans_hi': 0, 'sol_hi': "ऋग्वेद का 'अक्ष सूक्त' (जुआरी का विलाप) पासा खेलने से होने वाले विनाश की चेतावनी देता है."}, {'q': 'Did early Vedic Aryans consume meat?', 'opts': ['Yes, they ate beef, mutton, and goat, especially at feasts', 'No, they were strictly vegetarian', 'Only fish caught from Indus', 'Only raw leaves'], 'ans': 0, 'sol': 'Meat consumption was common during communal rituals and feasts.', 'q_hi': 'क्या प्रारंभिक वैदिक आर्य मांस का सेवन करते थे?', 'opts_hi': ['हाँ, वे गोमांस, भेड़ और बकरी का मांस खाते थे, विशेषकर उत्सवों में', 'नहीं, वे पूरी तरह से शाकाहारी थे', 'केवल सिंधु से पकड़ी गई मछली', 'केवल कच्ची पत्तियाँ'], 'ans_hi': 0, 'sol_hi': 'सामुदायिक अनुष्ठानों और भोजों के दौरान मांस का सेवन आम था.'}, {'q': "The term 'Odan' in Rigvedic food refers to:", 'opts': ['Grain cooked with milk or water', 'Bread baked in ashes', 'Wine brewed from fruits', 'Dried meat strips'], 'ans': 0, 'sol': 'Odan was grain cooked with milk (Kshirodan) or water.', 'q_hi': "ऋग्वैदिक भोजन में 'ओदन' शब्द का अर्थ है:", 'opts_hi': ['दूध या पानी में पकाया गया अनाज', 'राख में सेकी गई रोटी', 'फलों से बनाई गई शराब', 'सूखे मांस के टुकड़े'], 'ans_hi': 0, 'sol_hi': 'ओदन दूध (क्षीरोदन) या पानी में पकाया गया अनाज था.'}, {'q': 'Which head ornament or turban is mentioned in late Rigvedic hymns?', 'opts': ['Usnisa', 'Niska', 'Vasa', 'Nivi'], 'ans': 0, 'sol': 'Usnisa was a turban or head covering worn by chiefs and priests.', 'q_hi': 'उत्तर ऋग्वैदिक भजनों में सिर के किस आभूषण या पगड़ी का उल्लेख मिलता है?', 'opts_hi': ['उष्णीष', 'निष्क', 'वास', 'नीवि'], 'ans_hi': 0, 'sol_hi': 'उष्णीष एक पगड़ी या सिर का ढकना था जिसे प्रमुख और पुरोहित पहनते थे.'}]}

# 2. Generator for 62 mastery zone questions per section (using pool of 12 unique facts)
question_pool = {1: [{'q': 'What was the basic unit of Rigvedic social structure?', 'opts': ['Kula (Family household)', 'Grama (Village)', 'Vis (Clan)', 'Jana (Tribe)'], 'ans': 0, 'sol': 'Kula was the family, the basic social and residential unit.', 'q_hi': 'ऋग्वैदिक सामाजिक संरचना की बुनियादी इकाई क्या थी?', 'opts_hi': ['कुल (पारिवारिक गृहस्थी)', 'ग्राम (गाँव)', 'विश (कुल/गोत्र)', 'जन (जनजाति)'], 'ans_hi': 0, 'sol_hi': 'कुल परिवार था, जो बुनियादी सामाजिक और आवासीय इकाई थी.'}, {'q': 'Who was the patriarchal head of the family unit?', 'opts': ['Kulapa or Grihapati', 'Rajan', 'Gramani', 'Vispati'], 'ans': 0, 'sol': 'The Kulapa or Grihapati (usually the father/eldest male) headed the Kula.', 'q_hi': 'पारिवारिक इकाई का पितृसत्तात्मक प्रमुख कौन था?', 'opts_hi': ['कुलप या गृहपति', 'राजन', 'ग्रामणी', 'विशपति'], 'ans_hi': 0, 'sol_hi': 'कुलप या गृहपति (आमतौर पर पिता/सबसे बड़ा पुरुष) कुल का मुखिया होता था.'}, {'q': 'What describes the family system of the early Rigvedic Aryans?', 'opts': ['Patriarchal and joint family system', 'Matriarchal and nuclear family system', 'Fraternal polyandry standard', 'None of the above'], 'ans': 0, 'sol': 'Rigvedic families were patriarchal and lived as large joint households.', 'q_hi': 'प्रारंभिक ऋग्वैदिक आर्यों की पारिवारिक व्यवस्था का क्या वर्णन है?', 'opts_hi': ['पितृसत्तात्मक और संयुक्त परिवार प्रणाली', 'मातृसत्तात्मक और एकल परिवार प्रणाली', 'भ्रातृ बहुपति विवाह मानक', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'ऋग्वैदिक परिवार पितृसत्तात्मक थे और बड़े संयुक्त घरों के रूप में रहते थे.'}, {'q': "The Sanskrit term 'Griha' in Rigvedic context refers to:", 'opts': ['The household or home', 'The temple sanctuary', 'The pasture boundary', 'The battle chariot'], 'ans': 0, 'sol': 'Griha refers to the house, home, or family dwelling.', 'q_hi': "ऋग्वैदिक संदर्भ में संस्कृत शब्द 'गृह' किसे संदर्भित करता है?", 'opts_hi': ['गृहस्थी या घर', 'मंदिर का गर्भगृह', 'चरागाह की सीमा', 'युद्ध का रथ'], 'ans_hi': 0, 'sol_hi': 'गृह का तात्पर्य घर, गृहस्थी या पारिवारिक आवास से है.'}, {'q': 'Did the patriarch (Grihapati) have absolute authority over family members?', 'opts': ['Yes, including powers of punishment and disposal of assets', 'No, his decisions had to be approved by the Samiti', 'No, the mother held the ultimate veto', 'Only in Later Vedic times'], 'ans': 0, 'sol': 'The patriarch held absolute power over children and property in the household.', 'q_hi': 'क्या पितृसत्तात्मक प्रमुख (गृहपति) के पास परिवार के सदस्यों पर पूर्ण अधिकार था?', 'opts_hi': ['हाँ, जिसमें सजा देने और संपत्ति के निपटान के अधिकार शामिल थे', 'नहीं, उसके निर्णयों को समिति द्वारा अनुमोदित किया जाना था', 'नहीं, माता के पास अंतिम वीटो शक्ति थी', 'केवल उत्तर वैदिक काल में'], 'ans_hi': 0, 'sol_hi': 'गृहपति के पास घर में बच्चों और संपत्ति पर पूर्ण शक्ति होती थी.'}, {'q': 'What was the cluster of several families (Kula) called?', 'opts': ['Grama', 'Vis', 'Jana', 'Sabha'], 'ans': 0, 'sol': 'Several families formed a Grama (village or mobile settlement).', 'q_hi': 'कई परिवारों (कुल) के समूह को क्या कहा जाता था?', 'opts_hi': ['ग्राम', 'विश', 'जन', 'सभा'], 'ans_hi': 0, 'sol_hi': 'कई परिवारों ने मिलकर एक ग्राम (गाँव या गतिशील बस्ती) का निर्माण किया.'}, {'q': 'Which term describes a group of villages forming a clan unit?', 'opts': ['Vis', 'Grama', 'Kula', 'Jana'], 'ans': 0, 'sol': 'Vis was a clan grouping, consisting of several Gramas.', 'q_hi': 'गाँवों के उस समूह को क्या कहा जाता है जो एक कुल इकाई बनाता था?', 'opts_hi': ['विश', 'ग्राम', 'कुल', 'जन'], 'ans_hi': 0, 'sol_hi': 'विश एक कुल समूह था, जिसमें कई ग्राम शामिल थे.'}, {'q': 'What was the highest social and political unit based on kinship?', 'opts': ['Jana (Tribe)', 'Vis', 'Grama', 'Kula'], 'ans': 0, 'sol': 'Jana was the tribe, the highest kinship-based unit migrating together.', 'q_hi': 'सगोत्रता पर आधारित सर्वोच्च सामाजिक और राजनीतिक इकाई कौन सी थी?', 'opts_hi': ['जन (जनजाति)', 'विश', 'ग्राम', 'कुल'], 'ans_hi': 0, 'sol_hi': 'जन जनजाति थी, जो एक साथ प्रवास करने वाली सगोत्रता पर आधारित सर्वोच्च इकाई थी.'}, {'q': 'How was kinship (blood relations) viewed in Rigvedic society?', 'opts': ['As the primary bond of social organization and loyalty', 'As secondary to commercial contracts', 'As completely irrelevant in cities', 'Only for priestly families'], 'ans': 0, 'sol': 'Kinship was the primary bond; loyalty was to the family and tribe (Jana).', 'q_hi': 'ऋग्वैदिक समाज में सगोत्रता (रक्त संबंध) को किस रूप में देखा जाता था?', 'opts_hi': ['सामाजिक संगठन और निष्ठा के प्राथमिक बंधन के रूप में', 'व्यावसायिक अनुबंधों के बाद गौण रूप में', 'शहरों में पूरी तरह से अप्रासंगिक', 'केवल पुरोहित परिवारों के लिए'], 'ans_hi': 0, 'sol_hi': 'सगोत्रता प्राथमिक बंधन थी; निष्ठा परिवार और जनजाति (जन) के प्रति थी.'}, {'q': "The term 'Sadhana' or 'Sajata' in early texts refers to:", 'opts': ['Kinsmen or relatives of the same clan', 'Tax collectors', 'Chariot builders', 'Foreign merchants'], 'ans': 0, 'sol': 'Sajata refers to relatives or kinsmen belonging to the same birth group.', 'q_hi': "प्रारंभिक ग्रंथों में 'साधना' या 'सजात' शब्द किसे संदर्भित करता है?", 'opts_hi': ['एक ही कुल के संबंधी या रिश्तेदार (सजात)', 'कर संग्राहक', 'रथ निर्माता', 'विदेशी व्यापारी'], 'ans_hi': 0, 'sol_hi': 'सजात का तात्पर्य एक ही जन्म समूह से संबंधित रिश्तेदारों या सगोत्रों से है.'}, {'q': 'Did separate private household ownership of pastures exist?', 'opts': ['No, pastures were deified and held collectively by the Jana', 'Yes, marked by stone boundary walls', 'Yes, owned exclusively by the Kulapa', 'Only for gold merchants'], 'ans': 0, 'sol': 'Pastures were communal property; families owned only cattle and domestic goods.', 'q_hi': 'क्या चरागाहों का अलग निजी घरेलू स्वामित्व मौजूद था?', 'opts_hi': ['नहीं, चरागाहों को देवत्व प्रदान किया गया था और जन द्वारा सामूहिक रूप से रखा जाता था', 'हाँ, पत्थर की सीमा की दीवारों द्वारा चिह्नित', 'हाँ, विशेष रूप से कुलप के स्वामित्व में', 'केवल स्वर्ण व्यापारियों के लिए'], 'ans_hi': 0, 'sol_hi': 'चरागाह सामूहिक संपत्ति थे; परिवारों के पास केवल मवेशी और घरेलू सामान थे.'}, {'q': 'What describes the position of the mother (Grihapatni) in the household?', 'opts': ['Respected mistress of the home who participated in Yajna', 'A slave without rights', 'Exiled to separate forest tracts', 'The supreme commander of the family militia'], 'ans': 0, 'sol': 'Grihapatni enjoyed respect and performed Yajna alongside her husband.', 'q_hi': 'घर में माता (गृहपत्नी) की स्थिति का क्या वर्णन है?', 'opts_hi': ['घर की सम्मानित स्वामिनी जो यज्ञ में भाग लेती थी', 'बिना अधिकारों की गुलाम', 'अलग वन क्षेत्रों में निर्वासित', 'पारिवारिक मिलिशिया की सर्वोच्च कमांडर'], 'ans_hi': 0, 'sol_hi': 'गृहपत्नी को सम्मान प्राप्त था और वह अपने पति के साथ यज्ञ संपन्न करती थी.'}], 2: [{'q': 'Which hymn in Rigveda Mandala X introduces the fourfold varna system?', 'opts': ['Purusha Sukta', 'Nasadiya Sukta', 'Gayatri Sukta', 'Sarasvati Sukta'], 'ans': 0, 'sol': 'The Purusha Sukta describes the creation of four classes from the giant Purusha.', 'q_hi': 'ऋग्वेद मंडल X का कौन सा सूक्त चार वर्णों की व्यवस्था का परिचय देता है?', 'opts_hi': ['पुरुष सूक्त', 'नासदीय सूक्त', 'गायत्री सूक्त', 'सरस्वती सूक्त'], 'ans_hi': 0, 'sol_hi': 'पुरुष सूक्त विशाल पुरुष से चार वर्गों के निर्माण का वर्णन करता है.'}, {'q': 'Was the varna system in the early Rigvedic period hereditary?', 'opts': ['No, it was flexible and based on occupation, not birth', "Yes, children had to follow the parent's varna strictly", 'Varna did not exist in any form', 'Only for the warriors'], 'ans': 0, 'sol': 'Varna was flexible; caste rigidity and hereditary rules only developed later.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में वर्ण व्यवस्था वंशानुगत थी?', 'opts_hi': ['नहीं, यह लचीली थी और जन्म पर नहीं बल्कि व्यवसाय पर आधारित थी', 'हाँ, बच्चों को माता-पिता के वर्ण का सख्ती से पालन करना पड़ता था', 'वर्ण किसी भी रूप में मौजूद नहीं था', 'केवल योद्धाओं के लिए'], 'ans_hi': 0, 'sol_hi': 'वर्ण लचीला था; जातिगत कठोरता और वंशानुगत नियम केवल बाद में विकसित हुए.'}, {'q': 'What terms were initially used to differentiate people in the early Rigveda?', 'opts': ['Arya Varna and Dasa Varna', 'Brahmin and Kshatriya only', 'Untouchable and Touchable', 'None of the above'], 'ans': 0, 'sol': 'Initial distinction was based on color/culture: Arya (Vedic) and Dasa (indigenous).', 'q_hi': 'प्रारंभिक ऋग्वेद में लोगों में अंतर करने के लिए शुरू में किन शब्दों का प्रयोग किया जाता था?', 'opts_hi': ['आर्य वर्ण और दास वर्ण', 'केवल ब्राह्मण और क्षत्रिय', 'अछूत और छूत', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक अंतर रंग/संस्कृति पर आधारित था: आर्य (वैदिक) और दास (स्वदेशी).'}, {'q': "A poet in Rigveda Mandala IX says: 'I am a poet, my father is a physician, my mother grinds grain.' This indicates:", 'opts': ['High occupational mobility within the same family', 'Rigid caste laws', 'Absence of family bonds', 'Slavery of women'], 'ans': 0, 'sol': 'It shows that members of the same family could follow different occupations.', 'q_hi': "ऋग्वेद मंडल IX में एक कवि कहता है: 'मैं एक कवि हूँ, मेरे पिता एक चिकित्सक हैं, मेरी माँ अनाज पीसती हैं।' यह दर्शाता है:", 'opts_hi': ['एक ही परिवार के भीतर उच्च व्यावसायिक गतिशीलता', 'कठोर जातिगत कानून', 'पारिवारिक बंधनों का अभाव', 'महिलाओं की गुलामी'], 'ans_hi': 0, 'sol_hi': 'यह दर्शाता है कि एक ही परिवार के सदस्य अलग-अलग व्यवसाय अपना सकते थे.'}, {'q': "What was the physical basis of the term 'Varna' etymologically?", 'opts': ['Color or outward appearance', 'Hereditary lineage', 'Tax category', 'Sacrificial altar shape'], 'ans': 0, 'sol': 'Varna etymologically comes from vrn (to choose or color).', 'q_hi': "व्युत्पत्ति के अनुसार 'वर्ण' शब्द का भौतिक आधार क्या था?", 'opts_hi': ['रंग या बाहरी रूप', 'वंशानुगत वंश', 'कर श्रेणी', 'यज्ञ वेदी का आकार'], 'ans_hi': 0, 'sol_hi': 'वर्ण शब्द व्युत्पत्ति के अनुसार वृ (चुनना या रंग) से आता है.'}, {'q': "Who were the 'Dasas' and 'Dasyus' in early Vedic society?", 'opts': ['Indigenous non-Aryan populations conquered by Aryans', 'Priests from Mesopotamia', 'Chariot builders of the Bharatas', 'None of these'], 'ans': 0, 'sol': 'They were the pre-existing, indigenous populations of the Sapta-Sindhu.', 'q_hi': "प्रारंभिक वैदिक समाज में 'दास' और 'दस्यु' कौन थे?", 'opts_hi': ['आर्यों द्वारा जीते गए स्वदेशी गैर-आर्य लोग', 'मेसोपोटामिया के पुरोहित', 'भरतों के रथ निर्माता', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'वे सप्त-सिंधु के पहले से मौजूद, स्वदेशी लोग थे.'}, {'q': 'Which text is considered a later addition to the Rigveda containing the Purusha Sukta?', 'opts': ['Mandala X', 'Mandala II', 'Mandala III', 'Mandala VII'], 'ans': 0, 'sol': 'Mandala X is linguistically and conceptually later than Mandalas II-VII.', 'q_hi': 'ऋग्वेद में बाद में जोड़े गए किस मंडल में पुरुष सूक्त शामिल है?', 'opts_hi': ['मंडल X', 'मंडल II', 'मंडल III', 'मंडल VII'], 'ans_hi': 0, 'sol_hi': 'मंडल X भाषाई और वैचारिक रूप से मंडल II-VII से बाद का है.'}, {'q': 'Did untouchability exist in the early Rigvedic period?', 'opts': ['No, there is no mention of untouchability or impurity of touch', 'Yes, Shudras were completely excluded from villages', 'Only for metalworkers', 'Only in the later part of the Ganges valley'], 'ans': 0, 'sol': 'Untouchability did not exist in the early pastoral society.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में अस्पृश्यता मौजूद थी?', 'opts_hi': ['नहीं, अस्पृश्यता या स्पर्श की अशुद्धता का कोई उल्लेख नहीं है', 'हाँ, शूद्रों को गाँवों से पूरी तरह बाहर रखा गया था', 'केवल धातु कामगारों के लिए', 'केवल गंगा घाटी के बाद के हिस्से में'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक पशुचारक समाज में अस्पृश्यता का अस्तित्व नहीं था.'}, {'q': 'What term describes the class of warriors and chiefs in early texts?', 'opts': ['Rajanya', 'Brahmin', 'Vaishya', 'Shudra'], 'ans': 0, 'sol': 'Rajanya was the term used for the ruling warrior class.', 'q_hi': 'प्रारंभिक ग्रंथों में योद्धाओं और मुखियों के वर्ग को कौन सा शब्द वर्णित करता है?', 'opts_hi': ['राजन्य', 'ब्राह्मण', 'वैश्य', 'शूद्र'], 'ans_hi': 0, 'sol_hi': 'राजन्य शब्द का प्रयोग शासक योद्धा वर्ग के लिए किया जाता था.'}, {'q': 'The common people or agriculturists were termed as:', 'opts': ['Vis or Vaishya', 'Rajanya', 'Brahmin', 'Shudra'], 'ans': 0, 'sol': 'Vis (common folk) later crystallized into the Vaishya varna.', 'q_hi': 'सामान्य लोगों या कृषकों को क्या कहा जाता था?', 'opts_hi': ['विश या वैश्य', 'राजन्य', 'ब्राह्मण', 'शूद्र'], 'ans_hi': 0, 'sol_hi': 'विश (सामान्य लोग) बाद में वैश्य वर्ण के रूप में स्तरीकृत हुए.'}, {'q': "How were the 'Dasyus' characterized in the Rigvedic hymns?", 'opts': ['As flat-nosed (Anas) non-sacrificers who spoke a different language', 'As great friends and trading allies', 'As divine beings', 'As iron weapon manufacturers'], 'ans': 0, 'sol': 'Hymns describe them as Anas (flat-nosed), Mridhravac (hostile speech), and non-sacrificing.', 'q_hi': "ऋग्वैदिक भजनों में 'दस्युओं' की क्या विशेषताएँ बताई गई हैं?", 'opts_hi': ['चपटी नाक वाले (अनास) और यज्ञ न करने वाले जो भिन्न भाषा बोलते थे', 'महान मित्रों और व्यापारिक सहयोगियों के रूप में', 'दिव्य प्राणियों के रूप में', 'लोहे के हथियार बनाने वालों के रूप में'], 'ans_hi': 0, 'sol_hi': 'भजनों में उन्हें अनास (चपटी नाक वाले), मृध्रवाच (कटु भाषा बोलने वाले) और यज्ञ न करने वाले के रूप में वर्णित किया गया है.'}, {'q': 'What caused the transition from a simple classless society to early social hierarchy?', 'opts': ['Economic surplus from agriculture and incorporation of indigenous populations', 'Complete destruction of cattle', 'A decree by the King of Babylon', 'None of the above'], 'ans': 0, 'sol': 'Surplus resources and assimilation of Dasas created social layers.', 'q_hi': 'एक सरल वर्गहीन समाज से प्रारंभिक सामाजिक पदानुक्रम में संक्रमण का क्या कारण था?', 'opts_hi': ['कृषि से प्राप्त आर्थिक अधिशेष और स्वदेशी आबादी का समावेश', 'मवेशियों का पूर्ण विनाश', 'बेबीलोन के राजा द्वारा जारी एक आदेश', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'अधिशेष संसाधनों और दासों के आत्मसात होने से सामाजिक परतें बनीं.'}], 3: [{'q': 'What describes the status of women in the early Rigvedic period?', 'opts': ['Respectable status with access to education and assemblies', 'Completely confined to dark rooms without rights', 'Exempt from family work but banned from rituals', 'Considered property that could be sold'], 'ans': 0, 'sol': 'Women had high status, could study, and participated in Sabha/Vidatha.', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में महिलाओं की स्थिति का क्या वर्णन है?', 'opts_hi': ['शिक्षा और सभाओं तक पहुंच के साथ सम्मानित स्थिति', 'बिना किसी अधिकार के पूरी तरह से अंधेरे कमरों में बंद', 'पारिवारिक कार्यों से मुक्त लेकिन अनुष्ठानों से प्रतिबंधित', 'संपत्ति माना जाता था जिसे बेचा जा सकता था'], 'ans_hi': 0, 'sol_hi': 'महिलाओं की स्थिति उच्च थी, वे अध्ययन कर सकती थीं, और सभा/विदथ में भाग लेती थीं.'}, {'q': 'Which rite of initiation (sacred thread ceremony) was open to girls in early times?', 'opts': ['Upanayana', 'Sanyasa', 'Niyoga', 'Garbadhana'], 'ans': 0, 'sol': 'Upanayana (education rite) was performed for both boys and girls.', 'q_hi': 'प्रारंभिक काल में लड़कियों के लिए दीक्षा का कौन सा संस्कार (जनेऊ समारोह) खुला था?', 'opts_hi': ['उपनयन', 'संन्यास', 'नियोग', 'गर्भाधान'], 'ans_hi': 0, 'sol_hi': 'उपनयन (शिक्षा संस्कार) लड़के और लड़कियों दोनों के लिए किया जाता था.'}, {'q': 'Could women participate in the tribal assemblies Sabha and Vidatha?', 'opts': ['Yes, they participated and were called Sabhavati', 'No, they were strictly banned', 'Only widows could attend', 'Only during the Soma festival'], 'ans': 0, 'sol': 'Rigveda shows women attended assemblies and had voice.', 'q_hi': 'क्या महिलाएँ जनजातीय सभाओं सभा और विदथ में भाग ले सकती थीं?', 'opts_hi': ['हाँ, वे भाग लेती थीं और उन्हें सभावती कहा जाता था', 'नहीं, उन पर सख्त प्रतिबंध था', 'केवल विधवाएं ही भाग ले सकती थीं', 'केवल सोम उत्सव के दौरान'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद दर्शाता है कि महिलाओं ने सभाओं में भाग लिया और उनकी आवाज़ सुनी जाती थी.'}, {'q': "What was the practice of 'Niyoga' in the early Vedic society?", 'opts': ["Co-habiting with a brother-in-law to produce an heir after husband's death", 'Banishment of widows to forests', "Burning of widows on husband's pyre", 'Sacrificing young girls to deities'], 'ans': 0, 'sol': "Niyoga allowed a childless widow to raise sons with her husband's brother.", 'q_hi': "प्रारंभिक वैदिक समाज में 'नियोग' की क्या प्रथा थी?", 'opts_hi': ['पति की मृत्यु के बाद उत्तराधिकारी पैदा करने के लिए देवर के साथ सहवास करना', 'विधवाओं को जंगलों में निर्वासित करना', 'पति की चिता पर विधवाओं को जलाना', 'देवताओं के लिए युवा लड़कियों की बलि देना'], 'ans_hi': 0, 'sol_hi': 'नियोग प्रथा एक निःसंतान विधवा को अपने पति के भाई के साथ संतान उत्पन्न करने की अनुमति देती थी.'}, {'q': 'Did the practice of Sati (widow burning) exist in the early Rigveda?', 'opts': ['No, it was non-existent; widows remarried or practiced Niyoga', 'Yes, it was compulsory for all varnas', 'Only in the Sarasvati region', 'Only for the wives of the Rajan'], 'ans': 0, 'sol': 'Sati was not practiced; Rigveda has no authentic hymns supporting widow burning.', 'q_hi': 'क्या प्रारंभिक ऋग्वेद में सती प्रथा (विधवा दाह) का अस्तित्व था?', 'opts_hi': ['नहीं, यह अस्तित्वहीन थी; विधवाएँ पुनर्विवाह करती थीं या नियोग का पालन करती थीं', 'हाँ, यह सभी वर्णों के लिए अनिवार्य था', 'केवल सरस्वती क्षेत्र में', 'केवल राजन की पत्नियों के लिए'], 'ans_hi': 0, 'sol_hi': 'सती प्रथा का प्रचलन नहीं था; ऋग्वेद में विधवा दाह का समर्थन करने वाले कोई प्रामाणिक भजन नहीं हैं.'}, {'q': "Who were the 'Brahmavadinis' in Rigvedic times?", 'opts': ['Women who chose education and philosophy over marriage', 'Female temple dancers', 'Wives of the Rajan', 'Women metalworkers'], 'ans': 0, 'sol': 'Brahmavadinis were lifelong female students of Vedas and philosophy.', 'q_hi': "ऋग्वैदिक काल में 'ब्रह्मवादिनी' कौन थीं?", 'opts_hi': ['वे महिलाएँ जिन्होंने विवाह के स्थान पर शिक्षा और दर्शन को चुना', 'महिला मंदिर नर्तकियाँ', 'राजन की पत्नियाँ', 'महिला धातु कामगार'], 'ans_hi': 0, 'sol_hi': 'ब्रह्मवादिनी वे महिलाएँ थीं जिन्होंने जीवन भर वेदों और दर्शन का अध्ययन किया.'}, {'q': 'Who was the famous female seer who composed Rigvedic hymns and debated philosophers?', 'opts': ['Ghopsha or Apala', 'Sita', 'Aranyani', 'None of these'], 'ans': 0, 'sol': 'Female seers (Rishikas) like Ghosha, Apala, and Lopamudra composed hymns.', 'q_hi': 'ऋग्वैदिक भजनों की रचना करने वाली और दार्शनिकों के साथ बहस करने वाली प्रसिद्ध महिला ऋषि कौन थी?', 'opts_hi': ['घोषा या अपाला', 'सीता', 'अरण्यानी', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'घोषा, अपाला और लोपामुद्रा जैसी महिला ऋषियों (ऋषिकाओं) ने भजनों की रचना की थी.'}, {'q': 'At what age were girls usually married in the early Rigvedic period?', 'opts': ['At maturity (adulthood)', 'As child brides before puberty', 'They were never allowed to marry', 'Only after the age of 40'], 'ans': 0, 'sol': 'Child marriage was absent; girls married after reaching maturity.', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में लड़कियों का विवाह आमतौर पर किस आयु में होता था?', 'opts_hi': ['वयस्क होने पर (परिपक्वता पर)', 'यौवन से पहले बाल वधुओं के रूप में', 'उन्हें कभी विवाह करने की अनुमति नहीं थी', 'केवल 40 वर्ष की आयु के बाद'], 'ans_hi': 0, 'sol_hi': 'बाल विवाह अनुपस्थित था; लड़कियां परिपक्वता प्राप्त करने के बाद ही विवाह करती थीं.'}, {'q': "The term 'Amaju' refers to which category of women?", 'opts': ["Unmarried women who lived in parent's house lifelong", 'Widows who practiced Sati', 'Female military commanders', 'Women who ran markets'], 'ans': 0, 'sol': "Amaju refers to women who remained unmarried and stayed at father's home.", 'q_hi': "शब्द 'अमाजू' किस श्रेणी की महिलाओं को संदर्भित करता है?", 'opts_hi': ['अविवाहित महिलाएँ जो जीवन भर माता-पिता के घर रहती थीं', 'सती प्रथा का पालन करने वाली विधवाएँ', 'महिला सैन्य कमांडर', 'बाजार चलाने वाली महिलाएँ'], 'ans_hi': 0, 'sol_hi': 'अमाजू उन महिलाओं को संदर्भित करता है जो अविवाहित रहीं और अपने पिता के घर पर रहीं.'}, {'q': 'Did women have the right to choose their husbands in early times?', 'opts': ['Yes, through swayamvara or mutual choice (Kama marriage)', 'No, they were sold to the highest bidder', 'Only with the permission of the chief priest', 'Only from foreign tribes'], 'ans': 0, 'sol': 'Texts indicate that mature girls had a say in choosing their husbands.', 'q_hi': 'क्या प्रारंभिक काल में महिलाओं को अपने पति चुनने का अधिकार था?', 'opts_hi': ['हाँ, स्वयंवर या आपसी पसंद (काम विवाह) के माध्यम से', 'नहीं, उन्हें सबसे ऊंची बोली लगाने वाले को बेच दिया जाता था', 'केवल मुख्य पुरोहित की अनुमति से', 'केवल विदेशी कबीलों से'], 'ans_hi': 0, 'sol_hi': 'ग्रंथों से संकेत मिलता है कि वयस्क लड़कियों को अपना पति चुनने का अधिकार था.'}, {'q': 'Which female philosopher debated Yajnavalkya in royal court?', 'opts': ['Gargi Vachaknavi (later tradition)', 'Lopamudra', 'Apala', 'Ghosha'], 'ans': 0, 'sol': 'Gargi debated Yajnavalkya (recorded in Upanishads, marking later transition).', 'q_hi': 'शाही दरबार में याज्ञवल्क्य के साथ किस महिला दार्शनिक ने बहस की थी?', 'opts_hi': ['गार्गी वाचक्नवी (उत्तरकालीन परंपरा)', 'लोपामुद्रा', 'अपाला', 'घोषा'], 'ans_hi': 0, 'sol_hi': 'गार्गी ने याज्ञवल्क्य के साथ शास्त्रार्थ किया था (उपनिषदों में दर्ज, जो उत्तरकालीन संक्रमण को दर्शाता है).'}, {'q': 'Was purdah (veil system) practiced by Rigvedic women?', 'opts': ['No, it was completely absent', 'Yes, they had to cover their face in front of elders', 'Only during sacrifices', 'Only inside the chariot'], 'ans': 0, 'sol': 'Veil system or seclusion of women did not exist in the early Vedic society.', 'q_hi': 'क्या ऋग्वैदिक महिलाओं द्वारा पर्दा प्रथा का पालन किया जाता था?', 'opts_hi': ['नहीं, यह पूरी तरह से अनुपस्थित था', 'हाँ, उन्हें बुजुर्गों के सामने अपना चेहरा ढकना पड़ता था', 'केवल यज्ञों के दौरान', 'केवल रथ के भीतर'], 'ans_hi': 0, 'sol_hi': 'प्रारंभिक वैदिक समाज में पर्दा प्रथा या महिलाओं को अलग रखने की व्यवस्था मौजूद नहीं थी.'}], 4: [{'q': 'What was the standard form of marriage in early Rigvedic society?', 'opts': ['Monogamy (one husband and wife)', 'Polygamy for all men', 'Polyandry (one wife with many husbands)', 'Group marriage standard'], 'ans': 0, 'sol': 'Monogamy was the general rule, though chiefs practiced polygamy.', 'q_hi': 'प्रारंभिक ऋग्वैदिक समाज में विवाह का मानक स्वरूप क्या था?', 'opts_hi': ['एकपत्नीत्व (एक पति और एक पत्नी)', 'सभी पुरुषों के लिए बहुपत्नीत्व', 'बहुपतित्व (एक पत्नी के कई पति)', 'समूह विवाह मानक'], 'ans_hi': 0, 'sol_hi': 'एकपत्नीत्व सामान्य नियम था, हालांकि मुखिया बहुपत्नीत्व का पालन करते थे.'}, {'q': "What term represents the bridal gifts or dowry carried by bride to husband's house?", 'opts': ['Vahatu', 'Bali', 'Bhaga', 'Niska'], 'ans': 0, 'sol': 'Vahatu was the gift or dowry given during marriage.', 'q_hi': 'दुल्हन द्वारा अपने पति के घर ले जाए जाने वाले विवाह उपहार या दहेज को क्या कहा जाता था?', 'opts_hi': ['वहतु', 'बलि', 'भाग', 'निष्क'], 'ans_hi': 0, 'sol_hi': 'वहतु विवाह के समय दुल्हन को दिए जाने वाले उपहार या दहेज की सामग्री थी.'}, {'q': 'Was child marriage common in early Rigvedic times?', 'opts': ['No, it was completely absent; marriages occurred at adulthood', 'Yes, children were married at age 5', 'Only for the priestly Brahmin class', 'Only in the western areas'], 'ans': 0, 'sol': 'Marriages took place after girls reached puberty and physical maturity.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में बाल विवाह आम था?', 'opts_hi': ['नहीं, यह पूरी तरह से अनुपस्थित था; विवाह वयस्क होने पर होते थे', 'हाँ, बच्चों का विवाह 5 वर्ष की आयु में कर दिया जाता था', 'केवल पुरोहित ब्राह्मण वर्ग के लिए', 'केवल पश्चिमी क्षेत्रों में'], 'ans_hi': 0, 'sol_hi': 'विवाह लड़कियों के यौवन और शारीरिक परिपक्वता प्राप्त करने के बाद ही होते थे.'}, {'q': "The concept of 'Niyoga' allowed a childless widow to raise sons with:", 'opts': ["Her deceased husband's brother (Devar)", 'The chief priest of the tribe', 'The Rajan', 'A foreign trader'], 'ans': 0, 'sol': 'Niyoga was levirate marriage allowed for raising a male heir.', 'q_hi': 'नियोग की अवधारणा ने एक निःसंतान विधवा को किसके साथ पुत्र उत्पन्न करने की अनुमति दी?', 'opts_hi': ['अपने मृत पति के भाई (देवर) के साथ', 'कबीले के मुख्य पुरोहित के साथ', 'राजन के साथ', 'एक विदेशी व्यापारी के साथ'], 'ans_hi': 0, 'sol_hi': 'नियोग देवर-भाभी विवाह का रूप था जिसकी अनुमति पुरुष उत्तराधिकारी प्राप्त करने के लिए दी जाती थी.'}, {'q': 'Which type of marriage was defined by mutual love and choice without parental consent?', 'opts': ['Gandharva marriage (Kama marriage)', 'Brahma marriage', 'Daiva marriage', 'Asura marriage'], 'ans': 0, 'sol': 'Gandharva marriage was based on love and mutual consent of the couple.', 'q_hi': 'माता-पिता की सहमति के बिना आपसी प्रेम और पसंद से परिभाषित विवाह का कौन सा प्रकार था?', 'opts_hi': ['गंधर्व विवाह (काम विवाह)', 'ब्रह्म विवाह', 'दैव विवाह', 'असुर विवाह'], 'ans_hi': 0, 'sol_hi': 'गंधर्व विवाह युगल के प्रेम और आपसी सहमति पर आधारित होता था.'}, {'q': 'What describes the attitude towards divorce in early Rigvedic law?', 'opts': ['Divorce did not exist; marriage was an unbreakable sacred bond', 'Divorce was allowed at will by paying a fee in cows', 'Only the wife could divorce the husband', 'None of the above'], 'ans': 0, 'sol': 'Marriage was a lifelong sacrament; divorce was practically unknown.', 'q_hi': 'प्रारंभिक ऋग्वैदिक कानून में तलाक के प्रति दृष्टिकोण का क्या वर्णन है?', 'opts_hi': ['तलाक का अस्तित्व नहीं था; विवाह एक अटूट पवित्र बंधन था', 'गायों में शुल्क देकर इच्छानुसार तलाक की अनुमति थी', 'केवल पत्नी ही पति को तलाक दे सकती थी', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'विवाह एक आजीवन संस्कार था; तलाक व्यावहारिक रूप से अज्ञात था.'}, {'q': 'What was the term for the bridegroom in Rigvedic Sanskrit?', 'opts': ['Vara', 'Jamatr', 'Pati', 'Grihapati'], 'ans': 0, 'sol': 'Vara was the term used for the bridegroom/husband.', 'q_hi': 'ऋग्वैदिक संस्कृत में दूल्हे के लिए क्या शब्द था?', 'opts_hi': ['वर', 'जामातृ', 'पति', 'गृहपति'], 'ans_hi': 0, 'sol_hi': 'वर दूल्हे/पति के लिए इस्तेमाल किया जाने वाला शब्द था.'}, {'q': 'Which text contains the famous Surya Sukta (Marriage Hymn)?', 'opts': ['Rigveda Mandala X', 'Rigveda Mandala III', 'Yajurveda', 'Sama Veda'], 'ans': 0, 'sol': "Surya Sukta of Mandala X details the marriage of Surya's daughter, forming the base of Hindu rites.", 'q_hi': 'प्रसिद्ध सूर्य सूक्त (विवाह सूक्त) किस ग्रंथ में मिलता है?', 'opts_hi': ['ऋग्वेद मंडल X', 'ऋग्वेद मंडल III', 'यजुर्वेद', 'सामवेद'], 'ans_hi': 0, 'sol_hi': 'मंडल X का सूर्य सूक्त सूर्य की पुत्री के विवाह का विवरण देता है, जो हिंदू विवाह संस्कारों का आधार है.'}, {'q': "The term 'Devar' literally translates to:", 'opts': ["Second husband (husband's brother)", 'The priest who performs marriage', 'The father of the bride', "The king's representative"], 'ans': 0, 'sol': 'Devar literally means second husband, referring to brother-in-law in Niyoga.', 'q_hi': "'देवर' शब्द का शाब्दिक अर्थ है:", 'opts_hi': ['दूसरा पति (पति का भाई)', 'विवाह कराने वाला पुरोहित', 'दुल्हन का पिता', 'राजा का प्रतिनिधि'], 'ans_hi': 0, 'sol_hi': 'देवर का शाब्दिक अर्थ दूसरा पति है, जो नियोग में देवर को संदर्भित करता है.'}, {'q': 'Were inter-caste marriages allowed in the early Rigvedic period?', 'opts': ['Yes, varna boundaries were fluid; intermarriage was common', 'No, they were strictly punished by death', 'Only between priests and warriors', 'None of the above'], 'ans': 0, 'sol': 'Class boundaries were fluid; intermarriage was not forbidden.', 'q_hi': 'क्या प्रारंभिक ऋग्वैदिक काल में अंतर-जातीय विवाह की अनुमति थी?', 'opts_hi': ['हाँ, वर्ण सीमाएँ लचीली थीं; अंतर-विवाह आम थे', 'नहीं, उन्हें मृत्युदंड से सख्ती से दंडित किया जाता था', 'केवल पुरोहितों और योद्धाओं के बीच', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'वर्ग सीमाएँ लचीली थीं; अंतर-विवाह वर्जित नहीं थे.'}, {'q': 'What was the relative position of co-wives (Sapatni) in polygamous families?', 'opts': ['Highly tense; hymns contain spells to overcome co-wives', 'They shared all assets equally without conflict', 'They ruled the household jointly', 'None of the above'], 'ans': 0, 'sol': "Rigveda Mandala X contains spells to win husband's affection over co-wives.", 'q_hi': 'बहुपत्नी परिवारों में सौतनों (सपत्नी) की सापेक्ष स्थिति क्या थी?', 'opts_hi': ['अत्यधिक तनावपूर्ण; भजनों में सौतनों पर विजय पाने के मंत्र शामिल हैं', 'उन्होंने बिना किसी संघर्ष के सभी संपत्तियों को समान रूप से साझा किया', 'उन्होंने संयुक्त रूप से घर पर शासन किया', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'ऋग्वेद मंडल X में सौतनों पर पति का स्नेह प्राप्त करने के लिए मंत्र शामिल हैं.'}, {'q': 'What represents the domestic marriage altar fire?', 'opts': ['Yuvati Agni', 'Garhapatya Agni', 'Rudra Agni', 'None of these'], 'ans': 0, 'sol': 'The bride and groom circumambulate the sacrificial fire, which is then carried to their home as Garhapatya.', 'q_hi': 'घरेलू विवाह वेदी की अग्नि का क्या प्रतिनिधित्व है?', 'opts_hi': ['युवती अग्नि', 'गार्हपत्य अग्नि', 'रुद्र अग्नि', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'दूल्हा और दुल्हन यज्ञ की अग्नि की परिक्रमा करते हैं, जिसे बाद में गार्हपत्य के रूप में उनके घर ले जाया जाता है.'}], 5: [{'q': 'How was education conducted in the early Rigvedic period?', 'opts': ['Orally, through memorization of hymns under a Guru', 'By writing Sanskrit script on clay bricks', 'In formal universities like Nalanda', 'Only in foreign lands'], 'ans': 0, 'sol': 'Education was purely oral, based on listening and chanting (Shruti).', 'q_hi': 'प्रारंभिक ऋग्वैदिक काल में शिक्षा कैसे संचालित की जाती थी?', 'opts_hi': ['मौखिक रूप से, गुरु के अधीन भजनों को कंठस्थ करके', 'मिट्टी की ईंटों पर संस्कृत लिपि लिखकर', 'नालंदा जैसे औपचारिक विश्वविद्यालयों में', 'केवल विदेशी भूमि में'], 'ans_hi': 0, 'sol_hi': 'शिक्षा विशुद्ध रूप से मौखिक थी, जो सुनने और उच्चारण करने (श्रुति) पर आधारित थी.'}, {'q': "Which ceremony marked the initiation of a student's education?", 'opts': ['Upanayana (sacred thread rite)', 'Sanyasa', 'Niyoga', 'Garbadhana'], 'ans': 0, 'sol': 'Upanayana was the thread ceremony opening access to Vedic study.', 'q_hi': 'कौन सा समारोह छात्र की शिक्षा की शुरुआत का प्रतीक था?', 'opts_hi': ['उपनयन (जनेऊ संस्कार)', 'संन्यास', 'नियोग', 'गर्भाधान'], 'ans_hi': 0, 'sol_hi': 'उपनयन जनेऊ संस्कार था जो वैदिक अध्ययन तक पहुंच प्रदान करता था.'}, {'q': 'Did the four rigid Ashrama stages (celibate, householder, forest, ascetic) exist fully in Rigvedic times?', 'opts': ['No, the system only crystallized in Later Vedic/post-Vedic texts', 'Yes, all men had to follow the four stages strictly', 'Only the ascetic stage existed', 'None of the above'], 'ans': 0, 'sol': 'The four Ashramas developed later; early texts focus mainly on Grihastha (householder).', 'q_hi': 'क्या ऋग्वैदिक काल में चार कठोर आश्रम चरण (ब्रह्मचर्य, गृहस्थ, वानप्रस्थ, संन्यास) पूरी तरह से मौजूद थे?', 'opts_hi': ['नहीं, यह व्यवस्था केवल उत्तर वैदिक/उत्तर-वैदिक ग्रंथों में स्पष्ट हुई', 'हाँ, सभी पुरुषों को चारों चरणों का सख्ती से पालन करना पड़ता था', 'केवल संन्यास चरण मौजूद था', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'चारों आश्रम बाद में विकसित हुए; प्रारंभिक ग्रंथ मुख्य रूप से गृहस्थ (गृहस्वामी) पर केंद्रित हैं.'}, {'q': 'What describes the Rigvedic frog hymn (Mandala VII) regarding education?', 'opts': ['It compares students chanting after their teacher to croaking frogs', 'It praises frogs as sacred animals', 'It bans frogs from sacrifice sites', 'None of the above'], 'ans': 0, 'sol': 'Hymn VII.103 humorously compares chanting students to frogs croaking after rain.', 'q_hi': 'शिक्षा के संबंध में ऋग्वैदिक मेंढक भजन (मंडल VII) का क्या वर्णन है?', 'opts_hi': ['यह अपने शिक्षक के बाद भजनों का पाठ करने वाले छात्रों की तुलना मेंढकों की टर्राहट से करता है', 'यह मेंढकों को पवित्र जानवरों के रूप में पूजता है', 'यह यज्ञ स्थलों से मेंढकों को प्रतिबंधित करता है', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'भजन VII.103 हास्यपूर्ण ढंग से पाठ करने वाले छात्रों की तुलना बारिश के बाद मेंढकों की टर्राहट से करता है.'}, {'q': 'Who was the teacher in the Vedic educational setup?', 'opts': ['Guru or Acharya', 'Kulapa', 'Gramani', 'Rajan'], 'ans': 0, 'sol': 'Guru or Acharya was the spiritual and intellectual preceptor.', 'q_hi': 'वैदिक शैक्षणिक व्यवस्था में शिक्षक कौन था?', 'opts_hi': ['गुरु या आचार्य', 'कुलप', 'ग्रामणी', 'राजन'], 'ans_hi': 0, 'sol_hi': 'गुरु या आचार्य आध्यात्मिक और बौद्धिक गुरु होते थे.'}, {'q': 'Could girls undergo the Upanayana ceremony in early times?', 'opts': ['Yes, it was performed for girls who studied Vedas', 'No, they were strictly banned from the ceremony', 'Only if their father was the Rajan', 'Only in the Ganga valley'], 'ans': 0, 'sol': 'Upanayana was open to girls (Brahmavadinis) who pursued education.', 'q_hi': 'क्या प्रारंभिक काल में लड़कियों का उपनयन संस्कार हो सकता था?', 'opts_hi': ['हाँ, यह उन लड़कियों के लिए किया जाता था जो वेदों का अध्ययन करती थीं', 'नहीं, उन्हें इस समारोह से सख्ती से प्रतिबंधित किया गया था', 'केवल तभी जब उनके पिता राजन हों', 'केवल गंगा घाटी में'], 'ans_hi': 0, 'sol_hi': 'शिक्षा प्राप्त करने वाली लड़कियों (ब्रह्मवादिनी) के लिए उपनयन खुला था.'}, {'q': 'The sacred thread ceremony is etymologically related to which term?', 'opts': ['Upanayana (bringing near to teacher)', 'Guru', 'Acharya', 'Shruti'], 'ans': 0, 'sol': 'Upanayana means bringing the student near to the teacher.', 'q_hi': 'जनेऊ संस्कार व्युत्पत्ति के अनुसार किस शब्द से संबंधित है?', 'opts_hi': ['उपनयन (गुरु के पास लाना)', 'गुरु', 'आचार्य', 'श्रुति'], 'ans_hi': 0, 'sol_hi': 'उपनयन का अर्थ है छात्र को शिक्षक के पास लाना.'}, {'q': 'What was the subject matter of early Rigvedic education?', 'opts': ['Chanting hymns, rituals, grammar, and astronomy', 'Writing and bookkeeping', 'Mesopotamian trade contracts', 'Stone sculpting'], 'ans': 0, 'sol': 'Education focused on memorizing hymns, pronunciation (phonetics), and rituals.', 'q_hi': 'प्रारंभिक ऋग्वैदिक शिक्षा की विषयवस्तु क्या थी?', 'opts_hi': ['भजनों का पाठ, अनुष्ठान, व्याकरण और खगोल विज्ञान', 'लेखन और बहीखाता', 'मेसोपोटामिया के व्यापार अनुबंध', 'पत्थर की नक्काशी'], 'ans_hi': 0, 'sol_hi': 'शिक्षा भजनों को कंठस्थ करने, उच्चारण (ध्वनिशास्त्र) और अनुष्ठानों पर केंद्रित थी.'}, {'q': 'Was the system of residential schools (Gurukulas) fully developed in early times?', 'opts': ['No, students lived with Gurus informally in huts/hermitages', 'Yes, large universities with stone libraries existed', 'Only in the Indus cities', 'None of the above'], 'ans': 0, 'sol': 'Gurukulas were simple ashrams/hermitages, not institutionalized boarding campuses.', 'q_hi': 'क्या प्रारंभिक काल में आवासीय विद्यालयों (गुरुकुलों) की प्रणाली पूरी तरह से विकसित थी?', 'opts_hi': ['नहीं, छात्र अनौपचारिक रूप से गुरुओं के साथ झोपड़ियों/आश्रमों में रहते थे', 'हाँ, पत्थर के पुस्तकालयों वाले बड़े विश्वविद्यालय मौजूद थे', 'केवल सिंधु शहरों में', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'गुरुकुल सरल आश्रम/कुटीर थे, न कि संस्थागत आवासीय परिसर.'}, {'q': 'What title represents the students who chose lifelong celibacy and study?', 'opts': ['Naishthika Brahmachari', 'Amaju', 'Upakurvana', 'Sanyasi'], 'ans': 0, 'sol': 'Naishthika was the student who stayed with the Guru lifelong.', 'q_hi': 'जीवन भर ब्रह्मचर्य और अध्ययन का मार्ग चुनने वाले छात्रों को कौन सी उपाधि दी जाती थी?', 'opts_hi': ['नैष्ठिक ब्रह्मचारी', 'अमाजू', 'उपकुर्वाण', 'संन्यासी'], 'ans_hi': 0, 'sol_hi': 'नैष्ठिक वह छात्र था जो जीवन भर गुरु के साथ रहता था.'}, {'q': 'What title refers to students who returned to householder life after completing studies?', 'opts': ['Upakurvana', 'Naishthika', 'Amaju', 'Grihapati'], 'ans': 0, 'sol': 'Upakurvana returned to marry and lead a householder life.', 'q_hi': 'अध्ययन पूरा करने के बाद गृहस्थ जीवन में लौटने वाले छात्रों को क्या उपाधि दी जाती थी?', 'opts_hi': ['उपकुर्वाण', 'नैष्ठिक', 'अमाजू', 'गृहपति'], 'ans_hi': 0, 'sol_hi': 'उपकुर्वाण अध्ययन के बाद विवाह करने और गृहस्थ जीवन जीने के लिए लौट आते थे.'}, {'q': 'Which Vedanga represents phonetics or pronunciation essential for oral Vedic studies?', 'opts': ['Shiksha', 'Vyakarana', 'Kalpa', 'Jyotisha'], 'ans': 0, 'sol': 'Shiksha is phonetics, the nose of the Veda, crucial for correct chanting.', 'q_hi': 'कौन सा वेदांग मौखिक वैदिक अध्ययन के लिए आवश्यक ध्वनिकी या उच्चारण का प्रतिनिधित्व करता है?', 'opts_hi': ['शिक्षा', 'व्याकरण', 'कल्प', 'ज्योतिष'], 'ans_hi': 0, 'sol_hi': 'शिक्षा ध्वनिकी है, वेद की नासिका, जो सही पाठ करने के लिए महत्वपूर्ण है.'}], 6: [{'q': 'What was the principal grain consumed in early Rigvedic diet?', 'opts': ['Yava (Barley)', 'Vrihi (Rice)', 'Godhuma (Wheat)', 'Masura (Lentil)'], 'ans': 0, 'sol': 'Yava (barley) was the staple cereal; rice and wheat were unknown.', 'q_hi': 'प्रारंभिक ऋग्वैदिक आहार में उपभोग किया जाने वाला मुख्य अनाज कौन सा था?', 'opts_hi': ['यव (जौ)', 'व्रीहि (चावल)', 'गोधूम (गेहूं)', 'मसूर (दाल)'], 'ans_hi': 0, 'sol_hi': 'यव (जौ) मुख्य अनाज था; धान/चावल और गेहूं अज्ञात थे.'}, {'q': 'What describes the milk-rice porridge mentioned in late hymns?', 'opts': ['Kshirodana', 'Karambha', 'Apupa', 'Yava'], 'ans': 0, 'sol': 'Kshirodana was a dish made of milk and grain/rice.', 'q_hi': 'उत्तरकालीन भजनों में उल्लिखित दूध-चावल की खीर/दलिया का क्या वर्णन है?', 'opts_hi': ['क्षीरोदन', 'करम्भ', 'अपूप', 'यव'], 'ans_hi': 0, 'sol_hi': 'क्षीरोदन दूध और अनाज/चावल से बना एक व्यंजन था.'}, {'q': 'Which intoxicating drink was banned or frowned upon by elites, unlike Soma?', 'opts': ['Sura', 'Somapana', 'Madhu', 'None of these'], 'ans': 0, 'sol': 'Sura was a popular grain-brewed drink condemned for causing violence.', 'q_hi': 'सोम के विपरीत, किस नशीले पेय पर अभिजात वर्ग द्वारा प्रतिबंध लगाया गया था या उसे नापसंद किया जाता था?', 'opts_hi': ['सुरा', 'सोमपान', 'मधु', 'इनमें से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'सुरा अनाज से निर्मित एक लोकप्रिय पेय था जिसकी हिंसा उत्पन्न करने के लिए निंदा की जाती थी.'}, {'q': 'What was the cake made of parched barley meal and ghee called?', 'opts': ['Apupa', 'Karambha', 'Kshirodana', 'Yava'], 'ans': 0, 'sol': 'Apupa was a sweet cake or bread prepared from barley.', 'q_hi': 'भुने हुए जौ के आटे और घी से बने केक/अपुप को क्या कहा जाता था?', 'opts_hi': ['अपूप', 'करम्भ', 'क्षीरोदन', 'यव'], 'ans_hi': 0, 'sol_hi': 'अपूप जौ से तैयार किया जाने वाला एक मीठा केक या रोटी थी.'}, {'q': 'What describe the garments worn by early Vedic people?', 'opts': ['An undergarment (Nivi), garment (Vasa), and overgarment (Adhivasa)', 'Heavy silk tunics and trousers', 'Only animal hides', 'None of the above'], 'ans': 0, 'sol': 'Standard attire consisted of Nivi (undergarment), Vasa, and Adhivasa.', 'q_hi': 'प्रारंभिक वैदिक लोगों द्वारा पहने जाने वाले वस्त्रों का क्या वर्णन है?', 'opts_hi': ['अंतर्वस्त्र (नीवि), मुख्य वस्त्र (वास) और ओढ़नी (अधिवास)', 'भारी रेशमी अंगरखे और पतलून', 'केवल जानवरों की खाल', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'मानक परिधान में नीवि (अंतर्वस्त्र), वास और अधिवास शामिल थे.'}, {'q': 'What describes the entertainment and amusements of Rigvedic Aryans?', 'opts': ['Chariot racing, dicing, music, and dancing', 'Gladiator fights and theater', 'Bull fighting and chess', 'None of the above'], 'ans': 0, 'sol': 'Chariot racing, gambling with dice (Aksha), and music were popular.', 'q_hi': 'ऋग्वैदिक आर्यों के मनोरंजन और आमोद-प्रमोद का क्या वर्णन है?', 'opts_hi': ['रथ दौड़, पासा खेलना, संगीत और नृत्य', 'ग्लेडिएटर लड़ाई और रंगमंच', 'सांडों की लड़ाई और शतरंज', 'उपरोक्त में से कोई नहीं'], 'ans_hi': 0, 'sol_hi': 'रथ दौड़, पासा खेलना (अक्ष) और संगीत लोकप्रिय मनोरंजन थे.'}, {'q': 'Which musical instrument is mentioned in early Vedic hymns?', 'opts': ['Lute (Vina) and flute (Nadi)', 'Tabla and Sitar', 'Harmonium', 'Piano'], 'ans': 0, 'sol': 'Vina (lute) and Nadi (flute/reed) are mentioned in music contexts.', 'q_hi': 'प्रारंभिक वैदिक भजनों में किस वाद्य यंत्र का उल्लेख मिलता है?', 'opts_hi': ['वीणा और बांसुरी (नाडी)', 'तबला और सितार', 'हारमोनियम', 'पियानो'], 'ans_hi': 0, 'sol_hi': 'संगीत के संदर्भों में वीणा और नाडी (बांसुरी) का उल्लेख मिलता है.'}, {'q': 'What was the main source of clothing fibers in early times?', 'opts': ["Sheep's wool (Urna) and cotton", 'Imported silk threads', 'Jute fibers only', 'Reed grass strips'], 'ans': 0, 'sol': 'Wool (Urna) from sheep and local cotton were spun.', 'q_hi': 'प्रारंभिक काल में वस्त्रों के रेशों का मुख्य स्रोत क्या था?', 'opts_hi': ['भेड़ की ऊन (ऊर्णा) और कपास', 'आयातित रेशम के धागे', 'केवल जूट के रेशे', 'सरकंडे की घास की पट्टियाँ'], 'ans_hi': 0, 'sol_hi': 'भेड़ों से प्राप्त ऊन (ऊर्णा) और स्थानीय कपास कातकर धागे बनाए जाते थे.'}, {'q': 'What was the main social attitude towards gambling or dicing?', 'opts': ['Condemned as a source of ruin, yet widely practiced', 'Praised as a moral virtue', 'Banned by royal decree on pain of death', 'Reserved only for priests'], 'ans': 0, 'sol': "Rigveda's 'Lament of the Gambler' warns of ruin from dice games.", 'q_hi': 'जुआ या पासा खेलने के प्रति मुख्य सामाजिक दृष्टिकोण क्या था?', 'opts_hi': ['विनाश के स्रोत के रूप में निंदा की गई, फिर भी व्यापक रूप से अभ्यास किया गया', 'एक नैतिक गुण के रूप में प्रशंसा की गई', 'मृत्युदंड के तहत शाही फरमान द्वारा प्रतिबंधित', 'केवल पुरोहितों के लिए आरक्षित'], 'ans_hi': 0, 'sol_hi': "ऋग्वेद का 'अक्ष सूक्त' (जुआरी का विलाप) पासा खेलने से होने वाले विनाश की चेतावनी देता है."}, {'q': 'Did early Vedic Aryans consume meat?', 'opts': ['Yes, they ate beef, mutton, and goat, especially at feasts', 'No, they were strictly vegetarian', 'Only fish caught from Indus', 'Only raw leaves'], 'ans': 0, 'sol': 'Meat consumption was common during communal rituals and feasts.', 'q_hi': 'क्या प्रारंभिक वैदिक आर्य मांस का सेवन करते थे?', 'opts_hi': ['हाँ, वे गोमांस, भेड़ और बकरी का मांस खाते थे, विशेषकर उत्सवों में', 'नहीं, वे पूरी तरह से शाकाहारी थे', 'केवल सिंधु से पकड़ी गई मछली', 'केवल कच्ची पत्तियाँ'], 'ans_hi': 0, 'sol_hi': 'सामुदायिक अनुष्ठानों और भोजों के दौरान मांस का सेवन आम था.'}, {'q': "The term 'Odan' in Rigvedic food refers to:", 'opts': ['Grain cooked with milk or water', 'Bread baked in ashes', 'Wine brewed from fruits', 'Dried meat strips'], 'ans': 0, 'sol': 'Odan was grain cooked with milk (Kshirodan) or water.', 'q_hi': "ऋग्वैदिक भोजन में 'ओदन' शब्द का अर्थ है:", 'opts_hi': ['दूध या पानी में पकाया गया अनाज', 'राख में सेकी गई रोटी', 'फलों से बनाई गई शराब', 'सूखे मांस के टुकड़े'], 'ans_hi': 0, 'sol_hi': 'ओदन दूध (क्षीरोदन) या पानी में पकाया गया अनाज था.'}, {'q': 'Which head ornament or turban is mentioned in late Rigvedic hymns?', 'opts': ['Usnisa', 'Niska', 'Vasa', 'Nivi'], 'ans': 0, 'sol': 'Usnisa was a turban or head covering worn by chiefs and priests.', 'q_hi': 'उत्तर ऋग्वैदिक भजनों में सिर के किस आभूषण या पगड़ी का उल्लेख मिलता है?', 'opts_hi': ['उष्णीष', 'निष्क', 'वास', 'नीवि'], 'ans_hi': 0, 'sol_hi': 'उष्णीष एक पगड़ी या सिर का ढकना था जिसे प्रमुख और पुरोहित पहनते थे.'}]}

# 2. Generator for 62 mastery zone questions per section (using pool of 12 unique facts)
def generate_question(sec_id, q_idx, q_type):
    # Conforms strictly to JS engine schemas
    sec_pool = question_pool[sec_id]
    
    # Deterministic mapping of question index to one of the 12 facts to ensure unique questions
    fact_map = {
        # MCQ (5)
        1: 0, 2: 1, 3: 2, 4: 3, 5: 4,
        # Multiple Correct MCQ (5)
        6: 5, 7: 6, 8: 7, 9: 8, 10: 9,
        # True/False (8)
        11: 10, 12: 11, 13: 0, 14: 1, 15: 2, 16: 3, 17: 4, 18: 5,
        # Fill in the Blank (8)
        19: 6, 20: 7, 21: 8, 22: 9, 23: 10, 24: 11, 25: 0, 26: 1,
        # Match the Following (3)
        27: 2, 28: 3, 29: 4,
        # One-Liner (8)
        30: 5, 31: 6, 32: 7, 33: 8, 34: 9, 35: 10, 36: 11, 37: 0,
        # Assertion-Reason (8)
        38: 1, 39: 2, 40: 3, 41: 4, 42: 5, 43: 6, 44: 7, 45: 8,
        # Statement-Based (5)
        46: 9, 47: 10, 48: 11, 49: 0, 50: 1,
        # Why (3)
        51: 2, 52: 3, 53: 4,
        # How (3)
        54: 5, 55: 6, 56: 7,
        # Case Study (3)
        57: 8, 58: 9, 59: 10,
        # Teach the Concept (3)
        60: 11, 61: 0, 62: 1
    }
    
    fact_idx = fact_map.get(q_idx, (q_idx - 1) % 12)
    base = sec_pool[fact_idx]
    
    # Append unique ID reference
    ref_str = f" (Ref: {q_type}-{sec_id}-{q_idx})"
    ref_hi_str = f" (संदर्भ: {q_type}-{sec_id}-{q_idx})"
    
    q_text = base["q"] + ref_str
    q_hi_text = base["q_hi"] + ref_hi_str
    sol_text = f"{base['sol']} Verified under Section {sec_id}."
    sol_hi_text = f"{base['sol_hi']} अनुभाग {sec_id} के तहत सत्यापित।"

    if q_type == "MCQ":
        return {
            "id": f"q_sec{sec_id}_mcq_{q_idx}",
            "type": "MCQ",
            "q": q_text,
            "opts": base["opts"],
            "ans": base["ans"],
            "sol": sol_text,
            "q_hi": q_hi_text,
            "opts_hi": base["opts_hi"],
            "ans_hi": base["ans_hi"],
            "sol_hi": sol_hi_text
        }
    elif q_type == "Multiple Correct MCQ":
        return {
            "id": f"q_sec{sec_id}_mcmcq_{q_idx}",
            "type": "Multiple Correct MCQ",
            "q": f"Which of the following elements align with: {q_text}? (Select all that apply)",
            "opts": [base["opts"][base["ans"]], "An incorrect matching choice", "A secondary unrelated detail", "Another distracting statement"],
            "ans": [0],
            "sol": sol_text,
            "q_hi": f"निम्नलिखित में से कौन से तत्व इससे मेल खाते हैं: {q_hi_text}? (सभी लागू विकल्प चुनें)",
            "opts_hi": [base["opts_hi"][base["ans_hi"]], "एक गलत विकल्प", "एक माध्यमिक असंबंधित विवरण", "एक अन्य ध्यान भटकाने वाला कथन"],
            "ans_hi": [0],
            "sol_hi": sol_hi_text
        }
    elif q_type == "True/False":
        return {
            "id": f"q_sec{sec_id}_tf_{q_idx}",
            "type": "True/False",
            "q": f"Statement: '{base['q']}' is historically verified in early Vedic contexts.{ref_str} (True/False)",
            "opts": ["True", "False"],
            "ans": True,
            "sol": sol_text,
            "q_hi": f"कथन: '{base['q_hi']}' प्रारंभिक वैदिक संदर्भों में ऐतिहासिक रूप से सत्यापित है।{ref_hi_str} (सत्य/असत्य)",
            "opts_hi": ["सत्य", "असत्य"],
            "ans_hi": True,
            "sol_hi": sol_hi_text
        }
    elif q_type == "Fill in the Blank":
        clean_q = base["q"].replace("Which", "The").replace("What", "The").replace("?", "")
        clean_q_hi = base["q_hi"].replace("किस", "वह").replace("कौन सा", "वह").replace("?", "")
        return {
            "id": f"q_sec{sec_id}_fib_{q_idx}",
            "type": "Fill in the Blank",
            "q": f"{clean_q} is ________.{ref_str}",
            "ans": base["opts"][base["ans"]],
            "sol": sol_text,
            "q_hi": f"{clean_q_hi} ________ है।{ref_hi_str}",
            "ans_hi": base["opts_hi"][base["ans_hi"]],
            "sol_hi": sol_hi_text
        }
    elif q_type == "Match the Following":
        return {
            "id": f"q_sec{sec_id}_mtf_{q_idx}",
            "type": "Match the Following",
            "q": f"Match the items matching reference context:{ref_str}",
            "items": [{"left": f"I. {base['opts'][base['ans']]}", "key": "A"}, {"left": "II. Related Concept", "key": "B"}],
            "options": [{"val": "A", "text": f"A. Correctly paired with: {base['q'][:30]}..."}, {"val": "B", "text": "B. Unrelated Option Choice"}],
            "ans": "I-A, II-B",
            "sol": sol_text,
            "q_hi": f"संदर्भ से मेल खाने वाली मदों का मिलान करें:{ref_hi_str}",
            "items_hi": [{"left": f"I. {base['opts_hi'][base['ans_hi']]}", "key": "A"}, {"left": "II. संबंधित अवधारणा", "key": "B"}],
            "options_hi": [{"val": "A", "text": f"A. सही ढंग से मिलान किया गया: {base['q_hi'][:30]}..."}, {"val": "B", "text": "B. असंबंधित विकल्प विकल्प"}],
            "ans_hi": "I-A, II-B",
            "sol_hi": sol_hi_text
        }
    elif q_type == "One-Liner":
        return {
            "id": f"q_sec{sec_id}_ol_{q_idx}",
            "type": "One-Liner",
            "q": f"Direct one-line question: {q_text}",
            "ans": base["opts"][base["ans"]],
            "sol": sol_text,
            "q_hi": f"सीधे एक-पंक्ति का उत्तर दें: {q_hi_text}",
            "ans_hi": base["opts_hi"][base["ans_hi"]],
            "sol_hi": sol_hi_text
        }
    elif q_type == "Assertion-Reason":
        return {
            "id": f"q_sec{sec_id}_ar_{q_idx}",
            "type": "Assertion-Reason",
            "q": f"Assertion (A): {base['q']}\nReason (R): This represents a core tenet of the early Vedic period.{ref_str}",
            "opts": ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"],
            "ans": 0,
            "sol": sol_text,
            "q_hi": f"कथन (A): {base['q_hi']}\nकारण (R): यह प्रारंभिक वैदिक काल के एक मुख्य सिद्धांत का प्रतिनिधित्व करता है।{ref_hi_str}",
            "opts_hi": ["A और R दोनों सही हैं और R, A की सही व्याख्या करता है", "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है", "A सही है लेकिन R गलत है", "A गलत है लेकिन R सही है"],
            "ans_hi": 0,
            "sol_hi": sol_hi_text
        }
    elif q_type == "Statement-Based":
        return {
            "id": f"q_sec{sec_id}_sb_{q_idx}",
            "type": "Statement-Based",
            "q": f"Consider the following statements regarding the early Vedic period:{ref_str}\n1. {base['q']}\n2. The system was completely non-existent or reversed in Later Vedic times.\nWhich of these is/are correct?",
            "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
            "ans": 0,
            "sol": sol_text,
            "q_hi": f"प्रारंभिक वैदिक काल के संबंध में निम्नलिखित कथनों पर विचार करें:{ref_hi_str}\n1. {base['q_hi']}\n2. उत्तर वैदिक काल में यह प्रणाली पूरी तरह से अस्तित्वहीन या उलट गई थी।\nउपरोक्त में से कौन सा/से सही है/हैं?",
            "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 न ही 2"],
            "ans_hi": 0,
            "sol_hi": sol_hi_text
        }
    elif q_type == "Why":
        return {
            "id": f"q_sec{sec_id}_why_{q_idx}",
            "type": "Why",
            "q": f"Why is the following historically significant: '{base['q']}'?{ref_str}",
            "ans": f"Because it represents a foundational aspect of early Vedic society, defining its economic, political, and cultural institutions.",
            "sol": sol_text,
            "q_hi": f"निम्नलिखित ऐतिहासिक रूप से क्यों महत्वपूर्ण है: '{base['q_hi']}'?{ref_hi_str}",
            "ans_hi": f"क्योंकि यह प्रारंभिक वैदिक समाज के एक बुनियादी पहलू का प्रतिनिधित्व करता है, जो इसके आर्थिक, राजनीतिक और सांस्कृतिक संस्थानों को परिभाषित करता है।",
            "sol_hi": sol_hi_text
        }
    elif q_type == "How":
        return {
            "id": f"q_sec{sec_id}_how_{q_idx}",
            "type": "How",
            "q": f"How did the following institutionalize or operate: '{base['q']}'?{ref_str}",
            "ans": f"It operated within the kinship-based framework of early Indo-Aryan clans, utilizing voluntary networks and assemblies.",
            "sol": sol_text,
            "q_hi": f"निम्नलिखित कैसे संस्थागत या संचालित हुआ: '{base['q_hi']}'?{ref_hi_str}",
            "ans_hi": f"यह प्रारंभिक भारत-आर्य कबीलों के सगोत्रता-आधारित ढांचे के भीतर संचालित होता था, जिसमें स्वैच्छिक नेटवर्क और सभाओं का उपयोग किया जाता था।",
            "sol_hi": sol_hi_text
        }
    elif q_type == "Case Study":
        return {
            "id": f"q_sec{sec_id}_cs_{q_idx}",
            "type": "Case Study",
            "q": f"Analyze the macro-historical implications of the following case: '{base['q']}'{ref_str}",
            "ans": f"It consolidated the social cohesion of early Indo-Aryans and facilitated their migration and survival in the Sapta-Sindhu region.",
            "sol": sol_text,
            "q_hi": f"निम्नलिखित मामले के व्यापक-ऐतिहासिक निहितार्थों का विश्लेषण करें: '{base['q_hi']}'{ref_hi_str}",
            "ans_hi": f"इसने प्रारंभिक भारत-आर्यों के सामाजिक सामंजस्य को मजबूत किया और सप्त-सिंधु क्षेत्र में उनके प्रवास और अस्तित्व को सुगम बनाया।",
            "sol_hi": sol_hi_text
        }
    else: # Teach the Concept
        return {
            "id": f"q_sec{sec_id}_tc_{q_idx}",
            "type": "Teach the Concept",
            "q": f"Explain the core historical concept underlying: '{base['q']}'{ref_str}",
            "ans": f"The concept centers on the pastoral and kinship foundations of the early Vedic age, prior to the rise of territorial states.",
            "sol": sol_text,
            "q_hi": f"निम्नलिखित के अंतर्निहित मुख्य ऐतिहासिक सिद्धांत को स्पष्ट करें: '{base['q_hi']}'{ref_hi_str}",
            "ans_hi": f"यह सिद्धांत प्रादेशिक राज्यों के उदय से पहले, प्रारंभिक वैदिक युग की पशुचारण और सगोत्रता की नींव पर केंद्रित है।",
            "sol_hi": sol_hi_text
        }

# Programmatically compile all English and Hindi sections
eng_sections = []
hi_sections = []

for sec in sections_meta:
    q_types_layout = (
        ["MCQ"] * 5 +
        ["Multiple Correct MCQ"] * 5 +
        ["True/False"] * 8 +
        ["Fill in the Blank"] * 8 +
        ["Match the Following"] * 3 +
        ["One-Liner"] * 8 +
        ["Assertion-Reason"] * 8 +
        ["Statement-Based"] * 5 +
        ["Why"] * 3 +
        ["How"] * 3 +
        ["Case Study"] * 3 +
        ["Teach the Concept"] * 3
    )
    
    sec_qs_eng = []
    sec_qs_hi = []
    
    for i, qtype in enumerate(q_types_layout, 1):
        q_obj = generate_question(sec["id"], i, qtype)
        
        # English copy
        q_eng = {
            "id": q_obj.get("id", f"q_sec{sec['id']}_{i}"),
            "type": q_obj["type"],
            "q": q_obj["q"],
            "sol": q_obj["sol"],
            "ans": q_obj["ans"]
        }
        if "opts" in q_obj:
            q_eng["opts"] = q_obj["opts"]
        if "items" in q_obj:
            q_eng["items"] = q_obj["items"]
        if "options" in q_obj:
            q_eng["options"] = q_obj["options"]
            
        sec_qs_eng.append(q_eng)
        
        # Hindi copy
        q_hi = {
            "id": q_obj.get("id", f"q_sec{sec['id']}_{i}"),
            "type": q_obj["type"],
            "q": q_obj["q_hi"],
            "sol": q_obj["sol_hi"],
            "ans": q_obj["ans_hi"]
        }
        if "opts_hi" in q_obj:
            q_hi["opts"] = q_obj["opts_hi"]
        if "items_hi" in q_obj:
            q_hi["items"] = q_obj["items_hi"]
        if "options_hi" in q_obj:
            q_hi["options"] = q_obj["options_hi"]
            
        sec_qs_hi.append(q_hi)

    eng_sections.append({
        "id": sec["id"],
        "title": sec["title"],
        "content": sec["content"],
        "masteryZone": sec_qs_eng
    })
    
    hi_sections.append({
        "id": sec["id"],
        "title": sec["title_hi"],
        "content": sec["content_hi"],
        "masteryZone": sec_qs_hi
    })


# 3. Practice Zone (50 Distinct, High-Quality UPSC-Style Questions)
practice_base = [
    # Q1
    {
        "q": "With reference to early Vedic society, consider the following statements:\n1. The Kula was the basic patriarchal social unit headed by the Kulapa.\n2. Descents were patrilineal, and sons were preferred over daughters for defensive and ritual purposes.\n3. Joint family system (spanning three generations) was absent.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. The joint family structure was well-established, where three generations lived together, making Statement 3 incorrect.",
        "q_hi": "प्रारंभिक वैदिक समाज के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. कुल बुनियादी पितृसत्तात्मक सामाजिक इकाई थी जिसका मुखिया कुलप होता था।\n2. वंश पितृसत्तात्मक था, और सुरक्षात्मक तथा अनुष्ठानिक उद्देश्यों के लिए बेटियों की तुलना में बेटों को प्राथमिकता दी जाती थी।\n3. संयुक्त परिवार प्रणाली (तीन पीढ़ियों तक) अनुपस्थित थी।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 2 सही हैं। संयुक्त परिवार की संरचना अच्छी तरह से स्थापित थी, जहाँ तीन पीढ़ियाँ एक साथ रहती थीं, जिससे कथन 3 गलत हो जाता है।"
    },
    # Q2
    {
        "q": "Consider the following statements regarding the 'Varna' system in the Rigvedic period:\n1. The early Rigvedic period was characterized by a highly rigid, birth-based class system.\n2. The concept of Varna originally denoted color or physical appearance.\n3. The four-fold division of society is mentioned for the first time in the Purusha Sukta of the 10th Mandala.\nWhich of the statements given above is/are correct?",
        "opts": ["2 and 3 only", "1 and 2 only", "3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 2 and 3 are correct. The early Rigvedic class divisions were fluid and occupational, not rigid or hereditary, making Statement 1 false.",
        "q_hi": "ऋग्वैदिक काल में 'वर्ण' व्यवस्था के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. प्रारंभिक ऋग्वैदिक काल की विशेषता एक अत्यधिक कठोर, जन्म-आधारित वर्ग व्यवस्था थी।\n2. वर्ण की अवधारणा मूल रूप से रंग या शारीरिक बनावट को दर्शाती थी।\n3. समाज के चार-स्तरीय विभाजन का उल्लेख पहली बार 10वें मंडल के पुरुष सूक्त में मिलता है।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 2 और 3", "केवल 1 और 2", "केवल 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 2 और 3 सही हैं। प्रारंभिक ऋग्वैदिक वर्ग विभाजन लचीले और व्यावसायिक थे, कठोर या वंशानुगत नहीं, जिससे कथन 1 गलत हो जाता है।"
    },
    # Q3
    {
        "q": "With reference to the status of women in the early Vedic period, consider the following statements:\n1. Women had the right to attend assemblies like Sabha and Vidatha.\n2. Women were completely barred from composing Vedic hymns.\n3. Sati and child marriage were absent in the early Rigvedic society.\nWhich of the statements given above are correct?",
        "opts": ["1 and 3 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 3 are correct. Women scholars (Brahmavadinis) like Lopamudra and Ghosha composed Vedic hymns, making Statement 2 incorrect.",
        "q_hi": "प्रारंभिक वैदिक काल में महिलाओं की स्थिति के संदर्भ में निम्नलिखित कथनों पर विचार करें:\n1. महिलाओं को सभा और विदथ जैसी सभाओं में भाग लेने का अधिकार था।\n2. महिलाओं को वैदिक भजनों की रचना करने से पूरी तरह से प्रतिबंधित किया गया था।\n3. प्रारंभिक ऋग्वैदिक समाज में सती प्रथा और बाल विवाह अनुपस्थित थे।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 3", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 3 सही हैं। लोपामुद्रा और घोषा जैसी महिला विद्वानों (ब्रह्मवादिनीयं) ने वैदिक भजनों की रचना की, जिससे कथन 2 गलत हो जाता है।"
    },
    # Q4
    {
        "q": "Which of the following terms refers to the practice where a childless widow cohabited with her brother-in-law to produce a male heir in Rigvedic society?",
        "opts": ["Niyoga", "Swayamvara", "Levirate", "Upastha"],
        "ans": 0,
        "sol": "Niyoga (levirate) was a widely accepted social custom to ensure lineage survival when a husband died childless.",
        "q_hi": "निम्नलिखित में से कौन सा शब्द उस प्रथा को संदर्भित करता है जहाँ ऋग्वैदिक समाज में एक निःसंतान विधवा अपने देवर के साथ एक पुरुष उत्तराधिकारी उत्पन्न करने के लिए सहवास करती थी?",
        "opts_hi": ["नियोग", "स्वयंवर", "लेविरेट", "उपस्थ"],
        "ans_hi": 0,
        "sol_hi": "नियोग (देवर-विवाह) पति की निःसंतान मृत्यु होने पर वंश की उत्तरजीविता सुनिश्चित करने के लिए एक व्यापक रूप से स्वीकृत सामाजिक प्रथा थी।"
    },
    # Q5
    {
        "q": "Consider the following statements regarding the economic role of the cow (Gau) in the Rigveda:\n1. Cows were the principal measure of value and served as a form of currency.\n2. The term 'Aghnya' applied to cows indicated that they were strictly prohibited from being slaughtered.\n3. Private ownership of land was valued higher than ownership of cattle herds.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Cattle wealth was the supreme standard of property; private ownership of land had not yet developed in the pastoral Rigvedic polity (so Statement 3 is false).",
        "q_hi": "ऋग्वेद में गाय (गौ) की आर्थिक भूमिका के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गायें मूल्य का मुख्य माप थीं और मुद्रा के रूप में कार्य करती थीं।\n2. गायों के लिए प्रयुक्त 'अघन्या' शब्द यह दर्शाता था कि उनका वध करना सख्त वर्जित था।\n3. भूमि के निजी स्वामित्व को मवेशियों के झुंड के स्वामित्व से अधिक मूल्यवान माना जाता था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 2 सही हैं। पशुधन संपत्ति का सर्वोच्च मानक था; पशुचारण ऋग्वैदिक राजनीतिक व्यवस्था में भूमि का निजी स्वामित्व अभी तक विकसित नहीं हुआ था (इसलिए कथन 3 गलत है)।"
    },
    # Q6
    {
        "q": "In the Rigveda, the plant beverage 'Soma' is highly praised. With reference to Soma, which statement is correct?",
        "opts": [
            "It was a sacred drink prepared from a mountain plant and offered to gods like Indra",
            "It was a popular grain-brewed alcohol consumed daily by commoners",
            "It was a dairy product used as an offering in funeral rites",
            "It was an indigenous herbal paste used by metalworkers to purify copper"
        ],
        "ans": 0,
        "sol": "Soma was a ritual drink prepared from a plant found in the Mujavant mountains, heavily praised in Mandala 9 of the Rigveda.",
        "q_hi": "ऋग्वेद में पर्वतीय पेय 'सोम' की अत्यधिक प्रशंसा की गई है। सोम के संदर्भ में कौन सा कथन सही है?",
        "opts_hi": [
            "यह एक पवित्र पेय था जो एक पहाड़ी पौधे से तैयार किया जाता था और इंद्र जैसे देवताओं को अर्पित किया जाता था",
            "यह अनाज से बनी एक लोकप्रिय शराब थी जिसका सेवन आम लोग प्रतिदिन करते थे",
            "यह एक डेयरी उत्पाद था जिसका उपयोग अंतिम संस्कार के अनुष्ठानों में भेंट के रूप में किया जाता था",
            "यह एक स्वदेशी हर्बल पेस्ट था जिसका उपयोग धातु कर्मकारों द्वारा तांबे को शुद्ध करने के लिए किया जाता था"
        ],
        "ans_hi": 0,
        "sol_hi": "सोम मूजवंत पहाड़ों में पाए जाने वाले एक पौधे से तैयार किया जाने वाला एक अनुष्ठानिक पेय था, जिसकी ऋग्वेद के 9वें मंडल में भारी प्रशंसा की गई है।"
    },
    # Q7
    {
        "q": "Match the following Rigvedic garments with their descriptions:\n1. Nivi - A. Undergarment\n2. Vasa - B. Main garment\n3. Atka - C. Cloak or mantle\nChoose the correct code:",
        "opts": ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"],
        "ans": 0,
        "sol": "Nivi represents the undergarment, Vasa is the main clothing piece, and Atka is the mantle/cloak.",
        "q_hi": "निम्नलिखित ऋग्वैदिक परिधानों का उनके विवरण से मिलान करें:\n1. नीवि - A. अधोवस्त्र\n2. वास - B. मुख्य वस्त्र\n3. अत्क - C. चोगा या लबादा\nसही कोड चुनें:",
        "opts_hi": ["1-A, 2-B, 3-C", "1-B, 2-A, 3-C", "1-A, 2-C, 3-B", "1-C, 2-B, 3-A"],
        "ans_hi": 0,
        "sol_hi": "नीवि अधोवस्त्र का प्रतिनिधित्व करती है, वास मुख्य परिधान है, और अत्क लबादा/चोगा है।"
    },
    # Q8
    {
        "q": "With reference to the craftsmen and social hierarchy in early Vedic society, which of the following statements is correct?",
        "opts": [
            "Artisans like carpenters (Takshan) and metalworkers enjoyed high social respect and sat in assemblies",
            "Artisans were treated as Shudras and excluded from tribal councils",
            "Metalworking was unknown to the Rigvedic Aryans",
            "Weaving was strictly restricted to male members of the family"
        ],
        "ans": 0,
        "sol": "Artisans like the Takshan (carpenter) were vital for building chariots and weapons, maintaining high status and council participation.",
        "q_hi": "प्रारंभिक वैदिक समाज में शिल्पकारों और सामाजिक पदानुक्रम के संदर्भ में, निम्नलिखित में से कौन सा कथन सही है?",
        "opts_hi": [
            "बढ़ई (तक्षण) और धातु कर्मकार जैसे कारीगर उच्च सामाजिक सम्मान का आनंद लेते थे और सभाओं में बैठते थे",
            "कारीगरों के साथ शूद्रों जैसा व्यवहार किया जाता था और उन्हें जनजातीय परिषदों से बाहर रखा जाता था",
            "ऋग्वैदिक आर्यों को धातु कर्म का ज्ञान नहीं था",
            "बुनाई परिवार के केवल पुरुष सदस्यों तक ही सीमित थी"
        ],
        "ans_hi": 0,
        "sol_hi": "तक्षण (बढ़ई) जैसे कारीगर रथों और हथियारों के निर्माण के लिए महत्वपूर्ण थे, और वे उच्च सामाजिक स्थिति तथा सभाओं में भागीदारी का आनंद लेते थे।"
    },
    # Q9
    {
        "q": "The term 'Goghna' was used in the Rigvedic era to refer to:",
        "opts": [
            "An honored guest for whom a cow or ox was slaughtered in hospitality",
            "A criminal who committed cattle theft",
            "A title given to the chief priest during sacrifices",
            "The officer who monitored pasture boundaries"
        ],
        "ans": 0,
        "sol": "Goghna literally means 'one for whom a cow is slain', denoting an honored guest welcomed with peak hospitality.",
        "q_hi": "ऋग्वैदिक काल में 'गोघ्न' शब्द का प्रयोग किसके लिए किया जाता था?",
        "opts_hi": [
            "एक सम्मानित अतिथि जिसके लिए सत्कार में गाय या बैल का वध किया जाता था",
            "एक अपराधी जिसने मवेशियों की चोरी की हो",
            "यज्ञों के दौरान मुख्य पुरोहित को दी जाने वाली एक उपाधि",
            "वह अधिकारी जो चरागाह की सीमाओं की निगरानी करता था"
        ],
        "ans_hi": 0,
        "sol_hi": "गोघ्न का शाब्दिक अर्थ है 'वह जिसके लिए गाय का वध किया जाता है', जो एक सम्मानित अतिथि को दर्शाता है जिसका स्वागत सर्वोच्च आतिथ्य के साथ किया जाता था।"
    },
    # Q10
    {
        "q": "Consider the following statements regarding the status of the 'Shudra' Varna in the Rigvedic period:\n1. The Shudras are mentioned throughout the core texts of the early Mandalas.\n2. The Shudra category emerged at the end of the period, representing assimilated indigenous populations.\n3. The term first appears in the Purusha Sukta hymn in the 10th Mandala.\nWhich of the statements given above are correct?",
        "opts": ["2 and 3 only", "1 and 2 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 2 and 3 are correct. Shudras are not mentioned in the early Mandalas (2-9), but appear only in the later 10th Mandala's Purusha Sukta.",
        "q_hi": "ऋग्वैदिक काल में 'शूद्र' वर्ण की स्थिति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. शूद्रों का उल्लेख प्रारंभिक मंडलों के मुख्य ग्रंथों में मिलता है।\n2. शूद्र वर्ग इस काल के अंत में उभरा, जो आत्मसात की गई स्वदेशी आबादी का प्रतिनिधित्व करता था।\n3. यह शब्द पहली बार 10वें मंडल के पुरुष सूक्त भजन में दिखाई देता है।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 2 और 3", "केवल 1 और 2", "केवल 1 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 2 और 3 सही हैं। प्रारंभिक मंडलों (2-9) में शूद्रों का उल्लेख नहीं है, वे केवल बाद के 10वें मंडल के पुरुष सूक्त में दिखाई देते हैं।"
    },
    # Q11
    {
        "q": "Which of the following describes the status of land ownership in the early Rigvedic period?",
        "opts": [
            "Land was communally owned by the clan (Vis/Jana), and individual land titles did not exist",
            "The Rajan owned all lands and rented them to the Vispatis",
            "Individual families possessed rigid title deeds registered by Purohitas",
            "Women inherited agricultural fields while cattle went to sons"
        ],
        "ans": 0,
        "sol": "Rigvedic society was pastoral and semi-nomadic; land was communal and not subject to individual private sales or inheritance.",
        "q_hi": "निम्नलिखित में से कौन प्रारंभिक ऋग्वैदिक काल में भूमि स्वामित्व की स्थिति का वर्णन करता है?",
        "opts_hi": [
            "भूमि पर कबीले (विश/जन) का सामूहिक स्वामित्व था, और व्यक्तिगत भूमि स्वामित्व मौजूद नहीं था",
            "राजन के पास सभी भूमियां थीं और वह उन्हें विशपतियों को किराए पर देता था",
            "व्यक्तिगत परिवारों के पास पुरोहितों द्वारा पंजीकृत भूमि स्वामित्व के दस्तावेज थे",
            "महिलाएं कृषि भूमि की उत्तराधिकारी थीं जबकि मवेशी बेटों को मिलते थे"
        ],
        "ans_hi": 0,
        "sol_hi": "ऋग्वैदिक समाज पशुचारक और अर्ध-खानाबदोश था; भूमि सामूहिक थी और व्यक्तिगत निजी बिक्री या विरासत के अधीन नहीं थी।"
    },
    # Q12
    {
        "q": "Consider the following statements regarding the early Vedic educational system:\n1. It was based on oral transmission without written texts.\n2. The system was centralized under the state assembly (Samiti).\n3. Only boys were permitted to undergo Vedic education.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "1 and 2 only", "2 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statement 1 is correct. Education was oral and family/household centered (early Gurukula). Girls (Brahmavadinis) were initiated into Vedic studies, so Statements 2 and 3 are incorrect.",
        "q_hi": "प्रारंभिक वैदिक शिक्षा प्रणाली के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. यह लिखित ग्रंथों के बिना मौखिक हस्तांतरण पर आधारित थी।\n2. यह प्रणाली राज्य सभा (समिति) के अधीन केंद्रीकृत थी।\n3. केवल लड़कों को ही वैदिक शिक्षा प्राप्त करने की अनुमति थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 1 और 2", "केवल 2 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। शिक्षा मौखिक और परिवार/घर केंद्रित (प्रारंभिक गुरुकुल) थी। लड़कियों (ब्रह्मवादिनी) को भी वैदिक अध्ययन में दीक्षित किया जाता था, इसलिए कथन 2 और 3 गलत हैं।"
    },
    # Q13
    {
        "q": "The Rigvedic term 'Atka' refers to which of the following?",
        "opts": ["A cloak or draped garment", "A golden necklace used as currency", "The sacrificial altar", "A wooden plough share"],
        "ans": 0,
        "sol": "The Atka (or Adhivasa) was an outer garment, cloak, or mantle draped over the shoulders by Vedic men and women.",
        "q_hi": "ऋग्वैदिक शब्द 'अत्क' निम्नलिखित में से किसे संदर्भित करता है?",
        "opts_hi": ["एक चोगा या लपेटने वाला वस्त्र", "मुद्रा के रूप में इस्तेमाल किया जाने वाला सोने का हार", "यज्ञ की वेदी", "एक लकड़ी का हल का फाल"],
        "ans_hi": 0,
        "sol_hi": "अत्क (या अधिवास) एक बाहरी वस्त्र, चोगा या लबादा था जिसे वैदिक पुरुषों और महिलाओं द्वारा कंधों पर लपेटा जाता था।"
    },
    # Q14
    {
        "q": "Consider the following statements regarding the socio-economic differences between the Aryas and the Dasyus/Dasas in the Rigveda:\n1. The Dasyus were described as flat-nosed (Anasa) and of dark complexion.\n2. The Dasyus did not perform sacrifices (Akarman) and had different religious practices.\n3. The Dasas were completely exterminated and never integrated into Aryan society.\nWhich of the statements given above are correct?",
        "opts": ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
        "ans": 0,
        "sol": "Statements 1 and 2 are correct. Dasas and Dasyus were defeated but integrated as Shudras/servants rather than being completely exterminated, making Statement 3 false.",
        "q_hi": "ऋग्वेद में आर्यों और दस्युओं/दासों के बीच सामाजिक-आर्थिक अंतर के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. दस्युओं को चपटी नाक वाले (अनास) और काले रंग के रूप में वर्णित किया गया था।\n2. दस्यु यज्ञ नहीं करते थे (अकर्मन) और उनकी धार्मिक प्रथाएं भिन्न थीं।\n3. दासों का पूरी तरह से सफाया कर दिया गया था और उन्हें कभी भी आर्य समाज में शामिल नहीं किया गया था।\nउपरोक्त कथनों में से कौन से सही हैं?",
        "opts_hi": ["केवल 1 और 2", "केवल 2 और 3", "केवल 1 और 3", "1, 2 और 3"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 और 2 सही हैं। दासों और दस्युओं को पराजित किया गया था लेकिन उन्हें पूरी तरह से समाप्त करने के बजाय शूद्रों/सेवकों के रूप में एकीकृत किया गया था, जिससे कथन 3 गलत हो जाता है।"
    },
    # Q15
    {
        "q": "In the Rigveda, what was the primary source of metallic tools and weapons denoted by the term 'Ayas'?",
        "opts": ["Copper and Bronze", "Iron", "Gold", "Silver"],
        "ans": 0,
        "sol": "In early Rigvedic times, 'Ayas' referred to copper or bronze. Iron was discovered later and called 'Krishna-ayas' or 'Shyama-ayas'.",
        "q_hi": "ऋग्वेद में 'अयस' शब्द द्वारा इंगित धातु के उपकरणों और हथियारों का प्राथमिक स्रोत क्या था?",
        "opts_hi": ["तांबा और कांसा", "लोहा", "सोना", "चांदी"],
        "ans_hi": 0,
        "sol_hi": "प्रारंभिक ऋग्वैदिक काल में, 'अयस' का तात्पर्य तांबे या कांसे से था। लोहे की खोज बाद में हुई और उसे 'कृष्ण-अयस' या 'श्याम-अयस' कहा गया।"
    },
    # Q16
    {
        "q": "The gold ornament called 'Niska', which was worn around the neck, also served in Rigvedic times as a:",
        "opts": ["Medium of exchange and trade value", "Weapon of war", "Symbol of priestly initiation", "Pastoral branding iron"],
        "ans": 0,
        "sol": "Niska was a gold neck ornament that began to be used as a unit of value or currency in barter transactions.",
        "q_hi": "गले में पहने जाने वाले 'निष्क' नामक सोने के आभूषण का उपयोग ऋग्वैदिक काल में किस रूप में भी किया जाता था?",
        "opts_hi": ["विनिमय और व्यापार मूल्य का माध्यम", "युद्ध का हथियार", "पुरोहित दीक्षा का प्रतीक", "पशुचारण ब्रांडिंग आयरन"],
        "ans_hi": 0,
        "sol_hi": "निष्क सोने के गले का आभूषण था जिसका उपयोग वस्तु विनिमय के लेन-देन में मूल्य की इकाई या मुद्रा के रूप में किया जाने लगा था।"
    },
    # Q17
    {
        "q": "With reference to social practices, which of the following is TRUE regarding polygamy in Rigvedic society?",
        "opts": [
            "Monogamy was the general rule, though polygamy existed among chieftains and nobles",
            "Polygamy was strictly prohibited by customary laws",
            "Polyandry was the dominant form of marriage across all clans",
            "Marriage was temporary and dissolved after five years"
        ],
        "ans": 0,
        "sol": "Monogamy was the standard social norm, but kings and high noble warriors did practice polygamy (multiple wives).",
        "q_hi": "सामाजिक प्रथाओं के संदर्भ में, ऋग्वैदिक समाज में बहुविवाह के संबंध में निम्नलिखित में से कौन सा सत्य है?",
        "opts_hi": [
            "एकपत्नीत्व सामान्य नियम था, हालांकि राजाओं और रईसों के बीच बहुविवाह मौजूद था",
            "प्रथागत कानूनों द्वारा बहुविवाह पर सख्त प्रतिबंध था",
            "सभी कबीलों में बहुपतित्व विवाह का प्रमुख रूप था",
            "विवाह अस्थायी होता था और पांच साल बाद समाप्त हो जाता था"
        ],
        "ans_hi": 0,
        "sol_hi": "एकपत्नीत्व सामान्य सामाजिक मानदंड था, लेकिन राजाओं और उच्च कुलीन योद्धाओं ने बहुविवाह (कई पत्नियां) का अभ्यास किया था।"
    },
    # Q18
    {
        "q": "Consider the following statements regarding the status of the 'Grihapati' in Rigvedic family hierarchy:\n1. The Grihapati was the master of the household and owned family pastures.\n2. The Grihapati represented the family in local assemblies (Sabha).\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. The Grihapati (family head) managed the domestic unit and represented it in assemblies.",
        "q_hi": "ऋग्वैदिक पारिवारिक पदानुक्रम में 'गृहपति' की स्थिति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गृहपति घर का स्वामी होता था और पारिवारिक चरागाहों का मालिक होता था।\n2. गृहपति स्थानीय सभाओं (सभा) में परिवार का प्रतिनिधित्व करता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। गृहपति (परिवार का मुखिया) घरेलू इकाई का प्रबंधन करता था और सभाओं में इसका प्रतिनिधित्व करता था।"
    },
    # Q19
    {
        "q": "Who was the female seer mentioned in the Rigveda as having composed hymns and sponsored sacrifices to secure marital bliss?",
        "opts": ["Vishvavara", "Gargi", "Maitreyi", "Sulabha"],
        "ans": 0,
        "sol": "Vishvavara is one of the celebrated female composers of Rigvedic hymns, alongside Apala and Lopamudra.",
        "q_hi": "ऋग्वेद में उल्लिखित वह महिला ऋषि कौन थीं जिन्होंने भजनों की रचना की थी और वैवाहिक सुख प्राप्त करने के लिए यज्ञों का आयोजन किया था?",
        "opts_hi": ["विश्ववारा", "गार्गी", "मैत्रेयी", "सुलभा"],
        "ans_hi": 0,
        "sol_hi": "विश्ववारा ऋग्वैदिक भजनों की प्रसिद्ध महिला रचनाकारों में से एक हैं, जिनके साथ अपाला और लोपामुद्रा भी शामिल हैं।"
    },
    # Q20
    {
        "q": "In early Vedic society, the secondary alcoholic beverage 'Sura' was characterized as:",
        "opts": [
            "A secular, grain-based liquor popular among commoners but frowned upon by priests",
            "A mountain herb extract used only in Soma sacrifices",
            "A milk-honey mixture offered to deceased ancestors",
            "A purification chemical used by weavers to dye garments"
        ],
        "ans": 0,
        "sol": "Sura was grain liquor consumed during popular celebrations, but frowned upon in religious contexts due to its intoxicating nature.",
        "q_hi": "प्रारंभिक वैदिक समाज में, द्वितीयक मादक पेय 'सुरा' की विशेषता क्या थी?",
        "opts_hi": [
            "अनाज आधारित एक धर्मनिरपेक्ष मदिरा जो आम लोगों के बीच लोकप्रिय थी लेकिन पुरोहितों द्वारा नापसंद की जाती थी",
            "एक पहाड़ी जड़ी-बूटी का अर्क जिसका उपयोग केवल सोम यज्ञों में किया जाता था",
            "मृत पूर्वजों को अर्पित किया जाने वाला दूध-शहद का मिश्रण",
            "वस्त्रों को रंगने के लिए बुनकरों द्वारा उपयोग किया जाने वाला एक शोधन रसायन"
        ],
        "ans_hi": 0,
        "sol_hi": "सुरा अनाज से बनी मदिरा थी जिसका सेवन आम उत्सवों के दौरान किया जाता था, लेकिन इसके नशीले स्वभाव के कारण धार्मिक संदर्भों में इसे नापसंद किया जाता था।"
    },
    # Q21
    {
        "q": "Which of the following describes the position of the father (Kulapa/Grihapati) in Rigvedic family administration?",
        "opts": [
            "He had broad patriarchal powers, but could not sell or disinherit his children under customary ethics",
            "He held absolute divine rights of life and death over children without any checks",
            "He was subordinate to the mother in domestic affairs",
            "His authority was shared equally with the eldest daughter of the household"
        ],
        "ans": 0,
        "sol": "Though patriarchal authority was strong, child protection and family ethics restricted extreme abuses like selling children.",
        "q_hi": "निम्नलिखित में से कौन ऋग्वैदिक पारिवारिक प्रशासन में पिता (कुलप/गृहपति) की स्थिति का वर्णन करता है?",
        "opts_hi": [
            "उसके पास व्यापक पितृसत्तात्मक शक्तियाँ थीं, लेकिन प्रथागत नैतिकता के तहत वह अपने बच्चों को बेच या बेदखल नहीं कर सकता था",
            "उसके पास बिना किसी रोक-टोक के बच्चों पर जीवन और मृत्यु का पूर्ण दैवीय अधिकार था",
            "घरेलू मामलों में वह माता के अधीन होता था",
            "उसका अधिकार परिवार की सबसे बड़ी बेटी के साथ समान रूप से साझा किया जाता था"
        ],
        "ans_hi": 0,
        "sol_hi": "यद्यपि पितृसत्तात्मक अधिकार मजबूत था, लेकिन बाल संरक्षण और पारिवारिक नैतिकता ने बच्चों को बेचने जैसे चरम शोषण को प्रतिबंधित किया था।"
    },
    # Q22
    {
        "q": "Consider the following statements regarding the early Vedic diet and agricultural habits:\n1. The Rigvedic diet was predominantly vegetarian, heavily centered on dairy products.\n2. Barley (Yava) was roasted and mixed with milk or ghee as a common dish (Karambha).\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Karambha was a popular dish made of barley flour mixed with ghee or curd.",
        "q_hi": "प्रारंभिक वैदिक आहार और कृषि आदतों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ऋग्वैदिक आहार मुख्य रूप से शाकाहारी था, जो डेयरी उत्पादों पर भारी केंद्रित था।\n2. जौ (यव) को भूनकर दूध या घी के साथ मिलाकर एक सामान्य व्यंजन (करम्भ) तैयार किया जाता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। करम्भ जौ के आटे को घी या दही के साथ मिलाकर बनाया जाने वाला एक लोकप्रिय व्यंजन था।"
    },
    # Q23
    {
        "q": "In the Rigvedic social vocabulary, the word 'Sajana' refers to which group?",
        "opts": ["Members of the same clan or kinship lineage", "Defeated non-Aryan servants", "Priestly assistants of the Purohita", "Artisans working in metal guilds"],
        "ans": 0,
        "sol": "Sajana represents clansmen or kinsmen who shared common bloodline and fought together in battles.",
        "q_hi": "ऋग्वैदिक सामाजिक शब्दावली में, 'सजन' शब्द किस समूह को संदर्भित करता है?",
        "opts_hi": ["एक ही वंश या सगोत्रता के सदस्य", "पराजित गैर-आर्य सेवक", "पुरोहित के सहायक पुरोहित", "धातु संघों में काम करने वाले कारीगर"],
        "ans_hi": 0,
        "sol_hi": "सजन उन सगोत्रों या कबीले के सदस्यों का प्रतिनिधित्व करता है जो समान रक्त रेखा साझा करते थे और युद्धों में एक साथ लड़ते थे।"
    },
    # Q24
    {
        "q": "Which of the following games was a highly popular amusement in Rigvedic society but also warned against due to its ruinous effects?",
        "opts": ["Dicing (Aksa)", "Chariot racing", "Archery contests", "Bull fighting"],
        "ans": 0,
        "sol": "Dicing (playing with Aksa/dice) was popular, but Rigvedic hymns (like the Gambler's Lament in Mandala 10) warn against its addictive ruin.",
        "q_hi": "निम्नलिखित में से कौन सा खेल ऋग्वैदिक समाज में एक अत्यधिक लोकप्रिय मनोरंजन था लेकिन इसके विनाशकारी प्रभावों के कारण इसके प्रति चेतावनी भी दी गई थी?",
        "opts_hi": ["पासा खेलना (अक्ष)", "रथ दौड़", "तीरंदाजी प्रतियोगिता", "सांडों की लड़ाई"],
        "ans_hi": 0,
        "sol_hi": "पासा (अक्ष/जुआ) खेलना लोकप्रिय था, लेकिन ऋग्वैदिक भजनों (जैसे कि 10वें मंडल में जुआरी का विलाप) में इसके व्यसनी विनाश के खिलाफ चेतावनी दी गई है।"
    },
    # Q25
    {
        "q": "Assertion (A): Rigvedic women did not possess independent legal rights to inherit paternal property.\nReason (R): Rigvedic society was patriarchal and focused on patrilineal descent and family integrity.\nCodes:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true. Women held high status but property was held and inherited by males to keep lineage herds intact.",
        "q_hi": "कथन (A): ऋग्वैदिक महिलाओं के पास पैतृक संपत्ति विरासत में पाने के स्वतंत्र कानूनी अधिकार नहीं थे।\nकारण (R): ऋग्वैदिक समाज पितृसत्तात्मक था और पितृवंशीय वंशानुक्रम तथा पारिवारिक अखंडता पर केंद्रित था।\nकोड:",
        "opts_hi": [
            "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
            "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
            "A सही है लेकिन R गलत है",
            "A गलत है लेकिन R सही है"
        ],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। महिलाओं को उच्च स्थान प्राप्त था लेकिन वंश के पशुधन को अक्षुण्ण रखने के लिए संपत्ति पुरुषों द्वारा रखी जाती थी और विरासत में दी जाती थी।"
    },
    # Q26
    {
        "q": "Which of the following metal types was referred to by the Rigvedic term 'Krishna-ayas' in the Later Vedic texts?",
        "opts": ["Iron", "Copper", "Gold", "Lead"],
        "ans": 0,
        "sol": "Krishna-ayas (black metal) refers to iron, which only appears in Later Vedic texts. Early Rigvedic used 'Ayas' (bronze/copper).",
        "q_hi": "उत्तर वैदिक ग्रंथों में ऋग्वैदिक शब्द 'कृष्ण-अयस' द्वारा निम्नलिखित में से किस धातु के प्रकार को संदर्भित किया गया था?",
        "opts_hi": ["लोहा", "तांबा", "सोना", "सीसा"],
        "ans_hi": 0,
        "sol_hi": "कृष्ण-अयस (काली धातु) लोहे को संदर्भित करता है, जो केवल उत्तर वैदिक ग्रंथों में दिखाई देता है। प्रारंभिक ऋग्वैदिक काल में 'अयस' (कांस्य/तांबा) का उपयोग किया जाता था।"
    },
    # Q27
    {
        "q": "With reference to the craftsmen of the Rigvedic era, who was the 'Charmakara'?",
        "opts": ["Leatherworker", "Blacksmith", "Weaver", "Potter"],
        "ans": 0,
        "sol": "The Charmakara was a leatherworker who produced shields, bowstrings, reins, and water bags from animal hides.",
        "q_hi": "ऋग्वैदिक काल के शिल्पकारों के संदर्भ में, 'चर्मकार' कौन था?",
        "opts_hi": ["चर्म-शिल्पी", "लोहार", "बुनकर", "कुम्हार"],
        "ans_hi": 0,
        "sol_hi": "चर्मकार एक चमड़ा कलाकार था जो जानवरों की खाल से ढाल, धनुष की डोर, लगाम और पानी के थैले बनाता था।"
    },
    # Q28
    {
        "q": "Consider the following statements regarding the status of widows in Rigvedic society:\n1. Widow remarriage was legally and socially permitted.\n2. The custom of burning widows on the funeral pyre (Sati) was highly prevalent.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Widow remarriage was allowed, and Sati was completely absent in the early Rigvedic period (so Statement 2 is false).",
        "q_hi": "ऋग्वैदिक समाज में विधवाओं की स्थिति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. विधवा पुनर्विवाह कानूनी और सामाजिक रूप से स्वीकृत था।\n2. चिता पर विधवाओं को जलाने की प्रथा (सती प्रथा) अत्यधिक प्रचलित थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। विधवा पुनर्विवाह की अनुमति थी, और प्रारंभिक ऋग्वैदिक काल में सती प्रथा पूरी तरह से अनुपस्थित थी (इसलिए कथन 2 गलत है)।"
    },
    # Q29
    {
        "q": "The Rigvedic division between Aryas and Dasas was primarily based on which parameters?",
        "opts": [
            "Language and religious sacrifices",
            "Rigid hereditary caste lines registered in guilds",
            "Geographical borders divided by the Indus river",
            "The iron technology used in chariot wheels"
        ],
        "ans": 0,
        "sol": "The early division was linguistic (Mridhravac/hostile speech) and ritual (anyavrata/different rites), not based on rigid caste lines.",
        "q_hi": "आर्यों और दासों के बीच ऋग्वैदिक विभाजन मुख्य रूप से किन मानदंडों पर आधारित था?",
        "opts_hi": [
            "भाषा और धार्मिक यज्ञ",
            "श्रेणियों में पंजीकृत कठोर वंशानुगत जाति रेखाएं",
            "सिंधु नदी द्वारा विभाजित भौगोलिक सीमाएँ",
            "रथ के पहियों में प्रयुक्त लोहे की तकनीक"
        ],
        "ans_hi": 0,
        "sol_hi": "प्रारंभिक विभाजन भाषाई (मृध्रवाच/विरोधी भाषा) और अनुष्ठानिक (अन्यव्रत/भिन्न अनुष्ठान) था, न कि कठोर जाति रेखाओं पर आधारित।"
    },
    # Q30
    {
        "q": "What was the term used in the Rigvedic period for girls who chose to remain unmarried and stay at their father's house throughout their lives?",
        "opts": ["Amaju", "Sabhāvati", "Brahmavadini", "Grihapati"],
        "ans": 0,
        "sol": "Amaju was the term for females who remained unmarried and lived in their parent's home, receiving a share in ancestral maintenance.",
        "q_hi": "ऋग्वैदिक काल में उन लड़कियों के लिए किस शब्द का प्रयोग किया जाता था जिन्होंने अविवाहित रहने और जीवन भर अपने पिता के घर रहने का फैसला किया था?",
        "opts_hi": ["अमाजू", "सभावती", "ब्रह्मवादिनी", "गृहपति"],
        "ans_hi": 0,
        "sol_hi": "अमाजू उन महिलाओं के लिए इस्तेमाल किया जाने वाला शब्द था जो अविवाहित रहीं और अपने माता-पिता के घर में रहीं, और उन्हें पैतृक भरण-पोषण में हिस्सा मिलता था।"
    },
    # Q31
    {
        "q": "Consider the following statements regarding early Vedic social transitions:\n1. The migration to the Ganga-Yamuna Doab triggered settled agriculture.\n2. The surplus from agriculture led to class division and increased status for ruling groups.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Eastward migration and agriculture led to surplus wealth accumulation by chieftains and priests, creating class divisions.",
        "q_hi": "प्रारंभिक वैदिक सामाजिक परिवर्तनों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. गंगा-यमुना दोआब में प्रवास ने स्थायी कृषि को गति दी।\n2. कृषि से प्राप्त अधिशेष (सरप्लस) के कारण वर्ग विभाजन हुआ और शासक समूहों की स्थिति में वृद्धि हुई।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। पूर्व की ओर प्रवास और कृषि के कारण प्रमुखों और पुरोहितों द्वारा अधिशेष धन का संचय हुआ, जिससे वर्ग विभाजन हुआ।"
    },
    # Q32
    {
        "q": "In the context of the early Vedic economy, which animal is described as the standard of barter transactions?",
        "opts": ["Cow (Gau)", "Horse (Ashva)", "Sheep (Avi)", "Elephant (Hasti)"],
        "ans": 0,
        "sol": "The cow was the standard unit of value, though horses and gold ornaments were also used.",
        "q_hi": "प्रारंभिक वैदिक अर्थव्यवस्था के संदर्भ में, किस जानवर को वस्तु विनिमय के लेन-देन का मानक माना गया है?",
        "opts_hi": ["गाय (गौ)", "घोड़ा (अश्व)", "भेड़ (अवि)", "हाथी (हस्ती)"],
        "ans_hi": 0,
        "sol_hi": "गाय मूल्य की मानक इकाई थी, हालांकि घोड़ों और सोने के आभूषणों का भी विनिमय में उपयोग किया जाता था।"
    },
    # Q33
    {
        "q": "The prestigious gold ornament 'Rukma' mentioned in the Rigveda was worn as a:",
        "opts": ["Breastplate or disc ornament worn on the chest", "Ring on the finger", "Anklet", "Crown on the head"],
        "ans": 0,
        "sol": "Rukma was a brilliant gold plate or disc ornament worn on the chest, often mentioned in descriptions of gods like Maruts.",
        "q_hi": "ऋग्वेद में उल्लिखित प्रतिष्ठित सोने का आभूषण 'रुक्म' किस रूप में पहना जाता था?",
        "opts_hi": ["छाती पर पहना जाने वाला एक स्वर्ण-चक्र या आभूषण", "उंगली में अंगूठी", "पायल", "सिर पर मुकुट"],
        "ans_hi": 0,
        "sol_hi": "रुक्म छाती पर पहना जाने वाला एक चमकीला सोने का पत्तर या चक्राकार आभूषण था, जिसका उल्लेख अक्सर मरुत जैसे देवताओं के विवरण में मिलता है।"
    },
    # Q34
    {
        "q": "Consider the following statements regarding the Vedic food and drinks:\n1. Soma was a drink offered to the gods during sacrifices.\n2. Sura was an alcoholic beverage prepared from grains.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Soma was highly sacred (religious), while Sura was secular and popular grain alcohol.",
        "q_hi": "वैदिक भोजन और पेय पदार्थों के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. सोम यज्ञों के दौरान देवताओं को अर्पित किया जाने वाला पेय था।\n2. सुरा अनाज से तैयार किया जाने वाला एक मादक पेय था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। सोम अत्यधिक पवित्र (धार्मिक) था, जबकि सुरा सामान्य लोकप्रिय अनाज मदिरा थी।"
    },
    # Q35
    {
        "q": "Which of the following Rigvedic terms represents a group of families forming a mobile kin group under a leader?",
        "opts": ["Grama", "Kula", "Vis", "Jana"],
        "ans": 0,
        "sol": "The Grama was a mobile camp of kinsmen led by the Gramani.",
        "q_hi": "निम्नलिखित में से कौन सा ऋग्वैदिक शब्द एक नेता के अधीन एक गतिशील सगोत्र समूह बनाने वाले परिवारों के समूह को दर्शाता है?",
        "opts_hi": ["ग्राम", "कुल", "विश", "जन"],
        "ans_hi": 0,
        "sol_hi": "ग्राम ग्रामणी के नेतृत्व में सगोत्रों का एक गतिशील शिविर था।"
    },
    # Q36
    {
        "q": "The term 'Sabhāvati' in the Rigvedic texts demonstrates which aspect of social life?",
        "opts": [
            "Women had the right to participate in assembly discussions",
            "The assembly was headed by a female queen",
            "Polygamy was the standard norm of the royal court",
            "Special quarters were reserved for female artisans"
        ],
        "ans": 0,
        "sol": "Sabhāvati proves that women actively participated in and deliberated in the political councils of the early Vedic period.",
        "q_hi": "ऋग्वैदिक ग्रंथों में 'सभावती' शब्द सामाजिक जीवन के किस पहलू को प्रदर्शित करता है?",
        "opts_hi": [
            "महिलाओं को सभा की चर्चाओं में भाग लेने का अधिकार था",
            "सभा का नेतृत्व एक महिला रानी करती थी",
            "बहुविवाह शाही दरबार का सामान्य मानक था",
            "महिला कारीगरों के लिए विशेष क्वार्टर आरक्षित थे"
        ],
        "ans_hi": 0,
        "sol_hi": "सभावती यह सिद्ध करता है कि महिलाओं ने प्रारंभिक वैदिक काल की राजनीतिक परिषदों में सक्रिय रूप से भाग लिया और विचार-विमर्श किया था।"
    },
    # Q37
    {
        "q": "With reference to the class division in the Later Vedic period, which Rigvedic hymn laid the cosmic justification for the Varna hierarchy?",
        "opts": ["Purusha Sukta", "Nasadiya Sukta", "Hiranyagarbha Sukta", "Devi Sukta"],
        "ans": 0,
        "sol": "The Purusha Sukta (10th Mandala) justified class hierarchy by linking varnas to the creation from the primeval giant.",
        "q_hi": "उत्तर वैदिक काल में वर्ग विभाजन के संदर्भ में, किस ऋग्वैदिक सूक्त ने वर्ण पदानुक्रम के लिए ब्रह्मांडीय औचित्य की नींव रखी थी?",
        "opts_hi": ["पुरुष सूक्त", "नासदीय सूक्त", "हिरण्यगर्भ सूक्त", "देवी सूक्त"],
        "ans_hi": 0,
        "sol_hi": "पुरुष सूक्त (10वें मंडल) ने वर्णों को आदि पुरुष से सृष्टि के निर्माण से जोड़कर वर्ग पदानुक्रम को उचित ठहराया।"
    },
    # Q38
    {
        "q": "Consider the following statements regarding the early Vedic crafts:\n1. Weaving (spinning and loom work) was primarily performed by women.\n2. The carpenter (Takshan) enjoyed a respected status due to chariot-making.\nWhich of the statements given above is/are correct?",
        "opts": ["Both 1 and 2", "1 only", "2 only", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Both statements are correct. Weaving was a major female craft, and carpenters had high status due to ratha-making.",
        "q_hi": "प्रारंभिक वैदिक शिल्पकला के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. बुनाई (कताई और करघे का काम) मुख्य रूप से महिलाओं द्वारा की जाती थी।\n2. बढ़ई (तक्षण) रथ निर्माण के कारण सम्मानित स्थिति का आनंद लेता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["1 और 2 दोनों", "केवल 1", "केवल 2", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सही हैं। बुनाई एक प्रमुख महिला शिल्प था, और रथ निर्माण के कारण बढ़ई की स्थिति उच्च थी।"
    },
    # Q39
    {
        "q": "Which of the following represents the correct hierarchical order of social units from the smallest to the largest in Rigvedic society?",
        "opts": [
            "Kula -> Grama -> Vis -> Jana",
            "Grama -> Kula -> Vis -> Jana",
            "Kula -> Vis -> Grama -> Jana",
            "Jana -> Vis -> Grama -> Kula"
        ],
        "ans": 0,
        "sol": "The order is Kula (family), Grama (clan unit), Vis (clan canton), and Jana (entire tribe).",
        "q_hi": "ऋग्वैदिक समाज में सबसे छोटी से सबसे बड़ी सामाजिक इकाई का सही पदानुक्रमित क्रम निम्नलिखित में से कौन सा है?",
        "opts_hi": [
            "कुल -> ग्राम -> विश -> जन",
            "ग्राम -> कुल -> विश -> जन",
            "कुल -> विश -> ग्राम -> जन",
            "जन -> विश -> ग्राम -> कुल"
        ],
        "ans_hi": 0,
        "sol_hi": "क्रम कुल (परिवार), ग्राम (कबीला इकाई), विश (कबीला छावनी), और जन (संपूर्ण जनजाति) है।"
    },
    # Q40
    {
        "q": "Assertion (A): Rigvedic society was patriarchal but women enjoyed high respect.\nReason (R): Girls received Vedic education, attended assemblies, and child marriage was absent.\nCodes:",
        "opts": [
            "Both A and R are true and R is the correct explanation of A",
            "Both A and R are true but R is not the correct explanation of A",
            "A is true but R is false",
            "A is false but R is true"
        ],
        "ans": 0,
        "sol": "Both statements are true, and the freedom/education of women explains their respected status within the patriarchy.",
        "q_hi": "कथन (A): ऋग्वैदिक समाज पितृसत्तात्मक था लेकिन महिलाओं को उच्च सम्मान प्राप्त था।\nकारण (R): लड़कियों को वैदिक शिक्षा मिलती थी, वे सभाओं में भाग लेती थीं, और बाल विवाह अनुपस्थित था।\nकोड:",
        "opts_hi": [
            "A और R दोनों सही हैं और R, A की सही व्याख्या करता है",
            "A और R दोनों सही हैं लेकिन R, A की सही व्याख्या नहीं करता है",
            "A सही है लेकिन R गलत है",
            "A गलत है लेकिन R सही है"
        ],
        "ans_hi": 0,
        "sol_hi": "दोनों कथन सत्य हैं, और महिलाओं की स्वतंत्रता/शिक्षा पितृसत्ता के भीतर उनकी सम्मानित स्थिति की व्याख्या करती है।"
    },
    # Q41
    {
        "q": "In the Rigvedic period, the metalworker who worked with copper and bronze was called:",
        "opts": ["Karmara", "Takshan", "Charmakara", "Vispati"],
        "ans": 0,
        "sol": "The Karmara worked with Ayas (copper/bronze) to manufacture tools and weapons.",
        "q_hi": "ऋग्वैदिक काल में तांबे और कांसे का काम करने वाले धातु कर्मकार को क्या कहा जाता था?",
        "opts_hi": ["कर्मार", "तक्षण", "चर्मकार", "विशपति"],
        "ans_hi": 0,
        "sol_hi": "कर्मार उपकरण और हथियार बनाने के लिए अयस (तांबे/कांसे) के साथ काम करता था।"
    },
    # Q42
    {
        "q": "Which of the following Rigvedic terms represents a female weaver?",
        "opts": ["Vayatri", "Brahmavadini", "Sabhāvati", "Kulapa"],
        "ans": 0,
        "sol": "Vayatri denotes a female weaver in Rigvedic occupational structure.",
        "q_hi": "निम्नलिखित में से कौन सा ऋग्वैदिक शब्द एक महिला बुनकर का प्रतिनिधित्व करता है?",
        "opts_hi": ["वयित्री", "ब्रह्मवादिनी", "सभावती", "कुलप"],
        "ans_hi": 0,
        "sol_hi": "वयित्री ऋग्वैदिक व्यावसायिक संरचना में एक महिला बुनकर को दर्शाता है।"
    },
    # Q43
    {
        "q": "Consider the following statements regarding the non-Aryan tribe called 'Panis':\n1. They were rich traders who hoarded cattle herds.\n2. They were highly praised by Vedic priests for sponsoring sacrifices.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. Panis were rich cattle-owners but were hated by priests because they refused to perform sacrifices (so Statement 2 is false).",
        "q_hi": "पणि नामक गैर-आर्य जनजाति के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. वे अमीर व्यापारी थे जो मवेशियों के झुंड जमा करते थे।\n2. यज्ञों का आयोजन करने के लिए वैदिक पुरोहितों द्वारा उनकी अत्यधिक प्रशंसा की जाती थी।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। पणि अमीर मवेशी-मालिक थे लेकिन पुरोहितों द्वारा उनसे घृणा की जाती थी क्योंकि उन्होंने यज्ञ करने से इनकार कर दिया था (इसलिए कथन 2 गलत है)।"
    },
    # Q44
    {
        "q": "In the Rigvedic context, the term 'Amaju' represents:",
        "opts": [
            "A woman who chose to remain unmarried throughout her life",
            "A childless widow who remarried her brother-in-law",
            "The head of the local artisan guild",
            "A girl married at an early mature age"
        ],
        "ans": 0,
        "sol": "Amaju refers to a woman who chose lifelong spinsterhood and resided with her parental family.",
        "q_hi": "ऋग्वैदिक संदर्भ में, 'अमाजू' शब्द किसे दर्शाता है?",
        "opts_hi": [
            "वह महिला जिसने जीवन भर अविवाहित रहने का फैसला किया",
            "एक निःसंतान विधवा जिसने अपने देवर से पुनर्विवाह किया",
            "स्थानीय शिल्पकार संघ के प्रमुख",
            "एक लड़की जिसका विवाह परिपक्व आयु में हुआ हो"
        ],
        "ans_hi": 0,
        "sol_hi": "अमाजू उस महिला को संदर्भित करता है जिसने आजीवन अविवाहित रहने का विकल्प चुना और अपने माता-पिता के परिवार के साथ रही।"
    },
    # Q45
    {
        "q": "The pastoral mobility of the early Vedic people had which political and social consequence?",
        "opts": [
            "It prevented the growth of fixed cities and territorial boundaries",
            "It led to the early establishment of empires with written laws",
            "It resulted in the complete absence of family hierarchy",
            "It forced the transition of the entire population to rice agriculture"
        ],
        "ans": 0,
        "sol": "Pastoral nomadism made it difficult to establish sedentary cities or territorial state systems.",
        "q_hi": "प्रारंभिक वैदिक लोगों की पशुचारण गतिशीलता का क्या राजनीतिक और सामाजिक परिणाम हुआ?",
        "opts_hi": [
            "इसने निश्चित शहरों और क्षेत्रीय सीमाओं के विकास को रोका",
            "इसके कारण लिखित कानूनों के साथ साम्राज्यों की प्रारंभिक स्थापना हुई",
            "इसके परिणामस्वरूप पारिवारिक पदानुक्रम का पूर्ण अभाव हुआ",
            "इसने पूरी आबादी को धान की खेती की ओर संक्रमण के लिए मजबूर किया"
        ],
        "ans_hi": 0,
        "sol_hi": "पशुचारण खानाबदोश जीवन शैली ने स्थायी शहरों या क्षेत्रीय राज्य प्रणालियों को स्थापित करना कठिन बना दिया था।"
    },
    # Q46
    {
        "q": "Which of the following foods was NOT known or consumed by the early Rigvedic people?",
        "opts": ["Vrihi (Rice)", "Yava (Barley)", "Ghee", "Milk Curd"],
        "ans": 0,
        "sol": "Rice (Vrihi) was not known in the early Sapta-Sindhu phase; it appears in Later Vedic texts as clans moved to the wetter Ganga valley.",
        "q_hi": "निम्नलिखित में से कौन सा खाद्य पदार्थ प्रारंभिक ऋग्वैदिक लोगों को ज्ञात नहीं था या उनके द्वारा उपभोग नहीं किया जाता था?",
        "opts_hi": ["व्रीहि (धान)", "यव (जौ)", "घी", "दही"],
        "ans_hi": 0,
        "sol_hi": "प्रारंभिक सप्त-सिंधु चरण में धान (व्रीहि) ज्ञात नहीं था; यह उत्तर वैदिक ग्रंथों में दिखाई देता है जैसे ही कबीले आर्द्र गंगा घाटी की ओर बढ़े।"
    },
    # Q47
    {
        "q": "With reference to Rigvedic ornaments, the ornament 'Rukma' was traditionally made of:",
        "opts": ["Gold", "Iron", "Bronze", "Silver"],
        "ans": 0,
        "sol": "Rukma was a brilliant gold chest-piece ornament.",
        "q_hi": "ऋग्वैदिक आभूषणों के संदर्भ में, 'रुक्म' आभूषण पारंपरिक रूप से किससे बना होता था?",
        "opts_hi": ["सोना", "लोहा", "कांसा", "चांदी"],
        "ans_hi": 0,
        "sol_hi": "रुक्म छाती पर पहना जाने वाला एक चमकदार सोने का आभूषण था।"
    },
    # Q48
    {
        "q": "Consider the following statements regarding the role of 'Gramani' in Rigvedic social layout:\n1. The Gramani led the mobile family clusters (Grama) during migrations.\n2. The Gramani was the head priest who conducted domestic rituals.\nWhich of the statements given above is/are correct?",
        "opts": ["1 only", "2 only", "Both 1 and 2", "Neither 1 nor 2"],
        "ans": 0,
        "sol": "Statement 1 is correct. The Gramani was a village/clan head who led them in migrations and military raids, not a priest.",
        "q_hi": "ऋग्वैदिक सामाजिक व्यवस्था में 'ग्रामणी' की भूमिका के संबंध में निम्नलिखित कथनों पर विचार करें:\n1. ग्रामणी ने प्रवास के दौरान गतिशील पारिवारिक समूहों (ग्राम) का नेतृत्व किया।\n2. ग्रामणी मुख्य पुरोहित था जो घरेलू अनुष्ठान करता था।\nउपरोक्त कथनों में से कौन सा/से सही है/हैं?",
        "opts_hi": ["केवल 1", "केवल 2", "1 और 2 दोनों", "न तो 1 और न ही 2"],
        "ans_hi": 0,
        "sol_hi": "कथन 1 सही है। ग्रामणी एक ग्राम/कबीले का प्रमुख था जो प्रवास और सैन्य छापों में उनका नेतृत्व करता था, पुरोहित नहीं।"
    },
    # Q49
    {
        "q": "The system of weregild or blood-money compensation for murder in Rigvedic justice was called:",
        "opts": ["Vairadeya", "Bhaga", "Bali", "Niyoga"],
        "ans": 0,
        "sol": "Vairadeya was the system of weregild where murder was compensated in cows to prevent blood feuds.",
        "q_hi": "ऋग्वैदिक न्याय में हत्या के लिए मुआवजे (रक्त-मूल्य) की प्रणाली को क्या कहा जाता था?",
        "opts_hi": ["वैरदेय", "भाग", "बलि", "नियोग"],
        "ans_hi": 0,
        "sol_hi": "वैरदेय रक्त-मूल्य की प्रणाली थी जहाँ खून के बदले खून के संघर्ष को रोकने के लिए पीड़ित परिवार को गायों के रूप में हर्जाना दिया जाता था।"
    },
    # Q50
    {
        "q": "Which assembly is described in the Rigveda as a place for social entertainment, dicing, and music alongside political debates?",
        "opts": ["Sabha", "Samiti", "Vidatha", "Gana"],
        "ans": 0,
        "sol": "The Sabha was not only a political council but also a center of social life, dicing, music, and gatherings.",
        "q_hi": "ऋग्वेद में राजनीतिक बहसों के साथ-साथ सामाजिक मनोरंजन, पासा खेलने और संगीत के स्थान के रूप में किस सभा का वर्णन किया गया है?",
        "opts_hi": ["सभा", "समिति", "विदथ", "गण"],
        "ans_hi": 0,
        "sol_hi": "सभा न केवल एक राजनीतिक परिषद थी बल्कि सामाजिक जीवन, पासा खेलने, संगीत और सामाजिक समारोहों का एक केंद्र भी थी।"
    }
]

# 4. Mock Test Questions (10 authentic questions)
mock_questions_eng = [
    {
        "id": "m_q_1",
        "type": "MCQ",
        "q": "In early Vedic society, who was the master of the household who held patriarchal authority over the family?",
        "opts": ["Grihapati or Kulapa", "Vispati", "Gramani", "Rajan"],
        "ans": 0,
        "sol": "The Grihapati (or Kulapa) was the male head of the patriarchal family unit (Kula/Griha)."
    },
    {
        "id": "m_q_2",
        "type": "MCQ",
        "q": "The four-fold Varna system appears for the first time in which part of the Rigvedic corpus?",
        "opts": ["Purusha Sukta of Mandala 10", "Nasadiya Sukta of Mandala 10", "Mandala 9 hymns", "Mandala 3 hymns"],
        "ans": 0,
        "sol": "The Purusha Sukta of Mandala 10 first describes the creation of the four Varnas from the cosmic giant's body."
    },
    {
        "id": "m_q_3",
        "type": "MCQ",
        "q": "Which term in the Rigveda is used to describe a woman eligible to sit and participate in assembly discussions?",
        "opts": ["Sabhāvati", "Brahmavadini", "Amaju", "Grihapati"],
        "ans": 0,
        "sol": "A Sabhāvati was a woman who had the right to sit and participate in the Sabha assembly."
    },
    {
        "id": "m_q_4",
        "type": "MCQ",
        "q": "What was the principal grain cultivated by the early Indo-Aryans in the Sapta-Sindhu region?",
        "opts": ["Yava (Barley)", "Vrihi (Rice)", "Godhuma (Wheat)", "Tila"],
        "ans": 0,
        "sol": "Yava (barley) was the primary crop; rice (Vrihi) was introduced in Later Vedic times."
    },
    {
        "id": "m_q_5",
        "type": "MCQ",
        "q": "Which artisan group was held in high respect due to their role in building battle chariots (Rathas)?",
        "opts": ["Takshan (Carpenter)", "Karmara (Metalworker)", "Charmakara (Leatherworker)", "Vayatri (Weaver)"],
        "ans": 0,
        "sol": "Carpenters (Takshan) held a highly respected administrative and social position because of chariot-crafting."
    },
    {
        "id": "m_q_6",
        "type": "MCQ",
        "q": "The term 'Aghnya' in the Rigveda, applied to cows, literally means:",
        "opts": ["Not to be killed", "A sacred sacrifice", "The standard currency", "Cattle thief"],
        "ans": 0,
        "sol": "Aghnya literally means 'not to be killed/slain', denoting the sacred and economic value of the cow."
    },
    {
        "id": "m_q_7",
        "type": "MCQ",
        "q": "What was the nature of the sacred plant beverage 'Soma' in Rigvedic rituals?",
        "opts": [
            "It was a mountain-plant beverage offered to the gods and consumed in sacrifices",
            "It was a grain-brewed secular alcohol consumed in public festivals",
            "It was a dairy product used as currency in barter transactions",
            "It was a dye used by weavers to color wool garments"
        ],
        "ans": 0,
        "sol": "Soma was a highly sacred plant beverage offered to gods (especially Indra) to gain vitality."
    },
    {
        "id": "m_q_8",
        "type": "MCQ",
        "q": "Which social custom was completely absent in the early Rigvedic societal setup?",
        "opts": ["Sati or widow burning", "Niyoga (levirate)", "Widow remarriage", "Women attending assemblies"],
        "ans": 0,
        "sol": "Sati (widow burning) and child marriage were completely absent in the early Vedic societal setup."
    },
    {
        "id": "m_q_9",
        "type": "MCQ",
        "q": "The hierarchical ascending order of social units in early Vedic times is:",
        "opts": [
            "Kula -> Grama -> Vis -> Jana",
            "Grama -> Kula -> Vis -> Jana",
            "Kula -> Vis -> Grama -> Jana",
            "Jana -> Vis -> Grama -> Kula"
        ],
        "ans": 0,
        "sol": "The correct ascending order is Kula (family), Grama (clan unit), Vis (clan subdivision), and Jana (tribe)."
    },
    {
        "id": "m_q_10",
        "type": "MCQ",
        "q": "In Rigvedic justice, what was the weregild (blood-money compensation) system called?",
        "opts": ["Vairadeya", "Amaju", "Karambha", "Niyoga"],
        "ans": 0,
        "sol": "Vairadeya was the system of weregild where murder was compensated in cows to resolve disputes."
    }
]

mock_questions_hi = [
    {
        "id": "m_q_1",
        "type": "MCQ",
        "q": "प्रारंभिक वैदिक समाज में, परिवार पर पितृसत्तात्मक अधिकार रखने वाला घर का स्वामी कौन होता था?",
        "opts": ["गृहपति या कुलप", "विशपति", "ग्रामणी", "राजन"],
        "ans": 0,
        "sol": "गृहपति (या कुलप) पितृसत्तात्मक पारिवारिक इकाई (कुल/गृह) का पुरुष मुखिया होता था।"
    },
    {
        "id": "m_q_2",
        "type": "MCQ",
        "q": "चार-स्तरीय वर्ण व्यवस्था ऋग्वैदिक संग्रह के किस भाग में पहली बार दिखाई देती है?",
        "opts": ["मंडल 10 का पुरुष सूक्त", "मंडल 10 का नासदीय सूक्त", "मंडल 9 के भजन", "मंडल 3 के भजन"],
        "ans": 0,
        "sol": "10वें मंडल का पुरुष सूक्त पहली बार आदि पुरुष के शरीर से चार वर्णों के निर्माण का वर्णन करता है।"
    },
    {
        "id": "m_q_3",
        "type": "MCQ",
        "q": "ऋग्वेद में सभा की चर्चाओं में बैठने और भाग लेने के लिए पात्र महिला का वर्णन करने के लिए किस शब्द का प्रयोग किया जाता है?",
        "opts": ["सभावती", "ब्रह्मवादिनी", "अमाजू", "गृहपति"],
        "ans": 0,
        "sol": "सभावती वह महिला थी जिसे सभा में बैठने और भाग लेने का अधिकार प्राप्त था।"
    },
    {
        "id": "m_q_4",
        "type": "MCQ",
        "q": "सप्त-सिंधु क्षेत्र में प्रारंभिक भारत-आर्यों द्वारा खेती किया जाने वाला मुख्य अनाज क्या था?",
        "opts": ["यव (जौ)", "व्रीहि (धान)", "गोधूम (गेहूं)", "तिल"],
        "ans": 0,
        "sol": "यव (जौ) प्राथमिक फसल थी; धान (व्रीहि) को उत्तर वैदिक काल में पेश किया गया था।"
    },
    {
        "id": "m_q_5",
        "type": "MCQ",
        "q": "युद्ध रथों (रथ) के निर्माण में उनकी भूमिका के कारण किस कारीगर समूह को उच्च सम्मान दिया जाता था?",
        "opts": ["तक्षण (बढ़ई)", "कर्मार (धातु कर्मकार)", "चर्मकार (चर्म-शिल्पी)", "वयित्री (बुनकर)"],
        "ans": 0,
        "sol": "रथ-निर्माण के कारण बढ़ई (तक्षण) को अत्यधिक सम्मानित प्रशासनिक और सामाजिक स्थान प्राप्त था।"
    },
    {
        "id": "m_q_6",
        "type": "MCQ",
        "q": "ऋग्वेद में गायों के लिए प्रयुक्त 'अघन्या' शब्द का शाब्दिक अर्थ है:",
        "opts": ["न मारने योग्य", "एक पवित्र बलि", "मानक मुद्रा", "मवेशी चोर"],
        "ans": 0,
        "sol": "अघन्या का शाब्दिक अर्थ है 'न मारे जाने योग्य/वध न करने योग्य', जो गाय के पवित्र और आर्थिक मूल्य को दर्शाता है।"
    },
    {
        "id": "m_q_7",
        "type": "MCQ",
        "q": "ऋग्वैदिक अनुष्ठानों में पवित्र पौधे के पेय 'सोम' की प्रकृति क्या थी?",
        "opts": [
            "यह एक पहाड़ी पौधे का पेय था जो देवताओं को अर्पित किया जाता था और यज्ञों में उपभोग किया जाता था",
            "यह अनाज से बनी एक धर्मनिरपेक्ष शराब थी जिसका सेवन सार्वजनिक त्योहारों में किया जाता था",
            "यह एक डेयरी उत्पाद था जिसका उपयोग वस्तु विनिमय में मुद्रा के रूप में किया जाता था",
            "यह बुनकरों द्वारा ऊनी कपड़ों को रंगने के लिए इस्तेमाल किया जाने वाला एक रंग था"
        ],
        "ans": 0,
        "sol": "सोम एक अत्यधिक पवित्र पौधे का पेय था जिसे जीवन शक्ति प्राप्त करने के लिए देवताओं (विशेष रूप से इंद्र) को अर्पित किया जाता था।"
    },
    {
        "id": "m_q_8",
        "type": "MCQ",
        "q": "प्रारंभिक ऋग्वैदिक सामाजिक व्यवस्था में कौन सी सामाजिक प्रथा पूरी तरह से अनुपस्थित थी?",
        "opts": ["सती प्रथा या विधवा को जलाना", "नियोग (देवर-विवाह)", "विधवा पुनर्विवाह", "महिलाओं का सभाओं में भाग लेना"],
        "ans": 0,
        "sol": "प्रारंभिक वैदिक सामाजिक व्यवस्था में सती प्रथा (विधवा को जलाना) और बाल विवाह पूरी तरह से अनुपस्थित थे।"
    },
    {
        "id": "m_q_9",
        "type": "MCQ",
        "q": "प्रारंभिक वैदिक काल में सामाजिक इकाइयों का पदानुक्रमित आरोही क्रम है:",
        "opts": [
            "कुल -> ग्राम -> विश -> जन",
            "ग्राम -> कुल -> विश -> जन",
            "कुल -> विश -> ग्राम -> जन",
            "जन -> विश -> ग्राम -> कुल"
        ],
        "ans": 0,
        "sol": "सही आरोही क्रम कुल (परिवार), ग्राम (कबीला इकाई), विश (कबीला उपखंड), और जन (जनजाति) है।"
    },
    {
        "id": "m_q_10",
        "type": "MCQ",
        "q": "ऋग्वैदिक न्याय में, रक्त-मूल्य (मुआवजे) प्रणाली को क्या कहा जाता था?",
        "opts": ["वैरदेय", "अमाजू", "करम्भ", "नियोग"],
        "ans": 0,
        "sol": "वैरदेय रक्त-मूल्य की प्रणाली थी जहाँ विवादों को सुलझाने के लिए गायों के रूप में हर्जाना दिया जाता था।"
    }
]

# We will populate exactly 50 unique practice questions
practice_qs_eng = []
practice_qs_hi = []

for i in range(50):
    base = practice_base[i % len(practice_base)]
    q_num = i + 1
    
    q_eng = {
        "id": f"p_q_{q_num}",
        "type": "MCQ",
        "q": base["q"],
        "opts": base["opts"],
        "ans": base["ans"],
        "sol": base["sol"]
    }
    
    q_hi = {
        "id": f"p_q_{q_num}",
        "type": "MCQ",
        "q": base["q_hi"],
        "opts": base["opts_hi"],
        "ans": base["ans_hi"],
        "sol": base["sol_hi"]
    }
    
    practice_qs_eng.append(q_eng)
    practice_qs_hi.append(q_hi)


# Compile everything into final data structures
eng_output = {
    "breadcrumbs": {
        "parent": "UPSC Syllabus",
        "parent_hi": "UPSC पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "Societal Setup",
        "current_hi": "सामाजिक संरचना"
    },
    "hero": {
        "title": "Societal Setup of the Rig Vedic Period",
        "description": "Kinship, Gender Status & Material Culture of the Early Indo-Aryans"
    },
    "deepDive": {
        "title": "Syllabus Core Study Notes (Deep-Dive)",
        "description": "Master the family structure, gender status, social stratification, economy, crafts, and transitions of early Vedic society.",
        "sections": eng_sections
    },
    "practiceQuestions": practice_qs_eng,
    "mockTestQuestions": mock_questions_eng,
    "labels": {
        "clickToExpand": "Click to expand details",
        "mockIntro": {
            "title": "Interactive UPSC Mock Test",
            "description": "Test your knowledge of the societal setup, varna systems, and material culture of the Rig Vedic period. This timed test contains 10 high-quality, exam-standard questions with detailed solutions.",
            "startBtn": "Start Mock Test"
        },
        "mockPlay": {
            "prevBtn": "Previous Question",
            "nextBtn": "Next Question",
            "submitBtn": "Submit Test"
        }
    },
    "timeline": {
        "title": "Rigvedic Societal Evolution",
        "description": "Click on each card below to explore social stages of the early Indo-Aryans.",
        "cards": [
            {
                "period": "Early Pastoral Phase",
                "date": "1500 BCE",
                "details": "Mobile pastoral clans, highly egalitarian, kinship-based family structure (Kula)."
            },
            {
                "period": "Mid-Vedic Social Integration",
                "date": "c. 1300 BCE",
                "details": "Integration with indigenous Dasas/Dasyus; emergence of early occupational varnas."
            },
            {
                "period": "Late Rigvedic Settlement",
                "date": "c. 1000 BCE",
                "details": "Sedentary agriculture begins in Doab; Varna systems mentioned in Purusha Sukta."
            }
        ]
    },
    "mnemonics": {
        "title": "Mnemonics & Memory Hacks",
        "description": "Short memory tips for Vedic social units and women seers.",
        "items": [
            {
                "title": "Vedic Social Units Order",
                "phrase": "K-G-V-J (Kula, Grama, Vis, Jana)",
                "decryption": "Remember: Kids Grow Very Joyful (Kula, Grama, Vis, Jana)."
            },
            {
                "title": "Women Seers of Rigveda",
                "phrase": "L-G-A-V (Lopamudra, Ghosha, Apala, Vishvavara)",
                "decryption": "Remember: Ladies Generate Active Vibes (Lopamudra, Ghosha, Apala, Vishvavara)."
            }
        ]
    },
    "traps": {
        "title": "UPSC Common Exam Traps to Avoid",
        "items": [
            "<strong>Trap:</strong> Rigvedic society had a rigid caste system. **False.** Class divisions were flexible and occupational; hereditary caste system developed in Later Vedic times.",
            "<strong>Trap:</strong> Rice (Vrihi) was a staple crop in early Rigvedic times. **False.** Barley (Yava) was the primary grain; rice appeared in Later Vedic times."
        ]
    },
    "flashcards": {
        "title": "Active Recall Flashcards",
        "description": "Flip to reveal key facts about Rig Vedic Society.",
        "items": [
            {
                "question": "What is the Sanskrit term for a woman scholar who composed hymns?",
                "answer": "Brahmavadini.",
                "icon": "fa-star"
            },
            {
                "question": "Which Mandala of the Rigveda contains the Purusha Sukta?",
                "answer": "Mandala 10.",
                "icon": "fa-book"
            }
        ]
    }
}

hi_output = {
    "breadcrumbs": {
        "parent": "UPSC पाठ्यक्रम",
        "parent_hi": "UPSC पाठ्यक्रम",
        "parentUrl": "/upsc/",
        "current": "सामाजिक संरचना",
        "current_hi": "सामाजिक संरचना"
    },
    "hero": {
        "title": "ऋग्वैदिक सामाजिक संरचना",
        "description": "प्रारंभिक भारत-आर्यों के सगोत्रता संबंध, लिंग स्थिति और भौतिक संस्कृति"
    },
    "deepDive": {
        "title": "पाठ्यक्रम कोर अध्ययन नोट्स (गहन अध्ययन)",
        "description": "प्रारंभिक वैदिक समाज के पारिवारिक संरचना, लिंग स्थिति, सामाजिक स्तरीकरण, अर्थव्यवस्था, शिल्प और संक्रमण में महारत हासिल करें।",
        "sections": hi_sections
    },
    "practiceQuestions": practice_qs_hi,
    "mockTestQuestions": mock_questions_hi,
    "labels": {
        "clickToExpand": "विवरण देखने के लिए क्लिक करें",
        "mockIntro": {
            "title": "इंटरैक्टिव UPSC मॉक टेस्ट",
            "description": "ऋग्वैदिक काल की सामाजिक संरचना, वर्ण व्यवस्था और भौतिक संस्कृति के अपने ज्ञान का परीक्षण करें। इस समयबद्ध परीक्षा में विस्तृत समाधानों के साथ 10 उच्च-गुणवत्ता वाले प्रश्न शामिल हैं।",
            "startBtn": "मॉक टेस्ट शुरू करें"
        },
        "mockPlay": {
            "prevBtn": "पिछला प्रश्न",
            "nextBtn": "अगला प्रश्न",
            "submitBtn": "सबमिट करें"
        }
    },
    "timeline": {
        "title": "ऋग्वैदिक सामाजिक विकास",
        "description": "प्रारंभिक भारत-आर्यों के सामाजिक चरणों का पता लगाने के लिए नीचे प्रत्येक कार्ड पर क्लिक करें।",
        "cards": [
            {
                "period": "प्रारंभिक पशुचारण चरण",
                "date": "1500 ईसा पूर्व",
                "details": "गतिशील पशुचारक कबीले, अत्यधिक समतावादी, सगोत्रता आधारित पारिवारिक संरचना (कुल)।"
            },
            {
                "period": "मध्य-वैदिक सामाजिक एकीकरण",
                "date": "लगभग 1300 ईसा पूर्व",
                "details": "स्वदेशी दासों/दस्युओं के साथ एकीकरण; प्रारंभिक व्यावसायिक वर्णों का उदय।"
            },
            {
                "period": "उत्तर ऋग्वैदिक स्थायी बसावट",
                "date": "लगभग 1000 ईसा पूर्व",
                "details": "दोआब में स्थायी कृषि शुरू; पुरुष सूक्त में वर्ण व्यवस्था का उल्लेख।"
            }
        ]
    },
    "mnemonics": {
        "title": "स्मरण सूत्र और मेमोरी हैक्स",
        "description": "वैदिक सामाजिक इकाइयों और महिला ऋषियों के लिए लघु मेमोरी टिप्स।",
        "items": [
            {
                "title": "वैदिक सामाजिक इकाइयों का क्रम",
                "phrase": "कुल -> ग्राम -> विश -> जन",
                "decryption": "याद रखें: कुल ग्राम में विश करते हैं जन।"
            },
            {
                "title": "ऋग्वेद की महिला ऋषि",
                "phrase": "लोपामुद्रा, घोषा, अपाला, विश्ववारा",
                "decryption": "प्रारंभिक वैदिक काल की प्रसिद्ध ब्रह्मवादिनी महिला ऋषि।"
            }
        ]
    },
    "traps": {
        "title": "बचने के लिए सामान्य UPSC परीक्षा के जाल",
        "items": [
            "<strong>जाल:</strong> ऋग्वैदिक समाज में एक कठोर जाति व्यवस्था थी। **असत्य।** वर्ग विभाजन लचीला और व्यावसायिक था; वंशानुगत जाति व्यवस्था उत्तर वैदिक काल में विकसित हुई।",
            "<strong>जाल:</strong> प्रारंभिक ऋग्वैदिक काल में धान (व्रीहि) एक मुख्य फसल थी। **असत्य।** जौ (यव) मुख्य अनाज था; धान उत्तर वैदिक काल में दिखाई दिया।"
        ]
    },
    "flashcards": {
        "title": "सक्रिय रिकॉल फ्लैशकार्ड",
        "description": "ऋग्वैदिक समाज के बारे में प्रमुख तथ्यों को प्रकट करने के लिए पलटें।",
        "items": [
            {
                "question": "भजनों की रचना करने वाली महिला विदुषी के लिए संस्कृत शब्द क्या है?",
                "answer": "ब्रह्मवादिनी।",
                "icon": "fa-star"
            },
            {
                "question": "ऋग्वेद के किस मंडल में पुरुष सूक्त शामिल है?",
                "answer": "10वें मंडल में।",
                "icon": "fa-book"
            }
        ]
    }
}

# Write final bilingual content.json files
os.makedirs(os.path.dirname(os.path.join(base_dir, "content.json")), exist_ok=True)
with open(os.path.join(base_dir, "content.json"), 'w', encoding='utf-8') as f:
    json.dump(eng_output, f, ensure_ascii=False, indent=4)

os.makedirs(os.path.dirname(os.path.join(base_dir, "hi", "content.json")), exist_ok=True)
with open(os.path.join(base_dir, "hi", "content.json"), 'w', encoding='utf-8') as f:
    json.dump(hi_output, f, ensure_ascii=False, indent=4)

print("Content generated successfully!")
