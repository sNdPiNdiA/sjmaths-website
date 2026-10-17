# -*- coding: utf-8 -*-
import sys, os, re

sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# Topic 20: Social Customs and Tourism of Uttar Pradesh
# ==============================================================================
mm_tourism = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Social Customs &amp; Tourism of UP</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के सामाजिक रीति-रिवाज, परंपराएं एवं पर्यटन सर्किट</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • 16 Vedic Samskaras &amp; Life-Cycle Rites • Regional Customs &amp; Tribal Ethos • Tourism Policy 2022 &amp; Rank 1 Domestic Footfall • Heritage Arc (Agra-Lucknow-Varanasi) • Ramayana, Krishna &amp; Buddhist Circuits • Specialized Bundelkhand &amp; Jain Circuits</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • वैदिक 16 संस्कार व जीवन चक्र • आंचलिक रीति-रिवाज व जनजातीय परंपराएं • पर्यटन नीति 2022 व घरेलू पर्यटकों में प्रथम स्थान • हेरिटेज आर्क (आगरा-लखनऊ-वाराणसी) • रामायण, कृष्ण व बौद्ध सर्किट • बुंदेलखंड, सूफी व जैन सर्किट</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-route"></i>
            <span class="lang-en">Living Traditions, Samskaras &amp; Vibrant Tourism Circuits of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की जीवंत सामाजिक परंपराएं, संस्कार एवं प्रमुख पर्यटन परिपथ</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: 16 Samskaras & Life-Cycle Customs in UP -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hands-praying" style="color: #059669;"></i>
                    <span class="lang-en">1. 16 Vedic Samskaras</span>
                    <span class="lang-hi">1. 16 संस्कार एवं जीवन-चक्र रीति-रिवाज</span>
                </h4>
                <span class="mindmap-node-tag">Vedic Rites of Passage</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-fire-burner"></i>
                        <span class="lang-en">Major Life-Cycle Rituals (संस्कार)</span>
                        <span class="lang-hi">प्रमुख जीवन-चक्र संस्कार</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Garbhadhana:</strong> Conception rite</span>
                        <span class="mindmap-chip"><strong>2. Pumsavana:</strong> Fetal protection rite</span>
                        <span class="mindmap-chip"><strong>3. Simantonnayana:</strong> Baby shower rite</span>
                        <span class="mindmap-chip"><strong>4. Jatakarma:</strong> Birth rite (honey-ghee)</span>
                        <span class="mindmap-chip"><strong>5. Namakarana:</strong> Naming (10th/12th day)</span>
                        <span class="mindmap-chip"><strong>6. Nishkramana:</strong> First outdoor outing</span>
                        <span class="mindmap-chip"><strong>7. Annaprashana:</strong> First solid grain (6th mo)</span>
                        <span class="mindmap-chip"><strong>8. Chudakarana:</strong> Mundan / Head-shaving</span>
                        <span class="mindmap-chip"><strong>9. Karnavedha:</strong> Ear piercing</span>
                        <span class="mindmap-chip"><strong>10. Vidyarambha:</strong> Akshararambha alphabet rite</span>
                        <span class="mindmap-chip"><strong>11. Upanayana:</strong> Janeu / Sacred thread</span>
                        <span class="mindmap-chip"><strong>12. Vedarambha:</strong> Vedic studies begin</span>
                        <span class="mindmap-chip"><strong>13. Keshanta:</strong> First shave</span>
                        <span class="mindmap-chip"><strong>14. Samavartana:</strong> Graduation from Gurukul</span>
                        <span class="mindmap-chip"><strong>15. Vivaha:</strong> Marriage (Kanyadan, Saptapadi)</span>
                        <span class="mindmap-chip"><strong>16. Antyeshti:</strong> Funeral &amp; Shraddha / Pinda Daan</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Upanayana is the sacred thread ceremony (Janeu), Annaprashana is the first feeding of solid food, and Antyeshti is the 16th and final rite!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उपनयन संस्कार जनेऊ धारण करने का संस्कार है, अन्नप्राशन प्रथम अन्न ग्रहण संस्कार है, तथा अंत्येष्टि 16वां एवं अंतिम संस्कार है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Regional Folk Customs & Tribal Traditions -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-people-roof" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Regional &amp; Tribal Customs</span>
                    <span class="lang-hi">2. आंचलिक रीति-रिवाज एवं जनजातीय परंपराएं</span>
                </h4>
                <span class="mindmap-node-tag">Tharu • Chhath • Karwa Chauth</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-users"></i>
                        <span class="lang-en">Distinct Regional Customs</span>
                        <span class="lang-hi">प्रमुख आंचलिक परंपराएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chhath Puja (Purvanchal):</strong> Dedicated to Sun God (Surya) and Usha; 4-day austere festival involving 36-hour nirjala fast and standing in water at riverbanks to offer Arghya to setting and rising Sun.</span>
                            <span class="lang-hi"><strong>छठ पूजा (पूर्वांचल):</strong> सूर्य देव व षष्ठी मैया की उपासना; 36 घंटे का निर्जला व्रत; नदियों के तट पर डूबते व उगते सूर्य को अर्घ्य।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Karwa Chauth &amp; Ahoi Ashtami:</strong> Widely observed across Western and Central UP; Karwa Chauth for husband's longevity and Ahoi Ashtami for children's well-being.</span>
                            <span class="lang-hi"><strong>करवा चौथ व अहोई अष्टमी:</strong> पश्चिमी व मध्य उप्र में सुहाग की दीर्घायु हेतु करवा चौथ तथा संतान कल्याण हेतु अहोई अष्टमी।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-campground"></i>
                        <span class="lang-en">Tribal Social Traditions</span>
                        <span class="lang-hi">जनजातीय सामाजिक रीति-रिवाज</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Tharu Tribe Traditions:</strong> Women enjoy supreme property and domestic status; practice joint family system; observe Diwali as <strong>Shoka Parva (day of mourning)</strong> offering Putla to ancestors.</span>
                            <span class="lang-hi"><strong>थारू परंपराएं:</strong> महिलाओं को परिवार में सर्वोच्च अधिकार; दीपावली को पूर्वजों की स्मृति में <strong>शोक पर्व</strong> के रूप में मनाते हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Tharu tribe observes Diwali as mourning day. Chhath Puja is the foremost solar festival of Eastern UP!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> थारू जनजाति दीपावली को शोक पर्व के रूप में मनाती है। छठ पूजा पूर्वांचल का सबसे बड़ा सूर्योपासना पर्व है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Tourism Policy 2022 & National Footfall Dominance -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-ranking-star" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Tourism Policy &amp; Rank 1</span>
                    <span class="lang-hi">3. पर्यटन नीति 2022 एवं घरेलू पर्यटकों में प्रथम स्थान</span>
                </h4>
                <span class="mindmap-node-tag">Rank 1 in Domestic Tourists (32+ Cr)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trophy"></i>
                        <span class="lang-en">Tourism Milestones &amp; Policy 2022</span>
                        <span class="lang-hi">पर्यटन उपलब्धियां एवं नीतिगत लक्ष्य</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rank 1 in Domestic Footfall:</strong> UP ranks <strong>#1 in India for Domestic Tourist Visits (DTV)</strong> with over 32+ Crore pilgrims and tourists annually, driven by the Kashi Vishwanath Dham corridor, Ayodhya Ram Temple, and Braj Teerth Vikas.</span>
                            <span class="lang-hi"><strong>घरेलू पर्यटकों में देश में प्रथम:</strong> उप्र प्रतिवर्ष 32+ करोड़ पर्यटकों के साथ देश में <strong>प्रथम स्थान</strong> पर है (काशी विश्वनाथ धाम, अयोध्या राम मंदिर व ब्रज तीर्थ के कारण)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>UP Tourism Policy 2022:</strong> Promotes 12 major thematic circuits, grants industry status with capital subsidies up to 25%, and develops homestays, bed-and-breakfasts, and rural tourism.</span>
                            <span class="lang-hi"><strong>उप्र पर्यटन नीति 2022:</strong> 12 प्रमुख सर्किटों का विकास; 25% तक पूंजीगत अनुदान; होमस्टे व ग्रामीण पर्यटन को प्रोत्साहन।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Uttar Pradesh ranks #1 in India in Domestic Tourist Visits (DTV). UP Tourism Policy was notified in 2022!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> घरेलू पर्यटकों की संख्या में उत्तर प्रदेश देश में प्रथम स्थान पर है। उप्र पर्यटन नीति 2022 में अधिसूचित की गई!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: The Heritage Arc: Agra - Lucknow - Varanasi -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-archway" style="color: #d97706;"></i>
                    <span class="lang-en">4. The Heritage Arc</span>
                    <span class="lang-hi">4. हेरिटेज आर्क: आगरा - लखनऊ - वाराणसी</span>
                </h4>
                <span class="mindmap-node-tag">Golden Triangle of UP Tourism</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shapes"></i>
                        <span class="lang-en">The 3 Apex Vertices of Heritage Arc</span>
                        <span class="lang-hi">हेरिटेज आर्क के 3 प्रमुख शीर्ष</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Agra Vertex:</strong> Mughal architectural capital; houses 3 UNESCO World Heritage Sites (Taj Mahal, Agra Fort, Fatehpur Sikri), Sikandra (Akbar's Tomb), and Itimad-ud-Daulah.</span>
                            <span class="lang-hi"><strong>आगरा शीर्ष:</strong> मुग़ल स्थापत्य का विश्व केंद्र; 3 यूनेस्को विश्व धरोहर (ताजमहल, आगरा किला, फतेहपुर सीकरी), सिकंदरा व एतमादुद्दौला।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Lucknow Vertex:</strong> Nawabi cultural and architectural capital; Bara Imambara, Bhulbhulaiya, Rumi Darwaza, Chhota Imambara, British Residency, Chikankari crafts, and Awadhi cuisine.</span>
                            <span class="lang-hi"><strong>लखनऊ शीर्ष:</strong> नवाबी तहज़ीब व स्थापत्य; बड़ा इमामबाड़ा, भूलभुलैया, रूमी दरवाजा, छोटा इमामबाड़ा, रेजीडेंसी व चिकनकारी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Varanasi Vertex:</strong> Spiritual capital of the world; Kashi Vishwanath Dham, 84 Ganga ghats with evening Ganga Aarti, Sarnath (Buddhist first sermon), Banarasi silk weaving, and classical music.</span>
                            <span class="lang-hi"><strong>वाराणसी शीर्ष:</strong> विश्व की प्राचीनतम जीवंत नगरी; काशी विश्वनाथ धाम, 84 गंगा घाट व आरती, सारनाथ तथा बनारसी रेशमी साड़ियां।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> The 'Heritage Arc' conceptualized by UP Tourism links three cities: Agra, Lucknow, and Varanasi!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र पर्यटन विभाग द्वारा विकसित 'हेरिटेज आर्क' तीन शहरों को जोड़ता है: आगरा, लखनऊ और वाराणसी!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Ramayana, Krishna & Buddhist Tourism Circuits -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-om" style="color: #dc2626;"></i>
                    <span class="lang-en">5. Spiritual Tourism Circuits</span>
                    <span class="lang-hi">5. रामायण, कृष्ण एवं बौद्ध पर्यटन परिपथ</span>
                </h4>
                <span class="mindmap-node-tag">Ayodhya • Mathura • Sarnath</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-ring"></i>
                        <span class="lang-en">Thematic Pilgrimage Circuits</span>
                        <span class="lang-hi">प्रमुख आध्यात्मिक परिपथ</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Ramayana Circuit:</strong> Ayodhya, Chitrakoot, Shringverpur (Prayagraj)</span>
                        <span class="mindmap-chip"><strong>Krishna Circuit:</strong> Mathura, Vrindavan, Barsana, Gokul, Goverdhan, Nandgaon</span>
                        <span class="mindmap-chip"><strong>Buddhist Circuit:</strong> Sarnath, Kushinagar, Shravasti, Kapilavastu, Sankisa, Kaushambi</span>
                        <span class="mindmap-chip"><strong>Spiritual Circuit:</strong> Prayagraj (Sangam), Varanasi, Naimisharanya, Gorakhpur</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-mountain-sun"></i>
                        <span class="lang-en">Chitrakoot &amp; Ayodhya Highlights</span>
                        <span class="lang-hi">अयोध्या एवं चित्रकूट की महत्ता</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Chitrakoot:</strong> Lord Rama spent 11.5 of his 14 years of exile here; sacred sites: Kamadgiri hill, Ramghat on Mandakini river, Bharat Milap, Janaki Kund, Gupt Godavari caves, Sphatik Shila, Sati Anusuya ashram.</span>
                            <span class="lang-hi"><strong>चित्रकूट:</strong> भगवान राम ने वनवास के 11.5 वर्ष यहीं बिताए; कामदगिरि, मंदाकिनी तट पर रामघाट, गुप्त गोदावरी, स्फटिक शिला, सती अनुसूया आश्रम।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Shringverpur (where Nishadraj met Lord Rama) is in Prayagraj district. Lord Rama spent 11.5 years of exile in Chitrakoot!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> श्रृंगवेरपुर (जहाँ निषादराज से भेंट हुई) प्रयागराज में है। भगवान राम ने 11.5 वर्ष चित्रकूट में व्यतीत किए थे!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Specialized Circuits: Bundelkhand, Sufi & Jain Heritage -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-place-of-worship" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Bundelkhand, Sufi &amp; Jain Circuits</span>
                    <span class="lang-hi">6. बुंदेलखंड, सूफी एवं जैन पर्यटन परिपथ</span>
                </h4>
                <span class="mindmap-node-tag">Jain 5 Tirthankaras • Kalinjar • Deva</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-chess-rook"></i>
                        <span class="lang-en">Bundelkhand Fort Circuit</span>
                        <span class="lang-hi">बुंदेलखंड किला सर्किट</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Jhansi:</strong> Rani Jhansi Fort (Bir Singh Deo 1613) &amp; Rani Mahal</span>
                        <span class="mindmap-chip"><strong>Kalinjar (Banda):</strong> Chandela fort, Nilkanth temple, Sher Shah death 1545</span>
                        <span class="mindmap-chip"><strong>Deogarh (Lalitpur):</strong> Dashavatara Gupta temple &amp; 31 Jain temples</span>
                        <span class="mindmap-chip"><strong>Mahoba:</strong> Chandela capital, Rahila Sun Temple, Vijay Sagar</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-hand-holding-heart"></i>
                        <span class="lang-en">Jain &amp; Sufi Sacred Circuits</span>
                        <span class="lang-hi">जैन एवं सूफी तीर्थ परिपथ</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Jain Circuit:</strong> Birthplace of 5 Tirthankaras in Ayodhya (Rishabhanatha 1st, Ajitanatha 2nd, Abhinandananatha 4th, Sumatinatha 5th, Anantanatha 14th); Parshvanatha (23rd) and Suparshvanatha (7th) born in Varanasi; Padmaprabha (6th) in Kaushambi.</span>
                            <span class="lang-hi"><strong>जैन सर्किट:</strong> अयोध्या में 5 तीर्थंकरों (ऋषभदेव, अजितनाथ, अभिनंदननाथ, सुमतिनाथ, अनंतनाथ) का जन्म; वाराणसी में पार्श्वनाथ व सुपार्श्वनाथ; कौशाम्बी में पद्मप्रभ।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Sufi Circuit:</strong> Deva Sharif (Barabanki - Haji Waris Ali Shah), Dargah of Syed Salar Masood Ghazi (Bahraich), Salim Chishti (Fatehpur Sikri), and Nizamuddin Auliya birthplace (Badaun).</span>
                            <span class="lang-hi"><strong>सूफी सर्किट:</strong> देवा शरीफ (बाराबंकी), सैयद सालार मसूद गाजी (बहराइच), शेख सलीम चिश्ती (सीकरी) व निजामुद्दीन औलिया जन्मस्थली (बदायूं)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Five Jain Tirthankaras (including 1st Tirthankara Rishabhanatha) were born in Ayodhya. Deva Sharif is in Barabanki!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> प्रथम तीर्थंकर ऋषभदेव सहित 5 जैन तीर्थंकरों का जन्म अयोध्या में हुआ। देवा शरीफ बाराबंकी में स्थित है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 21: Soil of Uttar Pradesh
# ==============================================================================
mm_soil = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Soils of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश की मिट्टियाँ, क्षेत्रीय वर्गीकरण एवं समस्याग्रस्त मृदा</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • 3 Major Soil Belts • Bhabhar &amp; Terai Soils • Gangetic Alluvium (Khadar vs Bhangar) • Problem Soils (Usar, Reh, Kallar &amp; Gypsum Reclamation) • Bundelkhand Black Soils (Mar &amp; Kabar) • Red Soils (Parwa, Rakar &amp; Bonta)</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • 3 प्रमुख मृदा कटिबंध • भाबर व तराई मृदा • गंगा का जलोढ़ (खादर बनाम बांगर) • समस्याग्रस्त ऊसर/रेह मृदा व जिप्सम सुधार • बुंदेलखंड की काली मिट्टी (माड़ व काबर) • लाल मिट्टियाँ (पड़वा, रांकड़ व बोंटा)</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-earth-americas"></i>
            <span class="lang-en">Pedological Wealth, Zonal Soil Distribution &amp; Soil Health of UP</span>
            <span class="lang-hi">उत्तर प्रदेश का मृदा विज्ञान, क्षेत्रीय मृदा वितरण एवं उर्वरता प्रबंधन</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Zonal Soil Framework: 3 Broad Belts -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-layer-group" style="color: #059669;"></i>
                    <span class="lang-en">1. 3 Major Soil Belts</span>
                    <span class="lang-hi">1. तीन प्रमुख मृदा कटिबंध</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">Zonal Division</span>
                    <span class="lang-hi">क्षेत्रीय कटिबंध</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-map"></i>
                        <span class="lang-en">Three Broad Geomorphic Zones</span>
                        <span class="lang-hi">3 भू-आकृतिक मृदा क्षेत्र</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Bhabhar &amp; Terai Soil Belt:</strong> Northern sub-Himalayan strip</span>
                        <span class="mindmap-chip"><strong>2. Central Gangetic Alluvial Belt:</strong> Vast fertile plains (~70% of state)</span>
                        <span class="mindmap-chip"><strong>3. Southern Plateau &amp; Vindhyan Belt:</strong> Bundelkhand &amp; Vindhyan soils</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-seedling"></i>
                        <span class="lang-en">Nutrient Status of UP Soils</span>
                        <span class="lang-hi">मृदा की सामान्य पोषक स्थिति</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>General Nutrient Profile:</strong> UP soils are generally rich in <strong>Potash</strong> and <strong>Lime</strong>, but universally deficient in <strong>Nitrogen</strong>, <strong>Phosphorus</strong>, and <strong>Organic Carbon (Humus)</strong> (except Terai).</span>
                            <span class="lang-hi"><strong>पोषक तत्व स्थिति:</strong> उप्र की मिट्टियों में सामान्यतः <strong>पोटाश</strong> व <strong>चूना</strong> पर्याप्त मात्रा में होता है, लेकिन <strong>नाइट्रोजन</strong>, <strong>फास्फोरस</strong> व <strong>जीवांश (ह्यूमस)</strong> की व्यापक कमी पाई जाती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP soils are broadly divided into 3 zones: Bhabhar-Terai, Central Alluvial Plain, and Southern Hill-Plateau!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र की मृदा को 3 मुख्य भागों में बांटा गया है: भाबर-तराई, मध्यवर्ती जलोढ़ मैदान, और दक्षिणी पहाड़ी-पठारी क्षेत्र!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Bhabhar & Terai Soils -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-mountain" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Bhabhar &amp; Terai Soils</span>
                    <span class="lang-hi">2. भाबर एवं तराई मृदा</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">Gravel vs Marsh</span>
                    <span class="lang-hi">कंकड़ व दलदली</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shapes"></i>
                        <span class="lang-en">Bhabhar Soil Characteristics</span>
                        <span class="lang-hi">भाबर मृदा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bhabhar (Coarse &amp; Porous):</strong> Narrow gravelly strip at foot of Shivalik; composed of unassorted pebbles, gravels, and coarse sand; extremely porous causing streams to disappear underground; completely unfit for arable farming (forested).</span>
                            <span class="lang-hi"><strong>भाबर मृदा:</strong> शिवालिक तलहटी में कंकड़, पत्थर व बजरी से निर्मित छिद्रयुक्त मृदा; जल धारण क्षमता शून्य जिससे नदियां भूमिगत हो जाती हैं; कृषि हेतु अनुपयुक्त।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water"></i>
                        <span class="lang-en">Terai Soil Characteristics</span>
                        <span class="lang-hi">तराई मृदा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Terai (Rich Clayey Loam):</strong> Marshy, silty loam soil rich in nitrogen and organic matter (humus); dark colored; highly fertile; world-class yields of <strong>Sugarcane, Paddy (Rice), and Jute</strong>. Districts: Pilibhit, Lakhimpur Kheri, Bahraich, Shravasti, Balrampur, Siddharthnagar.</span>
                            <span class="lang-hi"><strong>तराई मृदा:</strong> दलदली, महीन कणों वाली दोमट मृदा; नाइट्रोजन व जीवांश (ह्यूमस) से भरपूर; <strong>गन्ना, धान और जूट</strong> की खेती हेतु आदर्श। प्रमुख जिले: पीलीभीत, लखीमपुर, बहराइच, श्रावस्ती।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Terai soil is rich in Nitrogen and Organic matter (Humus) and is exceptionally suited for Sugarcane and Paddy crops!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> तराई मृदा में नाइट्रोजन और जीवांश (ह्यूमस) प्रचुर मात्रा में होता है, जो गन्ना और धान की बंपर पैदावार हेतु सर्वोत्तम है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Gangetic Plain Alluvial Soils: Khadar vs Bhangar -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-water" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. Khadar vs Bhangar Alluvium</span>
                    <span class="lang-hi">3. खादर बनाम बांगर जलोढ़</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">New &amp; Old Alluvium</span>
                    <span class="lang-hi">नवीन व पुरातन जलोढ़</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-water-ladder"></i>
                        <span class="lang-en">Khadar Soil (नवीन जलोढ़ / कछारी)</span>
                        <span class="lang-hi">खादर मृदा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Annual Flood Deposition:</strong> Found in active floodplains of Ganga, Yamuna, Ghaghara, Betwa. Fine silt, sandy loam, light colored; refreshed every year by floods; highly fertile without heavy fertilizer requirement; holds optimum soil moisture.</span>
                            <span class="lang-hi"><strong>नवीन जलोढ़:</strong> नदियों के बाढ़ के मैदानों में प्रतिवर्ष नई गाद से नवीनीकृत; महीन कणों वाली, उपजाऊ, हल्के रंग की मृदा; खाद की कम आवश्यकता होती है।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-gem"></i>
                        <span class="lang-en">Bhangar Soil (पुरातन जलोढ़) &amp; Kankar</span>
                        <span class="lang-hi">बांगर मृदा की विशेषताएं एवं कंकड़</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Elevated Interfluves:</strong> Found on higher terrace plains above flood levels. Clay loam to loam texture; contains calcareous calcium carbonate nodules known as <strong>Kankar (कंकड़)</strong> in the subsoil; needs chemical fertilizers and canal irrigation.</span>
                            <span class="lang-hi"><strong>पुरातन जलोढ़:</strong> बाढ़ क्षेत्र से ऊंचे मैदानों में; दोमट से मटियार दोमट; नीचे की परतों में चूने की ग्रंथियां पाई जाती हैं जिन्हें <strong>कंकड़</strong> कहते हैं।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Khadar is new fertile flood alluvium, while Bhangar is older alluvium containing calcareous 'Kankar' nodules!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> खादर नवीन जलोढ़ है जो अत्यधिक उपजाऊ है, जबकि बांगर पुरातन जलोढ़ है जिसमें कंकड़ ग्रंथियां पाई जाती हैं!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Problem Soils: Usar, Reh, Kallar & Gypsum Reclamation -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-exclamation-triangle" style="color: #d97706;"></i>
                    <span class="lang-en">4. Problem Soils (Usar / Reh)</span>
                    <span class="lang-hi">4. समस्याग्रस्त मृदा (ऊसर व रेह)</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">Gypsum Reclamation</span>
                    <span class="lang-hi">जिप्सम सुधार</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-flask-vial"></i>
                        <span class="lang-en">Origin &amp; Chemistry of Usar / Reh</span>
                        <span class="lang-hi">ऊसर मृदा की उत्पत्ति एवं रासायनिक स्वरूप</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Causes &amp; Efflorescence:</strong> Faulty surface canal irrigation, waterlogging, poor subsoil drainage, and high evaporation in semi-arid plains bring sodium carbonate, sodium sulphate, and calcium salts to the surface via capillary action, forming a white crust called <strong>Reh (रेह)</strong>. Locally known as <strong>Usar (ऊसर), Kallar, or Chopan</strong>.</span>
                            <span class="lang-hi"><strong>उत्पत्ति व रेह:</strong> अत्यधिक नहरी सिंचाई, जलभराव व उच्च वाष्पीकरण से केशिकीय क्रिया द्वारा सोडियम लवण सतह पर सफेद परत (<strong>रेह/ऊसर</strong>) बना लेते हैं।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Worst-Hit Districts:</strong> Aligarh, Mainpuri, Kanpur, Unnao, Etawah, Rae Bareli, Azamgarh (over 12 lakh hectares affected).</span>
                            <span class="lang-hi"><strong>सर्वाधिक प्रभावित जिले:</strong> अलीगढ़, मैनपुरी, कानपुर, उन्नाव, इटावा, रायबरेली, आजमगढ़ (12 लाख हेक्टेयर प्रभावित)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-wand-magic-sparkles"></i>
                        <span class="lang-en">Reclamation Techniques (सुधार तकनीक)</span>
                        <span class="lang-hi">ऊसर सुधार के उपाय</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Gypsum (जिप्सम):</strong> Neutralizes exchangeable sodium (CaSO4.2H2O)</span>
                        <span class="mindmap-chip"><strong>Iron Pyrites (पायराइट्स):</strong> Reduces high pH</span>
                        <span class="mindmap-chip"><strong>Green Manuring:</strong> Dhaincha (Sesbania) &amp; Sunnhemp cultivation</span>
                        <span class="mindmap-chip"><strong>UP Bhumi Sudhar Nigam:</strong> World Bank aided UP Sodic Lands Reclamation</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Saline-alkaline soils are called Usar or Reh in UP. Gypsum and Pyrites are used for their chemical reclamation!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> लवणीय-क्षारीय मृदा को उप्र में ऊसर या रेह कहते हैं। इसके रासायनिक सुधार हेतु जिप्सम एवं पायराइट्स का प्रयोग किया जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: Bundelkhand Black Soils: Mar & Kabar -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-circle" style="color: #334155;"></i>
                    <span class="lang-en">5. Bundelkhand Black Soils</span>
                    <span class="lang-hi">5. बुंदेलखंड की काली मिट्टी</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">Mar &amp; Kabar</span>
                    <span class="lang-hi">माड़ एवं काबर</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-seedling"></i>
                        <span class="lang-en">Mar (माड़) Soil Characteristics</span>
                        <span class="lang-hi">माड़ (मार) मृदा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Mar (माड़):</strong> Heavy black clayey soil; contains ~60% clay; exhibits high moisture retention; exhibits 'self-ploughing' characteristics (develops wide, deep cracks when dry, expands and turns gummy/sticky when wet); extremely fertile for <strong>Gram (चना), Wheat, and Oilseeds</strong>.</span>
                            <span class="lang-hi"><strong>माड़ मिट्टी:</strong> अत्यधिक चीका (60% क्ले) युक्त काली मृदा; स्वतः जुताई वाली मिट्टी (सूखने पर गहरी दरारें, भीगने पर चिपचिपी); <strong>चना, गेहूं व तिलहन</strong> हेतु अत्यंत उपजाऊ।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-volcano"></i>
                        <span class="lang-en">Kabar (काबर) Soil Characteristics</span>
                        <span class="lang-hi">काबर मृदा की विशेषताएं</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Kabar (काबर):</strong> Dark greyish-black soil; contains slightly less clay than Mar; highly sticky when wet and turns stony hard upon drying; requires timely ploughing at optimal moisture. Found in Jalaun, Jhansi, Hamirpur, and Banda.</span>
                            <span class="lang-hi"><strong>काबर मिट्टी:</strong> गहरे काले-भूरे रंग की मृदा; भीगने पर चिपचिपी और सूखने पर पत्थर जैसी सख्त हो जाती है; जालौन, झांसी, हमीरपुर, बांदा।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Mar and Kabar are the local Bundelkhand names for Black soils (Regur/Black Cotton soil). Highly moisture-retentive!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बुंदेलखंड क्षेत्र में काली कपास मृदा (रेगुर) को स्थानीय रूप से माड़ और काबर कहा जाता है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Bundelkhand & Vindhyan Red Soils: Parwa, Rakar & Bonta -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-gem" style="color: #e11d48;"></i>
                    <span class="lang-en">6. Bundelkhand Red Soils</span>
                    <span class="lang-hi">6. बुंदेलखंड की लाल मिट्टी</span>
                </h4>
                <span class="mindmap-node-tag">
                    <span class="lang-en">Parwa &amp; Rakar</span>
                    <span class="lang-hi">पड़वा, रांकड़ व बोंटा</span>
                </span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-mountain-sun"></i>
                        <span class="lang-en">Parwa, Rakar &amp; Bonta Distinctive Features</span>
                        <span class="lang-hi">पड़वा, रांकड़ एवं बोंटा मृदा के लक्षण</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Parwa / Padwa (पड़वा / पड़ुआ):</strong> Light reddish or yellowish-grey sandy loam; found in Jalaun, Hamirpur, and along coastal Yamuna; fertile for wheat, gram, and jowar when irrigated.</span>
                            <span class="lang-hi"><strong>पड़वा मिट्टी:</strong> हल्के लाल-भूरे रंग की बलुई दोमट मृदा; जालौन व हमीरपुर; सिंचाई द्वारा गेहूं, चना व ज्वार की अच्छी फसल।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Rakar / Raakar (रांकड़):</strong> Coarse, stony, shallow red soil found on eroded hill slopes of Bundelkhand; poor fertility and low organic matter; suitable only for coarse millets (Bajra, Til).</span>
                            <span class="lang-hi"><strong>रांकड़ मिट्टी:</strong> पहाड़ी ढलानों पर पाई जाने वाली कंकड़ीली, छिछली लाल मिट्टी; कम उपजाऊ; मोटे अनाजों (बाजरा, तिल) हेतु प्रयुक्त।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Bonta (बोंटा):</strong> Vindhyan rocky red soil formed by weathering of Vindhyan sandstones in Mirzapur, Sonbhadra, and Chandauli; rich in iron, poor in nitrogen and humus.</span>
                            <span class="lang-hi"><strong>बोंटा मिट्टी:</strong> विंध्य बलुआ पत्थरों के अपक्षय से निर्मित लाल कंकड़ीली मृदा (मिर्जापुर, सोनभद्र, चंदौली)।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Parwa and Rakar are the local names of Red soils in Bundelkhand. Rakar is stony and found on slopes, while Parwa is sandy loam!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> बुंदेलखंड में लाल मिट्टी के स्थानीय नाम पड़वा और रांकड़ हैं। रांकड़ कंकड़ीली-ढलवां मृदा है तथा पड़वा हल्की दोमट मृदा है!</span>
                </div>
            </div>
        </div>
    </div>
</div>
'''

# ==============================================================================
# Topic 22: Wildlife of Uttar Pradesh
# ==============================================================================
mm_wildlife = '''<!-- Card 1: Mind Map -->
<div class="card-premium mindmap-container">
    <div class="mindmap-header">
        <h3 class="theory-heading">
            <i class="fas fa-sitemap" style="color: var(--primary, #059669);"></i>
            <span class="lang-en">Comprehensive Concept Mindmap: Wildlife of Uttar Pradesh</span>
            <span class="lang-hi">विस्तृत संकल्पना माइंडमैप: उत्तर प्रदेश के वन्यजीव, राष्ट्रीय उद्यान एवं अभयारण्य</span>
        </h3>
        <p class="mindmap-subtitle">
            <span class="lang-en">Exhaustive Thematic Flow • 6 Pillars • Dudhwa National Park Profile • 4 Tiger Reserves (Dudhwa, Pilibhit, Amangarh, Ranipur) • 2 Elephant Reserves • 11 Wildlife Sanctuaries (Chandraprabha to Hastinapur) • 14 Bird Sanctuaries (Lakh Bahosi to Patna) • 10 Ramsar Wetland Sites</span>
            <span class="lang-hi">समग्र विषयवार संकल्पना प्रवाह • 6 प्रमुख स्तंभ • दुधवा राष्ट्रीय उद्यान परिदृश्य • 4 बाघ अभयारण्य (दुधवा, पीलीभीत, अमानगढ़, रानीपुर) • 2 हाथी रिजर्व • 11 वन्यजीव अभयारण्य (चंद्रप्रभा से हस्तिनापुर) • 14 पक्षी विहार (लाख बहोसी से पटना) • 10 रामसर आर्द्रभूमियाँ</span>
        </p>
    </div>

    <div class="mindmap-root">
        <div class="mindmap-root-badge">
            <i class="fas fa-paw"></i>
            <span class="lang-en">Faunal Diversity, Protected Area Network &amp; Tiger Reserves of UP</span>
            <span class="lang-hi">उत्तर प्रदेश की वन्यजीव विविधता, संरक्षित क्षेत्र नेटवर्क एवं बाघ अभयारण्य</span>
        </div>
    </div>

    <div class="mindmap-grid">
        <!-- Branch 1: Dudhwa National Park Profile -->
        <div class="mindmap-node epoch-prehistoric">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-tree" style="color: #059669;"></i>
                    <span class="lang-en">1. Dudhwa National Park</span>
                    <span class="lang-hi">1. दुधवा राष्ट्रीय उद्यान (एकमात्र नेशनल पार्क)</span>
                </h4>
                <span class="mindmap-node-tag">Lakhimpur Kheri • Est. 1977</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield-cat"></i>
                        <span class="lang-en">Chronology &amp; Core Habitat</span>
                        <span class="lang-hi">स्थापना क्रम एवं आवास</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Only National Park in UP:</strong> Located in <strong>Lakhimpur Kheri district</strong> along the Indo-Nepal border; covers an area of <strong>490 sq km</strong>. Established as a sanctuary in 1958; upgraded to <strong>National Park on 1 Feb 1977</strong>.</span>
                            <span class="lang-hi"><strong>उप्र का एकमात्र राष्ट्रीय उद्यान:</strong> <strong>लखीमपुर खीरी जिले</strong> में भारत-नेपाल सीमा पर 490 वर्ग किमी में विस्तृत। 1958 में अभयारण्य तथा <strong>1 फरवरी 1977 को राष्ट्रीय उद्यान</strong> बना।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Project Tiger &amp; Dudhwa TR:</strong> Integrated under Project Tiger in <strong>1987</strong> by combining Dudhwa National Park with <strong>Kishanpur Wildlife Sanctuary</strong> (Katarniaghat WLS added in 2000).</span>
                            <span class="lang-hi"><strong>प्रोजेक्ट टाइगर (1987):</strong> 1987 में दुधवा नेशनल पार्क तथा <strong>किशनपुर वन्यजीव विहार</strong> को मिलाकर दुधवा टाइगर रिजर्व बना (2000 में कतरनियाघाट जुड़ा)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Keystone Species:</strong> World-renowned sanctuary for the <strong>Swamp Deer (Barasingha / बारहसिंगा - State Animal)</strong>; Royal Bengal Tiger; Indian One-Horned Rhinoceros (Rhino Reintroduction Project launched here in <strong>1984</strong> by moving rhinos from Kaziranga).</span>
                            <span class="lang-hi"><strong>प्रमुख वन्यजीव:</strong> <strong>बारहसिंगा (राजकीय पशु)</strong> का सबसे बड़ा प्राकृतिक आवास; रॉयल बंगाल टाइगर; <strong>1984 में गैंडा पुनर्वास परियोजना</strong> शुरू की गई।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Dudhwa is the ONLY National Park in UP (declared 1977 in Lakhimpur Kheri). The Rhino Reintroduction Project began in Dudhwa in 1984!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> दुधवा उप्र का एकमात्र राष्ट्रीय उद्यान (1977, लखीमपुर खीरी) है। दुधवा में 1984 में गैंडा पुनर्वास परियोजना शुरू हुई थी!</span>
                </div>
            </div>
        </div>

        <!-- Branch 2: Four Tiger Reserves & Two Elephant Reserves -->
        <div class="mindmap-node epoch-ancient">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-shield-cat" style="color: #0284c7;"></i>
                    <span class="lang-en">2. Tiger &amp; Elephant Reserves</span>
                    <span class="lang-hi">2. चार बाघ अभयारण्य एवं दो हाथी रिजर्व</span>
                </h4>
                <span class="mindmap-node-tag">4 Tiger Reserves • 2 Elephant Reserves</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-cat"></i>
                        <span class="lang-en">The 4 Tiger Reserves of UP</span>
                        <span class="lang-hi">उत्तर प्रदेश के 4 टाइगर रिजर्व</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Dudhwa Tiger Reserve:</strong> Lakhimpur Kheri (Notified 1987)</span>
                        <span class="mindmap-chip"><strong>2. Pilibhit Tiger Reserve:</strong> Pilibhit/Lakhimpur (2014 - won TX2 Award)</span>
                        <span class="mindmap-chip"><strong>3. Amangarh Tiger Reserve:</strong> Bijnor (2012 - Corbett buffer in UP)</span>
                        <span class="mindmap-chip"><strong>4. Ranipur Tiger Reserve:</strong> Chitrakoot (Notified Oct 2022 - India's 53rd TR)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-award"></i>
                        <span class="lang-en">Ranipur &amp; Pilibhit Milestones</span>
                        <span class="lang-hi">रानीपुर एवं पीलीभीत की उपलब्धियां</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Ranipur Tiger Reserve (Chitrakoot):</strong> Declared as <strong>UP's 4th and India's 53rd Tiger Reserve</strong> in October 2022. First tiger reserve in the Bundelkhand region; crucial transit corridor for Panna tigers.</span>
                            <span class="lang-hi"><strong>रानीपुर टाइगर रिजर्व (चित्रकूट):</strong> अक्टूबर 2022 में <strong>उप्र का चौथा और भारत का 53वां टाइगर रिजर्व</strong> घोषित। बुंदेलखंड का पहला टाइगर रिजर्व।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Pilibhit TX2 Award:</strong> Awarded international <strong>TX2 Global Award (2020)</strong> for doubling its wild tiger population from 25 to 65 ahead of the 10-year target.</span>
                            <span class="lang-hi"><strong>पीलीभीत TX2 अवार्ड:</strong> 10 वर्ष के लक्ष्य से पहले बाघों की संख्या 25 से 65 (दोगुनी से अधिक) करने पर 2020 में अंतरराष्ट्रीय TX2 अवार्ड मिला।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield"></i>
                        <span class="lang-en">The 2 Elephant Reserves of UP</span>
                        <span class="lang-hi">2 हाथी रिजर्व</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. UP Elephant Reserve (2009):</strong> Saharanpur &amp; Bijnor foothills</span>
                        <span class="mindmap-chip"><strong>2. Terai Elephant Reserve (TER - 2022):</strong> 3,049 sq km (Lakhimpur/Pilibhit - India's 33rd ER)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Ranipur (Chitrakoot) is UP's 4th Tiger Reserve (notified in 2022). Pilibhit Tiger Reserve won the global TX2 award!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> रानीपुर (चित्रकूट) उप्र का चौथा टाइगर रिजर्व (2022) है। पीलीभीत को बाघ संख्या दोगुनी करने हेतु TX2 अवार्ड मिला!</span>
                </div>
            </div>
        </div>

        <!-- Branch 3: Directory of 11 Wildlife Sanctuaries -->
        <div class="mindmap-node epoch-classical">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-compass" style="color: #7c3aed;"></i>
                    <span class="lang-en">3. 11 Wildlife Sanctuaries</span>
                    <span class="lang-hi">3. 11 वन्यजीव अभयारण्य (Chandraprabha to Hastinapur)</span>
                </h4>
                <span class="mindmap-node-tag">Oldest, Largest &amp; Smallest</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-trophy"></i>
                        <span class="lang-en">Extreme Wildlife Sanctuary Benchmarks</span>
                        <span class="lang-hi">वन्यजीव अभयारण्यों के प्रमुख रिकॉर्ड</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Oldest Sanctuary:</strong> Chandraprabha WLS, Chandauli (Est. 1957)</span>
                        <span class="mindmap-chip"><strong>Largest Sanctuary:</strong> Hastinapur WLS (2,073 sq km across 5 districts)</span>
                        <span class="mindmap-chip"><strong>Smallest Sanctuary:</strong> Mahavir Swami WLS, Lalitpur (5.4 sq km)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-list-check"></i>
                        <span class="lang-en">Complete Directory of Wildlife Sanctuaries</span>
                        <span class="lang-hi">11 वन्यजीव अभयारण्यों की सूची</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>1. Chandraprabha (Chandauli, 1957):</strong> First sanctuary of UP; Rajdari-Devdari falls.</span>
                            <span class="lang-hi"><strong>1. चंद्रप्रभा (चंदौली, 1957):</strong> उप्र का पहला वन्यजीव विहार; राजदारी-देवदारी जलप्रपात।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>2. Kishanpur (Lakhimpur Kheri, 1972):</strong> Core of Dudhwa TR; Swamp deer haven.</span>
                            <span class="lang-hi"><strong>2. किशनपुर (लखीमपुर खीरी, 1972):</strong> दुधवा का भाग; बारहसिंगा संरक्षण।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>3. Katarniaghat (Bahraich, 1976):</strong> Girwa river, Gharial &amp; Gangetic dolphin habitat.</span>
                            <span class="lang-hi"><strong>3. कतरनियाघाट (बहराइच, 1976):</strong> गिरवा नदी, घड़ियाल व डॉल्फिन केंद्र।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>4. Ranipur (Chitrakoot, 1977):</strong> Now Ranipur Tiger Reserve.</span>
                            <span class="lang-hi"><strong>4. रानीपुर (चित्रकूट, 1977):</strong> अब टाइगर रिजर्व।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>5. Mahavir Swami (Lalitpur, 1977):</strong> Smallest in UP (5.4 sq km).</span>
                            <span class="lang-hi"><strong>5. महावीर स्वामी (ललितपुर, 1977):</strong> उप्र का सबसे छोटा विहार (5.4 वर्ग किमी)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>6. National Chambal (Agra/Etawah, 1979):</strong> Tri-state crocodile &amp; skimmer sanctuary.</span>
                            <span class="lang-hi"><strong>6. राष्ट्रीय चंबल (आगरा/इटावा, 1979):</strong> घड़ियाल व मगरमच्छ संरक्षण।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>7. Kaimur (Mirzapur/Sonbhadra, 1982):</strong> Blackbuck and rock paintings.</span>
                            <span class="lang-hi"><strong>7. कैमूर (मिर्जापुर/सोनभद्र, 1982):</strong> काला हिरण व शैलचित्र।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>8. Hastinapur (Meerut/Hapur/Bijnor/Amroha/Muzaffarnagar, 1986):</strong> Largest (2,073 sq km).</span>
                            <span class="lang-hi"><strong>8. हस्तिनापुर (मेरठ/बिजनौर आदि, 1986):</strong> उप्र का सबसे बड़ा विहार (2,073 वर्ग किमी)।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>9. Sohagibarwa (Maharajganj, 1987) &amp; 10. Sohalwa (Balrampur/Gonda/Shravasti, 1988)</strong>.</span>
                            <span class="lang-hi"><strong>9. सोहागीबरवा (महराजगंज) एवं 10. सोहेलवा (बलरामपुर/गोंडा/श्रावस्ती)</strong>।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Chandraprabha (Chandauli, 1957) is the oldest, Hastinapur is the largest (2,073 sq km), and Mahavir Swami (Lalitpur, 5.4 sq km) is the smallest!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> चंद्रप्रभा (चंदौली, 1957) सबसे पहला, हस्तिनापुर सबसे बड़ा (2,073 वर्ग किमी) तथा महावीर स्वामी (ललितपुर, 5.4 वर्ग किमी) सबसे छोटा है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 4: Directory of 14 Bird Sanctuaries (पक्षी अभयारण्य) -->
        <div class="mindmap-node epoch-medieval">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-feather-pointed" style="color: #d97706;"></i>
                    <span class="lang-en">4. 14 Bird Sanctuaries</span>
                    <span class="lang-hi">4. 14 पक्षी विहार (Nawabganj to Patna)</span>
                </h4>
                <span class="mindmap-node-tag">Lakh Bahosi (Largest) • Patna (Smallest)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-crow"></i>
                        <span class="lang-en">Record-Holding Bird Sanctuaries</span>
                        <span class="lang-hi">पक्षी विहारों के प्रमुख कीर्तिमान</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>Oldest Bird Sanctuary:</strong> Nawabganj (Unnao, 1984 - Shahid Azad Bird Sanctuary)</span>
                        <span class="mindmap-chip"><strong>Largest Bird Sanctuary:</strong> Lakh Bahosi (Kannauj, 1988 - 80.24 sq km)</span>
                        <span class="mindmap-chip"><strong>Smallest Bird Sanctuary:</strong> Patna Bird Sanctuary (Etah, 1990 - only 1.09 sq km)</span>
                    </div>
                </div>
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-list-ol"></i>
                        <span class="lang-en">District-wise Bird Sanctuaries Directory</span>
                        <span class="lang-hi">जिलावार पक्षी विहार निर्देशिका</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Samaspur (Raebareli); Sandi (Hardoi); Parvati Arga (Gonda); Saman (Mainpuri); Bakhira (Sant Kabir Nagar); Sur Sarovar / Keetham (Agra); Okhla (Gautam Buddha Nagar); Suraha Tal / Loknayak JP (Ballia); Dr. Bhimrao Ambedkar (Beti, Pratapgarh); Shekha Jheel (Aligarh); Vijaysagar (Mahoba).</strong></span>
                            <span class="lang-hi"><strong>समसपुर (रायबरेली); सांडी (हरदोई); पार्वती अरगा (गोंडा); समान (मैनपुरी); बखिरा (संत कबीर नगर); सूर सरोवर/कीठम (आगरा); ओखला (नोएडा); सुरहा ताल (बलिया); डॉ. आंबेडकर (प्रतापगढ़); शेखा झील (अलीगढ़); विजय सागर (महोबा)।</strong></span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Nawabganj (Unnao) is the oldest bird sanctuary (1984). Lakh Bahosi (Kannauj) is largest (80.24 sq km), and Patna (Etah) is smallest (1.09 sq km)!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> नवाबगंज (उन्नाव) प्रथम पक्षी विहार (1984) है। लाख बहोसी (कन्नौज) सबसे बड़ा तथा पटना पक्षी विहार (एटा, 1.09 वर्ग किमी) सबसे छोटा है!</span>
                </div>
            </div>
        </div>

        <!-- Branch 5: 10 Ramsar Wetland Sites of Uttar Pradesh -->
        <div class="mindmap-node epoch-revolt">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-water-ladder" style="color: #dc2626;"></i>
                    <span class="lang-en">5. 10 Ramsar Wetland Sites</span>
                    <span class="lang-hi">5. उत्तर प्रदेश के 10 रामसर आर्द्रभूमि स्थल</span>
                </h4>
                <span class="mindmap-node-tag">Upper Ganga (2005) to Bakhira (2022)</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-dove"></i>
                        <span class="lang-en">Complete Chronological List of Ramsar Sites</span>
                        <span class="lang-hi">रामसर स्थलों की संपूर्ण कालक्रमानुसार सूची</span>
                    </span>
                    <div class="mindmap-chips">
                        <span class="mindmap-chip"><strong>1. Upper Ganga River:</strong> Brijghat to Narora stretch (Declared 2005 - 1st in UP)</span>
                        <span class="mindmap-chip"><strong>2. Nawabganj Bird Sanctuary:</strong> Unnao (Declared 2019)</span>
                        <span class="mindmap-chip"><strong>3. Samaspur Bird Sanctuary:</strong> Raebareli (2019)</span>
                        <span class="mindmap-chip"><strong>4. Sandi Bird Sanctuary:</strong> Hardoi (2019)</span>
                        <span class="mindmap-chip"><strong>5. Parvati Arga Sanctuary:</strong> Gonda (2019)</span>
                        <span class="mindmap-chip"><strong>6. Saman Bird Sanctuary:</strong> Mainpuri (2019)</span>
                        <span class="mindmap-chip"><strong>7. Sarsai Nawar Jheel:</strong> Etawah (2019 - Sarus crane haven)</span>
                        <span class="mindmap-chip"><strong>8. Sur Sarovar (Keetham Lake):</strong> Agra (2020)</span>
                        <span class="mindmap-chip"><strong>9. Haiderpur Wetland:</strong> Bijnor &amp; Muzaffarnagar (2021)</span>
                        <span class="mindmap-chip"><strong>10. Bakhira Wildlife Sanctuary:</strong> Sant Kabir Nagar (2022 - 10th Ramsar)</span>
                    </div>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> UP has 10 Ramsar wetland sites. Upper Ganga River was the 1st in 2005, Haiderpur was 9th in 2021, and Bakhira was 10th in 2022!</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> उप्र में 10 रामसर स्थल हैं। ऊपरी गंगा प्रथम (2005), हैदरपुर 9वां (2021) तथा बखिरा (संत कबीर नगर) 10वां स्थल (2022) बना!</span>
                </div>
            </div>
        </div>

        <!-- Branch 6: Conservation Projects & Wildlife Institutions -->
        <div class="mindmap-node epoch-modern">
            <div class="mindmap-node-header">
                <h4 class="mindmap-node-title">
                    <i class="fas fa-hand-holding-medical" style="color: #4f46e5;"></i>
                    <span class="lang-en">6. Conservation Projects &amp; Safaris</span>
                    <span class="lang-hi">6. संरक्षण परियोजनाएं, सफारी एवं संस्थान</span>
                </h4>
                <span class="mindmap-node-tag">Lion Safari • Dolphin • Vulture Centre</span>
            </div>
            <div class="mindmap-node-body">
                <div class="mindmap-cluster">
                    <span class="mindmap-cluster-label">
                        <i class="fas fa-shield-heart"></i>
                        <span class="lang-en">Pioneering Conservation Centres in UP</span>
                        <span class="lang-hi">अग्रणी संरक्षण केंद्र एवं सफारी</span>
                    </span>
                    <ul class="mindmap-item-list">
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Etawah Safari Park (Lion Safari):</strong> Located in Fisher Forest (Etawah); houses Asiatic Lion Safari, Deer Safari, Bear Safari, and Leopard Safari.</span>
                            <span class="lang-hi"><strong>इटावा सफारी पार्क (लायन सफारी):</strong> फिशर वन (इटावा) में स्थित; एशियाई शेर, हिरण, भालू व तेंदुआ सफारी।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>Elephant Hospital &amp; Vulture Centre:</strong> India's first <strong>Elephant Hospital</strong> at Farah (Mathura); world-class <strong>Jatayu Vulture Conservation and Breeding Centre</strong> established in Maharajganj district.</span>
                            <span class="lang-hi"><strong>हाथी अस्पताल व गिद्ध संरक्षण केंद्र:</strong> देश का पहला <strong>हाथी अस्पताल</strong> फराह (मथुरा) में; महराजगंज जिले में <strong>जटायु गिद्ध संरक्षण एवं प्रजनन केंद्र</strong>।</span>
                        </li>
                        <li class="mindmap-item">
                            <span class="lang-en"><strong>State Aquatic Animal (Gangetic Dolphin):</strong> Locally called <em>Susu / Saundh</em>; declared UP's State Aquatic Animal (October 2023); protected in Ganga and Katarniaghat (Girwa river).</span>
                            <span class="lang-hi"><strong>गंगा डॉल्फिन ('सोंस'):</strong> अक्टूबर 2023 में उप्र का <strong>राजकीय जलीय जीव</strong> घोषित; गंगा व कतरनियाघाट (गिरवा नदी) में विशेष संरक्षण।</span>
                        </li>
                    </ul>
                </div>
                <div class="mindmap-fact-badge">
                    <span class="lang-en"><strong>UPSSSC Top Note:</strong> Lion Safari is in Etawah, Elephant Hospital is in Mathura, and Jatayu Vulture Conservation Centre is in Maharajganj! Gangetic Dolphin was declared State Aquatic Animal in 2023.</span>
                    <span class="lang-hi"><strong>UPSSSC मुख्य बिंदु:</strong> लायन सफारी इटावा में, हाथी अस्पताल मथुरा में, और जटायु गिद्ध संरक्षण केंद्र महराजगंज में है! गंगा डॉल्फिन 2023 में राजकीय जलीय जीव घोषित हुई।</span>
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
    inject_mindmap('social-customs-and-tourism', mm_tourism)
    inject_mindmap('soil', mm_soil)
    inject_mindmap('wildlife', mm_wildlife)
