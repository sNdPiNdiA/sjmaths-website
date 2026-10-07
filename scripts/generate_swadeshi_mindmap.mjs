import fs from 'fs';
import path from 'path';
import { chromium } from 'playwright';
import { execSync } from 'child_process';

const OUTPUT_DIR = path.resolve('upsssc-pet/history/swadeshi-civil-disobedience-gandhi');

// Helper to wrap text
function getHtmlTemplate(lang, layout) {
  const isEn = lang === 'en';
  const isLandscape = layout === 'landscape';

  const title = isEn 
    ? 'SWADESHI & CIVIL DISOBEDIENCE MOVEMENT' 
    : 'स्वदेशी एवं सविनय अवज्ञा आंदोलन (गांधी युग)';
  const subtitle = isEn 
    ? 'UPSSSC PET History Mind Map + Mnemonics' 
    : 'UPSSSC PET इतिहास माइंड मैप + स्मृति सूत्र (Mnemonics)';
  const centerTitle = isEn 
    ? 'Gandhian Era &<br>Mass Movements<br><span style="font-size:0.75em; color:#d97706;">(1905–1934)</span>' 
    : 'गांधी युग एवं<br>जनांदोलन<br><span style="font-size:0.75em; color:#d97706;">(1905–1934)</span>';

  // 8 modules data
  const m1 = isEn ? {
    num: '1',
    title: '1905 Swadeshi & Boycott Movement',
    color: '#dc2626',
    bg: '#fef2f2',
    border: '#fca5a5',
    icon: 'fa-fire',
    bullets: [
      '<strong>Trigger:</strong> Lord Curzon announced <strong>Partition of Bengal</strong> on 20 July 1905 (Effective: 16 Oct 1905).',
      '<strong>Proclamation:</strong> Formal boycott announced on <strong>7 Aug 1905</strong> at Town Hall, Calcutta.',
      '<strong>Day of Mourning:</strong> 16 Oct observed with bath in Ganges, fasts & <strong>Raksha Bandhan</strong> (Tagore).',
      '<strong>Key Figures:</strong> Lal-Bal-Pal, Aurobindo Ghosh; Tagore composed <em>Amar Sonar Bangla</em>.',
      '<strong>Institutions:</strong> National Council of Education (1906), Bengal National College.',
      '<strong>Result:</strong> Partition annulled in <strong>1911</strong> by Lord Hardinge II (Delhi Durbar).'
    ],
    mnemonicTitle: 'Mnemonic: BARE',
    mnemonicText: '= <strong>B</strong>oycott, <strong>A</strong>tmasakti, <strong>R</strong>aksha Bandhan, <strong>E</strong>ducation'
  } : {
    num: '1',
    title: '1905 स्वदेशी एवं बहिष्कार आंदोलन',
    color: '#dc2626',
    bg: '#fef2f2',
    border: '#fca5a5',
    icon: 'fa-fire',
    bullets: [
      '<strong>कारण:</strong> लॉर्ड कर्जन द्वारा <strong>बंगाल विभाजन</strong> की घोषणा (20 जुलाई 1905; प्रभावी: 16 अक्टूबर 1905)।',
      '<strong>औपचारिक घोषणा:</strong> <strong>7 अगस्त 1905</strong> को कलकत्ता टाउन हॉल में स्वदेशी व बहिष्कार का प्रस्ताव।',
      '<strong>शोक दिवस:</strong> 16 अक्टूबर को गंगा स्नान, उपवास और <strong>रक्षाबंधन</strong> दिवस (टैगोर) के रूप में मनाया गया।',
      '<strong>प्रमुख नेता:</strong> लाल-बाल-पाल, अरविंद घोष; रवींद्रनाथ टैगोर ने <em>अमार शोनार बांग्ला</em> रचा।',
      '<strong>राष्ट्रीय संस्थाएँ:</strong> राष्ट्रीय शिक्षा परिषद (1906), बंगाल नेशनल कॉलेज (प्रधानाचार्य: अरविंद घोष)।',
      '<strong>परिणाम:</strong> <strong>1911</strong> में लॉर्ड हार्डिंग द्वितीय द्वारा दिल्ली दरबार में विभाजन रद्द।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: BARE',
    mnemonicText: '= <strong>B</strong>oycott (बहिष्कार), <strong>A</strong>tmasakti (आत्मशक्ति), <strong>R</strong>aksha Bandhan, <strong>E</strong>ducation'
  };

  const m2 = isEn ? {
    num: '2',
    title: 'Surat Split & Lucknow Reunion',
    color: '#059669',
    bg: '#ecfdf5',
    border: '#6ee7b7',
    icon: 'fa-code-branch',
    bullets: [
      '<strong>1906 Calcutta Session:</strong> Dadabhai Naoroji proclaimed goal of <strong>Swaraj</strong>, Swadeshi & Boycott.',
      '<strong>1907 Surat Split:</strong> INC split on Tapi river bank; President: Rash Behari Ghosh; Extremists expelled.',
      '<strong>1909 Morley-Minto Reforms:</strong> Introduced separate electorates for Muslims.',
      '<strong>1916 Lucknow Session:</strong> Presided by A.C. Mazumdar; Moderates & Extremists reunited.',
      '<strong>1916 Lucknow Pact:</strong> Historic alliance between Congress & Muslim League.',
      '<strong>Home Rule Leagues:</strong> Tilak (Poona/Maharashtra) & Annie Besant (Madras/All India).'
    ],
    mnemonicTitle: 'Mnemonic: SPLIT-7',
    mnemonicText: '= <strong>S</strong>urat <strong>P</strong>arty <strong>L</strong>eaders <strong>I</strong>n <strong>T</strong>wo in 190<strong>7</strong>'
  } : {
    num: '2',
    title: 'सूरत विभाजन एवं लखनऊ पुनर्मिलन',
    color: '#059669',
    bg: '#ecfdf5',
    border: '#6ee7b7',
    icon: 'fa-code-branch',
    bullets: [
      '<strong>1906 कलकत्ता अधिवेशन:</strong> दादाभाई नौरोजी की अध्यक्षता में पहली बार <strong>स्वराज</strong> का लक्ष्य घोषित।',
      '<strong>1907 सूरत विभाजन:</strong> ताप्ती नदी तट पर कांग्रेस दो धड़ों में विभाजित; अध्यक्ष: रास बिहारी घोष; गरमदल निष्कासित।',
      '<strong>1909 मार्ले-मिंटो सुधार:</strong> मुसलमानों के लिए पृथक निर्वाचक मंडल की शुरुआत।',
      '<strong>1916 लखनऊ अधिवेशन:</strong> अंबिका चरण मजूमदार अध्यक्ष; नरमदल और गरमदल का ऐतिहासिक पुनर्मिलन।',
      '<strong>लखनऊ समझौता:</strong> कांग्रेस और मुस्लिम लीग के बीच संयुक्त राजनीतिक समझौता।',
      '<strong>होमरूल आंदोलन:</strong> तिलक (पुणे/महाराष्ट्र) और एनी बेसेंट (मद्रास/अखिल भारतीय)।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: SPLIT-7',
    mnemonicText: '= <strong>S</strong>urat <strong>P</strong>arty <strong>L</strong>eaders <strong>I</strong>n <strong>T</strong>wo in 190<strong>7</strong>'
  };

  const m3 = isEn ? {
    num: '3',
    title: "Gandhi's Early Satyagrahas (1915–18)",
    color: '#2563eb',
    bg: '#eff6ff',
    border: '#93c5fd',
    icon: 'fa-user-tie',
    bullets: [
      '<strong>Arrival:</strong> 9 Jan 1915 (Pravasi Bharatiya Divas) from South Africa; Mentor: G.K. Gokhale.',
      '<strong>Ashram:</strong> Sabarmati Ashram founded near Ahmedabad (1915-16).',
      '<strong>1917 Champaran (Bihar):</strong> 1st Civil Disobedience; against <em>Tinkathia</em> (3/20 indigo); Raj Kumar Shukla invited Gandhi.',
      '<strong>1918 Ahmedabad Mill Strike:</strong> 1st Hunger Strike; plague bonus dispute (35% wage hike won); Anasuya Sarabhai.',
      '<strong>1918 Kheda Satyagraha:</strong> 1st Non-Cooperation; tax remission for crop failure; supported by Sardar Patel.'
    ],
    mnemonicTitle: 'Mnemonic: CAK',
    mnemonicText: '= <strong>C</strong>hamparan (1917) &rarr; <strong>A</strong>hmedabad (1918) &rarr; <strong>K</strong>heda (1918)'
  } : {
    num: '3',
    title: 'गांधीजी के आरंभिक सत्याग्रह (1915–18)',
    color: '#2563eb',
    bg: '#eff6ff',
    border: '#93c5fd',
    icon: 'fa-user-tie',
    bullets: [
      '<strong>भारत आगमन:</strong> 9 जनवरी 1915 (प्रवासी भारतीय दिवस); राजनीतिक गुरु: गोपाल कृष्ण गोखले।',
      '<strong>आश्रम:</strong> अहमदाबाद में साबरमती आश्रम की स्थापना (1915-16)।',
      '<strong>1917 चंपारण (बिहार):</strong> प्रथम सविनय अवज्ञा; <em>तीनकठिया</em> (3/20 नील) प्रथा के विरुद्ध; राजकुमार शुक्ल ने आमंत्रित किया।',
      '<strong>1918 अहमदाबाद मिल हड़ताल:</strong> प्रथम भूख हड़ताल; प्लेग बोनस विवाद (35% मजदूरी वृद्धि सफल); अनुसूया साराभाई।',
      '<strong>1918 खेड़ा सत्याग्रह:</strong> प्रथम असहयोग; फसल नष्ट होने पर कर माफी (सरदार वल्लभभाई पटेल का सहयोग)।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: CAK',
    mnemonicText: '= <strong>C</strong>hamparan (1917) &rarr; <strong>A</strong>hmedabad (1918) &rarr; <strong>K</strong>heda (1918)'
  };

  const m4 = isEn ? {
    num: '4',
    title: 'Rowlatt Act & Jallianwala Bagh (1919)',
    color: '#d97706',
    bg: '#fffbeb',
    border: '#fcd34d',
    icon: 'fa-landmark',
    bullets: [
      '<strong>Rowlatt Act (March 1919):</strong> Black Act; detention without trial ("No Dalil, No Vakil, No Appeal").',
      '<strong>Rowlatt Satyagraha:</strong> Nationwide hartal called by Gandhi on 6 April 1919.',
      '<strong>13 April 1919 (Baisakhi):</strong> Jallianwala Bagh Massacre; Gen. Dyer fired on unarmed crowd protesting arrest of Dr. Kitchlew & Dr. Satyapal.',
      '<strong>Renunciation:</strong> Tagore gave up <strong>Knighthood</strong>; Gandhi returned <em>Kaisar-i-Hind</em> gold medal.',
      '<strong>Hunter Commission:</strong> Appointed to inquire into massacre; Dyer exonerated by House of Lords.'
    ],
    mnemonicTitle: 'Mnemonic: R-J-H',
    mnemonicText: '= <strong>R</strong>owlatt Act &rarr; <strong>J</strong>allianwala Bagh &rarr; <strong>H</strong>unter Commission'
  } : {
    num: '4',
    title: 'रौलट एक्ट एवं जलियांवाला बाग (1919)',
    color: '#d97706',
    bg: '#fffbeb',
    border: '#fcd34d',
    icon: 'fa-landmark',
    bullets: [
      '<strong>रौलट एक्ट (मार्च 1919):</strong> काला कानून; बिना मुकदमे जेल ("ना कोई दलील, ना वकील, ना अपील")।',
      '<strong>रौलट सत्याग्रह:</strong> गांधीजी के आह्वान पर 6 अप्रैल 1919 को देशव्यापी हड़ताल।',
      '<strong>13 अप्रैल 1919 (बैसाखी):</strong> जलियांवाला बाग हत्याकांड; डॉ. किचलू व डॉ. सत्यपाल की गिरफ्तारी के विरोध में सभा पर जनरल डायर की गोलीबारी।',
      '<strong>उपाधि त्याग:</strong> रवींद्रनाथ टैगोर ने <strong>नाइटहुड</strong> और गांधीजी ने <em>कैसर-ए-हिंद</em> पदक लौटाया।',
      '<strong>हंटर आयोग:</strong> हत्याकांड की जांच हेतु गठित सरकारी आयोग; डायर को केवल सेवामुक्त किया गया।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: R-J-H',
    mnemonicText: '= <strong>R</strong>owlatt Act &rarr; <strong>J</strong>allianwala Bagh &rarr; <strong>H</strong>unter Commission'
  };

  const m5 = isEn ? {
    num: '5',
    title: 'Non-Cooperation Movement (1920–22)',
    color: '#7c3aed',
    bg: '#f5f3ff',
    border: '#c4b5fd',
    icon: 'fa-hands-holding-circle',
    bullets: [
      '<strong>Khilafat Cause:</strong> Ali Brothers (Mohammad & Shaukat Ali) for Ottoman Caliph; Gandhi elected All-India Khilafat President.',
      '<strong>Launch:</strong> 1 Aug 1920 (Tilak passed away); <strong>Tilak Swaraj Fund</strong> raised &gt;&yen;1 Crore.',
      '<strong>Ratification:</strong> Special Calcutta session (Sept 1920) & Nagpur session (Dec 1920, C. Vijayaraghavachariar).',
      '<strong>Actions:</strong> Boycott of titles, courts, colleges, foreign cloth; Charkha adopted as national symbol.',
      '<strong>Chauri Chaura (4 Feb 1922):</strong> Mob burnt police station in Gorakhpur (22 policemen died).',
      '<strong>Suspension:</strong> Gandhi suspended movement via <strong>Bardoli Resolution</strong> (12 Feb 1922); jailed for 6 yrs.'
    ],
    mnemonicTitle: 'Mnemonic: K-T-N-B',
    mnemonicText: '= <strong>K</strong>hilafat &rarr; <strong>T</strong>ilak Fund &rarr; <strong>N</strong>on-Cooperation &rarr; <strong>B</strong>ardoli Halt'
  } : {
    num: '5',
    title: 'असहयोग एवं खिलाफत आंदोलन (1920–22)',
    color: '#7c3aed',
    bg: '#f5f3ff',
    border: '#c4b5fd',
    icon: 'fa-hands-holding-circle',
    bullets: [
      '<strong>खिलाफत मुद्दा:</strong> तुर्की के खलीफा के समर्थन में अली बंधु (शौकत अली, मुहम्मद अली); गांधीजी अध्यक्ष बने।',
      '<strong>शुरुआत:</strong> 1 अगस्त 1920 (तिलक जी का निधन); <strong>तिलक स्वराज फंड</strong> में ₹1 करोड़ से अधिक जुटाए गए।',
      '<strong>स्वीकृति:</strong> कलकत्ता विशेष सत्र (लाजपत राय) व नागपुर सत्र (दिसंबर 1920, सी. विजयराघवाचार्यार)।',
      '<strong>कार्यक्रम:</strong> उपाधियों का त्याग, अदालतों/विदेशी कपड़ों का बहिष्कार, चरखा व खादी को राष्ट्रीय प्रतीक बनाना।',
      '<strong>चौरी-चौरा कांड (4 फरवरी 1922):</strong> गोरखपुर में उग्र भीड़ ने थाना फूंका (22 पुलिसकर्मी मारे गए)।',
      '<strong>स्थगन:</strong> गांधीजी ने 12 फरवरी 1922 को <strong>बारदोली प्रस्ताव</strong> द्वारा आंदोलन वापस लिया; 6 वर्ष की जेल।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: K-T-N-B',
    mnemonicText: '= <strong>K</strong>hilafat &rarr; <strong>T</strong>ilak Fund &rarr; <strong>N</strong>on-Cooperation &rarr; <strong>B</strong>ardoli Halt'
  };

  const m6 = isEn ? {
    num: '6',
    title: 'Swaraj Party to Purna Swaraj (1923–29)',
    color: '#be123c',
    bg: '#fff1f2',
    border: '#fda4af',
    icon: 'fa-flag-checkered',
    bullets: [
      '<strong>Swaraj Party (Jan 1923):</strong> C.R. Das (President) & Motilal Nehru (Secy) entered legislative councils.',
      '<strong>Simon Commission (1927-28):</strong> All-white 7-member statutory commission; slogan: "Simon Go Back".',
      '<strong>Martyrdom:</strong> Lala Lajpat Rai fatally lathi-charged in Lahore (17 Nov 1928).',
      '<strong>Nehru Report (1928):</strong> Motilal Nehru framed constitution demanding Dominion Status; Jinnah gave 14 Points.',
      '<strong>Lahore Session (Dec 1929):</strong> Jawaharlal Nehru president; <strong>Purna Swaraj</strong> (Complete Independence) passed.',
      '<strong>26 Jan 1930:</strong> Observed as India\'s 1st Independence Day; Tricolor unfurled on Ravi bank (31 Dec 1929).'
    ],
    mnemonicTitle: 'Mnemonic: S-S-N-L',
    mnemonicText: '= <strong>S</strong>warajists &rarr; <strong>S</strong>imon &rarr; <strong>N</strong>ehru Report &rarr; <strong>L</strong>ahore Purna Swaraj'
  } : {
    num: '6',
    title: 'स्वराज पार्टी से पूर्ण स्वराज तक (1923–29)',
    color: '#be123c',
    bg: '#fff1f2',
    border: '#fda4af',
    icon: 'fa-flag-checkered',
    bullets: [
      '<strong>स्वराज पार्टी (जनवरी 1923):</strong> सी.आर. दास (अध्यक्ष) और मोतीलाल नेहरू (सचिव) द्वारा विधान परिषदों में प्रवेश हेतु।',
      '<strong>साइमन कमीशन (1927-28):</strong> 7 सदस्यीय श्वेत आयोग; देशव्यापी बहिष्कार: "साइमन वापस जाओ"।',
      '<strong>लालाजी का बलिदान:</strong> लाहौर में लाठीचार्ज से घायल होकर लाला लाजपत राय शहीद (17 नवंबर 1928)।',
      '<strong>नेहरू रिपोर्ट (1928):</strong> मोतीलाल नेहरू द्वारा संविधान प्रारूप तैयार; डोमिनियन स्टेट्स की मांग।',
      '<strong>लाहौर अधिवेशन (दिसंबर 1929):</strong> पं. जवाहरलाल नेहरू अध्यक्ष; ऐतिहासिक <strong>पूर्ण स्वराज</strong> प्रस्ताव पारित।',
      '<strong>26 जनवरी 1930:</strong> प्रथम स्वतंत्रता दिवस के रूप में मनाया गया; 31 दिसंबर 1929 को रावी तट पर तिरंगा फहराया।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: S-S-N-L',
    mnemonicText: '= <strong>S</strong>warajists &rarr; <strong>S</strong>imon &rarr; <strong>N</strong>ehru Report &rarr; <strong>L</strong>ahore Purna Swaraj'
  };

  const m7 = isEn ? {
    num: '7',
    title: 'Civil Disobedience & Dandi March (1930)',
    color: '#0284c7',
    bg: '#f0f9ff',
    border: '#7dd3fc',
    icon: 'fa-person-walking',
    bullets: [
      '<strong>Dandi March:</strong> 12 March – 6 April 1930 (24 days); <strong>78 followers</strong>; 240 miles from Sabarmati to Dandi.',
      '<strong>Salt Law Broken:</strong> On <strong>6 April 1930</strong>, Gandhi picked a fistful of salt, launching Civil Disobedience.',
      '<strong>Tamil Nadu:</strong> C. Rajagopalachari led Vedaranyam Salt March (Trichy to Vedaranyam).',
      '<strong>Kerala / Malabar:</strong> K. Kelappan led Payyanur march; <strong>Assam:</strong> Sylhet to Noakhali.',
      '<strong>NWFP (Frontier Gandhi):</strong> Khan Abdul Ghaffar Khan & <em>Khudai Khidmatgars</em> ("Red Shirts").',
      '<strong>Dharasana Raid:</strong> Sarojini Naidu, Imam Saheb & Manilal Gandhi faced brutal police lathi charges.'
    ],
    mnemonicTitle: 'Mnemonic: DANDI-78',
    mnemonicText: '= <strong>12 Mar–6 Apr</strong> | <strong>78</strong> Followers | <strong>240</strong> Miles | <strong>6 Apr</strong> Salt Law Broken'
  } : {
    num: '7',
    title: 'सविनय अवज्ञा एवं दांडी मार्च (1930)',
    color: '#0284c7',
    bg: '#f0f9ff',
    border: '#7dd3fc',
    icon: 'fa-person-walking',
    bullets: [
      '<strong>दांडी मार्च:</strong> 12 मार्च – 6 अप्रैल 1930 (24 दिन); <strong>78 सत्याग्रही</strong>; साबरमती से दांडी (240 मील / 385 किमी)।',
      '<strong>नमक कानून तोड़ा:</strong> <strong>6 अप्रैल 1930</strong> को गांधीजी ने मुट्ठी भर नमक बनाकर सविनय अवज्ञा का शंखनाद किया।',
      '<strong>तमिलनाडु:</strong> सी. राजगोपालाचारी ने त्रिची से वेदारण्यम तक नमक यात्रा निकाली।',
      '<strong>केरल / मालाबार:</strong> के. केलप्पन ने कालीकट से पय्यन्नूर तक मार्च किया।',
      '<strong>उत्तर-पश्चिम सीमांत:</strong> खान अब्दुल गफ्फार खान ("सीमांत गांधी") व <em>खुदाई खिदमतगार</em> ("लाल कुर्ती" दल)।',
      '<strong>धरासना सत्याग्रह:</strong> सरोजिनी नायडू, इमाम साहब व मणिलाल गांधी ने अहिंसक लाठीचार्ज झेला।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: DANDI-78',
    mnemonicText: '= <strong>12 मार्च–6 अप्रैल</strong> | <strong>78</strong> अनुयायी | <strong>240</strong> मील | <strong>6 अप्रैल</strong> नमक कानून तोड़ा'
  };

  const m8 = isEn ? {
    num: '8',
    title: 'Round Table Conferences & Poona Pact',
    color: '#15803d',
    bg: '#f0fdf4',
    border: '#86efac',
    icon: 'fa-scale-balanced',
    bullets: [
      '<strong>Gandhi-Irwin Pact (5 March 1931):</strong> Delhi Pact; suspension of CDM; Congress agreed to attend 2nd RTC.',
      '<strong>Karachi Session (March 1931):</strong> Sardar Patel president; passed resolutions on <strong>Fundamental Rights</strong> & Economy.',
      '<strong>Round Table Conferences (London):</strong> 1st (1930) boycotted; 2nd (1931) Gandhi attended; 3rd (1932); Dr. Ambedkar attended ALL THREE.',
      '<strong>Communal Award (16 Aug 1932):</strong> Ramsay MacDonald granted separate electorates to Depressed Classes.',
      '<strong>Poona Pact (24 Sept 1932):</strong> Signed by Dr. Ambedkar & M.M. Malaviya (for Gandhi in Yerwada jail); reserved seats increased from 71 to 148.'
    ],
    mnemonicTitle: 'Mnemonic: G-K-P',
    mnemonicText: '= <strong>G</strong>andhi-Irwin (1931) &rarr; <strong>K</strong>arachi Rights (1931) &rarr; <strong>P</strong>oona Pact (1932)'
  } : {
    num: '8',
    title: 'गोलमेज सम्मेलन एवं पूना पैक्ट (1931–32)',
    color: '#15803d',
    bg: '#f0fdf4',
    border: '#86efac',
    icon: 'fa-scale-balanced',
    bullets: [
      '<strong>गांधी-इरविन समझौता (5 मार्च 1931):</strong> दिल्ली समझौता; सविनय अवज्ञा स्थगित; कांग्रेस द्वितीय गोलमेज में शामिल होने पर सहमत।',
      '<strong>कराची अधिवेशन (मार्च 1931):</strong> सरदार पटेल अध्यक्ष; <strong>मूल अधिकार</strong> एवं राष्ट्रीय आर्थिक कार्यक्रम का प्रस्ताव पारित।',
      '<strong>गोलमेज सम्मेलन (लंदन):</strong> प्रथम (1930) बहिष्कार; द्वितीय (1931) गांधीजी शामिल; तृतीय (1932); डॉ. आंबेडकर तीनों सम्मेलनों में उपस्थित रहे।',
      '<strong>सांप्रदायिक पंचाट (16 अगस्त 1932):</strong> रैम्जे मैकडोनाल्ड द्वारा दलितों को पृथक निर्वाचक मंडल।',
      '<strong>पूना पैक्ट (24 सितंबर 1932):</strong> यरवदा जेल में गांधीजी के अनशन पर डॉ. आंबेडकर व मालवीय जी में समझौता; दलितों की आरक्षित सीटें 71 से बढ़कर 148।'
    ],
    mnemonicTitle: 'स्मृति सूत्र: G-K-P',
    mnemonicText: '= <strong>G</strong>andhi-Irwin (1931) &rarr; <strong>K</strong>arachi (1931) &rarr; <strong>P</strong>oona Pact (1932)'
  };

  const modules = [m1, m2, m3, m4, m5, m6, m7, m8];

  function renderCard(m) {
    const bulletsHtml = m.bullets.map(b => `
      <div style="display:flex; align-items:flex-start; margin-bottom:4px; font-size:${isLandscape ? '11px' : '13px'}; line-height:1.35; color:#1e293b;">
        <span style="display:inline-block; width:6px; height:6px; background:${m.color}; border-radius:50%; margin-top:5px; margin-right:6px; flex-shrink:0;"></span>
        <div>${b}</div>
      </div>
    `).join('');

    return `
      <div style="background:${m.bg}; border:1.5px solid ${m.border}; border-radius:12px; padding:${isLandscape ? '10px 12px' : '14px 16px'}; box-shadow:0 2px 6px rgba(0,0,0,0.04); display:flex; flex-direction:column; justify-content:space-between; position:relative; overflow:hidden;">
        <div>
          <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px; border-bottom:1.5px solid ${m.border}; padding-bottom:5px;">
            <div style="display:flex; align-items:center; gap:6px;">
              <span style="display:inline-flex; align-items:center; justify-content:center; width:${isLandscape ? '22px' : '26px'}; height:${isLandscape ? '22px' : '26px'}; background:${m.color}; color:#fff; border-radius:50%; font-weight:800; font-size:${isLandscape ? '12px' : '14px'};">${m.num}</span>
              <h3 style="margin:0; font-size:${isLandscape ? '13px' : '16px'}; font-weight:800; color:${m.color}; font-family:'Outfit', sans-serif;">${m.title}</h3>
            </div>
            <i class="fas ${m.icon}" style="color:${m.color}; font-size:${isLandscape ? '14px' : '18px'}; opacity:0.8;"></i>
          </div>
          <div>${bulletsHtml}</div>
        </div>
        <div style="background:#fef9c3; border:1px solid #fde047; border-radius:6px; padding:${isLandscape ? '4px 8px' : '6px 10px'}; margin-top:6px; font-size:${isLandscape ? '10.5px' : '12.5px'}; color:#854d0e; font-weight:600; line-height:1.25;">
          <span style="color:#b45309; font-weight:800;">${m.mnemonicTitle}:</span> ${m.mnemonicText}
        </div>
      </div>
    `;
  }

  // HTML Layout structure
  if (isLandscape) {
    // 1600 x 900 Desktop
    return `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="UTF-8">
<title>${title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1600px;
    height: 900px;
    overflow: hidden;
    background: radial-gradient(circle at 50% 50%, #ffffff 0%, #f8fafc 50%, #f1f5f9 100%);
    font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
    color: #0f172a;
    position: relative;
    padding: 16px 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .header-bar {
    text-align: center;
    position: relative;
    padding-bottom: 8px;
    border-bottom: 2px solid #e2e8f0;
  }
  .main-title {
    font-size: 27px;
    font-weight: 900;
    letter-spacing: -0.5px;
    color: #1e3a8a;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }
  .subtitle-pill {
    display: inline-block;
    background: #fef08a;
    border: 1.5px solid #eab308;
    color: #854d0e;
    font-size: 13px;
    font-weight: 800;
    padding: 3px 14px;
    border-radius: 9999px;
    margin-top: 4px;
    letter-spacing: 0.3px;
  }
  .grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr;
    gap: 12px;
    height: 770px;
    position: relative;
  }
  .center-hub {
    grid-column: 2 / 3;
    grid-row: 2 / 3;
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 50%, #eff6ff 100%);
    border: 2.5px solid #0284c7;
    border-radius: 20px;
    box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.15), 0 8px 10px -6px rgba(2, 132, 199, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 12px;
    position: relative;
    z-index: 10;
  }
  .hub-flag {
    width: 60px;
    height: 38px;
    background: linear-gradient(180deg, #ff9933 33.3%, #ffffff 33.3%, #ffffff 66.6%, #138808 66.6%);
    border-radius: 4px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.15);
    margin-bottom: 8px;
    position: relative;
    border: 1px solid #cbd5e1;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .hub-chakra {
    width: 12px;
    height: 12px;
    border: 1.5px solid #000080;
    border-radius: 50%;
  }
  .hub-title {
    font-size: 21px;
    font-weight: 900;
    color: #0f172a;
    line-height: 1.2;
    margin-bottom: 6px;
  }
  .hub-badge {
    background: #1e3a8a;
    color: #ffffff;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 12px;
    display: inline-flex;
    align-items: center;
    gap: 5px;
  }
  .footer-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    color: #64748b;
    font-weight: 600;
    padding-top: 4px;
    border-top: 1px solid #e2e8f0;
  }
</style>
</head>
<body>
  <div class="header-bar">
    <div class="main-title">
      <i class="fas fa-landmark" style="color:#dc2626;"></i>
      <span>${title}</span>
      <i class="fas fa-feather-pointed" style="color:#0284c7;"></i>
    </div>
    <br>
    <div class="subtitle-pill"><i class="fas fa-brain"></i> ${subtitle}</div>
  </div>

  <div class="grid-container">
    <!-- Top Row: Module 1, Module 2, Module 4 -->
    <div style="grid-column: 1 / 2; grid-row: 1 / 2;">${renderCard(m1)}</div>
    <div style="grid-column: 2 / 3; grid-row: 1 / 2;">${renderCard(m2)}</div>
    <div style="grid-column: 3 / 4; grid-row: 1 / 2;">${renderCard(m4)}</div>

    <!-- Middle Row: Module 3, Center Hub, Module 7 -->
    <div style="grid-column: 1 / 2; grid-row: 2 / 3;">${renderCard(m3)}</div>
    
    <div class="center-hub">
      <div class="hub-flag"><div class="hub-chakra"></div></div>
      <div class="hub-title">${centerTitle}</div>
      <div style="font-size:12px; color:#475569; font-weight:700; margin-bottom:8px;">
        <i class="fas fa-quote-left" style="color:#d97706; font-size:10px;"></i>
        ${isEn ? 'Swaraj is my birthright & I shall have it' : 'स्वराज मेरा जन्मसिद्ध अधिकार है और मैं इसे लेकर रहूँगा'}
        <i class="fas fa-quote-right" style="color:#d97706; font-size:10px;"></i>
      </div>
      <div class="hub-badge">
        <i class="fas fa-shield-halved"></i>
        ${isEn ? 'Complete Chronology & Exam Facts' : 'सम्पूर्ण कालक्रम एवं परीक्षा उपयोगी तथ्य'}
      </div>
    </div>

    <div style="grid-column: 3 / 4; grid-row: 2 / 3;">${renderCard(m7)}</div>

    <!-- Bottom Row: Module 5, Module 6, Module 8 -->
    <div style="grid-column: 1 / 2; grid-row: 3 / 4;">${renderCard(m5)}</div>
    <div style="grid-column: 2 / 3; grid-row: 3 / 4;">${renderCard(m6)}</div>
    <div style="grid-column: 3 / 4; grid-row: 3 / 4;">${renderCard(m8)}</div>
  </div>

  <div class="footer-row">
    <span><i class="fas fa-check-circle" style="color:#16a34a;"></i> 100% Comprehensive Coverage for UPSSSC PET, UP Teaching & State PSCs</span>
    <span style="font-weight:800; color:#1e3a8a;"><i class="fas fa-globe"></i> sjmaths.com</span>
  </div>
</body>
</html>`;
  } else {
    // 1080 x 1920 Mobile Portrait
    return `<!DOCTYPE html>
<html lang="${lang}">
<head>
<meta charset="UTF-8">
<title>${title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&family=Noto+Sans+Devanagari:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px;
    height: 1920px;
    overflow: hidden;
    background: radial-gradient(circle at 50% 20%, #ffffff 0%, #f8fafc 40%, #f1f5f9 100%);
    font-family: 'Outfit', 'Noto Sans Devanagari', sans-serif;
    color: #0f172a;
    padding: 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .header-bar {
    text-align: center;
    padding-bottom: 12px;
    border-bottom: 2px solid #e2e8f0;
  }
  .main-title {
    font-size: 32px;
    font-weight: 900;
    color: #1e3a8a;
    text-transform: uppercase;
    display: inline-flex;
    align-items: center;
    gap: 12px;
  }
  .subtitle-pill {
    display: inline-block;
    background: #fef08a;
    border: 2px solid #eab308;
    color: #854d0e;
    font-size: 16px;
    font-weight: 800;
    padding: 4px 18px;
    border-radius: 9999px;
    margin-top: 6px;
  }
  .hub-banner {
    background: linear-gradient(135deg, #ffffff 0%, #f0fdf4 50%, #eff6ff 100%);
    border: 2px solid #0284c7;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(2, 132, 199, 0.12);
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 24px;
    margin-top: 10px;
    margin-bottom: 12px;
  }
  .cards-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 12px;
    flex: 1;
    overflow: hidden;
  }
  .footer-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 14px;
    color: #64748b;
    font-weight: 600;
    padding-top: 8px;
    border-top: 2px solid #e2e8f0;
  }
</style>
</head>
<body>
  <div class="header-bar">
    <div class="main-title">
      <i class="fas fa-landmark" style="color:#dc2626;"></i>
      <span>${title}</span>
    </div>
    <br>
    <div class="subtitle-pill"><i class="fas fa-brain"></i> ${subtitle}</div>
  </div>

  <div class="hub-banner">
    <div style="display:flex; align-items:center; gap:16px;">
      <div style="width:48px; height:32px; background:linear-gradient(180deg, #ff9933 33.3%, #ffffff 33.3%, #ffffff 66.6%, #138808 66.6%); border-radius:4px; border:1px solid #cbd5e1; display:flex; align-items:center; justify-content:center;">
        <div style="width:10px; height:10px; border:1px solid #000080; border-radius:50%;"></div>
      </div>
      <div>
        <div style="font-size:18px; font-weight:900; color:#0f172a;">${centerTitle.replace('<br>', ' ').replace('<br>', ' ')}</div>
        <div style="font-size:13px; color:#475569; font-weight:600;">${isEn ? 'From 1905 Swadeshi to 1930 Dandi Salt March & Poona Pact' : '1905 के स्वदेशी आंदोलन से 1930 दांडी मार्च व पूना पैक्ट तक'}</div>
      </div>
    </div>
    <div style="background:#1e3a8a; color:#fff; font-size:13px; font-weight:800; padding:6px 14px; border-radius:12px;">
      <i class="fas fa-shield-halved"></i> 8 Core Modules
    </div>
  </div>

  <div class="cards-grid">
    ${modules.map(m => renderCard(m)).join('')}
  </div>

  <div class="footer-row">
    <span><i class="fas fa-check-circle" style="color:#16a34a;"></i> 100% Comprehensive Coverage for UPSSSC PET, UP Teaching & State PSCs</span>
    <span style="font-weight:800; color:#1e3a8a; font-size:16px;"><i class="fas fa-globe"></i> sjmaths.com</span>
  </div>
</body>
</html>`;
  }
}

async function main() {
  console.log('Generating HTML files and capturing with Playwright...');
  
  const tmpDir = path.resolve('temp_mindmaps');
  if (!fs.existsSync(tmpDir)) fs.mkdirSync(tmpDir, { recursive: true });

  const tasks = [
    { lang: 'en', layout: 'landscape', width: 1600, height: 900, outName: 'swadeshi-civil-disobedience-english-1600' },
    { lang: 'en', layout: 'portrait', width: 1080, height: 1920, outName: 'swadeshi-civil-disobedience-english-9x16-1080x1920' },
    { lang: 'hi', layout: 'landscape', width: 1600, height: 900, outName: 'swadeshi-civil-disobedience-hindi-1600' },
    { lang: 'hi', layout: 'portrait', width: 1080, height: 1920, outName: 'swadeshi-civil-disobedience-hindi-9x16-1080x1920' }
  ];

  const browser = await chromium.launch({ headless: true });

  for (const t of tasks) {
    const html = getHtmlTemplate(t.lang, t.layout);
    const htmlFile = path.join(tmpDir, `${t.outName}.html`);
    fs.writeFileSync(htmlFile, html, 'utf8');

    const page = await browser.newPage({
      viewport: { width: t.width, height: t.height },
      deviceScaleFactor: 1
    });

    await page.goto(`file://${htmlFile.replace(/\\/g, '/')}`, { waitUntil: 'networkidle' });
    // Wait for fonts to finish rendering
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(500);

    const pngFile = path.join(tmpDir, `${t.outName}.png`);
    await page.screenshot({ path: pngFile, type: 'png' });
    await page.close();

    console.log(`Captured PNG: ${pngFile}`);

    // Convert to high-quality WebP using Python PIL
    const destWebp = path.join(OUTPUT_DIR, `${t.outName}.webp`);
    execSync(`python -c "from PIL import Image; img = Image.open(r'${pngFile}'); img.save(r'${destWebp}', 'WEBP', quality=92, method=6)"`);
    console.log(`Generated WebP: ${destWebp} (${fs.statSync(destWebp).size} bytes)`);
  }

  await browser.close();

  // Clean up temp
  fs.rmSync(tmpDir, { recursive: true, force: true });
  console.log('✅ All 4 Mind Map WebP images generated successfully!');
}

main().catch(err => {
  console.error('Error generating mindmaps:', err);
  process.exit(1);
});
