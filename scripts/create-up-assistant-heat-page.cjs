const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');

const ROOT = process.cwd();
const sourcePath = path.join(ROOT, 'up-assistant-teacher/science/energy/index.html');
const outputDir = path.join(ROOT, 'up-assistant-teacher/science/heat');
const outputPath = path.join(outputDir, 'index.html');
const b = (en, hi) => ({ en, hi });

const concepts = {
  sections: [
    {
      title: b('Detailed Brief Overview', 'विस्तृत संक्षिप्त अवलोकन'),
      type: 'table',
      headers: [b('Aspect', 'पहलू'), b('Key details', 'मुख्य विवरण')],
      rows: [
        [b('Heat', 'ऊष्मा'), b('Energy transferred from a hotter body to a colder body because of a temperature difference.', 'तापमान के अंतर के कारण अधिक गर्म वस्तु से कम गर्म वस्तु में स्थानांतरित होने वाली ऊर्जा।')],
        [b('Temperature', 'तापमान'), b('A measure of how hot or cold a body is; it determines the direction of heat flow.', 'किसी वस्तु के गर्म या ठंडा होने का माप; इससे ऊष्मा प्रवाह की दिशा निर्धारित होती है।')],
        [b('Thermal equilibrium', 'तापीय साम्य'), b('Bodies in thermal contact stop having net heat flow when they reach the same temperature.', 'तापीय संपर्क में रखी वस्तुओं का तापमान समान होने पर उनके बीच शुद्ध ऊष्मा प्रवाह रुक जाता है।')],
        [b('SI units', 'SI मात्रक'), b('Heat is measured in joules (J); temperature is measured in kelvin (K).', 'ऊष्मा जूल (J) में और तापमान केल्विन (K) में मापा जाता है।')],
        [b('Heat capacity', 'ऊष्मा धारिता'), b('Heat needed to raise the temperature of an entire body by 1 K; unit: J K⁻¹.', 'पूरी वस्तु का तापमान 1 K बढ़ाने के लिए आवश्यक ऊष्मा; मात्रक: J K⁻¹।')],
        [b('Specific heat capacity', 'विशिष्ट ऊष्मा धारिता'), b('Heat needed to raise 1 kg of a substance by 1 K; Q = mcΔT.', 'किसी पदार्थ के 1 kg का तापमान 1 K बढ़ाने के लिए आवश्यक ऊष्मा; Q = mcΔT।')],
        [b('Change of state', 'अवस्था परिवर्तन'), b('During melting or boiling, supplied heat can change the state while temperature stays constant.', 'गलन या क्वथन के दौरान दी गई ऊष्मा अवस्था बदल सकती है, जबकि तापमान स्थिर रहता है।')],
        [b('UP exam focus', 'UP परीक्षा के लिए मुख्य बिंदु'), b('Distinguish heat from temperature; learn transfer modes, units, expansion, and specific/latent heat.', 'ऊष्मा और तापमान का अंतर, ऊष्मा-संचरण की विधियाँ, मात्रक, प्रसार तथा विशिष्ट/गुप्त ऊष्मा समझें।')]
      ]
    },
    {
      title: b('Mind Map', 'माइंड मैप'),
      type: 'list',
      items: [
        { term: b('Thermal energy', 'तापीय ऊर्जा'), definition: b('Temperature difference → heat flows hot to cold → thermal equilibrium.', 'तापमान का अंतर → ऊष्मा गर्म से ठंडे की ओर → तापीय साम्य।') },
        { term: b('Heating effect', 'गर्म करने का प्रभाव'), definition: b('Temperature rise: Q = mcΔT | State change: Q = mL | Expansion: length, area, or volume increases.', 'तापमान वृद्धि: Q = mcΔT | अवस्था परिवर्तन: Q = mL | प्रसार: लंबाई, क्षेत्रफल या आयतन बढ़ता है।') },
        { term: b('Transfer modes: C-C-R', 'संचरण विधियाँ: C-C-R'), definition: b('Conduction: contact, mainly solids | Convection: fluid movement | Radiation: electromagnetic waves, no medium required.', 'चालन: संपर्क, मुख्यतः ठोस | संवहन: द्रव/गैस का प्रवाह | विकिरण: विद्युतचुम्बकीय तरंगें, माध्यम आवश्यक नहीं।') },
        { term: b('Change of state', 'अवस्था परिवर्तन'), definition: b('Solid ⇄ liquid: melting/freezing | Liquid ⇄ gas: vaporisation/condensation | During latent heat, temperature remains constant.', 'ठोस ⇄ द्रव: गलन/जमना | द्रव ⇄ गैस: वाष्पीकरण/संघनन | गुप्त ऊष्मा के दौरान तापमान स्थिर रहता है।') }
      ]
    },
    {
      title: b('Core Concepts and Applications', 'मुख्य अवधारणाएँ एवं अनुप्रयोग'),
      type: 'subcards',
      items: [
        { title: b('Heat vs temperature', 'ऊष्मा और तापमान में अंतर'), content: b('• Heat is energy in transfer; temperature is a state measure.\n• Heat depends on mass, material, and temperature change; temperature alone does not tell total heat.\n• A large cool object can contain more internal energy than a small hot object.\n• Heat naturally flows from higher to lower temperature until equilibrium.', '• ऊष्मा स्थानांतरण में ऊर्जा है; तापमान किसी अवस्था का माप है।\n• ऊष्मा द्रव्यमान, पदार्थ और तापमान परिवर्तन पर निर्भर करती है; केवल तापमान से कुल ऊष्मा ज्ञात नहीं होती।\n• बड़ी ठंडी वस्तु की आंतरिक ऊर्जा छोटी गर्म वस्तु से अधिक हो सकती है।\n• ऊष्मा स्वाभाविक रूप से अधिक तापमान से कम तापमान की ओर बहती है और साम्य पर रुकती है।') },
        { title: b('Temperature scales and measurement', 'तापमान पैमाने एवं मापन'), content: b('• Celsius: water freezes at 0°C and boils at 100°C at standard atmospheric pressure.\n• Kelvin: K = °C + 273.15; 0 K is absolute zero.\n• Fahrenheit conversion: °F = (9/5 × °C) + 32.\n• Clinical thermometers measure human body temperature; laboratory thermometers have a wider range.\n• Read the scale at eye level and note the unit.', '• सेल्सियस: मानक वायुदाब पर पानी 0°C पर जमता और 100°C पर उबलता है।\n• केल्विन: K = °C + 273.15; 0 K परम शून्य है।\n• फारेनहाइट रूपांतरण: °F = (9/5 × °C) + 32।\n• क्लिनिकल थर्मामीटर शरीर का तापमान मापता है; प्रयोगशाला थर्मामीटर की परास अधिक होती है।\n• पैमाना आँख के स्तर पर पढ़ें और मात्रक लिखें।') },
        { title: b('Conduction, convection, radiation', 'चालन, संवहन एवं विकिरण'), content: b('• Conduction transfers energy through particle interactions without bulk movement; metals are generally good conductors.\n• Convection transfers heat by bulk movement in liquids and gases; warm, less-dense fluid rises.\n• Radiation transfers energy by electromagnetic waves and works through a vacuum.\n• The Sun warms Earth mainly by radiation.\n• Dark, dull surfaces absorb and emit radiant heat better than light, polished surfaces.', '• चालन में कणों की परस्पर क्रिया से ऊर्जा स्थानांतरित होती है, पर पदार्थ का समष्टिगत प्रवाह नहीं होता; धातुएँ सामान्यतः अच्छी चालक हैं।\n• संवहन में द्रव या गैस का समष्टिगत प्रवाह ऊष्मा ले जाता है; गर्म और कम घनत्व वाला द्रव ऊपर उठता है।\n• विकिरण विद्युतचुम्बकीय तरंगों से ऊर्जा पहुँचाता है और निर्वात में भी संभव है।\n• सूर्य पृथ्वी को मुख्यतः विकिरण से गर्म करता है।\n• काली, खुरदरी सतहें हल्की, चमकदार सतहों से बेहतर ऊष्मा अवशोषित और उत्सर्जित करती हैं।') },
        { title: b('Specific heat and latent heat', 'विशिष्ट ऊष्मा एवं गुप्त ऊष्मा'), content: b('• Q = mcΔT: Q in joules, m in kg, c in J kg⁻¹ K⁻¹, and ΔT in K or °C.\n• Water has a high specific heat capacity, so it warms and cools relatively slowly.\n• Q = mL during a state change; L is specific latent heat in J kg⁻¹.\n• Latent heat changes particle arrangement, not temperature, during the phase change.\n• Do not confuse heat capacity (whole body) with specific heat capacity (per unit mass).', '• Q = mcΔT: Q जूल में, m kg में, c J kg⁻¹ K⁻¹ में और ΔT K या °C में।\n• पानी की विशिष्ट ऊष्मा धारिता अधिक है, इसलिए वह अपेक्षाकृत धीरे गर्म और ठंडा होता है।\n• अवस्था परिवर्तन में Q = mL; L विशिष्ट गुप्त ऊष्मा (J kg⁻¹) है।\n• गुप्त ऊष्मा अवस्था परिवर्तन के दौरान कणों की व्यवस्था बदलती है, तापमान नहीं।\n• ऊष्मा धारिता (पूरी वस्तु) और विशिष्ट ऊष्मा धारिता (प्रति इकाई द्रव्यमान) को न मिलाएँ।') },
        { title: b('Thermal expansion and water anomaly', 'तापीय प्रसार एवं जल का असामान्य व्यवहार'), content: b('• Most substances expand on heating and contract on cooling.\n• Expansion is usually greatest in gases and least in solids.\n• Expansion joints in bridges and gaps in railway tracks allow safe expansion.\n• Water is densest at about 4°C; between 0°C and 4°C it contracts on warming.\n• Ice is less dense than liquid water and floats, helping aquatic life survive in cold conditions.', '• अधिकांश पदार्थ गर्म करने पर फैलते और ठंडा करने पर सिकुड़ते हैं।\n• सामान्यतः गैसों में प्रसार सबसे अधिक और ठोसों में सबसे कम होता है।\n• पुलों के विस्तार-जोड़ और रेल-पटरियों के अंतराल सुरक्षित प्रसार की जगह देते हैं।\n• पानी का घनत्व लगभग 4°C पर अधिकतम होता है; 0°C से 4°C तक गर्म करने पर वह सिकुड़ता है।\n• बर्फ का घनत्व द्रव पानी से कम होता है, इसलिए वह तैरती है और ठंड में जलीय जीवन को सहारा देती है।') },
        { title: b('Everyday applications', 'दैनिक जीवन में उपयोग'), content: b('• Wool and air trapped in blankets reduce heat loss; they do not produce heat.\n• Ventilators are placed high because warm air rises by convection.\n• A thermos reduces conduction, convection, and radiation using insulation, a vacuum gap, and reflective surfaces.\n• Sea breeze and land breeze arise from unequal heating and convection.\n• A metal spoon feels colder than a wooden spoon at the same room temperature because metal conducts heat away from the hand faster.', '• कंबल में फँसी हवा ऊष्मा-हानि घटाती है; ऊन स्वयं ऊष्मा उत्पन्न नहीं करती।\n• गर्म हवा संवहन से ऊपर उठती है, इसलिए रोशनदान ऊँचाई पर लगाए जाते हैं।\n• थर्मस में कुचालक परत, निर्वात और परावर्तक सतहें चालन, संवहन और विकिरण घटाती हैं।\n• समुद्री और स्थलीय समीर असमान गर्मी तथा संवहन से बनते हैं।\n• समान कमरे के तापमान पर धातु का चम्मच लकड़ी से ठंडा लगता है क्योंकि धातु हाथ से ऊष्मा तेजी से ले जाती है।') }
      ]
    },
    {
      title: b('Formulae and Quick Comparisons', 'सूत्र एवं त्वरित तुलना'),
      type: 'table',
      headers: [b('Quantity / process', 'राशि / प्रक्रिया'), b('Relation or unit', 'संबंध या मात्रक'), b('Exam check', 'परीक्षा में जाँच')],
      rows: [
        [b('Sensible heating', 'तापमान परिवर्तन'), b('Q = mcΔT', 'Q = mcΔT'), b('Use temperature change; no phase change.', 'तापमान परिवर्तन हो; अवस्था परिवर्तन न हो।')],
        [b('State change', 'अवस्था परिवर्तन'), b('Q = mL', 'Q = mL'), b('Temperature stays constant during the change.', 'परिवर्तन के दौरान तापमान स्थिर रहता है।')],
        [b('Celsius to kelvin', 'सेल्सियस से केल्विन'), b('K = °C + 273.15', 'K = °C + 273.15'), b('Kelvin is never written with a degree sign.', 'केल्विन के साथ डिग्री चिह्न नहीं लगाते।')],
        [b('Celsius to Fahrenheit', 'सेल्सियस से फारेनहाइट'), b('°F = (9/5 × °C) + 32', '°F = (9/5 × °C) + 32'), b('At 0°C, the reading is 32°F.', '0°C पर मान 32°F होता है।')],
        [b('Conduction', 'चालन'), b('Particle-to-particle transfer', 'कण से कण ऊर्जा-संचरण'), b('No bulk flow; common in solids.', 'समष्टिगत प्रवाह नहीं; ठोसों में सामान्य।')],
        [b('Convection', 'संवहन'), b('Bulk movement of fluid', 'द्रव का समष्टिगत प्रवाह'), b('Requires a liquid or gas.', 'द्रव या गैस आवश्यक है।')],
        [b('Radiation', 'विकिरण'), b('Electromagnetic waves', 'विद्युतचुम्बकीय तरंगें'), b('No material medium required.', 'भौतिक माध्यम आवश्यक नहीं।')],
        [b('Water anomaly', 'जल का असामान्य प्रसार'), b('Maximum density near 4°C', 'लगभग 4°C पर अधिकतम घनत्व'), b('Ice floats because it is less dense.', 'बर्फ कम घनत्व के कारण तैरती है।')]
      ]
    },
    {
      title: b('Memory Tricks and Mnemonics', 'स्मरण-युक्तियाँ एवं स्मृति-सूत्र'),
      type: 'list',
      items: [
        { term: b('C-C-R: transfer modes', 'C-C-R: ऊष्मा-संचरण'), definition: b('Conduction = Contact; Convection = Circulation; Radiation = Rays. Use the first letters to recall the three modes.', 'Conduction = Contact (संपर्क); Convection = Circulation (प्रवाह); Radiation = Rays (किरणें)। तीनों विधियाँ इसी क्रम से याद रखें।') },
        { term: b('“mcΔT” means mass × material × change', '“mcΔT” का संकेत'), definition: b('For Q = mcΔT, check mass (m), the material property specific heat (c), and temperature change (ΔT).', 'Q = mcΔT में द्रव्यमान (m), पदार्थ का विशिष्ट गुण (c) और तापमान परिवर्तन (ΔT) जाँचें।') },
        { term: b('Latent = hidden', 'Latent = छिपी हुई'), definition: b('Latent heat is “hidden” in the state change: energy is used, but the thermometer reading pauses during the change.', 'अवस्था बदलने में गुप्त ऊष्मा “छिपी” रहती है: ऊर्जा लगती है, पर परिवर्तन के समय थर्मामीटर का मान स्थिर रहता है।') },
        { term: b('Vacuum blocks C and C, not R', 'निर्वात C और C रोकता है, R नहीं'), definition: b('A vacuum prevents conduction and convection; radiation can still cross it. This explains how solar heat reaches Earth.', 'निर्वात चालन और संवहन रोकता है; विकिरण फिर भी गुजर सकता है। इसी से सूर्य की ऊष्मा पृथ्वी तक पहुँचती है।') }
      ]
    },
    {
      title: b('Common Mistakes to Avoid', 'सामान्य गलतियाँ जिनसे बचें'),
      type: 'list',
      items: [
        { term: b('Calling heat and temperature the same', 'ऊष्मा और तापमान को समान मानना'), definition: b('Heat is transferred energy; temperature is a measure of thermal state. Keep the definitions separate.', 'ऊष्मा स्थानांतरित ऊर्जा है; तापमान तापीय अवस्था का माप है। दोनों परिभाषाएँ अलग रखें।') },
        { term: b('Assuming every heat input raises temperature', 'हर ऊष्मा से तापमान बढ़ना मानना'), definition: b('During melting or boiling, energy can change state while temperature remains constant.', 'गलन या क्वथन के दौरान ऊर्जा अवस्था बदल सकती है और तापमान स्थिर रह सकता है।') },
        { term: b('Saying convection occurs in solids', 'ठोसों में संवहन मानना'), definition: b('Convection requires bulk movement of a fluid; solids mainly transfer heat by conduction.', 'संवहन के लिए द्रव का समष्टिगत प्रवाह चाहिए; ठोसों में ऊष्मा मुख्यतः चालन से जाती है।') },
        { term: b('Requiring a medium for radiation', 'विकिरण के लिए माध्यम आवश्यक मानना'), definition: b('Radiation can transfer heat through a vacuum; conduction and convection cannot.', 'विकिरण निर्वात में ऊष्मा पहुँचा सकता है; चालन और संवहन नहीं।') },
        { term: b('Mixing heat capacity and specific heat', 'ऊष्मा धारिता और विशिष्ट ऊष्मा मिलाना'), definition: b('Heat capacity refers to the whole object; specific heat capacity is per unit mass.', 'ऊष्मा धारिता पूरी वस्तु की है; विशिष्ट ऊष्मा धारिता प्रति इकाई द्रव्यमान की।') },
        { term: b('Using the wrong unit', 'गलत मात्रक लगाना'), definition: b('Heat: joule; temperature: kelvin or °C; specific heat: J kg⁻¹ K⁻¹; latent heat: J kg⁻¹.', 'ऊष्मा: जूल; तापमान: केल्विन या °C; विशिष्ट ऊष्मा: J kg⁻¹ K⁻¹; गुप्त ऊष्मा: J kg⁻¹।') }
      ]
    },
    {
      title: b('Point-wise Revision Summary', 'बिंदुवार पुनरावृत्ति-सार'),
      type: 'list',
      items: [
        { term: b('Direction', 'दिशा'), definition: b('Net heat flows from higher temperature to lower temperature until thermal equilibrium.', 'शुद्ध ऊष्मा अधिक तापमान से कम तापमान की ओर बहती है और तापीय साम्य पर रुकती है।') },
        { term: b('Heat is energy transfer', 'ऊष्मा ऊर्जा-संचरण है'), definition: b('A body does not “contain heat” in the strict physics sense; it has internal energy and can transfer energy as heat.', 'भौतिकी के सटीक अर्थ में वस्तु “ऊष्मा रखती” नहीं; उसमें आंतरिक ऊर्जा होती है और वह ऊष्मा के रूप में ऊर्जा दे सकती है।') },
        { term: b('Three transfer modes', 'संचरण की तीन विधियाँ'), definition: b('Conduction, convection, and radiation differ by mechanism and whether a medium is required.', 'चालन, संवहन और विकिरण अपनी प्रक्रिया तथा माध्यम की आवश्यकता में अलग हैं।') },
        { term: b('Specific heat relation', 'विशिष्ट ऊष्मा संबंध'), definition: b('Use Q = mcΔT when temperature changes without a phase change.', 'बिना अवस्था परिवर्तन के तापमान बदलने पर Q = mcΔT लगाएँ।') },
        { term: b('Latent heat relation', 'गुप्त ऊष्मा संबंध'), definition: b('Use Q = mL for a phase change at constant temperature.', 'स्थिर तापमान पर अवस्था परिवर्तन के लिए Q = mL लगाएँ।') },
        { term: b('Water at 4°C', '4°C पर पानी'), definition: b('Water has maximum density near 4°C; ice is less dense and floats.', 'पानी का घनत्व लगभग 4°C पर अधिकतम होता है; बर्फ कम घनत्व से तैरती है।') },
        { term: b('Insulation', 'ऊष्मारोधन'), definition: b('Insulators slow heat transfer; trapped air is an effective insulator in many everyday materials.', 'ऊष्मारोधक पदार्थ ऊष्मा-संचरण धीमा करते हैं; कई दैनिक वस्तुओं में फँसी हवा प्रभावी ऊष्मारोधक है।') },
        { term: b('Temperature conversion', 'तापमान रूपांतरण'), definition: b('K = °C + 273.15 and °F = (9/5 × °C) + 32.', 'K = °C + 273.15 तथा °F = (9/5 × °C) + 32।') }
      ]
    }
  ],
  upscNotes: [
    { type: 'tip', content: b('For numerical questions, write the known values, convert mass to kg, and state the final unit.', 'संख्यात्मक प्रश्नों में दिए मान लिखें, द्रव्यमान kg में बदलें और उत्तर का मात्रक अवश्य लिखें।') },
    { type: 'tip', content: b('First decide whether temperature changes or the substance changes state; this selects mcΔT or mL.', 'पहले तय करें कि तापमान बदलेगा या पदार्थ की अवस्था; इससे mcΔT या mL सूत्र चुनेगा।') },
    { type: 'trap', content: b('A vacuum stops conduction and convection, but not radiation.', 'निर्वात चालन और संवहन रोकता है, पर विकिरण नहीं।') },
    { type: 'trap', content: b('During a phase change, supplied heat does not necessarily raise temperature.', 'अवस्था परिवर्तन के दौरान दी गई ऊष्मा से तापमान आवश्यक रूप से नहीं बढ़ता।') },
    { type: 'tip', content: b('Use the Sun, a metal spoon, and a boiling pot to recall radiation, conduction, and convection respectively.', 'विकिरण, चालन और संवहन याद रखने के लिए क्रमशः सूर्य, धातु का चम्मच और उबलते बर्तन का उदाहरण लें।') }
  ],
  keyTakeaways: [
    b('Heat is energy transferred because of a temperature difference.', 'तापमान के अंतर से स्थानांतरित ऊर्जा ऊष्मा है।'),
    b('Temperature indicates thermal state; it is not the same as heat.', 'तापमान तापीय अवस्था बताता है; यह ऊष्मा के समान नहीं है।'),
    b('Conduction, convection, and radiation are the three main transfer modes.', 'चालन, संवहन और विकिरण ऊष्मा-संचरण की तीन मुख्य विधियाँ हैं।'),
    b('Use Q = mcΔT for temperature change and Q = mL for a phase change.', 'तापमान परिवर्तन के लिए Q = mcΔT और अवस्था परिवर्तन के लिए Q = mL लगाएँ।'),
    b('Water is densest near 4°C; ice floats because it is less dense.', 'पानी का घनत्व लगभग 4°C पर अधिकतम है; बर्फ कम घनत्व के कारण तैरती है।'),
    b('Check the physical process and units before selecting a formula.', 'सूत्र चुनने से पहले भौतिक प्रक्रिया और मात्रक जाँचें।')
  ]
};

function encodeScriptJson(value) {
  return JSON.stringify(value, null, 2).replace(/</g, '\\u003c');
}

function main() {
  if (!fs.existsSync(sourcePath)) throw new Error('Science Energy reference page is missing.');
  if (fs.existsSync(outputPath)) throw new Error('Heat page already exists; refusing to overwrite it.');

  let html = fs.readFileSync(sourcePath, 'utf8');
  html = html
    .replaceAll('/up-assistant-teacher/science/energy/', '/up-assistant-teacher/science/heat/')
    .replaceAll('up-assistant-teacher.science.energy', 'up-assistant-teacher.science.heat')
    .replaceAll('Energy - forms of energy, conservation of energy, kinetic and potential energy, work and power.', 'Heat - temperature, thermal expansion, specific heat, latent heat, change of state, and transfer by conduction, convection, and radiation.')
    .replaceAll('Energy', 'Heat')
    .replaceAll('ऊर्जा', 'ऊष्मा');

  const scriptPattern = /(<script\b[^>]*\bid=["']upsc-page-data["'][^>]*>)([\s\S]*?)(<\/script>)/i;
  const match = html.match(scriptPattern);
  if (!match) throw new Error('Reference page has no embedded upsc-page-data script.');

  const pageData = JSON.parse(match[2]);
  pageData.topicId = 'up-assistant-teacher.science.heat';
  pageData.topicName = 'Heat';
  pageData.hindiName = 'ऊष्मा';
  pageData.subject = 'Science';
  pageData.subjectDir = 'science';
  pageData.concepts = concepts;
  pageData.contentHash = `sha256-${crypto.createHash('sha256').update(JSON.stringify(concepts)).digest('hex')}`;
  pageData.generatedAt = new Date().toISOString();
  html = html.replace(scriptPattern, () => `${match[1]}\n${encodeScriptJson(pageData)}\n${match[3]}`);

  fs.mkdirSync(outputDir, { recursive: true });
  fs.writeFileSync(outputPath, html, 'utf8');
  execFileSync(process.execPath, [path.join(ROOT, 'scripts/prerender-seo-content.cjs'), '--scope=up-assistant-teacher/science/heat'], { cwd: ROOT, stdio: 'inherit' });
  console.log(`Created bilingual Heat notes in ${path.relative(ROOT, outputPath)}.`);
}

main();
