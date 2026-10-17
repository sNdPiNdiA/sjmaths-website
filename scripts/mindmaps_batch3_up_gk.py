# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 9: Festivals of Uttar Pradesh
# ==============================================================================
mm_festivals = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Festivals &amp; Fairs of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के प्रमुख त्यौहार, मेले एवं लोकोत्सव</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • 2,250+ Fairs &amp; Mathura Rank 1 • Maha Kumbh &amp; Dev Deepawali • Unique Holi Traditions (Lathmar &amp; Masan) • Tourism Mahotsavs (Taj, Lucknow, Ganga) • Historic Melas Directory • Sacred Parikramas</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • 2,250+ मेले व मथुरा प्रथम • महाकुंभ व देव दीपावली • अनूठी होली परंपराएं (लठमार व मसान) • पर्यटन महोत्सव (ताज, लखनऊ, गंगा) • ऐतिहासिक मेलों की निर्देशिका • पावन परिक्रमा उत्सव</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-sparkles"></i>
            <span class="lang-en">Festival Heritage, Sacred Congregations &amp; Fairs of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की पावन उत्सव परंपरा, महामेले एवं सांस्कृतिक समारोह</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Fairs Overview & District Rankings -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tent" style="color: #059669;"></i>
                    <span class="lang-en">1. Fairs Overview &amp; Rankings</span>
                    <span class="lang-hi">1. मेलों का परिदृश्य एवं जिला रैंकिंग</span>
                </h4>
                <span class="mindmap-node-tag">2,250+ Annual Melas</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trophy"></i>
                        <span class="lang-en">District-wise Frequency of Fairs</span>
                        <span class="lang-hi">मेलों की संख्या में जिलावार आंकड़े</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Rank 1 (Max Fairs):</strong> Mathura (86 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 2:</strong> Kanpur (80 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 3:</strong> Hamirpur (79 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 4:</strong> Jhansi (78 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 5:</strong> Prayagraj (77 Fairs)</span>
                        <span class="mindmap-chip"><strong>Rank 6:</strong> Fatehpur (70 Fairs)</span>
                        <span class="mindmap-chip"><strong>Lowest Fairs:</strong> Pilibhit (पीलीभीत - सबसे कम मेले)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-landmark"></i>
                        <span class="lang-en">Socio-Economic Dimensions of Melas</span>
                        <span class="lang-hi">मेलों के सामाजिक व आर्थिक आयाम</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rural Exchange Hubs:</strong> UP hosts over <strong>2,250 fairs annually</strong>. They act as rural commercial marts for agricultural tools, indigenous crafts, cattle trade, and cultural preservation.</span>
                            <span class="lang-hi"><strong>ग्रामीण विनिमय केंद्र:</strong> उप्र में प्रतिवर्ष <strong>2,250 से अधिक मेले</strong> आयोजित होते हैं, जो कृषि यंत्रों, हस्तशिल्प, पशु व्यापार व लोककला के केंद्र हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Mathura hosts the highest number of annual fairs (86), while Pilibhit hosts the fewest in Uttar Pradesh!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सर्वाधिक मेले मथुरा जिले (86) में तथा सबसे कम मेले पीलीभीत जिले में लगते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Spiritual Peaks: Maha Kumbh, Dev Deepawali & Deepotsav -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-om" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Spiritual Mega-Congregations</span>
                    <span class="lang-hi">2. आध्यात्मिक महाकुंभ, देव दीपावली व दीपोत्सव</span>
                </h4>
                <span class="mindmap-node-tag">UNESCO Intangible Heritage</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water"></i>
                        <span class="lang-en">Prayagraj Kumbh &amp; Magh Mela</span>
                        <span class="lang-hi">प्रयागराज कुंभ एवं माघ मेला</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Maha Kumbh (Prayagraj):</strong> Held every <strong>12 years</strong> at the Triveni Sangam (Ganga, Yamuna &amp; mythical Saraswati); <strong>Ardha Kumbh</strong> every 6 years; annual <strong>Magh Mela</strong>. Inscribed on the <strong>UNESCO Representative List of Intangible Cultural Heritage (2017)</strong> as the world's largest peaceful congregation.</span>
                            <span class="lang-hi"><strong>महाकुंभ (प्रयागराज):</strong> त्रिवेणी संगम पर हर <strong>12 वर्ष</strong> में महाकुंभ व 6 वर्ष में अर्धकुंभ; प्रतिवर्ष <strong>माघ मेला</strong>। 2017 में <strong>यूनेस्को की अमूर्त सांस्कृतिक विरासत</strong> में शामिल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dev Deepawali (Varanasi):</strong> Celebrated on Kartik Purnima (15 days after Diwali) along all 84 ghats of Varanasi; millions of earthen diyas lit to celebrate Lord Shiva's victory over demon Tripurasura (Tripurari Purnima).</span>
                            <span class="lang-hi"><strong>देव दीपावली (वाराणसी):</strong> कार्तिक पूर्णिमा पर 84 गंगा घाटों पर लाखों दीयों का प्रज्ज्वलन; त्रिपुरारी पूर्णिमा के रूप में देवताओं का गंगा अवतरण पर्व।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ayodhya Deepotsav:</strong> Annual grand festival celebrated on Chhoti Diwali eve at Ram ki Paidi on River Saryu; creates Guinness World Records by lighting over 22–25 lakh indigenous earthen lamps.</span>
                            <span class="lang-hi"><strong>अयोध्या दीपोत्सव:</strong> छोटी दीपावली पर सरयू तट (राम की पैड़ी) पर 22 से 25 लाख दीप प्रज्ज्वलित कर गिनीज बुक वर्ल्ड रिकॉर्ड।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kumbh Mela was inscribed on UNESCO's Intangible Cultural Heritage list in 2017. Dev Deepawali is celebrated on Kartik Purnima in Varanasi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कुंभ मेले को 2017 में यूनेस्को अमूर्त सांस्कृतिक धरोहर सूची में शामिल किया गया। देव दीपावली कार्तिक पूर्णिमा को वाराणसी में मनाई जाती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Unique Regional Holi Celebrations -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-brush" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Unique Holi Celebrations</span>
                    <span class="lang-hi">3. उत्तर प्रदेश की अनूठी होली परंपराएं</span>
                </h4>
                <span class="mindmap-node-tag">Lathmar • Masan • Laddu Holi</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-palette"></i>
                        <span class="lang-en">Braj &amp; Kashi Distinctive Holi Forms</span>
                        <span class="lang-hi">ब्रज एवं काशी की विशिष्ट होली शैलियाँ</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Lathmar Holi:</strong> Barsana &amp; Nandgaon (women strike men with lathis)</span>
                        <span class="mindmap-chip"><strong>Laddu Holi:</strong> Shriji Temple, Barsana (sweets showered)</span>
                        <span class="mindmap-chip"><strong>Phoolon ki Holi:</strong> Banke Bihari Temple, Vrindavan (flowers)</span>
                        <span class="mindmap-chip"><strong>Chhadimar Holi:</strong> Gokul (women use small sticks)</span>
                        <span class="mindmap-chip"><strong>Huranga:</strong> Dauji Temple, Mathura (cloth-tearing tradition)</span>
                        <span class="mindmap-chip"><strong>Bhasma / Masan Holi:</strong> Manikarnika Ghat, Varanasi (cremation pyre ash)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-fire"></i>
                        <span class="lang-en">Cultural Signatures</span>
                        <span class="lang-hi">सांस्कृतिक महत्व</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lathmar Holi:</strong> Gops of Nandgaon visit Radha's village Barsana; Gopis playfully beat their shields with wooden staffs (lathis) to the cadence of Dhamar and Rasiya singing.</span>
                            <span class="lang-hi"><strong>लठमार होली:</strong> नंदगांव के हुरियारों पर बरसाना की गोपियां लाठियां बरसाती हैं; ढालों से बचाव व रसिया गायन की अद्भुत परंपरा।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Masan ki Holi (Varanasi):</strong> Played at Manikarnika Ghat on Rangbhari Ekadashi where Shiva devotees play with funeral pyre ashes (Chita Bhasma) welcoming Baba Vishwanath.</span>
                            <span class="lang-hi"><strong>मसान की होली (काशी):</strong> रंगभरी एकादशी के अगले दिन मणिकर्णिका घाट पर चिता भस्म से खेली जाने वाली अड़भंगी शिव होली।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Lathmar Holi is played in Barsana and Nandgaon. Masan Bhasma Holi is celebrated at Manikarnika Ghat in Varanasi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> लठमार होली बरसाना व नंदगांव में खेली जाती है। मसान की भस्म होली वाराणसी के मणिकर्णिका घाट पर खेली जाती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Major State Tourism Mahotsavs -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-crown" style="color: #d97706;"></i>
                    <span class="lang-en">4. State Tourism Mahotsavs</span>
                    <span class="lang-hi">4. प्रमुख राज्य पर्यटन महोत्सव</span>
                </h4>
                <span class="mindmap-node-tag">Taj • Lucknow • Ganga • Kabir</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-calendar-days"></i>
                        <span class="lang-en">Annual Government Cultural Festivals</span>
                        <span class="lang-hi">वार्षिक सरकारी सांस्कृतिक महोत्सव</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Taj Mahotsav:</strong> Shilpgram, Agra (18–27 Feb, Crafts &amp; Cuisine)</span>
                        <span class="mindmap-chip"><strong>Lucknow Mahotsav:</strong> Lucknow (Nov–Dec, Awadhi Culture &amp; Ghazal)</span>
                        <span class="mindmap-chip"><strong>Ganga Mahotsav:</strong> Varanasi (Kartik Purnima, Classical Music)</span>
                        <span class="mindmap-chip"><strong>Jhansi Mahotsav:</strong> Jhansi (Ayurveda Festival &amp; Fort Pageant)</span>
                        <span class="mindmap-chip"><strong>Kannauj Mahotsav:</strong> Kannauj (Perfumery &amp; Attar Traditions)</span>
                        <span class="mindmap-chip"><strong>Maghar Mahotsav:</strong> Sant Kabir Nagar (Jan, Kabir Samadhi)</span>
                        <span class="mindmap-chip"><strong>Kampil Mahotsav:</strong> Farrukhabad (Jain Culture &amp; Heritage)</span>
                        <span class="mindmap-chip"><strong>Kalinjar Mahotsav:</strong> Banda (Chandela Martial Heritage)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Taj Mahotsav is celebrated annually from 18 to 27 February at Shilpgram, Agra. Maghar Mahotsav honors Sant Kabir!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ताज महोत्सव प्रतिवर्ष 18 से 27 फरवरी तक शिल्पग्राम, आगरा में मनाया जाता है। मगहर महोत्सव संत कबीर की स्मृति में होता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Historic Melas Directory of UP -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-map-pin" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Historic Melas Directory</span>
                    <span class="lang-hi">5. ऐतिहासिक मेलों की संपूर्ण निर्देशिका</span>
                </h4>
                <span class="mindmap-node-tag">District-Specific Fairs</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-list"></i>
                        <span class="lang-en">High-Frequency Exam Fairs</span>
                        <span class="lang-hi">परीक्षाओं में सर्वाधिक पूछे जाने वाले मेले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bateshwar Mela (Agra):</strong> Historic animal fair on Yamuna bank at Bateshwar with 101 Shiva temples; revered as UP's largest cattle trade fair.</span>
                            <span class="lang-hi"><strong>बटेश्वर मेला (आगरा):</strong> 101 शिव मंदिरों वाले बटेश्वर में यमुना तट पर लगने वाला राज्य का सबसे बड़ा पशु/ऊंट मेला।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Nauchandi Mela (Meerut):</strong> Communal harmony fair held on the 2nd Sunday after Holi; devotees visit Nauchandi Devi temple &amp; Bale Mian Dargah.</span>
                            <span class="lang-hi"><strong>नौचंदी मेला (मेरठ):</strong> होली के बाद सांप्रदायिक सौहार्द का प्रतीक मेला (नवचंडी देवी व बाले मियां दरगाह)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Deva Sharif &amp; Syed Salar:</strong> <em>Deva Sharif (Barabanki)</em> at tomb of Haji Waris Ali Shah; <em>Syed Salar Masood Ghazi (Bahraich)</em> annual historic Urs.</span>
                            <span class="lang-hi"><strong>देवा शरीफ व सैयद सालार:</strong> <em>देवा शरीफ (बाराबंकी)</em> हाजी वारिस अली शाह की दरगाह पर; <em>सैयद सालार मसूद गाजी (बहराइच)</em> ऐतिहासिक मेला।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Shakumbhari Devi &amp; Govind Sahib:</strong> <em>Shakumbhari Devi (Saharanpur)</em> Navratri fair; <em>Govind Sahib (Ambedkar Nagar)</em> famous Khichdi offering fair.</span>
                            <span class="lang-hi"><strong>शाकुंभरी व गोविंद साहब:</strong> <em>शाकुंभरी देवी (सहारनपुर)</em> का मेला; <em>गोविंद साहब (अंबेडकर नगर)</em> खिचड़ी चढ़ाने वाला प्रसिद्ध मेला।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Match-the-column: Bateshwar (Agra), Nauchandi (Meerut), Deva Sharif (Barabanki), Shakumbhari Devi (Saharanpur), Govind Sahib (Ambedkar Nagar)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बटेश्वर (आगरा), नौचंदी (मेरठ), देवा शरीफ (बाराबंकी), शाकुंभरी देवी (सहारनपुर) और गोविंद साहब (अंबेडकर नगर) का मिलान अनिवार्य प्रश्न है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Sacred Parikrama Fairs & Circuit Pilgrimages -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-person-walking-arrow-right" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Sacred Parikrama Melas</span>
                    <span class="lang-hi">6. पावन परिक्रमा मेले एवं तीर्थ यात्राएं</span>
                </h4>
                <span class="mindmap-node-tag">84-Kosi • Naimisharanya • Ayodhya</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-arrows-spin"></i>
                        <span class="lang-en">Major Parikramas in Uttar Pradesh</span>
                        <span class="lang-hi">उत्तर प्रदेश की प्रमुख परिक्रमा यात्राएं</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>84-Kosi Parikrama:</strong> Naimisharanya (Sitapur - 88,000 rishis penance land)</span>
                        <span class="mindmap-chip"><strong>Ayodhya Parikramas:</strong> 84-Kosi, 14-Kosi (Chaudah Kosi), 5-Kosi (Panch Kosi)</span>
                        <span class="mindmap-chip"><strong>Govardhan Parikrama:</strong> Mathura (21 km circuit around sacred hill)</span>
                        <span class="mindmap-chip"><strong>Chitrakoot Parikrama:</strong> Kamadgiri Mountain circumambulation (5 km)</span>
                        <span class="mindmap-chip"><strong>Panchkroshi Parikrama:</strong> Varanasi (sacred circumambulation of Kashi)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-tree"></i>
                        <span class="lang-en">Naimisharanya &amp; Kamadgiri Spiritual Footprint</span>
                        <span class="lang-hi">नैमिषारण्य एवं कामदगिरि का महत्व</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Naimisharanya (Sitapur):</strong> Ancient Vedic pilgrimage where sage Suta recited Puranas to 88,000 sages; home to Chakra Tirtha, Lalita Devi Temple, and annual 84-Kosi Parikrama in Phalguna month.</span>
                            <span class="lang-hi"><strong>नैमिषारण्य (सीतापुर):</strong> 88,000 ऋषियों की तपोभूमि; चक्रतीर्थ, ललिता देवी मंदिर; फाल्गुन माह में 84-कोसी परिक्रमा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Naimisharanya (Sitapur) is famous for its 84-Kosi Parikrama and Chakra Tirtha. Kamadgiri Parikrama is held in Chitrakoot!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नैमिषारण्य (सीतापुर) 84-कोसी परिक्रमा और चक्रतीर्थ के लिए प्रसिद्ध है। कामदगिरि परिक्रमा चित्रकूट में आयोजित होती है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 10: Folk Dances of Uttar Pradesh
# ==============================================================================
mm_folk_dances = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Folk Dances of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के लोक नृत्य एवं शास्त्रीय कत्थक</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Classical Kathak Heritage • Braj Folk Dances (Charkula, Mayur, Ras) • Bundelkhand Martial &amp; Festive Dances (Rai, Pai Danda) • Purvanchal Traditional Dances (Dhobia, Natwari) • Awadh &amp; Doab Styles • Sonbhadra Tribal Dances (Karma)</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • शास्त्रीय कत्थक विरासत • ब्रज के लोक नृत्य (चरकुला, मयूर, रास) • बुंदेलखंड के नृत्य (राई, पाई डंडा, जवारा) • पूर्वांचल के नृत्य (धोबिया, नटवरी) • अवध व दोआब शैलियाँ • सोनभद्र के जनजातीय नृत्य (कर्मा)</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-person-walking"></i>
            <span class="lang-en">Rhythmic Heritage &amp; Traditional Dance Treasures of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की समृद्ध नृत्य धरोहर, लोक ताल एवं जनजातीय अभिव्यक्तियां</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Classical Kathak Heritage -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-drum" style="color: #059669;"></i>
                    <span class="lang-en">1. Classical Kathak Heritage</span>
                    <span class="lang-hi">1. शास्त्रीय कत्थक परंपरा</span>
                </h4>
                <span class="mindmap-node-tag">Sole North Indian Classical Dance</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-feather"></i>
                        <span class="lang-en">Origins, Royal Patronage &amp; Gharanas</span>
                        <span class="lang-hi">उत्पत्ति, दरबारी संरक्षण एवं घराने</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Temple to Court Evolution:</strong> Originated from Brahmin temple storytellers (Kathakas). Transformed into classical stage art under <strong>Nawab Wajid Ali Shah ('Akhtarpiya')</strong> in Awadh court (composed Rahas dance-dramas).</span>
                            <span class="lang-hi"><strong>मंदिर से राजदरबार तक:</strong> मंदिर के कथाकारों से विकसित। अवध के नवाब <strong>वाजिद अली शाह ('अख्तरपिया')</strong> के दरबार में शास्त्रीय रूप मिला (रहस नृत्य नाटिका)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow Kathak Lineage:</strong> Founded by Ishwari Prasad. Great masters: Kalka-Bindadin Maharaj, Achchan Maharaj, Shambhu Maharaj, Lachhu Maharaj, and Padma Vibhushan <strong>Pandit Birju Maharaj</strong>. Hallmarks: <em>Nazakat</em> (grace), <em>Bhav</em> (expression), and subtle Thumri abhinaya.</span>
                            <span class="lang-hi"><strong>लखनऊ घराना:</strong> ईश्वरी प्रसाद द्वारा प्रवर्तित। कालका-बिंदादीन, अच्छन, शंभू, लच्छू व <strong>पं. बिरजू महाराज</strong>। नजाकत, भाव-अभिनय व ठुमरी पर विशेष बल।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Kathak is the only classical dance form of North India/Uttar Pradesh. The state institute is the National Kathak Sansthan in Lucknow!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कत्थक उत्तर प्रदेश/उत्तर भारत का एकमात्र शास्त्रीय नृत्य है। राष्ट्रीय कत्थक संस्थान लखनऊ में स्थित है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Braj Region Folk Dances: Charkula, Mayur & Ras -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-wheelchair" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Braj Region Folk Dances</span>
                    <span class="lang-hi">2. ब्रज क्षेत्र के लोक नृत्य</span>
                </h4>
                <span class="mindmap-node-tag">Charkula (108 Lamps) • Mayur • Ras</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-fire"></i>
                        <span class="lang-en">Charkula Dance (चरकुला नृत्य)</span>
                        <span class="lang-hi">चरकुला नृत्य की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>The 108 Deepaks Balance:</strong> The most celebrated folk dance of Braj (Mathura/Barsana). Female dancers balance a multi-tiered wooden pyramidal structure (charkula) containing <strong>108 burning oil lamps</strong> on their head, dancing gracefully to the rhythm of Rasiya songs celebrating Radha's birth.</span>
                            <span class="lang-hi"><strong>108 दीपकों का संतुलन:</strong> ब्रज का सर्वाधिक प्रसिद्ध लोकनृत्य। महिलाएं सिर पर 4-5 मंजिला लकड़ी का पहिया (चरकुला) रखकर, जिसमें <strong>108 जलते हुए दीपक</strong> होते हैं, रसिया की धुन पर नृत्य करती हैं (राधा जी के जन्मोत्सव का प्रतीक)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-dove"></i>
                        <span class="lang-en">Other Major Braj Dances</span>
                        <span class="lang-hi">ब्रज के अन्य प्रमुख नृत्य</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Mayur Dance (मयूर नृत्य):</strong> Dancers dress in peacock feathers mimicking peacock courting</span>
                        <span class="mindmap-chip"><strong>Raslila Dance:</strong> Enacts eternal love of Radha-Krishna with Gopis</span>
                        <span class="mindmap-chip"><strong>Jhula Dance:</strong> Performed in monsoon month of Shravan in temples</span>
                        <span class="mindmap-chip"><strong>Ghada Dance:</strong> Dancers balance water pots (ghadas) on head</span>
                        <span class="mindmap-chip"><strong>Huranga:</strong> Post-Holi rustic festive dance at Dauji (Mathura)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> In Charkula dance, female performers balance 108 oil lamps on a wooden pyramid on their head. It is exclusive to the Braj region!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> चरकुला नृत्य में महिलाएं सिर पर 108 जलते दीपक रखकर नृत्य करती हैं। यह ब्रज क्षेत्र का विशिष्ट लोक नृत्य है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Bundelkhand Region Folk Dances: Rai, Pai Danda & Jawara -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Bundelkhand Folk Dances</span>
                    <span class="lang-hi">3. बुंदेलखंड के लोक नृत्य</span>
                </h4>
                <span class="mindmap-node-tag">Rai • Pai Danda • Jawara</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-wand-magic-sparkles"></i>
                        <span class="lang-en">Rai Dance (राई नृत्य) &amp; Swang</span>
                        <span class="lang-hi">राई नृत्य एवं स्वांग</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rai Dance (राई):</strong> The premier folk dance of Bundelkhand performed by women on Krishna Janmashtami, births and auspicious ceremonies; involves rapid spins to the beat of Mridanga/Dholak.</span>
                            <span class="lang-hi"><strong>राई नृत्य:</strong> बुंदेलखंड का सबसे प्रसिद्ध लोक नृत्य; श्रीकृष्ण जन्माष्टमी, पुत्र जन्मोत्सव व विवाह पर महिलाओं द्वारा तीव्र गति के घुमावों (चक्करों) के साथ प्रस्तुत।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-lines-leaning"></i>
                        <span class="lang-en">Pai Danda, Jawara &amp; Martial Styles</span>
                        <span class="lang-hi">पाई डंडा, जवारा एवं अन्य नृत्य</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Pai Danda (पाई डंडा):</strong> Martial stick dance by Ahir community; 'Dandiya of Bundelkhand'</span>
                        <span class="mindmap-chip"><strong>Diwari Dance:</strong> Performed with colorful lathis during Diwali</span>
                        <span class="mindmap-chip"><strong>Jawara Dance:</strong> Harvest dance balancing baskets of green barley sprouts</span>
                        <span class="mindmap-chip"><strong>Badhaiya Dance:</strong> Performed on childbirth to congratulate parents</span>
                        <span class="mindmap-chip"><strong>Ghodha Dance:</strong> Trained horses dance to rhythmic beats at weddings</span>
                        <span class="mindmap-chip"><strong>Kartik Dance:</strong> Devotional dance during Kartik month (Gopis-Krishna)</span>
                        <span class="mindmap-chip"><strong>Naurata Dance:</strong> Performed by unmarried girls during Navratri</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Rai dance, Pai Danda (stick dance of Ahirs), and Jawara are quintessential folk dances of Bundelkhand!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> राई नृत्य, पाई डंडा (अहीरों का लाठी नृत्य), और जवारा बुंदेलखंड के सबसे प्रमुख लोक नृत्य हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Purvanchal Traditional Dances: Dhobia, Natwari & Dheewar -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-drum-steelpan" style="color: #d97706;"></i>
                    <span class="lang-en">4. Purvanchal Folk Dances</span>
                    <span class="lang-hi">4. पूर्वांचल के पारंपरिक लोक नृत्य</span>
                </h4>
                <span class="mindmap-node-tag">Dhobia • Natwari • Dheewar</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-vest"></i>
                        <span class="lang-en">Community Folk Dances</span>
                        <span class="lang-hi">जातीय समुदाय आधारित लोक नृत्य</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dhobia Dance (धोबिया नृत्य):</strong> Most famous folk dance of Eastern UP / Bhojpuri belt, performed by the Dhobi (washerman) community at weddings and births; enacts comic and emotional bond between washerman and donkey.</span>
                            <span class="lang-hi"><strong>धोबिया नृत्य:</strong> पूर्वांचल/भोजपुरी क्षेत्र में धोबी समुदाय द्वारा विवाह व मांगलिक अवसरों पर प्रस्तुत; धोबी व गधे के आत्मीय संबंधों का हास्यपूर्ण मंचन।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Natwari Dance (नटवरी नृत्य):</strong> Practiced by Ahir / Yadav community of Purvanchal; rhythmic footwork dedicated to Lord Krishna (Natwar), accompanied by Nakara and Pakhawaj.</span>
                            <span class="lang-hi"><strong>नटवरी नृत्य:</strong> पूर्वांचल के अहीर/यादव समुदाय द्वारा भगवान श्रीकृष्ण (नटवर) की स्मृति में नक्कारे व पखावज की थाप पर किया जाने वाला नृत्य।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dheewar / Kaharwa Dance:</strong> Performed by Kahar community at weddings to express joy and blessing for the bride.</span>
                            <span class="lang-hi"><strong>धीवर / कहरवा नृत्य:</strong> कहार जाति द्वारा मांगलिक अवसरों पर किया जाने वाला उल्लासपूर्ण नृत्य।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Dhobia dance and Natwari dance are native to Purvanchal (Eastern Uttar Pradesh)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> धोबिया नृत्य और नटवरी नृत्य पूर्वांचल (पूर्वी उत्तर प्रदेश) के प्रमुख पारंपरिक लोक नृत्य हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Awadh & Doab Regional Performing Traditions -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-theater-masks" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Awadh &amp; Doab Folk Dances</span>
                    <span class="lang-hi">5. अवध एवं दोआब के लोक नृत्य</span>
                </h4>
                <span class="mindmap-node-tag">Jogini • Dhedhiya • Kalabazi</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-masks-theater"></i>
                        <span class="lang-en">Festive &amp; Theatrical Dances of Awadh</span>
                        <span class="lang-hi">अवध के उत्सव एवं स्वांग नृत्य</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Jogini Dance (जोगिनी):</strong> Performed on Ram Navami in Awadh (males dress as females)</span>
                        <span class="mindmap-chip"><strong>Dhedhiya Dance (ढेढ़िया):</strong> Performed in Doab/Awadh during Dussehra with pierced earthen lamps</span>
                        <span class="mindmap-chip"><strong>Kalabazi Dance:</strong> Dancers balance on dummy horse performing acrobatic feats</span>
                        <span class="mindmap-chip"><strong>Chholiya Dance:</strong> Martial Rajput dance with swords and shields (border regions)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield-halved"></i>
                        <span class="lang-en">Dhedhiya &amp; Jogini Significance</span>
                        <span class="lang-hi">ढेढ़िया व जोगिनी नृत्य का महत्व</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dhedhiya:</strong> Commemorates Lord Rama's triumphant return to Ayodhya after slaying Ravana; dancers carry pierced clay pitchers with lighted earthen lamps on their heads.</span>
                            <span class="lang-hi"><strong>ढेढ़िया:</strong> रावण वध के बाद भगवान राम के अयोध्या आगमन पर सिर पर छिद्रयुक्त मिट्टी के घड़े में जलता दीप रखकर किया जाता है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Jogini dance is performed on Ram Navami in Awadh by male dancers disguised as females!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> जोगिनी नृत्य अवध क्षेत्र में रामनवमी के पावन अवसर पर पुरुषों द्वारा स्त्री रूप धारण कर किया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Sonbhadra & Mirzapur Tribal Dances -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tree" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Tribal Dances (Sonbhadra)</span>
                    <span class="lang-hi">6. सोनभद्र व मिर्जापुर के जनजातीय नृत्य</span>
                </h4>
                <span class="mindmap-node-tag">Karma • Shila • Tharu Badhaiya</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-people-arrows"></i>
                        <span class="lang-en">Karma &amp; Shila Tribal Dances</span>
                        <span class="lang-hi">कर्मा एवं शीला जनजातीय नृत्य</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Karma Dance (कर्मा नृत्य):</strong> The signature tribal folk dance of Sonbhadra and Mirzapur districts, practiced by Kharwar, Gond, Baiga, and Kol tribes; performed during Karma festival in autumn invoking blessings of deity Karam / Karma tree for fertility and good harvest.</span>
                            <span class="lang-hi"><strong>कर्मा नृत्य:</strong> सोनभद्र व मिर्जापुर की खरवार, गोंड, बैगा व कोल जनजातियों का प्रमुख नृत्य; भाद्रपद में कर्म वृक्ष की पूजा व अच्छी फसल की कामना हेतु वृत्ताकार समूह में प्रस्तुत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Shila / Saila &amp; Tharu Dances:</strong> <em>Saila</em> is danced with small wooden sticks by tribal youth; <em>Tharu Badhaiya</em> is performed in the Tarai belt to celebrate child births.</span>
                            <span class="lang-hi"><strong>शीला/सैला व थारू नृत्य:</strong> डंडों के साथ प्रस्तुत <em>सैला नृत्य</em> तथा तराई क्षेत्र की थारू जनजाति द्वारा जन्मोत्सव पर <em>बधैया नृत्य</em>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Karma dance belongs to the Kharwar, Baiga, and Gond tribes of Sonbhadra and Mirzapur districts!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> कर्मा नृत्य सोनभद्र एवं मिर्जापुर जिलों की खरवार, बैगा व गोंड जनजातियों द्वारा किया जाता है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 11: Forests of Uttar Pradesh
# ==============================================================================
mm_forests = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Forests &amp; Forestry of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के वन, वानिकी एवं पर्यावरणीय संपदा</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • ISFR 2021 Definitive Statistics • District Rankings (Sonbhadra vs Bhadohi) • 3 Major Forest Types • Forest Products &amp; Industries • State Symbols (Ashoka &amp; Palash) • Social Forestry &amp; Policy Target</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • ISFR 2021 वन स्थिति रिपोर्ट • जिलावार रैंकिंग (सोनभद्र बनाम भदोही) • 3 प्रमुख वन प्रकार • वनोपज एवं उद्योग • राज्य प्रतीक (अशोक व पलाश) • सामाजिक वानिकी व नीति लक्ष्य</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-tree"></i>
            <span class="lang-en">Forest Wealth, Ecological Cover &amp; State Symbols of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की वन संपदा, पारिस्थितिक आवरण एवं वानिकी नीतियां</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: ISFR 2021 Definitive Forest Statistics -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-chart-pie" style="color: #059669;"></i>
                    <span class="lang-en">1. ISFR 2021 Definitive Data</span>
                    <span class="lang-hi">1. ISFR 2021 वन स्थिति रिपोर्ट आंकड़े</span>
                </h4>
                <span class="mindmap-node-tag">Forest Cover: 6.15% • Total: 9.23%</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-square-poll-vertical"></i>
                        <span class="lang-en">Core Forest Cover &amp; Tree Cover Metrics</span>
                        <span class="lang-hi">वन आवरण एवं वृक्षावरण के आधिकारिक आंकड़े</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Total State Area:</strong> 2,40,928 sq km</span>
                        <span class="mindmap-chip"><strong>Recorded Forest Cover:</strong> 14,817.89 sq km (6.15%)</span>
                        <span class="mindmap-chip"><strong>Tree Cover (वृक्षावरण):</strong> 7,421 sq km (3.08%)</span>
                        <span class="mindmap-chip"><strong>Total Forest &amp; Tree Cover:</strong> 22,238.89 sq km (9.23%)</span>
                        <span class="mindmap-chip"><strong>Net Increase (ISFR 2019 to 2021):</strong> +12.24 sq km</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Forest Density Classification</span>
                        <span class="lang-hi">वन घनत्व के आधार पर वर्गीकरण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Very Dense Forest (VDF - Canopy >70%):</strong> 2,626.65 sq km (1.09% of total area).</span>
                            <span class="lang-hi"><strong>अत्यंत सघन वन (VDF):</strong> 2,626.65 वर्ग किमी (राज्य का 1.09%)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Moderately Dense Forest (MDF - Canopy 40-70%):</strong> 4,029.29 sq km (1.67%).</span>
                            <span class="lang-hi"><strong>मध्यम सघन वन (MDF):</strong> 4,029.29 वर्ग किमी (1.67%)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Open Forest (OF - Canopy 10-40%):</strong> 8,161.95 sq km (3.39% - largest component).</span>
                            <span class="lang-hi"><strong>खुले वन (OF):</strong> 8,161.95 वर्ग किमी (3.39% - सबसे बड़ा भाग)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Under ISFR 2021, UP has 6.15% Forest Cover and 3.08% Tree Cover, totaling 9.23% combined green cover!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> ISFR 2021 के अनुसार उप्र में वन आवरण 6.15% तथा वृक्षावरण 3.08% है, कुल हरित आवरण 9.23% है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: District Rankings by Forest Cover -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-ranking-star" style="color: #0284c7;"></i>
                    <span class="lang-en">2. District Rankings (Forests)</span>
                    <span class="lang-hi">2. जिलावार वन आवरण रैंकिंग</span>
                </h4>
                <span class="mindmap-node-tag">Sonbhadra #1 • Bhadohi Lowest</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-arrow-trend-up"></i>
                        <span class="lang-en">Top Districts by Forest Area &amp; Percentage</span>
                        <span class="lang-hi">सर्वाधिक वन क्षेत्र व प्रतिशत वाले जिले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Highest Forest Area (sq km):</strong> 1. <strong>Sonbhadra</strong> (2,436.75 sq km); 2. <strong>Lakhimpur Kheri</strong> (1,272.56 sq km); 3. <strong>Mirzapur</strong> (803.73 sq km); 4. <strong>Pilibhit</strong> (687.11 sq km).</span>
                            <span class="lang-hi"><strong>सर्वाधिक वन क्षेत्रफल वाले जिले:</strong> 1. <strong>सोनभद्र</strong> (2,436.75 वर्ग किमी); 2. <strong>लखीमपुर खीरी</strong> (1,272.56 वर्ग किमी); 3. <strong>मिर्जापुर</strong> (803.73 वर्ग किमी); 4. <strong>पीलीभीत</strong> (687.11 वर्ग किमी)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Highest Forest Percentage (%):</strong> 1. <strong>Sonbhadra</strong> (35.24%); 2. <strong>Chandauli</strong> (21.78%); 3. <strong>Pilibhit</strong> (18.60%); 4. <strong>Mirzapur</strong> (18.25%); 5. <strong>Chitrakoot</strong> (17.30%).</span>
                            <span class="lang-hi"><strong>सर्वाधिक वन प्रतिशत वाले जिले:</strong> 1. <strong>सोनभद्र</strong> (35.24%); 2. <strong>चंदौली</strong> (21.78%); 3. <strong>पीलीभीत</strong> (18.60%); 4. <strong>मिर्जापुर</strong> (18.25%); 5. <strong>चित्रकूट</strong> (17.30%)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-arrow-trend-down"></i>
                        <span class="lang-en">Lowest Forest Area &amp; Percentage</span>
                        <span class="lang-hi">न्यूनतम वन क्षेत्र व प्रतिशत वाले जिले</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lowest Forest Area &amp; Percentage:</strong> <strong>Bhadohi (Sant Ravidas Nagar)</strong> has both the lowest forest area (<strong>3.71 sq km</strong>) and lowest forest percentage (<strong>0.37%</strong>), followed by Mainpuri (0.49%) and Deoria (0.60%).</span>
                            <span class="lang-hi"><strong>न्यूनतम वन आवरण:</strong> <strong>भदोही (संत रविदास नगर)</strong> में न्यूनतम क्षेत्रफल (<strong>3.71 वर्ग किमी</strong>) और न्यूनतम प्रतिशत (<strong>0.37%</strong>) दोनों हैं, जिसके बाद मैनपुरी और देवरिया आते हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sonbhadra has the highest forest cover (area &amp; 35.24%), while Bhadohi has the lowest (3.71 sq km / 0.37%). Repeated in every exam!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सोनभद्र में सर्वाधिक वन (क्षेत्रफल व 35.24%) तथा भदोही में सबसे कम वन (3.71 वर्ग किमी / 0.37%) हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Three Major Forest Types of UP -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tree-city" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Three Major Forest Types</span>
                    <span class="lang-hi">3. उत्तर प्रदेश के 3 प्रमुख वन प्रकार</span>
                </h4>
                <span class="mindmap-node-tag">Champion &amp; Seth Classification</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-leaf"></i>
                        <span class="lang-en">Vegetation Zones &amp; Dominant Species</span>
                        <span class="lang-hi">वनस्पतिक क्षेत्र एवं प्रमुख वृक्ष प्रजातियां</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1. Tropical Moist Deciduous (उष्णकटिबंधीय नम पर्णपाती):</strong> Found in Bhabhar &amp; Tarai belt (rainfall 100–150 cm). Dominant species: <strong>Sal (Shorea robusta)</strong>, Teak, Shisham, Semal, Mahua, Bamboo, Cane.</span>
                            <span class="lang-hi"><strong>1. उष्णकटिबंधीय नम पर्णपाती वन:</strong> भाबर व तराई क्षेत्र (100-150 सेमी वर्षा); मुख्य वृक्ष: <strong>साल (साखू)</strong>, सागौन, शीशम, सेमल, महुआ, बांस, बेंत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2. Tropical Dry Deciduous (उष्णकटिबंधीय शुष्क पर्णपाती):</strong> Covers the vast central Gangetic plain (rainfall 75–100 cm). Dominant species: Sal, Teak, Neem, Peepal, Banyan, Bel, Amaltas, and <strong>Palash (Dhak)</strong>.</span>
                            <span class="lang-hi"><strong>2. उष्णकटिबंधीय शुष्क पर्णपाती वन:</strong> विशाल मैदानी भाग (75-100 सेमी वर्षा); मुख्य वृक्ष: साल, सागौन, नीम, पीपल, बरगद, बेल, अमलतास व <strong>पलाश (ढाक)</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3. Tropical Thorny Forests (उष्णकटिबंधीय कंटीले वन):</strong> Found in South-Western semi-arid belt and Bundelkhand (Agra, Mathura, Jhansi; rainfall <75 cm). Dominant species: Acacia (Babool), Khair, Kikar, Ber, Cactus.</span>
                            <span class="lang-hi"><strong>3. उष्णकटिबंधीय कंटीले वन:</strong> दक्षिण-पश्चिमी शुष्क भाग व बुंदेलखंड (आगरा, मथुरा, झांसी; <75 सेमी वर्षा); बबूल, खैर, कीकर, बेर, कैक्टस।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Sal (साखू) is the most valuable commercial timber tree of the Tarai moist deciduous forests!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> तराई के नम पर्णपाती वनों की सबसे मूल्यवान व्यापारिक इमारती लकड़ी साल (साखू) है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Forest Products & Associated Industries -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-boxes-packing" style="color: #d97706;"></i>
                    <span class="lang-en">4. Forest Products &amp; Industries</span>
                    <span class="lang-hi">4. वनोपज एवं वन-आधारित उद्योग</span>
                </h4>
                <span class="mindmap-node-tag">Tendu • Katha • Resin • Paper</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-industry"></i>
                        <span class="lang-en">Major Minor Forest Produce (MFP) &amp; Manufacturing Hubs</span>
                        <span class="lang-hi">प्रमुख लघु वनोपज एवं औद्योगिक केंद्र</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Tendu Leaves (तेंदू पत्ता):</strong> Bidi industry (Sonbhadra, Mirzapur, Bundelkhand)</span>
                        <span class="mindmap-chip"><strong>Katha (कत्था):</strong> Extracted from Khair tree (Bareilly &amp; Aligarh)</span>
                        <span class="mindmap-chip"><strong>Resin &amp; Turpentine (बिरोजा व तारपीन):</strong> Extracted from Pine/Chir (Bareilly factories)</span>
                        <span class="mindmap-chip"><strong>Paper Pulp Industry:</strong> Saharanpur (Star Paper Mills)</span>
                        <span class="mindmap-chip"><strong>Matchbox Industry (दियासलाई):</strong> Bareilly (Rank 1 center) &amp; Saharanpur</span>
                        <span class="mindmap-chip"><strong>Wood Carving:</strong> Saharanpur (Sheesham wood furniture)</span>
                        <span class="mindmap-chip"><strong>Cane &amp; Pith Furniture:</strong> Bareilly</span>
                        <span class="mindmap-chip"><strong>Bhabhar Grass:</strong> Used for rope and cordage manufacturing</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Bareilly is the primary hub for matchbox, resin, and cane industries. Saharanpur leads in paper pulp and wood carving!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> दियासलाई, बिरोजा-तारपीन व बेंत उद्योग का मुख्य केंद्र बरेली है। सहारनपुर कागज व काष्ठ नक्काशी में अग्रणी है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: State Symbols & Heritage Trees -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-award" style="color: #dc2626;"></i>
                    <span class="lang-en">5. State Symbols &amp; Institutions</span>
                    <span class="lang-hi">5. राजकीय वानिकी प्रतीक एवं संस्थान</span>
                </h4>
                <span class="mindmap-node-tag">Ashoka • Palash • Sarus • Swamp Deer</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-flag"></i>
                        <span class="lang-en">Official State Natural Symbols of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के आधिकारिक प्राकृतिक प्रतीक</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>State Tree:</strong> Ashoka / Sita Ashok (Saraca asoca)</span>
                        <span class="mindmap-chip"><strong>State Flower:</strong> Palash / Tesu (Butea monosperma) - notified 4 Jan 2011</span>
                        <span class="mindmap-chip"><strong>State Animal:</strong> Swamp Deer (Barasingha - Rucervus duvaucelii)</span>
                        <span class="mindmap-chip"><strong>State Bird:</strong> Sarus Crane (Grus antigone - world's tallest flying bird)</span>
                        <span class="mindmap-chip"><strong>State Aquatic Animal:</strong> Gangetic Dolphin (Platanista gangetica - 'Susu')</span>
                        <span class="mindmap-chip"><strong>State Fish:</strong> Chital / Chitala (Chitala chitala - 'Moi')</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-building-columns"></i>
                        <span class="lang-en">Key Forestry Institutions</span>
                        <span class="lang-hi">प्रमुख वानिकी संस्थान</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Forest Corporation:</strong> Established in <strong>1974</strong> at Lucknow for scientific extraction and sale of forest produce.</span>
                            <span class="lang-hi"><strong>उप्र वन निगम:</strong> वनोपज के वैज्ञानिक दोहन व विपणन हेतु <strong>1974 में लखनऊ</strong> में स्थापित।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Forest Training Institute:</strong> UP Forestry Training Institute located at <strong>Kanpur</strong>.</span>
                            <span class="lang-hi"><strong>वानिकी प्रशिक्षण संस्थान:</strong> उप्र वानिकी प्रशिक्षण संस्थान <strong>कानपुर</strong> में स्थित है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> State Tree is Ashoka and State Flower is Palash (Flame of the Forest, declared in 2011). Sarus Crane is the State Bird!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> राजकीय वृक्ष अशोक तथा राजकीय पुष्प पलाश (टेसू, 2011 में घोषित) है। सारस (क्रौंच) राजकीय पक्षी है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Social Forestry & Tree Plantation Campaigns -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-seedling" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Social Forestry &amp; Policy Target</span>
                    <span class="lang-hi">6. सामाजिक वानिकी एवं वृक्षारोपण महाभियान</span>
                </h4>
                <span class="mindmap-node-tag">Target: 15% Green Cover by 2026-27</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hand-holding-hand"></i>
                        <span class="lang-en">Pioneering Forest Conservation Schemes</span>
                        <span class="lang-hi">अग्रणी वन संरक्षण योजनाएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Social Forestry Project (1979):</strong> Launched with World Bank aid to plant trees along road margins, rail tracks, and canal embankments to meet rural fuel and fodder needs.</span>
                            <span class="lang-hi"><strong>सामाजिक वानिकी योजना (1979):</strong> विश्व बैंक की सहायता से सड़कों, नहरों व रेल पटरियों के किनारे वृक्षारोपण की शुरुआत।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Vriksharopan Jan Abhiyan:</strong> Massive state campaigns planting <strong>30 to 35+ Crore saplings annually</strong> to achieve the state policy goal of <strong>15% forest and tree cover by 2026-27</strong>.</span>
                            <span class="lang-hi"><strong>वृक्षारोपण जन अभियान:</strong> प्रतिवर्ष <strong>30-35 करोड़ पौधे</strong> लगाने का महाभियान; 2026-27 तक हरित आवरण 15% करने का लक्ष्य।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Social Forestry Scheme was launched in UP in 1979. UP targets 15% combined forest &amp; tree cover by 2026-27!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में सामाजिक वानिकी योजना 1979 में प्रारंभ हुई। उप्र का लक्ष्य 2026-27 तक हरित आवरण 15% पहुंचाना है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 12: Geographical Landscape and Environment
# ==============================================================================
mm_geography = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Geographical Landscape &amp; Environment of UP</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश का भौगोलिक परिदृश्य, सीमाएं एवं भौतिक विभाजन</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Geographical Coordinates &amp; Rank 4 Area • Borders (8 States + 1 UT + Nepal) • Extreme District Boundary Points • 3 Physiographic Divisions (Bhabhar/Tarai, Plains, Plateau) • River Drainage Basins • Environmental Dynamics</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • अक्षांशीय-देशांतरीय विस्तार व क्षेत्रफल में चौथा स्थान • सीमाएं (8 राज्य + 1 UT + नेपाल) • चरम सीमावर्ती जिले • 3 भौतिक विभाग (भाबर/तराई, मैदान, पठार) • अपवाह तंत्र • पर्यावरणीय परिदृश्य</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-earth-asia"></i>
            <span class="lang-en">Spatial Dimensions, Borders &amp; Physiography of Uttar Pradesh</span>
            <span class="lang-hi">उत्तर प्रदेश का भौगोलिक विस्तार, सीमावर्ती राज्य एवं भौतिक भू-आकृतियाँ</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Coordinates, Area & National Rank -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-compass" style="color: #059669;"></i>
                    <span class="lang-en">1. Coordinates &amp; Rank 4 Area</span>
                    <span class="lang-hi">1. स्थिति, विस्तार एवं क्षेत्रफल</span>
                </h4>
                <span class="mindmap-node-tag">2,40,928 sq km • 7.33% of India</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-globe"></i>
                        <span class="lang-en">Geographical Coordinates</span>
                        <span class="lang-hi">अक्षांशीय एवं देशांतरीय विस्तार</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Latitudinal Extent:</strong> <strong>23°52' N to 30°24' N</strong> (Total latitudinal span of 6°32').</span>
                            <span class="lang-hi"><strong>अक्षांशीय विस्तार:</strong> <strong>23°52' उत्तरी अक्षांश से 30°24' उत्तरी अक्षांश</strong> (कुल विस्तार 6°32')।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Longitudinal Extent:</strong> <strong>77°05' E to 84°38' E</strong> (Total longitudinal span of 7°33').</span>
                            <span class="lang-hi"><strong>देशांतरीय विस्तार:</strong> <strong>77°05' पूर्वी देशांतर से 84°38' पूर्वी देशांतर</strong> (कुल विस्तार 7°33')।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Dimensions &amp; Rank:</strong> East-to-West length is <strong>650 km</strong>; North-to-South width is <strong>240 km</strong>. Total area is <strong>2,40,928 sq km</strong> (7.33% of India, <strong>Rank 4</strong> after Rajasthan, MP, Maharashtra).</span>
                            <span class="lang-hi"><strong>आयाम व स्थान:</strong> पूर्व से पश्चिम लंबाई <strong>650 किमी</strong>; उत्तर से दक्षिण चौड़ाई <strong>240 किमी</strong>। क्षेत्रफल <strong>2,40,928 वर्ग किमी</strong> (देश का 7.33%, <strong>चतुर्थ स्थान</strong>)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP ranks 4th in India by area (7.33%), with 650 km East-West length and 240 km North-South width!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र क्षेत्रफल में देश में चौथे स्थान (7.33%) पर है; पूर्व-पश्चिम लंबाई 650 किमी व उत्तर-दक्षिण चौड़ाई 240 किमी है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Bordering States & International Boundary (Nepal) -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-map-location" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Bordering States &amp; Nepal</span>
                    <span class="lang-hi">2. सीमावर्ती राज्य एवं नेपाल सीमा</span>
                </h4>
                <span class="mindmap-node-tag">8 States + 1 UT + Nepal (7 Districts)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-border-all"></i>
                        <span class="lang-en">The 9 Internal Boundaries (8 States + 1 UT)</span>
                        <span class="lang-hi">9 सीमावर्ती राज्य/केंद्रशासित प्रदेश</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Madhya Pradesh:</strong> Longest state border (11 UP districts)</span>
                        <span class="mindmap-chip"><strong>2. Bihar:</strong> Eastern border (7 UP districts)</span>
                        <span class="mindmap-chip"><strong>3. Uttarakhand:</strong> Northern border (7 UP districts)</span>
                        <span class="mindmap-chip"><strong>4. Haryana:</strong> Western border (6 UP districts)</span>
                        <span class="mindmap-chip"><strong>5. Rajasthan:</strong> South-Western border (2 districts: Agra &amp; Mathura)</span>
                        <span class="mindmap-chip"><strong>6. Chhattisgarh:</strong> Touches Sonbhadra only</span>
                        <span class="mindmap-chip"><strong>7. Jharkhand:</strong> Touches Sonbhadra only</span>
                        <span class="mindmap-chip"><strong>8. Himachal Pradesh:</strong> Shortest state border (Saharanpur only)</span>
                        <span class="mindmap-chip"><strong>9. NCT Delhi (UT):</strong> Western border (Ghaziabad &amp; GB Nagar)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-flag"></i>
                        <span class="lang-en">Nepal International Border (579 km)</span>
                        <span class="lang-hi">नेपाल अंतरराष्ट्रीय सीमा (579 किमी)</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>7 Nepal Border Districts (West to East):</strong> 1. Pilibhit; 2. Lakhimpur Kheri; 3. Bahraich; 4. Shravasti; 5. Balrampur; 6. Siddharthnagar; 7. Maharajganj.</span>
                            <span class="lang-hi"><strong>नेपाल सीमा से लगे 7 जिले (पश्चिम से पूर्व):</strong> 1. पीलीभीत; 2. लखीमपुर खीरी; 3. बहराइच; 4. श्रावस्ती; 5. बलरामपुर; 6. सिद्धार्थनगर; 7. महाराजगंज।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP borders 8 States and 1 UT. Longest border is with MP (11 districts), shortest with Himachal Pradesh (Saharanpur). 7 districts touch Nepal!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र की सीमा 8 राज्यों व 1 UT से मिलती है। सबसे लंबी सीमा म.प्र. (11 जिले) और सबसे छोटी हि.प्र. (सहारनपुर) से लगती है। 7 जिले नेपाल को छूते हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Extreme District Points (Sonbhadra & Ballia) -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-arrows-to-dot" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Extreme Boundary Districts</span>
                    <span class="lang-hi">3. उत्तर प्रदेश के चरम सीमावर्ती जिले</span>
                </h4>
                <span class="mindmap-node-tag">Sonbhadra: Touches 4 States</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crosshairs"></i>
                        <span class="lang-en">The 4 Cardinal Extreme Districts</span>
                        <span class="lang-hi">4 दिशाओं के चरम सीमावर्ती जिले</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Northernmost District:</strong> Saharanpur (सहारनपुर)</span>
                        <span class="mindmap-chip"><strong>Southernmost District:</strong> Sonbhadra (सोनभद्र)</span>
                        <span class="mindmap-chip"><strong>Easternmost District:</strong> Ballia (बलिया - गंगा-घाघरा संगम)</span>
                        <span class="mindmap-chip"><strong>Westernmost District:</strong> Shamli (शामली - हरियाणा सीमा)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-gem"></i>
                        <span class="lang-en">Sonbhadra &amp; Saharanpur Unique Geographic Facts</span>
                        <span class="lang-hi">सोनभद्र व सहारनपुर की भौगोलिक विशिष्टता</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sonbhadra (The 4-State Border):</strong> Only district in India that borders <strong>4 different States</strong>: Madhya Pradesh (West), Chhattisgarh (South), Jharkhand (Southeast), and Bihar (East).</span>
                            <span class="lang-hi"><strong>सोनभद्र (4 राज्यों की सीमा):</strong> भारत का एकमात्र जिला जो <strong>4 राज्यों</strong> (मध्य प्रदेश, छत्तीसगढ़, झारखंड और बिहार) की सीमाओं को स्पर्श करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Saharanpur (The 3-State Border):</strong> Borders 3 States: Uttarakhand (East), Himachal Pradesh (North), and Haryana (West).</span>
                            <span class="lang-hi"><strong>सहारनपुर (3 राज्यों की सीमा):</strong> उत्तराखंड, हिमाचल प्रदेश तथा हरियाणा की सीमाओं को स्पर्श करता है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lalitpur (Surrounded by MP on 3 Sides):</strong> Surrounded by Madhya Pradesh on three sides; connected to UP mainland only through Jhansi.</span>
                            <span class="lang-hi"><strong>ललितपुर (3 ओर से म.प्र. से घिरा):</strong> तीन ओर से मध्य प्रदेश से घिरा जिला; उप्र के केवल झांसी जिले से जुड़ा है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Easternmost is Ballia, Westernmost is Shamli, Northernmost is Saharanpur, Southernmost is Sonbhadra. Sonbhadra touches 4 states!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> सबसे पूर्वी बलिया, पश्चिमी शामली, उत्तरी सहारनपुर, दक्षिणी सोनभद्र है। सोनभद्र देश का एकमात्र 4 राज्यों को छूने वाला जिला है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Three Physiographic Divisions -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-mountain" style="color: #d97706;"></i>
                    <span class="lang-en">4. Three Physiographic Divisions</span>
                    <span class="lang-hi">4. तीन प्रमुख भौतिक भू-आकृतिक विभाग</span>
                </h4>
                <span class="mindmap-node-tag">Bhabhar-Tarai • Plains • Plateau</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-layer-group"></i>
                        <span class="lang-en">Geological Formations &amp; Relief</span>
                        <span class="lang-hi">भू-आकृतिक संरचना एवं उच्चावच</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1. Bhabhar &amp; Tarai Belt:</strong> Foothill zone. <em>Bhabhar</em> is a narrow porous pebble/boulder belt where rivers disappear; <em>Tarai</em> is a marshy, humid, densely forested belt where rivers resurface (rich sugarcane &amp; paddy zone).</span>
                            <span class="lang-hi"><strong>1. भाबर व तराई क्षेत्र:</strong> शिवालिक तलहटी। <em>भाबर</em> कंकड़-पत्थरों वाला छिद्रयुक्त क्षेत्र जहाँ नदियां लुप्त हो जाती हैं; <em>तराई</em> दलदली, आर्द्र क्षेत्र जहाँ नदियां पुनः प्रकट होती हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2. Gangetic Plain (मैदानी भाग):</strong> Covers ~70% of state area between Yamuna in west and Gandak in east. Divided into <em>Khadar</em> (new flood alluvium) and <em>Bhangar</em> (older elevated alluvium). Gentle general slope is from <strong>North-West to South-East</strong>.</span>
                            <span class="lang-hi"><strong>2. विशाल गंगा का मैदान:</strong> उप्र का ~70% भूभाग; खादर (नवीन जलोढ़) व बांगर (पुरातन जलोढ़) में विभाजित। सामान्य ढाल <strong>उत्तर-पश्चिम से दक्षिण-पूर्व</strong> की ओर है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3. Southern Plateau &amp; Hill Region:</strong> Northern extension of the Deccan Peninsula (Bundelkhand &amp; Vindhyan plateau). Composed of ancient Pre-Cambrian granite and gneiss; average height 300m (peaks up to 600m in Mirzapur/Sonbhadra like Kaimur hills).</span>
                            <span class="lang-hi"><strong>3. दक्षिणी पठारी एवं पहाड़ी क्षेत्र:</strong> दक्कन प्रायद्वीप का उत्तरी विस्तार (बुंदेलखंड व विंध्य पठार); प्राचीन नीस व ग्रेनाइट चट्टानों से निर्मित; औसत ऊंचाई 300 मी.।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Rivers disappear in the porous Bhabhar belt and re-emerge in the marshy Tarai belt. The general slope of the Gangetic plain is North-West to South-East!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नदियां कंकड़ीले भाबर में लुप्त होकर दलदली तराई में पुनः प्रकट होती हैं। गंगा मैदान का सामान्य ढाल उत्तर-पश्चिम से दक्षिण-पूर्व है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: River Drainage Network & Hydrology -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-water" style="color: #dc2626;"></i>
                    <span class="lang-en">5. River Drainage Network</span>
                    <span class="lang-hi">5. अपवाह तंत्र एवं प्रमुख नदियाँ</span>
                </h4>
                <span class="mindmap-node-tag">Ganga • Yamuna • Gomti • Ghaghara</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-route"></i>
                        <span class="lang-en">Classification by Origin</span>
                        <span class="lang-hi">उद्गम के आधार पर नदियों का वर्गीकरण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Himalayan Rivers:</strong> Snow-fed perennial rivers: <em>Ganga</em> (enters at Bijnor, exits at Ballia; 1,450 km in UP traversing 28 districts), <em>Yamuna</em> (enters at Saharanpur, merges at Prayagraj Sangam traversing 19 districts), <em>Ramganga</em>, <em>Ghaghara (Saryu)</em>, <em>Gandak</em>, <em>Rapti</em>.</span>
                            <span class="lang-hi"><strong>हिमालयी नदियां:</strong> <em>गंगा</em> (बिजनौर से प्रवेश, बलिया से निकास; उप्र में 1,450 किमी, 28 जिले), <em>यमुना</em> (सहारनपुर से प्रवेश, प्रयागराज संगम में विलय, 19 जिले), <em>रामगंगा</em>, <em>घाघरा (सरयू)</em>, <em>राप्ती</em>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Plains Origin Rivers:</strong> <strong>Gomti River</strong> originates from <strong>Fulhar Jheel (Gomat Tal) in Pilibhit</strong>; flows through Lucknow, Sultanpur, Jaunpur, and meets Ganga at Kaithi (Ghazipur/Varanasi border).</span>
                            <span class="lang-hi"><strong>मैदानी नदियां:</strong> <strong>गोमती नदी</strong> <strong>पीलीभीत की फुलहर झील (गोमत ताल)</strong> से निकलती है; लखनऊ, सुल्तानपुर, जौनपुर होते हुए कैथी (गाजीपुर) में गंगा से मिलती है।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Peninsular Plateau Rivers:</strong> Flow from south to north joining Yamuna/Ganga: <em>Chambal</em>, <em>Betwa</em>, <em>Ken</em>, <em>Son</em> (Sonbhadra), <em>Tons (Tamasa)</em>.</span>
                            <span class="lang-hi"><strong>पठारी नदियां:</strong> दक्षिण से उत्तर बहकर यमुना/गंगा में मिलती हैं: <em>चंबल</em>, <em>बेतवा</em>, <em>केन</em>, <em>सोन</em> (सोनभद्र), <em>टोंस</em>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ganga enters UP at Bijnor and leaves at Ballia (flows through 28 districts). Gomti originates in the plains from Fulhar Lake (Pilibhit)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> गंगा उप्र में बिजनौर से प्रवेश कर बलिया से निकलती है (28 जिलों से प्रवाह)। गोमती नदी मैदानी भाग में फुलहर झील (पीलीभीत) से निकलती है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Environmental Landscape & Conservation -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-seedling" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Environmental Dynamics</span>
                    <span class="lang-hi">6. पर्यावरणीय परिदृश्य एवं संरक्षण</span>
                </h4>
                <span class="mindmap-node-tag">10 Ramsar Sites • 4 Tiger Reserves</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water-ladder"></i>
                        <span class="lang-en">Wetlands, Ravines &amp; Protected Ecosystems</span>
                        <span class="lang-hi">आर्द्रभूमियाँ, बीहड़ एवं संरक्षित परिस्थितिकी</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>10 Ramsar Wetlands:</strong> Upper Ganga (first 2005), Nawabganj, Samaspur, Sandi, Parvati Arga, Saman, Sarsai Nawar, Sur Sarovar, Haiderpur, Bakhira (10th 2022)</span>
                        <span class="mindmap-chip"><strong>4 Tiger Reserves:</strong> Dudhwa (1987), Pilibhit (2014), Amangarh (buffer), Ranipur (2022 - 4th in Chitrakoot)</span>
                        <span class="mindmap-chip"><strong>Ravines (बीहड़):</strong> Chambal &amp; Yamuna gullies (Agra, Etawah - severe badland gully erosion)</span>
                        <span class="mindmap-chip"><strong>National Chambal Sanctuary:</strong> Gharial and Gangetic dolphin protection</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 10 Ramsar Wetland sites (Upper Ganga River was the first in 2005; Bakhira in Sant Kabir Nagar was 10th). Ranipur (Chitrakoot) is the 4th Tiger Reserve!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में 10 रामसर स्थल हैं (ऊपरी गंगा प्रथम, बखिरा 10वां)। रानीपुर (चित्रकूट) राज्य का चौथा और देश का 53वां टाइगर रिजर्व है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Helper to inject and clean mermaid
# ==============================================================================
def inject_mindmap(topic_dir, mindmap_content):
    path = os.path.join('upsssc-up-gk', topic_dir, 'index.html')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match Card 1
    m1 = re.search(r'(<!--\s*Card 1:\s*Mind Map\s*-->.*?)(<!--\s*Card 2:)', content, re.DOTALL)
    m2 = re.search(r'(<div class="card-premium">.*?Mindmap.*?)(<div class="card-premium")', content, re.DOTALL | re.IGNORECASE)

    if m1:
        target = m1.group(1)
        content = content.replace(target, mindmap_content + '\n\n')
    elif m2:
        target = m2.group(1)
        content = content.replace(target, mindmap_content + '\n\n')
    else:
        print(f"ERROR: Could not match mindmap section in {topic_dir}")
        return False

    # Remove mermaid scripts
    content = re.sub(r'<script\s+src="https://cdn\.jsdelivr\.net/npm/mermaid/dist/mermaid\.min\.js"></script>\s*', '', content)
    content = re.sub(r'<script>mermaid\.initialize\(\{startOnLoad:true,\s*theme:\s*\'default\'\}\);</script>\s*', '', content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated: {topic_dir}")
    return True

if __name__ == '__main__':
    inject_mindmap('festivals', mm_festivals)
    inject_mindmap('folk-dances', mm_folk_dances)
    inject_mindmap('forests', mm_forests)
    inject_mindmap('geographical-landscape-and-environment', mm_geography)
